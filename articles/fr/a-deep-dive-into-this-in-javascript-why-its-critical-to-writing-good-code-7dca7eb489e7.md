---
title: 'Une plongée en profondeur dans ''this'' en JavaScript : pourquoi c''est crucial
  pour écrire du bon code.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T18:19:50.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-this-in-javascript-why-its-critical-to-writing-good-code-7dca7eb489e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hVnCdEtqlQvHS1GTXbo5Xw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une plongée en profondeur dans ''this'' en JavaScript : pourquoi c''est
  crucial pour écrire du bon code.'
seo_desc: 'By Austin Tackaberry

  Using simple terminology and a real world example, this post explains what this
  is and why it is useful.

  Is this for you

  I have noticed that many explanations for this in JavaScript are taught assuming
  you are coming from some ob...'
---

Par Austin Tackaberry

En utilisant une terminologie simple et un exemple concret, cet article explique ce qu'est `this` et pourquoi il est utile.

### Est-ce pour vous

J'ai remarqué que de nombreuses explications sur `this` en JavaScript sont enseignées en supposant que vous venez d'un langage de programmation orienté objet comme Java, C++ ou Python. Cet article s'adresse à ceux d'entre vous qui n'ont aucune préconception de ce que vous pensez que `this` est ou devrait être. Je vais essayer d'expliquer **ce qu'est** `this` et **pourquoi** il est utile de manière simple, sans jargon inutile.

Peut-être avez-vous procrastiné pour plonger dans `this` parce que cela semblait bizarre et effrayant. Ou peut-être ne l'utilisez-vous que parce que StackOverflow dit que vous en avez besoin pour faire certaines choses dans React.

Avant de plonger dans ce qu'est vraiment `this` et pourquoi vous l'utiliseriez, nous devons d'abord comprendre la différence entre la programmation **fonctionnelle** et la programmation **orientée objet**.

### Programmation fonctionnelle vs orientée objet

Vous savez peut-être que JavaScript possède à la fois des constructions fonctionnelles et orientées objet, vous pouvez donc choisir de vous concentrer sur l'une ou l'autre ou d'utiliser les deux.

J'ai adopté la programmation fonctionnelle tôt dans mon parcours JavaScript et j'ai évité la programmation orientée objet comme la peste. Je ne connaissais ni ne comprenais les mots-clés orientés objet tels que `this`. Je pense qu'une des raisons pour lesquelles je ne comprenais pas était que je ne voyais pas vraiment pourquoi c'était nécessaire. Il semblait que je pouvais faire tout ce dont j'avais besoin sans dépendre de `this`.

Et j'avais raison.

En quelque sorte. Vous pouvez peut-être vous en sortir en vous concentrant uniquement sur un paradigme et en n'apprenant jamais l'autre, mais vous serez limité en tant que développeur JavaScript. Pour illustrer les différences entre la programmation fonctionnelle et orientée objet, je vais utiliser un tableau de données d'amis Facebook comme exemple.

Supposons que vous construisez une application web où l'utilisateur se connecte avec Facebook, et vous affichez certaines données concernant leurs amis Facebook. Vous devrez frapper un endpoint Facebook pour obtenir leurs données d'amis. Il pourrait avoir des informations telles que `firstName`, `lastName`, `username`, `numFriends`, `friendData`, `birthday`, et `lastTenPosts`.

```js
const data = [
  {
    firstName: 'Bob',
    lastName: 'Ross',
    username: 'bob.ross',    
    numFriends: 125,
    birthday: '2/23/1985',
    lastTenPosts: ['What a nice day', 'I love Kanye West', ...],
  },
  ...
]
```

Les données ci-dessus sont ce que vous obtenez de l'API Facebook (fictive et imaginaire). Maintenant, vous devez les transformer pour qu'elles soient dans un format utile pour vous et votre projet. Supposons que vous souhaitiez afficher les éléments suivants pour chacun des amis de l'utilisateur :

* Leur nom au format ``${firstName} ${lastName}``
* Trois publications aléatoires
* Nombre de jours jusqu'à leur anniversaire

### Approche fonctionnelle

Une approche fonctionnelle consisterait à passer le tableau entier ou chaque élément d'un tableau à une fonction qui retourne les données manipulées dont vous avez besoin :

```
const fullNames = getFullNames(data)
// ['Ross, Bob', 'Smith, Joanna', ...]
```

Vous commencez avec des données brutes (de l'API Facebook). Pour les transformer en données utiles, vous passez les données à une fonction et la sortie est ou inclut les données manipulées que vous pouvez utiliser dans votre application pour les afficher à l'utilisateur.

Vous pourriez imaginer faire quelque chose de similaire pour obtenir les trois publications aléatoires et calculer le nombre de jours jusqu'à l'anniversaire de cet ami.

**L'approche fonctionnelle consiste à prendre vos données brutes, à les passer à travers une fonction ou plusieurs fonctions, et à produire des données utiles pour vous et votre projet.**

### Approche orientée objet

L'approche orientée objet peut être un peu plus difficile à comprendre pour ceux qui sont nouveaux en programmation et apprennent JavaScript. L'idée ici est que vous transformez chaque ami **en** un objet qui a tout ce dont il a besoin pour générer ce dont **vous**, en tant que développeur, avez besoin.

Vous pourriez créer des objets qui ont une propriété `fullName`, et deux fonctions `getThreeRandomPosts` et `getDaysUntilBirthday` qui sont spécifiques à cet ami.

```js
function initializeFriend(data) {
  return {
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // obtenir trois publications aléatoires de data.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // utiliser data.birthday pour obtenir le nombre de jours jusqu'à l'anniversaire
    }
  };
}
const objectFriends = data.map(initializeFriend)
objectFriends[0].getThreeRandomPosts() 
// Obtient trois publications de Bob Ross
```

**L'approche orientée objet consiste à créer des objets pour vos données qui ont un état et incluent toutes les informations dont ils ont besoin pour générer les données utiles pour vous et votre projet.**

### Quel est le rapport avec 'this' ?

Vous n'avez peut-être jamais pensé à écrire quelque chose comme `initializeFriend` ci-dessus, et vous pourriez penser que quelque chose comme cela pourrait être assez utile. Vous pourriez également remarquer, cependant, que ce n'est pas **vraiment** orienté objet.

La seule raison pour laquelle les méthodes `getThreeRandomPosts` ou `getDaysUntilBirthday` fonctionneraient dans l'exemple ci-dessus est à cause de la fermeture. Elles ont toujours accès à `data` après que `initializeFriend` retourne à cause de la fermeture. Pour plus d'informations sur la fermeture, consultez [You Dont Know JS: Scope & Closures](https://github.com/getify/You-Dont-Know-JS/blob/master/scope%20%26%20closures/ch5.md).

Et si vous aviez une autre méthode, appelons-la `greeting`. Notez qu'une méthode (en ce qui concerne un objet en JavaScript) est simplement un attribut dont la valeur est une fonction. Nous voulons que `greeting` fasse quelque chose comme ceci :

```js
function initializeFriend(data) {
  return {
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // obtenir trois publications aléatoires de data.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // utiliser data.birthday pour obtenir le nombre de jours jusqu'à l'anniversaire
    },
    greeting: function() {
      return `Hello, this is ${fullName}'s data!`
    }
  };
}
```

Est-ce que cela fonctionnera ?

Non !

Tout dans notre nouvel objet a accès à toutes les variables dans `initializeFriend` mais PAS à l'un des attributs ou méthodes au sein de l'objet lui-même. Certaines, vous poserez la question :

> Ne pourriez-vous pas simplement utiliser `data.firstName` et `data.lastName` pour retourner votre salutation ?

Oui, vous pourriez absolument. Mais que faire si nous voulions également inclure dans la salutation le nombre de jours jusqu'à l'anniversaire de cet ami ? Nous devrions trouver un moyen d'appeler `getDaysUntilBirthday` depuis `greeting`.

C'EST LE MOMENT POUR `this` !

![Image](https://cdn-media-1.freecodecamp.org/images/CjfAp0G6O8yFJPu4aKOV8tvPjs2kt0eCaWct)
_Photo par [Unsplash](https://unsplash.com/photos/geM5lzDj4Iw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">sydney Rae</a> sur <a href="https://unsplash.com/search/photos/this?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Enfin, qu'est-ce que 'this'

`this` peut faire référence à différentes choses selon les circonstances. Par défaut, `this` fait référence à l'objet global (dans le navigateur, il s'agit de l'objet `window`), ce qui n'est pas très utile. La règle `this` qui nous est utile pour l'instant est la suivante :

**Si `this` est utilisé dans une méthode d'objet et que la méthode est appelée dans le contexte de cet objet, `this` fait référence à l'objet lui-même.**

> Vous dites « appelé dans le contexte de cet objet »... qu'est-ce que cela signifie ?

Ne vous inquiétez pas, nous y viendrons plus tard !

Donc, si nous voulions appeler `getDaysUntilBirthday` depuis `greeting`, nous pouvons simplement appeler `this.getDaysUntilBirthday` car `this` dans ce scénario fait simplement référence à l'objet lui-même.

NOTE DE CÔTÉ : N'utilisez pas `this` dans une fonction régulière dans la portée globale ou dans la portée d'une autre fonction ! `this` est une construction orientée objet. Par conséquent, il n'a de sens que dans le contexte d'un objet (ou d'une classe) !

Refactorisons `initializeFriend` pour utiliser `this` :

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // obtenir trois publications aléatoires de this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // utiliser this.birthday pour obtenir le nombre de jours jusqu'à l'anniversaire
    },
    greeting: function() {
      const numDays = this.getDaysUntilBirthday()      
      return `Hello, this is ${this.fullName}'s data! It is ${numDays} until ${this.fullName}'s birthday!`
    }
  };
}
```

Maintenant, tout ce dont cet objet a besoin est limité à l'objet lui-même une fois que `intializeFriend` est exécuté. Nos méthodes ne dépendent plus de la fermeture. Elles n'utilisent que les informations contenues dans l'objet lui-même.

> Ok, donc c'est une façon d'utiliser `this`, mais vous avez dit que `this` peut être beaucoup de choses différentes selon le contexte. Qu'est-ce que cela signifie ? Pourquoi ne ferait-il pas toujours référence à l'objet lui-même ?

Il y a des moments où vous voulez forcer `this` à être quelque chose de particulier. Un bon exemple est pour les gestionnaires d'événements. Supposons que nous voulions ouvrir la page Facebook d'un ami lorsque l'utilisateur clique dessus. Nous pourrions ajouter une méthode `onClick` à notre objet :

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,
    username: data.username,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // obtenir trois publications aléatoires de this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // utiliser this.birthday pour obtenir le nombre de jours jusqu'à l'anniversaire
    },
    greeting: function() {
      const numDays = this.getDaysUntilBirthday()      
      return `Hello, this is ${this.fullName}'s data! It is ${numDays} until ${this.fullName}'s birthday!`
    },
    onFriendClick: function() {
      window.open(`https://facebook.com/${this.username}`)
    }
  };
}
```

Remarquez que nous avons ajouté `username` à notre objet, afin que `onFriendClick` y ait accès, pour que nous puissions ouvrir une nouvelle fenêtre avec la page Facebook de cet ami. Maintenant, nous devons simplement écrire le HTML :

```html
<button id="Bob_Ross">
  <!-- Un tas d'informations associées à Bob Ross -->
</button> 
```

Et maintenant le JavaScript :

```js
const bobRossObj = initializeFriend(data[0])
const bobRossDOMEl = document.getElementById('Bob_Ross')
bobRossDOMEl.addEventListener("onclick", bobRossObj.onFriendClick)
```

Dans le code ci-dessus, nous créons un objet pour Bob Ross. Nous obtenons l'élément DOM associé à Bob Ross. Et maintenant nous voulons exécuter la méthode `onFriendClick` pour ouvrir la page Facebook de Bob. Cela devrait fonctionner comme prévu, n'est-ce pas ?

Non !

Qu'est-ce qui a mal tourné ?

Remarquez que la fonction que nous avons choisie pour le gestionnaire onclick était `bobRossObj.onFriendClick`. Voyez-vous le problème maintenant ? Et si nous la réécrivions comme ceci :

```js
bobRossDOMEl.addEventListener("onclick", function() {  window.open(`https://facebook.com/${this.username}`)})bobRossDOMEl.addEventListener("onclick", function() {
  window.open(`https://facebook.com/${this.username}`)
})
```

Maintenant, voyez-vous le problème ? Lorsque nous avons défini le gestionnaire onclick pour être `bobRossObj.onFriendClick`, ce que nous faisons réellement est de prendre la fonction qui est stockée dans `bobRossObj.onFriendClick` et de la passer en tant qu'argument. Elle n'est plus « attachée » à `bobRossObj`, ce qui signifie que `this` ne fait plus référence à `bobRossObj`. Il fait réellement référence à l'objet global, ce qui signifie que `this.username` est indéfini. Il semble que nous soyons sans chance à ce stade.

C'EST LE MOMENT pour `bind` !

![Image](https://cdn-media-1.freecodecamp.org/images/o36QYF-UudyA0jO8JbooQYneFJo5jeA2oAtS)
_Photo par [Unsplash](https://unsplash.com/photos/KiAZ61Sh17k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ksenia Makagonova</a> sur <a href="https://unsplash.com/search/photos/rope?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Liaison explicite de 'this'

Ce que nous devons faire, c'est lier explicitement `this` à `bobRossObj`. Nous pouvons le faire en utilisant `bind` :

```js
const bobRossObj = initializeFriend(data[0])
const bobRossDOMEl = document.getElementById('Bob_Ross')
bobRossObj.onFriendClick = bobRossObj.onFriendClick.bind(bobRossObj)
bobRossDOMEl.addEventListener("onclick", bobRossObj.onFriendClick)
```

Auparavant, `this` était défini en fonction de la règle par défaut. Avec l'utilisation de `bind`, nous définissons explicitement la valeur de `this` dans `bobRossObj.onFriendClick` pour qu'elle soit l'objet lui-même, ou `bobRossObj`.

Jusqu'à présent, nous avons vu pourquoi `this` est utile et pourquoi vous pourriez vouloir lier explicitement `this`. Le dernier sujet que nous aborderons concernant `this` est les fonctions fléchées.

### Fonctions fléchées

Vous avez peut-être remarqué que les fonctions fléchées sont la nouvelle tendance. Les gens semblent les aimer parce qu'elles sont concises et élégantes. Vous savez peut-être qu'elles sont un peu différentes des fonctions normales, mais peut-être que vous ne savez pas exactement quelle est la différence.

Peut-être que la manière la plus simple de décrire comment les fonctions fléchées sont différentes est la suivante :

**Quoi que `this` fasse référence à l'endroit où une fonction fléchée est déclarée, `this` fait référence à la même chose à l'intérieur de cette fonction fléchée.**

> Ok... ce n'est pas utile... Je pensais que c'était le comportement d'une fonction normale ?

Expliquons avec notre exemple `initializeFriend`. Supposons que nous voulions ajouter une petite fonction d'aide dans `greeting` :

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,
    username: data.username,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // obtenir trois publications aléatoires de this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // utiliser this.birthday pour obtenir le nombre de jours jusqu'à l'anniversaire
    },
    greeting: function() {
      function getLastPost() {
        return this.lastTenPosts[0]
      }
      const lastPost = getLastPost()           
      return `Hello, this is ${this.fullName}'s data!
             ${this.fullName}'s last post was ${lastPost}.`
    },
    onFriendClick: function() {
      window.open(`https://facebook.com/${this.username}`)
    }
  };
}
```

Cela fonctionnerait-il ? Si non, comment pourrions-nous le changer pour qu'il fonctionne ?

Non, cela ne fonctionnera pas. Parce que `getLastPost` n'est pas appelé dans le contexte d'un objet, `this` à l'intérieur de `getLastPost` revient à la règle par défaut qui est l'objet global.

> Vous dites qu'il n'est pas appelé « dans le contexte d'un objet »... ne savez-vous pas qu'il est appelé à l'intérieur de l'objet qui est retourné par `initializeFriend` ? Si ce n'est pas appelé « dans le contexte d'un objet », alors je ne sais pas ce que c'est.

Je sais que « dans le contexte d'un objet » est une terminologie vague. Peut-être qu'une bonne façon de déterminer si une fonction est appelée « dans le contexte d'un objet » est de vous parler à travers comment la fonction est appelée et de déterminer si un objet est « attaché » à la fonction.

Parlons de ce qui se passe lorsque nous exécutons `bobRossObj.onFriendClick()`. « Prends-moi l'objet `bobRossObj`, cherche l'attribut `onFriendClick` et **appelle la fonction assignée à cet attribut** ».

Maintenant, parlons de ce qui se passe lorsque nous exécutons `getLastPost()`. « Prends-moi la fonction avec le nom `getLastPost` et appelle-la. » Remarquez comment il n'y a eu aucune mention d'un objet ?

D'accord, voici un cas délicat pour tester vos connaissances. Supposons qu'il y a une fonction `functionCaller` où tout ce qu'elle fait est d'appeler des fonctions :

```js
functionCaller(fn) {
  fn()
}
```

Et si nous faisions ceci : `functionCaller(bobRossObj.onFriendClick)` ? Diriez-vous que `onFriendClick` a été appelé « dans le contexte d'un objet » ? `this.username` serait-il défini ?

Parlons-en : « Prends l'objet `bobRossObj` et cherche l'attribut `onFriendClick`. Prends sa valeur (qui se trouve être une fonction), passe-la dans `functionCaller`, et nomme-la `fn`. Maintenant, exécute la fonction nommée `fn`. » Remarquez que la fonction est « détachée » de `bobRossObj` avant d'être appelée et n'est donc pas appelée « dans le contexte de l'objet `bobRossObj` », ce qui signifie que `this.username` sera indéfini.

Les fonctions fléchées à la rescousse :

```js
function initializeFriend(data) {
  return {
    lastTenPosts: data.lastTenPosts,
    birthday: data.birthday,
    username: data.username,    
    fullName: `${data.firstName} ${data.lastName}`,
    getThreeRandomPosts: function() {
      // obtenir trois publications aléatoires de this.lastTenPosts
    },
    getDaysUntilBirthday: function() {
      // utiliser this.birthday pour obtenir le nombre de jours jusqu'à l'anniversaire
    },
    greeting: function() {
      const getLastPost = () => {
        return this.lastTenPosts[0]
      }
      const lastPost = getLastPost()           
      return `Hello, this is ${this.fullName}'s data!
             ${this.fullName}'s last post was ${lastPost}.`
    },
    onFriendClick: function() {
      window.open(`https://facebook.com/${this.username}`)
    }
  };
}
```

Notre règle ci-dessus :

**Quoi que `this` fasse référence à l'endroit où une fonction fléchée est déclarée, `this` fait référence à la même chose à l'intérieur de cette fonction fléchée.**

La fonction fléchée est déclarée à l'intérieur de `greeting`. Nous savons que lorsque nous utilisons `this` dans `greeting`, il fait référence à l'objet lui-même. Par conséquent, `this` à l'intérieur de la fonction fléchée fait référence à l'objet lui-même, ce que nous voulons.

### Conclusion

`this` est un outil parfois confus mais utile pour développer des applications JavaScript. Ce n'est certainement pas tout ce qu'il y a à savoir sur `this`. Certains sujets qui n'ont pas été abordés sont :

* `call` et `apply`
* comment `this` change lorsque `new` est impliqué
* comment `this` change avec la `class` ES6

Je vous encourage à vous poser des questions sur ce que vous pensez que `this` devrait être dans certaines situations, puis à vous tester en exécutant ce code dans le navigateur. Si vous voulez en savoir plus sur `this`, consultez [You Dont Know JS: this & Object Prototypes](https://github.com/getify/You-Dont-Know-JS/tree/master/this%20%26%20object%20prototypes).

Et si vous voulez vous tester, consultez [YDKJS Exercises: this & Object Prototypes](https://ydkjs-exercises.com/this-object-prototypes).

![Image](https://cdn-media-1.freecodecamp.org/images/6MubkHTI9p32BuBFH5wqv-Sqp2DQBxLPhdDj)
_Photo par [Unsplash](https://unsplash.com/photos/0FRJ2SCuY4k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jonas Jacobsson</a> sur <a href="https://unsplash.com/search/photos/books?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_