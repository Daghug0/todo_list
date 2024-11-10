import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import unittest.mock
import pymongo
import pymongo.errors

from src.api.database_manager import DataBaseManager

class TestDataBaseManager(unittest.TestCase):

    def test_connection_closed_on_exit(self):
        with DataBaseManager() as db_manager:
            client = db_manager.client
            self.assertTrue(client.is_primary)
        with self.assertRaises(pymongo.errors.InvalidOperation):
            client.server_info()
    
    def test_separate_collections(self):
        db_manager = DataBaseManager()
        self.assertIsNotNone(db_manager.tasks_collection)
        self.assertIsNotNone(db_manager.collaborators_collection)
        self.assertNotEqual(db_manager.tasks_collection, db_manager.collaborators_collection)
        self.assertEqual(db_manager.tasks_collection.name, 'tasks')
        self.assertEqual(db_manager.collaborators_collection.name, 'collaborators')
    def test_connection_failure(self):
        with unittest.mock.patch('pymongo.MongoClient') as mock_client:
            mock_client.side_effect = pymongo.errors.ConnectionFailure("Connection failed")
            
            with self.assertRaises(SystemExit) as cm:
                DataBaseManager()
            
            self.assertEqual(str(cm.exception), "Connection failed")

    def test_database_not_found(self):
        with unittest.mock.patch('pymongo.MongoClient') as mock_client:
            mock_client.return_value.__getitem__.side_effect = pymongo.errors.InvalidName("Database not found")
            
            with self.assertRaises(SystemExit) as cm:
                DataBaseManager()
            
            self.assertEqual(str(cm.exception), "Database not found")   
    
    def test_collections_not_found(self):
        with unittest.mock.patch('pymongo.MongoClient') as mock_client:
            mock_db = unittest.mock.MagicMock()
            mock_client.return_value.__getitem__.return_value = mock_db
            mock_db.__getitem__.side_effect = pymongo.errors.InvalidName("Collection not found")
            
            with self.assertRaises(SystemExit) as cm:
                DataBaseManager()
            
            self.assertEqual(str(cm.exception), "Collection not found")
    
    def test_mongodb_connection_parameters(self):
        with unittest.mock.patch('pymongo.MongoClient') as mock_client:
            DataBaseManager()
            mock_client.assert_called_once_with("localhost", 27017)

if __name__ == '__main__':
    unittest.main()
