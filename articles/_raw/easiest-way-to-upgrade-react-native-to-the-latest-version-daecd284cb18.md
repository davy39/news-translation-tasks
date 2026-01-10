---
title: The easiest way to upgrade React Native to the latest version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T10:15:15.000Z'
originalURL: https://freecodecamp.org/news/easiest-way-to-upgrade-react-native-to-the-latest-version-daecd284cb18
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ytrkryPcES23LiO1srdSvg.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sam Johnson

  I’ve read many horror stories from people who have spent days trying to upgrade
  React-Native to the latest version. The official guideline as mentioned here do
  not work in most cases.

  Below is the way I found out after so many trials a...'
---

By Sam Johnson

I’ve read many horror stories from people who have spent days trying to upgrade React-Native to the latest version. The official guideline as mentioned [here](https://facebook.github.io/react-native/docs/upgrading) do not work in most cases.

Below is the way I found out after so many trials and errors to be the easiest.

There is a wonderful tool named [**_rn-diff-purge_**](https://github.com/pvinis/rn-diff-purge) (please don’t be fooled by the name, it won’t do any kinds of purge ?). What this tool does is compare different versions of react-native and shows you the differences from the source code level. By seeing the differences, you can make changes accordingly to the build. It depends on the number of libraries you are using, but the initial build could succeed at once or show some errors. Then you can work on those errors one by one.

![Image](https://cdn-media-1.freecodecamp.org/images/1X3qYpeOtjUhf3F4Tt0lHZRtEZcF-RaTqfFm)

I have used the tool to upgrade react-native three times so far, and it has taken me from 30 minutes to 1 hour to finish the upgrade.

Below are the steps I take every time I decide to do an upgrade:

* Make sure your codebase is in solid condition, which means you have ironed out all the known issues.
* Make sure you have committed all your changes:

```
git add . git commit -m “Last commit before upgrade to RN version 0.59.0” git push
```

* Copy & paste this to your browser: [https://github.com/pvinis/rn-diff-purge/compare/version/0.58.6..version/0.59.0](https://github.com/pvinis/rn-diff-purge/compare/version/0.58.6..version/0.59.0)
* Manually make changes according to the differences being shown.
* Run npm i to update versions
* Build & Deploy through Android Studio and Xcode

If no errors are shown, start your unit testing.

If some errors are shown, the errors are more likely due to the libraries you are using. If this is the case, go to the github repo for the library that gives error.

For example, when I upgraded React-Native from 0.58.6 to 0.59.0, a library I used (“lottie-react-native”) gave me some compiling errors under Android Studio. So I went to their github site and found [this issue](https://github.com/react-native-community/lottie-react-native/issues/453). Then I followed the instructions mentioned there to solve the issue.

You will certainly encounter many¹ issues, but most issues ( if not all ) I have encountered so far are caused by the libraries I used, not by React-Native itself.

When you are satisfied with all the changes, run `git diff` to see the changes, then `git add .` `git commit -m "Complete React Native Upgrade"` `git push` .

Congratulations! You are ready to use the latest features provided by the latest React-Native versions.

Note: some issues do not have immediate solutions (which might require a new version of the libraries themselves). But the good news is that all the issues will have some kind of workaround. ?

