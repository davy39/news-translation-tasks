---
title: Un guide du bluffeur pour maîtriser JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T16:47:13.000Z'
originalURL: https://freecodecamp.org/news/bluffers-guide-to-javascript-proficiency-18195dbe2618
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7ieiD5CDf0l6rYS5LvODGQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Un guide du bluffeur pour maîtriser JavaScript
seo_desc: 'By Greg Byrne

  So you’re trying to learn JavaScript but are inundated with all the different syntax
  and ways to program that have evolved over time?

  Why is that code littered with backticks? What in the world are these mysterious
  arrows, they look lik...'
---

Par Greg Byrne

Vous essayez d'apprendre JavaScript mais vous êtes submergé par toutes les différentes syntaxes et façons de programmer qui ont évolué au fil du temps ?

Pourquoi ce code est-il parsemé d'accent graves ? Qu'est-ce que ces mystérieuses flèches, elles ressemblent à des emojis ? 3 points, quoi ?

Notre industrie est composée d'une masse d'individus psychologiquement épuisés, stressés par le syndrome de l'imposteur et le doute de soi. "Vais-je être démasqué et avouer que je ne sais pas ce que je fais ?", "Je n'ai aucune idée de comment ce code fonctionne, il semble juste fonctionner par magie." "Je n'ai rien accompli hier et tout le monde me regarde maintenant lors du daily scrum." "Je suis un tel échec et tout le monde fait mieux que moi." Ça vous dit quelque chose ?

Dans un environnement où le savoir est pouvoir, nous sommes comme des hamsters sur un tapis de course d'apprentissage, essayant simplement de devancer tout le monde pour ne pas avoir l'air stupide devant nos pairs. Ce manque de (mes) connaissances est devenu évident récemment lorsque j'ai rejoint un projet front-end composé principalement de code JavaScript. Je pensais connaître JavaScript. J'avais complètement tort.

Vous dites, "N'est-ce pas qu'il faut utiliser le mot-clé function pour déclarer des fonctions ?" (parce que c'était écrit dans ce blog/vidéo que vous avez lu/regardé l'autre jour) ; "Idiot — comment ne pas connaître les fonctions fléchées. Pshhaw !" se vante un collègue.

> Note : ce n'est pas mon expérience, heureusement, mais veuillez reconsidérer votre environnement s'il est aussi hostile...

Alors je vous donne ceci, un guide du bluffeur, pour vous aider à passer votre journée. Un résumé des syntaxes JavaScript introduites dans ES2015+ que tous les jeunes utilisent ces jours-ci, ainsi que certaines fonctionnalités JS moins connues. Cela vous aidera à dissimuler ces moments gênants où vous hochez la tête en signe de compréhension et changez poliment de sujet.

Avant que vous ne criiez "Oh Greg, tu es fou, tu as créé un article qui est TLDR, où vais-je trouver les 15+ minutes pour lire ton article". Premièrement, je reconnais cette douleur de ne pas avoir assez de temps dans la vie, alors je compatis. Deuxièmement, l'article est divisé en sections concernant une syntaxe particulière, donc si vous n'êtes pas intéressé par les fonctions fléchées, alors passez cette section. Vous n'êtes pas sûr des littéraux de gabarit, alors restez 2-3 minutes, ami, et laissez-moi vous en parler. **Vous n'avez pas à consommer l'article en entier en une seule fois !**

Je ne cache pas que cet article est destiné à ceux qui apprennent JavaScript et **qui ont les connaissances de base de son fonctionnement !** Pour que cet article vous soit utile, vous devez savoir comment écrire en JavaScript (par exemple, juste les bases des fonctions, des objets, etc.). Sinon, allez consulter mes autres publications sur JavaScript et/ou complétez cela avec un tutoriel vidéo sur les fondamentaux de JavaScript si nécessaire.

**De plus, cet article explique principalement en utilisant la syntaxe introduite dans ES2015 et au-delà, qui peut ne pas être supportée dans tous les navigateurs**. En utilisant Babel, la plupart des syntaxes peuvent être compilées pour la compatibilité. Pour d'autres comme _Set_ ou _includes()_, vous pouvez utiliser des polyfills, mais cela dépasse le cadre de cet article. Toujours **vérifier les tableaux de compatibilité des navigateurs**, les exigences de support des navigateurs de votre projet, et vos responsables techniques concernant l'introduction de quelque chose de nouveau.

### var est pour les nuls ; let et const sont l'avenir

`let` et `const` sont de nouvelles déclarations de variables introduites dans ES2015. La différence entre celles-ci et `var` est principalement la portée des variables.

`var` est limité à la portée de la fonction, ce qui signifie qu'il est disponible dans la fonction où il est déclaré et dans les fonctions imbriquées. Cela signifie que vous obtenez un comportement étrange comme :

Et je n'ai même pas parlé (et ne le ferai pas) de la confusion avec le _hoisting_.

`let` et `const` sont la manière dont les variables doivent être déclarées. Elles sont limitées au bloc, donc votre tête n'a pas à tourner comme une chouette sur votre cou par frustration face à des valeurs de variables indésirables et mystérieuses qui persistent au-delà de l'accolade de fin. `const` a l'avantage supplémentaire de l'immuabilité, donc celui-ci devrait être votre choix par défaut sauf si la mutabilité est spécifiquement requise.

Une chose à savoir avec `const` est qu'il n'est immuable que dans son assignation. Cela fonctionne bien pour les types primitifs comme String ou Number. Les objets se comportent légèrement différemment ; la référence de l'objet est immuable, mais leurs _propriétés_ sont toujours mutables.

Lequel devez-vous utiliser ? Eh bien, définitivement pas `var`. Il y a des opinions divergentes sur l'utilisation de `let` ou `const`. En fin de compte, cela dépend de l'opinion personnelle ou des conventions du projet. Je privilégie l'utilisation de `const` (contrairement à mes exemples de code) en raison de son immuabilité (à l'exception des propriétés des objets).

Si vous voyez `var` dans du code maintenant, soyez le premier à proclamer comment vous pouvez améliorer la qualité du code en le remplaçant par `let` et `const` et arrêtez de l'utiliser dès maintenant. Point.

### Notation abrégée d'initialisation d'objet — économisez un temps précieux

Je vais partager avec vous une information qui vous fera économiser quelques secondes de temps précieux. Un temps précieux ; vous laissant libre de faire ce que vous aimez (ou détestez). Une charge de linge supplémentaire, un autre "Oh, au fait" la prochaine fois que vous discuterez autour de la fontaine à eau mythique du bureau, du temps supplémentaire pour vous détendre avant le daily scrum, etc.

Les objets peuvent être initialisés avec une forme de notation abrégée qui vous permet de définir implicitement les paires clé-valeur sur les objets sans avoir à les énoncer explicitement, mais en passant simplement la variable de paramètre.

> Note : MENSA ne m'a pas envoyé d'e-mail ; s'ils le faisaient, avec ce sujet, je serais assez inquiet car je ne pourrais pas être certain que ce serait une bonne nouvelle...

Vous devez utiliser cette notation de manière sensée, cependant, et ne pas être l'ingénieur malchanceux qui a essayé d'utiliser des mots-clés ou des doublons dans votre fonction. Le premier causera des erreurs tandis que le second (et peut-être pire) écrasera simplement vos valeurs avec la dernière valeur d'argument.

### Littéraux de gabarit — le chat cool de la concaténation

Les [littéraux de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) (alias _chaînes de gabarit_) vous permettent de référencer des variables au sein de chaînes, sans tout le tracas de la concaténation explicite, en utilisant l'_accent grave_. Les utilisateurs de Slack et Medium seront instantanément familiers avec le symbole ` pour désigner le balisage de code.

Prenez cet exemple standard de concaténation :

Beurk, c'est fastidieux. Vous pouvez rendre le code plus efficace en utilisant les littéraux de gabarit :

Nous pouvons même l'utiliser pour remplacer le horrible caractère d'échappement de nouvelle ligne `\n` sans code supplémentaire requis.

Nous pouvons également exécuter des calculs et des expressions (appelés _interpolation d'expression_) au sein d'un littéral de gabarit sans rompre notre "chaîne" :

Et nous pouvons faire une imbrication de littéraux de gabarit :

Les [littéraux de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) sont les genoux de l'abeille proverbial de la concaténation JavaScript. Dans les projets de travail, je l'ai trouvé configuré par défaut dans les règles de linting de sorte que la concaténation explicite est automatiquement transformée en littéraux de gabarit. N'attendez pas une fête spéciale, impressionnez vos amis dès maintenant avec votre nouvelle syntaxe de concaténation.

### Paramètres par défaut — être pleinement équipé

Comme beaucoup de cette nouvelle syntaxe de code, j'ai vu les paramètres par défaut avant même de savoir qu'ils existaient. Bien sûr, en lisant le code, j'étais perplexe et un peu apoplectique quant à la raison pour laquelle une certaine valeur qui se voyait attribuer une valeur n'était pas cette valeur à l'exécution. C'était 5 bon sang — il est écrit ainsi dans le paramètre de la fonction, comment pouvait-ce être 10 à l'exécution ! Maudits gremlins de code. Bien sûr, cette crise momentanée n'était que de l'ignorance de ma part.

Les paramètres par défaut vous permettent d'utiliser, vous l'avez deviné, un paramètre..._PAR DÉFAUT !_ Autant que je me moque, c'est en fait un moyen simple (comme une gifle sur le front pour réveiller le cerveau) mais efficace de contrôler l'imprévisibilité de l'`undefined` entrant dans votre contrat de fonction.

Par exemple, la plupart des développeurs logiciels, quel que soit le langage, ont à un moment donné vu `if(something != null)` _(en vous regardant, Java)_ autour de blocs de code simplement parce qu'il y a toujours cette chance de 1 % que notre ennemi passe un objet ou une valeur qui n'est pas ce à quoi nous nous attendons, et nous devons le prendre comme une certitude absolue qu'ils le feront.

Imaginez si votre compte bancaire avait une fonction qui un jour recevait un `undefined`. J'imagine qu'une chirurgie serait nécessaire pour réattacher la mâchoire après qu'elle soit tombée de votre visage si vous voyiez le solde de votre compte comme **NaN**.

Alors, comment se défendre ? Correct — les paramètres par défaut.

Simple mais efficace.

Ceci est un exemple artificiel et beaucoup pointeront les nombreuses façons d'empêcher l'effondrement économique des systèmes comptables mondiaux de NaN de différentes manières. Attendez, mon ami — c'était juste pour montrer cet exemple.

Les paramètres par défaut protègent contre l'`undefined`, donc vous avez raison lorsque vous pensez "et si un type de valeur non attendu est entré — les paramètres par défaut ne protégeront pas contre cela". En effet, c'est vrai et selon votre code, vous pourriez avoir besoin de vérifications supplémentaires pour garantir le type de valeur correct.

### Déstructuration — magie d'assignation de valeur

Lorsque j'ai vu pour la première fois des objets être déstructurés (sans savoir ce que je regardais), j'étais très confus. Les accolades que j'associais à la notation des objets, mais dans la déclaration du nom de la variable avec un tas d'autres noms pointant tous vers la même référence d'objet ? De la magie noire, en effet.

La réalité est que c'est assez simple, mais son utilisation vous donnera l'air d'un magicien, même Harry sera jaloux. Le concept est le suivant : vous déclarez des variables immédiates avec des valeurs qui correspondent aux propriétés de même nom sur un objet.

Plus de _someObject.someProperty;_ juste des variables simples pour nos besoins de programmation futurs.

Que se passe-t-il si la variable n'est pas disponible ou si nous ne voulons simplement pas toutes les variables ? Eh bien, nous pouvons créer des variables uniquement pour les valeurs que nous voulons, et si nous déclarons une variable qui n'est pas sur l'objet, nous obtenons simplement la même valeur que si nous avions normalement déclaré une variable sans définition : `undefined`

Mais la magie ne s'arrête pas là. Nous pouvons _garantir_ que nos variables ont des valeurs par défaut au cas où elles ne seraient pas assignées.

Et si nous le voulons, nous pouvons même renommer les variables comme nous le souhaitons. De la sorcellerie, en effet.

Et tant que c'est un objet que vous déstructurez, peu importe qu'il soit déstructuré directement, ou donné comme objet de retour sur une fonction.

Cela inclut également la déstructuration au niveau des _paramètres_. Pourquoi feriez-vous cela, demandez-vous ? Cela élimine le besoin d'avoir un _ordre de paramètres_ lors de l'invocation d'une fonction. Je ne mens pas.

Tout comme les objets, nous pouvons faire tout cela avec les tableaux. L'astuce est d'utiliser la notation des crochets de tableau plutôt que les accolades d'objet. L'assignation est donnée par l'ordre d'index du tableau, donc la première variable se voit attribuer l'élément du premier index, et ainsi de suite.

Les exemples ci-dessus de déstructuration sont un bon résumé de ce que vous pouvez faire, mais si vous voulez vraiment devenir le Gandalf de la déstructuration JavaScript, alors consultez la [documentation MDN sur l'assignation de déstructuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

### Boucle For..of — itérer les itérables de manière itérative

La boucle `for..of` en JavaScript permet une itération plus efficace des itérables. Souvent, les gens pensent aux itérables comme aux tableaux (et ils ont raison, bien sûr), mais les itérables peuvent aussi être les caractères d'une chaîne, les paires clé-valeur dans une Map, les éléments d'un Set, etc. (pssshhh — voir plus de types itérables [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)).

Vous pourriez penser, _n'y a-t-il pas d'autres boucles for en JavaScript_, et vous auriez raison — il y en a ; le traditionnel `for`, le `for..in`, le `while` et le `do..while`, le `forEach` et `map`. Alors, qu'est-ce qui rend `for..of` spécial ?

La meilleure façon dont je me décris la différence entre `for..of` et `for..in` est que, bien que les deux itèrent sur des listes, `for..in` retourne les clés de l'objet, tandis que `for..of` retourne les valeurs de l'objet itéré.

La différence est plus apparente dans les chaînes.

Alors, pourquoi s'embêter avec les autres boucles `for` bien armées avec l'artillerie de `for..of` ? Eh bien, `for..of` ne permet pas la mutation (c'est-à-dire le _changement_) du tableau comme le ferait `for`. De plus, il ne fonctionne pas bien sur les propriétés des objets comme `for..in`.

J'ai trouvé les différentes façons de boucler en JavaScript bien, y compris `for..of`, mais la plupart de mes besoins étaient satisfaits par l'utilisation de `map`, `filter` et `reduce`, qui sont la royauté des itérables et que je décris plus loin.

Probablement, `for..of` sera le _moins_ utile pour vous sur cette liste, mais impressionnera tout de même les autres avec vos connaissances.

### Array includes — Pas d'indexation pour moi

Dans un projet de travail, j'ai vu `indexOf` utilisé pour vérifier une valeur dans un tableau. Il avait aussi la vérification pour `-1` pour être sûr qu'il y avait une logique pour gérer si elle n'était pas trouvée — `if(array.indexOf(b) < 0) {`..}. Dans un de mes rares éclairs d'inspiration, j'ai eu l'idée que puisque j'avais vu toute cette nouvelle syntaxe que je décris dans cet article, que sûrement un malin avait rendu cela plus facile et plus lisible ! Sûrement. Et j'avais raison.

`[Array.prototype.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)` vous permet, de manière plus lisible et plus logique, de vérifier si certains tableaux ont certaines valeurs. Il retourne un simple booléen plutôt qu'une valeur numérique sentinelle et, dans l'ensemble, devrait être le défacto pour l'interrogation des tableaux.

Un bémol — ce projet de travail sur lequel je travaillais devait supporter IE11 comme navigateur. Et devinez quoi ? Pour le navigateur-qui-ne-veut-pas-mourir, il n'est pas supporté. Il existe un polyfill disponible pour ceux qui doivent travailler dans de telles conditions dramatiques.

### Set — Diversité sur le lieu de travail

Pour quand vous ne voulez pas que votre tableau ait des valeurs en double, un Set est votre ami. Si vous connaissez Java et connaissez bien l'_interface_ Set et ses implémentations, ce n'est pas vraiment nouveau, alors voici un laissez-passer et passez votre chemin.

Un set est un objet qui prend un tableau et est capable de le débarrasser des valeurs en double.

Le Set a un tas de fonctions telles que `add`, `delete`, `forEach`, etc. qui vous permettent de parcourir et de manipuler le set en question.

### Spread — répandre l'amour des valeurs

L'opérateur Spread, bien que je pense personnellement que son nom est confus pour son utilisation, est en fait l'une des nouvelles syntaxes les plus utiles.

La syntaxe de l'opérateur Spread est trois points () avant la référence de l'objet.

L'opérateur Spread _développe_ essentiellement un objet itérable contenant des valeurs et les place dans un espace où plusieurs valeurs sont attendues (par valeur et non par référence). Toujours confus ? Ce n'est pas grave — décomposons cela davantage.

Combinons quelques tableaux en tableaux plus grands.

Notre utilisation du spread passe ces objets _par valeur_ et non par référence. Cela signifie que nous pouvons muter le tableau original sans nous soucier qu'un tableau composé soit changé.

Donc, oui, cela semble évident maintenant, vous pouvez essentiellement composer des tableaux comme des blocs Lego d'autres tableaux. C'est bien, mais quoi d'autre ?

Eh bien, les Spreads peuvent être utilisés dans les listes d'arguments de fonction.

Il suit les règles typiques des arguments de fonction JavaScript où les valeurs supplémentaires ne sont pas utilisées et les arguments manquants sont `undefined`.

Donc, les tableaux, vérifié. Les arguments de fonction, vérifié. Spread semble génial, non ? Eh bien, il a une dernière belle surprise qu'il veut vraiment vous montrer — en étalant les littéraux d'objet !

De cette manière, nous pouvons _composer_ nos objets avec des objets plus petits. Les propriétés de clé non uniques sont écrasées par la dernière valeur tandis que les propriétés uniques sont ajoutées.

Un bémol ; l'étalement des littéraux d'objet est plus à la pointe (au moment de l'écriture) que les autres fonctionnalités de syntaxe ici (étant introduit dans ES2018).

Pour plus d'informations sur _Spread_ et le support général des navigateurs pour cet étalement, voir l'[article MDN sur la syntaxe Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) (surtout le tableau de compatibilité des navigateurs).

### Opérateur Rest — Acceptant tout le reste de vous

Si vous comprenez la syntaxe Spread, cela devrait sembler une extension naturelle de sa fonctionnalité. Si vous venez d'un arrière-plan Java, je dirai simplement _varargs_ pour que vous puissiez passer rapidement.

L'opérateur Rest est une syntaxe qui permet _une référence_ à autant d'arguments que ceux passés dans une fonction. Il permet aux fonctions d'accepter autant d'arguments que vous voulez leur lancer (tant que l'opérateur Rest est le seul et dernier argument de la fonction). Je pense à son nom comme une référence à _tout le reste_ des arguments qu'une fonction devrait utiliser.

C'est tout. Simples.

Attendez, qu'en est-il de `arguments` ? Pourquoi ne pas l'utiliser ? Eh bien, `arguments` est une chose étrange, car il ne retourne pas un tableau, mais plutôt un objet de type tableau. À cause de cela, nous ne pouvons pas le traiter comme un tableau.

Dans la plupart des cas, vous ne voulez pas que vos fonctions acceptent autant d'arguments que certains ingénieurs voyous voudront leur lancer. Cela peut conduire à de l'imprévisibilité ; soyons honnêtes, le travail est assez difficile sans ajouter _plus_ de complexité. Il y aura des cas d'utilisation où, bien sûr, vous devez être ouvert à tout (par exemple, une fonction _sum_) et lorsque cela se produit, l'opérateur Rest est ce dont vous avez besoin.

### Fonctions fléchées — droit au but fonctionnel

De plus en plus de code que je vois de nos jours utilise des fonctions fléchées plutôt que la syntaxe traditionnelle `function`. Personnellement, mon arrière-plan vient de Java, qui est typiquement connu pour sa verbosité, donc je tombe naturellement dans ce style. Connaître les fonctions fléchées vous aidera à bluffeur la maîtrise de JavaScript parmi vos pairs, à gagner des amis et à influencer les gens.

Les fonctions fléchées rationalisent la syntaxe traditionnelle des fonctions pour être moins verbeuses et plus courtes à implémenter. Bien sûr, il y a des _mineures_ différences entre elles et les expressions de fonction (comme pas de `this`, `super`, ou `arguments`), mais généralement, c'est un compromis acceptable.

Dans des lignes comme ci-dessus, non seulement nous nous sommes débarrassés du mot-clé `function`, mais nous avons également pu nous débarrasser des accolades et du mot-clé `return`. Cela est connu sous le nom de "corps concis". Vous pouvez bien sûr encore utiliser des accolades pour une logique multi-ligne, ce qui est connu sous le nom de "corps de bloc".

Les fonctions fléchées sont efficacement adaptées pour être utilisées dans les rappels.

> Oui, oui, je sais, le code ci-dessus aurait pu être rationalisé, comme les écailles d'un poisson élégant, pour être une ligne ; mais si je l'avais fait, je n'aurais pas pu montrer une fonction fléchée multi-ligne !

Les fonctions fléchées sont devenues plus prévalentes dans les frameworks JavaScript tels que React, où voir des composants sans état définis en utilisant des fonctions fléchées est assez ordinaire.

Ce n'est vraiment qu'un aperçu de ce que les fonctions fléchées peuvent faire, mais en tant que guide du bluffeur, c'est suffisant pour vous aider à passer la journée sans attirer le regard scrutateur de vos collègues autocratiques.

Alors, sortez et commencez à tirer des flèches partout ; pointez des flèches sur toutes les fonctions de vos amis ; cela séduira tout le monde avec votre maîtrise de JavaScript encore plus. Devenez aussi précis qu'un archer, et pour des leçons de maîtrise — voir la [documentation MDN sur les fonctions fléchées](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

### Noms de propriétés calculés — ne calcule pas ?

Les noms de propriétés calculés sont les noms de propriétés qui sont dérivés des valeurs d'autres variables. Malheureusement, vous ne pouvez pas assigner des variables directement comme clé à un objet.

Un outil disponible est d'utiliser la notation _crochets_. Cela peut être utilisé pour accéder aux propriétés d'un objet, tout comme son ennemi, l'opérateur _point_. Par exemple, `person['name']` est la même chose que `person.name`.

Nous pouvons également utiliser la même syntaxe pour _définir_ des propriétés sur des objets en utilisant leur valeur comme clé.

Ce qui est encore mieux, c'est que depuis ES2015, cela est devenu beaucoup plus facile ! Plus de bazar avec la création de l'objet, puis l'assignation de la valeur ensuite, et autres choses, beurk, si désordonné. Juste une définition clé-valeur directe. Quel soulagement.

### Map, filter, reduce — Pas de la cartographie

Je suis arrivé tard dans le jeu pour apprendre `map`, `filter` et `reduce`, et pire encore, ceux-ci ne sont pas des syntaxes _nouvelles_ ou _modernes_.

J'ai utilisé la syntaxe de boucle typique (par exemple, `for`) venant d'un arrière-plan Java. Cela signifie que lorsque je devais parcourir les éléments d'un tableau, je créais souvent un nouveau tableau vide, interrogeais le tableau de valeurs, et transférais les éléments que je voulais.

Un effort si gaspillé. Heureusement, il existe des moyens plus agréables de compléter ces épreuves.

J'aime penser à l'utilisation de `map` lorsque mes besoins sont :

* Je dois _transformer_ le contenu d'un tableau
* Je retourne un nouveau tableau

Alors, que veux-je dire par _transformer_ ? Eh bien, c'est une bonne question, cela pourrait être de manipuler le contenu du tableau de n'importe quelle manière. Par exemple, si je veux doubler les nombres dans un tableau de nombres, ou (plus pratiquement) créer un tas d'éléments HTML avec des valeurs d'un tableau de chaînes.

Généralement, `map` est adapté à la plupart des besoins de boucle que j'ai trouvés et il conserve également l'immuabilité du tableau original en retournant un nouveau tableau, ce qui est génial. Il est devenu ma manière par défaut de boucler dans la plupart des cas d'utilisation.

`filter` est, comme son nom l'indique, filtre un tableau et retourne une nouvelle _copie_ de ce tableau (filtré bien sûr). Très similaire à `map` à bien des égards, la seule différence est que le rappel doit retourner une valeur booléenne (pour indiquer si la valeur doit être conservée ou non). Magique !

Enfin, `reduce` est l'acte de _réduire_ votre tableau à une seule valeur, (comment déductif de votre part). Anecdotiquement, je n'ai pas vu beaucoup d'utilisation de cela en dehors des nombres autre que la concaténation de chaînes, etc. Mais hey, si c'est le bon outil pour le bon travail, alors qui suis-je pour argumenter.

`reduce` est un peu différent de `map` et `filter` en ce sens qu'il prend un _accumulateur_ ou une valeur _précédente_ (représentant le total jusqu'à présent) et la _valeur actuelle_.

C'est cool — je peux prendre un tas de nombres et les réduire à une seule valeur basée sur une règle. À partir de là, je pourrais obtenir des moyennes, des comptes, des écarts, et appliquer toute une agglomération de trucs de magie mathématique.

Mais qu'en est-il des objets ? Eh bien, vous pouvez... en quelque sorte. Reduce peut prendre un objet initial, ajouter des propriétés et attacher des valeurs. Comme dit précédemment, je n'ai personnellement pas vu beaucoup de cas d'utilisation autres que de compter le nombre de fois qu'un objet est dans un tableau, puis assigner les valeurs de compte à un objet de retour. Alors avec cette bombe...

Ce qui est génial avec `map`, `filter` et `reduce`, c'est qu'ils sont des [fonctions de l'Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), et comme ils retournent tous des tableaux, cela signifie qu'ils peuvent être enchaînés les uns après les autres. Des trucs puissants, en effet.

### Classes — comment rester classe

Pour ceux qui ont lu mon autre article [OOP Digest in JavaScript](https://medium.com/@byrne.greg/oop-digest-in-javascript-c57b52929fda), ou ceux qui ont expérimenté les joies de React (oui, je l'ai dit), les classes ne sont pas inconnues. Cependant, ce qui a été la surprise pour moi, en plongeant dans React avant de comprendre le JS moderne, c'est que la syntaxe `class` était un produit de _vanilla JavaScript_ et non une bibliothèque ou un framework.

Les classes sont presque un autre article à écrire et, pour être honnête, celui-ci est déjà assez encombrant, donc pour être concis, je vais souligner la compréhension simplifiée et vous envoyer avec la carte pour trouver plus de trésors d'informations.

Alors, avant de vous inquiéter de la complexité des Classes, il y a un réconfort simple à savoir : le modèle prototypal orienté objet de JavaScript n'a pas changé. Le ciel est en haut et le sol est en bas pour ceux d'entre nous qui sont encore quelque peu debout. MDN définit les classes comme [**_du sucre syntaxique_** _sur l'héritage basé sur les prototypes existants de JavaScript_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) et une belle façon de dire — c'est juste une autre façon de créer des objets (indice : 'orienté objet').

Traditionnellement, nous utilisions `function` pour créer des objets en JavaScript, et nous pouvons toujours le faire, bien sûr. Mais les classes **remplacent en toute sécurité** l'idée d'utiliser une `function Dog() {}` pour créer des objets en éliminant la confusion autour des fonctions qui sont, eh bien, des fonctions, et celles utilisées en mode constructeur.

Cela le fait en forçant l'utilisation du mot-clé `new`. Auparavant, lorsqu'une fonction qui était en fait une fonction constructeur (c'est-à-dire qui avait besoin de `new`) était appelée à l'ancienne, les propriétés étaient en fait définies sur l'objet _callee_, ce qui, bien sûr, provoquait un pandémonium.

Il y a un tas d'autres fonctionnalités de classes à considérer :

* Constructeurs

Les constructeurs peuvent être utilisés pour l'initialisation des objets et viennent avec leur propre mot-clé réservé.

* Fonctions d'objet

Auparavant, si nous voulions qu'un "type" d'objet contienne une fonction accessible à tous de ce type, nous la définissions sur le prototype de cet objet. Laborieux. Maintenant, nous pouvons facilement l'ajouter à la classe.

* Getters/Setters

Les classes peuvent utiliser les mots-clés `get` et `set` comme accesseurs/mutateurs pour accéder aux variables d'une classe. En règle générale, les classes ne peuvent pas contenir de variables d'instance déclarées au niveau de la classe (_comme en Java_), mais peuvent contenir des propriétés d'objet standard définies et récupérées à l'aide de fonctions. Note : notre convention `_` pour désigner quelque chose de privé n'est pas réellement privée en JavaScript et est accessible.

* Héritage

L'héritage est assez similaire pour quiconque a un arrière-plan dans les langages OOP comme Java. Il permet, à son niveau le plus simple, de transmettre des fonctions d'un type parent à un type enfant. Cela était apparemment assez fastidieux à faire avant ES2015.

Pour vous envoyer sur la voie de plus d'informations — je recommande vivement un article sur [JavaScript ES6 Class Syntax par Cory Rylan](https://coryrylan.com/blog/javascript-es6-class-syntax) que j'ai trouvé très éclairant sur le monde des classes JavaScript. C'est rapide et rempli de plus jolis exemples de code comparant l'ancienne et la nouvelle syntaxe JavaScript.

### Résumé

Alors, armé (secrètement bien sûr) de ce guide du bluffeur, vous devriez être l'envie de vos amis, craint par vos ennemis, et bien parti pour monter de niveau avec tous vos nouveaux points d'expérience JavaScript.

Cet article était long, oui, je ne m'excuse pas pour mon articulation bardique. Cependant, vous pourriez offrir un contre-argument différent et plus violent ; donc si j'étais amené à offrir un ensemble minimal de points à retenir — concentrez-vous sur **let/const, les fonctions fléchées, Spread** et **la déstructuration.**

Enfin, j'espère que vous penserez à moi lorsque vous serez riche et célèbre grâce à l'enseignement de cet article. Prenez réconfort en sachant que je secouerai mon poing avec colère.

> Si vous avez lu cet article, simplement sauté après un ou deux paragraphes, ou plus simplement vous n'en avez pas vraiment quelque chose à faire ; nourrissez quand même mon addiction à la validation publique en me donnant un applaudissement, puis allez consulter mes autres articles.

> Si vous n'avez pas aimé cet article et souhaitez enregistrer votre ressentiment, vous pouvez le faire en donnant un applaudissement haineux.

> Les **opinions exprimées** dans cette publication sont celles de l'auteur. Elles ne prétendent pas refléter les **opinions** ou vues de toute organisation ou entreprise à laquelle l'auteur peut être lié.