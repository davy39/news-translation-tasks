---
title: Comment améliorer votre flux de développement Front-End avec la bibliothèque
  ZenUI
subtitle: ''
author: Asfak Ahmed
co_authors: []
series: null
date: '2024-10-02T18:48:21.600Z'
originalURL: https://freecodecamp.org/news/improve-front-end-development-workflow-with-zenui-library
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727705676968/5e8a0836-8f8b-4ce3-a2fb-d98b2bd1eabe.png
tags:
- name: zenui library
  slug: zenui-library
- name: zenui
  slug: zenui
- name: UI library
  slug: ui-library
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Comment améliorer votre flux de développement Front-End avec la bibliothèque
  ZenUI
seo_desc: 'Hello everyone! In this guide, you’ll learn about the powerful ZenUI Library.
  It’s a comprehensive, free collection of UI components and templates designed to
  enhance your development workflow and elevate your projects.

  Whether you’re a developer loo...'
---

Bonjour à tous ! Dans ce guide, vous apprendrez à utiliser la puissante bibliothèque [**ZenUI**](https://zenui.net). Il s'agit d'une collection complète et gratuite de composants et de modèles d'interface utilisateur conçus pour améliorer votre flux de développement et élever vos projets.

Que vous soyez un développeur cherchant à accélérer la conception de votre interface utilisateur ou une entreprise ayant besoin de modèles modernes et élégants, la bibliothèque ZenUI dispose de tout ce dont vous avez besoin pour créer des sites web magnifiques avec un minimum d'effort.

### **Table des matières :**

* [Pourquoi utiliser ZenUI](#heading-pourquoi-utiliser-zenui) ?
    
* [Fonctionnalités de ZenUI](#heading-fonctionnalites-de-zenui)
    
* [Intégration de Tailwind CSS et compatibilité des frameworks](#heading-integration-de-tailwind-css-et-compatibilite-des-frameworks)
    
* [Comment commencer à utiliser ZenUI](#heading-comment-commencer-a-utiliser-zenui)
    
* [Comment personnaliser les composants ZenUI](#heading-comment-personnaliser-les-composants-zenui)
    
* [Comment utiliser les modèles de site web ZenUI](#heading-comment-utiliser-les-modeles-de-site-web-zenui)
    
* [Comment extraire les couleurs d'une image](#heading-comment-extraire-les-couleurs-dune-image)
    
* [Comment personnaliser n'importe quelle icône dans la bibliothèque ZenUI](#heading-comment-personnaliser-nimporte-quelle-icone-dans-la-bibliotheque-zenui)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi utiliser ZenUI ?

ZenUI est né du besoin de composants propres, personnalisables et réutilisables que vous pouvez facilement intégrer dans divers projets.

Contrairement à d'autres bibliothèques, ZenUI se concentre sur la fourniture d'une collection de composants **sur mesure**, garantissant que vos projets sont uniques et hautement fonctionnels.

Vous pouvez visiter leur site web pour en savoir plus : [https://zenui.net](https://zenui.net).

### Avantages clés de ZenUI :

* **Totalement gratuit** : Aucun coût caché. La bibliothèque ZenUI est et restera gratuite pour tous les utilisateurs.
    
* **Composants UI modernes** : Composants préconçus, entièrement réactifs, basés sur les normes web modernes.
    
* **Personnalisable** : Vous pouvez facilement modifier les composants pour qu'ils correspondent à la marque et au style de votre projet.
    
* **Convivial pour les développeurs** : Conçue en pensant aux développeurs, les composants ZenUI sont bien documentés, faciles à intégrer et viennent avec un code propre et sémantique.
    
* **Icônes personnalisables** : Accédez à une vaste bibliothèque d'icônes que vous pouvez personnaliser et télécharger en **PNG** ou **SVG**, ou simplement copier le code de l'icône pour l'utiliser directement dans votre projet. Personnalisez les couleurs, les tailles et les styles sans effort pour répondre à vos besoins.
    
* **Générateur de palette de couleurs** : Concevez des schémas de couleurs époustouflants avec le générateur de palette de couleurs intégré. Vous pouvez télécharger une image et extraire ses couleurs dominantes, puis générer et personnaliser une palette de couleurs complète basée sur vos choix. Que ce soit pour des éléments d'interface utilisateur ou de branding, cet outil garantit l'harmonie des couleurs de votre design.
    

## Fonctionnalités de ZenUI

ZenUI propose de nombreuses fonctionnalités conçues pour rationaliser votre développement d'interface utilisateur. Explorons chaque fonctionnalité et voyons comment elle peut vous être bénéfique.

### **1. Composants UI préconstruits**

ZenUI fournit de nombreux composants UI préconstruits pour rationaliser votre processus de développement. Voici la liste complète de ce que vous obtenez :

* `Boutons`
    
* `Barres de navigation`
    
* `Cartes`, `Modales et Popups`
    
* `Formulaires et Entrées`
    
* `Accordéons`
    
* `Menus déroulants et Menus`
    
* `Barres de progression et Chargeurs`
    
* `Onglets`
    
* `Badges et Info-bulles`
    
* `Notifications Toast`
    
* `Grilles et Mises en page réactives`
    
* `Pagination`
    
* `Avatars`
    
* `Fil d'Ariane`
    
* `Cases à cocher`
    
* `Boutons radio`
    
* `Alertes`
    
* `Pieds de page`
    
* `En-têtes`
    
* `Barres latérales`
    
* `Barres de recherche`
    
* `Chronologies`
    
* `Puces de balises`
    
* `Indicateurs de chargement`
    
* `Chargeurs squelettes`
    
* `Galeries d'images`
    
* `Tableaux de tarifs`
    
* `Sections Hero`
    

Avec cette collection exhaustive, ZenUI vous équipe pour construire rapidement des interfaces utilisateur réactives et visuellement attrayantes.

### **2. Extracteur de couleurs d'image**

Pour les designers qui ont besoin d'une inspiration de couleurs précise, ZenUI offre un outil d'extraction de couleurs d'image. Il vous permet de :

* **Extraire les couleurs** : Téléchargez une image, et l'outil détectera et générera automatiquement une palette de ses couleurs dominantes.
    
* **Sélecteur de couleurs** : Sélectionnez manuellement n'importe quel point sur l'image pour affiner votre palette.
    

Cette fonctionnalité aide à rationaliser votre processus de design en fournissant des combinaisons de couleurs précises et vibrantes directement à partir de vos images, garantissant que vos projets ont des schémas de couleurs cohérents et percutants.

### **3. Galerie de modèles**

Pour les développeurs et designers cherchant un coup de pouce, ZenUI inclut des **collections de modèles** comme :

* **Sites web d'entreprise** : Construisez des sites web multi-pages pour les entreprises en quelques clics.
    
* **Pages de destination** : Pages de destination propres et modernes optimisées pour les conversions.
    

Chaque modèle est conçu en gardant à l'esprit les meilleures pratiques UX, garantissant une expérience utilisateur fluide sur tous les appareils.

### **4. Blocs UI essentiels**

Avec **ZenUI Blocks**, vous n'avez pas besoin de construire à partir de zéro. Ces blocs sont des sections préconçues conçues pour vous aider à construire des pages web entières rapidement et efficacement. Voici la liste complète des blocs que vous pouvez utiliser :

* `Sections Hero`
    
* `Navbar réactive`
    
* `Sections de tarifs`
    
* `Pied de page réactif`
    
* `Formulaire de newsletter`
    
* `Formulaire de contact`
    
* `Barre de recherche réactive`
    
* `Barre latérale réactive`
    
* `Sections d'appel à l'action`
    
* `Pages d'erreur 404`
    
* `Page vide`
    

Tous les blocs sont entièrement personnalisables avec un minimum d'effort, vous permettant de construire des sites web plus rapidement tout en garantissant un look poli et professionnel.

### **5. Collection d'icônes SVG**

ZenUI 2.0 est livré avec un ensemble d'icônes **SVG** magnifiquement conçues et scalables. Ces icônes peuvent être utilisées dans n'importe quel projet sans compromettre la vitesse de chargement de la page ou la qualité de résolution. Il suffit de prendre les icônes et de les utiliser où vous en avez besoin, des boutons aux menus de navigation.

## Intégration de Tailwind CSS et compatibilité des frameworks

**ZenUI** est construit avec **Tailwind CSS**, un framework CSS utilitaire qui vous permet de personnaliser vos designs avec un minimum de code. En tirant parti des classes utilitaires de Tailwind, vous pouvez facilement ajuster l'apparence de n'importe quel composant sans avoir besoin d'écrire du CSS personnalisé.

### Compatibilité

ZenUI est conçu pour être polyvalent et compatible avec divers frameworks, ce qui le rend facile à intégrer dans vos projets. Vous pouvez utiliser ZenUI de manière transparente avec :

* **React** : Parfait pour construire des interfaces utilisateur interactives et gérer l'état de manière efficace.
    
* **Next.js** : Idéal pour les applications rendues côté serveur et la génération de sites statiques.
    

Avec ZenUI, vous pouvez créer des applications web visuellement époustouflantes et réactives rapidement et efficacement, quel que soit votre stack technique.

## Comment commencer à utiliser ZenUI

L'un des principaux avantages de ZenUI est que vous n'avez pas besoin d'installer quoi que ce soit pour commencer à l'utiliser. ZenUI fournit toute la structure **HTML** nécessaire et les classes **Tailwind CSS** directement dans sa documentation, vous permettant de copier et coller le code dans vos projets sans aucune configuration supplémentaire.

Si vous travaillez avec des frameworks comme **React** ou **Next.js**, tout ce dont vous avez besoin est un projet qui a intégré Tailwind CSS. Vous pouvez simplement copier le code du composant ou du bloc et le coller directement dans votre JSX, et vous êtes prêt à partir. Il n'est pas nécessaire d'installer des dépendances ou des packages externes.

ZenUI facilite le démarrage de votre projet sans aucune friction—il suffit de démarrer un projet avec React ou Next.js, d'intégrer Tailwind CSS, et de commencer à construire avec les composants et blocs préconstruits de ZenUI.

Voici un guide étape par étape sur la façon de commencer à utiliser la bibliothèque ZenUI :

### 1. Visitez le site web de la bibliothèque ZenUI

Rendez-vous sur le [site web de la bibliothèque ZenUI](https://zenuilibrary.com) où vous pouvez parcourir une large variété de composants UI, de modèles, de blocs essentiels et d'icônes SVG. La bibliothèque ZenUI offre tout, des simples boutons aux mises en page plus complexes.

### 2. Parcourez et sélectionnez un composant

Une fois sur le site web, explorez les différentes sections pour les composants comme :

* Boutons
    
* Formulaires
    
* Modales
    
* Barres de navigation
    
* Cartes
    
* Alertes, et plus encore.
    

Chaque composant est présenté avec un aperçu en direct, ce qui facilite la recherche de ce dont vous avez besoin pour votre projet.

### 3. Copiez le code du composant

Chaque composant listé dans la bibliothèque ZenUI a une section de code associée.

**Vous n'avez pas besoin d'installer de dépendances**—il suffit de **copier le code JSX** pour le composant sélectionné.

### 4. Intégrez le code dans votre projet

Après avoir sélectionné un composant sur le site web de la bibliothèque ZenUI et copié le code, son intégration dans votre projet est incroyablement simple :

**Collez le code** :

* **Projet React ou Next.js** : Ouvrez votre fichier de composant souhaité (par exemple, `App.js` ou tout autre fichier de composant) et **collez** le code copié directement dans le fichier où vous souhaitez le coller.
    
* **Projet Tailwind CSS** : Si vous utilisez du HTML simple avec Tailwind CSS, collez simplement le code HTML de la bibliothèque ZenUI dans votre fichier HTML.
    

**Terminé !** Vous êtes prêt. Vous pouvez maintenant voir le composant dans votre projet sans avoir besoin d'installer de dépendances ou de packages supplémentaires.

Les composants de la bibliothèque ZenUI sont conçus pour fonctionner directement, donc après avoir collé le code, vous verrez immédiatement le composant fonctionner dans votre projet.

### 5. **Personnalisez les composants**

Tous les composants et modèles de la bibliothèque ZenUI sont **hautement personnalisables**. Vous pouvez changer les couleurs, les tailles et les mises en page en utilisant Tailwind ou modifier la structure HTML pour répondre à vos besoins uniques. Que vous construisiez un thème clair ou sombre, ZenUI offre une flexibilité complète.

Je vais vous guider à travers la personnalisation d'un composant de carte étape par étape ci-dessous.

### 6. **Commencez à construire avec les composants ZenUI**

Maintenant que les composants sont intégrés, vous pouvez vous concentrer sur la construction du reste de votre application. Les composants ZenUI préconstruits, réactifs et réutilisables accéléreront votre processus de développement sans sacrifier la qualité du design.

En suivant ces étapes, vous pouvez commencer à utiliser la bibliothèque ZenUI immédiatement dans votre projet. Que vous construisiez avec React, Next.js ou du HTML simple avec Tailwind CSS, la bibliothèque ZenUI offre une solution simple et efficace pour le développement d'interfaces utilisateur sans le tracas de la gestion de dépendances supplémentaires.

## Comment personnaliser les composants ZenUI

Voici une analyse détaillée de la façon dont vous pouvez personnaliser un **composant de carte** dans la bibliothèque ZenUI en utilisant Tailwind CSS. Cela couvrira le changement de couleurs, l'ajustement des tailles et la modification de la mise en page pour correspondre à l'apparence et à la convivialité de votre projet.

### **Composant de carte original**

Voici un composant de carte de base utilisant Tailwind CSS :

```xml
<div class="bg-white shadow-lg rounded-lg p-6">
  <img src="image.jpg" alt="Image" class="w-full h-48 object-cover rounded-t-lg">
  <h2 class="text-xl font-bold mt-4">Titre de la carte</h2>
  <p class="text-gray-600 mt-2">Ceci est un composant de carte personnalisable.</p>
  <button class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">En savoir plus</button>
</div>
```

### **1. Personnalisez les couleurs**

Vous pouvez facilement changer les couleurs de fond, les couleurs de texte et les couleurs de bouton en modifiant les classes Tailwind.

#### **Changer les couleurs de fond et de texte pour le mode sombre**

Pour rendre la carte compatible avec le mode sombre, vous voudrez ajuster les couleurs de fond et de texte. Voici le code que vous pouvez utiliser pour cela :

```xml
<div class="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6">
  <img src="image.jpg" alt="Image" class="w-full h-48 object-cover rounded-t-lg">
  <h2 class="text-xl font-bold mt-4 text-gray-900 dark:text-white">Titre de la carte</h2>
  <p class="text-gray-600 dark:text-gray-400 mt-2">Ceci est un composant de carte personnalisable.</p>
  <button class="mt-4 bg-blue-500 dark:bg-yellow-500 text-white dark:text-gray-900 px-4 py-2 rounded">En savoir plus</button>
</div>
```

**Analyse du code :**

* `dark:bg-gray-800` : Change la couleur de fond en gris foncé lorsque le mode sombre est actif.
    
* `dark:text-white` : Définit la couleur du texte en blanc en mode sombre pour le titre.
    
* `dark:text-gray-400` : Éclaircit le texte du paragraphe en mode sombre pour une meilleure lisibilité.
    
* `dark:bg-yellow-500` : Change le fond du bouton en jaune en mode sombre.
    
* `dark:text-gray-900` : Change la couleur du texte du bouton en gris foncé en mode sombre.
    

### **2. Configurez** `tailwind.config.js` **pour activer le mode sombre**

Pour activer le **mode sombre** dans votre projet Tailwind CSS, vous devez configurer deux choses principales :

1. **Configurer le fichier** `tailwind.config.js` pour activer le mode sombre.
    
2. **Ajuster votre HTML pour basculer le mode sombre.**
    

Parcourons le processus étape par étape.

Dans le fichier `tailwind.config.js`, ajoutez l'option `darkMode`. Tailwind CSS prend en charge deux stratégies pour le mode sombre :

* `'media'` : Utilise la préférence système de l'utilisateur (mode clair ou sombre).
    
* `'class'` : Utilise une classe `dark` que vous pouvez basculer manuellement (vous donne plus de contrôle).
    

**Exemple de configuration utilisant la stratégie** `'class'` :

```javascript
module.exports = {
  darkMode: 'class', // Active le mode sombre basé sur les classes
  // Autres configurations...
  theme: {
    extend: {
      // Personnalisations...
    },
  },
  variants: {
    extend: {
      // Variantes...
    },
  },
  plugins: [],
};
```

#### **Configurez votre HTML pour basculer le mode sombre**

1. **Pour le mode sombre basé sur les classes (**`darkMode: 'class'`): Pour contrôler manuellement le mode sombre, vous devez ajouter ou supprimer la classe `dark` sur votre élément racine HTML.
    

**Ajoutez la classe** `dark` pour activer le mode sombre :

```xml
<html class="dark">
  <head>
    <!-- Contenu de l'en-tête -->
  </head>
  <body>
    <!-- Votre contenu -->
  </body>
</html>
```

2. **Basculer le mode sombre avec JavaScript** : Vous pouvez également ajouter un bouton pour basculer dynamiquement le mode sombre :
    

```xml
<button onclick="toggleDarkMode()">Basculer le mode sombre</button>

<script>
  function toggleDarkMode() {
    document.documentElement.classList.toggle('dark');
  }
</script>
```

**Résumé**

* **Étape 1** : Dans votre fichier `tailwind.config.js`, définissez `darkMode` sur `'class'` ou `'media'`.
    
    * Utilisez `'class'` si vous souhaitez basculer manuellement le mode sombre.
        
    * Utilisez `'media'` pour suivre automatiquement la préférence système de l'utilisateur.
        
* **Étape 2** : Si vous utilisez le mode `'class'`, ajoutez ou supprimez la classe `dark` sur votre balise `<html>` ou `<body>` pour activer ou désactiver le mode sombre.
    
* **Étape 3** : Dans votre HTML, utilisez le préfixe `dark:` dans les classes Tailwind CSS pour spécifier les styles pour le mode sombre.
    

### **3. Personnalisez les tailles et les espacements**

Vous pouvez modifier la taille de la carte et ajuster les rembourrages et les marges pour mieux adapter votre mise en page.

#### **Carte plus grande avec plus de rembourrage**

Si vous voulez une carte plus grande avec plus de rembourrage et une image plus grande :

```xml
<div class="bg-white shadow-lg rounded-lg p-10">
  <img src="image.jpg" alt="Image" class="w-full h-64 object-cover rounded-t-lg">
  <h2 class="text-xl font-bold mt-8">Titre de la carte</h2>
  <p class="text-gray-600 mt-4">Ceci est un composant de carte personnalisable.</p>
  <button class="mt-8 bg-blue-500 text-white px-6 py-3 rounded-lg">En savoir plus</button>
</div>
```

**Analyse du code :**

* `p-10` augmente le rembourrage à l'intérieur de la carte pour une mise en page plus spacieuse.
    
* `h-64` change la hauteur de l'image à 64 unités (16rem), la rendant plus haute.
    
* `mt-8` ajoute plus d'espace entre les éléments, comme le titre et le bouton.
    
* `px-6 py-3` augmente le rembourrage à l'intérieur du bouton, le rendant plus grand.
    
* `rounded-lg` ajoute des coins arrondis plus grands et plus proéminents au bouton.
    

### **4. Modifiez la mise en page**

Vous pouvez également ajuster la mise en page de la carte en la rendant plus compacte ou en alignant le contenu différemment.

#### **Carte compacte avec contenu aligné à gauche**

```xml
<div class="bg-white shadow-lg rounded-lg p-4 flex items-start">
  <img src="image.jpg" alt="Image" class="w-24 h-24 object-cover rounded-lg mr-4">
  <div>
    <h2 class="text-xl font-bold">Titre de la carte</h2>
    <p class="text-gray-600 mt-2">Ceci est un composant de carte personnalisable.</p>
    <button class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">En savoir plus</button>
  </div>
</div>
```

**Analyse du code :**

* `flex items-start` fait de la carte une mise en page de boîte flexible avec le contenu aligné en haut.
    
* `w-24 h-24` redimensionne l'image à un format carré plus petit.
    
* `mr-4` ajoute une marge à droite de l'image, la séparant du contenu textuel.
    
* Le reste du contenu (titre, texte et bouton) est contenu dans une `div` pour le garder aligné à côté de l'image.
    

### **5. Personnalisez-le avec un design réactif**

Tailwind facilite la personnalisation de la carte pour différentes tailles d'écran.

#### **Carte réactive pour mobile et bureau**

```xml
<div class="bg-white shadow-lg rounded-lg p-6 md:p-10">
  <img src="image.jpg" alt="Image" class="w-full h-48 md:h-64 object-cover rounded-t-lg">
  <h2 class="text-xl font-bold mt-4 md:mt-8">Titre de la carte</h2>
  <p class="text-gray-600 mt-2 md:mt-4">Ceci est un composant de carte personnalisable.</p>
  <button class="mt-4 md:mt-8 bg-blue-500 text-white px-4 py-2 md:px-6 md:py-3 rounded-lg">En savoir plus</button>
</div>
```

**Analyse du code :**

* `md:p-10` augmente le rembourrage sur les grands écrans (par exemple, tablettes ou ordinateurs de bureau).
    
* `md:h-64` rend l'image plus haute sur les grands écrans, offrant une meilleure expérience visuelle.
    
* `md:mt-8` ajoute plus d'espacement entre les éléments sur les grands écrans pour éviter un aspect encombré.
    
* `md:px-6 md:py-3` agrandit le bouton sur les grands écrans, le rendant plus facile à utiliser.
    

Comme vous venez de le voir, avec Tailwind CSS, vous pouvez personnaliser les composants de la bibliothèque ZenUI de diverses manières :

1. **Couleurs** : Ajustez les couleurs de fond, de texte et de bouton pour les thèmes clair et sombre.
    
2. **Tailles et espacements** : Modifiez les rembourrages, les marges et les dimensions pour adapter votre mise en page.
    
3. **Mise en page** : Utilisez une boîte flexible ou une grille pour modifier la disposition du contenu dans la carte.
    
4. **Design réactif** : Adaptez vos composants à différentes tailles d'écran en utilisant des classes utilitaires réactives.
    

## Comment utiliser les modèles de site web ZenUI

Commencer avec les **modèles de site web ZenUI** est rapide et facile. Je vais maintenant vous guider à travers la configuration de votre projet en utilisant l'un des modèles préconstruits de ZenUI.

### Étape 1 : Choisissez un modèle

Rendez-vous sur le **site web de la bibliothèque ZenUI** et naviguez jusqu'à la section des modèles. Vous y trouverez une variété de modèles de sites web.

* Choisissez un modèle qui correspond aux besoins de votre projet.
    
* Accédez au dépôt GitHub du modèle en cliquant sur le bouton **Obtenir le modèle**.
    

### Étape 2 : Clonez le dépôt sur votre bureau

Lorsque vous accédez au dépôt GitHub en cliquant sur le bouton **Obtenir le modèle**, vous verrez un bouton appelé **Code**. Cliquez dessus et vous verrez une URL HTTPS comme sur l'image ci-dessous. Copiez l'URL.

![cloner-le-modele-zenui-depuis-le-depot-github](https://cdn.hashnode.com/res/hashnode/image/upload/v1727202543195/e1c05f17-b12f-4ab3-9b9d-23cebd948349.png align="center")

Après avoir copié l'URL HTTPS, ouvrez simplement le terminal de votre ordinateur et tapez une commande comme celle ci-dessous :

```bash
git clone url-https-du-projet-ici
```

Après avoir traité la commande avec l'URL HTTPS correcte, vous obtiendrez le modèle sur votre ordinateur local. Ouvrez maintenant le projet de modèle dans l'éditeur de code de votre choix.

Après avoir ouvert le projet dans votre éditeur de code, vous devez faire juste 2 choses :

* Installez les packages npm en utilisant la commande `npm install` (les packages seront react-icons, react-router-dom, etc.)
    
* Exécutez le projet sur votre **localhost** en utilisant la commande `npm run dev`
    

### Étape 3 : Personnalisez le modèle

Vous pouvez [regarder cette vidéo](https://youtu.be/wPopdyqpxHQ?si=p-12ygf5LiXCLAQ7) sur la façon d'utiliser le modèle de la bibliothèque ZenUI et comment le personnaliser. Ou vous pouvez explorer :

* **Modification du contenu** : Changez le texte, les images ou les liens dans le fichier HTML.
    
* **Changement des couleurs** : Mettez à jour les classes utilitaires Tailwind CSS (par exemple, `bg-blue-500` en `bg-red-500`) pour appliquer votre marque personnalisée.
    
* **Ajout de nouveaux composants** : Copiez et collez des composants ou blocs supplémentaires de la documentation de la **bibliothèque ZenUI** et intégrez-les dans le modèle.
    

## Comment extraire les couleurs d'une image

Tout d'abord, allez sur le site web de la [bibliothèque ZenUI](https://zenui.net). Ensuite, cliquez sur le bouton Palette d'opacité dans la barre de navigation supérieure. Vous verrez certaines des palettes générées par défaut par ZenUI. Cliquez simplement sur le bouton d'icône d'image dans la barre de recherche d'icônes sur le côté droit, comme vous pouvez le voir dans l'image ci-dessous :

![televerser-image](https://cdn.hashnode.com/res/hashnode/image/upload/v1727273411733/738020d4-bdbe-4a8e-98ce-63aa21576a7b.png align="center")

Ensuite, vous devez sélectionner votre image depuis votre appareil. Après avoir sélectionné l'image, appuyez sur le bouton ouvrir comme dans l'image ci-dessous :

![selectionner-image-depuis-appareil](https://cdn.hashnode.com/res/hashnode/image/upload/v1727273571064/e90f47f7-dab9-458c-a26d-c6b20ba4199f.png align="center")

Maintenant, vous verrez un outil magique appelé « **Extraire les couleurs de l'image téléversée** » comme dans l'image ci-dessous :

![modale-selecteur-de-couleur-zenui](https://cdn.hashnode.com/res/hashnode/image/upload/v1727273665557/5faad30a-c3fc-4783-b59c-f6999b22d927.png align="center")

Maintenant, il est temps de sélectionner votre couleur dans l'image. Lorsque vous déplacez le curseur sur l'image, vous verrez un indicateur qui vous permet de voir la couleur sur laquelle vous survolez actuellement, comme vous pouvez le voir dans l'image ci-dessous :

![indicateur-en-temps-reel-du-selecteur-de-couleur](https://cdn.hashnode.com/res/hashnode/image/upload/v1727273940270/147b94a5-b95d-47b8-bb5e-437d0276c8a1.jpeg align="center")

En dessous, vous verrez votre couleur sélectionnée dans la section « **Couleur sélectionnée** ». À partir de là, vous pouvez copier le code couleur **Hex** ou **RGB** de votre couleur sélectionnée. Vous pouvez également générer la palette de couleurs sélectionnée en cliquant sur le bouton « **Générer la palette** ».

Vous pouvez également générer une palette de couleurs en fournissant le code couleur. Si vous avez un code couleur et que vous souhaitez créer la palette de couleurs, collez simplement le code couleur dans le champ de référence d'entrée, comme vous pouvez le voir dans l'image ci-dessous :

![entree-du-generateur-de-palette-de-couleurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1727274330786/019228a2-aae8-41e3-bb69-c2fe8a68f4d5.png align="center")

Après avoir collé votre code couleur, cliquez simplement sur le bouton « Générer » et la palette de couleurs sera générée automatiquement.

Après avoir généré la palette de couleurs, vous pouvez copier le code couleur de la palette générée pour n'importe quelle partie—il suffit de cliquer sur la partie de la palette. Pour cela, vous devez copier le code couleur. Vous verrez une modale apparaître avec votre variante de code couleur comme « HEX », « RGB » ou « HSL » comme dans l'image ci-dessous :

![copier-le-code-couleur](https://cdn.hashnode.com/res/hashnode/image/upload/v1727274619884/871ad483-a3f8-4d8e-9b9e-76ac7cbd0ee5.png align="center")

## Comment personnaliser n'importe quelle icône dans la bibliothèque ZenUI

Allez sur le site web de la [bibliothèque ZenUI](https://zenui.net), et cliquez sur le bouton des icônes dans la barre de navigation supérieure. Cela vous amènera à la page d'accueil des icônes ZenUI. Maintenant, choisissez une icône que vous souhaitez utiliser et cliquez dessus. Vous verrez un tiroir apparaître comme dans l'image ci-dessous :

![personnaliser-icone-zenui](https://cdn.hashnode.com/res/hashnode/image/upload/v1727274886810/a283107e-aa84-4537-b7f8-7e866b163422.png align="center")

Maintenant, vous pouvez changer la **couleur** et la **taille** de l'icône. Après l'avoir personnalisée, vous pouvez enregistrer l'icône dans plusieurs formats comme PNG ou SVG, ou copier le code SVG de l'icône.

## Rejoignez la communauté ZenUI

ZenUI ne se limite pas à des composants librement disponibles. Il s'agit également de favoriser une communauté de développeurs et de designers. Rejoignez la [**communauté ZenUI**](https://web.facebook.com/share/g/wAbkC1XFB5Ssc121/) pour partager votre travail, apprendre des autres développeurs et obtenir un accès anticipé aux nouveaux composants et modèles.

Vous pouvez contribuer à ZenUI en soumettant des modèles, en signalant des bugs ou en suggérant des fonctionnalités. Vous pouvez trouver la communauté sur des plateformes comme [GitHub](https://github.com/Asfak00/zenui-library) et [**Facebook**](https://web.facebook.com/zenuilibrary).

## Conclusion

Que vous construisiez un portfolio personnel, un site e-commerce ou une plateforme d'entreprise, ZenUI peut être votre ressource de référence pour des composants et modèles UI de haute qualité et personnalisables. Avec sa simplicité, sa flexibilité et sa large gamme d'options, ZenUI rend le développement front-end facile.

N'hésitez pas à explorer la bibliothèque à l'adresse [https://zenui.net](https://zenui.net), et n'hésitez pas à demander de l'aide ou à donner votre avis.

**Bon codage !**