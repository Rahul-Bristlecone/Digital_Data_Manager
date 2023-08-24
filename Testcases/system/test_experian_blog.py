from unittest import TestCase
from APIs import experian_blog
from unittest.mock import patch
from APIs.blog import Blog


class TestExperianBlog(TestCase):
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:  # patching replaced the print of print_blogs with mocked_print
            blog_obj = Blog("Dream Girl", "Ayushmaan")
            experian_blog.dict_blogs = {"name": blog_obj}
            experian_blog.print_blogs()
            mocked_print.assert_called_with('- Dream Girl by Ayushmaan (0 posts)')
