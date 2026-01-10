---
title: Qu'y a-t-il dans un __name__ (de Python) ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T16:27:28.000Z'
originalURL: https://freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zv8ZOTI8T_hmrYXG
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Qu'y a-t-il dans un __name__ (de Python) ?
seo_desc: 'By Bert Carremans

  An introduction to the _ name _ variable and its usage in Python

  You’ve most likely seen the __name__ variable when you’ve gone through Python code.
  Below you see an example code snippet of how it may look:

  if __name__ == ''__main__''...'
---

Par Bert Carremans

#### Une introduction à la variable _ _name_ _ et son utilisation en Python

Vous avez probablement vu la variable `__name__` lorsque vous avez parcouru du code Python. Ci-dessous, vous voyez un exemple de code montrant à quoi cela peut ressembler :

```
if __name__ == '__main__':    main()
```

Dans cet article, je veux vous montrer comment vous pouvez utiliser cette variable pour créer des modules en Python.

#### Pourquoi la variable _ _name_ _ est-elle utilisée ?

La variable `__name__` (avec deux underscores avant et après) est une variable spéciale en Python. Elle obtient sa valeur en fonction de la manière dont nous exécutons le script contenant.

Parfois, vous écrivez un script avec des fonctions qui pourraient être utiles dans d'autres scripts également. En Python, vous pouvez importer ce script en tant que module dans un autre script.

Grâce à cette variable spéciale, vous pouvez décider si vous souhaitez exécuter le script ou si vous souhaitez importer les fonctions définies dans le script.

#### Quelles valeurs la variable __name__ peut-elle contenir ?

Lorsque vous exécutez votre script, la variable `__name__` est égale à `__main__`. Lorsque vous importez le script contenant, il contiendra le nom du script.

Examinons ces deux cas d'utilisation et décrivons le processus avec deux illustrations.

#### Scénario 1 - Exécuter le script

Supposons que nous avons écrit le script `nameScript.py` comme suit :

```
def myFunction():    print 'La valeur de __name__ est ' + __name__
```

```
def main():    myFunction()
```

```
if __name__ == '__main__':    main()
```

Si vous exécutez nameScript.py, le processus suivant est suivi.

![Image](https://cdn-media-1.freecodecamp.org/images/PljpjxnM1OMMW7IkexNxVfwrKhP0RH-isapH)

Avant que tout autre code ne soit exécuté, la variable `__name__` est définie sur __main__. Après cela, les instructions de définition `main` et `myFunction` sont exécutées. Parce que la condition évalue à vrai, la fonction main est appelée. Cela, à son tour, appelle myFunction. Cela imprime la valeur de `__main__`.

#### Scénario 2 - Importer le script dans un autre script

Si nous voulons réutiliser myFunction dans un autre script, par exemple `importingScript.py`, nous pouvons importer `nameScript.py` en tant que module.

Le code dans `importingScript.py` pourrait être comme suit :

```
import nameScript as ns
```

```
ns.myFunction()
```

Nous avons alors deux portées : une de `importingScript` et la deuxième portée de `nameScript`. Dans l'illustration, vous verrez comment cela diffère du premier cas d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/k9OxzvJAP-s5qeZg88jUCOCVy1syrQu4oKds)

Dans importingScript.py, la variable `__name__` est définie sur __main__. En important nameScript, Python commence à chercher un fichier en ajoutant `.py` au nom du module. Il exécute ensuite le code contenu dans le fichier importé.

Mais cette fois, elle est définie sur nameScript. Encore une fois, les instructions de définition pour main et myFunction sont exécutées. Mais, maintenant la condition évalue à faux et main n'est pas appelée.

Dans importingScript.py, nous appelons myFunction qui sort nameScript. NameScript est connu de myFunction lorsque cette fonction a été définie.

Si vous imprimiez `__name__` dans importingScript, cela donnerait `__main__`. La raison en est que Python utilise la valeur connue dans la portée de importingScript.

#### Conclusion

Dans cet article court, j'ai expliqué comment vous pouvez utiliser la variable `__name__` pour écrire des modules. Vous pouvez également exécuter ces modules de manière autonome. Cela peut être fait en utilisant la manière dont les valeurs de ces variables changent en fonction de l'endroit où elles se produisent.