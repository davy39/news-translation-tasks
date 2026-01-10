---
title: Tutoriel de projet Full Stack – Créer une application de notes avec React et
  Node.js
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2023-09-28T14:10:44.000Z'
originalURL: https://freecodecamp.org/news/full-stack-project-tutorial-create-a-notes-app-using-react-and-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/react-node-notes-app-screenshot-1.png
tags:
- name: full stack
  slug: full-stack
- name: node js
  slug: node-js
- name: postgres
  slug: postgres
- name: React
  slug: react
seo_title: Tutoriel de projet Full Stack – Créer une application de notes avec React
  et Node.js
seo_desc: "Hey there! Ready to build something cool? In this tutorial, we're going\
  \ to create a full stack notes app using React, Node.js, and PostgreSQL. \nWe'll\
  \ start from scratch and end up with a fully functioning app where you can create,\
  \ edit, and delete no..."
---

Salut ! Prêt à construire quelque chose de cool ? Dans ce tutoriel, nous allons créer une application de notes full stack en utilisant React, Node.js et PostgreSQL. 

Nous allons partir de zéro et finir avec une application entièrement fonctionnelle où vous pourrez créer, modifier et supprimer des notes. De plus, nous ajoutons une validation à la fois sur l'UI et le backend pour garder les choses sous contrôle !

Ce guide est tout sur vous donner l'expérience réelle de la construction d'une application web. Vous allez apprendre comment chaque pièce du puzzle s'assemble – de la magie du front-end avec React, aux merveilles du côté serveur avec Node.js, et en stockant toutes les bonnes choses dans une base de données PostgreSQL. Et hey, nous nous assurons qu'elle a l'air bien et fonctionne bien sur les écrans mobiles aussi !

À la fin de cela, vous aurez une bonne prise sur le développement full stack avec React et Node, que vous pourrez emporter avec vous dans de futurs projets. C'est tout sur l'apprentissage en faisant, et l'acquisition des compétences pour donner vie à vos idées. Alors, prenez une tasse de café, retroussez vos manches, et commençons à coder !

## Prérequis

Puisque nous allons nous concentrer sur la construction d'un projet, il y a quelques prérequis qui seront nécessaires pour tirer le meilleur parti de ce tutoriel :

* Certaines connaissances sur les concepts de développement web (frontend, backend, bases de données, API, REST).
* Certaines connaissances en JavaScript (variables, fonctions, objets, tableaux, etc.).
* Compréhension de base de React (comment créer des composants, ajouter des styles, travailler avec l'état).
* Compréhension de base de Node.js/Express (travailler avec les API).

## Table des matières


- [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
- [Défi : Essayez par vous-même d'abord !](#heading-defi-essayez-par-vous-meme-d'abord)
- [Tutoriel vidéo](#heading-tutoriel-video)
- [PARTIE 1 – Créer l'UI](#heading-partie-1-creer-lui)
- [PARTIE 2 - Créer le Backend](#heading-partie-2-creer-le-backend)
- [PARTIE 3 - Connecter l'UI au Backend](#heading-partie-3-connecter-lui-au-backend)
- [La Fin - Pourquoi ne pas essayer les défis bonus ?](#heading-la-fin-pourquoi-ne-pas-essayer-les-defis-bonus)

## Ce que nous allons construire

Dans ce tutoriel, nous allons construire une application de notes full stack à partir de zéro, en utilisant React, Node.js et PostgreSQL, avec les fonctionnalités suivantes :

* Créer/Modifier/Supprimer des Notes
* Validation sur l'UI et le Backend
* Réactif sur les écrans mobiles

## Défi : Essayez par vous-même d'abord !

Si vous souhaitez tenter ce projet vous-même d'abord sans regarder le tutoriel, voici quelques indices :

* Abordez une petite partie à la fois. Par exemple, vous vous concentreriez sur le fonctionnement de l'UI d'abord, et aborderez les API plus tard.
* Pensez à vos données – Que devez-vous stocker ? Quelle structure de données (par exemple, des tableaux) utiliserez-vous pour retourner les données via l'API ? Comment allez-vous rendre ces données sur l'UI ?
* N'oubliez pas la validation et la gestion des erreurs. Que se passera-t-il si l'utilisateur essaie d'enregistrer une note sans champ de titre ? Comment allez-vous empêcher cela ? (Indice : Les formulaires et le champ `required` seront vos amis ici)
* N'oubliez pas qu'il n'y a pas de manière parfaite de compléter un projet. Le tutoriel ci-dessous est une manière d'aborder le problème. Vous pouvez choisir d'aller différemment, en mettant votre propre style unique sur les choses. L'essentiel est que vous commenciez !

Si vous avez besoin de plus d'aide pour commencer par vous-même, vous pouvez trouver plus d'indices et de conseils, du code de démarrage, et du code terminé que vous pouvez consulter sur [codecoyotes.com](https://www.codecoyotes.com/projects/react-node-notes-app).

## Tutoriel vidéo

%[https://youtu.be/2MoSzSlAuNk?si=nlblr0d40RslVYJ-]

## PARTIE 1 – Créer l'UI

Nous allons commencer ce tutoriel en créant l'UI en utilisant quelques données fictives. Cela nous permet de nous concentrer sur notre style, et sur l'apparence des choses, sans avoir à nous soucier de créer un backend tout de suite.

### Créer une nouvelle application React

D'accord, d'abord, créons la structure de notre projet. Ouvrez votre terminal et naviguez vers votre bureau. Notre prochaine étape est de créer un nouveau dossier qui contiendra à la fois notre code UI et backend. Nommons-le `notes-app` :

```bash
mkdir notes-app

```

Une fois cela fait, naviguez dans le répertoire nouvellement créé `notes-app` :

```bash
cd notes-app

```

Ensuite, nous allons créer une nouvelle application React en utilisant TypeScript comme modèle. Nous allons utiliser la commande `npx create-react-app` pour cela, en spécifiant TypeScript comme modèle :

```bash
npx create-react-app notes-app --template typescript

```

Après avoir appuyé sur Entrée, le processus peut prendre quelques minutes pour installer tous les paquets nécessaires. Une fois terminé, ouvrez le dossier `notes-app` dans Visual Studio Code ou votre IDE préféré.

Dans Visual Studio Code, vous devriez voir que `notes-app` est au niveau supérieur de votre répertoire. Au fur et à mesure que le cours avance, nous ajouterons un répertoire `notes-app-server` également pour garder tout le code ensemble au même endroit.

Maintenant, ouvrez un nouveau terminal dans votre IDE et naviguez vers le répertoire de votre application React (supposons que vous l'avez nommé `notes-app`) :

```bash
cd notes-app

```

Ensuite, exécutez la commande suivante pour démarrer le serveur de développement front-end :

```bash
npm start

```

Si tout se passe bien, votre navigateur s'ouvrira automatiquement et affichera votre nouvelle application React. Vous devriez voir un logo React en rotation, parmi d'autres actifs par défaut.

Enfin, nettoyons le code de démarrage pour avoir un point de départ propre pour notre application. Ouvrez `src/App.tsx` dans votre IDE et supprimez son contenu. Ce sera notre nouveau point de départ pour construire l'application.

### Ajouter des éléments d'UI

D'accord, la première chose que nous allons faire est de mettre en place certains de nos composants d'UI. Cela consistera en le balisage général et le CSS, sans impliquer de JavaScript. Cela nous donne un aperçu de la manière dont nous envisageons la mise en page, sans avoir à nous soucier des appels d'API ou des interactions avec la base de données à ce stade.

Nous allons naviguer vers `.App.tsx` et créer un nouveau composant. Assurez-vous d'importer notre feuille de style depuis `App.css`. La première chose à ajouter est une `div` avec un nom de classe `AppContainer`. Cela aidera à positionner notre formulaire et la grille CSS pour nos notes.

Dans cette `div`, nous inclurons nos balises de formulaire. Ici, nous ajouterons un champ de saisie pour le titre – c'est là que l'utilisateur peut entrer le titre de la note. Nous inclurons également une zone de texte pour le contenu de la note. Ces deux champs seront définis sur `required`, permettant les messages de validation natifs du navigateur si l'utilisateur essaie de soumettre un formulaire incomplet. 

En bas du formulaire, nous inclurons un bouton de type `submit`, qui gérera les soumissions de formulaire lorsqu'il sera cliqué.

Sur la droite, nous ajouterons une `div` pour contenir nos notes. Cela sera structuré comme une grille CSS. Initialement, nous remplirons cette grille avec une seule note pour voir à quoi elle ressemble.

Pour notre note, nous aurons un en-tête contenant un bouton de suppression situé sur le côté droit. Nous afficherons le titre saisi par l'utilisateur – à des fins de démonstration, nous utilisons un titre fictif. Nous inclurons également le contenu que l'utilisateur a saisi.

Enfin, nous exporterons notre composant tout en bas.

### Code complet pour cette section

```jsx
import "./App.css";

const App = () => {
  return (
    <div className="app-container">
      <form className="note-form">
        <input placeholder="Titre" required />
        <textarea placeholder="Contenu" rows={10} required />

        <button type="submit">Ajouter une note</button>
      </form>
      <div className="notes-grid">
        <div className="note-item">
          <div className="notes-header">
            <button>x</button>
          </div>
          <h2>Titre de la note</h2>
          <p>Contenu de la note</p>
        </div>
      </div>
    </div>
  );
};

export default App;

```

### Ajouter du CSS

#### Démarrer l'application

Tout d'abord, ouvrons un terminal et tapons `npm start`. Cela lancera l'application dans le navigateur. Comme vous pouvez le voir sur le côté droit, l'apparence n'est pas encore géniale. Cela est dû au fait que nous n'avons appliqué aucun style. Pour corriger cela, nous allons naviguer vers `App.css` et styliser les classes que nous avons ajoutées précédemment.

Vous pouvez télécharger les styles depuis le lien dans la description si vous préférez copier et coller. Alternativement, n'hésitez pas à suivre la vidéo et à faire pause si nécessaire. N'oubliez pas, ces styles ne sont que des exemples pour l'apprentissage – ils n'ont pas besoin d'être parfaits.

#### Styliser le corps et le conteneur de l'application

Dans `App.css`, la première chose que nous allons faire est d'ajouter quelques styles au `body`. Nous allons lui donner un fond gris et une marge pour empêcher l'application de toucher les bords de la fenêtre du navigateur. Ensuite, nous allons styliser notre `App Container`.

Nous concevons cela d'abord pour les mobiles, ce qui signifie que les styles par défaut cibleront les écrans mobiles. Nous utiliserons des requêtes média pour les affichages plus grands. Cette approche est facultative, mais souvent il est plus facile de commencer par les conceptions mobiles.

Pour les écrans mobiles, nous voulons que notre `App Container` utilise par défaut une mise en page à une seule colonne, en empilant notre formulaire et la grille de notes l'un au-dessus de l'autre.

#### Utiliser les requêtes média

Nous allons ajouter une requête média spécifiant que pour les écrans plus grands que 600 pixels, nous utiliserons une mise en page à deux colonnes. Nous allons définir cela en utilisant `grid-template-columns`. 

La première colonne aura une largeur de 200 pixels, accommodant le formulaire. La deuxième colonne utilisera `1fr`, remplissant l'espace restant. Un écart de 20 pixels séparera les deux colonnes.

#### Styliser la grille de notes

Ensuite, stylisons notre grille de notes. Nous allons utiliser CSS grid et définir `grid-template-columns`. 

Chaque élément de la grille aura une largeur minimale de 250 pixels et peut s'étendre pour remplir l'espace disponible. Ne vous inquiétez pas si cela semble confus – cela deviendra clair bientôt.

Nous allons également définir `grid-auto-rows` pour nous assurer que chaque ligne a une hauteur minimale de 250 pixels, accommodant des notes de différentes tailles tout en maintenant une hauteur de ligne cohérente.

#### Styliser les notes individuelles

Pour chaque note, nous allons utiliser Flexbox et définir `flex-direction` sur colonne, empilant l'en-tête, le titre et le contenu verticalement. Nous allons également ajouter quelques styles de base comme la bordure, le remplissage et la couleur de fond. Une ombre de boîte fournira une touche finale.

#### Styliser l'en-tête et le bouton de suppression

L'en-tête utilisera également Flexbox, et nous allons définir `justify-content` sur `flex-end` pour aligner le bouton de suppression à droite. Le bouton recevra des styles personnalisés pour un look soigné.

#### Styliser le formulaire

Enfin, nous allons styliser le formulaire dans la colonne de gauche. Encore une fois, nous allons utiliser Flexbox avec une mise en page en colonne et un écart de 20 pixels entre les éléments. La zone de texte et les champs de saisie auront des bordures, un remplissage et des polices redimensionnées. Nous allons également styliser le bouton de soumission et ajouter des effets de survol.

#### Code complet pour cette section

```css
body {
  margin: 20px;
  background-color: lightgrey;
}

.app-container {
  grid-template-columns: 1fr;
}

@media (min-width: 600px) {
  .app-container {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 20px;
  }
}

.notes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: minmax(250px, auto);
  gap: 20px;
}

.note-item {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  background-color: #f9f9f9;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.notes-header {
  display: flex;
  justify-content: flex-end;
}

.notes-header button {
  font-size: 16px;
  background: transparent;
  border: none;
  cursor: pointer;
  max-width: fit-content;
}

h2 {
  margin: 0;
}

.note-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

textarea,
input {
  border-radius: 5px;
  border: 1px solid black;
  padding: 10px;
  font-size: 16px;
}

.note-form button {
  border-radius: 5px;
  background-color: rgb(64, 154, 184);
  border: none;
  padding: 10px;
  font-size: 16px;
  color: white;
}

.note-form button:hover {
  background-color: rgb(106, 175, 198);
  cursor: pointer;
}

.edit-buttons {
  display: flex;
  justify-content: space-evenly;
  gap: 5px;
}

.edit-buttons button {
  flex: 1;
}

.edit-buttons button:last-of-type {
  background-color: rgb(220, 89, 89);
  color: white;
}

```

### Ajouter des notes fictives

#### Ajouter des notes fictives pour tester la grille CSS

Maintenant que nous avons notre CSS en place, l'étape suivante consiste à ajouter des notes fictives à notre composant `App` pour tester la réactivité de notre grille CSS. Pour ce faire, nous allons naviguer vers `App.tsx` et importer le hook `useState` de React.

À l'intérieur de notre composant `App`, nous allons stocker les notes dans le hook `useState`. Chaque fois que vous avez des éléments d'UI qui peuvent changer, il est bon de les gérer dans l'état. Nous allons l'initialiser avec un tableau fictif de notes, où chaque note a un `id`, un `title` et un `content` :

```javascript
const [notes, setNotes] = useState<Note[]>([
{
  id: 1,
  title: "test note 1",
  content: "bla bla note1",
},
{
  id: 2,
  title: "test note 2 ",
  content: "bla bla note2",
},
{
  id: 3,
  title: "test note 3",
  content: "bla bla note3",
},
{
  id: 4,
  title: "test note 4 ",
  content: "bla bla note4",
},
{
  id: 5,
  title: "test note 5",
  content: "bla bla note5",
},
{
  id: 6,
  title: "test note 6",
  content: "bla bla note6",
},
]);

```

Considérez cela comme la simulation d'un appel d'API et le stockage des données retournées dans l'état. La structure de ces données sera similaire à ce que nous recevrons de nos requêtes d'API lorsque nous construirons finalement notre backend.

#### Mapper les notes aux composants

Avec notre tableau de notes dans l'état, nous pouvons maintenant utiliser la fonction `map` dans notre grille de notes pour afficher le balisage de chaque note. La fonction `map` s'exécutera autant de fois qu'il y a de notes dans le tableau. Au lieu de coder en dur le `title` et le `content`, nous allons extraire ces valeurs de chaque objet `note` :

```jsx
<div className="notes-grid">
  {notes.map((note) => (
    <div className="note-item">
      <div className="notes-header">
        <button>x</button>
      </div>
      <h2>{note.title}</h2>
      <p>{note.content}</p>
    </div>
  ))}
</div>

```

#### Vérifier la réactivité

Après ces étapes, vous devriez voir quatre notes affichées dans le navigateur, remplies avec les valeurs des objets du tableau.

Pour vérifier que notre mise en page est réactive, vous pouvez changer la taille de la fenêtre. Vous verrez que les notes s'ajustent en fonction de la taille de la fenêtre. Lorsque la fenêtre est à sa plus petite taille—simulant un écran mobile—le formulaire s'empilera verticalement au-dessus de la grille de notes.

### Enregistrer le formulaire de note

Maintenant que nous avons notre UI configurée, concentrons-nous sur l'ajout de fonctionnalités au formulaire qui nous permet de créer une nouvelle note. Initialement, nous allons l'implémenter pour l'UI. Plus tard, nous rendrons les données persistantes en les reliant au backend, que nous construirons séparément.

#### Utiliser l'état pour les entrées de formulaire dans React

Dans React, lors de la gestion des formulaires, il est considéré comme une bonne pratique de maintenir une variable d'état pour chaque entrée de formulaire. Cela permet à React de contrôler ces entrées, facilitant ainsi la capture de leurs valeurs et leur utilisation de manière programmatique.

Dans notre code, nous avons deux entrées de formulaire : une pour le titre et une autre pour le contenu. Pour celles-ci, nous allons configurer deux variables d'état appelées `title` et `content` :

```javascript
const [title, setTitle] = useState("");
const [content, setContent] = useState("");

```

Pour le champ de titre, nous lions sa valeur à la variable d'état `title` et mettons à jour cet état chaque fois que l'utilisateur tape dans le champ :

```javascript
<input
  value={title}
  onChange={(event) => setTitle(event.target.value)}
  placeholder="Titre"
  required
></input>

```

De même, nous allons gérer la zone de texte pour le contenu :

```javascript
<textarea
  value={content}
  onChange={(event) => setContent(event.target.value)}
  placeholder="Contenu"
  rows={10}
  required
></textarea>

```

#### Gérer la soumission du formulaire

Après avoir lié nos entrées de formulaire à des variables d'état, l'étape suivante consiste à ajouter une fonction qui gère la soumission du formulaire. Nous nommerons cette fonction `handleAddNote` :

```javascript
const handleAddNote = (event: React.FormEvent) => {
  event.preventDefault();
  console.log("title: ", title);
  console.log("content: ", content);
};

```

Dans cette fonction, nous spécifions le type de paramètre comme `React.FormEvent` pour satisfaire l'exigence de typage de TypeScript. Nous appelons également `event.preventDefault()` pour empêcher le formulaire de se soumettre et de rafraîchir la page, ce qui est son comportement par défaut. Ensuite, nous enregistrons les variables d'état `title` et `content` dans la console.

Enfin, nous allons connecter cette fonction à l'événement `onSubmit` dans notre formulaire :

```jsx
<form onSubmit={handleAddNote}>{/* ...form inputs here... */}</form>

```

#### Tester le formulaire

Pour tester cette configuration, ouvrez la console du navigateur, saisissez un titre et un contenu, puis cliquez sur le bouton "Ajouter une note". Vous devriez voir les valeurs du titre et du contenu enregistrées dans la console, confirmant que notre formulaire capture les entrées comme prévu.

### Gérer la fonctionnalité "Ajouter une note"

Maintenant que nous avons configuré nos variables d'état pour le titre et le contenu, nous pouvons procéder à l'implémentation de la fonction qui gère l'ajout d'une nouvelle note. Cette fonction créera un nouvel objet de note et l'ajoutera à notre tableau `notes`, mettant ainsi à jour l'UI.

#### Créer un nouvel objet de note

Tout d'abord, créons un nouvel objet de note et spécifions son type comme `Note`, en tirant parti du système de types de TypeScript :

```javascript
const newNote: Note = {
  id: notes.length + 1,
  title: title,
  content: content,
};

```

Parce que nous avons explicitement typé notre objet, l'IntelliSense de TypeScript nous assistera dans le peuplement de l'objet, garantissant que nous ne manquons aucune propriété requise. Pour l'instant, nous allons définir l'`id` sur la longueur du tableau `notes` actuel plus un, bien que cet `id` sera finalement généré par notre base de données backend.

#### Mettre à jour l'état avec la nouvelle note

Une fois que nous avons notre nouvel objet de note, nous devons mettre à jour notre tableau d'état `notes`. Nous allons utiliser la fonction `setNotes` à cet effet :

```javascript
setNotes([newNote, ...notes]);

```

Le nouvel objet de note sera le premier élément dans le nouveau tableau `notes`, suivi des notes existantes, que nous allons étaler dans le nouveau tableau en utilisant l'opérateur de propagation. Cela crée effectivement une copie de l'ancien tableau `notes` et l'insère dans le nouveau.

#### Effacer les entrées du formulaire

Enfin, réinitialisons les variables d'état `title` et `content` à des chaînes vides, améliorant ainsi l'expérience utilisateur en effaçant le formulaire une fois qu'une note est ajoutée :

```javascript
setTitle("");
setContent("");

```

#### Tester la fonctionnalité

Et c'est tout ! Si vous allez maintenant dans le navigateur, saisissez un titre et un contenu, puis cliquez sur "Ajouter une note", vous verrez votre nouvelle note apparaître en haut de la liste, et les champs du formulaire seront effacés, prêts pour une nouvelle entrée.

### Gérer la fonctionnalité "Mettre à jour une note"

Dans cette section, nous allons nous concentrer sur l'implémentation de la fonctionnalité qui permet aux utilisateurs de mettre à jour une note existante. Lorsque l'utilisateur clique sur une note, nous voulons remplir les champs `title` et `content` de notre formulaire avec les valeurs existantes de la note. Nous allons également ajouter un bouton "Enregistrer" et "Annuler".

#### Nettoyage et configuration initiale

Tout d'abord, nettoyons notre code en supprimant toutes les instructions `console.log` – elles ne sont plus nécessaires :

```tsx
const [selectedNote, setSelectedNote] = useState<Note | null>(null);

```

#### Suivre la note sélectionnée

Pour suivre la note sur laquelle l'utilisateur a cliqué, nous allons créer une nouvelle variable d'état appelée `selectedNote`. Cette variable d'état aura un type de `Note` ou `null` pour tenir compte de la possibilité qu'aucune note ne soit sélectionnée. Nous allons initialiser cet état à `null`.

#### Créer le gestionnaire de clic

Ensuite, créons une fonction nommée `handleNoteClick` pour gérer l'événement de clic de l'utilisateur sur une note. Cette fonction prendra un objet `note` comme argument :

```javascript
const handleNoteClick = (note: Note) => {
  setSelectedNote(note);
  setTitle(note.title);
  setContent(note.content);
};

```

Dans cette fonction, nous allons utiliser `setSelectedNote` pour sauvegarder la note cliquée dans notre état `selectedNote`. De plus, nous allons remplir les variables d'état `title` et `content` avec les valeurs de la note cliquée.

#### Mettre à jour l'UI

Dans le JSX pour le rendu de chaque note, ajoutez un événement `onClick` à l'élément `div` de niveau supérieur pour chaque note. Appelez la fonction `handleNoteClick` et passez-lui l'objet `note` :

```jsx
<div key={note.id} className="note-item" onClick={() => handleNoteClick(note)}>
  <div className="notes-header">
    <button>x</button>
  </div>
  <h2>{note.title}</h2>
  <p>{note.content}</p>
</div>

```

Puisque nous itérons sur les notes en utilisant la fonction `map`, ce gestionnaire `onClick` sera ajouté à chaque note automatiquement.

#### Enregistrer les modifications de l'utilisateur

Maintenant que nous avons la capacité pour l'utilisateur de modifier une note, nous allons implémenter la fonctionnalité pour enregistrer les modifications qu'il apporte au `title` et au `content` d'une note dans notre état.

#### La fonction `handleUpdateNote`

Créons une nouvelle fonction appelée `handleUpdateNote` :

```javascript
const handleUpdateNote = (event: React.FormEvent) => {
  event.preventDefault();

  if (!selectedNote) {
    return;
  }

  const updatedNote: Note = {
    id: selectedNote.id,
    title: title,
    content: content,
  };

  const updatedNotesList = notes.map((note) => (note.id === selectedNote.id ? updatedNote : note));

  setNotes(updatedNotesList);
  setTitle("");
  setContent("");
  setSelectedNote(null);
};

```

Dans cette fonction, nous utilisons `event.preventDefault()` pour empêcher le formulaire de se soumettre automatiquement lorsque le bouton "Enregistrer" est cliqué. Nous validons également si une note est sélectionnée. Si ce n'est pas le cas, nous quittons la fonction tôt pour éviter les erreurs potentielles.

Ensuite, nous formons un objet de note mis à jour basé sur l'`id` de la note sélectionnée et le `title` et `content` mis à jour. Après cela, nous utilisons la fonction `map` pour générer un nouveau tableau de notes, en remplaçant la note sélectionnée par notre note mise à jour là où l'`id` correspond. Le tableau mis à jour est ensuite défini dans notre état en utilisant la fonction `setNotes`. Enfin, nous réinitialisons nos valeurs d'état `title`, `content` et `selectedNote` à leurs états initiaux.

#### La fonction `handleCancel`

Nous allons également implémenter une simple fonction `handleCancel` pour réinitialiser notre formulaire et la note sélectionnée lorsque l'utilisateur décide de ne pas procéder à une mise à jour :

```javascript
const handleCancel = () => {
  setTitle("");
  setContent("");
  setSelectedNote(null);
};

```

#### Mettre à jour le JSX

Introduisons un rendu conditionnel dans notre JSX pour afficher les boutons appropriés en fonction de si une note est sélectionnée pour édition ou non :

```jsx
<form
  className="note-form"
  onSubmit={(event) => (selectedNote ? handleUpdateNote(event) : handleAddNote(event))}
>
  {/* ... other form elements ... */}
  {selectedNote ? (
    <div className="edit-buttons">
      <button type="submit">Enregistrer</button>
      <button onClick={handleCancel}>Annuler</button>
    </div>
  ) : (
    <button type="submit">Ajouter une note</button>
  )}
</form>

```

Dans l'événement `onSubmit` de notre formulaire, nous avons ajouté une condition. Si une note est sélectionnée, nous déclencherons la fonction `handleUpdateNote`. Sinon, la fonction `handleAddNote` sera exécutée.

#### Tester l'implémentation

Après avoir incorporé ces changements, exécutez votre application. Lorsque vous sélectionnez une note, faites des modifications et cliquez sur "Enregistrer", vous observerez que la note est mise à jour.

### Supprimer des notes de l'UI

La dernière fonctionnalité dont nous avons besoin sur le frontend avant de passer au développement du backend est la capacité à supprimer des notes. Vous vous souvenez que nous avons ajouté un petit bouton "X" à chaque note à cet effet. Cliquer sur ce bouton devrait supprimer la note de l'UI. Revenons au fichier `App.tsx` et implémentons cela.

#### La fonction `deleteNote`

Tout d'abord, créez une fonction nommée `deleteNote` comme suit :

```javascript
const deleteNote = (event: React.MouseEvent, noteId: number) => {
  event.stopPropagation();

  const updatedNotes = notes.filter((note) => note.id !== noteId);

  setNotes(updatedNotes);
};

```

Cette fonction prend deux paramètres : l'objet `event` et le `noteId`. La ligne `event.stopPropagation()` est cruciale ici car le bouton de suppression est imbriqué dans une note cliquable. Elle empêche l'événement `deleteNote` d'interférer avec l'événement de clic sur la note elle-même. Cela est particulièrement important lors de la gestion d'événements `onClick` imbriqués.

#### La logique de filtrage

Le cœur de la fonctionnalité de suppression réside dans la méthode `filter` appliquée au tableau `notes`. Cette méthode parcourt le tableau et applique une fonction à chaque élément, un peu comme la méthode `map`. Elle ne retournera que les notes dont les ID ne correspondent pas au `noteId` fourni, supprimant ainsi efficacement la note sélectionnée.

Nous sauvegardons ce nouveau tableau filtré dans une variable appelée `updatedNotes` puis mettons à jour notre état avec celle-ci en appelant `setNotes(updatedNotes)`.

#### Ajouter l'événement `onClick`

Après avoir défini la fonction `deleteNote`, attachez-la au bouton de suppression dans la note. Passez l'événement et l'ID de la note, comme ceci :

```jsx
<button onClick={(event) => deleteNote(event, note.id)}>x</button>

```

#### Tester la fonctionnalité

Maintenant, si vous exécutez votre application et cliquez sur le bouton de suppression d'une note donnée, vous verrez que la note disparaît de l'UI.

## PARTIE 2 - Créer le Backend

Après avoir implémenté les fonctionnalités de l'UI, il est temps de configurer un backend qui nous permet de persister les notes lorsque l'utilisateur les ajoute, les modifie ou les supprime. Pour cela, créez un nouveau dossier dans votre projet au niveau supérieur et nommez-le `notes-app-server`. Même si cela peut sembler que le code du serveur est dans le même répertoire que l'UI, ils sont entièrement séparés et fonctionneront indépendamment.

### Configuration initiale

1. Ouvrez votre terminal et naviguez vers le dossier `notes-app-server` que vous venez de créer.
2. Exécutez les commandes suivantes :

```bash
npm init
npm i ts-node typescript nodemon @types/cors @types/express @types/node --save-dev
npm i @prisma/client cors express prisma
npx tsc --init

```

* `npm init` : Initialise un nouveau module npm et vous donne accès aux paquets npm.
* `npm i ... --save-dev` : Installe les dépendances de développement comme TypeScript et les définitions de types.
* `npm i ...` : Installe les dépendances de production comme Express et Prisma.

### Modifier `package.json`

Après avoir exécuté les commandes ci-dessus, naviguez vers votre `package.json` et mettez à jour la section `scripts` avec :

```json
"start": "npx nodemon"

```

Ce script utilise nodemon pour le rechargement à chaud.

### Implémenter le serveur

Maintenant, dans le répertoire `notes-app-server`, créez un dossier `src` et à l'intérieur, un fichier `index.ts`. Insérez le code suivant :

```javascript
import express from "express";
import cors from "cors";

const app = express();

app.use(express.json());
app.use(cors());

app.get("/api/notes", async (req, res) => {
  res.json({ message: "success!" });
});

app.listen(5000, () => {
  console.log("server running on localhost:5000");
});

```

1. `import express and cors` : Nous importons les bibliothèques requises pour notre serveur.
2. `const app = express();` : Initialise une nouvelle application Express.
3. `app.use(express.json());` : Analyse le corps JSON des requêtes API entrantes.
4. `app.use(cors());` : Ajoute la prise en charge de CORS.
5. `app.listen(5000, ...)` : Cela démarre le serveur en écoute sur le port 5000.

### Test

Enfin, vous pouvez tester le serveur en naviguant vers le répertoire `notes-app-server` dans votre terminal et en exécutant :

```bash
npm start

```

Vous devriez voir le journal de la console : `server running on localhost:5000`. Pour tester davantage, vous pouvez utiliser une commande curl pour atteindre le point de terminaison `/api/notes`. Si tout est configuré correctement, vous obtiendrez un objet JSON en retour.

### Créer une base de données Postgres

ElephantSQL est un service d'hébergement de base de données PostgreSQL qui facilite la configuration, la maintenance et la mise à l'échelle de votre base de données PostgreSQL. Voici comment commencer à créer une base de données en utilisant ElephantSQL.

#### Étape 1 : Inscription / Connexion

1. Naviguez vers le [site web d'ElephantSQL](https://www.elephantsql.com/).
2. Si vous n'avez pas de compte, vous pouvez vous inscrire gratuitement. Si vous en avez déjà un, connectez-vous.

#### Étape 2 : Créer une nouvelle instance

1. Une fois connecté, vous vous trouverez sur la page "Tableau de bord".
2. Cliquez sur le bouton "Créer une nouvelle instance".
3. Vous serez redirigé vers une page où vous pourrez définir les détails de votre nouvelle instance de base de données PostgreSQL.

#### Étape 3 : Choisir un plan

1. Vous pouvez commencer avec un plan gratuit "Tiny Turtle", qui est parfait pour les petits projets et les tests.
2. Sélectionnez le plan qui correspond le mieux à vos besoins et cliquez sur "Sélectionner".

#### Étape 4 : Configurer votre instance

1. Vous serez invité à nommer votre instance. Choisissez un nom que vous retiendrez et qui décrit le but de la base de données.
2. Vous pouvez également sélectionner le centre de données qui est géographiquement le plus proche de vous ou de vos utilisateurs pour de meilleures performances.
3. Cliquez sur "Revoir" puis sur "Créer une instance" pour finaliser la création.

#### Étape 5 : Accéder à votre base de données

1. Une fois l'instance créée, cliquez dessus dans le tableau de bord.
2. Ici, vous verrez l'onglet "Détails" qui inclut toutes les informations dont vous avez besoin pour vous connecter à votre base de données : `URL`, `Utilisateur et base de données par défaut`, `Mot de passe`, et plus encore.

### Remplir la base de données

#### Étape 1 : Connexion à ElephantSQL

Ouvrez votre navigateur web et accédez au site web d'ElephantSQL. Connectez-vous à votre compte.

#### Étape 2 : Ouvrir votre instance

Une fois connecté, cliquez sur le nom de l'instance de base de données que vous avez configurée.

#### Étape 3 : Accéder au navigateur SQL

Dans la barre latérale de gauche, trouvez et cliquez sur "Navigateur SQL" ou quelque chose de similaire (il peut dire "Navigateur").

#### Étape 4 : Exécuter une requête SQL

Dans l'éditeur de requêtes SQL qui apparaît, vous pouvez taper ou coller votre commande SQL :

```sql
INSERT INTO "public"."Note" (title, content)
VALUES ('test title', 'test content bla bla');

```

Après avoir saisi le SQL, cliquez sur le bouton "Exécuter" ou "Lancer".

Cela devrait insérer une nouvelle ligne dans votre table `Note` avec le titre 'test title' et le contenu 'test content bla bla'.

#### Optionnel : Vérifier l'insertion

Vous pouvez également vérifier si les données ont été insérées correctement. Pour cela, vous pourriez utiliser :

```sql
SELECT * FROM "public"."Note";

```

Exécutez cette requête SQL dans le même navigateur SQL, et elle devrait retourner toutes les lignes de la table `Note`, y compris celle que vous venez d'insérer.

Et c'est tout ! Vous avez inséré une nouvelle ligne dans votre table via la console web d'ElephantSQL.

### Se connecter à la base de données depuis le backend Node.js en utilisant Prisma

#### Étape 1 : Copier l'URL de connexion d'ElephantSQL

Une fois que vous avez configuré votre base de données ElephantSQL, assurez-vous de copier l'URL de connexion qui apparaît sur votre tableau de bord. Cette URL inclut votre nom d'utilisateur et votre mot de passe pour la base de données, alors gardez-la sécurisée.

#### Étape 2 : Créer un fichier `.env`

Naviguez vers votre répertoire `notes-app-server` et créez un nouveau fichier `.env` :

```bash
touch .env

```

Ouvrez ce fichier et ajoutez la ligne suivante pour spécifier l'URL de connexion à la base de données :

```bash
DATABASE_URL="votre_url_de_connexion_ici"

```

Assurez-vous de ne pas commiter ce fichier `.env` dans votre dépôt Git pour garder vos identifiants sécurisés.

#### Étape 3 : Initialiser Prisma

Si vous n'avez pas encore installé Prisma, installez-le d'abord :

```bash
npm install prisma --save-dev

```

Maintenant, initialisez Prisma dans le répertoire `notes-app-server` :

```bash
npx prisma init

```

Cette commande créera un nouveau dossier `prisma` contenant un fichier `schema.prisma`.

#### Étape 4 : Configurer `schema.prisma`

Ouvrez `schema.prisma` dans votre éditeur de texte. Vous verrez que Prisma a déjà généré certaines configurations pour vous. Mettez à jour le bloc `datasource` pour utiliser la variable d'environnement :

```javascript
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

```

#### Étape 5 : Créer le modèle Note

Sous le bloc `datasource`, ajoutez un nouveau bloc `model` pour représenter une `Note` :

```javascript
model Note {
  id      Int     @id @default(autoincrement())
  title   String
  content String
}

```

#### Étape 6 : Générer le client Prisma et la table de la base de données

Exécutez la commande suivante pour générer votre client Prisma et créer les tables de la base de données :

```bash
npx prisma db push

```

#### Étape 7 : Ajouter Prisma à votre application

Tout d'abord, importez Prisma en haut de votre fichier `index.ts` :

```typescript
import { PrismaClient } from "@prisma/client";

```

Ensuite, initialisez le client Prisma :

```typescript
const prisma = new PrismaClient();

```

#### Étape 8 : Interroger votre base de données

Maintenant, vous pouvez utiliser Prisma dans votre application pour interroger la base de données. Par exemple, dans un point de terminaison GET :

```typescript
app.get("/notes", async (req, res) => {
  const notes = await prisma.note.findMany();
  res.json(notes);
});

```

### Optionnel : Installer Thunder Client dans VS Code

(Vous pouvez sauter cette étape si vous avez déjà un client API préféré)

L'utilisation de `curl` est utile pour tester rapidement les API, mais cela devient fastidieux lorsque vous devez construire des requêtes plus complexes. Par exemple, gérer les requêtes POST avec des corps et des en-têtes personnalisés peut être plus compliqué. 

Pour simplifier les requêtes API, nous allons installer un client conçu à cet effet.

Bien qu'il existe plusieurs options comme Postman, nous allons nous concentrer sur l'installation de Thunder Client dans VS Code, ce qui facilite l'exécution des requêtes directement depuis votre IDE.

Pour installer Thunder Client, accédez à la section Extensions dans VS Code et tapez "Thunder Client" dans la barre de recherche. Vous le trouverez dans la liste des extensions disponibles, identifiable par son logo violet. Cliquez sur "Installer", et une fois l'installation terminée, vous verrez une option Thunder Client apparaître dans la barre des tâches de gauche de votre IDE.

Une fois que vous avez cliqué sur Thunder Client, une liste de vos requêtes passées s'affichera. Pour initier une nouvelle requête, cliquez sur le bouton "Nouvelle requête" en haut. Cette action ouvre un nouvel onglet dans Visual Studio Code.

Avant de continuer, assurez-vous que votre serveur est en cours d'exécution. Ouvrez le terminal et vérifiez cela. Nous allons utiliser Thunder Client pour tester notre point de terminaison GET et nous familiariser avec le processus de création de requêtes. Dans la barre d'URL, entrez l'adresse de votre point de terminaison 'notes' et spécifiez qu'il s'agit d'une requête GET.

Cliquez sur "Envoyer", et vous verrez une petite fenêtre affichant la réponse. Si le code d'état est 200 et que vous voyez un tableau contenant votre note, vous avez réussi à faire une requête GET. Thunder Client sera notre outil de choix pour tester les requêtes de création, de mise à jour et de suppression ultérieures. Bien sûr, n'hésitez pas à utiliser tout autre outil avec lequel vous êtes à l'aise pour ce faire.

### Créer un point de terminaison POST

Dans cette section, nous allons ajouter un point de terminaison à notre application Express qui nous permet de créer une nouvelle note. Localisez le fichier `index.ts` et insérez le code suivant sous votre point de terminaison GET existant :

```typescript
app.post("/api/notes", async (req, res) => {
  const { title, content } = req.body;

  if (!title || !content) {
    return res.status(400).send("Les champs titre et contenu sont requis");
  }

  try {
    const note = await prisma.note.create({
      data: { title, content },
    });
    res.json(note);
  } catch (error) {
    res.status(500).send("Oups, quelque chose s'est mal passé");
  }
});

```

La structure est similaire au point de terminaison GET, mais nous utilisons `app.post` cette fois. Nous spécifions l'URL pour ce point de terminaison POST puis définissons notre fonction.

À l'intérieur de la fonction, la première tâche consiste à extraire `title` et `content` de `req.body`. C'est ce que l'UI enverra lorsqu'un utilisateur soumet le formulaire "Ajouter une note".

Après avoir obtenu `title` et `content`, nous utilisons le client Prisma que nous avons configuré précédemment pour créer une nouvelle note. Nous passons `title` et `content` à la méthode `prisma.note.create()`, qui retourne un nouvel objet de note complet avec un ID. Cet objet est ensuite envoyé en réponse JSON.

Pour tester le point de terminaison, allez dans l'onglet Thunder Client dans VS Code. Changez la méthode HTTP de GET à POST tout en gardant la même URL. Cliquez sur l'onglet "Body", qui devrait être par défaut en JSON, et entrez quelques valeurs de test pour `title` et `content`. Après avoir cliqué sur "Send", vous devriez recevoir un statut 200 OK ainsi que la note créée, contenant un ID, un titre et un contenu.

Pour plus de robustesse, nous avons ajouté une validation et une gestion des erreurs. Si `title` ou `content` est manquant, le serveur retourne un statut 400 Bad Request avec un message d'erreur approprié. Pour tester cela, supprimez soit `title` soit `content` du corps de la requête et renvoyez-la. Vous devriez maintenant voir un code de statut 400 ainsi que votre message d'erreur.

De plus, nous utilisons un bloc try-catch pour gérer les erreurs lancées par le client Prisma. Cela aide en cas de problèmes de connexion à la base de données ou d'autres erreurs imprévues, empêchant le backend de planter.

Enfin, vous pouvez tester à nouveau le point de terminaison GET. Il devrait maintenant retourner deux notes : la première ajoutée manuellement à la base de données, et la deuxième créée via Thunder Client. Changez la méthode en GET dans Thunder Client et cliquez sur "Send" ; vous devriez voir deux notes dans la réponse.

### Créer un point de terminaison PUT

Dans ce segment du tutoriel, nous allons nous concentrer sur l'ajout de la capacité à mettre à jour une note. Ajoutez le code suivant sous le code de votre point de terminaison POST précédent :

```javascript
app.put("/api/notes/:id", async (req, res) => {
  const { title, content } = req.body;
  const id = parseInt(req.params.id);

  if (!title || !content) {
    return res.status(400).send("Les champs titre et contenu sont requis");
  }

  if (!id || isNaN(id)) {
    return res.status(400).send("L'ID doit être un nombre valide");
  }

  try {
    const updatedNote = await prisma.note.update({
      where: { id },
      data: { title, content },
    });
    res.json(updatedNote);
  } catch (error) {
    res.status(500).send("Oups, quelque chose s'est mal passé");
  }
});

```

La structure de cette fonction `app.put` est similaire aux points de terminaison GET et POST que vous avez déjà créés. La principale différence est le paramètre `:id` dans l'URL. Cela agit comme un espace réservé, vous permettant de spécifier l'ID de la note que vous souhaitez mettre à jour.

À l'intérieur de la fonction, vous remarquerez que nous extrayons `title` et `content` de `req.body`, comme avant. De plus, nous récupérons l'ID de `req.params` et le convertissons en entier en utilisant `parseInt()`, car notre base de données stocke les ID en tant qu'entiers.

Nous avons ajouté des vérifications de validation pour nous assurer que l'`id` existe et est un nombre valide. Si l'`id`, le `title` ou le `content` est manquant ou invalide, l'API retourne un code de statut 400 ainsi qu'un message d'erreur.

Ensuite, nous utilisons un bloc try-catch pour tenter l'opération de mise à jour. Dans la section `try`, nous appelons la fonction `prisma.note.update()`. Nous spécifions l'`id` dans un objet `where` et fournissons le nouveau `title` et `content` via un objet `data`. Si l'opération réussit, la note mise à jour est renvoyée dans la réponse. En cas d'erreur, le bloc `catch` retournera un statut 500 et un message d'erreur.

Pour tester cela, basculez vers votre onglet Thunder Client dans VS Code. Mettez à jour la méthode en PUT et définissez l'URL pour inclure l'ID de la note que vous souhaitez mettre à jour, par exemple, `/api/notes/3`. Dans le corps de la requête, envoyez des données JSON avec le nouveau `title` et `content`. Après avoir cliqué sur "Envoyer", un statut 200 devrait confirmer la mise à jour. La note renvoyée devrait refléter vos modifications.

Pour double-vérifier, effectuez une requête GET sur le point de terminaison `/api/notes`. Vous devriez voir la note mise à jour dans la liste.

Enfin, testez la validation en fournissant un ID invalide, comme une chaîne aléatoire. L'API devrait retourner un message d'erreur indiquant que l'ID doit être un nombre valide.

### Créer un point de terminaison DELETE

En plus de nos points de terminaison existants, il est crucial d'ajouter une validation pour les champs `title` ou `content` vides dans notre fonction `app.put`, puisque ces champs sont requis par notre base de données. Revisitez votre fonction `app.put` dans `index.ts` et ajoutez une validation similaire à celle que nous avons ajoutée pour la requête POST. Plus précisément, si `title` ou `content` est vide, retournez un code de statut 400 avec un message d'erreur.

Avec cela en place, passons au point de terminaison DELETE. Ajoutez le code suivant juste après votre point de terminaison PUT :

```javascript
app.delete("/api/notes/:id", async (req, res) => {
  const id = parseInt(req.params.id);

  if (!id || isNaN(id)) {
    return res.status(400).send("Le champ ID est requis");
  }

  try {
    await prisma.note.delete({
      where: { id },
    });
    res.status(204).send();
  } catch (error) {
    res.status(500).send("Oups, quelque chose s'est mal passé");
  }
});

```

Cette fonction `app.delete` fonctionne de manière similaire au point de terminaison de mise à jour (`app.put`). Elle accepte également un ID dans le cadre des paramètres d'URL (`query params` devrait être `URL parameters` ou `route parameters`).

Tout d'abord, nous validons que l'ID fourni est un nombre valide. Si ce n'est pas le cas, nous retournons un code de statut 400 et un message d'erreur correspondant.

Une fois l'ID validé, nous procédons à la suppression de la note en utilisant la méthode `delete` de Prisma. Dans le bloc `try`, nous spécifions quelle note supprimer par son ID dans l'objet `where`. Après une suppression réussie, nous retournons un code de statut 204, qui indique 'No Content'. C'est une manière standard de signaler au frontend ou aux consommateurs d'API que la suppression a réussi.

Si une erreur se produit lors de la suppression, le bloc `catch` retourne un code de statut 500 avec un message d'erreur générique.

Pour tester le nouveau point de terminaison DELETE, changez votre méthode HTTP en `DELETE` dans votre outil de test (comme Thunder Client ou Postman). Utilisez l'ID de la note que vous souhaitez supprimer, comme `/api/notes/3`, et cliquez sur 'Envoyer'. Vous devriez recevoir un code de statut 204, indiquant que l'opération a réussi. Pour confirmer, effectuez une requête GET sur votre point de terminaison `/api/notes` et observez que la note avec l'ID spécifié a bien été supprimée.

## PARTIE 3 - Connecter l'UI au Backend 

Maintenant que nous avons notre backend et notre UI prêts, il est temps de les connecter. Nous allons le faire en utilisant la fonction intégrée `fetch` pour appeler notre backend depuis notre UI.

### Obtenir et afficher les notes

Plongeons-nous dans notre code frontend. Juste en dessous de nos déclarations d'état en haut de notre composant, nous allons introduire un hook `useEffect` :

```jsx
useEffect(() => {
  // ...
}, []);

```

À l'intérieur de ce `useEffect`, nous allons définir une fonction asynchrone nommée `fetchNotes`. Nous devons mettre cela dans une fonction séparée car React ne supporte pas de rendre le hook `useEffect` asynchrone directement :

```jsx
const fetchNotes = async () => {
  // ...
};

```

Pour gérer les erreurs potentielles de l'API, nous allons envelopper notre logique d'API à l'intérieur d'un bloc `try-catch` :

```jsx
try {
  // ...
} catch (e) {
  console.log(e);
}

```

À l'intérieur du bloc `try`, nous utilisons la fonction native `fetch` pour faire un appel API. Notre API fonctionne à `http://localhost:5000/api/notes`. Par défaut, `fetch` effectue une requête GET, ce qui est ce dont nous avons besoin :

```jsx
const response = await fetch("http://localhost:5000/api/notes");

```

Après avoir fait la requête, nous allons traiter la réponse et la convertir en JSON. L'API retourne un tableau de notes, que nous allons capturer dans une variable nommée `notes` de type `Note[]` :

```jsx
const notes: Note[] = await response.json();

```

Si tout se passe bien, l'étape suivante consiste à mettre à jour notre état avec les notes récupérées de l'API :

```jsx
setNotes(notes);

```

Dans le bloc `catch`, nous allons enregistrer les erreurs qui peuvent survenir :

```jsx
console.log(e);

```

Nous avons défini `fetchNotes`, mais nous ne l'avons pas encore appelé. Pour invoquer cette fonction, ajoutez un appel à `fetchNotes()` à la fin du bloc `useEffect` :

```jsx
fetchNotes();

```

Enfin, ajoutez un tableau de dépendances vide pour vous assurer que ce code ne s'exécute qu'une seule fois lorsque le composant est monté pour la première fois :

```jsx
}, []);

```

Après avoir enregistré vos modifications, vous devriez voir les notes de votre base de données affichées dans le navigateur. Si vous avez ajouté ou supprimé des notes directement via la base de données, ces modifications devraient être reflétées ici.

Pour conclure, vous pouvez supprimer tout tableau codé en dur que vous avez initialement ajouté à votre variable d'état `notes`. Au lieu de cela, remplissez-le avec les données récupérées de l'API :

```jsx
const [notes, setNotes] = useState<Note[]>([]);

```

Cela garantit que l'état `notes` est initialement vide, puis rempli par le `useEffect` via la fonction `fetchNotes`.

### Code complété pour cette section

```jsx
  const [notes, setNotes] = useState<Note[]>([]);


  useEffect(() => {
    const fetchNotes = async () => {
      try {
        const response = await fetch(
          "http://localhost:5000/api/notes"
        );

        const notes: Note[] =
          await response.json();

        setNotes(notes);
      } catch (e) {
        console.log(e);
      }
    };

    fetchNotes();
  }, []);

```

### Enregistrer une nouvelle note

Ensuite, explorons comment enregistrer une note dans notre backend. Nous avons déjà une fonction appelée `handleAddNote` qui gère l'ajout d'une note à l'UI :

```jsx
const handleAddNote = async (
  event: React.FormEvent
) => {
  // ...
};

```

Pour commencer, supprimez tout code qui crée manuellement un nouvel objet de note sur le frontend. Cela est dû au fait que notre backend retournera cet objet avec toutes ses propriétés une fois que la note aura été enregistrée dans la base de données.

Comme dans notre exemple précédent, nous allons utiliser un bloc `try-catch` pour gérer la logique de l'API et la gestion des erreurs :

```jsx
try {
  // API logic here
} catch (e) {
  console.log(e);
}

```

Placez vos appels de fonction existants de changement d'état (`setNotes`, `setTitle`, et `setContent`) à l'intérieur du bloc `try`. Ceux-ci seront exécutés après que l'API ait enregistré la note avec succès :

```jsx
setNotes([newNote, ...notes]);
setTitle("");
setContent("");

```

Pour appeler l'API, nous allons utiliser la fonction `fetch`, similaire à la manière dont nous avons récupéré les notes. La différence est que cette fois, nous devons passer un deuxième argument à `fetch` pour spécifier la méthode HTTP et la charge utile :

```jsx
const response = await fetch(
  "http://localhost:5000/api/notes",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title,
      content,
    }),
  }
);

```

N'oubliez pas d'ajouter le mot-clé `async` à la signature de la fonction `handleAddNote` si vous ne l'avez pas déjà fait, car nous utilisons le mot-clé `await` à l'intérieur de la fonction.

Le serveur répondra avec le nouvel objet de note créé, que nous pouvons ensuite ajouter à notre UI. Convertissez la réponse en JSON et stockez-la dans une variable nommée `newNote` :

```jsx
const newNote = await response.json();

```

Enfin, dans le bloc `catch`, nous enregistrons les erreurs qui pourraient survenir :

```jsx
console.log(e);

```

Assurez-vous également d'ajouter des en-têtes pour spécifier le type de contenu des données que nous envoyons :

```jsx
headers: {
  "Content-Type": "application/json",
}

```

Enregistrez vos modifications et testez la fonctionnalité dans le navigateur. Utilisez le formulaire pour ajouter une nouvelle note et cliquez sur "Ajouter une note". Si tout est configuré correctement, votre nouvelle note devrait apparaître dans la liste.

### Code complété pour cette section

```jsx
  const handleAddNote = async (
    event: React.FormEvent
  ) => {
    event.preventDefault();
    try {
      const response = await fetch(
        "http://localhost:5000/api/notes",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            title,
            content,
          }),
        }
      );

      const newNote = await response.json();

      setNotes([newNote, ...notes]);
      setTitle("");
      setContent("");
    } catch (e) {
      console.log(e);
    }
  };



```

### Enregistrer une note mise à jour

Ensuite, explorons comment enregistrer une note dans notre backend. Nous avons déjà une fonction appelée `handleAddNote` qui gère l'ajout d'une note à l'UI :

```jsx
const handleAddNote = async (
  event: React.FormEvent
) => {
  // ...
};

```

Pour commencer, supprimez tout code qui crée manuellement un nouvel objet de note sur le frontend. Cela est dû au fait que notre backend retournera cet objet avec toutes ses propriétés une fois que la note aura été enregistrée dans la base de données.

Comme dans notre exemple précédent, nous allons utiliser un bloc `try-catch` pour gérer la logique de l'API et la gestion des erreurs :

```jsx
try {
  // API logic here
} catch (e) {
  console.log(e);
}

```

Placez vos appels de fonction existants de changement d'état (`setNotes`, `setTitle`, et `setContent`) à l'intérieur du bloc `try`. Ceux-ci seront exécutés après que l'API ait enregistré la note avec succès :

```jsx
setNotes([newNote, ...notes]);
setTitle("");
setContent("");

```

Pour appeler l'API, nous allons utiliser la fonction `fetch`, similaire à la manière dont nous avons récupéré les notes. La différence est que cette fois, nous devons passer un deuxième argument à `fetch` pour spécifier la méthode HTTP et la charge utile :

```jsx
const response = await fetch(
  "http://localhost:5000/api/notes",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title,
      content,
    }),
  }
);

```

N'oubliez pas d'ajouter le mot-clé `async` à la signature de la fonction `handleAddNote` si vous ne l'avez pas déjà fait, car nous utilisons le mot-clé `await` à l'intérieur de la fonction.

Le serveur répondra avec le nouvel objet de note créé, que nous pouvons ensuite ajouter à notre UI. Convertissez la réponse en JSON et stockez-la dans une variable nommée `newNote` :

```jsx
const newNote = await response.json();

```

Enfin, dans le bloc `catch`, nous enregistrons les erreurs qui pourraient survenir :

```jsx
console.log(e);

```

Assurez-vous également d'ajouter des en-têtes pour spécifier le type de contenu des données que nous envoyons :

```jsx
headers: {
  "Content-Type": "application/json",
}

```

Enregistrez vos modifications et testez la fonctionnalité dans le navigateur. Utilisez le formulaire pour ajouter une nouvelle note et cliquez sur "Ajouter une note". Si tout est configuré correctement, votre nouvelle note devrait apparaître dans la liste.

### Code complété pour cette section

```jsx
  const handleAddNote = async (
    event: React.FormEvent
  ) => {
    event.preventDefault();
    try {
      const response = await fetch(
        "http://localhost:5000/api/notes",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            title,
            content,
          }),
        }
      );

      const newNote = await response.json();

      setNotes([newNote, ...notes]);
      setTitle("");
      setContent("");
    } catch (e) {
      console.log(e);
    }
  };



```

### Supprimer une note

Dans cette section, nous allons discuter de la suppression d'une note en invoquant un point de terminaison API. Nous allons nous concentrer sur la fonction `deleteNote` pour cette fonctionnalité :

```jsx
const deleteNote = async (
  event: React.MouseEvent,
  noteId: number
) => {
  // ...
};

```

Tout d'abord, nous devons rendre notre fonction asynchrone pour gérer les appels API. Ajoutez donc le mot-clé `async` à la déclaration de la fonction comme ceci :

```jsx
const deleteNote = async (
  event: React.MouseEvent,
  noteId: number
) => {
  // ...
};

```

Ensuite, ajoutons un bloc `try-catch` pour gérer l'appel API. Le bloc `catch` est essentiel pour enregistrer les erreurs, ce qui empêche l'application de planter de manière inattendue :

```jsx
try {
  // API logic here
} catch (e) {
  console.log(e);
}

```

Copiez la logique de mise à jour de l'UI existante et collez-la dans le bloc `try`, juste après l'appel API. Cela garantit que l'UI ne se met à jour que si l'appel API est réussi.

Passons maintenant à la partie principale—faire l'appel API pour supprimer la note. Pour ce faire, nous allons utiliser l'API `fetch` :

```jsx
await fetch(
  `http://localhost:5000/api/notes/${noteId}`,
  {
    method: "DELETE",
  }
);

```

Notez que l'URL est une chaîne de modèle. Elle nous permet d'injecter l'ID de la note (`noteId`) que nous voulons supprimer. Cet `noteId` est passé dans notre fonction `deleteNote` lorsque l'utilisateur clique sur le bouton de suppression correspondant à une note spécifique.

Nous spécifions la méthode HTTP comme "DELETE" pour indiquer que nous demandons la suppression d'une note :

```jsx
method: "DELETE",

```

Contrairement aux opérations 'add' ou 'update', il n'est pas nécessaire d'assigner la réponse de l'API à une variable, car nous ne nous attendons pas à ce que des données soient retournées :

```jsx
await fetch(
  `http://localhost:5000/api/notes/${noteId}`,
  {
    method: "DELETE",
  }
);

```

Après avoir supprimé la note avec succès, nous filtrons la note supprimée de notre état local des notes :

```jsx
const updatedNotes = notes.filter(
  (note) => note.id !== noteId
);
setNotes(updatedNotes);

```

Enfin, si tout se passe bien et que vous enregistrez vos modifications, essayez d'exécuter l'application dans le navigateur. Cliquez sur le bouton de suppression pour une note spécifique, puis rafraîchissez la page. Vous verrez que la note a été supprimée avec succès.

### Code complété pour cette section

```jsx
  const deleteNote = async (
    event: React.MouseEvent,
    noteId: number
  ) => {
    event.stopPropagation();

    try {
      await fetch(
        `http://localhost:5000/api/notes/${noteId}`,
        {
          method: "DELETE",
        }
      );
      const updatedNotes = notes.filter(
        (note) => note.id !== noteId
      );

      setNotes(updatedNotes);
    } catch (e) {
      console.log(e);
    }
  };


```



## La Fin - Pourquoi ne pas essayer les défis bonus ?

Félicitations pour être arrivé à la fin ! Si vous avez aimé ce projet, j'ai créé [une liste de défis supplémentaires à essayer sur codecoyotes.com](https://www.codecoyotes.com/projects/react-node-notes-app). 

Si vous avez des questions ou des suggestions, n'hésitez pas à [me laisser un message ici.](https://www.codecoyotes.com/contact) À la prochaine !