# The very first thing we need to check is that, does the thing we want to test has any
# external dependency like "on any other API" or "on Database" or "any other file". If Not,
# These tests are usually or casually called unit tests
from unittest import TestCase
from APIs.blog_post import BlogPost


class TestBlogPost(TestCase):
    def test_blogpost(self):
        blog_post_obj = BlogPost("Espn cric info", "Rising Stars")
        self.assertEquals("Espn cric info", blog_post_obj.title)
        self.assertEquals("Rising Stars", blog_post_obj.content)

    def test_json(self):
        blog_post_obj = BlogPost("Espn cric info", "Rising Stars")
        expected_result = {"Title": "Espn cric info", "Content": "Rising Stars", }
        # checking that the values returned by the function in the form of dictionary are
        # same as provided or not (json type and values)
        self.assertDictEqual(expected_result, blog_post_obj.json())
