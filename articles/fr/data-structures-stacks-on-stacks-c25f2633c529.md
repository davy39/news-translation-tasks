---
title: 'Une Introduction en Douceur aux Structures de Données : Comment Fonctionnent
  les Piles'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-25T19:25:15.000Z'
originalURL: https://freecodecamp.org/news/data-structures-stacks-on-stacks-c25f2633c529
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3kenGRftkBau3t6MozALpw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une Introduction en Douceur aux Structures de Données : Comment Fonctionnent
  les Piles'
seo_desc: 'By Michael Olorunnisola

  Anyone who’s applied for a developer job at a large tech company — and spent days
  practicing common algorithm interview questions — has probably concluded:


  “Wow. I really gotta know data structures cold.”


  What are data struc...'
---

Par Michael Olorunnisola

Toute personne ayant postulé pour un emploi de développeur dans une grande entreprise technologique — et passé des jours à pratiquer des questions d'entretien courantes sur les algorithmes — a probablement conclu :

> « Wow. Je dois vraiment maîtriser les structures de données. »

Qu'est-ce que les structures de données ? Et pourquoi sont-elles si importantes ? Wikipedia fournit une réponse succincte et précise :

> *Une structure de données est une manière particulière d'organiser les données dans un ordinateur afin qu'elles puissent être utilisées efficacement.*

Le mot clé ici est *efficacement*, un mot que vous entendrez souvent lorsque vous analyserez différentes structures de données.

Ces structures fournissent un échafaudage pour stocker les données de manière à permettre des recherches, des insertions, des suppressions et des mises à jour rapides et dynamiques.

Aussi puissants que soient les ordinateurs, ils ne sont toujours que des machines nécessitant des instructions pour accomplir toute tâche utile (au moins jusqu'à l'arrivée de l'IA générale). En attendant, vous devez leur donner les commandes les plus claires et les plus efficaces possibles.

De la même manière que vous pouvez construire une maison de 50 façons différentes, vous pouvez structurer les données de 50 façons différentes. Heureusement pour vous, beaucoup de personnes très intelligentes ont construit de grands échafaudages qui ont résisté à l'épreuve du temps. Tout ce que vous avez à faire est d'apprendre ce qu'ils sont, comment ils fonctionnent et comment les utiliser au mieux.

Voici une liste de quelques-unes des structures de données les plus courantes. Je couvrirai chacune d'entre elles individuellement dans de futurs articles — celui-ci est entièrement consacré aux piles. Bien qu'il y ait souvent des chevauchements, chacune de ces structures a des nuances qui les rendent mieux adaptées à certaines situations :

* Piles
* Files d'attente
* Listes chaînées
* Ensembles
* Arbres
* Graphes
* Tables de hachage

Vous rencontrerez également des variations de ces structures de données, telles que les listes doublement chaînées, les b-arbres et les files d'attente prioritaires. Mais une fois que vous comprendrez ces implémentations de base, comprendre ces variations devrait être beaucoup plus facile.

Alors commençons la première partie de notre plongée dans les structures de données avec une analyse des Piles !

### **Piles**

* Littéralement une pile de données (comme une pile de crêpes)
* Ajouts (push) — toujours ajouter au sommet de la pile
* Suppressions (pop) — toujours supprimer du sommet de la pile
* **Type de motif :** **D**ernier entré, **P**remier sorti (LIFO)

![Image](https://cdn-media-1.freecodecamp.org/images/KSnmVKZl319rnXSgpeRfH277mozUpleR-wzi)

* **Exemple d'utilisation :** Utilisation des boutons de retour et d'avance dans votre navigateur

Dans de nombreux langages de programmation, les tableaux ont la fonctionnalité d'une pile intégrée. Mais pour être complet, vous allez la reconstruire ici en utilisant un objet JavaScript.

La première chose dont vous avez besoin est de créer une pile pour stocker chaque site que vous visitez, et une méthode sur votre pile pour suivre votre position actuelle :

```
class Stack {  constructor(){    this._storage = {};      this._position = -1; // indexé à 0 lorsque nous ajoutons des éléments !  }  top(){    return this._position;  }}
```

```
let browserHistory = new Stack();
```

Notez que le soulignement avant les noms de variables signifie pour les autres développeurs que ces variables sont privées et ne doivent pas être manipulées externement — seulement par les méthodes de la classe. Par exemple, je ne devrais pas exécuter quelque chose comme :

```
browserHistory._position = 2.
```

C'est pourquoi j'ai créé la méthode **top()** pour retourner la position actuelle de la pile.

Dans cet exemple, chaque site que vous visitez sera stocké dans votre pile browserHistory. Pour vous aider à suivre où il se trouve dans la pile, vous pouvez utiliser la position comme clé pour chaque site web, puis l'incrémenter à chaque nouvel ajout. Je vais faire cela via la méthode push :

```
class Stack {
```

```
  constructor(){    this._storage = {};     this._position = -1;  }
```

```
  push(value){    this._position++;     this._storage[this._position] = value   }
```

```
  top(){    return this._position;  }
```

```
}
```

```
let browserHistory = new Stack();
```

```
browserHistory.push("google.com"); // navigation vers Medium
browserHistory.push("medium.com"); // navigation vers Free Code Camp
browserHistory.push("freecodecamp.com"); // navigation vers Netflix
browserHistory.push("netflix.com"); // site actuel
```

Après l'exécution du code ci-dessus, votre objet de stockage ressemblera à ceci :

```
{
```

```
  0: "google.com"
```

```
  1: "medium.com"
```

```
  2: "freecodecamp.com"
```

```
  3: "netflix.com"
```

```
}
```

Imaginez que vous êtes actuellement sur Netflix, mais que vous vous sentez coupable de ne pas avoir terminé ce problème difficile de récursivité sur Free Code Camp. Vous décidez de cliquer sur le bouton de retour pour aller le résoudre.

Comment cette action est-elle représentée dans votre pile ? Avec pop :

```
class Stack {   constructor(){    this._storage = {};    this._position = -1;  }   push(value){    this._position++;     this._storage[this._position] = value;   }   pop(){    if(this._position > -1){      let val = this._storage[this._position];       delete this._storage[this._position];       this._position--;      return val;    }  }
```

```
  top(){    return this._position;  }}
```

```
let browserHistory = new Stack();
```

```
browserHistory.push("google.com"); // navigation vers Medium
browserHistory.push("medium.com"); // navigation vers Free Code Camp
browserHistory.push("freecodecamp.com"); // navigation vers Netflix
browserHistory.push("netflix.com"); // site actuel
```

```
browserHistory.pop(); // Retourne netflix.com
```

```
// Free Code Camp est maintenant notre site actuel
```

En cliquant sur le bouton de retour, vous supprimez le site le plus récent ajouté à votre historique de navigation et affichez celui au sommet de votre pile. Vous décrémentez également la variable de position pour avoir une représentation précise de l'endroit où vous vous trouvez dans l'historique. Tout cela ne devrait se produire que s'il y a effectivement quelque chose dans votre pile, bien sûr.

Cela semble bien jusqu'à présent, mais quelle est la dernière pièce manquante ?

Lorsque vous avez terminé de résoudre le problème, vous décidez de vous récompenser en retournant sur Netflix en cliquant sur le bouton d'avance. Mais où se trouve Netflix dans votre pile ? Vous l'avez techniquement supprimé pour économiser de l'espace, donc vous n'y avez plus accès dans votre browserHistory.

Heureusement, la fonction pop l'a retourné, donc peut-être pouvez-vous le stocker quelque part pour plus tard lorsque vous en aurez besoin. Et si c'était dans une autre pile !

Vous pouvez créer une pile « forward » pour stocker chaque site qui est retiré de votre browserHistory. Ainsi, lorsque vous souhaitez y retourner, vous les retirez simplement de la pile forward et les poussez à nouveau sur votre pile browserHistory :

```
class Stack {   constructor(){    this._storage = {};    this._position = -1;  }   push(value){    this._position++;     this._storage[this._position] = value;   }   pop(){    if(this._position > -1){      let val = this._storage[this._position];       delete this._storage[this._position];       this._position--;      return val;    }  }
```

```
top(){    return this._position;  }}
```

```
let browserHistory = new Stack();
let forward = new Stack() // Notre nouvelle pile forward !
```

```
browserHistory.push("google.com");
browserHistory.push("medium.com");
browserHistory.push("freecodecamp.com");
browserHistory.push("netflix.com");
```

```
// cliquer sur le bouton de retour
```

```
forward.push(browserHistory.pop()); // la pile forward contient Netflix
```

```
// ... Nous résolvons le problème Free Code Camp ici, puis cliquons sur forward !
```

```
  browserHistory.push(forward.pop());
```

```
// Netflix est maintenant notre site actuel
```

Et voilà ! Vous avez utilisé une structure de données pour réimplémenter la navigation de base du navigateur avec les boutons de retour et d'avance !

Maintenant, pour être complètement complet, disons que vous êtes allé sur un site complètement nouveau depuis Free Code Camp, comme LeetCode pour obtenir plus de pratique. Techniquement, vous auriez toujours Netflix dans votre pile forward, ce qui n'a vraiment pas de sens.

Heureusement, vous pouvez implémenter une simple boucle while pour vous débarrasser de Netflix et de tout autre site rapidement :

```
// Lorsque je navigue manuellement vers un nouveau site, vider la pile forward
```

```
while(forward.top() > -1){  forward.pop();}
```

Super ! Maintenant, votre navigation devrait fonctionner comme elle est censée le faire.

Il est temps pour un rapide récapitulatif. Les piles :

1. Suivent un motif Dernier Entré, Premier Sorti (LIFO)
2. Ont une méthode push (ajout) et pop (suppression) qui gèrent le contenu de la pile
3. Ont une propriété top qui nous permet de suivre la taille de votre pile et la position actuelle du sommet.

À la fin de chaque article de cette série, je ferai une brève [analyse de la complexité temporelle](http://bigocheatsheet.com/) des méthodes de chaque structure de données pour obtenir un peu plus de pratique.

Voici le code à nouveau :

```
push(value){    this._position++;     this._storage[this._position] = value;   }   pop(){    if(this._position > -1){      let val = this._storage[this._position];       delete this._storage[this._position];       this._position--;      return val;    }  }    top(){    return this._position;  }
```

**Push** (ajout) est **O(1)**. Puisque vous connaîtrez toujours la position actuelle (grâce à votre variable de position), vous n'avez pas besoin d'itérer pour ajouter un élément.

**Pop** (suppression) est **O(1)**. Aucune itération n'est nécessaire pour la suppression puisque vous avez toujours la position actuelle du sommet.

**Top** est **O(1)**. La position actuelle est toujours connue.

Il n'y a pas de méthode de recherche native sur les piles, mais si vous deviez en ajouter une, quelle complexité temporelle pensez-vous qu'elle aurait ?

**Find** (recherche) serait **O(n)**. Vous devriez techniquement itérer sur votre stockage jusqu'à ce que vous trouviez la valeur que vous cherchiez. Cela revient essentiellement à la méthode indexOf sur les tableaux.

### Lectures complémentaires

[Wikipedia](https://en.wikipedia.org/wiki/List_of_data_structures) propose une liste approfondie des types de données abstraits.

Je n'ai pas eu l'occasion d'aborder le sujet du débordement de pile, mais si vous avez lu mon article sur la [récursivité](https://medium.freecodecamp.com/recursion-recursion-recursion-4db8890a674d#.pxck4rh8k), vous avez peut-être une bonne idée de pourquoi ils se produisent. Pour approfondir cette connaissance, il y a un excellent article à ce sujet sur [StackOverflow](http://stackoverflow.com/questions/26158/how-does-a-stack-overflow-occur-and-how-do-you-prevent-it) (*vous voyez ce que j'ai fait là ?*).

Dans mon prochain article, je passerai directement aux files d'attente.