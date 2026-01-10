---
title: Comment commencer avec Hugging Face – Modèles et ensembles de données d'IA
  open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-10T21:05:36.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-hugging-face
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/HuggingFace_Title-1.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
- name: open source
  slug: open-source
seo_title: Comment commencer avec Hugging Face – Modèles et ensembles de données d'IA
  open source
seo_desc: "By Ambreen Khan\nWhat is Hugging Face \U0001F917?\nIf you are interested\
  \ in Artificial Intelligence and Natural Language Processing, you have probably\
  \ heard of Hugging Face – the company named after a cute emoji. \nHugging Face is\
  \ not only a company, but also a..."
---

Par Ambreen Khan

## **Qu'est-ce que Hugging Face 🤗 ?**

Si vous vous intéressez à l'intelligence artificielle et au traitement du langage naturel, vous avez probablement entendu parler de Hugging Face – la société nommée d'après un emoji mignon.

Hugging Face n'est pas seulement une société, mais aussi une plateforme qui transforme les domaines de l'IA et du TAL grâce à l'open source et la science ouverte.

Hugging Face offre une plateforme appelée le Hugging Face Hub, où vous pouvez trouver et partager des milliers de modèles d'IA, d'ensembles de données et d'applications de démonstration. Le Hub est comme le GitHub de l'IA, où vous pouvez collaborer avec d'autres passionnés et experts en apprentissage automatique, et apprendre de leur travail et de leur expérience.

La mission de Hugging Face est de démocratiser le bon apprentissage automatique, un commit à la fois. Que vous soyez débutant ou professionnel, vous pouvez bénéficier des ressources et outils incroyables que Hugging Face fournit.

Dans cet article, je vais vous guider à travers les bases de Hugging Face. Vous apprendrez comment créer votre compte Hugging Face, configurer votre environnement de développement et utiliser certains des modèles pré-entraînés disponibles sur le Hub. Commençons ! 🚀

## Voici ce que nous allons couvrir :

1. [Que pouvez-vous faire sur la plateforme Hugging Face ?](#heading-quest-ce-que-vous-pouvez-faire-sur-la-plateforme-hugging-face)
    * [Télécharger et affiner des modèles open source existants](#telecharger-et-affiner-des-modeles-open-source-existants)
    * [Exécuter des modèles directement depuis Hugging Face](#executer-des-modeles-directement-depuis-hugging-face)
    * [Ajouter/créer votre propre modèle](#ajoutercreer-votre-propre-modele)
    * [Utiliser des ensembles de données existants](#utiliser-des-ensembles-de-donnees-existants)
    * [Créer/parcourir des applications de démonstration (également connues sous le nom de Spaces)](#creerparcourir-des-applications-de-demonstration-egalement-connues-sous-le-nom-de-spaces)
    * [Rejoindre ou créer une organisation](#rejoindre-ou-creer-une-organisation)
    * [Créer un portfolio](#creer-un-portfolio)
    * [Apprendre des compétences en IA](#apprendre-des-competences-en-ia)
2. [Terminologie de Hugging Face](#heading-terminologie-de-hugging-face)
3. [Comment commencer avec Hugging Face](#heading-comment-commencer-avec-hugging-face)
    * [Créer un compte Hugging Face](#heading-creer-un-compte-hugging-face)
    * [Configurer votre environnement](#heading-configurer-votre-environnement)
4. [Comment utiliser des modèles pré-entraînés dans Hugging Face](#heading-comment-utiliser-des-modeles-pre-entraines-dans-hugging-face)
5. [Comment trouver le bon modèle pré-entraîné](#heading-comment-trouver-le-bon-modele-pre-entraine)
6. [Quelle est la suite ?](#quest-la-suite)


## Que pouvez-vous faire sur la plateforme Hugging Face ?

Voici quelques-unes des choses incroyables que vous pouvez faire sur Hugging Face :

### Télécharger et affiner des modèles open source existants :

Pourquoi commencer de zéro lorsque vous pouvez tirer parti de la puissance de plus de 450k modèles déjà disponibles dans la bibliothèque de modèles de Hugging Face ?

Vous pouvez facilement télécharger ces modèles et les affiner sur votre propre ensemble de données personnalisé avec seulement quelques lignes de code. De cette façon, vous pouvez économiser du temps et des ressources, et obtenir un modèle qui répond à vos besoins spécifiques.

Vous pouvez utiliser ces modèles pour effectuer diverses tâches, telles que :

1. Traitement du langage naturel (par exemple, traduction, résumé et génération de texte)
2. Fonctions liées à l'audio (par exemple, reconnaissance automatique de la parole, détection d'activité vocale et texte-parole)
3. Tâches de vision par ordinateur (par exemple, estimation de profondeur, classification d'images et traitement d'image à image),
4. Modèles multimodaux capables de gérer divers types de données (texte, images, audio) et de produire plusieurs types de sortie.

### Exécuter des modèles directement depuis Hugging Face :

Si vous ne souhaitez pas configurer ces modèles sur vos propres machines, vous pouvez simplement utiliser la bibliothèque Transformer de Hugging Face pour vous connecter à ces modèles, envoyer des requêtes et recevoir des sorties.

### Ajouter/créer votre propre modèle :

Si vous avez une idée brillante pour un nouveau modèle, ou si vous souhaitez améliorer un modèle existant, vous pouvez également ajouter/créer votre propre modèle sur Hugging Face.

La plateforme hébergera votre modèle et vous permettra de fournir des informations supplémentaires, de télécharger des fichiers essentiels et de gérer différentes versions. Vous pouvez également choisir si vos modèles sont publics ou privés, afin de décider quand ou si vous souhaitez les partager avec le monde.

Une fois votre modèle prêt, vous pouvez y accéder directement depuis Hugging Face, envoyer des requêtes et récupérer les sorties pour les intégrer dans les applications que vous développez.

### Utiliser des ensembles de données existants :

Un bon modèle a besoin d'un bon ensemble de données. Hugging Face fournit un dépôt de plus de 90 000 ensembles de données que vous pouvez utiliser et alimenter dans vos modèles.

Vous pouvez examiner en profondeur l'ensemble de données à l'aide du visualiseur de données. Vous pouvez également contribuer vos propres ensembles de données au dépôt et aider la communauté de l'apprentissage automatique à grandir.

![Image](https://lh7-us.googleusercontent.com/tYogXTtF_pOn4dIRAFUDP20kpbf4yzTvkWdINjnFqjka6N5b4xfDRT_ssvVqQCig09SlSfb3voil16yE37YOPLDmsHj508xkPtYWKHF63rX8ozOW21BQH2dKQL5jEuhq5Yn-m1xyU9pKKHOimOlDqHk)
_Capture d'écran du visualiseur de données_

### Créer/parcourir des applications de démonstration (également connues sous le nom de Spaces) :

Les Spaces de Hugging Face sont des dépôts Git qui vous permettent de présenter vos applications d'apprentissage automatique. Vous pouvez également parcourir et essayer les Spaces créés par d'autres utilisateurs, et trouver l'inspiration pour votre prochaine application d'IA.

Avec des milliers d'applications ML parmi lesquelles choisir, vous ne manquerez jamais de choses amusantes et intéressantes à faire.

Voici quelques Spaces sympas que vous pouvez consulter :

* [OpenAI's Whisper](https://huggingface.co/spaces/openai/whisper) : Transcrivez des entrées de microphone ou audio longues avec un simple clic.
* [AI Comic Factory](https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory) : Créez vos propres bandes dessinées.
* [QR Code AI Art Generator](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator) : Générez de beaux codes QR à l'aide de l'IA.
* [Stable Video Diffusion](https://huggingface.co/spaces/multimodalart/stable-video-diffusion) (Img2Vid - XT) : Générez une vidéo de 4s à partir d'une seule image.
* [Video-LLaMA](https://huggingface.co/spaces/DAMO-NLP-SG/Video-LLaMA) : Modèle de langage audio-visuel pour la compréhension vidéo.

### Rejoindre ou créer une organisation :

Vous pouvez rejoindre ou créer votre propre organisation sur Hugging Face. Cela vous permet de présenter votre travail et de collaborer avec d'autres membres de votre université, laboratoire ou entreprise. Vous pouvez également travailler sur des ensembles de données, modèles et espaces privés avec votre organisation.

### Créer un portfolio :

Vous pouvez créer un portfolio professionnel sur Hugging Face pour présenter votre travail et commencer à construire votre réputation. Cela peut vous aider à obtenir des emplois liés à l'entraînement, l'intégration et le développement de modèles d'IA.

Hugging Face fournit les ressources informatiques de base pour exécuter l'application de démonstration, y compris 16 Go de RAM, 2 cœurs CPU et 50 Go d'espace disque gratuitement. Vous pouvez également améliorer votre matériel pour des performances améliorées et plus rapides avec des options payantes.

### Apprendre des compétences en IA :

Hugging Face est une excellente plateforme pour apprendre des compétences en IA. Elle offre un ensemble complet d'outils et de ressources pour l'entraînement et l'utilisation de modèles. Cela inclut des démonstrations, des cas d'utilisation, de la documentation et des tutoriels qui vous guident à travers l'ensemble du processus d'utilisation de ces outils et d'entraînement de modèles.

Vous pouvez également apprendre des experts et de la communauté sur Hugging Face, et améliorer vos connaissances et compétences en IA.

## Terminologie de Hugging Face

Il y a quelques termes que vous devrez connaître pour tirer le meilleur parti de votre travail avec Hugging Face.

**Modèle pré-entraîné :** Un modèle qui a été entraîné sur un grand ensemble de données pour une tâche spécifique avant d'être mis à disposition pour une utilisation.

**Inférence :** L'inférence est le processus d'utilisation d'un modèle entraîné pour faire des prédictions ou tirer des conclusions sur de nouvelles données invisibles, sur la base des motifs appris à partir des données d'entraînement.

**Transformers :** Les Transformers sont des modèles qui peuvent gérer des tâches basées sur du texte, telles que la traduction, le résumé et la génération de texte. Ils utilisent une architecture spéciale qui repose sur des mécanismes d'attention pour capturer les relations entre les mots et les phrases.

**Tokenizer** : Un tokenizer est un processus qui décompose le texte en unités plus petites appelées tokens. Les tokens sont généralement des mots ou des sous-mots qui peuvent être utilisés pour des tâches de traitement du langage naturel (TAL).

## **Comment commencer avec Hugging Face**

Pour commencer avec HuggingFace, vous devrez configurer un compte et installer les bibliothèques et dépendances nécessaires. Ne vous inquiétez pas, c'est facile et amusant !

Voici les étapes que vous devez suivre :

### Créer un compte Hugging Face

L'inscription en tant que contributeur individuel à la communauté est gratuite. Vous pouvez également opter pour un plan 'Pro' ou un plan personnalisé pour les organisations si vous avez besoin de plus de fonctionnalités et de ressources.

Allez sur le site web de Hugging Face et cliquez sur "S'inscrire" pour créer un compte gratuit.

Ensuite, entrez votre adresse e-mail et un mot de passe. Cliquez sur suivant et complétez votre profil et la vérification de sécurité.

![Image](https://lh7-us.googleusercontent.com/OQA0CUGvs2Dg4LKI3X5mPVjNj7LYIbeUDF0q46sC2p39n-Ca56OwiGNYYdPJU4NrcZG4s-G_KKYX1YADa9QL2yyjHcMDoQ43BBllp6SHgq6P_33XG7ta4nVDTsjierUonbH3YYwuj7CploOW2tpAopo)
_Configuration d'un compte Hugging Face_

Félicitations, vous êtes maintenant membre de Hugging Face ! 🎉 Vous serez dirigé vers la page 'Bienvenue' de Hugging Face, où vous pourrez trouver plus d'informations et de conseils sur l'utilisation de la plateforme.

En bonus, vous obtenez également un dépôt hébergé basé sur Git où vous pouvez créer vos Modèles, Ensembles de données et Spaces. Vous pouvez le faire directement en utilisant le site web ou en utilisant la CLI. Si vous préférez cette dernière, vous pouvez consulter les instructions détaillées sur la page 'Bienvenue' sous la section 'Accès programmatique'.

![Image](https://lh7-us.googleusercontent.com/PhM1PcZxLn4jgchRlU2J6ZEemobdrBTBq0ypqFM3Y2mZsTwtvFUg7nhJ4KBL4HfvYJz4Zp2KsZa7SvbfJMe8o9ARKvy1NOdCGSn4WEJ0JUivxT2Lp4nnWrU21cCjjGl5yJMG7BqfaGzvqVGd9z06Mrg)
_Écran de bienvenue de Hugging Face montrant les options pour créer un nouveau modèle, parcourir la documentation et configurer l'accès programmatique_

### Configurer votre environnement

Avant de commencer à utiliser le hub de Hugging Face de manière programmatique, vous devrez configurer votre environnement.

#### Étape 1 : Installer Python et Pip :

Assurez-vous d'avoir Python 3.8 ou une version ultérieure installée sur votre système. Vous aurez également besoin de Pip, le gestionnaire de paquets pour Python, pour installer les bibliothèques de Hugging Face. Si vous n'avez pas Python, vous pouvez l'installer en suivant les instructions [ici](https://www.python.org/downloads/).

#### Étape 2 : Installer les bibliothèques HuggingFace :

Ouvrez un terminal ou une invite de commande et exécutez la commande suivante pour installer les bibliothèques HuggingFace :

```shell
pip install transformers
```

Cela installera la bibliothèque principale de Hugging Face ainsi que ses dépendances. Pour avoir toutes les fonctionnalités, vous devriez également installer les bibliothèques datasets et tokenizers.

```shell
pip install tokenizers, datasets
```

#### Étape 3 : Configurer un environnement de développement :

Choisissez un éditeur de code ou un IDE de votre choix, tel que Jupyter Notebook, PyCharm ou Visual Studio Code. Créez un nouveau répertoire de projet et configurez un environnement virtuel pour isoler les dépendances de votre projet. Vous pouvez trouver plus d'informations sur la façon de faire cela [ici](https://docs.python.org/3/library/venv.html).

Avec ces étapes terminées, vous avez réussi à configurer Hugging Face sur votre système et êtes prêt à commencer à explorer ses fonctionnalités et capacités. C'est parti ! 🚀

## Comment utiliser des modèles pré-entraînés dans Hugging Face

L'une des meilleures choses à propos de Hugging Face est qu'il vous donne accès à des milliers de modèles pré-entraînés qui peuvent effectuer diverses tâches sur différents types de données. Que vous travailliez avec du texte, de la vision, de l'audio ou une combinaison de ceux-ci, vous pouvez trouver un modèle qui répond à vos besoins.

Hugging Face dispose de deux bibliothèques principales qui fournissent un accès aux modèles pré-entraînés : **Transformers** et **Diffusers**. La bibliothèque Transformers gère les tâches basées sur du texte, telles que la traduction, le résumé et la génération de texte. Diffusers peut gérer les tâches basées sur des images, telles que la synthèse d'images, l'édition d'images et la légende d'images.

Vous avez déjà installé la bibliothèque transformers lors de la configuration de l'environnement. Voyons comment vous pouvez l'utiliser pour travailler avec des modèles pré-entraînés.

### Étape 1 : Visitez la page PyPI

Pour en savoir plus sur la bibliothèque transformers, vous pouvez visiter sa page sur PyPI, l'index des paquets Python.

Allez sur [PyPi](https://pypi.org/) et recherchez 'transformers'. Cliquez sur la dernière version de la bibliothèque transformers affichée dans le résultat de la recherche. Vous verrez une brève introduction de la bibliothèque, ainsi que quelques liens et informations utiles.

### Étape 2 : Téléchargez et utilisez des modèles pré-entraînés

La bibliothèque transformers fournit des API pour télécharger et utiliser rapidement des modèles pré-entraînés sur un texte donné, les affiner sur vos propres ensembles de données, puis les partager avec la communauté sur le [hub de modèles](https://huggingface.co/models) de Hugging Face.

### Étape 3 : Utilisez la méthode `pipeline()`

Pour utiliser un modèle pré-entraîné sur une entrée donnée, Hugging Face fournit une méthode `pipeline()`, une API facile à utiliser pour effectuer une grande variété de tâches.

La méthode [pipeline()](https://huggingface.co/docs/transformers/v4.36.1/en/main_classes/pipelines#transformers.pipeline) simplifie l'utilisation de n'importe quel [modèle](https://huggingface.co/models) du Hub pour l'inférence sur n'importe quelle tâche de langage, de vision par ordinateur, de parole et multimodale.

Essayons d'effectuer une tâche en utilisant la méthode pipeline().

#### Tâche : Analyse des sentiments :

Utilisons la méthode `pipeline()` pour classer les textes positifs et négatifs fournis par l'utilisateur :

```python
from transformers import pipeline

# Charger le modèle d'analyse des sentiments pré-entraîné
sentiment_analysis = pipeline(
"sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

input_text = [
"C'est une super application, mon plus gros problème est que les lecteurs de cartes ne se connectent pas régulièrement. Ce qui est un très mauvais service client pour nous car nous devons entrer manuellement les cartes de débit de nos clients, ce qui prend du temps. Cela ralentit notre efficacité."
]

# Effectuer l'analyse des sentiments sur le texte d'entrée
result = sentiment_analysis(input_text)

# Imprimer le résultat
print(result)
```

L'instruction pipeline télécharge et met en cache le modèle pré-entraîné utilisé par le pipeline, tandis que l'instruction `result = sentiment_analysis(input_text)` l'évalue sur le texte donné.

**Sortie :**

```shell
[{'label': 'NEGATIVE', 'score': 0.9996176958084106}]
```

Ici, la réponse est "NEGATIVE" avec une confiance de 99,96 %.

#### Tâche : Reconnaissance automatique de la parole

Essayons une autre tâche qui implique la reconnaissance vocale.

```python
from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition",
                       model="openai/whisper-small")
result = transcriber(
    "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")

print(result)
```

**Sortie :**

```shell
{'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'}
```

Vous pouvez voir à quel point il est facile de faire fonctionner un modèle pré-entraîné en utilisant les bibliothèques de Hugging Face.

### Comment trouver le bon modèle pré-entraîné

Mais comment pouvez-vous trouver le bon modèle pré-entraîné si vous souhaitez effectuer une tâche spécifique ?

C'est en fait assez facile. Vous pouvez parcourir les modèles sur le site web de Hugging Face, et les filtrer par tâche, langue, framework, et plus encore. Vous pouvez également rechercher des modèles et des ensembles de données par mot-clé et les trier par tendance, plus de likes, plus de téléchargements, ou par mises à jour récentes.

![Image](https://lh7-us.googleusercontent.com/e94ThjikQ7rAFXu-LUx6a0ZosgWFKqjfSION915OcA9fQweqZO62wLdyPkAH657OFOlO-Zw4O9WLvtQ1auZl8Oo9inxtul7J1hkuXs1Bqs10n_FRy8P6o-mhGVB_QKVEz4CHL7-mOm9wTGzbqr6gJJY)
_Recherche de modèles_

Chaque modèle dispose d'une fiche modèle contenant des informations importantes, telles que les détails du modèle, un exemple d'inférence, la procédure d'entraînement, les fonctionnalités d'interaction avec la communauté et le lien vers les fichiers. Vous pouvez également essayer le modèle sur la page de la fiche modèle en utilisant la section Inference API.

![Image](https://lh7-us.googleusercontent.com/Fs-OKp8zUOF4WIN9-dFBYQIQDL5loPowHzEzIr7T8mWZltyGSDGEj8K-U-CrTZwPK3D1RjkFZwSfhNex_BhWYCYW4AkUFuADkefneuJtyHSYkDoTqAU24zqvUFdTjx978g8jfVkoajhZ9PF_lTi2Ekg)
_Inference API_

Vous pouvez également vérifier la liste des espaces qui utilisent ce modèle particulier et explorer davantage les espaces en cliquant sur le lien de l'espace.

![Image](https://lh7-us.googleusercontent.com/z2abf18c-bvqWM82OJz7ua_sebywG4DHXQQbWE4QD0Vmv1tIOw35Okw56Va5nBrJlVRWJArC_L6RWdgYIl1nadcaRlMfbt_fyZyK6hFpDkhXAgURyDiU24hzRy91W8jQbwMbs4tavsAv2r3Di-Qjpo0)
_Spaces_

## Quelle est la suite ?

Dans ce guide, vous avez appris les bases de Hugging Face, et comment utiliser ses bibliothèques, modèles, ensembles de données et espaces. Mais il y a encore tant de choses à découvrir et à apprécier !

Voici quelques conseils pour tirer le meilleur parti de Hugging Face :

* Plongez dans les Spaces de Hugging Face : Les Spaces sont là où la magie opère. Vous pouvez trouver et essayer des milliers d'applications d'apprentissage automatique créées par la communauté, et voir ce qui est tendance et populaire. Vous pouvez également créer vos propres espaces et présenter votre travail au monde.
* Explorez la documentation et les tutoriels de Hugging Face : Si vous souhaitez en savoir plus sur la plateforme Hugging Face et ses fonctionnalités, vous pouvez consulter la documentation et les tutoriels. Ils fournissent des informations détaillées et des conseils sur l'utilisation des outils et ressources que Hugging Face offre. Vous pouvez également trouver des informations sur les tâches courantes de ML/IA, telles que la classification de texte, la génération d'images et la reconnaissance vocale, sur la page des tâches.
* Visitez la section [learn](https://huggingface.co/learn) : Si vous êtes intéressé par l'acquisition de nouvelles compétences et connaissances en IA et TAL, vous pouvez visiter la page 'learn' qui affiche des cours de Hugging Face. Ici, vous pouvez apprendre des experts et des meilleures pratiques du domaine, et les appliquer à vos propres projets.
* Rejoignez la communauté Hugging Face : L'apprentissage automatique est plus amusant en collaborant ! Vous pouvez rejoindre la communauté Hugging Face sur des plateformes comme GitHub, Discord et Twitter pour vous connecter avec d'autres utilisateurs et rester informé des derniers développements. Vous pouvez également partager vos commentaires, questions et idées avec la communauté, et aider Hugging Face à grandir et à s'améliorer.

Hugging Face n'est pas seulement une plateforme pour l'IA et le TAL – c'est aussi un terrain de jeu pour votre curiosité et votre créativité. Vous pouvez expérimenter de nouveaux modèles, élargir vos connaissances en IA et enrichir votre boîte à outils d'IA avec divers outils et ressources. Alors, continuez à apprendre, continuez à explorer. Il y a toujours quelque chose de nouveau et d'excitant à découvrir avec Hugging Face. 😊