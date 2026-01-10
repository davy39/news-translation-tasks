---
title: J'ai écrit un langage de programmation. Voici comment vous pouvez faire de
  même.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-31T03:20:01.000Z'
originalURL: https://freecodecamp.org/news/the-programming-language-pipeline-91d3f449c919
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vzwAxAI6RB89kPZZJIGkOA.png
tags:
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: J'ai écrit un langage de programmation. Voici comment vous pouvez faire
  de même.
seo_desc: 'By William W Wold

  Over the past 6 months, I’ve been working on a programming language called Pinecone.
  I wouldn’t call it mature yet, but it already has enough features working to be
  usable, such as:


  variables

  functions

  user defined structures


  If y...'
---

Par William W Wold

Au cours des 6 derniers mois, j'ai travaillé sur un langage de programmation appelé Pinecone. Je ne le qualifierais pas encore de mature, mais il possède déjà suffisamment de fonctionnalités pour être utilisable, telles que :

* les variables
* les fonctions
* les structures définies par l'utilisateur

Si cela vous intéresse, consultez la [page d'accueil](https://pinecone-lang.herokuapp.com/index.html) de Pinecone ou son [dépôt GitHub](https://github.com/william01110111/Pinecone).

Je ne suis pas un expert. Lorsque j'ai commencé ce projet, je n'avais aucune idée de ce que je faisais, et je ne sais toujours pas. Je n'ai suivi aucun cours sur la création de langages, j'ai lu seulement un peu à ce sujet en ligne, et je n'ai pas suivi beaucoup des conseils qui m'ont été donnés.

Et pourtant, j'ai quand même créé un langage complètement nouveau. Et il fonctionne. Donc, je dois faire quelque chose de bien.

Dans cet article, je vais plonger sous le capot et vous montrer le pipeline que Pinecone (et d'autres langages de programmation) utilise pour transformer le code source en magie.

Je vais également aborder certains des compromis que j'ai dû faire, et pourquoi j'ai pris les décisions que j'ai prises.

Ce n'est en aucun cas un tutoriel complet sur l'écriture d'un langage de programmation, mais c'est un bon point de départ si vous êtes curieux concernant le développement de langages.

### Mise en route

« Je n'ai absolument aucune idée de par où commencer » est quelque chose que j'entends souvent lorsque je dis à d'autres développeurs que j'écris un langage. Au cas où ce serait votre réaction, je vais maintenant passer en revue certaines décisions initiales qui sont prises et les étapes qui sont suivies lors du démarrage d'un nouveau langage.

#### Compilé vs Interprété

Il existe deux grands types de langages : compilés et interprétés :

* Un compilateur détermine tout ce qu'un programme va faire, le transforme en « code machine » (un format que l'ordinateur peut exécuter très rapidement), puis sauvegarde cela pour être exécuté plus tard.
* Un interpréteur parcourt le code source ligne par ligne, déterminant ce qu'il fait au fur et à mesure.

Techniquement, tout langage pourrait être compilé ou interprété, mais l'un ou l'autre a généralement plus de sens pour un langage spécifique. En général, l'interprétation tend à être plus flexible, tandis que la compilation tend à avoir des performances plus élevées. Mais ce n'est qu'effleurer la surface d'un sujet très complexe.

Je valorise grandement les performances, et j'ai constaté un manque de langages de programmation à la fois haute performance et orientés simplicité, donc j'ai opté pour la compilation pour Pinecone.

C'était une décision importante à prendre tôt, car de nombreuses décisions de conception de langage en sont affectées (par exemple, le typage statique est un grand avantage pour les langages compilés, mais pas autant pour les langages interprétés).

Malgré le fait que Pinecone ait été conçu en pensant à la compilation, il dispose d'un interpréteur entièrement fonctionnel qui était la seule façon de l'exécuter pendant un certain temps. Il y a plusieurs raisons à cela, que j'expliquerai plus tard.

#### Choix d'un langage

Je sais que c'est un peu méta, mais un langage de programmation est lui-même un programme, et donc vous devez l'écrire dans un langage. J'ai choisi C++ en raison de ses performances et de son large ensemble de fonctionnalités. De plus, j'aime vraiment travailler en C++.

Si vous écrivez un langage interprété, il est logique de l'écrire dans un langage compilé (comme C, C++ ou Swift) car les pertes de performance dans le langage de votre interpréteur et l'interpréteur qui interprète votre interpréteur se cumuleront.

Si vous prévoyez de compiler, un langage plus lent (comme Python ou JavaScript) est plus acceptable. Le temps de compilation peut être mauvais, mais à mon avis, ce n'est pas près d'être aussi grave qu'un mauvais temps d'exécution.

#### Conception de haut niveau

Un langage de programmation est généralement structuré comme un pipeline. C'est-à-dire qu'il comporte plusieurs étapes. Chaque étape a des données formatées d'une manière spécifique et bien définie. Il dispose également de fonctions pour transformer les données de chaque étape à la suivante.

La première étape est une chaîne contenant le fichier source d'entrée entier. La dernière étape est quelque chose qui peut être exécuté. Tout cela deviendra clair lorsque nous passerons en revue le pipeline de Pinecone étape par étape.

### Lexing

![Image](https://cdn-media-1.freecodecamp.org/images/qade0oMhjMIBsiv29aYB3YpAF-7MmO0mDndO)

La première étape de la plupart des langages de programmation est le lexing, ou tokenizing. 'Lex' est l'abréviation de lexical analysis, un terme très sophistiqué pour diviser un ensemble de texte en tokens. Le mot 'tokenizer' a beaucoup plus de sens, mais 'lexer' est tellement amusant à dire que je l'utilise quand même.

#### Tokens

Un token est une petite unité d'un langage. Un token peut être un nom de variable ou de fonction (également appelé identifiant), un opérateur ou un nombre.

#### Tâche du Lexer

Le lexer est censé prendre une chaîne contenant une quantité de code source d'un fichier entier et produire une liste contenant chaque token.

Les étapes futures du pipeline ne feront pas référence au code source original, donc le lexer doit produire toutes les informations nécessaires. La raison de ce format de pipeline relativement strict est que le lexer peut effectuer des tâches telles que la suppression de commentaires ou la détection si quelque chose est un nombre ou un identifiant. Vous voulez garder cette logique verrouillée à l'intérieur du lexer, à la fois pour ne pas avoir à penser à ces règles lors de l'écriture du reste du langage, et pour pouvoir changer ce type de syntaxe en un seul endroit.

#### Flex

Le jour où j'ai commencé le langage, la première chose que j'ai écrite était un lexer simple. Peu après, j'ai commencé à apprendre des outils qui rendraient supposément le lexing plus simple et moins bogué.

L'outil principal de ce type est Flex, un programme qui génère des lexers. Vous lui donnez un fichier qui a une syntaxe spéciale pour décrire la grammaire du langage. À partir de cela, il génère un programme C qui lexe une chaîne et produit la sortie souhaitée.

#### Ma Décision

J'ai choisi de garder le lexer que j'ai écrit pour le moment. En fin de compte, je n'ai pas vu d'avantages significatifs à utiliser Flex, du moins pas assez pour justifier l'ajout d'une dépendance et la complication du processus de construction.

Mon lexer ne fait que quelques centaines de lignes de long et me donne rarement des ennuis. Écrire mon propre lexer me donne également plus de flexibilité, comme la possibilité d'ajouter un opérateur au langage sans éditer plusieurs fichiers.

### Parsing

![Image](https://cdn-media-1.freecodecamp.org/images/NpNL7zAZTaWvCFEx9iVecnx0wyalOFW5TTkO)

La deuxième étape du pipeline est le parser. Le parser transforme une liste de tokens en un arbre de nœuds. Un arbre utilisé pour stocker ce type de données est connu sous le nom d'Arbre de Syntaxe Abstraite, ou AST. Au moins dans Pinecone, l'AST ne contient aucune information sur les types ou sur les identifiants. Il s'agit simplement de tokens structurés.

#### Devoirs du Parser

Le parser ajoute de la structure à la liste ordonnée de tokens que le lexer produit. Pour éviter les ambiguïtés, le parser doit prendre en compte les parenthèses et l'ordre des opérations. Le simple parsing des opérateurs n'est pas terriblement difficile, mais à mesure que davantage de constructions de langage sont ajoutées, le parsing peut devenir très complexe.

#### Bison

À nouveau, il y avait une décision à prendre concernant une bibliothèque tierce. La bibliothèque de parsing prédominante est Bison. Bison fonctionne beaucoup comme Flex. Vous écrivez un fichier dans un format personnalisé qui stocke les informations de grammaire, puis Bison utilise cela pour générer un programme C qui effectuera votre parsing. Je n'ai pas choisi d'utiliser Bison.

#### Pourquoi le Personnalisé est Mieux

Avec le lexer, la décision d'utiliser mon propre code était assez évidente. Un lexer est un programme si trivial que ne pas écrire le mien me semblait presque aussi ridicule que de ne pas écrire mon propre 'left-pad'.

Avec le parser, c'est une autre affaire. Mon parser Pinecone fait actuellement 750 lignes de long, et j'en ai écrit trois parce que les deux premiers étaient nuls.

J'ai initialement pris ma décision pour un certain nombre de raisons, et bien que cela ne se soit pas passé complètement sans heurts, la plupart d'entre elles restent valables. Les principales sont les suivantes :

* Minimiser le changement de contexte dans le flux de travail : le changement de contexte entre C++ et Pinecone est déjà assez mauvais sans ajouter la grammaire de Bison.
* Garder la construction simple : chaque fois que la grammaire change, Bison doit être exécuté avant la construction. Cela peut être automatisé, mais cela devient un casse-tête lors du passage entre les systèmes de construction.
* J'aime construire des trucs cool : Je n'ai pas fait Pinecone parce que je pensais que ce serait facile, alors pourquoi déléguer un rôle central alors que je pourrais le faire moi-même ? Un parser personnalisé peut ne pas être trivial, mais il est complètement réalisable.

Au début, je n'étais pas complètement sûr de suivre une voie viable, mais j'ai été rassuré par ce que Walter Bright (un développeur sur une version précoce de C++, et le créateur du langage D) [avait à dire sur le sujet](http://www.drdobbs.com/architecture-and-design/so-you-want-to-write-your-own-language/240165488) :

> « Un peu plus controversé, je ne perdrais pas de temps avec les générateurs de lexer ou de parser et autres soi-disant « compilateurs de compilateurs ». Ils sont une perte de temps. L'écriture d'un lexer et d'un parser est un petit pourcentage du travail d'écriture d'un compilateur. L'utilisation d'un générateur prendra environ autant de temps que d'en écrire un à la main, et cela vous mariera au générateur (ce qui compte lors du portage du compilateur vers une nouvelle plateforme). Et les générateurs ont également la réputation malheureuse d'émettre des messages d'erreur médiocres. »

### Arbre d'Action

![Image](https://cdn-media-1.freecodecamp.org/images/oEWwpUKAUetQYx8BsfDSkMjCVQ9-khJFZ9s4)

Nous avons maintenant quitté le domaine des termes communs et universels, ou du moins je ne connais plus les termes. D'après ma compréhension, ce que j'appelle l'« arbre d'action » est le plus proche de l'IR (représentation intermédiaire) de LLVM.

Il existe une différence subtile mais très significative entre l'arbre d'action et l'arbre de syntaxe abstraite. Il m'a fallu un certain temps pour comprendre qu'il devait même y avoir une différence entre eux (ce qui a contribué à la nécessité de réécrire le parser).

#### Arbre d'Action vs AST

En termes simples, l'arbre d'action est l'AST avec du contexte. Ce contexte est des informations telles que le type qu'une fonction retourne, ou que deux endroits où une variable est utilisée utilisent en fait la même variable. Parce qu'il doit déterminer et se souvenir de tout ce contexte, le code qui génère l'arbre d'action a besoin de nombreuses tables de recherche de namespace et autres trucs.

#### Exécution de l'Arbre d'Action

Une fois que nous avons l'arbre d'action, exécuter le code est facile. Chaque nœud d'action a une fonction 'execute' qui prend une entrée, fait ce que l'action doit faire (y compris éventuellement appeler une sous-action) et retourne la sortie de l'action. C'est l'interpréteur en action.

### Options de Compilation

« Mais attendez ! » je vous entends dire, « Pinecone n'est-il pas censé être compilé ? » Si, c'est le cas. Mais compiler est plus difficile que d'interpréter. Il y a quelques approches possibles.

#### Construire Mon Propre Compilateur

Cela m'a semblé être une bonne idée au début. J'aime faire les choses moi-même, et j'ai eu envie d'une excuse pour devenir bon en assembleur.

Malheureusement, écrire un compilateur portable n'est pas aussi facile que d'écrire du code machine pour chaque élément de langage. En raison du nombre d'architectures et de systèmes d'exploitation, il est peu pratique pour un individu d'écrire un backend de compilateur multiplateforme.

Même les équipes derrière Swift, Rust et Clang ne veulent pas s'en occuper toutes seules, donc au lieu de cela, elles utilisent toutes...

#### LLVM

LLVM est une collection d'outils de compilation. C'est essentiellement une bibliothèque qui transformera votre langage en un binaire exécutable compilé. Cela semblait être le choix parfait, alors je me suis lancé directement. Malheureusement, je n'ai pas vérifié la profondeur de l'eau et je me suis immédiatement noyé.

LLVM, bien que pas aussi difficile que le langage d'assemblage, est une bibliothèque complexe et gigantesque. Ce n'est pas impossible à utiliser, et ils ont de bons tutoriels, mais j'ai réalisé que je devrais m'entraîner avant d'être prêt à implémenter complètement un compilateur Pinecone avec.

#### Transpilation

Je voulais une sorte de Pinecone compilé et je le voulais rapidement, alors je me suis tourné vers une méthode que je savais pouvoir faire fonctionner : la transpilation.

J'ai écrit un transpileur Pinecone vers C++, et j'ai ajouté la capacité de compiler automatiquement le code source de sortie avec GCC. Cela fonctionne actuellement pour presque tous les programmes Pinecone (bien qu'il y ait quelques cas particuliers qui le cassent). Ce n'est pas une solution particulièrement portable ou évolutive, mais cela fonctionne pour le moment.

#### Futur

En supposant que je continue à développer Pinecone, il obtiendra le support de compilation LLVM tôt ou tard. Je soupçonne que, peu importe le temps que j'y consacre, le transpileur ne sera jamais complètement stable et les avantages de LLVM sont nombreux. Il s'agit simplement de savoir quand j'aurai le temps de faire quelques projets d'exemple dans LLVM et de m'y habituer.

En attendant, l'interpréteur est idéal pour les programmes triviaux et la transpilation C++ fonctionne pour la plupart des choses qui nécessitent plus de performance.

### Conclusion

J'espère avoir rendu les langages de programmation un peu moins mystérieux pour vous. Si vous souhaitez en créer un vous-même, je vous le recommande vivement. Il y a une tonne de détails d'implémentation à résoudre, mais le schéma ici devrait être suffisant pour vous lancer.

Voici mes conseils de haut niveau pour commencer (rappelez-vous, je ne sais pas vraiment ce que je fais, alors prenez-les avec des pincettes) :

* En cas de doute, optez pour l'interprété. Les langages interprétés sont généralement plus faciles à concevoir, à construire et à apprendre. Je ne vous décourage pas d'écrire un langage compilé si vous savez que c'est ce que vous voulez faire, mais si vous hésitez, je choisirais l'interprété.
* En ce qui concerne les lexers et les parsers, faites ce que vous voulez. Il y a des arguments valables pour et contre l'écriture des vôtres. En fin de compte, si vous réfléchissez à votre conception et implémentez tout de manière sensée, cela n'a pas vraiment d'importance.
* Apprenez du pipeline que j'ai fini par avoir. Beaucoup d'essais et d'erreurs ont été nécessaires pour concevoir le pipeline que j'ai maintenant. J'ai tenté d'éliminer les AST, les AST qui se transforment en arbres d'actions en place, et d'autres idées terribles. Ce pipeline fonctionne, alors ne le changez pas à moins d'avoir une très bonne idée.
* Si vous n'avez pas le temps ou la motivation pour implémenter un langage généraliste complexe, essayez d'implémenter un langage ésotérique tel que [Brainfuck](https://esolangs.org/wiki/Brainfuck). Ces interpréteurs peuvent être aussi courts que quelques centaines de lignes.

J'ai très peu de regrets en ce qui concerne le développement de Pinecone. J'ai fait un certain nombre de mauvais choix en cours de route, mais j'ai réécrit la plupart du code affecté par de telles erreurs.

Actuellement, Pinecone est dans un état suffisamment bon pour fonctionner correctement et pouvoir être facilement amélioré. Écrire Pinecone a été une expérience extrêmement éducative et agréable pour moi, et ce n'est qu'un début.