---
title: Legacy Code Tips – How to Take Over an Existing Project and its Codebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-17T16:01:28.000Z'
originalURL: https://freecodecamp.org/news/taking-over-an-existing-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/exisiting-proj.jpg
tags:
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: tips
  slug: tips
seo_title: null
seo_desc: 'By Milecia McGregor

  Working as a developer means you need to know how to dive into existing code bases.
  When you inherit a project, there are a lot of specifics that you don''t know, like
  why some of the code is written a certain way.

  So when it''s tim...'
---

By Milecia McGregor

Working as a developer means you need to know how to dive into existing code bases. When you inherit a project, there are a lot of specifics that you don't know, like why some of the code is written a certain way.

So when it's time to go into a hand off meeting, you need to know what questions to ask. This is the best time you will have to get the information you need to get up and running.

These questions come up in every project. You could be starting a new job or working on a different project at your current company. Regardless, here are a few things you should bring up in transfer meetings.

## Know what it's supposed to do

![Image](https://www.freecodecamp.org/news/content/images/2020/05/what-it-does.png)

What exactly is this application used for and who uses it? Without this context, it's going to be really hard figuring out how to implement new features or fix bugs.

Ask about the overall use of the app. Learn about the workflow for different parts of the app and how users move through it. If there's a task list, get a walk-through or more details about each of the items on the list.

This is one of the rare moments everyone is prepared to focus on answering questions about the project. So if there is _anything_ you're unclear on, don't leave that meeting without getting a better understanding of it.

Of course things come up once you start digging in, but this is your chance to preempt a large chunk of confusion. Try and get a high level understanding of the app before you dive into specific questions. Learning about the industry the app operates in can help answer questions that come up in your development as well.

## Know how source control is handled

![Image](https://www.freecodecamp.org/news/content/images/2020/05/source-control.png)

While most projects use Git, not everyone uses GitHub. Some projects could be hosted in BitBucket, Azure DevOps, or even on a SVN. You need to know where code is kept in version control so you can pull it down to your machine and also so you can do troubleshooting when those inevitable production bugs appear.

Make sure that you have access to the code repository and that you have the right level of permissions to do the work you need. When you receive the your login credentials, check them immediately.

The sooner you can find little problems like these, the smoother the project will go in the long run. Fix a small bug and do a quick commit to make sure that you can push up your local branches to wherever the remote repository is.

Also, take a quick look at everyone who has access to the repository. This will be useful info when it's time for pull requests and code reviews. This is also the time to ensure that only the necessary people have access to the code.

Note any users you are unfamiliar with and check with a project manager or someone to see if they still need access.

## Know how to run the project

![Image](https://www.freecodecamp.org/news/content/images/2020/05/run-code.png)

The hardest part of taking on a new project can be getting it set up and running on your machine the first time. There are a lot of one-time commands that can be lost if the process hasn't been well documented.

A few things you need to check that might not be obvious include your env variables, the versions of the software you're running, and the file names you are referencing. 

Other things that might come up are setting up a new local database and loading the seed data and changing any connection strings to APIs or databases.

```
REACT_APP_NAME="Boogaloo"
REACT_APP_API="https://not-staging.morwl.com/api"
API_KEY=ij2i0r9j02tt904tn93
```

If you are going through setup and you notice yourself running into issues, make sure you're documenting them so that it's easier for the next developer to do it. Plus you never know when you'll need to factory reset your computer and those notes will come in handy.

Once you have the app running, check that everything is functioning like it does in development or production. You should see the same behavior across all of the environments until people start pushing changes.

## Know the testing process

![Image](https://www.freecodecamp.org/news/content/images/2020/05/testing.png)

There are many different forms of testing that your app can go through and you need to know how that process works. Unit tests are common in most projects to some degree so always check for those. Some companies do integration testing to make sure no breaking changes sneak into the build or deploy pipelines.

Other places even have dedicated software testers that will run through user scenarios to see how things will work when real users see the updates. You need to be aware of all the steps your app will go through.

When you start this new project, looking at the tests can give you a good idea of how the app works. If there aren't any tests in the project then this is your chance to start adding them. Having some code coverage sets the tone for the app in the future that there should probably be more tests added as the code developed.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import Items from '../src/components/Items';
import CreateItemModal from '../src/components/CreateItemModal';

configure({ adapter: new Adapter() });
jest.mock('../__mocks__/getAllItemsMockRequest.js');

describe('Items component works', () => {
    it('Items renders without crashing', () => {
        const div = document.createElement('div');
        ReactDOM.render(<Items />, div);
        ReactDOM.unmountComponentAtNode(div);
    });

    it('should toggle CreateItemModal', () => {
        const div = document.createElement('div');
        const ItemComponent = shallow(<Items />, div);
        ItemComponent.find('#add-item-icon').simulate('click');
        expect(ItemComponent.contains(<CreateItemModal />)).toBe(true);
        ReactDOM.unmountComponentAtNode(div);
    });
});
```

Working with software testers is usually a more involved process. There's typically some kind of system in place like Jira or Basecamp where bugs and features can be discussed and tracked through sprints. Follow the process they have in place and it'll help get your code to the deploy phase faster and more consistently.

## Know the deploy process

![Image](https://www.freecodecamp.org/news/content/images/2020/05/deploy-process.png)

Although cloud services have just about taken over the hosting needs for most companies, you might still need to work with a physical server. Having this information will help you understand the deploy strategy you will be working with.

Is there a continuous build/deploy process in place or will you need to do manual deploys from your machine? Know how migrations should be handled across the different environments. Get all of the common parts of deploying an app clarified for this particular app.

Little wonky things happen with the cloud services that only the people who handled the deploys before know about so make sure you ask if there is any weird behavior you should look out for. Since you've already fixed a small bug to check that you can push up your changes, go ahead and deploy that small fix to the development environment.

```yml
version: 2
jobs:
  build:
    docker:
      - image: circleci/<language>:<version TAG>
    steps:
      - checkout
      - run: <command>
  test:
    docker:
      - image: circleci/<language>:<version TAG>
    steps:
      - checkout
      - run: <command>
workflows:
  version: 2
  build_and_test:
    jobs:
      - build
      - test
```

This is your test to see if you really understand how the deploys will work. Hopefully you won't have to do many manual deploys and you'll work with CI/CD pipelines so the process will stay consistent.

## Know who you can turn to for different parts of the project

![Image](https://www.freecodecamp.org/news/content/images/2020/05/team.png)

Unless you are responsible for the entire application from the front-end all the way to the database, there are probably other people who cover parts of the code or system you'll never touch. It's important to know who those people are so you know who to turn with questions.

Plus this is a great way to get to know other teams that work on the project and learn what they do. If it's just you working on every part of a project, make sure that you get every login credential that you can because it'll be up to you to answer all the questions.

## Know which third-party services the project uses

![Image](https://www.freecodecamp.org/news/content/images/2020/05/third-party.png)

When you start debugging issues, knowing where to turn for documentation is the fastest way to fix things. That means knowing what services the application uses and where they're used. One way to find this is to check the _package.json_ or _App.config_ file of your project to see what's installed.

```json
{
    "name": "dog-finder",
    "version": "0.1.0",
    "scripts": {
        "build": "npm install",
        "start": "npm run build && concurrently --kill-others \"node ./server.js\" \"http-server\""
    },
    "dependencies": {
        "concurrently": "^5.1.0",
        "cors": "^2.8.5",
        "express": "^4.17.1",
        "johnny-five": "^1.4.0",
        "path": "^0.12.7"
    }
}

```

This will help you sort out a lot of issues that come up in production and it'll help you ask better questions. You'll also need credentials for most services so that will likely come up when you try to run the project the first time. 

A few big advantages to looking at the third-party services early are to learn about any version compatibility changes and any known issues.

A common complaint you'll run into on older projects is that the app doesn't work the way it used to and no one knows why. Looking at these services is a quick and easy place to start looking while you get ready to take over.

## Know the best way to get in touch with the decision makers

![Image](https://www.freecodecamp.org/news/content/images/2020/05/decision-maker.png)

Even though you are taking over the primary development of a project, there will still be someone like a project manager that will guide the tasks you work on. Get their contact information as soon as you get approval to start on the project. This is one of the people that will be able to get your high level questions answered.

If you're working with a smaller company it would also be good to have the contact info of someone like the CEO or CTO because they will be able to give you a direct yes or no on many of the questions you have. 

For example, if you've researched a new database service that will decrease their bill by 10% and increase the overall performance of the app, you want to know if you can make those changes or not.

Learn who the people are that can give you approval or guidance for the next steps you take and then save their emails and phone numbers.

One instance this is especially crucial is if there's a fire in production. When you can get those quick decisions immediately, that can save a company thousands of dollars so they will understand if you call them.

## Know what your timeline is

![Image](https://www.freecodecamp.org/news/content/images/2020/05/timeline.png)

Sometimes it's so easy to get wrapped up in the minute details that when a timeline is thrown out, agreeing makes sense. 

Before you fully commit to any length of work, make sure that you've done a proper evaluation of what you are being asked to do with the resources you're provided. Do a quick code sweep to get an idea of what you'll be working with and see how long it takes for people to respond to your initial questions.

That way when you are given a deadline you can explain why it is or isn't reasonable for the amount of work being asked. You always want to give realistic estimates on so that your client or project manager doesn't get other people's hopes up. It's better to tell them upfront if something will take longer or not as long as they expect.

When you have reasonable expectations, it makes the whole project flow better for everyone. There aren't as many panicked sessions of coding and you are able to deliver quality code that won't have to be debugged in production.

## Know what the scope of your work is

![Image](https://www.freecodecamp.org/news/content/images/2020/05/scope.png)

The scope of projects tends to slowly expand as you make progress. You start getting a little feedback here and there about "little tweaks" that should be made. Then it turns into a question of what takes priority over what and it's not the original work you started with.

One way to prevent scope creep is to agree on a set list of tasks or a specific functionality that needs to be implemented. Anything else can be written down and brought up in another part of the project work, but not right now. 

Once the work has been agreed on, then there should be a clear finish state that the project will be in at the end.

## Final Thoughts

Taking over an existing project is a special skill because it's not something you do all the time. Some people work on one product or product line for a bulk of their career, so setting up new projects only happens every now and then.

Although if you ever do consulting or freelance work, you'll need to know how to do this with confidence on a regular basis. Usually there are small configuration changes that you have to figure out and once you set them you never have to worry about them again.

These are just a few things I try to check for when I'm setting up a new project. Some of these tips apply to open source projects as well. Do you have anything you always check for when you're getting set up?

---

I write about other random stuff in tech too, like air guitars and VR. You should follow me on [Twitter](https://twitter.com/FlippedCoding) to learn about that cool stuff.

