---
title: Comment utiliser les Mixins dans Sass et passer des arguments – Avec des exemples
  de code
subtitle: ''
author: Nazanin Ashrafi
co_authors: []
series: null
date: '2021-12-02T18:45:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-arguments-to-mixins
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/sass-mixins.jpg
tags:
- name: Sass
  slug: sass
seo_title: Comment utiliser les Mixins dans Sass et passer des arguments – Avec des
  exemples de code
seo_desc: 'Mixins are my favorite thing about Sass. They made my life so much easier,
  so I wanted to show you how they can do the same for you.

  Mixins can be a bit tricky to understand at first, but don''t worry. You''ll get
  the hang of it by practicing and will ...'
---

Les mixins sont ma fonctionnalité préférée de Sass. Ils ont grandement simplifié ma vie, alors je voulais vous montrer comment ils peuvent faire de même pour vous.

Les mixins peuvent sembler un peu délicats à comprendre au premier abord, mais ne vous inquiétez pas. Vous vous y habituerez en pratiquant et vous tomberez amoureux des mixins comme je l'ai fait.

Avant de commencer, laissez-moi vous montrer ce que vous allez lire dans cet article :

* Ce que sont les mixins
  
* Comment écrire des mixins et les inclure dans votre code
  
* Comment et quand passer des arguments
  

Maintenant, passons au vif du sujet, d'accord ?

## Qu'est-ce qu'un Mixin dans Sass ?

Commençons par un rapide aperçu de ce qu'est un mixin :

> "[Les Mixins](https://sass-lang.com/documentation/at-rules/mixin) vous permettent de définir des styles qui peuvent être réutilisés dans toute votre feuille de style. Ils facilitent l'éviter l'utilisation de classes non sémantiques comme `.float-left`, et la distribution de collections de styles dans des bibliothèques." – Documentation Sass

Pour faire simple, un mixin est un bloc de code qui vous permet d'écrire vos styles et de les utiliser dans l'ensemble du projet. Vous pouvez également le considérer comme un composant *réutilisable*. Il vous aide également à écrire un code plus propre sans avoir à vous répéter.

## Comment écrire un Mixin

Voici comment écrire un mixin dans Sass :

```scss
@mixin nom {
    propriétés;
}
```

Et voici comment l'inclure dans votre code :

```scss
div {
    @include nom;
}
```

Voici un exemple d'utilisation d'un mixin dans votre code :

```scss
@mixin cercle {
    width: 200px;
    height: 200px;
    background: red;
    border-radius: 50%;
}

div {
   @include cercle;
}
```

Voyons maintenant ce qui se passe dans le code ci-dessus :

1. Tout d'abord, nous définissons un mixin en utilisant la règle `@mixin`.
    
2. Ensuite, nous lui donnons un nom – choisissez ce que vous pensez convenir à ce pour quoi vous allez l'utiliser.
    
3. Ajoutez vos propriétés CSS.
    
4. En utilisant simplement `@include`, vous le passez au bloc mixin.
    

## Exemple de Mixin

Maintenant, regardons un exemple de mixin en action.

Voici comment créer un cercle rose avec un mixin :

```scss
@mixin cercle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: #ea0185 ;
}
```

```html
.cercle {
    @include cercle;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-18-19-27-24--1-.png align="left")

Maintenant, vous pourriez demander *"pourquoi devrais-je utiliser un mixin pour créer un cercle rose ? Je pourrais simplement donner à mon élément une classe et le styliser."*

Les mixins sont réutilisables, rappelez-vous ? Nous les utilisons lorsque nous savons que nous allons nous répéter beaucoup. Donc, le but est d'*éviter* la répétition et de garder le code propre.

## Passer des Arguments

Maintenant que nous avons vu comment écrire un mixin, passons à la section suivante. Je veux diviser cette section en parties plus petites :

* Qu'est-ce que les arguments de mixin ?
    
* Quand passer des arguments ?
    
* Comment passer des arguments ? + Exemples.
    

### Qu'est-ce que les Arguments de Mixin ?

Un argument est le nom d'une variable qui est séparée par une virgule.

### Quand Devez-Vous Passer des Arguments à un Mixin ?

Je vais commencer cette section avec un exemple :

Et si vous deviez créer deux cercles différents ? Comme un cercle vert et un cercle rose ?

Vous pourriez créer deux mixins séparés, un pour le vert et un pour le rose :

```scss
// un mixin pour le cercle vert
@mixin cercle-vert {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: green;
}

// et un autre mixin pour le cercle rose
@mixin cercle-rose {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: pink;
}
```

Mais ce n'est pas idéal car vous répétez votre code. Et nous devrions respecter le principe DRY (Don't Repeat Yourself), rappelez-vous ?

Et c'est là que les arguments de mixin interviennent.

Dans un mixin régulier (et par régulier, j'entends un mixin où aucun argument n'est passé), vous définissez certains styles. Mais un argument vous permet de définir différents styles en les transformant en variables. C'est comme personnaliser chaque style pour chaque élément. Passons à la section suivante et regardons quelques exemples.

### Comment Passer des Arguments aux Mixins

Nous avons vu ce qu'est un argument et quand l'utiliser. Et maintenant, il est temps de voir comment passer les arguments :

```scss
@mixin nom($argument,$argument) {
    propriété: $argument;
    propriété: $argument;

}
```

Voici un exemple :

```scss
@mixin cercle2 ($largeur,$hauteur,$couleur) {
    width: $largeur;
    height: $hauteur;
    background: $couleur;
}
```

Vous pouvez considérer les arguments comme des variables personnalisables que vous pouvez utiliser dans différentes situations pour créer différentes choses sans vous répéter.

Comme lorsque vous passez `$largeur` à la propriété width, vous pouvez la définir dans différentes situations. Peut-être avez-vous besoin que la largeur soit de 50px à un endroit et de 500px ailleurs.

Cela a-t-il du sens ? Laissez-moi vous l'expliquer avec un autre exemple.

D'accord, revenons à nos cercles.

Je veux faire un grand cercle rouge et un petit cercle vert (deux choses différentes) avec un seul mixin.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-22-21-25-44--1-.png align="left")

Maintenant, quelles propriétés ai-je besoin pour faire un cercle ?

```python
largeur, hauteur et couleur de fond, n'est-ce pas ?
```

Puisque nous construisons des cercles, le border-radius sera de 50% dans les deux situations. Donc je vais le laisser tel quel et ne pas passer d'argument.

Maintenant, nous avons trois propriétés :

1. largeur
    
2. hauteur
    
3. couleur de fond
    

Cela signifie que nous avons besoin de seulement trois arguments :

```scss
@mixin cercle($largeur,$hauteur,$couleur) {
    // Nous passons $largeur à la propriété width
    width: $largeur;
    
    // Nous passons $hauteur à la propriété height
    height: $hauteur;
    
    // Et nous passons $couleur à la propriété background
    background: $couleur;
    
    // pas d'argument pour cette propriété, car elle sera la
    // même dans les deux cercles
    border-radius: 50%;
}
```

Alors maintenant, voyons comment nous pouvons passer des arguments à notre mixin :

#### Pour le grand cercle rouge

```scss
.cercle-rouge {

    // cercle ($largeur,$hauteur,$couleur);
   @include cercle (350px,350px,red);
}
```

#### Pour le petit cercle vert

```scss
.cercle-vert {

     // cercle ($largeur,$hauteur,$couleur);
    @include cercle (200px,200px,green);
}
```

Et voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-22-21-25-44--1--1.png align="left")

Si vous voulez plus d'informations sur le passage d'arguments aux mixins, voici une petite vidéo pour vous aider :

%[https://www.youtube.com/watch?v=0s-xjyXOtP4] 

D'accord, revenons à notre tutoriel. Comme je l'ai dit plus tôt, je n'ai pas passé d'arguments à la propriété border-radius car elle sera toujours de 50% (dans *ce* cas).

Mais si je devais faire un carré et un cercle, alors j'aurais besoin de passer un argument à `border-radius` aussi :

```scss
@mixin cercle($largeur,$hauteur,$couleur,$rayon) {
    width: $largeur;
    height: $hauteur;
    background: $couleur;
    // passé l'argument à border-radius pour avoir le contrôle dessus 
    border-radius: $rayon;
}

.carre {
            // ($largeur,$hauteur,$couleur,$rayon)
    @include cercle (350px,350px,red, 10px);
}

.cercle {
            // ($largeur,$hauteur,$couleur,$rayon)
    @include cercle (200px,200px,green, 50%);
}
```

Maintenant, nous avons un grand carré rouge et un petit cercle vert :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-22-22-17-12--1-.png align="left")

Regardons un autre exemple. Cette fois, essayons d'utiliser un mixin sur du texte.

Voici ce que je veux faire, un texte vert avec un fond noir et un texte rouge avec un fond transparent :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-25-19-26-49--1-.png align="left")

Tout d'abord, j'ai créé deux éléments h2 :

```html
<h2 class="texte1">Texte</h2>
<h2 class="texte2">Texte</h2>
```

Nous avons besoin des propriétés `font-size, color, et background` ici. Maintenant, je devrais passer des arguments en les transformant en variables.

```scss
@mixin texte($taille-police,$couleur,$couleur-fond) {

     // nous passons $taille-police à la propriété font-size
    font-size: $taille-police;
    
    // nous passons $couleur à la propriété color
    color: $couleur;
    
    // nous passons $couleur-fond à la propriété background
    background: $couleur-fond;
}



.texte1 {
          // ($taille-police,$couleur,$couleur-fond)
    @include texte(3rem,green , black)
}

.texte2 {
          // ($taille-police,$couleur,$couleur-fond)
    @include texte(5em,red , transparent)
}
```

Et voilà.

**Conseil rapide :** Rappelez-vous que *l'ordre des arguments compte.*

Cela compte car la seule façon de savoir quelle valeur vous avez l'intention de passer pour chaque paramètre est d'utiliser le bon ordre.

Par exemple, si l'ordre de vos arguments est *$largeur, $hauteur, $couleur*, vous devez les passer dans cet ordre également :

```scss
@mixin cercle($largeur,$hauteur,$couleur) {
    width: $largeur;
    height: $hauteur;
    background: $couleur;
    border-radius: 50%;

}
```

```scss
.cercle-rouge {
             // ($largeur,$hauteur,$couleur)
    @include cercle (350px,350px,red);
}
```

Vous ne pouvez pas passer la couleur en premier suivie de la largeur et de la hauteur :

```python
.cercle-rouge {
    @include cercle (red,350px,350px);
}
```

En ce qui concerne cet ordre incorrect, nous avons passé `$largeur` à la propriété width, donc la première valeur doit être un nombre. Donc, si vous passez `$couleur` en premier, la valeur ne sera pas reconnue. C'est pourquoi nous devons passer les arguments dans l'ordre.

## Voici un rapide récapitulatif de ce dont nous avons parlé dans cet article

* Les mixins sont des blocs de code réutilisables.
    
* Nous les utilisons lorsque nous savons que nous allons répéter des morceaux de code beaucoup.
    
* Voici comment nous écrivons un mixin :
    

```scss
@mixin nom {
    propriétés;
}
```

* Un argument est le nom d'une variable qui est séparée par une virgule.
    
* Les arguments vous permettent de définir différents styles.
    
* L'ordre des arguments compte.
    
* Voici comment nous passons des arguments :
    

```scss
@mixin nom($argument,$argument) {
    propriété: $argument;
    propriété: $argument;

}
```

Et c'est tout pour cet article – j'espère que vous l'avez aimé et que vous l'avez trouvé utile. 😊

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-113.png align="left")

*Vous pouvez également me suivre sur* [***twitter-***](https://twitter.com/nazanin_ashrafi)