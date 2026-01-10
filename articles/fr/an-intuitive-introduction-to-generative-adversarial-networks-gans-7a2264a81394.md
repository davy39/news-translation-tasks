---
title: Une introduction intuitive aux réseaux antagonistes génératifs (GANs)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-07T18:51:54.000Z'
originalURL: https://freecodecamp.org/news/an-intuitive-introduction-to-generative-adversarial-networks-gans-7a2264a81394
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KnwzxqjSy0tYwIUcD8TBGw.png
tags:
- name: Generative Adversarial
  slug: generative-adversarial
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Une introduction intuitive aux réseaux antagonistes génératifs (GANs)
seo_desc: 'By Thalles Silva

  Warm up

  Let’s say there’s a very cool party going on in your neighborhood that you really
  want to go to. But, there is a problem. To get into the party you need a special
  ticket — that was long sold out.

  Wait up! Isn’t this a Generat...'
---

Par Thalles Silva

### Échauffement

Imaginons qu'il y a une fête très cool dans votre quartier à laquelle vous voulez vraiment aller. Mais il y a un problème. Pour entrer à la fête, vous avez besoin d'un billet spécial — qui est depuis longtemps épuisé.

Attendez ! N'est-ce pas un article sur les réseaux antagonistes génératifs ? Oui, c'est le cas. Mais restez avec moi pour l'instant, cela en vaudra la peine.

D'accord, puisque les attentes sont très élevées, les organisateurs de la fête ont engagé une agence de sécurité qualifiée. Leur objectif principal est de ne laisser personne s'incruster à la fête. Pour ce faire, ils ont placé de nombreux gardes à l'entrée du lieu pour vérifier l'authenticité des billets de tout le monde.

Puisque vous n'avez aucun talent en arts martiaux, la seule façon de passer est de les tromper avec un billet contrefait **très convaincant**.

Il y a cependant un gros problème avec ce plan — vous n'avez jamais vraiment vu à quoi ressemble le billet.

Même si vous concevez un billet basé sur votre créativité, il est presque impossible de tromper les gardes à votre premier essai. De plus, vous ne pouvez pas montrer votre visage tant que vous n'avez pas une réplique très décente du passe de la fête.

Pour aider à résoudre le problème, vous décidez d'appeler votre ami Bob pour faire le travail à votre place.

La mission de Bob est très simple. Il essaiera d'entrer à la fête avec votre faux passe. S'il se fait refuser, il reviendra vers vous avec des conseils utiles sur l'apparence du billet.

Sur la base de ces commentaires, vous créez une nouvelle version du billet et la donnez à Bob, qui retourne essayer. Ce processus se répète jusqu'à ce que vous soyez capable de concevoir une réplique parfaite.

![Image](https://cdn-media-1.freecodecamp.org/images/MWonWZ43jU--EdOpHx9MSAar40jwlu9AWyp7)
_C'est une fête à ne pas manquer. J'ai en fait pris cette image sur un site de générateur de faux billets !_

Mettant de côté les 'petits trous' dans cette anecdote, c'est à peu près ainsi que fonctionnent les réseaux antagonistes génératifs (GANs).

De nos jours, la plupart des applications des GANs se situent dans le domaine de la vision par ordinateur. Certaines des applications incluent l'entraînement de [classifieurs semi-supervisés](https://towardsdatascience.com/semi-supervised-learning-with-gans-9f3cb128c5e), et la génération d'images haute résolution à partir de contreparties basse résolution.

Cet article fournit une introduction aux GANs avec une approche pratique du problème de génération d'images. Vous pouvez cloner le notebook pour cet article [ici](https://github.com/sthalles/blog-resources/blob/master/dcgan/DCGAN.ipynb).

### Réseaux Antagonistes Génératifs

![Image](https://cdn-media-1.freecodecamp.org/images/m41LtQVUf3uk5IOYlHLpPazxI3pWDwG8VEvU)
_Cadre de travail des réseaux antagonistes génératifs._

Les GANs sont des modèles génératifs conçus par [Goodfellow et al](https://arxiv.org/abs/1406.2661) en 2014. Dans une configuration GAN, deux fonctions différentiables, représentées par des réseaux de neurones, sont verrouillées dans un jeu. Les deux joueurs (le générateur et le discriminateur) ont des rôles différents dans ce cadre.

Le générateur essaie de produire des données qui proviennent d'une certaine distribution de probabilité. Cela serait vous essayant de reproduire les billets de la fête.

Le discriminateur agit comme un juge. Il décide si l'entrée provient du générateur ou de l'ensemble d'entraînement réel. Cela serait la sécurité de la fête comparant votre faux billet avec le vrai billet pour trouver des défauts dans votre conception.

![Image](https://cdn-media-1.freecodecamp.org/images/uXVB08yxpUJPR3c4ynliVWoEBRudjYXGn5QL)

![Image](https://cdn-media-1.freecodecamp.org/images/CDT1Y39GdN09qVKx3vyxgbciSZx6AXvXmKTC)
_Nous avons utilisé un réseau de convolution à 4 couches (pour le discriminateur et le générateur) avec normalisation par lots. Le modèle a été entraîné pour générer des images SVHNs et MNIST. Ci-dessus, les échantillons du générateur SVHN (à gauche) et MNIST (à droite) pendant l'entraînement._

En résumé, le jeu se déroule comme suit :

* Le générateur essaie de maximiser la probabilité que le discriminateur prenne ses entrées pour des données réelles.
* Et le discriminateur guide le générateur pour produire des images plus réalistes.

À l'équilibre parfait, le générateur capturerait la distribution générale des données d'entraînement. En conséquence, le discriminateur serait toujours incertain quant à savoir si ses entrées sont réelles ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/cKZw7BBTj3gfDCc8xiSKzf6PyHZkhHEVrFy3)
_Adapté de l'article DCGAN. Le réseau générateur implémenté ici. Notez l'absence de couches entièrement connectées et de pooling._

Dans l'[article DCGAN](https://arxiv.org/abs/1511.06434), les auteurs décrivent la combinaison de certaines techniques d'apprentissage profond comme clé pour l'entraînement des GANs. Ces techniques incluent : (i) le réseau entièrement convolutionnel et (ii) la normalisation par lots (BN).

La première met l'accent sur les _convolutions à pas_ (au lieu des couches de pooling) pour à la fois : augmenter et diminuer les dimensions spatiales des caractéristiques. Et la seconde normalise les vecteurs de caractéristiques pour avoir une moyenne nulle et une variance unitaire dans toutes les couches. Cela aide à stabiliser l'apprentissage et à traiter les problèmes de mauvaise initialisation des poids.

Sans plus tarder, plongeons dans les détails de l'implémentation et parlons davantage des GANs au fur et à mesure. Nous présentons une implémentation d'un réseau antagoniste génératif convolutionnel profond (DCGAN). Notre implémentation utilise Tensorflow et suit certaines pratiques décrites dans l'[article DCGAN](https://arxiv.org/abs/1511.06434).

### Générateur

Le réseau compte 4 couches convolutionnelles, toutes suivies par BN (sauf pour la couche de sortie) et des activations ReLU (unité linéaire rectifiée).

Il prend comme entrée un vecteur aléatoire _z_ (tiré d'une distribution normale). Après avoir redimensionné _z_ pour lui donner une forme 4D, nous l'alimentons dans le générateur qui commence une série de couches de suréchantillonnage.

Chaque couche de suréchantillonnage représente une opération de convolution transposée avec des pas de 2. Les convolutions transposées sont similaires aux convolutions régulières.

Typiquement, les convolutions régulières vont de couches larges et peu profondes à des couches plus étroites et plus profondes. Les convolutions transposées vont dans l'autre sens. Elles vont de couches profondes et étroites à des couches plus larges et moins profondes.

Le pas d'une opération de convolution transposée définit la taille de la couche de sortie. Avec un remplissage "same" et un pas de 2, les caractéristiques de sortie auront le double de la taille de la couche d'entrée.

Cela se produit parce que, chaque fois que nous déplaçons un pixel dans la couche d'entrée, nous déplaçons le noyau de convolution de deux pixels sur la couche de sortie. En d'autres termes, chaque pixel dans l'image d'entrée est utilisé pour dessiner un carré dans l'image de sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/pq4-PMV3zumFqi9lTaheNE6jc088pUJWu6YE)
_La convolution transposée d'un noyau 3x3 sur une entrée 2x2 avec un pas de 2 est équivalente à la convolution d'un noyau 3x3 sur une entrée 5x5 avec un pas de 2. En utilisant aucun remplissage "VALID", pour les deux._

En bref, le générateur commence avec ce vecteur d'entrée très profond mais étroit. Après chaque convolution transposée, _z_ devient plus large et moins profond. Toutes les convolutions transposées utilisent une taille de noyau de _5x5_ avec des profondeurs réduites de 512 jusqu'à 3 — représentant une image couleur RVB.

```
def transpose_conv2d(x, output_space):    return tf.layers.conv2d_transpose(x, output_space,       kernel_size=5, strides=2, padding='same',      kernel_initializer=tf.random_normal_initializer(mean=0.0,                                                      stddev=0.02))
```

La couche finale produit un tenseur _32x32x3_ — écrasé entre les valeurs de -1 et 1 par la fonction [Tangente Hyperbolique](https://reference.wolfram.com/language/ref/Tanh.html) (_tanh_).

Cette forme de sortie finale est définie par la taille des images d'entraînement. Dans ce cas, si l'entraînement est pour SVHN, le générateur produit des images _32x32x3_. Cependant, si l'entraînement est pour MNIST, il générerait une image en niveaux de gris _28x28_.

Enfin, notez que avant d'alimenter le vecteur d'entrée _z_ dans le générateur, nous devons le mettre à l'échelle dans l'intervalle de -1 à 1. C'est pour suivre le choix d'utiliser la fonction _tanh_.

```
def generator(z, output_dim, reuse=False, alpha=0.2, training=True):    """    Définit le réseau générateur    :param z: vecteur aléatoire d'entrée z    :param output_dim: dimension de sortie du réseau    :param reuse: Indique si les variables du modèle existant doivent être utilisées ou recréées    :param alpha: scalaire pour la fonction d'activation lrelu    :param training: Booléen pour contrôler les statistiques de normalisation par lots    :return: sortie du modèle    """    with tf.variable_scope('generator', reuse=reuse):        fc1 = dense(z, 4*4*512)        # Redimensionner pour commencer la pile de convolution        fc1 = tf.reshape(fc1, (-1, 4, 4, 512))        fc1 = batch_norm(fc1, training=training)        fc1 = tf.nn.relu(fc1)        t_conv1 = transpose_conv2d(fc1, 256)        t_conv1 = batch_norm(t_conv1, training=training)        t_conv1 = tf.nn.relu(t_conv1)        t_conv2 = transpose_conv2d(t_conv1, 128)        t_conv2 = batch_norm(t_conv2, training=training)        t_conv2 = tf.nn.relu(t_conv2)        logits = transpose_conv2d(t_conv2, output_dim)        out = tf.tanh(logits)        return out
```

### Discriminateur

Le discriminateur est également un CNN à 4 couches avec BN (sauf sa couche d'entrée) et des activations Leaky ReLU. De nombreuses fonctions d'activation fonctionneront bien avec cette architecture GAN de base. Cependant, les Leaky ReLUs sont très populaires car ils aident les gradients à circuler plus facilement à travers l'architecture.

Une fonction ReLU régulière fonctionne en tronquant les valeurs négatives à 0. Cela a pour effet de bloquer les gradients à circuler à travers le réseau. Au lieu que la fonction soit nulle, les Leaky ReLUs permettent à une petite valeur négative de passer. **C'est-à-dire, la fonction calcule la plus grande valeur entre les caractéristiques et un petit facteur**.

```
def lrelu(x, alpha=0.2):     # fonction d'activation non linéaire    return tf.maximum(alpha * x, x)
```

Les Leaky ReLUs représentent une tentative de résoudre le problème du _ReLU mourant_. Cette situation se produit lorsque les neurones se retrouvent dans un état où les unités _ReLU_ sortent toujours 0 pour toutes les entrées. Dans ces cas, les gradients sont complètement bloqués pour circuler à travers le réseau.

Cela est particulièrement important pour les GANs puisque la seule façon pour le générateur d'apprendre est de recevoir les gradients du discriminateur.

![Image](https://cdn-media-1.freecodecamp.org/images/2Gt22y40ECfoeueVhbdJxlSxN56ANsdz1Upt)

![Image](https://cdn-media-1.freecodecamp.org/images/jnloudDblWrrXgjam9wLcJSIXhCkQsb4WIhz)
_(gauche) ReLU, (droite) fonctions d'activation Leaky ReLU. Notez que les Leaky ReLUs permettent une petite pente lorsque x est négatif._

Le discriminateur commence par recevoir un tenseur d'image 32x32x3. Contrairement au générateur, le discriminateur effectue une série de _convolutions à pas 2_. Chacune réduit les dimensions spatiales du vecteur de caractéristiques de moitié, doublant également le nombre de filtres appris.

Enfin, le discriminateur doit produire des probabilités. Pour cela, nous utilisons la fonction d'activation _Sigmoïde Logistique_ sur les logits finaux.

```
def discriminator(x, reuse=False, alpha=0.2, training=True):    """    Définit le réseau discriminateur    :param x: entrée pour le réseau    :param reuse: Indique si les variables du modèle existant doivent être utilisées ou recréées    :param alpha: scalaire pour la fonction d'activation lrelu    :param training: Booléen pour contrôler les statistiques de normalisation par lots    :return: Un tuple de (probabilités sigmoïdes, logits)    """    with tf.variable_scope('discriminator', reuse=reuse):        # La couche d'entrée est 32x32x?        conv1 = conv2d(x, 64)        conv1 = lrelu(conv1, alpha)        conv2 = conv2d(conv1, 128)        conv2 = batch_norm(conv2, training=training)        conv2 = lrelu(conv2, alpha)        conv3 = conv2d(conv2, 256)        conv3 = batch_norm(conv3, training=training)        conv3 = lrelu(conv3, alpha)        # Aplatir        flat = tf.reshape(conv3, (-1, 4*4*256))        logits = dense(flat, 1)        out = tf.sigmoid(logits)        return out, logits
```

Notez que dans ce cadre, le discriminateur agit comme un classifieur binaire régulier. La moitié du temps, il reçoit des images de l'ensemble d'entraînement et l'autre moitié du générateur.

Revenons à notre aventure, pour reproduire le billet de la fête, la seule source d'information que vous aviez était le retour de notre ami Bob. En d'autres termes, la qualité du retour que Bob vous a fourni à chaque essai était essentielle pour accomplir la tâche.

De la même manière, chaque fois que le discriminateur remarque une différence entre les images réelles et fausses, il envoie un signal au générateur. Ce signal est le gradient qui circule en arrière du discriminateur vers le générateur. En le recevant, le générateur est capable d'ajuster ses paramètres pour se rapprocher de la vraie distribution des données.

**C'est ainsi que le discriminateur est important. En fait, le générateur sera aussi bon à produire des données que le discriminateur est bon à les distinguer.**

### Pertes

Maintenant, décrivons la partie la plus délicate de cette architecture — les pertes. Tout d'abord, nous savons que le discriminateur reçoit des images à la fois de l'ensemble d'entraînement et du générateur.

Nous voulons que le discriminateur soit capable de distinguer les images réelles des images fausses. Chaque fois que nous exécutons un mini-lot à travers le discriminateur, nous obtenons des logits. Ce sont les valeurs non mises à l'échelle du modèle.

Cependant, nous pouvons diviser les mini-lots que le discriminateur reçoit en deux types. Le premier, composé uniquement d'images réelles provenant de l'ensemble d'entraînement et le second, avec uniquement des images fausses — celles créées par le générateur.

```
def model_loss(input_real, input_z, output_dim, alpha=0.2, smooth=0.1):    """    Obtenir la perte pour le discriminateur et le générateur    :param input_real: Images de l'ensemble de données réel    :param input_z: vecteur aléatoire z    :param out_channel_dim: Le nombre de canaux dans l'image de sortie    :param smooth: scalaire de lissage des étiquettes    :return: Un tuple de (perte du discriminateur, perte du générateur)    """    g_model = generator(input_z, output_dim, alpha=alpha)    d_model_real, d_logits_real = discriminator(input_real, alpha=alpha)    d_model_fake, d_logits_fake = discriminator(g_model, reuse=True, alpha=alpha)    # pour les images réelles, nous voulons qu'elles soient classées comme positives,      # donc nous voulons que leurs étiquettes soient toutes des uns.    # notez ici que nous utilisons le lissage des étiquettes pour aider le discriminateur à mieux généraliser.    # Le lissage des étiquettes fonctionne en évitant que le classifieur ne fasse des prédictions extrêmes lors de l'extrapolation.    d_loss_real = tf.reduce_mean(        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_real, labels=tf.ones_like(d_logits_real) * (1 - smooth)))    # pour les fausses images produites par le générateur, nous voulons que le discriminateur les classe comme fausses images,    # donc nous définissons leurs étiquettes à être toutes des zéros.    d_loss_fake = tf.reduce_mean(        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake, labels=tf.zeros_like(d_model_fake)))    # puisque le générateur veut que le discriminateur produise des 1 pour ses images, il utilise les logits du discriminateur pour les    # fausses images et leur attribue des étiquettes de 1.    g_loss = tf.reduce_mean(        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake, labels=tf.ones_like(d_model_fake)))    d_loss = d_loss_real + d_loss_fake    return d_loss, g_loss
```

Parce que les deux réseaux s'entraînent en même temps, les GANs ont également besoin de deux optimiseurs. Chacun pour minimiser les fonctions de perte du discriminateur et du générateur respectivement.

Nous voulons que le discriminateur produise des probabilités proches de 1 pour les images réelles et proches de 0 pour les images fausses. Pour ce faire, le discriminateur a besoin de deux pertes. Par conséquent, la perte totale pour le discriminateur est la somme de ces deux pertes partielles. **Une pour maximiser les probabilités pour les images réelles et une autre pour minimiser la probabilité des images fausses.**

![Image](https://cdn-media-1.freecodecamp.org/images/83aIMU9F35K9jffKDi8IdiV0E2Amhc4GHPNZ)
_Comparaison des images réelles (gauche) et générées (droite) de l'ensemble de données SVHN. Bien que certaines images semblent floues et que d'autres soient difficiles à reconnaître, il est notable que la distribution des données a été capturée par le modèle._

Au début de l'entraînement, deux situations intéressantes se produisent. Premièrement, le générateur ne sait pas comment créer des images qui ressemblent à celles de l'ensemble d'entraînement. Et deuxièmement, le discriminateur ne sait pas comment catégoriser les images qu'il reçoit comme réelles ou fausses.

En conséquence, le discriminateur reçoit deux types de lots très distincts. L'un, composé de vraies images de l'ensemble d'entraînement et l'autre contenant des signaux très bruyants. Au fur et à mesure que l'entraînement progresse, le générateur commence à produire des images qui ressemblent de plus en plus aux images de l'ensemble d'entraînement. Cela se produit parce que le générateur s'entraîne pour apprendre la distribution des données qui compose les images de l'ensemble d'entraînement.

En même temps, le discriminateur commence à devenir très bon pour classer les échantillons comme réels ou faux. En conséquence, les deux types de mini-lots commencent à se ressembler, en structure, l'un à l'autre. **Cela, en conséquence, rend le discriminateur incapable d'identifier les images comme réelles ou fausses.**

Pour les pertes, nous utilisons la cross-entropy vanilla avec Adam comme un bon choix pour l'optimiseur.

![Image](https://cdn-media-1.freecodecamp.org/images/ZxkH9WMdASNODE3rxwu9keAnpZTCjYsuAgY0)
_Comparaison des images réelles (gauche) et générées (droite) de l'ensemble de données MNIST. Parce que les images MNIST ont une structure de données plus simple, le modèle a été capable de produire des échantillons plus réalistes par rapport aux SVHNs._

### Conclusion

Les GANs sont l'un des sujets les plus chauds dans le domaine de l'apprentissage automatique en ce moment. Ces modèles ont le potentiel de débloquer des méthodes d'apprentissage non supervisé qui élargiraient le ML à de nouveaux horizons.

Depuis leur création, les chercheurs ont développé de nombreuses techniques pour entraîner les GANs. Dans Improved Techniques for Training GANs, les auteurs décrivent des techniques de pointe pour la génération d'images et l'apprentissage semi-supervisé.

Si vous êtes curieux d'approfondir ces sujets, je vous recommande de lire [Generative Models](https://blog.openai.com/generative-models/#gan).

De plus, consultez :

[**Plongez tête la première dans les GANs avancés : exploration de l'auto-attention et de la norme spectrale**](https://medium.freecodecamp.org/dive-head-first-into-advanced-gans-exploring-self-attention-and-spectral-norm-d2f7cdb55ede)  
[_Récemment, les modèles génératifs attirent beaucoup d'attention. Une grande partie de cela vient des réseaux antagonistes génératifs..._medium.freecodecamp.org](https://medium.freecodecamp.org/dive-head-first-into-advanced-gans-exploring-self-attention-and-spectral-norm-d2f7cdb55ede)[**Apprentissage semi-supervisé avec les réseaux antagonistes génératifs (GANs)**](https://towardsdatascience.com/semi-supervised-learning-with-gans-9f3cb128c5e)  
[_Si vous avez déjà entendu parler ou étudié l'apprentissage profond, vous avez probablement entendu parler de MNIST, SVHN, ImageNet, PascalVoc et autres..._towardsdatascience.com](https://towardsdatascience.com/semi-supervised-learning-with-gans-9f3cb128c5e)

Et si vous avez besoin de plus, voici mon [blog sur l'apprentissage profond](https://sthalles.github.io).

**Profitez-en, et merci pour la lecture !**

![Image](https://cdn-media-1.freecodecamp.org/images/D5dMss3-vGNt79fV9qDQwUIuRToVFqmPZKaY)

Crédits à [Sam Williams](https://www.freecodecamp.org/news/an-intuitive-introduction-to-generative-adversarial-networks-gans-7a2264a81394/undefined) pour ce superbe gif "clap" ! Consultez-le dans [son article](https://medium.freecodecamp.org/want-more-claps-and-followers-how-to-make-a-clap-me-gif-in-5-minutes-db85a24950f6).