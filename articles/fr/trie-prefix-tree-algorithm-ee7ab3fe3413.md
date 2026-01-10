---
title: La Structure de Données Trie (Arbre de Préfixes)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-07T04:09:23.000Z'
originalURL: https://freecodecamp.org/news/trie-prefix-tree-algorithm-ee7ab3fe3413
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vuZ47z2Ff_EyAuRi087ICQ.gif
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: La Structure de Données Trie (Arbre de Préfixes)
seo_desc: 'By Julia Geist


  A Trie, (also known as a prefix tree) is a special type of tree used to store associative
  data structures


  A trie (pronounced try) gets its name from retrieval — its structure makes it a
  stellar matching algorithm.

  Context

  Write your ...'
---

Par Julia Geist

> Un `Trie`, (également connu sous le nom d'arbre de préfixes) est un type spécial d'arbre utilisé pour stocker des structures de données associatives

Un trie (prononcé "try") tire son nom de la **re**cherche (re**trie**val) — sa structure en fait un algorithme de correspondance exceptionnel.

### Contexte

```
Écrivez votre propre méthode shuffle pour mélanger aléatoirement les caractères d'une chaîne.
```

```
Utilisez le fichier texte des mots, situé à /usr/share/dict/words, et votre méthode shuffle pour créer un générateur d'anagrammes qui ne produit que des mots réels.
```

```
Étant donné une chaîne comme argument de ligne de commande, affichez l'un de ses anagrammes.
```

Ce défi m'a été présenté cette semaine à [Make School’s Product Academy](https://www.makeschool.com/product-academy).

Les mots dans le fichier texte sont séparés par des nouvelles lignes. Leur formatage facilite grandement leur insertion dans une structure de données. Pour l'instant, je les stocke dans une liste — chaque élément étant un mot unique du fichier.

Une approche pour ce défi est de :

* mélanger aléatoirement les caractères de la chaîne
* puis, vérifier si le résultat correspond à l'un des mots du fichier _/usr/share/dict/words_ pour confirmer qu'il s'agit d'un mot réel.

Cependant, cette approche nécessite que je vérifie si les caractères mélangés aléatoirement dans la nouvelle chaîne correspondent à l'un des 235 887 mots de ce fichier — cela signifie **235 887 opérations** **pour _chaque_ chaîne** que je souhaite vérifier comme étant un mot réel.

Cette solution était inacceptable pour moi. J'ai d'abord cherché des bibliothèques déjà implémentées pour vérifier si des mots existent dans une langue, et j'ai trouvé [pyenchant](https://github.com/rfk/pyenchant). J'ai d'abord complété le défi en utilisant la bibliothèque, en quelques lignes de code.

```
def generateAnagram(string, language="en_US"):   languageDict = enchant.Dict(language)    numOfPossibleCombinationsForString = math.factorial(len(string))   for i in range(0, numOfPossibleCombinationsForString):       wordWithShuffledCharacters = shuffleCharactersOf(string)
```

```
       if languageDict.check(wordWithShuffledCharacters):            return wordWithShuffledCharacters     return "There is no anagram in %s for %s." % (language, string)
```

Utiliser quelques fonctions de bibliothèque dans mon code était une solution rapide et facile. Cependant, je n'ai pas appris grand-chose en trouvant une bibliothèque pour résoudre le problème à ma place.

J'étais sûre que la bibliothèque n'utilisait pas l'approche que j'ai mentionnée plus tôt. J'étais curieuse et j'ai fouillé dans le code source — j'ai trouvé un trie.

### Trie

Un trie stocke les données en "étapes". Chaque étape est un nœud dans le trie.

Stocker des mots est un cas d'utilisation parfait pour ce type d'arbre, puisque il y a un nombre fini de lettres qui peuvent être combinées pour former une chaîne.

Chaque étape, ou nœud, dans un trie de langue représentera une lettre d'un mot. Les étapes commencent à se ramifier lorsque l'ordre des lettres diverge des autres mots dans le trie, ou lorsqu'un mot se termine.

J'ai créé un trie à partir de répertoires sur mon bureau pour **_visualiser_** la descente à travers les nœuds. Voici un trie qui contient deux mots : apple et app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vuZ47z2Ff_EyAuRi087ICQ.gif)
_Vous pouvez visualiser la descente à travers les nœuds d'un trie comme un changement de répertoires._

Notez que la fin d'un mot est indiquée par un « $ ». J'utilise « $ » car c'est un caractère unique qui ne sera présent dans aucun mot d'aucune langue.

Si je devais ajouter le mot « aperture » à ce trie, je parcourrais les lettres du mot « aperture » tout en descendant simultanément les nœuds du trie. Si la lettre existe en tant qu'enfant du nœud actuel, descendez dedans. Si la lettre n'existe pas en tant qu'enfant du nœud actuel, créez-la puis descendez dedans. Pour visualiser ces étapes en utilisant mes répertoires :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zX2hBSdXJTGI0jMzYS3HfA.gif)

En descendant le trie, les deux premières lettres de « aperture » sont déjà présentes dans le trie, donc je descends dans ces nœuds.

La troisième lettre, « e », cependant, n'est pas un enfant du nœud « p ». Un nouveau nœud est créé pour représenter la lettre « e », se ramifiant des autres mots du trie. De nouveaux nœuds pour les lettres suivantes sont également créés.

Pour générer un trie à partir d'un fichier de mots, ce processus se produira pour chaque mot, jusqu'à ce que toutes les combinaisons pour chaque mot soient stockées.

Vous pourriez penser : « Attendez, ne va-t-il pas falloir beaucoup de temps pour générer le trie à partir de ce fichier texte contenant 235 887 mots ? Quel est l'intérêt de parcourir _chaque caractère_ de chaque mot ? »

Oui, parcourir chaque caractère de chaque mot pour générer un trie prend un certain temps. Cependant, le temps pris pour créer le trie en vaut bien la peine — car pour vérifier si un mot existe dans le fichier texte, il faut au maximum autant d'opérations que la _longueur du mot lui-même_. _Bien mieux_ que les 235 887 opérations qu'il aurait fallu auparavant.

J'ai écrit la version la plus simple d'un trie, en utilisant des dictionnaires imbriqués. Ce n'est pas la manière la plus efficace de l'implémenter, mais c'est un bon exercice pour comprendre la logique derrière un trie.

```
endOfWord = "$"
```

```
def generateTrieFromWordsArray(words):   root = {}   for word in words:      currentDict = root      for letter in word:         currentDict = currentDict.setdefault(letter, {})      currentDict[endOfWord] = endOfWord   return root
```

```
def isWordPresentInTrie(trie, word):   currentDict = trie   for letter in word:      if letter in currentDict:         currentDict = currentDict[letter]      else:          return False   return endOfWord in currentDict
```

Vous pouvez voir ma [solution](https://github.com/juliascript/Python-Challenges/blob/master/accurateAnagram.py) pour le générateur d'anagrammes sur mon Github. Depuis que j'ai exploré cet algorithme, j'ai décidé de faire de cet article de blog l'un des nombreux — chaque article couvrant un algorithme ou une structure de données. Le code est disponible sur mon dépôt [Algorithms and Data Structures](https://github.com/juliascript/Algorithms-and-Data-Structures) — étoilez-le pour rester à jour !

### Prochaines Étapes

Je suggère de consulter le [dépôt trie](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Trie) de Ray Wenderlich. Bien qu'écrit en Swift, c'est une source précieuse pour les explications de divers algorithmes.

Similaire au trie (mais plus efficace en mémoire) se trouve un arbre suffixe, ou radix. En bref, au lieu de stocker des caractères uniques à chaque nœud, la fin d'un mot, son suffixe, est stockée et les chemins sont créés de manière relative.

Cependant, un radix est plus compliqué à implémenter qu'un trie. Je suggère de jeter un coup d'œil au [dépôt radix](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Radix%20Tree) de Ray Wenderlich si vous êtes intéressé.

Ceci est le premier article de ma série sur les algorithmes et les structures de données. Dans chaque article, je présenterai un problème qui peut être mieux résolu avec un algorithme ou une structure de données pour illustrer l'algorithme/la structure de données elle-même.

Étoilez mon [dépôt algorithms](https://github.com/juliascript/Algorithms) sur Github et suivez-moi sur [Twitter](https://twitter.com/JuliaGeist) si vous souhaitez suivre !

Avez-vous tiré de la valeur en lisant cet article ? [Cliquez ici](http://ctt.ec/X041V) pour le partager sur Twitter ! Si vous aimeriez voir ce type de contenu plus souvent, suivez-moi sur Medium et abonnez-vous à ma newsletter mensuelle ci-dessous. N'hésitez pas à [m'offrir un café](https://buymeacoff.ee/juliageist) aussi.