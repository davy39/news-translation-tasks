---
title: 'A better web development workflow: Confluence, Airtable and more'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:38:58.000Z'
originalURL: https://freecodecamp.org/news/a-better-web-development-workflow-confluence-airtable-jira-abstract-e626ef4ff5bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K3DXpE4GwzoHTtFrrvF6Rw.png
tags:
- name: Design
  slug: design
- name: management
  slug: management
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'By Vince MingPu Shao

  Working as a front-end developer for nearly two years, I’ve got helpful experience
  from being part of several web development projects of design/digital agencies.

  One obvious but valuable lesson I’ve learnt is that collaborating ...'
---

By Vince MingPu Shao

Working as a front-end developer for nearly two years, I’ve got helpful experience from being part of several web development projects of design/digital agencies.

One obvious but valuable lesson I’ve learnt is that collaborating between each groups with one goal but distinct responsibilities and purposes is not easy. There’re different aspects and levels of difficulties in terms of collaboration, and the specific part of which I’d like to address here is workflow process.

Based on my experience, and with the help from my designer and developer friends, I built a website development workflow designed for small team (5–15 people). The system is composed of [Confluence](https://www.atlassian.com/software/confluence), [Jira](https://www.atlassian.com/software/jira), [Airtable](https://airtable.com/) and [Abstract](https://www.abstract.com/). In this article, I’ll share the why and how of the this workflow.

### **Motivation for building a new workflow**

To deliver a customized website without using templates provided by [website builders](https://www.wpbeginner.com/beginners-guide/how-to-choose-the-best-website-builder/), the minimum talent requirements includes a designer, developer and project manager. After participating in a couple of cases, I had a sense that there was something wrong with the workflow we had: important information was always not aligned both internally between different roles and externally to the client. This inefficient communication was clearly slowing down the development cycle and hurting the team.

So I started to solve this problem.

![Image](https://cdn-media-1.freecodecamp.org/images/OvSIwKWcr0uLNPIPbzpIfRHQS9zaHGbsbAbi)
_Google search workflow great resources: [workflow definition](https://medium.com/eightshapes-llc/system-features-step-by-step-e69c90982630" rel="noopener" target="_blank" title="">Design systems features</a>, <a href="http://styleguides.io/" rel="noopener" target="_blank" title="">style guide resources</a> and <a href="https://www.projectmanager.com/training/define-workflow-process" rel="noopener" target="_blank" title=")_

I Google searched resources about establishing and improving a workflow. Though I learned a lot from all the great resources, I found nearly none of which was for web development projects in a design/digital agency. It was either a design system or coding guidelines that scoped in design or front-end roles, or a workflow that was built for a team with its own product.

As a result, I decided to cherry pick the parts I needed to solve our problems, and formed a customized workflow for website development.

### **Problems and goals**

Following are the problems I inspected from our existing workflow, and the corresponding improvement goals:

#### **1. Waterfall methodology**

![Image](https://cdn-media-1.freecodecamp.org/images/DoyhUSqgX3dzSOt-H13itXsiXmdgnBidIS0V)
_waterfall model abstract demo_

**Problem:** Based on my experience, website projects adopt a waterfall approach because clients don’t have a concept of a minimum viable product (MVP). Instead of splitting functionalities from views and modulization, clients tend to think about the site in a traditional page-by-page way, which forces both designers and developers to work page by page in sequence. This causes them to lose a universal perspective across the project. This situation results in lots of back-and-forth redundant revisions between pages.

**Goal:** Changing the mindset of clients is both arrogant and unrealistic. The goal is to find a way to separate requirements from views as soon as possible and develop in as as modulized a way as possible internally based on page-by-page model.

#### **2. Universal design tokens and components managed by both designers and developers**

![Image](https://cdn-media-1.freecodecamp.org/images/vvgm0WaDEKF0T2cOXCKFxtTvQU8cv1542eZe)
_design tokens from [Salesforce](https://www.lightningdesignsystem.com/design-tokens/" rel="noopener" target="_blank" title=")_

**Problem:** This is a common issue that a lot of articles have shared great solutions to, which mostly propose building a design system that’s managed by [style guide/library generators](https://github.com/davidhund/styleguide-generators#user-content-nodejs). Though it is great solution, managing an extra site that barely provided edit permission to designers was not appropriate in our situation.

**Goal:** Except for creating universal design tokens and languages that designers, developers and managers can all understand, build a system that allows everyone to manage the assets in a synchronous way.

#### **3. Accurate, updated progress dashboard**

![Image](https://cdn-media-1.freecodecamp.org/images/FwCH5YpT2UsHNFtkhBFjwA0X5EYvii65dZ2G)
_we need an editable and accessible progress dashboard_

**Problem:** Though issue trackers, kanban, and more project management models are useful and practical, most of them failed to act as a straightforward, flexible and friendly progress dashboard. This kind of dashboard would save the team a lot of time because it would prevent team members from actively reporting or asking about the current situation of specific tasks. It also makes managers’ lives easier if they have a clear knowledge of the entire project without too much effort.

**Goal:** Build a dashboard system that provides edit permission for individuals in charge of specific tasks.

### **Workflow diagram**

Before we dive into the detail introduction of the management tools stack, let’s take a look at the abstract simplified workflow I organized. It’s pretty much just a visualization of a normal workflow that most agencies have, but there’s two points to be noted here.

![Image](https://cdn-media-1.freecodecamp.org/images/KJYSglCts4eVtawsVirn4A5Yk0q9uX0mb8kL)
_workflow diagram I designed_

#### **1. Developer evaluation**

First, when requirements or issues coming from the client are approved and documented by manager, with the exception of sending the task to a designer, they also go to a developer for evaluation. In this process, the developer reviews the specification of the task, checking if there are any rather complicated functions or features included. If it’s positive, the developer could start working on it or notify the designer about the potential problems beforehand.

#### **2. Single source of truth**

Also notice that after design deliverable is approved by the client, and before handing the task over to the developer’s hand, it goes through a process of **register/modify/delete over design store** conducted by the designer. This is because the developer should always be exposed to one and only one source of design store, which contains constantly maintained and updated assets ready for development.

Now we can dive into the management tools stack I prepared and see how the tools help us solve our problems.

### **The tools stack**

After experimenting with various options on the market, the stack I’m proposing here is composed of [Confluence](https://www.atlassian.com/software/confluence), [Jira](https://www.atlassian.com/software/jira), [Airtable](https://airtable.com/) and [Abstract](https://www.abstract.com/). In addition to basic introduction and few key application examples, I’ll not cover all the details of using the tools.

![Image](https://cdn-media-1.freecodecamp.org/images/gsTUQmkRJBddtnziPdjtqnVDMbVjnhBXhPTU)
_[ABEM](http://atomicdesign.bradfrost.com/" rel="noopener" target="_blank" title="">atomic design</a> and <a href="https://css-tricks.com/abem-useful-adaptation-bem/" rel="noopener" target="_blank" title=")_

Note: the system assumes that the development team adopts the [atomic design methodology](http://atomicdesign.bradfrost.com/) and [ABEM](https://css-tricks.com/abem-useful-adaptation-bem/) naming system.

### **1. Confluence**

**Role:** information and resource center

Though it’s intimidating at first, [Confluence](https://www.atlassian.com/software/confluence) provides a powerful workspace that’s easy to organize, and it has tons of features, integration of apps, and customized templates. It’s definitely not a universal solution to all problems, but it’s perfect for documentation of specifications, requirements, meeting notes and more.

Therefore, Confluence in this stack works as an information and resource center, which means every related link and detail about this project should be documented properly in here.

My favorite advantage of Confluence is the ability to customize document templates. This feature makes it really convenience to standardize the workflow.

![Image](https://cdn-media-1.freecodecamp.org/images/zukI9t8HsDbd772oHP5IU5AYp0FdmHsLxccu)
_developer evaluation stage_

#### **Example:** Component functionality review

I mentioned the **developer evaluation process** above, which is actually a complicated job. This is because this process includes basic information of the component, a developer’s [FSM review](https://www.vinceshao.com/blog/how-to-design-ui-states-and-communicate-with-developers-using-fsm-table) (if necessary), FAQ space and more. But the flexibility of the template and tools Confluence provides makes this super easy. Just build a template in configuration settings and you’re good to go.

![Image](https://cdn-media-1.freecodecamp.org/images/S58FbHZlVK5HY-YykmaxzZIb51ggDDM2gvzu)
_custom template for component review in Confluence_

### **2. Jira**

**Role:** issue tracking and action type management

Also a member of the Atlassian family, [Jira](https://www.atlassian.com/software/jira) is a super powerful issue tracking and project planning software. My favorite part about it is making customized issue workflows. Since there are tons of great tutorials on how to utilize power of Jira, the only thing I want to point out here is using issue type as mentioned below.

![Image](https://cdn-media-1.freecodecamp.org/images/qoZ5zv8GbyTHSKRLnEj8g2oI6ybCj6xreaTG)
_designer update design store_

#### **Example:** Update developer on changes of design store by [issue type](https://confluence.atlassian.com/jiraportfolioserver024/configuring-initiatives-and-other-hierarchy-levels-934716034.html)

To ensure that developers are building the components based on correct design views, they need to be notified whenever something in the design store is being updated, which includes actions like **register, modify and delete**. So, as a component is updated, the designer should open an issue with the responsible developer assigned and the correct issue/action type selected.

![Image](https://cdn-media-1.freecodecamp.org/images/T7JTRAHQx4Pix-oLPoiMXbQP2weMpxoskBFv)
_[Jira issue types function](https://confluence.atlassian.com/jiraportfolioserver024/configuring-initiatives-and-other-hierarchy-levels-934716034.html" rel="noopener" target="_blank" title=")_

### **3. Airtable**

**Role:** component management and progress dashboard

[Airtable](https://airtable.com), a mixture of spreadsheet and database, is the thing that makes this stack work. There’s two amazing features that support my workflow: four types of view transition in single table and related content linking. I’ll showcase two examples of using these two features here.

![Image](https://cdn-media-1.freecodecamp.org/images/peF16s69oSsbNSBglXcfYq5EepGzbXF9HNi8)
_developer starts working on the task_

#### **Example 1:** Component management

How do you manage your component library? We chose not to use a style guide generator, because it’s not accessible for designers to edit. Using the Sketch component library wasn’t appropriate either, because it’s has too many limitations if we tried to use it outside the scope of the software itself.

I wouldn’t say Airtable is a perfect solution, but it’s the easiest and most flexible option I could think of. Take a look at the demo template of the component management table here:

![Image](https://cdn-media-1.freecodecamp.org/images/h825KA9cEz3P3tgn911Lq8GHP9nXGDp8RSGc)
_component table_

Once a newly registered design view that’s ready to be developed programmatically is submitted to the developer, they would asses the view based on the ABEM system, and register it into the table. There are 9 columns in the table, including:

**1. Name:** naming of the component in ABEM principle

**2. Preview:** screenshot or exported image of component

**3. Linked page:** link to the page contains this component

**4. Children component:** link to children components contains this one

**5. Modifier:** checks if there’s style variations (ex: — active, — red)

**6. Component category:** a general category classification (ex: text, hero, sidebar)

**7. Development status:** status of development progress (pending, assigned, in progress, complete, in revision)

**8. Assignee:** developer responsible for this component

**9. Atomic level:** atomic category of this component (atom, molecule, organism)

The best thing here is that you can reference data in both the same and other tables. This connection of dots prevents things from getting messier as the scale grows. Also notice that you can filter, sort and change views easily.

#### **Example 2:** Page development status

Since the assumption here is that we’ll inevitably asses development progress page by page, a table template designed for this purpose is necessary. This table can be a progress dashboard for both internal teams and shared with client at the same time.

![Image](https://cdn-media-1.freecodecamp.org/images/UBnBd4zGsyJu7Yeiq01oSwuvSB8J1R39muZx)
_page list table_

Any information about the page, including deadline, InVision prototype link, assignee, and children component can be organized here. Note that it’s very convenient to document and update design, front-end, and back-end development status at the same time.

### **4. Abstract**

**Role:** single source of truth and design assets version control

[Abstract](https://www.abstract.com/) is [GitHub](https://github.com/) for [Sketch](https://www.sketchapp.com/) assets that saves designers from the hell of copying and pasting files. It’s out of this article’s scope to demonstrate details of managing version control flow. The key takeaway here is that Abstract is the design store that acts as the **single source of truth**. Designers should keep updating master branch to the latest version of confirmed design and then notify developers. On the other hand, developers should only take design assets in the master branch as reference.

![Image](https://cdn-media-1.freecodecamp.org/images/gyVsOvJOSx72uhwZNAPIV0nrHNh5DfuZsrMa)
_[Abstract branch template](https://www.abstract.com/how-it-works/" rel="noopener" target="_blank" title=")_

### More work to be done

From my own experience, development of the entire project after adopting this new workflow has been at least two times faster than before. It’s not a perfect solution, because it still requires lots of manual labor to update and maintain.

But I think it could be aa helpful reference to website development teams searching for aa better workflow, and hopefully more people can share their workflows in the future!

---

_?[中文](https://medium.com/as-a-product-designer/a-better-web-development-workflow-confluence-airtable-jira-abstract-zh-24fc8d5b8329)_[_版連結 (Chinese version)_](https://medium.com/as-a-product-designer/a-better-web-development-workflow-confluence-airtable-jira-abstract-zh-24fc8d5b8329)  _/ Originally posted on_ [_vinceshao.com_](https://www.vinceshao.com/blog/a-better-web-development-workflow-confluence-airtable-jira-and-abstract)

