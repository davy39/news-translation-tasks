---
title: Programmation Orientée Objet en Python – Cours Accéléré Complet
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2022-10-20T22:24:35.000Z'
originalURL: https://freecodecamp.org/news/crash-course-object-oriented-programming-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/udaXTUR.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: Programmation Orientée Objet en Python – Cours Accéléré Complet
seo_desc: "Object Oriented programming, or \"OOP\" for short, is a way of writing\
  \ code that relies on the concepts of classes and objects. \nThe main benefit of\
  \ writing your code in an object-oriented way is to structure your program into\
  \ simple, reusable pieces o..."
---

La programmation orientée objet, ou "POO" en abrégé, est une manière d'écrire du code qui repose sur les concepts de classes et d'objets. 

Le principal avantage d'écrire votre code de manière orientée objet est de structurer votre programme en morceaux de code simples et réutilisables.

Restez avec moi tout au long de cet article et vous aurez une compréhension complète des principes fondamentaux de la POO d'ici la fin. Tous les exemples de code seront en [Python](https://boot.dev/learn/learn-python), mais les concepts s'appliquent généralement à tous les langages de programmation.

J'ai inclus tout le matériel d'apprentissage dont vous aurez besoin ici dans cet article. Mais si vous souhaitez approfondir avec des exercices de codage en direct et des quiz, vous pouvez les trouver [ici](https://boot.dev/learn/learn-object-oriented-programming) sur [Boot.dev](https://boot.dev/).

## Table des Matières

1. [L'objectif de la Programmation Orientée Objet](#heading-lobjectif-de-la-poo-est-un-code-plus-propre)
2. [Les Classes en POO](#heading-les-classes-permettent-une-réutilisabilité-encore-plus-grande)
3. [Pilier de la POO #1 – Encapsulation](#heading-pilier-de-la-poo-1-encapsulation)
4. [Pilier de la POO #2 – Abstraction](https://www.freecodecamp.org/news/p/463de7a5-749b-49da-96e9-223a08fc983b/oop-pillar-2-abstraction)
5. [Pilier de la POO #3 – Héritage](#heading-pilier-de-la-poo-3-héritage)
6. [Pilier de la POO #4 – Polymorphisme](#heading-pilier-de-la-poo-4-polymorphisme)

## L'objectif de la POO est un Code Plus Propre

La programmation orientée objet et d'autres paradigmes comme la [programmation fonctionnelle](https://boot.dev/learn/learn-functional-programming) visent tous à rendre le code plus facile à utiliser et à comprendre. Nous appelons le code qui est facile à utiliser "code propre".

> N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre. – Martin Fowler

### Le code propre n'est pas :

* Une manière de faire fonctionner vos programmes plus rapidement
* Une manière de faire utiliser moins de mémoire à votre programme
* Nécessaire pour créer certains types de programmes
* Strictement meilleur que le code non-POO

### Le code propre est :

* Conçu pour rendre le code plus facile à utiliser dans de nombreuses situations
* Quelque chose qui aide les humains à modéliser et simuler le monde réel
* Une manière de rendre la recherche et la correction de bugs plus faciles
* Une manière de rendre le développement de nouvelles fonctionnalités plus rapide
* La meilleure manière de rester sain d'esprit en tant qu'ingénieur logiciel

Quelques exemples de pratiques de "code propre" incluent [l'écriture de bons commentaires](https://blog.boot.dev/clean-code/code-comments/), l'utilisation de [code DRY](https://blog.boot.dev/clean-code/dry-code/), et [le nommage correct des variables](https://blog.boot.dev/clean-code/naming-variables/), pour n'en nommer que quelques-uns.

## La POO est une Manière d'Écrire du Code DRY

Prétendons que nous avons du code qui ressemble à ceci :

```python
soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]

soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
```

Nous pouvons utiliser une fonction pour refactoriser un peu le code :

```python
def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
    
soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)
```

Nous ne voulons pas que trop de notre code fasse exactement la même chose. Lorsque le code est dupliqué, cela conduit à de nombreux problèmes potentiels. Dans notre exemple, supposons que le dictionnaire `soldier` change, et que maintenant la clé qui stocke la valeur "damage" s'appelle `dmg`.

Dans le premier exemple, nous devrions mettre à jour deux lignes de code. Dans le second exemple, nous devons seulement faire le changement à un seul endroit.

Ce n'est pas un gros problème lorsque deux lignes sont identiques et existent l'une à côté de l'autre. Cependant, imaginez si nous avions fait cela des centaines de fois dans dix ou vingt fichiers de code différents ! Tout à coup, cela a beaucoup de sens d'arrêter de se répéter et d'écrire des fonctions plus réutilisables. Nous appelons cela du [code DRY (ne vous répétez pas)](https://blog.boot.dev/clean-code/dry-code/).

## Les Classes Permettent une Réutilisabilité Encore Plus Grande

Une [classe](https://boot.dev/course/f9a48bbc-d1ff-4388-bf0c-23c6e3c60ae0/46f1f86f-9b7c-4a8b-8883-4b407c0e675b) est un type spécial de valeur dans un langage de programmation orienté objet comme Python. Tout comme une chaîne de caractères, un entier ou un flottant, une classe est un type _personnalisé_ qui a certaines propriétés spéciales.

Un objet est simplement une instance d'un type de classe. "Instance" est simplement un grand mot pour "l'un d'une chose". Par exemple, ici, `health` est une instance d'un type entier.

```python
health = 50
```

### Comment créer une classe ?

En Python, vous avez juste besoin d'utiliser le mot-clé `class`, et vous pouvez définir des propriétés personnalisées de la manière suivante.

```python
class Soldier:
    health = 5
```

Ensuite, pour créer une instance d'un `Soldier`, nous appelons simplement la classe. Remarquez qu'une classe n'est pas une fonction et qu'elle ne prend pas de paramètres d'entrée directement.

```python
first_soldier = Soldier()
print(first_soldier.health)
# imprime "5"
```

### Méthodes sur une classe

Vous vous demandez peut-être pourquoi les classes sont utiles – elles semblent comme des dictionnaires Python réguliers mais en pire !

Ce qui rend les classes vraiment cool, c'est qu'elles nous permettent de définir des [méthodes](https://en.wikipedia.org/wiki/Method_(computer_programming)) personnalisées sur elles. Une méthode est une fonction qui est associée à une classe, et elle a accès à toutes les propriétés de l'objet.

```python
class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# imprime "3"
```

### La valeur spéciale "self"

Comme vous pouvez le voir, les méthodes sont imbriquées dans la déclaration de la `class`. Les méthodes prennent toujours un paramètre spécial comme premier argument appelé `self`. La variable `self` est une référence à l'objet lui-même, donc en l'utilisant, vous pouvez lire et mettre à jour les propriétés de l'objet.

Remarquez que les méthodes sont appelées directement sur un objet en utilisant l'opérateur point.

```python
object.method()
```

### Comment retourner des valeurs depuis une méthode

Si une fonction régulière ne retourne rien, ce n'est généralement pas une fonction très utile. Mais les méthodes ne retournent souvent rien explicitement car elles modifient souvent les propriétés de l'objet à la place.

Cependant, elles _peuvent_ aussi retourner des valeurs !

```python
class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# imprime "6"
```

### Méthodes vs Fonctions

Une fonction est un morceau de code qui est appelé par un nom. Vous pouvez lui passer des données à traiter via des paramètres et elle peut optionnellement retourner des données. Toutes les données qui sont passées à une fonction sont explicitement passées via des paramètres.

Une méthode est un morceau de code qui est appelé par un nom _qui est associé à un objet_. Les méthodes et les fonctions sont similaires mais ont deux différences clés.

1. Une méthode est _implicitement_ passée à l'objet sur lequel elle a été appelée. En d'autres termes, vous ne verrez pas toutes les entrées dans la liste des paramètres
2. Une méthode est capable d'opérer sur des données qui sont contenues dans la classe. En d'autres termes, vous ne verrez pas toutes les sorties dans l'instruction `return`.

## Le Débat sur la POO

Parce que les fonctions sont plus explicites, certains développeurs soutiennent que la [programmation fonctionnelle](https://blog.boot.dev/clean-code/benefits-of-functional-programming/) est meilleure que la programmation orientée objet. En réalité, aucun paradigme n'est "meilleur", et les meilleurs développeurs apprennent et comprennent les deux styles et les utilisent comme ils le jugent approprié.

Par exemple, bien que les méthodes soient plus implicites et rendent souvent le code plus difficile à lire, elles facilitent également le regroupement des données et du comportement d'un programme en un seul endroit. Cela peut conduire à une base de code mieux organisée. Le compromis est celui de la lisibilité au niveau du fichier pour la lisibilité au niveau du projet.

## Constructeurs en Python

Il est assez rare dans le monde réel de voir une classe qui définit des propriétés de la manière dont nous l'avons fait jusqu'à présent.

```python
class Soldier:
    armor = 2
    num_weapons = 2
```

Il est beaucoup plus pratique d'utiliser un [constructeur](https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)). En Python, un constructeur est fait avec la méthode [__init__()](https://docs.python.org/3/reference/datamodel.html#object.__init__), et il est automatiquement appelé lorsqu'un nouvel objet est créé. Ainsi, avec un constructeur, le code ressemblerait à ceci.

```python
class Soldier:
    def __init__(self):
        self.armor = 2
        self.num_weapons = 2
```

Cependant, parce que le constructeur est une méthode, nous pouvons maintenant rendre l'armure de départ et le nombre d'armes configurables avec quelques paramètres.

```python
class Soldier:
    def __init__(self, armor, num_weapons):
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier(5, 10)
print(soldier.armor)
# imprime "5"
print(soldier.num_weapons)
# imprime "10"
```

## Variables de Classe vs Variables d'Instance

Jusqu'à présent, nous avons travaillé avec des variables de classe et des variables d'instance, mais nous n'avons pas vraiment parlé de la différence.

### Variables d'instance

Les variables d'instance varient d'un objet à l'autre et sont déclarées dans le constructeur.

```python
class Wall():
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20 # met à jour uniquement cette instance de mur
print(south_wall.height)
# imprime "20"

north_wall = Wall()
print(north_wall.height)
# imprime "10"
```

### Variables de classe

Les variables de classe restent les mêmes entre les instances de la même classe et sont déclarées au niveau supérieur d'une classe.

```python
class Wall():
    height = 10

south_wall = Wall()
print(south_wall.height)
# imprime "10"

Wall.height = 20 # met à jour toutes les instances de Wall

print(south_wall.height)
# imprime "20"
```

### **Variables de classe vs variables d'instance – lesquelles dois-je utiliser ?**

De manière générale, _évitez les variables de classe_. Tout comme les variables globales, les variables de classe sont généralement une mauvaise idée car elles rendent difficile le suivi des parties de votre programme qui effectuent des mises à jour de données. 

Cependant, il est important de comprendre comment elles fonctionnent car vous pourriez les rencontrer dans la nature.

# Les Quatre Pilliers de la POO

## Pilier de la POO #1 – Encapsulation

L'[encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) est l'un des outils les plus puissants de votre boîte à outils en tant qu'ingénieur logiciel. Comme nous l'avons couvert au début de ce tutoriel, écrire du code que les machines comprennent est facile. Mais écrire du code que les humains peuvent comprendre est très difficile.

L'encapsulation est la pratique qui consiste à cacher des informations à l'intérieur d'une "[boîte noire](https://en.wikipedia.org/wiki/Black_box)" afin que les autres développeurs travaillant avec le code n'aient pas à s'en soucier. 

Un exemple basique d'encapsulation serait une fonction. L'appelant d'une fonction n'a pas besoin de trop se soucier de ce qui se passe à l'intérieur – il doit simplement comprendre les entrées et les sorties.

```python
pythonacceleration = calc_acceleration(initial_speed, final_speed, time)
```

Dans l'exemple ci-dessus, pour utiliser la fonction `calc_acceleration`, nous n'avons pas vraiment besoin de comprendre ce qui se passe à l'intérieur. C'est l'objectif de l'encapsulation : elle facilite notre vie en tant que développeurs et nous aide à écrire un code plus propre.

### Encapsulation en POO

Dans le contexte de la programmation orientée objet, nous pouvons pratiquer une bonne encapsulation en utilisant des membres privés et publics. 

L'idée est que si nous voulons que les utilisateurs de notre classe interagissent directement avec quelque chose, nous le rendons _public_. S'ils n'ont pas besoin d'utiliser une certaine méthode ou propriété, nous la rendons _privée_ afin de garder les instructions d'utilisation de notre classe simples.

### Encapsulation en Python

Afin de faire respecter l'encapsulation en Python, les développeurs préfèrent les propriétés et les classes qu'ils ont l'intention de rendre privées avec un double soulignement.

```python
class Wall():
    def __init__(self, height):
        # cela nous empêche d'accéder à la propriété __height
        # directement sur une instance de Wall
        self.__height = height

    def get_height(self):
        return self.__height
```

Dans l'exemple ci-dessus, nous ne voulons pas que les utilisateurs de la classe `Wall` puissent changer sa hauteur. Nous rendons la propriété `__height` privée et exposons une méthode publique `get_height` afin que les utilisateurs puissent toujours lire la hauteur d'un mur sans être tentés de la mettre à jour. 

Cela empêchera les développeurs de faire quelque chose comme :

```python
# front_wall est une instance de Wall
front_wall.__height = 10 # cela résulte en une erreur
```

### L'encapsulation ne rend pas les systèmes plus sécurisés

Comme nous en avons parlé plus tôt, l'encapsulation est la pratique qui consiste à cacher une certaine complexité de code à l'intérieur d'une "[boîte noire](https://en.wikipedia.org/wiki/Black_box)" afin que les autres développeurs travaillant avec le code n'aient pas à s'en soucier. L'ajout d'encapsulation à nos programmes via des membres "publics" et "privés" rend notre code plus facile à utiliser. Il le rend "plus propre".

Pour être clair, l'encapsulation ne rend pas le code plus sécurisé dans le sens [cryptographique](https://boot.dev/learn/learn-cryptography) ou cybersécurité du terme. C'est un point qui m'a personnellement confus lorsque j'apprenais pour la première fois les membres de classe privés et publics à l'école. 

Des choses comme les hachages [SHA-256](https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/), les [JWTs pour l'authentification](https://blog.boot.dev/cryptography/hmac-and-macs-in-jwts/), et les [chiffrements](https://blog.boot.dev/cryptography/aes-256-cipher-python-cryptography-examples/) sont un sujet complètement séparé qui n'a rien à voir avec les classes ou l'encapsulation.

L'encapsulation est un mécanisme pour rendre le code plus facile à utiliser et moins bogué. Nous nous empêchons _nous-mêmes_ d'accéder aux données privées car nous avons décidé qu'il n'était pas logique de les utiliser en dehors de la classe.

## Pilier de la POO #2 – Abstraction

L'abstraction est l'un des concepts clés de la programmation orientée objet. Le but de l'abstraction est de gérer la complexité en cachant les détails inutiles. 

L'abstraction et l'encapsulation vont généralement de pair, et si nous ne sommes pas prudents avec nos définitions, elles peuvent sembler être la même chose.

### Abstraction vs encapsulation

Bien que les définitions changent toujours, j'aime penser à l'abstraction et à l'encapsulation de la manière suivante.

* L'abstraction est une technique qui nous aide à identifier quelles informations et quels comportements doivent être encapsulés, et ce qui doit être exposé.
* L'encapsulation est la technique pour organiser le code afin d'encapsuler ce qui doit être caché, et rendre visible ce qui est destiné à être visible.

Si vous souhaitez une lecture plus longue sur le sujet, consultez [cet essai](https://web.archive.org/web/20210513154547/https://www.tonymarston.net/php-mysql/abstraction.txt).

### Donc, est-ce que nous _encapsulons_ ou _abstrayons_ notre code lorsque nous rendons les choses privées ?

Les deux. Nous faisons presque toujours les deux. Le processus d'utilisation du double soulignement est une forme d'encapsulation. Le processus de _décision_ de quelles données _méritent_ d'être cachées derrière le double soulignement est l'abstraction. 

Regardons un exemple concret.

```python
import random

my_random_number = random.randrange(5)
```

Dans cet exemple, nous utilisons la bibliothèque `random` pour générer un nombre aléatoire. Comme il s'avère, [générer des nombres aléatoires](https://blog.boot.dev/cryptography/what-is-entropy-in-cryptography/) est un problème _*vraiment difficile*_. 

Le système d'exploitation utilise en fait l'état matériel physique de l'ordinateur comme entrée pour ensemencer l'aléatoire. 

Cependant, les développeurs de la bibliothèque `random` ont _abstrait_ cette complexité et _encapsulé_ beaucoup de ces données et comportements afin que nous n'ayons pas à nous en soucier. Nous disons simplement "Je veux un nombre aléatoire inférieur ou égal à 5" et la bibliothèque s'en charge pour nous.

La décision de prendre un seul nombre comme entrée pour la fonction `randrange` était une décision d'abstraction. Lors de l'écriture de logiciels de niveau production, il est crucial de bien faire les abstractions, car ce sont les choses les plus difficiles à changer plus tard. 

Pensez aux conséquences si les mainteneurs du package `random` changeaient les paramètres d'entrée de la fonction `randrange` ! Cela casserait du code dans le monde entier.

## Comment les Développeurs POO Pensent

Les méthodes peuvent en fait être privées également. En d'autres termes, nous pouvons encapsuler le _comportement_ ainsi que les _données_.

### **Regrouper les données et le comportement**

Les classes en programmation orientée objet concernent le regroupement des données et du comportement en un seul endroit : un objet. 

Les programmeurs orientés objet tendent à penser à la programmation comme un problème de modélisation. Ils pensent : "Comment puis-je écrire une classe `Human` qui simule les données et le comportement d'un humain réel ?"

Nous ne nous concentrons pas sur la [programmation fonctionnelle](https://boot.dev/learn/learn-functional-programming) dans ce cours. Mais pour fournir un contraste, les programmeurs fonctionnels tendent à penser à leur code comme des entrées et des sorties. "Lorsque qu'un humain effectue une action, quelles sont les entrées de cette action, et comment les sorties affectent-elles l'état de mon programme ?"

### **Les deux paradigmes sont précieux**

Bien que la POO ne soit pas le seul paradigme en programmation, c'est un paradigme éprouvé qui est utile dans une variété de circonstances. 

Dans tous les cas, si vous avez personnellement une compréhension de plusieurs façons de penser au code, vous serez un bien meilleur développeur dans l'ensemble.

## Pilier de la POO #3 – Héritage

Nous avons atteint le Saint-Graal de la programmation orientée objet : [l'héritage](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)). L'héritage est vraiment la caractéristique définissante des langages orientés objet. 

Les langages sans classes comme [Go](https://boot.dev/learn/learn-golang)lang et [Rust](https://www.freecodecamp.org/news/rust-in-replit/) fournissent des fonctionnalités d'encapsulation et d'abstraction. En fait, presque _tous_ les langages le font. L'héritage, en revanche, tend à être unique aux langages basés sur les classes comme [Python](https://boot.dev/learn/learn-python), [JavaScript](https://www.freecodecamp.org/news/learn-javascript-by-coding-7-games/), [Java](https://www.freecodecamp.org/news/the-java-handbook/), et Ruby.

### Qu'est-ce que l'héritage ?

L'héritage permet à une classe (aka "la classe enfant") d'_hériter_ des propriétés et des méthodes d'une autre classe (aka "la classe parente").

Cette puissante fonctionnalité du langage nous aide à éviter d'écrire beaucoup de code identique deux fois. Elle nous permet de rendre notre code [DRY (ne vous répétez pas)](https://blog.boot.dev/clean-code/dry-code/).

### Héritage en Python – Syntaxe

En Python, une classe peut hériter d'une autre en utilisant la syntaxe suivante :

```python
class Animal:
    # classe parente "Animal"

class Cow(Animal):
    # classe enfant "Cow" hérite de "Animal"
```

Afin d'utiliser le constructeur de la classe parente, nous pouvons utiliser la méthode intégrée `super()` de Python.

```python
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # appeler le constructeur parent pour
        # donner à la vache quelques pattes
        super().__init__(4)
```

### Quand devrais-je utiliser l'héritage ?

L'héritage est un outil puissant, mais il est _vraiment_ mauvais d'essayer de l'utiliser à outrance. Vous ne devriez utiliser l'héritage que lorsque chaque instance de la classe enfant peut également être considérée comme étant du même type que la classe parente.

Lorsque qu'une classe enfant hérite d'une classe parente, elle hérite de _tout_. Si vous ne souhaitez partager que _certaines_ fonctionnalités, l'héritage n'est probablement pas la meilleure réponse. Dans ce cas, vous voudriez probablement partager quelques fonctions, ou peut-être créer une nouvelle classe parente dont les deux classes héritent.

### Tous les chats sont des animaux mais tous les animaux ne sont pas des chats

![Image](https://www.freecodecamp.org/news/content/images/2022/10/LwZVCId.png)

### Hiérarchie d'héritage

Il n'y a pas de limite à la profondeur à laquelle nous pouvons imbriquer un arbre d'héritage. Par exemple, un `Cat` peut hériter de `Animal` qui hérite de `LivingThing`. 

Cela dit, nous devons toujours être prudents que chaque fois que nous héritons d'une classe de base, l'enfant est un _*sous-ensemble strict*_ du parent. Vous ne devriez jamais vous dire "ma classe enfant a besoin de quelques méthodes du parent, mais pas de ces autres" et décider d'hériter de ce parent.

### Enfants multiples

Jusqu'à présent, nous avons travaillé avec un héritage de classe linéaire. En réalité, les structures d'héritage forment souvent des arbres, pas des lignes. Une classe peut avoir autant de classes enfants directes que le programmeur le souhaite.

Vous trouverez souvent dans les logiciels de production qu'il est plus probable qu'un arbre d'héritage soit large plutôt que profond. En d'autres termes, au lieu d'un arbre profond comme :

`Organisme -> Animal -> Mammifère -> Félin -> Chat`

Vous verrez plus souvent un arbre large :

```
Dragon -> Drake
       -> Wyvern
       -> Hydra
       -> Druk
```

### Pourquoi les arbres d'**héritage** sont-ils souvent larges au lieu d'être profonds ?

Comme nous en avons parlé plus tôt, dans un bon logiciel, une classe enfant est un sous-ensemble strict de sa classe parente. 

Dans un arbre profond, cela signifie que les enfants doivent être des membres parfaits de tous les types de classes parent. Cela n'arrive tout simplement pas très souvent dans le monde réel. Il est beaucoup plus probable que vous ayez une classe de base qui a simplement de nombreuses classes sœurs qui sont des variations légèrement différentes de la base.

```
Véhicule -> Camion
        -> Voiture
        -> Bateau
        -> Train
```

## Pilier de la POO #4 – Polymorphisme

Bien que l'héritage soit la caractéristique la plus unique à laquelle les langages orientés objet prétendent, le polymorphisme est probablement le plus puissant.

Le polymorphisme est la capacité d'une variable, d'une fonction ou d'un objet à prendre plusieurs formes. Par exemple, dans un langage de programmation qui supporte l'héritage, les classes dans le même arbre hiérarchique peuvent avoir des méthodes avec le même nom mais des _comportements différents_.

### Polymorphisme avec des formes

Regardons un exemple simple :

```python
class Creature():
    def move(self):
        print("la créature se déplace")

class Dragon(Creature):
    def move(self):
        print("le dragon vole")

class Kraken(Creature):
    def move(self):
        print("le kraken nage")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# imprime :
# la créature se déplace
# le dragon vole
# le kraken nage
```

Dans cet exemple, les classes enfants, `Dragon` et `Kraken`, **remplacent** le comportement de la méthode `move()` de leur classe parente.

### Les racines du polymorphisme

Regardez les racines grecques de "polymorphisme".

* "poly" signifie "plusieurs"
* "morph" signifie "changer" ou "forme"

Le polymorphisme en programmation est la capacité de présenter la même interface (signatures de fonction ou de méthode) pour de nombreuses formes sous-jacentes différentes (types de données).

Un exemple classique est une classe `Shape` dont `Rectangle`, `Circle` et `Triangle` peuvent hériter. 

Avec le polymorphisme, chacune de ces classes aura des données sous-jacentes différentes. Le cercle a besoin d'un centre et d'un rayon. Le rectangle a besoin de deux coordonnées pour les coins supérieur gauche et inférieur droit. Le triangle a besoin de coordonnées pour les coins.

En rendant chaque classe responsable de ses données **et** de son code, vous pouvez atteindre le polymorphisme. 

Dans cet exemple, chaque classe aurait sa propre méthode `Draw()`. Cela permet au code qui utilise les différentes formes d'être simple et facile, et plus important encore, il peut traiter les formes comme étant les **mêmes** même si elles sont **différentes**. Il cache les complexités de la différence derrière une abstraction propre.

```python
shapes = [Circle(5, 10), Rectangle(1, 3, 5, 6)]
for shape in shapes:
    print(shape.Draw())
```

Cela contraste avec la manière fonctionnelle de faire les choses où vous auriez eu des fonctions séparées qui ont des **signatures de fonction différentes**, comme `draw_rectangle(x1, y1, x2, y2)` et `draw_circle(center, radius)`.

### Attendez, qu'est-ce qu'une "signature de fonction" ?

Une signature de fonction inclut le nom, les entrées et les sorties d'une fonction ou d'une méthode. Par exemple, ces deux classes ont les mêmes signatures de méthode.

```python
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
```

Les deux méthodes ont le même nom, prennent `0` entrées et retournent des entiers. Si _l'une quelconque_ de ces choses est différente, elles auraient des signatures de fonction différentes.

Voici un exemple de signatures différentes.

```python
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health
```

### Lorsque vous remplacez des méthodes, utilisez la même signature de fonction

Si vous changez la signature de fonction d'une classe parente lorsque vous remplacez une méthode, cela pourrait être une catastrophe. 

Le but de remplacer une méthode est que l'appelant de votre code _n'ait pas à se soucier_ de ce qui se passe de différent à l'intérieur des méthodes de différents types d'objets.

### Surcharge d'opérateur

Un autre type de polymorphisme intégré en Python est la capacité de remplacer un opérateur en Python en fonction des opérandes utilisés.

Les opérateurs arithmétiques fonctionnent pour les types intégrés comme les entiers et les chaînes de caractères.

```python
print(3 + 4)
# imprime "7"

print("three " + "four")
# imprime "three four"
```

Les classes personnalisées, en revanche, n'ont aucun support intégré pour ces opérateurs :

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

Cependant, nous pouvons ajouter notre propre support ! La méthode `__add__` est utilisée par l'interpréteur Python lorsque des instances d'une classe sont ajoutées avec l'opérateur `+`.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 est (6, 8)
```

Lorsque vous appelez `p1 + p2` sous le capot, l'interpréteur appelle simplement `p1.__add__(p2)`.

Voici une liste de la manière dont les opérateurs se traduisent en noms de méthodes. Si vous n'êtes pas familier avec les opérateurs logiques et bit à bit en Python, vous pouvez consulter [cette vidéo](https://www.youtube.com/watch?v=1rUzblmGHzk).

| Opération           | Opérateur | Méthode       |
| ------------------- | -------- | ------------ |
| Addition            | +        | __add__      |
| Soustraction         | -        | __sub__      |
| Multiplication      | *        | __mul__      |
| Puissance               | **       | __pow__      |
| Division            | /        | __truediv__  |
| Division entière      | //       | __floordiv__ |
| Reste (modulo)  | %        | __mod__      |
| Déplacement binaire à gauche  | <<       | __lshift__   |
| Déplacement binaire à droite | >>       | __rshift__   |
| ET binaire         | &        | __and__      |
| OU binaire          | \|       | __or__       |
| OU exclusif binaire         | ^        | __xor__      |
| NON binaire         | ~        | __invert__   |

### Comment surcharger les méthodes intégrées

Dernier point mais non des moindres, examinons certaines des méthodes intégrées que nous pouvons surcharger en Python. Bien qu'il n'y ait pas de comportement par défaut pour les opérateurs arithmétiques comme nous venons de le voir, il _y a_ un comportement par défaut pour **l'impression** d'une classe.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
print(p1)
# imprime "<Point object at 0xa0acf8>"
```

Ce n'est pas super utile ! Apprenons aux instances de notre objet `Point` à s'imprimer elles-mêmes. La méthode `__repr__` (abréviation de "représenter") nous permet de faire exactement cela. Elle ne prend aucune entrée mais retourne une chaîne qui sera imprimée sur la console lorsque quelqu'un passe une instance de la classe à la fonction `print()` de Python.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# imprime "(4,5)"
```

## Excellent Travail pour être Arrivé à la Fin !

Merci de m'avoir accompagné dans ce cours écrit sur la programmation orientée objet. 

Si vous êtes intéressé par les exercices de codage en direct et les quiz pour ce cours, vous pouvez le faire sur le [cours Apprendre la POO](https://boot.dev/learn/learn-object-oriented-programming) sur [Boot.dev](https://boot.dev/). 

Alternativement, si vous souhaitez consulter le prochain cours dans le [parcours de carrière de développeur back-end](https://boot.dev/tracks/computer-science), vous pouvez commencer le [cours Apprendre les Algorithmes](https://boot.dev/learn/learn-algorithms) ici.