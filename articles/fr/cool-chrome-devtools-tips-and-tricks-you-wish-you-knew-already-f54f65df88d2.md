---
title: Astuces et conseils cool pour Chrome DevTools que vous auriez aimé connaître
  déjà
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-03-21T03:43:40.000Z'
originalURL: https://freecodecamp.org/news/cool-chrome-devtools-tips-and-tricks-you-wish-you-knew-already-f54f65df88d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7B6B7FIxj18TSeYxh1ssLA.png
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Astuces et conseils cool pour Chrome DevTools que vous auriez aimé connaître
  déjà
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Check out my overview of Chrome DevTools if you’re new to this awesome browser feature!

  1. Drag-and-drop in the Elements panel

  In the Elements panel, you can drag and drop any HTML el...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

_Consultez mon [aperçu des Chrome DevTools](https://flaviocopes.com/browser-dev-tools/) si vous êtes nouveau dans cette fonctionnalité incroyable du navigateur !_

### 1. Glisser-déposer dans le panneau Éléments

Dans le panneau Éléments, vous pouvez glisser-déposer n'importe quel élément HTML et changer sa position sur la page

![Image](https://cdn-media-1.freecodecamp.org/images/J3dSB29NHaiRsAyWJoY3CtiY5YfvRiHztkkz)
_Glisser-déposer dans le panneau Éléments_

### 2. Référencer l'élément actuellement sélectionné dans la Console

Sélectionnez un nœud dans le panneau Éléments, et tapez `$0` dans la console pour le référencer.

Si vous utilisez jQuery, vous pouvez entrer `$($0)` pour accéder à l'API jQuery sur cet élément.

![Image](https://cdn-media-1.freecodecamp.org/images/uBex4ymprtLR2QDMMBJEACRiGwM5tCJqX0zo)
_Référencer l'élément actuellement sélectionné dans la Console_

### 3. Utiliser la valeur de la dernière opération dans la Console

Utilisez `$_` pour référencer la valeur de retour de l'opération précédente exécutée dans la Console

![Image](https://cdn-media-1.freecodecamp.org/images/-aFTiSJharifJBxSjaWA58lKtao6TYP6ws24)
_Utiliser la valeur de la dernière opération dans la Console_

### 4. Ajouter du CSS et modifier l'état de l'élément

Dans le panneau Éléments, il y a deux boutons super utiles.

Le premier vous permet d'ajouter une nouvelle propriété CSS avec n'importe quel sélecteur que vous voulez, mais en pré-remplissant l'élément actuellement sélectionné :

![Image](https://cdn-media-1.freecodecamp.org/images/aLksEN0rT35gMIVX1a-OKKH4GO6pPLUl2TYl)
_Ajouter des règles CSS_

Le second vous permet de déclencher un état pour l'élément sélectionné, afin que vous puissiez voir les styles appliqués lorsqu'il est actif, survolé ou en focus.

![Image](https://cdn-media-1.freecodecamp.org/images/tcLTyDx-Cpj63K80yhGngLvCJUC8vq00JKL9)
_Modifier l'état de l'élément_

### 5. Enregistrer dans un fichier le CSS modifié

Cliquez sur le nom du fichier CSS que vous avez modifié. L'inspecteur l'ouvre dans le panneau Sources, et à partir de là, vous pouvez l'enregistrer avec les modifications en direct que vous avez appliquées.

Cette astuce ne fonctionne pas pour les nouveaux sélecteurs ajoutés en utilisant +, ou dans les propriétés `element.style`, mais seulement pour les sélecteurs existants modifiés.

![Image](https://cdn-media-1.freecodecamp.org/images/cjIJRyFBsrqtacu7x-2hI2A138q1IkzGkOCx)
_Enregistrer dans un fichier le CSS modifié_

### 6. Capturer un seul élément

Sélectionnez un élément et appuyez sur `cmd-shift-p` (ou `ctrl-shift-p` sous Windows) pour ouvrir le Menu de Commandes, et sélectionnez **Capturer une capture d'écran du nœud**

![Image](https://cdn-media-1.freecodecamp.org/images/VY-9pqkmmxqQ65gagIT9ny1chbAFilNSARYx)
_Capturer un seul élément_

### 7. Trouver un élément en utilisant des sélecteurs CSS

Appuyez sur `cmd-f` (`ctrl-f` sous Windows) pour ouvrir la boîte de recherche dans le panneau Éléments.

Vous pouvez taper n'importe quelle chaîne de caractères pour correspondre au code source, ou vous pouvez également utiliser des sélecteurs CSS pour que Chrome génère une image pour vous :

![Image](https://cdn-media-1.freecodecamp.org/images/Et49Lo99VjJ8U7ecVlVHiDUKjbtgYlv3iQ-l)
_Trouver un élément en utilisant des sélecteurs CSS_

### 8. Shift-Entrée dans la Console

Pour écrire des commandes qui s'étendent sur plusieurs lignes dans la Console, appuyez sur `shift-entrée`.

Une fois que vous êtes prêt, appuyez sur entrée à la fin du script pour l'exécuter :

![Image](https://cdn-media-1.freecodecamp.org/images/Zp-kmkNp-xwadTjGHYBtG8iVDd2doLcvSF5c)
_Shift-Entrée dans la Console pour écrire des commandes multilingues_

Vous pouvez effacer la console en utilisant le bouton _Effacer_ en haut à gauche de la console, ou en appuyant sur `ctrl-l` ou `cmd-k`.

### 9. Aller à...

Dans le panneau Sources :

* `cmd-o` (`ctrl-o` sous Windows), affiche tous les fichiers chargés par votre page.
* `cmd-shift-o` (`ctrl-shift-o` sous Windows) affiche les symboles (propriétés, fonctions, classes) dans le fichier actuel.
* `ctrl-g` va à une ligne spécifique.

![Image](https://cdn-media-1.freecodecamp.org/images/puVmoQLIN2MNVSZCth0a2uIXoQtUYektEvXo)
_Aller à un fichier_

### 10. Expression de surveillance

Au lieu d'écrire encore et encore un nom de variable ou une expression que vous allez vérifier souvent pendant une session de débogage, ajoutez-la à la liste _Expression de surveillance_.

![Image](https://cdn-media-1.freecodecamp.org/images/bu7wYPMPNH4P3QTIepcO17XaU-Ydsl0vxjlR)
_Expression de surveillance_

### 11. Débogage XHR/Fetch

Depuis le débogueur, ouvrez le panneau **Points d'arrêt XHR/Fetch**.

Vous pouvez le configurer pour interrompre chaque fois qu'un appel XHR/Fetch est envoyé, ou seulement sur des appels spécifiques :

![Image](https://cdn-media-1.freecodecamp.org/images/uoE2VO1YJrvhZ2gc8NgpRdInyu9TKtPjiihw)
_Débogage XHR/Fetch_

### 12. Déboguer les modifications du DOM

Faites un clic droit sur un élément et activez _Interrompre sur les modifications des sous-éléments_. Chaque fois qu'un script parcourt les enfants de cet élément et les modifie, le débogueur s'arrête automatiquement pour vous permettre d'inspecter ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/hvvrtgLnmMgnDQogl0m9A2gF9FCyfUZfnpbk)
_Déboguer les modifications du DOM_

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)