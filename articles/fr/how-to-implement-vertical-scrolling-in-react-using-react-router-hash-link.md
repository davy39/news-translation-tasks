---
title: Comment implémenter le défilement vertical dans React en utilisant react-router-hash-link
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-09-27T17:42:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-vertical-scrolling-in-react-using-react-router-hash-link
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/ferenc-almasi-L8KQIPCODV8-unsplash.jpeg
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Comment implémenter le défilement vertical dans React en utilisant react-router-hash-link
seo_desc: 'Smooth scrolling is a feature that makes webpages more usable and allows
  for a better user scrolling experience in most browsers.

  Implementing a smooth page scroll while using react-router-dom has been a problem
  in React.js. So this article, you are ...'
---

Le défilement fluide (smooth scrolling) est une fonctionnalité qui rend les pages web plus utilisables et permet une meilleure expérience de défilement pour l'utilisateur dans la plupart des navigateurs.

L'implémentation d'un défilement de page fluide lors de l'utilisation de react-router-dom a été un problème dans React.js. Dans cet article, vous allez apprendre à implémenter un défilement vertical fluide à l'aide du package react-router-hash-link.

### Qu'est-ce que react-router-hash-link ?

Selon sa [documentation](https://github.com/rafgraph/react-router-hash-link), react-router-hash-link est une solution au problème de React Router qui ne défile pas vers les #hash-fragments lors de l'utilisation de composants de lien pour naviguer.

### Prérequis.

Vous devez utiliser _BrowserRouter_ de react-router-dom pour que le défilement fluide de react-router-hash-link fonctionne. Pour installer et utiliser react-router, entrez la commande suivante :

```js
npm i react-router-dom 
```

Ou pour yarn :

```js
yarn add react-router-dom 
```

Pour comprendre comment implémenter le défilement vertical, vous allez créer une page d'atterrissage simple avec une barre de navigation et trois sections.

## Comment utiliser react-router-hash-link

### Étape 1 : Installer react-router-hash-link

Pour installer le package react-router-hash-link, exécutez la commande suivante :

```js
npm install --save react-router-hash-link
```

Ou avec yarn :

```js
yarn add react-router-hash-link
```

### Étape 2 : Importer le package react-router-hash-link dans votre application React.

Ouvrez votre fichier LandingPage.js et importez _hashlink_ depuis votre package react-router-hash-link.

```js
import React from 'react';
import { HashLink } from 'react-router-hash-link';

const LandingPage = () => {
    return (
        <>
            <nav>
            . . .
            </nav>

            <section>
            . . .
            </section>
        </>
    )
}

export default LandingPage 
```

### Étape 3 : Ajouter le composant Hashlink pour pointer vers différentes zones de votre application

Ajoutez le composant Hashlink à votre fichier LandingPage.js comme ceci :

```js
import React from 'react';
import { HashLink } from 'react-router-hash-link';

const LandingPage = () => {
    return (
    <>
        <nav>
            <HashLink smooth to="/#home">
                À propos
            </HashLink>
        
            <HashLink smooth to="/#services">
            	Profil
            </HashLink>
        
            <HashLink smooth to="/#testimonial">
            	Services
            </HashLink>
        </nav>
        
        <section>
        . . .
        </section>
    </>
    )
}
export default LandingPage 
```

### Étape 4 : Ajouter l'ID de votre Hashlink à n'importe quel élément.

Lorsque vous cliquez sur le lien avec votre identifiant, un effet de défilement sera implémenté. Vous verrez un défilement vers l'élément ou la page qui possède un identifiant correspondant au #hashfragment dans le lien.

```js
import React from 'react';
import { HashLink } from 'react-router-hash-link';

const LandingPage = () => {

    return (
    <>
        <nav>
            <HashLink smooth to="/#home">
            	À propos
            </HashLink>
            
            <HashLink smooth to="/#services">
            	Profil
            </HashLink>
            
            <HashLink smooth to="/#testimonial">
            	Services
            </HashLink>
        </nav>
        
        <section id=”about”>
        	<h1> À propos</h1>
            
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Vero, nam! Iure officia aut esse tempore accusantium
                explicabo? Corporis deleniti ipsa fuga quas aut neque
                dicta nostrum laboriosam, iusto ullam minima est porro,
                totam saepe. Facilis aliquid praesentium, voluptates rem
                quibusdam sequi numquam illo eius adipisci eaque,
                necessitatibus consectetur, labore vero et ipsum.
                Officiis, ea vero. Praesentium, et. Enim, nostrum illo.
            </p>        
        </section>
        
        <section id=”profile”>
        	<h1> Profil </h1>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Vero, nam! Iure officia aut esse tempore accusantium
                explicabo? Corporis deleniti ipsa fuga quas aut neque
                dicta nostrum laboriosam, iusto ullam minima est porro,
                totam saepe. Facilis aliquid praesentium, voluptates rem
                quibusdam sequi numquam illo eius adipisci eaque,
                necessitatibus consectetur, labore vero et ipsum.
                Officiis, ea vero. Praesentium, et. Enim, nostrum illo.
            </p>
        </section>
        
        <section id=”services”>
        	<h1> Services </h1>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Vero, nam! Iure officia aut esse tempore accusantium
                explicabo? Corporis deleniti ipsa fuga quas aut neque
                dicta nostrum laboriosam, iusto ullam minima est porro,
                totam saepe. Facilis aliquid praesentium, voluptates rem
                quibusdam sequi numquam illo eius adipisci eaque,
                necessitatibus consectetur, labore vero et ipsum.
                Officiis, ea vero. Praesentium, et. Enim, nostrum illo.
            </p>
        </section>
    </>
    )
}

export default LandingPage 
```

Et voilà ! Vous avez maintenant implémenté le défilement fluide sur une page web simple.

## Conclusion

React-router-hash-link vous permet de tirer parti du défilement fluide de manière transparente tout en utilisant react-router-dom pour le routage.

Il possède de nombreuses fonctions, notamment les fonctions "Scroll to top" (Défilement vers le haut) et "Scroll with offset" (Défilement avec décalage), vous pouvez donc explorer tout ce qu'il peut faire.