---
title: Comment utiliser Google Colab avec VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-09T22:24:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-google-colab-with-vs-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/1_6glvkHvmHFc9JjcExBB3-w.jpeg
tags:
- name: Google Colab
  slug: google-colab
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Comment utiliser Google Colab avec VS Code
seo_desc: 'By Davis David

  Google Colab and VS Code are two popular editor tools that many Python developers
  use. They''re great for developing efficient tech solutions or systems especially
  in the areas of Machine Learning and Data Science.

  If you''re a Python de...'
---

Par Davis David

Google Colab et VS Code sont deux outils d'édition populaires que de nombreux développeurs Python utilisent. Ils sont excellents pour développer des solutions technologiques efficaces ou des systèmes, notamment dans les domaines de l'apprentissage automatique et de la science des données.

Si vous êtes un développeur Python ou un scientifique des données, vous savez peut-être déjà comment utiliser Google Colab. Mais saviez-vous que vous pouvez configurer VS Code sur Google Colab et l'utiliser comme éditeur de la même manière que sur votre machine locale ?

**Dans cet article, vous apprendrez :**

1. Comment installer le package Python colabcode.
2. Comment démarrer VS Code (code server).
3. Comment accéder à VS Code en ligne.
4. Comment ouvrir le terminal.
5. Comment exécuter un fichier Python.

## Comment utiliser Google Colab avec VS Code

### Ouvrir un notebook Colab

La première étape consiste à lancer un nouveau notebook Colab dans votre Google Colab. Vous pouvez renommer le fichier comme vous le souhaitez.

Par exemple, `run_vscode.ipynb`.

### Installer le package Python colabcode.

Pour utiliser Google Colab avec VS Code (code server), vous devez installer le package Python colabcode. Il s'agit d'un package Python open-source développé par [Abhishek Thakur](https://github.com/abhishekkrthakur).

Pour installer le package, exécutez la commande suivante dans une cellule de votre notebook :

```
!pip install colabcode
```

### Importer ColabCode

L'étape suivante consiste à importer la classe ColabCode depuis le package.

```python
from colabcode import ColabCode
```

### Créer une instance de ColabCode

Après avoir importé ColabCode, vous devez créer une instance de ColabCode et définir les arguments suivants :

* **port** – Le port sur lequel vous souhaitez exécuter le code-server. Par exemple, port=10000
* **password** – Vous pouvez définir un mot de passe pour protéger votre code-server contre les accès non autorisés. Il s'agit d'un argument optionnel.
* **mount_drive** – Si vous souhaitez utiliser votre Google Drive. Il s'agit d'un argument booléen, ce qui signifie que vous pouvez le définir sur True ou False. Il s'agit d'un argument optionnel.

```python
ColabCode(port=10000)
```

### Démarrer le serveur de code

Après avoir exécuté l'instance ColabCode, elle démarrera le serveur et affichera le lien pour accéder au serveur de code.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_2j1llmzWvkrJ1QcDX4TyKw.jpeg)

Vous devez cliquer sur le lien et il s'ouvrira dans un nouvel onglet.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_8WOTEo4531S7KEoE9qsocA.jpeg)

Maintenant, vous pouvez profiter d'un éditeur de code complet et effectuer différentes expériences sur la machine virtuelle Colab.

**Note :** Si vous vérifiez votre notebook Colab, vous verrez que la cellule qui exécute l'instance ColabCode est en cours d'exécution en continu. Ne fermez pas votre notebook Colab sauf si vous souhaitez fermer le serveur de code qui exécute VS Code.

## Conseils pour utiliser VS Code sur Google Colab

Après avoir lancé le serveur de code, utilisez les conseils suivants pour vous aider à commencer à utiliser VS Code sur Google Colab.

### Étape 1 : Ouvrir le terminal

Pour ouvrir le terminal sur VS Code qui s'exécute sur Google Colab, utilisez la commande de raccourci suivante :

```command
Ctrl + Shift + `
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_LdynqUTdluFY53C3DwIfdg.jpeg)

### Étape 2 : Changer le thème si vous le souhaitez

Vous pouvez changer le thème de l'éditeur en cliquant sur l'icône de paramètres (coin inférieur gauche) puis en cliquant sur "Color Theme". Une fenêtre contextuelle s'ouvrira avec différentes options de thème que vous pouvez sélectionner.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_oRbVQGlo1juU6yh4ylOIwQ.jpeg)

### Étape 3 : Exécuter un fichier Python

Vous pouvez créer un fichier Python en cliquant sur la section **"File"** dans la barre latérale, puis en sélectionnant l'onglet **"New File"**.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_8YC-QStbIB9sdzh3gV5krg-1.jpeg)

Dans l'exemple suivant, vous verrez comment exécuter un simple fichier Python qui entraîne un algorithme d'apprentissage automatique pour classer les fleurs d'iris en trois espèces (setosa, versicolor ou virginica) puis faire une prédiction.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/1_C21tD_JDFE6dh559nCmZ0Q-1.jpeg)

## Réflexions finales sur l'utilisation de Google Colab avec VS Code

Félicitations 👏👏, vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau. Vous pouvez configurer VS Code sur Google Colab et passer votre codage au niveau supérieur.

Vous pouvez également utiliser le package Python colabcode sur la plateforme **Kaggle** pour exécuter VS Code. Vous devez simplement suivre les mêmes étapes mentionnées ci-dessus.

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).

Et vous pouvez lire plus d'articles comme celui-ci [ici](https://hackernoon.com/u/davisdavid).