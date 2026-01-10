---
title: System Design Interview Tutorial – The Beginner's Guide to System Design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-14T22:46:31.000Z'
originalURL: https://freecodecamp.org/news/system-design-interview-practice-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/youtube-system-design-thumbnail.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: distributed systems
  slug: distributed-systems
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
- name: Microservices
  slug: microservices
- name: System Architecture
  slug: system-architecture
- name: System Design
  slug: system-design
seo_title: null
seo_desc: 'By Charles M.

  System Design is an important topic to understand if you want to advance further
  in your career as a software engineer. Even if you are just beginning your coding
  journey, it''s a good idea to get a head start on learning about system de...'
---

By Charles M.

System Design is an important topic to understand if you want to advance further in your career as a software engineer. Even if you are just beginning your coding journey, it's a good idea to get a head start on learning about system design. 

Early in your career you will mostly just be tested on your coding ability. In higher level interviews, however, there will often be a greater focus on testing your ability and experience at designing applications.

The biggest struggle engineers have with system design interviews is that they are more open-ended and there isn't any single correct answer. This lack of structure can be intimidating, so my goal with this article is to give you a roadmap for navigating these types of interviews with confidence.

What this article will cover:

* What is a system design interview and why they are used
* The main stages of a system design interview
* Example interview problem – Design YouTube

## Video Tutorial

You can also watch this tutorial on YouTube if you like:

%[https://youtu.be/YEwKnGARDZI]

And I've created a playlist of videos on specific topics related to system design and web architecture:

%[https://www.youtube.com/playlist?list=PL_esswHjNwIeiFfVFer8uYly3Zk6YqXd0]

## System Design Interview Overview

At first glance it seems silly to ask somebody to design a huge app like Twitter or YouTube in 45-60 minutes. These apps were designed over a period of years by hundreds of engineers working together, so it's clearly an impossible task to do in a short interview.

There are two main reasons why companies use these types of interviews. The first is, of course, to test your knowledge about the technologies being discussed. They want you to go deep enough to make sure you aren't just throwing buzzwords around without understanding how things actually work. 

The second reason might be more important, though. The system design interview is a way to simulate a realistic scenario where you are working together with the interviewer to determine the best design decision. 

Getting the perfect answer isn't necessarily the most important thing here – it's some of the other things you can show, like:

* How do you handle being challenged? Do you get defensive or take feedback with a positive attitude? Are you stubborn or narrow-minded?
* Do you show knowledge of the various tradeoffs certain design decisions involve? There's a big difference between blindly making a decision and not realizing the consequences, and knowing the pros/cons and accepting the tradeoffs.
* Are you able to effectively communicate and if necessary explain complex technical concepts in an easy to understand way?
* Are you candidate somebody the interviewer would want to work with long term? Even if somebody is a genius, if they are miserable to work with they might not be a good hire.

## Stages of a System Design Interview

In this section you'll learn a general framework for structuring how to handle a problem during a system design interview.

### Clarify the problem and establish design scope

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-106.png)

The first thing you'll want to do after your interviewer gives you the problem is to take a few minutes to ask some clarifying questions and figure out what exactly they are looking for. 

The worst thing you could do here is just start off in the completely wrong direction because you didn't take the time to ask a few questions. You have a limited amount of time during the interview, so you want to make sure you focus on what's important. 

Here are some examples of questions you might ask:

#### What are the use cases / features of the app?

In this article we will be using YouTube as an example. There are hundreds of different features you could design like ad delivery, authentication, recommendation algorithms, comments, video upload, video processing, and many others. 

During an interview you only have time to cover a few of those, so make sure to ask the interviewer questions to figure out what they want you to focus on designing.

#### How many users are expected / what is the likely traffic volume?

The complexity of the system will depend on the amount of traffic it needs to handle, so make sure to gather this information. 

You don't want to over-engineer things if the traffic is relatively low and you also don't want to get stuck with an app that can't scale because you didn't design it properly. 

Ask questions like how many users the app will have, the average amount of data per request, how long data needs to be stored, and how reliable and available does the system need to be?

This step is going to help you beyond just getting more information to work with. You're also showing the interviewer that you understand how to gather information about a vague problem. 

### Determine Rough Capacity Estimates

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-107.png)

Using the information you gathered during the first step, you can begin to make some rough estimates and generalizations for things like storage and bandwidth requirements.

This process will involve some basic math like multiplying the number of users by the average request size and the amount of requests each user is expected to make daily. 

### Create a High Level Design

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-108.png)

Here you want to create a rough architecture for the system. Draw out things like load balancers, web servers, app servers, task queues, database, caching, file storage, and so on. You should include all the core components you need to create the system. 

Make sure to communicate with the interviewer during this stage and check to ensure that you aren't missing anything. While they probably won't tell you directly, they will give you a nudge in the right direction if you forgot about some crucial feature.

### API Design

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-114.png)

This part is almost cheating because you are using the structure of the interview to your advantage to confirm that you are on the right path. 

The interviewer is never going to deliberately lead you down the wrong path, so once you've created your high level design you can start sketching out some rough API endpoints for each component. 

For the YouTube example they might look something like this, depending on which features you are building:

* uploadVideo (userID, video, description, title)
* comment (userID, videoID, comment)
* viewVideo (videoID)
* videoSearch (query)

In some cases you might not need to drill down to this level. If the interview question is very high level like "design Youtube", you can probably skip this part. On the other hand if you get a more focused question like "design YouTube's comment system", it would make sense to go more in depth.

### Create a Data Schema

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-113.png)

At this point you should have a good idea of all the requirements and data needed for the application to work, so now you can plan out how your data is structured. 

Depending on what you are building and the requirements, you'll need to weigh the costs and benefits of things like using a relational vs non-relational database. When modeling your data you'll also want to account for things like potential data partitioning and replication.

### Take a Detailed Look at the Components

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-112.png)

What happens during this section will mainly depend on the feedback of the interviewer. They will probably pick out a few specific components to focus on and ask why you made certain decisions. 

The most important part here isn't necessarily being 100% right. Instead, it's to show that you didn't just blindly make decisions and understand exactly what tradeoffs you were making. 

You should be able to propose alternate design decisions that could have been used and explain why you didn't use them.

## How to Design YouTube

Now that you have a general idea of how a system design interview works and a framework for handling a system design problem, I'm going to show you how to put it all into practice using YouTube as an example.

### Step 1 – Define Problem Scope and Requirements

This will be a high level problem where we implement a few of YouTube's major features without diving too in-depth on any of them. The features to focus on will be:

* Users can upload videos
* Users can view videos
* Users can comment on videos

### Step 2 – Determine Capacity estimates

The two biggest capacity factors in an app handling large amounts of video like YouTube will be storing all that content and bandwidth requirements to deliver the content to users. In this section you'll learn how to make rough estimates for capacity requirements. 

The main focus here is not on being highly accurate, but showing a logical thought process for calculating these numbers based on the information available to you.

In an interview you would be given the data, but in this case I'm using two key pieces of data that YouTube has made public:

* **YouTube creators upload 500 hours of video every minute**
* **YouTube users watch 1 billion hours of video per day**

You can use these numbers to calculate storage and bandwidth requirements with a few assumptions.

#### Bandwidth Calculation

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-92.png)
_Daily bandwidth calculation_

To calculate an estimate for bandwidth, we start with the amount of video watched daily. The key assumption here is how much bandwidth is used per hour watched, as this would depend on the quality of video most users choose to watch. 

The 3 Gigabyte estimate is based on a rough percentage of users watching in standard definition and others choosing HD or 4K, which consume much more bandwidth per hour watched.

The math here is fairly simple: multiply 1 billion hours by the average bandwidth of an hour of video, then divide that by 1000 to convert to terabytes, then divide by 1000 again to get to Petabytes. The final bandwidth estimate is **3,000 PB** used daily.

#### Storage Calculation

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-91.png)
_Step by step calculations for storage_

Based on a few assumptions we can calculate that YouTube will need to store around **2.16** **Petabytes** of new video every day. Here's how we get that number:

* Convert 500 hours to 30,000 minutes of video uploaded per minute
* Each minute of HD video is roughly 50 Megabytes due to having copies of each video in multiple formats. We multiply that by 30,000 minutes and then divide by 1000 to convert to Gigabytes.
* We then take the 1,500GB uploaded per minute and multiply by 60 then 24 to calculate the daily amount of video uploaded. We divide by 1000 again to convert Gigabytes to Terabytes
* Our final total is 2,160 Terabytes uploaded daily or 2.16 Petabytes

### Step 3 – Database Design

For our database we will use a standard relational database like MySQL. The schema will look something like this: 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-93.png)

This design is very simple but has the essentials that you'd need for a basic implementation. It would be a good idea to do some research into the differences between relational and non-relational databases so you understand what kind of situations each excel at and when to use them. 

For certain apps with different requirements a NoSQL database might make sense. Often large systems will have many different services that use different types of databases depending on their needs.

### Step 4 – High Level Design

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-95.png)

That's a pretty complex diagram, so let me break down what's happening:

* **Client** – This could be a user on a mobile app or their computer trying to upload a video, make a comment, or watch a video
* **CDN** – A content distribution network is used to reduce latency and improve reliability when it comes to delivering static content like videos or images. A CDN works by storing content in data centers all around the world so that the content is closer to users. This results in reduced latency because requests travel a shorter distance. There's also an added benefit of content being stored in multiple locations so even if one location can't serve traffic for some reason, another location can.
* **Load Balancers** – A load balancer accepts requests and routes them to servers depending on a number of factors. At YouTube's scale, a single server can't handle all the traffic and you want replication to prevent a single point of failure. The load balancer can check the status of servers and verify they can handle traffic or choose another server that can handle the request.
* **Services** – You can think of this as the app layer of the system. Instead of using a single monolith to handle traffic, we'll use several microservices to handle specific tasks. The second box for each of these services in the diagram represents multiple servers running for each of them to increase reliability. If one replica of the service goes down, there's always another to step in and handle traffic.
* **Data Stores** – When using microservices it is generally best practice for each microservice to own its own data. If one service needs data from another they can access it through an API.
* **Video Upload Process** – Handling the video uploads will involve multiple steps, as trying to handle it synchronously with the app server would be fragile and reduce performance. I'll cover this more in depth in the next section

I don't want to go too in-depth on these individual components because I could write entire articles on any of them if I wanted to explain them fully. 

If you are interested in a more detailed explanation you can check out the system design playlist I linked to above which has videos covering most of these concepts. 

### Step 5 – Go Over Specific Components and Details

At this stage you have a working design. Now let's look at some of the specific components in detail.

#### Video Upload

Video content is the lifeblood of YouTube, and it doesn't exist without it. This means that making it quick and easy for users to upload videos is probably the most important feature. 

Imagine uploading a multi-gigabyte video to YouTube and then seeing the upload fail after 30 minutes when it's 95% done. To prevent this you'll want to support the ability for resuming uploads if the client's connection is lost temporarily. The uploaded video can then be stored with a distributed file system like HDFS. 

Once the upload is complete there's still a lot more to do before the video is ready for users to access. The video needs to be encoded into multiple different quality formats, you need to generate thumbnails, and push copies of the video to the global CDN. 

Again, at any stage one of these processes could fail. To prevent this you'll have a task queue to manage this process and retry the processing attempt if it fails at any stage. 

#### Database Scaling

The database is often the bottleneck of an application. You will probably be tested on whether you understand some of the fundamental concepts around database scaling. This could include caching to handle read requests, sharding, and replication. 

## Conclusion

Hopefully this article has given you a better understanding of what to expect during a system design interview. 

This article mainly focused on the structure of the interview itself rather than the concepts you need to understand to answer the questions given during the interview. 

Two great resources for beginning to learn about that are:

A great article posted here on Free Code Camp News: [https://www.freecodecamp.org/news/systems-design-for-interviews/](https://www.freecodecamp.org/news/systems-design-for-interviews/)

The system design primer repo on GitHub: [https://github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

Both cover just about every major concept you need to know for your system design interview and should put you in a great position for success.


