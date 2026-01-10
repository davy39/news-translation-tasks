---
title: Comment évaluer les modèles de Machine Learning à l'aide de TensorBoard avec
  TensorFlow
subtitle: ''
author: Salim Oyinlola
co_authors: []
series: null
date: '2022-09-14T18:31:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-evaluate-machine-learning-models-using-tensorboard
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/TensorFlow_Logo_with_text.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: TensorFlow
  slug: tensorflow
seo_title: Comment évaluer les modèles de Machine Learning à l'aide de TensorBoard
  avec TensorFlow
seo_desc: "A key part of the Machine Learning pipeline is finding a model that best\
  \ represents your data and will function effectively on future datasets. \nBy virtue\
  \ of their very nature, Machine Learning models improve iteratively. There is hardly\
  \ any machine ..."
---

Une partie clé du pipeline de Machine Learning consiste à trouver un modèle qui représente au mieux vos données et qui fonctionnera efficacement sur de futurs ensembles de données. 

De par leur nature même, les modèles de Machine Learning s'améliorent de manière itérative. Il est rarement possible d'entraîner un modèle de machine learning parfaitement dès la première tentative. Habituellement, plusieurs itérations sont nécessaires. 

Comme vous pouvez l'imaginer, ces modèles doivent être évalués pour être améliorés. En d'autres termes, un modèle de machine learning doit être évalué avant de pouvoir être amélioré. 

[TensorBoard](https://www.tensorflow.org/tensorboard/get_started) a été développé pour donner aux ingénieurs en machine learning un aperçu plus approfondi des performances de leurs modèles. 

## **Qu'est-ce que TensorBoard ?**

La fonctionnalité de base de TensorBoard est de fournir les métriques et visualisations nécessaires pour votre workflow de Machine Learning. Il vous permet de surveiller la perte et la précision, de visualiser et d'évaluer les graphiques d'erreurs, et d'effectuer de nombreuses autres tâches. 

TensorBoard utilise des concepts de graphiques pour représenter le flux de données et les actions du modèle tout en vous permettant de voir les topologies de graphiques et les paramètres de modèles complexes et volumineux. Il dispose également d'une interface utilisateur très conviviale et basique.

Dans ce tutoriel, vous allez analyser et évaluer les résultats d'un modèle de machine learning entraîné. Le modèle que vous allez utiliser sera entraîné sur un ensemble de données [MNIST handwritten digits dataset](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist). Il utilise la base de données MNIST (Modified National Institute of Standards and Technology), qui contient une ample collection de chiffres manuscrits. Cet ensemble de données est couramment utilisé pour entraîner divers systèmes de traitement d'images.

### **Prérequis**

Pour suivre ce tutoriel, vous aurez besoin de :

1. Une compréhension fondamentale du fonctionnement des modèles de Machine Learning.
2. Un nouveau notebook Google Colab pour exécuter le code Python dans votre Google Drive. Vous pouvez le configurer en suivant ce [tutoriel](https://www.freecodecamp.org/news/google-colaboratory-python-code-in-your-google-drive/).

## **Étape 1 – Comment configurer TensorBoard**

Puisque TensorBoard est automatiquement inclus avec TensorFlow, vous n'avez pas besoin de l'installer avec `pip` dans cette configuration. De plus, comme TensorFlow est préinstallé lorsque vous créez un nouveau notebook sur Google Colab, TensorBoard est également préinstallé. Ainsi, lors de la configuration de TensorBoard, vous devez uniquement importer `tensorflow`.  

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-157.png)
_Un notebook (nouveau) vide en mode sombre_

* Chargez l'extension `tensorboard` en utilisant le magic `%load_ext` dans votre notebook. 
* Après cela, importez les bibliothèques nécessaires (c'est-à-dire `tensorflow` et `datetime`) comme montré ci-dessous :

```python
%load_ext tensorboard
```

```python
import tensorflow as tf
import datetime
```

À ce stade, vous avez importé avec succès une instance de `TensorBoard` et l'avez configurée. Vous pouvez maintenant commencer.

## **Étape 2 – Comment créer et entraîner le modèle**

Dans ce tutoriel, vous allez utiliser l'ensemble de données MNIST, qui inclut de petites images en niveaux de gris de chiffres manuscrits de 28 x 28 pixels. L'ensemble de données, qui est l'un des ensembles de données préinstallés offerts par `Keras`, est fréquemment utilisé pour développer des modèles de Machine Learning pour la reconnaissance de chiffres. 

* Créez une instance de l'ensemble de données et nommez-la `mnist`.
* Divisez les données en ensembles d'entraînement et ensembles de test. Un ensemble d'entraînement est un sous-ensemble des données originales utilisé pour entraîner le modèle de machine learning, tandis qu'un ensemble de test est le sous-ensemble utilisé pour vérifier la précision du modèle. 
* Standardisez toutes les valeurs de vos ensembles d'entraînement et de test. Cela implique de normaliser l'image dans la plage [0,1].
* Définissez une fonction qui sera utilisée pour entraîner le modèle de machine learning sur votre ensemble de données. Le modèle `Sequential` de Keras sera utilisé. 

```python
mnist = tf.keras.datasets.mnist

```

```python
(x_train, y_train),(x_test, y_test) = mnist.load_data()
```

```python
x_train, x_test = x_train/255.0, x_test/255.0
```

```python
def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])
```

Vous allez utiliser le modèle `Sequential` de Keras. À sa base, il regroupe une pile linéaire de couches dans `tf.keras.Model` tout en fournissant des fonctionnalités d'entraînement et d'inférence sur ce modèle.

La couche `.Flatten()` aplatit l'entrée sans affecter la taille du lot. La forme d'entrée dans cet exemple est de 28 x 28 puisque les images de l'ensemble de données sont des images en niveaux de gris de 28×28 pixels de chiffres manuscrits. La première couche `.Dense()` est une couche NN densément connectée régulière. 

La fonction d'activation utilisée est 'relu' et la dimensionnalité de son espace de sortie est de 512. La couche `.Dropout()` abandonne une partie de l'entrée avec la fraction des unités d'entrée abandonnées dans ce tutoriel donnée comme 0,2. 

Enfin, comme la première, la deuxième couche `Dense` est également votre couche NN densément connectée régulière. La fonction d'activation que nous utilisons est 'softmax' et la dimensionnalité de son espace de sortie est de dix.

* Appelez la fonction définie pour le modèle comme ceci : 
* Avec la fonction définie appelée, entraînez le modèle avec des paramètres appropriés.
* En utilisant la bibliothèque `datetime` que vous avez précédemment importée, placez les logs dans un sous-répertoire horodaté pour permettre une sélection facile des différentes exécutions d'entraînement.

```python
model = create_model()

```

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

Les logs sont importants car TensorBoard les lira pour afficher les différentes visualisations en fonction du temps à ce moment-là. 

```python
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
```

* Enfin, entraînez (ou ajustez) le modèle de machine learning sur trois époques (itérations).

```python
model.fit(x=x_train, 
          y=y_train, 
          epochs=3, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-158.png)

## **Étape 3 – Comment évaluer le modèle**

Pour démarrer TensorBoard dans votre notebook, exécutez le code ci-dessous :

```python
%tensorboard --logdir logs/fit
```

Vous pouvez maintenant visualiser les tableaux de bord affichant les métriques du modèle dans les onglets en haut et évaluer et améliorer vos modèles de machine learning en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-159.png)

## **Étape 4 – Comment améliorer le modèle**

Puisque le but de l'évaluation de vos modèles de Machine Learning est de mieux comprendre pour améliorer l'algorithme, il est impératif que nous améliorions notre modèle. Avec ces visuels, vous pouvez maintenant voir les performances approfondies du modèle.

* Le tableau de bord `Scalars` peut être utilisé pour observer d'autres valeurs scalaires telles que l'efficacité de l'entraînement et le taux d'apprentissage. Il démontre comment les métriques et la perte fluctuent à chaque époque. 
* Comme son nom l'indique, le tableau de bord `Graphs` est utilisé pour visualiser votre modèle. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-160.png)
_Le graphique avec TensorBoard_

Pour améliorer ce modèle, vous allez ajuster le nombre d'époques de 3 à 6 et voir comment le modèle se comporte.

En général, le nombre d'époques est le nombre d'itérations sur l'ensemble de données d'entraînement complet sur lequel le modèle de machine learning est entraîné.

Intuitivement, augmenter ce nombre améliore presque toujours les performances de votre modèle de machine learning. Pour ce faire, vous allez exécuter le code comme suit :

```python
model.fit(x=x_train, 
          y=y_train, 
          epochs=6, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-161.png)

Avec le changement que nous avons apporté, vous pouvez ensuite générer un autre TensorBoard comme ceci :

```
%tensorboard --logdir logs/fit
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-162.png)

À partir des nouveaux visuels générés, vous pouvez voir qu'il y a une amélioration remarquable des performances du modèle.

## **Conclusion**

Dans cet article, vous avez appris comment utiliser TensorBoard pour évaluer et améliorer les performances de votre modèle de Machine Learning.

Si à ce stade vous avez des questions sur la différence entre TensorBoard et TensorFlow Metrics Analysis (TFMA), c'est une préoccupation valide. Après tout, les deux sont des outils pour fournir les mesures et visualisations nécessaires pendant le workflow de Machine Learning.

Mais il est important de noter que vous utilisez chacun de ces outils à des étapes distinctes du processus de développement. À sa base, TensorBoard est utilisé pour analyser le processus d'entraînement lui-même, tandis que TFMA est concerné par l'analyse du modèle entraîné 'fini'.

Enfin, je partage mes écrits sur [Twitter](https://twitter.com/SalimOyinlola) si vous avez aimé cet article et souhaitez en voir plus.

Merci d'avoir lu :)