---
title: Comment j'ai utilisé l'apprentissage automatique pour explorer les différences
  entre la littérature britannique et américaine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-13T13:58:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-differentiate-between-british-and-american-literature-being-a-machine-learning-engineer-ac842662da1c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qjL1gt3ru64goK8PYlTjVw.jpeg
tags:
- name: books
  slug: books
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: writing
  slug: writing
seo_title: Comment j'ai utilisé l'apprentissage automatique pour explorer les différences
  entre la littérature britannique et américaine
seo_desc: 'By Sofia Godovykh

  As I delved further into English literature to further my own language gains, my
  interest was piqued: how do American and British English differ?

  With this question framed in my mind, the next steps were to apply natural language
  pr...'
---

Par Sofia Godovykh

Alors que je m'immergeais davantage dans la littérature anglaise pour améliorer mes propres compétences linguistiques, mon intérêt a été piqué : comment l'anglais américain et britannique diffèrent-ils ?

Avec cette question en tête, les prochaines étapes ont été d'appliquer des techniques de traitement du langage naturel et d'apprentissage automatique pour trouver des exemples concrets. J'étais curieuse de savoir s'il serait possible d'entraîner un classificateur, qui distinguerait les textes littéraires.

Il est assez facile de distinguer les textes écrits dans différentes langues puisque la cardinalité de l'intersection des mots (caractéristiques, en termes d'apprentissage automatique) était relativement faible. La classification de textes par catégorie (comme la science, l'athéisme, l'infographie, etc.) est un « hello world » bien connu lorsqu'il s'agit de tâches liées à la classification de textes. J'ai été confrontée à une tâche plus difficile lorsque j'ai essayé de comparer deux dialectes de la même langue, car les textes n'ont pas de thème commun.

L'étape la plus chronophage de l'apprentissage automatique concerne la récupération des données. Pour l'échantillon d'entraînement, j'ai utilisé des textes du Projet Gutenberg, qui peuvent être téléchargés librement. Quant à la liste des auteurs américains et britanniques, j'ai utilisé les noms d'auteurs que j'ai trouvés sur Wikipedia.

L'un des défis que j'ai rencontrés a été de trouver le nom de l'auteur d'un texte qui correspondait à la page Wikipedia. Une bonne recherche par nom était implémentée sur le site, mais comme le site n'autorise pas l'analyse des données, j'ai plutôt proposé d'utiliser des fichiers qui contenaient des métadonnées. Cela signifiait que je devais résoudre une tâche non triviale de correspondance des noms (Sir Arthur Ignatius Conan Doyle et Doyle, C. sont la même personne, mais Doyle, M.E. est une personne différente) — et je devais le faire avec un très haut niveau de précision.

Au lieu de cela, j'ai choisi de sacrifier la taille de l'échantillon pour le bien de l'obtention d'une grande précision, ainsi que pour économiser du temps. J'ai choisi, comme identifiant unique, le lien Wikipedia d'un auteur, qui était inclus dans certains des fichiers de métadonnées. Avec ces fichiers, j'ai pu acquérir environ 1 600 textes britanniques et 2 500 textes américains et les utiliser pour commencer l'entraînement de mon classificateur.

Pour ce projet, j'ai utilisé le package sklearn. La première étape après la collecte et l'analyse des données est le prétraitement, dans lequel j'ai utilisé un CountVectorizer. Un CountVectorizer prend des données textuelles en entrée et retourne un vecteur de caractéristiques en sortie. Ensuite, j'ai dû calculer le **tf-idf** (fréquence de terme — fréquence inverse de document). Une brève explication de pourquoi j'ai dû l'utiliser et comment :

Par exemple, prenons le mot « the » et comptons le nombre d'occurrences du mot dans un texte donné, A. Supposons que nous avons 100 occurrences, et le nombre total de mots dans un document est de 1000.

Ainsi,

`tf("the") = 100/1000 = 0.1`

Ensuite, prenons le mot « sepal », qui est apparu 50 fois :

`tf("sepal") = 50/1000 = 0.05`

Pour calculer la fréquence inverse de document pour ces mots, nous devons prendre le logarithme du rapport du nombre de textes à partir desquels il y a au moins une occurrence du mot, au nombre total de textes. Si nous avons 10 000 textes, et dans chacun, il y a le mot « the » :

`idf("the") = log(10000/10000) = 0` et

`tf-idf("the") = idf("the") * tf("the") = 0 * 0.1 = 0`

Le mot « sepal » est bien plus rare, et n'a été trouvé que dans 5 textes. Par conséquent :

`idf("sepal") = log(10000/5) et tf-idf("sepal") = 7.6 * 0.05 = 0.38`

Ainsi, les mots les plus fréquents portent moins de poids, et les mots spécifiques et plus rares en portent davantage. Si il y a de nombreuses occurrences du mot « sepal », nous pouvons supposer que c'est un texte botanique. Nous ne pouvons pas alimenter un classificateur avec des mots, nous utiliserons la mesure tf-idf à la place.

Après avoir présenté les données sous forme d'un ensemble de caractéristiques, j'ai dû entraîner le classificateur. Je travaillais avec des données textuelles, qui sont présentées sous forme de données clairsemées, donc la meilleure option est d'utiliser un classificateur linéaire, qui fonctionne bien avec de grandes quantités de caractéristiques.

Tout d'abord, j'ai exécuté le CountVectorizer, TF-IDFTransformer et SGDClassifier en utilisant les paramètres par défaut. En analysant le graphique de la précision de la taille de l'échantillon — où la précision fluctuait de 0,6 à 0,85 — j'ai découvert que le classificateur dépendait beaucoup de l'échantillon particulier utilisé, et donc n'était pas très efficace.

Après avoir reçu une liste des poids du classificateur, j'ai remarqué une partie du problème : le classificateur avait été alimenté avec des mots comme « of » et « he », que nous aurions dû traiter comme du bruit. J'ai facilement pu résoudre ce problème en supprimant ces mots des caractéristiques en définissant le paramètre `stop_words` du CountVectorizer : `stop_words = 'english'` (ou votre propre liste personnalisée de mots vides).

Avec les mots vides par défaut supprimés, j'ai obtenu une précision de 0,85. Après cela, j'ai lancé la sélection automatique des paramètres en utilisant GridSearchCV et j'ai atteint une précision finale de 0,89. Je pourrais peut-être améliorer ce résultat avec un échantillon d'entraînement plus grand, mais pour l'instant, je suis restée avec ce classificateur.

Maintenant, ce qui m'intéresse le plus : quels mots indiquent l'origine du texte ? Voici une liste de mots, triés par ordre décroissant de poids dans le classificateur :

**Américain :** dollars, new, york, girl, gray, american, carvel, color, city, ain, long, just, parlor, boston, honor, washington, home, labor, got, finally, maybe, hodder, forever, dorothy, dr

**Britannique :** round, sir, lady, london, quite, mr, shall, lord, grey, dear, honour, having, philip, poor, pounds, scrooge, soames, things, sea, man, end, come, colour, illustration, english, learnt

En m'amusant avec le classificateur, j'ai pu identifier les auteurs britanniques les plus « américains » et les auteurs américains les plus « britanniques » (une manière astucieuse de voir à quel point mon classificateur pouvait mal fonctionner).

**Les Américains les plus « britanniques » :**

* Frances Hodgson Burnett (née en Angleterre, déménagée aux États-Unis à l'âge de 17 ans, donc je la considère comme une écrivaine américaine)
* Henry James (né aux États-Unis, déménagé en Angleterre à l'âge de 33 ans)
* Owen Wister (oui, le père de la fiction western)
* Mary Roberts Rinehart (appelée l'Agatha Christie américaine pour une raison)
* William McFee (un autre écrivain déménagé en Amérique à un jeune âge)

**Les Britanniques les plus « américains » :**

* Rudyard Kipling (il a vécu en Amérique pendant plusieurs années, aussi, il a écrit « American Notes »)
* Anthony Trollope (l'auteur de « North America »)
* Frederick Marryat (Un vétéran de la guerre anglo-américaine de 1812, grâce à son « Narrative of the Travels and Adventures of Monsieur Violet in California, Sonara, and Western Texas » qui l'a fait tomber dans la catégorie américaine)
* Arnold Bennett (l'auteur de « Your United States: Impressions of a first visit » un autre gentleman a écrit des notes de voyage)
* E. Phillips Oppenheim

Et aussi les auteurs les plus « britanniques » britanniques et les plus « américains » américains (parce que le classificateur fonctionne toujours bien) :

**Américains :**

* Francis Hopkinson Smith
* Hamlin Garland
* George Ade
* Charles Dudley Warner
* Mark Twain

**Britanniques :**

* George Meredith
* Samuel Richardson
* John Galsworthy
* Gilbert Keith Chesterton
* Anthony Trollope (oh, salut)

J'ai été inspirée pour faire ce travail par le tweet de @TragicAllyHere :

Eh bien, les mots comptent vraiment, comme je l'ai réalisé.