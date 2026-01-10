---
title: Comment utiliser les génériques TypeScript avec les composants fonctionnels
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-27T18:53:32.000Z'
originalURL: https://freecodecamp.org/news/typescript-generics-with-functional-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/federico-beccari-ahi73ZN5P0Y-unsplash.jpg
tags:
- name: generics
  slug: generics
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser les génériques TypeScript avec les composants fonctionnels
  React
seo_desc: "By Olasunkanmi Balogun\nIn this article, we will explore the powerful synergy\
  \ between TypeScript generics and functional React components. \nGenerics allow\
  \ you to define flexible components that can adapt to different data structures\
  \ and enforce type s..."
---

Par Olasunkanmi Balogun

Dans cet article, nous allons explorer la puissante synergie entre les génériques TypeScript et les composants fonctionnels React. 

Les génériques vous permettent de définir des composants flexibles qui peuvent s'adapter à différentes structures de données et renforcer la sécurité des types dans votre base de code. 

En tirant parti des génériques dans les composants fonctionnels, vous pouvez créer des éléments d'interface utilisateur hautement réutilisables et adaptables qui peuvent gérer de manière transparente les différentes exigences de données.

Dans ce tutoriel, nous commencerons par comprendre le concept des génériques en TypeScript et comment ils peuvent être bénéfiques dans le contexte du développement React. 

Nous plongerons ensuite dans des exemples pratiques, démontrant comment définir des composants fonctionnels génériques dans React en utilisant TypeScript. 

Nous discuterons également de divers cas d'utilisation où les props génériques brillent, nous permettant de construire des applications React polyvalentes et évolutives.

## Qu'est-ce que les génériques en TypeScript ?

Afin d'explorer les composants fonctionnels avec les génériques, vous devez comprendre les bases des fonctions génériques en TypeScript, y compris leur définition et leur implémentation. 

Dans cette section, vous obtiendrez un aperçu concis de ce que sont les génériques et comment les implémenter en TypeScript. Cela devrait vous équiper des connaissances nécessaires pour approfondir le domaine des composants fonctionnels.

### Comment déclarer une fonction générique en TypeScript

Pour déclarer une fonction générique en TypeScript, nous plaçons un paramètre de type générique, noté `<T>`, au début de la signature de la fonction. Ce `<T>` représente un type qui sera passé lorsque la fonction est utilisée. Il sert de placeholder pour un type spécifique qui sera déterminé lors de l'exécution, similaire à la manière dont les paramètres se comportent dans les fonctions régulières. 

Par exemple, considérons la fonction suivante :

```ts
function func<T>(value: T):T[] {
   return [value];
}

func('Hello John');
```

Dans cet exemple, le paramètre de type générique `T` est utilisé pour indiquer que le paramètre de valeur et le type de retour seront du même type. 

Lorsque la fonction `func` est appelée avec l'argument `'Hello John'`, le type déduit pour `T` devient `string`. Par conséquent, le type de retour de la fonction est `string[]`, indiquant qu'un tableau contenant la valeur de chaîne fournie sera retourné.

### Comment définir des génériques avec des fonctions fléchées en TypeScript

La syntaxe pour définir une fonction générique avec des fonctions fléchées est légèrement différente de celle de la déclaration de fonction que nous avons vue précédemment :

```ts	
export const func = <T>(value: T):T[] => {
   return [value];
}

func('Hello John');
```

D'après ce qui précède, nous voyons que lorsque nous utilisons des fonctions fléchées pour définir des fonctions génériques en TypeScript, nous employons la syntaxe `<T>` avant la liste des paramètres pour indiquer un paramètre de type générique.

Ensuite, il est important de noter que le paramètre de type générique `T` utilisé dans les exemples précédents est simplement un nom descriptif et peut être remplacé par tout autre identifiant valide. Par exemple :

```ts
export const func = <K>(value: K):K[] => {
   return [value];
}

func('Hello John');
```

Le paramètre de type générique `T` a été remplacé par `K`, montrant que le choix du nom pour le type générique est flexible et peut être personnalisé pour correspondre au contexte ou à la préférence du développeur. 

La fonction `func` reste générique, capable d'accepter tout type spécifié lors de l'utilisation et de retourner un tableau de ce même type.

Maintenant que vous savez comment implémenter des fonctions génériques et comprendre leur flexibilité dans le retour de tout type passé, nous allons maintenant apprendre comment implémenter des composants génériques dans React. 

Dans la section suivante, je fournirai un guide étape par étape sur la façon de créer et d'utiliser des composants génériques. Cela vous aidera à exploiter la puissance des génériques dans le développement React.


## Comment définir et utiliser des composants génériques dans React

Tout comme avec les fonctions génériques, vous pouvez porter la réutilisabilité des composants à un niveau supérieur en concevant des composants génériques avec l'intégration des génériques TypeScript. 

Déclarer les props génériques qu'un composant générique acceptera est l'étape initiale dans la conception du composant. Nous pouvons construire une interface de props paramétrée qui supporte différents types de données en utilisant les génériques TypeScript.

```ts
interface MyComponentProps<T> {
  data: T;
  // Ajoutez des props supplémentaires spécifiques à votre composant
}
```

Une fois l'interface des props génériques définie, vous pouvez ensuite implémenter le composant générique lui-même. Cela implique l'utilisation des props génériques déclarées et leur intégration dans la structure du composant. 

Similaire à la description de la fonction TypeScript dans la section précédente, elle a la même implémentation.

```tsx
function MyComponent<T>({ data }: MyComponentProps<T>) {

  return (
    <div>
      {/* Contenu JSX */}
    </div>
  );
}
```

Suite à cela, vous pouvez également définir des composants génériques en utilisant la syntaxe des fonctions fléchées. Mais cela est différent lorsque vous écrivez votre code dans un fichier `JSX.Element`.

Pour éviter toute ambiguïté entre les paramètres de type générique et un composant `jsx`, vous ajoutez une virgule finale au paramètre de type pour le différencier d'un `JSX.Element`. Par exemple :

```tsx
interface MyComponentProps<T> {
  data: T;
}
// remarquez la virgule finale après <T
const MyComponent = <T,>({ data }: MyComponentProps<T>) => {
  return (
  <div>{Contenu JSX}</div>;
  )
};
export default MyComponent;
```

### Exemple de cas d'utilisation des composants génériques

Supposons que vous souhaitiez développer un tableau de bord de visualisation de données capable de présenter des données provenant de diverses sources, chacune avec ses propres structures et propriétés. Mais vous souhaitez créer un composant réutilisable qui peut générer un résumé de n'importe quel objet de données, en se concentrant sur une propriété spécifique.

Ce scénario offre l'opportunité de plonger dans une application pratique d'un composant générique dans React. 

En étendant le paramètre de type à un `object` et en utilisant l'opérateur `keyof` dans les interfaces, vous pouvez construire un composant qui offre à la fois flexibilité et sécurité de type. 

Cette approche exploite les capacités du système de types robuste de TypeScript, vous permettant de travailler avec une variété d'objets de manière transparente.

Pour ce faire, définissez un composant générique appelé `Summary<T>` qui accepte un paramètre de type `T` étendant un objet. Vous utiliserez également l'opérateur `keyof` pour spécifier la propriété de l'objet que vous souhaitez afficher dans le résumé :

```ts
interface SummaryProps<T extends object, K extends keyof T> {
  data: T;
  property: K;
}

export function Summary<T extends object, K extends keyof T>({
  data,
  property,
}: SummaryProps<T, K>) {
  const value = data[property] as string;

  return (
    <div>
      {(typeof property === "string") ? (
        <p>
          {property}: {value}{" "}
        </p>
      ) : (
        ""
      )}
    </div>
  );
}
```

Dans le composant `Summary`, nous avons défini un paramètre de type générique `T` qui étend `object`, garantissant que les données passées au composant sont de type `object`. 

Le deuxième paramètre de type `K` utilise la notation `keyof` `T`, indiquant qu'il doit être une clé du type d'objet `T`. De cette manière, vous pouvez accéder à une propriété spécifique de l'objet de données en fonction de la valeur de la propriété fournie.

Dans le composant, nous avons extrait la valeur de l'objet `data` en utilisant la `property` comme clé. Pour nous assurer que la valeur est traitée comme une `string`, nous avons utilisé le mot-clé `as` pour effectuer une assertion de type : `data[property] as string` pour éviter les erreurs d'assignation. Cette assertion de type indique à TypeScript de traiter la valeur comme une `string`.

Le composant retourne ensuite un élément `<div>` contenant un rendu conditionnel d'un élément `<p>`. Le code vérifie ensuite si la `property` est de type `string` en utilisant `typeof property === "string"`. De cette manière, il évite également les erreurs d'assignation.

Si cela évalue à `true`, le code rend l'élément `<p>`, affichant la `property` et la `value`. Sinon, une `string` vide est retournée.

Ayant défini le composant, considérons un exemple où vous avez deux sources de données différentes : `User` et `Product`. Chaque source de données a ses propres propriétés, mais vous souhaitez afficher un résumé basé sur une propriété spécifique.

Vous pouvez commencer par définir l'interface `User` pour représenter les données utilisateur, en spécifiant des propriétés telles que `id`, `name` et `email`. De même, créez l'interface `Product` pour représenter les données produit, incluant des propriétés comme `id`, `name` et `price`, comme ceci :

```tsx
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
}
```

Ensuite, vous pouvez créer des instances de ces objets de données. Par exemple, `userData` peut représenter un `user` et `productData` peut représenter un `product`, avec leurs propriétés respectives remplies de données d'exemple :

```ts
const userData: User = {
  id: 1,
  name: "John Doe",
  email: "johndoe@example.com"
};

const productData: Product = {
  id: 1,
  name: "Smartphone",
  price: 999
};
```

Pour utiliser le composant `Summary`, fournissez-lui différentes sources de données et spécifiez la propriété que vous souhaitez afficher dans le résumé. 

Par exemple, vous pouvez utiliser `<Summary<User, "name">>` pour rendre un résumé du nom de l'utilisateur, et `<Summary<Product, "price">>` pour afficher le prix du produit :

```ts
<Summary<User, "name"> data={userData} property="name" />
<Summary<Product, "price"> data={productData} property="price" />
```

Le code complet ressemble à ceci :

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
}

const userData: User = {
  id: 1,
  name: "John Doe",
  email: "johndoe@example.com"
};

const productData: Product = {
  id: 1,
  name: "Smartphone",
  price: 999
};

// Utilisation du composant Summary avec différentes sources de données et propriétés
<Summary<User, "name"> data={userData} property="name" />
<Summary<Product, "price"> data={productData} property="price" />
```

Le puissant mécanisme d'inférence de type de TypeScript entre en jeu dans ce scénario. Lorsque vous fournissez les `data` et `property` au composant `Summary`, TypeScript garantit que la propriété spécifiée est valide pour la source de données correspondante. 

Si vous tentez par erreur d'utiliser une propriété invalide, comme fournir `"email"` comme propriété pour les données `Product`, le compilateur TypeScript lèvera une erreur de type. Cela garantit la sécurité des types et aide à prévenir les problèmes potentiels d'exécution.

En tirant parti de la vérification de type statique de TypeScript, nous bénéficions de la sécurité des types et de la validation lors de l'utilisation de composants génériques comme `Summary`. Cela aide également à détecter les erreurs tôt dans le processus de développement et garantit que les combinaisons de `data` et `property` fournies sont correctes.

## Conclusion

Dans ce guide, nous avons exploré le concept des génériques en TypeScript et comment ils peuvent être appliqués pour créer des composants puissants et réutilisables dans React. 

Les génériques nous permettent de définir des composants suffisamment flexibles pour travailler avec divers types de données tout en maintenant la sécurité des types.

Tout au long de cet article, vous avez appris les fondamentaux des génériques, y compris l'implémentation des fonctions génériques. Nous avons ensuite plongé dans le monde des composants génériques dans React, démontrant comment les définir et les implémenter en utilisant à la fois les méthodes de fonction `arrow` et `named`.

Alors que vous continuez votre parcours avec TypeScript, je vous encourage à explorer davantage la puissance et la flexibilité des props génériques. En utilisant les génériques, vous pouvez débloquer de nouvelles possibilités dans la création de composants réutilisables et sécurisés qui renforcent vos applications React. Bon codage !