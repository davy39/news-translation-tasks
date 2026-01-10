---
title: Comment déployer un site web statique gratuitement en seulement 3 minutes directement
  depuis votre Google Drive, en utilisant Fast.io
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2020-01-15T12:24:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-static-website-for-free-in-only-3-minutes-with-google-drive
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/how-to-deploy-a-static-website-for-free-in-only-3-minutes-with-google-drive-1.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: Comment déployer un site web statique gratuitement en seulement 3 minutes
  directement depuis votre Google Drive, en utilisant Fast.io
seo_desc: 'In this article, I''ll show you how to deploy a static website for free
  in only 3 minutes, using a cloud storage service like Google Drive or Dropbox.

  And no - fast.io didn''t pay me or freeCodeCamp to create this article. We don''t
  have any relationshi...'
---

Dans cet article, je vais vous montrer comment déployer un site web statique gratuitement en seulement 3 minutes, en utilisant un service de stockage cloud comme Google Drive ou Dropbox.

Et non - fast.io ne m'a pas payé ni freeCodeCamp pour créer cet article. Nous n'avons aucune relation avec eux. J'écris simplement à ce sujet parce que j'ai trouvé leur outil vraiment excitant et utile pour héberger rapidement des sites web statiques gratuitement.

_Note : Les informations dans ce tutoriel sont maintenant obsolètes, mais cet article reste ici pour la postérité. [Voici quelques articles utiles que vous pourriez aimer](https://www.freecodecamp.org/news/search?query=static%20website) sur un sujet similaire._

## Qu'est-ce que Fast.io ?

Fast.io est une solution créée par Mediafire pour simplifier le fonctionnement du web. En quelques mots, leur objectif est de faciliter votre vie en rendant le web plus accessible et plus facile à gérer.

Il a été lancé à la fin de 2019, donc je vous le partage maintenant.

## Comment ça marche

Lorsque vous utilisez Fast.io, vous pourrez vous connecter à votre cloud (Google Drive, DropBox, etc.), choisir un nom de site web et déployer votre contenu en quelques clics.

Si votre contenu est prêt, seulement 3 minutes sont nécessaires pour mettre votre contenu en ligne et le rendre accessible à tous.

Une fois votre site web en ligne, vous pouvez le configurer, ajouter un nom de domaine personnalisé et connecter Google Analytics pour savoir combien de personnes vous atteignez.

Je ne l'ai pas encore mentionné, mais le service met automatiquement à jour votre site web une fois que vous modifiez les fichiers sources. Par exemple, si vous utilisez Google Drive pour partager votre contenu, une fois que vous changez quelque chose dans votre page HTML, elle sera mise à jour.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-how-it-works.png)
_Fast.io - [Comment ça marche](https://fast.io/)_

### Fournisseurs de stockage disponibles

Voici une liste des fournisseurs de stockage disponibles si je devais publier mon site web aujourd'hui :

* GitHub
* Dropbox
* Google Drive
* Box
* Mediafire
* OneDrive

Comme vous pouvez l'imaginer, cette liste va s'allonger à mesure que de nouveaux services seront ajoutés. Mais même maintenant, vous avez de nombreuses possibilités pour héberger votre site web statique.

## Concurrents

Il existe déjà un certain nombre d'entreprises différentes qui vous permettent de mettre rapidement un site web statique en ligne. Les solutions les plus connues sont GitHub Pages, Heroku et Netlify.

Je ne dis pas nécessairement que Fast.io est le meilleur, mais j'aime la simplicité avec laquelle on peut déployer un site web de base.

Note rapide : si vous voulez déployer quelque chose de plus complexe – comme un site web Python Flask – vous ne pouvez pas le faire avec Fast.io. Dans ce cas, je vous recommande vivement d'utiliser Heroku.

Comme je vous l'ai dit, je vais être transparent avec vous. Fast.io est un excellent service pour certaines tâches.

## Qu'est-ce qu'un site web statique ?

Avant de vous montrer comment déployer votre site web, je pense qu'il est essentiel de définir ce qu'est un site web statique et quelles sont les différences avec un site dynamique.

Un site web statique contient des pages web avec un contenu fixe. Le contenu de votre page est en HTML, et tous les utilisateurs voient la même chose.

Par exemple, vous pouvez utiliser ce type de site lorsque vous voulez faire une page de destination pour votre site web (une page de base avec des informations sur votre produit).

La principale différence entre cela et un site web dynamique est, bien sûr... la partie dynamique !

Un site web dynamique utilise une technologie serveur pour construire la page lorsqu'un utilisateur demande le site web.

Par exemple, vous pouvez utiliser ce type de site pour votre blog. Chaque fois que vous ajoutez un nouvel article à votre base de données, le site web l'affichera.

## Il est temps de déployer votre site web

Êtes-vous prêt à partager votre page avec tout le monde ? Faisons-le !

Dans cette partie, je vais vous montrer comment mettre votre site web en ligne en quelques clics. Je vais utiliser une page HTML de base, mais une fois que vous comprendrez comment Fast.io fonctionne, vous serez libre de tout modifier.

### 1) Créer un fichier index.html

Vous devez créer un fichier index.html avec votre code HTML à l'intérieur. Je vous recommande de commencer par quelque chose de simple car vous pourrez toujours le mettre à jour plus tard.

Enregistrez le fichier sur votre ordinateur.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Mon Site Web Statique</title>
  </head>
  <body>
    <h1>Mon Site Web Statique</h1>
    <p>
      Bonjour, je suis en ligne, et tout le monde peut me voir !
    </p>
  </body>
</html>
```

### 2) Ouvrir la page d'accueil de Fast.io

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-homepage.png)
_[Fast.io](https://fast.io) page d'accueil_

Tout ce que vous avez à faire pour commencer avec Fast.io est d'ouvrir le site web. Une fois que vous l'avez fait, cliquez sur **"Inscrivez-vous maintenant - c'est gratuit !"**.

### 3) Configurer Google Drive

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-storage-provider.png)
_Fast.io - Fournisseur de stockage_

Cette page apparaît après l'étape 2 et vous permet de sélectionner un fournisseur de stockage. Sélectionnez **"Google Drive"**.

Si vous voulez créer un site web avec un autre fournisseur, vous pouvez le faire plus tard en l'ajoutant via votre page de compte.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-connect-google-drive.png)
_Fast.io - Connecter Google Drive_

Fast.io a besoin d'accéder à votre compte Google Drive pour fonctionner. Ils créeront un dossier "Fast.io" pour contenir votre/vos site(s) web. Cliquez sur **"Connecter Google Drive Maintenant"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-select-google-account.png)
_Fast.io - Sélectionnez votre compte Google_

Vous devez **sélectionner votre compte Google** pour le lier avec Fast.io.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/fast-io-allow-google.png)
_Fast.io - Autoriser Fast.io à accéder à Google Drive_

Vous devez **autoriser Fast.io à accéder à votre compte Google** pour le lier correctement.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-create-account.png)
_Fast.io - Créer votre compte_

Votre compte est maintenant prêt, il vous suffit de choisir un mot de passe puis de **cliquer sur "Créer un compte"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-welcome.png)
_Fast.io - Page de bienvenue_

Lorsque votre compte est prêt, une page "Bienvenue sur Fast !" apparaîtra. **Cliquez sur "Commençons !"**.

### 4) Créer votre site web

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-add-new-website.png)
_Fast.io - Tableau de bord_

Vous êtes prêt à créer votre site web et à le partager avec tout le monde ! **Cliquez sur "Ajouter un nouveau site"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-website-name.png)
_Fast.io - Choisir un nom de site web_

**Choisissez le nom de votre site web et tapez-le** dans la boîte de saisie. Lorsque vous avez terminé, **cliquez sur "Suivant"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-select-website-type.png)
_Fast.io - Choisir un type de site web_

Fast.io vous permet de créer trois types de sites web : un site web de partage de fichiers, une page web ou un site web de navigateur de fichiers.

Dans notre cas, nous allons **sélectionner "Pages Web"** parce que nous voulons héberger une page web HTML.

Si plus tard vous voulez créer un site web pour partager des documents, vous devez retourner à votre tableau de bord, en créer un nouveau et sélectionner Téléchargements de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-select-google-drive.png)
_Fast.io - Choisir un fournisseur de stockage pour votre site web_

Une fois que vous avez cliqué sur "Pages Web", vous devez sélectionner votre fournisseur de stockage. **Cliquez sur "Google Drive"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-select-url.png)
_Fast.io - Choisir l'URL de votre site web_

**Choisissez l'URL de votre site web et tapez-la** dans la boîte de saisie. Lorsque vous avez terminé, **cliquez sur "Créer le site"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-success.png)
_Fast.io - Site web créé avec succès_

Vous l'avez fait ! Votre site web est en ligne et disponible à l'URL que vous avez choisie. Dans mon cas, vous pouvez trouver mon site sur [mygoogledrivewebsite.imfast.io](https://mygoogledrivewebsite.imfast.io)

### 5) Télécharger votre index.html

Si vous ouvrez votre site web, vous pourriez remarquer une erreur car vous n'avez pas téléchargé votre fichier index.html sur votre Google Drive.

Voici deux façons de le faire :

* **Ouvrez votre Google Drive et recherchez le dossier Fast.io**, puis le dossier de votre site web (dans mon cas, "mygoogledrivewebsite.imfast.io").
* Sur la page de succès de l'étape 4, **cliquez sur "Voir votre Google Drive"**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-google-drive-upload.png)
_Fast.io - Google Drive avant le téléchargement_

Une fois que vous avez fait cela, **faites un clic droit avec votre souris et sélectionnez "Télécharger des fichiers"**. Une nouvelle fenêtre s'ouvrira, **trouvez votre fichier "index.html" - sélectionnez-le**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-google-drive.png)
_Fast.io - Google Drive après le téléchargement_

Attendez un peu avant que le changement n'apparaisse sur votre site web.

### 6) Célébrez !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/fast-io-website-demo.png)
_Fast.io - Démonstration du site web_

Faites passer le mot à tous vos amis ! Votre site web est en ligne et tout le monde peut le voir !

 ? [Partagez-le sur Twitter en cliquant ici !](https://ctt.ac/Me7Uk) ?

### 7) Bonus

Si vous êtes curieux et que vous voulez tout configurer, vous pouvez retourner à votre tableau de bord et cliquer sur votre site web.

Vous pourrez lier votre site web à Google Analytics (statistiques des visiteurs), changer votre nom de domaine (par exemple, mon-site-web.com), et bien plus encore !

## Conclusion

Que pensez-vous de ce nouveau service ? L'avez-vous trouvé rapide et facile ?

N'hésitez pas à partager cet article si vous l'avez aimé.

Si vous voulez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/), où je tweete sur le développement web, l'amélioration de soi et mon parcours en tant que développeur full stack !

###