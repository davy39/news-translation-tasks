---
title: Comment pratiquer le logging en Python avec Logzero
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-13T21:26:52.000Z'
originalURL: https://freecodecamp.org/news/good-logging-practice-in-python-with-logzero
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/logezero-image.png
tags:
- name: logging
  slug: logging
- name: Python
  slug: python
seo_title: Comment pratiquer le logging en Python avec Logzero
seo_desc: 'By Davis David

  Logzero is a Python package created by Chris Hager that simplifies logging with
  Python 2 and 3. Logzero makes it easier as a print statement to show information
  and debugging details.

  If you are wondering what logging is, I recommend t...'
---

Par Davis David

Logzero est un package Python créé par [Chris Hager](https://twitter.com/metachris) qui simplifie le logging avec Python 2 et 3. Logzero facilite l'affichage d'informations et de détails de débogage comme une instruction print.

Si vous vous demandez **ce qu'est le logging**, je vous recommande de lire l'article précédent que j'ai écrit sur ["Comment exécuter des expériences de Machine Learning avec le module de logging Python"](https://medium.com/analytics-vidhya/how-to-run-machine-learning-experiments-with-python-logging-module-9030fbee120e), en particulier les 3 premières sections.

Dans cet article, vous apprendrez :

* Qu'est-ce que le logging ?
* Pourquoi le logging est important.
* Applications du logging dans différentes industries technologiques.

Logzero possède différentes fonctionnalités qui le rendent plus facile à utiliser dans les projets Python. Certaines de ces fonctionnalités sont :

* Logging facile vers la console et/ou un fichier.
* Fournit un objet logger Python standard entièrement configuré.
* Formatage joli, incluant des **couleurs** spécifiques aux niveaux dans la console.
* Fonctionne avec tous types d'encodages de caractères et caractères spéciaux.
* Compatible avec Python 2 et 3.
* Aucune dépendance Python supplémentaire.

## Installation

Pour installer logzero avec pip, exécutez la commande suivante :

```python
pip install -U logzero
```

Vous pouvez également installer logzero depuis le dépôt public [Github](https://github.com/metachris/logzero) :

```
git clone https://github.com/metachris/logzero.git
cd logzero
python setup.py install
```

## Exemple de base

Nous allons commencer par un exemple de base. Dans le fichier Python, nous allons importer le logger depuis logzero et essayer 4 exemples de niveaux de logging différents.

```python
#import logger from logzero
from logzero import logger

logger.debug("hello")
logger.info("info")
logger.warning("warning")
logger.error("error")
```

La sortie est colorée pour faciliter la lecture.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/dfdfdf.PNG)
_sortie logzero_

Comme vous pouvez le voir, chaque niveau a sa propre couleur. Cela signifie que vous pouvez identifier le niveau facilement en vérifiant la couleur.

## Écrire les logs dans un fichier

La plupart du temps, les utilisateurs Python ont tendance à écrire les logs dans un fichier. Lorsque le système est en cours d'exécution, vous pouvez sauvegarder les logs dans le fichier et les consulter pour vérifier les erreurs et à des fins de maintenance. Vous pouvez également définir un fichier pour sauvegarder toutes les entrées de log dans logzero.

Nous allons importer le logger et logfile depuis logzero. La méthode logfile nous aidera à configurer le fichier de log pour sauvegarder nos entrées de log.

Maintenant, vos entrées de log seront enregistrées dans le fichier nommé my_logfile.log.

```python
#import logger and logfile
from logzero import logger, logfile

#set logfile path
logfile('my_logfile.log')

# Log messages
logger.info("This log message saved in the log file")
```

La sortie dans le fichier my_logfile.log contient l'étiquette du niveau de logging (pour le niveau info étiqueté comme "I"), la date, l'heure, le nom du fichier Python, le numéro de ligne et le message lui-même.

```
[I 200409 23:49:59 demo:8] This log message saved in the log file
```

## Rotation d'un fichier de log

Vous n'avez pas besoin d'avoir un seul fichier de log sauvegardant toutes les entrées de log. Cela résulte en un fichier de log massif qui est intensif pour le système à ouvrir et fermer.

Vous pouvez utiliser les paramètres **maxBytes** et **backupCount** pour permettre au fichier de basculer à une taille prédéterminée. Lorsque la taille est sur le point d'être dépassée, le fichier est fermé et un nouveau fichier est ouvert silencieusement pour la sortie. La rotation se produit chaque fois que le fichier de log actuel est presque de la longueur maxBytes. Si maxBytes ou backupCount est zéro, la rotation ne se produit jamais.

Dans l'exemple ci-dessous, nous avons défini maxBytes à **1000000 octets (1 Mo).** Cela signifie que lorsque la taille dépasse 1 Mo, le fichier est fermé et un nouveau fichier est ouvert pour sauvegarder les entrées de log. Le nombre de sauvegardes à conserver est défini à 3.

```python
# Set a rotating logfile
logzero.logfile("my_logfile.log", maxBytes=1000000, backupCount=3)
```

## Définir un niveau de logging minimum

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_5vfxSz_sdZuPR0CnnBlDLg.png)
_[Photo par Son Nguyen Kim](https://www.toptal.com/resume/son-nguyen-kim?__hstc=753710.17be834d28ba29055621f0833fc6733b.1582400164835.1582400164835.1582400164835.1&amp;__hssc=753710.1.1582400164836&amp;__hsfp=3618320745" rel="noopener nofollow noopener)_

Le niveau de logging signifie définir le niveau d'importance d'un message de log donné. Vous pouvez également définir un **niveau de log** différent pour le gestionnaire de fichier en utilisant l'argument loglevel dans la méthode logfile.

Dans l'exemple ci-dessous, nous définissons loglevel à `warning`. Cela signifie que toutes les entrées de log en dessous du **niveau warning** ne seront pas sauvegardées dans un fichier de log.

```python
#import logzero package
from logzero import logger, logfile
import logging

# You can also set a different loglevel for the file handler
logfile("my_logfile.log", loglevel=logging.WARNING)

# Log messages
logger.info("This log message saved in the log file")
logger.warning("This log message saved in the log file")
```

## Définir un formateur personnalisé

La manière dont vous souhaitez que l'enregistrement de log soit formaté dépend de vous. Il existe différentes façons de formater votre enregistrement de log. Vous pouvez inclure la date, l'heure et le niveau de logging dans votre format afin de savoir quand le log a été envoyé et à quel niveau.

L'exemple ci-dessous montre comment vous pouvez configurer le format des enregistrements de log.

```python
#import logzero package
import logzero
from logzero import logger, logfile
import logging

#set file path
logfile("my_logfile.log")

# Set a custom formatter
my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');
logzero.formatter(my_formatter)

# Log messages
logger.info("This log message saved in the log file")
logger.warning("This log message saved in the log file")
```

Dans l'exemple ci-dessus, nous avons configuré le format de log en incluant _nom de fichier, date, heure, nom du niveau de logging,_ et _message._

Voici la sortie dans le fichier my_logfile.log :

```
demo.py - 2020-04-10 00:51:44,706 - INFO: This log message saved in the log file
demo.py - 2020-04-10 00:51:44,707 - WARNING: This log message saved in the log file
```

## Instances de Logger personnalisées

Au lieu d'utiliser le logger par défaut, vous pouvez également configurer des instances de logger spécifiques avec **logzero.setup_logger(..)**. Vous pouvez configurer et retourner une instance de logger entièrement configurée avec différents paramètres tels que _nom, nom de fichier de log, formateur, maxBytes, backupCount,_ et _niveau de logging._

Voici un exemple de fonctionnement de la configuration du logging avec une instance de logger personnalisée :

```python
import logzero package
from logzero import logger, logfile, setup_logger
import logging

# Set a custom formatter
my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');


#create custom logger instance
custom_logger = setup_logger(
 name="My Custom Logger",
 logfile="my_logfile.log",
 formatter=my_formatter,
 maxBytes=1000000,
 backupCount=3,level=logging.INFO)

# Log messages
custom_logger.info("This log message saved in the log file")
custom_logger.warning("This log message saved in the log file")
```

Dans l'exemple ci-dessus, nous avons défini une instance de logger personnalisée appelée **custom_logger** avec différentes valeurs de paramètres configurées.

## Conclusion

Dans cet article, vous avez appris les bases, ainsi que quelques exemples, de l'utilisation du package Python Logzero. Vous pouvez en apprendre davantage sur les fonctionnalités disponibles dans la [documentation](https://logzero.readthedocs.io/en/latest/#). Maintenant, vous pouvez commencer à implémenter le package logzero dans votre prochain [projet Python](https://realpython.com/intermediate-python-project-ideas/).

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine ! Vous pouvez également me joindre sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid)