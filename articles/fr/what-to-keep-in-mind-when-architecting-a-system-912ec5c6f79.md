---
title: Points à garder à l'esprit lors de l'architecture d'un système
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T17:54:27.000Z'
originalURL: https://freecodecamp.org/news/what-to-keep-in-mind-when-architecting-a-system-912ec5c6f79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GRF6gYIhUy5WBdbsqLWm3A.png
tags:
- name: Devops
  slug: devops
- name: software design
  slug: software-design
- name: software development
  slug: software-development
- name: System Architecture
  slug: system-architecture
- name: technology
  slug: technology
seo_title: Points à garder à l'esprit lors de l'architecture d'un système
seo_desc: 'By Ayelet Sachto

  Architecture may sound like a “scary ” or overwhelming subject, but actually, applying
  logic and approaching the problem methodologically simplifies the process drastically.

  When you architect a system, service, or feature, you actua...'
---

Par Ayelet Sachto

L'architecture peut sembler un sujet "effrayant" ou écrasant, mais en réalité, appliquer la logique et aborder le problème de manière méthodique simplifie grandement le processus.

Lorsque vous architectez un système, un service ou une fonctionnalité, vous concevez en réalité une **solution** à un problème dans un **contexte spécifique**. La solution doit répondre à un besoin réel et résoudre le problème **en question**.

Tout au long du texte, j'utiliserai **solution** afin de souligner que les **systèmes, services et fonctionnalités** que nous construisons font partie d'un **flux** plus grand.

![Image](https://cdn-media-1.freecodecamp.org/images/i1p8jGfhA263VAS7AsivCRtMxclqCJV36XT5)

Lorsque vous concevez une solution, pensez à l'ensemble du flux environnemental que vous affectez.

* Pensez à ce qui se passe avant que les données n'atteignent votre code
* Ce qui déclenche votre fonctionnalité ou service
* Qui l'envoie ?
* Est-ce quelque chose d'automatique ?
* Est-ce un utilisateur ?

Cela vous aidera également à réfléchir aux tests et aux cas limites que vous souhaitez aborder, à ce qui se passe après, qui l'utilisera et comment.

#### 1. Comprendre le problème

Commencez par comprendre le problème en question et comprenez vos limites. Ne vous optimisez pas pour un futur inconnu, concentrez-vous sur la situation actuelle et surtout, **ne faites pas de suppositions**. Ne vous limitez pas par des exigences qui n'existent pas.

> Assurez-vous d'avoir toutes les informations nécessaires pour comprendre le problème, n'ayez pas peur de faire des recherches, Google est votre ami ;)

![Image](https://cdn-media-1.freecodecamp.org/images/w9FZSfuNF8PsaTT9F8Puxl4mqP1gcDKVTEbI)
_Photo par [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### 2. Comprendre vos limites et établir des priorités

L'architecture de solution est toujours un compromis entre différentes préoccupations, telles que la résilience, la sécurité, l'intégrité des données, le débit, la scalabilité, la performance et bien sûr le coût.

> Pensez à la valeur par rapport à la friction

Comprenez vos contraintes. Quels sont vos **impératifs**. Si vous avez une équipe produit, travaillez avec eux afin de comprendre le besoin commercial, l'impact et les SLA. Cela vous aidera à mieux comprendre vos considérations et limitations.

Utilisez les **données** pour établir des **priorités**, évitez les suppositions lorsque cela est possible et soyez guidé par les données.

* Combien d'utilisateurs ?
* Nombre de requêtes ?
* Taille des requêtes ?

Testez votre service afin d'estimer les ressources nécessaires.

> Assurez-vous de prendre en compte le taux maximum que vous souhaitez supporter et pas seulement la moyenne (regardez le pourcentage par rapport à la moyenne).

Pensez **à** résoudre le problème et pas seulement **comment** le résoudre. Pensez d'abord à la solution et seulement après à l'implémentation. Lorsque vous vous libérez de l'attente de savoir à quoi la solution **devrait** ressembler, vous comprenez qu'une solution peut être fournie sous de nombreuses formes. Cela peut être un système, un service, une fonctionnalité, un processus ou même de la documentation.

#### 3. Posez la question POURQUOI ?

Remettre en question les gens et même vous-même peut parfois être frustrant. Mais poser **pourquoi** peut vous aider à résoudre le vrai problème, comprendre les exigences obligatoires et vos limites, et peut vous aider à éviter des erreurs et comprendre la motivation du côté commercial.

* Pourquoi est-ce un vrai problème ?
* Pourquoi devrait-ce être fait comme cela ?
* Pourquoi cela fonctionne-t-il comme cela aujourd'hui ?

> Remettez-vous en question et posez des questions. Cela vous aidera à prendre de meilleures décisions et à trouver de meilleures solutions.

![Image](https://cdn-media-1.freecodecamp.org/images/9T5m8DCeqFgZhYxrTs1XjV5MMWIWK42xILAl)
_Photo par [Unsplash](https://unsplash.com/@emilymorter?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Emily Morter</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### 4. Votre solution n'est pas dans le vide

Le contexte est important. Une startup de 4 personnes qui doit fournir un MVP et est limitée par les fonds résoudra et devrait résoudre un problème différemment d'une équipe dans une grande organisation qui doit créer un produit durable qui devra être maintenu par plusieurs équipes.

En revenant à ma première déclaration, après avoir compris le problème, pensez au contexte.

* Quels sont les outils à votre disposition ?
* Faites-vous partie d'une grande organisation ?
* Y a-t-il des limitations telles que le temps ou l'argent ?
* Qui maintiendra la solution ?

Pensez à ce qui est bon pour **votre** situation, définissez ce que signifie _prêt pour la production_ pour **vous**, et s'il doit être hautement disponible (HA). Pensez au [ROI](https://en.wikipedia.org/wiki/Return_on_investment). Devriez-vous aborder les cas limites ?

* Comment concevriez-vous une solution qui retournerait des valeurs depuis une base de données ?
* Et si je vous disais qu'elle ne serait utilisée qu'une fois par semaine jusqu'à la fin de l'année. Cela changerait-il votre réponse ? Cela affecterait-il la conception ?
* Si vous avez 1 jour pour construire une solution, serait-elle la même que si vous aviez un mois ?

**Pensez à la croissance**. Pour différentes solutions et différentes entreprises, la croissance signifie différentes choses. Cela peut être du point de vue de l'**échelle**, comme supporter la croissance d'utilisateurs supplémentaires. Cela peut aussi être du point de vue de la **fonctionnalité**, où votre solution devrait être **flexible** pour permettre à d'autres développeurs d'ajouter/modifier des fonctionnalités avec facilité.

#### 5. Coût

En tant qu'ingénieurs et développeurs, nous ne nous arrêtons parfois pas pour penser au coût de nos solutions et services. D'après mon expérience, cela est surtout dû à un manque de sensibilisation et non à une volonté.

Lorsque nous sommes à l'université, nous sommes "bombardés" de préoccupations de performance et de complexité, et on nous apprend à penser à l'efficacité de la solution. Mais lorsque nous concevons un produit qui sera utilisé, nous devons également penser à l'efficacité en termes de coût. Vous pouvez construire un service stable et fiable qui apporte de la valeur, mais si son ROI n'est pas élevé ou si votre entreprise ne pourra pas se permettre le coût, il sera abandonné au profit d'autres alternatives.

> N'oubliez pas, la performance et l'infrastructure ne sont pas gratuites.

#### 6. Le déploiement en production n'est que le début

Un concept important qui est parfois négligé est la **maintenance**. Notre système ou service est-il stable et facile à maintenir, déboguer, résoudre les problèmes et corriger ?

Le déploiement en production n'est que le début de notre solution. Assurez-vous qu'elle peut être facilement maintenue, assurez-vous qu'elle est prête pour la production et peut servir du trafic et des utilisateurs réels. Lorsque vous développez votre solution, pensez à la surveillance de bout en bout, en vous concentrant sur la surveillance de l'application par rapport à l'utilisation, et assurez-vous d'ajouter des journaux et de la documentation.

> Lorsque vous concevez votre solution, pensez à une conception simple et facile à maintenir, autant que les exigences le permettent, bien sûr.

En tant que développeurs, nous sommes parfois attirés par les nouvelles technologies "clinquantes" et tendance. Arrêtez-vous pour réfléchir si cette technologie est suffisamment mature. Pourrait-elle être maintenue en production ? Un autre stack pourrait-il être plus efficace ou offrir moins de risques ?

#### Conclusion

Pour résumer, si vous voulez architecturer la meilleure solution possible, commencez par comprendre le problème et vos limitations, et connaissez le contexte de la solution que vous essayez de concevoir.

Ensuite, pensez à ce qui arrive à votre solution une fois qu'elle est en place.

Sauf si vous avez des fonds illimités (ce qui n'est jamais le cas), pensez au coût de votre solution et assurez-vous qu'elle est maintenable.

Si vous avez aimé ce que vous avez lu, n'oubliez pas de le liker ci-dessous !

Faites-moi savoir dans les commentaires ❤️ si vous aimez plus de publications sur l'architecture et/ou si vous aimeriez que je plonge plus profondément dans chacun des points ci-dessus.