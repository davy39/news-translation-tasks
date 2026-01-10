---
title: Comment analyser la sécurité de votre application avec la modélisation des
  menaces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T11:09:14.000Z'
originalURL: https://freecodecamp.org/news/threat-modeling-goran-aviani
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/image-44-1.png
tags:
- name: Application Security
  slug: application-security
- name: Stride
  slug: stride
- name: threat modeling
  slug: threat-modeling
seo_title: Comment analyser la sécurité de votre application avec la modélisation
  des menaces
seo_desc: 'By Goran Aviani

  Digital attacks are more and more frequent, and the first step in securing your
  app is understanding the threats and how to counter them.

  Threat modeling is an approach that analyses the security of an application. It
  is a structured ...'
---

Par Goran Aviani

Les attaques numériques sont de plus en plus fréquentes, et la première étape pour sécuriser votre application est de comprendre les menaces et comment les contrer.

La modélisation des menaces est une approche qui analyse la sécurité d'une application. C'est une méthode structurée pour identifier, quantifier et atténuer les risques de sécurité dans une application.

Vous êtes sur le point de lire un bref résumé que j'ai écrit pour moi-même il y a quelque temps, composé d'informations que j'ai collectées en disséquant plusieurs autres articles. L'idée derrière cet article est qu'il serve de rappel et soit aussi court que possible tout en contenant des informations pertinentes.

---

Cela étant dit, écrivons la définition la plus courante de la modélisation des menaces :

> La modélisation des menaces est un processus de sécurité dont les objectifs sont d'identifier les objectifs et les vulnérabilités, puis de définir des contre-mesures pour prévenir ou réduire les effets des menaces sur le système.

J'ai également lu que la modélisation des menaces répond à ces quatre questions :

* _Sur quoi travaillons-nous ?_
* _Qu'est-ce qui peut mal tourner ?_
* _Que allons-nous faire à ce sujet ?_
* _Avons-nous fait du bon travail ?_

Et je ne pourrais pas être plus d'accord. C'est pourquoi la modélisation des menaces est composée de quatre parties, où chaque partie répond à une question :

* _Décomposer l'application._
* _Déterminer les menaces._
* _Déterminer les contre-mesures et les atténuations (réduire le danger)._
* _Classement des menaces._

# Décomposer l'application

L'objectif de cette étape est de comprendre l'application en la décomposant en parties et en voyant comment ces parties interagissent avec des entités externes. La façon de faire cela est de recueillir des informations et de la documentation en cartographiant les points d'entrée de l'application, les éléments/actifs et les dépendances.

* Décomposer l'application en dessinant un diagramme des divers composants de l'application. Vous pouvez faire cela avec des diagrammes de flux de données.
* Identifier les points d'entrée — Les points d'entrée logiciels peuvent servir de points d'entrée pour un attaquant (pages de connexion, champs de recherche, requêtes HTTP, etc.). Il est essentiel que tous les points d'entrée soient identifiés et documentés.
* Identifier les éléments/actifs — qui ont une valeur, et donc un risque d'être attaqués. Un actif peut être sous forme de données comme une liste d'informations clients, il peut également être sous différentes formes : disponibilité globale de l'application, réputation de l'organisation.
* Les dépendances sont des parties de l'application qui se trouvent à l'extérieur du code de l'application. Comme ces éléments sont hors de votre contrôle, ils peuvent poser une menace s'ils ne sont pas correctement maintenus, donc identifier ces dépendances minimisera le risque global de l'application.

# Déterminer les menaces

Déterminer les menaces peut être fait par la catégorisation des menaces STRIDE. STRIDE est une approche du point de vue de l'attaquant, et elle est utilisée pour déterminer les menaces. Bien qu'il existe d'autres approches telles que ASF (Application Security Framework — une approche du point de vue du défenseur pour déterminer les contre-mesures), dans cet article, je me concentrerai sur STRIDE.

> La catégorisation STRIDE décrit six types de menaces les plus courants et leurs contre-mesures.

## STRIDE

1. **S**poofing identity — Usurper l'identité de quelqu'un ou de quelque chose d'autre.
2. **T**empering with data — Modifier certaines données sur le disque, le réseau, la mémoire.
3. **R**eputation — Nier la preuve d'une action.
4. **I**nformation disclosure — Exposer des informations à quelqu'un non autorisé à les voir.
5. **D**enial of service — Refuser ou dégrader le service aux utilisateurs.
6. **E**levation of privileges — Obtenir des droits non autorisés supérieurs à ceux initialement prévus.

# Déterminer les contre-mesures

Chaque menace de STRIDE a une contre-mesure.

1. Authentification (pour Spoofing) — Établir une identité vérifiable.
2. Protection des données (pour Tempering with data) — Maintenir les données et assurer la cohérence des données et des méthodes qui travaillent sur les données.
3. Confirmation (pour Reputation) — Chaque action contre l'application doit être enregistrée.
4. Confidentialité (pour Information disclosure) — Restreindre l'accès au système et aux données.
5. Disponibilité (pour Dos) — Utiliser des niveaux de redondance.
6. Autorisation (pour Elevation of privileges) — Limiter l'accès aux données, actions et services.

# Classer les menaces

Pour aborder le problème du classement des menaces, Microsoft a conçu un modèle d'évaluation des risques appelé DREAD, un modèle qui fournit cinq catégories de notation pour chaque menace. Au début, ils utilisaient une notation de 1 à 10, par exemple, pour chaque menace dans chaque catégorie, une note de 1 à 10 serait donnée.

Cependant, comme différentes personnes sélectionnaient des nombres très différents, il y a eu un passage des notes DREAD dans des plages de nombres élevées vers une classification plus simple avec 4 niveaux de risque différents :

* 1 : faible
* 2 : moyen
* 3 : élevé
* 4 : critique

La somme de toutes les notes pour une menace donnée est utilisée pour la prioriser parmi les autres menaces.

Les catégories à noter pour chaque menace sont :

* **D**ommage — à quel point une attaque serait-elle grave ?
* **R**éproducibilité — à quel point est-il facile de reproduire l'attaque ?
* **E**xploitabilité — combien de travail faut-il pour lancer l'attaque ?
* **U**tilisateurs affectés — combien de personnes seront impactées ?
* **D**écouvrabilité — à quel point est-il facile de découvrir la menace ?

Pour chaque menace dans chaque catégorie, une note de 1 à 4 est donnée et la somme de toutes les notes pour une menace donnée est utilisée pour la prioriser parmi les autres menaces.

---

Jusqu'à présent, nous avons décomposé l'application, analysé les fonctionnalités, déterminé les risques possibles et identifié les points faibles qui pourraient être exploités. Ensuite, nous avons déterminé les contre-mesures et utilisé DREAD pour classer les risques. La seule chose restante est d'agir en conséquence pour résoudre ces risques.

---

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci sur mon profil freeCodeCamp : [https://www.freecodecamp.org/news/author/goran/](https://www.freecodecamp.org/news/author/goran/) et d'autres choses amusantes que je construis sur ma page GitHub : [https://github.com/GoranAviani](https://github.com/GoranAviani)