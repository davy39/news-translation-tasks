---
title: 'Programmation C# : Une Introduction pour Débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T21:55:00.000Z'
originalURL: https://freecodecamp.org/news/csharp
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc1740569d1a4ca3974.jpg
tags:
- name: C
  slug: c
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
seo_title: 'Programmation C# : Une Introduction pour Débutants'
seo_desc: 'C Sharp, more commonly referred to as “C#”, is a general-purpose, object-oriented
  programming language. C# was developed by Anders Hejlsberg and his development team
  at Microsoft and is currently on version 7.0.

  C# has its roots in the family of C la...'
---

C Sharp, plus communément appelé « C# », est un langage de programmation généraliste et orienté objet. C# a été développé par Anders Hejlsberg et son équipe de développement chez Microsoft et est actuellement en version 7.0.

C# a ses racines dans la famille des langages C. Il hérite de la plupart de ses fonctionnalités de C, C++ et Java. Pour cette raison, les programmeurs familiers avec ces langages peuvent être en mesure de se mettre à niveau avec C# en un temps plus court.

C# est un langage orienté objet qui offre un soutien pour la programmation orientée composant et fonctionnelle.

### Classes et Objets

Les classes nous permettent de modéliser des objets du quotidien dans le monde qui nous entoure dans le logiciel. Vous pouvez créer des classes personnalisées pour représenter presque tout. Tout comme un nom est une personne, un lieu ou une chose dans le langage, une classe représente également des objets.

Lorsque vous écrivez du code C#, c'est généralement parce que vous avez besoin d'un programme qui _fait_ quelque chose d'utile.

Dans le cas d'un besoin commercial, vous suivez les exigences de l'entreprise. Supposons que votre entreprise vous demande une base de données électronique de livres. Ils doivent pouvoir stocker les titres de livres, les auteurs, calculer des statistiques, comme le nombre d'emprunts dans un mois donné, ou une moyenne mensuelle.

Les exigences décrivent le programme qui doit être développé. Comment écrire un programme pour les exigences données ?

Généralement, nous utilisons des classes pour créer des abstractions pour les différents noms avec lesquels nous devons travailler. Un nom tel qu'un livre, un auteur ou un titre.

Un concept important en C# est que la définition de la classe est utilisée pour créer des instances d'objets. Vous pouvez le considérer comme un plan pour créer des instances d'objets. La définition de la classe permet la création d'objets qui stockent une référence à cet objet. Par exemple, supposons que nous voulons créer un nouvel objet livre. La ligne de code ressemble à ceci :

```c
Book book = new Book();
```

Cela crée un nouvel objet livre que nous pouvons utiliser pour manipuler des données et les stocker dans une base de données. La variable, book, est en fait un type de référence de Book (avec un B majuscule). Nous pouvons ensuite utiliser les méthodes disponibles dans la définition de la classe avec cette variable, book, telles que `AddTitle()`, `AddAuthor()`, et ainsi de suite.

#### **Fonctionnalités de C# :**

1. Collecte automatique des déchets
2. Gestion des exceptions
3. Sécurité des types
4. Versioning
5. Délégations
6. Propriétés
7. LINQ (Language-Integrated Query) et Expressions Lambda
8. Génériques
9. Indexeurs
10. Multithreading

#### **Nouvelles Fonctionnalités Ajoutées dans C# 7.0 :**

1. Déconstructeurs
2. Nouvelle syntaxe pour travailler avec les Tuples
3. Correspondance de motifs avec les Expressions Is
4. Fonctions Locales
5. Retour par Référence
6. Variables Out
7. Améliorations littérales
8. Types de Retour Async Généralisés
9. Plus de Membres à Corps d'Expression
10. Expressions Throw
11. Type Record
12. Minimisation de OUT
13. Type de référence non-'NULL'

#### **Applications ASP.NET et .NET**

Le langage C# est également utilisé avec le framework ASP.NET, développé par Microsoft Corp., spécifiquement pour créer des applications web indépendantes de la machine et du navigateur.

Le framework .NET plus large, également développé par Microsoft, est utilisé pour créer d'autres types d'applications telles que les applications de bureau, mobiles, serveur et réseau. Le framework .NET inclut les bibliothèques de classes de base .NET (BCL), ASP.NET, ADO.NET, Windows Forms, Windows Presentation Foundation (WPF) et les bibliothèques eXtensible Markup Language (XML).