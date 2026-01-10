---
title: Comment deux principes de développement logiciel peuvent sauver votre projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-18T01:38:33.000Z'
originalURL: https://freecodecamp.org/news/how-2-software-development-principles-can-save-your-project-573fc10461cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5IVmxQk8nIcC_qJ4n2fWBw.jpeg
tags:
- name: coding
  slug: coding
- name: design patterns
  slug: design-patterns
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment deux principes de développement logiciel peuvent sauver votre projet
seo_desc: 'By Jordy Baylac

  Introduction

  In this post I will focus on explaining how one Design Pattern (Inversion Of Control)
  and one Practice (YAGNI) can reduce the possibility of having a failed software
  project. You can start applying these techniques right ...'
---

Par Jordy Baylac

### Introduction

Dans cet article, je vais me concentrer sur l'explication de la manière dont un modèle de conception (**Inversion de Contrôle**) et une pratique (**YAGNI**) peuvent réduire la possibilité d'avoir un projet logiciel échoué. Vous pouvez commencer à appliquer ces techniques dès maintenant.

Si vous êtes un Engineering Manager, cet article est une bonne lecture si vous souhaitez réduire la volatilité du coût marginal des fonctionnalités ?.

### Inversion de Contrôle (IoC)

Voulais-je dire _Injection de Dépendances_ ? Pas vraiment, mais nous pouvons utiliser l'Injection de Dépendances comme outil pour atteindre l'Inversion de Contrôle entre les dépendances.

**IoC** peut aider à changer la direction des dépendances. Cela peut aider dans les situations où le composant A dépend du composant B, et maintenant vous voulez que A ne soit pas conscient des détails d'implémentation de B.

**Situation actuelle**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RCx6u3_JOxc8XPZxR134UQ.png)
_Le composant A dépend du composant B._

**Situation cible**

![Image](https://cdn-media-1.freecodecamp.org/images/1*1ZjKqM1zSvmGvr5ygWptdA.png)
_Le composant A ne dépend pas des détails d'implémentation du composant B._

Avec cette dernière approche, le composant A ne dépend pas des spécificités du composant B. En fait, de nouvelles implémentations de _IBehaviourB_ pourraient être ajoutées au projet sans même toucher au composant A.

#### Exemple de code

_Une application inconnue ayant trois couches bien connues._

```
UI -> REST API -> Database
```

En zooming sur l'API REST, nous avons trouvé la classe _UsersController_. Nous avons noté qu'elle lit et écrit depuis/vers une _Base de données SQLServer_. Voici une implémentation possible en C# :

Si vous considérez que la solution ci-dessus n'est pas un bon design, vous avez raison ?.

Dans l'exemple, _UsersController_ est **fortement couplé** avec l'implémentation SQLServer. La méthode _postUser_ rend difficile l'écriture de **Tests** (rappelez-vous qu'un test unitaire ne doit pas toucher les bases de données ou les services externes). À mesure que l'application évolue, il y aura une forte dépendance à la bibliothèque SQLServer spécifique utilisée. Si quelqu'un décide de diviser l'application par domaine, il peut être trop tard ?.

Cet exemple de code correspond à la **"situation actuelle"** présentée au début de l'article. Dans ce cas :

* **A** = _UsersController_
* **B** = _System.Data.SqlClient_ sur .NET

Mais attendez...

**Et si nous appliquions l'Inversion de Contrôle** pour que UsersController ne dépende pas d'une implémentation spécifique de SQLServer ? Et si nous rendions l'API REST inconsciente de la couche de Persistence que nous utilisons ?

?, ok, faisons-le :

![Image](https://cdn-media-1.freecodecamp.org/images/1*E4rMivDDauz8sM-KiJuCEA.jpeg)

**20 jours plus tard** ?:

Pour simplifier, nous avons désigné trois fichiers sources, mais en pratique, ils pourraient être divisés ou situés dans des assemblages ou dossiers séparés. Cette solution correspond à la **"situation cible"** présentée au début. Dans ce cas :

* **A** = _UsersController_
* **B** = _SQLUserService_
* **IBehaviourB** = _IUserService_.

Nous l'avons fait !

Oh, mais attendez, comment la dépendance _IUserService_ est-elle injectée dans le constructeur de _UsersController_ ? Eh bien, les détails d'implémentation de cela sont hors du cadre de cet article. Cependant, si vous êtes intéressé, consultez le tutoriel que j'ai ajouté à la fin.

#### Avantages

* Notre architecture est ouverte aux extensions. De plus, nous avons réduit la nécessité de modification dans les classes existantes. Principe **Open/Close** ?
* Les tests sont faciles à écrire. Nous pouvons injecter un mock _UserService_ lors du test de UsersController ?
* La logique métier n'est pas couplée et ne dépend d'aucune stratégie de _persistence_. 

### YAGNI

_Vous n'en aurez pas besoin !_

Je considère que chaque développeur devrait adopter YAGNI comme l'une de ses pratiques principales. Ce principe peut vous sauver de l'ingénierie excessive et du code inutilisé (_intouchable_). Il peut aussi sauver votre emploi.

**Une petite histoire amusante :**

J'ai travaillé sur un projet où les architectes logiciels ont décidé de représenter presque toutes les colonnes **booléennes** dans la base de données avec un type de données **char**. Au moins, ils utilisaient l'anglais — **true** était stocké comme "Y", **false** avec "N". Cela a du sens, n'est-ce pas ? Lorsque j'ai demandé comment une solution aussi magique avait été conçue, ils ont répondu :

"De cette manière, nous sommes ouverts à la possibilité qu'un troisième état puisse arriver."

Je n'ai jamais compris comment une chose **vrai/faux** peut avoir un troisième état (peut-être pensaient-ils aux qubits). Comme vous pouvez le noter, cela s'est avéré être une très mauvaise décision et les conséquences étaient présentes partout dans le code. J'ai trouvé des choses comme :

```
if (supportVisa === "Y" || supportVisa === "y") { ...
```

La lisibilité du code était affectée, et les requêtes SQL étaient également affectées.

Mais cela ne s'est pas arrêté là. Avec le temps, le logiciel a ajouté l'internationalisation à ses interfaces utilisateur. Certaines configurations et catalogues étaient fournis par le client lui-même en utilisant une application GUI. Nous en sommes arrivés au point où certaines de nos colonnes **booléennes** avaient "S" et "N" (**S**i et **N**o en espagnol).

Le code était vraiment difficile à maintenir. Je ne veux pas parler de la solution qu'ils ont proposée ?.

### Conclusions

Selon Uncle Bob, _les bons développeurs essaieront de maximiser le nombre de décisions non prises_. N'écrivez pas quelque chose que vous croyez être utile dans six mois. Au lieu de cela, attendez les six mois, jetez un coup d'œil à votre architecture, voyez combien elle a évolué, et ensuite, faites le travail. Appliquez YAGNI.

Vous devriez gérer vos dépendances correctement. L'Inversion de Contrôle vous guidera dans cette voie.

J'espère entrer dans votre conscience et vous aider à devenir un meilleur développeur.

> "N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre." — **Martin Fowler**

### Lire plus sur

* [Injection de Dépendances en C#](https://www.codeproject.com/Articles/1234518/Dependency-Injection-using-Unity-Resolve-dependenc)
* [Injection de dépendances en TypeScript.](https://nehalist.io/dependency-injection-in-typescript/)
* [Martin Fowler sur YAGNI](https://martinfowler.com/bliki/Yagni.html)

**Veuillez partager vos pensées et poser toutes vos questions. Je serai ravi d'y répondre.** ? **Retrouvez-moi sur [Twitter.](https://twitter.com/jbaylacc)**