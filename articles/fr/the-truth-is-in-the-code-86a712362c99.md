---
title: La vérité est dans le code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-21T15:14:26.000Z'
originalURL: https://freecodecamp.org/news/the-truth-is-in-the-code-86a712362c99
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ULvnxNPKHirSW5m9W2XBxA.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La vérité est dans le code
seo_desc: 'By Bertil Muth

  Sooner or later, every software developer will hear something like this:


  “Truth can only be found in one place: the code.”

  – Robert C. Martin, Clean Code


  But what does that mean?

  The Agile Manifesto values “working software over comp...'
---

Par Bertil Muth

Tôt ou tard, chaque développeur de logiciels entendra quelque chose comme ceci :

> « La vérité ne peut être trouvée qu'en un seul endroit : le code. »

> – Robert C. Martin, [Clean Code](https://www.amazon.de/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

Mais que signifie cela ?

Le [Manifeste Agile](http://agilemanifesto.org/) valorise « des logiciels fonctionnels plutôt qu'une documentation exhaustive ».

Les développeurs écrivent une documentation exhaustive du comportement des logiciels tout le temps, cependant. Le code.

Les commentaires de code et les spécifications externes documentent également le comportement du logiciel. Mais ils peuvent ne pas être mis à jour lorsque le code change. Ils cessent alors rapidement de refléter le comportement du logiciel.

En revanche, le code reflète *toujours* le comportement du logiciel. Il le définit.

C'est pourquoi la vérité est dans le code.

### Écrire pour vos lecteurs

Le code est de la documentation. Tout type de documentation doit être compréhensible par ses lecteurs.

Les lecteurs du code sont un compilateur ou un interpréteur, et d'autres développeurs.

Il ne suffit donc pas que votre code compile. D'autres développeurs doivent également le comprendre. Ils devront travailler sur votre code à l'avenir, le modifier et l'étendre.

Une suggestion courante pour rendre le code compréhensible est d'écrire du code propre. Un code qui utilise un langage compréhensible pour les noms de variables et de méthodes. Cela rend également de nombreux commentaires de code inutiles.

Le code propre doit exprimer l'intention : *ce* que quelqu'un peut accomplir en appelant une méthode. Pas *comment* la méthode y parvient.

Devinez ce que fait cette méthode :

```java
BigDecimal addUp(List<BigDecimal> ns){..}
```

Et si on écrivait plutôt ceci :

```java
BigDecimal calculateTotal(List<BigDecimal> individualPrice){..}
```

Le code propre est une bonne idée. Mais je ne pense pas que ce soit suffisant.

### L'importance d'une compréhension partagée

Lorsqu'il y a une nouvelle exigence, vous devez comprendre comment sa mise en œuvre affecte le code existant.

Cela peut être un défi si votre logiciel existe depuis un certain temps. Très souvent, j'ai entendu un dialogue comme celui-ci :

_X_ : Nous ne pouvons pas continuer avec la fonctionnalité _foo_.

_Y_ : Pourquoi ?

_X_ : Parce que _Z_ est le seul à connaître le code. Il a implémenté le code que nous devons modifier maintenant.

_Y_ : Eh bien, pourquoi ne pas lui demander ?

_X_ : Parce qu'il est malade / en vacances / à une conférence / n'est plus dans l'entreprise.

_Y_ : Oh...

Voici le problème. Pour savoir si votre code est compréhensible, quelqu'un d'autre devrait essayer de le comprendre.

Il existe des techniques pour cela. Le [Pair programming](https://en.m.wikipedia.org/wiki/Pair_programming) en est une bonne. Ou vous vous asseyez avec d'autres développeurs. Vous leur expliquez le code que vous avez écrit.

Pourtant, que se passe-t-il si de nombreux développeurs sont impliqués dans un produit ? Que se passe-t-il si les équipes de développement changent de membres ? Cela rend plus difficile l'écriture de code que suffisamment d'autres personnes comprennent.

### L'histoire

Le code propre vous donne les bons *mots*.

La question est : quelle *histoire* allez-vous raconter avec eux dans votre code ?

Je n'en ai aucune idée.

Mais pour une application métier typique, je suis assez sûr de l'histoire que je veux lire dans le code.

Après vous avoir présenté un bref exemple, je vais esquisser cette histoire.

### L'exemple du magasin de gants

En tant qu'utilisateur de logiciel, je veux [atteindre un résultat souhaité](https://medium.freecodecamp.com/nobody-wants-to-use-software-a75643bee654?source=linkShare-a74297325869-1489339708). Par exemple, je veux posséder une nouvelle paire de gants pour garder mes doigts au chaud en hiver.

Je vais donc en ligne et je vois qu'il y a un nouveau magasin en ligne spécialisé dans les gants. Le site web du magasin me permet d'acheter des gants. Le « flux de base » (également appelé « scénario de jour heureux ») du cas d'utilisation pourrait ressembler à ceci :

* Le système commence avec un panier vide.
* Le système affiche une liste de gants.
* J'ajoute les gants que j'aime au panier. Le système ajoute les gants à ma commande.
* Je passe à la caisse.
* Je saisis les informations de livraison et les détails de paiement. Le système enregistre ces informations.
* Le système affiche un résumé de la commande.
* Je confirme. Le système initie l'expédition de ma commande.

Après quelques jours, je reçois mes gants.

### Voici l'histoire que je veux lire dans le code.

### Chapitre 1 : Cas d'utilisation

Le premier chapitre de l'histoire concerne les cas d'utilisation. Lorsque je lis du code, je veux suivre un cas d'utilisation dans le code étape par étape jusqu'au résultat souhaité.

Je veux comprendre comment le système réagit lorsque quelque chose ne va pas. Du point de vue d'un utilisateur.

Je veux également comprendre les différents chemins possibles. L'utilisateur essaie de revenir des détails de paiement aux informations de livraison, par exemple. Que se passe-t-il ? Est-ce même possible ?

Je veux comprendre quel code regarder pour chaque partie d'un cas d'utilisation.

#### Quelles sont donc les *parties* d'un cas d'utilisation ?

La partie fondamentale d'un cas d'utilisation est une *étape* qui rapproche un utilisateur d'un résultat souhaité. Par exemple : « Le système affiche une liste de gants. »

Tous les utilisateurs ne peuvent pas exécuter une étape, mais seulement les membres de certains groupes d'utilisateurs (les *acteurs*). Les clients finaux achètent des gants. Les responsables marketing saisissent de nouvelles offres de gants dans le système.

Le système exécute certaines des étapes de lui-même. Comme lorsqu'il affiche les gants. Aucune interaction utilisateur nécessaire là.

Ou une étape est une interaction avec l'utilisateur. Le système *réagit* à un certain *événement utilisateur*. Par exemple : L'utilisateur saisit les informations de livraison. Le système enregistre les informations.

Je veux comprendre quelles *données* attendre avec l'événement. Les informations de livraison incluent le nom de l'utilisateur, l'adresse, etc.

L'utilisateur ne peut exécuter qu'un sous-ensemble d'étapes à un moment donné. L'utilisateur ne peut saisir les détails de paiement qu'après les informations de livraison. Il y a donc un *flux* qui définit l'ordre des étapes dans un cas d'utilisation. Et une *condition* qui définit si le système peut réagir, en fonction de l'état du système.

#### Pour comprendre le code, vous avez besoin d'un moyen facile de savoir plusieurs choses.

Pour un cas d'utilisation (comme « acheter des gants ») :

* Le ou les *flux* d'*étapes*

Pour chaque étape :

* Quels *acteurs* y ont accès (c'est-à-dire, quels groupes d'utilisateurs)
* Sous quelle *condition* le système réagit
* Si l'étape est *autonome*, ou basée sur une *interaction utilisateur*
* La *réaction* du *système*

Pour chaque étape qui est une interaction utilisateur :

* L'*événement utilisateur* (comme « l'utilisateur a saisi les informations de livraison »)
* Les *données* qui accompagnent l'événement

Une fois que je sais où trouver un cas d'utilisation et ses parties dans le code, je peux creuser plus profondément.

### Chapitre 2 : Décomposer les choses en étapes à travers les composants

Appelons un bloc de construction encapsulé et remplaçable de votre logiciel un *composant*. Les *responsabilités* d'un composant sont disponibles pour le monde extérieur au composant.

Un composant pourrait être :

* un composant technique comme un dépôt de base de données,
* un service comme « service de panier d'achat »,
* une entité dans votre modèle de domaine.

Cela dépend de la conception de votre logiciel. Mais peu importe ce que sont vos composants : vous avez généralement besoin de plusieurs d'entre eux pour réaliser une étape d'un cas d'utilisation.

Examinons la *réaction du système* de l'étape « Le système affiche une liste de gants ». Vous devez probablement développer au moins deux *responsabilités*. L'une trouve les gants dans la base de données, et l'autre transforme la liste de gants en une page web.

Lorsque je lis du code, je veux comprendre les choses suivantes :

* Quelles sont les *responsabilités* d'un composant. Par exemple : « trouver des gants » pour le dépôt de base de données.
* Quels sont les *entrées* / *sorties* de chaque responsabilité. Exemple d'entrée : critères pour trouver quels gants. Exemple de sortie : liste de gants.
* Qui *coordinate* les responsabilités. Par exemple : trouver les gants en premier. Transformer le résultat en une page web en second.

### Chapitre 3 : Ce que font les composants

Le code d'un composant remplit des responsabilités.

Cela se produit souvent dans un *modèle de domaine*. Le modèle de domaine utilise des termes pertinents dans le domaine métier.

Pour l'exemple, un terme pourrait être Gant. Un autre terme pourrait être Commande.

Le modèle de domaine décrit les *données* pour chaque terme. Chaque Gant a une couleur, une marque, une taille, un prix, etc.

Le modèle de domaine décrit également les calculs sur les données. Le prix total d'une Commande est la somme des prix de chaque Gant acheté par l'utilisateur.

Un composant peut également être un composant technique comme un dépôt de base de données. Le code doit répondre à la question : Comment le dépôt crée, trouve, met à jour et supprime des éléments dans la base de données ?

### Raconter votre histoire

Peut-être que votre histoire ressemble à celle ci-dessus. Peut-être qu'elle est différente. Quelle que soit votre histoire, les langages de programmation vous donnent une grande liberté pour vous exprimer et raconter cette histoire.

C'est une bonne chose car cela permet aux développeurs de s'adapter à différents contextes et exigences.

Cela comporte également le risque que les développeurs racontent trop d'histoires différentes. Même pour le même produit. Cela rend plus difficile que nécessaire la compréhension du code écrit par quelqu'un d'autre.

Une façon d'aborder cela est l'utilisation de modèles de conception. Ils vous permettent de structurer votre code. Vous pouvez convenir de cette structure commune dans votre équipe ou même entre les équipes.

Par exemple, le framework Rails est basé sur le modèle bien connu Modèle-Vue-Contrôleur.

Le modèle est l'endroit pour les *données* de *domaine*.

La vue est l'interface utilisateur côté client, comme les pages HTML. C'est l'origine des *événements* *utilisateur*.

Le contrôleur reçoit les événements utilisateur côté serveur. Il est responsable du *flux*.

Ainsi, si plusieurs développeurs utilisent Rails, ils savent quelle partie du code regarder pour certaines parties de leur histoire.

Ils pourraient découvrir ce qui manque en partageant leur compréhension. Ensuite, ils pourraient convenir de conventions supplémentaires sur l'endroit où mettre quelle partie de leur histoire.

Si cela fonctionne pour vous, c'est très bien. Mais je veux aller plus loin que cela.

### Exigences en tant que Code

De nombreux clients me demandent comment gérer la documentation logicielle à long terme.

Lorsqu'on travaille dans un contexte agile, comment créer de la documentation pour la maintenance logicielle ?

Quelles exigences ont été mises en œuvre jusqu'à présent ?

Où trouve-t-on leur réalisation dans le code ?

Pendant longtemps, je n'ai pas eu de réponse satisfaisante. Sauf, bien sûr : l'importance de tests bien écrits et automatisés. Un code de production propre. Une compréhension partagée.

Mais il y a quelques années, j'ai commencé à réfléchir :

> Si la vérité est dans le code, le code devrait être capable de dire la vérité.

En d'autres termes : si vous avez pris grand soin de raconter votre histoire dans le code, pourquoi voudriez-vous la raconter à nouveau ?

Il doit y avoir une meilleure façon. Il doit être possible d'extraire l'histoire et de générer de la documentation à partir de celle-ci. Une documentation que les parties prenantes non techniques comprennent également.

Une documentation qui est toujours à jour, car elle provient de la même source qui définit le comportement du logiciel.

La seule source fiable : le code lui-même.

Après de nombreuses expériences, j'ai obtenu quelques résultats. Je les ai rendus publics dans un projet Github appelé [requirements as code](https://github.com/bertilmuth/requirementsascode).

### Comment cela fonctionne

![Image](https://cdn-media-1.freecodecamp.org/images/8sBsUlQ3QJV4Vp7Cp29ojArqvcxcjNDc63TL)

* Une instance de Modèle définit les *acteurs*, les *cas d'utilisation*, leurs *flux* et *étapes*. Elle raconte le chapitre 1 de l'histoire. Vous trouverez un exemple d'un tel modèle au début de cet article.
* Un modèle configure des instances de ModelRunner. Chaque utilisateur a son propre runner, car chaque utilisateur peut suivre un chemin différent à travers les cas d'utilisation dans le modèle.
* Le runner réagit à un *événement utilisateur* du frontend en appelant la *réaction du système* dans le backend. Le frontend communique avec le backend uniquement via le runner.
* Mais le runner ne réagit que si l'utilisateur est à la bonne position du *flux* et que la *condition* de l'étape est remplie. Par exemple, le runner ne réagit à l'événement « EnterPaymentDetails » que si l'utilisateur a saisi les informations de livraison juste avant.
* La *réaction* du *système* est une méthode unique. Le corps de la méthode est responsable de la coordination des composants pour réaliser l'étape, comme décrit dans le chapitre 2.
* Le chapitre 3 est hors du champ d'application des exigences en tant que code. Il est laissé à l'application. Cela rend les exigences en tant que code compatibles avec des conceptions logicielles arbitraires.

Ainsi, le ModelRunner contrôle le comportement visible par l'utilisateur du logiciel. Basé sur un Modèle.

Avec [requirements as code extract](https://github.com/bertilmuth/requirementsascode/tree/master/requirementsascodeextract), vous pouvez générer de la documentation à partir du même modèle qui configure le runner. De cette manière, la documentation reflète toujours le fonctionnement du logiciel.

Requirements as code extract utilise le moteur de template FreeMarker. Cela vous permet de générer n'importe quelle documentation en texte brut que vous souhaitez. Par exemple, des pages HTML. Un traitement supplémentaire pourrait la transformer en d'autres formats de documentation, comme PDF.

### Vos commentaires m'aideront à améliorer ce projet

J'ai commencé à travailler sur les exigences en tant que code il y a plusieurs années. Cela a connu des améliorations significatives depuis le début.

Pour savoir si l'approche est évolutive, je l'ai essayée sur une application de plusieurs milliers de lignes de code. Cela a fonctionné. Je l'ai également essayée sur des applications plus petites.

Pourtant, jusqu'à présent, les exigences en tant que code ont été mon projet de loisir.

C'est pourquoi j'ai besoin de votre aide. Veuillez me donner votre avis.

Que pensez-vous de l'idée ? Pouvez-vous imaginer que cela fonctionne dans le contexte du logiciel que vous développez ? Tout autre commentaire ?

Vous pouvez me laisser un message dans les commentaires ou me contacter sur [Twitter](https://twitter.com/BertilMuth) ou [LinkedIn](https://www.linkedin.com/in/bertilmuth).

Vous pouvez [cloner](https://github.com/bertilmuth/requirementsascode) le projet et l'essayer vous-même.

Ou vous pouvez [contribuer](https://github.com/bertilmuth/requirementsascode/blob/master/CONTRIBUTING.md) à documenter la vérité dans le code.

_Modifié le 16 octobre 2018 : adapté à la version v1.0.0 des exigences en tant que code_