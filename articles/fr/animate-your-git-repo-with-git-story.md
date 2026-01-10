---
title: Comment animer l'historique des commits Git avec git-story
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2022-07-17T17:07:24.000Z'
originalURL: https://freecodecamp.org/news/animate-your-git-repo-with-git-story
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/git-story-image.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment animer l'historique des commits Git avec git-story
seo_desc: 'It is often useful for developers to visualize aspects of their code projects.
  This is especially true for version control systems like Git, where understanding
  the team''s workflow is essential.

  One way to approach this in Git is to draw a graph like...'
---

Il est souvent utile pour les développeurs de visualiser certains aspects de leurs projets de code. Cela est particulièrement vrai pour les systèmes de contrôle de version comme Git, où la compréhension du flux de travail de l'équipe est essentielle.

Une façon d'aborder cela dans Git est de dessiner un graphique comme celui que vous voyez ci-dessus.

Vous avez probablement rencontré des images comme celle-ci lorsque vous [apprenez à utiliser Git](https://initialcommit.com/cluster/git-commands-git-cheat-sheets).

Ce graphique représente un exemple d'historique de commits dans un dépôt Git.

Dans Git, l'historique des commits est représenté sous forme de DAG, ou **Graphe Acyclique Orienté**, qui est un type de graphique de réseau. Chaque commit est affiché sous forme de cercle et les commits sont enchaînés ensemble à l'aide de flèches. Chaque flèche pointe d'un commit enfant vers son parent immédiat.

Pour la plupart, si vous voulez l'un de ces graphiques, vous devez le dessiner vous-même (manuellement ou numériquement) – ce qui prend du temps et des efforts. De plus, ces graphiques sont statiques et il serait plus engageant dans certains cas d'animer la progression des commits dans un format vidéo.

Pour ces raisons, j'ai créé [**Git Story**](https://initialcommit.com/tools/git-story), qui vous permet de générer facilement des vidéos mp4 présentant la disposition et la progression de votre historique de commits Git, le tout avec une seule commande : `git-story`.

## Comment visualiser l'historique des révisions de Git

Dans Git, un commit est également connu sous le nom de révision et représente un ensemble de modifications de contenu faites à un moment spécifique par une personne spécifique.

Il existe plusieurs composants supplémentaires qui nous aident à comprendre visuellement notre historique Git.

### Propriétés des commits

Lors de la validation dans Git, la lisibilité humaine est importante. Par conséquent, il est considéré comme une bonne pratique de laisser un [message de commit](https://initialcommit.com/blog/git-commit-messages-best-practices) clair décrivant votre modification. Cela aide les autres développeurs qui consultent l'historique des commits à comprendre le but de chaque révision.

L'ID de commit est un identifiant unique pour chaque commit, généré spécifiquement à partir du contenu de chaque commit. En tant qu'utilisateur de Git, vous avez probablement vu que de nombreuses commandes Git acceptent un ID de commit complet ou partiel comme argument. Pour cette raison, avoir des ID de commit disponibles dans les visualisations Git peut être très utile.

### Refs : Branches, HEAD et Tags

Lors de la visualisation de l'historique Git, il est également utile de savoir où vous vous trouvez. Les refs Git (abréviation de références) vous aident à comprendre comment les commits sont organisés dans votre dépôt Git.

Les refs sont des étiquettes que Git attache à des commits spécifiques. Les noms de branches, [Git HEAD](https://initialcommit.com/blog/what-is-git-head) et les tags sont tous des exemples de refs dans Git. Vous pouvez considérer une ref comme un nom lisible par l'homme qui pointe vers un commit spécifique.

### Sortie vidéo de Git Story

[**Git Story**](https://initialcommit.com/tools/git-story) analyse toutes ces informations pour vous – commits, relations et refs – et les anime sous forme de vidéo `.mp4`. Le meilleur dans tout cela est que tout ce que vous avez à faire est de naviguer vers votre projet dans le terminal et d'exécuter la commande `git-story`.

Voici un exemple de vidéo d'animation générée par Git Story :

%[https://youtu.be/fI9D-c9wgPs]

## Pourquoi j'ai écrit Git Story en Python

J'ai choisi d'écrire Git Story en Python car il existe deux bibliothèques très utiles qui alimentent ce projet.

### GitPython

La première s'appelle [GitPython](https://gitpython.readthedocs.io/en/stable/intro.html). GitPython est un package Python qui fournit un accès aux données des dépôts Git via un ensemble pratique de méthodes. Voici comment Git Story accède aux données du dépôt Git local afin de les animer :

```python
import git

repo = git.Repo(search_parent_directories=True)
```

Cela crée un objet dépôt dans la mémoire du programme Python qui permet d'accéder aux objets Git sous-jacents et à leurs propriétés. Une liste de commits peut être accessible comme suit :

```python
commits = list(repo.iter_commits(REF))

# Cela extrait une liste de commits en travaillant à rebours depuis REF
# REF peut être un nom de branche, un tag, HEAD ou un ID de commit
```

En itérant à travers la liste des commits, on peut accéder aux propriétés de chaque commit, qui sont utilisées dans l'étape suivante pour générer l'animation.

### Manim

La deuxième dépendance s'appelle [Manim](https://www.manim.community/) qui est utilisée pour générer des vidéos animées de mathématiques en utilisant une API Python. Manim facilite la création d'objets Python qui représentent des lignes, des formes, du texte et des équations, et place ces objets dans une scène animée.

Git Story utilise Manim pour dessiner les cercles, les flèches, le texte, les noms de [branches Git](https://initialcommit.com/blog/git-branches) et les refs qui représentent la portion de votre historique Git obtenue en utilisant GitPython.

Voici comment le code Python utilise Manim pour créer un cercle rouge pour chaque commit :

```python
circle = Circle(stroke_color=commitFill, fill_color=commitFill, fill_opacity=0.25)
```

Et voici comment Manim est utilisé pour créer les flèches entre les commits :

```python
arrow = Arrow(start=RIGHT, end=LEFT, color=self.fontColor).next_to(circle, LEFT, buff=0)
```

Enfin, voici comment ces objets sont ajoutés à une scène animée :

```python
self.play(Create(circle), Create(arrow))
```

## Comment installer Git Story

1. Installez [manim et les dépendances de manim pour votre OS](https://www.manim.community/)

2. Installez GitPython : `$ pip3 install gitpython`

3. Installez git-story : `$ pip3 install git-story`

## Comment utiliser Git Story

1. Ouvrez un terminal en ligne de commande

2. Naviguez jusqu'au dossier racine de votre projet Git en utilisant `cd`

3. Exécutez la commande : `git-story`

L'exécution de cette commande générera une animation vidéo mp4 à partir des 8 derniers commits de votre dépôt Git. Le fichier vidéo sera placé dans le répertoire courant à l'emplacement `./git-story_media/videos`.

## Comment personnaliser la sortie de Git Story

Git Story inclut diverses façons de modifier la manière dont votre dépôt Git est représenté dans la vidéo de sortie. Vous pouvez le faire via des options et des flags en ligne de commande.

Pour spécifier le nombre de commits à animer, utilisez l'option `--commits=X`, où `X` est le nombre de commits que vous souhaitez afficher.

Vous pouvez souhaiter commencer l'animation à partir d'un commit spécifique autre que `HEAD`. Vous pouvez utiliser l'option `--commit-id=ref` pour sélectionner le commit à partir duquel commencer à travailler à rebours. Au lieu de `ref`, vous pouvez substituer un ID de commit complet ou partiel, un nom de branche ou un [tag Git](https://initialcommit.com/blog/git-tag).

Vous pouvez utiliser le flag `--reverse` pour animer les commits du plus récent au plus ancien, c'est-à-dire dans l'ordre chronologique inverse pour correspondre plus étroitement à la sortie du [journal Git](https://initialcommit.com/blog/git-log).

Essayez le flag `--low-quality` pour accélérer le temps de génération de l'animation lors des tests. Une fois que vous êtes satisfait de l'apparence de votre animation, retirez le flag et exécutez à nouveau la commande pour obtenir une version finale de la meilleure qualité.

Si vous préférez un schéma de couleurs clair au lieu du schéma sombre par défaut, vous pouvez spécifier le flag `--light-mode`.

À des fins de présentation, vous pouvez souhaiter ajouter un titre d'introduction, un logo et un générique de fin à votre animation. Vous pouvez le faire avec les options suivantes :

```sh
$ git-story --show-intro --title "Mon Dépôt Git" --show-outro --outro-top-text "Mon Dépôt Git" --outro-bottom-text "Merci d'avoir regardé !" --logo path/to/logo.png
```

Utilisez l'option `--media-dir=path/to/output` pour définir le chemin de sortie de la vidéo. Cela est utile si vous ne souhaitez pas que des fichiers supplémentaires soient créés dans votre projet.

Enfin, vous pouvez souhaiter tester le flag `--invert-branches` si votre historique de commits Git contient plusieurs branches. Ce flag inversera l'ordre dans lequel les branches sont analysées, ce qui modifie l'orientation des branches dans la vidéo de sortie. Certaines animations seront meilleures avec ce flag activé et d'autres non.

Voici un exemple final montrant à quoi ressemble la vidéo générée lorsque plusieurs branches existent dans la plage de commits d'entrée :

%[https://youtu.be/0uj5jRfOaZc]

## Résumé

Git Story est un outil en ligne de commande que j'ai écrit en Python pour faciliter la création d'animations vidéo de votre historique de commits Git. Les dépendances incluent Manim et GitPython.

La vidéo de sortie affiche l'ensemble souhaité de commits et leurs relations, ainsi que les noms de branches, le commit `HEAD` et les tags.

Git Story dispose d'une variété de flags et d'options en ligne de commande qui vous permettent de personnaliser l'animation. Exécutez la commande `git-story -h` pour obtenir la liste complète des options disponibles.

N'hésitez pas à m'envoyer un email à [jacob@initialcommit.io](mailto:jacob@initialcommit.io) pour tout commentaire, question ou suggestion.

Les pull requests sont les bienvenues sur la [page GitHub de Git Story](https://github.com/initialcommit-com/git-story).

Merci d'avoir lu et bon codage !