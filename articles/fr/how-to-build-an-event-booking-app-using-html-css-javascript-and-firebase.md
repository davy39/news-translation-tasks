---
title: Comment créer une application de réservation d'événements avec HTML, CSS, JavaScript
  et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-03T11:21:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-event-booking-app-using-html-css-javascript-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover-2.png
tags:
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
seo_title: Comment créer une application de réservation d'événements avec HTML, CSS,
  JavaScript et Firebase
seo_desc: 'By Ibrahima Ndaw

  In this tutorial, we are going to build an Event Booking App with HTML, CSS, JavaScript,
  and Firebase.


  Plan our app

  Markup

  Styling

  Interact With Firebase

  Fetch events

  Create an event

  Book an event

  Show and Update Data with JavaScrip...'
---

Par Ibrahima Ndaw

Dans ce tutoriel, nous allons créer une application de réservation d'événements avec HTML, CSS, JavaScript et Firebase.

* [Planifier notre application](#heading-planifier-notre-application)
* [Balisage](#heading-balisage)
* [Stylisation](#heading-stylisation)
* [Interagir avec Firebase](#heading-interagir-avec-firebase)
* [Récupérer les événements](#heading-recuperer-les-evenements)
* [Créer un événement](#heading-creer-un-evenement)
* [Réserver un événement](#heading-reserver-un-evenement)
* [Afficher et mettre à jour les données avec JavaScript](#heading-afficher-et-mettre-a-jour-les-donnees-avec-javascript)

## Planifier notre application

Nous n'allons pas créer une application complète de réservation d'événements avec toutes les fonctionnalités. Nous n'avons pas besoin de tout couvrir en un seul tutoriel. Comme je veux garder les choses simples et faciles à comprendre, nous aborderons la partie authentification dans un article séparé.

Ainsi, notre application de réservation d'événements aura les fonctionnalités suivantes :

* L'utilisateur peut créer un événement et le stocker dans Firestore.
* L'utilisateur peut récupérer tous les événements en temps réel.
* L'utilisateur peut réserver un événement.
* L'utilisateur ne peut pas réserver un événement plus d'une fois.

Maintenant que nous savons à quoi ressemblera notre application, commençons à la construire dans la section suivante.

## Balisage

Notre fichier HTML sera relativement simple. Nous placerons notre barre de navigation et le dernier événement dans la balise `header`.

* Dans `index.html`

```html
<body>
    <header id="home">
      <nav class="navbar">
        <h1>Eventic</h1>
        <ul>
            <li><a href="#home">Accueil</a></li>
            <li><a href="#events">Événements</a></li>
            <li><a href="#add-event">Nouvel Événement</a></li>
        </ul>
      </nav>
      <div class="welcome-event"></div>
    </header>
    <main>
        <section id="events">
            <h1 class="section-title">Événements</h1>
            <div class="events-container"></div>
        </section>
        <section id="add-event">
            <h1 class="section-title">Nouvel Événement</h1>
            <form class="form">
                <input type="text" id="name" placeholder="Nom">
                <input type="number" id="attendee" placeholder="Participants">
                <textarea id="description" cols="30" rows="10" placeholder="Description..."></textarea>
                <select id="status">
                    <option value="0">Gratuit</option>
                    <option value="1">Payant</option>
                </select>
                <button class="btn btn-primary">Enregistrer</button>
            </form>
        </section>
    </main>

```

Ensuite, la balise `main` enveloppera la liste des événements et le formulaire qui nous permet de créer un nouvel événement.

Les événements seront affichés plus tard avec l'aide de JavaScript.

* Dans `index.html`

```html
<script src="https://www.gstatic.com/firebasejs/7.9.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/7.9.1/firebase-firestore.js"></script>

<script>
  // Configuration Firebase de votre application web
  var firebaseConfig = {
    apiKey: "xxxxxxxxxxxxxxxxxxxxxxxxx",
    authDomain: "xxxxxxxxxxxxxxxxxxxxxxxx",
    databaseURL: "xxxxxxxxxxxxxxxxxxxxxxxxx",
    projectId: "xxxxxxxxxxxxxxxxxxxxxxxxx",
    storageBucket: "xxxxxxxxxxxxxxxxxxxxxxxxx",
    messagingSenderId: "xxxxxxxxxxxxxxxxxxxxxxxxx",
    appId: "xxxxxxxxxxxxxxxxxxxxxxxxx"
  };
  // Initialiser Firebase
  firebase.initializeApp(firebaseConfig);
  const db = firebase.firestore()
</script>

<script src="db.js"></script>
<script src="app.js"></script>

</body>
</html>

```

Ensuite, nous devons connecter notre application à [Firebase](https://firebase.google.com/) pour pouvoir stocker nos données.

Pour obtenir ces informations d'identification, vous devrez créer une nouvelle application dans la [Console Firebase](https://console.firebase.google.com/). Une fois le projet créé, cliquez sur l'icône de code `</>` qui se trouve à côté des icônes iOS et Android pour enregistrer votre application.

Maintenant, pour générer les informations d'identification, vous devez enregistrer le nom de votre application. 
Et enfin, placez les informations d'identification dans le fichier HTML comme je le fais ici.

Ensuite, dupliquez la première balise `script` et changez `firebase-app.js` en `firebase-firestore.js` car nous utiliserons Firestore dans ce projet.

Ensuite, initialisez `firebase` avec la configuration et déclarez une variable `db` qui sera utilisée plus tard pour interagir avec Firebase.

Maintenant, nous avons notre balisage et avons réussi à lier notre projet à Firebase. Alors commençons à le styliser dans la section suivante.

## Stylisation

Le fichier CSS est un peu long, donc je ne couvrirai pas tout dans cet article. Je vais juste mettre en évidence les parties les plus importantes. Cependant, ne vous inquiétez pas, vous trouverez le code source à la fin de l'article.

Comme d'habitude, nous commençons par importer notre police et faire quelques réinitialisations pour prévenir le comportement par défaut.

* Dans `style.css`

```css
@import url('https://fonts.googleapis.com/css?family=Nunito:400,700&display=swap');

*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
    --primary-color:#e74c3c;
    --secondary-color:#222;
    --tertiary-color:#333;
    --light-color: #fff;
    scroll-behavior: smooth; 
}

body {
    background-color: #1f1f1f;
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    color: var(--light-color);
    line-height: 1.6;
}

```

Ensuite, nous utilisons des variables CSS pour stocker nos couleurs et définir le `scroll-behavior` à `smooth` pour avoir un bel effet de défilement lorsque l'utilisateur clique sur les liens de la barre de navigation.

Cependant, soyez prudent avec le `scroll-behavior`, car il n'est pas [supporté par tous les navigateurs](https://caniuse.com/#search=scroll-behavior). Vous pouvez vérifier la compatibilité des navigateurs [ici](https://caniuse.com/).

* Dans `style.css`

```css
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 2.5rem;
    z-index: 100;
    width: 100%;
    transition: background 0.3s;
    position: fixed;
    top: 0;
    left: 0;
}

nav ul {
    display: flex;
    list-style: none;
}

nav li:not(:last-child), .welcome-event div span {
    margin-right: 1.5rem;
}

```

Pour la barre de navigation, par défaut, l'arrière-plan sera transparent. Pour une meilleure utilité, il changera lorsque l'utilisateur commencera à faire défiler.

Notre application de réservation d'événements commence à prendre forme. Maintenant, commençons à implémenter Firebase et à connecter notre application à Firestore.

![excellent](https://media.giphy.com/media/vMnuZGHJfFSTe/source.gif)

## Interagir avec Firebase

[Firebase](https://firebase.google.com/?gclid=EAIaIQobChMIjIichor85wIVWOJ3Ch1o_AlDEAAYASAAEgKmL_D_BwE) est une plateforme qui gère tout ce qui est lié au back-end pour nous. La seule chose que nous devons faire est de connecter notre application à celle-ci et de commencer à utiliser la base de données ou d'autres services.

[Firestore](https://firebase.google.com/docs/firestore) est une base de données NoSQL, elle est non relationnelle et utilise des documents, des collections, etc. pour créer la base de données.

Maintenant, connectons-nous à Firestore et créons notre toute première base de données.

### Récupérer les événements

Plus tôt dans ce tutoriel, nous avions déclaré une variable `db` dans la partie HTML. Maintenant, utilisons cette variable pour connecter notre application à Firestore.

Je vais mettre tout ce qui est lié à la base de données dans le fichier `db.js` pour avoir une structure plus propre.

* Dans `db.js`

```javascript
db.collection('events').onSnapshot(snapshot => {
    // Gérer le dernier événement
    const newestEvent = snapshot.docChanges()[0].doc.data()
    const id = snapshot.docChanges()[0].doc.id
    showLatestEvent(newestEvent, id);
    
    // supprimer l'élément du dernier événement
    snapshot.docChanges().shift()
    
    snapshot.docChanges().forEach(event => {
        showEvents(event.doc.data(), event.doc.id)
    });
})

```

Avec l'aide de `db`, nous pouvons maintenant accéder à notre collection `events`. Ce n'est que le nom de notre base de données, et si elle n'existe pas, Firestore la créera à la volée pour nous.

L'objet collection a une méthode très pratique appelée `onSnapshot()`. Elle nous aide à écouter en temps réel la base de données. Cela signifie que chaque fois qu'un changement se produit, elle réagira et retournera le changement en temps réel.

![magic](https://media.giphy.com/media/5p2wQFyu8GsFO/source.gif)

La méthode `onSnapshot()` nous aidera également à accéder au document (nos données). Et maintenant, nous pouvons extraire le dernier événement à afficher dans l'en-tête. Et, avant de parcourir le tableau des événements, supprimez le dernier événement pour qu'il ne l'affiche pas à nouveau.

Maintenant, pour afficher les événements sur l'interface utilisateur, nous devons appeler nos fonctions nécessaires `showLatestEvent()` et `showEvents()`. Ensuite, nous leur passons l'événement et l'id en tant que paramètres.

Nous pouvons maintenant récupérer les événements de Firestore, mais nous n'avons toujours aucun événement à afficher. Stockons notre tout premier événement dans notre base de données.

### Créer un événement

Pour obtenir les valeurs saisies par l'utilisateur, nous devons d'abord sélectionner la balise `form` et l'utiliser pour sélectionner l'id de chaque input et récupérer la valeur saisie.

* Dans `db.js`

```javascript
const addNewEvent = () => {
  const event = {
    name: form.name.value,
    attendee: form.attendee.value,
    booked: 0,
    description: form.description.value,
    status: parseInt(form.status.value, 10)
  }
    db.collection('events').add(event)
    .then(() => {
    // Réinitialiser les valeurs du formulaire
    form.name.value = "",
    form.attendee.value = "",
    form.description.value = "",
    form.status.value = ""

    alert('Votre événement a été enregistré avec succès')
    })
    .catch(err => console.log(err))
}

```

La variable `db` (rappelons qu'elle est la référence à `firebase.firestore()`) a une autre méthode pour sauvegarder les données dans Firestore : la fonction `save()`. C'est une promesse, et une fois qu'elle est complète, nous pouvons maintenant réinitialiser les valeurs du formulaire et afficher un message de succès à l'utilisateur.

Maintenant, passons à la gestion du cas où l'utilisateur souhaite réserver un événement.

### Réserver un événement

Comme je l'ai dit plus tôt, nous ne pouvons pas vérifier si l'utilisateur est authentifié ou non, donc il peut potentiellement réserver un événement plus d'une fois.

Pour gérer cela, j'utiliserai `localStorage` pour éviter les doublons de réservation.

* Dans `db.js`

```javascript
let bookedEvents = [];

const bookEvent = (booked, id) => {
  const getBookedEvents = localStorage.getItem('booked-events');

    if (getBookedEvents) {
     bookedEvents = JSON.parse(localStorage.getItem('booked-events'));
      if(bookedEvents.includes(id)) {
        alert('Il semble que vous avez déjà réservé cet événement') 
      } 
      else {
        saveBooking(booked, id)
     }
    } 
    else {
        saveBooking(booked, id)
    }
};

const saveBooking = (booked, id) => {
    bookedEvents.push(id);
    localStorage.setItem('booked-events', JSON.stringify(bookedEvents));

    const data = { booked: booked +1 }
    db.collection('events').doc(id).update(data)
    .then(() => alert('Événement réservé avec succès'))
    .catch(err => console.log(err))
}

```

Et comme vous pouvez le voir ici, nous vérifions d'abord si l'id de l'événement est stocké ou non dans localStorage. Si c'est le cas, l'utilisateur ne peut pas réserver le même événement à nouveau. Sinon, il pourra réserver l'événement.

Et pour mettre à jour le compteur de réservation, nous utilisons à nouveau `db` pour mettre à jour l'événement dans Firestore.

Le fichier `db.js` est maintenant complet, alors passons à la partie finale et connectons notre projet à `db.js`.

## Afficher et mettre à jour les données avec JavaScript

Comme d'habitude, nous commençons par sélectionner les éléments nécessaires.

```javascript
const eventsContainer = document.querySelector('.events-container')
const nav = document.querySelector('nav')
const welcomeEvent = document.querySelector('.welcome-event')
const form = document.querySelector('.form')

const showEvents = (event, id) => {
  const {name, attendee, status, description, booked} = event

  const eventStatus = status === 0 ? 'free': 'paid'
  const output = `
        <div class="card">
          <div class="card--details">
            <div>
              <h1>${name}</h1>
              <span>${attendee - booked} participants</span>
            </div>
            <span class="card--details-ribbon ribbon-${eventStatus}">
                ${eventStatus}
            </span>
             <p>${description}</p>
            <button onclick="bookEvent(${booked} ,'${id}')" class="btn btn-tertiary">Réserver</button>
          </div>
        </div>
        `
    eventsContainer.innerHTML += output;
}

```

Plus tôt dans cet article, nous avions passé en paramètre à la fonction `showEvents()` l'événement récupéré de Firestore dans le fichier `db.js`.

Nous pouvons maintenant extraire les valeurs contenues dans l'objet événement et les afficher. Et, lorsque l'utilisateur clique sur le bouton pour réserver un événement, nous appellerons la fonction `bookEvent()` pour le gérer.

```javascript
const showLatestEvent = (latestEvent, id) => {
  
  const {name, attendee, status, description, booked} = latestEvent 
  // Obtenir le premier événement
    welcomeEvent.innerHTML = `
    <h1>${name}</h1>
    <p>${description.length >= 100 ? `${description.substring(0, 100)}...` : description}</p>
    <div>
      <span>Participants: ${attendee - booked}</span>
      <span>Statut: ${status === 0 ? 'free': 'paid'}</span>
     </div>
     <button onclick="bookEvent(${booked} ,'${id}')" class="btn btn-tertiary">Réserver</button>
    `
}

form.addEventListener('submit', e => {
  e.preventDefault()
  addNewEvent()
})

window.onscroll = () =>  {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    nav.style.background = 'var(--tertiary-color)';
    nav.style.boxShadow = '0 10px 42px rgba(25,17,34,.1)';
  } else {
    nav.style.background = 'none';
    nav.style.boxShadow = 'none';
  }
}

```

Comme vous pouvez le voir, la méthode `showLatestEvent()` est assez similaire à `showEvents()`, contrairement à l'élément utilisé pour afficher l'événement.

Et, lorsque la description est un peu longue, nous utilisons `substring()` pour tronquer la valeur.

Ensuite, nous écoutons l'élément `form` pour gérer l'événement de soumission et le stocker dans Firestore avec `addNewEvent()`.

Et pour que tout soit joli, lorsque l'utilisateur fait défiler, nous ajoutons une couleur de fond et une ombre à la barre de navigation.

Avec ce changement, nous avons maintenant notre application de réservation d'événements utilisant JavaScript et Firebase.

Merci d'avoir lu cet article.

Vous pouvez la consulter [en direct ici](https://event-booking.netlify.com/) ou trouver le [Code Source ici](https://github.com/ibrahima92/event-booking-app-with-javascript-and-firebase).

[Lire plus d'articles sur mon blog](https://www.ibrahima-ndaw.com) - [S'abonner à ma newsletter](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75) - [Me suivre sur twitter](https://twitter.com/ibrahima92_)