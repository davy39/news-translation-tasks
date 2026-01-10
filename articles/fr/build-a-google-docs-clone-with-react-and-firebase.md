---
title: Comment créer un clone de Google Docs avec React, Material UI et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-09T21:16:05.000Z'
originalURL: https://freecodecamp.org/news/build-a-google-docs-clone-with-react-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/How-to-Build-a-Weather-Application-using-React--11-.png
tags:
- name: Firebase
  slug: firebase
- name: Google Docs
  slug: google-docs
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment créer un clone de Google Docs avec React, Material UI et Firebase
seo_desc: 'By Nishant Kumar

  In this article, we''ll build a Google Docs clone using React, Material UI, and
  Firebase.

  The final app will look like this:


  If we click any document, it will open up and we can edit them however we need to.


  And the most amazing fea...'
---

Par Nishant Kumar

Dans cet article, nous allons créer un clone de Google Docs en utilisant React, Material UI et Firebase.

L'application finale ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-145537.png)

Si nous cliquons sur un document, il s'ouvrira et nous pourrons les modifier comme nous le souhaitons.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-145643.png)

Et la fonctionnalité la plus incroyable est que nous pouvons éditer un document en temps réel. Cela signifie que si deux personnes travaillent sur le même document, leurs progrès seront reflétés dans les deux instances.

Mais avant de commencer, assurez-vous d'avoir Node installé dans votre système. Si ce n'est pas le cas, rendez-vous sur [https://nodejs.org/en/download/](https://nodejs.org/en/download/) pour le télécharger et l'installer.

Si vous souhaitez suivre ce tutoriel en format vidéo, voici la vidéo sur ma chaîne YouTube :

%[https://www.youtube.com/watch?v=7ZnjKIYVJsE]

## Configuration de base du projet

Commençons par créer une application React en utilisant la commande suivante :

```
npx create-react-app google-docs-clone
```

Cela installera tous les packages et dépendances dans un dossier local.

Ensuite, naviguez simplement dans le dossier du projet et exécutez **npm start** pour lancer l'application.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-105724.png)

Nous verrons tout ce code ici que nous devons supprimer. Nous commencerons avec une toile vierge.

Ensuite, créez un dossier appelé components. À l'intérieur de ce dossier, créons un fichier appelé **docs.js**.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-110011.png)

Faites de ce composant un composant fonctionnel, comme ceci :

```js
import React from 'react'

export default function Docs() {
  return (
    <div>
        <h1>docs</h1>
    </div>
  )
}

```

Maintenant, importez ce fichier dans le fichier principal **App.js**.

```js
import './App.css';
import Docs from './components/docs';

function App() {
  return (
    <Docs />
  );
}

export default App;

```

Et nous verrons cette sortie à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-110713.png)
_Clone de Google docs montrant la sortie "docs" dans le coin supérieur gauche_

Maintenant, faisons apparaître le titre au centre. Donc dans docs.js, donnez à la **div** principale une className de **docs-main**.

```js
import React from 'react'

export default function Docs() {
  return (
    <div className='docs-main'>
        <h1>Docs Clone</h1>
    </div>
  )
}

```

Et dans le fichier **App.css**, ajoutez les styles suivants :

```css
.docs-main{
    text-align: center;
}
```

Maintenant, notre application ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-113002.png)
_Clone de Google docs avec le titre au centre_

Maintenant, nous avons besoin d'un bouton pour ajouter nos documents. Donc, créons-le avec ce code :

```js
import React from 'react'

export default function Docs() {
  return (
    <div className='docs-main'>
        <h1>Docs Clone</h1>

        <button className='add-docs'>
            Ajouter un Document
        </button>
    </div>
  )
}

```

Et le CSS ressemble à ceci :

```css
.add-docs{
    height: 40px;
    width: 200px;
    background-color: #ffc107;
    border: none;
    cursor: pointer;
}
```

Importons quelques polices de Google Fonts. Placez ceci en haut du fichier CSS :

```
@import url('https://fonts.googleapis.com/css2?family=Poppins&family=Roboto&display=swap');
```

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins&family=Roboto&display=swap');

.docs-main{
    text-align: center;
    font-family: 'Roboto', sans-serif;
}

.add-docs{
    height: 40px;
    width: 200px;
    background-color: #ffc107;
    border: none;
    cursor: pointer;
    font-family: 'Poppins', sans-serif;
}
```

Pour ajouter des polices, faites simplement ceci dans les classNames respectives.

## Comment installer Material UI

Pour installer Material UI, tapez simplement la commande ci-dessous. Si vous souhaitez lire la documentation, rendez-vous sur [https://mui.com/](https://mui.com/).

```
npm install @mui/material @emotion/react @emotion/styled
```

Maintenant, créons un autre composant pour la modale. Nous utiliserons cette modale pour ajouter des documents à la base de données Firebase. 

```js
import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function Modal() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        Texte dans une modale
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
                    </Typography>
                </Box>
            </Modal>
        </div>
    );
}

```

Ceci est un simple composant de modale de Material UI. Maintenant, nous devons importer ce composant dans notre composant Docs.js.

Et nous devons déplacer quelques éléments de Modal.js vers Docs.js.

```
const [open, setOpen] = React.useState(false);
const handleOpen = () => setOpen(true);
```

Si nous cliquons sur le bouton Ajouter un Document, la modale s'ouvrira en utilisant ces fonctions :

```js
import React, { useState } from 'react';
import Modal from './Modal';

export default function Docs() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    return (
        <div className='docs-main'>
            <h1>Docs Clone</h1>

            <button
                className='add-docs'
                onClick={handleOpen}
            >
                Ajouter un Document
            </button>

            <Modal
                open={open}
                setOpen={setOpen}
            />
        </div>
    )
}

```

Donc, passez ces fonctions et états en tant que props dans le composant de modale et recevez-les.

```js
import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function ModalComponent({
    open,
    setOpen,
}) {
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        Texte dans une modale
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
                    </Typography>
                </Box>
            </Modal>
        </div>
    );
}

```

Maintenant, voici à quoi ressemble notre page avec la modale :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-115100.png)
_Page du clone de Google docs avec la modale affichée_

Ajoutons une entrée dans la modale, pour le nom du fichier.

```html
<Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <input
                        placeholder='Ajouter le Titre'
                        className='add-input'
                    />
                </Box>
            </Modal>
```

Donnons-lui quelques styles avec ce qui suit :

```css
.add-input{
    width: 95%;
    height: 40px;
    outline: none;
    border: 1px solid #676767;
    border-radius: 0px;
    padding: 10px;
    font-family: 'Poppins', sans-serif;
}
```

Et maintenant, voici à quoi ressemble notre modale :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-115756.png)
_Modale avec le style ajouté_

Ajoutons également un bouton. Nous pouvons copier le bouton Ajouter un Document.

```js
import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 500,
    height: 150,
    bgcolor: 'background.paper',
    boxShadow: 24,
    p: 5,
};

export default function ModalComponent({
    open,
    setOpen,
}) {
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <input
                        placeholder='Ajouter le Titre'
                        className='add-input'
                    />
                    <div className='button-container'>
                        <button
                            className='add-docs'
                        >
                            Ajouter
                        </button>
                    </div>
                </Box>
            </Modal>
        </div>
    );
}

```

Et le CSS ressemble à ceci :

```css
.button-container{
    text-align: center;
    margin: 30px;
}
```

Voici à quoi cela ressemble maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-120129.png)
_Modale avec le style et le bouton ajoutés_

## Comment ajouter Firebase à notre application

Maintenant, installons Firebase pour la base de données. Installez simplement Firebase en utilisant la commande ci-dessous :

```
npm install firebase
```

Rendez-vous sur [https://firebase.google.com/](https://firebase.google.com/) et cliquez sur Go to console en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-120526.png)

Ensuite, cliquez sur Ajouter un projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-120625.png)

Après avoir créé le projet, cliquez sur le bouton code pour créer une application web dans Firebase. Donnez-lui un nom et nous sommes prêts à partir.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-120803.png)

Maintenant, nous allons ajouter toutes ces données de configuration que nous devons stocker dans notre application React. Donc, créez un fichier appelé **firebaseConfig.js** et ajoutez-les.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-120857.png)

Nous allons avoir besoin de la base de données, donc initialisons-la. Exportons également la const app et la base de données comme ceci :

```js
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  //Vos données Firebase
};

export const app = initializeApp(firebaseConfig);
export const database = getFirestore(app)
```

Importez l'application et la base de données dans le fichier **App.js**. Et passez la base de données en tant que props au composant Docs. Nous l'utiliserons plus tard pour ajouter des données à Firebase Firestore.

```js
import './App.css';
import Docs from './components/docs';
import { app, database } from './firebaseConfig';

function App() {
  return (
    <Docs database={database}/>
  );
}

export default App;

```

Et dans le composant Docs. Recevons également l'export de la base de données depuis les props.

```js
import React, { useState } from 'react';
import Modal from './Modal';

export default function Docs({
    database
}) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    return (
        <div className='docs-main'>
            <h1>Docs Clone</h1>

            <button
                className='add-docs'
                onClick={handleOpen}
            >
                Ajouter un Document
            </button>

            <Modal
                open={open}
                setOpen={setOpen}
            />
        </div>
    )
}

```

Maintenant, configurons notre base de données Firestore. 

Allez dans la base de données Firestore depuis la barre latérale de gauche, et cliquez sur Créer une base de données.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-121804.png)

Nous allons démarrer notre base de données en mode Production. Donc, cliquez sur Suivant, puis sur Activer.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-121900.png)

Nous devons rendre les règles de sécurité publiques, juste pour l'instant. Donc, cliquez sur Règles dans l'onglet supérieur et modifiez les règles suivantes. Cela signifie que n'importe qui peut écrire des données ou les lire, même sans authentification.

```js
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write;
    }
  }
}
```

## Comment ajouter des données de documents à la base de données Firestore

Maintenant, ajoutons réellement nos données. Mais avant cela, nous devons obtenir les données du champ d'entrée.

Donc dans le composant Docs, créez un état qui contiendra ces données.

```
const [title, setTitle] = useState('')
```

Passez le titre et setTitle au composant modal.

```html
<Modal
                open={open}
                setOpen={setOpen}
                title={title}
                setTitle={setTitle}
            />
```

Recevez-les tous les deux en tant que props, et définissez-les dans le champ d'entrée.

```js
import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 500,
    height: 150,
    bgcolor: 'background.paper',
    boxShadow: 24,
    p: 5,
};

export default function ModalComponent({
    open,
    setOpen,
    title, 
    setTitle
}) {
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <input
                        placeholder='Ajouter le Titre'
                        className='add-input'
                        onChange={(event) => setTitle(event.target.value)}
                        value={title}
                    />
                    <div className='button-container'>
                        <button
                            className='add-docs'
                        >
                            Ajouter
                        </button>
                    </div>
                </Box>
            </Modal>
        </div>
    );
}

```

Maintenant, si nous tapons quelque chose dans l'entrée, il sera stocké dans l'état **title**.

Ensuite, nous avons besoin d'une fonction qui déclenchera les fonctions d'ajout de données, alors créons-la.

Dans Docs.js, créez une fonction et passez-la au composant modal :

```
const addData = () => {
        
}
```

Recevez-la dans le composant modal et liez-la simplement au bouton Ajouter comme ceci :

```html
<div className='button-container'>
                        <button
                            className='add-docs'
                            onClick={addData}
                        >
                            Ajouter
                        </button>
                    </div>
```

Maintenant, la fonction **addData** s'exécutera lorsque nous cliquerons sur le bouton Ajouter.

Maintenant, pour envoyer des données de React à Firebase dynamiquement, importons quelques éléments de Firebase Firestore :

```
import { addDoc, collection } from 'firebase/firestore';
```

Ici, nous utiliserons `collection` pour créer une collection de données dans Firebase, et addDoc ajoutera des données à cette collection.

Créons d'abord une référence de collection. Elle prendra la base de données que nous avons obtenue de **firebaseConfig.js** et le nom de la collection que nous voulons utiliser.

```
const collectionRef = collection(database, 'docsData')
```

Maintenant, dans la fonction addData, utilisons **addDoc**. Cette fonction **addDoc** prendra la référence de collection, et les données elles-mêmes.

```js
const addData = () => {
        addDoc(collectionRef, {
            title: title
        })
        .then(() => {
            alert('Données ajoutées')
        })
        .catch(() => {
            alert('Impossible d'ajouter les données')
        })
    }
```

Maintenant, ajoutez quelque chose dans le champ de texte et cliquez sur Ajouter. Il sera ajouté dans Firebase Firestore, avec une alerte indiquant que les données ont été ajoutées. Mais si cela échoue, nous obtiendrons "Impossible d'ajouter les données".

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-123810.png)

Si nous actualisons la base de données, nous verrons cette nouvelle entrée :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-07-123848.png)

Et c'est ainsi que nous ajoutons des données. Fermons également la modale après avoir ajouté les données.

Créez une fonction handleClose, et appelez cette fonction juste après le bloc **then** dans la fonction **addData**.

```js
const addData = () => {
        addDoc(collectionRef, {
            title: title
        })
        .then(() => {
            alert('Données ajoutées');
            handleClose()
        })
        .catch(() => {
            alert('Impossible d'ajouter les données')
        })
    }
```

## Comment lire les données de Firebase

Maintenant, lisons les données que nous avons ajoutées à Firebase. Nous aurons besoin de la fonction **onSnapshot** pour cela. La fonction onSnapshot obtient les données en temps réel.

Tout d'abord, importez-la de Firebase comme ceci :

```
import { addDoc, collection, onSnapshot } from 'firebase/firestore';
```

Ensuite, créez une fonction **getData** qui sera déclenchée lorsque notre page se chargera. Donc, nous mettrons cet onSnapshot dans le Hook **useEffect** de React.

```js
const getData = () => {
        onSnapshot(collectionRef, (data) => {
            console.log(data.docs.map((doc) => {
                return {...doc.data(), id: doc.id}
            }))
        })
    }
```

Ensuite, appelez cette fonction à l'intérieur du Hook useEffect.

```
useEffect(() => {
        getData()
    }, [])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-120757.png)

Mais comme vous pouvez le voir, nous obtenons les données deux fois. C'est parce que nous utilisons React version 18, qui inclut le **concurrent rendering**. C'est pourquoi le hook useEffect s'exécutera deux fois.

Pour résoudre ce problème, nous devons créer une référence **useRef**. 

```
const isMounted = useRef()
```

Ensuite, dans le Hook useEffect, nous devons vérifier si isMounted.current est vrai. Donc, si c'est vrai, nous ne retournerons rien. Et ensuite, nous définirons isMounted.current à vrai, et nous appellerons notre fonction getData.

```js
useEffect(() => {
        if(isMounted.current){
            return 
        }

        isMounted.current = true;
        getData()
    }, [])
```

Et si nous actualisons maintenant la page, nous obtiendrons les données une seule fois.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-121500.png)

Maintenant, nous devons inclure ces données dans un état de tableau. Donc, faisons cela.

Créez un état de **docsData**.

```
 const [docsData, setDocsData] = useState([]);
```

Et définissez les données entrantes à l'intérieur de cet état en utilisant **setDocsData**.

```
const getData = () => {
        onSnapshot(collectionRef, (data) => {
            setDocsData(data.docs.map((doc) => {
                return {...doc.data(), id: doc.id}
            }))
        })
    }
```

Maintenant, mappons notre tableau pour que les données s'affichent dans l'UI.

```html
<div>
                {docsData.map((doc) => {
                    return (
                        <div>
                            <p>{doc.title}</p>
                        </div>
                    )
                })}
            </div>
```

Cela affichera toutes les données dans notre application React.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-121859.png)

Nous verrons les deux documents sur notre page. Mais faisons-les apparaître dans une grille. Donnez aux conteneurs div les classNames de **grid-main** et **grid-child**.

```html
<div className='grid-main'>
                {docsData.map((doc) => {
                    return (
                        <div className='grid-child'>
                            <p>{doc.title}</p>
                        </div>
                    )
                })}
            </div>
```

Et dans le CSS, ajoutez les classes suivantes :

```css
.grid-main{
    display: grid;
    grid-template-columns: auto auto auto auto;
    color: whitesmoke;
    margin-top: 20px;
    gap: 20px;
    justify-content: center;
}

.grid-child{
    padding: 20px;
    background-color: rgb(98, 98, 98);
    width: 300px;
    cursor: pointer;
}
```

Maintenant, notre application ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-122658.png)

## Comment obtenir l'ID et rediriger vers la page d'édition des documents

Maintenant, chacun de ces éléments ci-dessus a un ID. Nous utiliserons ces ID pour rediriger vers une autre page où nous pouvons éditer les éléments et écrire notre contenu principal. 

Pour cela, nous avons besoin de deux packages. L'un est React-Router pour nous rediriger, et l'autre est React-Quill pour notre éditeur. Installez-les comme ceci :

```
npm i react-quill react-router-dom@6
```

Maintenant, configurons le routage vers une autre page. Mais nous avons besoin d'une autre page d'abord. Donc, créons-la.

Créez un composant appelé **EditDocs.** Faites-en un composant fonctionnel.

```js
import React from 'react'

export default function EditDocs() {
  return (
    <div>EditDocs</div>
  )
}

```

Pour configurer le routage, allez dans **index.js**, le point d'entrée de l'application. Enveloppez le <App /> à l'intérieur de **BrowserRouter**.

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

Maintenant, nous pouvons utiliser le routage n'importe où car nous déclarons BrowserRouter au niveau de base.

Maintenant, allez dans le fichier **App.js**. Importez Routes et Route de React-Router. Nous ajoutons également l'ID dans le chemin **editDocs**, afin que nous puissions voir l'ID dans la barre d'adresse.

```
import { Routes, Route } from "react-router-dom";
```

```js
import './App.css';
import Docs from './components/docs';
import EditDocs from './components/EditDocs';
import { Routes, Route } from "react-router-dom";
import { app, database } from './firebaseConfig';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Docs database={database} />} />
      <Route path="/editDocs/:id" element={<EditDocs database={database}/>} />
    </Routes>
  );
}

export default App;

```

Et ajoutez les routes suivantes. Si nous allons à **'/editDocs/:id'**, nous verrons notre page editDocs.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-124659.png)

Maintenant, nous devons obtenir l'ID spécifique des documents et l'envoyer à la page editDocs.

Créez une fonction getID et attribuez la fonction aux documents.

```
const getID = () => {

}
```

```html
<div className='grid-main'>
                {docsData.map((doc) => {
                    return (
                        <div className='grid-child' onClick={() => getID(doc.id)}>
                            <p>{doc.title}</p>
                        </div>
                    )
                })}
            </div>
```

Maintenant, si nous cliquons sur le document, nous obtiendrons son ID si nous le journalisons dans la console.

```
const getID = (id) => {
        console.log(id)
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-124956.png)

Maintenant, envoyons cet ID à la page editDocs en utilisant **useNavigate**.

Tout d'abord, importez useNavigate de react-router.

```
import { useNavigate } from 'react-router-dom';
```

Ensuite, créez une instance de useNavigate comme ceci :

```
let navigate = useNavigate();
```

Ensuite, pour passer l'ID, faites simplement ceci. Nous nous enverrons à la page editDocs, avec l'ID.

```js
const getID = (id) => {
        navigate(`/editDocs/${id}`)
}
```

Maintenant, recevons notre ID à l'autre extrémité. Dans le composant editDocs, nous avons besoin de **useParams** de react-router.

Donc, importez-le et créez une instance :

```js
import { useParams } from 'react-router-dom';

let params = useParams();
```

Aussi, si nous le journalisons, nous verrons l'ID.

```js
import { useParams } from 'react-router-dom';

let params = useParams();
console.log(params)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-125849.png)

Nous pouvons voir que nous obtenons l'ID dans la barre d'adresse ainsi que dans la console.

Maintenant, ajoutons **React Quill** à notre page editDocs.

```js
import React from 'react';
import { useParams } from 'react-router-dom';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
export default function EditDocs() {
    let params = useParams();
    return (
        <div>
            <h1>EditDocs</h1>

            <ReactQuill />
        </div>
    )
}

```

Nous devons importer React-Quill et le CSS.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-131423.png)

Mais nous pouvons voir que nous avons deux barres d'outils ici. Pour résoudre ce problème, supprimez simplement **React.StrictMode** de **index.js**.

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

Et tout ira bien.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-131534.png)

Maintenant, nous avons besoin d'un état pour ces données React Quill. Donc, créons-le. Nous créerons également une fonction pour déclencher lorsque nous tapons.

```js
const [docsDesc, setDocsDesc] = useState('');
    const getQuillData = () => {
        
    }
```

Maintenant, attachons la fonction et l'état à React Quill.

```html
<ReactQuill
   value={docsDesc}
   onChange={getQuillData}
/>
```

Dans la fonction **getQuillData**, attachons la valeur à l'état **docsDesc**, en utilisant la fonction **setDocsDesc**.

```js
const getQuillData = (value) => {
        setDocsDesc(value)
    }
```

Et nous avons terminé ici. Vous pouvez journaliser cet état docsDesc pour vérifier.

Maintenant, nous avons l'ID et les données que nous pouvons utiliser pour mettre à jour le document. Donc, faisons cela.

## Comment mettre à jour le document

Nous avons besoin de deux choses, **updateDoc** et la fonction **collection**. Nous utiliserons une fonction Debounce pour appeler la fonction updateDoc. Cela signifie que lorsque nous aurons fini de taper, après 5 ou 10 secondes, notre fonction updateDoc s'exécutera. 

Donc, créons une fonction :

```
const updateDocsData = () => {

}
```

Nous devons également spécifier la collection. Pour cela, nous avons besoin de la **database** de **App.js.** Donc, obtenons-la en utilisant les props.

```
<Route path="/editDocs/:id" element={<EditDocs database={database}/>} />
```

Maintenant, créons une référence de collection.

```
const collectionRef = collection(database, 'docsData')
```

Maintenant pour le debouncing, nous avons besoin de **updateDocsData** dans un hook useEffect.

```js
useEffect(() => {
        const updateDocsData = () => {

        }
 }, [])
```

Maintenant, ajoutons une fonction setTimeout avec un intervalle. Cela signifie que la fonction s'exécutera après cet intervalle spécifié. Faites l'intervalle **1000 millisecondes**, ou **1 seconde**.

```js
useEffect(() => {
    const updateDocsData = setTimeout(() => {
      
    }, 1000)  
    return () => clearTimeout(updateDocsData)
  }, [])
```

Maintenant, à l'intérieur de setTimeOut, ajoutons la fonction updateDoc. Donc à l'intérieur de la variable document, nous passons **collectionRef** et l'**ID** des params. Et ensuite, updateDoc prend cette variable document comme premier paramètre.

```js
const updateDocsData = setTimeout(() => {
            const document = doc(collectionRef, params.id)
            updateDoc(document, {

            })
        }, 1000)
```

Importons également la fonction **doc**. Elle spécifie quel document mettre à jour en utilisant l'ID comme clé primaire.

```js
import {
    updateDoc,
    collection,
    doc
} from 'firebase/firestore';
```

Maintenant, passons les données dans le deuxième paramètre, dans la fonction updateDoc.

```js
useEffect(() => {
        const updateDocsData = setTimeout(() => {
            const document = doc(collectionRef, params.id)
            updateDoc(document, {
                docsDesc: docsDesc
            })
        }, 1000)
        return () => clearTimeout(updateDocsData)
    }, [])
```

Dans le tableau de dépendances, ajoutez l'état de **docsDesc.** Donc après avoir tapé quelque chose, la fonction updateDoc s'exécutera après 1 seconde.

```js
useEffect(() => {
        const updateDocsData = setTimeout(() => {
            const document = doc(collectionRef, params.id)
            updateDoc(document, {
                docsDesc: docsDesc
            })
            .then(() => {
                alert('Enregistré')
            })
            .catch(() => {
                alert('Impossible d'enregistrer')
            })
        }, 1000)
        return () => clearTimeout(updateDocsData)
    }, [docsDesc])
```

Donc, tapez quelque chose dans l'éditeur, et il sera enregistré dans la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-135046.png)

Et les données ici :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-135105.png)

Si nous ajoutons quelque chose de plus, nous ajouterons les données précédentes :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-135224.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-135242.png)

## Comment récupérer les données de la base de données vers l'éditeur

Maintenant, si nous revenons en arrière et cliquons sur un document, les données seront nulles, ou effacées. Donc, nous devons récupérer les données de la base de données et les définir dans l'éditeur.

Nous utiliserons la fonction **onSnapshot** pour cela.

```js
import {
    updateDoc,
    collection,
    doc,
    onSnapshot
} from 'firebase/firestore';
```

```js
const getData = () => {
        
    }

    useEffect(() => {
        if(isMounted.current){
            return 
        }

        isMounted.current = true;
        getData()
    }, [])
```

Donc, c'est exactement comme nous l'avons fait dans le composant Docs. Nous devons spécifier quelles données récupérer en utilisant le paramètre ID. Et ensuite, nous passons ce document à la fonction onSnapshot pour obtenir les données dont nous avons besoin.

```js
const getData = () => {
        const document = doc(collectionRef, params.id)
        onSnapshot(document, (docs) => {
            console.log(docs.data().docsDesc)
        })
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-140423.png)

Définissons ce **docs.data().docsDesc** dans l'état docsDesc en utilisant setDocsDesc. Donc, si le document se charge, il sera défini là. 

Ajoutez quelques données, puis revenez en arrière. Et si vous revenez au même composant, la description du document sera là.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-140723.png)

Maintenant, dans la page d'accueil où nous voyons toutes les données, nous devons également ajouter la description, si elle existe.

```
 <div dangerouslySetInnerHTML={{__html: doc.docsDesc}} />
```

Nous utilisons **dangerouslySetInnerHTML** car les données sont ajoutées sous forme de balises dans React Quill. Cela facilite le rendu de la mise en forme. 

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-141304.png)

Voyez, j'ai ajouté quelques mises en forme comme des textes en **gras** et en *italique*.

Maintenant, nous devons apporter quelques modifications mineures. Dans le fichier App.js (où nous ajoutons le titre du document), ajoutons également la description, qui sera initialement vide.

```js
const addData = () => {
        addDoc(collectionRef, {
            title: title,
            docsDesc: ''
        })
        .then(() => {
            alert('Données ajoutées');
            handleClose()
        })
        .catch(() => {
            alert('Impossible d'ajouter les données')
        })
    }
```

Donc, si nous créons un document, nous aurons docsDesc dans le document Firestore. Cela empêchera notre application de planter lorsque nous allons à la page EditDocs.

Maintenant, dans la page EditDocs, ajoutons le titre du document pour qu'il s'affiche en haut. Créez un état appelé documentTitle et définissez-le. 

```js
const [documentTitle, setDocumentTitle] = useState('')

const getData = () => {
        const document = doc(collectionRef, params.id)
        onSnapshot(document, (docs) => {
            setDocumentTitle(docs.data().title)
            setDocsDesc(docs.data().docsDesc);
        })
    }
```

Et affichez cet état en haut :

```
<h1>{documentTitle}</h1>
```

Voici le code complet de la page **EditDocs** jusqu'à présent :

```js
import React, { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import {
    updateDoc,
    collection,
    doc,
    onSnapshot
} from 'firebase/firestore';
export default function EditDocs({
    database
}) {
    const isMounted = useRef()
    const collectionRef = collection(database, 'docsData')
    let params = useParams();
    const [documentTitle, setDocumentTitle] = useState('')
    const [docsDesc, setDocsDesc] = useState('');
    const getQuillData = (value) => {
        setDocsDesc(value)
    }
    useEffect(() => {
        const updateDocsData = setTimeout(() => {
            const document = doc(collectionRef, params.id)
            updateDoc(document, {
                docsDesc: docsDesc
            })
                .then(() => {
                    alert('Enregistré')
                })
                .catch(() => {
                    alert('Impossible d'enregistrer')
                })
        }, 1000)
        return () => clearTimeout(updateDocsData)
    }, [docsDesc])

    const getData = () => {
        const document = doc(collectionRef, params.id)
        onSnapshot(document, (docs) => {
            setDocumentTitle(docs.data().title)
            setDocsDesc(docs.data().docsDesc);
        })
    }

    useEffect(() => {
        if (isMounted.current) {
            return
        }

        isMounted.current = true;
        getData()
    }, [])
    return (
        <div>
            <h1>{documentTitle}</h1>

            <ReactQuill
                value={docsDesc}
                onChange={getQuillData}
            />
        </div>
    )
}

```

## Comment ajouter un peu de style

Maintenant, ajoutons un peu de style à cette page EditDocs :

```html
<div className='editDocs-main'>
            <h1>{documentTitle}</h1>
            <div className='editDocs-inner'>
                <ReactQuill
                    className='react-quill'
                    value={docsDesc}
                    onChange={getQuillData}
                />
            </div>
        </div>
```

Et dans le CSS, ajoutez le style suivant :

```css

.editDocs-main {
    font-family: 'Poppins', sans-serif;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.editDocs-inner {
    width: 800px;
    box-shadow: 0px -2px 5px 2px rgba(181, 181, 181, 0.75);
    -webkit-box-shadow: 0px -2px 5px 2px rgba(181, 181, 181, 0.75);
    -moz-box-shadow: 0px -2px 5px 2px rgba(181, 181, 181, 0.75);
    padding: 20px;
    height: 750px;
}

.ql-container.ql-snow {
    border: none !important;
}
```

Nous ajoutons une ombre de boîte, nous supprimons la bordure de React Quill, et nous centrons tout. 

Voici à quoi ressemble notre page d'édition de document maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-144341.png)

Maintenant, pour notre dernière chose : remplaçons nos alertes par des messages toast. Nous avons besoin d'un autre package appelé [React Toastify](https://www.npmjs.com/package/react-toastify). Donc, installons-le.

```
npm i react-toastify
```

Ensuite, nous devons importer ces deux choses :

```js
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
```

Et puis, le composant **<ToastContainer />**.

Maintenant, pour le message toast, faites simplement ceci :

```js
useEffect(() => {
        const updateDocsData = setTimeout(() => {
            const document = doc(collectionRef, params.id)
            updateDoc(document, {
                docsDesc: docsDesc
            })
                .then(() => {
                    toast.success('Document enregistré', {
                        autoClose: 2000
                    })
                })
                .catch(() => {
                    toast.error('Impossible d'enregistrer le document', {
                        autoClose: 2000
                    })
                })
        }, 1000)
        return () => clearTimeout(updateDocsData)
    }, [docsDesc])
```

Nous avons **toast.success** pour les alertes de succès, et **toast.error** pour les alertes d'erreur.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-08-145209.png)

## Conclusion

Et voilà, vous avez créé un clone de Google Docs. Vous êtes libre d'expérimenter et d'améliorer cela.

Vous pouvez obtenir le code complet ici : [https://github.com/nishant-666/Google-Docs-Clone](https://github.com/nishant-666/Google-Docs-Clone)

Aussi, consultez ma chaîne [Cybernatico](https://www.youtube.com/c/CybernaticoByNishant) pour plus de tutoriels incroyables comme celui-ci. 

> Bon apprentissage.