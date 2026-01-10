---
title: 'Off With Their Heads: Comment construire un WordPress Headless pour gérer
  du contenu'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T20:32:17.000Z'
originalURL: https://freecodecamp.org/news/off-with-their-heads-building-a-headless-wordpress-to-manage-content-bb04e6b2a792
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vSKpWd9zJnRW3tTNz3tjKg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: 'Off With Their Heads: Comment construire un WordPress Headless pour gérer
  du contenu'
seo_desc: 'By Drew Dahlman

  Managing content can be a pain. Still, mentions of WordPress often bring about moans
  from some developers. Surely in 2018 there’s a better way.

  Well, let’s make a headless CMS and publish static JSON that can be consumed by
  a serverle...'
---

Par Drew Dahlman

Gérer du contenu peut être une corvée. Pourtant, les mentions de WordPress provoquent souvent des gémissements chez certains développeurs. Sûrement, en 2018, il existe une meilleure façon.

Eh bien, créons un CMS headless et publions du JSON statique qui peut être consommé par une application serverless — ou rendu côté serveur avec mise en cache pour une vitesse ultime ! Bonus pour cette approche : nous pouvons réduire les problèmes de sécurité ainsi qu'utiliser les données de notre CMS à plusieurs endroits. Et nous n'avons jamais à gérer les charges du serveur, car tout provient d'AWS S3.

Oui, WordPress dispose d'une API que vous pouvez utiliser. Mais l'objectif ici est d'éviter d'interfacer directement avec WordPress dans vos applications, gardez tout statique.

Pour ce post, j'ai créé un dépôt qui contient tout ce dont nous allons parler ici, mais ce post expliquera ce qui se passe et comment vous pourriez créer votre propre version de l'uploader et du parser.

Dépôt du projet : [https://github.com/DrewDahlman/headless-wordpress](https://github.com/DrewDahlman/headless-wordpress)
Plugin : [https://github.com/DrewDahlman/wp-headless](https://github.com/DrewDahlman/wp-headless)

### Introduction

Très bien — parlons un peu des objectifs de ce projet.

**Sécurité** : Puisque nous n'utiliserons pas WordPress de manière traditionnelle, nous pouvons cacher tout cela derrière une authentification ou même simplement garder le projet avec des sauvegardes de la base de données sur GitHub et, lorsque des modifications sont nécessaires, vous pourriez lancer le projet localement et publier.

**Vitesse** : Puisque nous publions des fichiers statiques sur S3, la seule fois où nous avons une charge sur notre base de données est lors de la publication de contenu et des modifications. En faisant cela, notre application ne fera qu'une seule requête, ou nous pourrions le diviser et charger selon nos besoins, ce qui rendra toujours une application plus rapide.

Une autre façon d'accélérer les choses est de faire du rendu côté serveur et de mettre en cache notre fichier de données, ce qui augmente encore la vitesse de livraison.

Cool, créons un WordPress headless.

Notez que le projet d'exemple est livré avec un fichier de base de données qui configurera automatiquement toutes les choses suivantes pour vous, mais n'hésitez pas à jouer avec. Vous devrez cependant fournir vos propres identifiants AWS pour que les téléchargements fonctionnent.

### Installation

La première chose que nous voulons faire est de lancer notre instance WordPress. Pour cela, j'utilise le dépôt d'exemple, mais vous pourriez le faire vous-même. Une fois que nous sommes en cours d'exécution, nous voudrons installer nos plugins. Pour cet exemple, j'utilise :

[Advanced Custom Fields Pro](https://www.advancedcustomfields.com/pro/)
[Custom Post Types](https://wordpress.org/plugins/custom-post-type-ui/)
[Amazon Web Services](https://wordpress.org/plugins/amazon-web-services/)
[Amazon s3 et Cloudfront](https://wordpress.org/plugins/amazon-s3-and-cloudfront/)
[WP Headless](https://github.com/DrewDahlman/wp-headless)

Avec juste ces plugins, nous sommes prêts à démarrer.

La première chose que nous voulons faire est de configurer AWS et notre bucket S3. Allez sur la page des paramètres AWS et entrez vos identifiants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZSx1XR3jStoJpwWgjuE3Rg.png)

Une fois que c'est prêt, configurons notre bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JGvMtWTHcCRrv3VnLZ4xJA.png)

Une fois que c'est configuré, configurons quelques types de publications et quelques champs personnalisés. Pour cet exemple, créons un type de publication personnalisé pour les émissions de télévision.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E78tGldFqDYZAxYZpSTCJQ.png)

Cool, maintenant créons quelques champs personnalisés : Nom, Couverture, À propos, et un répéteur de personnages avec nom et photo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ci5QG0oPAdcu2P2QptDS-g.png)

Très bien — maintenant que nous avons nos champs et types de publications configurés, la prochaine chose à faire est d'entrer du contenu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*r3EU5BnNUyRsB4jktYKCRg.png)

Avec un article créé, voyons maintenant comment cela fonctionne. Dans le plugin "Publish Site", il y a une page de contenu où nous pouvons configurer les fichiers que nous allons publier et leur structure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*047GrHnlbSDHT2tzxFX_Qg.png)

Configurer le contenu sur l'endroit où les fichiers doivent être téléchargés dans le bucket que nous avons configuré précédemment, puis donner un nom à notre fichier de données ainsi que sélectionner les articles, pages et médias que nous voulons.

Après cela, c'est aussi simple que d'enregistrer et de cliquer sur "Publish Staging" ou "Publish Production".

![Image](https://cdn-media-1.freecodecamp.org/images/1*UJofCINJ2ok9694KC5pW8g.png)

Boom ! Succès ! Vous devriez voir [quelque chose comme ceci](http://wp-headless-demo.s3.amazonaws.com/app-data/staging-shows.json).

Alors, examinons les données.

C'est un exemple simple, mais pour vos projets, vous pourriez avoir encore plus de données. Remarquez quelques choses intéressantes ici. Nous obtenons les données brutes de WordPress sur le slug et autres, mais nous obtenons également tous nos champs ACF ainsi que des objets image et, si nous le voulions, des articles liés ou des galeries — tout ce que vous voulez créer !

Comment cela fonctionne-t-il ?

### Le Code

Cool, donc maintenant nous avons tout cela qui fonctionne. Mais comment cela fonctionne-t-il ? Et comment pouvez-vous créer quelque chose de similaire avec vos propres modifications pour la publication ? Parfois, vous ne voulez peut-être aucune des données brutes de WordPress, peut-être juste un slug et un ID.

Examinons le plugin wp-headless. Je l'ai fait en tant que plugin car il est plus facile de gérer les hooks de cycle de vie, mais aussi en gardant l'idée que nous pouvons garder tout cela vivant de manière indépendante. Peut-être que vous voulez toujours utiliser le thème traditionnel, mais aussi avoir cette option.

[**DrewDahlman/wp-headless**](https://github.com/DrewDahlman/wp-headless/blob/master/wp-headless/wp-headless.php)
[_wp-headless - Un plugin simple pour publier des fichiers JSON statiques à partir de WordPress pour un CMS headless._github.com](https://github.com/DrewDahlman/wp-headless/blob/master/wp-headless/wp-headless.php)

En examinant le code, tout est assez simple. Le plugin est bien car il vérifie les dépendances et configure la page de publication initiale avec les essentiels pour la rendre plus facile. Vous pourriez totalement créer votre propre version de cela si vous vouliez d'autres options ou des options plus raffinées.

Une chose intéressante ici aussi est la configuration des environnements, donc nous pouvons avoir un staging-FILENAME.json et production-FILENAME.json.

Là où les choses deviennent intéressantes, c'est autour de la ligne 134 où nous avons une fonction récursive qui analyse un article.

Cela est appelé par notre fonction de publication qui boucle sur le champ de contenu dans notre page de paramètres du site de publication.

En bouclant sur chacun de nos potentiels buckets de contenu — ainsi que les articles à l'intérieur de ceux-ci — nous appelons parse post qui boucle sur chaque champ de WordPress puis vérifie les champs ACF que nous pouvons avoir.

Cela a la capacité d'aller un niveau plus profond en termes de champs de relation. (Cela est principalement dû au fait qu'un article lié peut référencer cet article, ce qui continuerait indéfiniment en imbriquant et en reliant.)

Quelques autres choses ici : nous générons un nom aléatoire pour notre fichier et l'enregistrons localement avant de le télécharger. Si cela réussit, nous supprimons le répertoire et le fichier aléatoires et le site est publié.

L'uploader est également simple, il utilise les plugins AWS que nous avons configurés précédemment pour déterminer le bucket de destination. Notez que vous pourriez absolument ajouter plusieurs langues à ces publications en ajoutant un paramètre pour vérifier WPML si vous l'utilisez et en ajoutant quelque chose comme staging-es-FILENAME.json ou autre chose.

L'uploader obtient le nom de fichier, un fichier temporaire et la destination finale. Cela vérifie avec nos plugins et télécharge sur S3.

Maintenant que tout cela est configuré et fonctionne, vous pouvez consommer ce fichier S3 n'importe où ! Les façons dont j'ai utilisé cette configuration ont été de mettre une installation WordPress sur un serveur sous un sous-domaine avec authentification avant la connexion, comme [https://admin.example.com](https://admin.example.com). Cela cache à nouveau WordPress du monde et ajoute une couche de sécurité à votre application.

Vous pourriez même avoir une autre application vivant sur votre serveur qui consomme depuis S3 et rend côté serveur. Les avantages de tout cela sont une meilleure sécurité, plus d'options pour consommer le contenu et des charges de serveur plus faibles.

Une autre option que vous pouvez prendre est de faire un dump de la base de données après avoir fait des modifications et de l'enregistrer dans un dépôt GitHub et de permettre aux membres de l'équipe de télécharger, de lancer le site, de faire des modifications et de publier. Encore une fois, en gardant les choses sécurisées sans se soucier des vulnérabilités.

Consultez à nouveau le plugin sur GitHub et le projet d'exemple pour voir comment cela fonctionne !

[**DrewDahlman/wp-headless**](https://github.com/DrewDahlman/wp-headless)
[_wp-headless - Un plugin simple pour publier des fichiers JSON statiques à partir de WordPress pour un CMS headless._github.com](https://github.com/DrewDahlman/wp-headless)