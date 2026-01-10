---
title: Réduire la taille du bundle CSS de 70 % en raccourcissant les noms de classe
  et en utilisant l'isolement de portée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-12T22:50:35.000Z'
originalURL: https://freecodecamp.org/news/reducing-css-bundle-size-70-by-cutting-the-class-names-and-using-scope-isolation-625440de600b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mGuDYFM56iyLi1MgZPC8bw.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: SEO
  slug: seo
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Réduire la taille du bundle CSS de 70 % en raccourcissant les noms de classe
  et en utilisant l'isolement de portée
seo_desc: 'By Gajus Kuizinas

  Just like Google does it

  At the beginning of this year I have quit consulting and set out to build GO2CINEMA
  — Fast, simple and secure way to book cinema tickets in the UK. I have done a splendid
  job making it fast, simple and secur...'
---

Par Gajus Kuizinas

#### Comme le fait Google

Au début de cette année, j'ai quitté le conseil et je me suis lancé dans la construction de [GO2CINEMA](https://go2cinema.com/) — Un moyen rapide, simple et sécurisé de réserver des billets de cinéma au Royaume-Uni. J'ai fait un travail splendide pour le rendre _rapide, simple et sécurisé_. En cours de route, je me suis obsédé par l'optimisation du chemin de rendu critique ⚡.

J'ai résolu le pré-rendu du HTML en utilisant [ŭsus](https://github.com/gajus/usus). ŭsus rend le HTML des applications monopages (SPA) et [intègre le CSS utilisé pour rendre la page](https://medium.com/@gajus/pre-rendering-spa-for-seo-and-improved-perceived-page-loading-speed-47075aa16d24). Cependant, je n'aimais pas intégrer 70 Ko dans chaque document HTML, surtout si la plupart étaient des noms de classes CSS.

#### Comme le fait Google

Avez-vous déjà jeté un coup d'œil au code source de [https://www.google.com/](https://www.google.com/)? La première chose que vous remarquerez est que les noms des classes CSS ne font pas plus de quelques caractères.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGuDYFM56iyLi1MgZPC8bw.png)
_HTML de google.com_

Mais comment?

#### Les limites des minifieurs CSS

Il y a une chose qu'un minifieur ne peut pas faire – changer les noms des sélecteurs. Cela est dû au fait qu'un minifieur CSS ne contrôle pas la sortie HTML. Pendant ce temps, les noms CSS peuvent devenir longs.

Si vous utilisez des modules CSS, vos modules CSS incluront probablement le nom du fichier de feuille de style, le nom de l'identifiant local et un hash aléatoire. Le modèle de nom de classe est décrit en utilisant la configuration [css-loader `localIdentName`](https://github.com/webpack-contrib/css-loader), par exemple `[name]___[local]___[hash:base64:5]`. Par conséquent, un nom de classe généré ressemblera à quelque chose comme `.MovieView___movie-title___yvKVV`; si vous aimez les noms descriptifs, cela peut devenir beaucoup plus long, par exemple `.MovieView___movie-description-with-summary-paragraph___yvKVV`.

#### Renommer les noms de classe CSS au moment de la compilation

Cependant, si vous utilisez [webpack](https://webpack.js.org/) et [babel-plugin-react-css-modules](https://github.com/gajus/babel-plugin-react-css-modules), vous avez de la chance ? – vous pouvez renommer les noms de classe au moment de la compilation en utilisant la configuration c[ss-loader g`etLocalIdent`](https://github.com/webpack-contrib/css-loader) et la configuration équivalente babel-plugin-react-css-modules g`[enerateScopedName](https://github.com/gajus/babel-plugin-react-css-modules#configuration)`.

Le truc cool avec `generateScopedName` est que la même instance de la fonction peut être utilisée pour le processus de construction Babel et webpack:

#### Rendre les noms courts

Grâce à `babel-plugin-react-css-modules` et `css-loader` partageant la même logique pour générer les noms de classe CSS, nous pouvons changer les noms de classe en ce que nous voulons, même un hash aléatoire. Cependant, au lieu d'un hash aléatoire, je voulais les noms de classe les plus courts possibles.

Pour générer les noms de classe les plus courts, j'ai créé un index de noms de classe et utilisé le module `[incstr](https://github.com/grabantot/incstr)` pour générer des IDs incrémentiels pour chaque entrée dans l'index.

Cela garantit des noms de classe courts et uniques. Maintenant, au lieu de `.MovieView___movie-title___yvKVV` et `.MovieView___movie-description-with-summary-paragraph___yvKVV`, nos noms de classe sont devenus `.a_a`, `.b_a`, etc.

Cela a réduit la taille du bundle CSS de [GO2CINEMA](https://go2cinema.com/) de 140 Ko à 53 Ko.

#### Utiliser l'isolement de portée pour réduire davantage la taille du bundle

Il y a une bonne raison pour laquelle j'ai ajouté `_` dans le nom de la classe CSS séparant le nom du composant et le nom de l'identifiant local – la distinction est utile pour la minification.

[csso](https://github.com/css/csso) (minifieur CSS) a une configuration [scopes](https://github.com/css/csso#scopes). Les scopes définissent des listes de noms de classe qui sont exclusivement utilisés sur certains balisages, c'est-à-dire que les sélecteurs de différents scopes ne correspondent pas au même élément. Cette information permet à l'optimiseur de déplacer les règles de manière plus agressive.

Pour tirer parti de cela, utilisez [csso-webpack-plugin](https://github.com/zoobestik/csso-webpack-plugin) pour post-traiter le bundle CSS:

Cela a réduit la taille du bundle CSS de [GO2CINEMA](https://go2cinema.com/) de 53 Ko à 47 Ko.

#### Est-ce que cela en vaut la peine?

Le premier argument contre une telle minification est que les algorithmes de compression le feront pour vous. Le bundle CSS de GO2CINEMA compressé en utilisant l'algorithme [Brotli](https://en.wikipedia.org/wiki/Brotli) économise seulement 1 Ko par rapport au bundle original avec les longs noms de classe.

D'un autre côté, la configuration de cette minification est un investissement ponctuel et elle réduit la taille du document qui doit être analysé. Elle a d'autres avantages, tels que dissuader les scrapers qui dépendent des noms de classe CSS pour naviguer ou correspondre accidentellement aux sélecteurs CSS des listes noires des [bloqueurs de publicités](https://gist.github.com/spyesx/42fe84c0ef757d1c38a4).

Pendant ce temps, vous pouvez voir une démonstration de cette minification utilisée sur les pages de films et de lieux de GO2CINEMA, par exemple

* [https://go2cinema.com/movies/wonder-woman-2017-1305237](https://go2cinema.com/movies/wonder-woman-2017-1305237)
* [https://go2cinema.com/venues/odeon-oxford-magdalen-st-1001053](https://go2cinema.com/venues/odeon-oxford-magdalen-st-1001053)

#### Pouvez-vous m'aider avec GO2CINEMA?

[GO2CINEMA](https://go2cinema.com/) est mon bébé. J'adore travailler dessus ?. Cependant, c'est ma première startup de cette décennie et il y a beaucoup de choses pour lesquelles j'ai besoin d'aide.

Si vous pouvez donner des commentaires, un conseil SEO, un conseil commercial, connaître un investisseur providentiel, connaître quelqu'un qui peut écrire un article sur [GO2CINEMA](https://go2cinema.com/), faire un tweet, m'inviter à une conférence, une émission de radio, etc. ou simplement exprimer votre soutien/curiosité et dire « Salut ! », envoyez-moi un email à gajus@gajus.com ou DM via Twitter, [https://twitter.com/kuizinas](https://twitter.com/kuizinas).

### Vous aimez lire, j'aime écrire

Vous pouvez soutenir mon [travail open-source](https://github.com/gajus) et mes articles techniques via [Buy Me A Coffee](https://www.buymeacoffee.com/gajus) et [Patreon](https://www.patreon.com/gajus). Vous aurez ma gratitude éternelle ?