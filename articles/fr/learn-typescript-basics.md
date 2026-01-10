---
title: Apprendre les bases de TypeScript dans ce guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-04T18:01:00.000Z'
originalURL: https://freecodecamp.org/news/learn-typescript-basics
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Typescript-Getting-Started.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Apprendre les bases de TypeScript dans ce guide pour débutants
seo_desc: 'By Joel P. Mugalu

  TypeScript has taken the development world by storm. No wonder it has over 15 million
  weekly downloads on npm. But what is TypeScript, and what do you need to know about
  it?

  In this article, I am going answer those questions. By the...'
---

Par Joel P. Mugalu

TypeScript a conquis le monde du développement. Pas étonnant qu'il compte plus de 15 millions de téléchargements hebdomadaires sur npm. Mais qu'est-ce que TypeScript, et que devez-vous savoir à son sujet ?

Dans cet article, je vais répondre à ces questions. À la fin, vous aurez une compréhension des éléments suivants :

- Qu'est-ce que TypeScript
- Les piliers principaux de TypeScript
- Les fonctionnalités principales de TypeScript
- Pourquoi vous devriez utiliser TypeScript
- Les bases de TypeScript pour bien démarrer

Commençons par aborder l'éléphant dans la pièce.

## Qu'est-ce que TypeScript ?
TypeScript est un langage de programmation développé et maintenu par Microsoft.
C'est un sur-ensemble de JavaScript qui ajoute une vérification forte des types et est compilé en code JavaScript simple.

Être un sur-ensemble signifie que TypeScript possède toutes les fonctionnalités de JavaScript ainsi que certaines fonctionnalités supplémentaires.

TypeScript offre des fonctionnalités telles qu'un meilleur outil de développement, une analyse statique du code, une vérification des types au moment de la compilation et une documentation au niveau du code.

Ne vous inquiétez pas si vous ne savez pas ce que tout cela signifie. Je vais tout expliquer dans cet article.

Toutes ces fonctionnalités qui accompagnent TypeScript en font le langage de programmation parfait pour construire des applications JavaScript à grande échelle.

## Piliers principaux de TypeScript
TypeScript est construit sur trois piliers principaux – à savoir le langage, le compilateur et le service de langage.

### Langage TypeScript
Cela comprend la syntaxe, les mots-clés et les annotations de type de TypeScript.
La syntaxe TypeScript est similaire mais pas identique à la syntaxe JavaScript.

### Compilateur TypeScript
Le compilateur est responsable de la compilation du code TypeScript en JavaScript.
En réalité, ce qui se passe n'est pas vraiment de la compilation mais de la transpilation.

> La compilation signifie que le code source est transformé d'un format lisible par l'homme à un format lisible par la machine, tandis que la transpilation est la transformation du code source d'un format lisible par l'homme à un autre format lisible par l'homme.

Le compilateur TypeScript est également responsable de l'effacement de toute information liée aux types au moment de la compilation.

Les types ne sont pas des fonctionnalités valides en JavaScript. Et puisque TypeScript doit être compilé en JavaScript simple, tout ce qui est lié aux types doit être effacé avant de pouvoir devenir du JavaScript valide prêt à être exécuté par le navigateur.

Le compilateur TypeScript effectue également une analyse de code. Il émet des erreurs et des avertissements s'il y a lieu de le faire.

### Service de langage
Le service de langage est responsable de la collecte des informations de type à partir du code source.

Ces informations peuvent ensuite être utilisées par les outils de développement pour fournir IntelliSense, des indices de type et des alternatives de refactorisation.

## Fonctionnalités principales de TypeScript

### Annotations de type dans TypeScript
L'annotation de type signifie simplement attribuer un type à une variable ou à une fonction.

```js
const birthdayGreeter = (name: string, age: number): string => {
  return `Happy birthday ${name}, you are now ${age} years old!`;
};

const birthdayHero = "Jane User";
const age = 22;
console.log(birthdayGreeter(birthdayHero, 22));
```

Dans l'exemple ci-dessus, nous définissons une fonction qui accepte deux paramètres `name` et `age`. Nous attribuons `name` au type _string_ et `age` au type _number_.

Nous pouvons également attribuer des types à la valeur de retour d'une fonction. Dans ce cas, notre fonction retourne une valeur de type _string_.

```js
const birthdayGreeter = (name: string, age: number): string => { };
TypeScript générerait une erreur si nous passions des arguments de types différents de ceux que nous attendons.
```

### Typage structurel dans TypeScript
TypeScript est un langage à typage structurel, ce qui signifie que si deux éléments ont des caractéristiques correspondantes et identiques, ils sont considérés comme étant du même type.

### Inférence de type dans TypeScript
Le compilateur TypeScript peut tenter d'inférer les informations de type s'il n'y a pas de type spécifique attribué. Cela signifie que TypeScript peut attribuer un type à une variable ou à une fonction en fonction de ses valeurs initiales ou de son utilisation.

L'inférence de type se produit généralement lorsque vous initialisez des variables, définissez des valeurs par défaut et déterminez les types de retour des fonctions.

```js
const platform = 'freeCodeCamp';
const add = (a: number, b: number) => a + b
```

La variable platform dans l'exemple ci-dessus se voit attribuer le type _string_ même si nous ne l'avons pas fait explicitement et la valeur de retour de la fonction `add` est inférée comme étant de type _number_.

### Effacement de type dans TypeScript
TypeScript supprime les constructions du système de types pendant la compilation :

Entrée
```js
let x: someType;
```

Sortie
```js
let x;
```

## Pourquoi utiliser TypeScript ?

### Vérification des types et analyse statique du code

Cela réduit les erreurs globales dans votre code car TS vous avertira lorsque vous utiliserez incorrectement un certain type.

Cela réduit également les erreurs d'exécution et, grâce à l'analyse statique du code, TypeScript émettra des avertissements concernant les fautes de frappe et autres. Donc, cela signifie moins d'erreurs, ce qui pourrait potentiellement signifier moins de tests.

### Les annotations de type peuvent agir comme une documentation de code

Les annotations de type nous aident à comprendre quel type d'arguments une fonction attend, par exemple, et ce qu'elle retourne.

Cela rend le code plus lisible et facilite la compréhension pour les autres et pour nous-mêmes de ce que le code est censé faire.

Un autre avantage de TypeScript est que les IDE peuvent fournir des suggestions IntelliSense plus spécifiques et plus intelligentes lorsqu'ils savent exactement quels types de données vous traitez.

## Comment commencer avec TypeScript
Commençons par installer le package TypeScript. Ici, nous avons deux options : nous pouvons soit l'installer globalement pour l'utiliser sur n'importe quel projet du système, soit l'installer pour l'utiliser sur le projet spécifique sur lequel nous travaillons.

Vous pouvez installer TypeScript globalement en exécutant cette commande :
```shell
npm install -g typescript
```

Si vous ne souhaitez pas installer globalement, vous pouvez simplement exécuter ceci :
```js
npm install --save-dev typescript 
```

Dans le cas d'une installation locale, TypeScript est installé comme une dépendance de développement car nous l'utilisons pour le développement. Il doit d'abord être compilé en JavaScript avant de pouvoir être utilisé en production. Le navigateur ne peut pas exécuter TypeScript.

Après avoir installé TypeScript, nous devons initier un nouveau projet. Vous pouvez le faire en exécutant la commande suivante :
```shell
tsc --init
```

Cette commande initie un nouveau fichier _tsconfig.json_ dans le répertoire racine du projet. Ce fichier de configuration contient toutes les options de configuration dont nous disposons pour utiliser TypeScript dans un projet.

![un exemple de fichier tsconfig](https://www.freecodecamp.org/news/content/images/2021/05/image1-1.png)

Toutes les options de compilation pour un projet particulier peuvent être spécifiées dans le fichier tsconfig.json sous la clé _compileOptions_.

Le fichier contient certaines options de configuration par défaut, mais vous pouvez ajouter plus d'options au projet selon vos besoins. Vous pouvez commenter ou supprimer les options de compilateur inutilisées.

### Types intégrés dans TypeScript
TypeScript est livré avec tous les types primitifs de JavaScript comme string, number et boolean.

Les types peuvent ensuite être attribués à des variables pour spécifier quel type de données doit être attribué à la variable. Cela s'appelle l'annotation de type.

```js
const myName: string = 'Joel';
const myAge: number = 99;
```

Les annotations TypeScript ne sont pas toujours nécessaires car TypeScript infère automatiquement le type d'une variable en fonction de sa valeur initiale ou de son utilisation. Par conséquent, ce qui suit serait également un code TypeScript valide :

```js
// myName est inféré de type 'string'
 const myName = 'Jonathan';
```

### Tableaux dans TypeScript
Pour spécifier le type d'un tableau, vous pouvez utiliser la syntaxe `string[]` ou `number[]`. Cela signifie effectivement 'tableau de chaînes' ou 'tableau de nombres'.

Vous verrez également des personnes utiliser la syntaxe `Array<number>` ou `Array<string>` qui signifie la même chose.

### Types d'union dans TypeScript
Les types d'union nous permettent de définir plusieurs types qui peuvent être attribués à une variable. Pour cela, nous utilisons un pipe | pour spécifier les différents types.

```js
const someValue: number | string = value; 
```

Par défaut, `null | undefined` peut être attribué à n'importe quelle variable, mais TypeScript dispose de l'option de compilateur _strictNullChecks_ qui n'autorise pas l'attribution des deux à une variable.

### Fonctions dans TypeScript
Les fonctions peuvent également recevoir des annotations de type. Cependant, avec les fonctions TypeScript, elles ne peuvent recevoir que les paramètres spécifiés. Ni plus ni moins.

```js
function introduction(name: string, age: number): string {
    return `Hello, my name is ${name} and I'm {age} years old`
}
```

Les paramètres de fonction reçoivent une annotation de type normale.

Les fonctions TypeScript doivent également spécifier le type de données de retour. Dans le cas où une fonction ne retourne rien, nous pouvons utiliser le type _void_ comme type de données de retour.

Nous pouvons également utiliser l'opérateur `?` pour spécifier **des paramètres qui sont optionnels**. Dans ce cas, TypeScript ne se plaindra pas si le paramètre n'est pas passé lors de l'appel de la fonction.

Nous pouvons également attribuer des valeurs par défaut aux paramètres, comme nous le ferions en JavaScript normal.

```js
const introduction = (name: string, age: number, job?: string = 'developer'): string => `Hello, my name is ${name} and I'm ${age} years old. I work as a ${job}`
```

Remarquez que dans cet exemple, j'ai utilisé la syntaxe de la [fonction fléchée](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) JavaScript et j'ai spécifié que le paramètre job est optionnel et je lui ai attribué une valeur par défaut 'developer'.

### Le type `any` dans TypeScript
Dans TypeScript, chaque variable dont le type ne peut pas être inféré devient implicitement du type _any_.

`Any` est typiquement un type joker qui signifie littéralement 'n'importe quel type'. Nous pouvons également attribuer explicitement le type _any_ à une variable.

Cependant, les typages `any` sont généralement considérés comme problématiques.

TypeScript dispose de l'option de compilateur _noImplicitAny_ qui génère une erreur lorsque nous attribuons le type _any_ à une variable ou à une expression.

### Comment créer vos propres types dans TypeScript
TypeScript offre un moyen de définir et d'utiliser nos propres types pour les entrées. Ici, nous pouvons décrire le type exact qui est acceptable pour une entrée particulière.

Nous pouvons utiliser le mot-clé `type` pour définir nos propres types.

```js
type Operator = 'multiply' | 'add' | 'divide'; 
```

Maintenant, le type `Operator` peut accepter l'une des valeurs. Remarquez comment nous utilisons l'opérateur OR `|` pour créer un type d'union. Dans ce cas, toute variable à laquelle le type Operator est attribué peut accepter l'une des trois valeurs.

## Projet d'exemple TypeScript

Utilisons maintenant cette connaissance pour créer un simple programme de calculatrice. Un utilisateur ne peut entrer qu'une des trois opérations - add, multiply ou divide. Si vous le souhaitez, prenez un moment et essayez de le faire, puis revenez et suivez le guide.

Espérons que vous l'avez essayé par vous-même. Le programme pourrait alors ressembler à ceci :
```js
type Operation = 'multiply' | 'add' | 'divide';

const calculator = (a: number, b:number, op: Operation): number => {
    switch(op) {
        case 'multiply':
            return a * b;
        case 'add':
            return a + b;
        case 'divide': 
            if (b === 0) return 'Can't divide by 0;
            return a / b;
        default:
        return 'Operation unknow';          
    }
}
```

Essayez de lire le code ci-dessus et voyez si vous pouvez comprendre ce qui se passe.

Nous pouvons également créer des types personnalisés en utilisant le mot-clé `interface`. Les interfaces nous permettent de définir les propriétés et le type d'un objet. Une interface peut avoir la capacité d'étendre une autre interface.

```js
interface Employee {
    name: string,
    title: string
}

interface Manager extends Employee {
    meeting: (topic: string) => void
}
```

Ici, nous définissons une interface Employee qui a deux propriétés - `name` et `title`, toutes deux de type _string_.

Nous utilisons ensuite cette interface pour créer une autre interface `Manager` qui a les mêmes propriétés que l'interface Employee mais avec une méthode meeting.

Au début, j'ai mentionné que TypeScript est un langage à typage structurel. Cela signifie que si un élément a les mêmes propriétés qu'un autre, ils sont tous deux du même type.

Il en va de même pour les interfaces. Si un objet a les propriétés d'une interface, alors il a le type de l'interface. Un tel objet peut avoir des propriétés supplémentaires tant que certaines propriétés correspondent à celles de l'interface.

Nous pouvons maintenant utiliser notre interface définie comme suit :

```js
const newEmployee: Employee = {
    name: 'Joel',
    title: 'FrontEnd Developer'
}
```

Jusqu'à présent, nous avons vu que nous pouvons créer nos propres types en utilisant les mots-clés _type_ et _interface_. Mais, quelle est la différence entre les deux ?

La différence la plus notable est que la définition de plusieurs interfaces avec le même nom entraînera une interface fusionnée. En revanche, la définition de plusieurs types avec le même nom entraînera une erreur indiquant que le nom est déjà déclaré.

## Conclusion
TypeScript possède de nombreuses fonctionnalités qui ne peuvent pas être épuisées dans cet article. J'ai simplement mis en évidence quelques-unes des fonctionnalités qui peuvent être utiles à comprendre pour commencer à travailler avec lui.

Vous pouvez en apprendre davantage sur TypeScript en lisant la [documentation](https://www.typescriptlang.org/docs/).

Si vous avez aimé cet article, envisagez de me suivre sur [Twitter](https://twitter.com/codingknite) ou de vous connecter avec moi sur [LinkedIn](https://linkedin.com/in/codingknite). Je partage du contenu sur la programmation et ce que j'apprends. N'hésitez pas à entrer en contact.