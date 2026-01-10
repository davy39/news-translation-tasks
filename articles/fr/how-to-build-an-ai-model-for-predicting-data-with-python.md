---
title: Comment construire un modèle d'IA quantique pour prédire les données de fleurs
  d'iris avec Python
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-08-08T13:18:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ai-model-for-predicting-data-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-guvo-20731157.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Comment construire un modèle d'IA quantique pour prédire les données de
  fleurs d'iris avec Python
seo_desc: 'Machine learning is an area of AI where the likes of ChatGPT and other
  famous models were created. These systems were all created with neural networks.

  The field of machine learning that deals with the creation of these neural networks
  is called deep...'
---

L'apprentissage automatique est un domaine de l'IA où des modèles célèbres comme ChatGPT et d'autres ont été créés. Ces systèmes ont tous été créés avec des réseaux de neurones.

Le domaine de l'apprentissage automatique qui traite de la création de ces réseaux de neurones est appelé apprentissage profond.

Dans cet article de blog, nous allons créer un réseau de neurones avec certains neurones qui fonctionnent sur un ordinateur classique et d'autres sur des ordinateurs quantiques.

Ainsi, la création et l'entraînement d'un réseau de neurones avec ces deux types de neurones donnera un modèle d'IA basé sur l'informatique quantique, car la plupart du traitement se déroulera dans les neurones quantiques.

Nous parlerons de ces sujets :

* [Introduction à l'IA, aux réseaux de neurones hybrides et à leurs avantages](#heading-introduction-a-lia-aux-reseaux-de-neurones-hybrides-et-a-leurs-avantages)
* [L'IA quantique en action : Prédire les données de fleurs d'iris avec Python](#heading-lia-quantique-en-action-predire-les-donnees-de-fleurs-diris-avec-python)
* [Conclusion : L'avenir des modèles d'IA efficaces](#heading-conclusion-lavenir-des-modeles-dia-efficaces)

**Note :** Nous allons créer un réseau de neurones simple, en évitant les architectures complexes comme les transformers, les plongées profondes dans la physique quantique ou les techniques avancées d'optimisation des modèles d'IA.

Le code complet est disponible [ici](https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code).

<h2 id = "Introduction">Introduction à l'IA, aux réseaux de neurones hybrides et à leurs avantages</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-pavel-danilyuk-8438918.jpg)
_Photo par Pavel Danilyuk : https://www.pexels.com/photo/elderly-man-thinking-while-looking-at-a-chessboard-8438918/_

### Qu'est-ce que l'apprentissage profond en intelligence artificielle ?

L'apprentissage profond est un sous-domaine de l'IA qui utilise des réseaux de neurones pour prédire des motifs complexes comme la météo, la classification d'images, la réponse à du texte, et ainsi de suite.

Plus le réseau de neurones est grand, plus il peut faire des choses complexes. Comme ChatGPT, qui peut traiter le langage naturel pour interagir avec les utilisateurs.

### Réseaux de neurones

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Firefox_Screenshot_2024-08-03T13-56-12.699Z.png)
_Réseau de neurones simple_

L'apprentissage profond est l'entraînement de réseaux de neurones pour prédire des données futures. L'entraînement d'un réseau de neurones implique de lui fournir des données, de lui permettre d'apprendre, puis de faire des prédictions.

Les réseaux de neurones sont composés de nombreux neurones organisés en couches. Toutes les couches obtiennent différents motifs des données.

Cette structure en couches permet aux modèles d'IA d'interpréter des données et des motifs complexes. Par exemple, le réseau de neurones dans l'image ci-dessus peut, par exemple, avec 8 caractéristiques de données météorologiques, être entraîné pour prédire s'il va pleuvoir ou non.

La couche qui reçoit les données est appelée couche d'entrée et la dernière est appelée couche de sortie. Entre ces couches se trouvent les couches cachées qui capturent des motifs complexes.

Bien sûr, il s'agit d'un réseau de neurones très simple, mais l'idée d'entraîner un réseau de neurones est la même pour toute architecture complexe.

### Réseaux de neurones hybrides - Combinaison de l'informatique quantique et classique

Nous allons maintenant créer un réseau de neurones hybride. Essentiellement, les couches d'entrée et de sortie fonctionneront sur des ordinateurs classiques tandis que la couche cachée traitera les données sur un ordinateur quantique.

Cette approche utilise le meilleur de l'informatique classique et quantique pour entraîner un réseau de neurones.

### Pourquoi choisir les réseaux de neurones hybrides plutôt que les réseaux de neurones traditionnels ?

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-weekendplayer-45072.jpg)
_Photo par Burak The Weekender : https://www.pexels.com/photo/lighted-light-bulb-in-selective-focus-photography-45072/_

L'idée principale de l'utilisation d'un réseau de neurones hybride est de faire en sorte que le traitement des données se déroule sur un ordinateur quantique, ce qui est beaucoup plus rapide qu'un ordinateur classique.

De plus, les ordinateurs quantiques effectuent certaines tâches avec une consommation d'énergie bien moindre. Cette efficacité dans le traitement et l'utilisation de l'énergie permet la création de modèles d'IA plus petits et plus fiables.

C'est l'idée principale d'un réseau de neurones hybride : créer des modèles d'IA plus petits et plus efficaces.

<h2 id = "Quantum">L'IA quantique en action : Prédire les données de fleurs d'iris avec Python</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-googledeepmind-25626507.jpg)
_Photo par Google DeepMind : https://www.pexels.com/photo/quantum-computing-and-ai-25626507/_

Dans ce code, nous allons créer un modèle d'IA basé sur le quantique pour prédire les espèces de fleurs d'iris à partir du célèbre jeu de données Iris.

Le code utilise un simulateur quantique appelé `default.qubit`, qui imite le comportement d'un ordinateur quantique sur un ordinateur classique.

Cela est possible grâce à l'utilisation de modèles mathématiques pour simuler les opérations quantiques.

Cependant, avec quelques modifications de code, vous pouvez exécuter ce code sur les plateformes IBM, Amazon ou Microsoft pour qu'il s'exécute réellement sur un ordinateur quantique.

```jsx
import pennylane as qml
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Charger et prétraiter le jeu de données Iris
data = load_iris()
X = data.data
y = data.target

# Standardiser les caractéristiques
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encoder les labels en one-hot
encoder = OneHotEncoder(sparse=False)
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

# Diviser le jeu de données
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_onehot, test_size=0.2, random_state=42)

# Définir un dispositif quantique
n_qubits = 4
dev = qml.device('default.qubit', wires=n_qubits)

# Définir un nœud quantique
@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    for i in range(len(inputs)):
        qml.RY(inputs[i], wires=i)
    
    for i in range(n_qubits):
        qml.RX(weights[i], wires=i)
        qml.RY(weights[n_qubits + i], wires=i)
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Définir un modèle hybride quantique-classique
def hybrid_model(inputs, weights):
    return quantum_circuit(inputs, weights)

# Initialiser les poids
np.random.seed(0)
weights = np.random.normal(0, np.pi, (2 * n_qubits,))

# Définir une fonction de coût
def cost(weights):
    predictions = np.array([hybrid_model(x, weights) for x in X_train])
    loss = np.mean((predictions - y_train) ** 2)
    return loss

# Optimiser les poids en utilisant la descente de gradient
opt = qml.GradientDescentOptimizer(stepsize=0.1)
steps = 100
for i in range(steps):
    weights = opt.step(cost, weights)
    if i % 10 == 0:
        print(f"Étape {i}, Coût : {cost(weights)}")

# Tester le modèle
predictions = np.array([hybrid_model(x, weights) for x in X_test])
predicted_labels = np.argmax(predictions, axis=1)
true_labels = np.argmax(y_test, axis=1)

# Calculer la précision
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Précision du test : {accuracy * 100:.2f}%")


```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/1-1.png)

Décortiquons le code bloc par bloc !

### Importer les bibliothèques

```
import pennylane as qml
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/2-1.png)
_Importer les bibliothèques_

Dans cette partie du code, nous avons importé les bibliothèques nécessaires :

* `pennylane` et `pennylane.numpy` : Pour créer et manipuler des circuits quantiques.
* `sklearn.datasets` : Pour charger le jeu de données Iris.
* `sklearn.preprocessing` : Pour le prétraitement des données comme la mise à l'échelle et l'encodage.
* `sklearn.model_selection` : Pour diviser les données en ensembles d'entraînement et de test.
* `sklearn.metrics` : Pour évaluer la précision du modèle.

### Charger et prétraiter le jeu de données Iris

```
# Charger et prétraiter le jeu de données Iris
data = load_iris()
X = data.data
y = data.target

# Standardiser les caractéristiques
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encoder les labels en one-hot
encoder = OneHotEncoder(sparse=False)
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

# Diviser le jeu de données
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_onehot, test_size=0.2, random_state=42)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/3-1.png)
_Charger et prétraiter le jeu de données Iris_

Ici, nous avons préparé les données pour l'entraînement du réseau de neurones :

* Charge le jeu de données Iris et extrait les caractéristiques (`X`) et les labels (`y`).
* Standardise les caractéristiques pour avoir une moyenne nulle et une variance unitaire en utilisant `StandardScaler`.
* Encode les labels en one-hot pour la classification multi-classe en utilisant `OneHotEncoder`.
* Divise le jeu de données en ensembles d'entraînement et de test avec un ratio de 80/20.

### Définir le dispositif quantique et le circuit

```
# Définir un dispositif quantique
n_qubits = 4
dev = qml.device('default.qubit', wires=n_qubits)

# Définir un nœud quantique
@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    for i in range(len(inputs)):
        qml.RY(inputs[i], wires=i)
    
    for i in range(n_qubits):
        qml.RX(weights[i], wires=i)
        qml.RY(weights[n_qubits + i], wires=i)
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/4-1.png)
_Définir le dispositif quantique et le circuit_

Ce segment définit le dispositif quantique et le circuit :

* Configure un dispositif quantique avec 4 qubits en utilisant le simulateur par défaut de PennyLane.
* Définit un circuit quantique (`quantum_circuit`) qui prend des entrées et des poids. Le circuit applique des portes de rotation (`RY`, `RX`) pour encoder les entrées et les paramètres, et mesure les valeurs d'attente des opérateurs `PauliZ` sur chaque qubit.

### Définir le modèle hybride et initialiser les poids

```
# Définir un modèle hybride quantique-classique
def hybrid_model(inputs, weights):
    return quantum_circuit(inputs, weights)

# Initialiser les poids
np.random.seed(0)
weights = np.random.normal(0, np.pi, (2 * n_qubits,))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/5-1.png)
_Définir le modèle hybride et initialiser les poids_

Ici, nous avons effectivement créé le modèle et démarré ses poids.

* Définit une fonction de modèle hybride qui utilise le circuit quantique.
* Initialise les poids pour le modèle en utilisant une distribution normale avec une graine spécifiée pour la reproductibilité.

### Définir la fonction de coût et optimiser les poids

```
# Définir une fonction de coût
def cost(weights):
    predictions = np.array([hybrid_model(x, weights) for x in X_train])
    loss = np.mean((predictions - y_train) ** 2)
    return loss

# Optimiser les poids en utilisant la descente de gradient
opt = qml.GradientDescentOptimizer(stepsize=0.1)
steps = 100
for i in range(steps):
    weights = opt.step(cost, weights)
    if i % 10 == 0:
        print(f"Étape {i}, Coût : {cost(weights)}")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/6-1.png)
_Définir la fonction de coût et optimiser les poids_

Enfin, nous avons commencé à entraîner le réseau de neurones basé sur le quantique.

* Définit une fonction de coût qui calcule l'erreur quadratique moyenne entre les prédictions et les vrais labels.
* Utilise `GradientDescentOptimizer` de PennyLane pour minimiser la fonction de coût en mettant à jour les poids de manière itérative. Il imprime le coût toutes les 10 étapes pour suivre la progression.

Il imprime :

```
Étape 0, Coût : 0.35359229278282217
Étape 10, Coût : 0.3145818194833503
Étape 20, Coût : 0.28937668289628116
Étape 30, Coût : 0.2733108557682183
Étape 40, Coût : 0.26273285477208475
Étape 50, Coût : 0.25532913470009133
Étape 60, Coût : 0.24973939376050813
Étape 70, Coût : 0.24517135825709957
Étape 80, Coût : 0.2411459409849017
Étape 90, Coût : 0.23735091263019087
```

### Tester le modèle et évaluer la précision

```
# Tester le modèle
predictions = np.array([hybrid_model(x, weights) for x in X_test])
predicted_labels = np.argmax(predictions, axis=1)
true_labels = np.argmax(y_test, axis=1)

# Calculer la précision
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Précision du test : {accuracy * 100:.2f}%")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/7-1.png)
_Tester le modèle et évaluer la précision_

Ensuite, nous évaluons le modèle entraîné :

* Fait des prédictions sur l'ensemble de test en utilisant les poids optimisés.
* Convertit les prédictions et les vrais labels encodés en one-hot en labels de classe.
* Calcule et imprime la précision du modèle en utilisant `accuracy_score`.

Et les résultats finaux ont donné :

```
Précision du test : 66.67%
```

Une précision de 67 % n'est pas un bon résultat pour un modèle d'IA. Cela est dû au fait que nous n'avons pas optimisé ce réseau de neurones pour ces données.

Nous devrions changer la structure du réseau de neurones pour obtenir de meilleurs résultats.

Cependant, pour ce jeu de données, avec des réseaux de neurones normaux et une bibliothèque comme [optuna](https://optuna.org/) pour l'optimisation des hyperparamètres, une précision bien plus grande dépassant 98 % est possible et peut être facilement atteinte.

Néanmoins, nous avons créé un modèle d'IA quantique simple.

<h2 id = "Conclusion">Conclusion : L'avenir des modèles d'IA efficaces</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/pexels-pixabay-210158.jpg)
_Photo par Pixabay : https://www.pexels.com/photo/low-angle-photography-of-grey-and-black-tunnel-overlooking-white-cloudy-and-blue-sky-210158/_

L'intégration de l'informatique quantique dans l'IA permet la création de modèles d'IA plus petits et plus efficaces. Avec les avancées futures dans la technologie quantique, elle sera de plus en plus appliquée dans l'IA.

À mon avis, l'avenir de l'IA sera finalement intégré avec les ordinateurs quantiques.

Voici le code complet :

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]