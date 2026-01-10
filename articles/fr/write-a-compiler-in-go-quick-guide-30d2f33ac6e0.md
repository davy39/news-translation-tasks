---
title: 'Comment écrire un compilateur en Go : un guide rapide'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T14:54:04.000Z'
originalURL: https://freecodecamp.org/news/write-a-compiler-in-go-quick-guide-30d2f33ac6e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xwPzWlZJoBbgrtEvwslRdg.jpeg
tags:
- name: compilers
  slug: compilers
- name: golang
  slug: golang
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Comment écrire un compilateur en Go : un guide rapide'
seo_desc: 'By Joseph Livni

  Compilers are awesome! ? ? ? They combine theory and application and touch on a
  lot of software related topics such as parsing and language construction. At their
  core, compilers are a program that make a program readable by the compu...'
---

Par Joseph Livni

Les compilateurs sont géniaux ! 💡 ✨ Ils combinent théorie et application et touchent à de nombreux sujets liés au logiciel tels que l'analyse syntaxique et la construction de langages. Au cœur, les compilateurs sont un programme qui rend un programme lisible par l'ordinateur.

L'inspiration pour cela est venue d'un cours sur les compilateurs que j'ai suivi cet automne passé et de mon amour pour Go.

Ceci est le guide que j'aurais aimé avoir en commençant mon voyage dans les compilateurs. Il existe de nombreux livres, vidéos et tutoriels sur la création de compilateurs. Le but de cet article est de trouver un équilibre entre fournir un exemple non trivial de certaines des choses qu'un compilateur peut faire tout en évitant de se perdre dans les détails. 🌱

Le résultat sera un compilateur capable d'exécuter un petit langage inventé. Pour consulter et exécuter le projet final, voir les instructions ci-dessous. 🚀

**Note :** N'oubliez pas que Go est strict concernant les chemins absolus lors de l'exécution de ceci

```
cd $GOPATH/src/github.com/Lebonescogit clone https://github.com/Lebonesco/go-compiler.gitcd go-compilergo test -vgo run main.go ./examples/math.bx
```

#### Aperçu du compilateur

* **Lexer/Parser**
* **Générateur AST**
* **Vérificateur de types**
* **Génération de code**

#### Le langage

Le but de cet article est de vous familiariser avec les compilateurs le plus rapidement possible, donc nous garderons le langage simple. Pour les **types**, nous travaillerons avec des `strings`, des `integers` et des `bools`. Il aura des **instructions** qui incluent `func`, `if`, `else`, `let` et `return`. Cela devrait suffire pour s'amuser avec certaines des complexités d'un compilateur.

Le premier compilateur que j'ai construit, je l'ai terminé sur une période de deux mois et a pris **1000's de lignes** de code. J'ai pris quelques raccourcis dans cet article afin de vous montrer les fondamentaux clés.

Deux composants courants que notre langage ne possède pas sont les `classes` et les `arrays`. Ceux-ci ajoutent des complications supplémentaires que nous n'avons pas le temps d'aborder maintenant. Si les gens veulent vraiment savoir comment gérer ces éléments, j'écrirai une suite.

Quelques exemples de code :

```
func add(a Int, b int) Int {    return a + b;}
```

```
func hello(name String) String {    return "hello:" + " " + name;}
```

```
let num = add(1, 2);let phrase = string hello("Jeff");let i = int 0;let result = "";
```

```
if (i == 2) {    result = hello("cat");} else {    result = hello("dog");}
```

```
PRINT(result);
```

#### Installation rapide

Le seul package externe dont nous avons besoin est `**gocc**`, qui aidera à construire le lexer et le parser.

Pour l'obtenir, exécutez :

```
go get github.com/goccmack/gocc
```

Assurez-vous que le dossier bin où se trouve gocc est dans votre `**PATH**` :

```
export PATH=$GOPATH/bin:$PATH
```

**Note :** Si vous avez des problèmes à ce stade, essayez d'exécuter `go env` pour vous assurer que votre `$GOROOT` et `$GOPATH` sont correctement assignés.

Super, plongeons dans du code.

#### Construction du Lexer

Le travail du lexer est de lire le programme et de produire un flux de tokens qui sont consommés par le parser. Chaque `Token` contient le `type` que le token représente dans le langage et le `Literal` string de ce token.

Pour identifier les morceaux du programme, nous utiliserons des expressions régulières. gocc convertira ensuite ces expressions régulières en un **DFA** (_Automate Fini Déterministe_) qui peut théoriquement s'exécuter en temps linéaire.

La notation que nous utiliserons est **BNF** (_Backus–Naur form_). Ne confondez pas cela avec **EBNF** (_extended Backus–Naur form_) ou **ABNF** (_augmented Backus–Naur form_) qui ont des fonctionnalités supplémentaires. Gardez cela à l'esprit lorsque vous regardez d'autres exemples en ligne qui pourraient utiliser d'autres formes fournissant plus de sucre syntaxique.

Commençons par les bases et définissons à quoi ressembleront les `strings` et les `integers`.

Notez que :

* Tous les noms de tokens doivent être en minuscules
* Toute clé précédée de '!' sera ignorée
* Toute clé précédée de '_' ne sera pas transformée en token
* Toute expression enfermée par '{' `expression` '}' peut être répétée 0 ou plusieurs fois

Dans l'exemple ci-dessous, nous ignorons tous les espaces blancs et avons défini un token `int` et `string_literal`.

Chaque langage a des `mots-clés` intégrés qui sont des mots réservés offrant une fonctionnalité spéciale. Mais comment le lexer saura-t-il si une `string` est un `mot-clé` ou un `identifiant` créé par l'utilisateur ? Il gère cela en donnant la préférence à l'ordre dans lequel les tokens sont définis. Par conséquent, définissons les `mots-clés` ensuite.

Nous terminerons cela en ajoutant la ponctuation nécessaire pour les expressions.

Super ! Voyons si cela fait réellement ce que nous voulons avec quelques **tests unitaires**. N'hésitez pas à coller cette partie dans votre IDE. 😊

**Note :** Il est généralement bon en Go de placer les fichiers de test dans le sous-répertoire pertinent, mais pour simplifier, je place tous les tests à la racine.

Pour tester notre **scanner**, exécutez :

```
$ gocc grammer.bnf$ go test -v=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/compiler       0.364s
```

Génial, nous avons maintenant un `**Lexer**` fonctionnel 🎉

#### Construction du Parser

La construction du `**Parser**` est similaire à celle du `**Lexer**`. Nous construirons un ensemble de séquences d'éléments qui, lorsqu'elles correspondent correctement à un flux de tokens, produisent une grammaire. Cela s'exécutera également en temps linéaire en convertissant internement notre grammaire **NFA** (_Automate Non Déterministe_) en **DFA** (_Automate Fini Déterministe_).

Gardons les choses simples. Qu'est-ce que notre programme ? Eh bien, c'est un ensemble d'`instructions` dans lequel chaque `instruction` peut contenir un ensemble d'`instructions` et/ou d'`expressions`. Cela semble être un bon point de départ pour notre grammaire.

Ci-dessous se trouve le début de la hiérarchie récursive du programme. `Statements` est une séquence de zéro ou plusieurs `Statements` et `Functions` est une liste de fonctions. Notre langage nécessite que les fonctions soient définies avant les autres types d'`instructions`. Cela réduira certains maux de tête lors de la phase de vérification de type. `empty` est un mot-clé en **BNF** qui représente un espace vide.

Mais attendez ! Qu'est-ce qu'une `instruction` ? C'est une unité de code qui ne retourne pas de valeur. Cela inclut : les instructions `if`, `let` et `return`. Cela s'oppose aux `expressions` qui retournent des valeurs. Nous y viendrons ensuite.

Ci-dessous se trouve notre grammaire pour `Statement` et `Function`. Un `StatementBlock` est une abstraction plus large qui encapsule une liste d'`instructions` avec des accolades `{` `}`.

Ensuite, construisons notre `Expression` qui gère toutes les opérations infixes telles que `+`, `-`, `*`, `<`, `>`, `==`, `&&`, `||`.

Presque terminé avec une grammaire entièrement fonctionnelle ! Terminons en définissant notre insertion de paramètres. Chaque `fonction` peut accepter n'importe quelle quantité de valeurs. Lors de la **définition d'une fonction**, nous devons étiqueter les types d'arguments dans la signature tandis qu'une **fonction appelée** peut accepter n'importe quelle quantité d'`expressions`.

Maintenant que notre parser est terminé, ajoutons du code à notre driver, `main.go`.

Au fur et à mesure que nous progressons dans le compilateur, nous ajouterons plus de fonctionnalités à ce driver.

L'une des choses difficiles dans la construction d'un parser est qu'il existe de nombreuses façons différentes de définir la grammaire. 🤔

Nous ne saurons pas vraiment comment nous nous en sommes sortis jusqu'à ce que nous arrivions à la section suivante qui utilise la sortie que nous venons de générer. La difficulté de construire le vérificateur de types statiques sera fortement influencée par notre conception de grammaire. Croisez les doigts 🤞.

#### Test du Parser

Nous garderons cela simple car à ce stade, notre parser peut encore produire des faux positifs. Une fois que nous commencerons à travailler sur l'AST, nous pourrons vérifier sa précision.

```
go test -v=== RUN   TestParser--- PASS: TestParser (0.00s)=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/go-compiler        7.295s
```

Félicitations 🎉 🎊 ! Vous avez maintenant un Lexer et un Parser entièrement fonctionnels. Il est temps de passer à l'AST (**A**rbre **S**yntaxique **A**bstrait).

### Arbre Syntaxique Abstrait

La meilleure façon de comprendre un arbre syntaxique abstrait est en relation avec un arbre d'analyse syntaxique, que nous avons généré dans le dernier article. Un arbre d'analyse syntaxique représente chaque partie du programme qui est appariée dans notre grammaire.

> En revanche, un AST ne contient que les informations liées à la vérification de type et à la génération de code, et ignore tout autre contenu supplémentaire utilisé lors de l'analyse du texte.

Ne vous inquiétez pas si cette définition n'a pas de sens pour le moment. J'apprends toujours mieux en codant, alors plongeons dedans !

Créez un nouveau répertoire et deux nouveaux fichiers. `ast.go` contiendra nos fonctions de génération AST et `types.go` aura les _types de nœuds d'arbre_.

```
mkdir astcd asttouch ast.gotouch types.go
```

Comme avec l'arbre d'analyse syntaxique, nous définirons notre structure de haut en bas. Chaque `nœud` sera soit une `instruction` soit une `expression`. Go n'est pas orienté objet, donc nous utiliserons un modèle de composition utilisant `interface` et `struct` pour représenter nos catégories de `nœuds`. Notre AST retournera un nœud `Program` qui contient le reste du programme. À partir de maintenant, toute structure que nous créons avec une méthode `TokenLiteral()` est un `nœud`. Si ce `nœud` a une méthode `statementNode()`, il correspondra à l'interface `Statement` et s'il a une méthode `expressionNode()`, c'est une `Expression`.

De plus, nous ajouterons des balises `json` à chaque champ de structure pour faciliter la conversion de notre AST en `json` à des fins de test.

Maintenant, commençons à construire nos structures `Statement` basées sur les interfaces `Statement` et `Node`.

**_Note:_** `json:"-"` signifie que le champ sera omis de notre json.

Ensuite, nous avons besoin de quelques crochets pour connecter nos `nœuds` et notre `parser`. Le code ci-dessous permet à nos nœuds `Statement` de correspondre aux interfaces `Node` et `Statement`.

Nous avons ensuite besoin des crochets qui seront appelés par le parser.

Comme vous pouvez le voir, **la plupart de notre code** vérifie et caste notre type d'entrée.

Ces crochets seront ensuite appelés par le parser dans `grammar.bnf`. Pour accéder à ces fonctions, nous devons `import "github.com/Lebonesco/go-compiler/ast"`.

Maintenant, lorsqu'une partie de la grammaire est identifiée, elle appelle un crochet AST et passe les données nécessaires pour construire un `nœud`.

Comme vous pouvez l'imaginer, il y a beaucoup de flexibilité dans la manière dont vous souhaitez générer votre AST. Il existe des **stratégies de conception** qui réduisent le nombre de nœuds uniques dans l'AST. Cependant, avoir plus de types de nœuds facilitera votre vie lorsque nous arriverons au `typechecker` et à la `génération de code`. 😊

Cette partie contient beaucoup de code. Cependant, ce n'est pas très difficile et c'est surtout la même chose. La gestion des erreurs en Go peut sembler un peu fastidieuse, mais à long terme, cela en vaudra la peine lorsque nous ferons une erreur stupide. La sécurité d'abord 🚧

Nous ne ferons rien de trop fou avec notre gestion des erreurs car je veux économiser des lignes de code. Cependant, si vous vous sentez inspiré, vous pouvez ajouter des erreurs plus descriptives et utiles.

Passons aux `Expressions` !

Adaptez-les aux interfaces `Node` et `Expression`.

Et créez les crochets `Expression`.

Enfin, insérez les crochets dans le `parser`.

#### Test du générateur AST

Les cas de test pour le générateur AST sont les plus fastidieux à écrire. Mais croyez-moi, ce n'est pas une partie que vous voulez rater. Si vous avez des problèmes ici, ces bugs se répercuteront dans votre `vérificateur de types` et votre `générateur de code`. 🐛

À mon avis, si le code n'a pas de tests, il est cassé.

Dans notre test AST, nous construirons à quoi devrait ressembler notre résultat final. Pour éviter de comparer des éléments tels que les `tokens`, qui pourraient créer des faux négatifs, nous convertissons notre résultat et la sortie attendue en json avant de les comparer avec une fonction de **comparaison profonde**, `reflect.DeepEqual()`.

Exécuter le test :

```
go test -v=== RUN   TestAST--- PASS: TestAST (0.00s)=== RUN   TestParser--- PASS: TestParser (0.00s)=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/go-compiler        9.020s
```

À mi-chemin d'un compilateur fonctionnel ! 🎉 Pendant que vous donnez à cet article quelques 👍 👍, n'oubliez pas de vous applaudir pour être arrivé aussi loin.

Ajoutons un peu plus de code au driver.

Passons maintenant à ma partie préférée, le **vérificateur de types**.

### Vérificateur de types

Notre vérificateur de types s'assurera que les utilisateurs n'écrivent pas de code qui entre en conflit avec notre langage **statiquement typé**.

L'épine dorsale de notre **vérificateur de types** sera une combinaison de structures de données qui suivent les types d'identifiants, l'initialisation et les opérations de types valides. Cela peut devenir beaucoup plus compliqué une fois que nous commençons à traiter avec différents niveaux de portée et de classes. Cependant, nous gardons cela aussi simple que possible. 😊

Pour commencer :

```
touch checker_test.gomkdir checkercd checkertouch checker.gotouch environment.go
```

`environment.go` contiendra toutes nos fonctions auxiliaires qui seront utilisées par notre **vérificateur** et notre **générateur de code** pour accéder et manipuler notre ensemble de variables et leurs types correspondants. Notre environnement est simple, donc cela sera direct.

Nous commencerons par définir toutes nos valeurs constantes, y compris les **types d'opérations**, les **types de variables** et la **cartographie de chaque type à ses méthodes valides**. 

**Note :** Si nous avions des classes dans notre langage, notre vérificateur gérerait cette troisième partie plutôt que de le faire à la main.

Le reste de `environment.go` sont des **getters** et **setters** basiques qui gèrent les identifiants et les fonctions.

La fondation de notre vérificateur de types sera une seule fonction **dispatch**, `checker()`, qui prend un `Node` et déclenche la fonction de vérification correspondante.

J'ai eu envie d'économiser des lignes de code, donc nous utiliserons un environnement global pour stocker nos types de variables.

**Note :** Cela ne serait pas possible si nous permettions aux `Block Statements` et aux `Functions` d'avoir leur propre portée ou si nous suivions les meilleures pratiques.

Maintenant, évaluons les `Statements`. Les `Block Statements` sont la seule instruction dans laquelle nous retournons un type afin de gérer le cas où il se trouve à l'intérieur d'une fonction. Si une `Return Statement` se trouve à l'intérieur du `Block Statement`, son type est retourné. Sinon, le `Nothing_Type` est retourné.

Passons à l'évaluation des `Expressions`. La partie la plus compliquée sera `evalFunctionCall()` car elle pourrait être une fonction intégrée telle que `PRINT()` ou définie par l'utilisateur.

**Note :** Actuellement, il n'y a qu'une seule fonction **intégrée**. Cependant, d'autres pourraient être facilement ajoutées étant donné le cadre que nous avons construit.

Super ! Ajoutons un petit extrait à notre driver.

#### Test du vérificateur de types

```
go test -v=== RUN   TestAST--- PASS: TestAST (0.00s)=== RUN   TestOperations--- PASS: TestOperations (0.00s)=== RUN   TestIdents--- PASS: TestIdents (0.00s)=== RUN   TestFunctions--- PASS: TestFunctions (0.00s)=== RUN   TestParser--- PASS: TestParser (0.00s)=== RUN   TestToken--- PASS: TestToken (0.00s)PASSok      github.com/Lebonesco/go-compiler        9.020s
```

J'ai fait des choix délibérés pour laisser certaines choses de côté dans ce langage, comme les `classes`, les `boucles for` et la `portée des fonctions`. La plupart des complexités qui découlent de ces éléments se produisent dans le `vérificateur` et le `générateur de code`. Si j'avais ajouté ces éléments, cet article serait beaucoup plus long. 😅

### Génération de code

Nous avons enfin atteint la dernière étape ! 🎉 🎊

Afin de gérer le plus de cas possible avec le moins de tracas, chaque `expression` sera assignée à une variable temporaire. Cela pourrait rendre notre code généré un peu gonflé, mais cela résoudra toutes les expressions imbriquées.

Le code gonflé n'aura aucun impact sur la vitesse finale du programme car l'optimiseur supprimera toute redondance lorsque nous compilerons notre code C++ généré final.

Notre générateur ressemblera au vérificateur de types. La principale différence est que nous passerons un `buffer` pour stocker le code généré.

Bien que j'aie choisi de compiler en C++, vous pouvez substituer n'importe quel langage. Le but principal de ce **Guide du compilateur Go** était de vous permettre de comprendre suffisamment les pièces pour pouvoir créer le vôtre.

Pour commencer :

```
touch gen_test.gomkdir gencd gentouch gen.go
```

Nous commencerons par importer tous les packages nécessaires et définir trois **fonctions utilitaires**, `write()` pour écrire le code généré dans un buffer, `check()` pour gérer les erreurs et `freshTemp()` pour générer des noms de variables **uniques** pour les variables temporaires que nous créons à la volée.

**Note :** Il est généralement mauvais en Go d'utiliser `panic()` pour la gestion normale des erreurs, mais je suis fatigué d'écrire des `if statements`.

Similaire au **vérificateur**, notre **générateur** a une fonction de dispatch centrale qui accepte un `Node` et appelle la fonction **gen** correspondante.

Générons quelques `Statements`. `genProgram()` génère les en-têtes nécessaires et la fonction `main()`.

La génération d'`Expressions` ressemblera beaucoup au code ci-dessus. La principale différence est qu'une variable `temp` est retournée représentant cette expression. Cela nous aide à gérer l'imbrication plus complexe des `Expressions`.

Le dernier morceau de code sera nos **types intégrés C++**. Sans cela, rien ne fonctionnera.

#### Test du générateur de code

### Rassembler le tout

Nous allons maintenant combiner notre **lexer**, **parser**, **générateur AST**, **vérificateur de types** et **générateur de code** en un programme exécutable final, `main.go`.

**Note :** Je fais tourner cela sur Windows donc mon C++ compile en `main.exe`. Si cela ne fonctionne pas pour vous, retirez l'extension `.exe`.

Pour trouver quelques programmes de test à exécuter, allez sur `github.com/Lebonesco/go-compiler/examples`.

```
go run main.go ./example/function.bxhello Jeff3
```

Et voilà ! Nous avons complété un compilateur entièrement fonctionnel en Go !

Merci d'avoir pris le temps de lire cet article.

Si vous l'avez trouvé utile ou intéressant, faites-le moi savoir 👍 👍 👍.