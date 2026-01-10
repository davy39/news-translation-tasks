---
title: Comment nous avons donné vie à notre mascotte produit avec AR.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T14:36:04.000Z'
originalURL: https://freecodecamp.org/news/how-we-brought-our-product-mascot-to-life-87830db12ff4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OWm5DKa9eQRjwPEn.png
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: coding
  slug: coding
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Virtual Reality
  slug: virtual-reality
seo_title: Comment nous avons donné vie à notre mascotte produit avec AR.js
seo_desc: 'By Mateusz Tarnaski

  Short answer: using a browser-based Augmented Reality (AR) application. For the
  long answer, read below.

  The idea of playing with AR started as a random interesting experiment. In our company,
  we strive to stay at the edge of the ...'
---

Par Mateusz Tarnaski

Réponse courte : en utilisant une application de réalité augmentée (AR) basée sur un navigateur. Pour la réponse longue, lisez ci-dessous.

L'idée de jouer avec la RA a commencé comme une expérience intéressante aléatoire. Dans notre entreprise, nous nous efforçons de rester à la pointe de la courbe. Nous partageons des nouveautés techniques et de nouvelles technologies les uns avec les autres sur une base semi-régulière. Puisque nous traitons principalement avec des technologies web, le concept de RA dans le navigateur a vraiment décollé.

Puisque la RA est principalement une technologie de divertissement, une application pratique n'était pas évidente pour nous dès le départ. Heureusement, deux choses sans rapport se sont produites en même temps :

* nous venions de créer une mascotte pour notre [produit](https://voucherify.io) — [Hubert](https://uploads-ssl.webflow.com/58fe5d0657dd045f17ae2345/5ab8c85eff9c8b50cbce8b28_voucherify_index_v2_03%20(2).png),
* nous devions faire un stand marketing à [devoxxPL 2018](https://devoxx.pl/)

Nous avons décidé de donner vie à Hubert pendant l'événement, sous la forme d'une application AR pour que les gens puissent jouer avec. Dans nos têtes, les utilisateurs devraient pouvoir :

* rendre Hubert sur un fond de mur dans leurs téléphones
* prendre une photo du modèle rendu
* tweeter la photo (non sujet de cet article)

Le résultat final est disponible sur [glitch.com](https://meet-hubert.glitch.me/), réduit et tourné pour être adapté à une expérience de bureau (vous pouvez également jeter un coup d'œil rapide au [code source](https://glitch.com/edit/#!/meet-hubert?path=contestant_app/index.html:1:0)).

![Image](https://cdn-media-1.freecodecamp.org/images/vvpzSs7qYIixdMDjC8TY4kto2aRREFWKHJ4H)

![Image](https://cdn-media-1.freecodecamp.org/images/lTqvZf927WIlmukzwzK7qt-fN1PWfDDSKPYn)

### Rendre Hubert en temps réel

Nous avons utilisé [AR.js](https://github.com/jeromeetienne/AR.js/) (version de [ce commit](https://github.com/jeromeetienne/AR.js/commit/bfe82a70eae397e02e457801052ca54a3dbd09e2)) comme bloc de construction principal de notre application AR — il regroupe l'accès à la caméra webRTC, la reconnaissance de marqueurs et le rendu de scènes 3D. Nous l'avons aimé principalement parce que vous pouvez avoir une démo de base en environ 20 lignes de code.

Sous le capot, AR.js peut utiliser soit des implémentations three.js ou A-frame pour rendre vos scènes 3D.

* three.js offre un contrôle fin du rendu 3D et est basé sur JavaScript. Vous en avez probablement entendu parler dans le contexte du rendu de scènes 2D et 3D dans le navigateur.
* A-frame est un framework web conçu spécifiquement pour construire des expériences VR et AR. Il a une syntaxe déclarative de type HTML qui est plus déclarative que three.js, mais sacrifie une partie du contrôle en faveur de la facilité d'utilisation.

Nous n'avions pas d'expert en VR ou en 3D (sauf [Mrówka](https://twitter.com/mr_oova), qui a préparé le modèle 3D). Comme la syntaxe déclarative de type HTML d'A-frame nous semblait plus familière, nous avons opté pour A-frame pour faire le rendu.

Ici, vous pouvez voir le code pour rendre Hubert, 30 lignes exactement. Nous avons omis certaines options et ajustements A-frame pour simplifier. Vous pouvez vous référer au dépôt pour tout voir.

Cela nous donne Hubert bien rendu **dans le navigateur web en temps réel.**

### Capturer une photo à tweeter

Malheureusement, nous n'avons pas un seul flux vidéo rendant toute la scène. Il y a la vidéo de votre caméra et une scène 3D rendue. Nous avons rapidement compris que nous devrions capturer une image des deux sources et les assembler pour une belle photo de Hubert.

Prendre des images d'un flux vidéo webRTC est assez simple. [Le meilleur matériel sur le sujet peut être trouvé ici](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Taking_still_photos). Si votre navigateur dispose de l'API appropriée, vous avez besoin de deux éléments :

* une référence à votre balise source <video/>
* un élément <canvas/> de destination dans lequel mettre votre image

Ensuite, il s'agit simplement de dessiner une image 2D de la vidéo vers le canevas. Dans notre cas, les deux sont un peu délicats.

La vidéo que nous utilisons est générée et intégrée par AR.js. Nous ne savions pas comment l'obtenir élégamment, alors nous avons contourné le problème avec une boucle et un sélecteur DOM :

Nous devions également ajuster l'échelle. AR.js ne présente pas le flux vidéo brut à l'utilisateur, ils le mettent à l'échelle pour remplir l'écran sans perdre le ratio d'aspect. Cela signifie que nous devons appliquer la même mise à l'échelle à notre image. Sinon, notre capture d'écran aura "plus" du flux vidéo que ce qui est montré à l'écran. Nous ne voulons pas confondre les utilisateurs ici.

Ce que l'utilisateur voit :

![Image](https://cdn-media-1.freecodecamp.org/images/TqNXPoUowQqneSK0YcqTmW0Zs3IXHPXN8Ivv)

Si nous prenons une image **sans** mise à l'échelle et que nous essayons simplement de copier à partir du point (0,0), nous perdons les marges imposées par AR.js. Cela donne une image totalement différente de ce qui est présenté à l'utilisateur :

![Image](https://cdn-media-1.freecodecamp.org/images/G86uFDWwJ15KiGqWsBEJQdRy-hmnvD9qL8gM)

Disons simplement que nous avons inversé l'ingénierie de la mise à l'échelle et déterminé la boîte de délimitation de ce que l'utilisateur voit :

Pour obtenir ce résultat final (le même que ce qui est présenté en direct à l'utilisateur, à quelques secousses de caméra près) :

![Image](https://cdn-media-1.freecodecamp.org/images/qanFbFOXGrc4HzplknO4E7PwqGzEw4ZVO1M5)

Maintenant, nous devons simplement obtenir Hubert dans l'image. Encore une fois, [l'API](https://github.com/aframevr/aframe/blob/master/docs/components/screenshot.md) pour cela est très simple. Pour capturer une capture d'écran d'une scène A-frame rendue, nous devons obtenir le canevas de la scène. La partie pertinente est copiée dans notre canevas de destination, par-dessus l'image vidéo précédemment prise.

Obtenir la partie pertinente est le point délicat dans notre cas. Grâce à la mise à l'échelle d'AR.js, nous ne pouvons pas simplement obtenir le "perspective" de la scène et l'utiliser. Cela aura l'air trop large ou trop court, selon l'orientation.

Pour le mode paysage (largeur > hauteur), la méthode de mise à l'échelle que nous avons utilisée pour la vidéo fonctionne parfaitement bien.

Pour le mode portrait, cela fonctionne bien sur un PC... Cependant, une fois que vous entrez dans le domaine des appareils mobiles, la mise à l'échelle se brise et la capture d'écran n'a pas l'air belle. Vous obtenez ce Hubert maigre...

![Image](https://cdn-media-1.freecodecamp.org/images/b6iPvi5VULuttWNr0fhEbL3Sb68rBHK9vXex)

...au lieu de notre mascotte adorable et bouillonnante dans toute sa gloire :

![Image](https://cdn-media-1.freecodecamp.org/images/DpNxsKWRiI-WKImCfjd7PZCfg7HAFGk7dB95)

Nous ne sommes toujours pas sûrs de la raison. Nous avons fait l'erreur de ne pas le tester à fond sur des appareils mobiles réels, pensant qu'il fonctionnerait de la même manière que sur la machine de développement. (Oui, nous savons à quel point cela semble mauvais, mais c'est la réalité.) Pendant la conférence, nous avons réussi à trouver la formule pour la mise à l'échelle en portrait et avons introduit une correction :

Ce n'est pas joli. C'est l'une de ces corrections "il est tard, ça marche, laissez-le comme ça". Les valeurs présentées ci-dessus ont produit un résultat satisfaisant et nous en sommes restés là.

Avec cela, nous avons une photo de Hubert dans le monde réel ! Elle peut être récupérée à partir de l'élément canevas de destination et affichée sur la page ou envoyée au serveur pour être tweetée.

### Résumé

La RA dans le navigateur est possible. Même plus, elle est possible sur du matériel mobile de milieu de gamme (en juin 2018). La faire fonctionner sur tous les téléphones et navigateurs est encore un coup de chance, alors ne comptez pas dessus pour des bases d'utilisateurs larges et diversifiées.

Cependant, si vous avez un environnement quelque peu contrôlé, la réalité augmentée sur un téléphone peut être utilisée pour créer des expériences uniques. Celles-ci ne nécessitent pas de matériel spécial ou de stations de travail et c'est un gros, gros plus. Assurez-vous simplement de le tester sur des appareils réels à l'avance.