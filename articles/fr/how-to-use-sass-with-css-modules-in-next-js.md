---
title: Comment utiliser Sass avec les modules CSS dans Next.js
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2021-01-07T17:31:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sass-with-css-modules-in-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Article.jpg
tags:
- name: CSS Modules
  slug: css-modules
- name: Next.js
  slug: nextjs
- name: Sass
  slug: sass
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Sass avec les modules CSS dans Next.js
seo_desc: 'Next.js gives us CSS Modules by default, providing benefits like scoped
  styles and focused development in our app. How can we give our Next.js CSS superpowers
  with Sass?


  What are CSS Modules?

  What is Sass?

  What are we going to build?

  Step 0: Creatin...'
---

Next.js nous offre les modules CSS par défaut, fournissant des avantages comme des styles à portée limitée et un développement ciblé dans notre application. Comment pouvons-nous donner des superpouvoirs CSS à notre application Next.js avec Sass ?

* [Qu'est-ce que les modules CSS ?](#heading-quest-ce-que-les-modules-css)
* [Qu'est-ce que Sass ?](#heading-quest-ce-que-sass)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Création d'une nouvelle application Next.js](#heading-etape-0-creation-dune-nouvelle-application-nextjs)
* [Étape 1 : Installation de Sass dans une application Next.js](#heading-etape-1-installation-de-sass-dans-une-application-nextjs)
* [Étape 2 : Importation des fichiers Sass dans une application Next.js](#heading-etape-2-importation-des-fichiers-sass-dans-une-application-nextjs)
* [Étape 3 : Utilisation des variables Sass dans une application Next.js](#heading-etape-3-utilisation-des-variables-sass-dans-une-application-nextjs)
* [Étape 4 : Utilisation des mixins Sass avec des imports globaux dans Next.js](#heading-etape-4-utilisation-des-mixins-sass-avec-des-imports-globaux-dans-nextjs)

%[https://www.youtube.com/watch?v=C1-hmauMht0]

## Qu'est-ce que les modules CSS ?

[CSS Modules](https://github.com/css-modules/css-modules) sont essentiellement des fichiers CSS qui, lorsqu'ils sont importés dans des projets JavaScript, fournissent des styles qui sont limités à cette partie particulière du projet par défaut.

Lors de l'importation de votre module, les classes sont représentées par un objet mappé avec chaque nom de classe, vous permettant d'appliquer cette classe directement à votre projet.

Par exemple, si j'avais un module CSS pour le titre de ma page :

```css
.title {
  color: blueviolet;
}
```

Et que j'importe cela dans mon projet React :

```js
import styles from './my-styles.css'
```

Je peux ensuite appliquer ce titre directement à un élément comme s'il s'agissait d'une chaîne :

```jsx
<h1 className={styles.title}>My Title</h1>
```

En limitant la portée des styles, vous n'avez plus à vous soucier de casser d'autres parties de l'application avec des styles en cascade. Il est également plus facile de gérer de petits morceaux de code qui concernent une partie spécifique de l'application.

## Qu'est-ce que Sass ?

[Sass](https://sass-lang.com/) est une extension du langage CSS qui fournit des fonctionnalités puissantes comme les variables, les fonctions et d'autres opérations qui vous permettent de construire plus facilement des fonctionnalités complexes dans votre projet.

Par exemple, si je voulais stocker ma couleur ci-dessus dans une variable pour pouvoir la changer facilement plus tard, je peux ajouter :

```scss
$color-primary: blueviolet;

.title {
  color: $color-primary;
}
```

Si je voulais changer cette couleur mais seulement à un endroit, je peux utiliser les fonctions de couleur intégrées pour changer la teinte :

```scss
$color-primary: blueviolet;

.title {
  color: $color-primary;
  border-bottom: solid 2px darken($color-primary, 10);
}
```

Un avantage supplémentaire est la possibilité d'imbriquer les styles. Cela permet une organisation plus facile et plus logique de votre CSS.

Par exemple, si je voulais changer seulement un élément `<strong>` imbriqué dans un titre, je peux ajouter :

```
$color-primary: blueviolet;
$color-secondary: cyan;

.title {

  color: $color-primary;
  border-bottom: solid 2px darken($color-primary, 10);

  strong {
    color: $color-secondary;
  }

}
```

## Que allons-nous construire ?

Nous allons créer une nouvelle application [React](https://reactjs.org/) en utilisant [Next.js](https://nextjs.org/).

Avec notre nouvelle application, nous allons apprendre comment installer et configurer Sass afin de pouvoir tirer parti de ses fonctionnalités dans Next.js.

Une fois Sass configuré, nous allons voir comment utiliser les [variables](https://sass-lang.com/documentation/variables) et les [mixins](https://sass-lang.com/documentation/at-rules/mixin) de Sass pour recréer certains des éléments par défaut de l'interface utilisateur de Next.js.

> Vous voulez sauter le tutoriel et plonger directement dans le code ? Consultez [Next.js Sass Starter sur GitHub](https://github.com/colbyfayock/next-sass-starter) : [_https://github.com/colbyfayock/next-sass-starter_](https://github.com/colbyfayock/next-sass-starter)

## Étape 0 : Création d'une nouvelle application Next.js

Pour commencer avec une nouvelle application Next.js, nous pouvons utiliser [Create Next App](https://nextjs.org/docs/api-reference/create-next-app).

Dans votre terminal, naviguez vers l'endroit où vous voulez créer le nouveau projet et exécutez :

```
yarn create next-app my-next-sass-app
```

_Note : vous pouvez utiliser npm au lieu de yarn pour tous les exemples avec installation et gestion de paquets._

Une fois l'installation terminée, vous pouvez naviguer dans le répertoire et démarrer votre serveur de développement :

```
yarn dev
```

Ce qui devrait démarrer votre nouveau projet Next.js à l'adresse [http://localhost:3000](http://localhost:3000) !

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-app.jpg)
_Nouvelle application Next.js_

Si c'est la première fois que vous créez une nouvelle application Next.js, jetez un coup d'œil ! Elle vient avec une page d'accueil basique ainsi que deux fichiers CSS :

* `/styles/globals.css`
* `/styles/Home.module.css`

Ici, nous allons nous concentrer sur le fichier home. Si vous regardez à l'intérieur de `pages/index.js`, vous verrez que nous importons le fichier home, rendant ces styles disponibles.

Next.js a les modules CSS intégrés par défaut. Cela signifie que lorsque nous importons notre fichier de styles home, les classes CSS sont ajoutées à l'objet styles, et nous appliquons chacun de ces noms de classe aux éléments React à partir de cet objet, comme :

```jsx
<h1 className={styles.title}>
```

Cela signifie que nos styles sont limités à cette seule page.

Pour en savoir plus sur les modules CSS ou le support intégré dans Next.js, vous pouvez consulter les ressources suivantes :

* [https://github.com/css-modules/css-modules](https://github.com/css-modules/css-modules)
* [https://nextjs.org/docs/basic-features/built-in-css-support](https://nextjs.org/docs/basic-features/built-in-css-support)

## Étape 1 : Installation de Sass dans une application Next.js

Bien que Next.js vienne avec un bon support CSS intégré, il ne vient pas avec Sass complètement intégré.

Heureusement, pour faire fonctionner Sass dans notre application Next.js, tout ce que nous avons à faire est d'installer le [package Sass](https://www.npmjs.com/package/sass) depuis npm, ce qui permettra à Next.js d'inclure ces fichiers dans son pipeline.

Pour installer Sass, exécutez la commande suivante à l'intérieur de votre projet :

```
yarn add sass
```

Et si nous redémarrons notre serveur de développement et rechargeons la page, nous remarquerons en fait que rien ne s'est passé encore, ce qui est une bonne chose !

Mais ensuite, nous allons apprendre comment tirer parti de nos superpouvoirs CSS.

[Suivez avec le commit !](https://github.com/colbyfayock/my-next-sass-app/commit/053b07ccaa1eb30a7d0eff15e2e24470564092f6)

## Étape 2 : Importation des fichiers Sass dans une application Next.js

Maintenant que Sass est installé, nous sommes prêts à l'utiliser.

Pour utiliser des fonctionnalités spécifiques à Sass, nous devons utiliser des fichiers Sass avec l'extension `.sass` ou `.scss`. Pour ce guide, nous allons utiliser la syntaxe SCSS et l'extension `.scss`.

Pour commencer, à l'intérieur de `pages/index.js`, changez l'import de l'objet styles en haut de la page en :

```jsx
import styles from '../styles/Home.module.scss'
```

Et une fois la page rechargée, comme nous nous y attendons probablement, la page est en fait cassée.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-error-import.jpg)
_Next.js a échoué à compiler_

Pour corriger cela, renommez le fichier :

```
/styles/Home.module.css
```

en

```
/styles/Home.module.scss
```

La différence est que nous changeons l'extension de fichier de `.css` à `.scss`.

Une fois la page rechargée, nous verrons que notre site Next.js se charge et est prêt pour l'action !

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-app-title.jpg)
_Nouvelle application Next.js en cours de chargement_

_Note : Nous ne allons pas couvrir le fichier de styles globaux ici - vous pouvez faire la même chose en renommant le fichier de styles globaux et en mettant à jour l'import à l'intérieur de `/pages/_app.js`_

Ensuite, nous allons apprendre comment utiliser les fonctionnalités de Sass pour notre application Next.js.

[Suivez avec le commit !](https://github.com/colbyfayock/my-next-sass-app/commit/cf2a3f56688a728163f2e2d3229565c4efdd6661)

## Étape 3 : Utilisation des variables Sass dans une application Next.js

Maintenant que nous utilisons Sass dans notre projet, nous pouvons commencer à utiliser certaines des fonctionnalités de base comme les variables.

Pour montrer comment cela fonctionne, nous allons mettre à jour le bleu à l'intérieur de notre application en ma couleur préférée, le violet !

En haut de `/styles/Home.module.css`, ajoutez ce qui suit :

```scss
$color-primary: #0070f3;	
```

La couleur `#0070f3` est celle que Next.js utilise par défaut dans l'application.

Ensuite, mettez à jour chaque emplacement qui utilise cette couleur dans notre fichier CSS home avec nos nouvelles variables, par exemple en changeant :

```css
.title a {
  color: #0070f3;
```

en

```scss
.title a {
  color: $color-primary;
```

Si nous actualisons la page, rien ne devrait changer.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-app-1.jpg)
_Application Next.js inchangée_

Mais maintenant, parce que nous utilisons une variable pour définir cette couleur, nous pouvons facilement la changer.

En haut de la page, changez la variable `$color-primary` en violet ou en votre couleur préférée :

```scss
$color-primary: blueviolet;
```

Et lorsque la page se recharge, nous pouvons voir que nos couleurs sont maintenant violettes !

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-app-purple.jpg)
_Application Next.js avec couleur violette_

Les variables ne sont que le début des superpouvoirs que Sass donne à notre CSS, mais nous pouvons voir qu'elles nous permettent de gérer facilement nos couleurs ou d'autres valeurs dans toute notre application.

[Suivez avec le commit !](https://github.com/colbyfayock/my-next-sass-app/commit/0a9e72485957154cfc6a9dbe68f2d9d0d056daed)

## Étape 4 : Utilisation des mixins Sass avec des imports globaux dans Next.js

L'une des nombreuses autres fonctionnalités de Sass est les mixins. Ils nous donnent la possibilité de créer des définitions similaires à des fonctions, nous permettant de configurer des règles que nous pouvons répéter et utiliser dans toute notre application.

Dans notre exemple, nous allons créer un nouveau mixin qui nous permet de créer des styles réactifs en utilisant une requête média dans toute notre application. Bien que nous puissions déjà faire cela avec une requête média seule, l'utilisation d'un mixin nous permet d'utiliser une seule définition, en gardant cela cohérent et en nous permettant de gérer cette définition réactive à partir d'un seul endroit.

Parce que ce mixin est quelque chose que nous voulons utiliser dans toute notre application, nous pouvons également utiliser une autre fonctionnalité de Sass, qui est la possibilité d'importer des fichiers.

Pour commencer, créez un nouveau fichier sous le répertoire `/styles` :

```
/styles/_mixins.scss
```

Nous utilisons un tiret bas devant notre nom de fichier pour indiquer qu'il s'agit d'un partiel.

Ensuite, à l'intérieur de notre fichier `/styles/Home.module.scss`, importons ce nouveau fichier :

```scss
@import "mixins";
```

Une fois la page rechargée, nous remarquerons que rien n'a changé.

Si nous regardons en bas de `Home.module.scss`, nous verrons que nous utilisons une requête média pour rendre la classe `.grid` réactive. Nous allons utiliser cela comme base pour notre mixin.

À l'intérieur de `_mixins.scss`, ajoutez ce qui suit :

```
@mixin desktop() {
  @media (max-width: 600px) {
    @content;
  }
}
```

_Note : bien que nous puissions probablement trouver un meilleur nom pour ce mixin que desktop, nous allons l'utiliser comme base de notre exemple._

Le `@content` signifie que chaque fois que nous utilisons notre mixin desktop, il inclura le contenu imbriqué à cet endroit.

Pour tester cela, dans notre fichier `Home.module.css`, mettons à jour notre extrait `.grid` :

```scss
@include desktop() {
  .grid {
    width: 100%;
    flex-direction: column;
  }
}
```

Si nous ouvrons notre application et réduisons la fenêtre du navigateur, nous pouvons voir que nous avons toujours nos styles réactifs !

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-responsive-styles.jpg)
_Styles réactifs dans Next.js_

Nous pouvons même aller plus loin. Sass permet d'imbriquer les styles. Par exemple, au lieu d'écrire :

```css
.footer {
  // Styles
}

.footer img {
  margin-left: 0.5rem;
}
```

Nous pouvons inclure cette définition `img` directement à l'intérieur de la définition originale `.footer` :

```scss
.footer {

  // Styles

  img {
    margin-left: 0.5rem;
  }
  
}
```

Cette définition img sera compilée en `.footer img`, exactement comme si elle était écrite en CSS standard.

Ainsi, avec cela en tête, nous pouvons utiliser le même concept et déplacer notre mixin desktop dans notre classe `.grid` originale :

```scss
.grid {

  @include desktop() {
    width: 100%;
    flex-direction: column;
  }

}
```

Et si vous remarquez, parce que nous sommes déjà à l'intérieur de la classe `.grid`, nous pouvons la supprimer de l'intérieur du mixin, car elle sera déjà appliquée.

Cela permet une organisation beaucoup plus facile de nos styles réactifs.

Enfin, si nous regardons notre application, nous remarquerons que toujours, rien n'a changé, ce qui signifie que nous utilisons avec succès notre mixin Sass.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nextjs-responsive-styles-1.jpg)
_Aucun changement dans notre application Next.js_

[Suivez avec le commit !](https://github.com/colbyfayock/my-next-sass-app/commit/6781916d8c12225c85dfde96bdab59bfaa14e22b)


## Que pouvons-nous faire d'autre avec Sass et Next.js ?

Nous ne faisons qu'effleurer la surface ici avec Sass. Parce que nos modules CSS ont maintenant le pouvoir de Sass, nous avons une tonne de capacités qui ne viennent pas par défaut avec CSS.

### Fonctions de couleur

Sass a une tonne de fonctions intégrées qui nous permettent de manipuler les couleurs, en mélangeant et en assortissant les teintes beaucoup plus facilement.

Deux que j'utilise souvent sont [darken](https://sass-lang.com/documentation/modules/color#darken) et [lighten](https://sass-lang.com/documentation/modules/color#lighten), qui vous permettent de prendre une couleur et de changer la teinte.

[En savoir plus sur toutes les fonctions de couleur disponibles dans Sass.](https://sass-lang.com/documentation/modules/color)

### Fonctions personnalisées

Bien que les mixins semblent être des fonctions, nous pouvons définir de vraies fonctions dans Sass qui nous permettent d'effectuer des opérations complexes et de produire des valeurs basées sur une entrée.

[En savoir plus sur les fonctions personnalisées dans Sass.](https://sass-lang.com/documentation/values/functions)

### Autres types de valeurs

Bien que la plupart du temps avec CSS nous utilisons des chaînes ou des nombres, nous avons vu qu'une simple extension de cela est la possibilité d'utiliser des variables.

En plus des variables, Sass nous donne plus de types de valeurs comme les [Maps](https://sass-lang.com/documentation/values/maps), qui fonctionnent un peu comme un objet, et les [Lists](https://sass-lang.com/documentation/values/lists), qui sont un peu comme des tableaux.

[En savoir plus sur les types de valeurs dans Sass.](https://sass-lang.com/documentation/values)

### Plus

Il y a une tonne de fonctionnalités disponibles dans Sass et de nombreux articles qui couvrent les fonctionnalités les plus utilisées. Prenez le temps d'explorer la documentation et de découvrir ce qui existe !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">F426 Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">F4FA Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">F4EB Inscrivez-vous à ma newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">F49D Sponsorisez-moi</a>
    </li>
  </ul>
</div>