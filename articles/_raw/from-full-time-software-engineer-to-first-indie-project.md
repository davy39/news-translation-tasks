---
title: 'One Step at a Time: My Journey from Full-time Software Engineer to First Indie
  Project'
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2024-04-01T19:33:07.000Z'
originalURL: https://freecodecamp.org/news/from-full-time-software-engineer-to-first-indie-project
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Blog-Banner-Final.png
tags:
- name: 'Career development '
  slug: career-development
- name: Entrepreneurship
  slug: entrepreneurship
- name: personal development
  slug: personal-development
- name: software development
  slug: software-development
seo_title: null
seo_desc: "Introduction: The Spark of Indie Hacking\nI’m Gaël, a 25-year-old software\
  \ engineer who’s been working in a startup environment in Southeast Asia for a few\
  \ years. \U0001F30F \nWorking remotely has its perks, and while hopping from one\
  \ exotic location to anothe..."
---

## Introduction: The Spark of Indie Hacking

I’m Gaël, a 25-year-old software engineer who’s been working in a startup environment in Southeast Asia for a few years. 🌏 

Working remotely has its perks, and while hopping from one exotic location to another, I’ve been nurturing a little dream: to kick-start my journey as a solopreneur.

I genuinely love my job—there’s a certain thrill in startup life that I think everyone should experience at least once. Sure, it’s a rollercoaster of highs and lows, but it's where I've learned the ropes of product development and caught the bug for making things people love (and will hopefully pay for!). I often think of coding as adult LEGO—endless possibilities and just plain fun. 🤓

After two years of nomadic life, I chose to plant my feet firmly on the ground to strike a better work-life balance and finally carve out time for my side projects. 

But here’s the kicker: settling down didn’t magically make time appear. Between the 9-5 grind and weekend exhaustion, I struggled to find the energy and belief needed to start something of my own.

## Choosing the Right Tools for the Journey

Embarking on this solopreneur journey, I decided to harness the tools and technologies I was already familiar with: HTML, CSS, Tailwind, JavaScript, along with React and Next.js for creating websites. 

This choice was not just about comfort but was also about applying best practices in web development that I've learned over a few years of experience.

In the following sections, I'll explain why I chose these particular technologies. I'll also provide guidance on how you can select the most suitable tools for your own projects, balancing learning curves, productivity, and project requirements. 

Expect to find practical tips and lessons from my hands-on experience, which you can apply to enhance your coding skills or streamline your development process.

## Realizing the Need for Change

Until recently, my daily routine was disordered. I juggled work with late-night phone scrolling sessions until 1-2 AM, only waking just in time for a hurried breakfast before starting my day. 

Frequent use of food delivery apps led to overeating and unhealthy habits, which, despite my overall good life, I knew wasn’t sustainable. 

I was trapped in a cycle, fearing that cutting back on my late nights would reduce my life to just work, work, and work. 💻

Then, something clicked a month ago. Motivated by all the recommendations I've seen about going to the gym, I contacted a personal trainer and started my first few sessions. Initially skeptical about lifting weights, I was surprised by the surge in energy it brought me.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/CleanShot-2024-03-26-at-09.17.21@2x.png)
_"Talking to my therapist today" - @levelsio on X (Twitter)_

This burst of energy triggered a chain reaction: I began paying more attention to my diet, choosing healthier, lighter meals. Sleep, too, became a priority. Influenced by the insights from "Why We Sleep" I transformed my sleep routine, targeting eight hours a night. This shift turned my mornings from a rush into a peaceful, productive time. 😴

Now, a month later, these practices have almost become natural. Waking up earlier, I feel more energized, and I've discovered precious time in the morning before work.

### How Improved Health Boosts Coding Productivity

For those on a coding journey or balancing work with learning new skills, I cannot stress enough the importance of good sleep and regular exercise. These aren’t just lifestyle choices – they are essential tools for enhancing your cognitive function and focus.

After integrating better sleep and exercise into my routine, I noticed a significant improvement in my coding productivity. I was able to learn faster, stay focused for more extended periods, and tackle complex problems with more clarity. It felt like unlocking a cheat code for my brain!

Coding is an exciting yet demanding journey. With the additional energy gained from these changes, you'll be more equipped to face the challenges and joys of learning how to code.

## Taking the First Step: BooksByMood

The concept for BooksByMood had been developing in my mind for months, inspired by Mood2Movie, an app developed by [Marc Lou](https://twitter.com/marc_louvion). 

The idea of finding books based on your mood captivated me, and I envisioned a platform with my own twist on design and suggestions. This marked the beginning of my indie project journey with BooksByMood. 📚

Getting started on this new journey was daunting. My Twitter feed was full of stories of polished apps and good earnings, which heightened my stress and anxiety about starting. At that time, I didn't fully realize that we all have to start somewhere, and even the well-known people out there started at the beginning one day. 

To manage my expectations and focus, I established clear, achievable goals:

* To create a straightforward website centered around a single, compelling feature.
* To keep the website free, ensuring accessibility and user engagement (IMO, also easier to get started with–particularly as a 1st project).
* To dedicate a week to learning promotion techniques, aiming to drive traffic to the site.

These goals weren’t just milestones – they were my commitment to myself to prove that I could bring an idea to fruition and attract visitors. 🎯

### How I Chose My Technical Stack

As mentioned earlier, I utilized technologies I was proficient in: HTML, CSS, JavaScript, along with Tailwind for styling and Next.js for the framework. I chose this stack for its familiarity and efficiency.

I specifically opted for Next.js due to its convenient features:

* server-side rendering and static site generation, leading to improved website performance
* the file-based routing system
* various optimizations such as website navigation using the `<Link>` component or the `<Image>` component
* it's great for SEO
* overall it helps craft a better user experience

This stack allowed me to rapidly prototype and deploy, enhancing the site's performance without additional effort.

**Takeaways:** Stick to technologies you know well when validating an idea quickly. This approach helps you move faster and focus on the project's core value. That's why you can find many solopreneurs online using the same technologies for years (for example, [Pieter Levels](https://twitter.com/levelsio) is using HTML, CSS, JS (with JQuery) and PHP for years).

## App Development Process and Challenges

The journey of developing BooksByMood was iterative, starting with a basic, barely functional version. 

I encountered several challenges, such as sourcing reliable book data and crafting a user-friendly interface. Overcoming these obstacles required research, trial and error, and continuous iteration.

### Challenge 1: Finding Reliable Books Data

Finding a dependable source for book data was unexpectedly challenging.

I initially wanted to use some APIs. Unfortunately, Goodreads closed its API on December 8th, 2020. OpenLibrary was not bad, but the data needed to be more consistent. Google Books API was alright, but I would have also curated manually in the end, and sometimes some info could have been better.

This made me realize that it's hard to find a good books API out there (probably due to Amazon owning Goodreads and making sure it's hard for competitors to have good data as they do).

There was one thing I knew: it'd be complex to satisfy everyone with the recommendations, but I could do my best. My best was to ensure that what was recommended was well rated by the community (for example, it had a good rating on Goodreads).

You may wonder what will happen in the future, if the website is growing? In that case, it'll definitely need improvement. But, for a first release, it does the trick!

**Takeaways:** When facing a challenge on a new project, always take your time to consider all options and find the right balance between shipping fast, quality and reliability. 

As an example, I'm 95% sure that curating books manually in JSON files with the help of AI has been a great choice. It resulted in shipping in a reasonable time, only showing books liked by the community, and controlling the data (for example, cover, title, description, tags, authors, and so on).

### Challenge 2: Designing a user-friendly interface

As a full stack developer who's been working on the backend for a while, designing an appealing front end was my second major hurdle. Ensuring the site was not only functional but also aesthetically pleasing was crucial for user engagement.

I'm still in the process of learning about design, and it's far from perfect. But I discovered [Dribbble](https://dribbble.com/) and it's been a great place to get inspiration. Also, I've been using [Excalidraw](https://excalidraw.com/) to sketch an initial layout version showing how I'd like to organize the information.

**Takeaways:** For non-designers, drawing inspiration from design-focused platforms like Dribbble can be incredibly helpful. Combining this with UI component libraries, like [DaisyUI](https://daisyui.com/), can significantly enhance the design process, making it more effective.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Build-in-Public-Day-1.png)
_Initial sketch of BooksByMood on Excalidraw (shared for my 1st day of #buildinpublic)_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/CleanShot-2024-03-30-at-15.56.46@2x.png)
_1st version of BooksByMood_

## Releasing the App

With the extra time my new morning routine afforded me, I devoted 1-2 hours each weekday and additional weekend time to developing BooksByMood. After a week of focused effort, I opted for a soft launch: I added the project on Twitter by updating my bio link.

The following day marked the beginning of more assertive promotion across various platforms, including Twitter, Reddit, and HackerNews. ✍️

**Takeaways:** Feel free to release your project everywhere you can. It can sound scary, but you never know what will happen. Doing that will help you in many ways, such as starting to attract visitors, getting feedback, getting backlinks, and so on. There's nothing to lose!

![Image](https://www.freecodecamp.org/news/content/images/2024/03/CleanShot-2024-03-28-at-21.52.59@2x.png)
_BooksByMood Homepage_

## Learning and Growing: Early Lessons from the Journey

### Personal and Business Lessons

It might sound a bit cliché, but these points have genuinely resonated with me:

* **Believe in Yourself**: Doubt was a constant companion, but taking the leap showed me the importance of faith in my ability to turn an idea into reality.
* **Ship That Idea:** After all, there could be only positives in doing so. Releasing a product, no matter how small, is a victory in itself.
* **Building Publicly Is Rewarding**: Engaging with the Indie Hackers community has been a blast. Their support and encouragement have been pivotal, making the process not just about building a product but also about being part of an inspiring collective.
* **Believe in the Internet’s Magic**: Sharing my project on HackerNews was a leap into the unknown. To my astonishment, we hit the first page, and the influx of visitors exceeded my expectations. Indeed, the internet can work wonders, turning small actions into significant impacts.

### Technical lessons

On the technical front, the project has been a rich source of learning:

* **Choosing the Right Stack**: Leveraging familiar technologies like Next.js and React facilitated a smoother development process and quicker iterations. This really underscored the importance of choosing the right tools for the job. I've said it many times in this article: _Use what you know_. Don't try to overthink using the latest shiny technology. I'd advise you to focus on your product, not how it's being built.
* **Data Handling and AI Utilization**: The challenge of sourcing reliable book data forced me to consider solutions, including using AI for content curation. This experience highlighted the need for flexibility and creativity in problem-solving. Sometimes, in tech, you'll not find exactly what you want, and you'll have to evaluate potential tradeoffs to find alternatives.
* **Design for the User**: As a backend-focused developer, delving into front-end design was challenging. But prioritizing user experience and employing design resources like Dribbble for inspiration proved crucial in creating an engaging interface. Also, don't be too worried about your design. Your first version will probably be "ugly," but over time and iterations, you'll start having something visually pleasing. Everything takes time!
* **Iterative Development**: Start with a minimal viable product with only one focused feature. It's tempting for a developer to add many features, such as a dark mode, a user account, fancy filters, and so on, but that's unnecessary. Instead, use your technical skills to make that one feature work perfectly.

To wrap up this reflection, I can’t emphasize enough the satisfaction of crafting a project, releasing it, and seeing people using it. It’s an amazing experience that I recommend to everyone. If you’ve been sitting on an idea, stop overthinking and start building it now. 🚧

## Looking Ahead: The Road to Indie Hacking

I plan to stay committed to the indie hacking path for the upcoming months, balancing it alongside my 9-5 job. 

A vast landscape of knowledge awaits me, especially in areas like design and marketing, where my experience is limited. Objectively, I know it's not gonna be easy. Yet, the idea of acquiring new skills is exciting. 🎨

The Indie Hackers community has been a goldmine of insights, with members generously sharing their tips and success stories. This collective wisdom, along with a wealth of books and resources, will continue to guide and inspire my journey. 🔖

In the coming months, my focus is on continuous learning and building. I aim to diversify my projects, incorporating paid features to explore different business models and market needs.

Regarding the tech stack, I plan to stick with my current tools, which are versatile enough to meet most of my needs. While I'm open to integrating new libraries like [NextAuth](https://next-auth.js.org/) for streamlined authentication processes, my primary focus will be learning marketing. Understanding and getting better at marketing is crucial for any indie hacker, as it's often required to transform a side project into something bigger.

Whether it leads to success or failure, every step forward is one step toward. I'm excited to see where this path will take me and to share the journey's story with you all.

**Takeaways:** Your journey should be one of continuous iteration and exploration. While developing your project, never underestimate the power of marketing—it's essential for gaining traction and turning your ideas into reality. To realize your full potential, embrace both the technical and business sides.

## Conclusion: An Invitation to Join the Journey

As this chapter of my journey unfolds, I invite you to come along. I'd love to navigate the ups and downs of indie hacking together.

[Join me on Twitter](https://twitter.com/gaelgthomas) where I share real-time updates, insights, and milestones of this journey, all in the hope of inspiring some of you to embark on your own adventures. 👀

## Explore BooksByMood

Curious about what I’ve been working on? Check out BooksByMood, my first indie project that helps you find books based on your mood. 👇

%[https://booksbymood.com/]


