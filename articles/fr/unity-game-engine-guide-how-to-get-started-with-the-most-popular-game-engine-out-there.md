---
title: 'Guide du moteur de jeu Unity : Comment commencer avec le moteur de jeu le
  plus populaire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-13T18:47:00.000Z'
originalURL: https://freecodecamp.org/news/unity-game-engine-guide-how-to-get-started-with-the-most-popular-game-engine-out-there
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c98740569d1a4ca3316.jpg
tags:
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: toothbrush
  slug: toothbrush
- name: unity
  slug: unity
seo_title: 'Guide du moteur de jeu Unity : Comment commencer avec le moteur de jeu
  le plus populaire'
seo_desc: 'Game Development with Unity

  Unity is a cross-platform game engine developed by Unity Technologies, which is
  primarily used to develop video games and simulations for computers, consoles and
  mobile devices. First announced only for OS X, at Apple’s Wo...'
---

## **Développement de jeux avec Unity**

Unity est un moteur de jeu multiplateforme développé par Unity Technologies, principalement utilisé pour développer des jeux vidéo et des simulations pour ordinateurs, consoles et appareils mobiles. Initialement annoncé uniquement pour OS X, lors de la Worldwide Developers Conference d'Apple en 2005, il a depuis été étendu pour cibler 27 plateformes.

## **Aperçu**

Unity est un moteur de jeu polyvalent qui supporte les graphismes 2D et 3D, la fonctionnalité de glisser-déposer et le scripting via [C#](https://guide.freecodecamp.org/csharp).

Unity est particulièrement populaire pour le développement de jeux mobiles et une grande partie de leur focus est sur les plateformes mobiles. Le pipeline 2D de Unity3D est une addition plus récente au moteur, et est moins mature que le pipeline 3D. Malgré cela, Unity est une plateforme adéquate pour développer des jeux 2D même en comparaison avec d'autres moteurs dédiés 2D, particulièrement si vous prévoyez de sortir le jeu sur plusieurs appareils mobiles.

Unity est également un bon choix pour le développement VR, bien que le marché VR soit encore très petit. Les marchés mobile et PSVR sont les plus grands dans le VR, et Unity est déjà bien positionné pour porter des jeux sur de nombreuses plateformes telles que PS4 et PC, ou de nombreux marchés mobiles différents.

Le moteur cible les API graphiques suivantes : Direct3D sur Windows et Xbox One ; OpenGL sur Linux, macOS et Windows ; OpenGL ES sur Android et iOS ; WebGL sur le web ; et des API propriétaires sur les consoles de jeux vidéo.

De plus, Unity supporte les API de bas niveau Metal sur iOS et macOS et Vulkan sur Android, Linux et Windows, ainsi que Direct3D 12 sur Windows et Xbox One. Dans les jeux 2D, Unity permet l'importation de sprites et un moteur de rendu 2D avancé.

Pour les jeux 3D, Unity permet la spécification des paramètres de compression et de résolution de texture pour chaque plateforme que le moteur de jeu supporte, et fournit un support pour le bump mapping, le reflection mapping, le parallax mapping, l'occlusion ambiante en espace écran (SSAO), les ombres dynamiques utilisant des shadow maps, le rendu vers texture et les effets de post-traitement plein écran.

Unity offre également des services aux développeurs, notamment : Unity Ads, Unity Analytics, Unity Certification, Unity Cloud Build, Unity Everyplay, Unity IAP, Unity Multiplayer, Unity Performance Reporting et Unity Collaborate. En outre, Unity dispose d'une boutique d'assets où la communauté des développeurs peut télécharger et upload des ressources tierces, commerciales et gratuites, telles que des textures, des modèles, des plugins, des extensions d'éditeur et même des exemples complets de jeux.

Unity est remarquable pour sa capacité à cibler des jeux pour plusieurs plateformes. Les plateformes actuellement supportées sont Android, Android TV, Facebook Gameroom, Fire OS, Gear VR, Google Cardboard, Google Daydream, HTC Vive, iOS, Linux, macOS, Microsoft HoloLens, Nintendo 3DS family, Nintendo Switch, Oculus Rift, PlayStation 4, PlayStation Vita, PlayStation VR, Samsung Smart TV, Tizen, tvOS, WebGL, Wii U, Windows, Windows Phone, Windows Store et Xbox One.

Unity est le kit de développement logiciel (SDK) par défaut pour la plateforme de console de jeu vidéo Wii U de Nintendo, avec une copie gratuite incluse par Nintendo avec chaque licence de développeur Wii U. Unity Technologies appelle ce regroupement d'un SDK tiers une "première dans l'industrie".

## **Interface**

![Interface Unity](https://github.com/pawelszpiczakowski/PublicStuff/raw/master/unityInterface.png)

Sur l'image ci-dessus, vous remarquerez cinq sections :

1. Section 1. **Vue de la Scène** : C'est ici que vous créerez le niveau pour votre jeu, scène ou projet 3D. Tous vos Game Objects seront placés et manipulés ici.
2. Section 2. **Vue du Jeu** : C'est ici que vous verrez vos résultats, à quoi ressemble votre niveau ou scène. Vous devez avoir une Caméra sur la scène pour voir à quoi elle ressemble. Parfois, cela s'appelle Vue Caméra.
3. Section 3. **Hiérarchie** : Cette fenêtre affichera tous les Game Objects placés directement sur la scène. Basiquement, tout ce que vous voyez dans la Vue du Jeu doit être listé ici. Cela inclura les objets de jeu visuels et non visuels.
4. Section 4. **Projet** : C'est votre fenêtre de projet. Basiquement, elle montre ce qui se trouve dans le dossier Assets sur votre disque. Tout, des Game Objects, Scripts, Textures, Dossiers, Modèles, Audio, Vidéo, etc., sera accessible depuis cette fenêtre.
5. Section 5. **Inspecteur** : Ce panneau affichera différents attributs et propriétés des Game Objects sélectionnés. Selon la sélection, les attributs et composants appropriés seront listés.

## **Jeux notables :**

* Assassin’s Creed: Identity
* Temple Run Trilogy
* Battlestar Galactica Online
* Hearthstone: Heroes of Warcraft
* Inside
* Cuphead

## **Histoire**

Deux autres langages de programmation étaient supportés : Boo, qui a été déprécié avec la sortie de Unity 5, et UnityScript, qui a été déprécié en août 2017 après la sortie de Unity 2017.1.

Unity supportait autrefois 7 autres plateformes, y compris son propre Unity Web Player.

Unity Web Player était un plugin de navigateur qui était supporté uniquement sur Windows et OS X, et qui a été déprécié au profit de WebGL.

Unity est le moteur utilisé par Rust, Kerbal Space Program et Cup Head.

## Plus d'informations sur Unity :

* [Guide ultime du débutant pour le développement de jeux dans Unity](https://www.freecodecamp.org/news/the-ultimate-beginners-guide-to-game-development-in-unity-f9bfe972c2b5/)
* [Comment créer un jeu 2D dans Unity](https://www.freecodecamp.org/news/how-to-create-a-2d-card-game-in-unity/) (vidéo)
* [Faites un tour de Unity 2D](https://www.freecodecamp.org/news/take-a-tour-of-unity-2d/) (vidéo)
* [Comparaison de Unity et d'autres moteurs de jeu](https://www.freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines/)