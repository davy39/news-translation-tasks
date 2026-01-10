---
title: Comment déployer une application React sur Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T17:35:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-application-to-netlify-363b8a98a985
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hxXLMsJtGQCg2RNAdXd3bQ.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
seo_title: Comment déployer une application React sur Netlify
seo_desc: 'By Abhishek Jakhar

  I’m going to teach you how to deploy and host your React app with Netlify.Netlify
  is a service that automates builds, deployments and manages your websites. It’s
  one of the fastest and easiest deployment solutions these days.

  Netli...'
---

Par Abhishek Jakhar

Je vais vous apprendre comment déployer et héberger votre application React avec Netlify. 
**Netlify** est un service qui automatise les builds, les déploiements et gère vos sites web. C'est l'une des solutions de déploiement les plus rapides et les plus faciles ces jours-ci.

[**Netlify**](https://www.netlify.com/) offre un plan gratuit. Donc d'abord, nous allons nous connecter à [**Netlify**](https://www.netlify.com/) en utilisant l'une des options (Github, Gitlab, Bitbucket, Email) données sur la page de connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/JVM7UWA0NJZBlBLjw9VovVR4B42w-Wp5LR1C)

![Image](https://cdn-media-1.freecodecamp.org/images/SnfWQ7EEIA5ni1Q0jSNotjADvHuH0jdtDpfK)

![Image](https://cdn-media-1.freecodecamp.org/images/o1fu3AiHPI8NBgsxRTUGsklGgVGi1kA6JbvJ)
_**Gauche** (Page de connexion) **Centre** (Autorisation) **Droite** (Application en ligne Netlify)_

Nous allons commencer par créer un build de notre application en exécutant cette commande :

```
npm run build
```

Ainsi, notre dossier build sera généré, contenant tous les fichiers prêts pour la production.

Maintenant, il y a **deux façons** de déployer notre application sur Netlify.

#### **Glisser-déposer**

Netlify a rendu cela si facile que nous devons simplement **glisser-déposer** notre **dossier build** dans leur **application en ligne** (image la plus à droite ci-dessus), et notre application sera déployée sur une URL live.

> **Note :** L'application en ligne Netlify est l'écran qui apparaît après vous être connecté à votre compte Netlify.

![Image](https://cdn-media-1.freecodecamp.org/images/Val5BuZKW8cVCM8TZ3UUWnezqGOy5SvKYbek)
_**Glisser-déposer** le dossier **build** vers l'**Application en ligne Netlify** pour déployer_

#### **Netlify CLI**

Netlify propose également une interface en ligne de commande qui vous permet de déployer votre application directement depuis la ligne de commande. C'est ce que nous allons faire maintenant.

Donc d'abord, nous allons installer le CLI en utilisant la commande suivante :

```
npm install netlify-cli -g
```

Maintenant, nous sommes prêts à la déployer. Pour déployer l'application, nous devons nous assurer que nous sommes dans le dossier du projet et ensuite nous allons exécuter cette commande :

```
netlify deploy
```

Nous pourrions obtenir une fenêtre pop-up qui nous demandera de nous connecter avec Netlify et d'accorder l'accès au **Netlify CLI**.

![Image](https://cdn-media-1.freecodecamp.org/images/7Y2-XpgfmWPO-JBB6UgyuqeCyRTOqCHCgGT9)
_Fenêtre pop-up vous demandant de vous connecter avec Netlify et d'accorder l'accès au Netlify CLI_

Maintenant, nous cliquerons sur Autoriser. Maintenant que nous sommes autorisés, nous pouvons suivre les invites de la ligne de commande pour déployer l'application.

#### Invites de la ligne de commande

1. Dans la console, il est écrit que « **Ce dossier n'est pas lié à un site pour l'instant. Que souhaitez-vous faire ?** » Il veut savoir si nous voulons lier ce répertoire à un site existant ou créer et configurer un nouveau site. Comme il s'agit d'un nouveau site, nous sélectionnerons **Créer et configurer un nouveau site**.

![Image](https://cdn-media-1.freecodecamp.org/images/jCjmOzAhGxe8iQTkmDWB6qjTjwecSm2Wxcq6)

2. Il nous donne l'option de donner un nom à notre site. Je vais taper **portfolio sur netlify** (Vous pouvez taper n'importe quel nom disponible que vous aimez).

![Image](https://cdn-media-1.freecodecamp.org/images/biH9rSuAPba39ANKe-jGWcJC5biol2bVmQrh)

3. Maintenant, il demandera le compte Netlify que vous souhaitez utiliser, donc je vais sélectionner **mon compte (Abhishek Jakhar)**, vous pouvez sélectionner le vôtre.

![Image](https://cdn-media-1.freecodecamp.org/images/shXwNfAQX9ecLo6fxTGFLC2zItwK3PlUZTa7)

4. Maintenant, en tant que chemin de déploiement, nous devons spécifier le répertoire de build de notre projet qui contient les assets pour le déploiement. Donc, nous allons taper **build** là et appuyer sur entrer.

![Image](https://cdn-media-1.freecodecamp.org/images/o0zMKENf5BfzR81Ej7jQbOtgDsvNUytgsB9i)

5. Maintenant, notre site sera créé et sera déployé sur une URL de draft en premier, que nous pouvons voir en copiant et collant l'URL dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/w7qhwqu6ONS81HFHoTzSlTN2eHhAaHgQ-Eoz)

Maintenant, de retour dans la console, il est écrit **"Si tout semble bon sur votre URL de draft, passez en live avec le flag --prod"**.

Donc pour rendre notre application live, nous allons exécuter la commande montrée sur la ligne de commande

```
netlify deploy --prod
```

Il nous demandera une fois de plus de spécifier le chemin de déploiement pour le build live qui est à nouveau notre dossier build.

![Image](https://cdn-media-1.freecodecamp.org/images/wDrwvxPQo9IN3KFg1UO4V0CXfeGUFCvkKr7C)

Maintenant, dans la sortie de la console, nous obtenons deux URLs. Une **URL de déploiement unique**, qui représente l'URL unique pour chaque déploiement individuel, et une **URL live** qui affiche toujours votre dernier déploiement.

Ainsi, chaque fois que vous mettez à jour votre site web et le déployez, vous allez obtenir une URL unique pour ce déploiement. En gros, si nous déployons plusieurs fois, nous aurons **plusieurs URLs uniques** afin que vous puissiez diriger les utilisateurs vers une **version spécifique** de votre application. Mais l'**URL live** affiche toujours vos **dernières modifications** à la même URL.

> **Note :** Netlify sécurise automatiquement votre site via **HTTPS** **gratuitement**.

#### Erreur Page Non Trouvée

![Image](https://cdn-media-1.freecodecamp.org/images/4skG2qD8TRKYRPFAjVSQ0dgEzrD2PECpdFPi)
_**Erreur 404** lorsque nous actualisons l'application après avoir navigué vers une route différente_

Si vous publiez une application qui utilise un routeur comme React Router, vous devrez configurer des redirections et des règles de réécriture pour vos URLs. Parce que lorsque nous cliquons sur un élément de navigation pour changer de page (route) et actualisons le navigateur, nous obtenons une page d'erreur 404.

Ainsi, Netlify facilite la configuration des redirections et des règles de réécriture pour vos URLs. Nous devons ajouter un fichier à l'intérieur du dossier build de notre application nommé _redirects. À l'intérieur du fichier, nous devons inclure la règle de réécriture suivante.

```
/*    /index.html  200
```

Cette règle de réécriture va servir le fichier index.html au lieu de donner une erreur 404, peu importe quelle URL le navigateur demande.

![Image](https://cdn-media-1.freecodecamp.org/images/sXFzzGd39iKJRWwS1syabew0T-GSjCaQI5kw)
_Le fichier **_redirects** à l'intérieur du dossier build contenant la **règle de redirection**_

Ainsi, maintenant, pour voir les dernières modifications dans l'URL live, nous devons déployer avec `netlify deploy`. Encore une fois, nous spécifierons build comme chemin de déploiement. Maintenant, lorsque nous voyons l'URL live et actualisons l'application après avoir changé de route, nous ne verrons plus la page d'erreur 404.

![Image](https://cdn-media-1.freecodecamp.org/images/HD3tmNtrQ0udjfcEry7TJgkDE0XK2FU5xLYF)

C'est tout. Sur netlify.com, vous pouvez voir les paramètres de votre site. Là, vous pouvez faire des choses comme configurer un domaine personnalisé ou connecter le site à un dépôt GitHub.

[**Netlify : Plateforme tout-en-un pour automatiser les projets web modernes**](https://www.netlify.com/)  
[_Déployez des sites web statiques modernes avec Netlify. Obtenez CDN, déploiement continu, HTTPS en 1 clic, et tous les services dont vous avez besoin...www.netlify.com](https://www.netlify.com/)

J'espère que vous avez trouvé cet article informatif et utile. J'adorerais avoir votre retour !

**Merci d'avoir lu !**