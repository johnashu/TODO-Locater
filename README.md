# TODO-Locater

Find and locate TODO items, save to csv and print to screen

# 2 Different files Functional and a class based option.
### It started  off as a functional project but I had a need for a class option so both remain..

As Functions

```python
todos = find_todos('.', ext='py', comment_start='#', recursive=True)
show_todos(todos)
save_csv(todos, 'py')
```

As a class
```python
path = "."
ext = "py"
td = "TODO"
comment = '#'

find = TodoLocater(path, ext, td, comment, recursive=True)
find.show_todos()
```
