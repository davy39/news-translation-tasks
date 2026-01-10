---
title: Comment utiliser les outils de développement React – Expliqué avec des exemples
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-05-06T20:12:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-devtools
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/React-Devtools.png
tags:
- name: devtools
  slug: devtools
- name: React
  slug: react
seo_title: Comment utiliser les outils de développement React – Expliqué avec des
  exemples
seo_desc: 'Traditional browser developer tools are designed to inspect and debug web
  pages by interacting with your HTML, CSS, and JavaScript code. However, you can''t
  use them to inspect and debug React applications efficiently due to the nature of
  React.

  This ...'
---

Les outils de développement traditionnels des navigateurs sont conçus pour inspecter et déboguer les pages web en interagissant avec votre code HTML, CSS et JavaScript. Cependant, vous ne pouvez pas les utiliser pour inspecter et déboguer efficacement les applications React en raison de la nature de React.

C'est là que les outils de développement React, également connus sous le nom de React DevTools, entrent en jeu. Ils vous permettent d'inspecter et de déboguer vos applications React en fournissant un accès aux composants, aux états, aux hooks, aux props, à ce qui est rendu et plus encore.

Cet article vous montrera comment utiliser React DevTools en vous concentrant sur l'inspection des composants, des props et des états. Nous examinerons également comment l'utiliser pour améliorer les performances de l'application.

Pour la démonstration, nous utiliserons le code du jeu 2048. Vous pouvez le récupérer dans [ce dépôt GitHub](https://github.com/mateuszsokola/2048-in-react).

## Comment installer les outils de développement React

L'installation de l'extension des outils de développement React pour votre navigateur est la méthode la plus courante pour l'utiliser.

Si vous utilisez Chrome, visitez le Chrome Webstore et recherchez "React", puis sélectionnez "React Developer Tools" et cliquez sur le bouton "_Ajouter à Chrome_" pour l'installer.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2044-05-06-at-11.14.42.png)
_React Devtools dans le Chrome Web Store_

React DevTools est également disponible en tant qu'application electron autonome, un package NPM et une extension pour les navigateurs Edge et Firefox. Si vous utilisez le navigateur Safari, envisagez d'utiliser le package NPM.

Si vous utilisez l'extension sur Chrome mais souhaitez migrer vos données vers Edge ou Firefox, elle sera automatiquement installée pour vous !

## Comment naviguer dans l'interface des outils de développement React

Après avoir installé DevTools en tant qu'extension, ouvrez la console de votre navigateur et vous devriez voir deux onglets supplémentaires – Composants et Profiler.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-25.png)
_Google Chrome avec l'extension React DevTools_

L'onglet Composants affiche une vue arborescente des composants de votre application. Il vous donne également accès aux hooks et aux props de chaque composant.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-11.22.31.png)
_Onglet Composants dans React DevTools_

L'onglet Profiler vous permet d'analyser les performances d'exécution de vos applications et d'identifier les re-rendus coûteux ou les goulots d'étranglement de performance. À partir de là, vous pouvez importer et exporter des sections de performance enregistrées et voir combien de temps un composant met à se rendre ou pourquoi il se re-rend.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-11.23.32.png)
_Onglet Profiler dans React DevTools_

Si vous cliquez sur l'icône d'engrenage sur le côté droit dans l'un des onglets, vous devriez voir une fenêtre contextuelle avec 4 onglets – Général, Débogage, Composants et Profiler.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-11.24.24.png)
_Paramètres de React DevTools_

Dans les 4 onglets, vous pouvez ajuster les paramètres liés au thème, à l'affichage, aux options de débogage, aux filtres de composants et aux paramètres d'enregistrement pour le profiler.

## Comment inspecter les composants React avec DevTools

Dans l'onglet Composants, vous pouvez sélectionner un composant et l'inspecter, tout comme vous le feriez avec des éléments HTML dans les outils de développement traditionnels d'un navigateur.

Pour ce faire, cliquez sur l'icône de sélection en haut à gauche, puis sélectionnez n'importe quelle partie de l'application pour voir le composant qui la représente :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/devtools-1--1-.gif)
_Inspection des composants dans React DevTools_

Au fur et à mesure que vous apportez des modifications impliquant l'ajout de quelque chose, de nouveaux composants seront ajoutés à l'arborescence.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/devtools-2.gif)
_Mises à jour des composants en temps réel dans React DevTools_

Sur le côté droit dans l'onglet Composants se trouvent les `props`, `hooks`, `renderer` et la `source` pour tout composant que vous sélectionnez dans l'arborescence.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-26.png)
_Détails des composants dans React DevTools_

## Comment explorer l'état et les props des composants

Rappelez-vous que lorsque vous sélectionnez un composant dans l'arborescence, l'état et les props de ce composant sont disponibles sur le côté droit.

Dans la capture d'écran ci-dessous, j'ai sélectionné un composant `Tile` pour que vous puissiez voir les props :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-27.png)
_Composant Tile sélectionné_

Vous pouvez voir que le composant `Tile` a des propriétés `id`, `position` et `value`. À partir de là, vous pouvez ajouter une nouvelle prop et modifier les props existantes.

Par exemple, je viens de changer une prop `value` de `2` à `4` et cela s'est reflété dans l'UI en temps réel :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/devtools-3.gif)
_changer la valeur de 2 à 4_

Vous pouvez également apporter des modifications à un état. Par exemple, le tableau de scores que vous pouvez voir dans l'UI est un état dans le contexte `GameProvider`. Il met à jour votre score au fur et à mesure que vous jouez au jeu.

Vous pouvez sélectionner le contexte `GameProvider`, rechercher l'état `score` et le changer en autre chose :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/devtools-4.gif)
_Changer l'état du score_

## Comment déboguer les applications React avec React DevTools

Les outils de développement traditionnels des navigateurs sont bons pour déboguer votre code HTML, CSS et JavaScript, mais ils ont des limitations concernant le débogage des applications React.

C'est la raison principale pour laquelle React DevTools a été créé en premier lieu, car il possède les fonctionnalités intégrées essentielles qui peuvent vous montrer tout ce dont vous avez besoin pour déboguer vos applications React.

L'une des erreurs que le navigateur peut vous aider à déboguer est une erreur de référence. Par exemple, s'il y a une erreur dans l'un de vos composants, le navigateur peut vous montrer le message d'erreur et la ligne affectée.

Par exemple, j'ai forcé une erreur en changeant `cells` en `cell` à la ligne 62 dans le fichier **board.tsx** de l'application. Voici à quoi ressemble le message d'erreur dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-12.08.50.png)
_Erreur de référence dans React 19_

Vous pouvez ensuite aller à la ligne de code où l'erreur s'est produite et faire les ajustements nécessaires pour que l'application puisse fonctionner à nouveau.

React DevTools vous montre également une erreur de référence et le composant dans lequel elle se produit.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-12.11.19.png)
_Erreur de référence dans React DevTools_

## Comment React DevTools porte le débogage au niveau supérieur

Dans l'onglet Composants, au-dessus des éléments sur le côté droit, se trouvent des boutons iconisés que vous pouvez utiliser pour :

* Forcer le composant sélectionné à un état d'erreur
* Inspecter l'élément DOM correspondant
* Suspendre le composant sélectionné
* Journaliser les données du composant dans la console
* Voir le code source des éléments dans le composant sélectionné

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-28.png)
_Utilitaires de composants dans React DevTools_

Par exemple, si les tuiles du jeu ne s'affichent pas comme elles le devraient, il s'agit probablement d'un problème de style.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-12.16.43.png)
_Tuiles non stylisées dans le jeu 2048_

Cette erreur particulière n'empêchera pas votre application de fonctionner, donc la meilleure façon de la déboguer est d'utiliser React DevTools au lieu de parcourir votre code, surtout s'il est volumineux.

Vous pouvez sélectionner le composant `Tile` et journaliser ses données dans la console. Lorsque vous faites cela, les `props`, `hooks` et `nodes` de ce composant seront journalisés pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-29.png)
_Utilitaire permettant de journaliser les données du composant dans la console dans React DevTools_

Pour voir les données du composant, vous devez passer à l'onglet console et inspecter les `nodes` pour voir ce qui a pu mal se passer.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-12.21.11.png)
_Données du composant imprimées dans la console React DevTools_

Dans l'image ci-dessus, il est indiqué qu'il y a un élément `div` avec un `className` indéfini. Cela vous indique que vous avez mal orthographié une valeur `className`, vous devez donc revenir à votre code et la corriger.

Si l'erreur que vous obtenez concerne les `props` ou les `hooks`, vous devez alors ouvrir l'un d'eux pour voir ce qui n'a pas fonctionné.

Vous pouvez également parcourir le code source de tout composant posant problème. Par exemple, si le tableau de scores ne s'affiche pas comme il le devrait, sélectionnez le composant et cliquez sur l'icône "Voir le code source de cet élément".

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-30.png)
_Utilitaire Voir la source de ce composant dans React DevTools_

Une fois le code source affiché, vous pouvez parcourir la fin de chaque ligne. Toute fin de ligne qui est rouge lorsque vous faites cela est celle qui cause l'erreur.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/devtools-5.gif)

Vous pouvez ensuite revenir à votre éditeur et apporter les modifications nécessaires sur cette ligne.

## Analyse des performances avec React DevTools

Faire une analyse des performances avec React peut vous aider à comprendre l'efficacité de votre application et à identifier les goulots d'étranglement de performance. C'est ce que l'onglet Profiler vous permet de faire.

Pour ce faire, passez à l'onglet Profiler et cliquez sur l'icône "Démarrer le profilage" pour commencer l'enregistrement.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-31.png)
_Bouton d'enregistrement dans l'onglet Profiler de React DevTools_

Effectuez les actions dans votre application que vous souhaitez analyser. Cela peut être des chargements de page, des interactions utilisateur comme des clics de bouton, des balayages ou le chargement de contenu dynamique. Lorsque vous avez terminé, cliquez sur "Stop" pour terminer l'enregistrement.

Le Profiler affichera alors un graphe de flamme et une liste de commits. Chaque commit représente une phase de rendu de votre application React. Les composants qui prennent plus de temps à se rendre auront des barres plus larges.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/devtools-6.gif)

Vous pouvez ensuite sélectionner un commit spécifique pour voir des informations détaillées sur les performances de rendu des composants pendant ce commit :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-06-at-12.28.57-1.png)
_Résultats du profilage dans React DevTools_

Vous pouvez également télécharger la session de profilage ou importer une session de profilage. Cela signifie que vous pouvez partager la session avec vos coéquipiers.

## Problème courant et solution : Comment corriger React DevTools qui ne s'affiche pas

Si DevTools ne s'affiche pas, cela peut être dû au fait qu'il n'a pas accès aux sites React que vous consultez dans le navigateur.

Pour corriger cela, tapez `chrome://extensions/` dans la barre d'adresse et appuyez sur Entrée, puis recherchez l'extension et assurez-vous qu'elle est activée.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-32.png)
_Comment activer l'extension React DevTools dans Google Chrome_

Si cela ne corrige pas le problème, cliquez sur le bouton "Détails" et assurez-vous d'accorder un accès "Sur tous les sites" sous l'option "Accès au site".

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Group-33.png)
_Comment changer les paramètres d'accès au site de l'extension dans Google Chrome_

## Conclusion

De l'inspection de la hiérarchie des composants et de la modification de l'état et des props à l'analyse des performances et à la compréhension des re-rendus complexes, les outils de développement React offrent un ensemble complet de fonctionnalités qui peuvent améliorer la qualité de vos applications React.

Que vous soyez un débutant cherchant à mieux comprendre le fonctionnement interne de React, ou un développeur expérimenté cherchant à optimiser vos applications, investir du temps pour maîtriser les outils de développement React sera profitable dans vos processus de développement.

## Apprendre React et Next JS

Êtes-vous prêt à plonger profondément dans React et à commencer à créer des applications réelles ? Inscrivez-vous à mon [cours React et Next JS sur Udemy](https://assets.mateu.sh/r/fcc-react-devtools) ! Vous apprendrez par le codage pratique alors que nous construisons un incroyable jeu 2048 à partir de zéro avec des animations cool.

Rejoignez maintenant et commencez votre voyage pour devenir un développeur React employable !

[![Apprendre Next.js et React 19 pour créer le jeu 2048 à partir de zéro](https://assets.mateu.sh/assets/fcc-react-devtools)](https://assets.mateu.sh/r/fcc-react-devtools)
_Cliquez pour commencer_