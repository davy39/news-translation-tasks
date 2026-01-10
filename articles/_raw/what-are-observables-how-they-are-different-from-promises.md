---
title: An intro to Observables and how they are different from promises
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-01T20:29:18.000Z'
originalURL: https://freecodecamp.org/news/what-are-observables-how-they-are-different-from-promises
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/code_feature.jpeg
tags:
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
- name: observables
  slug: observables
- name: promises
  slug: promises
- name: RxJS
  slug: rxjs
seo_title: null
seo_desc: 'By Anchal Nigam

  ‘Observables’, ‘Observables’, ‘Observables’...Yes! Today, we will talk about this
  often discussed word of the market. We''ll also learn how they are different from
  Promises (haven''t heard about Promises? Not to worry! You will know mor...'
---

By Anchal Nigam

‘**Observables**’, ‘**Observables**’, ‘**Observables**’...Yes! Today, we will talk about this often discussed word of the market. We'll also learn how they are different from Promises (haven't heard about Promises? Not to worry! You will know more soon). Let’s start!

I first encountered the term **Observable** when I started learning Angular. Although it’s not an Angular-specific feature, it’s a new way of handling **async** requests.  Async request?  You know it, right? No! It’s ok. Let’s first understand what’s an **async** request is then.

## Async Requests

Well! You must have read about asynchronous features in the JavaScript world. '**Asynchrony**' in the computer world means that the flow of the program occurs independently. It does not wait for a task to get finished. It moves to the next task. 

Now, you might be thinking - what happens to the task that is not finished? The co-worker handles those unfinished tasks. Yes! In the background, a co-worker works and handles those unfinished tasks and once they are done, it sends data back. 

This can bring up another question of how we handle the data that is returned. The answer is **Promises**, **Observables**, **callbacks** and many more. 

We know that these asynchronous operations return responses, either some data after success or an error. To handle this, concepts like **Promises**, **callbacks**, **observables** came into the market. Well! I will not get into them now as we have deviated from our sub topic i.e '**async**' request. (Don't worry! These topics will be discussed soon).

After discussing the above points, you might ha have got a rough picture of what the **async** request is. Let’s clear it up. An **Async** request is one where the client does not wait for the response. Nothing is blocked. Let’s understand this concept by looking at a very common scenario.

In the web world, it's quite common to hit the server to get data like the details of a user, a list, and so on. We know it will take time and anything can follow (success/failure). 

 this case, instead of waiting for data to come, we handle it asynchronously (no waiting) so that our application does not get blocked. Such requests are asynchronous requests. I think now we are clear with it. So let's see how we can actually handle these async requests.

As I already told you, Observables gave us a new way of handling async requests. The other ways are promises, callbacks, and async/await. These are the popular ways. Let’s have a look at two of them which are callbacks and promises.

## Callbacks

Callbacks are quite a common one. Callback functions (as their name suggests) are called at the back. That is when the request gets completed and returns the data or error, these functions get called. Have a look at the code for a better understanding:

```
const request = require(‘request’);
request('https://www.example.com', function (err, response, body) {
  if(error){
    // Error handling
  }
  else {
    // Success 
  }
});
```

This is one way of handling an async request. But what happens when we want to again request to the server for data after the success of the first request? What if we want to make a third request after that successful second request? Horrible! 

At this point, our code will become messy and less readable. This is called ‘**callback** **hell**’. To overcome it, promises came around. They offer a better way of handling an async request that improves code readability. Let’s understand a bit more.

## Promises

Promises are objects that promise they will have value in the near future - either a success or failure. Promises have their own methods which are **then** and **catch**. **.then()** is called when success comes, else the **catch()** method calls.  **Promises** are created using the **promise** constructor. Have a look at code to better understand.

```
function myAsyncFunction(name){
     return new Promise(function(resolve, reject){
          if(name == ‘Anchal’){
               resolve(‘Here is Anchal’)
         }
         else{
              reject(‘Oops! This is not Anchal’)
        }

     }
} 

myAsyncFunction(‘Anchal’)
.then(function(val){
      // Logic after success
      console.log(val)     // output -  ‘Here is Anchal’
})
.catch(function(val){
    //Logic after failure
     console.log(val)     // output - ‘Oops! This is not Anchal’
})
```

As you can see, **myAsyncFunction** is actually promising that it will have some value in near future. **.then()** or **.catch()** is called according to the promise's status. 

**Promises** improve **code** **readability**. You can see how readable the code is by using promises. Better handling of async operations can be achieved using Promises. This is a brief introduction of what promises are, how they handle data and what beauty promises carry.

Now, it's time to learn about our main topic: Observables.

## What are Observables?

Observables are also like callbacks and promises - that are responsible for handling async requests. Observables are a part of the **_RXJS_** library. This library introduced Observables. 

Before understanding what an observable actually is, you must understand two communication models: **pull** and **push**. These two concepts are protocols of how producers of data communicate with the consumers of data.

### Pull & Push Model

As I have already told you, Push and Pull are communication protocols between data producers and consumers.  Let’s understand both one by one.

**Pull Model:** In this model, the **consumer** of data is **king**. This means that the consumer of data determines when it wants data from the producer. The producer does not decide when the data will get delivered. You can better understand if you relate **functions** to it.

As we know, functions are responsible for doing some task. For example, **dataProducer** is a function which is simply returning a string, like "**Hi** **Observable**".

```
function dataProducer(){
   return ‘Hi Observable’;
}
```

  
Now, you can see that the above function is not going to decide when it will deliver the ‘Hi Observable’ string. It will decide by the consumer, that is code that calls this function. Consumer is king. The reason why it is called a pull model is that **pull** task is determining the communication.  This is the **pull** **Model**. Now, let’s go into the **Push** **Model**_._

**Push Model:** In this model, the **producer** of data is **king**. Producer determines when to send data to consumer. The Consumer does not know when data is going to come. Let’s understand it by taking an example:

I hope you remember **promises**_._ Yes, **Promises** follow the **push** **model**_._  A Promise (producer) delivers data to the callback (_.then()_ - consumer). Callbacks do not know when data is going to come. Here, **promise** (producer) is king. It is determining the communication. That’s why it's called **Push** **Model** as the producer is in charge.

Like promises, Observables also follow the push model. How? You will get the answer once I elaborate on observables. Let’s get back to observables then.

## Observables as functions

To simply understand, you can think of observables as functions. Let’s have a look at the below examples:

```
function dataProducer(){
    return ‘Hi Observable’
}

var result = dataProducer();
console.log(result) // output -  ‘Hi Observable’

```

  
You can get the same behaviour using an observable: 

```
var observable = Rx.Observable.create((observer: any) =>{

   observer.next(‘Hi Observable’);

})

observable.subscribe((data)=>{
   console.log(data);    // output - ‘Hi Observable’
})
```

From above, you can see both functions and observables show the same behaviour. This may bring a question to your mind - are observables the same as functions? No. I'll clarify in a minute why the answer is no. Have a look at an elaborate version of the above example.

```
function dataProducer(){
    return ‘Hi Observable’;
    return ‘Am I understandable?’ // not a executable code.
}

var observable = Rx.Observable.create((observer: any) =>{

   observer.next(‘Hi Observable’);
   observer.next( ‘Am I understandable?’ );

})

observable.subscribe((data)=>{
   console.log(data);    
})

Output :
‘Hi Observable’
‘Am I understandable?’ 
```

  
I hope you can now see what difference I wanted to address. From above, you can see, **both functions and observables are lazy**. We need to call (functions) or subscribe (observables) to get the results. 

**Subscriptions to observables are quite similar to calling a function.** But where observables are different is in their ability to return **multiple** **values** called **streams** (a stream is a sequence of data over time). 

Observables not only able to return a value **synchronously**, but also **asynchronously**.

```
var observable = Rx.Observable.create((observer: any) =>{
   observer.next(‘Hi Observable’);
    setTimeout(()=>{
        observer.next(‘Yes, somehow understandable!’)
    }, 1000)   

   observer.next( ‘Am I understandable?’ );
})

output :

‘Hi Observable’
‘Am I understandable?’ 
Yes, somehow understandable!’.

```

In short, you can say **observables are simply a function that are able to give multiple values over time, either synchronously or asynchronously**_**.**_

You now have an outline about observables. But let’s understand them more by looking into different phases of observables.

## Observable Phases

  
We have already seen from the above example how observables create and execute and come into play by subscription. Hence, there are four stages through which observables pass. They are:

1. **Creation**
2. **Subscription.**
3. **Execution**
4. **Destruction.**

  
**Creation of an observable** is done using a **create** **function**.

```
var observable = Rx.Observable.create((observer: any) =>{
})

```

To make an **observable** **work**, we have to **subscribe** it. This can be done using the subscribe method.

```
observable.subscribe((data)=>{
   console.log(data);    
})
```

  
Execution of observables is what is inside of the create block. Let me illustrate with the help of an example:

```
var observable = Rx.Observable.create((observer: any) =>{

   observer.next(‘Hi Observable’);        
    setTimeout(()=>{
        observer.next(‘Yes, somehow understandable!’)
    }, 1000)   

   observer.next( ‘Am I understandable?’ );

})

```

The above code inside the create function is observable execution. The **three** types of **values** that an observable can deliver to the subscriber are:

```
observer.next(‘hii’);//this can be multiple (more than one)

observer.error(‘error occurs’) // this call whenever any error occus.

Observer.complete(‘completion of delivery of all values’) // this tells the subscriptions to observable is completed. No delivery is going to take place after this statement.
```

Let’s have a look below to understand all three values:

```
var observable = Rx.Observable.create((observer: any) =>{
try {
   observer.next(‘Hi Observable’);                                       
    setTimeout(()=>{
        observer.next(‘Yes, somehow understandable!’)
    }, 1000)   

   observer.next( ‘Am I understandable?’ );
   
   observer.complete();
   
   observer.next(‘lAST DELIVERY?’ );  
   // above block is not going to execute as completion notification is      already sent.
   }
catch(err){
     observer.error(err);	
  }

})                      
```

Last phase that comes into the market is destruction. After an error or a complete notification, the observable is automatically unsubscribed. But there are cases where we have to manually **unsubscribe** it. To manually do this task, just use:

```
var subscription = observable.subscribe(x => console.log(x)); // Later: subscription.unsubscribe();
```

This is all about the different phases through which an observable passes.

I think, now, we know what observables are? But what about the other question which is - how observables are different from promises? Let’s find the answer to it.

## Promises vs observables

As we know, promises are for handling async requests and observables can also do the same. But where do they differ?

### Observables are lazy whereas promises are not

This is pretty self-explanatory: observables are lazy, that is we have to subscribe observables to get the results. In the case of promises, they execute immediately.

### Observables handle multiple values unlike promises 

Promises can only provide a single value whereas observables can give you multiple values.

### Observables are cancelable

You can cancel observables by unsubscribing it using the **unsubscribe** method whereas promises don’t have such a feature.

### Observables provide many operators

There are many operators like **map**_,_ **forEach**_,_ **filter** etc. Observables provide these whereas promises does not have any operators in their bucket.

These are features that makes observables different from promises.

Now, it's time to end. I hope you have a better understanding of the hot topic of observables!

Thanks for reading!  

