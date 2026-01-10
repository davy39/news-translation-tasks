---
title: Comment créer un panier d'achat avec React et TypeScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2023-06-23T17:09:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-shopping-cart-with-react-and-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/shopping-cart-app-article.png
tags:
- name: ecommerce
  slug: ecommerce
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment créer un panier d'achat avec React et TypeScript
seo_desc: 'In this tutorial we are going to build a real-life shopping cart 🛒 application.

  We''ll talk about the technology stack and the features it will have in a minute.
  I''ll also walk you through the process step-by-step. But first, let me show you
  what it''...'
---

Dans ce tutoriel, nous allons construire une application de panier d'achat 🛒 réelle.

Nous parlerons de la pile technologique et des fonctionnalités qu'elle aura dans un instant. Je vais également vous guider à travers le processus étape par étape. Mais d'abord, laissez-moi vous montrer à quoi cela va ressembler.

## Faisons un croquis 👋

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-214.png align="left")

*Liste des produits*

Nous allons rendre notre application mobile-friendly en implémentant un niveau décent de réactivité.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-215.png align="left")

*Liste des produits - Mobile*

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-216.png align="left")

*Panier Desktop*

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-217.png align="left")

*Panier Mobile*

Cette fois, avant de me lancer directement dans la construction de ce projet, j'ai décidé d'adopter une approche plus traditionnelle. J'ai pris un stylo et du papier et j'ai dessiné ces croquis peu esthétiques, juste pour m'assurer d'avoir une idée visuelle de ce que je vais construire.

Et honnêtement, cela a vraiment fait l'affaire ✨. Cette technique aide lorsque vous êtes sur le point de vous asseoir devant votre ordinateur et de vous poser la question :

> Par quoi commencer maintenant ?

### **TL;DR**

💡 Si vous voulez sauter la lecture, [ici](https://github.com/mihailgaberov/shopping-cart-app) 💁 est le dépôt GitHub avec un [README](https://github.com/mihailgaberov/shopping-cart-app/blob/main/README.md) 👍 détaillé, et ici vous pouvez voir la démo en direct [demo](https://shopping-cart-app-coral.vercel.app/).

## Qu'est-ce qu'un panier d'achat ?

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-218.png align="left")

*Paniers d'achat*

Un panier d'achat permet aux gens de transporter ou de stocker leurs marchandises pendant qu'ils font leurs achats – soit en ligne, soit dans la vie réelle.

Dans les applications de commerce électronique, le panier d'achat est un endroit où l'utilisateur peut stocker et consulter les articles qu'il envisage d'acheter. Typiquement, il s'agit d'une page séparée ou d'une partie de la page où les gens peuvent consulter une liste des articles qu'ils ont choisis d'acheter avant de les payer réellement.

## Le plan pour notre application

Nous allons construire une application composée de deux pages : une page de liste de produits et une page de panier.

L'application récupérera les données d'une API RESTful tierce et utilisera le localStorage du navigateur pour stocker les articles sélectionnés qui doivent être affichés dans le panier.

### Fonctionnalités de l'application

L'application de panier d'achat doit récupérer et afficher les produits à partir du point de terminaison de l'API [https://dummyjson.com/products](https://dummyjson.com/products).

La page Liste des produits doit afficher les articles disponibles ainsi que certaines informations spécifiques. Par exemple, elle doit afficher 3 produits par ligne pour les grands viewports. Chaque article doit afficher au moins une image miniature, un titre, le prix (formaté en GBP, par exemple £100.23), et un bouton « Ajouter au panier » qui ajoute l'article au panier.

La page Panier doit afficher les articles choisis par le client. Chaque article doit afficher au moins une image miniature, un titre, des boutons plus et moins (pour ajouter/supprimer des articles) et la quantité actuelle de l'article dans le panier, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-219.png align="left")

*Boutons plus et moins*

Si la quantité d'un article dans le panier est de 1, appuyer sur moins le supprime du panier. Le panier doit également afficher le prix total de tous les articles ajoutés (formaté en GBP, par exemple, £100.23).

En plus de ces fonctionnalités de base, l'UI/UX doit être aussi élégante que possible. Nous voulons également nous assurer de tester unitairement l'application.

### Pile technologique

Si vous avez eu l'occasion de jeter un œil à certains de mes autres tutoriels, la pile technologique que j'ai choisie ne vous surprendra pas beaucoup.

J'ai choisi ces technologies en tenant compte des exigences pour l'application – qu'elle soit performante, bien testée et qu'elle ait une apparence et une sensation élégantes.

* React / TypeScript / Vite – pour la bibliothèque UI, nous utilisons à nouveau React et un environnement de développement [Vite](https://cloudfour.com/thinks/in-praise-of-vite/). Mais cette fois, nous allons l'utiliser avec TypeScript au lieu de JavaScript.

* SASS / CSS Modules – pour styliser notre application, nous allons miser sur la solution éprouvée des [CSS Modules](https://github.com/css-modules/css-modules) avec [SASS/SCSS](https://sass-lang.com/documentation/).

* react-testing-library / Vitest – pour tester l'application, nous allons utiliser [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/) et [Vitest](https://vitest.dev/guide/).

Si vous voulez en savoir plus sur RTL, voici un tutoriel perspicace [tutoriel](https://www.robinwieruch.de/react-testing-library/) d'un gars très compétent [guy](https://www.robinwieruch.de/about/) qui peut vous aider.

## Comment construire l'application

Dans cette section, nous allons examiner la structure du projet et je vais expliquer pourquoi je l'ai choisie.

Ensuite, je vais passer brièvement en revue chacun des composants et décrire son rôle.

Une fois que vous comprendrez comment les composants fonctionnent ensemble pour créer une application fonctionnelle, nous explorerons comment utiliser le stockage local du navigateur pour stocker des données qui peuvent être utilisées dans d'autres parties de l'application.

### **📦 Dépendances**

Jetons un bref coup d'œil aux dépendances de notre projet. Il s'agit de packages externes que nous devons installer pour garantir l'exécution réussie de notre projet.

En plus de Vite et Vitest, j'ai installé SASS, React Testing Library et use-local-storage-state. Voir ci-dessous mon fichier [package.json](https://github.com/mihailgaberov/shopping-cart-app/blob/main/package.json).

```json
{
  "name": "shopping-cart-app",
  "private": false,
  "version": "1.0.0",
  "author": "Mihail Gaberov",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "test": "vitest",
    "build": "tsc && vite build",
    "lint": "eslint src --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.13.0"
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^14.0.0",
    "@types/react": "^18.0.37",
    "@types/react-dom": "^18.0.11",
    "@typescript-eslint/eslint-plugin": "^5.59.0",
    "@typescript-eslint/parser": "^5.59.0",
    "@vitejs/plugin-react": "^4.0.0",
    "eslint": "^8.38.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.3.4",
    "jsdom": "^22.1.0",
    "sass": "^1.63.4",
    "typescript": "^5.0.2",
    "use-local-storage-state": "^18.3.3",
    "vite": "^4.3.9",
    "vitest": "^0.32.0"
  }
}
```

### **🧑‍💻 Installation**

Dans cette étape, je suppose que vous partez de zéro. Nous allons utiliser Vite pour échafauder le projet. Pour ce faire, vous devez avoir Node.js installé sur votre système – au moins la version 14.18. Je vous suggère de le mettre à jour vers la dernière version stable. Et comme gestionnaire de paquets, vous pouvez choisir soit [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) soit [yarn](https://classic.yarnpkg.com/lang/en/docs/install/).

Une fois que vous avez installé l'un de ces gestionnaires sur votre système, ouvrez votre application Terminal et exécutez la commande suivante :

```bash
yarn create vite votre-nom-d-app --template react-ts
```

Cette commande installera les fichiers initiaux de l'application dans un dossier nommé 'votre-nom-d-app'. Après cette étape, vous pourrez l'ouvrir dans votre IDE préféré et commencer à travailler dessus.

Une dernière chose que vous devriez faire ici est d'installer les deux paquets supplémentaires que j'ai mentionnés dans la section précédente. Vous pouvez le faire en exécutant la commande suivante :

```bash
yarn add -D sass @testing-library/react use-local-storage-state
```

### **🏗️ Structure du projet**

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-220.png align="left")

*Structure du projet*

Cela ne sera pas une surprise pour ceux d'entre vous qui ont de l'expérience dans la construction d'applications React. La structure que j'ai choisie est assez standard.

Le niveau racine de l'application contient des fichiers liés aux configurations et à la mise en place, ainsi que le fichier index HTML. C'est ici que le module JavaScript principal est chargé et que l'application est lancée.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-221.png align="left")

*index.html*

Le dossier `src` (abréviation de "source") contient deux sous-dossiers : un pour les assets et un pour les composants.

Les dossiers `public` et `screenshots` ont des objectifs simples. Le dossier `.github` contient le fichier de configuration YAML qui est utilisé par [GitHub Actions](https://github.com/features/actions). Nous en discuterons plus en détail plus tard.

### **🖼️ Composants**

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-222.png align="left")

*Composants de l'application*

Tous les composants sont organisés dans des dossiers séparés. Dans chaque dossier, vous trouverez un fichier index.ts qui exporte le composant. Ce fichier utilise des [exports nommés](https://react.dev/learn/importing-and-exporting-components#default-vs-named-exports), comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-223.png align="left")

*Export nommé - Composant Header*

Nous allons commencer par examiner les composants selon une approche de haut en bas, tels qu'ils sont vus et utilisés dans l'application. Pour clarifier, laissez-moi vous fournir une visualisation.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-224.png align="left")

*Composants de l'application visualisés dans l'ordre*

Voici ce que fait chacun de ces composants en plus de détails :

[Header](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/Header) – contient la partie supérieure de l'application. Sur le côté gauche se trouve l'image du logo, un SVG que j'ai téléchargé depuis [Iconify](https://icon-sets.iconify.design/noto-v1/shopping-bags/). Sur le côté droit se trouve le composant CartWidget.

[CartWidget](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/CartWidget) – rend un bouton composé d'une image SVG représentant un panier d'achat et d'une valeur numérique indiquant le nombre de produits actuellement ajoutés au panier. Lorsque l'on clique dessus, le bouton emmène l'utilisateur à la page du panier.

[Products](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/Products) – ce composant est responsable de l'affichage du contenu principal de la page, qui consiste en une liste de produits. Sur les grands viewports, les produits sont affichés en trois colonnes par ligne. Chaque produit est représenté par une image miniature, un titre, des informations de prix et un bouton "Ajouter au panier". Le prix de chaque produit est formaté en GBP à l'aide du composant CurrencyFormatter.

[CurrencyFormatter](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/CurrencyFormatter) – formate un montant numérique donné en GBP – c'est-à-dire que 499 deviendrait £499.00.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-225.png align="left")

*Composants de l'application visualisés*

[Cart](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/Cart) – ce composant est responsable de l'affichage du contenu principal de la page. Il affiche un produit par ligne et inclut un composant quantificateur qui permet à l'utilisateur de mettre à jour la quantité du produit. En bas de la page, il affiche également le prix total des produits sélectionnés, qui est formaté en GBP à l'aide du composant CurrencyFormatter.

[Quantifier](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/Quantifier) – ce composant affiche des boutons plus et moins ainsi qu'un champ de saisie positionné entre eux. Il sert à indiquer la quantité actuelle d'un produit et permet à l'utilisateur de modifier cette valeur. De plus, il offre une fonctionnalité pour supprimer entièrement le produit du panier d'achat.

[Footer](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/Footer) – ce composant est conçu pour fournir une manière simple et visuellement représentative d'afficher des informations sur l'auteur et les droits d'auteur.

[Loader](https://github.com/mihailgaberov/shopping-cart-app/tree/main/src/components/Loader) – ce composant n'est pas visible sur les captures d'écran ci-dessus, mais il représente une simple animation de chargement qui devient visible une fois que l'utilisateur ouvre l'application pour la première fois et que les données des produits sont encore en cours de chargement.

### 🧑‍🔧 Comment construire l'en-tête

Comme mentionné précédemment, la section supérieure de l'application, communément appelée le "chapeau", est connue sous le nom d'en-tête. Dans notre cas spécifique, l'en-tête comprend deux éléments : le logo positionné à gauche et le CartWidget à droite.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-09.54.02.png align="left")

*En-tête de l'application*

Maintenant, passons en revue le processus de construction de l'application ensemble 👍. Les étapes décrites ci-dessous sont applicables à chaque composant que nous incorporons dans l'application.

Pour commencer, je crée un dossier dédié pour le composant et j'inclus un fichier index.ts à l'intérieur. Ce fichier servira de module d'exportation pour le composant.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-09.56.31.png align="left")

*Création du composant Header*

C'est ici que nous exportons le composant réel comme ceci :

```python
export { Header } from'./Header'
```

Ensuite, nous implémentons le composant lui-même. Ce code ira dans un fichier nommé de la même manière – `Header.tsx`

```python
import { FunctionComponent } from 'react'


export const Header: FunctionComponent = () => {
 
  return (
    <header>
      contenu de l'en-tête ici...
    </header>
  )
}
```

Nous commençons simplement.

Actuellement, ce composant n'affiche que le texte 'contenu de l'en-tête ici...' sur la page. Notre objectif est de l'améliorer progressivement jusqu'à obtenir le résultat final représenté dans l'image ci-dessus.

Pour ce faire, il est important d'incorporer le style dans le processus. En utilisant les CSS Modules, nous pouvons importer un fichier SCSS séparé contenant les styles nécessaires pour notre composant.

```typescript
import { FunctionComponent } from 'react'
import classes from './header.module.scss' // <---- importe les styles

export const Header: FunctionComponent = () => {
 
  return (
    <header>
      contenu de l'en-tête ici...
    </header>
  )
}
```

Ce fichier doit exister dans le dossier de notre composant. Après avoir inclus le fichier de tests, la structure du dossier pour ce composant ressemblera à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-10.16.21.png align="left")

*Dossier du composant Header*

Améliorons le code du composant en incorporant les éléments nécessaires. Sur le côté gauche, nous allons ajouter l'élément logo, qui fonctionnera comme un lien cliquable. Nous allons également inclure le composant `CartWidget` qui affiche le nombre de produits sélectionnés.

```typescript
import { FunctionComponent } from 'react'


export const Header: FunctionComponent = () => {
 
  return (
    <header className={classes.header}>
      <div>
        <Link to="/">
          <img src={logo} className={classes.logo} alt="Application de panier d'achat" />
        </Link>
      </div>
      <div>
        <CartWidget productsCount={productsCount} />
      </div>
    </header>
  )
}
```

Pour obtenir un bel aspect et une bonne réactivité, nous allons utiliser les styles suivants :

```scss
.header {
  width: 100%;
  display: flex;
  align-items: center;
  background-color: #213547;
  transition: height 0.3s ease;
  position: fixed;
  right: 0;
  left: 0;
  top: 0;
  opacity: 0.9;
  backdrop-filter: saturate(180%) blur(20px);
  justify-content: space-between;
  z-index: 1;

  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
    transform: scaleX(-1);


    &:hover {
      filter: drop-shadow(0 0 2em #646cffaa);
    }
  }
}
```

Je vais vous montrer le code du composant widget ci-dessous, mais avant cela, je veux que vous remarquiez comment nous passons la valeur du compte des produits en tant que prop. De cette façon, nous pouvons nous libérer de l'implémentation de toute logique dans le composant lui-même et l'utiliser uniquement à des fins de représentation.

Cela dit, voici le code du composant :

```python
import { FunctionComponent } from 'react'
import { useNavigate } from 'react-router-dom'

import shoppingCart from '../../assets/shopping-cart.svg'
import classes from './cart-widget.module.scss'

interface Props {
  productsCount: number
}

export const CartWidget: FunctionComponent<Props> = ({ productsCount }) => {
  const navigate = useNavigate()

  const navigateToCart = () => {
    navigate('/cart')
  }

  return (
    <button className={classes.container} onClick={navigateToCart}>
      <span className={classes.productsCount}>{productsCount}</span>
      <img src={shoppingCart} className={classes.shoppingCart} alt="Aller au panier" />
    </button>
  )
}
```

Et son style :

```scss
.container {
  margin: 1rem;
  padding: 0 1rem;
  display: flex;
  border: none;
  background: none;
  cursor: pointer;
  align-items: center;
  flex-direction: row-reverse;
  justify-content: space-between;

  &:hover {
    outline: 1px solid white;
  }


  .shoppingCart {
    height: 3em;
    padding: 1.5rem .4rem;
    will-change: filter;
    transition: filter 300ms;
  }

  .productsCount {
    z-index: 1;
    font-size: 2em;
    top: 38px;
    color: orange;
  }
}
```

#### Réduction de l'en-tête

Avant de continuer, il y a un autre aspect à discuter : l'animation de réduction fluide de l'en-tête que vous pouvez voir lors du défilement vers le bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screen-Recording-2023-06-22-at-10.50.40.gif align="left")

*Réduction de l'en-tête*

Pour accomplir cela, j'ai utilisé des hooks React ainsi qu'une technique impliquant la manipulation manuelle des styles pour divers éléments DOM.

J'ai implémenté cette fonctionnalité dans une méthode de composant appelée `shrinkHeader`, qui est invoquée chaque fois qu'un utilisateur fait défiler. Dans cette méthode, je vérifie si la position de défilement verticale actuelle dépasse une valeur de seuil spécifiée, `DISTANCE_FROM_TOP`, et j'applique différents styles en fonction du résultat de cette comparaison.

Un aspect que nous n'avons pas encore discuté est l'utilisation du hook pour gérer le stockage local, dont nous parlerons plus tard.

Voici la version complète du composant :

```python
import { FunctionComponent, useEffect } from 'react'
import { Link } from 'react-router-dom'
import useLocalStorageState from 'use-local-storage-state'

import logo from '/logo.svg'
import { CartWidget } from '../CartWidget'
import { CartProps } from '../Products/Products.tsx'
import classes from './header.module.scss'

export const Header: FunctionComponent = () => {
  useEffect(() => {
    window.addEventListener("scroll", () => shrinkHeader(), false)

    return () => {
      window.removeEventListener("scroll", () => shrinkHeader())
    }
  }, [])

  const shrinkHeader = () => {
    const DISTANCE_FROM_TOP = 140
    const headerElement = document.querySelector("header") as HTMLElement
    const logoElement = document.querySelectorAll("img")[0] as HTMLElement
    const cartWidgetElement = document.querySelectorAll("img")[1] as HTMLElement
    const productsCountElement = document.querySelector("span") as HTMLElement
    const scrollY = document.body.scrollTop || document.documentElement.scrollTop

    if (scrollY > DISTANCE_FROM_TOP) {
      headerElement.style.transition = "height 200ms ease-in"
      headerElement.style.height = "80px"
      logoElement.style.transition = "height 200ms ease-in"
      logoElement.style.height = "4rem"
      cartWidgetElement.style.transition = "height 200ms ease-in"
      cartWidgetElement.style.height = "2rem"
      productsCountElement.style.transition = "font-size 200ms ease-in"
      productsCountElement.style.fontSize = "1.5em"
    } else {
      headerElement.style.height = "150px"
      logoElement.style.height = "6rem"
      cartWidgetElement.style.height = "3rem"
      productsCountElement.style.fontSize = "2em"
    }
  }
  const [cart,] = useLocalStorageState<CartProps>('cart', {})

  const productsCount: number = Object.keys(cart || {}).length

  return (
    <header className={classes.header}>
      <div>
        <Link to="/">
          <img src={logo} className={classes.logo} alt="Application de panier d'achat" />
        </Link>
      </div>
      <div>
        <CartWidget productsCount={productsCount} />
      </div>
    </header>
  )
}
```

### 🧑‍🔧 Comment construire la liste des produits

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-11.03.49.png align="left")

*Liste des produits*

Pour construire le composant de liste des produits, j'ai suivi la même approche que ci-dessus. Initialement, j'ai établi la structure de base, qui impliquait de créer le code du composant, d'exporter le composant dans le fichier index et de mettre en œuvre un fichier SCSS séparé pour définir les styles du composant.

En conséquence, la structure du dossier après avoir terminé ces étapes devrait ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-11.06.23.png align="left")

*Dossier du composant Liste des produits*

Un aspect intéressant de ce composant est qu'il gère l'envoi d'une requête à une API REST afin de récupérer les données des produits. Cela est accompli grâce à la méthode `fetchData`, qui est invoquée dans un hook `useEffect`.

En spécifiant un tableau de dépendances vide, le code à l'intérieur du hook `useEffect` est exécuté une seule fois lorsque le composant est initialement chargé. Cela garantit que les requêtes redondantes sont évitées, optimisant ainsi les performances de notre application et réduisant l'utilisation de la bande passante.

```typescript
 useEffect(() => {
    fetchData(API_URL)
  }, [])


  async function fetchData(url: string) {
    try {
      const response = await fetch(url)
      if (response.ok) {
        const data = await response.json()
        setProducts(data.products)
        setIsLoading(false)
      } else {
        setError(true)
        setIsLoading(false)
      }
    } catch (error) {
      setError(true)
      setIsLoading(false)
    }
  }
```

L'aspect de rendu du composant est relativement simple. Une fois que nous avons réussi à récupérer les données des produits, nous pouvons les parcourir en utilisant une fonction `map()` régulière. Pour chaque produit, nous pouvons afficher son image miniature, son titre, son prix et un bouton pour l'ajouter au panier.

Pour garantir que chaque ligne affiche trois éléments lorsqu'ils sont vus sur de grands viewports, nous utilisons des styles CSS (SCSS). Nous allons le faire en exploitant les capacités de [Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox), comme démontré dans l'extrait suivant :

```scss
.productPage {
  padding: 1rem;
  margin-top: 8rem;

  .container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;

    .product {
      flex-basis: 33.33%;
      margin-bottom: 5rem;
      text-align: center;

      h3 {
        color: #007185;
        font-weight: 700;
        line-height: 20px;
        margin: 0;
      }

      img {
        height: 6rem;
      }

      button {
        background-color: #fbd815;
        width: 13rem;
        padding: .5rem;
        font-size: 1.1em;
        border-radius: 25px;
        border-color: #D5D9D9;
        border-style: solid;
        border-width: 1px;

        &:hover:not([disabled]) {
          background-color: #eecf1d;
          cursor: pointer;
        }

        &:disabled {
          opacity: .5;
          background-color: lightgray;
        }
      }
    }

    @media (max-width: 767px) {
      .product {
        flex-basis: 50%;
      }
    }

    @media (max-width: 400px) {
      .product {
        flex-basis: 100%;
      }
    }
  }
}

.error {
  color: red;
  text-align: center;
}
```

En plus de ces fonctionnalités, le code du composant inclut également une fonctionnalité pour gérer l'événement de clic sur le bouton "Ajouter au panier", spécifiquement pour ajouter l'article sélectionné au stockage local. Nous implémentons également une logique de gestion des erreurs de base pour afficher un message d'erreur en cas d'échec de la requête vers l'API tierce.

Voici le composant complet :

```typescript
import { FunctionComponent, useEffect, useState } from 'react'
import useLocalStorageState from 'use-local-storage-state'

import { CurrencyFormatter } from '../CurrencyFormatter'
import classes from './products.module.scss'
import { Loader } from '../Loader'

const API_URL = 'https://dummyjson.com/products'

export type Product = {
  id: number
  title: string
  price: number
  thumbnail: string
  image: string
  quantity: number
}

export interface CartProps {
  [productId: string]: Product
}

export const Products: FunctionComponent = () => {
  const [isLoading, setIsLoading] = useState(true)
  const [products, setProducts] = useState<Product[]>([])
  const [error, setError] = useState(false)
  const [cart, setCart] = useLocalStorageState<CartProps>('cart', {})


  useEffect(() => {
    fetchData(API_URL)
  }, [])


  async function fetchData(url: string) {
    try {
      const response = await fetch(url)
      if (response.ok) {
        const data = await response.json()
        setProducts(data.products)
        setIsLoading(false)
      } else {
        setError(true)
        setIsLoading(false)
      }
    } catch (error) {
      setError(true)
      setIsLoading(false)
    }
  }

  const addToCart = (product: Product):void => {
    product.quantity = 1

    setCart((prevCart) => ({
      ...prevCart,
      [product.id]: product,
    }))
  }

  const isInCart = (productId: number):boolean => Object.keys(cart || {}).includes(productId.toString())

  if (error) {
    return <h3 className={classes.error}>Une erreur s'est produite lors de la récupération des données. Veuillez vérifier l'API et réessayer.</h3>
  }

  if (isLoading) {
    return <Loader />
  }


  return (
    <section className={classes.productPage}>
      <h1>Produits</h1>

      <div className={classes.container}>
        {products.map(product => (
          <div className={classes.product} key={product.id}>
            <img src={product.thumbnail} alt={product.title} />
            <h3>{product.title}</h3>
            <p>Prix : <CurrencyFormatter amount={product.price} /></p>
            <button disabled={isInCart(product.id)} onClick={() => addToCart(product)}>Ajouter au panier</button>
          </div>
        ))}
      </div>
    </section>
  )
}
```

### 🧑‍🔧 Comment construire le panier

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-11.31.02.png align="left")

*Composant Panier*

Ce composant présente certaines similitudes avec le composant Liste des produits en ce sens qu'il liste également des produits, mais de manière différente avec un seul article par ligne.

Il introduit également une fonctionnalité supplémentaire en incorporant un autre composant pour mettre à jour la quantité des produits sélectionnés. Et il calcule le prix total de tous les produits dans le panier.

```typescript
 <section className={classes.cart}>
      <h1>Panier</h1>

      <div className={classes.container}>
        {getProducts().map(product => (
          <div className={classes.product} key={product.id}>
            <img src={product.thumbnail} alt={product.title} />
            <h3>{product.title}</h3>
            <Quantifier
              removeProductCallback={() => handleRemoveProduct(product.id)}
              productId={product.id}
              handleUpdateQuantity={handleUpdateQuantity} />
          </div>
        ))}
      </div>
      <TotalPrice amount={totalPrice} />
    </section>
```

La principale distinction ici est que, au lieu de récupérer les données des produits depuis une API, nous les récupérons depuis le stockage local. C'est ici que nous stockons les données de chaque produit sélectionné depuis le composant de liste des produits.

```typescript
const [cart, setCart] = useLocalStorageState<CartProps>('cart', {}) // lecture de la valeur du stockage local via le hook ici

....
....

  const getProducts = () => Object.values(cart || {}) // méthode pour obtenir toutes les données des produits sous forme de structure de données de tableau, ce qui nous permettra une itération plus facile plus tard
  
....
....
```

Dans ce cas, nous utilisons le hook `useEffect` une fois de plus, mais cette fois pour réinitialiser la position de défilement de la fenêtre chaque fois que l'utilisateur visite la page. Cela garantit que toutes les données pertinentes sont constamment visibles pour l'utilisateur, indépendamment de la distance à laquelle il a fait défiler sur la page de liste des produits.

```typescript

  useEffect(() => {
    window.scrollTo(0, 0)
  }, [location])
```

En effet, vous pouvez voir que les méthodes pour diminuer ou augmenter la quantité d'un produit sont passées au composant sous forme de callbacks via ses props. Cette approche est utile car elle aide à maintenir un composant relativement propre en élevant la responsabilité de la gestion de l'état à un niveau supérieur.

En élevant la logique de gestion de l'état en dehors du composant, cela permet une meilleure séparation des préoccupations et favorise la réutilisabilité.

```typescript
const handleRemoveProduct = (productId: number): void => {
    setCart((prevCart) => {
      const updatedCart = { ...prevCart }
      delete updatedCart[productId]
      return updatedCart
    })
  }

  const handleUpdateQuantity = (productId: number, operation: Operation) => {
    setCart((prevCart) => {
      const updatedCart = { ...prevCart }
      if (updatedCart[productId]) {
        if (operation === 'increase') {
          updatedCart[productId] = { ...updatedCart[productId], quantity: updatedCart[productId].quantity + 1 }
        } else {
          updatedCart[productId] = { ...updatedCart[productId], quantity: updatedCart[productId].quantity - 1 }
        }
      }
      return updatedCart
    })
  }
```

Nous pouvons styliser le composant en utilisant Flexbox pour obtenir notre mise en page souhaitée :

```scss
.cart {
  padding: 1rem;
  margin-top: 8rem;

  .container {
    display: flex;
    flex-direction: column;

    .product {
      display: flex;
      border-top: 1px dotted;
      border-left: 1px dotted;
      border-right: 1px dotted;
      padding: .3rem .5rem;
      align-items: center;

      h3 {
        color: #007185;
        font-weight: 700;
        font-size: 1em;
        line-height: 20px;
        margin: .3rem;
        flex: 1;
      }

      img {
        max-width: 3rem;
        height: auto;
        margin: .875rem;
      }
    }
  }
}
```

Voici la version finale du code du composant :

```typescript
import { FunctionComponent, useEffect } from 'react'
import useLocalStorageState from 'use-local-storage-state'

import { Quantifier } from '../Quantifier'
import { CartProps } from '../Products/Products.tsx'
import { TotalPrice } from '../TotalPrice'
import { Operation } from '../Quantifier/Quantifier.tsx'
import classes from './cart.module.scss'
import { useLocation } from 'react-router-dom'


export const Cart: FunctionComponent = () => {
  const [cart, setCart] = useLocalStorageState<CartProps>('cart', {})
  const location = useLocation()

  useEffect(() => {
    window.scrollTo(0, 0)
  }, [location])

  const handleRemoveProduct = (productId: number): void => {
    setCart((prevCart) => {
      const updatedCart = { ...prevCart }
      delete updatedCart[productId]
      return updatedCart
    })
  }

  const handleUpdateQuantity = (productId: number, operation: Operation) => {
    setCart((prevCart) => {
      const updatedCart = { ...prevCart }
      if (updatedCart[productId]) {
        if (operation === 'increase') {
          updatedCart[productId] = { ...updatedCart[productId], quantity: updatedCart[productId].quantity + 1 }
        } else {
          updatedCart[productId] = { ...updatedCart[productId], quantity: updatedCart[productId].quantity - 1 }
        }
      }
      return updatedCart
    })
  }


  const getProducts = () => Object.values(cart || {})

  const totalPrice = getProducts().reduce((accumulator, product) => accumulator + (product.price * product.quantity), 0)

  return (
    <section className={classes.cart}>
      <h1>Panier</h1>

      <div className={classes.container}>
        {getProducts().map(product => (
          <div className={classes.product} key={product.id}>
            <img src={product.thumbnail} alt={product.title} />
            <h3>{product.title}</h3>
            <Quantifier
              removeProductCallback={() => handleRemoveProduct(product.id)}
              productId={product.id}
              handleUpdateQuantity={handleUpdateQuantity} />
          </div>
        ))}
      </div>
      <TotalPrice amount={totalPrice} />
    </section>
  )
}
```

### 🧑‍🔧 Comment construire le pied de page

Pour améliorer l'apparence générale de l'application, j'ai inclus un composant de pied de page. Voici un exemple de son apparence :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/footer.png align="left")

L'implémentation du composant de pied de page est relativement simple. Il se compose de deux liens vers des plateformes sociales et d'un texte de copyright.

```typescript
import { FunctionComponent } from 'react'
import classes from "./footer.module.scss"
import packageJson from '../../../package.json'

export const Footer: FunctionComponent = () => {
  const currentYear = new Date().getFullYear()

  return (
    <footer className={classes.footer} data-cy="footer">
      <ul>
        <li className={classes.footerLinks}>
          <a
            href="https://twitter.com/mihailgaberov"
            target="_blank"
            rel="noopener noreferrer"
            data-cy="twitterLink"
          >
            twitter
          </a>{" 