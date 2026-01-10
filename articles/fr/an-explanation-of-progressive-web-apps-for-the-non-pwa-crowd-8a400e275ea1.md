---
title: Une explication des Progressive Web Apps pour les non-initiés aux PWA
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-05-13T16:02:17.000Z'
originalURL: https://freecodecamp.org/news/an-explanation-of-progressive-web-apps-for-the-non-pwa-crowd-8a400e275ea1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*bFT4XZ6spjmElUly
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: PWA
  slug: pwa
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une explication des Progressive Web Apps pour les non-initiés aux PWA
seo_desc: The world of applications was classified into two categories not too long
  ago. You were either creating an application for Android devices or for iOS. Enter
  PWAs, or elongated, Progressive Web Applications. You have probably been hearing
  all about th...
---

Le monde des applications était classé en deux catégories il n'y a pas si longtemps. Vous créiez soit une application pour les appareils Android, soit pour iOS. Voici les PWAs, ou en long, **P**rogressive **W**eb **A**pplications. Vous en avez probablement entendu parler depuis quelques années, mais en dehors d'un bel acronyme, vous ne savez pas ce qu'est une PWA. Alors que leur popularité augmente, il pourrait être bon de comprendre de quoi il s'agit.

Dans cet article, je vais vous emmener dans un tour de ce qu'est une PWA, de quels composants elle est construite, et je vais vous montrer comment vous pouvez en créer une vous-même.

#### Les bases

Une application web progressive est un site web transformé en application. Cela signifie que, au lieu de devoir coder en Java ou en Objective-C (ou dans des langages de codage mobile plus récents), vous pouvez écrire le code de l'application comme vous le feriez pour un site web. Vous avez vos fichiers html, vos feuilles de style et vos scripts.

Pourquoi créer une PWA plutôt qu'une application native ? Pour commencer, imaginez que, une fois que vous publiez une PWA, vous pouvez la modifier constamment sans avoir à republier votre application. Puisque tout le code est hébergé sur un serveur et ne fait pas partie de l'APK/IPA, toute modification que vous apportez se fait en temps réel.

Si vous avez déjà utilisé une application qui dépend d'une connexion réseau, vous connaissez la frustration de ne pas pouvoir faire quoi que ce soit. Avec les PWAs, vous avez la possibilité d'offrir une expérience hors ligne à vos utilisateurs en cas de problèmes de réseau.

Et pour ajouter la cerise sur le gâteau, il est possible de demander à l'utilisateur d'ajouter votre PWA à son écran d'accueil. Une fonctionnalité que les applications natives ne possèdent pas.

#### Composants

Il existe une norme concernant les PWA, et vous devez vous y conformer si vous souhaitez en publier une. Chaque PWA est construite à partir des composants suivants :

* Un manifeste d'application web
* Un service worker
* Expérience d'installation
* HTTPS
* Création d'un APK
* Audit Lighthouse

#### Le manifeste

Il s'agit purement d'un fichier de configuration (**_.JSON_**), qui vous permet de modifier divers paramètres de votre PWA et la manière dont elle apparaîtra à l'utilisateur. Voici un exemple :

Vous devez définir soit une clé de nom/nom court. Lorsque vous définissez les deux, le nom court sera utilisé sur l'écran d'accueil et le lanceur. La valeur du nom sera utilisée dans l'expérience "Ajouter à l'écran d'accueil" (ou invite d'installation de l'application).

L'affichage peut avoir quatre valeurs différentes :

* **fullscreen** - cela permet à votre application de prendre tout l'écran lorsqu'elle est ouverte
* **standalone** - votre application ressemble à une application native, masquant les éléments du navigateur
* **minimal-ui** - fournit certains contrôles de navigation (uniquement pris en charge pour Chrome mobile)
* **browser** - comme son nom l'indique, l'apparence de votre application sera identique à une expérience de navigation

Vous pouvez également définir l'**orientation** de votre application et la **portée** des pages considérées comme faisant partie de votre application.

N'oubliez pas d'ajouter le manifeste à votre fichier html principal en plaçant la balise meta suivante à l'intérieur de votre balise head :

![Image](https://cdn-media-1.freecodecamp.org/images/-sgj8knyKimbaSIeLGhmo5oflTKZzHunce4V)
_Photo par [Unsplash](https://unsplash.com/@solimonster?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">sol</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Le Service Worker

Un service worker est un composant qui s'exécute en arrière-plan de votre site web sur le navigateur. Il dispose d'un large éventail de fonctionnalités, notamment les notifications push, la mise en cache des ressources et leur fourniture pour une expérience hors ligne, et la capacité de différer les actions jusqu'à ce que l'utilisateur ait une connexion stable à Internet. Un service worker peut faire l'objet d'un article Medium entier à lui seul, je ne vais donc pas m'attarder sur les [détails internes](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) de son fonctionnement. Mais je vais vous fournir un exemple simple à utiliser dans votre PWA.

Il est d'usage d'enregistrer le code lié au service worker dans un fichier appelé **_sw.js_**.

> 💡 L'emplacement du service worker est important, car il ne peut accéder qu'aux fichiers qui se trouvent dans le même répertoire ou sous-répertoire que lui-même.

Un service worker a un cycle de vie qui peut être résumé aux phases suivantes :

* Enregistrement
* Installation/Activation
* Réponse à divers événements

#### Expérience d'installation

L'une des fonctionnalités uniques d'une PWA est son expérience d'installation. Cela signifie que vous pouvez inviter l'utilisateur à installer votre application. Pour nous permettre de présenter cette capacité à l'utilisateur, nous devons écouter un événement appelé **_beforeinstallprompt_**. Voici un exemple de code démontrant le flux de présentation de l'option à l'utilisateur pour ajouter l'application à la logique d'activation basée sur son choix.

![Image](https://cdn-media-1.freecodecamp.org/images/LG4XqHneeagI9dGNOJ28F2oYInSR6vjQRTvy)
_Photo par [Unsplash](https://unsplash.com/@jamessutton_photography?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">James Sutton</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### HTTPS

Il n'y a pas si longtemps, les sites web pouvaient encore utiliser le protocole [http](https://www.w3schools.com/whatis/whatis_http.asp) trop courant. En raison des changements récents en matière de sécurité et dans [Chrome](https://searchengineland.com/effective-july-2018-googles-chrome-browser-will-mark-non-https-sites-as-not-secure-291623), tous les sites web qui n'utilisent pas le protocole https seront marqués comme non sécurisés. Même si votre site web ne traite pas de données utilisateur ou de communications sensibles, il est toujours bon de passer à https.

Et comme je l'ai mentionné précédemment, si vous souhaitez pouvoir publier une PWA, elle doit utiliser le protocole https. Si vous ne voulez pas vous embêter à acquérir un domaine, à trouver un hébergeur approprié et à activer SSL, vous pouvez opter pour l'option facile de Github. Si vous avez un compte, vous pouvez ouvrir un dépôt et configurer une [GitHub Page](https://pages.github.com/). Ce processus est assez simple et direct, et le bonus est d'obtenir le HTTPS intégré en tant que partie de Github.

#### Création d'un APK

Pour que notre PWA soit disponible dans le Google Play Store, nous devons créer un APK. Vous pouvez utiliser l'outil populaire [PWA2APK](https://pwa2apk.com/?ref=steemhunt), qui fera le travail difficile pour vous. Mais si vous préférez apprendre à le faire vous-même, continuez à lire.

Google a introduit une nouvelle façon d'intégrer votre PWA dans le Play Store en utilisant ce qu'on appelle une **_T_**rusted **_W_**eb **_A_**ctivity, ou TWA. En quelques étapes simples, vous apprendrez comment créer une TWA, que vous pourrez ensuite télécharger sur le Play Store.

1. Ouvrez Android Studio et créez une activité vide
2. Allez dans le fichier build.gradle du projet et ajoutez le dépôt jitpack

3. Allez dans le fichier build.gradle au **_niveau du module_** et ajoutez les lignes suivantes pour activer la compatibilité Java8

4. Ajoutez la bibliothèque de support TWA comme dépendance

5. Ajoutez le XML de l'activité à l'intérieur de votre fichier AndroidManifest entre les balises de l'application

6. Nous devons créer une association de l'application au site web en utilisant un lien de ressources numériques. Collez ce qui suit à l'intérieur de votre fichier **_strings.xml_**

7. Ajoutez la balise meta suivante comme enfant de votre balise d'application à l'intérieur du fichier AndroidManifest.xml

8. [Créez une clé de téléchargement et un keystore](https://developer.android.com/studio/publish/app-signing#generate-key)

9. Utilisez la commande suivante pour extraire le SHA-256

10. Allez sur le [générateur de liens de ressources](https://developers.google.com/digital-asset-links/tools/generator), fournissez l'empreinte SHA-256, le package de votre application et le domaine du site web

11. Placez le résultat dans un fichier nommé **_assetlinks.json_** sous l'emplacement **_/.well-known_** dans le répertoire de votre site web. Chrome recherchera spécifiquement cette destination.

12. [Générez un APK signé et téléchargez-le sur le Play Store](https://medium.freecodecamp.org/how-to-publish-an-application-in-the-play-store-8ddcc6dc3587)

![Image](https://cdn-media-1.freecodecamp.org/images/mp3eDdZW9F9StMhoajqbVozrN3FPeyDgQw8s)
_Photo par [Unsplash](https://unsplash.com/@aaronburden?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Aaron Burden</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Lighthouse

À ce stade, je suis sûr que vous avez déjà perdu de vue ce qui est requis pour votre PWA afin qu'elle soit valide pour la publication. Il y a tant de choses à prendre en considération qu'il est facile de perdre de vue les exigences.

Heureusement pour nous, Google a créé [Lighthouse](https://developers.google.com/web/tools/lighthouse/#devtools). Il peut être trouvé dans les outils de développement Chrome (à partir de la version 60 de Chrome). Il peut être facilement accessible en cliquant avec le bouton droit de la souris à l'intérieur du navigateur et en sélectionnant inspecter. Lorsque le nouveau panneau s'ouvre, vous verrez un onglet **_Audits_** dans le coin supérieur droit.

![Image](https://cdn-media-1.freecodecamp.org/images/iUXU9aPKpNWuJnHTDj6gfjsMpDewFzo4Zvy4)
_L'onglet Audits_

En laissant les paramètres de cet onglet tels quels, vous pouvez maintenant exécuter un audit en cliquant sur le bouton "Exécuter les audits". Cela prendra une minute ou deux, mais à la fin, vous recevrez une présentation graphique informative de la manière dont votre PWA se classe par rapport à trois propriétés :

* Performance
* Accessibilité
* Bonnes pratiques

Chaque propriété a une ventilation des points où votre application a passé les exigences et où elle ne les a pas passées. Cela vous permet de voir où vous devez faire des ajustements et où vous répondez à la norme. Si vous êtes intéressé, vous pouvez trouver une ventilation de la liste de contrôle [ici](https://developers.google.com/web/progressive-web-apps/checklist#baseline).

#### PWA à fond

Nous sommes arrivés à la fin de notre voyage et, espérons-le, vous vous sentez mieux préparé à naviguer dans le monde des PWAs. Cet article a été inspiré par le processus que j'ai suivi lors de la création d'une PWA récemment. Vous pouvez la consulter ci-dessous :

[**Android Menu XML Generator - Apps on Google Play**](https://play.google.com/store/apps/details?id=com.tomerpacific.androidmenugenerator)  
[_Générez tout type de menu dont vous avez besoin pour votre application Android. Choisissez parmi un menu Options, Contexte ou Popup et_play.google.com](https://play.google.com/store/apps/details?id=com.tomerpacific.androidmenugenerator)