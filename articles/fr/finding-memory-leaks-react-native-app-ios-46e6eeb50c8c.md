---
title: Détection des fuites de mémoire dans une application React Native (iOS)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-10T07:51:39.000Z'
originalURL: https://freecodecamp.org/news/finding-memory-leaks-react-native-app-ios-46e6eeb50c8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*krH5Jncq4a9wjIikKiHP2A.png
tags:
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Détection des fuites de mémoire dans une application React Native (iOS)
seo_desc: 'By Jignesh Kakadiya

  Problem:Our react-native app was working well on all devices and except iPhone 6
  it was resulting in a crash. After high level profiling we found out that its a
  memory issue. While using some heavy features in the app memory was s...'
---

Par Jignesh Kakadiya

**Problème :**  
Notre application React Native fonctionnait bien sur tous les appareils, sauf sur l'iPhone 6, où elle plantait. Après un profilage de haut niveau, nous avons découvert qu'il s'agissait d'un problème de mémoire. Lors de l'utilisation de certaines fonctionnalités gourmandes dans l'application, la mémoire grimpait jusqu'à 600+ Mo. Et comme l'iPhone 6 a 1 Go de RAM, iOS ferme automatiquement l'application.

**Solution :**  
Voici ce que j'ai fait pour réduire l'utilisation totale de la mémoire de l'application de 600 Mo à 60 Mo.

1. Lors du profilage pour détecter les fuites de mémoire, assurez-vous que l'application est construite avec le schéma de release. Puisque le build de développement inclut le logging/les avertissements et le rechargement à chaud, nous n'en avons pas besoin lors de la vérification des fuites. [Voici comment vous pouvez changer le build de release avec Xcode](https://facebook.github.io/react-native/docs/running-on-device.html#2-configure-release-scheme).
2. **Commencez à suivre les fuites**  
Allez dans Xcode → Product → Profile (⌘ + i)  
Une fenêtre avec les templates de profilage s'ouvrira. Veuillez sélectionner celui qui est nécessaire.  
Sélectionnez `Leaks` et cliquez sur `choose`.

![Image](https://cdn-media-1.freecodecamp.org/images/cDoGQtXWVyDoua8UUIIqNsjlJaLzyE62nXhD)
_Liste des profileurs_

3. Cela devrait ouvrir le profileur de fuites sur votre écran. Ensuite, vous pouvez cliquer sur le `point rouge` en haut à gauche, ce qui **redémarrera l'application dans le simulateur**, et vous pourrez commencer à interagir avec l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/fxTsPg0wyIhD6GNGdWCq020cNQhZTWPp13Ha)

4. Voici à quoi cela ressemble après avoir effectué quelques balayages sur l'écran et des opérations de carrousel. J'ai réalisé que lorsque je passe à l'écran du carrousel et que je sélectionne une image parmi un carrousel de 12 images, la mémoire augmente pour chaque image. Le résultat ci-dessous nous montre la mémoire occupée par les objets image "en mémoire".

![Image](https://cdn-media-1.freecodecamp.org/images/6A-UcrCs6eyxJtaQ0LKLQGSaYGw8hHZgnIeg)

5. **Trouver la cause.**  
Nous utilisions le package [react-native-fast-image](https://github.com/DylanVann/react-native-fast-image) pour mettre en cache les images sur cet écran, et comme React Native n'a pas de "meilleure" façon de mettre en cache les images récupérées, nous avons fini par utiliser `react-native-fast-image`. J'ai donc décidé de supprimer ce package de mon application, et le résultat était choquant. Voici à quoi ressemble le résultat après l'avoir supprimé.

![Image](https://cdn-media-1.freecodecamp.org/images/MaLE0gA8bGNEq95gdnUPP3iOT0kvHWWlQldK)

PS : Pour que vous sachiez, nous avons fini par utiliser [react-native-cached-image](https://github.com/kfiroo/react-native-cached-image), qui ne stocke pas les images en mémoire.

Si vous développez quelque chose avec React Native et avez besoin d'aide, n'hésitez pas à me contacter.