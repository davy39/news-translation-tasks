---
title: Comment créer une Progressive Web App (PWA) avec Next.js
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2024-09-20T21:48:26.624Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-nextjs-pwa
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726728761614/ba739b83-78b9-4cd7-9040-13ade8e515f7.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: reactjs
- name: PWA
  slug: pwa
seo_title: Comment créer une Progressive Web App (PWA) avec Next.js
seo_desc: Have you ever wanted to create a web app that works smoothly on any device—whether
  it's on the web, mobile, or desktop? Imagine if your app could load quickly, work
  without an internet connection, and feel like a native app, all without needing
  to be...
---

Avez-vous déjà voulu créer une application web qui fonctionne de manière fluide sur n'importe quel appareil, que ce soit sur le web, sur mobile ou sur ordinateur de bureau ? Imaginez si votre application pouvait se charger rapidement, fonctionner sans connexion Internet et ressembler à une application native, le tout sans avoir besoin d'être installée depuis un app store. C'est exactement ce que les Progressive Web Apps (PWA) peuvent faire.

Dans ce tutoriel, vous apprendrez à construire une PWA en utilisant Next.js. Nous commencerons par créer un site web de recherche de films fonctionnel avec ces outils. Une fois les bases posées, nous transformerons cette application en PWA, en ajoutant le support hors ligne et des temps de chargement plus rapides. À la fin, vous disposerez d'une PWA puissante offrant une expérience utilisateur fluide sur toutes les plateformes, le tout à partir d'une seule base de code.

### **Ce que nous allons couvrir**

* **Configuration du projet :** Nous commencerons par créer l'application de recherche de films avec Next.js, qui est un choix idéal en 2024 pour construire des applications React rapides et fiables fonctionnant sur tous les appareils.
    
* **Transformer l'application en PWA :** Ensuite, nous passerons en revue les étapes pour convertir l'application en une Progressive Web App, en couvrant les fonctionnalités clés et les meilleures pratiques des PWA.
    
* **Ajout du support hors ligne :** Enfin, nous veillerons à ce que votre application reste fonctionnelle même sans connexion Internet en implémentant des capacités hors ligne.
    

Voici à quoi ressemblera l'application finale :

![Cette capture d'écran montre la PWA MovieMaster terminée, mettant en avant son design épuré et ses capacités hors ligne.](https://cdn.hashnode.com/res/hashnode/image/upload/v1726724446891/47398ad8-fa1f-46d2-8a22-0a5d49e6a67e.png align="center")

### **Public**

Ce tutoriel s'adresse aux développeurs React de tous niveaux, que vous débutiez ou que vous soyez déjà expérimenté. Si vous souhaitez améliorer vos applications web avec des fonctionnalités PWA, ce guide vous accompagnera à travers les étapes nécessaires.

### **Prérequis**

Avant de commencer, assurez-vous d'être familier avec React.js et Next.js. Si vous découvrez les PWA, vous devriez lire quelques articles d'introduction pour obtenir un aperçu rapide.

* [*What are Progressive Web Apps? PWA Guide for Beginners*](https://www.freecodecamp.org/news/what-are-progressive-web-apps-pwa-guide/)
    
* [*Learn Progressive Web Apps*](https://web.dev/learn/pwa)
    

<aside>
  <h2>Table des matières</h2>
  <ul>
    <li><a href="#0">Introduction</a></li>
    <li><a href="#heading-ce-que-nous-allons-couvrir">Ce que nous allons couvrir</a></li>
    <li><a href="#heading-public">Public</a></li>
    <li><a href="#heading-prerequis">Prérequis</a></li>
    <li><a href="#heading-quest-ce-quune-progressive-web-app-pwa">Qu'est-ce qu'une Progressive Web App (PWA) ?</a></li>
    <li><a href="#heading-pourquoi-transformer-votre-application-web-en-pwa">Pourquoi transformer votre application web en PWA ?</a></li>
    <li><a href="#heading-premiers-pas-configuration-du-projet-nextjs">Premiers pas : Configuration du projet Next.js</a></li>
    <li><a href="#heading-pourquoi-choisir-nextjs-en-2024">Pourquoi choisir Next.js en 2024 ?</a></li>
    <li><a href="#heading-installation-du-projet">Installation du projet</a></li>
    <li><a href="#heading-apercu-de-la-structure-du-projet">Aperçu de la structure du projet</a></li>
 <li><a href="#heading-comprendre-les-layouts">Comprendre les Layouts</a></li>
    <li><a href="#heading-execution-et-apercu-du-projet">Exécution et aperçu du projet</a></li>
    <li><a href="#heading-comment-transformer-votre-application-web-en-pwa">Comment transformer votre application web en PWA</a></li>
    <li><a href="#heading-criteres-dune-pwa">Critères d'une PWA</a></li>
    <li><a href="#heading-comment-ajouter-un-fichier-web-manifest-a-votre-application-nextjs">Comment ajouter un fichier Web Manifest à votre application Next.js</a></li>
    <li><a href="#heading-comment-enregistrer-un-service-worker">Comment enregistrer un Service Worker</a></li>
    <li><a href="#heading-comment-ajouter-le-support-hors-ligne">Comment ajouter le support hors ligne</a></li>
    <li><a href="#heading-que-mettre-en-cache">Que mettre en cache ?</a></li>
    <li><a href="#heading-quand-mettre-en-cache">Quand mettre en cache ?</a></li>
    <li><a href="#heading-mise-en-cache-dynamique">Mise en cache dynamique</a></li>
    <li><a href="#heading-mise-en-cache-des-requetes-api">Mise en cache des requêtes API</a></li>
    <li><a href="#heading-comment-servir-les-ressources-mises-en-cache">Comment servir les ressources mises en cache</a></li>
    <li><a href="#heading-fournir-une-page-de-secours">Fournir une page de secours</a></li>
    <li><a href="#heading-conclusion">Conclusion</a></li>
  </ul>
</aside>

## Qu'est-ce qu'une Progressive Web App (PWA) ?

Une Progressive Web App (PWA) est un type d'application web construite à l'aide de technologies web standard telles que HTML, CSS et JavaScript. Les PWA fonctionnent sur le web, sur ordinateur et sur les appareils mobiles, combinant les meilleures fonctionnalités des applications web et natives pour offrir une expérience rapide, fiable et engageante.

Ce qui rend les PWA spéciales, c'est leur capacité à fonctionner hors ligne, à envoyer des notifications push et à être installées sur l'appareil d'un utilisateur sans passer par un app store. En bref, une PWA donne à votre application web l'aspect d'une application native tout en conservant la flexibilité et la large portée du web.

### **Pourquoi transformer votre application web en PWA ?**

Convertir votre application web en PWA apporte plusieurs avantages :

* **Disponibilité multiplateforme :** Une PWA fonctionne sur n'importe quel appareil doté d'un navigateur. Vous n'avez donc besoin de développer et de maintenir qu'une seule base de code pour les applications web, mobiles et de bureau. Cela permet de gagner du temps et de garantir une expérience cohérente sur toutes les plateformes.
    

![Cette image montre la PWA MovieMaster fonctionnant sur un téléphone mobile, un navigateur web et un ordinateur de bureau, illustrant la nature polyvalente des PWA.](https://cdn.hashnode.com/res/hashnode/image/upload/v1726724668376/acf531ba-7ff7-4c62-8d11-ac283d236bd8.png align="left")

* **Capacités hors ligne :** Les PWA peuvent fonctionner hors ligne ou dans des zones à faible connectivité en mettant en cache les ressources essentielles, gardant votre application fonctionnelle même sans accès Internet.
    
* **Performances améliorées :** Les PWA sont conçues pour se charger rapidement et fonctionner de manière fluide, même sur des réseaux lents, grâce à des techniques comme les service workers et la mise en cache.
    
* **Engagement utilisateur accru :** Les utilisateurs peuvent ajouter les PWA directement sur leur écran d'accueil sans passer par un app store. Cet accès facile, ainsi que des fonctionnalités comme les notifications push, aide à maintenir l'engagement des utilisateurs.
    

**Inconvénients des PWA**

Bien que les PWA offrent de nombreux avantages, il existe quelques inconvénients :

* **Accès limité aux fonctionnalités de l'appareil** : Les PWA n'ont pas un accès complet à certaines fonctionnalités de l'appareil comme le Bluetooth ou les contrôles avancés de l'appareil photo. Pour les applications nécessitant une intégration matérielle profonde, cela peut être une limitation.
    
* **Moins de visibilité** : Comme les PWA ne passent pas par les app stores, elles ne bénéficient pas de la visibilité que ces derniers offrent. Certains utilisateurs peuvent également préférer télécharger des applications depuis les stores plutôt que directement depuis le navigateur.
    
* **Support iOS limité** : Certaines fonctionnalités des PWA, comme les notifications push, ne fonctionnent pas aussi bien sur iPhone et iPad que sur les appareils Android, ce qui peut limiter l'engagement avec les utilisateurs iOS.
    

## **Premiers pas : Configuration du projet Next.js**

Maintenant que nous avons discuté des avantages des PWA, passons à l'implémentation concrète. Nous allons commencer par configurer les fichiers nécessaires dans notre projet.

### **Pourquoi choisir Next.js en 2024 ?**

Next.js est un choix de premier plan pour construire des applications React en 2024. Il offre des fonctionnalités telles que le rendu côté serveur (SSR) et la génération de sites statiques (SSG), facilitant la création d'applications web rapides et fiables. Ces fonctionnalités garantissent que votre application est performante sur tous les appareils et fonctionne même hors ligne.

### **Installation du projet**

Suivez ces étapes pour configurer votre projet Next.js :

1. Cloner le dépôt : Ouvrez votre terminal et lancez :
    
    ```bash
    git clone https://github.com/iamspruce/MovieMaster.git
    ```
    
2. Naviguez vers le répertoire de votre projet :
    
    ```bash
    cd your-repo
    ```
    
3. Installez les dépendances : Installez les paquets requis avec :
    
    ```bash
    npm install
    ```
    
4. Configurez les variables d'environnement : Créez un fichier .env.local à la racine et ajoutez votre clé API OMDB :
    
    ```plaintext
    NEXT_PUBLIC_OMDB_API_KEY=your-api-key
    ```
    

Vous pouvez obtenir votre clé API sur le [site web de l'API OMDB](https://www.omdbapi.com/apikey.aspx).

**Pourquoi la clé API OMDB est-elle nécessaire ?**  
La clé API OMDB permet à votre PWA de récupérer des données de films, comme les titres, les affiches et les descriptions, directement depuis la base de données OMDB. C'est essentiel pour une application liée au cinéma comme MovieMaster, car cela fournit des informations à jour aux utilisateurs sans que vous ayez à stocker toutes les données vous-même.

Dans une PWA, l'utilisation d'une API comme OMDB garantit que l'application peut fournir du contenu frais aux utilisateurs, même lorsqu'elle est installée sur leurs appareils. Combiné avec les fonctionnalités de mise en cache et hors ligne de la PWA, les utilisateurs peuvent toujours consulter les détails des films précédemment récupérés, même s'ils perdent leur connexion Internet.

**Note** : Assurez-vous que Node.js et npm sont installés sur votre système. Si ce n'est pas le cas, vous pouvez les télécharger sur [nodejs.org](http://nodejs.org/).

#### **Aperçu de la structure du projet**

Voici un bref aperçu de l'organisation du projet :

* **/public** : Contient les fichiers statiques tels que les images et les favicons.
    
* **/src/app** : Héberge les fichiers principaux de l'application, y compris les styles globaux (globals.css), la page principale (**page.tsx**), les configurations de layout (**layout.tsx**) et la logique côté client (**RootLayoutClient.tsx**).
    
* **/src/components** : Comprend les composants réutilisables. Les composants Shadcn UI sont situés dans le répertoire /ui, et d'autres composants spécifiques comme **MovieCard.tsx** se trouvent ici.
    
* **/src/lib** : Contient des fonctions utilitaires et du code de récupération de données, tels que **fetchMovies.ts** et **useMediaQuery.ts**.
    

Pour le style, nous utilisons :

* **TailwindCSS** : Appliqué via **globals.css** pour une approche de conception orientée utilitaires.
    
* **Shadcn UI** : Une bibliothèque fournissant des composants UI accessibles et prêts à l'emploi.
    

#### **Comprendre les Layouts**

Le projet utilise deux layouts clés :

1. **layout.tsx** : Gère le rendu côté serveur et définit les métadonnées de l'application. Il utilise le composant `RootLayoutClient` pour gérer les fonctionnalités côté client. Voici à quoi il ressemble :
    
    ```javascript
    import React from "react";
    import type { Metadata } from "next";
    import { cn } from "@/lib/utils";
    import { Inter as FontSans } from "next/font/google";
    
    import RootLayoutClient from "./RootLayoutClient";
    
    const fontSans = FontSans({
      subsets: ["latin"],
      variable: "--font-sans",
    });
    
    export const metadata: Metadata = {
      title: "MovieMaster",
      description: "La PWA MovieMaster vous aide à trouver les derniers films grâce à une recherche facile par genre, année, et plus encore. Elle fonctionne de manière fluide sur n'importe quel appareil, même hors ligne, vous offrant une excellente expérience de navigation cinématographique.",
      manifest: "/web.manifest",
    };
    
    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="fr" suppressHydrationWarning>
          <body className={cn("min-h-screen bg-background font-sans antialiased", fontSans.variable)}>
            <RootLayoutClient>{children}</RootLayoutClient>
          </body>
        </html>
      );
    }
    ```
    
2. **RootLayoutClient.tsx** : Gère la logique côté client, essentielle pour le rendu des éléments interactifs et la gestion des états de l'interface utilisateur.
    
    ```javascript
    "use client";
    
    import React from "react";
    import { Toaster } from "@/components/ui/sonner";
    import "./globals.css";
    
    export default function RootLayoutClient({ children }: { children: React.ReactNode }) {
      return (
        <div className="text-white flex flex-col">
          <div className="container mx-auto px-4 max-w-[1024px]">
            {children}
            <Toaster />
          </div>
        </div>
      );
    }
    ```
    

#### **Exécution et aperçu du projet**

Pour commencer à travailler sur votre projet :

**Lancer le serveur de développement** : Dans votre terminal, exécutez :

```bash
npm run dev
```

Cela lancera le serveur de développement, et vous pourrez visualiser l'application en naviguant sur http://localhost:3000 dans votre navigateur.

## **Comment transformer votre application web en PWA**

Pour transformer votre application web en PWA, votre application doit répondre à certains critères. Passons en revue ces exigences et implémentons les changements nécessaires étape par étape.

### Critères d'une PWA

1. **Servie via HTTPS** : Votre application doit être servie via une origine sécurisée (HTTPS) ou `localhost` pour le développement. Si vous développez localement, ce critère est déjà rempli.
    
2. **Fichier Web Manifest** : Un fichier web manifest fournit des métadonnées sur votre application, telles que son nom, ses icônes et son URL de départ. Ce fichier est crucial pour rendre votre application installable sur l'appareil d'un utilisateur.
    
3. **Service Worker avec un événement** `fetch` : Votre application doit enregistrer un service worker avec au moins un événement `fetch`. C'est essentiel pour que votre application soit reconnue comme une PWA et soit installable. Au-delà de cela, les service workers améliorent les performances et la fiabilité de votre application, lui permettant de mettre en cache des ressources et de gérer les requêtes réseau même hors ligne.
    

### **Comment ajouter un fichier Web Manifest à votre application Next.js**

Pour ajouter un fichier web manifest dans votre application Next.js, placez-le dans le répertoire **public/** et référencez-le dans votre fichier layout. Assurez-vous que toutes les images incluses dans votre fichier manifest se trouvent également dans le répertoire **public/**.

Voici un exemple de fichier **web.manifest** :

```json
{
  "name": "Movie Master",
  "short_name": "Moviemaster",
  "theme_color": "#8936FF",
  "background_color": "#333333",
  "start_url": "/",
  "id": "MovieMaster",
  "display": "standalone",
  "description": "La PWA MovieMaster vous aide à trouver les derniers films avec une recherche facile par genre, année et plus encore. Elle fonctionne de manière fluide sur n'importe quel appareil, même hors ligne.",
  "icons": [
    {
      "purpose": "maskable",
      "sizes": "512x512",
      "src": "icon512_maskable.png",
      "type": "image/png"
    },
    {
      "purpose": "any",
      "sizes": "512x512",
      "src": "icon512_rounded.png",
      "type": "image/png"
    }
  ],
  "screenshots": [
    {
      "src": "screenshot1.png",
      "type": "image/png",
      "sizes": "1080x1920",
      "form_factor": "narrow"
    }
  ]
}
```

#### **Champs obligatoires**

* `name` : Le nom complet de votre application.
    
* `short_name` : Une version plus courte du nom de l'application, affichée lorsqu'il n'y a pas assez d'espace pour le nom complet.
    
* `icons` : Icônes représentant votre application à différentes tailles.
    
* `start_url` : L'URL qui s'ouvre au lancement de l'application.
    
* `display` : Définit le mode d'affichage (par exemple, `standalone` pour une expérience plein écran).
    

#### **Champs recommandés**

* `theme_color` : Définit la couleur de thème de l'interface utilisateur du navigateur, comme la barre d'adresse. Cette couleur renforce l'aspect natif de votre PWA.
    

Cet exemple montre comment la couleur de thème (#8936FF) est appliquée à l'interface utilisateur du navigateur, donnant à votre PWA un aspect natif.

![Une interface de recherche de films sur thème sombre affichant "The Avengers" (2012) montrant comment la couleur du thème est appliquée à l'interface utilisateur du navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1726725605476/32366f45-b981-44bc-ac60-0f3661b8ed2c.png align="left")

* `background_color` : Définit la couleur d'arrière-plan de l'écran de démarrage (splash screen) lors du lancement de votre application.
    
* `screenshots` : Fournissez des captures d'écran de votre application pour améliorer l'expérience d'installation, en particulier sur les appareils Android.
    

Cet exemple illustre comment les captures d'écran sont affichées pendant le processus d'installation, améliorant l'expérience utilisateur, surtout sur Android.

![Une image montrant comment les captures d'écran sont affichées pendant le processus d'installation sur Android.](https://cdn.hashnode.com/res/hashnode/image/upload/v1726725620443/53b6712b-574a-445c-aca2-7c57dd62a268.jpeg align="left")

* `id` : Identifiant unique pour l'application
    

### **Comment référencer le fichier Web Manifest**

Ensuite, ajoutons le fichier manifest à vos pages. Dans Next.js, vous pouvez l'inclure dans les `metadata` de votre **layout.tsx** :

```javascript
export const metadata: Metadata = {
  title: "MovieMaster",
  description: "Trouvez les derniers films en toute simplicité.",
  manifest: "/web.manifest", // Lien vers le fichier manifest
};
```

### **Comment enregistrer un Service Worker**

Un service worker est un script que votre navigateur exécute en arrière-plan, vous permettant de contrôler la façon dont votre application gère les requêtes réseau, la mise en cache et d'autres tâches.

L'enregistrement d'un service worker avec au moins un événement `fetch` est essentiel pour que votre application soit reconnue comme une PWA et soit installable.

Créez un fichier **service-worker.js** dans le répertoire **public/** avec le code suivant :

```javascript
self.addEventListener('install', (event) => {
  console.log('Service Worker en cours d\'installation.');
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker activé.');
});

self.addEventListener('fetch', (event) => {
  console.log('Récupération de :', event.request.url);
  event.respondWith(fetch(event.request));
});
```

Ensuite, enregistrez le service worker dans votre fichier **RootLayoutClient.tsx** :

```javascript
"use client";

import React from "react";

export default function RootLayoutClient({ children }) {
  React.useEffect(() => {
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker
        .register("/service-worker.js")
        .then((registration) => {
          console.log("Service Worker enregistré avec le scope :", registration.scope);
        })
        .catch((error) => {
          console.error("L'enregistrement du Service Worker a échoué :", error);
        });
    }
  }, []);

  return (
    <div className="text-white flex flex-col">
      <div className="container mx-auto px-4 max-w-[1024px]">
        {children}
      </div>
    </div>
  );
}
```

Une fois que votre application répond à tous les critères, les utilisateurs peuvent facilement l'installer sur leurs appareils. Par exemple, avec le navigateur Edge, une option d'installation apparaîtra dans le menu du navigateur, permettant aux utilisateurs d'ajouter votre application directement à leur bureau ou écran d'accueil.

Voici à quoi ressemble le processus d'installation :

![Une image montrant l'option d'installation sur le navigateur Edge](https://cdn.hashnode.com/res/hashnode/image/upload/v1726725642915/c7e6af8a-56e8-4eb2-b1b6-fd715ea7210a.png align="left")

## Comment ajouter le support hors ligne

À ce stade, même si notre application est techniquement une PWA, elle se comporte toujours comme une application web classique. Chaque fois qu'un utilisateur demande une ressource, l'application effectue une requête réseau, et si le réseau échoue, l'utilisateur se retrouve face à une page d'erreur. Ce n'est pas idéal, surtout quand la puissance d'une PWA réside dans sa capacité à fonctionner hors ligne ou dans de mauvaises conditions de réseau.

Avec une PWA, vous pouvez intercepter chaque requête effectuée par votre application à l'aide d'un service worker. Cela vous donne la flexibilité de décider comment servir le contenu : depuis le réseau ou depuis un cache. Ce contrôle vous permet de garantir que les utilisateurs peuvent toujours accéder à l'application, même sans connexion Internet.

### **Comment livrer des ressources depuis le réseau**

Commençons par examiner comment notre application se comporte actuellement, ce qui est similaire à n'importe quelle application web standard :

```javascript
self.addEventListener("fetch", (event) => {
  event.respondWith(fetch(event.request));
});
```

Ce code récupère simplement les ressources directement depuis le réseau. Si le réseau est indisponible, la requête échouera, entraînant une erreur. C'est le comportement par défaut d'une application web standard.

### **Comment implémenter le support hors ligne**

Pour fournir une expérience hors ligne, nous devons mettre en cache les ressources de notre application lorsque l'utilisateur est en ligne, puis servir ces ressources mises en cache lorsqu'il est hors ligne. Pour cela, nous utiliserons l'API Cache Storage, qui nous permet de stocker des ressources localement sur l'appareil de l'utilisateur.

### **Que mettre en cache ?**

La décision de ce qu'il faut mettre en cache dépend des besoins de votre application. Pour une application de recherche de films comme la nôtre, nous voudrons mettre en cache les ressources essentielles nécessaires pour afficher une version de base de l'application :

* La page HTML principale
    
* Les feuilles de style CSS nécessaires au rendu du site
    
* Les images utilisées dans l'interface utilisateur
    
* Les fichiers JavaScript requis pour les fonctionnalités
    
* Les réponses aux requêtes API
    

**Note :** Bien que vous puissiez presque tout mettre en cache, soyez attentif aux limitations de stockage, car tous les éléments mis en cache sont stockés sur l'appareil de l'utilisateur. Utilisez le stockage judicieusement pour éviter de prendre trop de place.

### **Quand mettre en cache ?**

Une fois que nous savons quoi mettre en cache, la question suivante est de savoir quand le faire. Devez-vous tout mettre en cache lors de l'installation du service worker, ou au fur et à mesure que les ressources sont demandées ?

La réponse dépend des besoins de l'application, mais une bonne pratique consiste à mettre en cache les fichiers de base nécessaires au rendu d'une version minimale de l'application lors de l'installation du service worker.

Voici comment vous pouvez faire cela :

```javascript
const CACHE_NAME = "MOVIE_MASTER_V1";

async function cacheCoreAssets() {
  const cache = await caches.open(CACHE_NAME);
  return cache.addAll([
    "/",
    "/imdb-logo.svg",
    "/rotten-tomatoes-logo.svg",
  ]);
}

self.addEventListener("install", (event) => {
  event.waitUntil(cacheCoreAssets());
  self.skipWaiting();
});
```

Dans ce code, `self.skipWaiting()` garantit que le nouveau service worker s'active immédiatement après l'installation, en sautant la phase d'attente.

Il est également important de supprimer les anciens caches lorsqu'un nouveau service worker est activé :

```javascript
async function clearOldCaches() {
  const cacheNames = await caches.keys();
  return Promise.all(
    cacheNames
      .filter((name) => name !== CACHE_NAME)
      .map((name) => caches.delete(name))
  );
}

self.addEventListener("activate", (event) => {
  event.waitUntil(clearOldCaches());
  self.clients.claim();
});
```

La méthode `self.clients.claim()` garantit que le nouveau service worker prend le contrôle de toutes les pages dès qu'il est activé.

### **Mise en cache dynamique**

La mise en cache dynamique est particulièrement utile pour les applications React comme la nôtre, où les fichiers statiques sont générés automatiquement. Avec la mise en cache dynamique, vous n'avez pas besoin de connaître tous les fichiers à l'avance. Au lieu de cela, elle gère le processus de mise en cache pour vous au fur et à mesure que les fichiers sont demandés.

```javascript
async function dynamicCaching(request) {
  const cache = await caches.open(CACHE_NAME);

  try {
    const response = await fetch(request);
    const responseClone = response.clone();
    await cache.put(request, responseClone);
    return response;
  } catch (error) {
    console.error("La mise en cache dynamique a échoué :", error);
    return caches.match(request);
  }
}
```

Avec la mise en cache dynamique, les fichiers demandés par l'application sont mis en cache au moment de leur récupération, garantissant qu'ils seront disponibles pour une utilisation future hors ligne.

### **Mise en cache des requêtes API**

Lorsqu'il s'agit de mettre en cache des réponses API, au lieu de mettre en cache la réponse entière, il est souvent préférable de mettre en cache les données spécifiques renvoyées par l'API. Pour cela, nous pouvons utiliser IndexedDB, une base de données locale intégrée au navigateur.

IndexedDB est plus puissante que l'API Cache Storage, en particulier pour stocker et récupérer des données structurées comme le JSON. Cela en fait un excellent choix pour les applications qui nécessitent de stocker des données complexes ou de gérer efficacement de grandes quantités d'informations.

![Une capture d'écran montrant la structure et les données stockées dans IndexedDB pour la PWA MovieMaster.](https://cdn.hashnode.com/res/hashnode/image/upload/v1726726244513/6e99d4b6-fefb-40f1-9ad1-db88c2c7b3da.png align="left")

#### **Comment configurer IndexedDB**

Tout d'abord, créez une fonction pour ouvrir la base de données et créer un magasin d'objets (object store) :

```javascript
const DB_NAME = "MovieMaster";
const DB_VERSION = 1;
const DB_STORE_NAME = "myStore";

function openDb() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION);
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      db.createObjectStore(DB_STORE_NAME, { keyPath: "url" });
    };
  });
}
```

Ensuite, créez des fonctions pour ajouter des données à la base de données et les récupérer :

```javascript
async function addData(url, jsonData) {
  const db = await openDb();
  const transaction = db.transaction(DB_STORE_NAME, "readwrite");
  const store = transaction.objectStore(DB_STORE_NAME);

  const data = {
    url,
    response: JSON.stringify(jsonData),
  };

  const request = store.put(data);
  await new Promise((resolve, reject) => {
    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

async function getData(url) {
  try {
    const db = await openDb();
    const transaction = db.transaction(DB_STORE_NAME, "readonly");
    const store = transaction.objectStore(DB_STORE_NAME);

    const request = store.get(url);

    const result = await new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });

    if (result && result.response) {
      return JSON.parse(result.response);
    }

    return null;
  } catch (error) {
    console.error("Erreur lors de la récupération depuis IndexedDB :", error);
    return null;
  }
}
```

### **Comment servir les ressources mises en cache**

Une fois que nous avons mis en cache nos ressources et stocké les données API dans IndexedDB, l'étape suivante consiste à servir ces données aux utilisateurs lorsqu'ils sont hors ligne. Il existe plusieurs stratégies pour y parvenir :

#### **Stratégie Cache First**

Dans la stratégie Cache First (le cache d'abord), nous vérifions si une ressource est disponible dans le cache. Si c'est le cas, nous la servons depuis le cache ; sinon, nous la récupérons sur le réseau. C'est particulièrement utile pour servir des ressources statiques comme les fichiers HTML, CSS et JavaScript :

```javascript
async function cacheFirstStrategy(request) {
  try {
    const cache = await caches.open(CACHE_NAME);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
      return cachedResponse;
    }

    const networkResponse = await fetch(request);
    const responseClone = networkResponse.clone();
    await cache.put(request, responseClone);
    return networkResponse;
  } catch (error) {
    console.error("La stratégie cache first a échoué :", error);
    return caches.match("/offline");
  }
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (event.request.mode === "navigate") {
    event.respondWith(cacheFirstStrategy(request));
  } else {
    event.respondWith(dynamicCaching(request));
  }
});
```

Dans cette configuration, la stratégie cache-first est appliquée lors de la navigation vers de nouvelles pages, tandis que la mise en cache dynamique gère les autres requêtes.

#### **Stratégie Network First**

La stratégie Network First (le réseau d'abord) est l'opposé : elle tente d'abord de récupérer les ressources sur le réseau, et si le réseau est indisponible, elle se rabat sur le cache. Cette stratégie est particulièrement utile pour les requêtes API où vous voulez les données les plus récentes :

```javascript
async function networkFirstStrategy(request) {
  try {
    const networkResponse = await fetch(request);

    if (networkResponse.ok) {
      const responseClone = networkResponse.clone();
      const responseData = await responseClone.json();
      await addData(request.url, responseData);
      return networkResponse;
    }

    throw new Error("La réponse réseau n'était pas correcte");
  } catch (error) {
    console.error("La stratégie network first a échoué :", error);
    const cachedResponse = await getData(request.url);

    if (cachedResponse) {
      console.log("Utilisation de la réponse en cache :", cachedResponse);
      return new Response(JSON.stringify(cachedResponse), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    }

    return new Response("[]", { status: 200 });
  }
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  const url = new URL(request.url);

  if (url.origin === "https://www.omdbapi.com") {
    event.respondWith(networkFirstStrategy(request));
  } else if (event.request.mode === "navigate") {
    event.respondWith(cacheFirstStrategy(request));
  } else {
    event.respondWith(dynamicCaching(request));
  }
});
```

Dans notre application, nous utilisons la stratégie network-first pour les appels API, garantissant que l'utilisateur obtient les dernières données lorsqu'il est en ligne, tout en se rabattant sur les données mises en cache dans IndexedDB lorsqu'il est hors ligne.

#### **Code complet du Service Worker**

Voici le fichier **service-worker.js** complet qui intègre tout ce dont nous avons discuté :

```javascript
const CACHE_NAME = "MOVIE_MASTER_V1";
const DB_NAME = "MovieMaster";
const DB_VERSION = 1;
const DB_STORE_NAME = "myStore";

async function cacheCoreAssets() {
  const cache = await caches.open(CACHE_NAME);
  return cache.addAll([
    "/",
    "/imdb-logo.svg",
    "/rotten-tomatoes-logo.svg",
    "/offline",
  ]);
}

self.addEventListener("install", (event) => {
  event.waitUntil(cacheCoreAssets());
  self.skipWaiting();
});

async function clearOldCaches() {
  const cacheNames = await caches.keys();
  return Promise.all(
    cacheNames
      .filter((name) => name !== CACHE_NAME)
      .map((name) => caches.delete(name))
  );
}

self.addEventListener("activate", (event) => {
  event.waitUntil(clearOldCaches());
  self.clients.claim();
});

async function dynamicCaching(request) {
  const cache = await caches.open(CACHE_NAME);

  try {
    const response = await fetch(request);
    const responseClone = response.clone();
    await cache.put(request, responseClone);
    return response;
  } catch (error) {
    console.error("La mise en cache dynamique a échoué :", error);
    return caches.match(request);
  }
}

function openDb() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION);
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      db.createObjectStore(DB_STORE_NAME, { keyPath: "url" });
    };
  });
}

async function addData(url, jsonData) {
  const db = await openDb();
  const transaction = db.transaction(DB_STORE_NAME, "readwrite");
  const store = transaction.objectStore(DB_STORE_NAME);

  const data = {
    url,
    response: JSON.stringify(jsonData),
  };

  const request = store.put(data);
  await new Promise((resolve, reject) => {
    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

async function getData(url) {
  try {
    const db = await openDb();
    const transaction = db.transaction(DB_STORE_NAME, "readonly");
    const store = transaction.objectStore(DB_STORE_NAME);

    const request = store.get(url);

    const result = await new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });

    if (result && result.response) {
      return JSON.parse(result.response);
    }

    return null;
  } catch (error) {
    console.error("Erreur lors de la récupération depuis IndexedDB :", error);
    return null;
  }
}

async function cacheFirstStrategy(request) {
  try {
    const cache = await caches.open(CACHE_NAME);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
      return cachedResponse;
    }

    const networkResponse = await fetch(request);
    const responseClone = networkResponse.clone();
    await cache.put(request, responseClone);
    return networkResponse;
  } catch (error) {
    console.error("La stratégie cache first a échoué :", error);
    return caches.match("/offline");
  }
}

async function networkFirstStrategy(request) {
  try {
    const networkResponse = await fetch(request);

    if (networkResponse.ok) {
      const responseClone = networkResponse.clone();
      const responseData = await responseClone.json();
      await addData(request.url, responseData);
      return networkResponse;
    }

    throw new Error("La réponse réseau n'était pas correcte");
  } catch (error) {
    console.error("La stratégie network first a échoué :", error);
    const cachedResponse = await getData(request.url);

    if (cachedResponse) {
      console.log("Utilisation de la réponse en cache :", cachedResponse);
      return new Response(JSON.stringify(cachedResponse), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    }

    return new Response("[]", { status: 200 });
  }
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  const url = new URL(request.url);

  if (url.origin === "https://www.omdbapi.com") {
    event.respondWith(networkFirstStrategy(request));
  } else if (event.request.mode === "navigate") {
    event.respondWith(cacheFirstStrategy(request));
  } else {
    event.respondWith(dynamicCaching(request));
  }
});
```

Avec cette configuration, votre PWA est maintenant entièrement équipée pour gérer le contenu statique et dynamique, fournir une expérience hors ligne et mettre en cache les données API intelligemment.

#### **Lectures complémentaires**

Il existe de nombreuses autres stratégies et nuances pour construire une expérience hors ligne robuste avec les service workers. Si vous souhaitez approfondir ce sujet, envisagez de vous renseigner sur :

* Différentes stratégies de mise en cache : Cache-First, Network-First, Stale-While-Revalidate, etc.
    
* Fonctionnalités avancées des service workers comme la synchronisation en arrière-plan (background sync) et les notifications push.
    
* Meilleures pratiques pour gérer le cache et les limites de stockage.
    

En comprenant et en implémentant ces concepts, vous pouvez vous assurer que votre application reste fonctionnelle et conviviale, même dans des conditions de réseau difficiles.

### **Fournir une page de secours**

Même avec des stratégies de mise en cache en place, il peut arriver que les utilisateurs tentent d'accéder à une ressource qui n'est pas disponible hors ligne et qui n'est pas accessible via le réseau. Pour gérer ces situations avec élégance, nous pouvons créer une page de secours (fallback). Cette page s'affichera chaque fois qu'un utilisateur essaie d'accéder à un contenu qui ne peut être récupéré ni depuis le cache ni depuis le réseau.

Si vous avez cloné le projet d'exemple pour ce tutoriel, vous devriez déjà avoir une page de secours située dans le répertoire app. Cette page est conçue pour gérer les scénarios hors ligne avec élégance et inclut un jeu de Morpion (Tic-Tac-Toe) pour que les utilisateurs puissent jouer en attendant que la connexion soit rétablie. Voici à quoi ressemble la page de secours :

```javascript
"use client";
import TicTacToe from "@/components/TicTacToe";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";

const Fallback: React.FC = () => {
  const [isOnline, setIsOnline] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const handleOnline = () => {
      setIsOnline(true);
      // Rediriger vers la page d'accueil si en ligne
      router.push("/");
    };

    const handleOffline = () => {
      setIsOnline(false);
    };

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, [router]);

  const handleRefresh = () => {
    if (navigator.onLine) {
      router.push("/");
    } else {
      setIsOnline(false);
    }
  };

  return (
    <div className="flex mx-auto h-screen max-w-[500px] w-full flex-col items-center justify-center h-screen bg-foreground text-black p-6 mt-12 text-white">
      <h1 className="text-3xl font-bold mb-6">
        {isOnline ? "Vous êtes en ligne !" : "Vous êtes hors ligne"}
      </h1>
      <p className="text-lg text-center mb-6">
        {isOnline
          ? "Vous êtes de retour en ligne."
          : "Veuillez vérifier votre connexion Internet et réessayer."}
      </p>
      <div className="">
        <TicTacToe />
      </div>
      {isOnline ? (
        <Link
          href={"/"}
          className="mt-6 px-4 py-2 bg-blue-500 text-white rounded shadow hover:bg-blue-600"
        >
          Retour à la page d'accueil
        </Link>
      ) : (
        <button
          onClick={handleRefresh}
          className="mt-6 px-4 py-2 bg-blue-500 text-white rounded shadow hover:bg-blue-600"
        >
          Actualiser
        </button>
      )}
    </div>
  );
};

export default Fallback;
```

![Une image montrant notre page Fallback](https://cdn.hashnode.com/res/hashnode/image/upload/v1726726501345/46e5c3a7-7640-4e54-b6b8-2f43c5b24dcd.png align="left")

**Note :** Vous pouvez personnaliser cette page de secours pour l'adapter aux besoins de votre application, qu'il s'agisse d'afficher un contenu hors ligne utile, de fournir un message ou d'offrir une petite fonctionnalité interactive comme le jeu de Morpion inclus ici.

#### **Mise en cache de la page de secours**

Ensuite, assurez-vous que la page de secours est mise en cache lors de l'installation du service worker :

```javascript
const CACHE_NAME = "MOVIE_MASTER_V1";

async function cacheCoreAssets() {
  const cache = await caches.open(CACHE_NAME);
  return await cache.addAll([
    "/",
    "/fallback",
    // autres ressources
  ]);
}
```

#### **Servir la page de secours**

Enfin, modifiez la fonction `cacheFirstStrategy` pour servir la page **offline.html** lorsqu'une requête échoue :

```javascript
async function cacheFirstStrategy(request) {
  try {
    const cache = await caches.open(CACHE_NAME);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
      return cachedResponse;
    }

    const networkResponse = await fetch(request);
    const responseClone = networkResponse.clone();
    await cache.put(request, responseClone);
    return networkResponse;
  } catch (error) {
    console.error("La stratégie cache first a échoué :", error);
    return caches.match("/offline.html");
  }
}
```

Cette approche garantit que les utilisateurs voient toujours un message significatif au lieu d'une erreur lorsqu'ils sont hors ligne ou lorsqu'une ressource est indisponible.

## **Conclusion**

Avec notre application Next.js configurée, nous l'avons transformée avec succès en une Progressive Web App (PWA) pleinement fonctionnelle, la rendant plus performante et conviviale.

Ce guide a montré comment construire une PWA robuste à l'aide de Next.js en ajoutant des fonctionnalités telles que le support hors ligne, la mise en cache et les service workers. Ces améliorations boostent les performances et offrent une expérience fluide sur tous les appareils, combinant le meilleur du web et des applications natives.

Grâce à ces conseils, vous serez prêt à créer des PWA engageantes, fiables et performantes qui se démarquent dans le monde du développement web.