from os.path import exists
import sys
from glob import glob


class TodoLocater:
    def __init__(self, path, ext, td, comment, recursive=False):
        self.path = path
        self.ext = ext
        self.td = td
        self.comment = comment
        self.recursive = recursive
        self.todos = {}

    def get_files(self):
        g = glob(self.path + f"/**/*{self.ext}", recursive=self.recursive)
        if exists(self.path):
            for x in g:
                print(f"Searching  ::  {x}")

                result = self.find_todo(x)
                if result:
                    self.todos[x] = result
        else:
            raise OSError("Path does not exist.")


    def find_todo(self, f):
        temp_todos = []
        with open(f, "r") as input_:
            for line_no, line in enumerate(input_):                
                if self.comment in line and self.td in line:
                    # check to make sure that it is a true comment and not a variable name.
                    # Avoid false positives like :: `TODOs.append(todo) # there are no todos in this line`
                    comment_index = line.find(self.comment)
                    todo_index = line.find(self.td)                
                    if todo_index > comment_index:
                        temp_todos.append([f, f"Line - {line_no+1}  ::  {line.strip()}"])
        return temp_todos

    def show_todos(self):
        line = "-" * 100
        self.get_files()
        for k, v in self.todos.items():
            print(f"\n{line}\n\n{k}")
            for x in v:
                print(f">>>{x[1]}")
            self.save_csv(k, [v])

    def save_csv(self, fn, todos):
        import csv

        with open(fn + ".csv", "w", newline="") as csvfile:
            w = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            for row in todos:
                for r in row:
                    w.writerow(r)


if __name__ == "__main__":
    path = "."
    ext = "py"
    td = "TODO"
    comment = '#'

    find = TodoLocater(path, ext, td, comment, recursive=True)
    find.show_todos()


