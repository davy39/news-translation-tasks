---
title: Comment installer et commencer à utiliser TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T08:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-and-begin-using-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/florian-klauer-mk7D-4UCfmg-unsplash-4.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: TypeScript
  slug: typescript
seo_title: Comment installer et commencer à utiliser TypeScript
seo_desc: 'By Jonathan Sexton

  TypeScript is one of the current hot topics in web development, and for good reasons.

  It allows us to type cast when declaring variables which means we explicitly set
  the type of data we expect back. Then it throws errors if the re...'
---

Par Jonathan Sexton

TypeScript est l'un des sujets brulants actuels dans le développement web, et pour de bonnes raisons.

Il nous permet de typer les variables lors de leur déclaration, ce qui signifie que nous définissons explicitement le type de données que nous attendons. Ensuite, il génère des erreurs si les données retournées ne sont pas du type que nous attendions, ou si un appel de fonction a trop peu ou trop d'arguments. Et ce n'est qu'un échantillon de tout ce qu'il offre.

Si vous souhaitez un aperçu des types de données, vous trouverez utile de lire mon [article précédent](https://jonathansexton.me/blog/learn-typescript-data-types-from-zero-to-hero/). La lecture de cet article n'est pas obligatoire, mais elle vous donnera une excellente compréhension des types de données et de la syntaxe pour TypeScript.

_Avant de commencer, il est important de noter que TypeScript peut être utilisé en conjonction avec un framework/bibliothèque, mais il peut également être utilisé indépendamment d'un framework/bibliothèque. TypeScript est le choix par défaut dans les projets Angular et j'ai un article en préparation sur la prise en main de celui-ci._

_De plus, cet article suppose que vous avez une compréhension de base de la programmation JavaScript._

Alors, maintenant nous sommes prêts à commencer avec TypeScript et à commencer à utiliser ses fonctionnalités géniales.

Commençons !

## Installation de TypeScript

Il existe deux principales façons d'installer TypeScript. La première est via [Visual Studio](https://visualstudio.microsoft.com/vs/) (à ne pas confondre avec [Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=DX_841432)) qui est un [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment). Les versions 2015, 2017 et je crois 2019 viennent avec TypeScript déjà installé.

Ce n'est pas la méthode que je couvrirai aujourd'hui puisque j'utilise principalement Visual Studio Code pour tous mes besoins.

La deuxième façon, et celle sur laquelle nous nous concentrerons, est via [NPM](https://www.npmjs.com/get-npm) (Node Package Manager).

Si vous n'avez pas déjà NPM et/ou [Node](https://nodejs.org/en/) installé (vous obtenez NPM lorsque vous installez Node), c'est le moment idéal pour le faire car c'est une exigence pour les étapes suivantes (et par association une exigence pour utiliser TypeScript).

![la page de téléchargement de node js](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-1-1024x550.png)
_La page de téléchargement de Node - il est judicieux d'utiliser la version LTS car elle est la plus stable_

Une fois que vous avez Node et NPM installés, ouvrez votre terminal dans VS Code et exécutez la commande suivante :

`npm install -g typescript`

Une fois l'installation terminée, vous verrez qu'un package a été ajouté. Vous verrez également un message indiquant la version de TypeScript qui a été installée.

C'est tout ce dont vous avez besoin pour commencer à compiler TypeScript en JavaScript.

Vous êtes maintenant prêt à commencer à écrire en TypeScript !

## Démarrer un projet TypeScript

Créons un projet TypeScript afin de pouvoir tirer parti de toutes ces excellentes fonctionnalités qui l'accompagnent.

Dans l'éditeur de votre choix (j'utilise VS Code), créons un fichier HTML pour être le côté visuel de notre code. Voici à quoi ressemble mon fichier HTML de base :

![texte html sur un fond sombre](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-2-1024x376.png)
_Balises HTML de base avec un texte de remplissage_

Honnetement, nous utilisons simplement ce HTML pour avoir quelque chose à regarder sur la page. Ce qui nous intéresse vraiment, c'est d'utiliser la console.

Vous remarquerez que j'ai lié `app.js` dans l'en-tête de notre fichier `index.html`.

Vous vous dites probablement _Je pensais que c'était un article sur TypeScript ?_

Eh bien, patience, c'en est un. Je veux simplement souligner certaines des différences entre JavaScript et TypeScript (Vous apprendrez d'où vient ce fichier plus bas).

Ci-dessous, vous verrez une simple déclaration de variable et une instruction de journalisation de la console :

![code javascript montrant une déclaration de variable de nom d'utilisateur](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-4.png)
_Une simple déclaration de variable et une instruction de journalisation de la console_

En tant que note à part, si vous souhaitez désactiver certaines règles [ES-Lint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint), vous pouvez placer les règles en haut en commentaires comme je l'ai fait ci-dessus. Ou si vous souhaitez **complètement** désactiver ES-Lint pour ce fichier uniquement, vous pouvez placer `/* eslint-disable */` en haut du fichier.

Et voici la console du navigateur :

![la console à l'intérieur du navigateur firefox](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-5.png)
_Notre variable userName à l'intérieur de FireFox_

Supposons que je construise une application et que pour `userName`, je m'attends toujours à obtenir une chaîne de caractères. En cours de route, je peux faire une erreur ou mes données peuvent être mutées par une autre source.

Maintenant, `userName` est un nombre :(

![code javascript montrant une déclaration de variable de nom d'utilisateur](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-6.png)
_Maintenant userName est un nombre !_

Et voici la console du navigateur montrant les changements de `userName` que nous ne voulions probablement pas voir se produire si cela était une application de production :

![Image](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-7.png)
_La console FireFox montrant les résultats de la mutation de la variable_

Et si le `userName` retourné était ensuite passé à une autre fonction ou utilisé comme une pièce d'un puzzle de données plus grand ?

Non seulement ce serait un désordre de déterminer où la mutation s'est produite (surtout si nous avions une application plus grande), mais cela créerait également un nombre incalculable de bugs dans notre code.

Maintenant, essayons la même expérience en TypeScript. Pour cela, nous devons créer un nouveau fichier avec l'extension `.ts` pour désigner un fichier TypeScript.

Je nommerai le mien `app.ts` pour rester cohérent avec les conventions de nommage et je mettrai le même code de notre fichier JavaScript dans notre nouveau fichier TypeScript.

![code typescript sur un fond sombre](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-8.png)
_Le même code de notre JavaScript copié dans le fichier TypeScript_

Vous remarquerez que j'utilise le typage lors de la déclaration de ma variable maintenant, et je dis explicitement à TypeScript que cette variable doit pointer vers une valeur de chaîne uniquement.

Vous remarquerez également que j'ai une ligne d'erreur sous `userName` lorsque je réassigne sa valeur.

## Compilation de TypeScript avec la CLI

Pour voir à quoi cela ressemble dans notre console, nous devons le compiler en JavaScript. Nous faisons cela en exécutant `tsc app.ts` dans notre console VS Code (vous pouvez également exécuter la même commande dans n'importe quel terminal tant que vous êtes dans le bon répertoire).

Lorsque nous exécutons cette commande, elle compilera notre TypeScript en JavaScript. Elle générera également un autre fichier avec le même nom, mais avec une extension `.js`.

C'est d'où vient ce fichier `app.js` dont j'ai parlé plus tôt dans l'article.

Pour compiler plusieurs fichiers à la fois, il suffit de fournir ces noms dans votre commande, l'un après l'autre : `tsc app.ts header.component.ts`

Il est également possible de compiler plusieurs fichiers TypeScript en un seul fichier JavaScript en ajoutant le flag `--out` :

`tsc *.ts --out index.js`

Il existe également une commande de surveillance qui recompilera automatiquement tout le TypeScript chaque fois qu'un changement est détecté. Cela vous évite d'avoir à exécuter la même commande encore et encore :

`tsc *.ts --out app.js --watch`

Voici le résultat de cette commande `tsc app.ts` ci-dessus :

![Image](https://jonathansexton.me/blog/wp-content/uploads/2019/12/image-9-1024x408.png)
_L'erreur dans ma console_

Cette erreur nous indique qu'il y a un problème avec la réassignation de `userName`. Parce que nous avons explicitement défini notre variable comme étant une chaîne de caractères (_même si je n'avais pas défini la variable comme une chaîne de caractères, l'erreur se produirait toujours car TypeScript infère les types de données_), nous ne pouvons pas la réassigner à un nombre.

C'est une excellente fonctionnalité car elle nous oblige à être explicites avec nos déclarations de variables et nous évite de faire des erreurs qui pourraient s'avérer ennuyeuses et chronophages. Si vous attendez un type de données particulier, vous devriez obtenir ces données, sinon vous devriez obtenir une erreur.

## Utilisation de tableaux et d'objets explicitement déclaratifs

Supposons que je construise un projet et que, au lieu de définir manuellement les liens de navigation, je souhaite stocker ces informations dans un tableau d'objets.

Je m'attendrai à un format spécifique pour les informations qui sont stockées afin qu'elles soient cohérentes pour tous les liens.

Voici comment je peux définir un tableau "complexe" en TypeScript :

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-1-1024x51.png)
_Un tableau avec un format spécifique_

Du côté gauche, nous déclarons le nom de la variable `navLinks`, suivi d'un deux-points. Aux accolades, nous commençons à déclarer le format des informations que nous attendons dans ce tableau.

Nous disons à TypeScript que nous attendons de ce tableau qu'il contienne un objet ou des objets avec ces noms et types de propriétés. Nous attendons un `name` qui est une chaîne de caractères, un `link` qui est une chaîne de caractères, et un `alt` qui est également une chaîne de caractères.

Comme pour les autres [types de données](https://jonathansexton.me/blog/learn-typescript-data-types-from-zero-to-hero/), si nous nous écartons du format que nous avons établi pour cette variable, nous rencontrons des erreurs.

Ici, nous avons essayé d'ajouter une nouvelle entrée qui était vide et nous avons obtenu l'erreur suivante :

`Type '{}' is missing the following properties from type '{ name: string; link: string; alt: string; }' : name, link, <sub>alt ts(2739)</sub>`

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-3-1024x97.png)

Nous obtenons des erreurs similaires si nous essayons d'ajouter une autre entrée avec le mauvais type d'informations :

`{ name: 'Jonathan', link: 15, alt: false }`  F534

`{ name: ['Jon','Marley'], link: `https://link123.net`, alt: null }`  F534

`this.navLinks[0].img = '../../assets/img'` F534

`this.navLinks[0].name = 'Barnaby'`F534F3FF

Vous voyez l'idée. Une fois que nous avons établi le format, TypeScript nous tiendra à ce format et nous informera si/quand nous nous en écartons avec une erreur.

De plus, voici quelques façons de définir un tableau :

`const arr1: Array<any> = ['Dave', 35, true];` _// nous permettra d'avoir n'importe quel nombre d'éléments de n'importe quel type_

`const people: [string,string,string] = ['John', 'Sammy', 'Stephanie'];` _// générera une erreur si plus de 3 chaînes ou des éléments non chaînés apparaissent dans le tableau_

`const people: Array<string> = ['Jimmy', 'Theresa', 'Stanley'];` _// nous permettra d'avoir n'importe quel nombre d'éléments uniquement de type chaîne dans notre tableau_

Les objets fonctionnent de la même manière que les tableaux en TypeScript. Ils peuvent être explicitement définis avec des types fixes ou vous pouvez laisser TypeScript faire toutes les inférences. Voici un exemple de base d'un objet :

`const person: {name:string, address: string, age: number} = {name: 'Willy', address: '123 Sunshine Ln', age: 35}`

Encore une fois, du côté gauche, nous déclarons person comme nom de variable avec le premier ensemble d'accolades définissant le format dans lequel nous voulons que nos données soient.

Il est important de noter que dans les objets, l'ordre dans lequel nous définissons nos propriétés n'a pas besoin de correspondre à l'ordre du format :

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-5.png)
_Les propriétés n'ont pas besoin de correspondre à l'ordre dans lequel elles ont été définies_

## Fonctions, paramètres et arguments

Certains des plus grands avantages que vous verrez dans TypeScript viennent lors de l'utilisation de fonctions.

Avez-vous déjà construit une fonction pour effectuer une tâche spécifique, seulement pour découvrir qu'elle ne fonctionne pas comme vous l'aviez prévu ?

En utilisant TypeScript, ce ne sera pas parce que vous n'avez pas obtenu/envoyé le bon type de données ou utilisé le bon nombre de paramètres/arguments.

Voici un excellent exemple :

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-1024x454.png)
_Une fonction TypeScript qui devrait retourner un nombre_

Dans notre fonction, nous nous attendons à recevoir 3 arguments lorsque `calculator` s'exécute. Cependant, si nous recevons le mauvais nombre d'arguments (trop peu ou trop), TypeScript nous donnera une belle erreur :

![Image](https://jonathansexton.me/blog/wp-content/uploads/2020/01/image-4.png)
_L'erreur que nous obtenons lors de l'appel d'une fonction avec le nombre/type incorrect d'arguments_

De même, si nous recevons le mauvais type de données lors de l'exécution de cette fonction, TypeScript générera une erreur et la fonction ne s'exécutera pas.

`calculator('12', '11', 'add) ;` F534

Maintenant, vous vous dites peut-être _'Et alors ? C'est bien et bon, mais cela ne semble pas être un gros problème.'_ Mais imaginez que votre application est composée de dizaines et dizaines de fichiers avec de nombreuses couches d'abstractions.

Un excellent exemple de cela serait une application Angular avec des services, des modèles de données, des composants multiniveaux, et toutes les dépendances qui vont avec. Il devient de plus en plus difficile de localiser d'où provient une erreur lorsque votre application devient grande.

## C'est tout

Espérons que vous pouvez maintenant voir les avantages de TypeScript. Il y en a beaucoup plus que ceux que j'ai décrits ici et je vous encourage à lire la documentation si vous souhaitez en découvrir davantage.

Vous pouvez trouver cet article et d'autres similaires sur mon [blog](https://jonathansexton.me/blog). J'aimerais que vous passiez me voir !

Pendant que vous y êtes, pourquoi ne pas vous inscrire à ma **Newsletter** – vous pouvez le faire en haut à droite de la page principale du blog. Je promets de ne jamais spammer votre boîte de réception et vos informations ne seront pas partagées avec qui que ce soit/site. J'aime occasionnellement envoyer des ressources intéressantes que je trouve, des articles sur le développement web, et une liste de mes nouveaux articles.

Si vous ne l'avez pas encore fait, vous pouvez également me suivre sur les réseaux sociaux ! Tous mes liens sont également en haut à droite de cette page. J'aime me connecter avec les autres et rencontrer de nouvelles personnes, alors n'hésitez pas à dire bonjour. 😊

Passez une excellente journée, ami, et bon codage !