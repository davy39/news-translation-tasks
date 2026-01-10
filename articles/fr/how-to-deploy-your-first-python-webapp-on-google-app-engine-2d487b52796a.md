---
title: Un guide rapide pour déployer votre application web Python sur Google App Engine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T00:12:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-first-python-webapp-on-google-app-engine-2d487b52796a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BD_VuHYR7AmZpNo0Jsz6MA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Un guide rapide pour déployer votre application web Python sur Google App
  Engine
seo_desc: 'By Karan Asher

  The growth in the number of web-based applications and frameworks in the recent
  times is astounding. As companies such as Google, Amazon, and Microsoft provide
  more and more easy-to-use tools to build and deploy applications, it makes ...'
---

Par Karan Asher

La croissance du nombre d'applications et de frameworks basés sur le web ces derniers temps est stupéfiante. Alors que des entreprises comme Google, Amazon et Microsoft fournissent de plus en plus d'outils faciles à utiliser pour construire et déployer des applications, il est plus judicieux d'utiliser les services et outils qu'ils fournissent plutôt que de tout construire en interne et de l'héberger sur site.

Google App Engine est un excellent moyen de commencer à apprendre le développement web. Il offre une série de fonctionnalités utiles telles que le sharding, la réplication automatique de la base de données, la mise à l'échelle automatique, le memcache, et bien plus encore.

Cependant, le processus d'inscription et de déploiement de votre première application de test "hello world" n'est pas très intuitif.

Dans cet article, vous apprendrez une méthode très simple et facile à comprendre pour **déployer votre première application web Python sur Google App Engine. Alors, commençons.**

### Étape 1. Téléchargez les éléments de base nécessaires

Peu importe la plateforme sur laquelle vous construisez des produits, il y a toujours quelques éléments de base à mettre en place avant de pouvoir démarrer. Et le déploiement d'applications dans Google App Engine ne fait pas exception.

1. Téléchargez [Python 2.7](https://www.python.org/download/releases/2.7/)
Au moment de la rédaction de cet article, Google App Engine [ne prend en charge Python que jusqu'à la version 2.7](https://cloud.google.com/appengine/docs/standard/python/). Cependant, il n'est qu'une question de temps avant que le support pour Python 3.x soit ajouté. Vous pouvez consulter la documentation d'App Engine pour les dernières informations.
2. Téléchargez [Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/python/download)
Cela vous permettra de cloner des applications sur votre machine locale, d'apporter des modifications (éditer et développer l'application), et de déployer votre application sur le cloud.
3. Définissez le chemin de Python dans le lanceur de Google App Engine
Après avoir téléchargé le SDK, lancez le lanceur de App Engine, allez dans Edit -> Preferences et assurez-vous de définir le chemin où vous avez installé Python à l'étape 1 ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/ykQfsEj0zmdjjRFnxiLSFqOOjGF1lWdJYkGK)
_Définissez le chemin de Python dans le lanceur de Google App Engine_

C'est tout ce dont vous avez besoin. Votre machine locale devrait maintenant être prête à construire des applications web.

### Étape 2. Inscription à App Engine

C'est souvent la partie la plus confuse de toute l'installation. Voici ce que vous devez savoir lorsque vous vous inscrivez :

1. Actuellement, App Engine offre un essai gratuit d'un an.
2. L'essai inclut 300 $ de crédit qui peuvent être utilisés pendant la période d'essai d'un an.
3. Vous devrez ajouter une carte de crédit pour vous inscrire (à des fins de vérification).
4. Vous ne serez pas facturé pendant le processus d'inscription.
5. Vous ne serez pas facturé pendant la période d'essai tant que vous ne dépassez pas la limite de crédit offerte.

Voici les étapes à suivre pour vous inscrire :

1. Allez sur la page d'accueil de [Google Cloud](https://cloud.google.com/)
2. Suivez le processus d'inscription et allez sur votre tableau de bord App Engine

La majeure partie du travail est terminée après une inscription réussie.

### Étape 3. Créez un nouveau projet

L'étape suivante consiste à créer un nouveau projet Python sur lequel vous pourrez travailler. Suivez les captures d'écran ci-dessous pour créer un nouveau projet.

Lancez l'assistant de nouveau projet.

![Image](https://cdn-media-1.freecodecamp.org/images/gHQqw94gnz6i7FPB93bNNPMXoTCIHps5pKEN)
_Image courtoisie. [https://console.cloud.google.com/home](https://console.cloud.google.com/home" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/QcsRz0RUf6xmkrBwttFSLeqGLj5rRHqUePXF)
_Image courtoisie [https://console.cloud.google.com/home](https://console.cloud.google.com/home" rel="noopener" target="_blank" title=")_

Donnez un nom à votre application et notez votre identifiant de projet.

![Image](https://cdn-media-1.freecodecamp.org/images/Vxf5RJu080-wPyclcCkQYqHiXeS5uJwZIkbp)
_Image courtoisie. [https://console.cloud.google.com/home](https://console.cloud.google.com/home" rel="noopener" target="_blank" title=")_

Cliquez sur le bouton créer et Google devrait prendre quelques minutes pour configurer tout ce qui est nécessaire pour votre nouvelle application.

### Étape 4. Clonez l'application pour la développer localement

L'étape suivante du processus consiste à cloner l'application sur votre machine locale. Cela vous permettra d'apporter des modifications à l'application localement et de la déployer lorsque vous le souhaitez.

Allez dans le lanceur de Google App Engine et créez une nouvelle application.

![Image](https://cdn-media-1.freecodecamp.org/images/OYQUQ619PxSHi9DMmgMitKSChUuUF6JdTsYR)

Entrez l'identifiant de projet de votre nouvelle application. Indiquez également le dossier (destination locale) où vous souhaitez stocker l'application localement. Assurez-vous de sélectionner Python 2.7 comme moteur d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/8zCrS5i2DBzmxWur4iVctxlktlpYLbfka7aa)

Cliquez sur le bouton créer, et vous devriez voir votre application listée dans la fenêtre qui suit. Vous devriez également vérifier que vous voyez maintenant quelques fichiers dans votre stockage local (le répertoire que vous avez choisi dans la capture d'écran ci-dessus) après cette étape.

### Étape 5. Exécutez l'application localement

Avant d'apporter des modifications à l'application, il est important de vérifier si vous avez exécuté toutes les étapes ci-dessus correctement. Cela peut être fait simplement en exécutant l'application localement.

Sélectionnez l'application et cliquez sur le bouton d'exécution dans la fenêtre.

![Image](https://cdn-media-1.freecodecamp.org/images/s6uLNJX1RSlALzBAIyodKAZ6ijTwJ9O40Mom)

Attendez quelques secondes jusqu'à ce que vous puissiez cliquer sur le bouton **Parcourir**. Une fois que le bouton **Parcourir** devient cliquable, cliquez dessus. Cela devrait vous amener au navigateur, et vous devriez voir le texte "hello world" apparaître dans votre fenêtre de navigateur. Alternativement, vous pouvez aller manuellement dans le navigateur et utiliser le port spécifié pour accéder à l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/8P4dKa9dS8DMRug1p-jxwNaAyITijRwWGn2x)

Tant que vous voyez l'écran ci-dessus, vous êtes prêt.

### Étape 6. Comprendre la structure de l'application

Il est enfin temps de regarder les lignes de code qui exécutent cette application web. Ouvrez le dossier de votre application dans l'éditeur de texte de votre choix. Je recommande [Sublime Text](https://www.sublimetext.com/) ou [VS Code](https://code.visualstudio.com). Cependant, n'hésitez pas à choisir celui que vous préférez.

Voici une description des différents fichiers.

**app.yaml**

Ce fichier est un fichier de balisage de base qui stocke des informations (certaines métadonnées) sur l'application. Il est important de noter les parties cruciales suivantes du fichier.

1. **application**
Ceci est l'identifiant du projet que vous ne devez jamais changer. C'est l'identifiant unique de l'application
2. **url -> script**
Ceci est la page d'accueil de l'application. En d'autres termes, ce fichier sera rendu dans votre navigateur lorsque vous lancerez l'application
3. **libraries**
C'est ici que vous pouvez inclure des bibliothèques externes à utiliser dans l'application web

![Image](https://cdn-media-1.freecodecamp.org/images/3Yw98n-vBszn0AtjOTQZKHwyXQdAHFhLzasM)
_fichier app.yaml dans le dossier de l'application web_

**main.py**

Ceci est la page d'accueil de l'application (comme discuté ci-dessus). Notez que le texte "hello world" dans la fenêtre du navigateur (étape 5) est dû au code que vous voyez mis en évidence ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/FmhahIpA3gof3ZFwQf0JnA5px4KaqHqEDR6n)
_fichier main.py dans le dossier de l'application web_

### Étape 7. Apportez vos modifications et déployez la nouvelle application

Aucune application "hello world" n'est jamais complète sans que le développeur ne change le texte "hello world" en quelque chose d'autre juste pour s'assurer que tout ce qui se passe en coulisses fonctionne comme il se doit.

Allez-y et changez le texte dans la capture d'écran ci-dessus en quelque chose d'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/QitcnUiNGjFfYJeANmoPZZydYdMLYGc2D-do)
_fichier main.py dans le dossier de l'application web_

Enregistrez les modifications, allez dans le navigateur et actualisez la page. Vous devriez voir la page avec le texte "MEOW" affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/w7D7QiVHfJW0JCL3Dl3Ua8S7hNuApqU2psAt)

Enfin, il est temps de déployer vos modifications sur le cloud pour les rendre accessibles mondialement via une URL. Allez dans le lanceur de App Engine, sélectionnez l'application, et cliquez sur le bouton **Déployer**.

![Image](https://cdn-media-1.freecodecamp.org/images/breGh1hefgwsD5w7zR7yVtiujWPENETaPs9Z)

Cela garantira que votre application est déployée sur Google Cloud. Pour vérifier si tout s'est bien passé, allez à l'URL suivante :

**https://<votreIDdeProjet>.appspot.com/**

Vous devriez voir la même fenêtre que ci-dessus, sauf que maintenant, il s'agit d'une URL accessible mondialement.

![Image](https://cdn-media-1.freecodecamp.org/images/9wrAp6-bGh7bdzEjdaO2Gb1u38lA1wjhMQBd)

### Étape 8. Divers

Félicitations, vous avez enfin déployé votre première application web Python sur Google App Engine. Voici quelques autres points que vous pourriez trouver utiles.

1. [Jinja 2](http://jinja.pocoo.org/docs/2.10/) est une bibliothèque de templating front-end incroyable pour Python qui peut faire des choses cool, comme passer des objets de Python à HTML, utiliser des boucles for, des conditions if, et bien plus encore directement hors de la boîte
2. [Voici](https://classroom.udacity.com/courses/cs253) un cours Udacity très utile sur le développement web que j'ai personnellement trouvé très ressourçant
3. Voir les logs pendant l'exécution de votre application web peut être utile pour déboguer et découvrir également certains bugs à la volée

![Image](https://cdn-media-1.freecodecamp.org/images/saG-0CilWV6HYRdE9e7GhMEhVjk2k6yE7PFp)
_Console de logs de l'application web_

_#JusquàLaProchaineFois_.