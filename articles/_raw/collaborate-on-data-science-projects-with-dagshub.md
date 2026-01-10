---
title: How to Collaborate on Data Science Projects with DAGsHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T19:13:20.000Z'
originalURL: https://freecodecamp.org/news/collaborate-on-data-science-projects-with-dagshub
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/dagshub-storage.png
tags:
- name: Data Science
  slug: data-science
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Linda Ikechukwu

  For software engineering teams, tools like Git and remote Git clients like GitHub,
  GitLab, and BitBucket have made collaboration easy and uncomplicated.

  They let different developers in different locations work on and contribute to...'
---

By Linda Ikechukwu

For software engineering teams, tools like Git and remote Git clients like GitHub, GitLab, and BitBucket have made collaboration easy and uncomplicated.

They let different developers in different locations work on and contribute to the same project seamlessly. This ability to easily collaborate on projects has fostered the development of the massive open-source software/libraries ecosystem.

Unfortunately, the same cannot readily be said for data science teams. Even the most adept data science teams still lack best practices for organizing their projects and collaborating effectively. 

The data science field is a combination of software engineering and research, that is code + datasets, trained models, and label encodings. Just as it’s elementary to control version history and remotely collaborate on code with a few git commands, data scientists should be able to browse, preview, share, fork, and merge data & models with ease.

Two things have to be in place to aid remote collaboration: version control and remote central storage. 

Just as Git allows software engineers to safely go back and forth between different versions of their code, data scientists need to control not only different versions of their code but also different versions of their data. 

They should also be able to keep track of what they did to achieve a particular state for a particular version and also be able to reproduce the same state when needed.

So, what are the possible solutions?

## Option 1: Using Git for Version Control in Data Science Projects

You might already be asking – can’t we just use Git? The problem is that Git has a file size limit of 100MB. This wouldn’t be enough for serious data science projects that sometimes have data files that run into gigabytes. 

A solution would be to add [Git LFS](https://www.atlassian.com/git/tutorials/git-lfs) (Large File Storage) to the mix.

Git LFS is a git extension for handling the file size restriction in Git. It does this by creating a pointer file in which it stores references to the large data files. These large files will be stored somewhere else – either in the local Git LFS cache or a remote server like [GitHub](https://docs.github.com/en/github/managing-large-files/collaboration-with-git-large-file-storage) or [Gitlab](https://docs.gitlab.com/ee/topics/git/lfs/).

Still, this wouldn’t be good enough. Git LFS still limits file size (around 2GB) and is not a full-fledged data science solution. It doesn’t provide useful information on what has changed for large file versions (only text-based changes in the pointer file). You also won’t have access to before and after visualizations or graphs. 

Git LFS also doesn’t support diffs out of the box, so it’s quite challenging to examine the difference between subsequent versions of a file.

## Option 2: Using DVC for Version Control in Data Science Projects

A better option is to use [DVC](https://dvc.org/). DVC, which stands for data version control, is essentially like Git but was made especially for data. 

And DVC’s syntax is similar to Git! So, if you already know Git, learning DVC won’t be difficult. DVC tracks large files easily — which makes reusability and reproducibility a piece of cake. 

With DVC, you can:

* track and save data and machine learning models the same way you capture code
* create and switch between versions of data and ML models easily
* understand how datasets and ML artifacts were built in the first place
* compare model metrics among experiments
* adopt engineering tools and best practices in data science projects

But still, DVC only aids version control locally. To set it up for remote collaboration, you need to connect it to [remote storage](https://dvc.org/doc/command-reference/remote#description). The problem is that setting up this cloud storage is just too much of a hassle.

Take Amazon S3, for example. You’ll have to provide your credit card, install the AWS CLI tool, create an IAM user, assign the correct permissions (which most people usually don’t get right on the first try), and so on. 

That’s just way too complicated. This level of friction can discourage people from contributing to the project – which is the whole purpose of remote collaboration. 

Things should be as easy as creating an account and Git push. Access control should also be handled automatically. 

And this is where DagsHub Storage comes in.

## Option 3: Using DVC + DAGsHub Storage for Version Control and Remote Collaboration

[DAGsHub Storage](https://dagshub.com/docs/reference/onboard_storage/) is an alternative (and free-to-use) DVC remote that requires zero configurations. It is a new tool from the makers of DAGsHub, a web platform for data version control and collaboration for data scientists and machine learning engineers (DAGsHub is to DVC what Github is to Git). 

With DAGsHub storage, you don’t have to go through the stress of setting up anything. It works the same way as adding a Git remote. 

When you create a repository on DagsHub, it automatically provides you with a DVC remote URL. With this URL, you can quickly push and pull data using your existing DAGsHub credentials (via HTTPS basic authentication). 

This also means that sharing work with non-DVC users is much easier, as there is no cloud setup required on their end. Isn’t that so much better?

To connect DAGsHub Storage as your remote storage, you need to create an account on DAGsHub and create a project. You can do this either by creating one from scratch or connecting to an existing project on another platform like Github or Bitbucket, and [setting up DVC for local data versioning](https://dagshub.com/docs/experiment-tutorial/2-data-versioning/).  


![Image](https://lh5.googleusercontent.com/pptgXgKjG8tKKl1edmThDD-fsvmckeNcOTo5lBlT3bnexEr_JgQWvaHd6z0OkLdvBF9EG5fHDnnvsRuCBppijm4QbkEJFalBGdCs-QdRnaPQFa7buMwmI6r5ez70px1yec3isZhx)
_Creating a new repository on DAGsHub._

When you create a repo on DAGsHub, you get two remotes: Git and DVC. 

![Image](https://lh4.googleusercontent.com/HzmNRfDG774q_7TeuwytoXTk2qmbEwxlrzofsYBu0rosNI_oHfp8nZK0O_hc0w7v2vxrTTONyHrJmusQe2BXMkljb699aN2dYolx_Xgf9gbLcepxChanbTn4bghIKH6jiivdnDFu)

  
To get started using DAGsHub storage, copy the DVC link (which can be found on your repo’s homepage) and add it as a remote for your local project.

Open your project in a terminal and add the DVC remote: 

```
dvc remote add <--dvc remote link-->

```

Next thing is to set up DAGsHub credentials for your local machine, just the way you would for GitHub: 

```
dvc remote modify origin --local auth basic
dvc remote modify origin --local user Linda-Ikechukwu
dvc remote modify origin --local ask_password true
```

And voilà! You can now either push or pull datasets and models seamlessly with `dvc push -r origin` or  `dvc pull -r origin`. 

If you want to switch to different versions of your data, just like you do git checkout, all you have to do is run: 

```
git checkout <..branch or commit..>
dvc checkout

```

What’s more? You can also receive and merge pull requests to your project with [DAGsHub pull requests](https://dagshub.com/docs/collaborating_on_dagshub/data_science_pull_requests/).

## Conclusion

With DAGsHub Storage, sharing data and models becomes as easy as sharing a link, offering collaborators an easy overview of project data, models, code, experiments, and pipelines. 

All of this provides a better collaborative experience for data science teams and will hopefully aid in massive development and acceptance of Open Source Data Science (OSDS) projects.

Looking for more articles like this?

My name is Linda and I'm a Frontend developer. I run a blog: [codewithlinda](https://www.codewithlinda.com/blog/), targeted at growing frontend developers where I write about how to get and survive your first tech job and also technical tips to help you level up. You can also find me on twitter at @[_MsLinda](https://twitter.com/_MsLinda).  


  


  


  


  

