import builtins
from unittest import TestCase
from APIs import experian_blog
from unittest.mock import patch
from APIs.blog import Blog
from APIs.blog_post import BlogPost


class TestExperianBlog(TestCase):

    def test_menu_choice_prompt(self):
        with patch('builtins.input') as mocked_input:  # patching input method
            experian_blog.menu()
            mocked_input.assert_called_with(experian_blog.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('APIs.experian_blog.print_blogs') as mocked_print_blogs:  # patching function call
            with patch('builtins.input', return_value='q'):
                experian_blog.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:  # patching replaced the print of print_blogs with mocked_print
            blog_obj = Blog("Dream Girl", "Ayushmaan")
            experian_blog.blogs = {"name": blog_obj}
            experian_blog.print_blogs()
            mocked_print.assert_called_with('- Dream Girl by Ayushmaan (0 posts)')

    def test_create_blog(self):
        # patching means target function, class, method ka replica create karna
        # because we don't know what will be the return value
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ("OMG 2", "Akshay")
            experian_blog.create_blog()
            self.assertIsNotNone(experian_blog.blogs.get("OMG 2"))

    def test_read_blog(self):
        # Testing that read_blog function is calling print_posts or not (print_posts need parameters)
        blog_obj = Blog("Test", "Author")
        experian_blog.blogs = {'Test': blog_obj}
        with patch('builtins.input', return_value="Test"):
            with patch('APIs.experian_blog.print_posts') as mocked_print_posts:
                experian_blog.read_blog()
                mocked_print_posts.assert_called_with(blog_obj)

    def test_print_posts(self):
        blog_obj = Blog("Test", "Author")
        blog_obj.create_post('Mother', "India")
        experian_blog.blogs = {'Test': blog_obj}
        with patch('APIs.experian_blog.print_post') as mocked_print_post:
            experian_blog.print_posts(blog_obj)
            mocked_print_post.assert_called_with(blog_obj.posts[0])

    def test_print_post(self):
        post_obj = BlogPost("Hero", "Govinda")
        with patch('builtins.print') as mocked_print:  # patching input method
            experian_blog.print_post(post_obj)
            mocked_print.assert_called_with("Hero", "Govinda")
