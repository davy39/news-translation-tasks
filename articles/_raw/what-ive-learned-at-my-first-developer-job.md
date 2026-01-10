---
title: I Got My First Developer Job – Here's What I've Learned So Far
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-18T00:08:02.000Z'
originalURL: https://freecodecamp.org/news/what-ive-learned-at-my-first-developer-job
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/things-learned-at-first-job-image.jpeg
tags:
- name: career advice
  slug: career-advice
- name: 'Junior developer '
  slug: junior-developer
- name: 'self-improvement '
  slug: self-improvement
seo_title: null
seo_desc: "By Leonardo Brombilla Antunes\nIn this article, I'm going to share with\
  \ you what I've learned so far at my first programming job as a junior full-stack\
  \ developer. \nEver since my developer career began in July, 2021 I've been learning\
  \ constantly. And I..."
---

By Leonardo Brombilla Antunes

In this article, I'm going to share with you what I've learned so far at my first programming job as a junior full-stack developer. 

Ever since my developer career began in July, 2021 I've been learning constantly. And I'm gonna share some tips from my experiences so that you can learn as well. 

At my company, I work on tasks end-to-end from the front-end to the back-end on a service that has a lot of users

Alright, here are the skills and tips I've taken away so far from this experience.

## Technical Skills

I've learned a lot of technical skills (what some might call "hard skills") in my first few months on the job. Here are the highlights:

### Architecture and Design Patterns

The first thing that opened my eyes was the architecture I get to work with at my job. When we are working on small projects we rarely think about the architecture – and that's okay, because we are at the beginning. 

But there's a lot to learn about the most commonly used architectural patterns (like [microservices](https://www.freecodecamp.org/news/microservices-architecture-for-humans/), the [MVC pattern](https://www.freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained/), [serverless architecture](https://www.freecodecamp.org/news/how-to-get-started-with-serverless-architecture/)...the list goes on). 

A really cool pattern that I've learned about recently is the repository pattern. This pattern will help to separate your application from your data. 

So why is this helpful? Because it lets you easily change your database technology. Look at the example below to see how it works:

```typescript
import {takeLatest, put, call, select} from 'redux-saga/effects';

import {authError, signIn, signOut, signUpSuccess} from '../actions';

import {
  signInWithEmailPasswordFirebase,
  signOutFirebase,
  signUpWithEmailPasswordFirebase,
} from '../repository';

import {
  AuthAction,
  AuthSignInInput,
  AuthSignUpInput,
  AuthTypes,
} from '../types';

import * as authSelectors from '../selectors/index';

export function* requestSignInEmailPasswordSaga(
  props: AuthAction<AuthSignInInput>,
): any {
  const email = props.payload.email;
  const password = props.payload.password;

  try {
    if (email && password) {
      const userCredentials = yield call(
        signInWithEmailPasswordFirebase,
        email,
        password,
      );

      yield put(signIn(userCredentials._user));
    }
  } catch (err: any) {
    yield put(authError('cannot sign In'));
  }
}

export function* requestSignOutSaga(): any {
  try {
    const isLogged = yield select(authSelectors.isLogged);

    if (isLogged) {
      yield call(signOutFirebase);
    }
    yield put(signOut());
  } catch {
    yield put(signOut());
  }
}

export function* requestSignUpEmailPasswordSaga(
  props: AuthAction<AuthSignUpInput>,
): any {
  const email = props.payload.email;
  const password = props.payload.password;

  try {
    if (email && password) {
      yield call(signUpWithEmailPasswordFirebase, email, password);
    }

    yield put(signUpSuccess());
  } catch (err) {
    yield put(authError('cannot sign Up'));
  }
}

export default [
  takeLatest(
    AuthTypes.REQUEST_SIGNIN_EMAIL_PASSWORD,
    requestSignInEmailPasswordSaga,
  ),
  takeLatest(AuthTypes.REQUEST_SIGNOUT, requestSignOutSaga),
  takeLatest(
    AuthTypes.REQUEST_SIGNUP_EMAIL_PASSWORD,
    requestSignUpEmailPasswordSaga,
  ),
];
```

In my sagas, I'm calling some services but I'm not doing this directly inside. I'm calling from the repository as you can see:

```typescript
import {firebase} from '@react-native-firebase/auth';

export const signUpWithEmailPasswordFirebase = async (
  email: string,
  password: string,
) => {
  return firebase
    .auth()
    .createUserWithEmailAndPassword(email, password)
    .then(user => console.log(user + 'signed Up'))
    .catch(err => {
      throw new Error(err);
    });
};

export const signOutFirebase = () => {
  firebase.auth().signOut();
};

export const signInWithEmailPasswordFirebase = async (
  email: string,
  password: string,
) => {
  return firebase
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then(user => user.user)
    .catch(err => {
      throw new Error(err);
    });
};
```

My repository is handling all contact with the Firebase service that pulls my users. If I decided that I wanted to change Firebase for any reason, I would only have to change this file and my sagas would be safe and sound. 

If, on the other hand, I decided to use any Firebase service on another part of my code, I could just call the service from the repository without passing through other places. This separation of concerns is super helpful in the long run. 

Here is the link to the whole project if you want to explore more:

%[https://github.com/LeoAntunesBrombilla/waterPlant]

And this article can help you to learn more about this pattern:

%[https://medium.com/@erickwendel/generic-repository-with-typescript-and-node-js-731c10a1b98e]

### Global State Management

When I was working on my React projects, I didn't know about global state management and Flux architecture. But I've learned that it can be an important thing to know. You can read more about it **[in this introduction to Flux architecture](https://www.freecodecamp.org/news/an-introduction-to-the-flux-architectural-pattern-674ea74775c9/).**

Redux will help you implement this architecture, but many other libraries can help you deal with Flux architecture – like Mobx, for example. If you want to understand the general idea about Redux, read [here](https://medium.com/@antunes.b.leonardo/redux-understanding-the-general-idea-cf1d8bda3f0)! You can try to learn one of these libs and build a project on top of it. 

An example would be the problem that Facebook had some years ago. This problem is better explained in the article below:

%[https://medium.com/@grover.vinayak0611/what-is-flux-architecture-why-facebook-used-it-and-the-comparison-with-mvc-architecture-49c01ed5d2e1]

### Clean Code

It's really important to deliver clean and readable code. So if you can do that then you're ahead. 

There are a lot of repositories that show best practices for each language, so you can search yours and try to write your code like that. 

Here's a simple but important example. Don't use this:

```
const a = "Leonardo"
```

What is `a`? The name of the author? The name of someone who lives in Brazil? you don't know because nobody besides the person that has created this variable will know what the context of this variable is. And after some time even the person who wrote it won't know either. 

So do something like this instead:

```
const freeCodeCampColaborator = "Leonardo"
```

Now you know the context even if I don't write any comments. And it's far easier to search for something like this when you're in a big monorepo with over 1000 files, for instance.

You can see more examples of good practices and clean code in JavaScript in the following repo:

%[https://github.com/ryanmcdermott/clean-code-javascript]

and check here for TypeScript: 

%[https://github.com/labs42io/clean-code-typescript]

### How do you learn all these skills? 

I learned these skills by building projects and asking for feedback from my co-workers. But I would suggest that, even if you don't have any co-workers, you should read some good tutorials and then try to build the projects in them. 

Make sure to use the technologies that you're trying to learn. If you just read, and don't build, you won't grasp them fully. 

I have a project with this approach if you need a more general idea of how to do it:

%[https://github.com/LeoAntunesBrombilla/projetoHitss]

## Non-Technical Skills

### Be proactive

If you're working remotely, it's often hard to show that you're being proactive and productive. If you're working in your first developer job, like I am, asking for stuff to do might sound scary – but is very rewarding when you're able to pull it off. 

Even if you can't get it done or don't understand the task, then ask for help. That's normal and super useful as well.

Here's a good example: let's say you have just finished a task and now you have to wait for a code review or something. In the meantime you can offer your help to others, talk to people other than developers to learn more about the business side, and document some environmental difficulties that you had on your first task so that others can learn by that as well.

### Learn how to ask for help

One of the skills you'll learn as a developer is how to ask better questions. Before I was a programmer I studied mathematics, and doing my bachelor's thesis I learned how to ask good questions to my advisor.

Here's one of my main tips: try to narrow your question down.

If you go with a question like: "I don't know React Native, can you help me?" What can you expect as an answer? If you don't know anything start by googling it and finding some resources on the topic.

Then you can ask your colleagues who know the tech, "Hey, I'm trying to learn React Native and found these materials – do you have any suggestions? Are they good?"

As another example, let's say that you were given a task to center a div. After some time you weren't able to do it and you want to ask someone to help you. Don't ask like this:

"Hey I was trying to center this div and I wasn't able to do it – how does it work?"

Instead, ask like this:

"Hey to center this div I've tried this method and it didn't work because of this, and then I've tried this .... and so on, so... do you have a better approach?"

On the path to asking a good question, sometimes you will find your answer. Generic and abstract questions are not so good because they make you look like you're giving up and asking for help before even trying. If you tried and still don't know the answer, then go for it – ask for help. As you gain more experience, you'll get better at asking questions.

### Stay organized

If you are not the Notion type, just take notes about what you do during your day. Create a system to remember meetings or silly things that you will probably forget if you leave them only to your memory. 

If someone asks you to do something simple, like change a description of a task from this to this and you forget because you trusted this to your already busy mind, it won't look good for you. 

So it's not only important to have an organized note system but to stick with it. This will show your team and your boss that you can get stuff done without someone watching you 24/7.

Thomas Frank's YouTube channel has lots of helpful tips for staying organized and getting things done. 

%[https://www.youtube.com/watch?v=ODXV-fb_c-I]

## Conclusion

When you're at your first developer job, you will learn a lot of stuff that is not only code-related – so be open to it. Learn to Google and ask for help!

That's it! I hope my experience helps you and happy coding :)

If you want to contact me, you can find me on [LinkedIn](https://www.linkedin.com/in/leonardo-brombilla/).






