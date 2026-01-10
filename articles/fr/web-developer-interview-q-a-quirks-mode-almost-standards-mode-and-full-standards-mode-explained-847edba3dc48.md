---
title: Les modes navigateur expliqués avec nostalgie et le mot le plus triste jamais
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-22T14:28:59.000Z'
originalURL: https://freecodecamp.org/news/web-developer-interview-q-a-quirks-mode-almost-standards-mode-and-full-standards-mode-explained-847edba3dc48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bZZLpdpMiwhyzRqKAc7OyQ.jpeg
tags:
- name: internet
  slug: internet
- name: interview questions
  slug: interview-questions
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les modes navigateur expliqués avec nostalgie et le mot le plus triste
  jamais
seo_desc: 'By Zuzana K

  In my last article, I discussed the doctype — what it is and why it is needed. In
  this article, I am going to look into the difference between various modes that
  browsers can run: the full standards mode, the almost standards mode, and th...'
---

Par Zuzana K

Dans mon [dernier article](https://medium.freecodecamp.org/web-developer-interview-q-a-what-does-a-doctype-do-146dd757d7d1), j'ai discuté du doctype — ce qu'il est et pourquoi il est nécessaire. Dans cet article, je vais examiner la différence entre les divers modes dans lesquels les navigateurs peuvent fonctionner : le mode pleinement conforme, le mode presque conforme et le mode quirks.

Ces deux articles sont assez liés, vous voudrez peut-être lire le précédent d'abord pour comprendre de quoi je parle.

### Question : Quelle est la différence entre le mode pleinement conforme, le mode presque conforme et le mode quirks ?

Les différents modes sont tous liés à la première implémentation des standards du [W3C](https://www.w3.org/).

Le doctype a été introduit pour indiquer aux navigateurs quel type de documents ils devaient rendre. Si le développeur oublie d'inclure le doctype dans son document HTML, le navigateur ne sait pas quel type de document il traite.

Ainsi, pour être prudent, il rendra le document pour qu'il soit compatible avec les anciens navigateurs (Navigator 4, Internet Explorer 4 et 5) dans ce qu'on appelle le mode quirks.

Et comme les anciens navigateurs vivaient dans un monde de CSS très mauvais, cela signifie qu'une grande partie de vos styles CSS ne seront pas appliqués, et votre site ne ressemblera pas à ce que vous attendez.

Bien sûr, certains développeurs peuvent choisir d'omettre le doctype intentionnellement parce qu'ils veulent que leur document soit rendu en mode quirks pour diverses raisons.

Comme, que se passerait-il si je voulais savoir à quoi ressemblerait mon site web en 1998 ?

Bonne raison, je dirais.

Maintenant que nous savons ce qu'est le mode quirks et ce qu'il fera à notre pauvre site web (le casser), quel est le problème avec les modes pleinement conforme et presque conforme ?

Le mode presque conforme est également connu sous le nom de mode quirks limité. Comme vous pouvez l'imaginer, le contenu rendu en mode presque conforme est presque entièrement conforme au mode pleinement conforme.

Presque.

Le mot le plus triste jamais.

> I. Petites histoires

> Le mot le plus triste

> dans le monde entier

> est le mot presque.

> Il était presque amoureux.

> Elle était presque bonne pour lui.

> Il a presque arrêté.

> Elle a presque attendu.

> Il a presque vécu.

> Ils ont presque réussi.

Par [Nikita Gill](https://quotecatalog.com/quote/nikita-gill-i-tiny-stories-g7O3RR7/)

N'importe, continuons.

Le mode presque conforme rend le document avec seulement quelques quirks qui concernent le dimensionnement vertical des cellules de tableau.

D'autre part, le mode pleinement conforme rend le document selon les dernières spécifications HTML et CSS. Même s'il existe encore quelques différences entre la façon dont les navigateurs modernes rendent le contenu à l'écran, nous pouvons utiliser [Normalize.css](https://necolas.github.io/normalize.css/) ou [Reset CSS](https://meyerweb.com/eric/tools/css/reset/) pour réduire les incohérences (et garder notre santé mentale).

Donc, s'il y a des quirks sur votre site web, ils sont probablement dus à vous, pas au navigateur.

Désolé.

Eh bien, nous y voilà. Si quelqu'un vous demande un jour quelle est la différence entre les modes pleinement conforme, presque conforme et quirks, souvenez-vous simplement des anciens navigateurs, du CSS cassé et du mot le plus triste jamais.

Si vous voulez lire plus sur l'activation des différents modes de navigateur, il y a un [aperçu fantastique](https://hsivonen.fi/doctype/) écrit par Henri Sivonen. Et une liste approximative des quirks peut être trouvée sur [MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Mozilla_quirks_mode_behavior).

La prochaine fois, je regarderai la différence entre HTML et XHTML. J'espère que vous me rejoindrez dans ce qui s'annonce comme un sujet assez excitant ! À bientôt !

La liste des questions auxquelles je réponds a été aimablement fournie par [Rose](http://www.verifyrecruitment.com/blog/index.php/tag/askrose/) de l'agence de recrutement [Verify](http://www.verifyrecruitment.com/) à Dublin, en Irlande.

*Si vous avez apprécié cet article et l'avez trouvé bénéfique, envisagez de me laisser un commentaire ou quelques applaudissements. Merci !*