---
title: 'Structures de données 101 : Tableaux — Une introduction visuelle pour débutants'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-02-12T16:29:51.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-arrays-a-visual-introduction-for-beginners-7f013bcc355a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*plaTqL5DDa2MgqeK-0EClg.png
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Structures de données 101 : Tableaux — Une introduction visuelle pour
  débutants'
seo_desc: 'Get to know the data structures that you use every day.

  👋 Welcome! Let’s Start with some Vital Context. Let me ask you this:✅ Do you listen
  to music on your smartphone?✅ Do you keep a list of contacts on your phone?✅ Have
  you ever seen a leaderboard...'
---

### Découvrez les structures de données que vous utilisez chaque jour.

👋 Bienvenue ! Commençons par un contexte essentiel. Laissez-moi vous poser ces questions :   
✅ Écoutez-vous de la musique sur votre smartphone ?  
✅ Avez-vous une liste de contacts sur votre téléphone ?  
✅ Avez-vous déjà vu un tableau des scores lors d'une compétition ?

**Si vous avez répondu "oui" à l'une de ces questions, alors il est presque certain que vous avez utilisé des tableaux sans même le savoir ! 😃** Les tableaux sont des structures de données très puissantes qui stockent des **listes d'éléments**. Ils ont des applications infinies. Ils sont très importants dans le monde de l'informatique.

Dans cet article, vous apprendrez les avantages et les inconvénients des tableaux, leur structure, leurs opérations et leurs cas d'utilisation.

**Commençons ! **👍****

### 🔎 Plongez dans la structure de base des tableaux

Pour comprendre comment ils fonctionnent, il est très utile de visualiser la mémoire de votre ordinateur comme une grille, comme celle ci-dessous. Chaque morceau d'information est stocké dans l'un de ces petits éléments (carrés) qui composent la grille.

![Image](https://cdn-media-1.freecodecamp.org/images/uxNDqnrhHuS197WjrTeak8WQq2QZKAJD5xp4)

**Les tableaux** tirent parti de cette structure de "grille" pour **stocker** des **listes d'informations liées dans** des **emplacements mémoire adjacents** afin de garantir une efficacité extrême pour trouver ces valeurs. 🔳🔳🔳🔳

**Vous pouvez penser aux tableaux comme ceci :**

![Image](https://cdn-media-1.freecodecamp.org/images/HjKZtf6JKxcrH8t51iRrId-4lTqjOlGtICip)

**Leurs éléments sont côte à côte en mémoire.** Si vous devez accéder à plus d'un d'entre eux, le processus est extrêmement optimisé car votre ordinateur sait déjà où se trouve la valeur.

Génial, n'est-ce pas ? Apprenons comment cela fonctionne en coulisses ! 😃

#### 📜 Classification

Les tableaux sont classés comme **Structures de Données Homogènes** car ils stockent des **éléments du même type**.

Ils peuvent stocker des nombres, des chaînes de caractères, des valeurs booléennes (vrai et faux), des caractères, des objets, etc. Mais **une fois que vous avez défini le type de valeurs que votre tableau stockera, tous ses éléments doivent être de ce même type. Vous ne pouvez pas "mélanger" différents types de données.**

![Image](https://cdn-media-1.freecodecamp.org/images/sbk9-CGxQ5VKddqpz9S12GxpR26I8f8e0hj6)

![Image](https://cdn-media-1.freecodecamp.org/images/oS1i6uyY71HPvrPCVEqEVDpscFgyeUCAwlPN)

### 👀 Lecture des valeurs — La magie commence !

Le pouvoir incroyable des tableaux vient de leur **efficacité à accéder aux valeurs**. Cela est réalisé grâce à leur structure en forme de grille. Examinons cela plus en détail.🔍

**Lorsque vous créez un tableau, vous :**  
- L'assignez à une variable. 👈  
- Définissez le type d'éléments qu'il stockera. 🎊  
- Définissez sa taille (le nombre maximum d'éléments). 📜

![Image](https://cdn-media-1.freecodecamp.org/images/xzGLFN8ymKFdxyZWHk4YInJ6cyQQHxUJiJQX)

**📌 Note :** Le nom que vous assignez à cette variable est très important car vous l'utiliserez plus tard dans votre code pour accéder aux valeurs et modifier le tableau.

Mais comment pouvez-vous indiquer à l'ordinateur quelle valeur particulière vous souhaitez accéder ? C'est là que les indices jouent un rôle vital !

#### 1️⃣ Indices

**Vous utilisez ce qu'on appelle un "index"** ("indices" au pluriel) pour accéder à une valeur dans un tableau. Il s'agit d'un nombre qui fait référence à l'emplacement où la valeur est stockée.

Comme vous pouvez le voir dans le diagramme ci-dessous, le premier élément du tableau est référencé en utilisant l'index 0. En vous déplaçant vers la droite, l'index augmente de un pour chaque espace en mémoire.

![Image](https://cdn-media-1.freecodecamp.org/images/TuWNHRYkAgpBEjuszG9DElXUIAf8Osw2z--7)

**📌 Note :** Je sais que cela semble étrange au début de commencer à compter à partir de 0 au lieu de 1, mais cela s'appelle [Zero-Based Numbering](https://en.wikipedia.org/wiki/Zero-based_numbering). C'est très courant en informatique.

**La syntaxe générale pour accéder à un élément est :** `**<ArrayVariable>[<index>]**`

**Par exemple :**  
Si votre tableau est stocké dans la variable `**myArray**` et que vous souhaitez accéder au premier élément (à l'index 0), vous utiliseriez `**myArray[0]**`

![Image](https://cdn-media-1.freecodecamp.org/images/Yu9nSlzmHkZV4e7f7sulFIamSwWONw4wNcpg)

#### 2️⃣ Mémoire

Maintenant que vous savez comment accéder aux valeurs, voyons comment les tableaux sont stockés dans la mémoire de votre ordinateur. **Lorsque vous définissez la taille du tableau, tout cet espace en mémoire est "réservé" à partir de ce moment** pour les valeurs futures que vous pourriez vouloir insérer.

**📌 Note :** Si vous ne remplissez pas le tableau avec des valeurs, cet espace restera réservé et vide jusqu'à ce que vous le fassiez.

**Par exemple :**  
Supposons que vous définissez un tableau de taille 5 mais que vous n'insérez qu'une seule valeur. Tout cet espace restant sera vide et "réservé" en mémoire, en attente de futures affectations.

![Image](https://cdn-media-1.freecodecamp.org/images/7Hoys8sq0RuDF4-Rgr4WRD4RrImGhtQmzR9P)

Cela est clé car les tableaux sont extrêmement efficaces pour accéder aux valeurs car tous les éléments sont stockés dans des espaces contigus en mémoire. **De cette façon, l'ordinateur sait exactement où chercher pour trouver l'information que vous avez demandée.**

**Mais…** il y a un inconvénient 😞 car cela **n'est pas efficace en mémoire**. Vous réservez de la mémoire pour des opérations futures qui peuvent ne pas se produire. **C'est pourquoi les tableaux sont recommandés dans les situations où vous savez à l'avance combien d'éléments vous allez stocker.**

### ⚗️ Opérations — En coulisses !

Maintenant que vous savez ce que sont les tableaux, quand ils sont utilisés et comment ils stockent les éléments, nous allons plonger dans leurs opérations comme l'insertion et la suppression.

#### 1️⃣ Insertion — Bienvenue !

Supposons que nous avons un tableau de taille 6 et qu'il reste encore un espace vide. Nous voulons insérer un élément "e" au début du tableau (index 0), mais cet endroit est déjà occupé par l'élément "a". Que devons-nous faire ?

![Image](https://cdn-media-1.freecodecamp.org/images/JX8sviJCpwXkWT6mZ4fDIwzSNFDUZ0C8LfrP)

**Pour insérer dans les tableaux**, nous déplaçons tous les éléments situés à droite du site d'insertion, d'un index vers la droite. L'élément "a" sera maintenant à l'index 1, l'élément "b" sera à l'index 2 et ainsi de suite…

![Image](https://cdn-media-1.freecodecamp.org/images/8KFz74m1v5dPBzXGr5IXAvt3a5XFbzL78gVs)

**📌 Note :** Vous devrez créer une variable pour suivre le dernier index qui contient des éléments. Dans le diagramme ci-dessus, le tableau est rempli jusqu'à l'index 4 avant l'insertion. De cette façon, vous pouvez déterminer si le tableau est plein et quel index vous devez utiliser pour insérer un élément à la fin.

Après avoir fait cela, notre élément est inséré avec succès. 👏

![Image](https://cdn-media-1.freecodecamp.org/images/VqmOSyTnIvPWbkw9p1PIhenPthaxd3bHxzvS)

#### ⚠️ Attendez une minute ! Que se passe-t-il si le tableau est plein ?

Que pensez-vous qu'il se passera si le **tableau est plein et que vous essayez d'insérer** un élément ? 😱

![Image](https://cdn-media-1.freecodecamp.org/images/IlI473xQSRYYCMjlcF0YMSOs-Kca2hqqupGk)

**Dans ce cas, vous devez créer un nouveau tableau plus grand et copier manuellement tous les éléments dans ce nouveau tableau.** Cette opération est **très coûteuse en temps**. Imaginez ce qui se passerait si vous aviez un tableau avec des millions d'éléments ! Cela pourrait prendre très longtemps à compléter. ⏳

![Image](https://cdn-media-1.freecodecamp.org/images/P2q2OaohnsEPDa3KMu3e6eOJaPpw-bpufH95)

**📌 Note :** La seule exception à cette règle, lorsque l'insertion est très rapide, est lorsque vous insérez un élément à la **fin** du tableau (à l'index situé à droite du dernier élément) et qu'il reste encore de l'espace disponible. Cela se fait en temps constant O(1).

#### 2️⃣ Suppression — Au revoir !

Maintenant, supposons que vous souhaitez supprimer un élément du tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/yG5HNXTX7Xj7aXAstjEMU2VNWHkEZXtG9q5z)

Pour maintenir l'efficacité de l'accès aléatoire (pouvoir accéder au tableau via un index extrêmement rapidement), les éléments doivent être stockés dans des espaces contigus de la mémoire. **Vous ne pouvez pas simplement supprimer l'élément et laisser cet espace vide.**

![Image](https://cdn-media-1.freecodecamp.org/images/bd9KRk22FyVVrW3RJEKvCd8y-VAJQodeABOD)

Vous devez déplacer les éléments qui viennent après l'élément que vous souhaitez supprimer d'un index vers la gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/G13PaxPTyIQRCBJdh2Ioup-4jM-qlDMnTVd7)

Et enfin, vous avez ce tableau résultant 👋. Comme vous pouvez le voir, "b" a été supprimé avec succès.

![Image](https://cdn-media-1.freecodecamp.org/images/85yhQ9XK19hJ2paBhkb9Cf0-8v52DO0igncc)

**📌 Note :** La suppression est très efficace lorsque vous retirez le **dernier** élément. Puisque vous devez créer une variable pour suivre le dernier index qui contient des éléments (dans le diagramme ci-dessus, index 3), vous pouvez directement supprimer cet élément en utilisant l'index.

#### 3️⃣ Trouver un élément

Vous avez trois options pour trouver un élément dans un tableau :

* **Si vous savez où il se trouve**, utilisez l'index.
* **Si vous ne savez pas où il se trouve et que vos données sont triées**, vous pouvez utiliser des algorithmes pour optimiser votre recherche, comme la recherche binaire.
* **Si vous ne savez pas où il se trouve et que vos données ne sont pas triées**, vous devrez rechercher dans chaque élément du tableau et vérifier si l'élément actuel est celui que vous cherchez (veuillez voir la séquence de diagrammes ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/hlrl4kdBl3eM8cT7DXJX7rItWeHzTvrretfG)

![Image](https://cdn-media-1.freecodecamp.org/images/nFz0jZQu4dtAqv4fauEE-7zVqxtGlKVVfKew)

![Image](https://cdn-media-1.freecodecamp.org/images/hxcwNp-VfOem0psPkl26HCLrILCR1mlrdpku)

![Image](https://cdn-media-1.freecodecamp.org/images/dEd3ArmSERT63fk95KSlKwwCqdwjvUBAOQen)

### 👋 En résumé…

* **Les tableaux sont des structures de données extrêmement puissantes** qui stockent des éléments du même type. Le type d'éléments et la taille du tableau sont fixes et définis lorsque vous le créez.
* **La mémoire est allouée immédiatement** après la création du tableau et elle est vide jusqu'à ce que vous assigniez les valeurs.
* Leurs **éléments sont situés dans des emplacements contigus en mémoire**, donc ils peuvent être accédés très efficacement (accès aléatoire, O(1) = temps constant) en utilisant des **indices**.
* **Les indices commencent à 0**, pas à 1 comme nous en avons l'habitude.
* **Insérer des éléments** au début ou au milieu du tableau implique de déplacer des éléments vers la droite. Si le tableau est plein, créer un nouveau tableau plus grand (ce qui n'est pas très efficace). Insérer à la fin du tableau est très efficace, en temps constant O(1).
* **Supprimer des éléments** du début ou du milieu du tableau implique de déplacer tous les éléments vers la gauche pour éviter de laisser un espace vide en mémoire. Cela garantit que les éléments sont stockés dans des espaces contigus en mémoire. Supprimer à la fin du tableau est très efficace car vous supprimez uniquement le dernier élément.
* **Pour trouver un élément**, vous devez vérifier tout le tableau jusqu'à ce que vous le trouviez. Si les données sont triées, vous pouvez utiliser des algorithmes tels que la recherche binaire pour optimiser le processus.

> _"Apprenez d'hier, vivez pour aujourd'hui, espérez pour demain. L'important est de ne pas cesser de questionner."_  
>   
> _— Albert Einstein_

#### 👋 Merci !

J'espère vraiment que vous avez aimé mon article. ❤️  
**Suivez-moi sur** [Twitter](https://twitter.com/Estefania_CN_) pour trouver plus d'articles comme celui-ci. 😃