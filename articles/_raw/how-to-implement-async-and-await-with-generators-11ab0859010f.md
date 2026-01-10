---
title: Implementing Async And Await With Generators
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T10:54:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-async-and-await-with-generators-11ab0859010f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9wHrewC1Dyf2Au_qEqwWcg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Maciej Cieślar

  Nowadays we can write our asynchronous code in a synchronous way thanks to the async
  and await keywords. This makes it easier to read and understand. Recently I wondered,
  however, how the same effect could be achieved without using ...'
---

By Maciej Cieślar

Nowadays we can write our asynchronous code in a synchronous way thanks to the **async** and **await** keywords. This makes it easier to read and understand. Recently I wondered, however, how the same effect could be achieved without using these keywords.

It turns out to be quite simple, since the behavior of **async** and **await** can easily be emulated using generators. Let’s have a look!

Go ahead, clone the [repository](https://github.com/maciejcieslar/asynq) and let’s get started.

### Generators

I am going to assume you have little to no experience with generators since, honestly, most of the time they aren’t particularly useful and you can easily manage without them. So don’t worry — we’ll start with a quick reminder.

Generators are objects created by [generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) — functions with an _*_ (asterisk) next to their name.

These generators have an amazing ability that lets us stop the execution of code — whenever we want — by using the keyword **yield**.

Consider this example:

```javascript
const generator = (function*() {
  // waiting for .next()
  const a = yield 5;
  // waiting for .next()
  console.log(a); // => 15
})();

console.log(generator.next()); // => { done: false, value: 5 }
console.log(generator.next(15)); // => { done: true, value: undefined }
```

Given that these are absolute basics, I would recommend that, before you scroll any further, you read [this article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators) to get a grasp on what is really going on here.

If you feel like you have a strong understanding of the underlying ideas, we can move on.

### Hold on, await a minute

Haven’t you ever wondered how **await** really works?

Somehow it just waits for our promise to return a value and proceed with the execution. For me, that seems like something a generator would be able to do after a little tweaking.

What we could do is just take every yielded value, put it into a promise, and then wait for the promise to be resolved. Afterwards, we just return it to the generator by calling _generator.next(resolvedValue)._

Sounds like a plan. But first, let’s write some tests just to be sure that everything is working as expected.

What our **asynq** function should do:

* wait for asynchronous code before continuing the execution
* return a **promise** with the returned value from the function
* make **try/catch** work on asynchronous code

Note: because we are using generators, our **await** becomes **yield**.

```typescript
import { asynq } from '../src';

describe('asynq core', () => {
  test('Waits for values (like await does)', () => {
    return asynq(function*() {
      const a = yield Promise.resolve('a');
      expect(a).toBe('a');
    });
  });

  test('Catches the errors', () => {
    return asynq(function*() {
      const err = new Error('Hello there');

      try {
        const a = yield Promise.resolve('a');
        expect(a).toBe('a');

        const b = yield Promise.resolve('b');
        expect(b).toBe('b');

        const c = yield Promise.reject(err);
      } catch (error) {
        expect(error).toBe(err);
      }

      const a = yield Promise.resolve(123);
      expect(a).toBe(123);
    });
  });

  test('Ends the function if the error is not captured', () => {
    const err = new Error('General Kenobi!');

    return asynq(function*() {
      const a = yield Promise.reject(err);
      const b = yield Promise.resolve('b');
    }).catch((error) => {
      expect(error).toBe(err);
    });
  });

  test('Returns a promise with the returned value', () => {
    return asynq(function*() {
      const value = yield Promise.resolve(5);
      expect(value).toBe(5);

      return value;
    }).then((value) => {
      expect(value).toBe(5);
    });
  });
});
```

Alright, great! Now we can talk about the implementation.

Our **asynq** function takes as a parameter a function generator — by calling it, we create a generator.

Just to be sure, we call [_isGeneratorLike_](https://github.com/maciejcieslar/asynq/blob/master/src/utils.ts) which checks if the received value is an object and has methods **next** and **throw**.

Then, recursively, we consume each **yield** keyword by calling _generator.next(ensuredValue)._ We wait for the returned promise to be settled, and then return its result back to the generator by repeating the whole process.

We must also attach the **catch** handler, so that, should the function throw an exception, we can catch it and return the exception inside the function by calling _generator.throw(error)_.

Now, any potential errors will be handled by **catch**. If there wasn’t a **try/catch** block in place, an error would simply stop the execution altogether — like any unhandled exception would — and our function would return a rejected promise.

When the generator is done, we return the generator’s return value in a promise.

```typescript
import { isGeneratorLike } from './utils';

type GeneratorFactory = () => IterableIterator<any>;

function asynq(generatorFactory: GeneratorFactory): Promise<any> {
  const generator = generatorFactory();

  if (!isGeneratorLike(generator)) {
    return Promise.reject(
      new Error('Provided function must return a generator.'),
    );
  }

  return (function resolve(result) {
    if (result.done) {
      return Promise.resolve(result.value);
    }

    return Promise.resolve(result.value)
      .then((ensuredValue) => resolve(generator.next(ensuredValue)))
      .catch((error) => resolve(generator.throw(error)));
  })(generator.next());
}
```

Now, having run our tests, we can see that everything is working as expected.

### Wrapping up

While this implementation is probably not the one used inside the JavaScript engines, it sure feels good to be able to do something like this on our own.

Feel free to go over the code again. The better your understanding of the underlying ideas, the more you will be able to appreciate the brilliance of the creators of the **async** and **await** keywords.

Thank you very much for reading! I hope you found this article informative. I also hope it helped you see there is no magic involved in the **async** and **await** keywords, and that they can be easily replaced with generators.

If you have any questions or comments, feel free to put them in the comments section below or send me a [message](https://www.mcieslar.com/contact).

Check out my [social media](https://www.maciejcieslar.com/about/)!

[Join my newsletter](http://eepurl.com/dAKhxb)!

_Originally published at [www.mcieslar.com](https://www.mcieslar.com/implementing-async-and-await-with-generators) on August 6, 2018._

