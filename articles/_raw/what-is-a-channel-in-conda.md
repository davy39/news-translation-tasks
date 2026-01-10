---
title: Conda Channel - What Is a Channel in Conda?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-14T16:36:11.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-channel-in-conda
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/freestocks-11SgH7U6TmI-unsplash.jpg
tags:
- name: anaconda
  slug: anaconda
seo_title: null
seo_desc: 'When you install a package in Conda, it is downloaded and extracted from
  a remote directory using the directory''s URL. The directory where these packages
  are stored is known as a channel.

  In this article, you''ll learn what a channel is, how to use de...'
---

When you install a package in Conda, it is downloaded and extracted from a remote directory using the directory's URL. The directory where these packages are stored is known as a channel.

In this article, you'll learn what a channel is, how to use default channels, and how add new channels in Conda.

## What Is a Channel in Conda?

A channel is the location where packages are stored remotely. 

When you install Conda for the first time, it comes with a channel called `default`. You can check that using the command below:

```bash
conda config --show channels
```

The `default` channel enables you to install packages that are currently available in its directory/storage.

To install a package using the `default` channel, you use the `conda install` command followed by the name of the package. That is:

```bash
conda install package-name
```

Although numerous packages can be installed from the `default` channel, it's possible to come across packages that are not accessible from it. 

In cases like this, you'd usually get the "PackagesNotFoundError: The following channels are not available from current channels" error message. 

You'll see a workaround for that error in the next section. 

## How To Install a Package in Conda Using a Channel Name

In this section, you'll learn how to install a package that isn't available from the `default` channel in Conda by specifying the name of the channel where that package is stored remotely. 

You'll also see how to add a channel to your list of channels.

Here's an example using Matplotlib:

```bash
conda install -c conda-forge matplotlib
```

In the command above:

* The `-c` flage denotes the word channel.
* `conda-forge` denotes the name of the channel where Matplotlib was installed from. 

Although we installed Matplotlib from `conda-forge`, `conda-forge`will not be added to our list of channels. 

So if you run the `conda config --show channels` command, you'd only see the `default` channel. 

You can add a channel to the list of channels using the `conda config --add channels channel-name` command. That is:

```bash
conda config --add channels conda-forge
```

The command above will add `conda-forge` to the list of Conda channels. This means that you don't have to specify the channel name if you are installing a package that is available from the `conda-forge` channel. 

## Summary

In this article, we talked about channels in Conda. They are used to access packages remotely. 

We saw how to use Conda's default channel to install packages. We also saw how to use and add new channels that aren't built into Conda.

Happy coding!

