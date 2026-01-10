---
title: Comment créer un curseur de souris personnalisé avec CSS et JavaScript
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2022-01-10T16:13:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-custom-mouse-cursor-with-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/salman-hossain-saif-m3xjTe9zl6k-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_title: Comment créer un curseur de souris personnalisé avec CSS et JavaScript
seo_desc: "Have you ever visited a website and been totally blown away by its amazing\
  \ features? One of them might be a cool mouse cursor that is different from the\
  \ regular arrow or pointer cursors you are used to.  \nThis can really improve user\
  \ experience, and ..."
---

Avez-vous déjà visité un site web et été totalement impressionné par ses fonctionnalités incroyables ? L'une d'entre elles pourrait être un curseur de souris cool, différent des curseurs en forme de flèche ou de pointeur auxquels vous êtes habitué.  

Cela peut vraiment améliorer l'expérience utilisateur, et dernièrement, je me suis demandé comment cela fonctionnait. Alors, j'ai commencé à faire quelques recherches et j'ai découvert comment cela était fait.

Dans cet article, je vais expliquer comment créer un curseur de souris personnalisé. À la fin de cet article, vous apprendrez à créer ces curseurs avec deux méthodes différentes, en utilisant CSS et JavaScript. Ensuite, vous serez prêt à dynamiser votre site web avec différents curseurs créatifs pour garder votre audience engagée. Prêt ? Plongeons-nous dans le sujet.

## Prérequis

Cet article est adapté aux débutants, mais pour comprendre certains concepts, vous devez avoir des connaissances de base en :

* HTML
* CSS de base
* JavaScript de base

## Comment personnaliser un curseur de souris avec CSS

Personnaliser un curseur de souris avec CSS est assez simple, car CSS dispose déjà d'une propriété pour gérer cela. Tout ce que nous devons faire est d'identifier cette propriété et de l'utiliser. 

En tant qu'ingénieurs Frontend, nous utilisons souvent cette propriété – il n'y en a pas d'autre que la toute-puissante propriété `cursor`. Oui, cette propriété est ce qui nous donne le pouvoir de créer un curseur personnalisé de notre choix.

Avant de passer à un exemple pratique, examinons les valeurs associées à la propriété CSS `cursor`. Bien que la plupart des développeurs n'utilisent que quelques-unes des plus importantes, il y en a d'autres que nous devrions examiner.

%[https://codepen.io/developeraspire5/pen/XWeBEXo]

À partir de l'extrait de code ci-dessus et des résultats, vous pouvez voir et tester différents curseurs de souris que CSS propose en survolant votre curseur de souris sur chacune de ces cases contenant le nom de chaque valeur de la propriété CSS `cursor`.

Maintenant, comment utiliser CSS pour personnaliser un curseur de souris ? Pour utiliser cela, vous devez simplement indiquer à CSS quelle image vous souhaitez utiliser et pointer la propriété cursor vers l'URL de l'image en utilisant la valeur `url`.

```css
body {
  cursor: url('chemin-de-l-image.png'),auto;
}
```

À partir de l'extrait de code ci-dessus, vous pouvez voir que je l'ai défini sur le corps du document, afin qu'il puisse s'appliquer au curseur où qu'il se déplace. Il contient l'image spécifiée dans `url()`.

La valeur suivante de la propriété est un recours, au cas où l'image ne se chargerait pas ou ne pourrait pas être trouvée, peut-être en raison de certains bugs internes. Je suis sûr que vous ne voudriez pas que votre site web soit "sans curseur", donc ajouter un recours est très important. Vous pouvez également ajouter autant d'URL de recours que vous le souhaitez.

```css
body {
  cursor: url('chemin-de-l-image.png'), url('chemin-de-l-image-2.svg), 
          url('chemin-de-l-image-3.jpeg'), auto;
}
```

Vous pouvez également personnaliser le curseur sur un élément ou une section particulière de votre page web. Voici un exemple CodePen :

%[https://codepen.io/developeraspire5/pen/GRMBxWN]

C'est tout ce qu'il y a à savoir sur la personnalisation des curseurs en CSS. Maintenant, voyons comment nous pouvons faire cela en JavaScript.

## Comment créer des curseurs de souris personnalisés avec JavaScript

Pour réaliser cela avec JavaScript, vous devez manipuler le DOM pour obtenir le résultat souhaité. 

Tout d'abord, examinons le HTML :

### Le HTML

```html
<div class="cursor rounded"></div>
<div class="cursor pointed"><div>
```

À partir de l'extrait de code ci-dessus, j'ai créé deux `divs` pour représenter le curseur. Le plan est de manipuler ces divs à partir de JavaScript afin que leur mouvement sur la page web soit contrôlé par l'événement `mousemove` de JavaScript en utilisant les coordonnées X et Y du mouvement de la souris. 

Maintenant, passons à la partie CSS qui aura tout son sens pièce par pièce.

### Comment styliser des curseurs personnalisés avec CSS 

```css
body{
  background-color: #1D1E22;
  cursor: none;
}

.rounded{
  width: 30px;
  height: 30px;
  border: 2px solid #fff;
  border-radius: 50%;
}

.pointed{
  width: 7px;
  height: 7px;
  background-color: white;
  border-radius: 50%;
}
```

En regardant le code CSS ci-dessus, j'ai désactivé le curseur (vous vous souvenez de `cursor:none` ?). Cela rendra le curseur invisible, permettant uniquement à notre curseur personnalisé de s'afficher. 

Les `divs` que j'ai stylisées pour leur donner un look unique de type "curseur". Vous pouvez absolument faire plus avec, peut-être ajouter une image de fond, un emoji, des autocollants, etc., à condition qu'il y ait des images. Maintenant, jetons un coup d'œil au JavaScript.

### Comment utiliser JavaScript pour faire bouger le curseur

```javascript
const cursorRounded = document.querySelector('.rounded');
const cursorPointed = document.querySelector('.pointed');


const moveCursor = (e)=> {
  const mouseY = e.clientY;
  const mouseX = e.clientX;
  
  cursorRounded.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
  
  cursorPointed.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
 
}

window.addEventListener('mousemove', moveCursor)
```

J'ai ajouté un écouteur d'événement sur l'objet window global pour écouter tout mouvement de la souris. Lorsque la souris bouge, l'expression de fonction `moveCursor` est appelée et elle reçoit l'objet événement en tant que paramètre. Avec ce paramètre, j'ai pu obtenir les coordonnées X et Y de la souris à tout point sur la page.

J'ai déjà sélectionné chaque type de curseur à partir du DOM en utilisant JavaScript `querySelector`. Donc, tout ce que j'avais à faire était de les déplacer selon les coordonnées X et Y de la souris en contrôlant les propriétés de transformation sur le style avec la valeur `translate3d`. Cela permettra aux divs de se déplacer lorsque la souris se déplace à n'importe quel point sur la page web. 

Et les guillemets inversés que vous voyez s'appellent des littéraux de gabarit. Cela permet d'écrire des variables facilement pour les ajouter aux chaînes de caractères. L'alternative serait de concaténer les variables aux chaînes de caractères.

Simple, n'est-ce pas ? C'est tout !

Voici un exemple CodePen et le résultat de l'extrait de code ci-dessus :

%[https://codepen.io/developeraspire5/pen/gOGjeZG]

## Quelle méthode fonctionne le mieux ?

Maintenant, c'est à vous, en tant que développeur, de choisir la méthode qui fonctionne le mieux pour vous. Vous pouvez choisir d'utiliser CSS si vous souhaitez utiliser des emojis ou des images jolis comme curseur. D'autre part, vous pourriez vouloir utiliser JavaScript pour personnaliser des formes complexes de votre choix et animer le mouvement du curseur.

Dans les deux cas, c'est bien, tant que vous obtenez les résultats souhaités et impressionnez tous les visiteurs de votre site.

J'espère que vous avez appris beaucoup de choses grâce à cet article, et j'ai hâte de voir ce que vous allez construire avec cette connaissance. 

Pour plus de conseils CSS, suivez-moi sur [Twitter](https://twitter.com/DeveloperAspire).

Merci d'avoir lu, à la prochaine.