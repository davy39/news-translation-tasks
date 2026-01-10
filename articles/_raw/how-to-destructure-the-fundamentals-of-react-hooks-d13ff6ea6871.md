---
title: How to destructure the fundamentals of React Hooks
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-04-17T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-destructure-the-fundamentals-of-react-hooks-d13ff6ea6871
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6g791iHSFVEe6yZqH9IlIA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: Hooks have become a pretty powerful new feature of React. They can be intimidating
  if you’re not really sure what’s going on behind the scenes. The beauty is now being
  able to manage state in a simple (and reusable) manner within function components....
---

Hooks have become a pretty powerful new feature of React. They can be intimidating if you’re not really sure what’s going on behind the scenes. The beauty is now being able to manage state in a simple (and reusable) manner within function components.

But why not use a class? Without getting too far away from the topic, functions provide a more straightforward way to write your components, guiding you to write in a cleaner and more reusable way. Bonus: it typically makes writing tests easier.

There’s [a lot of use cases for hooks](https://github.com/rehooks/awesome-react-hooks), so I won’t dive into examples. It shouldn’t be too bad to get up to speed with a few quick lines. For the sake of this article, let’s assume browser cookies aren’t a thing and these are the edible type.

### Diving into the cookie jar

Here we have `MyCookies`, a function component, which we can consider our cookie jar. Let's say we want to internally keep track of how many cookies we have in the jar. With the new hooks API, we can add a simple line using `useState` to handle the job.

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  ...
};
```

### Wait, how do we get cookies out of that?

If you think the above is magic and are wondering how the values in the array are getting set, you’ll need to understand the basics of array destructuring.

While destructuring an object will use the same key wherever you try to pull it from, arrays destructure using the order of the items within the array.

```js
const [ one, two ] = [ 1, 2 ];
console.log(one); // 1
console.log(two); // 2
```

While the above seems like it’s naming them in a particular order, it’s not as shown below:

```js
const [ two, one ] = [ 1, 2 ];
console.log(two); // 1
console.log(one); // 2
```

Without going too far down the technical rabbit hole, `useState` is a function that returns an array that we're destructuring for use within our component.

What about the 0 inside the invocation of `useState` itself? That’s simply the initial value we’re setting the state instance to. In this case, we’ll sadly start off with 0 cookies.

### Actually, use state

Once we have our destructured `cookies` and the `setCookiesCount` function, we can start interacting with the component's local state like you might do using `setState` within a class component.

At render time, our `cookies` value will be that invocation of `useState`'s internal state value, similar to what you might see with `this.state`. To update that value, we can simply call `setCookiesCount`.

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  return (
    <>
      <h2>Cookies: { cookies }</h2>
      <button onClick={() => setCookieCount(cookies + 1)} >
        Add Cookie
      </button>
    </>
  );
};
```

If you’re more used to the class syntax, you might update state using `this.setState` looking something like this:

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  });
  ...
};
```

### How to use effects

Often components need a way to create side effects that won’t necessarily interrupt the functional flow of a function component. Say we have the number of cookies we have saved on a server somewhere, we might want to fetch that count when the app loads.

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  }, []);
  ...
};
```

After the component renders, everything inside of `useEffect` will run. Any side effects originating from `useEffect` will only occur after the render is complete. That said, once `useEffect` does run, we fire `getCookieCount` and use our previous `setCookieCount` function to update the state of the component.

### Hold up, there’s something wrong…

There’s a gotcha in the code above though. That effect will run every time, essentially wiping out any new increments to our cookie value from our original Add Cookie button.

To get around this, we can set a 2nd argument to the `useEffect` function that allows us to let React know when to run it again. In our example above, setting that 2nd argument to an empty array will make it run only once.

```js
const MyCookies = ({cookieType = 'chocolate'}) => {
  const [ cookies, setCookieCount ] = useState(0);
  useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  }, [ cookieType ]);
  ...
};
```

In most cases though, you’ll want to pass an array of dependencies that, when changed, will cause `useEffect` to fire again. Say, for example, you're fetching the count of a specific cookie type and want to get the count again if that type changes.

```js
import BasketContext from 'context';

const Basket = ({children}) => {
  return (
    <BasketContext.Provider value={basketItems}>
      <h1>My Basket</h1>
      { children }
    </BasketContext.Provider>
  );
}

// MyCookies.js
const MyCookies = ({cookieType = 'chocolate'}) => {
  const basketItems = useContext(BasketContext);
  ...
};
```

In the above code, any time our prop `cookieType` changes, React knows that we depend on it for our effect, and will rerun that effect.

### Trying to make use of context

I’m not going to [go into the details of React’s context API](https://reactjs.org/docs/context.html) as that’s a little out of scope. However, if you’re familiar with it, the `useContext` hook lets you easily make use of your context from within your function component.In the above code, given our already created context, we can immediately “use” said context and collect the values passed into our context provider.

```js
import BasketContext from 'context';

const Basket = ({children}) => {
  return (
    <BasketContext.Provider value={basketItems}>
      <h1>My Basket</h1>
      { children }
    </BasketContext.Provider>
  );
}

// MyCookies.js
const MyCookies = ({cookieType = 'chocolate'}) => {
  const basketItems = useContext(BasketContext);
  ...
};
```

### Cleaning your hooks

What makes hooks even more powerful is combining and abstracting them DRYing up your code in a cleaner way. As a quick last example, we can take our cookie examples of `useState` and `useEffect` and abstract them into their own `use[Name]` function, effectively [creating a custom hook](https://reactjs.org/docs/hooks-custom.html).

```
// useCookies.js
function useCookies(initialCookieCount) {

  const [ cookies, setCookieCount ] = useState(initialCookieCount);

    useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  }, []);

  function addCookie() {
    setCookieCount(cookies + 1);
    console.log('?');
  }

  function removeCookie() {
    setCookieCount(cookies - 1);
    console.log('?');
  }

  return {
    cookies,
    addCookie,
    removeCookie
  }
};

// MyCookies.js
const MyCookies = () => {
  const { cookies, addCookie, removeCookie } = useCookies(0);
  ...
};
```

We were safely able to abstract our state logic and still utilize it to manage our cookies.

### Plenty more to get hooked on

These are the basic 3 hooks React gives us, but [there are many more they provide out of the box](https://reactjs.org/docs/hooks-reference.html), all with the same underlying principles that the React documentation does a good job at explaining.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Originally published at [https://www.colbyfayock.com/2019/04/destructuring-the-fundamentals-of-react-hooks](https://www.colbyfayock.com/2019/04/destructuring-the-fundamentals-of-react-hooks)._

