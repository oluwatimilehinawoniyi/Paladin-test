import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        """test the instance of the BaseModel class"""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_to_dict(self):
        """test that it returns a dictionary"""
        instance = BaseModel()
        value = instance.to_dict()
        self.assertIsInstance(value, dict)


if __name__ == "__main__":
    unittest.main()
