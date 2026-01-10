---
title: Comment réduire le Round Trip Time (RTT) avec Next.js
subtitle: ''
author: Chukwudi Nweze
co_authors: []
series: null
date: '2025-11-06T10:28:20.629Z'
originalURL: https://freecodecamp.org/news/how-to-reduce-round-trip-time-rtt-with-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762424304223/4d818ff7-0fe2-448d-8acd-3da092bc55a4.png
tags:
- name: Next.js
  slug: nextjs
- name: web performance
  slug: web-performance
- name: optimization
  slug: optimization
seo_title: Comment réduire le Round Trip Time (RTT) avec Next.js
seo_desc: Have you ever wondered why some websites load almost immediately and others
  leave you looking at a blank screen, even when your internet connection is fast?
  In some cases, your internet speed may not be the issue. It is usually because of
  Round Trip ...
---

Vous êtes-vous déjà demandé pourquoi certains sites web se chargent presque instantanément alors que d'autres vous laissent devant un écran vide, même avec une connexion internet rapide ? Dans certains cas, la vitesse de votre connexion n'est pas en cause. C'est généralement dû au Round Trip Time (RTT), c'est-à-dire le temps nécessaire à votre navigateur pour envoyer une requête à un serveur et recevoir une réponse.

Internet dépend d'une infrastructure physique : câbles à fibres optiques, satellites et centres de données souvent situés à des milliers de kilomètres. Les requêtes réseau voyagent à grande vitesse, mais elles restent limitées par la vitesse de la lumière (environ 300 000 km/s). Par exemple, une requête réseau entre Lagos, au Nigeria, et un serveur à San Francisco, aux États-Unis, parcourt plus de 12 000 km et prend environ 150 à 200 millisecondes pour un seul aller-retour dans des conditions idéales. Multipliez cela par les 20 à 30 requêtes qu'une page web typique effectue (pour le HTML, le CSS, les images, les API, etc.), et ces millisecondes s'additionnent rapidement pour devenir des secondes de retard avant qu'une page ne soit complètement chargée.

Dans cet article, nous expliquerons en détail ce qu'est le Round Trip Time (RTT), pourquoi il est l'un des facteurs les plus négligés de la performance web, et comment vous pouvez utiliser Next.js pour minimiser le nombre de RTT afin de rendre vos applications rapides et réactives. Vous apprendrez comment des fonctionnalités telles que le Server-Side Rendering (SSR), les React Server Components (RSC), l'optimisation des images et la mise en cache travaillent ensemble pour réduire le Round Trip Time d'une page web.

## **Ce que vous allez apprendre**

* [Ce que vous allez apprendre](#heading-ce-que-vous-allez-apprendre)
    
* [Qu'est-ce que le Round Trip Time (RTT) ?](#heading-quest-ce-que-le-round-trip-time-rtt)
    
    * [Comment la distance augmente le Round Trip Time](#heading-comment-la-distance-augmente-le-round-trip-time)
        
* [Comment le Round Trip Time affecte les performances web](#heading-comment-le-round-trip-time-affecte-les-performances-web)
    
    * [Pourquoi le Client-Side Rendering semble plus lent](#heading-pourquoi-le-client-side-rendering-semble-plus-lent)
        
* [Comment réduire le Round Trip Time avec Next.js](#heading-comment-reduire-le-round-trip-time-avec-nextjs)
    
    * [Server-Side Rendering (SSR)](#heading-server-side-rendering-ssr)
        
    * [React Server Components (RSC)](#heading-react-server-components-rsc)
        
    * [Optimisation des images](#heading-optimisation-des-images)
        
    * [Mise en cache et rendu statique](#heading-mise-en-cache-et-rendu-statique)
        
* [Compromis entre les méthodes de rendu de Next.js](#heading-compromis-entre-les-methodes-de-rendu-de-nextjs)
    
* [Quand utiliser chaque méthode de rendu](#heading-quand-utiliser-chaque-methode-de-rendu)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le Round Trip Time (RTT) ?

Lorsque vous visitez un site web, le navigateur effectue une requête réseau vers un serveur. Le serveur traite la requête puis renvoie une réponse. Le Round Trip Time est la durée complète de ce trajet en millisecondes, ce qui inclut :

1. **Temps de trajet aller** : Le temps nécessaire à la requête réseau pour atteindre le serveur.
    
2. **Temps de traitement** : Le temps que le serveur a pris pour traiter la requête.
    
3. **Temps de trajet retour** : Le temps nécessaire à la réponse pour revenir au navigateur.
    

![Une illustration montrant la communication du round-trip time (RTT) entre un client et un serveur, où la requête du client prend environ 100 ms pour atteindre le serveur, et la réponse du serveur prend environ 200 ms pour revenir au client](https://cdn.hashnode.com/res/hashnode/image/upload/v1761405949671/1ceaadf4-5576-41ae-9f25-e846f41b3e67.png align="center")

### Comment la distance augmente le Round Trip Time

Le Round Trip Time dépend fortement de la distance physique entre le client et le serveur. Par exemple :

* Un utilisateur à Lagos, au Nigeria, effectuant une requête réseau vers un serveur à Londres situé à environ 5 000 km, pourrait voir un RTT de 100 à 150 ms.
    
* Un serveur à San Francisco situé à environ 12 000 km pourrait faire grimper le RTT à 200-300 ms. Plus le serveur est éloigné, plus le RTT est élevé.
    

## Comment le Round Trip Time affecte les performances web

Les pages web modernes effectuent de multiples requêtes réseau pour se charger complètement. Imaginez le chargement d'une page produit e-commerce qui nécessite :

* 1 requête réseau pour le HTML (environ 200 ms)
    
* 5 requêtes réseau pour le CSS/JavaScript (environ 1 000 ms)
    
* 10 requêtes réseau pour les images (environ 2 000 ms)
    
* 4 requêtes réseau pour les données produit via API (environ 800 ms)
    

Cela montre que la page produit prendra 20 requêtes réseau pour se charger complètement, ce qui représente environ 4 secondes de délai réseau.

La probabilité de rebond augmente de 32 % lorsque le temps de chargement de la page passe de 1 seconde à 3 secondes ([Étude Google/SOASTA, 2017](https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/page-load-time-statistics/)). Cela signifie qu'environ un tiers des visiteurs partent avant même que la page ne soit chargée.

### Pourquoi le Client-Side Rendering semble plus lent

Dans les applications en rendu côté client, chaque requête ajoute un RTT, et le rendu côté client traditionnel (CSR) dans les applications React accentue cela :

* Le navigateur télécharge une coquille HTML minimale et un volumineux bundle JavaScript.
    
* Le JavaScript s'exécute pour récupérer les données et générer l'interface utilisateur, ce qui nécessite des requêtes réseau supplémentaires.
    
* Chaque appel API ajoute un autre RTT, retardant le First Contentful Paint (FCP).
    

Le First Contentful Paint (FCP) mesure le temps écoulé entre le moment où l'utilisateur a commencé la navigation et le moment où une partie du contenu de la page, comme du texte, des images, des éléments `<svg>` ou `<canvas>`, est affichée à l'écran.

Dans les applications CSR, le FCP est retardé car le navigateur ne peut afficher aucun contenu significatif tant que le JavaScript n'a pas fini de charger, d'analyser et d'exécuter le code nécessaire à la construction de l'interface. Une application CSR classique peut nécessiter 5 à 10 allers-retours réseau pour obtenir toutes les ressources nécessaires au rendu de l'interface, ce qui peut facilement ajouter plusieurs secondes de délai.

```javascript
// pages/index.js (CSR)
import { useState, useEffect } from "react"

export default function Home() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    // Fetch data after page loads
    fetch("https://api.example.com/products")
      .then((res) => res.json())
      .then((data) => setProducts(data))
  }, [])

  return (
    <div>
      <h1>Products</h1>
      {products.length ? (
        products.map((product) => <p key={product.id}>{product.name}</p>)
      ) : (
        <p>Loading...</p>
      )}
    </div>
  )
}
```

Dans le code ci-dessus, lorsque le composant `Home` est monté, il initialise l'état avec un tableau vide. Le hook `useEffect` s'exécute ensuite une fois pour effectuer une requête API. Pendant que la requête est en cours, le message "Loading..." s'affiche à l'écran. Une fois la requête terminée avec succès, React met à jour l'état avec les données récupérées et restitue l'interface pour afficher les produits. Ce processus introduit un aller-retour supplémentaire, ce qui retarde davantage le FCP.

## Comment réduire le Round Trip Time avec Next.js

Vous ne pouvez pas éliminer complètement le RTT. Les données doivent toujours voyager sur le réseau. Ce que fait Next.js, c'est réduire la fréquence de ces requêtes réseau et la quantité de données transportées par chaque requête. Il y parvient grâce à plusieurs techniques, telles que le **Server-Side Rendering (SSR)**, les **React Server Components (RSC)**, l'**optimisation des images** et la **mise en cache ou le rendu statique**.

### Server-Side Rendering (SSR)

Contrairement aux applications React.js traditionnelles, où le navigateur gère la majeure partie du travail (récupération des fichiers statiques, du JavaScript et des données nécessaires au rendu d'une page), le serveur génère l'intégralité du HTML, récupère les données, effectue le rendu de la page et l'envoie au navigateur en un seul RTT.

**Avantages :**

* **Moins d'allers-retours :** Puisque la récupération des données et le rendu ont lieu sur le serveur, le navigateur reçoit une page prête à l'affichage en un seul RTT.
    
* **Amélioration du First Contentful Paint :** Un RTT faible signifie que le contenu s'affiche sur la page presque immédiatement.
    

```javascript
// pages/index.js (SSR)
export async function getServerSideProps() {
  // Fetch data on the server
  const res = await fetch('https://api.example.com/products');
  const products = await res.json();

  return {
    props: { products }, // Pass data to the page
  };
}

export default function Home({ products }) {
  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <p key={product.id}>{product.name}</p>
      ))}
    </div>
  );
}
```

Dans le code ci-dessus, `getServerSideProps` s'exécute entièrement sur le serveur. Lorsqu'un utilisateur visite ou rafraîchit la page, `getServerSideProps()` est appelé pour récupérer les données des produits depuis l'API externe. Les données récupérées sont ensuite pré-rendues sur le serveur, ce qui signifie que la liste des produits est incluse dans le HTML avant d'être envoyée au navigateur. Cela supprime l'aller-retour supplémentaire observé en CSR et améliore le FCP, car les utilisateurs voient un contenu significatif dès le chargement de la page.

### React Server Components (RSC)

Le Server-Side Rendering est une technique où toute la page est générée sur le serveur. Mais imaginez si seulement certaines parties d'une page devaient être rendues sur le serveur tandis que d'autres le seraient sur le client ?

Les React Server Components permettent de partitionner le rendu entre le serveur et le client.

Par exemple, un composant `ProductList` peut être rendu sur le serveur, tandis qu'un composant `SearchInput` est rendu sur le client pour gérer les interactions utilisateur.

**Avantages :**
Les RSC réduisent le RTT global et augmentent également le FCP de la page.

```javascript
// app/ProductList.jsx (Server Component)
async function ProductList() {
  // Fetch data on the server
  const res = await fetch('https://api.example.com/products');
  const products = await res.json();

  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <p key={product.id}>{product.name}</p>
      ))}
      <ClientSearch /> {/* Client Component */}
    </div>
  );
}

export default ProductList;
```

Dans le code ci-dessus, `ProductList` est un composant serveur avec un composant `ClientSearch` comme enfant. Le `ClientSearch` est rendu dans le navigateur tandis que le reste de `ProductList` est rendu sur le serveur. Au chargement de la page, le serveur exécute `fetch()` pour récupérer les données et génère le HTML complet pour la liste de produits, tandis que `ClientSearch` s'occupe des interactions côté client.

```javascript
// components/ClientSearch.jsx (Client Component)
'use client';

import { useState } from 'react';

export default function ClientSearch() {
  const [query, setQuery] = useState('');

  return (
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Search products..."
    />
  );
}
```

Le composant `ClientSearch` ci-dessus gère les interactions utilisateur, comme la mise à jour de l'entrée de recherche avec `useState`. Il est marqué par `'use client'`, il s'exécute donc entièrement côté client.

### Optimisation des images

Les images impactent négativement le RTT lorsqu'elles ne sont pas optimisées, car les fichiers volumineux prennent plus de temps à être transférés du serveur au navigateur.

Le composant Image de Next.js optimise les images automatiquement :

**Redimensionnement** : Il ajuste la taille de l'image en fonction de l'appareil de l'utilisateur.

**Compression** : Il utilise de nouveaux formats comme WebP pour réduire considérablement la taille du fichier.

**Lazy Loading** : Charge les images uniquement lorsqu'elles entrent dans le champ de vision de l'utilisateur, ce qui réduit le nombre de requêtes initiales.

```javascript
// pages/index.js
import Image from 'next/image';

export default function Home() {
  return (
    <div>
      <h1>Welcome to Our Store</h1>
      <Image
        src="/product.jpg"
        alt="Product Image"
        width={500}
        height={300}
      />
    </div>
  );
}
```

Dans le code ci-dessus, la page utilise le composant `Image` intégré de Next.js pour afficher une image optimisée. Au chargement de la page, Next.js gère le redimensionnement, le chargement différé, etc. Cela signifie que le navigateur ne téléchargera que la taille d'image appropriée pour l'appareil.

### Mise en cache et rendu statique

Avec le SSR et les Server Components, le RTT peut rester élevé si le serveur doit traiter les données à chaque requête. Next.js résout ce problème avec la Static Site Generation (SSG) et l'Incremental Static Regeneration (ISR).

Voici comment cela fonctionne :

**Static Site Generation** : Les pages sont pré-rendues au moment du build, mises en cache et livrées sous forme de HTML statique depuis un CDN.

**Incremental Static Regeneration** : Les pages sont pré-rendues mais peuvent être régénérées en arrière-plan après un intervalle, par exemple toutes les 60 secondes.

```javascript
// app/page.jsx
export const revalidate = 60; // Regenerate the page every 60 seconds

export default async function Home() {
  // Fetch data on the server
  const res = await fetch("https://api.example.com/products", {
    next: { revalidate: 60 }, 
  });
  const products = await res.json();

  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <p key={product.id}>{product.name}</p>
      ))}
    </div>
  );
}
```

Dans le code ci-dessus, la page utilise l'Incremental Static Regeneration (ISR). L'option `revalidate = 60` permet de régénérer la page toutes les 60 secondes. Lorsqu'un utilisateur visite la page, le serveur sert instantanément le HTML pré-rendu. Le `next: { revalidate: 60 }` à l'intérieur du `fetch()` signifie que les données sont mises en cache pendant 60 secondes. Après ce délai, la requête suivante déclenchera la régénération de données fraîches par le serveur.

## Compromis entre les méthodes de rendu de Next.js

Avec le **Server-Side Rendering (SSR)**, le navigateur reçoit la page complète en un seul aller-retour. En revanche, cela peut augmenter la charge du serveur et entraîner un TTFB élevé. Le TTFB (Time to First Byte) est le temps nécessaire pour qu'un utilisateur commence à voir le contenu s'afficher sur son navigateur.

Avec l'**Incremental Static Regeneration (ISR)**, la page est pré-rendue et mise en cache, offrant ainsi une réponse instantanée du serveur. La page sera régénérée selon une période fixe (comme toutes les 60 secondes). L'inconvénient est que les utilisateurs pourraient voir du contenu obsolète avant sa mise à jour.

Dans les **Server Components**, le rendu a lieu sur le serveur et seules les parties interactives sont gérées sur le client. Ainsi, les avantages du rendu côté serveur sont conservés tout en permettant les interactions client. Le seul bémol est que les développeurs doivent être très attentifs lorsqu'ils décident de ce qui doit s'exécuter sur le serveur ou sur le client.

## Quand utiliser chaque méthode de rendu

Le **Server-Side Rendering (SSR)** doit être appliqué aux pages qui se mettent à jour fréquemment, comme les tableaux de bord, les profils d'utilisateurs, etc. Le SSR garantit que les utilisateurs voient toujours les dernières données.

Quant à l'**Incremental Static Regeneration (ISR)**, elle doit être appliquée aux pages dont les changements sont peu fréquents, par exemple les listes de produits, les pages marketing ou les blogs.

Utilisez les **Server Components** lorsque vous voulez qu'une partie de la page soit rendue sur le serveur tandis que certaines sections s'exécutent sur le client. Par exemple, des pages nécessitant une interaction utilisateur comme des entrées de recherche ou des filtres, alors que la récupération et le rendu des données se font sur le serveur.

## Conclusion

Le Round Trip Time (RTT) est l'un des facteurs cachés derrière la lenteur de chargement des pages. Chaque requête réseau ajoute un aller-retour, et ces délais s'accumulent à mesure que le navigateur récupère diverses ressources comme des scripts, des images et des fichiers de données. Next.js traite ce problème en minimisant le nombre de requêtes réseau nécessaires avant le premier affichage du contenu.

* Le **Server-Side Rendering (SSR)** et les **React Server Components (RSC)** déplacent la récupération des données et le rendu vers le serveur, ce qui réduit les requêtes côté client.
    
* L'**optimisation des images** réduit la taille des fichiers et utilise des CDN pour livrer le contenu plus rapidement depuis des serveurs proches.
    
* La **mise en cache et le rendu statique** servent instantanément des pages pré-générées sans traitement supplémentaire du serveur.
    

Grâce à ces techniques, vous pouvez créer des applications web qui se chargent plus rapidement et semblent plus réactives, même pour les utilisateurs éloignés de votre serveur d'origine ou disposant de réseaux lents.