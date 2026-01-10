---
title: Qu'est-ce qu'un filtre de Kalman ? Comment simplifier les données bruyantes
  dans la navigation et la finance
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-08-07T13:42:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-kalman-filter-with-python-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-skitterphoto-63901.jpg
tags:
- name: data analytics
  slug: data-analytics
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Qu'est-ce qu'un filtre de Kalman ? Comment simplifier les données bruyantes
  dans la navigation et la finance
seo_desc: 'In a world where precision is key, handling noisy data effectively is crucial
  for solving complex problems.

  Whether you''re trying to control a rocket or forecast the stock market, the ability
  to get good data from an uncertain environment is importan...'
---

Dans un monde où la précision est essentielle, le traitement efficace des données bruyantes est crucial pour résoudre des problèmes complexes.

Que vous essayiez de contrôler une fusée ou de prévoir le marché boursier, la capacité à obtenir de bonnes données à partir d'un environnement incertain est importante.

C'est exactement le problème que les filtres de Kalman aident à résoudre. Les filtres de Kalman offrent une solution qui vous aide à traiter les données bruyantes dans de nombreux domaines.

Dans cet article, nous discuterons de :

* [Conduire à travers le brouillard : les filtres de Kalman comme vos phares](#heading-conduire-a-travers-le-brouillard-les-filtres-de-kalman-comme-vos-phares)
* [Qu'est-ce que les filtres de Kalman ?](#heading-quest-ce-que-les-filtres-de-kalman)
* [Filtres de Kalman en action : un exemple de code étape par étape](#heading-filtres-de-kalman-en-action-un-exemple-de-code-etape-par-etape)
* [Conclusion : Naviguer dans les données non linéaires avec des techniques avancées](#heading-conclusion-naviguer-dans-les-donnees-non-lineaires-avec-des-techniques-avancees)

<h2 id="Conduire">Conduire à travers le brouillard : les filtres de Kalman comme vos phares</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-eberhardgross-1287075.jpg)
_Photo par eberhard grossgasteiger : https://www.pexels.com/photo/forest-under-clouds-1287075/_

Imaginez que vous conduisez à travers un brouillard dense avec une visibilité limitée.

Pour atteindre la destination, vous vous fiez à vos sens et au système de navigation de votre voiture qui combine des données en temps réel avec une carte prédéterminée.

En vous déplaçant, le système de navigation de la voiture est toujours en train de s'ajuster pour atteindre la destination, et vous vous fiez toujours à vos sens pour bien conduire la voiture.

Ce processus est très similaire à la façon dont un filtre de Kalman fonctionne.

Il est constamment mis à jour et affine les estimations en fonction des données entrantes. Même si ces données sont pleines de bruit et d'incertitude.

En intégrant les informations passées avec les informations actuelles, un filtre de Kalman vous donne une image claire de l'endroit où vous vous trouvez et de l'endroit où vous vous dirigez.

## Qu'est-ce que les filtres de Kalman ?

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-mikebirdy-170811.jpg)
_Photo par [Mike Bird sur Pexels](https://www.pexels.com/photo/blue-bmw-sedan-near-green-lawn-grass-170811/)_

Un filtre de Kalman est un algorithme mathématique utilisé pour trouver l'état d'un système dynamique à partir de nombreuses mesures bruyantes.

Il est souvent utilisé pour des systèmes qui changent avec le temps – comme le suivi de la position d'un objet en mouvement.

### Comment fonctionne un filtre de Kalman ?

Le filtre de Kalman prédit votre état actuel en fonction des données passées, comme la carte et votre position précédente.

Lorsque de nouvelles données apparaissent, comme de nouveaux signaux GPS, le filtre compare les nouvelles données avec sa prédiction et ajuste son estimation.

Même si les données sont bruyantes, le filtre de Kalman utilise un processus de moyenne intelligent pour améliorer l'estimation. Comme la façon dont vous équilibrez ce que votre système de navigation vous dit et ce que vous voyez sur la route.

En intégrant toujours les nouvelles données avec les données passées, les filtres de Kalman vous aident à savoir où vous êtes et où vous allez. De cette façon, il est possible de prédire des choses même dans des conditions incertaines.

### Pourquoi les filtres de Kalman sont-ils utilisés en ingénierie ?

Puisque les filtres de Kalman sont capables de gérer des données incomplètes, ils sont largement utilisés pour faire de bonnes prédictions même lorsque les mesures ne sont pas certaines.

Cela les rend très utiles pour :

* **Systèmes de navigation** : Estimation de la position et de la vitesse des véhicules.
* **Robotique** : Aider les robots à comprendre leur environnement et leur position.
* **Finance** : Filtrer le bruit des données de prix des actions pour prédire les tendances.

De cette façon, ils sont très adaptatifs et peuvent traiter des informations en temps réel.

### Quel problème les filtres de Kalman ont-ils résolu ?

Les filtres de Kalman ont été développés par Rudolf Kalman au début des années 1960 pour résoudre le problème de la gestion de l'incertitude et du bruit dans les données.

De nos jours, ils sont excellents pour extraire des informations significatives à partir de données bruyantes.

Mathématiquement, les filtres de Kalman sont appelés estimateurs quadratiques linéaires.

C'est parce que, dans le processus d'estimation du futur basé sur les données actuelles et passées, les filtres de Kalman utilisent :

* Algèbre linéaire : L'étude des vecteurs et des matrices utilisés pour résoudre des équations linéaires.
* Optimisation quadratique : Trouver la solution optimale pour des problèmes avec des termes au carré.

<h2 id="Kalman">Filtres de Kalman en action : un tutoriel de code étape par étape</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-captainsopon-3402846.jpg)
_Photo par capt.sopon : https://www.pexels.com/photo/gray-airplane-control-panel-3402846/_

Les filtres de Kalman ont été créés pour gérer les systèmes linéaires – c'est-à-dire les systèmes qui suivent des motifs prévisibles.

Dans cet exemple de code, nous allons implémenter un filtre de Kalman étendu. Il s'agit d'une variante qui a été créée pour gérer les données non linéaires (en d'autres termes, les systèmes qui ont des motifs imprévisibles ou changeants).

Voici le code complet (que nous allons décomposer ci-dessous) :

```
import numpy as np
from filterpy.kalman import ExtendedKalmanFilter as EKF
from filterpy.common import Q_discrete_white_noise

def fx(x, dt):
    """ Fonction de transition d'état pour le système non linéaire. """
    # Exemple : x' = [x[0] + x[1]*dt, x[1]]
    F = np.array([x[0] + x[1]*dt, x[1]])
    return F

def hx(x):
    """ Fonction de mesure pour le système non linéaire. """
    # Exemple : z = [x[0]]
    return np.array([x[0]])

def jacobian_F(x, dt):
    """ Jacobien de la fonction de transition d'état. """
    return np.array([[1, dt],
                     [0, 1]])

def jacobian_H(x):
    """ Jacobien de la fonction de mesure. """
    return np.array([[1, 0]])

# Initialiser EKF
ekf = EKF(dim_x=2, dim_z=1)

# État initial
ekf.x = np.array([0, 1])

# Covariance de l'état initial
ekf.P = np.eye(2)

# Covariance du bruit de processus
ekf.Q = Q_discrete_white_noise(dim=2, dt=1, var=0.1)

# Covariance du bruit de mesure
ekf.R = np.array([[0.1]])

# Définir les fonctions de transition d'état et de mesure
ekf.F = jacobian_F
ekf.H = jacobian_H

# Entrée de contrôle
dt = 1.0  # pas de temps

# Mesures simulées
measurements = [1, 2, 3, 4, 5]

for z in measurements:
    # Étape de prédiction
    ekf.predict_update(z, HJacobian=jacobian_H, Hx=hx, Fx=fx, args=(dt,), hx_args=())

    # Imprimer l'estimation actuelle de l'état
    print("État estimé :", ekf.x)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/1-2.png)
_Code complet_

Examinons le code bloc par bloc.

### Importer les bibliothèques

```
import numpy as np
from filterpy.kalman import ExtendedKalmanFilter as EKF
from filterpy.common import Q_discrete_white_noise

```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/2-2.png)
_Importation des bibliothèques_

Dans cette partie du code, nous importons les bibliothèques Python dont nous avons besoin :

* **`import numpy as np`** : Cela importe un outil appelé [NumPy](https://numpy.org/), qui nous aide à travailler avec des nombres et des listes de nombres (comme une feuille de calcul).
* **`from [filterpy](https://filterpy.readthedocs.io/en/latest/).kalman import ExtendedKalmanFilter as EKF`** : Cela apporte un outil appelé `ExtendedKalmanFilter` de la bibliothèque `filterpy`. Nous utiliserons cet outil, nommé `EKF` ici, pour suivre les choses qui changent avec le temps de manière non linéaire.
* **`from [filterpy](https://filterpy.readthedocs.io/en/latest/).common import Q_discrete_white_noise`** : Cela importe une fonction qui nous aide à configurer le bruit, qui est comme le "flou" naturel ou l'incertitude dans notre système.

### Définir le fonctionnement du système

```
def fx(x, dt):
    """ Fonction de transition d'état pour le système non linéaire. """
    # Exemple : x' = [x[0] + x[1]*dt, x[1]]
    return np.array([x[0] + x[1]*dt, x[1]])

def hx(x):
    """ Fonction de mesure pour le système non linéaire. """
    # Exemple : z = [x[0]]
    return np.array([x[0]])
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/3-3.png)
_Définir le fonctionnement du système_

Dans ce code, nous définissons comment le système fonctionnera :

* **`fx(x, dt)`** : Cette fonction décrit comment notre système change avec le temps. Elle dit que la nouvelle position est l'ancienne position plus la vitesse fois le temps (`x[0] + x[1]*dt`). La vitesse (`x[1]`) reste la même.
* **`hx(x)`** : Cette fonction nous dit ce que nous pouvons mesurer à partir du système. Ici, elle dit que nous pouvons mesurer la position (`x[0]`).

### Définir comment les changements affectent le système

```
def jacobian_F(x, dt):
    """ Jacobien de la fonction de transition d'état. """
    return np.array([[1, dt],
                     [0, 1]])

def jacobian_H(x):
    """ Jacobien de la fonction de mesure. """
    return np.array([[1, 0]])
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/4-2.png)
_Définir comment le système fonctionne_

Dans ce code, nous définissons comment les changements affectent le système :

* **`jacobian_F(x, dt)`** : Cette fonction nous montre à quel point le système est sensible aux changements dans le temps et la position. Elle aide le filtre à prédire les changements plus précisément en tenant compte de ces sensibilités.
* **`jacobian_H(x)`** : Cette fonction nous dit à quel point notre mesure est sensible aux changements de position. Elle aide le filtre à ajuster la prédiction en fonction des nouvelles mesures.

### Configurer le filtre de Kalman

```
# Initialiser EKF
ekf = EKF(dim_x=2, dim_z=1)

# État initial
ekf.x = np.array([0, 1])
print("État initial :", ekf.x)

# Covariance de l'état initial
ekf.P = np.eye(2)
print("Covariance de l'état initial :\n", ekf.P)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/5-2.png)
_Configurer le filtre de Kalman_

Dans cette partie du code, nous créons un filtre de Kalman très simple :

* **`ekf = EKF(dim_x=2, dim_z=1)`** : Cela crée un filtre de Kalman étendu qui suit deux choses (position et vitesse) et une mesure (position).
* **`ekf.x = np.array([0, 1])`** : Cela définit la position de départ à `0` et la vitesse à `1`.

Il imprime :

```
État initial : [0 1]
```

* **`ekf.P = np.eye(2)`** : C'est une façon de dire que nous ne sommes pas très sûrs de nos suppositions de départ. C'est comme dire "commençons d'ici, mais nous sommes ouverts aux changements."

Il imprime :

```
Covariance de l'état initial :
 [[1. 0.]
 [0. 1.]]
```

### Décrire l'incertitude dans le système

```
# Covariance du bruit de processus
ekf.Q = Q_discrete_white_noise(dim=2, dt=1, var=0.1)
print("Covariance du bruit de processus :\n", ekf.Q)

# Covariance du bruit de mesure
ekf.R = np.array([[0.1]])
print("Covariance du bruit de mesure :\n", ekf.R)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/6-2.png)
_Décrire l'incertitude dans le système_

* **`ekf.Q = Q_discrete_white_noise(dim=2, dt=1, var=0.1)`** : Cela définit la quantité d'aléatoire ou d'imprévisibilité que nous attendons dans le système lui-même. C'est comme dire, "les choses ne bougent peut-être pas exactement comme nous le pensons."

Il imprime :

```
Covariance du bruit de processus :
 [[0.025 0.05 ]
 [0.05  0.1  ]]
```

* **`ekf.R = np.array([[0.1]])`** : Cela définit à quel point nous faisons confiance à nos mesures. Un nombre plus petit signifie que nous leur faisons plus confiance.

```
Covariance du bruit de mesure :
 [[0.1]]
```

### Simuler les données et l'état initial

```
# Entrée de contrôle
dt = 1.0  # pas de temps

# Mesures simulées
measurements = [1, 2, 3, 4, 5]

# Vrai état initial pour comparaison (non utilisé dans l'EKF)
true_state = np.array([0, 1])
print("\nVrai état initial :", true_state)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/7-2.png)
_Simuler les données et l'état initial_

* **`dt = 1.0`** : C'est le temps entre chaque étape de notre simulation.
* **`measurements = [1, 2, 3, 4, 5]`** : Ce sont les mesures fictives que nous utiliserons pour tester le filtre.
* **`true_state = np.array([0, 1])`** : C'est la vraie position et vitesse de départ de notre système, utilisée pour comparaison.

Il donne :

```
Vrai état initial : [0 1]
```

### Simuler les changements réels du système

```
# Simuler l'évolution du vrai état (pour comparaison)
true_states = [true_state[0]]
for _ in range(len(measurements) - 1):
    true_state = fx(true_state, dt)
    true_states.append(true_state[0])

print("\nÉtats vrais simulés (pour référence) :", true_states)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/8-1.png)
_Simuler les changements réels du système_

* **Simuler les vrais états** : Cette partie calcule ce que devrait être la vraie position au fil du temps en utilisant le fonctionnement du système (`fx`). C'est comme avoir un GPS parfait pour vérifier nos estimations.

```
États vrais simulés (pour référence) : [0, 1.0, 2.0, 3.0, 4.0]

```

### Étapes du filtre pour estimer l'état

```
for i, z in enumerate(measurements):
    print(f"\nÉtape {i+1} :")
    print("Mesure :", z)

    # Étape de prédiction
    ekf.predict(u=0)  # Utilisez predict_x si vous devez personnaliser la prédiction
    print("État prédit avant la mise à jour :", ekf.x)

    # Étape de mise à jour
    ekf.update(z, HJacobian=jacobian_H, Hx=hx, args=(), hx_args=())
    print("État mis à jour après la mesure :", ekf.x)
    print("Covariance de l'état après la mise à jour :\n", ekf.P)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/9.png)
_Étapes du filtre pour estimer l'état_

**Boucle à travers les mesures** : Cette boucle passe par chaque fausse mesure une par une.

* **Étape de prédiction (`ekf.predict(u=0)`)** : Avant de regarder la nouvelle mesure, le filtre fait une supposition sur l'endroit où se trouvent la position et la vitesse maintenant.
* **Étape de mise à jour (`ekf.update`)** : Après la supposition, le filtre voit la nouvelle mesure et ajuste sa supposition pour être plus proche de cette mesure, en équilibrant la nouvelle information avec ce qu'il avait précédemment prédit.

Voici les résultats :

```
Étape 1 :
Mesure : 1
État prédit avant la mise à jour : [0. 1.]
État mis à jour après la mesure : [0.91111111 1.04444444]
Covariance de l'état après la mise à jour :
 [[0.09111111 0.00444444]
 [0.00444444 1.09777778]]

Étape 2 :
Mesure : 2
État prédit avant la mise à jour : [0.91111111 1.04444444]
État mis à jour après la mesure : [1.49614396 1.31876607]
Covariance de l'état après la mise à jour :
 [[0.05372751 0.0251928 ]
 [0.0251928  1.1840617 ]]

Étape 3 :
Mesure : 3
État prédit avant la mise à jour : [1.49614396 1.31876607]
État mis à jour après la mesure : [2.15857605 1.95145631]
Covariance de l'état après la mise à jour :
 [[0.0440489  0.0420712 ]
 [0.0420712  1.25242718]]

Étape 4 :
Mesure : 4
État prédit avant la mise à jour : [2.15857605 1.95145631]
État mis à jour après la mesure : [2.91071524 2.95437384]
Covariance de l'état après la mise à jour :
 [[0.04084552 0.05446424]
 [0.05446424 1.30228131]]

Étape 5 :
Mesure : 5
État prédit avant la mise à jour : [2.91071524 2.95437384]
État mis à jour après la mesure : [3.74022237 4.27039095]
Covariance de l'état après la mise à jour :
 [[0.03970292 0.06298888]
 [0.06298888 1.33648045]]
```

<h2 id="Au-dela">Conclusion : Naviguer dans les données non linéaires avec des techniques avancées</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-noellegracephotos-906055.jpg)
_Photo par [Noelle Otto sur Pexels](https://www.pexels.com/photo/close-up-photography-of-magnifying-glass-906055/)_

Les filtres de Kalman sont un outil puissant pour extraire des estimations précises à partir de données bruyantes et incomplètes.

Des variantes comme le filtre de Kalman étendu (EKF) et le filtre de Kalman non parfumé (UKF) ont été développées pour traiter les non-linéarités dans les données.

Cependant, ces variantes peuvent encore rencontrer des défis liés à la stabilité et à la précision lorsqu'elles sont appliquées à des systèmes non linéaires complexes.

Cela est dû à leur dépendance aux approximations linéaires, qui peuvent ne pas capturer la dynamique complète des processus hautement non linéaires.

Pour surmonter ces limitations, des méthodes alternatives telles que les approches basées sur les réseaux de neurones ont gagné en attention.

Les réseaux de neurones peuvent apprendre des motifs complexes directement à partir des données, offrant une solution robuste pour les scénarios hautement non linéaires.

Malgré ces avancées, les filtres de Kalman restent un outil important dans divers domaines de la science et de l'économie en raison de leur simplicité, de leur efficacité et de leur efficacité dans une large gamme d'applications.

À mesure que la technologie continue d'évoluer, l'intégration des filtres de Kalman avec d'autres techniques avancées améliorera probablement leur capacité à naviguer dans les défis des données non linéaires de manière plus efficace.

Voici le code complet :

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]