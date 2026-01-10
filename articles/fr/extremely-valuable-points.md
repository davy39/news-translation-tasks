---
title: Comment embaucher des développeurs Python et identifier les vrais maîtres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-18T12:11:02.000Z'
originalURL: https://freecodecamp.org/news/extremely-valuable-points
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/hire-a-Python-Developer-in-2019.jpg
tags:
- name: Hire app developers
  slug: hire-app-developers
- name: hire python developer
  slug: hire-python-developer
- name: Python
  slug: python
- name: python developer
  slug: python-developer
- name: Python Developers
  slug: python-developers
seo_title: Comment embaucher des développeurs Python et identifier les vrais maîtres
seo_desc: "By Shifa Martin\n“The joy of coding is in seeing a short, concise, readable,\
  \ and small amount of clear code, not in trivial code that bores the reader,” said\
  \ Guido van Rossum, a Dutch computer scientist and the inventor of Python. \nPython\
  \ developers u..."
---

Par Shifa Martin

« Le plaisir de coder réside dans le fait de voir un code court, concis, lisible et clair, et non un code trivial qui ennuie le lecteur », a déclaré **Guido van Rossum**, un informaticien néerlandais et l'inventeur de Python. 

Les développeurs Python utilisent des technologies web modernes pour construire des solutions logicielles et applicatives, des plus basiques aux plus complexes. 

## La demande de développeurs Python croît très rapidement

Python a conquis presque tous les marchés. Et il a apporté une programmation facile à portée de main des développeurs qui étaient autrefois totalement déconcertés par des langages de programmation triviaux. Pourtant, la demande pour les développeurs Python semble continuer à augmenter. Pour le prouver, j'ai inclus ici quelques statistiques clés.        

> Une recherche de [l'Economist](https://www.economist.com/science-and-technology/2018/07/19/python-has-brought-computer-programming-to-a-vast-new-audience) suggère qu'en Amérique, les recherches liées à Python sont plus fréquentes que celles pour **Kim Kardashian, une star de la téléréalité**. 

> L'enquête [Stack Overflow 2019](https://insights.stackoverflow.com/survey/2019) a révélé que près de 39,4 % des développeurs préfèrent Python pour le codage, et les autres souhaitent l'utiliser. 

## Comment interviewer des développeurs Python ?

Les opportunités d'embaucher des développeurs Python sur les marchés d'Amérique du Nord, d'Europe de l'Ouest et d'Asie sont en hausse. Les entreprises cherchent donc à embaucher des développeurs Python pour renforcer leurs équipes de développement. 

> Les principaux avantages de Python sont sa facilité d'utilisation, sa syntaxe directe, sa simplicité et l'utilisation d'espaces indentés. 

Ces caractéristiques le rendent facile à apprendre et à partager avec d'autres développeurs d'applications. 

Pour toutes ces raisons, je pense que l'embauche de développeurs Python expérimentés est l'une des tâches les plus importantes pour toute entreprise. 

Parfois, cela peut aussi être frustrant. J'ai donc pensé partager ici mon expérience pour embaucher des développeurs Python.

### Trouvez quelqu'un qui est flexible avec le langage et les outils

Si vous posez encore des questions comme comment concaténer deux listes en Python, alors vous devrez peut-être réviser tout votre processus d'entretien pour un développeur Python. N'oubliez pas les énigmes techniques. De plus, en donnant une tâche de codage en Python à un candidat, vous avez l'opportunité d'évaluer ses normes et compétences en codage.

### Pour vérifier les capacités du candidat, posez des questions :

> Quels sont les risques qui peuvent survenir avec ce code ?

> Quelle est la manière de surmonter les problèmes de codage ? 

> Comment géreraient-ils le problème en tant que développeur Python ?    

> Demandez au candidat d'écrire une fonction Python pour trouver le maximum de trois nombres.  

```py
Données d'entrée : z=1, y=3, x=5
Résultat attendu : x=5 
```

> Demandez au candidat d'écrire un programme en Python qui calcule et affiche la valeur donnée dans la formule.

**Voici un exemple de question que vous pouvez poser aux développeurs Python :**

Q = Racine carrée de [(4 * A * B)/J]  

Voici les valeurs fixes de A et J :

A est 50. J est 30.

B est la variable dont les valeurs doivent être entrées dans votre programme sous forme de séquence séparée par des virgules.

**Exemple pour les développeurs Python :**

Supposons que la séquence d'entrée suivante, séparée par des virgules, soit donnée au programme :

```py
Entrée : 100,150,180

Résultat attendu : 18,22,24
```

**Indications :**

> Si le résultat obtenu est sous forme décimale, il doit être arrondi à sa valeur la plus proche (par exemple, si le résultat obtenu est 46,0, il doit être affiché comme 46)

> Dans le cas où les données d'entrée sont fournies à la question, il faut supposer qu'il s'agit d'une entrée console. 

> Assurez-vous que le candidat, en tant que développeur Python, termine cette tâche dans un délai imparti. Disons 1 heure - 2 heures environ.

**Voici le résultat final des exemples de codage ci-dessus :**

```py
#!/usr/bin/env python
import math
a=50
j=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
   value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
   print ','.join(value)
```

**Voici un autre exemple de question pour un développeur Python :**

Écrivez un programme qui accepte une virgule dans une séquence séparée de mots et affiche les mots dans une séquence séparée par des virgules après tri.

```py
Entrée :
With, purse, blue, lady

Résultat attendu :
Blue, purse, with, lady
```

Il faut beaucoup de travail pour devenir un excellent développeur Python. C'est pourquoi je partage cette information avec vous. Je pense qu'il vaut la peine de l'ajouter à votre liste de questions d'entretien.

> _Voyez ce que mon prochain point va vous dire sur le processus d'embauche des développeurs Python._ 

### Donnez-leur des problèmes de codage Python réels que vous avez rencontrés auparavant

Comme on dit, si vous embauchez un développeur Python plus intelligent que vous, alors faites le changement rapidement. C'est une loi simple de l'attraction : les personnes talentueuses veulent travailler dans un endroit fantastique. Nous leur donnons donc une tâche issue d'un problème technologique réel. 

Voici ce que j'ai trouvé qui fonctionne bien.

### Exemple de projet Python réel

Dans mon entreprise ValueCoders ([Société d'externalisation informatique](https://www.valuecoders.com/)), j'ai travaillé sur le développement de la [solution logicielle de détection d'anomalies de données](https://www.valuecoders.com/case-studies/anomaly-detection-system#more-info) construite avec Python et le Machine Learning. 

Notre portefeuille de projets Python comprend une large gamme de solutions de machine learning, de portails B2B, d'applications web, etc. 

Mon équipe complète de développeurs Python a travaillé jour et nuit pour construire le système de détection d'anomalies de données. Ce système a été conçu de manière à pouvoir identifier la nature et les tendances des données pour les entreprises. 

### Défis du projet

J'ai rencontré de nombreux défis en travaillant sur ce projet. Bien que j'aie reçu une grande aide de mon équipe complète de développeurs Python, j'ai dû examiner les choses de près pour déterminer si l'application pouvait être parfaitement équilibrée. 

Selon mon expérience, le défi est de développer une application mobile qui peut aider les entreprises à traiter le problème des anomalies de données en temps réel. L'application doit révéler des informations importantes sur les données qui sont cruciales pour les entreprises numériques. Elle doit avoir un système pour révéler les problèmes des informations sur les données. Nous devons résoudre le problème des changements constants et variables dans les données.

_Cela n'est possible que grâce aux efforts de notre équipe de développeurs Python._

_Voyez comment ils ont trouvé une solution._

### Comment avons-nous trouvé une solution ? 

Notre équipe de développeurs Python a surmonté tous ces défis avec l'idée de développer une application à l'aide des technologies suivantes : Python, PyCHARM, PYGTK, PYQT, WXPython et Machine Learning. 

**Voici les étapes que nous avons appliquées pour identifier les anomalies dans les ensembles de données avec le concept de Python et de machine learning.**

**Étape 1**

Lire les données du fichier CSV à partir duquel les anomalies doivent être détectées.

**Étape 2**

Calculer la moyenne et la matrice de co-variance des échantillons de données.

**Étape 3**

Trouver la distribution [gaussienne](https://en.wikipedia.org/wiki/Gaussian_function) de l'ensemble de données. Correctement réalisée par nos développeurs Python.

**Étape 4**

Ensuite, calculer le [f1_score](https://en.wikipedia.org/wiki/F1_score) et le [epsilon](https://en.wikipedia.org/wiki/Machine_epsilon) minimum pour chaque valeur d'epsilon selon la taille du pas.

**Étape 5**

Comparer les probabilités de l'ensemble de données de test avec l'epsilon. Celui qui tombe en dessous de l'epsilon pourrait être considéré comme une anomalie.

> **En conséquence, notre équipe de développement a développé une solution efficace de détection d'anomalies de données basée sur Python et le machine learning.**

L'objectif est donc d'attirer des développeurs Python de niveau A dans votre entreprise. Pour cela, vous devez vous concentrer sur la manière dont un candidat aborde le problème, élabore une carte de codage et résout le problème. 

Observez les techniques de résolution de problèmes utilisées par le candidat pour un seul langage. 

Travaillez également sur votre processus d'entretien et encouragez votre équipe de recrutement à faire de même. 

Écrire un code lisible en Python est important. 

Les développeurs Python ayant des connaissances sur une variété de bibliothèques open-source aident à réduire le temps de développement logiciel et vous libèrent des tâches répétitives et des erreurs.  

### Ne vous concentrez pas uniquement sur l'expérience - Demandez-leur leurs compétences en codage

J'ai interviewé plusieurs développeurs Python qui montraient une grande expérience dans leur CV mais qui performaient mal lors de l'entretien. Peu importe à quel point le CV est bon. Si vous avez besoin que votre nouveau développeur Python travaille sur quelque chose de critique, plus d'expérience est généralement requise ici, ce qui signifie plus de productivité. 

Ici, j'aimerais souligner que votre nouvelle recrue doit s'attaquer à de nouveaux problèmes. Plus d'expérience conduit souvent à des développeurs Python ayant des opinions arrêtées, surtout lorsque vous essayez de créer quelque chose de nouveau avec Python.

## Conclusion

Les décisions de dernière minute sont rarement satisfaisantes. Qu'en pensez-vous ? Est-ce vrai ou non ?  

Il est également dit que, *« N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre, mais les bons programmeurs écrivent du code que les humains peuvent comprendre. »_ 

C'est la plus grande chose que je vois manquer chez la plupart des startups lorsqu'elles embauchent des développeurs Python sans une idée claire de la manière dont leur expérience et leur travail justifieront le coût de leur embauche. 

Oui, un développeur Python doit être bien formé, expérimenté et, surtout, produire un code Python bien écrit. 

Enfin, je vous encourage à embaucher des développeurs Python après une analyse approfondie de leurs compétences en codage, de leur communication et de leur performance lors de l'entretien en personne. Ne vous concentrez pas trop sur le CV du candidat. J'ai vu des personnes qui sont bien sur le papier, mais d'autres domaines ne peuvent pas être négligés.

**Besoin d'[embaucher des développeurs Python](https://www.valuecoders.com/hire-developers/hire-python-developers) ? N'hésitez pas à [nous contacter](https://www.valuecoders.com/contact).** 

**Ou, suivez-nous sur Twitter pour les mises à jour futures : [https://twitter.com/ValueCoders](https://twitter.com/ValueCoders)**