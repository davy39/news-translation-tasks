---
title: What I learned by diving into Hacktoberfest for the first time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-06T23:55:20.000Z'
originalURL: https://freecodecamp.org/news/the-results-of-dipping-my-toes-in-this-hacktoberfest-3def90987fcc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fvKBQ0addZa-P8zY
tags:
- name: GitHub
  slug: github
- name: hacktoberfest
  slug: hacktoberfest
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Travis Fantina

  Imposter syndrome is something we all struggle with to one degree or another. Imposter
  syndrome is the fear of exposure as a fraud. If you’re anything like me you have
  felt like your work was not good enough to show. Or you weren’t ...'
---

By Travis Fantina

Imposter syndrome is something we all struggle with to one degree or another. Imposter syndrome is the fear of exposure as a fraud. If you’re anything like me you have felt like your work was not good enough to show. Or you weren’t far along enough in your journey as a developer to have much to contribute.

After learning about Hacktoberfest last year, I wanted to contribute. But I felt overwhelmed, and imposter syndrome began to take hold.

I told myself I was too inexperienced as a developer and I worried that my commits wouldn’t be worthwhile. Unfortunately, I let those fears get the better of me, and I didn’t even bother signing up.

This year I forced myself to set my fears aside, studied [this post](https://medium.freecodecamp.org/hacktoberfest-2018-how-you-can-get-your-free-shirt-even-if-youre-new-to-coding-96080dd0b01b) on Hacktoberfest, and I dove in. I’m going to share a little of what I worked on and the benefits of getting involved. Benefits that go far beyond getting a shirt and can be had 12 months out of the year!

![Image](https://cdn-media-1.freecodecamp.org/images/cqmCGieQ0qebpj3trmwsa3RW01EETqHfgmd9)
_Image: [twillo](https://www.twilio.com/blog/hacktoberfest-and-new-twilioquest-mission-here" rel="noopener" target="_blank" title=")_

#### My Hacktoberfest experience

I began on October 11th. I was starting at a slight disadvantage already being a third of the way through the month.

The time crunch motivated me. I decided I would try to submit a pull request every Friday and once during the week for the rest of the month. Setting a schedule was important. I focused on pull requests two or three days out of the week and tried not to stress the rest of the time. Regardless of how ambitious your goal is, five pull requests in a month or five pull requests in a week: it’s important to have a plan.

My first pull request was on freeCodeCamp. I was working through some of the JavaScript algorithms challenges. I noticed a link pointing to an unexpected location. It was a simple fix but it provided some needed confidence. There were indeed things out there that I could tackle!

The pull request was easy, I didn’t fork or clone the freeCodeCamp repository, I opened it right on the GitHub page.

Boom first pull request opened.

I didn’t want all five pull requests to come from one repository (although there is nothing wrong with that). After a few pull requests on freeCodeCamp, I started venturing out and exploring GitHub.

I started by looking at projects I was familiar with familiar with. Specifically, I browsed tools and projects that I had used a lot like Rails, React, Bootstrap, and Devise, among others. Whenever possible I searched by issues tagged “Hacktoberfest”, “First Time Contributor” or “Easy”.

![Image](https://cdn-media-1.freecodecamp.org/images/nvN-kYzKeFb1rpF5rBOhtJo0qr-LI2uOQfvf)
_GitHub makes it easy to search through issues_

With larger projects, there are a lot more contributors. The easy issues tend to get ironed out fairly quickly. I narrowed my search to smaller repositories.

A few years ago a friend and I built a reviews site for professors called “AvalueMeuProfessor”. Working on that project I discovered a library called [jQuery Raty.](https://github.com/wbotelhos/raty) This library makes it easy to add voting stars to your project. Although it has over 2,000 stars on GitHub there were only 21 contributors. It had several unresolved issues.

![Image](https://cdn-media-1.freecodecamp.org/images/E5RQPbqXZVfFjDEOrj8PSGbSy2uDT8ehCGcu)
_Raty doing it’s thing…_

Improving what I could, I submitted a pull request that added value to the project. This is important. The size or scope of your pull request doesn’t matter but it should provide value to the project. It was merged into the project in a few hours.

Even though I only fixed typos in the documentation I gained a new understanding of how the library worked. It also gave me a greater appreciation for the project and its maintainers.

Through my work with Rails and the Raty app, I happened across an abandoned Ruby gem. It served jQuery Raty into the Rails asset pipeline: simple but useful. There were a few open issues but the readme made it clear that the project was abandoned.

Again, this was an ideal project because it was small in scope and activity on the project was minimal… none.

I forked the repository and began updating the gem to make it compatible with Rails 5. In the process, I learned a bit about the asset pipeline and a whole lot of how Rails gems work. I read several articles on creating gems that I otherwise would have never seen. In the process, I reached out to the original creator. He was no longer interested in managing the project and I took it over. It’s now maintained on [my fork](https://github.com/tfantina/jquery-raty-rails).

Despite my initial insecurities about contributing, I took the plunge and pushed myself. I was hoping for a shirt but I ended up getting a more. I was able to:

* Submit my first pull request in a public repo
* Learn a lot about Ruby gems
* Take over the maintenance of a gem
* Gain a new appreciation for some of the tools and resources I have used for years
* Boost my average commits for the month (by a lot)
* Became more comfortable with Git both on GitHub and through the CLI

![Image](https://cdn-media-1.freecodecamp.org/images/CHMriD3rpBsx0hsPF1gjwSo9MHA12ypLBuLQ)
_Hacktoberfest gets it done! (From [https://hacktoberfest.digitalocean.com](https://hacktoberfest.digitalocean.com" rel="noopener" target="_blank" title="))_

Above all else, my participation is Hacktoberfest has made me a better developer with a greater desire to contribute. I’ve seen that there is room in these projects for new contributors.

You may want to contribute but worry that you are not good enough or don’t know where to start. But contributing to open source repos is not only for senior developers with years of experience. Contributing to projects is a great way to improve your skills, gain confidence and practice coding. While finding the right project may take a bit of searching, it will be well worth your while.

