---
title: 'YouTube Subscribe Button: How to Get People to Subscribe to Your Channel From
  a Link'
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-10-05T17:23:15.000Z'
originalURL: https://freecodecamp.org/news/youtube-subscribe-button-link
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/freeCodeCamp_org_-_YouTube-1.jpg
tags:
- name: how-to
  slug: how-to
- name: social media
  slug: social-media
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Did you know you can prompt people to subscribe when they visit your channel?

  Here is what this will look like to someone who clicks the link on a laptop or desktop
  computer:


  YouTube will show a Confirm channel subscription message.

  And don''t worry ...'
---

Did you know you can prompt people to subscribe when they visit your channel?

Here is what this will look like to someone who clicks the link on a laptop or desktop computer:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/freeCodeCamp_org_-_YouTube.jpg)
_YouTube will show a Confirm channel subscription message._

And don't worry – if someone is already a subscriber to your channel when they click this link, they will just see your channel like normal, without the subscription confirmation message.

## The Two Methods of Getting People to Subscribe to Your YouTube Channel Directly

There are two main methods you can use to accomplish this goal of getting people to subscribe to your channel directly:

1. A YouTube Subscribe link you can use anywhere – including social media sites and messaging tools.
2. A YouTube Subscribe button you can use anywhere where you can embed JavaScript, such as your personal website.

## How to Make Your Own YouTube Subscribe Link

YouTube has a feature where you can just add the `?sub_confirmation=1` parameter to your YouTube channel URL.

Again, this is perfect for linking to your YouTube channel from social media or another place where you don't have the ability to insert code for a proper subscribe button.

There are two types of channels on YouTube:

1. Channel Channels
2. Users Channels

In practice, there is no major difference between these types of channels. They each just use a slightly different URL structure.

### How to Create a Subscribe Link if Your YouTube Channel is Classified as a Channel

You can tell your channel uses the "channel" structure by visiting your channel and seeing whether it has the word "channel" in the address bar.

Here's an example:

```
https://www.youtube.com/channel/freecodecamp
```

See the word "channel" here? So in this case, you can use this structure for your link:

```
https://www.youtube.com/channel/<YOUR CHANNEL ID>?sub_confirmation=1
```

You would just replace the `<YOUR CHANNEL ID>` in this URL with your channel's ID, which you can find by going to your YouTube channel. 

It will either be a custom name (in this case, `freecodecamp`) or it will be a string of base-64 characters like this: `UC0syIz79dzjMXIf5VdJ65EA`

Once you add your channel ID to that link, you'll be good to go. The people who click that link will not only be taken to your channel, but they'll also see the subscription confirmation prompt.

### How to Create a Subscribe Link if Your YouTube Channel is Classified as a User

Some older channels are still set up as users rather than channels. You can tell your channel uses the "user" structure by visiting your channel and seeing whether it has the word "user" in the address bar.

Here's an example:

```
https://www.youtube.com/user/thenewboston
```

This channel is set up as a user.

In this case, you would use this structure:

```
https://www.youtube.com/user/<YOUR CHANNEL ID>?sub_confirmation=1
```

You would just replace the `<YOUR CHANNEL ID>` in this URL with your channel's ID. It will either be a custom name (in this case, `thenewboston`) or it will be a string of base-64 characters like this: [`UC0syIz79dzjMXIf5VdJ65EA`](https://www.youtube.com/channel/UC0syIz79dzjMXIf5VdJ65EA)

Once you add your channel ID to that link, you'll be good to go.

## How to Make Your Own YouTube Subscribe Button

All right – here is the fun part. YouTube gives you a way to embed subscribe buttons directly into your website.

Here is what one of these buttons looks like:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Configure_a_Button_-_-_YouTube_Subscribe_Button_-_-_Google_Developers.png)
_This is a static image that leads to [a subscribe prompt](https://www.youtube.com/c/freecodecamp?sub_confirmation=1)._

And here's the embed-able HTML code you would add to your blog. Note that this code will import Google's `platform.js` JavaScript library in order to dynamically show the button and your current subscriber count.

```
<script src="https://apis.google.com/js/platform.js"></script>

<div class="g-ytsubscribe" data-channelid="<YOUR CHANNEL ID>" data-layout="full" data-theme="dark" data-count="default"></div>
```

You can embed this code. Be sure to replace `<YOUR CHANNEL ID>` with the channel ID you see when you visit your page. 

If you have a custom YouTube channel URL like `https://www.youtube.com/freecodecamp` you may be able to use that as your channel ID, but I find it more reliable to use the full channel 24-character ID.

## How to Customize Your YouTube Subscribe Button

There are two other ways you can customize your subscribe button.

### How to Show Your Channel Name and Logo in your Subscribe Button

You can change `data-layout` to be either `default` or `full` (which will show your channel name and icon).

Here is what this looks like when you set `data-layout="default"`:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Configure_a_Button_-_-_YouTube_Subscribe_Button_-_-_Google_Developers-1.png)
_This is a static image that would lead to [a subscribe prompt](https://www.youtube.com/c/freecodecamp?sub_confirmation=1)._

And here's what this looks like when you set `data-layout="full"`:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Configure_a_Button_-_-_YouTube_Subscribe_Button_-_-_Google_Developers.png)
_This is a static image that leads to [a subscribe prompt](https://www.youtube.com/c/freecodecamp?sub_confirmation=1)._

You can also set the theme to dark with `data-theme="dark"`.

And you can hide your subscriber count completely with `data-count="hidden"`. If you only have a handful of subscribers, you may want to hide this for a few months while you build up a thousand subscribers or more, to avoid "negative social proof".

# Why I Recommend YouTube Subscribe Links Instead of YouTube Subscribe Buttons

There are several reasons why I recommend using the link approach instead of these dynamic buttons.

1. Ad blockers, firewalls, and browser plugins may block the button from rendering correctly or from working correctly. This button does involve pulling a JavaScript file from Google's CDNs, which means it won't render in China, for example, where Google is currently blocked.
2. It is hard to control the styling of these buttons, and they may end up looking bad on a mobile device.
3. These buttons may lead to accessibility issues. The link, on the other hand, is just a link, and is easy for people to use in screen readers or other assistive tools.

But Google does support these YouTube subscription buttons as well, so it's up to you whether you want to use them.

## A YouTube Subscribe Button Customization Tool

Google has an official tool for customizing these YouTube subscribe buttons. [You can access it here](https://developers.google.com/youtube/youtube_subscribe_button). Note that you will still need to have access to the HTML of the page you want to embed these buttons into.

Thanks for reading this guide, and I hope it has helped you understand how these YouTube subscribe links and buttons work, and how you can use them to get more people to subscribe to your channel.

If you want more tips on being a successful YouTube creator in general, you can learn from our nonprofit's 5+ years of experimentation that has helped us become the largest programming channel on YouTube. 

Here's our [free YouTube handbook, which also includes a 1 hour video course](https://www.freecodecamp.org/news/how-to-start-a-software-youtube-channel/). We designed it with software-focused creators in mind, but many of the techniques can be applied to other subject domains. I hope it's helpful for you.

Cheers.

– Quincy






