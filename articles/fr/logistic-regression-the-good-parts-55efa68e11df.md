---
title: 'Régression logistique : les bons côtés'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T16:43:20.000Z'
originalURL: https://freecodecamp.org/news/logistic-regression-the-good-parts-55efa68e11df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KtyUBxGIhq99V1Wm11CXlw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: 'Régression logistique : les bons côtés'
seo_desc: 'By Thalles Silva

  In the last post, we tackled the problem of Machine Learning classification through
  the lens of dimensionality reduction. We saw how Fisher’s Linear Discriminant can
  project data points from higher to smaller dimensions. The projecti...'
---

Par Thalles Silva

Dans le dernier article, nous avons abordé le problème de la [classification en apprentissage automatique à travers le prisme de la réduction de dimensionnalité](https://medium.freecodecamp.org/an-illustrative-introduction-to-fishers-linear-discriminant-9484efee15ac?source=friends_link&sk=842b291dc6304d477b278c7aa622ec23). Nous avons vu comment le discriminant linéaire de Fisher peut projeter des points de données de dimensions supérieures à des dimensions plus petites. La projection suit deux principes.

* Elle maximise la variance inter-classe.
* Elle minimise la variance intra-classe.

Bien que la méthode de Fisher ne soit pas (en essence) un discriminant, nous en avons construit un en modélisant une distribution conditionnelle de classe à l'aide d'une gaussienne. D'abord, nous avons trouvé les probabilités a priori des classes p(Ck). Ensuite, nous avons utilisé le théorème de Bayes pour trouver les probabilités a posteriori des classes p(Ck|x). Ici, x est le vecteur d'entrée et Ck est l'étiquette pour la classe k.

En bref, nous pouvons catégoriser les modèles de ML en fonction de la manière dont ils classent les données. Il existe deux types : les méthodes génératives et discriminatives.

Les méthodes génératives apprennent explicitement les probabilités a posteriori des classes. À l'inverse, les algorithmes discriminatifs apprennent directement les probabilités a posteriori des classes.

Intuitivement, cela a une belle interprétation géométrique. Pour chaque classe, les modèles génératifs cherchent à trouver une représentation probabiliste des données. Au contraire, les algorithmes discriminatifs se concentrent sur la séparation des données par des frontières de décision.

En d'autres termes, les modèles génératifs tentent d'expliquer les données en construisant un modèle statistique pour chaque classe.

D'un autre côté, le but d'un algorithme discriminatif est de trouver une frontière de décision optimale qui sépare les classes. Ainsi, tant qu'il y a une surface de décision, de tels modèles ne se soucient pas des distributions des données.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/0_Wd4CdfPAq3m_Sw00.png)

Prenons un problème de classification binaire comme exemple. Étant donné un vecteur d'entrée **x**, nous devons décider à quelle classe Ck, **x** est le plus susceptible d'appartenir. Pour prendre cette décision, les deux types d'algorithmes de ML ont besoin d'un moyen de calculer la probabilité a posteriori p(Ck|x) à partir des données d'entraînement.

Pour Fisher, nous avons explicitement appris les probabilités a posteriori des classes en utilisant une gaussienne. Une fois que nous l'avons trouvée, nous avons utilisé la théorie de la décision pour déterminer l'appartenance à une classe pour **x**.

Pour un modèle discriminatif, la probabilité a posteriori p(Ck|x) sera directement dérivée. Dans ce cas, une fois que nous avons la probabilité a posteriori, nous pouvons utiliser la théorie de la décision et assigner **x** à la classe la plus probable.

## Régression logistique

_Avant de commencer, assurez-vous de suivre avec ces_ [_Colab notebooks_](https://github.com/sthalles/logistic-regression).

La régression logistique est probablement le modèle discriminatif le plus connu. En tant que tel, elle dérive implicitement la probabilité a posteriori de la classe p(Ck|**x**).

Pour la classification binaire, les probabilités a posteriori sont données par la fonction sigmoïde σ appliquée sur une combinaison linéaire des entrées _φ._

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_4bD360SiUX3NvZ-SIEW1rg.png)
_Fonction sigmoïde_

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_1F8NRd8spsu1u_z0A4Rozw.png)
_Pour la classification binaire, les probabilités a posteriori sont représentées par la fonction sigmoïde logistique._

De même, pour les problèmes multiclasses, nous pouvons estimer la probabilité a posteriori en utilisant la fonction softmax. Comme la sigmoïde, softmax normalise un vecteur donné en probabilités — valeurs entre 0 et 1.

Commençons par le cas de la classification binaire.

## Régression logistique binaire

Pour un vecteur de caractéristiques d'entrée de dimension M, la régression logistique doit apprendre M paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_lIYPmMb2KjTAnZOLcKY-rw.png)
_Paramètres entraînables pour la régression logistique binaire._

Prenons le jeu de données SVHN comme exemple. Chaque image RGB a une forme de 32x32x3. Ainsi, la régression logistique doit apprendre 32x32x3=3072 paramètres.

Pour trouver ces paramètres, nous optimisons généralement la fonction d'erreur de l'entropie croisée.

L'entropie croisée mesure à quel point les prédictions du modèle sont éloignées des étiquettes. Elle augmente lorsque les valeurs prédites s'écartent des valeurs réelles et diminue sinon.

En supposant que les valeurs cibles **t** soient soit 0 soit 1, l'entropie croisée est définie comme :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_d8tU436ojPNjJOC8-T9Zmw.png)

Ici, **N** désigne le nombre total d'instances dans le jeu de données et **yᵢ** sont les probabilités du modèle.

L'entropie croisée compare 2 distributions de probabilités. Pour cette raison, il est important de noter que la sortie de la régression logistique est interprétée comme des probabilités — même pendant l'apprentissage.

En prenant la dérivée de l'entropie croisée par rapport au vecteur de poids **w**, nous obtenons le gradient.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_A7d_tcGiRph9FzhqoSwT4g.png)
_Le gradient de l'entropie croisée_

Notez que pour calculer cette dérivée, nous avons besoin de la dérivée de la fonction sigmoïde par rapport aux poids **w**. Heureusement, une belle propriété de la sigmoïde est que nous pouvons exprimer sa dérivée en termes d'elle-même.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_dzZwMfiCdsj278OkpRFmUw.png)
_La dérivée de la fonction sigmoïde._

Le gradient est une fonction à valeurs vectorielles. En fait, le gradient est une transformation linéaire qui mappe les vecteurs d'entrée à d'autres vecteurs de même forme.

Le gradient capture la dérivée d'une fonction multivariée entière. Chacune de ses valeurs désigne la direction dans laquelle nous pouvons changer un poids spécifique afin que nous puissions atteindre le point maximum d'une fonction. Ainsi, le gradient représente la direction de la pente la plus raide.

## Régression Softmax

Pour la classification multiclasse, seules quelques choses changent. Maintenant, nous pouvons modéliser les probabilités a posteriori en utilisant une fonction softmax.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_lGqGh8Ylp8guk5qawiDtQQ.png)
_Ici, ak sont les activations._

Puisque la régression logistique traite ses prédictions comme des probabilités, nous devons changer la manière dont nous représentons nos étiquettes. Jusqu'à présent, le vecteur cible/étiquette est généralement représenté comme un vecteur d'entiers. Chaque valeur représentant une classe différente. Si nous voulons qu'elles soient des probabilités de valeur égale, elles doivent être comprises entre 0 et 1. Pour ce faire, nous pouvons changer leur représentation en one-hot-encodings.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/0_DcT6ulzhWBZVFrKO.png)
_Représentation one-hot-encoding._

Cette fois, pour des entrées avec M caractéristiques et K classes différentes, la régression logistique apprend MxK paramètres. Nous pouvons le voir comme une matrice.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_I98p3Bbe7AwceWmmI2C3Gg.png)
_Paramètres entraînables pour la régression logistique multiclasse._

Maintenant, nous pouvons procéder de manière similaire au cas de la classification binaire. D'abord, nous prenons la dérivée de la softmax par rapport aux activations. Ensuite, le logarithme négatif de la vraisemblance nous donne la fonction d'entropie croisée pour la classification multiclasse.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_6jM-fYPRSAqGVFYFHMO5AQ.png)

En pratique, l'entropie croisée mesure la distance entre deux vecteurs de probabilités. L'un, qui provient de la **softmax**. Et un second contenant les représentations one-hot-encoding des valeurs cibles réelles.

Notez la différence entre les fonctions d'erreur utilisées pour la classification binaire et multiclasse. En réalité, elles sont vraiment la même chose.

L'entropie croisée binaire traite les cibles comme des scalaires. Elles prennent soit 0 soit 1. Pour la classification multiclasse, les cibles sont représentées comme des vecteurs one-hot-encodés.

Enfin, nous prenons le gradient de la fonction d'erreur par rapport aux poids **w** et obtenons les vecteurs de gradient suivants.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_rEAr_JYpSNtyEyi7Prkf0g.png)

## Moindres carrés réitérés repondérés

Contrairement à la régression linéaire, la régression logistique n'a pas de solution sous forme fermée. En d'autres termes, pour la régression linéaire, nous pouvons résoudre pour un point de gradient égal à 0 avec l'équation suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_lk00NIv6naO4lZfJuJDwqw.png)
_Solution sous forme fermée pour la régression linéaire._

Pour la régression logistique, une telle équation sous forme fermée n'existe pas. Grâce à la non-linéarité que nous appliquons sur la combinaison linéaire des entrées.

Cependant, la relation entre la fonction de perte et les paramètres **w** nous donne toujours une **fonction d'erreur concave**. Ainsi, nous pouvons être assurés qu'il n'y a qu'un seul minimum unique sur la surface d'erreur.

En conséquence, nous pouvons la résoudre en utilisant une technique itérative telle que la descente de gradient ou Newton-Raphson.

Si nous choisissons la descente de gradient, nous avons tout prêt.

* Il suffit de suivre la direction opposée du gradient.

En anglais simple, la direction de la descente la plus raide. Ainsi, nous pouvons mettre à jour itérativement les poids **w** comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_Ai7Tf1405tpXdgvVGeoljQ.png)

Cependant, nous pouvons faire un peu mieux.

La descente de gradient offre la direction de la descente la plus raide vers le prochain point critique. Et le taux d'apprentissage contrôle la longueur (magnitude) du pas que nous faisons dans cette direction. Jetez un coup d'œil à l'image suivante cependant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_tg8F9vtZoqymq622tvUYOw.png)
_Image basée sur le livre [Deep Learning](https://www.deeplearningbook.org/contents/numerical.html" rel="noopener nofollow) de Ian Goodfellow, Yoshua Bengio et Aaron Courville._

Surtout en (c), selon la magnitude du pas que nous faisons, nous pourrions faire en sorte que notre fonction de perte augmente plutôt. Pour éviter cet écueil, nous tirons parti des informations données par la deuxième dérivée.

En pratique, au lieu de prendre uniquement la dérivée de l'entropie croisée, nous prenons également la dérivée de sa dérivée. La deuxième dérivée, décrite par f''(x), donne des informations sur la courbure d'une fonction.

Intuitivement, si :

* f''(x)=0, alors il n'y a pas de courbure.
* f''(x)<0, cela signifie que la fonction courbe vers le bas.
* f''(x)>0, il y a une courbure vers le haut dans la fonction.

Avec ces informations, l'étape de mise à jour, pour minimiser l'entropie croisée, prend la forme de :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_MH6k1TaL5f1gxLxszXdJHA.png)

Cette équation de mise à jour est appelée Newton-Raphson.

Notez qu'elle multiplie l'inverse de la matrice **H⁻¹** par le gradient. **H**, ou le Hessien, stocke les deuxièmes dérivées de l'entropie croisée par rapport aux poids **w**.

Plongeons maintenant dans le code.

Prenons cet exemple de jeu de données jouet.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_Zh0y1YsOM3prEYQreP7hHg.png)

Il y a 210 points dans ce système de coordonnées 2D avec 3 classes : cercles bleus, rouges et verts. Puisque le nombre de classes est supérieur à 2, nous pouvons utiliser la régression logistique Softmax.

D'abord, pour introduire les variables de biais dans notre modèle, nous pouvons effectuer une transformation simple appelée : fonction de base fixe. Cela se fait simplement en ajoutant une colonne remplie de 1 aux entrées. Pour la classification binaire, cela fait que la valeur de poids correspondante w₀ joue le rôle du biais. Pour le multiclasse, la première colonne de la matrice de poids agit comme les biais.

Ensuite, nous pouvons créer un objet de régression logistique.

```py
clf = LogisticRegression(fit_intercept=True, method="newton")
clf.fit(x_train,y_train,iterations=10)
print("Test acc:",clf.score(x_test,y_test))
```

Suivant l'API basée sur sklearn, nous pouvons **ajuster** et **évaluer** le modèle :

```py
for i in range(iterations):
  logits = self._forward(X)

  if self.method == 'newton':
    # calculer le hessien
    for i in range(k):
      for j in range(k):
        r = np.multiply(logits[:,i],((i==j)-logits[:,j]))  ## r a une valeur négative, donc ne peut pas utiliser sqrt
        HT[:,i,:,j] = np.dot(np.multiply(X.T,r),X) # 4.110      
    H = np.reshape(HT,(dk,dk))
    
  # calculer le gradient de l'entropie croisée
  G = np.dot(X.T,(logits-y))

  if self.method == 'newton':
    # Mise à jour de Newton
    self.W = self.W.reshape(-1) - np.dot(pinv(H), G.reshape(-1)) # 4.92
    self.W = np.reshape(self.W,W_shape)
  else:
    # suivre le gradient avec GD
    self.W = self.W - self.learning_rate * G
```

Notez que nous pouvons choisir entre les règles de mise à jour de Newton et de la descente de gradient. Bien que la méthode de Newton tende à converger plus rapidement, elle doit calculer et stocker un Hessien complet à chaque itération. De plus, le Hessien doit être inversible — pour la mise à jour des paramètres.

Pour qu'une matrice soit inversible, il y a certaines contraintes qui doivent être vraies.

Premièrement, **H** doit être une matrice carrée. Deuxièmement, les colonnes de **H** doivent être linéairement indépendantes. Cela signifie que pour toute colonne **_i_** de **H**, **_i_** ne peut pas être représentée comme une combinaison linéaire de toute autre colonne **_j_**.

Cela revient à dire que les colonnes de **H** couvrent le système de coordonnées. Ou que le déterminant de **H** est non nul.

Puisque pour les matrices vraiment grandes, ces contraintes ne sont probablement pas respectées, nous pouvons utiliser des techniques de pseudo-inverse ici. C'est ce que fait la fonction **_pinv(H)_** dans le code ci-dessus.

Même si pour les petits jeux de données, cela peut ne pas poser de problème, le Hessien tend à croître à mesure que le nombre de caractéristiques et de classes augmente. Pour avoir une idée, en utilisant des entrées avec M caractéristiques et un jeu de données avec K classes. Le Hessien complet a une forme [M*K, M*K] ; ce qui pour cet exemple signifie : [9x9] — rappelez-vous, nous avons ajouté une nouvelle colonne de caractéristiques aux entrées.

Pour le jeu de données CIFAR-10, chaque image RGB a une forme de 32x32x3. Cela signifie stocker et inverser une matrice carrée de forme [30720x30720]. En utilisant une précision de 32 bits, le Hessien nécessite 3,775 Go (gigaoctets).

Pour conclure, jetez un coup d'œil au modèle ajusté en utilisant le jeu de données jouet et la méthode de Newton. Les croix sont les données de test.

Profitez.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_l2e41fUAuX5PVGw1h9uwNQ.png)
_Frontières de décision pour la régression logistique utilisant la méthode de Newton. Les cercles représentent les données d'entraînement et les croix les instances de test._

En résumé, les modèles génératifs sont une classe d'algorithmes de ML qui apprennent explicitement les probabilités des classes.

* Ils fonctionnent généralement bien avec moins d'exemples d'entraînement.
* Ils peuvent gérer les données manquantes.
* Et peuvent être utilisés pour l'apprentissage supervisé et non supervisé.

Les modèles discriminatifs apprennent implicitement les probabilités des classes.

* En général, ils nécessitent plus de données étiquetées.
* Ils ont souvent moins d'hypothèses et moins de paramètres.
* Mais ne peuvent être utilisés que pour l'entraînement supervisé.

Pour la classification binaire, la régression logistique utilise la fonction sigmoïde pour représenter les probabilités a posteriori. Pour la classification multiclasse, elle utilise softmax.

Pour plus de choses cool sur l'apprentissage automatique, jetez un coup d'œil à :

* [Une introduction au réglage des hyper-paramètres en haute dimension](https://www.freecodecamp.org/news/an-introduction-to-high-dimensional-hyper-parameter-tuning-df5c0106e5a4/)
* [Une introduction illustrative au discriminant linéaire de Fisher](https://www.freecodecamp.org/news/an-illustrative-introduction-to-fishers-linear-discriminant-9484efee15ac/)

## Références

Christopher M. Bishop. 2006. Pattern Recognition and Machine Learning (Information Science and Statistics). Springer-Verlag, Berlin, Heidelberg.

**Merci d'avoir lu.**