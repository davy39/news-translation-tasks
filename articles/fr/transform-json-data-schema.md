---
title: Comment transformer des données JSON pour correspondre à n'importe quel schéma
subtitle: ''
author: Nneoma Uche
co_authors: []
series: null
date: '2025-07-10T04:23:53.810Z'
originalURL: https://freecodecamp.org/news/transform-json-data-schema
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752121420492/513db316-cdc7-47ef-8f20-4911cf5d41f9.png
tags:
- name: Python
  slug: python
- name: pandas
  slug: pandas
- name: json
  slug: json
- name: json-schema
  slug: json-schema
- name: python beginner
  slug: python-beginner
seo_title: Comment transformer des données JSON pour correspondre à n'importe quel
  schéma
seo_desc: 'Whether you’re transferring data between APIs or just preparing JSON data
  for import, mismatched schemas can break your workflow.  Learning how to clean and
  normalize JSON data ensures a smooth, error-free data transfer.

  This tutorial demonstrates ho...'
---

Que vous transfériez des données entre des API ou que vous prépariez simplement des données JSON pour une importation, des schémas non correspondants peuvent interrompre votre flux de travail. Apprendre à nettoyer et normaliser les données JSON garantit un transfert de données fluide et sans erreur.

Ce tutoriel démontre comment nettoyer un JSON désordonné et exporter les résultats dans un nouveau fichier, basé sur un schéma prédéfinis. Le fichier JSON que nous allons nettoyer contient un ensemble de données de 200 enregistrements clients synthétiques.

Dans ce tutoriel, nous appliquerons deux méthodes pour nettoyer les données d'entrée :

* Avec Python pur

* Avec `pandas`

Vous pouvez appliquer l'une ou l'autre de ces méthodes dans votre code. Mais la méthode `pandas` est meilleure pour les grands ensembles de données complexes. Commençons directement par le processus.

### Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequis)

* [Ajouter et inspecter le fichier JSON](#heading-ajouter-et-inspecter-le-fichier-json)

* [Définir le schéma cible](#heading-definir-le-schema-cible)

* [Comment nettoyer les données JSON avec Python pur](#heading-comment-nettoyer-les-donnees-json-avec-python-pur)

* [Comment nettoyer les données JSON avec Pandas](#heading-comment-nettoyer-les-donnees-json-avec-pandas)

* [Comment valider le JSON nettoyé](#heading-comment-valider-le-json-nettoye)

* [Pandas vs Python pur pour le nettoyage des données](#heading-pandas-vs-python-pur-pour-le-nettoyage-des-donnees)

## Prérequis

Pour suivre ce tutoriel, vous devez avoir une compréhension de base de :

* Les dictionnaires, listes et boucles Python

* La structure des données JSON (clés, valeurs et imbrication)

* Comment lire et écrire des fichiers JSON avec le module `json` de Python

## Ajouter et inspecter le fichier JSON

Avant de commencer à écrire du code, assurez-vous que le fichier **.json** que vous souhaitez nettoyer se trouve dans votre répertoire de projet. Cela facilite le chargement dans votre script en utilisant uniquement le nom du fichier.

Vous pouvez maintenant inspecter la structure des données en visualisant le fichier localement ou en le chargeant dans votre script, avec le module intégré `json` de Python.

Voici comment faire (en supposant que le nom du fichier est **« old_customers.json »**) :

![Code pour visualiser ou imprimer le contenu du fichier JSON brut dans le terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1752079424973/3cd77410-6fa9-483d-9a73-edbe4c035327.jpeg align="center")

Cela vous montre si le fichier JSON est structuré comme un dictionnaire ou une liste. Il imprime également le fichier entier dans votre terminal. Le mien est un dictionnaire qui mappe à une liste de 200 entrées de clients. Vous devriez toujours ouvrir le fichier JSON brut dans votre IDE pour examiner de plus près sa structure et son schéma.

## Définir le schéma cible

Si quelqu'un demande que les données JSON soient nettoyées, cela signifie probablement que le [schéma actuel](https://json-schema.org/understanding-json-schema/about) n'est pas adapté à son usage prévu. À ce stade, vous devez être clair sur ce à quoi l'exportation JSON finale devrait ressembler.

Le schéma JSON est essentiellement un plan qui décrit :

* les champs requis

* les noms des champs

* le type de données pour chaque champ

* les formats standardisés (par exemple, les emails en minuscules, les espaces blancs rognés, etc.)

Voici à quoi ressemble l'ancien schéma par rapport au schéma cible :

![Une capture d'écran de l'ancien schéma JSON à transformer](https://cdn.hashnode.com/res/hashnode/image/upload/v1751956173106/d5957404-57ae-4de9-b61b-90eefa0b9260.jpeg align="center")

![Le schéma JSON attendu](https://cdn.hashnode.com/res/hashnode/image/upload/v1751956365336/dcf6a024-1ae6-4c95-92ae-5544ba4cbb3e.jpeg align="center")

Comme vous pouvez le voir, l'objectif est de supprimer les champs `customer_id` et `address` dans chaque entrée et de renommer le reste comme suit :

* `name` en `full_name`

* `email` en `email_address`

* `phone` en `mobile`

* `membership_level` en `tier`

Le résultat doit contenir 4 champs de réponse au lieu de 6, tous renommés pour correspondre aux exigences du projet.

## Comment nettoyer les données JSON avec Python pur

Explorons l'utilisation du module intégré `json` de Python pour aligner les données brutes avec le schéma prédéfinis.

### Étape 1 : Importer les modules `json` et `time`

L'importation de `json` est nécessaire car nous travaillons avec des fichiers JSON. Mais nous utiliserons le module `time` pour suivre combien de temps prend le processus de nettoyage des données.

```python
import json
import time
```

### Étape 2 : Charger le fichier avec `json.load()`

```python
start_time = time.time()
with open('old_customers.json') as file:
    crm_data = json.load(file)
```

### Étape 3 : Écrire une fonction pour parcourir et nettoyer chaque entrée de client dans le dictionnaire

```python
def clean_data(records):
    transformed_records = []
    for customer in records["customers"]:
        transformed_records.append({
                "full_name": customer["name"],
                "email_address": customer["email"],
                "mobile": customer["phone"],
                "tier": customer["membership_level"],

                })
    return {"customers": transformed_records}

new_data = clean_data(crm_data)
```

`clean_data()` prend les données originales (**temporairement**) stockées dans la variable records, les transformant pour correspondre à notre schéma cible.

Puisque le fichier JSON que nous avons chargé est un dictionnaire contenant une clé `customers`, qui mappe à une liste d'entrées de clients, nous accédons à cette clé et parcourons chaque entrée dans la liste.

Dans la boucle for, nous renommons les champs pertinents et stockons les entrées nettoyées dans une nouvelle liste appelée `transformed_records`.

Ensuite, nous retournons le dictionnaire, avec la clé `customers` intacte.

### Étape 4 : Sauvegarder la sortie dans un fichier .json

Décidez d'un nom pour vos données JSON nettoyées et attribuez-le à une variable `output_file`, comme ceci :

```python
output_file = "transformed_data.json"
with open(output_file, "w") as f:
    json.dump(new_data, f, indent=4)
```

Vous pouvez également ajouter une instruction `print()` sous ce bloc pour confirmer que le fichier a été sauvegardé dans votre répertoire de projet.

### Étape 5 : Chronométrer le processus de nettoyage des données

Au début de ce processus, nous avons importé le module time pour mesurer combien de temps il faut pour nettoyer les données JSON en utilisant Python pur. Pour suivre le temps d'exécution, nous avons stocké l'heure actuelle dans une variable `start_time` avant la fonction de nettoyage, et nous inclurons maintenant une variable `end_time` à la fin du script.

La différence entre les valeurs `end_time` et `start_time` vous donne le temps d'exécution total en secondes.

```python
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Transformed data saved to {output_file}")
print(f"Processing data took {elapsed_time:.2f} seconds")
```

Voici combien de temps le processus de nettoyage des données a pris avec l'approche Python pur :

![Temps d'exécution du script affiché dans le terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1751957367537/4a33fc16-7158-427e-b715-bec10a586857.jpeg align="center")

## Comment nettoyer les données JSON avec Pandas

Maintenant, nous allons essayer d'obtenir les mêmes résultats qu'auparavant, en utilisant Python et une bibliothèque tierce appelée `pandas`. Pandas est une bibliothèque open-source utilisée pour la manipulation et l'analyse de données en Python.

Pour commencer, vous devez avoir la bibliothèque Pandas installée dans votre répertoire. Dans votre terminal, exécutez :

```python
pip install pandas
```

Puis suivez ces étapes :

### Étape 1 : Importer les bibliothèques pertinentes

```python
import json
import time
import pandas as pd
```

### Étape 2 : Charger le fichier et extraire les entrées de clients

Contrairement à la méthode Python pur, où nous avons simplement indexé le nom de la clé `customers` pour accéder à la liste des données clients, travailler avec `pandas` nécessite une approche légèrement différente.

Nous devons extraire la liste avant de la charger dans un DataFrame car `pandas` attend des données structurées. Extraire la liste des dictionnaires de clients à l'avance garantit que nous isolons et nettoyons les enregistrements pertinents seuls, prévenant les erreurs causées par des données JSON imbriquées ou non pertinentes.

```python
start_time = time.time()
with open('old_customers.json', 'r') as f:
    crm_data = json.load(f)

#Extraire la liste des entrées de clients
clients = crm_data.get("customers", [])
```

### Étape 3 : Charger les entrées de clients dans un DataFrame

Une fois que vous avez une liste propre de dictionnaires de clients, chargez la liste dans un DataFrame et attribuez ladite liste à une variable, comme ceci :

```python
#Charger dans un dataframe
df = pd.DataFrame(clients)
```

Cela crée une structure tabulaire ou de type feuille de calcul, où chaque ligne représente un client. Charger la liste dans un DataFrame vous permet également d'accéder aux puissantes méthodes de nettoyage de données de `pandas` comme :

* `drop_duplicate()` : supprime les lignes ou entrées en double d'un DataFrame

* `dropna()` : supprime les lignes avec des données manquantes ou nulles

* `fillna(value)` : remplace toutes les données manquantes ou nulles par une valeur spécifiée

* `drop(columns)` : supprime explicitement les colonnes inutilisées

### Étape 4 : Écrire une fonction personnalisée pour renommer les champs pertinents

À ce stade, nous avons besoin d'une fonction qui prend une seule entrée de client - une ligne - et retourne une version nettoyée qui correspond au schéma cible (`full_name`, `email_address`, `mobile` et `tier`).

La fonction doit également gérer les données manquantes en définissant des valeurs par défaut comme **« Unknown »** ou **« N/A »** lorsqu'un champ est absent.

**P.S** : Au début, j'ai utilisé `drop(columns)` pour supprimer explicitement les champs `address` et `customer_id`. Mais ce n'est pas nécessaire dans ce cas, car la fonction `transform_fields()` ne sélectionne et ne renomme que les champs requis. Toutes les colonnes supplémentaires sont automatiquement exclues des données nettoyées.

### Étape 5 : Appliquer la transformation de schéma à toutes les lignes

Nous utiliserons la méthode `apply()` de `pandas` pour appliquer notre fonction personnalisée à chaque ligne du DataFrame. Cela créera une Série (par exemple, 0 → {...}, 1 → {...}, 2 → {...}), qui n'est pas compatible JSON.

Comme `json.dump()` attend une liste, et non une Série Pandas, nous appliquerons `tolist()`, convertissant la Série en une liste de dictionnaires.

```python
#Appliquer la transformation de schéma à toutes les lignes
transformed_df = df.apply(transform_fields, axis=1)

#Convertir la série en liste de dictionnaires
transformed_data = transformed_df.tolist()
```

Une autre façon d'aborder cela est avec une compréhension de liste. Au lieu d'utiliser `apply()` du tout, vous pouvez écrire :

```python
transformed_data = [transform_fields(row) for row in df.to_dict(orient="records")]
```

`orient=records` est un argument pour `df.to_dict` qui indique à pandas de convertir le DataFrame en une liste de dictionnaires, où chaque dictionnaire représente un seul enregistrement de client (c'est-à-dire une ligne).

Ensuite, la **boucle for** itère à travers chaque enregistrement de client de la liste, appelant la fonction personnalisée sur chaque ligne. Enfin, la compréhension de liste (**\[...\]**) collecte les lignes nettoyées dans une nouvelle liste.

### Étape 6 : Sauvegarder la sortie dans un fichier .json

```python
#Sauvegarder les données nettoyées
output_data = {"customers": transformed_data}
output_file = "applypandas_customer.json"
with open(output_file, "w") as f:
    json.dump(output_data, f, indent=4)
```

Je recommande de choisir un nom de fichier différent pour votre sortie `pandas`. Vous pouvez inspecter les deux fichiers côte à côte pour voir si cette sortie correspond au résultat que vous avez obtenu en nettoyant avec Python pur.

### Étape 7 : Suivre le temps d'exécution

Une fois de plus, vérifiez la différence entre l'heure de début et l'heure de fin pour déterminer le temps d'exécution du programme.

```python
end_time = time.time()
elapsed_time = end_time - start_time

#print(f"Transformed data saved to {output_file}")
print(f"Transformed data saved to {output_file}")
print(f"Processing data took {elapsed_time:.2f} seconds")
```

Lorsque j'ai utilisé la **compréhension de liste** pour appliquer la fonction personnalisée, le temps d'exécution de mon script était de **0,03 secondes**, mais avec la fonction `apply()` de `pandas`, le temps d'exécution total est passé à **0,01 secondes**.

### Aperçu de la sortie finale :

Si vous avez suivi ce tutoriel de près, votre sortie JSON devrait ressembler à ceci - que vous ayez utilisé la méthode `pandas` ou l'approche Python pur :

![La sortie JSON attendue après la transformation du schéma](https://cdn.hashnode.com/res/hashnode/image/upload/v1751961256627/d7b585f7-4585-4354-9fa7-a171adb31f90.jpeg align="center")

## Comment valider le JSON nettoyé

Valider votre sortie garantit que les données nettoyées suivent la structure attendue avant d'être utilisées ou partagées. Cette étape aide à détecter les erreurs de formatage, les champs manquants et les mauvais types de données tôt.

Voici les étapes pour valider votre fichier JSON nettoyé :

### Étape 1 : Installer et importer `jsonschema`

`jsonschema` est une bibliothèque de validation tierce pour Python. Elle vous aide à définir la structure attendue de vos données JSON et à vérifier automatiquement si votre sortie correspond à cette structure.

Dans votre terminal, exécutez :

```python
pip install jsonschema
```

Importez les bibliothèques requises :

```python
import json
from jsonschema import validate, ValidationError
```

`validate()` vérifie si vos données JSON correspondent aux règles définies dans votre schéma. Si les données sont valides, rien ne se passe. Mais s'il y a une erreur - comme un champ manquant ou un mauvais type de données - elle lève une `ValidationError`.

### Étape 2 : Définir un schéma

Comme vous le savez, le schéma JSON change avec chaque structure de fichier. Si vos données JSON diffèrent de ce avec quoi nous avons travaillé jusqu'à présent, apprenez à créer un schéma [ici](https://json-schema.org/learn/getting-started-step-by-step#validate-json-data-against-the-schema). Sinon, le schéma ci-dessous définit la structure que nous attendons pour notre JSON nettoyé :

```python
schema = {
    "type": "object",
    "properties": {
        "customers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "full_name": {"type": "string"},
                    "email_address": {"type": "string"},
                    "mobile": {"type": "string"},
                    "tier": {"type": "string"}
                },
                "required": ["full_name", "email_address", "mobile", "tier"]
            }
        }
    },
    "required": ["customers"]
}
```

* Les données sont un objet qui doit contenir une clé : `"customers"`.

* `"customers"` doit être un **tableau** (une liste), chaque objet représentant une entrée de client.

* Chaque entrée de client doit avoir quatre champs - tous des chaînes de caractères :

    * `"full_name"`

    * `"email_address"`

    * `"mobile"`

    * `"tier"`

* Les champs `"required"` garantissent qu'aucun des champs pertinents ne manque dans aucun enregistrement de client.

### Étape 3 : Charger le fichier JSON nettoyé

```python
with open("transformed_data.json") as f:
    data = json.load(f)
```

### Étape 4 : Valider les données

Pour cette étape, nous utiliserons un bloc `try... except` pour terminer le processus en toute sécurité, et afficher un message utile si le code lève une `ValidationError`.

```python
try:
    validate(instance=data, schema=schema)
    print("JSON is valid.")
except ValidationError as e:
    print("JSON is invalid:", e.message)
```

## Pandas vs Python pur pour le nettoyage des données

D'après ce tutoriel, vous pouvez probablement dire que l'utilisation de Python pur pour nettoyer et restructurer le JSON est l'approche la plus directe. Elle est rapide et idéale pour gérer de petits ensembles de données ou des transformations simples.

Mais à mesure que les données grandissent et deviennent plus complexes, vous pourriez avoir besoin de méthodes avancées de nettoyage de données que Python seul ne fournit pas. Dans de tels cas, `pandas` devient le meilleur choix. Il gère efficacement les grands ensembles de données complexes, fournissant des fonctions intégrées pour gérer les données manquantes et supprimer les doublons.

Vous pouvez étudier la [feuille de triche Pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) pour apprendre davantage de méthodes de manipulation de données.