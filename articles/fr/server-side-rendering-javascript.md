---
title: Rendu côté serveur en JavaScript – SSR vs CSR expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-24T22:12:31.000Z'
originalURL: https://freecodecamp.org/news/server-side-rendering-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-steve-johnson-12939554.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Rendu côté serveur en JavaScript – SSR vs CSR expliqué
seo_desc: "By Scott Gary\nThe concept of Server Side Rendering (SSR) is often misunderstood.\
  \ So my aim in this article is to bring clarity to this process and how it works.\
  \ \nHere's what we'll cover in this guide:\n\nWhat is server side rendering? What\
  \ are its pros..."
---

Par Scott Gary

Le concept de rendu côté serveur (SSR) est souvent mal compris. Mon objectif dans cet article est donc de clarifier ce processus et son fonctionnement. 

Voici ce que nous allons couvrir dans ce guide :

1. Qu'est-ce que le rendu côté serveur ? Quels sont ses avantages et inconvénients par rapport à d'autres méthodes de rendu telles que le rendu côté client (CSR) ?
2. Comment savoir si un site est rendu en utilisant le SSR ?
3. Comment utiliser le SSR, et les choses à garder à l'esprit lors du choix d'un framework SSR.
4. Comment exploiter le SSR pour améliorer les performances.

Nous aborderons chacun de ces points en profondeur, afin qu'à la fin de ce tutoriel, vous ayez une solide compréhension du rendu côté serveur et de sa place dans le monde en constante évolution du développement web.

Nous devrions également examiner deux termes clés que nous utiliserons tout au long de cet article, et ce qu'ils signifient :

1. HTML – Hyper Text Markup Language. Le HTML n'est pas techniquement du code, c'est simplement un langage de balisage qui structure votre contenu sur une page web.
2. DOM – Document Object Model. Le DOM est un modèle réel de votre HTML, composé d'objets. Il dispose d'une interface API qui permet de le modifier, et par conséquent, de modifier le HTML.

Il est important de comprendre la différence entre le HTML et le DOM. Lorsque vous lisez de la documentation, il est facile de devenir confus et de mal interpréter les deux.

## Qu'est-ce que le rendu côté serveur (SSR) ?

Le SSR consiste à rendre le HTML de votre site web sur le serveur. Cela s'oppose au rendu côté client (CSR) où votre site web rend le HTML dans le navigateur en manipulant le DOM avec JavaScript.

## Comment vérifier le SSR

Il arrive que vous souhaitiez vérifier si un site utilise le [rendu côté serveur](https://www.ohmycrawl.com/check-server-side-rendering/). Par exemple, les développeurs et les professionnels du SEO ont souvent besoin de cette information pour aider à résoudre et optimiser les problèmes techniques de SEO. 

Nous allons discuter de quelques techniques couramment utilisées pour déterminer cela. 

### Vérifier le code source de la page

Un moyen facile de déterminer si un site utilise le SSR est de consulter le code source de la page. 

Si le code HTML est complet avec tout le contenu, y compris le corps principal, les images, le texte, etc., le site utilise probablement le SSR. 

En revanche, si le code HTML est minimal, il nécessite alors JavaScript pour rendre le contenu. Dans ce cas, il n'utilise probablement pas le rendu côté serveur.

La première étape consiste à faire un clic droit dans Chrome ou votre navigateur web préféré :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Capto_Capture-2023-04-24_05-33-39_PM.png)
_Clic droit 'afficher le code source de la page'_

Une fois que vous consultez le code source, vous pourrez facilement rechercher des éléments de contenu, par exemple vous pourrez trouver `<p>`, `<h1>`, et ainsi de suite. 

Si vous pouvez les voir ici, il est fort probable qu'ils soient rendus côté serveur :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/rendering-server-side.png)
_Tout ce que vous voyez ici est rendu côté serveur_

### 
Vérifier le cache Google

Un moyen facile de déterminer si votre contenu est rendu côté serveur est de vérifier le cache Google. 

Il suffit de taper l'URL que vous souhaitez inspecter comme ceci avec l'opérateur `site:` dans Google.

Par exemple, ci-dessous, j'ai tapé `site:[https://www.freecodecamp.org/news/](https://www.freecodecamp.org/news/)` puis j'ai sélectionné '_En cache_' :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Capto_Capture-2023-04-24_05-36-42_PM.png)
_tapez votre URL dans Google, puis sélectionnez 'En cache'_

En général, tout ce que vous pouvez voir visuellement est rendu côté serveur. Si c'est rendu avec JavaScript, il est fort probable que vous ne pourrez pas le voir :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Capto_Annotation.png)
_Tout ce que vous voyez ici est probablement rendu côté serveur_

### Astuce bonus : Désactiver JavaScript

Vous pouvez également tester si un site utilise le SSR en désactivant JavaScript sur votre navigateur. Si le contenu du site web est toujours visible sans JavaScript, il utilise probablement le SSR. Si le site web apparaît vide, il n'utilise pas le SSR.

Dans cet exemple, nous pouvons clairement voir qu'Airbnb n'utilise pas le rendu côté serveur sur sa page d'accueil :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/visual-representation.png)

Et voici une assez bonne représentation visuelle si vous ne comprenez pas encore tout à fait le concept :

%[https://www.youtube.com/watch?v=_ojqh9G4c28]

## SSR vs CSR 

Décortiquons les différents processus de rendu côté client et côté serveur, suivis des avantages et inconvénients de chacun.

### Comment fonctionne le SSR

1. Une requête HTTP est envoyée au serveur.
2. Le serveur reçoit la requête et traite tout (ou la plupart) du code nécessaire sur-le-champ.
3. Le résultat final est une page HTML entièrement formée et facilement consommable qui peut être envoyée au navigateur du client via la réponse du serveur.

C'est un concept assez simple en surface, mais les choses peuvent devenir assez compliquées lorsque l'on considère comment inclure des composants interactifs sur le client qui nécessitent JavaScript. Nous aborderons cela plus tard – d'abord, voyons ce qui se passe lorsque vous demandez une application web CSR.

### Comment fonctionne le CSR

1. Une requête HTTP est envoyée au serveur.
2. Le serveur reçoit la requête et répond en envoyant une coquille HTML vide au client ainsi qu'un ensemble de JavaScript.
3. Le client reçoit la coquille HTML vide et procède au traitement de tout le JavaScript.
4. Le JavaScript modifie extensivement le DOM, ce qui rend le HTML final pour l'utilisateur final.

Pour simplifier, le rendu côté client est lorsque votre site web ou votre application web se rend en HTML dans le navigateur en traitant JavaScript, plutôt que sur le serveur en utilisant le framework backend de votre choix.

Ensuite, nous examinerons les forces et les faiblesses de chaque style de rendu.

## Avantages du SSR

Le principal avantage du rendu côté serveur est la vitesse de chargement des pages. La vitesse de chargement des pages est une métrique importante pour l'expérience utilisateur, et par conséquent un aspect important du SEO technique. Google veut également consommer les pages rapidement.

Lorsque une page est rendue en HTML sur le serveur, tout le travail lourd est pris en charge. Pour cette raison, lorsque la réponse arrive dans le navigateur du client, il n'y a pas beaucoup de travail restant pour le navigateur pour afficher la page. Elle est prête à l'emploi dès sa livraison.

## Inconvénients du SSR

Il y a de nombreuses raisons pour lesquelles la plupart des frameworks JavaScript ont décidé d'inclure le SSR comme option de rendu dans leurs frameworks. Mais il y a quelques inconvénients au SSR.

Les designers veulent que les pages soient interactives, et lorsqu'une page est rendue en HTML pur pour le client, cela laisse une expérience utilisateur assez fade. Alors, comment rendre ces pages interactives tout en préservant tous les grands avantages du rendu côté serveur ? 

La réponse est une couche supplémentaire de complexité qui porte de nombreux noms, mais elle est plus communément connue sous le nom de code-splitting et d'hydratation.

### Code Splitting et Hydratation

Pour qu'une page soit interactive, nous avons besoin que JavaScript soit envoyé au client. Les frameworks SSR tels que Next.js et Astro nous permettent de construire une page HTML uniquement sur le serveur qui peut être envoyée rapidement au client, tout en permettant l'envoi de bundles spécifiques de JavaScript au client après le chargement initial du HTML.

Dans le monde React, ce processus est connu sous le nom d'hydratation. Le code est divisé en morceaux gérables qui peuvent ensuite être demandés au besoin et injectés, ou _hydratés_, dans la page client pour ajouter de l'interactivité et de la fonctionnalité.

Vous vous demandez peut-être pourquoi c'est un "inconvénient". Eh bien, l'idée elle-même n'est pas l'inconvénient, c'est le défi technique qui l'accompagne. L'Isomorphic React et d'autres technologies utilisées pour atteindre cet objectif sont notoirement complexes, et il faut une connaissance intime d'un framework pour programmer ces sites efficacement.

## Avantages du CSR

Les avantages du rendu côté client sont essentiellement le contraire du rendu côté serveur. Nous avons une excellente disponibilité pour les fonctionnalités interactives, car la page HTML entière est construite en utilisant JavaScript sur le client. En fait, l'ensemble du framework CSR est souvent envoyé au client dans un environnement de rendu purement côté client.

Pour cette raison, une fois la page initialement chargée, tout est très réactif pour l'utilisateur final. C'est parce que tout, y compris le code pour toutes les autres pages, est chargé avec le chargement initial de la page.

Du point de vue d'un développeur, le rendu côté client est une excellente expérience. La complexité de partager la charge de travail avec le serveur est inexistante, et nous pouvons nous concentrer sur la construction de composants interactifs réutilisables qui permettent un processus de développement rationalisé.

## Inconvénients du CSR

Peu après l'explosion des frameworks CSR, les spécialistes du SEO ont commencé à réaliser que Google et d'autres moteurs de recherche ne font pas un bon travail d'indexation de ces pages. Le résumé était clair : le CSR pur est mauvais pour le SEO.

La vitesse de chargement initial de la page est le principal inconvénient ici. Lorsque vous utilisez le CSR, la page est initialement envoyée au client sous forme de coquille HTML vide sans contenu. Cette coquille vide est souvent ce que Google et d'autres moteurs de recherche voient, ce qui n'est pas souhaitable pour des raisons évidentes.

Le JavaScript construira la page assez rapidement, mais en pratique, la plupart des moteurs de recherche ont encore du mal à indexer le contenu après que la manipulation du DOM a été terminée et que le HTML est rendu.

Dans le pire des cas, le temps de chargement d'une application de rendu côté client mal construite peut même commencer à affecter négativement l'expérience utilisateur, ce qui est la pire des erreurs.

## Quand utiliser le SSR vs CSR

Sur la base de ce que nous avons appris jusqu'à présent, il n'est pas surprenant que le rendu côté serveur soit un excellent choix lorsque le chargement initial de la page est une priorité et que le SEO technique est important. Mais ce n'est pas le seul facteur motivant cette considération.

Lorsque un site contient une tonne de données dynamiques et fréquemment changeantes, le rendu côté serveur permet aux développeurs de partager la charge de travail de récupération de contenu.

Lorsque vous utilisez une application purement côté client pour des sites intensifs en données, cela nécessite de nombreux appels du client au serveur pour récupérer les données. Cela peut entraîner un ralentissement des pages et un chargement lent, ce qui peut entraîner une mauvaise expérience utilisateur. 

Le rendu côté serveur résout ce problème en permettant au serveur de pré-récupérer et de pré-rendre les données nécessaires avant de les envoyer au client.

Rappelez-vous, la plupart des implémentations de rendu côté serveur ne sont pas _purement_ SSR, elles se contentent de faire le travail lourd. Les développeurs ont toujours la possibilité d'envoyer des bundles spécifiques et petits de JavaScript après coup qui ajoutent de l'interactivité et même de la récupération de données, partageant ainsi la charge de récupération de données avec le serveur.

## Comment exploiter le SSR pour votre projet

Sauf si vous essayez de construire un framework à vous seul, le SSR n'est pas quelque chose que vous souhaitez implémenter à partir de zéro. Heureusement, il existe de nombreux frameworks et bibliothèques qui peuvent vous aider à exploiter le SSR dans votre projet. 

Une option populaire est [Next.js pour le SEO](https://www.freecodecamp.org/news/nextjs-seo/), un framework React qui fournit un support intégré pour le SSR, ainsi que le code-splitting et d'autres optimisations de performance.

Lorsque vous exploitez le rendu côté serveur de manière à maximiser ses avantages de performance, vous devez être conscient de l'impact de la distribution de la récupération de données de votre application. Les charges de données lourdes peuvent ralentir le processus SSR et affecter les performances de votre application, ce qui est l'une des raisons pour lesquelles les développeurs récupèrent également les données du client.

En ce qui concerne la récupération et le traitement des données côté serveur, vous pouvez également commencer à encourir des frais assez élevés de la part de votre fournisseur d'hébergement. Gardez un œil attentif sur cela si les exigences de votre projet incluent une abondance de données externes.

## Aperçu et conclusions

Le rendu côté serveur (SSR) peut être un outil puissant pour améliorer les performances et l'expérience utilisateur des applications web. En rendant le HTML sur le serveur avant de l'envoyer au client, le SSR peut réduire considérablement le temps nécessaire pour afficher une page web, ce qui se traduit par des temps de chargement plus rapides et une meilleure expérience utilisateur.

Lorsque le SSR est utilisé correctement, les avantages techniques se traduisent généralement par un meilleur SEO, car il fournit aux moteurs de recherche des documents HTML facilement explorables. Si vous souhaitez en savoir plus sur le rendu côté serveur, consultez [OhMyCrawl](https://ohmycrawl.com/) pour en apprendre davantage.