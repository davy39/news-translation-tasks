---
title: 'A remote sync solution for iOS and Linux: Git and Working Copy'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-04-02T15:36:55.000Z'
originalURL: https://freecodecamp.org/news/a-remote-sync-solution-for-ios-and-linux-git-and-working-copy-1aba488b3547
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1fs_sMiHpsoYdX1uQMriYg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'How to set up a cross-platform cloud sync solution for working anywhere
  using Git on iOS.

  I previously wrote about a (hackish) way to use a single Dropbox folder on a dual-boot
  Windows and Linux machine. I’ve since gained some sense gone full Linux w...'
---

#### How to set up a cross-platform cloud sync solution for working anywhere using Git on iOS.

I previously wrote about a (hackish) way to use a [single Dropbox folder on a dual-boot Windows and Linux machine](https://victoria.dev/verbose/how-i-set-up-a-single-dropbox-folder-on-my-dual-boot-windows-and-linux-system/). I’ve since gained some sense gone full Linux with Ubuntu 18.04 LTS, but the Dropbox set up seems to have stopped being an option in any case. Fortunately, I’ve since found a much better (far less hackish) way to remote-sync files across different file systems. Reflecting my current set up, I’m talking about iOS (iPad and iPhone) and my Linux machine.

The new sync system is based on Git, very customizable, and conveniently extensible. Beyond text files, you can sync anything that Git can (which is almost everything — if you want to edit your `.gitignore`d files on the go I’m not sure I can help). If you’re already familiar with Git, getting set up will be a walk in the park. If Git is new to you, I think these tools help make the concepts of Git cloning, pulling, and pushing straightforward to understand.

### Components

* [Working Copy app](https://workingcopy.app) ($15.99 one-time pro-unlock and well worth it, iOS only)
* [iA Writer app](https://ia.net/writer) ($8.99 one-time purchase for iOS, also available on Mac, Windows, and Android)
* GitHub repositories ([private](https://github.blog/2019-01-07-new-year-new-github/) or public, both free)

I was inspired by [this article](https://www.macstories.net/ios/my-markdown-writing-and-collaboration-workflow-powered-by-working-copy-3-6-icloud-drive-and-github/) as well as [this one](http://blog.joncairns.com/2011/10/how-to-use-git-submodules/).

### Get set up

Here are the steps to setting up that I’ll walk you through in this article.

1. Create your remote repository
2. Clone repository to iPad with Working Copy
3. Open and edit files with iA Writer
4. Push changes back to remote
5. Pull changes from repository on your computer

This system is straightforward to set up whether you’re a command line whiz or just getting into Git. Let’s do it!

#### Create your remote repository

GitHub now offers free [private repositories](https://github.blog/2019-01-07-new-year-new-github/) for up to three collaborators. Choose “Private” on GitHub’s repository creation page:

![Image](https://cdn-media-1.freecodecamp.org/images/ItFaqv-hTrHTAZBHmsGEffVasUsDH-RqlyqU)

Create the repository. If you’d like to, you can follow GitHub’s instructions to push some files to it from your computer, or you can add files later from your iPad.

#### Clone repository to iPad with Working Copy

Download [Working Copy](https://workingcopy.app) from the App Store. It’s one of the more expensive apps I’ve purchased, but I think it’s well worth it. Developer [Anders Borum](https://twitter.com/palmin) has a steady track record of frequent updates and incorporating the latest features for iOS apps, like [drag and drop](https://workingcopy.app/manual/dragdrop) on iPad. I think he’s fairly priced his product in light of the work he puts into maintaining and enhancing it.

In Working Copy, find the gear icon in the top left corner and touch to open Settings.

![Image](https://cdn-media-1.freecodecamp.org/images/VuBXLHI2Tjs-mize4R-94tGwyJrdH4r43ajD)

Tap on SSH Keys, and you’ll see this screen:

![Image](https://cdn-media-1.freecodecamp.org/images/knqrfxBovulHFSbzBkwDamluhb4fBoacjSTT)

SSH keys, or Secure Shell keys, are access credentials used in the [SSH protocol](https://en.wikipedia.org/wiki/Secure_Shell). Your key is a password that your device will use to securely connect with your remote repository host — GitHub, in our example. Since anyone with your SSH keys can potentially pretend to be you and gain access to your files, it’s important not to share them accidentally, like in a screenshot on a blog post.

Tap on the second line that looks like “WorkingCopy@iPad-xxxxxxxx” to get this screen:

![Image](https://cdn-media-1.freecodecamp.org/images/qeX3GRpPhnr8oA3Em51b1nC6nd8t0897wyOy)

Working Copy supports easy connection to both BitBucket and GitHub. Tap “Connect With GitHub” or BitBucket to bring up some familiar sign-in screens that will authorize Working Copy to access your account(s).

Once connected, tap the “+” symbol in the top right of the side bar to add a new repository. Choose “Clone repository” to bring up this screen:

![Image](https://cdn-media-1.freecodecamp.org/images/sf4D5NkNmRpjHzdccE3Vlgnzmg-ykFU5ToAO)

Here, you can either manually input the remote URL, or simply choose from the list of repositories that Working Copy fetches from your connected account. When you make your choice, the app clones the repository to your iPad and it will show up in the sidebar. You’re connected!

#### Open and edit files with iA Writer

One of the (many) reasons I adore [iA Writer](https://ia.net/writer) is its ability to select your freshly cloned remote repository as a Library Location. To do this in the iA Writer app:

1. From the main Library list, in the top right of the sidebar, tap “Edit”
2. Tap “Add Location…”
3. A helpful popup appears. Tap OK.
4. From the Working Copy location, tap “Select” in the top right, then choose the repository folder.
5. Tap “Open”, then “Done”

Your remote repository now appears as a Location in the sidebar. Tap on it to work within this directory.

While inside this location, new files you create (by tapping the pencil-and-paper icon in the top right corner) will be saved to this folder locally. As you work, iA Writer automatically saves your progress. Next, we’ll look at pushing those files and changes back to your remote.

#### Push changes back to remote

Once you’ve made changes to your files, open Working Copy again. You should see a yellow dot on your changed repository.

![Image](https://cdn-media-1.freecodecamp.org/images/cbUDJ3vGR0tbBfJVggpkEhKhXHJxzOVwmTrc)

Tap on your repository name, then on “Repository Status and Configuration” at the top of the sidebar. Your changed files will be indicated by yellow dots or green “+” symbols. These mean that you’ve modified or added files, respectively.

Working Copy is a sweet iOS Git client, and you can tap on your files to see additional information including a comparison of changes (“diff”) as well as status and Git history. You can even edit files right within the app, with [syntax highlighting](https://workingcopyapp.com/manual/edit) for its many supported languages. For now, we’ll look at how to push your changed work to your remote repository.

![Image](https://cdn-media-1.freecodecamp.org/images/8Tpm89mGfCKzwYNQV6u6GOYqEyvcF2DrCDs-)

On the “Repository Status and Configuration” page, you’ll see right at the top that there are changes to be committed. If you’re new to Git, this is like “saving your changes” to your Git history, something typically done with the terminal command `[git commit](https://git-scm.com/docs/git-commit)`. You can think of this as saving the files that we’ll want to send to the GitHub repository. Tap “Commit changes.”

![Image](https://cdn-media-1.freecodecamp.org/images/HxVYK8VHBhl2bVQdnlt9sKmwYLBHKDwHDECl)

Enter your commit message, and select the files you want to add. Turn on the “Push” switch to send everything to your remote repository when you commit the files. Then tap “Commit.”

You’ll see a progress bar as your files are uploaded, and then a confirmation message on the status screen.

![Image](https://cdn-media-1.freecodecamp.org/images/CuKi9hmxEnUMgcSh3Qc2ZlcjlHCNXSLkd9cW)

Congratulations! Your changes are now present in your remote repository on GitHub. You’ve successfully synced your files remotely!

#### Pull changes from repository on your computer

To bring your updated files full circle to your computer, you pull them from the GitHub repository. I prefer to use the terminal for this as it’s quick and easy, but GitHub also offers a [graphical client](https://help.github.com/en/desktop/getting-started-with-github-desktop) if terminal commands seem a little alien for now.

If you started with the GitHub repository, you can clone it to a folder on your computer by following [these instructions](https://help.github.com/en/articles/cloning-a-repository).

#### Staying in sync

When you update your work on your computer, you’ll use Git to push your changes to the remote repository. To do this, you can use GitHub’s [graphical client](https://help.github.com/en/desktop/getting-started-with-github-desktop), or follow [these instructions](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line).

On your iOS device, Working Copy makes pulling and pushing as simple as a single tap. On the Repository Status and Configuration page, tap on the remote name under “Remotes”.

![Image](https://cdn-media-1.freecodecamp.org/images/u5dr0LkZTsYBvy2v4mk3me4RvEzdmtU9VUwA)

Then tap “Synchronize”. Working Copy will take care of the details of pushing your committed changes and/or pulling any new changes it finds from the remote repository.

### Not bad, right?

For a Git-based developer and work-anywhere-aholic like me, this set up couldn’t be more convenient. Working Copy really makes staying in sync with my remote repositories seamless, never mind the ability to work with any of my GitHub repos on the go.

For editing on the go, here’s a useful tip. Use `.gitignore` in your sync repository if you don’t need to move large files, like images, around with you. This will stop the ignored files from being pushed to GitHub and pulled to your iOS device - they’ll only remain on your computer’s larger hard drive. The `.gitignore` file of one of my sync repositories looks like this:

```
*.png
*.jpeg
*.jpg
*.mp4
*.gif
```

This means all the media files stay on my computer, and I can pull just the text file content to my iPad from GitHub to work on while I’m out and about.

I most recently used this set up to get some writing done while hanging out in the atrium of Washington DC’s National Portrait Gallery, which is pleasantly photogenic.

![Image](https://cdn-media-1.freecodecamp.org/images/Ee1wX2GpB5ipu8cYJdMcrdyi2y2yWZltgeKR)

I’d love to hear how this set up works for you and how you use it. In the meantime, happy working!

