# Blog title, Blog Author, Blog Posts [Empty initially]
from APIs.blog_post import BlogPost


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []  # list of dictionary

    # representation of class object
    def __repr__(self):
        return "{} by {} ({} post{})".format(self.title,
                                             self.author,
                                             len(self.posts),
                                             "s" if len(self.posts) != 1 else "")

    # This is the second unit (imported from another module)
    # targeting to create a post which requires title and content
    # - we have already created a test for this test_blog_post
    # Integration test will be written for this
    def create_post(self, title, content):
        self.posts.append(BlogPost(title, content))
        print(self.posts[0].title)
        print(self.posts[0].content)

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts]
        }


green = Blog("hulk", "huj")
green.create_post("mouyh", "huj")
