---
title: How Git best practices saved me hours of rework
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T19:37:15.000Z'
originalURL: https://freecodecamp.org/news/how-git-best-practices-saved-me-hours-of-rework-cf227bad9a50
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fbmqZte8Tx-KfrZlkw4q4g.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Hemal Patel

  Recently I was working on the task to upgrade a certificate for a NodeJS application.
  This was last touched two years ago for a feature enhancement. Any live issue raised
  to this app would require immediate attention, although the app ...'
---

By Hemal Patel

Recently I was working on the task to upgrade a certificate for a NodeJS application. This was last touched two years ago for a feature enhancement. Any **live** issue raised to this app would require immediate attention, although the app has only been used internally.

The app is old. Core-NodeJS-Infra modules have not been updated for more than two years. Downstream services are deprecated. The way we call downstream services is changed. The tight deadline is a cherry on the cake. I knew it was gonna be a roller-coaster ride.

I spent three days getting the app running.

Infra-modules are updated? Check.

Downstream services are working fine? Check.

UI flows are working fine? Check.

One of our team members had touched the app for an upgrade over a year ago. He pointed out that the repo from where I forked was itself a forked repo. Some other team had worked on that repo, and then our team worked on the original repo from that point onwards — but my team member doesn’t know from what point onwards. So it was a bit of a mess!

We have an “Ownership” tool which shows the correct repo and it “lied” to me. So the situation was like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vWPKaIKu8tCtgYQyo-Ejsw.jpeg)
_Forkception_

Yes, it was Forkception! WTF and FML were the first two thoughts that came out of my mouth. I **should** have worked on the live repo but, **instead**, I worked on a fork which was stale. How stupid of me!

First thought — my three days of work have been wasted, and I need to start fresh.

Second thought? Let me ask my old friend Git?. He has been helping me for a very long time.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fbmqZte8Tx-KfrZlkw4q4g.png)

**Me** — “Hey Git? I’m in a deep trouble and I need your help resolving this issue.”

**Git** — “Hey! Ok, so we have to start from whatever is in live first. Create a new branch-called **upgrade**, and point that branch to the live code. You can use a [git hard reset](https://git-scm.com/docs/git-reset#git-reset---hard) for that.”

**Me** — “Ok, I will.”

At this point, the situation looks like this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GRnnYUHYrJU3CF5V-miFUg.jpeg)
_Using Git features_

**Git** — “We need to know what changed between develop and upgrade. Can you list out the files that differ between your **upgrade** and **develop**? Check those files individually, and figure out what kind of changes there were.”

**Me** — “Cool. I see three kinds of changes. There is a service S1 which I need to call in a different way. There is a service S2 which I need to call using a different endpoint. There is a service S3 which I need to call using different parameters. I also see the **package.json** file in the **upgrade** branch has some of the packages already upgraded. So only a few packages need to be changed.”

**Git** — “Awesome that you segregated the changes. Now show me the Git log of your **develop** branch. Hope you have followed some basic Git practices, for example always having buildable code in each commit. The commit message should depict what you have changed.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*hH5gt56WcMwTKl_iF50Uuw.png)
_Git log on develop branch_

**Me** — “Yes, I have a total of four commits in the **develop** branch. One commit was for making the project buildable. There is one for each of the three service calls. ”

**Git** — “Perfect! It seems like you have followed best practices properly. Let’s start by stabilizing the project build by making package.json up-to-date. Checkout to the **upgrade** branch and make a duplicate of package.json — package-copy.json. Now, using Git [replace](https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/) , upgrade/package.json with develop/package.json, and run the diff between package.json and package-copy.json. Since, the live code has some of the packages changed already, and has different versions, you will need to upgrade by looking at the diff.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*rFVh4Jf6JCpLgBDj9Qj_6g.jpeg)
_**Making the project buildable**_

**Me** — “Let me try that. Ok, it is building and running.”

**Git** — “Awesome! Now, let’s work on the service calls. I see that you have one commit for each service-call change in the develop branch. Time to [cherry pick](https://git-scm.com/docs/git-cherry-pick). Pick from least complicated service call to the most complicated service call. Pick, merge, and resolve conflicts. Make sure to check if the project is in buildable condition **after** each cherry-pick and **before** each commit.”

**Me** — “S1 done. S2 done. S3 done. Thanks, Git”

**Git** — “You’re welcome. But it is you who have helped yourself, by following Git commit practices, and not treating Git as a mere code-storage.”

### **What did I do here? ?**

#### Commit Related Changes

Take a pause for a moment and think if this change should go in this commit. A commit which says that “change: service-s1 endpoints” and has service-s2 changes would just create confusion.

#### Don’t Commit Half-Done Work

We have often heard the “commit early, commit often” mantra. In the above example, you can have one commit for different endpoints of the same service. This is called [**Sausage Making**](https://sethrobertson.github.io/GitBestPractices/#sausage).

However, I personally squash my small commits using **git rebase interactive mode**. This helps me to have one logical change, which can be certified, and it helps a Trusted Committer to review your code as well. This is much preferable for large-scale projects.

#### Test Your Code Before You Commit

We should think of Git as a state machine, and any machine should be in buildable condition at any state.

#### Write Good Commit Messages

This is a most crucial part. I always pause for a moment and think whether I will be able to understand — after three months — the kind of change in this commit by just looking at the commit message.

### Conclusion

I was able to quickly resolve the mess. I could come out of that WTF and FML moment just because I followed some good practices. They exist for a reason and are like salt in food — you only realize their value when they are not used.

Mistakes will happen sooner or later, unconsciously. But make sure you consciously follow some practices around Git.

I’m a fan of [Git semantic commit messages](https://gist.github.com/mutewinter/9648651#file-commit_format_examples-txt), which help to navigate through the Git history. Because, let’s be honest, you can’t expect everyone to use the same words for each commit message. However, **message-type** can be expected.

This helps make sure that, after each commit, your project can be built — which is really helpful.

VSCode has sick support for Git. It becomes super easy to see the conflicts and resolve them, sometimes with just a single click. See the below example ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BtLN8xTuTbJgXkJMPD7GgA.jpeg)

### References

* [Git Best Practices](https://sethrobertson.github.io/GitBestPractices/)
* [Super Awesome Version Control Integration in VSCode](https://code.visualstudio.com/Docs/editor/versioncontrol)
* [Git Semantic Commit Messages](https://seesparkbox.com/foundry/semantic_commit_messages)
* Git Tip ?: H[ow to “merge” specific files from another branch](https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/)
* Git Tip ?: G[it — git-cherry-pick Documentation](https://git-scm.com/docs/git-cherry-pick)
* Git Tip ?: G[it — git-reset Documentation](https://git-scm.com/docs/git-reset#git-reset---hard)

Special thanks to my friends [**Saurabh Rajani**](https://www.linkedin.com/in/saurabh-rajani-72268590/?originalSubdomain=in) and [**Anish Dhargalkar**](https://www.linkedin.com/in/anishdhargalkar/) who helped me with content refinement.

