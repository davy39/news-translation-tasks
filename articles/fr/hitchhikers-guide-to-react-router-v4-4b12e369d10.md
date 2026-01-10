---
title: 'Le Guide du voyageur à React Router v4 : [match, location, history] — vos
  meilleurs amis !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-02T13:41:46.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YhuuQPVUvZ_fVSA7
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Le Guide du voyageur à React Router v4 : [match, location, history] —
  vos meilleurs amis !'
seo_desc: 'By Eduardo Vedes

  Hey! Welcome to the Hitchhiker’s Guide to React Router v4, Part II!

  Now that we’ve set the ball rolling with our first small App, let’s focus on your
  three travel mates: match, location and history.

  What happens if you get inside you...'
---

Par Eduardo Vedes

### Salut ! Bienvenue dans le Guide du voyageur à React Router v4, Partie II !

Maintenant que nous avons [lancé la balle](https://medium.freecodecamp.org/hitchhikers-guide-to-react-router-v4-a957c6a5aa18) avec notre première petite application, concentrons-nous sur vos trois compagnons de voyage : **match**, **location** et **history**.

Que se passe-t-il si vous entrez dans le code de votre composant Home et que vous y placez un _console.log_ pour vérifier les props ?

![Image](https://cdn-media-1.freecodecamp.org/images/nHKRAkDljCjDcqgGQ5MbtVorvtcnAddzIdDb)
_**console.log(props) à l'intérieur du composant &lt;Home /&gt;**_

Router introduit dans votre composant les objets suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/6LMI81YyC97GbgkqkALwuHgL9gRWruaxhF6u)
_console.log(props) résultat dans la console Chrome_

Wow ! D'où cela vient-il ? ?

Eh bien, chaque vue, composant, ou autre chose qui est enveloppé par Router a ces objets. **<Router/>** fait son travail en tant que composant d'ordre supérieur et enveloppe vos composants ou vues et injecte ces trois objets en tant que props à l'intérieur.

Alors... pourquoi sont-ils là et quelle utilisation puis-je en faire ? ?

Ils seront vos meilleurs amis ! Faites-moi confiance ! ?

### **Match**

L'objet **match** contient des informations sur la façon dont un **<Route path>** a correspondu à l'URL.

* **params** : (object), paires clé/valeur analysées à partir de l'URL correspondant aux segments dynamiques du chemin
* **isExact** : (boolean), vrai si l'URL entière a été correspondante (aucun caractère de fin)
* **path** : (string), le modèle de chemin utilisé pour la correspondance. Utile pour construire des routes imbriquées. Nous y jetterons un coup d'œil plus tard dans l'un des prochains articles.
* **url** : (string), la portion correspondante de l'URL. Utile pour construire des liens imbriqués.

Donc dans le composant **Home**, nous avons cet objet **match** :

![Image](https://cdn-media-1.freecodecamp.org/images/uHh5Y5m7cDC7jIR7H7n8py4nDU2ffGdhjKAt)
_**objet match à l'intérieur du composant Home**_

**isExact** est vrai parce que l'URL entière a été correspondante, l'objet **params** est vide parce que nous n'avons rien passé dedans, les valeurs des clés **path** et **url** sont égales confirmant que **isExact** est vrai.

Maintenant, jetons un coup d'œil à la **Vue TopicList** :

![Image](https://cdn-media-1.freecodecamp.org/images/b8EZtA2VpFlxdsLyycjIWhoX9JRh1o5usrPs)
_**Code de la vue TopicList**_

![Image](https://cdn-media-1.freecodecamp.org/images/xddWSXptrwdcsqjl9iIZuZlWIP7QOfI5lyg2)
_**console.log(match) à l'intérieur de la vue TopicList**_

Rien de nouveau jusqu'à présent, même histoire que dans la **Vue Home**, montrant le **path** et l'**url** de **TopicList**.

Mais que se passe-t-il si nous jetons un coup d'œil à **TopicDetails** ?

![Image](https://cdn-media-1.freecodecamp.org/images/7HqUri6J58zzX0A2Ibee8gG44OdjhDQkhXNo)
_**TopicDetails**_

![Image](https://cdn-media-1.freecodecamp.org/images/wpl-oFxuzOEW2DNVAuFd-ShAK-yLTZ8xj0xb)
_**console.log(match) à l'intérieur de TopicDetails**_

D'accord, que avons-nous ici ?

**isExact** continue d'être vrai parce que l'URL entière a été correspondante. L'objet **params** apporte l'information **topicId** qui a été passée dans le composant.

![Image](https://cdn-media-1.freecodecamp.org/images/0xEFd2yRpU30Zkh4Wdd5NpZJjcpsngQPKFyB)
_Route pour le composant TopicDetail dans routes.js_

Faites attention à la façon dont **topicId** est une variable.

Mais où prend-il la valeur **Topic1** ?

Simple, vous l'invoquez de manière explicite dans les **Liens TopicList**.

Vérifiez comment nous avons utilisé **match** pour **TopicList** pour connaître son URL.

![Image](https://cdn-media-1.freecodecamp.org/images/v2DiZPFGU7SdipLFW56Ojtz2R2Xi8hmPxqYA)

Ce lien pourrait être **dynamique**. Plus tard, nous ferons un exemple où vous **Liez** à un chemin relatif où vous ne savez pas auparavant si c'est **Topic1** ou **Topic3520**.

Mais...

Dans quelle situation **isExact** est-il faux ?

Eh bien... laissez-moi vous donner un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/tBPCHxskUCJOaLM3o7qKXPkTyFUE4fSIMr1d)
_**exemple où isExact est faux**_

Dans cette situation, nous avons introduit **/HelloWorldSection** dans l'URL du navigateur.

Ce qui se passe, c'est que le Router ne connaît pas le chemin complet vers **HelloWorldSection**, donc il vous route jusqu'à l'endroit où il connaît le chemin.

**isExact** montre faux, vous indiquant précisément que "**l'URL entière n'a pas été correspondante**".

C'est très utile, comme vous le verrez dès que vous commencerez à faire des SPAs avec RRv4 !

Juste pour terminer notre approche de **match**, vérifiez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/nYP-RV9WCaUtjbnurwmOgO6XXTMqLCx4iDMH)
_**Code de TopicDetails**_

Nous avons utilisé **match.params.topicId** pour afficher à l'écran le nom de notre sujet.

C'est l'une des utilisations les plus courantes pour **match**.

Bien sûr, il a une multitude d'applications. Supposons que nous devons récupérer une API avec cette information **topicId**. ?

### **Location**

L'objet **location** représente où se trouve l'application maintenant, où vous voulez qu'elle aille, ou même où elle était.

Il se trouve également sur **history.location**, mais vous ne devriez pas l'utiliser car il est mutable.

Un objet **location** n'est jamais muté, donc vous pouvez l'utiliser dans les hooks de cycle de vie pour déterminer quand la navigation se produit. Cela est vraiment utile pour la récupération de données ou les effets secondaires du **DOM**.

Faisons un _console.log(location)_ à l'intérieur de la **Vue Home** :

![Image](https://cdn-media-1.freecodecamp.org/images/ZH7dpyNWt8oOe4L0AbF--pLAysezPkJlJAqg)
_**console.log(location) à l'intérieur de la Vue Home**_

Ne plongeons pas trop profondément et restons avec sa fonctionnalité simple.

Vous avez la clé/valeur **pathname**.

Vous pouvez l'utiliser, par exemple, pour vérifier si **pathname** a changé :

![Image](https://cdn-media-1.freecodecamp.org/images/Fs8NVjFmantqRIJqxNK6ekxDVUFDxUx5ZTIH)
_**utilisation de location à l'intérieur de la méthode de cycle de vie componentDidUpdate()**_

Vous pouvez **<Link/>** ou **<Redirect />** vers celui-ci. Vous pouvez faire un history.push ou history.replace comme nous allons le voir plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/H3q-WXDs49wRkMD4KbsQorU4FMS6R2lN1C75)

Vous pouvez créer un objet personnalisé et l'utiliser

* **<Redirect to={locationX} />**
* **<Link to={locationX}/>**
* **history.push(locationX)**

Vous pouvez également le passer dans les composants **<Route/>** et **<Switch />**.

Cela les empêchera d'utiliser l'emplacement réel dans l'état du routeur. Peut-être voulez-vous tromper un composant pour qu'il s'affiche à un endroit différent de celui réel ?

Assez parlé de location maintenant...

Passons à **history** !

### **History**

L'objet **history** vous permet de gérer et de manipuler l'historique du navigateur à l'intérieur de vos vues ou composants.

* **length** : (number), le nombre d'entrées dans la pile d'historique
* **action** : (string), l'action actuelle (PUSH, REPLACE ou POP)
* **location** : (object), l'emplacement actuel
* **push(path, [state])** : (function), pousse une nouvelle entrée sur la pile d'historique
* **replace(path, [state])** : (function), remplace l'entrée actuelle sur la pile d'historique
* **go(n)** : (function), déplace le pointeur dans la pile d'historique de n entrées
* **goBack()** : (function), équivalent à go(-1)
* **goForward()** : (function), équivalent à go(1)
* **block(prompt)** : (function), empêche la navigation

Alors, faisons un console.log de l'objet **history** dans notre **Vue Home** et voyons ce qu'il montre :

![Image](https://cdn-media-1.freecodecamp.org/images/TlxBJpus9XCfVoTXpuwlYpMIJdSuDQ6AlzuA)
_**console.log(history) à l'intérieur de la Vue Home**_

D'accord, exactement ce à quoi nous nous attendions.

Il nous dit que nous sommes arrivés ici avec une action **PUSH**, que la **longueur** de l'objet est **40** (à mesure que vous naviguez dans votre application, **history** grandit jusqu'à **50** et s'arrête là, en supprimant les entrées plus anciennes et en gardant sa taille chaque fois que l'application pousse une autre entrée d'historique dans l'objet).

Il nous donne les informations sur **location**.

Encore une fois, l'objet **history** est **mutable**. Par conséquent, il est recommandé d'accéder à **location** à partir des props de **render** de **Route**, et non à partir de **history.location**.

Cela garantit que vos hypothèses sur React sont correctes dans les hooks de cycle de vie.

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/11tFGOkM-0hm2n6rF3Mn3bxqFCC87kJeXkUU)
_**exemple d'utilisation de location, correct et incorrect**_

Typiquement, vous pouvez l'utiliser pour changer le chemin de l'URL du navigateur.

Dans l'exemple ci-dessous, nous évitons **<Link>** et créons un bouton qui fait un history push :

![Image](https://cdn-media-1.freecodecamp.org/images/U6XKE1UjV-vBx5xUen3qRdxP-iO-olkPAmN3)
_**exemple d'utilisation de history.push**_

Bien sûr, vous pouvez l'utiliser pour déclencher le changement d'URL après une certaine récupération de données ou des effets secondaires.

C'est confortable de l'utiliser au milieu de JSX où vous ne voulez pas invoquer de composants. Vous pouvez simplement **retourner** un **history push** et déclencher **Router** pour **mettre à jour** l'URL du navigateur.

### Dernier mais non des moindres

Je pense qu'à ce stade, vous avez déjà une bonne idée de la façon d'utiliser **match**, **location** et **history**.

Je n'ai apporté aucune modification à notre modèle initial, alors n'hésitez pas à jouer avec dans le même [dépôt](https://github.com/evedes/React-Boilerplate-01) fourni dans la [Partie 1](https://medium.freecodecamp.org/hitchhikers-guide-to-react-router-v4-a957c6a5aa18) de ce guide.

#### **05. Bibliographie**

Pour écrire cet article, j'ai utilisé la documentation de React Router que vous pouvez trouver [ici](https://reacttraining.com/react-router/core/guides/philosophy).

Tous les autres sites que j'ai utilisés sont liés tout au long du document pour ajouter des informations ou fournir un contexte à ce que j'ai essayé de vous expliquer.

Cet article est la partie 2 d'une série intitulée "Guide du voyageur à React Router v4"

* [Partie I : Comprendre React Router en 20 minutes](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)
* [Partie III : chemins récursifs, à l'infini et au-delà !](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8/)
* Partie IV : [configuration de route, la valeur cachée de la définition d'un tableau de configuration de route](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399/)

? Merci beaucoup !