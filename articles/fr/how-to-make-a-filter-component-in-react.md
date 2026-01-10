---
title: Comment créer un composant de filtre dans React
subtitle: ''
author: Ateev Duggal
co_authors: []
series: null
date: '2022-01-19T16:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-filter-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Filter-Component-1.png
tags:
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant de filtre dans React
seo_desc: 'Filter components are useful on websites because they help users find the
  results they need quickly and easily.

  This is especially true if your data comes from an API, since users cannot look
  through everything your app has to offer.

  In this article,...'
---

Les composants de filtre sont utiles sur les sites web car ils aident les utilisateurs à trouver rapidement et facilement les résultats dont ils ont besoin.

Cela est particulièrement vrai si vos données proviennent d'une API, car les utilisateurs ne peuvent pas tout parcourir ce que votre application a à offrir.

Dans cet article, nous utiliserons des données fictives que nous avons codées en dur et enregistrées comme un tableau dans un composant séparé nommé **Data.js.**

**Ce que nous allons couvrir ici :**

1. Introduction
   
2. Création de notre application React
   
3. Récupération des données de Data.js en utilisant les Hooks
   
4. Travail sur l'interface utilisateur de notre application
   
5. Création du composant de filtre
   
6. Conclusion

## Introduction

Pour ce projet particulier, nous utiliserons des données fictives sur la nourriture qui contiennent plusieurs paires clé-valeur comme montré dans ce code :

```json
const Data = [
  {
    id: "1",
    title: "Poha",
    category: "Petit-déjeuner",
    price: "$1",
    img: "https://c.ndtvimg.com/2021-08/loudr2go_aloo-poha_625x300_05_August_21.jpg?im=FeatureCrop,algorithm=dnn,width=620,height=350",
    desc: " Poha. Léger, nourrissant et facile à préparer, le poha est un célèbre petit-déjeuner qui est mangé presque partout dans le pays. Et le meilleur, c'est qu'il peut être préparé de nombreuses façons. Kanda poha, soya poha, Indori poha, Nagpur Tari Poha en sont quelques exemples",
  },
  {
    id: "2",
    title: "Upma",
    category: "Petit-déjeuner",
    price: "$1",
    img: "https://c.ndtvimg.com/2021-04/37hi8sl_rava-upma_625x300_17_April_21.jpg?im=FeatureCrop,algorithm=dnn,width=620,height=350",
    desc: " Un petit-déjeuner typique du Sud de l'Inde ! Préparé avec du dal d'urad riche en protéines et de la semoule, suivi de légumes croquants et de yaourt, cette recette constitue un repas copieux pour le matin. Avec un peu de noix de coco râpée sur le dessus, cela donne une belle saveur du Sud de l'Inde.",
  },
  {
    id: "3",
    title: "Cheela",
    category: "Petit-déjeuner",
    price: "$1",
    img: "https://c.ndtvimg.com/2019-05/1afu8vt8_weight-loss-friendly-breakfast-paneer-besan-chilla_625x300_25_May_19.jpg?im=FaceCrop,algorithm=dnn,width=620,height=350",
    desc: "Un aliment de base dans les foyers indiens, le moong dal est largement utilisé dans de nombreuses délicatesses indiennes. L'une de ces délicatesses est le moong dal cheela. Vous pouvez également ajouter du paneer à cette recette pour augmenter la valeur nutritionnelle et le rendre encore plus riche en protéines",
  },
  {
    id: "4",
    title: "Channa Kulcha",
    category: "Déjeuner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-04/chana-kulcha_625x350_41429707001.jpg",
    desc: "Un plat classique qui ne se démode jamais. Le chana kulcha quintessentiel nécessite seulement quelques ingrédients - poudre de cumin, gingembre, poudre de coriandre, poudre de carom, et un peu de poudre de mangue, ce qui donne au chana son goût aigre et tangy.",
  },
  {
    id: "5",
    title: "Egg Curry",
    category: "Déjeuner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2017-11/goan-egg-curry_620x350_41511515276.jpg",
    desc: "Les œufs sont un aliment polyvalent qui peut être cuisiné pour n'importe quel repas de la journée. Du petit-déjeuner au dîner, cela peut être un aliment de choix. Voici un curry d'œufs légèrement épicé fait avec de l'ail, des oignons, beaucoup de kasuri methi, de la crème fraîche, du yaourt et de la coriandre fraîche.",
  },
  {
    id: "6",
    title: "Paneer Aachari",
    category: "Déjeuner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-04/paneer_625x350_61429707960.jpg",
    desc: "Ne vous laissez pas intimider par la liste des ingrédients car non seulement ils sont déjà dans votre placard de cuisine, mais aussi parce qu'ils ne nécessiteront que 20 minutes de votre temps. Des morceaux de fromage cottage cuits dans des épices excitantes, du yaourt et une pincée de sucre.",
  },
  {
    id: "7",
    title: "Fish Fry",
    category: "Dîner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-06/indian-dinner_625x350_41434360207.jpg",
    desc: "Obtenez votre dose quotidienne de protéines parfaites. Des morceaux de poisson surmai marinés dans de l'ail, du cumin, du fenouil, des feuilles de curry et des tomates sont poêlés dans de l'huile raffinée et servis chauds. Cette recette de poisson frit utilise une variété d'épices délicieuses pour la marinade, lui donnant une touche unique.",
  },
  {
    id: "8",
    title: "Dum Alloo",
    category: "Dîner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-06/indian-dinner_625x350_51434362664.jpg",
    desc: "Votre famille vous remerciera pour ce fantastique bol de dum aloo cuisiné à la manière de Lucknow. Prenez quelques pommes de terre, du paneer émietté, du kasuri methi, du beurre, des oignons et un peu de ghee.",
  },
  {
    id: "9",
    title: "Malai Kofta",
    category: "Dîner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2017-10/makhmali-kofte_620x350_51508918483.jpg",
    desc: "Une sauce riche faite de khus khus, de noix de coco et de lait qui se marie parfaitement avec des koftas faits à partir de khoya. Cette recette veloutée et crémeuse vous laissera vous lécher les doigts. Makhmali kofte peut être votre plat de choix pour les dîners car cela est assez différent des autres recettes de kofta et extrêmement délicieux.",
  },
  {
    id: "10",
    title: "Malai Kofta",
    category: "Collations",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2017-10/makhmali-kofte_620x350_51508918483.jpg",
    desc: "Une sauce riche faite de khus khus, de noix de coco et de lait qui se marie parfaitement avec des koftas faits à partir de khoya. Cette recette veloutée et crémeuse vous laissera vous lécher les doigts. Makhmali kofte peut être votre plat de choix pour les dîners car cela est assez différent des autres recettes de kofta et extrêmement délicieux.",
  },
];
 
export default Data;
```

Parmi ces paires clé-valeur, nous avons également une catégorie qui sera utilisée pour filtrer les résultats.

Nous utiliserons Bootstrap comme CDN pour ce projet pour styliser notre application.

Après ce tutoriel, vous devriez en savoir plus sur la création et l'importation de composants dans React, sur l'utilisation dynamique des données, et surtout sur la façon de passer et d'utiliser des props entre les composants parents et enfants.

## Comment créer notre composant React

Il est très facile de créer une application React – allez simplement dans votre répertoire de travail dans l'un de vos IDE préférés et entrez la commande suivante dans le terminal :

```php
npx create-react-app react-filter-app
```

Si vous n'êtes pas sûr de la façon de configurer correctement un projet create-react-app, vous pouvez vous référer au guide officiel ici à [create-react-app-dev](https://create-react-app.dev/docs/getting-started/).

Après la configuration, exécutez `npm start` dans le même terminal pour démarrer le localhost:3000 où notre application React sera hébergée. Nous pouvons également voir toutes nos modifications là-bas.

## Comment obtenir les données de Data.js en utilisant les Hooks

Maintenant que nous avons réussi à configurer notre projet React, il est temps de récupérer nos données de Data.js et de les utiliser dans notre interface utilisateur.

Pour cela, nous devons d'abord importer nos données dans notre composant **App.js**, puis utiliser le hook useState pour gérer l'état de nos données.

```javascript
import React, { useState } from "react";
import Data from "./Data";
import Card from "./Card";
 
const App = () => {
  const [item, setItem] = useState(Data);
  return (
    <>
      <div className="container-fluid">
        <div className="row">
          <h1 className="col-12 text-center my-3 fw-bold">Notre Menu</h1>
          <Card item={item} /> // Composant UI
        </div>
      </div>
    </>
  );
};
 
export default App;
```

## Comment construire la partie UI de notre application

Maintenant que nous avons nos données stockées dans une variable que nous pouvons utiliser librement dans notre application, nous pouvons travailler sur l'interface utilisateur.

L'interface utilisateur contiendra des [cartes Bootstrap](https://getbootstrap.com/docs/5.0/components/card/) que nous créerons dynamiquement en utilisant la fonction map.

Nous créerons un composant différent pour nos cartes. Comme vous pouvez le voir dans le code ci-dessus, nous l'avons nommé **Card.js** et l'avons également importé. Nous avons également passé **item** en tant que props afin de pouvoir utiliser les données stockées dans l'item dans le composant de carte.

Ce composant contiendra toutes nos cartes et les données que nous afficherons dynamiquement dans notre application en utilisant la **fonction map.**

```javascript
import React from "react";
 
const Card = ({ item }) => {            
           // déstructuration des props
  return (
    <>
      <div className="container-fluid">
        <div className="row justify-content-center">
          {item.map((Val) => {
            return (
              <div
                className="col-md-4 col-sm-6 card my-3 py-3 border-0"
                key={Val.id}
              >
                <div className="card-img-top text-center">
                  <img src={Val.img} alt={Val.title} className="photo w-75" />
                </div>
                <div className="card-body">
                  <div className="card-title fw-bold fs-4">
                    {Val.title} &nbsp;&nbsp;&nbsp;&nbsp;--&nbsp;&nbsp;
                    {Val.price}
                  </div>
                  <div className="card-text">{Val.desc}</div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
};
 
export default Card;
```

Notre application avec 10 cartes ressemblera à ceci :

![Image](https://lh5.googleusercontent.com/dcZ-3eTALXbuRdMYsDgy672KsDcuN7D--QbHOl5_2xNjocun5-zAONVPFqD8txXpVvbyKNNBV6rjEi5JAIceQzMy-K-D1OOOjWkKs59EzlRzf-VBkjwz3LxY2I8E4FBL6Bn4vrf5 align="left")

## Comment créer le composant de filtre

Il existe de nombreuses façons d'utiliser les composants de filtre pour filtrer les données que l'utilisateur obtient à partir des résultats de recherche. Mais ici, nous allons créer des boutons à cette fin qui filtreront les données en fonction de la catégorie de cet aliment – comme le petit-déjeuner, le déjeuner, le dîner et les collations.

Nous devons créer un nouveau tableau qui contiendra uniquement les valeurs de la clé catégorie et les afficher en utilisant la méthode map.

```javascript
// l'opérateur de décomposition affichera toutes les valeurs de notre section catégorie de nos données tandis que Set ne permettra qu'à une seule valeur de chaque type d'être affichée

  const menuItems = [...new Set(Data.map((Val) => Val.category))];
```

Nous utilisons ici l'**opérateur de décomposition** afin que chaque valeur que nous obtenons en affichant le tableau ci-dessus ait la même interface utilisateur, et aussi pour afficher toutes les 10 catégories sous forme de boutons.

Nous utilisons la valeur `Set()` afin que seules 3 ou 4 valeurs uniques soient affichées et aussi pour garantir qu'il n'y a pas de valeurs répétées.

Nous allons créer un nouveau composant pour ces boutons qui seront affichés dynamiquement en utilisant la méthode map. Mais cette fois, nous utiliserons notre nouveau tableau car il contient toutes les catégories stockées dans un tableau et les affichera une seule fois grâce à **Set()**.

```javascript
import React from "react";
import Data from "./Data";
 
const Buttons = ({ setItem, menuItems }) => {
  return (
    <>
      <div className="d-flex justify-content-center">
        {menuItems.map((Val, id) => {
          return (
            <button
              className="btn-dark text-white p-1 px-2 mx-5 btn fw-bold"
              key={id}
            >
              {Val}
            </button>
          );
        })}
        <button
          className="btn-dark text-white p-1 px-3 mx-5 fw-bold btn"
          onClick={() => setItem(Data)}
        >
          Tout
        </button>
       </div>
    </>
  );
};
 
export default Buttons;
```

Placez ce composant de bouton là où vous souhaitez afficher les boutons. Dans notre cas, nous avons affiché les boutons au-dessus de notre composant de carte dans app.js.

![Image](https://lh5.googleusercontent.com/gX2PTVbyYQIJ-6o_WvhHZVucTJwEZhQz0moqf7GZoC68fcgC2iORyLyqRILAmhQn-e_SQy172o1_BgeLMidY69Jm3UCAXtRBiP-fNwFf50VaJPj8_54SjjlngVvCun_EaOVG-DRh align="left")

Il est temps d'ajouter un filtre à ces boutons afin qu'ils puissent filtrer les plats en fonction de la catégorie.

```javascript
const filterItem = (curcat) => {
    const newItem = Data.filter((newVal) => {
      return newVal.category === curcat; 
        	// comparaison de la catégorie pour afficher les données
    });
    setItem(newItem);
  };
```

La méthode filter filtre les données en fonction de la catégorie de cet objet.

En utilisant le gestionnaire d'événements `onClick()`, nous pouvons attacher ce filtre à nos boutons :

```javascript
import React from "react";
import Data from "./Data";
 
const Buttons = ({ filterItem, setItem, menuItems }) => {
  return (
    <>
      <div className="d-flex justify-content-center">
        {menuItems.map((Val, id) => {
          return (
            <button
              className="btn-dark text-white p-1 px-2 mx-5 btn fw-bold"
              onClick={() => filterItem(Val)}
              key={id}
            >
              {Val}
            </button>
          );
        })}
        <button
          className="btn-dark text-white p-1 px-3 mx-5 fw-bold btn"
          onClick={() => setItem(Data)}
        >
          Tout
        </button> 
       </div>
    </>
  );
};
 
export default Buttons;
```

## Conclusion

Il existe de nombreuses façons d'utiliser un composant de filtre pour réduire le temps que nos utilisateurs perdent à rechercher des résultats idéaux dans nos applications.

Il n'y a que 10 objets dans le tableau que nous avons utilisé dans cette application, mais souvent nous obtenons nos données à partir d'une API, où il peut y avoir des tonnes de données. Dans ces cas, une seule recherche n'est souvent pas idéale pour donner des résultats exacts, donc nous utilisons des filtres pour aider.

Vous pouvez voir le code complet dans le [Dépôt GitHub](https://github.com/Ateevduggal/Filter-Menu-in-React), et vous pouvez vérifier comment ces boutons de filtre fonctionnent en consultant un [lien live](https://filter-menu-in-react.vercel.app/) de l'application.

Vous pouvez également consulter mes autres projets :

1. [Comment créer un composant de pagination dans React en utilisant les Hooks](https://tekolio.com/how-to-make-custom-pagination-in-react-js-with-hooks/)
   
2. [Comment créer une application de dictionnaire dans React en utilisant les Hooks](https://tekolio.com/how-to-create-a-dictionary-app-in-react/)
   
3. [Comment héberger une application React sur GitHub Pages avec un domaine personnalisé](https://tekolio.com/how-to-host-a-react-app-on-github-pages-with-a-custom-domain/)