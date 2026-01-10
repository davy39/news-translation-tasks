---
title: 'Le défi Foobar : le test caché de Google pour les développeurs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T01:02:39.000Z'
originalURL: https://freecodecamp.org/news/the-foobar-challenge-googles-hidden-test-for-developers-ed8027c1184
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MirHqdGmQeG2kH_CuAkyow.jpeg
tags:
- name: coding
  slug: coding
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: recruiting
  slug: recruiting
- name: 'tech '
  slug: tech
seo_title: 'Le défi Foobar : le test caché de Google pour les développeurs'
seo_desc: 'By Daniel Simmons

  You’re just sitting at your desk, minding your own business, trying to get some
  work done. Then, as inevitably happens, you hit a minor roadblock: your code throws
  a cryptic error message.

  “No problem” you think. This isn’t your fir...'
---

Par Daniel Simmons

Vous êtes assis à votre bureau, concentré sur votre travail, essayant d'avancer. Puis, comme cela arrive inévitablement, vous rencontrez un petit obstacle : votre code génère un message d'erreur cryptique.

« Pas de problème », pensez-vous. Ce n'est pas votre première expérience. Vous copiez-collez donc le message d'erreur tel quel dans Google pour voir ce que vous obtenez.

Pas de chance.

Il y a beaucoup de résultats de recherche, mais aucun ne correspond suffisamment à votre situation pour fournir une réponse utile.

Commence alors le processus de recherche créative sur Google. Vous essayez plusieurs combinaisons de l'erreur et du contexte dans lequel vous l'utilisez. Vous essayez d'inclure le nom de la bibliothèque que vous utilisez. Vous savez que vous vous rapprochez...

À votre sixième tentative, vous essayez une autre combinaison de termes de recherche et appuyez sur Entrée. La page se charge et vous commencez à parcourir les résultats lorsque, soudain, votre fenêtre de navigateur se divise et vous voyez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/SGTMxvXNNEOLVst2tM8KUMqC47UCvoPblaHy)

> « Vous parlez notre langue. Prêt pour un défi ? »

« Attendez, quoi ? »

« D'où cela vient-il ? »

« Une sorte de défi de Google... Est-ce basé sur mon historique de recherche ? »

Vous oubliez complètement le bug dans votre code. Vous êtes maintenant totalement absorbé par la situation bizarre dans laquelle vous vous trouvez. Et, aussi intéressant que cela soit déjà, vous remarquez quelque chose qui ajoute à l'intrigue. À côté du message, vous voyez que le premier bouton dit :

> « Je veux jouer »

Oh, donc c'est un **jeu** ? Intéressant...

Submergé par la curiosité, vous acceptez. La division de votre fenêtre de navigateur s'agrandit lentement pour révéler un grand écran noir, qui s'estompe ensuite. Vous êtes redirigé vers [www.google.com/foobar/](http://www.google.com/foobar/?eid=...). Un écran noir s'estompe et du texte apparaît. Cela ressemble à un terminal Unix.

L'esthétique de la page (la police d'ordinateur rétro, le terminal caché, l'absence d'une interface moderne) combinée à l'ambiance « 007 - Votre mission, si vous l'acceptez » de cette expérience vous donne l'impression d'avoir été plongé dans un monde secret. Vous êtes maintenant totalement absorbé.

Il y a du texte en haut de l'écran :

> « Google a un défi de code prêt pour vous »

Juste en dessous, il y a un paragraphe de texte bleuâtre qui plante le décor pour une aventure de science-fiction :

> « Succès ! Vous avez réussi à infiltrer l'organisation maléfique du Commandant Lambda, et vous avez enfin obtenu un poste de débutant en tant que Minion sur sa station spatiale. À partir de là, vous pourriez peut-être contrer ses plans d'utiliser le dispositif de fin du monde LAMBCHOP pour détruire la Planète Bunny. Le problème, c'est que les Minions sont les plus bas dans la hiérarchie de Lambda. Mieux vaut se ressaisir et se mettre au travail, sinon vous n'arriverez jamais au sommet... »

![Image](https://cdn-media-1.freecodecamp.org/images/gQefNspuqe9bRP2e88JFcL6qfJdriFbE5jLg)

« Très bien. Donc, il semble que je puisse soit explorer le terminal, soit commencer le défi... »

Votre curiosité prend le dessus et vous pensez : « Je ne peux pas commencer le jeu sans fouiner un peu. » Vous tapez donc « help » et appuyez sur Entrée. Une liste de commandes shell apparaît.

![Image](https://cdn-media-1.freecodecamp.org/images/Mva-DSMeGRFz543CL8DIdKI3t2ZEEx6wLxA-)

« Très intéressant. Nous allons clairement travailler avec un système de fichiers. Mais cette liste d'options est assez limitée. »

Vous décidez de voir si certaines des commandes courantes non listées sont disponibles, alors vous essayez quelque chose de simple :

```
foobar:~/guest$ pwd
```

Cela fonctionne ! Vous voyez :

```
/home/guest
```

Super.

« Bon, jetons un coup d'œil à ce répertoire personnel. Il doit y avoir des choses plus intéressantes là-bas. »

Vous essayez donc :

```
foobar:~/guest$ cd ..
```

Et...

Rien.

Vous obtenez une nouvelle ligne sans erreur, mais lorsque vous exécutez à nouveau `pwd`, juste pour vérifier, vous voyez toujours `/home/guest`. D'accord, donc ce terminal n'est probablement pas un shell Unix en monde ouvert rempli d'easter eggs comme vous l'espériez. Vous décidez donc de simplement passer au défi.

Vous tapez le mot « request » et appuyez sur Entrée.

Un message apparaît, vous avertissant que ce défi est chronométré et que vous aurez 48 heures pour le compléter.

« Wow. D'accord, donc c'est chronométré... »

Vous acceptez et continuez.

![Image](https://cdn-media-1.freecodecamp.org/images/rb6AaixRYZyeczg-5-JNvv-EgLsdh82HPADW)

Plus de récit de science-fiction, et vous voyez qu'un fichier nommé `solar_doomsday` a été ajouté à votre dossier personnel. Vous naviguez donc vers le dossier, l'ouvrez et trouvez quatre fichiers :

```
constraints.txt
readme.txt
solution.java
solution.py
```

Le fichier readme semble être l'endroit évident pour commencer. Vous ouvrez le fichier readme et voyez ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/9ElOQQfX6u4iACgoptqIXS3yT1uBH5WO3RXm)

« D'accord », pensez-vous, « lorsque vous retirez le récit, ils veulent que j'écrive une fonction qui retourne un tableau trié de tous les nombres carrés (y compris 1) qui s'additionnent pour donner un nombre donné, en commençant par le plus grand. » Plutôt cool.

« Donc, c'est le genre de défi que Google utilise pour tester la capacité à résoudre des problèmes ? »

« Eh bien, je suis déjà allé aussi loin. Autant essayer ! »

#### À propos du défi Foobar

Ce qui précède est une description du défi Foobar de Google : une sorte d'easter egg dans Chrome qui est ostensiblement utilisé pour recruter de nouveaux talents pour l'équipe d'ingénierie de Google ; bien que Google ne semble pas avoir reconnu Foobar de manière significative (du moins, pas que j'aie trouvé). Il existe cependant de nombreux témoignages de développeurs ayant traversé le processus, ce qui confirme clairement de quoi il s'agit.

L'aspect unique du défi Foobar est qu'il **vous** trouve. Et pas de la manière dont un email de recrutement non sollicité ou un message texte commercial vous « trouve ». Il vous trouve en suivant votre activité de recherche et en la faisant (semble-t-il) correspondre aux besoins connus des départements d'ingénierie de Google. De plus, la perturbation visuelle soudaine de quelque chose qui est autrement si constant et inchangé, la page des résultats de recherche Google, est suffisamment déstabilisante pour vraiment vous attirer - certainement une utilisation très astucieuse des actifs de Google.

Étant donné l'accès de Google à (1) votre activité de navigation personnelle et (2) la plateforme sur laquelle vous naviguez sur Internet, ils ont vraiment l'opportunité parfaite de capter des personnes talentueuses, où qu'elles soient, de manière directe et engageante. Ils semblent essayer de déterminer votre niveau de compétence de base et vos domaines de compétence en fonction de votre historique de recherche, puis essayer de vous engager à entrer dans leur pipeline de talents avec ce « jeu », qui, s'il est complété avec succès, pourrait ou non mener à une invitation à un entretien.

La première mention du défi Foobar semble avoir été [ce post](https://news.ycombinator.com/item?id=8588080) sur HackerNews en 2014.

#### Note de bas de page : withgoogle.com

Lorsque vous êtes sur la page du défi Foobar, si vous ouvrez les outils de développement et regardez le DOM, vous verrez que toute la page est dans un iFrame, dont la source est : [https://foobar.withgoogle.com/?eid=...](https://foobar.withgoogle.com/?eid=...). Lorsque j'ai vu cela pour la première fois, j'ai pensé : « Withgoogle.com ? Qu'est-ce que c'est que ça ? »

Encore une fois, ceci est une totale digression par rapport au sujet du défi Foobar, mais il s'avère que le défi lui-même réside sur le « domaine de projet parallèle » de Google appelé « withgoogle.com ». Si vous creusez un peu, vous trouverez d'autres projets assez intéressants. En voici quelques-uns que j'ai rencontrés :

[Paper Signals](https://papersignals.withgoogle.com/), [Quickdraw](https://quickdraw.withgoogle.com/), [CSFirst](https://csfirst.withgoogle.com/), [QiblaFinder](https://qiblafinder.withgoogle.com/), [AIYProjects](https://aiyprojects.withgoogle.com/), [ScienceJournal](https://sciencejournal.withgoogle.com/)