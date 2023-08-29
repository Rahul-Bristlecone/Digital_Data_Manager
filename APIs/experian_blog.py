from APIs.blog import Blog
from APIs.blog_post import BlogPost

blogs = dict()  # blog name : blog object
MENU_PROMPT = "Enter your choice, c-create, r-read, d-delete, e-exit"


def menu():
    # Show user the blogs
    # Pick a choice from the menu
    # Do something with that choice
    # Exit
    print_blogs()
    choice = input(MENU_PROMPT)
    # print(choice)
    match choice:
        case 'c':
            ask_create_blog()
        case 'r':
            read_blog()
        case 'd':
            delete_post()
        case 'e':
            exit()
    choice = input(MENU_PROMPT)


def print_blogs():
    for b_name, b_object in blogs.items():  # [(name, object), (name, object)]
        print("- {}".format(b_object))


def ask_create_blog():
    blog_title = input("Enter title of your blog")
    blog_author = input("Enter author name")
    blogs[blog_title] = Blog(blog_title, blog_author)


def read_blog():
    blog_title = input("Enter title of the blog to be read")
    print_posts(blogs[blog_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(post.title, post.content)


def delete_post():
    pass
