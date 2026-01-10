---
title: Comment construire de meilleurs modèles de Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-23T16:22:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-better-machine-learning-models
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/pexels-pixabay-373543.jpg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
seo_title: Comment construire de meilleurs modèles de Machine Learning
seo_desc: "By Rishit Dagli\nHello developers \U0001F44B. If you have built Deep Neural\
  \ Networks before, you might know that it can involve a lot of experimentation.\
  \ \nIn this article, I will share with you some useful tips and guidelines that\
  \ you can use to better build ..."
---

Par Rishit Dagli

Bonjour les développeurs 👋. Si vous avez déjà construit des réseaux de neurones profonds (Deep Neural Networks), vous savez peut-être que cela peut impliquer beaucoup d'expérimentation.

Dans cet article, je vais partager avec vous quelques conseils et directives utiles que vous pouvez utiliser pour mieux construire de meilleurs modèles de deep learning. Ces astuces devraient vous faciliter grandement le développement d'un bon réseau.

Vous pouvez choisir les conseils que vous utilisez, car certains seront plus utiles pour les projets sur lesquels vous travaillez. Tout ce qui est mentionné dans cet article n'améliorera pas forcément directement les performances de vos modèles.

## Une approche de haut niveau pour le réglage des hyperparamètres🕹️

L'un des aspects les plus pénibles de l'entraînement des réseaux de neurones profonds est le grand nombre d'hyperparamètres auxquels vous devez faire face.

Il peut s'agir de votre taux d'apprentissage (learning rate) **α**, du facteur d'actualisation **ρ** et d'epsilon **ε** si vous utilisez l'optimiseur RMSprop ([Hinton et al.](https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)) ou des taux de décroissance exponentielle **β₁** et **β₂** si vous utilisez l'optimiseur Adam ([Kingma et al.](https://arxiv.org/abs/1412.6980)).

Vous devez également choisir le nombre de couches dans le réseau ou le nombre d'unités cachées pour les couches. Vous utilisez peut-être des planificateurs de taux d'apprentissage (learning rate schedulers) et souhaiteriez configurer ces fonctionnalités et bien d'autres encore 😫 ! Nous avons définitivement besoin de moyens pour mieux organiser notre processus de réglage des hyperparamètres.

Un algorithme courant que j'ai tendance à utiliser pour organiser ma recherche d'hyperparamètres est la Recherche Aléatoire (Random Search). Bien qu'il existe d'autres algorithmes qui pourraient être meilleurs, je finis généralement par l'utiliser quand même.

Disons, pour les besoins de cet exemple, que vous voulez régler deux hyperparamètres et que vous soupçonnez que les valeurs optimales pour les deux se situent quelque part entre un et cinq.

L'idée ici est qu'au lieu de choisir systématiquement vingt-cinq valeurs à essayer comme (1, 1), (1, 2) et ainsi de suite, il serait plus efficace de sélectionner vingt-cinq points au hasard.

![Image](https://lh3.googleusercontent.com/MLzfMgeWASsgXEsq2XUGxo8QFl99R-4TA_--azr_k7F9rkEhh31esm47zemiPDTIPrjNWQjmlpEXtstqgcopQnEgF0R2CsNDPTuwaPq-_54IgaGp0Dkjd7TCMe3oWe-gjiVnrc2Y)
_Basé sur les notes de cours d'[Andrew Ng](https://www.andrewng.org/)<span class="-mobiledoc-kit__atom">‌‌</span>_

Voici un exemple simple avec TensorFlow où j'essaie d'utiliser la Recherche Aléatoire sur le jeu de données Fashion MNIST pour le taux d'apprentissage et le nombre d'unités dans la première couche Dense :

```py
import kerastuner as kt
import tensorflow as tf

def model_builder(hp):
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
  
  # Régler le nombre d'unités dans la première couche Dense
  # Choisir une valeur optimale entre 32 et 512
  hp_units = hp.Int('units', min_value = 32, max_value = 512, step = 32)
  model.add(tf.keras.layers.Dense(units = hp_units, activation = 'relu'))
  model.add(tf.keras.layers.Dense(10))

  # Régler le taux d'apprentissage pour l'optimiseur 
  # Choisir une valeur optimale parmi 0.01, 0.001 ou 0.0001
  hp_learning_rate = hp.Choice('learning_rate', values = [1e-2, 1e-3, 1e-4]) 
  
  model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = hp_learning_rate),
                loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True), 
                metrics = ['accuracy'])
  
  return model
  
tuner = kt.RandomSearch(model_builder,
                        objective = 'val_accuracy', 
                        max_trials = 10,
                        directory = 'random_search_starter',
                        project_name = 'intro_to_kt') 
                     
tuner.search(img_train, label_train, epochs = 10, validation_data = (img_test, label_test))

# Quel était le meilleur modèle ?
best_model = tuner.get_best_models(1)[0]

# Quels étaient les meilleurs hyperparamètres ?
best_hyperparameters = tuner.get_best_hyperparameters(1)[0] 
```

Ici, je soupçonne qu'un nombre optimal d'unités dans la première couche Dense se situerait quelque part entre 32 et 512, et que mon taux d'apprentissage serait l'un des suivants : 1e-2, 1e-3 ou 1e-4.

Par conséquent, comme le montre cet exemple, je fixe ma valeur minimale pour le nombre d'unités à 32 et la valeur maximale à 512 avec un pas de 32. Ensuite, au lieu de coder en dur une valeur pour le nombre d'unités, je spécifie une plage à essayer.

```py
hp_units = hp.Int('units', min_value = 32, max_value = 512, step = 32)
model.add(tf.keras.layers.Dense(units = hp_units, activation = 'relu'))
```

Nous faisons de même pour notre taux d'apprentissage, mais notre taux d'apprentissage est simplement l'un des choix 1e-2, 1e-3 ou 1e-4 plutôt qu'une plage.

```py
hp_learning_rate = hp.Choice('learning_rate', values = [1e-2, 1e-3, 1e-4])
optimizer = tf.keras.optimizers.Adam(learning_rate = hp_learning_rate)
```

Enfin, nous effectuons la Recherche Aléatoire et spécifions que parmi tous les modèles que nous construisons, le modèle ayant la précision de validation la plus élevée sera appelé le meilleur modèle. Ou simplement que l'objectif est d'obtenir une bonne précision de validation.

```py
tuner = kt.RandomSearch(model_builder,
                        objective = 'val_accuracy', 
                        max_trials = 10,
                        directory = 'random_search_starter',
                        project_name = 'intro_to_kt') 
                     
tuner.search(img_train, label_train, epochs = 10, validation_data = (img_test, label_test))
```

Après cela, je veux également récupérer le meilleur modèle et le meilleur choix d'hyperparamètres. J'aimerais toutefois souligner que l'utilisation de `get_best_models` est généralement considérée comme un raccourci.

Pour obtenir les meilleures performances, vous devriez réentraîner votre modèle avec les meilleurs hyperparamètres obtenus sur l'ensemble du jeu de données.

```py
# Quel était le meilleur modèle ?
best_model = tuner.get_best_models(1)[0]

# Quels étaient les meilleurs hyperparamètres ?
best_hyperparameters = tuner.get_best_hyperparameters(1)[0] 
```

Je ne parlerai pas de ce code en détail dans cet article, mais vous pouvez lire [cet article](https://towardsdatascience.com/the-art-of-hyperparameter-tuning-in-deep-neural-nets-by-example-685cb5429a38) que j'ai écrit il y a quelque temps si vous le souhaitez.

## Utiliser l'entraînement en précision mixte pour les grands réseaux🎨

Plus votre réseau de neurones est grand, plus vos résultats sont précis (en général). À mesure que la taille des modèles augmente, les besoins en mémoire et en calcul pour l'entraînement de ces modèles augmentent également.

L'idée de l'utilisation de l'entraînement en précision mixte (Mixed Precision Training) (NVIDIA, [Micikevicius et al.](https://arxiv.org/abs/1710.03740)) est d'entraîner des réseaux de neurones profonds en utilisant des nombres à virgule flottante en demi-précision, ce qui vous permet d'entraîner de grands réseaux de neurones beaucoup plus rapidement avec une diminution nulle ou négligeable des performances des réseaux.

Mais, je tiens à souligner que cette technique ne devrait être utilisée que pour les grands modèles avec plus de 100 millions de paramètres environ.

Bien que la précision mixte fonctionne sur la plupart des matériels, elle n'accélérera les modèles que sur les GPU NVIDIA récents (par exemple Tesla V100 et Tesla T4) et les Cloud TPU.

Je veux vous donner une idée des gains de performance lors de l'utilisation de la précision mixte. Lorsque j'ai entraîné un modèle ResNet sur mon instance GCP Notebook (composée d'un Tesla V100), le temps d'entraînement était presque trois fois meilleur et presque 1,5 fois sur une instance Cloud TPU avec presque aucune différence de précision. Le code pour mesurer les accélérations ci-dessus a été tiré de [cet exemple](https://www.tensorflow.org/guide/mixed_precision).

Pour augmenter encore votre débit d'entraînement, vous pourriez également envisager d'utiliser une taille de lot (batch size) plus grande – et puisque nous utilisons des tenseurs float16, vous ne devriez pas manquer de mémoire.

Il est également assez facile d'implémenter la précision mixte avec TensorFlow. Avec TensorFlow, vous pouvez facilement utiliser le module [tf.keras.mixed_precision](https://www.freecodecamp.org/news/p/d63b23cb-c1f8-4997-87c1-6c5c44ea9e14/tf.keras.mixed_precision) qui vous permet de mettre en place une politique de type de données (pour utiliser float16) et d'appliquer également une mise à l'échelle de la perte (loss scaling) pour éviter le sous-dépassement (underflow).

Voici un exemple minimaliste d'utilisation de l'entraînement en précision mixte sur un réseau :

```py
import tensorflow as tf

policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

inputs = keras.Input(shape=(784,))
x = tf.keras.layers.Dense(4096, activation='relu')(inputs)
x = tf.keras.layers.Dense(4096, activation='relu')(x)
x = layers.Dense(10)(x)
outputs = layers.Activation('softmax', dtype='float32')(x)
model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(...)
model.fit(...)
```

Dans cet exemple, nous définissons d'abord la politique dtype sur float16, ce qui implique que toutes les couches de notre modèle utiliseront automatiquement float16.

Après cela, nous construisons un modèle, mais nous surchargeons le type de données pour la dernière couche ou la couche de sortie en float32 pour éviter tout problème numérique. Idéalement, vos couches de sortie devraient être en float32.

Note : J'ai construit un modèle avec autant d'unités pour que nous puissions voir une différence dans le temps d'entraînement avec l'entraînement en précision mixte, car cela fonctionne bien pour les grands modèles.

Si vous cherchez plus d'inspiration pour utiliser l'entraînement en précision mixte, voici une image démontrant l'accélération pour plusieurs modèles par Google Cloud sur un TPU :

![Image](https://lh6.googleusercontent.com/jDx-lq4Ll6Ihre2G5_JIYRDr1ogkMUCHiNcQ8g_WXz3cpGeylmICsQtQkV5JE9wcwZswzImi57AfNzWPEqBuLWfabl405AbH4HsZH6eOKs8kEF_zjZRKkQ6qQjLGk-JSca3rCGU7)
_Accélérations sur un Cloud TPU_

## Utiliser le Grad Check pour la rétropropagation ✔️

Dans plusieurs scénarios, j'ai dû implémenter moi-même un réseau de neurones. Et l'implémentation de la rétropropagation (backpropagation) est typiquement l'aspect le plus sujet aux erreurs et le plus difficile à déboguer.

Avec une rétropropagation incorrecte, votre modèle pourrait apprendre quelque chose qui semble raisonnable, ce qui le rend encore plus difficile à déboguer. Alors, ne serait-ce pas génial si nous pouvions implémenter quelque chose qui nous permettrait de déboguer nos réseaux de neurones facilement ?

J'utilise souvent le Gradient Check (vérification du gradient) lors de l'implémentation de la rétropropagation pour m'aider à la déboguer. L'idée ici est d'approcher les gradients en utilisant une approche numérique. Si elle est proche des gradients calculés par l'algorithme de rétropropagation, vous pouvez alors être plus confiant dans le fait que la rétropropagation a été implémentée correctement.

À l'heure actuelle, vous pouvez utiliser cette expression en termes standards pour obtenir un vecteur que nous appellerons `dθ[approx]` :

![Image](https://lh5.googleusercontent.com/BMyeu-1N1INBGjyDzdc_MNpRVToTt6lmidWN5CYualOQ67wvF_rki1axuSeCGkWNxr4dHnp1kA0zP6E3HmUw3SeofkUHhwsElB0kEvtst2220ycNfQCZGoumHnNQzWb8r_mST8Ep)
_Calculer les gradients approximatifs<span class="-mobiledoc-kit__atom">‌‌</span>_

Si vous cherchez le raisonnement derrière cela, vous pouvez en savoir plus dans [cet article](https://towardsdatascience.com/debugging-your-neural-nets-and-checking-your-gradients-f4d7f55da167) que j'ai écrit.

Nous avons donc maintenant deux vecteurs `dθ[approx]` et `dθ` (calculé par rétropropagation). Et ceux-ci devraient être presque égaux l'un à l'autre. Vous pourriez simplement calculer la distance euclidienne entre ces deux vecteurs et utiliser ce tableau de référence pour vous aider à déboguer vos réseaux :

![Image](https://lh5.googleusercontent.com/R-vrp1hq3psZmldrPYkupqofV7KOSWi0URLihhHAN5etHlR8U2kHdGE1XEAu-A9E_4w2Q8OmLXBZoYyyxJzIYwxG50dDPUSGL2gYw8U_lKCQtHXauUIUMa62H0mYp4eUO1LiJNnP)
_Tableau de référence_

## Mettez vos jeux de données en cache 💾

Mettre en cache les jeux de données est une idée simple, mais je ne l'ai pas vue beaucoup utilisée. L'idée ici est de parcourir l'intégralité du jeu de données et de le mettre en cache soit dans un fichier, soit en mémoire (s'il s'agit d'un petit jeu de données).

Cela devrait vous éviter d'effectuer certaines opérations CPU coûteuses comme l'ouverture de fichiers et la lecture de données à chaque époque.

Cela signifie également que votre première époque prendrait comparativement plus de temps 📉 puisque vous effectueriez idéalement toutes les opérations comme l'ouverture des fichiers et la lecture des données lors de la première époque, puis leur mise en cache. Mais les époques suivantes devraient être beaucoup plus rapides puisque vous utiliseriez les données mises en cache.

Cela semble vraiment être une idée très simple à mettre en œuvre, n'est-ce pas ? Voici un exemple avec TensorFlow montrant comment vous pouvez très facilement mettre en cache des jeux de données. Il montre également l'accélération 🚀 résultant de la mise en œuvre de cette idée. Retrouvez le code complet de l'exemple ci-dessous dans [ce gist](https://gist.github.com/Rishit-dagli/5d06c69c69e990f9e15249e15002bb07) de ma part.

![Image](https://lh5.googleusercontent.com/uMIS-r7tn2VD85nNQ1mNTyqaDwcTUeyV2mY47q1UkJvEEGoemFcuYPVgcyVDyG3E2a0iz9rrdimRGG9m9mOOEVZai_UiS1IRmiuvWYwOrmxHNuh711H0UVYum3o4u-8sWqcHrmvt)
_Un exemple simple de mise en cache des jeux de données et l'accélération obtenue_

## Comment s'attaquer au surapprentissage ⭐

Lorsque vous travaillez avec des réseaux de neurones, le surapprentissage (overfitting) et le sous-apprentissage (underfitting) peuvent être deux des problèmes les plus courants auxquels vous faites face. Cette section traite de certaines approches courantes que j'utilise pour résoudre ces problèmes.

Vous le savez peut-être, mais un biais élevé (high bias) vous fera manquer une relation entre les caractéristiques et les étiquettes (sous-apprentissage) et une variance élevée (high variance) amènera le modèle à capturer le bruit et à surapprendre les données d'entraînement.

Je pense que le moyen le plus efficace de résoudre le surapprentissage est d'obtenir plus de données – bien que vous puissiez également augmenter vos données (data augmentation). Un avantage des réseaux de neurones profonds est que leurs performances s'améliorent à mesure qu'ils reçoivent de plus en plus de données.

Mais dans beaucoup de situations, il peut être trop coûteux d'obtenir plus de données ou tout simplement impossible de le faire. Dans ce cas, parlons de quelques autres méthodes que vous pourriez utiliser pour lutter contre le surapprentissage.

En plus d'obtenir plus de données ou d'augmenter vos données, vous pourriez également lutter contre le surapprentissage soit en changeant l'architecture du réseau, soit en appliquant certaines modifications aux poids du réseau. Voyons ces deux méthodes.

### Changer l'architecture du modèle

Un moyen simple de changer l'architecture pour qu'elle ne surapprenne pas serait d'utiliser la Recherche Aléatoire pour tomber sur une bonne architecture. Ou vous pourriez essayer l'élagage (pruning) de nœuds de votre modèle, abaissant ainsi la capacité de votre modèle.

Nous avons déjà parlé de la Recherche Aléatoire, mais au cas où vous voudriez voir un exemple d'élagage, vous pourriez jeter un œil au [Guide d'élagage pour l'optimisation des modèles TensorFlow](https://www.tensorflow.org/model_optimization/guide/pruning).

### Modifier les poids du réseau

Dans cette section, nous verrons quelques méthodes que j'utilise couramment pour prévenir le surapprentissage en modifiant les poids d'un réseau.

#### Régularisation des poids

Pour revenir sur ce que nous avons discuté, "les modèles plus simples sont moins susceptibles de surapprendre que les modèles complexes". Nous essayons de limiter la complexité du réseau en forçant ses poids à ne prendre que de petites valeurs.

Pour ce faire, nous ajouterons à notre fonction de perte un terme qui peut pénaliser notre modèle s'il a des poids élevés. Souvent, les régularisations L₁ et L₂ sont utilisées, la différence étant :

* L1 - La pénalité ajoutée est ∝ à |coefficients de poids|
* L2 - La pénalité ajoutée est ∝ à |coefficients de poids|**²**

où |x| représente les valeurs absolues.

Remarquez-vous la différence entre L1 et L2, le terme au carré ? À cause de cela, L1 pourrait pousser les poids à être égaux à zéro alors que L2 aurait des poids tendant vers zéro mais pas nuls.

Si vous êtes curieux d'explorer cela davantage, [cet article](https://towardsdatascience.com/solving-overfitting-in-neural-nets-with-regularization-301c31a7735f) approfondit les régularisations et pourrait vous aider.

C'est aussi la raison exacte pour laquelle j'ai tendance à utiliser la régularisation L2 plus que la L1. Voyons un exemple de cela avec TensorFlow.

Voici un code pour créer une couche Dense simple avec 3 unités et la régularisation L2 :

```py
import tensorflow as tf
tf.keras.layers.Dense(3, kernel_regularizer = tf.keras.regularizers.L2(0.1))
```

Pour apporter plus de clarté sur ce que cela fait, comme nous l'avons discuté plus haut, cela ajouterait un terme (0,1 × valeur_coefficient_poids²) à la fonction de perte qui fonctionne comme une pénalité pour les poids très importants. De plus, il est aussi facile de remplacer L2 par L1 dans le code ci-dessus pour implémenter L1 pour votre couche.

#### Dropouts

La première chose que je fais quand je construis un modèle et que je fais face au surapprentissage est d'essayer d'utiliser des dropouts ([Srivastava et al.](https://jmlr.org/papers/v15/srivastava14a.html)). L'idée ici est d'abandonner aléatoirement ou de mettre à zéro (ignorer) x % des caractéristiques de sortie de la couche pendant l'entraînement.

Nous faisons cela pour empêcher les nœuds individuels de dépendre de la sortie d'autres nœuds et pour les empêcher de trop co-s'adapter à partir d'autres nœuds.

Les dropouts sont assez faciles à implémenter avec TensorFlow puisqu'ils sont disponibles sous forme de couches. Voici un exemple où j'essaie de construire un modèle pour différencier des images de chiens et de chats avec Dropout pour réduire le surapprentissage :

```py
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), padding='same', activation='relu',input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Conv2D(128, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

Comme vous pouvez le voir dans le code ci-dessus, vous pouvez directement utiliser `tf.keras.layers.dropout` pour implémenter le dropout, en lui passant la fraction de caractéristiques de sortie à ignorer (ici 20 % des caractéristiques de sortie).

#### Arrêt précoce (Early stopping)

L'arrêt précoce est une autre méthode de régularisation que j'utilise souvent. L'idée ici est de surveiller les performances du modèle à chaque époque sur un ensemble de validation et d'interrompre l'entraînement lorsque vous remplissez une condition spécifiée pour les performances de validation (comme arrêter l'entraînement quand la perte < 0,5).

Il s'avère que la condition de base dont nous avons parlé plus haut fonctionne à merveille si votre erreur d'entraînement et votre erreur de validation ressemblent à ce qu'il y a dans cette image. Dans ce cas, l'arrêt précoce arrêterait simplement l'entraînement lorsqu'il atteint la boîte rouge (pour la démonstration) et empêcherait purement et simplement le surapprentissage.

> C'est (l'arrêt précoce) une technique de régularisation si simple et efficace que Geoffrey Hinton l'a appelée un "beautiful free lunch". – Hands-On Machine Learning with Scikit-Learn and TensorFlow par Aurelien Geron

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-99.png)
_Adapté de [Lutz Prechelt](https://link.springer.com/chapter/10.1007/978-3-642-35289-8_5)_

Cependant, dans certains cas, vous ne vous retrouveriez pas avec des choix aussi simples pour identifier le critère ou savoir quand l'arrêt précoce devrait arrêter l'entraînement du modèle.

Pour la portée de cet article, nous ne parlerons pas d'autres critères ici, mais je vous recommande de consulter "[Early Stopping — But When, Lutz Prechelt](https://link.springer.com/chapter/10.1007/978-3-642-35289-8_5)" que j'utilise beaucoup pour aider à décider des critères.

Voyons un exemple d'arrêt précoce en action avec TensorFlow :

```py
import tensorflow as tf

callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
model = tf.keras.models.Sequential([...])
model.compile(...)
model.fit(..., callbacks = [callback])
```

Dans l'exemple ci-dessus, nous créons un callback EarlyStopping et spécifions que nous voulons surveiller nos valeurs de perte. Nous spécifions également qu'il doit arrêter l'entraînement s'il ne voit pas d'améliorations notables des valeurs de perte pendant 3 époques. Enfin, lors de l'entraînement du modèle, nous spécifions qu'il doit utiliser ce callback.

De plus, pour les besoins de cet exemple, je montre un modèle Sequential – mais cela pourrait fonctionner exactement de la même manière avec un modèle créé avec l'API fonctionnelle ou des modèles sous-classés également.

## Merci de m'avoir lu !

Merci d'être resté avec moi jusqu'à la fin. J'espère que vous bénéficierez de cet article et que vous intégrerez ces conseils dans vos propres expériences.

Je suis impatient de voir s'ils vous aident également à améliorer les performances de vos réseaux de neurones. Si vous avez des commentaires ou des suggestions pour moi, n'hésitez pas à me [contacter sur Twitter](https://twitter.com/rishit_dagli).