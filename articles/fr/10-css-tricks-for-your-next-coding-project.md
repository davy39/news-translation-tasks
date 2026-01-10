---
title: Feuille de triche CSS – 10 astuces pour améliorer votre prochain projet de
  codage
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-07-21T22:39:42.000Z'
originalURL: https://freecodecamp.org/news/10-css-tricks-for-your-next-coding-project
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/csstricks.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Feuille de triche CSS – 10 astuces pour améliorer votre prochain projet
  de codage
seo_desc: "The cascading nature of CSS sometimes makes it tough to understand and\
  \ use. Developers at all levels often struggle while trying to figure out how to\
  \ use certain features, and you'll often find yourself googling or asking a colleague\
  \ for help. \nSo wh..."
---

La nature en cascade de CSS le rend parfois difficile à comprendre et à utiliser. Les développeurs de tous niveaux ont souvent du mal à comprendre comment utiliser certaines fonctionnalités, et vous vous retrouverez souvent à chercher sur Google ou à demander de l'aide à un collègue. 

Alors, lorsque vous avez des problèmes avec CSS, ne soyez pas trop dur avec vous-même – cela arrive à tout le monde.

Puisque CSS peut être mystérieux et trompeur, vous devez aussi être rusé si vous espérez le démystifier. C'est pourquoi, dans cet article, je vous apporte 10 astuces CSS géniales qui vous faciliteront la vie en tant que développeur, surtout si vous êtes débutant.

## 1. Comment corriger le défilement horizontal sur une page web en CSS

Si vous stylisez votre page web et que vous voyez une barre de défilement horizontale en bas, vous devez trouver l'élément qui a une largeur supérieure à la largeur d'écran disponible.

Par exemple, dans la capture d'écran ci-dessous, vous pouvez voir qu'il y a un défilement horizontal :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/horizontalscroll1.png)

Vous pouvez utiliser le sélecteur universel (*) pour trouver l'élément responsable en appliquant les règles suivantes :

```css
* { 
     border: 2px solid red;
}
```

Cela applique une bordure rouge de 2 pixels à chaque élément de la page et vous pouvez ainsi facilement identifier l'élément à ajuster.

Après avoir appliqué le style ci-dessus, voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/horizontalscrollfix.png)

Vous pouvez voir que la deuxième vague verte provoque le défilement horizontal. Cela est dû au fait que la largeur a été définie à 1400px, ce qui est plus large que la largeur d'écran disponible de 1200px.

```
.wave2 {
  width: 1400px;
}
```

Rétablir la largeur à 1200px ou la supprimer entièrement résoudra le problème afin qu'il n'y ait plus de défilement horizontal.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/horizontalScrollFixed.png)

## 2. Comment remplacer un style en CSS

Dans certains cas spécifiques, vous pourriez vouloir remplacer un style particulier qui existe déjà (comme celui d'une bibliothèque). Ou vous pourriez avoir un modèle avec une grande feuille de style que vous devez personnaliser pour une partie particulière.

Dans ces situations, vous pouvez soit [appliquer les règles de spécificité CSS](https://www.freecodecamp.org/news/what-is-css-specificity/), soit utiliser l'exception `!important` devant votre règle.

Dans l'exemple ci-dessous, `!important` donne à chaque élément h1 une variation verte émeraude de #2ecc71 (ma couleur préférée) :

```css
h1 {
    color: #2ecc71 !important;
}
```

Mais attention – utiliser cette exception est considéré comme une mauvaise pratique, et vous devriez l'éviter autant que possible.

Pourquoi ? Eh bien, `!important` brise en réalité la nature en cascade de CSS, et cela peut rendre le débogage plus difficile.

Le meilleur cas d'utilisation pour `!important` est de l'utiliser pour identifier un problème dans votre base de code lorsque vous travaillez avec une grande feuille de style de modèles ou de vieux code. Ensuite, vous pouvez rapidement corriger le problème et supprimer l'exception.

Au lieu d'utiliser !important pour appliquer des styles, vous pouvez [en apprendre davantage sur la spécificité CSS](https://www.freecodecamp.org/news/what-is-css-specificity/) et appliquer ces règles.

## 3. Comment créer un carré avec CSS

Si vous voulez créer un carré sans avoir à trop vous soucier de la largeur et de la hauteur, vous pouvez styliser votre div [ou span selon le cas] en définissant une couleur de fond, la largeur dont vous avez besoin, puis un ratio d'aspect avec des chiffres égaux. Le premier chiffre est pour la dimension haut et bas, le second pour gauche et droite.

Vous pouvez aller plus loin en jouant avec les deux chiffres pour créer des rectangles et tout autre carré que vous souhaitez.

```html
<div class="square"></div>
```

```css
.square {
  background: #2ecc71;
  width: 25rem;
  aspect-ratio: 1/1;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/square.png)

## 4. Comment centrer une div avec CSS

Centrer une div peut devenir assez difficile à mesure que votre feuille de style grandit. Pour styliser n'importe quelle div, donnez-lui un affichage de type bloc, une marge automatique et une largeur inférieure à 100%.

```html
<div class="center"></div>
```

```css
.center {
    background-color: #2ecc71;
    display: block;
    margin: auto;
    width: 50%;
    height: 200px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/centeredDiv.png)

## 5. Comment supprimer le remplissage supplémentaire dans une boîte en CSS

Utiliser `box-sizing: border-box` garantira qu'aucun remplissage supplémentaire ne sera ajouté à une boîte lorsque vous définissez une largeur et un remplissage pour celle-ci. Cela aidera vos mises en page à avoir une meilleure apparence.

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

## 6. Comment créer une lettrine avec CSS

Vous pouvez créer une lettrine avec le pseudo-élément first-letter. Oui ! La lettrine que vous voyez dans les journaux.

Sélectionnez l'élément HTML approprié et appliquez le style comme je l'ai fait ci-dessous :

```html
 <p class="texts">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia officia nisi
      veniam laboriosam? In excepturi ea inventore eligendi iusto! Incidunt
      molestiae quas molestias, nesciunt voluptate aut vitae odio corrupti
      quisquam laudantium aperiam consequuntur voluptas eum? Velit, eligendi ad
      laboriosam beatae corporis perferendis tempore consequatur sint rem quam,
      quae, assumenda rerum.
 </p>
```

```css
p.texts::first-letter {
  font-size: 200%;
  color: #2ecc71;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/dropcapScreen-1.png)

## 7. Comment mettre du texte en majuscules ou en minuscules en CSS

Les lettres en majuscules ou en minuscules n'ont pas besoin de provenir directement de votre HTML. Vous pouvez forcer n'importe quel texte à être en MAJUSCULES ou en minuscules dans votre CSS.

J'espère qu'il y aura des options pour SentenceCase et tOGGLEcASE à l'avenir. Mais pourquoi voudriez-vous mettre un texte en tOGGLEcASE de toute façon ?

```html
<p class="upper">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium,
      minima.
</p>
<p class="lower">LOREM IPSUM DOLOR SIT AMET</p>
```

```css
.upper {
  text-transform: uppercase;
}

.lower {
  text-transform: lowercase;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/transform.png)

## 8. Comment déclarer des variables pour garder votre CSS DRY

Des variables ? Oui. Vous pouvez déclarer des variables en CSS.

Lorsque vous déclarez des variables, vous pouvez les utiliser dans un certain nombre d'autres styles. Si vous avez quelque chose à changer, vous ne changez que cette variable et le résultat sera reflété partout où elles sont utilisées. Cela aidera à garder votre code CSS DRY (Don't Repeat Yourself).

Vous pouvez déclarer une variable en la plaçant dans la portée racine afin qu'elle soit globale dans la feuille de style. Et pour utiliser votre variable, vous placez la propriété à l'intérieur des accolades à côté du mot-clé "var".

Il est courant de déclarer la ou les variables en haut de la feuille de style – c'est-à-dire avant les réinitialisations.

```css
:root {
  --text-color: hsl(145, 63%, 49%);
}

p {
  color: var(--text-color);
}

```

## 9. Comment utiliser les sélecteurs :before et :after pour ajouter du contenu supplémentaire à votre CSS

Le sélecteur `:before` en CSS vous aide à insérer du contenu avant un élément :

```html
<p class="texts">
  Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium,
  minima.
</p>
```

```css
p.texts::before {
  content: "Some Lorem Texts: ";
  color: #2ecc71;
  font-weight: bolder;
}
```

Le sélecteur `:after` fait de même, mais il insère le contenu après l'élément :

```css
p.texts::after {
  content: " Those were Some Lorem Texts";
  color: #2ecc71;
  font-weight: bolder;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/beforeAndAfter.png)

## 10. Comment obtenir un défilement fluide avec du CSS pur

Vous pouvez appliquer un défilement fluide sur une page web sans avoir à écrire du JavaScript complexe ou à utiliser un plugin. Ainsi, si vous avez des balises d'ancrage qui lient à plusieurs portions de la page web et que vous cliquez dessus, le défilement est fluide.

```css
html {
  scroll-behavior: smooth;
}
```

C'est tout !

Merci d'avoir lu. Connectez-vous avec moi via mon [portfolio](https://ksound22.github.io) et [Twitter](https://twitter.com/koladechris), où je passe la plupart de mon temps à tweeter et à m'engager dans des sujets liés au codage et au développement web.