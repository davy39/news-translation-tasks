---
title: Comment simplifier vos composants React avec l'état dérivé
subtitle: ''
author: Olaleye Blessing
co_authors: []
series: null
date: '2025-11-24T20:58:35.744Z'
originalURL: https://freecodecamp.org/news/simplify-react-components-with-derived-state
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764017894421/6bbd5cf2-c221-490c-891a-bf984cfaa92c.png
tags:
- name: React
  slug: reactjs
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
- name: ReactHooks
  slug: reacthooks
seo_title: Comment simplifier vos composants React avec l'état dérivé
seo_desc: 'React simplifies building user interfaces with hooks like useState for
  managing dynamic values. But it''s common to overuse useState. This often leads
  to duplicated data and unnecessary complexity.

  For instance, you might store a full name in state wh...'
---


React simplifie la création d'interfaces utilisateur avec des hooks comme `useState` pour gérer les valeurs dynamiques. Mais il est courant de surestimer l'utilisation de `useState`. Cela conduit souvent à une duplication des données et à une complexité inutile.

Par exemple, vous pourriez stocker un nom complet dans un état alors qu'il peut être calculé à partir des props de prénom et de nom, ou dupliquer des données récupérées via une bibliothèque comme React Query. Cela crée des problèmes tels qu'un débogage plus difficile, des re-rendus superflus et des problèmes de synchronisation.

Dans ce tutoriel, vous apprendrez à utiliser l'état dérivé pour améliorer vos composants. À la fin, vous saurez quand dériver un état au lieu de le stocker, rendant votre code React plus propre et plus facile à maintenir.

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Qu'est-ce qu'un état dérivé ?](#heading-qu-est-ce-qu-un-etat-derive)
    
3. [Comment dériver l'état à partir de données existantes](#heading-comment-deriver-l-etat-a-partir-de-donnees-existantes)
    
    * [Comment dériver l'état à partir des props ou d'un autre état](#heading-comment-deriver-l-etat-a-partir-des-props-ou-d-un-autre-etat)
        
    * [Comment dériver l'état à partir d'une URL](#heading-comment-deriver-l-etat-a-partir-d-une-url)
        
    * [Comment dériver l'état à partir de données externes](#heading-comment-deriver-l-etat-a-partir-de-donnees-externes)
        
4. [Comment empêcher le recalcul d'un état dérivé](#heading-comment-empecher-le-recalcul-d-un-etat-derive)
    
5. [Quand utiliser useState](#heading-quand-utiliser-usestate)
    
    * [Entrée contrôlée](#heading-entree-controlee)
        
    * [Changements d'état indépendants](#heading-changements-d-etat-independants)
        
6. [Conclusion](#heading-conclusion)
    

## Prérequis {#heading-prerequis}

Avant de continuer, assurez-vous d'avoir :

* Des connaissances de base en JavaScript, TypeScript, React et les hooks React
    
* Une compréhension des appels asynchrones
    
* Un environnement de développement React simple.
    

Si vous n'avez pas de configuration React, vous pouvez vous rendre sur le [repo derived-state](https://github.com/Olaleye-Blessing/freecodecamp-derived-states). Le repo a été configuré avec [React Router](https://reactrouter.com/) et [React Query](https://tanstack.com/query/latest/docs/framework/react/overview). Exécutez les commandes ci-dessous pour l'installer :

```bash
# clone the repo
git clone <https://github.com/Olaleye-Blessing/freecodecamp-derived-states.git>

# navigate to the folder
cd freecodecamp-derived-states

# install the packages
pnpm install

# start development
pnpm dev
```

## Qu'est-ce qu'un état dérivé ? {#heading-qu-est-ce-qu-un-etat-derive}

Un état dérivé est toute valeur qui peut être calculée à partir de données existantes. Ces données existantes peuvent provenir de :

* **Props :** Données transmises depuis un composant parent.
    
* **État existant :** Autres variables d'état déjà présentes dans votre composant.
    
* **Paramètres d'URL :** Données provenant des routes ou des chaînes de requête (query strings).
    
* **Données externes :** Données provenant d'une bibliothèque de récupération comme React Query.
    

Stocker un état dérivable dans `useState` peut créer plusieurs problèmes. Premièrement, cela peut causer des difficultés de débogage : plus il y a de variables d'état, plus il est difficile de tracer le flux de données. Plus vous avez d'états, plus le nombre de changements d'état à suivre lors du débogage est important.

Cela peut également provoquer des re-rendus inutiles. React déclenchera un re-rendu chaque fois que vous appellerez la fonction de mise à jour de l'état (setter).

Enfin, il peut y avoir des problèmes de synchronisation, car vous êtes obligé de mettre à jour manuellement l'« état dérivé » chaque fois que la donnée source change. Lorsque des données similaires existent dans plusieurs états, elles peuvent se désynchroniser.

## Comment dériver l'état à partir de données existantes {#heading-comment-deriver-l-etat-a-partir-de-donnees-existantes}

Par la suite, nous explorerons des scénarios courants où vous pouvez dériver l'état au lieu de le stocker dans un autre `useState`.

Note : Tout le code de cet article est exécuté en [mode non-strict](https://react.dev/reference/react/StrictMode).

### Comment dériver l'état à partir des props ou d'un autre état {#heading-comment-deriver-l-etat-a-partir-des-props-ou-d-un-autre-etat}

Dans cette section, nous examinerons d'abord les problèmes causés par l'utilisation de `useState` pour des valeurs dérivables. Nous regarderons un composant de formulaire qui stocke des états inutiles comme le nom complet, le statut d'adulte et une copie locale d'un e-mail. Vous verrez les re-rendus dans différents scénarios, puis apprendrez à refactoriser en utilisant l'état dérivé pour éliminer ces problèmes.

#### Le problème des états superflus

Toute valeur qui provient directement des props ou d'un autre état peut être dérivée à la volée. Prenez l'exemple ci-dessous, où vous passez une prop `email` à un composant de formulaire :

```typescript
<DetailForm email="olaleyedev@gmail.com" />
```

Voici comment le formulaire reçoit la prop email et gère également son propre état :

```typescript
import { useEffect, useState, type FormEventHandler } from "react";

interface DetailFormProps {
  email: string;
}

const DetailForm = ({ email }: DetailFormProps) => {
  const [lastName, setLastName] = useState("");
  const [fullName, setFullName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [age, setAge] = useState(0);
  const [isAdult, setIsAdult] = useState(false);
  const [localEmail, setLocalEmail] = useState(email);

  useEffect(() => {
    setLocalEmail(email);
  }, [email]);

  useEffect(() => {
    setFullName(`${firstName} ${lastName}`.trim());
  }, [firstName, lastName]);

  useEffect(() => {
    setIsAdult(age > 18);
  }, [age]);

  const submitForm: FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    console.log({ fullName, age, isAdult });
  };

  console.count("-- Form render --");

  return (
    <form onSubmit={submitForm}>
      <div style={{ marginBottom: "1rem" }}>
        <label
          htmlFor="firstName"
          style={{
            display: "inline-block",
            marginRight: "1rem",
            width: "10rem",
          }}
        >
          First Name
        </label>
        <input
          id="firstName"
          type="text"
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>
      <div style={{ marginBottom: "1rem" }}>
        <label
          htmlFor="lastName"
          style={{
            display: "inline-block",
            marginRight: "1rem",
            width: "10rem",
          }}
        >
          Last Name
        </label>
        <input
          id="lastName"
          type="text"
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>
      <div style={{ marginBottom: "1rem" }}>
        <label
          htmlFor="age"
          style={{
            display: "inline-block",
            marginRight: "1rem",
            width: "10rem",
          }}
        >
          Age
        </label>
        <input type="number" onChange={(e) => setAge(Number(e.target.value))} />
      </div>
      <p>
        Your receipt will have{" "}
        <span
          style={{
            borderBottom: "1px solid #fffa",
            paddingBottom: "1px",
          }}
        >
          {fullName.trim() || "-----"}
        </span>{" "}
        as the recipient's name and will be sent to {localEmail || "-----"}.
      </p>
      <p>
        {isAdult
          ? "You are allowed to order a drink."
          : "You are not allowed to order any drinks."}
      </p>
      <button type="submit" disabled={!isAdult}>
        Submit
      </button>
    </form>
  );
};

export default DetailForm;
```

Le composant de formulaire collecte les informations d'un utilisateur. Il affiche plus d'informations basées sur leur saisie et l'e-mail fourni. Il maintient certains états pour suivre la saisie de l'utilisateur.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762625903293/c952e785-2b37-4411-987f-01686db8f54e.png align="center")

Bien que cela semble simple, il y a des problèmes dans la façon dont l'état est utilisé ici.

Tout d'abord, un composant React se re-rend chaque fois que l'un de ses états change. En regardant l'interface utilisateur, le formulaire ne devrait se re-rendre que lorsque les utilisateurs saisissent leur prénom, leur nom et leur âge, ou lorsque la prop email change depuis le parent. Cela signifie que le formulaire ne devrait suivre que ces trois états en interne, tout en dérivant les autres de la prop et des autres états.

Mais le formulaire suit trois états supplémentaires (`fullName`, `isAdult`, et `localEmail`). Cela signifie que le formulaire se re-rendra chaque fois que ces états supplémentaires changeront.

Voyons cela en action :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762626688959/f381aa1f-6244-4065-aa36-123134f26b1b.gif align="center")

Comme vous pouvez le voir, le formulaire s'est re-rendu deux fois lorsque le champ de saisie a changé, au lieu d'une seule fois. Le formulaire s'est re-rendu la première fois que l'utilisateur a mis à jour son prénom. Mais à chaque fois que le prénom et le nom changeaient, le deuxième `useEffect` se déclenchait.

```typescript
useEffect(() => {
  setFullName(`${firstName} ${lastName}`.trim());
}, [firstName, lastName]);
```

Ceci sert à synchroniser le `fullName` avec le `firstName` et le `lastName`. La mise à jour du `fullName` provoque le second re-rendu du formulaire.

La même chose s'applique à l'état `isAdult`. Lorsque l'utilisateur met à jour son `age`, `setAge()` re-rend le formulaire, et le troisième `useEffect` provoque également un autre re-rendu.

#### Gestion des changements d'e-mail

Voyons ce qui se passe lorsque vous mettez à jour l'e-mail depuis le composant parent. Voici le code qui permet de mettre à jour l'e-mail :

```typescript
function App() {
  const [email, setEmail] = useState("olaleyedev@gmail.com");

  return (
    <>
      <div
        style={{
          marginBottom: "1rem",
          border: "1px solid #fff",
          paddingBottom: "1rem",
        }}
      >
        <h3>Parent Component</h3>
        <input
          style={{ padding: "0.4rem 0.8rem" }}
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <DetailForm email={email} />
    </>
  );
}
```

Le composant parent suit l'e-mail de l'utilisateur et le met également à jour via un élément `input`.

Note : Dans le composant `<Detail />`, j'ai supprimé les `useEffect` qui synchronisent le `fullName` et `isAdult`. C'est pour se concentrer principalement sur la prop `email`. Le composant de formulaire ressemble maintenant à ceci :

```typescript
import { useEffect, useState, type FormEventHandler } from "react";

interface DetailFormProps {
  email: string;
}

const DetailForm = ({ email }: DetailFormProps) => {
  const [lastName, setLastName] = useState("");
  const [fullName, setFullName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [age, setAge] = useState(0);
  const [isAdult, setIsAdult] = useState(false);
  const [localEmail, setLocalEmail] = useState(email);

  useEffect(() => {
    setLocalEmail(email);
  }, [email]);

  const submitForm: FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    console.log({ fullName, age, isAdult });
  };

  console.count("-- Form render --");

  return <form onSubmit={submitForm}>{/* Rest */}</form>;
};

export default DetailForm;
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762626841744/9beffe7d-2513-4d3e-9970-21477b16161e.gif align="center")

La mise à jour de l'e-mail depuis le composant parent provoque un re-rendu supplémentaire du formulaire de détails. Parce que vous enregistrez l'e-mail dans un état local, tout changement de la prop `email` déclenche le `useEffect` pour mettre à jour l'état, provoquant un re-rendu supplémentaire. Votre interface utilisateur afficherait des données obsolètes sans `useEffect`.

#### Comment résoudre cela avec les états dérivés

Vous pouvez résoudre tous ces re-rendus supplémentaires en utilisant des états dérivés. Ni `fullName` ni `isAdult` n'ont directement besoin d'une saisie utilisateur spécifique pour que nous connaissions leur valeur. Vous pouvez calculer leur valeur lorsque leurs états dépendants changent sans utiliser `useEffect`. De même, vous pouvez dériver l' `email` directement en utilisant la valeur de la prop à la volée.

```diff
import { useEffect, useState, type FormEventHandler } from "react";

interface DetailFormProps {
  email: string;
}

const DetailForm = ({ email }: DetailFormProps) => {
  const [lastName, setLastName] = useState("");
  const [firstName, setFirstName] = useState("");
- const [fullName, setFullName] = useState("");
  const [age, setAge] = useState(0);
- const [isAdult, setIsAdult] = useState(false);
- const [localEmail, setLocalEmail] = useState(email);

- useEffect(() => {
-   setFullName(`${firstName} ${lastName}`.trim());
- }, [firstName, lastName]);

- useEffect(() => {
-   setIsAdult(age > 18);
- }, [age]);

- useEffect(() => {
-   setLocalEmail(email);
- }, [email]);

+ const fullName = `${firstName} ${lastName}`.trim();
+ const isAdult = age > 18;

  const submitForm: FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
-   console.log({ fullName, age, isAdult, email: localEmail });
+   console.log({ fullName, age, isAdult, email });
  };
};

export default DetailForm;
```

Le formulaire stocke maintenant l'état nécessaire : `lastName`, `firstName`, et `age`. Les valeurs `fullName` et `isAdult` sont dérivées directement de leurs valeurs dépendantes.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762627041623/69004769-ddd9-470c-9212-ba7711350b57.gif align="center")

Comme vous pouvez le voir avec l'état dérivé, nous avons 0 re-rendu supplémentaire. Le formulaire ne s'est re-rendu que lorsqu'il le devait. Le formulaire s'est re-rendu une fois lorsque chaque valeur de saisie a changé, pas deux. De plus, lorsque l'e-mail change dans le composant parent, il n'y a qu'un seul re-rendu.

### Comment dériver l'état à partir d'une URL {#heading-comment-deriver-l-etat-a-partir-d-une-url}

Vous pouvez également utiliser une URL pour enregistrer des données dynamiques via des paramètres de route ou des chaînes de requête. Chaque bibliothèque de routage fournit des hooks pour accéder à ces données.

Par exemple, React Router fournit `useParams` ou `useSearchParams`. Dans la plupart des cas, les valeurs renvoyées par ces hooks n'ont pas besoin d'être replacées dans un `useState` – car cela reviendrait à suivre deux stockages, `useState` et l'URL.

Maintenant, nous allons examiner quelques exemples utilisant des paramètres de recherche de React Router. Vous verrez d'abord un exemple qui abuse de `useState` et provoque des re-rendus supplémentaires et des problèmes de synchronisation. Ensuite, vous verrez sa solution dérivée.

#### Synchronisation avec `useEffect`

Le composant que vous allez utiliser est un composant de filtre :

```typescript
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router";

const Products = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [selectedMaterial, setSelectedMaterial] = useState("");

  useEffect(() => {
    setSearchQuery(searchParams.get("search") || "");
    setSelectedCategory(searchParams.get("category") || "");
    setSelectedMaterial(searchParams.get("material") || "");
  }, [searchParams]);

  console.count("__ RENDERDED ___");

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "1rem",
      }}
    >
      <input value={searchQuery} />
      <select value={selectedCategory}>
        <option value="">All Categories</option>
        <option value="electronics">Electronics</option>
        <option value="clothing">Clothing</option>
      </select>
      <select value={selectedMaterial}>
        <option value="">All Material</option>
        <option value="leather">Leather</option>
        <option value="silk">Silk</option>
      </select>
      <button>Clear Filters</button>
    </div>
  );
};

export default Products;
```

Ce composant permet aux utilisateurs de rechercher un produit et/ou de filtrer par catégorie et matériaux. Bien qu'il semble simple, ce composant présente tous les problèmes mentionnés précédemment.

Voyons ce qui se passe lorsque le composant est monté sans filtre et avec des filtres prédéfinis.

##### Sans filtre :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762627432720/fb1ffe32-b3ae-4506-9a33-cdd42cffb5dd.gif align="center")

Le composant ne s'affiche qu'une seule fois lorsqu'il n'y a pas de filtre. C'est une bonne chose.

##### Avec un filtre prédéfini :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762627673969/3a29eb6d-694d-4499-8f78-06cd8702ae3d.gif align="center")

Il s'affiche deux fois parce que vous essayez de vous assurer que vos `useState` sont synchronisés avec l'URL en utilisant `useEffect`. Le composant s'affiche la première fois qu'il est monté, puis se re-rend à cause de la dépendance dans `useEffect`.

#### Initialisation directe de `useState`

Vous pourriez penser qu'il est préférable de déplacer les accesseurs (getters) directement dans les `useState`, ce qui résout effectivement le cas du re-rendu lors du montage du composant.

```typescript
const Products = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [searchQuery, setSearchQuery] = useState(
    searchParams.get("search") || "",
  );
  const [selectedCategory, setSelectedCategory] = useState(
    searchParams.get("category") || "",
  );
  const [selectedMaterial, setSelectedMaterial] = useState(
    searchParams.get("material") || "",
  );

  // prev code
};
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762627883127/76b4af17-a0c6-4f7d-bc40-fbf013fb2ad9.gif align="center")

Comme vous pouvez le voir, le composant ne s'affiche qu'une seule fois. Il n'y a plus de `useEffect` pour déclencher un autre re-rendu.

Gardez simplement à l'esprit que ce n'est pas encore une solution. Cela pose d'autres problèmes que vous verrez bientôt.

Que se passe-t-il lorsque l'un des filtrages change ou lorsque vous saisissez une requête de recherche ?

#### Gestion des changements

Les deux solutions montrent que vous avez des re-rendus inutiles. C'est parce que vous devez maintenir deux états synchronisés : les `useState` et l'URL.

```typescript
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router";

const Products = () => {
  // prev code

  const handleSearchChange = (query: string) => {
    setSearchQuery(query);
    setSearchParams((prev) => {
      const newParams = new URLSearchParams(prev);
      if (query) {
        newParams.set("search", query);
      } else {
        newParams.delete("search");
      }
      return newParams;
    });
  };

  const handleCategoryChange = (category: string) => {
    setSelectedCategory(category);
    setSearchParams((prev) => {
      const newParams = new URLSearchParams(prev);
      if (category) {
        newParams.set("category", category);
      } else {
        newParams.delete("category");
      }
      return newParams;
    });
  };

  const handleMaterialChange = (material: string) => {
    setSelectedMaterial(material);
    setSearchParams((prev) => {
      const newParams = new URLSearchParams(prev);
      if (material) {
        newParams.set("material", material);
      } else {
        newParams.delete("material");
      }
      return newParams;
    });
  };

  const clearFilters = () => {
    setSearchQuery("");
    setSelectedCategory("");
    setSelectedMaterial("");
    setSearchParams({});
  };

  console.count("__ RENDERDED ___");

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "1rem",
      }}
    >
      <input
        value={searchQuery}
        onChange={(e) => handleSearchChange(e.target.value)}
      />
      <select
        value={selectedCategory}
        onChange={(e) => handleCategoryChange(e.target.value)}
      >
        {/* prev options */}
      </select>
      <select
        value={selectedMaterial}
        onChange={(e) => handleMaterialChange(e.target.value)}
      >
        {/* prev options */}
      </select>
      <button onClick={clearFilters}>Clear Filters</button>
    </div>
  );
};

export default Products;
```

Parce que vous suivez les valeurs dans `useState`, vous devez d'abord mettre à jour le `useState` avant de mettre à jour l'URL. L'interface utilisateur ne sera pas mise à jour si vous mettez à jour l'URL sans mettre à jour le `useState`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762628106580/c28d2453-9faa-460d-9cfa-d000b9ed41a4.gif align="center")

Remarquez que chaque changement entraîne 2 à 3 re-rendus.

#### Utilisation de l'état dérivé

L'utilisation d'un état dérivé résoudra tous les problèmes rencontrés. Votre état peut être dérivé directement de l'URL sans utiliser `useState` et/ou `useEffect`.

```typescript
import { useSearchParams } from "react-router";

const Products = () => {
  const [searchParams, setSearchParams] = useSearchParams();

  const searchQuery = searchParams.get("search") || "";
  const selectedCategory = searchParams.get("category") || "";
  const selectedMaterial = searchParams.get("material") || "";

  const updateFilter = (key: string, value: string) => {
    setSearchParams((prev) => {
      const newParams = new URLSearchParams(prev);
      if (value) {
        newParams.set(key, value);
      } else {
        newParams.delete(key);
      }
      return newParams;
    });
  };

  const clearFilters = () => {
    setSearchParams({});
  };

  console.count("__ RENDERDED ___");

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "1rem",
      }}
    >
      <input
        value={searchQuery}
        onChange={(e) => updateFilter("search", e.target.value)}
      />
      <select
        value={selectedCategory}
        onChange={(e) => updateFilter("category", e.target.value)}
      >
        <option value="">All Categories</option>
        <option value="electronics">Electronics</option>
        <option value="clothing">Clothing</option>
      </select>
      <select
        value={selectedMaterial}
        onChange={(e) => updateFilter("material", e.target.value)}
      >
        <option value="">All Material</option>
        <option value="leather">Leather</option>
        <option value="silk">Silk</option>
      </select>
      <button onClick={clearFilters}>Clear Filters</button>
    </div>
  );
};

export default Products;
```

Vous lisez maintenant vos valeurs directement depuis l'URL. Vous ne mettez également à jour l'URL que lorsque l'une des valeurs change.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762628297681/03d0eabb-1030-4e70-83a0-11feb7f4e9e9.gif align="center")

Remarquez que vous n'avez aucun re-rendu lors du montage du composant, même avec des filtres prédéfinis. Le composant se re-rend une seule fois lorsqu'une clé de filtrage change.

Cette approche offre plusieurs avantages :

* Vous n'avez pas besoin de `useEffect` pour synchroniser les données.
    
* Vous n'avez qu'une seule source de vérité à maintenir, qui est l'URL.
    
* Vous avez moins de code, ce qui est plus facile à maintenir.
    

### Comment dériver l'état à partir de données externes {#heading-comment-deriver-l-etat-a-partir-de-donnees-externes}

Les bibliothèques de récupération de données comme React Query fournissent des états qui peuvent être utilisés comme source unique de vérité. Enregistrer ces données dans `useState` peut parfois être redondant.

Regardez cet exemple utilisant React Query. Tout d'abord, créez un composant parent qui affichera les détails de l'utilisateur :

```typescript
import { useSearchParams } from "react-router";
import UserDetail from "./user-detail";

const UserIdInput = () => {
  const [search, updateSearch] = useSearchParams();

  return (
    <input
      value={search.get("id") || ""}
      onChange={(e) => updateSearch({ id: e.target.value })}
    />
  );
};

const User = () => {
  return (
    <>
      <UserIdInput />
      <UserDetail />
    </>
  );
};

export default User;
```

Vous utilisez le `<UserIdInput />` pour mettre à jour les détails de l'utilisateur que vous devez récupérer. Maintenant, créez le composant `<UserDetail />` :

```typescript
import { useQuery } from "@tanstack/react-query";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router";

interface IUser {
  id: number;
  name: string;
}

const getUser = async (id: string) => {
  const req = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
  await new Promise((r) => setTimeout(r, 2_000));
  return req.json();
};

const UserDetail = () => {
  const [search] = useSearchParams();
  const userId = search.get("id") || "";

  const {
    data,
    isFetching,
    error: fError,
  } = useQuery<IUser>({
    queryKey: ["user", userId],
    queryFn: () => getUser(userId),
    enabled: Boolean(userId),
    refetchOnWindowFocus: false,
  });

  const [user, setUser] = useState<IUser>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setUser(undefined);
    setError(undefined);
  }, [userId]);

  useEffect(() => {
    setError(fError?.message);
    setLoading(isFetching);
    setUser(data);
  }, [data, fError, isFetching]);

  console.count("__ RENDERED __");

  console.log({ data, user, isFetching, loading, error });

  if (error) return <div>Try again later!</div>;
  if (loading) return <div>Loading...</div>;

  if (user) {
    return (
      <div>
        <p style={{ fontSize: "2rem" }}>
          {user.id}: {user.name}
        </p>
      </div>
    );
  }

  return null;
};

export default UserDetail;
```

Le composant `<UserDetail />` affiche les détails d'un utilisateur. Il récupère l'ID de l'utilisateur à partir de l'URL.

Le composant utilise la fonction `getUser` pour obtenir des données factices d'une API. Il simule un petit délai réseau en attendant deux secondes supplémentaires avec cette ligne de code :

```typescript
await new Promise((r) => setTimeout(r, 2_000));
```

Le composant utilise `useQuery` pour récupérer les données. En interne, une partie de l'état suivi par React Query comprend `data`, `isFetching`, et `error`. Mais le composant crée un autre état local pour suivre ces états de React Query.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762629782249/ac64794f-9264-4e31-989c-5ee1a7274b0e.gif align="center")

Remarquez que le composant s'affiche un total de quatre fois. Le composant se re-rend lorsque React Query et les états locaux changent. Remarquez également que les deux états sont désynchronisés à un moment donné. Par exemple, dans le troisième log, la clé `data` de React Query contenait déjà les détails de l'utilisateur, alors que l'état local `user` est toujours indéfini. Vous avez dû utiliser `useEffect` pour mettre à jour son état.

C'est encore plus intéressant lorsque le composant essaie de récupérer les détails d'un autre utilisateur.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762630953734/d1810dfd-82d9-4c6d-9c57-fa473f6438e4.gif align="center")

Le composant réagit au changement de l'ID de l'utilisateur, au changement d'état de React Query et au changement d'état local. Comme pour le problème de montage, le composant se re-rend plus qu'il n'en a besoin : il se re-rend six fois. De plus, l'état local était désynchronisé à un moment donné parce que nous devions compter sur `useEffect`.

#### Dériver directement de React Query

Vous pouvez corriger tous ces problèmes en utilisant un état dérivé comme ceci :

```typescript
import { useQuery } from "@tanstack/react-query";
import { useSearchParams } from "react-router";

interface IUser {
  id: number;
  name: string;
}

const getUser = async (id: string) => {
  const req = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
  await new Promise((r) => setTimeout(r, 2_000));
  return req.json();
};

const UserDetail = () => {
  const [search] = useSearchParams();
  const userId = search.get("id") || "";

  const {
    data: user,
    isFetching: loading,
    error,
  } = useQuery<IUser>({
    queryKey: ["user", userId],
    queryFn: () => getUser(userId),
    enabled: Boolean(userId),
  });

  console.count("__ RENDERED __");

  if (error) return <div>Try again later!</div>;
  if (loading) return <div>Loading...</div>;

  if (user) {
    return (
      <div>
        <p style={{ fontSize: "2rem" }}>
          {user.id}: {user.name}
        </p>
      </div>
    );
  }

  return null;
};

export default UserDetail;
```

React Query est désormais la source unique de vérité. Il n'y a plus de synchronisation manuelle ni de `useState` supplémentaires.

De plus, la première chose que vous remarquerez est que vous avez moins de lignes de code. Cela facilite la maintenance. Consultez le GIF ci-dessous pour voir à quelle fréquence le composant s'affiche lorsqu'il est monté.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762631232781/d2b03b52-bffe-4226-9535-5b8d5a4eca20.gif align="center")

Comme vous pouvez le voir, le composant ne se re-rend que deux fois. Une fois lors du montage initial du composant, et une autre fois lorsque l'état de React Query change.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762631500289/e87f1c5e-2741-4c2a-bf1d-9406f06812ce.gif align="center")

La même chose s'est produite lorsque vous avez récupéré les détails d'un autre utilisateur. Vous avez moins de re-rendus : trois fois contre six fois lorsque nous suivions l'état localement.

## Comment empêcher le recalcul d'un état dérivé {#heading-comment-empecher-le-recalcul-d-un-etat-derive}

La plupart des calculs sont assez rapides pour s'exécuter à chaque re-rendu. Cela devient un problème lorsqu'il s'agit d'un calcul coûteux. Dans ce cas, vous pouvez utiliser `useMemo` et/ou `memo` pour éviter un travail inutile.

```typescript
const Detail = () => {
  const product = useQuery(...);
  const users = useQuery(...);

  const result = useMemo(() => {
    const expensiveResult = ...;

    return expensiveResult;
  }, [product.data]);

  return (
    <>
      {/* some other components */}
      <Result result={result} />
    </>
  );
};

const Result = memo(({ result }: { result: number }) => {
  return <></>;
});
```

Avec `useMemo`, la variable `result` ne sera recalculée que lorsque `product.data` changera. Cela signifie que le composant `<Result />` reste le même jusqu'à ce que `product.data` change.

Vous pouvez en savoir plus ici sur [comment utiliser useMemo dans React](https://www.freecodecamp.org/news/how-to-work-with-usememo-in-react/).

## Quand utiliser `useState` {#heading-quand-utiliser-usestate}

Bien que cet article se soit concentré sur l'utilisation des états dérivés, il existe des cas où vous devez utiliser `useState`.

### Entrée contrôlée {#heading-entree-controlee}

Vous avez besoin de `useState` pour gérer la valeur de l'entrée et la maintenir synchronisée avec l'état du composant lors de la création d'une entrée contrôlée.

```typescript
import { useState, type FormEventHandler } from "react";

const ControlledInput = () => {
  const [username, setUsername] = useState("");

  const handleSubmit: FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    console.log("Submitted value:", username);
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: "flex", flexDirection: "column", gap: "1rem" }}
    >
      <div>
        <label htmlFor="username">Username:</label>
        <input
          id="username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{
            marginLeft: "1rem",
            padding: "0.5rem 0.4rem",
            border: `1px solid ${username.length < 2 ? "red" : "green"}`,
          }}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};
```

`useState` est nécessaire ici parce que :

* vous voulez suivre la valeur de l'utilisateur au fur et à mesure qu'il tape
    
* la valeur provient directement de l'interaction de l'utilisateur
    

Parce que nous suivons la valeur d'entrée avec `useState`, nous pouvons facilement valider le `username` et changer la couleur de la bordure. freeCodeCamp propose un [article qui explique ce que sont les composants contrôlés et non contrôlés.](https://www.freecodecamp.org/news/what-are-controlled-and-uncontrolled-components-in-react/)

### Changements d'état indépendants {#heading-changements-d-etat-independants}

Vous devriez utiliser `useState` lorsqu'une valeur peut changer sans dépendre d'un autre état ou de props. Par exemple, lors de l'ouverture/fermeture d'une fenêtre modale, vous avez besoin de `useState` pour suivre son état.

```typescript
import { useState } from "react";

const Modal = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div>
      <button onClick={() => setIsModalOpen(true)}>Open Modal</button>
      {isModalOpen && (
        <div>
          <p>Modal Content</p>
          <button onClick={() => setIsModalOpen(false)}>Close</button>
        </div>
      )}
    </div>
  );
};
```

## Conclusion {#heading-conclusion}

La gestion de l'état est l'une des parties les plus délicates de React. Vous ne devriez pas stocker ce que vous pouvez calculer, et vous ne devriez stocker que ce que vous ne pouvez pas dériver.

En gardant les états minimaux et en dérivant quand c'est possible, il sera plus facile de déboguer et de maintenir vos composants.