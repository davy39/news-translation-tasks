---
title: 'Concepts de Programmation Orientée Objet : Comment passer de Zéro à Un avec
  les Objets'
subtitle: ''
author: Parathan Thiyagalingam
co_authors: []
series: null
date: '2019-08-07T19:09:25.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-concepts
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca108740569d1a4ca4c46.jpg
tags:
- name: Blogging
  slug: blogging
- name: coding
  slug: coding
- name: freeCodeCamp.org
  slug: freecodecamp
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: 'Concepts de Programmation Orientée Objet : Comment passer de Zéro à Un
  avec les Objets'
seo_desc: Object Oriented Programming is one of the most widely used programming paradigms.
  The name itself defines how it works. “Object Oriented” - the Object plays an important
  role. Manipulating objects and getting the results is the ultimate goal of Objec...
---

La Programmation Orientée Objet est l'un des paradigmes de programmation les plus largement utilisés. Le nom lui-même définit comment cela fonctionne. « Orienté Objet » - l'Objet joue un rôle important. Manipuler des objets et obtenir des résultats est l'objectif ultime de la Programmation Orientée Objet.

Les langues qui utilisent les paradigmes de Programmation Orientée Objet sont connues sous le nom de Langages de Programmation Orientée Objet. Ce sont principalement des langues de haut niveau telles que

1. Java
2. C#
3. Python - Python est à la fois un langage Scripté/Structuré et Orienté Objet

Pour programmer en Programmation Orientée Objet, des concepts appelés « **Concepts Orientés Objet** » sont utilisés. Ces concepts simplifient et ajoutent plus de valeur à la Programmation Orientée Objet.

Ces concepts sont

1. Encapsulation
2. Abstraction
3. Polymorphisme
4. Héritage

Avant de passer à ces concepts, nous devons connaître la Classe et les Objets.

**Un Objet** est l'entité de base à l'exécution en POO. Dans notre vie quotidienne, nous voyons beaucoup d'objets comme une télévision, un téléphone mobile, un chien, des humains, des voitures et d'autres objets vivants et non vivants. Ceux-ci peuvent être représentés comme des objets en POO.

**Une Classe** est un plan ou un prototype qui définit des variables/propriétés et des méthodes/fonctions communes à tous les objets d'un certain type. C'est un composant logique.

En termes simples, la Classe est un type de données **définis par l'utilisateur**. Les Objets sont des **variables** d'une Classe. Une fois la Classe créée, nous pouvons créer autant d'Objets que nous le souhaitons.

Par exemple, prenons une classe nommée Arbre. L'état/propriétés de la classe Arbre sont :

* Nom de l'arbre
* Âge de l'arbre
* Type de l'arbre
* Hauteur de l'arbre

L'état/propriétés sont utilisés pour définir les attributs d'un objet.

C'est-à-dire que **État/propriétés/attributs** représentent tous la même chose.

Les comportements de l'Arbre peuvent être :

* Donner des fruits
* Chute des feuilles
* Absorber l'eau des racines vers les parties supérieures
* Créer des ombres

Ensuite, Mango est une variable de la Classe Arbre. Nous pouvons stocker et récupérer toutes les propriétés et comportements que nous avons définis pour la classe Arbre en créant un objet de Mango.

Syntaxe pour créer un objet de Mango à partir de la classe Arbre :

												**Tree** Mango;

### Encapsulation

Avez-vous déjà utilisé une tablette/médicament encapsulée par une couverture colorée ?

![Image](https://www.freecodecamp.org/news/content/images/2019/08/pills_tablets_medicine_capsule_heal_drugs_pharmacy_nutrient_additives-859474.jpg-d.jpeg)
_Les médicaments sont encapsulés et placés à l'intérieur de la tablette_

À l'intérieur, le médicament est conservé en toute sécurité. Nous ne pouvons rien voir à l'œil nu. Pour voir ce qu'il y a à l'intérieur, nous devons ouvrir cette couverture...

De même, tous les **membres de données (variables, attributs/propriétés)** et **comportements (fonctions/méthodes)** sont rassemblés et fermés. La classe est le meilleur exemple d'Encapsulation.

Par exemple,

Vous allez à la pharmacie pour acheter des médicaments prescrits. Vous remettez l'ordonnance au pharmacien et il/elle prendra le médicament dans le magasin et vous donnera la facture.

Dans ce scénario,

Médicaments - agissent comme des variables ou propriétés ou attributs

Pharmacien - agit comme une fonction membre/méthode où il/elle aide à vous donner le médicament

Vous - application externe ou un autre code logiciel

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-from-2019-08-20-22-13-54.png)

En utilisant l'Encapsulation, les **données peuvent être restreintes** de l'utilisation du monde extérieur. La fonction définie dans la classe peut uniquement accéder aux propriétés. Cela peut être défini à l'étape de l'implémentation. Les programmeurs peuvent définir et spécifier l'accessibilité des variables membres pendant le développement plutôt que de rendre toutes les variables globales comme dans les langues procédurales. Ce contrôle de l'accessibilité est également connu sous le nom de **Masquage d'informations**.

L'Encapsulation **permet d'exposer les choses nécessaires et de cacher les choses importantes du monde extérieur**. Ainsi, les parties cachées d'une classe agissent comme **Encapsulation** et les parties exposées agissent comme **Abstraction**.

### Abstraction

Exposer les caractéristiques nécessaires d'une classe **sans expliquer beaucoup ou les détails** est fait par l'Abstraction.

Ce matin, je voulais faire un thé chaud et j'ai utilisé une bouilloire pour faire bouillir l'eau. J'ai simplement allumé le bouton **On** pour commencer à faire bouillir l'eau. Je ne veux pas savoir le flux de travail interne de la bouilloire où elle a une haute résistance et cette résistance produit de la chaleur et fait bouillir l'eau. Au lieu de cela, je dois accomplir mon travail facilement. Par conséquent, avoir ce bouton On pour faire bouillir l'eau est connu sous le nom d'Abstraction.

De même, nous pouvons prendre une télécommande qui aide à manipuler l'opération de la TV en utilisant des touches simples sur la télécommande.

**L'abstraction de données** est une technique de programmation qui dépend de la séparation de **l'interface** et de **l'implémentation**.

Cette abstraction de données peut être archivée à partir de l'utilisation de 2 classes différentes lors de la programmation en utilisant la POO

1. Classe d'Abstraction : (0-100)% d'abstraction
2. Classe d'Interface : 100% d'abstraction

### Héritage

Le mot lui-même décrit sa fonctionnalité. Tout le monde a ses qualités d'héritage dès sa naissance. Vous pourriez avoir les qualités de vos grands-parents/vos parents dès votre naissance. C'est ce que fait l'Héritage en POO.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-from-2019-08-20-22-14-01.png)

Une classe peut avoir des propriétés et des méthodes de sa classe parente. De plus, la classe peut avoir ses propres propriétés et méthodes. La classe parente est appelée **classe de base**. La classe qui hérite de la classe de base est appelée **classe dérivée**. L'héritage est la fonctionnalité la plus puissante de la POO.

En utilisant efficacement l'Héritage, nous pourrions économiser beaucoup de temps et réduire les erreurs dans notre programme. Cela nous permet d'**augmenter la qualité du travail** et la **productivité**.

Il existe différents types d'Héritage

1. Héritage Simple
2. Héritage Hiérarchique
3. Héritage Multiple
4. Héritage Multi Niveau

### Polymorphisme

Le Polymorphisme est un terme **Grec** qui fait référence à la capacité de prendre plus d'une forme / surcharge.

Par exemple, nous connaissons tous les **fonctions** en programmation. Elles prennent différents arguments à l'intérieur des parenthèses. Le Polymorphisme n'est rien d'autre qu'avec le même nom de fonction, différents arguments passés pour obtenir le résultat.

Par exemple : une fonction appelée sum peut prendre 2 arguments ou 3 arguments.

									sum(3,4)  sum(10,23,56)  
Appeler ces fonctions en fournissant un nombre approprié de paramètres donnera le résultat selon la manière dont la fonction appelée a été conçue.

**_Comment le programme distingue-t-il quelle fonction doit être exécutée dans le scénario ci-dessus ?_**

Il existe une fonctionnalité appelée **Liaison Dynamique** en POO. Cela appellera la fonction réelle selon l'exécution du programme. Lorsque le programme exécute la fonction avec 2 arguments, le compilateur prend les fonctions à deux arguments pour exécuter le programme, de même pour 3 arguments également.

Jusqu'à l'exécution, le compilateur ne saura pas exactement quelle fonction doit être invoquée. Cela dépend de la manière dont le programme appelle le nom de la fonction. Cela est également connu sous le nom de **Liaison Tardive**.

### Utilisations des Concepts Orientés Objet

* Les données peuvent être cachées de l'extérieur en utilisant **l'Encapsulation** (Masquage d'informations)
* Le code peut être réutilisé en utilisant **l'Héritage**
* Les opérateurs/méthodes.fonctions peuvent être surchargés en utilisant **le Polymorphisme**. C'est-à-dire : le même nom de fonction ou d'opérateur peut être utilisé pour le multitâche
* L'abstraction de données peut être archivée à partir de **l'Abstraction**.
* Les migrations de projet sont faciles (peuvent être converties en taille plus grande à partir de taille plus petite)
* Partitionnement des travaux pour le même projet
* Complexité logicielle gérable

### Domaines d'application de la POO

1. IA et systèmes experts
2. Applications d'entreprise
3. Réseau de neurones et programmation parallèle
4. Systèmes d'automatisation de bureau

J'espère que vous avez apprécié une brève introduction aux Concepts Orientés Objet en lisant. J'espère écrire comment nous pouvons programmer la Programmation Orientée Objet dans mes prochains articles également.

---

Veuillez envoyer vos commentaires sur mon article à parathan19@gmail.com

[LinkedIn](https://www.linkedin.com/in/parathantl/) | [Twitter](http://twitter.com/parathantl)