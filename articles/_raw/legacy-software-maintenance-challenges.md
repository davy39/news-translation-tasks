---
title: Why Your Legacy Software is Hard to Maintain - and What to Do About it.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-28T17:06:30.000Z'
originalURL: https://freecodecamp.org/news/legacy-software-maintenance-challenges
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c5f740569d1a4ca31cb.jpg
tags:
- name: software
  slug: software
seo_title: null
seo_desc: 'By Alfrick Opidi

  Believe it or not, some organizations still rely on legacy software to carry out
  operations even though newer and more versatile options are available. We know that
  “old is gold”, but legacy applications cannot glitter forever. As su...'
---

By Alfrick Opidi

Believe it or not, some organizations still rely on legacy software to carry out operations even though newer and more versatile options are available. We know that “old is gold”, but legacy applications cannot glitter forever. As such, these old and outdated programs have become hard to maintain.

Recently, the U.S. Government Accountability Office (GAO) gave a [report](https://www.gao.gov/products/gao-19-471#summary) that pointed out the most critical federal legacy systems that need to be modernized. This is because they are based on antiquated programming languages, are prone to security loopholes, and are difficult to maintain.

Are you in the same shoes?

In this article, I’m going to talk frankly about the challenges you'll face when maintaining legacy software applications, and how you can overcome them.

## Legacy systems are inefficient

Software maintenance is important – it helps enhance the efficiency of the product and narrows the margin for error. Without sufficient maintenance, an application can become inefficient and difficult to operate.

First of all, maintaining [a legacy system](https://www.freecodecamp.org/news/conquer-legacy-code-f9e23a6ab758/) can be difficult because the code used is old when compared to the code used in any modern software. Old code usually tends to be bulky, lengthy, and incompatible with most modern systems.

For example, JavaScript arrow functions, which were introduced in ES6 in 2015, offer developers a way to write shorter and cleaner function syntax, which is easier to maintain.

```javascript
let total = (x, y) => x + y;

/* This arrow function is a shorter form of:
let total = function(x, y) {
  return x + y;
};
*/

console.log(total(5, 2) ); 
// 7

```

## High maintenance costs

Another challenge facing most legacy systems is the high cost of maintenance, which may be out of reach for most enterprises. 

For example, according to the GAO report mentioned above, the U.S. government planned to spend more than $90 billion in 2019 on IT services, most of which went towards maintaining aging systems.

Furthermore, as technology is evolving, compliance is becoming a major issue for the protection of consumer-facing applications. Achieving compliance with legacy systems is time-consuming and expensive. It will not happen as quickly compared to new applications who are often compliant by default. It also requires a lot of testing to ensure a legacy infrastructure is compliant with the given regulations.

The cost of maintaining a legacy system often increases with time, as it slowly becomes obsolete due to technological enhancements. Also, modification of an existing system is a risky venture, which requires a lot of time and resources.

## Lack of sufficient skill sets

For legacy software to be maintained, you need a developer conversant with its operations. However, most developers are future-proofing their applications with new technologies. So, getting someone who can work with an old system can be a challenge.

In some cases, you might need to re-train developers on how the legacy system works, which increases a company’s operating costs. 

Furthermore, managing and controlling changes occurring in the software can be difficult. A lot of time and effort is required to keep the systems operational, which is expensive and time-consuming.

## Incompatibility with other IT solutions

Currently, there are modern tools that can be used to enable fast and smooth maintenance of software. However, most legacy IT infrastructure is incompatible with such solutions, which complicates their maintenance. 

If the features in a legacy system are not compatible with those of new IT solutions, developers may find it difficult to integrate them into their environments.

The difficulty of introducing new features to legacy systems also adds to the challenges in their maintenance. Since most legacy systems break easily, trying to restructure and make them more maintainable may not work as expected.

## Solutions to the challenges

To compete favorably in today’s dynamic IT landscape, legacy technologies need modernization. Updated legacy applications lead to more user productivity, reduced maintenance costs, and more helpful experiences.

According to recent research by [Avanade](https://www.avanade.com/en/media-center/press-releases/it-modernization-research), modernizing IT systems can lead to a revenue growth of about 14%. Therefore, choosing [different software modernization options](https://www.scnsoft.com/services/application/modernization) could lead to significant benefits to your business.

It’s important to note that software should not be declared obsolete just because it’s old. Some of the ‘old’ software may still contain rich features, which can be useful to the optimal functioning of an application.

Therefore, to overcome the challenges of maintaining aging software, developers can opt to refactor the source code of the system. This way, they can use clean and modern code that is reusable and easy to debug.

In refactoring, you alter your software system to enhance its internal structure. But you don't interfere with the external behavior of the code. This way, the features of the software are optimized due to the code's internal improvements.

When refactoring legacy code, updates and modifications should be sufficiently tested to avoid breakages and poor functioning of the application. For example, regression tests can be done to ensure that everything is working as desired.

Additionally, where resources permit, developers can opt to rewrite the entire source code of the software, while employing modern programming approaches.

If you want to continue maintaining your legacy code without breaking it, you can use any of the following three methods:

1. Identifying change points in the code
2. Isolating your code
3. Wrapping the code

Let's talk about each of the methods.

### Identify change points in the code

As pointed out earlier, maintaining legacy code can be challenging. Sometimes the issue can be caused by a section that has been poorly programmed. Therefore, you can overcome this by identifying a location that can allow you to change the application's behavior without altering the source code. 

For example, let's say you have the following JavaScript code in a legacy application that connects to a database:

```js
export class DataConnection {
     //some code here

  connector() {
    // some code to connect to database
  }
}
```

If you want to run some tests on the above code but the the **connector()** method is causing problems, you can identify where to modify the code behavior without affecting the source code.

In this case, you can extend the **DataConnection** class and stop it from establishing a connection to an actual database:

```js
class FakeConnection extends DataConnection {
  
    connector() {
    // solve the issues of making calls to DB
        
    console.log("Establishing a connection")
  }
}
```

Consequently, after modifying the code behavior without affecting the source code, you can run tests on the code and maintain it without any problems. 

### Isolate your code

Another technique that can allow you to maintain your legacy code easily is to isolate and make any changes on a different environment. You just need to identify an insertion point where you can call that changed code from the existing legacy code. 

Here is an example:

```js
class BooksData {
  // some code here

  addBooks(books) {
    for (let book of books) {
      book.addDate()
    }

    // some code here

    booksRecords.getNumberOfBooks().add(books)
  }

  // some code here
}
```

Let's say you want to optimize the **books** reference in the above legacy code, but **addBooks()** is giving you problems. 

So, you can isolate the code in another new method, like **newBooks().** 

Then you can run tests on this new method successfully because it is separate from the rest of the code. Afterwards, you can include a call to the new method in the existing, non-changed code. This way, there'll be minimal changes and minimal risks to the legacy code. 

Here it is:

```js
class BooksData {
  // some code here

  newBooks(books) {
    // some smart and testable logic to optimize books
  }

  addBooks(books) {
    const newBooks = this.newBooks(books)

    for (let book of newBooks) {
      book.addDate()
    }

    // some code here

     booksRecords.getNumberOfBooks().add(books)
  }

  // some code here
}
```

### Wrap the code

If you want to make changes that should take place before or after the existing code, wrapping it can also be another solution. 

You can achieve this by giving the old method you intend to wrap a new name, adding a new method with the same name and signature just like the old method, and calling the new method from the new method. Lastly, you should place the new logic before or after the previous method call. 

With the new logic, you can run tests or make any changes you want – without affecting the source code. 

For example, here is the code we used previously:

```js
class BooksData {
  // some code here

  addBooks(books) {
    for (let book of books) {
      book.addDate()
    }

    // some code here

    booksRecords.getNumberOfBooks().add(books)
  }

  // some code here
}
```

Here is how to solve the problem through wrapping:

```js
class BooksData {
  // some code here

  addBooks(books) {
    // some smart logic to get books
    this.addMoreNewBooks(moreBooks)
  }

  addMoreNewBooks(books) {
    for (let book of books) {
      book.addDate()
    }

    // some code here

    booksRecords.getNumberOfBooks().add(books)
  }

  // some code here
}
```

## Conclusion

Although modernizing antique software is complicated, demanding, and risky, the results are usually worth the risk. Continuing to rely on legacy IT systems is the same as continuing to use the post office to send an urgent message, while an email could do the trick at the click of the button.

Furthermore, as a programmer, do you equip yourself with modern coding skills? Or, do you still rely on old approaches?

For example, in the exciting world of JavaScript programming, we’ve witnessed a surge of frameworks, like React and Angular, which are defining the future of the language. Spending some time learning about them could prevent you from falling into obsoleteness.

Do you agree?

