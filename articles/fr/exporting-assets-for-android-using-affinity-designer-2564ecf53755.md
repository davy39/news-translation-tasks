---
title: Exporter des ressources pour Android en utilisant Affinity Designer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T06:46:52.000Z'
originalURL: https://freecodecamp.org/news/exporting-assets-for-android-using-affinity-designer-2564ecf53755
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UH2YFK41CVHsBQM1r8qABQ.png
tags:
- name: Android
  slug: android
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Exporter des ressources pour Android en utilisant Affinity Designer
seo_desc: 'By Dixita Ganatra

  Affinity Designer has a rich feature, Export Persona. I was wondering if it could
  ease the process of exporting assets for an Android project. Here’s what I found
  after delving into it.

  Preface

  This article assumes that you are fami...'
---

Par Dixita Ganatra

[Affinity Designer](https://affinity.serif.com/en-gb/designer/) possède une fonctionnalité riche, **Export Persona**. Je me demandais si cela pouvait faciliter le processus d'exportation des ressources pour un projet Android. Voici ce que j'ai découvert après l'avoir exploré.

#### Préambule

Cet article suppose que vous êtes familier avec la navigation dans Affinity Designer. Je vais utiliser une maquette d'exemple d'une application de fitness appelée **Watch Your Steps**. Cette application compte vos pas quotidiens, le temps pendant lequel vous avez été actif, les calories que vous avez brûlées et la distance que vous avez parcourue.

![Image](https://cdn-media-1.freecodecamp.org/images/QGOWZjfU8z54IHq4YGZIOymi1GSI38eHOlQE)
_« Watch Your Steps »_

Pour utiliser ces icônes dans une application Android, nous devons les exporter. Comme cette application va fonctionner sur des appareils Android avec diverses tailles d'écran, nous devons les exporter pour diverses résolutions.

#### Les étapes

**Étape 1 :** Lorsque votre design est prêt, passez à **Export Persona**.

![Image](https://cdn-media-1.freecodecamp.org/images/PhNCxNMRb2vf1HT8kr9wYSn1rEfZ3CW47kp9)
_Export Persona_

**Étape 2 :** Allez dans le panneau **Slices** dans le volet de droite.

![Image](https://cdn-media-1.freecodecamp.org/images/cH24SAa8xefhaadpih6sQfSmYAvfieVoy6LB)
_Panneau **Slices**_

Pour exporter des icônes, nous devons les découper. Affinity crée une tranche pour notre œuvre par défaut. Maintenant, nous devons découper les icônes de notre œuvre. Nous allons créer des tranches directement à partir des calques. Nous pourrions également utiliser l'**Outil de découpe** pour créer des tranches manuellement.

**Étape 3 :** Allez dans le panneau des calques. Sélectionnez les calques que vous souhaitez exporter et cliquez sur **Create Slice**.

![Image](https://cdn-media-1.freecodecamp.org/images/Aick0-inYuaP8QFArocDwh1p27VkOaAt7wNR)
_Calques à découper_

Ce sont les calques qui ont été créés dans **Draw Persona**. Nous allons exporter les calques mis en évidence ci-dessus. Vous devriez maintenant voir des bordures bleues autour des calques découpés dans votre œuvre, indiquant les tranches créées.

![Image](https://cdn-media-1.freecodecamp.org/images/tgJgk-HVZyTkxpgu3GOI8wBJSSIJfrpEYUjm)
_Triches_

**Étape 4 :** Allez dans le panneau **Slices** et décochez la tranche par défaut (la tranche de l'application dans cet exemple) et toute autre tranche que vous ne souhaitez pas exporter.

![Image](https://cdn-media-1.freecodecamp.org/images/H3jruZ80r1eiHUhesv8Hkg61LZ2mpxRctsmW)
_Calques découpés_

**Étape 5 :** Développez une tranche en cliquant sur une flèche du côté gauche et définissez le chemin du fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/HPQFVDufWe4lZX4Kuh9auAdiWpaNxFf0T1R5)

Il montre les détails d'une tranche. La zone mise en évidence montre le chemin du fichier de la tranche développée. Puisque nous avons donné à nos calques des noms appropriés, nous pouvons les réutiliser pour les chemins de fichiers.

Par défaut, la taille du png sera **1x** (identique à celle de l'icône). Nous avons besoin de cette taille pour **drawable-mdpi** dans un projet Android. Cliquez sur le chemin du fichier et effectuez les étapes suivantes pour le définir.

Supprimez **Scale suffix (1x)** du nom de fichier et ajoutez `drawable-mdpi/` à notre chemin de fichier (n'oubliez pas le / final). Parce que nous voulons que notre ressource soit dans le dossier `drawable-mdpi/`, nommée `back_button.png`.

![Image](https://cdn-media-1.freecodecamp.org/images/f6idoX0cUSIO5yLeBVBEc4SrMjIsC8A5Fyil)
_drawable-mdpi/back_button.png_

**Étape 6 :** Suivez l'étape précédente pour **drawable-hdpi — 1.5x, drawable-xhdpi — 2x, drawable-xxhdpi — 3x** et **drawable-xxxhdpi — 4x**.

Après avoir terminé l'**Étape 6**, la tranche ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/iJfP5g7SzU0mpKoVYHsC6wKS-CElCaffEF73)
_Toutes les tailles avec leurs dossiers respectifs_

Nous n'avons pas à répéter cette procédure pour toutes les icônes suivantes. Affinity fournit une fonctionnalité pour sauvegarder cela comme un préréglage.

**Étape 7 :** Cliquez sur l'icône de menu en haut à droite du panneau Slices et sélectionnez **Create export setup preset**. Ensuite, nommez-le **Android** (ou ce que vous préférez).

![Image](https://cdn-media-1.freecodecamp.org/images/2FZxwSyVMNWwKrqekZA7S9B00SyjHcv94w7j)
_Créer le préréglage **Android**_

Maintenant, nous sommes prêts à sélectionner le reste des tranches et à appliquer le préréglage **Android** sur elles. ?

![Image](https://cdn-media-1.freecodecamp.org/images/GAxwMzX3bQ35iwA-C5xHDXdjrZN8dgI9sJ3n)
_Appliquer le préréglage Android au reste des tranches_

Comme vous pouvez le voir, une fois que vous avez créé un préréglage, il est extrêmement facile de l'appliquer aux autres.

**Étape 8 :** Cliquez sur **Export Slices** placé en bas à droite. Les icônes seront exportées dans leurs dossiers respectifs. Après les avoir exportées, la structure des dossiers ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BurQKOsSbedJfJP2StkliLRrGgDGB8uucJvn)
_Icônes exportées exactement comme nous le voulions ?_

Et si nous changeons les icônes plus tard ? Devons-nous les exporter à nouveau ??

Non, nous n'avons pas à le faire.

#### Bonus

Vérifiez simplement l'option mise en évidence, **Continuous**.

![Image](https://cdn-media-1.freecodecamp.org/images/cg83sJ1q6zO8hQDr0QoPSoBCuW3LNuxtIoV5)
_Vérifier continuous_

Maintenant, chaque fois que vous enregistrez vos modifications, les ressources exportées seront mises à jour en continu. N'est-ce pas cool ??

![Image](https://cdn-media-1.freecodecamp.org/images/vsm2ijONxrMgOziFPy1ymQfBc5M1TfA-gahF)
_Mise à jour en direct lors de l'enregistrement de l'œuvre_

C'est tout, les amis. Contactez-moi si vous avez des idées à partager. Je serais ravie de vous entendre sur Twitter [@dixita0607](https://twitter.com/dixita0607).

#### Maquette de l'application

Vous pouvez télécharger le fichier de maquette utilisé dans ce tutoriel ici ?.

[**watch-your-steps.afdesign**](https://drive.google.com/file/d/1XMIWRoeKHryH2B7i3CMLb30usCDJo3p2/view?usp=sharing)  
 drive.google.com

#### Références

[**Android Icon Reference Chart | The Icon Handbook**](http://iconhandbook.co.uk/reference/chart/android/)  
[_The Icon Handbook is a reference manual, how-to guide and coffee table 'showcase' in one. learn how to design icons for…_iconhandbook.co.uk](http://iconhandbook.co.uk/reference/chart/android/)[**A Designers Guide for naming Android Assets**](https://medium.com/@AkhilDad/a-designers-guide-for-naming-android-assets-f790359d11e5)  
[_This article is mainly intended for Curious Designers and it will also help newbie developers but experienced…_medium.com](https://medium.com/@AkhilDad/a-designers-guide-for-naming-android-assets-f790359d11e5)