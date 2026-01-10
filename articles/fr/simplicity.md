---
title: La simplicité est la sophistication
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-07T09:54:58.000Z'
originalURL: https://freecodecamp.org/news/simplicity
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca1a3740569d1a4ca4fc9.jpg
tags:
- name: Clean Architecture
  slug: clean-architecture
- name: mental models
  slug: mental-models
- name: Mindset
  slug: mindset
- name: soft skill
  slug: soft-skill
- name: software architecture
  slug: software-architecture
seo_title: La simplicité est la sophistication
seo_desc: 'By Srinivasan C

  Recently I attended a meeting with multiple stakeholders from the business side.
  When asked to explain a feature, I started explaining them the details of the feature
  and its implementation. After the meeting one of my colleagues told...'
---

Par Srinivasan C

Récemment, j'ai assisté à une réunion avec plusieurs parties prenantes du côté commercial. Lorsqu'on m'a demandé d'expliquer une fonctionnalité, j'ai commencé à leur expliquer les détails de la fonctionnalité et de sa mise en œuvre. Après la réunion, l'un de mes collègues m'a dit que même si je l'avais expliqué en détail, ils demanderaient une réunion de suivi pour discuter de la même chose et c'était vrai — le lendemain, nous avons reçu une invitation à une réunion pour la même chose en tant que suivi. Il m'a expliqué que la raison était que je leur avais fourni plus de détails que nécessaire, ce qui les avait probablement confus. Cet incident m'a conduit au principe du Rasoir d'Occam.

Cité de Wikipedia

> _Le rasoir d'Occam ou la loi de parcimonie est le principe de résolution de problèmes qui stipule essentiellement que « les solutions les plus simples sont plus susceptibles d'être correctes que les solutions complexes ». Lorsqu'on est confronté à des hypothèses concurrentes pour résoudre un problème, on doit sélectionner la solution avec le moins d'hypothèses. L'idée est attribuée au frère franciscain anglais Guillaume d'Ockham (v. 1287–1347), un philosophe scolastique et théologien._

Nous avons tous entendu la célèbre citation de Sherlock Holmes

> _Une fois que vous avez éliminé l'impossible, ce qui reste, peu importe à quel point cela semble improbable, doit être la vérité._

Cela découle directement du Rasoir d'Occam. Ce principe stipule que, étant donné deux explications d'une situation, celle dans laquelle il y a le moins de variables (la plus simple), peu importe à quel point elle semble improbable, est l'explication la plus probable. Ce principe est très utile et peut être utilisé dans une grande variété de situations, mais il est particulièrement puissant entre les mains des professionnels du logiciel.

Il existe de nombreux domaines du développement logiciel qui peuvent bénéficier de ce principe. Voici quelques-uns d'entre eux :

### Codage

Le premier et le plus important domaine est le codage. En tant que développeurs, nous prenons des centaines de décisions chaque jour qui affectent directement la santé de la base de code et, par conséquent, l'entreprise. Quelques-unes des erreurs que nous commettons incluent l'ajout d'abstractions indésirables, la conception pour l'avenir, la rendre « extensible » (quoi que cela signifie). Ces codes avec une complexité supplémentaire indésirable se détériorent lentement avec le temps et deviennent « cette » partie de la base de code que personne ne comprend et que personne n'est prêt à toucher. Ce sont les choses que nous faisons, soit consciemment, soit inconsciemment, qui peuvent nuire à la santé de notre base de code à long terme.

Pour surmonter cela, il serait prudent pour nous de penser en termes de Rasoir d'Occam. Faites toujours la chose la plus simple possible à tout moment. Les principes comme YAGNI et KISS sont des exemples du Rasoir d'Occam en codage. Si vous voulez combiner 3 modèles de conception pour accommoder une demande de fonctionnalité que vous attendez dans le futur, retenez vos instincts primaires et restez avec une seule classe pour l'instant. Utiliser le Rasoir d'Occam pendant le processus de développement maintiendrait la base de code simple et lisible, et vos futurs pairs vous en seront vraiment reconnaissants.

Un mot d'avertissement ici est que ce principe ne doit pas être utilisé comme une excuse pour écrire du mauvais code ou prendre des raccourcis. Si il y a un réel besoin d'ajouter de la complexité, alors vous devriez le faire. Considérez cela comme un cadre pour vous permettre de reculer et de réfléchir un moment et de peser le coût de votre décision à long terme.

### Débogage

Une autre application intéressante de ce principe est le débogage. La partie difficile du débogage est que personne ne connaît la réponse, surtout lorsque vous travaillez dans une base de code héritée avec des fonctionnalités critiques pour l'entreprise. Plus la base de code est grande, plus le processus de débogage est complexe et ainsi le Rasoir d'Occam devient vraiment utile. Tous les bons développeurs logiciels que je connais tracent la cause profonde d'un bug en utilisant ce principe sans même s'en rendre compte.

Disons que vous écrivez un programme pour afficher quelques statistiques dans le tableau de bord. Vous observez que chaque fois que le tableau de bord est mis à jour, vous obtenez 2x au lieu de x pour une statistique particulière. Quelle serait votre première intuition ? Est-ce un problème de double comptage ou une condition de course au niveau des threads ? Je suppose que la plupart d'entre vous opteront pour le premier. C'est le Rasoir d'Occam en action. Vous avez choisi l'option qui fournit l'explication la plus simple pour le problème de manière intuitive.

Cela ne signifie pas que l'explication la plus simple est toujours la bonne. Au lieu de cela, vous commencez par la plus simple et éliminez une par une, soit par la théorie, soit par l'expérimentation, jusqu'à ce que vous arriviez à la cause réelle du problème. Cela fournit un cadre pour aborder les problèmes de manière méthodique.

### Communication

L'une des fonctions les plus sous-estimées d'un développeur logiciel est la communication. Que ce soit avec des pairs, des managers ou des parties prenantes, la communication est aussi importante que le codage pour tout développeur. En tant que développeurs, nous sommes les plus proches de tout problème donné et il est naturel que les gens comptent sur nous pour comprendre le tableau complet d'un produit ou d'une fonctionnalité. Cela rend ce que vous communiquez et la manière dont vous le communiquez extrêmement crucial du point de vue commercial.

Étant les plus proches d'un problème, nous aurons beaucoup de connaissances techniques et de domaine à ce sujet. Mais il est extrêmement important de communiquer les bonnes choses aux bonnes personnes. Supposons que vous soyez dans un fil de courrier avec un ingénieur senior, un chef de produit, un manager et un exécutif de développement commercial, vous devez fournir juste la bonne quantité de détails pour que l'ingénieur puisse comprendre les défis techniques et que les autres puissent également comprendre la complexité technique ainsi que la justification commerciale. Vous devez atteindre le bon équilibre dans le mélange technique/commercial pour que le public comprenne et ne perde pas intérêt. C'est là que le Rasoir d'Occam intervient. Vous devez fournir le niveau de détail le plus bas dans le courrier et planifier un suivi pour les personnes qui doivent comprendre davantage.

Prenons cela comme exemple : « nous avons fait un POC sur x et nous avons pu atteindre y. Même si nous avons discuté de A dans le courrier précédent, nous n'avons pas pu atteindre A en raison des complexités dans une bibliothèque que nous utilisions. Il y avait beaucoup d'hypothèses dans le modèle de threading de la bibliothèque et cela nous a empêchés d'atteindre A ».

Maintenant, que pensez-vous que les différentes parties prenantes comprendront ?

1. Ingénieur — Oui, je comprends le problème.
2. Chef de produit — Donc, en gros, nous ne pouvons pas atteindre A. Et qu'est-ce qu'un modèle de threading ?
3. Manager — A-t-il assez essayé pour atteindre A ?

Au lieu de cela, si nous écrivons « nous avons fait un POC sur x et avons pu atteindre y. A était visé mais n'a pas été atteint. Je vais planifier une réunion pour démontrer le POC et entrer dans les détails sur le bloqueur pour A. » Après cela, vous avez tout le temps du monde pour expliquer en détail les bloquants au bon public et atteindre un consensus.

Maintenant, quel est le processus de réflexion après la démonstration ?

1. Ingénieur — Cela a du sens.
2. Chef de produit — Le POC est bon pour l'instant. Je suppose que nous pouvons abandonner A pour l'instant et procéder sans lui.
3. Manager — Il a fait une analyse approfondie et sait ce qu'il fait.

### Conclusion

Le Rasoir d'Occam peut être employé dans une grande variété de scénarios et ceux-ci ne sont que quelques exemples. Les développeurs utilisent ce principe de manière intuitive sans le savoir. Mais le connaître et l'utiliser délibérément dans diverses situations vous améliorera grandement en tant que développeur logiciel. Si vous pouvez penser à un autre domaine du logiciel où ce principe est utilisé, n'hésitez pas à laisser vos pensées dans les commentaires.

---

Si vous avez aimé cet article, n'hésitez pas à me contacter à [https://kaizencoder.com/contact](https://kaizencoder.com/contact).