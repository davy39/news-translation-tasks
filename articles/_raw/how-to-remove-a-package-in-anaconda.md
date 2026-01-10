---
title: Conda Remove Package - How To Remove Matplotlib in Anaconda
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-12T12:21:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-package-in-anaconda
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/joshua-woroniecki-lzh3hPtJz9c-unsplash.jpg
tags:
- name: anaconda
  slug: anaconda
- name: Matplotlib
  slug: matplotlib
seo_title: null
seo_desc: "You can use Conda to create and manage different environments and their\
  \ packages. It is mostly used for data science and machine learning projects. \n\
  In this article, you'll learn how to remove an environment's package using in built\
  \ Conda commands. \n..."
---

You can use Conda to create and manage different environments and their packages. It is mostly used for data science and machine learning projects. 

In this article, you'll learn how to remove an environment's package using in built Conda commands. 

You'll learn the following: 

* How to create an environment. 
* How to install packages in an environment. 
* How to remove/delete an environment's package. 

Let's get started!

## How To Create an Environment in Conda

You can use the `conda create package-name` to create a new environment in Conda. 

Here's an example:

```bash
conda create -n package-tutorial
```

The command above creates an environment called `package-tutorial`.

You can activate or switch to the `package-tutorial` environment using the `conda activate environment-name` command. That is:

```bash
conda activate package-tutorial
```

## How To Install Packages in a Conda Environment

In the last section, we created and activated an environment called `package-tutorial`. 

In this section, you'll see how to install a package in that environment. Let's install Matplotlib. 

You can install a package using the `conda install package-name` command.

Here's one of the command for installing Matplotlib in Conda: 

```bash
conda install -c conda-forge matplotlib
```

The installation might take a while to download and extract the package. You can check the packages that exist in your environment using `conda list` command. 

Once the installation is complete, use the `conda list` command to verify that the package has been installed in your environment. 

## How To Remove a Package in Conda

You can remove a package in the current environment by running the `conda remove package-name` command. 

In our case, we want to remove Matplotlib from the current environment (`package-tutorial` environment):

```bash
conda remove matplotlib
```

The command above removes Matplotlib from the current environment. When you run the `conda list` command, Matplotlib will no longer be listed as a package.

## Summary

In this article, we talked about packages in Conda. They can be installed in Conda environments. 

We saw how to create and activate a Conda environment . We also saw how to install and remove packages in Conda. 

Happy coding!

