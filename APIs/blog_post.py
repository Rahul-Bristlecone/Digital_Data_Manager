# BlogPost will have title and content
# Blog will have author
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Accepting the title and content, converting it into a dictionary to send it for creating a post.
    def json(self):
        return {
                "Title": self.title,
                "Content": self.content,
                }
