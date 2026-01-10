---
title: Uno - Une Plateforme pour les Gouvernantes Toutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-08T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/uno-platform
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/UnoLogoLargeCut-1.png
tags:
- name: C
  slug: c
- name: mobile app development
  slug: mobile-app-development
seo_title: Uno - Une Plateforme pour les Gouvernantes Toutes
seo_desc: "By Kenzie Whalen\nFirst, we should start off with what Uno is and why you\
  \ should care. \nAs stated on their website, Uno is \"The only platform for building\
  \ native mobile, desktop and WebAssembly apps with C#, XAML from a single codebase.\
  \ Open source an..."
---

Par Kenzie Whalen

Tout d'abord, nous devrions commencer par ce qu'est Uno et pourquoi vous devriez vous en soucier. 

Comme indiqué sur leur [site web](https://platform.uno), Uno est "La seule plateforme pour construire des applications mobiles natives, de bureau et WebAssembly avec C#, XAML à partir d'une seule base de code. Open source et professionnellement supporté."

## Que signifie cela ?

Eh bien, si vous avez de l'expérience (ou non) dans la construction d'une application mobile et d'une application web ultérieure, vous avez essentiellement dû construire les deux séparément, en dehors du partage potentiel de données via une API. 

Avant Xamarin, vous auriez même dû construire les applications iOS et Android séparément en utilisant différents langages (Swift/Objective-C et Java/Kotlin respectivement). Uno introduit un moyen de construire pour iOS, Android, Web et UWP en utilisant une logique et une UI partagées. 

C'est énorme.

Partager la logique entre les plateformes a été la partie "facile" pour les développeurs. Partager l'UI, cependant, ne l'est pas. Il y a une énorme différence d'UI entre Android et iOS et des différences encore plus grandes entre le web et le mobile. Xamarin.Forms nous permet de partager l'UI pour Android et iOS, mais nous étions toujours seuls pour le web. 

Uno vous permet d'écrire l'UI une fois, puis, en utilisant des contrôles natifs, déploie l'apparence et le comportement natifs de l'UI sur chacune de vos plateformes. Cela signifie que vous écrivez le même code pour un bouton, quelle que soit la plateforme pour laquelle le bouton est destiné, et l'utilisateur verra le bouton natif pour sa plateforme.

## Comment cela fonctionne-t-il ?

La plateforme Uno fonctionne différemment selon ce que vous construisez. 

L'UI spécifique à la plateforme est créée en prenant l'arborescence visuelle et en la rendant dans ce que la plateforme supporte :

**iOS** _-_ UI Kit

**Android** _-_ ViewGroups et Views

**Web** _-_ Contrôles natifs

La logique est également déployée différemment pour chaque plateforme.

Lors de la construction d'une application UWP, Uno fonctionne sur UWP et WinUI. Lors de la construction d'applications Android et iOS, Uno fonctionne sur la pile native Xamarin. Enfin, lorsque vous construisez une application Web, Uno fonctionne sur WebAssembly. Les applications mobiles et les applications web fonctionnent toutes avec le runtime Mono. Lorsque tout est assemblé, cela ressemble un peu à ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/unodiagram.png)
_Architecture de haut niveau de la plateforme Uno_

Cela semble bien, mais que se passe-t-il vraiment sous le capot ?

## Décomposons cela :

**Android et iOS**

1. Vous écrivez votre code C# et XAML dans Visual Studio
2. Uno prend le code et vous permet d'ajouter des bibliothèques ou outils spécifiques à Xamarin 
3. Le runtime Mono exécute le code C#

Ce processus est essentiellement le même que Xamarin régulier. La grande différence entre Xamarin et Uno vient avec la capacité à exécuter la même UI sur le Web.

**Applications Web** - 

1. Vous réutilisez à la fois votre **logique** et votre **UI** que vous avez écrites pour vos applications mobiles.
2. Uno utilise le _Web Assembly Bootstrapper_ pour prendre n'importe quelle bibliothèque .NET standard et exécuter ces fichiers dans la console JavaScript. 
3. Le runtime Mono exécute ensuite le code

La capacité d'Uno à utiliser Web Assembly (ce qui vous permet d'écrire votre code en C# et non en JavaScript) est ce qui rend Uno si unique. 

**UWP** -

1. Vous réutilisez à la fois votre **logique** et votre **UI** que vous avez écrites pour vos applications mobiles et vos applications Web Assembly.
2. Votre code est exécuté via l'interface utilisateur Windows qui n'a pas besoin du runtime Mono pour s'exécuter.

La grande différence ici est que les applications UWP ont déjà les espaces de noms Windows et n'ont pas besoin de référencer Uno.UI. L'avantage qu'Uno offre ici est la capacité de réutiliser le code que vous avez déjà écrit pour le mobile et le web.

Maintenant que nous avons une idée de comment cette beauté fonctionne, écrivons un peu de code !

Pour commencer avec Uno, suivez leurs instructions [ici](https://platform.uno/docs/articles/get-started.html).

Lorsque vous créez votre solution Uno dans Visual Studio, il y a une sensation similaire à celle lorsque vous créez une solution Xamarin.Forms en raison des différents projets créés pour vous. Voici un aperçu des projets qui sont créés automatiquement :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/2019-10-01_1528.png)

Comme vous le verriez dans un projet Xamarin.Forms, il y a des projets séparés pour chaque plateforme et un seul projet partagé. Les projets Droid, iOS, UWP et Wasm sont tous les mêmes que si vous aviez créé une application vide pour chacun, la seule différence étant les références à l'UI Uno. La magie opère dans le projet _Shared_.

Similaire au projet _Shared_ dans Xamarin.Forms, c'est ici que vous écrirez toute votre logique et votre UI partagées. Uno offre un support pour le [MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel), un modèle de conception que de nombreux développeurs connaissent et avec lequel ils sont à l'aise. 

## Alors, à quoi ressemble un produit fini ?

En utilisant l'exemple d'application "Todo" fourni par Uno [ici](https://github.com/unoplatform/workshops/blob/master/uno-bootcamp/modules/99-Ship-your-app/TodoApp.sln), voici des exemples de chacune des quatre plateformes.

iOS

![Image](https://www.freecodecamp.org/news/content/images/2019/10/iOS.png)

Android

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Android.png)

Web

![Image](https://www.freecodecamp.org/news/content/images/2019/10/WASM-1.png)

UWP

![Image](https://www.freecodecamp.org/news/content/images/2019/10/UWP.png)

Ces projets utilisent tous la logique et l'UI du projet partagé. Codez une fois, quatre applications. 

## Parlons débogage. 

Le débogage dans Uno peut être un peu différent selon la plateforme que vous essayez de déboguer. 

**Android et iOS** - Pour le mobile, vous utiliserez le même débogueur Mono auquel vous êtes habitué dans Visual Studio, avec accès à tous vos points d'arrêt, changements de valeur, etc. 

**Web** - Actuellement, il n'y a de support que pour le débogage Chromium, ce qui signifie Chrome et Edge.

**UWP** - Ici, les outils proviennent des studios .NET qui ne sont pas aussi efficaces avec le runtime Mono. 

**Vous voulez essayer Uno mais ne voulez pas passer par les étapes pour vous installer via Visual Studio ?**

Alors consultez leur [playground](https://playground.platform.uno/#wasm-start) !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/2019-10-02_1518.png)

Le Uno Playground est un moyen amusant et facile de voir comment différents éléments sont rendus sur différentes plateformes. Ils rendent rapide et facile l'essai de nouveaux styles et est idéal pour les débutants et les tutoriels.

## Quelles sont les fonctionnalités futures auxquelles nous pouvons nous attendre ?

1. Support pour MacOS ou Linux.
2. Plus de fonctionnalités de l'API UWP
3. Support pour les montres intelligentes

La vraie beauté d'Uno est qu'il englobe ce que nous, en tant que développeurs, devrions tous nous efforcer d'accomplir - construire sur les accomplissements des autres. Nous n'avons pas besoin de réinventer la roue, la vraie innovation se produit lorsque vous vous tenez sur les épaules des géants et que nous progressons tous ensemble. 

Bon codage. 

Pour plus de leçons et de conseils sur Uno, consultez mon [blog](https://knzwhalen.com).