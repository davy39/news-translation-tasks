---
title: Guide de construction Hackintosh – Pourquoi votre prochain Mac devrait être
  un Hackintosh
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-07T14:41:32.000Z'
originalURL: https://freecodecamp.org/news/why-your-next-mac-should-be-a-hackintosh-311e54b303e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xnSuMACm-2DojLT_MX8ZRA.png
tags:
- name: Apple
  slug: apple
- name: Life lessons
  slug: life-lessons
- name: mac
  slug: mac
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Guide de construction Hackintosh – Pourquoi votre prochain Mac devrait
  être un Hackintosh
seo_desc: 'By Sebastian Dobrincu

  I just finished a 48-hour Hackintosh building marathon. It was a fun experience
  and I learned a lot of new things.

  In this post I’ll try to convince you to choose a Hackintosh as your next main computer.

  Why a Hackintosh

  Perform...'
---

Par Sebastian Dobrincu

Je viens de terminer un marathon de construction de Hackintosh de 48 heures. Ce fut une expérience amusante et j'ai appris beaucoup de nouvelles choses.

Dans cet article, je vais essayer de vous convaincre de choisir un Hackintosh comme votre prochain ordinateur principal.

### **Pourquoi un Hackintosh**

#### Performance

À l'heure actuelle, la gamme actuelle de Mac est assez obsolète en termes de performance. Bien sûr, de nouveaux produits sont juste autour du coin, mais vous pouvez être un pas en avant en construisant votre machine avec les composants que vous voulez (_ou dont vous avez besoin_).

#### Flexibilité

Essayez de changer la RAM sur votre iMac / MacBook. Ce n'est pas une tâche très amusante, n'est-ce pas ?

Et si vous voulez une nouvelle carte graphique plus puissante ? Cela n'arrivera pas.

Remplacer des composants défectueux ? _Appelez Apple._

Overclocker votre CPU ? Oubliez simplement.

Avec un Hackintosh construit sur mesure, vous pouvez toujours remplacer les anciens composants par des nouveaux, et les changer facilement s'ils cessent de fonctionner pour une raison quelconque.

#### Rapport prix-performance

Il va sans dire que ce serait un très mauvais investissement de jeter quelques milliers de dollars sur un Mac Pro de 3 ans lorsque vous pouvez obtenir deux fois la performance avec un ordinateur construit sur mesure.

### Ma construction ?

Lorsque j'ai commencé à choisir mes composants, j'avais quatre choses en tête : je voulais une carte mère entièrement compatible avec macOS, un CPU puissant et overclockable, beaucoup de RAM, et une GPU décente.

Je fais principalement du développement mobile/web, et occasionnellement un peu de Photoshop/Sketch/édition vidéo légère. Voici donc les composants que j'ai trouvés être les meilleurs pour ces tâches :

* **Carte mère** : Gigabyte Z170MX-Gaming 5
* **Processeur** : Intel Core i7-6700K (Overclocké à 4,5 GHz)
* **Mémoire** : G.SKILL Ripjaws V Series 32GB DDR4, 3200Mhz
* **GPU** : Gigabyte GeForce GTX 960, 4GB
* **Alimentation** : Corsair CS650M
* **Refroidisseur CPU** : Corsair H100i v2
* **SSD** : Samsung 850 Evo, 500GB
* **Wi-Fi** : Carte PCI-E TP-Link
* **Boîtier** : BitFenix Prodigy M, Arctic White

Prix total : **≈1350$**

![Image](https://cdn-media-1.freecodecamp.org/images/yXygAND1aLbi7hNkWcYdVrjsSSTkTw6VRjYu)

### À quoi s'attendre

En passant d'un MacBook Pro Retina 2014, la différence de performance est assez notable. La compilation d'une application est maintenant 3 fois plus rapide, les temps d'exportation ont considérablement diminué, et maintenant je peux enfin utiliser mon _Mac_ avec plus de 10 onglets ouverts dans Chrome.

Voici les résultats Cinebench pour vous, les geeks :

![Image](https://cdn-media-1.freecodecamp.org/images/jmIyxicQMRO7wz4201XQQokh631go0e1yGpX)

Et les (wannabe) sexy-shots obligatoires de la construction finalisée :

![Image](https://cdn-media-1.freecodecamp.org/images/2M5JWjCjDtHzv5zLT4akLJLdcSEHPySZz2RX)

![Image](https://cdn-media-1.freecodecamp.org/images/sNLCGI-Bc8zugiwRqo5G8Fc5R2F22QbGv9Qo)

### Attention ! ⚠️

Si vous avez pensé à construire un Hackintosh, vous avez probablement entendu dire que ce n'est pas pour tout le monde.

MacOS a été construit pour supporter uniquement le matériel officiel d'Apple, donc un certain piratage technique sera nécessaire pour le faire fonctionner sur des machines construites sur mesure.

Comme nous le savons tous, les hacks ne sont pas toujours _agréables et propres_, donc ne vous attendez pas à ce que la partie installation du système d'exploitation soit une promenade de santé.

Je suis assez expérimenté en développement logiciel et j'ai construit des ordinateurs auparavant. J'ai quand même dû passer la moitié du temps à ajuster les flags de démarrage, les SSDTs, et à utiliser différentes techniques pour faire démarrer le système dans le menu d'installation.

Croyez-moi, j'ai eu des moments où j'ai abandonné, pensant que les composants devaient être défectueux. J'ai continué à essayer cependant. J'ai cherché dans _chaque_ article/blog/post/vidéo/commentaire/guide, jusqu'à ce que je puisse rassembler les morceaux et le faire fonctionner. Donc, si vous allez retenir une chose de cet article, c'est **ne perdez pas espoir**, aussi cliché que cela puisse paraître.

### Comment commencer

Au cas où je vous aurais convaincu de construire votre propre Mac, la toute première chose que vous voudrez faire est de visiter [tonymacx86.com](http://www.tonymacx86.com/). Cela devrait être votre nouvelle page d'accueil jusqu'à ce que tout soit opérationnel.

Ma recommandation est de consulter leur guide mensuel de l'acheteur, qui vous aidera à choisir les meilleurs composants à jour pour votre configuration.

Une fois que vous avez trié et assemblé vos composants dans votre boîtier, vous voudrez vous lancer dans leur excellent guide d'installation de macOS, qui vous guidera tout au long de ce processus _tricky_.

La communauté est super sympa et toujours prête à aider, alors n'hésitez pas à poser des questions là-bas.

#### Bonne chance dans votre aventure Hackintosh

[Sebastian Dobrincu](http://dobrincu.co) est un entrepreneur, ingénieur logiciel et écrivain, actuellement PDG de [Storyheap](https://storyheap.com). [Suivez-le sur Twitter](http://twitter.com/Sebyddd) pour obtenir plus de mises à jour passionnantes à son sujet.