---
title: How user feedback improved my app’s security
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T18:37:46.000Z'
originalURL: https://freecodecamp.org/news/how-user-feedback-improved-my-apps-security-53eb11977880
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Sk4M13Bb8Sh3P1VL.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ethan Ryan

  Getting published on freeCodeCamp’s Medium publication was super exciting.

  The week my post was accepted, I was busy with work and headed out of town for the
  weekend, so I didn’t get a chance to check Medium for a few days. I’d gotten s...'
---

By Ethan Ryan

Getting published on [freeCodeCamp’s Medium publication](https://medium.freecodecamp.org/) was super exciting.

The week [my post](https://medium.freecodecamp.org/how-to-surprise-your-apps-users-by-hiding-easter-eggs-in-the-console-3b6e9285e7e7) was accepted, I was busy with work and headed out of town for the weekend, so I didn’t get a chance to check Medium for a few days. I’d gotten some email notifications, and was excited to catch up on the responses to [my piece](https://medium.freecodecamp.org/how-to-surprise-your-apps-users-by-hiding-easter-eggs-in-the-console-3b6e9285e7e7) when I got a chance.

![Image](https://cdn-media-1.freecodecamp.org/images/v0ypDXKM2V2tnU70O6qrejSXM9DEd0b3UhWF)
_Medium notifications_

Nice! That big green circle meant claps! New followers! People reading my words and checking out my story generator app! This was awesome!

Then I read the messages.

![Image](https://cdn-media-1.freecodecamp.org/images/7JVfMXKsZ6pCZ7TGtm-h1-5dJEUQemMqBpL0)
_comment one_

Uh-oh spaghetti-os.

![Image](https://cdn-media-1.freecodecamp.org/images/lrcyUuw6DTmxBiTOr7jMrcnBKOHm6ExjIRHE)
_comment two_

No bueno.

![Image](https://cdn-media-1.freecodecamp.org/images/a-ofyiUOaAunD3bHVbuYm9bzinFfvHzodIBw)
_comment 3_

Hmm, makes sense.

![Image](https://cdn-media-1.freecodecamp.org/images/RFAm14hs1xKedDqRWmGVCEcU2sTq0MPrvUHZ)
_comment 4_

Yikes!

Truth be told, I’d never checked out the Network tab in Chrome’s developer tools ¯\_(ツ)_/¯.

I spend tons of time in the console of the browser, reading my logs and warnings and errors, but not much time with the other Developer Tools options.

Those comments were super helpful, and made me realize I had work to do.

To summarize thus far:

* **Good news:** [WordNerds](http://wordnerds.co) was getting some new users! :)
* **Bad news:** Bad guys could still see a list of all my users, and their email addresses :/

All anyone had to do to find all my users’s email addresses was go to wordnerds.co, open the console, click on Networking, and go to: [https://word-nerds-api.herokuapp.com/users](https://word-nerds-api.herokuapp.com/users)

They’d see this:

![Image](https://cdn-media-1.freecodecamp.org/images/01-PJrx5GmmzwYfkteS8-BY9vOgM5Bl0b7fx)
_WordNerd’s /users API endpoint_

> Note: My first few users didn’t have email addresses stored in the database because they signed up for WordNerds before I made email addresses required attributes via frontend authentication.

Scrolling through that API endpoint, I also noticed another problem that needed to be fixed:

![Image](https://cdn-media-1.freecodecamp.org/images/MNjse84v41BnzDGf-j4zifMguGqc7K4lvDTf)
_lorem ipsum username_

Oops. My username attribute didn’t have any string length limit. Or if it did, that limit was too damn high. Nobody’s username needs to be that long.

For example:

![Image](https://cdn-media-1.freecodecamp.org/images/bLLS-ev9iBj7Puum5QGlvMUXEEb1DPwl0oAw)
_Navy Seal Copypasta username, profanity blurred_

Jeez Louise. How would anyone remember to paste in [the Navy Seal Copypasta](https://knowyourmeme.com/memes/navy-seal-copypasta) in order to sign into WordNerds?!

What a hassle. I didn’t want to give my users a bad user experience, expecting them to remember to copy and paste all that copypasta.

Username input fields are like children: they crave limits.

So I had some work to do.

1. I had to protect my user’s email addresses. _Again_. I thought I’d fixed that last time, but boy was I wrong.
2. I had to limit how many characters a username could be.
3. As my helpful commenters had pointed out, I should only be retrieving the absolutely necessary data from the backend from each API endpoint. I was returning too much data, which was bad for both security and performance reasons. I had to protect my user data **and** limit the amount of data being returned for each API call.

Cool cool cool. Work work work. Time to get to work.

#### Protecting user data

My first and most pressing issue: making sure I wasn’t logging all my users names and email addresses to my /users API endpoint as JSON.

There were multiple ways to fix this, and after some thought I decide upon the most obvious, easiest approach, so obvious and easy I was surprised I didn’t realize it sooner. I had no need at all for an API endpoint for all users. So I could simply delete that API call from the frontend, and the corresponding Rails method on the backend.

I did like showing the total number of users in my app’s Metadata component, though. It was just a simple number, but I liked watching it slowly grow in size as more people signed up on my site.

So I decided to keep that number, **and** eliminate all that user data showing up on the API endpoint.

I kept the API call exactly the same on the frontend, and on the Ruby on Rails backend, I changed the index method in the UserController from this:

```
def index   users = User.all   render json: usersend
```

to this:

```
def index   users = User.all.size   render json: usersend
```

> Note: I could have used `length` or `count` instead of `size`, but `size` is the best bet according to [this StackOverflow post](https://stackoverflow.com/questions/14794492/which-is-faster-count-or-length).

Now instead of returning an array full of user objects, containing usernames and email addresses, my backend is instead simply returning a number.

### BEFORE:

![Image](https://cdn-media-1.freecodecamp.org/images/pgjW8cW1-EJkFlQ9Sitdmltrf-nbaaJ55L-f)
_/users API endpoint — BEFORE_

### AFTER:

![Image](https://cdn-media-1.freecodecamp.org/images/CSVl2iG9jXMEA9KXbD2Hl-sXlWnNVAdKO8Fk)
_/users API endpoint — AFTER_

Whoa! What an amazing transformation!

After that change to the backend, I had some minor changes to the frontend. Instead of rendering `props.users.length` in my Metadata component, I could simply render `props.users`. And I could change that name in the container state from `this.state.users` to `this.state.userCount`. Easy updates.

No more user data in my publicly accessible API endpoint!

Well, my usernames and email addresses where still accessibly via the /stories endpoint, so I still had that to fix. But that could be dealt with soon.

#### Limiting username length

I didn’t like seeing that a username could be as long as the Navy Seal Copypasta, and although it’s nutso that someone would even try making their name that long, I’m glad they did, because now I could fix that issue!

Thank you, whoever made your WordNerds username crazy long. I’m looking at you, Lorem Ipsum and Navy Seal Copypasta.

I already had some validations on my frontend to make sure that users logging in or signing up for WordNerds had usernames and passwords that were not empty.

My SignUpForm is a stateful component that called validate in my render function, as well as in my canBeSubmitted function.

I got that validate function from [this freeCodeCamp blog post](https://medium.freecodecamp.org/how-to-use-reacts-controlled-inputs-for-instant-form-field-validation-b1c7b033527e), probably about a year ago.

My original validate function looked like this:

```
validate(name, password) {   return {      name: name.length === 0, //true if username is empty      password: password.length === 0 //true if password is empty   }}
```

I decided to refactored this function, making it less succinct, but also more clear, so current and future me will understand it:

```
validateFormInputs(name, password) {   let nameIsInvalid = (name.length === 0) //true if empty   let passwordIsInvalid = (password.length === 0) //true if empty   let errorObject = {      name: nameIsInvalid,      password: passwordIsInvalid   }   return errorObject}
```

I can hear some of you groaning, “Ugg, you made that succinct function so long and ugly! You added variable names for no reason!”

Sure, I’m adding some lines here, but to me, I can now understand more quickly what is happening in this function.

Now I simply add some more conditions to be met. Apart of a valid username not being empty, I’m also validating that it cannot be longer than 15 characters.

I choose the number 15 because that’s what [Twitter allows for its usernames](https://help.twitter.com/en/managing-your-account/twitter-username-rules), and if it’s good enough for Twitter, it’s good enough for WordNerds.

With my new condition for usernames, my function looks like this:

```
validateFormInputs(name, password) {   let nameIsInvalid = (name.length < 2 || name.length > 15)   let passwordIsInvalid = (password.length === 0)   let errorObject = {      name: nameIsInvalid,      password: passwordIsInvalid   }   return errorObject}
```

Nice! Now the Navy Seal Copypasta can now longer be used as a username on WordNerds.

Sorry copypasta fans! Gotta keep your usernames at or under 15 characters from here on in.

![Image](https://cdn-media-1.freecodecamp.org/images/TA0dzPY0YYqljqaX3ATdn0Wg4niTczfDqEh6)
_invalid name if more than 15 characters_

I realized it was good practice to not allow spaces in usernames either. “Bob Smith” would be a bad username, as would “ ”. I considered adding a simple regex to my function, when I learned about the [input pattern attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#Attributes) in HTML5. Cool! No need to add anything to my function, I could simply update my JSX form field for the username.

My React frontend’s username form field now looks this:

![Image](https://cdn-media-1.freecodecamp.org/images/ofzGmtUNes-oQwFIrGsH2fuEzujDUJMTLABj)
_LoginForm username form field_

Which results in this alert in the browser:

![Image](https://cdn-media-1.freecodecamp.org/images/tVyjswWUpBxtn15mInmg1jAh7lWKCPtHDi6y)
_bad name alert_

I made similar updates to my SignUpForm as I did to my LoginForm, and included some validations for email addresses.

Sweet, now I just had to make sure there weren’t any email addresses being made visible in my /stories API endpoint. To the backend!

#### Limiting data returned for each API call

Blah blah blah, a bunch of stuff on the backend.

I didn’t do a good job or writing this stuff down cuz I was trying to get it done quickly, and when that failed, I was trying to get it done.

I’m continuing to think of ways to improve what data is returned from my API endpoints, to make my app both more secure and more scalable.

But to summarize, no more email addresses being made visible in my /stories API endpoint!

Now each story has a `user_name` attribute, in addition to a `user_id` attribute, but no more email addresses are accessible via the API.

The argument could be made that I’m still exposing my app’s users’ usernames, and that I shouldn’t be doing that. But I’m treating those usernames as public info. Users can choose their usernames, so it’s up to them how revealing they want to be in their username choice. It could be RichAt123FakeSt, or it could be batman6669. Who am I to judge what my app’s users choose as their usernames? It’s not like I’m revealing their extremely personal email addresses or anything! I mean, not anymore.

### Conclusion: Feedback is good

After making those security updates, I made a few more fun changes as well. It’s fun to continually be improving my app, thanks to helpful feedback from internet strangers, as well as whatever zany feature I think will make it better.

Check out WordNerds here, at [WordNerds.co](http://wordnerds.co).

Thanks for reading, nerds!

Till next time.

