---
title: Qu'est-ce que les Logs en Programmation ?
subtitle: ''
author: Syeda Maham Fahim
co_authors: []
series: null
date: '2025-02-11T23:48:20.097Z'
originalURL: https://freecodecamp.org/news/what-are-logs-in-programming
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738685115991/600c01b6-b031-4ce9-a77a-5d88fcdaa68a.png
tags:
- name: logging
  slug: logging
- name: Python
  slug: python
- name: error handling
  slug: error-handling
seo_title: Qu'est-ce que les Logs en Programmation ?
seo_desc: 'Have you ever run a program, and it crashed? No error messages, no hints,
  just silence. How do you figure out what went wrong? That''s where logging saves
  the day.

  Logs keep track of what’s happening inside your code so that when things go wrong,
  you ...'
---

Avez-vous déjà exécuté un programme, et il a planté ? Aucun message d'erreur, aucun indice, juste le silence. Comment faire pour comprendre ce qui s'est mal passé ? C'est là que le logging sauve la journée.

Les logs gardent une trace de ce qui se passe à l'intérieur de votre code afin que, lorsque les choses tournent mal, vous n'ayez pas à deviner. Ils sont similaires à `print` ou `console.log`, mais plus puissants.

Dans ce tutoriel, j'utiliserai Python pour créer et vous guider à travers quelques exemples de code de logging.

Avant de parler des logs, comprenons les différents types d'erreurs que vous pourriez utiliser ou rencontrer.

## Types d'Erreurs

Lorsque vous construisez une application de niveau production, vous devez afficher des erreurs en fonction de leur gravité. Il existe plusieurs types d'erreurs, et les plus importants sont :

* **DEBUG** : Informations détaillées, généralement utiles pour diagnostiquer les problèmes.

* **INFO** : Informations générales sur la progression du programme.

* **WARNING** : Quelque chose d'inattendu s'est produit, mais ce n'est pas critique.

* **ERROR** : Une erreur s'est produite, mais le programme peut encore s'exécuter.

* **CRITICAL** : Une erreur très grave qui peut empêcher le programme de s'exécuter.

## Qu'est-ce que le Logging ?

Maintenant, allons droit au but et comprenons ce qu'est le logging.

En termes simples, les logs ou le logging est l'acte d'enregistrer des informations sur tout ce que fait votre programme. Les informations enregistrées peuvent être de n'importe quel type, allant de détails de base comme quelles fonctions ont été appelées à des détails plus approfondis comme le suivi des erreurs ou des problèmes de performance.

### Pourquoi Avons-Nous Besoin du Logging ?

Vous pourriez penser, "Si les logs impriment des erreurs, des infos, etc., je peux simplement utiliser des instructions print. Pourquoi ai-je besoin du logging ?" Eh bien, `print` fonctionne, mais le logging vous donne plus de contrôle :

↳ Il peut stocker des messages dans un fichier.  
↳ Il a différents niveaux (info, warning, error, etc.).  
↳ Vous pouvez filtrer les messages en fonction de leur importance.  
↳ Il aide au débogage sans encombrer votre code.

Ce sont des choses que les instructions `print` ne peuvent pas faire efficacement.

## Comment Ajouter des Logs en Python

En Python, le module `logging` est spécialement conçu pour le logging.

Configurons quelques logs pour voir comment ils fonctionnent.

### Étape 1 : Importer le Module de Logging

Pour commencer à utiliser le logging, nous devons importer le module :

```bash
import logging
```

### Étape 2 : Logger des Messages

Maintenant, vous pouvez commencer à logger des messages dans votre programme. Vous pouvez utiliser différents niveaux de log en fonction de l'importance du message. Pour rappel, ces niveaux sont (du moins au plus urgent) :

* DEBUG

* INFO

* WARNING

* ERROR

* CRITICAL

Loggons un message simple à chaque niveau :

```bash
logging.debug("Ceci est un message de debug")
logging.info("Ceci est un message d'information")
logging.warning("Ceci est un message d'avertissement")
logging.error("Ceci est un message d'erreur")
logging.critical("Ceci est un message critique")
```

Lorsque vous exécutez cela, vous verrez un message imprimé dans la console, similaire à ceci :

![Terminal montrant les messages de log Python.](https://cdn.hashnode.com/res/hashnode/image/upload/v1738500126070/a2a395c3-5cbe-4f94-bea2-d871cfc1529e.png align="center")

Vous pourriez vous demander pourquoi vous ne voyez pas les messages **DEBUG** et **INFO**. Le niveau de logging par défaut empêche cela.

Par défaut, le niveau de logging est défini sur `WARNING`. Cela signifie que seuls les messages avec une gravité de `WARNING` ou supérieure seront affichés (c'est-à-dire `WARNING`, `ERROR`, et `CRITICAL`).

### **Étape 3 : Configurer la Configuration de Base

Pour voir les messages `debug` et `info`, nous devons définir le niveau de logging sur `DEBUG` avant d'exécuter le code.

Cela signifie que nous devons configurer les logs. Pour ce faire, utilisez la méthode `basicConfig` ci-dessous :

```bash
logging.basicConfig(level=logging.DEBUG)
```

Cette configuration de base vous permet de logger des messages au niveau **DEBUG** ou supérieur. Vous pouvez changer le niveau en fonction du type de logs que vous souhaitez.

Maintenant, tous les logs sont imprimés :

![messages de log : debug, info, warning, error, critical.](https://cdn.hashnode.com/res/hashnode/image/upload/v1738500423798/96b65689-f0e4-4663-9d1a-1dc7147e964e.png align="center")

### Étape 4 : Logger dans un Fichier

Maintenant, sauvegardons ces logs dans un fichier afin que nous puissions garder une trace des erreurs, ainsi que de leur moment d'occurrence. Pour ce faire, mettez à jour la configuration :

```bash
logging.basicConfig(filename='data_log.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
```

Ici :

* `asctime` – L'heure à laquelle l'événement s'est produit.

* `levelname` – Le type de log (par exemple, **DEBUG**, **INFO**).

* `message` – Le message que nous affichons.

Maintenant, lorsque vous exécutez le programme, le fichier de log sera généré et sauvegardera vos logs, montrant le moment exact, le type d'erreur et le message. Comme ceci :

![Fichier de log avec des messages debug, info, warning, error, critical](https://cdn.hashnode.com/res/hashnode/image/upload/v1738500713832/7895f1db-8740-494a-86dd-86020f4f5569.png align="center")

## Comment Utiliser les Loggers pour Plus de Contrôle

Si vous travaillez sur un grand projet, vous pourriez vouloir un logger utilitaire que vous pouvez utiliser n'importe où dans le code. Créons ce logger personnalisé.

Tout d'abord, nous mettrons à jour le `basicConfig` pour ajouter le nom du fichier, le numéro de ligne et nous nous assurerons qu'il écrit tout, même les caractères spéciaux :

```bash
logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s', 
        filemode='w',
        encoding='utf-8' 
    )
```

Explication :

* `encoding='utf-8'` — Assure que les caractères spéciaux sont loggés.

* `%(filename)s:%(lineno)d` — Log le nom du fichier et le numéro de ligne où le log a été généré.

Maintenant, configurons un logger de console personnalisé :

```bash
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.DEBUG)
  console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')  # Ajout du numéro de ligne
  console_handler.setFormatter(console_formatter)

    
   logging.getLogger().addHandler(console_handler)
```

Cette configuration fait ce qui suit :

* `console_handler` : Envoie les messages de log à la console (stdout).

* `console_formatter` : Formate le message de log avec l'heure, le niveau, le nom du fichier, le numéro de ligne et le message.

* `logging.getLogger().addHandler(console_handler)` : Ajoute le gestionnaire personnalisé au logger racine, afin que les messages de log soient imprimés dans la console.

### Exemple de Code Complet

```python
import logging
import os
from datetime import datetime

def setup_daily_logger():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, 'logs')  
    os.makedirs(log_dir, exist_ok=True)

    
    current_time = datetime.now().strftime("%m_%d_%y_%I_%M_%p")
    log_file = os.path.join(log_dir, f"{current_time}.log")

   
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s', 
        filemode='w',
        encoding='utf-8' 
    )

    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')  # Ajout du numéro de ligne
    console_handler.setFormatter(console_formatter)

    
    logging.getLogger().addHandler(console_handler)

    
    return logging.getLogger(__name__)
```

### Que se Passe-t-il Maintenant ?

Maintenant, chaque fois que vous exécutez le programme, un nouveau fichier de log sera créé dans le dossier `logs`. Chaque fois que le programme est exécuté, un nouveau fichier de log avec un horodatage unique sera généré.

Comme ceci :

![log personnalisé utilisé dans app.py](https://cdn.hashnode.com/res/hashnode/image/upload/v1738503550743/1ad9fb99-762a-4ca9-a189-58d044955617.png align="center")

Ces logs vous donneront une image claire du comportement de votre programme et vous aideront à le déboguer.

J'espère que cet article vous a aidé à avoir une image plus claire des logs et de leur importance en programmation.

# Exemples Pratiques du Monde Réel

Maintenant que vous comprenez ce que sont les logs et comment les configurer en Python, examinons des cas d'utilisation réels.

## 1. Bot : Scraping du Plus Grand Site Immobilier de Corée

Voici un exemple de bot conçu pour scraper le plus grand site immobilier de Corée.

* Les logs montrent chaque étape que le bot effectue, ce qui facilite le suivi de la progression.

* Si une erreur se produit à une étape quelconque, elle est enregistrée dans le fichier de log.

* Même si le bot plante, je peux vérifier les logs pour identifier où les choses ont mal tourné.

![Fichier de log avec des messages INFO montrant les détails d'extraction de la ville et de la localité.](https://cdn.hashnode.com/res/hashnode/image/upload/v1739037891010/69a8b5ae-d202-4466-add0-bb2ace28230a.png align="center")

![Fichier de log avec des messages INFO montrant les détails d'extraction de la ville et de la localité.](https://cdn.hashnode.com/res/hashnode/image/upload/v1739037833210/bf9ceba0-2caf-48c6-bdb8-ac2d9eb901bd.png align="center")

L'une des méthodes de cette classe de bot utilise le logging pour suivre si le bot sélectionne correctement la province.

![Fonction select_province qui utilise le logging](https://cdn.hashnode.com/res/hashnode/image/upload/v1739038058017/6153c909-477d-4cd6-b493-124b96bc595f.png align="center")

Ici :

* Si une erreur ou un avertissement se produit, il est sauvegardé dans le fichier de log.

* Plus tard, vous pouvez consulter les logs et découvrir exactement ce qui s'est passé.

## 2. Bot : Scraping des Groupes Facebook

Maintenant, voyons comment le logging aide dans un scraper de groupes Facebook.

##### Suivi des Erreurs

* À un moment donné, le bot a échoué en raison d'une erreur.

* Puisque nous avions le logging en place, l'erreur a été sauvegardée dans le fichier de log.

* Cela vous permet de découvrir rapidement ce qui s'est mal passé.

![Fichier de log d'erreur](https://cdn.hashnode.com/res/hashnode/image/upload/v1739038507530/9662bed7-a124-4dd8-94a9-9d657ec022a1.png align="center")

Ici, vous voyez le nom exact du fichier et le numéro de ligne où l'erreur se produit.

![Le fichier de log montre les logs de succès](https://cdn.hashnode.com/res/hashnode/image/upload/v1739038826232/ce717b49-e532-4c5f-a40d-955591aa27a2.png align="center")

Une fois que nous avons identifié et corrigé le problème, le bot a recommencé à fonctionner.

Il capture chaque détail dans le log, économisant des heures de débogage en identifiant où les erreurs se produisent.

##### Débogage Facilité

* Les logs ont enregistré chaque détail de l'exécution du bot.

* Cela peut vous faire économiser des heures de débogage car vous saurez exactement où l'erreur s'est produite.

## Conclusion

Le logging est l'une de ces choses auxquelles personne ne pense jusqu'à ce que quelque chose se casse. Mais lorsque cela arrive, les logs deviennent votre meilleur ami.

Rappelez-vous :

* Le logging n'est pas seulement pour le suivi des erreurs—il vous aide à surveiller le flux de votre programme.

* Au lieu de deviner ce qui s'est mal passé, vérifiez les logs. La réponse s'y trouve généralement.

Assurez-vous d'ajouter le logging à votre code. Vous vous remercierez plus tard !

**Restez Connecté - @syedamahamfahim 🐭**