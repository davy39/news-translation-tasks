---
title: Apprendre le système de grille Bootstrap 4 en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T21:17:11.000Z'
originalURL: https://freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9nkJt3S1Fe_KMkDtpIhgXw.png
tags:
- name: Bootstrap
  slug: bootstrap
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre le système de grille Bootstrap 4 en 10 minutes
seo_desc: 'By Elena-Cristina Conacel

  The Bootstrap 4 Grid System is used for responsive layouts.

  A responsive layout represents the way elements align in the page on different resolutions.
  It is important you understand how to use the grid before learning about...'
---

Par Elena-Cristina Conacel

Le système de grille Bootstrap 4 est utilisé pour les mises en page responsives.

Une mise en page responsive représente la manière dont les éléments s'alignent dans la page sur différentes résolutions. Il est important de comprendre comment utiliser la grille avant d'apprendre tout autre composant Bootstrap 4, car quel que soit l'élément que vous utilisez, vous devrez le placer quelque part sur l'écran.

Commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/bIvdmOpWL2YSwkrfoTrOUWMPwyhyjhgyDDND)
_Crédit photo à [shot](https://dribbble.com/animade" rel="noopener" target="_blank" title="">Animade </a> pour son <a href="https://dribbble.com/shots/4948320-Computer-Mouse" rel="noopener" target="_blank" title=")._

### Table des matières

* [Conteneurs Bootstrap 4](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#bootstrap-4-containers)
* [Lignes Bootstrap 4](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#bootstrap-4-rows)
* [Colonnes Bootstrap 4](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#bootstrap-4-columns)
* [Lectures complémentaires](https://www.freecodecamp.org/news/learn-the-bootstrap-4-grid-system-in-10-minutes-e83bfae115da/#further-reading)

La grille Bootstrap 4 se compose de conteneurs, de lignes et de colonnes. Nous allons les prendre un par un et les expliquer.

### Conteneurs Bootstrap 4

Un conteneur Bootstrap 4 est un élément avec la classe `.container`. Le conteneur est la racine du système de grille Bootstrap 4 et il est utilisé pour contrôler la largeur de la mise en page.

Le conteneur Bootstrap 4 contient tous les éléments d'une page. Cela signifie que votre page doit avoir la structure suivante : d'abord le corps de la page HTML, à l'intérieur duquel vous devez ajouter le conteneur et tous les autres éléments à l'intérieur du conteneur.

```html
<body>
   <div class="container">
    ...
   </div>
</body>
```

La classe simple `.container` définit la largeur de la mise en page en fonction de la largeur de l'écran. Elle place le contenu au milieu de la page en l'alignant horizontalement. Il y a un espace égal entre le conteneur Bootstrap 4 et les bords gauche et droit de la page.

Le `.container` réduit sa largeur à mesure que la largeur de l'écran diminue et devient plein écran sur mobile. La largeur du conteneur est définie à l'intérieur de la bibliothèque Bootstrap 4 pour chaque taille d'écran. Vous pouvez voir les tailles exactes [ici](https://getbootstrap.com/docs/4.1/layout/grid/#grid-options).

Un conteneur plein écran prend 100% de la taille de l'écran, quelle que soit la largeur de l'écran. Pour l'utiliser, vous devez ajouter la classe `.container-fluid`.

![Image](https://cdn-media-1.freecodecamp.org/images/1rf1sYoCfHD8IlHcFIed9qH5pttf4Bf1KSsw)

```html
<div class="container">
  Bonjour ! Je suis dans un conteneur simple.
</div>

<div class="container-fluid">
  Bonjour ! Je suis dans un conteneur plein écran.
</div>
```

Vous pouvez voir le CodePen [ici](https://codepen.io/cristinaconacel/pen/XBLVre).

Pour voir les différences entre les deux types de conteneurs, vous pouvez ouvrir le pen dans votre console et basculer entre les tailles d'écran.

### Lignes Bootstrap 4

Les lignes Bootstrap 4 sont des tranches horizontales de l'écran. Elles sont utilisées uniquement comme enveloppes pour les colonnes. Pour les utiliser, vous avez besoin de la classe `.row`.

```html
<div class="row">
  ...
</div>
```

Voici les choses les plus importantes à retenir sur les lignes Bootstrap 4 :

* **Elles ne sont utilisées que pour contenir des colonnes.** Si vous placez d'autres éléments à l'intérieur de la ligne avec des colonnes, vous n'obtiendrez pas le résultat attendu.
* **Elles doivent être placées dans des conteneurs.** Si vous ne faites pas cela, vous obtiendrez un défilement horizontal sur votre page. Cela se produit parce que les lignes ont des marges négatives de 15 à gauche et à droite. Le conteneur a des remplissages de 15px, ce qui contrebalance les marges.
* **Les colonnes doivent être des enfants de la ligne.** Sinon, elles ne s'aligneront pas. Les lignes et les colonnes sont créées pour fonctionner ensemble dans cette hiérarchie stricte.

### Colonnes Bootstrap 4

Nous pouvons maintenant passer à la partie intéressante de ce tutoriel, les colonnes Bootstrap 4. Les colonnes sont géniales ! Elles vous aident à diviser l'écran horizontalement.

Si vous placez une seule colonne dans votre ligne, elle occupera toute la largeur. Si vous ajoutez deux colonnes, elles prendront chacune 1/2 de la largeur. Et ainsi de suite pour n'importe quel nombre de colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/aaNpgARcShivW4WorInpghjdLbX7Jiohd2DA)

```html
<div class="container">
  <div class="row">
    <div class="col">
      ...
    </div>
  </div>
  <div class="row">
    <div class="col">
      ...
    </div>
    <div class="col">
       ...
    </div>
  </div>
  <div class="row">
    <div class="col">
      ...
    </div>
    <div class="col">
       ...
    </div>
    <div class="col">
      ...
    </div>
    <div class="col">
       ...
    </div>
    <div class="col">
       ...
    </div>
  </div>
</div>
```

_Vous pouvez voir le code en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/NOLEyy)._

**Note de côté :** Les colonnes ne sont pas colorées. J'ai simplement ajouté des couleurs pour une description visuellement plus convaincante/pour qu'elles soient plus jolies.

### **Définir les tailles des colonnes**

L'utilisation de la classe `.col` définit la largeur de la colonne de manière dynamique. Cela signifie que, selon le nombre de colonnes dans une ligne, la largeur d'une colonne sera la largeur du conteneur divisée par le nombre de colonnes.

Mais il y a une autre façon de définir les colonnes. Vous pouvez utiliser des classes pour les colonnes et définir leur taille.

Par défaut, la grille Bootstrap 4 se compose de 12 colonnes. Vous pouvez sélectionner n'importe quelle taille de 1 à 12 pour votre colonne. Si vous voulez 3 colonnes égales, vous pouvez utiliser `.col-4` pour chacune (car 3*4 colonnes chacune = 12). Ou vous pouvez définir différentes tailles pour elles. Voici quelques exemples :

![Image](https://cdn-media-1.freecodecamp.org/images/3ib3OrRrGbxeQNZengIzNKNf4Pkm3nYuVGW8)

```html
<div class="row">
  <div class="col-6">
    ...
  </div>
  <div class="col-6">
     ...     
  </div>
</div>
<div class="row">
  <div class="col-5">
    ...
  </div>
  <div class="col-7">
     ...     
  </div>
</div>
<div class="row">
  <div class="col-3">
    ...
  </div>
  <div class="col-4">
     ...     
  </div>
</div>
<div class="row">
  <div class="col-6">
    ...
  </div>
  <div class="col-7">
     ...     
  </div>
</div>
```

Vous pouvez voir le code en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/xyaQNw).

Si la somme des colonnes dans votre ligne n'atteint pas 12, elles ne remplissent pas toute la ligne. Si la somme des colonnes dépasse 12, elle passera à la ligne suivante. La première ligne n'affichera que les premiers éléments qui s'additionnent à 12 ou moins.

### Définir les points d'arrêt pour les colonnes

Si vous prenez l'exemple ci-dessus et que vous souhaitez l'afficher sur mobile, vous pourriez rencontrer quelques problèmes. Afficher cinq colonnes sur mobile rendra le contenu illisible.

C'est là qu'intervient l'un des composants les plus puissants de Bootstrap 4. Pour avoir différentes mises en page sur différents écrans, vous n'aurez pas besoin d'écrire des requêtes média, mais vous pourrez utiliser les points d'arrêt des colonnes.

Un point d'arrêt est une variable Bootstrap 4 qui représente une résolution d'écran. Lorsque vous spécifiez un point d'arrêt pour une classe, vous indiquez à la classe d'être active uniquement pour les résolutions qui sont au moins aussi grandes que le nombre que le point d'arrêt contient.

La classe la plus simple que nous allons apprendre est la classe `.col-[breakpoint]`. Lorsque vous utilisez cette classe, vous définissez le comportement des colonnes uniquement lorsqu'elles sont affichées sur des appareils ayant une résolution d'au moins le point d'arrêt défini. Jusqu'au point d'arrêt donné, vos colonnes s'aligneront verticalement par défaut. Et après votre point d'arrêt, elles s'aligneront horizontalement à cause de la classe.

Bootstrap a 4 points d'arrêt que vous pouvez utiliser :

* `.col-sm` pour les grands téléphones mobiles (appareils avec des résolutions ≥ 576px) ;
* `.col-md` pour les tablettes (≥768px) ;
* `.col-lg` pour les ordinateurs portables (≥992px) ;
* `.col-xl` pour les ordinateurs de bureau (≥1200px)

Supposons que vous souhaitez afficher deux colonnes l'une après l'autre verticalement sur les petits écrans et sur la même ligne sur les écrans plus grands. Vous devrez spécifier le point d'arrêt où les colonnes se placent sur la même ligne.

Dans notre exemple, nous utiliserons le point d'arrêt `.col-lg` et verrons comment les colonnes se présentent sur différents écrans. Pour les résolutions inférieures au point d'arrêt donné (<992px), les colonnes seront affichées verticalement. Cela signifie que sur les appareils mobiles et les tablettes, les colonnes ressembleront à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/JZZ4xgPEjOQ09MBX8NoX65F9XLn4esZ2HnCi)
_L'affichage pour les résolutions < 992px (appareils mobiles)._

Et pour les appareils ayant une résolution supérieure ou égale au point d'arrêt (≥992px), les colonnes se placeront sur la même ligne. Cela signifie que sur les ordinateurs portables et les ordinateurs de bureau, vous obtiendrez ce résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/YCvBIbCtFgLI9Ret9gwVbnkNxuu1wk8EjR-l)
_L'affichage pour les résolutions >= 992px (ordinateurs portables et écrans plus grands)._

```html
<div class="row">
 <div class="col-lg">
   ...
 </div>
 <div class="col-lg">
    ...   
 </div>
</div>
```

Vous pouvez voir le code en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/OBoqqz). Si vous ouvrez le Codepen dans une autre fenêtre et voyez la page à différentes résolutions, vous verrez les colonnes changer de position.

Si vous souhaitez que les 2 colonnes se placent sur la même ligne à partir des grands téléphones mobiles, vous utiliseriez `.col-sm`, pour les tablettes `.col-md` et pour les écrans extra larges `.col-xl`.

### **Définir les tailles et les points d'arrêt pour les colonnes**

Vous pouvez combiner les tailles et les points d'arrêt et utiliser une seule classe avec le format `.col-[breakpoint]-[size]`.

Par exemple, si vous voulez trois colonnes de différentes tailles pour s'aligner sur une ligne à partir de la résolution de l'ordinateur portable, vous devez faire ceci :

```html
<div class="row">
  <div class="col-lg-4">
    ...
  </div>
  <div class="col-lg-3">
    ...
  </div>
  <div class="col-lg-5">
    ...     
  </div>
</div>
```

Vous obtiendrez ce résultat sur les résolutions <992px :

![Image](https://cdn-media-1.freecodecamp.org/images/KH7dwBmHGHssTgFII9tlk0IlzJ2lTFjoDuY1)

Et pour les écrans qui sont ≥992px :

![Image](https://cdn-media-1.freecodecamp.org/images/xLOVbs29mzGIiSe9WKNfIUyKwL2fEc6n0pp8)

Encore une fois, vous pouvez voir le code en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/ReYOwZ).

Mais que se passe-t-il si vous voulez afficher une colonne par ligne sur les résolutions mobiles, deux colonnes par ligne sur les tablettes et quatre sur les ordinateurs portables ou les appareils avec des résolutions plus élevées ?

Alors vous ajoutez plusieurs classes pour une seule colonne pour décrire le comportement pour chaque résolution. En utilisant plusieurs classes, vous spécifiez que le contenu prendra six emplacements sur les tablettes et trois sur les ordinateurs portables.

```html
<div class="row">
  <div class="col-sm-6 col-lg-3">
    ...
  </div>
  <div class="col-sm-6 col-lg-3">
    ...
  </div>
  <div class="col-sm-6 col-lg-3">
     ...     
  </div>
  <div class="col-sm-6 col-lg-3">
     ...     
  </div>
</div>
```

Le résultat s'affichera comme ceci sur les tablettes :

![Image](https://cdn-media-1.freecodecamp.org/images/8Ub6sFDws2UJO8qyLNx3zXiWMylQWpIeLPyX)

Et comme ceci sur les ordinateurs portables et les résolutions plus élevées :

![Image](https://cdn-media-1.freecodecamp.org/images/hVaaOjxUkTRDXBpyKNRBIZt6mzerVq-UoFHO)

Cet exemple est également en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/mjZBPO).

En guise d'exercice, vous pouvez essayer de créer des lignes avec un nombre différent de colonnes en fonction de la taille de l'écran et vérifier le comportement dans votre console de navigateur.

### **Décalage des colonnes**

Si vous ne voulez pas que vos colonnes soient côte à côte, vous pouvez utiliser la classe `.offset-[breakpoint]-[size]` avec la classe `.col-[breakpoint]-[size]`.

Utiliser cette classe revient à ajouter une colonne vide avant votre colonne. Voici un exemple simple :

![Image](https://cdn-media-1.freecodecamp.org/images/b7dxvLZ2St8xI37XTc0R8kFvdfae2Zjvqbmf)

```html
<div class="row">
  <div class="col-md-4 offset-md-4">
     ...     
  </div>  
  <div class="col-md-4">
     ...     
  </div>  
</div>
```

Vous pouvez voir le code en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/KGxYaL).

Vous pouvez utiliser la classe sur n'importe quelle colonne de la ligne. Voici quelques exemples supplémentaires :

![Image](https://cdn-media-1.freecodecamp.org/images/tem6Qp-WqVavEKizT-OIshNBMSDDrSVP3wIY)

```html
<div class="row">
  <div class="col-md-4">
     ...     
  </div>  
  <div class="col-md-4 offset-md-4">
     ...     
  </div>  
</div>
<div class="row">
  <div class="col-md-4 offset-md-2">
     ...    
  </div>  
  <div class="col-md-4 offset-md-2">
     ...     
  </div>  
</div>
<div class="row">
  <div class="col-md-6 offset-md-3">
     ...
  </div>   
</div>
```

### **Imbrication des colonnes**

Cela peut sembler une surprise, mais vous pouvez ajouter une ligne à l'intérieur d'une colonne !

La ligne en question (qui aura la largeur de sa colonne parente) sera ensuite divisée en 12 (plus petites) colonnes que vous pouvez référencer via les classes `.col-*`.

Voyons ce qui se passe lorsque nous insérons une nouvelle ligne à l'intérieur d'une colonne :

![Image](https://cdn-media-1.freecodecamp.org/images/SiRLnZuYJJqLeAK2eN42Xhb9dZz9s87wDaN7)

```html
<div class="row">
    <div class="col-md-8">
        ...
        <div class="row">
            <div class="col-md-5">
               ...
            </div>
            <div class="col-md-7">
               ...   
            </div>
        </div>
      </div>     
    </div>
    <div class="col-md-4">
       ...
    </div>
</div>
```

Vous pouvez voir le code en direct sur [CodePen](https://codepen.io/cristinaconacel/pen/OBoGZr).

Sachant cela, vous pouvez aller à plusieurs niveaux de profondeur pour organiser vos informations. Les colonnes vous fourniront un moyen simple de gérer votre espace.

Cela conclut les connaissances de base concernant le système de grille responsive Bootstrap 4. Si vous avez des questions, n'hésitez pas à me le faire savoir dans les commentaires, je serai ravie d'y répondre.

### Lectures complémentaires

Si vous avez plus de temps, voici quelques ressources utiles :

* [Documentation officielle de la grille](https://getbootstrap.com/docs/4.1/layout/grid/) de GetBootstrap
* [Tutoriel vidéo](https://scrimba.com/p/pD5KUE/cdm3asD) de Scrimba

Cet article a été initialement publié sur le [Blog BootstrapBay](https://bootstrapbay.com/blog/day-2-bootstrap-4-grid-system-tutorial-examples/). Il fait partie d'une série plus large de tutoriels Bootstrap 4 intitulée [14 Days of Bootstrap 4](https://bootstrapbay.com/blog/14-days-bootstrap-4/). Si vous souhaitez continuer à apprendre sur les composants Bootstrap 4, ces articles sont un bon point de départ.

Et si vous souhaitez démarrer rapidement votre développement avec un modèle Bootstrap, vous pouvez consulter notre [marketplace](http://bootstrapbay.com).

Mais avant d'approfondir, prenez un moment pour célébrer vos nouvelles compétences acquises !

![Image](https://cdn-media-1.freecodecamp.org/images/gS3FeSJGquHlZEzANXWSsAakOD2FbabpNvD7)
_Crédit photo à [shot](https://dribbble.com/jonasmosesson" rel="noopener" target="_blank" title="">Jonas Mosesson</a> pour son <a href="https://dribbble.com/shots/4198035-Sweet-Berry-Wine" rel="noopener" target="_blank" title=")._