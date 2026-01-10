---
title: 'ModuleNotFoundError: no module named ''requests'' [Résolu en Python Django]'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-17T23:55:53.000Z'
originalURL: https://freecodecamp.org/news/python-module-not-found-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Shittu-Olumide-ModuleNotFoundError-no-module-named--requests
seo_title: 'ModuleNotFoundError: no module named ''requests'' [Résolu en Python Django]'
---

Solved-in-Python-Django-.png
tags:
- name: Django
  slug: django
- name: erreur
  slug: erreur
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nLes erreurs sont une partie inévitable de la programmation, et chaque\
  \ programmeur en rencontrera à un moment donné de sa carrière. \nLes erreurs en programmation\
  \ peuvent prendre diverses formes, y compris les erreurs de syntaxe, les erreurs de logique et les erreurs d'exécution,\
  \ et elles..."
---

Par Shittu Olumide

Les erreurs sont une partie inévitable de la programmation, et chaque programmeur en rencontrera à un moment donné de sa carrière. 

Les erreurs en programmation peuvent prendre diverses formes, y compris les erreurs de syntaxe, les erreurs de logique et les erreurs d'exécution, et elles peuvent avoir un impact significatif sur le fonctionnement d'un programme.

Comprendre les différents types d'erreurs en programmation et apprendre à les identifier et à les corriger est essentiel pour écrire un code robuste et fiable. 

À cet égard, divers outils, tels que les débogueurs, les profileurs et les frameworks de test automatisés, peuvent vous aider à détecter et à corriger les erreurs plus efficacement.

Dans ce tutoriel rapide, nous allons examiner une erreur Python spécifique – l'erreur "`ModuleNotFoundError: no module named 'requests'`" – pour voir ce qui la cause et comment la corriger.

## Qu'est-ce que l'erreur `ModuleNotFoundError: no module named 'requests'` en Python ?

L'erreur `ModuleNotFoundError: no module named 'requests'` se produit lorsque vous essayez d'importer le module `requests` dans votre code Python, mais que le module n'est pas installé ou n'est pas disponible dans l'environnement actuel. 

Cette erreur est couramment rencontrée lors de l'utilisation de Python Django car le module `requests` est souvent utilisé pour effectuer des requêtes HTTP dans les applications Django.

## Comment corriger l'erreur `ModuleNotFoundError: no module named 'requests'` en Python

Pour résoudre cette erreur, vous pouvez suivre ces étapes :

Tout d'abord, vérifiez si le module `requests` est installé. Ouvrez un terminal ou une invite de commande et entrez la commande suivante :

```bash
pip freeze | grep requests

```

Cette commande recherchera le module `requests` dans votre environnement et imprimera son numéro de version s'il est installé. Si rien n'est imprimé, cela signifie que le module n'est pas installé.

Si le module `requests` n'est pas installé, vous pouvez l'installer en exécutant la commande suivante dans votre terminal ou invite de commande :

```bash
pip install requests

```

Cette commande téléchargera et installera le module `requests` ainsi que toutes ses dépendances.

Ensuite, vous devrez vérifier si le module `requests` a été importé correctement. Une fois le module `requests` installé, vous pouvez l'importer dans votre code Python en utilisant l'instruction suivante :

```py
import requests

```

Assurez-vous que cette instruction est placée en haut de votre fichier Python avant toute autre instruction utilisant le module `requests`.

Enfin, si vous utilisez le module `requests` dans une application Python Django, vous devrez peut-être redémarrer votre serveur après avoir installé le module pour vous assurer que les modifications prennent effet.

## Conclusion

En suivant ces étapes, vous devriez être en mesure de résoudre l'erreur `ModuleNotFoundError: no module named 'requests'` et d'utiliser le module `requests` dans votre application Python Django.

Et c'est tout !

N'hésitez pas à me contacter sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !