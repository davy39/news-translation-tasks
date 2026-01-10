---
title: Erreur 403 Forbidden Expliquée - Comment Corriger Ce Code d'Erreur HTTP ?
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-03T19:02:00.000Z'
originalURL: https://freecodecamp.org/news/error-403-forbidden-explained-how-can-i-fix-this-http-error-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/403-error.png
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: Erreur 403 Forbidden Expliquée - Comment Corriger Ce Code d'Erreur HTTP
  ?
seo_desc: "So you have encountered a 403 Forbidden error and you are wondering what\
  \ it means. \nThis error is an HTTP status code which means that you are forbidden\
  \ from accessing the page or resource that you are trying to reach. Unless you are\
  \ the person who c..."
---

Vous avez rencontré une erreur **403 Forbidden** et vous vous demandez ce que cela signifie. 

Cette erreur est un code d'état HTTP qui signifie que vous êtes interdit d'accéder à la page ou à la ressource que vous essayez d'atteindre. À moins que vous ne soyez la personne qui a créé le site web, il n'y a souvent rien que vous puissiez faire. Cependant, il y a quelques choses qui pourraient aider.

Il est possible que le créateur du site web ait configuré les permissions correctement et vous interdise intentionnellement l'accès à la page. Mais cette erreur pourrait également indiquer que le site web a été configuré incorrectement.

Voici quelques choses que vous pouvez essayer pour corriger l'erreur 403 Forbidden.

### 💡 Vérifiez et actualisez

Tout d'abord, vérifiez que l'URL est correcte et actualisez la page. C'est la première chose à faire lorsque vous rencontrez une erreur sur un site web. 

La plupart des serveurs web sont configurés pour retourner une erreur 403 Forbidden si quelqu'un essaie d'accéder à un répertoire sur le serveur au lieu d'un fichier (comme un fichier HTML). Vous avez peut-être mal tapé l'URL et essayez d'accéder à un répertoire.

### ✨ Effacer le cache du navigateur

Une version mise en cache de la page pourrait causer le problème. Voici les raccourcis clavier qui effaceront le cache du navigateur sur la plupart des navigateurs :

* Windows : `CTRL + F5`
* Mac/Apple : `Apple + Shift + R ou Command + Shift + R`

### 🔑 Connectez-vous

Il est possible que la page à laquelle vous essayez d'accéder nécessite une connexion. Si c'est le cas, assurez-vous de vous connecter pour obtenir un accès supplémentaire.

### 🍪 Effacer les cookies

Effacer les cookies de votre navigateur peut parfois aider. Cela est particulièrement vrai si le site nécessite généralement une connexion, et si la déconnexion et la reconnexion ne résolvent pas le problème.

### 📧 Contactez le site web

Il est possible que le site web ait été configuré incorrectement et que le créateur du site web n'en soit pas conscient. D'autres personnes pourraient obtenir cette même erreur. Essayez de trouver les informations de contact du site web et faites-leur savoir le problème. Cela pourrait être une solution simple de leur côté.

### ⏳ Revenez plus tard

Souvent, les erreurs 403 Forbidden sont causées par un problème avec le site web. Il est possible que les développeurs du site web travaillent actuellement sur une solution. Si vous essayez à nouveau plus tard, le problème pourrait être résolu.

## Pour les développeurs web uniquement

Si vous êtes le créateur de la page qui génère une erreur 403 Forbidden, alors c'est à vous de corriger l'erreur sur le serveur. Les deux raisons les plus courantes de l'erreur sont l'absence de page d'index et des permissions incorrectes.

Assurez-vous d'avoir un fichier appelé index.htm ou index.php à l'emplacement où l'erreur est affichée. Par exemple, si l'URL `https://www.freecodecamp.org/forbidden` affiche l'erreur, assurez-vous que le répertoire nommé `forbidden` sur votre serveur contient un fichier index.htm ou index.php.

La prochaine chose à vérifier est les permissions sur les fichiers qui causent l'erreur. Voici à quoi les permissions devraient généralement ressembler :

* Dossiers : 755
* Contenu statique : 644
* Contenu dynamique : 700