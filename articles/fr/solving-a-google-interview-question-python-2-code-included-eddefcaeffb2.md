---
title: 'Guide des questions d''entretien chez Google : Supprimer les caractères récurrents
  avec Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T16:42:33.000Z'
originalURL: https://freecodecamp.org/news/solving-a-google-interview-question-python-2-code-included-eddefcaeffb2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e56V2AE2vxE7FgYBWb80_g.jpeg
tags:
- name: Google
  slug: google
- name: Job Interview
  slug: job-interview
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: 'Guide des questions d''entretien chez Google : Supprimer les caractères
  récurrents avec Python'
seo_desc: 'By Anthony Sistilli

  Nowadays, Google interviews are all the rage. But sometimes, interviews can get
  the best of us. Especially if it’s for a position we really want.

  I’ve had the pleasure of interviewing at multiple top companies as a student, and
  la...'
---

Par Anthony Sistilli

De nos jours, les entretiens chez Google sont très en vogue. Mais parfois, les entretiens peuvent nous mettre à rude épreuve. Surtout s'il s'agit d'un poste que nous voulons **vraiment**.

J'ai eu le plaisir de passer des entretiens dans plusieurs grandes entreprises en tant qu'étudiant, et j'ai décroché un emploi dans la Silicon Valley en tant qu'ingénieur logiciel.

Mon objectif est de vous aider à obtenir ce travail de rêve que vous avez toujours voulu !

Nous allons passer en revue une question classique qui pourrait apparaître lors de votre prochain entretien chez Google.

**Attention : si vous êtes un vétéran de la programmation, vous savez probablement déjà comment résoudre cette question !**

Si vous essayez d'obtenir un **stage** ou un emploi **à temps plein** l'année prochaine, alors vous bénéficierez définitivement de cet article. ???

### QUESTION : Étant donné une chaîne de caractères en entrée, supprimez tout caractère récurrent et retournez la nouvelle chaîne.

Si vous préférez une vidéo pour expliquer la question, [j'en ai fait une ici](https://www.youtube.com/watch?v=EaNX2PG6PEM).

![Image](https://cdn-media-1.freecodecamp.org/images/vv17teBZkBcz1N9YYWbuSuDrjToPBRKECOs9)

Comme nous pouvons le voir dans l'exemple ci-dessus, la sortie est « abc » parce que nous supprimons le deuxième 'a', 'b' et 'c'.

Tout d'abord, définissons notre fonction en Python 2.7.

```
def deleteReoccurringCharacters(string):
```

Pour aborder cette question, nous allons utiliser une structure de données spécifique appelée HashSet.

![Image](https://cdn-media-1.freecodecamp.org/images/LcEjXtDtuirkkf-VWJ5VNDes95irHF-8K89D)
_Un Set_

Vous pouvez penser à un set comme étant similaire à un tableau, avec deux exceptions principales.

1. **Il est complètement non ordonné**
2. **Il ne peut pas contenir de doublons**

Parce qu'il est non ordonné, nous aurons également besoin d'une chaîne de caractères vide pour stocker les caractères que nous avons ajoutés au set dans l'ordre. Ce sera la chaîne que nous retournerons.

Définissons ces deux éléments.

```
def deleteReoccurringCharacters(string):    seenCharacters = set()    outputString = ''
```

Maintenant que nous avons mis en place les structures de données dont nous avons besoin, parlons de notre algorithme.

En raison du fonctionnement d'un set en mémoire, il a une complexité de temps de recherche de 0(1).

Cela signifie que nous pouvons l'utiliser pour vérifier si nous avons déjà visité un caractère !

### Notre algorithme

**Parcourez tous les caractères de la chaîne initiale et faites ce qui suit :**

> Étape 1 : Vérifiez si le caractère est déjà dans notre set

> Étape 2 : S'il n'est pas dans le set, ajoutez-le au set et ajoutez-le à la chaîne

Voyons à quoi cela ressemblerait en code ???

```
for char in string:    if char not in seenCharacters:        seenCharacters.add(char)        outputString += char
```

Nous n'avons pas à nous soucier d'un cas « else », car nous ne faisons rien avec le caractère récurrent lui-même.

Il ne nous reste plus qu'à retourner la outputString.

**Voici à quoi ressemble le code final :**

```
def deleteReoccurringCharacters(string):    seenCharacters = set()    outputString = ''    for char in string:        if char not in seenCharacters:            seenCharacters.add(char)            outputString += char    return outputString
```

Et voilà !

Maintenant, si cela avait été un entretien, votre recruteur vous aurait demandé la complexité en temps et en espace.

Faisons une petite analyse.

### Complexité en temps

Parcourir toute la chaîne d'entrée a une complexité en temps de O(n), puisque la chaîne contient _n_ caractères.

Pour chacun de ces caractères, nous devons vérifier si nous l'avons déjà vu... Cependant, comme un HashSet a un temps de recherche de O(1), notre complexité en temps n'est pas affectée.

Ce qui nous laisse une complexité en temps finale de **O(n).**

### Complexité en espace

Dans le pire des cas, nous obtenons une chaîne avec tous les caractères uniques. Par exemple, « abcdef ».

Dans ce cas, nous stockerions tous les _n_ éléments dans notre chaîne et notre set.

Cependant, nous sommes également limités par la taille de l'alphabet anglais.

C'est une bonne occasion de demander à notre intervieweur quel type de caractères compte comme unique dans la chaîne (majuscules / minuscules / nombres / symboles).

En supposant que la chaîne initiale contiendra des lettres minuscules de l'alphabet, puisque l'alphabet est fini, notre set et notre chaîne de sortie ne pourront jamais être plus grands que 26 caractères.

Ce qui nous laisse une complexité en espace dans le pire des cas de **O(1).**

### Vous savez maintenant comment résoudre une question d'entretien chez Google !

Cette question est susceptible de se poser aux premiers stades de l'entretien en raison de sa simplicité... Comme le test en ligne, ou le premier appel téléphonique.

Si vous êtes un apprenant visuel comme moi, [regardez cette vidéo que j'ai faite expliquant davantage la solution](https://www.youtube.com/watch?v=EaNX2PG6PEM). **Je crée une nouvelle vidéo de tutoriel chaque jour autour du démarrage de votre carrière dans le logiciel.**

J'ai également publié le code final sur Github [ici](https://github.com/AtotheY/YoutubeTutorials/blob/master/InterviewPrep/deleteReoccuringCharacters.py).

Merci d'avoir regardé, et bonne chance !

.a #33