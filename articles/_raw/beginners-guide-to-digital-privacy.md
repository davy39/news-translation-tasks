---
title: What Is Digital Privacy? A Beginner's Guide to Protecting Your Data
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-10T17:45:33.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-digital-privacy
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-kevin-paster-1901388.jpg
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
seo_title: null
seo_desc: "For all the many benefits we enjoy from technology – and particularly the\
  \ technologies that make up the public internet – there are plenty of costs, too.\
  \ \nFiguring out how you want to balance the benefits against the costs can take\
  \ some careful think..."
---

For all the many benefits we enjoy from technology – and particularly the technologies that make up the public internet – there are plenty of costs, too. 

Figuring out how you want to balance the benefits against the costs can take some careful thinking. Here's a concise and effective way to describe the equation (whose source I've sadly forgotten):

> "Select any two of privacy, security, and convenience. But you can't have all three."

In other words, if security is a critical value for you, then you'll need to give up on 24/7 instant access to your money, credit, and personal accounts. That's because that kind of access requires exposing your accounts across public networks at a level that won't permit as much data protection as you might want. 

Similarly, what if you just can't live without the convenience of getting news updates and social connectivity through sites belonging to third party businesses that collect and use your personal information? Well, you'll need to "pay for it" by giving up a measure of your privacy.

This tutorial was taken from my book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://www.youtube.com/watch?v=p7PmzNLzUws]

Of course, most of us will choose some blend of those three elements based on a practical compromise between competing values and needs. But making a reasonable decision on that blend will require solid information. That's what you'll find through the rest of this article.

# How Companies Get Your Data

Curious about what kinds of personal and even private data you may be exposing through the course of a normal day on the internet? 

How about using "all kinds" as a starting point? Perhaps the best way to understand the scope and nature of the problem is to break it down by platform.

## Data from Financial Transactions

Take a moment to visualize what's involved in a simple online credit card transaction. You probably signed into the merchant's website using your email address as an account identifier and a (hopefully) unique password. 

After browsing a few pages, you'll add one or more more items to the site's virtual shopping cart. When you've got everything you need, you'll begin the checkout process, entering shipping information, including a street address and your phone number. You might also enter the account number of the loyalty card the merchant sent you and a coupon code you received in an email marketing message.

Of course, the key step involves entering your payment information which, for a credit card, will probably include the card owner's name and address, and the card's number, expiry date, and a security code. 

Assuming the merchant infrastructure is compliant with Payment Card Industry Data Security Standard (PCI-DSS) protocols for handling financial information, then it's relatively unlikely that this information will be stolen and sold by criminals. But either way, it will still exist within the merchant's own database.

To flesh all this out a bit, understand that using your loyalty card account and coupon code can communicate a lot of information about your shopping and lifestyle preferences, along with records of some of your previous activities. 

Your site account comes with contact information and your home location. All of that information can, at least in theory, be stitched together to create a robust profile of you as a consumer and citizen.

It's for these reasons that I personally prefer using third-party e-commerce payment systems like PayPal because such transactions leave no record of my specific payment method and on the merchant's own databases.

## Data from Devices

Modern operating systems are built from the ground up to connect to the internet in multiple ways. They'll often automatically query online software repositories for patches and updates and "ask" for remote help when something goes wrong. 

Some performance diagnostics data is sent and stored online, where it can contribute to statistical analysis or bug diagnosis and fixes. Individual software packages might connect to remote servers independently of the OS to get their own things done.

All that's fine. Except that you might have a hard time being sure whether _all_ the data coming and going between your device and the internet is stuff you're OK with sharing. 

Can you know that private files and personal information aren't being swept in with all the other data? And are you confident that none of your data will ever accidentally find its way into some unexpected application lying beyond your control?

To illustrate the problem, I'd refer you to devices powered by digital assistants like Amazon's Alexa and the Google Assistant ("Ok Google"). Since, by definition, the microphones used by digital assistants are constantly listening for their key word ("Alexa..."), everything anyone says within range of the device is registered. 

At least some of those conversations are also recorded and stored online and, as it turns out, some of _those_ have eventually been heard by human beings working for the vendor. In at least one case, an inadvertently-recorded conversation was used to convict a murder suspect.

Amazon, Google, and other players in this space are aware of the issue and are trying to address it. But it's unlikely they'll ever fully solve it. Remember, convenience, security, and privacy don't work well together.

Now if you think the information from computers and tablets that can be tracked and recorded is creepy, wait 'till you hear about thermostats and light bulbs. 

As more and more household appliances and tools are adopted as part of "smart home" systems, more and more streams of performance data will be generated alongside them. 

And, as has already been demonstrated in multiple real-world applications, all that data can be programmatically interpreted to reveal significant information about what's going on in a home and who's doing it.

## Data from Mobile devices

Have you ever stopped in the middle of a journey, pulled out your smartphone, and checked a digital map for directions? Of course you have. 

Well, the map application is using your current location information and sending you valuable information but, at the same time, you're sending some equally valuable information back. What kind of information might that be?

I once read about a mischievous fellow in Germany who borrowed a few dozen smartphones, loaded them up on a kids' wagon, and slowly pulled the wagon down the middle of an empty city street. It wasn't long before Google Maps was reporting a serious traffic jam where there wasn't one.

How does the Google Maps app know more about your local traffic conditions than you do? One important class of data that feeds their system is obtained through constant monitoring of the location, velocity, and direction of movement of every active Android phone they can reach - including your Android phone. 

I, for one, appreciate this service and I don't much mind the way my data is used. But I'm also aware that, one day, that data might be used in ways that sharply conflict with my interests. Call it a calculated risk.

Of course, it's not just GPS-based movement information that Google and Apple – the creators of the two most popular mobile operating systems – are getting. They, along with a few other industry players, are also handling the records of all of our search engine activity and the data returned by exercise and health monitoring applications.

In other words, should they decide to, many tech companies could effortlessly compile profiles describing our precise movements, plans, and health status. And from there, it's not a huge leap to imagine the owners of such data predicting what we're likely to do in the coming weeks and months.

## Data from Web browsers

Most of us use web browsers for most of our daily interactions with the internet. And, all things considered, web browsers are pretty miraculous creations, often acting as an impossibly powerful concierge, bringing us all the riches of humanity without even breaking into a sweat. But, as I'm sure you can already anticipate, all that power comes with a trade-off.

For just a taste of the information your browser freely shares about you, take a look at the Google Analytics page shown in the iamge below. This dashboard displays a visual summary describing all the visits to my own bootstrap-it.com site over the previous seven days. I can see:

* Where in the world my visitors are from
* When during the day they tend to visit
* How long they spent on my site
* Which pages they visit
* Which site they left before coming to my site
* How many visitors make repeat visits
* What operating systems they're running
* What device form factor they're using (that is, desktop, smartphone, or tablet)
* The demographic cohorts they belong to (genders, age groups, income groups)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/figure2-2.png)
_The home dashboard of a Google Analytics page displaying visualizations of visitors to a website._

Besides all that, a web server's own logs can report detailed information, in particular the specific IP address and precise time associated with each visitor. 

This means that, whenever your browser connects to my website (or any other website), it's giving my web server an awful lot of information. Google just collects it and presents it to me in a fancy, easy-to-digest format.

By the way, I'm fully aware that, by having Google collect all this information about my website's users, that I'm part of the problem. And, for the record, I do feel a bit guilty about it.

In addition, web servers are able to "watch" what you're doing in real time and "remember" what you did on your last visit.

To explain, have you ever noticed how on some sites, right before you click to leave the page a "Wait! Before you go!" message pops up? Servers can track your mouse movements and, when they get "too close" to closing the tab or moving to a different tab, they'll display that popup. 

Similarly, many sites save small packets of data on your computer called "cookies." Such a cookie could contain session information that might include the previous contents of a shopping cart or even your authentication status. The goal is to provide a convenient and consistent experience across multiple visits. But such tools can be misused.

Finally, like operating systems, browsers will also silently communicate with the vendor that provides them. Getting usage feedback can help providers stay up to date on security and performance problems. But independent tests have shown that, in many cases, far more data is heading back "home" that would seem appropriate.

## Data from Website Interactions

Although some of this might be covered by previous sections in this article, I should highlight at least a couple of particularly relevant issues. 

Like, for instance, the fact that websites love getting you to sign up for extra value services. The newsletters and product updates that they'll send you might be perfectly legitimate and, indeed, provide great value – but they're still coming in exchange for some of your private contact information. As long as you're aware of that, I've done my job.

A perfect example is the data you contribute to social media platforms like Twitter, Facebook, and LinkedIn. You may think you're just communicating with your connections and followers, but it actually goes much further than that.

Take a marvelous – and scary – piece of software called Recon-ng that's used by network security professionals to test for an organization's digital vulnerability. Once you've configured it with some basics about your organization, Recon-ng will head out to the internet and search for any publicly available information that could be used to penetrate your defences or cause you harm.

For instance, are you sure outsiders can't possibly know enough about the software environment your developers work with to do you any damage? Well perhaps you should take a look at the "qualifications" section from some of those job ads you posted on LinkedIn. 

Or how about questions (or answers) your developers might have posted to Stack Overflow? Every post tells a story, and there's no shortage of clever people out there who love reading stories.

Software like Recon-ng can help you identify potential threats, but that only underlines your responsibility to avoid leaving your data out there in public in the first place.

The bottom line? Smile. You're being watched.

# Why Companies Want Your Data

Data is money. Some of the biggest and most successful tech companies of the past decade or two made their billions from data. Generally, that'd be from your data.

Of course, the value doesn't all move in one direction. Big tech companies do, as a rule, provide useful services. 

Health tracking apps do track and report on your health. Social media companies do (on rare occasion) provide for healthy social interactions. And historical performance data does sometimes help improve customer and technical service.

But businesses exist to generate revenue and, as a rule, the more data they own, the more revenue that data can generate. The more potential customers there are who provide their email and social media account coordinates, the easier it'll be to connect to them with new offers. And the easier it would be for other companies working in overlapping industries to connect to a business's customers as well. 

The incentive for you to sell your contact list to an interested third party is clear.

Naturally, legal restrictions and user agreements can sometimes stop such sales of data sets. But not every use-case is necessarily covered by such laws, and not every company is necessarily bound by a strong desire to follow the law.

A delicious case in point would be Canada's Do Not Call list from all the way back in 2004. The law prevented telemarketers from contacting anyone who had added themselves to the national list. The law required all telemarketers to remove all entries from the list from their own call lists.

The problem was that spammers happily downloaded the Do Not Call lists and, confident that they represented confirmed active accounts, called those specifically. The only law that was effective in this case was the _law of unintended consequences_.

Your data can also be useful for personalizing the results you get from search engine queries. Of course, you might sometimes enjoy seeing results relating to previous browsing behavior, but don't lose sight of the fact that your behavior is being used as part of a campaign to sell you stuff.

It's not only search engines: smartphone browsing histories are sometimes used by nearby businesses to push customized ads in your direction – sometimes even through automated digital displays on physical billboards and other signage.

Perhaps the biggest value your data can offer is when it's aggregated along with data generated by thousands or millions of other users. 

Data scientists can stream and parse huge, dynamic data sets to extract significant insights about subtle but significant trends. In many cases, such data is sanitized to remove any personally identifiable information (PII).

We can nicely sum up the 21st Century web application business model with this popular – and accurate – expression:

> "If you're not paying for the product, you are the product."

# How to Protect Your Data

All that sounds pretty bleak. After all, George Orwell's 1984 was meant to be a warning, not a how-to guide. What can you do to push back?

### Be aware of your environment.

Do you still even notice those terms of service disclosures you "click to sign" before they'll let you use some service or tool? Some of those disclosures are as long as this article – and, if I may say so myself, a whole lot less fun. 

But the fact is that they contain information that can have a profound impact on both you and your data.

Many agreements describe what data they're likely to collect and what they're planning to do with it. They'll often also offer assurances that they'll never sell your data to third parties – an assurance that they might sometimes even honor in both the letter and the spirit of the law (although there have been famous cases of companies that did neither).

I've never met anyone who has the time and energy to read through those endless disclosures from end to end. But if an organization pays a bunch of lawyers to write something, you can bet it's a serious business.

### Be aware of your rights.

Beyond your specific agreement with a technology service provider, the use of your data might be regulated by government legislation. 

One example is the European Union's General Data Protection Regulation (GDPR), which controls how organizations must treat any personal data they encounter in the course of their operations. 

Another example is the US government's Health Insurance Portability and Accountability Act (HIPAA), which regulates the handling of private information in the health insurance and healthcare industries.

### Be aware of your alternatives.

Consider adopting privacy-first tools instead of the more heavily commercial services you're using now. For instance, the DuckDuckGo.com search engine, whose home page is shown below, doesn't track your search behavior and will return the same results to a particular query for you as for anyone else. 

They are a for-profit business, but they earn much of their income through affiliate links that pay them a commission for sales generated through search links – none of which has any impact on your privacy.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/duckduck.png)
_The DuckDuckGo browser homepage_

The Brave browser, as another example, has been shown to send far less undocumented data out to the internet than any other major browser. 

To be specific, in early 2020, Douglas Leith of the School of Computer Science & Statistics, Trinity College Dublin, tested six browsers for their risks of revealing unique identifying information about their host computers (scss.tcd.ie/Doug.Leith/pubs/browser_privacy.pdf). He found that Brave clearly offered the greatest privacy protection.

Brave also blocks web page ads by default, which raises a question. Since many web pages earn income exclusively through display ads, does Brave expect content providers to offer their services for free? 

The browser provider actually has a business model that includes the content providers: users of the Brave browser can opt to be shown simple and extremely unobtrusive ads from carefully curated advertisers in exchange for micro payments in a crypto currency. The users can then choose to make micro payments to website content providers using those funds as a way to pay for their content through the Brave Rewards program (pictured below).

![Image](https://www.freecodecamp.org/news/content/images/2022/12/figure2-4.png)
_Screenshot of the Brave rewards program_

Opting for open source applications can also be an effective privacy strategy. OpenStreetMap (openstreetmap.org) is an alternative to Google Maps. It might not have all the bells and whistles and built-in connectivity you may be used to, but it's just that connectivity that powers our reservations, isn't it?

If you're not comfortable with the big mobile operating system players (Android and iOS), you could, instead, buy a phone and install one of a number of experimental mobile Linux variations. 

Going down this road will likely be bumpy. Expect to run into unexpected configuration and compatibility challenges, and don't expect to find all the convenient apps that you've come to know and love using the big app stores.

See a hole that needs filling? Why not contribute your own innovation by participating in existing open source projects or adding your own solutions to the community?

## Thanks for Reading!

I hope this article has given you the tools to take good care of your digital privacy.

_YouTube videos of all ten chapters from this book [are available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness - in the form of books, courses, and articles - [can be had here](https://bootstrap-it.com). And consider taking my [AWS, security, and container technology courses here](https://www.udemy.com/user/david-clinton-12/)._

