import unittest
from flask import Flask

class TestRenderTemplate(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    #check there is data in the admin list
    def test_table_row_count_admin(self):
        with self.app.test_request_context():
            rendered = self.app.jinja_env.get_template('list/admin-list-admin.html').render()
            table_rows = rendered.count('<th>')
            self.assertGreater(table_rows, 1)

    #check there is data in the employer list
    def test_table_row_count_employer(self):
        with self.app.test_request_context():
            rendered = self.app.jinja_env.get_template('list/employer-list-admin.html').render()
            table_rows = rendered.count('<th>')
            self.assertGreater(table_rows, 1)

    #check there is data in the staff list
    def test_table_row_count_staff(self):
        with self.app.test_request_context():
            rendered = self.app.jinja_env.get_template('list/staff-list-admin.html').render()
            table_rows = rendered.count('<th>')
            self.assertGreater(table_rows, 1)
    
    


if __name__ == '__main__':
    unittest.main()
