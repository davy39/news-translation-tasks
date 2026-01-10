---
title: 'De zéro à déploiement : comment j''ai créé un site statique à partir de rien
  en utilisant Netlify + Gatsby'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-18T16:39:07.000Z'
originalURL: https://freecodecamp.org/news/from-zero-to-deploy-how-i-created-a-static-website-from-scratch-using-netlify-gatsby-ebca82612ffd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CHViJ8BewpcNw36AGdkczQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'De zéro à déploiement : comment j''ai créé un site statique à partir de
  rien en utilisant Netlify + Gatsby'
seo_desc: 'By Eden Adler

  After my first year working as a frontend web developer, I got the idea to have
  my own personal site. It’d be a platform to showcase my work, share content, and
  serve as a creative outlet for me outside of work. Here, I’ll walk you thro...'
---

Par Eden Adler

Après ma première année en tant que développeur web frontend, j'ai eu l'idée d'avoir mon propre site personnel. Ce serait une plateforme pour présenter mon travail, partager du contenu et servir de débouché créatif pour moi en dehors du travail. Ici, je vais vous guider à travers mon expérience de construction du site, de zéro jusqu'au déploiement.

### Acheter un domaine : Google Domains

J'ai commencé de zéro, en achetant un domaine. Il existe de nombreuses options. J'ai choisi Google Domains puisque j'avais déjà un compte et je n'aurais pas à en ouvrir un autre juste pour cela. Cela coûte 12 $/an (prix standard) et a été très rapide à configurer. (Pour information, vous pouvez également acheter un domaine via Netlify.)

Trois mois se sont écoulés où mon domaine est resté vide. J'étais trop pris par les nombreux détails pour mettre le site en ligne. En prenant du recul, j'ai réalisé que personne ne verrait mon site tant que je ne commencerais pas à le promouvoir activement. Une fois que j'ai soulagé cette pression, je me suis poussé à mettre _quelque chose_ pour combler le vide. Avec ce poids en moins sur mes épaules, j'ai décidé de m'amuser et de créer quelque chose de simple et amusant.

### Commencer

Il y a beaucoup de choses à considérer lors de la création d'un site web : le design, l'UI/UX, l'accessibilité, le SEO, l'analytique, et plus encore. Cela peut être accablant de tout penser et planifier en même temps.

Pour rendre cela moins intimidant, j'ai décidé de le diviser en étapes. La première étape était de créer une simple page "bientôt disponible" et de la déployer. Ensuite, une fois que cela était en ligne, je pourrais travailler en coulisses sur la conception, le développement et la perfection du site.

> "Fini est mieux que parfait." — Sheryl Sandberg

### Construire le frontend : Gatsby.js

J'ai d'abord entendu parler de Gatsby lors de la conférence [ReactNext](https://www.gatsbyjs.org/blog/2017-09-13-why-is-gatsby-so-fast/) à laquelle j'ai assisté, et j'étais curieux de l'utiliser depuis. Une alternative que j'ai considérée était Hugo, un autre générateur de site statique très populaire écrit en Go.

Gatsby.js m'attirait également car il est basé sur React.js, que nous utilisons dans notre stack chez [Lemonade](https://www.freecodecamp.org/news/from-zero-to-deploy-how-i-created-a-static-website-from-scratch-using-netlify-gatsby-ebca82612ffd/undefined). Il intègre également GraphQL, une technologie que je souhaitais essayer. Je suis pour l'efficacité, donc je suis curieux de voir comment GraphQL aide à récupérer des données plus efficacement et permet au frontend d'être moins dépendant de la logique serveur.

Lorsqu'il a fallu choisir un boilerplate, ou "starter" comme les appelle Gatsby, je savais que je voulais quelque chose de basique. Après avoir parcouru les starters populaires, j'ai choisi d'utiliser `gatsby-starter-default` plutôt que `gatsby-starter-netlify-cms`.

Pourquoi ? Je ne voulais pas m'engager à ce que le site soit principalement un blog. Avec le starter Netlify, j'aurais eu beaucoup de dépendances supplémentaires dont je ne prévoyais pas avoir besoin.

La première itération du site est une simple page de remplacement "bientôt disponible" avec un accent sur **simple**. Je me suis inspiré de [CodePen](https://codepen.io/juanbrujo/pen/XmXqyw), j'ai créé mon composant React personnalisé et j'ai ajouté quelques polices et icônes personnalisées. C'est tout.

Pour modifier le titre de l'en-tête par défaut, j'ai été doucement forcé (?) de plonger dans GraphQL. Voici une version simplifiée de ce à quoi ressemble mon en-tête :

<script src="https://gist.github.com/edenadler/dd55a1552c330730a3707d22a5f782dc.js"></script>

Les points clés à retenir ici sont :

* StaticQuery a 2 props : `query` et `render`
* `SiteTitleQuery` est le nom de l'opération. Pensez-y comme à un nom de fonction. Il est utile pour le débogage et la journalisation, vous permettant de rechercher facilement la requête spécifique dans votre base de code.
* Un avantage majeur de `StaticQuery` par rapport à `page query` est qu'il vous permet de configurer une requête GraphQL dans le composant où elle est utilisée (au lieu de la passer en tant que prop).
* J'ai modifié mon titre dans le fichier `gatsby-config.js`, où sont stockées les options de configuration du site. Cela explique d'où vient le `site` dans `data.site.siteMetadata.title`.

### Hébergement : Netlify

Avec tant d'outils disponibles, il est difficile de savoir ce qui convient à la portée d'un projet. Les critères importants pour moi étaient :

* Hébergement gratuit pour un domaine personnalisé
* Facilité d'utilisation
* Capacité à servir du contenu dynamique (pas seulement statique)
* Sécurité HTTPS intégrée

[Netlify](https://www.freecodecamp.org/news/from-zero-to-deploy-how-i-created-a-static-website-from-scratch-using-netlify-gatsby-ebca82612ffd/undefined) est un service d'hébergement et de backend [serverless](https://martinfowler.com/articles/serverless.html) pour les sites statiques. Il m'a offert tout ce que je cherchais, plus des fonctionnalités bonus auxquelles je n'avais même pas pensé, comme :

* Capacité à visualiser une version de prévisualisation avant de déployer en production
* Fonctionnalité de test A/B prête à l'emploi

Ils vous gâtent un peu de cette manière, j'ai été impressionné.

Une fois que j'avais atteint ce que vous avez vu ci-dessus, j'ai décidé qu'il était prêt à être déployé. Comme je n'ai pas utilisé Netlify comme fournisseur DNS, j'ai dû configurer un "domaine personnalisé". J'ai suivi leur [tutoriel](https://www.netlify.com/docs/custom-domains/#assigning-a-custom-domain), et quelques minutes plus tard, tout était configuré.

Il ne me restait plus qu'à déployer. Pour cela, il y a quelques options :

* **Déploiement continu**

Lie votre compte Github (ou autre), et Netlify construira et déployera automatiquement pour vous lorsque vous pousserez votre nouvelle version. Vous pouvez également choisir de limiter leur accès Github à vos dépôts publics uniquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RYT57lUC9wFjVJ_XNQQTOA.png)
_Choisir de déployer via "Déploiement continu"_

* **Manuel**

Si vous choisissez de ne pas lier votre compte, ou si vous étiez comme moi et que vous vouliez simplement essayer la première fois, vous pouvez facilement glisser-déposer votre projet pour déclencher le déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FuBIrBdIs23X5u5YY_XqOg.png)
_Choisir de déployer manuellement via glisser-déposer_

J'ai testé la méthode manuelle pour le premier déploiement. 2 minutes (?) plus tard, le site était en ligne et fonctionnait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vct7rqIr0jzonIqV3GU26g.png)
_Logs de déploiement clairs et descriptifs_

Découvrez-le → [edenadler.com](https://edenadler.com)

### Rétrospective

Pour cette POC basique, je suis content de ne pas avoir essayé de faire des choses compliquées avec GraphQL, et d'avoir été trop ambitieux avec le design et l'exécution du site. Vous pourriez même remarquer des choses, comme le favicon, qui sont toujours là depuis le boilerplate de Gatsby. Je voulais vraiment faire le strict minimum. Fini plutôt que parfait.

Que vous créiez votre propre site personnel, travailliez sur un projet parallèle ou écriviez un article de blog, ne cherchez pas la perfection. Fixez-vous un objectif réaliste et tangible et commencez. Si votre projet implique d'essayer de nouvelles technologies, ne les essayez pas toutes en même temps. Divisez le projet en tâches plus petites et réalisables en une journée, ou même en un après-midi. Plus important encore, amusez-vous.

### Mes prochaines étapes

* Engager un designer et implémenter les designs
* Planifier et ajouter du contenu
* Explorer l'intégration de GraphQL
* … beaucoup d'autres idées ?

Merci d'avoir lu ✨ Si vous avez des questions, n'hésitez pas à commenter ici ou à me contacter sur [Instagram](https://www.instagram.com/edenadler) ❤️