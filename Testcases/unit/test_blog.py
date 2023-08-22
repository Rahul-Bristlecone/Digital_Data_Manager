import unittest
from APIs import blog
from APIs.blog import Blog


class TestBlog(unittest.TestCase):
    def test_create_blog(self):
        b = Blog("Dreams", "Rooh")
        self.assertEqual("Dreams", b.title)  # add assertion here
        self.assertEqual("Rooh", b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog("Dreams", "Rooh")
        self.assertEqual(b.__repr__(), "Dreams by Rooh (0 posts)")

# part of integration test
    # def test_create_post(self):
    #     b = Blog("GADAR2", "Akshay")
    #     b.create_post("OMG2", "Not PEGI 18")
    #     # b.create_post("GADAR2", "Desh Bhakti")
    #
    #     self.assertEqual(len(b.posts), 1)
    #     self.assertEqual(b.posts[0].title, "OMG2")
    #     self.assertEqual(b.posts[0].content, "Not PEGI 18")


if __name__ == '__main__':
    unittest.main()
