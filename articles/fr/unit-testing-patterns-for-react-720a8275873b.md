---
title: Découvrez ces modèles de tests unitaires adaptés aux débutants pour React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-04T20:56:00.000Z'
originalURL: https://freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JIQ0Vp6gRaNr40h4wDw7GA.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Découvrez ces modèles de tests unitaires adaptés aux débutants pour React
seo_desc: 'By Benedek Gagyi

  There are many frameworks and even more ways to test a React component. But in my
  experience, there are a few patterns that are particularly useful to know, regardless
  of the testing framework you prefer (especially if you are just g...'
---

Par Benedek Gagyi

Il existe de nombreux frameworks et encore plus de façons de tester un composant React. Mais selon mon expérience, il y a quelques modèles particulièrement utiles à connaître, quel que soit le framework de test que vous préférez (surtout si vous commencez tout juste à découvrir React). Voici donc 5 modèles de tests unitaires **agnostiques de framework** pour React.

[Alex Moldovan](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined) a publié un [excellent article](https://medium.com/@alexnm/evolving-patterns-in-react-116140e5fe8f) il y a quelques jours sur les modèles actuels dans React. Ce que j'ai le plus aimé, c'est la manière dont il a abordé le problème. Vous voyez, comme React est si peu prescriptif, un guide de style universel ne conviendrait pas à la communauté (nous avons vu le contraire exact lorsque [John Papa](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined) a publié son guide de style pour AngularJS).

Alex résout ce problème en proposant des modèles utiles pour les débutants et les développeurs plus expérimentés, sans imposer une seule façon de faire.

En continuation de son travail, voici quelques modèles que je trouve utiles lors de l'écriture de tests unitaires pour les composants React.

**Commençons par le début : que dois-je tester ?**

Chaque fois que j'enseigne les bases des tests unitaires, la même question est posée : « Que dois-je tester ? Quels sont les cas que mes tests doivent vérifier ? » Donner une réponse en une phrase qui couvre toutes les situations possibles est assez difficile, mais dans le cas de React, c'est légèrement plus facile.

La plupart des composants avec lesquels vous allez travailler seront sans état, ils peuvent donc être vus simplement comme des fonctions pures : ils reçoivent quelques arguments sous forme de props et retournent un composant rendu. La réponse dans ce cas à la question ci-dessus est donc : « Vérifiez si les différentes combinaisons d'entrées donnent les sorties correctes. » Si vous me demandez, c'est beaucoup plus facile à comprendre et à exécuter !

Faites simplement attention : si vous voyez _this.state_ dans un composant, cela signifie qu'il est avec état. Donc, en plus des choses mentionnées précédemment, vous devrez également écrire des tests contre les mutations d'état.

**#1 : PropTypes**

Dans la plupart des frameworks de test, un avertissement est émis lorsqu'une prop n'est pas fournie ou a un type incorrect. Pour une raison quelconque, beaucoup de gens ignorent ces avertissements et les laissent s'accumuler, rendant les PropTypes inutiles du point de vue des tests.

Un argument en faveur de cette approche est que ces erreurs apparaîtront dans la console du navigateur comme des erreurs à l'exécution, donc il n'y a pas de raison de fournir toutes les props nécessaires dans les tests.

Selon mon expérience, bien que l'énoncé ci-dessus soit vrai, cette méthode présente un inconvénient majeur : certaines erreurs et bugs ne peuvent être trouvées qu'à l'exécution et non en exécutant les tests. Et c'est l'une des raisons pour lesquelles nous écrivons des tests unitaires : pour ne pas avoir à tout vérifier manuellement à l'exécution.

Si vous utilisez un système de typage comme TypeScript ou Flow, cela peut ne pas s'appliquer à vous, car dans ce cas, une erreur sera émise à la compilation. C'est un grand avantage et devrait être pris en compte lors de la décision d'utiliser de tels outils. Merci à [Liran Tal](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined), qui a souligné ce point !

Oublier de définir une prop dans un test unitaire n'est pas un bug dans notre application, alors pourquoi devrions-nous nous soucier de remplir correctement le contrat PropTypes ? La réponse est simple : parce que cela aide à garder les tests sains. Ajouter une prop dans un composant entraînera un avertissement PropType dans les tests, nous avertissant ainsi que nos tests ne couvrent pas tous les cas. Il en va de même pour le changement du type d'une PropType : si un avertissement est émis dans nos tests, cela signifie qu'ils doivent être mis à jour.

Le seul inconvénient de cette méthode est que les props dans le test doivent être maintenues à jour. Ensuite, je vais discuter de la manière que je préfère pour le faire.

**#2 : Props réutilisables**

Lors du test d'un composant React, la plupart de vos cas de test auront besoin d'un certain ensemble de props pour hydrater le composant. La manière la plus simple de le faire est de créer une constante pour chaque cas de test contenant une version des props nécessaires.

Le problème avec cette solution est qu'il est rare que tous les props fournis soient pertinents pour ce cas de test donné. La plupart du temps, ils sont simplement là pour garantir le comportement correct du composant (et pour remplir les PropTypes).

Copier et coller ces props supplémentaires est fastidieux, sujet aux erreurs et entraîne un code gonflé difficile à lire.

Le modèle que je préfère utiliser pour éviter cela repose sur une constante de props globale, et l'étendre si nécessaire en utilisant l'opérateur de propagation.

Ce modèle présente trois avantages principaux :

* pas besoin de copier-coller, le code est plus concis et il n'y a pas de gonflement
* les PropTypes sont toujours correctement remplis
* la lisibilité des tests augmente, puisque les props utilisées par le cas de test donné sont mises en évidence. Il suffit de regarder la définition des props pour voir quel cas est testé. C'est pourquoi j'aime redéfinir une propriété si elle est utilisée dans ce cas de test, même si elle a la même valeur ou une valeur similaire dans l'objet props global.

Une variante de ce modèle utilise également un objet props global. Mais au lieu de toujours créer un nouvel objet pour chaque cas de test, il continue de muter l'objet global pour répondre aux besoins actuels. Je trouve cette solution trop fragile à mon goût. Mais mon plus gros problème avec elle est qu'elle fait dépendre les tests les uns des autres, entraînant de graves problèmes de performance, car ces tests ne peuvent pas être exécutés en parallèle.

**#3 : Rendu superficiel**

Un défi des tests unitaires en général est d'écrire du code qui teste l'unité donnée, mais pas ses dépendances. Tout comme dans n'importe quel écosystème décent, nous avons une tonne d'options lorsque nous voulons simuler ou substituer les dépendances d'un composant React.

L'une de ces bibliothèques utilise une solution si simple, mais élégante que je pense qu'elle devrait faire partie de tous vos tests unitaires React. Cette bibliothèque s'appelle [Enzyme](https://github.com/airbnb/enzyme). Elle est créée par les gens sympas de [AirbnbEng](https://www.freecodecamp.org/news/unit-testing-patterns-for-react-720a8275873b/undefined), et la fonctionnalité dont je parle est le rendu superficiel.

Le rendu superficiel est essentiellement un moyen de rendre un composant React sans rendre ses sous-composants, rendant ainsi le test indépendant de ces sous-composants.

Permettez-moi de vous donner un exemple. Supposons que nous avons un composant appelé _TextAndButton_ qui a un composant enfant appelé _Button_ :

Lorsque _TextAndButton_ est rendu dans un navigateur, son sous-composant est également rendu. Donc, à la fin, il ressemblera à quelque chose comme ceci :

Mais lorsque vous faites un rendu superficiel, les sous-composants restent tels qu'ils ont été écrits :

De cette façon, si _Button_ a des dépendances, elles ne sont pas incluses pour ce rendu. Mieux encore : le composant parent n'a pas besoin de connaître quoi que ce soit sur ses enfants.

Outre les avantages évidents en termes de performance, j'aime cette approche car elle simplifie le modèle mental et clarifie ce qui doit être testé où.

Dans le cas de notre exemple, le test pour _TextAndButton_ doit uniquement vérifier si l'action correcte a été transmise à _Button_. Mais nous ne nous soucions pas de ce qu'il fait réellement, comme afficher le texte correct ou appeler la fonction fournie lorsque nécessaire.

En plus de cela, vos tests seront plus robustes, car la modification d'un composant enfant ne cassera pas les tests écrits pour le parent.

Bien que je puisse imaginer quelques cas où le rendu superficiel n'est pas la meilleure idée, en général, je pense qu'il peut et doit être utilisé pour tous vos tests de composants.

**#4 : Réducteurs et créateurs d'actions Redux**

La philosophie de React est fortement influencée par la programmation fonctionnelle, et il en va de même pour Redux. Ne vous laissez donc pas intimider par tous les noms fantaisistes comme « réducteur » et « créateur d'actions » : ce sont simplement des fonctions régulières et pures avec des objectifs spécifiques.

La popularité de Redux est en partie due à sa simplicité. C'est pourquoi je suis toujours surpris de voir des projets utilisant des modèles de test de réducteurs et de créateurs d'actions surcompliqués.

Selon mon expérience, les tests unitaires des réducteurs et des créateurs d'actions en tant que fonctions sont parfaitement suffisants. Vérifiez s'ils retournent la valeur correcte pour l'entrée donnée (par exemple, un réducteur doit retourner l'objet d'état correct pour l'état et l'action donnés), et c'est tout. Faire plus, comme simuler des actions ou les dispatcher réellement sur un magasin simulé, est excessif — de cette manière, vous finissez par tester Redux lui-même (en plus de votre unité).

Ne me croyez pas sur parole : les [docs officiels de test Redux](https://github.com/reactjs/redux/blob/master/docs/recipes/WritingTests.md) utilisent la même approche simpliste basée sur les fonctions.

D'un autre côté, il n'y a rien de mal à simuler des actions si votre objectif est de créer des tests d'intégration pour vérifier si tout est correctement connecté. Mais il est important de ne pas mélanger les tests unitaires et les tests d'intégration, alors utilisez ce modèle en conséquence.

**#5 : Ne testez pas le DOM**

Selon mon expérience, écrire des tests unitaires fragiles est presque aussi mauvais que d'en écrire aucun. Si un test unitaire échoue alors qu'il ne devrait pas (lorsque le comportement réel de l'unité n'a pas changé), cela prend du temps jusqu'à ce que le développeur corrige la fragilité (coûtant du temps et des efforts supplémentaires) ou, pire encore, le commente simplement.

Il existe de nombreuses façons d'écrire des tests fragiles pour les composants React, mais il y en a une que j'ai vue plusieurs fois et qui est vraiment facile à éviter : écrire des tests contre le DOM.

Pour vous donner un exemple simple, affirmer contre le DOM consisterait à vérifier le nombre d'enfants que le composant donné a. À mon avis, ce n'est pas un test utile, car il ne échouera pas lorsque nous casserons réellement le composant (par exemple en changeant un champ de mot de passe en une entrée de texte régulière). Mais il échouera lorsque nous apporterons des ajustements mineurs et non cassants (comme envelopper un texte dans une balise _span_).

Une autre façon de tester le DOM consiste à interroger certains éléments à l'intérieur de votre composant par leur « héritage », en passant par des chaînes « enfant-de-frère-de-enfant-de ». La manière dont un composant donné est construit en interne ne doit pas être testée car elle change trop souvent et, plus important encore, car elle n'apporte aucune valeur supplémentaire.

Optez plutôt pour des requêtes ciblées, de type CSS, qui ne ciblent que l'élément qui vous intéresse. Encore une fois, une requête comme _div span img_ n'est pas une bonne idée. Optez plutôt pour des requêtes basées sur les classes qui ne dépendent pas de la structure HTML.

**Réflexions finales**

Tester les composants React, surtout avec les derniers outils, est un jeu d'enfant. Ne vous laissez pas décourager par les difficultés initiales et les quelques heures passées à chercher sur Google au début. Vous regagnerez ces heures au centuple si vous continuez à écrire des tests de bonne qualité.

Et n'oubliez pas : vous n'aidez pas seulement votre futur vous-même, mais aussi vos utilisateurs, qui vous seront reconnaissants de recevoir les nouvelles fonctionnalités plus rapidement et sans bugs.