---
title: 'Vous n''avez pas besoin de CSS-in-JS : Pourquoi (et quand) j''utilise des
  feuilles de style à la place'
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-08-13T14:30:00.000Z'
originalURL: https://freecodecamp.org/news/you-dont-need-css-in-js-why-i-use-stylesheets
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/you-dont-need-css-in-js.jpg
tags:
- name: CSS
  slug: css
- name: CSS in JS
  slug: css-in-js
- name: JavaScript
  slug: javascript
- name: Sass
  slug: sass
- name: styled-components
  slug: styled-components
seo_title: 'Vous n''avez pas besoin de CSS-in-JS : Pourquoi (et quand) j''utilise
  des feuilles de style à la place'
seo_desc: 'CSS-in-JS is all the rage. But is it really the best option?

  Solving problems you don’t need to solve

  Don’t get me wrong, CSS-in-JS is a great solution, but it’s for a problem most people
  don’t have. Maintaining your components in a very siloed appro...'
---

Le CSS-in-JS est à la mode. Mais est-ce vraiment la meilleure option ?

## Résoudre des problèmes que vous n'avez pas besoin de résoudre

Ne vous méprenez pas, le CSS-in-JS est une excellente solution, mais il répond à un problème que la plupart des gens n'ont pas. Maintenir vos composants dans une approche très cloisonnée aide absolument pour des choses comme :

* Les effets secondaires non intentionnels des styles en cascade
* Aider les équipes à organiser leurs règles
* Éviter de marcher sur les pieds des autres pendant le développement

Mais ces problèmes ne deviennent vraiment problématiques qu'avec de grandes équipes comptant de nombreux développeurs et une vaste bibliothèque de composants.

## Alors, que voulez-vous que j'utilise ?

Pour commencer avec une vue légèrement plus élevée, vous pouvez prendre l'habitude de quelques idées de base :

* Établir et suivre quelques règles de base pour l'écriture
* Utiliser des outils ou établir des normes pour l'organisation
* Développer avec des méthodologies comme [BEM](http://getbem.com/)

Cela éliminera toutes ces préoccupations sur un projet plus petit (ou grand) et peut même faciliter la vie.

## Ce pour quoi le CSS-in-JS est bon...

### Aider les grandes équipes à préserver leur santé mentale

Une des raisons pour lesquelles cette solution existe est que les très grandes équipes ont du mal à éviter les conflits lorsqu'elles ont une énorme bibliothèque à gérer. Pouvoir avoir votre composant et tout ce qui l'impacte dans une seule zone compartimentée aide les gens à éviter de marcher sur les pieds des autres et potentiellement à déployer des ajustements qui se propagent involontairement dans toute l'application. C'est génial, mais plus probablement qu'autrement, vous êtes 1 parmi quelques-uns (ou seul) à travailler sur une petite application. Si vous et votre équipe ne communiquez pas sur quelques règles et normes de base, je dirais que vous avez des problèmes plus importants.

### Élimine un peu le besoin d'apprendre le CSS (un peu)

Certains développeurs se moquent du CSS en disant que ce n'est pas du vrai code, d'autres ont peur de sa magie (ne le soyez pas, embrassez-la). N'avoir à se soucier que de quelques règles dans un composant aide à mettre l'esprit des gens à l'aise en sachant que ce n'est qu'un peu plus de JS qui change un peu l'apparence.

## Ce que les deux peuvent faire

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1_VRkx9H7RikKZg4pl6EP5rw.png)
_CSS pointant vers CSS_

### Rechargement de module à chaud (HMR)

Bien que certains disent qu'un avantage du CSS-in-JS est le HMR, vous constaterez que cela fonctionne bien avec les feuilles de style. Parfois, cela fonctionne même un peu mieux si vous travaillez sur un composant qui nécessite un rerender, comme ceux avec une requête réseau comme dépendance, où les changements CSS ne forceront pas ce rerender.

### Variables, paramètres globaux

Si quelqu'un fait valoir que le CSS ne peut pas faire cela, c'est parce qu'il n'a pas prêté attention depuis un moment. Non seulement Sass fournit cela, [c'est natif dans les navigateurs modernes](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties).

### Encapsulation

Oui, vous n'avez pas besoin de JS pour faire cela. Ajoutez un nom de classe à l'élément de niveau supérieur du composant ou de la page, imbriquez tous les styles à l'intérieur, et vous avez votre encapsulation.

```css
.page-about {
  .header {
    background-color: red;
  }
}

.navigation {
  .button {
    background-color: blue;
  }
}
```

### Linting

[https://stylelint.io/](https://stylelint.io/)

### Beaucoup plus

Honêtement, il y a probablement beaucoup plus de choses que les deux font de manière similaire et que vous ne réalisez pas.

## Ce que les feuilles de style et SASS font mieux...

### Partage de règles et configuration

SASS vous permet de configurer des variables, des fonctions personnalisées et des mixins qui portent votre développement CSS au niveau supérieur.

En ignorant les mauvais noms de sélecteurs :

```css
// settings.scss

$color-ultraviolet: #5F4B8B;

// colbys-styles.scss

@import "settings";

.colbys-text-color {
  color: $color-ultraviolet
}

.colbys-background-color {
  background-color: $color-ultraviolet
}
```

Bien que la syntaxe et la configuration de cela soient probablement plus faciles que de configurer un tas de configurations d'objets en JS, cela vous permet grandement de fournir des expériences visuelles cohérentes et de DRY votre code.

### Design réactif

L'une des nombreuses choses qui ajoutent au rôle d'un bon ingénieur front-end est de prêter attention à l'apparence du projet sur plusieurs appareils et tailles. Globalement, l'UX est le travail de tout le monde. Développer avec une mentalité réactive dès le départ non seulement rend ce processus plus facile, mais aide également à construire un meilleur produit.

Essayer de rendre vos composants réactifs en JS signifie plus de JavaScript et plus d'écouteurs d'événements. Non seulement cela ajoute de la complexité, mais cela affecte les performances. Nous pouvons faire cela beaucoup plus facilement avec des requêtes média intégrées directement dans le CSS.

```css
.colbys-sidebar {
  width: 100%;
}

// AUCUN ÉCOUTEUR D'ÉVÉNEMENTS

@media (min-width: 1024px) {
  .colbys-sidebar {
    width: 25%;
  }
}
```

Au lieu d'avoir à limiter les écouteurs d'événements, de vous assurer que vos écouteurs d'événements se désinscrivent lors du démontage, et de simplement gérer l'organisation de tout cela "à la manière React", les requêtes média se déclenchent à la demande et basculeront vos styles selon les besoins de manière plus cohérente.

### Moins de complexité de vos composants

Pouvoir se concentrer sur la fonctionnalité et la sortie rendue vous permet d'éviter d'importer des bibliothèques ou des méthodes complexes pour essentiellement intégrer le CSS dans votre JS, sans compter les hacks JS ou deux ou trois que vous utilisez pour le faire fonctionner en premier lieu.

```jsx
// C'est une exagération

const styles = {
  color: blue;
}

if ( whos_favorite === 'Colby' || whos_favorite === 'Lord Commander' ) {
  styles.color = 'ultraviolet';
} else if ( whos_favorite === 'The Gary' ) {
  styles.color = 'red';
} else if ( whos_favorite === 'Mooncake' ) {
  styles.color = 'green';
} else if ( whos_favorite === 'HUE' ) {
  styles.color = 'blue';
} else if ( whos_favorite === 'KVN' ) {
  styles.color = 'yellow';
}

<MyCompnent styles={styles} />
```

### Performance

[Moins de JavaScript est toujours un gain](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4). C'est moins que votre navigateur doit charger, moins que votre navigateur doit compiler, ce qui se traduira finalement par une vitesse de page plus rapide. Lorsque le navigateur charge une page, il essaie d'optimiser le HTML et le CSS autant que possible. Oui, vous chargez probablement plus de CSS dès le départ, mais plus de JS est très coûteux et est également plus susceptible de [forcer un rerender complet](https://developers.google.com/web/fundamentals/performance/rendering/) ;

Beaucoup des petits morceaux de magie que vous faites avec JavaScript peuvent être réalisés avec des méthodes d'animation CSS assez puissantes, il suffit de parcourir un peu Codepen ou de vérifier quelque chose comme [Animista](http://animista.net/).

Je n'ai pas vraiment de chiffres sur cela à part [quelques bonnes notes](https://blog.primehammer.com/the-performance-of-styled-react-components/) et quelques [benchmarks CSS-in-JS](https://github.com/A-gambit/CSS-IN-JS-Benchmarks). _Quelqu'un a-t-il fait le travail de recherche sur cela ?_

## À la fin de la journée, faites ce qui est efficace

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1_rHuLBikidh3kSQ5M4JXjQQ.png)

**Chacun a une préférence personnelle, chacun est productif à sa manière.** Faites ce qui est mieux pour vous, faites ce qui est mieux pour votre équipe, et évitez de traiter ce que disent les autres développeurs comme des droits et des torts dogmatiques.

Si vous êtes un développeur seul sur un projet et que vous voulez pratiquer le CSS-in-JS pour vous y habituer pour quand vous serez dans une grande équipe, allez-y ! Si vous êtes dans une équipe énorme, énorme chez Facebook et que vous voulez utiliser des feuilles de style, eh bien, vous pourriez rencontrer des problèmes si tout le monde ne suit pas les mêmes directives, mais faites ce qui est mieux pour vous et votre équipe.

La seule façon de le découvrir est avec l'expérience et l'expérimentation. Jouez avec les deux solutions et découvrez pourquoi VOUS pensez qu'une est meilleure que l'autre. Vous ne savez jamais où vous vous retrouverez après avoir décroché ce poste chez Google ou dans votre nouvelle startup dans votre garage.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?F5F9 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">F4E9F5F9 Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.colbyfayock.com/2019/07/you-dont-need-css-in-js-why-i-use-stylesheets](https://www.colbyfayock.com/2019/07/you-dont-need-css-in-js-why-i-use-stylesheets)._