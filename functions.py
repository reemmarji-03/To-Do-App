import lookups

def get_todos(filepath=lookups.todos_text_file):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=lookups.todos_text_file):
     with open(filepath, 'w') as file:
          file.writelines(todos_arg)  