---
title: Coding Interviews Behind the Scenes - the good and the bad
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-05T16:15:22.000Z'
originalURL: https://freecodecamp.org/news/behind-the-scenes-of-coding-interviews-good-vs-bad
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca112740569d1a4ca4c7d.jpg
tags:
- name: coding
  slug: coding
- name: coding interview
  slug: coding-interview
- name: Job Interview
  slug: job-interview
seo_title: null
seo_desc: 'By Srinivasan C

  Interviewing is a skill in and of itself. You can be the best developer in the world
  but you may still screw up an interview.

  https://twitter.com/mxcl/status/608682016205344768?ref_src=twsrc%5Etfw

  How many times have you come out of a...'
---

By Srinivasan C

Interviewing is a skill in and of itself. You can be the best developer in the world but you may still screw up an interview.

%[https://twitter.com/mxcl/status/608682016205344768?ref_src=twsrc%5Etfw]

How many times have you come out of an interview and wondered what did I do wrong? Why did they reject me?

As a candidate, it helps a lot to understand the expectations in an interview. 

In this article, I want to show every aspiring candidate the difference between a good and a bad interview and how it is perceived by the interviewer. 

We will compare and contrast two different interviews and learn from each of them so that you can tweak your actions to match the expectations.

## First Interview

Let me take the same question above "Inverting a binary tree".

_Interviewer (I)_: Hi, Welcome to our company. I am xxx doing yyy. So tell me about yourself.

_Candidate (C)_ : I am xxx. I have about 5 years of experience in Backend development. I love solving technical problems.....

_I_: That's great. So shall we move on to the problem-solving part?

_C_: Sure!

_I_: So you are given a binary tree. I want you to invert the binary tree and print the resulting tree.

_C_: _**(Thinking in the head)**_ Hmmm Ok. A binary tree has two children. So I am assuming inverting means printing from leaf to root. So the easiest way to do that is to traverse the tree till the end and find the leaves...

_I_: _**(After 5 mins of complete silence)**_  Do you understand the question? Do you need any clarification?

_C_: I am **clear**. Now I am just thinking of a way to print the nodes starting from the leaf.

_I_: What do you mean to print the nodes starting from the leaf?

_C_: So basically I should print from leaf to root right? It is easy to traverse until the leaf. But the hard part is traversing back?

_I_: Hmmm. Are you sure you understand the question right? Inverting a tree means you should **swap the left and right children**.

_C_: Sorry I am not clear. When you said invert I **assumed** you meant printing from leaf to root.

_I_: That's alright _**(This is where you lost the job)**_. Now that you are clear let's proceed.

_C_: Yes I am clear. So now I have to swap the left and right nodes. That's easy right.  
_**(Writes code in silence)**_

```ruby
def invert(node)
  t = node.left 
  node.left = node.right
  node.right = t
  return node
end

```

_C_: I am done with the code.

_I_: Cool. So what have you done here?

_C_: I have inverted the tree by swapping the left and right nodes. So I keep a temp variable to achieve the same.

_I_: _**(Trying to nudge towards a proper solution)**_ But this swaps only the root node right?

_C_:_**(Puzzled)**_ Hmm yes, so the left and right children will be inverted. That's the question right?

_I_: _**(Still there is no clarity in question)**_ So the question is the complete tree should be inverted. Not just the root.

_C_: Oh geez. So it is not just the root but the complete tree. Am I right?

_I_: Yes that is correct.

_C_: Ok. Let me think about it.

_**(After 2 mins)**_

_C_: I think I got it. So basically I need to do the same algorithm I wrote for the whole tree. Am I right?

_I_: Yes, but how do you do that?

_C_: _**(Starts writing Code)**_

```ruby
def invert(node)
  n = Node.new(node.val)
  invert(node.left)
  invert(node.right)
  n.left = node.right
  n.right = node.left
  return n
end
```

So I am **guessing** this should work.

_I_: Hmmm, let me see. _**(Finds the issue. Can you?)**_ I am not sure if it works. Can you please run me through it?

_C_: Sure. First I am inverting the left subtree, then the right subtree and then I am swapping them so that root is inverted.

_I_: Hmmm. But the left and right nodes are returning new nodes after the swap right? You are still swapping the old nodes.

_C_: I am not sure what you mean by that. I think this **will** work for all cases.

_I_: Great man! We have run out of time. Thanks for your time, it was lovely talking to you. HR will get back to you.

## Feedback

Now, what do you think was the final decision and what was the interviewer's feedback? The hypothetical feedback would be something along these lines:

* The candidate assumed a lot of things and did not clarify the problem.
* The candidate came up with the approach out of nowhere and there was no proper reasoning behind the approach taken. (Remember the silence in the interview?)
* The candidate was not clear with the requirements even in the implementation stage.
* The candidate struggled with the implementation and he was not able to pick up hints pointing towards the solution.
* The candidate failed to identify the bugs in code, even after providing enough time and probing to check if the solution is correct.

If this were an actual interview, the candidate would have been rejected. Now how should the ideal interview go?

## Second interview

_Interviewer (I)_: Hi, Welcome to our company. I am xxx doing yyy. So tell me about yourself.

_Candidate (C)_ : I am xxx. I have about 5 years of experience in Backend development. I love solving technical problems.....

_I_: That's great. So shall we move on to the problem-solving part?

_C_: Sure!

_I_: So you are given a binary tree. I want you to invert the binary tree and print the resulting tree.

_C_: _**(Thinking out loud)**_ Cool. So a binary tree has two nodes. So what exactly is inverting? is it swapping the left and right?

_I_: Exactly. So left node should be on the right and vice versa.

_C_: Ok. So in this case what happens?

_**Provides an example and clarifies input and output**_

_I_: You are correct to some extent. But this should happen for the whole tree, not just the root alone._**(Notice how early the requirements were solidified)**_

_C_: Oh got it! So I am thinking I need to do it recursively. Man, that's tough! Let me see. But before that, I'll just check my understanding by running through one more example.  
_Provides one more eg to clarify any missing pieces_

_I_: Yes you are right. That's the output. I think you got the problem completely. So how do you approach it?

_C_: Let me see. So to swap left and right, I can just use a temp. But then how will I do it for remaining? Oh ya, I could just recurse for the others and do the same.

_I_: Cool. Is there any problem with that approach?

_C_: Hmmm. Yes, if I just swap the left and right recursively, how will I track the old and new tree?

_I_: I am not sure I am following you. What is old and new?

_C_: What I meant is, there will be updated children, I need to swap them and not the old children.

_I_: Yes, correct.

_C_: Ya I can just call this function recursively for left and right and store those values in a variable. I could then update the tree with those variables. This way I can make sure the whole tree is inverted.

_I_: Cool. Anything else you are missing?

_C_: No I think. So it will take O(n) time and O(1) space as I don't use any extra space._**(Notice how proactively the candidate discusses time and space)**_

_I_: I am fine. You can start coding.

_C_: Sure. _**(Talks through the code while coding)**_

```ruby
def invert(node)
  invert(node.left)
  invert(node.right)
  node.left,node.right = node.right, node.left
  return node
end

```

_C_: So I am done. Let me walk you through my code. So for a tree like ..._**(Explains and dry runs with an example)**_

_I_: I guess you are right. Does it work for all cases?

_C_: Hmmm. I guess I'll get Null pointer exception for an empty tree. Let me fix that by adding a null check.

_I_: Now it looks good. Anything else you are missing.

_C_: No, I think other things I have covered like no leaves, one leaf, etc._**(Notice how he calls out each case he considered)**_

_I_: Cool. I am good. Any questions? :)

## Feedback

So what do you think about this interview?

* The candidate clarified the requirements before starting implementation.
* The candidate also froze the requirements by running through a few examples and clarifying his understanding.
* The candidate came up with a working solution without any probing.
* The candidate proactively discussed the time and space complexities.
* While coding, the candidate had a clear vision of what he was doing and where he was going.
* The candidate had a bug in his code, and when asked to check for errors, he found the error and rectified it themselves.

## Conclusion

Interviewing is a completely different skill from coding. Even though you are good at problem-solving, the interview is a setting where the interviewer is trying to decide between hiring you or not. So in addition to coding, you also need to understand the interviewer's perspective so that you make it easy for him to hire you. In this article, I wanted to compare and contrast a good interview vs a mediocre one. Try to practice interview skills separately as the more you practice the better you get at it. You can [reach out](https://kaizencoder.com/about) to me if you need help taking mock interviews.

This article was first published on [http://kaizencoder.com](http://kaizencoder.com/). If you liked this article, please [visit](http://kaizencoder.com) to read more like this or learn more about me!

