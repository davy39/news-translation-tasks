---
title: Notions de base d'AWS pour DevOps - Comment configurer une machine Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-25T14:26:19.000Z'
originalURL: https://freecodecamp.org/news/aws-basics-for-devops
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Getting-Started-With-DevOps--1-.png
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Linux
  slug: linux
seo_title: Notions de base d'AWS pour DevOps - Comment configurer une machine Linux
seo_desc: "By Satyam Tripathi\nTo create an application like WhatsApp or Facebook,\
  \ you'd need many servers (30-40), operating system licenses, routers, cables, switches,\
  \ gateways, air conditioning units, and employees for maintenance. \nAll this can\
  \ be expensive ..."
---

Par Satyam Tripathi

Pour créer une application comme WhatsApp ou Facebook, vous auriez besoin de nombreux serveurs (30-40), de licences de système d'exploitation, de routeurs, de câbles, de commutateurs, de passerelles, d'unités de climatisation et d'employés pour la maintenance.

Tout cela peut être coûteux et prendre du temps, et il n'y a aucune garantie que l'application sera réussie sur le marché.

Mais en utilisant des services cloud comme AWS, vous pouvez éviter les coûts initiaux et la complexité de la construction et de la gestion de votre propre infrastructure de centre de données.

Au lieu de cela, vous pouvez payer pour l'infrastructure sur une base de paiement à l'utilisation, ce qui signifie que vous ne payez que pour les ressources que vous utilisez. Cela rend les choses plus flexibles et abordables.

Dans cet article, vous apprendrez à créer un serveur (instance) sur AWS. Nous verrons également comment se connecter à votre instance AWS en utilisant **Putty**.

Tout d'abord, nous allons configurer le compte AWS. Ensuite, nous créerons une instance. Et enfin, nous configurerons Putty et Puttygen pour exécuter la machine Linux.

Putty et Puttygen sont des outils logiciels gratuits et open source que vous pouvez utiliser pour accéder et gérer des ordinateurs distants.

Putty est un client SSH ou un émulateur de terminal open source qui vous permet d'établir une connexion sécurisée à un ordinateur distant. Il est disponible pour Windows, Linux et macOS.

Puttygen est un générateur de clés utilisé pour créer des clés SSH. Puttygen vous permet de générer de nouvelles paires de clés, d'importer des clés existantes et de convertir des clés entre différents formats.

## Avantages de l'utilisation des services cloud

Les services cloud comme AWS offrent un certain nombre d'avantages qui peuvent faciliter et rendre plus rentable la création d'applications.

* **Coûts initiaux réduits :** Les services cloud comme AWS vous permettent d'éviter les coûts initiaux d'achat et de maintenance de votre propre infrastructure de centre de données.
* **Flexibilité accrue :** Les services cloud peuvent être dimensionnés à la hausse ou à la baisse selon les besoins, ce qui vous donne plus de flexibilité pour répondre à une demande changeante.
* **Fiabilité améliorée :** Les services cloud sont généralement plus fiables que les infrastructures traditionnelles sur site, car ils sont soutenus par plusieurs centres de données.
* **Sécurité renforcée :** Les services cloud offrent un certain nombre de fonctionnalités de sécurité qui peuvent aider à protéger les applications contre les accès non autorisés.

Maintenant, plongeons dans la tâche à accomplir.

## Créer un compte sur AWS

Cliquez sur le bouton **Créer un compte AWS**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--3-.jpg)

Inscription avec votre adresse e-mail. Vous recevrez un code de vérification par e-mail à votre adresse e-mail.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-06-134515.jpg)

Une fois votre adresse e-mail vérifiée, créez un mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-06-150553.jpg)

Maintenant, vous pouvez entrer vos détails personnels et choisir l'option **Personnel - pour vos propres projets**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-06-150826.jpg)

Maintenant, la dernière étape consiste à entrer les informations de votre carte de crédit. Ne vous inquiétez pas, vous ne serez pas facturé.

**Note :** Dans le cadre de l'offre gratuite AWS, vous pouvez commencer à utiliser Amazon EC2 gratuitement. Cela inclut **750** heures d'instances Linux et Windows t2.micro chaque mois pendant un an.

Plus tard, nous discuterons de la manière de terminer vos instances afin de ne pas être facturé. Bien que vous ayez 750 heures à utiliser en un mois, vous devez terminer votre instance créée lorsqu'elle n'est pas utilisée.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-06-150915.jpg)

Félicitations ! Vous avez créé votre compte AWS. Maintenant, reconnectez-vous - assurez-vous de sélectionner le **Root user**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-06-135657.jpg)

Bienvenue sur AWS !

À chaque fois que vous vous connectez, vous pouvez vérifier votre facture en visitant le **Tableau de bord de facturation**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--8-.jpg)

**Note :** Mumbai est la région la plus proche de moi où je vais créer mon serveur. Choisissez donc la région la plus proche de vous en conséquence.

**Pour afficher votre tableau de bord de facturation :**

1. Cliquez sur votre nom en haut à droite de la page.
2. Sélectionnez **Tableau de bord de facturation** dans le menu.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-06-152952.jpg)

Si vous voyez des frais sur votre tableau de bord de facturation, vous pouvez créer un cas. Pour ce faire, accédez au Centre de support AWS et créez un cas.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--6-.jpg)

Choisissez Compte et Facturation, puis sous Service, choisissez Facturation, et sous Catégorie, choisissez Contester une charge.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--7-.jpg)

Notez que vous devez toujours travailler dans la même région. Lorsque vous travaillez dans la même région, vos données n'ont pas besoin de voyager aussi loin, ce qui peut réduire la latence et améliorer les performances.

## Comment lancer l'instance

Pour vous aider à apprendre et à pratiquer DevOps, nous allons créer une machine Linux dans AWS. Linux est le système d'exploitation de choix pour de nombreux praticiens DevOps et est largement utilisé dans les environnements de production.

Pour créer une machine Linux à partir de zéro, cliquez sur le service **EC2** dans la console de gestion AWS.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--9-.jpg)

Cliquez sur l'onglet **Instances**. Actuellement, il y a 0 instance en cours d'exécution, ce qui signifie que nous n'avons aucune instance en cours d'exécution pour le moment.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--10-.jpg)

Cliquez sur le bouton **Lancer les instances** pour démarrer une instance EC2.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--11-.jpg)

Vous pouvez choisir la machine ci-dessous car elle est éligible à l'offre gratuite.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--19-.jpg)

Maintenant, vous devez créer une nouvelle paire de clés. Cette paire de clés sera utilisée lorsque nous exécuterons la machine Linux en utilisant PuTTY. Ici, nous utiliserons PuTTY pour nous connecter à une machine Linux distante.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--20-.jpg)

Pour créer une nouvelle paire de clés, donnez d'abord un nom à la paire de clés. Le type de paire de clés doit être RSA, et le format de fichier de clé privée doit être .pem. Plus tard, vous pouvez utiliser Puttygen pour convertir le format PEM en format PPK. Ensuite, vous pouvez utiliser PuTTY pour ouvrir le fichier .ppk afin d'exécuter une machine Linux.

PPK (Putty Private Key) et PEM (Privacy Enhanced Mail) sont deux formats de fichiers utilisés pour stocker les clés privées utilisées dans l'authentification SSH.

Notez que Putty ne prend en charge que le format PPK, et nous allons utiliser Putty. Par conséquent, vous devrez d'abord convertir votre clé SSH au format PPK.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--23-.jpg)

Si vous retournez au **Tableau de bord EC2**, vous verrez qu'il y a 1 instance en cours d'exécution. Si vous cliquez sur cette instance, vous verrez toutes les informations, telles que l'adresse IPv4 publique et l'ID de l'instance.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--24-.jpg)

Voyez, **2/2 vérifications réussies** signifie que l'instance a été lancée avec succès et est en cours d'exécution. Vous pouvez copier l'adresse IPv4 publique, car vous l'utiliserez lors de la création de la machine Linux en utilisant PuTTY.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--25-.jpg)

Hourra ! L'instance a été lancée avec succès.

## Comment créer la machine Linux

Nous avons réussi à lancer l'instance dans la console AWS. Maintenant, nous allons télécharger PuTTY et PuTTYgen pour exécuter la machine Linux.

Voici le lien de téléchargement : [https://www.puttygen.com/](https://www.puttygen.com/)

### Télécharger Putty et Puttygen

Tout d'abord, téléchargez PuTTY et PuTTYgen. Pour Windows, vous pouvez télécharger les versions suivantes à partir du lien suivant :

Lien de téléchargement : [https://www.puttygen.com/download-putty](https://www.puttygen.com/download-putty)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--26-.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--27-.png)

### Comment configurer Puttygen

Ouvrez PuTTYgen et cliquez sur le bouton Load.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--29-.jpg)

Maintenant, sélectionnez l'option "All files" afin que vous puissiez voir le fichier .pem dans votre système.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--30-.jpg)

Maintenant, enregistrez la clé privée.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--31-.jpg)

Lorsque vous cliquez sur le bouton Save private key, vous verrez une fenêtre pop-up. Cliquez sur le bouton Yes.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--32-.jpg)

Maintenant, donnez un nom à votre clé privée et enregistrez-la au format .ppk. Notez que vous utiliserez ce fichier lorsque nous configurerons PuTTY.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--33-.jpg)

### Comment configurer Putty

Copiez l'adresse IPv4 publique d'AWS et collez-la dans le champ hostname dans la configuration de PuTTY.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--34-.jpg)

Cliquez sur le bouton **+** dans la section **SSH**, puis cliquez sur le bouton **+** dans la section **Auth**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--35-.jpg)

Dans la section **Auth**, cliquez sur **Credentials**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--37--1.jpg)

Lorsque vous cliquez sur **Credentials**, vous verrez l'option **Browse**. Cliquez dessus et parcourez jusqu'au fichier .ppk que vous avez enregistré précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--39-.jpg)

Lorsque vous cliquez sur Accept, vous verrez une nouvelle fenêtre noire s'ouvrir sur votre système. C'est ici que vous pouvez exécuter toutes vos commandes Linux.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--40-.jpg)

Maintenant, vous devez vous connecter en tant que **ec2-user**. Pour Amazon Linux 2 ou l'AMI Amazon Linux, le nom d'utilisateur est **ec2-user**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--41-.png)

Voyez, vous êtes connecté en tant qu'utilisateur ec2-user.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--42-.png)

Pour exécuter des commandes en tant qu'utilisateur root, vous pouvez changer d'utilisateur en utilisant la commande `sudo su`. L'utilisateur root a tous les droits sur le système. Il est important d'utiliser cette commande avec prudence, car tout changement effectué en tant qu'utilisateur root peut avoir un impact significatif sur le système.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--43-.png)

L'invite a changé de `$` à `#`. Cela montre que vous êtes maintenant un utilisateur root et que vous pouvez exécuter n'importe quelle commande sans aucun privilège supplémentaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--45-.png)

Félicitations ! Votre machine Linux est maintenant prête à être utilisée.

## Comment terminer ou arrêter une instance

Terminer une instance signifie supprimer l'instance et toutes ses données associées. Vous ne pouvez pas récupérer une instance terminée.

Arrêter une instance signifie déplacer l'instance vers l'état arrêté, où elle peut être redémarrée plus tard.

**Pour terminer ou arrêter une instance sur AWS :**

1. Allez dans la console Amazon EC2.
2. Dans le volet de navigation, choisissez Instances.
3. Sélectionnez l'instance que vous souhaitez terminer.
4. Choisissez État de l'instance, puis Terminer ou Arrêter l'instance.
5. Dans la boîte de dialogue de confirmation, choisissez Terminer ou Arrêter.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/annotely_image--46-.jpg)

## Conclusion

Dans cet article, nous avons vu comment créer une instance AWS et utiliser PuTTY et PuTTYgen pour lancer une machine Linux distante. Dans les prochains articles, je parlerai plus en détail des commandes Linux.

Vous pouvez me suivre sur Twitter : [@triposat](https://twitter.com/triposat).