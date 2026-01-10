---
title: 'Hugo + Firebase : Comment créer votre propre site web statique gratuitement
  en quelques minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T20:26:08.000Z'
originalURL: https://freecodecamp.org/news/hugo-firebase-how-to-create-your-own-dynamic-website-for-free-in-minutes-463b4fb7bf5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KAeUHR7NoyfTxOHsfPjqCw.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Hugo + Firebase : Comment créer votre propre site web statique gratuitement
  en quelques minutes'
seo_desc: 'By Aravind Putrevu

  Ever thought of having your own website for putting up your project portfolio or
  resume or a blog for yourself. By the end of this article, you will be able to create
  one.

  Generally, to develop a website you need to know HTML, CSS,...'
---

Par Aravind Putrevu

Vous avez déjà pensé à avoir votre propre site web pour y mettre votre portfolio de projets, votre CV ou un blog personnel ? À la fin de cet article, vous serez capable d'en créer un.

Généralement, pour développer un site web, vous devez connaître le HTML, le CSS et un peu de JavaScript (parfois). Mais pour cela, vous n'avez pas besoin d'avoir des compétences en codage. Vous avez juste besoin de compétences informatiques de base.

Pour mettre en ligne un site web, vous devez avoir un "espace" (aka hébergement) où tous vos fichiers seront téléchargés. Chaque fois que quelqu'un tape votre site web et clique sur entrer, ce sont ces fichiers qui sont servis/présentés à l'utilisateur sur le navigateur.

Commençons par ce que vous devez avoir/connaître :

#### Compte Google

Je crois que vous avez déjà un compte Gmail, ce qui suffit. Sinon, créez-en un.

#### Domaine

Ceci est optionnel. Il existe divers fournisseurs de noms de domaine dans le monde, vous pouvez également en acheter un chez [Google](https://www.google.co.in/search?q=buy+a+domain+name). Vous pouvez trouver une liste de fournisseurs de noms de domaine. C'est aussi simple que de faire des achats sur [Amazon](http://amazon.com).

#### Hugo

[Hugo](https://gohugo.io/) est un outil basé sur le langage [Go](https://golang.org/), qui génère des sites web statiques. Vous pouvez utiliser divers modèles et créer différents types de sites web comme des blogs, des sites de portfolio, etc.

Téléchargez-le depuis [ici](https://github.com/gohugoio/hugo/releases).

#### Firebase

[Firebase](http://firebase.com/) est une plateforme pour applications mobiles et web, acquise par Google il y a quelques années. Firebase offre l'hébergement comme l'une de ses fonctionnalités. Cependant, de nombreux développeurs mobiles l'utilisent pour l'analytique, les notifications, les rapports de plantage des applications. Nous allons l'utiliser pour héberger notre site web.

#### Node.js

Node.js est un environnement d'exécution JavaScript open-source construit sur le [moteur V8 JavaScript de Chrome](https://developers.google.com/v8/). Pour ce tutoriel, vous devez l'installer sur votre machine pour que les outils Firebase fonctionnent. Vous pouvez le télécharger et l'installer depuis [ici](https://nodejs.org/en/download/).

#### Étape 1 : Installer Hugo sur votre machine

Windows : Vous obtiendrez un simple fichier exécutable portable. Vous pouvez le placer n'importe où et l'exécuter via la ligne de commande. Vous pouvez l'ajouter à votre variable de chemin dans les variables d'environnement Windows pour qu'il soit référencé n'importe où.

Mac : Vous pouvez l'installer en utilisant Homebrew. Si vous n'avez pas brew installé sur votre mac, vous pouvez télécharger le tarball depuis [ici](https://github.com/gohugoio/hugo/releases).

Dans les deux cas, assurez-vous de pouvoir accéder à Hugo en donnant la commande ci-dessous.

#### Étape 2 : Créer un site de modèle

Rendez-vous à l'emplacement où vous avez décidé de créer votre site web et entrez la commande ci-dessous :

```
$ hugo new site <chemin_vers_le_dossier>
```

À l'emplacement donné, vous pouvez voir une structure de dossier comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/Gxfil53Td3cs6jmv9qEIBw6eGeRSPG6bzfi5)
_Image prise sur Windows 10_

Ces dossiers sont simplement des espaces réservés pour votre contenu. Tout le contenu textuel de votre site va dans le dossier _content_.

Vous pouvez exécuter les commandes ci-dessous pour ajouter de nouveaux fichiers.

```
$ hugo new about.md
```

Si vous souhaitez ajouter un article de blog, créez un dossier nommé "_blog_" dans le dossier "_content_" et commencez à ajouter vos fichiers. Ces fichiers ont une extension "_.md_" qui sont des fichiers [Markdown](https://en.wikipedia.org/wiki/Markdown).

Markdown est un langage de balisage de formatage de texte brut. Il est joli et facile. Il existe de nombreux guides sur la façon d'aborder Markdown, en voici [un](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

#### Étape 3 : Définir un thème pour le site

Hugo a une grande communauté. Leur site de [thèmes](https://themes.gohugo.io/) est enrichi de différentes catégories de thèmes de sites web. Rendez-vous sur ce site et sélectionnez un thème qui correspond à vos besoins.

J'ai choisi le thème [Introduction](https://github.com/vickylaiio/hugo-theme-introduction). En cliquant sur le bouton de téléchargement, vous serez redirigé vers [GitHub](https://github.com/vickylaiio/hugo-theme-introduction).

Chaque thème a sa propre façon de configurer les choses. Ce thème particulier n'a pas beaucoup d'étapes. Il suffit de cloner ou de télécharger le zip dans le dossier des thèmes. Copiez le fichier _config.toml_ dans le dossier racine de votre site web.

#### Étape 4 : Configurer vos préférences

Ouvrez le fichier _config.toml_ et commencez à le modifier. Donnez votre nom et autres détails que vous souhaitez afficher sur le site web. Certains thèmes supportent Google Analytics afin que vous puissiez suivre le nombre de visites des utilisateurs, etc. Vous pouvez donner votre identifiant GA pour collecter des données.

#### Étape 5 : Configurer un projet d'hébergement Firebase

Comme je l'ai mentionné précédemment, [Firebase](https://en.wikipedia.org/wiki/Firebase) est une belle plateforme mobile avec une tonne de fonctionnalités. J'ai utilisé l'hébergement Firebase pour héberger mon site web statique généré via Hugo.

Pour utiliser les services Firebase, utilisez votre compte Google et [connectez-vous au site web de Firebase](https://firebase.google.com/).

Cliquez sur "Go to console." Créez un projet en lui donnant un nom. Vous verrez une page d'aperçu dans laquelle vous devez sélectionner "getting started on Hosting."

#### Étape 6 : Configurer les outils Firebase sur votre machine

Ouvrez votre terminal/interface de ligne de commande sur votre machine et tapez la commande ci-dessous.

```
$ npm install -g firebase-tools
```

La commande ci-dessus installe le package Firebase-tools. Vous devez exécuter quelques commandes supplémentaires pour pouvoir déployer votre site web directement.

```
$ firebase login
```

Cette commande connecte votre machine au projet Firebase. Elle vous permet de lister et de sélectionner le projet auquel vous souhaitez pousser vos modifications.

```
$ firebase list
```

Vous pouvez exécuter la commande ci-dessus pour voir le projet que vous avez créé. Une dernière touche à l'ensemble du flux de travail, nous devons initialiser le dossier racine de votre site web en tant que racine du projet Firebase.

```
$ firebase init
```

Il vous posera quelques questions comme

* Quelles fonctionnalités de l'interface de ligne de commande Firebase souhaitez-vous configurer ? Réponse : Hébergement.
* Sélectionnez un projet Firebase par défaut pour ce répertoire Réponse : Sélectionnez le projet Firebase que vous avez créé dans l'étape 5.
* Voulez-vous utiliser comme votre répertoire public ? Réponse : Oui.
* Configurer comme une application monopage ? Réponse : Oui.

Pour éviter toute confusion, j'ai détaillé des captures d'écran prises à chaque étape pour votre référence. Elles peuvent être téléchargées [ici](https://www.dropbox.com/s/z6siqqymi1rin0u/Screenshots_Firebase_Tools_Setup.zip?dl=0).

Enfin ! L'initialisation de Firebase est terminée.

#### Étape 7 : Vérifier votre site web localement

Exécutez la commande ci-dessous pour vérifier votre site localement sur votre machine.

```
$ hugo server -w
```

Hugo est livré avec un serveur web léger et haute performance, où vous pouvez vérifier toutes vos modifications. Assurez-vous que toutes vos images sont placées dans le dossier _static/img_. Dans un processus itératif, modifiez votre _config.toml_ et vérifiez ceux-ci sur le navigateur. Ci-dessous se trouve le port sur lequel votre serveur sera en cours d'exécution.

```
http://localhost:1313
```

#### Étape 8 : Déployer votre site web

Tapez la commande ci-dessous pour générer votre site et le pousser vers le projet Firebase correspondant que vous avez configuré dans l'**étape 5**.

```
$ hugo && firebase deploy
```

#### Étape 9 : Le connecter à votre domaine (optionnel)

Firebase offre une option pour connecter votre domaine à l'application Firebase. Cliquez sur _connect domain_ et donnez votre domaine et ajoutez les enregistrements TXT pour vérifier la propriété de votre domaine.

![Image](https://cdn-media-1.freecodecamp.org/images/bgk-Sh1N99CJ2qImzFWdiVnO7YdR-EGMw0K4)

Pour cela, connectez-vous à votre portail d'enregistrement de domaine.

#### Étape 10 : Créer un article de blog

Créer un article de blog est assez simple. Hugo comprend les fichiers markdown. Rendez-vous simplement dans _content->b_log folder (l'emplacement du dossier dépend du thème). Créez un fichier markdown. Répétez l'étape 8 pour voir les résultats.

Si vous avez des questions ou des doutes, vous pouvez me DM sur [twitter](https://twitter.com/aravindputrevu) !

Toujours heureux d'aider !