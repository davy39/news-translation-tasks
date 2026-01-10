---
title: API error codes are prehistory — try this instead
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T09:36:18.000Z'
originalURL: https://freecodecamp.org/news/api-error-codes-are-prehistory-try-this-instead-b3abd156f9fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*29vCdubMr2uQk5laP7Lmiw.jpeg
tags:
- name: api
  slug: api
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pakal de Bonchamp

  A cautionary tale

  Once upon a time, a young girl observed her mother, who was unwrapping a freshly
  bought piece of beef for roasting. The mother cut the extremities of the meat out.

  “Mommy, why do you do that?” the young girl ask...'
---

By Pakal de Bonchamp

### A cautionary tale

Once upon a time, a young girl observed her mother, who was unwrapping a freshly bought piece of beef for roasting. The mother cut the extremities of the meat out.

“Mommy, why do you do that?” the young girl asked.

“It gives a better taste,” the mother replied, as she put the meal in the oven.

“How is it so?”

“I don’t remember, go ask your grand-mother, she taught me all these kinds of tips and tricks.”

The child was curious, and ran to the nearby house of her grandmother.

“Grand-mommy, do you know why cutting the sides of roast beef makes it better?”

“It has to be with the flow of the juice,” the grandmother replied.

“Can’t we just punch holes with a fork instead?”

“My mother has always prepared them so, and for sure she was a great cook.”

The child was not only curious but also perseverant, and ran to the home where her elder lived. She narrated what her mother and grandmother had told her, and repeated her question.

The elder burst in laughter.

“I did always cut the ends of my roast beef, but only because my oven was waaaayyy too small for a whole one.”

This little tale, which exists in [infinite variations](https://www.snopes.com/fact-check/grandmas-cooking-secret/), makes an important point about human life. Old habits die hard, even when they haven’t made sense for decades (if ever). And computer science, though evolving at a fast pace, is quite prone to this type of harmful tradition.

![Image](https://cdn-media-1.freecodecamp.org/images/ISagFl1mcQBDqHbbHGrgUZDMmwy9E7FQOtjV)

### Error handling

Take error handling, for example. We are deeply used to HTTP status codes, to small unix “errnos”, to lengthy windows error codes… and our APIs are filled with custom numbers, indicating problems with inputs, or with SQL operational errors, or with access permissions…

The first, low level, programming languages — including C and Fortran — had very rudimentary data types. That’s why they handled errors as mere integers, that they could compare, switch-case, lookup as array indices, and transmit painlessly. And that’s why they ended up using 0 (boolean False) to indicate all successes, and non-zero integers (boolean True) to indicate errors — something not deeply intuitive to ordinary mortals.

But what do we expect from errors in our everyday modern, high level languages ? That they be:

* **explicit**, so we know what they mean without asking the whole web everytime
* **deeply hierarchical**, so that we can refine error cases without breaking current software, and fallback to generic treatments when too specific errors are encountered
* **contextualized**, so that additional data may accompany the error, and detail what exactly went wrong and why

This is the way exceptions are implemented in many modern languages. There are hierarchies of classes with (hopefully) clear meanings. Each has different instance attributes in different branches in these hierarchies, for example filenames, field names, and origin OS errors. And those instances drag with them tons of information, including tracebacks and their per-frame local variables.

But when it’s time for the error to cross the boundaries of this specific process, of this specific language? Error codes are amongst the worst supports for this.

What does “Error 0x29273363833” mean? You have no idea. You can’t subdivide this error into more precise cases. If you want more context information, you’ll have to fetch it somewhere else.

And you have little clue what the closest parent error code could be. True, some systems advocate rudimentary fallback behaviours — for example if you encounter an unknown HTTP 478 error, you’re supposed to handle it as an HTTP 400. But it is still a bit too coarse-grained for lots of cases, and once you have used all the numbers of an error class, you’re out-of-luck.

### **So what do I propose?**

Just map exception types to their closest JSON-compatible representations.   
Which happen to be… sequences of identifiers.

Ladies and gentlemen, I present to you, a bunch of **status slugs**:

* [“Exception”, “LookupError”, “KeyError”]
* “error|functional|invalid_input|missing_value”
* “error|technical|connectivity|mysql.database_unreachable”
* [“success”]
* [“success”, “instance_found_in_cache”]

As you can see, whether we use lists or strings doesn’t matter much ; even the term “slug” must not be taken too rigidly, having underscores or capital letters in them is harmless.

The **important take-away** **messages** are that these slugs are:

* quite explicit
* quite easy to map to language-specific exceptions
* quite easy to match in the error handling dispatcher.

Dots should be reserved to qualify, and thus differentiate, same-name exceptions provided by different packages. An example here is “cuteforms.Invalid” vs “validator.Invalid”.

The cherry on the cake is that status slugs may be used to distinguish success cases too, like the “HTTP 2XX” family advocated it for the web.

So here is the first point I wanted to make: **use status slugs to announce operation results**.

**Error handling is at the very core of software robustness and a pleasant user experience, so it deserves more than assembly-level data types**. Let’s just stop using poor error dispatching based on integers, on single slugs, or — worst of all — on booleans.

![Image](https://cdn-media-1.freecodecamp.org/images/swBxJBfvHeKOw87J-k1doVYZAi0FYdJGPl6N)
_Still better error handling than “An error occurred, plz check logs”…_

The second point I wanted to make about error handling is: **be ambitious**.

Lots of protocols define castrated error structures — “if it’s enough for me, it’s enough for others”. And developers end up adding their own error handling system. Sometimes SUCCESS responses of initial protocol are stuffed with their own error structures, when ERROR responses leave no room for customization (looking at you, XML-RPC).

So if you end up, one day, having to specify your own error format — which is always a pity, but sometimes unavoidable — **think big**.

What do we expect from a response format?

* For sure we need status slugs, to see precisely which kind of success or error occurred.
* We may also need translated messages for UI display.
* Most probably we need untranslated messages too, as they are much more convenient to seek in source codes, or to translate frontend-side.
* We need room for status-specific trees of data, so that all relevant information may be provided in a machine-processable way.
* We probably also need support for multiple — or rather recursive — data structures, like when several fields of a web form each have their own reason to be rejected.
* We might have to convey partial successes, for example when not all user account data could be retrieved from directories. We might have to convey and partial failures, for example when an authoritative answer could not be fetched, but some cached data is returned just in case it helps you.

Here is an example of an (almost) one-size-fits-all StatusPack structure:

> {  
>  status_slugs : list of slugs for success/error dispatching, mandatory field  
>  data: data tree with contextual information (results, invalid input fields...)  
>  traceback : for dev mode only, might include frames with local variables  
>  nested_statuses: optional list of StatusPack structures  
>  message_translated: displayable string  
>  message_untranslated: string or [string template, parameters] pair  
> }

This structure should cover the use cases mentioned above, thanks to the malleability provided by the “nested_statuses” field.

If you deal with **microservices**, chaining these status packs, and displaying them properly user-side — **especially the traceback** — might save you days of logs investigations.

And if you want to obfuscate your errors, then fine. But there is no need to specify error codes yourself. Just create **hashes** of your “status_slugs” and automatically generate the whole listing of available errors by introspecting your codebase.

![Image](https://cdn-media-1.freecodecamp.org/images/IjhQTfo7JkC9BOqM1fDtlEfpWs9nNIv0ipHk)
_That feeling when your code handles all kinds of user and network errors flawlessly_

The last point I am emphasizing is: **be kind to API consumers.**

Ensure that your consumers **know** when an error occurs. Ensure that your consumers also **know** what to do, especially programmatically, in this case.

* Silent errors are Hell’s antechamber. Deleting a non-existing account **must** return an error. But provide a gentle “strict=False” parameter to such operations, so that users may issue unimportant calls without embarrassing themselves with errors.
* Having a “ValueError” on a form field that users submitted (input error), or on a variable which they know nothing about (server error), are totally different cases. These should end up as different status slugs. When your API acts as a relay between users and other APIs, this analysis might be very hard to achieve, especially if remote APIs have poor error reporting. But try, anyway.
* Be clear, in your documentation, about the meaning of error classes, and what actions are expected from consumers. Typically, technical errors mean “if you retry later, it might work.” On the other hand, functional errors mean “your workflows or inputs are wrong, blindly retrying won’t help.” Your hierarchy of status slugs might need to be fine-tuned, with love and attention, over several years.

These two ideas — **status slugs and StatusPack structures** — are certainly not the epitome of error handling, but they represent a sure step forward in terms of precision and evolvability.

I’d like to hear the other error fields, or other handling strategies, that API developers around here might have come up with. **Please share your innovations and hard-earned lessons!**

_**Edited on 2018/09/07:** Fix typos, and precise the idea behind the “slug” term._

_**Edited on 2019/06/22:** Precise the StatusPack "data" field_ 


