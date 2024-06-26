import unittest
import MySQLdb
import os
from console import HBNBCommand
from models.base_model import BaseModel  # Ensure you import your BaseModel class correctly

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Establish a connection to the MySQL database
        cls.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            user=os.getenv('HBNB_MYSQL_USER', 'hbnb_test'),
            passwd=os.getenv('HBNB_MYSQL_PWD', 'hbnb_test_pwd'),
            db=os.getenv('HBNB_MYSQL_DB', 'hbnb_test_db')
        )
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.cursor.close()
        cls.db.close()

    def setUp(self):
        # Get the initial number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        self.initial_count = self.cursor.fetchone()[0]

    def test_create_state(self):
        # Perform the action: execute the console command to create a new state
        HBNBCommand().onecmd('create State name="California"')

        # Get the new number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Assert the difference is +1
        self.assertEqual(new_count, self.initial_count + 1)

if __name__ == '__main__':
    unittest.main()
