---
title: Comment utiliser la Réalité Augmentée avec JavaScript — une étude de cas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T13:28:42.000Z'
originalURL: https://freecodecamp.org/news/augmented-reality-with-javascript-a-case-study-c9cffaadcf07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*evN61t_cenPxPZgDZOB2Mw.png
tags:
- name: AR
  slug: ar
- name: Augmented Reality
  slug: augmented-reality
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Virtual Reality
  slug: virtual-reality
seo_title: Comment utiliser la Réalité Augmentée avec JavaScript — une étude de cas
seo_desc: 'By Apurav Chauhan

  In this experiment, I talk about how Augmented Reality with JS can be used to make
  learning more fun and interactive. The case study will discuss the design process,
  implementation and feedback from children in the age group 2 to 10...'
---

Par Apurav Chauhan

Dans cette expérience, je parle de la manière dont la Réalité Augmentée avec JS peut être utilisée pour rendre l'apprentissage plus amusant et interactif. L'étude de cas discutera du processus de conception, de la mise en œuvre et des retours d'enfants dans la tranche d'âge de 2 à 10 ans.

![Image](https://cdn-media-1.freecodecamp.org/images/1*evN61t_cenPxPZgDZOB2Mw.png)
_Éducation et apprentissage interactif des alphabets utilisant la Réalité Augmentée et Javascript_

La Réalité Augmentée (AR) m'a toujours attiré, et dans cette expérience, j'essaie de créer une application AR pratique. Le cas d'utilisation que nous allons couvrir est l'éducation primaire et nous verrons comment nous pouvons rendre l'apprentissage amusant et interactif. Nous allons créer une application pour apprendre les alphabets dans trois langues principalement : le Pendjabi, l'Hindi et l'Anglais.

_L'application Javascript de Réalité Augmentée n'a actuellement pas de détection de plan. Pour simplifier, nous superposons simplement nos objets sur la vue avec un suivi de mouvement 3D._

#### OBJECTIF FINAL

Ci-dessous une démonstration de notre expérience AR Javascript. Vous pouvez télécharger et jouer avec l'application [ici](https://play.google.com/store/apps/details?id=com.webilm.games.arlearning&hl=en).

Le code complet a été open-sourcé à des fins d'apprentissage et est disponible [ici](https://github.com/apuravchauhan/augmented-reality-javascript).

![Image](https://cdn-media-1.freecodecamp.org/images/1*nfxElKKhaa0zlcdODDdtPg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*O6FCNchAd2dNaJwK32GL-A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UKBmHOO3uW7NIKuoHYDNXA.jpeg)
_Alphabets en réalité augmentée et javascript pour rendre l'éducation plus amusante et engageante_

### Le Processus de Conception

Pour rendre l'apprentissage amusant et sans effort, je m'appuie sur les points suivants :

1. Participation active de l'enfant
2. Activité physique de l'enfant au lieu de rester assis à un seul endroit
3. Un peu d'effort pour trouver les alphabets.
4. UX/UI intuitive.

Le thème central de l'application sera assez similaire à la célèbre application de réalité augmentée Pokemon Go. Seuls deux composants principaux seront impliqués : la **Vue Caméra** et les **Alphabets**.

#### UX des Alphabets pour le Jeu AR

_Itération 1_

![Image](https://cdn-media-1.freecodecamp.org/images/1*_711pNZKifCSaa9bXWbc5g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YdiDXaHGXYKPMD1gdGbZaw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EmkTDWxyVZYcqA9vn2Ixtg.png)
_Alphabets 2D en Anglais, Hindi et Pendjabi pour notre Jeu de Réalité Augmentée JS_

Dans notre première itération, nous avons des alphabets 2D que nous allons essayer de fusionner dans notre vue caméra. L'idée de l'application de Réalité Augmentée (AR) est d'avoir des enfants qui trouvent ces lettres de l'alphabet dans une pièce ou un espace autour d'eux. Le prototype après la fusion de l'espace avec des alphabets 2D ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gu70VjYLyFLzzmMvhafZyA.gif)
_Capteur de mouvement AR avec objet 2D_

Comme vous pouvez le voir ci-dessus, l'expérience immersive est manquante avec un modèle 2D car l'œil humain voit les choses en 3D.

_Itération 2_

Essayons de créer un modèle 3D et voyons si nous pouvons améliorer l'expérience de notre jeu de Réalité Augmentée basé sur Javascript :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lHUszUcxZfFJj0f81Ebixg.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*cyXqdHs11SmHwICi-P461g.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GK2PuNQlEEJU8FY9edCR8A.gif)
_Alphabets 3D en Anglais, Hindi et Pendjabi pour notre projet AR_

Et ci-dessous la comparaison de l'expérience d'un capteur de mouvement avec des modèles d'alphabets 2D vs 3D. Comme vous pouvez le voir, le 3D vous donne naturellement une expérience beaucoup plus immersive en matière de réalité augmentée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gu70VjYLyFLzzmMvhafZyA.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IPTMBO-kP6EcqhL0tDD_8A.gif)
_Expérience de mouvement AR 2D vs 3D_

### Le Processus de Mise en Œuvre de la Réalité Augmentée

Pour mettre en œuvre le concept AR ci-dessus, j'utiliserai les outils et technologies suivants :

1. [Ionic Framework](https://ionicframework.com) : Pour construire l'application hybride
2. [Aframe](https://aframe.io/) : Pour apporter l'expérience de la réalité virtuelle (VR) et de la réalité augmentée (AR) à notre application
3. [MagicaVoxel](https://ephtracy.github.io/) : Pour créer nos modèles 3D

Le processus de base de construction de l'application est très simple. Vous pouvez suivre mon article précédent pour apprendre comment construire et déployer une application en utilisant le framework Ionic [ici](https://codeburst.io/part-1-simple-ionic-tutorial-from-scratch-from-0-to-live-app-9a79db510a90).

Une fois que vous avez suivi le tutoriel ci-dessus pour créer une application simple, il est temps d'intégrer Aframe pour apporter nos alphabets 3D avec des capteurs de mouvement dans notre application.

Chargez simplement les bibliothèques core et loader d'Aframe dans le fichier index.html du projet Ionic :

```
<script src="https://aframe.io/releases/0.8.2/aframe.min.js"></script>
```

```
<script src="https://rawgit.com/donmccurdy/aframe-extras/v2.1.1/dist/aframe-extras.loaders.min.js"></script>
```

Avec cela, nous sommes prêts à faire un peu de magie AR/VR dans notre base de code Javascript.

Maintenant, dans votre composant home.html, incluons nos modèles 3D exportés depuis MagicaVoxel :

Et cela devrait rendre une scène 3D prête pour l'interaction avec tous les capteurs de mouvement prêts :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fref3HwlAuN0AJ9VHRaWhQ.gif)
_Scène finale de Réalité Virtuelle 3D prête avec des alphabets 3D_

#### Ajout de l'Effet de Réalité Augmentée

La dernière partie de cette expérience consiste à ajouter l'effet de Réalité Augmentée (AR) dans notre application hybride basée sur Javascript. Comme déjà expliqué, la Réalité Augmentée consiste à superposer des modèles 3D ou d'autres objets sur votre vue caméra. La seule chose manquante est donc la vue caméra derrière notre scène.

Pour ce faire, nous utilisons le plugin de prévisualisation de la caméra comme expliqué [ici](https://ionicframework.com/docs/native/camera-preview/). Et voici le gist complet après l'intégration avec le plugin de prévisualisation de la caméra :

Nous devons également nous assurer que nos arrière-plans sont transparents afin que la prévisualisation de la caméra soit visible sur mobile. Cela est très **IMPORTANT**, sinon vous pourriez penser que le plugin ne fonctionne pas. Voici le fichier home.scss avec le CSS de transparence activé :

**Et voici à quoi cela ressemblerait finalement :**

#### Réaction des utilisateurs à notre jeu JS de réalité augmentée

La dernière étape pour mesurer le succès de votre concept est la validation par de vrais utilisateurs — dans notre cas, des enfants :) Et voici leurs retours en direct enregistrés.

Il était assez clair que chacun d'eux a apprécié le jeu et nous avons obtenu la note maximale pour la partie amusement. Cependant, au début, j'ai dû leur dire de bouger le téléphone dans l'espace pour trouver les lettres. Points perdus en termes d'intuitivité :(

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fe97s79RI5BFONl9X5T27w.png)
_Points obtenus sur 10_

#### Retours des utilisateurs pour le jeu JS de réalité augmentée

### Réflexions Finales

C'était un projet passionnant et j'ai pu voir un grand potentiel pour la Réalité Augmentée dans l'apprentissage et l'éducation. Les enfants l'adorent vraiment et cela ajoute certainement le facteur amusement manquant à l'éducation, surtout dans notre système éducatif monotone.

N'hésitez pas à commenter et à partager vos retours.

### Téléchargements

Le code de cette application est disponible sur [github](https://github.com/apuravchauhan/augmented-reality-javascript). N'hésitez pas à jouer et à ajouter de nouvelles fonctionnalités. Je serai ravi de pousser les mises à jour en production.

Vous pouvez télécharger l'application pour Android [ici](https://play.google.com/store/apps/details?id=com.webilm.games.arlearning&hl=en).