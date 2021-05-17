from django.test import TestCase
from Content.models import Post
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self) -> None:
        Post.objects.create(post_title='test', text='testeteste')

    def test_content_post(self):
        test1 = Post.objects.get(post_title='test')
        self.assertEqual(test1)