---
title: 'Pourquoi vous devriez utiliser des images SVG : comment animer vos SVGs et
  les rendre ultra-rapides'
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2019-11-26T14:51:07.000Z'
originalURL: https://freecodecamp.org/news/a-fresh-perspective-at-why-when-and-how-to-use-svg
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/svg.png
tags:
- name: 100Days100Projects
  slug: 100days100projects
- name: Design
  slug: design
- name: SVG
  slug: svg
seo_title: 'Pourquoi vous devriez utiliser des images SVG : comment animer vos SVGs
  et les rendre ultra-rapides'
seo_desc: 'Why Are We Using SVG?

  The web development sector is growing at a rapid pace, and SVG (scalable vector
  graphics) images are becoming more popular. As vector images, SVGs are composed
  of mathematical equations that define the positioning and color of l...'
---

## **Pourquoi utilisons-nous le SVG ?**

Le secteur du développement web évolue à un rythme rapide, et les images SVG (graphiques vectoriels adaptables) deviennent de plus en plus populaires. En tant qu'images vectorielles, les SVGs sont composés d'équations mathématiques qui définissent le positionnement et la couleur des lignes et des courbes formant des formes graphiques et du texte au format XML. Les SVGs sont utilisés pour les icônes, les logos, les designs graphiques et les polices.

L'utilisation des SVGs est un choix facile une fois que vous considérez les avantages qu'ils offrent. Pour un client, vous obtenez une qualité supérieure sur n'importe quel appareil. Pour nous, en tant que développeurs, il y a encore plus de raisons d'utiliser le SVG.

Discutons maintenant de certains des avantages du SVG.

### **1. Format basé sur du texte**

Les éléments SVG contiennent du texte, ce qui améliore grandement l'accessibilité d'un site web. Mais l'avantage principal est que ce texte est indexé par les moteurs de recherche. Et un utilisateur peut trouver un fichier SVG via Google.

### **2. Adaptabilité**

La qualité des images SVG ne dépend pas de la résolution. Contrairement aux images d'autres formats ou aux polices d'icônes, les SVGs apparaissent parfaitement nets sur n'importe quel appareil avec n'importe quelle taille d'écran. L'adaptabilité signifie également que si vous utilisez la même image sur l'ensemble du site web mais dans différentes tailles, vous utilisez un seul SVG. Vous n'avez pas à créer plusieurs copies comme dans le cas du PNG. Au lieu de cela, vous intégrez la même image et définissez sa taille directement dans le code SVG.

![Adaptabilité](https://images.ctfassets.net/6xhdtf1foerq/u6zLw9HQVb8DpDR1rhvHp/a5e491c95b5261e47e1c28098b2a2422/Copy_of_2.7_billion_people_use_smartphones__1_-min.png?fm=png&q=85&w=1000)

### **3. Haute performance**

Si vous privilégiez la performance, vous devriez utiliser le SVG. Avec le SVG, il n'est pas nécessaire de faire une requête HTTP pour charger un fichier image. La page se charge plus rapidement car elle n'a pas de fichiers à télécharger. Un temps de chargement plus rapide se traduit par de meilleures performances de la page web et un meilleur classement dans les moteurs de recherche. Cela améliore également l'expérience utilisateur.

### **4. Petite taille de fichier**

La taille des fichiers SVG simples est définie par les couleurs, les calques, les dégradés, les effets et les masques qu'ils contiennent. La taille d'un fichier PNG ou de tout autre fichier de graphiques matriciels est définie par le nombre de pixels qui le composent. Plus une image PNG est grande, plus elle devient lourde. Ce n'est pas le cas pour les icônes SVG, cependant. De plus, les SVGs peuvent être optimisés, et je vous expliquerai comment plus tard dans cet article.

![Taille de fichier SVG](https://images.ctfassets.net/6xhdtf1foerq/6TEDo4rR558facWlrHZjlT/ab71bf067cf14098d65c602eac3d5735/Copy_of_2.7_billion_people_use_smartphones__2_-min.png?fm=png&q=85&w=1000)

### **5. Nombreuses opportunités d'édition et d'animation**

Contrairement aux images matriciels, les images vectorielles peuvent être éditées à la fois dans des programmes spéciaux de dessin vectoriel et directement dans un éditeur de texte. Vous pouvez également éditer les couleurs ou les tailles des icônes SVG directement via CSS. En ce qui concerne l'animation des SVGs, cela peut être fait à l'aide de SMIL, Web Animations API, WebGL ou de l'animation CSS. Faites défiler vers le bas pour en savoir plus sur l'animation CSS des images SVG.

### **6. Intégration avec HTML, XHTML et CSS**

Le SVG a été conçu « pour s'intégrer et étendre d'autres technologies Web ouvertes majeures, telles que X/HTML, CSS et Javascript », selon [<ins>W3C</ins>](https://dev.w3.org/SVG/proposals/svg-html/svg-html-proposal.html). Ainsi, contrairement à différents formats d'image, ce format peut être facilement intégré avec d'autres documents et technologies.

### **7. Support du modèle d'objet de document W3C**

Il y a un soutien croissant de la communauté pour le SVG. Le [<ins>World Wide Web Consortium</ins>](https://www.w3.org/) (W3C) a toujours affirmé que l'Internet ne peut pas se passer d'images vectorielles. Cette organisation a essentiellement [<ins>créé le format SVG</ins>](https://www.w3.org/2002/04/svg11-pressrelease), et ils le soutiennent activement de nos jours.

## **Quels sont les inconvénients du SVG ?**

Le grand nombre de petites parties rend l'utilisation du format SVG irrationnelle. Plus une image est composée de parties, plus elle devient lourde en taille.

Par exemple, [<ins>ici</ins>](https://www.amcharts.com/svg-maps/?map=usa) se trouvent deux cartes SVG des États-Unis. La seconde est légèrement plus détaillée que la première. Mais le niveau de détail plus élevé a coûté une augmentation presque quintuplée de la taille du fichier – 33 Ko contre 147 Ko. Si cette carte n'était pas monochromatique, l'augmentation aurait été beaucoup plus grande.

![Cartes SVG](https://images.ctfassets.net/6xhdtf1foerq/4xg76fiYHZzxpSxDXW9uFp/4f5161cd3efc5dd2ea0d9578388498f0/Copy_of_2.7_billion_people_use_smartphones__3_-min.png?fm=png&q=85&w=1000)

Si l'image est linéaire et contient peu de couleurs, le SVG est une solution. Cependant, si les détails comptent et qu'il y en a beaucoup, le PNG ou le JPEG peuvent être plus adaptés.

Notez également que le SVG ne peut pas être utilisé pour les photographies. Si vous utilisez une photographie sur votre site web, le SVG n'est pas la meilleure option. Vous devriez définitivement opter pour un format d'image matricielle.

## **Comment optimiser les images SVG**

Lors du rendu d'un format vectoriel, nous devons écrire un peu de code SVG supplémentaire. Le résultat final doit être optimisé à l'aide de différents services. Le plus souvent, pour optimiser le SVG, j'utilise un outil <ins>[Node.js](https://keenethics.com/services-web-development-node)</ins> appelé [<ins>SVGO</ins>](https://github.com/svg/svgo). Il est assez facile à utiliser, et il n'est pas nécessaire de télécharger les images sur d'autres sites web.

![Exemple d'optimisation SVG utilisant SVGO](https://images.ctfassets.net/6xhdtf1foerq/7m9UpCpPW7GNLR9tXAvTca/4c804519c3dd110b650977f72785453a/0_8YcO63_4ajXq0qEb.)
_Exemple d'optimisation SVG utilisant SVGO_

## **Comment animer le SVG**

Les graphiques SVG sur le web peuvent être animés de plusieurs manières :

1. SMIL, qui est la spécification native d'animation SVG
2. Web Animations API, qui est une API JavaScript native vous permettant de créer des animations séquentielles plus complexes sans charger de scripts externes
3. WebGL
4. Animation CSS

Considérons cette dernière.

**L'animation CSS** est utilisée afin d'éviter de surcharger votre service avec de grandes bibliothèques pour animer des icônes et des chargeurs.

Pour voir l'exemple de SVG, consultez [<ins>le jaune animé</ins>](http://jsfiddle.net/yd3c81bg/9/embedded/html,css,result), dont le design graphique a été initialement dessiné dans Sketch.

![SVG gif](https://images.ctfassets.net/6xhdtf1foerq/7JTBd4pwJJwKYmqgTSwScv/525b6d4e42c53c35961706390802bc5e/ezgif.com-crop.gif)

Comme vous pouvez le voir ici, j'utilise la syntaxe d'animation Keyframe pour l'animation. Elle est implémentée en définissant la position initiale d'un élément par son id (0 %), la transition (50 %) et la position finale (100 %). Pour obtenir une animation fluide, les valeurs initiale et finale sont égales.

Voici quelques **avantages** de l'utilisation de l'approche CSS pour l'animation SVG :

1. Vous n'avez pas besoin d'une bibliothèque externe.
2. Les préprocesseurs (comme Sass ou Less) vous permettent de créer des variables.
3. Vous pouvez utiliser onAnimationEnd et certains autres hooks d'animation avec JavaScript natif.
4. Cette approche est facile à utiliser pour le développement de design web réactif car vous pouvez modifier votre animation avec des requêtes média.

Les **inconvénients** de l'utilisation de l'animation CSS sont les suivants :

1. Vous ne pouvez pas produire certains effets physiques complexes, ce qui rendrait l'animation plus réaliste.
2. Beaucoup de recalculs doivent être effectués si vous ajustez le timing.
3. CSS et les graphiques SVG sur mobile nécessitent parfois des astuces étranges.

## **Par exemple**

Néanmoins, nous pouvons réaliser des projets intéressants à l'aide d'une animation CSS simple et triviale. Par exemple, j'ai créé une simple vidéo-jeu en utilisant HTML, CSS et un peu de JavaScript. Tous les SVGs ont été dessinés dans Sketch. L'objectif de ce jeu est de sauver la princesse. Dans n'importe quelle situation, il suffit de cliquer. Vous pouvez trouver le projet sur mon [<ins>GitHub</ins>](https://github.com/maryna-yanul/duck-the-princess/).

## **Pour conclure**

Les SVGs sont un excellent format d'image à adopter. Ils sont adaptables, légers, basés sur du texte et efficaces. Ils sont faciles à éditer, animer et intégrer. Importamment, ils sont supportés par presque tous les navigateurs à l'exception d'Internet Explorer 8 et Android 2.3.

Bien que l'apprentissage du travail avec des images vectorielles adaptables puisse prendre un certain temps, c'est un investissement qui portera ses fruits compte tenu des avantages du SVG.

## Avez-vous une idée pour un projet logiciel ?

Mon entreprise KeenEthics est une équipe de développeurs expérimentés en [applications web](https://keenethics.com/services-web-development). Si vous avez besoin d'une estimation gratuite pour un projet similaire, n'hésitez pas à [nous contacter](https://keenethics.com/contacts?activeForm=estimate).

Vous pouvez lire plus d'articles similaires sur mon Keen Blog. Permettez-moi de vous suggérer de lire [La Valeur des Tests Utilisateurs](https://keenethics.com/blog/the-value-of-user-testing) ou [7 Cas Où Vous Ne Devriez Pas Utiliser Docker](https://www.freecodecamp.org/news/7-cases-when-not-to-use-docker/).

## P.S.

Je voudrais également dire "merci" à [Maryna Yanul](https://www.linkedin.com/in/yanul/) pour la co-rédaction de cet article ainsi qu'aux lecteurs pour l'avoir lu jusqu'à la fin !

L'article original publié sur le blog KeenEthics peut être trouvé ici : [Une Nouvelle Perspective sur Pourquoi, Quand et Comment Utiliser le SVG](https://keenethics.com/blog/1478674800000-svg-animation-scalable-vector-graphics).