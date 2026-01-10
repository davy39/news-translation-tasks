---
title: Comment utiliser la programmation orientée objet en Python – Expliqué avec
  des exemples
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2024-04-24T14:39:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-oop-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/WhatsApp-Image-2024-04-24-at-8.25.07-AM.jpeg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: Comment utiliser la programmation orientée objet en Python – Expliqué avec
  des exemples
seo_desc: 'Object-oriented programming (OOP) is a style of programming that heavily
  relies on objects. These objects can have attributes and methods. While attributes
  store data, methods define behavior.

  Like many other programming languages, Python supports bo...'
---

La programmation orientée objet (OOP) est un style de programmation qui repose fortement sur les objets. Ces objets peuvent avoir des attributs et des méthodes. Alors que les attributs stockent des données, les méthodes définissent le comportement.

Comme de nombreux autres langages de programmation, Python prend en charge à la fois la programmation orientée objet et la programmation fonctionnelle. Cependant, la programmation orientée objet devient précieuse lors de l'écriture de programmes volumineux et complexes.

Dans cet article, vous apprendrez les avantages de la programmation orientée objet en Python, comment définir une classe, les attributs de classe et d'instance, et les méthodes d'instance. Vous apprendrez également le concept d'encapsulation et comment implémenter l'héritage entre les classes en Python.

Pour comprendre pleinement cet article, vous devez avoir les prérequis suivants :

* Connaissance de base du langage de programmation Python.

* Familiarité avec les concepts de fonctions et d'objets en programmation.

* Expérience de travail avec un éditeur de code ou un environnement de développement intégré (IDE).

* Compréhension de base de l'utilisation d'un terminal ou d'une console en ligne de commande.

Maintenant, plongeons dans le sujet.

## Pourquoi utiliser la programmation orientée objet ?

La programmation orientée objet (OOP) offre plusieurs avantages lors de l'organisation et de la gestion du code. En regroupant les données et fonctions apparentées en classes logiques, la programmation orientée objet favorise la structure du code et simplifie la maintenance, surtout lorsque les programmes deviennent volumineux et complexes. L'approche modulaire rend plus facile la compréhension, la modification et la réutilisation du code, réduisant ainsi le temps de développement.

Un autre avantage de la programmation orientée objet est sa capacité à fournir un style de programmation clair et compréhensible, ce qui peut être plus utile pour les développeurs. L'utilisation d'objets et les relations entre eux reflètent les concepts du monde réel. Cela facilite le raisonnement sur le code et la conception de systèmes complexes.

Enfin, les concepts de la programmation orientée objet tels que l'encapsulation et l'héritage contribuent à la robustesse du code en favorisant la protection des données et la réutilisabilité du code.

## Qu'est-ce qu'une classe en Python ?

La programmation orientée objet en Python repose fortement sur le concept de « classe ». Vous pouvez considérer une classe comme un plan utilisé pour créer des objets. Pour illustrer cela, imaginez que vous avez un plan pour un haut-parleur. Vous pouvez utiliser ce plan pour construire plusieurs haut-parleurs. Chaque haut-parleur créé à l'aide du plan est une instance du plan. De plus, chaque haut-parleur créé a ses propres attributs tels que la couleur, le modèle et le nom. Ils auront également leurs méthodes montrant un certain type de comportement tel que l'augmentation et la diminution du volume.

## Comment définir une classe en Python

Pour définir une classe, vous devez utiliser le mot-clé `class`, fourni par Python, suivi du nom de la classe et d'un deux-points :

```python
class NomDeClasse:
    pass
```

Maintenant, en utilisant notre illustration précédente, créons une classe nommée `HautParleur`. Dans votre éditeur de code, créez un fichier nommé `classes.py` et copiez les lignes de code suivantes dedans :

```python
class HautParleur:
    pass

haut_parleur_un = HautParleur()
print(haut_parleur_un)
```

Dans le code précédent, vous avez défini une classe nommée `HautParleur` sans aucun attribut ou méthode. Vous avez utilisé le mot-clé `pass` dans le corps de la classe. En Python, le mot-clé `pass` ne fait rien et est généralement utilisé comme espace réservé.

À la quatrième ligne du code, vous avez créé une instance de la classe `HautParleur` et l'avez assignée à la variable `haut_parleur_un`. Ce processus est également connu sous le nom d'instanciation d'un objet à partir d'une classe. Vous avez ensuite imprimé `haut_parleur_un` à la ligne cinq.

Maintenant, exécutez le code en exécutant la commande `python classes.py` dans votre terminal. Vous obtiendrez une sortie similaire à celle-ci dans votre terminal :

```bash
<__main__.HautParleur object at 0x10087f8e0>
```

La sortie montre que `haut_parleur_un` est un objet. `0x10087f8e0` dans la sortie montre l'adresse mémoire où Python stocke l'objet sur votre ordinateur.

L'adresse mémoire dans votre sortie de terminal sera différente.

Vous pouvez créer plusieurs autres instances de la classe `HautParleur` et elles seront toutes différentes les unes des autres. Pour vérifier cela, utilisons l'opérateur de comparaison d'égalité (**==**). Dans votre fichier `classes.py`, supprimez `print(haut_parleur_un)` et ajoutez ce qui suit au bas de votre code :

```python
haut_parleur_deux = HautParleur()

if haut_parleur_un == haut_parleur_deux:
    print("haut_parleur_un est le même que haut_parleur_deux")
else:
    print("haut_parleur_un est différent de haut_parleur_deux")
```

Maintenant, exécutez `python classes.py` dans votre terminal. Vous obtiendrez la sortie suivante :

```bash
haut_parleur_un est différent de haut_parleur_deux
```

## Attributs de classe et d'instance

Dans cette section, vous allez ajouter des attributs à votre classe `HautParleur`. Vous pouvez voir les attributs comme des données stockées dans un objet. Alors que les attributs de classe sont communs à toutes les instances créées à partir de votre classe, les attributs d'instance sont uniques à chaque instance.

Maintenant, modifiez votre fichier `classes.py` en remplaçant votre code par ce qui suit :

```python
class HautParleur:
    marque = "Beatpill" # attribut de classe

    def __init__(self, couleur, modele):
        self.couleur = couleur # attribut d'instance
        self.modele = modele # attribut d'instance
```

Vous devriez déjà être familier avec la première ligne de votre nouveau code. À la ligne deux, vous avez défini un attribut de classe, nommé `marque`, et lui avez assigné la valeur `Beatpill`. Les attributs de classe sont des variables qui appartiennent à la classe elle-même, plutôt qu'aux instances individuelles de la classe. L'effet des attributs de classe est que toutes les instances que vous créez à partir de votre classe hériteront et partageront cet attribut de classe et sa valeur. Dans ce cas, chaque instance que vous créez à partir de votre classe `HautParleur` partagera la même valeur de `marque`.

La ligne quatre de votre code définit une méthode `__init__`, qui prend trois paramètres — `self`, `couleur`, et `modele`. Cette méthode sera appelée chaque fois que vous créez une nouvelle instance à partir de votre classe `HautParleur`. Le paramètre `self` est une référence à la classe `HautParleur` et il est conventionnel en Python de toujours l'avoir comme premier paramètre dans une méthode `__init__`. Les lignes cinq et six définissent les attributs d'instance, `couleur`, et `modele` pour votre classe `HautParleur`.

Ainsi, chaque fois que vous créez une nouvelle instance à partir de votre classe, vous devez fournir des arguments pour vos attributs `couleur` et `modele`. Ne pas le faire entraînera une erreur.

Maintenant, ajoutez ce qui suit au bas de votre code :

```python
haut_parleur_un = HautParleur("noir", "85XB5")
haut_parleur_deux = HautParleur("rouge", "Y8F33")

print(f"haut_parleur_un est {haut_parleur_un.couleur} tandis que haut_parleur_deux est {haut_parleur_deux.couleur}")
```

En ajoutant le code précédent, vous avez créé deux instances de la classe `HautParleur` — `haut_parleur_un` et `haut_parleur_deux`. Les arguments dans chaque instance représentent les valeurs de leurs attributs `couleur` et `modele`. Vous avez ensuite imprimé un message qui affiche l'attribut de couleur de chaque objet. Maintenant, si vous exécutez la commande `python classes.py` dans votre terminal, vous obtiendrez la sortie :

```bash
haut_parleur_un est noir tandis que haut_parleur_deux est rouge
```

Pour voir que les deux instances partagent le même attribut de classe `marque`, modifiez votre fonction `print()` comme ceci :

```python
print(
    f"haut_parleur_un est {haut_parleur_un.couleur} tandis que haut_parleur_deux est {haut_parleur_deux.couleur}",
    haut_parleur_un.marque,
    haut_parleur_deux.marque,
    sep="\n",
)
```

Maintenant, exécutez `python classes.py` et vous obtiendrez la sortie suivante :

```bash
haut_parleur_un est noir tandis que haut_parleur_deux est rouge
Beatpill
Beatpill
```

## Méthodes d'instance

En plus des attributs de classe et d'instance, les classes peuvent également avoir des méthodes, appelées méthodes d'instance. Les méthodes d'instance sont des fonctions définies dans une classe qui opèrent sur les instances de la classe. Elles utilisent les attributs de classe et d'instance pour fournir un comportement et une fonctionnalité aux objets.

Pour ajouter des méthodes d'instance, modifiez votre fichier de code comme suit :

```python
class HautParleur:
    marque = "Beatpill"

    def __init__(self, couleur, modele):
        self.couleur = couleur
        self.modele = modele

    def allumer(self):
        print(f"Allumage du haut-parleur {self.couleur} {self.modele}.")

    def eteindre(self):
        print(f"Extinction du haut-parleur {self.couleur} {self.modele}.")


haut_parleur_un = HautParleur("noir", "85XB5")
haut_parleur_deux = HautParleur("rouge", "Y8F33")
```

Dans l'exemple ci-dessus, nous avons ajouté deux méthodes d'instance — `allumer()` et `eteindre()`. Ces méthodes, comme la méthode `__init__`, prennent `self` comme premier argument.

La méthode `allumer()` imprime un message indiquant que le haut-parleur de la couleur et du modèle donnés est en cours d'allumage. De même, la méthode `eteindre()` imprime un message sur l'extinction du haut-parleur.

Pour appeler ces méthodes, ajoutez ce qui suit au bas de votre fichier :

```python
haut_parleur_un.allumer()
haut_parleur_deux.eteindre()
```

Maintenant, exécutez `python classes.py` dans votre terminal et vous obtiendrez la sortie suivante :

```bash
Allumage du haut-parleur noir 85XB5.
Extinction du haut-parleur rouge Y8F33.
```

## Encapsulation en Python

L'encapsulation est l'un des concepts fondamentaux de la programmation orientée objet. Elle fait référence à la combinaison des données (attributs) et des méthodes au sein d'une classe. L'encapsulation fournit une protection des données et un contrôle sur la manière dont le code interagit avec l'état interne d'un objet.

Vous pouvez réaliser l'encapsulation en Python en définissant des attributs et des méthodes privés au sein d'une classe. Par convention, les attributs et méthodes privés sont précédés d'un seul underscore (_). Bien que Python ne dispose pas de modificateurs privés stricts comme certains autres langages, le préfixe underscore sert d'avertissement aux autres développeurs de ne pas accéder ou modifier les attributs et méthodes directement depuis l'extérieur de la classe.

Voici un exemple d'encapsulation en Python :

```python
class HautParleur:
    marque = "Beatpill"

    def __init__(self, couleur, modele):
        self._couleur = couleur  # Attribut privé
        self._modele = modele  # Attribut privé

    def allumer(self):
        print(f"Allumage du haut-parleur {self._couleur} {self._modele}.")

    def eteindre(self):
        print(f"Extinction du haut-parleur {self._couleur} {self._modele}.")

    def obtenir_couleur(self):
        return self._couleur

    def definir_couleur(self, nouvelle_couleur):
        self._couleur = nouvelle_couleur


haut_parleur_un = HautParleur("noir", "85XB5")
haut_parleur_un.allumer()

# Accéder à un attribut privé directement (non recommandé)
print(haut_parleur_un._couleur)

# Accéder à un attribut privé en utilisant la méthode getter (recommandé)
print(haut_parleur_un.obtenir_couleur())

# Modifier un attribut privé en utilisant la méthode setter (recommandé)
haut_parleur_un.definir_couleur("blanc")
print(haut_parleur_un.obtenir_couleur())
```

Dans l'exemple précédent, les attributs `couleur` et `modele` sont des attributs privés de la classe `HautParleur`. Bien qu'il soit possible d'accéder et de modifier ces attributs directement depuis l'extérieur de la classe en utilisant, par exemple, `print(haut_parleur_un._couleur)`, cette pratique est déconseillée. Faire cela viole l'encapsulation et peut entraîner un comportement non intentionnel ou une corruption des données.

Au lieu de cela, la classe fournit des méthodes getter `obtenir_couleur()` et setter `definir_couleur()` pour accéder et modifier les attributs privés de manière contrôlée. Ces méthodes agissent comme une interface pour interagir avec l'état interne de l'objet, assurant l'intégrité des données et permettant une validation supplémentaire.

L'encapsulation favorise la modularité du code, la maintenabilité et la protection des données en séparant l'état interne de l'interface publique (méthodes). Elle vous permet de changer l'état interne sans affecter le code qui utilise la classe, tant que l'interface publique reste la même.

## Héritage en Python

L'héritage est un autre concept fondamental de la programmation orientée objet. Il permet aux classes d'hériter des attributs et des méthodes d'autres classes. La nouvelle classe hérite des attributs et des méthodes de la classe existante, appelée classe parente ou classe de base. La nouvelle classe est appelée classe enfant ou classe dérivée.

L'héritage favorise la réutilisation du code en permettant à la classe enfant d'hériter et d'étendre la fonctionnalité de la classe parente. Cela aide à créer des relations hiérarchiques entre les classes et à organiser le code de manière plus structurée et logique.

En Python, l'héritage est implémenté en utilisant la syntaxe suivante :

```python
class ClasseDerivee(ClasseDeBase):
    # Méthodes et attributs de la classe dérivée
```

Pour voir comment fonctionne l'héritage, modifiez votre code comme suit :

```python
class HautParleur:
    marque = "Beatpill"

    def __init__(self, couleur, modele):
        self._couleur = couleur
        self._modele = modele

    def allumer(self):
        print(f"Allumage du haut-parleur {self._couleur} {self._modele}.")

    def eteindre(self):
        print(f"Extinction du haut-parleur {self._couleur} {self._modele}.")

# Ajouter une classe HautParleurIntelligent et la faire hériter de la classe HautParleur
class HautParleurIntelligent(HautParleur):
    def __init__(self, couleur, modele, assistant_vocal):
        super().__init__(couleur, modele)
        self._assistant_vocal = assistant_vocal

    def dire_bonjour(self):
        print(f"Bonjour, je suis {self._assistant_vocal}")


# Créer une instance de la classe HautParleurIntelligent
haut_parleur_intelligent = HautParleurIntelligent("noir", "XYZ123", "Alexa")
haut_parleur_intelligent.allumer()  # Hérité de HautParleur
haut_parleur_intelligent.dire_bonjour()
```

Dans le code précédent, la classe `HautParleurIntelligent` est dérivée de la classe `HautParleur`. La classe `HautParleurIntelligent` hérite des attributs et des méthodes de la classe `HautParleur`.

La méthode `__init__` de la classe `HautParleurIntelligent` appelle la méthode `__init__` de la classe `HautParleur` en utilisant `super().__init__(couleur, modele)`. Cela garantit que les attributs hérités `_couleur` et `_modele` sont correctement initialisés. De plus, la classe `HautParleurIntelligent` a son propre attribut `_assistant_vocal`, et une nouvelle méthode `dire_bonjour`.

Maintenant, exécutez `python classes.py` dans votre terminal et vous obtiendrez la sortie suivante :

```bash
Allumage du haut-parleur noir XYZ123.
Bonjour, je suis Alexa
```

## Conclusion

Tout au long de cet article, nous avons mis en évidence les avantages de la programmation orientée objet (OOP) et démontré comment définir des classes, créer et utiliser des attributs et méthodes d'instance. Nous avons fourni des exemples pratiques pour illustrer l'implémentation des classes en Python, ainsi que des concepts clés de la programmation orientée objet tels que l'encapsulation et l'héritage.

L'application des leçons couvertes dans cet article vous aidera à améliorer votre expérience de programmation en Python et à augmenter l'efficacité et la maintenabilité de votre code.

## Références et lectures complémentaires

* https://en.wikipedia.org/wiki/Object-oriented_programming

* https://realpython.com/python3-object-oriented-programming/

* https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming

* https://docs.python.org/3/tutorial/classes.html

* https://realpython.com/python-classes/

* https://realpython.com/python-double-underscore/