[Home](/)
#Lesson : Json

###Convert A Python Dictionary To JSON String : Pretty Print
You saw in the two notions above (`json.dump and json.dumps`) that
it convert a python dictionary into a JSON string. 
But the result is not really pretty and hard to understand because it writes the dictionary in one single line. 
What should we do to make it more readable ?

We can use the parameters `indent` and `sort_keys`:

---
```python
import json

my_family = {
    "parents" :['Beth', 'Jerry'],
    "children" :['Summer', 'Morty']
}

json_file = "index.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)
```
---


Code in Python with highlight:

```python
if isAwesome:
  return true
```

Code in JavaScript:

```javascript
if (isAwesome){
  return true
}
```

---
**NOTE**

It works with almost all markdown flavours (the below blank line matters).

---
Take me to the [exercises](exe)