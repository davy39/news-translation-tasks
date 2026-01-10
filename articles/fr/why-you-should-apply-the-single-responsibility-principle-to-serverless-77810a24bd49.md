---
title: Pourquoi vous devriez appliquer le principe de responsabilité unique au serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-29T08:30:07.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-apply-the-single-responsibility-principle-to-serverless-77810a24bd49
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lIL-txZJ5iBrg9DDf6-nww.png
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi vous devriez appliquer le principe de responsabilité unique au
  serverless
seo_desc: 'By Yan Cui

  A fun­ny moment (at 38:50) hap­pened dur­ing Tim Bray’s ses­sion (SRV306) at re:invent
  2017. Tim asked the audi­ence if we should have many single-purposed func­tions,
  or few­er mono­lith­ic func­tions, and there was an equal split in opin...'
---

Par Yan Cui

Un moment amusant (à 38:50) s'est produit lors de la session de Tim Bray ([SRV306](https://www.youtube.com/watch?v=sMaqd5J69Ns)) à re:invent 2017. Tim a demandé à l'audience si nous devrions avoir de nombreuses fonctions à usage unique, ou quelques fonctions monolithiques, et il y avait une division égale des opinions.

Ce fut un moment qui a remis en question ma croyance, car j'ai été élevé avec les principes SOLID.

* Principe de responsabilité unique
* Principe ouvert/fermé
* Principe de substitution de Liskov
* Principe de ségrégation des interfaces
* Principe d'inversion des dépendances

J'ai, pendant longtemps, cru que suivre le **Principe de responsabilité unique** (SRP) était une évidence.

Cela a suscité cet examen plus approfondi des arguments des deux côtés.

Divulgation complète : **Je suis partial dans ce débat.** Si vous trouvez des lacunes dans ma réflexion, ou si vous n'êtes pas d'accord avec mes opinions, veuillez les signaler dans les commentaires.

Par « fonctions monolithiques », j'entends des fonctions qui ont une logique de branchement interne. Ces fonctions peuvent faire l'une des plusieurs choses en fonction de l'événement d'invocation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lIL-txZJ5iBrg9DDf6-nww.png)

Par exemple, vous pouvez avoir une fonction qui gère tous les endpoints d'une API. La fonction effectuerait une action différente en fonction des paramètres `path` et `method`.

```
module.exports.handler = (event, context, cb) => {   const path = event.path;   const method = event.httpMethod; 
```

```
  if (path === '/user' && method === 'GET') {     .. // obtenir l'utilisateur   } else if (path === '/user' && method === 'DELETE') {     .. // supprimer l'utilisateur   } else if (path === '/user' && method === 'POST') {     .. // créer l'utilisateur   } else if {    .. // autres endpoints et méthodes   }}
```

Vous ne pouvez pas raisonnablement raisonner et comparer des solutions sans d'abord comprendre le problème et quelles qualités sont les plus souhaitables dans une solution.

Et lorsque j'entends des plaintes comme « avoir tant de fonctions est difficile à gérer », je me demande ce que signifie **gérer** ?

* Est-ce trouver des fonctions spécifiques que vous cherchez ?
* Est-ce découvrir quelles fonctions vous avez ?
* Cela devient-il un problème lorsque vous avez 10 fonctions ou 100 fonctions ?
* Cela devient-il un problème seulement lorsque vous avez plus de développeurs travaillant dessus que vous ne pouvez en suivre ?

En m'appuyant sur mes propres expériences, le problème a moins à voir avec les fonctions que nous avons. Plutôt, il s'agit de découvrir quelles fonctionnalités et capacités nous possédons à travers ces fonctions.

Après tout, une fonction Lambda, comme un conteneur Docker, est un conduit pour livrer une fonctionnalité ou une capacité métier.

Vous ne demanderiez pas « Avons-nous une fonction `get-user-by-facebook-id` ? » puisque vous devriez savoir ce que la fonction était appelée sans même savoir si la capacité existe et si elle est capturée par une fonction Lambda. Au lieu de cela, vous demanderiez probablement, « Avons-nous une fonction Lambda qui peut trouver un utilisateur basé sur son ID Facebook ? »

Donc, le vrai problème est que, étant donné que nous avons un système complexe composé de nombreuses fonctionnalités et capacités, maintenu par de nombreuses équipes de développeurs, **comment organisons-nous ces fonctionnalités et capacités en fonctions Lambda pour qu'elles soient optimisées vers :**

* **découvrabilité** : comment puis-je découvrir quelles fonctionnalités et capacités existent dans notre système ?
* **débogage** : comment puis-je identifier et localiser rapidement le code dont j'ai besoin pour examiner et déboguer un problème ? Par exemple, il y a des erreurs dans les logs du système X, où puis-je trouver le code pertinent pour commencer à déboguer le système ?
* **mise à l'échelle de l'équipe** : comment puis-je minimiser les frictions et faire croître l'équipe d'ingénierie tout en maintenant le code ?

Ci-dessous se trouvent les qualités qui sont les plus importantes pour moi. Avec cette connaissance, je peux comparer différentes approches et voir laquelle est **la mieux adaptée pour moi**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OG159w6MLTOQnLL6ei18lw.png)

Vous pourriez vous soucier de qualités différentes. Par exemple, vous pourriez ne pas vous soucier de la mise à l'échelle de l'équipe, mais le coût est une considération importante pour vous. Quelles qu'elles soient, il est utile de rendre ces objectifs de conception explicites. Vous devriez également vous assurer qu'ils sont partagés et compris par votre équipe.

### Découvrabilité

Le manque de découvrabilité n'est pas un nouveau problème. Selon Simon Wardley, il est plutôt rampant dans les gouvernements ainsi que dans le secteur privé. La plupart des organisations manquent d'un moyen systématique pour que les équipes partagent et découvrent le travail des autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xqxvFs3jRv_gc9eePzWf2g.png)
_courtoisie des publications de Simon Wardley sur Twitter_

Comme indiqué précédemment, la découverte consiste à trouver quelles capacités sont disponibles à travers vos fonctions. Savoir quelles fonctions vous avez ne suffit pas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6FC_6slSGi3GyQP_5zMLLw.png)
_Ne demandez pas quelles fonctions vous avez, demandez plutôt ce que vos fonctions peuvent faire._

Un argument que j'entends souvent pour les fonctions monolithiques est qu'elles réduisent le nombre de fonctions, ce qui les rend plus faciles à gérer.

En surface, cela semble avoir du sens. Mais plus j'y pense, plus l'argument semble erroné. Le nombre de fonctions ne serait un obstacle que si nous essayions de les gérer à la main plutôt que d'utiliser les outils disponibles.

Après tout, nous sommes capables de localiser des livres par leur contenu dans un immense espace physique avec des dizaines de milliers de livres. En utilisant l'analogie de la bibliothèque, avec les outils disponibles, nous pouvons cataloguer nos fonctions et les rendre faciles à rechercher.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P9R8YbGTO_zVQH3Owjbrig.png)

Par exemple, le framework [Serverless](https://serverless.com/framework/) impose une convention de nommage simple de `{service}-{stage}-{function}`. Cette convention simple facilite la recherche de fonctions connexes par préfixe. Si je veux trouver toutes les fonctions qui font partie d'une API `user`, je peux le faire en recherchant `user-api`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xNLVK6_Jq7MVZd69Yn3NDg.png)

Avec des tags, nous pouvons cataloguer des fonctions à travers plusieurs dimensions. Par exemple, nous pouvons cataloguer en utilisant l'environnement, le nom de la fonctionnalité, la source de l'événement, l'auteur, et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ck-QETFR0AMVV0OgHP2usQ.png)
_Par défaut, le framework Serverless ajoute le tag STAGE à toutes vos fonctions. Vous pouvez également ajouter vos propres tags, voir la [documentation](https://serverless.com/framework/docs/providers/aws/guide/functions/#tags" rel="noopener" target="_blank" title=") sur la façon d'ajouter des tags._

![Image](https://cdn-media-1.freecodecamp.org/images/1*jAtLpmlp2yjQ4cT3JwUKWQ.png)
_La console de gestion Lambda vous donne également une liste déroulante pratique des valeurs disponibles lorsque vous essayez de rechercher par tag._

Si vous avez une idée approximative de ce que vous cherchez, alors le nombre de fonctions n'est pas un obstacle à votre capacité à découvrir ce qui existe.

Avec des fonctions à usage unique, les capacités de l'API `user-api` sont immédiatement évidentes. Je peux voir à partir des fonctions connexes que j'ai les capacités CRUD de base, car il y a des fonctions correspondantes pour chacune.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C22Wu2wC8uROThTfwyn7iQ.png)
_Je peux voir quelles capacités je possède dans la suite de fonctions qui composent la fonctionnalité user-api._

Avec une fonction monolithique, cependant, ce n'est pas si simple. Il n'y a qu'une seule fonction, mais que peut faire cette fonction ? Je devrais soit regarder le code moi-même, soit consulter l'auteur de la fonction. Pour moi, cela rend la découvrabilité médiocre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o9wXc2rndRZm2hO0ggevtA.png)

À cause de cela, je marque l'approche monolithique comme inférieure en termes de découvrabilité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bXYf0mExyAPrzHuA3wMz2A.png)

Cependant, avoir plus de fonctions signifie qu'il y a plus de pages à parcourir. Cela peut être fastidieux si vous voulez simplement naviguer et voir quelles fonctions existent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Xjwc62Up78CfUs3qwYECg.png)

Bien que, selon mon expérience, cela n'a jamais été un problème en soi. Grâce à la convention de nommage du framework _Serverless_, toutes les fonctions connexes sont proches les unes des autres. C'est en fait assez agréable de voir ce que chaque groupe de fonctions peut faire, plutôt que de devoir deviner ce qui se passe à l'intérieur d'une fonction monolithique.

Mais, cela peut être pénible de parcourir tout lorsque vous avez **des milliers** de fonctions. Donc, je vais pénaliser les fonctions à usage unique pour cela.

À ce niveau de complexité, cependant, regrouper plus de capacités dans chaque fonction ne rendrait le système que plus difficile à comprendre. Supposons que vous avez mille fonctions, et que vous savez ce que chacune fait au premier coup d'œil. Ne serait-il pas plus simple de les remplacer par cent fonctions, mais sans savoir ce que chacune fait ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*xGGFxDFUXcRHNDjopc23eA.png)

### Débogage

Pour le débogage, la question pertinente est de savoir si avoir moins de fonctions facilite l'identification et la localisation du bug.

Selon mon expérience, le chemin d'une erreur à la fonction et au dépôt pertinent est le même, indépendamment du fait que la fonction fasse une chose ou plusieurs choses.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qV9A5t6nXBmulssjGXzfRw.png)

La différence réside dans la façon de trouver le code pertinent à l'intérieur du dépôt pour les problèmes que vous enquêtez.

Une fonction monolithique a plus de logique de branchement. Il faudrait donc plus d'efforts cognitifs pour suivre le code pertinent au problème en question.

Pour cela, je vais légèrement pénaliser les fonctions monolithiques. Bien sûr, nous parlons d'une différence minimale ici, ce qui explique pourquoi la pénalité est également minimale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7BfnhHIlQx0KEqnFIxQa4A.png)

### Mise à l'échelle

Dans les premiers jours des microservices, l'un des arguments en faveur des microservices était qu'ils facilitaient la mise à l'échelle.

Mais ce n'est pas le cas !

Si vous savez comment mettre à l'échelle un système, alors vous pouvez mettre à l'échelle un monolithe aussi facilement que vous pouvez mettre à l'échelle un microservice.

Je dis cela en tant que quelqu'un qui a construit des systèmes backend monolithiques pour des jeux qui avaient un million d'utilisateurs actifs quotidiens (DAU). **Supercell**, le créateur de jeux à gros revenus comme **Clash of Clans** et **Clash Royale**, compte bien plus de 100 millions de DAU. Les systèmes backend de ces jeux sont tous des monolithes, et **Supercell** n'a aucun problème à mettre à l'échelle ces systèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uXFIo5_szcKnh0kd6m3Vxg.png)

Au lieu de cela, des géants technologiques comme Amazon et Google nous ont appris que les microservices facilitent la mise à l'échelle dans une dimension différente — notre équipe d'ingénierie.

Ce style d'architecture nous permet de créer des frontières au sein de notre système, autour des fonctionnalités et des capacités. Il permet à nos équipes d'ingénierie de mettre à l'échelle la complexité de ce qu'elles construisent, car elles peuvent plus facilement construire sur le travail que d'autres ont créé avant elles.

Prenez [Cloud Datastore](https://cloud.google.com/datastore/docs/concepts/overview) de Google comme exemple. Les ingénieurs de cette équipe ont pu produire un service sophistiqué en [construisant sur plusieurs couches de services](http://bit.ly/2CQx3C4). Chaque couche fournit des abstractions puissantes que la couche suivante peut exploiter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cyUwWcGZkfpw4tzlrS8muQ.png)
_[http://bit.ly/2CQx3C4](http://bit.ly/2CQx3C4" rel="noopener" target="_blank" title=")_

Ces frontières nous donnent une plus grande division du travail. Ce qui permet à plus d'ingénieurs de travailler sur le système en leur donnant des zones où ils peuvent travailler en isolation relative. De cette façon, ils ne se gênent pas mutuellement avec des conflits de fusion, des problèmes d'intégration, et ainsi de suite.

Michael Nygard a également écrit un [bel article](https://bit.ly/coherence-penalty) qui explique cet avantage sous un autre angle : que ces frontières et cette isolation nous aident à réduire les frais généraux de partage de modèles mentaux.

> « Si vous avez une pénalité de cohérence élevée et trop de personnes, alors l'équipe dans son ensemble avance plus lentement... Il s'agit de **réduire les frais généraux de partage de modèles mentaux**. »

> - Michael Nygard

Avoir beaucoup de fonctions à usage unique est peut-être l'apogée de cette division des tâches. Vous perdez un peu cette division lorsque vous passez à des fonctions monolithiques. Bien que dans la pratique, vous n'aurez probablement pas autant de développeurs travaillant sur le même projet pour ressentir la douleur.

Restreindre une fonction à une seule chose aide également à limiter la complexité d'une fonction. Pour rendre quelque chose de plus complexe, vous composeriez ces fonctions simples ensemble via d'autres moyens, tels que les **Step Functions** d'AWS.

Je vais pénaliser les fonctions monolithiques pour la perte de division du travail et pour l'augmentation du plafond de complexité d'une fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GNu9RlaxpUhdyTRwyLzozQ.png)

### Conclusion

**Sur la base des critères qui sont importants pour moi**, avoir de nombreuses fonctions à usage unique est la meilleure voie à suivre. Mais je ne vois pas cela comme une règle absolue.

Comme tout le monde, je viens avec un ensemble de préjugés et de biais formés à partir de mes expériences, qui ne reflètent probablement pas exactement les vôtres. Je ne vous demande pas d'être d'accord avec moi. Bien que j'espère que vous apprécierez le processus de détermination de ce qui est important pour vous afin de trouver l'approche qui vous convient.

Mais qu'en est-il des **démarrages à froid** ? Les fonctions monolithiques ne vous aideraient-elles pas à réduire le nombre de démarrages à froid ?

La réponse courte est non, elles ne vous aident pas avec les démarrages à froid de manière significative. C'est aussi le mauvais endroit pour optimiser les démarrages à froid. Si vous êtes intéressé par la version plus longue de cette réponse, veuillez lire mon autre article [ici](https://theburningmonk.com/2018/02/aws-lambda-monolithic-functions-wont-help-you-with-cold-starts/).

Et enfin, avoir des surfaces d'attaque plus petites avec des fonctions à usage unique réduit la surface d'attaque. Vous pouvez donner à chaque fonction la permission exacte dont elle a besoin et rien de plus. C'est un avantage important, mais souvent sous-estimé des fonctions à usage unique.