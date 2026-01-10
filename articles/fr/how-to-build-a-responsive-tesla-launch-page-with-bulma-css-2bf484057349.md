---
title: Comment Construire Une Page de Lancement Tesla Réactive Avec Bulma CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T19:24:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-tesla-launch-page-with-bulma-css-2bf484057349
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jEoG8kpxxBob8I_6ai4WRw.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment Construire Une Page de Lancement Tesla Réactive Avec Bulma CSS
seo_desc: 'By ZAYDEK


  0-60 in 1.9s ?

  How To Build A ? Responsive Tesla Launch Page With Bulma CSS

  To accelerate the advent of sustainable web design

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some ...'
---

Par ZAYDEK

![Image](https://cdn-media-1.freecodecamp.org/images/1*nJPbo3jYDSo7JORmoMZpkQ.gif)

#### De 0 à 100 en 1,9 s ?

# Comment Construire Une Page de Lancement Tesla Réactive Avec Bulma CSS

#### Pour accélérer l'avènement du design web durable

Avant d'aborder l'article, je souhaite partager que je développe un produit et que j'aimerais collecter des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de le consulter ! Et maintenant, revenons à notre programme habituel.

### Bonjour Internet ! (Salut Elon !)

Je suis ici pour vous convaincre que construire des sites web n'a pas à être difficile. De plus, en quelques minutes, nous, simples mortels, allons apprendre à construire une belle et réactive page de lancement Tesla en utilisant Bulma.

#### Bulma ?! [Bulma](https://bulma.io/) est un framework CSS et l'œuvre de [@jgthms](https://jgthms.com/). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQHwKzcZaWbWrew33_bV4A.png)

#### J'ai également enseigné un cours complet et gratuit sur Bulma CSS sur Scrimba.com, où nous construisons ces designs ??. C[liquez ici pour vous inscrire gratuitement !](https://scrimba.com/g/gbulma) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MkSQUnosnWEuIIvoiUxadA.png)

#### [Scrimba.com](https://scrimba.com/g/gbulma) est une plateforme de nouvelle génération pour les développeurs front-end afin d'enregistrer et de partager leurs sites web sous forme de screencasts interactifs ! ?

### Bulma ? \_()_/

Bulma résout beaucoup de problèmes — beaucoup. Que vous ayez besoin d'un composant visuel ou que vous souhaitiez comprendre [comment un composant pourrait être codifié](https://github.com/jgthms/bulma/tree/master/sass), avec les meilleures pratiques et [la meilleure documentation de sa catégorie](https://bulma.io/documentation/), Bulma est là pour aider ! ??

Bulma n'est même pas en version 1.0 et connaît une adoption majeure avec [150K+ téléchargements](https://github.com/jgthms/bulma/) par mois et [26K+ étoiles](https://github.com/jgthms/bulma) sur GitHub. Considérez Bulma comme un concurrent de Bootstrap, malgré le fait qu'il ne soit *que* du CSS. ? Regarde maman, pas de Y[avaScript !](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript)

### Comment fonctionne Bulma ?

Bulma utilise plusieurs techniques pour créer une interface cohérente pour les développeurs. Nous devons simplement nous soucier de décrire le design de notre site web en utilisant des classes sémantiques — pas des éléments — ou en d'autres termes, [des modèles idiomatiques](https://bulma.io/documentation/overview/start).

Ces modèles sémantiques peuvent être considérés comme des blocs de construction interconnectés que nous utilisons pour construire des sites web rapidement !  Ces composants sont également réactifs dès la sortie de la boîte, ce qui signifie que nous pouvons nous concentrer davantage sur notre contenu que sur le code.

#### Confus ? Commencez ? i[ci](https://medium.freecodecamp.org/free-course-level-up-with-bulma-css-d82dcb4b980a) pour apprendre d'abord les bases de Bulma.

### Et ce design ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MdW2WFa4Wi_rx_KLwcnLew.gif)
_Voulez-vous apprendre à construire ce graphique 3D en HTML et CSS ? ? L[aissez-moi savoir ! ](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")?_

Ce design peut être mieux compris comme étant composé de **trois parties** :

**Arrière-plan réactif**  
 **Composants Bulma + modificateurs**  
? **CSS Grid**

Regardez un peu plus près… voyez quelque chose ? L'**arrière-plan** n'est pas continu ! ? Ce n'est pas une erreur ; l'équipe Tesla a optimisé pour le bureau, la tablette et le mobile. Avec cela comme base, nous ajouterons des **composants Bulma et des modificateurs**, puis utiliserons **CSS Grid** pour obtenir le design réactif complexe pour les spécifications.

###  Arrière-plan réactif

Ce sont les **vraies** images d'arrière-plan que j'ai ??????? de tesla.c[om ! ?](https://www.tesla.com/roadster) Alors… comment construire un arrière-plan réactif ? En utilisant des requêtes média, évidemment ! Les requêtes média nous permettent, dans certaines circonstances, de remplacer le CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JzP04PS4J9ezcbeH0hlMqQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*OddPEy3sFCb-9PYQ5Y_zNQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*hPBa5yyxaI9K4ROCdJHNcg.jpeg)

Et les requêtes média sont puissantes ; nous pouvons remplacer le CSS en fonction du ratio d'aspect rendu du site web, du ratio d'aspect de l'appareil, ou simplement et clairement : la largeur rendue du site web. Oui — choisissons cela.

Tout d'abord, nous commençons avec l'un des composants de Bulma, `.hero`, et utilisons l'un de ses modificateurs, `is-fullheight`, pour créer une section plein écran. Ensuite, nous attribuons divers arrière-plans pour [les largeurs courantes](https://bulma.io/documentation/overview/responsiveness/) en utilisant des requêtes média :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TOI29Yr3PqCc_GBkOJnVNA.png)
_1337 hax ??_

Super — donc maintenant notre site web échange les arrière-plans à `1024px` et `768px`. Parfois, lorsque cela se produit, il y a un flash blanc, donc `black` le dissimule. Et `center` et `cover` aident simplement à aligner et à focaliser l'image.

Croyez-le ou non, `background` est [un raccourci pour 8 propriétés CSS](https://developer.mozilla.org/en/docs/Web/CSS/background) : ?

1. `background-clip`  
2. `background-color`  
3. `background-image`  
4. `background-origin`  
5. `background-position`  
6. `background-repeat`  
7. `background-size`  
8. `background-attachment`

Nous avons utilisé `-color`, `-image`, `-position`, et `-size` !

### ** Composants Bulma + modificateurs**

C'est là que Bulma devient intéressant. **Lequel est la vraie page de lancement ?!**

![Image](https://cdn-media-1.freecodecamp.org/images/1*JV4-eSj3Lqbwx-NijKOBsQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ctTD3MVhZA0i-ErZqbFMnA.png)
_Choisissez-en un ; la pilule rouge ou la pilule bleue ? ?_

…

…

…

**Celui de gauche est [authentique](https://www.tesla.com/roadster) !** (;) Attendez… comment Bulma peut-il être si polyvalent ? Eh bien — souvenez-vous des modificateurs ? Oui, donc, avec suffisamment de modificateurs à notre disposition, nous pouvons créer une esthétique variée, même sans éditer la source de Bulma.

Maintenant, sans plus attendre, je présente la page de lancement sous forme d'art ASCII ! ??

![Image](https://cdn-media-1.freecodecamp.org/images/1*UTyZczNl2EoU6a9JjjAQ4w.png)
_Et si nous pouvions écrire du code comme ceci… ?_

Vous pouvez ignorer les ID entre parenthèses pour l'instant. À part cela, ce sont quelques-uns des [composants Bulma](https://bulma.io/documentation/) disponibles. Et imaginez ceci, ? les composants de Bulma sont également réactifs ! Whoa.

Gardez à l'esprit que ceci est bien moins concis que l'implémentation réelle, [voir ici](https://scrimba.com/p/pV5eHk/c3E6PCb). J'obscurcis les modificateurs et le HTML superflu pour montrer comment Bulma fonctionne ; nous relions les composants ensemble, tout comme des LEGO, mais pour concevoir une page web !

Et les modificateurs sont ce qui nous permet d'obtenir une esthétique de type Tesla, malgré le fait que Bulma n'ait rien à voir avec Tesla. Tout au long [du code](https://scrimba.com/p/pV5eHk/c3E6PCb), remarquez l'utilisation *extensive* de `has-*` et `is-*` ; c'est ce qui nous donne une esthétique variée.

#### Vous pouvez cliquer ? i[ci](https://bulma.io/documentation/) pour en savoir plus sur les composants de Bulma.

### **? CSS Grid**

Avons-nous besoin de CSS Grid ? Je ne suis pas sûr, >< mais j'ai trouvé que la programmation du design réactif pour les spécifications était beaucoup plus facile que je ne l'avais anticipé en utilisant grid plutôt qu'une autre technique. Donc, voici où ces ID entrent en jeu :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6pNXOd66bj55SZJX34FkBg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fvpX6HYKnTYpuICtSixYvA.png)

Hehehe… donc nous avons les ID `#a` à `#e`, avec `#a` étant un peu de marketing, et `#e` étant le bouton « Réserver Maintenant ». L'effet souhaité est que sur mobile, nous glissons le bouton « Réserver Maintenant » sous `#b`, `#c`, et `#d`.

3…

2…

1… ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*7h9GZsbCFrA8yEQR1xrdbg.png)
_Hein ? ? Je m'attendais à quelque chose de *plus difficile*_

Dans la première diapositive, nous attribuons des identifiants à chacun des ID en utilisant `grid-area`. Ensuite, nous communiquons à `#grid` la *forme* de notre grille en utilisant de l'art ASCII ! ? C'est la grille par défaut ; pour le bureau et la tablette.

Enfin — vous vous souvenez des requêtes média ? YAS ! Tout ce que nous avons à faire est de communiquer la forme de notre grille pour le mobile. Imaginez ceci… nous écrivons une seule requête média pour remplacer la forme de notre grille pour le mobile. ?

#### Le code interactif complet est disponible dans le cours Bulma ? i[ci.](https://scrimba.com/g/gbulma)

### Ou… ET SI ON PARLAIT DE PORSCHE ?!! ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*GY_GtCVBE0wQ0wShYBBVHA.png)
_Voulez-vous apprendre à construire ce graphique 3D en HTML et CSS ? ? L[aissez-moi savoir ! ](http://bit.do/subscribe-d82dcb4b980a" rel="noopener" target="_blank" title=")?_

Nikita Rudenko [@rdnkta](http://twitter.com/rdnkta), qui est nouveau dans #100DaysOfCode(!), a créé ceci après avoir terminé le cours, et l'a partagé avec moi ! Santé ! ?

### Félicitations ! Merci d'avoir lu ! 6(^^)9

Maintenant est un moment phénoménal comme aucun autre pour se lancer dans le développement front-end. Avec l'introduction des spécifications CSS comme [Flexbox](https://en.wikipedia.org/wiki/CSS_flex-box_layout) et [CSS Grid](https://en.wikipedia.org/wiki/CSS_grid_layout), et des frameworks comme [Bulma](https://bulma.io/), construire pour le web n'a jamais été aussi accessible !

#### Vous aimez cet article ?! Il y a un autre article tout comme celui-ci ! Cliquez ? i[ci !](https://medium.freecodecamp.org/how-to-build-a-responsive-blog-design-with-bulma-css-c2257a17c16b)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zQKHJaZS8s5iXvBBYP3FOg.png)