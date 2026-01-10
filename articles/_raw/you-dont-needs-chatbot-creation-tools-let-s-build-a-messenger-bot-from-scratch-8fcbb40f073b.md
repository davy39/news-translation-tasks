---
title: You don’t need chatbot creation tools — Let’s build a Messenger bot from scratch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T08:08:41.000Z'
originalURL: https://freecodecamp.org/news/you-dont-needs-chatbot-creation-tools-let-s-build-a-messenger-bot-from-scratch-8fcbb40f073b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eEi9foMd0qRFROy-B8UO6Q.jpeg
tags:
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Daoud Clarke

  There are many many chatbot creation tools out there. To paraphrase Dr. Seuss, some
  are good and some are sad and some are very, very bad. I know, I’ve reviewed a bunch
  of them.

  But what if you want to write one yourself, from scratch...'
---

By Daoud Clarke

There are many many chatbot creation tools out there. To paraphrase Dr. Seuss, some are good and some are sad and some are very, very bad. I know, I’ve [reviewed](https://chatbottech.io/) a bunch of them.

But what if you want to write one yourself, from scratch, without using any fancy tools? Is that even possible? And can you make something useful? The answer is yes, because I’ve done it, and I’m going to show you how.

All the code is available [here](https://github.com/daoudclarke/chatbot-from-scratch) on Github. We will be creating a bot for Facebook Messenger, and we will use Google App Engine to host our bot, which will be written in Python.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NVfzXyBPKYGaNqHk2f208w.jpeg)
_I happen to know a thing or two about chatbots. Photo by [Unsplash](https://unsplash.com/photos/KesWZ9GyJ5k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Scott Webb</a> on <a href="https://unsplash.com/search/photos/dr-seuss?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

But wait, why would you want to do this? Using a graphical user interface to make your bot is much easier. Well, here are a few reasons:

* It’s free. App Engine’s [free tier](https://cloud.google.com/free/docs/always-free-usage-limits#gae_name) is so generous it’s unlikely you will exceed it unless you have many thousands of bot users — in which case, you’ll be laughing.
* To learn. See what it really takes to build a chatbot.
* Go beyond what the chatbot creation tools can do. Feeling ambitious? Make something totally original, or make your [own](http://daoudclarke.github.io/chatbots/2018/02/06/manifesto-for-a-new-chatbot-platform) chatbot platform.

### Choosing a chatbot channel

You can build a bot for many different channels. Some of the most popular are Facebook Messenger, Kik, Slack, Twitter, and Telegram. If you need to support several platforms, you’ll be better off using a bot framework. This way you won’t have to write the code to integrate with all the platforms you want to support.

In this article we’re going to build a chatbot for Facebook Messenger. Why? Well, firstly, it’s the most popular platform for chatbots. Nearly all the tools for building chatbots target Messenger, and quite a few of them _only_ support Messenger. And with good reason: it had 1.2 billion monthly active users in 2017. That’s a lot of potential chatbot users.

There’s another reason we want to target Messenger: quick replies. These are buttons that your chatbot can offer users as a shortcut so they don’t have to type. Not only do they make your bot much more engaging (who likes typing on a mobile phone?), but they also make your job as a chatbot developer a whole lot easier.

If you offer users buttons, they’ll press those buttons. This means you don’t have to worry about parsing arbitrary queries from users who want to know whether it’s going to rain tomorrow or where they can get pizza. Guiding users is good for them and us.

### What’s a bot to do?

![Image](https://cdn-media-1.freecodecamp.org/images/1*e0z56Y8J_p8KcfaFYS6rvA.jpeg)
_None shall pass. Well, mostly none. Photo by [Unsplash](https://unsplash.com/photos/wdtF-f4qBdU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jeremy Dorrough</a> on <a href="https://unsplash.com/search/photos/visa?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Your bot needs a purpose. It can’t do everything. My friend [Naré Vardanyan](https://www.linkedin.com/in/narevardanyan/) and I designed a bot to help people navigate the turbid waters of visa applications to the UK. We’ll be using a simplified version of that bot as an example in this article.

### Tree Traversal Magic

![Image](https://cdn-media-1.freecodecamp.org/images/1*xkhS6RGZ1D7OhYdsC64IQA.jpeg)
_Not this kind of tree. Photo by [Unsplash](https://unsplash.com/photos/zThTy8rPPsY?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Adarsh Kummur</a> on <a href="https://unsplash.com/search/photos/tree?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

We’ll be using a bot design method based around [**trees**](https://en.wikipedia.org/wiki/Tree_(data_structure)). Each node of the tree represents a possible conversation state. Each child of a node corresponds to a possible user message that we understand as being relevant from this particular state.

```yaml
say: "What is the purpose of your visit? (options: travel, study, business/work, medical treatment, join family/get married, visit child at school, diplomatic/government visit)"
answers:
  travel:
    say: You need a Standard Visitor Visa
  study:
    say: How long are you going to stay in the UK? up to 6 months; more than 6 months
    answers:
      up to 6 months:
        say: You can apply for a Short-term Study Visa
      more than 6 months:
        say: You need a Study Visa (Tier 4)
  business/work:
    say: How long are you going to stay in the UK? up to 6 months; more than 6 months
    answers:
      up to 6 months:
        say: You need a Standard Visitor Visa
      more than 6 months:
        say: Are you an 1. entrepreneur 2.investor 3. leader in arts or sciences 4. none of the above
        answers:
          '1':
            say: You can apply for a Tier 1 Entrepreneur
          '2':
            say: You can apply for Tier 1 Investor
          '3':
            say: You can apply for Tier 1 (Exceptional Talent)
          '4':
            say: Are you offered  1. a skilled job 2. role in the UK branch of your employer 3. job in a religious community 4. job as an elite sportsman or coach
            answers:
              '1':
                say: You can apply for a Tier 2 (General) visa
              '2':
                say: You can apply for a Tier 2 (Intra-company transfer)
              '3':
                say: Tier 2 (Minister of Religion)
              '4':
                say: Tier 2 (Sportsperson)
  medical treatment:
    say: You need a Standard Visitor Visa
  join family/get married:
    say: You need a Family of a settled person visa if your family/partner are settled in the UK or a 'dependant' visa of their visa category if they are working or studying
  visiting a child:
    say: You need a Parent visa if you're visiting for over 6 months and a Standard Visitor visa if your visit is  for less than 6 months
  diplomatic or government visit:
    say: You can apply for exempt vignette (exempt from immigration control)
```

This is a simplified version of our visa advice bot, in tree form. It’s in YAML (Yet Another Markup Language) format, which makes it easy to read. The root node specifies the first message the bot sends to the user, in this case, asking the user “What is the purpose of your visit?” The child nodes (specified under “answers”) contain the possible answers we will accept, namely “travel,” “study,” “business/work,” and so on.

### Getting started

To create our bot, we need to set up a bunch of things in Facebook. The official [instructions are here](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup), but in summary, you will need:

* A Facebook page — each bot needs a different Facebook page.
* A developer account to allow you to create apps.
* A Facebook app to get a secret access token which will be needed later.

Facebook bots work with **webhooks**, which are just URLs that Facebook Messenger uses to interact with your bot.

To create our webhook, we’ll use [Google App Engine](https://cloud.google.com/appengine/). The advantage of this is that it’s free for low volumes, and automatically scales as you get more traffic. For this article, I’ve used Python, but there are lots of other languages you can use. You will need to [download the Python SDK](https://cloud.google.com/appengine/docs/standard/python/download) and [create a Google Cloud Project](https://console.cloud.google.com/project) if you don’t already have one.

### Creating our webhook

![Image](https://cdn-media-1.freecodecamp.org/images/1*wvmnYETqWUowkuP5Y2jQPA.jpeg)
_Hooked? Photo by [Unsplash](https://unsplash.com/photos/TRggaD8mHJ4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Fabien Bazanegue</a> on <a href="https://unsplash.com/search/photos/hook?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

The first thing our webhook needs to do is to allow Facebook to verify that we are really the correct webhook. We do that by handling a GET request which contains a “verify token.” This is a secret random string that we’ve shared with Facebook. This part of our code is based on the excellent Facebook Messenger Bot [repository](https://github.com/hartleybrody/fb-messenger-bot).

```py
class MainPage(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        super(MainPage, self).__init__(request, response)
        logging.info("Initialising with new bot.")
        self.bot = TreeBot(send_message, UserEventsDao(), TREE)

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        mode = self.request.get("hub.mode")
        if mode == "subscribe":
            challenge = self.request.get("hub.challenge")
            verify_token = self.request.get("hub.verify_token")
            if verify_token == VERIFY_TOKEN:
                self.response.write(challenge)
        else:
            self.response.write("Ok")
```

Here we first initialize a class to handle requests within the [webapp2 framework](https://webapp2.readthedocs.io/en/latest/). We first log a message to say that the bot is being initialized, then construct the class `TreeBot` that will handle all the bot logic, discussed below.

Next we check for “subscribe” requests from Facebook and check that the verify token sent in the request is the same as the secret one we shared with Facebook.

### Handling messages from users

Next we need to interpret messages from users, which are sent by Facebook to our webhook using POST requests.

```py
    def post(self):
        data = json.loads(self.request.body)
        logging.info("Got data: %r", data)

        if data["object"] == "page":

            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    sender_id = messaging_event["sender"]["id"]

                    if messaging_event.get("message"):
                        message = messaging_event['message']
                        if message.get('is_echo'):
                            logging.info("Ignoring echo event: " + message.get('text', ''))
                            continue
                        message_text = messaging_event['message'].get('text', '')
                        logging.info("Got a message: %s", message_text)
                        self.bot.handle(sender_id, message_text)

                    if messaging_event.get("postback"):
                        payload = messaging_event['postback']['payload']
                        self.bot.handle(sender_id, payload)
                        logging.info("Post-back")
```

Here we first parse the JSON data from Facebook and log it to help with debugging. We then iterate over the messaging events in the data. First we extract the sender ID, which we’ll need to send replies back to the user. There are two types of events, messages (which the user has typed) and “postback” events, which are sent when a user clicks a quick reply button.

For the first of these, we need to ignore “echo” events. We then extract the message text and send it to our bot logic to handle. We do the same with the postback events, extracting the payload, which in our case is just the text of the button.

### Sending messages to users

![Image](https://cdn-media-1.freecodecamp.org/images/1*JYGEBAIYB9j-gkfy7iijQg.jpeg)
_Messages from users don’t come in bottles. Photo by [Unsplash](https://unsplash.com/photos/ssoJQfH7Acw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Scott Van Hoy</a> on <a href="https://unsplash.com/search/photos/message-in-a-bottle?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

When we constructed our `TreeBot` class, we passed a function `send_message` that allows the bot logic to send return messages to the user. Here it is:

```py
def send_message(recipient_id, message_text, possible_answers):
    logging.info("Sending message to %r: %s", recipient_id, message_text)
    headers = {
        "Content-Type": "application/json"
    }
    message = get_postback_buttons_message(message_text, possible_answers)
    if message is None:
        message = {"text": message_text}

    raw_data = {
        "recipient": {
            "id": recipient_id
        },
        "message": message
    }
    data = json.dumps(raw_data)
    r = urlfetch.fetch("https://graph.facebook.com/v2.6/me/messages?access_token=%s" % ACCESS_TOKEN,
                       method=urlfetch.POST, headers=headers, payload=data)
    if r.status_code != 200:
        logging.error("Error sending message: %r", r.status_code)


def get_postback_buttons_message(message_text, possible_answers):
    if possible_answers is not None and len(possible_answers) <= 3:
        buttons = []
        for answer in possible_answers:
            if len(answer) > 20:
                return None
            buttons.append({
                "type": "postback",
                "title": answer,
                "payload": answer,
            })
        return {
            "attachment": {
                "type":"template",
                "payload": {
                    "template_type": "button",
                    "text": message_text,
                    "buttons": buttons,
                }
            }
        }
    return None
```

The recipient ID will be the sender ID we extracted earlier. Along with that we have the message text, and some quick reply buttons for the user to press. We first make sure that the request headers specify our content as JSON, and then construct our postback buttons part of the message. We specify the recipient ID and message text and convert to JSON. We make our request to the Facebook Graph API, passing in the secret access token that Facebook gave us when we created our app.

### Running the bot server

The last piece of code in this file just constructs the main class and runs it:

```py
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
```

### Bot brains

![Image](https://cdn-media-1.freecodecamp.org/images/1*HFJOSbIDPjI3SW8Jx4a4Zg.jpeg)
_Not a brain, but looks like one. Photo by [Unsplash](https://unsplash.com/photos/ZEpxoNzKfcc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Vlad Tchompalov</a> on <a href="https://unsplash.com/search/photos/brain?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Now we come to the interesting bit: how does the bot know what to say? The brains of the bot are in the file `bot.py`.

```py
class TreeBot(object):
    def __init__(self, send_callback, users_dao, tree):
        self.send_callback = send_callback
        self.users_dao = users_dao
        self.tree = tree

    def handle(self, user, message):
        self.users_dao.add_user_event(user, 'received', message)
        history = self.users_dao.get_user_events(user)
        tree = self.tree
        logging.debug("History items: %d", len(history))
        restarting = False
        nothing_sent = True
        response = DEFAULT
        possible_answers = DEFAULT_POSSIBLE_ANSWERS
        for direction, content in history:
            response = DEFAULT
            possible_answers = DEFAULT_POSSIBLE_ANSWERS
            if direction == 'received':
                key = get_content_match(content, tree)
                if nothing_sent:
                    response = tree['say']
                    possible_answers = tree['answers'].keys()
                elif key is not None:
                    tree = tree[key]
                    if 'say' in tree:
                        response = tree['say']
                        possible_answers = None
                        if 'answers' in tree:
                            possible_answers = tree['answers'].keys()
                    restarting = False
                elif restarting:
                    if content == 'yes':
                        tree = self.tree
                        response = tree['say']
                        possible_answers = tree['answers'].keys()
                        restarting = False
            elif direction == 'sent':
                nothing_sent = False
                if 'answers' in tree and direction == 'sent' and content == tree.get('say'):
                    tree = tree['answers']
                elif direction == 'sent' and content == DEFAULT:
                    restarting = True
            else:
                raise ValueError("Unexpected direction: " + direction)

        logging.debug("Responding: %s", response)

        self.send_callback(user, response, possible_answers)
        self.users_dao.add_user_event(user, 'sent', response)
```

The class is initialized with three parameters:

* a callback function (that was defined above) to send messages back to users
* a data access object for storing information about users
* the tree that contains the logic of what should be said when. This is parsed from the YAML we showed above.

First, we record that we received the user’s message, and then retrieve all of the user’s past actions from the data access object. We then replay the user’s actions to figure out where they are currently in the tree.

We initialize the response to a default message that will be returned when the user says something we don’t understand. In our case, this is “I’m sorry, I didn’t understand, shall we start again?” There are also some default possible answers, which are “yes” and “no”. We also keep a record of whether we think we are restarting the conversation from scratch.

We then start iterating over the user’s history. For each message, we check whether it was sent by us, or whether we received it from the user. If it was received, we check for a match with the current options in the tree. This uses the following function:

```py
def get_content_match(content, tree):
    matches = []
    for key in sorted(tree):
        if content.lower() in key.lower():
            matches.append(key)
    if len(matches) == 1:
        return matches[0]
```

This checks the content of the user’s message to see if it occurs as a substring of one of the current options in the tree. If there is exactly a single match, we return that match, otherwise either the user’s response is ambiguous or there is no match at all.

Next we check whether we have sent anything at all to the user before. If not, we set our response to be the first response in the tree, and set the possible answers to the first set from the tree.

Then we check whether we found a match for the user’s message. If we did, we update the tree to be the appropriate child branch, and extract the correct response and possible answers from the tree.

We then check if we have suggested restarting and if the user has confirmed they do want to restart the conversation. In that case, we reset the tree back to its initial state and use the first response as we did before.

For each message in the history that was sent by the bot, we update the tree accordingly. Or if we sent the default message, record that we may restart the conversation.

Finally, after traversing all the history, we log our response, send the message back to the user, and record the message we sent in our data access object.

### The last piece of the puzzle

![Image](https://cdn-media-1.freecodecamp.org/images/1*a5N4vokpfnlmUnnJMou9zw.jpeg)
_Writing a chatbot is easier than doing this puzzle. Photo by [Unsplash](https://unsplash.com/photos/3y1zF4hIPCg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Hans-Peter Gauster</a> on <a href="https://unsplash.com/search/photos/puzzle?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

The only piece of code left to discuss is the data access object that stores all user interactions. We made the design decision to store all user actions and replay them as we did above because it allowed us to easily change the logic of the bot and still be able to deduce an appropriate state for the bot and the user. If we had chosen instead to label each node of the tree and store that label, then any change to the tree would render old conversations invalid.

So our data access object needs to be able to do two things: store a new user event, and retrieve all the events for a particular user.

```py
class UserEvent(ndb.Model):
    user = ndb.StringProperty()
    direction = ndb.StringProperty()
    message = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class UserEventsDao(object):
    def add_user_event(self, user, direction, message):
        event = UserEvent()
        event.user = user
        event.direction = direction
        event.message = message
        logging.info("Adding event: %r", event)
        event.put()

    def get_user_events(self, user):
        events = UserEvent.query(UserEvent.user == user)
        sorted_events = sorted(events, key=lambda x: x.date)
        return [(event.direction, event.message) for event in sorted_events]
```

Our data access object makes use of [Google Datastore](https://cloud.google.com/datastore/docs/concepts/overview), which is very easy to use from App Engine, and has a generous free usage tier. The Python API makes using Datastore very easy. First we create a model class, `UserEvent` which specifies the fields and their types. In our case, the user ID, direction of the message and the message itself are strings, and finally the date of the event has a date-time type.

To create and store a new user event, we simply construct this class, set the properties, and then call `put()` on the object.

To retrieve the events for user, we call the `query()` function on the class, passing in the user ID. We then sort the events by date, and return a list of direction-message pairs.

### Deployment

That’s all the bits of our bot! Now to deploy it and connect it up to Messenger.

To deploy your app to App Engine, use the `gcloud` command that came with the App Engine SDK:

```
gcloud app deploy --project [YOUR_PROJECT_ID]
```

Once deployed, the URL of your webhook is

```
http://[YOUR_PROJECT_ID].appspot.com/
```

Update your Facebook app with this webhook URL (follow the instructions [here](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup)) and you should be good to go!

### The world is your chatbot oyster

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-NZf2K93B_GCI71CR5jjA.jpeg)
_Oysters are tasty but chatbots are fun. Photo by [Unsplash](https://unsplash.com/photos/p4-LAfM9yAg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Charlotte Coneybeer</a> on <a href="https://unsplash.com/search/photos/oyster?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

You can make many kinds of chatbot using these techniques. I once had fun making a [_Choose Your Own Adventure_](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) style bot, but I’m sure you’ll be able to come up with much more inventive things. Oh, and if you want to try out the visa bot, you can try it [here](https://www.facebook.com/harveyaibot/) (although this version is a little more sophisticated).

And, if you don’t fancy all this hard work, you could always try one of the many chatbot creation [tools](https://chatbottech.io/).

