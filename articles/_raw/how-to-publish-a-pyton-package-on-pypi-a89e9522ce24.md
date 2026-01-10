---
title: How to publish your own Python Package on PyPi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-19T02:09:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-a-pyton-package-on-pypi-a89e9522ce24
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OebmlFYpKPFJJ-qT2qSfiA.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Marco Massenzio

  Want to share your Python code with other developers? Want to make your users’ lives
  easier when installing your package? Then you should publish your Python packages
  to PyPi.

  The good news is that it is now easier than ever. This ...'
---

By Marco Massenzio

Want to share your Python code with other developers? Want to make your users’ lives easier when installing your package? Then you should publish your Python packages to PyPi.

The good news is that it is now easier than ever. This is a short guide that will walk you through the process and point you toward relevant documentation along the way.

### Step #1: Create a setup.py file

The arguments for _setup()_ are documented [here](https://packaging.python.org/distributing/#setup-args) and are non-trivial. A good example to go by is my [filecrypt](https://github.com/massenz/filecrypt) project’s _setup.py_ file.

Below is a brief excerpt. Again, be sure to [read the documentation](https://packaging.python.org/distributing/#setup-args) for more info on this, since it explains what all these arguments mean much better than I could, even with a full Medium article to do it:

```
setup(name='crytto',      description='An OpenSSL-based file encryption                    and decryption utility',      long_description=long_description,      version='0.2.0',      url='https://github.com/massenz/filecrypt',      author='M. Massenzio',      author_email='marco@alertavert.com',      license='Apache2',      classifiers=[          'Development Status :: 4 - Beta',          'Intended Audience :: System Administrators',          'License :: OSI Approved :: Apache Software License',          'Programming Language :: Python :: 3'      ],      packages=['crytto'],      install_requires=[          'PyYAML>=3.11',          'sh>=1.11'      ],      entry_points={          'console_scripts': [              'encrypt=crytto.main:run'          ]      })
```

**Note:** Do **not** confuse setuptools with distutils — here’s the correct import for setup.py:

```
from setuptools import setup
```

The trickiest part is figuring out package names and the correct configuration for your _script files._ It’s probably best to decide these in advance, but you can always rectify these while crafting your setup.py.

The biggest challenge is to come up with a top-level package name that does not conflict with an existing one. As far as I can tell, it’s currently mostly a process of trial-and-error.

Once the setup.py is in decent shape, you can try and build a wheel:

```
python setup.py bdist_wheel
```

After doing that, it’s good practice to create a new virtualenv, and try to install the new package in that one:

```
virtualenv test_env./test_env/bin/activatepip install dist/my-project.whl
```

This is particularly useful for testing out whether the _console_scripts_ have been correctly configured.

If you use _classifiers_ as in:

```
classifiers=[     'Development Status :: 4 - Beta',     'Intended Audience :: System Administrators',     'License :: OSI Approved :: Apache Software License',    'Programming Language :: Python :: 3']
```

…then make sure to consult the [classifiers list](https://pypi.python.org/pypi?%3Aaction=list_classifiers), as anything else will cause an error and prevent registration.

### Register your Project

![Image](https://cdn-media-1.freecodecamp.org/images/0kPl1058z7-o9Hw-0VLNSkuHpuIjLTsx7R6i)

**Note:** The documentation told me to use twine for this step, but it didn’t work for me. Your mileage may vary.

Unless you have already have an account on PyPi, you’ll need to [create one](https://pypi.python.org/pypi?%3Aaction=register_form), then log in.

You can then head over to the [registration form](https://pypi.python.org/pypi?%3Aaction=submit_form) and upload your **PKG_INFO** file. This has been created in a _[prj name].egg-info/_ directory. It may take a bit of back and forth, while you try to appease the Gods of PyPi to accept your configuration choices.

In particular, coming up with a non-conflicting-yet-meaningful package name may take more attempts than you’d expect. Again, I recommend you plan, as I’ve been unable to find an easy way to list **all** package names. If you do know of one, be sure to leave a comment. You’ll note that, according to PyPi…

```
There are currently 88906 packages here.
```

(“here” being PyPi, as of September 16, 2016).

### Upload to PyPi

Once registration succeeds, the actual upload is rather easy, using twine:

```
twine upload dist/*
```

Provided you have a valid ~/.pypirc, it will just ask for your password. Then you just need to:

```
$ cat ~/.pypirc [distutils] index-servers=pypi
```

```
[pypi] repository = https://upload.pypi.org/legacy/ username = [your username]
```

That's it. Enjoy building and sharing your Python packages!

_I originally published this on my blog at [codetrips.com](https://codetrips.com/2016/09/19/how-to-publish-a-pyton-package-on-pypi/)._

