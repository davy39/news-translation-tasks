---
title: Get the most out of Ruby by using the .select .map and .reduce methods together
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-30T06:01:48.000Z'
originalURL: https://freecodecamp.org/news/ruby-using-the-select-map-and-reduce-methods-together-a9b2af30804b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1WIbhb82wmieRfp3XL2Ysg.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Declan Meehan

  You should absolutely never ever repeat yourself when writing code. In other words,
  do not repeat yourself twice. To be clear — do not write something which has been
  explained already.

  This is called tautology, and when writing code ...'
---

By Declan Meehan

You should absolutely never ever repeat yourself when writing code. In other words, do not repeat yourself twice. To be clear — do not write something which has been explained already.

This is called tautology, and when writing code it should be avoided at all times. For instance, wouldn’t it have been nice instead of reading this lengthy paragraph if I just used the three powerful words “never, repeat, yourself”?

Well that’s what I’m going to show you how to do with Ruby’s .select .map and .reduce(or .inject) methods.

### Example

Let’s suppose you are looking at a dictionary full of employee’s names, job titles, and salaries. Let’s also imagine that you wanted to find out the total amount that the company was spending on developers’ salaries. Now, without using a single method in Ruby, you would most likely write your code out something like this:

```ruby
people = [
  {
    first_name: "Gary", 
    job_title: "car enthusiast", 
    salary: "14000" 
  },  
  {
    first_name: "Claire", 
    job_title: "developer", 
    salary: "15000"
  },  
  {
    first_name: "Clem", 
    job_title: "developer", 
    salary: "12000"
  }
]
person1 = people[0][:job_title]
person2 = people[1][:job_title]
person3 = people[2][:job_title]
total = 0
if person1 == "developer"
    total += people[0][:salary].to_i
end
if person2 == "developer"
    total += people[1][:salary].to_i
end
if person3 == "developer"
    total += people[2][:salary].to_i
end
puts total
```

Wow — that is a lot of lines to write to find only three people. Imagine if the company employed hundreds of people!

Now if you know a bit about loops, then the next easiest step would be to write an each method to put all the salaries together. This might only take up five or six lines but check this out!

```ruby
puts people.select{|x| x[:job_title] == "developer"}.map{|y| y[:salary].to_i}.reduce(:+)
```

![Image](https://cdn-media-1.freecodecamp.org/images/CVi6LVbCoOsskAzyQdVJGQ2GzBZq68XOExMJ)
_It may look confusing but let's break it down into pieces._

You’ll notice every method begins and ends with a curly bracket. This can be used instead of the do and end commands if it is a single line block.

```ruby
{} == (do end) #for single-line blocks only
```

### .select

Let’s start with the .select method. We create a variable (x) and iterate over every method in the people array. It then checks with a boolean expression if the key of (:job_title) is equal to the “developer” string. If the boolean returns true, then the select method places the hash that returned true into a new object.

### .map

The map method is used for creating a new array that does not affect the array it is looping through. I used this method to create a new variable (y), and then used that variable to grab the value of the key (:salary). Then, finally, I turned that value from a string into an integer.

### .Reduce

This one probably looks the most confusing so let's expand it a bit.

```ruby
.reduce(0){|sum, indv| sum + indv} #is the same as .reduce(:+)
```

The reduce method creates a new variable which you set the value equal to in the first parentheses (0). You then create two new values (sum and indv) of which one is the sum that you add the individual salaries to.

I hope that explains it well! Please let me know if you have any questions.

