---
title: J'ai essayé la méthode brillante de Pandora pour la priorisation des fonctionnalités.
  Voici ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-20T16:27:30.000Z'
originalURL: https://freecodecamp.org/news/i-tried-pandoras-brilliant-method-for-feature-prioritization-c5fb586ad317
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8s-VzNIcca2gZ3JNLseODw.jpeg
tags: []
seo_title: J'ai essayé la méthode brillante de Pandora pour la priorisation des fonctionnalités.
  Voici ce que j'ai appris.
seo_desc: 'By Josh Temple

  How Pandora’s method and a $3 pack of sticky notes made stakeholder management a
  breeze.


  Sticky notes: $3. Stakeholder buy-in? Priceless.

  Army of one

  Like many data professionals at small and mid-size companies, I’m a data team of
  one...'
---

Par Josh Temple

#### Comment la méthode de Pandora et un paquet de 3 $ de notes autocollantes ont rendu la gestion des parties prenantes un jeu d'enfant.

![Image](https://cdn-media-1.freecodecamp.org/images/9ExPNpdhUc77MfTrKEDoUIem-zZNS5w8k9Na)
_Notes autocollantes : 3 $. L'adhésion des parties prenantes ? Inestimable._

#### Armée d'une seule personne

Comme de nombreux professionnels des données dans les petites et moyennes entreprises, je suis une équipe de données à moi tout seul chez [Milk Bar](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities). En tant que premier embauché dans le domaine des données, j'ai eu le privilège plutôt terrifiant de construire notre pile de données à partir de zéro. J'ai passé les premiers mois de mon temps ici à construire des chargeurs de données, à modéliser nos données dans BigQuery et [dbt](https://www.getdbt.com/), et à déployer et former nos équipes sur [Looker](https://looker.com/). Maintenant que notre pile de données est fonctionnelle, il est temps de planifier pour le prochain trimestre.

La valeur de l'intelligence d'affaires et de l'analyse devient rapidement apparente chez [Milk Bar](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities), et de plus en plus de personnes viennent à moi avec des demandes de fonctionnalités. Mon backlog se remplit plus vite que je ne peux réaliser les fonctionnalités, et je dois m'assurer que les projets que je m'attaque au prochain trimestre sont vraiment essentiels pour l'entreprise. J'ai lu il y a quelques mois le processus de priorisation des produits de Pandora et j'ai trouvé cela brillant, surtout pour les petites équipes aux ressources limitées, alors j'ai décidé de l'essayer.

#### La méthode Pandora

Le crédit pour ce système revient à [Tom Conrad](https://www.linkedin.com/in/tomconrad/), CTO de Pandora pendant 10 ans, qui a développé cette approche. Je vous encourage à lire [cet article](https://firstround.com/review/This-Product-Prioritization-System-Nabbed-Pandora-More-Than-70-Million-Active-Monthly-Users-with-Just-40-Engineers/) de First Round Review, qui décrit en détail le processus de Pandora, mais je vais le résumer ici :

1. Le leader de l'équipe collecte des idées de fonctionnalités qui sont des "évidences" à travers l'entreprise. Ces idées ne sont pas censées être des projets tape-à-l'œil, de type R&D — elles sont censées être des idées que l'entreprise serait _stupide_ de ne pas aborder lors du prochain trimestre.
2. Chaque idée est condensée en une seule diapositive qui décrit l'impact sur l'entreprise et comment le succès sera mesuré.
3. Chaque idée se voit également attribuer un coût en dollars basé sur le temps d'ingénierie estimé nécessaire pour la construire. Pandora a décidé que 5 $ seraient égaux à un mois de travail d'un ingénieur. Comme mon équipe est beaucoup plus petite, mon ratio de coût était de 5 $ pour une journée de mon temps de développement principal.
4. Le leader de l'équipe organise une réunion avec les décideurs pertinents. Conrad recommande de choisir des leaders qui ne sont pas trop liés à une seule fonction et qui comprennent les priorités de l'entreprise dans son ensemble, comme le PDG et le DAF.
5. Le leader de l'équipe parle de chaque fonctionnalité et répond aux questions, puis colle une impression de chaque diapositive au mur. Le leader de l'équipe divise le "budget" total du temps de l'équipe parmi les décideurs sous forme de notes autocollantes — chaque note autocollante représentant 5 $.
6. Lors du premier tour, les décideurs votent en plaçant leurs notes autocollantes de 5 $ sur les diapositives de fonctionnalités qu'ils souhaitent voir financées. Ensuite, ils peuvent discuter, négocier et déplacer leurs dollars lors du deuxième tour.
7. Après quelques ajustements, les fonctionnalités qui restent financées sont celles que l'équipe d'ingénierie est responsable de construire le trimestre suivant.

La méthode est similaire à la [planification basée sur la capacité](https://www.mountaingoatsoftware.com/blog/capacity-driven-sprint-planning) et emprunte des principes Agile comme les [points de story](https://www.atlassian.com/agile/project-management/estimation) et le poids. Elle est conçue pour résoudre le problème fondamental que les équipes technologiques sont souvent invitées à construire beaucoup plus de fonctionnalités qu'elles n'ont de temps pour. La planification basée sur la capacité n'est pas un nouveau concept, mais cette méthode est spéciale car elle force les parties prenantes avec des priorités concurrentes à s'aligner sur l'ensemble de fonctionnalités qui est le meilleur pour l'entreprise dans son ensemble.

#### Ce que j'espérais et ce que je m'attendais à ce qu'il arrive

Pour utiliser cette méthode chez [Milk Bar](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities), je devais déterminer mon budget total disponible pour le développement de fonctionnalités. Historiquement, j'ai passé environ 20 % de mon temps à travailler sur des demandes ad hoc, 20 % sur des mises à niveau d'infrastructure et de fiabilité, et 60 % sur le développement principal. Avec 61 jours ouvrables au premier trimestre 2019, cela signifiait que j'aurais environ 37 jours pour le développement principal. En utilisant mon ratio de coût de 5 $ par jour de développement principal, j'ai calculé un budget total de 185 $.

J'ai recueilli environ 15 demandes de fonctionnalités pour les produits de données de toute l'entreprise et de mon backlog. Ces demandes allaient de la construction simple de tableaux de bord (5 $, ou une journée de mon temps) à des sources de données entièrement nouvelles nécessitant une ETL et une modélisation extensives (65 $, ou presque trois semaines de mon temps). Le coût total de toutes les fonctionnalités était bien supérieur à 400 $, plus du _double_ de mon temps de développement principal pour le prochain trimestre. Cela m'a vraiment fait comprendre le point. Je déteste dire non, mais je **n'avais définitivement pas assez de temps pour construire tout ce qu'on me demandait de construire**, même si je le voulais ! J'espérais que montrer clairement cet écart entre la demande et la capacité me donnerait des munitions pour demander des effectifs supplémentaires pour mon équipe.

Ensuite, j'ai réduit chaque demande de fonctionnalité à une diapositive concise décrivant l'impact sur l'entreprise et les métriques de succès. Je ne pense pas qu'il y ait une manière particulière de faire cela, mais il est important que la diapositive soit suffisamment succincte pour être comprise rapidement lorsque vos décideurs doivent lire 50 d'entre elles. Voici un exemple de l'une de nos diapositives de fonctionnalités :

![Image](https://cdn-media-1.freecodecamp.org/images/df1OonSQ7kTtQvFR4K1nk70OinHHWE1xAB2X)
_Un exemple de diapositive de fonctionnalité pour un tableau de bord de performance de produit._

Après avoir compilé toutes les diapositives de fonctionnalités, j'ai réalisé que le résultat le plus probable était que l'équipe de décision se rallierait autour de quelques fonctionnalités à fort impact et à coût élevé. Je les appellerai des fonctionnalités de données fondamentales. Ce sont des projets comme de nouvelles intégrations d'API ou de sources de données, de nouvelles explorations Looker, et d'autres constructions similaires complexes. J'ai pensé que notre équipe de décision finirait par laisser de nombreuses demandes de fonctionnalités à coût moyen que je considérais comme "agréables à avoir" non financées.

Je savais que je ne pourrais pas construire les fonctionnalités de données fondamentales sans avoir à dire non à plusieurs des demandes de fonctionnalités plus petites, et j'espérais que ce processus aiderait notre équipe de décision à arriver à cette réalisation par elle-même. Il serait plus facile pour tout le monde de décider ensemble que d'avoir à dire à certains de nos leaders que leurs besoins étaient moins importants que les besoins d'une autre équipe.

#### Le résultat

J'ai rencontré nos responsables d'équipe, notre responsable de la stratégie et notre directeur de l'exploitation pendant environ une heure. J'ai présenté chaque diapositive de fonctionnalité et répondu aux questions sur l'importance d'une fonctionnalité ou sur la raison pour laquelle elle était tarifiée d'une certaine manière. En rappelant à tout le monde que le but était de sélectionner les fonctionnalités qui étaient les meilleures pour [_Milk Bar_](https://milkbarstore.com/?utm_source=medium&utm_campaign=jt_feature_priorities) _dans son ensemble_, je les ai laissés discuter, négocier et dépenser leur budget. Avoir notre directeur de l'exploitation et notre responsable de la stratégie dans la salle a certainement aidé, car ils n'étaient pas liés à une fonction et étaient capables de médier et de régler les désaccords sur les priorités.

Après que la poussière se soit déposée, **seulement 5 des 15 fonctionnalités originales sont restées financées.** J'ai trouvé cela stupéfiant, puisque les responsables d'équipe avec lesquels je travaille avaient fortement plaidé pour chaque fonctionnalité lors de nos réunions individuelles.

[Conrad résume](https://firstround.com/review/This-Product-Prioritization-System-Nabbed-Pandora-More-Than-70-Million-Active-Monthly-Users-with-Just-40-Engineers/) mes pensées sur le résultat...

> C'est incroyable, car quelqu'un de très intelligent a un jour pensé : "Nous serions absolument stupides de ne pas faire cette chose." Mais vraiment, lorsqu'on les considère dans le contexte de toutes les opportunités pour l'entreprise, la moitié des choses que les gens pensaient importantes tombent immédiatement.

**C'est exactement ce qui s'est passé.**

Notre équipe de décideurs s'est alignée sur quelques-unes des fonctionnalités à plus fort impact, choisissant de ne pas financer certains des projets plus petits et "agréables à avoir" qui avaient été suggérés. Certaines des fonctionnalités n'ont pas reçu un seul vote.

C'était l'occasion parfaite pour moi de mentionner que nous aurions presque le double de la capacité pour de nouvelles fonctionnalités si nous étions prêts à embaucher un autre ingénieur de données. Après avoir traversé le processus difficile de couper des fonctionnalités qui semblaient encore importantes, nos leaders ont clairement compris le besoin d'effectifs supplémentaires et m'ont même demandé d'avancer mon calendrier d'embauche. Je ne peux pas penser à une meilleure façon de demander plus de ressources.

Dans l'ensemble, lors de ma première expérience avec cette méthode, j'ai observé quelques avantages significatifs...

* Toutes mes parties prenantes ont une **compréhension claire de ce sur quoi je travaille** le prochain trimestre, combien de temps chaque projet prendra et la priorité de chaque projet par rapport aux autres.
* **Nous n'avons choisi que les choses qui devaient vraiment, vraiment être faites.** Les parties prenantes étaient prêtes à accepter le statu quo là où il était suffisant pour économiser le budget pour les fonctionnalités dont elles ne voulaient pas se passer.
* J'ai obtenu **plus de soutien pour l'embauche** de plus d'ingénieurs et d'analystes de données.
* **Les parties prenantes ont vu à quel point leurs besoins étaient importants** par rapport aux autres besoins de l'entreprise. Elles étaient prêtes à céder des fonctionnalités plus spécifiques à leurs équipes en faveur de fonctionnalités à plus fort impact.
* Dire non à une demande de fonctionnalité peut parfois faire sentir à une partie prenante qu'elle n'est pas valorisée. Dans ce cas, **tout le monde a apprécié le processus.** C'était efficace en temps et amusant. Quelqu'un a dit que l'idée était "géniale", et notre directeur de l'exploitation m'a dit que c'était une "excellente réunion et une approche brillante".

#### Conseils pour adopter cette approche

Je recommanderais absolument cette méthode, et j'ai hâte de la refaire à la fin du prochain trimestre. Voici mes recommandations pour utiliser cette méthode.

* **La planification est la clé.** Prenez votre temps pour rencontrer vos parties prenantes et apprendre les fonctionnalités qu'elles souhaitent. Vous voulez former une image complète de ce dont vos parties prenantes ont besoin de vous pour le prochain trimestre, et il est préférable de leur demander plutôt que de deviner.
* **Soyez prêt à expliquer chaque fonctionnalité de manière concise.** Vous devez être capable de comprendre la motivation et l'exécution prévue de chaque fonctionnalité suffisamment bien pour la décrire rapidement et clairement. Il est utile de pratiquer la description de chaque diapositive de fonctionnalité en moins d'une minute avant votre réunion de décision finale.
* **Soyez prêt à expliquer pourquoi certaines fonctionnalités étaient plus chères que d'autres.** Certains de nos responsables d'équipe étaient initialement frustrés de voir que les fonctionnalités qu'ils demandaient coûtaient plus que leur budget alloué entier. Assurez-vous de pouvoir justifier le coût avec une estimation légitime du travail et de pouvoir expliquer votre estimation.
* **Gardez-le léger mais tenez bon.** En tant qu'animateur, essayez de garder l'atmosphère amusante et aidez à diffuser les tensions ou les désaccords lorsqu'ils surviennent. En même temps, soyez ferme avec vos estimations de travail. En fin de compte, vous n'avez que tant d'heures dans la journée, alors n'ayez pas peur de rappeler à vos parties prenantes que vous ne pouvez pas créer plus de temps. Si elles résistent, vous avez une excellente opportunité de proposer des effectifs supplémentaires pour votre équipe.

Si vous utilisez déjà la méthode Pandora, êtes intéressé à l'essayer ou avez des suggestions sur la façon d'améliorer ce processus, faites-le moi savoir dans les commentaires !

*Si vous avez aimé cet article, veuillez lui donner quelques applaudissements (sur une échelle de 1 à 50) ci-dessous ! Suivez-moi [ici](https://medium.com/@josh.temple) pour plus de contenu sur l'ingénierie des données et l'analyse dans les petites et moyennes entreprises.*