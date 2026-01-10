---
title: Comment adopter de bonnes habitudes de codage en tant que nouveau développeur
  Python
subtitle: ''
author: Eleanor Hecks
co_authors: []
series: null
date: '2024-08-20T20:46:01.389Z'
originalURL: https://freecodecamp.org/news/how-to-build-good-coding-habits
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724179204764/68fe386c-336f-4f05-9652-bbf5644b5a1b.jpeg
tags:
- name: Python
  slug: python
- name: python beginner
  slug: python-beginner
- name: coding
  slug: coding
- name: '#codingNewbies'
  slug: codingnewbies
seo_title: Comment adopter de bonnes habitudes de codage en tant que nouveau développeur
  Python
seo_desc: 'When you''re starting out as a new Python developer, you''ll likely develop
  some habits, both good and bad.

  Coding is something of an art form. Flexibility and customization are encouraged
  — and you can usually write code how you want within the contex...'
---

Lorsque vous débutez en tant que nouveau développeur Python, vous allez probablement développer certaines habitudes, qu'elles soient bonnes ou mauvaises.

Le codage est en quelque sorte une forme d'art. La flexibilité et la personnalisation sont encouragées — et vous pouvez généralement écrire du code comme vous le souhaitez dans le contexte du langage.

Le problème est que vous communiquez publiquement avec l'ordinateur. Vous devez écrire votre code d'une manière qui ait du sens pour les autres.

De plus, l'utilisation d'une syntaxe incorrecte ou le fait de ne pas s'assurer d'écrire efficacement peut entraîner des erreurs dans votre programmation. Un code désordonné rend extrêmement difficile la recherche de ces erreurs plus tard. Une écriture lisible et propre est la voie à suivre, ce qui signifie prendre de bonnes habitudes de codage dès le début afin de les suivre tout au long de votre carrière.

Voici six conseils pour instaurer de bonnes habitudes de codage alors que vous commencez avec Python.

## **1\. Suivre le guide de style PEP 8**

Les rédacteurs et autres créateurs de contenu utilisent généralement ce qu'on appelle un guide de style. Un guide de style définit des règles concernant le formatage et l'organisation du texte. Il peut expliquer s'il faut utiliser la virgule d'Oxford ou quand utiliser les majuscules dans les titres et d'autres approches structurées.

Python possède un guide de style exactement comme celui-ci, connu sous le nom de PEP 8, PEP8 ou PEP-8. Plusieurs développeurs Python qualifiés ont [publié le guide en 2001](https://peps.python.org/pep-0008/) pour partager la manière d'écrire un code parfaitement lisible et cohérent.

Certains principes incluent :

* L'utilisation de techniques d'indentation appropriées.
    
* Rester en dessous de la longueur maximale de ligne de 79 caractères.
    
* L'utilisation de sauts de ligne.
    
* L'emploi de lignes vides — doubles ou simples — pour les définitions de fonctions, de classes et de méthodes.
    
* L'utilisation de conventions de nommage appropriées pour les variables, les classes, les fonctions, etc.
    

Si vous ne l'avez pas encore fait, lisez le guide de style PEP 8 de Python et assurez-vous de suivre ces techniques.

## **2\. Utiliser la version la plus récente de Python**

Les langages de programmation comme Python passent par de nombreuses itérations au cours de leur cycle de vie. Les anciennes versions sont généralement progressivement supprimées au profit de nouvelles versions. En général, la version la plus récente inclut des corrections de bogues, ainsi que des améliorations de sécurité ou de performance.

Au minimum, utilisez Python 3 plutôt que Python 2, car l'ancienne version [a atteint son statut de fin de vie](https://www.python.org/doc/sunset-python-2/) depuis janvier 2020. De plus, lorsque vous travaillez avec des modules tiers, des Frameworks ou des dépôts, référez-vous toujours à la Version minimale de Python requise. Il s'agit de la version la plus ancienne de Python compatible avec les composants associés.

## **3\. Toujours commenter le code spécifique**

Au moment où vous écrivez votre code, vous savez ce que vous essayez d'accomplir. Lorsque vous relirez ce code plus tard, vous pourriez l'oublier — ou pire encore, si quelqu'un d'autre lit ce code, il pourrait se retrouver perplexe. C'est à cela que servent les commentaires.

Chaque langage a une manière de « commenter » certaines sections de code. L'idée est d'utiliser des commentaires descriptifs mais succincts pour expliquer ce qui se passe. Certains développeurs oublient complètement de le faire, mais si vous commencez tôt et suivez toujours cette règle, vous serez en mesure d'écrire une syntaxe facile à suivre.

En Python, vous utilisez le symbole « # » au début du commentaire pour commenter une ligne. Pour écrire un commentaire sur plusieurs lignes, vous pouvez utiliser des triples guillemets (''') au début ou à la fin, ou plusieurs hashtags par ligne.

`# Ceci est un commentaire normal.`

```python
'''
Ceci est un commentaire multiligne.
Pour expliquer ce que fait le code.
'''
```

Le commentaire peut être une partie vitale du processus de codage car il vous permet de mieux vous souvenir et de visualiser les idées qui vous traversent l'esprit pendant que vous codez.

Selon les experts, écrire vos notes à la main puis les transcrire numériquement par des choses comme les commentaires [améliore votre rétention de 75](https://blog.box.com/best-note-taking-methods) pour cent. Cela signifie que lorsque vous découvrez un bogue ou que vous souhaitez apporter des améliorations plus tard, vous pouvez plus facilement vous rappeler les segments de code pertinents.

Les commentaires en ligne peuvent également apparaître sur la même ligne qu'un point de code. Par exemple :

`print ("Hello World. This is my first code.") # C'est ainsi que vous créez un commentaire en ligne`

## **4\. Utiliser un linter**

Un linter Python examine l'espacement du code, la longueur des lignes et diverses qualifications de conception comme le positionnement des arguments. En conséquence, votre code paraît propre, organisé et écrit de manière cohérente à travers plusieurs fichiers de votre projet.

Gardez à l'esprit qu'un linter est différent d'un auto-formateur ou d'un embellisseur — bien que, dans le codage moderne, le même outil puisse gérer ces deux fonctions de support. Vous pouvez considérer un linter comme quelque chose qui corrige les problèmes pratiques par rapport à un auto-formateur, qui corrige davantage le style.

Les linters peuvent analyser et identifier les erreurs de codage, les bogues potentiels, les fautes d'orthographe ou les problèmes de syntaxe, mais aussi les incohérences stylistiques, telles que la façon dont vous utilisez les indentations et l'espacement. Les auto-formateurs se concentrent sur la partie rédactionnelle ou stylistique de la syntaxe comme les virgules, les guillemets, la longueur de ligne appropriée, etc. Les deux sont utiles, mais vous voudrez rarement coder sans un linter à portée de main.

Certains exemples des meilleurs linters Python incluent Pylint, Flake8, Ruff, Xenon et Radon, entre autres. Le linter utilisé dans la capture d'écran suivante est Ruff, installé via VSCode.

![Python Linter in VSCode with Ruff](https://www.freecodecamp.org/news/content/images/2024/08/Python-Linter-in-VSCode-with-Ruff.jpg align="left")

## **5\. S'appuyer sur les fonctions et bibliothèques intégrées**

La beauté de Python et des langages similaires est que vous ne partez jamais de zéro. Vous n'avez pas à écrire chaque fonction ou réalisation vous-même — au lieu de cela, vous pouvez vous appuyer sur des fonctions intégrées, des bibliothèques, des Frameworks et des dépôts.

Les fonctions intégrées vous font gagner du temps, vous donnent des fonctions prêtes à l'emploi et sont généralement gérées par un groupe de développeurs. Plus important encore, elles augmentent les performances de votre code et de votre logiciel. Vous pouvez [consulter la documentation officielle de Python](https://docs.python.org/3/library/functions.html) pour voir les fonctions intégrées du langage.

Certains exemples incluent :

* `append()`**:** Prend un seul élément et l'ajoute à une liste, modifiant une liste existante en y ajoutant un élément et en augmentant la taille de la liste d'une unité.
    
* `eval()`**:** Évalue toute expression spécifiée comme s'il s'agissait d'une instruction Python officielle.
    
* `id()`**:** Utilisé pour référencer l'identité unique d'un objet ou d'un entier.
    
* `max()`**:** Renvoie la valeur maximale d'un itérable à partir de plusieurs valeurs données.
    
* `print()`**:** Affiche ou renvoie des variables texte dans la console Python.
    
* `round()`**:** Arrondit un nombre ou une valeur à une décimale donnée.
    

En utilisant le tutoriel pour débutant le plus courant, lorsque vous utilisez la fonction `print()`, cela ressemble à ceci :

```python
print("Hello world I am coding.")
```

Cela renverra :

Hello world I am coding

Cette fonction intégrée sera toujours reconnue quel que soit l'IDE ou l'environnement de codage que vous utilisez, ce qui s'applique à toutes les fonctions intégrées, de append() à round().

D'un autre côté, les bibliothèques sont nombreuses et variées — ce sont des collections beaucoup plus vastes de code ou de fonctions pré-écrits. Pour utiliser ou référencer des bibliothèques et leurs fonctions, il vous suffit de les importer dans votre script Python. Des exemples sont Requests, FastAPI, Asyncio, aiohttp, Tkinter, et plus encore.

## **6\. Corriger les problèmes de code dès que possible**

Lors de l'écriture du code, si vous remarquez que quelque chose ne va pas, corrigez-le sur-le-champ. Ne le remettez pas à plus tard et n'attendez pas de faire des tests. Vous pourriez égarer le bogue ou l'erreur — et imaginez si vous ne parvenez pas à le retrouver. Entre [23% et 42% du temps d'un développeur](https://codescene.com/blog/measuring-the-business-impact-of-low-code-quality) est gaspillé à cause d'un mauvais code, ce qui représente un temps précieux que vous pourriez passer ailleurs.

Surtout, les bogues et les erreurs s'accumulent avec le temps, donc plus vous attendez, plus il est probable que des segments entiers de votre code génèrent des erreurs ou cessent de fonctionner. De nombreux IDE et linters peuvent aider dans ce processus, surtout [si vous utilisez le module logging](https://docs.python.org/3/library/logging.html#module-logging) au lieu de simplement afficher les résultats.

Le module logging de Python suit les événements pendant le runtime — lorsqu'un programme est en cours d'exécution. Essentiellement, cela vous permet d'identifier les problèmes ou les erreurs lors du test de votre code. Il peut signaler des avertissements relatifs aux erreurs, au débogage ou aux événements liés au code, mais il peut aussi vous aider à comprendre le comportement au moment de l'exécution de votre projet — toutes choses que vous pourriez négliger pendant le processus d'écriture.

Vous pouvez voir et analyser les interactions des utilisateurs, par exemple, surtout si des utilisateurs externes testent votre application. Plus important encore, le module logging est un outil d'audit inestimable une fois que vous commencez à tester ou à exécuter le code que vous avez écrit. Ne codez pas sans lui.

## **La pratique rend parfait**

Il y a beaucoup de choses à considérer lorsque l'on travaille avec Python, et peu importe votre niveau de compétence ou d'habileté. Suivre les meilleures pratiques de Python est toujours la voie à suivre. Mais en fin de compte, la meilleure façon d'apprendre est toujours d'adopter une approche pratique, ce qui signifie la pratique.

Continuez à utiliser Python, même juste pour créer des projets simples ou petits pour vous-même. Entraînez-vous à utiliser les habitudes discutées ici et à écrire un code propre. Vous devriez également lire le code d'autres développeurs pour voir comment ils abordent le processus.