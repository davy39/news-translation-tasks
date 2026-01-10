---
title: Le guide d'exemples de code Python
date: '2023-08-22T21:54:38.000Z'
author: Farhan Hasin Chowdhury
authorURL: https://www.freecodecamp.org/news/author/farhanhasin/
originalURL: https://freecodecamp.org/news/the-python-code-example-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Learn-Python-with-Code-Examples-Handbook-Cover.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: example
  slug: example
- name: handbook
  slug: handbook
- name: Python
  slug: python
seo_desc: 'Very few programming languages are as universally loved as Python. The
  brainchild of Dutch programmer Guido van Rossum, Python is easy to learn, powerful,
  and an utter joy to work with.

  Thanks to its popularity, video and written resources about Pyth...'
---


Très peu de langages de programmation sont aussi universellement appréciés que Python. Fruit de l'imagination du programmeur néerlandais Guido van Rossum, Python est facile à apprendre, puissant et c'est un pur plaisir de travailler avec.

<!-- more -->

Grâce à sa popularité, les ressources vidéo et écrites sur Python sont abondantes. Ce manuel, cependant, tente d'être un peu différent en ne se voulant pas un guide définitif du langage.

À la place, vous découvrirez tous les sujets que je considère comme les fondamentaux du langage avec de nombreux exemples de code.

Je n'ai pas abordé la programmation orientée objet dans ce manuel car j'estime qu'il s'agit d'un sujet très vaste qui mérite son propre manuel séparé.

Vers la fin, j'ai également listé quelques ressources d'apprentissage pour approfondir vos connaissances sur Python et la programmation en général.

Sans plus attendre, lançons-nous !

## Table des matières

-   [Prérequis][1]
-   [Comment installer Python sur votre ordinateur][2]
-   [Comment installer un IDE Python sur votre ordinateur][3]
-   [Comment créer un nouveau projet dans PyCharm][4]
-   [Comment écrire le programme Hello World en Python][5]
-   [Comment initialiser et publier un dépôt Git depuis PyCharm][6]
-   [Comment travailler avec les variables et les différents types de données en Python][7]
-   [Comment travailler avec les nombres simples en Python][8]
-   [Comment récupérer les entrées utilisateur en Python][9]
-   [Comment travailler avec les chaînes de caractères en Python][10]
-   [Quels sont les types de séquences en Python ?][11]
    -   [Les listes en Python][12]
    -   [Les tuples en Python][13]
    -   [Les ranges en Python][14]
    -   [Comment fonctionne l'indexation en Python][15]
-   [Quels sont les types itérables et comment les utiliser pour les boucles en Python][16]
-   [Comment utiliser les boucles While en Python][17]
-   [Comment écrire des boucles imbriquées en Python][18]
-   [Quelles sont les opérations courantes sur les types de séquences en Python ?][19]
    -   [Comment utiliser l'opérateur in en Python][20]
    -   [Comment utiliser les opérateurs + et \* avec les types de séquences en Python][21]
    -   [Comment utiliser les fonctions len(), min() et max() en Python][22]
-   [Quelles sont les opérations sur le type chaîne de caractères en Python ?][23]
    -   [Comment mettre en majuscule des chaînes de caractères en Python][24]
    -   [Comment convertir des chaînes en minuscules ou en majuscules en Python][25]
    -   [Comment compter le nombre d'occurrences d'une sous-chaîne dans une chaîne en Python][26]
    -   [Comment diviser et joindre des chaînes de caractères en Python][27]
-   [Comment écrire des instructions conditionnelles en Python][28]
-   [Quels sont les opérateurs relationnels et logiques en Python ?][29]
-   [Quels sont les opérateurs d'affectation en Python ?][30]
-   [Qu'est-ce que le type Set en Python ?][31]
-   [Qu'est-ce que le type Mapping en Python ?][32]
    -   [Que sont les objets de vue de dictionnaire en Python ?][33]
-   [Comment écrire des fonctions en Python][34]
    -   [Comment écrire des fonctions anonymes ou lambda en Python][35]
    -   [Comment travailler avec les variables locales, non locales et globales en Python][36]
    -   [Comment passer un nombre variable d'arguments à une fonction en utilisant \*args et \*\*kwargs en Python][37]
-   [Que sont les modules en Python ?][38]
-   [Comment utiliser efficacement la documentation Python][39]
-   [Quelle est la suite ?][40]
    -   [Programmation Orientée Objet][41]
    -   [Algorithmes et structures de données][42]
    -   [Django][43]
    -   [Qt][44]
    -   [PyGame][45]
    -   [Data Science][46]
-   [Conclusion][47]

## **Prérequis**

Vous n'avez pas besoin de connaître d'autre langage de programmation pour ce livre, mais en connaître un peut vous aider à comprendre les bases de Python.

En dehors de cela, vous devrez être suffisamment à l'aise avec votre système d'exploitation pour télécharger et installer de nouveaux logiciels, et obtenir un accès administratif si nécessaire.

## Comment installer Python sur votre ordinateur

L'installation de Python sur votre ordinateur est un processus très simple. En fait, si vous êtes sur un système Linux, Python devrait déjà être installé.

Ouvrez votre fenêtre de terminal et exécutez la commande suivante :

```
python --version
```

Si Python est installé sur votre système, vous obtiendrez une sortie comme `Python 3.10.4` ou une autre version mineure.

Bien que la plupart des distributions Linux modernes utilisent Python 3 par défaut, certaines distributions plus anciennes peuvent encore utiliser Python 2 par défaut.

Si la commande susmentionnée fait référence à Python 2, essayez la commande suivante :

```
python3 --version
```

Je vous suggère également de vérifier les mises à jour de votre distribution Linux et d'installer toutes les nouvelles mises à jour pour Python.

Bien que Python soit également préinstallé avec macOS, je vous suggère de suivre cet article de [Dillion Megida][48] pour installer une version plus récente.

[https://www.freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide/][49]

Enfin, pour Windows, je vous suggère de suivre un article de [Md. Fahim Bin Amin][50] pour installer correctement la dernière version de Python.

[https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/][51]

Tant que vous avez une version de Python 3 installée, tout est prêt.

## Comment installer un IDE Python sur votre ordinateur

Une grande partie de votre expérience en tant que développeur dépendra du programme que vous avez choisi pour écrire votre code. Un bon environnement de développement intégré (IDE) ou éditeur de code peut vraiment booster votre productivité.

De nos jours, [Visual Studio Code][52] est devenu l'éditeur de code de référence pour tous les langages et plateformes. Mais par souci de simplicité, nous utiliserons [PyCharm][53] dans ce livre.

Si vous souhaitez utiliser VS Code, j'ai écrit un article complet sur [comment configurer Visual Studio Code pour le développement Python][54]. N'hésitez pas à le consulter si la configuration manuelle de votre éditeur ne vous dérange pas.

L'édition professionnelle de l'IDE [peut vous coûter 89,00 $ par an][55], mais il existe également une édition communautaire gratuite et open-source. Rendez-vous sur la [page de téléchargement de PyCharm][56].

![Image](https://www.freecodecamp.org/news/content/images/2024/04/download-pycharm-page.png) _Page de téléchargement de PyCharm_

Utilisez le bouton noir "Download" pour télécharger l'édition communautaire. La taille du fichier devrait être légèrement supérieure à 350 mégaoctets.

Sur Windows, vous obtiendrez un installateur exécutable, sur macOS une image disque Apple, et sur Linux une archive TAR.

Je ne ferai pas de démonstration du processus d'installation dans ce livre car il est similaire à l'installation de n'importe quel autre logiciel sur votre machine.

Une fois installé, vous pouvez lancer l'IDE depuis votre menu de démarrage/lanceur d'applications. Lors de votre premier lancement, vous aurez la possibilité de configurer quelques éléments. Je vous suggère de conserver les valeurs par défaut.

Une fois l'assistant de configuration terminé, vous devriez voir la fenêtre de bienvenue suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-469.png) _Écran de bienvenue de PyCharm - avec les options pour démarrer un nouveau projet, ouvrir un projet ou en obtenir un depuis votre VCS_

Choisir un IDE ou un éditeur de code plutôt qu'un autre n'affectera pas votre expérience avec ce manuel, alors n'hésitez pas à utiliser celui avec lequel vous vous sentez à l'aise.

## Comment créer un nouveau projet dans PyCharm

Si la fenêtre de bienvenue de la section précédente est ouverte, cliquez sur le bouton "New Project".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/start-a-new-project-in-pycharm.png) _Démarrer un nouveau projet dans PyCharm_

À l'étape suivante, choisissez un emplacement pour stocker votre projet :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-472.png)

Dans la zone de saisie de l'emplacement, la partie `HelloWorld` est le nom du projet. Assurez-vous ensuite que "New environment using Virtualenv" est sélectionné. Ensuite, vérifiez que la version correcte de Python est sélectionnée dans le menu déroulant "Base interpreter".

[Virtualenv][57] est un programme qui peut créer des environnements Python isolés à partir d'un interpréteur de base donné. C'est très utile car plus tard, lorsque vous travaillerez sur plusieurs projets Python, leurs dépendances pourraient entrer en conflit.

Créer des environnements isolés pour chaque projet résoudra ce problème et cela gardera également votre installation globale de Python exempte de toute installation de paquet inutile.

Puisqu'il s'agit peut-être de votre premier projet Python, je vous suggère de laisser l'option "Create a main.py welcome script" cochée. Une fois que vous êtes satisfait de vos choix, cliquez sur le bouton "Create".

Le processus de création du projet ne devrait pas prendre très longtemps. Une fois terminé, l'IDE devrait ouvrir le projet automatiquement pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-473.png)

Vous pouvez utiliser le bouton de lecture dans le coin supérieur droit pour exécuter le code. Le bouton est configuré pour exécuter le fichier "main.py" par défaut.

C'est pourquoi vous pouvez voir "main" écrit à côté. Vous pouvez également écrire votre configuration personnalisée, mais c'est un sujet pour une section ultérieure.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-474.png)

Vous pouvez voir la sortie de votre programme en bas de l'IDE. PyCharm prend en charge les commentaires TODO, possède un terminal intégré et plus encore. Vous découvrirez un grand nombre de ces fonctionnalités au fur et à mesure.

## Comment écrire le programme Hello World en Python

En continuant sur la lancée de la dernière section, ouvrez le fichier "main.py" et remplacez tout le code préexistant par la ligne de code suivante :

```
print('Hello, World!')

# Hello, World!
```

La fonction `print()` affiche tout ce que vous passez entre les parenthèses. Vous n'êtes pas obligé de nommer votre fichier Python spécifiquement "main.py". C'est juste une façon de faire savoir qu'il s'agit du point d'entrée de ce programme.

C'est tout ce dont vous avez besoin pour écrire le programme exécutable le plus simple en Python. Mais il existe une manière encore meilleure de le faire. Mettez à jour le code comme suit :

```
def main():
    print('Hello, World!')


if __name__ == '__main__':
    main()

# Hello, World!
```

Au fur et à mesure que vous travaillerez sur des projets plus importants, vous finirez par avoir plus d'un fichier Python dans votre projet et cette façon d'écrire un script peut être utile.

Pour simuler un projet plus important, créez un autre fichier Python en faisant un clic droit sur le nom du projet "HelloWorld" et en sélectionnant "Python File" sous le sous-menu "New".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image.png)

Nommez votre fichier quelque chose comme "library" et appuyez sur Entrée pendant que "Python file" est en surbrillance dans la liste des types de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-1.png)

Un nouveau fichier nommé "library.py" apparaîtra dans votre dossier de projet. Mettez la ligne de code suivante à l'intérieur du fichier :

```
def greet():
    print('Hello, World!')
```

Il s'agit d'une fonction très simple qui affiche "Hello, World!" sur la console. Vous pouvez `import` et utiliser cette fonction dans votre fichier "main.py".

Pour ce faire, mettez à jour le code du fichier "main.py" comme suit :

```
from library import greet


def main():
    greet()


if __name__ == '__main__':
    main()

# Hello, World!
```

Vous importez la fonction `greet()` du fichier "library.py" et vous l'exécutez à l'intérieur de la fonction `main()`.

Actuellement, dans votre projet, vous avez deux types de fichiers Python. Vous avez le fichier "main.py" qui est un script. En d'autres termes, vous pouvez exécuter ce fichier.

Ensuite, vous avez le fichier "library.py" qui est une bibliothèque. En d'autres termes, il héberge un certain nombre de fonctions et de variables utiles que vous pouvez importer dans d'autres fichiers Python.

Imaginez maintenant que vous ayez des centaines de fichiers dans votre projet et qu'ils se ressemblent plus ou moins tous. Comment quelqu'un d'autre trouverait-il le point d'entrée du programme ?

Le moyen le plus simple serait d'effectuer une recherche sur la ligne `if __name__ == '__main__'` dans tout le projet. Cela rend votre code beaucoup plus lisible.

Maintenant que je vous ai convaincu que c'est la voie à suivre, laissez-moi vous expliquer ce qui se passe réellement ici.

`__name__` est une variable spéciale de Python. Dans le cas d'un script, la valeur de cette variable sera `__main__` et dans le cas d'une bibliothèque, sa valeur sera le nom de ce fichier.

Ainsi, dans le programme susmentionné, la valeur de `__name__` à l'intérieur du fichier "main.py" sera `__main__` et `library` à l'intérieur du fichier "library.py".

Si vous changez le nom du fichier "main.py" en autre chose, la valeur sera toujours `__main__` car il s'agit d'un script.

Rien n'empêche le fichier "library.py" d'être un script, cependant. Si vous exécutez ce fichier à la place, il deviendra un script.

Dans des langages comme C/C++/Go/Java, vous aurez une fonction `main` spécifiée. Cette fonction sera le point d'entrée du programme.

Comme Python n'a rien de tel, l'utilisation de l'expression `if __name__ == '__main__'` impose un sentiment de point d'entrée spécifié à votre programme.

Cela indique au programmeur et à l'IDE que ce script est destiné à l'exécution (et non à l'importation dans d'autres fichiers Python).

## Comment initialiser et publier un dépôt Git depuis PyCharm

Vous connaissez peut-être déjà [Git][58] et savez comment initialiser un nouveau dépôt. Si vous préférez utiliser un autre client Git, c'est tout à fait possible.

Cependant, je pense que savoir comment effectuer des commits directement depuis votre IDE peut booster votre productivité.

Gardez à l'esprit que vous devrez avoir Git installé et configuré sur votre système. Si ce n'est pas le cas, [cet article][59] de [Bolaji Ayodeji][60] pourrait vous être utile.

Maintenant, en continuant sur la lancée de la dernière section, si vous regardez en bas de votre IDE, vous devriez voir un onglet "Version Control".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-2-1.png)

Cliquez dessus et vous devriez passer à l'onglet de contrôle de version. Cliquez maintenant sur le lien "Create Git repository...".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-3-1.png)

PyCharm vous demandera où vous souhaitez initialiser le nouveau dépôt. Assurez-vous de choisir le bon dossier.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-4.png)

Dès que vous appuyez sur le bouton "OK", l'onglet "Version Control" se transformera en onglet "Git".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-5-1.png)

Dans son état actuel, il n'y a pas de commits. Avant de faire votre premier commit, je vous suggère d'ajouter un fichier ".gitignore" afin qu'aucun fichier indésirable ne parvienne au dépôt.

Pour générer un nouveau fichier gitignore, rendez-vous sur le site [gitignore.io][61]. Vous pouvez générer des fichiers gitignore pour un grand nombre de technologies à partir de ce site.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-6.png)

Vous écrivez le nom des technologies pour lesquelles vous souhaitez générer le fichier. Je choisis généralement "Python", "PyCharm" et j'appuie sur le bouton "Create".

Le site affichera le contenu de votre fichier ".gitignore" souhaité. Sélectionnez et copiez tout à partir de là et retournez sur PyCharm.

Pour simuler cela, créez un nouveau fichier dans votre projet en faisant un clic droit sur le nom du projet "HelloWorld" et en sélectionnant "File" sous le sous-menu "New".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-7.png)

Nommez votre fichier ".gitignore" et appuyez sur Entrée. PyCharm vous demandera si vous souhaitez ajouter ce fichier à Git ou non. Cliquez sur Add, puis collez le contenu copié.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-10.png)

En ce moment, votre dépôt n'a aucun commit. Pour créer un nouveau commit, cliquez sur le lien "Commit local changes" ou passez à l'onglet "Commit".

Puisqu'il s'agit de votre premier commit, cochez tous les "Changes" et "Unversioned Files" dans l'onglet commit.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-11.png)

Puisqu'il s'agit de votre premier commit, mettez un message de commit descriptif tel que "Initial commit" et appuyez sur le bouton "Commit" pour finaliser.

Vous avez réussi à effectuer un commit dans votre dépôt local. Vous pouvez maintenant voir tous les commits sous la branche master en détail.

Il est maintenant temps de publier ce dépôt sur GitHub. Pour ce faire, créez un nouveau dépôt sous votre compte GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-14.png)

Copiez ensuite le lien SSH vers ce dépôt. Si vous n'avez pas configuré SSH pour votre projet, vous pouvez utiliser le lien HTTPS mais je recommande vivement SSH.

Retournez maintenant sur PyCharm et regardez dans le coin supérieur droit. À côté de l'endroit où il est écrit Git, vous trouverez quelques signes.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-15.png)

La flèche bleue vers le bas récupérera le code de votre dépôt distant, le signe de coche créera un nouveau commit, la flèche verte vers le haut poussera le code.

L'icône de l'horloge affichera votre historique de commit et enfin la flèche en boucle annulera vos modifications. Cliquez sur la flèche de push et une nouvelle fenêtre apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-16.png)

Cliquez sur le lien "Define remote" et dans la zone de saisie d'URL, collez le lien que vous avez copié de GitHub. Appuyez sur le bouton OK et attendez la fin du processus.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-17.png)

Si tout se passe bien, PyCharm vous donnera un bouton "Push". Cela ne devrait pas prendre plus de quelques secondes pour pousser le code vers votre dépôt distant.

Si vous utilisez HTTPS au lieu de SSH, vous devrez peut-être fournir votre e-mail et votre mot de passe GitHub à chaque push.

Une fois terminé, visitez votre dépôt distant et rafraîchissez la page pour voir si les modifications ont été poussées correctement ou non.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-18.png)

Vous pouvez maintenant committer et pousser votre code vers GitHub directement depuis votre IDE chaque fois que vous apportez une modification significative.

Par exemple, supprimez le fichier "library.py" et mettez à jour le code à l'intérieur du fichier "main.py" pour afficher "Hello, World!" sur la console.

```
def main():
    print("Hello, World!")


if __name__ == '__main__':
    main()

# Hello, World!
```

Une fois les modifications effectuées, passez à l'onglet commit et vous verrez toutes les modifications non committées.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-19.png)

Assurez-vous d'avoir coché toutes les modifications que vous souhaitez committer. Écrivez un message de commit descriptif.

Ensuite, au lieu de simplement committer, essayez le bouton "Commit and Push..." cette fois. Une nouvelle fenêtre apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-21.png)

Si tout vous semble correct, cliquez sur le bouton Push et attendez la fin du processus.

N'oubliez pas que si vous utilisez HTTPS, vous devrez peut-être ressaisir votre e-mail et votre mot de passe à chaque push.

Vous pouvez vérifier votre dépôt distant sur GitHub pour vous assurer que le push a été effectué correctement.

Vous pouvez faire beaucoup plus en termes de contrôle de version dans PyCharm, comme gérer les pull requests, mais je laisserai cela pour une autre fois.

## Comment travailler avec les variables et les différents types de données en Python

Une variable est une entité qui peut prendre différentes valeurs de différents types. C'est un emplacement nommé dans la mémoire de votre ordinateur.

Pour créer une nouvelle variable en Python, il vous suffit de taper le nom de la variable, suivi d'un signe égal et de la valeur.

```
def main():
    book = 'Dracula'
    author = 'Bram Stoker'
    release_year = 1897
    goodreads_rating = 4.01

    print(book)
    print(author)
    print(release_year)
    print(goodreads_rating)


if __name__ == '__main__':
    main()

# Dracula
# Bram Stoker
# 1897
# 4.01
```

En ce qui concerne le nommage de votre variable, le [PEP 8 - Guide de style pour Python][62] indique :

> Les noms de fonctions doivent être en minuscules, avec des mots séparés par des underscores si nécessaire pour améliorer la lisibilité.

Et

> Les noms de variables suivent la même convention que les noms de fonctions.

Le [guide indique également][63] :

> N'utilisez jamais les caractères ‘l’ (lettre minuscule el), ‘O’ (lettre majuscule oh) ou ‘I’ (lettre majuscule i) comme noms de variables à un seul caractère. Dans certaines polices, ces caractères sont indiscernables des chiffres un et zéro. Lorsque vous êtes tenté d'utiliser ‘l’, utilisez ‘L’ à la place.

Tant que vous gardez ces directives à l'esprit, déclarer des variables en Python est très simple.

Au lieu de déclarer les variables sur des lignes séparées, vous pouvez les déclarer d'un seul coup comme suit :

```
def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    print(book)
    print(author)
    print(release_year)
    print(goodreads_rating)


if __name__ == '__main__':
    main()

# Dracula
# Bram Stoker
# 1897
# 4.01
```

Tout ce que vous avez à faire est d'écrire les noms des variables individuelles sur une seule ligne en utilisant des virgules comme séparateurs.

Ensuite, après le signe égal, vous devez écrire les valeurs correspondantes dans le même ordre que leurs noms, en utilisant à nouveau des virgules comme séparateurs.

En fait, vous pouvez également les afficher toutes d'un seul coup. La méthode `print()` peut prendre plusieurs paramètres séparés par des virgules.

```
def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    print(book, author, release_year, goodreads_rating)


if __name__ == '__main__':
    main()

# Dracula Bram Stoker 1897 4.01
```

Ces paramètres sont ensuite affichés sur le terminal sur une seule ligne en utilisant des espaces pour séparer chacun d'eux.

En parlant de la méthode `print()`, vous pouvez utiliser le signe `+` pour ajouter des variables avec des chaînes de caractères à l'intérieur d'une méthode d'affichage :

```
def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    print(book + ' is a novel by ' + author + ', published in ' + release_year + '. It has a rating of ' + goodreads_rating + ' on goodreads.')


if __name__ == '__main__':
    main()


# TypeError: can only concatenate str (not "int") to str
```

Si vous essayez d'exécuter ce code, vous obtiendrez une `TypeError` indiquant que Python peut concaténer ou ajouter des chaînes de caractères, mais pas des entiers.

Dans l'extrait de code ci-dessus, `book`, `author`, `release_year` et `goodreads_rating` sont toutes des variables de types différents.

Les variables `book` et `author` sont des chaînes de caractères. `release_year` est un entier et enfin la variable `goodreads_rating` est un nombre à virgule flottante.

Chaque fois que Python rencontre un signe `+` devant un type numérique, il suppose que le programmeur effectue peut-être une opération arithmétique.

Le moyen le plus simple de résoudre ce problème est de convertir les types numériques en chaînes de caractères. Vous pouvez le faire en appelant la méthode `str()` sur les variables numériques.

```
def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    print(book + ' is a novel by ' + author + ', published in ' + str(release_year) + '. It has a rating of ' + str(goodreads_rating) + ' on goodreads.')


if __name__ == '__main__':
    main()

# Dracula is a novel by Bram Stoker, published in 1897. It has a rating of 4.01 on goodreads.
```

C'est mieux – mais vous pouvez rendre cette ligne de code encore plus lisible en utilisant une f-string.

```
def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    print(f'{book} is a novel by {author}, published in {release_year}. It has a rating of {goodreads_rating} on goodreads.')


if __name__ == '__main__':
    main()

# Dracula is a novel by Bram Stoker, published in 1897. It has a rating of 4.01 on goodreads.
```

Vous pouvez transformer une chaîne ordinaire en f-string en plaçant un `f` devant elle, et soudain vous pouvez écrire des noms de variables entre accolades directement à l'intérieur de la chaîne elle-même.

Il y a une dernière chose qui me gêne, c'est la longueur de la ligne de code elle-même. Heureusement, vous pouvez diviser les chaînes longues en plusieurs chaînes plus courtes comme suit :

```
def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    print(f'{book} is a novel by {author}, published in {release_year}.'
          f' It has a rating of {goodreads_rating} on goodreads.')


if __name__ == '__main__':
    main()

# Dracula is a novel by Bram Stoker, published in 1897. It has a rating of 4.01 on goodreads.
```

Voilà à quoi devrait ressembler un bon morceau de code Python. Je vous suggère d'essayer de rendre votre code lisible dès le début – vous me remercierez plus tard pour cela.

En dehors de `int` et `float`, il existe un autre type numérique appelé `complex` en Python. Il a été spécifiquement conçu pour traiter des nombres comme `500+2j`.

Il existe également des données booléennes qui peuvent contenir la valeur `True` ou `False` et rien d'autre. Vous pouvez en fait poser des questions à Python et il répondra en booléen.

Tout au long de ce livre, vous ne verrez pas de nombres complexes en action et les booléens entreront en jeu beaucoup plus tard. Pour l'instant, concentrons-nous sur les nombres simples et les chaînes de caractères.

## Comment travailler avec les nombres simples en Python

Les nombres simples en Python sont de deux types. Les nombres entiers sont des integers et les nombres avec des points décimaux sont des floats.

En Python, vous pouvez représenter les entiers en utilisant quatre bases différentes. Ce sont les bases décimale, hexadécimale, octale et binaire.

| Base | Représentation |
| --- | --- |
| Décimale | 404 |
| Hexadécimale | 0x194 |
| Octale | 0o624 |
| Binaire | 0b000110010100 |

Vous pouvez donc représenter la valeur de 404 en hexadécimal, octal ou binaire en préfixant la valeur correspondante par `0x`, `0o` ou `0b` respectivement.

D'autre part, vous pouvez représenter des floats avec une précision allant jusqu'à 15 chiffres significatifs en Python. Tout chiffre après la 15ème place peut être inexact.

Il existe six opérations arithmétiques différentes que vous pouvez effectuer sur n'importe lequel des types numériques simples. Les plus simples du lot sont l'addition et la soustraction.

```
def main():
    num_1 = 15
    num_2 = 12

    print(f'sum of num_1 and num_2 is: {num_1 + num_2}')
    print(f'difference of num_1 and num_2 is: {num_1 - num_2}')

if __name__ == '__main__':
    main()

# sum of num_1 and num_2 is: 27
# difference of num_1 and num_2 is: 3
```

Dans le cas d'une opération de soustraction, le résultat sera négatif si le deuxième opérande est plus grand que le premier.

```
def main():
    num_1 = 15
    num_2 = 12

    print(f'difference of num_2 and num_1 is: {num_2 - num_1}')

if __name__ == '__main__':
    main()

# difference of num_2 and num_1 is: -3
```

De même, vous pouvez effectuer des opérations de multiplication et de division en utilisant leurs opérateurs correspondants.

```
def main():
    num_1 = 15
    num_2 = 12

    print(f'product of num_1 and num_2 is: {num_1 * num_2}')
    print(f'quotient of num_1 and num_2 is: {num_1 / num_2}')
    print(f'floored quotient of num_1 and num_2 is: {num_1 // num_2}')


if __name__ == '__main__':
    main()

# product of num_1 and num_2 is: 180
# quotient of num_1 and num_2 is: 1.25
# floored quotient of num_1 and num_2 is: 1
```

Gardez à l'esprit que vous ne pouvez pas diviser un nombre par zéro en Python. Si vous tentez cela, vous obtiendrez une erreur `ZeroDivisionError` (nous y reviendrons plus tard).

Le résultat d'une opération de division sera toujours une valeur float, à moins que vous n'effectuiez une division entière (division euclidienne) en utilisant deux opérateurs de division.

```
def main():
    num_1 = 15
    num_2 = 12

    print(f'floored quotient of num_1 and num_2 is: {num_1 // num_2}')


if __name__ == '__main__':
    main()

# floored quotient of num_1 and num_2 is: 1
```

Dans ce cas, le résultat sera arrondi à l'entier inférieur le plus proche – ainsi, par exemple, 0,25 sera perdu. N'effectuez donc cette opération que lorsque cette perte de données est admissible.

La dernière opération à discuter est de trouver le reste d'une opération de division.

```
def main():
    num_1 = 15
    num_2 = 12

    print(f'remainder of num_1 / num_2 is: {num_1 % num_2}')


if __name__ == '__main__':
    main()

# remainder of num_1 / num_2 is: 3
```

Cette opération est également appelée opération modulo. Donc, si quelqu'un mentionne l'opérateur modulo, il se réfère au signe pourcentage.

Vous pouvez transformer un nombre non signé en un nombre négatif simplement en ajoutant un signe `-` devant lui. Vous pouvez également convertir librement un entier en float et vice versa.

```
def main():
    float_variable = 1.25
    integer_variable = 55

    print(f'{float_variable} converted to an integer is: {int(float_variable)}')
    print(f'{integer_variable} converted to a float is: {float(integer_variable)}')


if __name__ == '__main__':
    main()

# 1.25 converted to an integer is: 1
# 55 converted to a float is: 55.0
```

La perte de données dans le cas d'une conversion de float en entier est inévitable, soyez donc prudent. Vous pouvez également utiliser les méthodes `int()` et `float()` sur des chaînes de caractères (nous y reviendrons plus tard).

Toute opération arithmétique impliquant un opérande float produira toujours un résultat float, à moins d'être convertie explicitement en entier.

```
def main():
    float_variable = 5.0
    integer_variable = 55

    print(f'the sum of {float_variable} and {integer_variable} is: {float_variable + integer_variable}')
    print(f'the sum of {float_variable} and {integer_variable} '
          f'converted to integer is: {int(float_variable + integer_variable)}')


if __name__ == '__main__':
    main()

# the sum of 5.0 and 55 is: 60.0
# the sum of 5.0 and 55 converted to integer is: 60
```

Si vous souhaitez obtenir la valeur absolue d'une valeur signée, vous pouvez le faire en utilisant la méthode `abs()`.

```
def main():
    num_1 = -5.8

    print(f'the absolute value of {num_1} is: {abs(num_1)}')


if __name__ == '__main__':
    main()

# the absolute value of -5.8 is: 5.8
```

Il existe une méthode similaire `pow(x, y)` que vous pouvez utiliser pour appliquer `x` à la puissance `y` comme ceci.

```
def main():
    x = 2
    y = 3

    print(f'{2} to the power of {3} is: {pow(2, 3)}')
    print(f'{2} to the power of {3} is: {2 ** 3}')


if __name__ == '__main__':
    main()

# 2 to the power of 3 is: 8
# 2 to the power of 3 is: 8
```

Vous pouvez effectuer la même opération en utilisant deux opérateurs de multiplication, mais je préfère toujours la méthode `pow()`.

Enfin, il y a la méthode `divmod()` que vous pouvez utiliser pour combiner l'opération de division et de modulo.

```
def main():
    num_1 = 8
    num_2 = 2

    print(f'division and modulus of {num_1} and {num_2} is: {divmod(num_1, num_2)}')


if __name__ == '__main__':
    main()

# division and modulus of 8 and 2 is: (4, 0)
```

La méthode renvoie un tuple de nombres (nous y reviendrons plus tard). Le premier est le résultat de la division et le second est le résultat de l'opération modulo.

Ce sont les opérations de base que vous pouvez effectuer sur des nombres simples dès le départ. Mais vous pouvez faire beaucoup plus une fois que vous commencez à utiliser les modules intégrés.

## Comment récupérer les entrées utilisateur en Python

Apprendre à prendre des entrées d'un utilisateur est une étape importante car cela vous permet de créer des programmes avec lesquels un être humain peut interagir.

Contrairement à de nombreux autres langages de programmation, la récupération des entrées utilisateur en Python est très simple.

```
def main():
    name = input('What is your name? ')

    print(f'Nice to meet you {name}')


if __name__ == '__main__':
    main()

# What is your name? Farhan
# Nice to meet you Farhan
```

La méthode intégrée `input()` fait exactement ce qu'elle suggère. La méthode accepte un paramètre unique `prompt` qui est de type chaîne de caractères.

Tout ce que vous écrivez comme valeur de ce paramètre sera affiché dans la console – comme dans ce cas, "What is your name?" est l'invite.

Une fois que l'utilisateur écrit quelque chose sur la console et appuie sur Entrée, la méthode input renverra cela sous forme de chaîne de caractères.

Vous pouvez enregistrer cette chaîne dans n'importe quelle variable, comme j'ai enregistré le nom dans la variable `name`. Même si l'utilisateur saisit un nombre, `input()` le renverra sous forme de chaîne.

```
def main():
    name = input('What is your name? ')
    age = input(f'How old are you {name}? ')
    current_year = input(f'What year is this again? ')

    print(f'If my calculations are right, you were born in {current_year - age}')


if __name__ == '__main__':
    main()

# What is your name? Farhan
# How old are you Farhan? 27
# What year is this again? 2023
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

Même si Python prend correctement toutes les entrées utilisateur, il échoue à calculer l'année de naissance de l'utilisateur car les opérations arithmétiques ne sont pas adaptées aux chaînes de caractères.

Pour résoudre ce problème, il vous suffit de convertir les entrées utilisateur en types numériques à l'aide des fonctions `int()` ou `float()` selon les besoins.

```
def main():
    name = input('What is your name? ')
    age = int(input(f'How old are you {name}? '))
    current_year = int(input(f'What year is this again? '))

    print(f'If my calculations are right, you were born in {current_year - age}')


if __name__ == '__main__':
    main()

# What is your name? Farhan
# How old are you Farhan? 27
# What year is this again? 2023
# If my calculations are right, you were born in 1996
```

Et voilà, cela fonctionne à merveille. Vous pouvez effectuer cette conversion à n'importe quel point du code. Il n'est pas obligatoire de les convertir dès le début.

```
def main():
    temperature_in_celsius = input('What is the temperature in celsius? ')

    temperature_in_fahrenheit = (float(temperature_in_celsius) * 1.8) + 32

    print(f'{temperature_in_celsius} degree celsius is equivalent to {temperature_in_fahrenheit} degree fahrenheit.')


if __name__ == '__main__':
    main()

# What is the temperature in celsius? 32
# 32 degree celsius is equivalent to 89.6 degree fahrenheit.
```

Ce programme peut convertir la température de Celsius en Fahrenheit. Dans ce programme, je n'ai pas converti l'entrée de chaîne en type numérique immédiatement.

J'ai effectué la conversion pendant le calcul en laissant la variable d'entrée originale intacte. Notez également l'utilisation de `float()` au lieu de la fonction `int()`.

## Comment travailler avec les chaînes de caractères en Python

Vous avez déjà vu des exemples de chaînes de caractères dans les sections précédentes – mais il y a beaucoup plus à apprendre sur les chaînes.

En Python, tout ce qui est entouré d'un ensemble de guillemets simples, doubles ou triples est une chaîne de caractères. Ce sont des séquences d'octets représentant des caractères Unicode.

```
def main():
    book = 'Dracula'
    author = "Bram Stoker"

    print('Title:', book)
    print('Author:', author)


if __name__ == '__main__':
    main()

# Title: Dracula
# Author: Bram Stoker
```

Déclarer une chaîne avec des guillemets simples ou doubles ne fait aucune différence. Mais selon le scénario, vous devrez peut-être choisir l'un plutôt que l'autre.

Par exemple, si vous avez une apostrophe dans votre phrase, vous voudrez peut-être utiliser des guillemets doubles.

```
def main():
    question = "What's your name?"

    print(question)


if __name__ == '__main__':
    main()

# What's your name?
```

L'inverse peut également se produire. Par exemple, lorsque vous avez une citation directe dans votre chaîne :

```
def main():
    sentence = 'Harriet Jacobs writes, "She sat down, quivering in every limb"'

    print(sentence)


if __name__ == '__main__':
    main()

# Harriet Jacobs writes, "She sat down, quivering in every limb"
```

Vous pouvez également opter pour des [séquences d'échappement][64] si vous le souhaitez, mais le [PEP 8 - Guide de style pour le code Python][65] recommande d'éviter l'utilisation de barres obliques inverses (backslashes) dans les chaînes.

Les guillemets triples sont un cas tout à fait à part. Vous pouvez mettre des chaînes multi-lignes entre guillemets triples et Python préservera également les espaces blancs.

```
def main():
    synopsis = """Dracula comprises journal entries, letters, and telegrams written by the main characters.
It begins with Jonathan Harker, a young English lawyer, as he travels to Transylvania.
Harker plans to meet with Count Dracula, a client of his firm, in order to finalize a property transaction.
When he arrives in Transylvania, the locals react with terror after he discloses his destination: Castle Dracula.
Though this unsettles him slightly, he continues onward.
The ominous howling of wolves rings through the air as he arrives at the castle.
When Harker meets Dracula, he acknowledges that the man is pale, gaunt, and strange.
Harker becomes further concerned when, after Harker cuts himself while shaving, Dracula lunges at his throat.
Soon after, Harker is seduced by three female vampires, from whom he barely escapes.
He then learns Dracula’s secret—that he is a vampire and survives by drinking human blood.
Harker correctly assumes that he is to be the count’s next victim.
He attacks the count, but his efforts are unsuccessful.
Dracula leaves Harker trapped in the castle and then, along with 50 boxes of dirt, departs for England."""

    print('Synopsis:', synopsis)


if __name__ == '__main__':
    main()

# Synopsis: Dracula comprises journal entries, letters, and telegrams written by the main characters.
# It begins with Jonathan Harker, a young English lawyer, as he travels to Transylvania.
# Harker plans to meet with Count Dracula, a client of his firm, in order to finalize a property transaction.
# When he arrives in Transylvania, the locals react with terror after he discloses his destination: Castle Dracula.
# Though this unsettles him slightly, he continues onward.
# The ominous howling of wolves rings through the air as he arrives at the castle.
# When Harker meets Dracula, he acknowledges that the man is pale, gaunt, and strange.
# Harker becomes further concerned when, after Harker cuts himself while shaving, Dracula lunges at his throat.
# Soon after, Harker is seduced by three female vampires, from whom he barely escapes.
# He then learns Dracula’s secret—that he is a vampire and survives by drinking human blood.
# Harker correctly assumes that he is to be the count’s next victim.
# He attacks the count, but his efforts are unsuccessful.
# Dracula leaves Harker trapped in the castle and then, along with 50 boxes of dirt, departs for England.
```

Donc, si vous voulez un jour afficher une chaîne multi-ligne tout en préservant les espaces blancs, optez pour les guillemets triples.

Vous pouvez déclarer une chaîne entre guillemets triples en utilisant trois guillemets simples, mais le [PEP 8 - Guide de style pour le code Python][66] recommande l'utilisation de trois guillemets doubles.

Il y a beaucoup plus à apprendre sur les chaînes, mais j'aimerais vous présenter d'autres types de séquences en Python.

## Quels sont les types de séquences en Python ?

En Python, il existe trois types de séquences. Ce sont les listes, les tuples et les ranges. Je vais commencer par les listes car c'est probablement le type de séquence le plus utilisé en Python.

### Les listes en Python

Une liste en Python est exactement ce que son nom suggère : une collection de données stockées de manière séquentielle dans la mémoire de l'ordinateur.

Vous pouvez créer une nouvelle liste en Python en écrivant son nom suivi d'un signe égal, puis des valeurs à stocker entourées de crochets :

```
def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books)


if __name__ == '__main__':
    main()

# ['Dracula', 'Carmilla', 'The Imago Sequence']
```

Dans cet exemple, `horror_books` est une liste de chaînes de caractères. Mais vous pouvez créer des listes d'entiers, de floats ou même de types mixtes.

```
def main():
    a_random_list = ['Dracula', 1, 5.7, 'Carmilla']

    print(a_random_list)


if __name__ == '__main__':
    main()

# ['Dracula', 1, 5.7, 'Carmilla']
```

Bien que cela soit parfaitement valide, vous vous retrouverez plus souvent à créer des listes de mêmes types.

Les listes en Python sont mutables. Cela signifie que vous pouvez modifier une liste après sa création. Par exemple, vous pouvez utiliser la méthode `pop()` pour supprimer la dernière valeur d'une liste.

```
def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books.pop())
    print(horror_books)


if __name__ == '__main__':
    main()

# The Imago Sequence
# ['Dracula', 'Carmilla']
```

Comme vous pouvez le voir, la méthode `pop()` renvoie la dernière valeur de la liste et la supprime. Comme `pop()`, il existe la méthode `append()` pour insérer un nouvel élément dans la liste.

```
def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books)

    horror_books.append('The Exorcist')

    print(horror_books)


if __name__ == '__main__':
    main()

# ['Dracula', 'Carmilla', 'The Imago Sequence']
# ['Dracula', 'Carmilla', 'The Imago Sequence', 'The Exorcist']
```

Comme vous pouvez le voir d'après le nom de la méthode, elle ajoute le nouvel élément à la fin de la liste. Compte tenu de leur nature mutable, les listes peuvent également être triées.

N'hésitez pas à consulter l'article suivant écrit par ma collègue [Dionysia Lemonaki][67] ici sur freeCodeCamp sur la façon de trier les listes en Python :

[https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/][68]

### Les tuples en Python

Les listes ne sont pas le seul type de séquence en Python. Les parents les plus proches des listes en Python sont les tuples.

Vous pouvez créer un nouveau tuple en Python en écrivant son nom suivi d'un signe égal, puis en entourant d'une paire de parenthèses les valeurs que vous souhaitez stocker.

```
def main():
    horror_books = ('Dracula', 'Carmilla', 'The Imago Sequence')

    print(horror_books)


if __name__ == '__main__':
    main()

# ('Dracula', 'Carmilla', 'The Imago Sequence')
```

Tout comme les listes, vous pouvez également mélanger différents types de données au sein d'un même tuple comme bon vous semble.

```
def main():
    a_random_list = ('Dracula', 1, 5.7, 'Carmilla')

    print(a_random_list)


if __name__ == '__main__':
    main()

# ('Dracula', 1, 5.7, 'Carmilla')
```

La différence la plus flagrante entre une liste et un tuple est le fait qu'un tuple est immuable. Il n'y a donc pas de pop ni d'append pour nous cette fois.

### Les ranges en Python

Le dernier type de séquence que vous allez découvrir dans cette section est le range. Un range en Python est simplement une plage de nombres.

Vous pouvez créer un range en appelant la méthode `range()` et elle renverra une plage de nombres. Vous pouvez appeler la méthode de plusieurs façons différentes.

La plus courante consiste à passer un seul nombre en paramètre. Dans ce cas, la méthode traitera ce nombre comme la fin de la plage et 0 comme le début.

```
def main():
    a_range = range(10)

    print(a_range)

    list_a_range = list(a_range)

    print(list_a_range)


if __name__ == '__main__':
    main()

# range(0, 10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

Afficher un range tel quel ne vous donnera pas beaucoup d'informations. Vous devrez convertir le range en liste ou en tuple en appelant soit la méthode `list()`, soit la méthode `tuple()`.

Une fois converti, vous pouvez alors afficher toute la plage sur la console. Notez que 10 ou le nombre passé à la méthode `range()` n'est pas inclus dans la plage.

La deuxième façon d'appeler la méthode consiste à fournir à la fois les nombres de début et de fin de la plage.

```
def main():
    a_range = range(5, 15)

    print(a_range)

    list_a_range = list(a_range)

    print(list_a_range)

    tuple_a_range = tuple(a_range)

    print(tuple_a_range)


if __name__ == '__main__':
    main()

# range(5, 15)
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# (5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
```

Encore une fois, le nombre que vous passez comme fin de la plage ne sera pas inclus dans la plage résultante.

La troisième et dernière façon d'appeler la méthode est de définir également un pas (step). Par exemple, imaginez que vous vouliez une plage composée de tous les nombres impairs entre 1 et 10.

```
def main():
    a_range = range(1, 10, 2)

    print(a_range)

    list_a_range = list(a_range)

    print(list_a_range)

    tuple_a_range = tuple(a_range)

    print(tuple_a_range)


if __name__ == '__main__':
    main()

# range(1, 10, 2)
# [1, 3, 5, 7, 9]
# (1, 3, 5, 7, 9)
```

Puisque la valeur du pas est 2 dans ce cas, la plage commencera à 1 mais sautera ensuite un nombre sur deux.

Il faudra peut-être un certain temps pour assimiler ce concept, mais s'entraîner avec différentes valeurs de pas vous aidera.

Ou vous pouvez lire l'article suivant écrit par [Bala Priya C][69] :

[https://www.freecodecamp.org/news/python-range-function-explained-with-code-examples/][70]

### Comment fonctionne l'indexation en Python

L'un des concepts les plus importants concernant les types de séquences que vous devez comprendre est l'indexation.

Voyez-vous, chaque élément d'une séquence possède un numéro qui lui est attaché et qui exprime sa position dans la liste, appelé index. Ces indices commencent à 0.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/horror-books-list.svg)

Ce diagramme représente notre liste de livres d'horreur. L'index du premier livre est 0 – cela signifie que le premier élément est à la 0ème place.

Le deuxième est à la 1ère place et le troisième est à la 2ème place. Cette indexation basée sur zéro peut sembler déroutante au début, mais vous finirez par vous y habituer.

L'utilisation la plus basique d'un index est d'accéder à sa valeur correspondante à partir de la séquence.

```
def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books[0])
    print(horror_books[1])
    print(horror_books[2])


if __name__ == '__main__':
    main()

# Dracula
# Carmilla
# The Imago Sequence
```

Vous pouvez également utiliser des nombres négatifs comme indices, mais dans ce cas, le comptage commencera par la fin.

```
def main():
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow',
             'And Then There Were None', 'The ABC Murders', 'The Valley of Fear']

    print(books[0])

    print(books[1])
    print(books[-1])

    print(books[2])
    print(books[-2])


if __name__ == '__main__':
    main()

# Dracula

# Frankenstein
# The Valley of Fear

# The Omen
# The ABC Murders
```

L'élément 0 d'une liste sera toujours le premier. Maintenant, si vous accédez à l'élément en position 1, vous obtenez "Frankenstein".

Mais si vous essayez d'accéder à l'élément en position -1, vous obtenez "The Valley of Fear" car c'est le premier élément en partant de la fin.

L'élément en position 2 est "The Omen" mais l'élément en position -2 est "The ABC Murders" car c'est le deuxième élément en partant de la fin.

Si vous avez du mal à vous y retrouver, imaginez la liste comme une horloge.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/list-clock.svg) _L'indexation basée sur zéro représentée sous forme de diagramme circulaire comme une horloge_

Ici, le nombre extérieur est l'index négatif et le nombre intérieur est l'index positif. Si vous essayez de faire correspondre les sorties avec cette horloge imaginaire, cela devrait être plus facile à comprendre.

## Quels sont les types itérables et comment les utiliser pour les boucles en Python

Jusqu'à présent, vous avez appris à créer des collections de données et à y accéder une par une. C'est bien, mais il y a mieux.

Imaginez que vous ayez une liste ou un autre type qui contient un tas de nombres.

Maintenant, vous voulez multiplier chaque nombre de cette liste par deux, insérer les nombres multipliés dans une nouvelle liste et afficher la liste sur le terminal.

C'est un excellent cas d'utilisation pour l'instruction `for` en Python. Commençons par itérer sur chaque nombre d'une liste donnée.

```
def main():
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]

    for number in random_numbers:
        print(number)

if __name__ == '__main__':
    main()

# 6
# 1
# 3
# 8
# 0
# 9
# 12
# 3
# 4
# 0
# 54
# 8
# 100
# 55
# 60
# 70
# 85
```

Vous commencez par écrire le mot `for` suivi d'un nom de variable. J'ai utilisé `number` mais vous pouvez utiliser tout ce qui a du sens pour vous.

Bien que vous l'écriviez `for number`, Python le lit comme `for each number` (pour chaque nombre) et se demande où se trouvent ces nombres.

C'est là que vous dites `in` suivi du nom de la séquence, `random_numbers` dans ce cas.

Maintenant Python comprend que vous voulez faire quelque chose avec chaque nombre de la séquence `random_numbers`, mais quoi ?

C'est ce que vous devez écrire après les deux points et faire très attention à l'indentation. Tout ce qui est indenté d'un niveau après la déclaration de la boucle for est considéré comme le corps de la boucle.

À l'intérieur de la boucle for, vous pouvez écrire tout ce que vous voulez faire avec la valeur actuelle de la variable `number`.

Comme il y a 17 nombres dans la séquence, la boucle s'exécutera 17 fois et aura à chaque fois une nouvelle valeur.

Elle commencera à l'index 0 qui a la valeur de 6 et passera par les index 1, 2, 3, 4, 5, et ainsi de suite.

À chaque itération, elle enregistrera la valeur de l'index sur lequel elle travaille actuellement dans la variable `number` et l'affichera. C'est ainsi que vous obtenez la longue liste de nombres.

Au lieu d'afficher la valeur originale, vous pouvez la multiplier par 2 et afficher la valeur résultante à la place.

```
def main():
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]

    for number in random_numbers:
        print(number * 2)

if __name__ == '__main__':
    main()

# 12
# 2
# 6
# 16
# 0
# 18
# 24
# 6
# 8
# 0
# 108
# 16
# 200
# 110
# 120
# 140
# 170
```

Maintenant vous obtenez les valeurs multipliées. La tâche finale consiste à insérer ces valeurs multipliées dans une nouvelle liste et à afficher la nouvelle liste elle-même.

```
def main():
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]
    multiplied_random_numbers = []

    for number in random_numbers:
        multiplied_random_numbers.append(number * 2)

    print(multiplied_random_numbers)

if __name__ == '__main__':
    main()

# [12, 2, 6, 16, 0, 18, 24, 6, 8, 0, 108, 16, 200, 110, 120, 140, 170]
```

Pour cela, vous aurez besoin d'une liste vide. Ensuite, après avoir multiplié le nombre, vous pouvez simplement appeler la méthode `append()` sur la nouvelle liste et passer la valeur multipliée.

Enfin, assurez-vous de placer l'instruction print en dehors du corps de la boucle, sinon vous finirez par afficher la liste 17 fois.

La boucle `for` fonctionne avec tous les types de séquences et tout type itérable dans le langage Python. Qu'est-ce qu'un type itérable, me demanderez-vous ?

Eh bien, tout objet qui possède la méthode `__iter__()` est considéré comme un itérable en Python.

Vous pouvez appeler la fonction `dir()` sur n'importe quel objet pour lister toutes ses méthodes et propriétés. Prenez la liste `random_numbers` comme exemple.

```
def main():
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]

    print(dir(random_numbers))

if __name__ == '__main__':
    main()

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Vous pouvez voir des méthodes familières telles que `append`, `count` et `index` mais surtout elle possède la méthode `__iter__`.

Au fur et à mesure que vous travaillerez en Python, vous finirez par vous souvenir des types pris en charge par la boucle `for`, mais vous pouvez toujours utiliser la méthode `dir()` sur un objet pour le découvrir.

## Comment utiliser les boucles While en Python

Il existe un autre type de boucle en Python connu sous le nom de boucle `while`. Contrairement à `for`, une boucle `while` peut exécuter une instruction tant qu'une condition donnée est évaluée à `true`.

```
def main():
    number = 1
    while number < 11:
        print(number)
        number += 1

if __name__ == '__main__':
    main()

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
```

Ici vous avez une variable `number` avec la valeur `1` et une boucle `while` qui affiche la valeur de number, puis l'augmente de 1.

Une boucle `while` commence par l'écriture de `while` suivi de la condition. Ensuite, vous écrivez le corps de la boucle en commençant par la ligne suivante après les deux points.

Les boucles `for` sont utiles lorsque vous essayez d'accéder à chaque élément à l'intérieur d'un itérable. Les boucles `while` sont utiles lorsque vous voulez répéter le même ensemble d'instructions un nombre arbitraire de fois.

La ligne `number += 1` est une autre façon d'écrire `number = number + 1` et elle est très couramment utilisée par les programmeurs dans différents langages de programmation.

## Comment écrire des boucles imbriquées en Python

Vous pouvez également imbriquer une boucle à l'intérieur d'une autre. Par exemple, regardez le code suivant qui affiche des tables de multiplication :

```
def main():
    for x in range(1, 6):
        print()
        for y in range(1, 11):
            print(f"{x} x {y} = {x * y}")


if __name__ == '__main__':
    main()

#
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
#
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
#
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
#
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
#
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
```

Pour être honnête, c'est un morceau de code très simple qui utilise beaucoup de choses que vous avez déjà apprises dans ce manuel.

Pour créer une table de multiplication, nous avons besoin de deux opérandes : l'un reste constant pour toute la table et l'autre augmente de 1 jusqu'à atteindre 10.

Ici, `x` représente l'opérande de gauche ou celui qui est constant et `y` représente l'opérande de droite ou celui qui est variable.

La première boucle itère sur une plage de 1 à 5 et la seconde boucle itère sur une plage de 1 à 10.

Comme le nombre de fin d'une plage est exclusif, vous devez mettre un nombre qui est supérieur de 1 au nombre de fin souhaité.

Tout d'abord, l'interprète Python rencontre la boucle extérieure et commence à l'exécuter. À l'intérieur de cette boucle, la valeur de `x` est 1.

L'interprète rencontre alors la boucle intérieure et commence à l'exécuter. À l'intérieur de la boucle intérieure, la valeur de `x` reste 1 mais la valeur de `y` augmente à chaque itération.

La boucle intérieure est le corps de la boucle extérieure dans ce cas, donc la première itération de la boucle extérieure dure jusqu'à ce que la boucle intérieure se termine.

Après avoir terminé 10 itérations de la boucle intérieure, l'interprète revient à la boucle extérieure et recommence à l'exécuter.

Cette fois, la valeur de `x` devient 2 puisque c'est ce qui suit dans la plage.

C'est ainsi que la boucle extérieure s'exécute 5 fois et la boucle intérieure s'exécute 10 fois pour chacune de ces itérations.

Comme beaucoup d'autres concepts, assimiler les boucles imbriquées peut être difficile, mais la pratique facilitera les choses.

Je vous suggère d'aller de l'avant et d'implémenter ce programme en utilisant des boucles `while` pour tester votre compréhension.

Vous pouvez également prendre les deux nombres de l'utilisateur et afficher la table de multiplication dans cette plage.

Par exemple, si l'utilisateur saisit 5 et 10 comme entrées, vous afficherez alors les tables de multiplication de tous les nombres de 5 à 10.

Vous pouvez imbriquer des boucles à des niveaux encore plus profonds, mais aller au-delà de deux boucles peut causer des problèmes de performance, alors soyez prudent avec cela.

## Quelles sont les opérations courantes sur les types de séquences en Python ?

En supposant que vous vous souveniez du type de séquence de texte (strings), vous connaissez maintenant les quatre types de séquences Python les plus populaires.

Je pense donc qu'il est temps pour vous d'apprendre quelques opérations courantes que vous pouvez effectuer sur elles. Commençons, voulez-vous ?

### Comment utiliser l'opérateur `in` en Python

L'opérateur `in` est le moyen le plus courant de vérifier l'existence d'un objet. Par exemple, supposons que vous ayez une chaîne de caractères et que vous vouliez vérifier si elle contient le mot "red" ou non.

```
def main():
    a_string = 'Little Red Riding-Hood comes to me one Christmas Eve to give me information of the cruelty and ' \
               'treachery of that dissembling Wolf who ate her grandmother. '

    print('Red' in a_string)


if __name__ == '__main__':
    main()

# True
```

C'est littéralement comme demander à Python si le mot `Red` est `in` (dans) la variable `a_string`. Et Python vous donnera soit `True` soit `False` comme réponse.

L'opérateur `in` n'est pas exclusif aux chaînes de caractères. Vous pouvez en fait l'utiliser sur tout autre type de collection tel que les listes, les tuples et les ranges.

```
def main():
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
    movies = ('A Christmas Carol', 'The Sea Beast', 'Enchanted', 'Pinocchio', 'The Addams Family')
    numbers = range(10)

    print('A Christmas Carol' in books)
    print('Enchanted' in movies)
    print(5 in numbers)


if __name__ == '__main__':
    main()

# False
# True
# True
```

A Christmas Carol n'existe pas dans la liste `books`, c'est donc une instruction `False`. Les deux autres instructions sont correctes, elles sont donc `True`.

Vous voudrez peut-être aussi en savoir plus sur l'absence d'un objet. Pour cela, vous pouvez utiliser l'opérateur `not` conjointement avec l'opérateur `in`.

```
def main():
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
    movies = ('A Christmas Carol', 'The Sea Beast', 'Enchanted', 'Pinocchio', 'The Addams Family')
    numbers = range(10)

    print('A Christmas Carol' not in books)
    print('Enchanted' not in movies)
    print(15 not in numbers)


if __name__ == '__main__':
    main()

# True
# False
# True
```

A Christmas Carol n'existe pas dans la liste `books`, donc la première instruction est évaluée à `true`. La seconde est évaluée à false car Enchanted est présent dans la liste `movies`.

La dernière est explicite à ce stade. Les opérateurs `in` et `not in` s'avèrent très utiles lorsque vous travaillez avec des instructions conditionnelles.

### Comment utiliser les opérateurs `+` et `*` avec les types de séquences en Python

Vous avez déjà découvert `+` et `*` en tant qu'opérateurs arithmétiques – mais dans le cas des types de séquences, ils jouent un rôle très différent.

L'opérateur `+` vous permet de fusionner deux séquences ensemble.

```
def main():
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
    more_books = ['And Then There Were None', 'The ABC Murders', 'The Valley of Fear', 'The Hound of the Baskervilles', 'The Chestnut Man']


    print(books + more_books)


if __name__ == '__main__':
    main()

# ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow', 'And Then There Were None', 'The ABC Murders', 'The Valley of Fear', 'The Hound of the Baskervilles', 'The Chestnut Man']
```

Comme vous pouvez le voir, l'opérateur a ajouté le contenu de la liste `books` au contenu de la liste `more_books`.

L'opérateur `*`, quant à lui, crée plusieurs copies d'une séquence donnée.

```
def main():
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']


    print(books * 2)


if __name__ == '__main__':
    main()

# ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow', 'Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
```

Ainsi, multiplier la liste `books` par 2 nous donne deux fois les 5 livres de la liste. Ces opérateurs fonctionnent de la même manière pour les tuples, les chaînes de caractères, les ranges ou tout autre type de séquence.

### Comment utiliser les fonctions `len()`, `min()` et `max()` en Python

La fonction `len()` peut renvoyer la longueur d'une séquence donnée. Et les fonctions `min()` et `max()` peuvent renvoyer respectivement la valeur minimale et maximale d'une séquence donnée.

```
def main():
    random_numbers = [6, 1, 3, 8, 0]


    print(len(random_numbers))
    print(min(random_numbers))
    print(max(random_numbers))


if __name__ == '__main__':
    main()

# 5
# 0
# 8
```

Comme il y a 5 éléments dans la liste, 5 est le résultat de l'appel à la fonction `len()`.

La plus petite valeur de la liste est 0 et la plus grande valeur est 8, ce qui correspond respectivement aux résultats des appels aux fonctions `min()` et `max()`.

Selon le type de programmes que vous finirez par écrire à l'avenir, ces trois fonctions peuvent s'avérer être parmi les plus utiles.

## Quelles sont les opérations sur le type chaîne de caractères en Python ?

Dans la section précédente, vous avez découvert quelques opérations courantes que vous pouvez effectuer sur n'importe quel type de séquence, y compris les chaînes de caractères.

Cependant, le type de séquence de texte, alias strings, dispose de certaines opérations spéciales.

Dans ce chapitre, je vais vous présenter quelques-unes des méthodes de chaînes de caractères les plus courantes. Gardez à l'esprit qu'il ne s'agit pas d'une liste exhaustive.

Bien que chacune des méthodes que je vais vous enseigner accomplisse une tâche différente, elles ont un point commun. Aucune d'entre elles ne modifie une variable de chaîne donnée sur place, mais renvoie plutôt une nouvelle copie modifiée.

Si vous souhaitez en savoir plus sur toutes les méthodes de chaînes disponibles, n'hésitez pas à consulter la documentation officielle de Python.

[https://docs.python.org/3/library/stdtypes.html#string-methods][71]

N'oubliez pas non plus qu'il ne s'agit pas simplement de passer en revue chaque méthode et de mémoriser leur utilisation.

Il s'agit de savoir ce qui fonctionne le mieux dans un scénario donné et de trouver des solutions astucieuses. Et cela demande de la pratique.

### Comment mettre en majuscule des chaînes de caractères en Python

La première méthode que vous allez apprendre s'appelle `capitalize()` et elle fait ce que son nom suggère.

```
def main():
    country_name = 'bangladesh'

    print(country_name.capitalize())


if __name__ == '__main__':
    main()

# Bangladesh
```

Comme vous pouvez le voir dans l'extrait de code ci-dessus, la méthode `capitalize()` transforme la première lettre du mot en majuscule.

C'est simple, mais essayons cela sur une chaîne contenant plusieurs mots – une phrase peut-être.

```
def main():
    book_name = 'the house of silk'

    print(book_name.capitalize())


if __name__ == '__main__':
    main()

# The house of silk
```

Bien que la méthode ait fait son travail, il y a un léger problème. Selon ce que vous essayez d'accomplir, vous pourriez vous attendre à ce que la première lettre de chaque mot soit mise en majuscule.

C'est là qu'intervient la méthode `title()`. Cette méthode renvoie une version de type titre d'une chaîne donnée.

```
def main():
    book_name = 'the house of silk'

    print(book_name.title())


if __name__ == '__main__':
    main()

# The House Of Silk
```

Mais il y a toujours un problème. Prenez la chaîne suivante avec des apostrophes par exemple.

```
def main():
    book_name = "alice's adventures in wonderland"

    print(book_name.title())


if __name__ == '__main__':
    main()

# Alice'S Adventures In Wonderland
```

Comme vous pouvez le voir, la méthode `title()` traite le `s` suivant l'apostrophe comme un mot séparé et le met en majuscule.

Concernant ce problème, la [documentation officielle][72] stipule :

> L'algorithme utilise une définition simple du mot, indépendante de la langue, comme des groupes de lettres consécutives. La définition fonctionne dans de nombreux contextes, mais elle signifie que les apostrophes dans les contractions et les possessifs forment des limites de mots.

La fonction d'aide `capwords()` peut résoudre ce problème. Cette fonction divise la chaîne en plusieurs mots en fonction des espaces entre eux, met les mots en majuscules, les regroupe dans une chaîne et renvoie cela à l'utilisateur.

```
from string import capwords


def main():
    book_name = "alice's adventures in wonderland"

    print(capwords(book_name))


if __name__ == '__main__':
    main()

# Alice's Adventures In Wonderland
```

Faites attention à l'instruction `import` en haut. La fonction `capwords()` n'est pas une méthode à l'intérieur du type string mais une fonction qui réside à l'intérieur du module `string`.

Vous en apprendrez plus sur les modules et les importations plus tard. Pour l'instant, faites avec. Bien que la fonction utilise des espaces pour diviser les mots, vous pouvez l'écraser.

```
from string import capwords


def main():
    address = 'house 42, road 02, wonderland'

    print(capwords(address, ', '))


if __name__ == '__main__':
    main()

# House 42, Road 02, Wonderland
```

Comme vous pouvez le voir, dans ce cas, la chaîne comporte plusieurs parties divisées par une virgule suivie d'un espace.

La fonction `capwords()` peut prendre un délimiteur personnalisé comme second paramètre. Vous pouvez passer n'importe quelle chaîne comme délimiteur.

Enfin, il existe la méthode `istitle()` qui peut vérifier si une chaîne donnée est en casse de titre (title case) ou non.

```
def main():
    book_name = 'hearts in atlantis'

    print(f'Is "{book_name}" in title case? {book_name.istitle()}')
    print(f'Is "{book_name.title()}" in title case? {book_name.title().istitle()}')


if __name__ == '__main__':
    main()

# Is "hearts in atlantis" in title case? False
# Is "Hearts In Atlantis" in title case? True
```

Cependant, gardez à l'esprit que la méthode `istitle()` ne fonctionne pas avec la fonction d'aide `capwords()`.

### Comment convertir des chaînes en minuscules ou en majuscules en Python

En dehors de la mise en majuscule, vous voudrez peut-être convertir une chaîne entière en majuscules ou en minuscules. Vous pouvez le faire en utilisant les méthodes `upper()` et `lower()` en Python.

```
def main():
    book_name = 'moriarty'

    print(book_name.upper())

    another_book_name = 'DRACULA'

    print(another_book_name.lower())


if __name__ == '__main__':
    main()

# MORIARTY
# dracula
```

Il existe également les méthodes `isupper()` et `islower()` pour vérifier si une chaîne donnée est déjà dans l'une ou l'autre de ces casses ou non.

```
def main():
    book_name = 'moriarty'

    print(book_name)
    print(f'Is {book_name} in upper case? {book_name.isupper()}')
    print(f'Is {book_name} in lower case? {book_name.islower()}')

    another_book_name = 'DRACULA'

    print(another_book_name)
    print(f'Is {another_book_name} in upper case? {another_book_name.islower()}')
    print(f'Is {another_book_name} in lower case? {another_book_name.isupper()}')


if __name__ == '__main__':
    main()

# moriarty
# Is moriarty in upper case? False
# Is moriarty in lower case? True
# DRACULA
# Is DRACULA in upper case? True
# Is DRACULA in lower case? False
```

Il existe une dernière méthode appelée `casefold()` qui est une sorte de version plus agressive de la méthode `lower()`.

Selon la [documentation officielle][73] :

> Le casefolding est similaire à la mise en minuscules mais plus agressif car il est destiné à supprimer toutes les distinctions de casse dans une chaîne. Par exemple, la lettre minuscule allemande 'ß' est équivalente à "ss". Comme elle est déjà en minuscules, lower() ne ferait rien à 'ß' ; casefold() la convertit en "ss".

L'utilisation de cette méthode est identique à la méthode `lower()`.

```
def main():
    book_name = 'DRACULA'

    print(book_name.casefold())


if __name__ == '__main__':
    main()

# dracula
```

Ces trois méthodes sont fort utiles, mais que se passe-t-il si vous ne voulez utiliser aucune de ces méthodes particulières et que vous voulez simplement inverser la casse d'une chaîne donnée ?

La méthode `swapcase()` peut faire exactement cela.

```
def main():
    book_name = 'HEARTS IN ATLANTIS'

    print(book_name.swapcase())


if __name__ == '__main__':
    main()

# hearts in atlantis
```

Comme vous pouvez le voir, la méthode a converti le nom du livre en minuscules à partir des majuscules.

### Comment compter le nombre d'occurrences d'une sous-chaîne dans une chaîne en Python

Si vous voulez trouver le nombre d'occurrences d'une sous-chaîne à l'intérieur d'une chaîne, vous pouvez utiliser la méthode `count()` en Python.

```
def main():
    paragraph = '''At three in the morning the chief Sussex detective, obeying the urgent call from Sergeant Wilson of 
    Birlstone, arrived from headquarters in a light dog-cart behind a breathless trotter. By the five-forty train in 
    the morning he had sent his message to Scotland Yard, and he was at the Birlstone station at twelve o'clock to 
    welcome us. White Mason was a quiet, comfortable-looking person in a loose tweed suit, with a clean-shaved, 
    ruddy face, a stoutish body, and powerful bandy legs adorned with gaiters, looking like a small farmer, 
    a retired gamekeeper, or anything upon earth except a very favourable specimen of the provincial criminal 
    officer.'''

    substring = 'morning'

    print(f'The substring "{substring}" shows up {paragraph.count(substring)} times in the paragraph.')


if __name__ == '__main__':
    main()

# The substring "morning" shows up 2 times in the paragraph.
```

Si vous appelez la méthode `count()` sans rien lui passer, la méthode renverra le nombre d'espaces vides dans la chaîne donnée.

### Comment diviser et joindre des chaînes de caractères en Python

Vous pouvez en fait diviser une chaîne en une liste de mots ou joindre une liste de mots dans une chaîne en Python.

```
def main():
    string = 'Holmes was certainly not a difficult man to live with'

    word_list = string.split()

    print(word_list)


if __name__ == '__main__':
    main()

# ['Holmes', 'was', 'certainly', 'not', 'a', 'difficult', 'man', 'to', 'live', 'with']
```

Si vous appelez la méthode `split()` sans aucun paramètre, elle divisera la chaîne donnée en mots en utilisant les espaces comme séparateurs.

Vous pouvez passer outre en fournissant un séparateur personnalisé et également fixer le nombre de divisions que vous souhaitez.

```
def main():
    string = 'Holmes,was,certainly,not,a,difficult,man,to,live,with'

    word_list = string.split(',', 5)

    print(word_list)


if __name__ == '__main__':
    main()

# ['Holmes', 'was', 'certainly', 'not', 'a', 'difficult,man,to,live,with']
```

Cette fois, j'ai remplacé les espaces de la chaîne source par des virgules. J'ai également remplacé le séparateur par défaut par une virgule et fixé le nombre de divisions à cinq.

Comme vous pouvez le voir dans la sortie, il y a cinq divisions et le reste de la chaîne est conservé inchangé comme sixième élément de la liste.

La méthode `split()` est idéale pour les données qui ont été intentionnellement délimitées. L'utiliser avec du texte naturel comportant de la ponctuation peut produire des résultats inattendus.

L'opposé de la méthode `split()` est `join()` et elle fonctionne sur n'importe quel type d'itérateur en Python.

```
def main():
    word_list = ['Holmes', 'was', 'certainly', 'not', 'a', 'difficult', 'man', 'to', 'live', 'with']
    string = ''

    string = string.join(word_list)

    print(string)

    word_list = ['Holmes ', 'was ', 'certainly ', 'not ', 'a ', 'difficult ', 'man ', 'to ', 'live ', 'with']
    string = ''

    string = string.join(word_list)

    print(string)


if __name__ == '__main__':
    main()

# Holmeswascertainlynotadifficultmantolivewith
# Holmes was certainly not a difficult man to live with
```

Et voilà. Notez que la méthode `join()` ne s'est pas souciée d'ajouter des espaces comme séparateur après chaque mot lors du premier appel.

J'ai donc ajouté un espace à chaque mot de la liste et, lors du deuxième appel, la ligne est devenue beaucoup plus lisible.

## Comment écrire des instructions conditionnelles en Python

C'est ici que cela devient intéressant. En Python ou dans tout autre langage de programmation, vous pouvez prendre des décisions basées sur des conditions.

J'espère que vous vous souvenez du type de données `boolean` d'une section précédente – celui qui ne peut contenir que des valeurs `True` ou `False`.

Eh bien, vous pouvez utiliser un booléen avec une instruction `if` (une instruction conditionnelle) en Python pour effectuer une action de manière conditionnelle.

```
def main():
    number = int(input('what number would you like to check?\n- '))

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


if __name__ == '__main__':
    main()

# what number would you like to check?
# - 10
# 10 is even.
```

Vous commencez par écrire `if` suivi d'une condition et de deux points. Par condition, j'entends une instruction qui est évaluée à une valeur booléenne (vrai ou faux).

Vous utilisez l'opérateur `==` depuis le début et savez déjà qu'il vérifie si la valeur à sa gauche est égale à celle à sa droite ou non.

Ainsi, si vous divisez un nombre donné par 2 et que le reste est 0, c'est un nombre pair – sinon, il sera impair.

Vous pouvez utiliser l'instruction `if...else` pour choisir entre deux options différentes. Mais si vous avez plusieurs options parmi lesquelles choisir, vous pouvez utiliser l'instruction `if...elif...else`.

```
def main():
    year = int(input('which year would you like to check?\n- '))

    if year % 400 == 0 and year % 100 == 0:
        print(f"{year} is leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not leap year.")


if __name__ == '__main__':
    main()

# which year would you like to check?
# - 2004
# 2004 is leap year.
```

L'instruction `elif` se place généralement après une instruction `if` et avant une instruction `else`.

Considérez-la comme "else if" (sinon si), donc si l'instruction `if` échoue, alors le `elif` prendra le relais. Vous l'écrivez exactement comme une instruction `if` classique.

Une autre nouveauté dans cet exemple est l'opérateur `and`. C'est l'un des opérateurs logiques de Python. Il fait ce qu'il fait dans la vie réelle.

Si les expressions des deux côtés de l'instruction `and` sont évaluées à `true`, alors l'expression entière est évaluée à `true`. Simple.

Ne vous inquiétez pas si vous ne comprenez pas l'opérateur `and` en détail pour le moment. Vous en apprendrez plus sur lui et ses semblables dans la section suivante.

Une autre chose que vous devez comprendre est que ces instructions `if` ne sont que des instructions ordinaires, vous pouvez donc faire à peu près n'importe quoi à l'intérieur.

```
def main():
    number = int(input('what number would you like to check?\n- '))

    is_not_prime = False

    if number == 1:
        print(f"{number} is not a prime number.")
    elif number > 1:
        for n in range(2, number):
            if (number % n) == 0:
                is_not_prime = True
                break

        if is_not_prime:
            print(f"{number} is not a prime number.")
        else:
            print(f"{number} is a prime number.")


if __name__ == '__main__':
    main()

# what number would you like to check?
# - 10
# 10 is not a prime number.
```

Cet exemple est un peu plus complexe que ce que vous avez vu jusqu'à présent. Laissez-moi vous l'expliquer. Le programme vérifie si un nombre donné est un nombre premier ou non.

Tout d'abord, vous demandez un nombre à l'utilisateur. Pour qu'un nombre soit premier, il doit être divisible uniquement par 1 et par lui-même. Comme 1 n'est divisible que par 1, ce n'est pas un nombre premier.

Maintenant, si le nombre donné est supérieur à 1, vous devrez diviser le nombre par tous les nombres de 2 jusqu'à ce nombre particulier.

Si le nombre est divisible par l'un de ces nombres, vous passerez la variable `is_not_prime` à `True` et vous interromprez la boucle avec `break`.

L'instruction `break` permet simplement de sortir immédiatement d'une boucle. Il existe également l'instruction `continue` qui peut sauter l'itération actuelle au lieu de sortir de la boucle.

Enfin, si la variable `is_not_prime` est `True`, alors le nombre n'est pas premier, sinon c'est un nombre premier.

Comme vous pouvez le voir, non seulement vous pouvez mettre des boucles à l'intérieur d'une instruction conditionnelle, mais aussi mettre des instructions conditionnelles à l'intérieur d'une boucle.

Le dernier exemple que j'aimerais vous montrer est l'instruction `for...else`. Comme vous pouvez le voir dans l'exemple ci-dessus, vous avez une instruction `for` suivie d'une instruction `if...else`.

```
def main():
    number = int(input('what number would you like to check?\n- '))

    if number == 1:
        print(f"{number} is not a prime number.")
    elif number > 1:
        for n in range(2, number):
            if (number % n) == 0:
                print(f"{number} is not a prime number.")
                break
        else:
            print(f"{number} is a prime number.")


if __name__ == '__main__':
    main()

# what number would you like to check?
# - 5
# 5 is a prime number.
```

Si vous placez une instruction `else` au même niveau qu'une instruction `for`, alors Python exécutera tout ce que vous mettez à l'intérieur de ce bloc `else` dès que la boucle sera terminée.

## Quels sont les opérateurs relationnels et logiques en Python ?

Dans les exemples ci-dessus, vous avez vu l'utilisation de `==` ainsi que des opérateurs `and`. Dans cette section, vous en apprendrez plus sur eux en détail.

Les opérateurs relationnels sont utiles lorsque vous souhaitez vérifier la relation entre deux opérandes. Il existe six de ces opérateurs :

| OPÉRATEUR | EXPLICATION | UTILISATION |
| --- | --- | --- |
| `==` | Égal à | `5 == 5` donne `True`, mais `5 == 10` donne `False` |
| `!=` | Différent de | `5 != 10` donne `True`, mais `5 != 5` donne `False` |
| `>` | Supérieur à | `10 > 5` donne `True`, mais `5 > 10` donne `False` |
| `<` | Inférieur à | `5 < 10` donne `True`, mais `10 < 5` donne `False` |
| `>=` | Supérieur ou égal | `10 >= 5` et `10 >= 10` donnent `True`, mais `5 >= 10` donne `False` |
| `<=` | Inférieur ou égal | `5 <= 10` et `5 <= 5` donnent `True`, mais `10 <= 5` donne `False` |

Vous utilisez l'opérateur `égal à` depuis le tout début. Vous découvrirez les autres au fur et à mesure.

En dehors de ceux-ci, il existe trois opérateurs logiques en Python. Ce sont les opérateurs `and`, `or` et `not`.

Prenez un jeu RPG, par exemple, où le héros doit avoir un bouclier de niveau 45 ou plus et une épée de niveau 48 ou plus pour passer au niveau suivant.

```
def main():
    shield = int(input('what is your shield level? '))
    sword = int(input('what is your sword level? '))

    if shield >= 45 and sword >= 48:
        print('you shall pass!')
    else:
        print('you shall not pass!')


if __name__ == '__main__':
    main()

# what is your shield level? 42
# what is your sword level? 52
# you shall not pass!
```

À moins de remplir les deux conditions, l'instruction sera évaluée à `False`. Vous pouvez avoir plus de conditions dans une instruction comme celle-ci :

```
def main():
    shield = int(input('what is your shield level? '))
    sword = int(input('what is your sword level? '))
    armor = int(input('what is your armor level? '))

    if shield >= 45 and sword >= 48 and armor >= 25:
        print('you shall pass!')
    else:
        print('you shall not pass!')


if __name__ == '__main__':
    main()

# what is your shield level? 45
# what is your sword level? 50
# what is your armor level? 10
# you shall not pass!
```

L'opérateur `or`, en revanche, est un peu plus indulgent. Si l'une des conditions données est évaluée à vrai, alors l'instruction entière sera évaluée à vrai.

Par exemple, dans un autre jeu d'horreur, vous ne pouvez entrer dans le château de Dracula que si vous avez plus de 500 000 ans ou si vous êtes légalement mort.

```
def main():
    age = 10_000
    is_legally_dead = True

    if is_legally_dead or age > 500_000:
        print('you shall pass!')
    else:
        print('you shall not pass!')


if __name__ == '__main__':
    main()

# you shall pass!
```

Vous pouvez mélanger les opérateurs `and` et `or` ensemble. Je ne listerai pas toutes les combinaisons possibles de ces opérateurs, mais au fur et à mesure que vous travaillerez avec Python, vous en utiliserez beaucoup.

Le dernier opérateur logique dont j'aimerais discuter est l'opérateur `not`. Cet opérateur ne prend qu'un seul opérande et renvoie la valeur opposée.

```
def main():
    print('not True =', not True)
    print('not False =', not False)


if __name__ == '__main__':
    main()

# not True = False
# not False = True
```

Par exemple, si vous changez les règles du jeu d'horreur dont nous avons parlé dans l'exemple précédent et faites en sorte que seules les personnes de plus de 500 000 ans et qui ne sont pas Van Helsing puissent entrer dans le château.

```
def main():
    age = 800_000
    is_van_helsing = True

    if age > 500_000 and not is_van_helsing:
        print('you shall pass!')
    else:
        print('you shall not pass!')


if __name__ == '__main__':
    main()

# you shall not pass!
```

Puisque nous avons parlé des instructions conditionnelles et de certains opérateurs qui leur sont associés, j'aimerais vous présenter une autre instruction introduite pour la première fois dans Python 3.10, l'instruction `match...case`.

[https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/][74]

Comme mon collègue [Kolade Chris][75] a écrit un excellent article sur le sujet, je ne le répéterai pas ici. N'hésitez pas à le consulter à votre guise.

## Quels sont les opérateurs d'affectation en Python ?

Vous avez déjà rencontré l'opérateur d'affectation simple qui est le signe `=` que vous avez utilisé pour attribuer une valeur à une variable.

Il existe maintenant quelques variantes de cet opérateur que vous pouvez utiliser pour effectuer des opérations arithmétiques et bit à bit tout en attribuant une valeur.

Les opérations bit à bit sortent un peu du cadre de ce livre, je m'en tiendrai donc aux opérations arithmétiques.

Il existe sept opérateurs d'affectation différents en Python. Comme vous avez déjà appris l'opérateur simple, je discuterai des six autres dans le tableau suivant.

| OPÉRATEUR | UTILISATION | ÉQUIVALENT À |
| --- | --- | --- |
| `+=` | `a += b` | `a = a + b` |
| `-=` | `a -= b` | `a = a - b` |
| `*=` | `a *= b` | `a = a * b` |
| `/=` | `a /= b` | `a = a / b` |
| `%=` | `a %= b` | `a = a % b` |
| `**=` | `a **= b` | `a = a ** b` |

Ces opérateurs ne sont pas exclusifs à Python, et dans la plupart des ressources de programmation, vous les trouverez dans un chapitre bien antérieur.

Mais je voulais attendre que vous ayez appris à récupérer les entrées utilisateur, à travailler avec les ranges et à boucler sur eux avant de les introduire ici.

Supposons que vous vouliez écrire un programme qui calcule la somme de tous les nombres dans une plage donnée.

```
def main():
    start = int(input('which number do you want to start from?\n- '))
    end = int(input('which number do you want to stop at?\n- '))

    total = 0

    for number in range(start, end + 1):
        total += number

    print(f"the sum of the numbers between {start} and {end} is: {total}")


if __name__ == '__main__':
    main()

# which number do you want to start from?
# - 1
# which number do you want to stop at?
# - 10
# the sum of the numbers between 1 and 10 is: 55
```

J'espère que vous vous souvenez que le nombre de fin d'une fonction `range()` est exclusif. J'ai donc dû ajouter un `+1` au nombre de fin.

Sinon, c'est une boucle for basée sur une plage très simple qui ajoute chaque nombre à la variable `total` et l'affiche une fois la boucle terminée.

## Qu'est-ce que le type Set en Python ?

Jusqu'à présent, vous avez découvert un certain nombre de types itérables tels que les listes, les tuples et aussi les chaînes de caractères. Il en existe un autre connu sous le nom de set (ensemble). Regardons un exemple :

```
def main():
    numbers = {1, 2, 3, 4, 5}

    for number in numbers:
        print(number)


if __name__ == '__main__':
    main()

# 1
# 2
# 3
# 4
# 5
```

Vous pouvez créer un nouveau set en plaçant les valeurs entre des accolades. Gardez à l'esprit cependant que vous ne pouvez pas créer un set vide en utilisant des accolades.

Vous devrez utiliser la fonction `set()` pour cela.

```
def main():
    numbers = {}

    print(type(numbers))

    numbers = set()

    print(type(numbers))


if __name__ == '__main__':
    main()

# <class 'dict'>
# <class 'set'>
```

Comme vous pouvez le voir, l'utilisation d'accolades vides crée un dictionnaire alors que la fonction `set()` crée un set vide.

Les sets peuvent sembler similaires aux listes, mais ils sont en réalité assez différents. Pour commencer, vous ne pouvez pas mettre de valeurs en double dans un set.

```
def main():
    numbers_list = [1, 2, 3, 4, 5, 3, 2, 4]

    print(numbers_list)

    numbers_set = set(numbers_list)

    print(numbers_set)


if __name__ == '__main__':
    main()

# [1, 2, 3, 4, 5, 3, 2, 4]
# {1, 2, 3, 4, 5}
```

La liste de nombres peut contenir des valeurs en double sans aucun problème. Mais dès que vous créez un set à partir de cette liste, toutes les valeurs en double disparaissent.

Les sets sont mutables, vous pouvez donc ajouter de nouvelles valeurs à un set en utilisant la méthode `add()`.

```
def main():
    numbers = {1, 2, 3, 4, 5}

    numbers.add(500)

    print(numbers)


if __name__ == '__main__':
    main()

# {1, 2, 3, 4, 5, 500}
```

De même, vous pouvez utiliser la méthode `discard()` pour supprimer un élément d'un set ou utiliser la méthode `clear()` pour supprimer toutes les valeurs d'un coup.

```
def main():
    numbers = {1, 2, 3, 4, 5}

    numbers.discard(3)

    print(numbers)

    numbers.clear()

    print(numbers)


if __name__ == '__main__':
    main()

# {1, 2, 4, 5}
# set()
```

Notez comment un set vide s'affiche comme `set()` au lieu de `{}` car ce dernier indique un dictionnaire vide.

Outre le fait qu'un set ne contient jamais de valeurs en double, il existe une autre spécialité de ce type.

Vous pouvez effectuer des opérations sur les ensembles telles que l'union, l'intersection, le complément et la différence en utilisant les sets en Python.

Ma collègue [Estefania Cassingena Navone][76] a écrit un excellent guide sur les sets, les frozensets et toutes les opérations que vous pouvez effectuer sur eux.

[https://www.freecodecamp.org/news/python-sets-detailed-visual-introduction/][77]

Enfin, si vous souhaitez avoir un aperçu définitif du type set, la [documentation officielle][78] sera plus que suffisante.

## Qu'est-ce que le type Mapping en Python ?

Vous avez déjà découvert les types de séquences et les types de sets en Python. Ceux-ci sont vraiment utiles pour contenir un tas de données.

Mais les situations où vous souhaitez stocker des données sous forme de paires clé-valeur ne sont pas rares. Prenez, par exemple, une librairie en ligne où vous devez stocker les prix des livres.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    print(programming_books)


if __name__ == '__main__':
    main()

# {'C Programming Language': 35, 'Introduction to Algorithms': 100, 'Clean Code: A Handbook of Agile Software Craftsmanship': 50}
```

La variable `programming_books` ici est un type Mapping généralement connu sous le nom de dictionnaire (dictionary). Déclarer un dictionnaire est similaire à déclarer une liste ou un tuple, mais vous utilisez des accolades au lieu de crochets ou de parenthèses.

À l'intérieur des accolades se trouvent un tas de paires clé-valeur. Les chaînes de caractères sur le côté gauche sont les clés et les nombres sont les valeurs. Vous pouvez accéder à n'importe laquelle des clés en utilisant la méthode `get()`.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    cpl = 'C Programming Language'
    algo = 'Introduction to Algorithms'

    print(f"The price of {cpl} is ${programming_books.get(cpl)}")
    print(f"The price of {algo} is ${programming_books[algo]}")


if __name__ == '__main__':
    main()

# The price of C Programming Language is $35
# The price of Introduction to Algorithms is $100
```

Alternativement, vous pouvez également utiliser des crochets comme vous l'avez fait avec les listes pour accéder à un élément du dictionnaire.

Les dictionnaires sont mutables, ce qui signifie que vous pouvez y ajouter de nouveaux éléments, supprimer ou modifier des éléments existants.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    key = 'C Programming Language'

    programming_books[key] = 45

    programming_books['The Pragmatic Programmer'] = 32

    print(programming_books)


if __name__ == '__main__':
    main()

# {'C Programming Language': 45, 'Introduction to Algorithms': 100, 'Clean Code: A Handbook of Agile Software Craftsmanship': 50, 'The Pragmatic Programmer': 32}
```

Vous pouvez modifier un élément existant en y accédant à l'aide des crochets et en lui attribuant une nouvelle valeur. Le prix de C Programming Language a augmenté de 10 $.

Si vous mettez une clé inexistante entre les crochets, elle apparaîtra comme un nouvel élément. Le prix de The Pragmatic Programmer n'était pas dans le dictionnaire auparavant, mais il a maintenant été ajouté.

Pour supprimer un élément d'un dictionnaire, vous pouvez utiliser la méthode `popitem()` ou `pop()`.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    print(programming_books.popitem())

    key = 'C Programming Language'

    print(programming_books.pop(key))

    print(programming_books)


if __name__ == '__main__':
    main()

# ('Clean Code: A Handbook of Agile Software Craftsmanship', 50)
# 35
# {'Introduction to Algorithms': 100}
```

La méthode `popitem()` supprime le dernier élément du dictionnaire et le renvoie sous forme de tuple.

La méthode `pop()`, quant à elle, renvoie la valeur d'une clé donnée et supprime la paire.

Le dernier appel à la fonction `print()` montre qu'en effet deux éléments ont été supprimés du dictionnaire suite aux appels pop.

Enfin, il existe la méthode `clear()` qui efface toutes les paires d'un dictionnaire donné d'un seul coup.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    programming_books.clear()

    print(programming_books)


if __name__ == '__main__':
    main()

# {}
```

### Que sont les objets de vue de dictionnaire en Python ?

Jusqu'à présent dans cette section, vous avez vu des dictionnaires affichés sous forme de longues lignes séparées par des virgules entre des accolades – mais ce n'est pas très lisible.

C'est là que les objets de vue (view objects) s'avèrent utiles. Vous pouvez appeler certaines méthodes spécifiques sur les dictionnaires et obtenir des objets de vue en retour.

La première méthode dont je vais discuter est la méthode `keys()`. Elle renvoie les clés d'un dictionnaire donné et vous pouvez boucler sur elles.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    for key in programming_books.keys():
        print(key)


if __name__ == '__main__':
    main()

# C Programming Language
# Introduction to Algorithms
# Clean Code: A Handbook of Agile Software Craftsmanship
```

Tout comme la méthode `keys()`, il existe la méthode `values()` qui renvoie les valeurs d'un dictionnaire à la place.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    for value in programming_books.values():
        print(value)


if __name__ == '__main__':
    main()

# 35
# 100
# 50
```

Enfin, si vous voulez à la fois les clés et les valeurs sous forme de tuples, vous pouvez utiliser la méthode `items()`.

```
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    for item in programming_books.items():
        print(item)


if __name__ == '__main__':
    main()

# ('C Programming Language', 35)
# ('Introduction to Algorithms', 100)
# ('Clean Code: A Handbook of Agile Software Craftsmanship', 50)
```

## Comment écrire des fonctions en Python

Une fonction en Python (et en programmation en général) est une collection d'instructions autonome qui effectue une tâche unique.

```
def print_hello():
    print('Hello, World!')


def main():
    print_hello()


if __name__ == '__main__':
    main()

# Hello, World!
```

Vous définissez une fonction en écrivant `def` suivi du nom de la fonction et de deux points. Vous pouvez ensuite écrire le corps de la fonction à partir de la ligne indentée suivante.

Dans cet exemple, `print_hello()` affiche `Hello, World!` sur le terminal. Elle n'accepte aucun argument.

```
def print_hello(message):
    print(message)


def main():
    print_hello('Hello, Universe!')


if __name__ == '__main__':
    main()

# Hello, Universe!
```

Maintenant, au lieu d'afficher `Hello, World!` tout le temps, vous pouvez passer un message personnalisé pour que la fonction l'affiche.

Vous pouvez faire en sorte qu'une fonction accepte plusieurs arguments et même définir une valeur par défaut pour l'un d'eux.

```
def print_hello(message, is_lower=False):
    if is_lower:
        print(message.lower())
    else:
        print(message.upper())


def main():
    print_hello('Hello, Universe!')
    print_hello('Hello, Universe!', True)


if __name__ == '__main__':
    main()

# HELLO, UNIVERSE!
# hello, universe!
```

Définir une valeur par défaut pour un paramètre de fonction le rend optionnel. Ainsi, si vous ne passez pas de valeur lors de l'appel de la fonction, votre programme utilisera la valeur par défaut.

Au lieu d'afficher le message directement, vous pouvez faire en sorte que la fonction renvoie le message.

```
def hello(message, is_lower=False):
    if is_lower:
        return message.lower()
    else:
        return message.upper()


def main():
    print(hello('Hello, Universe!'))
    print(hello('Hello, Universe!', True))


if __name__ == '__main__':
    main()

# HELLO, UNIVERSE!
# hello, universe!
```

Comme la fonction n'affiche plus le message directement, changer son nom de `print_hello()` en simplement `hello()` est plus logique.

Lorsque vous appelez la fonction avec ou sans message personnalisé, la fonction renvoie une chaîne de caractères que vous pouvez ensuite afficher à l'intérieur de la fonction `main()`.

Vous pouvez également enregistrer le message dans des variables au lieu de les passer directement à la fonction `print()`.

```
def hello(message, is_lower=False):
    if is_lower:
        return message.lower()
    else:
        return message.upper()


def main():
    uppercase_message = hello('Hello, Universe!')
    print(uppercase_message)

    lowercase_message = hello('Hello, Universe!', True)
    print(lowercase_message)


if __name__ == '__main__':
    main()

# HELLO, UNIVERSE!
# hello, universe!
```

Il n'est pas nécessaire de ne passer que des valeurs simples à une fonction. Vous pouvez passer des listes, des tuples, des dictionnaires ou tout autre objet à une fonction.

```
def total(numbers):
    s = 0
    for number in numbers:
        s += number
    return s


def main():
    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


if __name__ == '__main__':
    main()

# 55
```

Dans cette fonction, vous pouvez passer une liste de nombres et obtenir leur somme. J'ai dû nommer la fonction `total()` au lieu de `sum()` car il existe une fonction intégrée portant ce nom.

Il y a un dernier concept concernant les fonctions que j'aimerais aborder dans cette section, et c'est la récursivité.

La récursivité en Python ou en programmation en général est la technique consistant à faire en sorte qu'une fonction s'appelle elle-même pour effectuer une tâche de manière itérative.

Par exemple, imaginez une fonction qui accepte un entier et calcule la somme de tous les nombres naturels jusqu'à cet entier donné. Vous pouvez écrire ce programme en utilisant des boucles.

```
def natural_sum(last_number):
    if last_number < 1:
        return last_number

    total = 0
    for number in range(1, last_number + 1):
        total += number

    return total


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(natural_sum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55
```

Il n'y a rien de nouveau ici, juste l'utilisation régulière d'une boucle for basée sur une plage. Maintenant, vous pouvez également écrire le même programme sans aucune boucle.

```
def recursive_natural_sum(last_number):
    if last_number < 1:
        return last_number

    return last_number + recursive_natural_sum(last_number - 1)


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(recursive_natural_sum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55
```

À première vue, ce morceau de code peut vous sembler très compliqué. Mais en réalité, il est très simple. Décomposons-le étape par étape.

Lorsque vous appelez la fonction `recursive_natural_sum()` avec la valeur 10 pour la première fois, vous déclenchez une sorte de réaction en chaîne.

Comme la valeur n'est pas inférieure à 1, l'instruction `if` est évaluée à `False` et la seconde instruction `return` est appelée.

À l'intérieur de cette instruction `return`, vous appelez la fonction `recursive_natural_sum()` en passant la valeur de `last_number - 1` qui est 9 à ce stade.

Vous ajoutez également la valeur renvoyée par cet appel à la valeur actuelle de la variable `last_number`.

Mais vous n'obtiendrez pas de valeur de retour immédiatement car votre appel de fonction interne s'appellera à nouveau avec `last_number - 1` qui sera 8 à ce moment-là.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/recursion-1.drawio.svg)

Ces appels se poursuivent jusqu'à ce que la valeur de `last_digit` devienne zéro. Une fois qu'elle devient zéro, l'instruction `if` est évaluée à `True` et les appels de fonction commencent à renvoyer une valeur.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/recursion-2.drawio-1.svg)

La valeur renvoyée par chaque appel de fonction est `last_digit + (last_digit - 1)`. À la fin de la chaîne de récursivité, elle s'additionne pour donner 55.

Mon collègue [Beau Carnes][79] a écrit un article plus approfondi expliquant le fonctionnement de la récursivité. Vous pouvez y jeter un œil si vous voulez en savoir plus.

[https://www.freecodecamp.org/news/how-recursion-works-explained-with-flowcharts-and-a-video-de61f40cb7f9/][80]

Je ne dis pas que les fonctions récursives sont plus faciles que les boucles – mais parfois, utiliser une fonction récursive au lieu de boucles imbriquées peut être plus efficace.

### Comment écrire des fonctions anonymes ou lambda en Python

Les fonctions anonymes ou lambda sont des fonctions sans nom. Ce n'est pas quelque chose d'exclusif à Python et la plupart des langages de programmation modernes ont une sorte d'implémentation lambda.

Au lieu de commencer la déclaration de la fonction par `def`, vous commencez par écrire `lambda` suivi de deux points et du corps de la fonction.

```
print_hello = lambda: print('Hello, World!')


def main():
    print_hello()


if __name__ == '__main__':
    main()

# Hello, World!
```

Comme les lambdas n'ont pas de nom, vous devez les mettre dans une variable pour y accéder, mais cela n'est pas recommandé. Si vous avez besoin d'une fonction nommée, utilisez `def` à la place.

Les fonctions lambda sont utiles lorsque vous souhaitez passer une fonction comme argument à un autre appel de fonction. Prenez la fonction `filter()` par exemple.

```
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]

    even_numbers = filter(check_even, numbers)

    print(list(even_numbers))


if __name__ == '__main__':
    main()

# [2, 4, 88, 12]
```

La fonction `filter()` prend une fonction et un type itérable comme deux arguments. La fonction doit décrire la logique de filtrage et le type itérable contiendra les valeurs que vous souhaitez filtrer.

Dans ce code, vous avez une liste de nombres et vous voulez filtrer les nombres impairs de cette liste.

La fonction `check_even()` prend un nombre comme argument. Elle renvoie ensuite `True` si le nombre est divisible par deux et `False` sinon.

La fonction `filter()` parcourt la liste de nombres et passe chaque nombre à la fonction `check_even()`.

Elle conserve le nombre si la fonction `check_even()` renvoie `True` ou rejette le nombre si la fonction `check_even()` renvoie `False`.

Maintenant, cette fonction `check_even()` n'a d'autre but que de vérifier si un nombre donné est divisible par deux ou non. Vous pouvez donc l'écrire sous forme de lambda.

```
def main():
    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]

    even_numbers = filter(lambda number: True if number % 2 == 0 else False, numbers)

    print(list(even_numbers))


if __name__ == '__main__':
    main()

# [2, 4, 88, 12]
```

Cette lambda prend un argument nommé `number` puis renvoie `True` s'il est divisible par deux et `False` sinon.

Vous pouvez ajouter plusieurs arguments en séparant chacun par une virgule. Enfin, une lambda n'a pas besoin d'une instruction return, mais vous pouvez en supposer une.

Ainsi, `True if number % 2 == 0 else False` est équivalent à `return True if number % 2 == 0 else False`. L'instruction `if...else` à l'intérieur de la lambda est sous forme abrégée.

### Comment travailler avec les variables locales, non locales et globales en Python

La portée (scope) d'une variable en Python ou en programmation en général se réfère à la région où cette variable est accessible.

```
def outside():
    message = 'Hello, World!'


def main():
    print(message)


if __name__ == '__main__':
    main()

# NameError: name 'msg' is not defined
```

Dans cet exemple, la variable `message` est définie à l'intérieur de la fonction `outside()` et elle n'existe nulle part ailleurs.

Par conséquent, lorsque vous essayez d'accéder à cette variable depuis la fonction `main()`, vous obtenez une `NameError` puisque la variable est limitée à la portée de la fonction `outside()`.

Les variables de ce type sont appelées variables locales et elles n'existent qu'à l'intérieur du bloc où elles ont été déclarées.

Les variables globales, en revanche, sont généralement déclarées en dehors de tout bloc de code particulier.

```
message = 'Hello, World!'


def main():
    print(message)


if __name__ == '__main__':
    main()

# Hello, World!
```

Comme vous pouvez le voir, maintenant la variable `message` n'a pas d'indentation et est déclarée en haut de la fonction. Vous auriez pu déclarer la variable après la fonction `main()`.

```
def main():
    print(message)


message = 'Hello, World!'

if __name__ == '__main__':
    main()

# Hello, World!
```

Cela fonctionne parce que vous n'essayez pas d'accéder à la variable avant d'appeler la fonction `main()` à l'intérieur de l'instruction `if`.

Bien que les variables globales soient accessibles à peu près partout, il peut être un peu délicat de travailler avec elles si vous avez une variable locale portant un nom similaire.

```
message = 'Hello, {name}!'


def main():
    message = message.format(name='Farhan')
    print(message)


if __name__ == '__main__':
    main()

# UnboundLocalError: local variable 'message' referenced before assignment
```

Dans ce code, vous avez un espace réservé (placeholder) pour un nom à l'intérieur de la variable `message`. Vous pouvez utiliser la méthode `format()` pour y mettre un nom.

Mais si vous essayez d'exécuter ce code, vous obtiendrez un message `local variable 'message' referenced before assignment`. En termes plus simples, vous essayez d'accéder à une variable locale nommée `message` avant même de lui avoir assigné quoi que ce soit.

Il est clair que Python cherche une variable locale portant le nom donné au lieu d'accéder à la variable globale. Puisqu'il la réclame, essayez de lui donner une variable locale.

```
message = 'Hello, {name}!'


def main():
    message = str()

    message = message.format(name='Farhan')
    print(message)


if __name__ == '__main__':
    main()
```

Cette fois, l'erreur aura disparu mais vous n'obtiendrez aucune sortie dans votre console. C'est parce que la variable locale `message` est vide et qu'il n'y a pas d'espace réservé pour y mettre un nom.

C'est là qu'intervient le mot-clé `global`. Au lieu de créer une variable locale, vous pouvez faire savoir à Python que vous essayez d'accéder à la variable globale `message`.

```
message = 'Hello, {name}!'


def main():
    global message

    message = message.format(name='Farhan')
    print(message)


if __name__ == '__main__':
    main()

# Hello, Farhan!
```

Désormais, au lieu d'essayer de chercher une variable nommée `message` dans la portée locale, Python s'adressera directement à la portée globale.

Enfin, il existe le mot-clé `nonlocal` généralement utilisé dans les fonctions imbriquées. Il résout un problème similaire au mot-clé `global` mais dans une portée locale.

```
def greet(name):
    message = 'Hello, {name}!'

    def include_name():
        message = message.format(name=name)

    include_name()
    return message


def main():
    print(greet('Farhan'))


if __name__ == '__main__':
    main()

# UnboundLocalError: local variable 'message' referenced before assignment
```

Dans cet exemple, vous avez affaire à trois fonctions. Il y a la fonction `main()`, il y a la fonction `greet()`, et à l'intérieur de celle-ci se trouve la fonction `include_name()`.

La fonction `greet()` prend un nom comme argument mais ne l'inclut pas tout de suite dans le message.

Au lieu de cela, elle appelle la fonction `include_name()` définie dans sa portée locale. C'est là que le problème commence.

Voyez-vous, la variable `message` est en dehors de la portée de la fonction `include_message()` et c'est pourquoi vous obtenez le message d'erreur `referenced before assignment`.

```
def greet(name):
    message = 'Hello, {name}!'

    def include_name():
        global message

        message = message.format(name=name)

    include_name()
    return message


def main():
    print(greet('Farhan'))


if __name__ == '__main__':
    main()

# NameError: name 'message' is not defined
```

Vous ne pouvez pas non plus utiliser le mot-clé `global` puisque la variable `message` n'est pas définie dans la portée globale et c'est ce que dicte le message d'erreur.

Vous pouvez utiliser le mot-clé `nonlocal` pour utiliser des variables qui ne sont pas dans la portée globale mais dans la portée de la fonction extérieure.

```
def greet(name):
    message = 'Hello, {name}!'

    def include_name():
        nonlocal message
        message = message.format(name=name)

    include_name()
    return message


def main():
    print(greet('Farhan'))


if __name__ == '__main__':
    main()

# Hello, Farhan!
```

Désormais, la fonction `include_name()` cherchera la variable `message` dans la portée de la fonction `greet()` au lieu de sa propre portée locale.

### Comment passer un nombre variable d'arguments à une fonction en utilisant \*args et \*\*kwargs en Python

Imaginez une fonction qui prend un tas de nombres comme arguments et renvoie leur somme. Dans une fonction comme celle-ci, il serait agréable d'avoir la possibilité de passer un nombre variable d'arguments.

Certes, vous pouvez passer les nombres sous forme de tuple ou de liste, mais vous voudrez peut-être les passer comme des arguments ordinaires séparés par des virgules. Vous pouvez le faire en utilisant `*args` ou des arguments non-clés en Python.

```
def total(*args):
    print(type(args))

    t = 0
    for arg in args:
        t += arg

    return t


def main():
    print(total(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()

# <class 'tuple'>
# 15
```

Ici, vous pouvez passer un nombre arbitraire de variables à la fonction `total()` en tant qu'argument et vous y aurez accès sous forme de tuple à l'intérieur de cette fonction.

Il n'est pas obligatoire de nommer l'argument `*args`, vous pouvez l'appeler quelque chose de plus descriptif comme `*numbers` ou n'importe quoi d'autre. Tant que vous mettez l'astérisque devant, tout va bien.

Comme `*args`, il existe également `**kwargs` ou arguments par mots-clés qui vous permettront d'accéder aux arguments de la fonction sous forme de dictionnaire.

```
def items(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} : {value}")


def main():
    items(
        Apple=10,
        Orange=8,
        Grape=35
    )


if __name__ == '__main__':
    main()

# <class 'dict'>
# Apple : 10
# Orange : 8
# Grape : 35
```

Dans ce cas, vous pouvez passer un nombre arbitraire de paires clé-valeur et y accéder sous forme de dictionnaire à l'intérieur de la fonction `items()`.

Tout comme le mot-clé `*args`, vous n'êtes pas obligé de le nommer absolument `**kwargs`. Au lieu de cela, vous pouvez le nommer comme vous le souhaitez.

Tant que vous mettez les deux astérisques devant, tout ira bien. La méthode `items()` à l'intérieur des dictionnaires vous permet d'itérer à travers eux.

Vous pouvez également changer les noms des variables `key` et `value`. Une version plus lisible de la fonction peut être la suivante :

```
def items(**fruits):
    print(type(fruits))

    for fruit, price in fruits.items():
        print(f"{fruit} : {price}")


def main():
    items(
        Apple=10,
        Orange=8,
        Grape=35
    )


if __name__ == '__main__':
    main()

# <class 'dict'>
# Apple : 10
# Orange : 8
# Grape : 35
```

Gardez à l'esprit que le type des clés dans ce cas doit être une chaîne de caractères et les valeurs peuvent être tout ce que vous voulez.

## Que sont les modules en Python ?

Au fur et à mesure que votre projet grandit, diviser votre code en plusieurs fichiers devient une nécessité. Un module en Python est simplement un fichier contenant du code Python que vous pouvez importer dans d'autres fichiers Python.

Par exemple, supposons que vous ayez un projet Python avec deux fichiers. Le premier peut être "mathstuff.py" et l'autre peut être "main.py".

Le fichier "mathstuff.py" peut contenir des éléments liés aux mathématiques, par exemple une fonction qui additionne tous les nombres naturels d'une plage.

```
# mathstuff.py

def natural_sum(last_number):
    if last_number < 1:
        return last_number

    total = 0
    for number in range(1, last_number + 1):
        total += number

    return total
```

Maintenant vous pouvez importer cette fonction dans n'importe quel autre fichier tel que le fichier "main.py".

```
import mathstuff


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(mathstuff.natural_sum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55
```

L'instruction `import`, comme son nom l'indique, importe des morceaux de code d'un autre fichier ou module.

Il n'est pas rare d'héberger plus d'une fonction, variable ou autre objet dans un module Python et souvent vous ne voudrez en utiliser que quelques-uns.

Vous pouvez utiliser l'instruction `from...import` dans ces situations.

```
from mathstuff import natural_sum


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(natural_sum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55
```

Cela vous évite également d'avoir à écrire le nom du module chaque fois que vous voulez accéder à une fonction ou à un objet vivant à l'intérieur de ce module.

Enfin, vous pouvez utiliser le mot-clé `as` pour changer le nom d'un module importé afin de le rendre plus facilement accessible.

```
import mathstuff as math


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(math.natural_sum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55
```

Cela fonctionne également avec l'instruction `from...import`.

```
from mathstuff import natural_sum as nsum


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(nsum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55
```

L'importation de modules est une chose que vous devrez faire tout le temps. Outre les modules, il existe également l'idée de packages (paquets).

Dans ces exemples, les deux fichiers se trouvent dans le même dossier. Les packages sont un moyen astucieux de regrouper des modules Python connexes dans différents dossiers.

Par exemple, dans un framework web, vous pouvez avoir un package appelé `framework` qui héberge tout le code fourni avec ce framework web.

Maintenant, ce package `framework` peut à son tour avoir plusieurs sous-packages – par exemple, il peut y avoir un package nommé `http` pour gérer les requêtes et les réponses HTTP.

```
├───framework
│   └───http
```

Pour l'instant, ce ne sont que des dossiers ordinaires. Pour les transformer en Python, tout ce dont vous avez besoin est de créer des fichiers `__init__.py` à l'intérieur.

```
├───framework
│   │   __init__.py
│   │
│   └───http
│           __init__.py
```

Maintenant, ces fichiers sont devenus des packages. Ces fichiers `__init__.py` indiqueront au système d'importation de Python que ces dossiers sont bien des packages.

Enfin, pour mettre du code à l'intérieur du package `http`, créez un fichier nommé `response.py` avec le contenu suivant :

```
# framework/http/response.py

from json import dumps


def as_json(message):
    return dumps({
        'message': message
    })
```

Tout d'abord, vous importez la fonction `dumps` du package `json`. Ceux-ci font partie de la bibliothèque standard de Python.

La fonction `dumps` peut transformer un objet Python comme un dictionnaire en une chaîne JSON, ce qui signifie que la fonction `as_json()` renvoie une valeur donnée au format JSON.

```
{"message": "Hello, World"}
```

Maintenant vous pouvez importer cette fonction dans le fichier "main.py".

```
from framework.http.response import as_json


def main():
    print(as_json('Hello, World!'))


if __name__ == '__main__':
    main()

# {"message": "Hello, World"}
```

Au lieu de mettre la fonction `as_json()` dans un autre fichier Python, vous pouvez simplement la mettre à l'intérieur du fichier "framework/http/__init__.py".

Ensuite, vous pouvez mettre à jour le fichier "main.py" pour utiliser le chemin de package mis à jour.

```
from framework.http import as_json


def main():
    print(as_json('Hello, World!'))


if __name__ == '__main__':
    main()

# {"message": "Hello, World"}
```

Si jamais vous essayez un framework comme Django, vous verrez que le framework contient une énorme quantité de packages, donc comprendre comment fonctionne le système d'importation vous aidera énormément.

## Comment utiliser efficacement la documentation Python

Puisque vous n'êtes plus un novice en tant que programmeur Python, j'aimerais vous montrer comment vous pouvez parcourir la documentation officielle de Python.

Vous pourriez penser que parcourir la documentation n'est pas difficile et vous auriez tout à fait raison. Mais cela peut être intimidant au début.

Ce que je vais donc faire, c'est vous donner une petite introduction sur la façon dont j'ai utilisé la documentation tout au long de ma carrière.

La première étape consiste à visiter [https://docs.python.org/][81] et vous atterrirez automatiquement sur la documentation de la dernière version de Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-154.png) _Documentation Python ([https://docs.python.org/][82])_

Au moment de la rédaction de cet article, la dernière version de Python est la 3.11.4, mais j'ai toujours la version 3.10.11 installée sur mes ordinateurs.

Dès le départ, vous pouvez voir de nombreux liens différents vers d'autres pages et, pour être honnête, vous n'allez pas avoir besoin de tous immédiatement.

La meilleure façon de savoir quel lien mène à quelle page est de jeter un œil à tout ce qui vous semble intéressant.

Je vais parler de trois liens de cette page qui m'ont énormément aidé. Le premier est la page "Tutorial".

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-155.png) _Le tutoriel Python (https://docs.python.org/3/tutorial/index.html)_

À l'époque où je passais du C au Python, c'est le tutoriel que j'ai suivi. Le tutoriel commence par une introduction à l'interprète Python.

Ensuite, il vous enseigne des sujets incluant, sans s'y limiter, les types de données, les instructions de flux de contrôle, les structures de données, les modules, la gestion des erreurs, la bibliothèque standard et même la programmation orientée objet.

L'autre page extrêmement utile est la page "Glossary". Elle contient une liste de tous les termes importants que vous pourriez rencontrer en travaillant avec Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-156.png) _Glossaire (https://docs.python.org/3/glossary.html)_

Ainsi, à tout moment, si vous sentez que vous ne connaissez pas la signification d'un mot, jetez un œil au glossaire.

Enfin, la page "Library Reference" est une description détaillée de tout ce qui est inclus dans la bibliothèque standard de Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-158.png) _Référence de la bibliothèque (https://docs.python.org/3/library/index.html)_

Disons, par exemple, que j'aimerais en savoir plus sur le type gestionnaire de contexte (context manager), qui dépasse le cadre de ce livre. Je peux simplement regarder dans la section "Built-in Types".

Ou si vous voulez savoir autre chose comme le package JSON, vous pouvez rechercher JSON dans la référence de la bibliothèque – et bien sûr, vous trouverez quelque chose à ce sujet.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-159.png) _JSON se trouve dans la section Internet Data Handling ()_

Suivre le lien vous mènera à la page décrivant le fonctionnement du package JSON.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-160.png) _Encodeur et décodeur JSON (https://docs.python.org/3/library/json.html)_

La page ne contient pas seulement du texte, mais aussi des exemples de code pratiques et très utiles.

La documentation officielle sera votre source d'apprentissage la plus fiable et la plus approfondie, donc plus tôt vous vous y habituerez, mieux ce sera.

## Quelle est la suite ?

Comme je l'ai dit, ce texte n'est pas un guide définitif de Python – ce qui signifie qu'il y a encore beaucoup à apprendre. Dans cette section, je vais lister un certain nombre de ressources différentes.

### Programmation Orientée Objet

La première chose que vous voudrez peut-être apprendre juste après avoir terminé ce manuel est la programmation orientée objet avec Python.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ej_02ICOIgs" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

Ce cours vidéo complet est hébergé sur la chaîne YouTube de freeCodeCamp. Il dure un peu plus de 2 heures et couvre joliment les concepts essentiels.

La programmation orientée objet ne consiste pas seulement à apprendre des concepts tels que les classes, les objets et l'héritage.

Écrire un bon code orienté objet demande beaucoup de pratique et tout commence par les bases. Prenez votre temps avec celui-ci et assurez-vous de tout comprendre.

### Algorithmes et structures de données

Le deuxième élément de la liste que vous devriez absolument apprendre si vous voulez sérieusement devenir un programmeur efficace est les structures de données et les algorithmes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8hly31xKli0" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

Heureusement, la chaîne YouTube de freeCodeCamp héberge une vidéo très complète produite par certains des meilleurs enseignants du domaine sur le sujet.

La vidéo dure un peu plus de 5 heures et vous enseignera tout ce que vous devez savoir sur les structures de données et les algorithmes en tant que débutant.

Ce cours ne fera pas de vous un meilleur programmeur instantanément, mais il vous enseignera une façon de penser plus efficace et plus structurée face aux problèmes.

### Django

Si vous souhaitez vous lancer dans le développement web avec Python, Django figure parmi les choix les plus populaires.

<iframe width="560" height="315" src="https://www.youtube.com/embed/o0XbHvKxw7Y" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

La chaîne YouTube de freeCodeCamp héberge ce cours massif de 18 heures enseigné par le Dr Chuck, l'un des meilleurs enseignants au monde.

Le cours n'enseigne pas seulement Django à partir de zéro, mais aussi une longue liste de concepts autour du web lui-même.

Avoir une bonne compréhension de la programmation orientée objet est important avant de vous lancer dans le monde de Django, alors assurez-vous de l'avoir.

### Qt

Python n'est peut-être pas le langage le plus populaire pour créer des interfaces utilisateur graphiques, mais il est étonnamment capable sur ce plan également.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Z1N9JzNax2k" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

Qt est un framework d'interface utilisateur multiplateforme très populaire et PySide6 est le binding Python officiel pour Qt 6.

Dans ce cours de 5 heures, vous apprendrez tous les fondamentaux de la création d'interfaces utilisateur à l'aide de Qt et créerez des logiciels robustes et multiplateformes en un rien de temps.

### PyGame

Tout comme les interfaces utilisateur graphiques multiplateformes, Python n'est pas le choix le plus populaire en matière de programmation de jeux.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R9apl6B_ZgI" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

Cependant, la bibliothèque PyGame est une bibliothèque très puissante et facile à utiliser pour écrire des jeux 2D en Python.

Dans ce cours de près de 7 heures sur la programmation de jeux avec Python, vous apprendrez à écrire un jeu qui imite le très populaire Stardew Valley.

Il s'agit sans aucun doute d'une vidéo très exigeante à suivre, mais la création de jeux l'est tout autant. Donc, si vous aimez le développement de jeux et Python, c'est peut-être le cours qu'il vous faut.

### Data Science

La science des données (Data Science) est sans doute le domaine le plus populaire où Python joue un rôle majeur. Devenir un data scientist peut prendre des années, mais il faut bien commencer quelque part.

<iframe width="560" height="315" src="https://www.youtube.com/embed/LHBE6Q9XlzI" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

Ce cours de 12 heures sur la chaîne YouTube de freeCodeCamp vous apprend beaucoup sur la façon d'utiliser vos connaissances en Python dans la science des données.

Bien que le cours n'aille pas très loin dans le domaine de la science des données, il vous enseigne un certain nombre de bibliothèques très importantes utilisées régulièrement dans ce domaine.

Vers la fin du cours, vous créerez également un projet en appliquant tout ce que vous avez appris tout au long du cours.

## Conclusion

Je tiens à vous remercier du fond du cœur pour le temps que vous avez passé à lire cet article.

Bien que je n'aie listé qu'un petit nombre de cours ici, la [chaîne YouTube de freeCodeCamp][83] regorge d'excellentes ressources d'apprentissage pour Python.

Gardez à l'esprit que ce manuel est un document vivant et que je le mettrai à jour de temps à autre. Le mettre dans vos favoris peut donc être une excellente idée.

J'ai également un blog personnel où j'écris sur divers sujets technologiques, donc si cela vous intéresse, allez voir [https://farhan.dev][84].

Si vous avez des questions ou si vous êtes confus à propos de quoi que ce soit – ou si vous voulez simplement entrer en contact – je suis disponible sur [Twitter][85] et [LinkedIn][86].

[1]: #heading-prerequis
[2]: #heading-comment-installer-python-sur-votre-ordinateur
[3]: #heading-comment-installer-un-ide-python-sur-votre-ordinateur
[4]: #heading-comment-creer-un-nouveau-projet-dans-pycharm
[5]: #heading-comment-ecrire-le-programme-hello-world-en-python
[6]: #heading-comment-initialiser-et-publier-un-depot-git-depuis-pycharm
[7]: #heading-comment-travailler-avec-les-variables-et-les-differents-types-de-donnees-en-python
[8]: #heading-comment-travailler-avec-les-nombres-simples-en-python
[9]: #heading-comment-recuperer-les-entrees-utilisateur-en-python
[10]: #heading-comment-travailler-avec-les-chaines-de-caracteres-en-python
[11]: #heading-quels-sont-les-types-de-sequences-en-python
[12]: #heading-les-listes-en-python
[13]: #heading-les-tuples-en-python
[14]: #heading-les-ranges-en-python
[15]: #heading-comment-fonctionne-l-indexation-en-python
[16]: #heading-quels-sont-les-types-iterables-et-comment-les-utiliser-pour-les-boucles-en-python
[17]: #heading-comment-utiliser-les-boucles-while-en-python
[18]: #heading-comment-ecrire-des-boucles-imbriquees-en-python
[19]: #heading-quelles-sont-les-operations-courantes-sur-les-types-de-sequences-en-python
[20]: #heading-comment-utiliser-l-operateur-in-en-python
[21]: #heading-comment-utiliser-les-operateurs-et-avec-les-types-de-sequences-en-python
[22]: #heading-comment-utiliser-les-fonctions-len-min-et-max-en-python
[23]: #heading-quelles-sont-les-operations-sur-le-type-chaine-de-caracteres-en-python
[24]: #heading-comment-mettre-en-majuscule-des-chaines-de-caracteres-en-python
[25]: #heading-comment-convertir-des-chaines-en-minuscules-ou-en-majuscules-en-python
[26]: #heading-comment-compter-le-nombre-d-occurrences-d-une-sous-chaine-dans-une-chaine-en-python
[27]: #heading-comment-diviser-et-joindre-des-chaines-de-caracteres-en-python
[28]: #heading-comment-ecrire-des-instructions-conditionnelles-en-python
[29]: #heading-quels-sont-les-operateurs-relationnels-et-logiques-en-python
[30]: #heading-quels-sont-les-operateurs-d-affectation-en-python
[31]: #heading-qu-est-ce-que-le-type-set-en-python
[32]: #heading-qu-est-ce-que-le-type-mapping-en-python
[33]: #heading-que-sont-les-objets-de-vue-de-dictionnaire-en-python
[34]: #heading-comment-ecrire-des-fonctions-en-python
[35]: #heading-comment-ecrire-des-fonctions-anonymes-ou-lambda-en-python
[36]: #heading-comment-travailler-avec-les-variables-locales-non-locales-et-globales-en-python
[37]: #heading-comment-passer-un-nombre-variable-d-arguments-a-une-fonction-en-utilisant-args-et-kwargs-en-python
[38]: #heading-que-sont-les-modules-en-python
[39]: #heading-comment-utiliser-efficacement-la-documentation-python
[40]: #heading-quelle-est-la-suite
[41]: #heading-programmation-orientee-objet
[42]: #heading-algorithmes-et-structures-de-donnees
[43]: #heading-django
[44]: #heading-qt
[45]: #heading-pygame
[46]: #heading-data-science
[47]: #heading-conclusion
[48]: https://www.freecodecamp.org/news/author/dillionmegida/
[49]: https://www.freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide/
[50]: https://www.freecodecamp.org/news/author/fahimbinamin/
[51]: https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/
[52]: https://code.visualstudio.com/
[53]: https://www.jetbrains.com/pycharm/
[54]: https://www.freecodecamp.org/news/how-to-configure-visual-studio-code-for-python-development/
[55]: https://www.jetbrains.com/pycharm/buy/
[56]: https://www.jetbrains.com/pycharm/download/
[57]: https://virtualenv.pypa.io/
[58]: https://git-scm.com/
[59]: https://www.freecodecamp.org/news/git-first-time-setup/
[60]: https://www.freecodecamp.org/news/author/bolajiayodeji/
[61]: https://www.toptal.com/developers/gitignore/
[62]: https://peps.python.org/pep-0008/#function-and-variable-names
[63]: https://peps.python.org/pep-0008/#names-to-avoid
[64]: https://www.freecodecamp.org/news/escape-sequences-python/
[65]: https://peps.python.org/pep-0008/#string-quotes
[66]: https://peps.python.org/pep-0008/#string-quotes
[67]: https://www.freecodecamp.org/news/author/dionysia/
[68]: https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/
[69]: https://www.freecodecamp.org/news/author/bala-priya/
[70]: https://www.freecodecamp.org/news/python-range-function-explained-with-code-examples/
[71]: https://docs.python.org/3/library/stdtypes.html#string-methods
[72]: https://docs.python.org/3/library/stdtypes.html#str.title
[73]: https://docs.python.org/3/library/stdtypes.html#str.casefold
[74]: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
[75]: https://www.freecodecamp.org/news/author/kolade/
[76]: https://www.freecodecamp.org/news/author/estefaniacn/
[77]: https://www.freecodecamp.org/news/python-sets-detailed-visual-introduction/
[78]: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
[79]: https://www.freecodecamp.org/news/author/beau/
[80]: https://www.freecodecamp.org/news/how-recursion-works-explained-with-flowcharts-and-a-video-de61f40cb7f9/
[81]: https://docs.python.org/
[82]: https://docs.python.org/
[83]: https://www.youtube.com/c/Freecodecamp/search?query=python
[84]: https://farhan.dev
[85]: https://twitter.com/frhnhsin
[86]: https://www.linkedin.com/in/farhanhasin/