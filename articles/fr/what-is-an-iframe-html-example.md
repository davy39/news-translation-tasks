---
title: Qu'est-ce qu'une iframe ? Exemple d'iframe HTML
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-02T04:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-iframe-html-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pine-watt-3_Xwxya43hE-unsplash.jpg
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_title: Qu'est-ce qu'une iframe ? Exemple d'iframe HTML
seo_desc: "An iframe is an HTML document embedded inside another HTML document on\
  \ a website. Think of it as a \"webpage within a web page.\" \nPerhaps you've seen\
  \ the movie Inception, which deals with dreams within dreams. Or played with one\
  \ of those Russian neste..."
---

Une iframe est un document HTML intégré à l'intérieur d'un autre document HTML sur un site web. Considérez cela comme une « page web dans une page web ». 

Peut-être avez-vous vu le film Inception, qui traite de rêves à l'intérieur de rêves. Ou joué avec l'une de ces poupées russes. C'est le même concept.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/1280px-Matryoshka_transparent.png)
_[Photo par BrokenSphere (CC BY-SA 3.0)](https://commons.wikimedia.org/w/index.php?curid=3773186)_

## Exemple de balise iframe HTML

La balise HTML iframe est utilisée pour spécifier l'URL du document à intégrer.

Les iframes sont souvent utilisées pour intégrer des vidéos, des cartes et d'autres médias sur une page web. Vous pouvez également les utiliser pour intégrer une autre page web dans une page web. Voici quelques exemples de code utilisant `iframe` pour intégrer une ressource externe :

```html
<iframe src="http://www.example.com/">

<iframe src="http://www.example.com/" width="400" height="300">

<iframe src="http://www.example.com/" style="border: 0;">

```

Voici quelques exemples d'intégration de ressources interactives en HTML. Ce code particulier intégrera un lecteur vidéo Vimeo :

```html
<iframe src="https://player.vimeo.com/video/76979872" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
```

Les iframes existent depuis les débuts du web. Les développeurs les utilisaient à l'origine pour intégrer du contenu externe sur une page web, comme une vidéo de YouTube.

Il existe également des sites web de type « barre d'outils » comme Stumbleupon qui ajoutaient leur barre d'outils au-dessus d'un site web. Stumbleupon faisait cela en affichant le site web sur sa propre page à l'aide d'une iframe.

## Pourquoi les développeurs ont majoritairement cessé d'utiliser les iframes dans leurs sites web

De nos jours, les développeurs utilisent toujours les iframes pour intégrer des médias et d'autres contenus sur une page web. Mais en raison de considérations de sécurité, de nombreux Framework de développement web le déconseillent.

En fin de compte, une iframe s'exécutant à l'intérieur d'une autre page web ne constitue pas une expérience utilisateur idéale. Les iframes peuvent paraître particulièrement mauvaises sur les téléphones mobiles et briser les mises en page de conception web responsive. C'est pourquoi les iframes sont largement tombées en disgrâce.

J'espère que cela vous a été utile. Si vous voulez en savoir plus sur la programmation et la technologie, essayez le [programme de codage principal de freeCodeCamp](https://www.freecodecamp.org/learn). C'est gratuit.