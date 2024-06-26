import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import uuid
from models.base_model import BaseModel  # Ensure you import your BaseModel class correctly
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
@unittest.skip("demonstrating skipping")
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Setup for tests"""
        self.model = BaseModel()
        
    @patch('models.storage')
    def test_init(self, mock_storage):
        """Test initialization of BaseModel"""
        mock_storage.new.assert_called_once_with(self.model)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)
    
    @patch('models.storage')
    def test_init_with_kwargs(self, mock_storage):
        """Test initialization with kwargs"""
        kwargs = {
            'id': '1234',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'test'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.name, 'test')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertFalse(mock_storage.new.called)
    
    def test_str(self):
        """Test __str__ method"""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)
    
    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)
        mock_storage.save.assert_called_once()
    
    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
