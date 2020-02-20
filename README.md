# TODO-Locater

Find and locate TODO items, save to csv and print to screen



```python
 path = "."
 ext = "py"
 td = "TODO"
 comment = '#'

find = TodoLocater(path, ext, td, comment, recursive=True)
find.show_todos()
```
