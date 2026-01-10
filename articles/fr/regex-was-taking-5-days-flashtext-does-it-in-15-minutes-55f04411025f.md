---
title: Regex prenait 5 jours pour s'exécuter. J'ai donc construit un outil qui l'a
  fait en 15 minutes.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-08T19:40:48.000Z'
originalURL: https://freecodecamp.org/news/regex-was-taking-5-days-flashtext-does-it-in-15-minutes-55f04411025f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QvHXLlSAuPZsQTycvcv9bQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Regex prenait 5 jours pour s'exécuter. J'ai donc construit un outil qui
  l'a fait en 15 minutes.
seo_desc: 'By Vikash Singh

  When developers work with text, they often need to clean it up first. Sometimes
  it’s by replacing keywords. Like replacing “Javascript” with “JavaScript”. Other
  times, we just want to find out whether “JavaScript” was mentioned in a d...'
---

Par Vikash Singh

Lorsque les développeurs travaillent avec du texte, ils doivent souvent le nettoyer d'abord. Parfois, c'est en remplaçant des mots-clés. Comme remplacer « Javascript » par « JavaScript ». D'autres fois, nous voulons simplement savoir si « JavaScript » a été mentionné dans un document.

Les tâches de nettoyage de données comme celles-ci sont standard pour la plupart des projets de science des données traitant du texte.

### **La science des données commence par le nettoyage des données.**

J'ai eu une tâche très similaire à travailler récemment. Je travaille en tant que scientifique des données chez [Belong.co](https://belong.co/) et le traitement du langage naturel fait partie de mon travail.

Lorsque j'ai entraîné un modèle [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) sur notre corpus de documents, il a commencé à donner des synonymes comme termes similaires. « Javascripting » apparaissait comme un terme similaire à « JavaScript ».

Pour résoudre cela, j'ai écrit une expression régulière (Regex) pour remplacer tous les synonymes connus par des noms standardisés. La Regex a remplacé « Javascripting » par « JavaScript », ce qui a résolu 1 problème mais en a créé un autre.

> Certaines personnes, lorsqu'elles sont confrontées à un problème, pensent
> « Je sais, j'utiliserai des expressions régulières. » Maintenant, elles ont deux problèmes.

La citation ci-dessus provient de cette [question stack-exchange](https://softwareengineering.stackexchange.com/questions/223634/what-is-meant-by-now-you-have-two-problems) et elle s'est avérée vraie pour moi.

Il s'avère que Regex est rapide si le nombre de mots-clés à rechercher et à remplacer est de l'ordre de la centaine. Mais mon corpus contenait plus de 20 000 mots-clés et 3 millions de documents.

Lorsque j'ai évalué mon code Regex, j'ai constaté qu'il allait prendre **5 jours** pour compléter une exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GpNMd7fBtrH4TvVZRglfNg.jpeg)
_oh l'horreur_

La solution naturelle était de l'exécuter en parallèle. Mais cela n'aidera pas lorsque nous atteindrons des dizaines de millions de documents et des centaines de milliers de mots-clés. **Il devait y avoir une meilleure façon !** Et j'ai commencé à la chercher...

J'ai demandé autour de moi dans mon bureau et sur Stack Overflow — quelques suggestions sont apparues. [Vinay Pandey](https://www.linkedin.com/in/vinay-pande-54810813/), [Suresh Lakshmanan](https://www.linkedin.com/in/suresh-lakshmanan/) et [Stack Overflow](https://stackoverflow.com/questions/44178449/regex-replace-is-taking-time-for-millions-of-documents-how-to-make-it-faster) ont pointé vers le bel algorithme appelé [algorithme d'Aho-Corasick](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm) et l'approche de la [structure de données Trie](https://en.wikipedia.org/wiki/Trie). J'ai cherché des solutions existantes mais je n'ai pas trouvé grand-chose.

J'ai donc écrit ma propre implémentation et [FlashText](https://github.com/vi3k6i5/flashtext) est né.

Avant de voir ce qu'est FlashText et comment il fonctionne, examinons ses performances pour la recherche :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WMgrVJmoke7ZIyYSuReEjw.png)
_Ligne rouge en bas est le temps pris par FlashText pour la recherche_

Le graphique montré ci-dessus est une comparaison de Regex compilé contre FlashText pour 1 document. À mesure que le nombre de mots-clés augmente, le temps pris par Regex croît presque linéairement. Pourtant, avec FlashText, cela n'a pas d'importance.

#### **FlashText a réduit notre temps d'exécution de 5 jours à 15 minutes !!**

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZfRhHGtxhbEB0dS-3BHOAw.png)
_nous sommes bons maintenant :)_

Voici le temps d'exécution de FlashText pour le remplacement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*doXUZk_bYVVvNf7O3JIQSw.png)
_Ligne rouge en bas est le temps pris par FlashText pour le remplacement_

Le code utilisé pour le benchmark montré ci-dessus est lié [ici](https://gist.github.com/vi3k6i5/dc3335ee46ab9f650b19885e8ade6c7a), et les résultats sont liés [ici](https://goo.gl/wWCyyw).

### **Alors, qu'est-ce que FlashText ?**

FlashText est une bibliothèque Python que j'ai open sourcée sur [GitHub](https://github.com/vi3k6i5). Elle est efficace à la fois pour extraire des mots-clés et les remplacer.

Pour utiliser FlashText, vous devez d'abord lui passer une liste de mots-clés. Cette liste sera utilisée en interne pour construire un dictionnaire Trie. Ensuite, vous lui passez une chaîne de caractères et vous lui indiquez si vous souhaitez effectuer un remplacement ou une recherche.

Pour le `**remplacement**`, il créera une nouvelle chaîne avec les mots-clés remplacés. Pour la `**recherche**`, il retournera une liste des mots-clés trouvés dans la chaîne. Tout cela se fera en un seul passage sur la chaîne d'entrée.

Voici ce qu'un utilisateur satisfait avait à dire sur la bibliothèque :

### Pourquoi FlashText est-il si rapide ?

Essayons de comprendre cette partie avec un exemple. Supposons que nous avons une phrase qui contient 3 mots `J'aime Python`, et un corpus qui contient 4 mots `{Python, Java, J2ee, Ruby}`.

Si nous prenons chaque mot du corpus et vérifions s'il est présent dans la phrase, cela prendra 4 essais.

```
'est-ce que 'Python' est dans la phrase ? est-ce que 'Java' est dans la phrase ?...
```

Si le corpus avait `n` mots, cela aurait pris `n` boucles. De plus, chaque étape de recherche `est-ce que <mot> est dans la phrase ?` prendra son propre temps. C'est un peu ce qui se passe dans la correspondance Regex.

Il existe une autre approche qui est l'inverse de la première. Pour chaque mot dans la phrase, vérifiez s'il est présent dans le corpus.

```
'est-ce que 'Je' est dans le corpus ? est-ce que 'aime' est dans le corpus ? est-ce que 'python' est dans le corpus ?
```

Si la phrase avait `m` mots, cela aurait pris `m` boucles. Dans ce cas, le temps qu'il faut dépend uniquement du nombre de mots dans la phrase. Et cette étape, `est-ce que <mot> est dans le corpus ?` peut être rendue rapide en utilisant une recherche dans un dictionnaire.

L'algorithme FlashText est basé sur la deuxième approche. Il est inspiré par l'algorithme d'Aho-Corasick et la structure de données Trie.

La façon dont il fonctionne est :
D'abord, un dictionnaire Trie est créé avec le corpus. Il ressemblera à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*N09Y_XEQFhFMxVpgEeqExQ.png)
_Dictionnaire Trie du corpus._

Start et EOT (End Of Term) représentent les limites de mots comme `espace`, `point` et `nouvelle ligne`. Un mot-clé ne correspondra que s'il a des limites de mots des deux côtés. Cela empêchera la correspondance de apple dans pomme.

Ensuite, nous prendrons une chaîne d'entrée `J'aime Python` et la rechercherons caractère par caractère.

```
Étape 1 : est-ce que <start>J<EOT> est dans le dictionnaire ? NonÉtape 2 : est-ce que <start>aime<EOT> est dans le dictionnaire ? NonÉtape 3 : est-ce que <start>Python<EOT> est dans le dictionnaire ? Oui
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*noWWci3fCrbcbrj40B4UaA.png)
_&lt;Start&gt; Python &lt;EOT&gt; est présent dans le dictionnaire._

Puisque cela correspond caractère par caractère, nous pourrions facilement sauter `<start>aim`e<`;EOT>` à <d`é`but>l car l n'est `pas` connecté à start. Cela rend le saut des mots manquants vraiment rapide.

L'algorithme FlashText n'a parcouru chaque caractère de la chaîne d'entrée « J'aime Python » qu'une seule fois. Le dictionnaire aurait très bien pu contenir un million de mots-clés, sans impact sur le temps d'exécution. C'est la véritable puissance de l'algorithme FlashText.

### Alors, quand devriez-vous utiliser FlashText ?

Réponse simple : Lorsque le nombre de mots-clés > 500

![Image](https://cdn-media-1.freecodecamp.org/images/1*_wjTfRdsnLKGnbr4VJ4Xqw.png)
_Pour la recherche, FlashText commence à surpasser Regex après ~ 500 mots-clés._

Réponse compliquée : Regex peut rechercher des mots-clés basés sur des caractères spéciaux comme `^,$,*,\d,.` qui ne sont pas supportés dans FlashText.

Donc, ce n'est pas bon si vous voulez faire correspondre des mots partiels comme ``word\dvec``. Mais il est excellent pour extraire des mots complets comme ``word2vec``.

### FlashText pour trouver des mots-clés

### **FlashText pour remplacer des mots-clés**

Au lieu d'extraire des mots-clés, vous pouvez également remplacer des mots-clés dans des phrases. Nous utilisons cela comme une étape de nettoyage des données dans notre pipeline de traitement des données.

Si vous connaissez quelqu'un qui travaille avec des données textuelles, la reconnaissance d'entités, le traitement du langage naturel ou Word2vec, envisagez de partager ce blog avec eux.

Cette bibliothèque nous a été vraiment utile, et je suis sûr qu'elle serait utile pour les autres aussi.

Au revoir, et merci pour tous les applaudissements ?