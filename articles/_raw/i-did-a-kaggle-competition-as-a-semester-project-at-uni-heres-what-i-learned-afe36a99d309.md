---
title: I did a Kaggle competition as a semester project at uni. Here’s what I learned.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T17:36:04.000Z'
originalURL: https://freecodecamp.org/news/i-did-a-kaggle-competition-as-a-semester-project-at-uni-heres-what-i-learned-afe36a99d309
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Q7IdllDE47WuWP-H
tags:
- name: kaggle
  slug: kaggle
- name: learning
  slug: learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: university
  slug: university
seo_title: null
seo_desc: 'By Ane Berasategi

  It was my first competition and my first semester. I didn’t know what I was doing.


  _Photo by [Unsplash](https://unsplash.com/@miguel_photo?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Miguel Henriq...'
---

By Ane Berasategi

It was my first competition and my first semester. I didn’t know what I was doing.

![Image](https://cdn-media-1.freecodecamp.org/images/9pu2uThG1h1G6Uasfc6HKW9SEEOuTNbYdcNv)
_Photo by [Unsplash](https://unsplash.com/@miguel_photo?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Miguel Henriques</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

This is the story of how I decided to be creative in a semester-long project, how my initial topic choice was crushed and how doing a Kaggle competition at the last minute saved my grade.

As my personal background, I studied Telecommunications Engineering, I have some experience with software development and machine learning, but I had no idea about NLP back then.

I started my Masters degree last semester and one of the first subjects I attended was called ‘Classification and clustering’ in NLP. The professor explained the basics of text processing during the first weeks and afterwards each student had to pick a classification or clustering problem in NLP, document the theory, implement a solution, and present it to the class. The implementation could be done at the end of the semester, not right away with the presentation.

> I was new at the uni so I decided to wait and observe what the other students did.

#### Choosing the topic

Very quickly, the topics of decision trees, naïve Bayes, random forests, SVMs, logistic regression, etc were picked. I barely knew what they were so I was excited at the thought of my peers squeezing these topics into 30 min presentations, and I gave them all my attention and wrote all the notes I could.

Unfortunately, these first presentations were **purely theoretical,** since no one had had time to implement anything so early in the semester. I learnt later that the motivation behind presenting so early had been the urge to ‘pick an easy topic before someone else took it’ and ‘get the presentation over with’, postponing the implementation of the algorithm until later on in the semester.

As much as I tried, I didn’t understand much of the presentations. I need to visualize things, see the code, see examples. It’s not easy for me to follow a presentation full of mathematical notation and formulas.

> Weeks passed, the professor started to urge us to choose a topic and set a date for the presentation, and I had nothing. I waited some presentations more before starting to panic.

The next presentations were a little more advanced: LDA, LSI, perceptrons, NNs, tensorflow, keras and word embeddings among others.

I was completely ignorant on some topics (LDA and LSI), but I did know some minimal ML. These presentations did include **code**, sometimes even too much. There was a lot of scrolling and very little time spent on analyzing the code, the focus was purely on the results. I learnt about the origins of tensorflow and keras, and I was left exhausted and confused at the end of each presentation. As much as I’d tried, I hadn’t learnt much.

> I was one of the last students left to choose a topic, and the professor was looking at me every time he mentioned the ‘friendly reminder’. I got the message.

I tried to think rationally: there weren’t many obvious topics left, and I wanted a topic interesting for me and for the other students where I could put everything to use, not just a data structure or a ML model. The subject had 6 ECTS and I wanted to use the time to produce something I could be proud of.

I asked my friend to Google for classification problems in NLP, and after some searching I found out about **sentiment analysis**. It wrapped everything together beautifully, and I had my topic. I checked if someone had already picked it up, no one had, I told the professor, he said ‘Finally!’, and I started gathering my references. The wheel was in motion.

The following week, at another lecture, a guest lecturer gave a very interesting talk about his Master Thesis, on **sentiment analysis**. Of course. My fellow classmates and I spent 90 mins learning about it, the motivation of using it, the applications, the development, the code, the results, _everything_. It was a majestic Master Thesis and a very illustrative talk, and it ruined my presentation.

I could have still done my project on the same topic, but everyone had heard the experienced researcher on his thorough talk for 90 mins, there was no way I could’ve been able to do the equivalent of his Master Thesis in a couple of months, so I decided to keep looking for something unique, something I could present and people would say: “oooh”.

> At this point, panic mode was on.

My presentation date was in 2 months, my awesome topic was no more, and I needed something, fast. I was scrolling through Twitter trying to ignore the pressure when I saw Kaggle announced their brand new [**Quora insincere questions classification competition**](https://www.kaggle.com/c/quora-insincere-questions-classification/)**,** and I remember thinking:

* Quora? I like Quora
* Insincere questions? Sounds like fun!
* Classification? Could this be…

I went to the webpage, and it was indeed a text classification problem. It was as if Kaggle had seen me drowning and lent me a helping hand. This competition could solve all my problems.

![Image](https://cdn-media-1.freecodecamp.org/images/u9Ukm6X1wwRQ6aLue1jH8XrByi1scWr8z8CO)

1. Had I ever done a Kaggle competition before? I have done some small projects on ML but never a competition.
2. Was the competition for beginners? No, it was hosted by Quora with real prizes, and professional people competing hard for it.
3. Did I have the slightest clue where to begin? No I did not.

So I went for it. Doing this project would be doing something completely different from the rest of the class, and of course I was afraid. This is the mental dialogue with myself:

* What’s the worst that could happen?
* Well, the professor might reject the topic.
* Okay assuming it’s accepted, the worst thing?
* Not finishing in time, not having something complete to present.
* Fair point, what if I have something complete?
* It could be terrible, worse than random classification.
* That would indeed be bad.

So I set my goal to have something finished and ideally with a decent result in two months.

I enthusiastically pitched the idea to the professor, he listened and nodded and said: “Sure, you can change the topic”. I also heard “if you can pull it off” but I’m somewhat sure that last part came from inside my mind and he didn’t actually say it.

I was going to do the documentation and implementation of my submission at the same time, so I set to work.

#### The Kaggle competition

Since my ambitions were humble, I didn’t bother with the imposter syndrome. I made a list of the popular kernels in the website, went through them, understood them, combined them, tweaked them, and made my own.

#### 1. EDA

The first thing to do was exploratory data analysis (EDA). In hindsight I spent way too much time exploring the questions, but in my defense, I didn’t know what I was doing, and some of the insincere questions were funny, I have to admit. I gathered all the questions Quora classifies as insincere and extracted some that I personally find funny. [You can see them in my github](https://github.com/anebz/kaggle/tree/master/quora_insincere_questions). And you can see my [EDA in kaggle](https://www.kaggle.com/anebzt/quora-eda).

#### 2. Preprocessing

Strategies were a bit different in the preprocessing, and it took some more time to understand what people were doing. I learnt how to use word embeddings, adjust the input text so that the text coverage is the maximum and the amount of unknown words is at the minimum. I was quite proud of how much I learnt about text processing in such a short time.

I used Glove as pretrained embeddings, the text coverage at the beginning:

![Image](https://cdn-media-1.freecodecamp.org/images/MdCtirsEuSPJSJEbIyBEYKFxtsFPp6l5GKOJ)

From all the different words that were used, 31.5% are recognized by the embeddings, and from all the text used, 88%. There are more frequent words than others, such as ‘the’. ‘a’. etc. That 31.5% of the vocabulary makes up to 88% of the total text.

After lowering the text, expanding the contractions and removing special characters and punctuations, the coverage is as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/ZhXNxFC2JkSAWduggHBqRU9vt5TpLEo4PQRq)

Out of vocabulary words (those not recognized by the embeddings) include the following, along with their frequency:

![Image](https://cdn-media-1.freecodecamp.org/images/rG861sZlXpZO7nWxO5iT9Xq59PL9W1X7C-i3)

You can see my [preprocessing kernel in kaggle](https://www.kaggle.com/anebzt/quora-preprocessing-model).

#### 4. The model

Here my limited knowledge on ML helped me move a bit faster, the only bottleneck was deciding which architecture to use. People were using models from RNNs to LSTMs to BERT even, adding KFold, cyclical learning rates, bidirectional models, what?

My stress level went up, the presentation date was in two weeks and I didn’t understand any of the architectures. I picked the simplest one that could give me a decent score, I started with a LSTM architecture.

I connected everything together, and I got a result. A terrible one, but a result nonetheless. My basic needs fulfilled, I started working on the presentation while I left model tuning as my procrastination activity. Eventually I added an Attention layer, and finally turned it into a bidirectional LSTM. The score was decent.

![Image](https://cdn-media-1.freecodecamp.org/images/RL7l3MyvHRdeMR3R40GoeCkDC1VVhr9GzwEQ)

The final architecture I used, a BiLSTM with an Attention layer. It trained quite fast and gave a relatively good result. As before, you can see [the whole kernel in kaggle](https://www.kaggle.com/anebzt/quora-preprocessing-model).

#### 5. The preparation

For the first time in my life, I had too much material for my presentation. I had to cut enough to fit into 30 minutes, but no more lest I made my talk too general. I had to show code but not only code, since in my experience it’s difficult to focus on just code for half an hour.

I spent the last two weeks documenting my code, adding all the references I had used, just in case someone somewhere thought I had made that project by myself and had retrieved the information from my imagination.

> The openness in Kaggle and the availability of public and well-documented code is one of the greatest incentives of using Kaggle in my opinion.

I polished my presentation and trained with classmates to see that I didn’t talk for over 30 mins. I did, and they gave me tips to reduce repetition in what I was saying, showing in the slides, and showing again in the code; I made much simpler slide-code transitions as a result.

#### 6. The presentation

For my presentation, I only used slides to explain the specifics of the competition: motivation, problem definitio, ninput data, metrics, etc.

For the EDA and preprocessing, I had a slide explaining what I would show in the code, later I switched to the code, and then came back to the slides and showed a recap of what I had just shown. At the end, I included all the advanced model architecture additions I hadn’t had time to consider.

The presentation went very well, I only spoke for 30 mins and there was a follow-up discussion of another 30 mins, where the whole class discussed different strategies to classify insincere questions. The professor praised my creativity and said he would consider changing the structure of the semester so that more students did their projects similar to mine.

I consider that a successful project!

#### 7. Conclusion

Since I didn’t know what I was doing throughout the project, I had many doubts, it’s risky doing something completely opposite to the rest of the class, it can end very well or terribly.

I learnt that being creative can sometimes be rewarded, and that calculated risks are worth taking. In this case, I consulted with the professor before doing anything and he approved, so the risk was smaller.

I learnt a lot doing the Kaggle competition, I scored on the top 29% which is not so terrible! I’m quite proud of it, considering it was my first competition.

If there’s anything I can say as a takeaway, it’s this:

> If you’re at university or at a course/program, use the time to learn, experiment, and put yourself in situations where you could fail, but also succeed. My professional relationship with the professor got stronger because of my project.

> If you can afford to do more than just completing the subject, consider going beyond what the professor says. Read the references, research online, propose topics. Who knows where your initiative could take you.

> And lastly, **you don’t have to do exactly what the other students do**. Just because everyone follows a certain structure or submission format doesn’t mean it’s the correct one. Talk to the professor or teaching assistants, ask students who had the subject the previous year, and then decide consciously how you want to handle the subject.

I hope you liked my story! If you want to hear more about it or contact me in any way, you can reach me [on twitter.](https://twitter.com/aberasategi)

