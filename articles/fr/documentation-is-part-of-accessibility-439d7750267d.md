---
title: Pourquoi la documentation logicielle fait partie de l'accessibilité [avec exemples]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-06T11:54:13.000Z'
originalURL: https://freecodecamp.org/news/documentation-is-part-of-accessibility-439d7750267d
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb37d740569d1a4cac934.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technical writing
  slug: technical-writing
- name: Web Development
  slug: web-development
seo_title: Pourquoi la documentation logicielle fait partie de l'accessibilité [avec
  exemples]
seo_desc: 'By Anna Monus

  Accessibility is mostly discussed as a way to enable people with disabilities to
  use a tool (website, application, etc.) with as little information loss as possible.
  However, the accessibility needs of users who don’t have any disabilit...'
---

Par Anna Monus

L'accessibilité est principalement discutée comme un moyen de permettre aux personnes handicapées d'utiliser un outil (site web, application, etc.) avec aussi peu de perte d'information que possible. Cependant, les besoins d'accessibilité des utilisateurs qui n'ont pas de handicaps mais qui rencontrent d'autres types de difficultés sont moins largement discutés.

Le manque de connaissances sur un sujet donné est une telle difficulté, donc fournir une documentation technique de qualité aux utilisateurs est une partie essentielle de l'accessibilité. Dans le cas des outils open-source, c'est probablement encore plus important, car ici, les utilisateurs ne veulent pas simplement utiliser l'outil mais beaucoup d'entre eux contribueraient également au code.

Si vous avez déjà dû utiliser un logiciel mal documenté, vous savez de quoi je parle. Une documentation ennuyeuse, mal structurée et hostile à l'utilisateur peut faire abandonner les gens un outil, tout comme un processus d'achat trop compliqué peut entraîner l'abandon du panier sur les sites de commerce électronique.

### Deux types de documentation technique

Essentiellement, il existe deux types de documentation technique (Cependant, vous pourriez en trouver plus, par exemple [cet article](https://www.rhyous.com/2011/07/21/the-different-types-of-technical-documentation-for-software-and-why-each-is-important/) mentionne huit types) :

1. documentation créée pour les utilisateurs finaux
2. documentation créée pour les développeurs

### Documentation pour les utilisateurs finaux

Les entreprises tendent à se concentrer davantage sur la documentation pour les utilisateurs finaux ; vous pouvez trouver des [exemples agréables et conviviaux](http://blog.screensteps.com/10-examples-of-great-end-user-documentation) de ce type de documentation. Cependant, même les meilleures documentations pour les utilisateurs finaux tendent à manquer de fonctionnalités d'accessibilité cruciales (par exemple, un contraste de couleur suffisant, ou des sous-titres pour les vidéos d'instruction).

Par exemple, jetez un coup d'œil au [Centre d'apprentissage](https://www.salesforce.com/uk/learning-centre/) de Salesforce. Dans l'ensemble, ils ont fait un excellent travail avec la documentation. Les informations sont bien structurées et logiques, et la documentation n'utilise pas trop de jargon technique.

D'un autre côté, vous constaterez que certaines des fonctionnalités d'accessibilité nécessaires font défaut, par exemple, les liens sont distingués uniquement par la couleur au lieu de fournir un [désignateur non coloré](https://www.annalytic.com/link-accessibility-colors-not-enough.html) tel qu'un soulignement.

![Image](https://cdn-media-1.freecodecamp.org/images/kn55f8Ng19dc8tTw0PU0LBsKrOdr99L1H04A)

### Documentation pour les développeurs

Les documentations techniques créées pour les développeurs étaient dans un état médiocre pendant de nombreuses années. Elles ne manquaient pas seulement de fonctionnalités d'accessibilité mais étaient également mal structurées, utilisaient des polices illisibles et une petite hauteur de ligne, manquaient de table des matières et étaient visuellement peu attrayantes dans l'ensemble.

L'essor des tutoriels vidéo a grandement amélioré la scène des documentations pour développeurs, car à peu près à la même époque, des documentations bien conçues ont commencé à apparaître.

La première documentation pour développeurs que j'ai vraiment aimée était la [Documentation Zurb Foundation](http://foundation.zurb.com/sites/docs/). Elle s'est beaucoup améliorée depuis que je l'ai vue pour la première fois, mais même les versions antérieures étaient conçues, écrites et structurées de manière à me donner envie d'apprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/nxLE9Px7tWxRaIx-wp9XxTfdIS37cMYre9By)

Les [Tutoriels Git d'Atlassian](https://www.atlassian.com/git/tutorials/what-is-version-control) constituent un autre bon exemple de documentation pour développeurs conviviale. Ils sont tout aussi bien structurés que la Documentation Foundation mais comportent également de grandes illustrations explicatives (en SVG !) et une [feuille de triche téléchargeable](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet).

![Image](https://cdn-media-1.freecodecamp.org/images/tqHAz27roCXcLj49xp9vNTJxAJXBkWXzmAaT)

Bien que les documentations Foundation et Git Tutorials présentent les informations de manière accessible aux utilisateurs sans aucune connaissance du sujet, vous trouverez quelques problèmes d'accessibilité dans les deux, qui peuvent gêner les utilisateurs handicapés (par exemple, des problèmes de contraste de couleur).

### Deux niveaux d'accessibilité de la documentation

Essentiellement, l'accessibilité de la documentation a deux niveaux :

1. Les documents doivent être accessibles aux utilisateurs sans connaissances suffisantes de l'outil.
2. Les documents doivent être accessibles aux utilisateurs qui peuvent avoir différents handicaps.

Les deux niveaux peuvent également se croiser, car il peut y avoir des utilisateurs qui sont affectés par les deux problèmes (c'est-à-dire qui n'ont pas les connaissances suffisantes et qui ont un handicap).

Les trois exemples que j'ai mentionnés dans cet article (Salesforce, Foundation, Atlassian) gèrent très bien le premier niveau d'accessibilité de la documentation, car ils :

* n'utilisent pas de jargon technique, ou s'ils le font, ils donnent l'explication nécessaire
* fournissent des menus / widgets / tables des matières pour faciliter la navigation
* structurent les pages (typographie soignée, assez d'espace blanc, rythme vertical, etc.)
* fournissent des illustrations ou des vidéos d'instruction
* fournissent des exemples d'utilisation, des démonstrations ou des extraits de code

Ils mettent également partiellement en œuvre le deuxième niveau d'accessibilité, cependant, vous trouverez ici et là des problèmes avec des choses telles que le contraste des couleurs, la visibilité des liens, le sous-titrage des vidéos, etc.

### La documentation peut-elle être parfaitement accessible ?

Je ne sais pas si des documentations parfaitement accessibles existent ou non, mais si elles existent, elles doivent mettre en œuvre les deux niveaux d'accessibilité de la documentation. Ce n'est certainement pas quelque chose de facile à accomplir, car il y a tant de choses auxquelles il faut prêter attention.

Cependant, l'accessibilité de la documentation reste une partie importante de l'accessibilité. D'abord, parce que les utilisateurs handicapés ne devraient pas être exclus de l'adoption de nouvelles technologies, mais aussi parce qu'elle a un impact considérable sur le nombre de personnes prêtes à faire un effort supplémentaire pour adopter un nouvel outil.

_Vous pouvez lire plus de mes articles de blog sur [annalytic.com](https://www.annalytic.com/documentation-part-of-accessibility/)._