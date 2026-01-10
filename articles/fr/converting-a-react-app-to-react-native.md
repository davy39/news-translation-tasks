---
title: Comment convertir une application React en React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-04T20:36:00.000Z'
originalURL: https://freecodecamp.org/news/converting-a-react-app-to-react-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb77f740569d1a4cae4f4.jpg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Comment convertir une application React en React Native
seo_desc: 'By Gwendolyn Faraday

  I have been working on a lot of mobile projects lately — including Cordova, PhoneGap,
  React Native, some Ionic and Swift — but I have to say, React Native is by far the
  best experience in mobile development I have had so far. It ...'
---

Par Gwendolyn Faraday

J'ai travaillé sur de nombreux projets mobiles récemment — incluant Cordova, PhoneGap, React Native, un peu d'Ionic et Swift — mais je dois dire que React Native est de loin la meilleure expérience en développement mobile que j'ai eue jusqu'à présent. Il offre de excellents outils de développement similaires à ceux du web, me permet d'utiliser des packages NPM ainsi que de nombreux packages react-native, et produit également des applications plus rapides et plus fluides que Cordova ou Ionic. Il partage le même flux de travail qu'une application React pour le web, ce qui est assez facile à comprendre et permet de trouver rapidement où se trouvent les choses.

Actuellement, je développe une application pour gamifier le recyclage dans l'Indiana. J'ai une application web terminée en version alpha, cependant, l'application nécessite l'utilisation de la géolocalisation, de la réalité augmentée et d'autres fonctionnalités, donc je développe une application mobile pour compléter celle du web. Comme l'application web est en React, j'ai pensé qu'il serait plus facile de construire la version Native pour iOS et Android en même temps en utilisant React Native.

Voici quelques maquettes pour vous donner une idée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wueFtT0VpHQ3uxJm5sqWQg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dSFJs29dTU8RiLBcpwUhAg.png)
_(J'ai changé le menu du côté droit vers le côté gauche après cela)_

### Installation de l'application React Native

Là où React Native surpasse React, c'est dans sa configuration simple pour les applications. Une seule commande crée un dossier avec toute votre configuration Xcode et Android ainsi qu'une application de démarrage prête pour l'émulateur.

[Lien vers les instructions de configuration simple](https://facebook.github.io/react-native/docs/getting-started.html).

Après l'avoir fait fonctionner dans le simulateur, je crée un répertoire 'src' pour y mettre tout mon code. Ensuite, j'active le rechargement en direct (commande + D ouvre le menu de développement sur iOS et contrôle + D sur Android) et je commence à développer !

![Image](https://cdn-media-1.freecodecamp.org/images/1*uakeeXPDb09NCgpr3uK3yQ.png)

Une rapide note sur les applications de style React : Si vous êtes nouveau dans ce domaine, cela peut sembler un peu étrange de retourner votre vue depuis vos fichiers `.js`.

React, dans sa forme la plus simple, est un moyen d'écrire du code modulaire et réutilisable. Chaque composant est divisé en sous-composants là où cela a du sens. Chaque composant est encapsulé en tant que fonction ou classe dans son propre fichier, ce qui signifie que vous n'importez que ce dont vous avez besoin. La fonction retourne ensuite sa vue — le contenu à afficher à l'écran depuis le composant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZF5Pc5eg9KYQP-Cpo6IkyQ.png)

### Menu et Navigation

J'ai un menu sur le web, mais je dois changer l'emplacement pour le mobile. Je voulais que l'utilisateur puisse balayer ou cliquer pour ouvrir le menu. Il existe un nombre surprenant de bibliothèques React Native pour couvrir la plupart des besoins mobiles.

[react-native-side-menu](https://github.com/react-native-community/react-native-side-menu) est une petite bibliothèque géniale qui était assez facile à configurer. J'ai testé le balayage pour m'assurer qu'il était fluide, puis j'ai ajouté des liens au menu latéral.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CrUTBi4wdMstsOh5kZ005Q.png)

RN ne vient pas avec une solution de navigation intégrée, donc j'ai ajouté [react-native-router-flux](https://github.com/aksonov/react-native-router-flux). Cela fonctionne très bien, même si vous n'utilisez pas un système de gestion d'état flux traditionnel (flux était similaire en concept à Redux) et c'est facile à configurer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rIFVcz6EFmanByClF4Ix7Q.png)
_router.js_

Une `Scene` est une 'vue' ou une 'page' dans l'application (vous pouvez voir comment la navigation fonctionne ensemble dans le court clip vidéo à la fin). L'attribut `title` s'affiche dans l'en-tête en haut, la `key` est utilisée pour naviguer vers la page spécifique, et le `component` est le fichier Javascript réel qui contient le composant React Native à afficher sur cette page. Donc, j'ai créé un composant pour chaque page avec un contenu de remplissage :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gTBtDUUcGA9s9cAXuQNWzQ.png)

Maintenant, il y a un menu et des pages de base factices et l'utilisateur a la possibilité de naviguer dans l'application. C'était assez rapide et facile — j'ai juste installé quelques modules et écrit une quantité minimale de code.

### Listes

La plupart des composants que j'ai créés, j'ai pu les copier depuis mon application web et simplement mettre à jour l'UI.

Pour cette application, j'ai un tableau en constante croissance de divers personnages que je voulais afficher dans une liste déroulante sur mobile. React Native offre ScrollView et ListView comme solutions intégrées pour gérer le défilement infini.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DdyYRy8j07M53H_DM-se3w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mi5OiCEeLYFAb4r3Hc8gqA.png)

Chacun des animaux ci-dessus peut être cliqué et vu sur une page individuelle :

![Image](https://cdn-media-1.freecodecamp.org/images/1*P7ROW-uP6fqCH4DSvkkWmw.png)

J'ai défini la page 'Amici Info' comme une scène dans le routeur et je la remplis avec les informations de la créature sur laquelle on a cliqué.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xi5wNcI6RBCc7zICrAE8hg.png)

### Composants réutilisables

Je peux également créer des enveloppes autour des composants avec des styles et des fonctionnalités de base des solutions mobiles courantes. Par exemple, des cartes, je peux mettre à jour les couleurs et le remplissage légèrement pour chaque projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2DvVIaSBmtTHtC-Q2N4Ezg.png)

### Portage de Redux

Heureusement, la plupart de mes appels Redux et API sont les mêmes. L'application n'a pas besoin de autant de données que le site web, donc j'ai pu supprimer quelques fonctions.

La seule chose que je fais pour l'instant est de récupérer les objets de personnages depuis DynamoDB (AWS).

![Image](https://cdn-media-1.freecodecamp.org/images/1*njqrI7O6EUIB1KfstjuDKw.png)

Voici le réducteur pour correspondre à cette action :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SztYfpquPHgEVr5C4ntIQg.png)

C'est essentiellement l'état de Redux pour l'instant. J'ai encore beaucoup de travail à faire sur la partie Redux mais c'est un bon début. **Prochaine étape :** Je dois configurer un composant de carte et afficher les emplacements pour que les utilisateurs puissent les voir.

### Débogage et outils de développement

L'une des meilleures fonctionnalités de React Native est l'outil de développement. `Command + D` me donne un menu de développement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vlbSKws1cVciibhiK2zXyw.png)

Il suffit d'un clic pour ouvrir les outils de développement Chrome ou utiliser un inspecteur similaire à l'option `inspecter l'élément` lorsque vous cliquez avec le bouton droit dans un navigateur.

### Conclusion

Pour un MVP, je pense que cela avance bien jusqu'à présent.

%[https://youtu.be/44hq-XaqR14]

Je prends vraiment plaisir à travailler avec React Native et je continuerai à l'utiliser chaque fois que possible jusqu'à ce que quelque chose de mieux arrive.

_Si je manque d'informations dans cet article ou si vous avez des questions, faites-le moi savoir_ :)