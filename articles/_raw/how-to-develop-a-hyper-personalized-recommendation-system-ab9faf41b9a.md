---
title: How to develop a hyper-personalized recommendation system
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T00:35:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-a-hyper-personalized-recommendation-system-ab9faf41b9a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*49XRS70Wt6F5-Wwo7JghNQ.jpeg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mariya Yao

  Interview with Jack Chua of Expedia


  As part of our AI For Growth executive education series, we interview top executives
  at leading global companies who have successfully applied AI to grow their enterprises.
  Today, we sit down with Ja...'
---

By Mariya Yao

#### Interview with Jack Chua of Expedia

![Image](https://cdn-media-1.freecodecamp.org/images/1*49XRS70Wt6F5-Wwo7JghNQ.jpeg)

As part of our [AI For Growth executive education series](https://www.topbots.com/ai-for-growth), we interview top executives at leading global companies who have successfully applied AI to grow their enterprises. Today, we sit down with [Jack Chua](https://www.linkedin.com/in/jackchua/), Director of Data Science at Expedia.

Jack has built automated trading systems for multi-million dollar investment portfolios, terabyte-scale recommender systems for Amazon, and personalized marketing for an iconic American beverage brand. Previously he led industrial applications of machine learning for global clients of Boston Consulting Group (BCG). Now he heads the data science team at Expedia, where he applies his deep expertise in product and pricing optimization.

Watch the episode (or read the transcript below) to learn:

1. A brief history about the evolution of the recommender system
2. How to choose the right KPI metric to come up with the right mixture of recommendations
3. Pitfalls to avoid when building your own recommender system
4. Hot topics in applying AI to retail in the next three to five years

**Marlene Jia:** Thank you all for joining our AI for Growth Executive series. In this interview series, we learn from executives at leading global companies who have successfully applied AI to their enterprise and their team.

My name is Marlene — you can call me MJ — and today we’ll be chatting with Jack Chua, who’s the Director of Data Science at Expedia. He’s also had a background at Amazon, working at BCG, so I think we’ll have a lot of really interesting things to learn from Jack today.

Jack, thanks for joining us. For our first question, we would love to hear more about you, your story, and how you first became interested in AI.

**Jack Chua:** It’s a field that a lot of us inadvertently land into. Obviously it’s super interesting and very high impact.

My path has been a bit unconventional. I started studying theoretical math at the University of Chicago. Maybe two or three years in, I thought to myself, “What the heck am I going to do with this degree?”

I looked into what was hot at the time. This was back in 2006. A lot of my peers were going into investment banking, hedge funds, that kind of space. I was thinking, “Is there a way to apply the theoretical math that I learned and merge that into the sexy M&A banking type of thing?”, and I stumbled into the field of quantitative finance.

I started voraciously reading books about option pricing, volatility trading, things where you can basically determine the underlying stochastic process of the instrument and trade, given its dynamics.

I was lucky. I got in before the whole subprime financial crisis hit, but I would say that was how I started bridging the gap between theoretical math and industry.

Another point in time came when I started doing high-frequency trading. It’s a field where not just the statistical elements of the trade are necessary but also the engineering elements, and I realized the gap between knowing the theory [and] actually being able to implement the theory, whether in C++ or Python or what-have-you.

At the time, coming from a pretty theoretical academic background and job, I had to sit down and learn how to code from scratch. That’s what led me to go back to graduate school in Georgia Tech in applied mathematics, and that’s where machine learning was really starting to burgeon. I started taking computational data analysis courses, learned from some of the best professors in the world there. A few years later, here we are today.

**MJ:** You’ve worked at Amazon, [and] you’ve worked on numerous projects within recommendation engines. How did you get started there and where did that lead you? Obviously you’re at Expedia now.

**JC:** Recommendation engines are a small part of what I do, but it’s a very important part. The way that I like to describe it is “surfacing the right content to the right customer at the right time and in the right channel.” On top of the content, it’s [a] whole ecosystem of how that content is displayed and what’s the context.

Maybe this is pre-empting other things you might ask me, but when you think about recommending something to someone, there’s a real business reason why you might want to do that, whether it’s to encourage cross-selling of products, or increasing the frequency of someone coming back to your website because you’ve got great information and so on. I think recommender engines have a great tie-in to the underlying KPI of what you want to drive.

I think that’s what drove Amazon to invest in data scientists and engineers to work on the recommender systems, because the underlying context of why someone buys something is so complex. It could be the fact that it’s seasonal, maybe there’s a big discount that’s about to happen, or maybe it’s utilitarian, so they actually just thought of something [like] “Hey, I want this USB stick”, so they just go to our website and buy it.

All these contextual clues combine in a way that classical business intelligence or business rules cannot capture. It’s like a pure play AI problem, it’s something that using business rules or human rules would be suboptimal.

**MJ:** Before we dive into all the details, I would love for you to tell us exactly what a recommendation engine really is, walk us through how you would go about building it, and what the factors of consideration are, which you started talking about.

**JC:** Just starting from pure axiomatic definition, a recommender system is real estate on a channel of some sort, whether it’s email or a website or mobile app, what-have-you. You’ve probably seen it on Amazon, it’s a ribbon that has multiple products on it. It could be an email that has multiple components that has different products. There’s building blocks that comprise these emails or these marketing materials, and it’s the job of the human to figure out what should go in there.

What drives the system is usually a whole engineering work streaming ecosystem that goes into a simple email that falls into your mailbox. It could have UX designers designing what the email looks like, whether it’s summer festive-looking or maybe something that looks more transactional.

It could also just be data-driven — what data sciences tend to do — this is called [a batch process](https://en.wikipedia.org/wiki/Batch_processing). They’ll train the models in the backend, and the models could look at historical transaction data, they could look at a customer demographics, they could look at the product metadata itself, [like] the difference between a USB stick or a TV or a toy, take all this information and provide the marketers with a list of customer IDs to all the products that they think are going to be relevant.

There are also [real-time processes](https://en.wikipedia.org/wiki/Real-time_computing) where literally the minute someone clicks on the email, it sends a signal back to the data scientists, [who] then immediately incorporates it back into the next touch point. Where I’ve seen that done best is probably Amazon, or actually in travel websites like Booking.com and Expedia.

Retail is a space where the margins [are] so tight that to really innovate in this space, you have to think of different contexts and ways to understand what the customer’s trying to buy that’s out of the ordinary

**MJ:** You talked about Amazon doing it the best. Obviously they’ve been working on this for a long time. What spurred the initial development of this? It makes sense to us today, but Amazon and Google were some of the first companies to do this.

Can you tell us about the thought process and how it’s evolved since the time that you are there?

**JC:** Evolution might be the more natural point to start. All of these things in industry are generally driven by a business purpose. Recommender systems for retail [center around this idea of] “Hey, we have this dynamic real estate that no longer is limited to signposts or billboards, and it can change every second or maybe even every time someone lands on the website.” It’s now dynamic real estate, and in order to capture the dynamic-ness of the real estate, there needs to be some way to incorporate data seamlessly to update it.

Usually that’s how it started. There’s many things in practice that could be called recommendation systems, but we can just focus on websites for now.

If you land on Amazon, you have multiple ribbons, and a good example of how different KPIs can be targeted is every ribbon has a different purpose. One of them could be “these are things you’ve searched before” or “these are things we think you like” that are based on what you bought before.” Amazon is usually pretty good about explaining what the ribbon is, so you land on it, and there’s a contextual anchoring, so you see exactly what the recommendation is for.

Historically, those ribbons have been business-ruled, so a very simple business rule might be “show things that you’ve bought before so you’ll buy it again.” Shockingly, that led to a lot of lift when Amazon implemented the Buy-It-Again module, so that’s something that doesn’t require any intelligence, just looking at what someone has bought before inserting the exact same thing. That can work for things that customers have irregularity buying like pet food or various beauty products, but it tends to not work in things like fashion, where if you buy one shirt, you’re probably not going to buy the exact same shirt again.

That’s what drives the evolution of the recommender system, like, what is product [and] what is the KPI for the product, what are you trying to incentivize a purchase of the same thing or something like it? Based on that, you can tailor your algorithm.

A simple business-rule algorithm for cross-sell might be [association rule mining](https://mapr.com/blog/association-rule-mining-not-your-typical-data-science-algorithm/): looking at things that tend to be bought in the same basket.

In a grocery store context, there’s staples and things that are often cross-sold because they have a higher margin, maybe milk, bread, and eggs. Someone goes into the grocery store to buy milk, maybe then a natural thing to get next is bread.

That’s something that doesn’t require predictive analytics. It’s really just mining the data to see what patterns emerge.

Another way of doing it is based on something called [collaborative filtering](http://recommender-systems.org/collaborative-filtering/). This is [before] predictive models…actually I would say it’s not outdated because it’s newer than some predictive models…but it’s a relatively simple approach.

The idea is to look at people that are similar to you in transactions.

Marlene and I are pretty similar at Amazon, so maybe we’ve both bought the exact same things except for one item. A natural thing to do is say, “Okay, because Marlene and Jack have been almost exactly the same until that one item, let’s just recommend that item to both Marlene and Jack and see what happens.”

It’s not as simple as that, because the similarity can go multiple ways. It could be I’m 10% of Marlene and 10% of someone else and 80% of someone else, and that combines into essentially a linear combination of different people. That score that’s extracted for every product for me is a combination of different people’s weights. That was a breakthrough, and Netflix and the movie recommendation problem spurred the development of collaborative filtering

Then it moved into, “Can we make collaborative filtering even better?” Are there ways to start incorporating variables into the collaborative filtering so [that] not only do we know that Jack and Marlene are similar, Jack and Marlene are similar because these products are similar? Or, maybe Jack and Marlene are similar because they both live in the same city and they’re both in the same demographic? That removed one of the fallbacks of the traditional collaborative filtering, which had no variables.

Another thing that came up was the idea of neural networks, and obviously that’s been a big thing with deep learning and so on. Because deep learning enables someone to take in the raw transactions, you can incorporate so much more information and just let the algorithm do things a priori.

With a neural network, you can take in transactions, you can take in product information, you can take in customer information…. All that can just flow in its raw form. There’s no need to create any new variables, and the algorithm will just figure out the rank order of products that you like to buy.

**MJ:** Deep learning is such a popular term and method [that] people are starting to explore. I would love to hear more.

**JC:** The traditional way you can think about neural nets are kind of like [functional approximators.](https://www.cse.unsw.edu.au/~billw/cs9414/notes/ml/04fn/04fn.html) Actually, a linear regression is a neural net, just with one layer and one set of weights. Think back to middle school or high school arithmetic, when you do the chain rule you have an f(g(h)) equals to something. That’s essentially what a neural net is, but it’s actually discovering the correct f, g, and h that most accurately models your data.

The most generic form of the deep neural net is a [multi-layer feed-forward neural network.](https://towardsdatascience.com/deep-learning-feedforward-neural-network-26a6705dbdc7) You can create multiple layers that are called dense layers. It’s dense because each node, which represents a variable, will connect to another node in the next layer.

The node could be the types of a product you buy, or a node can be a customer. A neural net could be tens of thousands of nodes. With the advancements of [back-propagation](https://medium.com/datathings/neural-networks-and-backpropagation-explained-in-a-simple-way-f540a3611f5e) and all the new inference techniques, it’s now way easier to train a deep neural network than it has been in the past.

I’m not an expert in the underlying technology, but definitely an advanced practitioner.

**MJ:** You had mentioned earlier that some of these methods are actually not predictive. Which of the methods are predictive, then? What are the current methods that companies like Netflix and Amazon are using?

**JC:** Collaborative filtering, I think it maybe could be predictive, but most of how people use it is not predictive. That’s historically how Netflix has used it, and that’s just a limitation of the collaborative filtering and matrix factorization family of algorithms.

The reason is because the way you think about it is actually a matrix completion problem. If you think of a matrix, each customer would represent one row, and every column would represent the product, and every cell in a matrix is a score that represents how much a customer likes that product. In Netflix’s case, [it would be] how much a customer likes that movie. As you can imagine, that matrix is probably pretty sparse, because not every customer has seen every movie.

That’s one of the drawbacks of collaborative filtering: it’s not only not predictive, but often you’ve got a really sparse matrix.

The way to initialize this matrix is to use some historical figure. Maybe this is Jack’s rank on the movie, because he watched the movie last week and he gave it a 5. It’s not predictive in the sense that maybe I would give the movie a five next week.

I think part of Netflix decided that this was fine because movie preference is generally pretty stable over time. If you watched a movie a year ago, there’s a good chance you probably still like the movie now, so the predictive component is not as important for this problem.

In transactions or retail, it’s quite possible that your preference changes rapidly, or the minute you buy something, it no longer has the same recommendation power.

That’s where the predictive elements come in, and you can frame recommender systems in a similar way as you frame other problems like churn detection or anomaly detection. You have an X matrix that contains all your variables, and these X variables are historical. You know if you’re at a time T, these are things that are time T minus one before, and your Y variable is the thing that’s predictive, so it’s actually time t+1, or t plus a month, or whatever forward lead period you have.

That’s how most classification and regression problems are structured. If you train a deep neural network, that’s pretty much exactly the information that goes into training your neural network.

I’m not talking about tensors or anything that’s more dimensional than that, but generally speaking, you’ll have a dataset that contains your historical data, you’ll have an objective function or Y variable that contains the future information you want to predict.

What happens is, when you’re trying to predict something given your current point in time, you’re not leaking information. You’re only using the information you know at time t to predict time t+1.

**MJ:** To your point about all of these use cases that you mentioned, like retail, movies, so many brands (both small and large) talk about building a recommender engine of some sort. What really makes it powerful?

With Amazon obviously you can say that they have a big data set, but what are some of the other variables that allow a recommendation engine to be better than the next?

**JC:** Data is number one, [like] the data assets that your company has housed. If it’s Amazon, obviously it’s the incredible number of customers and transactions they have, the incredible product diversity they have, so not just in the popular products but even in the long tail.

After data, then the algorithm is what can help differentiate. If you’re a company that’s using simple business rules versus deep neural networks or something like that, that makes a big difference as well.

Another thing that a lot of people underestimate but is super important is the customer experience. Instead of just throwing a ribbon with a bunch of recommendations, thinking through a whole ecosystem with things like “what are all the touch points that customers are receiving”, “am I fatiguing the customer with too many touch points”, “is it information overload”, “am I representing the intent correctly”?

Amazon, for instance, historically has been utilitarian. A good number of customers [go] to Amazon with an explicit agenda in mind, like they wanted to buy specific things, [so] they type it in and bought it. [Amazon] tried really hard to leverage that, because it’s a good thing, it’s good that people come to Amazon for the purpose. Leverage that, lean into that to see how we can cross sell better, selling things in different channels [such as] digital media, sell hardware [like] Kindles.

**MJ:** I don’t know if you saw the [Mary Meeker report](https://www.recode.net/2018/5/30/17385116/mary-meeker-slides-internet-trends-code-conference-2018). She had said that 49% of people who go to Amazon start and basically end with Amazon. They search through Amazon and then they purchase through Amazon.

To your point, I think you’re right, most people do come with the intent of purchasing there. It’s very utilitarian.

**JC:** Another really great example that I love to give is Starbucks. If you’re part of the Starbucks loyalty program, more often than not you’ve seen games that pop up either through email or your app.

It’s a game so it’s a different medium than your traditional recommender system, but underlying that game is actually a heavy customer data-driven recommender engine, which determines what products you like, what is the type of engagement you need in order to be a more valuable customer, and so on.

The main point is that data scientists have to work in lockstep with either designers or marketers or business analyst in order to come up with the optimal experience.

Otherwise, something like a game requires so many different cross functional lines of thought that I don’t think either a data scientist or a marketer could have done it by themselves. Data scientists would have just tried to figure out the recommender problem and not thought about the experience, whereas marketers would not even realize that data science could be used to optimize something. Literally, to as many customers that they can have, you can pull as many levers. If you have 15 million customers, you literally could have 15 million variants using data science.

**MJ:** We’ve already talked about some examples where [companies have] built a really strong recommendation engine. Can you give some other examples of good recommendation engine you’ve seen out there, whether it be brands or specific use cases within companies?

**JC:** There’s so many. I love Spotify. I think they do a great job with both the customer-based recommender system, meaning finding out which other people are like you and what they like to listen to…

**MJ:** They squash SoundCloud at this point, in my opinion. I used SoundCloud before Spotify…

**JC:** I did too actually. But yes, Spotify definitely is — in terms of engineering and the sophistication of what they what they recommend — they just do so much more.

The interesting thing — most likely, I don’t know for sure because I don’t work there — they actually look at the music itself. Whether it’s the tags of the music, like what kind of genre is it, who’s the artist…they also probably look at what’s the tempo, what are the instruments, and they’re actually digging into the DNA of the music, similar to what Pandora was doing and use that to figure out what types of music you’d like. So, going beyond genre as well.

I’ve noticed that sometimes Spotify recommends me things that I didn’t think I would ever like listening to, but the more I listen to it, the more I realize it actually is similar to things that I like.

Another one is YouTube. They have slightly different KPIs in retail — in the sense that most of your KPIs are not transaction-based, they center on engagement — so they’re designed to keep you on the website for longer.

I think their process probably starts with the design, so what is the actual UX that we want to enable someone that’s currently on the platform to do, so kind of like the whole customer journey mapping and figuring out at this point in a journey, what is the right experience for the customer.

An example might be when you’ve just finished watching a video, that’s a great piece of real estate to step in and figure out based on what was just watched, so contextual on Marlene or Jack finishing this video on fuzzy cats, what is the next thing that we think that they would like to watch?

Often times, these contextual hints pop up [at] opportune moments on a customer journey, and I think YouTube figures out what these journeys are and what these optimal points are, and then builds bottles around that.

**MJ:** Now you’ve spurred a different question, which is how exactly people go about creating these engines? You mentioned that with different use cases, you have to start at different questions and different points. For example, you said with YouTube, you might start with a question of design and engagement, but with Spotify, it might be different.

What are the different ways you would even begin to design this engine for a good customer experience?

**JC:** That’s a good question. I wish there was a one-size-fits-all answer, but I don’t think there is. It’s kind of a gray thing because there’s multiple ways that YouTube or Spotify could have designed their experience but I think it’s generally just working cross-functionally and figuring out what it is, what is the rank order of things that customers care about.

For Amazon, it was, “Hey, our customers are really utilitarian, let’s cross-sell to them a bit more. For Expedia or travel companies, it’s “Let’s figure out customer segments.” Can we figure out if someone is a luxury traveler or a business traveler? Are they [at] the end of the customer lifecycle, where they’re off to churn and go to some other website, or are they in the beginning, so it’s more about education?

There’s just so many ways to characterize a customer, but I think it generally starts with understanding the customer better, like what segments they’re in, how they engage. Of the people that are falling off, what are the leading indicators that might tell us you’re falling off? Of the people that are just starting, what are the indicators if someone’s actually growing into a stable trajectory? Those are just your typical customer lifecycle modeling, and from there, designing the right experience to maximize the life cycle.

**MJ:** I assume KPIs are similar. The KPIs for Spotify, for example, or for Amazon are probably different than YouTube, to your point around [whether] you’re going for the purchase or the next song or engagement.

What would you say are some baseline KPIs that you track for these engines?

**JC:** That’s a really great question. Conversion, whether it’s converting to a transaction or converting into a click, that’s generally the de facto standard for a recommender system. I’ve also seen recommender systems optimized for other things like revenue and profit and maybe even some more esoteric things, like revenue on items that have a higher margin than 30% net of returns, so that objective would be “I want to recommend things that are high margin and people don’t just return it.” So you can be very precise with these KPIs.

The thing to realize, in choosing between these, is what am I enabling? In choosing this KPI, what is actually happening to the things that I recommend?

For the margin one, what’s most likely to happen is if we build a data science model that optimizes profit, naturally you’re gonna start recommending things that are high margin. It may not necessarily be what the customer wants. Even if it doesn’t say high profit, like you don’t explicitly call that on your website, it still biases your algorithm to pick things that are not representative of a broader set.

Another interesting KPI in the recommender system is diversity. In most models, the model will have a pretty strong conviction of what type of customer you are. It doesn’t take into account the cross-correlation between the things I recommend. Maybe from going to Amazon, it determines that I really like socks. Most likely in the top ten, you’ll see socks, maybe you’ll see underwear, maybe you’ll see more socks. Although it may be true that I like socks, one slot is enough for that sock. There needs to be a way to take things that scored lower in the algorithm and surface that up for the sake of diversity.

There’s these cross-hybridized [objective functions](http://kronosapiens.github.io/blog/2017/03/28/objective-functions-in-machine-learning.html) where you do want to maximize for conversion, but you have to take into account the customer experience as well. If you give them diversity, then they explore the longer-tailed products, and [maybe] longer term [that] might increase customer value

**MJ:** I have so many more questions, but I think we’re running out of time. I want to just ask this final question: what are your final tips for building a good recommendation engine? How do you avoid the pitfalls? What are the things to watch out for?

**JC:** The number one tip: you know your product better than a vendor does. The vendor can give you advice on the algorithm and what to use, but [don’t] plug-and-play a recommender system into your website without really understanding your business and what drives it. Is it like a milk and eggs and bread type of thing, or is it a fashion thing where you don’t want to recommend too similar things, or if it’s a lifecycle thing where you need to recommend things that fit the lifecycle, only you know that. If a vendor claims to know this better than you, I think it’s a clear sign to stay away.

Number two, you have to consider the maturity of your business to actually take in something that’s as complicated as deep neural network. Obviously a deep neural net will give you cutting edge performance, [but] your business might not need that depending on where it is.

Something I found is that if you look at all the research papers about [random forests](https://medium.com/@williamkoehrsen/random-forest-simple-explanation-377895a60d2d) versus [gradient boosted decision trees](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) versus [neural network](http://news.mit.edu/2017/explained-neural-networks-deep-learning-0414), the difference in the cutting edge once you get past the gradient boosted tree is really small. You’ll generally only see a five to ten percent improvement in your accuracy by going to something that’s cutting edge. What this means is that you can get to 80% of what you need with something that’s fairly simple. Take that into account.

Another thing to take into account is the resourcing. If you do decide to build something in-house, it’s hard to find a deep learning expert or a machine learning expert that can maintain it over time. What this means is that your business has to be mature enough to support these engineers, because I think a lot of people have a notion that once they build it for me, it’s done, I have the capability.

In reality, it’s something that needs to be maintained over time, improved, bugs can pop up. No machine learning pipeline is perfect. From a strategic perspective or a technical perspective, you have to think about it as a long-term investment versus just a build and throw it over the fence, which again brings it back to why it’s more important to build a capability in-house than having a vendor do it, because the vendor isn’t invested long-term in your business like you are.

**MJ:** Just thinking about this, I think you are probably the best recommender engine. What do you think would be a good topic for us to cover in another one of our AI for Growth series?

**JC:** Well, tapping it into the human neural network, I think something around pricing would be interesting [like] dynamic pricing and the ability to price on-the-fly is something that, especially for companies that are moving away from brick-and-mortar channels or on order, companies like Uber where pricing things is done on-the-spot, that’s something that machine learning has really just scratched the surface in industry

Another really interesting thing is the intersection between pricing and personalization. Not just servicing the right content but also servicing the right price in conjunction with that content to give personalized promos that are dynamic and tailored to every customer. That looks like the next frontier for retail over the next three to five years. I think it’s going to be happening pretty quickly, because there’s so much value associated with it. I’m happy to come on and discuss more, depending on how many of these you have.

**MJ:** Thank you so much, Jack. This was such a wonderful conversation, and I’m sure we’ll be just having you on another one another time, so thank you. And thank you everyone for tuning into AI for Growth. We’ll see you guys at our next episode!

![Image](https://cdn-media-1.freecodecamp.org/images/0*teA74RZe1k3nGCS7.png)

#### Learned something? Click the ? to say “thanks!” and help others find this article.

_The full transcript from this interview was first published on [TopBots](https://www.topbots.com/developing-hyperpersonalized-recommendation-systems-interview-jack-chua-expedia/?utm_medium=article&utm_source=Medium&utm_campaign=Hyperpersonalized)._

