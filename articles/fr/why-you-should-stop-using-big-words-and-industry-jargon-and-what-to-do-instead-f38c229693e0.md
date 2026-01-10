---
title: Pourquoi vous devriez arrêter d'utiliser des mots compliqués et du jargon professionnel
  (et que faire à la place)
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-03T23:45:15.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-stop-using-big-words-and-industry-jargon-and-what-to-do-instead-f38c229693e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o7WmwGkLVR0dVQUYqfSBeg.jpeg
tags:
- name: communication
  slug: communication
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: 'tech '
  slug: tech
seo_title: Pourquoi vous devriez arrêter d'utiliser des mots compliqués et du jargon
  professionnel (et que faire à la place)
seo_desc: 'Let’s say you want to teach a person something. Why does the person not
  understand what you’re saying?

  One of the main reasons is likely because we like to use big words and industry
  jargon. This jargon may mean something to us, but it means nothing ...'
---

Disons que vous voulez enseigner quelque chose à une personne. Pourquoi cette personne ne comprend-elle pas ce que vous dites ?

L'une des principales raisons est probablement que nous aimons utiliser des mots compliqués et du jargon professionnel. Ce jargon peut signifier quelque chose pour nous, mais il ne signifie rien pour les personnes à qui nous essayons d'enseigner.

La prochaine fois que vous essayez d'enseigner la programmation, faites attention aux mots que vous utilisez.

### Trois types de mots compliqués

Nous pouvons diviser le jargon en trois catégories :

1. Celui qui peut être expliqué en quelques mots
2. Celui qui ne peut pas être expliqué avec des mots simples
3. Celui qui peut signifier différentes choses dans différents contextes.

Lorsque vous enseignez, vous devez toujours faire attention à ces trois types de mots.

### Jargon qui peut être expliqué en quelques mots

Si le jargon peut être expliqué en quelques mots, vous voulez **utiliser ces mots au lieu du jargon.**

L'interopérabilité est un exemple de tel mot.

Cela semble effrayant et compliqué, mais cela peut être expliqué en quelques mots simples.

Si vous cherchez la signification de l'interopérabilité, vous tomberez sur des définitions comme celles-ci :

De Wikipedia :

> « L'interopérabilité est une caractéristique d'un produit ou d'un système, dont les interfaces sont complètement comprises, pour travailler avec d'autres produits ou systèmes, actuellement ou dans le futur, en termes d'implémentation ou d'accès, sans aucune restriction. »

De Dictionary.com :

> « L'interopérabilité est la capacité à partager des données entre différents systèmes informatiques, en particulier sur différentes machines. »

Si nous le mettons en termes simples, « interopérabilité » signifie la « capacité à partager des données ».

Voyez comment cela réduit considérablement la barrière linguistique ?

Si vous pouvez remplacer un tel jargon par des mots simples, pourquoi vous en tenir au mot difficile ?

### Jargon qui signifie différentes choses dans différents contextes

Certains jargons ont des significations différentes lorsqu'ils sont utilisés dans différents contextes.

Un exemple de tel jargon est l'encapsulation.

Encapsuler quelque chose signifie l'enfermer avec autre chose. Si vous enveloppez une pomme de terre avec un tissu, vous pouvez dire que le tissu encapsule la pomme de terre.

Les développeurs adorent le mot encapsulation. Ils l'utilisent tout le temps.

La première façon est d'enfermer des variables et d'autres codes à l'intérieur d'une fonction. Dans ce cas, la fonction encapsule le code à l'intérieur.

```
// Ceci est du JavaScript
function someFunction () {  const variableName = 'I am a variable!'}
```

La deuxième façon est de contenir l'individualité d'un objet. Par exemple, si vous avez un objet Human, et que vous créez deux humains à partir de l'objet human, ces deux humains ne devraient pas être les mêmes.

Dans ce cas, chaque objet encapsule ses propres données.

```
// Ceci est du JavaScript
function Human (name) {  this.name = name}
```

```
const zell = new Human('Zell')
const vincy = new Human('Vincy')
```

```
zell.name === vincy.name // false
```

La troisième façon est pour le masquage d'informations. En JavaScript, nous pouvons créer des variables privées. Ces variables privées sont enfermées par l'objet.

Dans ce cas, l'objet encapsule la variable privée. Vous ne pouvez pas accéder à la variable privée. Dans ce cas, l'encapsulation est utilisée pour signifier quelque chose de différent du deuxième cas.

```
// Ceci est du JavaScript
function Human () {  const privateVariable = 'private'  this.publicVariable = 'public'}
```

Alors, que comprenez-vous par Encapsulation ?

Vous ne pouvez pas être sûr.

Il ne devrait y avoir aucune ambiguïté lorsque vous communiquez. Si il y a ambiguïté, la communication s'effondre, et les étudiants n'apprennent pas.

Il est préférable d'**abandonner le jargon si le jargon signifie différentes choses dans différents contextes.**

### Jargon qui ne peut pas être expliqué avec des mots simples

Certains jargons ne peuvent pas être expliqués avec des mots simples. Ce jargon est souvent utilisé pour parler de concepts abstraits, ce qui explique pourquoi des mots simples peuvent ne pas suffire.

Un exemple de tel mot est « mutation ».

Mutation vient du mot muter. Muter signifie changer de forme ou de nature. En JavaScript, la mutation se produit sous le capot sans que vous le remarquiez.

Dans ce cas, le changement n'est pas suffisant pour expliquer la mutation. Il manque de profondeur et de détail. De plus, le changement est encore trop abstrait.

Vous ressentez qu'un concept est abstrait, parce que vous ne pouvez pas l'imaginer. Vous ne pouvez pas le voir, l'entendre, le sentir, le toucher ou le goûter. Pour rendre un concept abstrait concret, nous devons faire appel aux cinq sens humains.

**Pour expliquer un concept abstrait, vous pouvez utiliser des analogies.** Lorsque vous utilisez des analogies, vous pouvez décrire un objet ou un scénario de manière à ce que les gens puissent voir, entendre ou ressentir ce que vous voulez dire.

Par exemple, [j'ai utilisé les X-men comme analogie lorsque j'ai expliqué la mutation](https://alistapart.com/article/why-mutation-can-be-scary).

J'ai demandé aux étudiants d'imaginer un ami qui pousse des poils et devient bleu sous leurs yeux. Tout le monde peut imaginer ce que signifie pousser des poils et devenir bleu, même s'ils ne savent pas qui est Beast.

Si vous voulez étendre l'analogie pour toucher plus de personnes, vous pouvez faire appel à plus de sens. Par exemple, pour faire imaginer la mutation aux aveugles, vous pouvez aussi leur dire d'imaginer que leur ami grogne comme une bête.

Le point clé ici est un changement qui passe inaperçu. Personne ne sait si une personne est un mutant jusqu'à ce qu'elle montre ses pouvoirs. Sur le même front, personne ne sait qu'un objet JavaScript a changé jusqu'à ce qu'il ait changé.

J'ai souligné ce point pour établir un lien avec la mutation en JavaScript.

La mutation devient plus concrète une fois le lien établi. Lorsque je dis mutation, les étudiants qui ont lu l'article peuvent imaginer leur ami devenir bleu, pousser des poils et grogner comme une bête.

Une fois que vous avez transformé le jargon abstrait en un concept concret, vous pouvez utiliser ce jargon comme vous le feriez habituellement. Les étudiants comprendront ce que vous voulez dire.

J'ai écrit un article sur [la création de bonnes analogies](https://zellwk.com/blog/creating-good-analogies) si vous êtes intéressé à apprendre cette compétence.

### Conclusion

Faites attention aux mots que vous utilisez lorsque vous enseignez la programmation. Si vous utilisez des mots difficiles qui ne signifient rien pour votre étudiant, ils ne pourront pas comprendre ce que vous voulez dire.

Remplacez les mots difficiles par des mots plus simples et plus faciles à comprendre si vous le pouvez.

Évitez d'utiliser du jargon qui peut signifier différentes choses dans différents contextes. Ce jargon rend les choses ambiguës et confuses.

Enfin, utilisez des analogies pour transformer des concepts abstraits en concepts concrets.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Stop%20using%20big%20words%20and%20industry%20jargons%20(and%20what%20to%20do%20instead)%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/big-words/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [zellwk.com](https://zellwk.com/blog/big-words).

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.