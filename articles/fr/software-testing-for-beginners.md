---
title: Tests Logiciels – Guide du Débutant
subtitle: ''
author: Mabel Obadoni
co_authors: []
series: null
date: '2022-03-07T23:14:46.000Z'
originalURL: https://freecodecamp.org/news/software-testing-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Talk2Her-Foundation--4-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
- name: user testing
  slug: user-testing
seo_title: Tests Logiciels – Guide du Débutant
seo_desc: "What is Software Testing?\nLet's say you're working on a coding project.\
  \ You have been writing a bunch of code and staying up late at night to fix bugs.\
  \ All this is part of the process before you release that software product. \nThen\
  \ you'll check your ..."
---

## Qu'est-ce que les Tests Logiciels ?

Disons que vous travaillez sur un projet de codage. Vous avez écrit beaucoup de code et passé des nuits blanches à corriger des bugs. Tout cela fait partie du processus avant de publier ce produit logiciel.

Ensuite, vous vérifierez votre code pour confirmer qu'il effectue réellement ce pour quoi il a été programmé. C'est là que les tests logiciels interviennent.

Cet article discutera des catégories de Tests Logiciels et des différents types de tests que les développeurs utilisent le plus couramment. Vous verrez que certains des tests sont nommés selon leur fonction. Ainsi, lorsque je dis test API, je fais référence aux tests effectués sur les APIs consommées dans votre code source.

Mais avant d'aller plus loin, assurons-nous de savoir ce que nous entendons par Tests Logiciels.

En termes simples, les Tests Logiciels sont le processus de vérification des différents aspects d'un produit logiciel pour valider les spécifications du logiciel et s'assurer qu'il est prêt à être utilisé.

## Objectifs des Tests Logiciels

D'une simple ligne de code à un bloc de code, et même au produit fini, vous testez le logiciel pour :

* vérifier les défauts et vous assurer que le produit fonctionne comme spécifié
* vous assurer que le produit répond aux normes du marché
* résoudre toute faille au stade de la production
* prévenir les futurs dysfonctionnements du produit

## Caractéristiques des Tests Logiciels

Lorsque vous testez votre logiciel, vous voulez vous assurer que vos tests sont :

* Pratiques
* Fiables
* Authentiques
* Capables de trouver des erreurs
* Capables de vérifier la validité de votre logiciel

## Quand Devez-Vous Tester Votre Logiciel ?

Quand vous testez votre logiciel dépendra du test que vous souhaitez effectuer.

Vous pouvez tester votre logiciel pendant la phase de développement logiciel – c'est-à-dire, lors de l'écriture du code source, comme dans le cas des tests unitaires, des tests API, et autres.

Vous pouvez également tester après que le logiciel a été développé, comme dans les Tests d'Interface Utilisateur (UI).

## Quand Arrêter les Tests ?

Vous pouvez arrêter de tester votre logiciel lorsque :

* Tous les tests nécessaires ont été effectués efficacement
* Les bugs dans les codes sources ont été réduits au minimum ou éradiqués
* Les testeurs ont terminé les tests
* Le produit est entièrement sécurisé contre les menaces
* Le produit est publié

## **Méthodes de Tests Logiciels**

Maintenant que vous savez ce que signifie les Tests Logiciels, comment sont-ils effectués exactement ?

Les Tests Logiciels sont effectués sur la base de deux méthodes principales :

1. Tests Fonctionnels
2. Tests Non Fonctionnels

La principale différence entre ces catégories de Tests Logiciels est que les Tests Fonctionnels testent la fonctionnalité d'un produit logiciel tandis que les tests non fonctionnels se concentrent sur la performance du produit logiciel.

### **Tests Fonctionnels**

Les tests fonctionnels sont le processus de test du logiciel pour valider son utilité par rapport à ses spécifications.

En termes simples, il consiste en divers tests effectués sur le logiciel généralement pour vérifier ses fonctionnalités.

Les tests fonctionnels aident l'équipe logicielle à savoir si le logiciel fonctionne comme requis. Notez bien, les Tests Fonctionnels ne signifient pas tester les fonctions unitaires ou les modules.

### Exemples de Tests Fonctionnels

#### Tests Unitaires

Dans les tests unitaires, vous testez des unités ou fonctions individuelles du code source de votre logiciel. Les tests unitaires peuvent être effectués automatiquement ou manuellement.

Les tests unitaires automatiques se font avec l'assistance humaine tandis que les tests unitaires manuels sont activement effectués par des humains.

La différence entre ces deux méthodes est que la première est automatisée tandis que la seconde nécessite un codage manuel.

Le but des tests unitaires est de s'assurer que chaque composant unitaire fonctionne comme prévu.

#### Tests API

Une Interface de Programmation d'Application (ou API) est un lien entre votre programme et une source externe. Donc, si vous voulez que votre programme fasse plus que ce que vous codez, vous pourriez utiliser les fonctionnalités d'un autre programme également. C'est tout l'intérêt de la consommation d'APIs.

Par exemple, disons que je veux que mon application ait une fonctionnalité de carte. Au lieu d'en coder une à partir de zéro, je pourrais me sauver du temps et du stress en utilisant l'une des APIs de carte disponibles.

L'utilisation d'APIs, surtout à partir de sources externes, comporte ses avantages et ses inconvénients, cependant. Et je parie que vous voulez réduire les inconvénients autant que possible. Eh bien, c'est pourquoi vous devez tester l'API avant la publication du produit.

Lorsque vous consommez une API publique ou privée, pendant le développement de votre logiciel, vous devez vérifier la fiabilité, la sécurité et l'efficacité de l'API dans votre produit avant la publication.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/API.png)
_Image représentant une API_

#### Tests UI (Interface Utilisateur)

L'Interface Utilisateur est le canal de communication entre l'utilisateur et le logiciel.

Chaque produit logiciel est développé avec certaines spécifications pour l'Interface Utilisateur. Cela signifie que la manière dont l'utilisateur interagit avec l'application est prédéterminée avant le développement du produit.

Afin de s'assurer que ces spécifications sont respectées selon la conception, vous pouvez effectuer des tests sur l'UI – et cela est connu sous le nom de Tests UI.

Les Tests UI impliquent des choses comme vérifier si la page d'inscription accepte correctement les entrées, vérifier si le bouton de soumission est fonctionnel, et une série d'autres fonctionnalités UI.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Signup-page3--1-.png)
_Image d'une Page de Paiement_

#### Tests d'Intégration

Mettre des composants en groupes pour les tester est connu sous le nom de tests d'intégration. Les tests d'intégration impliquent de vérifier comment chaque composant séparé fonctionne ensemble pour atteindre l'objectif commun du produit.

Par exemple, dans une application de commerce électronique, les tests d'intégration peuvent vérifier comment la page d'accueil se connecte à la page des Paniers lorsque le menu Panier est cliqué.

Le but des tests d'intégration est de s'assurer que les composants fonctionnent en synchronie – c'est-à-dire, que le composant A fonctionne bien avec le composant B.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/LOGIN_SIGNUP-PAGE.png)
_Image de deux pages UI_

#### Tests de Régression

Le Développement Logiciel implique l'itération, qui se produit souvent à cause de bugs dans le code source.

Après avoir débogué votre code, mis à jour le programme logiciel, ou apporté toute autre modification à votre code, vous devez tester ce logiciel pour valider sa fonctionnalité. Ce test est appelé test de régression.

Des exemples de tests de régression sont les tests de régression correctifs, les tests de régression sélectifs, les tests de régression progressifs, et autres.

### **Tests Non Fonctionnels ou de Performance**

Les tests non fonctionnels font référence aux divers tests effectués sur un produit pour vérifier sa préparation pour le marché. Les Tests Non Fonctionnels vont plus loin pour assurer la viabilité d'un produit et sa valeur.

### Exemples de Tests Non Fonctionnels

#### Tests de Volume

La force de chaque produit réside dans sa capacité à gérer différents volumes de données. Certains logiciels peuvent ne pas fonctionner avec une grande base de données. Pour éviter une telle rupture, vous pouvez effectuer des tests de volume.

Le test de volume implique de fournir une grande base de données au logiciel pour vérifier sa fonctionnalité en fonction du grand volume de données. Tester votre produit sur différents volumes de données montre que votre produit peut résister à plus ou moins de données à un moment donné.

#### Tests de Sécurité

Dans le monde d'aujourd'hui, la sécurité est un sujet important et beaucoup discuté. Les préoccupations vont de la sécurité physique à l'espace cybernétique – et tout le monde veut cette assurance de sécurité lorsqu'ils sont sur Internet.

L'un des problèmes que vous voudrez éviter en tant que développeur de logiciels est les menaces pour votre application. Vous pouvez effectuer des tests de sécurité sur votre produit logiciel pour vérifier son niveau de vulnérabilité.

Les tests de sécurité incluent l'authentification, l'autorisation, la confidentialité, et d'autres mesures requises pour protéger votre logiciel contre les risques et les menaces.

## Où placer les fichiers de test dans un dossier de programme

Vos fichiers de test doivent être ensemble dans un dossier de test à l'intérieur du dossier racine de votre projet. Cela est pour une navigation et une intégration faciles dans votre projet.

## **Conclusion**

Maintenant que vous connaissez l'importance des tests dans le développement logiciel, vous devez vous assurer d'écrire un code qui est exempt d'erreurs et de bugs lorsqu'il est testé.

Cela réduira le temps que vous perdez à corriger des bugs et rendra la date de publication du produit plus réalisable.

Enfin, faites attention à placer vos fichiers de test dans le même dossier, surtout pour les tests autres que les tests unitaires.