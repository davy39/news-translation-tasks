---
title: Comment utiliser l'opérateur satisfies de TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-10T17:12:59.000Z'
originalURL: https://freecodecamp.org/news/typescript-satisfies-operator
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Copy-of-Typescript-satisfies-Operator.png
tags:
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser l'opérateur satisfies de TypeScript
seo_desc: 'By Satyam Tripathi

  In TypeScript, the satisfies operator is a very useful tool. It was introduced in
  TypeScript v4.9 as an effective way to ensure type safety.

  The satisfies operator tells you whether a given type satisfies a particular condition
  – a...'
---

Par Satyam Tripathi

Dans TypeScript, l'opérateur `satisfies` est un outil très utile. Il a été introduit dans [TypeScript v4.9](https://github.com/microsoft/TypeScript/issues/50457) comme un moyen efficace d'assurer la sécurité des types.

L'opérateur `satisfies` vous indique si un type donné satisfait une condition particulière – et il fournit cette information avant d'exécuter votre code. De plus, lorsque vous l'utilisez, vous pouvez déclarer une nouvelle variable pour vérifier si le type d'une expression correspond à un autre type.

Dans cet article, vous apprendrez tout sur cet opérateur utile de TypeScript. J'expliquerai comment les choses étaient avant que cet opérateur ne soit disponible, et pourquoi nous en avons besoin. Nous explorerons également des scénarios réels où vous pouvez utiliser `satisfies` et les avantages qu'il offre.

## Qu'est-ce que l'opérateur `satisfies` de TypeScript ?

L'opérateur `satisfies` de TypeScript vérifie si un type donné satisfait une condition ou une interface spécifique. C'est un nouveau moyen efficace d'assurer la sécurité des types dans TypeScript.

`satisfies` garantit que toutes les variables correspondent à la définition et possèdent toutes les propriétés requises d'un type ou d'une interface spécifique.

## Pourquoi avez-vous besoin de l'opérateur `satisfies` ?

Examinons la vie avant l'opérateur `satisfies` de TypeScript et le problème qu'il résout. Nous commencerons par considérer un exemple simple.

Créons un type appelé `personInfo`, qui est une union de `personName` et `otherDetails`.

```typescript
type personInfo = personName | otherDetails;
```

`personInfo` sera soit `personName`, soit `otherDetails`. Maintenant, nous allons définir `personName` comme une chaîne avec trois valeurs possibles : '_John_', '_Jack_', et '_Justin_'.

```typescript
type personName = "John" | "Jack" | "Justin";
```

Maintenant, nous allons définir `otherDetails`.

```typescript
type otherDetails = {
  id: number;
  age: number;
};
```

`otherDetails` est un objet qui a deux propriétés, `id` et `age`, qui seront des nombres. Nous pouvons donc dire que notre type `personInfo` est une union d'une `string` et d'un `object`. Maintenant, créons le type `Person`.

```typescript
type Person = {
  myInfo: personInfo;
  myOtherInfo: personInfo;
};
```

Le type `Person` a deux propriétés, `myInfo` et `myOtherInfo`, toutes deux de type `personInfo`. Cela indique que les deux propriétés peuvent être soit `personName`, soit `otherDetails`. Maintenant, créons la variable `applicant`.

```typescript
const applicant: Person = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: 22 },
};
```

Comme montré dans le code ci-dessus, `myInfo` de l'applicant est défini sur "_John_" (l'une des valeurs du type `personName`). La propriété `myOtherInfo` est définie sur un objet avec la propriété `id` ayant la valeur `123`, et `age` ayant la valeur `22`. Maintenant, imaginons que nous voulons accéder à `myInfo` et le convertir en majuscules.

```typescript
applicant.myInfo.toUpperCase();
```

Maintenant, si nous survolons la fonction `toUpperCase()` avec notre souris, nous verrons un message d'erreur : `Property 'toUpperCase' does not exist on type 'personInfo' and Property 'toUpperCase' does not exist on type 'otherDetails'`.

Cette erreur se produit parce que TypeScript n'est pas sûr que la valeur de `myInfo` ou `myOtherInfo` soit une chaîne ou un objet puisque nous avons défini notre `personInfo` comme une union de chaîne et d'objet.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_145501157f840023f204935d54e49de1.png)
_Message d'erreur parce que TypeScript n'est pas sûr que la valeur de `myInfo` ou `myOtherInfo` soit une chaîne ou un objet._

Pour supprimer cette erreur, nous devons valider manuellement la propriété comme montré ci-dessous :

```typescript
if (typeof applicant.myInfo === "string") {
  applicant.myInfo.toUpperCase();
}
```

Ici, nous validons d'abord si le type `applicant` est une chaîne ou non. Si c'est une chaîne, nous utiliserons la méthode de chaîne pour nous assurer que TypeScript ne lance aucun message d'erreur.

Maintenant, supposons que nous avons beaucoup de propriétés, et il devient fastidieux de valider chaque propriété. Dans de tels cas, l'opérateur `satisfies` est très utile.

## Comment utiliser l'opérateur `satisfies`

Maintenant, les développeurs sont heureux parce que l'opérateur `satisfies` est arrivé. Avant cet opérateur, nous devions toujours pré-valider, et cela pouvait devenir fastidieux. Maintenant, avec l'aide de cet opérateur, vous n'avez plus besoin de faire tout cela.

Au lieu de définir `Person` à nouveau, nous pouvons le remplacer par l'opérateur `satisfies`, comme montré ci-dessous :

```typescript
const applicant = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: 22 },
} satisfies Person;

applicant.myInfo.toUpperCase();
```

L'opérateur `satisfies` détermine que la variable `myInfo` est une chaîne et non un objet. Cela est dû au fait que, avant d'exécuter le code, il vérifie toutes les valeurs du type `Person`. Cet opérateur garantit que nous attribuons toute valeur qui satisfait le type `Person` à la variable `applicant`.

Voir le code complet ci-dessous :

```typescript
type personInfo = personName | otherDetails;

type personName = "John" | "Jack" | "Justin";

type otherDetails = {
  id: number;
  age: number;
};

type Person = {
  myInfo: personInfo;
  myOtherInfo: personInfo;
};

const applicant = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: 22 },
} satisfies Person;
```

**Note :** Si nous essayons d'ajouter quelque chose à la propriété `myInfo` qui ne correspond pas au type défini, une erreur se produira. Par exemple, dans ce cas, `myInfo` devrait être une chaîne, mais si nous attribuons une valeur booléenne, une erreur sera générée.

Vous pouvez obtenir une erreur si vous n'utilisez pas l'opérateur `satisfies` de TypeScript et que vous définissez un objet avec une propriété différente. Par exemple, dans notre scénario, l'âge est une valeur `boolean`, donc il ne satisfait pas l'exigence (les données devraient être soit une `string`, soit un `object`).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_6eb976f68482f623c0db89fb5130c0b6.png)
_La ligne rouge dans age et dans toUpperCase() montre que vous n'utilisez pas l'opérateur satisfies._

Vous pouvez voir qu'il y a une ligne rouge dans `age` et dans la fonction `toUpperCase()`. Cela montre que si vous n'utilisez pas l'opérateur `satisfies` et que vous essayez de faire des changements à d'autres objets, vous obtiendrez une erreur.

Ici, le problème était seulement avec `age`, mais nous obtenons également une erreur en changeant `myInfo`.

Si vous utilisez l'opérateur `satisfies`, vous ne rencontrerez pas d'erreurs dans d'autres objets. Dans ce cas, le problème est avec `age`, qui devrait être soit une `string`, soit un `object` mais est au lieu de cela un `boolean`. Par conséquent, l'erreur est spécifique à la variable `age` et n'affecte pas les autres objets.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_e1066360bb78289236ec5574be935af0.png)
_L'erreur est spécifique à la variable age et n'affecte pas les autres objets._

Lorsque vous survolez l'âge, vous verrez le message d'erreur suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_3bba64495ec8e5783fcb92eb78f1afa5.png)
_Lorsque vous survolez l'âge, vous verrez le message d'erreur._

Merci à l'opérateur `satisfies` de TypeScript pour la pré-validation.

**Note :** Pour résoudre l'erreur ci-dessus, vous pouvez modifier la propriété `age` de l'objet `otherDetails`. Vous pouvez inclure le booléen dans l'âge comme montré ci-dessous :

```typescript
type otherDetails = {
  id: number;
  age: number | boolean;
};
```

Maintenant, le code ci-dessous ne lancera aucune erreur car nous avons déjà mentionné que notre âge pourrait être soit un `number`, soit un `boolean`.

```typescript
type personInfo = personName | otherDetails;

type personName = "John" | "Jack" | "Justin";

type otherDetails = {
  id: number;
  age: number | boolean;
};

type Person = {
  myInfo: personInfo;
  myOtherInfo: personInfo;
};

const applicant = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: true },
} satisfies Person;

applicant.myInfo.toUpperCase();
```

### Contrainte de nom de propriété

Nous pouvons utiliser l'opérateur `satisfies` pour nous assurer qu'un sous-ensemble des clés est inclus. Dans le code ci-dessous, nous avons 5 clés et notre code indique que l'objet person doit satisfaire le type `Partial<Record<Keys, string | number>>`.

```typescript
type Keys = "personID" | "personName" | "personEmail" | "personAge" | "personPhone";

const person = {
  personID: 12345,
  personName: "Jacky",
  personEmail: "jacky@testing.com",
  personAge: 22,
} satisfies Partial<Record<Keys, string | number>>;

person.personName.toUpperCase();
person.personAge.toFixed();
```

`Partial<Record<Keys, string | number>>` créera un objet qui aura toutes les cinq clés et valeurs (qui peuvent être une `string` ou un `number`). Actuellement, notre objet person n'a que quatre propriétés : `personID`, `personName`, `personEmail`, et `personAge`. Toutes les propriétés de l'objet person satisfont les propriétés du type partiel.

### Remplissage du nom de propriété

Ici, nous vérifions si toutes les propriétés de l'objet person satisfont `Record<Keys, string | number>`.

`Record<Keys, string | number>` créera un type de record qui a 4 propriétés, chacune pouvant être soit une `string`, soit un `number`.

```typescript
type Keys = "personID" | "personName" | "personEmail" | "personAge";

const person = {
  personID: 12345,
  personName: "Jacky",
  personEmail: "jacky@testing.com",
  personAge: 22,
} satisfies Record<Keys, string | number>;

person.personName.toUpperCase();
person.personAge.toFixed();
```

Maintenant, si nous supprimons une propriété de l'objet `person`, alors le code lancera une erreur, car l'objet `person` ne restera qu'avec 3 propriétés qui ne satisferont pas le type `record`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_159790f137c6c0b380a6beff3201231b.jpg)
_L'objet `person` n'a que 3 propriétés qui ne satisferont pas le type record._

### Conformité de la valeur de propriété

Comme discuté dans la section `contrainte de nom de propriété`, l'opérateur `satisfies` a pu restreindre les noms des propriétés dans un objet. Cependant, il peut également restreindre les valeurs de ces propriétés.

Considérons l'exemple ci-dessous. Nous avons défini un objet appelé `pcStore` qui contient divers pcs. Chaque pc dans l'objet `pcStore` suit les propriétés définies dans le type `PC`.

Dans `pc4`, nous avons représenté par erreur le `price` comme une `string`, ce qui est incorrect. L'objet `PC` spécifie que la propriété `price` devrait être un `number`.

Pour identifier et attraper cette erreur, nous pouvons utiliser l'opérateur `satisfies`. Il déterminera si toutes les propriétés dans `pcStore` suivent le type `PC` ou non.

```typescript
type PC = { name: string; ram: string; price: number };

const pcStore = {
  pc1: { name: "Dell", ram: "10 GB", price: 12000 },
  pc2: { name: "HP", ram: "8 GB", price: 11000 },
  pc3: { name: "Asus", ram: "6 GB", price: 13000 },
  pc4: { name: "Mac", ram: "20 GB", price: "21000" },
} satisfies Record<string, PC>;
```

Si nous survolons le prix avec la souris, TypeScript lance une erreur indiquant que `string cannot be assigned to a variable of type number`. Cette erreur se produit parce que la variable `price` est déclarée comme un `number`, mais nous essayons de lui attribuer une valeur `string`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_2a7a4636ae3870ac3c9e48825f9416b7.jpg)
_Nous essayons d'attribuer la chaîne à l'objet price, mais une chaîne n'est pas attribuable à un nombre._

L'opérateur `satisfies` attrapera l'erreur avant que vous n'exécutiez le code.

## Avantages de l'opérateur `satisfies` de TypeScript

L'opérateur `satisfies` nous permet de vérifier si un objet a une propriété spécifique. Il peut aider à la sécurité des types, à la correction du code, à la validation, à la réutilisabilité du code et à l'organisation du code.

### Sécurité des types

Vous pouvez utiliser l'opérateur `satisfies` pour vérifier si un objet satisfait un type particulier ou non. Cela peut rendre votre code plus fiable et diminuer les chances d'erreurs dans le code.

### Validation

Vous pouvez également utiliser l'opérateur `satisfies` pour valider l'entrée de l'utilisateur. Il nous permet de vérifier si le type d'une expression correspond à un autre type. Par exemple, vous pouvez l'utiliser pour vérifier si l'email de l'utilisateur correspond au type string ou non.

### Correction du code

L'opérateur `satisfies` vous permet également de vérifier si le code est correct ou non. Il vérifie si un objet particulier satisfait toutes les propriétés requises.

### Réutilisabilité du code

L'opérateur `satisfies` aide à rendre le code plus réutilisable. Il garantit que différents blocs de code peuvent travailler avec les mêmes types de données et suivre les mêmes propriétés.

### Organisation du code

En fonction du type de valeur, vous pouvez diviser votre code en différents blocs, ce qui peut rendre le code plus facile à lire et à gérer.

## Conclusion

L'opérateur `satisfies` peut rendre votre code réutilisable et maintenable. Le meilleur aspect de l'opérateur `satisfies` est qu'il pré-valide les valeurs et offre la meilleure expérience de vérification de type.

Vous pouvez également utiliser l'opérateur `satisfies` pour restreindre les noms et les valeurs de toute propriété, comme nous l'avons discuté dans les sections Contrainte de nom de propriété et Conformité de la valeur de propriété.

Merci d'avoir lu !