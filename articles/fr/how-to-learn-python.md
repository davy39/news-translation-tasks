---
title: Comment apprendre Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-05-06T17:09:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/brett-jordan-NDjaUqvB7uE-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: learn to code
  slug: learn-to-code
- name: Python
  slug: python
seo_title: Comment apprendre Python
seo_desc: 'With each passing year, the Python programming language becomes more and
  more popular.

  According to the Stack Overflow Developer Survey for 2021, Python was the 3rd most
  popular language, following JavaScript and HTML & CSS.

  And this growth doesn''t s...'
---

Chaque année qui passe, le langage de programmation Python devient de plus en plus populaire.

Selon le [Stack Overflow Developer Survey pour 2021](https://insights.stackoverflow.com/survey/2021#technology), Python était le 3ème langage le plus populaire, après JavaScript et HTML & CSS.

Et cette croissance ne semble pas ralentir de sitôt, donc les programmeurs Python sont très demandés.

Dans cet article, vous verrez pourquoi Python est un excellent premier langage de programmation pour les débutants en codage, et vous apprendrez comment commencer à apprendre ce langage.

Je partagerai une liste de cours utiles que vous pouvez suivre, ainsi que des conseils pour obtenir de l'aide lorsque vous êtes bloqué sur un problème de codage.

Voici ce que nous allons couvrir dans ce guide :

1. [Qu'est-ce que le langage de programmation Python ?](#quest-ce-que-le-langage-de-programmation-python)
    
    1. [Pourquoi apprendre Python ?](#pourquoi-apprendre-python)
        
    2. [Python 2 vs Python 3](#python-2-vs-python-3)
        
    3. [Comment installer Python et configurer un environnement de développement](#comment-installer-python-et-configurer-un-environnement-de-developpement)
        
2. [Cours Python](#cours-python)
    
    1. [Tutoriel de projet Python - Votre premier projet Python](#tutoriel-de-projet-python-votre-premier-projet-python)
        
    2. [Tutoriel Python pour débutants](#tutoriel-python-pour-debutants)
        
    3. [Python pour tous](#python-pour-tous)
        
    4. [Projet de développement de jeu Python utilisant la POO – Tutoriel Minesweeper (avec Tkinter)](#projet-de-developpement-de-jeu-python-utilisant-la-poo-tutoriel-minesweeper-avec-tkinter)
        
    5. [Cours de développement web backend Python (avec Django)](#cours-de-developpement-web-backend-python-avec-django)
        
    6. [Cours de programmation Python intermédiaire](#cours-de-programmation-python-intermediaire)
        
    7. [Introduction à Python en espagnol](#introduction-a-python-en-espagnol)
        
3. [Comment obtenir de l'aide lorsque vous êtes bloqué](#comment-obtenir-de-laide-lorsque-vous-etes-bloque)
    

## Qu'est-ce que le langage de programmation Python ?

Python a été conçu par Guido van Rossum, un programmeur néerlandais, et il a été publié pour la première fois le 20 février 1991.

La Python Software Foundation, une organisation à but non lucratif américaine, est responsable de la promotion, de l'avancement et de la croissance du langage depuis 2001.

Lorsque vous pensez au mot Python, une image de serpent vous vient probablement à l'esprit.

Mais le nom du langage de programmation Python a été inspiré par une série comique de la BBC appelée "Monty Python's Flying Circus", qui était populaire dans les années 1970.

Python est un langage polyvalent, et il est utilisé dans de nombreux domaines du secteur technologique.

C'est un langage populaire lorsqu'il s'agit de travailler avec de grandes quantités de données, donc il est souvent utilisé pour le machine learning et la science des données, ainsi que pour l'analyse et le traitement des données.

C'est également le langage de choix pour le web scraping. Le web scraping est une technique automatisée qui extrait, collecte et traite de grandes quantités de données brutes à partir du web.

Vous pouvez également utiliser Python pour le développement web afin de créer des applications web puissantes avec l'aide de frameworks tels que Django et Flask.

De plus, Python est un langage populaire pour l'automatisation des tests.

Au lieu d'écrire tous les tests pour vos programmes manuellement, vous pouvez compter sur des outils d'automatisation, des bibliothèques Python et des scripts Python pour accomplir le travail.

### Pourquoi choisir d'apprendre Python ?

Lorsque vous commencez à apprendre à coder, vous pouvez rapidement être submergé par le nombre impressionnant de langages de programmation disponibles à apprendre.

Alors, pourquoi choisir d'apprendre Python plutôt qu'un autre langage ?

Tout d'abord, tous les langages de programmation sont des outils, et ils donnent essentiellement des instructions - ils disent à un ordinateur quoi faire et quelles tâches il doit accomplir.

Ils ont tous certains concepts et paradigmes en commun, donc lorsque vous avez une bonne connaissance de l'un, il est plus facile d'en apprendre un autre plus tard.

Cela dit, il y a quelques raisons pour lesquelles Python est un excellent premier langage de programmation pour les nouveaux codeurs.

Tout d'abord, Python est un langage de programmation de script côté serveur de **haut niveau**.

En informatique, il existe deux types de langages de programmation. Il y a les langages de programmation de bas niveau et ceux de haut niveau.

Un langage de programmation de haut niveau signifie qu'il y a beaucoup d'abstraction et de séparation entre le langage et les instructions de niveau machine des ordinateurs qui sont écrites en binaire. Le binaire est un système numérique composé de `1` et de `0`.

Les langages de haut niveau ont une syntaxe qui est beaucoup plus facile à lire, à apprendre, à comprendre et à écrire, car la syntaxe est conviviale et ressemble à la langue anglaise.

La syntaxe de Python est plus concise et moins verbeuse. Vous pouvez accomplir quelque chose en écrivant significativement moins de lignes de code.

Par exemple, voici comment vous écrivez un programme "Hello World" en C++ :

```cpp
#include <iostream>

using namespace std;

int main()
{
   cout<<"Hello World!";

   return 0;
}
```

Et voici comment vous écrivez un programme "Hello World" en Python :

```python
print("Hello World")
```

Il faut moins de lignes pour accomplir la même chose - comme imprimer 'Hello World' sur une console.

Sans parler du fait que c'est beaucoup plus facile à lire et bien plus direct, n'est-ce pas ?

Python est un langage Open Source, ce qui signifie qu'il est utilisable et librement distribué pour tout le monde.

Vous êtes également encouragé à [contribuer](https://github.com/python) et à faire partie d'une grande communauté.

### Python 2 vs Python 3 - Quelles sont les différences ?

Lorsque vous commencez à apprendre Python, vous rencontrerez probablement Python 2 et Python 3 et pourriez être confus quant aux différences entre les deux.

Au fil des ans, Python a évolué en tant que langage.

Il a subi des améliorations constantes, des corrections de bugs et des mises à jour avec de nouvelles fonctionnalités améliorées.

La dernière version de Python 2, Python 2.7, n'est plus maintenue ni supportée. Il n'y aura pas de futures mises à jour, telles que des mises à jour sur les problèmes de sécurité.

Donc, Python 2 est obsolète et n'est plus utilisé.

Lorsque vous commencez à travailler en tant que développeur Python, vous pourriez rencontrer quelques anciennes bases de code avec du code Python 2.

Cependant, cette version du langage ne devrait pas vous préoccuper - surtout en tant que débutant.

Python 3 est la version la plus récente de Python. Il a été créé pour corriger certains problèmes de Python 2.

Les nombreux changements et nouvelles fonctionnalités qu'il a introduits n'étaient pas compatibles avec Python 2.

En programmation, cela est connu sous le nom d'*incompatibilité ascendante*.

Les deux versions ont des différences significatives dans leur syntaxe.

Une différence notable est lorsque vous voulez imprimer quelque chose sur la console :

```python
#print est une instruction en Python 2
print "Hello World"

#print() est une fonction en Python 3
# les parenthèses ont été introduites

print("Hello World")
```

Pour résumer, la norme actuelle maintenable est Python 3, et en cas de doute, c'est la version de Python sur laquelle vous devriez vous concentrer.

### Comment installer Python et configurer un environnement de développement

Vous devrez d'abord installer Python sur votre machine locale.

Plus précisément, vous devrez installer l'interpréteur Python. L'interpréteur Python est un programme logiciel.

Lorsque vous écrivez du code Python dans un fichier avec une extension `.py`, vous avez besoin d'un programme qui traduira votre code Python dans le langage que l'ordinateur comprend.

Ce programme, qui agit comme traducteur, est l'interpréteur Python.

Certains systèmes d'exploitation ont l'interpréteur Python déjà installé par défaut.

Par exemple, sur macOS, la version Python 2.x est installée.

Vous pouvez vérifier cela en ouvrant une nouvelle fenêtre de terminal (entrez le raccourci `Command Space` et tapez Terminal.app. Ensuite, cliquez sur la première option qui apparaît).

Une fois dans le terminal, tapez `python -v`, où l'argument `-v` signifie `version`.

Vous verrez la version 2.x par défaut déjà sur le système.

Cependant, vous ne voulez **pas** utiliser cette version, car elle est obsolète (comme nous l'avons discuté ci-dessus).

Vous pouvez télécharger l'interpréteur Python quel que soit votre système d'exploitation, mais les étapes pour télécharger et installer Python diffèrent d'un système d'exploitation à l'autre.

À ce stade, il est également utile d'apprendre à créer des environnements virtuels en Python.

Cela vous sera utile pour vos futurs projets, surtout lorsque vous travaillez avec des packages tiers.

Les environnements virtuels créent un espace isolé pour chacun de vos projets, ce qui signifie que vous pouvez créer plusieurs environnements virtuels.

Cela garantira que les dépendances des packages installés dans un projet n'interfèrent pas avec le reste de vos projets.

Voici une liste de ressources pour installer Python sur votre machine locale et pour en savoir plus sur les environnements virtuels :

* [Comment installer Python sur Windows](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/)
    
* [Comment installer Python 3 sur Mac et mettre à jour la version avec Pyenv – Guide de commande macOS Homebrew](https://www.freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide/)
    
* [Environnements virtuels Python expliqués avec des exemples](https://www.freecodecamp.org/news/python-virtual-environments-explained-with-examples/)
    
* [Comment configurer un environnement virtuel en Python – Et pourquoi c'est utile](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
    

Plus tôt, j'ai mentionné l'écriture de code Python dans un fichier avec une extension `.py`.

Mais où exactement écrivez-vous le code Python ? Dans un IDE (Environnement de Développement Intégré).

Voici quelques fonctionnalités utiles d'un IDE :

* Un éditeur de code pour écrire et modifier le code source (le code source est un autre terme pour le code écrit dans un langage de programmation lisible par l'homme tel que Python),
    
* La coloration syntaxique (qui rend le code plus facile à lire), les suggestions de code et l'autocomplétion,
    
* Un terminal intégré pour exécuter des commandes,
    
* Des outils de débogage et de test.
    

Essentiellement, un IDE possède tous les outils nécessaires pour augmenter la productivité du programmeur, tout sous le même toit, et [il existe de nombreux IDE pour écrire du code Python parmi lesquels choisir](https://www.freecodecamp.org/news/python-ide-best-ides-and-editors-for-python/).

Personnellement, lorsque j'ai commencé à apprendre Python, j'ai trouvé que l'écriture de code Python dans Visual Studio Code était une expérience agréable.

Visual Studio Code est un éditeur de code gratuit et open-source avec des fonctionnalités puissantes similaires à un IDE et offre un support pour l'utilisation de Python. [Vous pouvez en savoir plus sur la prise en main de l'écriture de Python dans Visual Studio Code en lisant la documentation utile](https://code.visualstudio.com/docs/python/python-tutorial)

## Cours Python

La mission de freeCodeCamp est de créer des ressources éducatives de haute qualité pour les personnes du monde entier, gratuitement.

Sur la [chaîne YouTube de freeCodeCamp](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ), vous trouverez des milliers d'heures de contenu éducatif sur une variété de sujets de programmation.

Voici quelques suggestions de cours vidéo pour vous aider à commencer à apprendre Python en tant que débutant complet.

### Tutoriel de projet Python - Votre premier projet Python

[Ce cours vidéo d'une heure](https://www.youtube.com/watch?v=_ZqAVck-WeM), créé par Tech with Tim, est idéal pour créer votre tout premier projet Python et apprendre les bases du langage.

Apprendre en construisant des jeux est une manière amusante de comprendre les concepts fondamentaux.

Dans ce cours, vous n'avez pas besoin d'avoir un environnement configuré, car il utilise [Repl.it](http://repl.it/), un éditeur dans le navigateur, donc vous pouvez commencer à coder immédiatement.

### Tutoriel Python pour débutants

[Dans ce cours de 3 heures](https://www.youtube.com/watch?v=8124kv-632k) créé par Bobby Stearman, un ingénieur logiciel senior, vous apprendrez les bases de Python.

Ce cours ne suppose aucune connaissance préalable, car il vous guide à travers l'installation et la configuration d'un processus pour écrire du Python et créer des environnements virtuels localement sur votre machine.

Vous apprendrez également les types de données de base de Python, tels que les chaînes de caractères et les nombres, puis passerez à des types plus avancés, tels que les tuples, les dictionnaires et les ensembles, pour n'en nommer que quelques-uns des sujets couverts.

### Python pour tous

[Ceci est un cours de 14 heures](https://www.youtube.com/watch?v=8DvywoWv6fI) créé par Dr. Chuck, un professeur clinique à l'Université du Michigan School of Information.

Dans ce cours, vous apprendrez les bases absolues de Python et des sujets plus avancés tels que la POO (abréviation de Programmation Orientée Objet).

freeCodeCamp propose également ce cours comme l'une de ses certifications disponibles.

Dans la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/), le cours vidéo ci-dessus est divisé en sections plus petites.

Chaque section contient une vidéo avec des matériaux à suivre et des exercices à compléter.

Après avoir regardé la vidéo, il y a une question à choix multiples à répondre.

![https://www.freecodecamp.orghttps://www.freecodecamp.orghttps://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-05-at-12.08.13-PM.png](/news/content/images/2022/05/Screenshot-2022-05-05-at-12.08.13-PM.png align="left")

C'est une excellente façon de pratiquer le [Rappel Actif](https://www.youtube.com/watch?v=ukLnPbIffxE), une technique d'étude et d'apprentissage efficace.

Pour pratiquer le Rappel Actif, vous lisez ou regardez quelque chose et une fois que vous avez terminé de lire/regarder, vous récupérez les concepts clés que vous avez appris - vous vous testez essentiellement sur les informations que vous venez de consommer.

La [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) comprend également 5 projets pratiques à compléter, où vous pouvez consolider vos connaissances en mettant vos nouvelles compétences en pratique.

### Projet de développement de jeu Python utilisant la POO – Tutoriel Minesweeper (avec Tkinter)

[Dans ce cours de 3 heures](https://www.youtube.com/watch?v=OqbGRZx4xUc) créé par Jim de JimShapedCoding, vous construirez un jeu Démineur en utilisant la bibliothèque tkinter.

Ce cours est parfait pour vous une fois que vous avez compris les bases de Python et que vous souhaitez construire un projet qui implémente la Programmation Orientée Objet.

### Cours de développement web backend Python (avec Django)

Plus tôt, j'ai mentionné que Python est un choix populaire pour le développement web, avec l'aide du framework web Django.

[Dans ce cours de 10 heures](https://www.youtube.com/watch?v=jBzwzrDvZ18) créé par Tomi Tokko, en plus d'apprendre les bases de Python, vous apprendrez également comment créer des applications web en utilisant Python avec Django.

### Cours de programmation Python intermédiaire

Une fois que vous avez maîtrisé les bases des cours précédents et construit quelques projets simples, vous ne savez peut-être pas comment avancer et construire sur vos compétences déjà existantes.

[Dans ce cours de 6 heures](https://www.youtube.com/watch?v=HGOBQPFzWKo) créé par Patrick Loeber, vous plongerez plus profondément dans le langage de programmation Python et aborderez des sujets tels que les fonctions Lambda, le Multithreading, le Multiprocessing, et les Exceptions et Erreurs, pour n'en nommer que quelques-uns.

### Introduction à Python en espagnol

Enfin, si vous êtes hispanophone, ou si vous avez un ami/un membre de la famille qui est hispanophone et souhaite apprendre Python, ce cours est idéal pour apprendre Python en espagnol.

[Ceci est un cours vidéo](https://www.youtube.com/watch?v=DLikpfc64cA) créé par Estefania Cassingena Navone, une membre du personnel de freeCodeCamp, et dure plus de 4 heures.

Vous apprendrez les bases absolues avec l'aide de visuels détaillés et d'explications approfondies.

## Comment obtenir de l'aide lorsque vous êtes bloqué

Lorsque vous êtes un codeur débutant, vous rencontrerez inévitablement des défis et des obstacles sur votre parcours d'apprentissage.

Lorsque vous vous trouvez dans une telle situation, la meilleure façon de vous en sortir est de vous appuyer sur une communauté.

Le [forum freeCodeCamp](https://forum.freecodecamp.org/) est une communauté bienveillante et amicale qui vous aidera à vous débloquer.

Par exemple, si quelque chose ne vous a pas été clair dans l'une des vidéos YouTube de freeCodeCamp, ou si vous êtes bloqué à une étape de la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/), n'hésitez pas à poser une question.

Avant de le faire, assurez-vous d'[apprendre à poser de bonnes questions sur le forum](https://www.freecodecamp.org/news/how-to-ask-a-question-on-a-forum/) pour vous assurer de poser la bonne question qui vous aidera à résoudre le problème auquel vous êtes confronté.

De plus, le forum est un excellent endroit pour interagir avec d'autres développeurs. Il peut vous aider à commencer à construire votre réseau et à rester motivé en lisant des histoires inspirantes des membres de la communauté qui ont appris à coder en utilisant freeCodeCamp et ont obtenu de superbes emplois de développeurs.

Enfin, lorsque vous souhaitez comprendre davantage et approfondir un sujet spécifique en apprenant Python, vous pouvez compter sur la [publication freeCodeCamp](https://www.freecodecamp.org/news/).

Il y a plus de 8000 articles approfondis sur des sujets de programmation et de technologie écrits par la communauté.

Donc, disons que vous apprenez les listes Python mais que vous ne comprenez pas tout à fait la méthode `.append()`.

Lorsque vous utilisez la version web, vous verrez une barre de recherche en haut à gauche.

Vous pouvez alors taper `.append() python`, et vous verrez plusieurs résultats d'articles qui vous aideront à en savoir plus.

## Conclusion

Cela marque la fin de l'article – merci beaucoup d'être arrivé jusqu'au bout !

Espérons que ce guide a été utile et qu'il vous a donné un aperçu non seulement des raisons pour lesquelles vous devriez envisager d'apprendre Python, mais aussi de la manière d'apprendre ce langage en 2022 et au-delà.

Bon codage !