---
title: Tout ce que vous devez savoir sur le prétraitement de texte pour le NLP et
  le Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-23T21:20:45.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-about-text-preprocessing-for-nlp-and-machine-learning-bc1c5765ff67
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NRzVPEOl9NkpP9Ug3Nmh6w.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Tout ce que vous devez savoir sur le prétraitement de texte pour le NLP
  et le Machine Learning
seo_desc: 'By Kavita Ganesan

  Based on some recent conversations, I realized that text preprocessing is a severely
  overlooked topic. A few people I spoke to mentioned inconsistent results from their
  NLP applications only to realize that they were not preprocessi...'
---

Par Kavita Ganesan

D'après certaines conversations récentes, j'ai réalisé que le prétraitement de texte est un sujet gravement négligé. Quelques personnes à qui j'ai parlé ont mentionné des résultats incohérents de leurs applications NLP pour se rendre compte qu'elles ne prétraitaient pas leur texte ou utilisaient le mauvais type de prétraitement de texte pour leur projet.

Avec cela en tête, j'ai pensé éclairer ce qu'est vraiment le prétraitement de texte, les différentes méthodes de prétraitement de texte, et une façon d'estimer combien de prétraitement vous pourriez avoir besoin. Pour ceux qui sont intéressés, j'ai également fait quelques [extraits de code de prétraitement de texte](https://github.com/kavgan/nlp-text-mining-working-examples/tree/master/text-pre-processing) pour que vous puissiez essayer. Maintenant, commençons !

### Qu'est-ce que le prétraitement de texte ?

Prétraiter votre texte signifie simplement amener votre texte sous une forme qui est **_prévisible_** et **_analysable_** pour votre tâche. Une tâche ici est une combinaison d'approche et de domaine. Par exemple, extraire les mots-clés principaux avec tfidf (approche) à partir de Tweets (domaine) est un exemple de _Tâche_.

> _Tâche = approche + domaine_

Le prétraitement idéal pour une tâche peut devenir le pire cauchemar pour une autre tâche. Donc, notez bien : le prétraitement de texte n'est pas directement transférable d'une tâche à une autre.

Prenons un exemple très simple, disons que vous essayez de découvrir les mots couramment utilisés dans un ensemble de données de nouvelles. Si votre étape de prétraitement implique la suppression des [mots vides](http://kavita-ganesan.com/what-are-stop-words/) parce qu'une autre tâche les a utilisés, alors vous risquez de manquer certains des mots courants car vous les avez DÉJÀ éliminés. Donc, ce n'est vraiment pas une approche universelle.

### Types de techniques de prétraitement de texte

Il existe différentes façons de prétraiter votre texte. Voici quelques-unes des approches que vous devriez connaître et j'essaierai de souligner l'importance de chacune.

#### Mise en minuscules

Mettre en minuscules TOUTES vos données textuelles, bien que souvent négligé, est l'une des formes les plus simples et les plus efficaces de prétraitement de texte. Elle est applicable à la plupart des problèmes de fouille de texte et de NLP et peut aider dans les cas où votre ensemble de données n'est pas très grand et aide considérablement à la cohérence du résultat attendu.

Très récemment, l'un de mes lecteurs de blog a entraîné un [modèle de plongement de mots pour des recherches de similarité](http://kavita-ganesan.com/gensim-word2vec-tutorial-starter-code/). Il a découvert que différentes variations de capitalisation d'entrée (par exemple, 'Canada' vs. 'canada') lui donnaient différents types de résultats ou aucun résultat du tout. Cela se produisait probablement parce que l'ensemble de données contenait des occurrences en casse mixte du mot 'Canada' et il n'y avait pas assez de preuves pour que le réseau de neurones apprenne efficacement les poids pour la version moins courante. Ce type de problème est susceptible de se produire lorsque votre ensemble de données est assez petit, et la mise en minuscules est un excellent moyen de traiter les problèmes de rareté.

Voici un exemple de la façon dont la mise en minuscules résout le problème de rareté, où les mêmes mots avec des casse différentes sont mappés à la même forme minuscule :

![Image](https://cdn-media-1.freecodecamp.org/images/fIH6CiCkfUMOYwNF8JVFluNOlofSf0MIoogQ)
_Mot avec différentes casse mappé à la même forme **minuscule**_

Un autre exemple où la mise en minuscules est très utile est pour la recherche. Imaginez, vous cherchez des documents contenant 'usa'. Cependant, aucun résultat n'apparaissait parce que 'usa' était indexé comme **'USA'**. Maintenant, qui devons-nous blâmer ? Le concepteur U.I. qui a configuré l'interface ou l'ingénieur qui a configuré l'index de recherche ?

Bien que la mise en minuscules devrait être une pratique standard, j'ai également eu des situations où la préservation de la casse était importante. Par exemple, dans la prédiction du langage de programmation d'un fichier de code source. Le mot `System` en Java est assez différent de `system` en python. La mise en minuscules des deux les rend identiques, ce qui fait que le classificateur perd des caractéristiques prédictives importantes. Bien que la mise en minuscules _soit généralement_ utile, elle peut ne pas être applicable à toutes les tâches.

#### Racinisation

La racinisation est le processus de réduction des inflexions dans les mots (par exemple, troubled, troubles) à leur forme racine (par exemple, trouble). La 'racine' dans ce cas peut ne pas être un mot racine réel, mais simplement une forme canonique du mot original.

La racinisation utilise un processus heuristique brut qui coupe les fins des mots dans l'espoir de transformer correctement les mots en leur forme racine. Ainsi, les mots 'trouble', 'troubled' et 'troubles' pourraient en fait être convertis en `troubl` au lieu de `trouble` parce que les fins ont simplement été coupées (ughh, comme c'est brut !).

Il existe différents algorithmes pour la racinisation. L'algorithme le plus courant, qui est également connu pour être empiriquement efficace pour l'anglais, est [l'algorithme de Porter](https://tartarus.org/martin/PorterStemmer/). Voici un exemple de racinisation en action avec Porter Stemmer :

![Image](https://cdn-media-1.freecodecamp.org/images/7t5CB5HnVD33SL4b2oJMuSk6JIsSRRnlFVzs)
_Effets de la racinisation des mots fléchis_

La racinisation est utile pour traiter les problèmes de rareté ainsi que pour standardiser le vocabulaire. J'ai eu du succès avec la racinisation dans les applications de recherche en particulier. L'idée est que, si par exemple vous recherchez 'deep learning classes', vous voulez également faire apparaître des documents qui mentionnent 'deep learning **_class_**' ainsi que 'deep **_learn_** classes', bien que ce dernier ne semble pas correct. Mais vous voyez où nous voulons en venir. Vous voulez faire correspondre toutes les variations d'un mot pour faire apparaître les documents les plus pertinents.

Dans la plupart de mes travaux précédents de classification de texte, cependant, la racinisation n'a aidé que marginalement à améliorer la précision de la classification par rapport à l'utilisation de caractéristiques mieux conçues et d'approches d'enrichissement de texte telles que l'utilisation de plongements de mots.

#### Lemmatisation

La lemmatisation, en surface, est très similaire à la racinisation, où le but est de supprimer les inflexions et de mapper un mot à sa forme racine. La seule différence est que la lemmatisation essaie de le faire de la bonne manière. Elle ne coupe pas simplement les choses, elle transforme réellement les mots en leur racine réelle. Par exemple, le mot 'better' serait mappé à 'good'. Elle peut utiliser un dictionnaire tel que [WordNet pour les mappings](https://www.nltk.org/_modules/nltk/stem/wordnet.html) ou certaines approches spéciales [basées sur des règles](https://www.semanticscholar.org/paper/A-Rule-based-Approach-to-Word-Lemmatization-Plisson-Lavrac/5319539616e81b02637b1bf90fb667ca2066cf14). Voici un exemple de lemmatisation en action utilisant une approche basée sur WordNet :

![Image](https://cdn-media-1.freecodecamp.org/images/7QIjtgIQuFNzmIuQSIRDDnTVXc3IEG-PMvbc)
_Effets de la Lemmatisation avec WordNet_

Dans mon expérience, la lemmatisation ne fournit aucun avantage significatif par rapport à la racinisation pour les recherches et les classifications de texte. En fait, selon l'algorithme que vous choisissez, elle pourrait être beaucoup plus lente par rapport à l'utilisation d'un racinisateur très basique et vous pourriez avoir besoin de connaître la partie du discours du mot en question afin d'obtenir un lemme correct. [Cet article](https://arxiv.org/pdf/1707.01780.pdf) constate que la lemmatisation n'a pas d'impact significatif sur la précision pour la classification de texte avec des architectures neuronales.

J'utiliserais personnellement la lemmatisation avec parcimonie. Le surcoût supplémentaire peut ou non en valoir la peine. Mais vous pourriez toujours l'essayer pour voir l'impact qu'elle a sur votre métrique de performance.

#### Suppression des mots vides

Les mots vides sont un ensemble de mots couramment utilisés dans une langue. Des exemples de mots vides en anglais sont 'a', 'the', 'is', 'are' et etc. L'intuition derrière l'utilisation des mots vides est que, en supprimant les mots à faible information du texte, nous pouvons nous concentrer sur les mots importants à la place.

Par exemple, dans le contexte d'un système de recherche, si votre requête de recherche est '_what is text preprocessing?_', vous voulez que le système de recherche se concentre sur les documents qui parlent de `text preprocessing` plutôt que sur les documents qui parlent de `what is`. Cela peut être fait en empêchant tous les mots de votre liste de mots vides d'être analysés. Les mots vides sont couramment appliqués dans les systèmes de recherche, les applications de classification de texte, la modélisation de sujets, l'extraction de sujets et autres.

Dans mon expérience, la suppression des mots vides, bien qu'efficace dans les systèmes de recherche et d'extraction de sujets, s'est avérée non critique dans les systèmes de classification. Cependant, cela aide à réduire le nombre de caractéristiques à considérer, ce qui aide à garder vos modèles de taille décente.

Voici un exemple de suppression de mots vides en action. Tous les mots vides sont remplacés par un caractère factice, **W** :

![Image](https://cdn-media-1.freecodecamp.org/images/KKCwQyjH3XQGPMdSQfPfpM7gWxhVoYTpy1n7)
_Phrase avant et après la suppression des mots vides_

[Les listes de mots vides](http://kavita-ganesan.com/what-are-stop-words/) peuvent provenir d'ensembles préétablis ou vous pouvez créer [une liste personnalisée pour votre domaine](http://kavita-ganesan.com/tips-for-constructing-custom-stop-word-lists/). Certaines bibliothèques (par exemple, sklearn) vous permettent de supprimer les mots qui sont apparus dans X% de vos documents, ce qui peut également vous donner un effet de suppression de mots vides.

#### Normalisation

Une étape de prétraitement souvent négligée est la normalisation du texte. La normalisation du texte est le processus de transformation d'un texte en une forme canonique (standard). Par exemple, le mot 'gooood' et 'gud' peuvent être transformés en 'good', leur forme canonique. Un autre exemple est le mappage de mots presque identiques tels que 'stopwords', 'stop-words' et 'stop words' à simplement 'stopwords'.

La normalisation du texte est importante pour les textes bruyants tels que les commentaires sur les réseaux sociaux, les messages texte et les commentaires des articles de blog où les abréviations, les fautes d'orthographe et l'utilisation de mots hors vocabulaire (oov) sont répandues. [Cet article](https://sentic.net/microtext-normalization.pdf) a montré qu'en utilisant une stratégie de normalisation de texte pour les Tweets, ils ont pu améliorer la précision de la classification des sentiments d'environ 4%.

Voici un exemple de mots avant et après la normalisation :

![Image](https://cdn-media-1.freecodecamp.org/images/GMcUWMp77cqScgAyPoEtz4IO7Nefdsi6uU--)
_Effets de la Normalisation de Texte_

Remarquez comment les variations sont mappées à la même forme canonique.

Dans mon expérience, la normalisation de texte a même été efficace pour analyser [des textes cliniques très non structurés](http://kavita-ganesan.com/general-supervised-approach-segmentation-clinical-texts/) où les médecins prennent des notes de manière non standard. Je l'ai également trouvé utile pour [l'extraction de sujets](https://githubengineering.com/topics/) où les quasi-synonymes et les différences d'orthographe sont courants (par exemple, topic modelling, topic modeling, topic-modeling, topic-modelling).

Malheureusement, contrairement à la racinisation et à la lemmatisation, il n'existe pas de méthode standard pour normaliser les textes. Cela dépend généralement de la tâche. Par exemple, la façon dont vous normaliseriez les textes cliniques serait probablement différente de la façon dont vous normaliseriez les messages SMS.

Certaines approches courantes de normalisation de texte incluent les mappages de dictionnaire (les plus faciles), la traduction automatique statistique (SMT) et les approches basées sur la correction d'orthographe. [Cet article intéressant](https://nlp.stanford.edu/courses/cs224n/2009/fp/27.pdf) compare l'utilisation d'une approche basée sur un dictionnaire et d'une approche SMT pour normaliser les messages texte.

#### Suppression du bruit

La suppression du bruit consiste à supprimer les `caractères`, `chiffres` et `morceaux de texte` qui peuvent interférer avec votre analyse de texte. La suppression du bruit est l'une des étapes de prétraitement de texte les plus essentielles. Elle dépend également fortement du domaine.

Par exemple, dans les Tweets, le bruit pourrait être tous les caractères spéciaux sauf les hashtags car ils signifient des concepts qui peuvent caractériser un Tweet. Le problème avec le bruit est qu'il peut produire des résultats incohérents dans vos tâches en aval. Prenons l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/dJ9OMBBZUZwqJXjnUo6XHSIxNogICNRFEwN1)
_Racinisation **sans** Suppression du Bruit_

Remarquez que tous les mots bruts ci-dessus contiennent un certain bruit environnant. Si vous racinisez ces mots, vous pouvez voir que le résultat racinisé ne semble pas très joli. Aucun d'entre eux n'a une racine correcte. Cependant, avec un peu de nettoyage comme appliqué dans [ce notebook](https://github.com/kavgan/nlp-text-mining-working-examples/blob/master/text-pre-processing/Text%20Pre-Processing%20Examples.ipynb), les résultats semblent maintenant beaucoup mieux :

![Image](https://cdn-media-1.freecodecamp.org/images/mF046Lr37QZpSJdH5T8ZAp6WR0fzlJsy9YQA)
_Racinisation **avec** Suppression du Bruit_

La suppression du bruit est l'une des premières choses que vous devriez examiner en matière de fouille de texte et de NLP. Il existe diverses façons de supprimer le bruit. Cela inclut la _suppression de la ponctuation_, la _suppression des caractères spéciaux_, la _suppression des nombres_, la _suppression du formatage html_, la _suppression des mots-clés spécifiques au domaine_ (par exemple, 'RT' pour retweet), la suppression du code source, la suppression des en-têtes et plus encore. Tout dépend du domaine dans lequel vous travaillez et de ce qui constitue le bruit pour votre tâche. Le [fragment de code dans mon notebook](https://github.com/kavgan/nlp-text-mining-working-examples/tree/master/text-pre-processing) montre comment effectuer une suppression de bruit de base.

#### Enrichissement / Augmentation de texte

L'enrichissement de texte consiste à augmenter vos données textuelles originales avec des informations que vous n'aviez pas auparavant. L'enrichissement de texte apporte plus de sémantique à votre texte original, améliorant ainsi son pouvoir prédictif et la profondeur de l'analyse que vous pouvez effectuer sur vos données.

Dans un exemple de récupération d'informations, l'expansion d'une requête utilisateur pour améliorer la correspondance des mots-clés est une forme d'augmentation. Une requête comme `text mining` pourrait devenir `text document mining analysis`. Bien que cela n'ait pas de sens pour un humain, cela peut aider à récupérer des documents plus pertinents.

Vous pouvez être très créatif dans la façon dont vous enrichissez votre texte. Vous pouvez utiliser le [**balisage des parties du discours**](https://en.wikipedia.org/wiki/Part-of-speech_tagging) pour obtenir des informations plus granulaires sur les mots de votre texte.

Par exemple, dans un problème de classification de documents, l'apparition du mot **book** en tant que **nom** pourrait entraîner une classification différente de **book** en tant que **verbe**, car l'un est utilisé dans le contexte de la lecture et l'autre dans le contexte de la réservation de quelque chose. [Cet article](http://www.iapr-tc11.org/archive/icdar2011/fileup/PDF/4520a920.pdf) parle de la façon dont la classification de texte chinois est améliorée avec une combinaison de noms et de verbes comme caractéristiques d'entrée.

Avec la disponibilité de grandes quantités de textes, les gens ont commencé à utiliser des [plongements](https://en.wikipedia.org/wiki/Word_embedding) pour enrichir le sens des mots, des phrases et des phrases pour la classification, la recherche, la synthèse et la génération de texte en général. Cela est particulièrement vrai dans les approches NLP basées sur l'apprentissage profond où une [couche de plongement au niveau des mots](https://keras.io/layers/embeddings/) est assez courante. Vous pouvez soit commencer avec des [plongements préétablis](https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html) ou créer les vôtres et les utiliser dans des tâches en aval.

D'autres façons d'enrichir vos données textuelles incluent [l'extraction de phrases](http://kavita-ganesan.com/how-to-incorporate-phrases-into-word2vec-a-text-mining-approach/#.XHCcJ1xKg2w), où vous reconnaissez les mots composés comme un seul (aka chunking), [l'expansion avec des synonymes](http://aclweb.org/anthology/R09-1073) et [l'analyse des dépendances](http://www.cs.virginia.edu/~kc2wc/teaching/NLP16/slides/15-DP.pdf).

### Avez-vous besoin de tout cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/B2WRW-0jW3kLQd-FwUGd15e9rrb1EiHSY6lp)

Pas vraiment, mais vous devez en faire certaines si vous voulez des résultats bons et cohérents. Pour vous donner une idée de ce que devrait être le minimum, je l'ai divisé en **_Doit Faire_**, **_Devrait Faire_** et **_Dépendant de la Tâche_**. Tout ce qui relève de la tâche dépendante peut être testé quantitativement ou qualitativement avant de décider si vous en avez vraiment besoin.

Rappelez-vous, moins c'est plus et vous voulez garder votre approche aussi élégante que possible. Plus vous ajoutez de surcoût, plus vous aurez de couches à peler lorsque vous rencontrerez des problèmes.

### Doit Faire :

* Suppression du bruit
* Mise en minuscules (peut être dépendante de la tâche dans certains cas)

### Devrait Faire :

* Normalisation simple — (par exemple, standardiser les mots presque identiques)

### Dépendant de la Tâche :

1. Normalisation avancée (par exemple, traitement des mots hors vocabulaire)
2. Suppression des mots vides
3. Racinisation / lemmatisation
4. Enrichissement / augmentation de texte

Donc, pour toute tâche, le minimum que vous devriez faire est d'essayer de mettre en minuscules votre texte et de supprimer le bruit. Ce qui constitue le bruit dépend de votre domaine (voir la section sur la suppression du bruit). Vous pouvez également effectuer quelques étapes de normalisation de base pour plus de cohérence, puis ajouter systématiquement d'autres couches selon vos besoins.

### Règle générale

Toutes les tâches n'ont pas besoin du même niveau de prétraitement. Pour certaines tâches, vous pouvez vous en tirer avec le minimum. Cependant, pour d'autres, l'ensemble de données est si bruyant que, si vous ne prétraitez pas suffisamment, ce sera du garbage-in-garbage-out.

Voici une règle générale. Cela ne sera pas toujours vrai, mais cela fonctionne pour la plupart des cas. Si vous avez beaucoup de textes bien écrits à travailler dans un domaine assez général, alors le prétraitement n'est pas extrêmement critique ; vous pouvez vous en tirer avec le minimum (par exemple, entraîner un modèle de plongement de mots en utilisant tous les textes de Wikipedia ou les articles de Reuters).

Cependant, si vous travaillez dans un domaine très étroit (par exemple, les Tweets sur les aliments santé) et que les données sont rares et bruyantes, vous pourriez bénéficier de plus de couches de prétraitement, bien que chaque couche que vous ajoutez (par exemple, suppression des mots vides, racinisation, normalisation) doive être vérifiée quantitativement ou qualitativement comme une couche significative. Voici un tableau qui résume combien de prétraitement vous devriez effectuer sur vos données textuelles :

![Image](https://cdn-media-1.freecodecamp.org/images/wR-bjpHRJObby8HZOPlV3Art2knhypDmeO9g)

J'espère que les idées ici vous orientent vers les bonnes étapes de prétraitement pour vos projets. Rappelez-vous, _moins c'est plus_. Un ami m'a mentionné un jour comment il a rendu un grand système de recherche e-commerce plus efficace et moins bogué simplement en supprimant des couches de prétraitement _inutiles_.

### Ressources

* [Code Python pour le prétraitement de texte de base utilisant NLTK et regex](https://github.com/kavgan/nlp-text-mining-working-examples/blob/master/text-pre-processing/Text%20Preprocessing%20Examples.ipynb)
* [Construction de listes de mots vides personnalisées](http://kavita-ganesan.com/tips-for-constructing-custom-stop-word-lists/)
* [Code source pour l'extraction de phrases](https://kavgan.github.io/phrase-at-scale/)

### Références

* Pour une liste mise à jour d'articles, veuillez consulter [mon article original](http://kavita-ganesan.com/text-preprocessing-tutorial/#Relevant-Papers)

[**_Suivez mon blog_**](http://kavita-ganesan.com/subscribe/#.XHmu_5NKhuV) **_pour continuer à apprendre sur la fouille de texte, le NLP et le Machine Learning d'un point de vue appliqué._**

**_Cet article est initialement paru sur [kavita-ganesan.com](http://kavita-ganesan.com/text-preprocessing-tutorial/#.XIbdHJNKhhE)_**