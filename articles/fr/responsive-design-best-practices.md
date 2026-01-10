---
title: Comment créer des sites Web réactifs – Bonnes pratiques pour les développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-30T20:04:07.000Z'
originalURL: https://freecodecamp.org/news/responsive-design-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/responsive-g619d39e59_1280.png
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Comment créer des sites Web réactifs – Bonnes pratiques pour les développeurs
seo_desc: 'By Fakorede Damilola

  The way we interact with the web has changed dramatically, and it will keep changing.

  In the past, most people used desktop computers to access the internet. But today,
  people are using a wide variety of devices, including laptop...'
---

Par Fakorede Damilola

La façon dont nous interagissons avec le web a changé de manière spectaculaire, et cela continuera d'évoluer.

Par le passé, la plupart des gens utilisaient des ordinateurs de bureau pour accéder à Internet. Mais aujourd'hui, les gens utilisent une grande variété d'appareils, y compris des ordinateurs portables, des tablettes et des smartphones. Cela a entraîné une demande croissante pour le design web réactif.

Le design web réactif est une approche de conception qui garantit qu'un site web a une bonne apparence et fonctionne correctement sur tous les appareils. Cela est réalisé en utilisant des mises en page fluides et des requêtes média pour adapter le site web à différentes tailles d'écran.

Il y a de nombreux avantages à utiliser le design web réactif. Tout d'abord, il offre une meilleure expérience utilisateur pour tout le monde. Lorsqu'un site web est réactif, les utilisateurs peuvent y accéder depuis n'importe quel appareil sans avoir à zoomer ou à faire défiler horizontalement. Cela rend la lecture du contenu et la navigation sur le site web plus faciles.

Les jours où vous construisiez un site web qui avait une bonne apparence sur votre ordinateur portable et où vous ne considériez pas les appareils des autres utilisateurs sont révolus.

Ainsi, vous pouvez dire que le design web réactif est l'approche qui suggère que la conception et le développement doivent répondre au comportement et à l'environnement de l'utilisateur en fonction de la taille de l'écran, de la plateforme et de l'orientation.

Dans ce tutoriel, je vais expliquer certains des détails les plus vitaux que vous devez garder à l'esprit lorsque vous construisez votre site web réactif.

## 5 Principes à appliquer lors de la création de sites Web réactifs

Il y a un certain nombre de principes que vous devez considérer lors de la création de votre prochain site web afin de le rendre réactif. Et voici cinq d'entre eux que je pense être particulièrement importants.

Je ne vais pas entrer dans les détails de chacun de ces principes. Cela ressemble plus à un aperçu à garder à l'esprit lorsque vous construisez.

### Utiliser les requêtes média

L'une des façons les plus fondamentales de créer un site web réactif est d'utiliser les **requêtes média**. Les requêtes média vous aident à définir différents points d'arrêt pour votre site web.

Un point d'arrêt dans un design réactif est le « point » auquel le contenu et le design d'un site web s'adapteront d'une certaine manière pour offrir la meilleure expérience utilisateur possible. Ces points d'arrêt vous aident à spécifier différentes propriétés CSS à utiliser en fonction de la taille de l'écran de l'utilisateur.

Des exemples courants de points d'arrêt incluent 480px, 768px, 1024px et 1280px.
Mais vous ne pouvez pas définir de points d'arrêt pour tous les différents écrans. Ainsi, les développeurs travaillent en définissant deux (mobile-desktop) à trois (mobile-tablette-desktop) points d'arrêt différents. Ensuite, avec d'autres propriétés dont nous parlerons ci-dessous, vous pouvez définir vos divers styles pour chaque point d'arrêt.

Voici un exemple typique de la manière dont vous pouvez utiliser une requête média lors de la création d'un site web. Je suppose que vous souhaitez créer une **mise en page principale** et une **mise en page latérale**.

![MacBook-Air---1](https://www.freecodecamp.org/news/content/images/2023/05/MacBook-Air---1.png)

Le code devrait ressembler à ceci :

```html
     .wrapper{
            width:100%;
            display:flex;
        }
        .main {
            width:80%;
            height:100px;
            background:blue;
        	display:flex;
            justify-content: center;
            align-items: center;
           
        }
        .aside{
            height:100px;
            background:red;
            width:20%;
        	display:flex;
            justify-content: center;
            align-items: center;
        }
    </style>
<body>
    <div class="wrapper">
       <main class="main">
        <h1>MAIN</h1>
    </main> 
    <aside class="aside">
       <h1>ASIDE</h1> 
    </aside>
    </div>
    
    
</body>
```

Mais vous devez considérer le fait que certains utilisateurs pourraient essayer de consulter le site web sur un smartphone, qui a un écran beaucoup plus petit que votre système de bureau.

Pour que cela ait une bonne apparence même sur les appareils avec des écrans plus petits, vous pouvez utiliser des requêtes média pour soit supprimer complètement la barre latérale, soit la placer sous la zone de contenu principale.

Cela dépend de vous et de ce que vous pensez que vos utilisateurs pourraient vouloir voir ou du type d'informations sur la barre latérale. Cela est juste pour vous aider à réfléchir aux options – rappelez-vous que vous êtes un résolveur de problèmes et qu'il y a rarement une seule façon de résoudre un problème. Choisissez donc ce qui fonctionne le mieux pour vous.

Pour l'écran plus petit, dans cet exemple, nous placerons la barre latérale sous la zone principale avec une requête média.

Lors de la création d'un site web, il y a une question que vous devriez poser avant de commencer à coder. **Construisez-vous pour le mobile d'abord ou pour le bureau ?** Cette question est assez importante car elle déterminera la manière dont vous structurez votre CSS.

Personnellement, je préfère commencer par le mobile, simplement parce que je sais que la plupart des gens consulteront mon site web sur des smartphones, donc je veux perfectionner cela en premier. Je réalise que ce débat dure depuis un certain temps, mais cela dépend de vous et des besoins de votre site.

En utilisant les requêtes média, nous ferions ceci pour changer la mise en page du code afin qu'elle ait une bonne apparence à la fois sur les smartphones et les ordinateurs de bureau :

```html
 <style>
       
    .wrapper > div {
        display:flex;
            justify-content: center;
            align-items: center;
    } 
        

        .main {
            width:100%;
            height:100px;
            background:blue;
           
        }
        .aside{
            height:100px;
            background:red;
            width:100%;
        }
        @media (min-width:600px) {
                   .wrapper{
            width:100%;
            display:flex;
                   }
                   .main {
            width:80%;
           
        }
        .aside{
            width:20%;
        }
        }
    </style>
<body>
    <div class="wrapper">
       <div class="main">
        <h1>MAIN</h1>
    </div> 
    <div class="aside">
       <h1>ASIDE</h1> 
    </div>
    </div>
    
    
</body>
```

Il y a quelques points à noter ici (mais encore une fois, cela n'est pas destiné à être un tutoriel approfondi sur les requêtes média, donc nous n'entrerons pas dans trop de détails).

Lorsque vous travaillez avec des requêtes média, vous pouvez définir **min-width** ou **max-width**.

Le code écrit à l'intérieur du conteneur de min-width est celui que nous voulons appliquer pour cette largeur et au-dessus – dans ce cas, pour le **wrapper**, vous avez appliqué le display flex uniquement lorsque la largeur de l'écran de l'utilisateur est **600px ou plus**.

D'autres styles comme la **largeur principale** et la **largeur latérale** ont également leurs tailles individuelles ajustées lorsque l'écran atteint une taille de 600px et plus. C'est-à-dire que les styles que vous avez définis en dehors de cette requête média continueront à fonctionner jusqu'à ce qu'ils voient un écran de 600px et plus.

À 600px, il remplace ces styles, ce qu'il fait dans le bloc de requête média, puis apporte les modifications nécessaires.

Vous pouvez en apprendre davantage sur les requêtes média et pratiquer vos compétences en construisant des projets [dans ce tutoriel](https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/).

### Utiliser des mises en page flexibles

La mise en page est l'une des parties les plus fondamentales d'un site web. C'est la structure de votre site web, et vous pouvez disposer les choses de différentes manières, selon vos besoins.

Puisque c'est l'une des parties les plus cruciales de votre site web, vous voulez créer votre mise en page de manière à ce qu'elle ne soit pas encombrée et ne paraisse pas désordonnée pour les principales tailles d'écran comme le mobile, la tablette et le bureau.

En utilisant des propriétés CSS comme Flexbox, Grid, et ainsi de suite, vous pouvez facilement y parvenir.

**CSS Grid** : CSS Grid est un système de mise en page bidimensionnel pour créer des designs web réactifs.

Il vous permet de définir des lignes et des colonnes dans une grille, puis de placer et d'aligner le contenu dans ces cellules de grille.

Grid est généralement utilisé pour des mises en page plus complexes, telles que celles avec plusieurs lignes et colonnes. Il vous donne un contrôle précis sur la manière dont le contenu est placé et espacé dans les cellules de grille, et peut même être utilisé pour du contenu superposé.

Avec la mise en page de grille, vous pouvez facilement réorganiser votre site web lorsqu'il est utilisé avec des requêtes média.

**Flexbox** : CSS Flexbox est un système de mise en page unidimensionnel pour créer des designs web flexibles et réactifs.

Il vous permet de définir un conteneur flexible puis d'aligner et de distribuer les éléments dans ce conteneur le long d'un seul axe (soit horizontalement, soit verticalement).

Flexbox est mieux utilisé pour des mises en page plus simples où les éléments doivent être disposés le long d'un seul axe. Il vous permet de contrôler facilement l'espacement et l'alignement de ces éléments, et peut être utilisé pour des mises en page horizontales et verticales.

Vous pouvez en apprendre davantage sur CSS Flexbox [dans ce cours accéléré](https://www.freecodecamp.org/news/learn-css-flexbox/). Et [voici un manuel](https://www.freecodecamp.org/news/complete-guide-to-css-grid/) pour vous lancer avec Grid.

Ensuite, si vous souhaitez mettre en pratique vos compétences en Flexbox et Grid, consultez [ce guide basé sur des projets](https://www.freecodecamp.org/news/css-flexbox-and-grid-tutorial/).

### Utiliser des unités flexibles

Un autre concept fondamental dans le développement web est celui des unités. Selon le type d'unité que vous utilisez, cela peut rendre votre site web ordonné ou désordonné.

Il existe différentes unités que vous pouvez utiliser pour définir, par exemple, la taille d'une boîte ou d'un cercle. Et bien qu'il existe une large gamme d'unités parmi lesquelles choisir (comme rem, cm, px, inches, et plus), elles peuvent être classées en deux types :

* Unités relatives : Ce sont les unités dont la valeur change en fonction de la taille de l'écran. Ce type d'unité n'a pas de dimension fixe, mais peut facilement s'étendre ou se contracter en fonction de la taille de l'appareil. Les exemples incluent le pourcentage, rem (taille de la police de l'élément racine) ou em.

* Unités absolues : Ce sont des unités dont les valeurs restent les mêmes quelle que soit la taille de l'écran. Peu importe la taille de l'écran, l'espace occupé restera toujours le même.

Choisir des unités qui s'étendent ou se redimensionnent automatiquement en fonction de la taille de l'écran ou du contenu qu'elles transportent devrait être votre choix par défaut (sauf lorsque cela est absolument nécessaire, et dans ce cas, vous pouvez opter pour des unités absolues).

Un exemple typique est l'utilisation d'une **valeur en pourcentage** lorsque vous voulez qu'une div (boîte) s'étende toujours sur tout l'écran. Ou vous pouvez utiliser une **valeur en px** lorsque vous voulez qu'elle reste de la même taille quelle que soit la taille de l'écran.

Les unités plus récentes et plus faciles à utiliser incluent rem et em. Voici un exemple de ce qu'il ne faut pas faire en premier :

```html
  <style>
        .main {
            width:500px;
            height: 500px;
            background-color: red;
        }
    </style>
 <div class="main">
        <h1>MAIN</h1>
    </div>
```

Le code ci-dessus est une boîte avec du texte à l'intérieur. Avoir une configuration comme celle-ci aura une bonne apparence sur votre grand écran, mais lorsque vous la comparerez avec ce que vous voyez sur le smartphone, il y aura un débordement horizontal. Et en tant que développeur web, vous ne voulez pas cela (sauf lorsque cela est absolument nécessaire).

Créer quelque chose de mieux pourrait ressembler à ceci :

```html
<style>
        .main {
            width:50%;
           height:100px;
            background-color: red;
        }
    </style>
       <div class="main">
        <h1>MAIN</h1>
    </div>
    
```

Comme vous pouvez le voir dans le code ci-dessus, nous avons défini la div avec la classe main, avec une largeur relative. C'est-à-dire, selon la taille de votre écran, la boîte ici occupera 50 % de la taille totale de votre écran. C'est vraiment bien car maintenant vous n'avez pas à vous soucier de la taille de l'écran de l'utilisateur car, quelle que soit la taille, la boîte sera toujours la moitié de l'écran.

### La propriété de position CSS

Vous pouvez également utiliser les différentes propriétés de positionnement en CSS pour vous aider à créer des sites web réactifs. Certains exemples incluent relative, absolute, static, sticky et fixed.

La propriété de position en CSS vous aide à déplacer facilement différents éléments de leur flux normal, en fonction de la propriété que vous définissez.

Ces éléments sont ensuite positionnés en utilisant les propriétés top, bottom, left et right. Mais ces propriétés ne fonctionneront pas à moins que la propriété de position ne soit définie en premier. Elles fonctionnent également différemment en fonction de la valeur de position.

* Static : La position static est la position par défaut de tout élément sur le navigateur, donc les propriétés top, left, right et bottom ne fonctionneront pas pour elle. Cette propriété peut être utilisée lorsque vous souhaitez ramener un élément à sa position initiale après l'avoir déplacé avec une autre propriété de positionnement.

```html
<html>
 <style>
   .position{
     background:red;
     padding:5px;
     position:static;
     top:10px;
     left:20px;
   }
   .wrapper{
background:yellow;
     padding:5px;
   }
  </style>
  <body>
   <div class="main">
     It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</div>
    <div class="wrapper">
    <div class="position">
      This is positioned static
    </div>
    </div>
  </body>
</html>
```

Comme vous pouvez le voir ci-dessus, nous avons ajouté la position static avec d'autres propriétés et rien ne s'est passé. Ce n'est pas parce que le code ne fonctionne pas – c'est simplement le comportement de la position static. Ajouter ou supprimer la position static ne fait rien au code, c'est là qu'elle devrait être.

![Screenshot--1799-](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot--1799-.png)

* Relative : La propriété de position relative positionne un élément par rapport à l'endroit où se trouvait la position initiale de cet élément. Le code suivant expliquera cela mieux :

```html
<html>
 <style>
   .position{
     background:red;
     padding:5px;
     position:relative;
     top:10px;
     left:20px;
   }
   .wrapper{
background:yellow;
     padding:5px;
   }
  </style>
  <body>
   <div class="main">
      It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</div>
    <div class="wrapper">
    <div class="position">
      This is positioned relative
    </div>
    </div>
  </body>
</html>
```

Comme vous pouvez le voir dans le code ci-dessus, une position relative déplace simplement l'élément autour de sa position réelle en fonction de la valeur que vous définissez. Elle est donc relative à sa position réelle :

![Screenshot--1800-](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot--1800-.png)

* Fixed : Nous utilisons la position fixed pour maintenir un élément à un point particulier de l'écran, indépendamment du contenu de la page. La position fixed sera relative à la taille de l'écran, c'est-à-dire que lorsque vous définissez une valeur top, elle sera calculée à partir du haut de votre écran. Voici un exemple. Je vais réduire le contenu factice que j'utilise.

```html
<html>
 <style>
   .position{
     background:red;
     padding:5px;
     position:fixed;
     top:10px;
     left:20px;
   }
   .wrapper{
background:yellow;
     padding:5px;
   }
  </style>
  <body>
   <div class="main">
     This is a really long text
    </div>
    <div class="wrapper">
      
    <div class="position">
      This is positioned fixed
    </div>
    </div>
  </body>
</html>
 ```
 
 ![Screenshot--1802-](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot--1802-.png)
 
Cet élément avec la position fixed a complètement quitté sa position d'origine. Ensuite, en fonction de la valeur de top et left, il a été aligné à une certaine distance du haut de l'écran. Si le contenu est défilable, l'élément restera toujours là.

* Absolute : La propriété absolute positionne un élément par rapport à un élément parent. Donc, s'il est à l'intérieur d'un autre élément qui a une propriété de position autre que static, il sera positionné par rapport à cet élément. S'il n'y a pas un tel élément, il sera positionné par rapport au haut de l'écran.

```html
<html>
 <style>
   .position{
     background:red;
     padding:5px;
     position:absolute;
     top:7px;
     left:20px;
   }
   .wrapper{
background:yellow;
     position:fixed;
     top:30px;
     padding:30px;
   }
  </style>
  <body>
   <div class="main">
this is dummy content
</div>
    <div class="wrapper">
    <div class="position">
      This is positioned
    </div>
    </div>
  </body>
</html>
```

![Screenshot--1803-](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot--1803-.png)

Comme vous pouvez le voir dans le code et l'image ci-dessus, la position est relative à celle de l'élément parent – dans ce cas, c'est le wrapper fixed.

Vous pouvez en apprendre davantage sur la propriété de position CSS [dans ce tutoriel](https://www.freecodecamp.org/news/css-positioning-and-flexbox-explained/).

### Rendre les images réactives

Les images sont assez spéciales, et c'est pourquoi j'ajoute également une section à leur sujet ici.

Vous pouvez rendre les images réactives en utilisant les diverses méthodes listées ci-dessus – mais en raison de la nature des images, elles sont facilement recadrées ou déformées si vous n'êtes pas prudent.

Voici quelques choses que vous pouvez faire lorsque vous travaillez avec des images si vous voulez qu'elles soient réactives.

**Utiliser des images SVG** : SVG signifie Scalable Vector Graphics. C'est un type de format d'image qui utilise des graphiques vectoriels pour créer des images redimensionnables qui peuvent être redimensionnées sans perte de qualité.

Contrairement aux images raster (par exemple, jpg, png, etc.) qui sont composées de pixels individuels, les images SVG sont définies par des équations mathématiques et peuvent être mises à l'échelle de manière infinie sans perdre de clarté.

Certains développeurs préfèrent utiliser les SVG plutôt que d'autres types d'images parce que :
* **scalabilité** – les SVG sont infiniment scalables, ce qui signifie qu'ils peuvent être utilisés dans une variété de tailles et de résolutions différentes sans perdre de qualité.
* **taille de fichier plus petite** – les images SVG ont généralement une taille de fichier plus petite que d'autres types d'images, comme les JPEGs ou les PNGs.

**Object-fit** : La propriété object-fit est utilisée pour spécifier comment l'image doit être redimensionnée pour s'adapter à son conteneur. Cette propriété indique au contenu de remplir le conteneur de diverses manières, telles que "conserver ce rapport d'aspect" ou "s'étirer et occuper autant d'espace que possible".

## Conclusion

Dans cet article, j'espère vous avoir aidé à apprendre les composants de base dont vous aurez besoin lors de la création de sites web réactifs.

Les sites web réactifs sont nécessaires, et il est essentiel pour chaque développeur web de pouvoir construire confortablement des applications web réactives.

Dans cet article, j'ai parlé des 5 principaux blocs de construction des sites réactifs, qui sont :
* Les requêtes média
* La mise en page flexible
* Les unités flexibles
* Le positionnement des éléments
* Les images

J'espère que vous pourrez commencer à les utiliser dans vos propres projets.