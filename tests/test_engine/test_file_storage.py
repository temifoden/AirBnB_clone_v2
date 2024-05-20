import unittest
from unittest.mock import patch, mock_open, MagicMock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test case environment."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """Clean up after tests."""
        FileStorage._FileStorage__objects = {}
    
    def test_all(self):
        """Test that all() returns the __objects dictionary."""
        self.assertEqual(self.storage.all(), {f"BaseModel.{self.model.id}": self.model})
    
    def test_new(self):
        """Test that new() adds an object to __objects."""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(f"BaseModel.{new_model.id}", self.storage.all())
        self.assertEqual(self.storage.all()[f"BaseModel.{new_model.id}"], new_model)
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("models.engine.file_storage.FileStorage.save")
    def test_save(self, mock_save, mock_open):
        """Test that save() serializes __objects to JSON file."""
        self.storage.save()
        mock_open.assert_called_once_with(FileStorage._FileStorage__file_path, 'w')
        handle = mock_open()
        handle.write.assert_called_once_with(
            json.dumps({f"BaseModel.{self.model.id}": self.model.to_dict()})
        )
    
    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234"}}')
    def test_reload(self, mock_open):
        """Test that reload() deserializes JSON file to __objects."""
        with patch("json.load", return_value={"BaseModel.1234": {"__class__": "BaseModel", "id": "1234"}}):
            self.storage.reload()
        self.assertIn("BaseModel.1234", self.storage.all())
        self.assertIsInstance(self.storage.all()["BaseModel.1234"], BaseModel)

    @patch("builtins.open", new_callable=mock_open)
    def test_reload_no_file(self, mock_open):
        """Test that reload() handles file not found error."""
        mock_open.side_effect = FileNotFoundError
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

if __name__ == "__main__":
    unittest.main()
