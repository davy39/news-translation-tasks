---
title: What I Learned from Maintaining a Repo During Hacktoberfest and Merging 356
  PRs
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-11-02T16:17:06.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-as-a-hacktoberfest-repo-maintainer
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-5.56.25-PM.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: hacktoberfest
  slug: hacktoberfest
- name: lessons learned
  slug: lessons-learned
- name: open source
  slug: open-source
seo_title: null
seo_desc: 'Hacktoberfest is a month long celebration of open source. And this year
  I participated as a maintainer for freeCodeCamp''s Developer Quiz Site.

  I merged a total of 356 pull requests and helped a lot of new contributors get started
  with open source. We...'
---

Hacktoberfest is a month long celebration of open source. And this year I participated as a maintainer for [freeCodeCamp's Developer Quiz Site](https://github.com/freeCodeCamp/Developer_Quiz_Site).

I merged a total of 356 pull requests and helped a lot of new contributors get started with open source. We were able to add a total of 477 new quiz questions to the [Developer Quiz Site](https://developerquiz.org/). 

Here are some more statistics: 

### Stats on Oct 1, 2022

Number of questions: 694

Forks: 61

Stars:42

### Stats on November 1, 2022

Number of questions: 1171

Forks: 246

Stars: 109

This month long journey has been crazy, productive, fun and educational. Here are all of the things that I learned during Hacktoberfest 2022.

## Table of Contents

- [How it all began](#heading-how-it-all-began)
- [Preparing for Hacktoberfest](#heading-preparing-for-hacktoberfest)
  - [Step 1: Adding the Hacktoberfest topic and labels](#heading-step-1-adding-the-hacktoberfest-topic-and-labels)
  - [Step 2: Creating issue templates](#heading-step-2-creating-issue-templates)
  - [Step 3: Updating the contributing documentation](#heading-step-3-updating-the-contributing-documentation)
  - [Step 4: Creating well-defined issues](#heading-step-4-creating-well-defined-issues)
  - [Step 5: Adding Saved replies](#heading-step-5-adding-saved-replies)
  - [Step 6: Opening up GitHub Discussions](#heading-step-6-opening-up-github-discussions)
- [Lessons I learned during Hacktoberfest](#heading-lessons-i-learned-during-hacktoberfest)
  - [Lead with patience, empathy and kindness](#heading-lead-with-patience-empathy-and-kindness)
  - [Don't get worked up over spam](#dont-get-worked-up-over-spam)
  - [How to gracefully close PR's that will not be accepted](#how-to-gracefully-close-prs-that-will-not-be-accepted)
- [Conclusion](#heading-conclusion)

## How it All Began

In December of 2021, freeCodeCamp was launching their [Learn to Code RPG game](https://www.freecodecamp.org/news/learn-to-code-rpg/). It's an interactive visual novel that follows Lydia's dream of becoming a developer. 

I was involved with helping to create quiz questions on topics like HTML, CSS, Computer Science, Python, and so on for the initial launch. 

About a week before the launch, Quincy approached me and a few others to build out a [Developer Quiz Site](https://developerquiz.org/). This was meant to be a companion site to the [Learn to Code RPG game](https://www.freecodecamp.org/news/learn-to-code-rpg/) and provide campers with a way to practice more quiz questions outside of the game. 

The initial launch of the [Developer Quiz Site](https://developerquiz.org/) had about 600+ quiz questions. We also created a few open issues in the [repository](https://github.com/freeCodeCamp/Developer_Quiz_Site) for the community to add more questions to the site. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.11.55-PM.png)

During parts of 2022, there was a moderate amount of activity in the repository but a lot of the time it remained rather slow. But once September rolled around, I thought about entering the [Developer Quiz Site](https://developerquiz.org/) into Hacktoberfest.

I reached out to Quincy and he thought it was a great idea because we could use this opportunity to get more quiz questions from the community.

## Preparing for Hacktoberfest

There were about 3 weeks left before Hacktoberfest started. Here is how I used that time to get the repository ready.

### Step 1: Adding the Hacktoberfest topic and labels

The first step was to add the Hacktoberfest topic to the repository so people knew we were participating in this year's event. I spruced up the About section and added the appropriate labels to help invite people to the repository. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.41.14-PM.png)

I then made sure to create the `hacktoberfest-accepted` label so I could apply it to each approved PR to help us keep track of the total number of Hacktoberfest PR's. I also added the `spam`, `hacktoberfest`, and `first-timers-only` labels because I knew they would come in handy. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.45.45-PM.png)

### Step 2: Creating issue templates

[GitHub issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) are a great way to ensure that contributors provide all of the necessary information for bug fixes, documentation changes, feature requests or general issues.  

I decided to setup 5 issue categories and make certain fields required so contributors would provide some level of detail to the issues they were creating.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.57.28-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.53.25-PM.png)

### Step 3: Updating the contributing documentation

When the repository was initially created, the contributing documentation pointed to the [general freeCodeCamp contributing guidelines](https://contribute.freecodecamp.org./#/). While that documentation is very thorough, it wasn't specific enough on how people could best contribute to the [Developer Quiz site repository](https://github.com/freeCodeCamp/Developer_Quiz_Site) in particular. 

I decided to completely overhaul the documentation and create a new in depth file just for the Developer Quiz Site. Since I anticipated that we would have a lot of beginners with Git and GitHub, I tried to make it as accessible and beginner friendly as possible.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-7.08.50-PM.png)

### Step 4: Creating well-defined issues

In order to attract contributors to our repository, I knew that we needed to have some clearly defined issues. If the issues were too vague, then I knew people would have tons of questions or might not be interested in contributing.

I made sure to include all of the necessary guidelines for submission, including code snippets for the proper formatting, links to the Code of Conduct, Contributing docs, and links to the files they needed to change. 

Here is an example of one of the issues I created to encourage more JavaScript questions.

#### Sample issue

[developerquiz.org](developerquiz.org) currently has over 600 quiz questions. We are looking to expand on the JavaScript questions and we encourage other developers to add their quiz questions to the site.

**Please note: we are only focusing on general JavaScript questions instead of library and framework specific questions.**

You can find the complete list of questions below.
https://github.com/freeCodeCamp/Developer_Quiz_Site/blob/main/src/data/javascript-quiz.ts

You can add your own questions to the top of that file.
**Please first check to make sure your question doesn't already exist in the file before creating a PR.**

Here is an example format for the questions. 

```
  {
    Question:
      "In JavaScript, what is the name of the method used to remove white space from the beginning and end of a string?",
    Answer: ".trim()",
    Distractor1: ".substring()",
    Distractor2: ".reduce()",
    Distractor3: ".slice()",
    Explanation:
      "The .trim() method removes white space (including space, tab, etc.) from both ends of a string and returns a new string without modifying the original.",
    Link: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim",
  },
```
For the `link` field, please make sure to use a freeCodeCamp article, freeCodeCamp YouTube video, or official documentation.
If you choose to reference a video, please make sure to include the timestamp for the topic covered.

You can read more about how to create timestamps in this [helpful article](https://www.lifewire.com/link-to-specific-part-of-youtube-video-1616414#). 

This issue will not be assigned to anyone and will remain open for multiple contributors. 

**Please do not assign yourself to this issue or close it.**

Happy contributing!


For most of our issues, I wanted multiple contributors to be able to participate. So I added a disclaimer at the bottom letting people know that it would remain open and wouldn't be assigned to anyone. 

I also made sure to add the `good-first-issue`, `help-wanted`, and `hacktoberfest` labels to help attract more contributors. 

### Step 5: Adding Saved replies

[Saved replies](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/creating-a-saved-reply) is a feature on GitHub were you can create and save your own messages that you intend to use repeatedly in issues and pull requests.  

I decided to create the following replies:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-7.59.09-PM.png)

I wanted replies to congratulate both first time and returning contributors because they took the time to make our repository better. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.01.40-PM.png)

I also wanted to create a reply where I thanked the contributor for their contribution and requested changes to the pull request. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.05.29-PM.png)

The last reply I created was to let contributors know that their pull request was reviewed but was not going to be accepted. I saw that the main [freeCodeCamp learn repository](https://github.com/freeCodeCamp/freeCodeCamp) used a similar reply so I wanted to include it in the Developer Quiz Site repository.  

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.09.14-PM.png)

### Step 6: Opening up GitHub Discussions

A few days before Hacktoberfest started, I wanted to open up another avenue for contributors to ask questions and propose new features. So I decided to open up [GitHub discussions](https://docs.github.com/en/discussions).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.14.52-PM.png)

When I created this post, we had a few people new to the repository feel welcomed to contribute and happy that there was a place to connect with me and other contributors. 

Now that everything was in place, the countdown to Hacktoberfest was underway.

## Lessons I learned during Hacktoberfest

Right from day 1, I was pretty busy reviewing pull requests and helping new contributors get started in open source. But the whole experience was very educational and rewarding. 

Here are a few lessons that I learned during this time.

### Lead with patience, empathy, and kindness

We were all beginners once, and sometimes it is scary to learn something new. I made sure to lead with kindness and empathy because I remember what it was like to just start out in open source. 

Every time a new question came in, I made sure to reply back and provide as much as assistance as I could to help them resolve the issue. This resulted in a welcoming and safe environment to learn.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-01-at-6.25.48-PM.png)

We also had times where some contributors wanted to add quiz questions but were nervous because English is not their first language. My job was to assure them that I was here to help and not pass judgement on spelling or grammar mistakes. 

I believe that helped in the larger volume of quiz questions we ended up getting. 

### Don't get worked up over spam

One of the downsides to Hacktoberfest is the increased amount of spam pull requests for open source maintainers. While this is frustrating to deal with, I learned pretty quickly to just close the PR, label it as spam, and move on.

There was no point in arguing with them or getting upset because that is wasted energy. The majority of people did want to meaningfully contribute and that is where I chose to spend my energy.

### How to gracefully close PR's that will not be accepted

One of the surprising issues that came up were people wanting to take quiz questions and explanations from other quiz sites and add it to [freeCodeCamp's Developer Quiz Site](https://github.com/freeCodeCamp/Developer_Quiz_Site). The first couple of times this happened, I closed the pull request and let them know that this is plagiarism and we can't accept that. 

Well, I received a response back from one contributor stating that they didn't realize and they wanted to know if they could try again. I assured them that they were free to create a new PR and I could help them with any spelling or grammar. 

This led me to revise my response to let contributors know that they weren't in trouble and were free to contribute again in the future with their own questions.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-01-at-6.42.40-PM.png)

This helped to maintain a healthy open source environment and most of those cases ended up being prolific contributors after they understood the rules. 

## Conclusion

I am really glad that I participated as a maintainer in this year's Hacktoberfest. I learned a lot about communication, empathy, patience, and leadership.

I hope my post encourages you to want to get involved with open source either as a maintainer or contributor in the future. 

