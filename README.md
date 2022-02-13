# skinport.py
An API wrapper for the Skinport API written in Python.

Installing
----------

**Python 3.8 or higher is required**

To install the development version, do the following:
```bash
$ git clone https://github.com/PaxxPatriot/skinport.py
$ cd skinport.py
$ python3 -m pip install -U .
```

Quick Example
--------------

```Python
import skinport

client = skinport.Client()
# Get a list of all listed CS:GO items on skinport.com
client.get_items()
```
