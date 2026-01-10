---
title: Comment ajouter une base de données serverless à vos projets React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-01T17:16:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-serverless-database-to-react-projects-and-web-apps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/601084310a2838549dcb80e0.jpg
tags:
- name: React
  slug: react
- name: serverless
  slug: serverless
seo_title: Comment ajouter une base de données serverless à vos projets React
seo_desc: 'By Michael Bagley

  React is still one of the most popular front end Javascript libraries around. According
  to the annual Stack Overflow Developer Survey, React is the most popular front end
  library for building interfaces and the second most popular w...'
---

Par Michael Bagley

React reste l'une des bibliothèques front-end JavaScript les plus populaires. Selon l'enquête annuelle des développeurs de Stack Overflow, [React est la bibliothèque front-end la plus populaire pour construire des interfaces et le deuxième framework web le plus populaire au monde](https://insights.stackoverflow.com/survey/2020#technology-web-frameworks).

Encore plus impressionnant, sa popularité continue de croître d'année en année.

Pourquoi React continue-t-il d'être si populaire (et recherché) parmi les développeurs alors que [tant de concurrents](https://www.slant.co/topics/3790/~best-react-js-alternatives) ont tenté de le détrôner ces dernières années ?

La réponse complète à cette question peut devenir très technique, alors je vais faire de mon mieux pour la rendre courte et simple.

Premièrement, le DOM virtuel de React est rapide et efficace. Deuxièmement, la syntaxe déclarative JSX est facile à apprendre et propose des modèles de programmation que les développeurs trouvent familiers.

Ces avantages rendent React idéal pour divers types d'applications. De plus, les individus et les petites équipes continuent de choisir React pour leurs applications web.

Une exigence courante pour les applications web modernes est une base de données backend pour servir et interroger des données en temps réel. L'implémentation traditionnelle d'une base de données backend peut souvent être assez précaire et coûteuse.

Heureusement, au cours des cinq dernières années, la technologie serverless est devenue un élément central du développement d'applications modernes.

Dans ce contexte, serverless signifie que le développeur n'a pas à configurer et administrer un serveur réel pour héberger sa base de données et d'autres services backend. Au lieu de cela, il utilise un fournisseur sécurisé pour héberger son backend et s'y connecte directement depuis le code de l'application front-end. Pas besoin de s'inquiéter de la scalabilité et des systèmes.

Cette architecture d'application est relativement nouvelle, mais elle est économique et augmente considérablement la productivité. Ces avantages sont particulièrement appréciés par ceux qui utilisent React pour construire des applications modernes et de production. De plus, des services comme Easybase ont créé des bibliothèques serverless spécialement conçues pour les composants React stateful.

Cet article démontrera à quel point il est facile d'utiliser la bibliothèque [easybase-react](https://github.com/easybase/easybase-react) pour implémenter une base de données stateful et serverless dans un nouveau projet React. L'exemple ci-dessous sera une application simple de prise de notes, mais l'architecture serverless a le potentiel de rationaliser toutes sortes d'applications.

## Table des matières :

* Comment initialiser un projet React et ses composants
* Comment configurer la base de données serverless
* Tableau de base de données mutable

## **Comment initialiser un projet React et ses composants**

Pour créer un nouveau projet React, je vais utiliser la bibliothèque populaire [create-react-app](https://github.com/facebook/create-react-app) ([assurez-vous d'avoir Node installé sur votre machine](https://www.npmjs.com/get-npm)).

Pour ceux qui ne sont pas familiers avec la configuration manuelle d'un projet React, je suggère d'utiliser cette bibliothèque car elle créera un projet vide et correctement configuré.

Exécutez la commande suivante là où vous souhaitez créer votre nouveau projet :

```zsh
npx create-react-app serverless-database-app
```

Une fois cela terminé, installons la bibliothèque serverless :

```zsh
cd serverless-database-app && npm install easybase-react
```

Enfin, nous pouvons démarrer le projet :

```zsh
npm run start
```

Votre application s'ouvrira automatiquement dans votre navigateur par défaut. Le composant racine que vous voyez est dans `src/App.js` et c'est là que les principales modifications seront apportées.

Avant de nous pencher sur le fournisseur serverless, je vais simplifier le code dans `App.js`. Nous aurons deux composants : _App_ et _Cards_. `App.js` ressemblera maintenant à ce qui suit :

```jsx
import './App.css';

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <Notes />
    </div>
  );
}

function Notes() {
  const backendData = [
    { title: "Liste de courses", description: "Lait, Soupe, Pain", createdat: "01-18-2021" },
    { title: "Devoirs de maths", description: "N'oubliez pas de finir les questions 8-10 avant lundi", createdat: "12-01-2020" },
    { title: "Appeler James", description: "Demandez-lui à propos de la fête de l'entreprise.", createdat: "12-30-2020" }
  ]

  const noteRootStyle = {
    border: "2px #0af solid",
    borderRadius: 9,
    margin: 20,
    backgroundColor: "#efefef",
    padding: 6
  };

  return (
    <div style={{ width: 400 }}>
      {backendData.map(ele => 
        <div style={noteRootStyle}>
          <h3>{ele.title}</h3>
          <p>{ele.description}</p>
          <small>{ele.createdat}</small>
        </div>
      )}
    </div>
  )
}

export default App;

```

J'ai ajouté des **données d'exemple** appelées _backendData_, mais nous les remplacerons par une base de données en temps réel dans l'étape suivante. Voici une capture d'écran de mon implémentation actuelle pour référence :

![exemple React serverless avant la base de données](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-26-at-6.19.02-PM.png)

Pour des raisons de concision, le style de cette application sera très rudimentaire. Mais vous devriez certainement donner à votre propre application un look et une sensation uniques !

## **Comment configurer la base de données serverless**

Il existe de nombreux fournisseurs de backend serverless généraux ([AWS](https://aws.amazon.com/serverless/), [Google Cloud](https://cloud.google.com/), et ainsi de suite). Il existe des différences entre la fonctionnalité de ces fournisseurs. Certains sont mieux adaptés pour, peut-être, les applications mobiles ou le traitement parallèle ou l'apprentissage automatique, et ainsi de suite.

Je vais utiliser Easybase car leur plateforme propose une bibliothèque spécifique à React qui est [conçue pour les applications serverless](https://easybase.io/about/2021/01/30/What-Is-a-Serverless-Application/). Nous verrons ci-dessous à quel point ce package est rapide et facile à configurer dans le code.

J'ai utilisé cette plateforme pour plusieurs projets et de loin les aspects les plus précieux de `easybase-react` sont le _cache de session automatique_ et la _récupération sécurisée des données_. Implémenter ces modules manuellement est un véritable casse-tête et peut être un projet à part entière.

Pour commencer, nous allons apporter deux modifications à `App.js`. Premièrement, utilisons le package `easybase-react` que nous avons installé précédemment en ajoutant une ligne d'importation en haut de `App.js`. Importez _EasybaseProvider_ et _useEasybase_.

Deuxièmement, enveloppez le composant _Notes_ dans le composant _EasybaseProvider_.

`App.js` devrait maintenant ressembler à ceci. Notez que j'ai également importé le hook _useEffect_ de React.

```jsx
import './App.css';
import { EasybaseProvider, useEasybase } from 'easybase-react';
import { useEffect } from 'react';

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <EasybaseProvider>
        <Notes />
      </EasybaseProvider>
    </div>
  );
}

// ...
```

Le composant _EasybaseProvider_ donnera à tous les composants enfants un accès valide au hook _useEasybase_, une fois que nous aurons passé la configuration requise.

_EasybaseProvider_ a une prop appelée `ebconfig` qui est un fichier unique qui authentifie et sécurise toutes les connexions depuis notre projet React.

Voici comment nous pouvons obtenir un jeton `ebconfig` associé à une table de données personnalisée :

* [Connectez-vous à Easybase](https://easybase.io/) ou [créez un compte gratuit](https://app.easybase.io/?view=signup)
* Ouvrez la boîte de dialogue **Créer une table** via le bouton '+' dans le groupe de boutons en bas à gauche
* Donnez un nom à votre table et créez des colonnes qui correspondent à celles du tableau d'exemple _(title, description, createdat)_

![Easybase React créer une table](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-10.54.21-AM.png)

Je vais ajouter manuellement les lignes d'exemple du tableau _backendData_ pour référence, <ins>mais cette étape n'est pas nécessaire.</ins>

![Easybase React ajout d'une ligne à l'application Notes](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-11.02.27-AM.png)

* Accédez à l'onglet **Intégrer** et créez une nouvelle intégration **React**

![Easybase React ajouter une intégration](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-1.32.45-PM.png)

* Dans le tiroir de droite, **activez** _Active, Testing Mode,_ et la lecture et l'écriture dans _Permissions_. Ensuite, téléchargez le jeton _React_ et cliquez sur **Enregistrer** en haut à droite

![Easybase React intégration modifier 1](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-6.37.13-PM.png)

![Easybase React intégration modifier 2](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-6.37.16-PM.png)

* Placez le fichier _ebconfig.js_ nouvellement téléchargé dans le dossier `src/` de votre projet

```
 README.md
 node_modules/
 package.json
 public/
 src/
     ebconfig.js   <---
     App.css
     App.js
     index.css
     index.js
     ...
```

* Enfin, **importez** ce fichier dans `App.js` et passez-le en tant que prop `ebconfig` de _EasybaseProvider_ comme suit :

```jsx
import './App.css';
import { EasybaseProvider, useEasybase } from 'easybase-react';
import { useEffect } from 'react';
import ebconfig from './ebconfig';

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <EasybaseProvider ebconfig={ebconfig}>
        <Notes />
      </EasybaseProvider>
    </div>
  );
}

// ...
```

Et voilà, notre projet est configuré pour la fonctionnalité serverless. Il ne reste plus qu'à utiliser les fonctions fournies par le hook `useEasybase`, ce que nous ferons dans la section suivante.

[Consultez ce guide pour plus d'informations sur l'utilisation de React ou React Native avec l'architecture serverless](https://easybase.io/react/).

Si votre projet doit gérer des utilisateurs individuels avec une authentification sécurisée, utilisez l'onglet **Projets** plutôt qu'une simple intégration **React**.

[Des informations sur l'authentification des utilisateurs React peuvent être trouvées dans cet article de freeCodeCamp sur le flux de travail des projets Easybase](https://www.freecodecamp.org/news/build-react-native-app-user-authentication/).

## **Tableau de base de données mutable**

Maintenant que nous avons correctement configuré notre backend, les composants enfants de _EasybaseProvider_ peuvent accéder au hook _useEasybase_. Ce hook fournit les fonctions essentielles nécessaires pour accéder à nos données distantes.

Commençons par importer trois fonctions : _configureFrame_, _sync_, et _Frame_, dans notre composant _Notes_ avec `const { Frame, sync, configureFrame } = useEasybase();`.

Lorsque notre composant est monté pour la première fois, nous voulons configurer notre _Frame_ pour obtenir les 10 premières entrées de notre base de données, **NOTES APP**. _Frame_ agit comme un **tableau de base de données stateful** dans lequel l'appel de _sync_ normalisera les modifications locales avec les modifications de la base de données backend.

```jsx
function Notes() {
  const { Frame, sync, configureFrame } = useEasybase();

  useEffect(() => {
    configureFrame({ tableName: "NOTES APP", limit: 10 });
    sync();
  }, []);

  const noteRootStyle = {
    border: "2px #0af solid",
    borderRadius: 9,
    margin: 20,
    backgroundColor: "#efefef",
    padding: 6
  };

  return (
    <div style={{ width: 400 }}>
      {Frame().map(ele => 
        <div style={noteRootStyle}>
          <h3>{ele.title}</h3>
          <p>{ele.description}</p>
          <small>{String(ele.createdat).slice(0, 10)}</small>
        </div>
      )}
    </div>
  )
}
```

_Sync_ gérera automatiquement les processus backend nécessaires. Plus important encore, il re-rendra notre composant avec les nouvelles données dans _Frame_.

Si nous reconstruisons notre application, les nouvelles notes affichées seront les mêmes que celles présentes dans notre table de données. _Félicitations, vous utilisez une base de données serverless !_

Amusons-nous un peu plus en ajoutant un bouton qui poussera une nouvelle note vers Easybase et rendra votre application en conséquence.

Créez un nouveau composant appelé _NewNoteButton_. Obtenez les fonctions _sync_ et _Frame_ du hook _useEasybase_.

Je vais placer ce bouton en haut à gauche de la fenêtre en utilisant le positionnement absolu. Lorsque l'utilisateur clique sur ce bouton, mon composant obtiendra un nouveau titre et une nouvelle description de l'utilisateur et les publiera sur Easybase en utilisant _Frame_ et _sync_.

Placez ce composant nouvellement créé sous le composant _Notes_ dans le _EasybaseProvider_.

```jsx

function App() {
  return (
    <div className="App" style={{ display: "flex", justifyContent: "center" }}>
      <EasybaseProvider ebconfig={ebconfig}>
        <Notes />
        <NewNoteButton />
      </EasybaseProvider>
    </div>
  );
}

// ...

function NewNoteButton() {
  const { Frame, sync } = useEasybase();

  const buttonStyle = {
    position: "absolute",
    left: 10,
    top: 10,
    fontSize: 21
  }

  const handleClick = () => {
    const newTitle = prompt("Veuillez entrer un titre pour votre note");
    const newDescription = prompt("Veuillez entrer votre description");
    
    Frame().push({
      title: newTitle,
      description: newDescription,
      createdat: new Date().toISOString()
    })
    
    sync();
  }

  return <button style={buttonStyle} onClick={handleClick}>4c34c3 Ajouter une note 4c34c3</button>
}
```

Mon implémentation recueille le titre et la description souhaités par l'utilisateur via la [fonction native prompt](https://www.w3schools.com/jsref/met_win_prompt.asp), mais votre application de production nécessitera probablement une solution d'entrée plus robuste. Cela fonctionnera très bien pour une démonstration, cependant.

![projet React serverless ajouter une note](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-8.20.09-PM.png)

Remarquez le nouveau bouton dans le coin supérieur droit de l'écran. Cliquer dessus fera apparaître deux zones de texte. Après avoir terminé, le composant _Notes_ se re-rendra après l'appel de _sync_ qui affichera votre nouvelle entrée.

![projet React serverless avec une note ajoutée](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-27-at-8.22.01-PM.png)

Ces modifications seront instantanément visibles dans votre table Easybase, alors n'hésitez pas à y apporter des modifications également !

## Conclusion

[Les chiffres ne mentent pas](https://github.com/facebook/react/graphs/contributors) – React est robuste, mature et aimé par les développeurs. La communauté open-source a vraiment adopté le projet, [avec plus de 1500 contributeurs](https://github.com/facebook/react/graphs/contributors).

Cette bibliothèque s'est avérée être l'une des meilleures façons de créer des interfaces belles et haute performance. En fait, vous pouvez même [déployer votre projet React directement sur GitHub Pages](https://github.com/gitname/react-gh-pages).

L'utilisation de React avec serverless est devenue une évidence. L'adoption de cette technologie scalable a considérablement augmenté. Jetez un coup d'œil au graphique Google Trends pour le terme « serverless » au cours des 8 dernières années.

![Google Trends pour 'serverless'](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-28-at-2.32.12-PM.png)
_Google Trends pour 'serverless'_

Cette technologie a permis aux développeurs de déployer des applications scalables de niveau entreprise à une fraction du coût et sans les frais généraux conventionnels. En débloquant les outils traditionnellement disponibles pour ceux disposant de ressources abondantes, la technologie serverless continue d'encourager les développeurs à transformer leurs idées en réalité.