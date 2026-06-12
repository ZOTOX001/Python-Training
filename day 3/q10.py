# Combined Example of *args and **kwargs:
def complete_info(*args, **kwargs):

    print("Args:", args)
    print("Kwargs:", kwargs)

complete_info(1, 2, 3, name="Aniket", age=21)