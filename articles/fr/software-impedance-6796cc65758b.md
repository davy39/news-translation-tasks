---
title: L'impédance logicielle expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-07T22:10:27.000Z'
originalURL: https://freecodecamp.org/news/software-impedance-6796cc65758b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8GFgF4KqixGeYwqcExmbjg.png
tags:
- name: Batch Processing
  slug: batch-processing
- name: General Programming
  slug: programming
- name: Signal Processing
  slug: signal-processing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: L'impédance logicielle expliquée
seo_desc: 'By Milan Mimica

  The impedance mismatch between data processing components


  It all starts with the simplest signal-processing diagram ever:


  Component A is passing the signal to component B. Let’s switch to software engineering
  jargon immediately: A p...'
---

Par Milan Mimica

#### Le désaccord d'impédance entre les composants de traitement de données

![Image](https://cdn-media-1.freecodecamp.org/images/sRwHZwN9J3U4vil9jWIkjayd65oGcKzKutpu)

Tout commence avec le diagramme de traitement de signal le plus simple jamais conçu :

![Image](https://cdn-media-1.freecodecamp.org/images/nzzHsg3xL9DOOfkcN47d9rmjuX2Vj4GakPlF)

Le composant A transmet le signal au composant B. Passons immédiatement au jargon de l'ingénierie logicielle : un producteur invoque une méthode d'un consommateur. Invoquer une méthode prend un temps fini. Nous appelons cela le temps de réponse ou la _latence_. Le producteur peut transmettre une quantité arbitraire (mais limitée) de données à chaque invocation de méthode. Nous appelons cela la _taille de lot_. Le niveau de concurrence est une autre variable avec laquelle nous pouvons jouer. Le producteur peut contrôler le nombre d'invocations concurrentes en limitant la _taille de fenêtre_ des réponses en attente. Invoquer la méthode de manière concurrente multiplie effectivement le débit. Le débit (T) est une fonction de la taille de fenêtre (W), de la taille de lot (B) et de la latence (t).

![Image](https://cdn-media-1.freecodecamp.org/images/DGlIiCyr6ZzXjHEPYYdwadfYBDIZFq7wXnv5)

Nous visons un débit maximal, donc nous augmentons la concurrence et utilisons des tailles de lot plus grandes. Si seulement ! Le temps de réponse dépend de la taille de lot et de la taille de fenêtre. Pour le dire plus formellement, le temps de réponse est une fonction à la fois de la taille de fenêtre et de la taille de lot.

![Image](https://cdn-media-1.freecodecamp.org/images/bS5mNpTz-h2fAZj5gfjYhMNJW-y9WFpLlbJX)

Pour atteindre un débit maximal, nous devons trouver les valeurs les plus élevées de _W_ et _B_ qui produisent la plus faible _t_. Des valeurs non idéales de _W_ et _B_ induiront une "résistance" plus élevée dans le composant, ou appelez cela une _contre-pression_ si vous préférez.

> Qu'il produise les données ou qu'il les transmette simplement, un producteur doit adapter la taille de fenêtre et la taille de lot pour mieux convenir au consommateur. Sinon, nous avons ce que j'appelle un désaccord d'impédance logicielle.

Il n'existe pas d'expression générique pour f(W, B), car cela dépend de l'implémentation du composant. La théorie n'est d'aucune aide ici. Vous devez sonder le consommateur avec différentes tailles de lot et de fenêtre pour repérer les valeurs idéales qui maximiseront le débit.

Une fois que vous avez trouvé la taille de lot idéale, vous devez construire un "adaptateur d'impédance". Voici une implémentation Java suggérée qui accumule les éléments et les regroupe avant de les envoyer au composant suivant (beaucoup de code passe-partout omis pour plus de concision).

Notez que l'invocation du consommateur avec une taille de lot inférieure à la taille maximale (idéale) est toujours autorisée. Cela garantit qu'aucune latence supplémentaire n'est ajoutée. Si la taille de lot sélectionnée est optimale, en supposant un flux régulier d'éléments, l'invocation du consommateur prendra exactement le temps nécessaire pour remplir _maxBatchSize_ éléments dans la file d'attente.

De même, le nombre d'invocations de méthode concurrentes vers une instance de consommateur peut être contrôlé à l'aide d'un sémaphore.

#### Mode Push vs. Pull

Le scénario ci-dessus décrit le mode "push", dans lequel le composant producteur contrôle l'invocation, son timing et les paramètres clés mentionnés. Une approche plus moderne pour gérer la contre-pression consiste à mettre le composant consommateur en charge de l'invocation. Cela place le concepteur du système dans une position légèrement meilleure, car les ingénieurs du composant consommateur n'ont pas besoin de communiquer la taille de lot et de fenêtre aux producteurs. Néanmoins, un adaptateur d'impédance similaire est nécessaire.

#### Conclusion

Les adaptateurs d'impédance sont des composants étatiques, composés de files d'attente, de threads, de cartes de rappel, etc., ce qui ajoute de la complexité, mais l'adaptation de l'impédance est essentielle dans la communication inter-composants.

Je soutiens que chaque composant devrait spécifier ses paramètres d'impédance : taille de lot optimale et niveau de concurrence. Ainsi, les composants producteurs peuvent s'adapter pour minimiser la contre-pression.

Contrairement à l'impédance électrique, l'impédance dans le logiciel n'est pas limitée à deux dimensions. Ici, je ne montre que deux paramètres, mais souvent le temps de réponse dépend également d'autres variables.

L'impédance est une propriété très dynamique. Elle peut dépendre des données envoyées, de la charge de travail globale, parfois même de variables non contrôlées par l'appelant. Si nécessaire, l'API du consommateur devrait être conçue de manière à permettre au composant de publier ses derniers paramètres d'impédance via l'API. Ainsi, les producteurs pourraient s'adapter dynamiquement.