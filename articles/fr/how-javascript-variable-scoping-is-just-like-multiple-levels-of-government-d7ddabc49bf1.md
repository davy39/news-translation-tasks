---
title: Comment la portée des variables JavaScript est similaire à plusieurs niveaux
  de gouvernement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-22T11:51:42.000Z'
originalURL: https://freecodecamp.org/news/how-javascript-variable-scoping-is-just-like-multiple-levels-of-government-d7ddabc49bf1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oTySOUhld2PJyrp83Pblog.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment la portée des variables JavaScript est similaire à plusieurs niveaux
  de gouvernement
seo_desc: 'By Kevin Kononenko

  Have you ever smashed your keyboard in frustration after getting an undefined value
  over and over again while trying to find the value of a variable?

  Or, have you named two variables the same thing after hours and hours of coding,
  ...'
---

Par Kevin Kononenko

Avez-vous déjà frappé votre clavier de frustration après avoir obtenu une valeur **undefined** encore et encore en essayant de trouver la valeur d'une variable ?

Ou bien, avez-vous nommé deux variables de la même manière après des heures et des heures de codage, pour découvrir votre erreur plus tard ?

Ces deux problèmes peuvent être liés à la portée de votre variable. **La portée** définit où vos variables seront accessibles dans votre script.

Lorsque vous définissez correctement la portée de vos variables, vous constaterez que votre code est plus facile à lire et à déboguer pour tout lecteur.

#### Le problème

Avant la mise à jour ES6 de JavaScript, vous ne pouviez déclarer des variables qu'avec **var**_._ Puisque **var** ne limite pas la portée de la variable, vous deviez deviner si la variable avait une portée globale ou locale.

Maintenant, JavaScript vous permet de déclarer des variables avec **const** et **let**_._ Ils peuvent ajouter une certaine complexité, mais ils rendent votre code beaucoup plus facile à comprendre.

Malheureusement, la plupart des tutoriels décrivent ces portées comme des boîtes dans des boîtes ou du verre sans tain. Je ne sais pas pour vous, mais je ne passe pas beaucoup de temps à emballer des boîtes dans des boîtes ou à regarder à travers des couches de verre sans tain !

Je pense avoir une meilleure façon. La portée peut être expliquée en regardant comment les lois internationales, les lois nationales et les lois locales fonctionnent ensemble. Vous n'avez donc besoin de comprendre que différents niveaux de gouvernement existent pour apprendre les différents niveaux de portée. Voici un rapide aperçu, puis nous entrerons dans le vif du sujet !

![Image](https://cdn-media-1.freecodecamp.org/images/1*YWPubaj-_gMWS4jEDVBUfA.png)
_Les lois sur l'alcool sont ennuyeuses mais espérons qu'elles ne sont pas trop controversées_

Je vais essayer d'éviter toute loi liée aux questions politiques actuelles.

### Portée globale (Nations Unies)

Les variables définies au niveau supérieur de votre script sont à portée globale. Elles sont disponibles pour toutes les fonctions. Ce sont des variables **globales**.

Celles-ci sont similaires aux lois internationales. Gardez à l'esprit qu'il est assez difficile de faire passer des lois que les 193 membres des Nations Unies accepteront. Ces lois ne devraient donc couvrir que les droits humains les plus fondamentaux. Les Nations Unies ne s'impliquent pas dans la politique des drogues ou les lois religieuses qui pourraient concerner des pays individuels. Deux exemples pourraient être :

« La torture est interdite. »

« Les armes chimiques sont interdites. »

Cela signifie que ces lois seront valables pour tout pays faisant partie des Nations Unies, ainsi que pour tout État ou province au sein de ces pays.

Voici la version pré-ES6 de ces lois.

En ES6, nous pouvons maintenant déclarer des variables avec **const** et **let**. **Const** rendra la valeur de la variable immuable — elle ne pourra pas être changée. **Let** ne le fera pas. Je pense que ces deux droits humains fondamentaux devraient définitivement être immuables ! Donc, cela devrait être :

Vous ne voulez pas créer trop de variables globales. « Polluer » la portée globale signifie que vous définissez trop de variables qui sont accessibles globalement. D'un point de vue programmation, vous rendez le débogage et la maintenance du code difficiles lorsque vous utilisez des variables globales.

Dans cette analogie, il n'y a pas de lois internationales sur l'âge auquel les individus sont autorisés à boire de l'alcool. Chaque pays doit définir ces règles. L'ONU ne pourrait jamais exister si elle essayait de réguler les âges de consommation d'alcool !

![Image](https://cdn-media-1.freecodecamp.org/images/1*kLUNLgITy56QwvIw60qbsQ.png)

### Portée de fonction (États-Unis)

Puisque les lois ci-dessus sont définies globalement, elles sont accessibles n'importe où dans notre script. Et, puisque elles sont définies avec **const**_,_ elles sont immuables.

Alors, qu'en est-il des lois qui ne s'appliquent qu'aux États-Unis ? Un exemple est l'âge légal pour boire, l'ennemi des étudiants universitaires partout. Vous devez avoir 21 ans pour acheter de l'alcool aux États-Unis.

Cet âge devrait-il être immuable ou inchangable ? Non. En fait, il n'y avait [aucune loi universelle sur l'âge légal pour boire aux États-Unis jusqu'en 1984](https://en.wikipedia.org/wiki/Legal_drinking_age). Cela pourrait changer à nouveau dans le futur.

Nous utiliserons **let** pour définir celle-ci.

Si nous essayons d'accéder à la valeur de **drinkingAge** en dehors de la fonction **unitedStates**, nous obtiendrons une erreur puisque elle n'existe qu'à l'intérieur de la **portée de fonction**.

Rappelez-vous simplement — les lois de l'ONU sont toujours valables aux États-Unis.

Les accolades sont comme les frontières du pays, dans ce cas. Les lois ne sont valables qu'à l'intérieur des frontières de ce pays. Donc, si vous vouliez créer une fonction **mexico**, vous pourriez définir drinkingAge **à nouveau** comme 18.

Voici ce code sous forme de diagramme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eFFaFaZ7Es521Wi6DP5Xbg.png)

### Portée de bloc (Massachusetts)

Je vis dans le Massachusetts, donc j'ai décidé de prendre mon propre État pour cet exemple. Il y a un autre niveau de portée : la **portée de bloc**. La portée de bloc et la portée de fonction sont toutes deux des exemples de **portée locale**, car elles créent des limites locales pour la définition des variables.

La portée de bloc signifie qu'une variable peut être locale à un ensemble d'accolades {}, comme une instruction **if** ou une boucle **for**. Tout comme la portée de fonction, la variable n'est valable qu'à l'intérieur de ces accolades.

Dans le Massachusetts, tous les bars doivent arrêter de servir à 2h du matin. Je sais, je sais — si vous vivez en Europe, cela semble probablement scandaleux. Cette loi varie en fait selon les États. À New York, ils peuvent servir jusqu'à 4h du matin.

En tout cas, pour que cela fonctionne dans le code, nous devons définir des instructions if à l'intérieur de la fonction unitedStates. Nous définirons à nouveau la variable avec **let**, car ces lois peuvent certainement changer.

La variable **closingTime** n'est valable qu'à l'intérieur du bloc **if**, tandis que drinkingAge est valable n'importe où dans la fonction unitedStates.

Si nous voulons définir une heure de fermeture séparée pour New York, nous pouvons également le faire grâce à la **portée de bloc**.

Si vous vouliez prendre une mesure basée sur la variable closingTime, vous pourriez maintenant faire quelque chose à l'intérieur de chaque bloc if.

Voici un diagramme qui couvre tout cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cdQas_85deas-TeAm241aQ.png)

### Modifier une variable (adopter une nouvelle loi)

Dernière partie. Supposons que vous souhaitiez adopter une loi pour changer l'âge légal de consommation d'alcool aux États-Unis. Vous devez créer une fonction qui pourra modifier la variable drinkingAge. Appelons-la **passDrinkingLaw**.

Vous devrez créer la fonction passDrinkingLaw à l'intérieur de la fonction unitedStates, car elle n'est pertinente que pour les États-Unis. Il n'y a pas de lois globales sur la consommation d'alcool.

Elle devra également accéder à la variable drinkingAge, qui définit l'âge original. Imaginez que vous souhaitiez changer l'âge légal de consommation d'alcool à 18 ans. Voici comment vous feriez cela.

C'est pourquoi il est important de définir la variable dans toute la portée de unitedStates. Vous voudriez que les changements prennent effet pour toute utilisation future de drinkingAge. Et, si vous vouliez créer une fonction passDrinkingLaw universelle, elle ne fonctionnerait pas avec cette structure.

drinkingAge est **locale** à la fonction unitedStates. Voici une version diagramme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pepSwOaIwHrf2iqJsG4TUA.png)

#### Appel à l'action

Avez-vous aimé cela ? Applaudissez pour que d'autres puissent le découvrir également. Et, si vous voulez être informé lorsque je publierai de futurs tutoriels utilisant des analogies, inscrivez-vous ici :