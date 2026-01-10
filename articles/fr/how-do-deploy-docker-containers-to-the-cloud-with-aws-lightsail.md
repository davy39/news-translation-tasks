---
title: Guide de déploiement Docker – Comment déployer des conteneurs dans le cloud
  avec AWS Lightsail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-09T22:45:36.000Z'
originalURL: https://freecodecamp.org/news/how-do-deploy-docker-containers-to-the-cloud-with-aws-lightsail
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/ct-yt--containers--3-.png
tags:
- name: AWS
  slug: aws
- name: container
  slug: container
- name: deployment
  slug: deployment
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
seo_title: Guide de déploiement Docker – Comment déployer des conteneurs dans le cloud
  avec AWS Lightsail
seo_desc: "By Marcia Villalba\nContainers have become the de-facto way to develop\
  \ applications nowadays. They provide a standard way to package all the dependencies\
  \ that your application needs. \nBut how you deploy a containerized application\
  \ to the cloud? The cl..."
---

Par Marcia Villalba

Les conteneurs sont devenus la méthode de facto pour développer des applications de nos jours. Ils fournissent un moyen standard d'emballer toutes les dépendances dont votre application a besoin. 

Mais comment déployer une application conteneurisée dans le cloud ? Le cloud offre une scalabilité, une élasticité et un modèle "payez pour ce que vous utilisez" très souhaitables dans les applications modernes.

Imaginons que vous avez développé votre application et l'avez emballée dans un conteneur Docker. Cette application peut être votre site web, un logiciel que vous développez pour votre entreprise, ou autre chose.

C'est à ce stade que la plupart des tutoriels de base sur les conteneurs et Docker s'arrêtent. Mais vous voulez déployer votre application quelque part pour que d'autres puissent l'utiliser. Vous devrez maintenant commencer à apprendre Kubernetes et tous les systèmes d'orchestration complexes. Ils semblent si compliqués pour simplement déployer une application simple.

Vous savez que le cloud est le meilleur endroit pour déployer votre application. Pourtant, la plupart des services cloud sont complexes.

Pour les utiliser, vous devez connaître des concepts cloud spécifiques tels que la mise en réseau, les types d'instances, et autres. Tant de défis, et vous voulez simplement déployer une application web simple.

Et si je vous disais qu'il existe un service cloud que vous pouvez utiliser pour déployer vos conteneurs de manière simple ? Un service qui offre tous les avantages du cloud, et vous n'avez pas besoin d'utiliser un système d'orchestration complexe pour gérer les charges de travail des conteneurs.

Si cela vous intéresse, continuez à lire. Dans cet article, je vais vous présenter Amazon Lightsail. Ensuite, je vous montrerai une démonstration sur la façon de déployer une application conteneurisée sur AWS en utilisant Lightsail.

## Qu'est-ce qu'AWS ?

[AWS signifie Amazon Web Services](https://aws.amazon.com/) et est la plateforme cloud la plus largement adoptée. Elle dispose de nombreux services différents qui vous aident à développer et à héberger vos applications.

L'utilisation du cloud pour vos applications présente de nombreux avantages par rapport à l'utilisation de vos propres serveurs sur site. Par exemple, cela vous aide à réduire les coûts de votre application, à devenir plus agile et à innover plus rapidement.

## Qu'est-ce qu'Amazon Lightsail ?

[Amazon Lightsail](https://aws.amazon.com/lightsail/) fait partie des offres cloud d'AWS. C'est un service qui fournit tout ce dont vous avez besoin pour déployer des applications et des sites web dans le cloud de manière simple et économique.

Même la tarification est simplifiée – vous savez chaque mois exactement ce que vous payez. Amazon Lightsail est un moyen idéal pour déployer des applications et des sites web simples et pour commencer avec AWS.

Lightsail est alimenté sous le capot par des services AWS tels que les machines virtuelles ([Amazon EC2](https://aws.amazon.com/ec2/)), les bases de données relationnelles ([Amazon RDS](https://aws.amazon.com/rds/)), et d'autres services. Il offre le même niveau de scalabilité, de fiabilité et de sécurité que vous attendez de tout autre service AWS.

Fin 2020, [Lightsail a ajouté la prise en charge du déploiement de conteneurs dans le cloud](https://aws.amazon.com/blogs/aws/lightsail-containers-an-easy-way-to-run-your-containers-in-the-cloud/). Pour ce faire, il vous suffit de fournir une image Docker pour vos conteneurs et Lightsail la déployera automatiquement pour vous.

Lightsail fournit un point de terminaison HTTPS prêt à servir votre application. Il gère également l'équilibrage de charge et l'orchestration de l'application.

## Comment déployer une application avec Lightsail

Voyons comment fonctionne Lightsail en déployant une simple application NodeJS emballée sous forme d'image de conteneur. Cette image est celle que [Docker Desktop fournit](https://www.docker.com/101-tutorial) pour apprendre leur plateforme.

Nous commencerons cette démonstration là où la plupart des tutoriels s'arrêtent – lorsque votre image d'application est hébergée dans [Docker Hub](https://hub.docker.com/).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/docker1010.png)

### Étape 1 - Configurer votre compte AWS

La première étape de ce tutoriel consiste à obtenir un [compte AWS](https://portal.aws.amazon.com/billing/signup). Dans ce compte AWS, vous déployerez vos conteneurs.

Si vous venez de créer votre compte, le [niveau gratuit](https://aws.amazon.com/free/) devrait suffire pour ce projet. Le niveau gratuit vous donnera accès à de nombreux services AWS gratuitement pendant les 12 premiers mois. Et vous obtiendrez un mois d'Amazon Lightsail gratuitement.

Gardez à l'esprit que la possession d'un compte AWS est gratuite si vous n'utilisez aucun service. Vous ne serez pas facturé pour la création du compte, et si vous n'utilisez pas le compte, rien ne sera facturé.

Pour créer un compte AWS, vous pouvez suivre les étapes de cette vidéo :

%[https://www.youtube.com/watch?v=9_wo0FHtVmY]

### Étape 2 - Créer votre service de conteneur

À ce stade, vous devriez avoir un compte AWS et votre application dans Docker Hub - comme le montre ce [tutoriel Docker Desktop](https://www.docker.com/101-tutorial).

Connectez-vous à votre compte AWS et allez sur Amazon Lightsail.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/01lightsail.png)

L'interface d'Amazon Lightsail est assez différente de l'interface AWS régulière. Vous pouvez voir que cette interface dispose de nombreux onglets disponibles. Celui qui nous intéresse pour cet article est **Conteneurs**. Mais de manière similaire, vous pouvez créer des instances virtuelles, des bases de données et d'autres composants cloud en utilisant Lightsail.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/02lightsail.png)

Maintenant, nous pouvons **créer un service de conteneur**, ce qui nous amènera à un formulaire où nous devons prendre quelques décisions simples.

La première consiste à choisir dans quelle région nous voulons déployer notre image de conteneur. Amazon Lightsail est disponible dans toutes ces régions, vous pouvez donc choisir celle qui est la meilleure pour votre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/03lightsail.png)

Ensuite, nous devons choisir la puissance à donner à la machine qui exécutera notre application conteneurisée. Nous devons décider de la taille de la machine et du nombre de machines dont nous avons besoin.

Vous pouvez voir combien cela coûtera par machine et combien de mémoire et de CPU chacune d'elles possède. De plus, après avoir sélectionné l'échelle, vous pouvez voir exactement combien ce service coûtera.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/04lightsail.png)

Lightsail est très clair en ce qui concerne les coûts. Nous pouvons voir le coût final à l'écran. Cela inclut le stockage, l'équilibrage de charge, la mise en réseau et tout ce dont ce conteneur a besoin pour fonctionner.

Ensuite, nous devons configurer notre déploiement. Le service de conteneur que nous créons peut contenir jusqu'à 10 images de conteneurs.

Pour chacun des conteneurs, nous devons définir un nom, l'emplacement de l'image (l'URL de Docker Hub) et comment nous allons exécuter et accéder à cette application.

Dans notre cas, nous ouvrirons le port 3000 avec le protocole HTTP afin que l'application puisse être accessible via cette URL.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/05lighsail.png)

La dernière chose que nous devons configurer est un **point de terminaison public**. Vous pouvez choisir dans votre déploiement quel conteneur vous souhaitez rendre accessible via un point de terminaison public sur Internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/06lightsail.png)

Après cela, vous êtes prêt à **démarrer** le déploiement. Cela prend quelques minutes. Une fois terminé, vous pouvez accéder au point de terminaison public de ce service.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/07lightsail.png)

En haut de la page du service de conteneur, vous pouvez voir le **domaine public**. Lorsque vous cliquez sur cette URL, vous accéderez à l'application que vous avez définie dans le point de terminaison public.

Si vous avez besoin que vos conteneurs communiquent entre eux sans les rendre publics, utilisez le **domaine privé**.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/08lightsial.png)

## Conclusion

Vous avez maintenant une application conteneurisée déployée dans le cloud. Cette application est scalable. Vous pouvez surveiller l'utilisation de la puissance que vous avez définie précédemment dans l'onglet **Métriques**. Vous pouvez toujours modifier ces spécifications si vous voyez que vous avez besoin de plus ou moins de puissance.

De plus, si vous avez besoin d'un domaine pour votre application, vous pouvez en obtenir un depuis la [console Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-dns-in-amazon-lightsail).

Si vous souhaitez regarder cet article de blog sous forme de vidéo, vous pouvez le consulter ici où nous faisons la même chose ensemble. [Cette vidéo est également disponible en espagnol si vous préférez](https://www.youtube.com/watch?v=V-C_ZJi6-o0&t=432s).

%[https://youtu.be/xMudAoq-vmI]

Merci d'avoir lu.

Je suis Marcia Villalba, Developer Advocate pour AWS et l'hôte d'une chaîne YouTube appelée FooBar. J'y ai publié plus de 300 tutoriels vidéo sur Serverless, AWS et les pratiques d'ingénierie logicielle.

* Twitter : [https://twitter.com/mavi888uy](https://twitter.com/mavi888uy)
* YouTube : [https://youtube.com/foobar_codes](https://youtube.com/foobar_codes)
* Chaîne YouTube en espagnol : [https://bit.ly/aws-esp-yt](https://bit.ly/aws-esp-yt)