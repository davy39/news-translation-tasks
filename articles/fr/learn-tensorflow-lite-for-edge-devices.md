---
title: Apprendre TensorFlow Lite pour les appareils en périphérie
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-19T16:58:53.000Z'
originalURL: https://freecodecamp.org/news/learn-tensorflow-lite-for-edge-devices
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/tensoflowlite2.png
tags:
- name: TensorFlow
  slug: tensorflow
- name: youtube
  slug: youtube
seo_title: Apprendre TensorFlow Lite pour les appareils en périphérie
seo_desc: 'TensorFlow Lite is an open source deep learning framework that can be used
  on small devices.

  We just published a TensorFlow Lite course on the freeCodeCamp.org YouTube channel.

  Bhavesh Bhatt created this course. Bhavesh has created many courses on hi...'
---

TensorFlow Lite est un framework d'apprentissage profond open source qui peut être utilisé sur de petits appareils.

Nous venons de publier un cours sur TensorFlow Lite sur la chaîne YouTube freeCodeCamp.org.

Bhavesh Bhatt a créé ce cours. Bhavesh a créé de nombreux cours sur sa propre chaîne et est un excellent enseignant.

TensorFlow Lite est développé par Google et est utilisé pour entraîner des modèles de Machine Learning sur des appareils mobiles, IoT (Internet des Objets) et embarqués.

Lorsque vous utilisez TensorFlow Lite, tout le machine learning se fait à l'intérieur de l'appareil. Cela peut éviter d'envoyer des données en va-et-vient avec un serveur.

Voici les sujets abordés dans ce cours :

* Pourquoi avons-nous besoin de TensorFlow Lite ?
* Qu'est-ce que l'Edge Computing ?
* Pourquoi l'Edge Computing gagne-t-il en popularité ?
* Les défis du déploiement de modèles sur les appareils en périphérie
* Qu'est-ce que TensorFlow Lite ou TFLite ?
* Le flux de travail de TensorFlow Lite
* Créer un modèle TensorFlow ou Keras
* Convertir un modèle TensorFlow ou Keras en TFLite
* Valider les performances du modèle TFLite
* Qu'est-ce que la quantification ?
* Compresser davantage le modèle TFLite
* Compresser encore plus le modèle TFLite
* Valider les performances du modèle TFLite le plus compressé

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/OJnaBhCixng) (1 heure de visionnage).

%[https://youtu.be/OJnaBhCixng]

## Transcription

(générée automatiquement)

TensorFlow Lite vous permet de faire du machine learning sur de petits appareils.

Bhavesh est un instructeur expérimenté et il vous enseignera tout sur TensorFlow Lite dans ce cours.

Bonjour à tous.

Dans ce tutoriel, vous apprendrez les bases de TensorFlow Lite, et comment TensorFlow Lite peut vous aider à créer des modèles vraiment efficaces que vous pouvez déployer sur des appareils en périphérie.

Alors sans perdre plus de temps, commençons le tutoriel.

Commençons la discussion d'aujourd'hui sur le vol avec une petite histoire.

J'ai un ami dont le nom est John.

JOHN aime vraiment voyager dans différents endroits.

L'une de ses applications préférées est Google Lens.

Chaque fois qu'il visite un nouveau pays, il sort son téléphone portable, prend une photographie du monument qui est devant lui.

Et Google lui dit essentiellement quel monument c'est.

Alors maintenant, juste par la fascination pure de l'outil, John avance et crée son propre réseau de neurones pour détecter les monuments.

Il passe par un processus rigoureux de collecte de données, d'étiquetage de données, de nettoyage de données.

Et finalement, il crée un modèle de machine learning qui peut dire à John quel monument c'est.

Donc tout semble bien, il est capable d'atteindre un score de précision très élevé également.

Maintenant, le seul défi qu'il a est de savoir où il doit déployer le modèle qui est créé.

Donc techniquement, il a deux options.

La première option qu'il explore est le cloud computing.

Il prend son modèle entraîné et le déploie sur le Cloud.

Il expose l'API qu'il a créée.

Et essentiellement, il crée une application Android qui interroge l'API et récupère le résultat une fois qu'il a passé une image.

Maintenant, l'un des principaux défis qu'il a vus lorsqu'il a créé la solution est la latence du réseau.

Donc les images qui sont capturées généralement par les téléphones portables aujourd'hui, varient entre trois et 10 Mo.

Donc transporter de tels fichiers volumineux prend beaucoup de temps dans l'ensemble du processus de prédiction.

Le deuxième élément qui ajoute de la complexité à l'ensemble de la solution est le coût.

Le réseau de neurones que John a créé nécessite des ressources, une ressource de stockage où il peut sauvegarder les poids du modèle, et une ressource de calcul pour faire une inférence, l'ensemble du projet devient une affaire coûteuse pour John.

Que fait-il ensuite, il crée une application Android.

Et il trouve un moyen de faire une inférence sur Android en utilisant ce modèle énorme qu'il a créé.

Donc John fait maintenant face à un nouveau problème.

Le problème est que le modèle est vraiment énorme.

Et le téléphone portable n'est pas très capable de stocker et de traiter un modèle aussi grand.

Donc maintenant John est vraiment confus.

Il a essayé différentes techniques pour faire fonctionner cela.

Mais rien ne résout ce problème.

Eh bien, c'est ici que TF Lite entre en jeu.

Avant de sauter et de discuter du vol, je voulais éclairer en termes de ce que sont les appareils en périphérie.

Donc les appareils en périphérie sont vos téléphones portables normaux que vous utilisez.

Donc si vous prévoyez de créer des applications incroyables basées sur TensorFlow, alors essentiellement l'une des principales plateformes que vous pouvez utiliser est vos téléphones portables, que ce soit un téléphone portable Android ou un téléphone portable alimenté par iOS, tout fonctionne.

Les autres pièces de matériel que vous pouvez classer dans les appareils en périphérie ou les microcontrôleurs.

Donc il y a des applications incroyables qui ont été construites en utilisant une très petite puissance de calcul.

Et tout cela est grâce aux microcontrôleurs.

Étant donné comment récemment, les appareils variables que vous aviez essentiellement ont augmenté leur puissance de calcul en utilisant un CPU plus rapide, vous pouvez également mettre vos appareils portables tels que vos montres intelligentes dans la catégorie de l'informatique en périphérie.

Maintenant, laissez-moi avancer et vous donner une définition formelle de l'informatique en périphérie.

Donc l'informatique en périphérie est essentiellement la pratique de déplacer les ressources de calcul et de stockage plus près de l'emplacement où elles sont nécessaires.

C'est là que vos appareils en périphérie entreraient en jeu.

Maintenant, si vous vous en souvenez, John avait deux options pour déployer le modèle.

La première option était de déployer le modèle sur le Cloud.

Beaucoup d'entre vous auraient l'impression qu'un modèle de machine learning fonctionnant sur le serveur en utilisant un grand GPU est beaucoup plus performant par rapport à l'exécuter sur l'appareil lui-même.

Eh bien, la vérité est que les appareils en périphérie sont devenus une plateforme importante pour le machine learning.

Pourquoi gagne-t-il autant en popularité que vous devez essentiellement exécuter vos modèles de machine learning sur les appareils en périphérie ? Eh bien, laissez-moi partager les détails un à un.

La première et principale raison pour laquelle l'informatique en périphérie dans son ensemble gagne en popularité est à cause de la latence.

Les cas d'utilisation qui nécessitent une vitesse en temps réel, nécessitent définitivement des modèles pour fonctionner sur l'appareil.

Par exemple, vous pourriez être en mesure de réduire la latence d'inférence de resnet 50, de 30 millisecondes à 20 millisecondes.

Mais la latence du réseau peut aller jusqu'à plusieurs secondes.

Donc, cela dépend essentiellement de l'endroit où votre modèle est déployé.

Où attendez-vous l'API ?

Donc si vous prenez en compte tous ces facteurs, alors déployer un modèle sur le serveur ne serait pas la meilleure situation possible lorsque vous voulez des inférences en temps quasi réel, ou exactement en temps réel également.

La deuxième raison pour laquelle la création de modèles de machine learning sur des appareils en périphérie est importante est à cause du réseau et de l'activité.

Donc si vous revenez à notre exemple précédent, où John voulait créer sa propre version de Google Lens pour détecter les monuments, s'il se rend dans un pays où il y a peu ou pas de connectivité, c'est ici que la création d'un modèle qui réside sur l'appareil serait beaucoup mieux par rapport au déploiement sur le serveur, car il y a cette dépendance supplémentaire au réseau qui entre en jeu.

La troisième raison pour laquelle il est très important pour vous de créer des modèles de machine learning qui fonctionnent sur des appareils en périphérie est la confidentialité des utilisateurs.

Mettre vos modèles de machine learning sur les appareils en périphérie est également attrayant lorsque vous manipulez des données utilisateur sensibles.

Le machine learning sur le cloud signifie que vos systèmes pourraient avoir à envoyer des données utilisateur sur des réseaux, les rendant susceptibles d'être interceptées.

Le cloud computing signifie également que le stockage des données de nombreux utilisateurs au même endroit ou lieu, ce qui signifie qu'une violation de données peut affecter de nombreuses personnes à la fois.

Il devient donc vraiment important de créer des modèles de machine learning qui peuvent fonctionner sur des appareils en périphérie, ce qui peut préserver les données de confidentialité des utilisateurs.

Laissez-moi maintenant avancer et vous montrer quelques exemples de cas d'utilisation du machine learning sur l'appareil.

Le premier que je vous montre maintenant est la fonctionnalité pour essayer divers cosmétiques en utilisant la RA sur YouTube.

L'ensemble de la partie computationnelle que vous voyez ici se fait essentiellement sur l'appareil lui-même.

Maintenant, le deuxième exemple que je veux vous montrer est quelque chose que vous connaissez peut-être déjà, qui est Google Translate.

Google Translate a une fonctionnalité qui vous permet de capturer du texte avec l'appareil photo de votre téléphone et de les traduire en temps réel sans aucune connexion Internet.

Tout cela est essentiellement possible grâce à l'informatique en périphérie, et plus spécifiquement, TF Lite.

Maintenant que vous avez vu les nouvelles applications incroyables que vous pouvez créer à votre tour, vous vous demandez peut-être, la deuxième alternative que John avait prise initialement, c'est-à-dire créer un modèle TensorFlow entier et énorme, puis exécuter les inférences à partir de l'appareil.

Pourquoi cela a-t-il échoué ? Eh bien, pour répondre à cette question, voici quelques-uns des défis que vous pourriez rencontrer lorsque vous créez des modèles chaotiques ou TensorFlow et les déployez directement sur des appareils en périphérie.

Les appareils en périphérie, non seulement restreints aux téléphones mobiles, mais aussi vos microcontrôleurs, ont une puissance de calcul limitée.

Mémoire limitée.

La consommation de la batterie est également un facteur que vous devez prendre en compte, ainsi que la taille de l'application.

Si je considère un simple microcontrôleur, la puissance de traitement n'est pas suffisante pour exécuter des inférences sur un modèle de trois ou quatre Go.

Si je considère la capacité de stockage de la majorité des appareils en périphérie, alors idéalement, vous n'auriez pas beaucoup de stockage que vous pouvez utiliser pour un seul modèle.

Ce sont donc les défis auxquels John a été confronté lorsqu'il a pris la deuxième approche également.

Donc quelle est la solution ? Eh bien, la solution est TensorFlow Lite.

Et donc, TensorFlow Lite est un framework multiplateforme prêt pour la production, permettant de déployer des modèles de machine learning sur des appareils mobiles et des systèmes embarqués.

Et TensorFlow Lite, à ce stade, prend en charge Android, iOS et tout appareil IoT capable d'exécuter Linux.

Donc, essentiellement, si vous avez l'un de ces appareils matériels à portée de main, vous pouvez rapidement créer un modèle TensorFlow, le convertir en un modèle TF Lite équivalent et commencer à utiliser le modèle TF Lite incroyable.

Maintenant, vous pourriez vous demander, quel est exactement le flux de travail pour créer un modèle TF Lite ? Eh bien, regardons cela également.

Donc le flux de travail est assez simple, vous commencez par créer un modèle TensorFlow ou Keras.

Donc dans l'ensemble du processus, vous devrez collecter des données, vous devrez nettoyer les données, pré-traiter les données, puis créer des modèles, itérer sur plusieurs modèles, et en fonction de la métrique que vous poursuivez, si vous cherchez un score de précision plus élevé, alors vous choisirez un modèle qui vous donnera la meilleure précision possible.

Et c'est à peu près tout, vous avez votre modèle TensorFlow prêt.

Maintenant, à partir de ce modèle TensorFlow, vous le convertissez en un modèle TensorFlow Lite.

Donc il y a un changement de format qui se produit.

J'en parlerai davantage au fur et à mesure.

Une fois que vous avez converti votre modèle de TensorFlow en TensorFlow Lite, vous avancez et déployez l'ensemble du modèle TF Lite et exécutez vos inférences sur l'appareil en périphérie.

Lorsque je dis inférences, je veux dire prédictions.

D'accord.

Laissez-moi maintenant expliquer cela à l'aide d'un diagramme de blocs.

Donc, cela représente essentiellement le flux de travail que je viens de mentionner, vous commencez avec votre curiosité de haut niveau pour créer un modèle.

Une fois que vous avez le modèle prêt, vous pouvez essentiellement utiliser un convertisseur TF Lite.

Et le convertisseur prend essentiellement votre fichier de format TensorFlow sauvegardé et le convertit en un fichier de tampon plat.

Je vous donnerai une idée de ce que je veux dire par fichier de tampon plat.

Donc, avançons.

Donc, TensorFlow Lite représente votre modèle dans un format de tampon plat.

Maintenant, le format de tampon plat est une bibliothèque de sérialisation efficace et multiplateforme pour C++, C#, Go, Java, Kotlin, JavaScript, Python, et ainsi de suite.

Il a été initialement créé chez Google pour le développement de jeux et d'autres applications critiques en termes de performance.

Mais lentement, Google a réalisé que vous pouvez utiliser le format de tampon plat pour déployer des modèles sur des appareils en périphérie.

Maintenant, vous pourriez avoir une question évidente, pourquoi ne pas utiliser nos anciens protocoles buffers éprouvés.

Et pourquoi passer à quelque chose de nouveau comme les flatbuffers ? Les protocoles buffers, juste pour vous donner un contexte, tous vos modèles Keras que vous créez, tous vos modèles TensorFlow que vous créez sont essentiellement au format protocole buffer.

Les protocoles buffers sont essentiellement très similaires au format de tampon plat que Google a créé.

La différence majeure est que les flatbuffers n'ont pas besoin d'une étape d'analyse ou de décompression vers une représentation secondaire, avant de pouvoir accéder aux données.

Et le code est également plus volumineux dans le cas des protocoles buffers.

C'est votre cas lorsque vous utilisez TF Lite, nous utilisons un format de tampon plat, et non un format de protocole buffer.

Donc maintenant, avançons.

Jusqu'à présent, nous avons examiné divers aspects de l'informatique en périphérie, nous avons vu comment le déploiement de modèles sur des appareils en périphérie est meilleur par rapport au déploiement sur le Cloud.

Nous avons également examiné ce qu'est TensorFlow Lite, et tout ce qu'il peut prendre en charge à ce stade.

Maintenant, c'est là que les choses deviennent intéressantes lorsque je vous montre à travers le code, comment TF Lite peut réellement compresser la taille de votre modèle sans compromettre la précision.

Donc maintenant, avançons et assistons à la magie de TF Lite.

Maintenant que nous avons compris les bases de TensorFlow Lite et de l'informatique en périphérie, laissez-moi vous montrer la puissance de TensorFlow Lite en utilisant Python.

Donc pour cet exemple, j'utilise Google Colab.

Pour ceux d'entre vous qui ne le savent pas, Google Colab est un environnement en ligne où vous pouvez écrire du code Python, créer des modèles de machine learning et de deep learning, vous pouvez également utiliser des modèles de deep learning auxquels Google vous donne accès pendant une bonne période.

Donc c'est l'interface que j'utiliserai.

Je joindrai le lien vers le dépôt GitHub dans la section description de la vidéo, n'hésitez pas à accéder au code à partir de là.

De plus, à l'intérieur du dépôt GitHub, je vous donnerai également un lien qui peut ouvrir directement un notebook Google Colab.

Avec tout le travail préparatoire fait, laissez-moi maintenant avancer et vous montrer la magie de TensorFlow Lite.

Donc le processus que je vais suivre dans ce tutoriel particulier est le suivant : je vais créer un modèle de deep learning en utilisant TensorFlow/Keras.

Je vais le réduire à un modèle équivalent TF Lite.

Une fois cela accompli, je vous montrerai la différence de taille entre le modèle original et le modèle compressé.

Je vous montrerai des techniques pour continuer à compresser le modèle encore plus sans avoir à compromettre la précision.

Avec cela, laissez-moi créer une instance sur Google Colab en appuyant sur Connecter.

Actuellement, Google alloue de l'espace pour mes calculs.

Si vous prévoyez de répliquer tout ce que je montre dans la vidéo d'aujourd'hui sur votre machine locale, alors vous aurez besoin de certaines installations également.

Étant donné que je travaille avec Google Colab, toutes les dépendances dont j'ai besoin pour cet exemple sont déjà satisfaites.

Donc maintenant, laissez-moi passer en revue les différentes choses nécessaires pour ce tutoriel entier.

Tout d'abord, j'ai besoin du module os pour lire mes fichiers.

Ensuite, j'importerai NumPy en tant que np, j'aurai besoin de cette bibliothèque particulière pour les opérations mathématiques.

J'aurai également besoin de la bibliothèque h5py.

La bibliothèque h5py est une interface pythonique au format de données binaires HDF5.

Donc techniquement, tous les modèles que je crée dans Keras, je les sauvegarderai essentiellement au format h5.

Ensuite, j'ai besoin de matplotlib.

Cela est à nouveau utilisé pour la visualisation.

J'ai besoin de TensorFlow, j'importerai keras.

De TensorFlow.

Ce sont quelques-unes des couches dont j'aurai besoin lorsque nous en viendrons à l'aspect de création de modèles de deep learning.

Si je veux calculer à quel point mon modèle performe en termes de score de précision, c'est là que le module metrics de sklearn me donnera la fonctionnalité de score de précision.

Et de la bibliothèque système, j'aurai également besoin de la fonction getsizeof.

Donc ce sont quelques-unes des choses dont j'ai besoin pour créer un modèle TF Lite.

Donc maintenant, laissez-moi avancer et exécuter la cellule.

Donc lorsque j'exécute la cellule, ce qui se passe essentiellement est que Python exécute ce morceau de code.

Donc laissez-moi maintenant avancer et exécuter la cellule.

Je ne vois aucune erreur.

Cela signifie que toutes nos importations sont en place.

Laissez-moi avancer et vous montrer la version de TensorFlow que j'utilise pour ce tutoriel particulier.

J'utilise actuellement TensorFlow 2.6.0.

S'il y a des changements qui apparaissent concernant l'API.

N'hésitez pas à vous référer à la documentation de TensorFlow.

Il y a deux fonctions qui ont été créées, la première fonction s'appelle get_file_size.

Essentiellement, je passe l'emplacement du fichier en utilisant la bibliothèque os et spécifiquement la fonction getsize, je suis capable d'obtenir la taille d'un fichier particulier que je passe en octets, donc laissez-moi maintenant avancer et exécuter cette cellule.

Dans la fonction précédente, c'est-à-dire get_file_size, la valeur retournée serait en octets.

Donc maintenant, plutôt que de comprendre les valeurs de la taille d'un fichier en octets, j'ai créé une fonction auxiliaire appelée convert_bytes, qui prend essentiellement la taille d'entrée en octets et la convertit en Ko ou Mo.

Donc c'est quelque chose que j'ai créé.

Je n'ai pas inclus les Go car c'est plus une vidéo explicative dans laquelle j'ai l'intention de créer un modèle plus petit ou plutôt une preuve de concept plutôt qu'un modèle énorme.

Donc c'est pourquoi j'ai limité mes unités à des Ko ou Mo.

Donc laissez-moi avancer et exécuter la cellule.

Pour cet exemple particulier, je vais utiliser un ensemble de données très célèbre en deep learning, l'ensemble de données Fashion MNIST de Keras, donc laissez-moi démasquer la cellule, donc l'ensemble de données Fashion MNIST contient 70 000 images en niveaux de gris, qui appartiennent à 10 catégories différentes.

Donc les catégories incluront le t-shirt, le pantalon, le pull, la robe, le manteau, la sandale, la chemise, la basket, le sac et la botte.

Donc ce sont les différentes catégories qui font partie de cet ensemble de données.

L'ensemble de l'activité est une tâche d'apprentissage supervisé, j'aurai un ensemble d'images, et chaque image aura une étiquette associée.

Et j'essaie d'entraîner un modèle de deep learning.

Donc maintenant, laissez-moi avancer.

Vous n'avez pas à vous soucier des pièces de téléchargement.

Eh bien, si vous avez installé TensorFlow correctement, alors essentiellement vous devez simplement appeler la fonction keras.datasets.fashion_mnist, sauvegarder l'ensemble de données dans une variable appelée fashion_mnist.

Donc c'est la première étape que j'ai faite ici.

Une fois que vous avez fait cela, alors essentiellement ce que vous devez faire ensuite est de diviser votre ensemble de données en entraînement et test.

La façon dont vous pouvez y parvenir est idéalement en appelant une fonction appelée load_data.

Donc c'est ce que vous avez en termes de fonction.

Une fois que vous appelez cette fonction à partir de fashion_mnist, la variable que vous venez de créer, vous serez en mesure de diviser vos données en images d'entraînement, étiquettes d'entraînement, images de test et étiquettes de test.

Donc c'est aussi simple que cela.

Donc laissez-moi avancer et exécuter la cellule.

Donc nous avons téléchargé les fichiers de données, nous avons divisé nos données en entraînement et test.

J'ai également créé une variable, une variable de liste, appelée class_names, qui contient tous les noms des classes qui font partie de cette activité entière.

Donc laissez-moi avancer et exécuter la cellule.

Si vous vous souvenez, nous avions 70 000 échantillons dans notre ensemble de données, nous avons déjà divisé cet ensemble de données en entraînement et test.

Donc laissez-moi avancer et vous montrer combien d'images font partie de l'ensemble de données d'entraînement.

Donc laissez-moi exécuter cette cellule.

Donc la forme de mon ensemble de données d'entraînement est 60 000, 28, 28.

Donc j'ai 60 000 images.

Chaque image a une taille de 28 par 28.

Donc 28 lignes, 28 colonnes représentent chaque image, et j'ai 60 000 images de ce type.

Étant donné que c'est une tâche d'apprentissage supervisé, j'aurai également besoin de 60 000 étiquettes.

Donc laissez-moi vérifier si le nombre total d'étiquettes dans mon ensemble de données d'entraînement est de 60 000.

Donc laissez-moi exécuter cette cellule.

Donc, comme vous pouvez clairement le voir, j'ai également 60 000 étiquettes.

Maintenant, étant donné cela, j'ai déjà mentionné qu'il y a 10 classes uniques, laissez-moi vérifier cela également.

Donc, comme vous pouvez clairement le voir, j'ai des numéros de classe allant de zéro à neuf.

Et la correspondance est ce que j'ai créé ici, qui est contenu dans la variable class_names.

Allons maintenant de l'avant et explorons également l'ensemble de données de test.

Donc laissez-moi rapidement démasquer cela, laissez-moi vous montrer le nombre total d'images dans l'ensemble de données de test.

Donc cela donne 10 000, 60 000 pour l'entraînement et 10 000 pour le test.

Chaque image est à nouveau de la taille 28 par 28.

De même, si je regarde test_labels, j'aurai 10 000 échantillons.

Ce que j'ai l'intention de vous montrer ensuite, c'est une image d'exemple.

Donc laissez-moi vous montrer cela.

Donc voici une image d'exemple qui fait partie de cet ensemble de données.

C'est clairement une botte.

La taille de l'image est de 28 par 28.

Donc 28 lignes, 28 colonnes, c'est ce que vous voyez ici.

Avant d'avancer et d'entraîner un réseau de neurones, une bonne pratique consiste à mettre à l'échelle les valeurs d'intensité des images, qui varient entre zéro et 255, de zéro à un.

C'est ce que j'ai fait dans ce morceau de code.

Donc laissez-moi exécuter cela.

Donc maintenant, mes images d'entraînement auront des valeurs allant de zéro à un, et non de zéro à 255.

Jusqu'à présent, nous avons téléchargé l'ensemble de données, nous avons divisé notre ensemble de données en entraînement et test.

Et nous avons fait un certain prétraitement également, maintenant est le moment où nous allons créer un simple réseau de neurones qui classera les images entières dans l'une des 10 catégories qui existent.

Donc dans ce morceau de code, j'appelle la classe Sequential de la bibliothèque keras.

Je passe la première couche comme une couche aplatie.

Maintenant, si vous vous souvenez, les images étaient de 28 par 28.

Si je dois les passer à travers une couche, alors je dois essentiellement les aplatir d'abord, je ne crée pas de réseau de neurones convolutionnel étant donné que l'ensemble de données est assez simple, je vais rester sur un réseau de neurones profond normal.

Donc la première couche que j'ajoute est une couche aplatie, où je passe la forme d'entrée, qui est 28, virgule 28.

La deuxième couche est la couche dense.

Et les activations fournies à cette couche dense sont relu.

La couche finale est à nouveau une couche dense, étant donné que j'ai 10 classes différentes à classer.

Donc c'est ce que j'ai ici.

Donc laissez-moi rapidement créer une instance du modèle.

Donc laissez-moi exécuter cela.

Avant d'avancer et de compiler le modèle, je vous montrerai la structure du modèle également.

Donc je dirai model.summary.

Donc c'est essentiellement le résumé du modèle.

Donc pour l'architecture donnée, nous avons près de 100k paramètres entraînables.

Maintenant, l'étape suivante consiste à compiler le modèle.

Je passe l'optimiseur, je passe cette perte de cross-entropy catégorielle sparse.

Étant donné que nos classes sont mutuellement exclusives, j'utilise la perte de cross-entropy catégorielle sparse par rapport à la perte de cross-entropy catégorielle normale.

Et la matrice attend casing pour sa précision.

Donc je veux créer un modèle qui est assez précis.

Donc laissez-moi maintenant avancer et exécuter la cellule.

Donc j'ai créé une instance du modèle.

J'ai également compilé le modèle, maintenant est le moment où je vais passer les images d'entraînement ainsi que les étiquettes d'entraînement pour entraîner tous les paramètres entraînables.

Donc laissez-moi maintenant appeler la fonction model.fit, où je vais passer les images d'entraînement, les étiquettes d'entraînement, et je fais tourner tout l'exercice pendant 10 époques.

Donc laissez-moi exécuter la cellule.

Donc avec chaque époque, vous pouvez voir que la précision augmente.

Donc nous avons réussi à entraîner notre modèle et nous avons atteint un score de précision d'entraînement d'environ 91 %, ce qui est quelque chose de raisonnablement bon étant donné que j'ai entraîné le modèle pendant seulement 10 époques.

Donc allons de l'avant.

Et rappelez-vous une chose, l'objectif de la vidéo n'est pas d'entraîner le classificateur le plus précis à ce stade, mais de vous montrer la puissance de TF Lite, c'est pourquoi je me suis arrêté à 10 époques.

Maintenant, la prochaine chose que je fais est de créer une variable appelée keras_model_name.

C'est quelque chose qui sera utilisé comme référence, ou ce sera la performance de base du modèle que j'évaluerai plus tard avec les modèles TF Lite également.

Donc le nom de cette variable particulière est tf_model_fashion_mnist.h5.

Donc laissez-moi rapidement exécuter la cellule.

Maintenant, laissez-moi avancer et appeler la fonction model.save et passer le nom de fichier que je viens de créer.

Donc laissez-moi exécuter la cellule.

Donc dès que vous exécutez la cellule, vous aurez un fichier qui sera créé dans votre session Google Colab ou dans votre répertoire local, qui est essentiellement votre fichier de modèle sauvegardé.

Donc laissez-moi montrer cela également.

Donc voici notre fichier de modèle sauvegardé qui a été créé.

Donc laissez-moi rapidement exécuter la cellule à nouveau.

Maintenant, j'irai de l'avant et je vous montrerai la taille de ce fichier particulier que nous avons créé.

Donc laissez-moi appeler les deux fonctions que j'ai créées, c'est-à-dire convert_bytes et get_file_size, je passe le même nom de fichier, et je veux que la taille du fichier soit en Mo.

Donc laissez-moi exécuter la cellule.

Donc actuellement, j'ai un modèle qui occupe 1,2 Mo.

Donc j'irai de l'avant et je créerai une variable appelée keras_model_size, et j'enregistrerai la taille équivalente en octets dans cette variable particulière.

Donc laissez-moi exécuter la cellule.

Nous savons pour un fait que le modèle fonctionne très bien sur l'ensemble de données d'entraînement.

Mais alors le test de litmus essentiel est de vérifier à quel point le modèle fonctionne sur des données invisibles, c'est-à-dire mon ensemble de données de test.

Donc laissez-moi avancer et évaluer à quel point les performances de notre modèle sont bonnes sur leur ensemble de données de test.

Donc j'appelle la fonction model.evaluate, je passe les images de test, les étiquettes de test.

Et j'enregistre les résultats dans deux variables appelées test_loss et test_accuracy.

Donc laissez-moi rapidement exécuter la cellule.

Donc, comme vous pouvez clairement le voir, la perte est à une valeur très petite, qui est d'environ 0,37.

Et j'ai atteint un score de précision de test d'environ 88 %.

Donc nous avons terminé la première partie, maintenant il est temps de passer à la partie suivante qui consiste à créer un équivalent TF Lite du même modèle.

Donc, allons de l'avant.

Donc je commence l'activité en créant une variable appelée tf_lite_model_file_name.

Et je passe un nom équivalent à ce modèle TF Lite particulier, qui dans notre cas, actuellement est tf_lite_model.tflite.

Donc laissez-moi rapidement exécuter la cellule.

Maintenant, le processus de conversion d'un modèle TensorFlow ou Keras en un modèle TF Lite nécessite essentiellement quelques étapes.

Donc c'est ce que je vais mettre en évidence maintenant.

Donc la première étape consiste à appeler tf.lite.TFLiteConverter.from_keras_model, je passe le modèle que j'ai créé.

Donc si vous vous souvenez du nom de la variable du modèle était essentiellement model, c'est ce que je passe ici dans la première ligne.

Une fois que j'ai créé une instance du convertisseur TF Lite à partir de Keras, j'enregistre toute la pièce dans une variable appelée tf_lite_converter.

Et enfin, ce que je fais ensuite, c'est que j'appelle la fonction Convert.

Une fois la conversion effectuée, je veux que le résultat soit enregistré dans une variable appelée tf_lite_model.

Donc laissez-moi rapidement exécuter la cellule.

Donc si vous regardez la sortie, elle indique que les actifs sont écrits dans un fichier temporaire particulier.

Donc à partir de ce fichier temporaire, je dois essentiellement récupérer les poids du modèle et les enregistrer dans un fichier équivalent TF Lite.

Donc c'est ce que j'ai fait en utilisant ce morceau de code.

J'ai créé la première variable qui est tf_lite_module_name.

Et je passe le nom initial que j'ai créé dans la première ligne de cette section particulière.

J'ouvre le nom du fichier avec un accès en écriture, et j'écris ce fichier temporaire particulier dans ce fichier que j'ai créé.

Donc c'est aussi simple que cela.

Donc laissez-moi rapidement exécuter cela.

Donc il y a une sortie particulière qui est affichée.

Cela me dit le nombre total d'octets qui ont été retournés à ce fichier particulier.

Maintenant, laissez-moi avancer et vous montrer la taille exacte de ce modèle TF Lite en kilooctets.

Donc laissez-moi exécuter cela.

Donc la taille totale du fichier est proche de 400 kilooctets.

Donc nous avons commencé avec un modèle qui occupait environ 1,2 Mo.

Et après avoir exécuté quelques lignes de code, nous avons réduit la taille du fichier à environ 400 Ko.

Maintenant, laissez-moi avancer et enregistrer cette taille de fichier dans une variable appelée tf_lite_file_size.

C'est quelque chose qui aura beaucoup de sens une fois que nous avancerons.

Donc laissez-moi rapidement exécuter cette cellule.

Nous avons déjà converti un modèle de Keras en tf lite.

Mais une chose que nous n'avons pas validée actuellement, c'est à quel point le modèle est performant.

Est-il réellement bon sur des données invisibles ? Ou a-t-il chuté en termes de score de précision.

Donc c'est ce que je veux vérifier ensuite, c'est-à-dire après avoir compressé le modèle en utilisant TF Lite, perdons-nous en précision ou non.

Donc dans cette section, je vais passer en revue comment vous pouvez valider les résultats en termes de performance de votre modèle TF Lite.

Donc maintenant, laissez-moi rapidement démasquer la cellule.

Maintenant, ne vous laissez pas effrayer par ce morceau de code, je vais vous aider à comprendre ce que j'essaie d'accomplir.

Vous chargez maintenant un modèle, ou un modèle TensorFlow ou Keras dans une session TensorFlow est assez facile.

Mais ici, ce que nous avons fait, c'est que nous avons créé un modèle TF Lite.

Si vous revenez à la discussion que nous avons eue, les modèles TF Lite sont essentiellement des fichiers au format flat buffer et non vos fichiers protocol buffer habituels.

Donc, afin de faire une inférence à partir des fichiers TF Lite sur notre session TensorFlow ou Python, nous avons besoin de quelque chose appelé un interpréteur.

Donc c'est votre interpréteur qui utilisera essentiellement l'interpréteur de TensorFlow pour charger le fichier TF Lite, puis faire des inférences ou des prédictions.

Donc laissez-moi maintenant vous guider à travers chaque ligne de code.

Donc dans la première ligne, je crée une instance de la classe Interpreter, je passe le nom du modèle TF Lite que nous venons de créer.

Donc si vous regardez cette section particulière, vous aurez également un fichier TF Lite.

C'est ce que je passe ici.

Maintenant, une fois que nous avons créé l'objet Interpreter, l'objet Interpreter sauvegarde les détails sur le modèle.

Il aura des détails sur l'entrée qu'il attend, la valeur, le type de valeurs qu'il attend, et en termes de sortie, il vous dira quelle doit être la forme de la sortie.

En termes de sortie, il vous dira la forme de la sortie ainsi que le type de sortie, c'est-à-dire les valeurs de sortie, il prédira quelles sont les valeurs et quel est le type de valeurs.

Donc tout cela est ce que cet interpréteur particulier aura réellement des détails.

Les détails qu'il récupère proviennent à nouveau de l'objet Interpreter que nous avons créé et nous avons passé le fichier TF Lite.

Donc tous les détails seraient capturés dans ce fichier TF Lite particulier, qui est ce qui est lu par cet objet Interpreter.

Et c'est ce que nous essayons d'accumuler à partir de input_details et output_details.

Une fois que nous avons les détails d'entrée et de sortie, je m'intéresse également à la forme de l'entrée attendue et au type de ces entrées, c'est-à-dire la nature variable des entrées.

Donc laissez-moi rapidement exécuter cette cellule pour mieux comprendre.

Donc si vous regardez de près, la forme d'entrée est 1 28 28.

Le type d'entrée qu'il attend est NumPy float32, la forme de sortie est 1 10, c'est-à-dire une ligne et 10 colonnes, et le type de sortie est à nouveau NumPy float32.

Donc c'est essentiellement ce que contient le fichier TF Lite.

Maintenant, si vous regardez ce particulier, cela indique que le TF Lite attend une entrée à la fois.

Maintenant, je veux vérifier ses performances pour 10 000 entrées.

C'est là que je devrais redimensionner la forme d'entrée à une valeur particulière, ce que je vais réaliser dans ce morceau de code.

Juste pour réitérer, la forme d'entrée est 1 28 28.

Donc idéalement, je dois passer une seule image.

Et essentiellement, j'obtiendrais une sortie correspondante.

Mais essentiellement, dans mon cas d'utilisation, je veux valider les performances du modèle TF Lite pour l'ensemble de données de test que j'ai, qui contient essentiellement 10 000 images.

Donc si cette idée est claire pour vous, allons de l'avant.

Donc maintenant, je veux valider les performances de mon modèle TF Lite sur mon ensemble de données de test.

Donc j'appelle la fonction resize_tensor_input.

Je passe les détails que je veux redimensionner cette valeur d'index particulière, et je passe comment je dois la redimensionner.

Donc actuellement, j'ai 10 000 échantillons.

Donc c'est ce que j'ai entré ici, c'est-à-dire 10 000, 28, 28.

Une opération de redimensionnement similaire est ce que je fais du côté de la sortie.

Donc vous pouvez voir 10 000, 10, à partir du 1, 10 initial.

Donc c'est ce que j'ai fait ici.

Maintenant, une fois que l'opération de redimensionnement a eu lieu, je veux appeler allocate_tensors.

Pour changer réellement la structure entière de l'interpréteur.

C'est ce qui est lu en utilisant le fichier TF Lite.

Et maintenant, lorsque j'imprime les détails d'entrée et de sortie, je devrais être en mesure de voir que les valeurs d'entrée et de sortie de TF Lite ont changé.

Donc laissez-moi rapidement exécuter ce morceau de code.

Donc, comme vous pouvez clairement le voir, la forme d'entrée a changé de 1 28 28 à 10 000 28 28.

Donc cela va essentiellement m'aider à valider les performances de mon modèle TF Lite.

L'autre chose que je veux souligner maintenant est que test_images.dtype est float64.

Donc si vous regardez la forme d'entrée que le modèle attend est NumPy.float32.

Donc maintenant, le seul autre changement que je dois faire pour valider mon modèle TF Lite est de créer un nouveau tableau appelé test_images_numpy.

Passer le tableau original, et changer le dtype.

Je peux le faire dans le même tableau également.

Mais j'opte essentiellement pour créer deux tableaux différents.

Donc laissez-moi rapidement exécuter la cellule.

Donc maintenant, si je vous montre le dtype de test_images_numpy, il sera NumPy float32.

Maintenant que nous avons l'objet interpréteur entier configuré correctement pour notre ensemble d'entrées, c'est-à-dire l'ensemble de données de test.

Tout ce que je dois faire maintenant est d'abord appeler la fonction set_tensor, en passant le tableau test_images_numpy que je viens de créer et appeler la fonction invoke.

Ce que la fonction invoke fera essentiellement, c'est passer les entrées, obtenir la sortie.

Et une fois que vous avez la sortie prête, vous appelez la fonction get_tensor qui aura la sortie prête pour vous et l'enregistrera dans une variable appelée tf_lite_model_predictions.

Donc laissez-moi rapidement exécuter la cellule.

Maintenant, la sortie que vous voyez ici, qui est la forme des résultats de prédiction, est de 10 000 lignes et 10 colonnes.

Donc chaque colonne contiendra essentiellement un score de probabilité.

Donc ce que je dois faire ensuite, c'est sélectionner la valeur ou l'index entre zéro et neuf qui a la probabilité maximale, ce que j'ai fait en utilisant cette fonction appelée np.argmax.

Donc cela m'aidera à obtenir des nombres directement, c'est-à-dire de zéro à neuf plutôt que d'avoir 10 colonnes différentes avec des scores de probabilité.

Maintenant, laissez-moi calculer le score de précision.

Et laissez-moi l'imprimer pour vous.

Donc la précision de test du modèle TF Lite est exactement la même que celle que vous voyez lorsque vous la comparez avec votre modèle Keras normal.

Maintenant, combien d'espace avez-vous économisé dans l'ensemble de ce processus ? Dites, Mel, laissez-moi calculer un ratio entre la taille du fichier TF Lite et la taille du fichier du modèle Keras.

Donc, dans l'ensemble, le modèle TF Lite occupe environ 32 % de la taille totale du fichier que mon modèle Keras normal occupe.

Mais l'unicité est que je ne perds pas en précision.

Donc c'est la puissance de TF Lite.

J'ai été en mesure de compresser mon modèle entier de 1,2 Mo à environ 400 Ko.

Et je n'ai pas encore compromis un peu sur les morceaux de précision.

Eh bien, n'est-ce pas incroyable ? Eh bien, si vous pensez que l'histoire se termine ici, attendez une seconde, il y a plus à venir.

Jusqu'à présent, ce que nous avons fait, c'est que j'ai pris un modèle TensorFlow.

Et sans aucune optimisation, je l'ai essentiellement converti en un modèle TF Lite équivalent.

Maintenant, je vais vous montrer comment vous pouvez compresser votre modèle encore plus.

sans perdre en précision.

Donc maintenant, laissez-moi vous présenter un nouveau concept appelé la quantification.

Donc qu'est-ce exactement que ce terme que je viens de mentionner, c'est-à-dire la quantification.

Donc pour une valeur de poids donnée qui peut être représentée en format float 32 ou float 64 ? Ne serait-ce pas génial si nous pouvons réduire la taille de ces valeurs particulières et voir très peu de changement en précision ? Eh bien, cela représente essentiellement le concept de quantification, je réduis le nombre total de bits pour chaque valeur de poids, de sorte que la taille globale de l'ensemble du tableau soit réduite.

Juste pour être plus clair, si j'ai un réseau de neurones comme celui-ci, où cette valeur de poids particulière est 5.31345, cette valeur de poids particulière est 3.8958.

Et vous avez les autres valeurs de poids également, que se passerait-il si je pouvais changer ces représentations qui occupent tant de bits en quelque chose comme ceci, il y aura un petit impact sur la précision.

Mais globalement, je serai en mesure de compresser mon modèle encore plus.

Comment quand quelles que soient les questions que vous avez en tête, attendez un peu.

Si cette idée entière est claire pour vous, revenons à la section de codage.

Et je vous montrerai comment vous pouvez compresser votre modèle TF Lite encore plus.

Donc par défaut, dans l'exemple précédent, où nous avons pris un modèle Keras et nous l'avons converti en un modèle TF Lite, chaque valeur de poids est essentiellement au format float 32.

Ne serait-ce pas génial si je le compresse de float 32 à float 16.

C'est l'activité que je vais effectuer ensuite.

Donc je crée une variable avec un nom de fichier de modèle tf_lite_float_16.

Et je lui donne essentiellement un nom qui représente que tous les poids à l'intérieur seront en float 16.

Donc c'est ce que j'ai ici.

Donc laissez-moi rapidement exécuter la cellule.

Si vous regardez la section précédente en termes de la façon dont nous avons créé un modèle TF Lite, la première ligne de code est quelque chose qui vous est assez familier, vous passez votre modèle Keras, vous appelez le convertisseur tf.lite.TFLiteConverter.from_keras_model, et vous l'enregistrez dans une variable.

Même le dernier morceau de code est également quelque chose que vous avez déjà vu.

Ce que vous n'avez pas vu jusqu'à présent, c'est l'optimisation.

Donc lorsque vous créez une instance du convertisseur tf.lite.TFLiteConverter, il y a un drapeau appelé optimizations.

Donc vous avez le drapeau optimizations ici.

Je le définis sur tf.lite.Optimize.DEFAULT, donc je veux que les optimisations par défaut aient lieu.

Et une autre chose que je fais ici.

Donc je parlerai davantage des optimisations dans la section suivante.

Donc gardez cette pensée également.

Maintenant, il y a un autre drapeau appelé target_spec et supported_types.

C'est ici que je définis chaque valeur de poids de float32 à float16.

Donc c'est ce que je fais ici.

Donc laissez-moi rapidement exécuter ce morceau de code.

Donc maintenant, j'ai un modèle TF Lite, où chaque valeur de poids serait un float16, je suis le même processus à nouveau, où je récupère les données du fichier temporaire et je les enregistre dans un modèle TF Lite.

Donc laissez-moi exécuter cela.

Je ne sais pas si vous l'avez deviné déjà ou non.

Cela représente essentiellement une taille de fichier en octets pour le modèle TF Lite nouvellement converti.

Donc si je vous montre maintenant la taille de ce modèle TF Lite nouvellement converti, alors ma taille a considérablement diminué de 400 kilooctets à 200 kilooctets.

La seule chose que j'ai changée ici, c'est que j'ai modifié la représentation individuelle de chaque valeur de poids, c'est tout.

N'est-ce pas incroyable, je suis capable d'économiser autant de mémoire, juste en changeant quelques valeurs ici et là.

Dites à nouveau, enregistrez la taille du fichier dans une variable appelée tf_lite_float_16_file_size.

Donc laissez-moi exécuter cela.

Maintenant, si je le compare au modèle Keras original, ce modèle particulier occupe 16 % de la taille que le modèle original occupait.

Et si je le compare à la version précédemment créée, alors je peux voir une compression d'environ 50 % que je suis capable d'atteindre en changeant les poids de float32 à float16.

Donc c'est la puissance des optimisations et de TF Lite.

Si vous pensez que c'est tout, attendez la section suivante, où je compresse le modèle encore plus.

Je ne vous montre pas la partie précision pour l'instant, vous vous demandez peut-être, pourquoi ne nous montre-t-il pas la précision ? La précision a-t-elle pris un coup ? Eh bien, la réponse est non.

Je vous montre la précision d'un modèle encore plus compressé.

Donc cela vous donnera une idée juste de la façon dont la compression change les valeurs de précision globales également.

D'accord.

Donc maintenant nous avons atteint la section finale où je vais compresser le modèle encore plus.

D'accord, donc ici j'ai créé une variable appelée tf_lite_size_current_model_file_name.

Et ici je veux voir ce que le fichier eflite avec ce nom particulier.

Donc je vais rapidement exécuter la cellule.

Dans l'exemple précédent, j'ai changé chaque valeur de poids de float32 à float16.

Plutôt que de décider ce qui est bon pour votre modèle, je préférerais laisser TF Lite décider cela pour moi.

Donc si vous avez suivi jusqu'à présent, alors ce morceau de code est quelque chose que nous avons déjà couvert.

Ce morceau de code est également quelque chose que nous avons déjà couvert.

Cela est quelque chose d'unique.

Donc ici, je définis le drapeau optimizations.

Et ici je mentionne simplement, optimiser pour la taille, il y a différentes valeurs que vous pouvez parcourir dans la documentation.

Donc en fonction de vos besoins, vous pouvez optimiser pour la taille, et les autres optimisations qui sont également disponibles pour TF Lite.

Donc je ne spécifie pas quel type de type de données je veux, je veux simplement la version la plus optimisée où la taille occupée par ce modèle TF Lite particulier est la version la plus compressée.

D'accord, donc je vais rapidement exécuter la cellule.

Donc j'attrape tout le fichier qui est sauvegardé dans une variable temporaire, je l'enregistre dans cette variable particulière que j'ai créée.

Et si vous avez deviné maintenant, c'est la nouvelle taille de fichier en octets.

Si je vais à la section kilooctet, alors mon fichier occupe environ 100 Ko.

Donc si vous vous souvenez, nous avons commencé à 1,4 Mo, et nous avons réduit la taille du fichier d'un réseau de neurones profond.

200 kilooctets.

N'est-ce pas incroyable.

Juste pour vous donner quelques chiffres à nouveau, si je compare cette taille de fichier particulière avec ma taille de fichier originale, alors mon fichier actuel fait presque 8 % de la taille de mon fichier original, c'est-à-dire mon modèle Keras que j'ai créé.

Si je le compare au modèle précédent également, je suis essentiellement capable d'atteindre une compression de 50 %, tout cela grâce à l'optimisation pour la taille.

Cela représente essentiellement la puissance de TF Lite.

Maintenant, je suis vraiment heureux de la compression, j'ai un fichier de 1,4 Mo que j'ai compressé à environ 100 Ko.

Mais la précision est-elle toujours la même ? Eh bien, nous allons à nouveau suivre le même processus, où je charge le modèle nouvellement quantifié dans l'objet interpréteur.

J'obtiendrai les détails de ces objets, et je vais à nouveau redimensionner les valeurs et passer l'ensemble de données de test entièrement à travers l'objet interpréteur.

Donc je vais rapidement exécuter la cellule.

Donc, comme vous pouvez clairement le voir, 1 28 28 sont les valeurs d'entrée de l'objet interpréteur qu'il attend, j'ai la sortie comme 1, 10.

Les valeurs d'entrée et de sortie attendues sont NumPy float32.

Donc tout est bon également.

Venons-en à la section finale, je suis le même processus.

Encore une fois, aucun changement dans le processus.

J'ai un ensemble de données de test de 10 000 images, que je passe ici.

J'alloue des tenseurs, j'obtiens les détails, et je vous montrerai les détails également.

Donc laissez-moi rapidement exécuter cela 10 000 28 28 1 28 28.

Donc nous avons redimensionné les valeurs d'entrée des tenseurs que nous attendons pour valider notre ensemble de données de test.

Vous n'avez essentiellement pas besoin de cette étape à nouveau, mais je l'ai copiée de la partie initiale.

Donc je l'exécute à nouveau.

Je passe les valeurs à nouveau.

Maintenant, je calcule le score de précision.

Maintenant, c'est le test de litmus pour ce modèle TF Lite hautement compressé.

Donc laissez-moi rapidement exécuter la cellule.

Donc la précision d'un modèle TF Lite qui occupe presque 8 % de la taille du modèle Keras original est équivalente au modèle Keras original.

Si je remonte, j'enregistre cette vidéo en une seule fois.

Donc si je remonte, où est passée cette valeur ? Ici, la valeur était à 7,66 %.

Ici, elle est à 87,59 %.

Donc c'est ce que vous pouvez réaliser en utilisant TF Lite.

J'ai commencé avec un réseau de neurones très simple, l'ensemble du modèle occupait environ 1,2 Mo.

Vous pourriez aussi argumenter que 1,2 Mo est assez petit.

Mais l'énoncé du problème était assez simple.

Si vous avez un exemple vraiment complexe, où vous devez classer des images en 1000 ou 10 000 catégories, la taille du modèle augmenterait éventuellement.

Donc l'objectif devient alors, pouvons-nous compresser la taille du modèle ? Et la réponse est oui, TF Lite vous aidera à compresser la taille du modèle sans avoir à compromettre la précision.

Si vous avez atteint ce point, alors j'imagine que vous avez vu la vidéo entière ou si vous avez atteint ce point au hasard, de quelque manière que vous avez atteint ce point.

J'espère que vous avez apprécié la vidéo d'aujourd'hui, je continue à créer de telles vidéos incroyables sur la science des données, le machine learning et Python.

Donc n'hésitez pas à consulter ma chaîne dans la section description de la vidéo également.

Merci beaucoup d'avoir regardé cette vidéo.