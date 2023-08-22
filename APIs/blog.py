# Blog title, Blog Author, Blog Posts [Empty initially]
from APIs.blog_post import BlogPost


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    # representation of class object
    def __repr__(self):
        return "{} by {} ({} post{})".format(self.title,
                                             self.author,
                                             len(self.posts),
                                             "s" if len(self.posts) != 1 else "")

    # This is the second unit (imported another module) - we have already created a test for this test_blog_post
    # Integration test will be written for this
    def create_post(self, title, content):
        self.posts.append(BlogPost(title, content))

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts]
        }
