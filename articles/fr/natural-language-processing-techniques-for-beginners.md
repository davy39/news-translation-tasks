---
title: Tutoriel NLP – Techniques de prétraitement de texte pour débutants
subtitle: ''
author: Crypt(iq)
co_authors: []
series: null
date: '2023-07-12T14:31:24.000Z'
originalURL: https://freecodecamp.org/news/natural-language-processing-techniques-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/NLP-6.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
seo_title: Tutoriel NLP – Techniques de prétraitement de texte pour débutants
seo_desc: Natural Language Processing (NLP) is a branch of Machine learning (ML) that
  is focused on making computers understand the human language. It is used to create
  language models, language translation apps like Google translate, and virtual assistants,
  a...
---

Le traitement du langage naturel (NLP) est une branche de l'apprentissage automatique (ML) qui se concentre sur la compréhension du langage humain par les ordinateurs. Il est utilisé pour créer des modèles de langage, des applications de traduction comme Google Translate et des assistants virtuels, entre autres.

Cet article vous guide à travers l'une des étapes les plus basiques du NLP, qui est le prétraitement de texte. C'est un sujet incontournable pour toute personne intéressée par les modèles de langage et le NLP en général, qui est une partie centrale du domaine de l'intelligence artificielle (IA) et du ML.

## Qu'est-ce que le prétraitement de texte ?

Le prétraitement de texte est le processus de transformation de texte non structuré en texte structuré pour le préparer à l'analyse.

Lorsque vous prétraitez le texte avant de le fournir aux algorithmes, vous augmentez la précision et l'efficacité de ces algorithmes en supprimant le bruit et d'autres incohérences dans le texte qui peuvent rendre difficile la compréhension par l'ordinateur.

Rendre le texte plus facile à comprendre aide également à réduire le temps et les ressources nécessaires pour que l'ordinateur prétraite les données.

## Processus impliqués dans le prétraitement de texte

Pour prétraiter correctement votre texte et le mettre dans le bon état pour effectuer des analyses et des actions supplémentaires, il y a plusieurs opérations à effectuer sur le texte et quelques étapes à suivre pour obtenir un texte bien structuré.

Passons en revue ces processus dans les sous-sections suivantes.

### Tokenisation

La tokenisation est la première étape du processus.

Ici, votre texte est analysé puis divisé en morceaux appelés « tokens » qui peuvent être des mots ou des phrases. Cela permet à l'ordinateur de travailler sur votre texte token par token plutôt que sur l'ensemble du texte dans les étapes suivantes.

Les deux principaux types de tokenisation sont la tokenisation de mots et la tokenisation de phrases.

La **tokenisation de mots** est le type de tokenisation le plus courant.

Ici, chaque token est un mot, ce qui signifie que l'algorithme décompose l'ensemble du texte en mots individuels :

```python
text = 'Wisdoms daughter walks alone. The mark of Athena burns through rome'

words = text.split()
print(words)

#le résultat de ceci est donné ci-dessous
>>>> ['Wisdoms', 'daughter', 'walks', 'alone.', 'The', 'mark', 'of', 'Athena', 'burns', 'through', 'rome']
```

D'autre part, la **tokenisation de phrases** décompose le texte en phrases au lieu de mots. C'est un type de tokenisation moins courant, utilisé uniquement dans quelques tâches de traitement du langage naturel (NLP).

Il existe divers algorithmes de tokenisation tels que la tokenisation par espaces blancs, la tokenisation par expressions régulières (également appelée Regex) et la tokenisation statistique.

Le type d'algorithme que vous utilisez dépendra de la tâche particulière sur laquelle vous travaillez et de ce que vous visez à accomplir avec celle-ci.

### Normalisation

Dans la normalisation, votre texte est converti en une forme standard.

Un exemple de cela est la conversion de tout le texte en minuscules, la suppression des nombres ou la suppression des ponctuations. La normalisation aide à rendre le texte plus cohérent.

Il existe plusieurs techniques de normalisation différentes, mais je vais vous donner une explication de certaines des techniques de normalisation les plus couramment employées ci-dessous.

#### Normalisation de casse

Cette technique convertit toutes les lettres de votre texte en une seule casse, soit en majuscules, soit en minuscules.

La normalisation de casse garantit que vos données sont stockées dans un format cohérent et facilite le travail avec les données.

Un exemple serait de rechercher toutes les instances d'un mot et de le rechercher dans votre texte. Sans normalisation de casse, le résultat de la recherche du mot « Boy » serait différent du résultat de la recherche de « boy ».

Vous pouvez utiliser le code suivant pour effectuer une normalisation de casse :

```python
text = "'To Sleep Or NOT to SLEep, THAT is THe Question'"

def lower_case(text):
    text = text.lower()
    return text

lower_case = lower_case(text)#convertit tout en minuscules
print(lower_case)

#le résultat de ceci est donné ci-dessous
>>>> to sleep or not to sleep, that is the question
```


#### Racinisation

Des mots comme coding, coder et coded ont tous le même mot de base qui est *code*.

Les modèles de ML comprennent le plus souvent que ces mots sont tous dérivés d'un seul mot de base. Ils peuvent travailler avec votre texte sans les temps, préfixes et suffixes dont nous, en tant qu'humains, aurions normalement besoin pour en comprendre le sens.

La racination de vos textes aide non seulement à réduire le nombre de mots avec lesquels le modèle doit travailler, et par extension améliore l'efficacité du modèle.

Bien que l'efficacité d'un modèle soit augmentée avec cette technique, elle supprime également des informations importantes de votre texte et pourrait amener certains mots à être mal catégorisés par le modèle.

Un exemple de cela serait la différence entre *writing* et *write* dans les phrases ci-dessous :

```

📡 Writing makes me happy.

📡 He writes regularly.

```

Dans la première phrase, le mot *writing* représente un nom, tandis que *writes* dans la deuxième phrase représente un verbe.

Si votre modèle de ML racine à la fois *writing* et *writes* à la base *write*, la différence dans leurs parties de discours respectives est négligée, ce qui entraîne une perte d'informations dans le processus d'analyse du texte.

#### Lemmatisation

Cette méthode est très similaire à la racination en ce sens qu'elle est également utilisée pour identifier la base des mots. Cependant, c'est une technique plus complexe et plus précise que la racination.

Contrairement à la racination, la lemmatisation prend en compte la structure des mots avant d'identifier un mot de base.

En raison de la complexité de cette technique, elle a des exigences computationnelles élevées et est donc plus coûteuse que la racination.


#### Suppression de la ponctuation

Lors des conversations humaines, les marques de ponctuation comme `‘’`, ` !` , `[`, `}`, `*`, ` #`, ` /`, ` ?`, et `‘’` sont incroyablement pertinentes et nécessaires pour avoir une conversation appropriée. Elles aident à transmettre pleinement le message de l'auteur.

Les modèles de ML, en revanche, trouvent les ponctuations distrayantes.

Leur présence pourrait interférer avec l'analyse de texte et le processus de traitement du langage naturel (NLP).

En supprimant les marques de ponctuation de notre texte, nous permettons au modèle de se concentrer sur le texte seul plutôt que de le distraire avec des symboles. Cela facilite l'analyse du texte.

Pour effectuer la suppression de la ponctuation sur du texte, le code suivant peut être utilisé :

```python
import re

text = ' (to love is to destroy, and to be loved, is to be "the" one <destroyed>} '

def remove_punctuations(text):
    punctuation = re.compile(r'[{};():,."/<>-]')
    text = punctuation.sub(' ', text)
    return text

clean_text = remove_punctuations(text)
print(clean_text)

#le résultat de ceci est donné ci-dessous
>>>> to love is to destroy  and to be loved  is to be  the  one  destroyed
```

#### Suppression des accents


Ce processus consiste à supprimer les symboles de caractères spécifiques à une langue du texte.

Certains caractères sont écrits avec des accents ou des symboles spécifiques pour impliquer une prononciation différente ou pour signifier que les mots contenant de tels textes accentués ont une signification différente.

Un exemple de cela serait la différence de signification et de prononciation entre les mots *résumé* et *resume*.

Le premier fait référence à un document qui met en avant vos compétences professionnelles et vos réalisations, tandis que le second signifie « reprendre quelque chose, ou continuer une tâche ou une action précédente ».

Vous pouvez utiliser le code ci-dessous pour effectuer la suppression des accents sur votre texte :

```python
import re

text = "her fiancé's résumé is beautiful"

def remove_accents(text):
    accents = re.compile(u"[\u0300-\u036F]|\u00e9|\u00e8")
    text = accents.sub(u"e", text)
    return text

cleaned_text = remove_accents(text)
print(cleaned_text)

#le résultat de ceci est donné ci-dessous
>>>> her fiance's resume is beautiful
```


#### Suppression des mots vides

Les mots vides sont des mots sans signification. Ils n'ajoutent aucune valeur supplémentaire aux données.

Des mots comme *A, the, and, of* et ainsi de suite sont appelés mots vides.

Comme tous les processus précédents, la suppression des mots vides aide également à augmenter l'efficacité de votre modèle.

Puisqu'elle réduit la taille de notre ensemble de données, elle le rend plus gérable et augmente la précision des tâches de NLP.

## Conclusion

Dans cet article, vous avez appris les bases du NLP.

Vous êtes maintenant familiarisé avec la procédure appropriée à suivre lors du prétraitement de votre texte pour les tâches de NLP. N'hésitez pas à pratiquer cela par vous-même et à travailler sur quelques projets de NLP.

Notez que le choix de la ou des techniques de prétraitement à utiliser sur votre texte dépendra largement du type de texte avec lequel vous travaillez, de la source de vos données et de l'objectif que vous visez à atteindre avec celles-ci.

Pour en savoir plus sur le NLP, vous pouvez consulter [FreeCodeCamp](https://www.freecodecamp.org/news/tag/nlp/) pour plus d'articles et de cours sur le NLP et le ML en général.


Connectez-vous avec moi sur Twitter [@Iqma](https://twitter.com/Iqma__) et suivez [mon blog hashnode](https://iqmacodes.hashnode.dev/) pour lire plus de contenu comme celui-ci et pour en apprendre davantage sur tout ce qui concerne l'IA et l'apprentissage automatique.

Bon apprentissage !