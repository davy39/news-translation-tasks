---
title: Comment intégrer des questions de quiz à choix multiples dans votre article
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-06T08:30:53.000Z'
originalURL: https://freecodecamp.org/news/multiple-choice-quiz-template
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bc5740569d1a4ca2dcf.jpg
tags:
- name: blog
  slug: blog
- name: Blogging
  slug: blogging
seo_title: Comment intégrer des questions de quiz à choix multiples dans votre article
seo_desc: 'By Alexander Arobelidze

  In my experience, supplementing study with practical exercises greatly improves
  my understanding of a topic. This is especially true when I can test my knowledge
  as I go and receive instant feedback for each question.

  The mult...'
---

Par Alexander Arobelidze

D'après mon expérience, compléter l'étude par des exercices pratiques améliore grandement ma compréhension d'un sujet. Cela est particulièrement vrai lorsque je peux tester mes connaissances au fur et à mesure et recevoir un retour instantané pour chaque question.

Le format de quiz à choix multiples est parfait pour cela. J'ai développé une méthode pour intégrer des questions à choix multiples dans les articles de mathématiques que je rédige pour freeCodeCamp, et je souhaite montrer à d'autres auteurs comment faire de même.

## Comment ajouter du code à votre article

L'éditeur Ghost vous permet d'intégrer des blocs de code tout au long d'un article. L'éditeur de code peut être accessible en cliquant sur le bouton rond avec un signe plus **(+)** utilisé pour ajouter des images, des vidéos YouTube, et ainsi de suite :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-25.png)

Cliquez sur le bouton "HTML" pour ajouter un éditeur à l'article. L'éditeur supporte HTML, CSS, et même JavaScript.

Une fois que vous commencez à ajouter du code, cliquez n'importe où en dehors du cadre de l'éditeur pour rendre le code et voir votre progression. Double-cliquez sur la sortie rendue pour rouvrir la fenêtre de l'éditeur :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/editor.gif)

Pour tester la fonctionnalité de votre code, sauvegardez l'article en appuyant sur Ctrl/⌘ + S, puis cliquez sur le bouton "Voir l'aperçu" qui apparaît dans le coin inférieur gauche :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-26.png)

Votre article s'ouvrira dans un onglet séparé où vous pourrez voir comment votre code sera rendu une fois votre article publié. Prenez le temps de vérifier le style et la fonctionnalité de votre quiz à choix multiples.

Le code de base pour le quiz à choix multiples est disponible dans la section suivante. Tout ce que vous avez à faire est de le coller dans votre propre article et de changer la question et les réponses.

## Comment fonctionne le quiz à choix multiples

Vous pouvez ajouter autant de questions différentes que vous le souhaitez. Cependant, bien que votre article puisse avoir plusieurs quiz, ils sont tous contenus dans un **seul corps HTML** en coulisses. Chaque élément de question commence avec le code suivant :

```html
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <h3>ÉCRIVEZ VOTRE QUESTION ICI</h3>
  <p>Choisissez 1 réponse</p>
  <hr />
```

Chacun des éléments `div` suivants contient une réponse possible :

```html
  ...
  <div id='block-11' style='padding: 10px;'>
    <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      RÉPONSE 1</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      RÉPONSE 2</label>
    <span id='result-12'></span>
  </div>
  <hr />
  ...
```

Au moment de la rédaction, l'éditeur de code intégré de Ghost ne supporte pas les littéraux de gabarit, donc certaines choses doivent être codées en dur.

N'oubliez pas que toutes les questions sont essentiellement chargées ensemble en coulisses, donc les chiffres à deux chiffres dans chaque `id` représentent ce qui suit :

* Le **premier** chiffre indique l'ordre de la question à choix multiples dans l'article (1 est la question un, 2 est la question deux, et ainsi de suite)
* Le **deuxième** chiffre indique l'ordre de chaque réponse possible dans son bloc de question (1 est le choix de réponse un, 2 est le choix de réponse deux, etc.)

Par exemple, `block-12` représente **question 1/choix de réponse 2**, tandis que `block-43` est **question 4/choix de réponse 3**.

Cette convention d'indexation est nécessaire pour que différents blocs de questions fonctionnent indépendamment les uns des autres.

Une logique similaire s'applique aux noms de fonctions responsables de l'interactivité. Le code qui gère l'interaction de l'utilisateur est placé dans des balises `<script>` et se compose de deux parties. La première partie est la fonction qui évalue les réponses et affiche les résultats :

```js
function displayAnswer1() {
    if (document.getElementById('option-11').checked) {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
    }
    if (document.getElementById('option-12').checked) {
      document.getElementById('block-12').style.border = '3px solid red'
      document.getElementById('result-12').style.color = 'red'
      document.getElementById('result-12').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-13').checked) {
      document.getElementById('block-13').style.border = '3px solid red'
      document.getElementById('result-13').style.color = 'red'
      document.getElementById('result-13').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-14').checked) {
      document.getElementById('block-14').style.border = '3px solid red'
      document.getElementById('result-14').style.color = 'red'
      document.getElementById('result-14').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
```

Comme le suggère le nom, la fonction `displayAnswer1` gère la première question dans un article. S'il y a une troisième question dans votre article, `displayAnswer3` la gérera.

Dans l'exemple ci-dessus, `option-11` est la bonne réponse, et le style dans le premier bloc `if` est mis à jour pour montrer que la bonne réponse a été sélectionnée. Si l'une des autres réponses incorrectes est sélectionnée, le style est mis à jour pour refléter cela.

N'hésitez pas à jouer avec les fonctions `displayAnswer_` dans votre propre article. Il suffit de vous souvenir d'attacher le style approprié aux réponses correctes et incorrectes.

Voici la deuxième partie du code qui gère l'interaction de l'utilisateur :

```js
function showCorrectAnswer1() {
    let showAnswer1 = document.createElement('p')
    showAnswer1.innerHTML = 'Show Corrent Answer'
    showAnswer1.style.position = 'relative'
    showAnswer1.style.top = '-180px'
    showAnswer1.style.fontSize = '1.75rem'
    document.getElementById('showanswer1').appendChild(showAnswer1)
    showAnswer1.addEventListener('click', () => {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
      document.getElementById('showanswer1').removeChild(showAnswer1)
    })
  }
```

Cette fonction s'appelle `showCorrectAnswer1` car elle gère la première question à choix multiples de l'article. Vous devrez ajouter `showCorrectAnswer2`, `showCorrectAnswer3`, et plus si votre article a plus d'une question.

Veuillez jouer avec le style et les dimensions utilisés dans tout le code, et personnalisez-le à votre goût. De plus, je suis sûr qu'il existe d'autres moyens de mettre en œuvre des quiz à choix multiples, mais c'est le mien, et je suis heureux de le partager avec vous.

Voici le code complet et un exemple fonctionnel :

```html
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <h3>Quelle fraction d'une journée représente 6 heures ?</h3>
  <p>Choisissez 1 réponse</p>
  <hr />

  <div id='block-11' style='padding: 10px;'>
    <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6/24</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6</label>
    <span id='result-12'></span>
  </div>
  <hr />

  <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/3</label>
    <span id='result-13'></span>
  </div>
  <hr />

  <div id='block-14' style='padding: 10px;'>
    <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/6</label>
    <span id='result-14'></span>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer1()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer1'></a>
<script>
  //    La fonction évalue la réponse et affiche le résultat
  function displayAnswer1() {
    if (document.getElementById('option-11').checked) {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
    }
    if (document.getElementById('option-12').checked) {
      document.getElementById('block-12').style.border = '3px solid red'
      document.getElementById('result-12').style.color = 'red'
      document.getElementById('result-12').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-13').checked) {
      document.getElementById('block-13').style.border = '3px solid red'
      document.getElementById('result-13').style.color = 'red'
      document.getElementById('result-13').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-14').checked) {
      document.getElementById('block-14').style.border = '3px solid red'
      document.getElementById('result-14').style.color = 'red'
      document.getElementById('result-14').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
  // la fonction affiche le lien vers la bonne réponse
  function showCorrectAnswer1() {
    let showAnswer1 = document.createElement('p')
    showAnswer1.innerHTML = 'Show Corrent Answer'
    showAnswer1.style.position = 'relative'
    showAnswer1.style.top = '-180px'
    showAnswer1.style.fontSize = '1.75rem'
    document.getElementById('showanswer1').appendChild(showAnswer1)
    showAnswer1.addEventListener('click', () => {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
      document.getElementById('showanswer1').removeChild(showAnswer1)
    })
  }
</script>
```

<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <h3>Quelle fraction d'une journée représente 6 heures ?</h3>
  <p>Choisissez 1 réponse</p>
  <hr />

  <div id='block-11' style='padding: 10px;'>
    <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6/24</label>
    <span id='result-11'></span>
  </div>
  <hr />

  <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      6</label>
    <span id='result-12'></span>
  </div>
  <hr />

  <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/3</label>
    <span id='result-13'></span>
  </div>
  <hr />

  <div id='block-14' style='padding: 10px;'>
    <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
      <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
      1/6</label>
    <span id='result-14'></span>
  </div>
  <hr />
  <button type='button' onclick='displayAnswer1()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Submit</button>
</div>
<a id='showanswer1'></a>
<script>
  //    La fonction évalue la réponse et affiche le résultat
  function displayAnswer1() {
    if (document.getElementById('option-11').checked) {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
    }
    if (document.getElementById('option-12').checked) {
      document.getElementById('block-12').style.border = '3px solid red'
      document.getElementById('result-12').style.color = 'red'
      document.getElementById('result-12').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-13').checked) {
      document.getElementById('block-13').style.border = '3px solid red'
      document.getElementById('result-13').style.color = 'red'
      document.getElementById('result-13').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('option-14').checked) {
      document.getElementById('block-14').style.border = '3px solid red'
      document.getElementById('result-14').style.color = 'red'
      document.getElementById('result-14').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
  // la fonction affiche le lien vers la bonne réponse
  function showCorrectAnswer1() {
    let showAnswer1 = document.createElement('p')
    showAnswer1.innerHTML = 'Show Corrent Answer'
    showAnswer1.style.position = 'relative'
    showAnswer1.style.top = '-180px'
    showAnswer1.style.fontSize = '1.75rem'
    document.getElementById('showanswer1').appendChild(showAnswer1)
    showAnswer1.addEventListener('click', () => {
      document.getElementById('block-11').style.border = '3px solid limegreen'
      document.getElementById('result-11').style.color = 'limegreen'
      document.getElementById('result-11').innerHTML = 'Correct!'
      document.getElementById('showanswer1').removeChild(showAnswer1)
    })
  }
</script>

Vous pouvez également trouver le code de base complet [ici sur GitHub](https://github.com/sandroarobeli/quiz-template/blob/master/testTemplateHTML.txt).