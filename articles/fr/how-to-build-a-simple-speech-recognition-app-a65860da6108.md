---
title: Comment créer une application simple de reconnaissance vocale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T08:15:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-speech-recognition-app-a65860da6108
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e5flIoQf_jfcYYoSD0MkyA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer une application simple de reconnaissance vocale
seo_desc: 'By Chuks Opia


  “In this 10-year time frame, I believe that we’ll not only be using the keyboard
  and the mouse to interact but during that time we will have perfected speech recognition
  and speech output well enough that those will become a standard p...'
---

Par Chuks Opia

> « Dans ce cadre de 10 ans, je crois que nous n'utiliserons pas seulement le clavier et la souris pour interagir, mais pendant cette période, nous aurons perfectionné la reconnaissance vocale et la synthèse vocale suffisamment pour qu'elles deviennent une partie standard de l'interface. » — Bill Gates, 1er octobre 1997

La technologie a parcouru un long chemin, et avec chaque nouvelle avancée, la race humaine devient plus attachée à celle-ci et aspire à ces nouvelles fonctionnalités sur tous les appareils.

Avec l'avènement de Siri, Alexa et Google Assistant, les utilisateurs de technologie ont aspiré à la reconnaissance vocale dans leur utilisation quotidienne d'Internet. Dans cet article, je vais couvrir comment intégrer la reconnaissance vocale native et la synthèse vocale dans le navigateur en utilisant l'API JavaScript [WebSpeech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API).

Selon les documents web de Mozilla :

> L'API Web Speech vous permet d'incorporer des données vocales dans des applications web. L'API Web Speech se compose de deux parties : SpeechSynthesis (Texte-à-Parole) et SpeechRecognition (Reconnaissance Vocale Asynchrone.)

### Exigences pour construire notre application

Pour cette application simple de reconnaissance vocale, nous travaillerons avec seulement trois fichiers qui résideront tous dans le même répertoire :

* `index.html` contenant le HTML pour l'application.
* `style.css` contenant les styles CSS.
* `index.js` contenant le code JavaScript.

De plus, nous devons avoir quelques éléments en place. Ils sont les suivants :

* Connaissance de base de JavaScript.
* Un serveur web pour exécuter l'application. Le [Serveur Web pour Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en) sera suffisant à cette fin.

### Installation de notre application de reconnaissance vocale

Commençons par configurer le HTML et le CSS pour l'application. Voici le balisage HTML :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Reconnaissance Vocale</title>
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css?family=Shadows+Into+Light" rel="stylesheet">
  <!-- chargez font awesome ici pour l'icône utilisée sur la page -->
</head>
<body>
  <div class="container"> <!-- conteneur de la page -->
    <div class="text-box" contenteditable="true"></div> <!-- zone de texte qui contiendra le texte parlé -->
    <i class="fa fa-microphone"></i> <!-- icône de microphone à cliquer avant de parler -->
  </div>
  <audio class="sound" src="chime.mp3"></audio> <!-- son à jouer lorsque nous cliquons sur l'icône => http://soundbible.com/1598-Electronic-Chime.html -->
  <script src="index.js"></script> <!-- lien vers le script index.js -->
</body>
</html>
```

Voici son style CSS accompagnant :

```css
body {
  background: #1e2440;
  color: #f2efe2;
  font-size: 16px;
  font-family: 'Kaushan Script', cursive;
  font-family: 'Shadows Into Light', cursive;
}
.container {
  position: relative;
  border: 1px solid #f2efe2;
  width: 40vw;
  max-width: 60vw;
  margin: 0 auto;
  border-radius: 0.1rem;
  background: #f2efe2;
  padding: 0.2rem 1rem;
  color: #1e2440;
  overflow: scroll;
  margin-top: 10vh;
}
.text-box {
  max-height: 70vh;
  overflow: scroll;
}
.text-box:focus {
  outline: none;
}
.text-box p {
  border-bottom: 1px dotted black;
  margin: 0px !important;
}
.fa {
  color: white;
  background: #1e2440;
  border-radius: 50%;
  cursor: pointer;
  margin-top: 1rem;
  float: right;
  width: 2rem;
  height: 2rem;
  display: flex !important;
  align-items: center;
  justify-content: center;
}
@media (max-width: 768px) {
  .container {
    width: 85vw;
    max-width: 85vw;
  }
.text-box {
    max-height: 55vh;
  }
}
```

Copier le code ci-dessus devrait donner quelque chose de similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WKAizaPcY5uPW0JwsBTk6A.png)
_Interface web pour l'application simple de reconnaissance vocale_

### Alimenter notre application de reconnaissance vocale avec l'API WebSpeech

Au moment de la rédaction, l'API WebSpeech est uniquement disponible dans Firefox et Chrome. Son interface de synthèse vocale réside sur l'objet `window` du navigateur sous `speechSynthesis`, tandis que son interface de reconnaissance vocale réside sur l'objet `window` du navigateur sous `SpeechRecognition` dans Firefox et sous `webkitSpeechRecognition` dans Chrome.

Nous allons définir l'interface de reconnaissance sur `SpeechRecognition` quel que soit le navigateur que nous utilisons :

```js
window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
```

Ensuite, nous allons instancier l'interface de reconnaissance vocale :

```js
const recognition = new SpeechRecognition();
const icon = document.querySelector('i.fa.fa-microphone')
let paragraph = document.createElement('p');
let container = document.querySelector('.text-box');
container.appendChild(paragraph);
const sound = document.querySelector('.sound');
```

Dans le code ci-dessus, en plus d'instancier la reconnaissance vocale, nous avons également sélectionné les éléments `icon`, `text-box`, et `sound` sur la page. Nous avons également créé un élément de paragraphe qui contiendra les mots que nous disons, et nous l'avons ajouté à la `text-box`.

Chaque fois que l'icône du microphone sur la page est cliquée, nous voulons jouer notre son et démarrer le service de reconnaissance vocale. Pour y parvenir, nous ajoutons un écouteur d'événement de clic à l'icône :

```js
icon.addEventListener('click', () => {
  sound.play();
  dictate();
});
const dictate = () => {
  recognition.start();
}
```

Dans l'écouteur d'événement, après avoir joué le son, nous avons créé et appelé une fonction `dictate`. La fonction `dictate` démarre le service de reconnaissance vocale en appelant la méthode `start` sur l'instance de reconnaissance vocale.

Pour retourner un résultat pour ce qu'un utilisateur dit, nous devons ajouter un événement `result` à notre instance de reconnaissance vocale. La fonction `dictate` ressemblera alors à ceci :

```js
const dictate = () => {
  recognition.start();
  recognition.onresult = (event) => {
    const speechToText = event.results[0][0].transcript;
    
    paragraph.textContent = speechToText;
  }
}
```

L'événement résultant retourne un `SpeechRecognitionEvent` qui contient un objet `results`. Celui-ci contient à son tour la propriété `transcript` qui détient la parole reconnue en texte. Nous sauvegardons le texte reconnu dans une variable appelée `speechToText` et le plaçons dans l'élément `paragraph` sur la page.

Si nous exécutons l'application à ce stade, cliquons sur l'`icon` et disons quelque chose, cela devrait apparaître sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1kksWNSfKPzaCJaE9kotsQ.png)
_La parole en texte en plein effet_

### Conclusion avec la synthèse vocale

Pour ajouter la synthèse vocale à notre application, nous utiliserons l'interface `speechSynthesis` de l'API WebSpeech. Nous commencerons par l'instancier :

```
const synth = window.speechSynthesis;
```

Ensuite, nous créerons une fonction `speak` que nous appellerons chaque fois que nous voulons que l'application dise quelque chose :

```js
const speak = (action) => {
  utterThis = new SpeechSynthesisUtterance(action());
  synth.speak(utterThis);
};
```

La fonction `speak` prend en paramètre une fonction appelée `action`. La fonction retourne une chaîne qui est passée à `SpeechSynthesisUtterance`. `SpeechSynthesisUtterance` est l'interface de l'API WebSpeech qui contient le contenu que le service de reconnaissance vocale doit lire. La méthode `speak` de speechSynthesis est ensuite appelée sur son instance et le contenu à lire lui est passé.

Pour tester cela, nous devons savoir quand l'utilisateur a terminé de parler et dit un `mot-clé`. Heureusement, il existe une méthode pour vérifier cela :

```js
const dictate = () => {
  ...
  if (event.results[0].isFinal) {
    if (speechToText.includes('quelle heure est-il')) {
        speak(getTime);
    };
    
    if (speechToText.includes('quelle est la date daujourdhui')) {
        speak(getDate);
    };
    
    if (speechToText.includes('quel temps fait-il à')) {
        getTheWeather(speechToText);
    };
  }
  ...
}
const getTime = () => {
  const time = new Date(Date.now());
  return `il est ${time.toLocaleString('fr-FR', { hour: 'numeric', minute: 'numeric', hour12: true })}`
};
const getDate = () => {
  const time = new Date(Date.now())
  return `aujourdhui nous sommes le ${time.toLocaleDateString()}`;
};
const getTheWeather = (speech) => {
fetch(`http://api.openweathermap.org/data/2.5/weather?q=${speech.split(' ')[5]}&appid=58b6f7c78582bffab3936dac99c31b25&units=metric`)
.then(function(response){
  return response.json();
})
.then(function(weather){
  if (weather.cod === '404') {
    utterThis = new SpeechSynthesisUtterance(`Je ne peux pas trouver la météo pour ${speech.split(' ')[5]}`);
    synth.speak(utterThis);
    return;
  }
  utterThis = new SpeechSynthesisUtterance(`la condition météo à ${weather.name} est principalement composée de ${weather.weather[0].description} à une température de ${weather.main.temp} degrés Celsius`);
  synth.speak(utterThis);
  });
};
```

Dans le code ci-dessus, nous avons appelé la méthode `isFinal` sur notre résultat d'événement qui retourne `true` ou `false` selon que l'utilisateur a terminé de parler ou non.

Si l'utilisateur a terminé de parler, nous vérifions si la transcription de ce qui a été dit contient des mots-clés tels que `quelle heure est-il`, et ainsi de suite. Si c'est le cas, nous appelons notre fonction `speak` et lui passons l'une des trois fonctions `getTime`, `getDate` ou `getTheWeather` qui retournent toutes une chaîne pour que le navigateur la lise.

Notre fichier `index.js` devrait maintenant ressembler à ceci :

```js
window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
const synth = window.speechSynthesis;
const recognition = new SpeechRecognition();

const icon = document.querySelector('i.fa.fa-microphone')
let paragraph = document.createElement('p');
let container = document.querySelector('.text-box');
container.appendChild(paragraph);
const sound = document.querySelector('.sound');

icon.addEventListener('click', () => {
  sound.play();
  dictate();
});

const dictate = () => {
  recognition.start();
  recognition.onresult = (event) => {
    const speechToText = event.results[0][0].transcript;
    
    paragraph.textContent = speechToText;

    if (event.results[0].isFinal) {

      if (speechToText.includes('quelle heure est-il')) {
          speak(getTime);
      };
      
      if (speechToText.includes('quelle est la date daujourdhui')) {
          speak(getDate);
      };
      
      if (speechToText.includes('quel temps fait-il à')) {
          getTheWeather(speechToText);
      };
    }
  }
}

const speak = (action) => {
  utterThis = new SpeechSynthesisUtterance(action());
  synth.speak(utterThis);
};

const getTime = () => {
  const time = new Date(Date.now());
  return `il est ${time.toLocaleString('fr-FR', { hour: 'numeric', minute: 'numeric', hour12: true })}`
};

const getDate = () => {
  const time = new Date(Date.now())
  return `aujourdhui nous sommes le ${time.toLocaleDateString()}`;
};

const getTheWeather = (speech) => {
  fetch(`http://api.openweathermap.org/data/2.5/weather?q=${speech.split(' ')[5]}&appid=58b6f7c78582bffab3936dac99c31b25&units=metric`) 
  .then(function(response){
    return response.json();
  })
  .then(function(weather){
    if (weather.cod === '404') {
      utterThis = new SpeechSynthesisUtterance(`Je ne peux pas trouver la météo pour ${speech.split(' ')[5]}`);
      synth.speak(utterThis);
      return;
    }
    utterThis = new SpeechSynthesisUtterance(`la condition météo à ${weather.name} est principalement composée de ${weather.weather[0].description} à une température de ${weather.main.temp} degrés Celsius`);
    synth.speak(utterThis);
  });
};
```

Cliquons sur l'icône et essayons l'une des phrases suivantes :

* Quelle heure est-il ?
* Quelle est la date d'aujourd'hui ?
* Quel temps fait-il à Lagos ?

Nous devrions obtenir une réponse de l'application.

### Conclusion

Dans cet article, nous avons pu créer une application simple de reconnaissance vocale. Il y a quelques autres choses intéressantes que nous pourrions faire, comme sélectionner une voix différente pour lire aux utilisateurs, mais je vous laisse le soin de le faire.

Si vous avez des questions ou des commentaires, n'hésitez pas à les laisser ci-dessous. J'ai hâte de voir ce que vous allez construire avec cela. Vous pouvez me contacter sur Twitter [@developia_](https://twitter.com/developia_).