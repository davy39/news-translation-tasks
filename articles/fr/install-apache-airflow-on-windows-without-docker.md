---
title: Comment installer Apache Airflow sur Windows sans Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-02T00:18:32.000Z'
originalURL: https://freecodecamp.org/news/install-apache-airflow-on-windows-without-docker
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Airflow_Install.png
tags:
- name: apache
  slug: apache
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: Docker
  slug: docker
seo_title: Comment installer Apache Airflow sur Windows sans Docker
seo_desc: "By Aviator Ifeanyichukwu\nApache Airflow is a tool that helps you manage\
  \ and schedule data pipelines. According to the documentation, it lets you \"programmatically\
  \ author, schedule, and monitor workflows.\" \nAirflow is a crucial tool for data\
  \ engineers..."
---

Par Aviator Ifeanyichukwu

Apache Airflow est un outil qui vous aide à gérer et à planifier des pipelines de données. Selon la [documentation](https://airflow.apache.org/), il vous permet de "créer, planifier et surveiller des workflows de manière programmatique".

Airflow est un outil crucial pour les ingénieurs et les scientifiques des données. Dans cet article, je vais vous montrer comment l'installer sur Windows sans Docker.

Bien qu'il soit recommandé d'exécuter Airflow avec Docker, cette méthode fonctionne pour les machines à faible mémoire qui ne peuvent pas exécuter Docker.

### Prérequis :

Cet article suppose que vous êtes familiarisé avec l'utilisation de la ligne de commande et que vous pouvez configurer votre environnement de développement comme indiqué.

### Exigences :

Vous avez besoin de Python 3.8 ou supérieur, Windows 10 ou supérieur, et du sous-système Windows pour Linux (WSL2) pour suivre ce tutoriel.

### Qu'est-ce que le sous-système Windows pour Linux (WSL2) ?

WSL2 vous permet d'exécuter des commandes et des programmes Linux sur un système d'exploitation Windows.

Il fournit un environnement compatible Linux qui s'exécute nativement sur Windows, permettant aux utilisateurs d'utiliser des outils et des utilitaires de ligne de commande Linux sur une machine Windows.

Vous pouvez en lire plus [ici pour installer WSL2](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) sur votre machine.

Avec Python et WSL2 installés et activés sur votre machine, lancez le terminal en recherchant Ubuntu dans le menu démarrer.

## Étape 1 : Configurer l'environnement virtuel

Pour travailler avec Airflow sur Windows, vous devez configurer un environnement virtuel. Pour ce faire, vous devrez installer le package virtualenv.

Note : Assurez-vous d'être à la racine du terminal en tapant :

```
cd ~
```

```
pip install virtualenv
```

Créez l'environnement virtuel comme suit :

```
virtualenv airflow_env
```

Puis activez l'environnement :

```
source airflow_env/bin/activate
```

## Étape 2 : Configurer le répertoire Airflow

Créez un dossier nommé airflow. Le mien sera situé à c/Users/[Username]. Vous pouvez mettre le vôtre où vous préférez.

Si vous ne savez pas comment naviguer dans le terminal, vous pouvez suivre les étapes dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/set-virtual_env-1.png)
_Créer un répertoire Airflow à partir du terminal_

Maintenant que vous avez créé ce dossier, vous devez le définir comme variable d'environnement. Ouvrez un script .bashrc à partir du terminal avec la commande :

```
nano ~/.bashrc
```

Puis écrivez ce qui suit :

```
AIRFLOW_HOME=/c/Users/[YourUsername]/airflow
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/airflow_env_variable.png)
_Configurer le chemin du répertoire Airflow comme variable d'environnement_

Appuyez sur ctrl s et ctrl x pour quitter l'éditeur nano.

Cette partie du répertoire Airflow sera enregistrée en permanence comme variable d'environnement. Chaque fois que vous ouvrez un nouveau terminal, vous pouvez récupérer la valeur de la variable en tapant :

```
cd $AIRFLOW_HOME
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/airflow_home-2.png)
_Naviguer vers le répertoire Airflow en utilisant la variable d'environnement_

## Étape 3 : Installer Apache Airflow

Avec l'environnement virtuel toujours actif et le répertoire courant pointant vers le dossier Airflow créé, installez Apache Airflow :

```
pip install apache-airflow
```

Initialisez la base de données :

```
airflow db init
```

Créez un dossier nommé dags à l'intérieur du dossier airflow. Cela sera utilisé pour stocker tous les scripts Airflow.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/airflow_db_init-1.png)
_Voir les fichiers et dossiers générés par Airflow db init_

## Étape 4 : Créer un utilisateur Airflow

Lorsque Airflow est nouvellement installé, vous devez créer un utilisateur. Cet utilisateur sera utilisé pour se connecter à l'interface utilisateur d'Airflow et effectuer certaines fonctions d'administration.

```
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email youremail@email.com
```

Vérifiez l'utilisateur créé :

```
airflow users list
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/create-users.png)
_Créer un utilisateur Airflow et lister l'utilisateur créé_

## Étape 5 : Exécuter le serveur web

Exécutez le planificateur avec cette commande :

```
airflow scheduler
```

Lancez un autre terminal, activez l'environnement virtuel airflow, cd à $AIRFLOW_HOME, et exécutez le serveur web :

```
airflow webserver
```

Si le port par défaut 8080 est utilisé, changez le port en tapant :

```
airflow webserver --port <port number>
```

Connectez-vous à l'interface utilisateur en utilisant le nom d'utilisateur créé précédemment avec "airflow users create".

Dans l'interface utilisateur, vous pouvez voir les DAGs pré-créés qui viennent avec Airflow par défaut.

## Comment créer le premier DAG

Un DAG est un script Python pour organiser et gérer des tâches dans un workflow.

Pour créer un DAG, naviguez dans le dossier dags créé à l'intérieur du répertoire $AIRFLOW_HOME. Créez un fichier nommé "hello_world_dag.py". Utilisez VS Code si disponible.

Entrez le code de l'image ci-dessous, et enregistrez-le :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/first_dag.png)
_Exemple de script DAG dans l'éditeur VS Code_

Allez dans l'interface utilisateur d'Airflow et recherchez hello_world_dag. Si cela n'apparaît pas, essayez de rafraîchir votre navigateur.

C'est tout. Cela complète l'installation d'Apache Airflow sur Windows.

## Conclusion

Ce guide a couvert comment installer Apache Airflow sur une machine Windows sans Docker et comment écrire un script DAG.

J'espère que les étapes décrites ci-dessus vous ont aidé à installer Airflow sur votre machine Windows sans Docker.

Dans les articles suivants, vous apprendrez les concepts et les composants d'Apache Airflow.

Suivez-moi sur [Twitter](http://twitter.com/aviatorIfeanyi) ou [LinkedIn](https://www.linkedin.com/in/aviatorifeanyi/) pour plus de contenu sur l'ingénierie des données.