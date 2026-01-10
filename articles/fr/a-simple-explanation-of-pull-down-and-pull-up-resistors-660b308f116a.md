---
title: 'Fondamentaux du matériel : comment fonctionnent les résistances de pull-down
  et de pull-up'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-17T19:40:27.000Z'
originalURL: https://freecodecamp.org/news/a-simple-explanation-of-pull-down-and-pull-up-resistors-660b308f116a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SMTqmqkvw4LnRckc2Wj9RQ.jpeg
tags:
- name: arduino
  slug: arduino
- name: hardware
  slug: hardware
- name: Internet of Things
  slug: internet-of-things
- name: Makers
  slug: makers
- name: technology
  slug: technology
seo_title: 'Fondamentaux du matériel : comment fonctionnent les résistances de pull-down
  et de pull-up'
seo_desc: 'By Taron Foxworth

  If you’ve ever wired up a button to an Arduino, you’ve come across this diagram:


  At first, this can be confusing. My first thoughts: “Why do I need a resistor? I
  just want to it to tell me whether the button is being pressed.”

  Afte...'
---

Par Taron Foxworth

Si vous avez déjà câblé un bouton à un Arduino, vous êtes tombé sur ce diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/5z3GVJwnEtxRQZnrIeMa6806A0l45ZDHoLLc)

Au début, cela peut être déroutant. Mes premières pensées : « Pourquoi ai-je besoin d'une résistance ? Je veux simplement qu'il me dise si le bouton est enfoncé. »

Après beaucoup de lectures, il n'y avait pas d'explication simple.

### Que se passe-t-il ici

![Image](https://cdn-media-1.freecodecamp.org/images/lnCBI4aQPD72ryakAoXRZOOIscOKzO1TN8T-)
_Diagramme 1_

Dans ce bouton — AKA un interrupteur — les fils sont en forme de « H ». Mais le milieu n'est pas connecté — ou le circuit n'est pas connecté — jusqu'à ce que nous appuyions sur le bouton.

En réalité, nous voulons lire depuis l'Arduino un `0` lorsque rien n'est connecté et un `1` lorsque le bouton est enfoncé.

Sur l'Arduino, cela s'appelle General Purpose Input Output ([GPIO](https://en.wikipedia.org/wiki/General-purpose_input/output)).

Donc, nous pouvons faire quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ei-WY10bPEXDJh5eHRZ8VW0K1Xp0E-fWPQz5)
_Diagramme 2_

Nous connectons le positif (5v, 3.3V, ou VCC) au côté gauche du circuit.

Maintenant, lorsque le bouton est enfoncé, le GPIO lira un `1`, et tout est bon.

![Image](https://cdn-media-1.freecodecamp.org/images/WjBnoryrJcaJusAFgohNgpnKrR0mKXYI7fmd)
_Diagramme 3_

Eh bien, non. Regardons à nouveau le Diagramme 2 :

![Image](https://cdn-media-1.freecodecamp.org/images/1T7hhKBigZliDdNhgut-kKK8KMmgId1jEAEv)
_Diagramme 2_

Nous voulions un `0` lorsque rien n'est connecté, mais comment pouvez-vous garantir cela ? Actuellement, il n'y a aucun moyen de garantir que le GPIO soit `0`.

Il y a aussi des fréquences électromagnétiques dans l'air qui pourraient tirer votre GPIO vers `0` ou `1`. Cela pourrait même fluctuer entre les deux ! Ainsi, nous ne pouvons pas être sûrs qu'il s'agit d'un `0` (je suis si mauvais en jeux de mots). Cela est également connu comme un `0` logique.

Une façon d'obtenir un `0` logique est de relier la broche à la masse :

![Image](https://cdn-media-1.freecodecamp.org/images/mZLL1wlSMz6ReTNeJZDAQMaIOVnkOTrg5qqY)

Hourra ! Maintenant, c'est un zéro logique garanti. En appuyant sur le bouton, cela va être `1` maintenant. N'est-ce pas ?

Eh bien, non.

![Image](https://cdn-media-1.freecodecamp.org/images/sMUiXkmyybe-DrcMuYHb0IqpU3FFLtTYm-uy)

Vous venez de créer un [court-circuit](https://en.wikipedia.org/wiki/Short_circuit). ?

C'est là que la résistance entre en jeu. Pour éviter un court-circuit, nous devons ajouter une résistance à notre circuit. La résistance garde les choses sous contrôle.

![Image](https://cdn-media-1.freecodecamp.org/images/T3HTmawK4YN37wNqYke-QQdh5EVmFnNY8nec)

[L'électricité empruntera le chemin de moindre résistance.](http://ecmweb.com/content/path-least-resistance) Votre GPIO enregistrera maintenant un `1` lorsque le bouton est enfoncé. Comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yLtF3UnfFhhhZ4Kjdqg81d4MvXqVDsYuCclh)

![Image](https://cdn-media-1.freecodecamp.org/images/msnI0gnXpKvs5h6JuTVHExkeAWJuzxyl7J2x)

Hourra ! Maintenant, nous travaillons avec quelque chose.

Maintenant, regardons l'inverse : les résistances de pull-up. C'est la même chose mais à l'envers. Lorsque le bouton n'est pas enfoncé, le GPIO enregistrera un `1`. Lorsque vous enfoncez le bouton, le GPIO sera `0`.

Lorsque le bouton n'est pas enfoncé, nous avons le GPIO connecté au positif (VCC). Ainsi, tout courant qui s'y trouve sera tiré vers le haut de sorte que le GPIO enregistre un `1` logique.

![Image](https://cdn-media-1.freecodecamp.org/images/zUGnUEh9axrnFyaWOvkUNt1B5uCZxQBewETh)

Il est important de noter ici que l'électricité veut toujours aller à la masse. Donc, lorsque nous enfonçons le bouton, le courant qui circule ira à la masse. Ainsi, tout courant qui aurait pu aller au GPIO l'accompagne, laissant le GPIO à un `0` logique.

![Image](https://cdn-media-1.freecodecamp.org/images/4NW0bqGqmZbUolmRv4LObF5qR8fccQ1z9zl0)

? La Fin.

#### Pourquoi ai-je écrit cela ?

J'ai rejoint [Losant](https://losant.com) en septembre 2016 sans expérience matérielle. Chaque kit de démarrage matériel vous donne un bouton sans explication de ce concept. Espérons que cela aide votre ampoule à s'allumer aussi. ?

Cela n'a fait qu'effleurer la surface. Si vous voulez creuser plus profond, consultez ces ressources :

[**Pull-up Resistors - learn.sparkfun.com**](https://learn.sparkfun.com/tutorials/pull-up-resistors)
[_Une autre chose à souligner est que plus la résistance de pull-up est grande, plus la broche est lente à répondre à..._learn.sparkfun.com](https://learn.sparkfun.com/tutorials/pull-up-resistors)

J'adore les retours. Alors, s'il vous plaît, faites-moi savoir si cela pourrait être amélioré. **Si j'ai complètement manqué la balle sur ce coup, [faites-le moi savoir](http://twitter.com/anaptfox)!** J'adorerais le rendre meilleur pour les autres.