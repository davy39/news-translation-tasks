---
title: Qu'est-ce que l'ingénierie système ? Un guide pour débutants
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2022-04-18T15:18:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-systems-engineering
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/tt.jpeg
tags:
- name: systems-engineering
  slug: systems-engineering
seo_title: Qu'est-ce que l'ingénierie système ? Un guide pour débutants
seo_desc: 'I was recently reading J. Martin''s book Systems Engineering Guidebook
  – A Process for Developing Systems and Products. From it, I learned that systems
  engineering reduces manufacturing costs by 40% – did you know that?

  Neither did I. Even after takin...'
---

Je lisais récemment le livre de J. Martin _Systems Engineering Guidebook – A Process for Developing Systems and Products_. J'y ai appris que l'ingénierie système réduit les coûts de fabrication de 40 % – le saviez-vous ?

Moi non plus. Même après avoir suivi un cours où l'un des sujets était l'ingénierie système, je n'ai compris son importance que lorsque j'ai compris ses applications dans la vie réelle.

### Mais l'ingénierie système est-elle utilisée dans le développement logiciel ?

Oui !

Certaines grandes entreprises utilisent l'ingénierie système pour améliorer leurs produits. 

En fait, Google a sa propre discipline appelée [engineering productivity](https://landing.google.com/engprod/). 

Facebook a également la sienne, appelée [production engineering](https://engineering.fb.com/category/production-engineering/). 

De plus, Amazon emploie une [équipe](https://www.amazon.jobs/en/teams/aws-system-development-engineer) d'ingénieurs pour aider à construire son infrastructure de cloud computing.

Pour comprendre ce qu'est l'ingénierie système et son importance, répondons à quatre questions :

1. Qu'est-ce qu'un système ?
2. Quel est le cycle de vie d'un projet ?
3. Qu'est-ce que l'ingénierie système ?
4. Pourquoi l'ingénierie système est-elle importante ?

## Qu'est-ce qu'un système ?

Un système est une combinaison de nombreuses « choses » qui fonctionnent ensemble comme si elles formaient un tout.

Par exemple,

* Le système solaire
* Les arbres
* Les entreprises

Chacun de ces exemples a de nombreux composants (planètes, feuilles, départements) qui ensemble forment un tout.

Ces composants peuvent également être des sous-systèmes. Par exemple, notre système solaire a notre planète. Notre planète Terre a ses propres systèmes, tels que la géosphère, la biosphère, et ainsi de suite.

La géosphère est un _sous-système_ de la planète Terre. [2]

![Image](https://miro.medium.com/max/1242/1*eYsdUqZxsESlo2Q31JF6oQ.png)
_Exemple d'un système_



En programmation, vous pouvez voir les programmes comme des systèmes.

Par exemple, une fonction dans un programme donné pourrait être vue comme un élément du système.

En établissant un système des différents composants de votre programme, non seulement vous rendrez votre programme plus efficace, mais il deviendra également plus facile à maintenir et à développer à l'avenir.

Vous pouvez alors voir le système d'un programme comme une sorte d'architecture.

Voici un exemple de système en programmation :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--305-.png)
_Arborescence de fichiers du [modèle de site web htm5up](https://html5up.net/paradigm-shift)_

L'image montre la structure d'un répertoire (ou dossier) pour un projet de modèle de site web. 

Beaucoup de ces répertoires contiennent plusieurs fichiers .html, .css et .js.

Ces fichiers ont tous des composants et des caractéristiques qui interagissent avec d'autres fichiers à l'intérieur des projets. En essence, vous avez un système ici. 

Le projet entier est un système. Les sous-systèmes au sein de ce projet sont les répertoires. Chaque fichier dans un répertoire a de nombreux composants, qui constituent un projet dans son ensemble. 

En apprenant à créer un système, vous apprendrez à créer et à gérer des projets de manière plus efficace.

## Quel est le cycle de vie d'un projet ?

Le cycle de vie d'un projet fait référence aux étapes d'un certain projet – de l'idée à la création du projet, en passant par son utilisation éventuelle et sa fabrication finale.

Généralement, un cycle de vie de projet se compose de :

1. Idée
2. Création d'une idée
3. Création de concepts pour le concept de projet réel
4. Utilisation et support du projet
5. Désactivation

Ci-dessous se trouve un exemple qui explique comment vous pouvez appliquer l'ingénierie système pour développer un site web pour une entreprise.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/pexels-eduardo-dutra-2115217.jpg)
_[Photo par Eduardo Dutra de Pexels](https://www.pexels.com/photo/person-in-front-of-laptop-on-brown-wooden-table-2115217/)_

### Exemple de cycle de vie d'un projet

Supposons que vous dirigez une entreprise de logiciels et qu'un client vous a demandé de développer un site web pour son entreprise.

#### Trouver l'idée

Ici, vous devez avoir une conversation avec le client pour déterminer comment le projet sera développé et pour comprendre ce que le client veut réellement du projet.

Il est également bon de discuter avec le client des problèmes futurs potentiels qui pourraient survenir, qu'ils soient techniques ou financiers.

C'est de loin la phase la plus importante de tout le cycle de vie du projet.

Sans comprendre les besoins du client, vous ne pouvez pas accomplir les projets qu'il souhaite. Cela est vrai indépendamment de vos connaissances techniques.

#### Créer et développer l'idée

L'étape suivante consiste à planifier toutes les étapes nécessaires pour transformer le plan en un projet réel après avoir compris les besoins de votre client.

Par exemple, vous planifierez où vous lancerez le site, où vous le déployerez, et ainsi de suite.

#### Trouver les concepts pour le concept de projet réel

Dans cette phase, vous construisez les projets que le client souhaite. C'est également une étape extrêmement importante. 

Elle vous permet de concevoir le site web selon les souhaits du client.

#### Utiliser et supporter le projet

Nous sommes maintenant dans la phase de production. Pendant cette phase, le projet sera testé et tout problème technique sera résolu.

S'il y a des problèmes techniques, ils devraient être mineurs et ne devraient pas affecter négativement la majorité du site web. 

Cependant, une fois le projet remis au client, la maintenance devrait être gérée par le client.

#### Désactivation

Le site web sera désactivé dans cette dernière étape. 

Il est soit remplacé par un autre site, le client met fin à son entreprise et supprime le site, et ainsi de suite.

## Qu'est-ce que l'ingénierie système et pourquoi est-elle importante ?

Nous avons vu qu'un système est une combinaison de nombreuses « choses » qui fonctionnent ensemble comme un tout.

Nous avons également vu que les systèmes ont des cycles de vie.

L'acte de planifier ces cycles de vie avant de commencer le projet et pendant son exécution est appelé **ingénierie système**.

### Exemple technique d'ingénierie système

Imaginons que vous savez déjà ce que le client veut. 

Imaginez qu'il vous a demandé de concevoir un site de commerce électronique qui hébergera des milliers de photos de vendeurs. 

Le site a besoin d'un serveur central pour héberger et livrer de nombreuses images d'utilisateurs. Votre site, par exemple, peut présenter des images de produits qu'il vend. 

Vous devez créer un système efficace et facile à maintenir qui demande des images pour le site web en un temps court. 

Comment pouvez-vous y parvenir ? 

Difficile à répondre, n'est-ce pas ? Sans aucun doute, c'est un problème difficile.

Un problème qui nécessite la planification d'un système pour maximiser l'efficacité et être aussi facile que possible à maintenir.

Si vous voulez en savoir plus sur ce problème, vous pouvez consulter [cet article](https://www.aosabook.org/en/distsys.html).

Bien que ce soit un grand problème technique, il existe d'autres problèmes encore plus sérieux. 

Quelles sont les meilleures façons de gérer la croissance d'une grande bibliothèque open source, par exemple ?

Comment exactement son architecture sera-t-elle structurée, pour qu'elle soit efficace et facile à utiliser ? 

[Voici](https://www.aosabook.org/en/matplotlib.html) un aperçu de l'architecture d'une bibliothèque populaire en Python, [matplotlib](https://matplotlib.org/). 

Vous pouvez créer et gérer la structure du programme lorsque vous planifiez un système. 

Ainsi, le développeur n'aura pas à s'inquiéter des objectifs de fonctionnalité manquants, des défauts sérieux ou de dépenser beaucoup plus que prévu pour la production et la maintenance.

C'est pour cette raison que Google, Facebook, Amazon et bien d'autres ont des équipes dédiées d'ingénieurs système.

Grâce à l'ingénierie système, nous pouvons développer une sorte de "plan" qui atteint nos objectifs ou ceux de l'entreprise avec une quasi-perfection.

## Conclusion

Eh bien, maintenant vous comprenez :

* Ce qu'est un système
* Ce qu'est un cycle de vie de projet
* Ce qu'est l'ingénierie système et sa valeur dans tous les types de projets

Merci d'avoir lu !

## **Références**

1. J. Martin, _Systems Engineering Guidebook A Process for Developing Systems and Products_. Londres : CRC Press, pp. 5–6.
2. National Geographic Society, « Earth’s Systems », _National Geographic Society_, 29 oct. 2019. [https://www.nationalgeographic.org/article/earths-systems/](https://www.nationalgeographic.org/article/earths-systems/)
3. « The Architecture of Open Source Applications (Volume 2): Scalable Web Architecture and Distributed Systems », _www.aosabook.org_. [https://www.aosabook.org/en/distsys.html](https://www.aosabook.org/en/distsys.html)  
4. B. Douglass, dans _Real-time design patterns: Robust Scalable Architecture for real-time systems_, Boston : Addison-Wesley, 2003, pp. 96–97.