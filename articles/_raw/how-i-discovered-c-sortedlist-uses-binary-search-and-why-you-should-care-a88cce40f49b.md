---
title: How I Discovered that C# SortedList Uses Binary Search, and Why You Should
  Care
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-27T07:12:53.000Z'
originalURL: https://freecodecamp.org/news/how-i-discovered-c-sortedlist-uses-binary-search-and-why-you-should-care-a88cce40f49b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wnTXS4cPw-Tw_oC79VweTQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rina Artstain

  There is an age old debate: can programmers make do with just knowing how to code?
  Or do they need to understand some of their framework internals, basic data structures,
  and search/sort algorithms?

  I have encountered many bugs creat...'
---

By Rina Artstain

There is an age old debate: can programmers make do with just knowing how to code? Or do they need to understand some of their framework internals, basic data structures, and search/sort algorithms?

I have encountered many bugs created by being unaware of how hash tables are implemented. Or by a minor overlook which would have been a complete mystery to someone who didn’t know a binary search even existed. So you may guess that I’m of the opinion that you must have basic data structures/algorithms knowledge. I hope after reading this you will agree with me — but if not, you may leave your disagreements in the comment section below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wnTXS4cPw-Tw_oC79VweTQ.jpeg)

### System Overview

Imagine a system of customer service reps, where each user writes notes for tracking actions and conversations with clients. If the note requires future action, the user can add a due date for a specific date and time, and it becomes a “task.” At any point, the user can mark the task as “done” and the task will be removed while remaining in the list of notes.

For easy access, all the notes are displayed in a descending order by insert date (oldest note first). Tasks are displayed in ascending order by due date (upcoming/overdue tasks first).

As usual, some of the complexity of the original system is omitted for simplicity (persistency, multi threading etc.). I’ve also included a link to GitHub with a working version of the code included in this post. You can run it for yourself. (It’s at the bottom of the post, so even if you don’t read it you’ll have to scroll all the way down ha!).

### Implementation

Let’s start with the Note class definition:

It’s a simple data object.

Next, we’ll create a NotesManager class which holds all the notes/tasks and manages access to them:

The NotesManager class uses a SortedList to keep the Notes/Tasks in the correct order determined by the type of the list and SortDirection given to the NoteComparer. Notes are ordered by InsertDate, ascending and tasks are ordered by DueDate, descending. The NotesManager class takes care of creating the NoteIndex with the right date. It inserts the note in the appropriate list.

The last functionality we need is to mark a task as “done,” which then removes the task from the Tasks list.

What was I thinking when I wrote this code? I honestly don’t remember. Probably not thinking much of anything. This is the underlying issue for many mistakes.

Take a second before reading on and try to figure out where the problem is.

### What’s Going On?

Imagine my surprise when I started testing the NotesManager. I found that when I marked some Tasks as “done”, they were not removed from the Tasks list. It appeared to be totally random, sometimes working and sometimes not.

There I was, staring at the debugger in disbelief. The Task is sitting **right there** in the tasks list, but “remove” wasn’t removing it. I had no idea what was going on.

I assumed something was wrong with the NoteComparer implementation. I added a breakpoint in the Compare method. There I found something strange: The tasks weren’t being scanned sequentially. The debugger seemed to be randomly accessing items in the task list.

Hmmmm. Weird. For a second I thought there might be some multithreading weirdness going on, but this was a local development environment — there was nobody else who could be accessing my web server (and if there was, how likely was it that they are testing the same user and data I was currently using?). Nope, the answer had to be somewhere else.

After a couple more tests, a pattern emerged. The first access to Compare was somewhere in the middle of the list. Then it jumped to another location. Then another jump and another, before finally giving up on the whole thing. Then came the #facepalm moment, and I realized that SortedList must use binary search for finding items in the list! It should have been obvious (anything else would be silly, really).

I tried to verify my idea by searching [MSDN Documentation](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.sortedlist-2?view=netframework-4.7.2), and there it was — [Remove](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.sortedlist-2.remove?view=netframework-4.7.2#System_Collections_Generic_SortedList_2_Remove__0_) uses binary search. OK then, my guess was right — but why wasn’t the binary search **working**?

This time I moved the breakpoint a little further down in the Comparer implementation. I immediately saw where the problem was. I was passing the NoteIndex with only the Id, assuming that would be enough for equality.

If this was a regular List, that would have worked. But cutting that corner in combination with binary search (instead of a sequential scan which I was implicitly assuming) resulted in the SortedList being unable to find the Note it was looking for. So I changed the implementation of “MarkDone”.

And it worked!

(There’s a bug in this implementation as well, but I wanted to focus on the issue at hand. Can you find the problem?)

You can download a working example which shows the bug, and its solution [here](https://github.com/rinaarts/NoteSystem).

### Key Takeaways

Here are my key takeaways from this case:

1. If you’re using a new service or data structure, take 5 minutes to read the documentation. If I had done that and realized that the key on the SortedList was used for uniqueness and not only sorting, I probably wouldn’t have made the mistake that I did.
2. Having a good grasp of basic data structures and algorithms is essential for day-to-day work. This type of bug is extremely hard to find and solve. It happens sporadically with no apparent logic. It’s best to avoid that type of bug altogether, but if you can’t avoid it — at least be able to analyze it after it happens.

### Bonus Question

Why did I override GetHashCode() on the Note class? Why should you **always** override GetHashCode() if you’ve overridden Equals()?

Hint: which data structure uses hash codes?

Like what you read? Share the love by clapping. Have a question or comment? Let me know in the comments section.

