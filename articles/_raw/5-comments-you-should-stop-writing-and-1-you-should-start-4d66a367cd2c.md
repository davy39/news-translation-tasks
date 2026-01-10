---
title: Five code comments you should stop writing // and one you should start
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T22:44:58.000Z'
originalURL: https://freecodecamp.org/news/5-comments-you-should-stop-writing-and-1-you-should-start-4d66a367cd2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PIFH2fl9dk8fvWJy8ynvgA.png
tags:
- name: clean code
  slug: clean-code
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alon Kiriati

  With examples from your favorite and most popular open source projects — React,
  Angular, PHP, Pandas and more!

  The correlation between code quality and comments

  One of the first things we were taught in college was that comments are e...'
---

By Alon Kiriati

With examples from your favorite and most popular open source projects — React, Angular, PHP, Pandas and more!

### The correlation between code quality and comments

One of the first things we were taught in college was that comments are essential. We were also taught that there is a correlation between code quality and the number of comments a code has — the more comments you have, the better your code is. We were trained to believe that comments tell the story of the program we write, and that they express whatever code can’t provide. We learned that human language is best read by human, while machine language is best read by machines.

Moreover, teaching that wasn’t enough and we were “punished” for handing in assignments without comments by a few points being deducted from our grades. If you somehow managed to avoid the human checks, your lack of comments was caught by scripts which were designed to check that.

### Maybe the correlation is inverse

As I gained more experience, I realized that not only is it that the opposite may be true — it’s possible that there is an inverse correlation between good code and the number of comments the code has. There are two main reasons why this can happen:

1. Too many times comments are just an excuse for writing bad code. Instead of writing good code, programmers believe that if they write dirty code with some weird hacks, and describe it with a 5 lines of comments — that the code is readable and well written. I beg to differ — the code is actually still bad. If your colleague needs to read a long commented story in order to understand it, then you’re doing it wrong. If your code is not self explanatory, it is best to improve it and not use comments to describe it.
2. Comments decay over time, which makes them wrong and misleading. They are true only when written, and even then they can’t be enforced efficiently. Over time, people will inevitably make logic changes, change types, and move things around. Some of them will notice the comment that should be changed, and some will not. Even if somehow you find a way to set a very rigid discipline around updating comments when code changes, this will break the first time you perform an automatic refactor. Think of a refactor that adds a parameter to a core function that is used more than 250 times — do you really want to go and manually change all those comments?

![Image](https://cdn-media-1.freecodecamp.org/images/7YrMu1H2zUOi2iRAJC9k38eT3ARmfCC9HDhw)
_[www.imagewishes.com](http://www.imagewishes.com" rel="noopener" target="_blank" title=")_

### What are the most common comments you should try to avoid?

All this doesn’t mean you should stop writing comments right away or try to reduce the number of comments you have at any cost. I would also not recommend going over your code, and trying to clean all of the unnecessary or misleading comments — this will take too much time and your time is better used elsewhere. Instead, I would recommend to be more thoughtful before you add your next comment and ask yourself these three questions:

1. Is this comment really required and what value does it add?
2. Is there a way to improve the code so this comment is unnecessary?
3. Am I only covering my a** by adding this comment?

To help you out, I’ve identified the top 5 bad comments I’ve seen over time — these types of comment should raise a red flag before you add it. I used some very common open source projects to get some examples. Don’t get me wrong, I don’t think these project are poorly written. On the contrary, those are my favorite projects. But nothing in life is perfect; all code can be improved.

#### 1. Stating the obvious

These are comments that explain what your code does. You’ve probably seen some of these around:

An example from [react.js](https://github.com/facebook/react/blob/master/scripts/jest/noHaste.js#L5):

```js
getHasteName() {
   // We never want Haste.
   return null;
}
```

And another one from [vscode](https://github.com/Microsoft/vscode/blob/master/src/cli.js#L11):

```js
// Avoid Monkey Patches from Application Insights// Avoid Monkey Patches from Application Insights
bootstrap.avoidMonkeyPatchFromAppInsights();
// Enable portable support
bootstrap.configurePortable();
// Enable ASAR support
bootstrap.enableASARSupport();
// Load CLI through AMD loader
require('./bootstrap-amd').load('vs/code/node/cli');
```

Believe it or not, people reading your code are coders themselves. It is highly probable that they work at the same company as you or on the same project. They have some context, and are pretty smart (hopefully… if you believe you are surrounded by idiots, you might want to consider updating your Linkedin). They can read code, even without footnotes. If your variables, functions, and classes have meaningful names, then don’t clutter them with pointless explanations that will be outdated in the next code change or refactor.

Disclaimer: Like many others, I have comment-blindness. I ignore comments and will most likely never notice there was a comment which should be updated when changing or refactoring the code.

Back to the example — what happens if we removed all of the comments in the code above? would it really be much harder to read?

#### 2. Explaining your code

If your code is clean and uses the right level of abstraction, you don’t need to explain what it does. If you still find yourself explaining the code, it might be the result of some habit you picked up over the years. You might want to consider getting rid of it, or have to endure a code that is not self-expressive

Look at this code from [react.js](https://github.com/facebook/react/blob/master/dangerfile.js#L35):

```js
if (!existsSync('./scripts/rollup/results.json')) {
  // This indicates the build failed previously.
  // In that case, there's nothing for the Dangerfile to do.
  // Exit early to avoid leaving a redundant (and potentially      confusing) PR comment.
  process.exit(0);
}
```

Wouldn’t this be cleaner if we refactored it like this:

```js
if (buildFailedPreviously())
  process.exit(0);
```

Another common example can be naming; either functions, variables, or classes. Good naming is one of the hardest things to do, but that doesn’t mean we need to unconditionally raise a white flag, and use comments to describe what our code does. Look at this code from [php](https://github.com/php/php-src/blob/master/main/alloca.c#L226):

```php
struct stack_control_header
{ 
  long shgrow:32;    /* Number of times stack has grown.  */
  long shaseg:32;    /* Size of increments to stack.  */
  long shhwm:32;     /* High water mark of stack.  */
  long shsize:32;    /* Current size of stack (all segments).  */
};
```

If you pass it around and then try to use it, you might not immediately understand what shgrow, shaseg and other fields are. What if we wrote it this way:

```
struct stack_control_header
{
  long num_of_time_grown:32;
  long size_of_inc:32;
  long high_water_mark:32;
  long current_size:32;
};
```

See? Much better. The reader can better understand what each field does without needing to jump to the struct definition and read the comments.

#### 3. Long comments

Long comments that are used to describe every decision you’ve made. These comments may explain each line in detail: why you chose to write it that way, what were the alternatives, what is the code history that led to it. It made it really hard to read the code fluently, and it can cause the reader further confusion. Ultimately, causing more damage than good. Try to keep comments as short as you can with minimal context.

If the reason you add a comments is because the code is hacky or complicated, then make it readable by refactoring it — not by adding another confusing layer. Choose better names, break functions to do one thing, and use abstractions. Whatever you need to make your code more readable, do it with code, not comments.

An example from [vue.js](https://github.com/vuejs/vue/blob/dev/src/core/observer/scheduler.js#L36):

```js
// Async edge case #6566 requires saving the timestamp when event listeners are
// attached. However, calling performance.now() has a perf overhead especially
// if the page has thousands of event listeners. Instead, we take a timestamp
// every time the scheduler flushes and use that for all event listeners
// attached during that flush.
export let currentFlushTimestamp = 0
// Async edge case fix requires storing an event listener's attach timestamp.
let getNow: () => number = Date.now
// Determine what event timestamp the browser is using. Annoyingly, the
// timestamp can either be hi-res (relative to page load) or low-res
// (relative to UNIX epoch), so in order to compare time we have to use the
// same timestamp type when saving the flush timestamp.
if (inBrowser && getNow() > document.createEvent('Event').timeStamp) {
// if the low-res timestamp which is bigger than the event timestamp
// (which is evaluated AFTER) it means the event is using a hi-res timestamp,
// and we need to use the hi-res version for event listeners as well.
getNow = () => performance.now()
}
```

This will probably require more refactoring to move the focus from comments to the actual code.

#### 4. Titles, headers and other “beautifications”

Writing pretty code is essential, but that doesn’t mean you should decorate it like a book. We occasionally tend to creates blocks of code and give them titles, in order to differentiate one block from another. Let’s see this example from [angular.js](https://github.com/angular/angular.js/blob/master/lib/grunt/utils.js#L134):

```js
...
build: function(config, fn) {
var files = grunt.file.expand(config.src);
  // grunt.file.expand might reorder the list of files
  // when it is expanding globs, so we use prefix and suffix
  // fields to ensure that files are at the start of end of
  // the list (primarily for wrapping in an IIFE).
  if (config.prefix) {
    files = grunt.file.expand(config.prefix).concat(files); 
  }
  if (config.suffix) {
   files = files.concat(grunt.file.expand(config.suffix));
  }
  var styles = config.styles;
  var processedStyles;
  //concat
  var src = files.map(function(filepath) {
    return grunt.file.read(filepath);
  }).join(grunt.util.normalizelf('\n'));
  //process
  var processed = this.process(src, grunt.config('NG_VERSION'), config.strict);
  if (styles) {
  processedStyles = this.addStyle(processed, styles.css, styles.minify);
  processed = processedStyles.js;
  if (config.styles.generateCspCssFile) {
    grunt.file.write(removeSuffix(config.dest) + '-csp.css', CSP_CSS_HEADER + processedStyles.css);
  }
}
//write
grunt.file.write(config.dest, processed);
grunt.log.ok('File ' + config.dest + ' created.');
fn();
...

```

If you find yourself doing this, your function undoubtedly does more than one thing. It is probably too long, explicit, and lacks some levels of abstractions. In the example above, the function has at least four parts: fetch files, concat, process, and write. Each of these parts appears with detailed implementation, that creates long functions that are also hard to read. This can be fixed by expanding each block to a different function.

```js
build: function(config, fn) {
  files = this.fetch_files(config)
  var src = this.concat(files)
  var processed = this.process(src)
  write(processed, config)
}
```

As code grows, the “headers” are not bold enough. This is where we get creative and add additional “beautifications” to our comments — line of asterisk, dashes, equals sign, etc. Take a look at this code from [pandas](https://github.com/pandas-dev/pandas/blob/master/pandas/core/algorithms.py):

```py
...
# --------------- #
# dtype access    #
# --------------- #
def _ensure_data(values, dtype=None):
...
def _reconstruct_data(values, dtype, original):
...
def _get_hashtable_algo(values):
...
# --------------- #
# top-level algos #
# --------------- #
def match(to_match, values, na_sentinel=-1):
...
def unique(values):
...
def isin(comps, values):
...
# --------------- #
# select n        #
# --------------- #
class SelectN(object):
...
class SelectNSeries(SelectN):
...
class SelectNFrame(SelectN):
...
# ------------ #
# searchsorted #
# ------------ #
def searchsorted(arr, value, side="left", sorter=None):
...
# ---- #
# diff #
# ---- #
_diff_special = {
...
}
def diff(arr, n, axis=0):
...
```

The module includes a list of functions, variables, and classes all mixed together in one bundle with coupled dependencies. This could be avoided using one simple rule — if you feel that you need titles to gather functions or classes together, this would be a good time to break your code to smaller parts.

If your class has “groups” of method from different types — each group of functions should be a class of its own. If your file has too many classes or functions that require grouping, it’s time to break each group to its own file.

The code above could be much easier to understand and navigate if we break it to files. By doing this we also decouple the dependencies, so we can import only the code we need:

```py
date_acces.py:
def _ensure_data(values, dtype=None)
def _reconstruct_data(values, dtype, original)
def _get_hashtable_algo(values):
top_level_algos.py
def match(to_match, values, na_sentinel=-1):
def unique(values):
def isin(comps, values):
selectn.py
class SelectN(object):
selectn_series.py
class SelectNSeries(SelectN):
selectn_frames.py
class SelectNFrame(SelectN):
search_sorted,py
def searchsorted(arr, value, side="left", sorter=None):
diff.py
_diff_special = {
...
}
def diff(arr, n, axis=0):
...
```

#### 5. /* TODO: */

from [react.js](https://github.com/facebook/react/blob/master/packages/react-dom/server.browser.js#L14):

```
// TODO: decide on the top-level export form.
// This is hacky but makes it work with both Rollup and Jest
module.exports = ReactDOMServer.default || ReactDOMServer;
```

Whether it’s /* TODO */, [#TODO](https://paper.dropbox.com/?q=%23TODO), or <! — TODO →, one thing is for sure — no one will ever do it. Yes, even if you add a name next to it and assign it to someone. The assignee will leave the company long before they’ll fix this issue. I’ve never heard anyone anywhere saying something like: “hey folks, we have some free time, why don’t we fix all of the todos in our code?” (If you have some time for that, then your company has a bigger problems, but we’ll leave that one for another post).

![Image](https://cdn-media-1.freecodecamp.org/images/5ynOP9pwo8quY5qsMsN8P5U8nlxpbDQo7xWV)
_www.xkcd.com_

The main problem with todos is that it’s not only an excuse for writing a bad code, but also it’s unclear to the reader what is the state of that code — Is it going to be changed soon? Was this already fixed and the author forgot to remove the comment? Is there a pull request waiting that should fix this issue? Did the code author leave it for us to fix? — Make a decision, either fix it, or accept the consequences.

The one exception is if you are working on a feature and want to break your code changes into multiple commits. In that case, add the todo comment and add your task number/link to a real task in your task management system. This way, you can track it and make sure it is on your roadmap. If for some reason you decided not to handle the task, don’t forget to also delete the comment

### Finally, here are the comments you should write

A rule of thumb — use comments to answer “Why?” and the code to answer “How?”

Even if the code is self explanatory, the reason we decided to take one approach is not always clear, especially if the reader has no context. It might be due to product requirements, system limitation, efficiency or just a bad code that you didn’t have time to refactor.

Using comments to highlight why you did something the way you did is good, but keep it short and focused. If you want to document, use a wiki; if you want talk broadly about your decision making use a doc; if you want to log the code changes history, that’s what git comments are for.

A good example from [linux](https://github.com/torvalds/linux/blob/master/lib/xz/xz_dec_bcj.c#L337):

```c
/*
Apply the selected BCJ filter. Update *pos and s->pos to match the amount of data that got filtered. NOTE: This is implemented as a switch statement to avoid using function pointers, which could be problematic in the kernel boot code, which must avoid pointers to static data (at least on x86).
*/
static void bcj_apply(struct xz_dec_bcj *s, uint8_t *buf, size_t *pos, size_t size)
```

**If there is one thing you should take from this post — use code to tell your story and comments to turn “WTF** ?” **to “OHHHH… ?**” 

![Image](https://cdn-media-1.freecodecamp.org/images/q1VxxU9Mei14U0INJ4pfOSgIydZPscPlRLvc)
_www.giphy.com_

**Thanks for spending a few minutes of your time. If you liked it, feel free to ? or respond with /*comments*/**

**-Alon**

**_Special thanks to:_**

* **[Rina Artstain](https://www.freecodecamp.org/news/5-comments-you-should-stop-writing-and-1-you-should-start-4d66a367cd2c/undefined) _and [Keren](https://www.freecodecamp.org/news/5-comments-you-should-stop-writing-and-1-you-should-start-4d66a367cd2c/undefined) for proofreading, reviewing this article and giving awesome technical feedback_**

