---
title: Qu'est-ce que la programmation informatique ? Définition du développement logiciel.
subtitle: ''
author: Phoebe Voong-Fadel
co_authors: []
series: null
date: '2020-04-16T15:38:38.000Z'
originalURL: https://freecodecamp.org/news/what-is-computer-programming-defining-software-development
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/illustration_cover.png
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Qu'est-ce que la programmation informatique ? Définition du développement
  logiciel.
seo_desc: 'My five year old son, Ramy, approached me one day while I was working from
  home and asked, “What are you doing Mama?”

  “I’m working,” I replied.

  He looked at my laptop screen and inquired again: “But what are you doing?”

  I paused and started to think ...'
---

Mon fils de cinq ans, Ramy, est venu me voir un jour alors que je travaillais depuis la maison et m'a demandé : « Qu'est-ce que tu fais, Maman ? »

« Je travaille », ai-je répondu.

Il a regardé l'écran de mon ordinateur portable et a demandé à nouveau : « Mais qu'est-ce que tu *fais* ? »

J'ai marqué une pause et j'ai commencé à réfléchir à cela. Je suis une développeuse web et je programme en JavaScript. Comment expliquer cela à un enfant de cinq ans ?

« J'écris des instructions pour l'ordinateur et l'ordinateur fait ce que je lui dis de faire. Cela s'appelle la programmation », ai-je expliqué. Ramy avait l'air perplexe.

J'ai continué : « Par exemple, je peux donner à l'ordinateur des instructions pour additionner deux nombres et il me donnera la réponse. » J'ai écrit une fonction qui additionnait 2 + 2 et je lui ai montré la réponse sur mon écran. Ses yeux se sont illuminés.

À partir de ce moment, j'ai commencé à réfléchir à *qu'est-ce que la programmation* ? Que se passe-t-il réellement sous le capot ? Lorsque j'ai commencé à apprendre à coder en 2017 sur [freeCodeCamp](https://www.freecodecamp.org/), j'ai utilisé l'éditeur de code intégré sur le site web et je voyais les résultats. Cependant, je ne comprenais pas vraiment la magie qui se passait derrière les coulisses.

J'ai commencé à faire quelques recherches et voici quelques-uns des termes que j'ai recherchés : « Qu'est-ce que la programmation informatique ? Qu'est-ce qu'un logiciel ? » Il y a plus de 600 millions de résultats de recherche sur Google pour « Qu'est-ce que la programmation informatique ? » C'est un peu comme tomber dans un terrier de lapin – cela peut être compliqué et accablant.

Je voulais rassembler une introduction complète à ce qu'est la programmation informatique et le développement logiciel pour les débutants. Je vais commencer par la programmation informatique, puis aborder les langages de programmation. Ensuite, je parlerai des logiciels et du développement logiciel. Enfin, je passerai aux tendances actuelles et à l'avenir de la programmation informatique.

Si vous envisagez de vous lancer dans le monde de la programmation ou si vous êtes simplement intéressé par l'apprentissage du code, cela vous fournira un aperçu général, sans (trop !) de jargon technique.

Une seule chose à noter : vous pouvez utiliser les mots « Développeur » et « Programmeur » pour désigner quelqu'un qui écrit du code.

## Qu'est-ce que la programmation informatique ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_input_output.png align="left")

Sur Wikipedia, la définition de « Programmation informatique » est :

> *« La programmation informatique est le processus de conception et de construction d'un programme informatique exécutable pour accomplir un résultat informatique spécifique. »*

Mais que signifie cela ?

Un ordinateur en lui-même n'est pas intelligent. Oui, ils sont puissants et ont le potentiel d'effectuer des tâches beaucoup plus rapidement qu'un humain. Mais les ordinateurs ont besoin qu'un humain écrive des instructions et leur dise quoi faire.

Par conséquent, la programmation est le processus d'écriture de ces instructions. Nous utilisons un langage de programmation pour cela. Ces instructions sont traduites dans un format lisible qu'un ordinateur peut comprendre. Les instructions sont ensuite exécutées par l'ordinateur.

## Programmation : comment faire une tasse de thé

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_programming_tea.png align="left")

Prenons l'exemple de la préparation d'une tasse de thé. Si vous deviez donner des instructions sur la façon de faire une tasse de thé, cela ressemblerait à ce qui suit :

1. Faire bouillir de l'eau
   
2. Verser de l'eau chaude dans une tasse avec un sachet de thé
   
3. Laisser infuser le thé
   
4. Retirer le sachet de thé
   
5. Ajouter du lait et/ou du sucre (si désiré)
   

Simple, n'est-ce pas ?

Ce que nous tenons pour acquis, c'est que la communication avec un être humain est différente de la communication avec un ordinateur. Un humain a des connaissances et une expérience de vie antérieures – ils peuvent savoir où trouver le thé. Nous supposons qu'ils savent que le lait est conservé dans un réfrigérateur.

Les humains ont aussi de l'intuition. Si vous ne trouvez pas de tasse, vous pourriez alors chercher dans les placards. Il y a aussi la lecture des indices non verbaux des gens comme le langage corporel.

En matière de programmation, vous devez être **très** spécifique. En continuant avec l'exemple de la préparation d'une tasse de thé, vous pourriez écrire des instructions en [pseudo-code](https://en.wikipedia.org/wiki/Pseudocode) comme ceci :

1. Allez dans la cuisine
   
2. Localisez la bouilloire
   
3. Ouvrez le couvercle de la bouilloire
   
4. Remplissez la bouilloire d'eau
   
5. Allumez la bouilloire
   
6. Attendez qu'elle bout à 100 degrés Celsius
   
7. Trouvez une tasse
   

Et ainsi de suite.

Et si des instructions comme celles ci-dessus ne suffisent pas ? Vous devrez peut-être ajouter une certaine *logique* pour tenir compte de tous les scénarios. Par exemple : 2) Localisez la bouilloire. Eh bien, est-ce une bouilloire électrique ou une bouilloire que vous mettez sur une plaque de cuisson ? Vous devrez ajouter une condition que **si** c'est une bouilloire électrique, alors faites xyz. **Sinon**, faites xyz pour une bouilloire que vous mettez sur une plaque de cuisson.

Même lorsque vous pensez avoir tenu compte de chaque condition possible et donné des instructions très spécifiques, il y a des choses que vous n'avez peut-être pas prévues. Vous commencez à faire votre tasse de thé et quelque chose ne va pas. Oh non ! Votre bouilloire cesse de fonctionner après avoir commencé à faire bouillir l'eau.

Qu'est-il arrivé ? Il y a un bug dans votre code ! Un bug est une erreur ou un défaut dans votre code qui peut entraîner des résultats inattendus. Afin de corriger votre code, vous passez par un processus de « [débogage](https://en.wikipedia.org/wiki/Debugging) », où vous trouvez les problèmes dans votre code et résolvez les problèmes.

Dans ce cas, vos instructions n'incluaient pas de remplir votre bouilloire à 0,8 litre pour couvrir l'élément chauffant. Donc la bouilloire s'éteint par mesure de sécurité.

Pour éviter que des erreurs ne se produisent après l'exécution de votre programme, les développeurs effectuent des tests et des [tests unitaires](https://en.wikipedia.org/wiki/Unit_testing) sur leurs programmes. Les tests unitaires consistent à écrire des tests pour des parties de votre code. Les tests échouent ou réussissent.

Par exemple, vous écrivez une fonction qui additionne deux nombres : 1 + 1. Vous écrivez ensuite un test unitaire où le résultat attendu est 2. Toutes les réponses échoueront sauf si c'est 2.

Vous passez en revue votre code jusqu'à ce que tout fonctionne sans aucun problème inattendu. La programmation est donc un processus détaillé et itératif où vous améliorez continuellement ce que vous avez écrit précédemment.

## Comment votre ordinateur comprend-il votre code ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_low_high_languages.png align="left")

Ce que la plupart des programmeurs écrivent en tant que « code » est un [langage de programmation de haut niveau](https://en.wikipedia.org/wiki/High-level_programming_language). Il est [abstrait](https://levelup.gitconnected.com/what-is-abstraction-in-programming-2f35c8c72e15) par conception. L'abstraction dans ce contexte signifie que nous nous éloignons du code machine et que les langages de programmation sont plus proches des langues parlées.

Mais un ordinateur ne peut pas comprendre le code basé sur du texte. Il doit être compilé (traduit) en [code machine](https://en.wikipedia.org/wiki/Machine_code). Le code machine est un ensemble d'instructions qui peuvent être comprises par l'unité centrale (CPU) d'un ordinateur. Considérez le CPU comme le cerveau d'un ordinateur. Le code machine est composé de uns et de zéros. Cela s'appelle le binaire.

Par exemple, voici comment vous écrirez « Hello World » en binaire :

`01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100`

Comme vous pouvez le voir, le binaire n'est pas facilement lisible pour les humains, donc nous évitons généralement de programmer en code machine !

## Qu'est-ce qu'un langage de programmation exactement ?

Les langages de programmation se situent à la fois dans le spectre des langages de bas niveau, comme l'assembleur, et des langages de programmation de haut niveau, comme JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_spoken_programming_lang.png align="left")

Mais qu'est-ce qu'un langage de programmation exactement ? La meilleure analogie à laquelle je peux penser sont les langues parlées que nous utilisons aujourd'hui. Toutes les langues expriment la même idée, mais de différentes manières à une autre personne :

Anglais : Hello

Français : Bonjour

Espagnol : Hola

Les langages de programmation sont différentes façons d'exprimer la même idée, mais à un ordinateur. Les exemples suivants imprimeront « Hello » dans trois langages de programmation différents :

JavaScript : `alert("Hello");`

Python : `print("Hello")`

Perl : `print "Hello";`

Chaque langage de programmation a sa propre [syntaxe](https://en.wikipedia.org/wiki/Syntax_(programming_languages)). En anglais, nous avons la grammaire. Il en va de même pour les langages de programmation – chacun a son propre ensemble de règles.

## Comment savoir si un langage de programmation est un langage de programmation ?

Cela peut sembler une question étrange à poser. Tout le code est-il écrit dans un langage de programmation ? Techniquement, non. Par exemple, il y a une idée fausse que [HTML](https://en.wikipedia.org/wiki/HTML) (HyperText Markup Language) est un langage de programmation. En fait, c'est un langage « [déclaratif](https://en.wikipedia.org/wiki/Declarative_programming) », qui, selon Wikipedia, est :

> *« ...un style de construction de la structure et des éléments des programmes informatiques - qui exprime la logique du calcul sans décrire son flux de contrôle. »*

En d'autres termes, HTML fournit la structure d'une page web, mais ne contrôle pas le comportement ou le fonctionnement du site web.

Vous pouvez déterminer si un langage est un langage de programmation en vérifiant s'il est « Turing complet ». La [machine de Turing](https://en.wikipedia.org/wiki/Turing_machine) est une machine hypothétique décrite par Alan Turing en 1936. Pour qu'un langage de programmation soit [Turing complet](https://en.wikipedia.org/wiki/Turing_completeness), il doit avoir :

1. Des branchements conditionnels (que j'explore ci-dessous).
   
2. La capacité de lire et d'écrire sur une bande de papier infinie. Cela signifie essentiellement pouvoir stocker des données en mémoire.
   

Je ne vais pas approfondir ce sujet, mais si vous êtes intéressé, cette [vidéo](https://www.youtube.com/watch?v=RPQD7-AOjMI) est une introduction utile.

## Quels sont les fondamentaux d'un langage de programmation ?

Il existe certains éléments de base qui sont couramment présentés. Cela inclut les variables, les boucles, les instructions conditionnelles, les structures de données et les algorithmes. Ce sont les éléments de base de la plupart des langages de programmation.

### Qu'est-ce qu'une boucle 'for' ?

Les boucles 'for' sont utiles si vous devez exécuter un ensemble d'instructions de manière répétée. Par exemple, vous prenez le thé de l'après-midi et vous devez faire cinq tasses de thé pour vos invités. Pour faire une tasse de thé, vous devez suivre un ensemble d'instructions, comme dans mon exemple précédent.

Au lieu d'écrire les instructions cinq fois, vous pouvez dire à l'ordinateur de répéter les mêmes instructions cinq fois. Cela vous permet de mettre à l'échelle.

Voici un exemple d'une boucle `for` de base :

```js
for (let i = 0; i < 5; i++) {
  console.log("Make Tea!");
}

// résultat attendu :
"Make Tea!"
"Make Tea!"
"Make Tea!"
"Make Tea!"
"Make Tea!"
```

### Qu'est-ce qu'une instruction conditionnelle ?

En JavaScript, nous avons des instructions conditionnelles `if...else`. Celles-ci sont utilisées lorsque vous souhaitez exécuter différentes actions en fonction d'une condition.

En revenant à mon exemple précédent, vous demandez à l'utilisateur **s**'il veut du lait dans son thé. **Si** il veut du lait, alors ajoutez du lait au thé, **sinon** ne faites rien.

Voici un exemple d'une instruction `if...else` en JavaScript :

```js
if(milk == true) {
  // ajouter du lait
  } else {
  // ne pas ajouter de lait
}
```

### Quelles sont les structures de données ?

> *« Une structure de données est une manière d'organiser les données afin qu'elles puissent être utilisées efficacement... Elles sont des ingrédients essentiels dans la création d'algorithmes rapides et puissants. »*

([Cours sur les structures de données, de facile à avancé, William Fiset](https://www.youtube.com/watch?v=RBSGKlAvoiM))

Les [structures de données](https://en.wikipedia.org/wiki/Data_structure) courantes que vous pouvez trouver dans de nombreux langages de programmation sont les tableaux, les objets, les tuples et les unions. Je vais prendre les tableaux comme exemple.

En JavaScript, un tableau peut stocker une gamme de données telles que des nombres et des chaînes de caractères (texte). J'aime les biscuits avec mon thé, donc je vais les stocker dans mon tableau :

```js
biscuits = ["shortbread", "digestive", "ginger nut"];
```

Ces biscuits sont stockés dans la mémoire de l'ordinateur et vous, en tant que développeur, pouvez accéder à un biscuit spécifique en référençant son [index](https://simple.wikipedia.org/wiki/Array_data_structure). Vous commencez à compter l'index à partir de 0. L'index est comme la position du biscuit dans une boîte à biscuits. Vous le référencez en utilisant la notation des crochets.

```js
biscuits[0]; // "shortbread"
biscuits[1]; // "digestive"
biscuits[2]; // "ginger nut"
```

Si vous voulez obtenir un biscuit digestif, vous pouvez accéder à sa position d'index : `biscuits[1]`. Je peux facilement le trouver parce que je sais où il est stocké.

Rappelez-vous que le premier élément du tableau est l'index 0. Donc lorsque vous référencez l'index 1, il s'agit en fait du deuxième élément du tableau.

Par conséquent, les structures de données sont un moyen de gérer les données. Cela inclut le stockage et la récupération des données. Il est plus efficace d'exécuter des algorithmes si les données sont organisées dans une structure de données.

### Qu'est-ce qu'un algorithme ?

Un [algorithme](https://simple.wikipedia.org/wiki/Algorithm) est un ensemble spécifique d'instructions qui résout un problème. C'est un concept abstrait. Voici un lien vers une courte vidéo de TED sur "[Qu'est-ce qu'un algorithme ?](https://youtu.be/6hfOvs8pY1k)".

Vous vous souvenez lorsque nous écrivions des instructions sur la façon de faire une tasse de thé plus tôt ? Cela est essentiellement un algorithme : un ensemble d'instructions séquentielles.

Lorsque j'ai écrit ma première fonction en JavaScript, j'ai en fait créé mon premier algorithme sans savoir que c'était un algorithme ! Une fonction est une implémentation d'un algorithme.

Tout comme dans la vie réelle, il existe souvent plusieurs solutions pour un problème de codage. Par exemple, disons que vous prévoyez d'aller dans un café que vous n'avez jamais visité auparavant. Il y a plusieurs façons d'atteindre votre destination. Certains itinéraires prennent plus de temps que d'autres, mais finalement, ils vous mènent tous au même endroit. Idéalement, vous voulez choisir l'itinéraire le plus rapide, le plus efficace et le plus facile.

Le même principe peut être appliqué à la programmation. Il existe généralement plusieurs façons de résoudre un problème de codage, et les programmeurs s'efforcent de trouver la solution la plus élégante et la plus efficace.

Les développeurs n'ont souvent pas tout de suite juste ! Tout comme j'écrirais un premier jet pour un article, c'est la même chose pour le codage. Je réécrirais un article plusieurs fois, où je pourrais changer la structure, éditer, réécrire des sections et supprimer des phrases inutiles. En programmation, nous passons par un processus similaire, et nous appelons cela la [refactorisation](https://en.wikipedia.org/wiki/Code_refactoring) de notre code.

## Quels sont les principaux langages de programmation utilisés aujourd'hui ? Combien y en a-t-il ?

Il semble y avoir un certain débat sur le nombre total de langages de programmation sur Internet. Certains sites web comme [Wikipedia](https://en.wikipedia.org/wiki/List_of_programming_languages) listent environ 700 des langages de programmation actuels et historiques « notables ». D'autres sites comme [Tiobe](https://www.tiobe.com/tiobe-index/programming-languages-definition/#instances) suivent et surveillent 250 des langages les « plus populaires ».

Sur [Github](https://github.com/), le langage de programmation le plus populaire de 2019 était JavaScript :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/github-most-popular-languages.png align="left")

*Source :* [*https://octoverse.github.com/#top-languages*](https://octoverse.github.com/#top-languages)

### Pourquoi y a-t-il tant de langages de programmation ? Comment les langages de programmation ont-ils évolué ?

Différents langages de programmation sont développés pour satisfaire différents besoins. Cela est démontré tout au long de l'histoire des langages de programmation. Veuillez vous référer à ce diagramme d'O'Reilly qui cartographie l'[histoire des langages de programmation des années 1950 à 2004](https://www.cs.toronto.edu/~gpenn/csc324/PLhistory.pdf).

Dans les années 1950, le FORTRAN (Formula Translation) a été créé pour résoudre des problèmes mathématiques, statistiques et scientifiques complexes. Le COBOL (« Common Business Oriented Language ») a été créé en 1959 pour faciliter l'utilisation du code par les entreprises. Il existe certains langages plus adaptés à l'analyse statistique comme R (1976).

Il y a eu l'essor des langages de programmation à usage général à partir des années 1970, tels que C, C++, C# et Java. Comme vous pouvez le voir dans le graphique ci-dessus, les langages à usage général dominent le top 10 des langages les plus populaires.

JavaScript, créé en 1995, est un langage populaire pour le web. Il donne aux sites web leur interactivité et leur vie.

Plus récemment, nous avons vu la naissance de nouveaux langages comme Go de Google, qui était destiné à maintenir des systèmes logiciels de grande taille plus efficacement. Nous verrons probablement encore plus de langages de programmation créés à l'avenir.

## Langages de programmation compilés vs. interprétés

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_compiled_interpreted.png align="left")

À mesure que vous devenez plus familier avec les langages de programmation, vous rencontrerez des langages de programmation compilés et interprétés. Quelle est la différence ?

### Qu'est-ce qu'un langage compilé ?

Les langages de programmation comme C, C++, et Java ont un processus de « construction » où votre code est compilé en un format plus lisible (langage machine) pour l'ordinateur.

Il peut être plus facile de penser à deux personnes qui ne parlent pas la même langue, mais qui doivent travailler ensemble. John parle anglais et Chloe parle français. Chloe écrit un ensemble d'instructions sur la façon de faire un soufflé au chocolat en français, mais John ne peut pas le comprendre. Ils ont besoin d'un traducteur qui peut parler à la fois l'anglais et le français. Il est plus facile si le traducteur peut traduire les instructions de Chloe à l'avance avant qu'ils ne commencent à cuisiner ensemble.

Au lieu de cela, les développeurs « parlent » un langage de programmation comme Java ou Python. Ils ont besoin que leur code soit compilé (traduit) en langage machine avant qu'un programme ne puisse s'exécuter afin que l'ordinateur puisse le comprendre.

Les programmes créés à partir d'un langage compilé sont plus faciles à comprendre pour un ordinateur, et donc s'exécutent très rapidement.

### Qu'est-ce qu'un langage interprété ?

JavaScript, PHP et Python sont des exemples de langages de programmation interprétés. Il n'y a pas de processus de construction et le code n'a pas besoin d'être compilé. Votre code est interprété ou lu ligne par ligne lorsque vous exécutez le programme.

Revenons à mon analogie de Chloe et John. John écrit un ensemble d'instructions sur la façon de faire un shepherd's pie. Le traducteur ne traduit pas les instructions de John à l'avance, mais les rejoint plutôt pour leur session de cuisine. Le traducteur traduit chaque ligne des instructions de John de l'anglais vers le français pendant que Chloe cuisine. À cause de cela, il faut plus de temps à Chloe pour préparer et cuisiner le repas.

Par conséquent, les langages interprétés sont plus lents que les langages compilés. Ils doivent être traduits à la volée pour que l'ordinateur puisse les comprendre.

Mais avec les compilateurs [just-in-time](https://blog.sessionstack.com/how-javascript-works-inside-the-v8-engine-5-tips-on-how-to-write-optimized-code-ac089e62b12e) (JIT), les langages interprétés deviennent plus rapides et plus efficaces.

## Quel(s) langage(s) de programmation devrais-je choisir d'apprendre ?

Les langages de programmation font à peu près la même chose, mais ils sont simplement différentes façons d'exprimer les mêmes instructions à un ordinateur. Une fois que vous avez saisi les concepts et les fondamentaux d'un langage de programmation, la courbe d'apprentissage pour apprendre un autre langage ne sera pas aussi raide.

Le langage de programmation que vous devriez choisir d'apprendre en premier dépend de plusieurs facteurs. Par exemple, je voulais devenir développeuse web, donc j'ai choisi JavaScript comme mon langage de programmation principal. D'autres langages pour le web que vous pouvez apprendre sont PHP et Ruby on Rails.

Si vous voulez devenir data scientist, alors Python pourrait être une option. Python est considéré comme l'un des meilleurs outils de data science pour analyser les [big data](https://en.wikipedia.org/wiki/Big_data). J'ai mentionné R plus tôt, qui est un autre langage largement utilisé parmi les data scientists et les statisticiens.

Python est un langage de programmation à usage général, et il est également utile à apprendre si vous voulez vous lancer dans le domaine du Machine Learning et de l'Intelligence Artificielle.

Si vous voulez devenir ingénieur logiciel, alors Java pourrait être une option. Java est l'un des langages les plus populaires et les plus demandés au monde. C'est un langage polyvalent qui peut être utilisé pour développer des logiciels d'entreprise de petite à grande taille.

Alors réfléchissez au type de rôle dans la tech que vous aimeriez et au type d'entreprises pour lesquelles vous voulez travailler.

Choisir un langage de programmation dépend également du type de logiciel que vous essayez de construire. Cela nous amène bien à notre prochaine section.

## Qu'est-ce qu'un logiciel ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_software_everywhere.png align="left")

Combien de fois interagissez-vous avec un logiciel dans une journée donnée ?

Les logiciels sont partout. Ils sont intégrés en tant que [systèmes embarqués](https://en.wikipedia.org/wiki/Embedded_system) dans des appareils du quotidien tels que votre micro-ondes, vos machines à laver, vos voitures, vos téléviseurs, les jouets de vos enfants et vos télécommandes. Ensuite, il y a des appareils informatiques plus évidents qui ont des logiciels [d'application](https://en.wikipedia.org/wiki/Application_software) et/ou [système](https://en.wikipedia.org/wiki/System_software) tels que les tablettes, les smartphones, les ordinateurs portables, les ordinateurs de bureau et les assistants domestiques comme Alexa.

La personne moyenne interagit probablement avec des logiciels plusieurs dizaines de fois par jour, sinon plus. Cela fait partie de notre vie quotidienne.

Tous les logiciels sont programmés par un développeur. Les logiciels sont agiles par nature et peuvent constamment évoluer. Les logiciels et le matériel sont étroitement liés. Imaginez votre téléphone sans ses applications et son système d'exploitation. Le téléphone serait essentiellement une brique coûteuse ! Par conséquent, les logiciels donnent vie au matériel et le matériel est la façon dont nous interagissons avec les logiciels.

La majorité des logiciels créés par les programmeurs sont écrits dans un langage de programmation de haut niveau.

### Qu'est-ce que le développement logiciel ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_software_development.png align="left")

Le [développement logiciel](https://en.wikipedia.org/wiki/Software_development) englobe tout, de la conception d'une idée à son développement et son déploiement. Ce processus, de la conception d'une idée au déploiement du logiciel, est également connu sous le nom de cycle de vie du logiciel.

Il existe plusieurs étapes du cycle de vie du logiciel : découverte, conception, programmation/création, test et déploiement/exécution. Il inclut également tout le reste dans l'écosystème du développement logiciel, tel que la maintenance, la documentation et les corrections de bugs.

Je ne vais pas entrer dans les détails ici, car le sujet du développement logiciel mérite son propre article.

## Tendances actuelles en développement logiciel et programmation informatique

### Intelligence artificielle et apprentissage automatique

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_machine_learning.png align="left")

Ces dernières années, vous avez probablement entendu parler de termes comme l'intelligence artificielle et l'apprentissage automatique. Parfois, ils sont utilisés de manière interchangeable, mais sont-ils identiques ?

Non, ils ne sont pas tout à fait la même chose. L'apprentissage automatique est un domaine où une machine apprend par l'expérience. Alors que l'intelligence artificielle est une idée plus large selon laquelle les machines peuvent exécuter des tâches de manière intelligente. L'apprentissage automatique est un sous-ensemble de l'intelligence artificielle.

### Qu'est-ce que l'intelligence artificielle ?

J'ai expliqué comment fonctionnent les langages de programmation – le programmeur écrit un ensemble d'instructions pour que l'ordinateur les exécute. L'intelligence artificielle (IA) est un concept plus large où les ordinateurs peuvent imiter le fonctionnement du cerveau. C'est entraîner une machine à « penser » comme un humain.

La grande question est : peut-on reproduire l'intelligence humaine dans une machine ? Peut-on imiter la manière dont un humain apprend, raisonne et perçoit ? Alan Turing a posé cette question dans son article en 1950 :

> *« Les machines peuvent-elles penser ? »*

([Machinerie informatique et intelligence](https://phil415.pbworks.com/f/TuringComputing.pdf), 1950 par Alan Turing)

Dans l'article de Turing, il a proposé le « test de Turing » dans lequel une machine serait classée comme « intelligente » si une personne ne pouvait pas faire la différence entre les réponses d'un humain et celles de la machine artificiellement intelligente.

Après 70 ans, les développeurs d'IA, les universitaires, les scientifiques et les chercheurs tentent toujours de répondre à cette question et de créer une machine artificiellement intelligente. Je ne pense pas que nous y soyons encore. Avez-vous essayé d'avoir une conversation avec Siri ou Alexa ? Les conversations avec ces deux appareils sont encore basiques. Cependant, je suis sûr que ce n'est qu'une question de temps avant que la technologie ne s'améliore.

Des entreprises comme [DeepMind](https://deepmind.com/) recherchent ce concept et si les machines sont capables d'intelligence. Le programme [AlphaGo](https://deepmind.com/research/case-studies/alphago-the-story-so-far) de DeepMind a fait les gros titres lorsqu'il a battu un joueur professionnel à Go. Ce fut une étape majeure pour l'IA.

### Qu'est-ce que l'apprentissage automatique ?

L'[apprentissage automatique](https://en.wikipedia.org/wiki/Machine_learning) (ML) est un sous-ensemble de l'intelligence artificielle. Le ML est une manière différente de programmer. C'est l'idée que l'ordinateur a la capacité d'apprendre sans être explicitement programmé. Arthur Samuel a eu l'idée de l'apprentissage automatique dans son [article](https://www.semanticscholar.org/paper/Some-Studies-in-Machine-Learning-Using-the-Game-of-Samuel/e9e6bb5f2a04ae30d8ecc9287f8b702eedd7b772) en 1959 :

> *« Programmer des ordinateurs pour qu'ils apprennent de l'expérience devrait éventuellement éliminer le besoin de beaucoup de cet effort de programmation détaillé. »*

Lorsque j'enseignais à mon fils à reconnaître un chat, je lui montrais des images de chats. Je l'ai fait à plusieurs reprises jusqu'à ce qu'il puisse reconnaître un chat sans que je le lui suggère.

L'apprentissage automatique est similaire à cela. Vous donnez à votre ordinateur cent images (entrée) de chats. Il apprend ensuite les motifs dans les données et construit un système de classification par répétition. Si vous donnez à votre ordinateur plus d'images de chats et d'autres animaux, il devrait être capable d'identifier si l'animal sur l'image est un chat ou non. Il a essentiellement appris à quoi devrait ressembler un chat.

Le ML consiste à donner des données et des exemples à votre ordinateur, et en retour, il est capable d'apprendre par lui-même comme le font les bébés et les jeunes enfants. Au lieu que les développeurs donnent les instructions à un ordinateur, l'ordinateur crée son propre ensemble d'instructions à suivre – les algorithmes d'apprentissage automatique. Les algorithmes d'apprentissage automatique sont un sous-ensemble du ML, un concept connu sous le nom de ["apprentissage profond"](https://en.wikipedia.org/wiki/Deep_learning).

> « L'IA est l'une des choses les plus profondes sur lesquelles nous travaillons en tant qu'humanité. C'est plus profond que le feu ou l'électricité... »

(Sundar Pichai, [Forum économique mondial](https://www.youtube.com/watch?v=sqd516M0Y5A), janvier 2020)

La citation de Sundar Pichai, le PDG d'Alphabet Inc, résume l'importance de l'IA et du ML.

## Quel est l'avenir de la programmation informatique ?

Cette dernière section sera mes prédictions sur l'avenir de la programmation informatique.

Les développeurs continueront à créer de nouveaux langages de programmation. Les langages de programmation deviendront plus abstraits et, par conséquent, accessibles aux individus apprenant à coder.

Je crois qu'il y aura une plus grande importance accordée à l'éducation en matière de codage et de programmation dans les programmes scolaires primaires et secondaires. La demande pour les développeurs et les programmeurs ne fera qu'augmenter à mesure que la technologie et les logiciels deviendront de plus en plus intégrés dans notre vie quotidienne. La programmation deviendra omniprésente.

Nous verrons la montée continue et la popularité du ML et de l'IA pour aider les développeurs dans le processus de développement logiciel. Cela inclut l'automatisation des tests, ainsi que la détection et la prévention des vulnérabilités et des bugs.

L'IA révolutionnera tous les aspects de notre société, pas seulement en programmation et en développement logiciel. Par exemple, nous avons vu de grandes avancées dans le domaine de l'IA et des voitures autonomes.

L'une des entreprises leaders mondiales dans le développement de voitures autonomes est [Tesla](https://www.tesla.com/), fondée par Elon Musk. Avec la supervision d'un conducteur humain, une voiture Tesla peut maintenant changer de voie automatiquement, naviguer de manière autonome sur des autoroutes à accès limité, et le propriétaire peut appeler la voiture à et depuis un garage ou une place de parking. L'objectif de Tesla est de créer une voiture entièrement automatisée et autonome sans aucune supervision humaine.

À mesure que les machines deviennent plus intelligentes, nous pourrions arriver à un point où les machines surpassent l'intelligence des êtres humains. Cela est appelé [singularité](https://en.wikipedia.org/wiki/Technological_singularity). Cela peut sembler de la science-fiction complète pour le moment ! Mais des figures notables comme [Ray Kurzweil](https://en.wikipedia.org/wiki/Ray_Kurzweil) prédisent que des machines avec une intelligence de niveau humain seront disponibles dans les 20 prochaines années. Kurzweil est connu pour ses prédictions précises sur la progression des technologies. Il a écrit un livre à ce sujet : [L'Ère des machines spirituelles](https://en.wikipedia.org/wiki/The_Age_of_Spiritual_Machines).

Comment notre société changera-t-elle à la suite de machines super intelligentes ?

## Mots de la fin

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_ending_illustration.png align="left")

La technologie influence et le code touche presque tous les aspects de notre vie. De notre choix de divertissement (jeux en ligne, streaming) et de la manière dont nous faisons nos achats, à ce que nous mangeons et même comment nous sortons ! Le code est important et de plus en plus d'emplois nécessiteront que les gens aient au moins une compréhension de base de la programmation.

Pourtant, il n'y a qu'environ 23,9 millions de développeurs dans le monde selon l'étude [Global Developer Population and Demographic study 2019](https://evansdata.com/reports/viewRelease.php?reportID=9). Pour mettre cela en perspective, seulement **0,3%** de la population mondiale sait programmer. Comme je l'ai discuté plus tôt, notre dépendance aux logiciels et à la technologie augmente. Selon le [US Bureau of Labor statistics](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm#tab-6), la demande pour les ingénieurs logiciels devrait croître de 21% de 2018 à 2028. Par conséquent, nous devons augmenter le nombre de développeurs.

Si vous envisagez de devenir développeur, commencez dès aujourd'hui. C'est un moment incroyablement excitant pour le faire ! Il existe de nombreuses ressources en ligne pour apprendre à coder. Il y a des plateformes auto-rythmées comme [freeCodeCamp](https://www.freecodecamp.org/). Il y a aussi un excellent [article de Laurence Bradford](https://learntocodewith.me/posts/code-for-free/) qui compile toutes les meilleures ressources pour apprendre à coder gratuitement. Faites quelques recherches et découvrez quelle ressource convient à votre style d'apprentissage.

Si vous avez des questions ou si vous voulez simplement dire bonjour, trouvez-moi sur Twitter [@PhoebeVF](https://twitter.com/PhoebeVF).

*Un remerciement spécial à Katerina Limpitsouni de* [*Undraw*](https://undraw.co/) *pour avoir créé les illustrations de cet article.*