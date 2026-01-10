---
title: Une brève histoire du Responsive Web Design
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-02-04T09:44:00.000Z'
originalURL: https://freecodecamp.org/news/a-brief-history-of-responsive-web-design
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6034711fa675540a22921aad.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Une brève histoire du Responsive Web Design
seo_desc: 'These days, responsive web design is something we all take for granted.
  When we visit a website, we expect it to work and look good on all our devices,
  no matter what the screen size is.

  But it took us a long time to get to this point, and developers...'
---

De nos jours, le responsive web design est quelque chose que nous tenons tous pour acquis. Lorsque nous visitons un site web, nous nous attendons à ce qu'il fonctionne et qu'il soit esthétique sur tous nos appareils, peu importe la taille de l'écran.

Mais il nous a fallu beaucoup de temps pour en arriver là, et les développeurs ont imaginé un certain nombre de techniques pour adapter les sites à différentes tailles d'écran avant de se fixer sur le responsive web design.

Dans cet article, nous allons examiner le web des débuts, les différentes méthodes utilisées par les développeurs pour adapter un site à différentes tailles d'écran, et le design responsive moderne.

## Le premier site web

Le 6 août 1991, le premier site web de l'histoire est mis en ligne. Le site a été créé par Tim Berners-Lee et détaillait le projet World Wide Web (W3). Il fonctionnait à l'origine sur un ordinateur NeXT au CERN, l'Organisation européenne pour la recherche nucléaire.

Bien que le site original soit hors ligne, le CERN a lancé un projet en 2013 pour "préserver certains des actifs numériques associés à la naissance du web". Tout, des noms des machines originales, des adresses IP et de l'URL du premier site web, a été restauré au mieux de leurs capacités.

Bien que la version originale de 1991 du site web ait été perdue, ils ont pu restaurer une version de 1992. Si vous souhaitez la consulter, elle est désormais disponible à l'adresse [http://info.cern.ch/hypertext/WWW/TheProject.html](http://info.cern.ch/hypertext/WWW/TheProject.html).

## Le design web des débuts

Le web a rapidement changé depuis la mise en ligne du premier site web de Berners-Lee. Chaque année, des milliers de sites web ont été lancés, et de nouvelles techniques de design se sont développées aussi rapidement que la technologie web elle-même.

Dans les années 90, le design web était très simple. La plupart des sites web utilisaient des balises simples comme les en-têtes, les paragraphes et les premières balises de liste comme `<dl>`, `<dt>` et `<dd>` pour organiser l'information.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/yahoo-1994.png)
_Yahoo en 1994 ([Source](https://www.webdesignmuseum.org/web-design-history/yahoo-1994))_

Les sites plus complexes devaient utiliser des tableaux pour contrôler la mise en page et créer des éléments comme la navigation et les barres latérales, courants aujourd'hui.

Bien que des méthodes de stylisation des sites web existaient sous une forme ou une autre, Håkon Wium Lie a proposé pour la première fois le CSS en 1994 alors qu'il travaillait au CERN. Ensuite, en 1996, le World Wide Web Consortium (W3C), également fondé par Berners-Lee, a publié la première spécification formelle pour les Cascading Style Sheets, niveau 1 (CSS1).

Avec le CSS et d'autres technologies comme JavaScript et Flash, les développeurs web pouvaient être plus créatifs et ludiques dans leurs designs.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/internet-archive-1997.png)
_Internet Archive en 1997 ([Source](https://www.webdesignmuseum.org/web-design-history/internet-archive-1996))_

À la fin des années 90 et au début des années 2000, des modèles de design web et d'expérience utilisateur ont émergé, et les sites web ont commencé à ressembler à ceux que nous utilisons aujourd'hui :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/deviant-art-2000.png)
_DeviantArt en 2000 ([Source](https://www.webdesignmuseum.org/web-design-history/deviantart-2000))_

## Les premières méthodes de design responsive

Avec l'adoption plus large du CSS, les développeurs devaient passer beaucoup plus de temps sur des choses comme la mise en page, le design et la typographie. Mais une chose à laquelle ils n'avaient pas à trop penser était l'adaptation à différentes tailles d'écran. À l'époque, la plupart des moniteurs des gens étaient soit 640x480, 800x600, ou 1024×768.

Néanmoins, les développeurs ont trouvé plusieurs façons différentes de travailler avec ces tailles de moniteur ou de fenêtre de navigateur, ce qui a finalement conduit au responsive web design tel que nous le connaissons aujourd'hui. Examinons quelques-unes de ces méthodes.

### Les mises en page fluides

Selon [MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design), les deux principales options de mise en page dont disposaient les développeurs au début étaient soit la largeur fixe, où le contenu était défini à une largeur exacte, pixel par pixel, soit la mise en page fluide, où le contenu était dimensionné en utilisant des pourcentages.

MDN propose quelques bons exemples de mises en page à [largeur fixe](https://mdn.github.io/css-examples/learn/rwd/fixed-width.html) et [fluide](https://mdn.github.io/css-examples/learn/rwd/liquid-width.html).

Les mises en page fluides, d'abord inventées et popularisées par Glenn Davis, étaient révolutionnaires à l'époque et peuvent être considérées comme l'une des premières méthodes majeures de responsive web design.

Alors que les mises en page à largeur fixe pouvaient se casser si votre moniteur n'avait pas la même résolution que celle pour laquelle le site avait été conçu, les mises en page fluides étaient beaucoup plus flexibles et pouvaient s'adapter à différentes résolutions de moniteur ou tailles de navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/elastic.gif)
_Un exemple de design fluide ([Source](https://thehistoryoftheweb.com/mostly-complete-history-layout-web-part-1-liquid-cool/))_

Mais ce n'était pas parfait. Sur les sites avec des mises en page fluides, le contenu pouvait déborder et le texte pouvait se casser sur les petits écrans, et sur les grands écrans, il pouvait y avoir beaucoup d'espace blanc inutile.

### Les mises en page dépendantes de la résolution

En 2004, Cameron Adams a écrit un [article de blog](https://www.themaninblue.com/writing/perspective/2004/09/21/) dans lequel il détaillait une méthode utilisant JavaScript pour échanger différentes feuilles de style en fonction de la taille de la fenêtre du navigateur.

Cette technique est devenue connue sous le nom de mises en page dépendantes de la résolution, nommée d'après l'article de blog d'Adams. Même si cela représentait un peu de travail supplémentaire pour les développeurs à l'époque, cela permettait un contrôle plus fin sur la mise en page du site et fonctionnait comme une version précoce des points de rupture CSS avant que ceux-ci n'existent.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-117.png)
_L'exemple d'Adams d'une mise en page dépendante de la résolution ([Source](https://www.themaninblue.com/experiment/ResolutionLayout/))_

L'inconvénient de cette méthode était que les développeurs devaient créer différentes feuilles de style pour chaque résolution cible et s'assurer que le style et JavaScript fonctionnaient sur tous les principaux navigateurs.

Il y avait beaucoup de navigateurs à l'époque, et parfois ils géraient le HTML, le CSS et JavaScript différemment. En fait, c'est l'une des principales raisons pour lesquelles jQuery est devenu si populaire à l'époque - il abstraait beaucoup des différences entre les navigateurs afin que vous n'ayez à écrire votre code qu'une seule fois.

### Les sous-domaines mobiles

Tout cela se passait juste au moment où de plus en plus d'appareils mobiles se connectaient à Internet. Nokia, Blackberry, et finalement, l'iPhone, sont arrivés avec leurs propres navigateurs. Et soudain, les développeurs ont dû trouver différentes façons d'adapter l'expérience en ligne à différentes tailles d'écran.

Une façon ingénieuse que les développeurs ont trouvée pour gérer tous ces nouveaux appareils était de créer une version d'un site spécialement pour les mobiles et de la rendre disponible sur un sous-domaine.

Les sous-domaines mobiles, parfois appelés m-dots ou sous-domaines m, sont exactement cela - une version spécifique pour mobile d'un site qui est hébergée sur un sous-domaine, généralement `m`.

Par exemple, la version desktop de Facebook est à `facebook.com`, ou plus précisément, sur le sous-domaine `www`, `www.facebook.com` :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-119.png)
_La version desktop de Facebook_

Mais la version mobile de Facebook est à `m.facebook.com` :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-118.png)
_La version mobile de Facebook_

Si vous vous connectez aux deux applications et que vous les regardez côte à côte, elles se ressemblent beaucoup. Mais sous le capot, ce sont vraiment deux applications distinctes - la version mobile est beaucoup plus légère et est optimisée pour fonctionner sur des écrans plus petits et sur la plupart des navigateurs mobiles.

Les sous-domaines mobiles existent encore aujourd'hui, et cette approche présente certains avantages. Avec une version séparée d'un site sur un sous-domaine mobile, les développeurs peuvent s'assurer que le site se charge rapidement et utilise moins de données mobiles.

De plus, avoir un sous-domaine mobile permet aux développeurs de vraiment adapter le SEO (optimisation pour les moteurs de recherche) aux appareils mobiles et de générer plus de trafic vers la version mobile du site.

Mais il y a aussi des inconvénients certains. Opter pour des sous-domaines mobiles signifie que les développeurs doivent maintenir deux sites web, parfois très différents, au lieu d'un seul.

Et les sous-domaines mobiles peuvent parfois être frustrants. Je suis sûr que beaucoup d'entre vous connaissent la douleur d'essayer de visiter la version desktop d'un site pour être redirigé vers la version mobile.

Non seulement cela, mais les développeurs doivent déterminer quels appareils rediriger et dans quelles conditions.

Traditionnellement, cela se faisait en vérifiant l'agent utilisateur du navigateur du visiteur, mais avec le nombre d'appareils sortant à l'époque, c'était une cible mouvante constante. Finalement, les développeurs ont commencé à vérifier la largeur de la fenêtre du navigateur avec JavaScript et à rediriger en fonction de cela.

Maintenant, vous pourriez penser que cela ressemble beaucoup au responsive web design d'aujourd'hui. Et c'est vrai - à bien des égards, le responsive web design moderne est une réponse, eh bien, une réponse, aux techniques passées. Il reprend beaucoup des bonnes idées que les développeurs ont eues et construit dessus.

## Le responsive web design

À la fin des années 2000, concevoir un site pour qu'il fonctionne sur différentes tailles d'écran devenait rapidement la norme. Mais pour cela, les développeurs devaient trouver beaucoup d'astuces.

Même pour des mises en page simples, les développeurs devaient utiliser des astuces comme le `max-width: 100%` pour les images flexibles, et `float` avec des [clearfixes](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Floats#the_clearfix_hack) pour éviter que les choses ne se cassent.

Puis en 2010, un développeur nommé Ethan Marcotte a publié un article dans [A List Apart](https://alistapart.com/) où il décrivait une nouvelle façon de penser le design web flexible. Dans l'article, Marcotte listait trois composants importants pour créer un site web responsive : les grilles fluides, les images flexibles et les media queries.

Au-delà de la description des principaux composants du responsive web design, Marcotte est également crédité pour avoir inventé le terme lui-même, qui a été nommé d'après le titre de l'[article de 2010](https://alistapart.com/article/responsive-web-design/).

### Les grilles fluides

Les grilles fluides sont l'idée qu'un site web devrait adopter un nombre différent de colonnes flexibles qui grandissent ou rétrécissent en fonction de la taille actuelle de l'écran. Sur les appareils mobiles, il devrait y avoir une ou deux colonnes flexibles de contenu, et sur les ordinateurs de bureau, il peut y en avoir plus :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-126.png)
_Le site web d'Ethan Marcotte sur un appareil mobile ([Source](https://ethanmarcotte.com/work/))_

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-125.png)
_La même page sur un ordinateur de bureau ([Source](https://ethanmarcotte.com/work/))_

Vous pouvez lire plus de réflexions de Marcotte sur les grilles fluides dans cet [article précédent](https://alistapart.com/article/fluidgrids/).

### Les images flexibles

Les images flexibles sont l'idée que les images doivent grandir ou rétrécir avec la grille fluide dans laquelle elles se trouvent :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-127.png)
_Des photos plus petites sur un appareil mobile ([Source](https://ethanmarcotte.com/work/))_

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-128.png)
_Des photos plus grandes sur un ordinateur de bureau ([Source](https://ethanmarcotte.com/work/))_

Une méthode courante pour cela est l'astuce `max-width` mentionnée ci-dessus.

Si vous avez une image dans un conteneur, elle pourrait déborder, surtout si le conteneur est responsive. Par exemple, si vous avez ce qui suit, l'image pourrait déborder comme ceci :

```html
<style>
  .container {
    width: 250px;
    outline: solid;
    text-align: center;
  }
</style>
<body>
  <div class="container">
    <img src="./images/kelly-sikkema-v9FQR4tbIq8-unsplash.jpg" />
    <p>Exemple d'image</p>
  </div>
</body>

```

![Une image débordant de son conteneur de 250px de large.](https://www.freecodecamp.org/news/content/images/2021/02/image-129.png)

Mais si vous définissez sa `max-width` à `100%`, l'image ne débordera pas :

```html
<style>
  .container {
    width: 250px;
    outline: solid;
    text-align: center;
  }

  .my-image {
    max-width: 100%;
  }
</style>
<body>
  <div class="container">
    <img
      class="my-image"
      src="./images/kelly-sikkema-v9FQR4tbIq8-unsplash.jpg"
    />
    <p>Exemple d'image</p>
  </div>
</body>

```

![La même image contenue dans son conteneur de 250px de large.](https://www.freecodecamp.org/news/content/images/2021/02/image-130.png)

Et elle redimensionnera même avec le conteneur parent :

```html
<style>
  .container {
    width: 600px;
    outline: solid;
    text-align: center;
  }

  .my-image {
    max-width: 100%;
  }
</style>
<body>
  <div class="container">
    <img
      class="my-image"
      src="./images/kelly-sikkema-v9FQR4tbIq8-unsplash.jpg"
    />
    <p>Exemple d'image</p>
  </div>
</body>

```

![L'image redimensionnée au conteneur plus large de 600px de large.](https://www.freecodecamp.org/news/content/images/2021/02/image-131.png)

### Les media queries

Les media queries font référence aux requêtes media CSS qui étaient disponibles en 2010, mais qui n'ont pas été largement adoptées avant leur publication officielle en tant que [Recommandation W3](https://www.w3.org/TR/2012/REC-css3-mediaqueries-20120619/) en 2012.

Une media query est simplement une règle CSS qui est déclenchée en fonction d'options comme le type de média (`screen`, `print`, etc.) et les caractéristiques du média (`width`, `height`, etc.) :

```css
@media screen and (min-width: 500px) {
  background-color: red;
}
```

Bien qu'elles soient un peu plus simples à l'époque, les media queries permettaient aux développeurs d'implémenter des points de rupture, qui sont encore utilisés dans le responsive web design aujourd'hui.

Un point de rupture est simplement lorsque un site web change de mise en page ou d'autres styles en fonction de la largeur de l'appareil ou de la fenêtre du navigateur. Par exemple, voici le code complet pour l'extrait ci-dessus :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <style>
    .container {
      width: 250px;
      outline: solid;
      text-align: center;
    }

    .my-image {
      max-width: 100%;
    }

    @media screen and (max-width: 500px) {
      .container {
        background-color: red;
      }
    }
  </style>
  <body>
    <div class="container">
      <img
        class="my-image"
        src="./images/kelly-sikkema-v9FQR4tbIq8-unsplash.jpg"
      />
      <p>Exemple d'image</p>
    </div>
  </body>
</html>

```

Notez qu'il est important d'utiliser une [balise meta viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag) pour que les media queries fonctionnent comme prévu. Cela fonctionne dans la plupart des cas :

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

Avec la media query ci-dessus, voici à quoi ressemble le conteneur lorsque la résolution est de 500px de large ou moins :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-132.png)

Et voici à quoi il ressemble lorsque la résolution est de 501px ou plus :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-133.png)

### Mobile-first vs Desktop-first

Plus récemment, il existe deux approches principales pour le responsive web design : mobile-first ou desktop-first. Les deux sont des options tout à fait valables, et chacune a ses avantages et ses inconvénients.

Si vous concevez un site web à partir de zéro, de nombreux développeurs aujourd'hui pensent que le mobile-first est la voie à suivre - les designs mobiles tendent à être en une seule colonne et sont beaucoup plus faciles.

Si vous souhaitez adopter l'approche mobile-first, vous écriviez vos styles normalement, puis créez des points de rupture comme celui ci-dessus avec `min-width` une fois que vous commencez à créer les mises en page pour tablettes et ordinateurs de bureau.

Mais peut-être travaillez-vous sur un site plus ancien qui a été conçu en pensant aux ordinateurs de bureau et devez-vous l'adapter aux petits appareils mobiles. Dans ce cas, vous utiliseriez des media queries avec `max-width` pour cibler ces résolutions plus basses.

Vous pouvez en lire plus sur les philosophies de design mobile-first et desktop-first dans [cet article](https://www.freecodecamp.org/news/taking-the-right-approach-to-responsive-web-design/).

## En conclusion

C'est tout ! Maintenant, vous en savez un peu plus sur l'histoire du responsive web design et tous les tâtonnements que les développeurs ont traversés avant d'en arriver à ce que nous avons aujourd'hui.

Si vous souhaitez approfondir le responsive web design, Flexbox et d'autres techniques modernes, consultez ce tutoriel de 4 heures sur notre chaîne YouTube :

%[https://www.youtube.com/watch?v=srvUrASNj0s]

Et si vous souhaitez en savoir plus sur CSS Grid, la nouvelle façon de créer des mises en page complexes et flexibles, consultez l'un de nos tutoriels écrits [ici](https://www.freecodecamp.org/news/search/?query=css%20grid).

Quelle est votre histoire avec le responsive web design ? Ai-je oublié quelque chose ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).