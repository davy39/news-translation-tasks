---
title: Plonger dans les courbes de Bézier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-24T03:36:03.000Z'
originalURL: https://freecodecamp.org/news/nerding-out-with-bezier-curves-6e3c0bc48e2f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i1mnGie2xQNwMAetiiMeSw.jpeg
tags:
- name: Design
  slug: design
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Plonger dans les courbes de Bézier
seo_desc: 'By Nash Vail

  Since the past few days I have been trying to write my own little JavaScript animation
  library. I know I know no one really cares about a new animation library but hey,
  the point is, in the process I stumbled on to Bezier curves. I spent...'
---

Par Nash Vail

Depuis quelques jours, j'essaie d'écrire ma propre petite bibliothèque d'animation JavaScript. Je sais, je sais, personne ne se soucie vraiment d'une nouvelle bibliothèque d'animation, mais bon, le point est que, dans le processus, je suis tombé sur les courbes de Bézier. J'ai passé quelques heures à faire des recherches, à essayer de les comprendre, au cours desquelles je suis tombé sur cet article frais — « [Intuition mathématique derrière les courbes de Bézier](https://buildingvts.com/mathematical-intuition-behind-bezier-curves-2ea4e9645681#.qwbh5kssy) », qui est également l'inspiration pour cet article. C'est mathématique et semble destiné aux gens intelligents, donc j'ai eu un peu de mal à comprendre le concept. Mais, heureusement, à la fin, j'ai compris et cela m'a conduit à apprendre un certain nombre de nouvelles choses cool sur les courbes de Bézier que je suis très excité de partager avec vous.

#### Ce que vous allez apprendre

Je commencerai par une introduction aux courbes, ce qu'elles sont, pourquoi elles sont cool, leur représentation mathématique. Ne vous inquiétez pas pour les maths, pour être honnête, je suis un peu nul en maths, donc je dois trouver des moyens d'essayer de me l'expliquer à moi-même et je suis sûr que « les moyens » fonctionneront pour vous aussi :).

Ensuite, nous passerons aux courbes de Bézier. Ce qu'elles sont, et ce qui les rend différentes. Leur formule mathématique.

Vers la fin, nous construirons notre propre petit moteur de dessin de courbes de Bézier en JavaScript et SVG. C'est cool, non ?

### Courbes

Je n'ai pas besoin de donner une définition formelle de courbe ici, n'est-ce pas ? Toutes ces lignes sont des courbes, regardez-les

![Image](https://cdn-media-1.freecodecamp.org/images/my8th8Jldqw-kxYMJCGRHpFnXHG5zRTR31GC)
_Des courbes, des courbes, toutes des courbes_

Les courbes sont assez sympas, elles peuvent représenter un certain nombre de choses. Par exemple, la courbe ci-dessous montre le nombre de [mes abonnés sur Twitter](http://twitter.com/NashVail) au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/LXB5spmu33pv7bBIEtBPNtpV29O0qS0tnKCp)

D'accord, cela ressemble à une ligne griffonnée au hasard. Laissez-moi ajouter un peu de contexte.

![Image](https://cdn-media-1.freecodecamp.org/images/MAXIMca895Ct0B3dVVfX3qB0AOeuFRZ68IFq)
_Excusez mon écriture_

Cela devrait maintenant donner une meilleure idée de ce que cela représente. Sur l'axe horizontal se trouve le nombre de jours depuis que j'ai rejoint Twitter et sur l'axe vertical se trouve le nombre d'abonnés que j'ai gagnés.

Le premier jour sur Twitter, je n'avais aucun abonné, puis cela a lentement augmenté, j'en ai perdu certains, j'en ai gagné certains, puis dans la seconde moitié, comme vous pouvez le voir, j'ai gagné un certain nombre de nouveaux abonnés. Ce n'est pas la seule information que nous pouvons décrypter à partir de cette courbe. Je peux également trouver le nombre exact d'abonnés que j'avais à un jour donné. Il s'agit simplement de tracer deux lignes.

Disons que je veux savoir le nombre d'abonnés que j'avais au 60ème jour.

![Image](https://cdn-media-1.freecodecamp.org/images/AISquiZlfADsmht8487pFTdKqp2BSDyEInE-)

Je trace une ligne verticale à partir de _60_ sur l'axe horizontal, puis à partir du point où cette ligne intersecte la courbe, je trace une ligne horizontale. Cette ligne horizontale intersecte l'axe vertical (axe avec le nombre d'abonnés) en un point. La valeur de ce point sur l'axe vertical me donne le nombre exact d'abonnés que j'avais au 60ème jour, qui est 126.

Maintenant, là où les deux lignes rouges se croisent, c'est ce qu'on appelle un **point**. Sur un graphique en deux dimensions, comme notre graphique des abonnés Twitter, un point est identifié de manière unique par deux valeurs, sa coordonnée horizontale (_x_) et sa coordonnée verticale (_y_). Par conséquent, écrire _(x, y)_ est tout ce dont on a besoin pour représenter un point. Dans notre cas, le point rouge, où les deux lignes rouges se croisent, peut s'écrire _(60, 126)._

**(60 = x/Coordonnée horizontale, 126 = y/Coordonnée verticale)**

D'accord, assez parlé de ce qu'est un point, vous le saviez déjà. Parlons de la courbe, qui est _en fait_ une **collection de nombreux points** n'est-ce pas ?

Vous prenez un tableau de données comme au 0ème jour 0 abonnés, au 1er jour 50 abonnés … au 10ème jour 76 abonnés ... au 100ème jour 500 abonnés … et ainsi de suite. Vous convertissez ces données en points (0, 0) (1, 50) … (10, 76) … (100, 500) … Vous tracez les points sur le graphique, vous les reliez ensemble et voilà, vous avez une courbe.

Donc, pour une courbe, vous avez besoin de points et pour des points, vous avez besoin de valeurs x et y correspondantes. Par conséquent, maintenant, prenez garde ici, une courbe peut être représentée de manière unique par quelque chose qui peut nous donner des valeurs x et/ou y. Ce « quelque chose » est ce que nous appelons en mathématiques une _fonction._

Il existe de nombreuses fonctions standard en mathématiques. Considérons la fonction _sinus._

![Image](https://cdn-media-1.freecodecamp.org/images/9j9Qewq3fMTcEWMv-7ncPPRBoqmWDoZhQMvX)

Dans des fonctions comme celle-ci, le choix de x nous appartient. Nous lui donnons un _x_, elle nous donne un _y_. Et ensemble nous formons un point (x, y). Nous lui donnons un autre x, elle nous donne un autre y, et ainsi de suite, nous finissons par avoir une collection de points, nous les traçons et obtenons une forme unique.

![Image](https://cdn-media-1.freecodecamp.org/images/oo2vUaX02Ru3Q7WsDFy0H0mp9bXsDEFbxk1R)
_Source : [http://forum.kerbalspaceprogram.com/index.php?/topic/69707-sine-graphs-and-orbital-paths/](http://forum.kerbalspaceprogram.com/index.php?/topic/69707-sine-graphs-and-orbital-paths/" rel="noopener" target="_blank" title=")_

Une fonction peut également être représentée sous _forme paramétrique_. Dans la forme paramétrique, nous n'avons pas besoin de fournir une partie de la coordonnée du point comme nous l'avons fait (x) dans l'exemple précédent. Au lieu de cela, nous fournissons un paramètre/variable, généralement écrit comme _t_ et pour chaque _t_ nous obtenons les coordonnées _x_ et _y_, en bref, nous fournissons un _t_ nous obtenons un point.

Vous voudrez savoir ce qu'est la forme paramétrique lorsque nous parlerons des mathématiques derrière les courbes de Bézier.

### Courbes de Bézier

Les courbes de Bézier sont des courbes très spéciales. Les mathématiques et l'idée derrière elles m'ont époustouflé et vous devriez vous préparer à être époustouflé aussi.

Puisque vous lisez ceci, je suppose que vous êtes un designer ou un développeur et que vous avez déjà traité avec des courbes de Bézier, surtout des courbes de Bézier cubiques, nous verrons ce que sont les courbes de Bézier cubiques dans un instant. Maintenant, ces courbes sont utilisées dans une variété de domaines, pour créer des graphiques vectoriels, des chemins d'animation, des [courbes d'assouplissement d'animation](http://cubic-bezier.com/) etc., seulement parce qu'elles sont si **faciles à contrôler**. Vous n'avez pas besoin de connaître beaucoup de mathématiques, aucune du tout pour plier ces courbes à vos caprices. Imaginez si les courbes de Bézier n'existaient pas et que les gens devaient inventer des fonctions mathématiques uniques pour les courbes, par exemple pour dessiner des graphiques vectoriels comme des polices, un cauchemar bien sûr.

#### Math ?

D'accord, il est temps de faire quelques maths. Je vais commencer par la formule générale des courbes de Bézier, elle est assez intimidante à première vue, mais nous allons nous y retrouver.

![Image](https://cdn-media-1.freecodecamp.org/images/VzB9kgV4zGmyk2996nLmXGn7c8NXxibmWuwu)
_Formule générale pour une courbe de Bézier de degré n_

« Whoa ! Whoa ! Whoa ! Einstein ! ». Hé, attendez, ne cliquez pas. C'est facile, regardez, je l'ai rendu si coloré ?.

Commençons à décomposer la formule. Vous pouvez sauter les parties que vous connaissez déjà.

#### B(t)

![Image](https://cdn-media-1.freecodecamp.org/images/o5yPWZ1pmkuYereoCHlpK7dS0PhXrE2mwGnf)

_B_ parce que c'est une courbe de **B**ézier. Comme mentionné précédemment dans l'article sur la forme paramétrique des courbes, _t_ est un paramètre. Vous branchez _t_ et vous obtenez _x_ et _y_, un point. Nous verrons bientôt comment cela fonctionne avec l'équation ci-dessus. Il sera bon de mentionner ici que pour les courbes de Bézier, la valeur de _t_ doit être comprise entre 0 et 1, tous deux inclus.

#### Σ / Sigma

![Image](https://cdn-media-1.freecodecamp.org/images/EWA9lG4GtmEGRZQ6aWJuZzm10AWf4LncbyCw)

Ce symbole, Σ, en mathématiques est appelé l'opérateur de sommation. La façon dont il fonctionne est la suivante, à droite de ce symbole se trouve une expression avec une variable i, et i ne peut prendre que des valeurs entières. En haut et en bas du symbole, nous écrivons les limites de i. Pour chaque valeur de i, l'expression à droite est évaluée et ajoutée au total jusqu'à ce que i atteigne n.

Voici quelques exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/-Ya0sgRAwA0SbyUXDSNETHqWYpZ2BZM3YHNY)

![Image](https://cdn-media-1.freecodecamp.org/images/mqJTHlU9wIKg6IPa8bm2zl2rJWkQCc6tVESs)

Juste une notation plus courte pour quelque chose de plus long.

D'accord, il semble que nous soyons clairs avec sigma.

#### nCi

![Image](https://cdn-media-1.freecodecamp.org/images/eI4B658UU-GPQXVb4qa32ad0rRKSxjWPwk4I)

Ce _C_ ici, est le C des Permutations et **C**ombinaisons. Faisons un cours improvisé sur les Combinaisons, d'accord ? Maintenant, dans la formule, cette partie est ce qu'on appelle un coefficient binomial. La façon de lire nCi est comme suit, n _Choisir_ i. Ce qui signifie, étant donné n éléments, de combien de façons pouvez-vous choisir i éléments parmi eux (n est toujours supérieur ou égal à i). D'accord, cela n'a peut-être pas eu beaucoup de sens, considérons cet exemple : j'ai 3 éléments, un cercle, un carré et un triangle. Par conséquent, ici, n = 3. De combien de façons puis-je choisir 2 (i = 2) éléments parmi les 3. En langage mathématique, cela s'écrirait 3C2 (3 Choisir 2). La réponse est 3.

![Image](https://cdn-media-1.freecodecamp.org/images/4ZsMR8pbFHW3yntKbMtHCjOHrwR8ZJEPgDSb)

De même,

![Image](https://cdn-media-1.freecodecamp.org/images/lv7PaI-MUWLVvUnHSoOAzybkZ7qXurH1xkqa)

Et lorsque i est 0, il n'y a qu'une seule façon de choisir 0 élément parmi n, 1, ne rien choisir du tout.

Au lieu de dessiner des croquis et de trouver la réponse à une expression de Combinaison donnée, il y a cette formule généralisée.

![Image](https://cdn-media-1.freecodecamp.org/images/5xYXsUvebuQVIeikLx-ABWhYlkVMjrSLn9FB)

#### P sous i

![Image](https://cdn-media-1.freecodecamp.org/images/si0z5BQj4NU5hGuvCDFezZwVlj3r7RRCuAOL)

C'est la partie importante. Dans la formule générale de la courbe de Bézier, il y a t, i et n. Nous n'avons pas vraiment abordé ce qu'est n. n est ce qu'on appelle le degré de la courbe de Bézier. n est ce qui décide si une courbe de Bézier est linéaire, quadratique, cubique ou autre chose.

Vous voyez, si vous avez utilisé l'outil plume auparavant, vous cliquez à deux endroits distincts pour créer deux points distincts, puis vous contrôlez la courbe qui se forme entre les deux points à l'aide de poignées. Une courbe de Bézier aura toujours au moins deux points d'ancrage, et les autres sont des points de contrôle utilisés pour contrôler la forme de la courbe. De plus, ce que vous appelez des poignées ne sont que les points de contrôle connectés par une ligne à un point d'ancrage, ils sont juste là pour fournir un meilleur modèle mental. Donc, lorsque vous ajustez les poignées, en réalité, vous changez simplement les coordonnées des points de contrôle.

![Image](https://cdn-media-1.freecodecamp.org/images/nhFD2G9h7PxAX5-V8-uKKasvHSk1cgGlvmiN)
_Une courbe de Bézier cubique_

Débarrassons-nous de tous les accessoires et concentrons-nous sur l'essentiel.

![Image](https://cdn-media-1.freecodecamp.org/images/UXZCVKTmdlaeOeDYNaUAP3OEY-HBF2jYb11o)
_Courbe de Bézier cubique_

La courbe que vous voyez dans l'image ci-dessus est une _courbe de Bézier cubique_, ou en d'autres termes, le degré de la courbe de Bézier montrée ci-dessus est 3, ou dans la formule générale des courbes de Bézier, vous branchez n = 3.

n = 1 vous donne une courbe de Bézier linéaire avec deux points d'ancrage P0 et P1 et aucun point de contrôle, donc elle se termine essentiellement par une ligne droite.

n = 2 vous donne une courbe de Bézier quadratique avec deux points d'ancrage P0 et P2 et un point de contrôle P1

et de même n = 3 vous donne une courbe de Bézier cubique avec deux points d'ancrage P0 et P3 et deux points de contrôle P1 et P2. Plus n est élevé, plus des formes compliquées peuvent être dessinées.

Maintenant, nous allons former à partir de l'équation générale l'équation pour la courbe de Bézier cubique qui implique de substituer n = 3 dans la formule générale. L'équation que nous obtiendrons sera dans la variable _t_ qui, comme mentionné précédemment, est un paramètre dont la valeur varie entre 0 et 1. De plus, pour l'équation, nous aurons besoin de 4 Pis (lire : Pee eyes) P0, P1, P2 et P3. Le choix de ces points nous appartient, après tout, lorsque nous dessinons des graphiques vectoriels, par exemple en utilisant l'outil plume, nous choisissons la position des points d'ancrage et des points de contrôle, n'est-ce pas ? Après les changements, notre équation pour la courbe de Bézier cubique ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/60MnEVvXYutR7RZADBTfQ3akvL-6C3tgbDVO)
_Équation développée pour une courbe de Bézier cubique_

Nous utilisons ici une petite brièveté, en réalité chaque point (P) a deux coordonnées x et y et également en passant t à l'équation générale, nous devons obtenir un point qui a également des coordonnées x et y. Par conséquent, nous pouvons écrire l'équation ci-dessus comme

![Image](https://cdn-media-1.freecodecamp.org/images/yh0JfMYGC9XYyDbPTx99R6l6EN-4TZL3rgWT)
_Équation développée pour la courbe de Bézier cubique_

Vous allez assister à quelque chose de très spécial à propos de ces équations.

![Image](https://cdn-media-1.freecodecamp.org/images/XrMSfqOci0UByHBrWKWmRQkytlnJCvyrolOP)

Pour résumer, l'équation mentionnée est la forme paramétrique de la courbe de Bézier avec le paramètre _t_ qui peut prendre des valeurs variant entre 0 et 1. Une courbe est une collection de points. Chaque _t_ unique que vous passez à B donne un point unique qui construit toute la courbe de Bézier.

La chose magique à propos de l'équation est que lorsque t = 0, B(0) = P0 et lorsque t = 1, B(1) = P3, donc les valeurs extrêmes de t, 0 et 1, donnent les points les plus extrêmes de la courbe qui sont bien sûr les points d'ancrage. Ce n'est pas vrai seulement pour les courbes de Bézier cubiques, pour une courbe de degré n, B(0) = P0 et B(1) = Pn.

Pour toute autre valeur de _t_ entre 0 et 1 (par exemple t = 0,2 dans la figure ci-dessus), vous obtenez un point qui construit la courbe.

Puisque toute l'équation dépend de la position des Pis (Pee eyes), changer leur position change la forme de la courbe. Et c'est ainsi que fonctionnent les courbes de Bézier.

Maintenant que nous connaissons les mathématiques derrière les courbes de Bézier, utilisons ces connaissances.

J'ai créé un simple programme JavaScript qui rend une courbe de Bézier cubique, il n'y a pas d'interface utilisateur pour interagir avec elle parce que je ne voulais pas que la logique se perde dans tout le code de l'interface utilisateur et aussi parce que je suis paresseux. Mais cela ne signifie pas que vous ne pouvez pas interagir avec elle :).

![Image](https://cdn-media-1.freecodecamp.org/images/k17s4GCAqO6CEbl-qdS3Xpkent8q33vLjFvy)

C'était un peu trop à assimiler ? Nous avons commencé par définir ce que sont les courbes, de là nous sommes passés aux points et à la manière dont ils sont les éléments de base d'une courbe. Ensuite, nous sommes passés aux courbes de Bézier et avons compris les mathématiques pour trouver les points qui constituent une courbe de Bézier. J'espère que vous avez appris quelque chose et que vous quittez cet article plus intelligent que lorsque vous avez commencé à le lire.

Le code pour le petit moteur de Bézier cubique personnalisé peut être trouvé dans ce [dépôt GitHub](https://github.com/nashvail/BezierCurveGenerator).

**Mise à jour :** Le générateur peut maintenant générer une courbe de Bézier de n'importe quel degré et pas seulement des courbes de Bézier cubiques :).

#### Vous cherchez plus ? Je publie régulièrement sur mon [blog à l'adresse nashvail.me](https://nashvail.me). À bientôt, passez une bonne journée !

![Image](https://cdn-media-1.freecodecamp.org/images/gpMsnBPV7hDXYViIrf4o5oSv86GnGJ0UeL4V)