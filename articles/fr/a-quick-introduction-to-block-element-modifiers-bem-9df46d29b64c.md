---
title: Une introduction rapide aux Block Element Modifiers (BEM)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T15:31:39.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-block-element-modifiers-bem-9df46d29b64c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-ffATZSCMSAXm82epzuzxA.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide aux Block Element Modifiers (BEM)
seo_desc: 'By Michael Ozoemena

  Hi there! So you want to gain a better understanding of BEM? I guess if you are
  reading this, you may not know what BEM stands for. In case you don’t, it’s an abbreviation
  for Block Element and Modifier.

  What is BEM?


  BEM is a des...'
---

Par Michael Ozoemena

Bonjour ! Vous souhaitez donc mieux comprendre BEM ? Je suppose que si vous lisez ceci, vous ne savez peut-être pas ce que signifie BEM. Au cas où vous ne le sauriez pas, c'est l'abréviation de [**B**lock **E**lement et **M**odifier](http://getbem.com/).

#### **Qu'est-ce que BEM ?**

> _BEM est une méthodologie de conception qui vous aide à créer des composants réutilisables et à partager du code dans le développement front-end._ — getbem.com

Cela signifie que BEM est un système de méthodes qui vous aide à écrire votre code HTML et CSS de manière à ce qu'il soit simple à réutiliser et à partager avec d'autres parties de votre code.

### **BEM en action.**

Maintenant que vous connaissez la définition de BEM, vous ne savez peut-être pas à quoi il ressemble ou comment il fonctionne. Comme je l'ai mentionné précédemment, BEM est une abréviation, alors examinons chacun de ces mots et ce qu'ils signifient.

#### **Block**

Un « block » fait référence à toute entité qui peut se suffire à elle-même et avoir encore du sens. Des exemples de blocks sont `header`, `input` et `checkbox`. Des exemples de choses qui ne sont **pas** des blocks sont les titres d'en-tête, un élément dans une liste ou une étiquette pour une case à cocher.

Si nous devions supprimer le texte qui étiquette une entrée radio et le mettre seul, il n'aurait plus de sens.

Regardez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Buz2ehP8ELECMdgo4xbKUg.png)

Si la partie qui est encadrée devient séparée en blocks individuels, ils n'auront plus de sens pour l'utilisateur.

Voici une vraie séparation en blocks :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KANbx3IJWy-IzffvXIzRnQ.png)

Si j'enlève l'un de ces blocks et que je le jette, l'autre block aura encore un certain sens pour l'utilisateur. Bien que, dans ce cas, il ne sera pas utile à l'utilisateur car c'est un bouton radio au lieu d'une case à cocher.

Il est important de considérer un block comme toute combinaison (ou une seule balise HTML) de plusieurs éléments (ou d'autres blocks) de manière à ce qu'il _ait du sens pour l'utilisateur lorsqu'il est placé seul._

#### **Elements**

Un élément devrait être un peu plus facile à comprendre maintenant, puisque je l'ai expliqué lorsque j'ai parlé des **Blocks**. Ces parties d'un block qui n'ont aucune signification sémantique en dehors du block sont des éléments.

Regardons ceci à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Buz2ehP8ELECMdgo4xbKUg.png)

Les parties surlignées sont des éléments, car elles aident à définir ce qu'est le block.

Le code pour la capture d'écran ci-dessus ressemblerait à quelque chose comme ceci :

Nous avons trois éléments qui composent le block `option` : `option__text`, `option__radio-button`, `option__note`. Pourtant, nous pourrions changer l'un de ces éléments en un block à part entière :

L'élément `option__note` est maintenant un block `note`. Cela signifie que nous pourrions trouver `note` en dehors du block `option` d'une manière utile pour l'utilisateur.

#### **Modifier**

Un modificateur est un drapeau qui change l'apparence ou le comportement d'un block ou d'un élément. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KQSkWS77mlkLqQTAspoUBA.png)

Les deux boutons sont le même block, mais ils ont l'air différents. Le pouvoir que BEM nous donne nous permet d'utiliser le même block deux fois et de les faire paraître très différents.

Voyons à quoi ressemble le code pour cela :

Par défaut, le bouton est blanc avec un texte bleu. Pour obtenir une variation, nous ajoutons un drapeau `button--green`, qui rend alors le bouton vert avec un texte blanc.

Selon les règles de BEM, notre drapeau `button--green` a un « effet secondaire » qui pourrait prêter à confusion, à savoir la propriété `box-shadow`. Notre drapeau fait quelque chose que son nom ne nous dit pas. Mais ce n'est pas grave, car dans notre petit projet, nous n'aurons jamais un bouton vert avec un `box-shadow`. Si nous en avons un jour besoin, nous pouvons diviser le drapeau :

Maintenant, lorsque nous avons besoin d'un bouton vert avec une ombre de boîte, nous ajouterons uniquement le drapeau `button--green`. La même chose s'applique à la propriété `color`.

### **Conclusion**

BEM est une très bonne façon d'écrire et de structurer votre code HTML et CSS. Ce guide ne couvre pas 100 % de tout ce qui concerne BEM, mais il devrait être suffisant pour vous donner une compréhension solide de la méthodologie. Vous pouvez [en savoir plus sur BEM ici](http://getbem.com/).

J'espère que vous avez appris quelque chose et que vous avez une meilleure compréhension de BEM et de son apparence dans le monde réel. Si c'est le cas, n'hésitez pas à laisser un commentaire et quelques applaudissements.

Vous avez des questions ? Vous pouvez m'envoyer un DM sur Twitter [@THEozmic](https://twitter.com/THEozmic).