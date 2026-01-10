---
title: How to Participate in Hacktoberfest – Even if You Don't Write Code
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-10-06T15:14:48.000Z'
originalURL: https://freecodecamp.org/news/how-anyone-can-participate-in-hacktoberfest
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/untitled.png
tags:
- name: hacktoberfest
  slug: hacktoberfest
- name: open source
  slug: open-source
seo_title: null
seo_desc: 'Hacktoberfest is an event hosted by DigitalOcean that partners with many
  organizations. The goal is to give back and contribute to open-source projects.
  The organizers offer little incentives for a job well done, like a shirt and stickers.

  Other orga...'
---

[Hacktoberfest](https://hacktoberfest.digitalocean.com/) is an event hosted by [DigitalOcean](https://www.digitalocean.com/) that partners with many organizations. The goal is to give back and contribute to open-source projects. The organizers offer little incentives for a job well done, like a shirt and stickers.

Other organizations also get involved by offering their own rewards. You can find a community-sourced list of organizations offering incentives to contribute on [Hacktoberfest Swag](https://hacktoberfest-swag.com/).

Only meaningful contributions will count toward the total 4 required. Take your time and show common courtesy with maintainers to ensure your pull requests get merged. More on this in [Let's Avoid Turning it into Spamtoberfest](#heading-lets-avoid-turning-it-into-spamtoberfest) below.

## How you can Participate in Hacktoberfest

It's important to note that Hacktoberfest is for making any **quality** contribution to open-source projects. No one said it has to be code!

Everyone is capable of putting something forward:

* Authors
    
* Artists
    
* Software Developers
    
* Technical Writers
    
* Translators
    

### Recommended Projects for Hacktoberfest Contributions

I'm not going to explicitly list repositories for contributing code because that's easy enough to find. All repositories listed on the following links have opted-in to Hacktoberfest.

* [GitLab](https://gitlab.com/explore/projects?topic=hacktoberfest) (All repositories with the topic `hacktoberfest` on GitLab.)
    
* [GitHub](https://github.com/topics/hacktoberfest) (All repositories with the topic `hacktoberfest` on GitHub.)
    

Below are projects I recommend if you don't know how to code but still want to contribute to open-source (or [Creative Commons](https://creativecommons.org/)) projects. It only includes projects that have manually opted-in to Hacktoberfest.

You shouldn't need to know any programming languages or HTML to contribute to them. You will be expected to know how to commit your work with Git, though, which we'll cover later.

#### Art

Projects that need art or animations:

* [Cult of the Party Parrot](https://github.com/jmhobbs/cultofthepartyparrot.com) — Animated parrot emojis.
    
* [Elypia Emotes](https://gitlab.com/Elypia/elypia-emotes) — Red panda emojis.
    

#### Awesome Lists

Community-maintained lists of resources:

* [Awesome Mechanical Keyboard](https://github.com/BenRoe/awesome-mechanical-keyboard) ­— List of open-source keyboards.
    
* [Free Programming Books](https://github.com/EbookFoundation/free-programming-books/) — List of free books anyone can access.
    
* [Free Science Books](https://github.com/EbookFoundation/free-science-books) — List of free books anyone can access.
    
* [Remote-Friendly Companies](https://github.com/remoteintech/remote-jobs) — List of remote-friendly companies.
    

#### Books

Free eBooks maintained with a docs-as-code approach:

* [Introduction to Bash Scripting](https://github.com/bobbyiliev/introduction-to-bash-scripting) — Free eBook for Bash.
    

#### Configuration

Projects that revolve around configuration files. A contribution could just be appending an entry to a JSON file:

* [2fa.directory](https://github.com/2factorauth/twofactorauth) — List of sites with 2FA. ([More Info](https://github.com/2factorauth/twofactorauth/tree/master/entries))
    

#### Documentation

Projects where you just have to type in plain English. Programming and technical knowledge will help, but there's no need for a specialized skill.

This only includes repositories that maintain documentation in a format that would be simple for most users, like [Markdown](https://commonmark.org/help/).

* [.NET Docs](https://github.com/dotnet/docs) — Documentation for .NET.
    
* [GitHub Docs](https://github.com/github/docs) — Documentation for GitHub.
    
* [Jellyfin Docs](https://github.com/jellyfin/jellyfin-docs) — Documentation for Jellyfin.
    
* [Nextcloud Docs](https://github.com/nextcloud/documentation) — Documentation for Nextcloud.
    
* [tldr-pages](https://github.com/tldr-pages/tldr) — Cheat sheets for CLI applications.
    

#### Translations

Projects that need text translated from English to other languages.

Projects that use crowd-translations platforms like [Weblate](https://weblate.org/) aren't included here, since the translator doesn't create the pull request. Unfortunately, Hacktoberfest only considers whoever opened the pull request, not the authors of the changes.

Please make sure that you only contribute human-reviewed translations – so either translated by a human, or machine-translated but verified by a human. Again, quality is important.

* [Free Programming Books](https://github.com/EbookFoundation/free-programming-books/) — Translate health files.
    
* [tldr-pages](https://github.com/tldr-pages/tldr) — Translate cheat sheets.
    

#### Miscellaneous

Projects that are one of a kind:

* [Dumb Password Rules](https://github.com/duffn/dumb-password-rules) — List of sites with dumb password rules.
    
* [Hacktoberfest Swag](https://github.com/benbarth/hacktoberfest-swag) — List of projects rewarding contributors.
    

## Let's Avoid Turning it into Spamtoberfest

Unfortunately, Hacktoberfest has developed a bit of a bad reputation among some projects due to spam. Sometimes contributors can be a bit eager to complete Hacktoberfest and miss the point. ^-^'

From 2020, if a user makes 2 pull requests that get assigned a label with the word `spam` or `invalid` in it, the contributor will be banned from Hacktoberfest indefinitely, including future events.

[Mindustry](https://github.com/Anuken/Mindustry) handles this the best in my opinion with the [Hacktoberfest Hall of Shame](https://github.com/Anuken/Mindustry/pulls?q=label%3A%22hacktoberfest+hall+of+shame+%28invalid%29%22+).

From 2021, Hacktoberfest is doing more to crack down on spam by excluding projects that encourage pull requests with no value.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-8.png align="left")

*The goal of giving back to open-source gets undermined if most contributions just go to "Complete Hacktoberfest!" repositories.*

### How to make valuable Hacktoberfest contributions

* You have a month to make the 4 pull requests. Use it! They're more likely to get merged if you make fewer good quality pull requests.
    
* Don't assume every pull request you make will be merged before Hacktoberfest is over. Try to do more than 4 if you can!
    

### Practice common courtesy

Open-source maintainers have a life too. They don't always have time to review all pull requests, especially towards the end of Hacktoberfest.

Don't make maintainers feel bad, don't rush them, and don't demand attention. Just work on something else if they're busy.

## How to Commit Work and Open a Pull Request

Now that you know how to be a helpful Hacktoberfest participant, and you've learned about some projects you'll be able to contribute too, the only thing left is to actually learn how to contribute.

GitHub and GitLab both provide ways to simplify contributing for small changes. We're not going to use them because it'll be simpler to show a single set of instructions that will work everywhere rather than rely on platform-specific features.

Before you continue, pick a repository that you want to contribute to. If you're multilingual then tldr-pages will be easiest, otherwise consider Free Programming Books.

I'm going to use Free Programming Books in my examples.

### How to install Git

First, you should install Git which is a version control system. This is the tool that projects are using to manage changes.

Windows users can download it from the [git-scm](https://git-scm.com/) website. Linux users can install it using their preferred package manager.

Once you have Git installed, verify it's installed correctly with `git --version`.

Now configure your name and email address. The name doesn't matter, but you should specify the same email address you're using for Hacktoberfest.

```plaintext
git config --global user.name "Your Name"
git config --global user.email "your@email.org"
```

Note that the email address you specify here will be considered public information once your pull request has been merged. Anyone can view the details of a commit which includes the author details.

For example, my email address is in the output when I do `git log` on one of my commits.

```sh
commit 9647912b202a57474b4cd0ce796126c462c1ecc0 (HEAD -> added-react-book, develop/added-react-book)
Author: Seth Falco <seth@falco.fun>
Date:   Tue Oct 5 14:04:25 2021 +0200

    added a react book from digitalocean
```

If this is a problem, both [GitHub](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address#setting-your-commit-email-address-on-github) and [GitLab](https://docs.gitlab.com/ee/user/profile/index.html#use-an-automatically-generated-private-commit-email) provide a feature to hide your email address by giving you a disposable one. You can enable the feature and use that email address in `git config` instead.

### How to fork and clone a repository

Next, you'll want to fork the repository. You won't be allowed to push changes directly to the repository, so instead you'll make a fork which is a copy of the project that's under your control.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-10.png align="left")

*The "Fork" button is at the top-right of the repository page.*

Next, clone the repository locally. This pulls a copy of everything in the repository to your machine so you can start working on it.

We'll do this in the terminal. If you're on Windows you can use Command Prompt or [PowerShell](https://docs.microsoft.com/en-us/powershell/).

Go to an appropriate location on your file system like your `Downloads` or `Documents` directory, then execute this following:

* Clone the repository you want to work on.
    
* Enter the directory in the terminal.
    
* Link the repository with the fork on your account.
    

```sh
git clone https://github.com/EbookFoundation/free-programming-books.git
cd free-programming-books
git remote add develop https://github.com/{YOUR_USERNAME}/free-programming-books.md
```

### How to work with the project

Now that you've cloned the repository locally, you can start working with it. With most repositories, it's best to open it up in a code editor like [Visual Studio Code](https://code.visualstudio.com/), but you can technically work with any text editor including Notepad.

Open the directory containing the repository you cloned in your editor. By default, it's named after the repository name, for example I now have a folder named `free-programming-books`.

Now you can make changes:

* If you're not sure what to do, check if there's anything specific they need by looking under the "Issues" tab on the repository.
    
* Alternatively, make whatever *meaningful* change you want.
    

With Free Programming Books, it's a repository for maintaining a list of free eBooks, so we can add more resources to it.

[DigitalOcean](https://www.digitalocean.com/community/tags/book) has some great books in the community section of their website, so we can just add one or more of them to the repository. I've picked out [How To Code in React.js](https://www.digitalocean.com/community/books/how-to-code-in-react-js-ebook) for this example.

I can go to the respective section in the project which is the `books/free-programming-books-langs.md` file, and add the resource under the `React` section of the document.

The line I added looks like this:

```md
* [How To Code in React.js](https://www.digitalocean.com/community/books/how-to-code-in-react-js-ebook) - Joe Morgan
```

### How to commit your work

Now that you've made a change, you'll want to actually commit and push your work back up.

You've only made the change *locally* so far – now we want to send a pull request. This basically means you'll send a request asking the maintainer of the repository to include your changes in their repository.

In your terminal, we'll execute the following which will:

* Create a new branch.
    
* Tell Git you want to stage all changes to be saved.
    
* Commit the change with a message describing what you did.
    
* Push the changes to your fork.
    

```sh
git checkout -b added-react-book
git add .
git commit -m "added a react book from digitalocean"
git push develop added-react-book
```

This should hopefully produce output like the following:

```sh
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.07 KiB | 1.07 MiB/s, done.
Total 4 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: 
remote: Create a pull request for 'added-react-book' on GitHub by visiting:
remote:      https://github.com/SethFalco/free-programming-books/pull/new/added-react-book
remote: 
To github.com:SethFalco/free-programming-books.git
 * [new branch]        added-react-book -> added-react-book
```

### How to create a pull request

Both GitHub and GitLab will drop a link in the output of the command above that will take you to open a pull request.

If you click that link (you may need to hold `CTRL`), it'll take you to a page where you can provide more information and submit your pull request.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-11.png align="left")

Just fill in the details requested and click "Create pull request". All that's left is to wait for the maintainers to review it.

### Clean up the code

As soon as you've finished a pull request, you should leave your branch and go back to the primary branch of the repository.

Execute the following commands in your terminal:

* Check if the primary branch is `main` or `master`.
    
* Switch to the primary branch of the repository.
    
* Update your local copy to be in sync with the repository.
    

```sh
git branch
git checkout main
git pull
```

Restart from the "How to work with the project" step to make more changes.

## Conclusion

I hope this gives more information about Hacktoberfest, and that you feel more confident participating with the open-source community even if you don't write software.

Best of luck with your pull requests!
