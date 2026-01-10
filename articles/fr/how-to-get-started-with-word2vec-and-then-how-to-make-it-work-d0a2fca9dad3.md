---
title: Comment commencer avec Word2Vec — et ensuite comment le faire fonctionner
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-19T15:31:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-word2vec-and-then-how-to-make-it-work-d0a2fca9dad3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h4xBoeeDRdRkiPLGuQxUgQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment commencer avec Word2Vec — et ensuite comment le faire fonctionner
seo_desc: 'By Kavita Ganesan

  The idea behind Word2Vec is pretty simple. We’re making an assumption that the meaning
  of a word can be inferred by the company it keeps. This is analogous to the saying,
  “show me your friends, and I’ll tell who you are.”

  If you hav...'
---

Par Kavita Ganesan

L'idée derrière Word2Vec est assez simple. Nous faisons l'hypothèse que **le sens d'un mot peut être déduit par la compagnie qu'il fréquent.** Cela est analogue au dicton, « montre-moi tes amis, et je te dirai qui tu es. »

Si vous avez deux mots qui ont des voisins très similaires (signification : le contexte dans lequel ils sont utilisés est à peu près le même), alors ces mots sont probablement assez similaires en signification ou au moins liés. Par exemple, les mots _choqué_, _indigné_ et _étonné_ sont généralement utilisés dans un contexte similaire.

En utilisant cette hypothèse sous-jacente, vous pouvez utiliser Word2Vec pour découvrir des concepts similaires, trouver des concepts non liés, calculer la similarité entre deux mots, et plus encore !

### Passons aux choses sérieuses

Dans ce tutoriel, vous apprendrez à utiliser l'implémentation Gensim de Word2Vec et à le faire fonctionner réellement. J'ai longtemps entendu des plaintes sur les performances médiocres en général, mais cela est vraiment une combinaison de deux choses : **(1) vos données d'entrée** et **(2) vos paramètres**.

Notez que les algorithmes d'entraînement dans le package Gensim ont été portés de l'implémentation originale [Word2Vec par Google](https://arxiv.org/pdf/1301.3781.pdf) et étendus avec des fonctionnalités supplémentaires.

### Imports et journalisation

Tout d'abord, nous commençons avec nos imports et établissons la journalisation :

```
# imports nécessaires et journalisationimport gzipimport gensim import logging
```

```
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
```

### Ensemble de données

Notre prochaine tâche est de trouver un très bon ensemble de données. Le secret pour faire fonctionner Word2Vec pour vous est d'avoir beaucoup de données textuelles dans le domaine pertinent. Par exemple, si votre objectif est de construire un lexique de sentiment, alors utiliser un ensemble de données du domaine médical ou même de Wikipedia peut ne pas être efficace. Donc, choisissez votre ensemble de données avec sagesse.

Pour ce tutoriel, je vais utiliser des données de l'ensemble de données [OpinRank](http://kavita-ganesan.com/entity-ranking-data/) de certains de mes travaux de [doctorat](http://kavita-ganesan.com/opinion-based-entity-ranking/). Cet ensemble de données contient des critiques complètes d'utilisateurs sur des voitures et des hôtels. J'ai spécifiquement rassemblé toutes les critiques d'hôtels dans un seul grand fichier qui fait environ **97 Mo** compressé et **229 Mo** décompressé. Nous utiliserons le fichier compressé pour ce tutoriel. Chaque ligne de ce fichier représente une critique d'hôtel.

Maintenant, examinons de plus près ces données en imprimant la première ligne.

Vous devriez voir ce qui suit :

```
b"Oct 12 2009 \tNice trendy hotel location not too bad.\tI stayed in this hotel for one night. As this is a fairly new place some of the taxi drivers did not know where it was and/or did not want to drive there. Once I have eventually arrived at the hotel, I was very pleasantly surprised with the decor of the lobby/ground floor area. It was very stylish and modern. I found the reception's staff geeting me with 'Aloha' a bit out of place, but I guess they are briefed to say that to keep up the coroporate image.As I have a Starwood Preferred Guest member, I was given a small gift upon-check in. It was only a couple of fridge magnets in a gift box, but nevertheless a nice gesture.My room was nice and roomy, there are tea and coffee facilities in each room and you get two complimentary bottles of water plus some toiletries by 'bliss'.The location is not great. It is at the last metro stop and you then need to take a taxi, but if you are not planning on going to see the historic sites in Beijing, then you will be ok.I chose to have some breakfast in the hotel, which was really tasty and there was a good selection of dishes. There are a couple of computers to use in the communal area, as well as a pool table. There is also a small swimming pool and a gym area.I would definitely stay in this hotel again, but only if I did not plan to travel to central Beijing, as it can take a long time. The location is ok if you plan to do a lot of shopping, as there is a big shopping centre just few minutes away from the hotel and there are plenty of eating options around, including restaurants that serve a dog meat!\t\r\n"
```

Vous pouvez voir que c'est une critique assez complète avec beaucoup de mots et c'est ce que nous voulons. Nous avons environ 255 000 critiques de ce type dans cet ensemble de données.

Pour éviter toute confusion, le tutoriel Word2Vec de Gensim indique que vous devez passer une séquence de phrases en entrée à Word2Vec. Cependant, vous pouvez en fait passer une critique entière comme une phrase (c'est-à-dire une taille de texte beaucoup plus grande) si vous avez beaucoup de données et cela ne devrait pas faire une grande différence. En fin de compte, tout ce que nous utilisons l'ensemble de données pour est d'obtenir tous les mots voisins pour un mot cible donné.

### Lire les fichiers dans une liste

Maintenant que nous avons eu un aperçu de notre ensemble de données, nous pouvons le lire dans une liste afin de pouvoir le passer au modèle Word2Vec. Remarquez dans le code ci-dessous que je lis directement le fichier compressé. Je fais également un léger prétraitement des critiques en utilisant `gensim.utils.simple_preprocess(line)`. Cela fait un prétraitement de base tel que la tokenisation, la mise en minuscules, etc., et retourne une liste de tokens (mots). La documentation de cette méthode de prétraitement peut être trouvée sur le site officiel de la [documentation Gensim](https://radimrehurek.com/gensim/utils.html).

### Entraînement du modèle Word2Vec

L'entraînement du modèle est assez simple. Vous instanciez simplement Word2Vec et passez les critiques que nous avons lues à l'étape précédente. Nous passons donc essentiellement une liste de listes, où chaque liste dans la liste principale contient un ensemble de tokens d'une critique d'utilisateur. Word2Vec utilise tous ces tokens pour créer en interne un vocabulaire. Et par vocabulaire, j'entends un ensemble de mots uniques.

Après avoir construit le vocabulaire, nous devons simplement appeler `train(...)` pour commencer l'entraînement du modèle Word2Vec. En coulisses, nous entraînons en fait un simple réseau de neurones avec une seule couche cachée. Mais nous n'allons pas utiliser le réseau de neurones après l'entraînement. Au lieu de cela, le but est d'apprendre les poids de la couche cachée. Ces poids sont essentiellement les vecteurs de mots que nous essayons d'apprendre.

L'entraînement sur l'ensemble de données [Word2Vec OpinRank](https://github.com/kavgan/data-science/tree/master/word2vec) prend environ 10 à 15 minutes. Donc, veuillez être patient pendant l'exécution de votre code sur cet ensemble de données.

### La partie amusante — quelques résultats !

![Image](https://cdn-media-1.freecodecamp.org/images/1*s55bWApJm-OM6nWa9YZRQw.jpeg)

Passons déjà aux choses amusantes ! Puisque nous nous sommes entraînés sur des critiques d'utilisateurs, il serait bien de voir la similarité sur certains adjectifs. Ce premier exemple montre une simple recherche de mots similaires au mot 'sale'. Tout ce que nous devons faire ici est d'appeler la fonction `most_similar` et de fournir le mot 'sale' comme exemple positif. Cela retourne les 10 mots similaires les plus proches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mhFUguFBoAng8x1_AFqAzw.png)
_**Mots similaires à 'sale'**_

Ooh, cela semble assez bien. Regardons plus.

Similaires à _poli_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hDry7c8gyLVLX1GqXe9Ejw.png)
_**Mots similaires à 'poli'**_

Similaires à _france_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*m9AZmudvSoCy3m251JqNUQ.png)
_**Mots similaires à 'France'**_

Similaires à _choqué_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kc1hgr4oT1vLvvhmmNOGpQ.png)
_**Mots similaires à 'choqué'**_

Dans l'ensemble, les résultats ont en fait du sens. Tous les mots liés tendent à être utilisés dans le même contexte pour le mot de requête donné.

Maintenant, vous pourriez même utiliser Word2Vec pour calculer la similarité entre deux mots du vocabulaire en invoquant la fonction `similarity(...)` et en passant les mots pertinents.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f8WbL9IBegLzrVBtIgQ9TA.png)
_**Calculer la similarité entre deux mots du vocabulaire**_

Sous le capot, les trois extraits ci-dessus calculent la similarité cosinus entre les deux mots spécifiés en utilisant les vecteurs de mots de chacun. D'après les scores ci-dessus, il est logique que `sale` soit très similaire à `malodorant` mais que `sale` soit dissemblable à `propre`. Si vous faites une similarité entre deux mots identiques, le score sera de 1,0 car la plage du score de similarité cosinus sera toujours comprise entre [0,0-1,0]. Vous pouvez en savoir plus sur le score de similarité cosinus [ici](https://en.wikipedia.org/wiki/Cosine_similarity).

Vous trouverez plus d'exemples sur la façon dont vous pourriez utiliser Word2Vec dans mon [Jupyter Notebook](https://github.com/kavgan/data-science/blob/master/word2vec/Word2Vec.ipynb).

### Un regard plus attentif sur les paramètres

![Image](https://cdn-media-1.freecodecamp.org/images/1*3tAxNGPEol7rW4IhhA2GAA.jpeg)

Pour entraîner le modèle plus tôt, nous avons dû définir certains paramètres. Maintenant, essayons de comprendre ce que certains d'entre eux signifient. Pour référence, voici la commande que nous avons utilisée pour entraîner le modèle.

```
model = gensim.models.Word2Vec (documents, size=150, window=10, min_count=2, workers=10)
```

#### `size`

La taille du vecteur dense qui doit représenter chaque token ou mot. Si vous avez très peu de données, alors la taille doit être une valeur beaucoup plus petite. Si vous avez beaucoup de données, il est bon d'expérimenter avec diverses tailles. Une valeur de 100 à 150 a bien fonctionné pour moi pour les recherches de similarité.

#### `window`

La distance maximale entre le mot cible et son mot voisin. Si la position de votre voisin est supérieure à la largeur de fenêtre maximale à gauche ou à droite, alors certains voisins ne sont pas considérés comme étant liés au mot cible. En théorie, une fenêtre plus petite devrait vous donner des termes plus liés. Si vous avez beaucoup de données, alors la taille de la fenêtre ne devrait pas trop importer, tant qu'elle n'est pas trop étroite ou trop large. Si vous n'êtes pas trop sûr de cela, utilisez simplement la valeur par défaut.

#### `min_count`

Fréquence minimale des mots. Le modèle ignorerait les mots qui ne satisfont pas le `min_count`. Les mots extrêmement peu fréquents sont généralement sans importance, il est donc préférable de s'en débarrasser. À moins que votre ensemble de données soit vraiment minuscule, cela n'affecte pas vraiment le modèle.

#### `workers`

Combien de threads utiliser en coulisses ?

### Quand devriez-vous utiliser Word2Vec ?

Il existe de nombreux scénarios d'application pour Word2Vec. Imaginez si vous devez construire un lexique de sentiment. L'entraînement d'un modèle Word2Vec sur de grandes quantités de critiques d'utilisateurs vous aide à atteindre cet objectif. Vous avez un lexique non seulement pour le sentiment, mais pour la plupart des mots du vocabulaire.

Au-delà des données textuelles brutes non structurées, vous pourriez également utiliser Word2Vec pour des données plus structurées. Par exemple, si vous aviez des tags pour un million de questions et réponses StackOverflow, vous pourriez trouver des tags liés et les recommander pour exploration. Vous pouvez faire cela en traitant chaque ensemble de tags co-occurrents comme une « phrase » et entraîner un modèle Word2Vec sur ces données. Certes, vous avez toujours besoin d'un grand nombre d'exemples pour que cela fonctionne.

### Code source

Pour utiliser le Jupyter Notebook de ce tutoriel, vous pouvez aller à mon [dépôt GitHub](https://github.com/kavgan/data-science/tree/master/word2vec) et suivre les instructions sur la façon de faire fonctionner le notebook localement. Je prévois de télécharger les vecteurs pré-entraînés qui pourraient être utilisés pour votre propre travail.

**_Pour suivre les articles de Kavita par e-mail, veuillez [vous abonner à son blog](http://kavita-ganesan.com/subscribe/#.XGs_lpNKigQ)._**  
**_Cet article a été publié à l'origine sur [kavita-ganesan.com](http://kavita-ganesan.com/gensim-word2vec-tutorial-starter-code/#.XGtAZJNKigQ)_**