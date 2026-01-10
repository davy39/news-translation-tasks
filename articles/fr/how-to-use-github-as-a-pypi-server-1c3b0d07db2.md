---
title: Comment utiliser GitHub comme serveur PyPi
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2018-11-15T17:59:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E3Pn3GrE2DBJRBV8r1W__w.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment utiliser GitHub comme serveur PyPi
seo_desc: 'I was looking for a hosted private PyPi Python Package server, that used
  credentials that the team already has (such as GitHub).

  I didn’t want to create an on-premises server. For us, it would make it impossible
  to use cloud-based build servers, and ...'
---

Je cherchais un serveur de packages Python PyPi privé hébergé, utilisant des identifiants que l'équipe possède déjà (comme GitHub).

Je ne voulais pas créer un serveur sur site. Pour nous, cela rendrait impossible l'utilisation de serveurs de build basés sur le cloud, et c'est une autre pièce mobile qui peut mal fonctionner. Il y a aussi des problèmes potentiels avec la sécurité fine et la vitesse. (Nous avons une équipe mondiale, donc servir le contenu via un [CDN](https://www.webopedia.com/TERM/C/CDN.html) serait utile.)

Je ne voulais pas forcer l'équipe à créer des comptes avec un autre fournisseur. Ils ont déjà des comptes Active Directory et GitHub. C'est une nuisance pour eux et cela crée un fardeau de gouvernance pour moi.

Malheureusement, je n'ai pas trouvé un tel service. [GemFury](https://gemfury.com/) est excellent mais ne supporte pas l'autorisation GitHub (au niveau de l'équipe/organisation) et [Packagr](https://www.packagr.app) ne supporte pas du tout l'autorisation GitHub. [MyGet](https://docs.myget.org/) est également excellent, il me permet d'utiliser l'autorisation GitHub, mais n'héberge pas les packages Python. Azure DevOps a quelque chose qui semble prometteur, mais c'est en [bêta privée](https://docs.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages?view=vsts) pour le moment.

Heureusement, cela est possible en utilisant des dépôts Git cloud comme GitHub, GitLab et BitBucket.

### Pip peut installer des packages depuis Git

J'ai hébergé un package Python sur GitHub ([python_world](https://github.com/ceddlyburge/python_world)), que vous pouvez installer avec la commande suivante (assurez-vous de me faire confiance avant d'exécuter cette commande et d'installer mon code sur votre ordinateur).

`pip install git+https://github.com/ceddlyburge/python_world#egg=python_world`

Pip offre des options pour installer depuis head, depuis une branche, depuis une balise ou depuis un commit. Je balise généralement chaque version et installe depuis ces balises. Voir la [documentation de pip install pour plus de détails](https://pip.pypa.io/en/stable/reference/pip_install/#git).

Ce dépôt est public, mais il fonctionne de la même manière avec un dépôt privé, tant que vous avez la permission. Il n'y a pas de magie spéciale (c'est un package Python standard) et [Setup.py](https://github.com/ceddlyburge/python_world/blob/master/setup.py) fait la plupart du travail comme d'habitude.

Si vous êtes nouveau dans la création de packages Python, le [tutoriel Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) vaut le coup d'œil.

### Setuptools peut également installer des dépendances depuis Git

[Setuptools](https://pypi.org/project/setuptools/) est la manière dont la plupart des gens créent des packages Python.

J'ai hébergé un autre package sur GitHub [python_hello](https://github.com/ceddlyburge/python_hello), qui dépend de [python_world](https://github.com/ceddlyburge/python_world). (Je suis sûr que vous voyez où cela mène.)

Les parties pertinentes de setup.py sont ci-dessous. `install_requires` spécifie que `python_world` est une dépendance requise et indique à Setuptools où la trouver.

```python
install_requires=[
	'python_world@git+https://github.com/ceddlyburge/python_world#egg=python_world-0.0.1',
]
```

Vous pouvez installer ce package en utilisant la commande ci-dessous. Il téléchargera également le package dépendant `python_world`.

`pip install git+https://github.com/ceddlyburge/python_hello#egg=python_hello`

Cela lie à une version spécifique de `python_world`, ce qui est dommage car cela signifie que pip ne peut pas faire de gestion de dépendances (comme trouver une version acceptable si plusieurs choses en dépendent). Cependant, à la fin de cet article, nous aurons supprimé le besoin de ce lien spécifique.

### Environnements Python

Comme tout le monde qui a utilisé Python sans environnement le sait, les environnements évitent beaucoup de frustration et de temps perdu. Nous devons donc les supporter.

J'ai créé un dépôt ([use-hello-world](https://github.com/ceddlyburge/python_use_hello_world)) qui définit `python_hello` comme une dépendance dans [requirements.txt](https://github.com/ceddlyburge/python_use_hello_world/blob/master/requirements.txt) pour [Virtualenv](https://virtualenv.pypa.io/), et [environment.yml](https://github.com/ceddlyburge/python_use_hello_world/blob/master/environment.yml) pour [Conda](https://www.anaconda.com).

Si vous téléchargez le dépôt, vous pouvez installer les dépendances dans un virtualenv avec la commande suivante.

`pip install -r requirements.txt`

Si vous utilisez conda, vous pouvez utiliser cette commande :

`conda env create -n use-hello-world`

### Index PyPi

Jusqu'à présent, nous sommes capables d'installer des packages depuis nos dépôts Git privés. Ces packages peuvent, à leur tour, définir des dépendances vers d'autres dépôts privés. Il n'y a toujours pas de serveur PyPi en vue.

Nous pourrions nous arrêter à ce stade. Cependant, la syntaxe pour définir les dépendances est un peu mystérieuse. Il serait difficile pour l'équipe de découvrir quels packages sont disponibles, et nous lions des versions spécifiques de packages dépendants, au lieu de laisser pip les gérer.

Pour résoudre cela, nous pouvons configurer un index PyPi qui respecte [Pep 503](https://www.python.org/dev/peps/pep-0503). Cette spécification est assez simple, et j'ai simplement créé l'index à la main. Si cela devient trop encombrant, je peux le générer à partir de l'API GitHub.

J'ai créé cet [Index PyPi](https://ceddlyburge.github.io/python-package-server/) en utilisant GitHub Pages. Il y a des choses équivalentes pour GitLab et BitBucket. Vous pouvez voir que le [code source](https://github.com/ceddlyburge/python-package-server/) est très simple. Les sites GitHub Pages sont toujours publics (et il n'y a probablement pas d'informations sensibles dans votre index). Cependant, si vous avez besoin qu'ils soient privés, vous pouvez utiliser un service comme [PrivateHub](https://www.privatehub.cloud/).

Une chose à surveiller est la [normalisation des noms](https://www.python.org/dev/peps/pep-0503/#normalized-names) de la spécification. Cela nécessite que les informations du package `python_hello` soient présentes à `python-hello/index.html` (notez le changement de l'underscore en trait d'union).

Maintenant que nous avons un serveur PyPi, nous pouvons installer des packages en utilisant la commande ci-dessous.

`pip install python_hello --extra-index-url [https://ceddlyburge.github.io/python-package-server/](https://ceddlyburge.github.io/python-package-server/)`

Pour que vous puissiez voir cela fonctionner avec des environnements, j'ai créé un autre dépôt ([use_hello_world_from_server](https://github.com/ceddlyburge/python_use_hello_world_from_server)) qui définit la dépendance `python_hello` en utilisant cet index PyPi au lieu de liens directs GitHub. Si vous l'essayez avec Conda, la version >4.4 est requise.

À ce stade, nous pouvons revenir en arrière et supprimer le lien direct Git dans [install_requires dans setup.py de python_hello](https://github.com/ceddlyburge/python_hello_world/blob/master/setup.py) (car Setuptools pourra le trouver depuis notre serveur).

### Conclusions

Utiliser un fournisseur Git hébergé dans le cloud comme serveur PyPi est une option viable. Si vous utilisez déjà un tel service, cela signifie que vous pouvez réutiliser les identifiants et permissions que vous avez déjà. Cela fonctionnera avec les serveurs de build cloud et sera probablement fourni via un CDN, donc rapide dans le monde entier. Cela nécessite plus de connaissances pour être configuré qu'un serveur hébergé, mais probablement les mêmes ou moins que d'héberger votre propre serveur sur site.

### Astuces et conseils

Servir l'index localement peut aider à résoudre les problèmes (comme la normalisation des noms). Il est facile de voir quelles requêtes sont faites. Vous pouvez utiliser le serveur HTTP intégré de Python pour cela (`python -m Http.Server -8000`). Cela m'a conduit à découvrir que `pip search` utilise des requêtes `post`, donc ne fonctionnera pas avec GitHub pages.

Vous pouvez exécuter `python setup.py -install` pour vérifier vos packages pip localement, avant de les pousser vers Git.