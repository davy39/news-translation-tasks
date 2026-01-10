---
title: Une introduction à la programmation visuelle basée sur les automates dans Rosmaro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T13:53:42.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-visual-automata-based-programming-in-rosmaro-100dae8eb969
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wYiiltn59DLXuTckakv8rg.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction à la programmation visuelle basée sur les automates dans
  Rosmaro
seo_desc: 'By Łukasz Makuch

  To do automata-based programming is to program with states and transitions. States
  correspond to different behaviors. Transitions are named after events and describe
  how those behaviors change.

  The easiest way to think about this is ...'
---

Par 1ukasz Makuch

Faire de la programmation basée sur les automates, c'est programmer avec des états et des transitions. Les états correspondent à différents comportements. Les transitions sont nommées d'après des événements et décrivent comment ces comportements changent.

La manière la plus simple de penser à cela est un graphe orienté. Voici un exemple d'un prince maudit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cxViPSuy4F9OJtQXcRAd0Q.png)
_Un graphe orienté très simple_

Il peut être soit un _Prince_ soit une _Grenouille_. Le _Prince_ mangeant une pizza est un événement qui provoque une transition de l'état _Prince_ à l'état _Grenouille_.

Je vais vous montrer comment faire de la programmation (visuelle) basée sur les automates dans Rosmaro.

[Rosmaro](https://rosmaro.js.org) est une bibliothèque JavaScript qui vous permet de construire des objets étatiques.

Un objet est étatique lorsque deux appels de méthode identiques peuvent produire des résultats différents.

Voici un exemple :

```
> model.introduceYourself(); 'Je suis Le Prince de Rosmaro !'
```

```
> model.eat({dish: 'yakisoba'}); undefined
```

```
> model.introduceYourself(); 'Je suis Le Prince de Rosmaro !'
```

```
> model.eat({dish: 'pizza'}); undefined
```

```
> model.introduceYourself(); 'Coâ ! Coâ !'
```

Un autre excellent exemple d'objets étatiques est une Interface Utilisateur Graphique. Pensez à un distributeur automatique de billets. Vous pouvez regarder deux fois son écran et voir différents messages et champs. Vos yeux sont les mêmes. La manière dont vous regardez l'écran n'a pas changé. C'est l'état du distributeur qui a changé. Peut-être avez-vous sélectionné une option en cliquant sur un bouton, ou peut-être qu'un minuteur s'est déclenché. Quelque chose a provoqué une transition d'un état à un autre.

Ci-dessous se trouvent quelques exemples d'applications front-end construites en utilisant la programmation visuelle basée sur les automates.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wSe8QRkF9KCFWrK4l4gn6g.gif)
_Le code de [cette application To-Do](https://github.com/lukaszmakuch/bool-less-todo" rel="noopener" target="_blank" title=") ne contient aucune valeur booléenne._

![Image](https://cdn-media-1.freecodecamp.org/images/1*73H1rmEcexjfg3o-BB2SRA.gif)
_[Cet assistant](https://github.com/lukaszmakuch/Rosmaro-React-example-Bunny-App" rel="noopener" target="_blank" title=") a deux chemins. Il n'y a pas de IF pour cela._

La manière Rosmaro de construire des objets étatiques est de **combiner un graphe dessiné avec du code écrit**.

Le graphe montre tous les comportements possibles et ce qui les fait changer. Le fait qu'il soit dessiné à l'aide d'un éditeur visuel en fait un outil de programmation visuelle.

Chaque comportement est exprimé comme un ensemble de fonctions pures. Une fonction peut retourner un résultat ainsi qu'une demande de suivre une flèche.

Rosmaro stocke l'ensemble de l'état d'un modèle dans un mécanisme de stockage pluggable. Il peut s'agir de tout, d'un simple objet JavaScript à une base de données NoSQL. Il utilise également un verrouillage pessimiste pour éviter de passer à un état incohérent.

L'exemple que je veux vous montrer concerne un prince qui se transforme en grenouille lorsqu'il mange une pizza.

Tout d'abord, ouvrez l'[éditeur Rosmaro](https://rosmaro.js.org/editor/). Ensuite, cliquez sur le bouton _LOAD_ pour démarrer un nouveau projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UKxKP4zIYv0UaMXt0C2S4Q.png)

Ajoutez le graphe principal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ahW-cir31VYEJ9cejGyUsg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C2aMW6A9Z7rxwLll0nE8Hw.png)

Cliquez sur _NEW NODE_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kMlmPurzTdi02OryTx1rGg.png)

Ajoutez un nœud local appelé _Prince_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wcyKGVD0HjXTHp2gJ6e7xQ.png)

Ensuite, ajoutez un nœud local appelé _Frog_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*riJxknEZaHyt2bblanzuoQ.png)

Placez votre curseur de souris sur le point d'entrée _start_ et dessinez une flèche vers le nœud _Prince_. Ensuite, dessinez une flèche du _Prince_ vers la _Grenouille_ et appelez-la _ate pizza_. Enfin, cliquez sur _ADD NODE_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ny2w0wNxp8I4wQ3uKMLpkw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GuMz85fYAj4N6KZtinbYSA.png)

Ajoutez une feuille appelée _Prince_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NfV-0-geNWNNok4n6GyRRw.png)

Ensuite, ajoutez une feuille appelée _Frog_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GaWnKZe4G6ezzQGCHzsVjQ.png)

Pour compléter le graphe principal, associez les nœuds locaux avec les feuilles récemment ajoutées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6nIgD-hbb8wS8hbF6S8OJA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CR5ZvCLP8GsC4VLgN8sylA.png)

Le graphe est prêt. Cliquez sur le bouton appelé _GENERATE CODE_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*atgBQ9GnIjRBfNyc6CM_5w.png)

Il est temps d'écrire un peu de JavaScript. Tout d'abord, vous devez obtenir toutes les dépendances.

```
npm i rosmaro rosmaro-in-memory-storage rosmaro-process-wide-lock --save
```

Ensuite, vous devez les importer et les appeler.

Le graphe généré peut être soit importé en tant que fichier JSON, soit collé directement dans le code. Pour garder cet exemple aussi simple que possible, je suggère de le coller dans le code.

Une grenouille est certainement une créature plus simple qu'un prince. Implémenter son comportement est facile. Chaque fois que nous demandons à la grenouille de se présenter, elle dit « Coâ ! Coâ ! »

Le prince ne se présente pas seulement, mais fait également attention aux choses qu'il mange. Il peut manger un yakisoba et tout va bien. Mais dès qu'il mange une pizza, il suit la flèche appelée _ate pizza_.

Il est temps de mettre tous les gestionnaires ensemble.

Le modèle est prêt. Voici le code complet :

Des appels identiques à la méthode _introduceYourself_ retournent des valeurs différentes. La valeur retournée dépend des événements qui se sont produits dans le passé. Cela prouve que l'objet _model_ est étatique.

Le [code du Prince Maudit](https://github.com/lukaszmakuch/cursed-prince) est sur GitHub. Il n'utilise que les fonctionnalités de base de Rosmaro. Lorsque vous travaillez sur des applications réelles, vous voudrez utiliser des techniques plus avancées. Certaines d'entre elles incluent des sous-graphes, des régions orthogonales dynamiques et l'objet contexte.

Vous pouvez en apprendre plus sur Rosmaro à partir de sa [documentation officielle](https://rosmaro.js.org/doc/).