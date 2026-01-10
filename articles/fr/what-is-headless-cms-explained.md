---
title: Headless CMS Expliqué – Qu'est-ce que c'est et quand l'utiliser
subtitle: ''
author: Daniel Madalitso Phiri
co_authors: []
series: null
date: '2021-07-27T17:53:47.000Z'
originalURL: https://freecodecamp.org/news/what-is-headless-cms-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/siora-photography-hgFY1mZY-Y0-unsplash-1.jpg
tags:
- name: cms
  slug: cms
- name: headless cms
  slug: headless-cms
seo_title: Headless CMS Expliqué – Qu'est-ce que c'est et quand l'utiliser
seo_desc: 'By Daniel Madalitso Phiri

  CMSs are pretty hard to ignore because they''re everywhere on the internet. WordPress,
  for example, powers nearly 40% of the internet today.

  In this article, we''ll cover what CMSs are and why you should care about them.
  I''ll ...'
---

Par Daniel Madalitso Phiri

Les CMS sont assez difficiles à ignorer car ils sont partout sur Internet. WordPress, par exemple, alimente près de [40 % d'Internet](https://kinsta.com/wordpress-market-share/) aujourd'hui.

Dans cet article, nous allons couvrir ce que sont les CMS et pourquoi vous devriez vous en soucier. Je vais également vous présenter un nouveau type de CMS qui semble être partout en ce moment – le Headless CMS. Et nous allons faire tout cela avec une histoire !

La vie a une façon amusante de vous faire essayer des choses. Et après des années à ignorer les CMS en tant que technologie, en milieu d'année 2020, j'ai obtenu un emploi chez [Strapi](https://strapi.io), un outil de CMS headless. Depuis lors, j'ai développé une assez bonne compréhension de ce que ces outils font – alors plongeons-nous dedans.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/ezgif.com-gif-maker-2-.png align="left")

## Qu'est-ce qu'un CMS ?

Un système de gestion de contenu (CMS) est un outil qui aide les utilisateurs à créer, gérer et modifier du contenu numérique.

Dans cet article, cependant, je n'entrerai pas dans les détails. Au lieu de cela, si vous souhaitez en savoir plus, vous pouvez consulter [un article que j'ai écrit](https://strapi.io/blog/frontend-developers-headless-cms) qui approfondit les différents types de CMS.

## Qu'est-ce qu'un Headless CMS ?

Un CMS headless a un back-end où le contenu est préparé – et c'est tout. Le contenu et ses données ne sont accessibles que via des appels faits à l'API, qu'il s'agisse de REST ou de GraphQL.

J'aime utiliser ce diagramme pour illustrer comment fonctionne le Headless, alors espérons qu'il donne une image plus claire.

![Image](https://lh3.googleusercontent.com/zPdxhP33Y_kqX1SY-KXDq0Ma1IiJv15urJ_PVuiogvtI86tCa_A2qMJ0L2UqFD_U_MmTy0VHED1Oz9w5uumNipKSBzwmHYkHRrgXrdrLU0PNg9nvhUQC28Hy09H9Wrn5iiBep95U align="left")

*Architectures monolithiques vs découplées vs headless*

Outre la diffusion de contenu sur plusieurs plateformes, il existe quelques autres raisons pour lesquelles vous pourriez vouloir utiliser un CMS Headless.

### Vous ne voulez pas renoncer à la flexibilité du développeur

Adopter une architecture Headless par défaut signifie que vous avez la flexibilité de choisir un outil de front-end de votre choix. Et pour de nombreux développeurs, c'est un avantage critique.

### Vous avez besoin d'une solution de contenu sécurisée

Le découplage du front-end et du back-end rend les attaques ciblées beaucoup plus difficiles. C'est quelque chose avec lequel certains CMS traditionnels luttent encore aujourd'hui.

### Vous voulez rendre votre stack technologique future-proof

Passer au headless signifie également que vous êtes moins dépendant d'une seule solution pour un front-end. Si vous devez passer à un front-end plus moderne ou ajouter un nouveau front-end, le headless rend cela beaucoup plus facile.

### Vous devez créer des expériences personnalisées et personnalisables

Cela devient un avantage vraiment important pour les CMS headless pour de nombreuses organisations.

Avec le headless, vous avez l'opportunité de personnaliser différentes expériences pour différentes plateformes, le tout à partir d'une seule source de contenu.

## Comment je me suis lancé dans les CMS Headless

J'aime vraiment GraphQL, et c'est ainsi que j'ai commencé avec Strapi. Travailler pour un CMS, c'était comme plonger tête la première dans cet écosystème. Je pensais comprendre les CMS Headless car pour moi, ils étaient "données, API, frontend" et c'est ainsi que je les concevais.

Eh bien, nous utilisons ces outils pour construire nos front-ends, mais nous oublions souvent le côté gestion de contenu lorsque nous pensons à construire un front-end de cette manière. Et ce n'est que lorsque j'ai commencé à travailler avec Strapi que j'ai reconnu mon hypothèse.

"Gestion de contenu" semble un peu ennuyeux, n'est-ce pas ? Et CMS ? "Ewww, pourquoi voudrais-je utiliser un tel outil ?" Je sais ! Moi aussi, mais écoutez-moi. Les CMS sont en réalité assez utiles. Alors parlons de la manière dont un CMS pourrait vous aider.

## Pourquoi avez-vous besoin d'un CMS Headless ?

Pour commencer, il ne faut pas sous-estimer le rôle du contenu dans le monde d'aujourd'hui. Le contenu est partout et se manifeste sous tant de formes à travers le texte, l'audio, la vidéo, et plus encore.

Pendant longtemps, les ordinateurs et les navigateurs étaient les principaux outils de consommation de contenu. Nous lisions des blogs, regardions des vidéos YouTube et écoutions des podcasts sur nos ordinateurs personnels.

Progressivement, nos ordinateurs sont devenus plus petits et moins évidents. Le contenu sous ses nombreuses formes a commencé à apparaître tout autour de nous. Il s'est affiché sur les téléphones mobiles, sur nos téléviseurs intelligents, dans nos voitures, dans nos assistants virtuels et nos appareils portables.

La manière dont les gens consommaient le contenu a changé, et il en a été de même pour la manière dont nous devions construire des expériences de consommation de contenu.

### Comment le CMS Headless aide-t-il ?

Traditionnellement, les CMS étaient des monolithes avec le front-end et le back-end étroitement couplés. Le contenu que vous ajoutiez dans le back-end du CMS n'apparaissait que sur le front-end auquel il était couplé – pensez à WordPress et Drupal.

Cela s'est avéré inefficace car les développeurs avaient besoin d'une meilleure façon de construire et de s'adapter à ce nouveau comportement des consommateurs.

La solution ? Arracher la tête d'un CMS traditionnel et rendre possible la diffusion de contenu de votre back-end vers plusieurs plateformes. C'est ainsi que le Headless est né.

## Pourquoi vous n'avez peut-être pas besoin d'un CMS Headless

Le Headless n'est pas nécessairement la bonne solution pour tous les cas d'utilisation, cependant. Cela pourrait ne pas être pour vous si...

### Vous avez une petite équipe

Adopter et construire une architecture headless demande beaucoup d'efforts. Pour en tirer tous les avantages, vous devriez avoir une équipe de développeurs dédiée pour construire votre front-end ainsi que des personnes dans votre équipe pour travailler sur l'ajout de contenu à votre CMS.

### Vous dépendez fortement d'une implémentation simple de prévisualisation en direct

Les prévisualisations en direct sur les CMS Headless ne sont pas les plus intuitives à configurer (au moment de l'écriture) et demandent quelques efforts aux développeurs pour les implémenter.

### Vous n'avez besoin que de capacités de publication simples

Comme nous venons de l'apprendre, le headless demande un effort raisonnable pour fonctionner efficacement et efficacement.

Si vous n'avez besoin que de capacités de publication simples sans fonctionnalités comme l'internationalisation ou le contrôle d'accès basé sur les rôles, il est préférable d'attendre d'avoir besoin de ces fonctionnalités supplémentaires pour utiliser un CMS Headless.

## Cas d'utilisation pour un CMS Headless

Beaucoup de mes premiers projets de CMS étaient centrés autour de sites corporatifs et de blogs personnels, qui sont tous deux des cas d'utilisation solides pour le headless. Mais je ne construis pas de sites à temps plein, donc je ne livre pas souvent de code.

Personnellement, j'ai utilisé un CMS pour aider à construire un [Catalogue de Restaurants](https://foodadvisor.strapi.io/), un [Site Web d'Événements](https://conf.strapi.io/speakers), et un [Quiz en Ligne](https://conf.strapi.io/quizz).

Il y a des gens qui utilisent des CMS headless pour construire des sites eCommerce, des projets de suivi Covid, des systèmes de gestion hospitalière, des applications de gestion d'inventaire, des catalogues mobiles, des jeux VR, et certaines personnes gèrent même des campagnes email avec eux. Tant de possibilités.

## Conclusion

Voir ce que les gens construisent avec les CMS est très inspirant. Et j'ai gagné une énorme appréciation pour les CMS en tant que technologie. Ce que je pensais être un outil ennuyeux alimente en réalité tant de choses autour de moi.

Il y a beaucoup de cas d'utilisation pour les CMS Headless de nos jours. Et bien qu'à l'heure actuelle, il y ait un énorme focus sur le service aux développeurs (que de nombreux CMS font bien), nous avons encore du chemin à parcourir pour améliorer l'expérience des éditeurs de contenu.

C'est excitant d'avoir un pied dans la course, et tout ce que je peux vous dire, c'est que ce sera une période incroyable pour la technologie Headless en général.

Alors, espérons que cet article vous aide à sauter dans le wagon et à mieux comprendre ce que la technologie peut et ne peut pas faire.

Après tout, à la fin de la journée, le choix vous appartient !

![Image](https://www.freecodecamp.org/news/content/images/2021/06/javier-allegue-barros-C7B-ExXpOIE-unsplash.jpg align="left")

### Ressources

* [Headless CMS](https://jamstack.org/headless-cms/) | Jamstack.org

* [Qu'est-ce qu'un Headless CMS](https://strapi.io/what-is-headless-cms)

* [Qu'est-ce qu'un Headless CMS et pourquoi devriez-vous vous en soucier](https://www.stackbit.com/blog/what-is-a-headless-cms/)

* [Comparaison de CMS](https://cms-comparison.io/#/card)