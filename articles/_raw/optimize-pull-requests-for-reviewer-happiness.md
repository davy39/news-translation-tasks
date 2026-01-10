---
title: How to Optimize Your Pull Requests for Effective Code Reviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T22:24:06.000Z'
originalURL: https://freecodecamp.org/news/optimize-pull-requests-for-reviewer-happiness
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b42740569d1a4ca2abb.jpg
tags:
- name: best practices
  slug: best-practices
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: null
seo_desc: "By Chang Wang\nImagine reading a novel, but having the chapters sliced\
  \ up and reordered alphabetically by title. Or what if you were watching a movie,\
  \ but the scenes were reordered alphabetically by their first words of spoken dialog?\
  \ \nPuzzling a narr..."
---

By Chang Wang

Imagine reading a novel, but having the chapters sliced up and reordered alphabetically by title. Or what if you were watching a movie, but the scenes were reordered alphabetically by their first words of spoken dialog? 

Puzzling a narrative back together from these shuffled pieces might sound fun, but the novelty would wear off quickly if reviewing and understanding these stories were part of your day-to-day responsibilities.

## Shuffled narratives in code

The "Files changed" view for pull requests on Github lists changes alphabetically by file path. That's fine for the small feature branches that we strive for, but there are often complex changes with interdependent pieces that unavoidably result in large diffs across multiple files. Those changes can be overwhelming for reviewers to look at using the alphabetically-sorted files view. 

Instead, reviewers can view these changes in smaller more isolated chunks (i.e. commit-by-commit). Each commit's message can convey what the change is meant to achieve. And commits in sequence convey a sensible narrative for why these changes were necessary for this feature branch. All of this makes the reviewer's job much easier and more pleasant.

## Prepare a clear commit history

Thorough use of partial-staging, amending, and rebasing are all tools that will help achieve a clean commit history that your reviewers will appreciate. 

Avoid creating loosely focused commits. You might have forgotten to commit changes that made sense to be logically grouped together and continued on with editing the file. That's okay, happens all the time. Just because a file contains changes doesn't mean all those changes need to be committed. 

You also don't have to undo the changes that aren't related. You can use interactive staging to pick which chunks of a file should be staged for commit and which should be left for a future commit.

Aggressively rebase to avoid creating commits whose changes are later significantly modified or even deleted. 

It can be frustrating for a reviewer to spend time understanding what changed in one commit, then find that they'd essentially wasted their time on dead code a few commits later. Amend/fixup/squash those changes before you ask for a review!

If that sounds like a hassle, which is a reasonable reaction since git is hardly known for its UX, I highly recommend considering a Git GUI that can make much of that [painless](https://share.getcloudapp.com/OAubWjJJ).

## Request a review

After you have requested colleagues to review the pull request, **stop rebasing your commits!** Push changes requested by reviewers into new commits instead. 

"But doesn't this go against the goal of keeping a clean commit history?" 

Keeping a clean commit history was not the end goal, but rather a means towards making your changes easier for others to understand and review. Once a review has begun, modifying your commits actually makes your new changes _harder_ to review. 

Say you opened a pull request with these commits

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-263.png)
_(pseudo commits for demo purposes (ease-of-reference); don't actually number your commit messages)_

A reviewer then leaves a comment on something that was related to changes made in the first commit. If you modify that commit and force push, your old commits disappear from the pull request, and all commits since the ones that were rebased will appear as new commits following that review

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-266.png)
_All commits show up as new_

What's changed since the last time a reviewer looked at the pull request?  
Which commits have been modified and thus require attention, which haven't and can be skipped? 

The only way to tell is to look at all the commits that were force pushed, and try to recall whether what you see now is different from what was there before.

If you try to click on the file that was commented on to see if the comment had been addressed, or to get more context for code around the area of where the comment was made you'll be greeted with this charming telescope

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screen-Recording-2020-04-29-at-11.10-PM.gif)

Going back to the analogy of reading a novel – imagine making it halfway through, leave it alone for a day or two, and when you pick it back up you're told that important pieces in the parts you've read have changed, and the only way to know exactly what's changed is to read it all over again. Not fun.

Alternatively, this is what changes would look like if you push separate new commits instead:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-265.png)
_Can you tell what's new?_

You still should rebase from master, but as long as the commits that have already been reviewed haven't meaningfully changed, then your reviewers won't need to look over all of them again. Consider adding a comment after a force-push with a link to the most recently reviewed commit so reviewers can pick up where they left off.

## Changes approved!

By the time your PR has been approved, your branch probably now has a few commits that feel a bit messy. I recommend squash-merging and not worrying about it. The purpose for clarity has been achieved. Commit messages from squash-merged PRs will contain links back out to the pull requests where the squashed commits can once again be found. 

I'm not sure if squash merging is still controversial in 2020, in case it still is - React does it ??‍♂️

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-270.png)
_If Dan Abramov jumped off a bridge, would you? (Yes. The correct answer is "yes")_

However, perhaps you feel strongly that the commits in a PR are meaningful and significant enough to warrant being merged back into master as separate commits. If that's the case, then now is when you can go to town on rebasing until all the diffs are squashed into the perfect commits before merging without squashing.

## tldr:

* each commit in a PR should tell a story of what this commit changes, and ideally also what motivated the change
* rebase aggressively before opening the pull/merge request and requesting reviewers
* after review begins, _stop modifying your branch's commits and push new ones_
* after approval, squash merge (or selectively squash commits then merge)

## Keep in mind

Since the second part of this workflow is heavily informed by how Github handles rebased commits, there may come a day when those concerns are addressed by the platform and this workflow may no longer be required. Until then, please consider optimizing your commits for your reviewers :) 

### Related resources:

[Stacked Git](http://www.procode.org/stgit/doc/tutorial.html) is a tool for managing commit histories that I've found to be more intuitive than interactive rebasing via CLI. The tutorial may look daunting but that might be a design issue of having put everything (including Emacs usage instructions) on one page. It's actually quite easy to just learn and use a bit at a time.

Please let me know ([@CheapSteak](https://twitter.com/CheapSteak)) if you either have objections to this approach, or suggestions on how it could be improved.

