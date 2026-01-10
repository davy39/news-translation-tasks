---
title: Comment créer une application d'analyse de sentiment avec Blenderbot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-31T15:07:33.000Z'
originalURL: https://freecodecamp.org/news/build-a-sentiment-analayis-app-using-blenderbot
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/cover.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: Comment créer une application d'analyse de sentiment avec Blenderbot
seo_desc: 'By Edem Gold

  Turning machine learning models into actual applications other people can use is
  not something that is covered in most AI and Machine Learning Tutorials.

  In this article, we are going to create an end-to-end AI Sentiment Analysis web
  app...'
---

Par Edem Gold

Transformer les modèles de machine learning en applications réelles que d'autres personnes peuvent utiliser n'est pas quelque chose qui est couvert dans la plupart des tutoriels sur l'IA et le Machine Learning.

Dans cet article, nous allons créer une application web d'analyse de sentiment AI de bout en bout en utilisant Gradio et les transformateurs Hugging Face.

# Qu'est-ce que l'analyse de sentiment ?

![pic-1.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1635883449621/fWPS8d_c-.jpeg?auto=compress,format&format=webp)

Selon [Wikipedia](https://en.wikipedia.org/wiki/Sentiment_analysis),

> L'analyse de sentiment est l'utilisation du traitement du langage naturel, de l'analyse de texte, de la linguistique computationnelle et de la biométrie pour identifier, extraire, quantifier et étudier systématiquement les états affectifs et les informations subjectives.

En termes simples, l'analyse de sentiment est la capacité de l'intelligence artificielle à analyser une phrase ou un bloc de texte et à obtenir les émotions derrière cette phrase ou ce bloc de texte.

# Qu'est-ce que Gradio ?

![gradio-logo.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1635883565410/Oo46t3DPn.png?auto=compress,format&format=webp)

[Gradio est une bibliothèque Python open-source](https://gradio.app/) que vous pouvez utiliser pour créer et personnaliser rapidement des composants UI faciles à utiliser pour votre modèle ML, toute API, ou toute fonction arbitraire en quelques lignes de code.

Gradio facilite la création d'interfaces graphiques et le déploiement de modèles de machine learning.

# Qu'est-ce que Hugging Face ?

[Hugging Face](https://huggingface.co/) est une bibliothèque qui fournit des modèles et des ensembles de données de traitement du langage naturel pré-entraînés et open-source pour les ingénieurs en machine learning.

C'est une communauté open-source de Machine Learning où vous pouvez télécharger des modèles de machine learning pré-entraînés et les utiliser dans vos propres projets.

# Il est temps de construire notre projet

## **Prérequis**

* Avoir Python installé
* Avoir un IDE / éditeur de texte (comme [Visual Studio](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), ou [Jupyter Notebook](https://jupyter.org/) )
* Avoir une connexion internet

**Voici le [Dépôt GitHub](https://github.com/EdemGold/sentiment-analysis-app) pour le projet**.

## **Installer les dépendances**

Ici, nous allons installer les bibliothèques nécessaires pour construire l'application d'analyse de sentiment.

### Comment installer Transformers

Ici, nous allons installer la bibliothèque transformers. Cette bibliothèque nous donnera accès à l'API hugging face.

```
#Dans un notebook jupyter
!pip install transformers

#Dans le terminal
pip install transformers

```

### Comment installer PyTorch

Nous allons installer la bibliothèque de deep learning PyTorch. Visitez le [Site Web de PyTorch](https://pytorch.org/get-started/locally/) et installez votre version spécialisée.

![pytorch-install.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1635887110857/e_LVM9OR0.jpeg?auto=compress,format&format=webp)

Voici ma version installée de PyTorch.

```
#installer dans un notebook jupyter
!pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio===0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

#Installer dans le terminal
pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio===0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

```

### Importer et configurer le Pipeline

Ici, nous allons importer et configurer notre _modèle d'analyse de sentiment_ en utilisant un pipeline Hugging Face.

Hugging Face fournit un pipeline automatique qui aide à gérer des choses comme la tokenisation, le pré-traitement, l'encodage et le décodage pour vous et vous permet de vous concentrer sur des choses essentielles comme l'optimisation du modèle.

```
#configuration du pipeline hugging face
from transformers import pipeline
classifier = pipeline("sentiment-analysis")

```

Ci-dessus, nous avons importé et instancié l'objet pipeline, puis nous avons passé les modèles d'analyse de sentiment comme argument.

### Comment définir la fonction Gradio

Nous allons définir une fonction Gradio qui nous aidera à fournir la fonctionnalité d'analyse de sentiment pour notre application web.

Si vous avez lu mon [article précédent](https://www.freecodecamp.org/news/build-gui-using-gradio-for-machine-learning-models/) sur la création d'interfaces graphiques (GUI) pour les modèles de machine learning en utilisant Gradio, vous savez que Gradio vous permet de créer des composants graphiques pour vos modèles et ils fournissent la fonctionnalité de prédiction du modèle à travers des fonctions.

```
#fonction de modèle pour gradio

def func(utterance):
  return classifier(utterance)

```

Ci-dessus, nous avons créé une fonction appelée `func` et ajouté utterance (c'est-à-dire, le mot à analyser par le modèle pour les sentiments) comme argument pour notre fonction. Nous avons ensuite fait en sorte que notre fonction retourne l'analyse de sentiment de l'utterance précédemment passée et cela nous amène à l'étape suivante.

### Comment construire notre interface Gradio

Ici, nous allons créer notre application web Gradio, ajouter des composants graphiques, puis nous allons lancer l'application.

```
#obtenir la bibliothèque gradio
import gradio as gr
descriptions = "Ceci est un analyseur de sentiment AI qui vérifie et obtient les émotions dans une utterance particulière. Il suffit de mettre une phrase et vous obtiendrez les émotions probables derrière cette phrase"

app = gr.Interface(fn=func, inputs="text", outputs="text", title="Analyseur de Sentiment", description=descriptions)
app.launch()

```

Ci-dessus, nous avons importé la bibliothèque Gradio, puis nous avons ajouté une description de notre projet qui sera ensuite transmise à notre application web.

Nous avons ensuite créé une instance d'interface Gradio où nous allons fournir des détails sur notre application web. Nous avons passé la fonction du modèle dans le paramètre `fn`, puis nous avons fourni le type d'entrée.

Gradio vous permet de créer toute forme d'entrée de votre choix, qu'il s'agisse de texte, de radios, de cases à cocher, de nombres, etc. Mais ici, nous allons utiliser notre entrée sous forme de texte.

Ensuite, nous avons fourni le format de sortie, de la même manière que Gradio vous permet de choisir votre format d'entrée (c'est-à-dire texte, nombres, case à cocher, etc.). Il vous permet également de choisir votre format de sortie.

Dans ce cas, nous allons également utiliser du texte. Après avoir passé le paramètre de sortie, nous avons donné un titre à notre application web.

Enfin, nous lançons l'application.

![Screenshot (36).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1635983823728/v1LcvOBg6.png?auto=compress,format&format=webp)

Maintenant, vous pouvez utiliser votre nouvel outil d'analyse de sentiment !

Merci d'avoir lu.

## **Ressources importantes**

* [Site officiel de Gradio](https://gradio.app/)
* [Documentation de Gradio](https://gradio.app/docs)
* [Dépôt GitHub de Gradio](https://github.com/gradio-app/gradio)