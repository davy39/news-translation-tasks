---
title: Comment l'IA peut apprendre à générer des images de chats
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-19T06:54:23.000Z'
originalURL: https://freecodecamp.org/news/how-ai-can-learn-to-generate-pictures-of-cats-ba692cb6eae4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7wMCLJ-EbSeyQvFUb9zVbA.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Comment l'IA peut apprendre à générer des images de chats
seo_desc: 'By Thomas Simonini

  In 2014, the research paper Generative Adversarial Nets (GAN) by Goodfellow et al.
  was a breakthrough in the field of generative models.

  Leading researcher Yann Lecun himself called adversarial nets “the coolest idea
  in machine lea...'
---

Par Thomas Simonini

En 2014, l'article de recherche [Generative Adversarial Nets](https://arxiv.org/pdf/1406.2661.pdf) (GAN) de Goodfellow et al. a été une percée dans le domaine des modèles génératifs.

Le chercheur de premier plan Yann Lecun lui-même a appelé les réseaux adverses "l'idée la plus cool en apprentissage automatique des vingt dernières années".

Aujourd'hui, grâce à cette architecture, nous allons construire une IA qui génère des images réalistes de chats. N'est-ce pas génial ?!

![Image](https://cdn-media-1.freecodecamp.org/images/1*BRTW5OTSkeiseWOFcPgU4w.gif)
_DCGAN pendant l'entraînement_

Pour voir le code complet, consultez [mon dépôt Github](https://github.com/simoninithomas/CatDCGAN). Il sera utile si vous avez déjà une certaine expérience en Python, en Deep Learning et Tensorflow, et en CNNs (Convolutional Neural Nets).

Si vous êtes nouveau en Deep Learning, veuillez consulter cette excellente série d'articles :

[**L'apprentissage automatique est amusant !**](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471)
[_L'introduction la plus facile au monde à l'apprentissage automatique_medium.com](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471)

### Qu'est-ce que DCGAN ?

Les Deep Convolutional Generative Adverserial Networks (ou DCGAN) sont une architecture d'apprentissage profond qui génère des sorties similaires aux données de l'ensemble d'entraînement.

Ce modèle remplace les couches entièrement connectées du modèle de réseau adversarial génératif par des couches de convolution.

Pour expliquer comment DCGAN fonctionne, utilisons la métaphore de l'expert en art et du faussaire.

Le faussaire (a.k.a. "le générateur") essaie de produire de fausses peintures de Van Gogh et de les faire passer pour réelles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AsJFLppJC5ODgZdAXWQXMQ.png)
_Icône de criminel faite par Roundicon de [www.flaticon.com](http://www.flaticon.com" rel="noopener" target="_blank" title="Flaticon)_

D'autre part, l'expert en art (a.k.a., "le discriminateur") essaie d'attraper le faussaire en utilisant ses connaissances des vraies peintures de Van Gogh.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nuRYU3fkM0bnXsSAxq1eZQ.png)

Avec le temps, l'expert en art devient meilleur pour détecter les peintures contrefaites, et le faussaire devient meilleur pour les imiter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EqkCwfjKAK8sKG7lY9AnOQ.png)

Comme nous le voyons, les DCGAN sont composés de deux réseaux de neurones profonds séparés qui se font concurrence.

* Le générateur est un faussaire qui essaie de produire des données apparemment réelles. Il n'a aucune idée de ce que sont les données réelles, mais il apprend à s'ajuster grâce aux commentaires de l'autre modèle.
* Le discriminateur est un inspecteur qui essaie de déterminer ce que sont les données contrefaites (en les comparant avec les données réelles), tout en essayant de ne pas déclencher de faux positifs sur les données réelles. Les résultats de sortie de ce modèle serviront à la rétropropagation du générateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aXSejGMGtQyyzXAqA6MtEw.png)
_Illustration DCGAN_

* Le générateur prend un vecteur de bruit aléatoire et génère une image.
* Cette image est alimentée dans le discriminateur, qui compare l'ensemble d'entraînement avec l'image générée.
* Le discriminateur retourne un nombre entre 0 (image fausse) et 1 (image réelle).

### Créons un DCGAN !

Maintenant, nous sommes prêts à créer notre IA.

Dans cette partie, nous allons nous concentrer sur les éléments principaux de notre modèle. Si vous voulez voir le code complet, utilisez le notebook [ici](https://github.com/simoninithomas/CatDCGAN/blob/master/Cat%20DCGAN.ipynb).

#### Entrées

Ici, nous créons les placeholders d'entrée : inputs_real pour le discriminateur et inputs_z pour le générateur.

Notez que nous utilisons deux taux d'apprentissage, un pour le générateur et un pour le discriminateur.

Les DCGAN sont très sensibles aux hyperparamètres, il est donc très important de les ajuster précisément.

#### Le discriminateur et le générateur

Nous utilisons `tf.variable_scope` pour deux raisons.

Premièrement, nous voulons nous assurer que tous les noms de variables commencent par generator / discriminator. Cela nous aidera plus tard lorsque nous entraînerons les deux réseaux.

Deuxièmement, nous voulons réutiliser ces réseaux avec différentes entrées :

* Pour le générateur : nous allons l'entraîner, mais aussi échantillonner des images fausses après l'entraînement.
* Pour le discriminateur : nous devons partager les variables entre les images d'entrée fausses et réelles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rAg13RBdRqt02voSsCUshg.png)
_Le discriminateur_

Maintenant, créons le discriminateur. Rappelez-vous, il prend en entrée une image réelle ou fausse et retourne un score.

Quelques remarques techniques :

* Le principe est de doubler la taille du filtre à chaque couche de convolution.
* Il n'est pas recommandé d'utiliser le sous-échantillonnage. Au lieu de cela, nous utilisons uniquement des couches de convolution à pas.
* Nous utilisons la normalisation par lots à chaque couche (sauf pour la couche d'entrée), car elle réduit le décalage de covariance. Pour plus d'informations, consultez cet [excellent article](https://towardsdatascience.com/batch-normalization-in-neural-networks-1ac91516821c).
* Nous utilisons Leaky ReLU comme fonction d'activation, car elle aide à éviter l'effet de gradient qui disparaît.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5QXJKtkNguNqc9whAcHJbA.png)

Ensuite, nous créons le générateur. Rappelez-vous, il prend en entrée un vecteur de bruit aléatoire (z) et retourne une fausse image, grâce aux couches de convolution transposées.

L'idée est que, à chaque couche, nous réduisons de moitié la taille du filtre et doublons la taille de l'image.

Il a été constaté que le générateur fonctionne mieux en utilisant tanh comme fonction d'activation de sortie.

#### Pertes du discriminateur et du générateur

Parce que nous entraînons le générateur et le discriminateur en même temps, nous devons calculer les pertes pour les deux réseaux.

Nous voulons que le discriminateur retourne 1 lorsqu'il "pense" qu'une image est réelle, et 0 pour les images fausses. Par conséquent, nous devons configurer les pertes pour refléter cela.

La perte du discriminateur est la somme des pertes pour les images réelles et fausses :

```
d_loss = d_loss_real + d_loss_fake
```

`d_loss_real` est la perte lorsque le discriminateur prédit qu'une image est fausse, alors qu'en fait c'était une image réelle. Elle est calculée comme suit :

* Utilisez `d_logits_real` et les labels sont tous à 1 (puisque toutes les données réelles sont réelles)
* `labels = tf.ones_like(tensor) * (1 - smooth)` Nous utilisons le lissage des labels : cela signifie réduire les labels un peu de 1.0 à 0.9 afin d'aider le discriminateur à mieux généraliser.

`d_loss_fake` est la perte lorsque le discriminateur prédit qu'une image est réelle, alors qu'en fait c'était une fausse image.

* Utilisez `d_logits_fake` et les labels sont tous à 0.

La perte du générateur utilise à nouveau les `d_logits_fake` du discriminateur. Cette fois, les labels sont tous à 1, car le générateur veut tromper le discriminateur.

#### Optimiseurs

Après avoir calculé les pertes, nous devons mettre à jour le générateur et le discriminateur séparément.

Pour ce faire, nous devons obtenir les variables pour chaque partie en utilisant `tf.trainable_variables()`. Cela crée une liste de toutes les variables que nous avons définies dans notre graphe.

#### Entraînement

Ici, nous implémentons la fonction d'entraînement.

L'idée est relativement simple :

* Nous sauvegardons le modèle toutes les cinq époques.
* Nous sauvegardons une image dans le dossier images toutes les dix batches entraînés.
* Nous affichons le `g_loss, d_loss` et l'image générée toutes les 15 époques. Cela est pour une raison simple : le notebook Jupyter peut buguer si trop d'images sont affichées.
* Ou, nous pouvons générer directement des images réelles en chargeant le modèle sauvegardé (cela vous fera économiser 20 heures d'entraînement).

#### Comment l'exécuter

Vous ne pouvez pas exécuter cela sur votre ordinateur personnel — sauf si vous avez vos propres GPUs ou êtes prêt à attendre peut-être 10 ans !

Au lieu de cela, vous devez utiliser des services de GPU cloud, tels que AWS ou FloydHub.

Personnellement, j'ai entraîné ce DCGAN pendant 20 heures avec Microsoft Azure et leur [Machine Virtuelle de Deep Learning](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft-ads.dsvm-deep-learning).

Avis de non-responsabilité : Je n'ai aucune relation commerciale avec Azure. J'ai simplement adoré leur excellent service client !

Si vous avez des difficultés à l'exécuter sur une machine virtuelle, suivez cet excellent article [ici](https://medium.com/@manikantayadunanda/setting-up-deeplearning-machine-and-fast-ai-on-azure-a22eb6bd6429).

C'est tout, j'espère que ce tutoriel a été utile !

Si vous avez amélioré le modèle, n'hésitez pas à faire une pull request.

![Image](https://cdn-media-1.freecodecamp.org/images/0*hGcVJaw3kTvzCC3h.)

Si vous avez des pensées, des commentaires, ou voulez me montrer vos résultats, n'hésitez pas à commenter ci-dessous ou à m'envoyer un email : hello@simoninithomas.com, ou tweetez-moi [@ThomasSimonini](https://twitter.com/ThomasSimonini).

Et si vous avez aimé mon article, veuillez cliquer sur le ? ci-dessous pour que d'autres personnes puissent le voir ici sur Medium. Et n'oubliez pas de me suivre !

Santé !