---
title: Comment styliser votre page web ou markdown comme un article Medium — ou comme
  vous le souhaitez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T19:32:27.000Z'
originalURL: https://freecodecamp.org/news/style-webpage-or-markdown-like-medium-article-using-html-css-sass-bootstrap-c6f9e64c0955
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L8PQs8ubyxZVIr1EC-cZ6Q.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment styliser votre page web ou markdown comme un article Medium — ou
  comme vous le souhaitez
seo_desc: 'By ryanwhocodes

  If you love Medium’s style, then you can style your webpages or markdown files (converted
  to HTML) to give them the visual flavor of a Medium article. This tutorial will
  cover:


  Converting markdown to HTML

  Choosing custom fonts

  Stylin...'
---

Par ryanwhocodes

Si vous aimez le style de Medium, vous pouvez styliser vos pages web ou vos fichiers markdown (convertis en HTML) pour leur donner l'apparence visuelle d'un article Medium. Ce tutoriel couvrira :

* [Convertir le markdown en HTML](#conversion-markdown-html)
* [Choisir des polices personnalisées](#choix-polices-personnalisees)
* [Styliser avec CSS et Sass](#styliser-css-sass)
* [Gérer les mises en page et l'espacement](#gestion-mises-en-page)
* [Ajouter une barre de navigation et une légende utilisateur](#ajout-navbar-legende)
* [Aller plus loin](#aller-plus-loin)

Pour vous donner un aperçu de l'apparence du design avant et après l'application du style, regardez les images ci-dessous.

* Le Readme original (ci-dessous à gauche)
* Avec le style ajouté et hébergé sur Github pages (ci-dessous à droite)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NU7xgo7GBaVWeVHSieqXuA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XDN6scmU6mLMt0jTsxfxVA.png)
_Voir les pages respectives à : [https://ryandav.github.io/link-formatter/](https://github.com/ryandav/link-formatter/" rel="noopener" target="_blank" title="">https://github.com/ryandav/link-formatter/</a> et <a href="https://ryandav.github.io/link-formatter/" rel="noopener" target="_blank" title=")_

### Converting markdown to HTML

Il existe de nombreuses façons de convertir un fichier markdown, tel qu'un Readme, en HTML. Une méthode consiste à utiliser un générateur de site statique, tel que [Middleman](https://middlemanapp.com/) ou [Jekyll](https://jekyllrb.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DNJmqdEG6f_hzJ2ryp1Xrw.png)
_Commencez avec Middleman à [https://middlemanapp.com](https://middlemanapp.com/" rel="noopener" target="_blank" title=")_

[Middleman](https://middlemanapp.com/) est basé sur [Ruby](https://www.ruby-lang.org/en/) et inspiré par la conception de [Ruby on Rails](https://rubyonrails.org/). Il s'intègre avec des gems d'analyseur markdown, tels que [Redcarpet](https://github.com/vmg/redcarpet). Une fois que vous avez [démarré un site](https://middlemanapp.com/basics/install/), incluez `redcarpet` dans votre Gemfile, puis ajoutez ce qui suit au `config.rb` de votre projet :

```
set :markdown_engine, :redcarpetset :markdown,    :fenced_code_blocks => true,    :smartypants => true,    tables: true,    with_toc_data: true
```

Ensuite, assurez-vous que vos fichiers markdown sont [dans le dossier source du projet](https://middlemanapp.com/basics/directory-structure/), puis [servez](https://middlemanapp.com/basics/development-cycle/) ou [construisez](https://middlemanapp.com/basics/build-and-deploy) le site pour les rendre en HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZcyIABeCHl31RBlyAl-3w.png)
_Commencez avec Jekyll à [https://jekyllrb.com/](https://jekyllrb.com/" rel="noopener" target="_blank" title=")_

[Jekyll](https://jekyllrb.com/) a une intégration native avec [Github pages](https://pages.github.com/), et peut donc être pratique si vous voulez quelque chose d'hébergé sur Github avec un design et une configuration minimaux. Une fois que vous avez [configuré votre site](https://jekyllrb.com/docs/quickstart/), vous pouvez simplement inclure vos fichiers markdown et ils seront convertis en HTML pendant le processus de construction.

Pour en savoir plus, consultez l'article [Convertir un site HTML en Jekyll](https://jekyllrb.com/tutorials/convert-site-to-jekyll/).

Une fois que vous avez créé les fichiers HTML, examinez le code. Cela vous montrera quelles balises HTML sont utilisées dans votre page, que vous pouvez cibler pour votre stylisation.

### Choosing custom fonts

Vous pouvez trouver des polices similaires à celles de Medium sur des sites comme [Google fonts](https://fonts.google.com/). Trouvez une police sans empattement pour vos titres et une police avec empattement pour le texte du corps. Voici quelques suggestions :

* Titres : [**Open Sans**](https://fonts.google.com/specimen/Open+Sans) (gras)
* Corps : [**Lora**](https://fonts.google.com/specimen/Lora)

Le moyen le plus rapide de les ajouter est via un lien dans votre en-tête HTML ou votre fichier CSS. Cependant, héberger les polices localement signifie que vous pouvez être indépendant d'un service de téléchargement externe. Un excellent outil est le [Google Webfont Helper](https://google-webfonts-helper.herokuapp.com/fonts), qui non seulement fournit des téléchargements de polices mais aussi le CSS pour les charger dans vos feuilles de style. Maintenant, vous pouvez ajouter les polices pour les titres et les éléments de corps à votre feuille de style.

```
h1, h2, h3, h4, h5, h6 {  font-family: 'Open Sans', sans-serif;}
```

```
p, ul, li, a {    font-family: 'Lora', serif;}
```

### Styling with CSS and Sass

Le CSS vanilla est un bon choix pour les petites pages web et sites. Pour les projets plus importants, un pré-compilateur CSS, tel que [Sass](https://sass-lang.com/), signifie que vous pouvez construire votre CSS avec des fonctionnalités telles que [les partials et les variables partagées](https://sass-lang.com/guide).

![Image](https://cdn-media-1.freecodecamp.org/images/1*L--IdXLwdPI9H2pgvc_ZmA.png)
_Commencez avec Sass à [https://sass-lang.com/guide](https://sass-lang.com/guide" rel="noopener" target="_blank" title=")_

Si vous souhaitez définir toutes vos valeurs clés dans un fichier partagé entre vos autres feuilles de style, une méthode courante consiste à créer un fichier `_variables.scss`. Par exemple :

```
$primary-foreground-color: white;$body-font-size: 20px;$font-small: 14px;...
```

Ensuite, incluez les variables dans d'autres fichiers : `font-size: $body-font-size;`

Créez votre fichier Sass et ajoutez les polices et les mises en page. L'avantage de Sass est que vous pouvez les charger en utilisant [des partials](https://sass-lang.com/guide), afin que vous puissiez avoir un fichier SCSS appelé `site`, puis importer tous les partials pour les polices, les variables, les mises en page et d'autres parties de votre page web.

```
# site.css.scss
```

```
@import "fonts/lora";@import "fonts/playfair_display";@import "fonts/open_sans";
```

```
@import "variables";
```

```
@import 'layout';
```

### Manage layouts and spacing

Une façon simple de gérer les mises en page des pages est d'ajouter une marge ou un remplissage à vos éléments dans une feuille de style.

```
p {    margin: 25px;}
```

```
https://www.w3schools.com/Css/css_margin.asp
```

Alternativement, vous pouvez souhaiter écrire vos propres classes ou utiliser l'un des frameworks. Cet article couvre [Bootstrap](https://getbootstrap.com), mais les principes peuvent facilement être appliqués avec d'autres approches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S_3OIHV9vU4zzeco1346Ug.png)
_Bootstrap dispose d'une excellente documentation pour vous montrer comment utiliser ses classes de mise en page et ses composants._

**Espacement entre les en-têtes et les paragraphes :** Bootstrap dispose de quelques classes d'espacement pratiques pour ajouter facilement différentes quantités de remplissage ou de marge aux éléments.

> _Les classes sont nommées en utilisant le format `{property}{sides}-{size}` pour `xs` et `{property}{sides}-{breakpoint}-{size}` pour `sm`, `md`, `lg`, et `xl`._  
> _- [Espacement · Bootstrap](https://getbootstrap.com/docs/4.1/utilities/spacing/)_

Le système de numérotation va de 0 à 5, donc par exemple, vous pouvez ajouter une grande marge en haut d'un en-tête ou d'un paragraphe en utilisant la classe `.mt-4`, qui fait référence à **marge supérieure de taille 4**_._

```
h1, h3 {  @extend .mt-4 ;  @extend .mb-2 ;}
```

```
h5 {  @extend .my-3 ;}
```

```
p {  @extend .mb-4 ;}
```

Pour en savoir plus sur @extend et d'autres concepts Sass, consultez le [Guide Sass](https://sass-lang.com/guide).

**Définir la largeur maximale du corps du texte :** Sauf si vous voulez vraiment que le texte s'étende sur toute la largeur d'une fenêtre de navigateur, créer un `div` avec une classe qui a un style défini à une largeur maximale peut gérer cela.

```
.center-content-740px {  max-width: 740px;  margin: 0 auto;}
```

### Add a navbar and user caption

Si vous souhaitez inclure ces pages dans un site web plus grand, envisagez de styliser une page de mise en page qui inclut une [navbar](https://getbootstrap.com/docs/4.1/components/navbar/), un pied de page, et éventuellement des barres latérales et des liens vers les réseaux sociaux.

Vous pouvez ensuite inclure votre contenu de page web ou vos fichiers markdown convertis dans cette structure de mise en page pour produire un site web avec votre propre design inspiré de Medium.

Voici un [Codepen](https://codepen.io/ryanwhocodes/pen/oyNOVO) avec du HTML et du CSS que vous pouvez utiliser pour commencer avec votre propre navbar et légende utilisateur → → →

### Take it further

Voyez comment vous pouvez continuer à ajouter plus de votre propre personnalité et de votre marque au design de votre site web. Pourquoi ne pas essayer de personnaliser vos propres liens vers les réseaux sociaux, barres de navigation, choix de polices, mises en page et schémas de couleurs ? Si vous aimez la façon dont Medium présente ses menus, alors jetez un coup d'œil aux [popovers](https://getbootstrap.com/docs/4.0/components/popovers/) et aux [tooltips](https://getbootstrap.com/docs/4.0/components/tooltips/). Même si vous aimez l'idée que votre site web soit inspiré par Medium, l'objectif ultime est de le rendre unique.

#### Plus de [ryanwhocodes](https://www.freecodecamp.org/news/style-webpage-or-markdown-like-medium-article-using-html-css-sass-bootstrap-c6f9e64c0955/undefined)

* [Comment créer une application web progressive en une heure](https://medium.freecodecamp.org/how-you-can-make-a-progressive-web-app-in-an-hour-7e36d560610e)
* [Comment ajouter Bootstrap à votre projet Ruby on Rails](https://medium.freecodecamp.org/add-bootstrap-to-your-ruby-on-rails-project-8d76d70d0e3b)
* [Comment créer une extension multi-navigateurs en utilisant JavaScript et les API de navigateur](https://medium.freecodecamp.org/how-to-make-a-cross-browser-extension-using-javascript-and-browser-apis-355c001cebba)