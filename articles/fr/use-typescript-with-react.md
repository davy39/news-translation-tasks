---
title: Comment utiliser TypeScript avec React
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2023-11-15T18:53:19.000Z'
originalURL: https://freecodecamp.org/news/use-typescript-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/introduction_to_typescript_with_react_cover.png
tags:
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser TypeScript avec React
seo_desc: 'In this article, you will learn how to use TypeScript with React.

  By the end, you will have a solid understanding of how to write React code with
  TypeScript.

  Want to watch the video version of this tutorial? You can check out the video below:

  https:/...'
---

Dans cet article, vous apprendrez à utiliser TypeScript avec React.

À la fin, vous aurez une solide compréhension de la façon d'écrire du code React avec TypeScript.

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter la vidéo ci-dessous :

%[https://www.youtube.com/watch?v=KmYoJmZs3sY]

## Table des matières

* [Prérequis](#heading-prealables)
* [Premiers pas](#heading-installation)
* [Bases de React et TypeScript](#heading-react-et-typescript-basics)
* [Trois façons de définir les types de props](#heading-trois-facons-de-definir-les-types-de-props)
* [Comment créer une application de liste d'utilisateurs aléatoires](#heading-comment-creer-une-application-de-liste-dutilisateurs-aleatoires)
* [Comment stocker la liste des utilisateurs dans l'état](#heading-comment-stocker-la-liste-des-utilisateurs-dans-letat)
* [Comment afficher les utilisateurs sur l'interface utilisateur](#heading-comment-afficher-les-utilisateurs-sur-linterface-utilisateur)
* [Comment créer un composant utilisateur séparé](#heading-comment-creer-un-composant-utilisateur-separe)
* [Comment créer un fichier séparé pour les déclarations de types](#heading-comment-creer-un-fichier-separe-pour-les-declarations-de-types)
* [Comment afficher un indicateur de chargement](#heading-comment-afficher-un-indicateur-de-chargement)
* [Comment charger les utilisateurs au clic sur un bouton](#heading-comment-charger-les-utilisateurs-au-clic-sur-un-bouton)
* [Comment gérer l'événement de changement](#heading-comment-gerer-levenement-de-changement)
* [Merci d'avoir lu](#heading-merci-davoir-lu)

## Prérequis

Pour suivre ce tutoriel, voici ce que vous devez avoir :

* une connaissance de base de React
* une compréhension de base de l'écriture de code TypeScript

## **Premiers pas**

Pour commencer avec TypeScript, vous devez d'abord installer TypeScript sur votre machine. Vous pouvez le faire en exécutant `npm install -g typescript` depuis le terminal ou l'invite de commande.

Maintenant, nous allons créer un projet [Vite](https://vitejs.dev/) en utilisant TypeScript.

```js
npm create vite
```

Une fois exécuté, vous serez invité à répondre à quelques questions.

Pour le nom du projet, entrez `react-typescript-demo`.

Pour le framework, sélectionnez `React`, et pour la variante, sélectionnez `TypeScript`.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/1_create_project.png)
_Créer un projet avec Vite_

Une fois que vous avez créé le projet, ouvrez-le dans VS Code et exécutez les commandes suivantes depuis le terminal :

```js
cd react-typescript-demo
npm install
```

Maintenant, faisons un peu de nettoyage de code.

Supprimez le fichier `src/App.css` et remplacez le contenu du fichier `src/App.tsx` par le contenu suivant :

```javascript
const App = () => {
  return <div>App</div>;
};

export default App;
```

Après avoir enregistré le fichier, vous pourriez voir des soulignements rouges dans le fichier comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/2_red_error.png)
_Erreur de version TypeScript_

Si vous obtenez cette erreur, appuyez simplement sur `Cmd + Shift + P (Mac)` ou `Ctrl + Shift + P (Windows/Linux)` pour ouvrir la palette de commandes de VS Code et entrez le texte `TypeScript` dans la boîte de recherche, puis sélectionnez l'option `TypeScript: Select TypeScript Version...` :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/3_version_options.png)
_Options de la palette de commandes VSCode_

Une fois sélectionné, vous verrez des options pour choisir entre la version de VS Code et la version de l'espace de travail comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/4_select_option.png)
_Sélectionner Utiliser la version de l'espace de travail_

Parmi ces options, vous devez sélectionner l'option `Utiliser la version de l'espace de travail`. Une fois que vous avez sélectionné cette option, l'erreur du fichier `App.tsx` aura disparu.

Maintenant, ouvrez le fichier `src/index.css` et remplacez son contenu par le code suivant :

```css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
```

Maintenant, lançons l'application en exécutant la commande `npm run dev`.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/5_app_started.png)
_Application démarrée_

Maintenant, cliquez sur l'URL affichée et accédez à l'application. Vous verrez l'écran initial suivant avec le texte `App` affiché dans le navigateur.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1699944017441/701358b4-4bdc-49de-b008-245ef71fc929.png)
_Application en cours d'exécution_

## Bases de React et TypeScript

Lorsque vous utilisez React avec TypeScript, la première chose que vous devez savoir est l'extension de fichier.

Chaque fichier React + TypeScript doit avoir une extension `.tsx`.

Si le fichier ne contient aucun code spécifique à JSX, vous pouvez utiliser l'extension `.ts` au lieu de l'extension `.tsx`.

Pour créer un composant dans React avec TypeScript, vous pouvez utiliser le type `FC` du package `react` et l'utiliser après le nom du composant.

Ouvrez donc le fichier `src/App.tsx` et remplacez-le par le contenu suivant :

```javascript
import { FC } from 'react';

const App: FC = () => {
  return <div>App</div>;
};

export default App;
```

Maintenant, passons quelques props à ce composant `App`.

Ouvrez `src/main.tsx` et passez une prop `title` au composant `App` comme montré ci-dessous :

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App title='TypeScript Demo' />
  </React.StrictMode>
);
```

Cependant, avec la prop `title` ajoutée, nous avons maintenant une erreur TypeScript comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/7_prop_error.png)
_Erreur de prop_

## Trois façons de définir les types de props

Nous pouvons corriger l'erreur TypeScript ci-dessus de trois manières différentes.

* Déclarer les types en utilisant une interface

L'erreur provient du fait que nous avons ajouté une prop `title` en tant que prop obligatoire pour le composant `App` – nous devons donc la mentionner à l'intérieur du composant `App`.

Ouvrez le fichier `src/App.tsx` et remplacez son contenu par le code suivant :

```javascript
import { FC } from 'react';

interface AppProps {
  title: string;
}

const App: FC<AppProps> = () => {
  return <div>App</div>;
};

export default App;
```

Comme vous pouvez le voir ci-dessus, nous avons ajouté une interface supplémentaire `AppProps` pour spécifier quelles props le composant accepte. Nous avons également utilisé l'interface `AppProps` après `FC` entre chevrons.

C'est une bonne pratique et il est recommandé de commencer le nom de l'interface par une majuscule comme `AppProps` dans notre cas.

Maintenant, avec cette modification, l'erreur TypeScript aura disparu comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/8_no_prop_error.gif)
_Ajout des types de props au composant_

C'est ainsi que nous spécifions les props qu'un composant particulier accepte.

* Déclarer les types en utilisant type

Nous pouvons également déclarer le type des props en utilisant le mot-clé `type`.

Ouvrez donc le fichier `App.tsx` et changez le code ci-dessous :

```javascript
import { FC } from 'react';

interface AppProps {
  title: string;
}

const App: FC<AppProps> = () => {
  return <div>App</div>;
};

export default App;
```

par ce code :

```javascript
import { FC } from 'react';

type AppProps = {
  title: string;
};

const App: FC<AppProps> = () => {
  return <div>App</div>;
};

export default App;
```

Ici, au lieu de la déclaration `interface`, nous avons utilisé la déclaration `type`. Maintenant, le code fonctionnera sans aucune erreur TypeScript.

C'est à vous de choisir celle que vous utilisez. J'aime toujours utiliser une interface pour déclarer les types de composants.

* Utiliser une déclaration de type en ligne

La troisième façon de déclarer un type consiste à définir des types en ligne comme montré ci-dessous :

```javascript
const App = ({ title }: { title: string }) => {
  return <div>App</div>;
};

export default App;
```

Comme vous pouvez le voir ci-dessus, nous avons supprimé l'utilisation de `FC` car elle n'est pas nécessaire, et lors de la destructuration de la prop `title`, nous avons défini son type.

Donc, parmi ces trois façons, vous pouvez utiliser celle que vous préférez. Je préfère toujours utiliser une interface avec `FC`. Ainsi, si je veux ajouter plus de props plus tard, le code ne semblera pas compliqué (ce qui arrivera si vous définissez des types en ligne).

Maintenant, utilisons la prop `title` et affichons-la sur l'interface utilisateur.

Remplacez le contenu du fichier `App.tsx` par le code suivant :

```javascript
import { FC } from 'react';

interface AppProps {
  title: string;
}

const App: FC<AppProps> = ({ title }) => {
  return <h1>{title}</h1>;
};

export default App;
```

Comme vous pouvez le voir, nous utilisons une interface avec `FC`, et nous destructurons la prop `title` et l'affichons à l'écran.

Maintenant, ouvrez le fichier `src/index.css` et ajoutez le CSS suivant à l'intérieur :

```css
h1 {
  text-align: center;
}
```

Si vous vérifiez l'application dans le navigateur, vous verrez que le titre avec le texte `TypeScript Demo` s'affiche correctement.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/10_title_displayed.png)
_Titre de l'application affiché correctement_

## Comment créer une application de liste d'utilisateurs aléatoires

Maintenant que vous avez une idée de base sur la façon de déclarer les props des composants, créons une simple application de liste d'utilisateurs aléatoires qui affichera une liste de 10 utilisateurs aléatoires à l'écran.

Pour cela, nous utiliserons l'API [Random User Generator](https://randomuser.me/).

Voici l'URL de l'API que nous utiliserons :

```javascript
https://randomuser.me/api/?results=10
```

Commençons par installer la bibliothèque npm [Axios](https://www.npmjs.com/package/axios) afin de pouvoir faire un appel API avec elle.

Exécutez la commande suivante pour installer la bibliothèque Axios :

```javascript
npm install axios
```

Une fois installée, redémarrez l'application en exécutant la commande `npm run dev`.

Maintenant, remplacez le contenu du fichier `App.tsx` par le contenu suivant :

```javascript
import axios from 'axios';
import { FC, useEffect } from 'react';

interface AppProps {
  title: string;
}

const App: FC<AppProps> = ({ title }) => {
  useEffect(() => {
    const getUsers = async () => {
      try {
        const { data } = await axios.get(
          'https://randomuser.me/api/?results=10'
        );
        console.log(data);
      } catch (error) {
        console.log(error);
      }
    };
    getUsers();
  }, []);

  return <h1>{title}</h1>;
};

export default App;
```

Comme vous pouvez le voir ci-dessus, nous avons ajouté un hook `useEffect` où nous faisons l'appel API pour obtenir la liste des utilisateurs.

Maintenant, si vous ouvrez la console dans le navigateur, vous pourrez voir la réponse de l'API affichée dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/11_api_response.png)
_Réponse de l'API_

Comme vous pouvez le voir, nous obtenons correctement une liste de 10 utilisateurs aléatoires et la liste réelle des utilisateurs provient de la propriété `results` de la réponse.

## Comment stocker la liste des utilisateurs dans l'état

Maintenant, stockons ces utilisateurs dans l'état afin de pouvoir les afficher à l'écran.

À l'intérieur du composant `App`, déclarez un nouvel état avec une valeur initiale de tableau vide comme ceci :

```javascript
const [users, setUsers ] = useState([]);
```

Et appelez la fonction `setUsers` pour stocker les utilisateurs dans le hook `useEffect` après l'appel API.

Votre composant `App` ressemblera donc à ceci maintenant :

```javascript
import axios from 'axios';
import { FC, useEffect, useState } from 'react';

interface AppProps {
  title: string;
}

const App: FC<AppProps> = ({ title }) => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const getUsers = async () => {
      try {
        const { data } = await axios.get(
          'https://randomuser.me/api/?results=10'
        );
        console.log(data);
        setUsers(data.results);
      } catch (error) {
        console.log(error);
      }
    };
    getUsers();
  }, []);

  return <h1>{title}</h1>;
};

export default App;
```

Comme vous pouvez le voir ici, nous appelons la fonction `setUsers` avec la valeur de `data.results`.

## Comment afficher les utilisateurs sur l'interface utilisateur

Maintenant, affichons le nom et l'email de chaque utilisateur à l'écran.

Si vous vérifiez la sortie de la console, vous pouvez voir qu'il y a une propriété `name` pour chaque objet qui contient le prénom et le nom de famille de l'utilisateur. Nous pouvons donc les combiner pour afficher le nom complet.

De plus, nous avons une propriété `email` directe pour chaque objet utilisateur que nous pouvons utiliser pour afficher l'email.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/12_required_properties.gif)
_Exploration de la réponse de l'API_

Remplacez donc le contenu du fichier `App.tsx` par le contenu suivant :

```javascript
import axios from 'axios';
import { FC, useEffect, useState } from 'react';

interface AppProps {
  title: string;
}

const App: FC<AppProps> = ({ title }) => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const getUsers = async () => {
      try {
        const { data } = await axios.get(
          'https://randomuser.me/api/?results=10'
        );
        console.log(data);
        setUsers(data.results);
      } catch (error) {
        console.log(error);
      }
    };
    getUsers();
  }, []);

  return (
    <div>
      <h1>{title}</h1>
      <ul>
        {users.map(({ login, name, email }) => {
          return (
            <li key={login.uuid}>
              <div>
                Nom : {name.first} {name.last}
              </div>
              <div>Email : {email}</div>
              <hr />
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default App;
```

Comme vous pouvez le voir, nous utilisons la [méthode map de tableau](https://www.youtube.com/watch?v=ffxvkWmaU7s&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=8) pour parcourir le tableau `users`, et nous utilisons la [destructuration d'objet](https://www.youtube.com/watch?v=3JsFklg1WhU&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=20) pour destructurer les propriétés `login`, `name` et `email` des objets `user` individuels. De plus, nous affichons le nom et l'email de l'utilisateur sous forme de liste non ordonnée.

Mais vous verrez quelques erreurs TypeScript dans le fichier, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/13_user_errors.png)
_Erreur TypeScript des propriétés des utilisateurs_

C'est parce que, comme vous pouvez le voir ci-dessus, par défaut TypeScript suppose que le type du tableau `users` est `never[]` – il n'est donc pas en mesure de déterminer quelles propriétés le tableau `users` contient.

Cela signifie que nous devons spécifier toutes les propriétés que nous utilisons ainsi que leurs types.

Déclarons donc une nouvelle interface après l'interface `AppProps` comme ceci :

```javascript
interface Users {
  name: {
    first: string;
    last: string;
  };
  login: {
    uuid: string;
  };
  email: string;
}
```

Ici, nous spécifions que chaque utilisateur individuel sera un objet avec les propriétés `name`, `login` et `email`. Nous spécifions également le type de données de chaque propriété.

Comme vous pouvez le voir, chaque objet `user` provenant de l'API a beaucoup d'autres propriétés comme `phone`, `location` et autres. Mais nous devons seulement spécifier les propriétés que nous utilisons dans le code.

Maintenant, changez la déclaration du tableau des utilisateurs `useState` de ceci :

```javascript
const [users, setUsers] = useState([]);
```

en ceci :

```javascript
const [users, setUsers] = useState<Users[]>([]);
```

Ici, nous spécifions que `users` est un tableau d'objets de type `Users` qui est l'interface que nous avons déclarée.

Maintenant, si vous vérifiez le fichier `App.tsx`, vous verrez qu'il n'y a pas d'erreurs TypeScript.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/14_no_type_error.png)
_Erreur des types de propriétés corrigée_

Et vous pourrez voir la liste de 10 utilisateurs aléatoires affichée à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/15_random_users.png)
_Liste des utilisateurs aléatoires affichée à l'écran_

Comme vous l'avez vu précédemment, nous avons déclaré l'interface `Users` comme ceci :

```javascript
interface Users {
  name: {
    first: string;
    last: string;
  };
  login: {
    uuid: string;
  };
  email: string;
}
```

Mais lorsque vous avez des propriétés imbriquées, vous verrez qu'elles sont écrites comme ceci :

```javascript
interface Name {
  first: string;
  last: string;
}

interface Login {
  uuid: string;
}

interface Users {
  name: Name;
  login: Login;
  email: string;
}
```

L'avantage de déclarer des interfaces séparées pour chaque propriété imbriquée est que, si vous voulez utiliser la même structure dans un autre fichier, vous pouvez simplement exporter l'une des interfaces ci-dessus et les réutiliser dans d'autres fichiers (au lieu de redéclarer la même interface).

Exportez donc toutes les interfaces ci-dessus en tant qu'[exportation nommée](https://www.youtube.com/watch?v=_5nxKhP9UOo&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=4). Le code ressemblera donc à ceci :

```javascript
export interface Name {
  first: string;
  last: string;
}

export interface Login {
  uuid: string;
}

export interface Users {
  name: Name;
  login: Login;
  email: string;
}
```

Comme je l'ai dit précédemment, vous pouvez également utiliser une déclaration de type ici au lieu d'utiliser l'interface, donc cela ressemblera à ceci :

```javascript
type Name = {
  first: string;
  last: string;
};

type Login = {
  uuid: string;
};

type Users = {
  name: Name;
  login: Login;
  email: string;
};
```

## Comment créer un composant utilisateur séparé

Lorsque nous utilisons la méthode `map` de tableau pour afficher quelque chose à l'écran, il est courant de séparer cette partie d'affichage dans un composant différent. Cela facilite les tests et rendra également votre code de composant plus court.

Créez un dossier `components` à l'intérieur du dossier `src` et créez un fichier `User.tsx` à l'intérieur. Ajoutez ensuite le contenu suivant à l'intérieur de ce fichier :

```javascript
const User = ({ login, name, email }) => {
  return (
    <li key={login.uuid}>
      <div>
        Nom : {name.first} {name.last}
      </div>
      <div>Email : {email}</div>
      <hr />
    </li>
  );
};

export default User;
```

Si vous enregistrez le fichier, vous verrez à nouveau les erreurs TypeScript.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/16_user_component_props_error.png)
_Erreur de déclaration des props du composant utilisateur_

Nous devons donc spécifier quelles props le composant `User` recevra. Nous devons également spécifier le type de données de chacune d'entre elles.

Le fichier `User.tsx` mis à jour ressemblera donc à ceci :

```javascript
import { FC } from 'react';
import { Login, Name } from '../App';

interface UserProps {
  login: Login;
  name: Name;
  email: string;
}

const User: FC<UserProps> = ({ login, name, email }) => {
  return (
    <li key={login.uuid}>
      <div>
        Nom : {name.first} {name.last}
      </div>
      <div>Email : {email}</div>
      <hr />
    </li>
  );
};

export default User;
```

Comme vous pouvez le voir ci-dessus, nous avons déclaré une interface `UserProps` ci-dessus et nous l'avons spécifiée pour le composant `User` en utilisant `FC`.

Remarquez également que nous ne déclarons pas le type de données des propriétés `name` et `login`. Au lieu de cela, nous utilisons les types exportés depuis le fichier `App.tsx` :

```javascript
import { Login, Name } from '../App';
```

C'est pourquoi il est bon de déclarer des types séparés pour chaque propriété imbriquée, afin de pouvoir les réutiliser ailleurs.

Maintenant, nous pouvons utiliser ce composant `User` à l'intérieur du fichier `App.tsx`.

Changez donc le code ci-dessous :

```javascript
{users.map(({ login, name, email }) => {
  return (
    <li key={login.uuid}>
      <div>
        Nom : {name.first} {name.last}
      </div>
      <div>Email : {email}</div>
      <hr />
    </li>
  );
})}
```

par ce code :

```javascript
{users.map(({ login, name, email }) => {
  return <User key={login.uuid} name={name} email={email} />;
})}
```

Comme vous le savez peut-être, lors de l'utilisation de la méthode `map` de tableau, nous devons fournir la `key` pour l'élément parent qui est `User` dans notre cas. Nous avons donc ajouté la prop `key` lors de l'utilisation du composant `User` comme montré ci-dessus.

Cela signifie que nous n'avons pas besoin d'une clé à l'intérieur du composant `User`, nous pouvons donc supprimer la prop `key` et `login` du composant `User`.

Le composant `User` mis à jour ressemblera donc à ceci :

```javascript
import { FC } from 'react';
import { Name } from '../App';

interface UserProps {
  name: Name;
  email: string;
}

const User: FC<UserProps> = ({ name, email }) => {
  return (
    <li>
      <div>
        Nom : {name.first} {name.last}
      </div>
      <div>Email : {email}</div>
      <hr />
    </li>
  );
};

export default User;
```

Comme vous pouvez le voir, nous avons supprimé la prop `login` de l'interface tout en la destructurant. L'application fonctionne toujours comme avant sans aucun problème, comme vous pouvez le voir ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/17_working_with_refactor.png)
_Liste des utilisateurs aléatoires affichée sur l'interface utilisateur_

## Comment créer un fichier séparé pour les déclarations de types

Comme vous pouvez le voir, le fichier `App.tsx` est devenu assez volumineux en raison des déclarations d'interfaces. Il est courant d'avoir un fichier séparé juste pour déclarer les types.

Créez donc un fichier `App.types.ts` à l'intérieur du dossier `src` et déplacez toutes les déclarations de types du composant `App` vers le fichier `App.types.ts` :

```typescript
export interface AppProps {
  title: string;
}

export interface Name {
  first: string;
  last: string;
}

export interface Login {
  uuid: string;
}

export interface Users {
  name: Name;
  login: Login;
  email: string;
}
```

Notez que nous exportons également le composant `AppProps` dans le code ci-dessus.

Maintenant, mettez à jour le fichier `App.tsx` pour utiliser ces types comme montré ci-dessous :

```javascript
import axios from 'axios';
import { FC, useEffect, useState } from 'react';
import { AppProps, Users } from './App.types';
import User from './components/User';

const App: FC<AppProps> = ({ title }) => {
  const [users, setUsers] = useState<Users[]>([]);
  
  // ...
};

export default App;
```

Comme vous pouvez le voir ci-dessus, nous importons `AppProps` et `Users` depuis le fichier `App.types` :

```javascript
import { AppProps, Users } from './App.types';
```

Et votre fichier `User.tsx` ressemblera maintenant à ceci :

```javascript
import { FC } from 'react';
import { Name } from '../App.types';

interface UserProps {
  name: Name;
  email: string;
}

const User: FC<UserProps> = ({ name, email }) => {
  return (
    <li>
      <div>
        Nom : {name.first} {name.last}
      </div>
      <div>Email : {email}</div>
      <hr />
    </li>
  );
};

export default User;
```

Comme vous pouvez le voir ci-dessus, nous importons `Name` depuis le fichier `App.types`.

```javascript
import { Name } from '../App.types';
```

## Comment afficher un indicateur de chargement

Lorsque vous faites un appel API pour afficher quelque chose, il est toujours bon d'afficher un indicateur de chargement pendant que l'appel API est en cours.

Ajoutons donc un nouvel état `isLoading` à l'intérieur du composant `App` :

```javascript
const [isLoading, setIsLoading] = useState(false);
```

Comme vous pouvez le voir, nous n'avons pas mentionné de type de données lors de la déclaration d'un état comme ceci :

```javascript
const [isLoading, setIsLoading] = useState<boolean>(false);
```

C'est parce que, lorsque nous attribuons une valeur initiale (`false` dans notre cas), TypeScript déduit automatiquement le type de données que nous allons stocker – qui est `boolean` dans notre cas.

Lorsque nous avons déclaré l'état `users`, il n'était pas clair ce que nous allions stocker simplement par la valeur initiale d'un tableau vide `[]`. Nous devions donc mentionner son type comme ceci :

```javascript
const [users, setUsers] = useState<Users[]>([]);
```

Maintenant, changez le code `useEffect` par le code ci-dessous :

```javascript
useEffect(() => {
  const getUsers = async () => {
    try {
      setIsLoading(true);
      const { data } = await axios.get(
        'https://randomuser.me/api/?results=10'
      );
      console.log(data);
      setUsers(data.results);
    } catch (error) {
      console.log(error);
    } finally {
      setIsLoading(false);
    }
  };
  getUsers();
}, []);
```

Ici, nous appelons `setIsLoading` avec une valeur de `true` avant l'appel API. À l'intérieur du bloc `finally`, nous le remettons à `false`.

Le code écrit à l'intérieur du bloc `finally` s'exécutera toujours, qu'il s'agisse d'un succès ou d'un échec. Donc, que l'appel API réussisse ou échoue, nous devons masquer le message de chargement, et nous utilisons le bloc `finally` pour y parvenir.

Maintenant, nous pouvons utiliser la valeur de l'état `isLoading` pour afficher un message de chargement à l'écran.

Après la balise `h1` et avant la balise `ul`, ajoutez le code suivant :

```javascript
{isLoading && <p>Chargement...</p>}
```

Maintenant, si vous vérifiez l'application, vous pourrez voir le message de chargement pendant que la liste des utilisateurs est en cours de chargement.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/18_loading.gif)
_Affichage de l'indicateur de chargement_

C'est donc une meilleure expérience utilisateur.

Mais si vous regardez de plus près les utilisateurs affichés, vous verrez que les utilisateurs changent une fois chargés.

Ainsi, initialement, nous voyons un ensemble de 10 utilisateurs aléatoires, mais immédiatement après, nous voyons un ensemble différent d'utilisateurs aléatoires sans recharger la page.

C'est parce que nous utilisons React version 18 (que vous pouvez vérifier dans le fichier `package.json`) et `React.StrictMode` à l'intérieur du fichier `src/main.tsx`.

Et avec la version 18 de React, lorsque nous utilisons `React.StrictMode`, chaque hook `useEffect` s'exécute deux fois même sans dépendance spécifiée.

Cela ne se produit que dans l'environnement de développement et non en production lorsque vous déployez l'application.

À cause de cela, l'appel API est fait deux fois. Puisque l'API des utilisateurs aléatoires retourne un nouvel ensemble d'utilisateurs aléatoires à chaque fois que l'API est appelée, nous définissons un ensemble différent d'utilisateurs dans le tableau `users` en utilisant l'appel `setUsers` à l'intérieur du hook `useEffect`.

C'est la raison pour laquelle nous voyons les utilisateurs changer sans rafraîchir la page.

Si vous ne voulez pas ce comportement pendant le développement, vous pouvez supprimer le `React.StrictMode` du fichier `main.tsx`.

Changez donc le code ci-dessous :

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App title='TypeScript Demo' />
  </React.StrictMode>
);
```

par ce code :

```javascript
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <App title='TypeScript Demo' />
);
```

Maintenant, si vous vérifiez l'application, vous verrez que la liste des utilisateurs ne change pas une fois qu'elle est chargée.

## Comment charger les utilisateurs au clic sur un bouton

Maintenant, au lieu de faire l'appel API au chargement de la page, ajoutons un bouton "afficher les utilisateurs" et nous ferons l'appel API lorsque nous cliquerons sur ce bouton.

Ajoutez donc un nouveau bouton après la balise `h1`, comme montré ci-dessous :

```javascript
<button onClick={handleClick}>Afficher les utilisateurs</button>
```

Maintenant, ajoutez la méthode `handleClick` à l'intérieur du composant `App` et déplacez tout le code de la fonction `getUsers` vers la méthode `handleClick` :

```javascript
const handleClick = async () => {
  try {
    setIsLoading(true);
    const { data } = await axios.get('https://randomuser.me/api/?results=10');
    console.log(data);
    setUsers(data.results);
  } catch (error) {
    console.log(error);
  } finally {
    setIsLoading(false);
  }
};
```

Maintenant, vous pouvez supprimer ou commenter le hook `useEffect`, car il n'est plus nécessaire.

Votre fichier `App.tsx` mis à jour ressemblera maintenant à ceci :

```javascript
import axios from 'axios';
import { FC, useState } from 'react';
import { AppProps, Users } from './App.types';
import User from './components/User';

const App: FC<AppProps> = ({ title }) => {
  const [users, setUsers] = useState<Users[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleClick = async () => {
    try {
      setIsLoading(true);
      const { data } = await axios.get('https://randomuser.me/api/?results=10');
      console.log(data);
      setUsers(data.results);
    } catch (error) {
      console.log(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <h1>{title}</h1>
      <button onClick={handleClick}>Afficher les utilisateurs </button>
      {isLoading && <p>Chargement...</p>}
      <ul>
        {users.map(({ login, name, email }) => {
          return <User key={login.uuid} name={name} email={email} />;
        })}
      </ul>
    </div>
  );
};

export default App;
```

Maintenant, si vous vérifiez l'application, vous verrez que les utilisateurs sont chargés uniquement lorsque vous cliquez sur le bouton afficher les utilisateurs. Nous voyons également le message de chargement.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/19_load_on_click.gif)
_Utilisateurs chargés au clic sur le bouton_

## Comment gérer l'événement de changement

Maintenant, ajoutons un champ de saisie. Lorsque nous tapons quelque chose dans ce champ de saisie, nous afficherons le texte saisi en dessous de ce champ de saisie.

Ajoutez un champ de saisie après le bouton comme ceci :

```javascript
<input type='text' onChange={handleChange} />
```

Et déclarez un nouvel état pour stocker la valeur saisie comme ceci :

```javascript
const [username, setUsername] = useState('');
```

Maintenant, ajoutez une méthode `handleChange` à l'intérieur du composant `App` comme ceci :

```javascript
 const handleChange = (event) => {
  setUsername(event.target.value);
};
```

Cependant, vous verrez que nous obtenons une erreur TypeScript pour le paramètre event.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/20_event_type.png)
_Erreur TypeScript : type d'événement manquant_

Avec TypeScript, nous devons toujours spécifier le type de chaque paramètre de fonction.

Ici, TypeScript n'est pas en mesure d'identifier le type du paramètre `event`.

Pour découvrir le type du paramètre `event`, nous pouvons changer le code ci-dessous :

```javascript
<input type='text' onChange={handleChange} />
```

par ce code :

```javascript
<input type='text' onChange={(event) => {}} />
```

Ici, nous utilisons une fonction en ligne, car lors de l'utilisation d'une fonction en ligne, le type correct est automatiquement passé au paramètre de la fonction, nous n'avons donc pas besoin de le spécifier.

Si vous survolez le paramètre `event`, vous pourrez voir le type exact d'événement que nous pouvons utiliser dans notre fonction `handleChange` comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/21_change_event_type.gif)
_Identification du type d'événement TypeScript en utilisant une fonction en ligne_

Maintenant, vous pouvez revenir au code ci-dessous :

```javascript
<input type='text' onChange={(event) => {}} />
```

par ce code :

```javascript
<input type='text' onChange={handleChange} />
```

Maintenant, affichons la valeur de la variable d'état `username` sous le champ de saisie :

```javascript
<input type='text' onChange={handleChange} />
<div>{username}</div>
```

Si vous vérifiez l'application maintenant, vous pourrez voir le texte saisi affiché sous le champ de saisie.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/22_username.gif)
_Affichage du texte saisi par l'utilisateur sur l'interface utilisateur_

## **Merci d'avoir lu**

C'est tout pour ce tutoriel. J'espère que vous avez beaucoup appris.

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter [cette vidéo](https://www.youtube.com/watch?v=KmYoJmZs3sY).

Vous pouvez trouver le code source complet de cette application dans [ce dépôt](https://github.com/myogeshchavan97/react-typescript-demo).

Si vous voulez maîtriser JavaScript, ES6+, React et Node.js avec un contenu facile à comprendre, consultez ma [chaîne YouTube](https://www.youtube.com/@codingmastery_dev/). N'oubliez pas de vous abonner.

Vous voulez rester à jour avec du contenu régulier sur JavaScript, React et Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

[![Apprenez à créer une application de gestion des dépenses en utilisant React et TypeScript](https://www.freecodecamp.org/news/content/images/2023/11/expense_manager_app_banner.png)](https://courses.yogeshchavan.dev/build-expense-manager-app-using-react-and-typescript)