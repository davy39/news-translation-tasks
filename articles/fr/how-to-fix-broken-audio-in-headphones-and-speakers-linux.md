---
title: Comment réparer l'audio défectueux dans les écouteurs et les haut-parleurs
  sous Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-02-16T15:27:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-broken-audio-in-headphones-and-speakers-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--10-.jpg
tags:
- name: audio
  slug: audio
- name: Linux
  slug: linux
seo_title: Comment réparer l'audio défectueux dans les écouteurs et les haut-parleurs
  sous Linux
seo_desc: "If you are using the Linux operating system on your desktop, you might\
  \ have faced some audio issues before. Like when you're trying to get sound in your\
  \ speakers when your headphones are connected to the audio jack. \nIf so, no worries!\
  \ It is a pretty..."
---

Si vous utilisez le système d'exploitation Linux sur votre ordinateur, vous avez peut-être déjà rencontré des problèmes audio. Par exemple, lorsque vous essayez d'obtenir du son dans vos haut-parleurs alors que vos écouteurs sont connectés à la prise audio. 

Si c'est le cas, pas de panique ! C'est un problème assez courant que vous pouvez résoudre rapidement. Dans cet article, je vais vous aider à résoudre ce problème complètement. J'utiliserai une distribution bien connue appelée [Manjaro Linux](https://manjaro.org/), mais je pense que la même méthode est applicable à toutes les distributions Linux.

### Étape 1 – Ouvrir le terminal / la console


![Image](https://www.freecodecamp.org/news/content/images/2022/02/2.png)

### Étape 2 – Ouvrir Alsamixer
Nous allons utiliser alsamixer pour ajuster les paramètres audio. Tapez `alsamixer` et appuyez sur la touche **Entrée** de votre clavier.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/3.png)

Alsamixer s'ouvrira dans votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/4.png)

### Étape 3 – Sélectionner la carte son préférée

Maintenant, vous devez sélectionner votre carte son préférée. Pour cela, appuyez simplement sur la touche `F6` de votre clavier. Sélectionnez la carte son appropriée pour vous. 

Si vous n'êtes pas sûr, vous pouvez simplement en sélectionner une à la fois (appuyez sur la touche **Entrée** après avoir sélectionné la carte son) et essayer les autres méthodes pour voir si cette carte son était appropriée ou non. Pour moi, c'est **default:1 HD-Audio Generic**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/5.png)

La fenêtre AlsaMixer changera en fonction de la carte son sélectionnée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/6.png)

Ensuite, appuyez sur la touche flèche droite (`→`) jusqu'à ce que vous trouviez **Auto-Mute Mode**. 

Vous verrez qu'il est actuellement **ACTIVÉ**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/7.png)

Nous devons le changer en **DÉSACTIVÉ**. Vous devez appuyer sur la touche flèche bas (`↓`) pour le désactiver.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/8.png)

Ensuite, appuyez sur la touche `Échap` pour quitter AlsaMixer.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/10.png)

### Étape 4 – Sauvegarder les paramètres

Maintenant, nous devons sauvegarder les paramètres que nous venons d'ajuster dans AlsaMixer. Pour cela, tapez `sudo alsactl store`. Appuyez ensuite sur la touche **Entrée**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/11.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/12.png)

Maintenant, vous êtes prêt à partir !

Si vous souhaitez vérifier si l'audio fonctionne dans vos haut-parleurs ou non, vous pouvez aller dans **Paramètres**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/13.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/14.png)

Ensuite, allez dans **Son**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/15.png)

Si vous changez votre **Périphérique de sortie**, vous devriez voir que l'audio des haut-parleurs fonctionne parfaitement. J'utilise ici l'option **Line Out** pour ma station de travail.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/16.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/17.png)

Maintenant, vous devriez voir que le problème audio a été résolu !

**BONUS** : J'ai également réalisé un tutoriel vidéo complet à ce sujet et publié la [vidéo](https://youtu.be/zCaJ6lcaSOg) sur ma nouvelle chaîne YouTube.

%[https://youtu.be/zCaJ6lcaSOg]

## Conclusion

J'espère que cette astuce vous aidera si vous rencontrez également ce type de problème audio avec vos haut-parleurs. Merci beaucoup d'avoir lu l'article entier jusqu'à présent. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !