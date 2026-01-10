---
title: Conseils rapides pour construire des listes de mots vides personnalisées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T19:54:51.000Z'
originalURL: https://freecodecamp.org/news/quick-tips-for-constructing-custom-stop-word-lists-c22b40a25169
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eAdqKoWkI9p3NnQdx94yHw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: nlp
  slug: nlp
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: text mining
  slug: text-mining
seo_title: Conseils rapides pour construire des listes de mots vides personnalisées
seo_desc: 'By Kavita Ganesan

  In natural language processing (NLP) and text mining applications, stop words are
  used to eliminate unimportant words, allowing applications to focus on the important
  words instead.

  Stop words are a set of commonly used words in any...'
---

Par Kavita Ganesan

Dans les applications de traitement du langage naturel (NLP) et de fouille de texte, les mots vides sont utilisés pour éliminer les mots non importants, permettant aux applications de se concentrer sur les mots importants à la place.

Les mots vides sont un ensemble de mots couramment utilisés dans n'importe quelle langue. Par exemple, en anglais, « the », « is » et « and » seraient facilement qualifiés de mots vides.

Bien qu'il existe diverses listes de mots vides publiées que l'on peut utiliser, dans de nombreux cas, ces mots vides sont insuffisants car ils ne sont pas spécifiques à un domaine. Par exemple, dans les textes cliniques, des termes comme « mcg », « dr. » et « patient » apparaissent dans presque tous les documents que vous rencontrez. Ainsi, ces termes peuvent être considérés comme des mots vides potentiels pour la fouille de texte et la récupération de textes cliniques.

De même, pour les tweets, des termes comme « # », « RT », « @username » peuvent être potentiellement considérés comme des mots vides. La liste commune des mots vides spécifiques à une langue ne couvre généralement **pas** de tels termes spécifiques à un domaine.

La bonne nouvelle est qu'il est en réalité assez facile de construire votre propre liste de mots vides spécifique à un domaine. Voici quelques façons de procéder en supposant que vous disposez d'un grand corpus de texte dans le domaine d'intérêt, vous pouvez faire une ou plusieurs des actions suivantes pour créer votre liste de mots vides :

### 1. Les termes les plus fréquents comme mots vides

Sommez les fréquences de termes de chaque mot unique (**w**) dans tous les documents de votre collection. Triez les termes par ordre décroissant de fréquence brute des termes. Vous pouvez prendre les **K** premiers termes comme mots vides.

Vous pouvez également éliminer les mots anglais courants (en utilisant une liste de mots vides publiée) avant le tri afin de cibler les mots vides spécifiques au domaine.

Une autre option consiste à traiter les mots apparaissant dans plus de **X%** de vos documents comme des mots vides. J'ai trouvé que l'élimination des mots qui apparaissent dans **85%** des documents est efficace dans plusieurs tâches de fouille de texte. L'avantage de cette approche est qu'elle est vraiment facile à mettre en œuvre. L'inconvénient, cependant, est que si vous avez un document particulièrement long, la fréquence brute des termes de seulement quelques documents peut dominer et faire que le terme se retrouve en tête. Une façon de résoudre cela est de normaliser la fréquence brute des termes en utilisant un normalisateur tel que la longueur du document — le nombre de mots dans un document donné.

### 2. Les termes les moins fréquents comme mots vides

Tout comme les termes extrêmement fréquents pourraient être des termes distracteurs plutôt que des termes discriminants, les termes extrêmement peu fréquents peuvent également ne pas être utiles pour la fouille de texte et la récupération. Par exemple, le nom d'utilisateur « @username » qui n'apparaît qu'une seule fois dans une collection de tweets peut ne pas être très utile. D'autres termes comme « yoMateZ! » qui pourraient simplement être des termes inventés par des personnes peuvent à nouveau ne pas être utiles pour les applications de fouille de texte.

**Note** : certains termes comme « yaaaaayy!! » peuvent souvent être normalisés en formes standard telles que « yay ».

Cependant, malgré toute la normalisation, si un terme a toujours un compte de fréquence de un, vous pouvez le supprimer. Cela pourrait réduire significativement votre espace de caractéristiques global.

### 3. Les termes à faible IDF comme mots vides

La [fréquence inverse de document (IDF)](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) fait référence à la fraction inverse de documents dans votre collection qui contient un terme spécifique (**ti**). Supposons que :

* vous avez **N** documents
* le terme **ti** est apparu dans **M** des **N** documents.

L'IDF de **ti** est ainsi calculé comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PABvj4Re2EypV6zjzLkjIg.png)

Ainsi, plus le terme **ti** apparaît dans de documents, plus le score **IDF** est bas. Cela signifie que les termes qui apparaissent dans tous les documents auront un score IDF de 0.

Si vous classez chaque **ti** dans votre collection par son score IDF par ordre décroissant, vous pouvez traiter les **K** derniers termes avec les scores **IDF les plus bas** comme vos mots vides.

Encore une fois, vous pouvez également éliminer les mots anglais courants en utilisant une liste de mots vides publiée avant le tri afin de cibler les **mots à faible IDF spécifiques au domaine**. Cela n'est pas nécessaire si votre **K** est suffisamment grand pour qu'il élimine à la fois les mots vides généraux ainsi que les mots vides spécifiques au domaine. Vous trouverez plus d'informations sur les IDF [ici](http://kavita-ganesan.com/text-mining-cheat-sheet/#.W1olu9hKids).

### Alors, les mots vides aideraient-ils ma tâche ?

Comment savoir si la suppression des mots vides spécifiques à un domaine serait utile dans votre cas ? Facile — testez-le sur un sous-ensemble de vos données. Voyez si la mesure de précision et de performance s'améliore, reste constante ou se dégrade. Si elle se dégrade, il va sans dire, ne le faites pas sauf si la dégradation est négligeable et que vous voyez des gains sous d'autres formes telles qu'une diminution de la taille du modèle, ou la capacité à traiter les choses en mémoire.