---
title: 'Du texte au sens : comment les ordinateurs comprennent le langage'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-09-30T14:31:13.000Z'
originalURL: https://freecodecamp.org/news/how-computers-understand-language
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/blog_img.jpeg
tags:
- name: natural language processing
  slug: natural-language-processing
seo_title: 'Du texte au sens : comment les ordinateurs comprennent le langage'
seo_desc: 'Language is an intricate dance of words and meanings, a fundamental tool
  for human expression and understanding.

  For centuries, this dance was uniquely human. But with the advent of modern computing,
  a new question emerged: can machines understand ou...'
---

Le langage est une danse complexe de mots et de significations, un outil fondamental pour l'expression et la compréhension humaines.

Pendant des siècles, cette danse était uniquement humaine. Mais avec l'avènement de l'informatique moderne, une nouvelle question a émergé : les machines peuvent-elles comprendre notre langage ?

La réponse, comme beaucoup d'entre nous le savent, est un "oui" retentissant — mais comment font-elles ? Examinons comment le traitement du langage naturel (NLP) aide les ordinateurs à décoder et à extraire le contexte de notre langage.

## Les éléments de base : les tokens

Imaginez lire une phrase.

Pour la comprendre, votre cerveau la décompose, reconnaissant les mots individuels et leurs rôles. Les ordinateurs font quelque chose de similaire appelé tokenisation.

La tokenisation divise un texte en unités plus petites, ou "tokens", qui sont généralement des mots ou des sous-mots. C'est la première étape de l'ordinateur dans le traitement des données textuelles.

Par exemple, la phrase "Les ordinateurs sont intelligents" serait tokenisée en ["Les", "ordinateurs", "sont", "intelligents"].

## Comprendre les formes des mots : Stemming et Lemmatisation

Une fois qu'un ordinateur a tokenisé un texte, il doit comprendre les différentes formes des mots.

Prenons les mots "courant", "coureur" et "couru". Pour nous, ils sont liés. Mais un ordinateur les voit comme des mots séparés. Entrez le stemming et la lemmatisation.

### Stemming

Le stemming simplifie les mots à leur forme fondamentale. Par exemple, dans cet exemple, des variations comme "courant", "coureur" ou "courir" sont toutes réduites à la racine de base, qui est "cour".

Le stemming aide à simplifier les données textuelles, rendant plus facile pour les algorithmes l'analyse et le traitement. Bien qu'il soit utile pour certaines tâches, il est important de noter que le stemming peut parfois conduire à des résultats inexacts, car il peut trop réduire les mots et perdre une partie de leur signification originale.

Pour des tâches plus nuancées, d'autres techniques comme la lemmatisation peuvent être plus appropriées.

### Lemmatisation

La lemmatisation réduit un mot à sa forme de base ou canonique, appelée lemme.

Contrairement au stemming, qui se contente de réduire les mots, la lemmatisation prend en compte le contexte et la signification du mot. Elle garantit que les mots sont transformés en une forme de base valide. Par exemple, le mot "meilleur" pourrait être lemmatisé en "bon", et "courant" serait lemmatisé en "courir".

En utilisant la lemmatisation, nous pouvons regrouper différentes formes d'un mot ensemble afin qu'elles soient traitées comme un seul élément. Cela est utile lors de l'analyse de données textuelles, car cela aide à reconnaître que différentes formes de mots transmettent essentiellement le même concept.

La lemmatisation nécessite souvent plus de ressources computationnelles que le stemming, car elle doit prendre en compte les significations et les structures des mots. Elle dépend également généralement de dictionnaires ou d'outils d'analyse morphologique.

## Comprendre le contexte avec la syntaxe et la sémantique

Les mots interagissent les uns avec les autres, influençant leurs significations en fonction des mots voisins. Pour saisir ce contexte, les ordinateurs analysent à la fois la syntaxe et la sémantique.

Prenons le mot "chauve-souris" comme exemple. Dans la phrase "J'ai joué avec la chauve-souris", "chauve-souris" fait référence à un outil sportif. Cependant, dans la phrase "La chauve-souris a volé dans la nuit", "chauve-souris" indique un mammifère volant.

Grâce à la syntaxe, les ordinateurs déterminent la fonction d'un mot dans une phrase, et avec la sémantique, ils interprètent sa signification exacte donnée cette fonction.

## La puissance des plongements de mots

Les ordinateurs sont excellents avec les nombres, mais moins avec les mots.

Pour combler cette lacune, les mots sont souvent convertis en vecteurs de nombres dans un processus appelé plongement de mots. Ces vecteurs capturent la signification sémantique des mots.

Les mots ayant des significations similaires tendent à avoir des vecteurs similaires. Cette représentation numérique permet aux ordinateurs d'effectuer des opérations mathématiques sur les mots, conduisant à des tâches comme la recherche de similitudes entre mots ou même d'analogies.

J'ai récemment publié un article sur les plongements de mots et vous pouvez [lire l'article complet ici](https://www.freecodecamp.org/news/understanding-word-embeddings-the-building-blocks-of-nlp-and-gpts/).

## La pièce finale : l'apprentissage automatique

Tous les processus ci-dessus alimentent les modèles d'apprentissage automatique.

Ces modèles, formés sur de vastes ensembles de données, utilisent des motifs dans le texte pour faire des déterminations. Les ensembles de données peuvent inclure divers exemples et scénarios, permettant aux modèles d'apprendre et de reconnaître des motifs, des tendances et des relations dans le texte.

Une fois formés, lorsque ces modèles rencontrent de nouvelles informations textuelles, ils les analysent en recherchant des motifs familiers qu'ils ont appris. Par exemple, un texte donné est-il positif ou négatif en sentiment ? Ou un avis déclarant "Le film était captivant" versus "C'était un film ennuyeux à regarder".

Ces modèles peuvent ensuite alimenter des produits comme la traduction linguistique et les transformateurs. Il y a plus d'étapes impliquées dans la décomposition du langage pour le NLP, mais ce sont toutes celles que vous utiliserez presque quotidiennement en tant qu'ingénieur en IA.

## Résumé

Le voyage du texte au sens est complexe, même pour les humains. De la décomposition des phrases à la compréhension du contexte et à l'exploitation de la puissance de l'apprentissage automatique, les ordinateurs ont parcouru un long chemin dans le décryptage du langage humain.

Alors que la technologie continue de progresser, nous pouvons seulement anticiper des interactions encore plus profondes entre les humains et les machines, facilitées par la puissance du traitement du langage naturel.

Si vous avez trouvé cet article intéressant, [rejoignez ma newsletter](https://manishmshiva.com/) et je vous enverrai un email avec mon contenu chaque vendredi.