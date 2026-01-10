---
title: React est-il une bibliothèque ou un framework ? Voici pourquoi cela compte
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-12T21:29:45.000Z'
originalURL: https://freecodecamp.org/news/is-react-a-library-or-a-framework
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/is-react-a-library-or-framework.png
tags:
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: React est-il une bibliothèque ou un framework ? Voici pourquoi cela compte
seo_desc: 'Developers have spent a great deal of time talking about what React is.
  But they have left out why this topic matters so greatly for anyone who builds React
  applications.

  The answer to this question is essential for any React developer, regardless of...'
---

Les développeurs ont passé beaucoup de temps à discuter de ce qu'est React. Mais ils ont omis d'expliquer pourquoi ce sujet est si important pour quiconque construit des applications React.

La réponse à cette question est essentielle pour tout développeur React, quel que soit son niveau de compétence. Cela indique ce qu'ils doivent savoir et comment ils doivent travailler pour développer une application React.

Que vous soyez un développeur React débutant ou avancé, j'espère que cette analyse réfléchie améliorera votre propre processus de développement lors de la construction de votre prochain projet React.

## Pourquoi React est une bibliothèque et non un framework ?

React a été conçu pour construire des applications web complètes. Par conséquent, il est souvent comparé à d'autres outils que les développeurs utilisent pour construire des applications, comme Angular, Vue et Svelte. 

React est écrit en JavaScript et est utilisé pour créer de meilleures applications JavaScript. Nous référons spécifiquement à React comme une **bibliothèque**. 

*Mais qu'est-ce qui fait de React une bibliothèque et non un framework ?* 

La raison devient claire lorsque nous examinons d'autres outils similaires utilisés pour créer des applications web complètes.

Prenons l'exemple d'un projet comme Angular, qui partage le même objectif que React (créer des applications web monopage). Ce qui le distingue, c'est le fait que lorsque vous configurez un projet Angular, il est initialisé avec presque tout ce dont vous aurez besoin pour créer une application complète à grande échelle. 

> De nombreux développeurs aiment référer aux frameworks ou solutions similaires comme ayant des "batteries incluses". 

Les frameworks sont un choix courant pour les entreprises et quiconque souhaite créer des applications JavaScript d'entreprise, car ils incluent des ressources qu'une application à grande échelle pourrait probablement nécessiter. Cela inclut des outils intégrés pour des tâches courantes comme la création de formulaires, l'exécution de tests automatisés, la réalisation de requêtes réseau, et bien plus encore.

En bref, tout ce dont vous avez besoin pour créer une application complète est inclus dans votre projet Angular lorsqu'il est généré. Mais ce n'est pas le cas avec React.

## React est fondamentalement "non opinionné"

Bien que des outils populaires aient émergé comme Create React App, qui permettent de créer un projet React complet en une seule commande, React est souvent qualifié de "non opinionné". 

*Que signifie le fait que React soit non opinionné ?*

Les bibliothèques React et React DOM nous donnent les moyens de construire une interface utilisateur avec la syntaxe JSX, ainsi que des outils puissants de gestion d'état via les hooks, entre autres.

Cependant, React lui-même n'inclut pas beaucoup des bibliothèques spécifiques à React dont vous aurez besoin pour la plupart des projets. Angular et Vue, en comparaison, incluent beaucoup plus d'outils tous regroupés dans le package principal lui-même.

De nombreux développeurs considèrent cette discussion sur ce qui est et n'est pas une bibliothèque comme triviale. Mais elle a des conséquences réelles pour notre processus de développement. En d'autres termes, parce que React est une bibliothèque et non un framework, **devenir un développeur React compétent implique d'avoir une bonne connaissance des bibliothèques React tierces**.

## Puisque React est une bibliothèque, vous devez choisir les outils vous-même

Cela signifie que, pour construire des applications React complètes, vous devrez choisir ces packages et outils vous-même. 

Voici quelques exemples de décisions que je dois souvent prendre lorsque je construis une application React moi-même : 

Pour une bibliothèque de formulaires, je dois décider si je veux utiliser le package React Hook Form ou Formik. Ce sont deux bibliothèques de formulaires spécifiques à React pour ajouter des fonctionnalités importantes à nos formulaires comme la validation.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/react-form-libraries.jpg)

Pour tester mon application React, je pourrais utiliser soit React Testing Library, Jest, ou une combinaison des deux.

Pour faire des requêtes réseau, je pourrais devoir choisir entre l'API Fetch et Axios. Je pourrais également devoir décider si je veux ajouter une bibliothèque supplémentaire pour faciliter la gestion de l'état du serveur, comme React Query ou SWR.

## Les outils que vous choisissez dépendent de votre application et de votre connaissance de ceux-ci

Cette question de savoir si React est une bibliothèque ou un framework est importante car tout développeur React doit savoir quelles sont ses options et quel choix faire en fonction du type d'application React qu'il construit.

Si vous construisez une application sans beaucoup de formulaires, vous n'aurez peut-être pas besoin d'une bibliothèque de formulaires du tout. Si vous êtes plus à l'aise avec l'API Fetch, vous pourriez l'utiliser plutôt que quelque chose comme Axios. 

Cela dépend vraiment non seulement des exigences de l'application, mais aussi de vos préférences en tant que développeur. C'est probablement un avantage que React a en tant que bibliothèque et pourquoi je crois qu'il est très populaire parmi les nouveaux développeurs. Il ne vous enferme pas dans un choix ou ne vous oblige à utiliser des bibliothèques spécifiques autres que React lui-même. 

Vous êtes en mesure de prendre vos propres décisions, et vous avez plus de liberté globale, en tant que développeur. 

Cela dit, même si React n'est pas un framework, cela ne diminue pas sa présence dans le domaine corporatif. Il est toujours utilisé pour construire des applications complexes et impressionnantes de toutes sortes. Il existe de nombreuses listes d'applications React à grande échelle que les entreprises ont créées et que vous utilisez probablement au quotidien.

## Vous devez vous tenir au courant des bibliothèques émergentes

Si nous parlions de quelle bibliothèque de formulaires choisir il y a deux ans, j'aurais probablement inclus Redux Form. En ce qui concerne une bibliothèque de récupération de données, je n'aurais pas pu mentionner React Query ou SWR, car elles n'avaient pas encore été créées (ou n'avaient pas encore gagné beaucoup de traction), jusqu'à l'année dernière environ.

Parce que les applications React dépendent souvent de bibliothèques tierces, de nouvelles bibliothèques apparaissent qui améliorent les anciennes. Les développeurs individuels et les équipes passent à différents outils pour accomplir le travail et l'écosystème change dans son ensemble.

Que cela nous plaise ou non, le fait que React soit une bibliothèque et non un framework implique un large réseau changeant d'autres bibliothèques dont nous devons être conscients pour construire nos projets. Certaines d'entre elles peuvent tomber en désuétude et être remplacées par d'autres ou peuvent devenir obsolètes et ne plus être supportées en tant que projets open-source. 

En bref, le fait que React soit une bibliothèque peut nous obliger à prêter plus d'attention à ce qui se passe *autour* de React, par rapport à si c'était un framework.

## Vous souhaitez que React soit un framework ? Il en existe beaucoup !

Il est intéressant de noter qu'il existe des frameworks basés sur React. 

Bien que React lui-même soit juste une bibliothèque, de nombreux frameworks basés sur React ont vu le jour ces dernières années pour fournir aux développeurs un ensemble plus puissant d'outils intégrés. Ceux-ci vous permettent de construire des projets plus rapidement sans avoir besoin de tant de bibliothèques tierces. 

Parmi les plus populaires de ces frameworks, on trouve Next.js, Gatsby et Redwood.js, tous utilisés pour créer des applications React dynamiques et statiques à grande échelle.

C'est, à mon avis, le grand avantage des frameworks – vous n'avez pas à faire autant de choix tout au long du processus de développement.

## Utilisez la flexibilité de React à votre avantage

Sachez qu'à l'avenir, il existe un écosystème robuste de bibliothèques axées sur React que vous pouvez ajouter à votre projet React pour atteindre ce que vous recherchez, des tâches les plus générales aux plus spécifiques. 

Cela est dû à la popularité et à l'utilisation généralisée de React. Mais notez également, surtout si vous venez d'un framework opinionné comme Angular ou Vue, qu'il existe de nombreux frameworks basés sur React sur lesquels vous pouvez vous appuyer et apprendre pour construire des applications tout aussi fonctionnelles et riches en fonctionnalités.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*