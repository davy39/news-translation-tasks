---
title: pip Command Not Found – Erreur Mac et Linux Résolue
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-03T18:14:36.000Z'
originalURL: https://freecodecamp.org/news/pip-command-not-found-mac-and-linux-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pip.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: pip Command Not Found – Erreur Mac et Linux Résolue
seo_desc: "When using Python, you might need to install and use certain packages.\
  \ And there is a command available for that known as 'pip'. \nWith pip, you can\
  \ install, upgrade, and uninstall various Python packages. You'll learn how to use\
  \ it, and how to handle..."
---

Lorsque vous utilisez Python, vous pourriez avoir besoin d'installer et d'utiliser certains packages. Et il existe une commande pour cela connue sous le nom de 'pip'.

Avec pip, vous pouvez installer, mettre à jour et désinstaller divers packages Python. Vous apprendrez comment l'utiliser et comment gérer les erreurs pip dans cet article.

## Comment utiliser pip

Pip est une commande que vous pouvez utiliser sur la ligne de commande Linux ou Mac. Vous pouvez sélectionner un package à partir [d'ici](https://pypi.org/).

Voici un exemple de la façon dont vous installeriez le package `mock-open` avec `pip`.

```python
pip3 install mock-open
```

Sortie:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image.png)

Comme ce package était déjà installé, nous recevons le message indiquant que la condition est déjà remplie.

Notez que j'ai utilisé pip3 car j'utilise Python3. Nous en discuterons en détail plus tard.

## Qu'est-ce que l'erreur `pip: command not found`?

Parfois, lors de l'installation de packages, vous pourriez rencontrer l'erreur: **`pip: command not found`**. Cette erreur pourrait être due aux raisons suivantes:

1. Pip n'est pas installé.
2. Pip est installé, mais il n'est pas compatible avec l'environnement actuel.

Sur Linux, vous devez installer le gestionnaire de packages pip séparément car il s'agit d'un package indépendant. Mais sur Mac, vous n'avez pas besoin d'installer pip manuellement, tant que vous travaillez avec Python 3.x.

### Dépannage de l'erreur **`pip: command not found`**

1. **Vérifiez si pip est installé.**

Sur Mac et Linux, vous pouvez utiliser la commande suivante pour vérifier si pip est installé.

```
 python3 -m pip --version 
```

![pip installé](https://www.freecodecamp.org/news/content/images/2022/03/image-1.png)
_Ici, la sortie si pip est installé correctement_

Si pip n'est pas installé, vous pouvez suivre les étapes d'installation [ici](https://pip.pypa.io/en/stable/installation/) pour votre système d'exploitation respectif.

**2. Mettez à jour pip vers la dernière version**

Si pip ne fonctionne toujours pas, essayez de le mettre à jour vers la dernière version:

```
python -m pip install --upgrade pip
```

![Sortie après la mise à jour de pip](https://www.freecodecamp.org/news/content/images/2022/03/image-2.png)
_Sortie après la mise à jour de pip_

**3. Corriger les problèmes d'environnement**

Il est possible que vous essayiez d'utiliser la mauvaise version de pip. Par exemple, `pip3` fonctionne pour `Python3`, tandis que `pip` fonctionne uniquement pour `Python2`.

Vous pouvez vérifier votre version de Python sur Linux et Mac comme ceci:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-3.png)
_Je suis en train d'utiliser Python3_

Si votre code est en Python 2 et que vous souhaitez toujours utiliser une ancienne version de pip, vous pouvez suivre les étapes ci-dessous.

Notez que Python 2 a atteint sa fin de vie. Il est préférable de mettre à jour votre base de code vers Python 3 et d'utiliser la dernière version de pip.

Suivez les étapes ci-dessous uniquement si vous utilisez Python2:

1. Installer pip (ancienne version)

```
sudo easy_install pip
```

Cette commande installe la commande pip sur votre système.

Maintenant, essayez d'utiliser la commande pip – elle devrait fonctionner sans erreurs.

## Conclusion

Pip est une commande utile pour installer des packages Python. Nous avons couvert certaines méthodes de dépannage pour l'erreur **`pip: command not found`**.

J'espère que vous avez trouvé ce tutoriel utile.

Connectons-nous sur [Twitter](https://twitter.com/hira_zaira)!

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).