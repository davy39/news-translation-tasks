---
title: Comment construire un site Jamstack avec Next.js et Vercel - Guide Jamstack
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-09-17T16:08:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-jamstack-site-with-next-js-and-vercel-jamstack-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/jamstack-handbook.jpg
tags:
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
seo_title: Comment construire un site Jamstack avec Next.js et Vercel - Guide Jamstack
seo_desc: "The Jamstack architecture is a modern approach to an old idea: making fast,\
  \ static websites, but making them dynamic with tools like JavaScript. \nHow can\
  \ we leverage the web framework Next.js and hosting platform Vercel to build and\
  \ deploy performant..."
---

L'architecture Jamstack est une approche moderne d'une vieille idée : créer des sites web statiques rapides, mais les rendre dynamiques avec des outils comme JavaScript. 

Comment pouvons-nous tirer parti du framework web Next.js et de la plateforme d'hébergement Vercel pour construire et déployer des applications web performantes et fiables ?

_Note : Ceci est un aperçu de mon [Guide Jamstack](https://jamstackhandbook.com/), un guide pour tout ce que vous devez savoir sur le Jamstack. Il contient 3 tutoriels, y compris celui-ci. [Obtenez votre copie](https://jamstackhandbook.com/) et apprenez à construire des applications rapides et dynamiques avec JavaScript et le web statique._

* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 1 : Commencer avec une application React Next.JS](#heading-etape-1-commencer-avec-une-application-react-nextjs)
* [Étape 2 : Configurer le projet avec Git](#heading-etape-2-configurer-le-projet-avec-git)
* [Étape 3 : Déployer Next.js avec Vercel](#heading-etape-3-deployer-nextjs-avec-vercel)
* [Que venons-nous de déployer ?](#heading-que-venons-nous-de-deployer)
* [Comprendre le CI/CD moderne avec Git](#heading-comprendre-le-cicd-moderne-avec-git)
* [Faire une modification et voir le déploiement automatique](#heading-faire-une-modification-et-voir-le-deploiement-automatique)
* [Que avons-nous appris ?](#heading-que-avons-nous-appris)

%[https://www.youtube.com/watch?v=9nV4pIrKmyE]

[Next.js](https://nextjs.org/) est un framework web construit et maintenu par [Vercel](https://vercel.com/). Next.js facilite la création d'une nouvelle application React et fournit de nombreuses fonctionnalités prêtes à l'emploi comme le rendu côté serveur (SSR) et la génération de site statique (SSG).

## Que allons-nous construire ?

Notre projet lui-même sera relativement simple. Nous allons utiliser le Starter par défaut de Next.js pour démarrer facilement le projet, apprendre à configurer Next.js pour compiler statiquement, puis déployer ce projet avec nos personnalisations sur Vercel.

> Un Starter est un modèle qui permet aux développeurs de recréer ce modèle à partir de la ligne de commande. Lors de l'installation du starter, le framework configurera le projet et installera toutes les dépendances.

## Étape 1 : Commencer avec une application React Next.JS

Pour commencer, nous voulons d'abord naviguer vers le répertoire dans lequel nous souhaitons créer notre projet.

Nous utiliserons un Starter pour créer notre projet. Pour ce faire, nous avons deux options pour un gestionnaire de paquets à utiliser : yarn ou npm. Vous pouvez choisir celui avec lequel vous êtes le plus à l'aise pour le reste du guide.

```
yarn create next-app
# ou
npx create-next-app
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/yarn-create-next-app.jpg)
_Création d'une nouvelle application Next.js_

Lors de l'exécution de cette commande, Next.js vous demandera d'abord un nom de projet. Ici, nous pouvons utiliser n'importe quel nom pour identifier le projet. Je vais utiliser my-nextjs-app.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-project-name.jpg)
_Nommer un projet Next.js_

Une fois l'installation terminée, nous sommes maintenant prêts à commencer avec Next.js.

Naviguez dans votre terminal vers le nouveau répertoire où se trouve votre projet et exécutez :

```
yarn dev
# ou
npm run dev
```

Cela démarrera votre serveur de développement, qui rendra votre nouveau site disponible à l'adresse [http://localhost:3000](http://localhost:3000).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-dev-server.jpg)
_Démarrage du serveur de développement Next.js_

Si vous ouvrez votre adresse [http://localhost:3000](http://localhost:3000), vous devriez maintenant voir le projet par défaut de Next.js !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-default-starter.jpg)
_Nouvelle application Next.js_

## Étape 2 : Configurer le projet avec Git

Vous voudrez configurer cette étape suivante par vous-même. Créez un nouveau dépôt avec votre fournisseur Git préféré qui est supporté par Vercel.

Au moment de la rédaction de cet article, [Vercel supporte GitHub, Gitlab, et Bitbucket](https://vercel.com/docs/git-integrations).

Si vous choisissez un fournisseur pour la première fois, GitHub est une option solide et facile à démarrer.

Vous voudrez ensuite ajouter votre projet à ce nouveau dépôt et pousser le projet sur Git.

> Besoin d'aide ? Consultez « Ajouter un projet existant à GitHub en utilisant la ligne de commande » [https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line](https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)

Pour le reste de ce guide, je ferai référence à GitHub, mais les instructions devraient être les mêmes pour tout fournisseur supporté.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-app-github.jpg)
_Application Next.js sur GitHub_

## Étape 3 : Déployer Next.js avec Vercel

Une fois votre projet configuré avec GitHub, naviguez vers vercel.com et connectez-vous.

Si vous n'avez pas déjà de compte Vercel, vous devriez en créer un maintenant. Je recommande de créer un compte avec votre compte GitHub car cela vous aidera à importer votre projet.

Dans le tableau de bord Vercel, cliquez sur **Importer le projet**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vercel-import-project.jpg)
_Importer le projet vers Vercel_

Ensuite, sous Importer le dépôt Git, cliquez sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vercel-import-git-repository.jpg)
_Importer le dépôt Git vers Vercel_

Vercel vous demandera maintenant l'URL du dépôt. Ce sera la page d'accueil du dépôt que vous venez de créer pour votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vercel-git-repo-url.jpg)
_Ajouter l'URL du dépôt Git à Vercel_

Après avoir cliqué sur Continuer, Vercel a déjà détecté que votre projet utilise Next.js. Cela signifie que nous n'avons pas besoin de configurer des configurations personnalisées, et nous pouvons cliquer sur Déployer !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vercel-deploy-nextjs.jpg)
_Déployer le projet Next.js vers Vercel_

À ce stade, Vercel se mettra au travail et commencera à construire le nouveau projet et à le déployer sur leur infrastructure.

Une fois terminé, il vous félicitera et vous donnera un lien pour visiter votre site.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vercel-new-site-deployed.jpg)
_Projet Vercel déployé avec succès_

Cliquez sur Visiter et vous serez dirigé vers votre projet en direct sur Internet :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-app-on-vercel.jpg)
_Application Next.js en direct_

## Que venons-nous de déployer ?

Nous venons de créer une nouvelle application React avec Next.js et de la déployer sur Vercel.

Nous allons passer en revue chaque étape spécifique :

* **Créer une application Next** : Nous avons d'abord créé un nouveau projet Next.js sur notre ordinateur. Cela nous a fourni une nouvelle application React complète avec des dépendances et du code pour commencer avec un site web de base.
* **Ajouter le projet à Git** : Nous avons ajouté notre nouveau projet Next.js à un dépôt Git en ligne qui est supporté par Vercel. Cela nous permet d'interfacer facilement le projet avec d'autres services comme Vercel.
* **Connecter Git à Vercel** : Nous avons importé notre projet de Git vers Vercel. Cela a permis à Vercel d'interagir avec notre code.
* **Construire et déployer avec Vercel** : Vercel a téléchargé notre code, a pu reconnaître qu'il s'agissait d'un projet Next.js, a construit notre projet et a déployé la sortie compilée sur son infrastructure et l'a rendue disponible sur le web.

Si vous attendiez plus d'étapes pour publier votre projet dans le monde, il n'y en a pas ! Le point d'entrée pour publier un nouveau projet React est maintenant plus bas que jamais et Next.js et Vercel vous aident à y parvenir.

## Comprendre le CI/CD moderne avec Git

Un autre avantage des fournisseurs d'infrastructure modernes comme Vercel est que, lors de l'utilisation de GitHub comme service de connexion, Vercel peut surveiller les changements sur notre branche principale.

Une fois que Vercel reconnaît qu'un changement a été effectué, il téléchargera le dernier code et réexécutera le même processus que la première fois (à l'exception de toute mise en cache et optimisation).

Cela signifie que chaque fois que nous avons de nouveaux changements sur notre branche de production, ils seront automatiquement déployés. 

## Faire une modification et voir le déploiement automatique

Pour tester les déploiements automatiques, faisons une modification à notre projet.

Dans notre projet, faisons une modification du contenu de la page à l'intérieur de `pages/index.js`. Je vais changer le titre en « Projet Next.js de Colby ».

```jsx
<h1 className={styles.title}>
  Projet Next.js de Colby
</h1>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/colbys-nextjs-app.jpg)
_Application Next.js avec modification_

Ensuite, validez cette modification sur votre branche principale Git et poussez-la sur GitHub.

Si vous attendez quelques secondes et naviguez à nouveau vers [vercel.com](https://vercel.com), trouvez votre projet et cliquez sur l'onglet Déploiements.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vercel-deployments.jpg)
_Déploiement Vercel lorsque le changement est détecté_

Vous verrez que votre projet est maintenant en cours d'exécution ou a peut-être déjà terminé si vous n'avez pas été assez rapide. Maintenant, si vous ouvrez à nouveau le lien de votre site web, vous verrez les modifications déployées !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/deployed-nextjs-app-vercel.jpg)
_Application Next.js modifiée déployée sur Vercel_

## Que avons-nous appris ?

Next.js est un framework web qui nous permet de créer rapidement et facilement une nouvelle application React. 

Cela, ainsi que d'autres frameworks similaires, peut être utile pour être immédiatement productif au lieu de passer du temps à construire le framework du projet nous-mêmes.

Vercel est une plateforme d'hébergement et de déploiement qui nous permet de nous intégrer avec notre fournisseur Git préféré et supporté. Une fois connecté, Vercel téléchargera notre projet, construira notre projet et déployera la sortie sur Internet.

Les outils d'infrastructure modernes comme Vercel surveilleront les changements sur notre dépôt Git et construiront et déployeront notre projet afin que nous voyions toujours la dernière version.

## En savoir plus sur le Jamstack !

Vous pouvez en apprendre davantage sur le Jamstack, y compris 2 autres tutoriels approfondis, avec mon Guide Jamstack.

<p style="text-align: center;">
    <a href="https://jamstackhandbook.com/">
    	<img src="https://www.freecodecamp.org/news/content/images/2020/09/jamstack-handbook-social.jpg" alt="Guide Jamstack : Construire des applications rapides et dynamiques avec Javascript et le web statique" style="
		    max-width: 840px;
		    border: solid 5px #0A64EC;
		">
    	<button style="
    		background-color: #9162BB;
	    	color: white;
		    font-weight: bold;
    		padding: .5em 1em;
    		border-radius: .2em;
		    box-shadow: 0 2px 4px rgba(0,0,0,.25);
		">Commander sur jamstackhandbook.com</button>
    </a>
</p>

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Suivez-moi%20pour%20plus%20de%20JavaScript%252c%20UX%252c%20et%20d'autres%20choses%20intéressantes!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4E83FB Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsorisez-moi</a>
    </li>
  </ul>
</div>