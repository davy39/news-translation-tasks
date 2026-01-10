---
title: Nous avons construit un bac à sable ouvert pour entraîner les mains robotiques
  à saisir des objets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-29T04:34:23.000Z'
originalURL: https://freecodecamp.org/news/an-open-sandbox-for-robot-grasping-cee467a3fabb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*z4z_pGa-kSvjO-kgvwOetA.jpeg
tags:
- name: Docker
  slug: docker
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: robotics
  slug: robotics
- name: 'tech '
  slug: tech
seo_title: Nous avons construit un bac à sable ouvert pour entraîner les mains robotiques
  à saisir des objets
seo_desc: 'By Ugo Cupcic

  Getting started with robotics is probably a lot easier than you think. Here’s a
  simulation sandbox that’s cross-platform and provides a simple high level API. It
  should help you get started experimenting with robot grasping tasks.

  As th...'
---

Par Ugo Cupcic

Se lancer dans la robotique est probablement beaucoup plus facile que vous ne le pensez. Voici un bac à sable de simulation qui est multiplateforme et fournit une API simple de haut niveau. Il devrait vous aider à commencer à expérimenter avec des tâches de préhension robotique.

En tant qu'Architecte Technique en Chef chez [Shadow Robot Company](http://www.shadowrobot.com/), je passe beaucoup de temps à jouer avec différents algorithmes pour voir comment ils pourraient s'adapter à nos robots. Contrôler un robot complexe pour qu'il se comporte comme vous le souhaitez dans un environnement complexe est... complexe !

Une partie importante de notre feuille de route repose sur **l'apprentissage automatique**. Je ne veux pas avoir à spécifier chaque aspect d'un problème — je préfère que le système apprenne lui-même la meilleure façon d'aborder un problème donné.

Configurer l'environnement pour essayer facilement différents algorithmes d'apprentissage automatique — par exemple pour affiner les préhensions — n'est pas trivial. Voici mes exigences :

* **une** **bonne scène de simulation** pour commencer : un robot, un capteur 3D, quelques objets avec lesquels interagir, quelques meubles pour planifier autour et utiliser
* **une** **variété d'outils** et de bibliothèques pour commencer rapidement à jouer avec le robot : framework robotique ([ROS](http://www.ros.org)), simulateur ([Gazebo](http://gazebosim.org/)), bibliothèques de planification ([MoveIt!](http://moveit.ros.org))
* **un moyen de l'exécuter** **en mode headless** tout en pouvant visualiser les données
* **facilement** **déployable**, bien documenté... tout ce qu'il y a de plus habituel !

Si vous ne voulez pas lire les spécificités mais souhaitez simplement mettre la main sur le bac à sable, vous pouvez vous rendre sur le [dépôt github](https://github.com/shadow-robot/smart_grasping_sandbox) qui contient les instructions pour un démarrage rapide. Pour utiliser le bac à sable dans le cloud, vous pouvez également visiter le [ROS Development Studio](http://rds.theconstructsim.com/) où il est déployé.

### La simulation

Le Smart Grasping Sandbox fonctionnera sur le [Robotic Operating System](http://www.ros.org) — **ROS**. En tant qu'utilisateur et contributeur de longue date de ROS, je suis très partial à l'utilisation de ce framework. C'est le framework open source *de facto* conçu pour la robotique. Il élimine les tracas de la connexion des différents composants d'un système robotique avec une approche modulaire. Cela permet de remplacer facilement un composant donné. En plus de cela, il est soutenu par une communauté dynamique, vous pouvez donc toujours trouver le dernier algorithme ou pilote.

Pour enseigner à un robot, il est bon de commencer par un simulateur. Exécuter les algorithmes sur le matériel réel n'est pas seulement plus coûteux mais souvent moins pratique : il est plus difficile de réinitialiser l'environnement dans la vie réelle que dans la simulation. Il est également souvent plus difficile de caractériser l'impact du robot sur la scène : la balle a-t-elle été ramassée ? La préhension était-elle stable ? Toutes ces informations sont disponibles directement dans un simulateur.

Le simulateur que nous utiliserons est [**Gazebo**](http://gazebosim.org) ; il s'agit d'un simulateur physique pour la robotique et il est également étroitement intégré au framework ROS. De nombreux modèles de robots sont disponibles dans le simulateur, des bras et des pinces aux quadricoptères ! Dans le Smart Grasping Sandbox, le robot que je fournis est un [UR10 de Universal Robot](https://www.universal-robots.com/products/ur10-robot/?ads_cmpid=38441226&ads_adid=36523128894&ads_matchtype=b&ads_network=g&ads_creative=166486296408&utm_term=ur10&ads_targetid=kwd-951605358&utm_campaign=&utm_source=adwords&utm_medium=ppc&ttv=2&gclid=CNCC_p_c_dECFbcK0wodyCED_w) avec le [Smart Grasping System](https://www.shadowrobot.com/shadow-smart-grasping-system/) de Shadow. La scène ne contient pour l'instant que deux objets utiles : une balle de cricket et une perceuse. Ce n'est qu'un point de départ. La scène évoluera avec le temps. Le capteur de vision 3D dans la simulation est un [Microsoft Kinect](https://en.wikipedia.org/wiki/Kinect) car il est souvent utilisé en robotique (oui, le même Kinect que vous utilisiez pour jouer à *Just Dance* sur votre Xbox).

### Conteneur Docker

Configurer les différents frameworks et bibliothèques n'est pas trivial et prend du temps. Pour simplifier le déploiement, je construis automatiquement une image [Docker](https://www.docker.com/). Si vous n'êtes pas familier avec Docker, je n'entrerai pas dans les détails car cela dépasse le cadre de cet article, mais disons que c'est un environnement de type machine virtuelle super léger : vous pouvez créer des images très rapidement tout en exploitant tout le potentiel de votre ordinateur.

Déployer l'image avec Docker la rend également agnostique en termes de système d'exploitation — ROS et Gazebo sont plus adaptés à Linux. C'est aussi un excellent moyen de tester des choses sur votre ordinateur portable, puis une fois que vous êtes prêt à commencer une expérience plus longue, il suffit de la lancer dans le cloud. Puisque j'ai inclus une interface web pour le simulateur, vous pouvez même visualiser ce qui se passe dans la simulation en vous connectant via votre navigateur. Pour faciliter le processus de développement, j'ai inclus un [Jupyter notebook](http://jupyter.org/) auquel vous pouvez accéder via votre navigateur.

### Bibliothèques et outils

Pour accélérer votre processus de développement, j'ai développé une bibliothèque simple de haut niveau — audacieusement appelée *SmartGrasper*. Cette bibliothèque permet d'interagir directement avec le bac à sable simulé en envoyant des commandes telles que prendre la balle, ouvrir la main, se déplacer au-dessus de la balle... Pour la planification de trajectoire, elle repose sur la bibliothèque de planification de ROS : [MoveIt!](http://moveit.ros.org), afin que vous puissiez [déplacer le robot de A à B sans heurter les objets](https://medium.com/@ugocupcic/how-to-make-your-robot-go-from-a-to-b-without-hitting-things-1063a8890947).

![Image](https://cdn-media-1.freecodecamp.org/images/1*TfmzfFUkM-krMzLyFfumnQ.png)
_cahier iPython_

Le bac à sable est livré avec un exemple de cahier iPython qui montre comment ramasser la balle en utilisant la bibliothèque SmartGrasper. Vous pouvez utiliser cet exemple comme base pour vos propres développements.

### Mots de la fin

J'ai donc passé du temps à préparer ce bac à sable et maintenant qu'il est prêt, [je le partage avec vous](https://github.com/shadow-robot/smart_grasping_sandbox)! Rendez-vous sur le [dépôt github shadow-robot/smart-grasping-sandbox](https://github.com/shadow-robot/smart_grasping_sandbox) pour commencer. N'hésitez pas à jouer avec, [soumettre des problèmes](https://github.com/shadow-robot/smart_grasping_sandbox/issues), des demandes de tirage...

Il reste encore beaucoup à faire : ajouter [OpenRave](http://www.openrave.org) pour la planification des préhensions, ajouter plus de complexité à la scène pour pouvoir apprendre différentes actions, ajouter quelques algorithmes de vision pour reconnaître les différents objets... Mais ce n'est que la première version du Smart Grasping Sandbox !

![Image](https://cdn-media-1.freecodecamp.org/images/1*98Bu_qcmt975ADGwoKQYJA.png)
_Le Smart Grasping Sandbox dans The Construct_

Je travaille également avec l'équipe incroyable de The Construct pour rendre le Smart Grasping Sandbox disponible sur le [ROS Development Studio](http://rds.theconstructsim.com) pour une manière encore plus rapide de tester vos idées.

*Si vous faites quelque chose de cool avec le Smart Grasping Sandbox, ou si vous avez des questions, connectons-nous sur [Twitter](http://twitter.com/ugocupcic)! Si vous avez aimé cet article, pourquoi ne pas l'aimer et le partager ?*

![Image](https://cdn-media-1.freecodecamp.org/images/1*bYWLCSD5yxrMMlBV-nNaDA.gif)