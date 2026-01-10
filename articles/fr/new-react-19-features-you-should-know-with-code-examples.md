---
title: Nouvelles fonctionnalités de React 19 à connaître – Expliquées avec des exemples
  de code
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2024-09-30T18:36:59.834Z'
originalURL: https://freecodecamp.org/news/new-react-19-features-you-should-know-with-code-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727367514092/a75164cd-1e2e-4b0d-8c2e-5d000cee01f0.png
tags:
- name: React
  slug: reactjs
- name: React 19
  slug: react-19
- name: JavaScript
  slug: javascript
seo_title: Nouvelles fonctionnalités de React 19 à connaître – Expliquées avec des
  exemples de code
seo_desc: 'React.js is 11 years old, and it has become one of the most popular JavaScript
  libraries out there.

  And now, React is transitioning from version 18 to version 19. So hold onto your
  hats, React enthusiasts 🎩. React 19 has recently landed, and it’s a ...'
---

React.js a 11 ans et il est devenu l'une des bibliothèques JavaScript les plus populaires du marché.

Et maintenant, React passe de la version 18 à la version 19. Alors attachez vos ceintures, passionnés de React 🎩. React 19 vient d'arriver, et c'est un changement de donne.

Mais avant de vous inquiéter d'une courbe d'apprentissage abrupte, voici une excellente nouvelle : React 19 ne consiste pas à ajouter de la complexité, mais à la supprimer.

Dans ce guide, vous découvrirez comment cette nouvelle version simplifiera votre vie de développeur et boostera vos projets React.

## Ce que nous allons couvrir :

* [Introduction à React 19](#heading-introduction-a-react-19)
    
* [Ce que nous allons couvrir :](#heading-ce-que-nous-allons-couvrir)
    
* [Fonctionnalités de React 19](#heading-fonctionnalites-de-react-19)
    
* [React Compiler : La magie en coulisses](#heading-react-compiler-la-magie-en-coulisses)
    
* [Plus de hooks de mémoisation](#heading-plus-de-hooks-de-memoisation)
    
* [Plus de forwardRef : Gestion des refs simplifiée](#heading-plus-de-forwardref-gestion-des-refs-simplifiee)
    
* [Le nouveau hook use() : Un changement de donne](#heading-le-nouveau-hook-use-un-changement-de-donne)
    
* [Récupérer des données avec use() vs. useEffect](#heading-recuperer-des-donnees-avec-use-vs-useeffect)
    
* [Utiliser Context avec use()](#heading-utiliser-le-contexte-avec-use)
    
* [Directives : Une nouvelle approche](#heading-directives-une-nouvelle-approche)
    
* [Actions : Gestion des formulaires simplifiée](#heading-actions-gestion-des-formulaires-simplifiee)
    
* [useFormStatus() : Gestion de l'état du formulaire](#heading-useformstatus-gestion-de-letat-du-formulaire)
    
* [useFormState() : Actions de formulaire avec état](#heading-useformstate-actions-de-formulaire-avec-etat)
    
* [useOptimistic() : Amélioration de l'expérience utilisateur](#heading-useoptimistic-amelioration-de-lexperience-utilisateur)
    
* [Conclusion](#heading-conclusion)
    

Enthousiaste à l'idée d'essayer React 19 ? 🤩 Bien qu'il soit encore au stade canary, vous pouvez commencer à l'expérimenter en installant la version canary dès aujourd'hui. Cette mise à jour promet une expérience plus fluide en automatisant ce qui était auparavant des optimisations manuelles.

## **React Compiler : La magie en coulisses**

La star de React 19 est son nouveau compiler. 🎉 Ce compiler transforme votre code React en JavaScript pur, ce qui augmente les performances et, mieux encore, vous libère de l'ajustement constant des performances manuellement.

Pour optimiser nos applications React, nous utilisons des méthodes intégrées comme `useMemo` ou `useCallback`. Cela indique à React de ne pas recompiler le code si les entrées ne changent pas.

Mais si vous oubliez d'appliquer la mémoisation, cela entraîne un gaspillage des ressources de React et de la puissance de calcul. Pour remédier à cela, React 19 a introduit le React Compiler.

Dites adieu aux optimisations manuelles et bonjour à un code plus propre :

```javascript
// Pas besoin de useCallback/useMemo
function Component() {
  return <div>Optimized!</div>;
}
```

**Explication du code :** Le nouveau compiler transforme le code React en JavaScript optimisé, supprimant le besoin d'optimisations manuelles comme la mémoisation.

## **Plus de hooks de mémoisation**

Vous souvenez-vous de l'époque où vous jongliez entre `useCallback`, `useMemo` et `memo` pour optimiser les performances ? 😅 Avec React 19, cette époque est révolue. Le nouveau compiler optimise votre code en coulisses, vous pouvez donc abandonner ces hooks et vous concentrer sur l'écriture de composants React beaux et propres.

La mémoisation résout les problèmes de calculs complexes au sein de React, ce qui entraîne une optimisation de l'application et des améliorations de performance.

Auparavant, pour appliquer la mémoisation, vous deviez utiliser le hook `useMemo`. Voici à quoi cela ressemblait dans le code :

```javascript
// React 18 
import React, { useState, useMemo } from 'react';

const ExpensiveComponent = () => {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState('');

  // Mémoriser un calcul coûteux
  const expensiveCalculation = useMemo(() => {
    console.log("Calcul en cours...");
    let sum = 0;
    for (let i = 0; i < 1000000000; i++) {
      sum += i;
    }
    return sum;
  }, [count]); // Recalculer uniquement quand `count` change

  return (
    <div>
      <h1>Calcul coûteux : {expensiveCalculation}</h1>
      <button onClick={() => setCount(count + 1)}>Incrémenter le compte ({count})</button>
      <input 
        type="text" 
        value={input} 
        onChange={(e) => setInput(e.target.value)} 
        placeholder="Tapez quelque chose"
      />
    </div>
  );
};

export default ExpensiveComponent;
```

**Explication du code** :

* La fonction `expensiveCalculation` est lourde en termes de calcul, mais en utilisant `useMemo`, elle n'est recalculée que lorsque `count` change.
    
* Le champ de saisie peut être mis à jour sans déclencher un nouveau calcul de `expensiveCalculation`, ce qui optimise les performances.
    

Désormais, avec le compiler dans React 19, cela n'est plus nécessaire. Vous pouvez simplement écrire votre code et React appliquera la mémoisation.

Regardez cet exemple de code :

```javascript
// Pas besoin de mémoisation manuelle avec React 19
function Component({ children }) {
  return <div>{children}</div>;
}
```

**Explication du code :** vous n'avez plus besoin d'utiliser `useCallback` ou `useMemo` – React 19 gère automatiquement les optimisations.

## **Plus de** `forwardRef` **: Gestion des refs simplifiée**

Utiliser `forwardRef` pour passer des refs était autrefois une petite corvée. 😟 Mais dans React 19, vous pouvez passer des refs comme n'importe quelle autre prop. Cela simplifie le code de votre composant et rend la gestion des refs un jeu d'enfant. 🧹

```javascript
function Child({ innerRef }) {
  return <input ref={innerRef} />;
}
```

**Explication du code :** `forwardRef` n'est plus requis – à la place, les refs sont transmises comme des props régulières.

## **Le nouveau** `use()` Hook : Un changement de donne

Le nouveau hook polyvalent `use()` remplace plusieurs hooks, tels que `useEffect` pour la récupération de données ainsi que `useContext` et `useState` pour consommer les données de contexte. Il simplifie votre code en gérant les promesses et le contexte avec une solution unique et élégante.

Regardez cet exemple de code :

```javascript
import React, { useState, useEffect } from 'react';

const DataFetchingComponent = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  if (loading) return <p>Chargement...</p>;
  if (error) return <p>Erreur : {error}</p>;

  return (
    <div>
      <h1>Données :</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default DataFetchingComponent;
```

**Explication du code :**

* `useEffect` est déclenché après le montage du composant pour initier la récupération des données.
    
* Nous maintenons les états `loading`, `data`, et `error` pour gérer et afficher l'interface utilisateur appropriée.
    
* Une fois les données récupérées, l'état se met à jour, déclenchant un nouveau rendu pour afficher les données.
    

Maintenant, à l'aide du nouveau hook `use()` dans React 19, la récupération de données devient plus facile et vous n'avez plus besoin de dépendre de hooks de gestion d'état comme `useState()`.

Voici un exemple :

```javascript
import React, { use } from 'react';

// Fonction pour récupérer les données
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  if (!response.ok) {
    throw new Error('Échec de la récupération des données');
  }
  return response.json();
}

const DataFetchingComponent = () => {
  // `use()` suspend le composant jusqu'à ce que la promesse soit résolue
  const data = use(fetchData());

  return (
    <div>
      <h1>Données :</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default DataFetchingComponent;

```

**Explication du code :**

* **Suspense et** `use()` : Lorsque vous utilisez `use()`, cela suspend le rendu du composant jusqu'à ce que la promesse soit résolue. Si une erreur survient, cela peut également déclencher une frontière d'erreur `Suspense`.
    
* **Pas besoin de** `useEffect` : Il n'est plus nécessaire de gérer manuellement la récupération de données avec des effets secondaires, car React s'en occupe en interne.
    
* **États d'erreur et de chargement** : Ceux-ci peuvent désormais être gérés globalement à l'aide des frontières d'erreur `Suspense` sans suivre manuellement des états comme `loading` ou `error`.
    

### **Récupérer des données avec** `use()` vs. `useEffect`

Récupérer des données nécessitait autrefois un peu de code répétitif avec `useEffect`. Avec `use()`, vous résolvez simplement la promesse et utilisez React Suspense pour une expérience de récupération de données propre et facile. 🧼 Cela signifie moins de code et plus de concentration sur ce qui compte.

### **Utiliser Context avec** `use()`

La gestion des données de contexte est également devenue plus directe. Le nouveau hook `use()` peut désormais consommer directement le contexte, éliminant ainsi le besoin de `useContext` et rendant la gestion du contexte plus intuitive. 🎯

## **Directives : Une nouvelle approche**

Si vous utilisez Next.js, vous avez peut-être déjà vu des directives. 🌐 React 19 introduit des directives pour simplifier la configuration des composants. Utilisez `use client` pour les composants côté client et `use server` pour ceux côté serveur. C'est aussi simple que d'ajouter une chaîne de caractères en haut de votre fichier :

```javascript
"use client";
function ClientComponent() {
  return <div>Côté Client</div>;
}
```

**Explication du code :** Utilisez `use client` et `use server` pour déclarer des composants côté client ou côté serveur.

## **Actions : Gestion des formulaires simplifiée**

Les formulaires viennent de recevoir une mise à jour majeure avec les actions. 💥 Les actions sont des fonctions connectées aux soumissions de formulaires qui peuvent s'exécuter soit côté serveur, soit côté client. Cela signifie un code plus propre et un processus de gestion de formulaire plus fluide.

```javascript
async function action(formData) {
  return await handleSubmit(formData);
}
```

**Explication du code :** Les actions gèrent les soumissions de formulaires, s'exécutant sur le client ou le serveur.

#### **Actions Client : Un exemple pratique**

Les actions client sont idéales pour un retour immédiat. Par exemple, alerter les utilisateurs avec les valeurs qu'ils ont saisies n'a jamais été aussi simple. Utilisez simplement `use client` et connectez l'action du formulaire à la prop `action` du formulaire. Un jeu d'enfant ! 🥳

## `useFormStatus()` : Gestion de l'état du formulaire

Gardez une trace des soumissions de vos formulaires avec le hook `useFormStatus()`. ⏳ Il aide à gérer les états des formulaires, comme la désactivation du bouton de soumission pendant que le formulaire est en attente. C'est un indispensable pour des expériences utilisateur fluides.

```javascript
const { pending } = useFormStatus();
return <button disabled={pending}>Soumettre</button>;
```

**Explication du code :** `useFormStatus()` suit les états de soumission du formulaire, comme la désactivation d'un bouton pendant la soumission.

## `useFormState()` : Actions de formulaire avec état

Nous avons maintenant `useFormState()`, qui est un nouveau hook pour gérer l'état du formulaire. 🎛️ Il est similaire à `useState` mais fonctionne avec les actions de formulaire, vous permettant d'accéder à la fois à l'état précédent et aux données soumises. C'est parfait pour des scénarios comme l'ajout d'articles à un panier.

Je trouve que `useFormState()` est étroitement associé aux fonctionnalités de la bibliothèque React Hook Form, car ses caractéristiques de fonctionnement sont très similaires.

Voici un exemple de code pour vous aider à mieux comprendre :

```javascript
import React from 'react';
import { useForm, useFormState } from 'react-hook-form';

const MyForm = () => {
  const { register, handleSubmit, control } = useForm();
  const { isSubmitting, isDirty, isValid } = useFormState({ control });

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label htmlFor="firstName">Prénom :</label>
        <input {...register('firstName', { required: true })} />
      </div>
      <div>
        <label htmlFor="lastName">Nom :</label>
        <input {...register('lastName', { required: true })} />
      </div>
      <button type="submit" disabled={isSubmitting || !isValid}>
        Soumettre
      </button>
      <div>
        <p>Le formulaire est {isDirty ? 'modifié' : 'vierge'}</p>
        <p>En cours de soumission : {isSubmitting ? 'Oui' : 'Non'}</p>
      </div>
    </form>
  );
};

export default MyForm;
```

**Explication du code :**

1. **Importation des Hooks** : Nous importons `useForm` et `useFormState` depuis `react-hook-form`.
    
2. **Configuration du formulaire** :
    
    * `useForm` : Ce hook initialise les méthodes du formulaire, y compris `register`, `handleSubmit`, et `control`.
        
    * `useFormState` : Nous utilisons ce hook pour extraire les propriétés de l'état du formulaire comme `isSubmitting`, `isDirty`, et `isValid`.
        
3. **Enregistrement des entrées** : Nous enregistrons chaque champ de saisie à l'aide de la fonction `register`, en spécifiant toutes les règles de validation (par exemple `required`).
    
4. **Gestion de la soumission** : La fonction `onSubmit` gère la soumission du formulaire, où vous pouvez effectuer les actions souhaitées avec les données du formulaire.
    
5. **Informations sur l'état du formulaire** : Nous affichons l'état actuel du formulaire (s'il a été modifié ou soumis) sous le formulaire.
    

### Caractéristiques clés de `useFormState` :

* **Performance** : `useFormState` ne déclenche un nouveau rendu que lorsque les champs spécifiques qu'il surveille changent, ce qui le rend efficace.
    
* **État contrôlé** : Vous pouvez facilement gérer et observer l'état du formulaire sans écrire de code répétitif pour gérer les changements et les validations.
    

## `useOptimistic()` : Amélioration de l'expérience utilisateur

Pour les applications en temps réel, le hook `useOptimistic()` est utile. 💬 Il permet des mises à jour optimistes, rendant votre application plus réactive en mettant à jour instantanément l'interface utilisateur et en se synchronisant avec le serveur en arrière-plan.

```javascript
const [optimisticState, setOptimistic] = useOptimistic(initialState);
```

**Explication du code :** Permet des mises à jour optimistes de l'UI avant la synchronisation avec le serveur.

## **Conclusion**

React 19 est là pour simplifier votre expérience de codage et améliorer les performances. 🎉 Pour approfondir toutes ces fonctionnalités et plus encore, consultez mon récent [article](https://www.freecodecamp.org/news/learn-react-hooks-with-example-code/) sur les Hooks React.

Si vous êtes prêt à rationaliser vos projets React, embrassez l'avenir avec React 19 et rendez votre expérience de développement plus fluide et plus agréable. 🌟

* Suivez-moi sur X : [Twitter de Prankur](https://x.com/prankurpandeyy)
    
* Suivez-moi sur Linkedin : [Linkedin de Prankur](https://linkedin.com/in/prankurpandeyy)
    
* Consultez mon Portfolio ici : [Portfolio de Prankur](https://prankurpandeyy.netlify.app)