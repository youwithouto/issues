# Generator Comprehension

## Date: 12 Jan 2018

``` Python
foo = [1, 2, 3]
bar = (item for item in foo if foo.count(item) > 0)
foo = [2, 4, 6]
print(list(bar))
```

The output of the above code snippet is `[2]`. But why?