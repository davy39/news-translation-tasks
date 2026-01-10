---
title: Comment implémenter l'algorithme Paxos en fonctions pures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-29T18:06:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-paxos-algorithm-in-pure-functions
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Paxos-Made-Functional-Background-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Functional Programming
  slug: functional-programming
seo_title: Comment implémenter l'algorithme Paxos en fonctions pures
seo_desc: "By Edward Huang\nImagine that you are on a football team. After practice,\
  \ the team loves to go out together and eat. \nLet's say that the team usually wants\
  \ to eat pizza or burgers. However, you want the whole team to go out to the same\
  \ place after pra..."
---

Par Edward Huang


Imaginez que vous faites partie d'une équipe de football. Après l'entraînement, l'équipe aime sortir ensemble et manger.

Disons que l'équipe veut généralement manger de la pizza ou des burgers. Cependant, vous voulez que toute l'équipe aille au même endroit après l'entraînement parce que c'est plus amusant comme ça.

Par conséquent, vous devez faire en sorte que l'équipe se mette d'accord sur le terrain de football où tout le monde va – manger des burgers ou de la pizza.

Mais il y a un problème : l'entraîneur est rentré tôt. Tout le monde est épuisé et affamé après l'entraînement, donc ils se distraient facilement et veulent prendre une décision rapidement.

De plus, vous ne pouvez pas crier sur le terrain de football parce que toute l'équipe a tendance à parler très fort, et votre suggestion pourrait être facilement écrasée par une autre personne.

Vous devez penser, "Il n'y a qu'une seule façon pour moi d'atteindre cet accord – par la communication de personne à personne, et je veux que tout le monde atteigne un consensus."

Comment allez-vous résoudre ce problème ?

Cette analogie est le même problème que nous rencontrons dans les systèmes distribués, mais cette fois, vous traitez avec de nombreux serveurs. Nous voulons que de nombreux serveurs se mettent d'accord sur des événements communs ou des informations communes dans un environnement asynchrone.

Vous pouvez utiliser de nombreux algorithmes pour résoudre les problèmes, et aujourd'hui nous allons parler de l'un d'eux : l'algorithme Paxos.

Paxos est l'un des premiers articles publiés sur cet algorithme de consensus distribué qui exécute des rounds et des rounds pour aider de nombreux serveurs à se mettre d'accord sur une valeur proposée par un membre du groupe.

L'algorithme utilise la communication pair-à-pair, où chaque pair peut jouer trois rôles : le proposeur, l'accepteur et l'apprenant. Ces rôles n'ont pas besoin d'être séparés sur chaque serveur – ce qui signifie qu'un serveur peut avoir le rôle d'apprenant, d'accepteur et de proposeur en même temps.

Revenons à l'analogie du football ci-dessus, pour simplifier, nous séparons les trois rôles. La moitié de l'équipe peut être le proposeur, un quart peut être l'accepteur, et un quart peut être l'apprenant.

Le proposeur peut proposer où ils veulent aller manger à l'accepteur. L'accepteur aura certains critères pour déterminer, en fonction de chaque valeur proposée, quel endroit ils choisiront. Une fois que l'accepteur choisit la majorité des messages proposés, ils les enverront à l'apprenant.

Par exemple, l'un des accepteurs choisit un burger. Ils disent à l'apprenant que la majorité de l'équipe veut manger un burger. Cependant, c'est là que cela devient intéressant : un autre accepteur choisit une pizza, et ils disent à l'apprenant que la majorité de l'équipe veut manger une pizza.

Par conséquent, c'est à l'apprenant d'annoncer, en fonction du message qu'il reçoit de tous les accepteurs, ce que la majorité veut vraiment manger. L'algorithme continuera à exécuter plusieurs itérations jusqu'à ce que l'apprenant annonce le consensus.

Je vais expliquer l'algorithme Paxos plus en détail dans cet article ainsi que son implémentation. À la fin de cet article, vous saurez comment fonctionne une machine à états de réplication dans un système distribué et l'algorithme principal utilisé dans le protocole Chubby [protocole](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf).

## Avant de commencer

Dans cet article, nous ne discuterons pas du "pourquoi" et des étapes que l'algorithme suit pour atteindre un consensus. Si vous êtes intéressé par le fonctionnement de l'algorithme Paxos, vous pouvez consulter une excellente brève introduction dans ce Google [Tech Talk](https://www.youtube.com/watch?v=d7nAGI_NZPk).

Deuxièmement, je suppose que la preuve et la théorie fonctionnent, et cet article sera principalement consacré à l'implémentation.

## Une brève introduction à l'algorithme Paxos

Il y a 3 rôles dans l'algorithme Paxos – le proposeur, les accepteurs et l'apprenant.

Le proposeur proposera une valeur en envoyant des messages à un autre membre du groupe.

Les accepteurs accepteront la valeur proposée.

L'apprenant apprend si le groupe a atteint un consensus lors d'un round particulier de l'algorithme.

L'algorithme Paxos se déroule en deux phases (la phase de préparation et la phase d'acceptation) comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Paxos-Role-Simple-Diagram.png)

### La phase de préparation

Chaque proposeur du groupe sélectionne un numéro de proposition et envoie une demande préparée à l'accepteur du système. Le message n'a pas besoin d'être reçu par tous. Il suffit qu'il soit reçu par la majorité (un quorum) pour que l'algorithme puisse continuer.

L'accepteur qui reçoit ce message comparera le numéro de proposition actuel le plus élevé. Si la demande entrante est supérieure au numéro de proposition, il l'acceptera et enverra un message d'espoir en retour disant à la proposition, "okay, votre proposition est plus élevée que ce que j'ai actuellement, donc je vais vous choisir."

Si l'accepteur a déjà accepté un message, il enverra la même chose, sauf qu'il dira, "okay, votre proposition est plus élevée que ce que j'ai actuellement. Cependant, j'ai déjà accepté une proposition de message. Je vais joindre ce numéro de proposition et cette valeur dans le message aussi."

Si l'accepteur reçoit le message avec un numéro de proposition inférieur, il l'ignorera simplement.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Prepare-Phase.png)

### La phase d'acceptation

Si le proposeur reçoit une réponse de promesse de la majorité, il vérifiera si des messages promis ont un message accepté. S'il y a un message d'acceptation, la proposition acceptera le message pour envoyer la demande d'acceptation au processeur à nouveau.

Supposons que le proposeur ne reçoit pas de réponses de la plupart des accepteurs auxquels il diffuse son message. Dans ce cas, il supposera simplement que "mon numéro de proposition n'est pas assez élevé, je vais créer un numéro de proposition plus élevé et le diffuser à nouveau à l'accepteur."

Si le proposeur reçoit des réponses de la majorité des accepteurs, il informera l'apprenant qu'il a atteint un consensus.

Supposons qu'un accepteur reçoit une demande d'acceptation avec le numéro de proposition égal à ses promesses. Dans ce cas, il enverra une confirmation à ce proposeur que la valeur de la proposition est acceptée.

Si un accepteur reçoit une demande d'acceptation avec un numéro de proposition inférieur à la demande préparée, il l'ignore simplement.

Du côté de l'apprenant, une fois qu'il reçoit la majorité (quorum) de la valeur provenant de la proposition, il marquera qu'il a atteint un consensus.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Accept-Case.png)

En théorie, cela semble simple. Cependant, en pratique, il y a beaucoup de cas à prendre en compte. Plusieurs [articles](https://static.googleusercontent.com/media/research.google.com/en//archive/paxos_made_live.pdf) parlent de leur expérience dans l'implémentation de Paxos dans leurs systèmes de production.

J'ai vu de nombreuses sources implémenter Paxos sur la base d'un langage orienté objet, comme l'implémentation Java [implémentation](https://github.com/cocagne/paxos#cocagnepaxosessential) ou l'implémentation avec le [système d'acteurs](https://github.com/ahanwadi/paxos). J'ai donc pensé, "pourquoi ne pas essayer d'en implémenter un en termes de programmation fonctionnelle ?"

Veuillez noter que cette implémentation est basée sur l'article de l'algorithme Paxos simplifié. Elle n'a pas d'invariant sophistiqué tel qu'un compte pour les défaillances de machine, l'élection de leader, etc. Cette implémentation implémente également un algorithme Paxos de base à un seul round.

## Le défi

### Construction du modèle

L'essence de l'algorithme Paxos est la communication entre les nœuds. Par conséquent, il sera plus intuitif de modéliser le rôle en tant qu'objets.

Puisqu'il mentionne comment les proposeurs, les accepteurs et les apprenants interagissent, un système d'acteurs est le moyen le plus simple de créer l'algorithme. Nous pouvons avoir 3 acteurs et encapsuler la logique et l'état au sein des acteurs.

### Gestion de l'état immuable

Cela peut être un défi si nous voulons implémenter quelque chose d'immuable par nature, car l'algorithme nécessite un changement constant de l'état interne. La programmation orientée objet peut encapsuler la gestion de l'état pour les proposeurs, les accepteurs et les apprenants. Dans chacune de ces phases, nous pouvons muter l'état à l'intérieur de chaque instance.

Par exemple, une instance d'accepteur peut avoir un max_id en tant qu'état interne mutable, et elle peut changer le max_id si elle reçoit un message préparé qui contient un numéro d'id plus élevé.

## Comment implémenter l'algorithme Paxos de manière fonctionnelle

Discutons de la manière d'implémenter l'algorithme Paxos de manière fonctionnelle, et de la manière de concevoir cette implémentation. J'utiliserai Scala et exploiterai la bibliothèque de données cats pour ne pas réinventer la roue de la création de ses propres instances de monade et de sa loi.

### Modèles de domaine

Commençons par chacun des modèles de domaine. La manière la plus simple de procéder est de visualiser ce dont le proposeur, l'accepteur et l'apprenant ont besoin.

### Modèle de proposeur

Le proposeur consistera en une valeur, un numéro de proposition et une taille de quorum. Le numéro de proposition doit être unique et croissant. La manière courante d'implémenter ce numéro de proposition est un identifiant avec un identifiant de machine pour garantir l'unicité.

<script src="https://gist.github.com/edwardGunawan/9bae19520c83d074937eb986f5a734d4.js"></script>


L'instruction de comparaison est équivalente à un comparateur Java où vous pouvez vérifier si l'un est égal à l'autre.

La taille du quorum est le nombre de nœuds dans le système.

### Modèle d'accepteur

L'accepteur se compose d'un numéro de proposition de promesse et du numéro de proposition et de la valeur qu'il accepte. Puisque ces deux valeurs peuvent ne pas exister, rendons-les optionnelles.

<script src="https://gist.github.com/edwardGunawan/f6749b1bd04ea6080356f19788da03e1.js"></script>

### Modèle d'apprenant

L'apprenant doit garder une trace de toutes les réponses acceptées qu'il reçoit et vérifier si la valeur entrante est supérieure à la majorité. Par conséquent, il doit avoir une cartographie clé-valeur pour garder une trace de ces comptes.

La clé sera la valeur acceptée, et la valeur sera le nombre de comptes. Pour connaître la majorité, il doit avoir la taille du quorum. De plus, il doit y avoir un moyen de choisir une valeur lorsqu'elle est supérieure à la majorité.

Par conséquent, l'apprenant aura une taille de quorum, une cartographie des valeurs acceptées jusqu'à présent, et la valeur finale qui est choisie.

<script src="https://gist.github.com/edwardGunawan/b10f028898956e3a3a8b7572f747d0aa.js"></script>

Habituellement, en OOP, nous plaçons les fonctions à l'intérieur du modèle, et sa fonction mutera l'état du modèle.

Fonctionnellement, j'ai décidé de séparer les fonctions dans leur propre objet, `Ops`, qui peut interagir avec le proposeur. Cela sépare le modèle et l'opération afin que nous séparions les préoccupations concernant la mutation de l'état.

### Messages

Ensuite, nous réfléchirons au type de message pour communiquer pour chaque algorithme en deux phases. Il y a quatre types de messages au total :

* `messagePreapre`
* `messagePromise`
* `messageAccept`
* `messageAccepted`

Combinons ces messages en un trait scellé.

<script src="https://gist.github.com/edwardGunawan/74f270702d7c1fdf5e912d18e5410412.js"></script>

Puisqu'un accepteur n'a peut-être pas accepté de proposition lors de la réponse à une demande de promesse, nous utiliserons un type Option pour intégrer la `AcceptedValue` dans le message `Accept`.

### Action

L'un des avantages de l'implémentation de Paxos ou de tout autre algorithme de consensus en fonctions pures est que nous commençons à penser à placer tous les effets secondaires IO dans un seul composant.

Il existe de nombreuses façons de pousser la frontière des IO à la [fin du monde](https://stackoverflow.com/questions/13340458/what-does-the-world-mean-in-functional-programming-world). Cependant, une manière facile de faire cela est de changer l'instruction en une valeur.

Par conséquent, nous définirons un type `Action` dans l'implémentation. Ce type `Action` sera un type de valeur qui décrit tous les effets secondaires impurs requis par le protocole.

Par exemple, dans Paxos, l'effet secondaire du protocole envoie des messages à d'autres machines et processus. Par conséquent, ce type d'action contient `Broadcast` et `Send`, qui diffuseront le proposeur soit au groupe d'accepteurs, soit au groupe d'apprenants.

Par conséquent, le co-produit Action aura quelque chose comme ceci :

<script src="https://gist.github.com/edwardGunawan/8d7ce27c8a85407c940abf225bb82e76.js"></script>

### Comment créer une logique de gestion de messages pure

Une fois que nous avons séparé les effets impurs de l'algorithme, nous pouvons nous concentrer sur la gestion principale de l'état de l'algorithme.

Comment pouvons-nous gérer la gestion de l'état sans mutation ?

Une façon de faire cela est que chaque fonction sera enveloppée dans une monade `State`. Une monade d'état est une monade qui prend l'état précédent et retourne un nouvel état avec certains résultats.

Si vous n'êtes pas familier avec cela, consultez mon précédent article de blog sur les monades d'état [ici](https://edward-huang.com/scala/functional-programming/monad/programming/2020/12/21/must-know-patterns-for-constructing-stateful-programs-without-any-mutation/).

Par conséquent, nous pouvons avoir une fonction qui a un wrapper de `State[Proposer, Action]`, ce qui se traduit par `Proposer => (Proposer, Action)`.

Pour simplifier la conception, j'ai créé trois objets `Ops` – `ProposerOps`, `AcceptorOps` et `LearnerOps` – pour simplifier la conception de l'implémentation.

Ce type de conception est influencé par la manière dont le système d'acteurs ou la manière orientée objet d'implémenter l'algorithme sépare chacune des opérations à l'intérieur de l'objet de rôle. Le code est plus modulaire et propre de cette manière.

<script src="https://gist.github.com/edwardGunawan/4db7adb40e149ed19d10d09227545ed4.js"></script>

Chacune des fonctions d'opération à l'intérieur de la classe d'objet `Ops` effectuera l'action pour muter le rôle.

Par exemple, examinons la phase de préparation sur l'accepteur. L'accepteur reçoit le `PrepareMessage` et évalue si le `proposalId` est le `proposalId` actuel maximum vu jusqu'à présent.

Si le `proposalId` est le `proposalId` maximum vu jusqu'à présent, il répondra avec un `PromiseMessage`. Si la valeur est inférieure à l'identifiant maximum actuel, il l'ignorera.

<script src="https://gist.github.com/edwardGunawan/0d56c182f0c8c2a129e59761c85919a1.js"></script>

Par conséquent, la plupart des fonctions auront des définitions de fonction comme ceci :

<script src="https://gist.github.com/edwardGunawan/ee2e032f31283ce66a8b248f9357e112.js"></script>

Avec cela, la logique principale de l'algorithme devient sans état – elle ne se soucie pas vraiment de l'état interne et du processus de chaque machine.

Nous avons créé une gestion d'état pure. Cela rend le test et le débogage de l'algorithme Paxos plus faciles. La partie importante ici est que la méthode `Action` peut être exécutée par d'autres fonctions en dehors de l'algorithme Paxos pour appeler ces appels d'effets secondaires.

## En conclusion

Nous venons d'implémenter un algorithme Paxos dans un style fonctionnel pur. Cela peut être assez difficile à implémenter car l'algorithme dans l'article est un algorithme avec état. Vous devez garder une trace de chaque état pour atteindre un consensus.

Néanmoins, nous adoptons l'approche de séparer tous les algorithmes en deux logiques – la fonctionnalité impure et la gestion principale de l'état.

Séparer les IO et la logique de gestion principale de l'état dans l'algorithme est le plus grand avantage pour rendre l'algorithme testable même dans un environnement concurrent.

De plus, nous rendons chaque logique de gestion de messages aussi sans état que possible – chaque appel peut se terminer sans consulter les états internes de chaque machine ou processus.

Enfin, construire toute votre algèbre et tous les messages dont elle a besoin au début aide vraiment à façonner l'implémentation de l'algorithme lui-même.

Le reste de l'implémentation du code se trouve sur ce GitHub [ici](https://github.com/edwardGunawan/Blog-Tutorial/tree/master/ScalaTutorial/paxos/src/main/scala/paxos).

Si vous êtes intéressé à en apprendre davantage sur l'algorithme Paxos et son implémentation, vous pouvez consulter ces ressources :

* [scala-composable-paxos/Learner.scala at master · cocagne/scala-composable-paxos · GitHub](https://github.com/cocagne/scala-composable-paxos/blob/master/src/main/scala/com/github/cocagne/composable_paxos/Learner.scala)
* [Comprendre Paxos](https://understandingpaxos.wordpress.com/)
* [Paxos en Haskell](https://www.scs.stanford.edu/14sp-cs240h/projects/ma.pdf)

Merci d'avoir lu ! Si vous avez aimé cet article, n'hésitez pas à vous [abonner](https://edward-huang.com/subscribe/) à ma newsletter pour plus d'articles comme celui-ci.