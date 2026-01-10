---
title: Les outils de design sont en panne d'innovation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-11T10:30:59.000Z'
originalURL: https://freecodecamp.org/news/design-tools-are-running-out-of-track-94f21b6ae939
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_VWdbAYvJcC4A8_uHGj_jQ.jpeg
tags:
- name: Design
  slug: design
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Les outils de design sont en panne d'innovation
seo_desc: 'By Colm Tuite

  Rarely a day goes by where I don’t spend at least some time thinking about design
  tools. A few years ago, I built a design tool which was acquired by Marvel. That
  was over two years ago but since then the landscape hasn’t changed much, ...'
---

Par Colm Tuite

Il est rare qu'une journée passe sans que je ne consacre au moins un peu de temps à réfléchir aux outils de design. Il y a quelques années, j'ai construit un outil de design qui [a été acquis par Marvel](https://techcrunch.com/2015/10/12/prototyping-app-marvel-acquires-design-tool-plexi/). Cela fait plus de deux ans, mais depuis, le paysage n'a pas beaucoup changé, ni ma passion pour l'améliorer.

Récemment, j'ai tweeté à propos des outils de design — une chose qui arrive de temps en temps.

Je n'étais pas le seul à exprimer mon opinion ce jour-là, d'autres ont également donné leur avis.

Le 28 juillet 2017 n'était pas un bon jour pour les outils de design.

Il y a beaucoup de grandes idées enterrées dans ces fils Twitter, mais depuis longtemps, j'ai voulu prendre le temps de plonger profondément dans ce qui, selon moi, est si fondamentalement cassé dans le modèle actuel des outils de design, ainsi que de donner un indice sur la direction que je pense que nous devrions prendre.

### Nous ne faisons tous que dessiner des images. C'est insensé.

Presque tous les outils de design populaires exportent vers des images. Cela pose problème pour un certain nombre de raisons :

1. Vous ne pouvez pas interagir avec une image. Les outils de prototypage nous permettent d'ajouter des transitions d'écran et des interactions simples aux images. Cependant, à mesure que nos produits continuent de demander des transitions d'écran plus avancées et des micro-interactions, les images ne peuvent tout simplement pas suivre.
2. Les images ne sont pas fluides. Communiquer les décisions de design responsif à travers des images est généralement une tâche difficile.
3. Les images ne sont pas étatiques. Afin de communiquer efficacement les différents états d'une UI, souvent de nombreuses images sont nécessaires.
4. Les images bitmap dépendent de la résolution. Avec l'avènement des appareils rétina, les images peuvent parfois rendre pauvrement.
5. Les fichiers images tendent à être lourds et sont souvent encombrants à stocker, gérer ou partager.

Tant que les outils de design continueront à exporter des images, ils ne pourront _jamais_ produire des représentations précises de nos produits. Ce manque de précision entrave la communication entre les designers et les développeurs. Tant que les designers continueront à utiliser un médium inadéquat pour communiquer leur travail, ce travail sera _toujours_ ouvert à la mauvaise interprétation.

C'est un point très significatif car, au cœur, presque tous les outils de design convertissent les formes vectorielles en images. Photoshop, Illustrator, Marvel, Adobe XD, Sketch et Figma sont tous les mêmes à cet égard. Pourtant, les images ne peuvent communiquer que partiellement l'intention de design. À mesure que nos produits continuent d'adopter et de supporter des interactions complexes, des entrées vocales, des entrées vidéo, la réalité augmentée, la réalité virtuelle, la sensibilité à la température, etc., la valeur que ces outils fournissent diminuera rapidement. Le design basé sur les images est une impasse.

Nos outils de design devraient manipuler le _produit réel_, pas une image de celui-ci.

### Nos produits sont interactifs. Nos outils sont statiques.

J'ai effleuré ce point précédemment, mais il est super critique, alors j'ai pensé que je pourrais élaborer un peu.

Pensez à la quantité d'interactions simples qui sont courantes dans presque tous nos produits, mais qui ne peuvent pas être communiquées à travers nos outils de design. Voici une brève liste qui me vient à l'esprit :

* Survoler un bouton
* Focus sur une entrée
* Cocher une case
* Contenu à onglets
* Zones de défilement
* Index de tabulation pour les états focus
* Raccourcis clavier

Bien sûr, certaines de ces fonctionnalités peuvent être imitées avec un peu de bidouillage, mais on peut se demander, quel est le but sur Terre ? Pourquoi les designers ne peuvent-ils pas simplement concevoir le _produit réel_ ?! En fin de compte, toutes les maquettes sont jetables, pourtant les designers passent des mois à les peaufiner à la perfection. Ce temps serait bien mieux utilisé à peaufiner le produit réel.

Je ne vais pas trop m'aventurer dans le terrier du lapin "les designers devraient-ils coder", mais je ne suggère pas que nous écrivions tous du code. Je dis simplement qu'il n'y a aucune bonne raison pour laquelle nos outils de design ne peuvent pas supporter la manipulation directe de nos produits en direct.

Framer fait un meilleur travail que la plupart dans ce domaine, supportant des interactions avancées et détaillées. Le reste du peloton est _très_ loin derrière.

### Nos outils devraient supporter le paradigme de mise en page du web

Jusqu'à il y a environ un an, la seule façon de construire des mises en page sur le web était d'utiliser les propriétés CSS `display: table` et `vertical-align`. Maintenant, nous avons Flexbox et bientôt nous aurons CSS grid. Ces trois moteurs de mise en page fonctionnent de manière assez similaire, utilisant le flux du DOM. Presque tous les sites web sont construits en utilisant l'un de ces trois systèmes de mise en page.

Donc, il est logique que nos outils de design supportent le même modèle de mise en page. N'est-ce pas ?

Eh bien, presque tous les outils de design ignorent ces systèmes de mise en page, optant plutôt pour positionner chaque couche de manière absolue dans son artboard. Cela ouvre un fossé entre le fonctionnement du web et le fonctionnement de nos outils de design, introduisant de nombreux problèmes :

* Le design responsif devient très difficile car chaque couche doit être réarrangée manuellement pour chaque point d'arrêt. Alternativement, un système de mise en page basé sur des contraintes peut être introduit, mais cela ajoute de la complexité, rend l'apprentissage plus difficile et empêche finalement les développeurs de transférer la mise en page directement sur le web.
* Puisque chaque couche est en dehors du flux du document, manipuler le contenu devient délicat. Par exemple, si vous voulez ajouter un élément à une liste, vous devez repositionner manuellement les autres éléments de cette liste. Bien sûr, des fonctions de répétition et d'autres fonctionnalités sophistiquées peuvent être introduites pour atténuer la douleur, mais encore une fois, cela introduit une complexité supplémentaire et complique quelque chose que le DOM nous donne gratuitement.
* Le positionnement absolu conduit naturellement à des coordonnées et dimensions en pixels fixes. Cela engendre de l'inflexibilité et, encore une fois, est un énorme écart par rapport au fonctionnement du web. Le web est construit sur des unités fluides comme em, rem, vh, vw et %. Nos outils devraient supporter ces unités par défaut.

Les outils de design n'ont pas besoin de ressembler ou de refléter le web et ses nuances — ils devraient simplement ÊTRE le web.

### Un outil monolithique n'est pas la solution

Un bon design se fait par étapes. Un système de design bien structuré a quelques couches distinctes :

1. **Palette de styles**  
Une collection de couleurs, d'ombres, d'espacements, de rayons de bordure, de polices, de tailles de police, d'animations et d'autres styles qui forment votre identité de marque. Actuellement, la plupart des outils de design ne supportent que les palettes de couleurs. Jusqu'à ce qu'ils supportent les autres propriétés de style, il sera extrêmement laborieux de concevoir de manière systématique.
2. **Actifs**  
Cela inclut des éléments comme les icônes, les illustrations et les images. Il existe d'excellents éditeurs d'images et l'outil vectoriel de Figma est excellent, mais en ce qui concerne le support SVG, nos outils de design laissent beaucoup à désirer.
3. **Bibliothèque de composants**  
Un composant est une collection de styles et d'actifs qui rend les données à un seul élément dans une variété de variations. Les exemples incluent les boutons, les entrées, les badges, etc. Comme je l'ai mentionné, Figma et Sketch ont récemment abstrait ce processus de la principale séquence de dessin — c'est dommage qu'ils ne soient que des images de composants et non des _vrais_ composants.
4. **Modules**  
Un module/composition est une collection de composants qui rend les données à une pièce encapsulée d'UI dans une variété d'états. Les exemples pourraient inclure des barres d'en-tête, des menus à onglets, des formulaires de connexion, des tableaux, etc. Puisque les modules sont simplement des composants complexes, je suppose que Figma et Sketch peuvent également les gérer. Bien qu'il puisse y avoir un certain mérite à séparer les deux.
5. **Écrans**  
Un écran est une collection de modules, de composants et de données pour former une UI complète avec laquelle l'utilisateur peut interagir.

La plupart des outils de design fournissent des fonctionnalités qui supportent chacune de ces étapes de design dans une certaine mesure au moins. Le problème est que toutes les étapes sont confondues. Presque tous les outils de design n'offrent qu'un seul mode — le mode dessin. Vous créez un ensemble d'artboards et commencez simplement à dessiner des images. Ce n'est que très récemment que des outils comme Sketch et Figma ont abstrait les composants/symboles du mode de dessin principal — ce qui est étrange car dans le développement front-end, les composants ont été abstraits depuis de nombreuses années.

Lors de la conception d'une palette de styles, je n'ai pas besoin de voir des artboards ou des outils vectoriels. Je veux voir des outils pour choisir des couleurs harmonieuses. Je veux des préréglages pour des choses comme une échelle d'espacement de 8dp ou une sélection d'échelles de typographie.

La conception d'une icône nécessite un mode de pensée complètement différent de la conception d'un flux utilisateur. Un simple éditeur SVG qui me permettrait de dessiner des rectangles, cercles, lignes et chemins SVG natifs, puis d'exporter du code SVG optimisé serait idéal.

Lors de la conception d'un composant, je ne devrais plus penser aux styles individuels — je devrais simplement choisir des styles dans ma palette de styles prédéfinie. Je ne peux pas simplement commencer à ajuster les styles pour un composant car cela introduirait une incohérence, diluant l'efficacité de mon système de design. Une fois qu'une palette de styles est en place, elle ne devrait être modifiable qu'à la source.

De même, lors de la composition d'un module, je ne devrais être exposé qu'à ma bibliothèque de composants prédéfinie. Il ne devrait y avoir aucune propriété de style dans une barre latérale. Aucun outil vectoriel. Juste une bibliothèque de composants réutilisables que je peux glisser-déposer pour composer des modules.

Il en va de même pour la composition des écrans. À ce stade, nous réutilisons simplement des composants et des modules pour construire une UI. Nous ne pensons pas aux styles ou aux formes ou à d'autres entreprises créatives. Nous nous concentrons principalement sur la conception du contenu et des flux utilisateurs.

Chacune de ces étapes de design pourrait avoir lieu dans des outils entièrement séparés ou simplement dans différents modes au sein du même outil. Je ne pense pas que cela importe beaucoup. Une chose est sûre, cependant, la plupart des outils de design actuels ne reconnaissent même pas le processus.

### Nos outils devraient encourager un bon design

Les designers ont le rare luxe de pouvoir ajouter un nombre infini de styles uniques à un projet sans aucune conséquence notable. Besoin d'une taille de police légèrement plus grande ? Il suffit de l'augmenter. Pas de problème. Besoin d'une couleur légèrement plus vive ? Il suffit de l'ajuster. C'est cool. Vous pourriez même créer plusieurs artboards dans le même projet, chacun utilisant des valeurs légèrement différentes pour des styles similaires et cela passerait probablement inaperçu.

Votre outil de design ne vous dira jamais que vous ne pouvez pas faire quelque chose. Il ne vous tirera jamais vers le haut pour avoir utilisé une couleur hors marque. Il ne vous empêchera jamais d'utiliser une valeur d'espace blanc qui n'appartient pas à votre échelle d'espacement. Il ne vous avertira jamais que 20 % de la population ne peut littéralement pas voir ce texte gris clair que vous venez de concevoir.

Et pourquoi pas... ? Parce que les outils de design s'en fichent.

Les outils de design sont si éperdument épris d'une vision de créativité illimitée qu'ils ont perdu de vue ce que signifie concevoir de manière sensée, concevoir de manière inclusive, concevoir de manière systématique.

En termes simples, les outils de design nous permettent de faire tout ce que nous voulons. Dans une certaine mesure, ce niveau de créativité sans limites est utile, surtout dans les phases d'idéation. En tant que designers UI, cependant, la majorité de notre flux de travail n'appelle pas à beaucoup de créativité. Plutôt, notre flux de travail appelle à la réutilisation, à la répétition, à la familiarité et à la standardisation ; des besoins que nos outils font peu pour satisfaire.

Cette liberté illimitée est en contradiction avec la réalité du développement web. Puisque les développeurs travaillent avec le _produit réel_, ils doivent tous travailler avec le même code. Les développeurs ne peuvent pas simplement ajouter des tailles de police isolées ou des valeurs de couleur aléatoires à la base de code. Premièrement, un linter (un message d'alerte avertissant du code mal écrit) commencerait probablement à crier immédiatement. Si ce n'est pas le cas, alors leur mauvais travail serait probablement intercepté lors d'une revue de code. Si cela parvenait somehow à passer à travers les mailles du filet, un impact de performance notable finirait par donner l'alarme.

L'un des problèmes les plus perturbateurs que je vois dans les équipes produit est le décalage entre les équipes de design et de développement. Les développeurs ont travaillé avec des directives et des contraintes strictes depuis des années. À moins que nos outils de design n'adoptent ces mêmes contraintes, l'écart ne se _réduira jamais_.

### Nous devrions concevoir avec des données en direct

Les données en direct ont été incorporées dans une certaine mesure par de nombreux outils, ce qui est formidable à voir. Adobe XD dispose de certaines fonctionnalités vraiment intéressantes pour générer de fausses données qui ressemblent à des données en direct typiques. [Invision Craft](https://www.invisionapp.com/craft) propose également des fonctionnalités de données en direct intéressantes pour Sketch.

Les données en direct ne devraient pas s'arrêter au texte, cependant. D'autres éléments comme les images et les vidéos peuvent avoir un énorme impact sur l'expérience utilisateur en augmentant considérablement les temps de chargement. Si vous travaillez sur le web, les outils de développement du navigateur vous permettent de limiter la connexion pour ressembler à une variété de vitesses Internet. Ensuite, vous pouvez voir de première main comment un nouveau morceau de contenu pourrait affecter l'expérience utilisateur.

Nos outils de design nous offrent-ils ces luxes ?

En un mot : non.

Plus nous nous rapprochons de la conception du produit réel, plus notre travail de design peut être utile et impactant.

### Le web est ouvert. Nos outils devraient l'être aussi.

L'une des choses vraiment belles à propos du web est son accessibilité ouverte. Un site web peut être consulté dans n'importe quel navigateur web sur à peu près n'importe quel appareil.

Comment cela se compare-t-il avec les outils de design ? Eh bien, il y a quelques jours, mon frère David m'a demandé une revue de design d'une application qu'il construit. Il m'a envoyé un fichier Sketch. Lorsque je l'ai ouvert, cela s'est produit...

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZZ1xV5kFsJ_qBNiHbzEtQ.png)

La plupart des outils de design sont des jardins clos. Si un collègue travaille dans Photoshop, un autre collègue ne peut pas ouvrir ce projet dans Sketch. Il ne suffit même pas que toute votre équipe utilise le même outil — ils doivent également utiliser la même version de cet outil.

Marvel et Figma font du bon travail ici, offrant des plans gratuits et des fonctionnalités de collaboration innovantes.

### Alors, quel est l'avenir des outils de design ?

L'innovation dans les outils de design est extrêmement précieuse et il y en a eu beaucoup récemment. Chez Airbnb design tools, [Jon Gold](https://twitter.com/jongold) et [Benjamin Wilkins](https://twitter.com/thatbenlifetho) ont travaillé sur [React-Sketchapp](https://github.com/airbnb/react-sketchapp) qui prend des composants React et les rend à l'intérieur de Sketch. Jon et Ben ont également travaillé sur un [nouvel outil époustouflant](https://www.youtube.com/watch?v=z5XxgxBz3Fo) qui prend des croquis sur des serviettes et les transforme d'une manière ou d'une autre en composants React.

[Adam Morse](https://twitter.com/mrmrs_), [Brent Jackson](https://twitter.com/jxnblk) et [John Otander](https://twitter.com/4lpine) travaillent sur une suite d'outils chez [Compositor](https://twitter.com/getcompositor) qui [résolvent tous les problèmes](https://twitter.com/getcompositor/status/897946464269291521) de cet article et peut-être du monde.

Je travaille sur [Modulz](https://www.modulz.co), un nouvel outil de design et un système de design open-source qui vise également à résoudre les problèmes que j'ai mentionnés dans cet article. Si vous êtes intéressé, suivez les mises à jour sur [Twitter](https://twitter.com/Modulz).

Bien que l'innovation dans les outils soit importante, le vrai défi est l'éducation. La communauté du design n'est tout simplement pas prête pour un outil de design systématique. De nombreux designers ont peu ou pas d'intérêt à construire des systèmes. Pour certains, le JPG est l'objectif final — les likes sur Dribbble.

Nous devons somehow inspirer une culture de responsabilité. Les développeurs ont une culture de responsabilité depuis des années. Ils ont des outils pour garder leur code sous contrôle. Si un développeur s'écarte à plusieurs reprises de ses directives de code strictes, vous pouvez être sûr que le problème sera abordé.

Pendant ce temps, les designers accumulent fréquemment des montagnes de calques dans un désordre complet avec peu de considération pour le nommage, le regroupement et l'ordre des calques. C'est très beaucoup chacun pour soi. Puisque la sortie (image raster) n'est pas affectée par l'entrée (calques vectoriels), il n'y a pas de réel fardeau placé sur les designers pour être organisés. Les designers excusent souvent ce manque d'organisation en romantisant l'art du design, se peignant comme des magiciens qui doivent être laissés à leurs propres appareils afin de performer.

Nous devons également inspirer une culture d'inclusion. Nous devrions activement décourager les mauvaises pratiques comme les couleurs de texte ultra-légères qui rendent le texte difficile à lire pour de nombreuses personnes, ou les polices de très haute qualité qui rendent les pages web lentes à charger, ou les éléments d'UI sans motif qui rendent les choses difficiles à comprendre pour les personnes daltoniennes. Actuellement, ce type de mauvaise pratique est applaudie au sein de la communauté du design. Si nous voulons accueillir un outil de design intelligent, nous devons inverser cette culture.

Si un outil de design systématique doit gagner nos cœurs, il doit d'abord éduquer.