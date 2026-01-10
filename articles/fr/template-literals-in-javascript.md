---
title: Comment utiliser les littéraux de gabarit en JavaScript
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-05T18:30:18.000Z'
originalURL: https://freecodecamp.org/news/template-literals-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/JavaScript-template-literal
seo_title: Comment utiliser les littéraux de gabarit en JavaScript
---

freecodecamp.png
étiquettes:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Développement Web
  slug: developpement-web
seo_title: null
seo_desc: 'Les littéraux de gabarit sont une fonctionnalité en JavaScript qui ont été introduits avec ES6. Ils vous offrent une manière plus flexible et maintenable de travailler avec des chaînes de caractères en JavaScript.

À la fin de cet article, vous saurez comment utiliser les littéraux de gabarit. Vous apprendrez la syntaxe, les avantages et quelques cas d\'utilisation. Et vous apprendrez également une fonctionnalité encore plus puissante appelée littéraux de gabarit étiquetés.
---

Les littéraux de gabarit sont une fonctionnalité en JavaScript qui ont été introduits avec ES6. Ils vous offrent une manière plus flexible et maintenable de travailler avec des chaînes de caractères en JavaScript.

À la fin de cet article, vous saurez comment utiliser les littéraux de gabarit. Vous apprendrez la syntaxe, les avantages et quelques cas d\'utilisation. Et vous apprendrez également une fonctionnalité encore plus puissante appelée littéraux de gabarit étiquetés.

## Table des matières

* [Qu\'est-ce que les littéraux de gabarit ?](#quest-ce-que-les-litteraux-de-gabarit)
    
* [Littéraux de gabarit vs chaînes de caractères régulières](#litteraux-de-gabarit-vs-chaines-de-caracteres-regulieres)
    
* [Quelques cas d\'utilisation des littéraux de gabarit](#quelques-cas-dutilisation-des-litteraux-de-gabarit)
    
* [Littéraux de gabarit étiquetés](#litteraux-de-gabarit-etiquetés)
    
* [Exemples de littéraux de gabarit étiquetés](#exemples-de-litteraux-de-gabarit-etiquetés)
    
* [Conclusion](#conclusion)
    

## Qu\'est-ce que les littéraux de gabarit ?

Les littéraux de gabarit sont une fonctionnalité en JavaScript qui permettent aux développeurs de travailler avec des chaînes de caractères de manière pratique. Vous dénotez les chaînes de caractères régulières en JavaScript en utilisant des guillemets doubles `""` ou des guillemets simples `''`.

Mais avec les littéraux de gabarit, vous dénotez les chaînes de caractères en utilisant des backticks \`\`\`\`. Cela vous permet d\'intégrer des variables et des expressions dans vos chaînes de caractères.

Voici un exemple :

```javascript
const website = 'freeCodeCamp'
const message = `Bienvenue sur ${website}`

console.log(message)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-03-at-6.57.20-AM.png align="left")

*Sortie de l\'exemple de littéral de gabarit.*

La valeur de la variable `message` est un exemple de littéral de gabarit. Il inclut des backticks qui sont utilisés pour définir le littéral de gabarit. Et il inclut également la syntaxe `${}` qui est utilisée pour intégrer des variables dans la chaîne de caractères.

## Littéraux de gabarit vs chaînes de caractères régulières

Examinons maintenant comment les littéraux de gabarit diffèrent des chaînes de caractères régulières et aussi quelques avantages de l\'utilisation des littéraux de gabarit.

### Concaténation de chaînes

Avant l\'introduction des littéraux de gabarit, vous deviez utiliser le symbole plus `+` lorsque vous vouliez concaténer des chaînes.

```javascript
const userName = 'Marie'
const balance = 10

// Utilisation de chaîne régulière
const str1 = 'Bonjour ' + userName + ',' + ' votre solde est ' + balance + '.'
console.log("Chaîne régulière : ", str1)

// Utilisation de littéral de gabarit
const str2 = `Bonjour ${userName}, votre solde est ${balance}.`
console.log("Littéral de gabarit : ", str2)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-03-at-7.07.37-AM.png align="left")

*La chaîne régulière et le littéral de gabarit produisent la même sortie pour l\'exemple.*

Remarquez comment l\'utilisation de chaînes régulières implique l\'ajout de nombreux signes plus. Et aussi la prise en compte des espaces blancs aux bons endroits. Cela peut devenir difficile à gérer lorsque vous travaillez avec des chaînes de caractères longues.

Avec l\'exemple de littéral de gabarit, il n\'a pas été nécessaire d\'ajouter de signes plus. Vous écrivez tout ensemble comme une seule chaîne. Les variables sont directement intégrées en utilisant la syntaxe `${}`.

### Chaînes multi-lignes

Une autre manière dont les littéraux de gabarit facilitent le travail avec les chaînes de caractères est lorsqu\'il s\'agit de chaînes multi-lignes. Pour les chaînes régulières, vous devez utiliser une combinaison du signe plus `+` et de `\n` pour désigner une nouvelle ligne. Mais les littéraux de gabarit n\'exigent rien de tout cela.

```javascript
const regularString = 
'Bonjour ! \n' +
'Bienvenue sur notre site web. \n' +
'Comment pouvons-nous vous aider aujourd\'hui ?'

const templateLiteral = 
`Bonjour !
Bienvenue sur notre site web.
Comment pouvons-nous vous aider aujourd\'hui ?`

console.log(regularString)
console.log(templateLiteral)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-03-at-7.44.20-AM.png align="left")

*Exemples de chaînes multi-lignes pour chaîne régulière et littéral de gabarit.*

Les variables `regularString` et `templateLiteral` donnent la même sortie. Le littéral de gabarit reconnaît automatiquement les espaces blancs et les sauts de ligne.

### Lisibilité et maintenabilité

Les littéraux de gabarit rendent également votre code plus lisible et plus facile à maintenir. Comme vous l\'avez déjà vu, ils ne nécessitent aucune concaténation avec le signe plus `+`. Et vous n\'avez pas non plus besoin de vous soucier de l\'échappement des guillemets.

Voici un exemple :

```javascript
const city = "Paris"
const str1 = 'Elle a dit, "J\'adore ' + city + ', c\'est un endroit magnifique."'
const str2 = `Elle a dit, "J\'adore ${city}, c\'est un endroit magnifique`

console.log(regularString)
console.log(templateLiteral)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-04-at-7.00.42-AM.png align="left")

*Résultats des exemples de chaîne régulière et de littéral de gabarit*

Contrairement au littéral de gabarit, la chaîne régulière nécessite ce qui suit ;

* L\'utilisation du plus `+` pour la concaténation.
    
* L\'utilisation minutieuse des guillemets simples et doubles.
    
* La nécessité d\'échapper le guillemet simple dans la chaîne avec `\`.
    

## Quelques cas d\'utilisation pratiques des littéraux de gabarit

Jusqu\'à présent, vous avez appris ce que sont les littéraux de gabarit et comment ils se comparent aux chaînes de caractères régulières. Maintenant, examinons quelques exemples pratiques.

### Génération de balisage HTML

Vous verrez souvent des littéraux de gabarit utilisés pour générer du balisage HTML. Ils vous permettent d\'intégrer des expressions JavaScript directement dans des chaînes HTML. Cela facilite la création de contenu dynamique et piloté par les données.

Exemple :

```javascript
const user = {
  name: "Marie",
  age: 25,
};

const userProfile = `
<div>
  <h2>Nom : ${user.name}</h2>
  <p>Âge : ${user.age}</p>
</div>
`
```

Remarquez comment la syntaxe `${}` vous permet d\'exécuter des expressions JavaScript directement dans la chaîne. Dans ce cas, elle est utilisée pour lire les valeurs des propriétés de l\'objet `user`.

### Création de requêtes SQL dynamiques

Vous pouvez également utiliser des littéraux de gabarit pour créer des requêtes SQL dynamiques en intégrant des variables ou des expressions directement dans les chaînes de requête. Cela signifie que vous pouvez facilement créer des requêtes basées sur des valeurs d\'exécution.

Exemple :

```javascript
const tableName = "users";
const columnName = "name";
const searchValue = "John";

const sqlQuery = 
  `SELECT * FROM ${tableName} WHERE ${columnName} = '${searchValue}'`
```

### Localisation et internationalisation

Une autre utilisation pratique des littéraux de gabarit est la gestion de la localisation et de l\'internationalisation dans vos applications. Il est plus facile de gérer les traductions car avec les littéraux de gabarit, vous pouvez intégrer des variables pour le contenu localisé ou les clés de langue directement dans les chaînes.

Exemple :

```javascript
const user = {
  name: "Marie",
};

const locale = "fr";
const greetings = {
  en: "Hello",
  es: "Hola",
  fr: "Bonjour"
};

const localizedGreeting = `${greetings[locale]} ${user.name}!`;
console.log(localizedGreeting)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-04-at-7.51.34-AM.png align="left")

*Exemple d\'utilisation des littéraux de gabarit pour le contenu localisé.*

Cet exemple crée une chaîne `localizedGreeting` sans dépendre d\'aucune concaténation encombrante.

## Littéraux de gabarit étiquetés

Il s\'agit d\'une fonctionnalité des littéraux de gabarit JavaScript que vous pouvez utiliser pour effectuer une manipulation avancée de chaînes.

Pour utiliser cette fonctionnalité, vous avez besoin d\'une fonction d\'étiquette et ensuite d\'un gabarit étiqueté.

La fonction d\'étiquette prend en entrée un mélange de chaînes et de variables comme arguments. Elle les formate ensuite en fonction de certaines conditions ou règles que vous définissez.

Ensuite, vous appelez (ou exécutez) la fonction d\'étiquette en la plaçant avant le backtick d\'ouverture du littéral de gabarit.

### Syntaxe pour le littéral de gabarit étiqueté

```javascript
function taggedFunc(strings, ...values) {
  console.log(strings)
  console.log(values)
}

const name = 'Sarah'
const city = 'Rome'

taggedFunc`Bonjour ${name}. Bienvenue à ${city}.`
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-04-at-10.03.12-AM.png align="left")

*Résultats de journalisation pour les arguments de chaîne et de valeur d\'un littéral de gabarit étiqueté*

Il y a trois choses à noter ici.

Premièrement, le premier paramètre (`strings` dans cet exemple) est toujours un tableau de tous les blocs de chaînes dans le littéral de gabarit. Dans ce cas, il s\'agit du tableau ci-dessous.

```javascript
['Bonjour ', '. Bienvenue à ', '.']
```

Ensuite, le reste des paramètres sera toutes les variables et expressions évaluées dans les littéraux de gabarit. La syntaxe du [paramètre rest JavaScript](https://www.freecodecamp.org/news/javascript-rest-vs-spread-operators/) `...values` facilite l\'obtention de toutes.

```javascript
['Sarah', 'Rome']
```

Enfin, notez comment la `taggedFunc` est utilisée. Contrairement à une fonction régulière, vous ne l\'appellerez pas avec des parenthèses. Mais en l\'attachant avant le premier backtick du littéral de gabarit.

```javascript
taggedFunc`Bonjour ${name}. Bienvenue à ${city}.` ✅

taggedFunc(Bonjour ${name}. Bienvenue à ${city}.) ❌
```

## Exemples pratiques de littéraux de gabarit étiquetés

Maintenant, voyons quelques exemples pratiques d\'utilisation d\'un littéral de gabarit étiqueté pour gérer la manipulation de chaînes.

### Exemple 1

```javascript
function receiptTag(strings, ...values) {  

  let finalString = ''
  for (let i = 0; i < values.length; i++) {
    finalString += strings[i] + values[i]
  }

  // Ajouter le dernier littéral de chaîne
  finalString += strings[strings.length - 1] 

  return finalString
}

const item = 'apple'
const price = 2.5
const quantity = 3

const message = receiptTag`
  Vous avez ${quantity} ${item}s.
  Coût unitaire : $${price}. 
  Coût total : $${quantity * price}.
`

console.log(message)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-04-at-10.37.18-AM.png align="left")

*Exemple de chaîne formatée avec un littéral de gabarit étiqueté.*

Dans cet exemple, la fonction `recieptTag` reçoit un littéral de gabarit avec quatre expressions :

* `${quantity}`
    
* `${item}`
    
* `${price}`
    
* `${quantity * price}`
    

Le tableau `values` contiendra les valeurs évaluées de ces expressions.

```javascript
[3, 'apple', 2.5, 7.5]
```

Et vous pouvez les traiter en conséquence dans la fonction étiquetée.

Le résultat, enregistré dans la console est un `message` qui inclut des informations sur la quantité, l\'article, le coût unitaire et le coût total.

### Exemple 2

```javascript
function greetUser(strings, name) {
  const now = new Date()
  const currentHour = now.getHours()
  
  const timeOfDay = currentHour < 12 ? 'matin' : currentHour < 17 ? 'après-midi' : 'soirée'
  
  return `Bon ${timeOfDay} ${name}${strings[1]}`
}

const userName = 'Ama'

console.log(greetUser`Bonjour ${userName}, ravi de vous rencontrer !`)
```

Cet exemple utilise un littéral de gabarit étiqueté pour déterminer comment saluer l\'utilisateur en fonction de l\'heure de la journée.

La fonction obtient d\'abord l\'heure actuelle en utilisant l\'objet date. Ensuite, utilise un opérateur ternaire pour déterminer l\'heure de la journée. Et retourne une chaîne avec une variable `timeOfDay` indiquant l\'heure de la journée.

De plus, faites attention au premier mot de l\'instruction de journalisation et comparez-le au premier mot de la chaîne passée à l\'étiquette pour voir comment la fonction a modifié la chaîne.

## Conclusion

Les littéraux de gabarit offrent une manière pratique de travailler avec des chaînes en JavaScript. Dans cet article, vous avez appris la syntaxe et comment les utiliser dans vos projets.

Vous avez également appris une fonctionnalité avancée des littéraux de gabarit : les littéraux de gabarit étiquetés. Ce sont des fonctions qui prennent en entrée un tableau de blocs de chaînes et d\'expressions. Elles retournent une chaîne basée sur la logique que vous écrivez pour la fonction.

Merci d\'avoir lu. Et bon codage ! Pour des tutoriels plus approfondis, n\'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).