---
title: Améliorez WebStorm avec ces personnalisations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-03T17:28:08.000Z'
originalURL: https://freecodecamp.org/news/make-webstorm-better-with-these-customizations-c038c9e5f84b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oCrv_hHYKEzkVxS0zaVwwg.png
tags:
- name: how-to
  slug: how-to
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Améliorez WebStorm avec ces personnalisations
seo_desc: 'By Victor Savkin

  In this blog post I will show how to make WebStorm look awesome, make it faster,
  and improve the dev ergonomics.

  Make WebStorm Look Awesome

  If you are asking yourself why is my WebStorm UI looks so much cooler than the default
  UI, th...'
---

Par Victor Savkin

Dans cet article de blog, je vais montrer comment rendre WebStorm plus beau, plus rapide et améliorer l'ergonomie du développement.

#### Rendre WebStorm plus beau

Si vous vous demandez pourquoi mon interface utilisateur WebStorm est bien plus cool que l'interface par défaut, la réponse est que je l'ai personnalisée.

Pour obtenir le même look, faites ce qui suit :

* Masquez la barre d'outils et les boutons d'outils. WebStorm est un environnement adapté aux claviers, donc il n'y a absolument aucune raison d'avoir des boutons qui prennent de l'espace précieux.
* [Installez le plugin Material UI theme.](https://github.com/ChrisRM/material-theme-jetbrains) Il est magnifique.
* Ne vous contentez pas de la police par défaut. Utilisez celle que vous aimez vraiment. (par exemple, j'utilise [Operator Mono](http://www.typography.com/fonts/operator/styles/) ).

#### Rendre WebStorm plus rapide

Mon WebStorm ne se contente pas d'être plus beau, **il est aussi plus rapide**. Si vous ressentez le besoin de vitesse, faites ce qui suit :

Ouvrez :

```
/Applications/WebStorm.app/Contents/bin
```

Ouvrez le fichier de configuration idea.properties, et activez [le mode expérimental zéro latence](https://blog.jetbrains.com/idea/2015/08/experimental-zero-latency-typing-in-intellij-idea-15-eap/) en ajoutant la ligne suivante :

```
editor.zero.latency.typing=true
```

Si vous avez déjà trouvé que WebStorm était lent par rapport aux éditeurs de texte, le mode zéro latence corrigera cela.

Ensuite, ouvrez webstorm.vmoptions. Augmentez la taille maximale du tas à au moins 3 gigaoctets. Nos machines de développement ont tellement de mémoire — autant l'utiliser !

#### Arme secrète : AceJump

![Image](https://cdn-media-1.freecodecamp.org/images/21TrsXyKsi9uLC4w8vSiMOkguI6IeYlLyxxq)

Enfin, faites-vous une faveur et installez le plugin Ace Jump. Avec lui, vous pouvez déplacer votre curseur n'importe où sur l'écran avec seulement deux frappes. Donc, plus besoin de faire "bas bas bas bas bas droite droite droite droite". Pour le voir en action, [regardez cette vidéo de](https://www.youtube.com/watch?v=yK8eM50DsAY) John Lindquist.

[Suivez @victorsavkin](https://twitter.com/victorsavkin) pour en savoir plus sur le développement Web.

*Si vous avez aimé cela, cliquez sur le ? ci-dessous pour que d'autres personnes puissent le voir ici sur Medium.*