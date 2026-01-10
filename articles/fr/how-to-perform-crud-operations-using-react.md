---
title: Comment effectuer des opérations CRUD en utilisant React, React Hooks et Axios
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-26T21:41:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-using-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/React-CRUD-Operations-using-React-and-React-Hooks.png
tags:
- name: crud
  slug: crud
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment effectuer des opérations CRUD en utilisant React, React Hooks et
  Axios
seo_desc: 'By Nishant Kumar

  If you''re working with React, it can be quite difficult to understand and implement
  API Requests.

  So in this article, we''ll learn how it all works by implementing CRUD Operations
  using React, React Hooks, React Router, and Axios.

  Let...'
---

Par Nishant Kumar

Si vous travaillez avec React, il peut être assez difficile de comprendre et d'implémenter les requêtes API.

Alors dans cet article, nous allons apprendre comment tout cela fonctionne en implémentant des opérations CRUD en utilisant React, React Hooks, React Router et Axios.

Commençons.

## **Comment installer Node et npm**

Tout d'abord, installons Node dans notre système. Nous l'utiliserons principalement pour exécuter notre code JavaScript.

Pour télécharger Node, rendez-vous sur [https://nodejs.org/en/](https://nodejs.org/en/).

Vous aurez également besoin du **gestionnaire de paquets node**, ou npm, qui est basé sur Node. Vous pouvez l'utiliser pour installer des paquets pour vos applications JavaScript. Heureusement, il est inclus avec Node, donc vous n'avez pas besoin de le télécharger séparément.

Une fois les deux installés, ouvrez votre terminal ou invite de commande et tapez `node -v`. Cela vérifie quelle version de Node vous avez.

## **Comment créer votre application React**

Pour créer votre application React, tapez **`npx create-react-app <Nom de votre application>`** dans votre terminal, ou **`npx create-react-app react-crud`** dans ce cas.

Vous verrez que les paquets sont en cours d'installation.

Une fois les paquets installés, allez dans le dossier du projet et tapez **`npm start`**.

Vous verrez le modèle React par défaut, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-124754.png)
_Le modèle React Boilerplate par défaut_

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-124858.png)
_Notre fichier App.js_

## **Comment installer le package Semantic UI pour React**

Installons le package Semantic UI React dans notre projet. Semantic UI est une bibliothèque d'interface utilisateur conçue pour React qui possède des composants d'interface utilisateur pré-construits comme des tableaux, des boutons et de nombreuses fonctionnalités.

Vous pouvez l'installer en utilisant l'une des commandes ci-dessous, selon votre gestionnaire de paquets.

```bash
 yarn add semantic-ui-react semantic-ui-css
```

```bash
 npm install semantic-ui-react semantic-ui-css
```

De plus, importez la bibliothèque dans le fichier d'entrée principal de votre application, qui est index.js.

```js
 import 'semantic-ui-css/semantic.min.css'
```

## **Comment construire votre application CRUD**

Maintenant, commençons à construire notre application CRUD en utilisant React.

Tout d'abord, nous allons ajouter un titre à notre application.

Dans notre fichier app.js, ajoutez un titre comme ceci :

```
 import './App.css';

 function App() {
   return (
     <div>
       React Crud Operations
     </div>
   );
 }

 export default App;

```

Maintenant, assurons-nous qu'il est centré.

Donnez à la div parente un className de main. Et dans le fichier App.css, nous utiliserons Flexbox pour centrer le titre.

```
 import './App.css';

 function App() {
   return (
     <div className="main">
       React Crud Operations
     </div>
   );
 }

 export default App;

```

```
 .main{
   display: flex;
   justify-content: center;
   align-items: center;
   height: 100vh;
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-130340.png)

Maintenant, notre titre est parfaitement centré.

Pour qu'il ait meilleure apparence, nous devons le rendre plus gras et ajouter des polices sympas. Pour cela, nous allons utiliser des balises de titre autour de notre titre comme ceci :

```
 import './App.css';

 function App() {
   return (
     <div className="main">
       <h2 className="main-header">React Crud Operations</h2>
     </div>
   );
 }

 export default App;

```

Importons une police de Google Font. Rendez-vous sur [https://fonts.google.com/](https://fonts.google.com/) pour en choisir une.

Choisissez la police de votre choix, mais j'utiliserai la famille de polices Montserrat.

Importez la police de votre choix dans le fichier App.css, comme ceci :

```
 @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

```

Maintenant, changeons la police du titre.

```
 <div className="main">
       <h2 className="main-header">React Crud Operations</h2>
     </div>
```

Donnez à la balise de titre un `className` de `main-header`, comme ceci.

Ensuite, dans votre App.css, ajoutez la famille de polices :

```
 .main-header{
   font-family: 'Montserrat', sans-serif;
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-132749.png)

Maintenant, vous verrez le titre modifié.

## Comment créer vos composants CRUD

Créons quatre composants CRUD, qui seront Create, Read, Update et Delete.

Dans notre dossier src, créez un dossier appelé components. Et à l'intérieur de ce dossier, créez trois fichiers – create, read et update. Pour delete, nous n'avons pas besoin de composant supplémentaire.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-133242.png)

Maintenant, implémentons l'opération Create.

Mais pour cela, nous devons utiliser des API Mock. Ces API enverront des données au faux serveur que nous allons créer, juste à des fins d'apprentissage.

Alors, rendez-vous sur [https://mockapi.io/](https://mockapi.io/) et créez votre compte.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-133456.png)
_MockAPI_

Créez un projet en cliquant sur le bouton plus.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-133553.png)
_Cliquez sur le bouton plus pour créer un nouveau projet_

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-133702.png)

Ajoutez le nom de votre projet, et cliquez sur le bouton Create.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-133748.png)

Maintenant, créez une nouvelle ressource en cliquant sur le bouton NEW RESOURCE.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-133847.png)

Il vous demandera le nom de la ressource, alors entrez le nom que vous souhaitez utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-134009.png)

Supprimez les champs supplémentaires comme name, avatar, ou createdAt, car nous n'en aurons pas besoin. Ensuite, cliquez sur Create.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-134140.png)

Maintenant, nous avons créé notre fausse API, que j'ai nommée fakeData.

Cliquez sur fakeData, et vous verrez l'API s'ouvrir dans un nouvel onglet. La base de données est vide pour le moment.

## Comment créer un formulaire pour le composant Create

Utilisons un formulaire de la bibliothèque Semantic UI.

Rendez-vous sur Semantic React, et recherchez Form dans la barre de recherche à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-134532.png)

Vous verrez un formulaire comme ceci, alors cliquez sur Try it en haut à droite pour obtenir le code.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-134654.png)

Copiez ce code et collez-le dans votre fichier Create.js comme ceci :

```
 import React from 'react'
 import { Button, Checkbox, Form } from 'semantic-ui-react'

 const Create = () => (
     <Form>
         <Form.Field>
             <label>First Name</label>
             <input placeholder='First Name' />
         </Form.Field>
         <Form.Field>
             <label>Last Name</label>
             <input placeholder='Last Name' />
         </Form.Field>
         <Form.Field>
             <Checkbox label='I agree to the Terms and Conditions' />
         </Form.Field>
         <Button type='submit'>Submit</Button>
     </Form>
 )

 export default Create;
```

Importez le composant Create dans votre fichier app.js.

```
 import './App.css';
 import Create from './components/create';

 function App() {
   return (
     <div className="main">
       <h2 className="main-header">React Crud Operations</h2>
       <div>
         <Create/>
       </div>
     </div>
   );
 }

 export default App;

```

Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-135249.png)

Mais il y a un problème ici – les éléments ne sont pas correctement alignés et les couleurs des étiquettes de saisie de texte sont noires. Alors, changeons cela.

Dans le fichier create.js, donnez à **Form** un className de `create-form`.

```
 import React from 'react'
 import { Button, Checkbox, Form } from 'semantic-ui-react'

 const Create = () => (
     <Form className="create-form">
         <Form.Field>
             <label>First Name</label>
             <input placeholder='First Name' />
         </Form.Field>
         <Form.Field>
             <label>Last Name</label>
             <input placeholder='Last Name' />
         </Form.Field>
         <Form.Field>
             <Checkbox label='I agree to the Terms and Conditions' />
         </Form.Field>
         <Button type='submit'>Submit</Button>
     </Form>
 )

 export default Create;
```

Et ajoutez la classe suivante dans votre fichier App.css :

```
 .create-form label{
   color: whitesmoke !important;
   font-family: 'Montserrat', sans-serif;
   font-size: 12px !important;
 }
```

Cette classe ciblera toutes les étiquettes des champs de formulaire et appliquera la couleur whitesmoke. Elle changera également la police et augmentera la taille de la police.

Maintenant, dans notre classe `main`, ajoutez une propriété flex-direction. Cette propriété définira la direction en colonne, de sorte que chaque élément dans la classe `main` sera aligné verticalement.

```
 .main{
   display: flex;
   justify-content: center;
   align-items: center;
   height: 100vh;
   background-color: #212121;
   color: whitesmoke;
   flex-direction: column;
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-140141.png)

Vous pouvez voir que notre formulaire a beaucoup meilleure apparence maintenant.

Ensuite, obtenons les données des champs de formulaire dans notre console. Pour cela, nous allons utiliser le hook `useState` dans React.

Dans notre fichier create.js, importez `useState` de React.

```
 import React, { useState } from 'react';
```

Ensuite, créez des états pour le prénom, le nom de famille et la case à cocher. Nous initialisons les états comme vides ou faux.

```
 import React, { useState } from 'react';
 import { Button, Checkbox, Form } from 'semantic-ui-react'

 export default function Create() {
     const [firstName, setFirstName] = useState('');
     const [lastName, setLastName] = useState('');
     const [checkbox, setCheckbox] = useState(false);
     return (
         <div>
             <Form className="create-form">
                 <Form.Field>
                     <label>First Name</label>
                     <input placeholder='First Name' />
                 </Form.Field>
                 <Form.Field>
                     <label>Last Name</label>
                     <input placeholder='Last Name' />
                 </Form.Field>
                 <Form.Field>
                     <Checkbox label='I agree to the Terms and Conditions' />
                 </Form.Field>
                 <Button type='submit'>Submit</Button>
             </Form>
         </div>
     )
 }

```

Vous pouvez voir que cela agit maintenant comme un composant fonctionnel. Donc, nous devons changer le composant en un composant fonctionnel. Cela est dû au fait que nous ne pouvons utiliser les hooks que dans les composants fonctionnels.

Maintenant, configurons le prénom, le nom de famille et la case à cocher en utilisant les propriétés `setFirstName`, `setLastName` et `setCheckbox`, respectivement.

```
 <input placeholder='First Name' onChange={(e) => setFirstName(e.target.value)}/>

 <input placeholder='Last Name' onChange={(e) => setLastName(e.target.value)}/>

 <Checkbox label='I agree to the Terms and Conditions' onChange={(e) => setCheckbox(!checkbox)}/>
```

Nous capturons les états du prénom, du nom de famille et de la case à cocher.

Créez une fonction appelée `postData` que nous utiliserons pour envoyer des données à l'API. À l'intérieur de la fonction, écrivez ce code :

```
 const postData = () => {
         console.log(firstName);
         console.log(lastName);
         console.log(checkbox);
 }
```

Nous enregistrons les valeurs du prénom, du nom de famille et de la case à cocher dans la console.

Sur le bouton Submit, attribuez cette fonction en utilisant un événement onClick afin que chaque fois que nous appuyons sur le bouton Submit, cette fonction sera appelée.

```
 <Button onClick={postData} type='submit'>Submit</Button>
```

Voici le code complet pour le fichier _create_ :

```
 import React, { useState } from 'react';
 import { Button, Checkbox, Form } from 'semantic-ui-react'

 export default function Create() {
     const [firstName, setFirstName] = useState('');
     const [lastName, setLastName] = useState('');
     const [checkbox, setCheckbox] = useState(false);
     const postData = () => {
         console.log(firstName);
         console.log(lastName);
         console.log(checkbox);
     }
     return (
         <div>
             <Form className="create-form">
                 <Form.Field>
                     <label>First Name</label>
                     <input placeholder='First Name' onChange={(e) => setFirstName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <label>Last Name</label>
                     <input placeholder='Last Name' onChange={(e) => setLastName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <Checkbox label='I agree to the Terms and Conditions' onChange={(e) => setCheckbox(!checkbox)}/>
                 </Form.Field>
                 <Button onClick={postData} type='submit'>Submit</Button>
             </Form>
         </div>
     )
 }

```

Tapez une valeur dans le prénom et le nom de famille, et cochez la case à cocher. Ensuite, cliquez sur le bouton Submit. Vous verrez les données apparaître dans la console comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-142717.png)

## Comment utiliser Axios pour envoyer des requêtes API aux Mock APIs

Utilisons Axios pour envoyer les données de notre formulaire au serveur mock.

Mais d'abord, nous devons l'installer.

Tapez simplement `npm i axios` pour installer ce package.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-174213.png)

Après que le package a été installé, commençons l'opération de création.

Importez Axios en haut du fichier.

```
 import axios from 'axios';
```

Dans la fonction `postData`, nous allons utiliser Axios pour envoyer la requête POST.

```
 const postData = () => {
         axios.post(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData`, {
             firstName,
             lastName,
             checkbox
         })
     }
```

Comme vous pouvez le voir, nous utilisons axios.post. Et à l'intérieur de axios.post, nous avons le point de terminaison de l'API, que nous avons créé précédemment. Ensuite, nous avons les champs de formulaire enveloppés dans des accolades.

Lorsque nous cliquons sur Submit, cette fonction sera appelée et elle enverra les données au serveur API.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-174834.png)

Entrez votre prénom, votre nom de famille et cochez la case à cocher. Cliquez sur submit.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-174930.png)

Ensuite, si vous vérifiez l'API, vous obtiendrez votre prénom, votre nom de famille et la case à cocher comme vrai, enveloppés dans un objet.

## Comment implémenter les opérations Read et Update

Pour commencer l'opération de lecture, nous devons créer une page Read. Nous avons également besoin du package React Router pour naviguer vers différentes pages.

Rendez-vous sur [https://reactrouter.com/web/guides/quick-start](https://reactrouter.com/web/guides/quick-start) et installez le package en utilisant `npm i react-router-dom`.

Après son installation, importez quelques éléments de React Router :

```
 import { BrowserRouter as Router, Route } from 'react-router-dom'
```

Dans notre App.js, enveloppez tout le retour dans un Router. Cela signifie essentiellement que tout ce qui se trouve à l'intérieur de ce Router pourra utiliser le routage dans React.

```
 import './App.css';
 import Create from './components/create';
 import { BrowserRouter as Router, Route } from 'react-router-dom'

 function App() {
   return (
     <Router>
       <div className="main">
         <h2 className="main-header">React Crud Operations</h2>
         <div>
           <Create />
         </div>
       </div>
     </Router>
   );
 }

 export default App;

```

Notre App.js ressemblera maintenant à ceci.

Remplacez le Create à l'intérieur du return et ajoutez le code suivant :

```
 import './App.css';
 import Create from './components/create';
 import { BrowserRouter as Router, Route } from 'react-router-dom'

 function App() {
   return (
     <Router>
       <div className="main">
         <h2 className="main-header">React Crud Operations</h2>
         <div>
           <Route exact path='/create' component={Create} />
         </div>
       </div>
     </Router>
   );
 }

 export default App;

```

Ici, nous utilisons le composant Route comme Create. Nous avons défini le chemin de Create sur '/create'. Donc, si nous allons sur [http://localhost:3000/create](http://localhost:3000/create), nous verrons la page de création.

De même, nous avons besoin de routes pour read et update.

```
 import './App.css';
 import Create from './components/create';
 import Read from './components/read';
 import Update from './components/update';
 import { BrowserRouter as Router, Route } from 'react-router-dom'

 function App() {
   return (
     <Router>
       <div className="main">
         <h2 className="main-header">React Crud Operations</h2>
         <div>
           <Route exact path='/create' component={Create} />
         </div>
         <div style={{ marginTop: 20 }}>
           <Route exact path='/read' component={Read} />
         </div>

         <Route path='/update' component={Update} />
       </div>
     </Router>
   );
 }

 export default App;

```

Alors créez les routes read et update comme vous le voyez ci-dessus.

Et si vous allez sur [http://localhost:3000/read](http://localhost:3000/read), vous verrez ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-180318.png)
_Route Read_

Et sur [http://localhost:3000/update](http://localhost:3000/update), nous verrons le composant Update comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-180440.png)

### L'opération Read

Pour l'opération Read, nous aurons besoin d'un composant Table. Alors, rendez-vous sur React Semantic UI et utilisez un tableau de la bibliothèque.

```
 import React from 'react';
 import { Table } from 'semantic-ui-react'
 export default function Read() {
     return (
         <div>
             <Table singleLine>
                 <Table.Header>
                     <Table.Row>
                         <Table.HeaderCell>Name</Table.HeaderCell>
                         <Table.HeaderCell>Registration Date</Table.HeaderCell>
                         <Table.HeaderCell>E-mail address</Table.HeaderCell>
                         <Table.HeaderCell>Premium Plan</Table.HeaderCell>
                     </Table.Row>
                 </Table.Header>

                 <Table.Body>
                     <Table.Row>
                         <Table.Cell>John Lilki</Table.Cell>
                         <Table.Cell>September 14, 2013</Table.Cell>
                         <Table.Cell>jhlilk22@yahoo.com</Table.Cell>
                         <Table.Cell>No</Table.Cell>
                     </Table.Row>
                     <Table.Row>
                         <Table.Cell>Jamie Harington</Table.Cell>
                         <Table.Cell>January 11, 2014</Table.Cell>
                         <Table.Cell>jamieharingonton@yahoo.com</Table.Cell>
                         <Table.Cell>Yes</Table.Cell>
                     </Table.Row>
                     <Table.Row>
                         <Table.Cell>Jill Lewis</Table.Cell>
                         <Table.Cell>May 11, 2014</Table.Cell>
                         <Table.Cell>jilsewris22@yahoo.com</Table.Cell>
                         <Table.Cell>Yes</Table.Cell>
                     </Table.Row>
                 </Table.Body>
             </Table>
         </div>
     )
 }

```

Ici, vous pouvez voir que nous avons un tableau avec des données factices. Mais nous n'avons besoin que d'une seule ligne de tableau. Alors, supprimons le reste.

```
 import React from 'react';
 import { Table } from 'semantic-ui-react'
 export default function Read() {
     return (
         <div>
             <Table singleLine>
                 <Table.Header>
                     <Table.Row>
                         <Table.HeaderCell>Name</Table.HeaderCell>
                         <Table.HeaderCell>Registration Date</Table.HeaderCell>
                         <Table.HeaderCell>E-mail address</Table.HeaderCell>
                         <Table.HeaderCell>Premium Plan</Table.HeaderCell>
                     </Table.Row>
                 </Table.Header>

                 <Table.Body>
                     <Table.Row>
                         <Table.Cell>John Lilki</Table.Cell>
                         <Table.Cell>September 14, 2013</Table.Cell>
                         <Table.Cell>jhlilk22@yahoo.com</Table.Cell>
                         <Table.Cell>No</Table.Cell>
                     </Table.Row>
                 </Table.Body>
             </Table>
         </div>
     )
 }

```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-182905.png)

Ceci est le résultat de la page Read. Nous avons un tableau avec quatre colonnes, mais nous n'en avons besoin que de trois.

Supprimez les colonnes de champs supplémentaires et renommez les champs comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-183105.png)

Voici à quoi ressemble notre page Read maintenant :

```
 import React from 'react';
 import { Table } from 'semantic-ui-react'
 export default function Read() {
     return (
         <div>
             <Table singleLine>
                 <Table.Header>
                     <Table.Row>
                         <Table.HeaderCell>First Name</Table.HeaderCell>
                         <Table.HeaderCell>Last Name</Table.HeaderCell>
                         <Table.HeaderCell>Checked</Table.HeaderCell>
                     </Table.Row>
                 </Table.Header>

                 <Table.Body>
                     <Table.Row>
                         <Table.Cell>Nishant</Table.Cell>
                         <Table.Cell>Kumar</Table.Cell>
                         <Table.Cell>Yes</Table.Cell>
                     </Table.Row>
                 </Table.Body>
             </Table>
         </div>
     )
 }

```

Maintenant, envoyons la requête GET pour obtenir les données de l'API.

Nous avons besoin des données lorsque notre application se charge. Donc, nous allons utiliser le hook `useEffect`.

```
 import React, { useEffect } from 'react';

 useEffect(() => {
        
  }, [])
```

Créez un état qui contiendra les données entrantes. Ce sera un tableau.

```
 import React, { useEffect, useState } from 'react';

 const [APIData, setAPIData] = useState([]);
 useEffect(() => {
        
 }, [])
```

Dans le hook `useEffect`, envoyons la requête GET.

```
 useEffect(() => {
         axios.get(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData`)
             .then((response) => {
                 setAPIData(response.data);
             })
     }, [])
```

Donc, nous utilisons axios.get pour envoyer la requête GET à l'API. Ensuite, si la requête est remplie, nous définissons les données de réponse dans notre état _APIData_.

Maintenant, mappons nos lignes de tableau selon les données de l'API.

Nous allons utiliser la fonction Map pour cela. Elle itérera sur le tableau et affichera les données dans la sortie.

```
 <Table.Body>
   {APIData.map((data) => {
      return (
        <Table.Row>
           <Table.Cell>{data.firstName}</Table.Cell>
            <Table.Cell>{data.lastName}</Table.Cell>
            <Table.Cell>{data.checkbox ? 'Checked' : 'Unchecked'}</Table.Cell>
         </Table.Row>
    )})}
 </Table.Body>
```

Nous mappons notre firstName, lastName et checkbox selon les données de l'API. Mais notre checkbox est un peu différente. J'ai utilisé un opérateur ternaire ('?') ici. Si data.checkbox est vrai, la sortie sera Checked, sinon elle sera Unchecked.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-184955.png)
_Sortie de Read.js_

### L'opération Update

Créez un autre en-tête pour Update et une colonne dans la ligne de tableau pour un bouton de mise à jour. Utilisez le bouton de Semantic UI React.

```
 <Table.HeaderCell>Update</Table.HeaderCell>

 <Table.Cell> 
   <Button>Update</Button>
 </Table.Cell>
```

Maintenant, lorsque nous cliquons sur ce bouton, nous devons être redirigés vers la page de mise à jour. Pour cela, nous avons besoin de Link de React Router.

Importez Link de React Router. Et enveloppez la cellule de tableau pour le bouton de mise à jour dans des balises Link.

```
 import { Link } from 'react-router-dom';

 <Link to='/update'>
   <Table.Cell> 
      <Button>Update</Button>
    </Table.Cell>
 </Link>
```

Donc, si nous cliquons sur le bouton de mise à jour, nous serons redirigés vers la page de mise à jour.

Afin de mettre à jour les données des colonnes, nous avons besoin de leurs ID respectifs, qui proviennent des API.

Créez une fonction appelée `setData`. Liez-la au bouton Update.

```
  <Button onClick={() => setData()}>Update</Button>
```

Maintenant, nous devons passer les données en tant que paramètre à la fonction du haut.

```
  <Button onClick={() => setData(data)}>Update</Button>
```

Et dans la fonction en haut, enregistrez ces données dans la console :

```
 const setData = (data) => {
    console.log(data);
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-190515.png)
_Données dans la console_

Cliquez sur le bouton de mise à jour dans le tableau, et vérifiez la console. Vous obtiendrez les données du champ de tableau respectif.

Définissons ces données dans le localStorage.

```
 const setData = (data) => {
         let { id, firstName, lastName, checkbox } = data;
         localStorage.setItem('ID', id);
         localStorage.setItem('First Name', firstName);
         localStorage.setItem('Last Name', lastName);
         localStorage.setItem('Checkbox Value', checkbox)
 }
```

Nous déstructurons nos données en id, firstName, lastName et checkbox, puis nous définissons ces données dans le stockage local. Vous pouvez utiliser le stockage local pour stocker des données localement dans le navigateur.

Maintenant, dans le composant Update, nous avons besoin d'un formulaire pour l'opération de mise à jour. Réutilisons le formulaire de notre composant Create. Changez simplement le nom de la fonction de Create à Update.

```
 import React, { useState } from 'react';
 import { Button, Checkbox, Form } from 'semantic-ui-react'
 import axios from 'axios';

 export default function Update() {
     const [firstName, setFirstName] = useState('');
     const [lastName, setLastName] = useState('');
     const [checkbox, setCheckbox] = useState(false);

     return (
         <div>
             <Form className="create-form">
                 <Form.Field>
                     <label>First Name</label>
                     <input placeholder='First Name' onChange={(e) => setFirstName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <label>Last Name</label>
                     <input placeholder='Last Name' onChange={(e) => setLastName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <Checkbox label='I agree to the Terms and Conditions' onChange={(e) => setCheckbox(!checkbox)}/>
                 </Form.Field>
                 <Button type='submit'>Update</Button>
             </Form>
         </div>
     )
 }

```

Créez un hook `useEffect` dans le composant Update. Nous l'utiliserons pour obtenir les données que nous avons précédemment stockées dans le Local Storage. Créez également un état supplémentaire pour le champ ID.

```
 const [id, setID] = useState(null);

 useEffect(() => {
         setID(localStorage.getItem('ID'))
         setFirstName(localStorage.getItem('First Name'));
         setLastName(localStorage.getItem('Last Name'));
         setCheckbox(localStorage.getItem('Checkbox Value'))
 }, []);
```

Définissez les données respectives selon vos clés du Local Storage. Nous devons définir ces valeurs dans les champs de formulaire. Cela remplira automatiquement les champs lorsque la page Update se chargera.

```
 <Form className="create-form">
                 <Form.Field>
                     <label>First Name</label>
                     <input placeholder='First Name' value={firstName} onChange={(e) => setFirstName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <label>Last Name</label>
                     <input placeholder='Last Name' value={lastName} onChange={(e) => setLastName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <Checkbox label='I agree to the Terms and Conditions' checked={checkbox} onChange={(e) => setCheckbox(!checkbox)}/>
                 </Form.Field>
                 <Button type='submit'>Update</Button>
             </Form>
```



Maintenant, si nous cliquons sur le bouton Update dans la page Read, nous serons redirigés vers la page de mise à jour, où nous verrons toutes les données du formulaire automatiquement remplies.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-193521.png)
_Page de mise à jour_

Maintenant, créons la requête de mise à jour pour mettre à jour les données.

Créez une fonction appelée `updateAPIData`. À l'intérieur de cette fonction, nous allons utiliser axios.put pour envoyer une requête PUT qui mettra à jour nos données.

```
 const updateAPIData = () => {
     axios.put(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData/${id}`, {
         firstName,
          lastName,
          checkbox
 	})
 }
```

Ici, vous pouvez voir que nous ajoutons le point de terminaison de l'API avec un champ id.

Lorsque nous cliquons sur le champ dans le tableau, son ID est stocké dans le Local Storage. Et dans la page de mise à jour, nous le récupérons. Ensuite, nous stockons cet ID dans l'état _`id`_.

Après cela, nous passons l'id au point de terminaison. Cela nous permet de mettre à jour le champ dont nous passons l'ID.

Lie la fonction `updateAPIData` au bouton Update.

```
 <Button type='submit' onClick={updateAPIData}>Update</Button>
```

Cliquez sur le bouton Update dans le tableau de la page Read, changez votre nom de famille, puis cliquez sur le bouton Update dans la page Update.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-194627.png)
_Mise à jour des champs_

Retournez à la page Read, ou vérifiez l'API. Vous verrez que votre nom de famille a été changé.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-194756.png)
_L'API Mock_

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-194822.png)
_Notre tableau Read_

### L'opération Delete

Ajoutez un autre bouton dans le tableau Read, que nous utiliserons pour l'opération Delete.

```
 <Table.Cell>
    <Button onClick={() => onDelete(data.id)}>Delete</Button>
 </Table.Cell>
```

Créez une fonction appelée `onDelete`, et liez cette fonction au bouton Delete. Cette fonction recevra un paramètre ID lors du clic sur le bouton Delete.

```
 const onDelete = (id) => {

 }
```

Nous allons utiliser axios.delete pour supprimer les colonnes respectives.

```
 const onDelete = (id) => {
   axios.delete(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData/${id}`)
 }
```

Cliquez sur le bouton Delete et vérifiez l'API. Vous verrez que les données ont été supprimées.

Nous devons charger les données du tableau après leur suppression.

Alors, créez une fonction pour charger les données de l'API.

```
 const getData = () => {
     axios.get(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData`)
         .then((getData) => {
              setAPIData(getData.data);
          })
 }
```

Maintenant, dans la fonction `onDelete`, nous devons charger les données mises à jour après avoir supprimé un champ.

```
 const onDelete = (id) => {
         axios.delete(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData/${id}`)
      .then(() => {
         getData();
     })
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-201047.png)
_Tableau Read_

Donc, maintenant si nous cliquons sur Delete sur n'importe quel champ, il supprimera ce champ et rafraîchira le tableau automatiquement.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-24-201423.png)
_Tableau Read après la suppression d'un champ_

## Améliorons notre application CRUD

Donc, lorsque nous publions nos données dans la page Create, nous obtenons simplement les données dans la base de données mock. Nous devons rediriger vers la page Read lorsque nos données sont créées dans la page Create.

Importez `useHistory` de React Router.

```
 import { useHistory } from 'react-router';
```

Créez une variable appelée `history` avec `let`, et définissez-la sur `useHistory` :

```
 let history = useHistory();
```

Ensuite, utilisez la fonction history.push pour pousser vers la page Read juste après que l'API post soit appelée.

```
 const postData = () => {
         axios.post(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData`, {
             firstName,
             lastName,
             checkbox
         }).then(() => {
             history.push('/read')
         })
     }
```

Il poussera vers la page Read en utilisant le hook `useHistory`.

Faites de même pour la page Update.

```
 import React, { useState, useEffect } from 'react';
 import { Button, Checkbox, Form } from 'semantic-ui-react'
 import axios from 'axios';
 import { useHistory } from 'react-router';

 export default function Update() {
     let history = useHistory();
     const [id, setID] = useState(null);
     const [firstName, setFirstName] = useState('');
     const [lastName, setLastName] = useState('');
     const [checkbox, setCheckbox] = useState(false);

     useEffect(() => {
         setID(localStorage.getItem('ID'))
         setFirstName(localStorage.getItem('First Name'));
         setLastName(localStorage.getItem('Last Name'));
         setCheckbox(localStorage.getItem('Checkbox Value'));
     }, []);

     const updateAPIData = () => {
         axios.put(`https://60fbca4591156a0017b4c8a7.mockapi.io/fakeData/${id}`, {
             firstName,
             lastName,
             checkbox
         }).then(() => {
             history.push('/read')
         })
     }
     return (
         <div>
             <Form className="create-form">
                 <Form.Field>
                     <label>First Name</label>
                     <input placeholder='First Name' value={firstName} onChange={(e) => setFirstName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <label>Last Name</label>
                     <input placeholder='Last Name' value={lastName} onChange={(e) => setLastName(e.target.value)}/>
                 </Form.Field>
                 <Form.Field>
                     <Checkbox label='I agree to the Terms and Conditions' checked={checkbox} onChange={() => setCheckbox(!checkbox)}/>
                 </Form.Field>
                 <Button type='submit' onClick={updateAPIData}>Update</Button>
             </Form>
         </div>
     )
 }

```

Et maintenant vous savez comment effectuer des opérations CRUD en utilisant React et React Hooks !

Alternativement, vous pouvez regarder ma vidéo YouTube sur [React CRUD Operations](https://youtu.be/-ZMP8ZladIQ) si vous souhaitez compléter votre apprentissage.

Vous pouvez [trouver le code sur GitHub](https://github.com/nishant-666/React-CRUD-Operation-V2) si vous souhaitez expérimenter davantage.

> _Bon apprentissage._