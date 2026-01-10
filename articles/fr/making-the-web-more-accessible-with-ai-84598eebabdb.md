---
title: Rendre le web plus accessible avec l'IA
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-28T12:59:40.000Z'
originalURL: https://freecodecamp.org/news/making-the-web-more-accessible-with-ai-84598eebabdb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tnrnBXhvdS4242CppvDIfQ.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: AWS
  slug: aws
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Rendre le web plus accessible avec l'IA
seo_desc: 'By Abhinav Suri

  Most people see the Internet as a place full of text, images, and videos. But the
  Internet is something completely different for people who are visually impaired.

  Screen readers, tools that read text and metadata on a web page, are li...'
---

Par Abhinav Suri

La plupart des gens voient Internet comme un lieu rempli de texte, d'images et de vidéos. Mais pour les personnes malvoyantes, Internet est quelque chose de complètement différent.

Les lecteurs d'écran, des outils qui lisent le texte et les métadonnées d'une page web, sont limités. Ils ne montrent qu'un seul aspect d'une page web, à savoir le texte sur un site web. Certains développeurs ajoutent des légendes descriptives à leurs images, mais la grande majorité ne le fait pas.

Selon l'[Organisation mondiale de la santé](http://www.who.int/mediacentre/factsheets/fs282/en/), environ 285 millions de personnes dans le monde sont malvoyantes. Aux États-Unis seulement, 8,1 millions de personnes utilisant Internet sont malvoyantes.

J'ai donc créé un outil pour aider les malvoyants à "voir" Internet, grâce à la puissance de l'IA. Je l'ai nommé Auto Alt Text. C'est une extension Chrome où les utilisateurs cliquent simplement avec le bouton droit sur une image pour obtenir une description de celle-ci. C'est la première extension de ce type.

Regardez la vidéo ci-dessous pour voir comment cela fonctionne.

Vous pouvez également essayer Auto Alt Text en le téléchargeant [ici](http://www.abhinavsuri.com/aat/).

### Pourquoi j'ai créé Auto Alt Text

Je faisais partie de ces développeurs qui n'ajoutaient pas de descriptions aux images web. L'accessibilité était toujours une réflexion secondaire pour moi. Cela a changé lorsque j'ai reçu l'e-mail suivant concernant [l'un de mes projets](https://github.com/hack4impact/flask-base).

![Image](https://cdn-media-1.freecodecamp.org/images/1*uYx_pi9vAI17mQ20D81ykw.png)
_Texte de l'e-mail : "Bonjour Abhinav, j'ai trouvé votre projet flask-base et je pense qu'il sera parfaitement adapté à mon prochain projet. Merci de travailler dessus. Je voulais aussi vous faire savoir que vous devriez mettre des descriptions alt sur les images de votre readme. Je suis légalement aveugle et j'ai eu du mal à distinguer ce qu'il y avait dessus :/ De REDACTED"_

Avant cela, j'avais mis l'accessibilité en bas de ma liste de choses à faire. C'était une réflexion après coup. Mais cet e-mail a été un réveil pour moi. Il y a de nombreuses personnes qui ont besoin de fonctionnalités d'accessibilité pour utiliser le web, les applications, les projets, et plus encore.

> "Le web regorge d'images qui ont des textes alternatifs manquants, incorrects ou pauvres" — WebAIM (Centre pour les personnes handicapées de l'Université d'État de l'Utah)

### L'intelligence artificielle à la rescousse

Il existe de nombreuses façons de mettre des légendes sur les images. Cependant, la plupart partagent ces inconvénients :

* Elles ne sont pas réactives et prennent beaucoup de temps pour retourner une légende.
* Elles sont semi-automatisées. Elles dépendent des humains pour placer manuellement des légendes sur les images.
* Elles sont coûteuses à créer et à maintenir.

En créant un réseau de neurones, ces problèmes peuvent être résolus.

J'ai récemment commencé à plonger dans le machine learning et l'IA. C'est alors que j'ai découvert Tensorflow. TensorFlow est une bibliothèque open-source qui aide au machine learning. Tensorflow permet aux développeurs de construire des modèles robustes qui peuvent accomplir une variété de tâches, de la détection d'objets à la reconnaissance d'images.

Je suis tombé sur un article de Vinyals, [Toshev](https://arxiv.org/find/cs/1/au:+Toshev_A/0/1/0/all/0/1), [Bengio](https://arxiv.org/find/cs/1/au:+Bengio_S/0/1/0/all/0/1), et [Erhan](https://arxiv.org/find/cs/1/au:+Erhan_D/0/1/0/all/0/1) (2016) intitulé "[Show and Tell: Lessons learned from the 2015 MSCOCO Image Captioning Challenge](https://arxiv.org/abs/1609.06647)". Ces chercheurs ont créé un réseau de neurones pour décrire le contenu des images de manière sémantique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mSvmjcvUbpgB3izigcEi4w.png)
_Exemples d'images et de leurs descriptions de texte alternatif résultantes — im2txt en action — du [dépôt Github im2txt](https://github.com/tensorflow/models/tree/master/im2txt" rel="noopener" target="_blank" title="")_

### Détails techniques de im2txt

La mécanique du modèle est détaillée. Mais il s'agit essentiellement d'un schéma encodeur-décodeur. Tout d'abord, l'image est passée à travers un réseau de neurones convolutif profond appelé Inception v3, qui classe les images.

Ensuite, l'image encodée est passée à travers un LSTM (long short-term memory), qui est un type de réseau de neurones spécialisé dans la modélisation de séquences/informations sensibles au temps.

Le LSTM travaille ensuite à travers un vocabulaire défini et crée une phrase pour décrire l'image. Il le fait en calculant la probabilité que chaque mot d'un ensemble de vocabulaire apparaisse dans la phrase. Il calcule ensuite la probabilité du deuxième mot, en fonction du premier mot. Cela continue jusqu'à ce que le caractère le plus probable soit un point. Cela indique la fin de la légende.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CW6YVV_zEriaGrxMzN4quA.png)
_Aperçu de la structure du réseau de neurones (du [dépôt Github im2txt](https://github.com/tensorflow/models/tree/master/im2txt" rel="noopener" target="_blank" title=""))_

Selon le dépôt Github, il faut une à deux semaines pour entraîner ce réseau de neurones sur un GPU Tesla k20m (c'est probablement beaucoup plus pour un CPU standard sur un ordinateur portable). Heureusement, un membre de la communauté Tensorflow a fourni un modèle entraîné pour téléchargement public.

### Problèmes hors de la boîte + Lambda

Lorsque j'ai exécuté le modèle, j'ai réussi à le faire fonctionner avec Bazel. Bazel est un outil qui pré-packe les modèles Tensorflow en scripts (entre autres objectifs). Cependant, il a fallu 15 secondes pour obtenir le résultat pour une image. Et cela, lorsque je l'ai exécuté sur la ligne de commande ! La seule façon de résoudre ce problème est de garder le graphe Tensorflow en mémoire. Cela nécessite cependant que l'application fonctionne 24h/24 et 7j/7.

Je voulais mettre ce modèle sur AWS Elastic Beanstalk, où le temps de traitement est distribué à l'heure, mais garder une application active en permanence n'était pas idéal (point #3 dans la liste des inconvénients des logiciels de légendes). J'ai donc décidé de passer à AWS Lambda.

AWS Lambda est un service qui fournit une informatique sans serveur à un coût incroyablement bas. Il facture à la seconde lorsqu'il est utilisé.

AWS Lambda fonctionne comme suit : votre application reçoit une demande d'un utilisateur, puis AWS Lambda active une image de votre application. Ensuite, il sert une réponse et désactive cette image. Si vous avez plusieurs demandes en même temps, il se met à niveau pour gérer plusieurs demandes.

De plus, il garde votre application activée tant qu'il y a plusieurs demandes dans l'heure. Ce service était un excellent choix pour mon cas d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q4EaQYos3s-67OkhhKzDkg.png)
_AWS API Gateway + AWS = cœur ([src](https://cdn-media-1.freecodecamp.org/images/1*SzOPXTf_YQNtFejG0e4HPg.png" rel="noopener" target="_blank" title=""))_

Le problème avec AWS Lambda était que je devais créer une API pour le modèle im2txt. AWS Lambda a une contrainte de mémoire sur l'application qui peut être chargée en tant que fonction. Lorsque vous téléchargez un fichier .zip contenant le code de votre application et ses dépendances, le fichier ne peut pas dépasser 250 Mo. Cette limite était un problème car mon modèle im2txt faisait plus de 180 Mo. Et les dépendances qui permettent de l'exécuter faisaient plus de 350 Mo. La limite de stockage totale sur AWS Lambda est de 512 Mo. Mon application dépassait cette limite. Elle faisait environ 530 Mo.

Pour réduire la taille de mon projet, j'ai reconfiguré im2txt pour accepter un modèle réduit. Cela a réduit la taille à 120 Mo. J'ai ensuite découvert [Lambda-packs](https://github.com/ryfeus/lambda-packs) qui contenait une version minimisée de toutes les dépendances, mais avec une version antérieure de Python et Tensorflow. Après avoir rétrogradé la syntaxe Python 3.6 et le code Tensorflow 1.2, j'ai enfin eu un package de 480 Mo, juste en dessous de la limite de 512 Mo.

Pour garder un temps de réponse rapide, j'ai créé une fonction CloudWatch pour garder l'instance AWS Lambda active et l'application en cours d'exécution. J'ai ajouté quelques fonctions d'assistance pour manipuler les images qui n'étaient pas au format JPG. J'ai enfin eu une API fonctionnelle. Ces réductions ont conduit à un temps de réponse extrêmement rapide. Il était inférieur à cinq secondes dans la plupart des cas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e5awvS8Z3k5V9qaxzMadQw.png)
_Image avec les probabilités probables de ce qui se trouve dans l'image selon l'API_

De plus, AWS Lambda est incroyablement bon marché. Actuellement, je peux analyser 60 952 images gratuitement chaque mois. Et chaque image supplémentaire coûte 0,0001094 $ (soit environ 6,67 $ pour les **60 952** prochaines images).

Pour plus de détails sur l'API, veuillez cliquer [ici](https://github.com/abhisuri97/auto-alt-text-lambda-api).

Il ne restait plus qu'à l'emballer dans une extension Chrome pour faciliter son utilisation par l'utilisateur final. Cela n'a pas été trop difficile. Il s'agissait d'une simple requête AJAX vers mon point de terminaison API.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SXf884JCTh_Ze-0XcXsxiw.gif)
_Extension Chrome Auto Alt Text en action_

### Résultats

Im2txt fonctionne bien sur les images qui contiennent des personnes, des paysages et tout objet présent dans le jeu de données Common Objects in Context (COCO). Un échantillon des images de COCO est présenté dans l'illustration ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NE9GCZliWRPy9km6Kmaarw.png)
_Catégories d'images dans le jeu de données COCO_

Le modèle ci-dessus limite la portée de ce qui peut être légendé. Mais il couvre la majorité des images vues sur les sites de médias sociaux tels que Facebook et Reddit.

Cependant, il échoue souvent à légender les images qui contiennent du texte. Cela est dû au fait que le jeu de données COCO ne contient pas de telles images. J'ai essayé d'utiliser Tesseract pour accomplir cette tâche, mais les résultats n'étaient pas précis et prenaient trop de temps (plus de 10 secondes par image). Je tente actuellement de mettre en œuvre, dans Tensorflow, les idées discutées dans [l'article de Wang, Wu, Coates et Ng](http://ai.stanford.edu/~ang/papers/ICPR12-TextRecognitionConvNeuralNets.pdf) pour capturer les images qui contiennent du texte.

### Conclusion

Une nouvelle histoire sur les merveilles de l'IA est écrite chaque semaine. Mais il est important de voir comment ces outils peuvent être utilisés en dehors de la recherche afin qu'ils puissent aider les gens. Dans l'ensemble, j'ai adoré plonger dans Tensorflow avec im2txt et appliquer ce que j'ai appris pour aider à résoudre un problème réel. Espérons que cet outil sera le premier de nombreux outils qui aideront les personnes malvoyantes à voir un Internet meilleur.

### Liens

* Suivez-moi. Je publie principalement sur [Medium](https://medium.com/@abhisuri97). Si vous aimez cet article, je vous serais reconnaissant de me suivre. :) Dans les mois à venir, je publierai plus de guides "comment faire" pour utiliser l'IA/Tensorflow afin de résoudre des problèmes réels. Je publierai également des tutoriels JavaScript dans un avenir proche.
* Pour voir l'extension Chrome, [cliquez ici](http://abhinavsuri.com/aat).
* Pour voir le dépôt Github de l'API Lambda Auto Alt Text, [cliquez ici](http://github.com/abhisuri97/auto-alt-text-lambda-api).