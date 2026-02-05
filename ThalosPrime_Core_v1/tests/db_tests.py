"""
Thalos Prime - Database Tests
Copyright (c) 2026 Tony Ray Macier III
"""

import unittest
import numpy as np
import sys
from pathlib import Path
import tempfile
import shutil

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database.matrix_codex_db import MatrixCodexDB
from database.db_utils import DatabaseManager
from database.data_loader import DataLoader
from database.trainer_storage import TrainerStorage


class TestMatrixCodexDB(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.db = MatrixCodexDB(str(self.temp_dir / "test_codex.npz"))

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_save_load_parameters(self):
        params = {
            'weights': np.random.randn(100, 100),
            'biases': np.random.randn(100)
        }
        self.db.save_parameters(params)
        loaded = self.db.load_parameters()
        self.assertIn('weights', loaded)
        self.assertEqual(loaded['weights'].shape, (100, 100))


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.db_manager = DatabaseManager(str(self.temp_dir / "test.db"))
        self.db_manager.connect()

    def tearDown(self):
        if self.db_manager.connection:
            self.db_manager.connection.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_connection(self):
        self.assertIsNotNone(self.db_manager.connection)


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = DataLoader()

    def test_load_batch(self):
        inputs, targets = self.loader.load_batch(batch_size=16)
        self.assertEqual(inputs.shape[0], 16)
        self.assertEqual(targets.shape[0], 16)


class TestTrainerStorage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.storage = TrainerStorage(str(self.temp_dir))

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_save_checkpoint(self):
        model_state = {'layer1': np.random.randn(10, 10)}
        optimizer_state = {'lr': 0.001}
        self.storage.save_checkpoint(1, model_state, optimizer_state)

        loaded = self.storage.load_checkpoint(1)
        self.assertIsNotNone(loaded)


if __name__ == '__main__':
    unittest.main()
