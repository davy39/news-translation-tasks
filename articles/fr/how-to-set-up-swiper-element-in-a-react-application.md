---
title: Comment installer Swiper Element dans une application React
subtitle: ''
author: Alex Anie
co_authors: []
series: null
date: '2024-02-19T16:25:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-swiper-element-in-a-react-application
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/How-to-Set-up-Swiper-Element-in-React-Application-1.png
tags:
- name: animations
  slug: animations
- name: React
  slug: react
seo_title: Comment installer Swiper Element dans une application React
seo_desc: "Carousels or image sliders are an integral part of many web applications.\
  \ They help you group multiple elements in a single view. \nUsing carousels, you\
  \ can implement image slides, video slides, text slides, interactive image galleries,\
  \ product catalo..."
---

Les carousels ou sliders d'images sont une partie intégrante de nombreuses applications web. Ils vous aident à regrouper plusieurs éléments dans une seule vue.

En utilisant des carousels, vous pouvez implémenter des diapositives d'images, des diapositives vidéo, des diapositives de texte, des galeries d'images interactives, des catalogues de produits, des profils d'équipe, et bien plus encore.

[Swiper.js](https://swiperjs.com/) offre des fonctionnalités puissantes qui facilitent la création de composants de carousels fonctionnels, réutilisables avec des effets et des fonctionnalités impressionnants. Vous pouvez activer le zoom avant et arrière sur les images, le défilement horizontal et vertical des images, les effets de diapositive en parallaxe, et les diapositives en boucle infinie, pour n'en nommer que quelques-uns.

Dans ce tutoriel, nous nous concentrerons sur la nouvelle version de Swiper, 11.0.6, et le nouvel élément Swiper recommandé pour la création de diapositives dans Swiper.js.

À la fin de ce guide, vous devriez être en mesure d'implémenter le nouvel élément Swiper de Swiper.js pour créer des diapositives dynamiques et réactives avec des effets prédéfinis dans votre projet React.

## Table des matières

- [Qu'est-ce que Swiper.js ?](#heading-quest-ce-que-swiperjs)
- [Installations](#heading-installations)
- [Comment configurer Swiper](#heading-comment-configurer-swiper)
    - [Modules Node](#heading-modules-node)
    - [Éléments personnalisés Swiper depuis CDN](#heading-elements-personnalises-swiper-depuis-cdn)
    - [Éléments personnalisés Swiper](#heading-elements-personnalises-swiper)
- [Paramètres Swiper en tant qu'attributs](#heading-parametres-swiper-en-tant-quattributs)
- [Points de rupture réactifs dans Swiper Element](#heading-points-de-rupture-reactifs-dans-swiper-element)
- [Pagination et Navigation](#heading-pagination-et-navigation)
- [Chargement paresseux des images](#heading-chargement-paresseux-des-images)
- [Effets dans Swiper Element](#heading-effets-dans-swiper-element)
- [Sliders verticaux](#heading-sliders-verticaux)
- [Comment styliser Swiper Element](#heading-comment-styliser-swiper-element)
    - [Réinitialiser les styles personnalisés Swiper](#heading-reinitialiser-les-styles-personnalises-swiper)
    - [Créer un nouveau nom de classe](#heading-creer-un-nouveau-nom-de-classe)
- [Comment construire un élément Slider personnalisé](#heading-comment-construire-un-element-slider-personnalise)
- [Résumé](#heading-resume)
- [Références](#heading-references)

## Prérequis

Avant de commencer, vous aurez besoin d'avoir des connaissances de base sur [React.js](https://react.dev/).

Si vous avez besoin d'un rappel, vous pouvez consulter ce [guide React pour débutants](https://www.freecodecamp.org/news/react-beginner-handbook/).

## Qu'est-ce que Swiper.js ?

Swiper est une bibliothèque JavaScript moderne et gratuite pour créer des sliders tactiles (carousels) avec des transitions matérielles et des comportements natifs impressionnants.

Swiper est conçu pour les sites web mobiles, les applications web mobiles et les applications mobiles natives/hybrides. Swiper offre également un excellent support et des fonctionnalités pour les sites web et les applications de bureau.

![Guide de migration de Swiper React Component vers Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/Untitled.png)

Au moment de la rédaction, Swiper *v11.0.6* recommande de migrer vers [Swiper Element](https://swiperjs.com/element) au lieu de [Swiper React Components](https://swiperjs.com/react), qui sera probablement supprimé dans les versions futures. Dans ce tutoriel, nous nous concentrerons sur Swiper Element et ses cas d'utilisation.

## Installations

Pour commencer, générez du code React de base avec [Vite.js](https://vitejs.dev/guide/). Ensuite, accédez au répertoire du projet dans votre terminal et tapez la commande suivante pour installer Swiper.js :

```bash
npm i swiper
```

Ensuite, tapez la commande suivante pour lancer votre code de base React.js :

```bash
npm run dev
```

Cliquez sur l'URL du port dans le terminal pour ouvrir votre code de base React dans le navigateur.

## Comment configurer Swiper

Pour utiliser Swiper dans un projet React, vous pouvez utiliser les méthodes suivantes.

### Modules Node

Si vous installez Swiper via `npm i swiper`, puis `import` l'élément personnalisé depuis *node_modules* et enregistrez-le.

```jsx
 main.jsx

// import function to register Swiper custom elements
import { register } from 'swiper/element/bundle';
// register Swiper custom elements
register();
```

Cela doit être fait une fois directement sur le fichier `main.jsx` pour l'installer globalement.

### Éléments personnalisés Swiper depuis CDN

Pour activer Swiper Element, incluez le lien CDN dans la balise script comme indiqué ci-dessous :

```jsx
 index.html
<head>
	<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.js"></script>
</head>
```

Faites cela une fois directement sur le fichier `index.html` pour l'activer globalement.

## Éléments personnalisés Swiper

Si vous avez correctement configuré Swiper Element et appelez la méthode `register()`. Pour créer un slider, vous devrez utiliser `<swiper-container>` et `<swiper-slide>` de Swiper.js.

```jsx
export default function Usage() {
  return (
    <>
    <main>
        <swiper-container>
            <swiper-slide>Slide1</swiper-slide>
            <swiper-slide>Slide2</swiper-slide>
            <swiper-slide>Slide3</swiper-slide>
            <swiper-slide>Slide4</swiper-slide>
            <swiper-slide>Slide5</swiper-slide>
        </swiper-container>
    </main>
    </>
  )
}
```

Le code ci-dessus montre comment structurer les diapositives en utilisant les éléments personnalisés Swiper.

- `<swiper-container>` : Il s'agit de l'élément parent qui sert de conteneur à l'élément personnalisé `<swiper-slide>` et à d'autres éléments HTML qui composent les diapositives. Tout élément qui est imbriqué à l'intérieur de l'élément personnalisé `<swiper-container>` est traité comme une diapositive.
- `<swiper-slide>` : Il s'agit de l'enfant direct de l'élément personnalisé `<swiper-container>`. Le `<swiper-slide>` sert de diapositive individuelle des composants du slider.

Pour des raisons de clarté, j'ai ajouté quelques styles CSS personnalisés pour le rendre visuellement attrayant et facile à comprendre. Copiez le code ci-dessous : 

```css
*,*::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: calibri;
}

body {
    display: flex;
    justify-content: center;
}

swiper-container {
    width: 800px;
    height: 200px;
    line-height: 200px;
    text-align: center;
}

swiper-slide {
    background-color: rgb(4 47 46);
    color: #fff;
    font-size: 25px;
}

swiper-slide:nth-child(2) {
    background-color: rgb(15 118 110);
}

swiper-slide:nth-child(3) {
    background-color: rgb(45 212 191);
}

swiper-slide:nth-child(4) {
    background-color: rgb(153 246 228);
}

swiper-slide:nth-child(5) {
    background-color: rgb(34 197 94);
}
```

Votre code devrait ressembler à ceci dans votre navigateur :

![Slide montre le slider créé avec Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/Swiper_custome_Elements.gif)

## Paramètres Swiper en tant qu'attributs

Les [paramètres](https://swiperjs.com/element) dans Swiper sont des paires *clé* et *valeur* ou *clé*, *sous-clé* et *valeur* comme indiqué ci-dessous.

```jsx
const swiper = new Swiper('.swiper', {
  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true,
  },
mousewheel: {
    invert: true,
  },
slidesPerView: 3,
spaceBetween: 20,
scrollbar: {
	clickable: true,
});
```

Le code ci-dessus est valide si nous travaillons directement sur le fichier [index.html](https://codesandbox.io/p/sandbox/p3f7rh?file=%2Findex.html%3A58%2C33) et que nous utilisons les classes `swiper` et `swiper-slide` sur des éléments div.

Pour les éléments personnalisés Swiper, vous pouvez écrire le même code comme suit : 

```jsx
export default function Usage() {
return (
    <>
    <main>
      <swiper-container slides-per-view="3" space-between="20" scrollbar-clickable="true" mousewheel-invert="true">
            <swiper-slide>Slide1</swiper-slide>
            <swiper-slide>Slide2</swiper-slide>
            <swiper-slide>Slide3</swiper-slide>
            <swiper-slide>Slide4</swiper-slide>
            <swiper-slide>Slide5</swiper-slide>
        </swiper-container>
    </main>
    </>
)
}
```

Tous les paramètres Swiper sont écrits sous la forme d'attributs [kebab-case](https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/#kebab-case) sur les éléments personnalisés `<swiper-container>`.

Les paramètres avec *sous-clés* et *valeurs* sont écrits comme un seul attribut et une seule valeur. Par exemple, `scrollbar-clickable="true"` est un paramètre avec une sous-clé *(clickable)* maintenant écrit comme un seul attribut avec une valeur.

Si vous exécutez le code ci-dessus, vous devriez obtenir le même résultat que ci-dessous :

![sliders swiper.js avec vues à trois colonnes](https://www.freecodecamp.org/news/content/images/2024/02/Parameter_as_value.gif)

À partir du navigateur, nous avons pu diviser la vue en vues à *trois colonnes* au lieu de la vue à *une colonne* que nous avions précédemment. Nous avons pu faire cela en utilisant l'attribut `slide-per-view` analysé dans l'élément personnalisé `<swiper-container>`. Pour la liste complète des paramètres disponibles, voir les [API Swiper](https://swiperjs.com/swiper-api#parameters).

## Points de rupture réactifs dans Swiper Element

L'élément personnalisé Swiper nécessite des attributs pour analyser les objets de paramètres. Lorsque des propriétés d'objet complexes sont requises dans le cas des points de rupture, nous pouvons utiliser [JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) pour convertir les objets en chaînes, rendant les propriétés d'objet des points de rupture lisibles pour le `<swiper-container>`.

Considérez l'exemple de code ci-dessous :

```jsx
export default function Usage() {
return (
    <>
    <main>
        <swiper-container breakpoints={
            JSON.stringify({
                
                640:{
                    slidesPerView: 1,
                    spaceBetween: 20,
                },
    
                768: {
                    slidesPerView: 3,
                    spaceBetween: 40,
                },
    
                1024: {
                    slidesPerView: 4,
                    spaceBetween: 50,
                }
            })
        }>
            <swiper-slide>Slide1</swiper-slide>
            <swiper-slide>Slide2</swiper-slide>
            <swiper-slide>Slide3</swiper-slide>
            <swiper-slide>Slide4</swiper-slide>
            <swiper-slide>Slide5</swiper-slide>
            <swiper-slide>Slide6</swiper-slide>
            <swiper-slide>Slide7</swiper-slide>
            <swiper-slide>Slide8</swiper-slide>
            <swiper-slide>Slide9</swiper-slide>
        </swiper-container>
    </main>
    </>
)
}
```

Ici, nous ajoutons trois points de rupture différents *`640`*, `768` et `1024` respectivement pour trois tailles d'écran différentes (requêtes média), où `640` signifie (`max-width:640px`) pour les petits écrans.

Votre code devrait ressembler à ceci lorsque vous l'exécutez dans le navigateur :

![Points de rupture réactifs avec Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/Responsive_Breakpoints.gif)

Gardez à l'esprit que les points de rupture répondent dès que les composants [montent](https://www.freecodecamp.org/news/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630/) (c'est-à-dire que React rend les composants pour la première fois). Donc, si vous redimensionnez votre navigateur de bureau pendant que vous apprenez cela, vous devrez recharger toute la page en cliquant sur l'icône de rechargement pour voir les changements de points de rupture.

## Pagination et Navigation

Swiper propose des paramètres `navigation` et `pagination` pour ajouter des contrôles aux sliders. Avec `navigation`, vous pouvez passer de la diapositive actuelle à la diapositive précédente ou suivante, tandis qu'avec `pagination`, vous pouvez sauter à une diapositive spécifique dans le conteneur du slider.

Pour activer cela sur l'élément personnalisé swiper, appliquez chaque paramètre en tant qu'attribut sur le `<swiper-container>` avec une valeur de `true`.

```jsx
export default function Usage() {

return (
    <>
    <main>
    <swiper-container space-between="10" slides-per-view="3" pagination="true" navigation="true" >
            <swiper-slide>Slide1</swiper-slide>
            <swiper-slide>Slide2</swiper-slide>
            <swiper-slide>Slide3</swiper-slide>
            <swiper-slide>Slide4</swiper-slide>
            <swiper-slide>Slide5</swiper-slide>
        </swiper-container>
    </main>
    </>
)
}
```

Votre code devrait ressembler à ceci dans le navigateur :

![pagination et navigation dans Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/pagination_and_navigation.gif)

Pour déplacer les diapositives, cliquez sur la flèche de navigation ou sur les points de pagination.

## Chargement paresseux des images

Nous pouvons implémenter le [chargement paresseux](https://www.freecodecamp.org/news/how-to-lazy-load-images-in-react/) sur les sliders d'images dans les éléments personnalisés Swiper. Appliquez `lazy="true"` et `loading="lazy"` en tant qu'attributs sur `<swiper-slide>` et la balise `<img />`, respectivement.

```jsx
export default function Usage() {

return (
    <>
    <main>
    <swiper-container style={
        {
        "--swiper-navigation-color": "#fff", 
        "--swiper-pagination-color": "#fff"
        }
    } 
    pagination-clickable="true" 
    navigation="true" 
    className="mySwiper">
            <swiper-slide lazy="true">
                <img src="https://source.unsplash.com/slightly-opened-silver-macbook-mP7aPSUm7aE" loading="lazy" alt="" />
            </swiper-slide>
                
            <swiper-slide lazy="true">
                <img loading="lazy" src="https://source.unsplash.com/macbook-y0_vFxOHayg" alt="" />
            </swiper-slide>

            <swiper-slide lazy="true">
                <img loading="lazy" src="https://source.unsplash.com/black-macbook-near-black-iphone-7-plus-and-black-apple-watch-HY3l4IeOc3E" alt="" />
            </swiper-slide>

            <swiper-slide lazy="true">
                <img loading="lazy" src="https://source.unsplash.com/apple-products-on-table-tdMu8W9NTnY" alt="" />
            </swiper-slide>

            <swiper-slide lazy="true">
                    <img loading="lazy" src="https://source.unsplash.com/turned-on-ipad-Im8ylpB8SpI" alt="" />
            </swiper-slide>
        </swiper-container>
    </main>
    </>
)
}
```

L'implémentation du chargement paresseux sur les images nécessitera l'ajout de l'élément *preloader* paresseux à chaque diapositive sur le composant `<swiper-slide>` lorsque `lazy="true"` est défini sur l'élément.

J'ai ajouté quelques styles CSS pour nettoyer un peu les choses, donc vous pouvez simplement copier le code ci-dessous :

```css
*,*::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: calibri;
}

body {
    display: flex;
    justify-content: center;
}

swiper-container {
    width: 800px;
    height: 400px;
    
}

swiper-slide {
   width: 100%;
   height: 100%;
}

swiper-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

Votre code devrait ressembler à ceci lorsque vous l'exécutez dans le navigateur :

![chargement paresseux des images dans Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/lazy_loading_images.gif)

## Effets dans Swiper Element

Vous pouvez ajouter des effets dans Swiper Element en définissant l'attribut `effect` sur la valeur souhaitée pour votre projet. Par exemple, nous avons implémenté un effet `cube` pour créer un affichage de diapositive en 3D.

```jsx
export default function Usage() {

return (
    <>
    <main>
    <swiper-container style={
        {
        "--swiper-navigation-color": "#fff", 
        "--swiper-pagination-color": "#fff"
        }
    } 

    pagination-clickable="true" 
    navigation="true"
    effect="cube"
    grab-cursor="true"
    cube-effect-shadow="true"
    cube-effect-slide-shadows="true"
    cube-effect-shadow-offset="20"
    cube-effect-shadow-scale="0.94"

    className="mySwiper">
            <swiper-slide >
                <img src="https://source.unsplash.com/slightly-opened-silver-macbook-mP7aPSUm7aE"  alt="" />
            </swiper-slide>
                
            <swiper-slide>
                <img src="https://source.unsplash.com/macbook-y0_vFxOHayg" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/black-macbook-near-black-iphone-7-plus-and-black-apple-watch-HY3l4IeOc3E" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/apple-products-on-table-tdMu8W9NTnY" alt="" />
            </swiper-slide>

            <swiper-slide>
                    <img src="https://source.unsplash.com/turned-on-ipad-Im8ylpB8SpI" alt="" />
            </swiper-slide>
        </swiper-container>
    </main>
    </>
)
}
```

Votre code devrait ressembler à ceci dans le navigateur :

![effet cube dans Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/effects.gif)

Ici, nous appliquons les attributs de l'effet cube comme suit :

- **effect="cube"** : définit le slider en cube
- **grab-cursor="true"** : change le curseur en une icône de préhension.
- **cube-effect-shadow="true"** : définit l'ombre sur le composant principal de la diapositive
- **cube-effect-slide-shadows="true"** : définit l'ombre sur l'élément de la diapositive
- **cube-effect-shadow-offset="20"** : définit la direction de décalage de l'ombre
- **cube-effect-shadow-scale="0.94"** : définit la taille de l'ombre

Outre l'effet cube, vous pouvez spécifier d'autres valeurs comme vous pouvez le voir listé dans l'[API Swiper ici](https://swiperjs.com/swiper-api#cube-effect).

## Sliders verticaux

Pour appliquer des diapositives verticales, appliquez simplement l'attribut `direction="vertical"` sur le `<swiper-component>` comme vous pouvez le voir dans le code ci-dessous :

```jsx
export default function Usage() {

return (
    <>
    <main>
    <swiper-container style={
        {
        "--swiper-navigation-color": "#fff", 
        "--swiper-pagination-color": "#fff"
        }
    } 

    pagination-clickable="true" 
    navigation="true"
   
    direction="vertical"

    className="mySwiper">
            <swiper-slide >
                <img src="https://source.unsplash.com/slightly-opened-silver-macbook-mP7aPSUm7aE"  alt="" />
            </swiper-slide>
                
            <swiper-slide>
                <img src="https://source.unsplash.com/macbook-y0_vFxOHayg" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/black-macbook-near-black-iphone-7-plus-and-black-apple-watch-HY3l4IeOc3E" alt="" />
            </swiper-slide>

        </swiper-container>
    </main>
    </>
)
}
```

Votre code devrait ressembler à ceci lorsque vous l'exécutez dans le navigateur :

![diapositives verticales dans Swiper Element](https://www.freecodecamp.org/news/content/images/2024/02/vertical_slides.gif)

## Comment styliser Swiper Element

Styliser Swiper Element est très simple. Swiper propose de nombreuses classes prédéfinies qui sont appliquées aux paramètres Swiper (attributs dans les éléments personnalisés Swiper). Nous pouvons remplacer les règles de style par défaut de ces classes avec l'attribut HTML `style` ou des règles CSS externes.

Les éléments personnalisés Swiper peuvent être stylisés de deux manières : vous pouvez réinitialiser les styles par défaut sur les *éléments personnalisés Swiper* et les *classes CSS personnalisées*, ou créer un *nouveau nom de classe* sur l'élément Swiper et le styliser.

### Réinitialiser les styles personnalisés Swiper

Pour réinitialiser les styles des éléments personnalisés Swiper, ciblez les éléments ou classes personnalisés Swiper spécifiques auxquels les styles par défaut sont appliqués et modifiez-les selon vos styles souhaités.

```jsx
export default function Usage() {

return (
    <>
    <main>
    <swiper-container style={
        {
        "--swiper-navigation-color": "#fff", 
        "--swiper-pagination-color": "#fff"
        }
    } 

    pagination-clickable="true" 
    navigation="true"

    className="mySwiper">
            <swiper-slide >
                <img src="https://source.unsplash.com/slightly-opened-silver-macbook-mP7aPSUm7aE"  alt="" />
            </swiper-slide>
                
            <swiper-slide>
                <img src="https://source.unsplash.com/macbook-y0_vFxOHayg" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/black-macbook-near-black-iphone-7-plus-and-black-apple-watch-HY3l4IeOc3E" alt="" />
            </swiper-slide>

        </swiper-container>
    </main>
    </>
)
}
```

Dans l'exemple de code ci-dessus, `--swiper-navigation-color` et `--swiper-pagination-color` sont définis sur la couleur `#fff` pour changer les couleurs par défaut des boutons de *navigation* et de *pagination* de la couleur bleue claire `#007aff`. Selon ce sur quoi vous travaillez, vous pouvez personnaliser cela davantage en utilisant d'autres classes personnalisées de l'[API Swiper](https://swiperjs.com/swiper-api).

De plus, le `<swiper-container>` et le `<swiper-slide>` sont stylisés comme suit :

```jsx
*,*::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: calibri;
}

body {
    display: flex;
    justify-content: center;
}

swiper-container {
    width: 800px;
    height: 400px;
    
}

swiper-slide {
   width: 100%;
   height: 100%;
}

swiper-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

Dans l'exemple de code ci-dessus, le `swiper-container` est défini sur `width: 800px` et `height: 400px` pour donner au `swiper-container` une `width` et une `height` définies. Le `swiper-slide` est défini sur `100%` pour la `width` et la `height` pour définir intrinsèquement tout élément enfant du `swiper-slide` à la taille par défaut du `swiper-container`.

De plus, le `swiper-container` n'a pas de `width` et de `height` spécifiques définis. Cela lui permet de prendre la taille par défaut du contenu dans le `swiper-slide`.

Notez également que le `swiper-container` et le `swiper-slide` sont stylisés comme un élément HTML réel sans point (`.`) pour la classe ou le signe dièse (`#`) pour l'id.

Votre code devrait ressembler à ceci lorsque vous l'exécutez dans votre navigateur :

![Styliser l'élément personnalisé Swiper et les classes](https://www.freecodecamp.org/news/content/images/2024/02/custom_styles.gif)

### Créer un nouveau nom de classe

Parfois, une seule page peut contenir plusieurs `<swiper-container>` qui résolvent différents problèmes, et chacun peut nécessiter ses propres styles. Créer un nouveau nom de classe peut être très utile pour fournir différentes options de style.

```jsx
<swiper-container className="image-swiper" >
            <swiper-slide >
                <img src="https://source.unsplash.com/slightly-opened-silver-macbook-mP7aPSUm7aE"  alt="" />
            </swiper-slide>
                
            <swiper-slide>
                <img src="https://source.unsplash.com/macbook-y0_vFxOHayg" alt="" />
            </swiper-slide>
 </swiper-container>
```

La classe `image-swiper` indique que l'élément Swiper est un slider d'images.

## Comment construire un élément Slider personnalisé

Swiper dispose de contrôles par défaut tels que la *navigation* et la *pagination*, ce qui facilite le contrôle des diapositives dans le `swiper-container`. La navigation et la pagination sont accompagnées de certaines icônes par défaut pour l'interaction utilisateur.

Par exemple, vous avez les icônes d'angle *gauche* et *droite* pour la navigation et les petites icônes de *puce* pour la pagination. Mais en fonction de votre conception ou des exigences de l'interface utilisateur pour un site web ou une application spécifique, cela peut nécessiter des modifications.

Voici une méthode simple pour implémenter des SVG personnalisés en tant qu'icônes de navigation et personnaliser la pagination pour une meilleure interaction utilisateur.

```jsx
export default function Usage() {

return (
    <>
    <main className="slider-main-container">
        <swiper-container

            navigation-next-el=".custom-next-button"
            navigation-prev-el=".custom-prev-button"
            pagination-clickable="true"
            pagination-dynamic-bullets="true"
            autoplay-delay="2000"
            autoplay-disable-on-interaction="false"
            center-slides="true"

            style={
                {
                "--swiper-pagination-color": "#fff",
                "--swiper-pagination-bullet-size": "15px",
                }
            }
        >
            <swiper-slide>
                <img src="https://source.unsplash.com/white-lamborghini-aventador-parked-in-building-7_OQMgoGzDw"  alt="" />
            </swiper-slide>
                
            <swiper-slide>
                <img src="https://source.unsplash.com/shallow-focus-photo-of-white-sedan-oN661Kw9ZOY" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/black-car-interior-4xM5cytsdMo" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/turned-on-monitor-inside-vehicle-tU-L__PI7gw" alt="" />
            </swiper-slide>

            <swiper-slide>
                <img src="https://source.unsplash.com/black-and-blue-vacuum-cleaner-rHfTdK9YU2Q" alt="" />
            </swiper-slide>

            {/* Navigations */}
        </swiper-container>

        <div className="nav-btn custom-prev-button">
          {/* <!-- https://feathericons.dev/?search=arrow-left&iconset=feather --> */}
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" className="main-grid-item-icon" fill="none" stroke="#fff" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2">
            <line x1="19" x2="5" y1="12" y2="12" />
            <polyline points="12 19 5 12 12 5" />
            </svg>
        </div>

        <div className="nav-btn custom-next-button">
             {/* <!-- https://feathericons.dev/?search=arrow-right&iconset=feather --> */}
             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" className="main-grid-item-icon" fill="none" stroke="#fff" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2">
            <line x1="5" x2="19" y1="12" y2="12" />
            <polyline points="12 5 19 12 12 19" />
        </svg>
        </div>
    </main>
    </>
)
}
```

Voici ce qui se passe dans le code ci-dessus :

- **navigation-next-el=".custom-next-button"** : utilisé pour spécifier l'élément personnalisé pour l'icône de navigation suivante.
- **navigation-prev-el=".custom-prev-button"** : utilisé pour spécifier l'élément personnalisé pour l'icône de navigation précédente.
- **pagination-clickable="true"** : active et définit la pagination sur un bouton cliquable.
- **pagination-dynamic-bullets="true"** : utilisé pour changer la présentation de la conception du bouton de pagination.
- **autoplay-delay="2000"** : active la lecture automatique des diapositives et leur répétition.
- **center-slides="true"** : définit la diapositive active au centre.

Les icônes SVG sont déclarées en dehors de l'élément `swiper-container` pour éviter qu'elles ne soient rognées à la première diapositive. La balise `<main>` est définie avec une classe `slider-wrapper` pour envelopper à la fois les éléments personnalisés du slider et les icônes SVG personnalisées.

J'ai ajouté un peu de CSS pour le style. Vous pouvez le copier ici.

```css
*,*::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: calibri;
}

body {
    display: flex;
    justify-content: center;
}

swiper-container {
    width: 800px;
    height: 400px;
    
}

.slider-main-container {
    position: relative;
}

swiper-slide {
   width: 100%;
   height: 100%;
}

swiper-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.nav-btn {
    display: block;
    position: absolute;
    z-index: 20;
    user-select: none;
    -webkit-user-select: none;
    background-color: rgba(0, 0, 0, 0.3);
    cursor: pointer;
    padding: 2px;
    border-radius: 5px;
    transition: background 0.5s ease;
}

.nav-btn:hover {
    background-color: rgb(255, 165, 0);
}

.nav-btn.custom-prev-button {
    top: 50%;
    left: 2em;
}

.nav-btn.custom-next-button {
    right: 2em;
    top: 50%;
}
```

Votre code devrait ressembler à ceci lorsque vous l'exécutez dans le navigateur :

![Personnaliser Swiper Element dans React](https://www.freecodecamp.org/news/content/images/2024/02/Custom_Slider_Elements.gif)

## Résumé

Swiper Element est une nouvelle façon de créer des sliders dans Swiper.js à partir de la nouvelle version 11.0.6.

Dans ce tutoriel, j'ai expliqué comment créer et implémenter le nouvel élément personnalisé Swiper dans une application React.

Vous avez vu quelques cas d'utilisation pour Swiper.js tels que la navigation, la pagination, les diapositives, les effets et les propriétés. Vous avez également appris comment personnaliser Swiper à partir de la conception par défaut pour lui donner un style plus professionnel.

Merci d'avoir lu !

### Références

1. [Documentation officielle de Swiper](https://swiperjs.com/)
2. [Documentation de Swiper Element](https://swiperjs.com/element)
3. [Référence de l'API Swiper](https://swiperjs.com/swiper-api)
4. [Démos du projet Swiper](https://swiperjs.com/demos)
5. [Problèmes Git de Swiper](https://github.com/nolimits4web/swiper/)