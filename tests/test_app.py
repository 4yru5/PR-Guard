import unittest
from unittest.mock import patch

import app


class TestApp(unittest.TestCase):
    def test_get_user_uses_parameterized_query(self):
        with patch("app.sqlite3.connect") as mock_connect:
            mock_cursor = mock_connect.return_value.execute.return_value
            mock_cursor.fetchall.return_value = [(1, "alice")]

            result = app.get_user("1")

            self.assertEqual(result, [{"id": 1, "name": "alice"}])
            mock_connect.return_value.execute.assert_called_once_with(
                "SELECT * FROM users WHERE id = ?",
                (1,),
            )

    def test_get_user_rejects_invalid_id(self):
        with patch("app.sqlite3.connect") as mock_connect:
            result = app.get_user("abc")

            self.assertEqual(result, [])
            mock_connect.assert_not_called()


if __name__ == "__main__":
    unittest.main()
