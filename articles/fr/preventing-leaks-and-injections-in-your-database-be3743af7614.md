---
title: Comment prévenir les fuites et les injections de base de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-01T15:35:10.000Z'
originalURL: https://freecodecamp.org/news/preventing-leaks-and-injections-in-your-database-be3743af7614
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pxW6AFbOoapYpcO4qr_ikQ.jpeg
tags:
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment prévenir les fuites et les injections de base de données
seo_desc: 'By Cossack Labs Dev Stories

  Most web and mobile apps have a backend that includes a database of some kind. Your
  front end consumes data from your back end, and also gathers new data to feed back
  into your database.

  Often hackers will target your data...'
---

Par Cossack Labs Dev Stories

La plupart des applications web et mobiles ont un backend qui inclut une base de données d'un type ou d'un autre. Votre frontend consomme des données de votre backend et collecte également de nouvelles données à réinjecter dans votre base de données.

Souvent, les pirates cibleront votre base de données pour des attaques malveillantes, essayant de voler ou de modifier des informations sensibles. Mais la plupart des backends sont assez bien protégés, et le seul vecteur d'attaque disponible pour des actions malveillantes est à travers votre frontend lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/BSMBLVpI4-zg7BBiojecfZUdWPiqzdU-ThI6)
_Votre layout d'application moderne, propre et simple_

Il existe de nombreuses techniques traditionnelles pour protéger vos données. La plupart d'entre elles nuiront à vos performances et limiteront également la portée de la protection de vos données en même temps.

Cet article parle de quelque chose d'autre — plusieurs techniques intéressantes que nous utilisons pour détecter les intrus dans [Acra](https://www.cossacklabs.com/acra/), notre suite de protection de base de données open-source.

### Frontend sous attaque !

Peu importe quels types d'authentification et de chiffrement se trouvent entre votre frontend et le reste de votre système, vous devez faire confiance à votre frontend pour lui permettre de transmettre les données. Toute requête que votre frontend envoie avec les paramètres d'authentification corrects, votre base de données doit la servir.

Mais que se passe-t-il si votre application frontend est exposée de manière à ce qu'un attaquant puisse modifier l'exécution ou le flux de demande de données ?

![Image](https://cdn-media-1.freecodecamp.org/images/TK2HFw3HHtNhZhyeMt40bYaN-ZfgfOiF-EgJ)
_Et si vous oubliez de filtrer les guillemets ?_

Si vous faites confiance à votre application et à ses identifiants, vous servirez toutes ses requêtes, peu importe à quel point elles sont malveillantes.

#### Présentons un Watchdog

![Image](https://cdn-media-1.freecodecamp.org/images/RPXZ25FiPppNgmfPdm8cEZeOxsjUtb5kVW4C)
_Désormais, tout le trafic passe par le nœud Watchdog_

Watchdog est un serveur proxy réseau qui se situe entre votre application et votre base de données, et contrôle votre flux de données. Si l'infrastructure derrière l'application n'a pas été compromise et que seul le frontend est sous attaque, la seule façon pour les attaquants d'obtenir les données qu'ils recherchent est d'envoyer des requêtes malformées via ce Watchdog.

Mais en plus de simplement faire respecter la politique d'accès, il peut filtrer les requêtes correctes et refuser l'accès pour celles qui sont clairement malveillantes.

Alors, que fait un tel proxy Watchdog ? Il essaie de détecter les anomalies et toutes les sélections à grande échelle qui ne sont pas typiques pour un flux d'application. Ensuite, en fonction du niveau de menace, il ferme soit l'accès à la base de données, soit génère des événements de notification pour la surveillance.

Vous aimez l'idée ? [Acra](https://www.cossacklabs.com/acra/) est un tel watchdog, fournissant en outre des services cryptographiques, axés sur la protection sélective et flexible uniquement des parties sensibles des données que vous stockez.

#### Quels types de mauvaises requêtes devons-nous détecter ?

Charges utiles typiques pour les injections SQL :

* Insertions, ciblant les données d'authentification
* SELECT *
* Exécution de commandes
* Octroi de droits
* Attaques par déni de service
* Signatures typiques de charges utiles d'échappement pour l'exécution côté base de données

### Méthodes de détection

La détection semble simple — nous devons simplement examiner le trafic qui passe par Watchdog et le faire correspondre à une règle. Mais les injections SQL ne sont pas toujours des tableaux binaires simples de bytes avec des signatures prédéterminées, faciles à repérer. Il existe différentes méthodes que vous pouvez utiliser pour scanner efficacement le trafic des requêtes de la base de données :

#### **Modèles de requêtes**

Une méthode simple et flexible pour détecter les comportements suspects consiste à faire correspondre les requêtes SQL à une liste de motifs. Cela demande un certain effort pour créer une telle liste couvrant la plupart des vecteurs d'attaque typiques pour votre flux de données particulier. Ensuite, vous devez faire correspondre les requêtes à cette liste. Mais c'est un moyen efficace de repérer la plupart des tentatives non sophistiquées à grande échelle, et tôt.

#### **Enregistrements empoisonnés**

Un design classique utilisé pour prévenir les injections de type `SELECT *`, l'enregistrement empoisonné est un moyen de détecter les requêtes massives à la base de données. Concevoir vos requêtes de base de données vous-même — ou au moins énumérer celles que votre ORM génère — vous permet de comprendre quelles tables avec des données sensibles ne sont jamais accessibles via des requêtes avec des requêtes de scan complet. Vous pouvez stocker un enregistrement spécial, une balise, dans cette table, qui, en passant par le Watchdog, déclenche l'alarme.

#### **Énumération des requêtes**

> — Essayons d'injecter de cette manière...
> — Hmm, non, ça ne marche pas
> — Et cette manière d'échapper les guillemets magiques ?

La plupart des processus de recherche et d'exploitation de bugs reposent sur le cycle essayer-échec-réessayer, dans lequel l'attaquant génère beaucoup de requêtes cassées. Certaines d'entre elles contiendront des signatures typiques, mais globalement elles augmenteront le nombre de mauvaises requêtes à votre base de données.

Alors que la détection de ces signatures est difficile, détecter une augmentation soudaine des réponses vides/erreur de syntaxe de la base de données est assez facile.

L'un des défis intéressants que nous poursuivons actuellement est d'être capable de détecter un comportement anormal (comparé au flux de requêtes régulier) via un classificateur entraîné par machine learning.

#### Que se passe-t-il si un **attaquant monte une attaque indistinguishable du comportement normal de l'application** ?

Si l'attaquant est capable de reverse engineer le flux de données régulier et de l'émuler de manière à ce que vous ne puissiez pas le distinguer du comportement normal de l'application, il sera capable de passer votre watchdog.

### Lectures complémentaires

Je recommande de lire ces trois articles sur les modèles classiques et modernes de défense des bases de données :

[**Cossack Labs / Classic backend security design patterns**](https://www.cossacklabs.com/classic-backend-security-designs.html)
[_Dans les applications client-serveur modernes, la plupart des données sensibles sont stockées et (par conséquent) fuient sur le...www.cossacklabs.com_](https://www.cossacklabs.com/classic-backend-security-designs.html)
[**Cossack Labs / Key management for modern application security 101**](https://www.cossacklabs.com/key-management-101.html)
[_Souvent négligé, beaucoup moins médiatisé que les ordinateurs quantiques brisant les fonctions à trappe, la gestion des clés est en fait...www.cossacklabs.com_](https://www.cossacklabs.com/key-management-101.html)
[**Cossack Labs / 12 and 1 ideas how to enhance backend data security**](https://www.cossacklabs.com/backend-data-security-modern-ideas.html)
[_Précédemment, nous avons parlé des modèles de conception classiques en matière de sécurité des données backend, puis des objectifs de gestion des clés et...www.cossacklabs.com_](https://www.cossacklabs.com/backend-data-security-modern-ideas.html)

Merci d'avoir lu.