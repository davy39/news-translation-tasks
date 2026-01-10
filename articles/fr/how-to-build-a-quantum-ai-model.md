---
title: Comment construire un modèle d'intelligence artificielle quantique - Avec des
  exemples de code Python
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-23T18:28:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-quantum-ai-model
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/article_cover.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Python
  slug: python
seo_title: Comment construire un modèle d'intelligence artificielle quantique - Avec
  des exemples de code Python
seo_desc: 'Machine learning (ML) is one of the most important subareas of AI used
  in building great AI systems.

  In ML, deep learning is a narrow area focused solely on neural networks. Through
  the field of deep learning, systems like ChatGPT and many other AI m...'
---

L'apprentissage automatique (ML) est l'un des sous-domaines les plus importants de l'IA utilisé dans la construction de grands systèmes d'IA.

Dans le ML, l'apprentissage profond est un domaine étroit axé uniquement sur les réseaux de neurones. Grâce au domaine de l'apprentissage profond, des systèmes comme ChatGPT et de nombreux autres modèles d'IA peuvent être créés. En d'autres termes, ChatGPT est simplement un système géant basé sur des réseaux de neurones. 

Cependant, il y a un gros problème avec l'apprentissage profond : l'efficacité computationnelle. Créer de grands et efficaces systèmes d'IA avec des réseaux de neurones nécessite souvent beaucoup d'énergie, ce qui est coûteux.

Ainsi, plus le matériel est efficace, mieux c'est. Il existe de nombreuses solutions à ce problème, dont l'une est l'informatique quantique.

Cet article espère montrer, en anglais simple, la connexion entre l'informatique quantique et l'intelligence artificielle.

Nous parlerons de ces sujets :

* [Intelligence artificielle et l'essor de l'apprentissage profond](#heading-intelligence-artificielle-et-lessor-de-lapprentissage-profond)
* [Un grand problème dans l'apprentissage profond : l'efficacité computationnelle](#heading-un-grand-probleme-dans-lapprentissage-profond-lefficacite-computationnelle)
* [Une solution : l'informatique quantique](#heading-une-solution-linformatique-quantique)
* [Exemple de code : Un modèle d'IA quantique pour la chimie quantique](#heading-exemple-de-code-un-modele-dia-quantique-pour-la-chimie-quantique)
* [Conclusion : Limites de l'informatique quantique et développement](#heading-conclusion-limites-de-linformatique-quantique-et-developpement)

<h2 id="Artificial">Intelligence artificielle et l'essor de l'apprentissage profond</h2>

### Qu'est-ce que l'apprentissage profond en intelligence artificielle ?

L'apprentissage profond est un sous-domaine de l'intelligence artificielle. Il utilise des réseaux de neurones pour traiter des motifs complexes, tout comme les stratégies qu'une équipe sportive utilise pour gagner un match.

Plus le réseau de neurones est grand, plus il est capable de faire des choses incroyables - comme ChatGPT, par exemple, qui utilise le traitement du langage naturel pour répondre aux questions et interagir avec les utilisateurs.

Pour vraiment comprendre les bases des réseaux de neurones - ce que chaque modèle d'IA a en commun qui lui permet de fonctionner - nous devons comprendre les couches d'activation.

### Apprentissage profond = Entraînement des réseaux de neurones

![4-2](https://www.freecodecamp.org/news/content/images/2024/01/4-2.png)
_Réseau de neurones simple_

Au cœur de l'apprentissage profond se trouve l'entraînement des réseaux de neurones. Cela signifie utiliser des données pour obtenir les bonnes valeurs pour chaque neurone afin de pouvoir prédire ce que nous voulons.

Les réseaux de neurones sont constitués de neurones organisés en couches. Chaque couche extrait des caractéristiques uniques des données.

Cette structure en couches permet aux modèles d'apprentissage profond d'analyser et d'interpréter des données complexes.

<h2 id="problem">Un grand problème dans l'apprentissage profond : l'efficacité computationnelle</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/data-brett-sayles-4597280.jpg)
_Photo par Brett Sayles : https://www.pexels.com/photo/black-hardwares-on-data-server-room-4597280/_

L'apprentissage profond alimente une grande partie de la transformation que l'IA apporte à la société. Cependant, il vient avec un grand problème : l'efficacité computationnelle.

L'entraînement des systèmes d'IA d'apprentissage profond nécessite des quantités massives de données et de puissance computationnelle. Cela peut prendre de quelques minutes à plusieurs semaines et, dans le processus, cela consomme beaucoup d'énergie et de ressources computationnelles.

Il existe de nombreuses solutions à ce problème, comme une meilleure efficacité algorithmique. 

Dans les grands modèles de langage, cela a été le centre de beaucoup de recherches en IA. Pour faire en sorte que des modèles plus petits aient la même performance que des modèles plus grands.

Une autre solution, outre l'efficacité algorithmique, est une meilleure efficacité computationnelle. L'informatique quantique est l'une des solutions liées à une meilleure efficacité computationnelle.

<h2 id="Solution">Une solution : l'informatique quantique</h2>

L'informatique quantique est une solution prometteuse au problème d'efficacité computationnelle dans l'apprentissage profond.

Alors que les ordinateurs normaux fonctionnent en bits (soit 0 ou 1), les ordinateurs quantiques fonctionnent avec des qubits - qui peuvent être 0 et 1 en même temps.

Avec les qubits représentant 0 et 1 en même temps, il est possible de traiter de nombreuses possibilités simultanément, grâce à une propriété appelée superposition en physique quantique.

Cela rend les ordinateurs quantiques, pour certaines tâches, bien plus efficaces que les ordinateurs normaux.

De cette manière, il est également possible d'avoir des algorithmes basés sur le quantique qui sont plus efficaces que les algorithmes normaux. De cette manière, en réduisant la consommation d'énergie utilisée lors de la création de modèles d'IA.

### Pourquoi les ordinateurs quantiques ne sont-ils pas si largement utilisés ?

Le problème avec le calcul quantique est qu'il n'existe pas de bonne représentation physique bon marché des qubits.

Les bits sont créés et gérés avec des portes logiques faites de minuscules transistors, qui peuvent être facilement créés par milliards.

Les qubits sont créés et gérés par des circuits supraconducteurs, des ions piégés et des qubits topologiques, qui sont tous très coûteux.

C'est le plus grand problème du calcul quantique. Cependant, IBM, Amazon et beaucoup d'autres dans les services cloud permettent aux gens d'exécuter du code sur leurs ordinateurs quantiques.

<h2 id="Code">Exemple de code : Un modèle d'IA quantique pour la chimie quantique</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/chemnistry-pixabay-248152.jpg)
_Photo par Pixabay : https://www.pexels.com/photo/two-clear-glass-jars-beside-several-flasks-248152/_

Dans cet exemple de code, nous allons résoudre un problème de chimie quantique :

_Quel est le niveau d'énergie le plus bas de la molécule H₂ en utilisant l'informatique quantique ?_

Avant de comprendre le problème en question, discutons de la chimie quantique.

### Qu'est-ce que la chimie quantique ?

La chimie quantique est un domaine de la science qui étudie le comportement des électrons dans les atomes et les molécules.

Il s'agit d'utiliser la physique quantique pour comprendre comment les électrons, les atomes, les molécules et bien d'autres particules minuscules interagissent et forment différentes substances chimiques.

#### Le problème que nous voulons résoudre

Nous voulons trouver l'"énergie de l'état fondamental" de la molécule H₂. 

La molécule H₂ signifie le gaz hydrogène, qui est présent dans :

* L'eau
* Les composés organiques
* Les étoiles

En fait, la vie sur Terre ne serait pas possible sans lui. 

En trouvant l'"énergie de l'état fondamental", qui est l'énergie la plus basse possible que la molécule peut avoir, nous pouvons connaître sa forme et ses propriétés les plus stables. 

Cela permet aux scientifiques de mieux comprendre les réactions chimiques liées à H₂. 

Avec les ordinateurs classiques, ce problème peut être très complexe en raison d'un nombre énorme de possibilités et d'interactions complexes. 

Avec les ordinateurs quantiques, les qubits sont de bonnes représentations des électrons, qui peuvent directement simuler le comportement des électrons dans les molécules.

### Approximation avec le VQE (Variational Quantum Eigensolver)

Le Variational Quantum Eigensolver (VQE) est un algorithme hybride qui utilise à la fois le calcul quantique et classique. 

Dans cet exemple, l'algorithme VQE est utilisé pour trouver l'énergie de l'état fondamental d'une simple molécule H₂. 

Le code est conçu pour fonctionner sur un simulateur quantique (qui est un ordinateur classique exécutant un algorithme quantique).

Cependant, il peut être adapté pour fonctionner sur du matériel quantique réel via un service de calcul quantique basé sur le cloud. 

Cela impliquerait l'utilisation de ressources quantiques et classiques en pratique. Passons en revue le code étape par étape !

```
import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

# Définir la molécule (H2 à une longueur de liaison de 0,74 Å)
symbols = ["H", "H"]
coordinates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.74])

# Générer le Hamiltonien pour la molécule
hamiltonian, qubits = qml.qchem.molecular_hamiltonian(
    symbols, coordinates
)

# Définir le dispositif quantique
dev = qml.device("default.qubit", wires=qubits)

# Définir l'ansatz (circuit quantique variationnel)
def ansatz(params, wires):
    qml.BasisState(np.array([0] * qubits), wires=wires)
    for i in range(qubits):
        qml.RY(params[i], wires=wires[i])
    for i in range(qubits - 1):
        qml.CNOT(wires=[wires[i], wires[i + 1]])

# Définir la fonction de coût
@qml.qnode(dev)
def cost_fn(params):
    ansatz(params, wires=range(qubits))
    return qml.expval(hamiltonian)

# Définir une graine fixe pour la reproductibilité
np.random.seed(42)

# Définir les paramètres initiaux
params = np.random.random(qubits, requires_grad=True)

# Choisir un optimiseur
optimizer = qml.GradientDescentOptimizer(stepsize=0.4)

# Nombre d'étapes d'optimisation
max_iterations = 100
conv_tol = 1e-06

# Boucle d'optimisation
energies = []

for n in range(max_iterations):
    params, prev_energy = optimizer.step_and_cost(cost_fn, params)

    energy = cost_fn(params)
    energies.append(energy)
    if np.abs(energy - prev_energy) < conv_tol:
        break

    print(f"Étape = {n}, Énergie = {energy:.8f} Ha")

print(f"Énergie finale de l'état fondamental = {energy:.8f} Ha")

# Visualiser les résultats
import matplotlib.pyplot as plt

iterations = range(len(energies))

plt.plot(iterations, energies)
plt.xlabel('Itération')
plt.ylabel('Énergie (Ha)')
plt.title('Convergence du VQE pour la molécule H2')
plt.show()

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-5.png)
_Image du code complet_

### Importation des bibliothèques

```
import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2-4.png)
_Importation des bibliothèques_

* [pennylane](https://pennylane.ai/) : Une bibliothèque pour l'informatique quantique qui fournit des outils pour créer et optimiser des circuits quantiques, et pour exécuter des algorithmes quantiques basés sur l'apprentissage automatique.
* [numpy](https://numpy.org/) : Une bibliothèque pour les opérations numériques en Python, utilisée ici pour manipuler des tableaux et des calculs mathématiques.
* [matplotlib](https://matplotlib.org/) : Une bibliothèque pour créer des visualisations et des graphiques en Python, utilisée ici pour tracer la convergence de l'algorithme VQE.

### Définition de la molécule et génération du Hamiltonien

```
# Définir la molécule (H2 à une longueur de liaison de 0,74 Å)
symbols = ["H", "H"]
coordinates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.74])

# Générer le Hamiltonien pour la molécule
hamiltonian, qubits = qml.qchem.molecular_hamiltonian(
    symbols, coordinates
)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-4.png)
_Définition de la molécule et génération du Hamiltonien_

**Définition de la molécule** :

* Nous avons défini une molécule d'hydrogène (H₂).
* `symbols = ["H", "H"]` : Cela signifie que la molécule est composée de deux atomes d'hydrogène (H).
* `coordinates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.74])` : Cela donne les positions des deux atomes d'hydrogène. Le premier atome d'hydrogène est à l'origine (0.0, 0.0, 0.0), et le second atome d'hydrogène est à (0.0, 0.0, 0.74), ce qui signifie qu'il est à 0,74 angströms du premier atome le long de l'axe z.

**Génération du Hamiltonien** :

* `hamiltonian, qubits = qml.qchem.molecular_hamiltonian(symbols, coordinates)` : Cette ligne génère le Hamiltonien pour la molécule d'hydrogène. Le Hamiltonien est un objet mathématique utilisé pour décrire l'énergie de la molécule.
* `hamiltonian` : Représente l'opérateur d'énergie pour la molécule.
* `qubits` : Représente le nombre de bits quantiques (qubits) nécessaires pour simuler la molécule sur un ordinateur quantique.

### Définition du dispositif quantique et de l'ansatz (circuit quantique variationnel)

```
# Définir le dispositif quantique
dev = qml.device("default.qubit", wires=qubits)

# Définir l'ansatz (circuit quantique variationnel)
def ansatz(params, wires):
    qml.BasisState(np.array([0] * qubits), wires=wires)
    for i in range(qubits):
        qml.RY(params[i], wires=wires[i])
    for i in range(qubits - 1):
        qml.CNOT(wires=[wires[i], wires[i + 1]])

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-3.png)
_Définition du dispositif quantique et de l'ansatz (circuit quantique variationnel)_

**Définition du dispositif quantique** :

* `dev = qml.device("default.qubit", wires=qubits)` : Cette ligne configure un dispositif de calcul quantique pour simuler notre molécule.
* `"default.qubit"` : Cela spécifie le type de simulateur quantique que nous utilisons (un simulateur basé sur des qubits par défaut).
* `wires=qubits` : Cela indique au simulateur combien de qubits (bits quantiques) il doit utiliser, en fonction du nombre de qubits que nous avons déterminé précédemment.

**Définition de l'ansatz (circuit quantique variationnel)** :

* `def ansatz(params, wires)` : Cela définit une fonction nommée `ansatz` qui décrit le circuit quantique variationnel. Ce circuit sera utilisé pour trouver l'énergie de l'état fondamental de la molécule.
* `qml.BasisState(np.array([0] * qubits), wires=wires)` : Cela initialise les qubits dans l'état 0. Le `np.array([0] * qubits)` crée un tableau avec des zéros, un pour chaque qubit.
* `for i in range(qubits): qml.RY(params[i], wires=wires[i])` : Cette boucle applique une rotation autour de l'axe Y à chaque qubit. `params[i]` fournit l'angle pour chaque rotation.
* `for i in range(qubits - 1): qml.CNOT(wires=[wires[i], wires[i + 1]])` : Cette boucle applique des portes CNOT (NOT contrôlé) entre des qubits consécutifs, les enchevêtrant.

### Définition de la fonction de coût, des paramètres initiaux et de l'optimiseur

```
# Définir la fonction de coût
@qml.qnode(dev)
def cost_fn(params):
    ansatz(params, wires=range(qubits))
    return qml.expval(hamiltonian)

# Définir une graine fixe pour la reproductibilité
np.random.seed(42)

# Définir les paramètres initiaux
params = np.random.random(qubits, requires_grad=True)

# Choisir un optimiseur
optimizer = qml.GradientDescentOptimizer(stepsize=0.4)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5-3.png)
_Définition de la fonction de coût, des paramètres initiaux et de l'optimiseur_

**Définition de la fonction de coût** :

* `@qml.qnode(dev)` : Cette ligne est un décorateur qui transforme la fonction `cost_fn` en un nœud quantique, lui permettant de s'exécuter sur le dispositif quantique `dev`.
* `def cost_fn(params)` : Cela définit une fonction nommée `cost_fn` qui prend certains paramètres (`params`) en entrée.
* `ansatz(params, wires=range(qubits))` : À l'intérieur de cette fonction, nous appelons la fonction `ansatz` définie précédemment, en passant les paramètres et en spécifiant qu'elle doit utiliser tous les qubits.
* `return qml.expval(hamiltonian)` : Cette ligne retourne la valeur attendue du Hamiltonien, qui représente l'énergie de la molécule. La fonction de coût est ce que nous cherchons à minimiser pour trouver l'énergie de l'état fondamental.

**Définition d'une graine fixe pour la reproductibilité** :

* `np.random.seed(42)` : Cette ligne définit une graine fixe pour le générateur de nombres aléatoires. Cela garantit que les nombres aléatoires générés seront les mêmes à chaque fois que le code est exécuté, rendant les résultats reproductibles.

**Définition des paramètres initiaux** :

* `params = np.random.random(qubits, requires_grad=True)` : Cette ligne initialise les paramètres pour l'ansatz avec des valeurs aléatoires. Le nombre de paramètres est égal au nombre de qubits. La partie `requires_grad=True` indique que ces paramètres peuvent être ajustés pendant l'optimisation.

**Choix d'un optimiseur** :

* `optimizer = qml.GradientDescentOptimizer(stepsize=0.4)` : Cette ligne crée un optimiseur qui ajustera les paramètres pour minimiser la fonction de coût. Plus précisément, il utilise la descente de gradient avec une taille de pas de 0,4.

### Boucle d'optimisation

```
# Nombre d'étapes d'optimisation
max_iterations = 100
conv_tol = 1e-06

# Boucle d'optimisation
energies = []

for n in range(max_iterations):
    params, prev_energy = optimizer.step_and_cost(cost_fn, params)

    energy = cost_fn(params)
    energies.append(energy)
    if np.abs(energy - prev_energy) < conv_tol:
        break

    print(f"Étape = {n}, Énergie = {energy:.8f} Ha")

print(f"Énergie finale de l'état fondamental = {energy:.8f} Ha")

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/6-2.png)
_Boucle d'optimisation_

**Définition du nombre d'étapes d'optimisation** :

* `max_iterations = 100` : Cela définit le nombre maximum d'étapes que l'optimisation prendra. Dans ce cas, il s'agit de 100 étapes.
* `conv_tol = 1e-06` : Cela définit la tolérance de convergence. Si le changement d'énergie entre les étapes est inférieur à cette valeur, l'optimisation s'arrêtera.

**Boucle d'optimisation** :

* `energies = []` : Cela initialise une liste vide pour stocker les énergies calculées à chaque étape.

**Boucle à travers les étapes d'optimisation** :

* `for n in range(max_iterations):` : Cela commence une boucle qui s'exécutera jusqu'à `max_iterations` fois.
* `params, prev_energy = optimizer.step_and_cost(cost_fn, params)` : Cette ligne effectue une étape d'optimisation. Elle met à jour les paramètres et retourne les nouveaux paramètres et l'énergie précédente.
* `energy = cost_fn(params)` : Cela calcule l'énergie actuelle en utilisant les paramètres mis à jour.
* `energies.append(energy)` : Cela ajoute l'énergie actuelle à la liste `energies`.
* `if np.abs(energy - prev_energy) < conv_tol: break` : Cela vérifie si la différence absolue entre l'énergie actuelle et l'énergie précédente est inférieure à la tolérance de convergence. Si c'est le cas, la boucle s'arrête tôt car l'optimisation a convergé.
* `print(f"Étape = {n}, Énergie = {energy:.8f} Ha")` : Cela imprime le numéro de l'étape actuelle et l'énergie en Hartree (Ha) à huit décimales.

**Impression de l'énergie finale** :

* `print(f"Énergie finale de l'état fondamental = {energy:.8f} Ha")` : Après la boucle, cela imprime l'énergie finale de l'état fondamental.

### Visualisation des résultats

```
# Visualiser les résultats
iterations = range(len(energies))

plt.plot(iterations, energies)
plt.xlabel('Itération')
plt.ylabel('Énergie (Ha)')
plt.title('Convergence du VQE pour la molécule H2')
plt.show()

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/7.png)
_Visualisation des résultats_

**Préparation des données pour la visualisation** :

* `iterations = range(len(energies))` : Cela crée un objet range représentant le nombre d'itérations (étapes) que l'optimisation a traversées. `len(energies)` donne le nombre de valeurs d'énergie enregistrées.

**Tracé des résultats** :

* `plt.plot(iterations, energies)` : Cette ligne crée un graphique avec les numéros d'itération sur l'axe des x et les valeurs d'énergie correspondantes sur l'axe des y.
* `plt.xlabel('Itération')` : Cela définit l'étiquette de l'axe des x sur "Itération".
* `plt.ylabel('Énergie (Ha)')` : Cela définit l'étiquette de l'axe des y sur "Énergie (Ha)", où "Ha" signifie Hartree, une unité d'énergie.
* `plt.title('Convergence du VQE pour la molécule H2')` : Cela définit le titre du graphique sur "Convergence du VQE pour la molécule H2".
* `plt.show()` : Cela affiche le graphique.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/H2H.png)

Le graphique intitulé "Convergence du VQE pour la molécule H2" montre l'énergie (en Hartree, Ha) de la molécule H2 tracée en fonction du nombre d'itérations de l'algorithme Variational Quantum Eigensolver (VQE).

* **Axe X (Itération) :** Nombre d'itérations VQE.
* **Axe Y (Énergie (Ha)) :** Énergie de la molécule H2 en Hartree.

### Points clés :

* **Énergie initiale :** Environ 1,4 Ha à l'itération 0.
* **Diminution rapide :** L'énergie chute rapidement dans les 20 premières itérations.
* **Plateau :** L'énergie se stabilise autour de 0,4 Ha après 20 itérations, indiquant une convergence vers une solution optimale ou quasi-optimale.

<h2 id="Conclusion">Conclusion : Limites de l'informatique quantique et développement</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/PC-richasharma96-4247412.jpg)
_Photo par Richa Sharma : https://www.pexels.com/photo/ceramic-mug-on-black-laptop-on-table-in-office-4247412/_

Outre le fait de rendre les algorithmes d'IA beaucoup plus efficaces sur le plan computationnel, l'informatique quantique peut révolutionner de nombreux domaines comme :

* La découverte de médicaments
* La science des matériaux
* La cryptographie
* La modélisation financière
* Les problèmes d'optimisation
* La modélisation climatique
* L'apprentissage automatique

Cependant, pour que nous puissions tous utiliser l'informatique quantique, il faut une manière de représenter physiquement les qubits suffisamment petits pour tenir sur nos ordinateurs portables. Cela prendra des années.

Le code complet peut être trouvé ici :

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]