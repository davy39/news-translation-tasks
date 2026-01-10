---
title: 'Posez le Javascript : apprenez d''abord le HTML et le CSS'
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-08-28T14:19:24.000Z'
originalURL: https://freecodecamp.org/news/put-down-the-javascript-learn-html-css
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/put-down-the-javascript.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: 'Posez le Javascript : apprenez d''abord le HTML et le CSS'
seo_desc: 'A growing trend in front end development is the idea that you can dive
  right in to Javascript and succeed. Honestly, for better or worse you probably can.
  But you’re just building on top of a fragile foundation that will come back to bite
  you.

  Why do...'
---

Une tendance croissante dans le développement front-end est l'idée que vous pouvez vous lancer directement dans Javascript et réussir. Honnêtement, pour le meilleur ou pour le pire, vous pouvez probablement le faire. Mais vous construisez simplement sur une fondation fragile qui finira par vous causer des problèmes.

### Pourquoi ai-je besoin de HTML ou CSS ?

Les frameworks UI que nous connaissons aujourd'hui comme [React](https://reactjs.org/) et [Vue](https://vuejs.org) se construisent sur les blocs de base d'une page web : HTML et CSS. Bien que ces frameworks UI superchargent ces bases grâce à des outils cool et Javascript, ce que vous construisez est fondamentalement la même chose que le [site web Space Jam](https://www.spacejam.com/archive/spacejam/movie/jam.htm) de 1996.

Mais je comprends, écrire du HTML et du CSS manuellement est dépassé, n'est-ce pas ?

### Comprendre ce que vos outils font

Avoir au moins une compréhension de base de ce qui se passe sous le capot vous aidera énormément lorsque vous développerez et déboguerez vos applications.

Vous avez peut-être rencontré quelques choses étranges dans le navigateur, comme pourquoi le HTML transforme-t-il le code là ? En utilisant l'exemple suivant :

```html
<style>
p {
  color: purple;
}
</style>
<h1>Ma Page Cool</h1>
<p>
  Des trucs cool
  <div>Est-ce toujours cool ?</div>
</p>
```

Lorsque vous chargez cela dans Chrome, vous remarquerez quelques changements...

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Image-on-2019-08-17-at-20-15-44.png)
_Exemple de HTML corrigé par le navigateur_

Pourquoi tout mon paragraphe n'est-il pas cool et violet ?

Eh bien, il s'avère que votre navigateur est utile et corrige automatiquement votre code. Une balise de paragraphe (`<p>`) [ne peut pas contenir un autre élément de niveau bloc](https://www.w3.org/TR/html401/struct/text.html#h-9.3.1), donc Chrome et d'autres navigateurs ajusteront votre HTML à la volée pour le rendre valide. HTML est très indulgent de cette manière ! Mais c'est un bug courant qui déroute les développeurs, nouveaux et anciens, qui ne sont tout simplement pas familiers avec le fonctionnement de HTML.

### Apprenez la magie de CSS

CSS peut faire énormément de choses de nos jours. C'est bien plus que de définir quelques couleurs, mais il vous donne la capacité de fournir des motifs UI cohérents dans toute votre application.

N'ayez pas peur de cela ! Si vous avez commencé avec Javascript, vous pourriez être tenté de tout faire là-bas, mais vous découvrirez rapidement que gérer toute la puissance réelle de CSS dans votre JS est une corvée, et franchement, [inutile sauf si vous êtes Facebook](https://www.colbyfayock.com/2019/07/you-dont-need-css-in-js-why-i-use-stylesheets).

Que pouvez-vous faire ? Construisez [la scène du titre du film Alien](https://www.colbyfayock.com/2019/07/you-dont-need-css-in-js-why-i-use-stylesheets) avec du CSS pur. Attrapez quelques [effets de survol pour vos boutons](https://ianlunn.github.io/Hover/). Ou simplement [animez n'importe quoi](https://daneden.github.io/animate.css/) !

Un de mes préférés est de créer une classe d'animation de chargement de type Facebook qui appliquera un fond de dégradé animé à tout ce à quoi vous l'ajoutez :

```css
.loading {
  background: linear-gradient(90deg, #eff1f1 30%, #f7f8f8 50%, #eff1f1 70%);
  background-size: 400%;
  animation: loading 1.2s ease-in-out infinite;
}

@keyframes loading {
  0% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 50%;
  }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/loading-animation.gif)
_Exemple d'animation de chargement_

Ouvrez [un codepen](https://codepen.io/colbyfayock/pen/aKKoJP) et essayez-le vous-même !

### Rendez vos résultats de recherche pertinents

Les moteurs de recherche font de leur mieux pour déterminer comment le contenu que vous écrivez est pertinent pour les utilisateurs qui le recherchent. Mais la manière dont vous écrivez votre HTML fait une différence pour les aider à déterminer cette valeur. Une erreur courante que je vois est l'utilisation incorrecte des éléments [Heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) ou simplement le fait de ne pas les utiliser du tout.

```html
<h1>Tout</h1>
<h1>Mon</h1>
<h1>Contenu</h1>
<h1>Est</h1>
<h1>Important</h1>
```

Considérez le plan de cet article de blog :

```markdown
- Posez le Javascript - Apprenez le HTML & CSS
  - Pourquoi ai-je besoin de HTML ou CSS ?
  - Comprendre ce que vos outils font
  - Apprenez la magie de CSS
...
```

"Apprenez la magie de CSS" n'est pas le point clé à retenir de la page, donc je ne voudrais pas le mettre en avant comme le plus important. Le titre de l'article, cependant, "Posez le Javascript — Apprenez le HTML & CSS", reflète l'histoire globale, ce qui en fait le plus important, donc je voudrais en faire le #1.

Ainsi, avec mon HTML, je voudrais que cela ressemble à quelque chose comme :

```html
<h1>Posez le Javascript - Apprenez le HTML & CSS</h1>
<h2>Pourquoi ai-je besoin de HTML ou CSS ?</h2>
<h2>Comprendre ce que vos outils font</h2>
<h2>Posez le JS - Apprenez le HTML & CSS</h2>
```

Cela permet à Google, Bing et tous les autres moteurs de recherche de savoir exactement quelle devrait être la partie la plus importante de la page et aide à identifier la hiérarchie générale.

### Favorisez l'accessibilité par un développement inclusif

En ne codant pas de manière responsable, nous excluons automatiquement des personnes de l'accès au site pour lequel nous travaillons si dur. Souvent, ces personnes se soucient de ce qui est construit autant, sinon plus, que vous et moi.

En faisant un peu de travail préparatoire la première fois et en passant une seconde supplémentaire à réfléchir à ce que nous écrivons, nous pouvons être inclusifs envers tous les amis visitant nos sites.

Prenez une simple liste de navigation couramment vue dans la plupart des sites web aujourd'hui. Vous pourriez être tenté d'écrire quelques `div` car ils fonctionnent, n'est-ce pas ?

```html
<div className="nav">
  <div><a href="#">Lien 1</a></div>
  <div><a href="#">Lien 2</a></div>
  <div><a href="#">Lien 3</a></div>
</div>
```

Le problème est qu'ils ne sont pas aussi faciles à détecter pour les lecteurs d'écran. Pour corriger cela, vous pouvez /techniquement/ écrire encore moins de HTML ( `div` compte 3 caractères, `ul` et `li` en comptent 2 ?).

```html
<ul className="nav">
  <li><a href="#">Lien 1</a></li>
  <li><a href="#">Lien 2</a></li>
  <li><a href="#">Lien 3</a></li>
</ul>
```

En allant plus loin, si c'est votre menu de navigation, enveloppez-le dans un [élément de navigation HTML 5](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav) (`<nav>`) et [les utilisateurs pourront maintenant accéder directement au menu](https://www.w3.org/WAI/tutorials/menus/structure/#identify-menus).

Consultez [The A11y Project](https://a11yproject.com) pour plus de bons conseils sur l'accessibilité.

### Simplifiez votre code, adoptez les fonctionnalités natives

Vous seriez surpris de la quantité de fonctionnalités [existantes nativement dans les navigateurs modernes](https://dev.to/ananyaneogi/html-can-do-that-c0n), avec plus de support de navigateurs que vous n'en avez probablement besoin (désolé pour ceux d'entre vous qui supportent encore IE9).

Avec un peu de HTML de base, vous pouvez construire une entrée de texte qui a un texte de type recherche, avec autocomplétion, dans une liste déroulante :

```
<label>Ma Couleur Préférée</label>
<input type="text" name="color" list="colors">
<datalist id="colors">
  <option value="Magenta">
  <option value="Purple">
  <option value="Ultraviolet">
</datalist>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Capture-on-2019-07-30-at-21-49-55.gif)
_Sélecteur de couleur préféré_

En tirant parti des sélecteurs pseudo de CSS, nous pouvons styliser dynamiquement un élément de type case à cocher en fonction de son état :

```html
<style>
.is-checked {
    display: none;
}

#my-checkbox:checked + span .is-checked {
    display: inline;
}

#my-checkbox:checked + span .not-checked {
    display: none;
}
</style>

<label for="my-checkbox">
  <input id="my-checkbox" type="checkbox" />
  <span>
    <span class="not-checked">Non Coché</span>
    <span class="is-checked">Coché</span>
    </span>
</label>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Capture-on-2019-07-30-at-21-48-43.gif)
_Case à cocher dynamique_

### C'est Votre Art, Faites-En Attention

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-28-at-09.11.40.png)
_[https://twitter.com/markdalgleish/status/1155430223963234304](https://twitter.com/markdalgleish/status/1155430223963234304" rel="noopener)_

Je parierais que la majorité des personnes lisant ceci le font parce qu'elles se soucient de leur code et sont super passionnées par ce qu'elles font. Tout comme n'importe quel autre art qui a précédé le développement, pratiquer et se concentrer sur les fondamentaux renforcera votre capacité en tant que développeur. Bonus, vous obtiendrez une victoire facile en aidant à être plus inclusif avec votre travail et en attirant plus de personnes vers votre application !

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.colbyfayock.com/2019/08/put-down-the-javascript-learn-html-css](https://www.colbyfayock.com/2019/08/put-down-the-javascript-learn-html-css)_