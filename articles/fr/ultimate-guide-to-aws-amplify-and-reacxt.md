---
title: Comment créer une application Full Stack avec AWS Amplify et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-09T21:27:07.000Z'
originalURL: https://freecodecamp.org/news/ultimate-guide-to-aws-amplify-and-reacxt
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95a7740569d1a4ca0de3.jpg
tags:
- name: AWS
  slug: aws
- name: full stack
  slug: full-stack
- name: React
  slug: react
seo_title: Comment créer une application Full Stack avec AWS Amplify et React
seo_desc: "By Sam Williams\nAWS Amplify is a tool developed by Amazon Web Services\
  \ that helps make app development easier. \nIt includes loads of features which\
  \ allow you to quickly and easily work with other AWS services. This means you can\
  \ spend more time build..."
---

Par Sam Williams

AWS Amplify est un outil développé par Amazon Web Services qui facilite le développement d'applications.

Il inclut de nombreuses fonctionnalités qui permettent de travailler rapidement et facilement avec d'autres services AWS. Cela signifie que vous pouvez passer plus de temps à développer les fonctionnalités qui rendent votre application unique.

Ce tutoriel est divisé en quatre parties :

* Comment créer l'application avec une connexion
* Comment ajouter une base de données et travailler avec les données
* Comment ajouter un stockage de fichiers et utiliser ces fichiers
* Comment permettre aux utilisateurs de télécharger leurs propres fichiers et données

Si vous souhaitez lire cet article hors ligne, vous pouvez [le télécharger ici](https://www.subscribepage.com/amplify_full_stack).

## Comment créer l'application avec inscription, connexion et déconnexion

Dans cette première section, nous allons configurer une nouvelle application React avec AWS Amplify pour ajouter l'inscription, la connexion et la déconnexion de la manière la plus simple possible.

%[https://youtu.be/g4qKydnd0vU]

Nous devons commencer par créer une nouvelle application React en utilisant `create-react-app`. Ouvrez un terminal et exécutez ces commandes. Si vous n'avez pas installé create-react-app, vous pouvez d'abord exécuter `npm i -g create-react-app`.

```
npx create-react-app amplify-react-app

cd amplify-react-app
```

Avec cela configuré, nous pouvons maintenant installer Amplify puis le configurer.

```
npm install -g @aws-amplify/cli

amplify configure
```

Cela ouvrira un onglet de la console AWS dans votre navigateur. Assurez-vous d'être connecté au bon compte avec un utilisateur ayant des permissions d'administrateur.

Retournez dans le terminal et suivez les étapes, en ajoutant une région et un nom pour l'utilisateur. Cela vous ramènera ensuite dans le navigateur où vous pourrez suivre les étapes pour créer le nouvel utilisateur. Assurez-vous de rester sur la page où vous voyez la clé et le secret !

De retour dans le terminal, vous pouvez suivre les étapes, en copiant la clé d'accès et le secret dans le terminal lorsqu'on vous le demande. Lorsque l'on vous demande si vous souhaitez ajouter cela à un profil, dites `Oui`. Créez un profil du type `serverless-amplify`.

Maintenant, nous pouvons initialiser la configuration d'amplify en exécutant `amplify init`. Vous pouvez donner un nom au projet et répondre à toutes les questions. La plupart d'entre elles devraient déjà être correctes. Cela prend ensuite un certain temps pour apporter les modifications à votre compte.

Une fois terminé, nous devons ajouter l'authentification à l'application. Nous faisons cela avec `amplify add auth`. Sélectionnez la méthode comme `default`, la connexion à `email` puis `non, j'ai terminé`. Nous pouvons maintenant déployer cela en exécutant `amplify push`. Cela prend un certain temps mais à la fin, notre fichier `src/aws-exports.js` a été créé.

## Comment construire l'application React

Maintenant, nous pouvons passer à la création de l'application React. Commencez par installer les packages npm Amplify dont nous avons besoin.

```
npm install --save aws-amplify @aws-amplify/ui-react
```

Maintenant, nous pouvons commencer à modifier le code de notre application. Dans notre fichier `src/App.js`, nous pouvons supprimer tout ce qui se trouve dans les en-têtes et le remplacer par ceci :

```js
<header className="App-header">
    <AmplifySignOut />
    <h2>Contenu de mon application</h2>
</header>
```

C'est une configuration très basique, mais vous pourriez mettre le contenu principal de votre site ici et placer le bouton `AmplifySignOut` où vous le souhaitez.

Nous devons également ajouter quelques imports supplémentaires en haut du fichier :

```js
import Amplify from 'aws-amplify';
import awsconfig from './aws-exports';
import { AmplifySignOut, withAuthenticator } from '@aws-amplify/ui-react';

Amplify.configure(awsconfig);
```

Maintenant, la dernière chose que nous devons faire est de changer la façon dont nous exportons l'application. Changez la dernière ligne pour qu'elle soit `export default withAuthenticator(App);` pour ajouter Amplify à cette application.

Maintenant, lorsque nous exécutons `npm start`, nous devrions obtenir un écran de connexion. Nous n'avons pas créé celui-ci, donc il provient d'Amplify lui-même.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-11-at-06.48.01.png)

Si nous essayons de nous connecter, cela échouera, car nous devons d'abord nous inscrire. Nous pouvons cliquer sur `créer un compte` puis entrer notre email et un mot de passe pour nous inscrire.

Une fois que nous avons confirmé notre email en soumettant le code qui nous a été envoyé, nous accédons à la page d'accueil de notre application. Si nous nous déconnectons, nous pouvons maintenant nous reconnecter comme prévu.

## Comment ajouter une base de données à notre application

Si vous souhaitez ajouter des données à votre application React mais que vous ne souhaitez pas avoir à construire une API, alors cette section est faite pour vous. Nous allons voir comment nous pouvons utiliser AWS Amplify dans notre application React pour nous permettre d'accéder à notre base de données en backend en utilisant GraphQL.

%[https://youtu.be/kqi4gPfdVHY]

Pour commencer, nous devons aller dans le terminal et exécuter :

```
amplify add api
```

Cela nous lancera dans une série d'options CLI, nous posant quelques questions de configuration :

Quel type d'API nous voulons utiliser : **GraphQL**  
Le nom de l'API : **songAPI**  
Comment nous voulons authentifier l'API : **Amazon Cognito User Pool**  
Paramètres avancés : **Non, j'ai terminé**  
Avez-vous un schéma : **Non**  
Quel type de schéma souhaitez-vous : **Objet unique avec des champs**

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-20-at-07.13.40.png)

Après une petite configuration, on nous demande si nous voulons modifier notre nouveau schéma. Nous voulons dire oui. Cela ouvre le schéma GraphQL que nous allons mettre à jour pour qu'il soit le schéma listé ici.

```graphql
type Song @model {
    id: ID!
    title: String!
    description: String!
    filePath: String!
    likes: Int!
    owner: String!
}
```

Avec notre schéma configuré, nous allons exécuter `amplify push` qui comparera notre configuration amplify actuelle avec celle de notre compte AWS. Comme nous avons ajouté une nouvelle API, nous aurons des changements, donc on nous demandera si nous voulons continuer avec les changements.

Une fois que nous avons sélectionné **Oui**, nous sommes placés dans un autre ensemble d'options.

Voulons-nous générer du code pour notre API GraphQL : **Oui**  
Quel langage : **JavaScript**  
Modèle de fichier pour les nouveaux fichiers : **src/graphql/**/*.js**  
Générer toutes les opérations : **Oui**  
Profondeur maximale des instructions : **2**

Cela va maintenant déployer tous les changements sur AWS et également configurer les nouveaux fichiers de requête dans notre application React. Cela prend quelques minutes.

Une fois cela terminé, nous pouvons aller dans notre fichier `App.js` et le renommer en `App.jsx`. Cela facilite simplement l'écriture de notre code JSX.

Nous devons maintenant écrire une fonction ici pour obtenir la liste des chansons de notre nouvelle base de données. Cette fonction appelle l'API GraphQL en passant l'opération `listSongs`. Nous devons également ajouter un nouvel état au composant `App`.

```js
const [songs, setSongs] = useState([]);

const fetchSongs = async () => {
    try {
        const songData = await API.graphql(graphqlOperation(listSongs));
        const songList = songData.data.listSongs.items;
        console.log('liste de chansons', songList);
        setSongs(songList);
    } catch (error) {
        console.log('erreur lors de la récupération des chansons', error);
    }
};
```

Nous devons maintenant ajouter ou mettre à jour quelques imports dans notre fichier pour que cela fonctionne :

```js
import React, { useState, useEffect } from 'react';
import { listSongs } from './graphql/queries';
import Amplify, { API, graphqlOperation } from 'aws-amplify';
```

La fonction `listSongs` est l'une de ces fonctions créées par Amplify pour nous aider à accéder à nos données. Vous pouvez voir les autres fonctions disponibles dans le dossier `./graphql`.

Maintenant, nous voulons que cette fonction soit appelée une fois lorsque le composant est rendu, mais pas à chaque fois qu'il est re-rendu. Pour cela, nous utilisons `useEffect` mais nous devons ajouter un deuxième paramètre `[]` pour qu'il ne soit déclenché qu'une seule fois.

```js
useEffect(() => {
    fetchSongs();
}, []);
```

Si nous démarrons maintenant notre application en utilisant `npm start` puis allons dans l'application, nous pouvons ouvrir la console et voir un log de `song list []`. Cela signifie que le `useEffect` a appelé `fetchSongs` qui journalise le résultat, mais actuellement il n'y a rien dans la base de données.

Pour corriger cela, nous devons nous connecter à notre compte AWS et ajouter le service DynamoDB. Nous devrions trouver une nouvelle table appelée quelque chose comme `Song-5gq8g8wh64w-dev`. Si vous ne la trouvez pas, assurez-vous de vérifier également d'autres régions.

Celle-ci n'a actuellement aucune donnée, donc nous devons en ajouter. Pour l'instant, nous allons créer manuellement de nouvelles données ici. Sous `Items`, cliquez sur `Create item` puis assurez-vous que la liste déroulante en haut à gauche affiche `text`. Si elle affiche `tree`, cliquez simplement dessus et changez-la en `text`. Nous pouvons ensuite faire en sorte que les données aillent dans cette ligne.

Nous commençons avec le schéma GraphQL, en donnant à la ligne quelques données pour chaque attribut. Mais nous devons également ajouter des valeurs `createdAt` et `updatedAt`. Vous pouvez trouver cela en utilisant la console du navigateur.

Tapez `new Date().toISOString()` et copiez le résultat de cela. Vous devriez obtenir un objet comme ceci :

```json
{
  "id": "gr4334t4tog345ht35",
  "title": "Ma première chanson",
  "description": "Une chanson de test pour notre application amplify",
  "owner": "Sam Williams",
  "filePath": "",
  "likes": 4,
  "createdAt": "2020-08-13T07:01:39.176Z",
  "updatedAt": "2020-08-13T07:01:39.176Z"
}
```

Si nous sauvegardons ce nouvel objet, nous pouvons retourner dans notre application et actualiser la page. Nous devrions maintenant pouvoir voir nos données dans le console.log.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-20-at-07.46.49.png)

Nous pouvons maintenant utiliser ces données dans notre application pour afficher la liste des chansons que nous venons d'obtenir. Remplacez le texte existant de `song list` par cet ensemble de JSX.

```jsx
<div className="songList">
    {songs.map((song, idx) => {
        return (
            <Paper variant="outlined" elevation={2} key={`song${idx}`}>
                <div className="songCard">
                    <IconButton aria-label="play">
                        <PlayArrowIcon />
                    </IconButton>
                    <div>
                        <div className="songTitle">{song.title}</div>
                        <div className="songOwner">{song.owner}</div>
                    </div>
                    <div>
                        <IconButton aria-label="like">
                            <FavoriteIcon />
                        </IconButton>
                        {song.likes}
                    </div>
                    <div className="songDescription">{song.description}</div>
                </div>
            </Paper>
        );
    })}
</div>
```

Ce code parcourt chaque chanson de la liste et rend un nouveau `Paper` pour elles avec tous les détails dont nous avons besoin.

Nous utilisons la bibliothèque MaterialUI pour aider à rendre cela joli pour nous, donc nous devons nous assurer d'exécuter `npm install --save @material-ui/core @material-ui/icons` pour installer ces packages et ensuite les ajouter aux imports en haut du fichier aussi :

```js
import { Paper, IconButton } from '@material-ui/core';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';
import FavoriteIcon from '@material-ui/icons/Favorite';
```

Avec cela, si nous sauvegardons et rechargeons notre application, nous obtenons maintenant ceci :

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-20-at-07.53.02.png)

Bien que cela soit acceptable, nous pouvons mettre à jour le CSS pour le rendre beaucoup mieux. Ouvrez votre fichier `App.css` et changez-le pour cela :

```css
.App {
    text-align: center;
}

.App-logo {
    height: 10vmin;
    pointer-events: none;
}

.App-header {
    background-color: #282c34;
    min-height: 5vh;
    display: flex;
    align-items: center;
    justify-content: space-around;
    font-size: calc(10px + 2vmin);
    color: white;
}

.App-link {
    color: #61dafb;
}

.songList {
    display: flex;
    flex-direction: column;
}

.songCard {
    display: flex;
    justify-content: space-around;
    padding: 5px;
}

.songTitle {
    font-weight: bold;
}
```

Maintenant, nous obtenons quelque chose comme ceci - beaucoup mieux.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-20-at-07.54.40.png)

Maintenant, nous avons un élément dans la base de données, donc nous n'obtenons qu'un seul enregistrement. Si nous retournons dans Dynamo et créons un nouvel élément ou dupliquons celui existant, nous pouvons voir à quoi ressemblent plusieurs chansons. Vous pouvez dupliquer un élément en cliquant sur la case à cocher à sa gauche.

Maintenant que nous pouvons obtenir les données, qu'en est-il de la mise à jour de ces informations ? Pour cela, nous allons ajouter la possibilité d'aimer une chanson. Pour commencer, nous pouvons ajouter une fonction `onClick` au bouton d'icône que nous avons pour les likes.

```jsx
<IconButton aria-label="like" onClick={() => addLike(idx)}>
    <FavoriteIcon />
</IconButton>
```

Vous avez peut-être réalisé qu'il y a cette propriété `idx` que nous n'avons pas vue auparavant. Cela signifie index.

Là où nous faisons le `songs.map`, nous pouvons le mettre à jour légèrement pour obtenir la position de chaque élément dans la liste. Nous pouvons également utiliser cet idx pour ajouter une clé au `Paper` de niveau supérieur dans ce map pour supprimer les erreurs que nous obtenons de React.

```jsx
{songs.map((song, idx) => {
    return (
        <Paper variant="outlined" elevation={2} key={`song${idx}`}>
            ...
        </Paper>
    )}
)}
```

Avec le nouvel index et l'appel de fonction `onClick`, nous devons maintenant créer la fonction `addLike`.

Cette fonction doit prendre l'index de la chanson pour trouver la bonne chanson et mettre à jour le nombre de likes. Elle supprime ensuite certains champs qui ne peuvent pas être passés dans l'opération `updateSong` avant d'appeler cette opération.

```js
const addLike = async idx => {
    try {
        const song = songs[idx];
        song.likes = song.likes + 1;
        delete song.createdAt;
        delete song.updatedAt;

        const songData = await API.graphql(graphqlOperation(updateSong, { input: song }));
        const songList = [...songs];
        songList[idx] = songData.data.updateSong;
        setSongs(songList);
    } catch (error) {
        console.log('erreur lors de l\'ajout de Like à la chanson', error);
    }
};
```

Une fois que la chanson a été mise à jour dans la base de données, nous devons obtenir cette mise à jour dans notre état. Nous devons cloner les chansons existantes en utilisant `const songList = [...songs]`.

Si nous mutons simplement la liste originale des chansons, React n'aurait pas re-rendu la page. Avec cette nouvelle liste de chansons, nous appelons `setSongs` pour mettre à jour notre état et nous avons terminé avec la fonction.

Nous devons simplement ajouter un import de plus en haut du fichier que nous obtenons des mutateurs qu'Amplify a créés :

```js
import { updateSong } from './graphql/mutations';
```

Maintenant, lorsque nous cliquons sur le bouton like d'une chanson, elle est mise à jour dans l'état et dans la base de données.

![Image](https://completecoding.io/content/images/2020/08/ezgif.com-optimize.gif)

# Comment ajouter un stockage de fichiers

Maintenant que nous avons les données des chansons stockées dans Dynamo, nous voulons stocker les données MP3 réelles quelque part. Nous allons stocker les chansons dans S3 et y accéder en utilisant Amplify.

%[https://youtu.be/ZpdgHjbnef0]

### Comment ajouter la fonctionnalité de lecture/pause

Pour commencer, nous allons ajouter un moyen de lire et de mettre en pause chacune des chansons. Pour l'instant, cela changera simplement le bouton de lecture en un bouton de pause.

Plus tard, nous utiliserons les méthodes de stockage Amplify pour obtenir notre fichier MP3 depuis S3 et le lire directement dans notre application.

Nous allons ajouter une nouvelle fonction au composant `App` appelée `toggleSong`.

```js
const toggleSong = async idx => {
    if (songPlaying === idx) {
        setSongPlaying('');
        return;
    }
    setSongPlaying(idx);
    return
}
```

Pour que cela fonctionne, nous devons également ajouter une nouvelle variable d'état à l'application. Cela sera utilisé pour stocker l'index de la chanson qui est actuellement en lecture.

```js
const [songPlaying, setSongPlaying] = useState('');
```

Avec cela configuré, nous devons apporter une modification au code JSX pour utiliser notre nouvelle fonction et nos variables.

Trouvez le premier bouton dans la div `songCard`. Nous allons ajouter un `onClick` qui appelle notre nouvelle fonction. Nous allons également utiliser une équation ternaire pour dire que si la chanson qui est en lecture est cette chanson, afficher une icône de pause au lieu d'une icône de lecture.

```js
<IconButton aria-label="play" onClick={() => toggleSong(idx)}>
    {songPlaying === idx ? <PauseIcon /> : <PlayArrowIcon />}
</IconButton>
```

Nous devons simplement importer le `PauseIcon` en haut du fichier et nous serons prêts.

```js
import PauseIcon from '@material-ui/icons/Pause';
```

![Image](https://completecoding.io/content/images/2020/09/ezgif.com-video-to-gif--2-.gif)

### Comment ajouter le stockage à Amplify

Ensuite, nous devons utiliser l'interface de ligne de commande Amplify pour ajouter le stockage à notre application. Nous pouvons commencer par aller dans notre terminal et exécuter `amplify add storage`. Cela ouvrira une interface de ligne de commande où nous devons sélectionner les options suivantes.

Veuillez sélectionner votre service = **Contenu (images, audio, vidéo, etc.)**  
Nom convivial pour votre ressource = **songStorage**  
Nom du bucket = **song-storage**  
Qui doit avoir accès = **Utilisateurs authentifiés uniquement**  
Quel accès ces utilisateurs ont-ils = **Lire** et **Créer/Mettre à jour**  
Voulez-vous un déclencheur Lambda ?  = **Non**

Avec tout cela configuré, nous devons le déployer. Nous pouvons commencer cela avec `amplify push` qui prendra un peu de temps pour déterminer ce que nous avons changé dans notre application amplify. Vous obtiendrez ensuite un petit affichage de toutes les ressources que nous avons dans Amplify.

Le seul changement est la création de notre nouvelle ressource `songStorage`. Nous pouvons sélectionner **Oui** pour continuer et cela créera notre bucket S3 pour nous.

### Comment accéder au fichier S3 via les méthodes de stockage Amplify

Une fois le déploiement terminé, nous pouvons commencer à utiliser cela pour accéder à nos chansons. De retour dans notre fonction `toggleSong`, nous allons ajouter une logique supplémentaire.

```js
const toggleSong = async idx => {
    if (songPlaying === idx) {
        setSongPlaying('');
        return;
    }

    const songFilePath = songs[idx].filePath;
    try {
        const fileAccessURL = await Storage.get(songFilePath, { expires: 60 });
        console.log('url d\'accès', fileAccessURL);
        setSongPlaying(idx);
        setAudioURL(fileAccessURL);
        return;
    } catch (error) {
        console.error('erreur d\'accès au fichier depuis s3', error);
        setAudioURL('');
        setSongPlaying('');
    }
};
```

Cela obtient le chemin du fichier à partir des données de la chanson (qui était [stocké dans Dynamo](https://completecoding.io/amplify-database/)) puis utilise `Storage.get(songFilePath, { expires: 60 });` pour obtenir une URL d'accès au fichier.

Le `{ expires: 60 }` à la fin indique que l'URL retournée ne fonctionnera que pendant 60 secondes. Après cela, vous ne pourrez plus accéder au fichier avec elle. C'est une mesure de sécurité utile pour que les gens ne puissent pas partager l'URL avec d'autres personnes qui ne devraient pas avoir accès aux fichiers.

Une fois que nous avons le fichier, nous le définissons également dans une nouvelle variable d'état en utilisant `setAudioURL`. En haut de notre `App`, nous devons ajouter cet état supplémentaire.

```js
const [audioURL, setAudioURL] = useState('');
```

Enregistrez cela et retournez dans notre application. Si nous appuyons sur le bouton de lecture et ouvrons la console, nous verrons l'URL être journalisée. C'est ce que nous allons utiliser pour jouer la chanson.

### Comment télécharger nos chansons

Nous arrivons maintenant au point où nous avons besoin de chansons à jouer. Si nous allons dans notre compte AWS et recherchons `S3` puis recherchons `song`, nous devrions trouver notre nouveau bucket S3.

Dans celui-ci, nous devons créer un nouveau dossier appelé `public`. Cela est dû au fait que les fichiers seront publics pour tous ceux qui se sont connectés à l'application. Il existe d'autres moyens de stocker des données qui sont privées et visibles uniquement par des personnes spécifiques.

À l'intérieur de ce dossier, nous devons télécharger deux chansons. J'ai deux chansons libres de droits que j'ai téléchargées appelées `epic.mp3` et `tomorrow.mp3`. Une fois qu'elles ont été téléchargées, nous devons mettre à jour nos données Dynamo pour pointer vers ces chansons.

Dans Dynamo, nous pouvons trouver notre table `Songs-(beaucoup de caractères aléatoires)`. Sous `Items`, nous devrions avoir deux enregistrements. Ouvrez le premier et changez le `filePath` en `tomorrow.mp3` et le nom en `Tomorrow`.

Enregistrez cela et ouvrez la deuxième chanson, en la changeant en `"filePath": "epic.mp3"` et `"name": "Epic"`, en enregistrant également ce fichier.

Si vous avez utilisé vos propres chansons, assurez-vous simplement que le filePath correspond au nom de fichier de vos chansons.

Nous pouvons maintenant retourner dans notre application, actualiser la page et appuyer sur lecture sur l'une des chansons. Si nous regardons dans notre console et copions l'URL qui nous est donnée, nous pouvons la coller dans un navigateur et notre chanson devrait commencer à jouer.

### Comment ajouter un lecteur multimédia à notre application

Maintenant, nous voulons pouvoir jouer notre chanson directement depuis notre application. Pour cela, nous allons utiliser une bibliothèque appelée `react-player`. Nous devons d'abord l'installer avec `npm install --save react-player`.

Dans notre application, nous pouvons ensuite l'importer en haut du fichier.

```js
import ReactPlayer from 'react-player';
```

Si nous trouvons notre `<div _className_`="songCard">, nous voulons ajouter notre lecteur après ce composant. De la même manière que nous avons montré les icônes de lecture/pause, nous allons montrer ou masquer ce lecteur en fonction de la chanson qui est en lecture.

```js
<div className="songCard">
    .. ..
</div>
{songPlaying === idx ? (
    <div className="ourAudioPlayer">
        <ReactPlayer
            url={audioURL}
            controls
            playing
            height="50px"
            onPause={() => toggleSong(idx)}
        />
    </div>
) : null}
```

Le `ReactPlayer` prend quelques paramètres. L'`url` est simplement l'URL du fichier à lire, qui est celle que nous obtenons d'Amplify Storage. `controls` permet à l'utilisateur de changer le volume ou de mettre en pause la chanson. `playing` signifie que la chanson commence à jouer dès qu'elle est chargée et `onPause` est un écouteur pour que nous puissions faire en sorte que le bouton de pause intégré fonctionne de la même manière que notre bouton de pause.

Avec tout cela fait, nous pouvons tout sauvegarder à nouveau et ouvrir notre application. Si nous appuyons sur lecture sur l'une des chansons, nous devrions voir un lecteur apparaître et la chanson sera jouée.

![Image](https://completecoding.io/content/images/2020/09/Screenshot-2020-09-11-at-07.00.57.png)

# Comment activer les téléchargements des utilisateurs

Maintenant que nous avons une application qui permet aux utilisateurs de voir toutes les chansons et de les jouer depuis S3. Pour construire sur cela, nous voulons permettre à nos utilisateurs de télécharger leurs propres chansons sur la plateforme.

%[https://youtu.be/vYY3cCvJKv0]

Nous devons d'abord créer un moyen d'ajouter une chanson et de saisir certaines informations. Nous commençons par créer un bouton `Ajouter`.

```js
{
    showAddSong ? <AddSong /> : <IconButton> <AddIcon /> </IconButton>
}

```

Nous devons également ajouter le `AddIcon` à nos imports.

```
import AddIcon from '@material-ui/icons/Add';

```

Maintenant, nous pouvons passer à la création du nouveau composant `AddSong`. Nous pouvons créer cela en bas de notre fichier `App.jsx`.

```js
const AddSong = () => {
    return (
        <div className="newSong">
            <TextField label="Titre" />
            <TextField label="Artiste" />
            <TextField label="Description" />
        </div>
    )
}

```

Nous devons également ajouter `TextField` à nos imports de material UI.

```
import { Paper, IconButton, TextField } from '@material-ui/core';

```

La prochaine chose à faire est d'ajouter la capacité d'ouvrir notre nouveau composant en contrôlant la variable `showAddSong`. Nous devons créer une nouvelle déclaration d'état à côté des autres.

```js
const [showAddSong, setShowAddNewSong] = useState(false);

```

Nous pouvons maintenant mettre à jour notre nouveau bouton `AddIcon` pour définir `showAddSong` sur vrai.

```js
<IconButton onClick={() => setShowAddNewSong(true)}>
    <AddIcon />
</IconButton>

```

Pour le changer, nous pouvons ajouter un paramètre à notre composant `AddSong` appelé `onUpload`. Lorsque cela est appelé, nous réinitialiserons showAddSong à false.

```
<AddSong
    onUpload={() => {
        setShowAddNewSong(false);
    }}
/>

```

Nous devons ensuite mettre à jour notre composant pour qu'il fonctionne avec ce nouveau paramètre et un bouton pour "téléverser" la nouvelle chanson. Ce bouton appelle une fonction dans le composant où nous ajouterons la capacité de téléverser les données, mais pour l'instant, nous appellerons simplement la fonction `onUpload`.

```js
const AddSong = ({ onUpload }) => {
    const uploadSong = async () => {
        //Téléverser la chanson
        onUpload();
    };

    return (
        <div className="newSong">
            <TextField
                label="Titre"
            />
            <TextField
                label="Artiste"
            />
            <TextField
                label="Description"
            />
            <IconButton onClick={uploadSong}>
                <PublishIcon />
            </IconButton>
        </div>
    );
};

```

Et maintenant, nous ajoutons le `PublishIcon` à nos imports et nous sommes prêts à tester cela.

```
import PublishIcon from '@material-ui/icons/Publish';

```

Lorsque nous démarrons l'application et nous connectons, nous obtenons maintenant une icône plus. En cliquant dessus, nous pouvons entrer quelques détails pour la chanson et cliquer sur téléverser.

![Image](https://completecoding.io/content/images/2020/10/photo1-1.png)

![Image](https://completecoding.io/content/images/2020/10/photo2-1.png)

### Comment mettre à jour AddSong

Maintenant, nous voulons pouvoir stocker et accéder aux données qu'un utilisateur entre dans les champs lors de l'ajout d'une chanson.

```js
const AddSong = ({ onUpload }) => {
    const [songData, setSongData] = useState({});

    const uploadSong = async () => {
        //Téléverser la chanson
        console.log('songData', songData);
        const { title, description, owner } = songData;

        onUpload();
    };

    return (
        <div className="newSong">
            <TextField
                label="Titre"
                value={songData.title}
                onChange={e => setSongData({ ...songData, title: e.target.value })}
            />
            <TextField
                label="Artiste"
                value={songData.owner}
                onChange={e => setSongData({ ...songData, owner: e.target.value })}
            />
            <TextField
                label="Description"
                value={songData.description}
                onChange={e => setSongData({ ...songData, description: e.target.value })}
            />
            <IconButton onClick={uploadSong}>
                <PublishIcon />
            </IconButton>
        </div>
    );
};

```

Nous avons également dû changer tous les TextFields pour qu'ils soient contrôlés, en passant une valeur de notre état et en fournissant un `onChange` également. Si nous sauvegardons cela et essayons d'entrer quelques détails avant de téléverser, nous devrions voir un console.log des détails dans notre console chrome.

Ensuite, nous devons ajouter la capacité de téléverser réellement la chanson. Pour cela, nous allons utiliser l'entrée html par défaut avec un type de fichier. Ajoutez ceci au JSX juste avant le bouton d'icône de téléversement.

```js
<input type="file" accept="audio/mp3" onChange={e => setMp3Data(e.target.files[0])} />

```

Comme vous l'avez peut-être remarqué, nous appelons `setMp3Data` lors du changement. C'est un peu plus d'état dans le composant AddSong.

```js
const [mp3Data, setMp3Data] = useState();

```

Maintenant que nous avons toutes les données dont nous avons besoin, nous pouvons commencer par téléverser la chanson sur S3 puis les données dans notre base de données.

Pour téléverser la chanson, nous allons utiliser la classe de stockage Amplify à nouveau. Le nom du fichier sera un UUID, donc nous devons également exécuter `npm install --save uuid` dans notre terminal puis l'importer en haut de notre fichier `import { v4 as uuid } from 'uuid';`. Nous passons ensuite les données mp3 et un contentType et nous obtenons un objet avec une clé.

```js
const { key } = await Storage.put(`${uuid()}.mp3`, mp3Data, { contentType: 'audio/mp3' });

```

Maintenant que nous avons la clé, nous pouvons créer l'enregistrement pour la chanson dans la base de données. Comme il peut y avoir plusieurs chansons avec le même nom, nous utiliserons un UUID comme ID à nouveau.

```js
const createSongInput = {
    id: uuid(),
    title,
    description,
    owner,
    filePath: key,
    like: 0,
};
await API.graphql(graphqlOperation(createSong, { input: createSongInput }));

```

Pour que cela fonctionne, nous devons importer le mutateur `createSong` qui a été créé lorsque nous avons créé le stockage dynamo avec Amplify.

```js
import { updateSong, createSong } from './graphql/mutations';

```

La dernière chose que nous devons faire est de faire en sorte que l'application récupère à nouveau les données de la base de données une fois que nous avons terminé de les téléverser. Nous pouvons faire cela en ajoutant un appel `fetchSongs` dans le cadre de la fonction `onUpload`.

```js
<AddSong
    onUpload={() => {
        setShowAddNewSong(false);
        fetchSongs();
    }}
/>
```

Maintenant, lorsque nous rechargeons la page, nous pouvons cliquer pour ajouter une nouvelle chanson, saisir les détails, sélectionner notre nouvelle chanson, la téléverser puis la lire depuis l'application.

## C'est tout, les amis !

Si vous avez aimé cet article (et les vidéos qui l'accompagnent) et que vous souhaitez m'aider, la meilleure chose que vous puissiez faire est de vous abonner à ma [Chaîne YouTube](https://www.youtube.com/c/completecoding?sub_confirmation=1). Je crée des vidéos hebdomadaires sur AWS et Serverless pour vous aider à devenir un meilleur développeur. [Abonnez-vous ici](https://www.youtube.com/c/completecoding?sub_confirmation=1)

---