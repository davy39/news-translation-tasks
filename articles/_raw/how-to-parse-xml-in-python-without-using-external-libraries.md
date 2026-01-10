---
title: How to Parse XML in Python Without Using External Libraries
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-11-12T20:29:56.941Z'
originalURL: https://freecodecamp.org/news/how-to-parse-xml-in-python-without-using-external-libraries
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762979370762/de792485-6d8a-42aa-adcc-66bd797c207c.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: In software development, you’ll run into XML (Extensible Markup Language)
  when working with configuration files, API responses, data exports, and more. While
  there are powerful third-party libraries for parsing XML, Python's standard library
  already ...
---

In software development, you’ll run into XML (Extensible Markup Language) when working with configuration files, API responses, data exports, and more. While there are powerful third-party libraries for parsing XML, Python's standard library already includes everything you need.

In this tutorial, you'll learn how to parse XML using Python's built-in [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html) module. No pip installs required.

🔗 [**You can find the code on GitHub**](https://github.com/balapriyac/python-basics/tree/main/parse-xml).

## Prerequisites

To follow along with this tutorial, you should have:

* Python 3.7 or later installed on your system
    
* Basic understanding of Python syntax and data structures
    
* Familiarity with basic programming concepts like loops and conditionals
    
* A text editor or IDE for writing Python code
    

No external libraries are required as we'll use Python's built-in `xml.etree.ElementTree` module.

## Table of Contents

1. [How to Read an XML String](#heading-how-to-read-an-xml-string)
    
2. [How to Read an XML File](#heading-how-to-read-an-xml-file)
    
3. [How to Find Elements in an XML Tree](#heading-how-to-find-elements-in-an-xml-tree)
    
4. [How to Extract Text and Attributes from XML](#heading-how-to-extract-text-and-attributes-from-xml)
    
5. [How to Build a Simple XML Parser](#heading-how-to-build-a-simple-xml-parser)
    
6. [How to Handle Missing Data](#heading-how-to-handle-missing-data)
    

## How to Read an XML String

Let's start simple. We'll parse XML directly from a string to understand the fundamental concepts.

```python
import xml.etree.ElementTree as ET

xml_string = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
    </product>
</catalog>
"""

root = ET.fromstring(xml_string)
print(f"Root tag: {root.tag}")
print(f"Root attributes: {root.attrib}")
```

How this works:

* We import `xml.etree.ElementTree` and give it the alias `ET` (this is the convention)
    
* `ET.fromstring()` parses the XML string and returns the `root` element
    
* Every element has a `.tag` property (the element name) and `.attrib` dictionary (its attributes)
    
* The `root` object represents the `<catalog>` element in our XML
    

For the above example, you’ll see the following output:

```plaintext
Root tag: catalog
Root attributes: {}
```

Here, the `root.attrib` is empty because the root element `<catalog>` in the provided `xml_string` does not have any attributes defined. Attributes are key-value pairs within the opening tag of an XML element, like `id="101"` or `currency="USD"` in the `<product>` and `<price>` elements. Since `<catalog>` only has a tag and no additional information within its opening tag, its attributes dictionary is empty.

## How to Read an XML File

In real applications, you'll usually read XML from files. Say you have a [products.xml](https://github.com/balapriyac/python-basics/blob/main/parse-xml/products.xml) file. Here's how you can read from the XML file:

```python
# Parse an XML file
tree = ET.parse('products.xml')
root = tree.getroot()

print(f"Root element: {root.tag}")
```

Before we proceed to run and check the output, let’s note the differences between reading XML strings vs files:

* `ET.parse()` reads from a file and returns an `ElementTree` object
    
* We call `.getroot()` to get the `root` element
    
* Use `ET.parse()` for files, `ET.fromstring()` for strings
    

Running the above code should give you:

```plaintext
Root element: catalog
```

## How to Find Elements in an XML Tree

`ElementTree` gives you three main ways to search for elements. Understanding when to use each is important.

```python
import xml.etree.ElementTree as ET

xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <categories>
            <category>Electronics</category>
            <category>Accessories</category>
        </categories>
    </product>
    <product id="102">
        <name>USB Mouse</name>
        <categories>
            <category>Electronics</category>
        </categories>
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)

# Method 1: find() - returns the FIRST matching element
first_product = root.find('product')
print(f"First product ID: {first_product.get('id')}")

# Method 2: findall() - returns ALL direct children that match
all_products = root.findall('product')
print(f"Total products: {len(all_products)}")

# Method 3: iter() - recursively finds ALL matching elements
all_categories = root.iter('category')
category_list = [cat.text for cat in all_categories]
print(f"All categories: {category_list}")
```

Now let’s understand how the three methods work:

* `find()` stops at the first match. Use when you only need one element.
    
* `findall()` only searches direct children (one level deep). Use for immediate child elements.
    
* `iter()` searches recursively through the entire tree. Use when elements might be nested anywhere.
    

This is important: `findall('category')` on root won't find anything because `<category>` isn't a direct child of `<catalog>`. But `iter('category')` will find all categories no matter how deeply nested. So when you run the above code, you’ll get:

```plaintext
First product ID: 101
Total products: 2
All categories: ['Electronics', 'Accessories', 'Electronics']
```

## How to Extract Text and Attributes from XML

Now let's extract actual data from our XML. This is where you turn structured XML into Python data you can work with.

```python
xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
        <stock>45</stock>
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)
product = root.find('product')

# Get element text content
product_name = product.find('name').text
price_text = product.find('price').text
stock_text = product.find('stock').text

# Get attributes (two ways)
product_id = product.get('id')  # Method 1: .get()
product_id_alt = product.attrib['id']  # Method 2: .attrib dictionary

# Get nested attributes
price_element = product.find('price')
currency = price_element.get('currency')

print(f"Product: {product_name}")
print(f"ID: {product_id}")
print(f"Price: {currency} {price_text}")
print(f"Stock: {stock_text}")
```

This outputs:

```plaintext
Product: Wireless Keyboard
ID: 101
Price: USD 29.99
Stock: 45
```

What's happening here:

* `.text` gets the text content between opening and closing tags
    
* `.get('attribute_name')` safely retrieves an attribute (returns `None` if missing)
    
* `.attrib['attribute_name']` accesses the attribute dictionary directly (raises `KeyError` if missing)
    
* Use `.get()` when an attribute might be optional, use `.attrib[]` when it's required
    

## How to Build a Simple XML Parser

Let's put it all together with a practical example. We'll parse the full product catalog and convert it to a Python list of dictionaries.

```python
def parse_product_catalog(xml_file):
    """Parse an XML product catalog and return a list of product dictionaries."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    products = []

    for product_element in root.findall('product'):
        # Extract product data
        product = {
            'id': product_element.get('id'),
            'name': product_element.find('name').text,
            'price': float(product_element.find('price').text),
            'currency': product_element.find('price').get('currency'),
            'stock': int(product_element.find('stock').text),
            'categories': []
        }

        # Extract categories (nested elements)
        categories_element = product_element.find('categories')
        if categories_element is not None:
            for category in categories_element.findall('category'):
                product['categories'].append(category.text)

        products.append(product)

    return products
```

Breaking down this parser:

* We iterate through all `<product>` elements using `findall()`
    
* For each product, we extract text and attributes into a dictionary. We convert numeric strings to proper types (`float` for price, `int` for stock)
    
* For nested categories, we first check if the `<categories>` element exists. Then we iterate through child `<category>` elements and collect their text
    

The result is clean Python data structures you can easily work with. You can now use the parser like so:

```python
products = parse_product_catalog('products.xml')

for product in products:
    print(f"\nProduct: {product['name']}")
    print(f"  ID: {product['id']}")
    print(f"  Price: {product['currency']} {product['price']}")
    print(f"  Stock: {product['stock']}")
    print(f"  Categories: {', '.join(product['categories'])}")
```

Output:

```plaintext
Product: Wireless Keyboard
  ID: 101
  Price: USD 29.99
  Stock: 45
  Categories: Electronics, Accessories

Product: USB Mouse
  ID: 102
  Price: USD 15.99
  Stock: 120
  Categories: Electronics
```

## How to Handle Missing Data

Real-world XML is messy (no surprises there!). Elements might be missing, text might be empty, or attributes might not exist. Here's how to handle that gracefully.

```python
xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
    </product>
    <product id="102">
        <name>USB Mouse</name>
        <!-- Missing price element -->
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)

for product in root.findall('product'):
    name = product.find('name').text
    
    # Safe way to handle potentially missing elements
    price_element = product.find('price')
    if price_element is not None:
        price = float(price_element.text)
        currency = price_element.get('currency', 'USD')  # Default value
        print(f"{name}: {currency} {price}")
    else:
        print(f"{name}: Price not available")
```

Here, we handle potential missing data by:

1. Using `product.find('price')` to search for the `<price>` element within the current `<product>` element.
    
2. Checking if the result of `find()` is `None`. If an element is not found, `find()` returns `None`.
    
3. Using an `if price_element is not None:` condition to only attempt to access the text `(price_element.text)` and attributes `(price_element.get('currency', 'USD'))` of the `<price>` element if it was actually found.
    
4. Adding an `else` block to handle the case where the `<price>` element is missing, printing "Price not available".
    

This approach prevents errors that would occur if you tried to access `.text` or `.get()` on a `None` object. For the above code snippet, you’ll get:

```plaintext
Wireless Keyboard: USD 29.99
USB Mouse: Price not available
```

Here are a few more error-handling strategies:

* Always check if `find()` returns `None` before accessing `.text` or `.get()`
    
* Use `.get('attr', 'default')` to provide default values for missing attributes
    
* Consider wrapping parsing in try-except blocks for production code
    
* Validate your data after parsing rather than assuming XML structure is correct
    

## Conclusion

You now know how to parse XML in Python without installing any external libraries. You learned:

* How to read XML from strings and files
    
* The difference between `find()`, `findall()`, and `iter()`
    
* How to extract text content and attributes safely
    
* How to handle nested elements and missing data
    

The `xml.etree.ElementTree` module works well enough for most XML parsing needs, and it's always available in Python's standard library.

For more advanced XML navigation and selection, you can explore [XPath expressions](https://www.w3schools.com/xml/xpath_syntax.asp). XPath works well for selecting nodes in an XML document and can be very useful for complex structures. We’ll cover this in another tutorial.

Until then, happy parsing!
