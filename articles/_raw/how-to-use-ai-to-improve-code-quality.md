---
title: How You Can Use AI to Improve Your Code Quality
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-22T13:57:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-ai-to-improve-code-quality
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/AICodeQuality--1-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: coding
  slug: coding
- name: 'self-improvement '
  slug: self-improvement
seo_title: null
seo_desc: "By Shane Duggan\nAs a software developer, I've always tried to write flawless\
  \ code. Great code is not just functional – it should also be elegant, efficient,\
  \ and robust. \nBut let's be honest – the journey towards code perfection can sometimes\
  \ feel lik..."
---

By Shane Duggan

As a software developer, I've always tried to write flawless code. Great code is not just functional – it should also be elegant, efficient, and robust. 

But let's be honest – the journey towards code perfection can sometimes feel like an uphill battle. Or more often than not, a chore not worth pursuing. And with the huge advances in AI lately, it would be unfortunate not to use what's available to its full advantage.

Now what if you could have a digital assistant tirelessly working by your side, analyzing every line of code, catching bugs and vulnerabilities before they rear their ugly heads, suggesting improvements that elevate your work from good to exceptional?

Well, my friends, you can supercharge your coding skills if you know how to use these new AI tools effectively.

In this article, I want to share with you the six most common ways I've been leveraging AI to enhance my code quality. It's been a game-changer, unleashing new levels of efficiency, accuracy, and creativity in my development process. So let's jump in and see how you can do the same.

### A Disclaimer Before We Start

As it currently stands, I wouldn't recommend using AI to code out your projects in full. I've tried my hand at several projects, and you'll quickly find that the results are usually underwhelming.

Where AI doesn't let you down is in being your programming assistant. You should still be the captain of the ship, and steer the direction of your AI. When it comes to menial and maintenance tasks, such as improving code quality as we'll talk about here, that's where AI currently shines.

So with that out of the way, let's get started. 

## Ways to Use AI When Writing Code

### #1 – Idea Generation

I'll be the first to admit that I don't always come up with the best solutions for a coding problem. I can recall too many times that I've worked on a programming task for hours, only to hit a wall, and then have to consult a colleague or Stack Overflow to get new ideas.

It's only once I receive this external input from friends or forums that I can dig myself out of the mental block and continue with new ideas. But this usually takes time (and often someone else's time, too), which is precious as a programmer.

So I turned to AI to help me out. Even outside of programming, I've been a huge advocate that one of the healthy uses of AI is for idea generation – and it's not different for programmers.

One of the great ways to get over a mental block is to ask ChatGPT for suggestions. If you describe your problem in full, it usually does a good job and figuring out what the next step could be. Just remember to be specific in your prompts, and it helps to include some of your code snippets.

Here is an example of me asking it the question from [this Stack Overflow thread](https://stackoverflow.com/questions/76247438/how-to-convert-data-into-text-while-web-scraping), and it gave a pretty helpful response:

_"The error you're encountering is because the `player.find()` method is returning `None` for some elements, which means it couldn't find a match for the specified class. You need to handle these cases where the element is not found to avoid the `AttributeError`. Additionally, you can use the `pandas.read_html()` function to simplify the process of extracting table data from the HTML."_

Personally, I think it's a great suggestion! Certainly would be enough to get me back on track.

I will emphasize that you should take the ideas more-so then the code ChatGPT might suggest wholesale. ChatGPT did suggest code snippets from the above question, and in general the code snippets provided will work. But it's better to err on the side of caution and be accountable for the code you're putting out.

### #2 - Leveraging AI for Code Reviews

The next great way I've been using AI is in reviewing my code. This is especially useful for newer programmers who are trying to find their footing, and don't have a complete grasp of what's right or wrong and the best practices to follow.

I mainly suggeset this for newer programmers, as we already have tools such as Application Performance Monitoring Tools (APMs) that can give you a good indication of your code quality on larger applications. But when you're a newer dev working on smaller projects, AI is a great way to get quick and insightful code reviews.

If I was able to obtain personalized feedback of my code when I was first picking up coding, I'm sure my learning productivity and overall code quality would've been much more concrete. I hate to even think about what my code looked like in the early days!

There are tons of great tools for this. One of my favourites is [Rankode](https://www.rankode.ai/). They provide personalized reports to you that highlight your strengths, areas of improvement, and an overall assessment of your programming skills. It's a great way to track your growth as a programmer and keep any poor coding habits at bay.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-76.png)
_Rankode's AI Code Quality Reviews_

AI tools like these are going to be essential at driving up the overall quality of code from programmers.

### #3 - AI-Assisted Code Completion

Now, I've already discussed idea generation with AI, and also mentioned that I'm against taking code from ChatGPT or other AI tools wholesale. So this point is a little different.

Oftentimes when I have concept in my head, such as binary search or merge sort, I might have some trouble turning the theory of these concepts into actual code as a new programmer. So, instead of trying to dig myself into a hole of misguided code, a better alternative is to turn to AI to give myself a good picture of what's required.

This is where AI and tools like ChatGPT do a good job, creating snippets of code in isolation. You'll be able to get a pretty good idea of the structure of binary search, merge sort, and other concepts that you want to put down in code.

For example, I asked ChatGPT 

_"I'm trying to learn binary search. I understand the theory but would like to write it in code. Could you give me an example with explanations of what that might look like?"_ 

This is what I got:

```python
def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the target element.
    
    Arguments:
    arr -- A sorted list of elements.
    target -- The element to be found.
    
    Returns:
    The index of the target element if found, or -1 if it doesn't exist.
    """
    low = 0                   # Initialize the lower bound of the search range
    high = len(arr) - 1       # Initialize the upper bound of the search range

    while low <= high:        # Repeat the process until the range is valid
        mid = (low + high) // 2    # Calculate the middle index

        if arr[mid] == target:     # Check if the middle element is the target
            return mid

        if arr[mid] < target:      # If the middle element is smaller, narrow the range to the upper half
            low = mid + 1
        else:                      # If the middle element is larger, narrow the range to the lower half
            high = mid - 1

    return -1               # Target element was not found


# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11

result = binary_search(sorted_list, target_element)
if result != -1:
    print("Element", target_element, "found at index", result)
else:
    print("Element", target_element, "not found in the list.")

```

Along with tons of explanations. Now, I can use this code as a basis, switch to a fresh code editor, and try it out for myself (Again, if you really want to learn, resist copying this code). If I ever hit a wall again and I can't seem to continue, I have a perfectly annotated code snippet to refer to.

It's a great way to act as a guideline for your code and ensure that you're not straying off the path.

### #4 - Bug Detection

Another concrete application for AI in improving code quality is by easing a universal pain known to programmers - bug fixing.

There are tons of tools for these, including the new and refreshed [Github Copilot](https://github.com/features/copilot) that has been supercharged by AI. It acts as your built-in AI assistant, offering suggestions and maintaining code quality as you go.

We know all too well the feeling of being kept up all night just due to a single, minuscule bug. Well, that's going to change for the better with the help of AI, which is perfect for newer programmers or junior developers working on small-scale projects without the luxury of a QA team.

%[https://www.youtube.com/watch?v=4RfD5JiXt3A]

And along with the improvement of code quality, it also reduces the likelihood of vulnerabilities in your code that might slip in especially if you're not an experienced programmer. 

Overall, I just feel much more assured about my project's code quality knowing that I have an additional layer of checks and auditing with AI.

### #5 - AI-Powered Performance Optimization

This is sort of implied based on the previous points we've discussed. But I can't overstate it. Again, rather than resorting to industry tools like APMs that the majority of programmers do not have access to, you can now optimize your code without spending lots of money.

Learning how to leverage AI for performance optimization is a great way to ensure that the code you are putting out is of higher quality. Simply checking back with an AI tool on whether your implementation of a method or function is using the best runtime is a great way to raise the bar of your coding quality.

For example, I wanted to check the performance of one of my functions, so I asked ChatGPT:

_"My function is running slowly, can you give me any possible optimizations?"_ (While pasting the following code)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

And this is what I received:

_"Certainly! Here's an optimized version of the bubble sort algorithm with explanations:_

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to track if any swaps are made in the current pass
        swapped = False
        
        # Last i elements are already in place, so no need to iterate over them
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swaps were made in the current pass, the array is already sorted
        if not swapped:
            break
    
    return arr
```

_Explanation of optimizations:_

* _Introduced a `swapped` flag: This flag is used to track whether any swaps were made in the current pass. If no swaps occur, it means the array is already sorted, and we can terminate the sorting process early. This optimization helps in cases where the input array is already partially or fully sorted._
* _Reduced the range of inner loop: In the original implementation, the inner loop always iterates over the entire array, even if the last few elements are already sorted. By reducing the range of the inner loop to `n-i-1`, we avoid unnecessary iterations over the sorted elements in each pass._
* _Early termination: Once the `swapped` flag remains `False` after a complete pass, we can break out of the outer loop because it indicates that the array is already sorted."_

Not a bad response at all! Of course this is just a simple example. But applying this tactic throughout the development of an app or project will definitely add up to make a difference.

I've used this extensively, especially when looking at chunks of code in isolation. It's a great way to pick up on your poor implementation practices and find more efficient solutions. A simple prompt into ChatGPT to check whether your code is optimal is all you need!

### #6 - AI-Driven Documentation

While this one doesn't directly relate to the standard of your code, it definitely plays a big part when working collaboratively.

When working on projects through Github, it's important that everybody is on the same page. That comes as a result of having clear and concise documentation that everyone on the team can understand. I can't count the number of times I've struggled through a new code base due to the lack of documentation.

With AI, developers are able to put out higher quality docs and user guides. AI tools are able to flesh out any explanations, correct typos and wrong sentences, and evaluate the effectiveness of the documents as a whole.

I've even had some fun with some of my documentation, creating custom images and [AI-generated icons](https://www.mikestuzzi.com/ai--logo-generators/) to beautify the guides. While these didn't play a part in improving the code quality immediately, they definitely play a part in making the docs more digestible which translates to more comprehensible programming.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/aidocwriter.gif)
_An AI Doc Writer. Credits: BetterProgramming.pub_

## How Else Has AI Helped Me?

Like many developers and software engineers out there, I have also begun to turn toward [remote work](https://breathingtravel.com/best-sites-to-your-dream-remote-job/), working exclusively through GitHub and emails. In this case, AI has been a godsend in helping make sure I'm up to date with all my tasks, programming and non-programming related.

There are tons of ways AI can [improve your productivity](https://www.freecodecamp.org/news/ai-assistants-for-productivity/) in general, with AI notes, writers, and more. If you haven't been using AI to supercharge your workflows, I'd highly recommend getting on it!

## Conclusion

To wrap up, those are the top 6 ways AI has been a great help for improving my code quality.

And I really can't emphasize it enough: the difference of coding while backed with AI makes me feel like I'm blazing through programming tasks now. 

For beginner programmers, you can use it to help you learn and expose yourself to a variety of programming practices. But, I'll say it again: **there is no value in copying AI-generated code wholesale.** Use it as a means to improve and power your own skills, but nothing more.

If you enjoyed reading this article, you can find out more on what's going on in AI through my [Byte-Sized AI Newsletter](https://bytesizedai.beehiiv.com/). There are tons of exciting stories of what people are building in the AI space, and I'd love to hear from you. Alternatively, following me on Twitter is your best bet.

Happy programming and I look forward to how you're using AI as your new programming superpower!

