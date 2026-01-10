---
title: Qu'est-ce que Localhost ? Explication de l'adresse IP Local Host
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-29T16:11:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-localhost
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743780742807/3c1b7eab-e5bb-4b3c-aae9-6183d2cf3f72.jpeg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Computer Science
  slug: computer-science
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que Localhost ? Explication de l'adresse IP Local Host
seo_desc: 'If you are an experienced web developer, then you’ve likely seen the term
  “localhost” on many occasions.

  And even if you’re a beginner and just getting started in web development, you might
  have seen the number “127.0.0.1:” while using a live server ...'
---

Si vous êtes un développeur web expérimenté, vous avez probablement vu le terme « localhost » à de nombreuses reprises.

Et même si vous êtes débutant et que vous commencez tout juste en développement web, vous avez peut-être vu le nombre « 127.0.0.1 » en utilisant une extension de serveur en direct.

Vous l'utilisez peut-être pour tester des sites web et des applications web localement sans savoir exactement ce que c'est. Eh bien, « 127.0.0.1 » est localhost et « localhost » est « 127.0.0.1 ».

Dans cet article, vous apprendrez ce qu'est localhost ainsi que son adresse IP correspondante, « 127.0.0.1 ».

## Qu'est-ce que Localhost ?

En informatique, un hôte signifie un « serveur ». Tout comme vous pouvez mettre un site web sur Internet en l'hébergeant sur un serveur, vous pouvez faire de votre propre ordinateur ce serveur. Cette connexion est appelée **loopback**. L'adresse IP pour ce loopback est `127.0.0.1`.

Si vous avez déjà mis un site web sur Internet, alors vous avez traité avec des sociétés d'hébergement comme Heroku, Hostinger, Netlify, et bien d'autres. Ce sont ce que j'appelle des « hôtes distants » ou des serveurs virtuels.

Si vous avez servi un site web sur votre ordinateur pour pouvoir le tester sans vous connecter à Internet, ce avec quoi vous traitez est un localhost.

Ainsi, par définition, **localhost est l'ordinateur ou le nom d'hôte qui fait actuellement une requête à lui-même**. Dans ce cas, l'ordinateur est également le serveur virtuel.

## Qu'est-ce que l'adresse IP `127.0.0.1` ?

Si vous voulez visiter un site web, vous tapez l'adresse du site dans la barre d'adresse de votre navigateur, par exemple, `https://freecodecamp.org`.

Le serveur de noms de domaine (DNS) fait correspondre l'adresse à une adresse IP numérique correspondant à ce nom. Dans le cas de freeCodeCamp, cette adresse IP est `104.26.2.33`. C'est ainsi que cela se fait pour chaque site web que vous visitez.

Localhost n'est pas une exception à cela. Donc, si vous tapez `localhost` dans la barre d'adresse de votre navigateur, il se transforme en l'adresse IP `127.0.0.1`.

Cette adresse IP `127.0.0.1` est réservée pour les serveurs locaux sur les ordinateurs, donc vous ne trouverez jamais une autre adresse IP qui commence par 127.

### Mais localhost : quoi ? Ou 127.0.0.1 : quoi ?

Contrairement à `HTTP` et `HTTPS` qui sont des protocoles, `localhost` est un nom d'hôte. Rappelez-vous que le nom de domaine du site web est ce qui suit http ou https, par exemple, `https://www.google.com/` et `https://www.freecodecamp.org/`. Donc, quelque chose doit suivre `localhost:` et `127.0.0.1:`. Cette chose est le numéro de port.

Par exemple, dans une application Express, ce numéro de port est la variable de port que vous définissez. Quelque chose comme ceci :

```js
const port = 4000;
```

Donc, si vous tapez `localhost:4000` dans la barre d'adresse du navigateur et appuyez sur `ENTRÉE`, l'application web que vous êtes en train de créer sera servie :

![ss1-5](https://www.freecodecamp.org/news/content/images/2022/06/ss1-5.png align="left")

De plus, si vous tapez `127.0.0.1:4000`, vous obtiendrez la même réponse :

![ss2-5](https://www.freecodecamp.org/news/content/images/2022/06/ss2-5.png align="left")

Si vous utilisez l'extension de serveur en direct de VS Code, elle utilise un port `5500` attaché à `127.0.0.1`, suivi du nom de fichier :

![ss3-6](https://www.freecodecamp.org/news/content/images/2022/06/ss3-6.png align="left")

## Conclusion

J'espère que cet article vous a aidé à en apprendre davantage sur localhost, ce qu'est son adresse IP et comment il fonctionne pour servir des sites web pour des tests locaux.

Et oui ! Il n'y a pas de place comme localhost. Pour le dire correctement, « il n'y a pas de place comme `127.0.0.1` » :).

Continuez à coder...

Merci à [Bartosz Cytrowski](https://www.cytrowski.com/) pour avoir signalé une erreur clé concernant ce qu'est localhost. Vos commentaires ont amélioré l'article !