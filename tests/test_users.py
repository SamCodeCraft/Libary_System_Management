# tests/test_users.py
import unittest
from library.user_management import register_user, login_user, view_profile
from database import Session, engine, Base
from library.models import User

class TestUserManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database"""
        Base.metadata.create_all(bind=engine)

    def setUp(self):
        """Add sample user to the test database"""
        self.session = Session()
        self.sample_user = User(name="Test User", email="test@example.com", role="patron")
        self.session.add(self.sample_user)
        self.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        self.session.query(User).delete()
        self.session.commit()
        self.session.close()

    def test_register_user(self):
        # Add test for user registration
        register_user()
        new_user = self.session.query(User).filter_by(email="newuser@example.com").first()
        self.assertIsNotNone(new_user)

    def test_login_user(self):
        # Add test for user login
        login_user()
        user = self.session.query(User).filter_by(email="test@example.com").first()
        self.assertIsNotNone(user)

    def test_view_profile(self):
        # Add test for viewing user profile
        view_profile()
        user = self.session.query(User).filter_by(email="test@example.com").first()
        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
