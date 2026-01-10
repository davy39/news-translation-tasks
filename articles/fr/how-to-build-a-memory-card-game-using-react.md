---
title: Comment créer un jeu de mémoire avec React
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2024-11-27T17:23:51.766Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-memory-card-game-using-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732517515517/1ddfb635-6188-492a-9216-4b35ffb92096.png
tags:
- name: React
  slug: reactjs
- name: Game Development
  slug: game-development
- name: Testing
  slug: testing
- name: Kids
  slug: kids
- name: Anime
  slug: anime
seo_title: Comment créer un jeu de mémoire avec React
seo_desc: 'Recently, while watching my kid 🧒🏻 playing free memory games on her tablet,
  I noticed her struggling with an overwhelming number of ads and annoying pop-up
  banners.

  This inspired me to build a similar game for her. Since she''s currently into anime,...'
---

Récemment, en regardant ma fille 👩🏻‍🦰 jouer à des jeux de mémoire gratuits sur sa tablette, j'ai remarqué qu'elle avait du mal avec un nombre écrasant de publicités et de bannières pop-up ennuyeuses.

Cela m'a inspiré à créer un jeu similaire pour elle. Comme elle est actuellement passionnée par les anime, j'ai décidé de créer le jeu en utilisant des images mignonnes de style anime.

Dans cet article, je vais vous guider à travers le processus de création du jeu pour vous-même ou pour vos enfants 🎮.

Nous commencerons par explorer les fonctionnalités du jeu, puis nous couvrirons la pile technologique et la structure du projet, toutes deux étant simples. Enfin, nous discuterons des optimisations et de la garantie d'un gameplay fluide sur les appareils mobiles 📱.

Si vous souhaitez passer la lecture, [ici](https://github.com/mihailgaberov/memory-card) 💁 est le dépôt GitHub 👍. Et [ici](https://memory-card-blush-pi.vercel.app/) vous pouvez voir la démo en direct.

## **Table des matières**

* [Description du projet](#heading-installation)
    
* [Construisons le jeu](#heading-construisons-le-jeu)
    
* [Tester l'application](#heading-tester-lapplication)
    
* [Mécanisme de secours de l'API](#heading-mecanisme-de-secours-de-lapi)
    
* [Optimisations](#heading-optimisations)
    
* [Améliorations futures](#heading-ameliorations-futures)
    
* [Conclusion](#heading-conclusion)
    

## Description du projet

Dans ce tutoriel, nous allons construire un jeu de mémoire stimulant avec React qui teste vos capacités de rappel. Votre objectif est de cliquer sur des images d'anime uniques sans cliquer deux fois sur la même. Chaque clic unique vous rapporte des points, mais attention, cliquer deux fois sur une image réinitialise votre progression.

![Capture d'écran du jeu de mémoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1732517597049/8677428e-ebd6-4f0b-a1f6-2a2d9f5f2dd2.png align="center")

### Fonctionnalités du jeu:

* 🏮 Un gameplay dynamique qui met au défi votre mémoire
    
* 🔍 Les cartes se mélangent après chaque clic pour augmenter la difficulté
    
* 🏆 Suivi des scores avec persistance du meilleur score
    
* 😺 Des images d'anime adorables de The Nekosia API
    
* ✨ Des transitions de chargement fluides et des animations
    
* 📱 Un design réactif pour tous les appareils
    
* 🎨 Une interface utilisateur propre et moderne
    

Le jeu vous aidera à tester vos compétences en mémoire tout en profitant de jolies images d'anime. Pouvez-vous obtenir le score parfait ?

### Comment jouer

1. Cliquez sur n'importe quelle carte pour commencer
    
2. Rappelez-vous quelles cartes vous avez cliquées
    
3. Essayez de cliquer sur toutes les cartes exactement une fois
    
4. Regardez votre score augmenter avec chaque sélection unique
    
5. Continuez à jouer pour essayer de battre votre meilleur score
    

### La pile technologique

Voici une liste des principales technologies que nous allons utiliser :

* **NPM** – Un gestionnaire de paquets pour JavaScript qui aide à gérer les dépendances et les scripts du projet.
    
* **Vite** – Un outil de construction qui fournit un environnement de développement rapide, particulièrement optimisé pour les projets web modernes.
    
* **React** – Une bibliothèque JavaScript populaire pour construire des interfaces utilisateur, permettant un rendu efficace et une gestion d'état.
    
* **CSS Modules** – Une solution de style qui limite la portée du CSS aux composants individuels, empêchant les conflits de style et assurant la maintenabilité.
    

## Construisons le jeu

À partir de ce point, je vais vous guider à travers le processus que j'ai suivi lors de la construction de ce jeu.

### Structure et architecture du projet

Lors de la construction de ce jeu de mémoire, j'ai soigneusement organisé la base de code pour assurer la maintenabilité, la scalabilité et une séparation claire des préoccupations. Explorons la structure et la raison derrière chaque décision :

![Structure du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1732517663524/648124f0-aa8c-4c50-9292-4bdbd1c9c4db.png align="center")

#### Architecture basée sur les composants

J'ai choisi une architecture basée sur les composants pour plusieurs raisons :

* **Modularité** : Chaque composant est autonome avec sa propre logique et ses styles
    
* **Réutilisabilité** : Les composants comme `Card` et `Loader` peuvent être réutilisés dans toute l'application
    
* **Maintenabilité** : Plus facile à déboguer et à modifier les composants individuels
    
* **Testabilité** : Les composants peuvent être testés de manière isolée
    

#### Organisation des composants

1. Composant Card
    

* Séparé dans son propre répertoire car c'est un élément central du jeu
    
* Contient à la fois les modules JSX et SCSS pour l'encapsulation
    
* Gère le rendu des cartes individuelles, les états de chargement et les événements de clic
    

2. Composant CardsGrid
    

* Gère la disposition du plateau de jeu
    
* Gère le mélange et la distribution des cartes
    
* Contrôle la disposition de la grille réactive pour différentes tailles d'écran
    

3. Composant Loader
    

* Indicateur de chargement réutilisable
    
* Améliore l'expérience utilisateur pendant le chargement des images
    
* Peut être utilisé par n'importe quel composant ayant besoin d'états de chargement
    

4. Composants Header/Footer/Subtitle
    

* Composants structurels pour la disposition de l'application
    
* Header affiche le titre du jeu et les scores
    
* Footer montre les informations de copyright et de version
    
* Subtitle fournit les instructions du jeu
    

#### Approche des modules CSS

J'ai utilisé les modules CSS (fichiers `.module.scss`) pour plusieurs avantages :

* **Styling à portée limitée** : Empêche les fuites de style entre les composants
    
* **Collisions de noms** : Génère automatiquement des noms de classe uniques
    
* **Maintenabilité** : Les styles sont co-localisés avec leurs composants
    
* **Fonctionnalités SCSS** : Utilise les fonctionnalités SCSS tout en gardant les styles modulaires
    

#### Hooks personnalisés

Le répertoire `hooks` contient des hooks personnalisés comme useFetch :

* **Séparation des préoccupations** : Isole la logique de récupération des données
    
* **Réutilisabilité** : Peut être utilisé par n'importe quel composant ayant besoin de données d'image
    
* **Gestion d'état** : Gère les états de chargement, d'erreur et de données
    
* **Performance** : Implémente des optimisations comme le contrôle de la taille des images
    

#### Fichiers de niveau racine

#### App.jsx :

* Agit comme point d'entrée de l'application
    
* Gère l'état global et le routage (si nécessaire)
    
* Coordonne la composition des composants
    
* Gère les dispositions de haut niveau
    

#### Considérations de performance

La structure supporte les optimisations de performance :

* **Fractionnement du code** : Les composants peuvent être chargés de manière paresseuse si nécessaire
    
* **Mémoisation** : Les composants peuvent être mémoisés efficacement
    
* **Chargement des styles** : Les modules CSS permettent un chargement efficace des styles
    
* **Gestion des actifs** : Les images et les ressources sont correctement organisées
    

#### Scalabilité

Cette structure permet une mise à l'échelle facile :

* De nouvelles fonctionnalités peuvent être ajoutées sous forme de nouveaux composants
    
* Des hooks supplémentaires peuvent être créés pour de nouvelles fonctionnalités
    
* Les styles restent maintenables à mesure que l'application grandit
    
* Les tests peuvent être implémentés à tout niveau
    

#### Expérience de développement

La structure améliore l'expérience du développeur :

* Organisation claire des fichiers
    
* Emplacements intuitifs des composants
    
* Facile à trouver et à modifier des fonctionnalités spécifiques
    
* Supporte une collaboration efficace
    

Cette architecture s'est avérée particulièrement précieuse lors de l'optimisation du jeu pour une utilisation sur tablette, car elle m'a permis de :

1. Identifier et optimiser facilement les goulots d'étranglement de performance
    
2. Ajouter des styles spécifiques aux tablettes sans affecter les autres appareils
    
3. Implémenter des états de chargement pour une meilleure expérience mobile
    
4. Maintenir une séparation claire entre la logique du jeu et les composants UI
    

D'accord, maintenant commençons à coder.

## Guide de construction étape par étape

### 1. Configuration du projet

**Configurer l'environnement de développement**

Pour commencer avec un projet React propre, ouvrez votre application de terminal et exécutez les commandes suivantes (vous pouvez nommer votre dossier de projet comme vous le souhaitez - dans mon cas, le nom est 'memory-card') :

```bash
npm create vite@latest memory-card -- --template react
cd memory-card
npm install
```

**Installer les dépendances requises**

Les seules dépendances que nous utiliserons dans ce projet sont le package de hooks de UI.dev (au fait, [ici](https://ui.dev/why-react-renders) vous pouvez trouver un article bien expliqué sur le fonctionnement du rendu dans React).

L'autre dépendance est le célèbre préprocesseur CSS, [SASS](https://sass-lang.com/), dont nous aurons besoin pour pouvoir écrire nos modules CSS en SASS au lieu de CSS régulier.

```javascript
npm install @uidotdev/usehooks sass
```

**Configurer Vite et les paramètres du projet**

Lors de la configuration de notre projet, nous devons apporter quelques ajustements de configuration spécifiques pour gérer les avertissements SASS et améliorer notre expérience de développement. Voici comment vous pouvez configurer Vitest :

```javascript
// vitest.config.js
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./src/setupTests.js'],
    css: {
      modules: {
        classNameStrategy: 'non-scoped'
      }
    },
    preprocessors: {
      '**/*.scss': 'sass'
    },
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'src/setupTests.js',
        'src/main.jsx',
        'src/vite-env.d.ts',
      ],
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        quietDeps: true,  // Supprime les avertissements de dépendance SASS
        charset: false    // Empêche l'avertissement de charset dans les versions récentes de SASS
      }
    }
  }
});
```

Gardez à l'esprit que la plupart de ces configurations sont générées automatiquement pour vous lorsque vous créez le projet avec Vite. Voici ce qui se passe :

1. **Configuration SASS** :
    
    * `quietDeps: true` : Cela supprime les avertissements concernant les dépendances obsolètes dans les modules SASS. Particulièrement utile lorsque vous travaillez avec des fichiers SASS/SCSS tiers.
        
    * `charset: false` : Empêche l'avertissement "@charset" qui apparaît dans les nouvelles versions de SASS lorsque vous utilisez des caractères spéciaux dans vos feuilles de style.
        
2. **Configuration des tests** :
    
    * `globals: true` : Rend les fonctions de test globalement disponibles dans les fichiers de test
        
    * `environment: 'jsdom'` : Fournit un environnement DOM pour les tests
        
    * `setupFiles` : Pointe vers notre fichier de configuration de test
        

Ces configurations aident à créer une expérience de développement plus propre en supprimant les messages d'avertissement inutiles dans la console, en configurant les paramètres de l'environnement de test et en garantissant que le traitement SASS/SCSS fonctionne en douceur.

Vous pourriez voir des avertissements dans votre console sans ces configurations lorsque :

* Vous utilisez des fonctionnalités SASS/SCSS ou importez des fichiers SASS
    
* Vous exécutez des tests qui nécessitent une manipulation du DOM
    
* Vous utilisez des caractères spéciaux dans vos feuilles de style
    

### **2. Construction des composants**

**Créer le composant Card**

Tout d'abord, créons notre composant de carte de base qui affichera des images individuelles :

```javascript
// src/components/Card/Card.jsx
import React, { useState, useCallback } from "react";
import Loader from "../Loader";
import styles from "./Card.module.scss";

const Card = React.memo(function Card({ imgUrl, imageId, categoryName, processTurn }) {
  const [isLoading, setIsLoading] = useState(true);

  const handleImageLoad = useCallback(() => {
    setIsLoading(false);
  }, []);

  const handleClick = useCallback(() => {
    processTurn(imageId);
  }, [processTurn, imageId]);

  return (
    <div className={styles.container} onClick={handleClick}>
      {isLoading && (
        <div className={styles.loaderContainer}>
          <Loader message="Chargement..." />
        </div>
      )}
      <img
        src={imgUrl}
        alt={categoryName}
        onLoad={handleImageLoad}
        className={`${styles.image} ${isLoading ? styles.hidden : ''}`}
      />
    </div>
  );
});

export default Card;
```

Le composant Card est un élément fondamental de notre jeu. Il est responsable de l'affichage des images individuelles et de la gestion des interactions des joueurs. Décomposons son implémentation :

#### **Détail des props :**

1. `image` : (string)
    
    * L'URL de l'image à afficher qui est reçue de notre service API.
        
    * Elle est utilisée directement dans l'attribut src de la balise img.
        
2. `id` : (string)
    
    * Identifiant unique pour chaque carte qui est crucial pour suivre les cartes qui ont été cliquées.
        
    * Il est passé à la fonction de rappel `processTurn` lorsqu'une carte est cliquée.
        
3. `category` : (string)
    
    * Décrit le type d'image (par exemple, "anime", "neko"), et il est utilisé dans l'attribut alt pour une meilleure accessibilité.
        
    * Il aide avec le SEO et les lecteurs d'écran.
        
4. `processTurn` : (function)
    
    * Fonction de rappel passée depuis le composant parent qui gère la logique du jeu lorsqu'une carte est cliquée.
        
    * Elle gère également les mises à jour des scores et les changements d'état du jeu et détermine si une carte a été cliquée auparavant.
        
5. `isLoading` : (boolean)
    
    * Contrôle si un état de chargement doit être affiché. Lorsqu'il est vrai, il affiche un composant Loader au lieu de l'image.
        
    * Il améliore l'expérience utilisateur pendant le chargement de l'image.
        

#### **Style du composant :**

```javascript
// src/components/Card/Card.module.scss
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 30px;
  text-align: center;
  min-height: 200px;
  position: relative;
  cursor: pointer;
  transition: transform 0.2s ease;

  &:hover {
    transform: scale(1.02);
  }

  .image {
    width: 10rem;
    height: auto;
    opacity: 1;
    transition: opacity 0.3s ease;

    &.hidden {
      opacity: 0;
    }
  }

  .loaderContainer {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}
```

#### **Utilisation dans le composant :**

```javascript
<Card
    key={getKey()}
    imgUrl={item?.image?.original?.url || ""}
    imageId={item?.id}
    categoryName={item?.category}
    processTurn={(imageId) => processTurn(imageId)} 
/>
```

#### **Fonctionnalités clés :**

1. **Optimisation des performances :**
    
    * Utilise `React.memo` pour éviter les re-rendus inutiles
        
    * Implémente `useCallback` pour les gestionnaires d'événements
        
    * Gère l'état de chargement en interne pour une meilleure UX
        
2. **Gestion de l'état de chargement :**
    
    * État interne `isLoading` pour suivre le chargement de l'image
        
    * Affiche un composant Loader avec un message pendant le chargement
        
    * Cache l'image jusqu'à ce qu'elle soit complètement chargée en utilisant des classes CSS
        
3. **Gestion des événements :**
    
    * `handleImageLoad` : Gère la transition de l'état de chargement
        
    * `handleClick` : Traite les mouvements du joueur via la fonction de rappel `processTurn`
        

**Construire le composant CardsGrid**

C'est notre composant principal de jeu qui gère l'état du jeu, la logique des scores et les interactions des cartes. Décomposons son implémentation :

```javascript

// src/components/CardsGrid/CardsGrid.jsx
import React, { useState, useEffect } from "react";
import { useLocalStorage } from "@uidotdev/usehooks";
import Card from "../Card";
import Loader from "../Loader";
import styles from "./CardsGrid.module.scss";
import useFetch from "../../hooks/useFetch";

function CardsGrid(data) {
  // Gestion de l'état
  const [images, setImages] = useState(data?.data?.images || []);
  const [clickedImages, setClickedImages] = useLocalStorage("clickedImages", []);
  const [score, setScore] = useLocalStorage("score", 0);
  const [bestScore, setBestScore] = useLocalStorage("bestScore", 0);
  const [isLoading, setIsLoading] = useState(!data?.data?.images?.length);
  
  // Hook personnalisé pour récupérer les images
  const { data: fetchedData, fetchData, error } = useFetch();

  // Mettre à jour les images lorsque de nouvelles données sont récupérées
  useEffect(() => {
    if (fetchedData?.images) {
      setImages(fetchedData.images);
      setIsLoading(false);
      // Réinitialiser les images cliquées lorsqu'un nouveau lot est chargé
      setClickedImages([]);
    }
  }, [fetchedData]);

  // Fonction auxiliaire pour mettre à jour le meilleur score
  function updateBestScore(currentScore) {
    if (currentScore > bestScore) {
      setBestScore(currentScore);
    }
  }

  // Logique principale du jeu
  function processTurn(imageId) {
    const newClickedImages = [...clickedImages, imageId];
    setClickedImages(newClickedImages);

    // Si on clique deux fois sur la même image, tout réinitialiser
    if (clickedImages.includes(imageId)) {
      // Mettre à jour le meilleur score si nécessaire
      updateBestScore(score);
      
      setClickedImages([]);
      setScore(0);
    } else {
      // Gérer la sélection réussie de la carte
      const newScore = score + 1;
      setScore(newScore);

      // Vérifier le score parfait (toutes les cartes cliquées une fois)
       if (newClickedImages.length === images.length) {
        updateBestScore(newScore);
        fetchData();
        setClickedImages([]);
      } else {
        // Mélanger les images
        const shuffled = [...images].sort(() => Math.random() - 0.5);
        setImages(shuffled);
      }
    }
  }

 if (error) {
    return <p>Échec de la récupération des données</p>;
  }

  if (isLoading) {
    return <Loader message="Chargement des nouvelles images..." />;
  }

  return (
    <div className={styles.container}>
      {images.map((item) => (
        <Card
          key={getKey()}
          imgUrl={item?.image?.original?.url || ""}
          imageId={item?.id}
          categoryName={item?.category}
          processTurn={(imageId) => processTurn(imageId)}
        />
      ))}
    </div>
  );
}

export default React.memo(CardsGrid);
```

#### **Style du composant :**

```scss
.container {
  display: grid;
  gap: 1rem 1rem;
  grid-template-columns: auto; /* Par défaut : une colonne pour mobile-first */
  background-color: #2196f3;
  padding: 0.7rem;
  cursor: pointer;
}

@media (min-width: 481px) {
  .container {
    grid-template-columns: auto auto; /* Deux colonnes pour les tablettes et plus */
  }
}

@media (min-width: 769px) {
  .container {
    grid-template-columns: auto auto auto; /* Trois colonnes pour les ordinateurs de bureau et plus grands */
  }
}
```

#### **Détail des fonctionnalités clés :**

1. **Gestion de l'état :**
    
    * Utilise `useState` pour l'état au niveau du composant
        
    * Implémente `useLocalStorage` pour les données de jeu persistantes :
        
        * `clickedImages` : Suivi des cartes qui ont été cliquées
            
        * `score` : Score actuel du jeu
            
        * `bestScore` : Meilleur score atteint
            
    * Gère l'état de chargement pour la récupération des images
        
    * Mélange les cartes
        
2. **Logique du jeu :**
    
    * `processTurn` : Gère les mouvements du joueur
        
        * Suivi des clics en double
            
        * Mise à jour des scores
            
        * Gestion des scénarios de score parfait
            
    * `updateBestScore` : Met à jour le meilleur score lorsque nécessaire
        
    * Récupère automatiquement de nouvelles images lorsqu'une manche est terminée
        
3. **Récupération des données :**
    
    * Utilise le hook personnalisé `useFetch` pour les données d'image
        
    * Gère les états de chargement et d'erreur
        
    * Met à jour les images lorsque de nouvelles données sont récupérées
        
4. **Optimisation des performances :**
    
    * Composant enveloppé dans `React.memo`
        
    * Mises à jour d'état efficaces
        
    * Disposition de grille réactive
        
5. **Persistance :**
    
    * L'état du jeu persiste à travers les rechargements de page
        
    * Suivi du meilleur score
        
    * Sauvegarde de la progression actuelle du jeu
        

#### **Exemple d'utilisation :**

```javascript
...
...

function App() {
  const { data, loading, error } = useFetch();

  if (loading) return <Loader />;
  if (error) return <p>Erreur : {error}</p>;

  return (
    <div className={styles.container}>
      <Header />
      <Subtitle />
      <CardsGrid data={data} />
      <Footer />
    </div>
  );
}
export default App;
```

Le composant CardsGrid sert de cœur à notre jeu de mémoire, gérant :

* L'état et la logique du jeu
    
* Le suivi des scores
    
* Les interactions des cartes
    
* Le chargement et l'affichage des images
    
* La disposition réactive
    
* La persistance des données
    

Cette implémentation offre une expérience de jeu fluide tout en maintenant la lisibilité et la maintenabilité du code grâce à une séparation claire des préoccupations et une gestion appropriée de l'état.

### **3.** Implémentation de la couche API

Notre jeu utilise une couche API robuste avec plusieurs options de secours pour garantir une livraison fiable des images. Implémentons chaque service et le mécanisme de secours.

**Configurer le service API principal :**

```javascript
// src/services/api/nekosiaApi.js
const NEKOSIA_API_URL = "https://api.nekosia.cat/api/v1/images/catgirl";

export async function fetchNekosiaImages() {
  const response = await fetch(
    `${NEKOSIA_API_URL}?count=21&additionalTags=white-hair,uniform&blacklistedTags=short-hair,sad,maid&width=300`
  );

  if (!response.ok) {
    throw new Error(`Erreur de l'API Nekosia : ${response.status}`);
  }

  const result = await response.json();

  if (!result.images || !Array.isArray(result.images)) {
    throw new Error('Format de réponse invalide de l\'API Nekosia');
  }

  const validImages = result.images.filter(item => item?.image?.original?.url);

  if (validImages.length === 0) {
    throw new Error('Aucune image valide reçue de l\'API Nekosia');
  }

  return { ...result, images: validImages };
}
```

**Créer le premier service API de secours :**

```javascript
// src/services/api/nekosBestApi.js
const NEKOS_BEST_API_URL = "https://nekos.best/api/v2/neko?amount=21";

export async function fetchNekosBestImages() {
  const response = await fetch(NEKOS_BEST_API_URL, {
    method: "GET",
    mode: "no-cors"
  });

  if (!response.ok) {
    throw new Error(`Erreur de l\'API Nekos Best : ${response.status}`);
  }

  const result = await response.json();

  // Transformer la réponse pour qu\'elle corresponde à notre format attendu
  const transformedImages = result.results.map(item => ({
    id: item.url.split('/').pop().split('.')[0], // Extraire l\'UUID de l\'URL
    image: {
      original: {
        url: item.url
      }
    },
    artist: {
      name: item.artist_name,
      href: item.artist_href
    },
    source: item.source_url
  }));

  return { images: transformedImages };
}
```

**Créer le deuxième service API de secours :**

```javascript
// src/services/api/nekosApi.js
const NEKOS_API_URL = "https://api.nekosapi.com/v3/images/random?limit=21&rating=safe";

export async function fetchNekosImages() {
  const response = await fetch(NEKOS_API_URL, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Erreur de l\'API Nekos : ${response.status}`);
  }

  const result = await response.json();

  // Transformer la réponse pour qu\'elle corresponde à notre format attendu
  const transformedImages = result.items.map(item => ({
    id: item.id,
    image: {
      original: {
        url: item.image_url
      }
    }
  }));

  return { images: transformedImages };
}
```

**Construire le mécanisme de secours de l'API :**

```javascript
// src/services/api/imageService.js
import { fetchNekosiaImages } from "./nekosiaApi";
import { fetchNekosImages } from "./nekosApi";
import { fetchNekosBestImages } from "./nekosBestApi";

export async function fetchImages() {
  try {
    // Essayer d\'abord l\'API principale
    return await fetchNekosiaImages();
  } catch (error) {
    console.warn("L\'API principale a échoué, tentative de secours :", error);

    // Essayer la première API de secours
    try {
      return await fetchNekosBestImages();
    } catch (fallbackError) {
      console.warn("La première API de secours a échoué, tentative du deuxième secours :", fallbackError);

      // Essayer la deuxième API de secours
      try {
        return await fetchNekosImages();
      } catch (secondFallbackError) {
        console.error("Toutes les API d\'images ont échoué :", secondFallbackError);
        throw new Error("Toutes les API d\'images ont échoué");
      }
    }
  }
}
```

**Utiliser le service d'images :**

```javascript
// src/hooks/useFetch.js
import { useState, useEffect } from "react";
import { fetchImages } from "../services/api/imageService";

export default function useFetch() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await fetchImages();
      setData(result);
    } catch (err) {
      setError(err.message || 'Une erreur est survenue');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return {
    data,
    loading,
    error,
    fetchData,
  };
}
```

#### **Fonctionnalités clés de notre implémentation API :**

1. **Plusieurs sources API :**
    
    * API principale (Nekosia) : Fournit des images anime de haute qualité
        
    * Premier secours (Nekos Best) : Inclut des informations sur l'artiste
        
    * Deuxième secours (Nekos) : Sauvegarde simple et fiable
        
2. **Format de données cohérent :**
    
    * Toutes les API transforment leurs réponses pour qu'elles correspondent à notre format attendu :
        
    
    ```json
    {
      images: [
        {
          id: string,
          image: {
            original: {
              url: string
            }
          }
        }
      ]
    }
    ```
    
3. **Gestion robuste des erreurs :**
    
    * Valide les réponses de l'API
        
    * Vérifie les URL d'images valides
        
    * Fournit des messages d'erreur détaillés
        
    * Mécanisme de secours élégant
        
4. **Fonctionnalités de sécurité :**
    
    * Filtre de contenu sûr (`rating=safe`)
        
    * Limitation du nombre d'images (21 images)
        
    * Validation des URL
        
    * Validation du format de réponse
        
5. **Considérations de performance :**
    
    * Tailles d'images optimisées
        
    * Balises de contenu filtrées
        
    * Transformation de données efficace
        
    * Appels API minimaux
        

Cette implémentation garantit que notre jeu dispose d'une source fiable d'images tout en gérant les échecs potentiels de l'API de manière élégante. Le format de données cohérent sur toutes les API facilite le passage de l'une à l'autre sans affecter la fonctionnalité du jeu.

## Tester l'application

Les tests sont une partie cruciale du développement de toute application, et pour notre jeu de mémoire, nous avons mis en place une stratégie de test complète en utilisant des outils et des pratiques modernes. Plongeons dans la manière dont nous avons structuré nos tests et certains modèles de test clés que nous avons utilisés.

![Exécution des tests](https://cdn.hashnode.com/res/hashnode/image/upload/v1732517719141/8b034f36-761e-4433-acfd-82a2c4cffffc.png align="center")

### Pile de tests

* **Vitest** : Notre framework de test principal, choisi pour sa rapidité et son intégration transparente avec Vite
    
* **React Testing Library** : Pour tester les composants React avec une approche centrée sur l'utilisateur
    
* **@testing-library/user-event** : Pour simuler les interactions utilisateur
    
* **jsdom** : Pour créer un environnement DOM dans nos tests
    

### Modèles de test clés

Les tests ont été une partie cruciale pour garantir la fiabilité et la maintenabilité de ce jeu de mémoire. J'ai mis en place une stratégie de test complète en utilisant React Testing Library et Vitest, en me concentrant sur plusieurs domaines clés :

#### 1. Test des composants

J'ai écrit des tests approfondis pour mes composants React afin de m'assurer qu'ils s'affichent correctement et se comportent comme prévu. Par exemple, le composant `CardsGrid`, qui est le cœur du jeu, a une couverture de test approfondie incluant :

* Les états de rendu initiaux
    
* Les états de chargement
    
* La gestion des erreurs
    
* Le suivi des scores
    
* Le comportement des interactions avec les cartes
    

#### 2. Mocking des tests

Pour garantir des tests fiables et rapides, j'ai mis en place plusieurs stratégies de mocking :

* Les opérations de stockage local utilisant le hook useLocalStorage
    
* Les appels API utilisant le hook `useFetch`
    
* Les gestionnaires d'événements et les mises à jour d'état
    

#### 3. Bonnes pratiques de test

Tout au long de la mise en œuvre de mes tests, j'ai suivi plusieurs bonnes pratiques :

* Utilisation des hooks `beforeEach` et `afterEach` pour réinitialiser l'état entre les tests
    
* Test des interactions utilisateur en utilisant `fireEvent` de React Testing Library
    
* Écriture de tests qui ressemblent à la manière dont les utilisateurs interagissent avec l'application
    
* Test des scénarios de succès et d'erreur
    
* Isolation des tests en utilisant un mocking approprié
    

#### 4. Outils de test

Le projet utilise des outils et bibliothèques de test modernes :

* **Vitest** : Comme exécuteur de tests
    
* **React Testing Library** : Pour tester les composants React
    
* **@testing-library/jest-dom** : Pour des assertions de test DOM améliorées
    
* **@testing-library/user-event** : Pour simuler les interactions utilisateur
    

Cette approche de test complète m'a aidé à détecter les bugs tôt, à garantir la qualité du code et à rendre le refactoring plus sûr et plus gérable.

## Optimisations

Pour garantir des performances fluides, en particulier sur les appareils mobiles, nous avons mis en place plusieurs techniques d'optimisation :

1. **Transformation de la réponse**
    
    * Format de données standardisé sur toutes les API
        
    * Extraction efficace des identifiants à partir des URL
        
    * Métadonnées d'image structurées pour un accès rapide
        
2. **Optimisation du réseau**
    
    * Utilisation du mode `no-cors` lorsque cela est approprié pour gérer efficacement les problèmes CORS
        
    * Gestion des erreurs avec des codes de statut spécifiques pour un meilleur débogage
        
    * Structure de réponse cohérente sur toutes les implémentations d'API
        
3. **Considérations pour les mobiles d'abord**
    
    * Stratégie de chargement des images optimisée
        
    * Gestion efficace des erreurs pour éviter les nouvelles tentatives inutiles
        
    * Transformation de données rationalisée pour réduire la surcharge de traitement
        

## **Améliorations futures**

Il existe plusieurs façons d'améliorer davantage ce projet :

1. **Mise en cache des réponses de l'API**
    
    * Implémenter la mise en cache du stockage local pour les images fréquemment utilisées
        
    * Ajouter une stratégie d'invalidation du cache pour un contenu frais
        
    * Implémenter le chargement progressif des images
        
2. **Optimisations des performances**
    
    * Ajouter le chargement paresseux des images pour un meilleur temps de chargement initial
        
    * Implémenter la mise en file d'attente des requêtes pour une meilleure gestion de la bande passante
        
    * Ajouter la compression des réponses pour un transfert de données plus rapide
        
3. **Améliorations de la fiabilité**
    
    * Ajouter la vérification de l'état de l'API avant les tentatives
        
    * Implémenter des mécanismes de nouvelle tentative avec un délai exponentiel
        
    * Ajouter un modèle de disjoncteur pour les API défaillantes
        
4. **Analytique et surveillance**
    
    * Suivre les taux de réussite de l'API
        
    * Surveiller les temps de réponse
        
    * Implémenter le basculement automatique de l'API en fonction des métriques de performance
        

Cette implémentation robuste garantit que notre jeu reste fonctionnel et performant même dans des conditions réseau défavorables ou en cas d'indisponibilité de l'API, tout en laissant de la place pour des améliorations et optimisations futures.

## Conclusion

Construire ce jeu de mémoire a été plus qu'une simple création d'une alternative amusante et sans publicité pour les enfants - c'est un exercice de mise en œuvre des meilleures pratiques de développement web moderne tout en résolvant un problème réel.

Le projet démontre comment combiner une architecture réfléchie, des tests robustes et des mécanismes de secours fiables peut aboutir à une application prête pour la production, à la fois divertissante et éducative.

### 🛠️ Points clés à retenir

1. **Développement centré sur l'utilisateur**
    
    * Commencé avec un problème clair (les jeux remplis de publicités affectant l'expérience utilisateur)
        
    * Implémenté des fonctionnalités qui améliorent le gameplay sans interruptions
        
    * Maintenu l'accent sur la performance et la fiabilité sur tous les appareils
        
2. **Excellence technique**
    
    * Utilisé des modèles React modernes et des hooks pour un code propre et maintenable
        
    * Implémenté une stratégie de test complète garantissant la fiabilité
        
    * Créé un système de secours API robuste pour un gameplay ininterrompu
        
3. **Performance d'abord**
    
    * Adopté une approche mobile-first avec un design réactif
        
    * Optimisé le chargement et la gestion des images
        
    * Implémenté une gestion d'état et des stratégies de mise en cache efficaces
        

### 📚 Résultats d'apprentissage

Ce projet montre comment des jeux en apparence simples peuvent être d'excellents véhicules pour la mise en œuvre de solutions techniques complexes. De l'architecture des composants aux secours API, chaque fonctionnalité a été construite avec la scalabilité et la maintenabilité à l'esprit, prouvant que même les projets de loisirs peuvent maintenir une qualité de code de niveau professionnel.

### 🔮 Aller de l'avant

Bien que le jeu atteigne avec succès son objectif principal de fournir une expérience agréable et sans publicité, les améliorations futures documentées fournissent une feuille de route claire pour l'évolution. Qu'il s'agisse de mettre en œuvre des optimisations supplémentaires ou d'ajouter de nouvelles fonctionnalités, la fondation est solide et prête pour l'expansion.

Le jeu de mémoire est un témoignage de la manière dont les projets personnels peuvent à la fois résoudre des problèmes réels et servir de plateformes pour la mise en œuvre des meilleures pratiques en développement web moderne. N'hésitez pas à explorer le [code](https://github.com/mihailgaberov/memory-card), à contribuer ou à l'utiliser comme inspiration pour vos propres projets !