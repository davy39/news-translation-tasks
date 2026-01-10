---
title: Long-term, agile documentation of requirements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-25T18:47:01.000Z'
originalURL: https://freecodecamp.org/news/long-term-agile-documentation-of-requirements
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/art-book-pages-browse-256467.jpg
tags:
- name: agile
  slug: agile
- name: documentation
  slug: documentation
seo_title: null
seo_desc: 'By Bertil Muth

  In my training courses, we discuss many topics. Including: how do you document requirements
  in the long term, in an agile environment?

  Documentation is stored knowledge. As things are forgotten, its value increases
  over time. That’s wh...'
---

By Bertil Muth

In my training courses, we discuss many topics. Including: how do you document requirements in the long term, in an agile environment?

Documentation is stored knowledge. As things are forgotten, its value increases over time. That’s why I think the question of long-term documentation is interesting.

I’d like to start with two options for long-term documentation that  don’t make sense in an agile environment. Then I’d like to point out  sensible options. Each with advantages and disadvantages.

#### Not a useful option: Detailed up-front specification

It does not make sense to specify all requirements in detail in  advance. In a complex environment, there are frequent changes.  Requirements are re-prioritized. This is one of the advantages of agile development. Some requirements are considered, but never implemented. Or not as planned, because you gain new knowledge during development.

Discussion and documentation of a requirement costs time. If the requirement is not implemented as documented, it was a waste of time.  Time that is urgently needed in development.

#### Not a useful option either: The backlog

Let’s say you start to work in an agile way. Maybe you think: there  isn‘t any detailed specification. But a backlog. Let’s use it to document the requirements on a long-term basis.

But a backlog serves the future, not the past. It’s more like a to-do list. What do we implement next? The backlog isn't a sensible option for long-term documentation. It doesn’t document what has already been implemented.

#### Option 1: Archive user stories after implementation

In a training course, a participant told me that his company manages user stories in JIRA. And the developers archive them after implementation.  Of course, you can search this archive. The participant reported that it worked well for them.

An agile pragmatist can hardly disagree. What works, works. At least in a certain context. I see 2 risks of this approach:

* **Too many details:** In order to be able to use the  stories in the long term, you certainly have to document many details.  What if the details cannot be implemented as planned? Will the user stories be adjusted afterwards? The stories may no longer document the implementation correctly.
* **Delta documentation instead of system documentation:**  User stories describe what needs to be done. The “delta” from one state to another state. In order to find out the current state, it may be necessary to analyze several past user stories. Stories lack context  information. They are not system documentation, but only small  fragments.

#### Option 2: Incremental adaption of the system documentation

The documentation can be maintained continuously. During a Scrum Sprint, you document the current state.  The requirements that have just been implemented. The documentation grows over time. It is supplemented incrementally.

If you follow this approach consistently, it has a great advantage.  The system documentation is always up to date. It documents which requirements have actually been implemented.

One challenge with this option is discipline. Only if you document consistently, the documentation will remain up-to-date. And that costs  time.

Moreover, not every developer is a born documentation writer. If,  however, the developers do not document themselves, but instead delegate it to other employees, then there is a risk of information loss.

One way to promote this discipline within a team is to put it into the Definition of Done. Something like: “System documentation has been  updated”. To be checked in Sprint Review.

#### Option 3: Requirements inside the code

A completely underestimated type of long-term documentation is the code of the software. If you structure code appropriately and use naming  conventions, you can generate documentation from the code.

To realize this, I have [developed a library](https://github.com/bertilmuth/requirementsascode). With it you can specify executable Use Case models in the code. They act [similar to a state machine](https://www.freecodecamp.org/news/kissing-the-state-machine-goodbye/). Here is a code example for a Use Case for a credit card:

```java
	Model model = Model.builder()
	  .useCase("Use credit card")
	    .basicFlow()
	    	.step(ASSIGN).user(requestsToAssignLimit).system(assignsLimit)
	    	.step(WITHDRAW).user(requestsWithdrawal).system(withdraws).reactWhile(accountOpen)
	    	.step(REPAY).user(requestsRepay).system(repays).reactWhile(accountOpen)
	    	
	    .flow("Withdraw again").after(REPAY)
	    	.step(WITHDRAW_AGAIN).user(requestsWithdrawal).system(withdraws)
	    	.step(REPEAT).continuesAt(WITHDRAW)
	    	
	    .flow("Cycle is over").anytime()
	    	.step(CLOSE).on(requestToCloseCycle).system(closesCycle)
	    	
	    .flow("Assign limit twice").condition(limitAlreadyAssigned)
	    	.step(ASSIGN_TWICE).user(requestsToAssignLimit).system(throwsAssignLimitException)
	    	
	    .flow("Too many withdrawals").condition(tooManyWithdrawalsInCycle) 
	    	.step(WITHDRAW_TOO_OFTEN).user(requestsWithdrawal).system(throwsTooManyWithdrawalsException)
	.build();
```

The documentation [generated from this code](https://github.com/bertilmuth/requirementsascode/tree/master/requirementsascodeextract) follows.

GENERATED DOCUMENTATION - START

### **Use Credit Card**

#### **Basic flow**

**Assign limit** : User requests to assign limit. System assigns limit.  
**Withdraw** : As long as account open: User requests withdrawal. System withdraws.  
**Repay** : As long as account open: User requests repay. System repays.

#### Withdraw again

After Repay:  
**Withdraw again** : User requests withdrawal. System withdraws.  
**Repeat** : System continues at Withdraw.

#### Cycle is over

Anytime:  
**Close cycle** : Handles RequestToCloseCycle: System closes cycle.

#### Assign limit twice

Anytime, when limit already assigned:  
**Assign limit twice** : User requests to assign limit. System throws assign limit exception.

#### Too many withdrawals

Anytime, when too many withdrawals in cycle:  
**Withdraw too often** : System throws too many withdrawals exception.

GENERATED DOCUMENTATION - END

The same code controls the application behavior and is the source for the documentation. The advantage is obvious: You can generate documentation with little effort. And it reflects the actual behavior of the software.

Of course, this approach also requires discipline. Especially on the side of developers. Before using any approach, you should try it out. Is it suitable for the type of software being developed?

In addition, you can’t achieve completeness with such an approach.  For example, you can’t generate quality requirements like robustness from the code. Design trade-offs are not part of the code either.

I am looking forward to your feedback. Which options for long-term documentation do _you_ use?

_This article was first published on_ [_HOOD Blog_](https://blog.hood-group.com/blog/2017/05/10/anforderungen-langfristig-dokumentieren-im-agilen-umfeld/) _in German. If you want to keep up with what I'm doing or drop me a note, follow me on [dev.to](https://dev.to/bertilmuth), [LinkedIn](https://www.linkedin.com/in/bertilmuth/) or [twitter](https://twitter.com/BertilMuth). Or visit my [GitHub project](https://github.com/bertilmuth/requirementsascode)._

