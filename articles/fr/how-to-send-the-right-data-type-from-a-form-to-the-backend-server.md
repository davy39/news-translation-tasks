---
title: Comment convertir la valeur par défaut de react-dropdown-select d'un tableau
  en chaîne de caractères
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-10T21:30:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-the-right-data-type-from-a-form-to-the-backend-server
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/1641660058245.jpg
tags:
- name: forms
  slug: forms
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment convertir la valeur par défaut de react-dropdown-select d'un tableau
  en chaîne de caractères
seo_desc: "By Caleb Olojo\nWeb forms play an important role on many sites on the internet,\
  \ and they're something you should know how to build as a web developer. \nFrom\
  \ good ol' login forms to signup forms and survey forms (or whatever they're called\
  \ these days),..."
---

Par Caleb Olojo

Les formulaires web jouent un rôle important sur de nombreux sites internet, et c'est quelque chose que vous devez savoir construire en tant que développeur web. 

Des bons vieux formulaires de connexion aux formulaires d'inscription et aux formulaires d'enquête (ou quel que soit leur nom ces jours-ci), leur principal objectif est de recevoir des données et de les envoyer à un serveur backend où elles sont stockées.

Dans cet article, nous allons voir comment convertir les données obtenues à partir d'un formulaire d'un type à un autre avec JavaScript. Mais avant de lire cet article plus avant, vous devriez comprendre les éléments suivants :

* Les bases de React.js
* Comment préserver l'état du formulaire dans React.js
* Comment créer des composants d'entrée contrôlés

De plus, dans cet article, nous aborderons :

* Comment envoyer les données du formulaire que vous obtenez à un serveur backend via une API
* Comment obtenir la valeur exacte d'une étiquette dans le tableau `options` du package react-dropdown-select.

Maintenant que vous savez ce dont vous avez besoin pour commencer avec cet article, plongeons-nous dedans.

## Installation

Nous allons construire un formulaire simple avec React dans cet article afin de comprendre comment le processus fonctionne. Pour cela, nous allons utiliser [Next.js](https://nextjs.org) pour démarrer notre application. Si vous êtes nouveau dans Next.js, vous pouvez consulter leur documentation [ici](https://nextjs.org/docs/getting-started).

Maintenant, obtenons toutes les dépendances dont nous aurons besoin dans ce projet. Puisqu'il s'agit d'un projet Next.js, commençons par configurer une application next-app :

```
npx create-next-app nom-de-votre-application

```

La commande ci-dessus installera toutes les dépendances importantes dont nous avons besoin dans une fonction d'application Next.js. Les dépendances suivantes dont nous avons besoin dans ce projet sont :

* **axios** pour la récupération de données, et
* **styled-components** pour styliser l'application.

La commande ci-dessous fait cela pour nous :

```
npm install styled-components react-dropdown-select axios --save-dev

```

Une structure typique de projet Next.js est différente de celle de [create-react-app](https://create-react-app.dev). Pour garder cet article concis, nous ne passerons pas en revue toute la structure de l'application – nous nous concentrerons uniquement sur ce qui nous concerne.

Cela dit, jetons un coup d'œil à la structure de l'application ci-dessous :

```
|__pages
|   |-- _app.js
|   |-- index.js
|__src
|   |__components
|   |    |__role
|   |    |   |__style
|   |    |     |-- role.styled.js
|   |    |__index.js        
|   |
|   |__containers
|   |    |__dropdown-select 
|   |        |-- index.js
|   
|__
```

## Aperçu de la structure de l'application

Dans la dernière section, nous avons obtenu les dépendances requises pour ce projet. Dans cette section, nous allons examiner la structure du projet et la fonction que chaque fichier performs.

Le répertoire pages est l'endroit où tout le routage de l'application a lieu. Il s'agit d'une fonctionnalité prête à l'emploi de Nextjs. Elle vous évite le stress de coder en dur vos routes indépendantes.

`pages/api` : ce répertoire API vous permet d'avoir un backend pour votre application Next.js, dans le même code source. Cela signifie que vous n'avez pas à passer par la méthode courante de création de dépôts séparés pour vos API REST ou GraphQL et de les déployer sur des plateformes d'hébergement backend comme Heroku, et ainsi de suite.

Avec le répertoire API, chaque fichier est traité comme un point de terminaison API. Si vous regardez le dossier API, vous remarquerez que nous avons un fichier appelé user.js. Ce fichier devient un point de terminaison, ce qui signifie qu'un appel API peut être effectué en utilisant le chemin vers le fichier comme URL de base.

`pages/_app.js` est l'endroit où tous nos composants sont attachés au DOM. Si vous regardez la structure des composants, vous verrez que tous les composants sont passés en tant que pageProps aux props du composant également.

C'est comme le fichier index.js lors de l'utilisation de Create-React-App. La seule différence ici est que vous n'accrochez pas votre application au nœud DOM appelé "root".

```javascript
React.render(document.getElementById("root"), <App />)
```

`index.js` est la route par défaut dans le dossier pages. C'est là que nous ferons la majeure partie du travail dans ce projet. Lorsque vous exécutez la commande ci-dessous, elle démarre un serveur de développement et le contenu de index.js est rendu sur la page web.

`components/role` est le fichier de composant qui abrite le composant de sélection déroulante et son style.

Et enfin, `containers/dropdown-select` est l'endroit où nous construisons le composant de formulaire.

## Comment construire le formulaire et gérer l'état

Maintenant que nous avons vu certaines des fonctions de base des dossiers/fichiers dans l'application, commençons à construire le composant de formulaire. Nous ne nous concentrerons pas sur l'écriture des styles dans cet article.

L'extrait de code ci-dessous montre la structure de base du composant de formulaire sans les variables d'état. Nous allons adopter une approche étape par étape pour comprendre ce qui se passe dans l'extrait.

```javascript
import React from "react";
import styled from "styled-components";
import { InputGroup } from "../../components/role/style/role.styled";
import Role from "../../components/role";
import axios from "axios";

const AuthForm = styled.form`
	...
`;

const DropDownSelect = () => {
  return (
    <AuthForm onSubmit="">
      <h2>Créer un compte...</h2>
      <InputGroup>
        <label htmlFor="email">Adresse email</label>
        <input
          name="email"
          id="email"
          type="email"
          placeholder="Entrez l'adresse email"
          className="inputs"
        />
      </InputGroup>
      <InputGroup>
        <label htmlFor="password">Créer un mot de passe</label>
        <input
          name="password"
          id="password"
          type="password"
          placeholder="Créer un mot de passe"
          className="inputs"
        />
      </InputGroup>
      <Role />
   </AuthForm>
  );
};

export default DropDownSelect;

```

Le composant ci-dessus n'a aucun moyen de suivre l'entrée que l'utilisateur tape dans les champs de formulaire, et nous ne voulons pas cela. Pour résoudre ce problème, nous utiliserons le hook `useState()` de React pour surveiller l'état.

Commençons par créer les variables d'état. Vous remarquerez que nous avons trois champs d'entrée dans le composant, ce qui signifie que nous devrons créer trois variables d'état.

```js
 const [email, setEmail] = React.useState("");
 const [password, setPassword] = React.useState("");
 const [role, setRole] = React.useState();
```

Mais nous avons besoin d'un moyen de suivre l'état des données que nous envoyons au serveur backend, donc nous avons besoin d'une autre variable d'état pour surveiller le statut de notre requête de récupération de données asynchrone (POST).

Un modèle très populaire dans l'écosystème React est de créer un composant de chargement qui indiquera ce processus.

```js
const [loading, setLoading] = React.useState(false);
```

Maintenant que nous avons cela en place, nous pouvons configurer nos champs d'entrée pour qu'ils soient contrôlés à l'aide de la propriété `onChange()`.

```js
<input
  name="email"
  id="email"
  type="email"
  placeholder="Entrez l'adresse email"
  className="inputs"
  value={email}
  onChange={(e) => setEmail(e.target.value)}
/>
```

Le processus est ensuite répété pour les champs d'entrée restants. Mais il y a un piège. Vous remarquerez que nous avons déjà importé le composant `<Role />` et que nous avons déjà passé certaines propriétés prédéfinies au composant. Jetons un coup d'œil au composant lui-même avant d'aller plus loin.

## Le composant Role

Ce composant utilise le package `react-dropdown-select` pour sa fonctionnalité, il prend un tableau de valeurs dans ses propriétés.

La propriété minimale requise est la propriété `options` qui reçoit un tableau d'objets avec des clés `label` et `value`.

```js
const options = [
   { label: "Manager", value: "Manager" },
   { label: "Worker", value: "Worker" }
]

```

Jetons un coup d'œil au composant ci-dessous :

```javascript
import React from "react";
import { InputGroup } from "./style/role.styled";
import Select from "react-dropdown-select";
import propTypes from "prop-types";

const Role = ({ userRole, roleChange }) => {
  const options = [
    { label: "Worker", value: "Worker" },
    { label: "Manager", value: "Manager" },
  ];

  return (
    <React.Fragment>
      <InputGroup>
        <label htmlFor="fullname">Rôle</label>
        <Select
          value={userRole}
          options={options}
          placeholder="Veuillez sélectionner votre rôle"
          required={true}
          dropdownPosition="top"
          className="select"
          color="#ff5c5c"
          onChange={roleChange}
        />
      </InputGroup>
    </React.Fragment>
  );
};

export default Role;

Role.propTypes = {
  ...
};

```

J'ai mentionné précédemment que le composant `<Role />` a ses propres propriétés personnalisées, et vous pouvez voir cela ci-dessus.

Le composant prend deux propriétés : `userRole` qui suit l'entrée en fonction de l'option que l'utilisateur sélectionne, et la propriété `roleChange` qui est passée en tant que valeur à la propriété `onChange()` du composant `<Select />`.

Le composant `<Select />` a diverses propriétés que vous pouvez lui passer. De la propriété `dropdownPosition` qui spécifie où le menu des options est positionné sur la page, à la propriété `color` qui affecte le style des éléments dans le menu des options, et ainsi de suite. Vous pouvez consulter certaines d'entre elles [ici](https://www.npmjs.com/package/react-dropdown-select).

Nous avons fait une instruction d'importation qui apporte le module `"prop-types"` de React en haut du fichier de ce composant. Nous allons utiliser ce module pour valider le type de données qui est passé dans ce composant.

```javascript
Role.propTypes = {
  userRole: propTypes.array.isRequired,
  roleChange: propTypes.func.isRequired,
};
```

Dans l'extrait ci-dessus, nous avons indiqué que le type de données qui sera passé dans `userRole` en tant que valeur doit être d'un type de données de tableau JavaScript et que `roleChange` doit être une fonction. Tout autre chose que cela entraînera une erreur.

## Comment utiliser le composant Role

Maintenant que nous avons passé en revue le composant `<Role />` et appris comment il fonctionne, jetons un coup d'œil à la façon dont nous pouvons l'utiliser dans l'application ci-dessous :

```javascript
import React from "react";
import styled from "styled-components";
import { InputGroup } from "../../components/role/style/role.styled";
import Role from "../../components/role";

const AuthForm = styled.form`
 ...  
`;

const DropDownSelect = () => {
  const [role, setRole] = React.useState();
  
  return (
    <AuthForm onSubmit={handleSignUp}>
      <h2>Créer un compte...</h2>
      // détails précédents    
      <Role
        userRole={role}
        roleChange={(role) => setRole(role.map((role) => role.value))}
      />
   </AuthForm>
  );
};

export default DropDownSelect;

```

L'extrait ci-dessus montre comment le composant `<Role />` est utilisé. Vous pouvez voir les propriétés personnalisées en utilisation également. `userRole` est assigné à la valeur d'état `role`.

Vous vous êtes peut-être demandé pourquoi nous n'avons pas assigné de valeur à la valeur d'état `role` lorsque nous l'avons déclarée. Eh bien, c'est parce que le composant `<Select />` de **react-dropdown-select** a une valeur de type de données par défaut d'un tableau, donc il n'est pas nécessaire de définir un tableau dans le hook `useState()`.

La propriété `roleChange` semble totalement différente de la manière dont nous avons utilisé la propriété **onChange** dans les champs d'entrée. Ici, nous avons dû placer les éléments dont nous avions besoin dans un tableau séparé, afin de pouvoir obtenir les données exactes lorsque l'utilisateur sélectionne une option.

```javascript
roleChange={(role) => setRole(role.map((role) => role.value))}
```

Si vous vous souvenez, nous avions un tableau appelé `options` qui avait des paires clé-valeur de `label` et `value`. L'extrait ci-dessus nous aide à placer la clé `value` dans un tout nouveau tableau puisque c'est ce dont nous avons besoin, et cela est possible avec la méthode intégrée `map()` de JavaScript.

Lorsque l'utilisateur clique sur une option, nous obtiendrons un tableau contenant uniquement l'élément qui a été sélectionné. Par exemple, si l'utilisateur clique sur l'option "Worker", la valeur qui est stockée dans l'état du formulaire est : `['Worker']`.

Mais nous ne voulons pas que ce type de données soit envoyé au serveur – nous voulons une chaîne de caractères à la place. Comment pouvons-nous résoudre cela, pourriez-vous demander ? Nous verrons comment nous pouvons faire cela dans la section suivante.

## Comment envoyer les données du formulaire au serveur

Dans les sections précédentes, nous avons appris la structure d'une application Next.js et comment construire et gérer l'état dans un formulaire React.

Dans cette section, nous allons envoyer les données que nous avons obtenues à partir du formulaire au serveur backend via une API.

```javascript
import React from "react";
import styled from "styled-components";
import { InputGroup } from "../../components/role/style/role.styled";
import Role from "../../components/role";
import axios from "axios";

const AuthForm = styled.form`
  ...
`;

const DropDownSelect = () => {
  ...
  const [loading, setLoading] = React.useState(false);

  const handleSignUp = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const response = await axios({
        method: "POST",
        url: "https://your-api-endpoint.com",
        data: {
          email,
          password,
          role: role.toString(),
        },
        headers: {
          "Content-Type": "application/json",
        },
      });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <AuthForm onSubmit={handleSignUp}>
      <h2>Créer un compte...</h2>
	  // champs de formulaire
      <button className="btn">{loading ? "Enregistrement" : "S'inscrire"}</button>
    </AuthForm>
  );
};

export default DropDownSelect;
```

Nous allons nous concentrer sur la fonction d'appel de données asynchrone, `handleSignup`, que nous allons utiliser pour envoyer les données au serveur via le point de terminaison de l'API.

```javascript
const handleSignUp = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const response = await axios({
        method: "POST",
        url: "https://your-api-endpoint.com",
        data: {
          email,
          password,
          role: role.toString(),
        },
        headers: {
          "Content-Type": "application/json",
        },
      });
    } catch (error) {
      console.log(error);
    }
  };
```

La valeur initiale de l'état `loading` était définie sur `false`, mais dans le bloc `try`, elle est `true`. Cela signifie que si l'appel de données asynchrone est en cours, la valeur de chargement doit être `true`. Sinon, elle doit être `false`.

Nous avons mentionné précédemment que nous ne voulons pas envoyer un type de données de tableau comme valeur d'entrée au serveur. Au lieu de cela, nous voulons une chaîne de caractères. Nous faisons cela en utilisant la méthode native de chaîne de caractères [`toString()`] de JavaScript pour transformer ce type de données.

```javascript
data: {
  role: role.toString()
}
```

La valeur de l'état `loading` peut être vue en action ci-dessous. Nous utilisons un opérateur ternaire pour vérifier si la variable d'état de chargement est vraie. Si oui, le texte dans le bouton sera **"Enregistrement"**. Si non, le texte reste inchangé.

```javascript
<button className="btn">{loading ? "Enregistrement" : "S'inscrire"}</button>
```

Vous pouvez jouer avec l'extrait ci-dessous pour confirmer si le résultat est exact ou non.

```javascript
const options = [
   { label: "Worker", value: "Worker" },
   { label: "Manager", value: "Manager" }
]

// créer un nouveau tableau avec la paire clé-valeur que vous voulez
const mappedOptions = options.map(option => option.value)
console.log(mappedOptions) // ['Worker', 'Manager']

// convertir le tableau d'options mappées en une valeur de chaîne de caractères
const mappedOptionsToString = mappedOptions.toString()
console.log(mappedOptionsToString)
```

## Conclusion

Si votre API backend vous permet d'envoyer un type de données de tableau comme valeur d'un champ d'entrée, vous pouvez utiliser ce que vous avez appris ici, car le package react-dropdown-select vous permet de le faire.

Mais dans les scénarios où la valeur requise de votre champ d'entrée est une chaîne de caractères, vous pouvez envisager d'utiliser la méthode native `toString()` de JavaScript comme vous le souhaitez.

Voici le [lien](https://exdemo.netlify.app/demo/dropdown) vers l'application de démonstration déployée et un GIF qui vous montre à quoi elle ressemble avec tous les styles appliqués :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/ezgif.com-gif-maker--1-.gif)

Merci d'avoir lu cet article. Si vous l'avez trouvé utile, veuillez le partager avec vos pairs.