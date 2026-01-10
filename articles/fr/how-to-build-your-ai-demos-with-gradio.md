---
title: Comment créer vos démos d'IA avec Gradio
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-28T00:17:49.050Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-ai-demos-with-gradio
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756337736951/2a58e22d-dd7a-4768-b052-a981a91c36da.png
tags:
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
- name: deployment
  slug: deployment
seo_title: Comment créer vos démos d'IA avec Gradio
seo_desc: 'The world of artificial intelligence moves fast. Every week, new models
  appear, older ones get better, and the tools to use them become easier.

  But if you are building a machine learning project, you may face one big problem:
  how to share your work q...'
---

Le monde de l'intelligence artificielle évolue rapidement. Chaque semaine, de nouveaux modèles apparaissent, les plus anciens s'améliorent et les outils pour les utiliser deviennent plus simples.

Mais si vous construisez un projet de Machine Learning, vous pouvez être confronté à un problème majeur : comment partager votre travail rapidement pour que d'autres puissent l'essayer.

Un notebook rempli de code n'est pas toujours suffisant. Les gens veulent interagir avec votre modèle. Ils veulent voir des entrées, cliquer sur des boutons et voir les résultats apparaître instantanément.

C'est là qu'intervient [**Gradio**](https://www.gradio.app/). Avec seulement quelques lignes de Python, vous pouvez transformer votre modèle d'IA en une application web simple. Vous n'avez pas besoin de connaître le HTML, le CSS ou le JavaScript, Gradio s'occupe de l'interface pour que vous puissiez vous concentrer sur votre modèle.

Dans ce tutoriel, vous apprendrez à construire des démos d'IA en quelques minutes en utilisant Gradio. À la fin, vous aurez une démo en direct prête à être testée par n'importe qui.

## Table des matières

* [Qu'est-ce que Gradio ?](#heading-qu-est-ce-que-gradio)
    
* [Pourquoi utiliser Gradio ?](#heading-pourquoi-utiliser-gradio)
    
* [Votre première application Gradio](#heading-votre-premiere-application-gradio)
    
* [Comment ajouter des modèles de Machine Learning](#heading-comment-ajouter-des-modeles-de-machine-learning)
    
* [Comment personnaliser l'interface](#heading-comment-personnaliser-l-interface)
    
* [Comment partager votre application](#heading-comment-partager-votre-application)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Gradio ?

Gradio est une bibliothèque Python open-source qui facilite la création d'interfaces web interactives pour les modèles de Machine Learning.

Imaginez que vous avez entraîné un résumeur de texte ou un classificateur d'images. Sans Gradio, vous devriez construire un frontend, écrire du code backend, l'héberger quelque part, puis tout connecter ensemble. Cela prend du temps et des efforts.

Avec Gradio, vous écrivez quelques lignes de Python, et cela vous donne un lien partageable avec une UI complète. L'interface fonctionne sur n'importe quel appareil doté d'un navigateur. Vous pouvez même l'intégrer dans des sites web ou la partager avec vos coéquipiers pour obtenir leurs retours.

Gradio prend en charge le texte, les images, l'audio, la vidéo et de nombreux autres types de données. Cela le rend parfait pour la vision par ordinateur, le traitement du langage naturel (NLP), la reconnaissance vocale ou toute autre application d'IA.

## Pourquoi utiliser Gradio ?

La vitesse est une raison majeure de choisir Gradio. Construire une application web pour votre modèle peut prendre des heures, voire des jours, si vous le faites de zéro. Gradio réduit cela à quelques minutes. Vous vous concentrez sur votre modèle d'IA tandis que Gradio gère l'interface utilisateur.

Il est également facile à utiliser. Même les débutants ayant des connaissances de base en Python peuvent créer des démos fonctionnelles. Il fonctionne bien avec des bibliothèques populaires comme TensorFlow, PyTorch et [Hugging Face Transformers](https://www.turingtalks.ai/p/hugging-face-s-transformer-library-a-game-changer-in-nlp).

Un autre avantage est le partage. Lorsque vous lancez une application Gradio, vous obtenez un lien public que n'importe qui peut ouvrir. Vous n'avez pas besoin de le déployer manuellement ou de configurer des serveurs. Cela le rend parfait pour les hackathons, les prototypes rapides ou l'envoi de démos à des clients et amis.

#### Comment installer Gradio

Avant de construire votre première application, vous devez installer Gradio. Ouvrez votre terminal ou votre invite de commande et tapez :

```plaintext
pip install gradio
```

C'est tout. L'installation est rapide et prend généralement moins d'une minute. Une fois terminé, vous êtes prêt à construire votre première démo.

## Votre première application Gradio

Commençons simplement. Imaginez que vous vouliez construire une application d'inversion de texte. L'utilisateur tape une phrase, et l'application affiche la version inversée. Ce n'est peut-être pas un vrai modèle d'IA, mais cela vous aide à apprendre les bases.

Voici le code :

```plaintext
# Import the Gradio library
import gradio as gr

# Define a function that reverses any input text
def reverse_text(text):
    # The [::-1] slice notation reverses the string
    return text[::-1]

# Create a Gradio interface to connect the function with a simple web UI
demo = gr.Interface(
    fn=reverse_text,       # Function to call when the user submits input
    inputs="text",         # Type of input (a text box for user input)
    outputs="text",        # Type of output (a text box to display reversed text)
    title="Text Reversal App",          # Title displayed on the app
    description="Type any text and see it reversed instantly."  # Short description for users
)

# Launch the web app in the browser
demo.launch()
```

`gr.Interface()` lie votre fonction Python à une interface utilisateur web. `fn=reverse_text` indique à Gradio d'appeler cette fonction chaque fois que l'utilisateur fournit une entrée.

`inputs="text"` spécifie que le champ de saisie doit être une zone de texte. `outputs="text"` permet d'afficher la sortie sous forme de texte.

`title` et `description` améliorent l'apparence de l'application avec un titre et une explication.

Enregistrez ceci dans un fichier Python et exécutez-le. Une fenêtre de navigateur s'ouvrira avec une zone de texte. Tapez quelque chose, cliquez sur "submit", et vous verrez le texte inversé apparaître.

![Gradio Result](https://cdn.hashnode.com/res/hashnode/image/upload/v1756100382572/5fdc0ace-b9ab-43a5-943b-1174670e7cd1.png align="center")

Félicitations ! Vous venez de construire votre première application interactive avec Gradio en moins de cinq minutes.

## Comment ajouter des modèles de Machine Learning

Maintenant, construisons quelque chose de plus excitant. Supposons que vous ayez un modèle d'[analyse de sentiment](https://www.freecodecamp.org/news/how-to-build-a-simple-sentiment-analyzer-using-hugging-face-transformer/) qui prend du texte et prédit s'il est positif, négatif ou neutre. Vous pouvez le connecter facilement à Gradio.

Voici un exemple utilisant Hugging Face Transformers :

```plaintext
# Import the Gradio library
import gradio as gr

# Import the 'pipeline' function from Hugging Face's Transformers library
# 'pipeline' lets you load pre-trained AI models with a single line of code
from transformers import pipeline

# Load a pre-trained sentiment analysis model from Hugging Face
# This model can classify text as POSITIVE, NEGATIVE, or NEUTRAL along with a confidence score
sentiment_model = pipeline("sentiment-analysis")

# Define a function that uses the model to analyze text sentiment
def analyze_sentiment(text):
    # Pass the user-provided text to the model
    # The model returns a list of predictions; we take the first one using [0]
    result = sentiment_model(text)[0]
    
    # Return the label (e.g., POSITIVE) and the confidence score formatted to 2 decimal places
    return f"Label: {result['label']}, Score: {result['score']:.2f}"

# Create a Gradio interface to turn the function into a web app
demo = gr.Interface(
    fn=analyze_sentiment,         # The function to call when user inputs text
    inputs="text",                # The input type (a single-line text box)
    outputs="text",               # The output type (display as text)
    title="Sentiment Analysis App",    # Title shown at the top of the web app
    description="Type a sentence to check its sentiment."  # Short explanation for the app
)

# Launch the web app so users can interact with it in a browser
demo.launch()
```

Exécutez ce code, tapez "I love this product!" et regardez le modèle renvoyer "Label: POSITIVE" avec un score de confiance.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756100423148/15899f62-f962-488e-8dba-df9809ad56c1.png align="center")

## Comment personnaliser l'interface

Gradio vous donne le contrôle sur les titres, les descriptions, les thèmes et même les exemples. Par exemple, vous pouvez ajouter des exemples d'entrées comme ceci :

```plaintext
demo = gr.Interface(fn=analyze_sentiment, 
                    inputs="text", 
                    outputs="text",
                    title="Sentiment Analysis App",
                    description="Type a sentence to check its sentiment.",
                    examples=[["I love AI"], ["I hate waiting"]])
```

Désormais, l'application affiche des phrases d'exemple sur lesquelles les utilisateurs peuvent cliquer pour tester instantanément.

![Gradio demo with examples](https://cdn.hashnode.com/res/hashnode/image/upload/v1756100452336/6f8ee1d4-bcb1-4719-bbeb-74401f7d8990.png align="center")

## Comment partager votre application

Lorsque vous exécutez `demo.launch()`, Gradio démarre un serveur local et vous donne un lien local. Pour obtenir un lien partageable, utilisez `demo.launch(share=True)` et vous obtiendrez un lien public que vous pourrez partager avec d'autres.

![Public url for sharing demos](https://cdn.hashnode.com/res/hashnode/image/upload/v1756100477123/2b5fbb37-cbda-46e4-be5a-18422b9c6f78.png align="center")

Le lien public fonctionne pendant 72 heures par défaut. Si vous souhaitez un lien permanent, vous pouvez déployer sur Hugging Face Spaces gratuitement ou utiliser des plateformes comme AWS.

## Conclusion

Gradio change la façon dont les développeurs partagent les modèles de Machine Learning. Ce qui prenait autrefois des heures de codage ne prend plus que quelques minutes. Vous écrivez le code du modèle, vous le connectez à Gradio et vous obtenez instantanément une démo fonctionnelle avec un lien partageable.

Que vous soyez un étudiant apprenant l'IA, un chercheur partageant ses résultats ou un développeur créant des prototypes, Gradio vous fait gagner du temps et des efforts. Il élimine la complexité du développement web pour que vous puissiez vous concentrer sur ce qui compte : construire votre modèle d'IA.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite sur l'IA* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également me trouver sur* [***Linkedin***](https://www.linkedin.com/in/manishmshiva)***.***