---
title: Limiting concurrent operations in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T20:37:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-limit-concurrent-operations-in-javascript-b57d7b80d573
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7F50Qc-ysFgy6tCjUyruTA.jpeg
tags:
- name: concurrency
  slug: concurrency
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Maciej Cieślar

  Usually, the machine that executes our code has limited resources. Doing everything
  at once might not only hurt, but can also hang our process and make it stop responding
  altogether.

  When we want to crawl 100 websites, we should cra...'
---

By Maciej Cieślar

Usually, the machine that executes our code has limited resources. Doing everything at once might not only hurt, but can also hang our process and make it stop responding altogether.

When we want to crawl 100 websites, we should crawl, for example, 5 at once, so that we don’t take up all the available bandwidth. As soon as one website is crawled, the next one is ready to go.

Generally speaking, all “heavy” operations should be laid out in time. They should not be executed all-at-once, for better performance and to save resources.

### Implementation

If you are familiar with my previous post about [implementing promises](https://medium.freecodecamp.org/how-to-implement-promises-in-javascript-1ce2680a7f51), then you are going to notice many similarities.

```typescript
class Concurrently<T = any> {
  private tasksQueue: (() => Promise<T>)[] = [];
  private tasksActiveCount: number = 0;
  private tasksLimit: number;

  public constructor(tasksLimit: number) {
    if (tasksLimit < 0) {
      throw new Error('Limit cant be lower than 0.');
    }

    this.tasksLimit = tasksLimit;
  }

  private registerTask(handler) {
    this.tasksQueue = [...this.tasksQueue, handler];
    this.executeTasks();
  }

  private executeTasks() {
    while (this.tasksQueue.length && this.tasksActiveCount < this.tasksLimit) {
      const task = this.tasksQueue[0];
      this.tasksQueue = this.tasksQueue.slice(1);
      this.tasksActiveCount += 1;

      task()
        .then((result) => {
          this.tasksActiveCount -= 1;
          this.executeTasks();

          return result;
        })
        .catch((err) => {
          this.tasksActiveCount -= 1;
          this.executeTasks();

          throw err;
        });
    }
  }

  public task(handler: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) =>
      this.registerTask(() =>
        handler()
          .then(resolve)
          .catch(reject),
      ),
    );
  }
}

export default Concurrently;
```

We register a given task by adding it to our _tasksQueue_ and then we call _executeTasks_.

Now we execute as many tasks as our limit allows us — one by one. Each time adding 1 to our counter called _tasksActiveCount_.

When the executed task finishes, we remove 1 from _tasksActiveCount_ and again call _executeTasks_.

Below we can see an example of how it works.

The limit is set to 3. The first two tasks are taking very long to process. We can see the third “slot” getting opened from time to time, allowing the next task in the queue to be executed.

Always there are three, no more, no less.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MxACL9-7TXYJTpUTQdJIHQ.gif)
_Executing heavy and light tasks with the limit of 3._

You can see the code in the [repository](https://github.com/maciejcieslar/concurrently).

Thank you very much for reading! Can you think of any other way of achieving the same effect? Share them down below.

If you have any questions or comments feel free to put them in the comment section below or send me a [message](https://www.mcieslar.com/contact).

Check out my [social media](https://www.maciejcieslar.com/about/)!

[Join my newsletter](http://eepurl.com/dAKhxb)!

_Originally published at [www.mcieslar.com](https://www.mcieslar.com/limiting-concurrent-operations-in-javascript) on August 28, 2018._

