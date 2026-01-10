---
title: Comment déployer une application Front End avec Netlify
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2021-01-09T00:23:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-front-end-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Turquoise-Confetti-Birthday-Greetings-Facebook-Cover.png
tags:
- name: app development
  slug: app-development
- name: deployment
  slug: deployment
- name: Front-end Development
  slug: front-end-development
- name: Netlify
  slug: netlify
seo_title: Comment déployer une application Front End avec Netlify
seo_desc: 'Hi everyone! In this article, I''m going to discuss how to deploy an application
  you''ve built.

  The application deployment process might seem complicated, and this might prevent
  some developers from deploying their applications after they''ve developed ...'
---

Bonjour à tous ! Dans cet article, je vais vous expliquer comment déployer une application que vous avez construite.

Le processus de déploiement d'une application peut sembler compliqué, et cela peut empêcher certains développeurs de déployer leurs applications après les avoir développées.

Ici, je vais vous guider à travers un processus fluide pour lancer votre application, qui pourra ensuite être accessible partout dans le monde via une URL.

### Table des matières

- Pourquoi devez-vous déployer vos applications frontend ?
- Qu'est-ce que Netlify ?
- Ce que vous pouvez faire avec Netlify
- Comment déployer votre site
- Ressources

## Pourquoi devez-vous déployer vos applications frontend ?

Il y a de nombreux avantages à déployer vos applications. Bien sûr, vous ne voulez pas que votre belle application reste sur votre localhost pour toujours.

Déployer votre application facilite le partage de votre projet, de votre activité secondaire ou de votre startup avec des investisseurs potentiels ou de futurs employeurs. S'ils peuvent voir ces projets, cela les aide à évaluer vos compétences. Cela vous permet également de montrer votre progression au monde.

Dans cet article, nous allons utiliser la plateforme incroyable [Netlify](https://www.netlify.com 'Page d'accueil de Netlify') pour déployer notre application.

Ce nom vous semble familier, n'est-ce pas ? Mais si vous ne l'avez pas encore utilisé pour déployer une application web, faites-moi confiance, je sais ce que vous ressentez.

Je vais vous guider à travers les étapes pour déployer votre site sur [Netlify](https://www.netlify.com) en moins de 4 minutes. Nous verrons également quelques autres fonctionnalités qui peuvent être réalisées avec Netlify dès la sortie de la boîte.

## Qu'est-ce que Netlify ?

[Netlify](https://netlify.com/) est une plateforme qui permet aux développeurs d'automatiser des projets web modernes, et c'est un endroit où vous pouvez déployer votre application sans vous soucier des configurations frustrantes.

Vous pouvez également intégrer des fonctionnalités cool et des fonctionnalités dynamiques comme des fonctions serverless et la gestion de formulaires sur Netlify. Cela semble bien, n'est-ce pas ?

## Fonctionnalités de Netlify

### Configurer les builds
Netlify vous aide à exécuter la commande de build chaque fois que vous poussez une mise à jour vers votre dépôt.

Il existe des paramètres supplémentaires que vous pouvez configurer comme le déploiement automatique ainsi que d'autres paramètres de déploiement utiles.

### Déploiements de sites [(Atomic deploys)](https://docs.netlify.com/site-deploys/overview/)
L'une des fonctionnalités incroyables de Netlify est le déploiement de sites. Il garantit que votre site est déployé et toujours cohérent.

Vous pouvez également activer les notifications de déploiement, exécuter un test pendant que Netlify compare le nouveau déploiement avec celui existant, puis mettre à jour uniquement les fichiers qui ont été modifiés.

### Surveiller les sites [(Netlify Analytics)](https://docs.netlify.com/monitor-sites/analytics/)
La surveillance de votre site peut devenir difficile si vous n'avez pas une infrastructure appropriée en place.

Vous pouvez facilement surveiller les activités de votre site sur cette plateforme où vous pouvez suivre chaque journal sur l'utilisation des builds de l'équipe.

#### Domaines & HTTPS [(Enregistrer de nouveaux domaines)](https://docs.netlify.com/domains-https/netlify-dns/domain-registration)
En termes simples, un domaine est l'URL que quiconque tape dans le navigateur pour visiter votre site. Vous pouvez attribuer un domaine personnalisé si vous en avez déjà acheté un ou sécuriser un domaine auprès de Netlify.

Dans les deux cas, la gestion du système de noms de domaine est gérée par Netlify. Ils fournissent également un HTTPS automatique gratuit sur tous les sites. Cool, n'est-ce pas ?

#### Routage [(En savoir plus sur le routage)](https://docs.netlify.com/routing/redirects/)
Le routage, les redirections, les proxies, etc., deviennent beaucoup plus faciles lorsque votre site est déployé sur Netlify.

### Accès des visiteurs
Voici une autre fonctionnalité cool que j'apprécie : chaque fois que vous devez ajouter quelqu'un à l'équipe, vous pouvez configurer des contrôles d'accès basés sur les rôles qui permettent à l'administrateur/développeur senior de prendre le contrôle et de donner accès aux individus de l'équipe pour éviter les escalades.

### Formulaires [(Formulaires Netlify)](https://docs.netlify.com/forms/setup/)
Lorsque vous devez collecter des données auprès des utilisateurs sur un site déployé sur Netlify, vous pouvez le faire en utilisant les formulaires Netlify. Cela n'ajoute pas d'appels API ou de JavaScript supplémentaire sur votre site.

Les bots de build gèrent la soumission de formulaires en analysant vos fichiers HTML directement au moment du déploiement. Vous pouvez également configurer le destinataire, le groupe et les notifications.

### Fonctions [(Déployer des fonctions serverless)](https://docs.netlify.com/functions/overview/)
Les fonctions serverless peuvent être référencées comme des fonctions programmatiques à usage unique qui sont hébergées sur une infrastructure gérée.

Netlify vous permet de déployer des fonctions Lambda serverless avec une gestion gérée directement dans Netlify, tandis qu'elles sont construites et déployées avec le reste de vos sites.

### L'interface de ligne de commande Netlify [(Interface de ligne de commande Netlify)](https://docs.netlify.com/cli/get-started)
Vous vous demandez peut-être si toutes les activités sont réalisées uniquement sur l'interface utilisateur de Netlify - eh bien, non, ce n'est pas le cas.

Il existe une autre fonctionnalité formidable qui permet aux développeurs de déployer des sites ou de faire certaines configurations directement depuis leur terminal. L'interface de ligne de commande Netlify peut être utilisée pour exécuter un serveur de développement local qui peut être partagé, y compris des plugins.

### L'API Netlify [(API Netlify)](https://docs.netlify.com/api/get-started/#authentication)
L'API de Netlify peut être utilisée pour gérer le déploiement de sites, les injections de scripts, et plus encore. Elle utilise JSON pour la sérialisation, ce qui est conforme à la norme REST.

### Comptes & facturation
Découvrez comment [gérer les membres de l'équipe](https://docs.netlify.com/accounts-and-billing/team-management/manage-team-members) et comment transférer des sites entre les équipes.

> J'espère que vous pouvez maintenant voir à quel point Netlify est puissant. Mais parfois, voir peut être trompeur, alors essayons-le par nous-mêmes.

Comme vous pouvez le constater d'après le titre de cet article, je vais vous montrer uniquement comment déployer votre site sur netlify.com. Mais pour explorer d'autres fonctionnalités [cliquez ici pour en savoir plus](https://docs.netlify.com/), pratiquez et explorez.

## Comment déployer un site sur Netlify

### Étape Une

Connectez-vous ou inscrivez-vous sur netlify.com si vous êtes un nouvel utilisateur. C'est gratuit :)

### Étape Deux

Comme montré ci-dessous, tout ce dont vous avez besoin est de sélectionner un site à partir de Git en cliquant sur le bouton avec le nom « New site from Git ».

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119982/netlify%20deploy%20post/Screenshot.png)

### Étape Trois

Vous verrez l'interface ci-dessous où vous pouvez choisir le fournisseur Git où le code source de votre site est hébergé.

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/select_git.png)

### Étape Quatre

Choisissez le dépôt que vous souhaitez lier à votre site sur Netlify.

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/select_repo.png)

### Étape Cinq

Nous y sommes presque :)

Cette section vous permet d'avoir plus de contrôle sur la façon dont Netlify construit et déploie votre site avec l'option de paramètres montrée ci-dessous :

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119981/netlify%20deploy%20post/select_to_deploy_site.jpg)

### Étape Six

Attendez, Netlify prépare tout pour vous. :)

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/site_deploy_in_pgrogress.png)

### Étape Sept

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/site.png)

Félicitations ! Votre site est en ligne !

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119980/netlify%20deploy%20post/Screenshot1.png)

Cliquez sur l'URL générée avec l'extension .netlify.com sous l'en-tête qui indique « Deploys for ».

**Enfin : Vous pouvez également configurer un nouveau domaine ou changer celui généré en quelque chose de plus agréable en cliquant sur le « … » qui intègre « Edit site name » mais il se terminera par .netlify.com. [Cliquez ici pour en savoir plus](https://docs.netlify.com/domains-https/custom-domains/)**

![Netlify](https://res.cloudinary.com/olanetsoft/image/upload/v1608119981/netlify%20deploy%20post/domain_setup.png)

J'espère que vous avez trouvé ce guide utile :)

NOTE : l'extension d'URL Netlify est maintenant netlify.app. Toutes les URL netlify.com seront maintenant redirigées vers netlify.app.

**N'oubliez pas de consulter mes autres articles, cela me donne de la joie :) et l'envie d'écrire plus de choses.**

Vous pouvez également me contacter sur [Twitter](https://twitter.com/olanetsoft).