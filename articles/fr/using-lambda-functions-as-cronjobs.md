---
title: Tutoriel sur les fonctions Cron Job AWS Lambda – Comment planifier des tâches
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T22:25:15.000Z'
originalURL: https://freecodecamp.org/news/using-lambda-functions-as-cronjobs
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/aws-lambda
seo_title: Tutoriel sur les fonctions Cron Job AWS Lambda – Comment planifier des
  tâches
---

deno.png
étiquettes:
- nom: AWS
  slug: aws
- nom: aws lambda
  slug: aws-lambda
seo_title: null
seo_desc: "Par Marcia Villalba\nLes cron jobs sont généralement utilisés pour planifier des commandes à\
  \ un moment spécifique. Vous pouvez les utiliser pour des tâches comme l'exécution de sauvegardes, la surveillance de\
  \ l'état du système ou l'exécution de tâches de maintenance du système. \nLes cron jobs sont une\
  \ utilité pratique pour les administrateurs système..."
---

Par Marcia Villalba

Les cron jobs sont généralement utilisés pour planifier des commandes à un moment spécifique. Vous pouvez les utiliser pour des tâches comme l'exécution de sauvegardes, la surveillance de l'état du système ou l'exécution de tâches de maintenance du système. 

Les cron jobs sont une utilité pratique pour les administrateurs système. Et lorsque vous administrez un système dans le cloud, les cron jobs sont toujours très utiles – vous devez toujours effectuer de nombreuses tâches administratives sur vos systèmes. 

Une façon d'exécuter des cron jobs dans le cloud est d'utiliser une fonction en tant que service (FaaS), comme Lambda dans l'écosystème AWS. 

Les fonctions s'exécutent lorsqu'elles sont déclenchées pour le faire, et elles exécutent du code dans le cloud sans avoir besoin de provisionner ou de maintenir une infrastructure. De plus, les fonctions peuvent être configurées pour s'exécuter à un certain moment ou avec une certaine périodicité, comme les cron jobs traditionnels. 

Dans cet article de blog, je vais utiliser l'écosystème AWS pour vous montrer un exemple concret de la création d'un cron job utilisant une fonction dans le cloud. 

## Événements Amazon CloudWatch

Pour utiliser une fonction Lambda comme un cron job, nous devons comprendre les événements Amazon CloudWatch. 

Les événements Amazon CloudWatch sont envoyés lorsqu'il y a des changements dans les ressources AWS. Ces événements peuvent déclencher une fonction AWS Lambda. Lorsque vos ressources AWS changent d'état, elles envoient automatiquement des événements CloudWatch au flux d'événements. 

Par conséquent, vous pouvez créer une règle qui déclenche une fonction Lambda spécifique lorsque quelque chose se produit. Par exemple, vous pouvez invoquer automatiquement une fonction Lambda lorsqu'il y a un changement dans un groupe AutoScaling. 

De plus, les événements CloudWatch peuvent invoquer une fonction Lambda pour s'exécuter selon un calendrier régulier. Et de cette manière, vous pouvez avoir, par exemple, une fonction Lambda qui éteint toutes vos instances EC2 de test et de développement après 18h et une autre qui les allume après 8h. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/diagram2.png)
_Quand il y a un changement dans un groupe autoscaling, l'événement cloud watch généré déclenche une fonction Lambda_

## Configuration de la démonstration

Je veux vous montrer un exemple de fonction Lambda qui peut effectuer des actions sur vos instances EC2. J'utiliserai [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) pour définir ma fonction Lambda en tant qu'infrastructure en tant que code. 

Si vous souhaitez essayer cette démonstration, vous devez avoir un compte AWS et une ou plusieurs instances EC2 configurées dans votre compte AWS. Ce sont celles que nous allons manipuler depuis les fonctions Lambda. Les instances EC2 sont la version AWS des machines virtuelles dans le cloud.

Vous pouvez essayer la démonstration sur [AWS Cloud9 IDE](https://aws.amazon.com/cloud9/) (un IDE basé sur un navigateur), car AWS SAM est déjà configuré dans cet IDE. Si vous souhaitez savoir comment utiliser AWS Cloud9 IDE pour opérer des fonctions Lambda, vous pouvez consulter cette [vidéo](https://youtu.be/JmEMBxfYtf4). 

%[https://www.youtube.com/watch?v=JmEMBxfYtf4&feature=youtu.be]

Dans cet exemple, nous allons démarrer et arrêter des instances EC2 en utilisant deux fonctions AWS Lambda différentes qui sont déclenchées à un moment donné. Nous démarrons les instances à 8h tous les jours et les éteignons à 18h lorsque la journée est terminée. 

Pour cela, nous allons utiliser un événement CloudWatch pour déclencher la Lambda au bon moment et également le SDK AWS pour effectuer les opérations sur les instances. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/digram1-1.png)
_À un moment spécifique, une fonction Lambda est déclenchée et opérera sur un ensemble d'instances EC2_

Le code finalisé pour cet exemple est disponible dans ce [dépôt GitHub](https://github.com/mavi888/lambda-cronjobs). Pour faire fonctionner ce code dans AWS Cloud9 IDE, vous devez [configurer votre compte GitHub](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) dans l'IDE pour pouvoir cloner le projet, puis le cloner à l'intérieur de l'IDE.

Lorsque vous êtes prêt, exécutez simplement cette commande dans le répertoire cloné :

```
$ sam deploy --guided
```

Lorsque vous exécutez cette commande, vous obtiendrez une série de questions auxquelles vous devez répondre pour configurer ce projet afin qu'il s'exécute avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/video1-1.gif)
_Comment déployer le projet dans le cloud en utilisant AWS SAM CLI_

La première chose que vous devez définir est un **nom** pour votre projet. Ensuite, vous définirez la **région** où il est déployé - choisissez la même région où se trouvent vos instances EC2. Ensuite, nous devons donner au script de déploiement une **liste des instances** que nous voulons manipuler. Et puis nous avons terminé – il déployera le projet dans notre compte AWS.

## Définition de la fonction AWS Lambda

La première chose que je veux vous montrer est comment nous définissons une fonction AWS Lambda qui est déclenchée à un moment spécifique en utilisant AWS SAM. Cette définition sera dans le fichier appelé "template.yml". 

![Image](https://lh5.googleusercontent.com/bnnu336j4GcilKLBDIoohJH18ba3KNJUW71fNnD06vaZReh4EpEAQIJRIufYovNDvU9ARKTiyZZmFO4wUrT7u9yXY9wVh8RCvLZ77xnwQ7Q4Yw30H5-Uh8mBi3SgDAhgaOdKq2uq)
_AWS SAM de la fonction StartInstance_

Voici à quoi ressemble une fonction. Examinons les lignes importantes : 

La première ligne est le nom de la fonction, dans ce cas "**StartInstanceFunction**".

Ensuite, nous avons la définition "**Properties**". La première propriété est "**Handler**". Ici, nous spécifierons le module (fichier) où se trouve le code qui doit être exécuté, puis la méthode à l'intérieur de ce module. 

Ensuite, nous avons "**CodeUri**", qui est le chemin qui vous montre où trouver ce fichier. Dans ce cas, notre code sera à l'intérieur d'un répertoire appelé "cron" dans un fichier appelé "handler.js" et dans une méthode appelée "startInstance". 

Après cela, nous avons la définition "**Runtime**". J'utiliserai NodeJS version 12, mais vous pouvez utiliser Python, Java, Go, C#, ou tout ce qui vous rend heureux. [Lambda prend en charge plusieurs runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) et [vous pouvez apporter votre propre runtime](https://youtu.be/MS5pzddwwqU) si vous le souhaitez.

Ensuite, nous avons la définition "**Environment**" que nous utiliserons pour définir la variable d'environnement. Cette variable nous permettra d'envoyer dynamiquement différents identifiants d'instances au code, en fonction de la configuration lors du déploiement. 

Après cela, nous avons une section appelée "**Policies**" où nous définissons les permissions que cette fonction Lambda particulière aura. 

Il est important de savoir que toutes les fonctions Lambda sont créées sans aucune permission. Cela signifie qu'elles ne peuvent rien faire sur aucune autre ressource AWS. 

Pour que cette fonction Lambda démarre une instance EC2, elle a besoin de permissions pour effectuer cette action particulière sur cette ressource AWS particulière. Dans cette politique particulière, nous accordons des permissions pour démarrer TOUTES les instances EC2 dans ce compte AWS. TOUTES est représenté par le "*" dans la section des ressources. 

Si vous avez ce morceau de code en production, je vous recommande de limiter les ressources exactement à celles que vous voulez que cette Lambda puisse démarrer.

Et enfin, la dernière section est la section "**Events**". Ici, nous définirons comment cette fonction Lambda sera déclenchée. Cette fonction sera déclenchée avec un événement CloudWatch planifié qui déclenche la Lambda tous les jours à 8h du matin. Basiquement, à 8h tous les jours, elle allumera toutes les instances EC2 que vous spécifiez. 

Il existe de nombreuses règles pour former cette expression cron : par exemple, pour dire que vous souhaitez que cela s'exécute uniquement du lundi au vendredi, écrivez cron(0 8 ? * MON-FRI *). Vous pouvez trouver plus d'informations sur le site de documentation des événements CloudWatch ici : [https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html).

## Codage de la fonction AWS Lambda

Maintenant que nous avons défini la fonction Lambda, nous devons lui fournir du code. Dans le dossier "cron", dans le fichier "handler.js", nous devons ajouter la méthode appelée "**startInstance**" qui ressemble à ceci :  

![Image](https://lh6.googleusercontent.com/vZxQeuu9uphLodP3t-eEqtJ-fAxN4HMOsIcKgRq9Nmq5yCCyJCw_BE5U57pMiPLfG_uaoDhH4r0bboqo5MVfgDQ92td0dkvlNEBbhE2r5qUjoAvbWGDHQsOzBDWmA-DYJosJfL7T)
_Code de la fonction startInstance_

Cette méthode sera appelée lorsque la fonction est déclenchée tous les jours à 8h. Elle obtiendra la liste des instances EC2 à partir d'une variable d'environnement que nous avons passée tous les identifiants d'instances lors du déploiement. Ensuite, elle créera un tableau de celles-ci.

Lorsque cela est fait, elle appellera le SDK AWS et enverra le tableau des identifiants d'instances en tant que paramètre. Et s'il y a une erreur, elle la journalisera et terminera. Immédiatement après que cette Lambda termine son exécution, vous pouvez aller dans votre console EC2 et voir comment vos instances s'allument. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/start-instances.gif)
_Les instances EC2 démarrent automatiquement lorsque la fonction Lambda s'exécute_

La fonction pour éteindre les instances EC2 est très similaire avec quelques différences. Vous pouvez trouver le code pour cette fonction dans ce [lien](https://github.com/mavi888/lambda-cronjobs) et le consulter.

## Exécution du cron job

Pour exécuter ce cron job, il n'y a pas grand-chose à faire. Après que les deux fonctions sont déployées dans votre compte AWS, dans la même région que vos instances, elles s'exécuteront et feront ce pour quoi elles ont été programmées. 

![Image](https://lh3.googleusercontent.com/6gytkHs7wXgfKfc0-1IHBjl29miSOSm-8OeidooPaowAIJkHY_v11IIDfoEVJavCGANraYs8I_UvwjICWXQ3yHPfNJTporV8raxxDqZas7JyjCFEpjCMcAteUgitI2U1h7mKRf3E)
_Fonctions AWS Lambda pour démarrer et arrêter les instances déployées dans mon compte AWS_

Maintenant, vous devez attendre jusqu'à 8h ou 18h pour voir si elles fonctionnent. Ou si vous voulez les tester maintenant, changez l'heure de l'événement dans la définition Lambda à une heure qui vous convient. Assurez-vous que l'instance est allumée si vous prévoyez de les éteindre ou inversement, afin que vous puissiez voir les changements. 

Maintenant, attendez et voyez ce qui se passe dans la console EC2. Juste après l'heure que vous avez définie, vous verrez l'instance s'éteindre ou s'allumer, puis faire l'inverse à l'autre heure que vous avez définie. Cela continuera indéfiniment jusqu'à ce que vous supprimiez les fonctions Lambda.

## Nettoyage de votre compte AWS

Après avoir terminé cette démonstration, je vous recommande d'éteindre (ou de supprimer l'instance que vous avez créée pour le test) et de supprimer les fonctions Lambda que vous venez de créer. 

Supprimer les fonctions lambda est aussi simple que d'aller dans votre service CloudFormation dans votre console de gestion AWS et de supprimer la pile de ressources qu'AWS SAM a créée. 

N'oubliez pas non plus de terminer et de supprimer les instances EC2 si vous les avez créées pour cette démonstration.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/delete-lambda.gif)
_Comment supprimer les fonctions AWS Lambda que nous avons créées dans cette démonstration_

## Pour conclure

Les fonctions AWS Lambda sont un outil très utile pour effectuer toutes sortes de tâches dans votre compte AWS. Vous pouvez essentiellement recevoir des notifications de tout changement dans les ressources AWS via les événements CloudWatch, puis vous pouvez accéder à presque tous les services en utilisant le SDK AWS. Ainsi, vous pouvez effectuer toutes sortes de tâches de maintenance et de tâches automatisées sur votre infrastructure.

**Merci d'avoir lu.**

Je suis Marcia Villalba, Developer Advocate pour AWS et l'hôte d'une chaîne YouTube appelée FooBar où j'ai plus de 250 tutoriels vidéo sur Serverless, AWS et les pratiques d'ingénierie logicielle.

* Twitter: [https://twitter.com/mavi888uy](https://twitter.com/mavi888uy)
* YouTube: [https://youtube.com/foobar_codes](https://youtube.com/foobar_codes)