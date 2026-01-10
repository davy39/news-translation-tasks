---
title: Un bref aperçu de la conception de logiciels orientés objet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T01:18:13.000Z'
originalURL: https://freecodecamp.org/news/a-short-overview-of-object-oriented-software-design-c7aa0a622c83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DuIQNSG6UjcEXpskd4_dEQ.jpeg
tags:
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Un bref aperçu de la conception de logiciels orientés objet
seo_desc: 'By Stanislav Kozlovski

  Demonstrated by implementing a Role-Playing Game’s classes


  _[Zeppelin by Richard Wright](https://www.artstation.com/artwork/rO8e6" rel="noopener"
  target="blank" title=")

  Introduction

  Most modern programming languages support a...'
---

Par Stanislav Kozlovski

#### Démonté par la mise en œuvre des classes d'un jeu de rôle

![Image](https://cdn-media-1.freecodecamp.org/images/1*DuIQNSG6UjcEXpskd4_dEQ.jpeg)
_[Zeppelin par Richard Wright](https://www.artstation.com/artwork/rO8e6" rel="noopener" target="_blank" title=")_

### Introduction

La plupart des langages de programmation modernes supportent et encouragent la programmation orientée objet (POO). Même si récemment nous semblons voir un léger changement par rapport à cela, car les gens commencent à utiliser des langages qui ne sont pas **fortement** influencés par la POO (comme Go, Rust, Elixir, Elm, Scala), la plupart ont toujours des objets. Les principes de conception que nous allons décrire ici s'appliquent également aux langages non-POO.

Pour réussir à écrire un code clair, de haute qualité, maintenable et extensible, vous devrez connaître les principes de conception qui se sont avérés efficaces au fil des décennies d'expérience.

**Divulgation :** L'exemple que nous allons parcourir sera en **Python.** Les exemples sont là pour prouver un point et peuvent être négligés dans d'autres façons évidentes.

### Types d'objets

Puisque nous allons modéliser notre code autour des objets, il serait utile de différencier leurs différentes responsabilités et variations.

Il existe trois types d'objets :

#### 1. Objet Entité

Cet objet correspond généralement à une entité du monde réel dans l'espace problème. Supposons que nous construisons un jeu de rôle (RPG), un objet entité serait notre classe `Hero` simple :

Ces objets contiennent généralement des propriétés sur eux-mêmes (comme `health` ou `mana`) et sont modifiables selon certaines règles.

#### 2. Objet de Contrôle

Les objets de contrôle (parfois aussi appelés **objets Manager**) sont responsables de la coordination d'autres objets. Ce sont des objets qui **contrôlent** et utilisent d'autres objets. Un excellent exemple dans notre analogie RPG serait la classe `Fight`, qui contrôle deux héros et les fait combattre.

Encapsuler la logique d'un combat dans une telle classe vous offre plusieurs avantages : l'un d'eux est l'extensibilité facile de l'action. Vous pouvez très facilement passer un type de personnage non-joueur (NPC) pour que le héros combatte, à condition qu'il expose la même API. Vous pouvez également très facilement hériter de la classe et remplacer certaines des fonctionnalités pour répondre à vos besoins.

#### 3. Objet Frontière

Ce sont des objets qui se situent à la frontière de votre système. Tout objet qui prend des entrées ou produit des sorties vers un autre système — qu'il s'agisse d'un utilisateur, d'Internet ou d'une base de données — peut être classé comme un objet frontière.

Ces objets frontière sont responsables de la traduction des informations vers et depuis notre système. Dans un exemple où nous prenons des commandes utilisateur, nous aurions besoin de l'objet frontière pour traduire une entrée clavier (comme la barre d'espace) en un événement de domaine reconnaissable (comme un saut de personnage).

#### Bonus : Objet Valeur

Les [objets valeur](https://en.wikipedia.org/wiki/Value_object) représentent une valeur simple dans votre domaine. Ils sont immuables et n'ont pas d'identité.

Si nous devions les incorporer dans notre jeu, une classe `Money` ou `Damage` serait un excellent choix. Ces objets nous permettent de distinguer, trouver et déboguer facilement les fonctionnalités associées, tandis que l'approche naïve consistant à utiliser un type primitif — un tableau d'entiers ou un entier — ne le permet pas.

Ils peuvent être classés comme une sous-catégorie des objets `**Entité**`.

### Principes Clés de Conception

Les principes de conception sont des règles en conception logicielle qui se sont avérées précieuses au fil des ans. Les suivre strictement vous aidera à garantir que votre logiciel est de qualité irréprochable.

#### Abstraction

L'abstraction est l'idée de simplifier un concept à ses éléments essentiels dans un certain contexte. Elle vous permet de mieux comprendre le concept en le réduisant à une version simplifiée.

Les exemples ci-dessus illustrent l'abstraction — regardez comment la classe `Fight` est structurée. La façon dont vous l'utilisez est aussi simple que possible — vous lui donnez deux héros comme arguments lors de l'instanciation et appelez la méthode `fight()`. Rien de plus, rien de moins.

L'abstraction dans votre code doit suivre la [règle de la moindre surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). Votre abstraction ne doit surprendre personne avec un comportement ou des propriétés inutiles et sans rapport. En d'autres termes — elle doit être intuitive.

Notez que notre fonction `Hero#take_damage()` ne fait pas quelque chose d'inattendu, comme supprimer notre personnage à la mort. Mais nous pouvons nous attendre à ce qu'elle tue notre personnage si sa santé passe en dessous de zéro.

#### Encapsulation

L'encapsulation peut être considérée comme la mise de quelque chose dans une capsule — vous limitez son exposition au monde extérieur. En logiciel, restreindre l'accès aux objets et propriétés internes aide à l'intégrité des données.

L'encapsulation boite noire la logique interne et rend vos classes plus faciles à gérer, car vous savez quelle partie est utilisée par d'autres systèmes et quelle partie ne l'est pas. Cela signifie que vous pouvez facilement retravailler la logique interne tout en conservant les parties publiques et être sûr de ne rien avoir cassé. En effet secondaire, travailler avec la fonctionnalité encapsulée depuis l'extérieur devient plus simple car vous avez moins de choses à considérer.

Dans la plupart des langages, cela est fait par le biais des soi-disant [modificateurs d'accès](https://en.wikipedia.org/wiki/Access_modifiers) (privé, protégé, etc.). Python n'est pas le meilleur exemple de cela, car il manque de tels modificateurs explicites intégrés dans le runtime, mais nous utilisons des conventions pour contourner cela. Le préfixe `_` aux variables/méthodes les désigne comme étant privées.

Par exemple, imaginez que nous changeons notre méthode `Fight#_run_attack` pour qu'elle retourne une variable booléenne indiquant si le combat est terminé plutôt que de lever une exception. Nous saurons que le seul code que nous aurions pu casser est à l'intérieur de la classe `Fight`, car nous avons rendu la méthode privée.

Rappelez-vous, le code est plus fréquemment modifié que réécrit. Pouvoir changer votre code avec des répercussions aussi claires et minimes que possible est la flexibilité que vous voulez en tant que développeur.

#### Décomposition

La décomposition est l'action de diviser un objet en plusieurs parties séparées plus petites. Ces parties sont plus faciles à comprendre, maintenir et programmer.

Imaginez que nous voulions incorporer plus de fonctionnalités RPG comme des buffs, un inventaire, un équipement et des attributs de personnage en plus de notre `Hero` :

Je suppose que vous pouvez dire que ce code devient assez désordonné. Notre objet `Hero` fait trop de choses à la fois et ce code devient assez fragile en conséquence.

Par exemple, un point d'endurance vaut 5 points de santé. Si nous voulons jamais changer cela à l'avenir pour en faire 6 points de santé, nous devrions changer l'implémentation à plusieurs endroits.

La réponse est de décomposer l'objet `Hero` en plusieurs objets plus petits qui englobent chacun une partie de la fonctionnalité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*etyn_SN7_v4zqGDbeazJVA.png)
_Une architecture plus propre_

Maintenant, après avoir décomposé la fonctionnalité de notre objet Hero en objets `HeroAttributes`, `HeroInventory`, `HeroEquipment` et `HeroBuff`, l'ajout de fonctionnalités futures sera plus facile, plus encapsulé et mieux abstrait. Vous pouvez dire que notre code est beaucoup plus propre et plus clair sur ce qu'il fait.

Il existe trois types de relations de décomposition :

* **association** — Définit une relation lâche entre deux composants. Les deux composants ne dépendent pas l'un de l'autre mais peuvent travailler ensemble.

**Exemple :** `Hero` et un objet `Zone`.

* **agrégation** — Définit une relation faible "a-un" entre un tout et ses parties. Considérée comme faible, car les parties peuvent exister sans le tout.

**Exemple :** `HeroInventory` et `Item`.
Un `HeroInventory` peut avoir plusieurs `Items` et un `Item` peut appartenir à n'importe quel `HeroInventory` (comme échanger des objets).

* **composition** — Une relation forte "a-un" où le tout et la partie ne peuvent pas exister l'un sans l'autre. Les parties ne peuvent pas être partagées, car le tout dépend de ces parties exactes.

**Exemple :** `Hero` et `HeroAttributes`.
Ce sont les attributs du Hero — vous ne pouvez pas changer leur propriétaire.

#### Généralisation

La généralisation pourrait être le principe de conception le plus important — c'est le processus d'extraction des caractéristiques partagées et de leur combinaison en un seul endroit. Nous connaissons tous le concept de fonctions et d'héritage de classe — les deux sont une sorte de généralisation.

Une comparaison pourrait éclaircir les choses : tandis que l'**abstraction** réduit la complexité en cachant les détails inutiles, la **généralisation** réduit la complexité en remplaçant plusieurs entités qui effectuent des fonctions similaires par une seule construction.

Dans l'exemple donné, nous avons généralisé la fonctionnalité commune de nos classes `Hero` et `NPC` dans un ancêtre commun appelé `Entity`. Cela est toujours réalisé par l'héritage.

Ici, au lieu d'avoir nos classes `NPC` et `Hero` implémenter toutes les méthodes deux fois et violer le [principe DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), nous avons réduit la complexité en déplaçant leur fonctionnalité commune dans une classe de base.

En guise d'avertissement — ne faites pas trop d'[héritage](https://softwareengineering.stackexchange.com/questions/260343/why-is-inheritance-generally-viewed-as-a-bad-thing-by-oop-proponents). [De nombreuses personnes expérimentées](https://en.wikipedia.org/wiki/Design_Patterns#Introduction,_Chapter_1) recommandent de privilégier la [composition sur l'héritage](https://stackoverflow.com/a/53354).

L'héritage est souvent abusé par les programmeurs amateurs, probablement parce que c'est l'une des premières techniques POO qu'ils saisissent en raison de sa simplicité.

#### Composition

La composition est le principe de combiner plusieurs objets en un objet plus complexe. En pratique, cela signifie créer des instances d'objets et utiliser leur fonctionnalité au lieu de l'hériter directement.

Un objet qui utilise la composition peut être appelé un **objet composite**. Il est important que ce composite soit plus simple que la somme de ses pairs. En combinant plusieurs classes en une seule, nous voulons élever le niveau d'abstraction et rendre l'objet plus simple.

L'[API](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82) de l'objet composite doit masquer ses composants internes et les interactions entre eux. Pensez à une horloge mécanique, elle a trois aiguilles pour indiquer l'heure et un bouton pour le réglage — mais contient en interne des dizaines de pièces mobiles et interdépendantes.

Comme je l'ai dit, la composition est préférée à l'héritage, ce qui signifie que vous devriez vous efforcer de déplacer la fonctionnalité commune dans un objet séparé que les classes utilisent ensuite — plutôt que de l'entasser dans une classe de base que vous avez héritée.

Illustrons un problème possible avec l'héritage excessif de fonctionnalités :

Nous venons d'ajouter le mouvement à notre jeu.

Comme nous l'avons appris, au lieu de dupliquer le code, nous avons utilisé la généralisation pour mettre les fonctions `move_right` et `move_left` dans la classe `Entity`.

D'accord, maintenant, que faire si nous voulions introduire des montures dans le jeu ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*dK8x5H7sJF-3px7cbJ46Jw.jpeg)
_une bonne monture :)_

Les montures devraient également se déplacer à gauche et à droite mais n'ont pas la capacité d'attaquer. À y penser — elles n'ont peut-être même pas de santé !

Je sais quelle est votre solution :

Déplacer simplement la logique `move` dans une classe séparée `MoveableEntity` ou `MoveableObject` qui n'a que cette fonctionnalité. La classe `Mount` peut alors hériter de cela.

Ensuite, que faisons-nous si nous voulons des montures qui ont de la santé mais ne peuvent pas attaquer ? Plus de division en sous-classes ? J'espère que vous pouvez voir comment notre hiérarchie de classes commencerait à devenir complexe même si notre logique métier est encore assez simple.

Une approche quelque peu meilleure serait d'abstraire la logique de mouvement dans une classe `Movement` (ou un meilleur nom) et de l'instancier dans les classes qui pourraient en avoir besoin. Cela emballera bien la fonctionnalité et la rendra réutilisable dans tous types d'objets, pas seulement `Entity`.

Hourra, la composition !

#### Avertissement de Pensée Critique

Même si ces principes de conception ont été formés à travers des décennies d'expérience, il est encore extrêmement important que vous soyez capable de penser de manière critique avant d'appliquer aveuglément un principe à votre code.

Comme toutes choses, trop peut être mauvais. Parfois, les principes peuvent être poussés trop loin, vous pouvez être trop malin avec eux et finir avec quelque chose qui est en fait plus difficile à utiliser.

En tant qu'ingénieur, votre principale qualité est d'évaluer de manière critique la meilleure approche pour votre situation unique, et non de suivre et d'appliquer aveuglément des règles arbitraires.

### Cohésion, Couplage et Séparation des Préoccupations

#### Cohésion

La cohésion représente la clarté des responsabilités au sein d'un module ou, en d'autres termes, sa complexité.

Si votre classe effectue une tâche et rien d'autre, ou a un but clair — cette classe a une **forte cohésion**. En revanche, si elle est quelque peu floue dans ce qu'elle fait ou a plus d'un but — elle a une **faible cohésion**.

Vous voulez que vos classes aient une forte cohésion. Elles doivent avoir une seule responsabilité et si vous les prenez en train d'en avoir plus — il est peut-être temps de les diviser.

#### Couplage

Le couplage capture la complexité entre la connexion de différentes classes. Vous voulez que vos classes aient le moins et les connexions les plus simples possibles avec d'autres classes, afin de pouvoir les remplacer dans de futurs événements (comme changer de frameworks web). Le but est d'avoir un **couplage lâche**.

Dans de nombreux langages, cela est réalisé par une utilisation intensive des interfaces — elles abstraient la classe spécifique gérant la logique et représentent une sorte de couche d'adaptateur dans laquelle n'importe quelle classe peut se brancher.

#### Séparation des Préoccupations

La Séparation des Préoccupations (SoC) est l'idée qu'un système logiciel doit être divisé en parties qui ne se chevauchent pas en fonctionnalité. Ou comme le dit le nom — préoccupation — un terme général sur tout ce qui fournit une solution à un problème — doit être séparé en différents endroits.

Une page web est un bon exemple de cela — elle a ses trois couches (Information, Présentation et Comportement) séparées en trois endroits (HTML, CSS et [JavaScript respectivement](https://shinesolutions.com/2013/10/29/respect-the-javascript/)).

Si vous regardez à nouveau l'exemple du `Hero` RPG, vous verrez qu'il avait de nombreuses préoccupations au tout début (appliquer des buffs, calculer les dégâts d'attaque, gérer l'inventaire, équiper des objets, gérer les attributs). Nous avons séparé ces préoccupations par **décomposition** en classes plus **cohérentes** qui **abstraient** et **encapsulent** leurs détails. Notre classe `Hero` agit maintenant comme un objet [composite](https://en.wikipedia.org/wiki/Composite_pattern) et est beaucoup plus simple qu'avant.

### Retour sur Investissement

L'application de tels principes peut sembler excessivement compliquée pour un si petit morceau de code. La vérité est que c'est un **must** pour tout projet logiciel que vous prévoyez de développer et de maintenir à l'avenir. Écrire un tel code a un peu de surcharge au tout début mais se révèle multiple fois rentable à long terme.

Ces principes garantissent que notre système est plus :

* **Extensible** : La **forte cohésion** facilite la mise en œuvre de nouveaux modules sans se soucier des fonctionnalités sans rapport. Le **faible couplage** signifie qu'un nouveau module a moins de choses à connecter, donc il est plus facile à mettre en œuvre.
* **Maintenable** : Le **faible couplage** garantit qu'un changement dans un module n'affectera généralement pas les autres. La **forte cohésion** garantit qu'un changement dans les exigences du système nécessitera de modifier le moins de classes possible.
* **Réutilisable** : La **forte cohésion** garantit qu'une fonctionnalité de module est complète et bien définie. Le **faible couplage** rend le module moins dépendant du reste du système, le rendant plus facile à réutiliser dans d'autres logiciels.

### Résumé

Nous avons commencé par introduire quelques types d'objets de haut niveau de base (Entité, Frontière et Contrôle).

Nous avons ensuite appris les principes clés de la structuration de ces objets (Abstraction, Généralisation, Composition, Décomposition et Encapsulation).

Pour suivre, nous avons introduit deux métriques de qualité logicielle (Couplage et Cohésion) et appris les avantages de l'application de ces principes.

J'espère que cet article a fourni un aperçu utile de certains principes de conception. Si vous souhaitez approfondir vos connaissances dans ce domaine, voici quelques ressources que je recommande.

#### Lectures Complémentaires

[Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8) — Arguablement le livre le plus influent dans le domaine. Un peu daté dans ses exemples _(C++ 98)_ mais les motifs et idées restent très pertinents.

[Growing Object-Oriented Software Guided by Tests](http://www.growing-object-oriented-software.com/) — Un excellent livre qui montre comment appliquer pratiquement les principes décrits dans cet article (et plus) en travaillant sur un projet.

[Effective Software Design](https://effectivesoftwaredesign.com/category/oop/) — Un blog de premier ordre contenant bien plus que des insights sur la conception.

[Software Design and Architecture Specialization](https://www.coursera.org/specializations/software-design-architecture) — Une excellente série de 4 cours vidéo qui vous enseignent une conception efficace tout au long de son application sur un projet qui s'étend sur les quatre cours.

Si cet aperçu vous a été informatif, veuillez envisager de lui donner le nombre d'applaudissements que vous pensez qu'il mérite afin que plus de personnes puissent le découvrir et en tirer de la valeur.