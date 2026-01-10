---
title: Comment lire un fichier CSV depuis un bucket S3 dans AWS Lambda - Un guide
  définitif
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2023-09-12T10:44:09.000Z'
originalURL: https://freecodecamp.org/news/read-csv-file-from-s3-bucket-in-aws-lambda
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/unnamed.jpg
tags:
- name: AWS
  slug: aws
- name: Python
  slug: python
seo_title: Comment lire un fichier CSV depuis un bucket S3 dans AWS Lambda - Un guide
  définitif
seo_desc: "Amazon Simple Storage Service (S3) is a highly scalable, durable, and available\
  \ object storage service.\nIt is designed to store any amount of data, anytime,\
  \ from anywhere on the web. \nS3 is a key component of the Amazon Web Services (AWS)\
  \ cloud platf..."
---

Amazon Simple Storage Service (S3) est un service de stockage d'objets hautement scalable, durable et disponible.

Il est conçu pour stocker n'importe quelle quantité de données, à tout moment, depuis n'importe où sur le web.

S3 est un composant clé de la plateforme cloud Amazon Web Services (AWS).

AWS Lambda est un service de calcul serverless qui vous permet d'exécuter du code sans provisionner ni gérer de serveurs.

Lambda exécute votre code uniquement lorsque c'est nécessaire et s'adapte automatiquement, de quelques requêtes par jour à des milliers par seconde.

Vous êtes facturé uniquement pour le temps de calcul que vous consommez – il n'y a aucun frais lorsque votre code n'est pas en cours d'exécution.

S3 et Lambda sont deux des services AWS les plus populaires. Ils peuvent être utilisés ensemble pour créer des applications robustes, scalables et économiques.

S3 peut être utilisé pour stocker des données qui sont traitées par des fonctions Lambda.

L'architecture pilotée par les événements de Lambda s'interface de manière transparente avec les événements S3, permettant aux développeurs de déclencher facilement des fonctions serverless en réponse aux changements dans les buckets S3. Cela vous permet de construire des applications qui traitent automatiquement les données dès qu'elles sont ajoutées à S3.

Ce tutoriel vous apprendra à lire un fichier CSV depuis un bucket S3 dans AWS Lambda en utilisant la bibliothèque `requests` ou la bibliothèque `boto3`.

## Comment créer un rôle d'exécution Lambda avec des permissions de lecture S3

Pour que le service Lambda puisse lire les fichiers depuis le bucket S3, vous devez créer un rôle d'exécution lambda qui a des permissions de lecture S3.

Pour créer un rôle d'exécution lambda :

1. Connectez-vous à la Console AWS et accédez à la console Identity and Access Management (IAM)
2. Cliquez sur Rôles puis sur Créer un rôle :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-52.png)
_Créer un rôle_

3. Choisissez AWS service comme Entité de confiance et Lambda comme Cas d'utilisation comme montré dans l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-54.png)
_Sélectionner l'Entité de confiance et le Cas d'utilisation_



4. Ajoutez la politique AmazonS3ReadOnlyAccess pour un accès S3 en lecture seule :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-56.png)
_Ajout de permissions_

5. Donnez un nom et une description au rôle et passez en revue les politiques attachées. Enfin, cliquez sur Créer un rôle pour créer le rôle IAM comme montré dans l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-58.png)
_Création du rôle_

Pour attacher le rôle à la fonction Lambda :

1. Allez à votre fonction Lambda dans la console Lambda si elle existe déjà, ou créez une fonction Lambda si vous devez en créer une nouvelle
2. Dans la section Rôle d'exécution, cliquez sur Modifier
3. Choisissez le rôle IAM que vous avez créé
4. Enregistrez pour attacher le rôle à votre fonction Lambda :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-59.png)
_Attacher le rôle à la fonction Lambda_

Maintenant, voyons comment lire un fichier CSV.

## Comment lire un fichier CSV depuis un bucket S3 en utilisant la bibliothèque Requests dans AWS Lambda

La bibliothèque Requests est un module Python populaire pour effectuer des requêtes HTTP et interagir avec des services web.

Elle simplifie le processus d'envoi de requêtes HTTP, de gestion des réponses et de gestion de divers aspects de la communication web.

Avec une API facile à utiliser et intuitive, Requests permet aux développeurs d'envoyer des requêtes `GET`, `POST`, `PUT`, `DELETE`, et d'autres requêtes HTTP avec un minimum de code. Cela en fait un outil précieux pour des tâches telles que la récupération de données web, l'interaction avec des API RESTful, et plus encore.

Vous pouvez utiliser la bibliothèque requests pour envoyer une requête `GET` et lire un fichier CSV depuis un bucket S3.

Une fois la requête `GET` terminée, vous recevrez une réponse avec des codes de réponse appropriés.

Si la requête get est réussie, elle retournera le code de statut `200`. Vous pouvez obtenir les données à partir de `response.text`.

Le code suivant montre comment envoyer la requête `GET` et lire la réponse :

```python
response = requests.get(url)

if response.status_code == 200:
    # Analyser les données CSV à partir du contenu de la réponse
    csv_data = response.text
```

Ensuite, utilisez le lecteur `CSV` pour lire le contenu CSV à partir de `csv_data` et itérez sur l'objet lecteur pour accéder à chaque ligne du fichier CSV :

```python
    reader = csv.reader(csv_data.splitlines())
    
    for row in reader:
        
        print(row)
```

Le code suivant montre le programme complet pour obtenir le fichier CSV depuis S3 en utilisant la bibliothèque requests :

```python
import requests

import csv

# URL du fichier CSV
url = "https://mrcloudgurudemo.s3.us-east-2.amazonaws.com/sample_csv.csv"

try:
    # Envoyer une requête HTTP GET à l'URL
    response = requests.get(url)
    
    # Vérifier si la requête a réussi (code de statut HTTP 200)
    if response.status_code == 200:
        # Analyser les données CSV à partir du contenu de la réponse
        csv_data = response.text
        
        # Vous pouvez maintenant traiter les données CSV comme nécessaire
        # Par exemple, vous pouvez utiliser csv.reader pour lire les données
        reader = csv.reader(csv_data.splitlines())
        
        # Itérer à travers les lignes dans le CSV
        for row in reader:
            # Traiter chaque ligne comme nécessaire
            print(row)
    else:
        print(f"Échec de la récupération des données. Code de statut : {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")


```

Sortie :

```
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']
    ['4.9', '3', '1.4', '0.2', 'Iris-setosa']
    ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa']
    ['4.6', '3.1', '1.5', '0.2', 'Iris-setosa']
    ['5', '3.6', '1.4', '0.2', 'Iris-setosa']

```

Notez que si vous utilisez la bibliothèque `requests` version 2.30.0 dans AWS lambda, vous pourriez obtenir une erreur [Cannot Import Name DEFAULT_CIPHERS from urllib3.util.ssl_](https://www.mrcloud.guru/solve-error-cannot-import-name-default-ciphers-from-urllib3-util-ssl-aws-lambda/) lorsque l'une des bibliothèques dépendantes essaie d'importer la variable `default_ciphers` depuis `urllib3`.

Vous pouvez résoudre cette erreur en rétrogradant la bibliothèque requests à la version 2.29.0.

## Comment lire un fichier CSV en utilisant la méthode `get_Object()` du client Boto3 dans AWS Lambda

La deuxième option pour lire un fichier CSV est d'utiliser la bibliothèque [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

Boto3 est le SDK AWS pour Python. Il fournit une API orientée objet ainsi qu'un accès de bas niveau aux services AWS.

Boto3 facilite la création, la configuration et la gestion des ressources AWS depuis vos applications Python.

Par exemple, vous pouvez [lire le contenu d'un fichier depuis un bucket S3](https://www.mrcloud.guru/reading-file-content-from-aws-s3-bucket-using-boto3/) de manière programmatique.

Notez que pour interagir avec le service AWS en utilisant Boto3, vous devez [configurer les informations d'identification de sécurité pour éviter l'erreur unable to locate credentials](https://www.mrcloud.guru/fix-the-boto3-nocredentialserror-unable-to-locate-credentials-error/).

Vous pouvez configurer les informations d'identification de sécurité en utilisant la commande `aws configure`.

Pour lire un fichier CSV en utilisant la méthode [get_Object()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object.html) du client Boto3 dans AWS Lambda, créez d'abord le client Boto3 :

```
s3 = boto3.client('s3') 

```

Ensuite, invoquez la méthode `get_object()` depuis le client Boto3 et passez le nom du bucket et le nom de l'objet :

```
response = s3.get_object(Bucket=bucket_name, Key=file_key)

```

Maintenant, lisez le corps de la réponse en utilisant `response['Body'].read()` :

```
csv_content = response['Body'].read().decode('utf-8')

```

Utilisez la méthode [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) de la bibliothèque Pandas pour analyser le texte de la réponse en tant que contenu CSV et créer un dataframe pandas à partir de celui-ci. Vous pouvez également imprimer les cinq premières lignes pour voir si les données sont lues avec succès :

```
df = pd.read_csv(io.StringIO(csv_content))
print(df.head(5))

```

Le code suivant montre le programme complet pour lire un fichier CSV depuis un bucket S3 en utilisant Boto3 :

```python
import boto3

import pandas as pd

import io

def lambda_handler(event, context):
    # Initialiser le client S3
    s3 = boto3.client('s3')

    # Spécifier le bucket S3 et la clé de l'objet du fichier CSV
    bucket_name = 'mrcloudgurudemo'
    file_key = 'sample_csv.csv'

    try:
        # Lire le fichier CSV depuis S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        csv_content = response['Body'].read().decode('utf-8')

        # Créer un DataFrame Pandas
        df = pd.read_csv(io.StringIO(csv_content))

        # Vous avez maintenant votre DataFrame (df) pour un traitement ultérieur
        # Exemple : Imprimer les 5 premières lignes
        print(df.head(5))

        return {
            'statusCode': 200,
            'body': 'Fichier lu avec succès dans le DataFrame.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


```

Sortie :

```
sepal_length  sepal_width  petal_length  petal_width      species
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa

```

## Conclusion

Dans cet article, vous avez appris deux méthodes pour lire un fichier CSV depuis un bucket S3 dans AWS Lambda : en utilisant la bibliothèque `requests` et la bibliothèque `Boto3`.

Les deux méthodes sont efficaces et ont leurs propres avantages. La bibliothèque requests est simple et légère, facile à utiliser.

Boto3 est le SDK AWS officiel pour Python et offre un ensemble de fonctionnalités plus complet.

En fin de compte, la meilleure méthode pour lire un fichier CSV depuis S3 dans AWS Lambda dépend de vos besoins spécifiques.

Si vous avez besoin d'une solution simple et facile à utiliser, la bibliothèque `requests` est un bon choix.

Si vous avez besoin d'une solution plus complète et riche en fonctionnalités, alors `Boto3` est un meilleur choix.