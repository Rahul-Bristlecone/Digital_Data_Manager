import unittest
from APIs import blog
from APIs.blog import Blog


class TestBlog(unittest.TestCase):
    def test_create_post(self):
        b = Blog("GADAR2", "Akshay")
        b.create_post("OMG2", "Not PEGI 18")
        # b.create_post("GADAR2", "Desh Bhakti")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "OMG2")
        self.assertEqual(b.posts[0].content, "Not PEGI 18")

    def test_blog(self):
        b = Blog("Review", "Rahul")
        b.create_post("Jawan", "Action-Patriotism")

        expected = {
            "title": "Review",
            "author": "Rahul",
            "posts": [
                {"title": "Jawan", "content": "Action-Patriotism"}
            ]
        }

        self.assertDictEqual(expected, b.json())


if __name__ == '__main__':
    unittest.main()
