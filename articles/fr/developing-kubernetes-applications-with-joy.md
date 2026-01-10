---
title: Comment développer des applications Kubernetes avec plaisir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-20T08:55:00.000Z'
originalURL: https://freecodecamp.org/news/developing-kubernetes-applications-with-joy
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/ships-wheel.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Continuous Integration
  slug: continuous-integration
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: Kubernetes
  slug: kubernetes
- name: Visual Studio Code
  slug: vscode
seo_title: Comment développer des applications Kubernetes avec plaisir
seo_desc: "By Sven Efftinge\nLet’s face it: Developing distributed applications is\
  \ painful.\nMicroservice architectures might be great for decoupling and scalability\
  \ but they are intimidatingly complex when it comes to development. \nLocal Kubernetes\
  \ clusters (Min..."
---

Par Sven Efftinge

**Admettons-le : Développer des applications distribuées est douloureux.**

Les architectures de microservices peuvent être excellentes pour le découplage et la scalabilité, mais elles sont intimidantes en termes de complexité lors du développement. 

Les clusters Kubernetes locaux (Minikube), les longs temps de build (Docker) et les solutions de débogage maladroites ou même inexistantes étaient notre point de départ. Deux ans plus tard, nous avons tout automatisé : plus rien ne tourne sur ma machine locale et je peux commencer à coder et à déboguer des composants individuels sur n'importe quelle branche en seulement 15 secondes. ?

Je prends maintenant tellement de plaisir à travailler sur notre projet et je crois que c'est l'une des configurations les plus optimisées qui existent. Dans ce qui suit, je souhaite partager cette expérience.

## Commencer avec un environnement de prévisualisation

Pour commencer à travailler sur une correction de bug ou une fonctionnalité, je dois simplement créer une nouvelle branche sur GitHub. Cela déclenche immédiatement nos serveurs CI (nous utilisons Jenkins) qui déploiement ensuite une application de prévisualisation sur un cluster GKE. L'application réside dans un namespace correspondant au nom de la branche et, en utilisant l'URL de prévisualisation, je peux accéder et utiliser l'application.

Puisque je n'ai créé qu'une branche et que je n'ai pas poussé de modifications, les artefacts de build sont mis en cache et le déploiement ne prend que quelques secondes. Mais même une fois que j'ai poussé des modifications, le build s'exécutera rapidement car il ne reconstruit que ce qui est vraiment nécessaire.

## Commencer à coder

Ensuite, je lance un environnement de développement pour travailler sur ma tâche. Nous utilisons [Gitpod](https://www.gitpod.io), qui, similaire à un serveur CI, préconstruit des environnements de développement pour toute branche. Un clic sur un bouton depuis n'importe quelle page GitHub de notre projet démarre un nouvel environnement de développement pour exactement cette branche et l'ouvre dans mon navigateur.

L'environnement de développement est prêt après ~15 secondes et m'attend avec un clone frais de notre dépôt et la bonne branche sélectionnée. De plus, le projet est entièrement construit et toutes les dépendances sont déjà téléchargées. Le terminal m'accueille avec le message suivant :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-13.19.06.png)

L'IDE est préconfiguré avec toutes les extensions VS Code dont nous avons besoin, dans notre cas Kubernetes, Docker, MySQL, Go et TypeScript. Il est également déjà connecté au cluster Kubernetes exécutant l'environnement de prévisualisation ainsi qu'à la base de données correspondante. Ainsi, je peux, par exemple, taper '_kubectl get all_' dans mon terminal et voir tous les objets kube déployés.

La connexion est basée sur un jeton secret que chaque développeur doit mettre dans son compte utilisateur une fois et qui est injecté lors du démarrage d'un environnement de développement.

Bien que ces environnements de développement éphémères s'exécutent dans mon navigateur, ils fournissent tous les outils modernes, me permettant de coder, compiler, exécuter et déboguer du code ainsi qu'interagir avec la base de données et le cluster.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-13.23.33-1.png)

Bien sûr, je peux maintenant pousser n'importe quelle modification de mon code vers GitHub et attendre que le CI mette à jour mon environnement de prévisualisation en conséquence. Comme le build utilise largement la mise en cache, les petites modifications sont déployées en une minute environ. La plupart du temps, cependant, une minute est bien trop longue. Nous avons besoin d'une expérience de rechargement instantané qui permet de déboguer n'importe quel service dans le contexte de l'application complète. Entrez _Telepresence_.

## Débogage avec Telepresence

Je veux pouvoir déboguer n'importe quel service individuel dans le contexte de l'application complète. Au lieu d'attendre les redéploiements, nos composants ont des configurations de lancement appropriées pour les déboguer en utilisant [Telepresence](https://telepresence.io).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/bird-on-bricks.svg)

Telepresence remplace un déploiement Kubernetes par un proxy qui transfère toute la communication à un processus s'exécutant localement. Ainsi, en bref, je peux démarrer une session de débogage locale et la faire fonctionner dans le contexte de mon environnement de prévisualisation.

Cela fonctionne de manière fantastique et est la meilleure façon que j'ai vue jusqu'à présent pour déboguer les services Kubernetes. Cela me permet de réutiliser tous les outils de débogage existants disponibles.

## Pousser et réviser

Une fois que je suis satisfait de mes modifications, je les pousse vers ma branche et crée une Pull Request. Je peux le faire depuis Gitpod, ce qui est assez pratique.

Jenkins va maintenant mettre à jour l'environnement de prévisualisation et Gitpod préconstruit un nouvel environnement de développement. Ainsi, lorsqu'un collègue souhaite commencer à réviser mes modifications, il peut les essayer immédiatement et lancer rapidement un environnement de développement pour une inspection plus approfondie. Depuis Gitpod, ils peuvent ajouter des commentaires au code et même approuver (ou rejeter) la PR.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-11.54.50.png)
_Notre chaîne d'outils_

## Conclusion

Atteindre des cycles rapides et des configurations automatisées pour les applications distribuées est difficile mais une nécessité absolue pour entrer dans un flux productif. Toute friction dans ce processus aura un mauvais effet sur la productivité de votre équipe.

Un build rapide avec des environnements de prévisualisation et l'expérience de débogage fluide basée sur Telepresence ont été un gain de productivité agréable pour nous. Si Gitpod n'existait pas, nous devrions le construire ;).

Avez-vous des questions ? [Contactez-nous](https://www.typefox.io/contact/), nous sommes heureux de vous aider.

---

> Note : Certaines des fonctionnalités de Telepresence nécessitent des appels système qui sont actuellement uniquement autorisés dans Gitpod auto-hébergé.