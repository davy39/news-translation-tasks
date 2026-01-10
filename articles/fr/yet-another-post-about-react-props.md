---
title: Encore un article sur les props de React
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
seo_title: Encore un article sur les props de React
seo_desc: 'By Jeff M Lowery

  You could say this topic has been done to death, but lately I’ve started using a
  technique that I don''t recall having come across elsewhere. While it''s not  particularly
  clever, it is concise.  So please forgive one more post on the ...'
---

Par Jeff M Lowery

On pourrait dire que ce sujet a été traité [à](https://flaviocopes.com/react-pass-props-to-children/) [plusieurs](https://medium.com/better-programming/passing-data-to-props-children-in-react-5399baea0356) [reprises](https://zhenyong.github.io/react/docs/jsx-spread.html), mais récemment, j'ai commencé à utiliser une technique que je ne me souviens pas avoir vue ailleurs. Bien qu'elle ne soit pas particulièrement ingénieuse, elle est concise. Alors, pardonnez-moi un autre article sur le sujet...

# Les props de manière verbeuse

> « N'ayez pas peur ! Nous ne ferons pas de vous un auteur, tant qu'il y a un métier honnête à apprendre, ou la fabrication de briques à laquelle se tourner. »

Je vais baser mes exemples sur une [application React](https://pokermap.netlify.com/) qui utilise [jsheatmap](https://www.npmjs.com/package/jsheatmap), un package que j'ai écrit pour générer des données de heat map. La présentation de la heat map est faite via un `<table>`, où la couleur de fond de chaque cellule est définie par une valeur RGB que jsheatmap génère à partir d'un [ensemble donné de valeurs d'entrée](https://www.freecodecamp.org/news/a-heat-map-implementation-in-typescript/).

```js
const HeatMapTable = () => {
  const [players, setPlayers] = useState(2);
  const [suited, setSuited] = useState(false)
  const [ties, setTies] = useState(false)
  const [data, setData] = useState(getNewData(players, suited, ties))
```

Il y a un composant PlayersRow qui contient des contrôles permettant à l'utilisateur de définir le nombre de joueurs nécessaires pour déterminer certaines probabilités au poker. Il a besoin non seulement de la valeur initiale, mais aussi d'un setter pour définir de nouvelles valeurs. Ces propriétés (props) sont `players` et `setPlayers`.

On pourrait utiliser la technique éprouvée consistant à passer ces props en tant qu'attributs explicites lors de l'inclusion du composant dans son conteneur (HeatMapTable).

```js
<Players players={players} setPlayers={setPlayers} />
```

Assez basique.

# Les props de manière concise

> « S'il vous plaît, monsieur, je veux encore. »

Dans ce cas (comme cela arrive souvent), les variables utilisées pour contenir les valeurs des props ont souvent les mêmes noms que les noms des attributs des composants React. Cela permet une syntaxe plus concise pour passer les props au composant enfant.

Dans l'exemple que je viens de montrer, il y a deux props ; vous pourriez en avoir beaucoup plus. Une technique consiste à utiliser un objet intermédiaire pour contenir les props nécessaires au composant enfant, puis à utiliser l'opérateur de décomposition pour « développer » l'objet prop en valeurs d'attributs.

```js
const props = {players, setPlayers, anotherProp, yetAnotherProp, etc};
<Players {...props} />
```

Ce qui est équivalent à la version beaucoup plus verbeuse :

```js
<Players players={players} setPlayers={setPlayers} anotherProp={anotherProp} yetAnotherProp={yetAnotherProp} etc={etc} />
```

# Les props de manière encore plus concise

> « Hélas ! Combien peu de visages de la Nature sont laissés intacts pour nous réjouir de leur beauté ! »

Il s'avère que la variable intermédiaire n'est pas vraiment nécessaire, car vous pouvez simplement faire ceci :

```js
<Players {...{players, setPlayers, anotherProp, yetAnotherProp, etc}} />
```

Ou même quelque chose qui mélange des objets intermédiaires avec l'opérateur de décomposition :

```js
const props = {anotherProp, yetAnotherProp, etc};
<Players {...{players, setPlayers, ...props}} />
```

Comme je l'ai dit, ce n'est pas très malin, il s'agit simplement d'utiliser l'opérateur de décomposition pour développer un objet déclaré à l'intérieur du JavaScript désigné par les `{}` extérieurs.

---

C'est tout ! Un petit truc que je me surprends à utiliser de plus en plus fréquemment.