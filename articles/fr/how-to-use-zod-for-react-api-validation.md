---
title: Comment utiliser Zod pour la validation des API React
subtitle: ''
author: Emore Ogheneyoma Lawrence
co_authors: []
series: null
date: '2025-02-28T17:59:48.190Z'
originalURL: https://freecodecamp.org/news/how-to-use-zod-for-react-api-validation
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740756200896/a57c4e95-b13e-412a-828e-09e97f22a6c4.png
tags:
- name: React
  slug: reactjs
- name: zod
  slug: zod
- name: API
  slug: api
- name: TypeScript
  slug: typescript
- name: frontend
  slug: frontend
seo_title: Comment utiliser Zod pour la validation des API React
seo_desc: 'In React applications, handling API (Application Programming Interface)
  responses can be challenging. You might encounter data that’s missing crucial fields,
  that’s formatted unexpectedly, or that simply doesn’t match what you anticipated.

  This incon...'
---

Dans les applications React, la gestion des réponses d'API (Application Programming Interface) peut être difficile. Vous pouvez rencontrer des données manquantes, des champs cruciaux, des données formatées de manière inattendue ou des données qui ne correspondent tout simplement pas à ce que vous aviez anticipé.

Cette incohérence peut entraîner des erreurs dans votre code et rendre difficile le travail efficace avec les données. Imaginez lutter contre des réponses d'API imprévisibles à mesure que votre application grandit – cela peut rapidement devenir un cauchemar de développement !

C'est là que Zod intervient, offrant une solution pour gérer efficacement la validation des données d'API dans React.

### À la fin de ce tutoriel, vous apprendrez comment :

1. Configurer et utiliser Zod pour la validation des réponses d'API dans React.
   
2. Définir des schémas pour valider et transformer les données entrantes.
   
3. Intégrer Zod dans les appels d'API pour améliorer la gestion des données et prévenir les plantages de l'UI.
   

## Table des matières

* [Qu'est-ce que Zod et pourquoi l'utiliser pour les appels d'API React ?](#heading-questce-que-zod-et-pourquoi-lutiliser-pour-les-appels-dapi-react)
   
* [Comment générer un nouveau projet React TypeScript](#heading-comment-generer-un-nouveau-projet-react-typescript)
   
* [Concepts de base de Zod : Utilisation de base, types et validation](#heading-concepts-de-base-de-zod-utilisation-de-base-types-et-validation)
   
* [Comment construire des schémas Zod pour les réponses d'API](#heading-comment-construire-des-schemas-zod-pour-les-reponses-dapi)
   
* [Comment intégrer Zod avec les appels d'API React](#heading-comment-integrer-zod-avec-les-appels-dapi-react)
   
* [Comment rendre l'interface utilisateur (UI) et gérer les erreurs dans React](#heading-comment-rendre-linterface-utilisateur-ui-et-gerer-les-erreurs-dans-react)
   
* [Conclusion](#heading-conclusion)
   

## Qu'est-ce que Zod et pourquoi l'utiliser pour les appels d'API React ?

Zod est une bibliothèque puissante, conçue pour TypeScript, qui simplifie la validation des données. Elle vous permet de définir des règles claires (schémas) pour le format de données attendu.

Zod peut ensuite valider les données entrantes (souvent issues des réponses d'API) pour s'assurer qu'elles se conforment à ces règles. Ce processus de validation garantit que les données respectent votre format défini, améliorant ainsi la fiabilité et l'intégrité de votre application.

Voici pourquoi Zod est idéal pour la validation des API React :

* Schémas clairs : Zod vous aide à définir des plans concis pour les réponses d'API, améliorant la lisibilité et la maintenabilité.
   
* Validation des données : Il offre des méthodes de validation puissantes pour divers types de données, appliquant des règles comme les champs obligatoires et les formats spécifiques.
   
* Détection précoce des erreurs : Il vous aide à détecter les incohérences de données lors des appels d'API, prévenant ainsi les erreurs inattendues plus tard dans l'application.
   
* Meilleure expérience développeur : Il favorise le codage sécurisé par les types, rationalisant le temps de développement en éliminant les vérifications manuelles des types de données.
   
* Source unique de vérité : Enfin, Zod sert de point central pour les définitions de modèles de données, assurant la cohérence dans l'application React et réduisant les erreurs.
   

En utilisant Zod, vous pouvez transformer des réponses d'API imprévisibles en données propres et structurées, préparant le terrain pour une expérience de développement plus fluide et plus efficace dans vos applications React.

## Comment générer un nouveau projet React TypeScript

Créer un nouveau projet React avec TypeScript est simple. Voici comment commencer. Exécutez la commande suivante dans votre terminal :

```bash
npm create vite@latest my-react-app -- --template react-ts
```

Une fois le projet généré, naviguez vers le répertoire du projet :

```bash
cd my-react-app
npm install
npm run dev
```

C'est tout ! Votre projet React avec TypeScript est maintenant prêt à être utilisé. Exécutez la commande suivante pour installer le package Zod :

```bash
npm install zod
```

## Concepts de base de Zod : Utilisation de base, types et validation

Zod vous aide à définir des attentes claires pour les réponses de votre API en utilisant des **schémas**. Ces schémas agissent comme des plans, spécifiant les types de données que vous attendez de recevoir.

### Comment construire des schémas

Zod fournit des fonctions de construction comme `z.string()`, `z.number()` et `z.object()` pour créer des schémas. Ces fonctions définissent le type de données que vous souhaitez pour un champ spécifique dans votre réponse.

```typescript
import { z } from 'zod';
// Définir des types de données de base
const userName = z.string().min(5).max(10); // Chaîne avec min 5 et max 10 caractères
const userAge = z.number().positive().int();  // Entier positif
const userEmail = z.string().email();        // Assure un format d'email valide

console.log(userName.parse('John Doe'));       // Sortie : John Doe (valide)
console.log(userAge.parse(30));              // Sortie : 30 (valide)
console.log(userEmail.parse("johnDoe@gmail.com")); // Sortie : johnDoe@gmail.com (valide)
```

Le code ci-dessus définit trois types de données de base :

* `userName` : Représente une chaîne avec une longueur minimale de 5 caractères et une longueur maximale de 10 caractères.
   
* `userAge` : Représente un entier positif.
   
* `userEmail` : Assure un format d'email valide.
   

Voici le résultat du code ci-dessus :

![Image du résultat du code ci-dessus](https://cdn.hashnode.com/res/hashnode/image/upload/v1738857987322/55a5943c-6633-4432-a441-c3dfa9400d93.png align="center")

### Comment ajouter des règles de validation

Zod vous permet d'enchaîner des méthodes comme **min**, **max**, **positive**, **int** et **email** pour appliquer des règles spécifiques à ces types de données. Voici un exemple de chaîne invalide dépassant la longueur maximale :

```typescript
console.log(userName.parse("Hello there, My Name is John Doe")); // Lance une ZodError
```

Le code lance une `ZodError` en raison du dépassement de la longueur maximale de 10 caractères, perturbant le flux de votre application et provoquant finalement la rupture de votre application.

Voici l'image du résultat de l'erreur du code :

![Image du résultat du code ci-dessus](https://cdn.hashnode.com/res/hashnode/image/upload/v1738859384410/27c2a5f3-2410-4709-ac27-8bf24f6c3fd8.png align="center")

### Validation et analyse

Zod offre deux façons de vérifier les données par rapport à votre schéma :

* `schema.parse(data)` : Cette méthode tente d'analyser les données selon votre schéma. Mais en cas d'erreur de validation, elle lance une `ZodError`. Cela peut perturber le flux de votre application, comme illustré dans l'exemple précédent.
   
* `schema.safeParse(data)` : C'est l'approche recommandée. Elle analyse les données et retourne un objet `ZodResult`. Cet objet contient certaines propriétés clés :
   
   * `success` : Un booléen indiquant si l'analyse a réussi.
       
   * `data` : Les données analysées elles-mêmes (si la propriété success est vraie)
       
   * `error` : Un message d'erreur si la validation échoue (si la propriété success est fausse)
       

Voici deux exemples montrant l'utilisation de `safeParse` avec des données valides et invalides afin que vous puissiez voir les résultats obtenus.

Tout d'abord, voyons un exemple utilisant `safeParse` avec des données valides :

```typescript
const userSchema = z.object({
  name: userName,
  age: userAge,
  email: userEmail,
});

const userData = {
  name: "John Doe",
  age: 24,
  email: "johndoe@gmail.com"
};

const result = userSchema.safeParse(userData);

console.log(result); // ZodObject contenant les données et le statut de succès
```

Ce code définit un schéma pour les données utilisateur en utilisant Zod, incluant les propriétés pour le nom, l'âge et l'email. Il tente ensuite d'analyser un objet `userData` d'exemple en utilisant ce schéma via `safeParse()`. Si l'opération réussit, il imprime les données analysées – sinon, il journalise un message d'erreur indiquant l'utilisation de données invalides.

Voici l'image du résultat du code ci-dessus :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738861119776/7f9cf3ec-fc83-452c-9477-1c7d6422efe3.png align="center")

Voyons maintenant comment `safeParse()` gère les données invalides en utilisant le même exemple que ci-dessus. Nous allons passer des données invalides à la fonction `userSchema.safeParse()` pour observer son comportement.

```typescript
const userSchema = z.object({
  name: userName,
  age: userAge,
  email: userEmail,
});

const userData = {
  name: "John Doe",
  age: 24,
  email: "johndoe.com" // email invalide
};

const result = userSchema.safeParse(userData);

console.log(result); // ZodObject contenant l'erreur et le statut de succès
```

Dans cet exemple de code, nous avons défini le `userSchema`. Ensuite, nous avons tenté d'analyser l'objet `userData`. Mais l'analyse a échoué car la propriété email n'était pas correctement formatée. Voici une représentation visuelle du résultat obtenu :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1740502631913/25dead7a-ab09-4d1d-9dcc-fada38e7d4d6.png align="center")

Contrairement à l'utilisation de `parse`, qui arrête complètement votre application en cas d'erreurs de validation et lance une `ZodError`, l'utilisation de `safeParse` vous permet de gérer ces erreurs de manière élégante, assurant ainsi un fonctionnement ininterrompu.

## Comment construire des schémas Zod pour les réponses d'API

En nous basant sur notre compréhension des concepts de base de Zod, créons des schémas Zod spécifiquement pour les données reçues des appels d'API. Nous utiliserons les données de [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), qui offre des informations sur les posts.

Voici un exemple de réponse JSON représentant un post de JSONPlaceholder :

```typescript
{
  "userId": 1,
  "id": 3,
  "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
  "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut"
}
```

Créez un composant React (donnez-lui un nom qui correspond à la structure de votre projet) pour démontrer la construction et l'utilisation des schémas Zod pour la validation d'API. Dans cet article, à des fins d'illustration, nous l'appellerons le composant `ZodApi`.

```typescript
 import { z } from 'zod';

  const postSchema = z.object({
  userId: z.number().positive().int(),
  id: z.number().positive().int(),
  title: z.string(),
  body: z.string()
});
        
const postSchemaArray = z.array(postSchema); // Schéma pour un tableau de posts
```

Ce code définit la structure attendue d'un objet post unique (`postSchema`) et d'un tableau de posts (`postSchemaArray`).

Les sections suivantes exploreront l'intégration de Zod avec les composants React pour la gestion des appels d'API et la gestion des erreurs.

## Comment intégrer Zod avec les appels d'API React

Comblons l'écart entre vos schémas Zod définis et les interactions réelles avec l'API.

Nous devrons mettre à jour le code que nous avons écrit dans la section précédente pour obtenir le résultat souhaité dans cette section.

```typescript
import { z } from 'zod';
import { useEffect } from 'react';

const postSchema = z.object({
  userId: z.number().positive().int(),
  id: z.number().positive().int(),
  title: z.string(),
  body: z.string()
});

const postSchemaArray = z.array(postSchema); // schéma pour un tableau de posts

type Posts = z.infer<typeof postSchemaArray>; // type des posts

const ZodApi = () => {
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((posts: Posts) => {
        const validatedPosts = postSchemaArray.safeParse(posts); // n'oubliez pas d'utiliser safeParse au lieu de parse

        if (validatedPosts.success === false) {
          console.log("Erreur de validation :"validatedPosts.error);
          return;
        }

        // nous pouvons maintenant utiliser les posts en toute sécurité
        console.log(validatedPosts.data);
      });
  }, []);
  return <div>ZodApi</div>;
};

export default ZodApi;
```

Le composant `ZodApi` démontre :

* Récupération des données : Utilise `useEffect` et `fetch` pour obtenir les données de l'API.
   
* Sécurité des types : `type Posts = z.infer<typeof postSchemaArray>;` assure la sécurité des types en définissant le `type Posts` inféré du schéma `postSchemaArray`.
   
* Analyse avec Zod : Valide les données récupérées par rapport au `postSchemaArray` en utilisant `safeParse`.
   
* Gestion du succès : Si la validation réussit, elle fournit un accès aux données propres dans `validatedPosts.data` pour une utilisation dans votre composant (UI, état, etc.).
   

Gestion des erreurs : L'instruction `if` montre une approche simple pour la gestion des erreurs Zod. Dans un cas où la validation n'est pas réussie (`validatedPosts.success === false`), un message d'erreur Zod est journalisé dans la console.

Voici un aperçu montrant le résultat obtenu dans la console.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1740504815204/45ce101a-4e8c-475b-ad4d-783b0940710b.png align="center")

## Comment rendre l'interface utilisateur (UI) et gérer les erreurs dans React

Dans cette section, vous apprendrez comment rendre l'UI en fonction de nos données validées et mettre en œuvre le mécanisme de gestion des erreurs en utilisant les états React.

```typescript
import { z } from "zod";
import { useEffect, useState } from "react";

const postSchema = z.object({
  userId: z.number().positive().int(),
  id: z.number().positive().int(),
  title: z.string(),
  body: z.string(),
});

const postSchemaArray = z.array(postSchema); // schéma pour un tableau de posts

type Posts = z.infer<typeof postSchemaArray>; // type des posts

const ZodApi = () => {
  const [posts, setPosts] = useState<Posts>([]); // État pour stocker les posts validés
  const [error, setError] = useState(""); // État pour stocker les erreurs
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((posts: Posts) => {
        const validatedPosts = postSchemaArray.safeParse(posts); // n'oubliez pas d'utiliser safeParse au lieu de parse

        if (validatedPosts.success === false) {
          console.log(validatedPosts.error.name);
          setError(validatedPosts.error.message); // définir l'état d'erreur
          return;
        }

        // nous pouvons maintenant utiliser les validatedPosts en toute sécurité
        console.log(validatedPosts.data);
        setPosts(validatedPosts.data)
      });
  }, []);

  // Gérer l'état de chargement (optionnel)
  if (!posts.length && !error) {
    return <div>Chargement des posts...</div>;
  }

  // Gérer l'état d'erreur
  if (error) {
    return <div>Erreur lors de la récupération des données</div>; // Afficher un message d'erreur convivial
  }

  return (
    <div>
      <h1>Posts</h1>
      <ol>
        {posts.map((post) => (
          <li key={post.id}>
            {post.title}
          </li>
        ))}
      </ol>
    </div>
  );
};

export default ZodApi;
```

Dans le code ci-dessus, nous avons mis à jour le composant `ZodApi` pour effectuer les tâches suivantes :

* Déclaration d'état : Les états `posts` et `error` contiennent les données et les erreurs (le cas échéant) obtenues de la requête fetch.
   
* Gestion des erreurs : Nous utilisons les états `posts` et `error` pour afficher un message "Chargement des posts..." lorsque les posts sont en cours de récupération et qu'aucune erreur ne se produit, et afficher un message d'erreur lorsqu'une erreur se produit.
   
* Rendu des posts : Il parcourt les posts récupérés et les affiche sur l'UI.
   

Sortie :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1740506104138/f2afac53-e312-4a40-af01-500e0dd349f7.gif align="center")

Après avoir récupéré les résultats, vous devriez voir les 100 posts s'afficher à l'écran. Si vous avez suivi les étapes correctement, vous trouverez les 100 posts visibles. Si vous rencontrez des problèmes, assurez-vous que le processus de récupération a réussi.

## Conclusion

En intégrant Zod dans votre flux de travail de développement React, vous pouvez construire des applications plus robustes et fiables.

Zod vous permet de détecter les données non conformes dès le début, prévenant ainsi les erreurs et économisant un temps précieux de débogage. De plus, les messages d'erreur conviviaux fournis par la validation Zod améliorent l'expérience utilisateur globale de votre application.