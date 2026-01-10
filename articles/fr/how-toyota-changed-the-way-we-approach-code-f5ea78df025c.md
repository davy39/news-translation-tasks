---
title: Comment Toyota a changé notre façon d'aborder le code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-13T06:12:58.000Z'
originalURL: https://freecodecamp.org/news/how-toyota-changed-the-way-we-approach-code-f5ea78df025c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*gBSCjU9-eEZ_HVtx.
tags:
- name: Product Management
  slug: product-management
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment Toyota a changé notre façon d'aborder le code
seo_desc: 'By Adam Petrie

  As developers we don’t work in vacuums. We’re constantly faced with constraints
  like time, budget, and resources. We’re influenced by priorities outside of our
  teams that impact what we can work on, when, and for how long.

  This is part...'
---

Par Adam Petrie

En tant que développeurs, nous ne travaillons pas dans le vide. Nous sommes constamment confrontés à des contraintes comme le temps, le budget et les ressources. Nous sommes influencés par des priorités extérieures à nos équipes qui impactent ce sur quoi nous pouvons travailler, quand et pour combien de temps.

Cela est particulièrement vrai lorsque nous essayons de développer une réputation pour le support client. Notre capacité à répondre aux besoins du client de manière opportune peut faire la différence entre une relation lucrative et une opportunité manquée.

La qualité du code est souvent la première victime du travail dans ces paramètres. Nous faisons des sacrifices pour économiser du temps et des efforts. Nous prenons des dettes techniques avec la mentalité que, une fois notre deadline atteinte, nous pourrons revenir sur le code et nettoyer notre désordre.

Le seul problème avec cette approche est ce qui se profile juste au-delà de l'horizon : une autre deadline. Puis une autre. Puis une autre.

Avant de nous en rendre compte, nous avons accumulé une dette technique significative. Elle commence à inhiber notre capacité à faire des changements ou à ajouter de nouvelles fonctionnalités. Notre progression ralentit. Notre produit stagne. Les choix que nous faisions pour réussir commencent à devenir la cause de notre échec.

Assez de dette technique peut laisser même les meilleurs développeurs se sentir impuissants, et se demander : où allons-nous à partir de là ?

![Image](https://cdn-media-1.freecodecamp.org/images/wYqzYfx3dKgtDIBxRpAfAnWYhdtdHvNAFkwi)
_Source : [Realwire](http://www.realwire.com/writeitfiles/InspGadget.jpeg" rel="noopener" target="_blank" title=")_

### Nous devons accepter notre réalité

Notre objectif principal est de fournir une valeur commerciale grâce aux efforts de développement. Cela signifie que l'obtention de l'adhésion des parties prenantes pour consacrer une grande partie du temps à réduire la dette technique n'est souvent tout simplement pas une option. Le retour sur investissement pour les efforts de refactorisation à grande échelle est trop faible lorsque le résultat net n'est pas une amélioration tangible du produit.

Les améliorations techniques à plus grande échelle peuvent et doivent être liées à la valeur commerciale chaque fois que possible ; mais cela nécessite beaucoup de coordination et parfois n'est tout simplement pas réalisable. Même dans un scénario idéal, ces efforts sont généralement liés à de nouvelles fonctionnalités et rarement rendent le code existant obsolète de manière à ce que nos désirs de meilleur logiciel soient satisfaits.

Nous devons abandonner l'idée que nous aurons le temps de revisiter nos erreurs et de les corriger sans les pressions externes qui nous ont poussés à les commettre en premier lieu.

Avec cela à l'esprit, comment pouvons-nous améliorer notre code ?

![Image](https://cdn-media-1.freecodecamp.org/images/YYmhcuChwaMqk7wGAC5SFJcVe3NCyCq5PjjR)
_Source : [Behind the Voice Actors](http://statici.behindthevoiceactors.com/behindthevoiceactors/_img/shows/banner_385.jpg" rel="noopener" target="_blank" title=")_

### Un cas pour Kaizen

Une approche Kaizen d'amélioration continue souligne que les changements doivent être petits plutôt que radicaux. Kaizen suggère que les idées doivent venir des travailleurs eux-mêmes avec l'espoir qu'elles seront plus faciles à mettre en œuvre. Kaizen encourage l'appropriation parmi la main-d'œuvre, avec pour objectif d'améliorer la motivation et la construction d'équipe. En ce qui concerne l'amélioration de notre logiciel, ces principes s'appliquent parfaitement.

Le mot « Kaizen » est japonais pour « amélioration ». Il est peut-être le plus célèbre pour être [l'un des deux piliers de la méthode Toyota](http://www.mckinsey.com/industries/automotive-and-assembly/our-insights/still-learning-from-toyota), et est une philosophie qui est construite sur l'« amélioration continue ».

Il est mieux appliqué au six sigma et à la fabrication, mais il a également des applications pratiques dans le monde du logiciel. Chez Flipp, nous utilisons un ensemble de mots similaire (« réinvention constante ») pour décrire l'une de nos valeurs.

Bien qu'il existe [des systèmes spécifiques pour le flux de travail Kaizen appliqué au développement logiciel agile](http://agilean.blogs.com/business_productivity/2010/09/kanban-kaizen-scrum.html), nous appliquons Kaizen comme une philosophie.

### **_Refactoriser au fur et à mesure_**

Chaque fois que vous ouvrez votre éditeur, vous avez l'occasion de faire de la maintenance sur votre base de code. Cela n'a pas besoin d'être glamour ou révolutionnaire, mais si, à chaque changement, vous vous efforcez de laisser le code dans un meilleur état que vous ne l'avez trouvé, la différence cumulative peut être énorme.

En ce qui concerne l'amélioration du code, il existe toutes sortes d'approches différentes et votre succès avec l'une d'entre elles variera en fonction du code et de votre expérience, entre autres facteurs.

Voici quelques-unes des techniques que j'emploie pour essayer d'améliorer constamment toute base de code à laquelle je contribue :

* Corriger les erreurs de lint. Le lint affecte la lisibilité du code et si vous ne pouvez pas lire le code, vous ne pouvez pas espérer le comprendre ou le modifier. Une fois que vous avez terminé une histoire, pourquoi ne pas faire un seul commit pour supprimer le lint existant dans un fichier que vous avez édité ? Cela prend quelques instants à accomplir, mais l'impact peut être significatif.
* Rechercher les odeurs de code faciles à corriger. Sans exploser la portée d'un ticket donné, vous pouvez souvent traiter certains problèmes évidents.
* Commentaires excessifs — Lorsque les commentaires de code décrivent ce qui se passe plutôt que pourquoi, c'est un signe assez évident que des améliorations peuvent être apportées. Le code peut-il être écrit de manière auto-documentée de sorte que les commentaires soient inutiles ?
* Méthodes longues — Les méthodes plus courtes sont plus faciles à lire, éditer, tester et dépanner. Cette méthode de 75 lignes a besoin de votre aide.
* Longues listes de paramètres — Il est raisonnable de supposer que les longues listes de paramètres entraînent une complexité accrue. Tous ces paramètres sont-ils vraiment nécessaires ? Peuvent-ils être combinés en un objet ? Limitez la longueur des paramètres pour réduire la complexité.
* Code dupliqué — Trouvez des moyens de le rendre DRY. La duplication peut-elle être extraite dans une méthode ? Y a-t-il une opportunité pour un objet de service ? Supprimer la duplication aide à la lisibilité et réduit les opportunités d'introduire des erreurs.
* Code mort — Si vous tombez sur du code mort, supprimez-le. Maintenant. Cela améliorera la lisibilité et réduira la taille globale du code.
* Il y a beaucoup d'autres odeurs de code qui peuvent être traitées également. Plus vous êtes familier avec elles, plus vous serez capable de les identifier et de les corriger dans votre propre code.
* Les tests sont aussi du code. Maintenir des tests faciles à lire et décrivant avec précision la fonctionnalité souhaitée rend la refactorisation du code lui-même substantiellement plus facile. Y a-t-il un cas de test qui peut être ajouté ? Les tests peuvent-ils être plus lisibles ? Moins fragiles ? Un test donné teste-t-il la bonne chose ? Des tests améliorés signifient un code amélioré.

En général, posez-vous cette question chaque fois que vous faites un changement : que puis-je faire pour rendre ce morceau de code plus facile à lire, éditer, tester ou dépanner pour la prochaine personne ?

![Image](https://cdn-media-1.freecodecamp.org/images/zNlF8YIxRO1UVc8otW-Jv9VHOO3jobTmmz-0)
_Source : [Wikia](http://vignette1.wikia.nocookie.net/video151/images/1/17/Inspector_Gadget_Netflix_Trailer/revision/latest?cb=20150325202318" rel="noopener" target="_blank" title=")_

### **_Quand trouvons-nous le temps ?_**

Évidemment, le principal défi est le manque apparent de temps pour prendre ces approches pendant la journée de travail régulière. Je suggère de trouver du temps pendant votre routine normale, ou de le prioriser pendant les temps morts.

Par exemple, à condition d'avoir une bonne couverture de tests, vous pourriez facilement effectuer une refactorisation de base au sein d'une classe tout en traitant les critères d'acceptation pour un ticket donné. (Cela prend un peu de pratique, cependant.)

Pour les éléments plus importants, je trouve du temps les vendredis calmes pour revenir sur ou enfin traiter certains problèmes plus importants qui m'ont dérangé. J'ai également travaillé sur de gros travaux au cours de plusieurs semaines, si nécessaire.

En adoptant le bon état d'esprit, vous trouverez les opportunités dont vous avez besoin sans avoir à sacrifier autant de temps que ces tâches nécessiteraient pour un traitement complet comme une histoire régulière.

Si vous améliorez le code, il y aura moins de place pour les effets secondaires non intentionnels du nouveau développement. De plus, vous êtes plus familiarisé avec le code lui-même, donc votre capacité à le modifier sera améliorée à l'avenir également.

### **_Un point à temps en sauve neuf_**

L'effort que vous mettez dans l'amélioration incrémentielle de votre code se multiplie avec le temps.

En refactorisant constamment, vous augmenterez considérablement votre compréhension de la base de code. Lorsque vous comprenez bien le code, vous êtes beaucoup plus efficace pour l'éditer.

De plus, votre capacité à estimer la complexité liée aux nouvelles fonctionnalités est améliorée et vous êtes beaucoup plus fort en matière d'intégration de nouveaux développeurs ou d'aide à votre équipe.

Apprendre quand, quoi et comment refactoriser fait de vous un meilleur développeur. Les techniques que vous emploierez pour refactoriser efficacement sont universelles et vous aideront tout au long de votre carrière.

Enfin, nettoyer votre base de code fait de vous un meilleur membre de l'équipe. Il est presque certain que d'autres personnes de votre équipe ont été prises ou frustrées par les mêmes choses que vous rencontrez. Si vous trouvez un moyen de traiter le point de douleur de quelqu'un d'autre, ils vous en seront reconnaissants.

![Image](https://cdn-media-1.freecodecamp.org/images/fqnMQodmGCb2jrx8mins4Zza6hoVxEDwCJCO)
_Source : [Mental Floss](http://images.mentalfloss.com/sites/default/files/styles/article_640x430/public/4532657169913856.jpeg" rel="noopener" target="_blank" title=")_

### **_Construire des logiciels est difficile_**

Construire de bons logiciels avec un calendrier serré et des ressources limitées est encore plus difficile, mais ce n'est pas impossible.

Nous pouvons apprendre à accepter la réalité dans laquelle nous vivons et nous concentrer sur l'amélioration incrémentielle plutôt que sur l'écriture de code parfait. Alors nous serons mieux à même de maintenir l'agilité dont nous avons désespérément besoin. De cette façon, nous pouvons rester productifs et nos produits peuvent rester compétitifs.

Essayez d'adopter une approche d'amélioration continue dans vos efforts de développement quotidiens. Cela vous aidera à grandir en tant que développeur, à améliorer le moral de votre équipe et, en fin de compte, à augmenter votre capacité à fournir une valeur commerciale.

_Je suis Adam, ingénieur logiciel chez [Flipp](https://flipp.com/). J'ai publié une autre version de ceci sur le [blog d'ingénierie de Flipp](http://eng.flipp.com/a-kaizen-approach-to-code-quality/). Êtes-vous intéressé à réinventer la façon dont les gens achètent des choses ? Consultez nos [offres d'emploi](https://corp.flipp.com/jobs) actuelles._