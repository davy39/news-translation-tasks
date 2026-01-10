---
title: Comment valider vos modèles de Machine Learning à l'aide de TensorFlow Model
  Analysis
subtitle: ''
author: Salim Oyinlola
co_authors: []
series: null
date: '2022-10-05T14:37:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-machine-learning-models-with-tensorflow-model-analysis
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-159275.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
- name: Validation
  slug: validation
seo_title: Comment valider vos modèles de Machine Learning à l'aide de TensorFlow
  Model Analysis
seo_desc: "My first deployed Machine Learning model was a failure. It was a simple\
  \ Diabetes Diagnosis Model for potential diabetes mellitus patients – and quite\
  \ frankly, I was beyond excited on deployment. \nBut the excitement soon disappeared\
  \ when I received fe..."
---

Mon premier modèle de Machine Learning déployé a été un échec. Il s'agissait d'un simple modèle de diagnostic du diabète pour des patients potentiellement atteints de diabète sucré – et pour être honnête, j'étais plus qu'enthousiaste lors du déploiement.

Mais l'excitation a vite disparu lorsque j'ai reçu les retours des utilisateurs. Pour dire les choses simplement, les utilisateurs trouvaient que le modèle était mauvais.

J'en ai été attristé, mais avec le recul, ils avaient raison. Le modèle était peut-être performant en termes de métriques de haut niveau. Mais du point de vue du consommateur, si un modèle de machine learning fournit une mauvaise prévision, l'expérience de cette personne avec le modèle sera mauvaise.

Le problème était que certaines caractéristiques spécifiques du modèle, ou tranches de données (slices), entraînaient une mauvaise performance du modèle.

En résumé, avant de déployer tout modèle de machine learning, il incombe aux ingénieurs en machine learning de l'évaluer, de s'assurer qu'il respecte des normes de qualité strictes et qu'il agit comme prévu pour toutes les tranches de données pertinentes.

## Qu'est-ce que TensorFlow Model Analysis ?

Pour permettre aux ingénieurs en Machine Learning d'examiner les performances de leurs modèles à un niveau plus profond, Google a créé [TensorFlow Model Analysis (TFMA)](https://www.tensorflow.org/tfx/guide/tfma). Selon la documentation, « TFMA effectue ses calculs de manière distribuée sur de grandes quantités de données en utilisant Apache Beam ».

TFMA, en tant qu'outil, vous permet de creuser réellement dans les performances du modèle et de comprendre comment elles varient sur différentes tranches de données. Il prend en charge le calcul des métriques utilisées lors de l'entraînement (c'est-à-dire les métriques intégrées) ainsi que des métriques définies après la sauvegarde du modèle dans le cadre des paramètres de configuration de TFMA.

Dans ce tutoriel, vous analyserez et évaluerez les résultats d'un modèle de machine learning précédemment entraîné. Le modèle que vous utiliserez est entraîné pour un [Exemple Chicago Taxi](https://github.com/tensorflow/tfx/tree/master/tfx/examples/chicago_taxi_pipeline), qui utilise le [jeu de données Taxi Trips](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew) publié par la ville de Chicago. Vous pouvez consulter l'ensemble du jeu de données [ici](https://bigquery.cloud.google.com/dataset/bigquery-public-data:chicago_taxi_trips).

Une fois ce tutoriel terminé, vous serez en mesure d'utiliser Apache Beam pour effectuer un passage complet sur le jeu de données d'évaluation spécifié. De plus, vous aurez non seulement un calcul plus précis des métriques, mais vous pourrez également passer à des jeux de données d'évaluation massifs, car les pipelines Beam peuvent être exécutés à l'aide de back-ends de traitement distribué.

## Prérequis

* Connaissances fondamentales d'Apache Beam. Le [Guide de programmation Beam](https://beam.apache.org/documentation/programming-guide/) est un excellent point de départ.
* Compréhension fondamentale du fonctionnement des modèles de machine learning.
* Un nouveau notebook Google Colab pour exécuter le code Python dans votre Google Drive. Vous pouvez configurer cela en suivant ce [tutoriel](https://www.freecodecamp.org/news/google-colaboratory-python-code-in-your-google-drive/).

## Étape 1 – Comment installer TensorFlow Model Analysis (TFMA)

Une fois votre notebook Google Colab prêt, la première chose à faire est d'importer toutes les dépendances. Cela prendra un certain temps.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-23.png)
_Un nouveau notebook vierge en mode sombre_

Renommez le fichier de `Untitled.ipynb` à `TFMA.ipynb`.

```python
!pip install -U pip
!pip install tensorflow-model-analysis`
```

La première ligne met à jour `pip` vers la dernière version. `pip` est le système de gestion de paquets utilisé pour installer et gérer les paquets logiciels écrits en Python. Il signifie « preferred installer program ». La seconde ligne installera TensorFlow Model Analysis, TFMA.

Maintenant, une fois que c'est fait, redémarrez l'environnement d'exécution (runtime) avant d'exécuter les cellules ci-dessous. Il est important de redémarrer le runtime avant de lancer les cellules.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-26.png)

```python
import sys
assert sys.version_info.major==3 
import tensorflow as tf
import apache_beam as beam
import tensorflow_model_analysis as tfma

```

Ce bloc de code importe les bibliothèques nécessaires – `sys`, `tensorflow`, `apache_beam` et `tensorflow_model_analysis`. Vous utilisez la commande `assert sys.version_info.major==3` pour vérifier que le notebook est exécuté avec Python 3.

## Étape 2 – Comment charger le jeu de données

Vous allez télécharger le fichier `tar` et l'extraire.

```python
import io, os, tempfile
TAR_NAME = 'saved_models-2.2'
BASE_DIR = tempfile.mkdtemp()
DATA_DIR = os.path.join(BASE_DIR, TAR_NAME, 'data')
MODELS_DIR = os.path.join(BASE_DIR, TAR_NAME, 'models')
SCHEMA = os.path.join(BASE_DIR, TAR_NAME, 'schema.pbtxt')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

!curl -O https://storage.googleapis.com/artifacts.tfx-oss-public.appspot.com/datasets/{TAR_NAME}.tar
!tar xf {TAR_NAME}.tar
!mv {TAR_NAME} {BASE_DIR}
!rm {TAR_NAME}.tar

```

Le jeu de données téléchargé est au format de fichier `tar`. Il comprend les jeux de données d'entraînement, les jeux de données d'évaluation, le schéma des données et les modèles sauvegardés pour l'entraînement et le service, ainsi que les modèles sauvegardés pour l'évaluation. Vous en aurez besoin pour tout ce tutoriel.

## Étape 3 – Comment analyser le schéma

Vous devez analyser le schéma téléchargé afin de pouvoir l'utiliser avec TFMA.

```python
import tensorflow as tf
from google.protobuf import text_format
from tensorflow.python.lib.io import file_io
from tensorflow_metadata.proto.v0 import schema_pb2
from tensorflow.core.example import example_pb2

schema = schema_pb2.Schema()
contents = file_io.read_file_to_string(SCHEMA)
schema = text_format.Parse(contents, schema)

```

Vous analyserez le schéma en utilisant la méthode `text_format` de la bibliothèque `google.protobuf` pour convertir le message protobuf au format texte et le `schema_pb2` de TensorFlow.

## Étape 4 – Comment utiliser le schéma pour créer des TFRecords

L'étape suivante consiste à donner à TFMA l'accès à notre jeu de données. Pour cela, nous devons créer un fichier `TFRecords`. Nous avons utilisé notre schéma pour le créer, car il nous donne le type correct pour chaque caractéristique.

```python
import csv
datafile = os.path.join(DATA_DIR, 'eval', 'data.csv')
reader = csv.DictReader(open(datafile, 'r'))
examples = []
for line in reader:
  example = example_pb2.Example()
  for feature in schema.feature:
    key = feature.name
    if feature.type == schema_pb2.FLOAT:
      example.features.feature[key].float_list.value[:] = (
          [float(line[key])] if len(line[key]) > 0 else [])
    elif feature.type == schema_pb2.INT:
      example.features.feature[key].int64_list.value[:] = (
          [int(line[key])] if len(line[key]) > 0 else [])
    elif feature.type == schema_pb2.BYTES:
      example.features.feature[key].bytes_list.value[:] = (
          [line[key].encode('utf8')] if len(line[key]) > 0 else [])
  # Ajouter une nouvelle colonne 'big_tipper' qui indique si le pourboire était > 20 % du prix de la course. 
  # TODO(b/157064428) : À supprimer une fois que la transformation des étiquettes sera prise en charge pour Keras.
  big_tipper = float(line['tips']) > float(line['fare']) * 0.2
  example.features.feature['big_tipper'].float_list.value[:] = [big_tipper]
  examples.append(example)
tfrecord_file = os.path.join(BASE_DIR, 'train_data.rio')
with tf.io.TFRecordWriter(tfrecord_file) as writer:
  for example in examples:
    writer.write(example.SerializeToString())
!ls {tfrecord_file}

```

Il est à noter que TFMA prend en charge un certain nombre de types de modèles différents, notamment les modèles TF Keras, les modèles basés sur les API de signature génériques TF2, ainsi que les modèles basés sur les estimateurs TF. Cependant, pour ce tutoriel, vous configurerez un modèle basé sur Keras.

Dans votre [configuration](https://www.tensorflow.org/tfx/model_analysis/setup) Keras, vous ajouterez vos métriques et graphiques manuellement dans le cadre de la configuration (consultez le guide des [métriques](https://www.tensorflow.org/tfx/model_analysis/metrics) pour plus d'informations sur les métriques et les graphiques pris en charge).

## Étape 5 – Comment configurer et exécuter TFMA avec Keras

```python
import tensorflow_model_analysis as tfma

```

Vous allez enfin appeler et utiliser l'instance de `tfma` que vous avez précédemment importée à ce stade.

```python
# Vous allez configurer les paramètres tfma.EvalConfig
keras_eval_config = text_format.Parse("""
  ## Informations sur le modèle
  model_specs {
    # Pour Keras (et les modèles de service), nous devons ajouter une `label_key`.
    label_key: "big_tipper"
  }

  ## Vous publierez les informations sur les métriques d'entraînement. Celles-ci seront fusionnées avec toutes les
  ## métriques intégrées de l'entraînement.
  metrics_specs {
    metrics { class_name: "ExampleCount" }
    metrics { class_name: "BinaryAccuracy" }
    metrics { class_name: "BinaryCrossentropy" }
    metrics { class_name: "AUC" }
    metrics { class_name: "AUCPrecisionRecall" }
    metrics { class_name: "Precision" }
    metrics { class_name: "Recall" }
    metrics { class_name: "MeanLabel" }
    metrics { class_name: "MeanPrediction" }
    metrics { class_name: "Calibration" }
    metrics { class_name: "CalibrationPlot" }
    metrics { class_name: "ConfusionMatrixPlot" }
    # ... ajouter des métriques et des graphiques supplémentaires ...
  }

  ## Vous allez découper les informations (slicing)
  slicing_specs {}  # tranche globale
  slicing_specs {
    feature_keys: ["trip_start_hour"]
  }
  slicing_specs {
    feature_keys: ["trip_start_day"]
  }
  slicing_specs {
    feature_values: {
      key: "trip_start_month"
      value: "1"
    }
  }
  slicing_specs {
    feature_keys: ["trip_start_hour", "trip_start_day"]
  }
""", tfma.EvalConfig())

```

Il est également important de créer un `tfma.EvalSharedModel` qui pointe vers le modèle Keras.

```python
keras_model_path = os.path.join(MODELS_DIR, 'keras', '2')
keras_eval_shared_model = tfma.default_eval_shared_model(
    eval_saved_model_path=keras_model_path,
    eval_config=keras_eval_config)

keras_output_path = os.path.join(OUTPUT_DIR, 'keras')

```

Et enfin, vous exécutez TFMA, ce qui termine cette étape.

```python
keras_eval_result = tfma.run_model_analysis(
    eval_shared_model=keras_eval_shared_model,
    eval_config=keras_eval_config,
    data_location=tfrecord_file,
    output_path=keras_output_path)

```

Maintenant que vous avez exécuté l'évaluation, examinez les visualisations à l'aide de TFMA. Pour les exemples suivants, vous pouvez visualiser les résultats de l'évaluation effectuée sur le modèle Keras.

Pour afficher les métriques, vous utiliserez `[tfma.view.render_slicing_metrics](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/view/render_slicing_metrics)`. Par défaut, les vues afficheront la tranche `Overall` (globale). Pour afficher une tranche particulière, vous pouvez soit utiliser le nom de la colonne (en définissant `slicing_column`), soit fournir un [`tfma.SlicingSpec`](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/SlicingSpec).

## Étape 6 – Comment visualiser les métriques et les graphiques

À ce stade, il est important de noter que les colonnes utilisées dans le jeu de données sont les suivantes :

* `pickup_community_area`
* `fare`
* `trip_start_month`
* `trip_start_hour`
* `trip_start_day`
* `trip_start_timestamp`
* `pickup_latitude`
* `pickup_longitude`
* `dropoff_latitude`
* `dropoff_longitude`
* `trip_miles`
* `pickup_census_tract`
* `dropoff_census_tract`
* `payment_type`
* `company`
* `trip_seconds`
* `dropoff_community_area`, et
* `tips` 

Pour un premier essai et à titre d'exemple, vous pouvez définir `slicing_column` pour examiner la caractéristique `trip_start_hour` de nos précédents `slicing_specs`. Vous pourrez alors visualiser la colonne.

```python
tfma.view.render_slicing_metrics(keras_eval_result, slicing_column='trip_start_hour')
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-27.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-28.png)

En exécutant cela, vous verrez que la visualisation des métriques prend en charge les interactions suivantes :

* Cliquer et faire glisser pour déplacer la vue
* Faire défiler pour zoomer
* Clic droit pour réinitialiser la vue
* Survoler le point de données souhaité pour voir plus de détails.
* Choisir parmi quatre types de vues différents en utilisant les sélections en bas.

Notez que votre `tfma.EvalConfig` initial a créé toute une liste de `slicing_specs`, que vous pouvez visualiser en mettant à jour les informations de tranche passées à `tfma.view.render_slicing_metrics`. Ici, vous pouvez sélectionner la tranche `trip_start_day` (jours de la semaine).

```python
tfma.view.render_slicing_metrics(keras_eval_result, slicing_column='trip_start_day')

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-29.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-31.png)

TFMA prend également en charge la création de croisements de caractéristiques (feature crosses) pour analyser des combinaisons de caractéristiques. Pour tester cela, vous allez créer un croisement entre `trip_start_hour` et `trip_start_day`.

```python
tfma.view.render_slicing_metrics(
    keras_eval_result,
    slicing_spec=tfma.SlicingSpec(
        feature_keys=['trip_start_hour', 'trip_start_day']))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-32.png)

Maintenant, le croisement de ces deux colonnes crée énormément de combinaisons ! Mais vous allez restreindre votre croisement pour ne regarder que les _trajets qui commencent à 13h_. Ensuite, vous sélectionnerez `binary_accuracy` dans la visualisation comme indiqué ci-dessous.

```python
tfma.view.render_slicing_metrics(
    keras_eval_result,
    slicing_spec=tfma.SlicingSpec(
        feature_keys=['trip_start_day'], feature_values={'trip_start_hour': '13'}))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-33.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-34.png)

## Étape 7 – Comment suivre les performances de votre modèle au fil du temps

Vous utiliserez votre jeu de données d'entraînement pour entraîner votre modèle. Il sera, espérons-le, représentatif de votre jeu de données de test et des données qui seront envoyées à votre modèle en production.

Mais alors que les données dans les requêtes d'inférence peuvent rester les mêmes que vos données d'entraînement, dans de nombreux cas, elles commenceront à changer suffisamment pour que les performances de votre modèle évoluent.

Cela signifie que vous devez surveiller et mesurer les performances de votre modèle de manière continue, afin d'être conscient des changements et de pouvoir y réagir.

Voyons comment TFMA peut vous aider.

```python
output_paths = []
for i in range(3):
  # Créer un tfma.EvalSharedModel qui pointe vers notre modèle sauvegardé.
  eval_shared_model = tfma.default_eval_shared_model(
      eval_saved_model_path=os.path.join(MODELS_DIR, 'keras', str(i)),
      eval_config=keras_eval_config)

  output_path = os.path.join(OUTPUT_DIR, 'time_series', str(i))
  output_paths.append(output_path)

  # Exécuter TFMA
  tfma.run_model_analysis(eval_shared_model=eval_shared_model,
                          eval_config=keras_eval_config,
                          data_location=tfrecord_file,
                          output_path=output_path)
  
  eval_results_from_disk = tfma.load_eval_results(output_paths[:2])

tfma.view.render_time_series(eval_results_from_disk)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-35.png)

En utilisant `tfma`, vous pouvez valider et évaluer vos modèles de machine learning sur différentes tranches de données.

Vous pouvez voir sur l'image ci-dessus que vous pouvez évaluer les métriques `auc` (aire sous la courbe), `auc_precision_recall`, `binary_accuracy`, `binary_crossentropy`, `calibration`, `example_count`, `mean_label`, `mean_prediction`, `precision` et `recall` du modèle de machine learning.

## Conclusion

Enfin, il est important de noter que TFMA peut être configuré pour évaluer plusieurs modèles en même temps. En règle générale, vous faites cela pour comparer un nouveau modèle à une référence (baseline), comme le modèle actuellement en service, afin de déterminer quelles sont les différences de performance dans les métriques (par exemple l'AUC) par rapport à cette référence.

Lorsque des seuils sont configurés, TFMA produit un enregistrement [`tfma.ValidationResult`](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/ValidationResult) indiquant si la performance correspond aux attentes.

Si, à ce stade, vous vous posez des questions sur la différence entre l'évaluation des modèles de machine learning avec [TensorBoard](https://www.freecodecamp.org/news/how-to-evaluate-machine-learning-models-using-tensorboard/) et TensorFlow Metrics Analysis (TFMA), c'est une préoccupation légitime. Les deux sont des outils fournissant les mesures et les visualisations nécessaires pendant le flux de travail du Machine Learning.

Mais il est important de noter que vous les utilisez à différentes étapes du processus de développement. À un haut niveau, vous utilisez TensorBoard pour analyser le processus d'entraînement lui-même, tandis que TFMA s'occupe de l'analyse approfondie du modèle entraîné « fini ».

Merci de votre lecture !