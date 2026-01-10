---
title: Comment utiliser GitHub Actions pour déployer un site Next.js sur AWS S3
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-11-02T19:27:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-actions-to-deploy-a-next-js-website-to-aws-s3
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/actions-s3.jpg
tags:
- name: AWS
  slug: aws
- name: continuous deployment
  slug: continuous-deployment
- name: GitHub Actions
  slug: github-actions
- name: Next.js
  slug: nextjs
seo_title: Comment utiliser GitHub Actions pour déployer un site Next.js sur AWS S3
seo_desc: "The beauty of Next.js and static web apps is that they let you run the\
  \ project pretty much anywhere using object storage, like on AWS S3. But it can\
  \ be a pain to manually update those files each time. \nHow can we use GitHub Actions\
  \ to automate and co..."
---

La beauté de Next.js et des applications web statiques est qu'elles vous permettent d'exécuter le projet pratiquement n'importe où en utilisant le stockage d'objets, comme sur AWS S3. Mais il peut être fastidieux de mettre à jour manuellement ces fichiers à chaque fois.

Comment pouvons-nous utiliser GitHub Actions pour automatiser et déployer en continu notre application sur S3 ?

* [Qu'est-ce que GitHub Actions ?](#heading-questce-que-github-actions)
* [Qu'est-ce que le déploiement continu ?](#heading-questce-que-le-deploiement-continu)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Configuration d'un nouveau projet Next.js sur GitHub](#heading-etape-0-configuration-dun-nouveau-projet-nextjs-sur-github)
* [Étape 1 : Création et déploiement manuel d'un projet Next.js vers un nouveau bucket S3](#heading-etape-1-creation-et-deploiement-manuel-dun-projet-nextjs-vers-un-nouveau-bucket-s3)
* [Étape 2 : Création d'un nouveau workflow GitHub Action pour construire automatiquement un projet Next.js](#heading-etape-2-creation-dun-nouveau-workflow-github-action-pour-construire-automatiquement-un-projet-nextjs)
* [Étape 3 : Configuration d'une GitHub Action pour déployer un site web statique sur S3](#heading-etape-3-configuration-dune-github-action-pour-deployer-un-site-web-statique-sur-s3)

%[https://www.youtube.com/watch?v=D3h91EvRxuk]

## Qu'est-ce que GitHub Actions ?

GitHub Actions est un service gratuit de GitHub qui nous permet d'automatiser des tâches de code.

J'ai [précédemment écrit](https://www.freecodecamp.org/news/what-are-github-actions-and-how-can-you-automate-tests-and-slack-notifications/) sur la façon dont nous pouvons les utiliser pour automatiser des tâches comme l'exécution de tests sur notre code et l'envoi de notifications à Slack.

Ils fournissent un moyen flexible d'exécuter automatiquement du code basé sur nos workflows existants. Cela offre de nombreuses possibilités, comme même le déploiement de notre site web !

## Qu'est-ce que AWS S3 ?

[S3](https://aws.amazon.com/s3/) (Simple Storage Service) est un service de stockage d'objets d'AWS. Il vous permet de stocker des fichiers dans le cloud facilement, les rendant disponibles dans le monde entier.

Il vous permet également d'utiliser ces fichiers comme un site web. Parce que nous pouvons télécharger un fichier HTML en tant qu'objet, nous pouvons également configurer S3 pour accéder à ce fichier en tant que requête HTTP. Cela signifie que nous pouvons [héberger un site web entier directement dans S3](https://www.freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront/).

## Qu'est-ce que le déploiement continu ?

Le déploiement continu, souvent appelé par son acronyme CD, est la pratique de maintenir le code dans un état déployable et de déployer ce code automatiquement ou en cycles courts.

Particulièrement dans notre cas d'utilisation, nous allons configurer notre projet de sorte que chaque fois qu'une nouvelle mise à jour est poussée ou fusionnée dans la branche principale de Git, notre site web sera déployé.

## Que allons-nous construire ?

Nous allons d'abord démarrer une application simple [Next.js](https://nextjs.org/) en utilisant le modèle de démarrage par défaut de Next.js et la configurer pour compiler en fichiers statiques.

Si vous ne souhaitez pas créer un projet Next.js, vous pouvez suivre avec même un simple fichier HTML et ne pas exécuter de commandes de construction. Mais Next.js est une manière moderne de construire des applications web dynamiques, donc nous commencerons par là.

Avec les fichiers de notre site web prêts à l'emploi, nous créerons et configurerons un bucket S3 dans AWS où nous hébergerons notre site web.

Enfin, nous créerons un nouveau workflow GitHub Action qui mettra automatiquement à jour les fichiers du site web dans S3 chaque fois qu'un nouveau changement se produit sur notre branche principale (`main`).

## Étape 0 : Configuration d'un nouveau projet Next.js sur GitHub

Nous allons commencer avec le modèle par défaut de Next.js.

Après avoir navigué vers le répertoire où vous souhaitez créer votre projet, exécutez :

```
yarn create next-app my-static-website
# ou
npx create-next-app my-static-website

```

Note : N'hésitez pas à remplacer `my-static-website` par le nom de votre choix. Nous l'utiliserons pour le reste de ce tutoriel.

Si vous naviguez vers ce répertoire et exécutez la commande de développement, vous devriez pouvoir démarrer avec succès votre serveur de développement.

```
cd my-static-website
yarn dev
# ou
npm run dev

```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/new-nextjs-app.jpg)
_Nouvelle application Next.js_

Ensuite, configurons notre projet pour qu'il compile statiquement.

À l'intérieur du fichier `package.json`, mettez à jour le script `build` avec :

```json
"build": "next build && next export",

```

Ce que cela fera, c'est dire à Next de prendre le site web et de l'exporter en fichiers statiques, que nous utiliserons pour héberger le site.

Nous pouvons tester cela en exécutant la commande :

```
yarn build
# ou
npm run build

```

Et une fois terminé, nous pouvons regarder à l'intérieur du répertoire `out` et voir tous les fichiers de notre nouveau site web.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-build-export-output.jpg)
_Sortie statique de Next.js_

Enfin, nous voulons héberger cela sur GitHub.

À l'intérieur de votre compte GitHub, [créez un nouveau dépôt](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/create-a-repo). Cela fournira ensuite des instructions sur la façon dont vous pouvez [ajouter un projet existant](https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) à ce dépôt.

Et une fois que vous avez poussé votre projet vers GitHub, nous devrions être prêts à configurer notre nouveau projet de site web !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/project-on-github.jpg)
_Nouveau dépôt dans GitHub_

Suivez les commits :

* [Ajout du projet initial Next.js](https://github.com/colbyfayock/my-static-website/commit/ca9e4bca3c37fbd8553b0b183890c32836c35296) via [Create Next App](https://nextjs.org/docs/api-reference/create-next-app)
* [Configuration de Next.js pour exporter le projet](https://github.com/colbyfayock/my-static-website/commit/7907f4a0fac5f0aed2922202c5f0070dfc055f83)

## Étape 1 : Création et déploiement manuel d'un projet Next.js vers un nouveau bucket S3

Pour commencer avec notre nouveau bucket S3, connectez-vous d'abord à votre compte AWS et naviguez vers le service S3.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/aws-s3-console.jpg)
_Aucun bucket dans S3_

Nous allons vouloir créer un nouveau bucket, en utilisant le nom de notre choix, qui sera utilisé pour le point de terminaison S3 où notre site web est hébergé. Nous allons également vouloir configurer notre bucket S3 pour qu'il puisse héberger un site web.

_Note : ce tutoriel ne vous guidera pas à travers le processus d'hébergement d'un site web sur S3, mais vous pouvez consulter mon autre tutoriel qui vous [guidera à travers l'hébergement d'un site web sur S3](https://www.freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront/) étape par étape._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/s3-bucket-website-hosting.jpg)
_Hébergement de site web statique dans AWS S3_

Une fois que nous avons configuré notre bucket S3 en tant que site web, nous pouvons revenir à notre dossier de projet Next.js, exécuter notre commande de construction, puis télécharger tous nos fichiers du répertoire `out` dans notre nouveau bucket S3.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/website-files-in-s3.jpg)
_Bucket S3 avec application statique_

Et une fois que ces fichiers sont téléchargés et que nous avons configuré notre bucket S3 pour l'hébergement de site web, nous devrions maintenant pouvoir voir notre projet en direct sur le web !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-s3-website.jpg)
_Application Next.js hébergée sur AWS S3_

## Étape 2 : Création d'un nouveau workflow GitHub Action pour construire automatiquement un projet Next.js

Pour commencer, nous allons devoir créer un nouveau workflow.

Si vous êtes familier avec GitHub Actions, vous pourriez en créer un manuellement, mais nous allons rapidement passer en revue comment faire cela dans l'interface utilisateur.

Naviguez vers l'onglet Actions de votre dépôt GitHub et cliquez sur "set up a workflow yourself".

![Image](https://www.freecodecamp.org/news/content/images/2020/10/github-actions-new-workflow.jpg)
_Nouveau workflow GitHub Action_

GitHub fournit un modèle de départ que nous pouvons utiliser pour notre workflow, bien que nous voulions apporter quelques modifications.

Faisons ce qui suit :

* Optionnel : renommez le fichier en deploy.yml
* Optionnel : renommez le workflow en CD (car il est un peu différent de CI)
* Optionnel : supprimez tous les commentaires pour le rendre un peu plus facile à lire
* Supprimez la définition `pull_request` dans la propriété `on`
* Supprimez toutes les `steps` sauf `uses: actions/checkout@v2`

À ce stade, nous devrions être laissés avec :

```yaml
name: CD

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

```

Ce code seul déclenchera un processus qui lance une nouvelle instance d'Ubuntu et vérifie simplement le code depuis GitHub chaque fois qu'il y a un nouveau changement poussé vers la branche `main`.

Ensuite, une fois que nous avons notre code vérifié, nous voulons le construire. Cela nous permettra de prendre cette sortie et de la synchroniser avec S3.

Cette étape différera légèrement selon que vous utilisez yarn ou npm pour votre projet.

Si vous utilisez yarn, sous la définition `steps`, ajoutez ce qui suit :

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: 12
- run: npm install -g yarn
- run: yarn install --frozen-lockfile
- run: yarn build

```

Si vous utilisez npm, ajoutez ce qui suit :

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: 12
- run: npm ci
- run: npm run build

```

Entre ces deux ensembles d'étapes, ce que nous faisons est :

* Configuration de node : cela permet d'utiliser npm et node pour installer et exécuter nos scripts
* Installation de Yarn (Yarn uniquement) : si nous utilisons yarn, nous l'installons en tant que dépendance globale afin de pouvoir l'utiliser
* Installation des dépendances : nous installons nos dépendances et utilisons une commande spécifique qui garantit l'utilisation du fichier de verrouillage disponible pour éviter toute mise à jour de package inattendue
* Construction : enfin, nous exécutons notre commande de construction qui compilera notre projet Next.js dans le répertoire `out` !

Et maintenant, nous pouvons commiter ce fichier directement dans notre branche `main`, ce qui lancera une nouvelle exécution de notre workflow que nous pouvons voir dans notre onglet Actions.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/github-action-run-workflow.jpg)
_Nouveau workflow dans GitHub Actions_

Pour voir que cela fonctionne, nous pouvons naviguer dans cette exécution, sélectionner notre workflow et voir que toutes nos étapes se sont exécutées, y compris la construction de notre projet !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/github-action-successful-build.jpg)
_Logs de construction réussie pour un workflow GitHub Action_

[Suivez le commit !](https://github.com/colbyfayock/my-static-website/commit/59e0a5158d6afbf54793d826d05455f5205c98fb)

## Étape 3 : Configuration d'une GitHub Action pour déployer un site web statique sur S3

Maintenant que nous construisons notre projet automatiquement, nous voulons mettre à jour automatiquement notre site web dans S3.

Pour cela, nous allons utiliser l'action GitHub [aws-actions/configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials) et l'AWS CLI.

L'action GitHub que nous utilisons prendra nos identifiants et configuration AWS et les rendra disponibles pour une utilisation tout au long du cycle de vie du workflow.

À l'heure actuelle, l'instance Ubuntu que GitHub Actions fournit nous permet d'utiliser l'AWS CLI car elle est incluse. Nous pourrons donc utiliser les commandes CLI directement dans notre workflow.

Alternativement, nous pourrions utiliser l'action [S3 Sync action](https://github.com/jakejarvis/s3-sync-action). Mais en utilisant l'AWS CLI, nous gagnons plus de flexibilité pour personnaliser notre configuration, nous pouvons l'utiliser pour des commandes CLI supplémentaires, et il est également généralement agréable de se familiariser avec l'AWS CLI.

Pour commencer, ajoutons l'extrait suivant en tant qu'étapes supplémentaires dans notre workflow :

```yaml
- uses: aws-actions/configure-aws-credentials@v1
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: us-east-1

```

Ce que le code ci-dessus fera, c'est utiliser l'action de configuration des identifiants AWS pour configurer notre clé d'accès AWS, notre clé secrète et notre région en fonction de nos paramètres.

La région AWS peut être personnalisée selon la région que vous utilisez généralement avec votre compte AWS. Je suis dans le nord-est des États-Unis, donc je garderai `us-east-1`.

La clé d'accès et la clé secrète sont des identifiants que vous devrez générer avec votre compte AWS. La manière dont notre code est configuré est que nous stockerons ces valeurs à l'intérieur des secrets GitHub, ce qui empêchera ces clés d'être divulguées. Lorsque l'action s'exécute, GitHub transforme ces valeurs en étoiles (`***`) pour que les gens ne puissent pas accéder à ces clés.

Pour configurer ces secrets, nous devons d'abord générer des clés d'accès dans AWS.

Naviguez vers la console AWS. Dans le menu utilisateur, sélectionnez **Mes identifiants de sécurité**, puis sélectionnez **Créer une clé d'accès**.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/aws-console-create-access-key.jpg)
_Création d'une clé d'accès dans AWS_

Cela vous fournira deux valeurs : l'**ID de la clé d'accès** et la **clé d'accès secrète**. Enregistrez ces valeurs, car vous ne pourrez plus accéder à l'ID de la clé secrète.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/aws-secret-access-keys.jpg)
_Trouver la clé secrète et la clé d'accès dans AWS_

_Note : n'oubliez pas de NE PAS inclure la clé d'accès et la clé secrète à l'intérieur de votre code. Cela pourrait conduire quelqu'un à compromettre vos identifiants AWS._

Ensuite, à l'intérieur du dépôt GitHub, naviguez vers Paramètres, Secrets, puis sélectionnez Nouveau secret.

Ici, nous voulons ajouter nos clés AWS en utilisant les secrets suivants :

* AWS_ACCESS_KEY_ID : votre ID de clé d'accès AWS
* AWS_SECRET_ACCESS_KEY : votre clé secrète AWS

Et une fois enregistrés, vous devriez avoir vos deux nouveaux secrets.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/github-secrets-access-keys.jpg)
_Création de secrets dans GitHub_

Maintenant que nous avons configuré nos identifiants, nous devrions être prêts à exécuter la commande pour synchroniser notre projet avec S3.

À l'intérieur de l'action GitHub, ajoutez l'étape suivante :

```yaml
- run: aws s3 sync ./out s3://[bucket-name]

```

_Note : assurez-vous de remplacer `[bucket-name]` par le nom de votre bucket S3._

Cette commande déclenchera une synchronisation avec notre bucket S3 spécifié, en utilisant le contenu du répertoire `out`, qui est l'endroit où notre projet est construit.

Et maintenant, si nous validons nos changements, nous pouvons voir que notre action est automatiquement déclenchée une fois validée dans la branche `main`, où nous construisons notre projet et le synchronisons avec S3 !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/github-action-sync-s3-bucket.jpg)
_Synchronisation réussie avec AWS S3 dans le workflow GitHub Action_

_Note : Assurez-vous que avant de configurer cette action, vous avez configuré le bucket S3 pour héberger un site web (y compris le déblocage des permissions sur le bucket S3) – sinon cette action pourrait échouer._

À ce stade, notre projet ressemble probablement au même, car nous n'avons apporté aucune modification au code.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-s3-website.jpg)
_Application Next.js sur AWS S3_

Mais si vous apportez une modification de code, comme changer le titre de la page d'accueil à l'intérieur de `pages/index.js` et valider cette modification :

```jsx
<h1 className={styles.title}>
  Le site Next.js de Colby <a href="https://nextjs.org">Next.js!</a>
</h1>

```

Nous pouvons voir que notre modification déclenche le workflow :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/github-action-commit-workflow.jpg)
_Nouveau workflow GitHub Action à partir d'une modification de code_

Et une fois que notre workflow est terminé, nous pouvons voir que notre contenu est maintenant automatiquement mis à jour sur notre site web :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/updated-nextjs-site-title.jpg)
_Application hébergée sur AWS S3 avec les modifications de code mises à jour_

Suivez les commits :

* [Ajout de la configuration AWS et de la commande de synchronisation S3](https://github.com/colbyfayock/my-static-website/commit/f891412b827aca4b06e9bf3de8e4e5b4c5704fc8)
* [Mise à jour du titre pour tester le workflow](https://github.com/colbyfayock/my-static-website/commit/bb9b981416645e35c6d3442e02d6b61f2ba032d2)

## Que pouvons-nous faire d'autre ?

### Configuration de CloudFront

Le but de cet article n'était pas de passer par l'ensemble du processus de configuration d'un site web pour AWS, mais si vous servez un site web sur S3, vous pourriez également vouloir inclure CloudFront devant celui-ci.

Vous pouvez consulter [mon autre guide](https://www.freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront/) ici, qui vous guide à travers la configuration de CloudFront ainsi qu'un guide étape par étape pour créer le site dans S3.

### Invalidation du cache CloudFront

Si votre site web S3 est derrière CloudFront, il y a des chances que vous souhaitiez vous assurer que CloudFront ne met pas en cache les nouvelles modifications.

Avec l'AWS CLI, nous pouvons également déclencher une invalidation de cache avec CloudFront pour nous assurer qu'il récupère les dernières modifications.

[Consultez la documentation ici](https://docs.aws.amazon.com/cli/latest/reference/cloudfront/create-invalidation.html) pour en savoir plus.

### Déploiements de pull request

Si vous travaillez constamment sur des modifications de site web dans une pull request, il peut parfois être plus facile de voir les modifications en direct.

Vous pouvez configurer un nouveau workflow qui ne s'exécute que sur les pull requests, où le workflow peut créer dynamiquement un nouveau bucket basé sur la branche ou l'environnement et ajouter un commentaire à la pull request avec cette URL.

Vous pourriez trouver une GitHub Action qui existe pour gérer les commentaires sur la pull request pour vous ou vous pouvez consulter la [documentation GitHub Actions](https://docs.github.com/en/free-pro-team@latest/rest/reference/actions).

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">F426 Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">F3A5 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 FE0F Inscrivez-vous à ma newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">F49D Parrainez-moi</a>
    </li>
  </ul>
</div>