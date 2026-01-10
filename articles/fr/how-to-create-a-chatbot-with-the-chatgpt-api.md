---
title: Comment créer un chatbot avec l'API ChatGPT
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2023-07-26T15:48:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-chatbot-with-the-chatgpt-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/levart_photographer-drwpcjkvxuU-unsplash--1-.jpg
tags:
- name: '#chatbots'
  slug: chatbots
- name: chatgpt
  slug: chatgpt
- name: Node.js
  slug: nodejs
seo_title: Comment créer un chatbot avec l'API ChatGPT
seo_desc: 'OpenAI''s ChatGPT is a great tool for getting information as quickly as
  possible for your coding projects. Even better, you can now integrate the artificial
  intelligence-powered chat capability of OpenAI''s models directly into your application.

  Recent...'
---

ChatGPT d'OpenAI est un excellent outil pour obtenir des informations aussi rapidement que possible pour vos projets de codage. Mieux encore, vous pouvez désormais intégrer directement la capacité de chat alimentée par l'intelligence artificielle des modèles d'OpenAI dans votre application.

Récemment, l'équipe d'OpenAI a élargi leur API en donnant aux développeurs accès à leurs modèles d'IA pré-entraînés (DALL-E, Codex et GPT-3). Cela signifie que vous pouvez envoyer une question à l'API, obtenir la réponse et utiliser les données dans votre application, le tout en quelques secondes.

Dans cet article, vous apprendrez comment créer un compte OpenAI, récupérer vos clés API et interroger le modèle GPT-3 d'OpenAI depuis votre application Node.js. Commençons tout de suite !

## **Comment s'inscrire à un compte ChatGPT**

La première chose à faire est de s'inscrire à un [compte OpenAI](https://platform.openai.com/overview) si vous n'en avez pas déjà un. Une fois inscrit, vous serez redirigé vers la page d'accueil.

Dans le coin supérieur droit de la page, cliquez sur votre image de profil, puis cliquez sur Gérer le compte. Dans la barre latérale, cliquez sur Clés API, puis cliquez sur le bouton **créer une nouvelle clé secrète** pour générer une clé secrète :

![Screenshot_of_OpenAI_API_key](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot_of_OpenAI_API_key.jpg align="left")

*Capture d'écran de la clé secrète*

Copiez la clé secrète et collez-la dans un endroit sûr et accessible, car vous en aurez besoin plus tard pour connecter votre application à l'API OpenAI.

Avec la clé stockée en sécurité, l'étape suivante consiste à créer un projet Node.js et à lancer un serveur Express par-dessus. Commençons par l'installation et la configuration de base.

## **Comment configurer le projet**

Pour suivre ce projet, vous devez avoir Node.js et npm installés sur votre machine locale. La dernière version de Node.js inclut npm, et elle est disponible sur le [site officiel de Node.js](https://nodejs.org/en/download).

Commencez par créer un répertoire vide sur votre ordinateur. Ensuite, lancez l'invite de commande et utilisez `cd` pour accéder au dossier que vous venez de créer :

```bash
cd chemin/vers/projet
```

Une fois dans le répertoire, exécutez la commande suivante pour créer un projet Node :

```bash
npm init -y
```

Ensuite, exécutez la commande suivante pour installer les bibliothèques `express` et `openai` depuis npm :

```bash
npm i express openai
```

L'étape suivante consiste à créer le serveur.

## **Comment créer un serveur Express**

Pour l'instant, ce serveur ne servira que les fichiers statiques. Nous implémenterons l'API de chat à la fin de cet article.

Commencez par créer un fichier nommé **server.js** à la racine de votre projet. Ensuite, ouvrez le fichier avec un éditeur de code et ajoutez le code suivant :

```javascript
const express =  require('express')
const app = express()

app.use(express.static('public'))

app.listen(5000, ()=> {
    console.log("Le serveur est actif")
})
```

Avec ce code, vous avez créé un serveur web qui sert des fichiers statiques (c'est-à-dire HTML, CSS) depuis le dossier **/public**.

Ensuite, nous allons créer le fichier HTML qui affiche l'interface de chat sur la page web, ainsi que le fichier de feuille de style et le fichier JavaScript.

## **Comment créer le chatbot**

Commencez par créer un dossier nommé public à la racine de votre projet. Ensuite, à l'intérieur du répertoire **/public**, créez un fichier nommé **index.html**.

Ouvrez le fichier avec un éditeur de texte et ajoutez le balisage suivant dans le fichier :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="chat-area">

    </div>

    <div class="submit-form">
        <div class="input">
            <textarea name="input" id="input" cols="40" rows="3"></textarea>
            <button id="btn">Envoyer</button>
        </div>    
    </div>    
 
</body>
</html>
```

Comme vous pouvez le voir ci-dessus, la page se compose de la zone de chat (où les messages sont affichés) et de la zone de soumission (comprenant la zone de texte et le bouton de soumission).

Pour styliser la page, ajoutez la feuille de style suivante entre les balises `<head>` d'ouverture et de fermeture dans votre fichier **/public/index.html** :

```html
    <style>
        #chat-area {
            margin: 0 auto;
            width: 80%;
            height: 500px;
            overflow:scroll;
            border: 1px solid gray;
            border-radius: 4px;
        }

        .input {            
            width: 100%;
        }

        .submit-area{
            justify-content: center;
            display: flex;
            margin: 20px auto;
            width: 80%;            
        }       

        textarea {
            width: 100%;
        }

        .box {
            width: 96%;
            margin: 0 auto;
            padding: 10px 10px;
            background-color: #C4DBFE;
            margin: 10px auto;            
        }

        .answer {
            background-color: aquamarine;
        }

        button {
            background-color: #004089;
            color: white;
            padding: 10px 10px;
            border-radius: 5px;
            border: none;
        }
    </style>
```

Si vous enregistrez le fichier et vérifiez dans le navigateur, vous devriez voir votre page comme ceci :

![Document--1-](https://www.freecodecamp.org/news/content/images/2023/07/Document--1-.png align="left")

*Capture d'écran de la page*

La zone de chat est vide pour l'instant car nous n'avons encore soumis aucun message. Pour cela, nous devons intégrer JavaScript.

## **Comment ajouter JavaScript côté client**

Lorsque l'utilisateur saisit un message dans la zone de texte et clique sur le bouton de soumission, nous allons envoyer le message au backend, obtenir la réponse de l'API et l'afficher sur la page.

Commencez par ajouter un élément de script vide dans les balises `<body>` dans **index.html** :

```html
<script>

</script>
```

À l'intérieur des balises de script, nous allons appeler la fonction `getResponse()` chaque fois que l'utilisateur clique sur le bouton de soumission :

```javascript
const btn = document.getElementById("btn")

btn.addEventListener('click', getResponse)
```

La fonction `getResponse` obtient essentiellement la question de l'utilisateur, l'envoie à notre backend Node.js pour récupérer la réponse et affiche la réponse sur la page.

À l'intérieur de la fonction, nous commençons par accéder à l'invite soumise par l'utilisateur :

```javascript
async function getResponse() {                  
  var inputText = document.getElementById("input").value           
  const parentDiv = document.getElementById("chat-area") 
  
  // Le reste du code va à l'intérieur de cette fonction
}
```

Si la valeur de la zone de texte est vide, nous ne retournons simplement rien :

```javascript
if(inputText === '') { return }
```

Sinon, nous ajoutons d'abord la question à la zone de chat dans l'interface utilisateur :

```javascript
const question = document.createElement('div')
question.innerHTML = inputText
question.classList.add("box")
parentDiv.appendChild(question)
```

Ensuite, nous réinitialisons la zone de texte pour qu'elle soit vide :

```javascript
document.getElementById("input").value = ''
```

Puis nous envoyons la question à notre serveur afin que le serveur puisse l'envoyer à l'API OpenAI et nous renvoyer une réponse :

```javascript
let res = await fetch('http://localhost:5000/chat', 
  {
    method: 'POST',
    headers: {
      "Content-Type": 'application/json'                
    },
    body: JSON.stringify({
      question: inputText          
    })
  }
)
    
const data = await res.json()
```

Si la réponse a une propriété `message`, nous ajoutons le contenu du message à la zone de chat dans l'interface utilisateur :

```javascript
if(data.message) {
  const answer = document.createElement('div')
  answer.innerHTML = data.message
  answer.classList.add("box", "answer")
  parentDiv.appendChild(answer)
}
```

Maintenant, le frontend est prêt. Revenons au backend.

## **Comment envoyer la réponse de l'API au client**

Notre backend servira d'intermédiaire entre le frontend et l'API d'OpenAI. En gros, nous allons obtenir l'invite du client, l'envoyer à l'API et renvoyer la réponse au client.

Dans **server.js**, importez ceci en haut du fichier :

```javascript
const { OpenAI } = require("openai")
```

Ensuite, créez une instance de la connexion `openai` en utilisant la clé API que vous avez générée précédemment :

```javascript
const openai = new OpenAI({
    // remplacez votre-clé-api par votre clé API de ChatGPT
    apiKey: 'votre-clé-api'
})
```

Enfin, créez la route :

```javascript
app.post('/chat', async (req, res)=> {   
  try {
    const resp = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
        messages: [
          { role: "user", content: req.body.question}
        ]  
    })           
        
    res.status(200).json({message: resp.choices[0].message.content})
  } catch(e) {
      res.status(400).json({message: e.message})
  }
})
```

Enregistrez les modifications du fichier, puis allez dans votre navigateur et soumettez une question. Vous devriez obtenir une réponse après quelques secondes.

Vous pouvez poser autant de questions que vous le souhaitez, mais vous devrez attendre une réponse à chaque question du backend.

![Document](https://www.freecodecamp.org/news/content/images/2023/07/Document.png align="left")

*Capture d'écran des questions et des réponses correspondantes de ChatGPT*

Si une erreur est rencontrée, vérifiez la console dans votre navigateur pour inspecter le message d'erreur.

## **Conclusion**

L'API d'OpenAI vous offre un moyen d'inclure des chatbots alimentés par l'IA dans votre application en utilisant JavaScript ou même [HTMX](https://letsusetech.com/the-awesome-things-you-can-do-with-htmx) (si vous connaissez le HTML mais pas JavaScript).

Connectez-vous avec moi sur [Twitter](https://twitter.com/kingchuuks) et [LinkedIn](https://www.linkedin.com/in/kingchuks/).