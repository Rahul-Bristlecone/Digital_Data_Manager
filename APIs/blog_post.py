# BlogPost will have title and content
# Blog will have author
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # def blog_post(self, title, content):
    #     self.title = title
    #     self.content = content

    # Accepting the title and content, converting it into a dictionary to send it for creating a blog_post.
    def json(self):
        return {
                "title": self.title,
                "content": self.content,
                }
