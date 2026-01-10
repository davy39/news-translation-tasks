---
title: Qu'est-ce que l'échantillonnage aléatoire stratifié ? Définition et exemple
  en Python
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-11-15T16:33:52.000Z'
originalURL: https://freecodecamp.org/news/what-is-stratified-random-sampling-definition-and-python-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-viktorya-sergeeva
seo_title: Qu'est-ce que l'échantillonnage aléatoire stratifié ? Définition et exemple
  en Python
---

-----10275085.jpg
tags:
- name: Python
  slug: python
- name: statistiques
  slug: statistiques
seo_title: null
seo_desc: 'Lorsque nous souhaitons mener une expérience sur une population – par exemple, l'ensemble de la population d'un pays – il n'est pas toujours pratique ou réaliste d'inclure chaque sujet (citoyen) dans l'expérience.

Au lieu de cela, nous nous appuyons sur un échantillon, qui est un sous-ensemble de la population, puis nous tirons des conclusions sur la population en fonction des résultats de l'échantillon.'
---

Lorsque nous souhaitons mener une expérience sur une population – par exemple, l'ensemble de la population d'un pays – il n'est pas toujours pratique ou réaliste d'inclure chaque sujet (citoyen) dans l'expérience.

Au lieu de cela, nous nous appuyons sur un échantillon, qui est un sous-ensemble de la population, puis nous tirons des conclusions sur la population en fonction des résultats de l'échantillon.

Maintenant, tirer un échantillon d'une population est connu sous le nom de technique d'échantillonnage, et la manière dont l'échantillon est tiré est essentielle au résultat.

Il existe de nombreuses techniques d'échantillonnage, mais dans ce tutoriel, nous allons examiner l'une d'entre elles appelée échantillonnage aléatoire stratifié et son fonctionnement. Sans plus attendre, commençons.

## Qu'est-ce que l'échantillonnage aléatoire stratifié ?

Avant d'entrer dans les détails de l'échantillonnage aléatoire stratifié, décomposons le terme en parties pour mieux le comprendre. Commençons par stratifié.

Dans le contexte de l'échantillonnage, **stratifié** signifie diviser la population en groupes plus petits ou strates en fonction d'une caractéristique. En d'autres termes, vous divisez une population en groupes en fonction de leurs caractéristiques.

L'**échantillonnage aléatoire** consiste à sélectionner aléatoirement des sujets (entités) dans une population. Chaque sujet a une probabilité égale d'être choisi dans la population pour former un échantillon (sous-population) de la population globale.

Ainsi, l'**échantillonnage aléatoire stratifié** est une approche d'échantillonnage dans laquelle la population est séparée en groupes ou strates en fonction d'une caractéristique particulière. Ensuite, des sujets de chaque strate (le singulier de strates) sont échantillonnés aléatoirement.

Vous divisez la population en groupes en fonction d'une caractéristique, puis vous choisissez un sujet ou une entité aléatoirement dans chaque groupe.

## Types d'échantillonnage aléatoire stratifié

L'échantillonnage stratifié est divisé en deux catégories, qui sont :

* Échantillonnage aléatoire stratifié proportionnel.

* Échantillonnage aléatoire stratifié disproportionné.

L'**échantillonnage aléatoire stratifié proportionnel** est un type d'échantillonnage dans lequel la taille de l'échantillon aléatoire obtenu à partir de chaque strate est proportionnelle à la taille de la population de l'ensemble de la strate.

En d'autres termes, la proportion de l'ensemble de la strate est égale à la proportion de la strate de l'échantillon. Considérons l'exemple suivant :

```python
students = {

    "Name": ["Ibrahim", "Ganiyat", "Joel", "Elijah", "Yusuf", "Nurain", 
            "Dayo", "David", "Olu", "Tobi"],

    "ID":  ['001', '002', '003', '004', '005', '006','007', '008', '009', '010'],

    "Grade": ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'A', 'B', 'A'],

    "Category": [1, 2, 2, 1, 3, 3, 1, 2, 3, 3]
}
df = pd.DataFrame(students)
>>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-35.png align="left")

Le dataframe ci-dessus contient les noms, les identifiants, les notes et les catégories des étudiants. Supposons que nous souhaitons stratifier les étudiants en fonction de leurs caractéristiques de notes et échantillonner 60 % des étudiants de chaque groupe. Cela signifie que nous aurons trois strates dans le dataframe ci-dessus, car nous avons trois notes différentes.

Nous pouvons l'échantillonner en tapant ce qui suit :

```python
df_sample = df.groupby("Grade", group_keys=False).apply(lambda x:x.sample(frac=0.6))
```

Ce que nous avons fait ci-dessus, c'est regrouper le dataframe en différentes strates en utilisant la méthode `groupby()`. Ensuite, nous avons passé la caractéristique `Grade`. Pour chaque groupe (strate), nous avons échantillonné aléatoirement `0.6 (60%)` des observations.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-36.png align="left")

Maintenant, si nous regardons la proportion pour `df_sample` et `df`, nous verrons que les proportions pour les deux dataframes sont les mêmes.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-37.png align="left")

L'**échantillonnage aléatoire stratifié disproportionné**, en revanche, implique de sélectionner aléatoirement des strates sans tenir compte de la proportion. En d'autres termes, l'échantillonnage est effectué en fonction d'un nombre spécifié. Examinons un exemple.

```python
df.groupby('Grade', group_keys=False).apply(lambda x: x.sample(n=2))
```

Dans ce code, vous pouvez voir que nous avons uniquement spécifié le nombre réel d'échantillons que nous souhaitons obtenir.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-38.png align="left")

La plupart du temps, vous utiliserez l'échantillonnage stratifié proportionnel. L'échantillonnage disproportionné nécessite plus de connaissances expertes. Lorsque vous effectuez un échantillonnage stratifié, vous utiliserez probablement l'échantillonnage proportionnel.

## Applications de l'échantillonnage aléatoire stratifié

### 1. Échantillonnage basé sur une caractéristique partagée :

Lorsque un ou plusieurs sujets dans une expérience partagent des caractéristiques, cela suggère qu'ils sont membres du même groupe (un sujet ne peut être que dans un groupe particulier).

Par exemple, supposons que 50 étudiants passent un test, et que la plage de notes pour l'examen est simplement A-E. Nous pouvons donc avoir des étudiants qui sont dans le même groupe de notes, par exemple, des étudiants qui ont reçu un A (et il est impossible pour un étudiant d'avoir deux notes). Par conséquent, ils partagent la même caractéristique ou le même trait, qui est la note.

Ainsi, lorsque vous souhaitez échantillonner des sujets en fonction de caractéristiques partagées, vous devez utiliser l'échantillonnage aléatoire stratifié. Cela garantit qu'un membre d'un groupe spécifique sera inclus.

Cela est dû au fait que l'échantillonnage aléatoire stratifié diffère de l'échantillonnage aléatoire simple, qui est également une technique d'échantillonnage. L'échantillonnage aléatoire stratifié échantillonne aléatoirement la population sans caractéristiques (c'est-à-dire que chaque sujet de la population a des chances égales d'être choisi).

Par conséquent, l'échantillonnage aléatoire simple ne peut pas garantir qu'un certain membre d'un groupe particulier sera inclus dans l'échantillon.

Examinons un exemple pour voir de quoi nous parlons. Supposons que nous voulons échantillonner 60 % des étudiants en utilisant à la fois l'échantillonnage stratifié et l'échantillonnage aléatoire simple.

Nous pouvons voir le résultat pour l'échantillonnage aléatoire stratifié ci-dessous :

```python
df.groupby('Grade', group_keys=False).apply(lambda x: x.sample(frac=0.6))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-39.png align="left")

Et voici le résultat de l'échantillonnage aléatoire simple :

```python
df.sample(frac= 0.6)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-40.png align="left")

Nous pouvons voir que les étudiants avec des notes C ne sont pas inclus dans l'échantillon. Cela est dû au fait que dans l'échantillonnage aléatoire simple, chaque observation a une chance égale d'être choisie car nous n'échantillonnons pas en fonction des caractéristiques. Cela signifie qu'il y a une chance qu'une observation ne soit pas choisie.

Dans l'échantillonnage aléatoire stratifié, en revanche, nous considérons tous les groupes que nous voulons échantillonner, puis nous échantillonnons aléatoirement à partir de chaque groupe.

### 2. Ensemble de données déséquilibré :

Un ensemble de données déséquilibré est un problème de classification en apprentissage automatique dans lequel les deux étiquettes de classe dans la variable cible ne sont pas proportionnelles l'une à l'autre. En d'autres termes, une classe a un compte plus élevé que l'autre, ce qui entraîne un déséquilibre.

En apprentissage automatique, l'échantillonnage stratifié est également utilisé pour obtenir la même proportion d'échantillon pour un ensemble d'entraînement et de test s'il y a un déséquilibre dans l'ensemble de données.

Par exemple, un ensemble de données sur les maladies chroniques a une étiquette déséquilibrée comme montré ci-dessous. Vous pouvez cliquer [ici](https://www.kaggle.com/datasets/mansoordaku/ckdisease/download?datasetVersionNumber=1) pour télécharger l'ensemble de données.

```python
df = pd.read_csv("kidney_disease.csv")
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-41.png align="left")

Si nous vérifions la proportion de l'étiquette de la caractéristique qui est `classification`, nous pouvons voir qu'elle est déséquilibrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-42.png align="left")

Maintenant, supposons que nous voulons diviser l'ensemble d'entraînement et de test en utilisant l'échantillonnage aléatoire simple. Nous n'obtiendrons pas la même proportion pour l'ensemble d'entraînement et de test que la proportion de la population.

```python
from sklearn.model_selection import train_test_split
X = df.drop(columns = ["classification"])
y = df["classification"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-43.png align="left")

Nous pouvons voir que la proportion de l'étiquette pour `y_train` et `y_test` n'est pas la même que la proportion de la population. Pour obtenir la même proportion, nous pouvons utiliser le paramètre `stratify` dans `train_test_split` comme montré ci-dessous :

```python
from sklearn.model_selection import train_test_split
X = df.drop(columns = ["classification"])
y = df["classification"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y)
```

Le code ci-dessus montre que l'ensemble de données a été stratifié sur l'étiquette. Ainsi, avec cela, nous obtiendrons la même proportion que la proportion de la population.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-44.png align="left")

## Conclusion

Dans ce tutoriel, nous avons examiné l'échantillonnage stratifié et comment vous pouvez l'utiliser en statistiques et en apprentissage automatique. Nous avons également examiné les types d'échantillonnage stratifié.

Merci pour votre temps.