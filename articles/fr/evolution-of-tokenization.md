---
title: L'évolution de la tokenisation – L'encodage par paires d'octets en TAL
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-10-05T15:26:44.000Z'
originalURL: https://freecodecamp.org/news/evolution-of-tokenization
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/IMG_0079.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
- name: Tokenization
  slug: tokenization
seo_title: L'évolution de la tokenisation – L'encodage par paires d'octets en TAL
seo_desc: 'Natural Language Processing may have come a little late to the AI game,
  but companies like Google and OpenAI are working wonders with NLP techniques these
  days.

  These companies have released state-of-the-art language models like BERT and GPT-2
  and GP...'
---

Le traitement automatique du langage naturel (TAL) est peut-être arrivé un peu tard dans le jeu de l'IA, mais des entreprises comme Google et OpenAI font des merveilles avec les techniques de TAL ces jours-ci.

Ces entreprises ont publié des modèles de langage de pointe comme BERT et GPT-2 et GPT-3. Et GitHub Copilot et OpenAI codex font partie des applications populaires qui sont dans l'actualité récemment.

En tant que personne ayant eu très peu d'exposition au TAL, j'ai décidé de m'y intéresser comme domaine de recherche afin d'en apprendre davantage. Mes prochains articles et vidéos se concentreront sur le partage de ce que j'apprends après avoir disséqué certains composants importants du TAL.

### Composants principaux du TAL

Les systèmes de TAL ont trois composants principaux qui aident les machines à comprendre le langage naturel :

1. Tokenisation

2. Plongement (Embedding)

3. Architectures de modèles

Les meilleurs modèles de Deep Learning comme BERT, GPT-2 et GPT-3 partagent tous les mêmes composants mais avec différentes architectures qui distinguent un modèle d'un autre.

Dans cet article (et le [notebook](https://colab.research.google.com/drive/1QLlQx_EjlZzBPsuj_ClrEDC0l8G-JuTn?usp=sharing) qui l'accompagne), nous allons nous concentrer sur les bases du premier composant d'un pipeline TAL qui est la **tokenisation**. C'est un concept souvent négligé, mais c'est un domaine de recherche en soi.

Nous avons parcouru un long chemin depuis le processus de tokenisation traditionnel de NLTK. Et bien que nous ayons des algorithmes de pointe pour la tokenisation, il est toujours bon de comprendre son évolution et comment nous en sommes arrivés là.

Alors, voici ce que nous allons couvrir :

* Qu'est-ce que la tokenisation ?

* Pourquoi avons-nous besoin d'un tokeniseur ?

* Types de tokenisation – Mot, Caractère et Sous-mot.

* Algorithme d'encodage par paires d'octets - une version de celui-ci est utilisée par la plupart des modèles de TAL ces jours-ci.

La prochaine partie de ce tutoriel plongera dans des algorithmes plus avancés (ou des versions améliorées de l'encodage par paires d'octets) :

* **Algorithme Unigramme**

* **WordPiece – Transformateur BERT**

* **SentencePiece – Système de tokenisation de bout en bout**

## Qu'est-ce que la Tokenisation ?

La tokenisation est le processus de représentation de texte brut en unités plus petites appelées tokens. Ces tokens peuvent ensuite être mappés avec des nombres pour être ensuite fournis à un modèle de TAL.

Voici un exemple simplifié de ce que fait un tokeniseur :

```javascript
## lire le texte et énumérer les tokens dans le texte
text = open('example.txt', 'r').read(). # lire un fichier texte

words = text.split(" ") # diviser le texte en espaces

tokens = {v: k for k, v in enumerate(words)} # générer un mappage de mot à index
```

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcaa2e479-181a-4703-afb6-9796d0f74d09_229x327.png align="left")

Ici, nous avons simplement mappé chaque mot dans le texte à un index numérique. Cela est, bien sûr, un exemple très simple et nous n'avons pas considéré la grammaire, la ponctuation ou les mots composés (comme test, test-ify, test-ing, et ainsi de suite).

Nous avons donc besoin d'une définition plus technique et précise de la tokenisation pour notre travail ici. Pour prendre en compte toute la ponctuation et chaque mot apparenté, nous devons commencer à travailler au niveau des caractères.

Il existe de multiples applications de la tokenisation. L'un des cas d'utilisation vient de la conception de compilateurs où vous pourriez avoir besoin d'analyser des programmes informatiques pour convertir des caractères bruts en mots-clés d'un langage de programmation.

**En deep learning**, la tokenisation est le processus de conversion d'une séquence de caractères en une séquence de tokens qui doit ensuite être convertie en une séquence de vecteurs numériques pouvant être traités par un réseau de neurones.

## Pourquoi avons-nous besoin d'un Tokeniseur ?

Le besoin d'un tokeniseur est venu de la question "Comment pouvons-nous faire en sorte que les machines lisent ?"

Une méthode courante de traitement des données textuelles consiste à définir un ensemble de règles dans un dictionnaire, puis à rechercher ce dictionnaire de règles fixe. Mais cette méthode ne peut aller que jusqu'à un certain point, et nous voulons que les machines apprennent ces règles à partir du texte qu'elles lisent.

Maintenant, les machines ne connaissent aucune langue, ni ne comprennent le son ou la phonétique. Elles doivent être enseignées à partir de zéro et de manière à ce qu'elles puissent lire n'importe quelle langue qui existe.

Une tâche assez ardue, n'est-ce pas ?

Les humains apprennent une langue en reliant le son au sens, puis nous apprenons à lire et à écrire dans cette langue. Les machines ne peuvent pas faire cela, elles doivent donc recevoir les unités de texte les plus basiques pour commencer à traiter le texte.

C'est là que la tokenisation entre en jeu. Elle décompose le texte en unités plus petites appelées "tokens".

Et il existe différentes façons de tokeniser le texte, ce que nous allons apprendre maintenant.

## Différentes façons de tokeniser le texte

Pour faire apprendre le texte à un modèle de deep learning, nous avons besoin d'un processus en deux étapes :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fff7fafb7-a127-4e41-a050-cb02951f3112_1391x821.jpeg align="left")

1. Tokeniser – décider de l'algorithme que nous allons utiliser pour générer les tokens.

2. Encoder les tokens en vecteurs

## Tokenisation basée sur les mots

Comme le suggère la première étape, nous devons décider comment convertir le texte en petits tokens. Une méthode simple et directe que la plupart d'entre nous proposeraient est d'utiliser des tokens basés sur les mots, en divisant le texte par espaces.

### Problèmes avec le tokeniseur de mots

**Il y a un risque élevé de manquer des mots dans les données d'entraînement.** Avec des tokens de mots, votre modèle ne reconnaîtra pas les variantes de mots qui ne faisaient pas partie des données sur lesquelles le modèle a été entraîné.

Ainsi, si votre modèle a vu `foot` et `ball` dans les données d'entraînement, mais que le texte final contient `football`, le modèle ne pourra pas reconnaître le mot et il sera traité avec un token `<UNK>`.

De même, la ponctuation pose un autre problème. Par exemple, `let` ou `let's` nécessiteront des tokens individuels, ce qui est une solution inefficace. Cela **nécessitera un vocabulaire énorme** pour s'assurer que vous avez pensé à toutes les variantes du mot.

Même si vous ajoutez un **lemmatiseur** pour résoudre ce problème, vous ajoutez une étape supplémentaire dans votre pipeline de traitement.

**Il est également difficile de gérer l'argot et les abréviations.** Nous utilisons beaucoup d'argot et d'abréviations dans le texte de nos jours, comme "FOMO", "LOL", "tl;dr" et ainsi de suite. Que faisons-nous pour ces mots ?

**Enfin, que se passe-t-il si la langue n'utilise pas d'espaces pour la segmentation ?** Pour une langue comme le chinois, qui n'utilise pas d'espaces pour la séparation des mots, ce tokeniseur échouera complètement.

Après avoir rencontré ces problèmes, les chercheurs ont examiné une autre approche qui consistait à tokeniser tous les caractères.

## Tokenisation basée sur les caractères

Pour résoudre les problèmes associés à la tokenisation basée sur les mots, les scientifiques des données ont essayé une approche alternative de tokenisation caractère par caractère.

Cela a effectivement résolu le problème des mots manquants, car nous traitons maintenant des caractères qui peuvent être encodés en utilisant ASCII ou Unicode. Maintenant, il pouvait générer des plongements pour n'importe quel mot.

Chaque caractère, qu'il s'agisse d'un espace, d'une apostrophe, d'un deux-points ou autre, peut maintenant se voir attribuer un symbole pour générer une séquence de vecteurs.

Mais cette approche avait ses propres inconvénients.

### Problèmes avec les modèles basés sur les caractères

**Tout d'abord, cette approche nécessite plus de ressources informatiques.** Les modèles basés sur les caractères traiteront chaque caractère comme un token. Et plus de tokens signifie plus de calculs d'entrée pour traiter chaque token, ce qui à son tour nécessite plus de ressources de calcul.

Par exemple, pour une phrase de 5 mots, vous devrez peut-être traiter 30 tokens au lieu de 5 tokens basés sur les mots.

**De plus, cela réduit le nombre de tâches et d'applications de TAL.** Avec de longues séquences de caractères, vous ne pouvez utiliser qu'un certain type d'architecture de réseau de neurones.

Cela limite le type de tâches de TAL que nous pouvons effectuer. Pour des applications comme la reconnaissance d'entités ou la classification de texte, l'encodage basé sur les caractères pourrait s'avérer une approche inefficace.

**Enfin, il y a un risque d'apprendre des sémantiques incorrectes.** Travailler avec des caractères pourrait générer des orthographes incorrectes des mots. De plus, sans signification inhérente, apprendre avec des caractères revient à apprendre sans sémantique significative.

> Ce qui est fascinant, c'est que pour une tâche apparemment si simple, de multiples algorithmes ont été écrits pour trouver la politique de tokenisation optimale.

Après avoir compris les avantages et les inconvénients de ces méthodes de tokenisation, il est logique de chercher une approche qui offre une voie médiane. Nous en voudrons une qui préserve les sémantiques avec un vocabulaire limité qui peut générer tous les mots du texte lors de la fusion.

## Tokenisation par sous-mots

Avec les modèles basés sur les caractères, nous risquons de perdre les caractéristiques sémantiques du mot. Et avec la tokenisation basée sur les mots, nous avons besoin d'un vocabulaire très large pour englober toutes les variations possibles de chaque mot.

Ainsi, l'objectif était de développer un algorithme capable de :

1. Conserver les caractéristiques sémantiques du token, c'est-à-dire l'information par token.

2. Tokeniser sans exiger un vocabulaire très large avec un ensemble fini de mots.

Pour résoudre ce problème, vous pouvez penser à décomposer les mots en fonction d'un ensemble de préfixes et de suffixes. Par exemple, nous pouvons écrire un système basé sur des règles pour identifier des sous-mots comme `"##s"`, `"##ing"`, `"##ify"`, `"un##"` et ainsi de suite, où la position du double dièse indique les préfixes et les suffixes.

Ainsi, un mot comme `"unhappily"` est tokenisé en utilisant des sous-mots comme `"un##"`, `"happ"`, et `"##ily"`.

Le modèle n'apprend que relativement peu de sous-mots et les assemble ensuite pour créer d'autres mots. Cela résout les problèmes de mémoire requise et d'effort nécessaire pour créer un large vocabulaire.

### Problèmes avec l'algorithme de tokenisation par sous-mots :

Tout d'abord, certains des sous-mots qui sont créés selon les règles définies peuvent ne jamais apparaître dans votre texte à tokeniser et peuvent finir par occuper de la mémoire supplémentaire.

De plus, pour chaque langue, nous devrons définir un ensemble différent de règles pour créer des sous-mots.

Pour atténuer ce problème, en pratique, la plupart des tokeniseurs modernes ont une phase d'entraînement qui identifie le texte récurrent dans le corpus d'entrée et crée de nouveaux tokens de sous-mots. Pour les motifs rares, nous restons sur des tokens basés sur les mots.

Un autre facteur important qui joue un rôle vital dans ce processus est la taille du vocabulaire que l'utilisateur définit. Une grande taille de vocabulaire permet de tokeniser plus de mots courants, tandis qu'un vocabulaire plus petit nécessite la création de plus de sous-mots pour créer chaque mot dans le texte sans utiliser le token `<UNK>`.

Trouver le bon équilibre pour votre application est la clé ici.

## Algorithme d'encodage par paires d'octets (BPE)

Le BPE était à l'origine un algorithme de compression de données que vous utilisez pour trouver la meilleure façon de représenter les données en identifiant les paires d'octets communes. Nous l'utilisons maintenant en TAL pour trouver la meilleure représentation du texte en utilisant le plus petit nombre de tokens.

Voici comment cela fonctionne :

1. Ajoutez un identifiant (`</w>`) à la fin de chaque mot pour identifier la fin d'un mot, puis calculez la fréquence des mots dans le texte.

2. Divisez le mot en caractères, puis calculez la fréquence des caractères.

3. À partir des tokens de caractères, pour un nombre prédéfini d'itérations, comptez la fréquence des paires d'octets consécutives et fusionnez la paire d'octets la plus fréquemment rencontrée.

4. Continuez à itérer jusqu'à ce que vous ayez atteint la limite d'itération (définie par vous) ou jusqu'à ce que vous ayez atteint la limite de tokens.

Passons en revue chaque étape (dans le code) pour un exemple de texte. Pour coder cela, j'ai pris de l'aide sur [le blog très minimaliste de Lei Mao sur le BPE](https://leimao.github.io/blog/Byte-Pair-Encoding/). Je vous encourage à le consulter !

## Étape 1 : Ajouter des identifiants de mots et calculer la fréquence des mots

Voici notre texte d'exemple :

```javascript
"There is an 80% chance of rainfall today. We are pretty sure it is going to rain."
```

```javascript
## définir le texte d'abord
```

```javascript
text = "There is an 80% chance of rainfall today. We are pretty sure it is going to rain."
```

```javascript
## obtenir la fréquence des mots et ajouter le token de fin de mot (</w>) ## à la fin de chaque mot

words = text.strip().split(" ")

print(f"Taille du vocabulaire : {len(words)}")
```

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb90e5882-9f1f-4b05-be48-3e9336cf1854_283x392.png align="left")

## Étape 2 : Diviser le mot en caractères puis calculer la fréquence des caractères

```javascript
char_freq_dict = collections.defaultdict(int)
for word, freq in word_freq_dict.items():
    chars = word.split()
    for char in chars:
        char_freq_dict[char] += freq

char_freq_dict
```

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fecbf93c5-7fd6-4a40-a63d-e504be1bf157_396x536.png align="left")

## Étape 3 : Fusionner les paires d'octets consécutives les plus fréquemment rencontrées

```javascript
import re

## créer toutes les paires consécutives possibles
pairs = collections.defaultdict(int)
for word, freq in word_freq_dict.items():
    chars = word.split()
    for i in range(len(chars)-1):
        pairs[chars[i], chars[i+1]] += freq
```

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdaf21979-946b-4dfb-b090-64e591c13907_400x590.png align="left")

## Étape 4 - Itérer n fois pour trouver les meilleures paires (en termes de fréquence) à encoder puis les concaténer pour trouver les sous-mots

Il est préférable à ce stade de structurer notre code en fonctions. Cela signifie que nous devons effectuer les étapes suivantes :

1. Trouver les paires d'octets les plus fréquemment rencontrées à chaque itération.

2. Fusionner ces tokens.

3. Recalculer la fréquence des tokens de caractères avec le nouveau codage de paires ajouté.

4. Continuer à faire cela jusqu'à ce qu'il n'y ait plus de paires ou que vous atteigniez la fin de la boucle for.

Pour le code détaillé, vous devriez **consulter mon** [**Colab notebook**](https://colab.research.google.com/drive/1QLlQx_EjlZzBPsuj_ClrEDC0l8G-JuTn?usp=sharing)**.**

Voici une sortie réduite de ces 4 étapes :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4cb7b992-1986-4dbc-a444-da817255f80f_1295x637.png align="left")

Ainsi, à chaque itération avec chaque meilleure paire, nous fusionnons (concaténons) la paire. Vous pouvez voir que lorsque nous recalculons la fréquence, la fréquence des tokens de caractères d'origine est réduite et la nouvelle fréquence des tokens appariés apparaît dans le dictionnaire des tokens.

Si vous regardez le nombre de tokens créés, il augmente d'abord parce que nous créons de nouveaux appariements – mais le nombre commence à diminuer après un certain nombre d'itérations.

Ici, nous avons commencé avec 25 tokens, sommes passés à 31 tokens à la 14ème itération, puis sommes redescendus à 16 tokens à la 50ème itération. Intéressant, n'est-ce pas ?

## Comment améliorer l'algorithme BPE

L'algorithme BPE est un algorithme glouton, ce qui signifie qu'il essaie de trouver la meilleure paire à chaque itération. Et il y a certaines limitations à cette approche gloutonne.

Il y a donc bien sûr des avantages et des inconvénients à l'algorithme BPE.

Les tokens finaux varieront en fonction du nombre d'itérations que vous avez exécutées. Cela pose également un autre problème : nous pouvons maintenant avoir différents tokens pour un seul texte, et donc différents plongements.

Pour résoudre ce problème, plusieurs solutions ont été proposées. Mais celle qui s'est démarquée était un modèle de langage unigramme qui ajoutait un entraînement de [régularisation de sous-mots (une nouvelle méthode de segmentation de sous-mots)](https://arxiv.org/pdf/1804.10959.pdf) qui calcule la probabilité pour chaque token de sous-mot afin de choisir la meilleure option en utilisant une fonction de perte. Nous en parlerons plus en détail dans les prochains articles.

## Utilisons-nous le BPE dans les BERT ou les GPT ?

Des modèles comme BERT ou GPT-2 utilisent une version du BPE ou du modèle unigramme pour tokeniser le texte d'entrée.

BERT a inclus un nouvel algorithme appelé WordPiece. Il est similaire au BPE, mais possède une couche supplémentaire de calcul de probabilité pour décider si le token fusionné fera la coupe finale.

## Résumé

Dans ce blog, vous avez appris comment une machine commence à donner un sens au langage en décomposant le texte en unités très petites.

Maintenant, il existe de nombreuses façons de décomposer le texte et il devient donc important de comparer une approche avec une autre.

Nous avons commencé par comprendre la tokenisation en divisant le texte anglais par espaces – mais toutes les langues ne sont pas écrites de la même manière (c'est-à-dire en utilisant des espaces pour désigner la segmentation). Nous avons donc examiné la division par caractère pour générer des tokens de caractères.

Le problème avec les caractères était la perte des caractéristiques sémantiques des tokens au risque de créer des représentations ou des plongements de mots incorrects.

Pour obtenir le meilleur des deux mondes, nous avons examiné la tokenisation par sous-mots, qui était plus prometteuse. Et enfin, nous avons examiné l'algorithme BPE pour implémenter la tokenisation par sous-mots.

Nous examinerons plus en détail les prochaines étapes et les tokeniseurs avancés comme WordPiece, SentencePiece, et comment travailler avec le tokeniseur HuggingFace la semaine prochaine.

## Références et Notes

Mon article est en fait une accumulation des articles et blogs suivants que je vous encourage à lire :

1. [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/pdf/1508.07909.pdf) - Article de recherche qui discute des différentes techniques de segmentation basées sur l'algorithme de compression BPE.

2. [Dépôt GitHub sur Subword NMT (Neural Machine Translation)](https://github.com/rsennrich/subword-nmt) - code de support pour l'article ci-dessus.

3. [Blog de Lei Mao sur l'encodage par paires d'octets](https://leimao.github.io/blog/Byte-Pair-Encoding/) - J'ai utilisé le code de son blog pour implémenter et comprendre le BPE moi-même.

4. [Comment les machines lisent](https://blog.floydhub.com/tokenization-nlp/) - un blog de Cathal Horan.

Si vous cherchez à commencer dans le domaine de la science des données ou du ML, consultez mon cours sur les [**Fondements de la Science des Données et du ML**](https://www.wiplane.com/p/foundations-for-data-science-ml).

Si vous souhaitez recevoir tous mes tutoriels/blogs directement dans votre boîte de réception, envisagez de vous abonner à [ma newsletter ici](https://dswharshit.substack.com/).

Vous avez quelque chose à ajouter ou à suggérer, vous pouvez me contacter via :

* [YouTube](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ)

* [Twitter](https://twitter.com/dswharshit)

* [LinkedIn](https://www.linkedin.com/in/tyagiharshit/)