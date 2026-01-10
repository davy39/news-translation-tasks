---
title: Comment déployer des modèles TensorFlow en production avec TF Serving
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-15T23:10:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-tensorflow-models-to-production-using-tf-serving-4b4b78d41700
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xNJAAxtjy5tgQDIcfxd-Yw.jpeg
tags:
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: Comment déployer des modèles TensorFlow en production avec TF Serving
seo_desc: 'By Thalles Silva

  Introduction

  Putting Machine Learning (ML) models to production has become a popular, recurrent
  topic. Many companies and frameworks offer different solutions that aim to tackle
  this issue.

  To address this concern, Google released Te...'
---

Par Thalles Silva

### Introduction

Mettre des modèles de Machine Learning (ML) en production est devenu un sujet populaire et récurrent. De nombreuses entreprises et frameworks offrent différentes solutions pour résoudre ce problème.

Pour répondre à cette préoccupation, Google a publié TensorFlow (TF) Serving dans l'espoir de résoudre le problème de déploiement des modèles ML en production.

Cet article propose un tutoriel pratique sur le service d'un réseau de segmentation sémantique convolutionnel pré-entraîné. À la fin de cet article, vous serez en mesure d'utiliser TF Serving pour déployer et faire des requêtes à un CNN profond entraîné dans TF. De plus, je présenterai un aperçu des principaux blocs de TF Serving, et je discuterai de ses APIs et de son fonctionnement.

Une chose que vous remarquerez tout de suite est qu'il nécessite très peu de code pour servir un modèle TF. Si vous souhaitez suivre le tutoriel et exécuter l'exemple sur votre machine, suivez-le tel quel. Mais, si vous voulez seulement en savoir plus sur TensorFlow Serving, vous pouvez vous concentrer sur les deux premières sections.

Cet article met en avant une partie du travail que nous faisons ici chez [Daitan Group](http://www.daitangroup.com/).

### TensorFlow Serving Libraries — Un aperçu

Prenons le temps de comprendre comment TF Serving gère le cycle de vie complet du service des modèles ML. Ici, nous passerons en revue (à un niveau élevé) chacun des principaux blocs de construction de TF Serving. Le but de cette section est de fournir une introduction douce aux APIs de TF Serving. Pour un aperçu approfondi, veuillez consulter la page de documentation de [TF Serving](https://www.tensorflow.org/serving/).

TensorFlow Serving est composé de quelques abstractions. Ces abstractions implémentent des APIs pour différentes tâches. Les plus importantes sont Servable, Loader, Source et Manager. Passons en revue comment elles interagissent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TwfOoS3M8DaUiB7ntP07_w.png)

En résumé, le cycle de vie du service commence lorsque TF Serving identifie un modèle sur le disque. Le composant Source s'en occupe. Il est responsable de l'identification des nouveaux modèles qui doivent être chargés. En pratique, il surveille le système de fichiers pour identifier quand une nouvelle version de modèle arrive sur le disque. Lorsqu'il voit une nouvelle version, il procède en créant un Loader pour cette version spécifique du modèle.

En résumé, le Loader connaît presque tout sur le modèle. Cela inclut comment le charger et comment estimer les ressources requises par le modèle, telles que la RAM et la mémoire GPU demandées. Le Loader dispose d'un pointeur vers le modèle sur le disque ainsi que toutes les méta-données nécessaires pour le charger. Mais il y a un piège ici : le Loader n'est pas autorisé à charger le modèle tout de suite.

Après avoir créé le Loader, la Source l'envoie au Manager en tant que version Aspirée.

Lors de la réception de la version Aspirée du modèle, le Manager procède au processus de service. Ici, il y a deux possibilités. La première est que la première version du modèle est poussée pour le déploiement. Dans cette situation, le Manager s'assurera que les ressources requises sont disponibles. Une fois qu'elles le sont, le Manager donne au Loader la permission de charger le modèle.

La seconde est que nous poussons une nouvelle version d'un modèle existant. Dans ce cas, le Manager doit consulter le plugin Version Policy avant d'aller plus loin. La Version Policy détermine comment le processus de chargement d'une nouvelle version de modèle se déroule.

Plus précisément, lors du chargement d'une nouvelle version d'un modèle, nous pouvons choisir entre préserver (1) la disponibilité ou (2) les ressources. Dans le premier cas, nous nous intéressons à nous assurer que notre système est toujours disponible pour les requêtes des clients entrants. Nous savons que le Manager permet au Loader d'instancier le nouveau graphe avec les nouveaux poids.

À ce stade, nous avons deux versions de modèle chargées en même temps. Mais le Manager décharge l'ancienne version uniquement après que le chargement soit terminé et qu'il soit sûr de basculer entre les modèles.

D'autre part, si nous voulons économiser des ressources en n'ayant pas le tampon supplémentaire (pour la nouvelle version), nous pouvons choisir de préserver les ressources. Cela peut être utile pour des modèles très lourds d'avoir un petit écart de disponibilité, en échange d'économiser de la mémoire.

À la fin, lorsqu'un client demande un handle pour le modèle, le Manager retourne un handle pour le Servable.

Avec cet aperçu, nous sommes prêts à plonger dans une application réelle. Dans les sections suivantes, nous décrivons comment servir un réseau de neurones convolutionnel (CNN) en utilisant TF Serving.

### Exporter un modèle pour le service

La première étape pour servir un modèle ML construit dans TensorFlow est de s'assurer qu'il est dans le bon format. Pour cela, TensorFlow fournit la classe [SavedModel](https://www.tensorflow.org/programmers_guide/saved_model).

SavedModel est le format de sérialisation universel pour les modèles TensorFlow. Si vous êtes familier avec TF, vous avez probablement utilisé le TensorFlow Saver pour persister les variables de votre modèle.

Le TensorFlow Saver fournit des fonctionnalités pour sauvegarder/restaurer les fichiers de point de contrôle du modèle vers/depuis le disque. En fait, SavedModel enveloppe le TensorFlow Saver et est destiné à être la manière standard d'exporter les modèles TF pour le service.

L'objet SavedModel possède quelques fonctionnalités intéressantes.

Premièrement, il vous permet de sauvegarder plus d'un méta-graphe dans un seul objet SavedModel. En d'autres termes, il nous permet d'avoir différents graphes pour différentes tâches.

Par exemple, supposons que vous venez de terminer l'entraînement de votre modèle. Dans la plupart des situations, pour effectuer une inférence, votre graphe n'a pas besoin de certaines opérations spécifiques à l'entraînement. Ces opérations peuvent inclure les variables de l'optimiseur, les tenseurs de planification du taux d'apprentissage, les opérations de pré-traitement supplémentaires, et ainsi de suite.

De plus, vous pourriez vouloir servir une version quantifiée d'un graphe pour un déploiement mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WHJcm2nqCaCXk6XVgU_b-g.png)

Dans ce contexte, SavedModel vous permet de sauvegarder des graphes avec différentes configurations. Dans notre exemple, nous aurions trois graphes différents avec des tags correspondants tels que "training", "inference" et "mobile". De plus, ces trois graphes partageraient tous le même ensemble de variables — ce qui souligne l'efficacité de la mémoire.

Il n'y a pas si longtemps, lorsque nous voulions déployer des modèles TF sur des appareils mobiles, nous devions connaître les noms des tenseurs d'entrée et de sortie pour alimenter et obtenir des données depuis le modèle. Ce besoin forçait les programmeurs à rechercher le tenseur dont ils avaient besoin parmi tous les tenseurs du graphe. Si les tenseurs n'étaient pas correctement nommés, la tâche pouvait être très fastidieuse.

Pour faciliter les choses, SavedModel offre un support pour les [SignatureDefs](https://www.tensorflow.org/serving/signature_defs). En résumé, les SignatureDefs définissent la signature d'un calcul pris en charge par TensorFlow. Ils déterminent les tenseurs d'entrée et de sortie appropriés pour un graphe de calcul. En termes simples, avec ces signatures, vous pouvez spécifier les nœuds exacts à utiliser pour l'entrée et la sortie.

Pour utiliser ses APIs de service intégrées, TF Serving nécessite que les modèles incluent une ou plusieurs SignatureDefs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0yHcL0JGeLXJqhQo0see1w.png)

Pour créer de telles signatures, nous devons fournir des définitions pour les entrées, les sorties et le nom de la méthode souhaitée. **Inputs** et **Outputs** représentent un mappage de chaîne à des objets TensorInfo (plus sur cela plus tard). Ici, nous définissons les tenseurs par défaut pour alimenter et recevoir des données depuis un graphe. Le paramètre _method_name_ cible l'une des APIs de service de haut niveau de TF.

Actuellement, il existe trois APIs de service : Classification, Predict et Regression. Chaque définition de signature correspond à une API RPC spécifique. La SignatureDef de Classification est utilisée pour l'API RPC Classify. La SignatureDef Predict est utilisée pour l'API RPC Predict, et ainsi de suite.

Pour la signature de Classification, il doit y avoir un tenseur d'entrée (pour recevoir des données) et au moins l'un des deux tenseurs de sortie possibles : classes et/ou scores. La SignatureDef de Regression nécessite exactement un tenseur pour l'entrée et un autre pour la sortie. Enfin, la signature Predict permet un nombre dynamique de tenseurs d'entrée et de sortie.

De plus, SavedModel supporte le stockage des assets pour les cas où l'initialisation des ops dépend de fichiers externes. Il dispose également de mécanismes pour effacer les appareils avant de créer le SavedModel.

Maintenant, voyons comment nous pouvons le faire en pratique.

### Configuration de l'environnement

Avant de commencer, clonez [cette implémentation TensorFlow **DeepLab-v3**](https://github.com/sthalles/deeplab_v3) depuis Github.

DeepLab est le meilleur ConvNet de segmentation sémantique de Google. Basiquement, le réseau prend une image en entrée et produit une image de type masque qui sépare certains objets de l'arrière-plan.

Cette version a été entraînée sur le jeu de données de segmentation [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). Ainsi, il peut segmenter et reconnaître jusqu'à 20 classes. Si vous voulez en savoir plus sur la segmentation sémantique et DeepLab-v3, consultez [Diving into Deep Convolutional Semantic Segmentation Networks and Deeplab_V3](https://medium.freecodecamp.org/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df).

Tous les fichiers liés au service se trouvent dans : [./deeplab_v3/serving/](https://github.com/sthalles/deeplab_v3/tree/master/serving). Là, vous trouverez deux fichiers importants : [deeplab_saved_model.py](https://github.com/sthalles/deeplab_v3/blob/master/serving/deeplab_saved_model.py) et [deeplab_client.ipynb](https://github.com/sthalles/deeplab_v3/blob/master/serving/deeplab_client.ipynb)

Avant d'aller plus loin, assurez-vous de télécharger le modèle pré-entraîné Deeplab-v3. Rendez-vous sur le dépôt GitHub ci-dessus, cliquez sur le lien des checkpoints et téléchargez le dossier nommé **16645/**.

À la fin, vous devriez avoir un dossier nommé **tboard_logs/** avec le dossier **16645/** placé à l'intérieur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ScNnPqBm0IgcyyB6QAvkeA.png)

Maintenant, nous devons créer deux environnements virtuels Python. Un pour Python 3 et un autre pour Python 2. Pour chaque environnement, assurez-vous d'installer les dépendances nécessaires. Vous pouvez les trouver dans les fichiers [serving_requirements.txt](https://github.com/sthalles/deeplab_v3/blob/master/serving/serving_requirements.txt) et [client_requirements.txt](https://github.com/sthalles/deeplab_v3/blob/master/serving/client_requirements.txt).

Nous avons besoin de deux environnements Python car notre modèle, DeepLab-v3, a été développé sous Python 3. Cependant, l'API Python de TensorFlow Serving n'est publiée que pour Python 2. Par conséquent, pour exporter le modèle et exécuter TF serving, nous utilisons l'environnement Python 3. Pour exécuter le code client en utilisant l'API Python de TF Serving, nous utilisons le package PIP (disponible uniquement pour Python 2).

Notez que vous pouvez vous passer de l'environnement Python 2 en utilisant les APIs de Serving depuis bazel. Consultez [l'installation de TF Serving](https://www.tensorflow.org/serving/setup#aptget) pour plus de détails.

Avec cette étape terminée, commençons par ce qui compte vraiment.

### Comment faire

Pour utiliser SavedModel, TensorFlow fournit une classe utilitaire de haut niveau facile à utiliser appelée [SavedModelBuilder](https://www.tensorflow.org/api_docs/python/tf/saved_model/builder/SavedModelBuilder). La classe SavedModelBuilder fournit des fonctionnalités pour sauvegarder plusieurs méta-graphes, des variables associées et des assets.

Passons par un exemple concret de la façon d'exporter un modèle CNN de segmentation profonde pour le service.

Comme mentionné ci-dessus, pour exporter le modèle, nous utilisons la classe SavedModelBuilder. Elle générera un fichier de protocole buffer SavedModel ainsi que les variables et les assets du modèle (si nécessaire).

Décortiquons le code.

Le SavedModelBuilder reçoit (en entrée) le répertoire où sauvegarder les données du modèle. Ici, la variable _export_path_ est la concaténation de _export_path_base_ et de _model_version_. Par conséquent, différentes versions de modèle seront sauvegardées dans des répertoires séparés à l'intérieur du dossier _export_path_base_.

Supposons que nous avons une version de base de notre modèle en production, mais que nous voulons déployer une nouvelle version de celui-ci. Nous avons amélioré la précision de notre modèle et voulons offrir cette nouvelle version à nos clients.

Pour exporter une version différente du même graphe, nous pouvons simplement définir _FLAGS.model_version_ à une valeur entière plus élevée. Ensuite, un dossier différent (contenant la nouvelle version de notre modèle) sera créé à l'intérieur du dossier _export_path_base_.

Maintenant, nous devons spécifier les tenseurs d'entrée et de sortie de notre modèle. Pour cela, nous utilisons [SignatureDefs](https://www.tensorflow.org/serving/signature_defs). Les signatures définissent le type de modèle que nous voulons exporter. Elles fournissent un mappage de chaînes (noms logiques de tenseurs) à des objets [TensorInfo](https://www.tensorflow.org/api_docs/python/tf/TensorInfo). L'idée est que, au lieu de référencer les noms réels des tenseurs pour l'entrée/sortie, les clients peuvent se référer aux noms logiques définis par les signatures.

Pour servir un CNN de segmentation sémantique, nous allons créer une **signature Predict**. Notez que la fonction _build_signature_def()_ prend le mappage des tenseurs d'entrée et de sortie ainsi que l'API souhaitée.

Une SignatureDef nécessite la spécification de : entrées, sorties et nom de la méthode. Notez que nous attendons trois valeurs pour _inputs_ — une image, et deux tenseurs supplémentaires spécifiant ses dimensions (hauteur et largeur). Pour les _outputs_, nous avons défini un seul résultat — le masque de sortie de segmentation.

Notez que les chaînes 'image', 'height', 'width' et 'segmentation_map' ne sont pas des tenseurs. Au lieu de cela, ce sont des noms logiques qui font référence aux tenseurs réels _input_tensor_, _image_height_tensor_ et _image_width_tensor_. Ainsi, ils peuvent être n'importe quelle chaîne unique que vous aimez.

De plus, les mappages dans les SignatureDefs se rapportent à des objets protobuf TensorInfo, et non à des tenseurs réels. Pour créer des objets TensorInfo, nous utilisons la fonction utilitaire : [_tf.saved_model.utils.build_tensor_info(tensor)_](https://www.tensorflow.org/api_docs/python/tf/saved_model/utils/build_tensor_info).

C'est tout. Maintenant, nous appelons la fonction _add_meta_graph_and_variables()_ pour construire l'objet de protocole buffer SavedModel. Ensuite, nous exécutons la méthode _save()_ et elle persistera un instantané de notre modèle sur le disque contenant les variables et les assets du modèle.

Nous pouvons maintenant exécuter [deeplab_saved_model.py](https://github.com/sthalles/deeplab_v3/blob/master/serving/deeplab_saved_model.py) pour exporter notre modèle.

Si tout s'est bien passé, vous verrez le dossier **./serving/versions/1**. Notez que le '1' représente la version actuelle du modèle. À l'intérieur de chaque sous-répertoire de version, vous verrez les fichiers suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pDEnXV2Ewsrlz6bSWJBTyQ.png)

* _saved_model.pb_ ou _saved_model.pbtxt_. Il s'agit du fichier SavedModel sérialisé. Il inclut une ou plusieurs définitions de graphe du modèle, ainsi que les définitions de signature.
* Variables. Ce dossier contient les variables sérialisées des graphes.

Maintenant, nous sommes prêts à lancer notre serveur de modèle. Pour cela, exécutez :

```
$ tensorflow_model_server --port=9000 --model_name=deeplab --model_base_path=<chemin/complet/vers/serving/versions/>
```

Le _model_base_path_ fait référence à l'endroit où le modèle exporté a été sauvegardé. De plus, nous ne spécifions pas le dossier de version dans le chemin. Le contrôle de version du modèle est géré par TF Serving.

### Génération des requêtes client

Le code client est très simple. Jetez un coup d'œil à [deeplab_client.ipynb](https://github.com/sthalles/deeplab_v3/blob/master/serving/deeplab_client.ipynb).

Tout d'abord, nous lisons l'image que nous voulons envoyer au serveur et la convertissons au bon format.

Ensuite, nous créons un stub gRPC. Le stub nous permet d'appeler les méthodes du serveur distant. Pour cela, nous instancions la classe _beta_create_PredictionService_stub_ du module _prediction_service_pb2_. À ce stade, le stub contient la logique nécessaire pour appeler les procédures distantes (du serveur) comme si elles étaient locales.

Maintenant, nous devons créer et définir l'objet de requête. Puisque notre serveur implémente l'API Predict de TensorFlow, nous devons analyser une requête Predict. Pour émettre une requête Predict, nous instancions d'abord la classe **PredictRequest** du module _predict_pb2_. Nous devons également spécifier les paramètres _model_spec.name_ et _model_spec.signature_name_. Le paramètre _name_ est l'argument 'model_name' que nous avons défini lors du lancement du serveur. Et le _signature_name_ fait référence au nom logique attribué au paramètre _signature_def_map()_ de la routine _add_meta_graph()_.

Ensuite, nous devons fournir les données d'entrée comme défini dans la signature du serveur. Rappelez-vous que, dans le serveur, nous avons défini une API Predict pour attendre une image ainsi que deux scalaires (la hauteur et la largeur de l'image). Pour alimenter les données d'entrée dans l'objet de requête, TensorFlow fournit l'utilitaire _tf.make_tensor_proto()_. Cette méthode crée un objet TensorProto à partir d'un objet numpy/Python. Nous pouvons l'utiliser pour alimenter l'image et ses dimensions dans l'objet de requête.

Il semble que nous soyons prêts à appeler le serveur. Pour cela, nous appelons la méthode _Predict()_ (en utilisant le stub) et passons l'objet de requête comme argument.

Pour les requêtes qui retournent une seule réponse, gRPC supporte à la fois les appels synchrones et asynchrones. Ainsi, si vous voulez faire un travail pendant que la requête est en cours de traitement, nous pourrions appeler _Predict.future()_ au lieu de _Predict()_.

Maintenant, nous pouvons récupérer et profiter des résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tVrioWYLRyxTA-MXYoMCdA.png)

J'espère que vous avez aimé cet article. Merci pour votre lecture !

### Si vous voulez en savoir plus, consultez :

[**Comment entraîner votre propre FaceID ConvNet en utilisant l'exécution Eager de TensorFlow**](https://medium.freecodecamp.org/how-to-train-your-own-faceid-cnn-using-tensorflow-eager-execution-6905afe4fd5a)  
[_Les visages sont partout — des photos et vidéos sur les sites de réseaux sociaux, aux applications de sécurité grand public comme le..._medium.freecodecamp.org](https://medium.freecodecamp.org/how-to-train-your-own-faceid-cnn-using-tensorflow-eager-execution-6905afe4fd5a)[**Plonger dans les réseaux de segmentation sémantique convolutionnelle profonde et Deeplab_V3**](https://medium.freecodecamp.org/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df)  
[_Les réseaux de neurones convolutionnels profonds (DCNN) ont atteint un succès remarquable dans diverses applications de vision par ordinateur..._medium.freecodecamp.org](https://medium.freecodecamp.org/diving-into-deep-convolutional-semantic-segmentation-networks-and-deeplab-v3-4f094fa387df)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RzOHqzrJEIrB5ZY0nJAcvg.gif)