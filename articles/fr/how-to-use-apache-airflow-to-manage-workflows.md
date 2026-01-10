---
title: Comment utiliser Apache Airflow pour planifier et gérer des workflows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-13T15:11:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-apache-airflow-to-manage-workflows
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/My-project--1-.jpg
tags:
- name: apache
  slug: apache
- name: Python
  slug: python
- name: workflow
  slug: workflow
seo_title: Comment utiliser Apache Airflow pour planifier et gérer des workflows
seo_desc: 'By Sameer Shukla

  Apache Airflow is an open-source workflow management system that makes it easy to
  write, schedule, and monitor workflows.

  A workflow as a sequence of operations, from start to finish. The workflows in Airflow
  are authored as Directed...'
---

Par Sameer Shukla

Apache Airflow est un système de gestion de workflows open-source qui facilite l'écriture, la planification et la surveillance des workflows.

Un workflow est une séquence d'opérations, du début à la fin. Les workflows dans Airflow sont créés sous forme de graphes acycliques dirigés (DAG) en utilisant la programmation Python standard.

Vous pouvez configurer quand un DAG doit commencer son exécution et quand il doit se terminer. Vous pouvez également configurer la surveillance des workflows via l'interface utilisateur très intuitive d'Airflow.

Vous pouvez être opérationnel sur Airflow en un rien de temps – il est facile à utiliser et vous n'avez besoin que de quelques connaissances de base en Python. Il est également entièrement open-source.

Apache Airflow dispose également d'une collection utile d'opérateurs qui fonctionnent facilement avec les plateformes Google Cloud, Azure et AWS.

Dans cet article, nous allons couvrir :

* Qu'est-ce que les graphes acycliques dirigés (DAG) ?
* Qu'est-ce que les opérateurs ?
* Comment créer votre premier DAG
* Un cas d'utilisation pour les DAG
* Comment installer Cloud Composer
* Comment exécuter le pipeline sur Composer

## Qu'est-ce que les graphes acycliques dirigés, ou DAG ?

Les DAG, ou graphes acycliques dirigés, ont des nœuds et des arêtes. Les DAG ne doivent pas contenir de boucles et leurs arêtes doivent toujours être dirigées.

En bref, un DAG est un pipeline de données et chaque nœud dans un DAG est une tâche. Certains exemples de nœuds sont le téléchargement d'un fichier depuis GCS (Google Cloud Storage) vers un emplacement local, l'application de logique métier sur un fichier en utilisant Pandas, l'interrogation de la base de données, l'envoi d'une requête REST, ou le téléchargement d'un fichier à nouveau vers un bucket GCS.

### Visualisation des DAG

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-47.png)
_DAG correct sans boucles_

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-48.png)
_DAG incorrect avec boucle_

Vous pouvez planifier des DAG dans Airflow en utilisant l'attribut schedule_interval. Par défaut, il est "None", ce qui signifie que le DAG ne peut être exécuté qu'en utilisant l'interface utilisateur d'Airflow.

Vous pouvez planifier le DAG pour qu'il s'exécute une fois par heure, chaque jour, une fois par semaine, chaque mois, chaque année ou selon vos souhaits en utilisant les options de préréglages cron (@hour, @daily, @weekly, @hourly, @monthly, @yearly).

Si vous devez exécuter le DAG toutes les 5 minutes, toutes les 10 minutes, chaque jour à 14h00, ou une fois à un moment spécifique comme chaque jeudi à 10h00, alors vous devez utiliser ces expressions basées sur cron.

*/5 * * * * = Toutes les 5 minutes

0 14 * * * = Chaque jour à 14h00

## Qu'est-ce que les opérateurs ?

Un DAG se compose de plusieurs tâches. Vous pouvez créer des tâches dans un DAG en utilisant des opérateurs qui sont des nœuds dans le graphe.

Il existe divers opérateurs prêts à l'emploi disponibles dans Airflow, tels que :

* LocalFilesystemToGCSOperator – utilisez-le pour télécharger un fichier depuis un système local vers un bucket GCS.
* PythonOperator – utilisez-le pour exécuter des fonctions appelables en Python.
* functionEmailOperator – utilisez-le pour envoyer un email.
* SimpleHTTPOperator – utilisez-le pour faire une requête HTTP.

## Comment créer votre premier DAG

Le DAG d'exemple que nous allons créer se compose d'un seul opérateur (l'opérateur Python) qui exécute une fonction Python.

```python
from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

def message():
    print("Premier DAG exécuté avec succès !!")

with DAG(dag_id="FirstDAG", start_date=datetime(2022,1,23), schedule_interval="@hourly",
         catchup=False) as dag:

    task = PythonOperator(
        task_id="task",
        python_callable=message)

task

```

La première étape consiste à importer les modules nécessaires requis pour le développement du DAG. La ligne `with DAG` est le DAG qui est un pipeline de données ayant des paramètres de base comme `dag_id`, `start_date`, et `schedule_interval`.

L'intervalle de planification est configuré comme @hourly, ce qui indique que le DAG s'exécutera chaque heure.

La tâche dans le DAG consiste à imprimer un message dans les logs. Nous avons utilisé ici le PythonOperator. Cet opérateur est utilisé pour exécuter toute fonction Python appelable.

Une fois l'exécution terminée, nous devrions voir le message « Premier DAG exécuté avec succès » dans les logs. Nous allons exécuter tous nos DAGs sur GCP Cloud Composer.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-49.png)
_Interface utilisateur d'Airflow_

Après une exécution réussie, le message est imprimé dans les logs :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-50.png)
_Logs_

## Un cas d'utilisation pour les DAG

Le cas d'utilisation que nous allons couvrir dans cet article implique un processus en trois étapes.

Dans la première étape, nous allons télécharger un fichier .csv dans un bucket GCS d'entrée. Ce fichier doit être traité par PythonOperator dans le DAG. La fonction qui sera exécutée par le PythonOperator consiste en du code Pandas, qui représente comment les utilisateurs peuvent utiliser le code Pandas pour transformer les données dans le pipeline de données Airflow.

Dans la deuxième étape, nous allons télécharger le fichier .csv transformé vers un autre bucket GCS. Cette tâche sera gérée par le GCSToGCSOperator.

La troisième étape consiste à envoyer un email de statut indiquant que l'exécution du pipeline est terminée, ce qui sera géré par l'EmailOperator.

Dans ce cas d'utilisation, nous allons également couvrir comment notifier l'équipe par email en cas d'échec d'une étape de l'exécution.

## Comment installer Cloud Composer

Dans GCP, Cloud Composer est un service géré basé sur Apache Airflow. Cloud Composer a une intégration par défaut avec d'autres services GCP tels que GCS, BigQuery, Cloud Dataflow, etc.

Tout d'abord, nous devons créer l'environnement Cloud Composer. Recherchez donc Cloud Composer dans la barre de recherche et cliquez sur "Créer un environnement" comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-51.png)
_Créer un environnement_

Dans l'option Environnements, je sélectionne l'option "Composer 1" car nous n'avons pas besoin de mise à l'échelle automatique.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-54.png)

Une fois que nous avons sélectionné le type de compositeur dont nous avons besoin, nous devons effectuer une configuration de base comme pour tout service géré GCP ("Nom de l'instance", "Emplacement", etc.).

Le nombre de nœuds ici doit toujours être de 3 car GCP configura les 3 services nécessaires pour Airflow.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-56.png)

Une fois cela fait, il configura une instance Airflow pour nous. Pour télécharger un DAG, nous devons ouvrir le dossier DAGs montré dans la section 'Dossier DAGs'.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-57.png)
_Instance Airflow_

Si vous allez dans la section "Kubernetes Engine" sur GCP, nous pouvons voir 3 services en cours d'exécution :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-58.png)
_Kubernetes Engine_

Tous les DAGs résideront dans un bucket créé par Airflow.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-59.png)
_Bucket de l'instance Airflow pour les DAGs_

## Comment créer et exécuter le pipeline sur Composer

Dans le pipeline, nous avons deux buckets. input_csv contiendra le csv qui nécessite une transformation, et le bucket transformed_csv sera l'emplacement où le fichier sera téléchargé une fois la transformation terminée.

Le code complet du pipeline est le suivant :

```python
from airflow import DAG
from datetime import datetime
import pandas as pd

from airflow.utils.email import send_email
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator


def transformation():
    trainDetailsDF = pd.read_csv('gs://input_csv/Event_File_03_16_2022.csv')
    print(trainDetailsDF.head())


with DAG(
        dag_id="pipeline_demo",
        schedule_interval="@hourly",
        start_date=datetime(2022, 1, 23),
        catchup=False
) as dag:
    buisness_logic_task = PythonOperator(
        task_id='ApplyBusinessLogic',
        python_callable=transformation,
        dag=dag)

    upload_task = GCSToGCSOperator(
        task_id='upload_task',
        source_bucket='input_csv',
        destination_bucket='transformed_csv',
        source_object='Event_File_03_16_2022.csv',
        move_object=True,
        dag=dag
    )

    email_task = EmailOperator(
        task_id="SendStatusEmail",
        depends_on_past=True,
        to='youremail',
        subject='Statut du pipeline !',
        html_content='<p>Bonjour à tous, le processus est terminé avec succès ! <p>',
        dag=dag)

    buisness_logic_task >> upload_task >> email_task

```

Dans la première tâche, tout ce que nous faisons est de créer un DataFrame à partir du fichier d'entrée et d'imprimer les éléments de tête. Dans les logs, cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-60.png)
_Tête du DataFrame_

Dans la deuxième tâche, GCSToGCSOperator, nous avons utilisé l'attribut move_object=True qui supprimera le fichier du bucket source.

Une fois que nous avons téléchargé le fichier dans le bucket, nous pouvons voir que le DAG est en cours de planification. Le nom du DAG est "pipeline_demo".

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-61.png)
_DAGs_

Notez que si vous rencontrez des "erreurs d'importation" après avoir téléchargé ou exécuté un DAG, quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-62.png)

Vous pouvez télécharger ces packages manquants via l'option "PYPI Packages" dans GCP. Cela mettra à jour l'environnement après quelques minutes.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-63.png)
_Mise à jour de l'environnement avec les packages manquants_

Pour ouvrir une interface utilisateur Airflow, cliquez sur le lien "Airflow" sous le serveur web Airflow.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-64.png)
_Instance Airflow, cliquez sur le lien Airflow pour ouvrir l'interface utilisateur_

L'interface utilisateur d'Airflow ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-65.png)

Après une exécution réussie du pipeline, voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-66.png)

Afin d'envoyer un email si une tâche échoue, vous pouvez utiliser le on_failure_callback comme ceci :

```python
def notify_email(contextDict, **kwargs):
    title = "Alerte Airflow : {task_name} a échoué".format(**contextDict)
    body = """
    Nom de la tâche : {task_name} a échoué.<br>
    """.format(**contextDict)
    send_email('youremail', title, body)



buisness_logic_task = PythonOperator(
    task_id='ApplyBusinessLogic',
    python_callable=transformation,
    on_failure_callback=notify_email,
    dag=dag)


```

Nous effectuons la configuration de l'email de notification sur Composer via Sendgrid. De plus, une fois que vous avez terminé avec Cloud Composer, n'oubliez pas de supprimer l'instance car elle ne peut pas être arrêtée.

## Conclusion

Apache Airflow est un outil assez facile à utiliser. Il y a aussi beaucoup d'aide disponible sur Internet et la communauté grandit.

GCP a grandement simplifié le travail avec Airflow en créant un service géré séparé pour celui-ci.