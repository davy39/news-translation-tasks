---
title: Champs de modèle Django – Cas d'utilisation courants et leur fonctionnement
subtitle: ''
author: Victoria (Burah) Poromon
co_authors: []
series: null
date: '2023-11-23T00:03:28.000Z'
originalURL: https://freecodecamp.org/news/common-django-model-fields-and-their-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Django-models-article-cover.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Champs de modèle Django – Cas d'utilisation courants et leur fonctionnement
seo_desc: 'Django model fields define the structure of a database within a Django
  web application. Using this essential component will keep your work organized and
  help you make fewer mistakes in your code.

  This article will discuss some common Django model fie...'
---

Les champs de modèle Django définissent la structure d'une base de données au sein d'une application web Django. L'utilisation de ce composant essentiel gardera votre travail organisé et vous aidera à faire moins d'erreurs dans votre code.

Cet article discutera de certains champs de modèle Django courants et de la manière de les utiliser dans votre code.

Pour tirer le meilleur parti de cet article, vous devriez avoir au moins une connaissance de base de Django et comprendre comment fonctionne la programmation orientée objet.

## Qu'est-ce qu'un champ de modèle ?

Un champ de modèle est un type de données qui stocke un type spécifique de données. Chaque champ de modèle représente des données spécifiques, telles que des nombres, des dates, des textes, ou même des relations avec d'autres modèles.

Les champs contiennent des validations intégrées pour des types de données spécifiques. Par conséquent, un IntegerField n'acceptera pas, par exemple, des lettres de l'alphabet. Chaque champ est spécifique à son usage.

## Champs de modèle Django courants

Vous devez importer le module models de la base de données Django pour utiliser les champs Django. Cela garantira que le type de données que vous stockez dans votre colonne de base de données est bien défini.

Cette section discutera des types de champs de modèle courants de Django et de la manière de les utiliser.

### Le champ de modèle `CharField`

Ce champ stocke des caractères ou des chaînes de texte de longueur courte à moyenne, ce qui le rend adapté pour stocker un attribut comme un nom. `CharField` possède un paramètre `max_length` que vous devez spécifier chaque fois que vous utilisez le champ. Mais lorsque vous ne spécifiez pas la longueur du champ, elle est par défaut de 255 caractères.

Voici un exemple de la manière d'utiliser `CharField` dans votre code :

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
```

Dans l'extrait de code ci-dessus, `max_length` définit la longueur maximale de l'attribut 'name' à 20 caractères.

### Le champ de modèle `DateField`

Ce champ stocke les dates dans votre modèle et possède deux paramètres optionnels (`auto_now` et `auto_now_add`). Le paramètre `auto_now` définit la date chaque fois que vous modifiez ou mettez à jour les données, tandis que `auto_now_add` définit la date du champ uniquement lorsque vous créez les données.

Voici un exemple de la manière dont vous pouvez utiliser le champ de date :

```python
from django.db import models

class Product(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
```

Dans l'extrait de code ci-dessus, le module produit possède deux `DateField`. L'un définit la date lorsque vous créez les données, et l'autre définit la date lorsque vous mettez à jour les données.

### Le champ de modèle `DateTimeField`

Ce champ stocke les informations de date et d'heure dans un modèle. Tout comme le `DateField`, le `DateTimeField` possède également deux paramètres (`auto_now` et `auto_now_add`). Ils ont la même fonction, sauf que ce champ définit également l'heure.

### Le champ de modèle `DecimalField`

Ce champ stocke les nombres décimaux dans une base de données. Vous pouvez l'utiliser pour stocker des valeurs numériques comme le prix, le poids et la hauteur.

Il possède deux paramètres que vous devez spécifier lors de son utilisation. Ils incluent :

* `max_digit` : Il s'agit du nombre total de chiffres autorisés dans le nombre. Il inclut tous les chiffres à gauche et à droite du point décimal. Ce nombre doit être supérieur ou égal à `decimal_places`.
* `decimal_places` : Il s'agit du nombre de chiffres du côté droit du point décimal.

Voici un exemple de la manière de stocker des données dans le DecimalField :

```python
from django.db import models

class Product(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

Dans l'extrait de code ci-dessus, le nombre de chiffres des deux côtés du point décimal est de 6. En même temps, le nombre de décimales est égal à 2. Par conséquent, votre programme ne peut stocker que des prix comme 2100,00 $.

### Le champ de modèle `BooleanField`

Ce champ stocke des valeurs booléennes. Vous pouvez effectuer des opérations binaires simples avec ce champ.

Par exemple :

```python
from django.db import models

class Product(models.Model):
    add_to_cart = models.BooleanField(default=False)
```

Dans le modèle de produit ci-dessus, le `BooleanField` est défini à une valeur par défaut de False, ce qui signifie que les produits sont hors de votre panier par défaut. Cela signifie également que vous pouvez cliquer pour ajouter ou retirer un produit de votre panier à tout moment.

### Le champ de modèle `EmailField`

Le `EmailField` est une forme spécialisée de `CharField` qui stocke les adresses e-mail. Lorsque vous utilisez ce champ, il s'assure que la valeur que vous fournissez est une adresse e-mail valide. Sinon, il retourne une erreur.

Voici comment utiliser ce champ dans votre projet :

```python
from django.db import models

class Customer(models.Model):
    email = models.EmailField()
```

Le programme ci-dessus garantit que votre client entre une adresse e-mail valide dans la base de données.

### Le champ de modèle `TextField`

Un `TextField` stocke de grandes quantités de données textuelles. Ce champ est utile lorsque vous stockez des données textuelles trop longues pour un `CharField`. Il peut gérer des textes longs comme des paragraphes et même des documents entiers.

Voici un exemple de la manière dont vous pouvez utiliser ce champ :

```python
from django.db import models

class Product(models.Model):
    comments = models.TextField()
```

Dans l'exemple ci-dessus, le modèle Product possède un `TextField` nommé 'Comments'. Ce champ stockera les commentaires des clients sur les produits.

### Le champ de modèle `IntegerField`

Ce champ stocke des valeurs entières sous forme de nombres entiers. Ces valeurs vont de -2147483648 à 0 pour les entiers négatifs et de 0 à 2147483647 pour les entiers positifs. Il peut donc stocker n'importe quelle valeur entière, positive ou négative.

Selon les besoins de votre projet, vous pouvez contraindre ce champ à ne stocker qu'une valeur positive ou négative en utilisant respectivement `PositiveIntegerField` ou `NegativeIntegerField`.

Voici un exemple de la manière de stocker des données dans le IntegerField :

```python
from django.db import models

class Product(models.Model):
    available_quantity = models.PositiveIntegerField()
```

Dans cet exemple, le modèle possède un champ qui stocke le nombre de produits disponibles. Le `PositiveIntegerField` garantit que la quantité disponible est un entier non négatif et que seules les quantités valides peuvent être dans le champ.

### Le champ de modèle `TimeField`

Le TimeField est un champ qui stocke les informations de temps dans votre modèle. Il possède deux paramètres, tout comme le DateField.

Voici un exemple de la manière d'utiliser ce champ :

```python
from django.db import models

class Order(models.Model):
    time_placed = models.TimeField(auto_now_add=True)
```

Dans l'exemple ci-dessus, le champ `time_placed` affiche automatiquement l'heure actuelle chaque fois qu'il y a une nouvelle commande.

### Le champ de modèle `ForeignKeyField`

Le type de champ `ForeignKey` crée une relation plusieurs-à-un entre deux modèles. Ce champ est utile lorsqu'un modèle (le modèle enfant) doit référencer un autre (le modèle parent). Il possède deux paramètres obligatoires : la classe à laquelle le modèle est lié et l'option `on_delete`.

Voici un exemple de la manière d'utiliser le `ForeignKey` :

```python
from django.db import models

class Customer(models.Model):
    email = models.EmailField()

class Order(models.Model):
    order_number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
```

Le `ForeignKey` lie chaque commande à un client spécifique dans l'extrait de code ci-dessus. Il permet également à un client d'être associé à plusieurs commandes. L'option `on_delete` spécifie que si vous supprimez un client référencé, toutes les commandes relatives à ce client doivent également quitter la base de données.

### Le champ de modèle `ManyToManyField`

Ce type de champ représente une relation plusieurs-à-plusieurs entre deux modèles. Cela implique que vous pouvez associer un enregistrement dans un modèle à de nombreux enregistrements dans un autre et vice versa. Ce champ possède un paramètre obligatoire : la classe à laquelle le modèle est lié.

Voici un exemple de la manière d'utiliser ce champ :

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)

class Order(models.Model):
    order_number = models.CharField(max_length=10)
    products = models.ManyToManyField(Product)
```

Dans le code précédent, le modèle 'order' possède un champ 'products' qui établit une relation plusieurs-à-plusieurs avec le modèle 'product'. Par conséquent, une commande peut contenir plusieurs produits, et un produit peut être dans plusieurs commandes.

### Le champ de modèle `OneToOneField`

Le type de champ `OneToOne` crée une relation un-à-un entre deux modèles. Cela signifie que chaque enregistrement dans un modèle correspondra à exactement un enregistrement d'un autre. Ce champ possède un paramètre obligatoire : la classe à laquelle le modèle est lié.

Voici un exemple de la manière d'utiliser le `OneToOneField` :

```python
from django.db import models

class Customer(models.Model):
    email = models.EmailField()

class CustomerProfile(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
```

Dans l'exemple ci-dessus, le `CustomerProfile` est lié au client via le `OneToOneField`. Cela garantit que chaque Customer peut avoir exactement un `CustomerProfile` et que chaque `CustomerProfile` est associé à un seul Customer. Le paramètre supplémentaire `on_delete=models.CASCADE` indique simplement au programme de supprimer le `CustomerProfile` chaque fois que le Customer est supprimé.

## Conclusion

Les champs de modèle Django vous permettent de construire des structures de données efficaces pour vos applications web. Les types de champs vous aident à éliminer les erreurs humaines en imposant le type de données dans un champ particulier.

Dans cet article, vous avez vu certains des types de champs courants dans Django et comment les utiliser pour stocker vos données. Alors que vous continuez à construire vos projets Django, les connaissances acquises en comprenant et en implémentant ces champs de modèle seront inestimables pour créer des applications fiables pour vos utilisateurs.