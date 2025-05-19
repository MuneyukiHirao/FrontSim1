
import unittest
import sqlite3
from pathlib import Path

from backend.main import generate_daily, get_backlog

class EndpointTests(unittest.TestCase):
    def setUp(self):
        self.db_path = Path('test.db')
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(
            "CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, vehicle_id INTEGER, status TEXT, due_date TEXT, duration_min INTEGER, created_dt TEXT)"
        )
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        if self.db_path.exists():
            self.db_path.unlink()

    def test_generate_and_backlog(self):
        result = generate_daily('2025-05-13', conn=self.conn)
        self.assertEqual(result['generated'], 3)

        tasks = get_backlog(conn=self.conn)
        self.assertEqual(len(tasks), 3)

if __name__ == '__main__':
    unittest.main()
