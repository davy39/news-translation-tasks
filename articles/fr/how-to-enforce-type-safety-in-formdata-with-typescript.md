---
title: Comment appliquer la sécurité des types dans FormData avec TypeScript
subtitle: ''
author: Olabisi Olaoye
co_authors: []
series: null
date: '2025-03-10T14:06:41.633Z'
originalURL: https://freecodecamp.org/news/how-to-enforce-type-safety-in-formdata-with-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741615550682/6e709ad7-f8bb-4d26-acad-02f168d83acc.png
tags:
- name: TypeScript
  slug: typescript
- name: formdata
  slug: formdata
- name: JavaScript
  slug: javascript
- name: APIs
  slug: apis
seo_title: Comment appliquer la sécurité des types dans FormData avec TypeScript
seo_desc: When working with the FormData interface in JavaScript, where data is appended
  as key/value pairs, there's no built-in way to enforce type safety on the keys you
  append. This can lead to typos, missing keys, and unexpected runtime errors. But
  in Type...
---

Lorsque vous travaillez avec l'interface FormData en JavaScript, où les données sont ajoutées sous forme de paires clé/valeur, il n'existe aucun moyen intégré d'appliquer la sécurité des types sur les clés que vous ajoutez. Cela peut entraîner des fautes de frappe, des clés manquantes et des erreurs d'exécution inattendues. Mais avec TypeScript, nous pouvons résoudre ce problème en appliquant une validation stricte des clés.

J'ai eu besoin de cette solution moi-même lorsque j'envoyais les valeurs de mon formulaire à une API. J'ai ensuite réalisé que j'avais fait plusieurs erreurs typographiques dans plus d'une paire clé/valeur que je tentais d'ajouter à ma charge utile. Comme FormData accepte n'importe quelle chaîne comme clé, j'ai pu passer les mauvaises chaînes et poursuivre la demande API.

Après que cela soit arrivé, j'ai cherché un moyen de m'assurer que TypeScript n'autorise pas ces erreurs.

Cet article vous montrera comment rendre les clés `FormData` **sûres en termes de types** en utilisant TypeScript.

## Prérequis

Pour tirer le meilleur parti de cet article, vous devez avoir une compréhension de base des éléments suivants :

1. Programmation JavaScript
   
2. Fondamentaux de TypeScript, en particulier le fonctionnement des interfaces, des types et de l'opérateur `keyof`
   
3. L'interface FormData
   

Si vous êtes nouveau dans TypeScript ou FormData, je vous recommande de consulter la [documentation officielle de TypeScript](https://www.typescriptlang.org/docs/) et le [guide de MDN sur FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) avant de continuer.

## Étape 1 : Définir vos clés autorisées

### L'ancienne méthode

La méthode par défaut pour ajouter des données avec FormData consiste à le faire manuellement, avec des chaînes simples :

```typescript
const payload = new FormData();

payload.append("id", "1122");
payload.append("name", "Clark Kent");

payload.append("agge", "36"); // Faute de frappe dans la clé est autorisée
```

Dans l'extrait de code ci-dessus, vous pouvez voir qu'il y avait une faute de frappe lors de la définition d'une clé pour `age`. Mais TypeScript ne le signalera pas comme une erreur, et cela pourrait entraîner des erreurs lorsque ces données sont envoyées avec une demande API.

### La meilleure méthode

Au lieu de taper manuellement les clés, définissez-les dans un schéma d'objet avec une interface TypeScript.

```typescript
interface MyAllowedData {
    id: number;
    name: string;
    age: number;
}
```

Alternativement, vous pouvez les définir avec des types :

```typescript
type MyAllowedData = {
    id: number;
    name: string;
    age: number;
}
```

Vous pouvez utiliser soit des types soit des interfaces, c'est simplement une question de préférence. Vous pouvez en savoir plus sur leurs différences dans ce [bac à sable de la documentation officielle de TypeScript](https://www.typescriptlang.org/play/?#example/types-vs-interfaces).

Ensuite, définissez un type union à partir de chaque clé de votre interface.

```typescript
type MyFormDataKeys = keyof MyAllowedData
// cela revient au même que `type MyFormDataKeys = 'id' | 'name' | 'age'`
```

L'opérateur `keyof` aide à créer un type union des clés d'un type d'objet, donc il est très utile si vous ne voulez pas définir manuellement un type union pour un objet plus grand avec de nombreuses clés.

## Étape 2 : Créer une fonction d'assistance pour l'ajout

Maintenant que vous avez défini vos clés strictement typées, l'étape suivante consiste à créer une fonction d'assistance qui garantit que seules les clés valides sont ajoutées à FormData.

```typescript
function appendToFormData (formData: FormData, key: MyFormDataKeys, value: string) {
  formData.append(key, value);
};
```

La fonction `appendToFormData` prend trois arguments. Voici comment cela fonctionne :

* Le premier argument, `formData`, est une instance de l'objet FormData. C'est ici que les paires clé/valeur seront ajoutées avant d'être envoyées dans une demande API.
   
* Le deuxième argument, `key`, est le nom de la clé du champ que vous souhaitez ajouter. Son type est `MyFormDataKeys`, le type union que nous avons créé pour garantir que seules les clés que nous avons définies sont ajoutées à FormData.
   
* Le troisième argument est une chaîne `value` qui représente la valeur à ajouter avec la clé.
   

Notez que **FormData n'accepte que les types** `string` **et** `Blob` **comme valeurs** dans chaque paire clé/valeur. Dans ce guide, nous travaillons uniquement avec des valeurs de type chaîne, mais gardez à l'esprit que vous pouvez utiliser des valeurs blob pour ajouter des fichiers aux demandes API.

Testons maintenant la fonction :

```typescript
const payload = new FormData();

appendToFormData(payload, "id", "19282"); // ✅ Autorisé
appendToFormData(payload, "name", "Lenny Brown"); // ✅ Autorisé
appendToFormData(payload, "age", "20"); // ✅ Autorisé

appendToFormData(payload, "someOtherKey", "89"); // ❌ Erreur TypeScript : L'argument de type 'someOtherKey' n'est pas assignable.
```

## Étape 3 : Utiliser la fonction d'assistance après la soumission du formulaire

Maintenant, ajoutons nos champs à FormData avant de les envoyer à une API.

```typescript
const handleSubmitForm = () => {
  const payload = new FormData();
   appendToFormData(payload, "id", "19282");
   appendToFormData(payload, "name", "Lenny Brown");
   appendToFormData(payload, "age", "20");

  // Envoyer la charge utile via l'API
  fetch("/api/submit", { method: "POST", body: payload });
};
```

### Ajout de champs à partir d'un objet

Alternativement, si vous avez déjà votre charge utile complète dans un objet, vous pouvez éviter d'ajouter chaque champ un par un en implémentant la fonction comme ceci :

```typescript
const handleSubmitForm = () => {
  // toutes vos champs dans un objet
  const formValues: MyAllowedData = {
    id: 1123,
    name: 'John Doe',
    age: 56
  }
  const payload = new FormData();

  Object.entries(formValues).forEach(([key, value]) => {
    appendToFormData(payload, key as MyFormDataKeys, `${value}`); // utiliser les littéraux de gabarit pour passer la valeur
  });

  // Envoyer la charge utile via l'API
  fetch("/api/submit", { method: "POST", body: payload });
};
```

Dans l'extrait ci-dessus, nous utilisons `Object.entries` pour itérer sur chaque paire clé/valeur dans un objet afin qu'elle puisse être ajoutée à l'objet FormData. Notez que la valeur dans chaque paire, qu'il s'agisse d'une chaîne ou d'un nombre, est passée en tant que chaîne en utilisant des [littéraux de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) pour éviter une incompatibilité de type TypeScript avec l'argument `value` dans notre fonction d'assistance.

## Conclusion

En tirant parti de l'opérateur `keyof` de TypeScript, nous pouvons rendre `FormData.append()` entièrement sûr en termes de types. Cette technique simple aide à prévenir les incompatibilités de clés et rend vos demandes API plus fiables.

Faites-moi part de vos réflexions sur l'article et n'hésitez pas à faire des suggestions que vous pensez pouvoir améliorer ma solution.

Merci d'avoir lu !