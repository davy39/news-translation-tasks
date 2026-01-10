---
title: Comment exécuter des LLM open source localement avec Ollama
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-04-02T09:25:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-open-source-llms-locally-using-ollama
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Neon-Green-Motivational-Quote--1-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: 'LLM''s '
  slug: llms
- name: open source
  slug: open-source
seo_title: Comment exécuter des LLM open source localement avec Ollama
seo_desc: "This article will guide you through downloading and using Ollama, a powerful\
  \ tool for interacting with open-source large language models (LLMs) on your local\
  \ machine. \nUnlike closed-source models like ChatGPT, Ollama offers transparency\
  \ and customiza..."
---

Cet article vous guidera dans le téléchargement et l'utilisation d'Ollama, un outil puissant pour interagir avec des grands modèles de langage (LLM) open source sur votre machine locale.

Contrairement aux modèles à code fermé comme ChatGPT, Ollama offre transparence et personnalisation, ce qui en fait une ressource précieuse pour les développeurs et les passionnés.

Nous allons explorer comment télécharger Ollama et interagir avec deux modèles LLM open source passionnants : LLaMA 2, un modèle textuel de Meta, et LLaVA, un modèle multimodal capable de traiter à la fois du texte et des images.

## Comment télécharger Ollama

Pour télécharger Ollama, rendez-vous sur le site officiel d'[Ollama](https://ollama.com/) et cliquez sur le bouton de téléchargement.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/ollama-homepage-download.png)
_page d'accueil d'ollama_

Ollama prend en charge 3 systèmes d'exploitation différents, et la version Windows est en mode aperçu (preview).

![Image](https://www.freecodecamp.org/news/content/images/2024/03/ollama-download-screen.png)
_page de téléchargement d'ollama_

Vous pouvez choisir le fichier exécutable en fonction de votre système d'exploitation et, après avoir téléchargé le fichier exécutable avec succès, vous pouvez l'installer en l'exécutant.

Pour les utilisateurs de Linux, vous devez exécuter la commande affichée à l'écran au lieu de télécharger un fichier exécutable.

## Comment utiliser Ollama

Pour vous montrer la puissance de l'utilisation des LLM open source localement, je vais présenter plusieurs exemples avec différents modèles open source et différents cas d'utilisation. Cela vous aidera à utiliser facilement n'importe quel futur modèle LLM open source.

Alors, commençons par le premier exemple !

### Comment exécuter le modèle LLaMA 2 de Meta

Le modèle Llama 2 est un LLM open source de Meta et nous allons interagir avec lui comme nous le ferions avec ChatGPT (version gratuite), par une interaction uniquement textuelle.

Tout d'abord, téléchargeons le modèle à l'aide de la commande suivante :

```bash
ollama run llama2

```

Vous devriez voir une sortie similaire à celle-ci après le téléchargement du modèle.

```bash
pulling manifest
pulling 8934d96d3f08... 100% ╖████████████████████████████████████████████████████████████████████████████████╢ 3.8 GB
pulling 8c17c2ebb0ea... 100% ╖████████████████████████████████████████████████████████████████████████████████╢ 7.0 KB
pulling 7c23fb36d801... 100% ╖████████████████████████████████████████████████████████████████████████████████╢ 4.8 KB
pulling 2e0493f67d0c... 100% ╖████████████████████████████████████████████████████████████████████████████████╢   59 B
pulling fa304d675061... 100% ╖████████████████████████████████████████████████████████████████████████████████╢   91 B
pulling 42ba7f8a01dd... 100% ╖████████████████████████████████████████████████████████████████████████████████╢  557 B
verifying sha256 digest
writing manifest
removing any unused layers
success
>>> Send a message (/? for help)

```

Maintenant, il devrait vous demander d'envoyer un message ou un prompt. Demandons à llama2 "What can you do for me?" (Vous pouvez demander ce que vous voulez).

Si vous avez posé la même question que ci-dessus, vous devriez obtenir une réponse comme celle-ci :

```bash
>>> What can you do for me?

As a responsible AI language model, I am here to assist you with any questions or tasks you may have. Here are some examples of things I can help
with:

1. Answering questions: I can provide information on a wide range of topics, from science and technology to history and culture.
2. Generating ideas: I can help you brainstorm ideas for creative projects, or provide suggestions for solving problems.
3. Writing assistance: I can help you with writing tasks such as proofreading, edit-ing, and suggesting alternative words or phrases.
4. Translation: I can translate text from one language to another.
5. Summarizing content: I can summarize long pieces of text, such as articles or documents, into shorter, more digestible versions.
6. Creativity: I can help you generate creative ideas for stories, poems, or other forms of writing.
7. Language learning: I can assist you in learning a new language by providing grammar explanations, vocabulary lists, and practice exercises.
8. Chatting: I'm here to chat with you and provide a response to any question or topic you'd like to discuss.

Please let me know if there is anything specific you would like me to help you with.

>>> Send a message (/? for help)

```

C'est la réponse que j'ai obtenue de llama2.

Pour quitter le programme, vous pouvez taper `/exit`.

Exécutons maintenant un modèle multimodal où vous pouvez envoyer une image et poser des questions basées sur celle-ci.

### Comment exécuter le modèle LLaVA

LLaVA est un modèle LLM multimodal open source. Un modèle multimodal peut prendre plusieurs types d'entrées et générer une réponse en conséquence.

En utilisant ce modèle, nous allons maintenant transmettre une image et poser une question basée sur celle-ci.

Tout d'abord, téléchargeons le modèle :

```bash
ollama run llava

```

Après avoir téléchargé le modèle avec succès, vous devriez voir quelque chose comme ceci dans le terminal :

```bash
pulling manifest
pulling 170370233dd5... 100% ╖████████████████████████████████████████████████████████████████████████████████╢ 4.1 GB
pulling 72d6f08a42f6... 100% ╖████████████████████████████████████████████████████████████████████████████████╢ 624 MB
pulling 43070e2d4e53... 100% ╖████████████████████████████████████████████████████████████████████████████████╢  11 KB
pulling c43332387573... 100% ╖████████████████████████████████████████████████████████████████████████████████╢   67 B
pulling ed11eda7790d... 100% ╖████████████████████████████████████████████████████████████████████████████████╢   30 B
pulling 7c658f9561e5... 100% ╖████████████████████████████████████████████████████████████████████████████████╢  564 B
verifying sha256 digest
writing manifest
removing any unused layers
success
>>> Send a message (/? for help)

```

J'utiliserai cette [image](https://www.pexels.com/photo/aerial-view-of-vehicles-on-a-street-and-a-man-on-a-crosswalk-16456833/) de [pexels.com](https://www.pexels.com/).

Voici la sortie que j'ai obtenue de LLaVA :

```bash
>>> What's in this image? ./Downloads/test-image-for-llava.jpeg
Added image './Downloads/test-image-for-llava.jpeg'
 The image shows a person walking across a crosswalk at an intersection. There are traffic lights visible, and the street has a bus parked on one
side. The road is marked with lane markings and a pedestrian crossing signal. The area appears to be urban and there are no visible buildings or
structures in the immediate vicinity of the person.

>>> Send a message (/? for help)

```

Vous pouvez voir qu'il s'agit d'une explication précise de l'image.

N'hésitez pas à essayer autre chose et amusez-vous bien !

## Conclusion

C'est tout ! Avec Ollama, vous pouvez expérimenter des LLM puissants comme LLaMA 2 et LLaVA sur votre propre machine.

Téléchargez Ollama et explorez le monde passionnant des grands modèles de langage open source !