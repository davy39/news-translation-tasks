---
title: How to use GitHub as a PyPi server
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2018-11-15T17:59:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E3Pn3GrE2DBJRBV8r1W__w.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'I was looking for a hosted private PyPi Python Package server, that used
  credentials that the team already has (such as GitHub).

  I didn’t want to create an on-premises server. For us, it would make it impossible
  to use cloud-based build servers, and ...'
---

I was looking for a hosted private PyPi Python Package server, that used credentials that the team already has (such as GitHub).

I didn’t want to create an on-premises server. For us, it would make it impossible to use cloud-based build servers, and it is another moving part that can go wrong. There are also potential issues with fine-grained security and speed. (We have a worldwide team, so serving the content via a [CDN](https://www.webopedia.com/TERM/C/CDN.html) would be helpful.)

I didn’t want to force the team to create accounts with another provider. They already have Active Directory and GitHub accounts. It is an annoyance for them and creates a governance burden for me.

Sadly, I couldn’t find such a service. [GemFury](https://gemfury.com/) is excellent but doesn't support GitHub authorization (at the team / organisation level) and [Packagr](https://www.packagr.app) doesn’t support GitHub authorisation at all. [MyGet](https://docs.myget.org/) is also excellent, it does allow me to use GitHub authorization, but doesn’t host Python packages. Azure DevOps has something that looks promising, but it’s in [private beta](https://docs.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages?view=vsts) at the moment.

Happily, this is possible using cloud Git repositories such as GitHub, GitLab and BitBucket.

### Pip can install packages from Git

I have hosted a Python package on GitHub ([python_world](https://github.com/ceddlyburge/python_world)), which you can install with the following command (make sure you trust me before running this command and installing my code on your computer).

`pip install git+https://github.com/ceddlyburge/python_world#egg=python_world`

Pip provides options to install from head, from a branch, from a tag or from a commit. I usually tag each release and install from these tags. See the [pip install documentation for full details](https://pip.pypa.io/en/stable/reference/pip_install/#git).

This repository is public, but it works just the same with a private repo, as long as you have permission. There is no special magic (it's a vanilla Python package) and [Setup.py](https://github.com/ceddlyburge/python_world/blob/master/setup.py) does most of the work as normal.

If you are new to creating Python Packages, the [Packaging Python Projects tutorial](https://packaging.python.org/tutorials/packaging-projects/) is worth a quick read.

### Setuptools can also install dependencies from Git

[Setuptools](https://pypi.org/project/setuptools/) is how most people create Python packages.

I have hosted another package on GitHub [python_hello](https://github.com/ceddlyburge/python_hello), which depends on [python_world](https://github.com/ceddlyburge/python_world). (I’m sure you can see where this is going.)

The relevant bits from setup.py are below. `install_requires` specifies that `python_world` is a required dependency and tells Setuptools where to find it.

```python
install_requires=[
	'python_world@git+https://github.com/ceddlyburge/python_world#egg=python_world-0.0.1',
]
```

You can install this package using the command below. It will also download the dependent `python_world` package.

`pip install git+https://github.com/ceddlyburge/python_hello#egg=python_hello`

This links to a specific version of `python_world`, which is a shame as it means that pip can't do any dependency management (such as working out an acceptable version if multiple things are reliant on it). However, by the end of this article, we will have removed the need for the specific link.

### Python environments

As everyone who has used Python without an environment knows, environments save a lot of frustration and wasted time. So we need to support those.

I have created a repo ([use-hello-world](https://github.com/ceddlyburge/python_use_hello_world)) that defines `python_hello` as a dependency in [requirements.txt](https://github.com/ceddlyburge/python_use_hello_world/blob/master/requirements.txt) for [Virtualenv](https://virtualenv.pypa.io/), and [environment.yml](https://github.com/ceddlyburge/python_use_hello_world/blob/master/environment.yml) for [Conda](https://www.anaconda.com).

If you download the repo, you can install the dependencies into a virtualenv with the following command.

`pip install -r requirements.txt`

If you are using conda you can use this command:

`conda env create -n use-hello-world`

### PyPi Index

So far we are able to install packages from our private Git repositories. These packages can, in turn, define dependencies to other private repositories. There still isn’t a PyPi server in sight.

We could stop at this point. However, the syntax for defining dependencies is a bit mysterious. It would be difficult for the team to discover which packages are available, and we are linking to specific versions of dependent packages, instead of letting pip manage it.

To fix this we can set up a PyPi index that conforms to [Pep 503](https://www.python.org/dev/peps/pep-0503). This specification is quite simple, and I have just created the index by hand. If this becomes too cumbersome I can generate it from the GitHub API.

I created this [PyPi Index](https://ceddlyburge.github.io/python-package-server/) using GitHub Pages. There are equivalent things for GitLab and BitBucket. You can see that the [source code](https://github.com/ceddlyburge/python-package-server/) is very simple. GitHub Pages sites are always public (and there is probably no sensitive information in your index). However, if you need them to be private you can use a service such as [PrivateHub](https://www.privatehub.cloud/).

One thing to look out for is the [name normalisation](https://www.python.org/dev/peps/pep-0503/#normalized-names) of the specification. This requires the `python_hello` package information to be present at `python-hello/index.html` (note the change from an underscore to a dash).

Now that we have a PyPi server, we can install packages using the command below.

`pip install python_hello --extra-index-url [https://ceddlyburge.github.io/python-package-server/](https://ceddlyburge.github.io/python-package-server/)`

So that you can see this working with environments, I have created another repo ([use_hello_world_from_server](https://github.com/ceddlyburge/python_use_hello_world_from_server)) that defines the `python_hello` dependency using this PyPi index instead of direct GitHub Links. If you are trying it with Conda, version >4.4 is required.

At this point, we can go back and remove the direct Git link in [install_requires in setup.py of python_hello](https://github.com/ceddlyburge/python_hello_world/blob/master/setup.py) (as Setuptools will be able to find it from our server).

### Conclusions

Using a cloud-hosted Git provider as a PyPi server is a viable option. If you are already using one, that means that you can reuse the credentials and permissions that you already have. It will work with Cloud build servers and is likely to be provided via a CDN, so will be fast worldwide. It requires more knowledge to set up than a hosted server, but probably the same or less than hosting your own server on premises.

### Hints and tips

Serving the index locally can help to troubleshoot problems (such as name normalization). It’s easy to see what requests are being made. You can use the inbuilt python HTTP server for this (`python -m Http.Server -8000`). This led me to find out that `pip search` uses `post`requests, so won’t work with GitHub pages.

You can run `python setup.py -install` to check your pip packages locally, before pushing them to Git.

