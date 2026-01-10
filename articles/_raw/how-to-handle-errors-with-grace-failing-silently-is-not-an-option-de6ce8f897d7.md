---
title: 'How to handle errors with grace: failing silently is not an option'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-15T18:09:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-errors-with-grace-failing-silently-is-not-an-option-de6ce8f897d7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eDuyL7l8N39gsDb-KFLtog.jpeg
tags:
- name: clean code
  slug: clean-code
- name: error handling
  slug: error-handling
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rina Artstain

  I’ve never really had much of an opinion about error handling. This may come as
  a shock to people who know me as quite opinionated (in a good way!), but yeah. If
  I was coming into an existing code base I just did whatever they did be...'
---

By Rina Artstain

I’ve never really had much of an opinion about error handling. This may come as a shock to people who know me as quite opinionated (in a good way!), but yeah. If I was coming into an existing code base I just did whatever they did before, and if I was writing from scratch I just did whatever felt right to me at the time.

When I recently read the error handling section in [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/) by Uncle Bob, that was the first time I gave the subject any thought at all. Sometime later I ran into a bug which was caused by some code failing silently, and I realized it might be time to think about it a bit more. I might not be able to change how errors are handled in the entire code base I’m working on, but at least I would be informed on what approaches exists and what the tradeoffs are, and, you know, have an opinion about the matter.

### **Expect the Spanish Inquisition**

The first step of handling errors is to identify when an “error” is not an “error!”. This of course depends on your application’s business logic, but in general, some errors are obvious and easy to fix.

* Got a from-to date range where the “to” is before “from”? Switch the order.
* Got a phone number which starts with + or contains dashes where you expect no special characters? Remove them.
* Null collection a problem? Make sure you initialize it before accessing (using [lazy initialization](https://en.wikipedia.org/wiki/Lazy_initialization) or in the constructor).

Don’t interrupt your code flow for errors you can fix, and certainly don’t interrupt your users. If you can understand the problem and fix it yourself — just do it.

![Image](https://cdn-media-1.freecodecamp.org/images/gMPEtUMvrcUzejIk2Qc1m2yjc-vPWBeLCqAU)
_Photo by [Unsplash](https://unsplash.com/photos/7DITOdv_Uxo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Lance Anderson</a> on <a href="https://unsplash.com/search/photos/expect?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### **Returning Null or Other Magic Values**

Null values, -1 where a positive number is expected and other “magic” return values — all these are evils which move the responsibility for error checking to the caller of the function. This is not only a problem because it causes error checking to proliferate and multiply, it is also a problem because it depends on convention and requires your user to be aware of arbitrary implementation details.

Your code will be full of code blocks like these which obscure the application’s logic:

```
return_value = possibly_return_a_magic_value()if return_value < 0:   handle_error()else:    do_something()
```

```
other_return_value = possibly_nullable_value()if other_return_value is None:   handle_null_value()else:   do_some_other_thing()
```

Even if your language has a built in nullable value propagation system — that’s just applying an unreadable patch to flaky code:

```
var item = returnSomethingWhichCouldBeNull();var result = item?.Property?.MaybeExists;if (result.HasValue){    DoSomething();}
```

> Passing null values to methods is just as problematic, and you’ll often see methods begin with a few lines of checking that the input is valid, but this is truly unnecessary. Most modern languages provide several tools which allow you to be explicit about what you expect and skip those code-cluttering checks, e.g. defining parameters as non-nullable or with an appropriate decorator.

### Error Codes

Error codes have the same problem as null and other magic values, with the additional complication of having to, well, deal with error codes.

You might decide to return the error code through an “out” parameter:

```
int errorCode;var result = getSomething(out errorCode);if (errorCode != 0){    doSomethingWithResult(result);}
```

You may choose to wrap all your results in a “Result” construct like this (I’m very guilty of this one, though it was very useful for ajax calls at the time):

```
public class Result<T>{   public T Item { get; set; }   // At least "ErrorCode" is an enum   public ErrorCode ErrorCode { get; set; } = ErrorCode.None;    public IsError { get { return ErrorCode != ErrorCode.None; } } }
```

```
public class UsingResultConstruct{   ...   var result = GetResult();   if (result.IsError)   {      switch (result.ErrorCode)      {         case ErrorCode.NetworkError:             HandleNetworkError();             break;         case ErrorCode.UserError:             HandleUserError();             break;         default:             HandleUnknownError();             break;      }   }   ActuallyDoSomethingWithResult(result);   ...}
```

Yep. That’s really bad. The Item property could still be empty for some reason, there’s no actual guarantee (besides convention) that when the result doesn’t contain an error you can safely access the Item property.

After you’re done with all of this handling, you still have to translate your error code to an error message and do something with it. Often, at this point you’ve obscured the original problem enough that you might not have the exact details of what happened, so you can’t even report the error effectively.

On top of this horribly unnecessarily over-complicated and unreadable code, an even worse problem exists — if you, or someone else, change your internal implementation to handle a new invalid state with a new error code, the calling code will have **no way of knowing** something which they need to handle has changed and **will fail** in unpredictable ways.

### If At First You Don’t Succeed, Try, Catch, Finally

Before we continue, this might be a good time to mention that code failing silently is not a good thing. Failing silently means errors can go undetected for quite a while before exploding suddenly at inconvenient and unpredictable times. Usually over the weekend. The previous error handling methods **allow** you to fail silently, so maybe, just maybe, they’re not the best way to go.

![Image](https://cdn-media-1.freecodecamp.org/images/uJ6t46B9KpmPOCj1t9YGx48xEZcv-LSX-XdH)
_Photo by [Unsplash](https://unsplash.com/photos/iSTs6Lcu-Ek?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Scott Umstattd</a> on <a href="https://unsplash.com/search/photos/spanish?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

At this point, if you’ve read [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/) you’re probably wondering why anyone would ever do any of that instead of just throwing an exception? If you haven’t, you might think exceptions are the root of all evil. I used to feel the same way, but now I’m not so sure. Bear with me, let’s see if we can agree that exceptions are not all bad, and might even be quite useful. And if you’re writing in a language without exceptions? Well, it is what it is.

> _An interesting side note, at least to me, is that the default implementation for a new C# method is to throw a NotImplementedException, whereas the default for a new python method is “pass”._

> _I’m not sure if this is a C# convention or just how my Resharper was configured, but the result is basically setting up python to fail silently. I wonder how many developers have spent a long and sad debugging session trying to figure what was going on, only to find out they had forgotten to implement a placeholder method._

But wait, you could easily create a cluttered mess of error checking and exception throwing which is quite similar to the previous error checking sections!

```
public MyDataObject UpdateSomething(MyDataObject toUpdate){    if (_dbConnection == null)    {         throw new DbConnectionError();    }    try    {        var newVersion = _dbConnection.Update(toUpdate);        if (newVersion == null)        {            return null;        }        MyDataObject result = new MyDataObject(newVersion);        return result;     }     catch (DbConnectionClosedException dbcc)     {         throw new DbConnectionError();     }     catch (MyDataObjectUnhappyException dou)     {         throw new MalformedDataException();     }     catch (Exception ex)     {         throw new UnknownErrorException();     }}
```

So, of course, throwing exceptions will not protect you from unreadable and unmanageable code. You need to apply exception throwing as a well thought out strategy. If your scope is too big, your application might end up in an inconsistent state. If your scope is too small, you’ll end up with a cluttered mess.

My approach to this problem is as follows:

**Consistency rulezzz.** You must make sure that your application is always in a consistent state. Ugly code makes me sad, but not as much as actual problems which affect the users of whatever it is your code is actually doing. If that means you have to wrap every couple of lines with a try/catch block — hide them inside another function.

```
def my_function():    try:        do_this()        do_that()    except:        something_bad_happened()    finally:        cleanup_resource()
```

**Consolidate errors.** It’s fine if **you** care about different kinds of errors which need to be handled differently, but do your users a favor and hide that internally. Externally, throw a single type of exception just to let your users know something went wrong. They shouldn’t really care about the details, that’s your responsibility.

```
public MyDataObject UpdateSomething(MyDataObject toUpdate){    try    {                var newVersion = _dbConnection.Update(toUpdate);        MyDataObject result = new MyDataObject(newVersion);        return result;     }     catch (DbConnectionClosedException dbcc)     {         HandleDbConnectionClosed();         throw new UpdateMyDataObjectException();     }     catch (MyDataObjectUnhappyException dou)     {         RollbackVersion();         throw new UpdateMyDataObjectException();     }     catch (Exception ex)     {         throw new UpdateMyDataObjectException();     }}
```

**Catch early, catch often.** Catch your exceptions as close to the source at the lowest level possible. Maintain consistency and hide the details (as explained above), then try to avoid handling errors until the very top level of your application. Hopefully there aren’t too many levels along the way. If you can pull this off, you’ll be able to clearly separate the normal flow of your application logic from the error handling flow, allowing your code to be clear and concise without mixing concerns.

```
def my_api():    try:        item = get_something_from_the_db()        new_version = do_something_to_item(item)        return new_version    except Exception as ex:        handle_high_level_exception(ex)
```

Thanks for reading this far, I hope it was helpful! Also, I’m only starting to form my opinions on this subject, so I’d be really happy to hear what your strategy is for handling errors. The comments section is open!

