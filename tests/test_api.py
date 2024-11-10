import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import unittest.mock
import pymongo

from src.api.database_manager import DataBaseManager

class TestDataBaseManager(unittest.TestCase):

    def test_connection_closed_on_destruction(self):
        db_manager = DataBaseManager()
        client = db_manager.client
        self.assertTrue(client.is_primary)
        del db_manager
        self.assertFalse(client.is_primary)
    
    def test_separate_collections(self):
        db_manager = DataBaseManager()
        self.assertIsNotNone(db_manager.tasks_collection)
        self.assertIsNotNone(db_manager.collaborators_collection)
        self.assertNotEqual(db_manager.tasks_collection, db_manager.collaborators_collection)
        self.assertEqual(db_manager.tasks_collection.name, 'tasks')
        self.assertEqual(db_manager.collaborators_collection.name, 'collaborators')

    def test_tasks_collection_creation_error(self):
        with unittest.mock.patch('pymongo.MongoClient') as mock_client:
            mock_db = unittest.mock.Mock()
            mock_client.return_value.todolist = mock_db
            mock_db.tasks = unittest.mock.Mock(side_effect=pymongo.errors.CollectionInvalid("Unable to create collection"))
            
            with self.assertRaises(pymongo.errors.CollectionInvalid):
                DataBaseManager()
    

if __name__ == '__main__':
    unittest.main()
