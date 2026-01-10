---
title: Un guide sur le ramasse-miettes en programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-16T19:42:00.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-garbage-collection-in-programming
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dd4740569d1a4ca39d9.jpg
tags:
- name: c programming
  slug: c-programming
- name: Computer Science
  slug: computer-science
seo_title: Un guide sur le ramasse-miettes en programmation
seo_desc: 'What is Garbage Collection?

  In general layman''s terms, Garbage collection (GC) is nothing but collecting or
  gaining memory back which has been allocated to objects but which is not currently
  in use in any part of our program.

  Let''s get into more deta...'
---

## Qu'est-ce que le ramasse-miettes ?

En termes généraux, le ramasse-miettes (GC) n'est rien d'autre que la collecte ou la récupération de mémoire qui a été allouée à des objets mais qui n'est actuellement utilisée dans aucune partie de notre programme.

Entrons dans les détails. Le ramasse-miettes est le processus dans lequel les programmes tentent de libérer de l'espace mémoire qui n'est plus utilisé par des objets.

Le ramasse-miettes est implémenté différemment pour chaque langage. La plupart des langages de programmation de haut niveau ont une forme de ramasse-miettes intégré. Les langages de programmation de bas niveau peuvent ajouter le ramasse-miettes via des bibliothèques.

Comme mentionné ci-dessus, chaque langage de programmation a sa propre façon de réaliser le GC. En C, les développeurs doivent gérer l'allocation et la désallocation de mémoire en utilisant les fonctions malloc() et free(). Mais, dans le cas de C#, les développeurs n'ont pas besoin de gérer le GC et ce n'est pas recommandé non plus.

## Comment se fait l'allocation de mémoire ?

En C#, l'allocation de mémoire des objets se fait dans un tas géré, qui est pris en charge par le CLR (Common Language Runtime). L'allocation de mémoire pour le tas est effectuée via la DLL win32 dans le système d'exploitation et de manière similaire en C.

Mais, en C, les objets sont placés en mémoire partout où il y a de l'espace libre qui correspond à la taille de l'objet. De plus, le mappage mémoire fonctionne sur la base des concepts de liste liée. En C#, l'allocation de mémoire pour le tas se fait de manière linéaire, l'une après l'autre.

Chaque fois qu'un nouvel objet est créé, de la mémoire est allouée dans le tas et le pointeur est déplacé vers l'adresse mémoire suivante. L'allocation de mémoire en C# est plus rapide qu'en C. Cela est dû au fait qu'en C, la mémoire doit rechercher et allouer pour l'objet. Cela prendra donc un peu plus de temps qu'en C#.

## Générations dans le GC de C#

En programmation .net, le tas a trois générations appelées générations 0, 1 et 2. La génération 0 est remplie en premier chaque fois qu'un nouvel objet est créé. Ensuite, le ramasse-miettes s'exécute lorsque la génération 0 est remplie. Les objets nouvellement créés sont placés dans la génération 0.

Lors de l'exécution du ramasse-miettes, tous les objets indésirables sont détruits, et ainsi la mémoire est libérée et compactée. Le GC prend en charge le pointage des pointeurs de la mémoire libérée une fois que le GC a lieu.

Les générations 1 et 2 contiennent des objets qui ont des durées de vie plus longues. Le GC sur les générations 1 et 2 ne se produira pas tant que la génération 0 n'aura pas suffisamment de mémoire à allouer.

Vous ne devriez pas invoquer le GC de manière programmatique. Il est préférable de le laisser se produire naturellement. Le GC est appelé chaque fois que la génération 0 est remplie.

## Avantages et inconvénients du GC

Le ramasse-miettes est un outil qui fait gagner du temps aux programmeurs. Par exemple, il remplace le besoin de fonctions telles que malloc() et free() que l'on trouve en C. Il peut également aider à prévenir les fuites de mémoire.

L'inconvénient du ramasse-miettes est qu'il a un impact négatif sur les performances. Le GC doit régulièrement parcourir le programme, vérifier les références des objets et nettoyer la mémoire. Cela prend des ressources et nécessite souvent que le programme soit mis en pause.

## Quand le faire

Si un objet n'a pas de références (n'est plus accessible), alors il est éligible pour le ramasse-miettes.

Par exemple, dans le code Java ci-dessous, l'objet Thing initialement référencé par 'thing1' a sa seule et unique référence redirigée vers un autre objet dans le tas. Cela signifie qu'il est alors inaccessible et aura sa mémoire désallouée par le ramasse-miettes.

```java
class Useless {
  public static void main (String[] args) {
  Thing thing1 = new Thing();
  Thing thing2 = new Thing();
  thing2 = thing1; // redirige la référence de thing2 vers thing1
                   // aucune référence n'accède à thing2
} }
```

Un exemple de ramasse-miettes est ARC, abréviation de Automatic Reference Counting. Cela est utilisé dans Swift, par exemple. ARC revient à suivre les références à tous les objets qui sont créés. Si le nombre de références tombe à 0, l'objet sera marqué pour désallocation.

#### **Plus d'informations :**

* [https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals) - Pour en savoir plus sur le ramasse-miettes