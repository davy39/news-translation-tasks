---
title: Comment éviter l'apparence honteuse de votre site sur Twitter et Facebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T15:39:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-the-shaming-look-your-site-has-on-twitter-and-facebook-f2e8f4be568d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*R5gAdbWi_wTP1_zSBjBtYA.jpeg
tags:
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment éviter l'apparence honteuse de votre site sur Twitter et Facebook
seo_desc: 'By Emmanuel Ohans

  If you already understand what Facebook Open Graph and Twitter Cards are, this article
  is not aimed at you. Please pass it on to someone who doesn’t understand what those
  are.

  Introduction

  According to Mashable, 52% of shared links ...'
---

Par Emmanuel Ohans

Si vous comprenez déjà ce que sont Facebook Open Graph et Twitter Cards, cet article **ne vous est pas destiné**. Veuillez le transmettre à quelqu'un qui ne comprend pas ce que sont ces technologies.

### Introduction

Selon [Mashable](https://mashable.com/2012/08/16/twitter-day-in-the-life-infographic/#Cscw4XDZ.8qM), 52 % des liens partagés sur Twitter sont des articles et des images, les images représentant environ 36 % du total. En moyenne, les gens partagent environ [30 millions d'images uniques](https://www.quora.com/How-many-photos-are-shared-on-Twitter-per-day) par jour.

![Image](https://cdn-media-1.freecodecamp.org/images/PHJm0i5jyHlBYiyDsGVXWrUHebFS93A4YDqu)
_De [Mashable](https://mashable.com/2012/08/16/twitter-day-in-the-life-infographic/#Cscw4XDZ.8qM" rel="noopener" target="_blank" title=")_

Avez-vous été surpris ?

Moi, oui.

Les tweets avec des liens vers des images obtiennent 2 fois plus d'engagement que ceux sans, selon [Buffer](https://blog.bufferapp.com/10-new-twitter-stats-twitter-statistics-to-help-you-reach-your-followers).

Maintenant, ces statistiques ne concernent que Twitter. Les statistiques combinées pour d'autres plateformes de médias sociaux populaires vous couperont le souffle.

En résumé : **les humains sont des êtres visuels.**

Si votre site est partagé sur les réseaux sociaux et qu'il ressemble à un ragoût aigre et ennuyeux, l'engagement sera faible. Partagez un lien qui apparaît de manière attrayante dans le fil d'actualité des gens, et vous êtes plus susceptible d'obtenir le type d'engagement que vous recherchez.

Ne pas prendre ces éléments en considération lors de la construction de votre site ? Vous faites définitivement quelque chose de mal.

### À quoi ressemble exactement cette apparence honteuse ?

Eh bien, tous les liens ne sont pas créés égaux. Considérez les graphiques ci-dessous. Ils représentent l'apparence de deux liens différents partagés sur Twitter. L'un provient de Medium, l'autre de l'un de mes sites web.

![Image](https://cdn-media-1.freecodecamp.org/images/hhdzeV7Bmwg9V4uBdlksG0Sg9stiOZH9lQ-7)
_Ceci est un article Medium partagé, et il a définitivement bonne apparence !_

Le graphique précédent a une grande image, un titre, une description et a généralement bonne apparence.

![Image](https://cdn-media-1.freecodecamp.org/images/IRVjqvQg6QHvYqHv0-kNWsieGr1F1u8glvjU)
_Voici un lien de mon propre site web partagé et cela n'a pas aussi bonne apparence. Triste réalité :(_

Cela n'a tout simplement pas aussi bonne apparence. Alors, que fait Medium sous le capot pour que leurs URL partagées aient si bonne apparence ?

### Passer de zéro à héros

Prenons une approche étape par étape pour transformer un site d'une "apparence honteuse" à "super génial".

Pour nos considérations, j'utiliserai l'un de mes sites, `[TheReduxJSBooks.com](https://thereduxjsbooks.com)`, comme cobaye.

Tout d'abord, pour prévisualiser comment votre aperçu de lien sera affiché sur Twitter et Facebook, les deux entreprises fournissent des débogueurs où vous collez votre lien et voyez par vous-même.

Voici le lien pour le [débogueur de partage Facebook](https://developers.facebook.com/tools/debug/sharing), et [celui-ci](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/summary-card-with-large-image) pour Twitter.

En partant de "zéro", voyons à quoi ressemble `[TheReduxJSBooks.com](https://thereduxjsbooks.com)` lorsqu'il est partagé maintenant.

Voici ce que nous avons sur Facebook :

![Image](https://cdn-media-1.freecodecamp.org/images/uSAdcRyH6rIN1flXBxobnaR1lw-MvyOj3cSz)
_L'apparence pauvre lorsqu'il est partagé sur Facebook (FB). Comme simulé sur le débogueur de partage FB, FB a réussi à afficher l'URL et le premier morceau de texte sur le site web_

Et ceci sur Twitter :

![Image](https://cdn-media-1.freecodecamp.org/images/aO2xjqU6SedgDgGQsGt3-UYVTPa42htJZWbi)
_Tellement mauvais — aucun aperçu n'est montré :( Twitter ne récupère aucune info du site. Vous devez faire le travail._

Cela n'a pas l'air impressionnant pour le moment, mais nous allons corriger cela sous peu.

Pour avoir un certain contrôle sur l'apparence de vos liens lorsqu'ils sont partagés, Facebook a développé la technologie appelée **Open Graph**. Elle devient presque une norme sur d'autres services, et **pas** seulement Facebook. Twitter appelle la leur quelque chose de différent, **Twitter Cards**.

Voyons comment cela fonctionne.

### Facebook Open Graph

![Image](https://cdn-media-1.freecodecamp.org/images/EOjVvxA10KOD-R84wr1wdyuTtA5qcb04PfgE)

En termes simples, Facebook Open Graph consiste à inclure certaines balises `meta` dans l'en-tête de votre `html`.

Ces métadonnées seront lues depuis votre site et affecteront la manière dont votre lien est prévisualisé lorsqu'il est partagé.

Maintenant, regardez les résultats finaux que nous allons obtenir lorsque le lien est partagé sur Facebook.

![Image](https://cdn-media-1.freecodecamp.org/images/AaXwdtyqYFxz1tHcNYdWewf6gil3zhWmYHE7)
_Le résultat final que nous visons._

Qu'est-ce qui est différent maintenant ?

![Image](https://cdn-media-1.freecodecamp.org/images/Nms4XIeiT4XhIKchbTrV6UUllJFaeYj0rkXY)
_Voici ce qui est différent._

Maintenant, cela a l'air magnifique. Avec une image personnalisée, un titre et une description, vous contrôlez totalement l'apparence de l'aperçu de votre lien.

Voici le code qui a produit l'aperçu que vous voyez ci-dessus :

```html
<!-- Facebook Opengraph -->
<meta property="og:url" content="https://thereduxjsbooks.com" />
<meta property="og:type" content="website" />
<meta property="og:title" content="The ReduxJS Books" />
<meta property="og:description" content="Ce que vous allez voir est un guide complet pour maîtriser Redux, de débutant à expert, avec chaque niveau de compétence pris en compte. Prêt ?"/>

<meta property="og:image" content="https://thereduxjsbooks.com/images/redux-trio-1200x630.png" />
<meta property="og:image:alt" content="3 livres sur ReduxJS. Une suite qui vous emmène de débutant à pro." />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

Je sais que cela semble être beaucoup de code, mais ce n'est pas le cas.

Ces balises sont placées dans l'en-tête de votre page `html`. Par exemple :

```html
<head>
   <!-- placez-les ici -->
</head>
```

Maintenant, passons en revue chaque balise `meta` Open Graph une par une.

Voici la première :

```html
<meta property="og:url" content="https://thereduxjsbooks.com" />
```

Ce que vous avez là est une balise `meta` avec deux attributs, `property` et `content`.

`property` définit la **propriété** de la balise meta en question. Dans ce cas, elle a la valeur `og:url`.

Comme vous l'avez peut-être deviné, `og` est l'abréviation de `Open Graph` et `url` indique que cela décrit l'`url` du lien partagé. Le `content` contient alors la valeur pour l'`url`, c'est-à-dire "[https://thereduxjsbooks.com](https://thereduxjsbooks.com)".

C'était facile.

Maintenant, c'est la même chose pour les balises `type`, `title` et `description`. Vous les voyez ?

![Image](https://cdn-media-1.freecodecamp.org/images/r0kmRJ0rTKuMBPUMdo4xh7kiM3WV72b7wrfO)
_Les balises type, title et description._

Le prochain ensemble de balises `meta` sont celles qui décrivent l'aperçu de l'image. La première a une propriété, `og:image`, et le `content` est l'URL de l'image.

```html
<meta property="og:image" content="https://thereduxjsbooks.com/images/redux-trio-1200x630.png" />
```

Une chose importante à noter est que, pour Facebook Open Graph, vous devez fournir la `width` et la `height` de l'image — de préférence `1200px par 630px`.

Les autres balises décrivent simplement le texte `alt` de l'image, le `type`, la `width` et la `height`.

![Image](https://cdn-media-1.freecodecamp.org/images/MDwxsM9YKW6ZK53Z8H2VU5QuoOHUFWN4Sep0)
_Le texte alt, le type, la largeur et la hauteur de l'image !_

Super ! Maintenant, vous connaissez les éléments les plus importants de Facebook Open Graph.

### Twitter Cards

![Image](https://cdn-media-1.freecodecamp.org/images/XyXsWyrWXVpwgvld2f7oGYcxtRnb0YjuHtEn)

Comme Facebook, vous avez également un contrôle total sur l'apparence de votre lien lorsqu'il est partagé sur Twitter.

Si vous partagez votre lien sur Twitter, en supposant que vous avez déjà configuré les balises meta Facebook Open Graph, vous obtiendrez en fait un aperçu.

Cela peut ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/otJUDGfOAsJrHTAbnwGf-P5zUmNYvucHucdO)
_Une description de base est extraite des balises meta Facebook Open Graph. Pas si mal, en fait._

Pas mal, mais pas génial non plus.

Lorsque nous aurons terminé, voici ce que nous aurons sur Twitter :

![Image](https://cdn-media-1.freecodecamp.org/images/dAtlPj86grLCtyzPqCZPTh6CTBZCv8W3MNof)
_Le meilleur résultat à viser sur Twitter._

Comme vous pouvez le voir, l'image de l'aperçu est beaucoup plus grande et la description n'est pas aussi longue. Facebook accepte plus de caractères — mais pas Twitter.

Voici donc les balises de base dont vous avez besoin.

```html
<!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:image" content="https://thereduxjsbooks.com/images/redux-trio-560x300.png" />
    <meta name="twitter:image:alt" content="3 livres sur ReduxJS. Une suite qui vous emmène de débutant à pro." />
    <meta name="twitter:description" content="Pour chaque livre que vous achetez, nous enverrons une copie gratuite à un développeur en Inde, au Nigeria et en Tunisie qui ne peut pas se permettre le coût."
    />
```

Simple !

La première balise `meta` est **super importante**.

```html
<meta name="twitter:card" content="summary_large_image" />
```

Contrairement à Facebook Open Graph avec les attributs `property` et `content`, les cartes Twitter utilisent les attributs `name` et `content`.

Ici, le nom est `twitter:card` et le contenu est `summary_large_image`. Cela décrit le type de carte Twitter que vous souhaitez. Il existe de nombreux types de cartes Twitter disponibles, mais `summary_large_image` vous donne l'aperçu de grande image que vous avez vu précédemment.

Contrairement à Facebook, vous n'avez **pas** besoin de décrire la `width` et la `height` de l'image.

Avoir simplement le nom, `twitter:image` et l'URL du `content` suffira !

```html
<meta name="twitter:image" content="https://thereduxjsbooks.com/images/redux-trio-560x300.png" />
```

Enfin, incluez simplement le texte `alt` de l'image et une description plus courte pour Twitter.

```html
<meta name="twitter:image:alt" content="3 livres sur ReduxJS. Une suite qui vous emmène de débutant à pro." />
<meta name="twitter:description" content="Pour chaque livre que vous achetez, nous enverrons une copie gratuite à un développeur en Inde, au Nigeria et en Tunisie qui ne peut pas se permettre le coût."
''  />
```

Et c'est tout !

Ce qui est encore plus beau, c'est que la configuration de cela signifie que d'autres services peuvent également rechercher ces métadonnées et afficher vos liens de manière magnifique !   
  
Voici un aperçu lorsque le lien est partagé sur Slack.

![Image](https://cdn-media-1.freecodecamp.org/images/CqxGbOlFbjJQYIVWKGblc3zE4n3oCJx6nhmX)
_Le même lien partagé sur Slack. Cela a l'air bien !_

Slack n'est qu'un des nombreux services qui respectent la technologie Facebook Open Graph et Twitter Card.

### Conclusion

J'ai omis beaucoup d'informations pour garder cet article court. Pour plus d'informations techniques, assurez-vous de consulter la documentation officielle pour [Facebook Open Graph](https://developers.facebook.com/docs/opengraph/getting-started) et [Twitter Cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards.html).

Maintenant, vous savez que ces magnifiques aperçus de liens sur Twitter et Facebook ne sont pas arrivés là par magie.

Quelqu'un a écrit le code, et maintenant vous savez comment.

Allez, construisez des sites qui ont l'air super géniaux lorsqu'ils sont partagés sur Twitter et Facebook !