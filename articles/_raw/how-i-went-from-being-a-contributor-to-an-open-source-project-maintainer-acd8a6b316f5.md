---
title: How I went from being a contributor to an Open Source project maintainer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T17:04:16.000Z'
originalURL: https://freecodecamp.org/news/how-i-went-from-being-a-contributor-to-an-open-source-project-maintainer-acd8a6b316f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DgEQHQ2yavA5ex3FmlxrUQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dhanraj Acharya

  I was a lone software developer. When I was in college, I attended the KDE conference.
  It was my first encounter with the open source world. At the conference, I thought
  the presenters and the people raising hands were very smart. ...'
---

By Dhanraj Acharya

I was a lone software developer. When I was in college, I attended the KDE conference. It was my first encounter with the open source world. At the conference, I thought the presenters and the people raising hands were very smart. I knew there was free software available, created by the community for the community. But the developers that build it were foreign to me.

I thought really cool, intelligent people developed this software. I thought you had to to be really smart and privileged to join them.

I tried to participate in Google Summer of Code ([GSOC](https://summerofcode.withgoogle.com/)) two times during college, but wasn’t successful. Then after graduation, during my job, I used lots of open source projects. I even used them when freelancing. I heavily relied on community-developed tools and tech. I was really fascinated with people’s stories on how they started contributing to open source, and how they got their amazing remote jobs!

Now after procrastinating for another two months and not being able to land a remote job, I decided to do it once and for all and contribute myself.

I started uploading my code to the [GitHub](https://github.com/drex44) — whenever wrote any new code. I created an open source [NPM module](https://github.com/drex44/awesome-react-links) along with some other demo projects and uploaded them. But this wasn’t the gist of open source. I wasn’t actually contributing to other repos or working with other developers to create software. I was still working in isolation.

### Hacktoberfest!

Then it came: I stumbled upon [Hacktoberfest](https://hacktoberfest.digitalocean.com). They (DigitalOcean, GitHub, and Twilio) were giving away a **free t-shirt** if you submitted 5 Pull Requests to an open source project on GitHub in October. Even if your PR was not merged, still it counted towards your progress. And this time, they had a ton of t-shirts, so, it was easy to get one. This was the final push I needed — apparently, a free t-shirt gives you an amazing boost!.

So thus I started my journey in the OPEN SOURCE WORLD.

### Tracking down the issues

I searched for open source projects to tackle on GitHub. I wanted some easy tasks to quickly get familiar with the PR process. So I looked for issues which did not require me to jump into the whole source code.

There were many developers who started projects for Hacktoberfest and newcomers. It was easy to submit PR in these repos, so I submitted three PRs. I submitted my other two PRs to other people’s personal projects. There were many other repos where you just had to add your name to the file and submit the PR. But I decided that this was not productive and was not the spirit of open source.

Then I came across this amazing developer. She had created a static blog in Vue.js and had many issues listed. When I saw all of the issues, I found out that basically, she was making a personal blog and getting people to contribute by raising issues and labeling them with appropriate tags. I was like **?.**

Then I realized that the idea was great and I was like,

![Image](https://cdn-media-1.freecodecamp.org/images/Tr8DG2tcjF2t8FylD51k6TThhcMkT7BCA6C2)
_Hahaha_

I was impressed with her talent! She was building her static blog, and at the same time it was also benefiting other developers. First-timers were learning to work in the open source and getting a free t-shirt. She was getting her blog through a group effort!

Discovering her blog is what motivated me to create the [Good Food Guide](http://github.com/drex44/good-food-guide).

### The rise of the [Good food guide](http://github.com/drex44/good-food-guide)

I had already decided what to do once I had finished submitting my PRs. So after two days of work and submitting PRs, it was time for a new beginning. I was inspired by all other developers who had created a repo to support Hacktoberfest. They all were creating a welcoming environment to encourage newcomers to submit productive PRs. I also wanted to give my contribution towards this movement and decided to create my own project repo.

I too want to become an entrepreneur, and I have a list containing multiple ideas. But I did not want to put too much time into deciding which project to start. I looked through all the ideas and picked the one I thought was easy to understand and easy to implement.

I chose to build the **Good Food Guide.** My sister and I used to Google about which foods to eat to cure a particular disease. I thought, what if there’s already a site where you can just go and search for your symptoms or disease and it’ll tell you about the foods to eat? It should be available in all languages so multiple people can use it easily.

So I created a basic UI which conveyed the motivation and use of the website. I wanted to quickly upload it, so I decided to have all the data in a static file only. I wanted to choose a technology which was easy to learn and widely used. This would allow new developers to learn or existing developers to practice. So I ended up using React.

On top of it, I decided to use NextJs to leverage many of its features. It is also easy to use if you already know React. I uploaded the whole project on [GitHub](https://github.com/drex44/good-food-guide) and the journey began. But this wasn’t enough to attract the developers.

### The rise of the maintainer

After committing the initial code, I then produced proper documentation. I created issues with the appropriate labels. I created the issue just like we create tasks in an agile sprint. Moreover, I divided the tasks into sub-tasks and listed them with full details.

When I was looking for issues to contribute to, I looked for issues with a detailed problem and directions for the solution. So I tried to include the information I initially looked for in the issues.

This worked like a charm, and it was exactly what was needed to get the first timer contributors aboard. Most popular projects are useful to contribute to. The lack of information in issues works as a demotivation for them. Due to this, most of them don’t work on actual issues after compiling the code.

#### Example issue

![Image](https://cdn-media-1.freecodecamp.org/images/w4OHKsXyVbbu8ja7ckZRkMqLnwUiyGFAQK1Q)
_example issue_

One more thing which I did was publish the master branch with Netlify. Netlify has a great integration app with GitHub. So if any PR is merged then the contributor can see the change go LIVE almost instantly.

The result? I got 3 PRs and 4 requests to work in just 2 hours (told you, the power of free T-shirt is very strong ?).

I successfully went from being a contributor to a project maintainer!

### Understanding the other side of the coin

The repo was becoming more popular. People were raising issues for suggestions, submitting PRs, and commenting on issues. My repo was getting attention and it was just amazing.

I was getting notifications all day. Every hour I would get at least one notification from GitHub! I was juggling here and there. I was reviewing PRs, answering comments, merging PRs, raising more issues, and contributing.

One amazing feature that came handy by integrating Netlify was that it automatically sets CI (Continuous Integration) for your project. It performs various checks on the submitted PR, and also gives a test deployment where you can check the integration. I recommend using this feature in any projects you can!

As a result, people were learning and having fun! And also getting a Free T-shirt. I learned so much about GitHub and git. Pro tip: if you want to learn git fast then become an open source project maintainer. It gave me a new perspective and broadened my vision. So it was a win-win situation for all of us.

> “Anything that can go wrong will go wrong.” — Murphy’s Law

For some time, I would check the PR details, skim through the code, look at the deployed integration and merge the PRs. Sometimes, due to many pending PRs, after merging the first PR, it would create a ripple effect and there would be conflicts in all other PRs. Now, this looked bad initially but it was a blessing in disguise. Due to this, I learned how to resolve conflicts in git. I resolved many conflicts. Github’s online editor for merging PRs proved very handy for small changes.

Although the PRs did not all have good code quality, I still merged most of them. Because as they were from the first time contributors, I did not want to discourage them from submitting more PRs. I know the feeling when you submit a PR and keep waiting for the maintainer to approve or comment on it. So to keep the spirit of the contributors up, I decided to merge the PR and then do the clean up myself (and I think this resulted in a positive feeling for contributors).

As the number of PRs increased, I couldn’t give much time to contributing myself. Most of my allotted time would go to answering comments, emails, and merging and resolving PRs. After three days, I sat down to clean the code. It was a mess I only invited. I realized that I should have informed the contributors to follow at least some guidelines. The file names, function names, and project structure was all wrong. As the website was evolving, so were its problems.

I had to re-structure the whole codebase. It was a breaking change but it was much needed. If this continued, then the code would become non-maintainable after some time. This is when I realized why many companies emphasize their coding standards. I mean, I already knew the importance, but experiencing it first hand as a project maintainer was another thing! I could see why many popular open source projects were rigid about their coding standards.

I can also see how my thought process has evolved over the past 10–11 days. I was a naïve contributor working on his own repository, but managed to become a project maintainer working with all other developers.

#### GitHub Stats

Here are the stars, forks and contributors in the past 11 days!

![Image](https://cdn-media-1.freecodecamp.org/images/Z3mB1v5Vuj0BoSNSc6QmeiJgu3IWjpWhPOtC)
_GitHub stats_

### The Result!

A non-responsive website created in 10 minutes!

![Image](https://cdn-media-1.freecodecamp.org/images/sge5u4AyVadJ9fC4UwNdg33Q8ImZG5ma91JZ)
_Home_

![Image](https://cdn-media-1.freecodecamp.org/images/gbfiLSsJoTthqzjE4hqtp45A6H-b1cNuLdNR)
_About_

#### After 11 days,

![Image](https://cdn-media-1.freecodecamp.org/images/Ic76JVetjNJC2SLApBL3k-FyIkLXocoak8HO)
_Home_

![Image](https://cdn-media-1.freecodecamp.org/images/1nAIMG-dkvqh68zeU8wTbr7mB2HZ2YktXmQz)
_About us_

![Image](https://cdn-media-1.freecodecamp.org/images/7JDpAL606fb8Lk1SlLJYzLtNkniILKvKQcdM)
_Contributors_

![Image](https://cdn-media-1.freecodecamp.org/images/WWXyT7MCe3aREFRrhmnDg5bclf7iznwhzUZz)
_foodDetails (Work in progress)_

![Image](https://cdn-media-1.freecodecamp.org/images/hLnCHASQNOpS68JGSzAgzD93fdx0dOiynqRb)
_terms_

You can also checkout the latest version of the website live at [https://good-food-guide.now.sh](https://good-food-guide.now.sh/).

Each day the site is improving in a small or big way.

#### Bottom line

This 11 day journey has been great for me. I’ve learned a lot. Now, I can see both sides of the coin.

I see the power of a team and what it can achieve. If a handful of people decide to work on a particular issue then they can solve anything. People need a welcoming environment and a little bit of reward to stay motivated.

It can be difficult for new developers to start contributing. They look for issues to solve but it is not the only way to start contributing. The main idea is to have fun and build something collectively, to improve a piece of software. If you have used it and know something you can improve, then you can directly raise the issue, discuss with the maintainer, and submit a PR. I think this is one of the best ways to start.

It became clear to me how a project manager uses each individual’s strengths to accomplish a task that would’ve been difficult if done by a single person. This is the same situation in open source projects. The job of the maintainer is similar to the project manager. They have to maintain harmony between all developers and also listen to their thoughts.

I also realized that, before, I had this fear of a big codebase whenever I would think of joining a new open source project. I would compile the code, run it, and forget about it. Now that fear has gone and I think I can take the big step towards contributing to big projects. I hope to continue learning new things and become a good asset to the open source community.

Thank you for reading! And big thanks to **Jennifer and Abbey** from freeCodeCamp for reviewing. They helped me to prepare this article and make it worth your time.

If you have any questions or suggestions, then leave them in the comments below.

P.S. If you found this article helpful, clap! ??? It feels rewarding and gives me motivation to continue my writing.

[**drex44/good-food-guide**](https://github.com/drex44/good-food-guide)  
[_A guide to know which foods are good when you have certain disease! [Built in React/NextJs] - drex44/good-food-guide_github.com](https://github.com/drex44/good-food-guide)[**Good Food Guide**](https://good-food-guide.now.sh/)  
[_A guide to know which foods are good when you have certain disease!_ good-food-guide.now.sh](https://good-food-guide.now.sh/)

Edit:

Updated the URL to the Live site to [https://good-food-guide.now.sh](https://good-food-guide.now.sh/).

