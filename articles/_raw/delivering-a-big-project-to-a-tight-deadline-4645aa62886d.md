---
title: Delivering a big project to a tight deadline
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T12:58:37.000Z'
originalURL: https://freecodecamp.org/news/delivering-a-big-project-to-a-tight-deadline-4645aa62886d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg
tags:
- name: development
  slug: development
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Paul McGillivray

  This week we launched the first phase of a large website for a fast-growing business,
  ‘Jump In’. The company was opening another new trampoline park this week, and wanted
  the website to go live beforehand. So our deadline was fixe...'
---

By Paul McGillivray

This week we launched the first phase of a large website for a fast-growing business, ‘Jump In’. The company was opening another new trampoline park this week, and wanted the website to go live beforehand. So our deadline was fixed, and we were committed to launching a full-fat, high class website in time for the launch.

With only two and a half weeks to build the site once the designs were approved, the whole team had to, er, jump in, and pull together to deliver a project we were proud of.

This was the first ‘under fire’ test for our newly-rebuilt team here at Remote, so it was a good process and we learned a lot about how we work together and how our new workflow performs under pressure.

I thought it would be helpful to share the points that helped us stay on track and launch on time.

### **Prioritize your user stories**

For all our projects, we use the classic User Story backlog with a Kanban board for our task management. Being a .NET development company, we’ve inevitably ended up using Visual Studio Team Services, which we’ve found to be intuitive, simple, and powerful. In the past we’ve worked with [TargetProcess](https://www.targetprocess.com/), [ActiveCollab](https://activecollab.com/), and most recently [Jira](https://www.atlassian.com/software/jira), before moving to [VSTS](https://www.visualstudio.com/team-services/).

We make sure that our User Story backlog is always in priority order. With our hearts happily committed to the Agile Manifesto, those priorities are our customer’s business priorities, and not our development priorities.

What this means is that although we might really feel like we’d like to build the entire business layer for the whole project upfront to make our lives easier further down the road, the business layer in itself doesn’t offer any value to our client — they don’t want a business layer, they want their customers to click a ‘Book Now’ button that works, or to fill in a ‘Contact Us’ form that posts to the Constant Contact API.

So we name and prioritize our tasks accordingly, with the most pressing business requirement at the top, and the business layer is naturally built on an ‘as-needed’ basis.

We get three obvious benefits from this method:

1. We don’t find ourselves building architecture for features that are never built, or features that are never used.
2. If the client needs to swap out a feature in the backlog for a suddenly-more-urgent one, we haven’t wasted any development time in preparing for that feature.
3. If for whatever reason, the client needs to launch early, or runs out of money and can’t continue the development (although that’s never actually happened to us), the project will have already been built with the most important features, and those left behind will be the ones that don’t matter so much.

It’s a comforting and efficient way of working.

### **Build an in-advance checklist**

In the heat of the moment, hours from deadline, it can be easy to forget the small things that are still essential to getting a project launched.

Building a checklist right at the start of the project can help you keep focus in the heat of battle, and also might give you a pointer about what you might be able to do early, before the pressure mounts. Items that are relatively unimportant and small when it comes to development can mean big trouble later down the line if they’re forgotten; stuff like Google Analytics tracking code, and 301 redirects from pages on the old site, to their new replacements.

We created user story tasks for each item, and put them at the bottom of the backlog, so that once all the main features were uploaded and tested, we knew that these jobs also had to be done before launch.

There are some great web checklists available online which might help you think of what you might need to include.

[http://frontendchecklist.io](http://frontendchecklist.io/) is an open source project created by David Dias that’s incredibly comprehensive and trending highly on GitHub at the moment, with lots of community contributions. The [Humaan Website checklist](https://humaan.com/checklist/) is both pretty and comprehensive, as is [webdevchecklist.com](http://webdevchecklist.com/)

Tom Houdmont has a [very detailed and useful article on box UK](https://www.boxuk.com/insight/blog-posts/the-ultimate-website-launch-checklist) on things to remember. And if you want to go deep, the ever-excellent Smashing Magazine has a list of no less than [45 Website Checklists](https://www.smashingmagazine.com/2009/06/45-incredibly-useful-web-design-checklists-and-questionnaires/) to cover every web specialty.

### **Get important information up-front**

Now that we have our end-of-phase checklist, we know what we’ll need to know before launch. It’s really helpful to get any information or resources that you’re missing right away, so that you don’t forget to ask in the heat of the action further down the line.

Take it from me, there’s nothing so disheartening as working your guts out to meet a project deadline, only to realize at the very last minute that you didn’t get a copy of the SSL certificate for the new site, and will have to wait hours for a new one to be processed because the client’s IT manager doesn’t have a copy of the private key.

DNS login details, Google analytics ID, SSL certificate, and any other documents, images and any other resources you might need during the project development — anything you can get right upfront might save you hours later when it matters.

### **Don’t let scope-creep destroy your deadline**

When the client begins to see the project developing, new and previously-unscoped ideas can come in thick and fast. From suggestions for a new way of displaying data, to whole new features and sections that had previously been forgotten and omitted from the spec, it can be tempting to see the new must-have, and down-tools to add it to the project. That’s fine, but let’s remember the most important thing first.

There’s an old saying in the software development world: “Quality, Budget, or Time: pick any two”. We don’t like that. We don’t ever want to compromise on quality, go over budget, or miss a deadline. So we add a third: Scope.

So we keep our quality, we stick to budget, and we meet our deadline, but what’s delivered on that deadline is continually up for discussion and consideration.

So when a client asks for a new feature — mid-development — that will for example take half a day to build, we reply “certainly — which feature would you like to remove from the release to make way for this new feature?”

The resultant discussion will make sure that the client is focusing on their priorities, and will help inform them whether that new idea is worthy of the current release or whether it should be held off for a future phase. By keeping control of the scope, we keep the other values (and our evenings) protected. Which leads me nicely to my next point:

### **Keep quality high**

New features are built and uploaded quickly as the deadline approaches, and we can easily forget to test as thoroughly as we would normally. And quality control for stylesheets and interactions can just as easily be compromised.

I’d much rather spend that extra time when I’m in the code for a feature to make sure I’m going to deliver it properly — looking as it should, working as it should, with the correct stylesheets and appropriate validation on forms and so on.

I’m not saying we should over-build and write code that’s not required, but it’s much nicer to spend the time doing it right than having to go back and look at it again at the client’s request when I’m much closer to the deadline. It’s stressful, and I don’t need that kind of negativity in my life, thank you.

Keep it lean, keep your patterns in check, write your tests, and do your QA. First time, not when it’s about to launch — or worse, after it’s launched!

### **Don’t lose your process under pressure**

Flowing from what I’ve just been saying, as well as keeping your code clean, it’s important to keep your project management process in place when you’re under fire too, especially if you’re working in a team.

I’ve totally been there — I’m running out of time, and so instead of adding my user stories to the VSTS backlog, I write a little checklist in Notepad++ or [Todoist](https://todoist.com/) (my new favorite productivity tool). Before I know it, none of the team knows what tasks I’m working on, no one knows what tasks have been done, and another one of the dev team are working on something I’ve already fixed.

Stick to the process — there’s a reason it’s in place, or you’ll end up slowing down by trying to go more quickly.

There’s a fantastic book about this called ‘[Work Clean: The Life-Changing Power of Mise-En-Place to Organize Your Life’](https://www.amazon.co.uk/Work-Clean-Life-Changing-Mise-En-Place-Organize/dp/0241200334) by Dan Charnas. In the book, Charnas talks about ‘Slowing Down to Speed Up’ — taking time to make sure everything is prepared and processes are in place actually helps you reach a much faster productivity speed when you’re in the flow. Give it a try, and check out the book, too; I loved it.

### **Make sure you’re clear on your definition of “done”**

User stories are, by their definition, usually short and concise. We ensure that our agile-inspired project management doesn’t turn into a simple waterfall in short cycles by discussing each story when it’s due to be done, instead of speccing it out weeks in advance in full detail.

The downside of this is that a developer who’s not been involved in the scoping and specification process won’t have the full background on a user story when they pick it from the top of the list. If everyone’s got their head down on their own stories as the deadline draws near, it might be tempting for the developer to just get on with the task.

Now in many cases, a simple and concise user story will be easy to interpret. But in other cases, the developer could find themselves down a rabbit hole, working on tasks that simply don’t need to be completed by the deadline.

There are a few things we can do to try to prevent this scenario:

Taking to heart the ‘Slowing Down to Speed Up’ concept I’ve just referred to, the developer must always talk with the product manager about the story if there’s any need at all for clarification.

As developers, it can be very easy for us to think ‘oh it’s ok I got this’ and just get on with it. But remembering that the customer is part of the team, picking up the phone and going over the story with the client can be very enlightening most of the time.

At the very least, a quick conversation with the person who wrote the ticket will make sure that everyone’s on the same page.

The person writing the user story in the first place should include a ‘definition of done’. This can simply be a list of things that will happen when the story is completed. For example:

* The user clicks on the ‘reports’ button, and is presented with a list of reports
* The list contains the name, description, file type, and a ‘download’ button for each report
* Clicking on ‘download’ saves the report to the user’s device
* Access tokens must be used when retrieving the downloads to maintain security of the documents

So, those are the main things that either saved us or held us back, depending on when the lessons were learned during this particular project. I really hope you find some of these points useful when you’re working to a tight deadline, or even if you’re just working on your next software or web project.

We still have a couple of phases to go, but both us at Remote, and our clients, Jump In, are delighted with the site so far. Check it out at [www.gojumpin.com](http://www.gojumpin.com/).

Originally published at [remote.online](http://remote.online/journal/delivering-a-big-project-to-a-tight-deadline).

