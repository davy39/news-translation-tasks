---
title: Comment construire un clone de la fonctionnalité de recherche de fichiers de
  GitHub
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2020-07-14T08:06:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-clone-of-githubs-file-search-functionality
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99b8740569d1a4ca2159.jpg
tags:
- name: GitHub
  slug: github
- name: React
  slug: react
seo_title: Comment construire un clone de la fonctionnalité de recherche de fichiers
  de GitHub
seo_desc: 'In this article, we will build a project that mimics the lesser known but
  awesome file search functionality provided by GitHub.

  To see how it works, go to any GitHub repository and press the letter t which will
  land you in search view. Then you can s...'
---

Dans cet article, nous allons construire un projet qui imite la fonctionnalité de recherche de fichiers moins connue mais géniale fournie par GitHub.

Pour voir comment cela fonctionne, allez dans n'importe quel dépôt GitHub et appuyez sur la lettre **t** qui vous amènera à la vue de recherche. Ensuite, vous pouvez rechercher et faire défiler la liste simultanément comme montré dans le gif ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Github_Search-1.gif)
_Fonctionnalité de recherche de fichiers GitHub_

En construisant cette application, vous apprendrez les éléments suivants :

* Comment créer une interface utilisateur similaire à un dépôt GitHub
* Comment travailler avec les événements clavier dans React
* Comment travailler avec la navigation en utilisant les touches fléchées de votre clavier
* Comment mettre en surbrillance le texte correspondant lors de la recherche
* Comment ajouter des icônes dans React
* Comment rendre le contenu HTML dans une expression JSX

Et bien plus encore.

Vous pouvez voir la démonstration en direct de l'application [ici](https://github-file-search-react.netlify.app/).

### **Commençons**

Créez un nouveau projet en utilisant `create-react-app` :

```
create-react-app github-file-search-react
```

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez les fichiers `index.js`, `App.js` et `styles.scss` à l'intérieur du dossier `src`. Créez également les dossiers `components` et `utils` à l'intérieur du dossier `src`.

Installez les dépendances nécessaires :

```js
yarn add moment@2.27.0 node-sass@4.14.1 prop-types@15.7.2 react-icons@3.10.0
```

Ouvrez `styles.scss` et ajoutez le contenu de [ici](https://github.com/myogeshchavan97/github-file-search-react/blob/master/src/styles.scss) à l'intérieur.


Créez un nouveau fichier `Header.js` dans le dossier `components` avec le contenu suivant :

```
import React from 'react';

const Header = () => <h1 className="header">Recherche de fichiers GitHub</h1>;

export default Header;
```

Créez un nouveau fichier `api.js` dans le dossier `utils` et ajoutez le contenu de [ici](https://github.com/myogeshchavan97/github-file-search-react/blob/master/src/utils/api.js) à l'intérieur.


Dans ce fichier, nous avons créé des données statiques à afficher sur l'interface utilisateur pour garder l'application simple et facile à comprendre.

Créez un nouveau fichier `ListItem.js` dans le dossier `components` avec le contenu suivant :

```javascript
import React from 'react';
import moment from 'moment';
import { AiFillFolder, AiOutlineFile } from 'react-icons/ai';

const ListItem = ({ type, name, comment, modified_time }) => {
  return (
    <React.Fragment>
      <div className="list-item">
        <div className="file">
          <span className="file-icon">
            {type === 'folder' ? (
              <AiFillFolder color="#79b8ff" size="20" />
            ) : (
              <AiOutlineFile size="18" />
            )}
          </span>
          <span className="label">{name}</span>
        </div>
        <div className="comment">{comment}</div>
        <div className="time" title={modified_time}>
          {moment(modified_time).fromNow()}
        </div>
      </div>
    </React.Fragment>
  );
};

export default ListItem;
```

Dans ce fichier, nous prenons les données de chaque fichier que nous voulons afficher et nous affichons l'icône de dossier/fichier, le nom du fichier, les commentaires et la dernière fois que le fichier a été modifié.

Pour afficher les icônes, nous allons utiliser la bibliothèque npm `react-icons`. Elle a un site vraiment sympa qui vous permet de rechercher et d'utiliser facilement les icônes dont vous avez besoin. Consultez-le [ici](https://react-icons.github.io/react-icons/).

Le composant d'icônes accepte les props `color` et `size` pour personnaliser l'icône que nous avons utilisée dans le code ci-dessus.

Créez un nouveau fichier appelé `FilesList.js` dans le dossier `components` avec le contenu suivant :

```javascript
import React from 'react';
import ListItem from './ListItem';

const FilesList = ({ files }) => {
  return (
    <div className="list">
      {files.length > 0 ? (
        files.map((file, index) => {
          return <ListItem key={file.id} {...file} />;
        })
      ) : (
        <div>
          <h3 className="no-result">Aucun fichier correspondant trouvé</h3>
        </div>
      )}
    </div>
  );
};

export default FilesList;
```

Dans ce fichier, nous lisons les données statiques du fichier `api.js` puis nous affichons chaque élément du tableau de fichiers en utilisant la méthode map du tableau.

Ouvrez maintenant le fichier `src/App.js` et ajoutez le code suivant à l'intérieur :

```js
import React from 'react';
import Header from './components/Header';
import FilesList from './components/FilesList';
import files from './utils/api';

export default class App extends React.Component {
  state = {
    filesList: files
  };

  render() {
    const { counter, filesList } = this.state;

    return (
      <div className="container">
        <Header />
        <FilesList files={filesList} />
      </div>
    );
  }
}
```

Dans ce fichier, nous avons ajouté un état pour stocker les données de fichiers statiques que nous pouvons modifier chaque fois que nous devons le faire. Ensuite, nous l'avons passé au composant `FilesList` pour l'afficher sur l'interface utilisateur.

Ouvrez maintenant le fichier `index.js` et ajoutez le code suivant à l'intérieur :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.scss';

ReactDOM.render(<App />, document.getElementById('root'));
```

Maintenant, démarrez votre application en exécutant la commande `yarn start` depuis le terminal ou l'invite de commande et vous verrez l'écran initial suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/initial_screen.png)
_Écran initial_

Vous pouvez trouver le code jusqu'à ce point dans [cette branche](https://github.com/myogeshchavan97/github-file-search-react/tree/initial_code).

## Ajouter une fonctionnalité de recherche de base <br /> <br/>

Maintenant, ajoutons la fonctionnalité qui change l'interface utilisateur et nous permet de rechercher des fichiers lorsque nous appuyons sur la lettre **t** de notre clavier.

À l'intérieur du dossier `utils`, créez un nouveau fichier appelé `keyCodes.js` avec le contenu suivant :

```js
export const ESCAPE_CODE = 27;
export const HOTKEY_CODE = 84; // code de la touche t
export const UP_ARROW_CODE = 38;
export const DOWN_ARROW_CODE = 40;
```

Créez un nouveau fichier appelé `SearchView.js` dans le dossier `components` avec le contenu suivant :

```js
import React, { useState, useEffect, useRef } from 'react';

const SearchView = ({ onSearch }) => {
  const [input, setInput] = useState('');
  const inputRef = useRef();

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  const onInputChange = (event) => {
    const input = event.target.value;
    setInput(input);
    onSearch(input);
  };

  return (
    <div className="search-box">
      Mon dépôt <span className="slash">/</span>
      <input
        type="text"
        name="input"
        value={input}
        ref={inputRef}
        autoComplete="off"
        onChange={onInputChange}
      />
    </div>
  );
};

export default SearchView;
```

Nous utilisons ici les React Hooks pour notre état et nos méthodes de cycle de vie. Si vous êtes nouveau dans les React Hooks, consultez [cet article](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe) pour une introduction.

Dans ce fichier, nous avons d'abord déclaré un état pour stocker l'entrée tapée par l'utilisateur. Ensuite, nous avons ajouté une `ref` en utilisant le Hook `useRef` afin de pouvoir nous concentrer sur le champ d'entrée lorsque le composant est monté.

```js
const inputRef = useRef();

useEffect(() => {
  inputRef.current.focus();
}, []);

...

<input
    type="text"
    name="input"
    value={input}
    ref={inputRef}
    autoComplete="off"
    onChange={onInputChange}
  />
```

Dans ce code, en passant le tableau vide `[]` comme deuxième argument au hook `useEffect`, le code à l'intérieur du hook `useEffect` ne sera exécuté qu'une seule fois lorsque le composant est monté. Cela agit comme la méthode de cycle de vie `componentDidMount` dans les composants de classe.

Ensuite, nous avons assigné la `ref` au champ d'entrée comme `ref={inputRef}`. Lors du changement du champ d'entrée à l'intérieur du gestionnaire `onInputChange`, nous appelons la méthode `onSearch` passée en tant que prop au composant depuis le fichier `App.js`.

Ouvrez maintenant `App.js` et remplacez son contenu par le code suivant :

```js
import React from 'react';
import Header from './components/Header';
import FilesList from './components/FilesList';
import SearchView from './components/SearchView';
import { ESCAPE_CODE, HOTKEY_CODE } from './utils/keyCodes';
import files from './utils/api';

export default class App extends React.Component {
  state = {
    isSearchView: false,
    filesList: files
  };

  componentDidMount() {
    window.addEventListener('keydown', this.handleEvent);
  }

  componentWillUnmount() {
    window.removeEventListener('keydown', this.handleEvent);
  }

  handleEvent = (event) => {
    const keyCode = event.keyCode || event.which;

    switch (keyCode) {
      case HOTKEY_CODE:
        this.setState((prevState) => ({
          isSearchView: true,
          filesList: prevState.filesList.filter((file) => file.type === 'file')
        }));
        break;
      case ESCAPE_CODE:
        this.setState({ isSearchView: false, filesList: files });
        break;
      default:
        break;
    }
  };

  handleSearch = (searchTerm) => {
    let list;
    if (searchTerm) {
      list = files.filter(
        (file) =>
          file.name.toLowerCase().indexOf(searchTerm.toLowerCase()) > -1 &&
          file.type === 'file'
      );
    } else {
      list = files.filter((file) => file.type === 'file');
    }

    this.setState({
      filesList: list
    });
  };

  render() {
    const { isSearchView, filesList } = this.state;

    return (
      <div className="container">
        <Header />
        {isSearchView ? (
          <div className="search-view">
            <SearchView onSearch={this.handleSearch} />
            <FilesList files={filesList} isSearchView={isSearchView} />
          </div>
        ) : (
          <FilesList files={filesList} />
        )}
      </div>
    );
  }
}
```

Maintenant, redémarrez l'application en exécutant à nouveau la commande `yarn start` et vérifiez son fonctionnement.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/search.gif)
_Fonctionnalité de recherche initiale_

Comme vous pouvez le voir, initialement tous les dossiers et fichiers sont affichés. Ensuite, lorsque nous appuyons sur la lettre `t` du clavier, la vue change pour nous permettre de rechercher parmi les fichiers affichés.

Maintenant, comprenons le code du fichier `App.js`.

Dans ce fichier, nous avons d'abord déclaré `isSearchView` comme variable d'état. Ensuite, à l'intérieur des méthodes de cycle de vie `componentDidMount` et `componentWillUnmount`, nous ajoutons et supprimons le gestionnaire d'événements `keydown`, respectivement.

Ensuite, à l'intérieur de la fonction `handleEvent`, nous vérifions quelle touche est pressée par l'utilisateur.

- Si l'utilisateur presse la touche t, alors nous définissons l'état `isSearchView` sur `true` et mettons à jour le tableau d'état `filesList` pour inclure uniquement les fichiers et exclure les dossiers.
- Si l'utilisateur presse la touche échap, alors nous définissons l'état `isSearchView` sur `false` et mettons à jour le tableau d'état `filesList` pour inclure tous les fichiers et dossiers.

La raison pour laquelle nous déclarons `HOTKEY_CODE` et `ESCAPE_CODE` dans des fichiers séparés (`keyCodes.js` au lieu d'utiliser directement le code clé comme `84`) est que plus tard, si nous voulons changer le raccourci de `t` à `s`, alors nous devons simplement changer le code clé dans ce fichier. Il reflétera le changement dans tous les fichiers où il est utilisé sans avoir besoin de le changer dans chaque fichier.

Maintenant, comprenons la fonction `handleSearch`. Dans cette fonction, nous vérifions si l'utilisateur a entré quelque chose dans la boîte de recherche d'entrée et filtrons ensuite le ou les noms de fichiers correspondants qui incluent ce terme de recherche. Ensuite, nous mettons à jour l'état avec le ou les résultats filtrés.

Ensuite, à l'intérieur de la méthode render, en fonction de la valeur `isSearchView`, nous affichons soit la vue de la liste des fichiers, soit la vue de recherche à l'utilisateur.

Vous pouvez trouver le code jusqu'à ce point dans [cette branche](https://github.com/myogeshchavan97/github-file-search-react/tree/switching_view).

## Ajouter une fonctionnalité pour naviguer entre les fichiers <br /> <br />

Maintenant, ajoutons la fonctionnalité pour afficher une flèche devant le fichier actuellement sélectionné lors de la navigation dans la liste des fichiers.

Créez un nouveau fichier appelé `InfoMessage.js` dans le dossier `components` avec le contenu suivant :


```js
import React from 'react';

const InfoMessage = () => {
  return (
    <div className="info-message">
      Vous avez activé le <em>recherche de fichiers</em>. Commencez à taper pour filtrer la liste des fichiers. Utilisez <span className="navigation"> 2191</span> et{' '}
      <span className="navigation"> 2193</span> pour naviguer,{' '}
      <span className="navigation">esc</span> pour quitter.
    </div>
  );
};

export default InfoMessage;
```

Maintenant, ouvrez le fichier `App.js` et importez le composant `InfoMessage` pour l'utiliser :

```js
import InfoMessage from './components/InfoMessage';
```

Ajoutez une nouvelle variable d'état appelée `counter` avec la valeur initiale de `0`. Cela permet de suivre l'index de la flèche.

À l'intérieur du gestionnaire `handleEvent`, obtenez les valeurs `filesList` et `counter` de l'état :


```js
const { filesList, counter } = this.state;
```

Ajoutez deux nouveaux cas de commutation :

```js
case UP_ARROW_CODE:
  if (counter > 0) {
    this.setState({ counter: counter - 1 });
  }
  break;
case DOWN_ARROW_CODE:
  if (counter < filesList.length - 1) {
    this.setState({ counter: counter + 1 });
  }
  break;
```

Ici, nous décrémentons la valeur d'état `counter` lorsque nous appuyons sur la flèche vers le haut du clavier et incrémentons lorsque nous appuyons sur la flèche vers le bas.

Importons également les constantes de tableau haut et bas en haut du fichier :

```js
import {
  ESCAPE_CODE,
  HOTKEY_CODE,
  UP_ARROW_CODE,
  DOWN_ARROW_CODE
} from './utils/keyCodes';
```

À l'intérieur de la fonction `handleSearch`, réinitialisez l'état `counter` à `0` à la fin de la fonction afin que la flèche s'affiche toujours pour le premier fichier de la liste lors du filtrage de la liste des fichiers.

```js
this.setState({
  filesList: list,
  counter: 0
});
```

Modifiez la méthode render pour afficher le composant `InfoMessage` et passez `counter` et `isSearchView` en tant que props au composant `FilesList` :

```js
render() {
  const { isSearchView, counter, filesList } = this.state;

  return (
    <div className="container">
      <Header />
      {isSearchView ? (
        <div className="search-view">
          <SearchView onSearch={this.handleSearch} />
          <InfoMessage />
          <FilesList
            files={filesList}
            isSearchView={isSearchView}
            counter={counter}
          />
        </div>
      ) : (
        <FilesList files={filesList} />
      )}
    </div>
  );
}
```

Maintenant, ouvrez le fichier `FilesList.js` et acceptez les props `isSearchView` et `counter` et passez-les au composant `ListItem`.

Votre fichier `FilesList.js` ressemblera maintenant à ceci :

```js
import React from 'react';
import ListItem from './ListItem';

const FilesList = ({ files, isSearchView, counter }) => {
  return (
    <div className="list">
      {files.length > 0 ? (
        files.map((file, index) => {
          return (
            <ListItem
              key={file.id}
              {...file}
              index={index}
              isSearchView={isSearchView}
              counter={counter}
            />
          );
        })
      ) : (
        <div>
          <h3 className="no-result">Aucun fichier correspondant trouvé</h3>
        </div>
      )}
    </div>
  );
};

export default FilesList;
```

Maintenant, ouvrez le fichier `ListItem.js` et remplacez son contenu par le contenu suivant :

```js
import React from 'react';
import moment from 'moment';
import { AiFillFolder, AiOutlineFile, AiOutlineRight } from 'react-icons/ai';

const ListItem = ({
  index,
  type,
  name,
  comment,
  modified_time,
  isSearchView,
  counter
}) => {
  const isSelected = counter === index;

  return (
    <React.Fragment>
      <div className={`list-item ${isSelected ? 'active' : ''}`}>
        <div className="file">
          {isSearchView && (
            <span
              className={`arrow-icon ${isSelected ? 'visible' : 'invisible'}`}
            >
              <AiOutlineRight color="#0366d6" />
            </span>
          )}
          <span className="file-icon">
            {type === 'folder' ? (
              <AiFillFolder color="#79b8ff" size="20" />
            ) : (
              <AiOutlineFile size="18" />
            )}
          </span>
          <span className="label">{name}</span>
        </div>
        {!isSearchView && (
          <React.Fragment>
            <div className="comment">{comment}</div>
            <div className="time" title={modified_time}>
              {moment(modified_time).fromNow()}
            </div>
          </React.Fragment>
        )}
      </div>
    </React.Fragment>
  );
};

export default ListItem;
```

Dans ce fichier, nous acceptons d'abord les props `isSearchView` et `counter`. Ensuite, nous vérifions si l'index du fichier actuellement affiché dans la liste correspond à la valeur `counter`. 

En fonction de cela, nous affichons la flèche uniquement devant ce fichier. Ensuite, lorsque nous utilisons la flèche vers le bas ou vers le haut pour naviguer dans la liste, nous incrémentons ou décrémentons la valeur du compteur respectivement dans le fichier `App.js`. 

En fonction de la valeur `isSearchView`, nous affichons ou masquons la colonne de commentaire et de temps dans la vue de recherche sur l'interface utilisateur.

Maintenant, redémarrez l'application en exécutant à nouveau la commande `yarn start` et vérifiez son fonctionnement :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/navigation.gif)
_Rechercher et naviguer_

Vous pouvez trouver le code jusqu'à ce point dans [cette branche](https://github.com/myogeshchavan97/github-file-search-react/tree/navigation_functionality).

## Ajouter une fonctionnalité pour mettre en surbrillance le texte correspondant <br /> <br />

Maintenant, ajoutons la fonctionnalité pour mettre en surbrillance le texte correspondant du nom de fichier lorsque nous filtrons le fichier.

Ouvrez `App.js` et changez la fonction `handleSearch` par le code suivant :

```js
handleSearch = (searchTerm) => {
  let list;
  if (searchTerm) {
    const pattern = new RegExp(searchTerm, 'gi');
    list = files
      .filter(
        (file) =>
          file.name.toLowerCase().indexOf(searchTerm.toLowerCase()) > -1 &&
          file.type === 'file'
      )
      .map((file) => {
        return {
          ...file,
          name: file.name.replace(pattern, (match) => {
            return `<mark>${match}</mark>`;
          })
        };
      });
  } else {
    list = files.filter((file) => file.type === 'file');
  }

  this.setState({
    filesList: list,
    counter: 0
  });
};
```

Dans ce code, nous utilisons d'abord le constructeur `RegExp` pour créer une expression régulière dynamique pour une recherche globale et insensible à la casse :

```js
const pattern = new RegExp(searchTerm, 'gi');
```

Ensuite, nous filtrons les fichiers qui correspondent à ces critères de recherche :

```js
files.filter(
  (file) =>
    file.name.toLowerCase().indexOf(searchTerm.toLowerCase()) > -1 &&
    file.type === 'file'
);
```

Ensuite, nous appelons la méthode map du tableau sur le résultat que nous avons obtenu de la fonctionnalité de filtrage ci-dessus.

Dans la méthode map, nous utilisons la méthode `replace` de la chaîne.
La méthode `replace` accepte deux paramètres :

- le motif à rechercher
- la fonction à exécuter pour chaque motif correspondant

Nous utilisons la méthode `replace` pour trouver toutes les correspondances pour le `pattern` et le remplacer par la chaîne `<mark>${match}</mark>`. Ici, `match` contiendra le texte correspondant du nom de fichier.

Si vous vérifiez la structure JSON du fichier `utils/api.js`, la structure de chaque fichier ressemble à ceci :

```js
{
  id: 12,
  type: 'file',
  name: 'Search.js',
  comment: 'changes using react context',
  modified_time: '2020-06-30T07:55:33Z'
}
```

Comme nous voulons remplacer le texte du champ name uniquement, nous étalons les propriétés de l'objet fichier et ne changeons que le nom, en gardant les autres valeurs telles quelles.

```js
{
  ...file,
  name: file.name.replace(pattern, (match) => {
    return `<mark>${match}</mark>`;
  })
}
```

Maintenant, redémarrez l'application en exécutant à nouveau la commande `yarn start` et vérifiez son fonctionnement.

Vous verrez que le HTML est affiché tel quel sur l'interface utilisateur lorsque vous recherchez :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rendered_html.png)
_HTML non rendu correctement_

Cela est dû au fait que nous affichons le nom du fichier dans le fichier `ListItem.js` de la manière suivante :

```js
<span className="label">{name}</span>
```

Et pour prévenir les attaques `Cross-site scripting (XSS)`, React échappe tout le contenu affiché en utilisant l'expression JSX (qui est entre accolades).

Donc, si nous voulons réellement afficher le HTML correct, nous devons utiliser une prop spéciale appelée `dangerouslySetInnerHTML`. Elle passe le nom `__html` avec le HTML à afficher comme valeur, comme ceci :

```js
<span className="label" dangerouslySetInnerHTML={{ __html: name }}></span>
```

Maintenant, redémarrez l'application en exécutant à nouveau la commande `yarn start` et vérifiez son fonctionnement :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/highlight-1.gif)
_Application finale fonctionnelle_

Comme vous pouvez le voir, le terme de recherche est correctement mis en surbrillance dans le nom du fichier.


### C'est tout !

Vous pouvez trouver le code jusqu'à ce point dans [cette branche](https://github.com/myogeshchavan97/github-file-search-react/tree/text_highlighting).

Code source complet de GitHub : [ici](https://github.com/myogeshchavan97/github-file-search-react)
Démonstration en direct : [ici](https://github-file-search-react.netlify.app/)

**Consultez mes autres articles sur React, Node.js et Javascript sur [Medium](https://medium.com/@yogeshchavan), [dev.to](https://dev.to/myogeshchavan97) et abonnez-vous pour recevoir des mises à jour hebdomadaires directement dans votre boîte de réception [ici](https://subscribe-user.herokuapp.com/)**.