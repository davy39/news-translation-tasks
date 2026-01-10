---
title: Comment construire le div de Schrödinger ? avec Vue !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T19:26:33.000Z'
originalURL: https://freecodecamp.org/news/how-we-can-build-schrodingers-div-with-vue-4068f6423830
coverImage: https://cdn-media-1.freecodecamp.org/images/1*spoAQtMm1OBMU1iciAZmzg.png
tags: []
seo_title: Comment construire le div de Schrödinger ? avec Vue !
seo_desc: 'By ZAYDEK

  There’s a 50% chance we’ll get this right…

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I created
  a short questionnaire to che...'
---

Par ZAYDEK

#### Il y a 50 % de chances que nous ayons raison...

Avant de commencer l'article, je souhaite partager que je développe un produit et que j'aimerais collecter des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de le consulter — et maintenant, revenons à notre programme habituel.

![Image](https://cdn-media-1.freecodecamp.org/images/JzU2vsqeYVGGDIMtAFHsrXZ9AgC0-bVH7fwi)

### Bonjour Internet !

Vous ne savez probablement pas qui je suis *tousse* je suis [Zaydek](https://twitter.com/username_ZAYDEK) *tousse*, mais je sais qui vous êtes ! Vous êtes un développeur web aspirant et prometteur, intéressé à apprendre de nouvelles technologies, mais un peu hésitant car les frameworks vont et viennent, et JavaScript est bien... JavaScript ! Pour le dire légèrement.

Alors, permettez-moi de prendre quelques minutes de votre temps pour vous convaincre que apprendre Vue pourrait être une excellente décision. Vous devriez l'apprendre non seulement pour vos qualifications, mais aussi pour le pur plaisir et la joie qui accompagnent l'apprentissage d'un logiciel bien documenté et orchestré.

#### J'enseigne également comment cela fonctionne et bien plus dans le cours Vue que je viens de publier. Apprenez Vue depuis les bases et comment construire quelques choses aussi ! C[liquez ici pour vous inscrire gratuitement !](https://scrimba.com/g/glearnvue)

![Image](https://cdn-media-1.freecodecamp.org/images/Q5mqNqLWLYLhNAOUrVSXEdB7JggDGgdVn-el)
_[Cliquez pour vous inscrire à mon cours Vue gratuit](https://scrimba.com/g/glearnvue" rel="noopener" target="_blank" title=")_

#### [Scrimba.com](https://scrimba.com/g/glearnvue) est un nouveau site interactif pour apprendre et partager comment coder. Les screencasts peuvent être interrompus et modifiés, rendant l'apprentissage actif et amusant à expérimenter !

### Bonjour, Felix !

[Le chat de Schrödinger](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat) est une expérience de pensée morbide proposée par Albert Einstein et Erwin Schrödinger pour se moquer de l'absurdité de la physique quantique. C'est une expérience (in)concevable pour laquelle l'aléatoire à un niveau micro peut être mesuré dans le macro-monde que nous expérimentons. Ironiquement, elle est devenue une pièce centrale pour expliquer la physique quantique !

Vous pouvez en apprendre davantage sur l'expérience et ses origines [ici](http://nautil.us/issue/41/selection/how-einstein-and-schrdinger-conspired-to-kill-a-cat).

Cela se passe comme suit : Vous avez un chat. Vous le mettez dans une boîte scellée. Dans la boîte est placé un matériau radioactif qui, sur une heure, a 50 % de chances qu'un de ses atomes s'ionise. Également placé dans la boîte se trouve un compteur Geiger, qui est un appareil de mesure. S'il détecte un atome ionisé, il libérera un marteau qui brisera une fiole de poison, tuant ainsi le chat ! ??

Voici une explication plus académique du chat de Schrödinger :

> Le scénario présente un chat qui peut être simultanément à la fois vivant et mort, un état connu sous le nom de superposition quantique, résultant d'être lié à un événement subatomique aléatoire qui peut ou non se produire...

> ... Schrödinger ne souhaitait pas promouvoir l'idée de chats morts-et-vivants comme une possibilité sérieuse ; au contraire, il entendait que l'exemple illustre l'absurdité de la vision existante de la mécanique quantique.

> — [Wikipedia](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat#Origin_and_motivation)

Et c'est ce que nous allons construire en utilisant Vue ! ? Ce ne sera pas si difficile, mais nous trichons un peu car nous allons nous appuyer sur les facilités pseudo-aléatoires de JavaScript et non sur des atomes ionisés !

Pour ce cours, vous devriez connaître un peu de JavaScript et de HTML. Mais [dans le cours que je viens de publier](https://scrimba.com/g/glearnvue), je consacre 10 minutes à enseigner les bases absolues de JavaScript nécessaires pour commencer avec Vue ! [Alors n'oubliez pas de vous inscrire !](https://scrimba.com/g/glearnvue)

### Construire le div de Schrödinger

![Image](https://cdn-media-1.freecodecamp.org/images/eGCUyk4FWzRswbeA6e4YCbYCVOl8y2sFOBdE)

![Image](https://cdn-media-1.freecodecamp.org/images/fixclM1DbhaY4DQOXdmV5GwDgeTTzZUaTqao)

![Image](https://cdn-media-1.freecodecamp.org/images/NUcSEKbB1PCj4JBoAL5ZYK5pn8Ksokcd7VMv)
_Cliquez pour lancer les dés.. ?_

En utilisant Vue, nous pouvons lier un gestionnaire de clic à un `span` — j'ai menti, ce n'est pas un `div` — contenant le `?,` et sélectionner soit le ? `o`u ? `em`ojis. Cliquer dessus appelle une fonction qui émule le lancer de dés et révèle si notre chat a vécu ou est mort. Et cliquer à nouveau pourrait réinitialiser l'état à la boîte fermée originale. Tout cela peut être réalisé avec les attributs v-h`tml, @`cl`ick, a`nd :cl`ass de Vue.

![Image](https://cdn-media-1.freecodecamp.org/images/DsQgm6XM86dxM4PN93SJQYGwwTvjSojOKnJ4)

Psst.. le code complet est disponible dans le [huitième screencast](https://scrimba.com/p/pZ45Hz/ceJ3vUL).

À l'intérieur de `<div id="ap`p"> se trouve un p qui `affiche Cliquez sur la boîte ! Le cha`t...?! À l'intérieur du p `se trouve un` span avec quelques attribu`ts. v`-html `et emoj`ify() sont des techniques que j'utilise pour afficher les emojis en tant qu'images.

`@click="quantum_fluctuation()"` est la manière dont j'attache une fonction au `span` cliqué, et `:class="jittering()"` — également `:class="theme()"` — créent des effets spéciaux subtils.

Comprenons maintenant comment `quantum_fluctuation()` fonctionne : lorsqu'il est appelé, il invoque `Math.random()` de JavaScript pour influencer l'état de notre chat, qui est initialisé à `?,` et sélectionne soit ? `o`u ? `em`ojis.

Gardez à l'esprit que j'obfusque quelques détails pour le tableau d'ensemble, à savoir que nous avons l'état de notre chat, par exemple `this.cat`, stocké dans les données, et qu'un appel de fonction définit l'état de `this.cat`, qui est également mis à jour dans le DOM.

Vous pouvez bien sûr en apprendre davantage sur la mise en œuvre de `this.cat`, `rand()`, `this.alive_cats`, `this.dead_cats`, `this.is_open()`, et `this.is_alive()` dans le [screencast correspondant](https://scrimba.com/p/pZ45Hz/ceJ3vUL).

Pour aborder le fonctionnement des `:classes`, celles-ci renvoient des objets JavaScript qui lient des classes CSS normales en fonction de l'état de notre application. Et c'est une grande affaire, car cela signifie que notre CSS peut être considéré comme vivant. Whaaaaat!!

![Image](https://cdn-media-1.freecodecamp.org/images/3hm9upv14BeozAJasRDO4UwONrkjP71HClaY)

Le point principal est qu'il est désormais concevable — et sensé — pour un individu seul de créer des produits et services basés sur le web qui émulent la réactivité des applications natives modernes, tout cela sans la même dette technique. Et c'est une grande affaire car, bien que les applications natives soient agréables, elles nécessitent des étapes supplémentaires et souvent l'accès à des dizaines, voire à cent mégaoctets à télécharger. ?

#### Il y a beaucoup plus à apprendre sur Vue, alors j'ai écrit deux autres articles sur le sujet. S'il vous plaît, après cet article, jetez un coup d'œil !

![Image](https://cdn-media-1.freecodecamp.org/images/v82fTM9hJAhq4n2RC6euR6jsEq2758k-cDzx)

![Image](https://cdn-media-1.freecodecamp.org/images/evKfsXXPPpeztne9a8Xkjs89D6zUu5MxKFkq)
_Gauche : « [Comment créer un sélecteur de couleurs ? avec Vue !](https://medium.freecodecamp.org/learn-vue-js-in-our-free-course-85d5df41e47f" rel="noopener" target="_blank" title="">Apprenez Vue.js dans ce cours gratuit ! ?✨ »</a> Droite : « H<a href="https://medium.freecodecamp.org/how-to-make-a-color-picker-with-vue-9640043b6c82" rel="noopener" target="_blank" title=")_

### Vue est un superpouvoir déguisé en framework

J'adore les logiciels qui créent une valeur significative — et pas seulement pour les utilisateurs finaux, mais aussi pour les développeurs qui choisissent de les apprendre et de les utiliser. Les logiciels bien documentés et orchestrés sont agréables à apprendre, et c'est encore mieux lorsque l'expérience du développeur est à la hauteur de l'expérience utilisateur souhaitée. Vue ne fait pas exception ici, et programmer avec Vue a été une expérience délicieuse, et beaucoup plus facile que prévu.

J'ai refusé d'apprendre JavaScript pendant longtemps car, venant de langages de programmation hautement performants, concurrents et statiques, je m'étais habitué à un mépris général pour JavaScript. Cependant, après avoir appris Vue, ce qui est si attrayant, c'est que Vue fournit un guide idiomatique pour programmer en JavaScript, réduisant ainsi la charge et enseignant de bonnes pratiques de programmation.

Il n'y a jamais eu de meilleur moment pour se lancer dans le développement web. Avec l'introduction de CSS Flexbox et Grid, la conception web est devenue au moins un ordre de grandeur plus facile, plus amusante et plus puissante. Avec des langages backend comme Go et des frameworks frontend délicieux comme Vue, un programmeur/designer peut maintenant faire ce qui aurait nécessité des équipes entières ou des entreprises par le passé.

#### Alors, s'il vous plaît, allez dans le monde magnifique et apprenez Vue ! Vous pouvez (!) créer des choses incroyables et même changer la vie des gens, même la vôtre. Et si cela aide, [essayez le cours gratuit](https://scrimba.com/g/glearnvue) !

![Image](https://cdn-media-1.freecodecamp.org/images/K4EgWlAYcUSuINupYvMFrERMz5OmPnwS4J-V)