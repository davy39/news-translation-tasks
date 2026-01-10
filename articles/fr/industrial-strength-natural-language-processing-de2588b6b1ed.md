---
title: Traitement du langage naturel de qualité industrielle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T18:30:49.000Z'
originalURL: https://freecodecamp.org/news/industrial-strength-natural-language-processing-de2588b6b1ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kDvyUe6tJfUu36Q6p2KvTg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Traitement du langage naturel de qualité industrielle
seo_desc: 'By Kavita Ganesan

  I have spent much of my career as a graduate student researcher, and now as a Data
  Scientist in the industry. One thing I have come to realize is that a vast majority
  of solutions proposed both in academic research papers and in the...'
---

Par Kavita Ganesan

J'ai passé une grande partie de ma carrière en tant que chercheuse étudiante diplômée, et maintenant en tant que Data Scientist dans l'industrie. Une chose que j'ai réalisée est qu'une grande majorité des solutions proposées, tant dans les articles de recherche académiques que sur le lieu de travail, ne sont tout simplement pas destinées à être déployées — elles ne sont tout simplement pas scalables !

Et quand je parle de scalabilité, je veux dire :

* Gérer des cas d'utilisation **réels**
* Gérer de **grandes quantités** de données
* Facilité de **déploiement** dans un environnement de production.

Certaines de ces approches fonctionnent soit sur des cas d'utilisation extrêmement étroits, soit ont du mal à générer des résultats en temps opportun.

Plus souvent qu'autrement, le problème réside dans l'approche utilisée, bien que lorsque les choses tournent mal, nous avons tendance à rendre le problème "insoluble". Rappelez-vous, il y aura presque toujours plus d'une façon de résoudre un problème de traitement du langage naturel (NLP) ou de science des données. Optimiser vos choix augmentera vos chances de succès dans le déploiement de vos modèles en production.

Au cours de la dernière décennie, j'ai déployé des solutions qui servent de vrais utilisateurs. Grâce à cette expérience, je suis maintenant un ensemble de bonnes pratiques qui maximise mes chances de succès chaque fois que je commence un nouveau projet NLP.

Dans cet article, je vais partager certaines de ces pratiques avec vous. Je jure par ces principes et j'espère qu'ils vous seront également utiles.

### 1. KISS s'il vous plaît !

![Image](https://cdn-media-1.freecodecamp.org/images/1XNrUYvRw3Ilooemmmyz3J17pu0p41S9vgCS)

[KISS (Keep it simple, stupid)](https://en.wikipedia.org/wiki/KISS_principle). Lorsque vous résolvez des problèmes de NLP, cela semble être du bon sens.

Mais je ne peux pas le dire assez : choisissez des techniques et des pipelines qui sont faciles à comprendre et à maintenir. Évitez les complexes que vous seul comprenez, parfois seulement partiellement.

Dans de nombreuses applications NLP, vous remarquerez typiquement une de ces deux choses :

1. Des couches de pré-traitement profondes, OU
2. Des architectures de réseaux de neurones complexes qui sont simplement difficiles à comprendre, sans parler de les entraîner, les maintenir et les améliorer de manière itérative.

La première question à vous poser est de savoir si vous avez besoin de toutes les couches de pré-traitement ?

Avez-vous vraiment besoin de l'étiquetage des parties du discours, du chunking, de la résolution des entités, de la lemmatisation, etc. Que se passe-t-il si vous supprimez quelques couches ? Comment cela affecte-t-il les performances de vos modèles ?

Avec l'accès à des quantités massives de données, vous pouvez souvent laisser les preuves dans les données guider votre modèle.

Pensez à [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Le succès de Word2Vec réside dans sa simplicité. Vous utilisez de grandes quantités de données pour en tirer du sens — en utilisant les données elles-mêmes. Des couches ? Quelles couches ?

En ce qui concerne le Deep Learning, utilisez-le judicieusement. Tous les problèmes ne bénéficient pas du Deep Learning. Pour les problèmes qui en bénéficient, utilisez les architectures qui sont faciles à comprendre et à améliorer.

Par exemple, pour une tâche de classification de langage de programmation, j'ai simplement utilisé un réseau de neurones artificiels à deux couches et réalisé de grands gains en termes de vitesse d'entraînement et de précision.

De plus, l'ajout d'un nouveau langage de programmation est assez transparent, tant que vous avez des données à alimenter dans le modèle.

J'aurais pu compliquer le modèle pour gagner un peu de capital social en utilisant une architecture RNN vraiment complexe directement issue d'un article de recherche. Mais j'ai fini par commencer simplement pour voir jusqu'où cela me mènerait, et maintenant je suis à un point où je peux dire, quel est le besoin d'ajouter plus de complexité ?

### 2. En cas de doute, utilisez une approche éprouvée

![Image](https://cdn-media-1.freecodecamp.org/images/gLMrdH1IGQKjRssKwsV9p6ymkC53mi4-wfsZ)
_Les choses ne peuvent pas mal tourner avec des approches éprouvées_

Avec chaque problème de NLP/fouille de texte, vos options sont nombreuses. Il y aura toujours plus d'une façon d'accomplir la même tâche.

Par exemple, pour trouver des documents similaires, vous pourriez utiliser une simple approche de sac de mots et calculer les similitudes de documents en utilisant le vecteur [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) résultant.

Alternativement, vous pourriez faire quelque chose de plus fancy en générant des embeddings de chaque document et calculer les similitudes en utilisant les embeddings de documents.

Laquelle devriez-vous utiliser ? Cela dépend en réalité de plusieurs choses :

1. Quelles sont les méthodes qui ont le plus de chances de succès en pratique ? (Indice : Nous voyons tf-idf utilisé tout le temps pour la récupération d'informations et il est super rapide. Comment l'option d'embedding se compare-t-elle ?)
2. Lesquelles de ces méthodes comprenez-vous le mieux ? Rappelez-vous, plus vous comprenez quelque chose, meilleures sont vos chances de le régler et de le faire fonctionner comme vous l'attendez.
3. Avez-vous les outils/données nécessaires pour implémenter l'une de ces méthodes ?

Certaines de ces questions peuvent être facilement répondue avec une recherche dans la littérature.

Mais vous pourriez également contacter des experts tels que des professeurs d'université ou d'autres data scientists qui ont travaillé sur des problèmes similaires pour vous donner une recommandation. Occasionnellement, je fais passer mes idées par mes pairs qui sont dans le même domaine pour m'assurer que je pense aux problèmes et aux solutions potentielles correctement, avant de plonger directement.

À mesure que vous accumulez de plus en plus de projets, le facteur intuition entre en jeu. Vous développerez un sens très fort de ce qui va fonctionner et de ce qui ne va pas fonctionner.

### 3. Comprenez extrêmement bien votre point final

![Image](https://cdn-media-1.freecodecamp.org/images/ynwV1R1197WSvTb0oVgHmPVLhnbaXw9Pm6hE)

Mon travail sur [les sujets pour GitHub](https://githubengineering.com/topics/) a initialement commencé comme des sujets à des fins de recommandations de dépôt. Ces sujets n'auraient jamais été exposés à l'utilisateur. Ils étaient uniquement destinés à être utilisés en interne pour calculer la similarité entre les dépôts.

Pendant le développement, les gens étaient vraiment excités et ont suggéré que ceux-ci devraient être exposés directement aux utilisateurs. Ma réponse immédiate a été "Non, non !". Mais les gens se demandaient, pourquoi pas ?

Très simple, ce n'était pas l'utilisation prévue de ces sujets. Le niveau de tolérance au bruit pour quelque chose que vous utiliseriez uniquement en interne est beaucoup plus élevé que ce que vous montrez aux utilisateurs comme suggestions, externement.

Donc, dans le cas des sujets, j'ai en réalité passé trois mois supplémentaires à améliorer le travail afin qu'il puisse être exposé aux utilisateurs.

Je ne peux pas le dire assez, mais vous devez savoir quel est votre objectif final afin de travailler réellement à fournir une solution qui répond au problème.

Un flou dans l'objectif final que vous essayez d'atteindre peut entraîner soit une **refonte complète**, soit **des mois de travail supplémentaire** pour ajuster et peaufiner vos modèles afin qu'ils fassent la bonne chose.

### 4. Portez une attention particulière à la qualité de vos données

![Image](https://cdn-media-1.freecodecamp.org/images/Q4nrwNbxBOKz1RtKmQETssIbuG01JinLbOzj)

> "Garbage in, garbage out" est vrai dans tous les sens du terme lorsqu'il s'agit de machine learning et de NLP.

Si vous essayez de faire des prédictions de classes de sentiment (positif versus négatif) et que vos exemples positifs contiennent un grand nombre de commentaires négatifs et vice versa, votre classificateur va être confus.

Imaginez si je vous disais `1+2=3` et la fois suivante je vous dis `1+2=4` et la fois suivante je vous dis encore `1+2=3`. Ugh, ne seriez-vous pas si confus ? C'est la même analogie.

De plus, si vous avez 90 % d'exemples positifs et 10 % de négatifs, comment pensez-vous que votre classificateur va performer sur les commentaires négatifs ? Il va probablement dire que chaque commentaire est un commentaire positif.

Le déséquilibre des classes et le manque de diversité dans vos données peuvent être un vrai problème. Plus vos données d'entraînement sont diverses, mieux elles se généraliseront.

Cela était très évident dans l'un de mes projets de recherche sur la [segmentation de texte clinique](http://kavita-ganesan.com/wp-content/uploads/2017/10/stat-segment.pdf). Lorsque nous avons forcé la variété dans les exemples d'entraînement, les résultats se sont clairement améliorés.

Tandis que le sur-traitement de vos données peut être inutile, le sous-traitement peut également être préjudiciable.

Prenons les Tweets par exemple. Les Tweets sont très bruyants. Vous pouvez avoir des mots hors vocabulaire comme `looooooove` et des abréviations comme `lgtm`.

Pour comprendre tout cela, vous devrez probablement ramener ces mots à leur forme normale d'abord. Sans cela, cela tomberait directement dans le piège du garbage-in-garbage-out, surtout si vous traitez un ensemble de données assez petit.

### 5. Ne croyez pas complètement vos résultats quantitatifs.

![Image](https://cdn-media-1.freecodecamp.org/images/9WL1Q3Pbo6EWDT3S67TVGyCixTXB0wzplLQH)
_Doutez de vos résultats quantitatifs_

Les nombres peuvent parfois mentir.

Par exemple, dans un projet de résumé de texte, le chevauchement entre votre résumé de machine learning et le résumé curé par l'homme peut être de 100 %.

Cependant, lorsque vous inspectez visuellement les résumés de la machine et de l'homme, vous pourriez trouver quelque chose d'astonissant.

**L'homme dit** : _"c'est un excellent exemple de mauvais résumé"_.   
**La machine dit** : _"exemple excellent c'est résumé un mauvais un de"_

Et votre score de chevauchement serait toujours de 100 %. Vous voyez mon point ? L'évaluation quantitative seule ne suffit pas !

Vous devez **inspecter visuellement vos résultats** — et beaucoup. Essayez de comprendre intuitivement les problèmes que vous voyez. C'est une excellente façon d'obtenir plus d'idées sur la façon d'ajuster votre algorithme ou de l'abandonner complètement.

Dans l'exemple de résumé, le problème était évident : l'arrangement des mots a besoin de beaucoup de travail !

### 6. Pensez au coût et à la scalabilité.

![Image](https://cdn-media-1.freecodecamp.org/images/rMebIkecS0sr9JV5PbWUU2vl39WEI4uW194o)

Avez-vous déjà pensé à ce qu'il faudrait pour déployer votre modèle dans un environnement de production ?

* Quelles sont vos dépendances de données ?
* Combien de temps votre modèle prend-il pour s'exécuter ?
* Et le temps pour prédire ou générer des résultats ?
* De plus, quelles sont les exigences de mémoire et de calcul de votre approche lorsque vous passez à l'échelle du nombre réel de points de données qu'elle traitera ?

Tous ces facteurs ont un impact direct sur le fait que vous pouvez vous permettre d'utiliser votre approche proposée, et deuxièmement, si vous serez en mesure de gérer une charge de production.

Si votre modèle est lié au GPU, assurez-vous de pouvoir vous permettre le coût de servir un tel modèle.

Plus tôt vous pensez au coût et à la scalabilité, plus vos chances de succès dans le déploiement de vos modèles sont élevées.

Dans mes projets, je mesure toujours le temps pour entraîner, classer et traiter différentes charges pour approximer la performance des solutions que je développe dans un environnement de production.

### En résumé

Les prototypes que vous développez n'ont pas du tout à être des prototypes jetables. Cela peut être le début de solutions vraiment puissantes de niveau production si vous planifiez à l'avance.

Pensez à votre point final et à la manière dont la sortie de votre approche sera consommée et utilisée. Ne compliquez pas trop votre solution. Vous ne vous tromperez pas si vous [KISS](https://en.wikipedia.org/wiki/KISS_principle) et choisissez une technique qui correspond au problème au lieu de forcer votre problème à correspondre à votre technique choisie !

**_J'écris sur la fouille de texte, le NLP et le Machine Learning d'un point de vue appliqué. [Suivez mon blog](http://kavita-ganesan.com/subscribe/#.XGs_lpNKigQ) pour continuer à apprendre._**

**_Cet article a été initialement publié sur [kavita-ganesan.com](http://kavita-ganesan.com/how-to-build-text-mining-and-nlp-models-that-ship-i-e-serve-the-real-world/#.XGs_vJNKigQ)_**