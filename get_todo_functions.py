from os.path import exists
import sys
from glob import glob

def _get_files(path, ext, recursive=False):
    # return a list of files 
    return glob(path + f"/**/*{ext}", recursive=recursive)    

def _find_todos_in_file(fn, todo_token, comment_start):
    # return a list of todos in the file
    temp_todos = []
    with open(fn, "r") as input_:
        for line_no, line in enumerate(input_):                
            if comment_start in line and todo_token in line:
                # check to make sure that it is a true comment and not a variable name.
                # Avoid false positives like :: `TODOs.append(todo) # there are no todos in this line`
                comment_index = line.find(comment_start)
                todo_index = line.find(todo_token)                
                if todo_index > comment_index:
                    temp_todos.append([fn, f"Line - {line_no+1}  ::  {line.strip()}"])
    return temp_todos

def find_todos(path, ext, todo_token = 'TODO', comment_start = '#', recursive=False):
    # returns a dictionary of todos
    todos = {}
    files = _get_files(path, ext,recursive=recursive)
    if exists(path):
        for x in files:
            try:
                print(f"Searching  ::  {x}")
                result = _find_todos_in_file(x, todo_token, comment_start)
                if result:
                    todos[x] = result
            except PermissionError:
                pass # not a ext file (possible a folder)
    else:
        raise OSError("Path does not exist.")
    return todos

def show_todos(todos: dict):
    # show todos
    line = "-" * 100
    for k, v in todos.items():
        print(f"\n{line}\n\n{k}")
        for x in v:
            print(f">>>{x[1]}")

def save_csv(todos, ext):
    # save todos to a csv file
    import csv
    for k, v in todos.items():       
        k = k.split(ext)[0][:-1]
        with open(f"{k}-TODOS.csv", "w", newline="") as csvfile:
            w = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            for row in v:
                w.writerow(row)

if __name__ == "__main__":
    todos = find_todos('.', ext='py', comment_start='#', recursive=True)
    show_todos(todos)
    save_csv(todos, 'py')
