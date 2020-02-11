# json-templates

A small python module for populating json template files.

### Version 0.1.0

Accepts either a json string or a file path and a dictionary. json-template replaces the place holders found in the json with those found in the dictionary.

Below is a template example

```json
{
                "key":"hard coded value",
                "key2":1,
                "key3":"{{ variable }}",
                "key4":"{% array %}"
}
```

Currently supports `{{ variable }}` for single replacement and `{% array %}` for iterable replacement.

For example given the following dictionary
```python
{
  "variable":"hello world",
  "array":["foo","bar"]
}
```

The JSON would become

```json
{
                "key":"hard coded value",
                "key2":1,
                "key3":"hello world",
                "key4":["foo","bar"]
}
```
