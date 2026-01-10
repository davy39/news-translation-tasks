---
title: Pourquoi vous devriez faire de la Réalité Augmentée si vous êtes un développeur
  JavaScript — et comment commencer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T16:43:29.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-augmented-reality-for-the-javascript-developer-with-an-example-71875ab184ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hIfbsKuXmHPb0qEKvotZ4A.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: tools
  slug: tools
- name: Virtual Reality
  slug: virtual-reality
seo_title: Pourquoi vous devriez faire de la Réalité Augmentée si vous êtes un développeur
  JavaScript — et comment commencer
seo_desc: 'By Evaristo Caraballo

  If you are a JavaScript coder who is still late to making up a definitive list of
  resolutions for 2019, let me give you a hand: Start figuring out how to get into
  Augmented Reality (AR).

  The Augmented/Mixed/Virtual Reality (AR/M...'
---

Par Evaristo Caraballo

Si vous êtes un codeur JavaScript qui n'a pas encore établi une liste définitive de résolutions pour 2019, laissez-moi vous donner un coup de main : commencez à comprendre comment vous lancer dans la Réalité Augmentée (AR).

Le combo Réalité Augmentée/Mixte/Virtuelle (AR/MR/VR) a connu une croissance frénétique depuis 2016, passant d'une valeur de marché marginale de juste plus de 6 milliards de dollars à un marché qui pourrait atteindre 210 milliards de dollars de ventes (y compris le matériel) d'ici 2022. Parmi ces technologies, la Réalité Augmentée est celle qui connaît une croissance constante.

Au début, un développeur JavaScript (web) souhaitant se lancer dans l'AR pourrait se sentir découragé en découvrant les compétences habituellement requises ; et il y a ceux qui demandent des connaissances en Machine Learning ou en Internet des Objets. Cependant, si vous êtes principalement un développeur JavaScript, considérez-vous comme chanceux : le langage est régulièrement mentionné comme l'un de ceux que vous devez connaître pour entrer dans ce secteur. La raison ? Actuellement, **beaucoup de développement AR se fait sur le web**. Et c'est là que JavaScript règne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m3EEXIiH_ZXxVzl-7-grLg.png)
_Mobile et Web ont été les derniers à obtenir des capacités AR, et sont encore en développement (extrait d'une présentation buildAR)_

### Emplois Augmentés pour les fans de JavaScript — Vraiment ?

Peut-être pas trop vite. Il existe de nombreux exemples où l'AR/MR/VR brille par elle-même, en particulier sur des marchés de niche, mais l'industrie n'a pas encore complètement compris toute la valeur de la technologie pour le consommateur général. Une fois ce problème résolu, l'industrie fabriquera certainement plus de produits AR/MR/VR, ce qui se traduira par plus d'emplois.

Pour certains analystes, l'AR devrait avoir l'impact le plus envahissant, en partie parce qu'elle ne nécessite pas de dispositifs et de conditions spécifiques pour être mise en œuvre, contrairement à la VR.

> L'AR a une utilité pour presque tout, superposant des informations utiles et pertinentes sur le monde qui vous entoure. L'AR peut être envahissante d'une manière que la VR ne peut pas.

> - David McQueen -Strategy Analytics- [d'une interview sur Twice](https://www.twice.com/product/ces-2018-how-disruptive-can-vr-ar-become-roundtable-discussion)

Il appartient à l'industrie de trouver comment faire de l'AR une technologie plus quotidienne. Selon certaines entreprises, en particulier dans le domaine des téléphones mobiles, exploiter le potentiel de l'AR revient à une règle bien connue : _SIMPLICITÉ_.

> Bien que Unity soit devenu le chemin par défaut pour construire des applications AR, un nombre croissant d'applications n'ont besoin que d'une touche d'AR.

> - d'un [article](https://medium.com/homestory-ar/building-an-ar-ai-furniture-app-with-react-native-1847bc1fcbaa) par [Benjamin Devine](https://www.freecodecamp.org/news/an-intro-to-augmented-reality-for-the-javascript-developer-with-an-example-71875ab184ee/undefined), Homestory AR

Dans de nombreux cas, recourir aux outils AR leaders pourrait être un surkill. Au lieu de cela, un ensemble de bonnes fonctionnalités pilotées par l'UX sur certains actifs 2D/3D pourrait être plus que suffisant pour créer des produits frappants. Quelque chose qu'un développeur JavaScript fait régulièrement.

Il est donc possible que tout développeur JavaScript intégrera des fonctionnalités AR/VR (non) standard comme une extension de ses tâches traditionnelles à l'avenir. Et si nécessaire, JavaScript est suffisamment robuste pour des tâches plus complexes. Le ciel est la limite.

### Devenir JavaScript-Augmenté

Avant de commencer, je vous suggérerais de jeter un coup d'œil aux différentes plateformes et standards AR. Les mêmes contraintes techniques affectant l'industrie sont également reflétées dans le monde AR.

Par exemple, il existe plusieurs plateformes, une pour chaque grande entreprise technologique (Google = [ARCode](https://developers.google.com/ar/discover/), Apple = [ARKit](https://developer.apple.com/arkit/), MS = [ChakraCore](https://github.com/microsoft/chakracore), Facebook = [AR Studio](https://developers.facebook.com/blog/post/2018/05/01/ar-studio-create-distribute/), [React 360](https://facebook.github.io/react-360/), Mozilla = [aframe](https://aframe.io/)).

Après avoir jeté un coup d'œil rapide aux options, commencer des projets de Réalité Augmentée entièrement en JavaScript est relativement facile. Vous pouvez commencer par prendre n'importe quel framework de développement web/app comme [Cordova](https://cordova.apache.org/), [Ionic](https://ionicframework.com/), [React Native](https://facebook.github.io/react-native/) ou [Vue Native](https://vue-native.io/) pour intégrer le framework AR de votre choix — et déployer des actifs 3D sur le monde réel.

Si ce que vous voulez est de déployer sur le web en utilisant principalement de l'AR basée sur des marqueurs, vous pourriez utiliser des dépôts GitHub comme [AR.js](https://github.com/jeromeetienne/AR.js) (gratuit), [argon.js](https://www.argonjs.io/) (gratuit mais limité) ou [awe.js](https://awe.media/) (PaaS payant mais avec un ancien dépôt GitHub toujours disponible). Il existe quelques solutions sur mesure qui sont plus difficiles pour les novices, beaucoup d'entre elles étant axées sur des choses comme la reconnaissance faciale/capitaire (comme [tracking.js](https://trackingjs.com/) et [headtrackr](https://github.com/auduno/headtrackr)).

Ou vous pouvez booster les capacités de votre projet si vous êtes en mesure de porter des SDK disponibles créés par des entreprises liées à l'AR. Il existe de nombreuses API qui rendent également l'AR sur navigateur. Par exemple, [Mapbox](https://www.mapbox.com/) suit ce chemin et est développé en JavaScript.

Je vous suggérerais de garder cela simple mais interactif.

Cependant, si vos ambitions visent également à maîtriser la conception et l'animation en JavaScript, vous devez absolument apprendre au moins un package JavaScript 3D, et [THREE.js](https://threejs.org/) est le plus populaire. Attendez, cependant, jusqu'à ce que vous ayez acquis une bonne base de JavaScript et d'[OpenGl](https://www.opengl.org/) ainsi que de géométrie, trigonométrie, algèbre linéaire ou physique. Et n'attendez pas plus d'aide des GUIs JS 3D existants ; en particulier, THREE.js n'en a pas. Challenging mais excitant !

### Exemple Bonus

Je voulais préparer une démonstration rapide juste pour explorer la technologie, alors j'ai pris un joli CodePen et je l'ai modifié pour qu'il s'adapte à une animation AR basée sur des marqueurs et rendue sur le web, portée dans un clone du [grand travail](https://stemkoski.github.io/AR-Examples/) de [Stemkoski](https://github.com/stemkoski/AR-Examples) avec AR.js.

Pour voir l'exemple, vous avez besoin d'un appareil mobile avec une caméra et internet (téléphone ou tablette), et soit une copie imprimée du marqueur, soit un autre appareil pour l'afficher à l'écran.

Prêt ? Ouvrez maintenant ce [lien](https://evaristoc.github.io/ARexample/) en utilisant un navigateur sur votre appareil mobile :

[https://evaristoc.github.io/ARexample/](https://evaristoc.github.io/ARexample/)

Donnez l'autorisation d'utiliser votre caméra, et pointez la caméra vers un marqueur comme ci-dessous, soit imprimé, soit sur un autre écran.

**NOTE :** fonctionne sur Android et Chrome — cela pourrait ne pas fonctionner pour d'autres appareils et navigateurs ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7g9MciK6LR-9VRcH-LePSQ.png)
_L'animation originale peut être trouvée [ici](https://codepen.io/rainner/details/LREdXd)._

Bonne Année !

J'espère que vous trouverez cette technologie aussi fascinante que moi. Si c'est le cas, ne restez pas seul : contactez-nous sur le [forum freeCodeCamp](https://www.freecodecamp.org/forum/) et partagez vos questions et idées.

Et si vous avez aimé cet article, n'oubliez pas de lui donner un ? et de le partager sur les réseaux sociaux.

Merci pour la lecture, profitez de l'AR et Bon Codage !!