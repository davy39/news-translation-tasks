---
title: Comment commencer à déboguer TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T12:35:46.000Z'
originalURL: https://freecodecamp.org/news/debugging-tensorflow-a-starter-e6668ce72617
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Tpvh9TOicl1dT3W-
tags:
- name: debugging
  slug: debugging
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: tensor
  slug: tensor
- name: TensorFlow
  slug: tensorflow
seo_title: Comment commencer à déboguer TensorFlow
seo_desc: 'By Daniel Deutsch

  Table of Contents


  What this is about

  The reference code base

  1. Fetch and print values within Session.run

  2. Use the tf.Print operation

  3. Use Tensorboard visualization for monitoring

  a) clean the graph with proper names and name s...'
---

Par Daniel Deutsch

### Table des Matières

* [De quoi il s'agit](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#de-quoi-il-sagit)
* [La base de code de référence](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#la-base-de-code-de-reference)
* [1. Récupérer et afficher des valeurs dans Session.run](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#1-recuperer-et-afficher-des-valeurs-dans-sessionrun)
* [2. Utiliser l'opération tf.Print](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#2-utiliser-loperation-tfprint)
* [3. Utiliser la visualisation Tensorboard pour le monitoring](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#3-utiliser-la-visualisation-tensorboard-pour-le-monitoring)
* [a) nettoyer le graphe avec des noms et des portées de noms appropriés](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#a-nettoyer-le-graphe-avec-des-noms-et-des-portees-de-noms-approprie)
* [b) Ajouter des tf.summaries](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#b-ajouter-des-tfsummaries)
* [c) Ajouter un tf.summary.FileWriter pour créer des fichiers de log](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#c-ajouter-un-tfsummaryfilewriter-pour-creer-des-fichiers-de-log)
* [d) Démarrer le serveur tensorboard depuis votre terminal](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#d-demarrer-le-serveur-tensorboard-depuis-votre-terminal)
* [4. Utiliser le débogueur Tensorboard](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#4-utiliser-le-debogueur-tensorboard)
* [5. Utiliser le débogueur TensorFlow](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#5-utiliser-le-debogueur-tensorflow)
* [Conclusion](https://github.com/Createdd/Writing/blob/master/2018/articles/DebugTFBasics.md#conclusion)

### De quoi il s'agit

> _Déboguer est deux fois plus difficile que d'écrire le code en premier lieu. Par conséquent, si vous écrivez le code de la manière la plus intelligente possible, vous n'êtes, par définition, pas assez intelligent pour le déboguer. — BRIAN W. KERNIGHAN_

Le débogage en général peut être une tâche fastidieuse et difficile. Néanmoins, vous devez être à l'aise pour parcourir le code écrit et identifier les problèmes. Normalement, il existe de nombreux guides, et le processus de débogage est souvent bien documenté pour de nombreux langages et frameworks.

Cependant, lorsqu'il s'agit de TensorFlow, de nouveaux défis apparaissent en raison de son fonctionnement.

Comme le précise la [documentation officielle](https://www.tensorflow.org/guide/low_level_intro) :

Un programme TensorFlow Core se compose de deux sections distinctes :

1. Construction du graphe de calcul (un tf.Graph).
2. Exécution du graphe de calcul (en utilisant un tf.Session).

![Image](https://cdn-media-1.freecodecamp.org/images/5pJQsrMBjTL0bpKAOpec0kfI0MklVYYH7TIa)
_Source et crédit à [https://www.tensorflow.org/guide/graphs](https://www.tensorflow.org/guide/graphs" rel="noopener" target="_blank" title=")_

Le calcul réel est effectué avec `session.run()`, ce qui signifie que nous devons trouver un moyen d'inspecter les valeurs à l'intérieur de cette fonction.

### La base de code de référence

En référence, je vais fournir mon dépôt Github avec le code correspondant [ici](https://github.com/Createdd/tensorFlowTest/blob/debug/mnistPlain/mnistBasic.py).

Nous allons utiliser un réseau de neurones de base pour classer les chiffres manuscrits du jeu de données MNIST, en utilisant :

* `tf.nn.softmax_cross_entropy_with_logits_v2` comme opération de classification TF pour définir la perte
* `tf.train.GradientDescentOptimizer` pour minimiser la perte

L'exécution de ce petit réseau de neurones montre qu'il peut déjà atteindre une précision d'environ 92 % :

### Le processus de débogage

Maintenant, pour le débogage, il existe essentiellement 5 façons (pragmatiques) d'y parvenir.

> _En tant que note : Il est souvent utile d'assertionner les formes pour s'assurer que tout fonctionne ensemble comme prévu._

#### 1. Récupérer et afficher des valeurs dans Session.run

C'est probablement le moyen le plus rapide et le plus facile d'obtenir les informations dont vous avez besoin.

* facile et rapide
* toute évaluation peut être récupérée de partout
* il est nécessaire de conserver la référence au tenseur, ce qui est mauvais dans les modèles complexes

En essence, vous exécutez la session dans une instruction d'impression et vous lui passez le dictionnaire, comme ceci : `print( f"Le paramètre de biais est : {sess.run(b, feed_dict={x: mnist.test.images, y_: mnist.test.labels})}" )`

Si le code devient plus complexe, l'[exécution partial_run d'une session](https://www.tensorflow.org/api_docs/python/tf/Session#partial_run) pourrait être utilisée. Mais comme il s'agit d'une fonctionnalité expérimentale, je ne l'implémenterai pas pour la démonstration.

De plus, n'oubliez pas la méthode `[.eval()](https://www.tensorflow.org/api_docs/python/tf/Tensor#eval)` pour évaluer spécifiquement les tenseurs.

[Voir le code complet ici sur Github.](https://github.com/Createdd/tensorFlowTest/blob/debug/fetchValuesInSession/mnistBasic.py)

#### 2. Utiliser l'opération tf.Print

La [méthode tf.Print](https://www.tensorflow.org/api_docs/python/tf/Print) est utile lors de l'évaluation en temps réel lorsque nous ne voulons pas explicitement récupérer le code avec session.run(). Il s'agit d'une opération d'identité qui imprime les données lors de l'évaluation.

* elle nous permet de voir le développement des valeurs lors de l'évaluation
* elle a une configuration limitée et peut donc facilement encombrer le terminal

Yufeng G a créé une vidéo fantastique et [un article sur l'utilisation de l'instruction tf.Print](https://towardsdatascience.com/using-tf-print-in-tensorflow-aa26e1cff11e). Et comme il le souligne, il est vital de structurer le nœud d'impression de la manière dont il est utilisé. Comme il dit :

> _Il est vitalement important que vous utilisiez réellement ce nœud retourné, car si vous ne le faites pas, il sera suspendu._

Dans mon code, j'ai ajouté une instruction d'impression qui récupère les valeurs dans la session pour illustrer comment les deux méthodes se comportent différemment lors de l'exécution.

Avec l'évaluation en temps réel vient la possibilité d'[assertion en temps réel](https://www.tensorflow.org/api_guides/python/check_ops#asserts-and-boolean-checks) avec `tf.Assert`.

[Voir le code complet ici.](https://github.com/Createdd/tensorFlowTest/blob/debug/tfPrint/mnistBasic.py)

#### 3. Utiliser la visualisation Tensorboard pour le monitoring

Avant de plonger dans cette méthode de débogage, sachez qu'il existe Tensorboard et le débogueur Tensorboard !

Le [site TF](https://www.tensorflow.org/guide/summaries_and_tensorboard) offre un excellent tutoriel pour implémenter et utiliser le tableau de bord.

Une clé pour l'utilisation est la sérialisation des données. TensorFlow fournit les opérations de résumé, qui vous permettent d'exporter des informations condensées sur le modèle. Elles sont comme des ancres disant au tableau de visualisation quoi tracer.

**a) Nettoyer le graphe avec des noms et des portées de noms appropriés**

Tout d'abord, nous devons organiser toutes les variables et opérations avec les méthodes de `[scope](https://www.tensorflow.org/guide/graph_viz#name_scoping_and_nodes)` que TF fournit.

```
with tf.name_scope("variables_scope"):    x = tf.placeholder(tf.float32, shape=[None, 784], name="x_placeholder")    y_ = tf.placeholder(tf.float32, shape=[None, 10], name="y_placeholder")
```

**b) Ajouter des tf.summaries**

Par exemple :

```
with tf.name_scope("weights_scope"):    W = tf.Variable(tf.zeros([784, 10]), name="weights_variable")    tf.summary.histogram("weight_histogram", W)
```

**c) Ajouter un tf.summary.FileWriter pour créer des fichiers de log**

Conseil : Assurez-vous de créer des sous-dossiers pour chaque log afin d'éviter l'accumulation de graphes.

**d) Démarrer le serveur tensorboard depuis votre terminal**

Par exemple : `tensorboard --logdir=./tfb_logs/ --port=8090 --host=127.0.0.1`

En naviguant vers le serveur tensorboard (dans ce cas `http://127.0.0.1:8090`), on voit ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/offiWwNnxs5aZ7J8i3J7hOn1fUVxsXQ3291B)
_L'onglet distributions de tensorboard_

Maintenant, toute la puissance et l'utilisation de tensorboard deviennent claires. Il vous permet très facilement de repérer les erreurs dans votre modèle de machine learning. Mon exemple de code est très simple. Imaginez un modèle avec plusieurs couches et plus de variables et d'opérations !

[Voir le code complet ici sur Github.](https://github.com/Createdd/tensorFlowTest/blob/debug/tensorboard/mnistBasic.py)

#### 4. Utiliser le débogueur Tensorboard

Comme le précise le [dépôt Github Tensorboard](https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/debugger) :

> _Ce tableau de bord est en version alpha. Certaines fonctionnalités ne sont pas encore pleinement fonctionnelles._

Cependant, il peut encore être utilisé et offre des fonctionnalités de débogage intéressantes. Veuillez consulter le dépôt Github pour obtenir un aperçu adéquat. Consultez également leur [vidéo](https://www.youtube.com/watch?v=XcHWLsVmHvk) pour une compréhension plus approfondie. Ils ont fait un excellent travail.

Pour y parvenir, il y a 3 choses à ajouter à notre exemple précédent :

1. Importer `from tensorflow.python import debug as tf_debug`
2. Ajouter votre session avec `tf_debug.TensorBoardDebugWrapsperSession`
3. Ajouter à votre serveur tensorboard le `debugger_port`

Maintenant, vous avez la possibilité de déboguer tout le modèle visualisé comme avec n'importe quel autre débogueur, mais avec une belle carte. Vous êtes en mesure de sélectionner certains nœuds et de les inspecter, de contrôler l'exécution avec les boutons "step" et "continue", et de visualiser les tenseurs et leurs valeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/TfHCodSEr9yVNORtks9rB8mbJccZWEb8vueQ)
_La fonction de débogage de tensorboard en action_

Il y a beaucoup plus à dire sur cette fonctionnalité unique de Tensorflow, mais je consacrerai probablement un autre article à cela.

[Voir mon code complet ici sur Github.](https://github.com/Createdd/tensorFlowTest/blob/debug/tensorboardDebugger/mnistBasic.py)

#### 5. Utiliser le débogueur TensorFlow

La dernière méthode, mais aussi très puissante, est le [débogueur CLI TensorFlow](https://www.tensorflow.org/guide/debugger).

Ce débogueur se concentre sur l'interface de ligne de commande (CLI) de tfdbg, par opposition à l'interface graphique (GUI) de tfdbg, qui est le plugin de débogage TensorBoard.

Vous enveloppez simplement la session avec `tf_debug.LocalCLIDebugWrapperSession(sess)` et puis vous commencez le débogage en exécutant le fichier (peut-être est-il nécessaire d'ajouter le drapeau `--debug`).

Il vous permet essentiellement de lancer et de parcourir l'exécution de votre modèle, tout en fournissant des métriques d'évaluation.

Je pense que la [documentation officielle](https://www.tensorflow.org/guide/debugger#frequently_asked_questions) pourrait être améliorée, mais ils ont également créé une [vidéo](https://www.youtube.com/watch?v=CA7fjRfduOI&t=53s) qui introduit la fonctionnalité de manière adéquate.

Les principales fonctionnalités ici sont les commandes `invoke_stepper` et ensuite appuyer sur `s` pour parcourir chaque opération. C'est la fonctionnalité de base d'un débogueur mais dans le CLI. Cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/iU14oHmUGXh3dF35HToJ6MFFpB-fOTUq7ZIS)
_Métriques d'évaluation lors du débogage avec le CLI_

[Voir le code complet ici sur Github.](https://github.com/Createdd/tensorFlowTest/blob/debug/tfdbg/mnistBasic.py)

### Conclusion

Comme montré, il existe de nombreuses façons de déboguer une application TensorFlow. Chaque méthode a ses propres forces et faiblesses. Je n'ai pas mentionné le débogueur Python, car il n'est pas spécifique à TensorFlow, mais gardez à l'esprit que le simple débogueur Python fournit déjà quelques bonnes informations !

Il y a une excellente [présentation par Wookayin](https://wookayin.github.io/tensorflow-talk-debugging/#74) qui parle de ces concepts mais donne également quelques conseils généraux sur le débogage. Ces conseils sont :

* nommer correctement les tenseurs
* vérifier et nettoyer les entrées
* journalisation
* assertions
* utilisation correcte des exceptions
* échouer rapidement -> interrompre immédiatement si quelque chose ne va pas
* ne vous répétez pas
* organisez vos modules et votre code

Je suis vraiment enthousiaste pour toutes les fonctionnalités que TensorFlow a à offrir pour les personnes qui construisent des systèmes de machine learning. Ils font un excellent travail ! J'ai hâte de voir les développements futurs ! :)

Merci d'avoir lu mon article ! N'hésitez pas à laisser vos commentaires !

Daniel est un étudiant en LL.M. en droit des affaires, travaillant comme ingénieur logiciel et organisateur d'événements technologiques à Vienne. Ses efforts d'apprentissage personnel actuels se concentrent sur le machine learning.

Connectez-vous sur :

* [LinkedIn](https://www.linkedin.com/in/createdd)
* [Github](https://github.com/Createdd)
* [Medium](https://medium.com/@ddcreationstudi)
* [Twitter](https://twitter.com/DDCreationStudi)
* [Steemit](https://steemit.com/@createdd)
* [Hashnode](https://hashnode.com/@DDCreationStudio)