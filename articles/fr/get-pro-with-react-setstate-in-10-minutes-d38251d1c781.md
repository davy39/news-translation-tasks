---
title: Comment devenir un pro avec React setState() en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-06T19:47:37.000Z'
originalURL: https://freecodecamp.org/news/get-pro-with-react-setstate-in-10-minutes-d38251d1c781
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_agRQIzQvukx6TC7
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
seo_title: Comment devenir un pro avec React setState() en 10 minutes
seo_desc: 'By Eduardo Vedes

  This article is aimed at people who have already had their first approach to React,
  and who, as beginners, have doubts about how setState works and how to use it correctly.
  It should also help mid to senior devs use cleaner and more ...'
---

Par Eduardo Vedes

Cet article s'adresse aux personnes qui ont déjà eu leur premier contact avec React, et qui, en tant que débutants, ont des doutes sur le fonctionnement de `setState` et comment l'utiliser correctement. Il devrait également aider les développeurs de niveau intermédiaire à senior à utiliser des méthodes plus propres et plus abstraites pour définir l'état, et à faire en sorte que les fonctions d'ordre supérieur gèrent et abstraient l'état.

Lisez et amusez-vous !

Alors, prenez une tasse de café et continuez à lire ! ?

### Concepts de base de setState()

Les composants React vous permettent de diviser l'interface utilisateur (UI) en morceaux indépendants et réutilisables, afin que vous puissiez penser à chaque morceau de manière isolée.

Conceptuellement, les composants sont comme des fonctions JavaScript. Ils acceptent des entrées arbitraires (appelées « props ») et retournent des éléments React décrivant ce qui devrait apparaître à l'écran.

Si vous devez donner à l'utilisateur la possibilité d'entrer quelque chose ou de modifier les variables que le composant reçoit en tant que props, vous aurez besoin de `setState`.

Que vous déclariez un composant comme une fonction ou une classe, il ne doit jamais modifier ses propres props.

Tous les composants React doivent se comporter comme des fonctions pures par rapport à leurs props. Cela signifie des fonctions qui n'essaient jamais de changer leurs entrées et qui retournent toujours le même résultat pour les mêmes entrées.

Bien sûr, les interfaces utilisateur des applications sont dynamiques et changent avec le temps. C'est pourquoi l'`état` a été créé.

L'`état` permet aux composants React de changer leur sortie au fil du temps en réponse aux actions de l'utilisateur, aux réponses du réseau, et à tout autre événement, sans violer cette règle.

Les composants définis comme des classes ont quelques fonctionnalités supplémentaires. L'état local est une fonctionnalité disponible uniquement pour les composants de classe.

`setState` est la méthode de l'API fournie avec la bibliothèque afin que l'utilisateur puisse définir et manipuler l'état au fil du temps.

### **Trois règles d'or lors de l'utilisation de setState()**

#### **Ne modifiez pas l'état directement**

![Image](https://cdn-media-1.freecodecamp.org/images/fDk0J1KHkNJKyjha9jV2Ic5VtMHtx0hX54-5)
_manières incorrectes et correctes de définir l'état_

#### **Les mises à jour de l'état peuvent être asynchrones**

React peut regrouper plusieurs appels `setState()` en une seule mise à jour pour des raisons de performance.

Parce que `**this.props**` et `this.state` peuvent être mis à jour de manière asynchrone, vous ne devez pas vous fier à leurs valeurs pour calculer l'état suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/U802XeMCbWXgWEqgFS1oISKMBIalMacJHIr9)
_manipuler l'état avec une approche fonctionnelle_

Vous devez toujours effectuer ce type de manipulation avec une approche fonctionnelle, en fournissant l'`état` et les `props` et en retournant le nouvel `état` basé sur l'ancien.

#### **Les mises à jour de l'état sont fusionnées**

Lorsque vous appelez `setState()`, React fusionne l'objet que vous fournissez dans l'`état` actuel.

Dans l'exemple ci-dessous, nous mettons à jour la variable `dogNeedsVaccination` indépendamment des autres variables d'`état`.

La fusion est superficielle, donc `this.setState({ dogNeedsVaccination: true })` laisse les autres variables intactes, ne remplaçant que la valeur de `dogNeedsVaccination`.

![Image](https://cdn-media-1.freecodecamp.org/images/MkFjwenYGJsPRkbOZJOcSSHaU26jJ83Y430C)

### **Respectez le flux de données et évitez l'état au maximum**

**Les données circulent vers le bas !** Ni les composants parents ni les composants enfants ne peuvent savoir si un certain composant est avec état ou sans état, et ils ne devraient pas se soucier de savoir s'il est défini comme une fonction ou une classe.

C'est pourquoi l'`état` est souvent appelé local ou encapsulé. Il n'est pas accessible à aucun autre composant que celui qui le possède et le définit.

Lorsque vous définissez une prop avec `setState` et que vous l'utilisez dans votre composant, vous brisez le flux de rendu des props. Si, pour une raison quelconque, la prop passée à votre composant a changé dans le composant parent, l'enfant ne se re-rendra pas automatiquement ?!

Vérifions un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/BdJA87j3HTnLGzQMnx0enaMdNXelqTzrkgZ1)

Ici, vous avez un composant `Home` qui génère un nombre magique toutes les 1000 ms et le définit dans son propre `état`.

Ensuite, il affiche le nombre et invoque trois composants `Child` (frères et sœurs) qui recevront le nombre magique dans le but de l'afficher en utilisant trois approches différentes :

#### Première approche

Le composant `ChildOfHome` respecte le flux de cascade des props de React et, considérant que l'objectif est uniquement d'afficher le nombre magique, il affiche les `props` reçues directement.

![Image](https://cdn-media-1.freecodecamp.org/images/DdFAz1VvRhbZ1vgJgoKYoguzuPEWRDsFkI-L)

#### Deuxième approche

Le composant `ChildOfHomeBrother` reçoit les `props` de son parent et, en invoquant `componentDidMount`, définit le nombre magique dans l'`état`. Ensuite, il affiche `state.magicNumber`.

Cet exemple ne fonctionne pas car `render()` ne sait pas qu'une `prop` a changé, donc il ne déclenche pas le re-rendu du composant. Comme le composant n'est plus re-rendu, `componentDidMount` n'est pas invoqué et l'affichage n'est pas mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/gPNGY21whSekaZpxB2qWutfofEw96BwgAs6X)

#### Troisième approche

Habituellement, lorsque nous essayons de faire fonctionner cela en utilisant la deuxième approche, nous pensons qu'il manque quelque chose. Au lieu de faire un pas en arrière, nous continuons à ajouter du code pour le faire fonctionner !

Donc, dans cette troisième approche, nous avons ajouté `componentDidUpdate` pour vérifier s'il y a un changement dans les `props` afin de déclencher le re-rendu du composant. Cela est inutile et conduit à un code peu propre. Cela entraîne également des coûts de performance qui seront multipliés par le nombre de fois où nous faisons cela dans une grande application où nous avons beaucoup de composants enchaînés et des effets secondaires.

Cela est incorrect sauf si vous devez permettre à l'utilisateur de changer la valeur de la prop reçue.

Si vous n'avez pas besoin de changer la valeur de la prop, essayez toujours de garder les choses fonctionnant selon le flux React (Première approche).

Vous pouvez vérifier une page web fonctionnelle avec cet exemple que j'ai préparé pour vous sur [Glitch](https://freezing-transport.glitch.me/). Jetez un coup d'œil et amusez-vous ?

Consultez également le code dans `**Home.js**` et `**HomeCodeCleaned.js**` (sans le code HTML) dans [mon dépôt](https://github.com/evedes/set-state-in-10-min) à propos de cet article.

### Comment utiliser setState

À ce stade, je pense qu'il est temps de mettre les mains dans le cambouis !

Jouons un peu avec `setState` et améliorons cela ! Suivez simplement et prenez une autre tasse de café !

Créons un petit formulaire pour mettre à jour les données de l'utilisateur :

![Image](https://cdn-media-1.freecodecamp.org/images/7QEN8rHC9lVLP1YX2nyTVEcC7s7G-25dDkjG)
_Petit exercice sur setState()_

Voici le code pour l'exemple ci-dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/YVqIxzftG-aQyjVeMvPwb5IPbpe7Xlq-C7ln)
_Composant Home initial_

Nous définissons l'`état` comme un objet, et il n'y a pas de problème car notre état actuel ne dépend pas de notre état précédent.

Et si nous créons un autre champ de formulaire pour introduire et afficher le nom de famille ?

![Image](https://cdn-media-1.freecodecamp.org/images/FaqdEOSaxiOvUvHwrdTjTI4DVr9icW3-40Dt)
_Fonctionnalité de nom de famille_

![Image](https://cdn-media-1.freecodecamp.org/images/Jut4MxFFK81esqawr6NkqHWMsn4fNVWWfbzl)
_handleFormChange abstrait_

Bien ! Nous avons abstrait la méthode `handleFormChange` pour pouvoir gérer tous les champs de saisie et `setState`.

Et si nous ajoutons un bouton bascule pour marquer les données comme valides ou invalides et un compteur pour savoir combien de changements nous avons apportés à l'état ?

![Image](https://cdn-media-1.freecodecamp.org/images/T52heLJjKgK8ziG6CcEuxjYDhc91qjdOxP1h)
_Capture d'écran montrant le console.log de l'état du composant_

![Image](https://cdn-media-1.freecodecamp.org/images/iu0Fdle1B1iFim6GZIKf8O6z3fgjHDn4h7qe)
_handleFormChange mis à jour avec les gestionnaires de case à cocher et de compteur_

Oui ! Nous assurons ! Nous avons abstrait beaucoup de choses !

Hmmm... Disons que je ne veux pas une case à cocher pour contrôler la variable `isValid` mais un simple bouton bascule.

Séparons également le gestionnaire de compteur de cette méthode. Cela fonctionne bien, mais dans des situations plus complexes où React doit regrouper/modifier les changements, ce n'est pas une bonne politique de se fier à la variable `this.state.counter` pour en ajouter un de plus. Cette valeur peut changer sans que vous en soyez conscient.

Nous utilisons une copie superficielle de celle-ci au moment où l'opération est invoquée, et à ce moment précis, vous ne savez pas si sa valeur est celle que vous attendiez ou non !

Faisons un peu fonctionnel !

![Image](https://cdn-media-1.freecodecamp.org/images/0p8DlnnaNpXtqPG81xTayly9J8VE2ibidKwK)
_Capture d'écran montrant le basculement Valide/Invalide et le console.log de la variable state.counter_

![Image](https://cdn-media-1.freecodecamp.org/images/C5veVluHRXO39bXkvVKgHCWuH6japAFj3D3R)
_séparation des gestionnaires de contrôle_

D'accord — Nous avons perdu l'abstraction car nous avons séparé les gestionnaires, mais c'est pour une bonne raison !

À ce stade, nous conservons `handleFormChange` passant un objet à la méthode de l'API `setState`. Mais les méthodes `handleCounter` et `handleIsValid` sont maintenant fonctionnelles et commencent par récupérer l'état actuel puis, en fonction de cet état, le changent pour le suivant.

C'est la bonne façon de changer l'`état` des variables qui dépendent de l'état précédent.

Et si nous voulons `console.log()` les changements d'état des formulaires de saisie `firstName` et `lastName` chaque fois qu'un changement se produit ? Essayons !

![Image](https://cdn-media-1.freecodecamp.org/images/HUCXO8J0ASy4NNfDU1zZuEtXq-zpdiIQe1ZK)
_méthode logFields()_

Bien ! Chaque fois que `handleFormChange` se produit (ce qui signifie qu'une nouvelle touche a été pressée), la méthode `logFields()` est invoquée et enregistre l'état actuel dans la console !

Vérifions la console du navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/jLz33AfgQi6kldAGYf4KT479Zr2ntt3-RBUk)
_capture d'écran du console.log de l'état de firstName et lastName_

Attendez ! Qu'est-ce qui s'est passé ici les gars ? Le journal de la console est un changement avant la saisie actuelle du formulaire ! Pourquoi cela se produit-il ?

#### **setState est asynchrone !!**

Nous le savions déjà, mais maintenant nous le voyons de nos propres yeux ! Que se passe-t-il là ? Jetons un coup d'œil aux méthodes `handleFormChange` et `logFields` ci-dessus.

La méthode `handleFormChange` reçoit le nom et la valeur de l'événement, puis effectue un `setState` de ces données. Ensuite, elle appelle `handleCounter` pour mettre à jour les informations du compteur, et enfin invoque la méthode `logFields`. La méthode `logFields` récupère le `currentState` et retourne 'Eduard' au lieu de 'Eduardo'.

Le problème est que `setState` est asynchrone et n'agit pas sur le moment. React fait son travail et exécute la méthode `logFields` en premier, laissant `setState` pour la prochaine boucle d'événements.

Mais comment pouvons-nous éviter ce genre de situation ?

Eh bien, l'API `setState` a un `callback` pour éviter cette situation :

![Image](https://cdn-media-1.freecodecamp.org/images/3wyO2ef7SMFdzVrxDGpTwJkXvdEV7wCZLGh2)
_méthode de l'API setState_

Si nous voulons que `logFields()` prenne en compte les changements récents que nous avons apportés à l'état, nous devons l'invoquer à l'intérieur du callback, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/GPYFMLHBhIOkbjGGdfcDm5Uz24og0hvPYtvC)
_utilisation du gestionnaire de callback de la méthode de l'API setState()_

D'accord, maintenant cela fonctionne !

Nous disons à React : « Hé React ! Fais attention, quand tu invoques la méthode `logFields`, je veux que tu aies déjà mis à jour l'`état`, d'accord ? Je te fais confiance ! »

React dit : « D'accord Edo ! Je vais gérer tout ce lot de choses que je fais habituellement dans l'arrière-cour avec le truc `setState` et seulement quand j'aurai fini avec cela, j'invoquerai `logFields()` ! Cool mec ! Détends-toi ! »

![Image](https://cdn-media-1.freecodecamp.org/images/2YuGDOcmnseFY5lMTceR9FBGZ8h4friD-gnT)
_capture d'écran du console.log() de fullName_

Et en fait — cela a fonctionné !

D'accord tout le monde ! À ce stade, nous avons géré les principaux pièges de `setState`.

Avez-vous le courage d'aller au-delà du mur ? Prenez une tasse de café et devenons vraiment cool...

### Devenir élégant avec setState()

Maintenant que nous avons les méthodes `handleCounter` et `handleIsValid`, et que `setState()` est exprimé avec des fonctions, nous pouvons composer la mise à jour de l'état avec d'autres fonctions ! **J'aime la composition ! Amusons-nous !**

![Image](https://cdn-media-1.freecodecamp.org/images/pBcn25XBdxdA9uqPSqRXDRbRu6fdMB5MdS-4)
_abstraction de handleIsValid_

Nous pouvons prendre la logique à l'intérieur de `setState` pour une fonction en dehors du composant de classe. Appelons-la `toggleIsValid`. ☝️

![Image](https://cdn-media-1.freecodecamp.org/images/MQkXig9EC7Fem4-xeipehkq1KUJweQE027QD)
_Fonction toggleIsValid_

Maintenant, cette fonction peut vivre en dehors du composant de classe, n'importe où dans votre application.

Et si nous utilisons une fonction d'ordre supérieur ?

![Image](https://cdn-media-1.freecodecamp.org/images/AfGwofoy8ykA4pYHHr9cRiMSeUN9oEgH-yca)
_changement de toggleIsValid par une fonction d'ordre supérieur_

Waouh ! Maintenant, nous n'invoquons plus la fonction `toggleIsValid`. Nous invoquons une fonction d'ordre supérieur abstraite appelée `toggleKey` et nous lui passons une clé (une chaîne dans ce cas).

Comment devons-nous changer la fonction `toggleIsValid` maintenant ?

![Image](https://cdn-media-1.freecodecamp.org/images/YJ1jrcCACrvShq5Je8fZYWrxSfEOdlZYWiDo)
_fonction d'ordre supérieur toggleKey_

Quoi ?! Maintenant, nous avons une fonction appelée `toggleKey` qui reçoit une `clé` et retourne une nouvelle fonction qui change l'état selon la clé fournie.

Cette `toggleKey` peut être dans une bibliothèque ou dans un fichier d'aide. Elle peut être invoquée dans de nombreux contextes différents pour changer l'état de ce que vous voulez à son opposé.

Génial !

Faisons de même avec le gestionnaire de compteur d'incrémentation :

![Image](https://cdn-media-1.freecodecamp.org/images/nkgBbIQTNdFGZfTDtZkigh1HDMCWZBnnNii9)
_abstraction de handleCounter pour invoquer une fonction d'ordre supérieur_

![Image](https://cdn-media-1.freecodecamp.org/images/oxRMcY3Kwj72HrWrE5IpNTDhlcb4mnaw8s44)
_fonction d'ordre supérieur incrementCounter_

Oui ! Cela fonctionne ! C'est bien. Devenons fous maintenant...

### Viser la lune et revenir

Et si nous créons une fonction générique `makeUpdater` qui reçoit la fonction de transformation que vous souhaitez appliquer, prend la clé, et retourne la fonction d'état gérant l'état avec la fonction de transformation et la clé ? Un peu confus ? Allons-y !

![Image](https://cdn-media-1.freecodecamp.org/images/mKBYvEDHZDt1hhK-67J-yc7G9ciZd6ONeU37)
_fonction d'ordre supérieur makeUpdater_

D'accord, c'est assez... Arrêtons-nous ici. ?

Vous pouvez vérifier tout le code que nous avons fait dans ce [dépôt GitHub](https://github.com/evedes/variations-in-set-state).

### Dernier point mais non des moindres

N'oubliez pas d'éviter l'état maximum en utilisant l'état et respectez le flux de rendu des props de React.

N'oubliez pas que `setState` est asynchrone.

N'oubliez pas que `setState` peut prendre un objet ou une fonction.

N'oubliez pas que vous devez passer une fonction lorsque votre état suivant dépend de votre état précédent.

### **Bibliographie**

1. Documentation React
2. [Cours techniques Reach par Ryan Florence](https://reach.tech/courses), que je recommande vraiment.

Merci beaucoup !