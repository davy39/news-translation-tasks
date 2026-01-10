---
title: Comment fonctionnent les classificateurs Naive Bayes – avec des exemples de
  code Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T00:28:32.000Z'
originalURL: https://freecodecamp.org/news/how-naive-bayes-classifiers-work
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9583740569d1a4ca0d65.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Machine Learning
  slug: machine-learning
seo_title: Comment fonctionnent les classificateurs Naive Bayes – avec des exemples
  de code Python
seo_desc: "By Jose J. Rodríguez\nNaive Bayes Classifiers (NBC) are simple yet powerful\
  \ Machine Learning algorithms. They are based on conditional probability and Bayes's\
  \ Theorem. \nIn this post, I explain \"the trick\" behind NBC and I'll give you\
  \ an example that w..."
---

Par Jose J. Rodríguez

Les classificateurs Naive Bayes (NBC) sont des algorithmes simples mais puissants d'apprentissage automatique. Ils sont basés sur la probabilité conditionnelle et le théorème de Bayes. 

Dans cet article, j'explique "l'astuce" derrière les NBC et je vous donnerai un exemple que nous pouvons utiliser pour résoudre un problème de classification.

Dans les sections suivantes, je parlerai des mathématiques derrière les NBC. N'hésitez pas à sauter ces sections et à passer directement à la partie implémentation si les mathématiques ne vous intéressent pas.

Dans la section implémentation, je vous montrerai un algorithme NBC simple. Ensuite, nous l'utiliserons pour résoudre un problème de classification. La tâche consistera à déterminer si un certain passager du Titanic a survécu à l'accident ou non.

## Probabilité conditionnelle

Avant de parler de l'algorithme lui-même, parlons des mathématiques simples qui se cachent derrière. Nous devons comprendre ce qu'est la probabilité conditionnelle et comment nous pouvons utiliser le théorème de Bayes pour la calculer.

Pensez à un dé équilibré à six faces. Quelle est la probabilité d'obtenir un six en lançant le dé ? C'est facile, c'est 1/6. Nous avons six résultats possibles et également probables, mais nous nous intéressons à un seul d'entre eux. Donc, c'est 1/6.

Mais que se passe-t-il si je vous dis que j'ai déjà lancé le dé et que le résultat est un nombre pair ? Quelle est la probabilité que nous ayons obtenu un six maintenant ? 

Cette fois, les résultats possibles sont seulement trois car il n'y a que trois nombres pairs sur le dé. Nous nous intéressons toujours à un seul de ces résultats, donc maintenant la probabilité est plus grande : 1/3. Quelle est la différence entre les deux cas ?

Dans le premier cas, nous n'avions aucune information **préalable** sur le résultat. Ainsi, nous devions considérer chaque résultat possible.

Dans le second cas, on nous a dit que le résultat était un nombre pair, donc nous avons pu réduire l'espace des résultats possibles à seulement les trois nombres pairs qui apparaissent sur un dé à six faces régulier.

En général, lorsque nous calculons la probabilité d'un événement A, étant donné l'occurrence d'un autre événement B, nous disons que nous calculons la **probabilité conditionnelle** de A étant donné B, ou simplement la probabilité de A étant donné B. Nous le notons ```P(A|B)```. 

Par exemple, la probabilité d'obtenir un six étant donné que le nombre que nous avons obtenu est pair : ```P(Six|Pair) = 1/3```. Ici, nous avons noté avec **Six** l'événement d'obtenir un six et avec **Pair** l'événement d'obtenir un nombre pair.

Mais, comment calculons-nous les probabilités conditionnelles ? Y a-t-il une formule ?

## Comment calculer les probabilités conditionnelles et le théorème de Bayes

Maintenant, je vais vous donner quelques formules pour calculer les probabilités conditionnelles. Je promets qu'elles ne seront pas difficiles, et elles sont importantes si vous voulez comprendre les algorithmes d'apprentissage automatique dont nous parlerons plus tard.

La probabilité d'un événement A étant donné l'occurrence d'un autre événement B peut être calculée comme suit :

```pseudocode
P(A|B) = P(A,B)/P(B)
```

Où `P(A,B)` désigne la probabilité que A et B se produisent en même temps, et `P(B)` désigne la probabilité de B.

Remarquez que nous avons besoin de `P(B) > 0` car il n'a pas de sens de parler de la probabilité de A étant donné B si l'occurrence de B n'est pas possible.

Nous pouvons également calculer la probabilité d'un événement A, étant donné l'occurrence de plusieurs événements B1, B2,..., Bn :

```pseudocode
P(A|B1,B2,...,Bn) = P(A,B1,B2,...,Bn)/P(B1,B2,...,Bn)
```

Il existe une autre façon de calculer les probabilités conditionnelles. Cette façon est le soi-disant théorème de Bayes.

```pseudocode
P(A|B) = P(B|A)P(A)/P(B)

P(A|B1,B2,...,Bn) = P(B1,B2,...,Bn|A)P(A)/P(B1,B2,...,Bn)
```

Remarquez que nous calculons la probabilité de l'événement A étant donné l'événement B, en _inversant_ l'ordre d'occurrence des événements. 

Maintenant, nous supposons que l'événement A s'est produit et nous voulons calculer la probabilité de l'événement B (ou des événements B1,B2,...,Bn dans le deuxième et plus général exemple).

Un fait important qui peut être dérivé de ce théorème est la formule pour calculer ```P(B1,B2,...,Bn,A)```. Cela s'appelle la règle de la chaîne pour les probabilités.

```pseudocode
P(B1,B2,...,Bn,A) = P(B1 | B2, B3, ..., Bn, A)P(B2,B3,...,Bn,A)
= P(B1 | B2, B3, ..., Bn, A)P(B2 | B3, B4, ..., Bn, A)P(B3, B4, ..., Bn, A)
= P(B1 | B2, B3, ..., Bn, A)P(B2 | B3, B4, ..., Bn, A)...P(Bn | A)P(A)
```

C'est une formule compliquée, n'est-ce pas ? Mais sous certaines conditions, nous pouvons faire un contournement et l'éviter.

Parlons du dernier concept que nous devons connaître pour comprendre les algorithmes.

## Indépendance

Le dernier concept dont nous allons parler est l'indépendance. Nous disons que les événements A et B sont indépendants si

```pseudocode
P(A|B) = P(A)
```

Cela signifie que la probabilité de l'événement A n'est pas affectée par l'occurrence de l'événement B. Une conséquence directe est que ```P(A,B) = P(A)P(B)```. 

En termes simples, cela signifie que la probabilité de l'occurrence de A et B en même temps est égale au produit des probabilités des événements A et B se produisant séparément.

Si A et B sont indépendants, il est également vrai que :

```pseudocode
P(A,B|C) = P(A|C)P(B|C)
```

Maintenant, nous sommes prêts à parler des classificateurs Naive Bayes !

## Classificateurs Naive Bayes

Supposons que nous avons un vecteur **X** de _n_ caractéristiques et que nous voulons déterminer la classe de ce vecteur à partir d'un ensemble de _k_ classes _y1, y2,...,yk_. Par exemple, si nous voulons déterminer s'il va pleuvoir aujourd'hui ou non. 

Nous avons deux classes possibles (_k = 2_) : _pluie_, _pas de pluie_, et la longueur du vecteur de caractéristiques pourrait être de 3 (_n = 3_). 

La première caractéristique pourrait être s'il fait nuageux ou ensoleillé, la deuxième caractéristique pourrait être si l'humidité est élevée ou faible, et la troisième caractéristique serait si la température est élevée, moyenne ou faible. 

Donc, voici quelques exemples de vecteurs de caractéristiques possibles.

```pseudocode
<Nuageux, H_Haute, T_Basse>
<Ensoleillé, H_Basse, T_Moyenne>
<Nuageux, H_Basse, T_Haute>
```

Notre tâche est de déterminer s'il va pleuvoir ou non, étant donné les caractéristiques météorologiques.

Après avoir appris les probabilités conditionnelles, il semble naturel d'aborder le problème en essayant de calculer la probabilité de pluie étant donné les caractéristiques :

```pseudocode
R = P(Pluie | Nuageux, H_Haute, T_Basse)
NR = P(PasPluie | Nuageux, H_Haute, T_Basse)
```

Si ```R > NR``` nous répondons qu'il va pleuvoir, sinon nous disons qu'il ne pleuvra pas.

En général, si nous avons _k_ classes _y1, y2, ..., yk_, et un vecteur de _n_ caractéristiques **X = <X1, X2, ..., Xn>**, nous voulons trouver la classe _yi_ qui maximise

```pseudocode
P(yi | X1, X2, ..., Xn) = P(X1, X2,..., Xn, yi)/P(X1, X2, ..., Xn)
```

Remarquez que le dénominateur est constant et qu'il ne dépend pas de la classe _yi_. Donc, nous pouvons l'ignorer et nous concentrer uniquement sur le numérateur. 

Dans une section précédente, nous avons vu comment calculer `P(X1, X2,..., Xn, yi)` en le décomposant en un produit de probabilités conditionnelles (la formule compliquée) :

```
P(X1, X2,..., Xn, yi) = P(X1 | X2,..., Xn, yi)P(X2 | X3,..., Xn, yi)...P(Xn | yi)P(yi)
```

En supposant que toutes les caractéristiques **Xi** sont indépendantes et en utilisant le théorème de Bayes, nous pouvons calculer la probabilité conditionnelle comme suit :

```
P(yi | X1, X2,..., Xn) = P(X1, X2,..., Xn | yi)P(yi)/P(X1, X2, ..., Xn)
= P(X1 | yi)P(X2 | yi)...P(Xn | yi)P(yi)/P(X1, X2, ..., Xn)
```

Et nous devons nous concentrer uniquement sur le numérateur.

En trouvant la classe _yi_ qui maximise l'expression précédente, nous classons le vecteur d'entrée. Mais, comment pouvons-nous obtenir toutes ces probabilités ?

## Comment calculer les probabilités

Lorsque nous résolvons ce type de problèmes, nous devons avoir un ensemble d'exemples préalablement classés. 

Par exemple, dans le problème de deviner s'il va pleuvoir ou non, nous devons avoir plusieurs exemples de vecteurs de caractéristiques et leurs classifications qui seraient obtenus à partir des prévisions météorologiques passées. 

Donc, nous aurions quelque chose comme ceci :

```pseudocode
...
<Nuageux, H_Haute, T_Basse> -> Pluie
<Ensoleillé, H_Basse, T_Moyenne> -> PasPluie
<Nuageux, H_Basse, T_Haute> -> PasPluie
...
```

Supposons que nous devons classer un nouveau vecteur ```<Nuageux, H_Basse, T_Basse>```. Nous devons calculer :

```
P(Pluie | Nuageux, H_Basse, T_Basse) = P(Nuageux | H_Basse, T_Basse, Pluie)P(H_Basse | T_Basse, Pluie)P(T_Basse | Pluie)P(Pluie)/P(Nuageux, H_Basse, T_Basse)
```

Nous obtenons l'expression précédente en appliquant la définition de la probabilité conditionnelle et la règle de la chaîne. Rappelez-vous que nous devons nous concentrer uniquement sur le numérateur, donc nous pouvons ignorer le dénominateur. 

Nous devons également calculer la probabilité pour ```PasPluie```, mais nous pouvons le faire de manière similaire.

Nous pouvons trouver ```P(Pluie) = # Pluie/Total```. Cela signifie compter les entrées dans le jeu de données qui sont classées avec _Pluie_ et diviser ce nombre par la taille du jeu de données.

Pour calculer ```P(Nuageux | H_Basse, T_Basse, Pluie)``` nous devons compter toutes les entrées qui ont les caractéristiques _H_Basse, T_Basse_ et _Nuageux_. Ces entrées doivent également être classées comme ```Pluie```. Ensuite, ce nombre est divisé par le nombre total de données. Nous calculons le reste des facteurs de la formule de manière similaire.

Faire ces calculs pour chaque classe possible est très coûteux et lent. Nous devons donc faire des hypothèses sur le problème qui simplifient les calculs. 

Les classificateurs Naive Bayes supposent que toutes les caractéristiques sont indépendantes les unes des autres. Nous pouvons donc réécrire notre formule en appliquant le théorème de Bayes et en supposant l'indépendance entre chaque paire de caractéristiques :

```
P(Pluie | Nuageux, H_Basse, T_Basse) = P(Nuageux | Pluie)P(H_Basse | Pluie)P(T_Basse | Pluie)P(Pluie)/P(Nuageux, H_Basse, T_Basse)
```

Maintenant, nous calculons `P(Nuageux | Pluie)` en comptant le nombre d'entrées classées comme `Pluie` et qui étaient `Nuageux`.

>L'algorithme est appelé _Naive_ à cause de cette hypothèse d'indépendance. Il y a des dépendances entre les caractéristiques la plupart du temps. Nous ne pouvons pas dire que dans la vie réelle il n'y a pas de dépendance entre l'humidité et la température, par exemple. Les classificateurs Naive Bayes sont également appelés Bayes Indépendants, ou Bayes Simples.
>

La formule générale serait :

```
P(yi | X1, X2, ..., Xn) = P(X1 | yi)P(X2 | yi)...P(Xn | yi)P(yi)/P(X1, X2, ..., Xn)
```

Rappelez-vous que vous pouvez vous débarrasser du dénominateur. Nous calculons uniquement le numérateur et répondons la classe qui le maximise.

Maintenant, implémentons notre NBC et utilisons-le dans un problème.

## Codons !

Je vais vous montrer une implémentation d'un NBC simple, puis nous le verrons en pratique. 

Le problème que nous allons résoudre est de déterminer si un passager du Titanic a survécu ou non, étant donné certaines caractéristiques comme son sexe et son âge.

Voici une implémentation très simple d'un NBC :

```python
class NaiveBayesClassifier:
    
    def __init__(self, X, y):
        
        '''
        X et y désignent respectivement les caractéristiques et les étiquettes cibles
        '''
        self.X, self.y = X, y 
        
        self.N = len(self.X) # Longueur de l'ensemble d'entraînement

        self.dim = len(self.X[0]) # Dimension du vecteur de caractéristiques

        self.attrs = [[] for _ in range(self.dim)] # Ici nous stockerons les colonnes de l'ensemble d'entraînement

        self.output_dom = {} # Classes de sortie avec le nombre d'occurrences dans l'ensemble d'entraînement. Dans ce cas, nous avons seulement 2 classes

        self.data = [] # Pour stocker chaque ligne [Xi, yi]
        
        
        for i in range(len(self.X)):
            for j in range(self.dim):
                # si nous n'avons jamais vu cette valeur pour cet attribut auparavant, 
                # alors nous l'ajoutons au tableau attrs à la position correspondante
                if not self.X[i][j] in self.attrs[j]:
                    self.attrs[j].append(self.X[i][j])
                    
            # si nous n'avons jamais vu cette classe de sortie auparavant,
            # alors nous l'ajoutons à output_dom et comptons une occurrence pour l'instant
            if not self.y[i] in self.output_dom.keys():
                self.output_dom[self.y[i]] = 1
            # sinon, nous incrémentons l'occurrence de cette sortie dans l'ensemble d'entraînement de 1
            else:
                self.output_dom[self.y[i]] += 1
            # stocker la ligne
            self.data.append([self.X[i], self.y[i]])
            
            

    def classify(self, entry):

        solve = None # Résultat final
        max_arg = -1 # maximum partiel

        for y in self.output_dom.keys():

            prob = self.output_dom[y]/self.N # P(y)

            for i in range(self.dim):
                cases = [x for x in self.data if x[0][i] == entry[i] and x[1] == y] # toutes les lignes avec Xi = xi
                n = len(cases)
                prob *= n/self.N # P *= P(Xi = xi)
                
            # si nous avons une probabilité plus grande pour cette sortie que le maximum partiel...
            if prob > max_arg:
                max_arg = prob
                solve = y

        return solve
```

Ici, nous supposons que chaque caractéristique a un domaine discret. Cela signifie qu'elles prennent une valeur parmi un ensemble fini de valeurs possibles. 

Il en va de même pour les classes. Remarquez que nous stockons certaines données dans la méthode `__init__` afin de ne pas avoir à répéter certaines opérations. La classification d'une nouvelle entrée est effectuée dans la méthode `classify`.

>Il s'agit d'un exemple simple d'une implémentation. Dans les applications réelles, vous n'avez pas besoin (et il est préférable de ne pas faire) votre propre implémentation. Par exemple, la bibliothèque `sklearn` en Python contient plusieurs bonnes implémentations de NBC.
>

Remarquez à quel point il est facile de l'implémenter !

Maintenant, appliquons notre nouveau classificateur pour résoudre un problème. Nous avons un ensemble de données avec la description de 887 passagers du Titanic. Nous pouvons également voir si un passager donné a survécu à la tragédie ou non. 

Donc, notre tâche est de déterminer si un autre passager qui n'est pas inclus dans l'ensemble d'entraînement a survécu ou non.

Dans cet exemple, j'utiliserai la bibliothèque `pandas` pour lire et traiter les données. Je n'utilise aucun autre outil.

Les données sont stockées dans un fichier appelé _titanic.csv_, donc la première étape est de lire les données et d'en obtenir un aperçu.

```python
import pandas as pd

data = pd.read_csv('titanic.csv')

print(data.head())
```

La sortie est :

```text
Survived  Pclass                                               Name  \
0         0       3                             Mr. Owen Harris Braund   
1         1       1  Mrs. John Bradley (Florence Briggs Thayer) Cum...   
2         1       3                              Miss. Laina Heikkinen   
3         1       1        Mrs. Jacques Heath (Lily May Peel) Futrelle   
4         0       3                            Mr. William Henry Allen   

      Sex   Age  Siblings/Spouses Aboard  Parents/Children Aboard     Fare  
0    male  22.0                        1                        0   7.2500  
1  female  38.0                        1                        0  71.2833  
2  female  26.0                        0                        0   7.9250  
3  female  35.0                        1                        0  53.1000  
4    male  35.0                        0                        0   8.0500  
```

Remarquez que nous avons le Nom de chaque passager. Nous n'utiliserons pas cette caractéristique pour notre classificateur car elle n'est pas significative pour notre problème. Nous nous débarrasserons également de la caractéristique Fare car elle est continue et nos caractéristiques doivent être discrètes.

>Il existe des classificateurs Naive Bayes qui supportent les caractéristiques continues. Par exemple, le classificateur Naive Bayes Gaussien.
>

```python
y = list(map(lambda v: 'yes' if v == 1 else 'no', data['Survived'].values)) # valeurs cibles sous forme de chaîne

# Nous n'utiliserons pas le champ 'Name' ni le champ 'Fare'

X = data[['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard']].values # valeurs des caractéristiques
```

Ensuite, nous devons séparer notre ensemble de données en un ensemble d'entraînement et un ensemble de validation. Ce dernier est utilisé pour valider la performance de notre algorithme.

```python
print(len(y)) # >> 887

# Nous prendrons 600 exemples pour l'entraînement et le reste pour le processus de validation
y_train = y[:600]
y_val = y[600:]

X_train = X[:600]
X_val = X[600:]
```

Nous créons notre NBC avec l'ensemble d'entraînement, puis nous classons chaque entrée dans l'ensemble de validation. 

Nous mesurons la précision de notre algorithme en divisant le nombre d'entrées qu'il a correctement classées par le nombre total d'entrées dans l'ensemble de validation.

```python
## Création de l'instance du classificateur Naive Bayes avec les données d'entraînement

nbc = NaiveBayesClassifier(X_train, y_train)


total_cases = len(y_val) # taille de l'ensemble de validation

# Exemples bien classés et mal classés
good = 0
bad = 0

for i in range(total_cases):
    predict = nbc.classify(X_val[i])
#     print(y_val[i] + ' --------------- ' + predict)
    if y_val[i] == predict:
        good += 1
    else:
        bad += 1

print('TOTAL EXAMPLES:', total_cases)
print('RIGHT:', good)
print('WRONG:', bad)
print('ACCURACY:', good/total_cases)
```

La sortie :

```
TOTAL EXAMPLES: 287
RIGHT: 200
WRONG: 87
ACCURACY: 0.6968641114982579
```

Ce n'est pas génial, mais c'est quelque chose. Nous pouvons obtenir une amélioration de la précision d'environ 10 % si nous nous débarrassons d'autres caractéristiques comme _Siblings/Spouses Aboard_ et _Parents/Children Aboard_. 

Vous pouvez voir un notebook avec le code et l'ensemble de données [ici](https://github.com/josejorgers/naive-bayes-classifier-example)

## Conclusions

Aujourd'hui, nous avons des réseaux de neurones et d'autres algorithmes ML complexes et coûteux partout. 

Les NBC sont des algorithmes très simples qui nous permettent d'obtenir de bons résultats dans certains problèmes de classification sans avoir besoin de beaucoup de ressources. Ils s'adaptent également très bien, ce qui signifie que nous pouvons ajouter beaucoup plus de caractéristiques et que l'algorithme restera rapide et fiable.

Même dans un cas où les NBC ne seraient pas adaptés au problème que nous essayons de résoudre, ils pourraient être très utiles comme référence. 

Nous pourrions d'abord essayer de résoudre le problème en utilisant un NBC avec quelques lignes de code et peu d'efforts. Ensuite, nous pourrions essayer d'obtenir de meilleurs résultats avec des algorithmes plus complexes et coûteux. 

Ce processus peut nous faire gagner beaucoup de temps et nous donne un retour immédiat sur le fait que les algorithmes complexes valent vraiment la peine pour notre tâche.

Dans cet article, vous avez lu sur les probabilités conditionnelles, l'indépendance et le théorème de Bayes. Ce sont les concepts mathématiques derrière les classificateurs Naive Bayes. 

Après cela, nous avons vu une implémentation simple d'un NBC et résolu le problème de déterminer si un passager du Titanic a survécu à l'accident.

J'espère que vous avez trouvé cet article utile. Vous pouvez lire des sujets liés à l'informatique dans mon [blog personnel](https://jj.hashnode.dev/) et en me suivant sur [Twitter](https://twitter.com/josejorgexl).