---
title: Comment déployer un modèle de détection d'objets avec TensorFlow Serving
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T16:02:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-an-object-detection-model-with-tensorflow-serving-d6436e65d1d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KsgfPj8hFhV27uRXSsHsIw.png
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment déployer un modèle de détection d'objets avec TensorFlow Serving
seo_desc: 'By Gaurav Kaila

  Object detection models are some of the most sophisticated deep learning models.
  They’re capable of localizing and classifying objects in real time both in images
  and videos. But what good is a model if it cannot be used for productio...'
---

Par Gaurav Kaila

Les modèles de détection d'objets sont parmi les modèles de deep learning les plus sophistiqués. Ils sont capables de localiser et de classer des objets en temps réel, à la fois dans des images et des vidéos. Mais à quoi bon un modèle s'il ne peut pas être utilisé en production ?

Grâce à l'équipe formidable de TensorFlow, nous disposons de TensorFlow Serving, capable de servir nos modèles en production. Il existe de très bons articles sur TensorFlow Serving pour bien démarrer, comme [celui-ci](https://www.tensorflow.org/serving/) et [celui-là](https://towardsdatascience.com/how-to-deploy-machine-learning-models-with-tensorflow-part-1-make-your-model-ready-for-serving-776a14ec3198).

Cet article se concentrera sur la manière dont nous pouvons servir spécifiquement des **modèles de détection d'objets** avec TF Serving. Il est motivé par le manque de bonnes ressources en ligne expliquant comment créer des modèles de détection d'objets prêts pour la production et des environnements TF-serving utilisant Docker. Nous discuterons également de la manière de servir le modèle et de créer un script côté client pour y accéder. Notre architecture ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kkcvSFxF2GGr7Trmjm8kcA.png)

Dans l'esprit de ne pas réinventer la roue, j'ai utilisé les ressources disponibles dans l'[API de détection d'objets](https://github.com/tensorflow/models/tree/master/research/object_detection) pour ce tutoriel. Je suppose que vous avez cloné l'API de détection d'objets de TensorFlow — mais si ce n'est pas le cas, faites ce qui suit :

```
# Cloner le dépôt des modèles TensorFlow
git clone https://github.com/tensorflow/models.git
cd models/research/object_detection
```

### 1. Créer un modèle prêt pour la production pour TF-Serving

En supposant que vous avez entraîné votre modèle de détection d'objets en utilisant TensorFlow, vous aurez les quatre fichiers suivants enregistrés sur votre disque :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wwIWGlWy5xfS54Woy9raag.png)
_Fichiers du modèle entraîné enregistrés sur le disque_

Ces fichiers peuvent être utilisés pour [l'inférence directement](https://www.tensorflow.org/programmers_guide/saved_model). Ou nous pouvons utiliser le script _[freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)_ pour [convertir le modèle en un graphe figé](https://blog.metaflow.fr/tensorflow-how-to-freeze-a-model-and-serve-it-with-a-python-api-d4f3596b3adc) contenant l'architecture du modèle et les poids dans un seul fichier. Cela est utile pour des tests sur votre machine locale, mais n'est pas adapté à un environnement de production.

Pour créer des modèles prêts à être servis, nous allons modifier le fichier [_exporter.py_](https://github.com/tensorflow/models/blob/master/research/object_detection/exporter.py) disponible sur le dépôt GitHub de l'API de détection d'objets. Le script original disponible sur le dépôt n'enregistre pas les **Variables** nécessaires pour le service. Utilisez plutôt le script **_exporter.py_** suivant au lieu de celui de TensorFlow.

Les modifications suivantes ont été apportées au script **_exporter.py_** ci-dessus :

1. Modification de la méthode **__write_saved_model__**. Cela est nécessaire, car le script Python original n'enregistre pas les **_variables_**, qui sont nécessaires pour servir le modèle. Au lieu d'utiliser **_frozen_graph_def_**, nous utilisons **_trained_checkpoint_prefix_**, qui contient les poids du modèle sous forme de variables. (crédits à ce [problème GitHub](https://github.com/tensorflow/models/issues/1988))

2. Modification de la fonction d'appel de **_frozen_graph_def_** à **_trained_checkpoint_prefix_** en suivant :

3. Commenter le code qui enregistre des fichiers sur le disque non nécessaires pendant le service :

Vous êtes maintenant prêt à créer votre modèle qui peut être utilisé pour le service. Le code suivant peut vous aider à y parvenir :

Voici une explication de ce code :

1. Chaque modèle de détection d'objets a une configuration qui doit être passée à _export_model.py_. Cela comprend des informations concernant l'architecture du modèle. Pour plus d'informations, consultez ce [lien](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md).
2. La méthode **_get_configs_from_pipeline_file_** crée un dictionnaire à partir du fichier de configuration, et la méthode **_create_pipeline_proto_from_configs_** crée un objet proto buffer à partir de ce dictionnaire.
3. **_input_checkpoint_** est le chemin vers **_model.ckpt_** du modèle entraîné.
4. **_model_version_id_** est un entier pour la version actuelle du modèle. Cela est requis par TF-serving pour la gestion des versions des modèles.
5. **_object_detection.exporter_** enregistrera le modèle dans le format suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2jVWPNBi25L8hTmt0tal7w.png)
_Modèle prêt à être utilisé par TF-Serving_

**_1/_** est la version du modèle, **_saved_model.pb._** contient l'architecture du modèle, et le répertoire **_variables_** contient les poids du modèle. Ce modèle est prêt à être servi.

### 2. Créer un environnement TF-serving en utilisant Docker.

#### À propos de Docker

> Docker est un outil logiciel qui vous permet de packager des logiciels en unités standardisées pour le développement, l'expédition et le déploiement. Une image de conteneur Docker est un package léger, autonome et exécutable d'un logiciel qui inclut tout ce dont vous avez besoin pour l'exécuter : code, runtime, outils système, bibliothèques système, paramètres.

En bref, Docker nous permet d'isoler votre application et ses dépendances dans un package autonome qui peut être utilisé n'importe où et n'importe quand sans avoir à vous soucier de l'installation du code et des dépendances système.

Notre motivation pour utiliser Docker pour TensorFlow Serving est que nous pouvons expédier notre conteneur pour l'exécuter dans le cloud et facilement mettre à l'échelle notre service sans avoir à installer de dépendances à nouveau.

La [documentation officielle](https://www.tensorflow.org/serving/setup) de TensorFlow Serving décrit comment le construire à partir de la source. C'est bien, mais moi (et [beaucoup de la communauté](https://github.com/tensorflow/tensorflow/issues/14610#issuecomment-350412191)) avons eu des problèmes pour le compiler dans le conteneur Docker. Nous allons donc passer en revue les étapes une par une ici.

1. **Construire le conteneur en utilisant l'image Docker officielle**

En supposant que vous avez cloné le dépôt officiel de TensorFlow Serving comme décrit dans la dernière partie, vous pouvez construire l'image Docker en faisant ce qui suit :

```
# Se déplacer dans le répertoire des fichiers Docker
cd ./serving/tensorflow_serving/tools/docker/
```

```
# Construire l'image (CPU)
docker build --pull -t $USER/tensorflow-serving-devel-cpu -f Dockerfile.devel .
```

```
ou
```

```
# Construire l'image (GPU)
docker build --pull -t $USER/tensorflow-serving-devel-gpu -f Dockerfile.devel-gpu .
```

Avant de démarrer le conteneur Docker, augmentez la mémoire (à 10-12 Go) et les CPU (à 4-6) disponibles pour le conteneur dans la section des préférences de l'application Docker. La construction de TensorFlow Serving est un processus intensif en mémoire et les paramètres par défaut peuvent ne pas fonctionner. Une fois terminé, vous pouvez démarrer le conteneur comme ceci :

```
[POUR CPU]
docker run -it -p 9000:9000 $USER/tensorflow-serving-devel-cpu /bin/bash
```

```
ou
```

```
[POUR GPU]
docker run -it -p 9000:9000 $USER/tensorflow-serving-devel-gpu /bin/bash
```

Dans le conteneur, faites ce qui suit :

```
[POUR CPU]
# Cloner le dépôt GitHub de TensorFlow Serving dans le conteneur
git clone --recurse-submodules https://github.com/tensorflow/serving
cd serving/tensorflow
```

```
# Configurer TensorFlow
./configure
cd ..
```

```
# Construire TensorFlow Serving
bazel build -c opt --copt=-msse4.1 --copt=-msse4.2 tensorflow_serving/...
```

```
ou
```

```
[POUR GPU]
# Le dépôt GitHub de TensorFlow Serving est déjà présent dans le conteneur
# donc pas besoin de cloner à nouveau
# Configurer TensorFlow avec CUDA en acceptant (-y) --
# le flag with_CUDA_support
cd serving/tensorflow
./configure
```

```
# Construire TensorFlow Serving avec CUDA
bazel build -c opt --copt=-msse4.1 --copt=-msse4.2 --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-O3 --copt=/usr/local/cuda tensorflow_serving/...
```

Le processus de construction peut prendre jusqu'à une heure en fonction du système hôte et de la configuration de Docker. Une fois la construction terminée sans erreur, vous pouvez tester si le serveur de modèle est en cours d'exécution :

```
bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server
```

La sortie devrait ressembler à ceci :

```
Flags:
```

```
--port=8500                       int32 port to listen on
```

```
--enable_batching=false           bool enable batching
```

```
--batching_parameters_file=""     string If non-empty, read an ascii BatchingParameters protobuf from the supplied file name and use the contained values instead of the defaults.
```

```
--model_config_file=""            string If non-empty, read an ascii ModelServerConfig protobuf from the supplied file name, and serve the models in that file. This config file can be used to specify multiple models to serve and other advanced parameters including non-default version policy. (If used, --model_name, --model_base_path are ignored.)
```

```
--model_name="default"            string name of model (ignored if --model_config_file flag is set
```

```
--model_base_path=""              string path to export (ignored if --model_config_file flag is set, otherwise required)
```

```
--file_system_poll_wait_seconds=1 int32 interval in seconds between each poll of the file system for new model version
```

```
--tensorflow_session_parallelism=0 int64 Number of threads to use for running a Tensorflow session. Auto-configured by default.Note that this option is ignored if --platform_config_file is non-empty.
```

```
--platform_config_file=""         string If non-empty, read an ascii PlatformConfigMap protobuf from the supplied file name, and use that platform config instead of the Tensorflow platform. (If used, --enable_batching is ignored.)
```

Votre environnement de service est maintenant prêt à être utilisé. Quittez le conteneur et validez les modifications dans le conteneur pour créer une image. Vous pouvez faire cela comme suit :

* Appuyez sur [Ctrl-p] + [Ctrl-q] pour quitter le conteneur
* Trouvez l'ID du conteneur :

```
# Trouver l'ID du conteneur
docker ps
CONTAINER ID        IMAGE                        COMMAND             CREATED             STATUS              PORTS               NAMES
```

* Validez les modifications :

```
# Valider les modifications
[POUR CPU]
docker commit ${CONTAINER ID} $USER/tensorflow-serving-devel-cpu
```

```
ou
```

```
[POUR GPU]
docker commit ${CONTAINER ID} $USER/tensorflow-serving-devel-gpu
```

* Réentrez dans le conteneur :

```
docker exec -it ${CONTAINER ID} /bin/bash
```

Remarque : Pour que le conteneur TensorFlow Serving accède aux GPU de votre système hôte, vous devez [installer nvidia-docker](https://github.com/NVIDIA/nvidia-docker) sur votre système et exécuter le conteneur comme ceci :

```
nvidia-docker docker run -it -p 9000:9000 $USER/tensorflow-serving-devel-gpu /bin/bash
```

Vous pouvez ensuite vérifier l'utilisation de votre GPU à l'intérieur du conteneur en utilisant la commande **_nvidia-smi_**.

#### Images Docker pré-construites

Comme je l'ai vu sur un certain nombre de problèmes GitHub (voir les ressources), les gens ne parviennent pas à compiler TensorFlow Serving sur Docker. J'ai donc pré-construit des images Docker pour la prise en charge des CPU et des GPU.

Vous pouvez les trouver sur ma [page Docker Hub](https://hub.docker.com/u/gauravkaila/) ou vous pouvez télécharger les images comme ceci :

```
[POUR CPU]
docker pull gauravkaila/tf_serving_cpu
```

```
ou
```

```
[POUR GPU]
docker pull gauravkaila/tf_serving_gpu
```

### 3. Créer un client pour demander au serveur de modèle en cours d'exécution dans le conteneur Docker d'effectuer une inférence sur une image de test

#### Introduction rapide à gRPC (Google Remote Procedure Call) et Protocol Buffers

gRPC (Remote Procedure Call de Google) est le protocole RPC enveloppé HTTP2 de Google. Cela permet à un client s'exécutant sur un ordinateur d'accéder à un ordinateur distant, via le réseau informatique, et d'appeler une « fonction » sur cet ordinateur distant comme si la fonction était locale au client.

TensorFlow Serving utilise ce protocole pour servir des modèles pour l'inférence. Selon la [documentation officielle](https://grpc.io/docs/guides/),

> Dans gRPC, une application cliente peut appeler directement des méthodes sur une application serveur sur une machine différente comme si c'était un objet local, ce qui facilite la création d'applications et de services distribués.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RO0XkZlu83u4S4BuyOH6_A.png)
_Architecture gRPC_

Ici, le serveur gRPC est notre conteneur Docker exécutant le service TensorFlow Serving, et notre client est en Python qui demande ce service pour l'inférence. [Cet article décrit comment RPC fonctionne de manière très structurée.](https://scotch.io/tutorials/implementing-remote-procedure-calls-with-grpc-and-protocol-buffers)

gRPC utilise [**Protocol Buffers**](https://developers.google.com/protocol-buffers/) pour sérialiser des données structurées ainsi que pour définir les paramètres et les réponses de retour pour les méthodes appelables. Il est neutre en termes de langage et de plateforme. Il dispose d'un langage structuré qui compile ensuite le code de sérialisation de transport dans le langage de votre choix pour être inclus dans votre projet. Il transmet les données au format binaire, qui est plus petit et plus rapide par rapport au bon vieux JSON et XML.

#### Créer le client

Une demande TensorFlow Serving peut être de trois types :

1. Classification : Utilise l'API RPC de classification qui accepte un tenseur d'entrée (par exemple, une image) et produit une classe et un score.
2. Prédiction et Régression : Utilise l'API RPC de prédiction qui accepte un tenseur d'entrée (par exemple, une image) et produit plusieurs tenseurs tels que (pour la détection d'objets) des boîtes englobantes, des classes, des scores, etc.

Étant donné que le problème ici est un problème de prédiction, nous utiliserons l'API RPC de prédiction. Pour cela, nous avons besoin des protobufs de prédiction disponibles sur le [GitHub de TensorFlow Serving](https://github.com/tensorflow/serving/tree/master/tensorflow_serving/apis), et nous devons les convertir en code spécifique à notre langage (c'est-à-dire Python).

Vous pouvez le faire vous-même, ou opter pour la méthode facile et télécharger les fichiers Python depuis ce [dépôt GitHub](https://github.com/Vetal1977/tf_serving_example/tree/master/tensorflow_serving/apis). Nous utiliserons cet objet protobuf pour créer une demande de prédiction dans notre client.

**Modèle d'un client RPC de prédiction**

Stub est un morceau de code utilisé pour convertir les paramètres lors d'un appel de procédure à distance (RPC). Comme le client et le serveur se trouvent dans des espaces d'adressage différents, le paramètre envoyé du client au serveur (et vice-versa) doit être converti afin que l'ordinateur serveur distant perçoive l'appel RPC comme un appel de fonction local. Le stub utilisé ici est le code généré à partir du protobuf de prédiction comme décrit ci-dessus.

#### Lancer le service TensorFlow Serving

Comme décrit dans la partie précédente, notre service TensorFlow Serving s'exécutera dans un conteneur Docker avec des ports ouverts vers l'extérieur. En supposant que l'image Docker est disponible, le conteneur peut être démarré comme ceci :

```
$ docker run -it -d -P --name tf_serving_cpu -p 3000:3000 gauravkaila/tf_serving_cpu
```

Ici, le port 3000 est ouvert au monde et le client peut accéder au service TensorFlow Serving via ce port. Exportez le répertoire du modèle créé dans la première partie vers un dossier à l'intérieur du conteneur :

```
$ docker cp /path/to/model tf_serving_cpu:/path/to/destination
```

Pour exécuter le service, déplacez-vous dans le conteneur et démarrez :

```
# Se déplacer dans le répertoire serving/
$ cd serving/
```

```
# Démarrer le service
$ bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server --port=3000 --model_name=obj_det--model_base_path=/path/to/dest &> obj_det &
```

Assurez-vous que le flag **model_name** a le même nom que celui spécifié dans le client. La sortie est enregistrée dans **obj_det**. Si tout s'est bien passé, vous pourrez voir la sortie suivante lorsque vous tapez :

```
$ tail -f obj_det
```

> tensorflow_serving/model_servers/main.cc:288] Running ModelServer at 0.0.0.0:3000 …

Le modèle est servi et est prêt à être utilisé par notre client.

#### Visualiser les boîtes englobantes sur les images de test

Le but d'un modèle de détection d'objets est de visualiser les boîtes englobantes des objets localisés sur l'image. Afin de visualiser l'image finale avec les boîtes englobantes, nous utiliserons le fichier [**visualization_utils.py**](https://github.com/tensorflow/models/blob/master/research/object_detection/utils/visualization_utils.py) de l'API de détection d'objets de TensorFlow.

Nous pouvons accéder aux sorties individuelles à partir du résultat comme ceci :

```
boxes = result.outputs['detection_boxes'].float_val
classes = result.outputs['detection_classes'].float_val
scores = result.outputs['detection_scores'].float_val
```

Cela retourne des objets protobuf qui peuvent être alimentés dans le fichier **visualization_utils.py** :

```
image_vis = vis_util.visualize_boxes_and_labels_on_image_array(
    {input_image},
    np.reshape(boxes,[100,4]),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=8)
```

Le script client final ressemblera à ceci :

#### Sortie finale

En envoyant une image de test d'une horloge, notre sortie finale devrait ressembler à ceci. **Remarque** : le modèle utilisé ici est un Faster RCNN pré-entraîné sur le jeu de données COCO pour lequel le numéro de classe 85 correspond à une horloge.

```
outputs {key: "detection_boxes"
value {dtype: DT_FLOAT
tensor_shape {
dim {size: 1}
dim {size: 300}
dim {size: 4}}
float_val: 0.24750074744224548
float_val: 0.17159424722194672
float_val: 0.9083144068717957
float_val: 0.797699511051178
```

```
outputs {key: "detection_classes"
value {dtype: DT_FLOAT
tensor_shape {
dim {size: 1}
dim {size: 300}}
float_val: 85.0
```

```
outputs {key: "detection_scores"
value {dtype: DT_FLOAT
tensor_shape {
dim {size: 1}
dim {size: 300}}
float_val: 0.9963208436965942
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*lKKk2xTheqKRNoAJoGj48A.jpeg)

#### Ce que nous avons accompli

Nous avons commencé avec un cas d'utilisation de détection d'objets pour démontrer la puissance de TensorFlow Serving. Nous avons exporté notre modèle entraîné dans un format attendu par TensorFlow Serving, compilé TF-Serving en utilisant Docker, et créé un script client qui pouvait demander au serveur de modèle d'effectuer une inférence.

#### Que réserve l'avenir

1. En utilisant ce cas d'utilisation comme modèle, nous pouvons utiliser TensorFlow Serving pour servir d'autres modèles de prédiction et de classification.
2. Nous pouvons exploiter la version GPU de TensorFlow Serving pour obtenir une inférence plus rapide.
3. Nous pouvons mettre à l'échelle notre service en déployant plusieurs conteneurs Docker exécutant le service TF-Serving.
4. Vous pouvez regrouper les images d'entrée au lieu d'envoyer une image par demande.

#### Ressources

1. [API de détection d'objets TensorFlow](https://github.com/tensorflow/models/tree/master/research/object_detection)
2. [Ce blog génial sur TF-Serving](https://towardsdatascience.com/how-to-deploy-machine-learning-models-with-tensorflow-part-1-make-your-model-ready-for-serving-776a14ec3198)

**Problèmes GitHub :**

* [https://github.com/tensorflow/serving/issues/542](https://github.com/tensorflow/serving/issues/542)
* [https://github.com/tensorflow/serving/issues/590](https://github.com/tensorflow/serving/issues/590)
* [https://github.com/tensorflow/serving/issues/410](https://github.com/tensorflow/serving/issues/410)
* [https://github.com/tensorflow/serving/issues/672](https://github.com/tensorflow/serving/issues/672)
* [https://github.com/tensorflow/serving/issues/659](https://github.com/tensorflow/serving/issues/659)

**À propos de l'auteur :** Gaurav est un ingénieur en machine learning chez The Dock, le centre de recherche et d'innovation phare d'Accenture à Dublin, en Irlande. Ses intérêts incluent la construction de systèmes de deep learning scalables pour les applications de vision par ordinateur. En savoir plus sur [gauravkaila.com](http://gauravkaila.com)