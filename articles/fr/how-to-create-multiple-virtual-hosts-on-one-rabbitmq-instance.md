---
title: Comment créer plusieurs hôtes virtuels sur une seule instance RabbitMQ
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-26T21:25:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-multiple-virtual-hosts-on-one-rabbitmq-instance
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Untitled-design.png
tags:
- name: distributed systems
  slug: distributed-systems
- name: message broker
  slug: message-broker
- name: Python
  slug: python
- name: rabbitmq
  slug: rabbitmq
seo_title: Comment créer plusieurs hôtes virtuels sur une seule instance RabbitMQ
seo_desc: "By Ridwan Yusuf\nHi, friends, and welcome to another tutorial. We'll be\
  \ talking about RabbitMQ, a tool that is widely used as a message broker in distributed\
  \ and Pub-Sub systems. \nWhile multiple applications can share a single RabbitMQ\
  \ instance, it's ..."
---

Par Ridwan Yusuf

Bonjour, amis, et bienvenue dans un autre tutoriel. Nous allons parler de RabbitMQ, un outil largement utilisé comme courtier de messages dans les systèmes distribués et Pub-Sub.

Bien que plusieurs applications puissent partager une seule instance RabbitMQ, il est judicieux de la configurer pour avoir différents hôtes virtuels pour chaque application.

Une utilisation pratique dans une application Python est de l'utiliser comme URL de courtier Celery ou simplement comme file d'attente de messages.

L'un des avantages est qu'il permet d'économiser les coûts liés à la création de plusieurs instances de RabbitMQ. La création d'hôtes virtuels RabbitMQ est similaire, que ce soit localement ou lors de l'exécution dans une solution auto-gérée telle que AWS RabbitMQ.

À la fin de ce guide, vous serez en mesure de :

1. Créer plusieurs hôtes virtuels pour une seule instance RabbitMQ.
2. Tester les connexions en utilisant les bonnes informations d'identification, c'est-à-dire l'utilisateur, le mot de passe et l'hôte virtuel.

**Prérequis pour suivre ce tutoriel** :

1. Assurez-vous d'avoir Docker et Docker Compose installés, ou
2. Avoir une instance RabbitMQ auto-gérée à partir d'AWS, CloudAMQP ou tout autre fournisseur de services.

Sans plus tarder, commençons.

## Comment exécuter une instance RabbitMQ localement

Pour simplifier les choses, nous allons exécuter l'instance RabbitMQ dans un conteneur Docker.

Créez un fichier nommé docker-compose.yml et mettez-le à jour avec le contenu suivant :

_docker-compose.yml_

```yaml
version: "3.8"
services:
  rabbitmq:
    image: rabbitmq:3.8-management-alpine
    container_name: 'rabbitmq_test'
    environment:
      - RABBITMQ_DEFAULT_USER=sampleuser
      - RABBITMQ_DEFAULT_PASS=samplepassword
    ports:
        - 5672:5672
        - 15672:15672
    volumes:
      - ~/.docker-conf/rabbitmq/data/:/var/lib/rabbitmq/
      - ~/.docker-conf/rabbitmq/log/:/var/log/rabbitmq
```

Pour démarrer le conteneur, exécutez cette commande dans le terminal :

```yaml
docker-compose up
```

Une fois le conteneur démarré et en cours d'exécution, accédez à l'interface graphique en visitant ce lien : [http://localhost:15672/](http://localhost:15672/)

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-2-5cc0fa8243.jpg)
_Page de connexion à l'interface graphique RabbitMQ_

Utilisez les informations d'identification spécifiées dans le fichier docker-compose pour accéder au tableau de bord – "sampleuser" et "samplepassword" dans mon cas.

**Remarque :** Si vous utilisez une instance RabbitMQ auto-gérée à partir d'AWS ou CloudAMQP, la chaîne de connexion RabbitMQ ressemblera à ceci :

amqps://ausername:[apassword@32wewjijiokkoo.mq.eu-west-3.amazonaws.com](mailto:apassword@32wewjijiokkoo.mq.eu-west-3.amazonaws.com):5671

Pour accéder au tableau de bord d'administration RabbitMQ, suivez ces étapes :

1. Visitez l'URL en utilisant le protocole HTTPS : [https://32wewjijiokkoo.mq.eu-west-3.amazonaws.com](https://32wewjijiokkoo.mq.eu-west-3.amazonaws.com)
2. Supprimez le nom d'utilisateur, le mot de passe et le port de l'URL.
3. Après avoir accédé à l'URL, le système vous invitera à entrer le nom d'utilisateur et le mot de passe spécifiés dans la chaîne de connexion RabbitMQ ("ausername" et "apassword" dans ce cas). Fournissez ces informations d'identification pour vous connecter au tableau de bord d'administration.

## Comment créer un hôte virtuel

Une fois connecté, cliquez sur l'onglet "Admin", puis accédez à l'onglet "Virtual Hosts" comme indiqué dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-82232fd2b0.jpg)
_Onglet Virtual Hosts de RabbitMQ_

Cliquez sur "Add a new virtual host", et donnez-lui un nom approprié. Enfin, cliquez sur le bouton "Add virtual host" pour créer le nouvel hôte virtuel.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-26e9083f62.jpg)
_Nouvel hôte virtuel créé_

## Comment créer un nouvel utilisateur

Dans l'onglet Utilisateurs, cliquez sur le bouton "Add a user". Spécifiez un nom d'utilisateur et un mot de passe pour le nouvel utilisateur. Si vous le souhaitez, vous pouvez accorder à l'utilisateur l'accès à l'interface Admin (GUI). Enfin, cliquez sur le bouton "Add user" pour créer le nouvel utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-e787f0c102.jpg)
_Créer un nouvel utilisateur_

## Comment assigner le nouvel utilisateur à l'hôte virtuel créé (Vhost)

Dans l'onglet Utilisateurs, localisez et cliquez sur l'utilisateur précédemment créé, qui s'appelait "user1" dans mon cas.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-cb6b620bdf.jpg)
_Nouvel utilisateur dans la liste des utilisateurs_

Pour le nouvel utilisateur, choisissez l'hôte virtuel "new-virtual-host", puis cliquez sur le bouton "Set permission". Cela accorde à l'utilisateur l'accès à l'hôte virtuel spécifié. Pour confirmer cela, retournez à l'onglet Utilisateurs et vérifiez que l'utilisateur apparaît maintenant avec l'accès à "new-virtual-host".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/WhatsApp-Image-2023-07-25-at-19.59.44.jpeg)
_Assignation du nouvel utilisateur à l'hôte virtuel créé_

À ce stade, le nouvel utilisateur "user1" a été configuré pour accéder à l'hôte virtuel "new-virtual-host".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-26-06-22-12.png)
_Nouvel utilisateur assigné à l'hôte virtuel créé_

## Comment tester la connexion pour le nouvel utilisateur et l'hôte virtuel

Pour tester si le nouvel utilisateur peut accéder au nouvel hôte virtuel, vous pouvez utiliser le script Python suivant. Une fois que tout fonctionne correctement, vous pouvez utiliser la chaîne d'URL pour vous connecter au courtier RabbitMQ dans n'importe quelle application.

_test_rabbit.py_

```python
import pika

def test_rabbitmq_url(url):

    try:
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        connection.close()
        print("Connexion réussie !")

    except pika.exceptions.AMQPError as e:
        print("Échec de la connexion :", e)

test_rabbitmq_url('amqp://user1:password@localhost:5672/new-virtual-host')
```

Remarquez comment nous avons spécifié l'URL RabbitMQ : elle a le nom d'utilisateur "user1" et le mot de passe "password", tandis que l'hôte virtuel est nommé "new-virtual-host".

N'oubliez pas d'installer pika en exécutant `pip install pika` sur la ligne de commande.

Pour exécuter ce script dans le terminal, entrez la commande suivante :

```bash
python test_rabbit.py
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-4dda3c97ef.jpg)
_Connexion réussie à RabbitMQ_

Cela indique une connexion réussie à l'instance RabbitMQ.

Changez le mot de passe dans la fonction utilitaire par un mot de passe incorrect, et vous devriez voir un résultat similaire à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-4-85582a7c7f.jpg)
_Échec de la connexion à RabbitMQ_

## Conclusion

En conclusion, la création de plusieurs hôtes virtuels sur une seule instance RabbitMQ peut considérablement améliorer vos capacités de gestion des files d'attente de messages.

En séparant efficacement les applications et les ressources, vous assurez une meilleure organisation, sécurité et évolutivité. Avec le guide étape par étape fourni dans cet article, vous avez maintenant les connaissances pour exploiter tout le potentiel de RabbitMQ.

Merci d'avoir lu, et j'espère que vous avez apprécié l'article.

Pour plus de contenu intéressant et de conseils, n'hésitez pas à consulter ma collection de vidéos sur [YouTube](https://www.youtube.com/@ridwanray) et envisagez de cliquer sur le bouton d'abonnement.

Vous pouvez également me trouver sur [LinkedIn](https://linkedin.com/in/ridwan-yusufa/).