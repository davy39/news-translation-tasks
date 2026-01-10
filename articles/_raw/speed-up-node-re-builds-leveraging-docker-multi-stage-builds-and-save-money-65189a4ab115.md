---
title: How to speed up Node re-builds by leveraging docker multi-stage builds
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-20T01:52:58.000Z'
originalURL: https://freecodecamp.org/news/speed-up-node-re-builds-leveraging-docker-multi-stage-builds-and-save-money-65189a4ab115
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Nsp3DqX0_RyNxggv
tags:
- name: Docker
  slug: docker
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By John Standish

  Reinstalling npm dependencies can be a wasteful use of time and money. Depending
  on the size of your project, this can take several minutes. In my personal experience,
  I’ve seen npm install take upwards of 5 minutes. Now, if you have...'
---

By John Standish

Reinstalling `npm` dependencies can be a wasteful use of time and money. Depending on the size of your project, this can take several minutes. In my personal experience, I’ve seen `npm install` take upwards of 5 minutes. Now, if you have separate stages (Gate, CI, different environment branches) to your pipeline, this waiting time gets even worse. All jokes aside from the picture below, waiting is pricey!

![Image](https://cdn-media-1.freecodecamp.org/images/1*NhZ8Ts1Xe0SlreW2Ljzo6g.png)
_[https://www.reddit.com/r/ProgrammerHumor/comments/6s0wov/heaviest_objects_in_the_universe/](https://www.reddit.com/r/ProgrammerHumor/comments/6s0wov/heaviest_objects_in_the_universe/" rel="noopener" target="_blank" title=")_

### Waste is expensive, very expensive

#### TL;DR

It’s a significant amount of money (~**$9,918/yr per developer**) and time (18,792 minutes per year or 13.05 days per year) that’s wasted waiting for dependencies to install while our code goes through its pipeline. These numbers are an average of 4 check-ins per day. On the low end, waiting for the gate, it’s **~$3,132/yr per developer**. _See calculations below for where I got those numbers._

Let’s do some quick math to see why 5 minutes is a big problem. Assume you have a Gate, and a CI build for your 2 environments (Staging and Production). Each stage requires you to start a clean build.

So let’s add up how long we’re waiting for `npm install` to complete:

Build time: 1 minute  
Gate: 5 minutes  
Staging CI: 5 Minutes  
Production CI: 5 Minutes  
**NPM Wait Time: 15 minutes**  
**Total Build Time: 18 minutes**

Okay, so 18 minutes doesn’t seem that bad. That’s a coffee break, and we all love coffee. But that 18 minutes is idle time, time waiting for something to go out the door.

Now let’s expand that math a bit and multiply by a small team (4 developers), and for fun, we’ll figure an average amount check-ins and an hourly rate. Time is money, right? The average amount of check-ins is what I’ve seen in my day job, and your numbers may vary.

Build Time: 3 minutes  
NPM Wait Time: 15 minutes  
Developers: 4  
Avg. Check-Ins: 4  
Hourly Rate: $30 (your hourly rate may be higher)

**Gate Wait Time: 96 minutes** **(Gate wait time X Developers X Avg Check-Ins)**  
**Gate Cost: $48 (Gate Wait Time in hours x Hourly Rate)**  
**Total Time: 288 minutes (Build and NPM time X Developers X Avg Check-Ins)**  
**Cost: $144/day (Total Time in hours X Hourly Rate)**

So we’re looking $144/day of idle time, or $720/week, or **$37,584/yr**. And that’s waiting for our software to ship! On the low end, if we check-in our code and wait for the gate, that’s **$12,528/yr**. YIKES! The yearly cost was based on 261 American working days in a year ([https://hr.uiowa.edu/payroll/2015-fiscal-year-payroll-calendar](https://hr.uiowa.edu/payroll/2015-fiscal-year-payroll-calendar))

### Let’s cache and build this thing!

#### TL;DR

Here are my instructions on how to run. [https://github.com/jstandish/cached-node-module-build-example/blob/master/DOCKER_BUILD.md](https://github.com/jstandish/cached-node-module-build-example/blob/master/DOCKER_BUILD.md)

Alright, we’ve established that waiting for things is expensive. So as such, we should try and reduce how long we spend on `npm install` steps. We should only re-run `npm install` when the `package.json` file changes. By selectively running this we can significantly reduce the amount of time for new Gate/CI/CD builds from several minutes to less than a minute (depends on the size of your project).

#### Phase 1 — Create a cache stage

Our first step will be to create a multi-stage `dockerfile`. This will allow us to copy in the `package.json` file and only run a certain stage if that file has changed.

#### Phase 2 — Create a build stage

The next step will be to create the next stage which will pipe a command to `npm`. This is done using the `ENTRYPOINT` statement in your `dockerfile`. This will execute the given command pipe in any arguments. We are using a docker image that has `Chromium` installed already; this will allow us to run Chrome Headless for our unit tests.

Here is the complete dockerfile:

#### Phase 3 — Build the image

Now that we have our `dockerfile` set up, let’s build it. You will need to do this every time the files change, but the time required to copy your new files is trivial because docker will skip subsequent layers that haven’t changed. Woohoo!

This took about **2** **minutes.** But this could take longer depending on your internet connection, disk speed, CPU, etc.

Any build after our initial `docker build` will take less time because we will only re-run `npm install` if the package.json file has changed!

#### Phase 4 — Build the code!

So now let’s build our code inside the node-build-test image. We’ll specify a mount point so we can copy our build output to it. This will allow us to extract the compiled code from the dockerized environment! I am using a forked angular project as an example, but you can use this now for any project.

The build time took about 45 seconds. But that was compiling our code, not waiting for `npm install`. YES!

And we now have our compiled files!

![Image](https://cdn-media-1.freecodecamp.org/images/1*vx3LTl-eZWIT0eZwxB7tyA.png)

#### So, it’ll only be 45 seconds for all subsequent builds?

Yes! Because the `npm install` step is completely skipped, because the `package.json` file hasn’t changed, you’ll gain the benefits. If you change the `package.json`, you’ll incur the same time penalty you would have anyways.

### So how much time/money did we save?

So let’s go back to our calculation that we did previously, and now subtract our `npm install` wait time. We’ll keep the build time in there because you can’t get away from that.

Build Time: 3 minute  
Developers: 4  
Avg. Check-Ins: 4  
Hourly Rate: $30 (your hourly rate may be higher)

**Gate Time: 16 minutes** **(Gate wait time X Developers X Avg Check-Ins)**  
**Gate Cost: $8 (Gate Wait Time in hours x Hourly Rate)**  
**Total Time: 48 minutes (Build time X Developers X Avg Check-Ins x Environments)**  
**Cost: $24/day (Total Time in hours X Hourly Rate)**

So let’s look at that over a day, week, and year.

**Day: $24**  
**Week: $120**  
**Year: $6,264**

#### And how much did we save for our team of 4 developers?

The below is the format of (**previous amount — new amount**). And yes, it’s a lot of savings over the year!

**Day: ($144 - $24) = $120**  
**Week: ($720 - $120) =$600**  
**Year: ($37,584** - **$6,264) = $31,320**

### Conclusion

I hope you have enjoyed seeing how utilizing a docker multi-stage build can save you a significant amount of time, as well as money. Docker multi-stage builds are very powerful and can enable you to ship and build faster.

If you want to play around with this, please clone my GitHub repository and have fun!

[https://github.com/jstandish/cached-node-module-build-example](https://github.com/jstandish/cached-node-module-build-example)

Thanks for reading!

[https://www.instagram.com/john.does.code](https://www.instagram.com/john.does.code)

