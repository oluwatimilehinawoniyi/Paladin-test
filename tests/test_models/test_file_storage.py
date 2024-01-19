import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_storage_name(self):
        """test the name of the file storage"""
        store = FileStorage()
        value = store.all()
        self.assertIsInstance(value, dict)


if __name__ == "__main__":
    unittest.main()
