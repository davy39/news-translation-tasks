---
title: Apprendre les bases de Python – Un guide pour débutants
subtitle: ''
author: Chepkirui Dorothy
co_authors: []
series: null
date: '2024-02-20T19:04:56.000Z'
originalURL: https://freecodecamp.org/news/learn-python-basics
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/learn-python-image.png
tags:
- name: beginner
  slug: beginner
- name: Python
  slug: python
seo_title: Apprendre les bases de Python – Un guide pour débutants
seo_desc: "Are you eager to dive into the world of programming but unsure where to\
  \ begin? Look no further – Python is an excellent starting point for both newcomers\
  \ and seasoned developers. \nIn this guide, I'll take you through the basics so\
  \ you can get started..."
---

Êtes-vous impatient de plonger dans le monde de la programmation mais vous ne savez pas par où commencer ? Ne cherchez pas plus loin – Python est un excellent point de départ pour les nouveaux venus et les développeurs expérimentés.

Dans ce guide, je vais vous guider à travers les bases afin que vous puissiez commencer votre voyage avec Python.

## Table des matières

<ul>
    <li><a href="#prerequis">Prérequis</a></li>
    <li><a href="#pourquoi-apprendre-python">Pourquoi apprendre Python ?</a></li>
    <li><a href="#caracteristiques-cles-de-python">Caractéristiques clés de Python</a></li>
    <li><a href="#utilisations-pratiques-de-python">Utilisations pratiques de Python</a></li>
    <li><a href="#comment-ecrire-bonjour-le-monde-en-python">Comment écrire "Bonjour le monde" en Python</a></li>
    <li><a href="#variables-et-types-de-donnees-en-python">Variables et types de données en Python</a>
        <ul>
            <li><a href="#types-de-donnees-primitifs-fondamentaux">Types de données primitifs (fondamentaux)</a>
                <ul>
                    <li><a href="#caracteristiques-des-types-de-donnees-primitifs">Caractéristiques des types de données primitifs</a></li>
                    <li><a href="#cas-dutilisation-des-types-de-donnees-primitifs">Cas d'utilisation des types de données primitifs</a></li>
                </ul>
            </li>
            <li><a href="#types-de-donnees-non-primitifs-composites-en-python">Types de données non primitifs (composites) en Python</a>
                <ul>
                    <li><a href="#caracteristiques-des-types-de-donnees-non-primitifs">Caractéristiques des types de données non primitifs</a></li>
                    <li><a href="#cas-dutilisation-des-types-de-donnees-non-primitifs">Cas d'utilisation des types de données non primitifs</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><a href="#operateurs-en-python">Opérateurs en Python</a>
        <ul>
            <li><a href="#operateurs-arithmetiques">Opérateurs arithmétiques</a></li>
            <li><a href="#operateurs-de-comparaison">Opérateurs de comparaison</a></li>
        </ul>
    </li>
    <li><a href="#instructions-en-python">Instructions en Python</a>
        <ul>
            <li><a href="#instructions-daffectation">Instructions d'affectation</a> </li>
                
             <li><a href="#instruction-print">Instruction print</a></li>
               
            
            <li><a href="#instructions-conditionnelles-if-elif-else">Instructions conditionnelles (if, elif, else)</a>
    
                    <li><a href="#boucles-for-et-while">Boucles (for et while)</a>
                        <ul>
                            <li><a href="#boucle-for">Boucle for</a></li>
                            <li><a href="#boucle-while">Boucle while</a></li>
                        
                    </li></ul> </li>
                    <li><a href="#instructions-break-et-continue">Instructions break et continue</a></li>
                
           
        </ul>
    </li>
    <li><a href="#fonctions-en-python">Fonctions en Python</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
</ul>


### Prérequis

Avant de vous lancer dans cette aventure de codage, assurez-vous d'avoir ce qui suit :

* [Python installé](https://www.python.org/downloads/).
* Un éditeur de code comme [VSCode](https://code.visualstudio.com/download), [Vim](https://www.vim.org/download.php), ou [Sublime](https://www.sublimetext.com/3).

Maintenant, explorons les avantages de l'utilisation de Python.

## Pourquoi apprendre Python ?

Si vous vous demandez pourquoi Python est un excellent choix pour les débutants et les développeurs expérimentés, voici quelques raisons :

* **Lisibilité et simplicité :** La syntaxe claire de Python améliore la lisibilité du code, réduisant le temps de développement et le rendant accessible aux débutants.
* **Polyvalence :** Vous pouvez utiliser Python pour construire une grande variété d'applications, du développement web à la science des données et à l'IA. Il dispose également d'une bibliothèque standard étendue et de nombreux packages tiers utiles.
* **Communauté et documentation :** Python dispose d'une communauté robuste et d'une documentation complète qui offre un soutien important, favorisant la popularité et la croissance du langage.
* **Compatibilité multiplateforme :** Assure une exécution transparente sur Windows, macOS et Linux.
* **Bibliothèques et frameworks étendus :** Un écosystème riche simplifie les tâches complexes, faisant gagner du temps et des efforts aux développeurs.

Espérons que vous êtes intrigué par les avantages de Python – alors plongeons dans ses caractéristiques clés.

## Caractéristiques clés de Python

Comprendre les caractéristiques clés de Python vous donnera un aperçu de ses forces et de sa popularité parmi les développeurs :

* **Langage interprété :** Votre code n'est pas directement traduit par la machine cible. Au lieu de cela, un programme spécial appelé interpréteur lit et exécute le code, permettant une exécution multiplateforme de votre code.
* **Typage dynamique :** Le typage dynamique élimine le besoin de déclarations explicites de types de données, améliorant la simplicité et la flexibilité.
* **Orienté objet :** Python supporte les principes orientés objet, favorisant la modularité et la réutilisabilité du code.
* **Syntax basée sur l'indentation :** La syntaxe basée sur l'indentation impose la lisibilité du code et maintient un style de codage cohérent.
* **Gestion de la mémoire :** La gestion automatique de la mémoire par le ramasse-miettes simplifie la gestion de la mémoire pour les développeurs.

## Utilisations pratiques de Python

La polyvalence et la lisibilité de Python le rendent adapté à une large gamme d'applications. Voici quelques utilisations pratiques :

* **Développement web :** Python, avec des frameworks comme Django et Flask, alimente le développement backend pour des applications web robustes.
* **Science des données et apprentissage automatique :** Largement utilisé en science des données, les bibliothèques de Python comme NumPy et Pandas supportent l'analyse de données et l'apprentissage automatique.
* **Automatisation et scripting :** Python excelle dans l'automatisation des tâches et le scripting, simplifiant les opérations répétitives.
* **IA et TAL :** Python, avec des bibliothèques comme TensorFlow, domine dans les applications d'IA et de traitement du langage naturel.
* **Développement de jeux :** Python, combiné avec Pygame, facilite le développement de jeux 2D pour les amateurs et les développeurs indépendants.
* **Calcul scientifique :** Python est un outil précieux en calcul scientifique, choisi par les scientifiques et les chercheurs pour ses bibliothèques étendues.

Python est préinstallé dans la plupart des distributions Linux. Suivez [cet article](https://www.datacamp.com/blog/how-to-install-python) pour savoir comment installer Python sur Windows et MacOS.

## Comment écrire "Bonjour le monde" en Python

C'est généralement la première réalisation lorsque l'on commence à coder dans n'importe quel langage : faire en sorte que votre code dise 'Bonjour le monde'. Ouvrez n'importe quel éditeur de code de votre choix, et créez un fichier nommé `project.py`. À l'intérieur du fichier, tapez ce qui suit :

```python
     print("Bonjour le monde !")  
     
```

Pour exécuter ce code, ouvrez l'interface de ligne de commande (CLI). Suivez [cet article](https://www.freecodecamp.org/news/command-line-for-beginners/) pour mieux comprendre la CLI.

Assurez-vous d'ouvrir le répertoire où le fichier est enregistré, et exécutez ce qui suit :

```bash
 python3 project.py 
```

Lorsque vous exécutez ce programme, vous verrez le salut intemporel affiché dans votre interface de ligne de commande.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-01-30-11-59-12.png)
_bonjour le monde affiché dans la CLI_

Félicitations ! Vous venez d'exécuter votre premier script Python. Maintenant que vous avez imprimé un message simple, plongeons plus profondément dans Python.

## **Variables et types de données en Python**

Le but principal des ordinateurs est de traiter les données en informations utiles, pour que cela se produise, les données doivent être stockées dans sa mémoire. Cela est réalisé en utilisant les variables et les types de données d'un langage de programmation.

Les types de données en Python sont des types particuliers d'éléments de données, tels que définis par la valeur qu'ils peuvent prendre. Les variables, en revanche, sont comme des conteneurs étiquetés qui stockent ces données. Elles vous permettent de gérer et de modifier des informations en utilisant des identifiants spécifiques.

Les types de données sont généralement classés en deux types :

### Types de données primitifs (fondamentaux) :

Les types de données primitifs représentent des valeurs simples. Ces types de données sont les unités les plus basiques et essentielles utilisées pour stocker et manipuler des informations dans un programme. Ils se traduisent directement en code machine de bas niveau. 

Les types de données primitifs incluent :

* **Chaîne de caractères (`str`) :** Représente des séquences de caractères. Doit être encadré par des guillemets. Exemple : `"Bonjour, Python !"`
* **Entier (`int`) :** Représente des nombres entiers sans décimales. Exemple : `42`
* **Flottant (`float`) :** Représente des nombres avec des décimales. Exemple : `3.14`
* **Booléen (`bool`) :** Représente soit `True` soit `False`.

#### Caractéristiques des types de données primitifs :

* **Immuabilité :** Les types de données primitifs sont immuables, ce qui signifie que leurs valeurs ne peuvent pas être changées après leur création. Toute opération qui semble modifier une valeur primitive crée une nouvelle valeur.
* **Représentation directe :** Chaque type de données primitif correspond directement à une représentation spécifique de code machine de bas niveau.
* **Valeurs atomiques :** Les types de données primitifs représentent des valeurs individuelles et atomiques. Ils ne sont pas composés d'autres types ou structures.

#### Cas d'utilisation des types de données primitifs :

* Les chaînes de caractères sont utilisées pour la manipulation et la représentation de texte.
* Les entiers et les flottants sont essentiels pour les calculs numériques.
* Les booléens sont employés dans les opérations logiques et la prise de décision.

Voyons comment cela fonctionne en continuant à écrire du code Python.

Modifiez votre fichier `project.py` pour inclure ce qui suit :

```python
# Exemple de chaîne de caractères 
nom = "John"
# Exemple d'entier
age = 25 
# Exemple de flottant 
taille = 1.75 
# Exemple de booléen
est_etudiant = True
# Afficher les valeurs des variables 
print("Nom :", nom) 
print("Âge :", age) 
print("Taille :", taille)
print("Est étudiant ?", est_etudiant)
```

Dans cet extrait, vous avez introduit des variables avec différents types de données. Exécutez le programme et observez comment Python gère ces types de données.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-01-30-12-02-11.png)
_types de données primitifs_

La sortie révèle les valeurs assignées aux variables dans le script Python. Les instructions `print` affichent le contenu des variables `nom`, `age`, `taille` et `est_etudiant`. 

### Types de données non primitifs (composites) en Python

Les types de données non primitifs sont des structures qui peuvent contenir plusieurs valeurs et sont composés d'autres types de données, y compris des types primitifs et d'autres types composites. Contrairement aux types de données primitifs, les types non primitifs permettent des représentations de données plus complexes et structurées.

Les types de données non primitifs incluent :

* **Liste (`list`) :** Représente une collection ordonnée et mutable de valeurs. Exemple : `fruits = ["pomme", "banane", "cerise"]`
* **Tuple (`tuple`) :** Représente une collection ordonnée et immuable de valeurs. Exemple : `coordonnées = (3, 7)`
* **Dictionnaire (`dict`) :** Représente une collection non ordonnée de paires clé-valeur. Exemple : `personne = {"nom": "Alice", "age": 25, "est_etudiant": True}`

#### Caractéristiques des types de données non primitifs :

* **Mutabilité :** Les listes sont mutables, ce qui signifie que leurs éléments peuvent être modifiés après la création. Les tuples, en revanche, sont immuables – leurs éléments ne peuvent pas être changés. Les dictionnaires sont mutables – vous pouvez ajouter, modifier ou supprimer des paires clé-valeur.
* **Collection de valeurs :** Les types de données non primitifs permettent le regroupement de plusieurs valeurs dans une seule structure, permettant la création de représentations de données plus sophistiquées.
* **Ordonné (Listes et Tuples) :** Les listes et les tuples maintiennent l'ordre des éléments, permettant un indexage prévisible.
* **Mappage clé-valeur (Dictionnaire) :** Les dictionnaires mappent les clés aux valeurs, fournissant un moyen d'organiser et de récupérer des données basées sur des identifiants spécifiques.

#### Cas d'utilisation des types de données non primitifs :

* **Listes :** Utile lorsque vous avez besoin d'une collection qui peut être altérée pendant l'exécution du programme, comme maintenir une liste d'éléments qui peuvent changer avec le temps.
* **Tuples :** Adapté lorsque vous voulez vous assurer que les données restent constantes et ne peuvent pas être modifiées accidentellement. Souvent utilisé pour représenter des ensembles fixes de valeurs.
* **Dictionnaires :** Idéal pour les scénarios où les données doivent être associées à des étiquettes ou des clés spécifiques. Ils offrent une récupération efficace des données basée sur ces identifiants.

Très bien, continuons avec notre code Python – modifiez le fichier `project.py` comme montré ci-dessous :

```python
# Exemple de liste
fruits = ["pomme", "banane", "cerise"]
print("Exemple de liste :", fruits)

# Exemple de tuple
coordonnées = (3, 7)
print("Exemple de tuple :", coordonnées)

# Exemple de dictionnaire
personne = {"nom": "Alice", "age": 25, "est_etudiant": True}
print("Exemple de dictionnaire :", personne)

```

Exécutez le programme pour voir comment les listes et les tuples vous permettent d'organiser et de stocker des données. Dans cet extrait de code :

* La variable `fruits` est une liste contenant des chaînes de caractères représentant différents fruits.
* La variable `coordonnées` est un tuple avec deux entiers représentant des coordonnées.
* La variable `personne` est un dictionnaire associant des clés ("nom", "age", "est_etudiant") avec des valeurs correspondantes.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-01-31-11-19-39.png)
_types de données non primitifs_

Vous pouvez effectuer diverses opérations sur ces structures, comme ajouter des éléments à une liste ou accéder à des éléments individuels dans un tuple.

Les types de données sont cruciaux pour plusieurs raisons :

* **Allocation de mémoire :** Différents types de données nécessitent différentes quantités de mémoire. Connaître le type de données permet à l'ordinateur d'allouer la quantité appropriée de mémoire pour une variable.
* **Opérations :** Chaque type de données supporte des opérations spécifiques. Par exemple, vous pouvez additionner deux nombres `entiers`, concaténer deux `chaînes de caractères`, ou comparer deux valeurs `booléennes`.
* **Prévention des erreurs :** Utiliser le mauvais type de données dans une opération peut entraîner des erreurs. Les types de données aident à prévenir les conséquences involontaires en imposant des règles sur la manière dont différents types peuvent interagir.

## Opérateurs en Python

Les opérateurs en Python sont des symboles qui effectuent des opérations sur des variables et des valeurs. 
Un opérande fait référence aux entrées ou objets sur lesquels une opération est effectuée.

Explorons certains des opérateurs essentiels en Python :

### Opérateurs arithmétiques :

Les opérateurs arithmétiques sont des composants fondamentaux de tout langage de programmation, permettant aux développeurs d'effectuer des opérations mathématiques de base sur des valeurs numériques. 

En Python, plusieurs opérateurs arithmétiques vous permettent de réaliser des calculs efficacement. Explorons ces opérateurs :

* Addition (+) : Additionne deux opérandes.
* Soustraction (-) : Soustrait l'opérande de droite de l'opérande de gauche.
* Multiplication (*) : Multiplie deux opérandes.
* Division (/) : Divise l'opérande de gauche par l'opérande de droite (retourne toujours un flottant).
* Modulo (%) : Retourne le reste de la division de l'opérande de gauche par l'opérande de droite.
* Exponentiation (**) : Élève l'opérande de gauche à la puissance de l'opérande de droite.

Modifiez votre fichier `project.py` pour inclure des exemples de ces opérateurs :

```python
 # Opérateurs arithmétiques
 num1 = 10 
 num2 = 3 
 resultat_add = num1 + num2 
 resultat_sous = num1 - num2 
 resultat_mult = num1 * num2 
 resultat_div = num1 / num2 
 resultat_mod = num1 % num2 
 resultat_exp = num1 ** num2 
 print("Addition :", resultat_add) 
 print("Soustraction :", resultat_sous)
 print("Multiplication :", resultat_mult) 
 print("Division :", resultat_div) 
 print("Modulo :", resultat_mod) 
 print("Exponentiation :", resultat_exp)  
```

Le code ci-dessus initialise deux variables, `num1` et `num2`, avec les valeurs `10` et `3` respectivement, représentant deux opérandes numériques.

Ensuite, des opérations arithmétiques sont effectuées en utilisant ces opérandes :

* `resultat_add` stocke le résultat de l'addition de `num1` et `num2`.
* `resultat_sous` stocke le résultat de la soustraction de `num2` de `num1`.
* `resultat_mult` stocke le résultat de la multiplication de `num1` et `num2`.
* `resultat_div` stocke le résultat de la division de `num1` par `num2`.
* `resultat_mod` stocke le reste de la division de `num1` par `num2`.
* `resultat_exp` stocke le résultat de l'élévation de `num1` à la puissance de `num2`.

Enfin, les résultats de ces opérations arithmétiques sont imprimés en utilisant des instructions `print()`, chacune étiquetée de manière appropriée, comme "Addition :", "Soustraction :", et ainsi de suite, suivies du résultat correspondant.

 Voici la sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/arithmetic.png)
_opérations arithmétiques_

### Opérateurs de comparaison

Les opérateurs de comparaison en Python sont des outils essentiels pour évaluer et comparer des valeurs. Ils vous permettent d'exprimer des conditions et de prendre des décisions basées sur la relation entre différentes valeurs. Ils retournent soit `True` soit `False` en fonction du résultat de la comparaison.

Voici les opérateurs de comparaison courants :

* Égal à (==) : Vérifie si deux opérandes sont égaux.
* Différent de (!=) : Vérifie si deux opérandes ne sont pas égaux.
* Supérieur à (>) : Vérifie si l'opérande de gauche est supérieur à l'opérande de droite.
* Inférieur à (<) : Vérifie si l'opérande de gauche est inférieur à l'opérande de droite.
* Supérieur ou égal à (>=) : Vérifie si l'opérande de gauche est supérieur ou égal à l'opérande de droite.
* Inférieur ou égal à (<=) : Vérifie si l'opérande de gauche est inférieur ou égal à l'opérande de droite.

Étendez votre fichier `project.py` pour inclure des exemples d'opérateurs de comparaison :

```python
 # Opérateurs de comparaison 
 age = 25
 est_adulte = age >= 18
 est_adolescent = age >= 13 and age < 18
 print("Est adulte ?", est_adulte)
 print("Est adolescent ?", est_adolescent)       
```

La variable `age` est initialisée avec la valeur `25`, représentant l'âge d'une personne.

Ensuite, l'opérateur de comparaison `>=` est utilisé pour évaluer si `age` est supérieur ou égal à `18`. Le résultat de cette comparaison détermine la valeur booléenne stockée dans la variable `est_adulte`. Si l'âge est `18` ou plus, `est_adulte` sera `True`, indiquant l'âge adulte.

Ensuite, l'opérateur logique `and` est utilisé pour combiner deux opérations de comparaison. La première comparaison, `age >= 13`, vérifie si l'âge est `13` ou plus. La deuxième comparaison, `age < 18`, assure que l'âge est inférieur à `18`. Si les deux conditions sont vraies, `est_adolescent` sera `True`, signifiant les années d'adolescence.

Enfin, les résultats sont imprimés en utilisant des instructions `print()`, indiquant si la personne est classée comme adulte (`True` ou `False`) et si elle est identifiée comme un adolescent (`True` ou `False`).

Voici la sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/is-adult.png)

## Instructions en Python

Les instructions indiquent à l'interpréteur d'effectuer des actions ou des opérations spécifiques. Ces actions peuvent aller de simples affectations de valeurs à des variables à des structures de contrôle de flux et des itérations plus complexes. 

Comprendre les différents types d'instructions est essentiel pour écrire un code Python efficace et expressif.

### Instructions d'affectation

Les instructions d'affectation sont le type d'instruction le plus basique en Python. Elles sont utilisées pour affecter des valeurs à des variables, créant une référence nommée aux données. 

Voici un exemple :

```python
x = 10 
nom = "Alice" 
```

Dans cet extrait, `x` est affecté de la valeur entière `10`, et `nom` est affecté de la chaîne de caractères `"Alice"`. Ces affectations créent des variables qui peuvent être utilisées dans tout le programme.

### Instruction print

L'instruction print est utilisée pour afficher la sortie dans la console. C'est un outil crucial pour le débogage et la fourniture d'informations aux utilisateurs. Exemple :

```python
print("Bonjour, Python !")  
```

Ce code imprime la chaîne "Bonjour, Python !" dans la console.

### Instructions conditionnelles (if, elif, else)

Les instructions conditionnelles sont utilisées lorsque vous souhaitez exécuter différents blocs de code en fonction de certaines conditions. 

Supposons que vous souhaitiez déterminer si une personne a atteint l'âge légal pour boire. Modifiez le fichier `project.py` avec le code suivant :

```python
# Exemple d'instruction conditionnelle 
age = 20
if age < 18:
    print("Vous êtes mineur.")
elif 18 <= age < 21:
    print("Vous êtes un adulte, mais pas encore autorisé à boire.")
else:
    print("Vous êtes un adulte légal.")

```

Dans cet exemple :

* L'instruction `if` vérifie si `age` est inférieur à 18.
* L'instruction `elif` (abréviation de else if) vérifie si `age` est entre 18 (inclus) et 21 (exclus).
* L'instruction `else` est exécutée si aucune des conditions ci-dessus n'est remplie.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/drinking.png)
_instruction if else_

Une personne âgée de 20 ans n'est pas autorisée à boire.

### Boucles (for et while) 

Les boucles sont utilisées pour répéter un bloc de code plusieurs fois. Il existe deux principaux types de boucles en Python : les boucles `for` et les boucles `while`.

#### Boucle for :

Une boucle `for` est utilisée lorsque vous connaissez le nombre d'itérations à l'avance. Supposons que vous avez une liste contenant les noms de fruits, et que vous souhaitez imprimer chaque fruit. Dans ce cas, une boucle `for` est un choix idéal pour itérer sur les éléments de la liste. 

Voici un exemple utilisant Python :

```python
# Exemple de boucle for 
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)

```

Dans cet exemple, la boucle `for` itère sur chaque élément de la liste `fruits` et imprime chaque fruit.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/apple.png)
_liste de fruits dans la boucle for_

#### Boucle while :

Une instruction `while` est une instruction de contrôle de flux qui vous permet d'exécuter un bloc de code de manière répétée tant qu'une condition spécifiée est vraie.  

Supposons que vous souhaitez simuler un comptage jusqu'à ce qu'un certain seuil soit atteint. Modifiez votre `project.py` et ajoutez le code suivant :

```python
# Exemple de boucle while 
compte = 0
while compte < 5:
    print("Compte :", compte)
    compte += 1

```

Dans ce scénario, la boucle `while` continue à s'exécuter tant que la variable `compte` est inférieure à 5. Le code à l'intérieur de la boucle incrémente le compte et imprime le compte actuel à chaque itération. 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/count.png)
_sortie de la boucle while_

### Instructions break et continue

Les instructions break et continue sont utilisées dans les boucles.

* `break` : Quitte la boucle.
* `continue` : Saute le reste du code à l'intérieur de la boucle pour l'itération actuelle, puis continue la boucle.

 Exemples :

```python
# Exemple d'instruction break 
print("Sortie avec 'break' :")
for i in range(5):
    if i == 3:
        print(f"Rencontre 'break' à i={i}") 
        break
    print(i)

# Exemple d'instruction continue 
print("\nSortie avec 'continue' :")
for i in range(5):
    if i == 2:
        print(f"Itération sautée avec 'continue' à i={i}")
        continue
    print(i)

```

Dans l'exemple `break`, la boucle s'arrête lorsque `i` est égal à 3, et les nombres 0, 1 et 2 sont imprimés. 

Dans l'exemple `continue`, lorsque `i` est égal à 2, l'instruction `continue` saute l'instruction `print(i)` pour cette itération, résultant en l'omission du nombre 2 dans la sortie.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/break1.png)
_sortie des instructions break et continue_

## Fonctions en Python

Les fonctions sont des blocs de code réutilisables, améliorant la modularité en enfermant la fonctionnalité dans des unités séparées et organisées. Cette approche aide à éviter la duplication de code et améliore considérablement la lisibilité du code. 

À l'intérieur du fichier `project.py`, écrivez le code suivant :

```python
def saluer():
    print("Bonjour le monde !")

# Appeler la fonction pour l'exécuter
saluer()

```

Le code ci-dessus contient une fonction Python simple appelée `saluer()`. Lorsqu'elle est 'appelée' ou 'invoquée', cette fonction imprime "Bonjour le monde !" dans la console. C'est un exemple basique illustrant le fonctionnement des fonctions en Python.

Vous pouvez aller plus loin en incluant des paramètres. Les paramètres servent de placeholders pour les valeurs passées à une fonction lors de son invocation, permettant aux fonctions d'accepter des entrées et d'effectuer des opérations basées sur ces entrées.

Modifiez l'exemple précédent sur l'instruction `if elif else` pour inclure des fonctions :

```python
def verifier_age(age):
    if age < 18:
        print("Vous êtes mineur.")
    elif 18 <= age < 21:
        print("Vous êtes un adulte, mais pas encore autorisé à boire.")
    else:
        print("Vous êtes un adulte légal.")

# Appeler la fonction avec un âge spécifique
verifier_age(20)


```

Dans cet exemple, la fonction `verifier_age` prend un paramètre `age` et effectue la même vérification conditionnelle que le code original. La fonction vous permet de réutiliser cette logique pour différentes valeurs d'âge en appelant simplement la fonction avec l'âge souhaité.

Vous pouvez appeler la fonction `verifier_age` avec n'importe quelle valeur d'âge, et elle imprimera le message approprié en fonction de l'âge fourni.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-02-07-13-03-23.png)
_fonctions_

## Conclusion

En commençant votre voyage d'apprentissage de Python, ce guide vous présente les avantages de l'apprentissage de Python, ses caractéristiques clés et ses cas d'utilisation pratiques. 

En commençant par l'iconique "Bonjour le monde !" et en progressant à travers les variables, les types de données, les instructions et les fonctions, vous avez acquis une certaine expérience pratique avec les bases de Python. Nous avons également parlé des types de données primitifs et non primitifs, des instructions conditionnelles et des boucles.

Au fur et à mesure que votre voyage progresse, plongez dans des sujets avancés comme la programmation orientée objet, la gestion des fichiers et les projets du monde réel. Armé de connaissances fondamentales, vous pouvez maintenant embrasser les défis de codage qui se présentent à vous. Restez curieux et savourez le processus gratifiant de coder avec Python. Bon codage !



