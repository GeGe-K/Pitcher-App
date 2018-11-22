from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentTest(unittest.TestCase):
        '''
    Test class to test the behavior of the User class
    '''
    
    def setUp(self):
        self.user_James = User(
            username='Gloria', password='green', email='gege@ms.com')
        self.new_pitch = Pitch(id=1, title='Test', description='This is a test pitch',
                               category="interview", user=self.user_Glorias)
        self.new_comment = Comment(
            id=1, content='Test comment', user=self.user_Gloria, pitch=self.new_pitch)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.content, 'Test comment')
        self.assertEquals(self.new_comment.user, self.user_Gloria)
        self.assertEquals(self.new_comment.pitch, self.new_pitch)
