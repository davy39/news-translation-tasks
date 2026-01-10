---
title: Une introduction à la programmation orientée tâche
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-23T14:54:33.000Z'
originalURL: https://freecodecamp.org/news/dmpl
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/mars.jpeg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: programming languages
  slug: programming-languages
- name: technology
  slug: technology
seo_title: Une introduction à la programmation orientée tâche
seo_desc: 'By Nishant Shukla

  Vehicles on Mars autonomously self-regulate, plan, and navigate using software packaged
  up in millions of lines of C. Now, if hardware limitations were not a concern, what
  language would you choose to write the logic, decision-flow,...'
---

Par Nishant Shukla

Les véhicules sur Mars s'auto-régulent, planifient et naviguent de manière autonome en utilisant des logiciels composés de [millions de lignes de C](https://softwareengineering.stackexchange.com/questions/159637/what-is-the-mars-curiosity-rovers-software-built-in/159638#159638). Maintenant, si les limitations matérielles n'étaient pas un problème, quel langage choisiriez-vous pour écrire la logique, le flux de décision et le raisonnement d'un robot extraterrestre ? 

Certains préfèrent la brièveté de Python, tandis que d'autres apprécient la robustesse de Rust, mais choisir un langage pour un projet a des conséquences profondes. [Demandez à n'importe quel linguiste](http://www.inf.ed.ac.uk/teaching/courses/inf1/fp/lectures/2012/lect01.pdf) :

<blockquote>
    "Le langage façonne notre manière de penser et détermine ce à quoi nous pouvons penser." <br/> 
    – Benjamin Lee Whorf ; pionnier de la relativité linguistique
</blockquote>

<blockquote>
    "Les limites de mon langage signifient les limites de mon monde." <br /> 
    – Ludwig Wittgenstein ; mathématicien, logicien et philosophe
</blockquote>

<blockquote>
    "Un langage qui n'affecte pas la manière dont vous pensez à la programmation ne vaut pas la peine d'être connu." <br /> 
    – Alan Perlis ; premier récipiendaire du prix Turing
</blockquote>


Il n'existe pas de solution universelle en matière de langages de programmation, il est donc utile d'élargir nos horizons en étudiant ce qui existe. 

Catégoriser les milliers de langages de programmation existants n'est pas une tâche facile, mais les tendances logicielles au fil des années ont révélé deux frameworks souverains : les langages impératifs (orientés objet) et déclaratifs (fonctionnels). 

* ==**Impératif** :== Le programmeur définit comment exécuter les algorithmes et comment accéder à la mémoire. Les exemples incluent C++, JavaScript et Python.

* ==**Déclaratif** :== Le programmeur définit la composition des fonctions et laisse le runtime optimiser les algorithmes. Les exemples incluent Haskell, Erlang et OCaml.

Une manière classique de décrire la distinction entre la programmation déclarative et impérative est que les langages déclaratifs permettent au programmeur de décrire **ce qu'**il faut faire, tandis que les langages impératifs permettent au programmeur de définir **comment** le faire. 

Si nous étendons cette idée à un troisième type de langage qui permet au programmeur de définir **pourquoi** des choix sont faits, alors nous avons découvert les langages de programmation orientés tâche. 

* ==**Orienté tâche** :== Le programmeur définit les états souhaités et laisse le runtime résoudre la composition des actions. Les exemples incluent DMPL, PDDL et DTProbLog.

La figure ci-dessous résume ces paradigmes avec des détails glorieux sur la manière dont les langages se sont influencés les uns les autres au fil des années. Les types de langages sont partout, et tout a commencé il y a moins d'un siècle ! 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-7.png)
_Les flèches entre les langages représentent l'influence. Les langages sont placés dans des colonnes correspondant à leur paradigme principal, même si certains langages sont multi-paradigmes. Pour une analyse plus robuste, voir la Figure 1. Généalogie des langages de programmation, de Farooq et al. ([https://doi.org/10.1371/journal.pone.0088941](https://doi.org/10.1371/journal.pone.0088941))_

Les langages orientés tâche apportent une nouvelle perspective à la manière dont nous pensons au code. Dans cet article, nous allons voir exactement ce que cela signifie. 

La section suivante distille ce qui rend certains langages si populaires aujourd'hui (et pourquoi la popularité n'est peut-être pas un bon indicateur pour choisir un langage plutôt qu'un autre). 

La section suivante explique la mise en œuvre d'un algorithme dans les différents paradigmes. 

Nous concluons ensuite par une discussion sur ce que chaque paradigme fait exceptionnellement bien.

## Pourquoi rester avec un langage ?

Parmi les milliers de langages de programmation existants, vous vous demandez peut-être ce qui distingue votre langage préféré d'un langage nouvellement créé. Typiquement, ce qui retient les développeurs est une combinaison des facteurs suivants :

* **APIs/frameworks** : Parfois, vous avez vraiment besoin d'utiliser une bibliothèque qui n'est pas largement disponible dans de nombreux langages. OpenCV, par exemple, est une bibliothèque de vision par ordinateur qui se marie exceptionnellement bien avec C++ ou Python, mais qui a un support limité pour certains autres langages, comme Elixir. 
* **Courbe d'apprentissage** : Certains langages prennent des années d'étude pour être maîtrisés, comme Haskell, tandis que d'autres langages comme Python vous permettent de découvrir des comportements souhaités par essai et erreur.
* **Documentation** : Les langages plus anciens, comme C, ont généralement une documentation mature grâce à des années de raffinement. Cependant, les nouveaux langages peuvent rapidement dépasser leurs spécifications originales avant d'atteindre la stabilité.
* **Communauté** : Stack Overflow, par exemple, vous donne la tranquillité d'esprit que vous n'êtes pas seul pour résoudre certains de vos défis de programmation les plus difficiles. Les nouveaux langages peuvent ne pas avoir une communauté établie, donc parfois vous êtes seul.
* **Performance** : C/C++ sont des langages qui compilent en code machine et exécutent certains algorithmes plus efficacement que les langages interprétés de haut niveau comme JavaScript. 
* **Élégance** : Si vous êtes vraiment un romantique, alors la syntaxe et la philosophie du langage peuvent jouer un rôle clé dans le choix de rester avec un langage.
* **Robustesse** : La sécurité des types, les messages d'erreur informatifs et la gestion intuitive de la mémoire sont autant d'aspects des langages qui soulagent le programmeur de tout souci autre que la tâche à accomplir.
* **Héritage** : Parfois, l'argument "c'est toujours été fait comme ça" tend à être une raison suffisante pour maintenir une tradition. 

En effet, les langages impératifs sont sans doute les plus populaires dans l'industrie (voir le graphique ci-dessous), peut-être parce que ces langages ont réussi à satisfaire la plupart des critères ci-dessus. Cependant, vous avez lu jusqu'à ce point dans cet article, alors je parie que vous êtes prêt à essayer quelque chose de nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-4.png)
_Source : [https://www.tiobe.com/tiobe-index/](https://www.tiobe.com/tiobe-index/)_

Nous allons plonger dans quelques exemples concrets, alors accrochez-vous, attachez vos ceintures et gardez vos bras à l'intérieur du véhicule. 

## Comparaison des langages

Supposons que vous souhaitiez écrire un algorithme pour un rover martien qui envoie intelligemment des enregistrements vidéo au contrôle de mission sur Terre. Il n'y a pas de connexion fibre optique à haute vitesse entre les planètes, donc l'ordre dans lequel les vidéos sont envoyées est vraiment important.

La liste des enregistrements vidéo peut être définie comme suit :

```javascript
videos = [
    {name: "Excavation", minutes: 22, anomaly: true},
    {name: "Panoramique du ciel", minutes: 11, anomaly: false}
]
```

Disons que le contrôle de mission n'est intéressé que par la récupération des vidéos qui durent moins de 20 minutes, donc vous souhaitez écrire un algorithme qui séquence les vidéos en conséquence. Dans les prochaines sections, nous verrons comment différents paradigmes de langage pourraient implémenter cette tâche simple.

### Implémentation impérative

Si une boucle `for` à travers le tableau `videos` est votre premier instinct, alors vous pensez comme un programmeur impératif. Par exemple, vous pouvez vouloir utiliser une instruction `if` dans la boucle pour ajouter sélectivement des vidéos qui durent moins de 20 minutes à une file d'attente, comme montré ci-dessous :

```javascript

queue = []
for (var i = 0; i < videos.length; i++) {
    if (videos[i].minutes < 20) {
        queue.push(items[i])
    }
}

```

Les variables `queue` et `i` sont déclarées avec des valeurs initiales de `[]` et `0`, respectivement. Ensuite, le reste du code spécifie **comment** mettre à jour les variables.

### Implémentation fonctionnelle

Les programmeurs fonctionnels sourient et nous présentent une élégante ligne de code :

```javascript
queue = videos.filter(x => x.minutes < 20)
```

Ici, `filter` est une fonction qui réduit un tableau en fonction d'un prédicat. L'accent n'est plus mis sur la manière dont les variables sont mises à jour via un algorithme, mais plutôt sur **ce que** les transformations de données doivent se produire pour obtenir le résultat souhaité. 

### Implémentation orientée tâche

Dans les langages orientés tâche, vous définissez l'objectif et les actions possibles. L'objectif, dans notre cas, est de choisir des vidéos qui durent moins de 20 minutes. 

Une façon de rédiger des objectifs est de lister les situations par ordre de préférence, comme `[{minutes: 10}, {minutes: 40}]`, ce qui déclare que `minutes == 10` est plus favorable que `minutes == 40`. 

```javascript
preference = [{minutes: 10}, {minutes: 40}]
```

L'action consiste à sélectionner une vidéo dans la liste `videos`. Nous le faisons en utilisant l'instruction `fork`, qui est une instruction `if` généralisée. Les instructions `if` traditionnelles exécutent la première condition d'entrée satisfaisante, mais les instructions `fork` considèrent toutes les conditions d'entrée satisfaisantes et choisissent celle qui caractérise le mieux nos préférences en recherchant (par exemple, recherche en profondeur d'abord) vers l'avant dans le temps.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-197.png)
_Un `fork` dans la route. (Photo par [Jens Lelie](https://unsplash.com/@leliejens?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit))_

Le programmeur liste les choix candidats et laisse le runtime résoudre le meilleur chemin à prendre. Ainsi, une partie de la charge cognitive de définition du comportement du système est déchargée du programmeur.

```javascript
#{model: [preference]}
fork {
    _ {
        name, minutes, anomaly = videos[0]
        print name
    }
    _ {
        name, minutes, anomaly = videos[1]
        print name
    }
}
```

Le runtime du langage résout les forks en choisissant un bloc candidat qui augmentera l'utilité de la situation. Dans ce cas, le runtime sélectionnera les vidéos de durée plus courte. 

## Comprendre la puissance de chaque paradigme

Admettons-le, pour que le code reste pertinent, il doit être continuellement maintenu. Le refactoring, l'amélioration et la mise à l'échelle peuvent parfois être un peu effrayants. C'est pourquoi chacun des trois paradigmes championne ses propres mécanismes pour faire face aux exigences changeantes.

**Conception orientée objet** dans les langages impératifs : Au lieu d'accéder directement aux données, le programmeur définit des interfaces, qui masquent les détails d'implémentation de la manière dont les données changent. Ainsi, vous pouvez brancher et jouer avec ces *objets* pour de nouveaux problèmes, sans avoir besoin de vous submerger avec tous les détails mineurs.

**Fonctions pures** dans les langages fonctionnels : Une fonction pure est légèrement similaire à une table de recherche (comme un dictionnaire ou une carte). Elle garantit que, peu importe comment le logiciel évolue, la fonction pure ne mettra pas accidentellement à jour les variables au-delà de sa portée. Enchaîner des fonctions pures ensemble crée des fonctions plus complexes qui restent pures, vous permettant de refactoriser facilement sans vous soucier des variables globales.

**Tâches** dans les langages orientés tâche : Les tâches vous permettent d'expliquer un comportement souhaité sans avoir besoin de détailler un plan concret. Par exemple, définir ce que l'on peut vouloir pour le dîner est différent d'écrire une recette pour décrire les étapes précises dans la cuisine. Le runtime du langage est responsable de l'assemblage des instructions qui accomplissent la tâche, tandis que le programmeur est responsable de la définition minutieuse des états souhaitables.

Par exemple, dans notre exemple de rover martien, disons que les exigences ont changé : le contrôle de mission veut maintenant ne récupérer que les vidéos avec des anomalies. Considérez comment vous réécririez le code impératif, fonctionnel et orienté tâche. 

Je vous laisse réfléchir aux deux premiers, mais dans les langages orientés tâche, changez simplement l'objectif pour changer le comportement du programme : 

```javascript
preference = [{anomaly: true}, {anomaly: false}]
```

À mesure que les systèmes deviennent plus complexes, les langages orientés tâche révèlent des abstractions puissantes qui permettent aux programmeurs de mettre à l'échelle et de modifier le comportement de leurs systèmes plus efficacement. Le programmeur se concentre sur la définition du **pourquoi**, tandis que le runtime compose le **comment**. Ce découplage explicite des objectifs par rapport aux actions aide à atténuer les échecs logiciels dus à des cas limites imprévus. 

Ces langages orientés tâche pourraient un jour devenir la norme de facto pour la rédaction du comportement des agents de jeux vidéo (PNJ), des robots industriels, des chatbots ou de tout système de prise de décision. La maturité technique de la conception des langages de programmation n'a même pas atteint son adolescence – par exemple, comparée à l'histoire de l'automobile, nous n'avons même pas atteint la Ford Model T. C'est maintenant le moment pour les aventuriers de découvrir de nouveaux principes fondamentaux du logiciel. 

Si vous souhaitez essayer [DMPL](http://w3.org/2019/11/dms), rejoignez le [W3C](https://www.w3.org/community/conv/) Conversational Interfaces Community Group, et suivez [@binroot](https://twitter.com/binroot) pour plus d'annonces, de nouvelles et de discussions.