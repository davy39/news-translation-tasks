---
title: 'The Google Doc of Coding: Git & GitHub'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-23T01:16:38.000Z'
originalURL: https://freecodecamp.org/news/the-google-doc-of-coding-git-github-ec103e87926d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e5O_94Tw9eUfUAbQVnVr_Q.png
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yung L. Leung

  Introduction

  Google Doc is a server-side (online) word processor. A user’s files are created
  via a web browser & stored in a server. This software makes it possible for users
  to share documents with others for collaboration. Normally...'
---

By Yung L. Leung

### **Introduction**

Google Doc is a server-side (online) word processor. A user’s files are created via a web browser & stored in a server. This software makes it possible for users to share documents with others for collaboration. Normally, the workflow is the following:

* Create a document & fill with content.
* Save content & share file with others for collaboration.
* Members contribute on the same document, online.

Aside from file sharing, another important feature is the ability to undo or redo changes made to the ‘master’ file. The changes made to the document are sequential and any user can undo (or redo) those changes.

![Image](https://cdn-media-1.freecodecamp.org/images/Wk3M8qv3BVmUo8xK8WTiFKo8qtJzdOlOuc59)

But, this can quickly become a big mess, especially when multiple users are simultaneously adding or editing content. Who created or changed what content and for what reason is unknown.

### Atom, Git & GitHub

In software development, the tools for collaborative programming consists of a text editor, version control system & an online repository.

**Atom (**or any text editor**)** is like your client-side (desktop) word processor, except the document is code written in some language (i.e: JavaScript).

**Git** is a tool for selectively recording the history of your project’s saved changes. It is a way to ‘**control**’ all the **different versions** of your programming project.

**GitHub** is like your Google Docs, except you can create & save your version of the code offline, before ‘**pushing**’ it to be saved online.

![Image](https://cdn-media-1.freecodecamp.org/images/jLU1vB1GLr3vSedxMo-viUIvU4HtNfzCfrnY)
_Atom, Git &amp; GitHub_

So, you have your **text editor** **(**Atom**)**, **version control system (**Git**)** & **remote file storage system (**GitHub**)**. These are the basic elements that solve the problem of collaboration, especially for software developers. The workflow is similar to the use of Google Docs, with some differences.

### Collaborative Software Development Workflow

1. **Create online (**remote**) GitHub repository (**[https://github.com/new](https://github.com/new)**)**

![Image](https://cdn-media-1.freecodecamp.org/images/XEkgb2eqPgGSa7dz5imdRFXhyjcDzFfa8zJ1)

**2. Create an offline (**local**) repository.** The terminal command **git init** **_project_name_** initiates your project by creating a folder to store its content & version control files to store a history of its changes

* The idea is to eventually have a remote & a local copy of your project.

![Image](https://cdn-media-1.freecodecamp.org/images/YVsP0MYeOVIygYs4cz9x3NmjdsdRyue53aw7)

**3. Use a text editor to build content.** This is where you begin to write your program with Atom and create your JavaScript files.

![Image](https://cdn-media-1.freecodecamp.org/images/BIlW7r0KUNAyOXzkjQbNrXmSykewezNpGQRv)
_Coding with an Atom Text Editor_

**4. Save the content & note significant historical progressions in your project.** The terminal command **git add .** adds all folder contents, all the changes, **_to be committed_** in history. The command **git commit -m ‘message’** commits the changes to history, along with a message explaining the changes made. The command **git push** pushes your files and historical data to your remote repository.

* As you are continuously making progress in your project, you are recording the rationale behind each stage of development (git add, git commit, git push).

![Image](https://cdn-media-1.freecodecamp.org/images/sphMS4DSgfC8zZI4yky53GMI-6gWU5qCVdRQ)
_Your remote &amp; local copy grows with every push._

**5. Share file with others for collaboration.** Once your remote repository has content, you can share your project with collaborators.

![Image](https://cdn-media-1.freecodecamp.org/images/Viri6BCHeiLtcq9cxUGYFMGUmqNQ1pkUAHIa)

* After members accept the invitation, they can fork a branch off of the remote repository and clone the project locally (**git clone** **_<repo url or s_**sh>).

![Image](https://cdn-media-1.freecodecamp.org/images/wUhCAZn3Q6ieiNbNo9KK3Y3o4bRkytIGIPh-)
_Originator with two collaborators building content on project clones._

* Each collaborator can build content, save the content and push it to their remote branch.
* As collaborators continue to build and save their content, they end up building forks in the GitHub “sky” (**git add**, **git commit**, **git push**).

![Image](https://cdn-media-1.freecodecamp.org/images/AiMhl6s958Kgw6Q1Ev1xoHTiHEjftaId7yWC)
_Originator &amp; Collaborators developing project &amp; pushing it to GitHub._

* Each fork is a collaborator branching off from the original project so that members can work in parallel with the originator, without disrupting each other’s progress. Every time a collaborator performs a **git push**, the fork elongates.

**6. Merge branched files.** At the request of the collaborators, the **originator** can pull their branch to be merged with the master branch.

![Image](https://cdn-media-1.freecodecamp.org/images/NKXd9qyn0FphVnA-rAwtUXDesF7arDnJCRut)
_Collaborators are pushing &amp; submitting pull requests. The originator is pulling clones &amp; merging the branches._

* When a collaborator submits a pull request, the originator can perform a **git pull** to merge the branches into a single updated version of the project. This new version can then be pushed into the remote repo for all to see and use.

### Version Control & File Sharing

In collaborative software development, changes are made to multiple clones of a master copy, before they are merged to the master file. So the changes made are sequential, but with overlaps in time.

![Image](https://cdn-media-1.freecodecamp.org/images/uh4g7TmUn95gPVPP3SV1Z-HXTtDzZnCZkXeh)
_Collaborators forking, pushing &amp; having their branches merged with the Originator, at different times._

Every new piece of content that is created on a clone is ultimately pushed towards a collaborator’s master repo. Every collaborator’s commit message provides feedback to the originator so that they can make intelligible edits & additions to the original project.

This would be a difficult feat without **Git’s** version control & **GitHub’s** file sharing. A simple terminal command (**git branch &**lt;branch_n**a**me>) can take a clone on a local machine and create a branch so that a different version of the project can be developed. A user can then note take their progres**sion (git add & git** commit) at any point in time. If there were any problems with an active version, the user can simply switch to a previous br**anch (git chec**kout <br**a**nch_name>) and continue from there.

This is the meaning of **version control**. At any point in time, a user can switch to alternate versions of a project, while committing intelligible notes that explain the progression of each version. The user has full control over the versions that are developed. A simple terminal push to the GitHub “clouds” makes any version available to their collaborators. This is the power of using Git & GitHub in collaborative software development.

**References:**

[**Git - Videos**](https://git-scm.com/videos)  
[_Edit description_git-scm.com](https://git-scm.com/videos)[**_Learn Git with Bitbucket Cloud_ | Atlassian Git Tutorial**](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)  
[Learn Git with Bitbucket Cloudwww.atlassian.com](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)[**How Google Docs Works**](https://computer.howstuffworks.com/internet/basics/google-docs5.htm)  
[_Back End of Google Docs - The back end of Google Docs relies on simple, inexpensive hardware and software. Learn more…_computer.howstuffworks.com](https://computer.howstuffworks.com/internet/basics/google-docs5.htm)[**Atom (text editor) - Wikipedia**](https://en.wikipedia.org/wiki/Atom_(text_editor))  
[_Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows with support for…_en.wikipedia.org](https://en.wikipedia.org/wiki/Atom_(text_editor))[**Git - Wikipedia**](https://en.wikipedia.org/wiki/Git)  
[_Git () is a distributed version control system for tracking changes in source code during software development. It is…_en.wikipedia.org](https://en.wikipedia.org/wiki/Git)[**GitHub - Wikipedia**](https://en.wikipedia.org/wiki/GitHub)  
[_GitHub offers plans for enterprise, team, pro and free accounts which are commonly used to host open-source software…_en.wikipedia.org](https://en.wikipedia.org/wiki/GitHub)

