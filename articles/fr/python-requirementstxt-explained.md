---
title: Python Requirements.txt – Comment créer et installer avec Pip les dépendances
  dans Python
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2023-09-11T14:17:18.000Z'
originalURL: https://freecodecamp.org/news/python-requirementstxt-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/pexels-christina-morillo-1181671--1-.jpg
tags:
- name: Python
  slug: python
seo_title: Python Requirements.txt – Comment créer et installer avec Pip les dépendances
  dans Python
seo_desc: 'There are many Python packages we use to solve our coding problems daily.
  Take, for instance, the library "Beautiful Soup," – it doesn''t come with Python
  by default and needs to be installed separately.

  Many projects rely on libraries and other depen...'
---

Il existe de nombreux packages Python que nous utilisons pour résoudre nos problèmes de codage quotidiennement. Prenons, par exemple, la bibliothèque "Beautiful Soup" – elle ne vient pas avec Python par défaut et doit être installée séparément.

De nombreux projets dépendent de bibliothèques et d'autres dépendances, et installer chacune d'entre elles peut être fastidieux et chronophage.

C'est là qu'intervient un fichier 'requirements.txt'. Le fichier requirements.txt est un fichier qui contient une liste de packages ou de bibliothèques nécessaires pour travailler sur un projet, et qui peuvent tous être installés avec ce fichier. Il fournit un environnement cohérent et facilite la collaboration.

## Format d'un fichier requirements.txt

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-219.png align="left")

*Diagramme montrant une boîte contenant requirements.txt et une autre boîte en dessous contenant le texte "package\_name == version"*

L'image ci-dessus montre un exemple de fichier requirements.txt créé, contenant une liste de packages et leurs versions d'installation.

## Termes clés

J'ai mentionné quelques termes que vous ne connaissez peut-être pas. Voici ce qu'ils signifient, ainsi que d'autres termes importants que vous rencontrerez lors de l'utilisation de requirements.txt :

* Les **dépendances** sont des composants logiciels dont un programme a besoin pour fonctionner correctement. Il peut s'agir de bibliothèques, de frameworks ou d'autres programmes.
  
* Les **packages** sont un moyen de regrouper des dépendances liées. Ils facilitent l'installation et la gestion des dépendances.
  
* Les **environnements virtuels** sont un répertoire qui contient une copie de l'interpréteur Python et tous les packages nécessaires à un projet particulier.
  
* **Pip** : il s'agit d'un gestionnaire de packages pour Python. Vous pouvez utiliser Pip pour installer, désinstaller et gérer les packages Python.
  

## Comment créer un fichier requirements.txt

Pour créer un fichier requirements, vous devez configurer votre environnement virtuel. Si vous utilisez Pycharm, un environnement virtuel est déjà configuré (.venv). Mais avec Visual Studio Code, vous devez créer [l'environnement virtuel](https://code.visualstudio.com/docs/python/environments) vous-même.

Vous pouvez utiliser votre terminal ou l'invite de commande pour créer votre fichier requirements. Voici les étapes à suivre pour créer le fichier :

Tout d'abord, ouvrez votre terminal ou votre invite de commande. Ensuite, vérifiez si le chemin du fichier affiché est votre répertoire de travail. Utilisez la commande suivante pour cela :

```python
$ cd folder-name #cd - change directory
```

Dans la commande ci-dessus, remplacez 'folder-name' par le nom du répertoire auquel vous souhaitez accéder.

![Image](https://lh4.googleusercontent.com/vgAz2y8K2iS5wT805qSCN4GhJSv4CDu_eY1_lD_xjetaHhqkNIIvZfCmlVBmBfYYw3PrEYlkq2lasDFsc3YhMtqxZwP4AVn3P70820VeUPdVZxVXU8Cw_UNqPhKnKn3fqpy1sgC5UY4urtfqj4VlYcg align="left")

*Diagramme montrant la définition du répertoire du projet sur la ligne de commande*

Ensuite, exécutez cette commande :

```python
$ pip freeze > requirements.txt
```

Et vous verrez que le fichier requirements est ajouté.

**Voici le résultat :**

![Image](https://www.freecodecamp.org/news/content/images/2023/09/requirementfile.png align="left")

*Diagramme montrant le fichier requirements nouvellement créé*

Et voici votre fichier requirements.txt nouvellement créé :

![Image](https://lh5.googleusercontent.com/1NEE23GJuy_i0qdANdi6twSQGnjfHrjVZ6LuUlENe57kqsMoUve3W0WcmxZLfY9JW04GrYZghVWFtY4_LnVU-isHVxv0ySpMCDQ5sYwhw2BhlQjCLbj2oa_v_nMIUgar2xayjkPRj6ogUARpZEYtKiA align="left")

*Diagramme montrant les listes de packages dans le fichier requirements*

L'image ci-dessus montre les dépendances avec lesquelles vous pouvez travailler, ainsi que leurs versions.

## Comment travailler avec un fichier requirements.txt

Maintenant que nous avons le fichier requirements, vous pouvez voir qu'il se compose d'une longue liste de différents packages.

Pour travailler avec les packages, vous devez les installer. Vous pouvez le faire en utilisant l'invite de commande ou le terminal.

Tapez cette commande :

```python
pip install -r requirements.txt
```

Cela ressemblera à ceci :

![Image](https://lh3.googleusercontent.com/7FDCFqn38aY2GFcoqtrKyy4Oyu_8cAPdJkOxbUIdZTfSalvufWIrbEehT61tgJxuhqiA0nINSfkyHcbE-H-H-hc77rY1zTkMQhyRijtWBOEqcaWZL7fnyNxRDO1hmKcagc9sYI4qijgj6Ut2lVY-zto align="left")

*Image montrant l'installation des packages présents dans le fichier requirements.txt*

Maintenant que toutes les dépendances sont installées, vous pouvez travailler avec requirements.txt.

### Exemple d'utilisation de requirements.txt

Dans cet exemple, nous allons travailler avec deux bibliothèques, `beautifulsoup4` et `requests`, pour retourner certaines informations d'un site.

![Image](https://lh6.googleusercontent.com/M5xLixBqsvL-vtUPFwEZq7NzB-jJDSpycapgv22OxtBKRFa9ysE0kIIPSG0mjltzfknNMdtlPYC8xDWwVnNyGiURQxHFJCrMI_Axexn7dKMRfVN4qUHLt0TEojj_pbLMW-cz_9wlrVw6VOOr8MaD-uQ align="left")

*Diagramme montrant les bibliothèques de travail pour cet exemple dans le fichier requirements*

Dans l'image ci-dessus, nous voyons que les deux bibliothèques sont présentes dans le fichier requirements.txt avec leur version. Maintenant, nous pouvons travailler avec les bibliothèques car nous les avons installées précédemment.

* Importez la bibliothèque BeautifulSoup depuis le package bs4 (beautifulsoup4) et importez également la bibliothèque requests.
  

```python
from bs4 import BeautifulSoup
import requests
```

* Pour récupérer des informations depuis l'URL du site web, nous utilisons la méthode `.get()` pour accéder à la bibliothèque requests.
  

```python
web_data = requests.get("https://www.lithuania.travel/en/category/what-is-lithuania", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
```

* Maintenant que nous avons accès à l'URL, la bibliothèque Beautiful Soup accepte `web_data` et retourne tout le contenu HTML présent.
  

```python
soup = BeautifulSoup(web_data.content, features="html.parser")
```

* Le résultat final que j'ai choisi de retourner est les éléments avec la balise
  
  en première position \[0\].
  

```python
news_info = soup.findAll("p")[0]
print(news_info.text
```

En mettant tout ensemble :

```python
from bs4 import BeautifulSoup
import requests
web_data = requests.get("https://www.lithuania.travel/en/category/what-is-lithuania", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
soup = BeautifulSoup(web_data.content, features="html.parser")
news_info = soup.findAll("p")[0]
print(news_info.text)
```

Et voici le résultat :

![Image](https://lh4.googleusercontent.com/4H_qTUMuvWXNGMKpGrxHfVY6WaEntz51xZ936GwYWY6JRXILVPyd06spEt6emH0XKajK3Ov0qLixzgrqtEC5cIr-81UxyB61fTPPNhGcDc5eEhVoateHzmpAnvowdtbkqJgdz7IlpZ2aGtv9OWLCUCA align="left")

*Diagramme montrant le code et le résultat*

## Avantages de l'utilisation d'un fichier requirements.txt

* Gestion des dépendances : En listant les dépendances de votre projet dans un fichier requirements.txt, vous pouvez facilement voir quels packages sont requis et quelles versions sont nécessaires.
  
* Partage de votre projet avec d'autres : Si vous partagez votre projet avec d'autres, vous pouvez inclure le fichier requirements.txt afin qu'ils puissent facilement installer les packages requis. Cela peut leur faire gagner du temps et éviter des frustrations, et peut aider à garantir que tout le monde utilise les mêmes versions des packages.
  

## Conclusion

Dans cet article, nous avons appris comment créer un fichier requirements.txt et avons souligné les avantages de son utilisation.

Vous devriez également l'essayer et travailler sur quelques projets avec. Si vous avez des questions, vous pouvez me contacter sur [Twitter](https://twitter.com/HeritageAlabi1) 💙.