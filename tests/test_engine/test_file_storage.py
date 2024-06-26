import unittest
import json
import os
import sys

# Adjust the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test new method"""
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.file_path, "r") as f:
            obj_dict = json.load(f)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, obj_dict)

    def test_reload(self):
        """Test reload method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
