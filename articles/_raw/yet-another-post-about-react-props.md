---
title: Yet another post about React props
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-09T21:52:16.000Z'
originalURL: https://freecodecamp.org/news/yet-another-post-about-react-props
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/illustration-depicting-oliver-twist-asking-for-more-food-by-j--mahoney-517216578-59f93a010d327a0010b2dd78.jpg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: 'By Jeff M Lowery

  You could say this topic has been done to death, but lately I’ve started using a
  technique that I don''t recall having come across elsewhere. While it''s not  particularly
  clever, it is concise.  So please forgive one more post on the ...'
---

By Jeff M Lowery

You could say this topic has been [done](https://flaviocopes.com/react-pass-props-to-children/) [to](https://medium.com/better-programming/passing-data-to-props-children-in-react-5399baea0356) [death](https://zhenyong.github.io/react/docs/jsx-spread.html), but lately I’ve started using a technique that I don't recall having come across elsewhere. While it's not  particularly clever, it is concise.  So please forgive one more post on the topic...

# Props the verbose way

> “Don't be afraid! We won't make an author of you, while there's an honest trade to be learnt, or brick-making to turn to.”

I’ll base my examples on a [React application](https://pokermap.netlify.com/) that uses [jsheatmap](https://www.npmjs.com/package/jsheatmap), a package I wrote for generating heat map data. The presentation of the heat map is done via a `<table>`, where each cell’s background color is set to an RGB value that jsheatmap generates from a [given set of input values](https://www.freecodecamp.org/news/a-heat-map-implementation-in-typescript/).

```js
const HeatMapTable = () => {
  const [players, setPlayers] = useState(2);
  const [suited, setSuited] = useState(false)
  const [ties, setTies] = useState(false)
  const [data, setData] = useState(getNewData(players, suited, ties))
```

There is a PlayersRow component that contains controls to allow the user to set the number of players needed to determine certain poker odds. It needs not only the initial value, but a setter to set new values. These properties (props) are `players` and `setPlayers`.

One could use the time-honored technique of passing these props as explicit attributes when including the component in its container (HeatMapTable).

```js
<Players players={players} setPlayers={setPlayers} />
```

Pretty basic stuff.

# Props the concise way

> "Please, sir, I want some more."  

In this case (as often happens), the variables used to hold the prop values often have the same names as the attribute names of the React components. This allows a more concise syntax to pass the props down to the child.

In the example just shown, there are two props; you might have many more. One technique is to use an intermediate object to hold the props that are needed by the child component, then use the spread operator to “expand” the prop object into attribute values.

```js
const props = {players, setPlayers, anotherProp, yetAnotherProp, etc};
<Players {...props} />
```

Which is equivalent to the much more verbose:

```js
<Players players={players} setPlayers={setPlayers} anotherProp={anotherProp} yetAnotherProp={yetAnotherProp} etc={etc} />
```

# Props the conciser way

> “Alas! How few of Nature's faces are left alone to gladden us with their beauty!"

It turns out that the intermediate variable is not really needed, because you can just do this:

```js
<Players {...{players, setPlayers, anotherProp, yetAnotherProp, etc}} />
```

Or even something that mixes intermediate objects with the spread operator:

```js
const props = {anotherProp, yetAnotherProp, etc};
<Players {...{players, setPlayers, ...props}} />
```

As I said, not all that clever, it's just using the spread operator to spread an object declared inside the the JavaScript denoted by the outer `{}`.  

---

So that's all there is! A little trick I find myself using ever more frequently.


