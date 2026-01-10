---
title: Comment corriger l'écran noir de Google Chrome sur Linux OS (Wayland)
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-04-27T19:33:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-black-screen-on-google-chrome-on-linux-os
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Fix
seo_title: Comment corriger l'écran noir de Google Chrome sur Linux OS (Wayland)
---

1-.png
tags:
- name: Google Chrome
  slug: chrome
- name: Linux
  slug: linux
- name: Résolution de problèmes
  slug: problem-solving
seo_title: null
seo_desc: 'Si vous êtes un utilisateur Linux, alors vous avez probablement utilisé l'environnement de bureau GNOME au moins une fois.

Le dernier environnement de bureau GNOME (DE) utilise Wayland de nos jours. Et bien qu'il soit possible de supprimer Wayland et de sélectionner Xorg si vous le souhaitez, la plupart des utilisateurs commencent à utiliser Wayland comme leur environnement principal. '
---

Si vous êtes un utilisateur Linux, alors vous avez probablement utilisé l'environnement de bureau GNOME au moins une fois.

Le dernier environnement de bureau GNOME (DE) utilise Wayland de nos jours. Et bien qu'il soit possible de supprimer Wayland et de sélectionner Xorg si vous le souhaitez, la plupart des utilisateurs commencent à utiliser Wayland comme leur environnement principal. 

Et si vous utilisez toujours les navigateurs Chrome ou Chromium, vous rencontrerez souvent le problème d'écran noir lors du partage d'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Untitled-design.png)

Si vous utilisez généralement Wayland sur votre bureau, vous aurez ces problèmes lors du partage d'écran, en particulier dans Google Meet. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Untitled-design--1-.png)

Dans cet article, je vais vous montrer une astuce très simple qui vous aidera à résoudre le problème d'écran noir lors du partage d'écran sur tout type de navigateur Chromium, y compris le navigateur le plus populaire, Google Chrome. 

J'ai utilisé Ubuntu pour écrire cet article, mais le même processus est applicable à toutes les autres distributions Linux fonctionnant sur Wayland.

## Le problème d'écran noir 

Si vous avez le problème d'écran noir dans Google Meet dans un navigateur Chromium (Chrome, Brave, Vivaldi, etc.), cela ressemble probablement à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-38-51.png)

Parfois, cela peut arriver parce que le partage d'écran sous Wayland est rompu ou à cause d'autres problèmes. Beaucoup d'utilisateurs disent également que cela se produit alors que les développeurs tentent d'augmenter le niveau de sécurité. 

Le problème du partage d'écran peut devenir courant pour de nombreuses personnes de manière habituelle. Beaucoup d'utilisateurs reviennent à X11 uniquement pour ce problème ou essaient la solution pipewire pour le résoudre.

Je vais vous montrer la solution en utilisant la technologie pipewire afin que vous n'ayez pas besoin de revenir à X11 uniquement pour résoudre ce problème. 😊

Allez à **`chrome://flags/#enable-webrtc-pipewire-capturer`** en utilisant la barre d'adresse de votre navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-23.png)

Vous obtiendrez une longue liste, mais nous nous intéressons à **WebRTC PipeWire Support**. Vous verrez que l'option est en mode Default pour le moment.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-31.png)

Nous devons le changer en **Enabled**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-40.png)

Cliquez simplement sur le menu déroulant et cliquez sur **Enabled**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-54.png)

Maintenant, vous verrez une invite en bas à droite pour relancer le navigateur afin que cela prenne effet.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-39-54-1.png)

Cliquez sur **Relaunch**. Cela redémarrera simplement votre navigateur.

Le problème est résolu ! ✌️

## Comment tester le partage d'écran

Maintenant, si vous voulez partager votre écran comme d'habitude, vous pouvez certainement le faire. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-40-27.png)

Chaque fois que vous voulez partager l'écran, une invite apparaîtra et vous demandera de sélectionner le moniteur. Vous devez partager le moniteur. Si vous n'avez qu'un seul moniteur comme moi, alors vous obtiendrez un seul moniteur. Cliquez simplement dessus et cliquez sur **Share**. 

Vous pourrez également voir l'aperçu du partage d'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-40-40.png)

Vous devrez peut-être sélectionner le moniteur à nouveau dans l'invite. Sélectionnez simplement le moniteur et cliquez sur Share comme précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-40-47.png)

Désormais, vous pouvez partager votre écran sur Google Meet depuis Wayland.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-from-2022-04-25-19-41-07.png)

## Conclusion

Si cet article vous aide à résoudre le problème d'écran noir pour votre environnement de bureau Linux, alors j'ai réussi. 😊

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous voulez entrer en contact avec moi, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [VOUS ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous voulez apprendre divers types de langages de programmation avec beaucoup d'exemples pratiques régulièrement.

Si vous voulez consulter mes moments forts, vous pouvez le faire sur ma [timeline Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !