---
title: Comment auditer l'accessibilité Android avec l'application Accessibility Scanner
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2025-06-30T18:02:46.693Z'
originalURL: https://freecodecamp.org/news/how-to-audit-android-accessibility-with-the-accessibility-scanner-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751301060182/df4d483a-8dd6-45ce-a665-76cbf45ef945.png
tags:
- name: Android
  slug: android
- name: Accessibility
  slug: accessibility
- name: Mobile app accessibility testing
  slug: mobile-app-accessibility-testing
seo_title: Comment auditer l'accessibilité Android avec l'application Accessibility
  Scanner
seo_desc: The Web Content Accessibility Guidelines (WCAG 2.1 Level AA) is an internationally
  recognized standard for digital accessibility. Meeting these guidelines helps you
  make sure that your website is usable by people with visual, motor, hearing, and
  cogn...
---

Les Web Content Accessibility Guidelines (WCAG 2.1 Niveau AA) sont une norme internationale reconnue pour l'accessibilité numérique. Respecter ces directives vous aide à vous assurer que votre site web est utilisable par les personnes atteintes de déficiences visuelles, motrices, auditives et cognitives.

L'application [Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor&hl=fr_FR) de Google sur Google Play est une application gratuite qui offre aux développeurs, designers et responsables produits la possibilité d'auditer leur application pour trouver des problèmes d'accessibilité. L'application est conçue pour mettre en évidence les problèmes d'accessibilité qui pourraient ne pas respecter les normes WCAG 2.1 Niveau AA.

Une fois installée, l'application Accessibility Scanner vous permet de prendre des captures d'écran ou des enregistrements vidéo de votre application, puis met en évidence les zones qui pourraient ne pas respecter les exigences d'accessibilité, comme les petites cibles tactiles, le faible contraste des couleurs ou les étiquettes de contenu manquantes.

### Voici ce que nous allons couvrir :

1. [Comment télécharger et activer l'Accessibility Scanner](#heading-comment-télécharger-et-activer-laccessibility-scanner)
    
2. [Comment utiliser l'Accessibility Scanner](#heading-comment-utiliser-laccessibility-scanner)
    
    * [Comment utiliser la fonction Snapshot](#heading-comment-utiliser-la-fonction-snapshot)
        
    * [Comment utiliser la fonction Record](#heading-comment-utiliser-la-fonction-record)
        
3. [Pourquoi utiliser l'Accessibility Scanner ?](#heading-pourquoi-utiliser-laccessibility-scanner)
    

## **Comment télécharger et activer l'Accessibility Scanner**

En cinq étapes rapides, vous pouvez télécharger l'application Accessibility Scanner et l'activer sur votre appareil Android.

1. Recherchez "Accessibility Scanner" sur Google Play Store et téléchargez-le.
    
2. Trouvez l'application téléchargée sur votre appareil et ouvrez-la.
    
3. Activez l'Accessibility Scanner en cliquant sur le bouton "Turn on" en bas à droite de la page. Cela vous mènera à vos paramètres d'accessibilité.
    
4. Dans la page des paramètres d'accessibilité, cliquez sur le bouton Accessibility Scanner. Cela vous mènera aux paramètres de l'Accessibility Scanner.
    
5. Trouvez le bouton bascule de l'Accessibility Scanner et activez-le. (Cela ouvrira une fenêtre modale qui demande si vous autorisez "Accessibility Scanner" à avoir le contrôle total de votre appareil, cliquez sur Autoriser.
    

Après l'étape cinq, une icône de coche bleue apparaîtra sur le côté droit de votre écran (voir l'image ci-dessous). Cette icône flottante vous donne un accès rapide pour commencer à analyser n'importe quel écran à la recherche de problèmes d'accessibilité.

![Page de connexion Facebook avec l'icône de bascule de l'Accessibility Scanner à droite avec une flèche pointant vers elle](https://cdn.hashnode.com/res/hashnode/image/upload/v1750821547116/75f49863-7f19-4db5-ada1-45483c0df70b.png align="center")

## **Comment utiliser l'Accessibility Scanner**

Pour analyser ou enregistrer votre application afin de trouver des problèmes d'accessibilité, appuyez sur l'icône de coche bleue. Vous verrez quelques options après avoir cliqué sur la coche bleue :

* **Record** : Capture une courte vidéo de l'interaction de l'utilisateur et génère un rapport des problèmes d'accessibilité potentiels.
    
* **Snapshot** : Prend une capture d'écran statique et signale les problèmes trouvés sur cet écran.
    
* **Turn off** : Désactive l'Accessibility Scanner.
    
* **Collapse** : Réduit les options pour afficher la coche bleue initiale.
    

![Page de connexion Facebook avec l'icône de bascule de l'Accessibility Scanner ouverte à droite avec une flèche pointant vers elle](https://cdn.hashnode.com/res/hashnode/image/upload/v1750895121001/9673c7d5-5182-4c99-b36a-1b2a2e27986b.png align="center")

Vous pouvez choisir entre prendre un seul **Snapshot** ou enregistrer le flux utilisateur en utilisant **Record** pour évaluer plusieurs écrans.

### Comment utiliser la fonction Snapshot

Le bouton Snapshot prendra une capture de la page sur laquelle vous vous trouvez et vous donnera un résultat des problèmes d'accessibilité qui peuvent se trouver sur la page. Les problèmes d'accessibilité seront mis en évidence dans des boîtes rouges.

L'image ci-dessous est le résultat de la prise d'une capture de la page de connexion Facebook. L'Accessibility Scanner indique qu'il y a 10 suggestions d'accessibilité sur cette page seule.

![Page de connexion Facebook avec des boîtes rouges autour de plusieurs éléments, mettant en évidence les problèmes d'accessibilité.](https://cdn.hashnode.com/res/hashnode/image/upload/v1750898582440/76cc763c-e6db-46a9-b062-2e29a57e7022.jpeg align="center")

Vous pouvez cliquer sur la zone mise en évidence afin d'obtenir plus de détails sur le problème d'accessibilité potentiel. Par exemple, vous pouvez cliquer sur la boîte rouge qui met en évidence le formulaire "Numéro de mobile ou email" qui se trouve dans l'image ci-dessus. Une fois que vous cliquez sur la zone mise en évidence, vous obtiendrez des informations supplémentaires.

L'image ci-dessous est le résultat du clic sur l'élément de formulaire "Numéro de mobile ou email". L'Accessibility Scanner met en évidence les erreurs qu'il a trouvées sur ce formulaire d'email.

La première suggestion qu'il donne est de corriger l'étiquette de l'élément, car l'élément peut ne pas avoir d'étiquette lisible par les lecteurs d'écran. Le deuxième problème qu'il met en évidence est la cible tactile et suggère que la cible devrait être plus grande. La dernière suggestion est le texte non exposé, texte possible détecté : Numéro de mobile ou email.

Les snapshots nous permettent de prendre des captures d'écran de nos pages et de mettre en évidence les problèmes d'accessibilité.

![Champ de formulaire d'email sélectionné par l'Accessibility Scanner. Le scanner montre trois zones à corriger.](https://cdn.hashnode.com/res/hashnode/image/upload/v1750898563142/ce93909e-b351-405c-8367-dd47d7d19c9f.jpeg align="center")

### Comment utiliser la fonction Record

Si vous choisissez d'enregistrer, l'Accessibility Scanner prendra des captures à intervalles réguliers lorsque vous parcourrez les pages de votre application. Pour mettre fin à l'enregistrement, appuyez sur le bouton de pause bleu (qui remplace la coche originale pendant l'enregistrement).

Une fois que vous arrêtez l'enregistrement, l'Accessibility Scanner vous donnera plusieurs captures et erreurs mises en évidence. L'image ci-dessous est le résultat de l'enregistrement de la page de connexion Facebook en moins d'une minute.

Pendant l'enregistrement, j'ai navigué vers d'autres pages de l'application. L'enregistrement a donné 5 captures des pages que je parcourais. Vous pouvez voir les captures en haut de la page. Dans l'image ci-dessous, je suis sur l'écran un sur cinq. Je peux cliquer sur les autres captures sous les mots "Écran 1 sur 5" et voir les problèmes pour différentes captures prises pendant mon enregistrement. Similaire à l'audit d'accessibilité par snapshot, vous pouvez cliquer sur les boîtes rouges et obtenir plus d'informations sur les erreurs.

![Page de connexion Facebook avec l'Accessibility Scanner mettant en évidence des éléments avec des problèmes d'accessibilité.](https://cdn.hashnode.com/res/hashnode/image/upload/v1750898542344/a390f512-262d-40c1-87ad-35e36c31def4.jpeg align="center")

## **Pourquoi utiliser l'Accessibility Scanner ?**

L'Accessibility Scanner est un outil précieux pour les équipes tout au long du cycle de vie du développement d'applications. Les ingénieurs peuvent l'utiliser tôt dans le processus pour analyser l'application localement, identifier les problèmes d'accessibilité et les résoudre avant la publication. Pendant la phase de QA, les designers et les chefs de produit peuvent utiliser le scanner pour auditer les interfaces utilisateur et signaler les problèmes d'accessibilité potentiels. Même après qu'une application soit en production, toutes les équipes peuvent continuer à utiliser le scanner pour surveiller et améliorer l'accessibilité.

Mais il est important de noter que l'Accessibility Scanner n'est qu'une partie d'une stratégie d'accessibilité - ce n'est pas un remplacement complet pour les tests manuels ou les audits. Et il ne détectera pas tous les types de barrières d'accessibilité - surtout celles qui nécessitent une navigation au clavier, des tests avec des lecteurs d'écran ou des revues d'utilisabilité cognitive. Mais c'est un point de départ simple et efficace pour améliorer l'accessibilité dans les applications Android.

Vous devriez l'utiliser en parallèle avec d'autres outils, tels que TalkBack d'Android pour les tests avec lecteurs d'écran. Plus important encore, les retours du monde réel des personnes qui utilisent des technologies d'assistance sont essentiels pour identifier les barrières d'utilisabilité que les outils automatisés peuvent manquer.

Avec seulement quelques clics, l'Accessibility Scanner aide à mettre en évidence les problèmes qui pourraient autrement être manqués. C'est un outil gratuit, léger et essentiel pour quiconque construit des expériences mobiles inclusives.

## Merci d'avoir lu !

Vous devriez maintenant savoir comment commencer à utiliser l'Accessibility Scanner pour vérifier l'accessibilité de vos applications et vous assurer qu'elles sont utilisables par tout le monde.