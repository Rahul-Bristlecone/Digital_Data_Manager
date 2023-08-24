dict_blogs = {}  # blog name : blog object


def menu():
    # Show user the blogs
    # Pick a choice from the menu
    # Do something with that choice
    # Exit
    pass


def print_blogs():
    for b_name, b_object in dict_blogs.items():  # [(name, object), (name, object)]
        print("- {}".format(b_object))
