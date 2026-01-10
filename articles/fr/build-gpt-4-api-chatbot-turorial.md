---
title: Comment construire un ChatBot en utilisant l'API GPT-4 – Tutoriel complet basé
  sur un projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-21T14:07:17.000Z'
originalURL: https://freecodecamp.org/news/build-gpt-4-api-chatbot-turorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Slide-16_9
seo_title: Comment construire un ChatBot en utilisant l'API GPT-4 – Tutoriel complet
  basé sur un projet
---

15.png
tags:
- name: IA
  slug: ia
- name: Intelligence Artificielle
  slug: intelligence-artificielle
- name: '#chatbots'
  slug: chatbots
- name: openai
  slug: openai
seo_title: null
seo_desc: "Par Tom Chant\nLes chatbots transforment la façon dont nous interagissons en ligne. Grâce\
  \ à l'API OpenAI, créer des chatbots intelligents et conscients du contexte est désormais à\
  \ la portée de tout développeur web en herbe. \nDans ce tutoriel, je vais vous apprendre tout\
  \ ce dont vous avez besoin..."
---

Par Tom Chant

Les chatbots transforment la façon dont nous interagissons en ligne. Grâce à l'API OpenAI, créer des chatbots intelligents et conscients du contexte est désormais à la portée de tout développeur web en herbe. 

Dans ce tutoriel, je vais vous apprendre tout ce que vous devez savoir pour construire votre propre chatbot en utilisant l'API GPT-4. 

Pour une plongée plus profonde dans l'API OpenAI, j'ai créé un cours de 4,5 heures, "Build AI Apps with ChatGPT, DALL-E, and GPT-4", que vous pouvez trouver sur [FreeCodeCamps YouTube Channel](https://www.youtube.com/watch?v=jlogLBkPZ2A) et [Scrimba](https://scrimba.com/links/openai-api-course).

## Table des matières

* [L'application que nous construisons](#heading-lapplication-que-nous-construisons)
* [Prérequis](#heading-prerequis)
* [Le HTML et CSS pour l'application](#heading-le-html-et-css-pour-lapplication)
* [Comment stocker la clé API](#heading-comment-stocker-la-cle-api)
* [Comment importer la clé API dans index.js](#heading-comment-importer-la-cle-api-dans-indexjs)
* [Comment installer la dépendance OpenAI](#heading-comment-installer-la-dependance-openai)
* [Comment utiliser la dépendance OpenAI](#heading-comment-utiliser-la-dependance-openai)
* [Le flux de cette application](#heading-le-flux-de-cette-application)
* [Un tableau pour stocker la conversation](#heading-un-tableau-pour-stocker-la-conversation) 
* [Comment gérer l'entrée de l'utilisateur](#heading-comment-gerer-lentree-de-lutilisateur)
* [C'est l'heure de l'IA](#heading-cest-lheure-de-lia)
* [Comment implémenter l'effet machine à écrire](#heading-comment-implementer-leffet-machine-a-ecrire)
* [Conclusion](#heading-conclusion)

## L'application que nous construisons

![KnowItAll Chatbot](https://www.freecodecamp.org/news/content/images/2023/06/image-168.png)
_Capture d'écran de l'application que vous allez construire_

Rencontrez _KnowItAll_, un ChatBot avec des pouvoirs de conversation extraordinaires. Vous pouvez lui poser des questions, lui demander de créer du contenu, corriger le langage, suggérer des modifications ou traduire. Il peut même écrire du code sur demande.

## Prérequis

Dans ce tutoriel, vous utiliserez HTML, CSS et JavaScript vanilla. Une compréhension de base de JavaScript est suffisante – vous n'avez pas besoin d'être super avancé.

Vous aurez également besoin d'un compte OpenAI gratuit, que vous pouvez obtenir [ici](https://openai.com/). Les crédits complémentaires que vous recevez lors de l'inscription devraient être plus que suffisants pour compléter ce tutoriel. Pendant le processus d'inscription, assurez-vous de copier et coller votre clé API quelque part en sécurité, car vous en aurez besoin bientôt.

Ce tutoriel utilise le modèle GPT-4. Au moment de la rédaction, il y a une liste d'attente pour GPT-4 (vous pouvez la rejoindre [ici](https://openai.com/waitlist/gpt-4-api)). Mais ne vous inquiétez pas si vous n'avez pas encore accès, le modèle GPT-3.5-turbo est entièrement compatible avec tout ce que nous faisons dans ce tutoriel, et il est disponible pour tous maintenant. 

Et si vous ne savez pas ce qu'est un modèle OpenAI, ne vous inquiétez pas, nous en parlerons plus en détail dans un instant.

OK, commençons à coder !

## Le HTML et CSS pour l'application

Avant de plonger dans les composants JavaScript et IA, nous devons établir les fondations HTML et CSS de cette application. Ci-dessous, j'ai intégré un Scrim, qui est un éditeur de code interactif/capture d'écran. Dans ce scrim, vous pouvez :

* Parcourir le HTML et le CSS utilisés dans ce projet
* Cliquer sur PREVIEW pour voir le projet dans un mini navigateur
* Regarder une explication pas à pas du HTML et du CSS et faire une pause à tout moment pour jouer avec le code. 

Et si vous voulez exécuter ce code localement, vous pouvez cliquer sur l'icône d'engrenage (⚙️) en bas à droite et sélectionner _Download as zip._ Vous obtiendrez un dossier zippé avec tout le HTML, le CSS et les images. Vous pouvez dézipper ce dossier et l'ouvrir dans VS Code ou dans l'environnement de développement que vous préférez. 

Cliquez [ici](https://scrimba.com/learn/buildaiapps/starter-code-coa28453fbd547f14691eb135) pour une version plein écran de ce scrim.

<iframe src="https://scrimba.com/learn/buildaiapps/starter-code-coa28453fbd547f14691eb135" title="Un scrim intégré avec HTML et CSS pour l'application" style="width: 100%; height: 400px"></iframe>

Je veux attirer votre attention sur les lignes 22-24 de index.html qui contiennent une bulle de dialogue codée en dur du chatbot pour démarrer la conversation :

```html
<div class="speech speech-ai">
    Comment puis-je vous aider ?
</div>
```

Comme vous pouvez le voir sur la capture d'écran près du haut de cet article, chaque conversation commence avec le chatbot demandant _Comment puis-je vous aider ?_ Notez les deux classes CSS `speech` et `speech-ai`, qui stylisent la bulle de dialogue.

À part cela, il n'y a rien de particulièrement inhabituel avec ce HTML et ce CSS et nous ne nous y référerons pas beaucoup dans ce tutoriel. Mais prenez un moment pour soit le parcourir soit regarder la visite guidée avant de continuer.

## Comment stocker la clé API

Comme l'API OpenAI est centrale à ce projet, vous devez stocker la clé API OpenAI dans l'application.

⚠️ Souvenez-vous – votre clé API est vulnérable dans ce projet front-end uniquement. Lorsque vous exécutez cette application dans un navigateur, votre clé API sera visible dans les outils de développement, sous l'onglet réseau. Cela signifie que vous ne devez exécuter ce projet qu'en local. 

Si vous souhaitez déployer ce projet pour le partager et l'inclure dans votre portfolio, dans la troisième section du cours complet [YouTube](https://www.youtube.com/watch?v=jlogLBkPZ2A)/[Scrimba](https://scrimba.com/learn/buildaiapps) je montre comment vous pouvez utiliser les fonctions sans serveur de Netlify pour garder la clé API cachée en toute sécurité lors du déploiement.

Ok, avec cet avertissement écarté, continuons. Dans votre dossier de projet, créez un nouveau fichier appelé `env.js` pour contenir votre clé API.

À l'intérieur de `env.js`, configurez une const `process` qui contiendra un objet avec une seule propriété `env`. Cela stockera votre clé API dans une paire clé/valeur, où la clé est `OPENAI_API_KEY` et la valeur est la clé API elle-même. (Veuillez noter, la clé API dans le code ci-dessous n'est pas réelle !)

```js
export const process = {
    env: {
        OPENAI_API_KEY: "sk-123456789123456789123456789123456789123456789123"
    }
}
```

Voici un scrim mis à jour montrant tout le code du projet jusqu'à présent :

<iframe src="https://scrimba.com/scrim/co7b84323b2e1ffea0d0ea4bf" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

## Comment importer la clé API dans `index.js`

Ensuite, en haut de `index.js`, importez votre clé API depuis `env.js` avec cette instruction d'importation.

```js
import { process } from '/env.js'

```

Ceci est une _importation nommée_ ce qui signifie que vous incluez le nom de l'entité que vous importez entre accolades. Maintenant, l'objet `process` entier sera disponible dans `index.js`.

Comme vous utilisez JavaScript depuis plus d'un fichier, vous devez dire au navigateur de s'attendre à du JavaScript modulaire. Ajoutez donc `type="module"` à la balise script dans `index.html`.

```js
<script src="index.js" type="module"></script>

```

Et juste pour vérifier que vous n'avez pas fait de fautes de frappe qui causent des bugs plus tard, affichez `process` depuis `index.js`.

```js
import { process } from '/env.js'

console.log(process)
//{env: {OPENAI_API_KEY: "sk-123456789123456789123456789123456789123456789123"}}

```

Voici un scrim avec le code jusqu'à présent :

<iframe src="https://scrimba.com/scrim/cob3249dfab8737357f28fd34" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

## Comment installer la dépendance OpenAI

Vous pouvez accéder à l'API OpenAI avec une requête `fetch` régulière, mais il est beaucoup plus facile d'utiliser la dépendance OpenAI. Si vous travaillez localement, vous pouvez l'ajouter en utilisant NPM :

```terminal
$ npm install openai

```

Ou si vous travaillez dans Scrimba, survolez votre curseur sur DEPENDENCIES et cliquez sur l'icône des trois points qui apparaît.

![Un menu à trois points apparaît à côté des dépendances](https://www.freecodecamp.org/news/content/images/2023/06/image-169.png)
_Le menu à trois points adjacent aux dépendances_

Dans le menu déroulant, sélectionnez Add module.

![Menu déroulant avec l'option 'add module'](https://www.freecodecamp.org/news/content/images/2023/06/image-170.png)
_Menu déroulant avec l'option 'add module'_

Cela fera apparaître une boîte de dialogue. Tapez `openai`, cliquez sur ADD, et Scrimba fera le reste. 

![La boîte de dialogue Add NPM package](https://www.freecodecamp.org/news/content/images/2023/06/image-171.png)
_La boîte de dialogue Add NPM package_

Vous verrez alors la dépendance OpenAI listée dans la barre latérale.

Que vous travailliez localement ou dans Scrimba, vous avez maintenant la dépendance OpenAI installée.

## Comment utiliser la dépendance OpenAI

Vous devez importer deux constructeurs depuis la dépendance. Ils sont nécessaires pour configurer l'application pour utiliser l'API. Ce sont `Configuration` et `OpenAIApi` et vous pouvez les importer en ajoutant la ligne de code suivante à `index.js` :

```js
import { Configuration, OpenAIApi } from 'openai'

```

Pour interagir avec l'API, vous devez configurer votre propre objet `configuration` (notez le 'c' minuscule) en utilisant le constructeur `Configuration`.

```js
const configuration = new Configuration()

```

Ensuite, passez-lui un objet avec une paire clé/valeur. La clé sera `apiKey` et la valeur sera notre clé API que vous avez importée depuis `process` et à laquelle vous pouvez accéder avec `process.env.OPENAI_API_KEY`.

```js
const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY
})

```

Ensuite, vous devez passer `configuration` au constructeur `OpenAIApi`. Enregistrez cette nouvelle instance de `OpenAIApi` dans une const `openai` (notez le 'o' minuscule).

```js
const openai = new OpenAIApi(configuration)

```

Et pour vérifier que cela fonctionne, affichez `openai`.

```js
console.log(openai)
//OpenAIApi$1 {basePath: "<https://api.openai.com/v1>", configuration: {apiKey: "sk-12345678912345678912345678...", baseOptions: {headers: {User-Agent: "OpenAI/NodeJS/3.2.1", Authorization: "Bearer sk-1234567891234567891..."}}}}

```

Voici un scrim avec tout le code jusqu'à présent :

<iframe src="https://scrimba.com/scrim/cocbf43a78e2d0c1915a3cd7e" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

N'oubliez pas que vous pouvez cliquer sur l'icône d'engrenage (⚙️) pour télécharger tout le code dans un dossier zippé.

Maintenant que vous avez terminé la configuration de la dépendance de l'API OpenAI, vous pouvez procéder à son utilisation. Mais avant de continuer à écrire plus de code, prenons un moment pour imaginer comment ce chatbot fonctionnera.

## Le flux de cette application

Un défi majeur lors de l'utilisation des modèles OpenAI est qu'ils ne conservent pas les requêtes ou les réponses des interactions précédentes. En fait, ils n'ont aucun souvenir de leurs conversations passées avec vous. Cela peut conduire à des conversations disjointes et confuses comme celle-ci :

`Humain : Qui a été la première personne à marcher sur la lune ?`

`IA : Neil Armstrong.`

`Humain : Quel âge avait-il à l'époque ?`

`IA : Quel âge avait qui ?`

`Humain : ???`

Par conséquent, pour créer un chatbot capable de mener une conversation cohérente, nous devons fournir au modèle OpenAI une forme de mémoire. 

Heureusement, il existe une manière simple de le faire : nous incluons l'ensemble de la conversation telle qu'elle se présente actuellement avec chaque appel API. Cela permet à l'API d'utiliser le contexte de la conversation lors de la formation des complétions pour mieux comprendre les questions qui lui sont posées.

Ainsi, l'application fonctionne comme suit :

![1. L'utilisateur tape une question dans le champ de saisie et appuie sur envoyer.](https://www.freecodecamp.org/news/content/images/2023/06/image-172.png)
_L'utilisateur tape une question dans le champ de saisie et appuie sur envoyer._

Le message codé en dur _Comment puis-je vous aider ?_ est affiché. L'utilisateur tape une question ou une demande et appuie sur _entrée_ ou appuie sur le bouton d'envoi.

![2. La question est rendue dans le DOM.](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-21-at-11.28.11.png)
_La question est rendue dans le DOM._

La question est rendue dans le DOM dans une bulle de dialogue verte et la saisie est effacée.

![3. La question est stockée dans un tableau. Ce tableau est la seule source de vérité pour la conversation.](https://www.freecodecamp.org/news/content/images/2023/06/image-174.png)
_La question est stockée dans un tableau. Ce tableau est la seule source de vérité pour la conversation._

La question est stockée dans un tableau. Ce tableau contiendra toute la conversation et sert de seule source de vérité. Cela permet à l'application d'avoir une "mémoire" de la conversation afin qu'elle puisse comprendre les demandes et contextualiser ses réponses.

![4. Le tableau est envoyé à l'API OpenAI.](https://www.freecodecamp.org/news/content/images/2023/06/image-175.png)
_Le tableau est envoyé à l'API OpenAI._

Le tableau est envoyé à l'API. À mesure que la conversation grandit, ce tableau contiendra de plus en plus d'éléments.

![5. L'API OpenAI envoie une réponse avec la réponse. (Ceci est connu sous le nom de complétion.)](https://www.freecodecamp.org/news/content/images/2023/06/image-176.png)
_L'API OpenAI envoie une réponse avec la réponse. (Ceci est connu sous le nom de complétion.)_

L'API OpenAI envoie une réponse. Dans cette réponse se trouve le langage réel généré par le modèle IA. Cela s'appelle la _complétion_.

![6. La complétion est stockée dans le tableau et rendue dans le DOM.](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-21-at-11.30.23.png)
_La complétion est stockée dans le tableau et rendue dans le DOM._

La complétion est ajoutée au tableau contenant la conversation afin qu'elle puisse être utilisée pour contextualiser toute demande future à l'API. La complétion est également rendue dans le DOM afin que l'utilisateur puisse la voir.

![7. L'utilisateur continue la conversation.](https://www.freecodecamp.org/news/content/images/2023/06/image-178.png)
_L'utilisateur continue la conversation._

L'utilisateur continue maintenant la conversation. Et tout ce qu'il tape est rendu dans le DOM.

![8. L'entrée de l'utilisateur est ajoutée au tableau de conversation et le tableau entier est envoyé à l'API.](https://www.freecodecamp.org/news/content/images/2023/06/image-179.png)
_L'entrée de l'utilisateur est ajoutée au tableau de conversation et le tableau entier est envoyé à l'API._

⚠️L'étape 8 est particulièrement importante car ici la question _Combien de personnes y vivent ?_ ne mentionne pas _Paris_, donc l'API ne peut répondre correctement que si elle obtient le contexte de la conversation à partir du tableau que nous envoyons avec chaque demande.

![9. La réponse de l'API OpenAI montre qu'elle comprend le contexte de la question.](https://www.freecodecamp.org/news/content/images/2023/06/image-180.png)
_La réponse de l'API OpenAI montre qu'elle comprend le contexte de la question._

D'après sa réponse, nous pouvons voir que l'API a bien le contexte de la conversation à partir du tableau – elle savait que nous parlions de Paris même si Paris n'était pas mentionné dans la question _Combien de personnes y vivent ?_ Nous pouvons donc être sûrs que nous pourrons avoir une conversation logique et fluide avec le chatbot.

Maintenant que vous avez un aperçu de la façon dont l'application va fonctionner, plongeons dans les détails de l'IA.

## Un tableau pour stocker la conversation 

Comme mentionné précédemment, l'API OpenAI doit être fournie avec la conversation telle qu'elle existe à ce moment-là avec chaque appel API. La conversation doit être structurée sous forme de tableau d'objets, chaque objet suivant un format spécifique.

Tout d'abord, configurez un tableau et appelez-le `conversationArr`.

```js
const conversationArr = []

```

Chaque élément de ce tableau sera un objet avec deux paires clé/valeur. La première clé sera `role` et la deuxième clé sera `content`. Cette structure sera cohérente pour tous les objets stockés dans le tableau tout au long du projet.

Le premier objet du tableau contiendra des instructions pour le chatbot. Cet objet, connu sous le nom d'_objet d'instruction_, vous permet de contrôler la personnalité du chatbot et de fournir des instructions comportementales, de spécifier la longueur des réponses, et plus encore. 

La propriété `role` de l'objet d'instruction doit contenir la chaîne `'system'` et le `content` doit contenir votre instruction dans une chaîne. 

Voici quelques exemples d'instructions :

`'Vous êtes un assistant utile'`

`'Vous répondez en français'`

`'Vous traduisez tout ce que je dis en espagnol'`

`'Vous êtes un assistant utile qui donne des réponses longues et détaillées'`

Ainsi, `conversationArr` avec l'objet d'instruction ressemble à ceci.

```js
const conversationArr = [
	{ 
        role: 'system',
        content: 'Vous êtes un assistant utile.' // ceci est l'instruction
    }
]

```

Et comme l'objet d'instruction ne changera pas, codons-le en dur et mettons-le dans `index.js`.

Jusqu'à présent, notre code ressemble à ceci :

<iframe src="https://scrimba.com/scrim/co8dc4d75b48980490dba860e" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

Avant de continuer, examinons les deux autres types d'objets que vous allez stocker dans `conversationArr`. Et juste pour être clair, vous ne allez pas les coder en dur dans `index.js` maintenant, mais les ajouter de manière programmatique selon les besoins.

Lorsque l'utilisateur soumet un texte, ce texte sera stocké dans un objet dans `conversationArr` et il ressemblera à ceci, avec le `role` étant `'user'` et le `content` étant le texte que l'utilisateur a soumis.

```js
{ 
    role: 'user',
    content: 'Quelle est la capitale de la France ?' // votre question
}

```

Et la réponse de l'API sera également stockée dans un objet. Ici, le rôle sera `'assistant'` et le `content` sera le texte de complétion, par exemple :

```js
{ 
    role: 'assistant',
    content: 'La capitale de la France est Paris.' // la complétion
}

```

Tous les objets qui finissent dans `conversationArr` à mesure qu'il grandit suivront ce même modèle, avec les propriétés `role` et `content`.

Alors maintenant, traitons ce qui se passe lorsque l'utilisateur tape un texte et appuie sur le bouton de soumission.

## Comment gérer l'entrée de l'utilisateur

Votre prochaine tâche est de prendre l'entrée de l'utilisateur et de la rendre dans le DOM. La div qui contient la conversation dans `index.html` a l'id `chatbot-conversation`. Donc dans `index.js`, prenez le contrôle de cette div et enregistrez-la dans une const `chatbotConversation`.

```js
const chatbotConversation = document.getElementById('chatbot-conversation')

```

Et maintenant, vous devez ajouter un écouteur d'événement qui se déclenche lorsqu'un utilisateur soumet un texte. Un autre rapide coup d'œil à index.html confirme que le bouton est à l'intérieur d'un élément de formulaire :

```js
<form id="form" class="chatbot-input-container">
    <input name="user-input" type="text" id="user-input" required>
        <button id="submit-btn" class="submit-btn">
            <img 
            src="images/send-btn-icon.png" 
            class="send-btn-icon"
            >
    </button>
</form>

```

Donc, cliquer sur le bouton ou appuyer sur entrer déclenchera un événement `submit`. C'est ce que vous devez que l'écouteur d'événement écoute. Et comme vous voulez empêcher le navigateur de recharger avec une chaîne de requête dans l'URL, vous devez ajouter `e.preventDefault()`.

```js
document.addEventListener('submit', (e) => {
    e.preventDefault()
})

```

### Rendre le message de l'utilisateur

Lorsque l'utilisateur soumet un message, vous devez le rendre. Il y a cinq étapes à ce processus :

1. Prenez le contrôle du champ de saisie de texte, qui a l'id `user-input`.
2. Utilisez `createElement` pour créer une nouvelle div.
3. Ajoutez les classes CSS dont la div a besoin : `speech` qui est la classe générique de bulle de dialogue, et `speech-human` qui applique des styles qui différencient la bulle de dialogue humaine de la bulle de dialogue IA.
4. Ajoutez cette bulle de dialogue à `chatbotConversation`.
5. Définissez le `textContent` de la bulle de dialogue sur l'entrée de l'utilisateur, que vous pouvez obtenir à partir de `userInput.value`.

```js
document.addEventListener('submit', (e) => {
    e.preventDefault()
	// 1. prenez le contrôle du champ de saisie de texte
    const userInput = document.getElementById('user-input')  
	// 2. créez le nouvel élément
    const newSpeechBubble = document.createElement('div')
    // 3. donnez-lui des classes CSS
	newSpeechBubble.classList.add('speech', 'speech-human')
	// 4. ajoutez la bulle de dialogue à la conversation
    chatbotConversation.appendChild(newSpeechBubble)
	// 5. ajoutez le texte saisi par l'utilisateur à la bulle de dialogue
    newSpeechBubble.textContent = userInput.value
})

```

### Mettre à jour `conversationArr` avec l'entrée de l'utilisateur

Après avoir rendu le message dans le DOM, vous devez maintenant pousser un objet à `conversationArr` dans le format que nous avons vu précédemment. Cet objet aura un `role` de `'user'` et la propriété `content` contiendra ce que l'utilisateur a tapé dans le champ de saisie de texte.

```js
document.addEventListener('submit', (e) => {
    e.preventDefault()

	const userInput = document.getElementById('user-input')  
    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-human')
    chatbotConversation.appendChild(newSpeechBubble)
    newSpeechBubble.textContent = userInput.value
		
    // poussez l'objet à conversationArr
    conversationArr.push({ 
        role: 'user',
        content: userInput.value
    })

})

```

### Effacer le champ de saisie et faire défiler vers le bas

Il y a deux dernières tâches que la fonction de cet écouteur d'événement doit accomplir. 

Tout d'abord, effaçons le champ de saisie de texte en le définissant sur une chaîne vide. Et deuxièmement, faisons défiler la conversation vers le bas afin que l'utilisateur n'ait pas à faire défiler manuellement vers le bas. Vous pourriez utiliser la méthode `scrollIntoView` pour cela, mais comme je l'ai codé pour un mini navigateur et que `scrollIntoView` causait des problèmes, j'ai utilisé une technique légèrement différente comme montré ci-dessous :

```js
document.addEventListener('submit', (e) => {
    e.preventDefault()

	const userInput = document.getElementById('user-input')  
    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-human')
    chatbotConversation.appendChild(newSpeechBubble)
    newSpeechBubble.textContent = userInput.value
		
	conversationArr.push({ 
        role: 'user',
        content: userInput.value
    })

	// videz le champ de saisie de texte
    userInput.value = ''
	// faites défiler la conversation vers le bas
    chatbotConversation.scrollTop = chatbotConversation.scrollHeight
})

```

Donc, notre code jusqu'à présent ressemble à ceci :

<iframe src="https://scrimba.com/scrim/co5a74d69b0ff18ce5551c4df" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

Maintenant, si vous posez la question _Quelle est la capitale de la France ?_ et affichez `conversationArr` depuis la fonction de l'écouteur d'événement, vous obtenez ceci :

```js
console.log(conversationArr)
//[{role: "system", content: "Vous êtes un assistant utile."}, {role: "user", content: "Quelle est la capitale de la France ?"}]

```

## C'est l'heure de l'IA

Il est temps d'utiliser l'API OpenAI pour générer du texte. La dépendance rend cette API très facile à utiliser – vous avez juste besoin de trois informations.

1. Un endpoint
2. Un modèle
3. Notre conversation dans un tableau

Vous avez déjà configuré `conversationArr` pour traiter le numéro 3 de cette liste, mais avant de faire une requête à l'API, examinons les points 1 et 2 plus en détail.

### Endpoints

L'API OpenAI propose divers endpoints disponibles. Celui que vous utilisez dépend de ce que vous voulez que l'IA fasse (générer du langage, générer du code, créer des images à partir de prompts textuels, etc.). 

Pour ce chatbot, nous utiliserons l'endpoint `chat/completion`, qui, au moment de la rédaction, est l'endpoint le plus avancé pour la génération de langage naturel dans l'écosystème OpenAI.

### Modèles

Le modèle (parfois appelé le moteur) est ce qui crée réellement le langage. Notre modèle pour ce projet est `GPT-4`. `GPT-4` est en version limitée via une [liste d'attente](https://openai.com/waitlist/gpt-4-api) pour le moment, donc si vous ne pouvez pas y accéder maintenant, vous pouvez utiliser `GPT-3.5-turbo` à la place. Tout le code de ce projet fonctionne avec les deux modèles, et `GPT-3.5-turbo` est également très capable.

OK, faisons un appel à l'API.

### La fonction fetchReply

Nous avons besoin d'une fonction pour prendre en charge la tâche de faire une requête à l'API. Appelons cette fonction `fetchReply`. Les bases de la fonction ressemblent à ceci :

```js
async function fetchReply(){
    const response = await openai.createChatCompletion() 
}

```

À l'intérieur du corps de la fonction, nous avons une const `response` et nous avons attendu un appel à l'endpoint `chat/completion` que vous pouvez atteindre en prenant l'instance du constructeur `OpenAiAPI` que vous avez stockée dans la const `openai` précédemment et en appelant la méthode `createChatCompletion` sur celle-ci. (`createChatCompletion` est une méthode de l'API OpenAI qui nous donne accès à l'endpoint `chat/completion`. Pour plus d'informations, consultez la [documentation de l'API OpenAI](https://platform.openai.com/docs/api-reference).)

Parce que la dépendance fait une requête fetch, vous devez utiliser le mot-clé `await` et faire de cela une fonction `async`.

Ensuite, vous devez passer `createChatCompletion` un objet, et cet objet a besoin de deux propriétés : `model` et `messages`.

### Modèle

Notre modèle est GPT-4. Vous pouvez le spécifier en le mettant dans une chaîne en minuscules dans une paire clé/valeur : `model: 'gpt-4'`. C'est ici que vous pourriez également utiliser `model: 'gpt-3.5-turbo'` si vous n'avez pas encore accès à GPT-4.

### Messages

La propriété messages doit simplement contenir notre conversation, que vous avez stockée sous forme de tableau d'objets dans la const `conversationArr`.

Pour l'instant, affichez la réponse. Donc le code final ressemble à ceci :

```js
async function fetchReply(){
    const response = await openai.createChatCompletion({
        model: 'gpt-4', // ou 'gpt-3.5-turbo'
        messages: conversationArr,
    })
	console.log(response)
} 

```

Maintenant, appelez fetchReply depuis la fonction de l'écouteur d'événement.

```js
document.addEventListener('submit', (e) => {
    e.preventDefault()
    const userInput = document.getElementById('user-input')   
    conversationArr.push({ 
        role: 'user',
        content: userInput.value
    })
    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-human')
    chatbotConversation.appendChild(newSpeechBubble)
    newSpeechBubble.textContent = userInput.value
    userInput.value = ''
    chatbotConversation.scrollTop = chatbotConversation.scrollHeight
    console.log(conversationArr)

	// appelez fetch reply pour déclencher l'appel API
	fetchReply()
})


```

![Chatbot avec une question de l'utilisateur.](https://www.freecodecamp.org/news/content/images/2023/06/image-181.png)
_Chatbot avec une question de l'utilisateur._

Et lorsque vous tapez _Quelle est la capitale de la France ?_ et appuyez sur envoyer, vous obtenez cet objet massif : (N'hésitez pas à le parcourir, mais ne soyez pas intimidé !)

```js
{data: {id: "chatcmpl-7MuziItZYyiFpPG2KHQawd19rD54U", object: "chat.completion", created: 1685696658, model: "gpt-4-0314", usage: {prompt_tokens: 28, completion_tokens: 36, total_tokens: 64}, choices: [{message: {role: "assistant", content: "La capitale de la France est Paris."}, finish_reason: "stop", index: 0}]}, status: 200, statusText: "", headers: {cache-control: "no-cache, must-revalidate", content-type: "application/json"}, config: {transitional: {silentJSONParsing: true, forcedJSONParsing: true, clarifyTimeoutError: false}, adapter: xhrAdapter(e), transformRequest: [transformRequest(e,t)], transformResponse: [transformResponse(e)], timeout: 0, xsrfCookieName: "XSRF-TOKEN", xsrfHeaderName: "X-XSRF-TOKEN", maxContentLength: -1, maxBodyLength: -1, validateStatus: validateStatus(e), headers: {Accept: "application/json, text/plain, */*", Content-Type: "application/json", User-Agent: "OpenAI/NodeJS/3.2.1", Authorization: "Bearer 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"}, method: "post", data: "{"model":"gpt-4","messages":[{"role":"system","content":"Vous êtes un assistant très compétent qui est toujours heureux d'aider."},{"role":"user","content":"Quelle est la capitale de la France ?"}]}", url: "https://api.openai.com/v1/chat/completions"}, request: XMLHttpRequest {}}
```

Il y a beaucoup d'informations utiles ici, mais nous devons nous concentrer sur cette partie, que j'ai formatée pour une meilleure lisibilité :

```js
choices: [
    {
        message: {
            role: "assistant", 
            content: "La capitale de la France est Paris."
        }, 
        finish_reason: "stop", index: 0
    }
]

```

C'est ici que nous pouvons voir la complétion : _La capitale de la France est Paris._ Et c'est ce que vous devez rendre dans le DOM dans une bulle de dialogue. Et vous pouvez utiliser la notation par points et crochets pour accéder à ce texte.

Affichez cela.

```js
console.log(response.data.choices[0].message.content)
//La capitale de la France est Paris.

```

Mais avant de rendre quoi que ce soit, souvenez-vous que vous devez également inclure chaque morceau de dialogue dans `conversationArr`. Et le format dont vous avez besoin pour cela est un objet avec deux paires clé/valeur où une clé est `role` et a la valeur `'assistant'`, et l'autre est `content` et contient la complétion comme valeur.  

Et cet objet est exactement ce qui vous est donné dans `response.data.choices[0].message` – oui, l'objet que vous devez ajouter à `conversationArr` est en fait fourni par l'API !

Vous pouvez ajuster le `console.log` ci-dessus pour le prouver :

```js
console.log(response.data.choices[0].message)
//{role: "assistant", content: "La capitale de la France est Paris."}

```

Maintenant, vous pouvez faire en sorte que `fetchReply` pousse cet objet vers `conversationArr`.

Et affichons `conversationArr` pour vérifier que cela fonctionne :

```js
async function fetchReply(){
    const response = await openai.createChatCompletion({
        model: 'gpt-4',
        messages: conversationArr,
    })
    conversationArr.push(response.data.choices[0].message)
	console.log(conversationArr)
}

// [{role: "system", content: "Vous êtes un assistant utile."}, {role: "user", content: "Quelle est la capitale de la France ?"}, {role: "assistant", content: "La capitale de la France est Paris."}]

```

Le code du projet devrait maintenant ressembler à ceci :

<iframe src="https://scrimba.com/scrim/co5f9419c95e33d38a87a200c" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

Maintenant, il ne reste plus qu'à rendre la complétion.

## Comment implémenter l'effet machine à écrire

La dernière tâche consiste à faire en sorte que notre chatBot tape sa réponse. Il existe des milliers de façons de faire cela, et il est possible de le faire uniquement avec CSS. Nous allons le faire avec JavaScript.

Créez une fonction appelée `renderTypewriterText`. Cette fonction prendra un paramètre qui sera la chaîne de texte que vous obtenez de la réponse. 

La fonction `renderTypewriterText` doit créer un nouvel élément de bulle de dialogue, lui donner des classes CSS et l'ajouter à `chatbotConversation`. Cela ressemble presque au même code que vous avez utilisé précédemment pour l'entrée de l'utilisateur, mais notez ici que vous devrez également donner à la bulle de dialogue la classe `blinking-cursor`, qui utilise une animation CSS pour créer un effet de curseur pendant que le texte est rendu. Voir `index.css` lignes 151 et suivantes dans le scrim ci-dessus pour le CSS.

```js
function renderTypewriterText(text) {
    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-ai', 'blinking-cursor')
    chatbotConversation.appendChild(newSpeechBubble)
}

```

Ajoutez maintenant une logique pour rendre chaque caractère un par un :

```js
function renderTypewriterText(text) {
    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-ai', 'blinking-cursor')
    chatbotConversation.appendChild(newSpeechBubble)
    
	// rendre chaque caractère un par un 
    let i = 0
    const interval = setInterval(() => {
        newSpeechBubble.textContent += text.slice(i-1, i)
        if (text.length === i) {
            clearInterval(interval)
            newSpeechBubble.classList.remove('blinking-cursor')
        }
        i++
        chatbotConversation.scrollTop = chatbotConversation.scrollHeight
    }, 50)
}

```

C'est un peu un mélange de JavaScript, alors passons-le en revue étape par étape.

1. `let i = 0` : Cela initialise une variable `i` avec une valeur de 0. Elle sera utilisée pour suivre l'index actuel de la chaîne de texte `text`.
2. `const interval = setInterval(() => { ... }, 50)` : Cela crée un intervalle qui exécute la fonction fléchée toutes les 50 millisecondes. La fonction fléchée contient le code qui sera exécuté à chaque intervalle.
3. `newSpeechBubble.textContent += text.slice(i-1, i)` : Cette ligne ajoute une portion de la chaîne de texte `text` au contenu de l'élément `newSpeechBubble`. Elle utilise la méthode `slice` pour extraire un seul caractère de la chaîne de texte `text` en fonction de la valeur actuelle de `i`.
4. `if (text.length === i) { ... }` : Cette condition vérifie si toute la chaîne de texte `text` a été ajoutée à la bulle de dialogue. Si la longueur de la chaîne de texte `text` est égale à `i`, cela signifie que tous les caractères ont été ajoutés.
5. `clearInterval(interval)` : Cette ligne efface l'intervalle, arrêtant l'exécution de la fonction.
6. `newSpeechBubble.classList.remove('blinking-cursor')` : Cela supprime la classe CSS `'blinking-cursor'` de l'élément `newSpeechBubble`. Elle supprime l'effet de curseur clignotant une fois que toute la chaîne de texte `text` a été affichée. Vous ne voulez le curseur clignotant que pendant que la machine à écrire est en cours d'exécution.
7. `i++` : Cela incrémente la valeur de `i` de 1, passant au caractère suivant dans la chaîne de texte `text` pour l'exécution de l'intervalle suivant.
8. `chatbotConversation.scrollTop = chatbotConversation.scrollHeight` : Cela fait défiler le conteneur de conversation vers le bas, garantissant que le nouveau contenu est toujours visible.

Pour terminer le câblage, appelez `renderTypewriterText` depuis fetchReply, en n'oubliant pas de passer le texte de complétion qui revient de l'API.

```js
async function fetchReply(){
	const response = await openai.createChatCompletion({
        model: 'gpt-4',
        messages: conversationArr,
    }) 
    conversationArr.push(response.data.choices[0].message)

	// appelez renderTypewriterText en passant la complétion
    renderTypewriterText(response.data.choices[0].message.content)
}

```

Et vous avez terminé !

![L'application terminée avec une conversation entre un utilisateur et le chatbot IA](https://www.freecodecamp.org/news/content/images/2023/06/image-182.png)
_L'application terminée avec une conversation entre un utilisateur et le chatbot IA_

Nous avons maintenant un chatbot entièrement fonctionnel utilisant l'API GPT-4 et vous pouvez continuer la conversation aussi longtemps que vous le souhaitez ! 

Eh bien, ce n'est pas tout à fait vrai. Il y a une limite théorique à la durée de la conversation, mais vous devriez continuer à discuter pendant longtemps pour l'atteindre. Nous en parlons plus dans le cours complet. De plus, il est important de noter qu'à un moment donné, vous pourriez atteindre votre limite de crédit.

Voici le code final. Et comme avant, vous pouvez cliquer sur l'icône d'engrenage ⚙️ et le télécharger.

<iframe src="https://scrimba.com/scrim/co6f54980a423391dcd15fe81" title="scrim mis à jour montrant le code du projet jusqu'à présent." style="width: 100%; height: 400px"></iframe>

## Conclusion

Félicitations pour avoir réussi à construire votre propre chatbot en utilisant l'API GPT-4 ! Avec GPT-4, vous avez débloqué un monde de possibilités dans le traitement du langage naturel et la génération de conversations. 

Alors que vous continuez votre voyage dans l'IA, n'oubliez pas de rester curieux, de continuer à apprendre et d'explorer le domaine en évolution de l'intelligence artificielle. Partagez vos créations, collaborez avec les autres et faites partie de la communauté de l'IA. Bon codage !

N'hésitez jamais à me contacter sur Twitter. Je suis [@tpchant](https://twitter.com/Tpchant).