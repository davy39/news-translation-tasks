---
title: How to Create and Upload Your First Python Package to PyPI
subtitle: ''
author: Rochdi Khalid
co_authors: []
series: null
date: '2022-04-11T15:40:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/cover-image-python-packaging-blog-1.jpg
tags:
- name: package
  slug: package
- name: Python
  slug: python
seo_title: null
seo_desc: "A few weeks ago, I wanted to learn how to build my first Python package,\
  \ and I was trying to figure out where to start. \nWell, I got confused and a bit\
  \ stressed trying to find a simple and easy tutorial I could use to get started.\
  \ For this reason, I ..."
---

A few weeks ago, I wanted to learn how to build my first Python package, and I was trying to figure out where to start. 

Well, I got confused and a bit stressed trying to find a simple and easy tutorial I could use to get started. For this reason, I decided to write this tutorial documenting how I built my first Python package.

## What is a package in Python?

Before we get started, we should know a package means in Python.

A Python package is a directory that contains a bunch of modules with a dependency file called `__init__.py`. This file can be completely empty and you use it to mark the directory on a disk as a Python package. 

The following shows an example of a package directory:

```
package
	__init__.py
	module_a.py
	module_b.py
	module_c.py

```

The `__init__.py` is a dependency file that helps Python look for the available modules in our package directory. If we remove this file, Python will fail to import our modules.

## Packages vs modules in Python

You should now understand that Python packages create a structured directory with several modules, but what about modules? Let's make sure we understand the difference between a package and a module:

A **Module** always corresponds to a single Python file _turtle.py_. It contains logic like classes, functions, and constants.

A **Package** is basically a module that could contain many modules or sub-packages.

## Package structure

Packages don't only contain modules, though. They consist of top-level scripts, documentation, and tests, as well. The following example shows how a basic Python package can be structured:

```
package_name/
	docs/
	scripts/
	src/
		package_a
			__init__.py
			module_a.py
		package_b
			__init__.py
			module_b.py
	tests/
    	__init__.py
		test_module_a.py
		test_module_b.py
	LICENSE.txt
	CHANGES.txt
	MANIFEST.in
	README.txt
	pyproject.toml
	setup.py
	setup.cfg

```

Let's understand what each file in the tree above is used for:

* **package_name**: represents the main package.
* **docs**: includes documentation files on how to use the package.
* **scripts/**: your top-level scripts.
* **src**: where your code goes. It contains packages, modules, sub-packages, and so on.
* **tests**: where you can put unit tests.
* **LICENSE.txt**: contains the text of the license (for example, MIT).
* **CHANGES.txt**: reports the changes of each release.
* **MANIFEST.in**: where you put instructions on what extra files you want to include (non-code files).
* **README.txt**: contains the package description (markdown format).
* **pyproject.toml**: to register your build tools.
* **setup.py**: contains the build script for your build tools.
* **setup.cfg**: the configuration file of your build tools.

Note that there are two options for how to include our test files in our main package. We can keep it at the top level as we did above or put it inside the package like the following:

```
package_name/
      __init__.py
      module_a.py
      module_b.py
      test/
          __init__.py
          test_module_a.py
          test_module_b.py

```

In my opinion, I think keeping tests at the top level can help a lot especially when our tests require reading and writing other external files.

## Should you use setup.cfg or setup.py?

The **setup.py** and **setup.cfg** are the default packaging tools within PyPI, setuptools, pip, and the standard python library. 

Here, they represent the configuration and build scripts for setuptools. They both tell the setuptools how the package can be built and installed. 

The mentioned file contains information like the version, packages, and files to include, along with any requirements.

The following shows an example of `setup.py` that uses some `setup()` arguments. You can find more arguments [here](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#setup-args):

```python
import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "package-name",
    version = "0.0.1",
    author = "author",
    author_email = "author@example.com",
    description = "short package description",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)

```

The `setup.cfg` is written in a different format compared to `setup.py`, and contains basically two essential keys, `command` and `options`. 

The `command` key represents one of the **distutils** commands, while the `options` key defines the options the command can support.

```
[command]
option = value

```

The following shows an example of `setup.cfg` that uses some metadata and options. You can find a variety of metadata and options [here](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html):

```
[metadata]
name = package-name
version = 0.0.1
author = name of the author
author_email = author@example.com
description = short package description
long_description = file: README.md
long_description_content_type = text/markdown
url = package url
project_urls =
    Bug Tracker = package issues url
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src

```

The `setup.py` and `setup.cfg` are both specific to setuptools. Also, the `setup.cfg` can safely be moved to `pyproject.toml`. 

Here, the idea is that maybe one day we'll want to switch to other build systems like **flit** or **poetry**. In that case, all we'll need to do is change the build-system entry (setuptools for example) in `pyproject.toml` to something like flit or poetry rather than starting over from scratch. 

[Here](https://packaging.python.org/en/latest/key_projects/#build) you can find information about other tools that build and distribute Python packages.

No matter which configuration file we chose, we are "locked-in" to maintaining that particular configuration file, either pyproject.toml, setup.cfg, or setup.py.

According to the [Python Packaging User Guide](https://packaging.python.org/en/latest/), `setup.cfg` is preferred because it's static, clean, easier to read, and avoids encoding errors.

## How to build your first Python package

Now, it's time to start building a simple Python package. We will use setuptools as a build system and we will configure our project using `setup.cfg` and `pyproject.toml`.

### Set up the package files

For this simple package, we need to structure our directory by adding the dependency files needed to get the package ready for distribution. This is how to structure our package:

```
basicpkg/
	src/
		divide
			__init__.py
			divide_by_three.py
		multiply
			__init__.py
			multiply_by_three.py
	tests/
		__init__.py
		test_divide_by_three.py
		test_multiply_by_three.py
	LICENSE.txt
	README.txt
	pyproject.toml
	setup.cfg

```

Our main package consists of two packages: the first one to divide numbers by three, and the other to multiply numbers by three. 

Also, we ignore some files like `CONTEXT.txt`, `MANIFEST.in`, and the `docs/` directory to keep things simple at the moment. But we need the `test/` directory to include our unit tests to test the package's behaviors.

### Add some logic to our modules

As always, we will keep the `__init__.py` empty. Then, we need to put some logic in our modules to perform our operations. 

For the divide package, let's add the following content into `divide_by_three.py` to divide any number by three:

```python
def divide_by_three(num):
	return num / 3

```

The same logic applies to `multiply_by_three.py` inside the multiply package. But, this time is to multiply any number by three:

```python
def multiply_by_three(num):
	return num * 3

```

Feel free to add more packages and modules to perform other kinds of operations. For example, you can add packages to do addition and subtraction tasks.

### Test our modules

It's good to practice adding automated tests to any program we create. We will use `unittest` to test our modules and the package's behavior. 

Inside the `test/` directory, let's add the following code to `test_divide_by_three.py`:

```python
import unittest
from divide.by_three import divide_by_three 

class TestDivideByThree(unittest.TestCase):

	def test_divide_by_three(self):
		self.assertEqual(divide_by_three(12), 4)

unittest.main()

```

We imported TestCase from `unittest` to perform our automated testing. Then, we imported our division method `divide_by_three()` from `by_three` module that is located inside the divide package. 

If we remove the `__init__.py` here, Python will no longer be able to find our modules. 

The `.assertEqual()` is used to check the equality of the two values above (divide_by_three(12) and 4). The `unittest.main()` is instantiated to run all our tests.

The same logic applies to `test_multiply_by_three.py`:

```python
import unittest
from multiply.by_three import multiply_by_three

class TestMultiplyByThree(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(multiply_by_three(3), 9)

unittest.main()

```

To run the tests, type the following in your terminal/command:

For Linux:

```
python3 tests/test_divide_by_three.py

```

For Windows:

```
py tests/test_divide_by_three.py

```

Do the same to test the multiply module. If our tests run successfully, you should get the following:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```

If you add extra packages and modules, try to add some `unittest` methods to them. This is going to be a good challenge for you.

### Configure metadata using setup.cfg

Next, we need to add a configuration file for setuptools. As mentioned before, this config file will tell setuptools how our package can be built and installed. 

So, we need to add the following metadata and options to our `setup.cfg`. Then, don't forget to choose a different name because I already uploaded this package with the name below to [TestPyPi](https://test.pypi.org/project/basicpkg/). Also, change other information like author, email, and project URLs to distribute the package with your info.

```
[metadata]
name = basicpkg
version = 1.0.0
author = your name
author_email = your email
description = A simple Python package
long_description = file: README.md, LICENSE.txt
long_description_content_type = text/markdown
url = https://gitlab.com/codasteroid/basicpkg
project_urls =
    Bug Tracker = https://gitlab.com/codasteroid/basicpkg/-/issues
    repository = https://gitlab.com/codasteroid/basicpkg
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src

```

You should just keep everything as default in the options category. The package_dir locates the root package where your packages, modules, and all your Python source files are located. 

In the packages key, we can list our packages manually like this `[divide, multiply]`. But if we want to get all the packages, we can use `find:` and specify where we need to find these packages by using `[options.packages.find]` with the `where` key assigned to the name of the root package.

Always make sure to include the `classifiers` key in your configuration file to add some important information like the version of Python and the operating system our package is suitable for. You can find the complete list of classifiers [here](https://pypi.org/classifiers/).

### Create pyproject.toml

We will be using setuptools as a build system. To tell `pip` or other build tools about our build system, we need two variables, as seen below. 

We use `build-system.require` to include what we need to build our package, while `build-system.build-back-end` defines the object that will perform the build. 

So, let's enter the following content in `pyproject.toml`:

```
[build-system]
requires = ['setuptools>=42']
build-backend = 'setuptools.build_meta'

```

Note that you can safely move all configuration settings in `setup.cfg` to `pyproject.toml` if you decide to change the build system to flit or poetry, for example. This will save you time.

### Create the README.md

Creating a good `README.md` is important. Let's add a description to our package, and include some instructions on how to install it:

```markdown
# `basicpkg`

The `basicpkg` is a simple testing example to understand the basics of developing your first Python package. 

```

We can also add how to use our package like this:

```markdown
from multiply.by_three import multiply_by_three
from divide.by_three import divide_by_three

multiply_by_three(9)
divide_by_three(21)

```

Feel free to add any information that can help other devs understand what your package is used for and some instructions on how to install it and work properly with it. 

Note that our configuration file will load the `README.md` and will be included when we distribute our package.

### Add a license

It's very important to add a LICENSE to your project to let users know how they can use your code. Let's choose an MIT license for our Python package and add the following content to `LICENSE.txt`:

```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

Don't forget to replace [year] with the current year and [full name] with your name or the names of the copyright holders.

### Generate the distribution archives

One more step left to get our package ready for distribution: generating the distribution archives for our Python package. To do so, first we need to update our PyPA's build and then generate the source and built archives.

In the terminal/cmd, run the following commands from the same directory where the `pyproject.toml` file is located:

For Linux:

```
python3 -m pip install --upgrade build
python3 -m build

```

For Windows:

```
py -m pip install --upgrade build
py -m build

```

Once the process above is completed, a new directory is generated called `dist/` with two files in it. The `.tag.tz` file is the source archive and the `.whl*` file is the built archive. These files represent the distribution archives of our Python package which will be uploaded to the Python Package Index and installed by `pip` in the following sections.

## How to upload a package in Python

Python Package Index is where we should upload our project. Since our Python package is in test and we might add other functionalities to experiment with it, we should use a separate instance of PyPI called TestPyPI. This instance is specifically implemented for testing and experimentation. Then, once your package is ready and meets your expectations, you can upload it to PyPI as a real package.

Let's follow the instructions below to get our TestPyPI ready to upload our package:

1. Go to [TestPyPI](https://test.pypi.org/) and create an account.
2. Verify your email address so you can upload packages.
3. Update your profile settings (add your picture and so on).
4. Go to [api-tokens](https://test.pypi.org/manage/account/#api-tokens) and create your API token to securely upload your packages.
5. On the same page, set the scope to "entire account".
6. Copy and save your token in a safe place on your disk.

Next, we need to upload our distribution archives. To do so, we have to use an upload tool to upload our package. The official PyPI upload tool is **twine**, so let's install twine and upload our distribution archives under the `dist/` directory.

In the terminal/cmd, run the following commands from the same directory where the `pyproject.toml` file is located:

For Linux:

```
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*

```

For Windows:

```
py -m pip install --upgrade twine
py -m twine upload --repository testpypi dist/*

```

Then, enter `__token__`. as username, and the token (pypi- prefix included) you saved as a password. Press Enter to upload the distributions.

## How to install the uploaded Python package

Now, it's time to install our package. You can create a new virtual environment and use `pip` to install it from TestPyPI:

For Linux:

```
python3 -m venv env
source env/bin/activate
(env) python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps basicpkg

```

For Windows:

```
py -m venv env
.\env\Scripts\activate
(env) py -m pip install --index-url https://test.pypi.org/simple/ --no-deps basicpkg

```

Make sure your virtual environment is activated before you verify if our package works properly. 

In the terminal/command, run `python3` for Linux users or run `py` for Windows users. Then, type the following code to make sure that the multiply and divide packages work as expected:

```
from multiply.by_three import multiply_by_three
from divide.by_three import divide_by_three

multiply_by_three(9)
divide_by_three(21)

# Output: 27
# Output: 7

```

Remember that we need to import the methods from our modules that we need to perform the desired operations, as we did above.

Hooray! Our package works as expected.

So, once you test and experiment with your package, follow the instructions below to upload your package to the real PyPI:

1. Go to [PyPI](https://pypi.org/) and create an account.
2. Run `twine upload dist/*` in the terminal/command line.
3. Enter the account credentials you registered for on the actual PyPI.
4. Then, run `pip install [package_name]` to install your package.

Congratulations! Your package was installed from the real PyPI.

## What's next?

It would be great if you come up with a simple idea and build with it your first real Python package. In this blog post, I focused only on the basics you need to get started, but there is a lot to learn in the world of packaging. 

Hopefully, my first experience with developing Python packages helps you learn what you need to get building. If you have any questions, feel free to connect and hit me up at any time on [LinkedIn](https://www.linkedin.com/in/rochdi-khalid/). Also, you can subscribe to my [channel](https://www.youtube.com/channel/UCF8iZXSsjgc8kE8hITp5rdQ) on YouTube where I share videos on what I'm learning and building with code.

See you in the next post and keep moving forward!

### References

Here are some references that helped me develop my first Python package:

* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Configuring metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata)
* [PEP 621 – Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/#example)
* [Glossary - Python Packaging User Guide](https://packaging.python.org/en/latest/glossary/#term-Source-Archive)


