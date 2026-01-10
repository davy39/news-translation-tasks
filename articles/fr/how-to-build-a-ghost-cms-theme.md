---
title: Comment créer un thème personnalisé pour Ghost CMS
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2023-01-04T15:20:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-ghost-cms-theme
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/ghost-theme-development-.png
tags:
- name: blog
  slug: blog
- name: cms
  slug: cms
- name: Ghost
  slug: ghost-tag
- name: projects
  slug: projects
- name: writing
  slug: writing
seo_title: Comment créer un thème personnalisé pour Ghost CMS
seo_desc: "Ghost CMS is a platform specifically designed for bloggers and writers.\
  \ Using Ghost, you can quickly get a blog website up and running. \nGhost targets\
  \ primarily writers and all the features are specifically built for writing. \n\
  Ghost's new dashboard g..."
---

Ghost CMS est une plateforme spécifiquement conçue pour les blogueurs et les écrivains. Avec Ghost, vous pouvez rapidement mettre en place un site web de blog et le faire fonctionner.

Ghost cible principalement les écrivains et toutes les fonctionnalités sont spécifiquement conçues pour l'écriture.

Le nouveau tableau de bord de Ghost vous offre une interface conviviale, et les débutants peuvent facilement comprendre les fonctionnalités. De plus, les tutoriels gratuits de Ghost vous aideront si vous rencontrez des problèmes.

**Quelques fonctionnalités cool de Ghost :**

1. Open-source
2. Support des membres
3. Éditeur de texte riche (éditeur Koenig)
4. Newsletters
5. Support des abonnés par email
6. Support de la fonctionnalité de connexion
7. Plugin d'intégration
8. Tableau de bord d'analyse
9. Support des commentaires intégré
10. Support de la recherche intégré
11. Fonctionnalité de recherche intégrée
12. Support SEO et différents types de métadonnées pour les réseaux sociaux
13. Conception de thème personnalisé

Vous pouvez consulter tout [le code disponible pour ce projet sur GitHub ici](https://github.com/frontendweb3/fastest).

## Voici ce que nous allons couvrir :

1. [Auto-hébergement vs Hébergement avec Ghost](#heading-auto-hebergement-vs-hebergement-avec-ghost)
2. [Quels sont les inconvénients de Ghost ?](#heading-quels-sont-les-inconvenients-de-ghost-cms)
3. [Comment installer le Ghost CMS](#heading-comment-installer-le-ghost-cms)
4. [Comprendre la structure des dossiers de Ghost](#heading-comprendre-la-structure-des-dossiers-de-ghost)
5. [Comprendre la structure des dossiers des thèmes Ghost](#heading-comprendre-la-structure-des-dossiers-des-themes-ghost)
6. [Comment créer un nouveau thème avec l'outil CLI npm](#heading-comment-creer-un-nouveau-theme-avec-loutil-cli-npm)
7. [Comment créer un nouveau thème Ghost à partir de zéro](#heading-comment-creer-un-nouveau-theme-ghost-a-partir-de-zero)
8. [Comment installer ghost-cli globalement](##comment-installer-ghost-cli-globalement)
9. [Comment installer Ghost localement](#heading-comment-installer-ghost-localement)
10. [Comment configurer Tailwind CSS](#heading-comment-configurer-tailwind-css)
11. [Autres commandes importantes dans le CLI de Ghost](#heading-autres-commandes-importantes-dans-le-cli-de-ghost)
12. [Comment écrire le code pour notre thème Ghost personnalisé](#comment-ecrire-le-code-pour-notre-theme-ghost-personnalise)
13. [Comment ajouter la configuration du thème dans package.json](#heading-comment-ajouter-la-configuration-du-theme-dans-packagejson)
14. [Comment utiliser les assistants de thème](#heading-comment-utiliser-les-assistants-de-theme)
15. [Qu'est-ce que le dossier Partials ?](#heading-quest-ce-que-le-dossier-partials)
16. [Comment créer une page par défaut](#heading-comment-creer-une-page-par-defaut)
17. [Comment créer une page d'index](#heading-comment-creer-une-page-dindex)
18. [Comment créer une page de posts](#heading-comment-creer-une-page-de-posts)
19. [Comment créer des pages d'information](#heading-comment-creer-des-pages-dinformation)
20. [Comment créer une page d'auteur](#heading-comment-creer-une-page-dauteur)
21. [Comment créer une page de tags](#heading-comment-creer-une-page-de-tags)
22. [Comment créer une page d'erreur](#heading-comment-creer-une-page-derreur)
23. [Comment activer les commentaires](#heading-comment-activer-les-commentaires)
24. [Comment configurer la recherche](#heading-comment-configurer-la-recherche)
25. [Conclusion](#heading-conclusion)

## Auto-hébergement vs Hébergement avec Ghost

Ghost propose deux façons de créer/héberger votre site web :

1. Auto-hébergement
2. Avec la plateforme cloud de Ghost

### Auto-hébergement

Si vous choisissez l'auto-hébergement, vous hébergerez votre site web sur n'importe quelle plateforme cloud comme [Google Cloud](https://cloud.google.com/), [AWS Cloud](https://aws.amazon.com/), [Azure Cloud](https://azure.microsoft.com/), [Digital Ocean](https://www.digitalocean.com/), et ainsi de suite. Ce sont certaines des plateformes cloud les plus utilisées sur le marché.

La plupart des plateformes cloud offrent des solutions de déploiement en un clic. Cela signifie que vous pouvez déployer votre blog Ghost avec un seul clic.

Avant de déployer votre blog Ghost, vous devriez comparer toutes les plateformes cloud en fonction des prix avant d'en choisir une.

L'auto-hébergement de votre blog Ghost est gratuit, et vous n'avez pas besoin de payer quoi que ce soit à la plateforme Ghost. Vous paierez simplement votre fournisseur cloud.

### Hébergement avec la plateforme cloud de Ghost

Si vous choisissez d'héberger avec Ghost, ils vous aideront à créer le blog et à l'héberger sur la plateforme Ghost elle-même. L'équipe Ghost gère toute la maintenance et la sécurité. Vous n'aurez pas à vous soucier de la mise à jour de Ghost et de tous les thèmes que vous utilisez – le personnel de Ghost s'en chargera pour vous.

L'auto-hébergement cible davantage les développeurs, tandis que l'hébergement avec la plateforme Ghost cible toute personne qui ne connaît pas les ordinateurs et la programmation.

L'hébergement Ghost est payant – il n'est pas gratuit. Mais ils vous offrent une période d'essai gratuite de 14 jours, après laquelle vous passez automatiquement à un plan payant.

### Que devriez-vous choisir, payant ou auto-hébergement ?

D'après mon expérience, l'hébergement avec la plateforme Ghost est la meilleure solution pour les développeurs débutants, les non-développeurs et les écrivains. L'équipe Ghost gère tout pour vous. Vous ne vous souciez pas du trafic, de la sécurité ou de la maintenance et vous n'avez pas besoin de mettre à jour le Ghost CMS. Cela vous permet de vous concentrer sur l'écriture.

En tant que développeur, je recommande toujours de faire de l'auto-hébergement avec Ghost. J'ai fait fonctionner mon blog Ghost auto-hébergé avec Google Cloud pendant deux ans avec un déploiement en un clic de Bitnami.

Après six mois, j'avais utilisé mon crédit gratuit de 200 $, et ensuite j'ai commencé à payer mensuellement pour l'hébergement Google Cloud.

Pour une personne non technique, je recommande fortement d'utiliser la plateforme cloud Ghost (pro) ainsi que toute autre plateforme qui fournit un cloud basé sur Ghost et partage l'hébergement.

J'ai trouvé une [liste des plateformes d'hébergement Ghost](https://geekflare.com/ghost-hosting-platforms/) sur Internet. Peut-être que l'une d'entre elles résoudra vos problèmes ou questions d'hébergement. Si vous prévoyez de déployer Ghost avec la plateforme [Google Cloud](https://officialrajdeepsingh.dev/tags/ghost-cms/), j'ai un article à ce sujet.

## Quels sont les inconvénients de Ghost CMS ?

Le plus grand inconvénient de Ghost est que les performances web peuvent sembler lentes. Si vous voulez de bonnes performances web, vous devrez probablement utiliser un CDN pour les médias (images, vidéos et PDF) et aussi pour le CSS et le JavaScript.

Le deuxième plus grand inconvénient est le coût. J'ai fait fonctionner mon blog avec Ghost pendant deux ans, et je paie 10 à 20 fois plus à Google Cloud pour l'hébergement en tant que déploiement auto-hébergé.

Mon site web a 4000 à 5000 utilisateurs actifs par mois, et je paie 20 fois plus. À cause de cela, j'ai migré mon site web vers Hugo.

Maintenant, j'ai toujours 4000 à 5000 utilisateurs actifs sur le site web, et je ne paie rien à Netlify.

### La solution pour les développeurs

La meilleure solution pour les développeurs est d'utiliser Ghost comme backend et, avec l'API REST, de choisir n'importe quel framework JavaScript comme Next.js, Fresh, Astro, et ainsi de suite.

Il existe de nombreux frameworks qui peuvent vous aider à construire un site web statique. De plus, les sites web statiques sont rapides et se déployent avec zéro JavaScript.

Avec cette méthode, vous n'utiliserez peut-être pas toutes les fonctionnalités de Ghost, mais vous pouvez économiser beaucoup d'argent. Cependant, la construction du site web avec un framework JavaScript prend beaucoup de temps juste pour faire fonctionner la version essentielle du site web.

Ma solution ne fonctionne bien que pour une petite équipe. Donc, si votre équipe compte de nombreux écrivains et soumet de nombreux articles en une seule journée, je recommande de rester avec Ghost CMS comme frontend et backend.

La version 5.0 de Ghost est 20 % plus rapide que l'ancienne version. Supposons que vous utilisez Ghost et que vous souhaitez concevoir votre propre thème personnalisé – alors cet article est pour vous. Commençons.

## Comment installer le Ghost CMS

La manière d'installer Ghost CMS change selon votre système d'exploitation. Nous allons discuter de l'installation pour tous les systèmes d'exploitation dans ce guide. Vous pouvez installer Ghost avec npm, yarn et Docker.

Maintenant, voyons comment installer Ghost pour :

1. Windows, Linux et macOS
2. Image Docker

## Comment installer Ghost sur Windows, Linux et macOS

La configuration de l'environnement de développement de thème Ghost dans Windows et macOS est un processus simple. Mais il est préférable que vous ayez installé le gestionnaire de paquets npm ou yarn. Si vous n'avez pas Node.js, npm et yarn, vous devrez les installer – Node.js vient avec npm et yarn préinstallés.

Pour installer Ghost CMS globalement et localement, suivez ces étapes de base :

### Comment installer ghost-CLI globalement

Tout d'abord, vous pouvez installer `ghost-cli` globalement sur votre machine en utilisant npm ou yarn. Voici les commandes :

```bash
npm install ghost-cli@latest -g
    OU
yarn global add ghost-cli@latest
```

### Comment installer Ghost localement

Ensuite, lorsque votre installation de ghost-CLI est terminée, exécutez la commande `ghost local` dans votre terminal. Cela ressemble à ceci :

```bash
ghost install local
```

La sortie de la commande ressemble à ceci :

![Structure des dossiers de Ghost cms](https://www.freecodecamp.org/news/content/images/2022/09/carbon--1-.png)
_Structure des dossiers de Ghost cms_

**Note** : vous devez exécuter la commande `ghost install local` dans un dossier vide. Sinon, vous rencontrerez une erreur :

![Erreur de répertoire non vide avec ghost-cli](https://www.freecodecamp.org/news/content/images/2022/09/ghost-not-empty-error.png)
_Erreur de répertoire non vide avec ghost-cli_

Pour démarrer le serveur de développement local, exécutez la commande `ghost start` dans votre terminal.

![Commande ghost start](https://www.freecodecamp.org/news/content/images/2022/09/ghost-start-command.png)
_Commande ghost start_

Si vous obtenez une erreur lors de l'exécution de `ghost start` dans Ubuntu, exécutez la commande suivante : `ghost start --no-setup-linux-user`.

![Le répertoire n'est pas lisible par les autres utilisateurs dans ghost cms.](https://www.freecodecamp.org/news/content/images/2022/09/not-readable-by-other-user.png)
_Erreur de répertoire non lisible par les autres utilisateurs dans Ghost CMS._

## Comment configurer votre environnement en utilisant une image Docker

Docker est également un excellent moyen de configurer un environnement de développement ou de production de thème pour Ghost. L'équipe Ghost fournit une image [Ghost Docker officielle](https://hub.docker.com/_/ghost) sur Docker Hub.

Pour commencer la configuration, vous aurez besoin du fichier `docker-compose.yml` dans le dossier racine de votre projet. Ensuite, exécutez la commande `docker-compose up` dans votre terminal.

```
version: '3.8'
services:
  blog:
    image: ghost
    restart: always
    ports:
      - 8080:2368
    volumes:
      - ./custom-ghost-theme:/var/lib/ghost/content/themes/custom-ghost-theme/
    environment:
      url: http://localhost:808
      NODE_ENV: development
```

Dans la section des volumes, vous passez votre fichier. Dans mon cas, j'ai ajouté un fichier spécifique dans mon dossier de thème Ghost.

```
version: '3.8'
services:
  blog:
    image: ghost
    restart: always
    ports:
      - 8080:2368
    volumes:
      - ./assets:/var/lib/ghost/content/themes/fastest/assets
      - ./partials:/var/lib/ghost/content/themes/fastest/partials
      - ./author.hbs:/var/lib/ghost/content/themes/fastest/author.hbs
      - ./default.hbs:/var/lib/ghost/content/themes/fastest/default.hbs
      - ./error-404.hbs:/var/lib/ghost/content/themes/fastest/error-404.hbs
      - ./error.hbs:/var/lib/ghost/content/themes/fastest/error.hbs
      - ./gulpfile.js:/var/lib/ghost/content/themes/fastest/gulpfile.js
      - ./index.hbs:/var/lib/ghost/content/themes/fastest/index.hbs
      - ./package-lock.json:/var/lib/ghost/content/themes/fastest/package-lock.json
      - ./package.json:/var/lib/ghost/content/themes/fastest/package.json
      - ./page.hbs:/var/lib/ghost/content/themes/fastest/page.hbs
      - ./post.hbs:/var/lib/ghost/content/themes/fastest/post.hbs
      - ./query.hbs:/var/lib/ghost/content/themes/fastest/query.hbs
      - ./tag.hbs:/var/lib/ghost/content/themes/fastest/tag.hbs
      - ./readme.md:/var/lib/ghost/content/themes/fastest/readme.md
    environment:
      url: http://localhost:8080
      NODE_ENV: development
```

Dans votre dossier custom-ghost-theme, vous avez besoin des fichiers `index.hbs`, `post.hbs` et `package.json` pour commencer le développement du thème. Mais vous obtiendrez une erreur lorsque vous activerez votre thème dans le tableau de bord Ghost sans fichier requis.

**Voici le dépôt GitHub si vous voulez suivre :**

%[https://github.com/officialrajdeepsingh/ghostthemewithdocker]

#### Erreurs

Dans Ubuntu (22.04) ou toute autre distribution Linux, vous obtiendrez l'erreur `Message : Le répertoire /home/rajdeepsingh/ n'est pas lisible par les autres utilisateurs du système`. Cela signifie que le vôtre est ancien. Mettez donc à jour votre `ghost-cli`, puis exécutez la commande `ghost start` dans votre dossier.

## Comprendre la structure des dossiers de Ghost

La structure des dossiers de Ghost comporte trois dossiers principaux et un fichier. Ils sont :

1. Le fichier `config.development.json` contient la configuration pour le développement de Ghost.
2. Le dossier `current` est un lien (lien symbolique) qui cible la version installée.
3. Le dossier `version` contient toutes les versions de Ghost cms.
4. Le dossier content est le dossier principal contenant notre fichier de base de données, les paramètres, le thème, les images, les médias, etc.

![Structure des dossiers de Ghost cms](https://www.freecodecamp.org/news/content/images/2022/09/ghost-folder-sturture.png)
_Structure des dossiers de Ghost CMS_

La structure des dossiers peut changer selon le système d'exploitation, mais le dossier `content` est le même dans chaque système d'exploitation.

Le dossier content contient tous les fichiers importants pour Ghost. Ils sont :

1. Le dossier data contient un fichier de base de données SQLite3. Ghost utilise par défaut la base de données SQLite3.
2. Les dossiers files, images et media contiennent tous les fichiers que les écrivains téléchargent.
3. Le dossier public contient tous les fichiers CSS et JavaScript publics – par exemple, les fichiers JavaScript et CSS des cartes et des membres.
4. Enfin, le dossier settings contient tous les paramètres, par exemple, le fichier `router.xml`.
5. Le dossier theme contient tous les fichiers et dossiers utilisés pour développer le thème.

## Comprendre la structure des dossiers des thèmes Ghost

Vous pouvez construire un nouveau magasin de thèmes personnalisés dans le dossier `content/theme`. Pour développer un nouveau thème, vous devrez toujours créer un nouveau dossier avec le nom du thème et stocker tous les fichiers dans le dossier du nom du thème.

```
// structure du thème

content 
content/theme
content/theme/my-theme-name
content/theme/my-theme-name/index.hbs
content/theme/my-theme-name/post.hbs
content/theme/my-theme-name/package.json

// reste des fichiers créés dans le dossier my-theme-name

```

Ghost CMS utilise **handlebars** pour construire un thème Ghost. Il y a un certain nombre de fichiers, mais seulement trois fichiers sont requis :

1. `index.hbs` dans le fichier principal (requis) pour concevoir la page d'accueil du site web.
2. `post.hbs` le fichier (requis) est utilisé pour lire et concevoir l'article complet.
3. `package.json` fichier (requis) est utilisé pour la configuration de Node.js, et il utilise également le nom du thème, la description, la version, la configuration personnalisée, etc.
4. Le fichier `default.hbs` est utilisé pour construire la mise en page du thème.
5. Le dossier assets contient tous les fichiers JavaScript, CSS, polices et images.
6. Le dossier partials aide à diviser les fichiers en petits partials (parties) pour une meilleure lisibilité du code.

![Structure des dossiers des thèmes Ghost](https://www.freecodecamp.org/news/content/images/2022/09/theme-struture.png)
_Structure des dossiers des thèmes Ghost_

## Comment créer un nouveau thème avec l'outil CLI npm

La manière la plus simple de commencer un nouveau thème Ghost est avec le [create-ghost-theme CLI](https://www.npmjs.com/package/create-ghost-theme). Je l'ai construit, et je le maintiens. Le create-ghost-theme CLI vous aide à créer la structure de dossier suivante que nous allons discuter ensuite. Mais actuellement, il ne supporte que **Tailwind CSS**.

Tout d'abord, nous allons créer un nouveau thème avec le create-ghost-theme CLI et redémarrer le serveur local Ghost CMS.

### Structure de dossier

Après avoir créé un nouveau thème avec [create-ghost-theme CLI](https://www.npmjs.com/package/create-ghost-theme), votre structure de dossier ressemble à ceci :

![structure de dossier create-ghost-theme cli](https://www.freecodecamp.org/news/content/images/2022/09/ghost-theme-cli.png)
_structure de dossier create-ghost-theme cli_

### Comprendre la nouvelle mise en page du site web

Après avoir créé le thème avec create-ghost-theme CLI, votre thème ressemble à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/default-hbs.png)
_index.hbs_

Votre page de lecture de site web ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/index-hbs.png)

Votre nouvelle page de tag ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/tag-hbs.png)

## Comment créer un nouveau thème Ghost à partir de zéro

Lorsque vous apprenez le développement de thèmes Ghost, ma recommandation est de commencer à créer un nouveau thème à partir de zéro. Ensuite, vous pouvez utiliser l'outil CLI que je viens de vous montrer. Cela sera beaucoup plus facile pour vous.

Alors maintenant, c'est ce que nous allons couvrir en profondeur : comment créer un nouveau thème Ghost CMS à partir de zéro.

### Exigences :

Pour créer un nouveau thème, vous aurez besoin de deux bibliothèques : la première est `ghost-cli` et la seconde est Tailwind CSS.

Voici ce que nous allons passer en revue dans les sections à venir :

1. Comment installer `Ghost-cli` globalement
2. Comment configurer Tailwind CSS
3. Comment comprendre plus de commandes dans le Ghost CLI
4. Enfin, nous allons écrire le code

### Comment installer ghost-cli globalement

Nous avons vu comment faire cela ci-dessus, mais au cas où vous auriez besoin d'un rappel, le voici :

Tout d'abord, vous pouvez installer `ghost-cli` globalement sur votre machine en utilisant npm ou yarn. Voici les commandes :

```bash
npm install ghost-cli@latest -g
    OU
yarn global add ghost-cli@latest
```

### Comment configurer Tailwind CSS

Tailwind CSS est une puissante bibliothèque CSS pour concevoir le front-end d'un site web. Et vous pouvez facilement l'utiliser avec Ghost.

Installez Tailwind CSS dans votre dossier de thème comme ceci :

```bash
npm install -D tailwindcss postcss autoprefixer
```

Après que Tailwind et un autre package ont été installés avec succès, exécutez la commande suivante pour configurer Tailwind pour votre développement de thème :

```bash
npx tailwindcss init
```

La commande `tailwindcss init` crée un fichier `tailwind.config.js`. Voici ce que vous verrez :

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
content: [],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

Configurez le chemin de votre modèle dans la section content, afin que Tailwind CSS suive les classes CSS. Ensuite, compilez ces classes dans le fichier de production.

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*.hbs","partials/*.hbs"],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Créez un fichier `main.css` ou `dev.css` et utilisez un autre nom de fichier pour créer le fichier pour les directives Tailwind. Ensuite, collez le code suivant des directives CSS de Tailwind dans le fichier :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

```

Créez le script pour Tailwind CSS afin de vérifier toutes les classes, puis créez un fichier CSS prêt pour la production pour votre thème.

```json
    "scripts": {
        "start": "npx tailwindcss -i ./assets/css/dev.css -o ./assets/build/css/build.css --watch"
    },
```

La dernière étape consiste à lier le fichier CSS prêt pour la production à votre thème comme ceci :

```handlebars
<head>
    {{!-- lien vers le fichier css prêt pour la production --}}
    <link rel="stylesheet" href="{{asset 'build/css/build.css'}}" />
</head>
```

Le problème que vous pourriez rencontrer lorsque vous activez Tailwind CSS dans un thème Ghost est que le rafraîchissement de votre site dans le processus de développement est manuel. Lorsque vous changez quelque chose lié aux classes Tailwind, vous devrez rafraîchir manuellement votre site web. Je n'ai pas encore trouvé de solution, mais vous pouvez utiliser le serveur en direct pour cela pour l'instant.

### Autres commandes importantes dans le CLI de Ghost

Il existe un certain nombre d'autres commandes que vous utiliserez souvent lorsque vous travaillerez dans le CLI de Ghost. Passons-les en revue maintenant. Voici ce que nous allons discuter :

1. ghost stop
2. ghost ls
3. ghost doctor
4. ghost uninstall
5. ghost version
6. ghost restart
7. ghost update
8. ghost version
9. ghost --help

#### Comment utiliser la commande ghost stop

La commande `ghost stop` arrête l'instance en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost-stop.png)

#### Comment utiliser la commande ghost ls

La commande `ghost ls` imprime la liste des instances installées actuelles sur votre machine.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost-ls.png)

#### Comment utiliser la commande ghost doctor

La commande `ghost doctor` vérifie l'état du système pour voir si tout va bien avant d'exécuter la commande `ghost install` ou `ghost update`.

Si vous rencontrez des erreurs dans Ghost, vous pouvez également utiliser la commande ghost doctor pour vérifier les erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost-doctor.png)

#### Comment utiliser la commande ghost uninstall

La commande `ghost uninstall` supprime l'instance Ghost et les fichiers de configuration associés.

#### Comment vérifier la version de Ghost

Vous pouvez utiliser la commande `ghost version` pour vérifier votre version actuellement installée de Ghost.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost-version.png)

#### Comment utiliser la commande ghost restart

La commande `ghost restart` redémarre votre instance Ghost actuellement en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost-restart.png)

#### Comment utiliser la commande ghost update

La commande ghost update met à jour votre ancienne version de Ghost vers la nouvelle version.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost-update.png)

#### Comment utiliser la commande ghost --help

La commande `ghost --help` imprime une page d'aide :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ghost---help.png)

### Enfin, nous allons écrire le code

Maintenant, nous pouvons commencer à écrire le code. Voici ce que nous allons couvrir dans les sections à venir :

1. Comment ajouter la configuration du thème dans `package.json` [requis]
2. Comment utiliser les assistants de thème
3. Qu'est-ce que le dossier partials ?
4. Comment créer une page par défaut
5. Comment créer une page d'index [requis]
6. Comment créer une page de posts [requis]
7. Comment créer une page d'information
8. Comment créer une page de tags
9. Comment configurer les commentaires
10. Comment activer la recherche

### Comment ajouter la configuration du thème dans package.json

Le fichier `package.json` est le fichier principal où vous ajoutez ou modifiez le nom du thème, la description et la configuration personnalisée pour le thème.

La **première étape** consiste à créer le fichier `package.json` et à ajouter le nom du thème, la description, la version et la configuration supplémentaire.

Les propriétés suivantes sont utilisées par les thèmes Ghost : `name`, `description`, `version`, `engines`, `card_assets`, `license`, `author`, `keywords`, `screenshots` et `config` dans le fichier `package.json`.

Les propriétés les plus importantes sont `name`, `description`, `version`, `engines`, `card_assets` et `config`. Voici à quoi cela ressemble dans le code :

```json
{
    "name": "fastest",
    "description": "Thème de base Ghost CMS le plus rapide. Fastest est un thème moderne, léger et open-source",
    "version": "1.0.7",
    "engines": {
        "ghost": ">=5.0.0"
    },
    "license": "MIT",
    "scripts": {
        "dev": "gulp",
        "start": "npx tailwindcss -i ./assets/css/dev.css -o ./assets/build/css/build.css --watch"
    },
    "author": {
        "name": "Rajdeep Singh",
        "email": "officialrajdeepsingh@gmail.com",
        "url": "https://officialrajdeepsingh.dev"
    },
    "keywords": [
        "ghost",
        "theme",
        "blog",
        "light weight",
        "ghost-theme"
    ],
    "screenshots": {
        "desktop": [
            "assets/dark.png",
            "assets/light.png"
        ],
        "mobile": "assets/mobile.png"
    },
    "config": {
        "posts_per_page": 10,
        "card_assets": true,
        "image_sizes": {},
        "custom": {
            "linkedin_url": {
                "type": "text",
                "default": "None"
            },
            "github_url": {
                "type": "text",
                "default": "None"
            },
            "instagram_url": {
                "type": "text",
                "default": "None"
            },
            "copyright": {
                "type": "text",
                "default": "Droits d'auteur par Rajdeep Singh"
            },
            "copyright_url": {
                "type": "text",
                "default": "https://officialrajdeepsingh.dev/pages/terms-and-conditions/"
            },
            "adsense_enable": {
                "type": "select",
                "options": [
                    "Disable",
                    "Enable"
                ],
                "default": "Disable"
            }
        }
        },
    "devDependencies": {
        "@tailwindcss/typography": "^0.5.8",
        "autoprefixer": "^10.4.13",
        "cssnano": "^5.0.17",
        "gscan": "^4.22.0",
        "gulp": "4.0.2",
        "gulp-autoprefixer": "^8.0.0",
        "gulp-concat": "^2.6.1",
        "gulp-cssnano": "^2.1.3",
        "gulp-livereload": "4.0.2",
        "gulp-sourcemaps": "^3.0.0",
        "gulp-uglify": "^3.0.2",
        "postcss": "^8.4.20",
        "tailwindcss": "^3.2.4"
    }
}

```

Vous pouvez en savoir plus sur [card_assets](https://ghost.org/docs/themes/content/) et [config](https://ghost.org/docs/themes/structure/#packagejson) pour le thème. La section config aide à ajouter la configuration pour Ghost. Vous pouvez également ajouter plus de [configuration personnalisée](https://ghost.org/docs/themes/custom-settings/) pour Ghost et l'activer et la désactiver avec l'interface utilisateur de Ghost.

Pour vérifier toutes les configurations, allez dans Ghost > Paramètres > Design > et cliquez sur Site-wide. Là, vous pouvez vérifier toutes les listes de configuration fournies par le développeur du thème.

![activer et désactiver la configuration personnalisée dans ghost cms](https://www.freecodecamp.org/news/content/images/2022/12/customconfig.png)
_activer et désactiver la configuration personnalisée dans ghost cms_

### Comment utiliser les assistants de thème

L'équipe Ghost fournit de nombreuses fonctions utiles pour ajouter des fonctionnalités supplémentaires au thème Ghost avec [handlebars](https://handlebarsjs.com/). Certaines des fonctionnalités par défaut viennent avec handlebars et d'autres fonctionnalités sont construites par l'équipe Ghost et maintenues par la communauté.

L'équipe Ghost utilise handlebars pour construire l'ensemble du Ghost CMS et du thème. En gros, handlebars.js est un langage de modèle qui vous aide à construire des sites web statiques et dynamiques.

Il existe de nombreux assistants Ghost comme [foreach](https://ghost.org/docs/themes/helpers/foreach/), [get](https://ghost.org/docs/themes/helpers/get/), [if](https://ghost.org/docs/themes/helpers/if/), [is](https://ghost.org/docs/themes/helpers/is/), [match](https://ghost.org/docs/themes/helpers/match/), [@config](https://ghost.org/docs/themes/helpers/config/), [comments](https://ghost.org/docs/themes/helpers/comments/), [navigation](https://ghost.org/docs/themes/helpers/navigation/), [post](https://ghost.org/docs/themes/helpers/post/), [total_members](https://ghost.org/docs/themes/helpers/total_members/), [total_paid_members](https://ghost.org/docs/themes/helpers/total_paid_members/), [block](https://ghost.org/docs/themes/helpers/block/), [asset](https://ghost.org/docs/themes/helpers/asset/), [ghost_head](https://ghost.org/docs/themes/helpers/ghost_head_foot/), [ghost_foot](https://ghost.org/docs/themes/helpers/ghost_head_foot/), [pagination](https://ghost.org/docs/themes/helpers/pagination/), [partials](https://ghost.org/docs/themes/helpers/partials/), [body_class](https://ghost.org/docs/themes/helpers/body_class/), [block](https://ghost.org/docs/themes/helpers/block/), [search](https://ghost.org/docs/themes/helpers/search/) et bien d'autres.

Vous pouvez lire à propos de tous les [assistants sur la documentation officielle](https://ghost.org/docs/themes/helpers/). Vous pouvez également copier-coller certains du code pour ne pas avoir à vous en souvenir.

### Qu'est-ce que le dossier Partials ?

Le dossier partials est comme un dossier de composants où vous définissez tous les composants pour votre thème. En gros, les composants sont du code réutilisable que vous pouvez réutiliser aussi souvent que vous en avez besoin. Dans la structure du thème, nous appelons ces partials. Tous les partials sont créés avec handlebars.js.

![partials pour le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/partials.png)
_partials pour le thème ghost_

J'ai créé plus de 24 partials pour mon thème Ghost et vous pouvez facilement les réutiliser sur plusieurs sites web. Vous pouvez utiliser les partials avec la syntaxe suivante : `{{> votre-nom-de-fichier-partials}}`.

### Comment créer une page par défaut

Tout d'abord, nous devons créer un fichier `default.hbs`. Le fichier `default.hbs` nous aide à créer une mise en page pour le site web. Voici le code :

```handlebars
<!DOCTYPE html>

<html class="dark scroll-smooth overflow-x-hidden" lang="{{@site.locale}}">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    {{!-- lien vers le fichier css prêt pour la production --}}
    <link rel="stylesheet" href="{{asset 'build/css/build.css'}}" />
   {{!-- en-tête ghost --}}
      {{ghost_head}}

</head>


<body class="{{body_class}} bg-white dark:bg-slate-800 dark:text-white antialiased scroll-smooth ">
  
  {{!-- partials/header --}}
    {{> header}}

    <main class="mt-6 flex flex-col">

{{!-- Rendre d'autres pages --}}
        {{{body}}}

    </main>
{{!-- partials/footer --}}
    {{> footer}}
    {{> banner}}

{{!-- en-tête ghost --}}
    {{ghost_foot}}

    <script src="{{asset 'build/js/main.js'}}"></script>

</body>

</html>
```

Voyons ce qui se passe ici :

1. `{{meta_title}}` fournit le titre du site web.
2. Le `@site` est une variable globale et vous pouvez accéder à un titre avec `{{@site.title}}`.
3. Incluez un Ghost `{{ghost_head}}` dans la balise head.
4. Incluez un Ghost `{{ghost_foot}}` dans la balise footer.
5. Insérez tous les autres modèles avec la balise `{{{body}}}` dans index.hbs, post.hbs, etc.
6. Tous les autres modèles sont insérés dans index.hbs, post.hbs, etc.
7. Incluez des classes CSS dynamiques avec `{{body_class}}` dans la balise `<body>`
8. Ajoutez des partials de pied de page dans le fichier par défaut `{{> footer}}`
9. Ajoutez des partials d'en-tête dans le fichier par défaut `{{> header}}`
10. Incluez des assets depuis le dossier `{{asset "build/tailwind.css"}}`.

### Comment créer une page d'index

![Créer index.hbs dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/index.png)
_Créer `index.hbs` dans le thème Ghost_

La page d'index est la page principale du site web. Vous pouvez créer une page d'index similaire avec le code suivant :

```handlebars
{{!-- Ajouter le fichier de mise en page default.hbs --}}
{{!< default}} 

{{!-- boucler tous les posts et les afficher sur la page d'accueil --}}

{{#foreach posts}} 

{{!-- vérifier la condition définie dans la section config dans package.json et ajouter le code adsense après chaque troisième post --}}
    {{#has number="nth:3" }} 
        {{#match @custom.adsense_enable "Enable" }} 
            {{> ads}}
        {{/match}}
    {{/has}}
    
    {{!-- partials/postCard.hbs --}}
    {{> postCard }}

    {{/foreach}}

    {{!-- Ajouter la pagination --}}
    {{pagination}}

{{!-- vérifier la condition définie dans la section config dans package.json et ajouter adsense --}}
    {{#match @custom.adsense_enable "Enable"}}
        {{> ads}}
    {{/match}}

{{!-- partials/newsletter --}}
    {{> newsletter}}
```

Vous pouvez accéder à tous les posts avec une boucle foreach et les passer aux partials avec le modèle `{{> postCard}}`. Le `@custom.adsense_enable` est une configuration personnalisée écrite dans le fichier `package.json` et utilisée dans le thème pour vérifier si le propriétaire du site web a activé AdSense sur le site ou non. La configuration personnalisée vous permet d'aller dans Ghost > Paramètres > Design > et de cliquer sur Site-wide et d'activer Adsense.

### Comment créer une page de posts

![Créer post.hbs dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/post.png)
_Créer `post.hbs` dans le thème Ghost_

La page de posts est l'endroit où les lecteurs liront vos articles sur votre site. Vous pouvez créer une page de posts avec le code suivant.

```handlebars
{{!< default}}

{{#post}}


{{!-- Passer le temps de lecture à l'auteur des partials avec le bloc, en savoir plus sur le bloc https://ghost.org/docs/themes/helpers/block/ --}}
{{#contentFor "fastestReadingTime"}}

 <p class="text-slate-600 dark:text-slate-400 text-xs xs:text-xs sm:text-xs md:text-sm lg:text-sm xl:text-sm 2xl:text-sm ">
    {{reading_time}}
 </p>

{{/contentFor}}

{{#match @custom.adsense_enable "Enable"}}

    {{> ads}}

{{/match}}

<article class="{{post_class}} w-6/6 p-2">
    
    <!-- Section d'en-tête -->
    
    <div class="m-auto mb-4 w-6/6 xs:w-5/6 sm:w-5/6 md:w-5/6 lg:w-5/6 xl:w-5/6 2xl:w-5/6">
        <h1 class="mt-8 text-3xl xs:text-4xl sm:text-5xl md:text-5xl xl:text-5xl 2xl:text-5xl">
             {{title}} 
        </h1>
        <p class="text-slate-600 dark:text-slate-500 mt-2 text-1xl">
            {{excerpt}}
        </p>
    </div>
    
    <!-- Carte de l'auteur partials/authors -->
    {{> authors}}



    <!-- miniature de l'article avec partials/authors -->
    {{> featureImage}}


    <!-- corps de l'article -->
    <div class="prose-lg prose-neutral m-auto p-2 my-10 w-10/12">
        {{content}}
    </div>




</article>


    {{!-- partials/comment --}}
    {{> comment}}


{{!-- Ajouter adsense --}}
{{#match @custom.adsense_enable "Enable"}}

    {{> ads}}

{{/match}}

{{!-- Afficher les posts liés --}}
{{#get "posts" filter="authors:{{primary_author.slug}}+id:-{{id}}" limit="3" include="authors"}}

{{!-- si le post est disponible, l'afficher --}}
{{#if posts}}

<h2 class="mt-10 m-auto text-left w-5/6 text-xl xs:text-1xl sm:text-3xl md:text-4xl xl:text-5xl 2xl:text-6xl">
    Lire plus
</h2>

{{!-- boucler tous les posts --}}
{{#foreach posts}}
    {{> postCard }}
{{/foreach}}

{{/if}}

{{/get}}

{{!-- Ajouter adsense --}}
{{#match @custom.adsense_enable "Enable"}}

    {{> ads}}

{{/match}}

{{/post}}

{{!-- partials/newsletter --}}
{{> newsletter}}
```

Le bloc fastestReadingTime sert à transmettre le temps de lecture aux partials de l'auteur. Le `@custom.adsense_enable` est une configuration personnalisée écrite dans le fichier `package.json` et utilisée dans le thème pour vérifier si le propriétaire du site a activé AdSense sur le site ou non. La configuration personnalisée vous permet d'aller dans Ghost > Paramètres > Design > et de cliquer sur Site-wide et d'activer Adsense.

### Comment créer des pages d'information

![Créer page.hbs dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/page.png)
_Créer `page.hbs` dans le thème ghost_

Le fichier `page.hbs` vous aide à créer des pages d'information pour votre site web. Par exemple, vous pouvez créer une page à propos, contact, politique de confidentialité ou de non-responsabilité sur votre site.

```handlebars
{{!< default}} 

{{#post}} 

    {{!--Passer le temps de lecture à l'auteur des partials avec le bloc, en savoir plus sur le bloc https://ghost.org/docs/themes/helpers/block/     --}}
    {{#contentFor "fastestReadingTime"}}

    <p class="text-grey-600 text-xs xs:text-xs sm:text-xs md:text-sm lg:text-sm xl:text-sm 2xl:text-sm ">
        {{reading_time}}
    </p>
    {{/contentFor}}

{{!-- Ajouter adsense base si activé sur le thème --}}
    {{#match @custom.adsense_enable "Disable"}}

        {{> ads}}

    {{/match}}

    <article class="{{post_class}}  w-6/6 p-2">

        <!-- Section d'en-tête -->
        <div class=" m-auto mb-16 w-6/6 xs:w-5/6 sm:w-5/6 md:w-5/6 lg:w-5/6 xl:w-5/6 2xl:w-5/6">
            <h1 class="text-gray-800 mt-8 text-3xl xs:text-4xl sm:text-4xl md:text-5xl xl:text-6xl 2xl:text-8xl">
                {{title}}
            </h1>
            <p class="text-gray-600 text-xl xs:text-xl sm:text-xl md:text-1xl xl:text-2xl 2xl:text-2xl">
                {{excerpt}}
            </p>
        </div>
        
        <!-- partials/authors -->
        {{> authors}}


        {{!-- partials/featureImage --}}
        {{> featureImage}}



        <!-- corps de l'article -->
        <div class=" prose-xl prose-neutral m-auto p-2 my-10 w-10/12">
            {{content}}
        </div>



    </article>


    {{!-- Ajouter adsense --}}
    {{#match @custom.adsense_enable "Disable"}}

        {{> ads}}

    {{/match}}

    {{/post}}
```

Le bloc fastestReadingTime sert à transmettre le temps de lecture aux partials de l'auteur. Le `@custom.adsense_enable` est une configuration personnalisée écrite dans le fichier `package.json` et utilisée dans le thème pour vérifier si le propriétaire du site a activé AdSense sur le site ou non. La configuration personnalisée vous permet d'aller dans Ghost > Paramètres > Design > et de cliquer sur Site-wide et d'activer Adsense.

### Comment créer une page d'auteur

![Créer author.hbs dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/author.png)
_Créer `author.hbs` dans le thème ghost_

Les pages d'auteur vous permettent de décrire l'auteur. Vous pouvez afficher le nom de l'auteur, sa biographie et les articles associés.

```handlebar
{{!< default}}

{{#author}}

{{!-- Section de l'auteur transmise avec le bloc, en savoir plus sur le bloc https://ghost.org/docs/themes/helpers/block/ --}}
   {{#contentFor "authorName"}}
      {{name}}
    {{/contentFor}}

<div class="container mt-20 mb-16 flex flex-col justify-between mx-auto">
   
    <div class="flex flex-col mt-6 w-6/6 xs:w-5/6 sm:w-5/6  md:w-3/6 lg:w-3/6 xl:w-3/6 2xl:w-3/6 xs:mt-6 sm:mt-6 md:mt-6 lg:mt-0 xl:mt-0 2xl:mt-0 ">
    
        <h1 class="text-3xl mt-5 xs:text-3xl sm:text-3xl md:text-4xl xl:text-5xl 2xl:text-6xl"> {{name}} </h1>

        {{#if bio}}
            <p class="mt-0 xs:mt-0 sm:mt-0 md:mt-1 lg:mt-3 xl:mt-3 2xl:mt-3 text-md">
                {{bio}}
            </p>
        {{/if}}

        <ul class="flex flex-row my-3">

            <li class="text-md">{{location}}</li>

               {{#if facebook}}
                
                    <li class="mx-3 text-sm flex items-center">
                        <a target="_blank" href="https://facebook.com/{{facebook}}" >

                        {{!-- Passer partials/Icons/facebook --}}
                            {{> Icons/facebook}}

                        </a>
                    </li>
                
                {{/if}}
                {{#if twitter}} 
                    <li class="mx-3 text-sm flex items-center">
                        <a target="_blank" href="https://twitter.com/{{twitter}}" >

                        {{!-- Passer partials/Icons/twitter --}}
                            {{> Icons/twitter}}

                        </a>
                    </li>
                {{/if}}
                {{#if website}} 
                    <li class="mx-3 text-sm flex items-center">
                        <a target="_blank" href="{{website}}" >

                            {{!-- Passer partials/Icons/website --}}
                            {{> Icons/website}}

                        </a>
                    </li>
                {{/if}}
        </ul>
    </div>
</div>


{{!-- obtenir les posts liés à l'auteur en fonction de l'ID de l'auteur --}}
    {{#get "posts" limit="all" filter="authors:{{slug}}+id:-{{id}}" order="published_at desc"   }}

        {{#if posts}}
                {{#foreach posts}}
                    {{> authorCard}}
                {{/foreach}}
        {{/if}}

    {{/get}}

{{/author}}

```

### Comment créer une page de tags

![Créer tag.hbs dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/tag.png)
_Créer tag.hbs dans le thème ghost_

Vous pouvez utiliser le fichier `tag.hbs` pour afficher les articles liés au tag utilisé.

```
{{!< default}}


{{#tag}}

<div class="container m-auto mt-32  mb-16  w-5/6 xs:w-5/6 sm:w-5/6 md:w-5/6 lg:w-5/6 xl:w-5/6 2xl:w-5/6">

    <h1 class=" text-gray-800 text-4xl xs:text-5xl sm:text-6xl md:text-7xl xl:text-8xl 2xl:text-9xl">{{name}}</h1>

    {{#if description}}
        <p class=" text-gray-600 text-xl xs:text-xl sm:text-xl md:text-1xl xl:text-2xl 2xl:text-2xl">
            {{description}}       
        </p>
    {{/if}}


</div>

{{!-- obtenir les posts liés au tag en fonction du slug du tag --}}

    {{#get "posts" include="authors,tags" limit="3" filter="tag:{{slug}}" as |related|}}

   {{!-- boucler les posts en fonction de l'article --}}
        {{#foreach related}}

    {{!-- vérifier la condition définie dans la section config dans package.json et ajouter le code adsense après chaque troisième post --}}
            {{#has number="nth:3"  }}
                {{#match @custom.adsense_enable "Enable"}}
                    {{> ads}}
                {{/match}}
            {{/has}}

        {{!-- partials/postCard.hbs --}}
            {{> postCard }}

        {{/foreach}}

    {{/get}}

{{/tag}}
```

### Comment créer une page d'erreur

![Créer error.hbs dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/404error-1.png)
_Créer `error.hbs` dans le thème ghost_

Vous utilisez le fichier `error.hbs` pour afficher lorsque des erreurs se produisent sur le site web. Les pages d'erreur aident votre site web à ne pas planter en production. L'erreur la plus courante est une erreur 404 (non trouvée).

```
{{!< default}} 
<div class="flex flex-col m-auto p-10 w-5/6 xs:w-5/6 sm:w-5/6 md:w-5/6 lg:w-5/6 xl:w-5/6 2xl:w-5/6">
    <h1 style="font-size: 10.8rem;" class="text-black text-center">
        {{statusCode}}
    </h1>

    <p class="text-4xl -m-6 text-center">
        {{message}}
    </p>

    <a href="/" class="text-center w-32 m-auto my-20 p-3 bg-black text-white items-center rounded-full">
        Accueil
    </a>
</div>
```

### Comment activer les commentaires

![activer les commentaires dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/comment-1.png)
_activer les commentaires dans le thème ghost_

Ghost 5 supporte officiellement [le système de commentaires](https://ghost.org/docs/themes/helpers/comments/) (il est intégré) et vous pouvez simplement activer les commentaires sur le thème en copiant et collant le code – vous n'aurez jamais besoin de configuration. Ghost lui-même gère toutes les configurations. Voici le code :

```handlebars
<div class="m-auto my-8 w-10/12">
    <p class="text-right text-xs xs:text-xs sm:text-xs md:text-sm lg:text-sm xl:text-sm 2xl:text-sm ">
        Avant de commenter, lisez nos <a style='text-decoration: underline' href="https://officialrajdeepsingh.dev/terms-and-conditions/">termes et conditions</a>
    </p>
    <div class="mt-5 mb-5 p-4">

   {{!-- Activer les commentaires sur le thème --}}
       {{comments}}
    </div>
</div>

```

### Comment configurer la recherche

![activer la barre de recherche dans le thème ghost](https://www.freecodecamp.org/news/content/images/2022/12/serach-bar.png)
_activer la barre de recherche dans le thème ghost_

Ghost 5 vient avec [le support officiel de la fonctionnalité de recherche](https://ghost.org/docs/themes/helpers/search/). Vous n'avez besoin d'aucune autre configuration. Il suffit de coller le code suivant dans votre thème et la fonctionnalité de recherche commencera à fonctionner sur votre site.

```handlebars
{{!-- partials/Icons/search --}}
<button class="gh-search" data-ghost-search>{{> Icons/search}}</button>
```

## Conclusion

Construire un thème avec Ghost est un processus relativement simple par rapport à WordPress. L'équipe Ghost a créé une documentation bien définie que vous pouvez facilement suivre en tant que débutant avec des exemples.

Ils fournissent également de nombreux composants prêts à l'emploi, comme la fonctionnalité de recherche, la page amp, les commentaires, etc.

Vous pouvez créer votre thème Ghost en copiant et collant le code. Pour les développeurs débutants, cela peut sembler un peu compliqué, mais vous vous y ferez avec un peu de temps et de travail.

L'équipe Ghost a créé une structure de dossier bien définie pour le développement de thèmes. C'est le moyen le plus simple de gérer le processus de développement de thèmes. Vous pouvez également utiliser des paquets npm pour améliorer le processus de développement et ajouter plus de fonctionnalités au thème. Dans mon thème, j'utilise Tailwind CSS et le paquet Gulp pour accélérer le processus de développement.