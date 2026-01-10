---
title: How to Use Lazygit to Improve Your Git Workflow
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2025-04-10T13:49:46.631Z'
originalURL: https://freecodecamp.org/news/how-to-use-lazygit-to-improve-your-git-workflow
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744293114488/5332db88-bff6-4aef-91eb-3423f3b95e1a.png
tags:
- name: Lazygit-tutorial
  slug: lazygit-tutorial
- name: Lazygit
  slug: lazygit
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Lazygit is an open-source command line terminal UI for Git commands that
  I’ve used for the last couple of years, and it’s become my new best friend.

  Basically, the Lazygit tool is a wrapper for the Git command line that replaces
  it with a UI. Instead...'
---

[Lazygit](https://github.com/jesseduffield/lazygit) is an open-source command line terminal UI for Git commands that I’ve used for the last couple of years, and it’s become my new best friend.

Basically, the Lazygit tool is a wrapper for the Git command line that replaces it with a UI. Instead of typing out Git commands again and again in your terminal, you can use keyboard shortcuts to commit, push, pull, create, edit, and delete branches in your project.

In simple terms, Lazygit helps you increase your productivity while working with Git.

In this article, we'll walk through the essential features of Lazygit, and I’ll show you how it works.

## Table of Contents:

1. [How to Install Lazygit](#heading-how-to-install-lazygit)
    
2. [How to Use Lazygit](#how-to-use-lazygit)
    
3. [Shortcuts and Key Mappings in Lazygit](#heading-shortcuts-and-key-mappings-in-lazygit)
    
4. [Other Keybindings in Lazygit](#other-keybindings-in-lazygit)
    
5. [Conclusion](#conclusion)
    

## How to Install Lazygit

Before we start, you’ll need to make sure it’s installed on your machine. You can install the tool in your system using the following methods (depending on your system):

### Homebrew

You can [install lazygit](https://formulae.brew.sh/formula/lazygit#default) in macOS using Homebrew like this:

```bash
brew install lazygit
```

### Scoop (Windows)

You can [install lazygit](https://scoop.sh/#/apps?q=lazygit) in Windows using Scoop like this:

```bash
# Add the extras bucket
scoop bucket add extras

# Install lazygit
scoop install lazygit
```

### Arch Linux

You can [install lazygit](https://aur.archlinux.org/packages/lazygit-git) in Arch using Pacman like this:

```bash
sudo pacman -S lazygit
```

### Ubuntu and Debian

You can install lazygit in Ubuntu and Debian using the following command:

```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

Verify the correct installation of lazygit:

```bash
lazygit --version
```

The command output looks like this:

```bash
➜  lazygit --version
commit=, build date=, build source=nix, version=0.44.1, os=linux, arch=amd64, git version=2.47.0
```

### Fedora and RHEL

You can install lazygit in Fedora and RHEL using DNF like this:

```bash
sudo dnf copr enable atim/lazygit -y
sudo dnf install lazygit
```

### NixOS

You can [install lazygit](https://search.nixos.org/packages?channel=24.11&from=0&size=50&sort=relevance&type=packages&query=lazygit) in NixOS using the following method:

```bash
# with nix-shell
nix-shell -p lazygit

# with nix-env
nix-env -iA lazygit

# with /etc/nixos/configuration.nix
environment.systemPackages = [
  pkgs.lazygit
];
# or with enable lazygit flakes
nix run nixpkgs#lazygit
```

## How to Use Lazygit

To use Lazygit, you don’t need any advanced knowledge about Lazygit or the Git CLI. If you are a beginner, that’s okay – I’ll walk you through the process and the basics here.

The main thing to understand is how the key mappings (shortcut keys) work. In this tutorial, I won’t discuss every key mapping, but I’ll teach you about some of the most common Lazygit key mappings which you’ll use on a daily basis. They’ll help you build a solid base for using the tool effectively.

To use Lazygit, first open the terminal you use. For example, I’m using the GNOME distro, so I’ll use the [Ptyxis terminal](https://gitlab.gnome.org/chergert/ptyxis).

Type the `lazygit` command in your terminal:

```bash
lazygit
```

The command output should look like this in your terminal:

![Lazygit cli demo](https://cdn.hashnode.com/res/hashnode/image/upload/v1743685042853/ab3f10f0-0d13-44d3-a86a-a58676cf30a5.gif align="center")

The Lazygit UI is divided into six panels, or sections. Each panel serves a specific use case. Let’s explore these panels in more detail. You can see them highlighted in the image below:

![Explore the Lazygit panels](https://cdn.hashnode.com/res/hashnode/image/upload/v1743687006438/5ca2451e-d4a0-42a7-89b2-0b94fd4ca162.png align="center")

### Panels or Sections in Lazygit

As I mentioned above, there are six main panels in Lazygit. They are:

1. Status
    
2. Files
    
3. Branches
    
4. Commits
    
5. Stash
    
6. Previews
    

The most important panels in Lazygit are files, branches, and commits, but we’ll examine each of the six now.

#### Status panel

The status panel provides an overview of your current repository and the current checked-out branch, including local and remote changes.

![Status panel in Lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743759630157/a7ef738b-5353-4941-9eb5-073d3235aaba.png align="center")

Also, when you click on the status panel text, it opens a new tab or panel where it shows the recently opened repository list.

![Recently opened repos](https://cdn.hashnode.com/res/hashnode/image/upload/v1743760171736/8edb2f41-86ad-4e64-95f2-b1310d8c6f57.png align="center")

#### Files panel

The Files panel shows lists of the files in your repository that have been modified or changed. You can see files that you’ve deleted or discarded and unstaged.

![Files panel in Lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743760570130/c891940b-4ba2-4fcb-a867-817b74e53618.png align="center")

#### Branches panel

The Branches panel shows lists of local and remote branches which are available in this repository.

![Branches panel in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743761276628/b34dc945-11c8-482d-8c4d-51783c68bf55.png align="center")

#### Commits panel

The Commits panel shows a list of commits in the current branch, which allows you to view, checkout, or interact with (view/undo/and so on) specific commits.

![commits panel in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743761671236/80a7321a-8d16-4add-bc4a-db52d2987836.png align="center")

#### Stashes panel

The Stashes panel helps you manage your stashed changes, allowing you to apply, drop, or view them. Git stash is a location for storing uncommitted changes (modified, staged, or untracked files) in a hidden place, letting you switch branches without committing or discarding them.

![Stashes panel in laygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743764679570/d7233d92-cfb0-4757-a338-bcc3d9fec2b8.png align="center")

#### Preview panel

The preview panel lets you preview unstaged changes, commits, logs, file content, and so on in Lazygit.

![Preview panel in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743765844602/7c492361-bbcf-4d2c-8588-b0c3e8704132.png align="center")

To switch between panels, use the left and right arrow keys or the specific keybindings displayed at the top of each panel.

Press `1` to open the Status panel, `2` for Files, `3` for Branches, `4` for Commits, and `5` for the Stash panel.

![Navigation between panels in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743766590099/91689f4d-eba3-47cf-80a6-e18307c326cd.gif align="center")

## **Shortcuts and Key Mappings in Lazygit**

Lazygit is especially popular because of its shortcuts. You don’t need to write the same Git commands in the terminal over and over. Rather, you just need to use a shortcut.

For example, usually when you commit a file, you’ll first add the file using `git add` and then commit the file using `git commit`.

But in Lazygit, you just have to select the file using your mouse or the up and down keys and press space to commit the file.

In Lazygit, everything works around the shortcut commands, and you use shortcuts to perform common Git operations. Here are a few essential commands we’ll go over in this tutorial:

* `a` – Stage or unstage all the files available in the Files panel.
    
* `space` (file panel) – Stage or unstage a single file in the Files panel.
    
* `c` – Commit staged changes by opening a commit message editor.
    
* `p` – Push commits to the remote repository.
    
* `P` – Pull changes from the remote repository.
    
* `z` – Undo the commit.
    
* `s` – Stash changes, allowing you to switch branches or perform other operations.
    
* `S` – View and apply stashed changes.
    
* `n` – Create a new branch.
    
* `d` – Delete your branch.
    
* `y` – Copy to clipboard.
    
* `M` – Merge branch.
    
* `space` (branches panel) – Check out the selected target branch.
    
* `e` – Edit or open the file in an external editor.
    
* `q` – Quit Lazygit and return to the terminal.
    
* `d` – Discard any changes in the file.
    
* `?` – Open the keybinding menu.
    

Now let’s go over these shortcuts so you can understand how they work and see them in action.

### How to Commit a File

To commit a file in Lazygit, first select the file you need by pressing the `space` key or the `a` key or double-clicking on the file. Then press `c`, and a new panel should open. There, you can add a message and hit enter to commit the file.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743770682782/cbd83578-a286-482f-aeaa-31a9715a5483.gif align="center")

### How to Pull and Push Code

To pull remote code from the Git server (Github, GitLab, Gitea, and so on), you can press `p` (lower case p):

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743774642242/decec44c-7622-432a-9da5-81b14b60ef8a.gif align="center")

To push local code into a Git server, you can press `P` (upper case P):

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743842516002/37647a76-afe5-4d4b-acfc-fc85f1010749.gif align="center")

### How to Create and Delete a Branch

To create a new branch in Lazygit, press `n`. A new panel will open where you’ll add the name of the branch and hit Enter.

![Create a new branch in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743843881624/6c4db14e-0102-4333-be56-5d3796ab1c50.gif align="center")

To delete a branch, press `d` and then specify whether you want to delete the branch in a local or remote repository. In the following example, I’m deleting a local branch.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743847541934/34e378b6-03ac-4e6d-93d0-35aaeda39e57.gif align="center")

> Note: To delete and create a new branch in Lazygit, first select the branch panel and then press the corresponding shortcut key for deleting a branch. Press the d key to delete, and then to create a branch press the n key. Otherwise, it won’t work.

### How to Undo a Commit

To undo the last commit in Lazygit, just press `z`. A new panel will open, showing the details of the commit you are undoing. Then, hit Enter.

![Undo commit in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743852917448/a3f2cab7-2806-48e4-a749-90f821b537dc.gif align="center")

### How to Merge a Branch

To merge a branch, press `M` (capital M). To open the merge options, choose the merge type, then hit Enter.

#### Merge type:

* **Merge:** A standard merge, preserving the branch history.
    
* **Squash merge:** Combines all commits from the branch into a single commit on the target branch.
    
* **Squash merge and leave uncommitted**: Same as squash merge, but leaves the changes uncommitted.
    

![Merge branch in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743921595283/e46e0c89-b69a-4462-acd3-295045c99dfd.gif align="center")

### How to Resolve Merge Conflicts

To resolve merge conflicts in Lazygit, first merge a branch by pressing `M`, then choose the merge type (which I describe in the subsection on how to merge a branch) and hit Enter.

If any merge conflicts occur, the conflicting file(s) appear in the files panel. Press Enter to view the merge conflicts in the preview panel and navigate between conflicts using the up and down keys. Select the correct merge conflicts, press the space key, and your merge issue will be resolved.

![resolve merge conflicts in lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743921640247/e5b7f971-f027-47df-be4c-a90b356e24f8.gif align="center")

### How to Discard Changes

To discard or drop any changes in a file or commit, press `d`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743774406564/bc5b91fb-2d33-41d0-95b9-667478c4c8db.gif align="center")

### How to Copy

To copy a file name, path, commit hash, message, URL, author, or any other details, first select the commit or file, then press `y` to copy the information.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743856793802/e23d9e5c-b0b4-40a0-8124-f94669b377c0.gif align="center")

## Other Keybindings in Lazygit

There are other keybindings in Lazygit which I did not discuss in this article. To learn about every keybinding, you can check out the keybindings menu. Open the keybindings menu and press the `?`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743843262905/a4aba097-999b-4ff8-bd00-661181d96aad.gif align="center")

When you open the keybindings help menu, it changes according to the panel you’re in.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743915037200/9339b7b1-b2a4-45e5-8a51-5be0a9f2a319.gif align="center")

## Conclusion

Lazygit helps you become more productive when working with Git or Git commands. As a beginner, starting with Lazygit can be somewhat challenging because of its key mappings, but once you get the hang of them, they’re pretty easy to remember and use.

If you are a first-time Lazygit user, my suggestion is to avoid using Lazygit on a working repository. Instead, create a demo repository and try it out/practice.

To learn more about [LazyGit keybindings or shortcuts](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md), you can refer to the Lazygit documentation. You can also check out the following YouTube tutorials for beginners:

* [LazyGIt - A Faster, Easier Way to Use Git on Terminal & NeoVim](https://www.youtube.com/watch?v=A6F_8ajlrYQ)
    
* [Lazygit - The Best Way To Use Git On The Terminal & Neovim](https://www.youtube.com/watch?v=Ihg37znaiBo)
    
* [My new favorite way to use Git](https://www.youtube.com/watch?v=06lEP59XAgM)
    
* [LazyGit: Effortless Git in Your Terminal!](https://www.youtube.com/watch?v=dSWJKcEiAaM)
