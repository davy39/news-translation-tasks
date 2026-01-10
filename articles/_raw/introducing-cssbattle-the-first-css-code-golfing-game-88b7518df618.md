---
title: Introducing CSSBattle — the first CSS code-golfing game
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T15:52:06.000Z'
originalURL: https://freecodecamp.org/news/introducing-cssbattle-the-first-css-code-golfing-game-88b7518df618
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yDgSJrVPPH70Jdh6KUyokA.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Games
  slug: games
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By kushagra gour

  If you are learning Web development or are already a professional Web developer,
  there is a very high chance you have written CSS at least once in your life. It
  is a very basic building block of any webpage. Amidst all the discussion...'
---

By kushagra gour

If you are learning Web development or are already a professional Web developer, there is a very high chance you have written CSS at least once in your life. It is a very basic building block of any webpage. Amidst all the discussions and love and hate for CSS, we present to you all — [CSSBattle](https://cssbattle.dev) ?⚔️

CSSBattle is the first ever [code-golfing](https://en.wikipedia.org/wiki/Code_golf) platform for CSS lovers that I and my friend, [Kushagra Agarwal](https://twitter.com/kushsolitary), have created. The aim of this game is simple — you have an image target which you need to replicate with the smallest possible CSS (and slight HTML if you please) code. More visual match and fewer bytes get you a higher score. And that is how you climb the leaderboards in CSSBattle. Here is an example target screen:

![Image](https://cdn-media-1.freecodecamp.org/images/1*4Qin5gKKQlk7vJPRi5rKMg.png)
_Target #9 play screen_

### Some fun stats

At the time of writing this post, it has been 10 days since we launched. And here are some fun stats we have gathered:

* 13000+ players worldwide
* Over 100K code submissions
* Minimum bytes used on a target: [just 54 bytes](https://cssbattle.dev/play/1)! ?
* A lovely [community forum](https://spectrum.chat/css-battle) of 140+ players and 40+ conversations

### Product development

We decided to build and launch CSSBattle in one month, to prevent ourselves from getting into an infinite loop of adding and polishing features. We made a list of the absolutely necessary items for launch and focused on it.

During the development, we came up with tons of new ideas to implement in the website, which we kept noting down. I am proud we could resist the urge to work on those exciting ideas and finally launch in one month!

#### Tech Stack

Our tech stack is pretty standard for today’s product. We have [React](https://reactjs.org/) (using create-react-app as a starter) on the frontend which is deployed on [Zeit Now](https://zeit.co/now). For the backend, we use [Firebase](https://firebase.google.com/). Since we both primarily have frontend/design experience, Firebase turned out to be an amazing option to easily implement everything we had on our mind while getting best in class scalability and security without managing any server!

#### The scoring algorithm

One of the most interesting things about developing CSSBattle was designing the scoring algorithm. We sat literally for days discussing and trying out various formulas. We wanted that a amore visual match should always result in a higher score. And of course, for the same match percentage, the score should increase with decreasing code bytes. Also, we wanted a faster score progression towards lower bytes once you are at 100% match, to make it more rewarding for the players who sweat it out with each removed byte.

In the end, we are happy with what we came up with. Maybe we’ll write a separate post about just the scoring algorithm :)

### The Launch

We originally planned the launch for the 5th of April, but we had to launch it a day before. We had invited many eminent CSS developers to try out CSSBattle before going public. And “fortunately” [Jonathan Snook](https://twitter.com/snookca) [tweeted about us](https://twitter.com/snookca/status/1113480096713793542?s=20) a day before we planned to launch, sending in a huge stream of developers to the game! And so we decide to prepone our launch :)

We started with the announcement on [ProductHunt](https://www.producthunt.com/posts/cssbattle) where CSSBattle was the #1 product of the day. Immediately following it was a [Reddit rush](https://www.reddit.com/r/web_design/comments/b9e23w/we_just_launched_cssbattlethe_first_ever_css/). And then, the massive and really encouraging tweet by Lea Verou:

Since then, it has been a crazy ride for us both seeing the community grow, play, learn and compete! Each day we see players breaking the limits of creativity and imagination with CSS!

### Come join us

We have a [very lovely community](https://spectrum.chat/css-battle) of superbly creative and humble developers on Spectrum where you can hang out and learn some CSS Trickery.

So, what are you waiting for? If you have ever written CSS, play now — [https://cssbattle.dev](https://cssbattle.dev)  
(We have also seen people wanting to learn CSS just to play this game!)

### ⚠️ Fair warning

CSSBattle is highly fun and [addictive](https://twitter.com/LeaVerou/status/1114422182246064128). We have seen people [losing their sleep](https://twitter.com/LeaVerou/status/1114735776766595073), [having weird dreams](https://twitter.com/alexzaworski/status/1114742512067862529), [being late to meet friends](https://twitter.com/LeaVerou/status/1114953009061072896), [cursing](https://twitter.com/kevinnewcombe/status/1113808767907295233?s=20), [skipping project deadlines](https://twitter.com/trangcongthanh/status/1114164655448924160?s=20) and [what not](https://twitter.com/hashtag/CSSBattleChallenge). Please enter at your own risk! ?

Also, we feel it’s our responsibility to highlight that apart from creative approaches, CSSBattle requires you to exploit how CSS (and HTML) is parsed by browsers. It’s important to understand that the CSS you write here is not the way you would write in a real project. The tips and tricks you learn while playing here would certainly make you better understand CSS, but always be alert and curious about what’s a hack and what is not.

Have fun CSS-ing!

