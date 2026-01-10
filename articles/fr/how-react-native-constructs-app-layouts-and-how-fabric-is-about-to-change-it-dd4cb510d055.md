---
title: Comment React Native construit les mises en page des applications (et comment
  Fabric est sur le point de tout changer)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-17T17:38:30.000Z'
originalURL: https://freecodecamp.org/news/how-react-native-constructs-app-layouts-and-how-fabric-is-about-to-change-it-dd4cb510d055
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ujoyIWzko6WTIW8HhpIBwA.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment React Native construit les mises en page des applications (et comment
  Fabric est sur le point de tout changer)
seo_desc: 'By Mehul Mohan

  The React Native team has been working on something which is fundamentally going
  to change how the internals of React Native communication work with the host Operating
  System. It is nicely codenamed “project fabric” (until there’s an o...'
---

Par Mehul Mohan

L'équipe React Native travaille sur quelque chose qui va fondamentalement changer la manière dont les communications internes de React Native fonctionnent avec le système d'exploitation hôte. Cela est joliment nommé « projet fabric » (jusqu'à ce qu'un nom officiel soit publié).

Discutons de ce que c'est réellement et des changements qu'il apporte aux développeurs.

### Comment React Native fonctionne actuellement

Si nous regardons, React Native utilise actuellement 3 threads :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fKuJS2I7kvpcyII3x0Mxww.jpeg)

1. Thread UI — C'est le thread principal de l'application sur lequel votre application Android/iOS s'exécute. Il a accès à l'UI et votre UI ne peut être modifiée que par ce thread.
2. Thread Shadow — Ce thread est le thread en arrière-plan utilisé par React Native pour calculer votre mise en page créée à l'aide de la bibliothèque React.
3. Thread JavaScript — Ce thread est l'endroit où votre code JavaScript (votre code React, essentiellement) vit et s'exécute.

#### Le fonctionnement interne...

Commençons par le début. Supposons que vous souhaitez dessiner une boîte rouge au centre de votre écran. Ce qui se passe, c'est que votre thread JS contient du code pour créer une mise en page, c'est-à-dire cette boîte rouge à l'écran. Voici un extrait de code typique qui pourrait réaliser cela pour React Native (RN) :

```jsx
<View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
<View style={{width: 100, height: 100, backgroundColor: "red"}}></View>
</View>
```

Le système d'exploitation hôte a sa propre implémentation de mise en page et ne suit pas le type de code flexbox que vous venez d'écrire. Par conséquent, RN doit d'abord convertir votre mise en page codée en flexbox en un système de mise en page que votre système d'exploitation hôte peut comprendre.

Attendez ! Avant de faire cela, nous devons déporter cette partie de calcul de mise en page vers un autre thread afin de pouvoir continuer à exécuter notre thread JavaScript. Par conséquent, RN utilise le Shadow Thread qui construit essentiellement un arbre de votre mise en page que vous avez codée dans votre thread JS. Dans ce thread, RN utilise un moteur de mise en page appelé [Yoga](https://github.com/facebook/yoga) qui convertit la mise en page basée sur flexbox en un système de mise en page que votre hôte natif peut comprendre.

React Native utilise quelque chose appelé un pont React Native pour communiquer cette information du thread JS au thread Shadow. En résumé, cela sérialise simplement les données au format JSON et les transfère sous forme de chaîne via le pont.

À ce stade, nous sommes dans le thread Shadow. Le thread JS s'exécute et il n'y a rien de dessiné à l'écran.

Maintenant, une fois que nous avons le balisage rendu de yoga, cette information est à nouveau transférée au thread UI via le pont React Native. Encore une fois, cela effectue une sérialisation sur le thread Shadow et une désérialisation sur le thread principal. Ici, le thread principal rend alors l'UI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jsICCO6sFLBZt1Bd0VNPfQ.jpeg)

### Problèmes avec cette approche

Si vous voyez, toute la communication entre les threads se fait via un pont qui fonctionne, mais qui est rempli de limitations. Cela inclut :

* il est lent pour transférer de grandes quantités de données (par exemple, un fichier image converti en chaîne base64), et
* il y a une copie inutile de données si la même tâche peut être implémentée simplement en pointant vers les données en mémoire (encore une fois, par exemple, une image)

Ensuite, toute la communication est asynchrone, ce qui dans la plupart des cas est bien. Cependant, il n'y a actuellement aucun moyen de mettre à jour le thread UI à partir du thread JS de manière synchrone. Cela pose un problème lorsque vous utilisez, par exemple, FlatList avec une énorme liste de données. (Vous pouvez considérer FlatList comme une implémentation plus faible de RecyclerView.)

Enfin, en raison de cette nature asynchrone de la communication entre le thread JS et le thread UI, les modules natifs qui nécessitent strictement un accès synchrone aux données ne peuvent pas être utilisés pleinement. Par exemple, l'Adaptateur de RecyclerView sur Android nécessite un accès synchrone aux données qu'il rend pour éviter les scintillements à l'écran. Cela n'est pas possible actuellement en raison de l'architecture multithread mise en place par React Native.

### Présentation de Fabric

Prenez du recul et pensez à votre navigateur. Si vous regardez de plus près, les champs de saisie, les boutons, etc. sont en fait spécifiques au système d'exploitation. Par conséquent, c'est votre navigateur qui demande à votre système d'exploitation (Windows, Mac, Linux, ou presque n'importe quoi d'autre) de dessiner, par exemple, un champ de saisie quelque part sur une page web. Oh là là ! Voyez la belle correspondance entre les navigateurs et React Native.

* Thread UI → Thread UI
* Moteur de rendu du navigateur → Moteur de rendu de React Native (Yoga/Thread Shadow)
* Thread JavaScript → Thread JavaScript

Nous savons que les navigateurs modernes sont très matures et gèrent toutes ces tâches efficacement. Alors pourquoi pas React Native ? Quelle est la pièce manquante du puzzle qui restreint brutalement React Native mais pas les navigateurs ?

#### Exposition directe des appels d'API natifs à JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/1*AYVSGcao8TZW-POMIZRTeg.jpeg)

Avez-vous déjà écrit des commandes comme `document.getElementById` et des commandes comme `setTimeout` et `setInterval` dans votre console et vu le résultat ? Oh ! Leur implémentation est en fait `[native code]` ! Que signifie cela ?

Vous voyez, lorsque vous exécutez ces fonctions, elles n'appellent aucun code JavaScript. Au lieu de cela, ces fonctions sont directement liées au code natif C++ qui est appelé. Ainsi, le navigateur ne laisse pas JS communiquer avec le système d'exploitation hôte en utilisant un pont, mais expose plutôt directement JS à l'OS en utilisant du code natif ! En résumé, c'est ce que React Native Fabric ferait : éliminer le pont et permettre à l'UI d'être contrôlée directement à partir du thread JS en utilisant du code natif.

### Points clés

1. RN Fabric permet au thread UI (où l'UI est dessinée) d'être synchronisé avec le thread JS (où l'UI est programmée)
2. Fabric est encore en développement, et l'équipe React Native n'a pas mentionné de date de sortie publique pour l'instant. Mais je suis assez sûr que nous verrons quelque chose d'extraordinaire cette année.
3. Les frameworks pour le développement d'applications comme ceux-ci (RN, NativeScript, Flutter) s'améliorent de jour en jour !

_Sources des images : [https://www.slideshare.net/axemclion/react-native-fabric-review20180725](https://www.slideshare.net/axemclion/react-native-fabric-review20180725)_

### TL;DR

%[https://youtu.be/zsnSqdXqs64]

### Vous avez aimé cet article ?

Si vous avez aimé cet article, n'hésitez pas à me donner quelques applaudissements et à me suivre sur [twitter](https://twitter.com/mehulmpt). Vous savez quelle est la meilleure partie ? Les applaudissements et Twitter sont tous deux gratuits ! Si vous avez des questions, n'hésitez pas à les poser dans les commentaires !

**_Petite publicité éhontée :_** _Si vous commencez avec React Native, voici mon cours à 95 % de réduction sur comment commencer avec : [React Native — Les Premières Étapes](http://bit.ly/rn-basics-medium)_