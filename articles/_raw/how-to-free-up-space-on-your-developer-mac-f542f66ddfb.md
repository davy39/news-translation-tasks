---
title: How to free up space on your developer Mac
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T16:36:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-free-up-space-on-your-developer-mac-f542f66ddfb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iNNdLGh5TORjiWIHp5l0Ng.png
tags:
- name: Git
  slug: git
- name: JavaScript
  slug: javascript
- name: mac
  slug: mac
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: "By Gant Laborde\nClean up your dev environment you filthy animal!\nI love\
  \ cleaning software? PLZ! Remove duplicates, find old OS cruft etc. But it never\
  \ cleans a development machine as I can. \nSure, for general maintenance, nothing\
  \ beats CleanMyMac. Bu..."
---

By Gant Laborde

#### Clean up your dev environment you filthy animal!

I love cleaning software? PLZ! Remove duplicates, find old OS cruft etc. But it never cleans a development machine as I can. 

Sure, for general maintenance, nothing beats [CleanMyMac](https://macpaw.com/cleanmymac). But once a year, developers should run through a few manual commands, because auto-cleaners won’t know how to take care of a developer machine.

Before we start, let’s look at how much “Free Space” you’re starting with:

![Image](https://cdn-media-1.freecodecamp.org/images/y4j1aRSyr4UvT8Ns14UgTww17s6D7Ndr7wu1)

Mine is reporting 132.2 GB before cleaning. Time to get started!

### Mac Homebrew Users

This one usually shaves off hundreds of megs of data. Update, upgrade, and then clean up those files you’re not going to use.

**Update then remove old formulae and their folders:**

```
brew update && brew upgrade && brew cleanup
```

You might have used `brew prune` in the past, but that has been deprecated. Cleanup handles this for you!

#### General Brew Maintenance

Brew is a complicated system, and no one knows it better than the maintainers. So you can run `brew doctor` and get some additional chores you could take care of to have it run properly.

### Git Users

Git is great, but it’s not hard to leave a bunch of merged branches laying around on your local machine! Those branches aren’t useful anymore, and sometimes make naming conflicts for future branches.

**You can remove all the merged branches from a single project with this command:**

```
git branch --merged master | grep -v "\* master" | xargs -n 1 git branch -d
```

WOW, what a mouthful for only one project! Let’s make it worse. ?

**This code will CD into all folders in the current working directory, and then run the command to clean merged branches for each!**

```
for d in */; do cd $d; echo WORKING ON $d; git branch --merged master | grep -v "\* master" | xargs -n 1 git branch -d; cd ..; done
```

### JavaScript Developers

#### Delete OLD `node_modules` embedded in projects

The following command finds all `node_modules` folders older than 120 days and removes them. This does mean you will have to `npm i` or `yarn` again in those older projects. _This is usually a huge cleanup!_

**Removes all `node_modules` folders older than 4 months:**

```
find . -name "node_modules" -type d -mtime +120 | xargs rm -rf
```

If you’re feeling quite aggressive, you can just clear out ALL `node_modules` folders and re-install as needed, by removing the `mtime` flag.

**Removes all `node_modules` folders:**

```
find . -name "node_modules" -type d | xargs rm -rf
```

#### Remove old versions of Node

Remove old versions of Node. This varies depending on your Node manager. I use ’n’ so it’s easy for me. Consult uninstall for your specific version manager.

> **Using `n`?**

> List all versions of node + your installed ones with `n ls` and then remove any with `n rm <versi`on>.

> **Using `nvm`?**

> List your installed versions with `nvm ls` and then remove any with `nvm uninstall <versi`on>.

> **Using `asdf`?**

> List your installed versions with `asdf list nodejs` and then remove any with `asdf uninstall nodejs <versi`on>.

### Ruby Developers

Clean up old versions of Gems with the `cleanup` command. If you’re worried, you can see the results first with “dryrun”.

```
gem cleanup --dryrun
```

Then when you are confident, you can remove the “dryrun” param and run it for real.

```
gem cleanup
```

#### Remove old versions of Ruby

This depends specifically on your Ruby version manager. We’ll do two popular versions to help you out.

> **Using `rbenv`?**

> List your installed versions with `rbenv versions` and then remove any with `rbenv uninstall <versi`on>.

> **Using `rvm`?**

> List your installed versions with `rvm list` and then remove any with `rvm uninstall <versi`on>.

### Xcode Developers

Xcode loves to cache things all over your machine, and some of these are hundreds of megs. Time to clean them up, and if you need to rebuild them again, no worries!

**Clean up CocoaPod caches:**

```
rm -rf "${HOME}/Library/Caches/CocoaPods"
```

**Delete old Xcode Simulators:**

```
xcrun simctl delete unavailable
```

**Clean up various archives, logs, and derived data folders:**

```
rm -rf ~/Library/Developer/Xcode/Archives
rm -rf ~/Library/Developer/Xcode/DerivedData
rm -rf ~~/Library/Developer/Xcode/iOS Device Logs/
```

Check out your connected device info in `~/Library/Developer/Xcode/iOS Device Logs/` and delete anything for old iOS devices you’ve connected.

### Docker

You can remove all volumes not used by at least one container. Because… why would you want those?!

This might be huge or it might remove nothing. Worth a run right!?

**Remove unused local volumes**

```
docker volume prune
```

### RESULTS?!

Don’t forget to empty your trash and check on how we did!

![Image](https://cdn-media-1.freecodecamp.org/images/eVUvMYYTdZvKkHcbItSd-cR3ZSEmWoydQHz8)

> 30 GIGS! pulled off my machine! How about you?

Your success is probably vastly different, but I’d love to know. Comment or [tweet at me](https://twitter.com/GantLaborde?lang=en) your results, and any other developer spots you recommend we clean! I’ll be happy to add your advice to the article.

---

[Gant Laborde](https://www.freecodecamp.org/news/how-to-free-up-space-on-your-developer-mac-f542f66ddfb/undefined) is Chief Technology Strategist at [Infinite Red](http://infinite.red), published author, adjunct professor, worldwide public speaker, and a mad scientist in training. Clap/follow/[tweet](https://twitter.com/GantLaborde) or visit him [at a conference](http://gantlaborde.com/).

[**5 Things that Suck about Remote Work**](https://shift.infinite.red/5-things-that-suck-about-remote-work-506b98dd38f9)  
[_The Pitfalls of Remote Work + Proposed Solutions_shift.infinite.red](https://shift.infinite.red/5-things-that-suck-about-remote-work-506b98dd38f9)[**React Native vs. Native**](https://shift.infinite.red/react-native-vs-native-ccac6f05346a)  
[_Should I learn React Native or Native?_shift.infinite.red](https://shift.infinite.red/react-native-vs-native-ccac6f05346a)

