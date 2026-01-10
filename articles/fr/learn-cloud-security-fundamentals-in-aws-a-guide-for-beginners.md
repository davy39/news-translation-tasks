---
title: Apprendre les fondamentaux de la sécurité cloud dans AWS – Un guide pour débutants
author: Ijeoma Igboagu
date: '2025-12-09T00:58:17.967Z'
originalURL: https://freecodecamp.org/news/learn-cloud-security-fundamentals-in-aws-a-guide-for-beginners
description: La sécurité est un élément vital de tout système et de toute infrastructure.
  Le mot « sécurité » vient du latin securitas, composé de se- (signifiant « sans
  ») et cura (signifiant « soin » ou « souci »). À l'origine, cela signifiait « sans
  souci ». Au fil du temps, il en est venu à signifier être en sécurité ou protégé.
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764958826138/12b261c3-9a38-4b0b-b67a-48ce54452d5f.png
tags:
- name: AWS
  slug: aws
- name: cloud security
  slug: cloud-security
- name: '#sharedresponsibilitymodel'
  slug: sharedresponsibilitymodel
- name: Cloud Computing
  slug: cloud-computing
- name: BeginnerFriendly
  slug: beginnerfriendly
seo_desc: Security is a vital part of every system and infrastructure. The word "security"
  comes from the Latin securitas, which is composed of se- (meaning “without”) and
  cura (meaning “care” or “worry”). Originally, it meant "without worry." Over time,
  it ha...
---


La sécurité est un élément vital de tout système et de toute infrastructure. Le mot « sécurité » vient du latin *securitas*, qui est composé de *se-* (signifiant « sans ») et *cura* (signifiant « soin » ou « souci »). À l'origine, cela signifiait « sans souci ». Au fil du temps, il en est venu à signifier être en sécurité ou protégé.

Aujourd'hui, lorsque nous parlons de sécurité, nous nous référons généralement à la protection contre les dommages, les dangers ou les menaces, que ce soit dans nos maisons, en ligne, lors de l'utilisation de services bancaires en ligne, ou même à l'échelle d'un pays entier. La sécurité est importante dans tout ce que nous faisons.

Les fournisseurs de cloud, tels qu'AWS, ne font pas exception. Leur infrastructure doit être protégée pour garantir la tranquillité d'esprit des utilisateurs. Mais sur des plateformes comme AWS, la sécurité est une **responsabilité partagée**. Cela signifie que le fournisseur et l'utilisateur jouent tous deux un rôle dans le maintien de la sécurité.

Amazon Web Services (AWS) est l'un des fournisseurs de services cloud les plus populaires au monde. Une grande puissance et une grande flexibilité s'accompagnent de la responsabilité de sécuriser votre infrastructure, vos données et vos applications dans le cloud.

Dans ce tutoriel, nous explorerons les aspects fondamentaux de la sécurité cloud dans AWS – en particulier ceux qui relèvent de votre responsabilité – afin de les rendre faciles à comprendre si vous débutez dans le cloud computing.

## Table des matières

1. [Qu'est-ce que la sécurité cloud ?](#heading-qu-est-ce-que-la-securite-cloud)
    
2. [Pourquoi la sécurité cloud est-elle importante ?](#heading-pourquoi-la-securite-cloud-est-elle-importante)
    
3. [Concepts clés de la sécurité cloud](#heading-concepts-cles-de-la-securite-cloud)
    
    * [Qu'est-ce qu'un utilisateur Root ?](#heading-qu-est-ce-qu-un-utilisateur-root)
        
    * [Comment créer un utilisateur IAM pour les tâches quotidiennes](#heading-comment-creer-un-utilisateur-iam-pour-les-taches-quotidiennes)
        
    * [Différences clés entre l'utilisateur Root et un utilisateur IAM](#heading-differences-cles-entre-l-utilisateur-root-et-un-utilisateur-iam)
        
    * [Qu'est-ce que le MFA ?](#heading-qu-est-ce-que-le-mfa)
        
4. [Comprendre le modèle de responsabilité partagée d'AWS](#heading-comprendre-le-modele-de-responsabilite-partagee-d-aws)
    
    * [RDS (Relational Database Service)](#heading-rds-relational-database-service)
        
    * [S3 (Simple Storage Service)](#heading-s3-simple-storage-service)
        
    * [Comment donner des permissions à un utilisateur](#heading-comment-donner-des-permissions-a-un-utilisateur)
        
    * [Tester la politique](#heading-tester-la-politique)
        
5. [Conclusion](#heading-conclusion)
    
    * [Lectures complémentaires](#heading-lectures-complementaires)
        

## Qu'est-ce que la sécurité cloud ?

La sécurité cloud est l'ensemble des règles, outils et pratiques utilisés pour protéger vos données, applications et services stockés en ligne (dans le « cloud »). Elle aide à prévenir la perte de données, le piratage et l'utilisation abusive des informations.

Pensez à la sécurité cloud comme au fait de verrouiller les portes de votre maison. Vous ne laisseriez pas vos portes ouvertes pour que n'importe qui puisse entrer. De la même manière, votre compte cloud doit être sécurisé afin que vos données restent en sécurité.

Si vos services cloud ne sont pas sécurisés, des pirates pourraient voler vos données ou causer des dommages majeurs. Que vous soyez une entreprise ou simplement un particulier utilisant des applications cloud, la protection de vos informations est essentielle.

## Pourquoi la sécurité cloud est-elle importante ?

La sécurité cloud est importante car elle garantit que seules les bonnes personnes ont accès à vos informations. Elle protège vos données contre la perte, le vol ou l'utilisation abusive. Avec une bonne sécurité en place, vos applications peuvent fonctionner en toute sécurité sans être exposées à des attaques.

Elle vous aide également à préserver la confidentialité de vos données personnelles ou professionnelles. Lorsque votre environnement cloud est bien protégé, le risque de violation de données et de perte financière est considérablement réduit.

Maintenant que vous comprenez pourquoi la sécurité cloud est importante, examinons comment AWS vous aide à rester en sécurité et quel est votre propre rôle dans cette protection.

## Concepts clés de la sécurité cloud

Dans AWS, la sécurité cloud est la responsabilité d'AWS **et** du client. Ce modèle est appelé le Modèle de Responsabilité Partagée.

Mais avant d'apprendre comment AWS répartit les tâches de sécurité, vous devez comprendre que si AWS protège son infrastructure, vous devez protéger votre propre compte.

Discutons de certains concepts clés de sécurité qui relèvent de votre responsabilité, afin que vous sachiez comment jouer votre rôle dans le modèle de responsabilité partagée.

### Qu'est-ce qu'un utilisateur Root ?

Lorsque vous créez un compte AWS, la première identité créée est le compte utilisateur **Root**. Ce compte dispose d'un contrôle total et sans restriction. Il peut supprimer des ressources, changer de propriétaire et même fermer l'intégralité de votre compte AWS. Pour cette raison, il est risqué de l'utiliser pour les tâches quotidiennes.

AWS recommande d'utiliser le compte root uniquement pour quelques actions importantes au niveau du compte.

Certaines tâches nécessitent un compte utilisateur root, vous devrez donc l'utiliser occasionnellement. Ces tâches incluent :

* La mise à jour des informations de facturation et de paiement
    
* La fermeture de votre compte AWS
    
* Le changement de l'adresse e-mail du compte root
    
* La récupération ou la réinitialisation du MFA pour l'utilisateur root
    

En dehors de ces quelques tâches, évitez complètement d'utiliser le compte utilisateur root. Votre travail quotidien doit être effectué via des utilisateurs IAM, et non via le compte root.

### Comment créer un utilisateur IAM pour les tâches quotidiennes

Avant de commencer à créer une infrastructure dans votre compte AWS, vous avez besoin d'un utilisateur IAM avec les bonnes permissions.

Voici comment créer un utilisateur IAM, étape par étape :

* Ouvrez la console AWS.
    
* Recherchez **IAM**, puis sélectionnez-le. Cela vous amène à la **page IAM**.
    
* Sur le côté gauche, vous verrez **Users**.
    
* Cliquez dessus. Cela vous amène à la page **Create user**.
    
* Cliquez sur le bouton **Create user**. Cela vous amène à la page « specify user details » où vous créerez un **utilisateur IAM.**
    
* Entrez un nom d'utilisateur (par exemple, `adminuser`).
    
* Cliquez sur « Provide user access to the AWS Management Console ».
    

![fournir un accès utilisateur à la console AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1764236205525/47c2da54-537f-4242-9048-ced4b7ca6172.png align="center")

4. Faites défiler vers le bas et cliquez sur « Set a password », ou laissez AWS en générer un pour vous.
    
5. Cliquez sur **Next** pour accéder à la page des permissions.
    
6. Sélectionnez **Attach existing policies directly**.
    
7. Choisissez `AdministratorAccess`. Cette permission donne à l'utilisateur IAM un accès complet pour effectuer toutes les tâches administratives dans votre compte.
    
8. Cliquez sur **Create user**.
    

Une fois cet utilisateur créé, connectez-vous avec celui-ci et utilisez-le pour vos tâches quotidiennes. L'utilisateur root doit rester verrouillé et n'être utilisé que pour de rares modifications au niveau du compte.

#### Démonstration vidéo de la création d'un utilisateur IAM :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1764235482269/bf5b1f00-13b2-4ff5-b1e4-e6b2fd2796cb.gif align="center")

### Différences clés entre l'utilisateur Root et un utilisateur IAM

Pour être clair, résumons les différences entre ces deux comptes :

#### Compte Root

C'est le tout premier compte créé lors de la configuration d'AWS. Il a un pouvoir illimité – littéralement, tout dans le compte peut être modifié, supprimé ou fermé.

Il est destiné à des tâches rares et de haut niveau comme les changements de facturation, les réinitialisations de MFA ou la fermeture du compte. Parce qu'il est si puissant, vous ne devriez pas l'utiliser pour le travail quotidien.

#### Compte utilisateur IAM

C'est un utilisateur que vous créez à l'intérieur de votre compte AWS pour les tâches quotidiennes. Vous pouvez attribuer des permissions spécifiques, comme un accès administrateur ou limité, à cet utilisateur. C'est beaucoup plus sûr car vous pouvez contrôler ce qu'il peut et ne peut pas faire.

Si quelque chose tourne mal ou si les identifiants sont compromis, le rayon d'impact est beaucoup plus restreint que pour l'utilisateur root.

En résumé, le Root est la clé maîtresse, trop puissante pour un usage quotidien. Les utilisateurs IAM sont personnalisables et plus sûrs pour votre travail régulier.

Voici un visuel utile pour montrer également les différences entre les deux :

![différences entre les deux comptes](https://cdn.hashnode.com/res/hashnode/image/upload/v1764248147852/7e053766-f6ba-4a17-9b63-c20695f2933c.jpeg align="center")

Maintenant que vous avez configuré correctement votre utilisateur root et votre utilisateur IAM, revenons au concept de l'authentification multi-facteurs, ou MFA.

### Qu'est-ce que le MFA ?

Le MFA ajoute une couche de sécurité supplémentaire lors de votre connexion. Il combine quelque chose que vous connaissez, comme votre mot de passe, avec quelque chose que vous possédez, comme un téléphone ou un appareil de sécurité. Même si quelqu'un obtient votre mot de passe, il ne pourra pas se connecter sans votre code MFA.

Vous pouvez activer le MFA de plusieurs manières :

* En utilisant une application MFA virtuelle comme Google Authenticator ou Authy
    
* En utilisant une clé de sécurité physique telle qu'une