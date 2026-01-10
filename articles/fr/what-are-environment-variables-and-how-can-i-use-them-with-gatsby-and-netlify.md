---
title: Qu'est-ce que les variables d'environnement et comment les utiliser avec Gatsby
  et Netlify ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-28T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-environment-variables-and-how-can-i-use-them-with-gatsby-and-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/environment-variables.jpg
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: deployment
  slug: deployment
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: Git
  slug: git
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React
  slug: reactjs
- name: technology
  slug: technology
seo_title: Qu'est-ce que les variables d'environnement et comment les utiliser avec
  Gatsby et Netlify ?
seo_desc: "When starting to integrate 3rd party services into your application or\
  \ website, you'll start to find it useful to have different environments, such as\
  \ a development and production environment. \nHow can we configure this so we don't\
  \ have to directly e..."
---

Lorsque vous commencez à intégrer des services tiers dans votre application ou votre site web, vous trouverez utile d'avoir différents environnements, tels qu'un environnement de développement et de production. 

Comment pouvons-nous configurer cela pour ne pas avoir à modifier directement notre code pour changer notre environnement ?

* [Qu'est-ce que les variables d'environnement ?](#heading-questce-que-les-variables-denvironnement)
* [Comment les variables d'environnement peuvent-elles être utiles ?](#heading-comment-les-variables-denvironnement-peuvent-elles-etre-utiles)
* [Comment puis-je garder ces fichiers sécurisés ?](#heading-comment-puisje-garder-ces-fichiers-securises)
* [Gatsby et les variables d'environnement](#heading-gatsby-et-les-variables-denvironnement)
* [Netlify et les variables d'environnement](#heading-netlify-et-les-variables-denvironnement)
* [Étape 1 : Créer un site web "Hello, world"](#heading-etape-1-creer-un-site-web-hello-world)
* [Étape 2 : Créer une variable d'environnement locale avec Gatsby](#heading-etape-2-creer-une-variable-denvironnement-locale-avec-gatsby)
* [Étape 3 : Déployer le site web sur Netlify](#heading-etape-3-deployer-le-site-web-sur-netlify)
* [Où pouvez-vous ajouter ou mettre à jour plus de variables dans Netlify ?](#heading-ou-pouvez-vous-ajouter-ou-mettre-a-jour-plus-de-variables-dans-netlify)

%[https://www.youtube.com/watch?v=oq_RPOI0xsU]

## Qu'est-ce que les variables d'environnement ?

Les variables d'environnement sont des valeurs prédéterminées qui sont généralement utilisées pour fournir la capacité de configurer une valeur dans votre code depuis l'extérieur de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/environment-variable-secret.jpg)
_Variable d'environnement MY_SECRET_KEY utilisée pour l'autorisation_

Lors du développement local, ou parfois même dans un pipeline de déploiement, vous trouverez souvent ces variables stockées dans un fichier nommé avec une sorte de variation de `.env`.

## Comment les variables d'environnement peuvent-elles être utiles ?

Probablement le cas d'utilisation le plus courant pour les variables d'environnement est la possibilité de configurer différentes options pour différents environnements. Souvent, lors du développement contre des services tiers, vous souhaitez avoir une version de développement ou un bac à sable disponible pour faire des requêtes de test, de cette façon, cela n'impacte pas les données de production réelles.

Les variables d'environnement sont utiles car elles vous permettent de changer quel environnement utilise quel environnement de service tiers en changeant une clé API, un endpoint, ou ce que le service utilise pour distinguer les environnements.

Le code que vous déployez doit être prévisible, donc en n'ayant pas à changer de code, juste la configuration en dehors du code, vous pouvez maintenir cette prévisibilité.

## Comment puis-je garder ces fichiers sécurisés ?

C'est probablement l'un des points les plus importants ici – vous devez vous assurer de manipuler ces fichiers avec soin et de ne pas les ajouter à un dépôt git. En exposant ces clés en les téléchargeant involontairement dans un endroit public, l'internet pourrait facilement trouver ces clés et les utiliser à ses propres fins.

Par exemple, les clés [AWS](https://aws.amazon.com/) sont une source précieuse. Les gens exécutent des bots dans le seul but d'essayer de scanner Github pour des clés. Si quelqu'un trouve une clé AWS, il pourrait utiliser cette clé pour accéder à des ressources telles que l'exécution d'une opération bitcoin à vos frais. Ce n'est pas pour vous faire peur, c'est pour vous rendre conscient afin d'éviter que vos clés ne soient compromises.

Alors, comment pouvons-nous garder ces fichiers sécurisés ? La manière la plus simple est d'ajouter le fichier d'environnement où vous gardez ces clés à votre fichier `.gitignore`.

Pour ce faire, ouvrez simplement votre fichier `.gitignore` existant ou créez-en un nouveau à la racine de votre dépôt et ajoutez le nom du fichier comme nouvelle ligne :

```
# Dans .gitignore
.env

```

Si vous voulez aller plus loin et vous assurer que cela n'arrive jamais à un dépôt, vous pouvez consulter des outils comme [git-secrets](https://github.com/awslabs/git-secrets) d'AWS Labs ou [GitLeaks](https://github.com/zricethezav/gitleaks) qui dispose même d'une [Github Action](https://github.com/marketplace/actions/gitleaks) pour faciliter l'intégration avec Github.

## Gatsby et les variables d'environnement

[Gatsby](https://www.gatsbyjs.org/) par défaut rend deux fichiers disponibles dans le cadre de son [flux de travail des variables d'environnement](https://www.gatsbyjs.org/docs/environment-variables/) qui rend ces valeurs disponibles dans le client : `.env.development` et `.env.production`. Ces fichiers correspondent aux scripts `gatsby develop` et `gatsby build` pour développer ou construire votre site.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/environment-variable-secret-gatsby.jpg)
_Variable d'environnement MY_SECRET_KEY pour le développement et la production_

Pour utiliser ces fichiers dans le processus de développement et de construction de Gatsby, Gatsby vous demande de préfixer ces variables avec `GATSBY_`. Cela fonctionne également si vous souhaitez les avoir disponibles au niveau du processus OS.

Bien que vous puissiez intégrer [dotenv](https://github.com/motdotla/dotenv) si vous avez des besoins plus avancés ou si vous ne souhaitez pas utiliser le préfixe `GATSBY_`, votre chemin de moindre résistance est probablement de simplement suivre la méthode Gatsby lorsque vous travaillez dans Gatsby.

## Netlify et les variables d'environnement

[Netlify](https://www.netlify.com/) fournit la possibilité d'ajouter des variables d'environnement dans le cadre de ses paramètres **Build & deploy** qui sont pris en compte dans les processus de construction.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/netlify-environment-variable.jpg)
_Ajout d'une variable d'environnement dans Netlify_

Heureusement, Netlify facilite l'ajout de n'importe quelle variable d'environnement que vous souhaitez au processus de construction ! Pour en ajouter une, vous pouvez simplement naviguer vers la section **Environment** de la page des paramètres **Build & deploy** de votre projet et ajouter une variable sous **Environment variables.**

Nous vous guiderons à travers ce processus un peu plus tard.

## Étape 1 : Créer un site web "Hello, world"

Pour notre guide, nous allons configurer un exemple très basique d'un site web Gatsby juste pour tester cela.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/new-website-gatsby-starter-leaflet.jpg)
_Nouveau site web avec Gatsby Sass Starter_

Bien que ce ne soit pas vraiment un cas d'utilisation courant des variables d'environnement, où normalement vous les utiliseriez pour des choses comme les clés API et les configurations de service, cela vous donnera une excellente idée de leur fonctionnement fondamental.

Nous allons utiliser ce [Gatsby Sass Starter](https://github.com/colbyfayock/gatsby-starter-sass) que j'ai créé, ce qui nous donnera un point de départ et ajoutera "Hello, [Environment]" selon l'endroit où il s'exécute.

Pour commencer, créons notre projet local en utilisant le [Gatsby CLI](https://www.gatsbyjs.org/docs/gatsby-cli/). Naviguez vers l'endroit où vous souhaitez stocker ce projet et exécutez :

```shell
gatsby new my-env-project https://github.com/colbyfayock/gatsby-starter-sass

```

Vous pouvez changer `my-env-project` en n'importe quel répertoire où vous souhaitez que ce projet soit créé, mais une fois que vous exécutez cette commande, vous aurez maintenant un projet dans ce nouveau répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/new-gatsby-project-command-line.jpg)
_Nouveau projet Gatsby dans le terminal_

Pour commencer, une fois dans ce répertoire, exécutez `yarn develop` pour apporter des modifications localement ou `yarn build` pour compiler votre nouveau site.

Une fois que vous êtes prêt, vous voudrez ajouter ce projet à Github. Si vous n'êtes pas familier avec la façon de faire cela, vous pouvez apprendre à [ajouter un projet existant à Github](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) ici.

## Étape 2 : Créer une variable d'environnement locale avec Gatsby

Notre prochaine étape est de créer un environnement local et d'ajouter une modification qui nous permettra de voir que cela fonctionne.

Pour commencer, créons d'abord un nouveau fichier à la racine de notre projet appelé `.env.development`. Il pourrait vous demander si vous voulez vraiment utiliser le préfixe `.`, assurez-vous de dire oui !

À l'intérieur de ce fichier, ajoutons :

```
# Dans .env.development
GATSBY_MY_ENVIRONMENT="Development"

```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/gatsby-development-environment-file.jpg)
_Création d'un fichier .env.development_

Ensuite, pour nous assurer de ne pas oublier de le faire, ajoutons également ce fichier `.env.development` à notre `.gitignore` afin de ne pas commettre accidentellement cela dans notre historique git. Si vous n'avez pas déjà de fichier `.gitignore`, assurez-vous de le créer à la racine de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-development-environment-file-gitignore.jpg)
_Ajout de .env.development à votre .gitignore_

Enfin, pour vérifier que cela fonctionne, ouvrons `pages/index.js` et remplaçons le contenu de notre balise `<h1>` par une variation de "Hello, world!" :

```jsx
<h1>Hello, {process.env.GATSBY_MY_ENVIRONMENT}</h1>

```

Et si nous enregistrons ce changement et l'ouvrons dans notre navigateur, nous devrions voir "Hello, Development" !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/using-environment-variable-gatsby.jpg)
_Utilisation d'une variable d'environnement pour votre site Gatsby_

[Suivez le commit !](https://github.com/colbyfayock/my-env-project/commit/e3e7000fbfab4cecac7739458034e70958e52211)

## Étape 3 : Déployer le site web sur Netlify

Nous avons donc créé notre site web en utilisant une simple variable d'environnement. Ensuite, nous voudrons déployer ce site sur Netlify. Si vous ne l'avez pas déjà fait, nous devrons [ajouter notre site web à Github](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) ou un autre fournisseur Git. Assurez-vous d'avoir cela configuré avant de continuer.

Après avoir créé un compte et vous être connecté à Netlify, cliquons sur le bouton **New site from Git** du tableau de bord principal, suivons les instructions pour connecter votre Github ou un autre fournisseur Git à Netlify, puis trouvons votre nouveau dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/adding-new-github-repository-netlify.jpg)
_Ajout d'un nouveau dépôt Github à Netlify_

Une fois que vous avez sélectionné votre dépôt, vous serez invité à configurer votre processus de construction. Heureusement, Netlify peut détecter que nous utilisons un site Gatsby et l'a pré-rempli pour nous. Sauf si vous avez ajouté quelque chose de spécial, gardez la configuration de base pour utiliser `gatsby build` pour construire votre projet et `public/` pour la sortie.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/configuring-netlify-build.jpg)
_Configuration des paramètres de construction de Netlify_

Maintenant, avant de cliquer sur **Deploy**, il y a une chose que nous voulons ajouter, et c'est notre variable d'environnement !

Juste au-dessus du bouton **Deploy site**, il y a un bouton **Advanced**. Cliquez dessus et vous verrez une nouvelle liste déroulante avec un bouton supplémentaire **New variable**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/configuring-environment-variable-netlify.jpg)
_Configuration d'une variable d'environnement dans la configuration de Netlify_

Cliquez sur ce bouton **New variable**, ajoutez notre `GATSBY_MY_ENVIRONMENT` comme nouvelle variable et ajoutez `Production` comme valeur. Et enfin, cliquez sur **Deploy site** !

À partir de là, vous devriez pouvoir regarder votre site web se déployer et une fois terminé, vous verrez votre nouveau site avec "Hello, Production" !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/deployed-gatsby-site-with-environment-variable.jpg)
_Site Gatsby déployé utilisant la variable d'environnement de Netlify_

## Où pouvez-vous ajouter ou mettre à jour plus de variables dans Netlify ?

Avec notre exemple, nous n'avons ajouté qu'une seule variable pendant la configuration. Mais Netlify vous permet d'ajouter ou de mettre à jour n'importe quelle autre variable que vous souhaitez.

Si vous souhaitez un jour changer cette variable ou en ajouter d'autres, vous pouvez naviguer vers la section **Environment** des paramètres **Build & deploy**, où vous pouvez modifier et ajouter d'autres variables dans la section **Environment variables**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/environment-variable-settings-netlify.jpg)
_Paramètres des variables d'environnement dans Netlify_

## Vous cherchez à en apprendre plus ?

Voici quelques autres choses pour vous aider à commencer avec les fondamentaux du développement !

* [Qu'est-ce que Gatsby et pourquoi est-il temps de monter dans le train de la hype ?](https://www.colbyfayock.com/2019/09/what-is-gatsby-and-why-its-time-to-get-on-the-hype-train)
* [Qu'est-ce que le JAMstack et comment commencer ?](https://www.colbyfayock.com/2020/02/what-is-the-jamstack-and-how-do-i-get-started)
* [Comment devenir un développeur web full stack en 2020](https://www.colbyfayock.com/2020/02/how-to-become-a-full-stack-web-developer-in-2020)
* [Posez le Javascript - Apprenez HTML & CSS](https://www.colbyfayock.com/2019/08/put-down-the-javascript-learn-html-css)
* [Préparez votre futur vous pour le succès avec de bonnes habitudes de codage](https://www.colbyfayock.com/2020/04/set-future-you-up-for-success-with-good-coding-habits)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f3fb Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>