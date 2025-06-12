import unittest
from unittest.mock import patch, MagicMock
from models.article import Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.article_data = {
            "code": "A001",
            "name": "Test Article",
            "description": "A test article",
            "price": 10.5,
            "quantity": 100,
            "category": "TestCat",
            "storage_where": "Shelf 1",
            "last_modified": "2024-06-01",
            "id": 1
        }
        self.article = Article(**self.article_data)

    @patch("models.article.get_database_connection")
    def test_create_article(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        Article.create(self.article)

        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_get_by_id_found(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (
            self.article_data["id"],
            self.article_data["code"],
            self.article_data["name"],
            self.article_data["description"],
            self.article_data["price"],
            self.article_data["quantity"],
            self.article_data["category"],
            self.article_data["storage_where"],
            self.article_data["last_modified"]
        )

        result = Article.get_by_id(1)
        self.assertIsInstance(result, Article)
        self.assertEqual(result.code, self.article_data["code"])
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_get_by_id_not_found(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        result = Article.get_by_id(999)
        self.assertIsNone(result)
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_get_all(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        rows = [
            (
                self.article_data["id"],
                self.article_data["code"],
                self.article_data["name"],
                self.article_data["description"],
                self.article_data["price"],
                self.article_data["quantity"],
                self.article_data["category"],
                self.article_data["storage_where"],
                self.article_data["last_modified"]
            ),
            None
        ]
        mock_cursor.fetchone.side_effect = rows

        articles = list(Article.get_all())
        self.assertEqual(len(articles), 1)
        self.assertIsInstance(articles[0], Article)
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_update_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 1

        result = Article.update(self.article)
        self.assertTrue(result)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_update_not_found(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 0

        result = Article.update(self.article)
        self.assertFalse(result)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_delete_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 1

        result = Article.delete(1)
        self.assertTrue(result)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("models.article.get_database_connection")
    def test_delete_not_found(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 0

        result = Article.delete(999)
        self.assertFalse(result)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()