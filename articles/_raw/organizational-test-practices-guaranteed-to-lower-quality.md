---
title: 'Test Engineering Anti-Patterns: Destroy Your Customer Satisfaction and Crater
  Your Quality By Using These 9 Easy Organizational Practices'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-30T13:59:11.000Z'
originalURL: https://freecodecamp.org/news/organizational-test-practices-guaranteed-to-lower-quality
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca033740569d1a4ca4735.jpg
tags:
- name: engineering
  slug: engineering
- name: organization
  slug: organization
- name: satire
  slug: satire
seo_title: null
seo_desc: 'By Cristian Medina

  A recent podcast episode reminded me that it''s a good idea to examine things from
  different perspectives. Doing so can expose behaviors that appear purposeful as
  consequences of environmental factors. You won''t succeed at fixing th...'
---

By Cristian Medina

A recent podcast episode reminded me that it's a good idea to examine things from different perspectives. Doing so can expose behaviors that appear purposeful as consequences of environmental factors. You won't succeed at fixing those behaviors unless you do something about the environment that encourages them.

Today the discussion is about Test engineering and organizational practices that tend to lower the quality of your deliverables.

When reading through, please keep in mind that we're emphasizing goals that are contrary to what you expect - lower quality and customer satisfaction. The suggestions may seem cynical and counter-intuitive, but that's the point of the exercise. So let's get started.

## 1. Make the Test teams solely responsible for quality

One of the best ways to lower quality is by shifting focus away from the product and towards internal politics.

You want to capitalize on default human behavioral responses that minimize reasoning and maximize conflict — what better way of doing so than encouraging tribalism.

Holding only one organization responsible for a goal (no matter what it is) will guarantee the divisive behavior you're trying to obtain.

That group will spend most of its time and resources proving their responsibilities were met, instead of facilitating product goals.

To maximize the impact of this principle, make sure that Test teams _only_ own the quality objective. They should not be responsible for determining release content, that's the Marketing team. Nor should they be involved in setting release dates, that's a Sales function. They also don't determine which problems to fix, that's up to the Product team.

You want the Development team focused on delivering features by the time the Marketing and Sales orgs promised them. So avoid imposing any code commit or merge rules requested by Test, like requiring code reviews, passing linters, passing unit tests, and others. After all, quality is Test's responsibility, not Development's.

Breaking up objectives in this way, turns meeting agendas away from customer experience and towards the blame game. You know you're on the right track when you hear statements like:

* "Why didn't you find this bug sooner!"
* "The current tests failed, but we really need to merge this new feature so you can start testing it."
* "Why didn't Test find this customer issue?"
* "We promised the customer a release by this date, so let's defer all Test findings and give them a build today."
* "We found the issue that the customer reported, but you deferred it last month!"
* "I can't run tests because you gave me a broken build."

Spending time arguing about whose job it is to do the work is an excellent mechanism to reduce satisfaction with your product or service.

## 2. Require all tests to be automated before releasing

Another device for distracting from quality is requiring test automation for every feature. It guarantees that your Test organization spends most of its time doing software development instead of test engineering.

The goal should change from validating a product attribute, to counting how many automated tests ran to verify it.

Rather than thinking through the test breakdown that validates various code paths or fundamentals of a function, engineers will spend time and resources executing multiple iterations of the same test. It leads to higher counts.

It also promotes a fragile test infrastructure and increases maintenance costs.

Since there's no time to consider test strategy and abstractions, they're forced to write very specific - yet brittle - workflows. Whenever Development makes slight changes to the feature, the tests break.

The Test organization must focus on producing a large number of tests as fast as possible. Otherwise, they'll have time to push more value into the product with more meaningful tests.

Make sure to reward this behavior by promoting engineers that produce the highest number of automated tests that run frequently. But don't forget about those that save time by writing scripts that execute other scripts while hard-coding all the arguments so the user won't have to type them.

## 3. Require 100% code coverage

Since product quality and customer experience are only correlated to code coverage, forcing your Test and Dev teams to chase 100% coverage is another tactic.

Make sure you direct all execution conversations towards the coverage measurement and hold teams accountable for it. People will focus on building tests that call all code functions, regardless of their output.

A nice bonus is that measuring coverage tends to affect timing or performance. It makes it hard for anyone to understand the actual customer experience, thereby adding to your goal of decreased satisfaction.

Make sure that tool implementations are automated, and that every report includes the coverage numbers, so it's easy to bring up in conversations.

Avoid focusing on code branching coverage. It's essential to prove that you tested every function, not every code path in the function. After all, there's no point in planning for customers to hit failure cases. They only happen a small percentage of the time.

Just like the previous section, don't forget to reward the team for being as close as possible to the 100% coverage number. It goes a long way in showing your engineers the behavior that matters.

## 4. Isolate the Test organization from Development

One of the worst things in software development is when the Dev team is so in-sync with Test that they finish each other's sentences. It's a red flag! It means that you're on a path for producing a quality product or service.

Reduce all chances for collaboration, including physical proximity. 

Make sure to separate the teams, so it takes physical effort for a Test engineer to walk over to a Developer and ask questions. Human nature will take hold and solve the rest of the problem for you.

When both of these organizations actively collaborate, they tend to help each other considerably. You'll find the Developer gives the Tester a heads-up about new changes. Alternatively, the opposite could happen, where a Developer will know about a bug before it's reported. Not only does this break tribalism, but it sidetracks well-defined responsibilities.

Collaboration leads to less process: 

* In some cases, issues are just fixed instead of reported.
* Internal documentation and knowledge transfers receive less time and attention.
* Test engineers become more knowledgeable about the product. 
* Release schedules start to reflect reality during planning. 

All of these lead to higher quality and better customer satisfaction! The direct opposite of your goals.

Enforcing more process is a great way of discouraging this behavior. It helps highlight the requirements that an engineer doesn't meet when directly engaging with other teams. It can come in the form of extra checkpoints and meetings, but preferably, more documentation.

Another excellent tool for increasing isolation is access controls. Make sure that Test does not have access to source code and that Dev cannot see the procedures of a test case.

I find that separating tests from code is a must! If you have both in the same repository, then Developers will know ahead of time when they break a test. A process shortcut that leads to the very efficiencies we don't want.

## 5. Measure the success of the process, not the product

I can't tell you how many conversations I've had with coworkers that keep asking impertinent questions about customer adoption.

Things like: How many customers are using that feature? What's the potential impact to our install base? How many steps must the user go through to use this feature? What's the attach rate? How big is our potential customer pool for that requirement? How many users asked for this function?

These folks don't get it. It's imperative to discourage this behavior as it happens. It tends to spread to other team members, and pretty soon, you'll have an organization that only cares about quality.

The best thing to do is redirect that energy by asking questions about the process instead. The items below are some stats that help accomplish this.

### Number of open issues and who opened them

It helps prove how well the Test team is doing and how much work they're putting in.

Don't forget to encourage the employees that opened the highest number of issues. Bring it up in meetings often, so the rest of the folks are not surprised during performance reviews.

Some will try to argue that too many open issues lead to significant overhead in managing them. Again, that's the whole point.

Refocus team effort away from quality and towards process. Plus, if there are too few issues, then the Test org looks like their not working.

### Amount of time an issue spent waiting for Test response

It's trickier to measure, but when you can pull it off, it's a great way to show how well the Test org is doing when compared to Development. It encourages behaviors that help maximize the active issue count.

To help the situation, try to tie issue status changes to process requirements that enforce particular field values for specific situations.

It reduces the time an issue spends on the Test side whenever parameters don't match because the engineer will have to ask for the correction.

Development is usually too busy to care about this stuff. So it also leads to lots of political discussions in project management meetings and encourages more tribalism.

### Percentage of issues in a closed state

Before a release, you want to encourage the team to close all issues. It's best to base the performance review of Development engineers on how many issues were open against their code at release time.

It guarantees fewer defects opened by the Development team - further boosting your Test performance. It also discourages communication with the Test organization and increases friction.

### Percentage of tests executed compared to an execution plan

Don't forget to make an execution curve telling the team how to spend their time throughout the test cycle. Be careful not to base it on history, or you may find that the org meets the numbers and improves quality.

Check the graph in every status meeting and ask for progress regardless of the state of the product. It forces the inclusion of tests meant to always complete just to pad the numbers and meet expectations.

Discourage anyone that beats projections. Doing so makes it look like the Test org has free time.

### Measure the pass rate

You'll want to track the percent of test execution that's passing vs. failing for all the tests put together.

Make sure you explain to the team the required pass rate to reach a release stage. It reminds them to design suites with enough tests that always pass so that you can meet process requirements.

## 6. Require granular projections from engineers

Getting a schedule from Dev is hard. Many times they try to throw reality at the problem as if complexity mattered. The truth is you'll release by the date designated by the Sales organization regardless, but Dev never seems to understand that.

Whenever discussing code completion dates, make sure to ask for the day, not the week or the month when they'll complete. If you disagree with that date, bring it up in a public forum of all their peers so they can argue it.

Doing so accomplishes several essential points in lowering quality:

* Developers fight among themselves, reducing communication.
* They stop thinking they have a say in how to spend their days or do their jobs, which increases turnover.
* It makes it unlikely that they meet their deadlines, which lowers their performance review and also increases turnover.

Achieving high turnover is like the holy grail of lowering quality. It helps reduce the bottom line with fewer raises and promotions. It increases disinformation, emphasizing individualism. Finally, it removes any ownership that might build up in the team over time.

## 7. Reward quick patching instead of solving

Given enough time, engineers can solve almost every problem. But when you do the opposite, an interesting phenomenon occurs: instead of resolving the root issue, they fix the symptoms, sometimes ignoring the problem completely.

Here are some of the benefits you'll see when using this technique:

* Development gets praise for being quick.
* The base problem isn't solved, so there's a bunch of opportunities for writing future bugs, making the Test team and the process look better.
* The customer will keep running into the same issues, which translates to lower satisfaction.
* The patches for each symptom develop a spiderweb of dependencies, making future work harder and more brittle, which translates to lower quality.
* You'll gain issues for everyone you fix at a viral pace. The more problems to fix, the more process you need to track the ones left behind. Win-win!

Rewards are fundamental here as well. Make sure to incentivize this type of work with awards, and broadcast them to the team so everyone is aware of the behavior you want.

## 8. Plan for today instead of tomorrow

There's always someone trying to foresee what tomorrow brings. These days some engineers will do statistical analysis or machine learning. Formulating an algorithm that explains how well execution is going, which issues are important, how much time is actually needed, the number of resources required to test, etc.

Then there are the folks that have been around long enough and keep bringing up past mistakes or wasted efforts you should avoid.

Ignore that advice and always plan for the best case today. It doesn't matter if technical debt is high, if the 3rd party vendor has low quality, or if everyone planned a vacation on the same day during the next release.

Deal with problems when they occur, not before. Otherwise, efficiency will increase.

# 9. Conclusions

While there are many more points to cover, it seems our fictional Sales team decided to ship before completing the article!

On a more serious note, test engineering and product validation gets exponentially harder with complex systems and large organizations. It's important to incentivize the right type of behaviors in order to succeed. However, those aren't always obvious and in some cases, they're even counter-intuitive.

I do hope the article helped you observe the test world from a different perspective. One that provides some helpful insight. I find this practice of aiming for bad outcomes quite illuminating sometimes. At the very least, it's loads of fun to think through.

---

If you liked the article and want to read more about development best practices from Cristian Medina and others, please visit [tryexceptpass.org](https://tryexceptpass.org). Stay informed with their latest content by subscribing to [the mailing list](https://tinyurl.com/tryexceptpass-signup).

