---
title: Comment remplacer Bash par Python comme langage de ligne de commande principal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T18:33:37.000Z'
originalURL: https://freecodecamp.org/news/python-for-system-administration-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9daf740569d1a4ca390c.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Python
  slug: python
seo_title: Comment remplacer Bash par Python comme langage de ligne de commande principal
seo_desc: 'By Jillian Rowe

  I have a bit of a love and hate relationship with bash. I spend a lot of time in
  the terminal, and bash is my default "programming language". Sometimes I tell people
  that find, grep and xargs run their infrastructure, and they laugh a...'
---

Par Jillian Rowe

J'ai une relation un peu amour-haine avec bash. Je passe beaucoup de temps dans le terminal, et bash est mon langage de "programmation" par défaut. Parfois, je dis aux gens que find, grep et xargs font tourner leur infrastructure, et ils rient et rient jusqu'à ce qu'ils réalisent que je suis sérieuse. 

Apprendre un peu de Python est un choix parfait pour les administrateurs système. C'est aussi idéal pour quiconque doit travailler dans un terminal mais ne veut pas utiliser bash, ou a des besoins trop complexes pour bash. Une fois qu'une tâche dépasse

```bash
find $(pwd) -name "*.txt" | xargs -I {} echo "do stuff with {}"
```

il est temps de sortir Python ! 

Il y a beaucoup d'avantages à utiliser Python comme langage de ligne de commande principal. 

* Python dispose de nombreuses bibliothèques utiles pour presque tout. Cela inclut la gestion des opérations système, la lecture de fichiers, la liste des répertoires, l'écriture de boucles for, la vérification des codes de sortie, et bien plus encore.
* L'autocomplétion avec les IDE. Sérieusement. Qui veut devoir mémoriser quoi que ce soit ?
* Une suite de tests robuste si c'est votre truc (et si ce n'est pas le cas, vous devriez envisager de le faire).
* La console iPython. Elle est merveilleuse. Elle est incroyable. **JE L'ADORE.**
* Python est disponible sur la plupart des systèmes, et si ce n'est pas le cas, vous pouvez l'obtenir avec [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
* Vérification robuste des erreurs avec les blocs try et catch.
* Si vous travaillez sur différents systèmes d'exploitation, vous pouvez utiliser des bibliothèques Python qui géreront tout cela sous le capot.
* Même si vous n'avez aucune capacité de programmation, Python est un langage facile à prendre en main.

## Commençons

Pour commencer, vous devrez d'abord avoir Python installé ou l'installer avec Miniconda.

### Vérifiez si vous avez iPython installé

```
which python
which ipython
```

Si les deux commandes réussissent, vous êtes prêt ! Si vous avez Python mais pas iPython, vous devrez l'installer. Vous pourriez l'installer en tant que package système, mais je recommande vraiment de l'installer avec Miniconda.

### Installer Miniconda

Téléchargez l'installateur pour votre système d'exploitation [ici](https://docs.conda.io/en/latest/miniconda.html). Je suggère d'obtenir l'installation Python3. 

Ensuite, c'est une simple installation.

```
bash Miniconda3-latest-Linux-x86_64.sh
```

Suivez les invites et vous aurez Miniconda3 installé. Une fois installé, vous voudrez exécuter une mise à jour, car c'est de la tech et bien sûr vous voulez exécuter une mise à jour. ;-)

```
conda update conda
conda config --add channels conda-forge
conda update -y --all
conda install -y ipython
```

### Dépannage 

Si vous avez des problèmes pour installer des packages, voici quelques conseils.

* Exécutez `conda clean --all` et réessayez.
* Assurez-vous d'utiliser le bon canal.
* Exécutez `conda update -y --all`
* Essayez d'installer le moins possible dans votre espace conda global. Au lieu de cela, créez des environnements pour différentes tâches et projets, ce que nous allons aborder ensuite.

### Créer des environnements avec Conda

Si vous avez déjà utilisé virtualenv, pipenv (est-ce une chose ?), Rbenv, plenv, anyenv ou l'un des autres envs qui ont émergé au fil des ans, cela vous semblera très familier. L'idée est que différents projets doivent avoir leurs propres environnements logiciels isolés.

```
conda create -n mon-projet ipython package1 package2 package2
```

*Si vous êtes comme moi et aimez avoir iPython facilement disponible, assurez-vous de l'installer dans tous les nouveaux environnements !*


## Bibliothèques Python pour l'administration système

Avant de passer aux exemples, listons quelques packages utiles ainsi que leur documentation. 

Mon package de prédilection est le package [os](https://docs.python.org/3/library/os.html). Vous pouvez l'utiliser pour lister des répertoires, vérifier si des fichiers existent, vérifier si des liens symboliques existent, créer des répertoires, exécuter des commandes système, obtenir et définir des variables d'environnement, et bien plus encore. C'est génial !

Mon deuxième package pour exécuter des commandes système qui n'existent pas en tant que bibliothèques Python pratiques est le module [subprocess](https://docs.python.org/3/library/subprocess.html). 

Le module [shutil](https://docs.python.org/3/library/shutil.html) contient des opérations sur les fichiers qui ne sont pas dans la bibliothèque os.

La bibliothèque [pprint](https://docs.python.org/3/library/pprint.html) imprime des structures de données complexes avec une belle indentation.

La bibliothèque [pytest](https://docs.pytest.org/en/latest/) vous permet de tester votre code Python, car soyons réalistes, rien ne fonctionne correctement du premier (few) coup(s). 

## Comment exécuter mon code ?

Enfin ! Du code !

![Screenshot-2019-12-13-10.33.52](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.33.52.png)

Lorsque vous utilisez Python pour l'administration système, vous pouvez plonger directement dans la console iPython, ou écrire des scripts et ensuite les exécuter avec `python nom-du-script.py`. 

Si vous préférez écrire vos scripts, vous avez tant de choix, et c'est vraiment une question de préférence personnelle. J'utilise [PyCharm](https://www.jetbrains.com/pycharm/), qui est payant, mais [Visual Studio Code](https://code.visualstudio.com/) et [Atom](https://atom.io/) sont d'excellents choix gratuits tout aussi excellents. 

Je trouve que cela dépend de ce sur quoi je travaille. Parfois, j'ouvre simplement la console iPython et commence à taper, et d'autres fois, j'ai besoin de quelque chose de plus robuste avec des tests et tout le reste.

Si vous utilisez la console iPython ou l'un des éditeurs que j'ai listés ci-dessus, vous aurez l'autocomplétion. L'autocomplétion est géniale ! Avec iPython, commencez simplement à taper votre fonction et appuyez sur tab pour obtenir une liste de fonctions potentielles que vous pourriez vouloir.

![Screenshot-2019-12-13-10.49.07](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.49.07.png)

Je ne peux pas exprimer à quel point j'aime l'autocomplétion. ;-)

## Obtenir de l'aide

Vous pouvez aller sur n'importe quelle page de documentation pour n'importe quelle bibliothèque, mais si vous connaissez le nom de la bibliothèque ou de la fonction, vous pouvez l'afficher dans iPython.

![Screenshot-2019-12-13-10.55.14](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.55.14.png)

![Screenshot-2019-12-13-10.55.55](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.55.55.png)

Vous pouvez également afficher le menu d'aide dans la plupart des IDE et éditeurs de texte, mais cela sera spécifique à votre éditeur.

## Exemples

Tout d'abord, vous devrez importer vos packages

```
import os
import subprocess
import shutil
from pprint import pprint
```

Voici quelques exemples d'opérations courantes sur les fichiers et répertoires.

```
# Obtenez votre répertoire de travail actuel
# Cela retourne une chaîne de caractères
my_cwd = os.getcwd()
print(my_cwd)
```

```
# Listez le contenu d'un répertoire
# Cela retourne une liste
dir_list = os.listdir()
for item in dir_list:
    print(item)
```

```
# Obtenez le nom de chemin absolu d'un fichier (fichier + répertoire de travail actuel)
os.path.abspath('some-file')
```

```
# Obtenez le nom de base - retourne le fichier
os.path.basename('/path/to/file')
```

```
# Divisez un chemin de répertoire - indépendant de la plateforme
os.path.split(os.getcwd())
# Out[17]: ('/Users', 'jillian')
```

```
# Vérifiez si un chemin existe
os.path.exists('/path/on/filesystem')
```

```
# Vérifiez si un chemin est un lien symbolique
os.path.islink()
```

Déplacez des fichiers et des répertoires

```
# Copiez un répertoire
# cp -rf
shutil.copytree('src', 'dest')
```

```
# Copiez un fichier
# cp -rf
shutil.copyfile('file1', 'file2')
```

```
# Déplacez un répertoire
# mv
shutil.move('src', 'dest')
```

Tout ne sera pas disponible via les bibliothèques Python, comme l'installation de bibliothèques système, alors exécutez quelques commandes système !

```
# Exécutez une commande système arbitraire
command = "echo 'hello'"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Imprimez la sortie stdout et stderr
print(result.stdout)
print(result.stderr)
```

Écrivez dans des fichiers !

```
# Écrivez dans un fichier (et créez-le s'il n'existe pas)
# echo "hello" > hello.txt
f= open("hello.txt","w+")
f.write("hello!")
f.close()
```

```
# Ajoutez à un fichier
# echo "hello" >> hello.txt
f = open("hello.txt", "a+")
f.write("hello again!")
f.close()
```



## Écrivez quelques tests !

Les tests fonctionnent principalement en utilisant une fonction appelée assert, qui dit essentiellement assurez-vous que ceci est vrai et sinon, échouez bruyamment.

```
def test_system_command():
    """Testez le code de sortie d'une commande système"""
    command = "echo 'hello'"
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE)
    assert result.returncode == 0
```

Placez cette fonction dans un fichier appelé `test_my_code.py` et exécutez-le avec `pytest test_my_code.py`.

## Conclusion

C'est tout pour mes principaux conseils et astuces pour utiliser Python comme remplacement de bash. La prochaine fois que vous devrez écrire une boucle en bash, envisagez d'ouvrir la console iPython et voyez ce que vous pouvez faire à la place !