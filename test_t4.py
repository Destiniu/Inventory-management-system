#https://python-basics-tutorial.readthedocs.io/en/24.3.0/test/sqlite.html
#https://docs.python.org/3/library/unittest.html 
#https://docs.python.org/3/library/sqlite3.html

import unittest
import sqlite3


class TestT4Unit(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("ims.db")
        self.cur = self.con.cursor()

    def testDBconnection(self): #unit test 1
        self.assertIsNotNone(self.con)

    def testTABLEexistsCategory(self): #unit test 2
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='category'")
        result = self.cur.fetchone()
        self.assertIsNotNone(result)


    def testTABLEexistsProduct(self): #unit test 3
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='product'")
        result = self.cur.fetchone()
        self.assertIsNotNone(result)

    def tearDown(self):
        self.con.close()


class TestT4Integration(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("ims.db")
        self.cur = self.con.cursor()

    def testInsertSelect(self): #Integration test 1
        self.cur.execute("INSERT INTO category(name) VALUES(?)", ("Test111",))
        self.con.commit()

        self.cur.execute("SELECT name FROM category WHERE name=?", ("Test111",))
        result = self.cur.fetchone()

        self.assertEqual(result[0], "Test111")

    def testInsertDelete(self): #Integration test 2
        self.cur.execute("INSERT INTO category(name) VALUES(?)", ("Test222",))
        self.con.commit()

        self.cur.execute("DELETE FROM category WHERE name=?", ("Test222",))
        self.con.commit()

        self.cur.execute("SELECT * FROM category WHERE name=?", ("Test222",))
        result = self.cur.fetchone()

        self.assertIsNone(result)

    def tearDown(self):
        self.con.close()

class TestT4Regression(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("ims.db")
        self.cur = self.con.cursor()

    def testCategoryCount(self):
        self.cur.execute("INSERT INTO category(name) VALUES(?)", ("RegTestt8",))
        self.con.commit()

        self.cur.execute("SELECT COUNT(*) FROM category WHERE name=?", ("RegTestt8",))
        count = self.cur.fetchone()[0]

        self.assertEqual(count, 1)

    def tearDown(self):
        self.con.close()

if __name__ == "__main__":
    unittest.main()

