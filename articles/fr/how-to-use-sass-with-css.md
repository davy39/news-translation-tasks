---
title: Comment utiliser Sass avec CSS
subtitle: ''
author: Adalbert Pungu
co_authors: []
series: null
date: '2022-04-25T22:32:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sass-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/sass-image.png
tags:
- name: CSS
  slug: css
- name: Sass
  slug: sass
- name: Web Design
  slug: web-design
seo_title: Comment utiliser Sass avec CSS
seo_desc: 'Hi there! If you are reading this article, you''re probably trying to understand
  what Sass is and how it works.

  Sass is a CSS preprocessor that helps you manage tasks in large projects where the
  style sheets get larger, you have a number of lines of C...'
---

Bonjour ! Si vous lisez cet article, vous essayez probablement de comprendre ce qu'est Sass et comment il fonctionne.

Sass est un préprocesseur CSS qui vous aide à gérer les tâches dans les grands projets où les feuilles de style deviennent plus grandes, vous avez un nombre important de lignes de code CSS, et il devient difficile de maintenir vos codes CSS.

C'est là que Sass devient utile, car il possède des fonctionnalités qui n'existent pas encore en CSS comme l'imbrication, la création de fonctions avec des mixins, l'héritage, et plus encore. Ces fonctionnalités vous aideront à écrire du code CSS maintenable.

Sass vous permet de réutiliser votre code, de le diviser en fichiers, et il vous aide également à créer des fonctions, des variables, à imbriquer vos sélecteurs CSS, et d'autres raccourcis.

## Comment fonctionne Sass

Le navigateur web ne comprend pas le code Sass, bien qu'il ne comprenne que le code CSS. Cela signifie que vous devez transformer le code Sass en code CSS.

Pour ce faire, le compilateur générera un fichier avec le code CSS. Cette transformation est appelée compilation. Lorsque vous écrivez du code Sass dans un fichier .scss, il est compilé en un fichier CSS régulier que le navigateur utilisera pour l'afficher sur la page web.

## Pourquoi utiliser Sass ?

Il y a de nombreux avantages à utiliser Sass, alors examinons-en quelques-uns maintenant :

Tout d'abord, Sass est facile à comprendre si vous connaissez CSS. Puisqu'il s'agit d'un préprocesseur CSS, sa syntaxe est similaire.

De plus, si vous utilisez Sass, votre code CSS sera compatible avec toutes les versions des navigateurs.

Sass permet également de réutiliser votre code en créant des variables et des fonctions avec des mixins (morceaux de code) qui peuvent être réutilisés encore et encore. Cela vous aide à gagner du temps et vous permet de coder plus rapidement.

En parlant de gagner du temps, Sass réduit la répétition de l'écriture de code CSS. Cela est dû à ses fonctionnalités comme les fonctions, les variables, l'héritage, et ainsi de suite.

Enfin, Sass est compilé en CSS et ajoute tous les préfixes de fournisseurs nécessaires afin que vous n'ayez pas à vous soucier de les écrire manuellement.

## Comment installer et configurer Sass

Dans cet article, je vais vous montrer deux façons d'installer Sass.

### Comment installer Sass avec Node.js

Tout d'abord, nous allons télécharger et installer Node. Ensuite, nous allons utiliser le gestionnaire de paquets JavaScript npm pour installer Sass et le configurer dans votre projet.

Nous allons faire une installation globale, car cela vous évitera de l'installer chaque fois que vous prévoyez de travailler dans vos projets avec Sass.

Voici les étapes à suivre pour installer et configurer Sass dans un projet :

Tout d'abord, ouvrez votre terminal et tapez :

```css
npm install -g scss
```

Encore une fois, il s'agit d'une installation globale. Si vous faites cela, vous évitez de l'installer chaque fois que vous prévoyez de travailler avec Sass dans vos projets.

Ensuite, dans le dossier du projet, créez un fichier Sass dans celui sur lequel vous allez travailler :

```css
style.scss
```

`style` est le nom du fichier et `.scss` est le nom de l'extension Sass.

Ensuite, vous utiliserez la commande suivante pour générer un fichier style.css à partir du fichier SASS :

```css
sass --watch style.scss style.css
```

`style.scss` est le fichier source et `style.css` est le fichier de destination où Sass génère le code CSS.

L'installation et la configuration sont maintenant terminées ! Vous pouvez utiliser Sass dans vos projets.

Mais avant d'aborder comment utiliser Sass, je veux vous montrer une deuxième façon de le faire. Je recommande cette méthode, car c'est la plus simple et la plus facile pour installer et configurer Sass.

### Comment installer Sass en utilisant VS Code

Tout d'abord, téléchargez et installez l'éditeur VS Code de Microsoft si ce n'est pas déjà fait. Ensuite, lancez l'éditeur afin de pouvoir télécharger l'extension Live Sass Compiler.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-37.png align="left")

Et c'est tout ce que vous avez à faire. Une fois l'installation terminée, vous pourrez utiliser Sass dans vos projets. Facile, n'est-ce pas ?

## Comment utiliser Sass dans un projet

Pour comprendre comment utiliser Sass, nous allons travailler sur un exemple de projet où nous allons créer deux grilles. L'idée ici n'est pas d'apprendre tout sur Sass, mais ce que vous voyez est surtout ce que vous devez savoir pour commencer à utiliser Sass.

Voici un aperçu de ce que nous allons créer pour comprendre Sass.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--12--1.png align="left")

Vous vous demandez peut-être pourquoi j'ai pris l'exemple de la grille ? Eh bien, parce que nous utilisons souvent des grilles dans les pages web et elles sont simples à comprendre.

Tout d'abord, vous devez savoir que nous allons faire tout le codage dans le fichier Sass (style.scss) et non dans le fichier style.css. C'est Sass qui générera un fichier CSS pour nous avec le même code.

Pour commencer, créez un dossier avec deux dossiers à l'intérieur, **CSS** et **images**. Ensuite, à l'intérieur du dossier CSS, créez un fichier avec l'extension Sass – dans mon cas, c'est **style.scss**.

Ensuite, ouvrez-le et le fichier sera détecté immédiatement. En dessous de l'éditeur, un bouton apparaîtra nommé **Watch Sass**. Il suffit de cliquer dessus pour dire à Sass de surveiller ce fichier et de commencer à générer (compiler) du code dans le fichier CSS.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/capt.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-38.png align="left")

Une fois que SASS a terminé la compilation, il créera trois fichiers dans le dossier CSS du projet : **style.css**, **style.scss**, et **style.css.map**. Il suit tous les changements et est prêt à générer du code CSS.

Si vous revenez bientôt pour continuer à travailler, tout ce que vous avez à faire est d'ouvrir le fichier qui a l'extension .scss. Ensuite, cliquez sur Watch Sass pour que Sass commence à générer les modifications dans le fichier CSS (sinon rien ne sera généré dans le fichier CSS).

J'espère que tout se passe bien jusqu'à présent. Vous venez de voir comment installer, configurer et commencer à utiliser Sass dans votre projet. Alors maintenant, continuons avec notre exemple des grilles pour comprendre les différentes fonctionnalités que Sass apporte.

## Comment utiliser les variables dans Sass

Avant de voir comment créer des variables Sass, créez un fichier **index.html**, copiez et collez le code ci-dessous dans le fichier :

```html

<!DOCTYPE html>
<html lang="en">
      <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>card with sass</title>
      </head>
      <body>
            
            <div class="card">
                  <img src="https://images.unsplash.com/photo-1524749292158-7540c2494485?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fGRldmVsb3BlcnN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt="">
                  <div class="card_content">
                        <h2 class="card_title">Lorem</h2>
                        <p class="card_description">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum porro dolores sapiente.</p>
                  </div>
            </div>

            <div class="card card_dark">
                  <img src="https://media.istockphoto.com/photos/put-more-in-get-more-out-picture-id1291318636?b=1&k=20&m=1291318636&s=170667a&w=0&h=UvVIk7wwkN3X9OFm8gBlWWviV5vAjfrq2ejYP30JmnA=" alt="">
                  <div class="card_content">
                        <h2 class="card_title">Lorem</h2>
                        <p class="card_description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque amet obcaecati nihil.</p>
                  </div>
            </div>

      </body>
</html>
```

Exécutez le fichier dans votre navigateur pour voir le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--14--1.png align="left")

Sass vous permet de créer des variables, mais je veux vous montrer une différence entre Sass et CSS.

```css
body {
    font-family: 'Poppins', Helvertica, sans-serif;
    background-color: #ab99ca;
    padding: 2rem;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
```

Si vous regardez cet exemple, c'est du CSS. Mais si dans le projet je veux réutiliser une couleur, un padding ou une police, je dois réécrire le même code (en CSS).

Mais avec Sass, je peux créer des variables pour réutiliser ces fonctionnalités. Pour créer une variable en Sass, nous utilisons le signe dollar **$** suivi du nom de la variable et d'un deux-points pour la valeur. Gardez à l'esprit qu'il est préférable de créer un nom qui reflète l'objet que vous allez utiliser.

```css
/* Création et utilisation de variables */
    
$fonts: 'Poppins', Helvetica, sans-serif;
$primary-color: #ab99ca;
$spacing: 2rem;
   
body {
    font-family: $fonts;
    background-color: $primary-color;
    padding: $spacing;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
```

Ajoutez le code ci-dessus dans le fichier style.scss. Puisque nous travaillons avec un fichier Sass et que HTML ne reconnaît pas Sass, pour voir les résultats, nous spécifierons le fichier CSS qui a été généré dans notre fichier **index.html**.

## Comment lier le fichier CSS

Il est vraiment important de lier le fichier CSS à index.html, pour permettre au fichier CSS d'appliquer les styles CSS à l'HTML. Sinon, aucun style ne sera appliqué et vous ne verrez que le code produit par l'HTML.

Nous allons donc lier notre fichier CSS dans le fichier index.html. Dans mon cas :

```html
<link rel="stylesheet" href="css/style.css">
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--13--1.png align="left")

Exécutez le fichier dans votre navigateur pour voir le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--15--1.png align="left")

Nous allons maintenant voir comment organiser le code grâce aux IMPORTS. Le code sera découpé en fichiers tout en continuant à utiliser notre exemple.

Lors de la création d'un fichier, le nom du fichier sera précédé d'un tiret bas (_) pour éviter qu'il soit compilé par Sass.

Créez trois fichiers :

* `_variables.scss` : pour ajouter les variables

* `_mixins.scss` : pour ajouter les fonctions que nous allons réutiliser

* `_card.scss` : pour ajouter les styles de nos cartes

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-40.png align="left")

Copiez et collez les variables que vous avez créées dans le fichier **style.scss** et placez-les dans le fichier `_variables.scss` :

```css
    $fonts: 'Poppins', Helvetica, sans-serif;
    $primary-color: #ab99ca;
    $spacing: 2rem;
    $dark-grey: #999;
```

Pour le fichier `_mixins.scss`, c'est ici que nous allons créer les fonctions réutilisables avec des mixins.

Les mixins vous permettent de créer des fonctions réutilisables. Pour déclarer une fonction, vous devez entrer `@mixin nom_fonction { contenu }` ou si votre fonction a un paramètre, vous devez entrer `@mixin nom_fonction($nom_variable) { contenu }`.

Pour utiliser les mixins, vous devez les importer en tapant `@include nomfonction();` ce qui permet de gagner du temps dans un grand projet.

Ajoutez ce code au fichier `_mixins.scss` :

```css

@mixin flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* $radius est le paramètre de la fonction */

@mixin border-radius($radius) {
    -webkit-border-radius: $radius;
    -moz-border-radius: $radius;
    border-radius: $radius;
}
```

Pour le fichier `_card.scss`, ajoutez ce code :

```css
.card {
    background-color: white;
    width: 20rem;
    overflow: hidden;
    margin: 2rem;
    box-shadow: 5px 5px 5px 5px #000;
    @include border-radius(0.5rem); /* utilisation de la fonction mixins */
    
    img {
        height: 15rem;
        background-size: cover;
        background-position: center center;
    }

    .card_content {
        padding: $spacing;
    }

    .card_title {
        margin: 0;
        color: black;
    }

    .card_description {
        margin: 0;
        color: $dark-grey;
    }

    &_dark {

        background-color: black;

        .card_title {
            color: white;
        }
    }

}
```

Dans le code ci-dessus, nous utilisons l'**imbrication** et les **alias**. L'imbrication nous aide à simplifier la façon dont nous écrivons nos styles CSS et nous permet d'imbriquer les sélecteurs CSS.

Pour les alias, vous pouvez utiliser (**&**) ou (**and**) suivi du nom de la classe qui reprendra le code du sélecteur parent.

Pour utiliser un alias, vous devez l'importer en tapant l'alias suivi du nom de la variable (&\_dark).

Si vous essayez d'exécuter le fichier index.html, rien ne changera. Cela ne change pas parce que nous avons créé des fichiers qui ne sont pas liés à index.html et notre fichier style.sass ne génère que le code qu'il contient.

Pour corriger cela, nous allons importer tous les fichiers que nous avons créés dans le fichier style.sass afin que lorsque SASS effectue la surveillance, il génère le code de ces fichiers.

```css
/* importation de fichiers */
@import 'variables';
@import 'mixins';
@import 'card';
```

Pour le fichier style.scss, ajoutez le code ci-dessus. Le fichier style.scss devrait ressembler à ceci :

```css

/* importation de fichiers */

@import 'variables';
@import 'mixins';
@import 'card';

body {
    font-family: $fonts; /* utilisation de la variable */
    background-color: $primary-color;
    padding: $spacing;
    min-height: 100vh;
    @include flex-center(); /* utilisation de la fonction mixins */
}
```

Dans le code précédent, j'ai importé les fichiers (**SASS import**) dans style.css afin qu'ils puissent être suivis et générer du code lorsqu'il y a des changements.

Exécutez le fichier index.html dans votre navigateur pour voir le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--12--1.png align="left")

Si vous obtenez le même résultat que dans la capture ci-dessus, félicitations, vous comprenez maintenant comment fonctionne Sass.

Voici le lien de prévisualisation du projet que nous avons construit : [https://adalbertpungu.github.io/card\_with\_sass/](https://adalbertpungu.github.io/card_with_sass/)

Et voici le lien du dépôt GitHub :

%[https://github.com/AdalbertPungu/card_with_sass] 

## Conclusion

Dans cet article, vous avez appris comment fonctionne Sass en construisant une simple grille de photos. Dans ce petit projet, nous avons couvert de nombreuses fonctionnalités principales de Sass, mais pas toutes. J'espère donc que vous allez commencer à l'utiliser dans vos projets pour en apprendre davantage.

Vous pouvez consulter la documentation si vous souhaitez approfondir : [https://sass-lang.com/documentation](https://sass-lang.com/documentation).

C'est tout pour cet article. Merci d'avoir lu ! Je pense que vous êtes prêt à essayer d'utiliser Sass.

Bon codage.

Suivez-moi sur Twitter : [twitter.com/AdalbertPungu](https://twitter.com/adalbertpungu)