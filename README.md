# kakaopy

## Installation

1. install from PyPI

```cmd
pip install kakaopy
```

2. install from cloned repository

```cmd
git clone https://github.com/SeoJeongYeop/kakaopy.git
cd kakaopy
pip install .
```

However, this way occur warning 'DEPRECATION'
This way is removed from pip 21.3 version

3. install from GitHub repository

```cmd
pip install git+https://github.com/SeoJeongYeop/kakaopy.git
```

## Usage

1. from kakaopy import kakaopy

```py
from kakaopy import kakaopy
```

2. set your REST_API_KEY

```py
kakaopy.setHeader('YOUR_REST_API_KEY')
```

3. make object

e.g. doc, video, image, book, blog, cafe

```
doc1 = kakaopy.doc()
```

4. (option) setting object option.

e.g. size, page, sort, target(only book)

```py
doc1.setSort("recency")
```

More information can be found through object.help() function.

```py
doc1.help()
```

![help function](https://user-images.githubusercontent.com/41911523/123953929-c243ed80-d9e2-11eb-8d75-343b1fbc7e8e.PNG)

5. object.search(query): search query and return search results in the form of json.

```py
doc1.search("python")
```

6. object.save(query, path): save file.json in path. The 'path' is the file name or path to the file.

```py
doc1.save(query = "web crawling", path = "web.json")
```

is same as

```py
doc1.save(query = "web crawling", path = "web")
```
