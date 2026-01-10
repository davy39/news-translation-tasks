---
title: Yield! Yield! Comment fonctionnent les générateurs en JavaScript.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T16:32:59.000Z'
originalURL: https://freecodecamp.org/news/yield-yield-how-generators-work-in-javascript-3086742684fc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Ts8-usYa-T4lL8yc
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Yield! Yield! Comment fonctionnent les générateurs en JavaScript.
seo_desc: 'By Ashay Mandwarya ?️??

  If the title doesn’t already give a hint, we will be discussing generators in this
  piece.

  Before going into generators let’s revise some basics about functions.


  In JavaScript, functions are a set of statements that perform a ...'
---

Par Ashay Mandwarya 👨💻🚀

Si le titre ne donne pas déjà un indice, nous allons discuter des générateurs dans cet article.

Avant de plonger dans les générateurs, révisons quelques bases sur les fonctions.

* En JavaScript, les fonctions sont un ensemble d'instructions qui effectuent une tâche et retournent une valeur, mettant fin à la fonction.
* Si vous appelez une fonction encore et encore, elle exécutera toutes les instructions encore et encore.
* Les flèches, une fois tirées de l'arc, ne peuvent pas être arrêtées — elles ne font que toucher ou manquer. De la même manière, une fonction, une fois appelée, ne peut pas être arrêtée, elle s'exécutera, retournera une valeur, lancera une erreur et s'arrêtera après avoir exécuté toutes les instructions.

Nous devons seulement garder à l'esprit ces 3 points pour comprendre les générateurs.

### Générateurs

Un générateur est un type spécial de fonction qui peut arrêter son exécution à mi-chemin et redémarrer à partir du même point après un certain temps. Les générateurs sont une combinaison de fonctions et d'itérateurs. C'est une déclaration un peu confuse, mais je m'assurerai que cette ligne sera claire à la fin de l'article.

Pour plus de clarté, imaginez jouer à un jeu et soudainement votre mère vous appelle pour faire quelque chose. Vous mettez le jeu en pause, vous l'aidez, puis vous reprenez le jeu. C'est la même chose avec les générateurs.

> Un **itérateur** est un objet qui définit une séquence et potentiellement une valeur de retour à sa terminaison. — MDN.

_Les itérateurs en eux-mêmes sont un sujet vaste et ne sont pas l'objectif de cet article._

#### Syntaxe de base

Les générateurs sont définis comme une fonction avec un astérisque (*) à côté de la fonction.

```
function* nom(arguments) {   instructions}
```

**nom** — Le nom de la fonction.

**arguments** — Les arguments de la fonction.

**instructions** — Le corps de la fonction.

#### Retour

Une fonction peut retourner presque n'importe quoi, allant d'une valeur, d'un objet ou d'une autre fonction elle-même. Une fonction générateur retourne un objet spécial appelé l'objet générateur (_pas entièrement vrai_). L'objet ressemble au snippet ci-dessous

```
{   value: valeur,  done: true|false}
```

L'objet a deux propriétés `value` et `done`. La valeur contient la valeur à être **yieldée**. Done consiste en un **Booléen (true|false)** qui indique au générateur si **.next()** va yielder une valeur ou **undefined**.

La déclaration ci-dessus sera difficile à digérer. Changeons cela avec un exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/2GKCXYgOAdydbo5qaKeXPayVwUXMpDPPzY1p)

```
function* generateur(e) {  yield e + 10;  yield e + 25;  yield e + 33;}var generer = generateur(27);
```

```
console.log(generer.next().value); // 37console.log(generer.next().value); // 52console.log(generer.next().value); // 60console.log(generer.next().value); // undefined
```

Comprenons la mécanique du code ci-dessus ligne par ligne.

**_lignes 1–5:_** Les lignes 1–5 définissent le générateur ayant le même nom avec un argument e. À l'intérieur du corps de la fonction, il contient un ensemble d'instructions avec le mot-clé yield et une opération est effectuée après cela.

**_ligne 6:_** La ligne 6 assigne le générateur à une variable appelée generer.

**_lignes 8–11:_** Ces lignes appellent un ensemble de `console.log` chacun appelant le générateur enchaîné à une méthode `next` qui appelle la propriété `value` de l'objet générateur.

![Image](https://cdn-media-1.freecodecamp.org/images/cafqdPSIaj55dp6A5GaErDFtrS0LueYhf87K)

Chaque fois qu'une fonction générateur est appelée, contrairement aux fonctions normales, elle ne commence pas l'exécution immédiatement. Au lieu de cela, un itérateur est retourné (_la vraie raison pour laquelle * est utilisé par un générateur. Il indique à JS qu'un objet itérateur doit être retourné_). Lorsque la méthode `next()` de l'itérateur est appelée, l'exécution du générateur commence et s'exécute jusqu'à ce qu'il trouve la première instruction `yield`. À ce point de yield, l'objet générateur est retourné, dont les spécifications sont déjà expliquées. Appeler à nouveau la fonction `next()` reprendra la fonction générateur jusqu'à ce qu'elle trouve une autre instruction `yield` et le cycle se répète jusqu'à ce que tous les `yields` soient épuisés.

![Image](https://cdn-media-1.freecodecamp.org/images/b8YEAKz8FN0BiZTL-9nWtahqnChK1A0dcnIa)

Après ce point, si `next` est appelé, il retourne l'objet générateur avec une valeur indéfinie.

Maintenant, essayons de yielder une autre fonction générateur à partir du générateur original et aussi une instruction return.

![Image](https://cdn-media-1.freecodecamp.org/images/cwoYBqzWffwSM5RCEJAUzpsPs-U39zfe6EV1)

Une instruction `return` dans un générateur fera terminer l'exécution du générateur comme toute autre fonction. La propriété `done` de l'objet générateur sera définie sur `true` et la valeur retournée sera définie sur la propriété `value` de l'objet générateur. Tous les autres `yields` retourneront `undefined`.

Si une erreur est lancée, l'exécution du générateur s'arrêtera également, yielder un générateur lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/VtjqhfNkczhAnzaY7BmLV1Y7fLs0Du3cVzQP)

Pour `yield` un générateur, nous devons spécifier un * contre le `yield` afin de dire à JS qu'un générateur est yieldé. Le `[yield*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)` délègue à une autre fonction générateur — c'est la raison pour laquelle nous pouvons `yield` toutes les valeurs de la fonction `generateur2` en utilisant le `generer.next()` de la fonction générateur originale. La première valeur `yieldée` provient de la première fonction générateur et les deux dernières valeurs `yieldées` sont générées par la fonction générateur mais `yieldées` par le générateur original.

#### Avantages

**Chargement paresseux**

Le chargement paresseux est essentiellement l'évaluation de la valeur uniquement lorsqu'il y a un besoin. Comme nous le verrons dans un exemple à venir, nous pouvons réellement le faire avec des générateurs. Nous pouvons ne yielder les valeurs que lorsque cela est nécessaire et non toutes en même temps.

L'exemple ci-dessous provient d'un autre exemple dans cet article et il génère des nombres aléatoires infinis. Ici, nous pouvons voir que nous pouvons appeler autant de `next()` que nous voulons et ne pas obtenir toutes les valeurs qu'il produit. Seulement celles qui sont nécessaires.

![Image](https://cdn-media-1.freecodecamp.org/images/0uRO5-e1uAChjJR9-m21IhjV46cZ7tzH10Xl)

```
function * aleatoire() {  while (true) {let aleatoire = Math.floor(Math.random()*1000);    yield aleatoire;  }}
```

```
var aleatoire= aleatoire();
```

```
console.log(aleatoire.next().value)
```

**Efficace en mémoire**

Comme nous pouvons le déduire de l'exemple ci-dessus, les générateurs sont extrêmement efficaces en mémoire. Comme nous voulons les valeurs uniquement selon les besoins, nous avons besoin de très peu de stockage pour stocker ces valeurs.

#### Pièges

Les générateurs sont extrêmement utiles mais ont aussi leurs propres pièges.

* **Les générateurs ne fournissent pas d'accès aléatoire** comme les tableaux et autres structures de données. Comme les valeurs sont yieldées une par une à l'appel, nous ne pouvons pas accéder à des éléments aléatoires.
* **Les générateurs fournissent un accès unique.** Les générateurs ne vous permettent pas d'itérer les valeurs encore et encore. Une fois que toutes les valeurs sont épuisées, nous devons créer une nouvelle instance de générateur pour itérer toutes les valeurs à nouveau.

#### Pourquoi avons-nous besoin des générateurs ?

Les générateurs offrent une grande variété d'utilisations en JavaScript. Essayons de recréer quelques-unes nous-mêmes.

**Implémentation des itérateurs**

> **Un itérateur** est un objet qui permet à un programmeur de parcourir un conteneur -Wikipedia

Nous allons imprimer tous les mots présents dans une chaîne de caractères en utilisant des itérateurs. Les chaînes de caractères sont aussi des itérateurs.

**Itérateurs**

![Image](https://cdn-media-1.freecodecamp.org/images/jxlJeu0eRnrbnVoQQiUnQWuW6WRqy6lewlui)

```
const chaine = 'abcde';const iterateur = chaine[Symbol.iterator]();console.log(iterateur.next().value)console.log(iterateur.next().value)console.log(iterateur.next().value)console.log(iterateur.next().value)console.log(iterateur.next().value)
```

Voici la même chose en utilisant des générateurs

![Image](https://cdn-media-1.freecodecamp.org/images/BLoMgkxRn2Um8XnncvONthkIzSnwnDtLZxtd)

```
function * iterateur() {yield 'a';yield 'b';yield 'c';yield 'd';yield 'e';}for (let x of iterateur()) {console.log(x);}
```

En comparant les deux méthodes, il est facile de voir qu'avec l'aide des générateurs, nous pouvons le faire avec moins d'encombrement. Je sais que ce n'est pas un très bon exemple, mais suffisant pour prouver les points suivants :

* Pas d'implémentation de `next()`
* Pas d'invocation de `[Symbol.iterator]()`
* Dans certains cas, nous devons même définir la valeur de retour de la propriété `object.done` sur true/false en utilisant des itérateurs.

#### Async-Await ~ Promesses+Générateurs

Vous pouvez lire mon [précédent](https://medium.com/@ashaymurceilago/async-await-javascript-5038668ec6eb) article sur Async/Await si vous voulez en apprendre davantage sur eux, et consulter [celui-ci](https://medium.com/javascript-in-plain-english/truly-understanding-promises-in-javascript-cb31ee487860) pour les Promesses.

De manière brute, Async/Await est simplement une implémentation de Générateurs utilisée avec des Promesses.

Async-Await

```
async function async-await(){let a=await(tache1);console.log(a);
```

```
let b=await(tache2);console.log(b);
```

```
let c=await(tache3);console.log(c);
```

```
}
```

Promesses+Générateurs

```
function * generateur-promesse(){let a=yield Promesse1();console.log(a);let b=yield Promesse1();console.log(b);let c=yield Promesse1();console.log(c);
```

```
}
```

Comme nous pouvons le voir, les deux produisent le même résultat et presque de la même manière. C'est parce que le mécanisme Async/Await est vaguement basé sur une combinaison de générateurs et de promesses. Il y a beaucoup plus à Async/Await que ce qui est montré ci-dessus, mais juste pour montrer l'utilisation d'un générateur, nous pouvons considérer cela.

#### Structure de données infinie

Le titre peut être un peu trompeur, mais c'est vrai. Nous pouvons créer des générateurs, avec l'utilisation d'une boucle while qui ne se terminera jamais et qui yieldera toujours une valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/ximCs8aJ4EUtQfo8AAPza6eRK9IAUd70QLCN)

```
function * aleatoire() {  while (true) {let aleatoire = Math.floor(Math.random()*1000);    yield aleatoire;  }}var aleatoire= aleatoire();while(true)console.log(aleatoire.next().value)
```

Dans l'extrait ci-dessus, nous créons un générateur infini, qui yieldera un nombre aléatoire à chaque invocation de `next()`. Il peut être appelé comme un flux infini de nombres aléatoires. C'est un exemple très basique.

### Conclusion

Il reste encore beaucoup à couvrir sur les générateurs, et ceci n'était qu'une introduction au sujet. J'espère que vous avez appris quelque chose de nouveau et que l'article était facile à comprendre.

Suivez-moi et applaudissez !

![Image](https://cdn-media-1.freecodecamp.org/images/dagqbne49wWylj3wlhZWGKij2pXISMlkKyn6)