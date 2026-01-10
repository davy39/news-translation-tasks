---
title: Comment concevoir une expérience d'achat qui crée des habitudes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-16T16:07:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-a-habit-forming-shopping-experience-af7748402e90
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VG_TGt0PQnEQ12zSkAksTw.jpeg
tags:
- name: ecommerce
  slug: ecommerce
- name: Product Design
  slug: product-design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment concevoir une expérience d'achat qui crée des habitudes
seo_desc: 'By Mohammed Bilal

  Designing for e-commerce is an unforgiving task. Consumers — especially those in
  India — are inherently price-conscious. From mobile phone accessories to televisions,
  the cheapest listing wins.

  Whether it’s Flipkart, Amazon, or Snap...'
---

Par Mohammed Bilal

Concevoir pour le commerce électronique est une tâche impitoyable. Les consommateurs — surtout ceux en Inde — sont intrinsèquement [sensibles aux prix](http://www.livemint.com/Money/3a6pTo1Zor0fw6lY0kNKZP/Those-who-forget-Indian-consumers-are-priceconscious-pay-a.html). Des accessoires de téléphone mobile aux téléviseurs, la liste la moins chère gagne.

Que ce soit Flipkart, Amazon ou Snapdeal, le prix est la principale chose qui compte. Cela laisse très peu de place pour s'appuyer sur la fidélité.

Cela a laissé Flipkart avec un problème extrêmement intéressant à résoudre : comment créer des clients fidèles ? Comment construire une expérience d'achat qui aiderait à freiner le comportement axé sur la chasse aux bonnes affaires et la commodité ?

Pour maintenir l'activité, les plateformes de commerce électronique **dépendent d'événements périodiques** allant des soldes saisonniers/festifs, des soldes de liquidation, des soldes thématiques, etc., où les vendeurs parviennent à un accord pour offrir certaines réductions sur leurs listes.

Pour mettre mon organisation en contexte, en 2015, Flipkart a vendu des marchandises d'une valeur de 300 millions de dollars lors des "Big Billion Days", un événement de vente de cinq jours très important pour l'activité de Flipkart. Lors de la première heure de la vente, Flipkart a vendu environ 500 000 produits — avec presque 140 commandes par seconde, dans 3 200 villes et villages à travers l'Inde.

Mais la vie n'est pas toujours rose — même pour les géants du commerce électronique. Flipkart voit une augmentation du **nombre de désinstallations** juste après la fin de ces événements de vente — un **taux de rétention** d'environ 30 % en moyenne, année après année depuis 2014. Les utilisateurs n'utilisent pas souvent l'application mobile Flipkart une fois la vente terminée, ce qui suggère également les contraintes de stockage auxquelles sont confrontés les utilisateurs mobiles indiens. Ils choisissent de garder des applications comme Facebook, WhatsApp et YouTube, auxquelles ils sont plus habitués, mais pas Flipkart.

Ce qui nous a amenés à creuser un peu plus profondément comment différentes catégories d'applications se comportent en termes de fidélité des clients :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ctFffUcWoTTPwWFR8aXC1Q.png)

Cela nous a donné à moi et à Rahul, qui a travaillé sur ce projet chez Flipkart, suffisamment de contexte pour nous demander : **Qu'est-ce qu'il faut pour construire des produits qui créent des habitudes ?**

### Notre approche

Les habitudes sont des actions effectuées avec peu ou pas de pensée consciente. Les recherches suggèrent que ~40 % de ce que nous faisons chaque jour est une question d'habitude. L'industrie du jeu vidéo utilise le concept de `hook` pour garder l'utilisateur investi et engagé dans leurs produits.

Le hook commence par un déclencheur dans l'environnement de l'utilisateur. Nous sommes familiers avec les **déclencheurs externes** lorsque nous voyons des notifications de degrés variés sur nos produits. Mais ce qui est plus critique pour former des habitudes durables, ce sont les **déclencheurs internes.**

Les déclencheurs internes les plus fréquents sont émotionnels, et plus souvent qu'autrement, ils sont négatifs. Ainsi, les utilisateurs essaient de changer cette humeur négative en parcourant Instagram ou en regardant des vidéos [drôles](https://www.youtube.com/watch?v=f8uK_mWnbr4) en ligne.

Nous faisons de nombreuses activités involontaires au cours de la journée pour échapper à l'état émotionnel négatif, et c'est là que nous avons pensé que nous pourrions expérimenter en montrant des offres pertinentes pour l'utilisateur sur Flipkart.

L'utilisateur céderait — anticipant une **récompense** — et s'engagerait ainsi/**investirait** dans le produit/l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b-cUkPvUbMivM8hKgVBy0g.png)

Chaque matin, lorsque nous nous réveillons, la plupart d'entre nous ressentent au moins une émotion forte : une **peur de manquer quelque chose**. Si vous vous surprenez à vérifier vos emails, Facebook ou Twitter dès le matin, alors c'est peut-être ce qui se passe dans votre esprit.

> _Le mot **FOMO (Fear of missing out)** a en fait été ajouté à l'Oxford English Dictionary en 2013. Bien que la terminologie n'ait été ajoutée que récemment à notre lexique, l'expérience du FOMO n'est pas nouvelle._

Nous avons vu une opportunité de créer des déclencheurs internes et d'initier le hook, en plus de nos déclencheurs externes.

### Notre solution

Nous avons essayé de lister divers archétypes de déclencheurs externes qui pourraient attirer l'attention des consommateurs indiens dans le contexte des achats. **Pour créer un moyen de déclencheurs externes, nous devions penser à un modèle d'interface utilisateur qui pourrait permettre cela.**

Nous avons observé que l'approche traditionnelle des notifications ne fonctionnerait pas très bien en raison de nombreux problèmes inhérents, notamment une [cécité aux notifications](https://leftrightlabs.com/notification-blindness-can-be-deadly/) croissante parmi les consommateurs.

#### 1. Digest quotidien : `**Flux infini VS Flux fini**`

Nous avons pensé à créer un **digest quotidien** d'un nombre fini de produits et à actualiser le digest une fois par jour. Cela signifiait que nous devions nous éloigner de notre flux infini de produits sans fin, qui laisse souvent l'utilisateur en **paralysie de décision.**

Cela signifiait que nos moteurs de recommandation devaient être reconstruits à partir de zéro. Flipkart est une place de marché qui propose plus de 30 millions de produits dans plus de 80 catégories. Cette variété signifie que nous devons mapper ces produits aux intérêts des utilisateurs. Cela nous a conduit au prochain défi : la pertinence.

#### 2. Pertinence

Il était évident que la personnalisation de ce flux fini avec des produits pertinents serait une bouée de sauvetage pour l'engagement de notre application. Les [systèmes de recommandation traditionnels fonctionnent](http://rejoiner.com/resources/amazon-recommendations-secret-selling-online/) en cristallisant l'historique d'utilisation et en [trouvant des motifs](https://www.theverge.com/2016/2/17/11030200/netflix-new-recommendation-system-global-regional).

Mais pour nous, cela ne résoudrait que partiellement le problème. Nous avons donc [interviewé quelques utilisateurs](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) pour comprendre quand et comment ils font leurs achats en ligne. Nous avons appris que nos utilisateurs font leurs achats dans le cadre de deux thèmes principaux :

1. **Intention** : lorsqu'il y a un besoin fort, où l'utilisateur effectue une recherche ciblée. C'est là que nous devons rendre notre recherche beaucoup plus clinique pour capturer l'intention et servir le besoin.
2. **Intérêt** : À l'autre extrémité du spectre, il y a le "lèche-vitrines" pour des produits que l'utilisateur aime. Et pas seulement des produits — il y a des thèmes dans nos vies qui nous poussent (parfois même nous inspirent) à acheter. Peut-être êtes-vous soucieux de votre forme physique, ou vous êtes un passionné de voyage, ou vous aimez la marque Nautica, ou vous êtes récemment devenu parent, ou le mariage de votre ami approche. C'est là que nous devions recueillir les intérêts de l'utilisateur de manière approfondie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uk6qufMgYrHpqb15a1X1Dg.png)

#### 3. Réseau de choses

Lorsque nous réduisons des millions de produits à un flux digestible de quelques produits, nous devons réfléchir à la manière de rendre les produits de diverses catégories accessibles à l'utilisateur. Chez Flipkart, notre avantage concurrentiel est notre vaste et profond inventaire de produits.

Lorsque nous avons profiler les utilisateurs, nous avons vu que les achats se font par thèmes (encore une fois, intention et intérêt). Nous avons décidé que nous pourrions attribuer un ensemble de méta-balises à chaque produit, et chaque balise serait un nœud dans un nuage d'ensembles de produits thématiquement liés.

Au lieu de regrouper et diviser par catégories, nous avons retourné les tables. Nous avons regroupé les produits en divers thèmes et histoires.

Ce réseau peut être une combinaison de nœuds organiques et inorganiques. Cela signifie pousser du contenu intéressant basé sur des événements vers l'utilisateur. Et il se développe différemment pour chaque utilisateur. Ci-dessous se trouve l'un de ces réseaux que nous avons conçu pour le voyage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3SDpq1RjBs2VTh7newZOmA.png)

### Conception

Après quelques sessions de brainstorming et d'esquisses de divers composants, j'ai travaillé sur la création de prototypes interactifs sur Pixate tout en mettant les maquettes ensemble sur Sketch.

Voici une courte vidéo qui présente la solution de conception :

#### Présentation

* Il existe de nombreuses façons de présenter l'UX d'une application, mais je pense personnellement qu'une **courte vidéo** centrée sur une histoire d'utilisateur est la forme la plus pratique et complète d'explication.
* Écrivez un **script** qui est un mélange de l'ensemble des histoires d'utilisateurs. Passez un temps décent à l'affiner. Faites-le valider par les autres parties prenantes pour vous assurer que l'épine dorsale de la vidéo est bien en place.
* Une fois le script prêt, commencez à assembler les **prototypes interactifs**, dans la bonne séquence. Il est recommandé d'enregistrer le même sur un appareil pour refléter l'expérience réelle.
* Ensuite vient le **commentaire vocal**. J'aime que le ton de la voix soit un peu plus franc par rapport aux commentaires vocaux publicitaires traditionnels. Vous pouvez engager un artiste de commentaire vocal sur [Fiverr](http://www.fiverr.com).

### Esquisses

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_FKTB7kzEi0yBHN90lM4w.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Di-Kns3WquyknU54-ce4Kg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NNipQG4vELVThEA8kPggpg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fskz6eUSVsDIGDj9ELM0gQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*sRPzsS7W87U86RNA0YGVeA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*md1BrrczBA9k2pjrAdAAnw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IEmS61tzY1cagSl5GR8Sfg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*9W9GnM7k2ZIyr0UGDEOQ2A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CVGaBWB8hf-gAzntGbdwHQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*o8Ak0VEoodLHNsjm9RKr8g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jsg_CbqSkWJLqnwMSSMRhA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*xyywS8vmrLM6suZMc4LFKg.jpeg)

### Interface utilisateur

#### Prototypes

![Image](https://cdn-media-1.freecodecamp.org/images/0*gaT3Wq7L9-9-pHjh.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*b31hiO4ynbDLRrXWEFF4aQ.png)

`**Maquettes**`

![Image](https://cdn-media-1.freecodecamp.org/images/1*HJxC9wTVpkktUlxBoy2Nkw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*09HZ87-OKDDg7bBE_9cK0g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZM6AZkwdpx041rIbObGXJg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*DfuTy-C40WofEI4Mrrme8w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*KEIBdwN9-eJh-BdbtQ_VIg.png)

#### Tout cela a conduit à...

Nous avons partagé ce processus de réflexion parmi diverses équipes chez Flipkart pour obtenir des commentaires, et lentement, nous avons vu beaucoup adhérer à l'idée de la productisation du commerce électronique. Nous avons bientôt officialisé ces efforts en créant une équipe de 4 designers pour travailler exclusivement sur de tels **projets ambitieux** chez Flipkart.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EQ_UUGaKHCl8ajOiJqQqBw.jpeg)
_Skunkworks_

Merci d'avoir lu.

_Bilal est un designer de produits basé à Bangalore, en Inde. Il accorde une grande valeur à une approche basée sur les processus pour concevoir des solutions. Il pratique le design en tant qu'exécutant full-stack et le prototypage est l'une de ses forces. La formation en ingénierie de Bilal en informatique l'aide à concevoir de manière pragmatique et à avoir des collaborations efficaces avec les développeurs._

![Image](https://cdn-media-1.freecodecamp.org/images/1*-SRT8je-xiHvkuIQGX36sg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lt64aXWMFd5gf6_h_fXy8w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BrUoUgoEDS2212DqC-wMwA.png)