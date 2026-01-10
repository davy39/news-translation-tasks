---
title: 'Anti-Patterns en Ingénierie de Test : Détruisez la Satisfaction de vos Clients
  et Faites Chuter votre Qualité en Utilisant ces 9 Pratiques Organisationnelles Faciles'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-30T13:59:11.000Z'
originalURL: https://freecodecamp.org/news/organizational-test-practices-guaranteed-to-lower-quality
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca033740569d1a4ca4735.jpg
tags:
- name: engineering
  slug: engineering
- name: organization
  slug: organization
- name: satire
  slug: satire
seo_title: 'Anti-Patterns en Ingénierie de Test : Détruisez la Satisfaction de vos
  Clients et Faites Chuter votre Qualité en Utilisant ces 9 Pratiques Organisationnelles
  Faciles'
seo_desc: 'By Cristian Medina

  A recent podcast episode reminded me that it''s a good idea to examine things from
  different perspectives. Doing so can expose behaviors that appear purposeful as
  consequences of environmental factors. You won''t succeed at fixing th...'
---

Par Cristian Medina

Un récent épisode de podcast m'a rappelé qu'il est bon d'examiner les choses sous différents angles. Cela peut révéler des comportements qui semblent intentionnels mais qui sont en réalité des conséquences de facteurs environnementaux. Vous ne réussirez pas à corriger ces comportements tant que vous n'aurez pas agi sur l'environnement qui les encourage.

Aujourd'hui, nous discutons de l'ingénierie de test et des pratiques organisationnelles qui tendent à réduire la qualité de vos livrables.

En lisant cet article, gardez à l'esprit que nous mettons l'accent sur des objectifs contraires à ce que vous attendez : une qualité inférieure et une satisfaction client réduite. Les suggestions peuvent sembler cyniques et contre-intuitives, mais c'est tout l'intérêt de l'exercice. Alors, commençons.

## 1. Rendez les équipes de test uniquement responsables de la qualité

L'une des meilleures façons de réduire la qualité est de détourner l'attention du produit pour la diriger vers la politique interne.

Vous voulez capitaliser sur les réactions comportementales humaines par défaut qui minimisent la réflexion et maximisent les conflits — quelle meilleure façon de le faire qu'en encourageant le tribalisme.

Rendre une seule organisation responsable d'un objectif (peu importe lequel) garantira le comportement divisionnaire que vous essayez d'obtenir.

Ce groupe passera la plupart de son temps et de ses ressources à prouver que ses responsabilités ont été remplies, plutôt qu'à faciliter les objectifs du produit.

Pour maximiser l'impact de ce principe, assurez-vous que les équipes de test ne soient responsables que de l'objectif de qualité. Elles ne devraient pas être responsables de la détermination du contenu des versions, c'est l'équipe Marketing qui s'en charge. Elles ne devraient pas non plus être impliquées dans la fixation des dates de sortie, c'est une fonction commerciale. Elles ne déterminent pas non plus quels problèmes corriger, c'est à l'équipe Produit de le faire.

Vous voulez que l'équipe de développement se concentre sur la livraison des fonctionnalités à temps pour les dates promises par les équipes Marketing et Commerciales. Évitez donc d'imposer des règles de commit ou de fusion de code demandées par les équipes de test, comme l'exigence de revues de code, de passage de linters, de passage de tests unitaires, etc. Après tout, la qualité est la responsabilité des équipes de test, pas celle du développement.

En divisant les objectifs de cette manière, les ordres du jour des réunions se détournent de l'expérience client pour se diriger vers le jeu des responsabilités. Vous savez que vous êtes sur la bonne voie lorsque vous entendez des déclarations comme :

* "Pourquoi n'avez-vous pas trouvé ce bug plus tôt ?"
* "Les tests actuels ont échoué, mais nous devons vraiment fusionner cette nouvelle fonctionnalité pour que vous puissiez commencer à la tester."
* "Pourquoi le test n'a-t-il pas trouvé ce problème client ?"
* "Nous avons promis au client une version à cette date, alors reportons toutes les conclusions des tests et donnons-leur une version aujourd'hui."
* "Nous avons trouvé le problème signalé par le client, mais vous l'avez reporté le mois dernier !"
* "Je ne peux pas exécuter les tests car vous m'avez donné une version cassée."

Passer du temps à discuter de qui doit faire le travail est un excellent mécanisme pour réduire la satisfaction envers votre produit ou service.

## 2. Exigez que tous les tests soient automatisés avant la sortie

Un autre moyen de détourner l'attention de la qualité est d'exiger l'automatisation des tests pour chaque fonctionnalité. Cela garantit que votre organisation de test passe la plupart de son temps à faire du développement logiciel plutôt que de l'ingénierie de test.

L'objectif doit changer de la validation d'un attribut de produit au comptage du nombre de tests automatisés exécutés pour le vérifier.

Plutôt que de réfléchir à la décomposition des tests qui valident divers chemins de code ou les fondamentaux d'une fonction, les ingénieurs passeront du temps et des ressources à exécuter plusieurs itérations du même test. Cela conduit à des comptes plus élevés.

Cela favorise également une infrastructure de test fragile et augmente les coûts de maintenance.

Puisqu'il n'y a pas de temps pour considérer la stratégie de test et les abstractions, ils sont obligés d'écrire des workflows très spécifiques — mais fragiles. Chaque fois que le développement apporte des modifications mineures à la fonctionnalité, les tests échouent.

L'organisation de test doit se concentrer sur la production d'un grand nombre de tests le plus rapidement possible. Sinon, ils auront le temps de pousser plus de valeur dans le produit avec des tests plus significatifs.

N'oubliez pas de récompenser ce comportement en promouvant les ingénieurs qui produisent le plus grand nombre de tests automatisés qui s'exécutent fréquemment. Mais n'oubliez pas ceux qui économisent du temps en écrivant des scripts qui exécutent d'autres scripts tout en codant en dur tous les arguments pour que l'utilisateur n'ait pas à les taper.

## 3. Exigez une couverture de code à 100 %

Puisque la qualité du produit et l'expérience client ne sont corrélées qu'à la couverture de code, forcer vos équipes de test et de développement à poursuivre une couverture à 100 % est une autre tactique.

Assurez-vous de diriger toutes les conversations d'exécution vers la mesure de la couverture et de tenir les équipes responsables de celle-ci. Les gens se concentreront sur la construction de tests qui appellent toutes les fonctions de code, indépendamment de leur sortie.

Un bonus intéressant est que la mesure de la couverture tend à affecter le timing ou la performance. Cela rend difficile pour quiconque de comprendre l'expérience client réelle, contribuant ainsi à votre objectif de satisfaction réduite.

Assurez-vous que les implémentations d'outils sont automatisées et que chaque rapport inclut les chiffres de couverture, afin qu'il soit facile d'en parler lors des conversations.

Évitez de vous concentrer sur la couverture des branches de code. Il est essentiel de prouver que vous avez testé chaque fonction, et non chaque chemin de code dans la fonction. Après tout, il n'y a aucun intérêt à planifier pour que les clients rencontrent des cas d'échec. Ils ne se produisent qu'un petit pourcentage du temps.

Tout comme dans la section précédente, n'oubliez pas de récompenser l'équipe pour être aussi proche que possible du chiffre de couverture à 100 %. Cela montre à vos ingénieurs le comportement qui compte.

## 4. Isolez l'organisation de test du développement

L'une des pires choses dans le développement logiciel est lorsque l'équipe de développement est si en phase avec l'équipe de test qu'ils finissent les phrases l'un de l'autre. C'est un signal d'alarme ! Cela signifie que vous êtes sur la voie de la production d'un produit ou service de qualité.

Réduisez toutes les chances de collaboration, y compris la proximité physique.

Assurez-vous de séparer les équipes, afin qu'il faille un effort physique pour qu'un ingénieur de test aille voir un développeur et pose des questions. La nature humaine prendra le relais et résoudra le reste du problème pour vous.

Lorsque ces deux organisations collaborent activement, elles tendent à s'entraider considérablement. Vous constaterez que le développeur donne un avertissement au testeur sur les nouveaux changements. Alternativement, l'inverse pourrait se produire, où un développeur saura qu'un bug existe avant qu'il ne soit signalé. Non seulement cela brise le tribalisme, mais cela détourne également les responsabilités bien définies.

La collaboration conduit à moins de processus :

* Dans certains cas, les problèmes sont simplement corrigés au lieu d'être signalés.
* La documentation interne et les transferts de connaissances reçoivent moins de temps et d'attention.
* Les ingénieurs de test deviennent plus connaisseurs du produit.
* Les calendriers de sortie commencent à refléter la réalité lors de la planification.

Tout cela conduit à une meilleure qualité et à une meilleure satisfaction client ! L'opposé direct de vos objectifs.

Imposer plus de processus est un excellent moyen de décourager ce comportement. Cela aide à mettre en évidence les exigences qu'un ingénieur ne respecte pas lorsqu'il interagit directement avec d'autres équipes. Cela peut prendre la forme de points de contrôle et de réunions supplémentaires, mais de préférence, plus de documentation.

Un autre excellent outil pour augmenter l'isolement est le contrôle d'accès. Assurez-vous que les équipes de test n'ont pas accès au code source et que les équipes de développement ne peuvent pas voir les procédures d'un cas de test.

Je trouve que la séparation des tests du code est une nécessité ! Si vous avez les deux dans le même dépôt, alors les développeurs sauront à l'avance quand ils cassent un test. Un raccourci de processus qui conduit aux efficacités que nous ne voulons pas.

## 5. Mesurez le succès du processus, pas celui du produit

Je ne peux pas vous dire combien de conversations j'ai eues avec des collègues qui continuent à poser des questions impertinentes sur l'adoption par les clients.

Des choses comme : Combien de clients utilisent cette fonctionnalité ? Quel est l'impact potentiel sur notre base d'installation ? Combien d'étapes l'utilisateur doit-il suivre pour utiliser cette fonctionnalité ? Quel est le taux d'attachement ? Quelle est la taille de notre pool de clients potentiels pour cette exigence ? Combien d'utilisateurs ont demandé cette fonction ?

Ces gens ne comprennent pas. Il est impératif de décourager ce comportement dès qu'il se produit. Il tend à se répandre parmi les autres membres de l'équipe, et bientôt, vous aurez une organisation qui ne se soucie que de la qualité.

La meilleure chose à faire est de rediriger cette énergie en posant des questions sur le processus au lieu du produit. Les éléments ci-dessous sont quelques statistiques qui aident à accomplir cela.

### Nombre de problèmes ouverts et qui les a ouverts

Cela aide à prouver à quel point l'équipe de test fait du bon travail et combien de travail elle fournit.

N'oubliez pas d'encourager les employés qui ont ouvert le plus grand nombre de problèmes. Parlez-en souvent lors des réunions, afin que les autres ne soient pas surpris lors des revues de performance.

Certains essayeront d'argumenter que trop de problèmes ouverts entraînent des frais généraux importants pour les gérer. Encore une fois, c'est tout l'intérêt.

Recentrez les efforts de l'équipe sur le processus plutôt que sur la qualité. De plus, s'il y a trop peu de problèmes, alors l'organisation de test semble ne pas travailler.

### Temps passé par un problème en attente de réponse de l'équipe de test

C'est plus difficile à mesurer, mais lorsque vous y arrivez, c'est un excellent moyen de montrer à quel point l'organisation de test se comporte bien par rapport au développement. Cela encourage les comportements qui aident à maximiser le nombre de problèmes actifs.

Pour aider la situation, essayez de lier les changements d'état des problèmes aux exigences du processus qui imposent des valeurs de champ particulières pour des situations spécifiques.

Cela réduit le temps qu'un problème passe du côté du test lorsque les paramètres ne correspondent pas, car l'ingénieur devra demander la correction.

Le développement est généralement trop occupé pour se soucier de ces choses. Cela conduit également à de nombreuses discussions politiques lors des réunions de gestion de projet et encourage davantage le tribalisme.

### Pourcentage de problèmes dans un état fermé

Avant une sortie, vous voulez encourager l'équipe à fermer tous les problèmes. Il est préférable de baser la revue de performance des ingénieurs de développement sur le nombre de problèmes ouverts contre leur code au moment de la sortie.

Cela garantit moins de défauts ouverts par l'équipe de développement — ce qui améliore davantage les performances de votre équipe de test. Cela décourage également la communication avec l'organisation de test et augmente les frictions.

### Pourcentage de tests exécutés par rapport à un plan d'exécution

N'oubliez pas de créer une courbe d'exécution indiquant à l'équipe comment dépenser son temps tout au long du cycle de test. Faites attention à ne pas la baser sur l'historique, sinon vous pourriez constater que l'organisation atteint les chiffres et améliore la qualité.

Vérifiez le graphique dans chaque réunion de statut et demandez des progrès indépendamment de l'état du produit. Cela force l'inclusion de tests destinés à toujours se terminer juste pour gonfler les chiffres et répondre aux attentes.

Découragez quiconque qui dépasse les projections. Cela donne l'impression que l'organisation de test a du temps libre.

### Mesurez le taux de réussite

Vous voudrez suivre le pourcentage d'exécution des tests qui réussissent par rapport à ceux qui échouent pour tous les tests ensemble.

Assurez-vous d'expliquer à l'équipe le taux de réussite requis pour atteindre une étape de sortie. Cela leur rappelle de concevoir des suites avec suffisamment de tests qui réussissent toujours afin que vous puissiez répondre aux exigences du processus.

## 6. Exigez des projections granulaires de la part des ingénieurs

Obtenir un calendrier de la part du développement est difficile. De nombreuses fois, ils essaient de jeter la réalité au problème comme si la complexité comptait. La vérité est que vous sortirez à la date désignée par l'organisation commerciale quoi qu'il arrive, mais le développement ne semble jamais comprendre cela.

Lors de la discussion des dates d'achèvement du code, assurez-vous de demander le jour, pas la semaine ou le mois où ils termineront. Si vous n'êtes pas d'accord avec cette date, soulevez-la dans un forum public de tous leurs pairs afin qu'ils puissent en discuter.

Cela accomplit plusieurs points essentiels pour réduire la qualité :

* Les développeurs se disputent entre eux, réduisant la communication.
* Ils arrêtent de penser qu'ils ont leur mot à dire sur la façon de passer leurs journées ou de faire leur travail, ce qui augmente le turnover.
* Cela rend peu probable qu'ils respectent leurs délais, ce qui réduit leur revue de performance et augmente également le turnover.

Atteindre un turnover élevé est comme le saint graal de la réduction de la qualité. Cela aide à réduire les coûts avec moins d'augmentations et de promotions. Cela augmente la désinformation, en mettant l'accent sur l'individualisme. Enfin, cela élimine toute responsabilité qui pourrait se construire dans l'équipe au fil du temps.

## 7. Récompensez les correctifs rapides plutôt que la résolution

Donnez suffisamment de temps aux ingénieurs et ils peuvent résoudre presque tous les problèmes. Mais lorsque vous faites le contraire, un phénomène intéressant se produit : au lieu de résoudre le problème racine, ils corrigent les symptômes, parfois en ignorant complètement le problème.

Voici quelques-uns des avantages que vous verrez en utilisant cette technique :

* Le développement reçoit des éloges pour sa rapidité.
* Le problème de base n'est pas résolu, il y a donc de nombreuses opportunités pour écrire de futurs bugs, ce qui fait paraître l'équipe de test et le processus meilleurs.
* Le client continuera à rencontrer les mêmes problèmes, ce qui se traduit par une satisfaction réduite.
* Les correctifs pour chaque symptôme développent une toile d'araignée de dépendances, rendant le travail futur plus difficile et plus fragile, ce qui se traduit par une qualité inférieure.
* Vous gagnerez des problèmes pour chacun que vous corrigez à un rythme viral. Plus il y a de problèmes à corriger, plus vous avez besoin de processus pour suivre ceux qui restent. Gagnant-gagnant !

Les récompenses sont également fondamentales ici. Assurez-vous d'inciter ce type de travail avec des prix et de les diffuser à l'équipe afin que tout le monde soit conscient du comportement que vous souhaitez.

## 8. Planifiez pour aujourd'hui au lieu de demain

Il y a toujours quelqu'un qui essaie de prévoir ce que demain apportera. De nos jours, certains ingénieurs feront des analyses statistiques ou du machine learning. Formuler un algorithme qui explique comment l'exécution se déroule, quels problèmes sont importants, combien de temps est réellement nécessaire, le nombre de ressources requises pour tester, etc.

Ensuite, il y a les gens qui sont là depuis assez longtemps et qui continuent de rappeler les erreurs passées ou les efforts gaspillés que vous devriez éviter.

Ignorez ces conseils et planifiez toujours pour le meilleur cas aujourd'hui. Peu importe si la dette technique est élevée, si le fournisseur tiers a une faible qualité, ou si tout le monde a prévu des vacances le même jour lors de la prochaine sortie.

Traitez les problèmes lorsqu'ils se produisent, pas avant. Sinon, l'efficacité augmentera.

## 9. Conclusions

Bien qu'il y ait beaucoup plus de points à couvrir, il semble que notre équipe commerciale fictive ait décidé de livrer avant de terminer l'article !

Sur une note plus sérieuse, l'ingénierie de test et la validation des produits deviennent exponentiellement plus difficiles avec des systèmes complexes et de grandes organisations. Il est important d'inciter les bons types de comportements pour réussir. Cependant, ceux-ci ne sont pas toujours évidents et, dans certains cas, ils sont même contre-intuitifs.

J'espère que cet article vous a aidé à observer le monde des tests sous un angle différent. Un angle qui fournit quelques perspectives utiles. Je trouve cette pratique de viser de mauvais résultats assez éclairante parfois. À tout le moins, c'est très amusant d'y réfléchir.

---

Si vous avez aimé l'article et souhaitez en lire davantage sur les meilleures pratiques de développement de Cristian Medina et d'autres, veuillez visiter [tryexceptpass.org](https://tryexceptpass.org). Restez informé avec leur dernier contenu en vous abonnant à [la liste de diffusion](https://tinyurl.com/tryexceptpass-signup).