---
title: 'Le décorateur @property en Python : ses cas d''utilisation, avantages et syntaxe'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-12-19T17:47:43.000Z'
originalURL: https://freecodecamp.org/news/python-property-decorator
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/property-v2-HD.png
tags:
- name: Python Properties
  slug: python-properties
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: '@property'
  slug: property
- name: Python
  slug: python
seo_title: 'Le décorateur @property en Python : ses cas d''utilisation, avantages
  et syntaxe'
seo_desc: "\U0001F539 Meet Properties\nWelcome! In this article, you will learn how\
  \ to work with the @property decorator in Python. \nYou will learn:\n\nThe advantages\
  \ of working with properties in Python.\nThe basics of decorator functions: what\
  \ they are and how they are r..."
---

## 🔹 Rencontre avec les propriétés

Bienvenue ! Dans cet article, vous apprendrez à travailler avec le décorateur `@property` en Python. 

**Vous apprendrez :**

* Les avantages de travailler avec les propriétés en Python.
* Les bases des fonctions décorateurs : ce qu'elles sont et comment elles sont liées à @property.
* Comment utiliser @property pour définir des getters, setters et deleters.

### 1️⃣ Avantages des propriétés en Python

Commençons par un peu de contexte. **Pourquoi** utiliser des propriétés en Python ?

Les propriétés peuvent être considérées comme la manière "Pythonique" de travailler avec les attributs parce que :

* La syntaxe utilisée pour définir les propriétés est très concise et lisible.
* Vous pouvez accéder aux attributs d'instance exactement comme s'ils étaient des attributs publics tout en utilisant la "magie" des intermédiaires (getters et setters) pour valider les nouvelles valeurs et éviter d'accéder ou de modifier les données directement.
* En utilisant @property, vous pouvez "réutiliser" le nom d'une propriété pour éviter de créer de nouveaux noms pour les getters, setters et deleters.

**Ces avantages font des propriétés un outil vraiment génial pour vous aider à écrire un code plus concis et lisible.** ✨

### 2️⃣ Introduction aux **Décorateurs**

Une **fonction décorateur** est essentiellement une fonction qui ajoute de nouvelles fonctionnalités à une fonction passée en argument. Utiliser une fonction décorateur, c'est comme ajouter des pépites de chocolat à une glace 🍦. Cela nous permet d'ajouter de nouvelles fonctionnalités à une fonction existante sans la modifier. 

Dans l'exemple ci-dessous, vous pouvez voir à quoi ressemble une fonction décorateur typique en Python :

```python
def decorator(f):
    def new_function():
        print("Fonctionnalité supplémentaire")
        f()
    return new_function

@decorator
def initial_function():
    print("Fonctionnalité initiale")

initial_function()
```

**Analysons ces éléments en détail :**

* Nous trouvons d'abord la fonction décorateur `def decorator(f)` (les pépites ✨) qui prend une fonction `f` comme argument. 

```python
def decorator(f):
    def new_function():
        print("Fonctionnalité supplémentaire")
        f()
    return new_function
```

* Cette fonction décorateur a une fonction imbriquée, `new_function`. Remarquez comment `f` est appelée à l'intérieur de `new_function` pour atteindre la même fonctionnalité tout en ajoutant une nouvelle fonctionnalité avant l'appel de la fonction (nous pourrions également ajouter une nouvelle fonctionnalité après l'appel de la fonction).
* La fonction décorateur elle-même retourne la fonction imbriquée `new_function`.
* Ensuite (ci-dessous), nous trouvons la fonction qui sera _décorée_ (la glace 🍦) `initial_function`. Remarquez la syntaxe très particulière (`@decorator`) au-dessus de l'en-tête de la fonction. 

```python
@decorator
def initial_function():
    print("Fonctionnalité initiale")

initial_function()
```

Si nous exécutons le code, nous voyons cette sortie :

```python
Fonctionnalité supplémentaire
Fonctionnalité initiale
```

Remarquez comment la fonction décorateur s'exécute même si nous appelons uniquement `initial_function()`. C'est la magie d'ajouter @decorator ✨. 

**💡Note :** En général, nous écririons `@<nom_de_la_fonction_décorateur>`, en remplaçant le nom de la fonction décorateur après le symbole @.

**Je sais que vous vous demandez peut-être : comment cela est-il lié à @property ?** Le @property est un décorateur intégré pour la fonction [property()](https://docs.python.org/3/library/functions.html#property) en Python. Il est utilisé pour donner une fonctionnalité "spéciale" à certaines méthodes pour qu'elles agissent comme des getters, setters ou deleters lorsque nous définissons des propriétés dans une classe. 

Maintenant que vous êtes familiarisé avec les décorateurs, voyons un scénario réel de l'utilisation de @property !

## 🔸 Scénario réel : @property

Supposons que cette classe fait partie de votre programme. Vous modélisez une maison avec une classe `House` (pour le moment, la classe n'a qu'un attribut d'instance _price_ défini) :

```python
class House:

	def __init__(self, price):
		self.price = price
```

Cet attribut d'instance est public car son nom n'a pas de tiret bas initial. Puisque l'attribut est actuellement public, il est très probable que vous et les autres développeurs de votre équipe ayez accédé et modifié l'attribut **directement** dans d'autres parties du programme en utilisant la notation par points, comme ceci :

```
# Accéder à la valeur
obj.price

# Modifier la valeur
obj.price = 40000
```

💡 **Astuce :** _obj_ représente une variable qui référence une instance de `House`. 

Jusqu'à présent, tout fonctionne bien, n'est-ce pas ? **Mais** **disons que vous êtes invité à rendre cet attribut protégé (non public) et à valider la nouvelle valeur avant de l'assigner**. Plus précisément, vous devez vérifier si la valeur est un float positif. Comment feriez-vous cela ? Voyons cela.

### Changer votre code

À ce stade, si vous décidez d'ajouter des getters et setters, vous et votre équipe allez probablement paniquer 😱. Cela est dû au fait que chaque ligne de code qui accède ou modifie la valeur de l'attribut devra être modifiée pour appeler le getter ou le setter, respectivement. Sinon, le code ne fonctionnera plus ⚠️.

```python
# Changé de obj.price
obj.get_price()

# Changé de obj.price = 40000
obj.set_price(40000)
```

**Mais... Les propriétés viennent à la rescousse !** Avec `@property`, vous et votre équipe n'aurez pas besoin de modifier aucune de ces lignes car vous pourrez ajouter des getters et setters "en coulisses" sans affecter la syntaxe que vous utilisiez pour accéder ou modifier l'attribut lorsqu'il était public. 

Génial, n'est-ce pas ?  

## 🔹 @property : Syntaxe et Logique

Si vous décidez d'utiliser `@property`, votre classe ressemblera à l'exemple ci-dessous :

```python
class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Veuillez entrer un prix valide")

	@price.deleter
	def price(self):
		del self._price
```

Plus précisément, vous pouvez définir **trois méthodes** pour une propriété : 

* Un **getter** - pour accéder à la valeur de l'attribut.
* Un **setter** - pour définir la valeur de l'attribut.
* Un **deleter** - pour supprimer l'attribut d'instance.

**Le prix est maintenant "Protégé"**  
Veuillez noter que l'attribut _price_ est maintenant considéré comme "protégé" car nous avons ajouté un tiret bas initial à son nom dans `self._price` :

```python
self._price = price
```

En Python, [par convention](https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables), lorsque vous ajoutez un tiret bas initial à un nom, vous indiquez aux autres développeurs qu'il ne doit pas être accédé ou modifié directement en dehors de la classe. Il ne doit être accédé que par des intermédiaires (getters et setters) s'ils sont disponibles. 

### 🔸 Getter

Voici la méthode getter :

```python
@property
def price(self):
	return self._price
```

Remarquez la syntaxe :

* `@property` - Utilisé pour indiquer que nous allons définir une propriété. Remarquez comment cela améliore immédiatement la lisibilité car nous pouvons clairement voir le but de cette méthode. 
* `def price(self)` - L'en-tête. Remarquez comment le getter est nommé exactement comme la propriété que nous définissons : _price_. C'est le nom que nous utiliserons pour accéder et modifier l'attribut en dehors de la classe. La méthode ne prend qu'un seul paramètre formel, self, qui est une référence à l'instance.
* `return self._price` - Cette ligne est exactement ce à quoi vous vous attendez dans un getter régulier. La valeur de l'attribut protégé est retournée. 

Voici un exemple de l'utilisation de la méthode getter :

```python
>>> house = House(50000.0) # Créer une instance
>>> house.price            # Accéder à la valeur
50000.0
```

Remarquez comment nous accédons à l'attribut _price_ comme s'il s'agissait d'un attribut public. Nous ne changeons pas du tout la syntaxe, mais nous utilisons en réalité le getter comme intermédiaire pour éviter d'accéder directement aux données.

### 🔹 Setter

Maintenant, nous avons la méthode setter :

```python
@price.setter
def price(self, new_price):
	if new_price > 0 and isinstance(new_price, float):
		self._price = new_price
	else:
		print("Veuillez entrer un prix valide")
```

Remarquez la syntaxe :

* `@price.setter` - Utilisé pour indiquer que ceci est la méthode _setter_ pour la propriété _price_. Remarquez que nous n'utilisons **pas** _@**property**.setter_, nous utilisons _@**price**.setter_. Le nom de la propriété est inclus avant _.setter_.
* `def price(self, new_price):` - L'en-tête et la liste des paramètres. Remarquez comment le nom de la propriété est utilisé comme nom du setter. Nous avons également un deuxième paramètre formel (_new_price_), qui est la nouvelle valeur qui sera assignée à l'attribut _price_ (si elle est valide).
* Enfin, nous avons le corps du setter où nous **validons** l'argument pour vérifier s'il s'agit d'un float positif et ensuite, si l'argument est valide, nous mettons à jour la valeur de l'attribut. Si la valeur n'est pas valide, un message descriptif est imprimé. Vous pouvez choisir comment gérer les valeurs invalides selon les besoins de votre programme.

Voici un exemple de l'utilisation de la méthode setter avec @property :

```python
>>> house = House(50000.0)  # Créer une instance
>>> house.price = 45000.0   # Mettre à jour la valeur
>>> house.price             # Accéder à la valeur
45000.0
```

Remarquez comment nous ne changeons pas la syntaxe, mais maintenant nous utilisons un intermédiaire (le setter) pour valider l'argument avant de l'assigner. La nouvelle valeur (45000.0) est passée comme argument au setter : 

```
house.price = 45000.0
```

Si nous essayons d'assigner une valeur invalide, nous voyons le message descriptif. Nous pouvons également vérifier que la valeur n'a pas été mise à jour :

```python
>>> house = House(50000.0)
>>> house.price = -50
Veuillez entrer un prix valide
>>> house.price
50000.0
```

💡 **Astuce :** Cela prouve que la méthode setter fonctionne comme un intermédiaire. Elle est appelée "en coulisses" lorsque nous essayons de mettre à jour la valeur, donc le message descriptif est affiché lorsque la valeur n'est pas valide. 

### 🔸 Deleter

Enfin, nous avons la méthode deleter :

```python
@price.deleter
def price(self):
	del self._price
```

Remarquez la syntaxe :

* `@price.deleter` - Utilisé pour indiquer que ceci est la méthode _deleter_ pour la propriété _price_. Remarquez que cette ligne est très similaire à @price.setter, mais maintenant nous définissons la méthode deleter, donc nous écrivons @price.**deleter**.
* `def price(self):` - L'en-tête. Cette méthode n'a qu'un seul paramètre formel défini, self.
* `del self._price` - Le corps, où nous supprimons l'attribut d'instance.

💡 **Astuce :** Remarquez que le nom de la propriété est "réutilisé" pour les trois méthodes.

Voici un exemple de l'utilisation de la méthode deleter avec @property :

```python
# Créer une instance
>>> house = House(50000.0)

# L'attribut d'instance existe
>>> house.price
50000.0

# Supprimer l'attribut d'instance
>>> del house.price

# L'attribut d'instance n'existe plus
>>> house.price
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    house.price
  File "<pyshell#20>", line 8, in price
    return self._price
AttributeError: 'House' object has no attribute '_price'
```

L'attribut d'instance a été supprimé avec succès ✨. Lorsque nous essayons d'y accéder à nouveau, une erreur est levée car l'attribut n'existe plus.

### 🔹 Quelques conseils finaux 

Vous n'êtes pas obligé de définir les trois méthodes pour chaque propriété. Vous pouvez définir des propriétés en lecture seule en n'incluant qu'une méthode getter. Vous pourriez également choisir de définir un getter et un setter sans deleter. 

Si vous pensez qu'un attribut ne doit être défini que lorsque l'instance est créée ou qu'il ne doit être modifié qu'en interne dans la classe, vous pouvez omettre le setter. 

Vous pouvez choisir quelles méthodes inclure en fonction du contexte dans lequel vous travaillez.

## 🔸 En résumé

* Vous pouvez définir des propriétés avec la syntaxe @property, qui est plus compacte et lisible.
* @property peut être considéré comme la manière "pythonique" de définir des getters, setters et deleters.
* En définissant des propriétés, vous pouvez changer l'implémentation interne d'une classe sans affecter le programme, donc vous pouvez ajouter des getters, setters et deleters qui agissent comme des intermédiaires "en coulisses" pour éviter d'accéder ou de modifier les données directement.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Pour en savoir plus sur les propriétés et la programmation orientée objet en Python, [consultez mon cours en ligne](https://www.udemy.com/course/python-object-oriented-programming-oop/?referralCode=69EAFFB4805866B8CC31), qui comprend plus de 6 heures de cours vidéo, des exercices de codage et des mini-projets.