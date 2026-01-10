---
title: Les essentiels de l'Event Sourcing que vous devez connaître lorsque vous commencez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T18:47:14.000Z'
originalURL: https://freecodecamp.org/news/event-sourcing-essentials-you-need-to-know-when-starting-out-13af35d9f932
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6-84rquRE2oH4sJXRIabKA.png
tags:
- name: '#Domain-Driven-Design'
  slug: domain-driven-design
- name: Event Sourcing
  slug: event-sourcing
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Les essentiels de l'Event Sourcing que vous devez connaître lorsque vous
  commencez
seo_desc: 'By Noël Widmer

  Event Sourcing is a thought challenge when starting out. In this story, I will describe
  my experiences from the perspective of an engineer.

  My goal is to help you decide if you want to invest the resources to get started
  with Event Sou...'
---

Par Noël Widmer

L'Event Sourcing est un défi de réflexion lorsque vous commencez. Dans cette histoire, je vais décrire mes expériences du point de vue d'un ingénieur.

Mon objectif est de vous aider à décider si vous souhaitez investir des ressources pour commencer avec l'Event Sourcing.

![Image](https://cdn-media-1.freecodecamp.org/images/vRIbN9ppLB4ixj1hzxbGQ6AcoQKdy-8Fi-xn)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo se voit offrir un choix._

### À propos de l'auteur

Salut ? Je m'appelle Noël. Je vis près de Zurich (Suisse) et je travaille fièrement sur la plus grande plateforme E-Commerce de Suisse. Mon équipe et moi avons appliqué l'Event Sourcing tout au long des 12 derniers mois, et **nous avons beaucoup appris**.

Je veux partager avec vous quatre essentiels que j'aurais aimé connaître il y a un an.

### Une petite introduction à l'Event Sourcing

Cet article ne consiste pas à vous introduire aux concepts de l'Event Sourcing.   
Je pense toujours que je devrais faire **un pas** en arrière cependant — pour brosser un tableau plus clair.

Dans les applications orientées état, vous stockez le résultat d'un calcul dans votre stockage de données. Vous pouvez également conserver un journal où vous archivez les anciens états à des fins d'audit ou de débogage. Mais en stockant l'état, vous perdez l'information sur la transition d'un état à l'autre. Si le nom d'utilisateur d'un utilisateur a disparu, vous vous demanderez comment cela a pu se produire.

![Image](https://cdn-media-1.freecodecamp.org/images/w-5nI8fUU3m3DDBwt8QBX-g1g5YtG5F7A4OU)
_Stockage de l'état dans une application orientée état._

L'Event Sourcing préserve cette information. Cela est réalisé en stockant les transitions d'état plutôt que l'état résultant.

![Image](https://cdn-media-1.freecodecamp.org/images/H9prmbzan1lBxdV6YTG2H9xzWvxT8iLzrXZl)
_Stockage des transitions d'état (événements) dans une application basée sur l'Event Sourcing._

L'état actuel peut être restauré en appliquant tous les événements à une toile vide. Cela signifie que nous pouvons toujours accéder à l'état actuel mais devons investir des ressources computationnelles pour le faire.

Il existe de nombreux articles sur le web qui entrent dans plus de détails. Martin Fowler [en a écrit un](https://martinfowler.com/eaaDev/EventSourcing.html). Et Greg Young [parle beaucoup de l'Event Sourcing](https://youtu.be/kZL41SMXWdM?t=2). Greg est tellement obsédé par l'Event Sourcing qu'il [a implémenté un stockage de données spécialement conçu pour l'Event Sourcing](https://eventstore.org/). Mon équipe utilise le stockage d'événements de Greg — c'est génial !

### 1) L'Event Sourcing n'est pas une solution miracle

Une fois que vous êtes tombé sous le charme amer de l'Event Sourcing, il devient convaincant d'appliquer le concept à tous vos problèmes.

Cela vous fournira des tonnes de données à analyser et vous aurez une base puissante pour détecter des corrélations intéressantes. Vous pourrez détecter des processus inefficaces et les rendre plus efficaces.

Et le préféré de chaque ingénieur (le mien) :

Retracer un bug devient beaucoup plus facile lorsque vous pouvez "voyager dans le temps" jusqu'au moment exact où le bug s'est produit. À la fin, vous économiserez du temps et de l'argent.

Eh bien — pas tout à fait. ⚠️

L'Event Sourcing vous permet certainement de faire l'analyse. **Mais vous devez encore le faire.** Cela prendra du temps. Heureusement, le "voyage dans le temps" est gratuit. Le débogage amélioré est donc garanti dès le premier jour.

Seth Godin a écrit un [excellent article de blog](https://seths.blog/2019/02/the-am-pm-problem-the-curse-of-too-much-data/) sur le sujet. C'est une lecture de 2 minutes, alors consultez-le.

Maintenant, vous connaissez le prix que vous paierez si vous utilisez vos événements à des fins analytiques, ce qui est le principal avantage commercial de l'Event Sourcing après tout.

Il y a un autre coût cependant. L'Event Sourcing augmentera la complexité de votre application. Au lieu de traiter avec l'état actuel de votre application, vous devrez traiter avec tout ce qui s'est passé depuis sa mise en ligne. Les événements qui ne sont plus utilisés resteront dans votre stockage de données et vous devrez les supporter pendant longtemps.

C'est génial si vous déployez une fonctionnalité et continuez à itérer dessus. Soyez simplement conscient qu'il existe maintenant plusieurs versions des événements de cette fonctionnalité dans votre stockage de données et que vous devrez les supporter toutes. Même si vous ne créez plus de nouvelles instances de ces événements.

L'Event Sourcing impose des complexités temporelles supplémentaires auxquelles vous devrez vous habituer. Appliquez-le là où vous voyez une chance non nulle que les données collectées deviennent pertinentes. Où je définirais "pertinent" comme :

* les données pourraient vous donner plus d'informations sur votre domaine
* les données pourraient aider votre entreprise à améliorer ses processus par elle-même
* les données pourraient vous aider à trouver des bugs plus rapidement

Notez que j'ai ajouté le mot "pourraient" dans chacun des trois derniers points. Il est probable que vous ne connaissiez pas l'avantage exact de l'Event Sourcing à l'avance. Faites votre meilleure estimation.

### 2) Reconnaître la nature fonctionnelle de l'Event Sourcing

Les auteurs du célèbre [Patterns, Principles, and Practices of Domain-Driven Design](https://www.amazon.com/Patterns-Principles-Practices-Domain-Driven-Design/dp/1118714709) recommandent les langages de programmation orientés objet comme C# ou Java.

Je suppose que le raisonnement implicite derrière cette recommandation est le nombre de personnes utilisant de tels langages. C'est vrai. Les nouveaux membres de l'équipe auront probablement un démarrage plus facile dans le domaine lorsqu'ils seront confrontés à des langages familiers.

Mais je ne suis pas d'accord. [Greg Young non plus](https://youtu.be/kZL41SMXWdM?t=2). **L'Event Sourcing n'est pas un concept orienté objet.**

On pourrait soutenir que les transitions d'état sont également des objets. Et en effet. Vous pouvez modéliser tout comme des objets. Le fait que vous puissiez le faire ne signifie pas que ce soit le meilleur modèle à utiliser.

Envisagez d'utiliser un langage qui supporte les paradigmes fonctionnels. En particulier, les [unions étiquetées](https://en.wikipedia.org/wiki/Tagged_union) et la [correspondance de motifs](https://en.wikipedia.org/wiki/Pattern_matching) sont extrêmement précieuses. Travailler avec vos événements semblera naturel et vous n'aurez pas à lutter contre le système de types de votre langage. Si votre équipe n'a pas d'expérience avec le monde fonctionnel, il est peut-être préférable de rester avec des langages familiers.

Il est encore plus important de comprendre que **choisir un stockage de données relationnel sera une expérience douloureuse**. Vous ne traitez pas avec des données relationnelles lorsque vous utilisez l'Event Sourcing. Chaque événement a son propre schéma qui peut changer avec le temps. Utiliser un stockage de données relationnel sera douloureux.

> [SQL est le maître de rien mais il ne suce à rien.](https://youtu.be/kZL41SMXWdM?t=1597) - Greg Young

### 3) Préparez-vous à une courbe d'apprentissage abrupte

Comme pour toutes les nouvelles choses, il y aura un apprentissage impliqué. N'essayez pas de l'éviter. Cela ne fonctionnera pas.

![Image](https://cdn-media-1.freecodecamp.org/images/0jNwGHRNDnjJDzwwr2h76zYC7XkT91P1oIv2)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo apprend quelque chose de spécial._

Une excellente façon d'apprendre est de prototyper. Essayez ceci :

* construisez au moins un prototype de votre première application basée sur l'Event Sourcing
* exécutez et observez votre prototype pendant un certain temps
* implémentez de nouvelles fonctionnalités et habituez-vous à itérer sur ce que vous avez construit

Itérez aussi souvent que possible avant de passer en production. Une fois en production, il ne sera pas aussi facile d'implémenter de nouveaux apprentissages.

Passez en production une fois que votre équipe se sent confiante pour maintenir l'application.

Pensez également à la manière dont votre équipe présentera l'Event Sourcing aux nouveaux membres. Les nouveaux arrivants sont déjà dans une position écrasante et apprendre de nouveaux concepts ne leur facilitera pas la tâche.

Trouvez un moyen de les introduire à l'Event Sourcing de manière douce et sûre. Il est important de le déterminer une fois que vous commencez à avoir de nouveaux membres dans l'équipe. Il est acceptable de le retarder jusqu'à ce que cela se produise.

### 4) Préparez-vous aux débats politiques

Avez-vous réalisé que votre entreprise veut des résultats **bon marché** et de **qualité** **aujourd'hui** ?

Oh mon Dieu, à qui je parle — bien sûr que vous l'avez fait. ?

Est-ce qu'ils aimeront lorsque vous expérimenterez avec un concept qui défie l'esprit et dont ils n'ont peut-être jamais entendu parler ? Et à quoi ressemble la pile technologique de votre entreprise ? Utilisez-vous habituellement des langages de programmation orientés objet en combinaison avec des bases de données relationnelles ? Est-ce qu'ils aimeront lorsque vous passerez à une pile technologique fonctionnelle ?

Selon la culture de votre entreprise, vous devrez peut-être combattre vos collègues sur plusieurs fronts. Agissez en tant qu'exemple. Dites la vérité. Vous savez que ce sera difficile, surtout au début. Partagez vos préoccupations. Assurez-vous que toutes les personnes impliquées connaissent les risques et ce que vous ferez pour les prévenir.

Et n'oubliez pas de décrire comment vous imaginez le paradis de l'Event Sourcing. Faites participer l'entreprise en leur permettant de construire des rapports basés sur vos événements précieux. Ils adorent ça.

Faites participer les ingénieurs concernés en partageant l'expérience de débogage améliorée. Les ingénieurs sont têtus, ils pourraient ne pas aimer ça.

J'ai trouvé utile de pratiquer de tels débats avec mes collègues. Établissez un environnement sûr pour l'entraînement et encouragez les membres de votre équipe à y participer.

![Image](https://cdn-media-1.freecodecamp.org/images/Y7d79Cv8qbHMWOoWken3t-86JsVOnSWRJ-n3)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo s'entraîne dans un environnement sûr._

Soyez prêt et connaissez votre sujet. Vous allez réussir ! ?

### Conclusion

Permettez-moi de résumer.

* Plus de données n'est pas toujours bon.
* Des données supplémentaires sans le temps de les analyser sont inutiles.
* L'analyse sans l'intention et le temps d'agir sur le résultat est inutile.
* L'Event Sourcing améliore la capacité à déboguer votre application.
* L'Event Sourcing est un paradigme fonctionnel.
* Préparez-vous à une courbe d'apprentissage abrupte.
* Tout le monde ne sera pas heureux de vos plans.

C'est tout. Mon intention était de préparer vos attentes à mes expériences. Ne vous inquiétez pas. Soyez déterminé et **choisissez la pilule rouge !**

### The Matrix

Toutes les images de cette histoire sont empruntées au film [The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&qid=1550756146&s=movies-tv&sr=1-6).

J'ai passé 9 ans à écrire du code orienté objet et à travailler avec des bases de données relationnelles. Il y a environ deux ans, j'ai commencé à expérimenter avec du code fonctionnel et des bases de données non relationnelles. Le changement de mentalité a été l'une des leçons les plus importantes de ma carrière à ce jour.

Remettez en question votre environnement. Trouvez les défauts. Quittez la Matrice et découvrez un monde entièrement nouveau.

Au revoir. À la prochaine. Et bonne chance !

![Image](https://cdn-media-1.freecodecamp.org/images/nCTTljApCmGwNVYDCtgOabSoZ6V7wjQIvAC0)
_[The Matrix](https://www.amazon.com/Complete-Trilogy-Reloaded-Revolutions-Blu-ray/dp/B001CEE1YE/ref=sr_1_6?keywords=the+matrix&amp;qid=1550756146&amp;s=movies-tv&amp;sr=1-6" rel="noopener" target="_blank" title="): Neo reçoit un cadeau d'adieu._

**Je n'écris que sur la programmation et la technologie. Si vous me suivez, je ne perdrai pas votre temps.** ?