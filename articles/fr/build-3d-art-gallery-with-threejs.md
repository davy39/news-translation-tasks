---
title: Créer une Galerie d'Art 3D avec Three.js
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-03-07T16:21:11.000Z'
originalURL: https://freecodecamp.org/news/build-3d-art-gallery-with-threejs
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/art2.png
tags:
- name: three.js
  slug: three-js
- name: youtube
  slug: youtube
seo_title: Créer une Galerie d'Art 3D avec Three.js
seo_desc: '3D web experiences can provide engaging and interactive user interfaces.
  And one of the best JavaScript libraries to create these experiences is Three.js.

  We just posed a comprehensive Three.js course on the freeCodeCamp.org YouTube channel.
  This cou...'
---

Les expériences web 3D peuvent offrir des interfaces utilisateur engageantes et interactives. Et l'une des meilleures bibliothèques JavaScript pour créer ces expériences est Three.js.

Nous venons de publier un cours complet sur Three.js sur la chaîne YouTube freeCodeCamp.org. Ce cours est conçu pour vous guider à travers le processus de création d'une galerie d'art 3D interactive à partir de zéro en utilisant Three.js. Emilian Kasemi a créé ce cours.

## Comprendre Three.js

Three.js est une bibliothèque JavaScript qui permet aux développeurs web de créer des graphiques 3D détaillés et interactifs qui s'exécutent sans problème dans les navigateurs web sans avoir besoin de plugins spécialisés. Ici, nous approfondissons les facettes de Three.js, explorant ses composants principaux, comment il s'interface avec WebGL, et les diverses fonctionnalités qui en font un outil indispensable pour le développement web 3D.

Three.js abstrait la complexité du WebGL brut, offrant un ensemble d'API plus accessibles. Voici quelques-uns des composants principaux avec lesquels vous travaillerez fréquemment dans Three.js :

**Scènes :** Le point de départ de toute application Three.js, une scène agit comme un conteneur où vous placez des objets, des lumières, des caméras et d'autres éléments nécessaires pour votre monde 3D.

**Caméras :** Les caméras sont essentielles pour déterminer comment votre scène est vue. Three.js propose divers types de caméras, comme PerspectiveCamera et OrthographicCamera, chacune offrant une perspective et un cas d'utilisation uniques.

**Renderers :** Le renderer prend la scène et la caméra, les traitant pour afficher votre contenu 3D sur une page web. Le WebGLRenderer, l'un des renderers les plus couramment utilisés dans Three.js, utilise WebGL pour rendre les scènes avec une accélération matérielle.

**Géométrie :** Cela définit la forme des objets que vous créerez. Three.js inclut une pléthore de géométries prédéfinies comme BoxGeometry, SphereGeometry, et plus encore, que vous pouvez utiliser pour créer rapidement des formes standard.

**Matériaux :** Les matériaux définissent l'apparence de vos objets. Qu'il s'agisse de la couleur, de la façon dont il interagit avec la lumière, ou de la texture, les matériaux donnent du caractère et du réalisme à vos objets.

**Textures :** Les textures vous permettent d'ajouter de la complexité et des détails à vos matériaux, donnant aux objets une apparence plus réaliste. Vous pouvez utiliser des images ou des textures générées dynamiquement pour améliorer la qualité visuelle de vos modèles 3D.

**Lumières :** Les lumières ajoutent de la profondeur et du réalisme à vos scènes. Three.js offre divers types de lumières, comme AmbientLight, PointLight, DirectionalLight, etc., chacune contribuant différemment à l'illumination de votre scène.

Au cœur de Three.js se trouve WebGL, un standard web qui permet aux navigateurs de rendre des graphiques 3D interactifs. WebGL est puissant mais complexe, impliquant une courbe d'apprentissage abrupte en raison de sa nature de bas niveau. Three.js fournit une abstraction conviviale, permettant aux développeurs de tirer parti de la puissance de WebGL sans se perdre dans ses complexités. Cette abstraction permet aux développeurs de se concentrer sur les aspects créatifs de la conception 3D, plutôt que sur les détails techniques de la programmation WebGL.

En offrant une interface conviviale, un ensemble robuste de fonctionnalités et une communauté de soutien, Three.js équipe les développeurs des outils dont ils ont besoin pour donner vie à leurs visions 3D sur le web.

## Aperçu du Cours

Ce cours Three.js est conçu pour aider à la fois les débutants et les développeurs expérimentés cherchant à élargir leurs compétences dans le domaine du développement web 3D. Voici ce que vous pouvez vous attendre à apprendre :

### Création de Scène

Le cours commence par les fondamentaux de Three.js, en commençant par la création de scène. Vous apprendrez à configurer les composants essentiels d'une application Three.js, définissant l'espace où vos objets 3D vivront et interagiront.

### Configuration de la Caméra

Comprendre les configurations de caméra est crucial pour définir la perspective à partir de laquelle les utilisateurs verront votre monde 3D. Cette section couvre diverses configurations de caméra, vous aidant à choisir et à implémenter la bonne configuration de caméra pour votre projet.

### Développement du Renderer

Le rendu est le processus de génération d'une image photoréaliste à partir d'un modèle 2D ou 3D. Dans ce cours, vous plongerez dans le développement du renderer, apprenant à afficher avec précision votre scène 3D dans un navigateur web.

### Création de Géométrie, de Matériaux et de Textures

Aucune scène 3D n'est complète sans objets, et c'est là que la géométrie, les matériaux et les textures entrent en jeu. Vous explorerez comment créer des objets 3D complexes, appliquer différents matériaux et ajouter des textures pour améliorer l'attrait visuel de votre scène.

### Maillage

Le maillage est un processus critique dans la modélisation 3D qui implique la création d'un maillage—une collection de sommets, d'arêtes et de faces qui définissent la forme d'un objet 3D. Cette section vous guidera à travers le processus de maillage dans Three.js.

### Animation

Donnez vie à votre scène 3D avec l'animation. Apprenez à ajouter du mouvement aux objets, créant des expériences 3D dynamiques et engageantes pour les utilisateurs.

### Contrôles

L'interaction utilisateur est la clé des expériences 3D immersives. Ce cours couvrira comment implémenter des contrôles, permettant aux utilisateurs d'interagir avec les objets 3D et de naviguer dans la scène.

### Configuration de l'UI en Temps Réel à l'Aide d'un Debugger GUI

Affinez votre scène 3D avec une configuration d'UI en temps réel. Vous aurez une expérience pratique en utilisant un debugger GUI pour ajuster divers aspects de votre scène et de vos objets, garantissant que votre galerie 3D a l'apparence et fonctionne exactement comme vous l'imaginez.

### Ajout de la Prise en Charge de la VR

Le cours se termine par une incursion passionnante dans la réalité virtuelle, vous apprenant à ajouter la prise en charge de la VR à votre galerie d'art 3D. Cela permettra aux utilisateurs disposant de dispositifs VR de s'immerger pleinement dans le monde que vous avez créé.

## Conclusion

Ce cours offre un guide complet, étape par étape, pour maîtriser Three.js. Regardez le cours complet [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/imqiYWidUIA) (8 heures de visionnage).

%[https://youtu.be/imqiYWidUIA]