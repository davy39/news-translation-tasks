---
title: Comment créer un bouton Retour en haut et une barre de progression de page
  avec HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-21T16:39:02.000Z'
originalURL: https://freecodecamp.org/news/back-to-top-button-and-page-progressbar-with-html-css-and-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Thumbnail-1.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: Comment créer un bouton Retour en haut et une barre de progression de page
  avec HTML, CSS et JavaScript
seo_desc: "By Anish De\nYou've probably seen a \"back-to-top\" button at the bottom-right\
  \ corner on many websites when you're scrolling around. Clicking on that button\
  \ takes you back to the top of the page. \nThis is a great feature to have on any\
  \ website, and toda..."
---

Par Anish De

Vous avez probablement vu un bouton "retour en haut" dans le coin inférieur droit de nombreux sites web lorsque vous faites défiler la page. En cliquant sur ce bouton, vous revenez en haut de la page. 

C'est une fonctionnalité très utile pour tout site web, et aujourd'hui nous allons voir comment la créer avec rien d'autre que HTML, CSS et JavaScript. 

Nous allons également voir comment ajouter une barre de progression de page, en haut de la page, qui augmentera à mesure que nous ferons défiler vers le bas et diminuera à mesure que nous ferons défiler vers le haut. 

Notez que vous pouvez ajouter cela à n'importe quel site web, qu'il s'agisse d'un site existant ou de quelque chose sur lequel vous venez de commencer à travailler. La seule exigence est que le site web doit avoir suffisamment de contenu (ou une hauteur de corps suffisamment grande) pour être défilable, sinon cela n'aura pas de sens de l'ajouter.

Voici le CodePen de ce que nous allons construire (faites défiler pour voir la magie) :

%[https://codepen.io/anishde12020/pen/poWPPoe]

## Comment créer un bouton Retour en haut pour votre site web

Tout d'abord, je vais rendre le corps du site web énorme afin qu'il puisse être défilé :

```css
body {
  height: 5000px;
}
```

Je vais également ajouter un dégradé linéaire au corps du document afin que nous puissions savoir que le document est défilé :

```css
body {
  height: 5000px;
  background: linear-gradient(#00ff04, #09aad3);
}
```

Ajoutons également rapidement le bouton Retour en haut au balisage :

```html
<button class="back-to-top">Retour en haut</button>

```

Positionnons également le bouton comme ceci :

```css
.back-to-top {
  position: fixed;
  right: 2rem;
  bottom: 2rem;
}
```

Ici, nous lui donnons une position fixe afin qu'il reste visible même si le document est défilé. Nous le poussons à `2rem` du bas et du côté droit de l'écran également.

Voici à quoi notre document devrait ressembler maintenant :

![Document avec un fond dégradé et un bouton fixe dans le coin inférieur droit qui dit "Retour en haut"](https://www.freecodecamp.org/news/content/images/2021/12/image-28.png)
_Document avec un fond dégradé et un bouton fixe dans le coin inférieur droit qui dit "Retour en haut"_

Maintenant, il est temps pour la partie amusante – ajouter la logique.

### Comment afficher le bouton Retour en haut uniquement lors du défilement

Maintenant, nous ne voulons pas que le bouton Retour en haut soit visible tout le temps – comme lorsque l'utilisateur est en haut de la page. Nous allons donc l'afficher de manière conditionnelle. 

Pour cet exemple, nous allons uniquement l'afficher lorsque l'utilisateur a défilé au moins 100 pixels.

Tout d'abord, nous devons masquer le bouton chaque fois que l'utilisateur ouvre le site. Nous devons également nous assurer que nous ajoutons ce style, séparé des styles de base du bouton, car le bouton doit être affiché lors du défilement.

HTML :

```html
<button class="back-to-top hidden">Retour en haut</button>
```

CSS :

```css
.hidden {
  display: none;
}
```

Voici le code pour afficher conditionnellement le bouton :

```js
const showOnPx = 100;
const backToTopButton = document.querySelector(".back-to-top")

const scrollContainer = () => {
  return document.documentElement || document.body;
};

document.addEventListener("scroll", () => {
  if (scrollContainer().scrollTop > showOnPx) {
    backToTopButton.classList.remove("hidden")
  } else {
    backToTopButton.classList.add("hidden")
  }
})
```

Ici, la fonction `scrollContainer` retourne `document.documentElement`, qui n'est rien d'autre que l'élément HTML de notre document. Au cas où celui-ci ne serait pas disponible, l'élément `document.body` est retourné à la place.

Ensuite, nous ajoutons un écouteur d'événement à notre document qui déclenchera la fonction de rappel lors du défilement. La valeur `scrollTop` ([Référence MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight)) que nous obtenons du `scrollContainer` respectif n'est rien d'autre que le nombre de pixels que l'élément a été défilé depuis le haut. 

Ici, lorsque cette valeur est supérieure à notre valeur `showOnPx` définie, c'est-à-dire `100px`, nous supprimons la classe hidden de notre bouton. Si ce n'est pas le cas, nous ajoutons la classe au bouton (surtout utile lorsque l'utilisateur fait défiler manuellement vers le haut).

Maintenant, travaillons sur la logique pour faire défiler vers le haut chaque fois que l'utilisateur clique sur le bouton.

### Comment faire défiler vers le haut chaque fois que l'utilisateur clique sur le bouton Retour en haut

Écrivons rapidement une fonction pour cela :

```js
const goToTop = () => {
  document.body.scrollIntoView();
};
```

La fonction `scrollIntoView()` ([Référence MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView)) fait défiler la page pour amener l'élément sur lequel elle est appelée en vue. Ici, nous l'appelons sur le corps, donc la page sera défilée vers le haut. 

Maintenant, nous devons que cette fonction soit appelée chaque fois que le bouton Retour en haut est cliqué :

```js
backToTopButton.addEventListener("click", goToTop)
```

C'est tout ! Nous avons ajouté avec succès la fonctionnalité Retour en haut à notre site web.

### Comment rendre le défilement fluide

Maintenant, ce défilement vers le haut était assez brutal. Voyons comment le rendre plus fluide. Nous pouvons faire cela en passant le `behaviour` comme `smooth` à la fonction `scrollIntoView()`.

```js
const goToTop = () => {
  document.body.scrollIntoView({
    behavior: "smooth",
  });
};
```

C'est tout ! Maintenant, le défilement est agréable et fluide.

### Comment styliser le bouton Retour en haut

Actuellement, le bouton Retour en haut est un simple bouton HTML avec du texte – et cela semble assez laid. Alors stylisons-le. 

Avant cela, nous allons remplacer le texte par un SVG, alors laissez-moi rapidement en prendre un sur [HeroIcons](https://heroicons.com/) :

```html
<button class="back-to-top hidden">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    class="back-to-top-icon"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      d="M7 11l5-5m0 0l5 5m-5-5v12"
    />
  </svg>
</button>
```

Nous donnons à l'icône une classe appelée `back-to-top-icon`. C'est important car l'icône n'est pas visible immédiatement et doit donc être stylisée pour être visible.

```css
.back-to-top-icon {
  width: 1rem;
  height: 1rem;
  color: black;
}
```

Voici à quoi notre bouton devrait ressembler maintenant :

![Bouton avec une icône SVG stylisée](https://www.freecodecamp.org/news/content/images/2021/12/image-30.png)
_Bouton avec une icône SVG stylisée_

Le bouton semble encore assez laid, alors stylisons-le :

```css
.back-to-top {
  position: fixed;
  right: 2rem;
  bottom: 2rem;
  border-radius: 100%;
  background: #141c38;
  padding: 0.5rem;
  border: none;
  cursor: pointer;
}
```

Maintenant, la flèche vers le haut dans notre bouton n'est pas visible, changeons sa couleur en quelque chose de plus clair pour qu'elle soit visible :

```css
.back-to-top-icon {
  width: 1rem;
  height: 1rem;
  color: #7ac9f9;
}
```

Nous pouvons également ajouter un effet de survol juste pour le rendre un peu meilleur :

```css
.back-to-top:hover {
  opacity: 60%;
}
```

Maintenant, voici à quoi notre bouton devrait ressembler :

![Bouton Retour en haut stylisé](https://www.freecodecamp.org/news/content/images/2021/12/image-44.png)
_Bouton Retour en haut stylisé_

### Comment rendre l'entrée du bouton plus fluide

Le bouton semble apparaître de nulle part chaque fois que nous faisons défiler. Changeons ce comportement en ajoutant une transition et au lieu de changer l'affichage, nous allons changer son opacité :

```css
.back-to-top {
  position: fixed;
  right: 2rem;
  bottom: 2rem;
  border-radius: 100%;
  background: #7ac9f9;
  padding: 0.5rem;
  border: none;
  cursor: pointer;
  opacity: 100%;
  transition: opacity 0.5s;
}
```

```css
.hidden {
  opacity: 0%;
}
```

Cela rend également notre effet de survol plus fluide.

Maintenant, concentrons-nous sur la barre de progression de la page.

## Comment ajouter une barre de progression de page à votre site web

Nous allons créer une barre de progression en utilisant une `div`. À mesure que l'utilisateur fait défiler la page, nous déterminerons le pourcentage défilé et continuerons à augmenter la `width`. Ajoutons d'abord la `div` et donnons-lui un nom de classe `progress-bar` :

```html
<div class="progress-bar" />
```

Maintenant, nous allons ajouter quelques styles :

```css
.progress-bar {
  height: 1rem;
  background: white;
  position: fixed;
  top: 0;
  left: 0;
}
```

Nous la rendons fixe afin qu'elle soit visible lorsque l'utilisateur fait défiler. Nous la positionnons également en haut de la page.

Maintenant, ajoutons le JavaScript qui définit la largeur de la barre de progression :

```js
const pageProgressBar = document.querySelector(".progress-bar")
document.addEventListener("scroll", () => {
  const scrolledPercentage =
      (scrollContainer().scrollTop /
        (scrollContainer().scrollHeight - scrollContainer().clientHeight)) *
      100;
  
  pageProgressBar.style.width = `${scrolledPercentage}%`
  
  if (scrollContainer().scrollTop > showOnPx) {
    backToTopButton.classList.remove("hidden");
  } else {
    backToTopButton.classList.add("hidden");
  }
});
```

Notez que nous utilisons notre fonction d'écouteur d'événement de défilement de document existante. 

Voici à quoi notre barre de progression devrait ressembler lors du défilement :

![Barre de progression de défilement de page lors du défilement](https://www.freecodecamp.org/news/content/images/2021/12/image-46.png)
_Barre de progression de défilement de page lors du défilement_

### Comment calculer le pourcentage défilé

Calculer le pourcentage défilé est en fait assez simple. La propriété `scrollTop` ([Référence MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight)) est le nombre de pixels défilés comme mentionné précédemment.

`scrollHeight` ([Référence MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight)) est la hauteur minimale requise pour contenir tous ses enfants dans l'élément sur lequel elle est appelée.

Et enfin, `clientHeight` ([Référence MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientHeight)) est la hauteur intérieure de l'élément sur lequel elle est appelée. 

Le `clientHeight` est soustrait du `scrollHeight` car si nous ne le faisons pas, la zone visible sera également prise en compte, donc nous n'atteindrons jamais 100 % de défilement. 

J'ai rassemblé ce diagramme pour mieux l'expliquer :

![Capture d'écran expliquant clientHeight et scrollHeight](https://www.freecodecamp.org/news/content/images/2021/12/image-47.png)
_Capture d'écran expliquant `clientHeight` et `scrollHeight`_

Ici, la ligne sans les flèches représente le `clientHeight` qui est la hauteur du contenu visible pour nous. La ligne avec les flèches représente le `scrollHeight` et montre que cette ligne continue dans les deux directions. C'est la hauteur de la vue requise pour contenir tout le contenu.

Enfin, la valeur `scrollTop` est divisée par la différence de `scrollHeight` et `clientHeight` et nous obtenons une valeur décimale de la quantité défilée. Cela est multiplié par `100` pour obtenir la valeur en pourcentage que nous utilisons pour déterminer la largeur de la `div`, c'est-à-dire la progression sur notre barre de progression.

## Conclusion

J'espère que vous avez trouvé cet article utile et que vous êtes en mesure d'implémenter un bouton Retour en haut et une barre de progression de page sur votre site web. 

N'hésitez pas à me contacter sur [Twitter](https://twitter.com/AnishDe12020) si vous souhaitez me poser des questions. La prochaine étape serait de l'implémenter sur votre site web et d'apporter des modifications selon vos besoins. 

### Ressources

* [CodePen pour cet exemple](https://codepen.io/anishde12020/pen/poWPPoe)
* [Référence MDN pour `scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView)
* [Référence MDN pour `scrollTop`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop)
* [Référence MDN pour `scrollHeight`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight)
* [Référence MDN pour `clientHeight`](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientHeight)

Je travaille actuellement sur un projet appelé DevKit qui est une PWA qui hébergera des outils pour développeurs dans une seule application et fournira des moyens pour accomplir votre travail rapidement. N'hésitez pas à le consulter à l'adresse [https://www.devkit.one/](https://www.devkit.one/).