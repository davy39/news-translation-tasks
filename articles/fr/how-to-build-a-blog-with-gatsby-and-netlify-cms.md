---
title: Comment créer un blog avec Gatsby et Netlify CMS – Un guide complet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-06T15:16:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-blog-with-gatsby-and-netlify-cms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c984e740569d1a4ca1946.jpg
tags:
- name: blog
  slug: blog
- name: cms
  slug: cms
- name: Gatsby
  slug: gatsby
- name: Netlify
  slug: netlify
- name: Web Development
  slug: web-development
seo_title: Comment créer un blog avec Gatsby et Netlify CMS – Un guide complet
seo_desc: 'By Mohammed Asker

  In this article, we are going to build a blog with Gatsby and Netlify CMS. You will
  learn how to install Gatsby on your computer and use it to quickly develop a super
  fast blog site.

  You are also going to learn how to add Netlify CM...'
---

Par Mohammed Asker

Dans cet article, nous allons créer un blog avec Gatsby et Netlify CMS. Vous apprendrez comment installer Gatsby sur votre ordinateur et l'utiliser pour développer rapidement un site de blog super rapide.

Vous allez également apprendre comment ajouter Netlify CMS à votre site en créant et en configurant des fichiers, puis en connectant le CMS à votre site via l'authentification utilisateur.

Et enfin, vous apprendrez comment accéder à l'admin du CMS afin de pouvoir écrire votre premier article de blog.

Le code complet de ce projet peut être trouvé [ici](https://github.com/mohammedasker/foodblog).

Voici une brève introduction à ces outils.

## Qu'est-ce que Gatsby ?

[Gatsby](https://www.gatsbyjs.com/) est un framework gratuit et open-source basé sur React qui vous aide à construire des sites web et des applications web rapides. C'est également un générateur de sites statiques comme Next.js, Hugo et Jekyll.

Il inclut le SEO (Search Engine Optimization), l'accessibilité et l'optimisation des performances dès le départ. Cela signifie qu'il vous faudra moins de temps pour construire des applications web prêtes pour la production que si vous construisiez avec React seul.

## Qu'est-ce que Netlify CMS ?

[Netlify CMS](https://www.netlifycms.org/) est un CMS (Content Management System) pour les générateurs de sites statiques. Il est construit par les mêmes personnes qui ont fait [Netlify](https://www.netlify.com/). Il vous permet de créer et d'éditer du contenu comme si c'était WordPress, mais avec une interface beaucoup plus simple et conviviale.

Le principal avantage de Netlify CMS est que vous n'avez pas à créer de fichiers markdown à chaque fois que vous voulez écrire un article. Cela est utile pour les rédacteurs de contenu qui ne veulent pas avoir à gérer du code, des éditeurs de texte, des dépôts et tout ce qui a trait à la technologie - ils peuvent simplement se concentrer sur l'écriture d'articles.

Très bien, sans plus attendre, commençons à construire le blog !

**Mais avant de commencer, un petit avertissement** : Ce guide nécessite des connaissances préalables en JavaScript et React. Si vous n'êtes pas encore à l'aise avec ces outils, j'ai lié les ressources à la fin de l'article pour vous aider à vous rafraîchir sur ces compétences.

Même si vous êtes nouveau dans ces technologies, j'ai essayé de rendre ce guide aussi simple que possible afin que vous puissiez suivre.

## Comment configurer l'environnement

Avant de pouvoir construire des sites Gatsby, nous devons nous assurer que nous avons installé tous les logiciels nécessaires pour le blog.

### Installer Node.js

Node.js est un environnement qui peut exécuter du code JavaScript en dehors d'un navigateur web.

C'est un outil qui vous permet d'écrire du code serveur backend au lieu d'utiliser d'autres langages de programmation tels que Python, Java ou PHP. Gatsby est construit avec Node.js et c'est pourquoi nous devons l'installer sur notre ordinateur.

Pour installer Node.js, allez sur la [page de téléchargement](https://nodejs.org/en/download/) et téléchargez-le en fonction de votre système d'exploitation.

Lorsque vous avez terminé de suivre les invites d'installation, ouvrez le terminal et exécutez `node -v` pour vérifier si l'installation s'est déroulée correctement. Actuellement, la version doit être 12.18.4 ou supérieure.

### Installer Git

Git est un système de contrôle de version distribué gratuit et open-source qui vous aide à gérer vos projets de codage de manière efficace.

Gatsby starter utilise Git pour télécharger et installer ses fichiers requis et c'est pourquoi vous devez avoir Git sur votre ordinateur.

Pour installer Git, suivez les instructions en fonction de votre système d'exploitation :

* [Installer Git sur Mac OS](https://www.atlassian.com/git/tutorials/install-git#mac-os-x)
* [Installer Git sur Windows](https://www.atlassian.com/git/tutorials/install-git#windows)
* [Installer Git sur Linux](https://www.atlassian.com/git/tutorials/install-git#linux)

### Installer Gatsby CLI

Gatsby CLI (Command Line Interface) est l'outil qui vous permet de construire des sites alimentés par Gatsby. En exécutant cette commande, nous pouvons installer n'importe quel site Gatsby et les plugins que nous voulons.

Pour installer Gatsby CLI, ouvrez le terminal et exécutez cette commande :

```
npm install -g gatsby-cli

```

Une fois que tout est configuré avec succès, nous sommes prêts à construire notre premier site Gatsby.

## Comment construire un site Gatsby

Dans ce guide, nous allons utiliser le thème de démarrage par défaut de Gatsby, mais vous êtes libre de choisir n'importe quel thème dans la [bibliothèque de démarrage de Gatsby](https://www.gatsbyjs.com/starters/?v=2). Personnellement, j'utilise le [thème Lekoart](https://github.com/LekoArts/gatsby-starter-minimal-blog) car le design est minimaliste et beau, et il a un mode sombre.

Dans le terminal, exécutez cette commande pour installer le nouveau blog Gatsby :

```
gatsby new foodblog https://github.com/gatsbyjs/gatsby-starter-blog

```

**Note pour les utilisateurs de Windows** : Si vous rencontrez l'erreur "Error: Command failed with exit code 1: yarnpkg" lors de la création du site Gatsby, consultez [cette page](https://github.com/gatsbyjs/gatsby/issues/26804) pour le dépannage. Vous devrez peut-être nettoyer les dépendances des anciennes installations de yarn ou suivre les instructions de Gatsby sur Windows.

Que signifie exactement cette ligne de commande ? Laissez-moi expliquer.

* **new** - C'est la ligne de commande qui crée un nouveau projet Gatsby
* **foodblog** - C'est le nom du projet. Vous pouvez le nommer comme vous voulez ici. J'ai nommé ce projet _foodblog_ uniquement à titre d'exemple.
* **L'URL** ([https://github.com/gatsbyjs/gatsby-starter-blog](https://github.com/gatsbyjs/gatsby-starter-blog)) - Cette URL spécifiée pointe vers un dépôt de code qui contient le code de démarrage que vous souhaitez utiliser. En d'autres termes, j'ai choisi le thème pour le projet.

Une fois l'installation terminée, nous exécuterons la commande `cd foodblog` qui nous emmènera à l'emplacement de notre fichier de projet.

```
cd foodblog

```

Ensuite, nous exécuterons `gatsby develop` qui commencera à s'exécuter sur la machine locale. Selon les spécifications de votre ordinateur, cela prendra un peu de temps avant qu'il ne soit complètement démarré.

```
gatsby develop

```

Ouvrez un nouvel onglet dans votre navigateur et allez à `http://localhost:8000/`. Vous devriez maintenant voir votre nouveau site Gatsby !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--33-.png)
_À quoi ressemble la page d'accueil d'un blog de démarrage Gatsby_

Maintenant que nous avons créé le blog, l'étape suivante consiste à ajouter Netlify CMS pour faciliter l'écriture des articles de blog.

## Comment ajouter Netlify CMS à votre site

L'ajout de Netlify CMS à votre site Gatsby implique 4 étapes majeures :

* structure des fichiers de l'application,
* configuration,
* authentification, et
* accès au CMS.

Abordons chacune de ces étapes une par une.

### Comment configurer la structure des fichiers de l'application

Cette section traite de la structure des fichiers de votre projet. Nous allons créer des fichiers qui contiendront tous les codes de Netlify CMS.

Lorsque vous ouvrez votre éditeur de texte, vous verrez beaucoup de fichiers. Vous pouvez lire [cet article](https://github.com/gatsbyjs/gatsby-starter-blog#-whats-inside) si vous êtes curieux de savoir ce que fait chacun de ces fichiers.

```
 node_modules
 src
 static
 .gitignore
 .prettierrc
 gatsby-browser.js
 gatsby-config.js
 gatsby-node.js
 gatsby-ssr.js
 LICENSE
 package-lock.json
 package.json
 README.md

```

Ne vous inquiétez pas de tous ces fichiers — nous allons en utiliser très peu ici.

Ce que nous cherchons, c'est le dossier `static`. C'est le dossier où se formera la structure principale de Netlify CMS.

Si votre projet ne contient pas de dossier `Static`, créez le dossier à la racine de votre projet.

À l'intérieur du dossier `static`, créez un dossier `admin`. À l'intérieur de ce dossier, créez deux fichiers `index.html` et `config.yml` :

```
admin
  index.html
  config.yml

```

Le premier fichier, `index.html`, est le point d'entrée de votre admin CMS. C'est là que vit Netlify CMS. Vous n'avez pas besoin de faire de style ou quoi que ce soit car c'est déjà fait pour vous avec la balise script dans l'exemple ci-dessous :

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Content Manager</title>
</head>
<body>
  <script src="https://unpkg.com/netlify-cms@^2.0.0/dist/netlify-cms.js"></script>
</body>
</html>

```

Le deuxième fichier, `config.yml`, est le cœur principal de Netlify CMS. Cela va être un peu compliqué car nous allons écrire du code backend. Nous en parlerons plus dans la section configuration.

### Comment configurer le backend

Dans ce guide, nous utilisons Netlify pour l'hébergement et l'authentification, donc le processus de configuration du backend devrait être relativement simple. Ajoutez tous les extraits de code de cette section à votre fichier `admin/config.yml`.

Nous allons commencer par ajouter les codes suivants :

```yml
backend:
  name: git-gateway
  branch: master

```

**Attention** : Ce code ci-dessus fonctionne pour les dépôts GitHub et GitLab. Si vous utilisez Bitbucket pour héberger votre dépôt, suivez plutôt ces [instructions](https://www.netlifycms.org/docs/bitbucket-backend/).

Le code que nous venons d'écrire spécifie votre protocole backend et votre branche de publication (qui est branch: master). Git Gateway est une API open-source qui agit comme un proxy entre les utilisateurs authentifiés de votre site et votre dépôt de site. J'expliquerai plus en détail ce que cela fait dans la section authentification.

Ensuite, nous allons écrire `media_folder: "images/uploads"`. Cela vous permettra d'ajouter des fichiers multimédias comme des photos directement à votre CMS. Vous n'aurez alors plus besoin d'utiliser un éditeur de texte pour ajouter manuellement des médias et tout le reste.

```yml
media_folder: "images/uploads"

```

Assurez-vous d'avoir créé un dossier appelé `images` dans le dossier `admin`. À l'intérieur du dossier `images`, créez un dossier `uploads` car c'est l'endroit où vous hébergerez vos images.

### Configurer les Collections

Les collections définiront la structure pour les différents types de contenu sur votre site statique. Comme chaque site peut être différent, la manière dont vous configurez les paramètres de la collection différera d'un site à l'autre.

Disons simplement que votre site a un blog, avec les articles stockés dans `content/blog`, et les fichiers enregistrés dans un format date-titre, comme `2020-09-26-comment-faire-des-sandwichs-comme-un-pro.md`. Chaque article commence par des paramètres dans la matière frontale formatée YAML de cette manière :

```md
---
layout: blog
title: "Comment faire des sandwichs comme un pro"
date: 2020-09-26 11:59:59
thumbnail: "/images/sandwich.jpg"
---

C'est le corps de l'article où j'écris comment faire un sandwich si bon qu'il impressionnera Gordon Ramsay.

```

Avec cet exemple ci-dessus, voici comment vous ajouterez les paramètres `collections` à votre fichier `config.yml` de Netlify CMS :

```yml
collections:
  - name: "blog"
    label: "Blog"
    folder: "content/blog"
    create: true
    slug: "{{year}}-{{month}}-{{day}}-{{slug}}"
    fields:
      - {label: "Layout", name: "layout", widget: "hidden", default: "blog"}
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Publish Date", name: "date", widget: "datetime"}
      - {label: "Body", name: "body", widget: "markdown"}

```

Examinons ce que fait chacun de ces champs :

* `name` : Celui-ci est utilisé dans les routes comme /admin/collections/blog
* `label` : Celui-ci est utilisé dans l'UI (Interface Utilisateur). Lorsque vous êtes dans la page admin, vous verrez un grand mot "Blog" en haut de l'écran. Ce grand mot "Blog" est le label.
* `folder` : Celui-ci pointe vers le chemin du fichier où vos articles de blog sont stockés.
* `create` : Celui-ci permet à l'utilisateur (vous ou toute personne ayant un accès admin) de créer de nouveaux documents (articles de blog dans ce cas) dans ces collections.
* `slug` : Celui-ci est le modèle pour les noms de fichiers. `{{year}}`, `{{month}}`, et `{{day}}` qui sont tirés du champ de date de l'article ou de la date d'enregistrement. `{{slug}}` est une version URL-safe du titre de l'article. Par défaut, c'est `{{slug}}`.

Les champs sont l'endroit où vous pouvez personnaliser l'éditeur de contenu (la page où vous écrivez l'article de blog). Vous pouvez ajouter des éléments comme des notes (1-5), des images en vedette, des méta-descriptions, et ainsi de suite.

Par exemple, dans ce code particulier, nous ajoutons des accolades `{}`. À l'intérieur, nous écrivons `label` avec la valeur "Publish Date" qui sera le label dans l'UI de l'éditeur.

Le champ `name` est le nom du champ dans la matière frontale et nous le nommons "date" puisque le but de ce champ est d'entrer la date.

Et enfin, le widget détermine comment le style de l'UI apparaîtra et le type de données que nous pouvons entrer. Dans ce cas, nous avons écrit `"datetime"` ce qui signifie que nous ne pouvons entrer que la date et l'heure.

```yml
- {label: "Publish Date", name: "date", widget: "datetime"}

```

Vous pouvez consulter la liste juste [ici](https://www.netlifycms.org/docs/widgets/) pour voir exactement ce que vous pouvez ajouter. Si vous le souhaitez, vous pouvez même créer vos propres widgets. Pour des raisons de brièveté, nous allons essayer de garder les choses simples ici.

### Activer l'authentification

À ce stade, nous avons presque terminé l'installation et la configuration de Netlify CMS. Il est maintenant temps de connecter votre site Gatsby au CMS en activant l'authentification.

Nous allons ajouter un peu de code HTML puis activer certaines fonctionnalités de Netlify. Après cela, vous êtes sur le point de créer votre premier article de blog.

Nous allons avoir besoin d'un moyen de connecter une interface frontale au backend afin que nous puissions gérer l'authentification. Pour cela, ajoutez cette balise de script HTML à deux fichiers :

```html
<script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>

```

Le premier fichier à ajouter cette balise de script est le fichier `admin/index.html`. Placez-le entre les balises `<head>`. Et le deuxième fichier à ajouter la balise est le fichier `public/index.html`. Celui-ci va également entre les balises `<head>`.

Lorsque l'utilisateur se connecte avec le widget Netlify Identity, un jeton d'accès le dirige vers la page d'accueil du site. Afin de compléter la connexion et de revenir au CMS, redirigez l'utilisateur vers le chemin `/admin/`.

Pour cela, ajoutez le code suivant avant la balise de fermeture `body` du fichier `public/index.html` :

```html
<script>
  if (window.netlifyIdentity) {
    window.netlifyIdentity.on("init", user => {
      if (!user) {
        window.netlifyIdentity.on("login", () => {
          document.location.href = "/admin/";
        });
      }
    });
  }
</script>

```

Avec cela, nous avons maintenant terminé d'écrire le code et il est temps de visiter Netlify pour activer l'authentification.

Avant de continuer, vous devriez valider vos changements avec Git et les pousser vers le dépôt. De plus, vous devrez déployer votre site en direct afin de pouvoir accéder aux fonctionnalités dans la section Activer Identity et Git Gateway.

## Déployer votre site en direct avec Netlify

Nous allons utiliser Netlify pour déployer notre site Gatsby en direct. Le processus de déploiement est assez simple, rapide et surtout, il est livré avec un SSL gratuit (Secure Sockets Layer). Cela signifie que votre site est protégé (vous pouvez le voir en regardant le cadenas vert sur la recherche du navigateur).

Si vous ne vous êtes pas encore inscrit sur la plateforme, vous pouvez le faire [ici](https://app.netlify.com/signup?_ga=2.69477016.986166254.1601369549-1254573554.1571849986). Lorsque vous avez terminé l'inscription, vous pouvez commencer le processus de déploiement en suivant ces 3 étapes.

1. Cliquez sur le bouton "New site from Git" pour créer un nouveau site à déployer. Choisissez le fournisseur Git où votre site est hébergé. Mon site est hébergé sur GitHub, c'est donc ce que je vais choisir.
2. Choisissez le dépôt que vous souhaitez connecter à Netlify. Le nom de mon site Gatsby est "foodblog" mais vous devez choisir votre propre nom de projet.
3. La dernière étape demande comment vous souhaitez que Netlify ajuste vos builds et déploie votre site. Nous allons tout laisser tel quel et nous cliquerons sur le bouton "Deploy site". Cela commencera à déployer votre site en direct.

Une fois le déploiement terminé, vous pouvez visiter votre site en direct en cliquant sur le lien vert qui a été généré pour vous en haut à gauche de l'écran. Exemple : `https://random_characters.netlify.app`.

Avec cela, le monde peut maintenant voir votre site. Vous pouvez remplacer l'URL étrange par votre domaine personnalisé en lisant cette [documentation](https://docs.netlify.com/domains-https/custom-domains/#definitions).

### Comment activer Identity et Git Gateway

Les services Identity et Git Gateway de Netlify vous aident à gérer les utilisateurs admin du CMS pour votre site sans qu'ils aient besoin d'avoir un compte avec votre hébergeur Git (comme GitHub) ou un accès de commit sur votre dépôt.

Pour activer ces services, rendez-vous sur le tableau de bord de votre site sur Netlify et suivez ces étapes :

1. Allez dans **Paramètres** > **Identity**, et sélectionnez **Activer le service Identity**.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--34-.png)
_Dans la page d'accueil de votre site, cliquez sur le lien "Paramètres"._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--36-.png)
_Après avoir cliqué sur "Paramètres", faites défiler la barre latérale de gauche et cliquez sur le lien "Identity"._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--37-.png)
_Cliquez sur le bouton "Activer Identity" pour activer la fonctionnalité Identity._

2. Sous les préférences **Inscription**, sélectionnez **Ouvert** ou **Sur invitation uniquement**. La plupart du temps, vous voulez que seuls les utilisateurs invités accèdent à votre CMS. Mais si vous expérimentez, vous pouvez le laisser ouvert pour plus de commodité.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--38-.png)
_Sous le sous-menu Identity, cliquez sur le lien "Inscription" et vous serez redirigé vers les préférences d'inscription._

3. Faites défiler jusqu'à **Services** > **Git Gateway**, et cliquez sur **Activer Git Gateway**. Cela authentifie avec votre hébergeur Git et génère un jeton d'accès API.

Dans ce cas, nous laissons le champ **Rôles** vide, ce qui signifie que tout utilisateur connecté peut accéder au CMS.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--40-.png)
_Sous le sous-menu Identity, cliquez sur le lien "Services"._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--41-.png)
_Cliquez sur le bouton "Activer Git Gateway" pour activer la fonctionnalité Git Gateway._

Avec cela, votre site Gatsby a été connecté avec Netlify CMS. Il ne reste plus qu'à accéder à l'admin du CMS et à écrire des articles de blog.

## Comment accéder au CMS

Très bien, vous êtes maintenant prêt à écrire votre premier article de blog !

Il y a deux façons d'accéder à votre admin CMS, selon les options d'accès que vous avez choisies dans Identity.

Si vous avez sélectionné **Sur invitation uniquement**, vous pouvez vous inviter vous-même et d'autres utilisateurs en cliquant sur le bouton Inviter un utilisateur. Un message email sera alors envoyé avec un lien d'invitation pour vous connecter à votre admin CMS. Cliquez sur le lien de confirmation et vous serez redirigé vers la page de connexion.

Alternativement, si vous avez sélectionné **Ouvert**, vous pouvez accéder directement à l'admin de votre site à l'adresse `yoursite.com/admin/`. Vous serez invité à créer un nouveau compte. Lorsque vous le soumettez, un lien de confirmation sera envoyé à votre email. Cliquez sur le lien de confirmation pour terminer le processus d'inscription et vous serez redirigé vers la page du CMS.

**Note** : Si vous ne pouvez pas accéder à votre admin CMS après avoir cliqué sur le lien de l'email, la solution consiste à copier le lien dans le navigateur commençant par `#confirmation_token=random_characters` et à coller le lien après le hashtag "#", comme ceci : `https://yoursite.com/admin/#confirmation_token=random_characters`. Cela devrait résoudre le problème.

Si tout se passe bien, vous devriez voir le tableau de bord admin de votre site :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--42-.png)
_Admin de Netlify CMS._

Vous pouvez créer votre nouvel article en cliquant sur le bouton "Nouvel article".

Lorsque vous êtes prêt à publier votre article, vous pouvez cliquer sur le bouton "Publier maintenant" pour le publier immédiatement.

Lorsque vous cliquez sur le bouton de publication, le fichier de l'article est automatiquement créé. Il sera ensuite ajouté aux modifications avec le message de commit basé sur le nom de l'article ainsi que la date et l'heure de publication. Enfin, il sera poussé vers le dépôt hôte, et à partir de là, votre article sera visible en direct.

Vous pouvez voir les modifications en regardant le message de commit dans votre dépôt hôte.

Après avoir attendu quelques minutes, votre nouvel article devrait être en ligne.

### Une dernière chose

La dernière chose à faire est de nettoyer les articles d'exemple. Pour supprimer ces articles, allez dans les fichiers du blog dans votre éditeur de texte et supprimez-les un par un. Assurez-vous de vérifier votre terminal lors de leur suppression afin qu'il n'y ait pas de problèmes sur votre site.

Une fois tous les articles d'exemple supprimés, validez ces modifications et poussez-les vers le dépôt.

Et maintenant, vous avez terminé ! Vous pouvez maintenant créer vos nouveaux articles depuis le tableau de bord confortable du CMS et partager vos histoires avec le monde.

## Résumé

Dans ce guide, vous avez appris comment :

* Créer un site de blog Gatsby
* Ajouter Netlify CMS à votre site Gatsby en créant et en configurant des fichiers
* Activer l'authentification utilisateur en activant Identity et Git Gateway
* Accéder à l'admin du CMS de votre site
* Publier votre premier article alimenté par Gatsby et Netlify CMS

À la fin de ce guide, vous devriez maintenant être en mesure de profiter de l'écriture d'articles de blog avec un site web rapide et un éditeur de contenu simple. Et vous n'aurez probablement pas à toucher au code sauf s'il a besoin d'une personnalisation supplémentaire.

Il reste encore beaucoup à couvrir sur Gatsby et Netlify CMS. L'une des meilleures façons d'en apprendre davantage est de consulter leur documentation.

J'espère que vous avez trouvé ce guide bénéfique, et bon blogging !

[Consultez mon blog](https://www.mohammedasker.com/) pour apprendre plus de conseils, astuces et tutoriels sur le développement web.

Photo de couverture par [NeONBRAND](https://unsplash.com/@neonbrand?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/blogging?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

### Ressources pour JavaScript et React

Voici quelques ressources qui peuvent vous aider à apprendre JavaScript et React :

**JavaScript**

* [Documentation officielle de JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [freeCodeCamp](https://www.freecodecamp.org/)
* [W3Schools : Tutoriel JavaScript](https://www.w3schools.com/js/)
* [JavaScript.info](https://javascript.info/)

**React**

* [Documentation officielle de React](https://reactjs.org/docs/getting-started.html)
* [Complete React Developer in 2020 (w/ Redux, Hooks, GraphQL)](https://www.udemy.com/course/complete-react-developer-zero-to-mastery/)
* [Scrimba : Apprendre React gratuitement](https://scrimba.com/learn/learnreact)
* [Flavio Copes : The React Handbook](https://flaviocopes.com/page/react-handbook/)