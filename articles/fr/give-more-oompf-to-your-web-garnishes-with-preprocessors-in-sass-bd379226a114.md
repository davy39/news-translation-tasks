---
title: Sass — un préprocesseur pour vos garnitures web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T23:31:24.000Z'
originalURL: https://freecodecamp.org/news/give-more-oompf-to-your-web-garnishes-with-preprocessors-in-sass-bd379226a114
coverImage: https://cdn-media-1.freecodecamp.org/images/0*BKMwiv00w7wdMbnQ
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Sass
  slug: sass
- name: ux design
  slug: ux-design
- name: Web Development
  slug: web-development
seo_title: Sass — un préprocesseur pour vos garnitures web
seo_desc: 'By Chandrabhan Singh

  Importance of aesthetics, its impact, and tool to achieve it.

  I remember as a child, every time I’d walk up to a bakery, I’d choose the pastries
  with the most beautiful toppings. Only after having the first bite would I know
  if i...'
---

Par Chandrabhan Singh

#### Importance de l'esthétique, son impact et outil pour l'atteindre.

Je me souviens, enfant, chaque fois que je m'approchais d'une boulangerie, je choisissais les pâtisseries avec les plus belles garnitures. Ce n'est qu'après avoir pris la première bouchée que je savais si c'était celle que je désirais.

Un plat bien présenté peut parfois surpasser le goût. La tendance à choisir en fonction de l'apparence a un impact significatif sur nos choix. Cette inclination pour la présentation ne se limite pas à la nourriture. Des vêtements à la mode, un appartement décoré et une voiture bien conçue en sont quelques exemples.

Un chef cuisinier comprend l'importance de la présentation pour un restaurant prospère. L'art de la garniture peut différencier un chef-d'œuvre culinaire d'une assiette de novice. De plus, une présentation créative ajoute du plaisir et du goût, encourageant les clients à revenir fréquemment. Le web n'est pas différent d'un repas gourmet à cet égard. L'impact visuel a joué un rôle crucial dans toutes les applications web réussies.

Vous devez faire des efforts significatifs pour rendre les applications web agréables à l'œil. C'est là que les feuilles de style en cascade (CSS) entrent en jeu.

À mesure que le web évolue, les applications deviennent de plus en plus grandes. Pour répondre à nos besoins, nous avons besoin de plus de fonctionnalités CSS prêtes à l'emploi. Mais CSS a certaines limitations.

Puisque vous lisez cet article, vous avez déjà terminé les garnitures, et maintenant il est temps de goûter le reste du gâteau. Voyons quelles sont les limitations de CSS et comment nous pouvons les surmonter. L'objectif est de porter votre technique de présentation au niveau supérieur.

### Prérequis

Vous devez avoir une bonne compréhension de CSS et des sélecteurs CSS. Vous aurez également besoin de Node.js et de npm installés.

### Limitations de CSS

Identifier les limitations est subjectif, bien que je souhaiterais mentionner quelques-unes.

1. Mécanisme de programmation : Des fonctionnalités comme les variables, les fonctions, les classes et les opérateurs manquent dans CSS3 lui-même.
2. Fichier CSS long : Dans les applications avec une interface utilisateur riche, les feuilles de style peuvent croître rapidement. Les grands fichiers peuvent être un cauchemar pour la maintenance.
3. Opérateurs mathématiques absents : Les opérateurs mathématiques comme `+`, `-`, `*`, `/` peuvent être très pratiques à certains moments.

Pour surmonter ces limitations, nous avons des langages de script de préprocesseur.

### Le préprocesseur

Un préprocesseur est un logiciel qui prend un fichier d'entrée écrit dans un langage de programmation et le traite pour produire un fichier suivant la syntaxe d'un autre langage. Il est utilisé pour étendre la syntaxe d'un langage de programmation existant en y ajoutant de nouvelles fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/CESwXT5CXZaW0zD9UFfMK5-Da4aDae98nXsv)
_illustration : préprocesseur Sass_

Un préprocesseur CSS étend la syntaxe CSS en y ajoutant un mécanisme de programmation. SassScript est un sur-ensemble de CSS. Lorsqu'il est compilé, il crée des blocs CSS valides pour vos applications web.

Il existe plusieurs préprocesseurs CSS disponibles comme Less, Stylus et Sass. Notre focus sera sur Sass (Syntactically-awesome style sheets). Mais le concept est plus ou moins le même pour les autres préprocesseurs.

Nous allons passer par l'installation d'un compilateur Sass pour Node.js, et plus tard nous verrons diverses fonctionnalités de Sass en action. Alors, préparez-vous à garnir vos délicieuses recettes web ?.

### Préparation de Sass

Sass a d'abord été écrit en Ruby puis dans d'autres langages. Vous pouvez choisir parmi de nombreuses implémentations disponibles. Pour cet article, nous allons utiliser un package Node.js — [node-sass](https://www.npmjs.com/package/node-sass). Ce package utilise une implémentation Sass haute performance en C appelée libSassSass.

Commençons par installer node-sass. Ensuite, nous allons configurer une application d'exemple pour voir diverses fonctionnalités de Sass en action. Ouvrez un terminal sur votre machine et exécutez la commande ci-dessous.

```
npm install node-sass -g
```

Ici, nous demandons au gestionnaire de packages node d'installer `node-sass` pour nous. Avec le flag `-g`, nous avons installé le package globalement. Super ! Une fois l'installation terminée, assurez-vous que tout est en place.

```
node-sass -v
```

![Image](https://cdn-media-1.freecodecamp.org/images/HLBJvf-d3thAinPmMy57ICBe-Y7Ajv25U5lf)
_commande pour vérifier la version de node-sass._

D'accord ! Nous avons tous les ingrédients dont nous pourrions avoir besoin. Voyons quelles saveurs Sass nous offre, et ensuite nous commencerons notre voyage pour explorer Sass.

### Différentes saveurs de Sass

Il existe deux façons de créer un fichier Sass. Vous pouvez utiliser l'une ou l'autre de ces deux syntaxes.

1. Style Sass : Cette syntaxe utilise l'indentation pour séparer les blocs de code et les nouvelles lignes.
2. Style SCSS : Cette syntaxe utilise des blocs comme un langage de programmation. Nous utiliserons la syntaxe SCSS dans cet article.

Note : Il est possible de convertir d'une syntaxe à une autre avec une simple commande de conversion Sass. N'hésitez pas à adopter celle que vous préférez.

### Préparation du plat principal

Maintenant que nous sommes prêts à utiliser Sass sur notre machine, nous pouvons commencer à explorer les grandes fonctionnalités qu'il peut nous apporter. Suivez-moi pour configurer une application d'exemple.

Ici, j'utilise [Visual Studio Code](https://code.visualstudio.com/). Vous pouvez utiliser n'importe quel éditeur de code de votre choix. Je l'utilise depuis longtemps et je le recommande. Il dispose de quelques plugins de productivité sympas qui peuvent être d'une grande aide.

![Image](https://cdn-media-1.freecodecamp.org/images/zC4AvUGKCWqbLR5DrEeRNgx7QjCadVK5LASJ)

Jusqu'à présent, nous avons créé un dossier et deux fichiers.

1. index.html : un fichier HTML.
2. style.scss : le fichier script Sass principal (ou racine).

Pour commencer, créons un `div`, un `h1` et deux `button` dans le fichier HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/jTk6IeVPWVD77fz9CvCFXv36nJNtIULc60En)

Parcourons les fonctionnalités les plus utilisées de Sass. En cours de route, nous verrons également les blocs CSS compilés.

### Variables

Les variables vous aident à centraliser les propriétés CSS. Vous pouvez les assigner une fois en haut d'un fichier et les utiliser dans tout le fichier. Ces variables sont comme des espaces réservés pour la valeur d'une propriété CSS. Dans Sass, un nom de variable doit commencer par un signe `$`.

Nous allons créer deux variables : `$h1-color` et `$h1-height`. Ensuite, nous utiliserons ces variables pour assigner les propriétés de couleur et de hauteur à un élément `h1`. Voici le snippet Sass.

```
$h1-color     : blue;
$h1-height    : 50px;
h1{
   color  : $h1-color;
   height : $h1-height;
}
```

Très bien ! Nous avons un fichier HTML et un fichier Sass jusqu'à présent. Et le fichier CSS ? Il n'est pas encore apparu.

Eh bien, nous y sommes presque. Ouvrez votre terminal pour aller dans le dossier que nous avons créé et exécutez la commande suivante :

```
node-sass style.scss style.css
```

Les paramètres pour le compilateur `node-sass` sont les chemins des fichiers d'entrée et de sortie. Maintenant, si vous ouvrez le HTML que nous avons créé pendant la configuration du projet dans un navigateur, vous devriez voir ce qui suit.

![Image](https://cdn-media-1.freecodecamp.org/images/Y3ZYYB1x0X-4unWyqymzGItI3HPBe0rEBw6Y)
_HTML avec CSS appliqué_

Remarquez que le fichier CSS est déjà inclus dans la section `head` du HTML.

### Opérateurs

Les opérateurs mathématiques ont toujours manqué dans CSS. Sass fournit des opérateurs mathématiques de base comme l'addition `+`, la soustraction `-`, la multiplication `*` et la division `/`.

Vous pouvez utiliser des variables et des opérateurs ensemble pour manipuler les propriétés CSS. Prenons un exemple. Nous pouvons utiliser des opérateurs pour calculer le padding d'un élément `h1` en fonction de la largeur de son parent `div`. Nous utiliserons l'opérateur de division `/` pour cet exemple.

```
$h1-color   : blue;
$h1-font    : 50px;
$div-width  : 500px;
div{
   width: $div-width;
}
h1{
   color       :  $h1-color;
   height      :  $h1-font;
   padding     :  $div-width / 10;
}
```

### Mixins

Les mixins sont comme des classes de base abstraites. Les mixins sont pratiques pour regrouper des propriétés liées. Une fois créés, ces mixins peuvent être réutilisés dans le reste des blocs de style. De plus, vous pouvez même passer des variables. Confus ? Prenons un exemple.

Vous avez dû remarquer que créer un style pour border-radius est toujours assez compliqué. Pour la compatibilité entre navigateurs, nous devons utiliser des propriétés spécifiques aux fournisseurs. Cependant, avec les mixins, cela peut être super facile. Voyons cela.

```
@mixin border-radius($radius){
   -webkit-border-radius   : $radius;
   -moz-border-radius      : $radius;
   -ms-border-radius       : $radius;
   border-radius           : $radius;
}
div{
   width    : $div-width;
   border   : 2px solid grey;
   @include border-radius(20px);
}
```

Ici, nous avons utilisé la directive `@mixin` pour définir un mixin nommé `border-radius`. Ce mixin contient toutes les propriétés possibles pour définir le rayon d'une bordure. Nous avons également passé un paramètre à ce mixin. Chaque fois que vous devez définir le rayon d'un élément, incluez ce mixin avec le mot-clé `@include`.

Compilez le script une fois de plus pour générer le CSS. À quoi cela ressemble-t-il maintenant ?

```
//Sortie CSS traitée
div {
   width: 500px;
   border: 2px solid grey;
   -webkit-border-radius: 20px;
   -moz-border-radius: 20px;
   -ms-border-radius: 20px;
   border-radius: 20px; 
}
```

### Imbrication

Les éléments HTML ont une structure logique en forme d'arbre avec des éléments imbriqués. Pour écrire des sélecteurs CSS structurés, CSS devrait également suivre une certaine imbrication logique. Pourtant, CSS ne supporte pas l'imbrication.

Puisque vous avez Sass sur votre machine, écrire des sélecteurs CSS imbriqués est un jeu d'enfant.

```
div{
   >h1{
      color: blue;
      &:hover{
         color: greenyellow;
      }
   }
}
```

Ici, nous avons utilisé deux combinateurs, `&`gt; et &. Le but d'un combinateur est d'expliquer la relation entre les éléments. Notre exemple appliquera la couleur bleue à tous les enfants h1 d'un élément div. Un autre sélecteur est le sélecteur parent &. Utilisez ce sélecteur pour les pseudo-classes comme hover, focus et active.

Compilez une fois de plus pour voir les blocs CSS générés.

```
//Sortie CSS traitée
div h1 {
   color: blue;
}
div h1:hover {
   color: greenyellow;
}
```

### Héritage

Oui — vous pouvez utiliser la fonctionnalité OOP la plus populaire dans Sass également. Accumuler les propriétés de son parent est l'héritage. Mais cela a-t-il un sens dans CSS ? Et pouvons-nous les utiliser ? Nous pouvons ! Croyez-moi, et je suis sûr que vous allez adorer cette fonctionnalité.

Considérons une application où vous avez divers types de boutons. Enregistrer, Annuler et Abandonner pour n'en nommer que quelques-uns. Vous réalisez qu'ils partagent la plupart de leurs caractéristiques. Par exemple, le padding, la taille de la police, la marge. La seule différence est la couleur de fond.

Cela sent-il l'héritage ? Oui — Vous avez deviné juste ! Nous pouvons créer un style parent pour toutes ces propriétés communes et les utiliser dans les blocs enfants.

```css
%common-button{
   padding: 16px 8px;
   border: none;
   font-size: 18px;
}
.save{
   @extend %common-button;
   background-color: blue;
   color: white;
}
.cancel{
   @extend %common-button;
   background-color: goldenrod;
   color: white;
}
```

Ici, les boutons `save` et `cancel` ont hérité de leurs propriétés communes de la classe `common-button`. Pour déclarer un style parent, utilisez le signe `%`. Utilisez la directive `@extend` pour hériter d'un bloc enfant.

### Import

Nous avons vu de nombreuses fonctionnalités incroyables que Sass fournit. Nous avons pu rendre les styles plus lisibles et structurés. Pourtant, cela peut croître et devenir difficile à maintenir.

Sass a également une solution à ce problème : un fichier partiel. Un fichier partiel est un moyen de créer de petits fichiers Sass modulaires. Le fichier Sass racine peut ensuite importer ces fichiers modulaires ensemble. La convention de nommage pour les fichiers partiels est de préfixer le nom du fichier avec un tiret bas `_`.

![Image](https://cdn-media-1.freecodecamp.org/images/1Gmm4N1YrO2DElcL8igxSY7CTEulf0gqKQNQ)

```css
@import '_buttonpartial';
h1{
   color:blue;
}
```

Utilisez la directive `@import` pour inclure un fichier partiel dans le script Sass racine.

### Boucle

L'itération est l'un des mécanismes de programmation les plus fréquemment utilisés. Le script Sass vous permet d'itérer sur des variables. Vous pouvez utiliser diverses directives comme `@for`, `@each` et `@while`.

```css
$totalButton: 2;
@for $i from 1 through $totalButton{
   .button-#{$i} {
      width: 50px * $i;
      height: 120px / $i;
   }
}
```

Le bloc CSS généré aura deux classes avec des styles différents.

```css
//Sortie CSS traitée
.button-1 {
  width: 50px;
  height: 120px; }
.button-2 {
  width: 100px;
  height: 60px; }
```

### Évitez les répétitions — utilisez un robot culinaire

Un robot culinaire est un appareil de cuisine utilisé pour faciliter les tâches répétitives dans la préparation des aliments.

Nous avons utilisé un package Node.js pour compiler les fichiers Sass. Cela peut être très ennuyeux si vous devez compiler chaque fois que vous faites un changement dans le script Sass.

Il existe une manière élégante d'éviter les compilations répétitives : un exécuteur de tâches. Visual Studio Code a un exécuteur de tâches intégré, mais vous pouvez utiliser n'importe quel exécuteur de tâches de votre choix. [Gulp](https://gulpjs.com/) est un autre exécuteur de tâches populaire. Pour compiler le script Sass avec Gulp, vous aurez besoin du [compilateur gulp sass](https://www.npmjs.com/package/gulp-sass) à la place.

**Attention !** Sass est uniquement un outil de développement. Évitez de livrer toute bibliothèque ou fichier associé à Sass. Vous n'en aurez jamais besoin sur un serveur de production.

### Qu'est-ce qui suit

Nous avons appris comment utiliser les préprocesseurs pour créer des blocs CSS efficaces et maintenables. Nous avons vu diverses fonctionnalités de Sass avec des exemples. Pour des connaissances plus approfondies, rendez-vous sur le site officiel [website](https://sass-lang.com/guide).

J'ai également créé un projet [sample](https://github.com/SinghChandrabhan/SassSample). Allez-y, clonez le projet et commencez à jouer.