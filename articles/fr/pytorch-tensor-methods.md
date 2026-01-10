---
title: Méthodes de tenseurs PyTorch – Comment créer des tenseurs en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-03T17:00:26.000Z'
originalURL: https://freecodecamp.org/news/pytorch-tensor-methods
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc667ad49c47664ed828110.jpg
tags:
- name: Python
  slug: python
- name: pytorch
  slug: pytorch
- name: tensor
  slug: tensor
seo_title: Méthodes de tenseurs PyTorch – Comment créer des tenseurs en Python
seo_desc: 'By Srijan

  PyTorch is an open-source Python-based library. It provides high flexibility and
  speed while building, training, and deploying deep learning models.

  At its core, PyTorch involves operations involving tensors. A tensor is a number,
  vector, m...'
---

Par Srijan

PyTorch est une bibliothèque open-source basée sur Python. Elle offre une grande flexibilité et rapidité lors de la construction, de l'entraînement et du déploiement de modèles de deep learning.

Au cœur de PyTorch, on trouve des opérations impliquant des _tenseurs_. Un tenseur est un nombre, un vecteur, une matrice ou tout tableau à n dimensions.

Dans cet article, nous verrons différentes façons de créer des tenseurs en utilisant les méthodes (fonctions) de tenseurs PyTorch.

## Sujets que nous allons couvrir

* tensor
* zeros
* ones
* full
* arange
* linspace
* rand
* randint
* eye
* complex

### La méthode tensor()

Cette méthode retourne un tenseur lorsque des `data` lui sont passés. Les `data` peuvent être un scalaire, un tuple, une liste ou un tableau _NumPy_.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=76" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

Dans l'exemple ci-dessus, un tableau NumPy créé avec `np.arange()` a été passé à la méthode `tensor()`, résultant en un tenseur 1-D.

Nous pouvons créer un tenseur multidimensionnel en passant un tuple de tuples, une liste de listes ou un tableau NumPy multidimensionnel.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=77" title="Jovian Viewer" height="179" width="800" frameborder="0" scrolling="auto"></iframe>

Lorsque qu'un tuple ou une liste vide est passé à `tensor()`, il crée un tenseur vide.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=78" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode zeros()

Cette méthode retourne un tenseur où tous les éléments sont des zéros, de la `size` (forme) spécifiée. La `size` **peut** être donnée sous forme de tuple ou de liste ou ni l'un ni l'autre.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=4" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

Nous aurions pu passer `3, 2` à l'intérieur d'un tuple ou d'une liste également. Il est évident que passer des nombres négatifs ou un float entraînerait une erreur d'exécution.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=8" title="Jovian Viewer" height="318" width="800" frameborder="0" scrolling="auto"></iframe>

Passer un tuple vide ou une liste vide donne un tenseur de taille (dimension) 0, ayant 0 comme seul élément, dont le type de données est float.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=10" title="Jovian Viewer" height="205" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode ones()

Similaire à `zeros()`, `ones()` retourne un tenseur où tous les éléments sont 1, de la `size` (forme) spécifiée. La `size` **peut** être donnée sous forme de tuple ou de liste ou ni l'un ni l'autre.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/53&cellId=19" title="Jovian Viewer" height="400" width="800" frameborder="0" scrolling="auto"></iframe>

Comme `zeros()`, passer un tuple ou une liste vide donne un tenseur de dimension 0, ayant 1 comme seul élément, dont le type de données est float.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=23" title="Jovian Viewer" height="205" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode full()

Et si vous voulez que tous les éléments d'un tenseur soient égaux à une certaine valeur mais pas seulement 0 et 1 ? Peut-être 2.9 ?

`full()` retourne un tenseur de la forme donnée par l'argument `size`, avec tous ses éléments égaux à `fill_value`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=27" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

Ici, nous avons créé un tenseur de forme `3, 2` avec `fill_value` égal à 3. Ici encore, passer un tuple ou une liste vide crée un tenseur scalaire de dimension zéro.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=31" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

Lors de l'utilisation de `full`, il est **nécessaire** de donner `size` sous forme de tuple ou de liste.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=33" title="Jovian Viewer" height="444" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode arange()

Cette méthode retourne un tenseur 1-D, avec des éléments allant de `start` (inclus) à `end` (exclus) avec une différence commune `step`. La valeur par défaut pour `start` est 0 tandis que celle pour `step` est 1.

Les éléments du tenseur peuvent être considérés comme étant en **progression arithmétique**, avec `step` comme différence commune.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=37" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

Ici, nous avons créé un tenseur qui commence à 2 et va jusqu'à 20 avec un `step` (différence commune) de 2.

Les trois paramètres, `start`, `end` et `step`, peuvent être positifs, négatifs ou float.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=41" title="Jovian Viewer" height="297" width="800" frameborder="0" scrolling="auto"></iframe>

Lors du choix de `start`, `end` et `step`, nous devons nous assurer que `start` et `end` sont cohérents avec le signe de `step`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=41" title="Jovian Viewer" height="297" width="800" frameborder="0" scrolling="auto"></iframe>

Puisque `step` est défini comme -2, il n'y a aucun moyen que -42 puisse atteindre -22 (exclus). Par conséquent, cela donne une erreur.

### La méthode linspace()

Cette méthode retourne un tenseur 1-D, avec des éléments allant de `start` (inclus) à `end` (inclus). Cependant, contrairement à `arange()`, ici, `steps` n'est pas la différence commune mais le nombre d'éléments à inclure dans le tenseur.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=45" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

PyTorch décide automatiquement de la différence commune en fonction du nombre de `steps` donné.

Ne pas fournir de valeur pour `steps` est obsolète. Pour la _compatibilité ascendante_, ne pas fournir de valeur pour steps crée un tenseur avec **100** éléments. Selon la documentation officielle, dans une future version de PyTorch, l'omission de fournir une valeur pour steps générera une erreur d'exécution.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=47" title="Jovian Viewer" height="748" width="800" frameborder="0" scrolling="auto"></iframe>

Contrairement à `arange()`, `linspace` peut avoir un `start` supérieur à `end` puisque la différence commune est calculée automatiquement.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=49" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

Puisque `steps` ici n'est pas une différence commune, mais le nombre d'éléments, il ne peut être qu'un entier non négatif.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=51" title="Jovian Viewer" height="297" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode rand()

Cette méthode retourne un tenseur rempli de nombres aléatoires provenant d'une distribution uniforme sur l'intervalle 0 (inclus) à 1 (exclus). La forme est donnée par l'argument `size`. L'argument `size` peut être donné sous forme de tuple ou de liste ou ni l'un ni l'autre.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=55" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

Passer un tuple ou une liste vide crée un tenseur scalaire de dimension zéro.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=56" title="Jovian Viewer" height="158" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode randint()

Cette méthode retourne un tenseur rempli d'entiers aléatoires générés uniformément entre `low` (inclus) et `high` (exclus). La forme est donnée par l'argument `size`. La valeur par défaut pour `low` est 0.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=59" title="Jovian Viewer" height="242" width="800" frameborder="0" scrolling="auto"></iframe>

Lorsque seul un argument `int` est passé, `low` prend la valeur 0 par défaut, et `high` prend la valeur passée.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=60" title="Jovian Viewer" height="200" width="800" frameborder="0" scrolling="auto"></iframe>

L'argument `size` n'accepte qu'un tuple ou une liste. Un tuple ou une liste vide crée un tenseur de dimension zéro.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=62" title="Jovian Viewer" height="318" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode eye()

Cette méthode retourne un tenseur 2-D avec des uns sur la diagonale et des zéros ailleurs. Le nombre de lignes est donné par `n` et le nombre de colonnes par `m`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=65" title="Jovian Viewer" height="179" width="800" frameborder="0" scrolling="auto"></iframe>

La valeur par défaut pour `m` est la valeur de `n`. Lorsque seul `n` est passé, il crée un tenseur sous la forme d'une **matrice identité**. Une matrice identité a ses éléments diagonaux égaux à 1 et tous les autres égaux à 0.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=66" title="Jovian Viewer" height="242" width="800" frameborder="0" scrolling="auto"></iframe>

### La méthode complex()

Cette méthode retourne un tenseur complexe dont la partie réelle est égale à `real` et la partie imaginaire est égale à `imag`. `real` et `imag` sont tous deux des tenseurs.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=69" title="Jovian Viewer" height="363" width="800" frameborder="0" scrolling="auto"></iframe>

Le type de données des tenseurs `real` et `imag` doit être soit `float` soit `double`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=70" title="Jovian Viewer" height="523" width="800" frameborder="0" scrolling="auto"></iframe>

De plus, la `size` des deux tenseurs, `real` et `imag`, doit être la même, car les éléments correspondants des deux matrices forment un nombre complexe.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/different-ways-to-create-tensors/v/51&cellId=72" title="Jovian Viewer" height="499" width="800" frameborder="0" scrolling="auto"></iframe>

## Conclusion

Nous avons couvert dix différentes façons de créer des tenseurs en utilisant les méthodes PyTorch. Vous pouvez consulter la [documentation officielle](https://pytorch.org/docs/stable/torch.html) pour en savoir plus sur les autres méthodes PyTorch.

Vous pouvez cliquer [ici](https://jovian.ai/srijansrj5901/different-ways-to-create-tensors) pour accéder au notebook Jupyter où vous pouvez expérimenter avec ces méthodes.

Si vous souhaitez en apprendre davantage sur PyTorch, consultez [ce](https://jovian.ai/learn/deep-learning-with-pytorch-zero-to-gans) cours incroyable sur la chaîne [YouTube](https://www.youtube.com/watch?v=5ioMqzMRFgM&t=3s&ab_channel=freeCodeCamp.org) de freeCodeCamp.

Restez en sécurité !