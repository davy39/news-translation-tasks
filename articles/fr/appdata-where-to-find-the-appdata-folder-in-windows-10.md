---
title: AppData – Où trouver le dossier AppData dans Windows 10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T18:22:12.000Z'
originalURL: https://freecodecamp.org/news/appdata-where-to-find-the-appdata-folder-in-windows-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9975740569d1a4ca1fd7.jpg
tags:
- name: data
  slug: data
- name: Windows 10
  slug: windows-10
seo_title: AppData – Où trouver le dossier AppData dans Windows 10
seo_desc: 'By Vijit Ail

  The AppData folder includes application settings, files, and data unique to the
  applications on your Windows PC. The folder is hidden by default in Windows File
  Explorer and has three hidden sub-folders: Local, LocalLow, and Roaming.

  You...'
---

Par Vijit Ail

Le dossier AppData contient les paramètres des applications, les fichiers et les données uniques aux applications de votre PC Windows. Le dossier est masqué par défaut dans l'Explorateur de fichiers Windows et contient trois sous-dossiers masqués : Local, LocalLow et Roaming.

Vous n'utiliserez pas souvent ce dossier, mais c'est là que résident vos fichiers importants. Par exemple, vos favoris, les sessions enregistrées, etc.

Dans ce guide, vous apprendrez à trouver, afficher et accéder au dossier AppData dans Windows.

## Qu'est-ce que le dossier AppData ?

Les applications sous Windows stockent souvent leurs paramètres et données temporaires dans le dossier AppData. Chaque compte utilisateur Windows possède son propre dossier AppData. Comme je l'ai mentionné précédemment, il y a trois dossiers à l'intérieur d'AppData : Local, LocalLow et Roaming.

Le dossier Local est utilisé pour stocker des données spécifiques à un seul système Windows, ce qui signifie que les données ne sont pas synchronisées entre plusieurs PC.

Le dossier LocalLow est identique au dossier Local, sauf qu'il est utilisé par des applications avec une intégrité faible qui s'exécutent avec des paramètres de sécurité restreints, par exemple, Mozilla Firefox en mode privé.

Le dossier Roaming est utilisé pour stocker des données qui seront synchronisées sur plusieurs systèmes Windows. Cela est souvent utilisé pour stocker des paramètres comme les favoris, les mots de passe enregistrés, etc.

## Comment afficher le dossier AppData

Il existe deux façons d'accéder au dossier AppData. Vous pouvez y accéder manuellement ou en utilisant le nom de variable « AppData ».

Vous pouvez afficher le dossier AppData manuellement en allant dans votre dossier Utilisateurs, qui se trouve dans le lecteur C. Dans mon cas, le chemin est `C:\Users\ADMIN`.

Ensuite, allez dans l'onglet « Affichage » en haut et cochez la case « Éléments masqués », comme illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_373.png)

Maintenant, vous devriez pouvoir voir le dossier AppData dans votre dossier Utilisateur.

Vous pouvez également accéder directement au dossier AppData en utilisant la variable système AppData. Recherchez « Exécuter » dans la recherche Windows comme illustré ci-dessous, ou appuyez sur les touches Windows + R pour ouvrir l'application Exécuter.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_374.png)

Dans la zone de texte de l'application Exécuter, entrez « %AppData% » et cliquez sur OK. Windows ouvrira directement le dossier Roaming qui se trouve à l'intérieur du dossier AppData.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_375.png)

## Conclusion

Après avoir lu ce guide, j'espère que vous serez en mesure de trouver le dossier AppData sur votre PC.

Généralement, vous n'aurez pas à vous soucier des données à l'intérieur du dossier AppData – c'est pourquoi il est masqué par défaut. Il est uniquement utilisé par les développeurs d'applications pour stocker les données nécessaires requises par l'application.

Les utilisateurs quotidiens de Windows n'auront besoin d'accéder ou de consulter le dossier AppData que s'ils doivent créer une sauvegarde de leurs données d'application.