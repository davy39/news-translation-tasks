---
title: Comment implémenter la révélation au défilement dans React en utilisant l'API
  Intersection Observer
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-03-23T22:20:44.000Z'
originalURL: https://freecodecamp.org/news/reveal-on-scroll-in-react-using-the-intersection-observer-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Group-107.png
tags:
- name: animation
  slug: animation
- name: api
  slug: api
- name: React
  slug: react
seo_title: Comment implémenter la révélation au défilement dans React en utilisant
  l'API Intersection Observer
seo_desc: 'Are you looking for an elegant way to reveal content on your React website
  as users scroll down the page? Look no further than the Intersection Observer API.

  In this article, you’ll learn how to implement the reveal on scroll effect in React
  using In...'
---

Cherchez-vous un moyen élégant de révéler du contenu sur votre site React au fur et à mesure que les utilisateurs font défiler la page ? Ne cherchez pas plus loin que l'API Intersection Observer.

Dans cet article, vous apprendrez à implémenter l'effet de révélation au défilement (reveal on scroll) dans React à l'aide d'Intersection Observer. Cela vous permettra de créer des expériences utilisateur dynamiques et époustouflantes qui captiveront vos visiteurs.

Ce guide étape par étape vous aidera à comprendre cette technique en un rien de temps, propulsant vos compétences en développement React au niveau supérieur.

## Prérequis

* Fondamentaux du HTML et du CSS
* Fondamentaux de JavaScript et de l'API Intersection Observer de JavaScript
* Connaissances fondamentales de React
* Un éditeur de code, un navigateur (de préférence un qui prend en charge l'API Intersection de JavaScript, comme Google Chrome) et Node.js

## Qu'est-ce que l'API Intersection Observer ?

Intersection Observer est une API Web qui permet aux développeurs de détecter quand un élément spécifique entre en intersection avec un autre élément ou avec le viewport (la zone d'affichage du navigateur).

Vous pouvez utiliser cette API pour surveiller tout changement dans la visibilité d'un élément lorsqu'il croise un autre élément, ou lorsqu'il entre ou sort du viewport.

### Comment fonctionne l'API Intersection Observer

Intersection Observer surveille d'abord une intersection (soit entre deux éléments, soit entre un élément et le viewport du navigateur). Lorsqu'il détecte une intersection, la fonction de l'observateur déclenche une fonction de rappel (callback) qui indique au code la marche à suivre.

## Comment implémenter l'API Intersection Observer dans React

Cette section se compose de trois parties :

1. Configurer votre environnement React
2. Ajouter le code de base (boilerplate) et les styles
3. Implémenter la fonctionnalité de révélation au défilement

### Comment configurer votre environnement React :

Tout d'abord, vous devrez configurer un environnement React en exécutant `npx create-react-app [nom-de-votre-projet]`, soit dans votre terminal natif, soit dans le terminal d'un IDE.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/001-npx-cra.png)
_Commande pour créer votre application React_

Si vous avez choisi d'utiliser un terminal natif, l'étape suivante consistera à ouvrir ce dossier avec votre IDE préféré. Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/002-after-cra.png)
_Ouverture du fichier dans votre IDE_

### Comment ajouter le code de base et les styles

Ensuite, effacez tous les styles par défaut et débarrassez-vous de tous les fichiers et imports inutiles pour ce projet. La structure de votre dossier devrait alors ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/003-after-clearing-unnecessary-things.png)
_Structure du dossier de l'application React_

Pour le composant `App`, vous créerez trois éléments enfants (_header_, _main_ et _footer_). C'est nécessaire car cela vous permet de mieux comprendre l'effet de révélation au défilement lorsque vous arrivez depuis le _header_ et ressortez par le _footer_.

```js 
import './App.css'
function App()
{  return 
(    <div className="App">  
        <header>Ceci est le Header</header>
        <main>
            <div className="child-one">Enfant Un</div>
            <div className="child-two">Enfant Deux</div>
        </main>      
        <footer>Ceci est le Footer</footer>
      </div>  );
}
      
export default App;
```

Ensuite, appliquez ces styles dans le fichier App.css pour organiser la mise en page de votre application.

```css
@import url("https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation:wght@500&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.App {
  width: 100%;
  height: 100%;
  background: #fff;
  font-family: "Edu NSW ACT Foundation", cursive;
}

body {
  font-size: 50px;
}

header,
footer {
  box-shadow: 3px 5px 5px rgba(0, 0, 0, 0.3);
  height: 100vh;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

footer {
  margin-top: 50px;
  box-shadow: -3px -5px 5px rgba(0, 0, 0, 0.3);
}

main {
  box-shadow: 3px 5px 5px rgba(0, 0, 0, 0.3), -3px -5px 5px rgba(0, 0, 0, 0.3);
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 50px;
  gap: 50px;
  overflow: hidden;
}

main div {
  flex: 1;
  height: 80%;
  border: 2px solid #999;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  transition: all ease-in 1s;
}

.slide-in {
  transform: translateX(0) !important;
}

```

Votre projet devrait actuellement ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/001-Initial-styling.gif)
_Mise en page après application des styles_

### Comment implémenter la fonctionnalité de révélation au défilement

Tout d'abord, vous devez créer un état (state) qui contient la valeur d'intersection actuelle – c'est-à-dire, si l'élément surveillé est en intersection avec quelque chose ou non.

```js
import { useState} from "react";
export default function test() {
  const [isIntersecting, setIsIntersecting] = useState(false);
```

La valeur initiale de l'état est définie sur _false_, et passe à _true_ lorsqu'une intersection se produit.

Ensuite, vous créez une référence à l'aide du hook `useRef`, que vous attacherez ensuite à l'élément que vous souhaitez référencer. Ce hook est utilisé pour stocker une référence à un élément du DOM (similaire à ce que vous obtiendriez avec `document.querySelector`), vous permettant d'accéder et de manipuler l'élément directement si nécessaire.

```js
import { useState, useRef } from "react";
function App() {
  const [isIntersecting, setIsIntersecting] = useState(false);

  const ref = useRef(null);

  return (
    <div className="App">
      <header>Ceci est le Header</header>
      <main ref={ref}>
        <div className="child-one">Enfant Un</div>
        <div className="child-two">Enfant Deux</div>
      </main>
      <footer>Ceci est le Footer</footer>
    </div>
  );
}

export default App;
```

Ensuite, vous utilisez un hook `useEffect` pour créer une instance d'intersection observer qui surveille les intersections.

```js
import { useState, useRef, useEffect} from "react"; 

useEffect(() => {
    const observer = new IntersectionObserver();
  }, []);
```

Après cela, vous passerez une fonction de rappel qui met à jour l'état d'intersection.

```js
 useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsIntersecting(entry.isIntersecting);
      }
    );
  }, []);
```

Gardez à l'esprit que nous avons déstructuré le tableau d'entrées (`entries`) pour obtenir la première valeur, c'est-à-dire la première intersection.

Ensuite, vous fournissez un objet d'options comme second argument à la fonction `IntersectionObserver`.

L'objet d'options peut avoir plusieurs propriétés, dont la propriété `rootMargin`. La valeur de `rootMargin` définit les marges autour de l'élément observé, étendant ou contractant ainsi sa boîte englobante. La fonction de l'observateur se déclenche lorsque la boîte englobante ajustée entre ou sort de l'intersection avec l'élément racine spécifié.

```js
useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsIntersecting(entry.isIntersecting);
      },
      { rootMargin: "-300px" }
    );
  }, []);
```

**Note** : Il est important de noter que si vous spécifiez une valeur négative pour `rootMargin`, la fonction de l'observateur se déclenchera alors que l'élément observé est déjà partiellement visible. Par exemple, une valeur de `-300px` signifie que la fonction de l'observateur se déclenchera lorsque 300 pixels de l'élément observé seront entrés dans le champ de vision.

L'étape suivante consiste à appeler la méthode `observe` sur l'objet `observer` pour indiquer l'élément actuel que vous observez.

```js
useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsIntersecting(entry.isIntersecting);
      },
    );
    observer.observe(ref.current);
  }, []);
```

Avec cela, vous avez configuré votre instance d'observateur. Tout ce qu'il reste à faire dans ce hook est de créer une fonction de nettoyage (cleanup function) qui interrompt l'observation lorsque l'élément observé est démonté.

```js
 useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);
```

Testons si notre fonction d'observation fonctionne correctement en affichant la valeur actuelle de `isIntersecting` dans la console.

```js
useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    });
    console.log(isIntersecting);
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/002-Test-intersection.gif)
_Test des intersections avec la console du navigateur_

Comme vous pouvez le voir, lors du premier chargement de la page, la valeur de `isIntersecting` est _false_ car aucune intersection ne s'est produite. À mesure que vous faites défiler la page et que vous voyez votre élément cible, la valeur passe à _true_, et lorsque vous quittez l'élément, la valeur repasse à _false_.

Pour obtenir l'effet de révélation au défilement souhaité, il est crucial de déplacer d'abord les deux divs enfants hors du viewport. Cela vous permettra de les faire revenir lorsque `isIntersecting` est _true_, c'est-à-dire pendant l'intersection, ce qui est l'étape clé pour créer l'effet.

```css
main div:first-child {
  transform: translateX(-150%);
  opacity: 0;
}
main div:last-child {
  transform: translateX(150%);
  opacity: 0;
}
```

Ensuite, vous utilisez un second hook `useEffect` pour gérer la logique de l'apparition de nos divs enfants. Vous vérifiez d'abord s'il y a une intersection :

```js
 useEffect(() => {
    if (isIntersecting) {
     
    }
  }, []);
```

Ensuite, vous ciblez tous les éléments enfants à l'intérieur de l'élément observé, vous bouclez sur eux et vous ajoutez une classe CSS qui les révèle.

```css
.slide-in {
  transform: translateX(0) !important;
  opacity: 1 !important;
}
```

```js
 useEffect(() => {
    if (isIntersecting) {
      ref.current.querySelectorAll("div").forEach((el) => {
        el.classList.add("slide-in");
      });
    }
  }, [isIntersecting]);
```

**Note** : Puisqu'un changement dans la valeur de `isIntersecting` provoque le rendu du hook `useEffect`, nous le passons comme dépendance dans le tableau de dépendances.

Jetons un coup d'œil à ce que vous avez accompli jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/003-Initial-intersection.gif)
_Premier effet de révélation au défilement obtenu_

Et voilà, vous avez implémenté la fonctionnalité de révélation au défilement – félicitations !
Il ne reste plus qu'à faire en sorte que les éléments enfants quittent le viewport dès qu'il n'y a plus d'intersection.

```js
useEffect(() => {
    if (isIntersecting) {
      ref.current.querySelectorAll("div").forEach((el) => {
        el.classList.add("slide-in");
      });
    } else {
      ref.current.querySelectorAll("div").forEach((el) => {
        el.classList.remove("slide-in");
      });
    }
  }, [isIntersecting]);
```

Cela nous donne l'effet final :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/004-Final-intersection.gif)
_L'effet final de révélation au défilement obtenu_

Le code complet final est affiché ci-dessous :

```js
import "./App.css";

import { useState, useRef, useEffect } from "react";

function App() {
  const [isIntersecting, setIsIntersecting] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsIntersecting(entry.isIntersecting);
      },
      { rootMargin: "-300px" }
    );
    console.log(isIntersecting);
    observer.observe(ref.current);

    return () => observer.disconnect();
  }, [isIntersecting]);

  useEffect(() => {
    if (isIntersecting) {
      ref.current.querySelectorAll("div").forEach((el) => {
        el.classList.add("slide-in");
      });
    } else {
      ref.current.querySelectorAll("div").forEach((el) => {
        el.classList.remove("slide-in");
      });
    }
  }, [isIntersecting]);

  return (
    <div className="App">
      <header>Ceci est le Header</header>
      <main ref={ref}>
        <div className="child-one">Enfant Un</div>
        <div className="child-two">Enfant Deux</div>
      </main>
      <footer>Ceci est le Footer</footer>
    </div>
  );
}

export default App;
```

## Autres options

Il convient de mentionner que bien que l'utilisation de l'Intersection Observer pour les animations au défilement soit efficace, il existe des approches plus récentes pour implémenter des animations de révélation dans React. Ces approches incluent l'utilisation de bibliothèques d'animation telles que [Framer Motion](https://www.framer.com/motion/) et [GSAP](https://greensock.com/gsap/).

Ces bibliothèques offrent aux développeurs un moyen simple de créer des animations fluides et attrayantes tout en garantissant des performances élevées.

## Conclusion

L'API Intersection Observer est un outil efficace pour développer des interfaces utilisateur attrayantes en développement Web. Vous pouvez ajouter une couche supplémentaire d'interactivité à vos applications Web en implémentant des effets de révélation au défilement dans React avec cette API.

Dans ce tutoriel, nous avons couvert les bases de l'utilisation de l'API Intersection Observer dans React, de la configuration de votre environnement à l'ajout de styles et de fonctionnalités.

À l'avenir, vous pourrez utiliser les connaissances et les compétences acquises dans ce tutoriel pour enrichir votre savoir-faire en développement Web et créer des interfaces utilisateur époustouflantes et dynamiques qui inciteront vos utilisateurs à revenir.

### Liens du projet

* URL du site en direct : [Netlify](https://react-intersection-api-article.netlify.app/)
* Dépôt de code : [GitHub](https://github.com/Daiveedjay/React-Intersection-API-article)

### Autres ressources

Comme cet article n'est pas centré sur le fonctionnement complet de l'API Intersection Observer, voici quelques ressources qui peuvent vous aider à mieux la comprendre.

* [Implémenter le lazy loading des images pour améliorer les performances du site Web en utilisant JavaScript](https://daiveedjay.hashnode.dev/implementing-image-lazy-loading-to-improve-website-performance-using-javascript)
* [API Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
* [Guide ultime de l'Intersection Observer JavaScript](https://blog.webdevsimplified.com/2022-01/intersection-observer/)