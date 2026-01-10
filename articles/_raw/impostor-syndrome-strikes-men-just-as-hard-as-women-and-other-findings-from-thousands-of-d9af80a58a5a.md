---
title: Impostor syndrome strikes men just as hard as women… and other findings from
  thousands of…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T21:49:29.000Z'
originalURL: https://freecodecamp.org/news/impostor-syndrome-strikes-men-just-as-hard-as-women-and-other-findings-from-thousands-of-d9af80a58a5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bEEt_IXW6wWTmE2N6cucZQ.png
tags:
- name: interview
  slug: interview
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cat Hicks

  The modern technical interview is a rite of passage for software engineers and (hopefully!)
  the precursor to a great job. But it’s also a huge source of stress and endless
  questions for new candidates. Just searching “how do I prepare fo...'
---

By Cat Hicks

The modern technical interview is a rite of passage for software engineers and (hopefully!) the precursor to a great job. But it’s also a huge source of stress and endless questions for new candidates. Just searching “how do I prepare for a technical interview” turns up millions of Medium posts, coding bootcamp blogs, Quora discussions, and entire books.

Despite all this conversation, people struggle to know how they’re even doing in interviews. [In a previous post](http://blog.interviewing.io/people-are-still-bad-at-gauging-their-own-interview-performance-heres-the-data/), we found that a surprisingly large number of interviewing.io’s users consistently underestimate their performance, making them more likely to drop out of the process and ultimately harder to hire.

Now, and with considerably more data (over 10k interviews led by real software engineers!), we wanted to go deeper: **what seems to make candidates worse at gauging their own performance?**

We know some general facts that make accuracy a challenge: people aren’t always great at assessing or even remembering their performance on difficult cognitive tasks like writing code [[1](http://blog.interviewing.io/#imposter-fn1)]. Technical interviews can be particularly hard to judge if candidates don’t have much experience with questions with no single right answer.

Since many companies don’t share any kind of detailed post-interview feedback (beyond a yes/no) with candidates for liability reasons, many folks never get any sense of how they did, what they did well, or what could have been better [[2](http://blog.interviewing.io/#imposter-fn2), [3](http://blog.interviewing.io/#imposter-fn3)]. Indeed, pulling back the curtain on interviewing, _across the industry,_ was one of the primary motivators for building interviewing.io!

But to our knowledge, there’s little data out there looking specifically at how people feel after real interviews on this scale, across different companies — so we gathered it, giving us the ability to test interesting industry assumptions about engineers and coding confidence.

One big factor we were interested in was impostor syndrome. Impostor syndrome resonates with a lot of engineers [[4](http://blog.interviewing.io/#imposter-fn4)], indicating that many wonder whether they truly match up to colleagues and discount even strong evidence of competence as a fluke. Impostor syndrome can make us wonder whether we can count on the positive performance feedback that we’re getting, and how much our opportunities have come from our own effort, versus luck.

Of particular interest to us was whether this would show up for women on our platform. There’s a lot of research evidence that candidates from underrepresented backgrounds experience a greater lack of belonging that feeds impostor syndrome [[5](http://blog.interviewing.io/#imposter-fn5)], and this could show up as inaccuracy about judging their own interview performance.

### **The setup**

interviewing.io is a platform where people can practice technical interviewing anonymously, and if things go well, get jobs at top companies in the process. We started it because résumés suck and because we believe that anyone, regardless of how they look on paper, should have the opportunity to prove their mettle.

When an interviewer and an interviewee match on interviewing.io, they meet in a collaborative coding environment with voice, text chat, and a whiteboard and jump right into a technical question (feel free to [watch this process in action on our interview recordings page](https://interviewing.io/recordings/)). After each interview, people leave one another feedback, and each party can see what the other person said about them once they both submit their reviews.

Here’s an example of an interviewer feedback form:

![Image](https://cdn-media-1.freecodecamp.org/images/rUejiWD-QpW3yIhTLxdSMUOdB-E2nBBELDr1)
_Feedback form for interviewers_

Immediately after the interview, candidates answered a question about how well they thought they’d done on the same 1–4 scale:

![Image](https://cdn-media-1.freecodecamp.org/images/qTemiehT3G4R8MmU3uC-zCWJnkjGJEQ3scGv)
_Feedback form for interviewees_

For this post, we looked at over 10k technical interviews led by real software engineers from top companies. In each interview, a candidate was rated by an interviewer on their problem-solving ability, technical ability, and communication skills, as well as whether the interviewer would advance them to the next round. This gave us a measure of how different someone’s self-rating was from the rating that the interviewer actually gave them, and in which direction. In other words, how skewed was their estimation from their true performance?

Going in, we had some hunches about what might matter:

* **Gender**. Would women be harder on their coding performance than men?
* **Having been an interviewer before**. It seemed reasonable that having been on the other side would pull back the curtain on interviews.
* **Being employed at a top company**. Similar to above.
* **Being a top-performing interviewee** on interviewing.io — people who are better interviewees overall might have more confidence and awareness of when they’ve gotten things right (or wrong!)
* **Being in the Bay Area** or not. Since tech is still so geographically centered on the Bay Area, we considered that folks who live in a more engineering-saturated culture could have greater familiarity with professional norms around interviews.
* Within the interview itself, **question quality** and **interviewer quality**. Presumably, a better interviewer is also a better communicator, whereas a confusing interviewer might throw off a candidates’ entire assessment of their performance. We also looked at whether it was a practice interview, or for a specific company role.
* For some candidates, we could also look at few measures of their **personal brand** within the industry, like their number of GitHub and Twitter followers. Maybe people with a strong online presence are more sure of themselves when they interview?

### So what did we find?

#### **Women are just as accurate as men at assessing their technical ability**

Contrary to expectations around gender and confidence, we _didn’t_ find a reliable statistically significant gender difference in accuracy. At first, it looked like female candidates were more likely to underestimate their performance, but when we controlled for other variables, like experience and rated technical ability, it turned out that **the key differentiator was experience**. More experienced engineers are more accurate about their interview performance, and men are more likely to be experienced engineers. But experienced female engineers are just as accurate about their technical ability.

Based on previous research, we hypothesized that impostor syndrome and a greater lack of belonging could result in female candidates penalizing their interview performance, but we didn’t find that pattern [[6](http://blog.interviewing.io/#imposter-fn6)].

However, our finding echoes [a research project from the Stanford Clayman Institute for Gender Research](https://gender.stanford.edu/sites/default/files/publications/climbing_the_technical_ladder.pdf), which looked at 1,795 mid-level tech workers from high tech companies. They found that women in tech aren’t necessarily less accurate when assessing their own abilities, but do have significantly different ideas about what success requires (e.g., long working hours and risk-taking). In other words, **women in tech may not doubt their own abilities but might have different ideas about what’s expected**.

[And a survey from Harvard Business Review](https://hbr.org/2014/08/why-women-dont-apply-for-jobs-unless-theyre-100-qualified) asking over a thousand professionals about their job application decisions also made this point. Their results emphasized that gender gaps in evaluation scenarios could be more about **different expectations for how scenarios like interviews are judged**.

That said, we did find one interesting difference: women went through fewer practice interviews overall than men did. The difference was small but statistically significant, and harkens back to [our earlier finding that women leave interviewing.io roughly 7 times as often as men do](http://blog.interviewing.io/we-built-voice-modulation-to-mask-gender-in-technical-interviews-heres-what-happened/), after a bad interview.

But in that same earlier post, we also found that masking voices didn’t impact interview outcomes. This whole cluster of findings affirms what we suspected and what the folks doing [in-depth studies of gender in tech](https://gender.stanford.edu/sites/default/files/publications/climbing_the_technical_ladder.pdf) have found: **it’s complicated**. Women’s lack of persistence in interviews can’t be explained only by impostor syndrome about their _own_ abilities, but it’s still likely that they’re interpreting negative feedback more severely and making different assumptions about interviews.

Here’s the distribution of accuracy distance for both female and male candidates on our platform (zero indicates a rating that matches the interviewer’s score, while negative values indicate underestimated score, and positive values indicate an overestimated score). The two groups look pretty much identical:

![Image](https://cdn-media-1.freecodecamp.org/images/rCbQS0KYerTPE5v9SCqTwgnZAfgz8bTq6wJd)

#### What else didn’t matter?

Another surprise: **having been an interviewer didn’t help**. Even people who had been interviewers themselves don’t seem to get an accuracy boost from that.

**Personal brand was another non-finding.** People with more GitHub followers weren’t more accurate than people with few to no GitHub followers.

**Nor did interviewer rating matter** (i.e. how well an interviewer was reviewed by their candidates), although to be fair, interviewers are generally rated quite highly on the site.

#### So what was a statistically significant boost to accurate judgments of interview performance? Mostly, experience.

Experienced engineers have a better sense for how well they did in interviews, compared with engineers earlier in their careers [[7](http://blog.interviewing.io/#imposter-fn7)]. But it doesn’t seem to _just_ be that you’re better at gauging your interview performance because you’re better at writing code; although there is a small lift from this, with higher rated engineers being more accurate. But when you look at junior engineers, **even top-performing junior candidates struggled to accurately assess their performance.** [[8](http://blog.interviewing.io/#imposter-fn8)]

![Image](https://cdn-media-1.freecodecamp.org/images/hiFZy8I2mgxhskD5M2CX80Det2nK2yvEk23k)

Our data mirrors a trend seen in [Stack Overflow’s 2018 Developer survey](https://insights.stackoverflow.com/survey/2018#connection-and-competition). They asked respondents several questions about confidence and competition with other developers, and noted that more experienced engineers feel less competitive and more confident [[9](http://blog.interviewing.io/#imposter-fn9)].

This isn’t necessarily surprising: experience is correlated with skill level, after all, and highly skilled people are likely to be more confident. But our analysis let us control for performance and code skill within career groups, and we _still_ found that experienced engineers were better at predicting their interview scores.

There are probably multiple factors here: experienced engineers have been through more interviews, have led interviews themselves, and have a stronger sense of belonging, all of which may combat impostor syndrome.

#### **Insider knowledge and context also seems to help.**

Being in the Bay Area and being at a top company both made people more accurate. Like the experienced career group, engineers who seem more likely to have _contextual industry knowledge_ are also more accurate. We found small but statistically significant lifts from factors like being located in the Bay Area and working at a top company. However, the lift from working at a top company seems to mostly measure a lift from overall technical ability: being at a top company is essentially a proxy measure for being a more experienced, higher quality engineer.

#### **Finally, as you get better at interviewing and move into company interviews, you do get more accurate.**

People were more accurate about their performance in company interviews compared to practice interviews, and their overall ranking on the interviewing.io site also predicted improved accuracy: interviewing.io also gives users an overall ranking, based on their performance over multiple interviews and weighted toward more recent measures. People who scored in the top 25% were more likely to be accurate about their interview performance.

In general, how are people at gauging their interview performance overall? [We’ve looked at this before](http://blog.interviewing.io/people-are-still-bad-at-gauging-their-own-interview-performance-heres-the-data/), with roughly a thousand interviews, and now, with ten thousand, the finding continues to hold up. Candidates were accurate about how they did in only 46% of interviews, and underestimated themselves in 35% of interviews (and the remaining 19%, of course, are the overestimators).

Still, candidates are generally on the right track — it’s not like people who score a 4 are always giving themselves a 1 [[10](http://blog.interviewing.io/#imposter-fn10)]. Self-ratings _are_ statistically significantly predictive for actual interview scores (and positively correlated), but that relationship is noisy.

### The implications

Accurately judging your own interview performance is a skill in its own right, and one that engineers need to learn from experience and context in the tech industry. But we’ve also learned that **many of the assumptions we made about performance accuracy didn’t hold up to scrutiny** — female engineers had just as accurate a view of their own skills as male engineers, and engineers who had led more interviews or were well known on GitHub weren’t particularly better at gauging their performance.

What does this mean for the industry as a whole? First off, impostor syndrome appears to be the bleary-eyed monster that attacks across gender and ability, and how good you are, or where you are, or how famous you are isn’t that important. Seniority does help mitigate some of the pain, but impostor syndrome affects everyone, regardless of who they are or where they’re from.

So, maybe it’s time for a kinder, more empathetic interviewing culture. And a culture that’s kinder to everyone, because though marginalized groups who haven’t been socialized in technical interviewing are [hit the hardest by shortcomings in the interview process](http://blog.interviewing.io/you-cant-fix-diversity-in-tech-without-fixing-the-technical-interview/), no one is immune to self-doubt.

We’ve previously discussed what makes someone a good interviewer, and [empathy plays a disproportionately large role](http://blog.interviewing.io/what-do-the-best-interviewers-have-in-common-we-looked-at-thousands-of-real-interviews-to-find-out/). And we’ve seen that [providing immediate post-interview feedback is really important for keeping candidates from dropping out](http://blog.interviewing.io/people-are-still-bad-at-gauging-their-own-interview-performance-heres-the-data/). So, whether you’re motivated by kindness and ideology or cold, hard pragmatism, a bit more kindness and understanding toward your candidates is in order.

[_Cat Hicks_](https://www.drcathicks.com/)_, the author of this guest post, is a researcher and data scientist with a focus on learning. She’s published empirical research on learning environments, and led research on the cognitive work of engineering teams at Google and Travr.se. She holds a PhD in Psychology from UC San Diego._

