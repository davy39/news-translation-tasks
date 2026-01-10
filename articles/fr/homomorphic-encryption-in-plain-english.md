---
title: Comment fonctionne le chiffrement homomorphe – Expliqué en français simple
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-01-29T18:33:48.000Z'
originalURL: https://freecodecamp.org/news/homomorphic-encryption-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/vanna-phon-hRXIKdxoaPo-unsplash--1-.jpg
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: Comment fonctionne le chiffrement homomorphe – Expliqué en français simple
seo_desc: "As the fields of cryptography and cybersecurity advance, homomorphic encryption\
  \ stands out as a groundbreaking technology. \nIt has the potential to reshape everything\
  \ in data privacy and security.\nWhat really is homomorphic encryption? Why is it\
  \ gett..."
---

Alors que les domaines de la cryptographie et de la cybersécurité avancent, le [chiffrement homomorphe](https://www.freecodecamp.org/news/introduction-to-homomorphic-encryption/) se distingue comme une technologie révolutionnaire. 

Il a le potentiel de redéfinir tout ce qui concerne la confidentialité et la sécurité des données.

Qu'est-ce que le chiffrement homomorphe ? Pourquoi attire-t-il autant d'attention ? Comment peut-il améliorer la confidentialité des données ?

Essentiellement, avec le chiffrement homomorphe, nous pouvons traiter des données chiffrées sans jamais avoir besoin de les déchiffrer pour effectuer des calculs.

Cela garantit une confidentialité totale partout où les données sont traitées et stockées.

Dans cet article, vous apprendrez pourquoi ce type de chiffrement révolutionnera le domaine de la sécurité. Nous aborderons des questions telles que :

* Qu'est-ce que le chiffrement homomorphe ?
* Comment fonctionne le chiffrement homomorphe ?
* Chiffrement homomorphe vs chiffrement traditionnel – quelle est la différence ?
* Quelles sont les applications du chiffrement homomorphe ?

## Qu'est-ce que le chiffrement homomorphe ?

Utilisons une analogie pour comprendre le chiffrement homomorphe.

Imaginez un coffre au trésor verrouillé contenant de nombreux objets de valeur.

Pour ajouter ou retirer des objets, vous devez déverrouiller le coffre. Cela pourrait faciliter le vol des objets par des voleurs lorsque vous l'ouvrez.

Dans cette analogie, c'est ce que représente le chiffrement traditionnel.

Le chiffrement homomorphe est comme avoir une gante magique qui vous permet d'ajouter ou de retirer des objets du coffre sans jamais avoir à le déverrouiller.

Ainsi, vous éliminez le risque que les voleurs puissent jamais accéder aux objets à l'intérieur du coffre au trésor.

C'est essentiellement ce que fait le chiffrement homomorphe avec les données : il nous permet d'effectuer des opérations sur des données chiffrées sans jamais avoir besoin de les déchiffrer.

Cela n'est pas possible avec le chiffrement traditionnel. Dans ce cas, nous devons traiter les données que nous devons déchiffrer, effectuer les calculs nécessaires, puis chiffrer à nouveau les données.

Avec le chiffrement homomorphe, la sécurité n'est jamais compromise.

## Comment fonctionne le chiffrement homomorphe ?

Le chiffrement homomorphe permet aux calculs d'agir sur des données chiffrées – également appelées texte chiffré.

Cela signifie que les données sont traitées alors qu'elles sont chiffrées.

Le chiffrement homomorphe effectue des calculs sur des données chiffrées (texte chiffré). Mais les calculs effectués sur le texte chiffré donnent des résultats chiffrés.

Lorsque ces résultats sont déchiffrés, ils sont similaires à ceux qui auraient été obtenus si les opérations avaient été effectuées sur les données originales, non chiffrées.

Ainsi, le chiffrement homomorphe permet d'effectuer des opérations sur des données chiffrées pour obtenir les mêmes résultats que si elles étaient effectuées sur les données originales, déchiffrées.

### Comment cela est-il fait ?

Le chiffrement homomorphe utilise des algorithmes mathématiques complexes qui :

* transforment les nombres pour obscurcir les données originales, et 
* effectuent les mêmes opérations que ce soit sur les données originales ou sur ces données obscurcies.

Essentiellement, vous travaillez toujours sur les mêmes données de la même manière, mais à partir de différents points de vue.

Ainsi, vous pouvez travailler avec les données et obtenir exactement les mêmes résultats que si elles n'étaient pas chiffrées. Mais comme elles sont effectivement chiffrées, les données sont toujours protégées !

De cette manière, personne ne peut les voir et éventuellement les voler, ce qui permet la confidentialité des données même dans des environnements où la confiance est minimale.

### Exemple de code Python

Nous allons utiliser la bibliothèque Pyfhel pour cet exemple, que vous pouvez découvrir plus en détail [ici](https://pypi.org/project/Pyfhel/3.1.1/).

Dans ce code, nous allons additionner deux nombres sous leur forme chiffrée et voir les résultats.

Voici le code complet pour que vous puissiez vraiment comprendre comment fonctionne le chiffrement homomorphe :

```python
import numpy as np
from Pyfhel import Pyfhel

HE = Pyfhel()
HE.contextGen(scheme='bfv', n=2**14, t_bits=20)
HE.keyGen()

integer1 = np.array([127], dtype=np.int64)
integer2 = np.array([-57], dtype=np.int64)

ctxt1 = HE.encryptInt(integer1)
ctxt2 = HE.encryptInt(integer2)

ctxtSum = ctxt1 + ctxt2
ctxtSub = ctxt1 - ctxt2
ctxtMul = ctxt1 * ctxt2

resSum = HE.decryptInt(ctxtSum) 
resSub = HE.decryptInt(ctxtSub)
resMul = HE.decryptInt(ctxtMul)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/ray-so-export.png)

Maintenant, nous allons le décomposer ligne par ligne :

Tout d'abord, nous devons importer les modules nécessaires :

```
import numpy as np
from Pyfhel import Pyfhel
```

Ici, nous importons simplement les modules nécessaires pour effectuer nos calculs.

Ensuite, nous devons créer un objet Pyfhel et générer des clés :

```
HE = Pyfhel()
HE.contextGen(scheme='bfv', n=2**14, t_bits=20)
HE.keyGen()
```

Dans la première ligne, nous initialisons un objet python `Pyfhel`. Dans la deuxième ligne, nous définissons le chiffrement avec certains paramètres :

* `scheme='bfv'` : Nous utilisons le schéma de chiffrement homomorphe [BFV (Brakerski/Fan-Vercauteren)](https://link.springer.com/chapter/10.1007/978-3-030-92078-4_21).
* `n=2**14` : Définit le degré du module polynomiale. Le degré du module polynomiale équilibre le niveau de sécurité du chiffrement avec l'efficacité computationnelle. Un nombre plus grand offre un meilleur chiffrement mais au coût de plus de ressources computationnelles.
* `t_bits=20` : Définit la taille en bits du module de texte en clair. Des valeurs de taille en bits plus grandes vous permettent d'utiliser des nombres plus grands mais rendent le chiffrement moins propre.
* Dans la troisième ligne, nous [générons une clé publique et privée](https://www.freecodecamp.org/news/encryption-explained-in-plain-english/)

Ensuite, nous obtenons deux nombres et les chiffrons :

```
integer1 = np.array([127], dtype=np.int64)
integer2 = np.array([-57], dtype=np.int64)

ctxt1 = HE.encryptInt(integer1)
ctxt2 = HE.encryptInt(integer2)
```

Nous représentons les nombres dans un tableau avec un seul nombre et les chiffrons.

Nous représentons ces nombres dans un tableau et non comme si nous déclarions des variables.

Nous faisons cela car la fonction `encryptInt()` ne prend qu'un tableau d'entiers de 64 bits comme argument. D'après la [documentation](https://pyfhel.readthedocs.io/en/latest/_autosummary/Pyfhel.Pyfhel.html) :

```python
encryptInt(self, int64_t[:] arr, PyCtxt ctxt=None)
```

Maintenant, nous allons effectuer les opérations sur les deux nombres alors qu'ils sont chiffrés :

```
ctxtSum = ctxt1 + ctxt2
ctxtSub = ctxt1 - ctxt2
ctxtMul = ctxt1 * ctxt2
```

Puis nous déchiffrons les nombres après l'opération alors qu'ils étaient chiffrés :

```
resSum = HE.decryptInt(ctxtSum) 
resSub = HE.decryptInt(ctxtSub)
resMul = HE.decryptInt(ctxtMul)
```

Ce qui donnera le résultat suivant :

```
>>> [70  0  0 ...  0  0  0]
>>> [184   0   0 ...   0   0   0]
>>> [-7239     0     0 ...     0     0     0]
```

Et si nous effectuons les calculs normaux sans être chiffrés, nous voyons que les valeurs correspondent :

```
integer1 = 127
integer2 = -57

print(integer1+integer2)

print(integer1-integer2)

print(integer1*integer2)
```

Ce qui donne le résultat suivant :

```
>>> 70

>>> 184

>>> -7239
```

Comme vous pouvez le voir, nous obtenons les mêmes résultats si nous effectuons les opérations sur les données alors qu'elles sont chiffrées que lorsque elles ne le sont pas.

## Chiffrement homomorphe vs chiffrement traditionnel – Quelle est la différence ?

Dans les méthodes de chiffrement traditionnelles, les données doivent être déchiffrées avant tout traitement.

Dans le chiffrement homomorphe, les données sont toujours utilisées dans leur état chiffré.

Le chiffrement traditionnel est comme une enveloppe sécurisée : le contenu doit être sorti pour être lu ou modifié.

Le chiffrement homomorphe est comme une enveloppe spéciale qui permet la manipulation du contenu sans jamais avoir besoin de l'ouvrir pour le lire ou le modifier.

## Applications du chiffrement homomorphe

Il existe de nombreuses applications pratiques du chiffrement homomorphe.

Dans le cloud computing, il permet aux utilisateurs de traiter des données dans le cloud sans jamais les exposer aux fournisseurs de services cloud. Ainsi, les informations sensibles restent toujours confidentielles.

Dans le domaine de la santé, il permet l'analyse de dossiers médicaux chiffrés sans compromettre la confidentialité des patients. Les données de santé des patients restent toujours protégées.

Une autre application prometteuse du chiffrement homomorphe est dans les systèmes de vote sécurisés. En utilisant ce type de chiffrement, les votes sont comptés de manière à ce que personne ne puisse voir pour qui chaque personne a voté. Cela rendrait le processus de vote plus sûr et plus privé.

Ces exemples ne représentent que la partie émergée de l'iceberg.

## Conclusion

Le chiffrement homomorphe est un changement de paradigme dans la manière dont nous gérons et traitons les données sensibles.

Cette technologie et son développement sont importants alors que de plus en plus de violations de données se produisent tout le temps.

Le chiffrement homomorphe offre une voie vers la simplification des réglementations sur la confidentialité des données.

Il permet également plus d'innovation en rendant la protection des données privées plus simple, encourageant ainsi de nouveaux développements en matière de sécurité.