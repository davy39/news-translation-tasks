---
title: Comment créer une application de quiz avec React – avec des conseils et du
  code de démarrage
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-09-09T19:47:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-quiz-app-using-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/Build-a-Temperature-control-App--1-.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment créer une application de quiz avec React – avec des conseils et
  du code de démarrage
seo_desc: "In this beginner React tutorial we're going to build a quiz app. We'll\
  \ work with complex state objects, how to handle different state hooks, and render\
  \ things based on state. \nCheck it out:\n\nTry it yourself\nIf you want to have\
  \ a go yourself first, he..."
---

Dans ce tutoriel React pour débutants, nous allons créer une application de quiz. Nous travaillerons avec des objets d'état complexes, comment gérer différents hooks d'état et rendre les éléments en fonction de l'état. 

Découvrez-le :

![](https://jschris.com/262a1fab0110d0d612ed69c9bb7c4e7e/project.gif)

## Essayez par vous-même

Si vous souhaitez essayer par vous-même d'abord, voici les scénarios (vous pouvez également récupérer le code de démarrage ci-dessous) :

- Lorsque l'utilisateur clique sur un bouton, la question suivante doit s'afficher
- Si l'utilisateur répond correctement à la question, son score doit être incrémenté
- Lorsque l'utilisateur arrive à la fin du quiz, son score total doit être affiché

## Vidéo explicative

<iframe width="560" height="315" src="https://www.youtube.com/embed/Lya-qYiDqIA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Code de démarrage

[Téléchargez-le sur GitHub ici.](https://github.com/chrisblakely01/quiz-app)

## C'est parti !

Si vous ouvrez le code de démarrage et allez dans **App.js**, vous verrez que je vous ai fourni une liste de questions/réponses, stockées sous forme de tableau appelé **questions**. C'est notre quiz.

Notre premier objectif est de prendre les données de la question du tableau et de les afficher à l'écran. 

Nous allons supprimer le texte codé en dur et prendre les données de la première question pour l'instant, juste pour commencer. Nous nous occuperons du changement de questions plus tard.

Dans notre JSX, supprimez le texte de la question codé en dur et tapez `{questions[0]}` pour obtenir le premier élément (ou question) de notre tableau de questions.

```jsx
<div className='question-text'>{questions[0]}</div>
```

## Affichage de la question et des réponses

La première question est un objet, nous pouvons donc utiliser la notation par points pour accéder aux propriétés. Maintenant, nous allons simplement faire `{question[0].questionText}` pour accéder au texte de la question pour cet objet :

```jsx
<div className='question-text'>{questions[0].questionText}</div>
```

Enregistrez et exécutez l'application. Remarquez comment le texte est mis à jour. N'oubliez pas que nous prenons simplement le texte de la première question du premier objet de notre tableau de questions.

Nous allons adopter une approche similaire pour les options de réponse. Supprimez les boutons codés en dur et nous allons utiliser la fonction map pour parcourir les options de réponse pour une question donnée.

Rappelez-vous que la fonction map parcourt le tableau et nous donne l'élément actuel sur lequel la boucle se trouve, sous la forme d'une variable.

Remplacez la div "answer-section" par ce qui suit :

```jsx
<div className='answer-section'>
	{questions[0].answerOptions.map((answerOption, index) => (
		<button>{answerOption.answerText}</button>
	))}
</div>
```

Enregistrez et exécutez l'application. Remarquez comment quatre boutons de réponse apparaissent et le texte est rendu dynamiquement. 

Faisons un récapitulatif :

- Nous obtenons la première question du tableau de questions : `questions[0]`
- La première question est un objet, qui contient un tableau de `answerOptions`. Nous pouvons accéder à ce tableau en utilisant la notation par points : `questions[0].answerOptions`
- Comme `answerOptions` est un tableau, nous pouvons le mapper : `questions[0].answerOptions.map`
- À l'intérieur de la fonction map, nous rendons un bouton pour chaque `answerOption`, et affichons le texte

## Changer les questions en utilisant l'état

Maintenant, retournons dans notre JSX. Remarquez comment si nous changeons `questions[0]` en `questions[1]`, ou `questions[2]`, l'interface utilisateur sera mise à jour. Cela est dû au fait qu'il prend les données de différentes questions dans notre tableau de questions, selon l'index.

Ce que nous voulons faire, c'est utiliser un objet d'état pour stocker la question actuelle de l'utilisateur et le mettre à jour lorsqu'un bouton de réponse est cliqué. Vous pouvez voir cela en exécutant le code dans l'exemple final.

Allez-y et ajoutez un objet d'état, qui contiendra le **numéro de la question actuelle** de l'utilisateur. Cela sera initialisé à 0 pour que le quiz prenne la première question du tableau :

```jsx
const [currentQuestion, setCurrentQuestion] = useState(0);
```

Maintenant, nous voulons remplacer le '0' codé en dur dans notre JSX par cette variable. D'abord pour le texte de la question :

```jsx
<div className='question-text'>{questions[currentQuestion].questionText}</div>
```

Et aussi pour la section de la question :

```jsx
<div className='answer-section'>
	{questions[currentQuestion].answerOptions.map((answerOption, index) => (
		<button>{answerOption.answerText}</button>
	))}
</div>
```

Maintenant, si vous initialisez **currentQuestion** à autre chose que 0, par exemple 1 ou 2, l'interface utilisateur sera mise à jour pour afficher la question et les réponses pour cette question particulière. Plutôt cool !

Ajoutons un peu de code pour que lorsque nous cliquons sur une réponse, nous incrémentons la valeur **currentQuestion** pour passer à la question suivante.

Créez une nouvelle fonction appelée **handleAnswerButtonClick**. C'est ce qui sera appelé lorsque l'utilisateur clique sur une réponse. 

Nous allons incrémenter la valeur de la question actuelle de un, la sauvegarder dans une nouvelle variable et définir cette nouvelle variable dans l'état :

```jsx
const handleAnswerButtonClick = (answerOption) => {
	const nextQuestion = currentQuestion + 1;
	setCurrentQuestion(nextQuestion);
};
```

Ajoutez ensuite un événement onClick à notre bouton comme suit :

```jsx
<button onClick={() => handleAnswerButtonClick()}>{answerOption.answerText}</button>
```

Si nous essayons cela, vous verrez que cela fonctionne, jusqu'à ce que nous arrivions à la fin :

![](https://jschris.com/static/d0919a4780449b6f825cbf9c88041f24/e46b2/error.webp)

Alors, que se passe-t-il ? Eh bien, dans notre fonction **handleAnswerButtonClick**, nous incrémentons le nombre et le définissons dans l'état. C'est correct. 

Mais rappelez-vous que nous utilisons ce nombre pour accéder à un tableau, afin d'obtenir la question et les options de réponse. Une fois que nous arrivons à 5, cela ne fonctionnera plus car il n'y a pas de 5ème élément !

Faisons une vérification pour nous assurer que nous ne dépassons pas la limite. Dans notre fonction handleAnswerButtonClick, ajoutons la condition suivante :

```jsx
if (nextQuestion < questions.length) {
	setCurrentQuestion(nextQuestion);
} else {
	alert('vous avez atteint la fin du quiz');
}
```

Cela signifie essentiellement que si le numéro de la question suivante est inférieur au nombre total de questions, mettez à jour l'état pour passer à la question suivante. Sinon, nous avons atteint la fin du quiz, alors affichons une alerte pour l'instant.

## Affichage de l'écran de score

Au lieu d'afficher une alerte, ce que nous voulons faire, c'est afficher l'écran de "score". 

Si nous regardons le JSX, vous remarquerez que j'ai mis le balisage ici pour vous, nous devons simplement remplacer "false" par la logique.

Alors, comment procédons-nous ? Eh bien, c'est une chose parfaite à mettre dans l'état !

Ajoutez un autre objet d'état qui stockera si nous voulons afficher l'écran de score ou non :

```jsx
const [showScore, setShowScore] = useState(false);
```

Et remplacez `false` par `showScore` dans notre JSX :

```jsx
<div className='app'>{showScore ? <div className='score-section'>// ... balisage de la section de score</div> : <>// ... balisage de la question/réponse du quiz</>}</div>
```

Rien ne changera, mais si nous changeons la valeur de l'état en true, alors la div de score s'affichera. Cela est dû au fait que tout est enveloppé dans un ternaire, ce qui signifie :

> "Si showScore est vrai, rendez le balisage de la section de score, sinon, rendez le balisage de la question/réponse du quiz"

Maintenant, nous voulons mettre à jour cette variable d'état lorsque l'utilisateur a atteint la fin du quiz. Nous avons déjà écrit la logique pour cela dans notre fonction handleAnswerButtonClick.

Tout ce que nous avons à faire est de remplacer la logique de l'alerte qui met à jour la variable **showScore** pour qu'elle soit vraie :

```jsx
if (nextQuestion < questions.length) {
	setCurrentQuestion(nextQuestion);
} else {
	setShowScore(true);
}
```

Si nous cliquons sur les réponses du quiz, il affichera la section de score lorsque nous arriverons à la fin. Pour l'instant, le texte et le score affichés sont une chaîne codée en dur, nous devons donc le rendre dynamique.

## Enregistrement du score

Notre prochaine tâche est de stocker un score quelque part dans notre application et d'incrémenter cette valeur si l'utilisateur sélectionne l'option correcte.

L'endroit logique pour faire cela est dans la fonction "handleAnswerOptionClick".

Rappelez-vous lorsque nous itérons sur les **answerOptions**, la fonction map nous donne un objet pour chaque qui inclut le **questionText**, et une **valeur booléenne** indiquant si cette réponse est correcte ou non. Ce booléen est ce que nous utiliserons pour nous aider à incrémenter notre score. 

Dans notre bouton, mettez à jour la fonction comme suit :

```jsx
onClick={()=> handleAnswerButtonClick(answerOption.isCorrect)
```

Mettez ensuite à jour la fonction pour accepter ce paramètre :

```jsx
const handleAnswerButtonClick = (isCorrect) => {
	//... autre code
};
```

Maintenant, nous pouvons ajouter un peu de logique ici dans notre fonction. Pour l'instant, nous voulons dire "si isCorrect est vrai, nous voulons afficher une alerte" :

```jsx
const handleAnswerButtonClick = (isCorrect) => {
	if (isCorrect) {
		alert("la réponse est correcte !")
	}

	//...autre code
};
```

Cela est la même chose que `if(isCorrect === true)`, juste une version abrégée. Maintenant, si nous essayons cela, vous verrez que nous obtenons une alerte lorsque nous cliquons sur la bonne réponse.

Juste pour récapituler jusqu'à présent :

- Lorsque nous itérons sur les boutons, nous passons la valeur booléenne `isCorrect` pour ce bouton à la fonction **handleAnswerButtonClick**
- Dans la fonction, nous vérifions si cette valeur est vraie et affichons une alerte si c'est le cas.

Ensuite, nous voulons réellement enregistrer le score. Comment pensez-vous que nous faisons cela ? Si vous avez dit valeur d'état, vous avez raison !

Allez-y et ajoutez une autre valeur d'état appelée "score". N'oubliez pas de préfixer la fonction pour changer la valeur avec "set" pour qu'elle soit setScore. Initialisez-la à `0` :

```jsx
const [score, setScore] = useState(0);
```

Ensuite, au lieu d'afficher une alerte, nous voulons mettre à jour notre score de 1 si l'utilisateur a donné la bonne réponse. 

Dans notre fonction **handleAnswerButtonClick**, supprimez l'alerte et incrémentez notre score de un :

```jsx
const handleAnswerButtonClick = (isCorrect) => {
	if (answerOption.isCorrect) {
		setScore(score + 1);
	}

	//...autre code
};
```

## Affichage du score

Pour afficher le score, nous devons apporter une petite modification à notre code de rendu. Dans notre JSX, supprimez la chaîne codée en dur dans la section de score et ajoutez cette nouvelle variable :

```jsx
<div className='score-section'>
	Vous avez obtenu {score} sur {questions.length}
</div>
```

```jsx
<div className='score-section'>
	Vous avez obtenu {score} sur {questions.length}
</div>
```

Maintenant, si nous passons par les réponses, le score est dynamique et s'affichera correctement à la fin !

Une dernière chose avant de terminer notre application de quiz : vous remarquerez que la question actuelle affichée sur l'interface utilisateur est toujours "1", car elle est codée en dur. Nous devons changer cela pour le rendre plus dynamique. 

Remplacez le "question-count" par ce qui suit :

```jsx
<div className='question-count'>
	<span>Question {currentQuestionIndex + 1}</span>/{questions.length}
</div>
```

N'oubliez pas que nous avons besoin du +1 car les ordinateurs commencent à compter à partir de 0 et non de 1.

## Vous voulez plus d'idées de projets ?

Pourquoi ne pas essayer de créer des projets React pour booster votre apprentissage encore plus loin ? Chaque semaine, j'envoie un nouveau projet pour que vous puissiez essayer un exemple de travail, un code de démarrage et des conseils. [Abonnez-vous pour recevoir cela directement dans votre boîte de réception !](https://subscribe.jschris.com)