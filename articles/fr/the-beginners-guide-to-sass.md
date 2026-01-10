---
title: Le guide du débutant pour Sass
subtitle: ''
author: Israel Oyetunji
co_authors: []
series: null
date: '2022-04-04T23:39:31.000Z'
originalURL: https://freecodecamp.org/news/the-beginners-guide-to-sass
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/The-Beginner-s-Guide-to-SASS.png
tags:
- name: CSS
  slug: css
- name: Sass
  slug: sass
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Le guide du débutant pour Sass
seo_desc: 'Have you ever wondered what SASS stands for? Or perhaps you already know
  what it is but haven''t taken the time to study and use it.

  Whether you''re learning about it for the first time, or want to brush up on your
  knowledge of the subject, this is the...'
---

Vous vous êtes déjà demandé ce que signifie SASS ? Ou peut-être savez-vous déjà ce que c'est mais n'avez pas encore pris le temps de l'étudier et de l'utiliser.

Que vous l'appreniez pour la première fois ou que vous souhaitiez rafraîchir vos connaissances sur le sujet, cet article est fait pour vous.

Dans cet article, vous apprendrez les bases de Sass, ce que c'est et comment utiliser les fonctionnalités impressionnantes de Sass pour accélérer le processus d'écriture des styles.

## Prérequis

Cet article suppose que vous avez :

* Une compréhension de base de HTML & CSS
  
* Un éditeur de code (VS Code recommandé). Si vous ne l'avez pas installé, téléchargez-le [ici](http://code.visualstudio.com/).
  
* Et un navigateur (Chrome ou Firefox recommandé)
  

## Qu'est-ce que Sass exactement ?

Sass (Syntactically Awesome Style Sheets) est un préprocesseur CSS qui donne des superpouvoirs à votre CSS.

Admettons-le : écrire du CSS peut parfois être difficile, surtout dans le monde d'aujourd'hui avec des interfaces utilisateur de plus en plus complexes.

Et souvent, vous constaterez que vous vous répétez fréquemment.

Sass vient à la rescousse dans cette situation. Il vous aide à respecter la philosophie DRY (Do Not Repeat Yourself) lors de l'écriture de CSS.

Sass fournit un compilateur qui nous permet d'écrire des feuilles de style dans deux syntaxes différentes, indentée et SCSS. Examinons chacune d'elles maintenant.

### Syntaxe indentée

Il s'agit de l'ancienne syntaxe qui est indentée et qui se débarrasse des accolades et des points-virgules. Elle a une extension de fichier `.sass`.

```plaintext
nav
  ul
    margin: 0
    padding: 0
    list-style: none

  li
    display: inline-block

  a
    display: block
    text-decoration: none
```

### Syntaxe SCSS

Il s'agit de la syntaxe la plus récente et la plus populaire. Elle est essentiellement un sous-ensemble de la syntaxe CSS3. Cela signifie que vous pouvez écrire du CSS régulier avec quelques fonctionnalités supplémentaires.

En raison de ses fonctionnalités avancées, elle est souvent appelée *Sassy CSS*. Elle a une extension de fichier `.scss`.

```scss
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  li {
    display: inline-block;
  }

  a {
    display: block;
    text-decoration: none;
  }
}
```

> Avertissement rapide : Cet article utilise la syntaxe SCSS car elle est plus largement utilisée.

## Comment fonctionne Sass ?

Sass fonctionne de telle manière que lorsque vous écrivez vos styles dans un fichier `.scss`, il est compilé en un fichier CSS régulier. Le code CSS est ensuite chargé dans le navigateur.

C'est pourquoi on l'appelle un préprocesseur.

## Pourquoi devriez-vous utiliser Sass ?

* **Facile à apprendre** : Si vous êtes déjà familiarisé avec CSS, vous serez ravi de savoir que Sass a en fait une syntaxe similaire, et donc vous pouvez commencer à l'utiliser, même après ce tutoriel ;)
  
* **Compatibilité** : Il est compatible avec toutes les versions de CSS. Vous pouvez donc utiliser n'importe quelle bibliothèque CSS disponible.
  
* **Gain de temps** : Il aide à réduire la répétition de CSS, grâce à ses fonctionnalités puissantes.
  
* **Code réutilisable** : Sass permet des variables et des morceaux de code (mixins) qui peuvent être réutilisés encore et encore. Cela vous aide à gagner du temps et vous permet de coder plus rapidement.
  
* **Code organisé** : Sass aide à garder votre code organisé en utilisant des partials.
  
* **Compatibilité multi-navigateurs** : Sass est compilé en CSS et ajoute tous les préfixes de fournisseurs nécessaires, vous n'avez donc pas à vous soucier de les écrire manuellement.
  

## Fonctionnalités de Sass

Voici quelques-unes des fonctionnalités qui font de Sass un véritable CSS avec des superpouvoirs :

### Variables dans Sass

Vous pouvez déclarer des variables dans Sass. C'est l'une des forces de Sass puisque nous pouvons définir des variables pour diverses propriétés et les utiliser dans n'importe quel fichier.

L'avantage ici est que si cette valeur change, vous devez simplement mettre à jour une seule ligne de code.

Cela se fait en nommant une variable avec un symbole dollar `$` puis en la référençant ailleurs dans votre code.

```scss
$primary-color: #24a0ed;

.text {
  color: $primary-color;
}
button {
  color: $primary-color;
  border: 2px solid $primary-color;
}
```

### Imbrication dans Sass

La plupart du temps, lors de l'écriture de CSS, les classes sont souvent dupliquées. Nous pouvons éviter cette duplication en imbriquant les styles à l'intérieur de l'élément parent.

En CSS,

```css
nav {
  height: 10vh;
  width: 100%;
  display: flex;
}

nav ul {
  list-style: none;
  display: flex;
}

nav li {
  margin-right: 2.5rem;
}

nav li a {
  text-decoration: none;
  color: #707070;
}

nav li a:hover {
  color: #069c54;
}
```

Avec Sass, le code ci-dessus peut être écrit comme ceci :

```scss
nav {
  height: 10vh;
  width: 100%;
  display: flex;

  ul {
    list-style: none;
    display: flex;
  }

  li {
    margin-right: 2.5rem;

    a {
      text-decoration: none;
      color: #707070;

      &:hover {
        color: #069c54;
      }
    }
  }
}
```

### Sélecteur Parent

Dans le code Sass ci-dessus, vous avez peut-être remarqué le symbole esperluette `&` utilisé avec la pseudo-classe hover. Cela s'appelle un Sélecteur Parent.

> Le sélecteur parent, `&`, est un sélecteur spécial inventé par Sass qui est utilisé dans les sélecteurs imbriqués pour faire référence au sélecteur externe. Source – [Documentation Sass](https://sass-lang.com/documentation/style-rules/parent-selector)

Ainsi, dans le cas du code ci-dessus, `&` fera référence au parent qui est la balise d'ancrage `a`.

> Vous pouvez consulter mon [article](https://israelmitolu.hashnode.dev/writing-cleaner-css-using-bem-methodology) sur la façon d'implémenter Sass en utilisant la méthodologie BEM.

### Partials dans Sass

C'est l'une des nombreuses fonctionnalités impressionnantes de Sass qui vous donne un avantage.

À mesure que les feuilles de style deviennent volumineuses avec le temps, il devient difficile de les maintenir. C'est pourquoi il est logique de diviser vos feuilles de style en morceaux plus petits. En d'autres termes, les Partials vous aident à organiser et structurer votre code.

Pour déclarer un partial, nous commencerons le nom du fichier par un underscore `_`, et nous l'ajouterons dans un autre fichier Sass en utilisant la directive `@import`.

Par exemple, si nous avons un `_globals.scss`, `_variables.scss`, et `_buttons.scss`, nous pourrions les importer dans le fichier SCSS principal `main.scss`.

```scss
@import "globals";
@import "variables";
@import "buttons";
```

Vous remarquerez que l'underscore et le `.scss` ne sont pas ajoutés. C'est parce que Sass suppose automatiquement que vous faites référence au fichier `.sass` ou `.scss`.

### Mixins dans Sass

Un autre problème majeur avec CSS est que vous utiliserez souvent un groupe similaire de styles. Les Mixins vous permettent d'encapsuler un groupe de styles et d'appliquer ces styles n'importe où dans votre code en utilisant le mot-clé `@include`.

Un exemple de quand vous utiliseriez des mixins est lors de l'utilisation de Flexbox.

```scss
@mixin flex-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
  background: #ccc;
}

.card {
  @include flex-container;
}

.aside {
  @include flex-container;
}
```

### Fonctions et Opérateurs Sass

Sass fournit une suite d'outils pour aider à écrire un code plus programmatique.

Sass offre des fonctions intégrées qui nous permettent de faire des calculs et des opérations qui retournent une valeur spécifique.

Elles vont des calculs de couleur aux opérations mathématiques comme l'obtention de nombres aléatoires et le calcul des tailles, et même des conditionnelles.

Il fournit également un support pour les opérateurs mathématiques comme `+`, `-`, `\`, `*`, `/`, et `%`, que nous pouvons utiliser avec la fonction `calc`.

Voici un exemple utilisant une fonction de conversion de pixels en rem :

```scss
@function pxToRem($pxValue) {
  $remValue: ($pxValue / 16) + rem;
  @return $remValue;
}

div {
  width: pxToRem(480);
}
```

> Cependant, il est important de noter que l'opérateur `/` pour la division est obsolète et sera supprimé dans Dart Sass 2.0.0. Vous pouvez en lire plus dans la [Documentation](https://sass-lang.com/documentation/breaking-changes/slash-div).

Donc, voici comment cela devrait être écrit :

```scss
@use "sass:math";

@function pxToRem($pxValue) {
  @return math.div($pxValue, 16px) * 1rem;
}

div {
  width: pxToRem(480px); // donne 30rem
}
```

Voici un exemple de logique conditionnelle dans un mixin :

```scss
@mixin body-theme($theme) {
  @if $theme == "light" {
    background-color: $light-bg;
  } @else {
    background-color: $dark-bg;
  }
}
```

Sass fournit également les fonctions `lighten` et `darken` pour ajuster une couleur d'un certain pourcentage.

Par exemple :

```scss
$red: #ff0000;

a:visited {
  color: darken($red, 25%);
}
```

## Comment configurer Sass pour le développement local

Super ! Maintenant que nous avons appris les aspects "théoriques" de Sass, plongeons dans le code pour mieux comprendre comment cela fonctionne.

Dans cette section, vous apprendrez comment configurer un environnement de développement local et parcourir une simple page de destination que j'ai préparée.

Consultez la démonstration sur [Codesandbox](https://codesandbox.io/s/currying-river-44d7zr?file=/index.html) et le dépôt de code sur [GitHub](https://github.com/israelmitolu/Getting-Started-with-SASS).

### Façons de compiler Sass

Il existe différentes façons de compiler les fichiers Sass :

* Extension VS Code
  
* Installation en utilisant NPM globalement
  
* Installation en utilisant des applications open source telles que Compass.app, Live Reload et Koala.
  
* Installation en utilisant Homebrew (pour MacOS)
  

Dans ce tutoriel, nous utiliserons l'option d'extension VS Code car c'est la plus facile pour commencer.

### Comment configurer Sass pour VS Code

#### Étape 1 : Installer Live Sass Compiler

Tout d'abord, lancez Visual Studio Code. Une fois chargé, allez dans le panneau latéral de gauche et sélectionnez l'onglet des extensions.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/1.PNG align="left")

*Onglet des extensions dans VS Code*

Dans la barre de recherche, recherchez "Live Sass Compiler" et installez-le. Cette extension nous aide à compiler les fichiers Sass — `.scss` (ou `.sass`) — en fichiers `.css`.

#### Étape 2 : Définir l'emplacement d'enregistrement

Maintenant, changez le chemin du fichier afin que Sass soit compilé dans le dossier `styles`.

Pour ce faire, vous apporterez des modifications au fichier `settings.json`.

Dans VS Code, allez dans Fichier > Préférences > Paramètres. Recherchez maintenant `live sass compile` pour modifier les paramètres globaux.

Cliquez sur `Edit settings.json`.

Maintenant, dans les premières lignes, où vous voyez ce code :

```json
{
  "liveSassCompile.settings.formats": [
    {
      "format": "expanded",
      "extensionName": ".css",
      "savePath": "/"
    }
  ],
```

Changez `"savePath": "/"` en `"savePath": "/styles"`, pour qu'il ressemble maintenant à ceci :

```json
{
  "liveSassCompile.settings.formats":[
    {
      "format": "expanded",
      "extensionName":".css",
      "savePath":"/styles",
    },

    // Vous pouvez également utiliser cette extension minifiée pour la production, car elle réduit la taille du fichier

    {
      "format": "compressed",
      "extensionName":".min.css",
      "savePath":"/styles",
    }
  ],
```

#### Étape 3 : Compiler Sass

Maintenant, après avoir enregistré les paramètres, retournez au fichier Sass et cliquez sur le bouton qui dit "Watch Sass" tout en bas de la fenêtre.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/2.PNG align="left")

*Cliquez sur "Watch Sass"*

Après avoir cliqué sur le bouton, deux fichiers sont créés : `.css` et un `.css.map` dans le dossier `styles`.

Vous ne devez cependant pas les modifier. Parce qu'il vous aide déjà à compiler le Sass en CSS chaque fois que vous enregistrez de nouveaux styles.

#### Étape 4 : Lier le fichier CSS

Ensuite, liez le fichier CSS dans votre `index.html`. Dans notre cas :

```html
    <link rel="stylesheet" href="/styles/main.css" />
```

Maintenant, exécutez le fichier dans votre navigateur. Voici le layout résultant dans CodeSandbox ci-dessous :

%[https://codesandbox.io/embed/currying-river-44d7zr?autoresize=1&fontsize=14&hidenavigation=1&moduleview=1&theme=dark&view=preview] 

## Parcours du code

Voici une explication du code de la section précédente :

* Nous avons un balisage de base dans le fichier `index.html` qui contient un en-tête et une section d'accueil/hero.
  
  * Il contient un lien vers le fichier CSS que l'extension a compilé pour nous.
      
  * Et un peu de JavaScript pour le basculement du menu réactif.
      
* Le fichier `main.scss` est compilé, et le fichier CSS résultant `main.css` est ce qui est importé dans le `index.html` :
  
  ```html
  <link rel="stylesheet" href="/styles/main.css" />
  ```
  
* Le fichier principal Scss `main.scss` importe tous les partials : `_base.scss`, `_components.scss`, `_home.scss`, `_layout.scss`, `_responsive.scss`, `_variables.scss`.
  
  ```scss
  @import "variables";
  @import "base";
  @import "layout";
  @import "components";
  @import "home";
  @import "responsive";
  ```
  
* Le partial base contient les mixins de `flex` et `grid` qui sont inclus aux endroits où nous en avons besoin.
  
## Conclusion

Félicitations ! Si vous êtes arrivé à la fin, cela signifie que vous avez appris comment fonctionne Sass, ses fonctionnalités cool, et espérons-le, vous allez bientôt commencer à l'utiliser.

Si vous souhaitez en savoir plus sur Sass, je vous recommande de consulter le [cours de freeCodeCamp](https://www.youtube.com/watch?v=aoQ6S1a32j8&t=3323s).

Si vous avez trouvé cet article utile (ce dont je suis sûr 😉), partagez-le avec vos amis et votre réseau, et n'hésitez pas à me contacter sur [Twitter](https://twitter.com/israelmitolu) et sur mon [blog](https://israelmitolu.hashnode.dev) où je partage des ressources et des articles pour faire de vous un meilleur développeur.

Merci d'avoir lu, et bon codage !