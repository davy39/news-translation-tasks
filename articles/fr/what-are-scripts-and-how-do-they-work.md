---
title: Que sont les scripts et comment fonctionnent-ils ? Améliorez votre productivité
  avec la programmation de scripts
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2025-01-27T14:31:17.247Z'
originalURL: https://freecodecamp.org/news/what-are-scripts-and-how-do-they-work
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737988076418/347e6d8a-1dd8-45d1-854b-fbc576eeed5f.png
tags:
- name: scripts
  slug: scripts
- name: automation
  slug: automation
- name: Bash
  slug: bash
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
seo_title: Que sont les scripts et comment fonctionnent-ils ? Améliorez votre productivité
  avec la programmation de scripts
seo_desc: 'Developers who have a lot of experience building rigid, quality software
  tend to automate most of their work by writing scripts. These scripts range from
  simple alias bash commands to repetitive cron triggers that run on a server.

  In this tutorial, y...'
---

Les développeurs qui ont beaucoup d'expérience dans la construction de logiciels rigides et de qualité tendent à automatiser la plupart de leur travail en écrivant des scripts. Ces scripts vont des commandes alias bash simples aux déclencheurs cron répétitifs qui s'exécutent sur un serveur.

Dans ce tutoriel, vous apprendrez ce qu'est la programmation de scripts, ses nombreux cas d'utilisation, ainsi que quelques avantages et inconvénients de l'utilisation de scripts. Nous passerons également en revue quelques exemples de scripts afin que vous puissiez les voir en action.

## Qu'est-ce qu'un script ?

Un script est un ensemble d'instructions écrites dans un langage de script (comme Bash, Python, JavaScript, et autres) qui vous aide à automatiser des tâches ou à contrôler des processus. Contrairement aux programmes compilés, les scripts sont généralement [interprétés](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/), ce qui signifie qu'ils sont exécutés directement par un environnement d'exécution sans compilation préalable.

Les scripts sont des outils puissants pour automatiser des tâches répétitives, gérer des flux de travail et résoudre des problèmes petits (et parfois grands) de manière efficace. Que vous soyez débutant ou développeur expérimenté, comprendre comment écrire des scripts peut améliorer votre productivité et élargir vos capacités techniques.

## Pourquoi écrire des scripts ?

J'ai déjà abordé ce que vous pouvez faire avec des scripts. Alors examinons quelques-uns de leurs avantages (et défis aussi) afin que vous compreniez pourquoi ils sont si puissants – et quand les utiliser.

### Avantages des scripts

1. Automatisation : Les scripts peuvent vous aider à simplifier des tâches répétitives telles que le traitement de données ou la gestion de fichiers.
   
2. Efficacité : ils peuvent également vous faire gagner du temps en automatisant des tâches que vous devriez sinon faire manuellement.
   
3. Réduction des erreurs : Les scripts peuvent aider à réduire les erreurs humaines grâce à une exécution cohérente des instructions.
   
4. Flexibilité : Les scripts peuvent s'adapter à une grande variété de tâches avec une modification minimale.
   
5. Intégration : Ils peuvent également s'intégrer de manière transparente avec d'autres systèmes, outils ou flux de travail.
   

### Défis avec les scripts

1. Performance : Les scripts peuvent être plus lents que les programmes compilés en raison de l'overhead d'interprétation.
   
2. Évolutivité : Ils ne sont pas toujours adaptés aux tâches à grande échelle ou hautement complexes.
   
3. Débogage : Le débogage des scripts peut parfois être difficile en raison de leur nature dynamique.
   
4. Risques de sécurité : Les scripts mal écrits peuvent exposer des vulnérabilités, surtout s'ils exécutent des commandes au niveau du système.
   

### Quand utiliser ou ne pas utiliser les scripts

Les scripts sont idéaux pour :

1. Les tâches sont simples, bien définies ou ponctuelles
   
2. Le prototypage ou l'automatisation rapide d'un processus
   
3. La portée est suffisamment petite pour éviter la complexité
   

Les scripts ne sont pas idéaux pour :

1. Les tâches critiques pour la performance nécessitant une haute efficacité. Au lieu d'un script, essayez d'utiliser un outil ETL (Extract, Transform, Load) dédié ou un courtier de messages, ou des outils alternatifs similaires qui correspondent à votre cas d'utilisation.
   
2. Les applications avec des interfaces utilisateur étendues. Au lieu de cela, vous pouvez construire une petite application ou un système modulaire avec une journalisation, des tests et une documentation appropriés.
   
3. Les scénarios nécessitant une maintenance à long terme, où les programmes compilés pourraient être plus stables. Au lieu de cela, utilisez des planificateurs de tâches ou des gestionnaires de flux de travail comme CRON, Airflow, AWS Lambda/GCP Functions.
   

## Comment écrire des scripts efficaces

Voici le processus que j'utilise pour écrire des scripts utiles. Après cela, nous verrons quelques exemples de scripts dans différents langages afin que vous puissiez obtenir une pratique concrète.

1. Définir le problème : Avant d'écrire un script, identifiez le problème qu'il résoudra. Soyez clair sur les tâches à automatiser et les résultats attendus.
   
2. Choisir le bon langage :
   
   * **Bash** : Idéal pour les tâches au niveau du système comme les opérations sur les fichiers ou la gestion de serveur.
       
   * **Python** : Excellent pour le traitement de données, le scraping web et l'automatisation plus complexe.
       
   * **JavaScript** : Adapté pour le développement web et l'automatisation basée sur le navigateur.
       
3. Écrire le script : Utilisez un éditeur de texte ou un environnement de développement intégré (IDE), et assurez-vous de suivre les meilleures pratiques comme l'utilisation de commentaires, de noms de variables significatifs et de code modulaire. Nous aborderons ces points ci-dessous.
   
4. Tester le script : Testez le script dans un environnement contrôlé pour vous assurer qu'il fonctionne comme prévu sans causer d'erreurs.
   
5. Exécuter et déployer : Exécutez le script dans son environnement prévu. Si nécessaire, planifiez son exécution en utilisant des outils comme Cron (pour Bash) ou des planificateurs de tâches.
   

## Exemples de scripts

Maintenant que vous connaissez les bases, faisons un peu de pratique. Supposons que vous avez environ 100 fichiers avec les noms « book-part-1.pdf », « book-part-2.pdf », ..., « book-part-100.pdf ». Vous voulez remplacer tous les tirets (-) dans les noms de fichiers par des traits de soulignement (_), car le site web où vous essayez de télécharger ces documents ne vous permet pas de télécharger des fichiers avec des noms contenant des tirets.

Voici des scripts écrits dans trois langages différents qui effectuent tous la même opération. Le processus est le suivant :

1. trouver tous les fichiers dans un répertoire,
   
2. vérifier s'ils contiennent des tirets (-) dans leur nom, et
   
3. remplacer tous les tirets par des traits de soulignement (_).
   

Voici les noms de fichiers de départ (contenant des tirets) :

![Noms de fichiers avec tirets](https://cdn.hashnode.com/res/hashnode/image/upload/v1737563509852/e9b1e671-465d-43ed-a831-3034852de624.png align="center")

### Script Bash

Nous commencerons par un script bash. Le voici :

```bash
#!/bin/bash
# Remplacer "-" par "_" dans les noms de fichiers
DIRECTORY="/path/to/your/folder"
for FILE in "$DIRECTORY"/*; do
    if [[ "$FILE" == *-* ]]; then
        NEW_NAME=$(echo "$FILE" | sed 's/-/_/g')
        mv "$FILE" "$NEW_NAME"
        echo "Renommé : $FILE -> $NEW_NAME"
    fi
done
```

Nous définissons le répertoire (dossier) en haut où se trouvent nos fichiers. Pour chaque fichier dans le répertoire, nous vérifions si le nom contient un `-`. Dans ce cas, nous créons un nouveau nom de fichier et le stockons dans la variable `NEW_NAME` en copiant l'ancien nom de fichier à l'aide de la commande `echo` et en remplaçant le `-` par `_` à l'aide de la commande `sed`. Enfin, nous utilisons la commande de déplacement `mv` avec les anciens et nouveaux noms de fichiers comme arguments.

### Script Python

Ensuite, voyons à quoi cela ressemblerait en Python :

```python
import os
# Remplacer "-" par "_" dans les noms de fichiers
directory = "/path/to/your/folder"
for filename in os.listdir(directory):
    if "-" in filename:
        old_path = os.path.join(directory, filename)
        new_filename = filename.replace("-", "_")
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renommé : {filename} -> {new_filename}")
```

Les étapes sont assez similaires en Python. Tout d'abord, nous définissons le répertoire, puis nous itérons à travers chaque fichier dans le répertoire. Pour trouver tous les fichiers dans le répertoire, nous devons utiliser la méthode `listdir` du package `os`.

Ensuite, nous vérifions si le nom du fichier contient un `-` à la ligne suivante. Dans ce cas, nous trouvons le chemin actuel (`old_path`) du fichier en fusionnant le répertoire et son nom de fichier. Nous pouvons créer le nouveau nom de fichier en remplaçant le `-` par `_` à l'aide de la méthode `replace`.

Nous générons ensuite le nouveau chemin de fichier (`new_path`) de la même manière que nous générons le `old_path`. Enfin, nous appelons la méthode `rename` dans le package `os` avec les anciens et nouveaux chemins de fichiers comme arguments.

### Script JavaScript

Et maintenant, voyons à quoi cela ressemblerait en JavaScript :

```javascript
const fs = require('fs');
const path = require('path');
const directory = '/path/to/your/folder';

fs.readdir(directory, (err, files) => {
    if (err) {
        console.error('Erreur de lecture du répertoire :', err);
        return;
    }
    files.forEach(file => {
        if (file.includes('-')) {
            const oldPath = path.join(directory, file);
            const newFilename = file.replace(/-/g, '_');
            const newPath = path.join(directory, newFilename);
            fs.rename(oldPath, newPath, err => {
                if (err) {
                    console.error(`Erreur de renommage ${file} :`, err);
                } else {
                    console.log(`Renommé : ${file} -> ${newFilename}`);
                }
            });
        }
    });
});
```

L'implémentation JavaScript est quelque peu similaire à l'implémentation Python – mais vous devrez écrire plus de code. Généralement, les développeurs ne préfèrent pas JavaScript pour ce type de scripts. La plupart d'entre eux s'appuient sur Bash/Python. JavaScript est mieux adapté pour les scripts d'automatisation basés sur le navigateur.

Néanmoins, voyons ce que nous avons ici. Dans ce code JavaScript, vous devez utiliser deux packages différents, `fs` et `path`. Nous définissons le répertoire en haut, lisons les fichiers dans le répertoire en utilisant la méthode `readdir` du package `fs`, et passons le répertoire comme argument. Avec le répertoire, nous passons également une fonction de rappel qui sera exécutée une fois les fichiers lus.

À l'intérieur de la fonction de rappel, nous parcourons chaque fichier et vérifions si le nom du fichier inclut un tiret (`-`). Si c'est le cas, nous trouvons l'ancien chemin en utilisant le package `path` avec le répertoire et les noms de fichiers comme arguments. Nous construisons ensuite le nouveau nom de fichier en remplaçant tous les tirets par des traits de soulignement à l'aide de la méthode `replace`.

De manière similaire à l'ancien chemin, nous trouvons le nouveau chemin en utilisant le nouveau nom de fichier comme argument. Ensuite, nous utilisons la méthode `rename` du package `fs` pour renommer le fichier en passant à la fois les anciens et nouveaux noms de fichiers. Si des erreurs surviennent lors du renommage ou de la lecture des fichiers dans un répertoire, nous journalisons le message d'erreur. Sinon, nous journalisons le message de succès.

#### Comment exécuter ces scripts

D'accord, voici comment vous pouvez réellement utiliser ces scripts :

1. Remplacez `/path/to/your/folder` par le répertoire réel contenant les fichiers.
   
2. Exécutez le script dans l'environnement correspondant :
   
   * **Bash** : Enregistrez sous un fichier `.sh`, puis exécutez avec `bash script.sh`
       
   * **Python** : Enregistrez sous un fichier `.py`, puis exécutez avec `python script.py`
       
   * **JavaScript** : Enregistrez sous un fichier `.js`, puis exécutez avec `node script.js`
       

La capture d'écran ci-dessous montre l'exécution du script bash pour changer les noms des fichiers.

![Changer le nom des fichiers en utilisant un script bash](https://cdn.hashnode.com/res/hashnode/image/upload/v1737563774216/f31158ab-da77-4b18-8625-ee0b2522e3e6.png align="center")

![Après l'exécution du script, les tirets dans les noms de fichiers sont remplacés par des traits de soulignement](https://cdn.hashnode.com/res/hashnode/image/upload/v1737563640766/4aa508af-1f0e-4fad-8b2c-ac2369cbe337.png align="center")

## Scripts récurrents

Les scripts récurrents sont conçus pour s'exécuter à intervalles réguliers, comme la vérification de l'état d'un système chaque semaine, le nettoyage des logs ou la récupération des mises à jour de données. Ces scripts utilisent généralement une forme de planificateur de tâches.

### Approches courantes

1. Tâches CRON : La plupart des systèmes d'exploitation supportent CRON, qui peut déclencher des scripts selon un calendrier défini.
   
2. Files d'attente de tâches : Des outils comme Celery (Python), Bull (Node.js) ou Sidekiq (Ruby) peuvent gérer des tâches planifiées avec plus de flexibilité.
   
3. Planificateurs cloud : Des services comme AWS Lambda avec EventBridge, Google Cloud Scheduler ou Azure Logic Apps vous permettent de configurer des scripts récurrents dans une architecture serverless.
   

Un bon exemple de cas d'utilisation pour les scripts récurrents serait l'envoi d'un rapport quotidien/hebdomadaire de l'utilisation/performance de votre système. Vous pourriez écrire un script qui trouve le nombre d'utilisateurs qui ont rejoint et souscrit à votre produit et envoyer ce rapport par email chaque jour/semaine.

## Bonnes pratiques pour écrire des scripts

Voici quelques points à garder à l'esprit lorsque vous écrivez des scripts :

**1. Utilisez des commentaires** : Expliquez les parties complexes du script avec des commentaires.

Dans l'exemple ci-dessous, sans le commentaire, quelqu'un pourrait devoir passer du temps supplémentaire à comprendre pourquoi le taux de taxe est un décimal et non un pourcentage.

```python
# Calculer le prix total avec taxe
def calculate_price_with_tax(price, tax_rate):
    # Le taux de taxe est exprimé en décimal (par exemple, 0.07 pour 7%)
    return price + (price * tax_rate)
```

2. **Gestion des erreurs** : Prévoyez les erreurs possibles et gérez-les élégamment.

Dans l'exemple ci-dessous, si le fichier est manquant, le script ne plantera pas – au lieu de cela, il affichera un message d'erreur utile.

```python
try:
    with open('data.csv', 'r') as file:
        data = file.readlines()
except FileNotFoundError:
    print("Erreur : le fichier 'data.csv' est introuvable. Assurez-vous que le fichier existe avant d'exécuter le script.")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
```

3. **Conception modulaire** : Décomposez le script en fonctions ou modules réutilisables.

Dans l'exemple ci-dessous, en séparant la fonctionnalité en fonctions plus petites et réutilisables, vous pouvez déboguer ou réutiliser des parties du script indépendamment.

```python
def fetch_data_from_api(api_url):
    # Récupérer les données depuis l'API donnée
    pass

def process_data(data):
    # Traiter les données dans le format souhaité
    pass

def save_to_file(data, filename):
    # Sauvegarder les données traitées dans un fichier
    pass

# Script principal
if __name__ == "__main__":
    data = fetch_data_from_api("https://example.com/api")
    processed_data = process_data(data)
    save_to_file(processed_data, "output.json")
```

4. **Validation des entrées** : Validez les entrées utilisateur pour prévenir les erreurs inattendues ou les risques de sécurité.

Sans validation, quelqu'un pourrait entrer des données invalides ou malveillantes (par exemple, des chaînes d'injection SQL dans certains scénarios).

```python
import re

# Valider que l'entrée est une adresse email valide
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email):
        raise ValueError("Format d'adresse email invalide")
    return email

# Exemple d'utilisation
try:
    user_email = validate_email(input("Entrez votre email : "))
    print(f"Email valide : {user_email}")
except ValueError as e:
    print(e)
```

5. **Contrôle de version** : Utilisez Git ou d'autres outils de contrôle de version pour suivre les changements.

Si un changement casse le script, vous pouvez facilement revenir à un commit précédent en utilisant `git checkout`. De plus, vous pouvez collaborer sans effort avec les membres de l'équipe.

```bash
git init
git add script.py
git commit -m "Premier commit"
```

## Conclusion

Écrire des scripts est une compétence qui peut considérablement améliorer votre productivité et vos capacités de résolution de problèmes. En comprenant les bases des langages de script comme Bash, Python et JavaScript, vous pouvez automatiser des tâches, rationaliser des flux de travail et gagner un temps précieux. Commencez petit, construisez de manière incrémentielle et pratiquez l'écriture de scripts pour différents cas d'utilisation afin de maîtriser cette compétence inestimable.

J'ai un exercice pour vous. Pour exécuter et vérifier cet exemple de script, vous pourriez penser que vous devez créer manuellement 100 fichiers. Cela prend beaucoup de temps.

J'ai écrit un script pour générer ces 100 fichiers. Je vous recommande également d'essayer d'écrire un script pour générer 100 fichiers avec des tirets dans leurs noms. Ensuite, essayez d'exécuter l'exemple de script pour convertir les tirets en traits de soulignement.

Cela peut sembler difficile au début, mais croyez-moi, vous n'avez besoin d'écrire que 5 lignes de code bash pour générer 100 fichiers. Pas seulement 100 – vous pouvez même générer un million/milliard/billion de fichiers avec seulement 5 lignes de code.

Si vous souhaitez en apprendre davantage sur les scripts, abonnez-vous à ma [newsletter par email (https://5minslearn.gogosoon.com/)](https://5minslearn.gogosoon.com/?ref=fcc_what_are_scripts) et suivez-moi sur les réseaux sociaux.

Bon script !