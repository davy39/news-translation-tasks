---
title: Comment sortir de l'enfer des fonctions AWS Lambda grâce à la puissance de
  Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-17T21:58:27.000Z'
originalURL: https://freecodecamp.org/news/escaping-lambda-function-hell-using-docker-40b187ec1e48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HlfWIN7pNtK3ffZ-ll1cZQ.png
tags:
- name: Alexa
  slug: alexa
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: Comment sortir de l'enfer des fonctions AWS Lambda grâce à la puissance
  de Docker
seo_desc: 'By Liz Rice

  When you’re building Lambda functions, it’s easy to get trapped in an “Invalid ELF
  header” nightmare. The problem is that your binaries are built for the wrong platform.
  Here’s what’s going on, and how you can fix it easily using Docker.

  ...'
---

Par Liz Rice

Lorsque vous construisez des fonctions Lambda, il est facile de se retrouver piégé dans un cauchemar d'en-tête ELF invalide. Le problème est que vos binaires sont construits pour la mauvaise plateforme. Voici ce qui se passe et comment vous pouvez le corriger facilement en utilisant Docker.

Lorsque la plupart des gens commencent avec les fonctions Lambda, ils utilisent l'éditeur en ligne dans la console pour saisir leur code. Cela convient pour vos premiers exemples, mais très vite, vous voudrez faire quelque chose de plus complexe, comme, vous savez, importer une bibliothèque.

Au cours des derniers week-ends, j'ai travaillé sur [ma première compétence Alexa pour un Amazon Echo](https://hackernoon.com/my-first-alexa-custom-skill-6a198d385c84#.qfxjk23ov) et j'ai atteint le point où je veux utiliser du code tiers pour ajouter des fonctionnalités supplémentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/vktAeFvMs7ITPSm0PgNVUG6EWPSvDRoG7Xfu)
_Vos options pour fournir le code de votre fonction Lambda, comme vu dans la console AWS_

L'éditeur en ligne vous permet simplement de modifier un seul fichier. Si vous souhaitez faire référence à d'autres fichiers — y compris les bibliothèques importées — vous pouvez les télécharger dans un fichier ZIP (Amazon appelle cela un [package de déploiement](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)). Mais si vous travaillez sur un Mac ou un PC Windows, il y a un piège.

Lorsque vous utilisez pip pour installer des bibliothèques Python sur votre ordinateur portable, il vous donne des binaires (fichiers .so) qui sont construits pour fonctionner sur votre machine. Mais lorsque la fonction Lambda s'exécute dans le cloud AWS, elle s'exécutera sur Linux — et les binaires construits pour Mac (souvent appelés builds 'darwin') ou Windows ne s'exécuteront pas sur Linux (et vice versa).

Si vous téléchargez la version Mac, vous verrez des journaux invalid ELF header lorsque vous essayez de tester votre fonction Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/q0v1xD6yQw0OfdQsiZVo3Fgzlm1jTvAzNUqA)
_Invalid ELF header indique qu'il s'agit du mauvais format binaire pour la plateforme_

Vous allez donc avoir besoin des versions Linux de ces fichiers de bibliothèque. Mais que faire si vous n'avez pas de machine Linux à portée de main ?

Vous pourriez vous procurer une instance EC2 d'Amazon (ou une droplet sur Digital Ocean, ou toute VM Linux de votre choix), mais à mon avis, c'est assez compliqué et pourrait même vous coûter un peu d'argent (surtout si vous oubliez de supprimer la boîte EC2 lorsque vous n'en avez plus besoin).

Je pense que la solution la plus simple est d'utiliser Docker.

### L'approche Docker

Avec [Docker](http://docker.com), vous pouvez très facilement exécuter un conteneur Linux localement sur votre Mac, installer les bibliothèques Python dans le conteneur afin qu'elles soient automatiquement au bon format Linux, et compresser les fichiers prêts à être téléchargés sur AWS. Vous devrez d'abord installer [Docker pour Mac (ou Windows)](https://www.docker.com/products/docker).

Lancez un conteneur Ubuntu qui peut voir le code Lambda que vous souhaitez télécharger.

```
docker run -v <répertoire avec votre code>:/working -it --rm ubuntu
```

* Le drapeau `-v` rend votre répertoire de code disponible à l'intérieur du conteneur dans un répertoire appelé working.
* Le drapeau `-it` signifie que vous pouvez interagir avec ce conteneur.
* Le drapeau `--rm` signifie que Docker supprimera le conteneur lorsque vous aurez terminé.
* `ubuntu` est le nom d'une image de conteneur officielle contenant, comme vous l'avez deviné, Ubuntu. Si cette image de conteneur n'est pas déjà sur votre machine, Docker la téléchargera pour vous.

Vous devriez maintenant être à l'intérieur du conteneur à une invite de shell ressemblant à ceci :

```
root@c1996f32a397:/#
```

Installez pip et zip :

```
$ apt-get update
$ apt-get install python-pip
$ apt-get install zip
```

Déplacez-vous dans le répertoire de travail (vous devriez pouvoir voir le code de votre fonction Lambda ici) :

```
$ cd working
```

Utilisez pip pour obtenir la ou les bibliothèques qui vous intéressent. Vous pouvez utiliser le drapeau -t pour indiquer à pip de placer les bibliothèques ici dans le répertoire actuel, ce qui sera plus pratique plus tard car c'est là que le package de déploiement AWS les attend :

```
$ pip install -t . <bibliothèque>
```

Si vous êtes très curieux, vous pouvez jeter un coup d'œil pour voir ce que cela installe. Dans mon propre cas, j'ai installé la bibliothèque `editdistance`, qui m'a donné les répertoires et fichiers supplémentaires suivants.

```
editdistance:
__init__.py __init__.pyc _editdistance.h bycython.so def.h
```

```
editdistance-0.3.1.dist-info:
DESCRIPTION.rst INSTALLER METADATA RECORD WHEEL metadata.json top_level.txt
```

Vous voyez ce fichier bycython.so ? Il s'agit de la version correcte, Linux, du binaire auquel AWS s'opposait lorsque j'ai rencontré l'erreur Invalid ELF header (montrée dans la capture d'écran du journal d'erreurs ci-dessus).

Créez le fichier ZIP avec votre code Lambda (dans mon cas, un seul fichier appelé lambda_function.py) et les bibliothèques (pour moi, les deux répertoires editdistance et leur contenu).

```
$ zip linux-lambda.zip lambda_function.py
```

```
$ zip -r linux-lambda.zip edit*
```

Le drapeau `-r` sur zip indique de ajouter récursivement le contenu des répertoires.

Vous avez maintenant un fichier d'archive appelé linux-lambda.zip qui est prêt à être téléchargé sur AWS. Et comme le répertoire est monté depuis l'hôte (votre Mac) dans le conteneur, vous pouvez simplement télécharger le fichier dans la console.

De retour dans le terminal, tapez `exit` pour quitter le conteneur, et il sera comme s'il n'avait jamais existé, à l'exception de l'existence du fichier linux-lambda.zip, qui est toujours disponible sur l'hôte.

Téléchargez le fichier ZIP dans la console, enregistrez-le et essayez d'exécuter un test. Plus d'erreur Invalid ELF header !

Si cet article vous aide, n'hésitez pas à cliquer sur le bouton ? pour le rendre plus facile à trouver pour les autres. Si vous l'aimez vraiment, pourquoi ne pas le partager aussi ?

J'ai écrit quelques autres articles sur ce que j'apprends en écrivant ma première compétence Alexa, comme celui-ci où j'[ajoute des capacités de stockage de base de données à ma fonction Lambda](https://hackernoon.com/my-alexa-skill-with-storage-5adb1d097b88#.d0a1a7xha). Si vous les trouvez utiles, vous pourriez être intéressé par un livre que j'écris appelé [Adventures with Alexa](http://leanpub.com/adventureswithalexa). Choisissez votre propre prix !