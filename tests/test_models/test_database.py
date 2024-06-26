import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of BaseModel"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        model_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        updated_at = created_at
        model = BaseModel(id=model_id, created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.id, model_id)
        self.assertEqual(model.created_at.isoformat(), created_at)
        self.assertEqual(model.updated_at.isoformat(), updated_at)

    def test_str(self):
        """Test __str__ method"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
