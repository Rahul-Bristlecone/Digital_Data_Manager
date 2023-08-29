dict_blogs = {}  # blog name : blog object
MENU_PROMPT = "Enter your choice, c-create, l-list, d-delete, e-exit"


def menu():
    # Show user the blogs
    # Pick a choice from the menu
    # Do something with that choice
    # Exit
    print_blogs()
    choice = input(MENU_PROMPT)
    # print(choice)
    # match choice:
    #     case 'c': print()


def print_blogs():
    for b_name, b_object in dict_blogs.items():  # [(name, object), (name, object)]
        print("- {}".format(b_object))
