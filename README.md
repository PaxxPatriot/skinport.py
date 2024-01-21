# skinport.py
An API wrapper for the Skinport API written in Python.

Installing
----------

**Python 3.10 or higher is required**

To install the library, you can just run the following command:

```bash
# Linux/macOS
$ python3 -m pip install -U skinport.py

# Windows
> py -3 -m pip install -U skinport.py
```

To install the development version, do the following:
```bash
$ git clone https://github.com/PaxxPatriot/skinport.py
$ cd skinport.py
$ python3 -m pip install -U .
```

Quick Example
--------------

```Python
import asyncio

import skinport

async def main():
  client = skinport.Client()
  # Get a list of all listed CS:GO items on skinport.com
  items = await client.get_items()
  print(items)

if __name__ == "__main__":
    asyncio.run(main())
```

Advanced Example
-----------------

With this library an automated script was created which forwards cheap listings to a Discord webhook. You can find it at [PaxxPatriot/cheapbot](https://github.com/PaxxPatriot/cheapbot).
