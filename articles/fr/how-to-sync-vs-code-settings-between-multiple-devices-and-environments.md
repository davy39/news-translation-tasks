---
title: Comment synchroniser les paramètres de VS Code entre plusieurs appareils et
  environnements
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-16T14:45:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-sync-vs-code-settings-between-multiple-devices-and-environments
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync.jpg
tags:
- name: code
  slug: code
- name: coding
  slug: coding
- name: Developer Tools
  slug: developer-tools
- name: editor
  slug: editor
- name: Productivity
  slug: productivity
- name: programing
  slug: programing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: tools
  slug: tools
- name: Visual Studio Code
  slug: vscode
seo_title: Comment synchroniser les paramètres de VS Code entre plusieurs appareils
  et environnements
seo_desc: 'All developers like their text editor a certain way, but it can be tough
  to make sure all of your environments have the same configuration. How can we make
  sure our VS Code configuration is the same wherever we use it?


  What is VS Code?

  What will we ...'
---

Tous les développeurs aiment leur éditeur de texte d'une certaine manière, mais il peut être difficile de s'assurer que tous vos environnements ont la même configuration. Comment pouvons-nous nous assurer que notre configuration VS Code est la même partout où nous l'utilisons ?

* [Qu'est-ce que VS Code ?](#heading-qu-est-ce-que-vs-code)
* [Que allons-nous utiliser ?](#heading-que-allons-nous-utiliser)
* [Comment cela fonctionne-t-il ?](#heading-comment-cela-fonctionne-t-il)
* [Étape 1 : Installer Settings Sync](#heading-etape-1-installer-settings-sync)
* [Étape 2 : Autoriser l'accès à Github](#heading-etape-2-autoriser-l-acces-a-github)
* [Étape 3 : Télécharger vos paramètres actuels](#heading-etape-3-telecharger-vos-parametres-actuels)
* [Étape 4 : Synchroniser votre configuration vers un autre environnement](#heading-etape-4-synchroniser-votre-configuration-vers-un-autre-environnement)
* [Étape 5 : Mettre à jour votre configuration](#heading-etape-5-mettre-a-jour-votre-configuration)

%[https://www.youtube.com/watch?v=TR2va67cVkQ]

## Qu'est-ce que VS Code ?

[Visual Studio Code](https://code.visualstudio.com/), ou VS Code, est un éditeur de code tout-en-un qui prend toutes les fonctionnalités que vous souhaitez pour travailler avec du code et les met dans un seul éditeur pour vous rendre ultra-productif.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/visual-studio-code-editor.jpg)
_Éditeur VS Code_

Il est le "cool kid on the block" depuis un certain temps et sa popularité ne cesse de croître, au moins dans la communauté JavaScript. Microsoft a mis beaucoup d'efforts pour en faire quelque chose que les gens veulent utiliser (et ils font du très bon travail).

## Que allons-nous utiliser ?

Nous allons utiliser une extension VS Code appelée [Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) qui utilise la fonctionnalité [Gist](https://gist.github.com/) de Github pour stocker un fichier de configuration JSON privé dans le cloud.

## Comment cela fonctionne-t-il ?

L'extension utilise l'OAuth de Github pour se connecter à votre compte Github. Une fois approuvé, VS Code obtient un jeton d'accès et atteint à la fois pour stocker et télécharger votre fichier de paramètres vers un Gist Github privé.

Une fois configuré, vous pouvez ensuite configurer l'extension sur toute autre instance de VS Code et immédiatement télécharger votre configuration pour synchroniser votre éditeur.

## Étape 0 : VS Code

Nous supposerons pour ce guide que vous avez déjà installé VS Code. Bien que vous n'ayez pas besoin d'avoir une configuration spéciale, avoir quelque chose de différent de la configuration par défaut (comme un [thème de couleur](https://code.visualstudio.com/docs/getstarted/themes)) vous aidera à voir comment cela fonctionne.

Commençons !

## Étape 1 : Installer Settings Sync

La première chose que nous devons faire est d'installer l'extension. Vous pouvez le faire [de plusieurs manières](https://code.visualstudio.com/docs/editor/extension-gallery) — vous pouvez visiter [la page web](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) et cliquer sur **Installer** ce qui ouvrira VS Code ou vous pouvez rechercher l'extension dans le panneau des extensions.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-1.jpg)
_Extension VS Code Settings Sync_

Une fois installée, elle ouvrira un nouvel onglet avec le tableau de bord Settings Sync.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-dashboard.jpg)
_Tableau de bord Settings Sync après l'installation_

## Étape 2 : Autoriser l'accès à Github

Pour commencer avec Github, cliquez sur le bouton **Se connecter avec Github** dans le tableau de bord Settings Sync.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-login-with-github.jpg)
_Se connecter à Settings Sync avec Github_

Cela ouvrira Github dans votre navigateur web par défaut et vous demandera de vous connecter. Bien que vous puissiez utiliser n'importe quel compte Github, il serait probablement plus judicieux d'utiliser votre compte personnel.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-login-success.jpg)
_Connexion réussie à Github pour Settings Sync_

Une fois connecté, vous devriez maintenant voir **Succès !** dans votre navigateur.

## Étape 3 : Télécharger vos paramètres actuels

Maintenant que vous êtes connecté à Github, vous êtes prêt à télécharger vos paramètres.

Ouvrez votre [Palette de commandes](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) avec CMD+Shift+P (sur Mac) ou naviguez vers Affichage et Palette de commandes. Tapez "Sync Upload" ce qui filtrera les commandes et appuyez sur entrée une fois que l'option **Sync: Update/Upload Settings** est sélectionnée.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-upload-update-command.jpg)
_Commande Update/Upload Settings dans Settings Sync_

En faisant cela, vous pourriez être invité avec un écran qui demande si vous voulez forcer le téléchargement — appuyez sur **Oui**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-force-upload.jpg)
_Forcer le téléchargement des nouveaux paramètres dans Settings Sync_

À ce stade, Settings Sync créera un nouveau Gist dans votre compte Github avec vos paramètres de configuration. Une fois terminé, vous devriez voir un message de succès.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-successful-upload.jpg)
_Téléchargement réussi des paramètres dans Settings Sync_

Vous devriez maintenant pouvoir visiter [gist.github.com](https://gist.github.com/) et trouver un nouveau Gist privé `cloudSettings` qui inclut tous vos paramètres VS Code !

## Étape 4 : Synchroniser votre configuration vers un autre environnement

Pour synchroniser votre configuration VS Code vers un autre ordinateur ou environnement VS Code, vous devez d'abord suivre les étapes 1 et 2 ci-dessus — installer l'extension et vous connecter à Github.

La différence est que cette fois, vous voulez configurer VS Code pour télécharger vos paramètres au lieu de les téléverser.

Pour commencer, ouvrez à nouveau votre tableau de bord Sync Settings. Si c'est une nouvelle installation comme nous le supposons ici, vous pouvez ouvrir la Palette de commandes et taper "sync download" et appuyer sur entrée ce qui ouvrira ce tableau de bord. Ici, cliquez sur **Modifier la configuration** cette fois.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-edit-configuration.jpg)
_Modifier la configuration de Settings Sync_

Sur cet écran, vous devriez voir votre **Github Access Token**, mais vous devriez également voir un champ vide pour l'ID de Gist. Ici, nous voulons d'abord récupérer l'ID de notre URL de Gist cloudSettings :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-github-gist.jpg)
_ID du Gist cloudSettings de VS Code_

Puis collez cette valeur dans notre champ **Gist ID** dans VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-gist-id-configuration-1.jpg)
_Ajout de l'ID de Gist à la configuration de Settings Sync_

Une fois qu'il est là, vous pouvez ouvrir à nouveau la Palette de commandes, taper "sync download", et appuyer sur entrée, et Sync Settings récupérera votre configuration VS Code depuis le Gist et mettra à jour vos paramètres locaux avec cette configuration !

## Étape 5 : Mettre à jour votre configuration

À partir de maintenant, chaque fois que vous voulez apporter une nouvelle modification à votre configuration stockée, vous devrez utiliser à la fois les fonctionnalités Update/Upload et Download comme nous l'avons fait ci-dessus.

Pour mettre à jour une nouvelle modification de votre configuration, tapez "sync update" et appuyez sur entrée :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-update-settings.jpg)
_Commande de mise à jour pour Settings Sync_

Et pour télécharger votre configuration afin de synchroniser un autre éditeur, tapez "sync download" et appuyez sur entrée :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-download-command.jpg)
_Commande de téléchargement des paramètres pour Settings Sync_

Ces commandes mettront à jour votre Gist cloudSettings et téléchargeront depuis celui-ci pour synchroniser vos instances VS Code.

## Quel est votre truc préféré avec VS Code ?

[Partagez-le avec moi sur Twitter !](https://twitter.com/colbyfayock)

## Rejoignez la conversation

%[https://twitter.com/colbyfayock/status/1272906851005366274]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>