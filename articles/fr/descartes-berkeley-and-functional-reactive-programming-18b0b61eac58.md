---
title: Descartes, Berkeley et la Programmation Réactive Fonctionnelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-07T13:46:42.000Z'
originalURL: https://freecodecamp.org/news/descartes-berkeley-and-functional-reactive-programming-18b0b61eac58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eZcgzUUKk-PnETNqIXMfcw.png
tags:
- name: Computer Science
  slug: computer-science
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Philosophy
  slug: philosophy
- name: Reactive Programming
  slug: reactive-programming
seo_title: Descartes, Berkeley et la Programmation Réactive Fonctionnelle
seo_desc: 'By David Valdman

  Functional reactive programming is laden with unfamiliar terminology to the newcomer:
  pure functions, immutability, monads, etc. But beneath these concepts is a deeper
  principle — one debated long before Charles Babbage and the first...'
---

Par David Valdman

La programmation réactive fonctionnelle est chargée de terminologie peu familière pour le néophyte : fonctions pures, immutabilité, monades, etc. Mais sous ces concepts se cache un principe plus profond — un principe débattu bien avant Charles Babbage et les premiers ordinateurs. Je soutiens que la différence entre la programmation orientée objet (POO) et la programmation réactive fonctionnelle (PRF) est autant une question d'interprétations de la réalité qu'une question de structures de programmes.

Voici une expérience de pensée que nous avons tous probablement entendue :

> Si un arbre tombe au milieu d'une forêt, et que personne n'est là pour l'entendre, fait-il un son ?

Il existe de nombreuses façons d'attaquer cette question comme mal posée. En les ignorant pour l'instant, cette question aborde un aspect fondamental de la réalité : la causalité. L'existence est-elle dépendante de, ou indépendante de, l'observation ? Traduisons cette expérience de pensée en code. Voici un **_arbre_** :

```
class Tree {     constructor(){         this._fell = false;     }     set fell(state){         this._fell = state;     }     get fell(){         return this._fell;     }} 
```

```
var tree = new Tree();tree.fell = true;
```

Pour faire tomber l'**_arbre_**, nous définissons son état de chute à **_true_**. C'est de la programmation orientée objet classique. Ses motifs sont les getters, les setters et l'état. Assez simple, mais dans le contexte de notre expérience de pensée, il y a une interprétation qui se cache : si l'on se demande si l'arbre est tombé, même si personne ne l'a observé, la réponse est un "_Oui !_" retentissant. Il suffit de vérifier que **_tree.fell_** est **true**. Ceux qui répondent _oui_ à notre question philosophique le font parce qu'ils peuvent retourner dans la forêt, voir l'arbre tombé et déduire qu'il est tombé dans le passé. Voici l'équivalent codifié. On dirait que nous avons résolu cette vieille énigme centenaire.

Pas si vite ! Regardons une approche différente. Voici un autre **_arbre_** :

```
class Tree extends EventEmitter {}var tree = new Tree();tree.emit('fall');
```

C'est l'**_arbre_** "réactif". Ses motifs sont les événements et les transformations. Dans sa forme la plus pure, notre arbre ne maintient aucun état. Nous le faisons tomber en diffusant un événement **_fall_**. Hélas, le message tombe dans l'oreille d'un sourd ! Aucun état n'a changé, aucune preuve n'est laissée. Il n'y a aucun moyen de déduire le passé en interrogeant la réalité. L'arbre est-il tombé ? *_haussement d'épaules_*

### Descartes et Berkeley

Les approches orientées objet et réactives donnent deux réponses différentes à notre expérience de pensée parce qu'elles incarnent deux philosophies contradictoires de l'épistémologie : le Rationalisme, popularisé par Descartes à la fin des années 1600, et l'Empirisme popularisé par Berkeley au début des années 1700.

![Image](https://cdn-media-1.freecodecamp.org/images/1w0HHnALKtOg8UIL9dyDfrziVVwwfTj7f2eh)
_Descartes prend une courte pause pour écrire une interface Java_

Descartes, dans un élan de scepticisme fanatique, a découvert qu'il ne pouvait être sûr que d'une seule chose : sa propre existence. Il est parvenu à cette conclusion parce qu'il ne pouvait douter de l'existence de ses pensées et a conclu qu'il devait y avoir une entité qui pense, inventant ainsi la phrase, _cogito ergo sum_ : Je pense donc je suis. En d'autres termes : en reconnaissant qu'il y a un état interne qui change, il doit y avoir un agent auquel l'état appartient. Pour Descartes, les changements d'état sont la preuve de l'existence — tout comme notre premier **_arbre._**

![Image](https://cdn-media-1.freecodecamp.org/images/9jQ6H6ZLd-xgha0AWrT7PfFvfickuVBakznO)
_Berkeley vu en train de réfléchir aux définitions de types Haskell_

Peu après Descartes vient George Berkeley. Berkeley a dénoncé la vision réaliste. Pour Berkeley, il n'avait aucun sens que les objets matériels, comme les arbres, aient une existence. L'existence ne nous vient que par les pensées (expérience mentale par opposition à l'expérience physique), et les pensées doivent être assimilées dans l'esprit pour exister. Les objets matériels sont des illusions ; leur essence n'est pas leur physicalité mais leur capacité à transformer l'immatériel. Si une pensée n'est pas assimilée dans l'esprit, elle n'a pas d'existence. Ainsi, il a popularisé la phrase latine _esse percepi_ : être, c'est être perçu.

Traduisons la réalité de Berkeley en code. Pour que notre deuxième **_arbre_** fasse un son, un esprit doit l'interpréter. Nous allons créer une chaîne de causalité, commençant par la chute de l'arbre, en passant par la vibration de l'air, la création d'un stimulus électrique par l'oreille, jusqu'à l'interprétation de ce stimulus par le cerveau comme un son.

![Image](https://cdn-media-1.freecodecamp.org/images/XlaPm5rC3NWvz16x-OUYLTNSJF40VjosKvlC)

Lorsque l'arbre tombe, l'air vibre.

```
class Air extends EventEmitter {    constructor (){        super();                function mapFall (fall){...}        this.on('fall', (fall) => {            var vibration = mapFall(fall);            this.emit('vibrate', vibration);        };    }}
```

Lorsque l'air vibre, l'oreille le convertit en un stimulus électrique.

```
class Ear extends EventEmitter {    constructor (){         super();                function mapFrequency (frequency){...}        this.on('vibrate', (frequency) => {            var stimulus = mapFrequency(frequency);            this.emit('stimulus', stimulus);        };    }}
```

Lorsque l'oreille crée un stimulus, le cerveau l'interprète comme un son.

```
class Brain extends EventEmitter {    constructor (){        super();        function mapStimulus (signal){...}        this.on('stimulus', (signal) => {            var sound = mapStimulus(signal);            this.emit('sound', sound);        };    }}
```

Nous avons effectivement établi une chaîne de causalité, que nous rendons explicite en construisant un pipeline :

```
tree.pipe(air).pipe(ear).pipe(brain);
```

Maintenant, lorsque l'arbre tombe, il fait une impression sur un esprit :

```
brain.on('sound', (sound) => {    // Nous quittons le système. Vous avez été entendu !    console.log(sound); });
```

```
tree.emit('fall', fallData);
```

Berkeley a appelé ce concept _Idéalisme Subjectif_. _Idéalisme_ parce qu'il affirme que seules les pensées ou les idées existent, et _subjectif_ parce que la réalité dépend des sujets qui la perçoivent. À mon avis, l'Idéalisme Subjectif est la philosophie sous-jacente à la programmation réactive. Berkeley écrit,

> Il est en effet une opinion étrangement répandue parmi les hommes, que les maisons, les montagnes, les rivières, et en un mot tous les objets sensibles ont une existence naturelle ou réelle, distincte de leur perception par l'entendement. ...Car que sont les objets mentionnés ci-dessus, sinon les choses que nous percevons par les sens...et n'est-il pas clairement contradictoire que l'un de ces objets ou toute combinaison de ceux-ci puisse exister sans être perçu ?

J'aime cette citation pour son audace assurée. Berkeley nous traite essentiellement de fous pour penser que les maisons, les montagnes et les rivières existent. Dans notre exemple, les arbres, l'air, les oreilles et les cerveaux sont de faux idoles ; la seule réalité est **_mapFall_**, **_mapFrequency_** et **_mapStimulus_**. La réalité n'est alors jamais consommée, comme c'est le cas avec les objets lorsqu'ils retiennent l'état. La réalité est simplement transformée.

### _Idéalisme Subjectif_ en Pratique

En POO, nous créons des objets qui encapsulent un certain type de comportement. Nous construisons ensuite des programmes qui sont des relations en réseau de ces objets. Notre programme est structurellement un _graphe_.

En PRF, nous créons des pipelines de fonctions qui encapsulent des relations causales. Les pipelines sont ensuite fusionnés et ramifiés pour donner la structure en forme de graphe d'un programme orienté objet. Cependant, il y a une limitation importante sur les types de fonctions. Seules les [fonctions pures](https://en.wikipedia.org/wiki/Pure_function) sont autorisées. C'est-à-dire, des fonctions qui ne peuvent affecter rien en dehors d'elles-mêmes. Dans notre exemple, l'objet **Ear** ne peut pas changer la façon dont l'objet **Air** a vibré. Cette contrainte garantit que nos pipelines ont une direction bien définie de la cause à l'effet. En termes de structure, cela signifie que notre programme est un [_graphe acyclique dirigé_](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG).

Pour raisonner sur le logiciel, nous devons le considérer comme une séquence de relations causales. Nous devons être capables d'_ordonner_ le programme. Mathématiquement, un graphe peut être [ordonné](https://en.wikipedia.org/wiki/Topological_sorting) si et seulement s'il est un DAG. Cela est vrai peu importe comment vous écrivez votre programme. Que vous choisissiez la POO, la PRF ou XYZ. Ce qui est spécial avec la PRF, cependant, c'est que l'ordonnancement est imposé par le motif.

En POO, l'ordonnancement est laissé non spécifié. Les objets peuvent appeler des méthodes sur d'autres objets. Les objets peuvent changer l'état d'autres objets. Tout a des privilèges de lecture et d'écriture par défaut. Spécifier un ordre est fait manuellement par le développeur. C'est à lui de relier l'ordonnancement séquentiel des lignes dans un programme à un ordonnancement des relations causales des objets.

Malheureusement, il est trop facile de tout gâcher. Remarquez qu'en POO, lorsque deux objets écrivent dans le même état partagé, vous avez une condition de course. En PRF, lorsque deux fonctions essaient de s'affecter mutuellement, vous avez une boucle infinie. Ce n'est qu'un exemple d'un motif théorique imposant un résultat pratique.

En résumé, il ne suffit pas d'encapsuler l'état. Un programme bien écrit encapsulera également la dépendance.

### **Compromis**

> "Les programmeurs connaissent les avantages de tout et les compromis de rien." — Rich Hickey

Vous penseriez qu'après toutes ces louanges de la PRF et ces critiques de la POO, je serais fermement dans le camp de la PRF. Vous auriez tort ! La PRF est un motif de programmation, et les motifs servent à contraindre les solutions. Si la solution idéale ne satisfait pas les contraintes, vous gaspillerez de l'énergie à lutter contre le motif.

Pour être concret, il y a quelques simples désagréments de la PRF. Prenons l'immuabilité — vous créez toujours plus de mémoire. Vous ne pouvez jamais, par exemple, trier une liste sur place. Vous créerez toujours une nouvelle liste. En théorie, l'immuabilité est un bon motif à observer. En pratique, vous pouvez être limité par la mémoire, et il peut être judicieux de nager à contre-courant de la PRF.

Mais ce n'est pas _le_ problème flagrant. Le problème flagrant est que la PRF devient un anti-motif lorsque vous ne savez pas quand deux parties d'une base de code interagiront. Prenons, par exemple, un jeu de tir à la première personne. Quelque part, il y a un objet **bullet**, et ailleurs un objet **player**. Une balle peut toucher un joueur, mais il n'est pas clair quand cela se produira. Ces objets doivent retenir l'état (vitesse de la balle, santé du joueur, etc.) afin qu'il soit disponible au moment où ils interagissent. Peut-être que dans l'abstrait, tout le jeu peut être considéré comme un pipeline causal unique, mais cela me semble plus intimidant que de penser en termes d'objets découplés et d'état.

Pour remettre mon chapeau philosophique une fois de plus, la physique peut décréter que la réalité est un pipeline causal unique dont l'évolution temporelle est régie par des lois physiques déterministes, et dont les conditions initiales (ou probabilités) sont fournies par le big bang. Mais ce n'est guère ainsi que les humains raisonnent sur la cause et l'effet. Nous découpons naturellement la réalité en objets de plus haut niveau et raisonnons sur leurs inter-relations. Cela peut être plus simple, même si c'est sujet à des erreurs !

Je pense que c'est pourquoi la PRF n'a pas été entièrement adoptée par la communauté des programmeurs, même après avoir vu ses nombreux avantages. Le mieux que nous puissions espérer en écrivant des programmes est d'utiliser les principes de la PRF là où ses motifs correspondent à la solution, et de les laisser inspirer les motifs de la POO là où ses motifs ne correspondent pas. Pour moi, cela distingue les solutions qui peuvent être considérées comme des pipelines, et celles qui ne devraient pas l'être.

### Conclusion

En philosophie, l'objectif n'est pas de résoudre nos problèmes les plus profonds, mais d'avoir un langage partagé et un précédent historique pour les débattre. Ainsi, lorsqu'un nouveau problème émerge, nous n'avons pas à recommencer. Il en va de même pour les motifs de programmation. Ils ne sont pas utilisés pour décider du bien et du mal, comme si ces concepts avaient un attrait universel. Ils sont utilisés pour classer les problèmes et leurs approches.

Nous devrions également nous tourner vers d'autres disciplines, bien plus anciennes que l'informatique, pour voir si leur langage partagé et leur précédent historique peuvent inspirer les nôtres. Alors nous pourrons voir que la question, "_l'arbre est-il tombé ?_" n'est pas répondue par un _oui_ ou un _non_. Qu'au contraire, elle questionne une perspective. Une perspective qui peut encadrer notre philosophie de l'épistémologie ou notre architecture de programmes. Et une perspective à laquelle la réponse se situe entre un état d'esprit et un flux de pensée !

**Aperçu de la Partie II**

Il reste encore un dilemme tenace dans notre expérience de pensée. Même s'il n'y a personne pour entendre le son, sûrement lorsque l'arbre tombe, l'air doit vibrer ! N'est-ce pas ? Dans la Partie II, nous irons plus loin dans le terrier du lapin pour voir que la PRF peut également donner une interprétation surprenante ici. Nous penserons aux flux de données en termes de push vs pull et verrons comment cela apparaît dans des concepts comme l'évaluation paresseuse, des algorithmes comme le lancer de rayons, et des applications comme Excel.