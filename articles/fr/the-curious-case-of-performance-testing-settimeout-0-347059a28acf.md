---
title: Le cas étrange des tests de performance de setTimeout(0)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T07:40:12.000Z'
originalURL: https://freecodecamp.org/news/the-curious-case-of-performance-testing-settimeout-0-347059a28acf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ybjNWDE73_POdC0dIFOZ_Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Le cas étrange des tests de performance de setTimeout(0)
seo_desc: 'By Netta Bondy

  (For full effect, read in a husky voice while surrounded by a cloud of smoke)


  _Image by [Studio-Dee on Pixabay](https://pixabay.com/en/grain-retro-forties-trepidation-3026099/"
  rel="noopener" target="blank" title=").

  It all began on a...'
---

Par Netta Bondy

#### (Pour un effet complet, lisez avec une voix rauque tout en étant entouré d'un nuage de fumée)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ybjNWDE73_POdC0dIFOZ_Q.jpeg)
_Image par [Studio-Dee sur Pixabay](https://pixabay.com/en/grain-retro-forties-trepidation-3026099/" rel="noopener" target="_blank" title=")._

Tout a commencé un jour d'automne gris. Le ciel était nuageux, le vent soufflait, et quelqu'un m'a dit que `setTimeout(0)` créait, en moyenne, un délai de 4 ms. Ils affirmaient que c'était le temps nécessaire pour retirer le callback de la pile, le placer dans la file d'attente des callbacks et le remettre sur la pile. J'ai trouvé cela suspect (c'est ici que vous m'imaginez en noir et blanc avec un cigare dans la bouche). Étant donné que le pipeline de rendu doit s'exécuter toutes les 16 ms pour permettre des animations fluides, 4 ms me semblaient être une longue période. Une très longue période.

Quelques tests naïfs dans les devtools avec `console.time()` l'ont confirmé. Le délai moyen sur 20 exécutions était d'environ 1,5 ms. Bien sûr, 20 exécutions ne constituent pas un échantillon suffisant, mais maintenant j'avais un point à prouver. Je voulais exécuter des tests à plus grande échelle pour obtenir une réponse plus précise. Je pourrais alors, bien sûr, aller agiter cela sous le nez de mon collègue pour prouver qu'il avait tort.

Pourquoi faisons-nous ce que nous faisons sinon ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHoVJS_SNxeV0hAdKgxnig.jpeg)
_Séance photo Film Noir — Portland Lightist par [Randy Kashka sur flickr](https://www.flickr.com/photos/randykashka/5277322486" rel="noopener" target="_blank" title=")._

### La méthode traditionnelle

Dès le début, je me suis retrouvée dans une situation délicate. Pour mesurer le temps nécessaire à l'exécution de `setTimeout(0)`, j'avais besoin d'une fonction qui :

* prenait un instantané de l'heure actuelle
* exécutait `setTimeout`
* quittait immédiatement afin que la pile soit libre et que le callback planifié puisse s'exécuter et calculer la différence de temps
* **et j'avais besoin que cette fonction s'exécute un nombre suffisamment grand de fois pour que les calculs soient statistiquement significatifs**

Mais la structure de base pour cela — la boucle for — ne fonctionnerait pas. Parce que la boucle for ne vide pas la pile tant qu'elle n'a pas exécuté chaque itération, le callback ne s'exécuterait pas immédiatement. Ou, pour le dire en code, nous obtiendrions ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*nyT20-4_HmK0z2ir)
_La boucle s'exécute 10 fois, et ce n'est qu'alors que les callbacks sont replacés sur la pile_

Le problème était inhérent — si je voulais exécuter `setTimeout` plusieurs fois automatiquement, je devrais le faire depuis un autre contexte. Mais, tant que je m'exécutais depuis un autre contexte, il y aurait toujours un délai supplémentaire entre le moment où je commençais le test et le moment où le callback s'exécutait.

Bien sûr, je pourrais m'en sortir comme certains de ces détectives bons à rien, écrire une fonction qui fait ce dont j'ai besoin, puis la copier et la coller 10 000 fois. J'apprendrais ce que je voulais savoir, mais l'exécution serait loin d'être élégante. Si j'allais frotter cela sous le nez de quelqu'un d'autre, je préférerais de loin le faire autrement.

Puis une idée me vint.

### La méthode révolutionnaire

Je pourrais utiliser un web worker.

Les web workers s'exécutent sur un thread différent. Donc, si je place la logique `setTimeout` dans un web worker, je pourrais l'appeler plusieurs fois. Chaque appel créerait son propre contexte d'exécution, appelant `setTimeout`, et quittant immédiatement la fonction pour que le callback puisse s'exécuter. J'avais hâte de faire un peu de travail avec les web workers.

Il était temps de passer à mon fidèle [Sublime Text](https://www.sublimetext.com/).

J'ai commencé par tester les eaux. Avec ce code dans `main.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/0*jbunaO2AqtWGW2PN)

Un peu de plomberie ici pour préparer le test réel, mais initialement je voulais juste m'assurer que je pouvais communiquer correctement avec le web worker. Donc voici le `worker.js` initial :

![Image](https://cdn-media-1.freecodecamp.org/images/0*iAl6qOeph4ww82VV)

Et bien que cela ait fonctionné à merveille — cela a produit des résultats que j'aurais dû prévoir, mais que je ne prévoyais pas :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5C_QAUCW5q3EDuc818jG1w.jpeg)
_C'est sûr que c'est asynchrone…_

Étant si habituée à la synchronisation en JS, je ne pouvais m'empêcher d'être surprise par cela. Le premier moment où je l'ai vu, mon cerveau a enregistré un bug. Mais, puisque chaque boucle configure un nouveau web worker et qu'ils s'exécutent de manière asynchrone, il est logique que les nombres ne soient pas imprimés dans l'ordre.

Cela m'a peut-être surprise, mais cela fonctionnait comme prévu. Je pouvais continuer avec le test.

Ce que je voulais, c'est que la fonction `onmessage` du web worker enregistre `t0`, appelle `setTimeout`, puis quitte immédiatement afin de ne pas bloquer la pile. Je pourrais, cependant, ajouter des fonctionnalités supplémentaires à l'intérieur du callback, après avoir défini la valeur de `t1`. J'ai ajouté mon `postMessage` dans le callback, pour qu'il ne bloque pas la pile :

![Image](https://cdn-media-1.freecodecamp.org/images/0*TMgPjObYkeuTVx9T)
_worker.js_

Et voici le code `main.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/0*HvWvrei9KcHE3PQt)

Cette version a un problème.

Bien sûr — puisque je suis nouvelle dans les web workers, je n'y avais pas pensé au début. Mais, lorsque plusieurs exécutions de la fonction continuaient à imprimer `0`, j'ai compris que quelque chose n'allait pas.

Lorsque j'ai imprimé les sommes depuis `onmessage`, j'ai obtenu ma réponse. La fonction principale avançait de manière synchrone et n'attendait pas le message du worker pour revenir, donc elle calculait la moyenne avant que le web worker n'ait terminé.

Une solution rapide et sale consiste à ajouter un compteur et à effectuer le calcul uniquement lorsque le compteur a atteint la valeur maximale. Voici donc le nouveau `main.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/0*9DWX6pzoYDWMSn7O)

Et voici les résultats :

`main(10)` : `0.1`

`main(100)` : `1.41`

`main(1000)` : `13.082`

Oh. Mon. Eh bien, ce n'est pas génial, n'est-ce pas ? Que se passe-t-il ici ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*dRmCZYxnq3k8o7_v)

J'ai sacrifié les tests de performance pour jeter un coup d'œil à l'intérieur. Je enregistre maintenant `t0` et `t1` lorsqu'ils sont créés, juste pour voir ce qui se passe là.

Et les résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Rpu-snzwyLtCXJa0)

Il s'avère que mon attente que `t1` soit calculé immédiatement après `t0` était également mal fondée. **Basiquement, le fait que rien concernant les web workers ne soit synchrone signifie que mes hypothèses les plus basiques sur le comportement de mon code ne sont tout simplement plus valables.** C'est un angle mort difficile à voir.

Non seulement cela, mais même les résultats que j'ai obtenus pour `main(10)` et `main(100)`, qui m'avaient initialement rendue très heureuse et satisfaite, n'étaient pas quelque chose sur lequel je pouvais compter.

L'asynchronisme des web workers en fait également un proxy peu fiable pour le comportement des choses dans notre pile régulière. Ainsi, bien que la mesure des performances de `setTimeout` dans un web worker donne des résultats intéressants, ceux-ci ne répondent pas à notre question.

### La méthode du manuel

J'étais frustrée… ne pouvais-je vraiment pas trouver une solution vanilla JS qui soit à la fois élégante et prouve que mon collègue avait tort ?

Puis j'ai réalisé — il y avait quelque chose que je pouvais faire, mais je ne l'aimerais pas.

Je pourrais appeler `setTimeout` de manière récursive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7b2gfSohmz3wtHZg4Jw59w.png)

Maintenant, lorsque j'appelle `main`, cela appelle `testRunner` qui mesure `t0` puis planifie le callback. Le callback s'exécute ensuite immédiatement, calcule `t1` puis appelle à nouveau `testRunner`, jusqu'à ce qu'il ait atteint le nombre souhaité d'appels.

Les résultats de ce code étaient particulièrement surprenants. Voici quelques impressions de `main(10)` et `main(1000)` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1uKttvNJZrOzoSLUBxua7Q.png)

Les résultats sont significativement différents lorsque l'on appelle la fonction 1 000 fois par rapport à 10 fois. J'ai essayé cela à plusieurs reprises et obtenu largement les mêmes résultats, avec `main(10)` arrivant à 3-4 ms, et `main(1000)` dépassant 5 ms.

Pour être honnête, je ne suis pas sûre de ce qui se passe ici. J'ai cherché une réponse, mais je n'ai pas trouvé d'explication raisonnable. Si vous lisez ceci et avez une idée éclairée de ce qui se passe — j'adorerais avoir de vos nouvelles dans les commentaires.

### La méthode éprouvée

Quelque part au fond de mon esprit, je savais toujours que cela en viendrait là… Les choses tape-à-l'œil sont bien pour ceux qui peuvent les obtenir, mais les méthodes éprouvées seront toujours là à la fin. Même si j'ai essayé de l'éviter, je savais toujours que c'était une option. `setInterval`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-WpNKwlsLf0Vz_GUhxuEw.png)

Ce code fait le travail avec une certaine force brute. `setInterval` exécute la fonction de manière répétée, attendant 50 ms entre chaque exécution, pour s'assurer que la pile est libre. Ce n'est pas élégant, mais cela teste exactement ce dont j'avais besoin.

Et les résultats étaient également prometteurs. Les temps semblent correspondre à mes attentes initiales — moins de 1,5 ms.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bLfRyBhL2verNKh7buvhrg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PVVq-8FAzT_VZkYhnxTBKw.png)
_Des résultats similaires sur 10 000 exécutions_

Enfin, je pouvais clore cette affaire. J'avais eu des hauts et des bas, et ma part de résultats inattendus, mais au final, une seule chose comptait — j'avais prouvé qu'un autre développeur avait tort ! C'était suffisant pour moi.

Vous voulez jouer avec ce code ? Consultez-le ici : [https://github.com/NettaB/setTimeout-test](https://github.com/NettaB/setTimeout-test)