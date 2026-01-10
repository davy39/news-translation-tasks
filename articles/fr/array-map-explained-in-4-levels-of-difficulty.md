---
title: 'Array.map expliqué à 4 niveaux de complexité : d''un enfant de 5 ans à un
  programmeur fonctionnel.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-17T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/array-map-explained-in-4-levels-of-difficulty
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/4-levels-of-explanation.png
tags:
- name: arrays
  slug: arrays
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: 'Array.map expliqué à 4 niveaux de complexité : d''un enfant de 5 ans à
  un programmeur fonctionnel.'
seo_desc: 'By Yazeed Bzadough

  Array.map might be JavaScript''s most useful function. Forgoing it nowadays is like
  donning your toolbelt without a hammer.

  To further appreciate map and deepen our understanding of it, let''s see 4 levels
  of explanations in ascendin...'
---

Par Yazeed Bzadough

`Array.map` pourrait être la fonction la plus utile de JavaScript. Ne pas l'utiliser de nos jours, c'est comme mettre sa ceinture à outils sans marteau.

Pour mieux apprécier `map` et approfondir notre compréhension, voyons 4 niveaux d'explications en complexité ascendante.

Dites-moi lesquels vous avez compris et lesquels vous ont surpris !

## Table des matières
1. <a href="#pourunenfantdecinqans">Pour un enfant de cinq ans</a>
2. <a href="#pourellyceenapprenantlacodification">Pour un lycéen apprenant la codification</a>
3. <a href="#pourundeveloppeurreact">Pour un développeur React</a>
4. <a href="#pourundeveloppeurfonctionnel">Pour un développeur fonctionnel</a>

## Pour un enfant de cinq ans
Connais-tu Dragon Ball Z ? Voici mes personnages préférés de la série !

#### Goku
![goku-saluting-1](https://www.freecodecamp.org/news/content/images/2019/07/goku-saluting-1.png)

#### Vegeta
![vegeta-standing-2](https://www.freecodecamp.org/news/content/images/2019/07/vegeta-standing-2.png)

#### Trunks
![trunks-with-sword-1](https://www.freecodecamp.org/news/content/images/2019/07/trunks-with-sword-1.png)

Ils sont saiyans, et ils sont vraiment forts !

Je les ai mis dans cette liste – JavaScript les appelle des _tableaux_. Cela permet de regrouper plusieurs choses ensemble :

```js
saiyans = [goku, vegeta, trunks];
```

Et j'ai un code qui les transforme en Super Saiyans, donc ils deviennent 50 fois plus forts (littéralement) ! Ce code est appelé une _fonction_.

```js
turnSuperSaiyan = () => { /* utilise ton imagination */ };
turnSuperSaiyan(goku);
```

![transforming-goku](https://www.freecodecamp.org/news/content/images/2019/07/transforming-goku.png)

Et si je veux transformer les trois ? Je dois exécuter la fonction 3 fois ! Répéter les choses comme ça, c'est ennuyeux ?

```js
turnSuperSaiyan(goku);
turnSuperSaiyan(vegeta);
turnSuperSaiyan(trunks);
```

Heureusement, la programmation permet de répéter les choses très facilement ! `Array.map` peut les transformer tous en Super Saiyans en une seule fois !

Il suffit de brancher `turnSuperSaiyan` et d'obtenir un _nouveau tableau_ de Super Saiyan Goku, Vegeta et Trunks.

```js
superSaiyans = saiyans.map(turnSuperSaiyan);
```

![mapping-saiyans](https://www.freecodecamp.org/news/content/images/2019/07/mapping-saiyans.png)

## Pour un lycéen apprenant la codification
Salut !

Alors, tu as appris les boucles `for`. Elles sont géniales pour effectuer des travaux répétitifs, mais personnellement, je n'en ai pas eu besoin depuis des années.

Ne me comprends pas mal, j'adore toujours automatiser les travaux répétitifs. En fait, la plupart des applications impliquent des travaux répétitifs.

Pense à ces exemples...
* Instagram
* Whatsapp
* Résultats de recherche Google
* E-mails
* Contacts
* Messages texte


Si tu les réduis à l'essentiel, ces applications quotidiennes ne sont que des listes sophistiquées. Une grande partie du développement Front-End consiste à transformer ces listes en quelque chose de convivial.

Bien sûr, le tableau général est plus complexe, mais le cœur de la plupart des applications est la manipulation de listes !

Dans un programme JavaScript, nous représentons les listes sous forme de tableaux.

Tous les tableaux portent une méthode spéciale appelée `map`. Elle permet de transformer un tableau en un nouveau en fonction d'une fonction que tu lui donnes.

Voici quelques nombres.
```js
numbers = [1, 2, 3, 4, 5];
```

Et une fonction `double`.
```js
double = (x) => x * 2;
```

Peux-tu doubler chacun en utilisant une boucle `for` ?
```js
doubledNumbers = [];

for (let i = 0; i < numbers.length; i++) {
	doubledNumbers.push(double(numbers[i]))
}

// [2, 4, 6, 8, 10]
```

Cool ! Voici la même idée exprimée avec `map`.

```js
doubledNumbers = numbers.map(double);
// [2, 4, 6, 8, 10]
```

`map` construit la boucle en arrière-plan, donc tu n'as plus à t'inquiéter des fautes de frappe ou des points-virgules manquants !

![cant-forget-semis-if-you-forget-loops](https://www.freecodecamp.org/news/content/images/2019/07/cant-forget-semis-if-you-forget-loops.jpeg)

Et cela va au-delà des simples nombres. Voici quelques utilisateurs...

```js
users = [{
  name: 'Bruce Wayne',
  location: 'Gotham City',
  heroName: 'Batman'
}, {
  name: 'Barry Allen',
  location: 'Central City',
  heroName: 'The Flash'
}, {
  name: 'Clark Kent',
  location: 'Kryptonopolis',
  heroName: 'Superman'
}];
```

Comment créerais-tu un _nouveau tableau_ avec le `name` et le `heroName` de chaque utilisateur ? Probablement en utilisant une boucle `for`.

```js
userInfo = [];

for (let i = 0; i < users.length; i++) {
  userInfo.push({
    name: users[i].name,
    heroName: users[i].heroName
  });
}

// Résultat
[
  {
    "name": "Bruce Wayne",
    "heroName": "Batman"
  },
  {
    "name": "Barry Allen",
    "heroName": "The Flash"
  },
  {
    "name": "Clark Kent",
    "heroName": "Superman"
  }
]
```

Voici une version sans boucle.

```js
userInfo = users.map(u => ({
  name: u.name,
  heroName: u.heroName
}));

// Résultat
[
  {
    "name": "Bruce Wayne",
    "heroName": "Batman"
  },
  {
    "name": "Barry Allen",
    "heroName": "The Flash"
  },
  {
    "name": "Clark Kent",
    "heroName": "Superman"
  }
]
```

Tu vois comme c'est plus facile ? Nous pouvons implémenter `map` comme suit :
```js
map = (fn, array) => {
	const results = [];

	for (let i = 0; i < array.length; i++) {
		results.push(fn(array[i]));
	}

	return results;
}
```

Donc pour chaque élément, appelle la fonction donnée et stocke-la dans un nouveau tableau !


## Pour un développeur React
Salut !

Le prototype Array offre une méthode appelée `map`.

Elle va parcourir ton tableau, appeler une fonction donnée sur chaque élément, et retourner un nouveau tableau avec ces modifications.

Au lieu d'une boucle `for`, utilise simplement `map` pour obtenir les noms d'utilisateur et rendre l'UI.

```jsx
const App = users => {
  return (
    <ul>
      <li>Mon nom est {users.map(u => u.name)} !</li>
    </ul>
  );
};
```

Oui, tu peux enchaîner les méthodes, puisque cela retourne le même type !

```jsx
const App = users => {
  return (
    <ul>
      {users
        .map(u => u.name)
        .map(name => (
          <li>Mon nom est {name} !</li>
        ))}
    </ul>
  );
};
```

Très utile. La plupart de tes composants principaux utiliseront probablement `map`.

## Pour un développeur fonctionnel
Map élève simplement une fonction `a -> b` dans un contexte `F a -> F b`.

![functors](https://www.freecodecamp.org/news/content/images/2019/07/functors.png)

JavaScript ne va malheureusement pas au-delà des tableaux en termes d'expressivité...

![i-think-harold-gets-it](https://www.freecodecamp.org/news/content/images/2019/07/i-think-harold-gets-it.jpg)

Merci à Brian Lonsdorf pour [l'explication géniale](https://twitter.com/yazeedBee/status/1150108731759300608) !

Pour plus de contenu comme celui-ci, consulte <a href="https://yazeedb.com">https://yazeedb.com !</a>

Et fais-moi savoir ce que tu aimerais voir d'autre ! [Mes DM sont ouverts](https://twitter.com/yazeedBee) pour les questions, commentaires et suggestions !