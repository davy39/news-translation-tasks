---
title: Comment accepter les paiements avec React et Stripe
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-09-16T18:55:26.000Z'
originalURL: https://freecodecamp.org/news/react-stripe-payments
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/mugshotbot.com_customize_color-blue-image-00471e9c-mode-light-pattern-bank_note-theme-two_up-url-https___freecodecamp.org.png
tags:
- name: payments
  slug: payments
- name: React
  slug: react
seo_title: Comment accepter les paiements avec React et Stripe
seo_desc: "Payments are an essential part of any online business. But the process\
  \ of setting up those payments can be incredibly complex at times. \nTo accept payments,\
  \ developers were traditionally required to set up code both on the client and server.\
  \ This was..."
---

Les paiements sont une partie essentielle de toute entreprise en ligne. Mais le processus de configuration de ces paiements peut parfois être incroyablement complexe.

Pour accepter les paiements, les développeurs devaient traditionnellement configurer du code à la fois sur le client et le serveur. Cela s'ajoutait à l'apprentissage d'API tierces complexes qui nécessitaient de parcourir une grande quantité de documentation.

Heureusement, des outils comme Stripe Checkout rendent la gestion des achats sur le web et les appareils mobiles plus facile que jamais.

Dans ce tutoriel, vous allez découvrir comment configurer Stripe Checkout pour accepter les paiements par carte de crédit, Apple Pay et Google Pay dans nos applications React.

## Qu'est-ce que Stripe Checkout ?

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.57.01-PM.png)
_Exemple de page Stripe Checkout_

Stripe Checkout est un outil tout-en-un qui non seulement rationalise et simplifie le processus de paiement pour nous en tant que développeurs. Il nous offre également une interface utilisateur pour nos clients, optimisée pour la performance et l'utilisabilité.

Lors de l'utilisation de Stripe Checkout par rapport à des options alternatives telles que Stripe Elements, l'avantage est que vous devez écrire beaucoup moins de code pour obtenir le même résultat final. De plus, vous bénéficiez de fonctionnalités telles que des traductions automatiques pour les utilisateurs mondiaux dans leur langue.

Vous avez également la possibilité de personnaliser cette interface utilisateur sans avoir à écrire un seul composant React.

## Stripe Checkout est hébergé sur Stripe

Soyez conscient que Stripe Checkout est hébergé sur les serveurs de Stripe et qu'il implique de rediriger l'utilisateur vers _checkout.stripe.com_. Cela ne doit cependant pas être considéré comme un inconvénient.

Étant donné que la confiance est une partie si importante du processus de paiement, il est souvent un grand avantage de savoir que Stripe gère le paiement. Par conséquent, les clients peuvent être beaucoup plus sécurisés et confiants dans le processus de paiement.

En bref, il est judicieux d'utiliser une solution pré-construite telle que Stripe Checkout, considérant qu'elle signifiera non seulement moins de travail pour vous, mais créera également une plus grande confiance dans votre produit.

## Comment configurer Stripe Checkout

1. Allez sur stripe.com et créez un compte gratuit.
2. Vous serez redirigé vers votre tableau de bord à _dashboard.stripe.com_

Dans le coin supérieur droit de votre tableau de bord, assurez-vous d'activer le "Mode Test".

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.39.55-PM.png)
_Assurez-vous d'être en mode test_

3. Créez un nouveau produit dans Stripe.

Le moyen le plus rapide d'y accéder est de rechercher "Créer un produit" dans la recherche et de cliquer sur le résultat "Créer un produit".

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.41.32-PM.png)
_Allez à "Créer un produit"_

4. Ajoutez les informations de votre produit, y compris son nom, sa description et son image.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.42.17-PM.png)
_Fournissez les informations de votre produit_

5. Sur la même page, ajoutez les informations de prix pour ce produit.

Dans cet exemple, nous choisirons un modèle de prix récurrent (mensuel). Sachez que vous pouvez également sélectionner un paiement unique pour vos produits.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.43.09-PM.png)
_Sélectionnez les détails de votre prix_

6. Enregistrez votre nouveau produit et obtenez votre identifiant de prix

Après la création de votre produit, si vous descendez jusqu'à la section des prix, vous verrez un identifiant commençant par `price_` à côté de votre prix. Vous aurez besoin de cet identifiant pour créer une session de paiement avec Stripe.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.44.49-PM.png)
_Récupérez l'identifiant de prix créé pour votre produit_

7. Obtenez votre clé publiable.

La dernière étape consiste à obtenir la clé publiable (de test) de Stripe. Nous en avons également besoin pour créer une session de paiement avec Stripe.

Cette fois, nous pouvons rechercher "clé API" et choisir le premier résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.47.56-PM.png)
_Recherchez "clé API"_

Sur la page des clés API (une fois de plus, en mode test), vous récupérerez la clé publiable qui commence par `pk_test`

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-16-at-12.49.15-PM.png)
_Récupérez la clé publiable, sous "token"_

## Comment ajouter Stripe Checkout à React

Maintenant que nous avons tout ce dont nous avons besoin pour configurer Stripe Checkout avec React, à savoir l'identifiant de prix et la clé publiable, nous pouvons créer notre application React.

Pour ce tutoriel, j'utiliserai Next.js, qui est un framework React. Vous pouvez créer votre propre application Next.js instantanément en utilisant StackBlitz en allant sur _next.new_.

Nous commencerons par créer un bouton pour passer à la caisse sur notre page d'accueil (pages/index.js). Lorsque l'utilisateur clique sur ce bouton, Stripe redirigera notre utilisateur vers la page de paiement.

```js
// pages/index.js

export default function Home() {
  return <button>Payer</button>;
}
```

Pour communiquer avec Stripe, nous devons installer le package suivant avec NPM ou Yarn :

```bash
npm install @stripe/stripe-js
```

Une fois installé, nous créerons un nouveau dossier et un fichier à l'intérieur : `lib/getStripe.js` à la racine de notre projet.

Dans ce fichier, nous allons gérer le chargement de Stripe une seule fois. Pour ce faire, nous passons notre clé publiable à Stripe.

```js
import { loadStripe } from '@stripe/stripe-js';

let stripePromise;
const getStripe = () => {
  if (!stripePromise) {
    stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY);
  }
  return stripePromise;
};

export default getStripe;

```

Ici, nous chargeons la clé publiable à partir d'un fichier `.env`. Assurez-vous de créer ce fichier à la racine de votre projet avec les deux valeurs suivantes, pour votre clé publiable et votre identifiant de prix :

```js
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY='pk_test_my_key'

NEXT_PUBLIC_STRIPE_PRICE_ID='price_my_id'
```

Une fois que vous avez ajouté vos variables d'environnement, nous retournerons à la page d'accueil et créerons une fonction appelée `handleCheckout`.

Elle appellera d'abord `getStripe` que nous devons attendre car cette fonction retourne une promesse. Assurez-vous d'importer notre fonction `getStripe` depuis le dossier lib.

```js
import getStripe from '../lib/getStripe';

export default function Home() {
  async function handleCheckout() {
    const stripe = await getStripe();
    const { error } = await stripe.redirectToCheckout({
      lineItems: [
        {
          price: process.env.NEXT_PUBLIC_STRIPE_PRICE_ID,
          quantity: 1,
        },
      ],
      mode: 'subscription',
      successUrl: `http://localhost:3000/success`,
      cancelUrl: `http://localhost:3000/cancel`,
      customerEmail: 'customer@email.com',
    });
    console.warn(error.message);
  }

  return <button onClick={handleCheckout}>Payer</button>;
}
```

Ensuite, nous appellerons `stripe.redirectToCheckout`, qui est également une fonction que nous devons `await`.

À cette fonction, nous passerons un objet qui inclut quatre propriétés principales :

1. `lineItems` : un tableau d'objets incluant les produits et la quantité de ces produits dans notre commande.
2. `mode` : si notre transaction est récurrente ou ponctuelle
3. `successUrl` : la page vers laquelle l'utilisateur sera redirigé après un achat réussi (n'hésitez pas à configurer cela vous-même)
4. `cancelUrl` : la page vers laquelle l'utilisateur sera redirigé après un achat réussi (encore une fois, facile à configurer)

Il existe de nombreuses autres propriétés que vous pouvez passer à cet objet, comme passer le `customerEmail` pour pré-remplir le champ d'email de l'utilisateur.

## Comment tester Stripe Checkout

Une fois que nous avons cliqué sur notre bouton de paiement, nous devrions être redirigés vers une page complète qui, en mode test, nous permettra de fournir un numéro de carte de crédit de test pour vérifier le processus de paiement (répétez le numéro 4242 pour tous les champs).

Si notre utilisateur annule et tente de revenir en arrière, il sera redirigé vers le cancelUrl que nous avons spécifié. Sinon, s'il complète ce processus avec succès, il sera redirigé vers le successUrl.

Une fois que vous êtes prêt à passer en production et à accepter l'argent de vos clients, tout ce que vous avez à faire est de remplacer votre clé publiable de test par une clé non-test.

Espérons que cela vous a donné une bonne compréhension de comment commencer avec Stripe Checkout et comment accepter plus facilement les paiements dans vos applications React !

Vous pouvez trouver le code final de cet exemple ici : [https://stackblitz.com/edit/nextjs-4ts4y4?file=pages%2Findex.js](https://stackblitz.com/edit/nextjs-4ts4y4?file=pages%2Findex.js)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*