---
title: Créez une expérience interactive Arduino et Unity3D sans latence !⏱
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-16T13:35:22.000Z'
originalURL: https://freecodecamp.org/news/you-can-now-create-an-arduino-and-unity3d-interactive-experience-without-latency-2d7388dcc0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GYnriIV-IBFyGDDIHjbQBA.gif
tags:
- name: arduino
  slug: arduino
- name: DIY
  slug: diy
- name: open source
  slug: open-source
- name: technology
  slug: technology
- name: Unity3D
  slug: unity3d
seo_title: Créez une expérience interactive Arduino et Unity3D sans latence !⏱
seo_desc: 'By Maxime Coutte

  Hi, I’m 16 years old and during the holidays I like to work on little projects.
  I grew up in a very artistic environment - my father is a painter my brothers and
  sisters draw, play music, compose … And me, with my best friend we want...'
---

Par Maxime Coutte

Bonjour, j'ai 16 ans et pendant les vacances, j'aime travailler sur de petits projets. J'ai grandi dans un environnement très artistique - mon père est peintre, mes frères et sœurs dessinent, jouent de la musique, composent… Et moi, avec mon meilleur ami, nous voulions nous amuser avec notre nouvel Arduino et Unity3D, alors nous avons commencé à travailler sur des expériences artistiques interactives. Mais nous avons été bloqués par un gros problème. Si vous avez déjà voulu transmettre des données d'Arduino à Unity3D, vous connaissez le principal problème : **LA LATENCE FOLLE**.

#### Ne vous inquiétez pas pour la latence, [wrmhl](https://github.com/relativty/wrmhl) est là ⚡

![Image](https://cdn-media-1.freecodecamp.org/images/Eq8d7WJ-2ZRuoAtYB-3UtzLDkFKivnwklyUc)
_Sans wrmhl (en utilisant un simple ReadLine() )_

Nous n'avons pas trouvé de solutions gratuites, optimisées et personnalisables pour résoudre ce problème. Alors j'ai construit [**wrmhl**](https://github.com/relativty/wrmhl). Vous pouvez maintenant connecter n'importe quelle interface Arduino à Unity3D, et c'est complètement **Open Source.**

* Écrivez simplement votre code Arduino, pourquoi pas [Une Interface de Suivi 3D Sans Contact](https://www.youtube.com/watch?v=ikD_3Vemkf0) ou une [Interface Arduino Ordinateur-Cerveau](http://openbci.com/) ?
* Ajoutez un Serial print pour envoyer des données de votre interface à Unity3D ([voir les exemples](https://github.com/relativty/wrmhl/blob/master/Arduino/Arduino.ino))
* Importez wrmhl dans Unity, et voilà !

Vous pouvez utiliser le protocole wrmhl par défaut, ou implémenter le vôtre en une minute en modifiant simplement : [wrmhl/Assets/WRMHL/Scripts/Thread/wrmhlThread_Lines.cs](https://github.com/relativty/wrmhl/blob/master/Assets/WRMHL/Scripts/Thread/wrmhlThread_Lines.cs).

#### Comment commencer ?

Suivez simplement le guide en [**cliquant ici**](https://github.com/relativty/wrmhl#getting-started-). Étoilez le dépôt si vous l'avez aimé ⭐

J'espère que cela sera utile ! Si vous l'utilisez, j'adorerais savoir ce que vous construisez. Contactez-moi à **maxime@relativty.com** ou [@maximecoutte](https://twitter.com/maximecoutte).