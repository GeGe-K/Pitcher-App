from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test class to test the behavior of the User class
    '''

    def setUp(self):
        '''
        Set up method to run before each test 
        '''
        self.new_user = User(username = "Gloria", password = "12gege")

    def test_init(self):
        '''
        Tests if the User model has been instantiated correctly
        '''
        self.assertTrue(isinstance(self.new_user.username, "Gloria"))

    def tearDown(self):
        """
        Test will delete all the info from the db
        """
        User.query.delete()
        Pitch.query.delete()
    
    def test_save_user(self):
        '''
        Test saves the user
        '''
        self.new_user.save_user()
        users = User.query.all()
        self.assertTrue(len(users)>0)

      def test_password_setter(self):
        '''
        Test whether a password is generated
        '''
        self.assertTrue(self.new_user.pass_locked is not None)
    
    def test_password_is_hashed(self):
        '''
        Test whether the password cannot be viewed by other users
        '''
        with self.assertRaises(AttributeError):             self.new_user.password

    def test_password_verification(self):
        '''
        Test whether the password is verified correctly
        '''
        self.assertTrue(self.new_user.verify_password("12gege"))



    