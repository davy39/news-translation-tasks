---
title: Machine Learning as a Service avec TensorFlow
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T03:25:09.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-as-a-service-with-tensorflow-9929e9ce3801
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bhqON7cBLFo-TIrOyoDc1g.jpeg
tags:
- name: Docker
  slug: docker
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Machine Learning as a Service avec TensorFlow
seo_desc: 'By Kirill Dubovikov

  Imagine this: you’ve gotten aboard the AI Hype Train and decided to develop an app
  which will analyze the effectiveness of different chopstick types. To monetize this
  mind-blowing AI application and impress VC’s, we’ll need to ope...'
---

Par Kirill Dubovikov

Imaginez ceci : vous êtes monté à bord du train de l'hype de l'IA et avez décidé de développer une application qui analysera l'efficacité de différents types de baguettes. Pour monétiser cette application d'IA incroyable et impressionner les VC, nous devons l'ouvrir au monde. Et il vaut mieux qu'elle soit scalable car tout le monde voudra l'utiliser.

Comme point de départ, nous utiliserons ce jeu de données, qui contient des mesures de l'efficacité de la prise de nourriture de divers individus avec des baguettes de différentes longueurs.

#### Architecture

En tant que scientifiques des données et également ingénieurs logiciels responsables, nous allons d'abord esquisser notre architecture. Tout d'abord, nous devons décider comment nous allons accéder à notre modèle déployé pour faire des prédictions. Pour TensorFlow, un choix naïf serait d'utiliser [TensorFlow Serving](https://www.tensorflow.org/serving/). Ce framework vous permet de déployer des modèles TensorFlow entraînés, prend en charge le versionnage des modèles et utilise g[RPC](https://grpc.io) sous le capot.

Le principal inconvénient de gRPC est qu'il n'est pas très convivial pour le public par rapport aux services REST, par exemple. Toute personne avec un outil minimal peut appeler un service REST et obtenir rapidement un résultat. Mais lorsque vous utilisez gRPC, vous devez d'abord générer du code client à partir de fichiers proto en utilisant des utilitaires spéciaux, puis écrire le client dans votre langage de programmation préféré.

TensorFlow Serving simplifie beaucoup de choses dans ce pipeline, mais ce n'est toujours pas le framework le plus facile pour consommer une API côté client. Envisagez TF Serving si vous avez besoin d'une API ultra-rapide, fiable et strictement typée qui sera utilisée dans votre application (par exemple, comme service backend pour une application web ou mobile).

Nous devrons également satisfaire les exigences non fonctionnelles de notre système. Si de nombreux utilisateurs veulent connaître leur niveau d'efficacité avec les baguettes, nous aurons besoin que le système soit tolérant aux pannes et scalable. De plus, l'équipe UI devra déployer leur application web chopstick'o'meter quelque part aussi. Et nous aurons besoin de ressources pour prototyper de nouveaux modèles de machine learning, éventuellement dans un Jupyter Lab avec beaucoup de puissance de calcul derrière. L'une des meilleures réponses à ces questions est d'utiliser [Kubernetes](https://kubernetes.io).

> [Kubernetes](https://kubernetes.io/) est un système open-source pour automatiser le déploiement, la mise à l'échelle et la gestion des applications conteneurisées.

Avec Kubernetes en place, avec des connaissances et un peu de temps, nous pouvons créer une solution cloud PaaS interne scalable qui fournit l'infrastructure et le logiciel pour le développement complet de projets de science des données. Si vous n'êtes pas familier avec Kubernetes, je vous suggère de regarder ceci :

Kubernetes fonctionne sur la technologie [Docker](http://docker.com), donc si vous n'êtes pas familier avec celle-ci, il peut être bon de lire le [tutoriel officiel](https://docs.docker.com/get-started/) d'abord.

En résumé, c'est un sujet très riche qui mérite plusieurs livres pour être couvert complètement, donc ici nous nous concentrerons sur une seule partie : le passage des modèles de machine learning en production.

#### Considérations

Oui, ce jeu de données est petit. Et oui, appliquer le deep learning n'est peut-être pas la meilleure idée ici. Gardez simplement à l'esprit que nous sommes ici pour apprendre, et ce jeu de données est certainement amusant. La partie modélisation de ce tutoriel manquera de qualité, car l'accent principal est mis sur le processus de déploiement du modèle.

De plus, nous devons impressionner nos VC, donc le deep learning est un must ! :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gejeBAG1aRDFWOL8Uxz3dg.png)
_Image [source](https://xkcd.com/1838/" rel="noopener" target="_blank" title=")._

#### Code

Tout le code et les fichiers de configuration utilisés dans cet article sont disponibles dans un [dépôt GitHub compagnon](https://github.com/kdubovikov/chopstick-serving).

#### Entraînement du classificateur Deep Chopstick

Tout d'abord, nous devons choisir un framework de machine learning à utiliser. Comme cet article est destiné à démontrer les capacités de TensorFlow Serving, nous choisirons TensorFlow.

Comme vous le savez peut-être, il existe deux façons d'entraîner notre classificateur : en utilisant TensorFlow et en utilisant l'API [Estimator](https://www.tensorflow.org/versions/master/programmers_guide/estimators) de TensorFlow. L'API Estimator est une tentative de présenter une interface unifiée pour les modèles de deep learning de la manière dont scikit-learn le fait pour un ensemble de modèles ML classiques. Pour cette tâche, nous pouvons utiliser `tf.estimator.LinearClassifier` pour implémenter rapidement la régression logistique et exporter le modèle après l'entraînement.

L'autre façon de le faire est d'utiliser TensorFlow pour entraîner et exporter un classificateur :

#### Configuration de TensorFlow Serving

![Image](https://cdn-media-1.freecodecamp.org/images/1*nTik7YnlL8avMLiRm2iQBQ.jpeg)
_Serving, hein ?_

Alors, vous avez un modèle de deep learning génial avec TensorFlow et vous êtes impatient de le mettre en production ? Il est maintenant temps de nous pencher sur TensorFlow Serving.

TensorFlow Serving est basé sur gRPC — une bibliothèque d'appel de procédure à distance rapide qui utilise un autre projet Google sous le capot — Protocol Buffers.

Protocol Buffers est un framework de sérialisation qui vous permet de transformer des objets de la mémoire en un format binaire efficace adapté à la transmission sur le réseau.

Pour résumer, gRPC est un framework qui permet des appels de fonctions à distance sur le réseau. Il utilise Protocol Buffers pour sérialiser et désérialiser les données.

Les principaux composants de TensorFlow Serving sont :

* **Servable** — il s'agit essentiellement d'une version de votre modèle entraîné exporté dans un format adapté pour que TF Serving le charge
* **Loader** — composant TF Serving qui, par coïncidence, charge les servables en mémoire
* **Manager** — implémente les opérations de cycle de vie des servables. Il contrôle la naissance des servables (chargement), leur longue vie (service) et leur mort (déchargement)
* **Core** — fait fonctionner tous les composants ensemble (la documentation officielle est un peu vague sur ce qu'est réellement le core, mais vous pouvez toujours [regarder le code source](https://github.com/tensorflow/serving/blob/f34e79a1ef0315d0f2d86eb0751a4c3700f8a433/tensorflow_serving/model_servers/server_core.h) pour comprendre ce qu'il fait)

Vous pouvez lire une vue d'ensemble plus approfondie de l'architecture de TF Serving dans la [documentation officielle](https://www.tensorflow.org/serving/architecture_overview).

Pour mettre en place un service basé sur TF Serving, vous devrez :

1. Exporter le modèle dans un format compatible avec TensorFlow Serving. En d'autres termes, créer un Servable.
2. Installer ou compiler TensorFlow Serving
3. Exécuter TensorFlow Serving et charger la dernière version du modèle exporté (servable)

La [configuration de TensorFlow Serving](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/setup.md) peut être effectuée de plusieurs manières :

* Construction à partir de la source. Cela nécessite d'installer Bazel et de compléter un long processus de compilation
* Utilisation d'un package binaire pré-compilé. TF Serving est disponible sous forme de package deb.

Pour automatiser ce processus et simplifier l'installation ultérieure sur Kubernetes, nous avons créé un simple Dockerfile pour vous. [Veuillez cloner le dépôt de l'article et suivre les instructions dans le fichier README.md](https://github.com/kdubovikov/chopstick-serving) pour construire l'image Docker de TensorFlow Serving :

```
 make build_image
```

Cette image a TensorFlow Serving et toutes les dépendances préinstallées. Par défaut, elle charge les modèles depuis le répertoire `/models` à l'intérieur du conteneur Docker.

#### Exécution d'un service de prédiction

Pour exécuter notre service à l'intérieur de l'image TF Serving fraîchement construite et prête à l'emploi, assurez-vous de d'abord entraîner et exporter le modèle (ou si vous utilisez un dépôt compagnon, exécutez simplement la commande `make train_classifier`).

Après que le classificateur soit entraîné et exporté, vous pouvez exécuter le conteneur de service en utilisant le raccourci `make run_server` ou en utilisant la commande suivante :

```
 docker run -p8500:8500 -d --rm -v /path/to/exported/model:/models tfserve_bin
```

* `-p` mappe les ports du conteneur vers la machine locale
* `-d` exécute le conteneur en mode démon (arrière-plan)
* `--rm` supprime le conteneur après son arrêt
* `-v` mappe le répertoire local vers un répertoire à l'intérieur du conteneur en cours d'exécution. De cette façon, nous passons nos modèles exportés à l'instance TF Serving en cours d'exécution à l'intérieur du conteneur

#### Appel des services de modèle depuis le côté client

Pour appeler nos services, nous utiliserons les packages Python `grpc` et `tensorflow-serving-api`. Veuillez noter que ce package est actuellement disponible uniquement pour Python 2, vous devriez donc avoir un environnement virtuel séparé pour le client TF Serving.

Pour utiliser cette API avec Python 3, vous devrez soit utiliser un package non officiel depuis [ici](https://github.com/illagrenan/tensorflow-serving-api-python3), puis télécharger et décompresser le package manuellement, soit construire TensorFlow Serving à partir de la source (voir la [documentation](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/setup.md#tensorflow-serving-python-api-pip-package)). Des exemples de clients pour l'API Estimator et TensorFlow sont ci-dessous :

#### Passage en production avec Kubernetes

Si vous n'avez pas de cluster Kubernetes disponible, vous pouvez en créer un pour des expériences locales en utilisant [minikube](https://github.com/kubernetes/minikube), ou vous pouvez facilement déployer un vrai cluster en utilisant [kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/).

Nous allons opter pour l'option minikube dans cet article. Une fois que vous l'avez installé (`brew cask install minikube` sur Mac), nous pouvons démarrer un cluster local et partager son environnement Docker avec notre machine :

```
 minikube start...
 eval $(minikube docker-env)
```

Après cela, nous pourrons construire notre image et la mettre à l'intérieur du cluster en utilisant

```
 make build_image
```

Une option plus mature serait d'utiliser le registre Docker interne et d'y pousser l'image construite localement, mais nous allons laisser cela hors de portée pour être plus concis.

Après avoir construit notre image et l'avoir rendue disponible pour l'instance Minikube, nous devons déployer notre serveur de modèle. Pour tirer parti des fonctionnalités d'équilibrage de charge et de haute disponibilité de Kubernetes, nous allons créer un Deployment qui mettra à l'échelle notre serveur de modèle à trois instances et les maintiendra également surveillées et en cours d'exécution. Vous pouvez en lire plus sur les déploiements Kubernetes [ici](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

Tous les objets Kubernetes peuvent être configurés dans divers formats de texte, puis passés à la commande `kubectl apply -f file_name` pour (meh) appliquer notre configuration au cluster. Voici notre configuration de déploiement du serveur de baguettes :

Appliquons ce déploiement en utilisant la commande `kubectl apply -f chopstick_deployment.yml`. Après un certain temps, vous verrez tous les composants en cours d'exécution :

```
 kubectl get all
NAME                          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/chopstick-classifier   3         3         3            3           1d
```

```
NAME                                 DESIRED   CURRENT   READY     AGE
rs/chopstick-classifier-745cbdf8cd   3         3         3         1d
```

```
NAME                          AGE
deploy/chopstick-classifier   1d
```

```
NAME                                 AGE
rs/chopstick-classifier-745cbdf8cd   1d
```

```
NAME                                       READY     STATUS    RESTARTS   AGE
po/chopstick-classifier-745cbdf8cd-5gx2g   1/1       Running   0          1d
po/chopstick-classifier-745cbdf8cd-dxq7g   1/1       Running   0          1d
po/chopstick-classifier-745cbdf8cd-pktzr   1/1       Running   0          1d
```

Remarquez que, sur la base de la configuration du déploiement, Kubernetes a créé pour nous :

* Un déploiement
* Un [Replica Set](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
* Trois pods exécutant notre image chopstick-classifier

Maintenant, nous voulons appeler notre nouveau service brillant. Pour que cela se produise, nous devons d'abord l'exposer au monde extérieur. Dans Kubernetes, cela peut être fait en définissant des [Services](https://kubernetes.io/docs/concepts/services-networking/service/). Voici la définition du Service pour notre modèle :

Comme toujours, nous pouvons l'installer en utilisant `kubectl apply -f chopstick_service.yml`. Kubernetes attribuera un port externe à notre LoadBalancer, et nous pouvons le voir en exécutant

```
 kubectl get svc
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
chopstick-classifier   LoadBalancer   10.104.213.253   <pending>     8500:32372/TCP   1d
kubernetes             ClusterIP      10.96.0.1        <none>        443/TCP          1d
```

Comme vous pouvez le voir, notre `chopstick-classifier` est disponible via le port `32372` dans mon cas. Il peut être différent sur votre machine, alors n'oubliez pas de vérifier. Une manière pratique d'obtenir l'IP et le port pour tout Service lors de l'utilisation de Minikube est d'exécuter la commande suivante :

```
 minikube service chopstick-classifier --url
http://192.168.99.100:32372
```

#### Inférence

Enfin, nous sommes en mesure d'appeler notre service !

```
python tf_api/client.py 192.168.99.100:32372 10 10.0
Sending request
outputs {  key: "classes_prob"  value {    dtype: DT_FLOAT    tensor_shape {      dim {        size: 1      }      dim {        size: 3      }    }    float_val: 3.98174306027e-11    float_val: 1.0    float_val: 1.83699980923e-18  }}
```

#### Avant de passer en production réelle

![Image](https://cdn-media-1.freecodecamp.org/images/1*qYsGyocCbVbbrbWY15CULA.jpeg)

Comme cet article est principalement destiné à des fins éducatives et comporte certaines simplifications pour des raisons de clarté, il y a plusieurs points importants à considérer avant de passer en production :

* Utilisez un service mesh comme [linkerd.io](https://linkerd.io). L'accès aux services à partir de ports de nœuds générés aléatoirement n'est pas recommandé en production. En plus, linkerd ajoutera beaucoup plus de valeur à votre infrastructure de production : surveillance, découverte de services, équilibrage de charge à haute vitesse, et plus encore
* Utilisez Python 3 partout, car il n'y a vraiment aucune raison d'utiliser Python 2 maintenant
* Appliquez le Deep Learning avec sagesse. Même s'il s'agit d'un framework très général, spectaculaire et largement applicable, le deep learning n'est pas le seul outil à la disposition d'un scientifique des données. Ce n'est pas non plus une solution miracle qui résout n'importe quel problème. Le machine learning a beaucoup plus à offrir. Si vous avez des données relationnelles/tabulaires, des petits jeux de données, des restrictions strictes sur les ressources de calcul, ou le temps d'entraînement ou l'interprétabilité du modèle, envisagez d'utiliser d'autres algorithmes et approches.
* Contactez-nous si vous avez besoin d'aide pour résoudre des défis de machine learning : datalab@cinimex.ru