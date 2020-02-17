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
### Usage

```python
import JsonTemplates

json_tmp = JsonTemplates()
result = json_tmp.load("template.json")

if result[0]:
  new_dict = json_tmp.generate({"variable":"hello world","array":["foo","bar"]})
```

### Methods

- **load(json_file_path)** - Loads a JSON file  
Returns a tuple (Success,error message or dictionary)

- **loads(json_str)** - Loads a JSON string  
Returns a tuple (Success,error message or dictionary)  

- **generate(replacement_dict)** - Takes in a dictionary of replacement values and generates a new dictionary with the placeholders replaced with the values in the dictionary  
Returns a tuple (Success, error message or dictionary)
