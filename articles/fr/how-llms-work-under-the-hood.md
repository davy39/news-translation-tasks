---
title: Comment fonctionnent les LLM sous le capot
subtitle: ''
author: Alma Mohapatra
co_authors: []
series: null
date: '2025-10-02T14:40:10.904Z'
originalURL: https://freecodecamp.org/news/how-llms-work-under-the-hood
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759415587363/cc861698-598b-488a-bc79-58aeb99500ea.png
tags:
- name: 'LLM''s '
  slug: llms
- name: Python
  slug: python
- name: llm
  slug: llm
seo_title: Comment fonctionnent les LLM sous le capot
seo_desc: Large Language Models (LLMs) like LLaMA 2 and Mistral are often described
  as “black boxes”. This means that you can see the text you give them and the responses
  they produce, but their inner workings remain hidden. Inside the model, billions
  of weigh...
---

Les grands modèles de langage (LLM) comme LLaMA 2 et Mistral sont souvent décrits comme des "boîtes noires". Cela signifie que vous pouvez voir le texte que vous leur donnez et les réponses qu'ils produisent, mais que leur fonctionnement interne reste caché. À l'intérieur du modèle, des milliards de poids et d'activations de neurones transforment l'entrée en sortie de manières que nous ne pouvons pas interpréter directement ; nous voyons donc les résultats, mais pas le raisonnement étape par étape qui les sous-tend. Ils génèrent du texte de manière impressionnante, mais comment représentent-ils réellement le sens en interne ?

Dans ce tutoriel, vous allez exécuter un LLM open-source localement sur votre machine et explorer ses activations cachées — les valeurs internes des neurones produites lors du traitement du texte. En visualisant ces activations, vous pourrez voir des schémas liés au sentiment, à l'analogie et aux biais.

Ce tutoriel vous aidera à :

* Comprendre comment les LLM représentent le texte en interne
    
* Expérimenter avec les embeddings et les états cachés en Python
    
* Créer des visualisations montrant les différences entre les mots, les phrases ou les sentiments
    
* Réfléchir à la manière dont les biais et les associations émergent dans les modèles neuronaux
    

Voici ce que nous allons aborder dans ce tutoriel, et oui — nous ferons tout cela localement, sans frais de cloud.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Étape 0 : Créer et activer un environnement virtuel](#heading-etape-0-creer-et-activer-un-environnement-virtuel)
    
* [Étape 1 : Charger un modèle local et un tokenizer](#heading-etape-1-charger-un-modele-local-et-un-tokenizer)
    
* [Étape 2 : Extraire les états cachés](#heading-etape-2-extraire-les-etats-caches)
    
* [Étape 3 : Visualiser les activations de sentiment](#heading-etape-3-visualiser-les-activations-de-sentiment)
    
* [Étape 4 : Comparer deux phrases](#heading-etape-4-comparer-deux-phrases)
    
* [Étape 5 : Visualiser les analogies avec la PCA](#heading-etape-5-visualiser-les-analogies-avec-la-pca)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

* Python 3.10+
    
* Une machine avec au moins 8 Go de RAM (16 Go recommandés)
    
* Une familiarité de base avec la ligne de commande et Python
    
* Packages : `torch`, `transformers`, `matplotlib`, `scikit-learn`
    

## Étape 0 : Créer et activer un environnement virtuel

Pourquoi utiliser un environnement virtuel ?

Lorsque vous installez des bibliothèques Python avec `pip`, elles vont normalement dans votre configuration Python globale. Cela peut vite devenir désordonné :

* Différents projets peuvent nécessiter différentes versions de la même bibliothèque (par exemple, `torch==2.0` vs `torch==2.2`).
    
* La mise à jour d'un projet pourrait accidentellement en casser un autre.
    
* Votre Python système peut se retrouver encombré de packages dont vous n'avez pas réellement besoin ailleurs.
    

Un environnement virtuel résout ce problème en créant un "bac à sable" autonome juste pour votre projet.

* Toutes les installations (comme `torch`, `transformers`, `matplotlib`) résident à l'intérieur du dossier de votre projet.
    
* Lorsque vous avez terminé, vous pouvez supprimer le dossier et rien d'autre sur votre ordinateur n'est affecté.
    
* C'est la meilleure pratique standard pour le développement Python — léger et sûr.
    

En résumé : un environnement virtuel sépare les outils de votre projet, afin que rien ne casse lorsque vous expérimentez.

### Windows (Invite de commande ou PowerShell) / Mac (Terminal)

1. Créez ou accédez au dossier de votre projet (créez-en un si nécessaire) :
    
2. Créez l'environnement virtuel : cela crée un dossier nommé `venv/` à l'intérieur de votre projet.
    
3. Activez-le.
    
4. Votre invite de commande ressemblera maintenant à l'étape 4 dans le code ci-dessous.
    

```bash
#étape 1
mkdir llm_viz
cd llm_viz

#étape 2
python -m venv venv

#étape 3
#Windows
venv\Scripts\activate
#Mac
source venv/bin/activate

#étape 4
#windows
(venv) C:\Users\VotreNom\llm_viz>
#mac
(venv) votre-macbook:llm_viz votrenom$
```

### Installer les dépendances

```bash
pip install torch transformers matplotlib scikit-learn
```

Nous utiliserons DistilBERT (distilbert-base-uncased) car il est petit et facile à exécuter localement. Vous pouvez passer à des modèles plus grands comme LLaMA ou Mistral si vous disposez d'un matériel plus puissant.

## Étape 1 : Charger un modèle local et un tokenizer

Cette étape télécharge **DistilBERT** (un petit LLM gratuit) et le prépare à s'exécuter localement.

Dans un fichier nommé `app.py`, collez le code suivant.

**Note :** La première fois que vous l'exécutez via `python app.py`, Hugging Face téléchargera automatiquement le modèle (~250 Mo). Vous ne faites cela qu'une seule fois.

```python
from transformers import AutoTokenizer, AutoModel
import torch

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, output_hidden_states=True)
```

Ce code charge un petit modèle de langage open-source afin que nous puissions travailler avec lui sur notre propre ordinateur.  
Tout d'abord, il importe la bibliothèque Transformers et PyTorch, qui fournissent les outils pour télécharger et exécuter le modèle. Ensuite, il choisit le nom du modèle (`distilbert-base-uncased`) et utilise `AutoTokenizer` pour transformer le texte en tokens que le modèle comprend, tandis qu'`AutoModel` télécharge le modèle pré-entraîné lui-même et le prépare à renvoyer les sorties des couches cachées que nous allons visualiser.

## Étape 2 : Extraire les états cachés

Cela injecte du texte et récupère les "activations cachées" (les sorties des neurones à l'intérieur du modèle).

Dans le même fichier `app.py`, ajoutez cette fonction sous le code de l'étape 1.

```python
def get_hidden_states(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    hidden = outputs.hidden_states[-1][0] # Dernière couche cachée
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    return tokens, hidden

tokens, hidden = get_hidden_states("I love pizza!")
print(tokens)
print(hidden.shape)
```

Maintenant, nous pouvons appeler `get_hidden_states("I love pizza!")` et cela renverra des tokens comme `["i", "love", "pizza", "!"]` et un grand tenseur de nombres.

Vous pouvez utiliser `python app.py` pour exécuter le code.

## Étape 3 : Visualiser les activations de sentiment

Cette étape trace comment les valeurs des neurones diffèrent pour des phrases joyeuses ou tristes. Nous allons comparer les activations pour des critiques de films positives et négatives.

Dans le même `app.py`, ajoutez cette fonction sous le code de l'étape 2.

```python
import matplotlib.pyplot as plt

def plot_token_activations(tokens, hidden, title, filename):
    plt.figure(figsize=(12, 4))
    for i, token in enumerate(tokens):
        plt.plot(hidden[i].numpy(), label=token)
    plt.title(title)
    plt.xlabel("Neuron Index")
    plt.ylabel("Activation")
    plt.legend(loc="upper right", fontsize="x-small")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Exemple positif
tokens_pos, hidden_pos = get_hidden_states("I love this movie, it is fantastic!")
plot_token_activations(tokens_pos, hidden_pos, "Positive Sentiment Example", "positive_sentiment.png")

# Exemple négatif
tokens_neg, hidden_neg = get_hidden_states("I hate this movie, it is terrible.")
plot_token_activations(tokens_neg, hidden_neg, "Negative Sentiment Example", "negative_sentiment.png")
```

Après avoir exécuté le code `python app.py`, vérifiez votre dossier — vous verrez deux fichiers image : `positive_sentiment.png` et `negative_sentiment.png`. Ils ressembleront à des graphiques linéaires montrant les activations pour chaque token.

Figure 1 : Activations pour une critique positive. Des mots comme "love" et "fantastic" activent des schémas de neurones distinctifs.

![Figure 1 : Activations pour une critique positive. Des mots comme "love" et "fantastic" activent des schémas de neurones distinctifs.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757910763307/5556cf9b-69a9-4f7b-b13e-76041d2d52b0.png align="center")

Figure 2 : Activations pour une critique négative. Des mots comme "hate" et "terrible" déclenchent des courbes de neurones différentes.

![Figure 2 : Activations pour une critique négative. Des mots comme "hate" et "terrible" déclenchent des courbes de neurones différentes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757910816349/9aa6e149-3ff7-443e-96f9-7f86af0cc9bd.png align="center")

## Étape 4 : Comparer deux phrases

Cette étape compare les schémas neuronaux moyens entre deux phrases.

Maintenant, dans le même `app.py`, ajoutez cette fonction sous le code de l'étape 3.

```python
def compare_sentences(s1, s2, filename):
    tokens1, hidden1 = get_hidden_states(s1)
    tokens2, hidden2 = get_hidden_states(s2)
    
    plt.figure(figsize=(10,5))
    plt.plot(hidden1.mean(dim=0).numpy(), label=s1[:30]+"...")
    plt.plot(hidden2.mean(dim=0).numpy(), label=s2[:30]+"...")
    plt.title("Sentence Activation Comparison")
    plt.xlabel("Neuron Index")
    plt.ylabel("Mean Activation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

compare_sentences("I love coding.", "I hate coding.", "sentence_comparison.png")
```

Après avoir exécuté le code `python app.py`, vous obtiendrez `sentence_comparison.png`, montrant deux courbes — une pour la phrase joyeuse, une pour la phrase négative.

Figure 3 : Comparaison de "I love coding" vs "I hate coding". Même en faisant la moyenne sur les tokens, les profils neuronaux diffèrent considérablement.

![Figure 3 : Comparaison de "I love coding" vs "I hate coding". Même en faisant la moyenne sur les tokens, les profils neuronaux diffèrent considérablement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757910867868/824567dd-b390-4305-aa87-44d076205d3a.png align="center")

## Étape 5 : Visualiser les analogies avec la PCA

Nous pouvons vérifier si les embeddings encodent des analogies sémantiques comme homme → femme :: roi → reine.

Cette étape projette les embeddings de mots comme *homme, femme, roi, reine* dans un espace 2D afin que vous puissiez voir les relations.

Maintenant, dans le même `app.py`, ajoutez cette fonction sous le code de l'étape 4.

```python
from sklearn.decomposition import PCA

def get_sentence_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    hidden = outputs.last_hidden_state.mean(dim=1).squeeze()
    return hidden

def plot_embeddings(words, embeddings, filename):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(torch.stack(embeddings).numpy())

    plt.figure(figsize=(8, 6))
    for i, word in enumerate(words):
        x, y = reduced[i]
        plt.scatter(x, y, marker="o", s=100)
        plt.text(x+0.02, y+0.02, word, fontsize=12)
    plt.title("Word Embeddings in 2D (PCA)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

words = ["man", "woman", "king", "queen"]
embeddings = [get_sentence_embedding(w) for w in words]
plot_embeddings(words, embeddings, "word_analogies.png")
```

Après avoir exécuté le code `python app.py`, vous aurez `word_analogies.png` montrant la célèbre relation *homme→femme* et *roi→reine* sous forme de lignes presque parallèles.

Figure 4 : Visualisation PCA des embeddings de mots. Homme-femme et roi-reine forment des relations parallèles, reflétant la structure de l'analogie.

![Figure 4 : Visualisation PCA des embeddings de mots. Homme-femme et roi-reine forment des relations parallèles, reflétant la structure de l'analogie.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757910904012/758e3245-5ec7-4108-ae18-9fba8632f1a0.png align="center")

## Conclusion

Vous avez construit une boîte à outils locale pour :

* Extraire les activations cachées d'un LLM
    
* Visualiser l'activité neuronale pour les sentiments positifs vs négatifs
    
* Explorer les analogies sémantiques comme "roi → reine"
    
* Inspecter les biais potentiels dans les associations de rôles
    

Cela aide à démystifier les LLM — en montrant qu'ils sont des matrices massives de nombres encodant du sens, et non de la magie.

Les petits modèles comme DistilBERT fonctionnent sur n'importe quel ordinateur portable. Des modèles plus grands comme LLaMA 2 peuvent permettre de pousser l'exploration encore plus loin.