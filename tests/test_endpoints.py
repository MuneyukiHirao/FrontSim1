import os
import unittest
from datetime import datetime

from backend import main, models, database

class EndpointTests(unittest.TestCase):
    def setUp(self):
        test_db = "/tmp/test.db"
        os.environ["DB_PATH"] = test_db
        database.DB_PATH = test_db
        database.init_db()

    def tearDown(self):
        pass

    def test_get_tasks(self):
        with database.get_conn() as conn:
            conn.execute(
                "INSERT INTO tasks (type, status, due_date, duration_min) VALUES (?,?,?,?)",
                ("test", "pending", "2025-05-01", 60),
            )
            conn.commit()
            task_id = conn.execute("SELECT id FROM tasks").fetchone()[0]

        tasks = main.get_tasks("2025-05-01", "2025-05-02")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, task_id)

    def test_reset_sim(self):
        with database.get_conn() as conn:
            conn.execute(
                "INSERT INTO tasks (type, status, due_date, duration_min) VALUES (?,?,?,?)",
                ("test", "pending", "2025-05-01", 60),
            )
            conn.commit()
            count_before = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
            self.assertGreater(count_before, 0)
        main.reset_sim()
        with database.get_conn() as conn:
            count_after = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
            self.assertEqual(count_after, 0)

if __name__ == '__main__':
    unittest.main()
