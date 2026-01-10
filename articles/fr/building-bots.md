---
title: Comment créer un bot et automatiser votre travail quotidien
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T18:36:00.000Z'
originalURL: https://freecodecamp.org/news/building-bots
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/freecodecamp_cover.png
tags:
- name: automation
  slug: automation
- name: bots
  slug: bots
- name: node
  slug: node
- name: Python
  slug: python
- name: social media
  slug: social-media
seo_title: Comment créer un bot et automatiser votre travail quotidien
seo_desc: 'By Tim Grossmann

  Most jobs have repetitive tasks that you can automate, which frees up some of your
  valuable time. This makes automation a key skill to acquire.

  A small group of skilled automation engineers and domain experts may be able to
  automate ...'
---

Par Tim Grossmann

La plupart des emplois comportent des tâches répétitives que vous pouvez automatiser, ce qui libère une partie de votre temps précieux. Cela fait de l'automatisation une compétence clé à acquérir.

Un petit groupe d'ingénieurs en automatisation qualifiés et d'experts du domaine peut être en mesure d'automatiser de nombreuses tâches les plus fastidieuses de toute une équipe.

Dans cet article, nous allons explorer les bases de l'automatisation des flux de travail en utilisant Python – un langage de programmation puissant et facile à apprendre. Nous allons utiliser Python pour écrire un petit script d'automatisation facile et utile qui nettoiera un dossier donné et placera chaque fichier dans son dossier correspondant.

Notre objectif ne sera pas d'écrire du code parfait ou de créer des architectures idéales au début. Nous ne construirons rien d'« illégal » non plus. Au lieu de cela, nous verrons comment créer un script qui nettoie automatiquement un dossier donné et tous ses fichiers.

# Table des matières
1. [Domaines de l'automatisation et par où commencer](#heading-domaines-de-l-automatisation-et-par-ou-commencer)
    - Automatisation simple
    - Automatisation des API publiques
    - Ingénierie inverse des API
1. [Considérations éthiques de l'automatisation](#heading-considerations-ethiques)
1. [Création d'un script de nettoyage de répertoire](#heading-creation-d-un-script-de-nettoyage-de-repertoire)
1. [Un guide complet pour la création de bots et l'automatisation de votre travail quotidien](#heading-un-guide-complet-pour-la-creation-de-bots-et-l-automatisation-de-votre-travail-quotidien)

## Domaines de l'automatisation et par où commencer

Commençons par définir les types d'automatisations qui existent.

L'art de l'automatisation s'applique à la plupart des secteurs. Pour commencer, il aide à des tâches comme l'extraction d'adresses e-mail à partir d'un ensemble de documents afin de pouvoir envoyer un e-mail en masse. Ou des approches plus complexes comme l'optimisation des flux de travail et des processus au sein de grandes entreprises.

Bien sûr, passer de petits scripts personnels à une infrastructure d'automatisation de grande envergure qui remplace des personnes réelles implique un processus d'apprentissage et d'amélioration. Alors voyons par où vous pouvez commencer votre voyage.

### Automatisations simples

Les automatisations simples permettent un point d'entrée rapide et direct. Cela peut couvrir de petits processus indépendants comme le nettoyage de projets et la restructuration de fichiers à l'intérieur de répertoires, ou des parties d'un flux de travail comme le redimensionnement automatique de fichiers déjà enregistrés.

### Automatisations des API publiques

Les automatisations des API publiques sont la forme d'automatisation la plus courante puisque nous pouvons accéder à la plupart des fonctionnalités en utilisant des requêtes HTTP vers des API de nos jours. Par exemple, si vous souhaitez automatiser l'arrosage de votre jardin intelligent fait maison.

Pour cela, vous voulez vérifier la météo du jour en cours pour voir si vous devez arroser ou s'il va pleuvoir.

### Ingénierie inverse des API

L'automatisation basée sur l'ingénierie inverse des API est plus courante dans les bots réels et la section "Bot Imposter" du graphique dans la section "Considérations éthiques" ci-dessous.

En inversant une API, nous comprenons le flux utilisateur des applications. Un exemple pourrait être la connexion à un jeu en ligne dans un navigateur. 

En comprenant le processus de connexion et d'authentification, nous pouvons dupliquer ce comportement avec notre propre script. Ensuite, nous pouvons créer notre propre interface pour travailler avec l'application même si elle ne la fournit pas elle-même.

Quelle que soit l'approche que vous visez, considérez toujours si elle est légale ou non.

Vous ne voulez pas vous mettre dans l'embarras, n'est-ce pas ? ?

## Considérations éthiques

Un gars sur GitHub m'a un jour contacté et m'a dit ceci :

> « Les likes et l'engagement sont une monnaie numérique et vous les dévaluez. »

Cela m'est resté en tête et m'a fait remettre en question l'outil que j'avais construit précisément pour ce but.

Le fait que ces interactions et cet engagement puissent être automatisés et « falsifiés » de plus en plus conduit à un système de médias sociaux déformé et brisé.

Les personnes qui produisent du contenu précieux et de qualité sont invisibles pour les autres utilisateurs et les entreprises de publicité si elles n'utilisent pas de bots et d'autres systèmes d'engagement. 

Un ami a imaginé l'association suivante avec les "Neuf Cercles de l'Enfer" de Dante, où à chaque étape vers le fait de devenir un influenceur social, vous êtes de moins en moins conscient de la manière dont ce système est brisé.

Je veux partager cela avec vous ici car je pense que c'est une représentation extrêmement précise de ce que j'ai observé en travaillant activement avec des influenceurs avec InstaPy.

**Niveau 1 : Limbes** - Si vous n'utilisez pas de bot du tout
**Niveau 2 : Flirt** - Lorsque vous aimez et suivez manuellement autant de personnes que possible pour qu'elles vous suivent en retour / aiment vos publications
**Niveau 3 : Conspiration** - lorsque vous rejoignez un groupe Telegram pour aimer et commenter 10 photos afin que les 10 prochaines personnes aiment et commentent votre photo
**Niveau 4 : Infidélité** - Lorsque vous utilisez un assistant virtuel à bas coût pour aimer et suivre en votre nom
**Niveau 5 : Luxure** - Lorsque vous utilisez un bot pour donner des likes, et ne recevez aucun like en retour (mais vous ne payez pas pour cela - par exemple, une extension Chrome)
**Niveau 6 : Promiscuité** - Lorsque vous utilisez un bot pour donner 50+ likes pour obtenir 50+ likes, mais vous ne payez pas pour cela - par exemple, une extension Chrome
**Niveau 7 : Avarice ou cupidité extrême** - Lorsque vous utilisez un bot pour aimer / suivre / commenter entre 200 et 700 photos, en ignorant le risque de vous faire bannir
**Niveau 8 : Prostitution** - Lorsque vous payez un service tiers inconnu pour qu'il s'engage dans des likes / suivis réciproques automatisés pour vous, mais qu'ils utilisent votre compte pour aimer / suivre en retour
**Niveau 9 : Fraude / Hérésie** - Lorsque vous achetez des followers et des likes et essayez de vous vendre aux marques en tant qu'influenceur

Le niveau de botting sur les réseaux sociaux est si prévalent que **si vous n'utilisez pas de bot, vous serez coincé au Niveau 1, les Limbes**, avec aucune croissance de followers et un faible engagement par rapport à vos pairs.

En théorie économique, cela est connu sous le nom de **dilemme du prisonnier et jeu à somme nulle**. Si je n'utilise pas de bot et que vous en utilisez un, vous gagnez. Si vous n'utilisez pas de bot et que j'en utilise un, je gagne. Si personne n'utilise de bot, tout le monde gagne. Mais comme il n'y a aucune incitation pour que tout le monde n'utilise pas de bot, tout le monde utilise des bots, donc personne ne gagne.

> Soyez conscient de cela et n'oubliez jamais les implications que ces outils ont sur les réseaux sociaux.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/spectrum-bot-intent-ebook.png)
_Source : SignalSciences.com_

Nous voulons éviter de traiter les implications éthiques et travailler tout de même sur un projet d'automatisation ici. C'est pourquoi nous allons créer un simple script de nettoyage de répertoire qui vous aide à organiser vos dossiers désordonnés.

## Création d'un script de nettoyage de répertoire

Nous allons maintenant examiner un script assez simple. Il nettoie automatiquement un répertoire donné en déplaçant ces fichiers dans des dossiers correspondants en fonction de l'extension du fichier.

Donc, tout ce que nous voulons faire est ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/directory_clean_img.png)

### Configuration de l'analyseur d'arguments

Puisque nous travaillons avec des fonctionnalités du système d'exploitation comme le déplacement de fichiers, nous devons importer la bibliothèque `os`. En plus de cela, nous voulons donner à l'utilisateur un certain contrôle sur le dossier à nettoyer. Nous allons utiliser la bibliothèque `argparse` pour cela.

```python
import os
import argparse
```

Après avoir importé les deux bibliothèques, configurons d'abord l'analyseur d'arguments. Assurez-vous de donner une description et un texte d'aide à chaque argument ajouté pour fournir une aide précieuse à l'utilisateur lorsqu'il tape `--help`.

Notre argument s'appellera `--path`. Les doubles tirets devant le nom indiquent à la bibliothèque qu'il s'agit d'un argument optionnel. Par défaut, nous voulons utiliser le répertoire courant, donc définissons la valeur par défaut sur `"."`.

```python
parser = argparse.ArgumentParser(
    description="Nettoyer le répertoire et placer les fichiers dans les dossiers correspondants."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Chemin du répertoire à nettoyer",
)

# analyser les arguments donnés par l'utilisateur et extraire le chemin
args = parser.parse_args()
path = args.path

print(f"Nettoyage du répertoire {path}")
```

Cela termine déjà la section d'analyse des arguments – c'est assez simple et lisible, n'est-ce pas ?

Exécutons notre script et vérifions les erreurs.

```bash
python directory_clean.py --path ./test

=> Nettoyage du répertoire ./test
```

Une fois exécuté, nous pouvons voir le nom du répertoire s'afficher dans la console, parfait. 
Utilisons maintenant la bibliothèque `os` pour obtenir les fichiers du chemin donné.

### Obtenir une liste de fichiers à partir du dossier

En utilisant la méthode `os.listdir(path)` et en lui fournissant un chemin valide, nous obtenons une liste de tous les fichiers et dossiers à l'intérieur de ce répertoire.

Après avoir listé tous les éléments dans le dossier, nous voulons différencier les fichiers et les dossiers puisque nous ne voulons pas nettoyer les dossiers, seulement les fichiers.

Dans ce cas, nous utilisons une compréhension de liste Python pour parcourir tous les éléments et les placer dans les nouvelles listes s'ils répondent à l'exigence donnée d'être un fichier ou un dossier.

```python
# obtenir tous les fichiers du répertoire donné
dir_content = os.listdir(path)

# créer un chemin relatif à partir du chemin vers le fichier et le nom du document
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

# filtrer notre contenu de répertoire dans une liste de documents et de dossiers
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

# compteur pour suivre le nombre de fichiers déplacés
# et liste des dossiers déjà créés pour éviter les créations multiples
moved = 0
created_folders = []

print(f"Nettoyage de {len(docs)} sur {len(dir_content)} éléments.")
```

Comme toujours, assurons-nous que nos utilisateurs reçoivent un retour. Ajoutez donc une instruction d'impression qui donne à l'utilisateur une indication du nombre de fichiers qui seront déplacés.

```bash
python directory_clean.py --path ./test

=> Nettoyage du répertoire ./test
=> Nettoyage de 60 sur 60 éléments.
```

Après avoir réexécuté le script Python, nous pouvons maintenant voir que le dossier `/test` que j'ai créé contient 60 fichiers qui seront déplacés.

### Création d'un dossier pour chaque extension de fichier

L'étape suivante et plus importante consiste maintenant à créer le dossier pour chacune des extensions de fichier. Nous voulons faire cela en parcourant tous nos fichiers filtrés et, s'ils ont une extension pour laquelle il n'y a pas encore de dossier, en créer un.

La bibliothèque `os` nous aide avec d'autres fonctionnalités utiles comme la séparation du type de fichier et du chemin d'un document donné, l'extraction du chemin lui-même et le nom du document.

```python
# parcourir tous les fichiers et les déplacer dans les dossiers correspondants
for doc in docs:
    # séparer le nom de l'extension de fichier
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

	print(filetype)
    print(full_doc_path)
    print(doc_path)
    print(doc_name)
    
    break
```

L'instruction break à la fin du code ci-dessus garantit que notre terminal ne soit pas spammé si notre répertoire contient des dizaines de fichiers.

Une fois que nous avons configuré cela, exécutons notre script pour voir une sortie similaire à celle-ci :

```bash
python directory_clean.py --path ./test

=> ...
=> .pdf
=> ./test/test17
=> ./test
=> test17
```

Nous pouvons maintenant voir que l'implémentation ci-dessus sépare le type de fichier puis extrait les parties du chemin complet.

Puisque nous avons maintenant le type de fichier, nous pouvons vérifier si un dossier avec le nom de ce type existe déjà.

Avant de faire cela, nous voulons nous assurer de sauter quelques fichiers. Si nous utilisons le répertoire courant `"."` comme chemin, nous devons éviter de déplacer le script Python lui-même. Une simple condition if s'en charge.

En plus de cela, nous ne voulons pas déplacer les [fichiers cachés](https://www.lifewire.com/what-is-a-hidden-file-2625898), alors incluons également tous les fichiers qui commencent par un point. Le fichier `.DS_Store` sur macOS est un exemple de fichier caché.

```python
	# sauter ce fichier lorsqu'il est dans le répertoire
    if doc_name == "directory_clean" or doc_name.startswith('.'):
        continue

    # obtenir le nom du sous-dossier et créer le dossier s'il n'existe pas
    subfolder_path = os.path.join(path, filetype[1:].lower())

    if subfolder_path not in folders:
    	# créer le dossier
```

Une fois que nous nous sommes occupés du script Python et des fichiers cachés, nous pouvons maintenant passer à la création des dossiers sur le système.

En plus de notre vérification, si le dossier existait déjà lorsque nous avons lu le contenu du répertoire au début, nous avons besoin d'un moyen de suivre les dossiers que nous avons déjà créés. C'était la raison pour laquelle nous avons déclaré la liste `created_folders = []`. Elle servira de mémoire pour suivre les noms des dossiers.

Pour créer un nouveau dossier, la bibliothèque `os` fournit une méthode appelée `os.mkdir(folder_path)` qui prend un chemin et crée un dossier avec le nom donné à cet endroit.

Cette méthode peut lever une exception, nous indiquant que le dossier existe déjà. Alors assurons-nous également de capturer cette erreur.

```python
if subfolder_path not in folders and subfolder_path not in created_folders:
        try:
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Dossier {subfolder_path} créé.")
        except FileExistsError as err:
            print(f"Le dossier existe déjà à {subfolder_path}... {err}")
```

Après avoir configuré la création de dossiers, réexécutons notre script.

```bash
python directory_clean.py --path ./test

=> ...
=> Dossier ./test/pdf créé.
```

Lors de la première exécution, nous pouvons voir une liste de logs nous indiquant que les dossiers avec les types d'extensions de fichiers donnés ont été créés.

### Déplacement de chaque fichier dans le bon sous-dossier

La dernière étape consiste maintenant à déplacer réellement les fichiers dans leurs nouveaux dossiers parents.

Une chose importante à comprendre lors de l'utilisation des opérations os est que parfois les opérations ne peuvent pas être annulées. C'est, par exemple, le cas avec la suppression. Il est donc logique de simplement logger le comportement que notre script atteindrait si nous l'exécutons.

C'est pourquoi la méthode `os.rename(...)` a été commentée ici.

```python
# obtenir le nouveau chemin du dossier et déplacer le fichier
    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    # os.rename(doc, new_doc_path)
    moved += 1
    
    print(f"Fichier déplacé {doc} vers {new_doc_path}")
```

Après avoir exécuté notre script et vu le logging correct, nous pouvons maintenant supprimer le commentaire avant notre méthode `os.rename()` et lui donner un dernier essai.

```python
# obtenir le nouveau chemin du dossier et déplacer le fichier
    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1

    print(f"Fichier déplacé {doc} vers {new_doc_path}")

print(f"Renommé {moved} sur {len(docs)} fichiers.")
```

```bash
python directory_clean.py --path ./test

=> ...
=> Fichier déplacé ./test/test17.pdf vers ./test/pdf/test17.pdf
=> ...
=> Renommé 60 sur 60 fichiers.
```

Cette exécution finale va maintenant déplacer tous les fichiers dans leurs dossiers appropriés et notre répertoire sera bien nettoyé sans avoir besoin d'actions manuelles.

À l'étape suivante, nous pourrions maintenant utiliser le script que nous avons créé ci-dessus et, par exemple, le planifier pour qu'il s'exécute tous les lundis afin de nettoyer notre dossier de téléchargements pour plus de structure.

**C'est exactement ce que nous créons comme suite à l'intérieur de [notre cours Udemy sur la création de bots et l'automatisation des flux de travail](https://www.udemy.com/course/the-complete-guide-to-bot-creation/).**

## [Un guide complet pour la création de bots et l'automatisation de votre travail quotidien](https://www.udemy.com/course/the-complete-guide-to-bot-creation/)

Felix et moi avons construit un **cours vidéo en ligne pour vous apprendre à créer vos propres bots** basé sur ce que nous avons appris en construisant **InstaPy** et son **Travian-Bot**. En fait, il **a même été forcé de le supprimer car il était trop efficace.**

### [Rejoignez-nous et commencez à apprendre](https://www.udemy.com/course/the-complete-guide-to-bot-creation/).

%[https://youtu.be/zw20WBPjsr0]

Si vous avez des questions ou des commentaires, n'hésitez pas à nous contacter sur [Twitter](https://twitter.com/timigrossmann) ou directement dans la [section de discussion du cours](https://www.udemy.com/course/the-complete-guide-to-bot-creation/) ?