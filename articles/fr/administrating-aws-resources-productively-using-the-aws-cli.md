---
title: Comment utiliser l'AWS CLI pour exécuter vos services cloud directement depuis
  votre clavier - aucune interface graphique requise
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-06T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/administrating-aws-resources-productively-using-the-aws-cli
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/aws-cli.png
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
seo_title: Comment utiliser l'AWS CLI pour exécuter vos services cloud directement
  depuis votre clavier - aucune interface graphique requise
seo_desc: I’ll bet you’ve already got some stuff running on AWS and you made it happen
  using the browser console. But I’ll also bet that you already suspect that clicking
  your way through layers and layers of configuration pages isn’t always going to
  be the be...
---

Je parie que vous avez déjà des services en cours d'exécution sur AWS et que vous les avez configurés en utilisant la console du navigateur. Mais je parie aussi que vous suspectez déjà que cliquer à travers des couches et des couches de pages de configuration n'est pas toujours la meilleure approche. En fait, l'AWS CLI est une meilleure méthode qui accomplira exactement le même travail, mais avec beaucoup moins d'efforts.

En utilisant du contenu adapté de mon [_Cours Pluralsight : Automatiser les opérations AWS avec l'AWS CLI_](https://pluralsight.pxf.io/c/1191769/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fautomating-aws-operations-aws-cli), laissez-moi vous démontrer rapidement. Supposons que vous souhaitez lancer une instance Amazon Linux à partir d'EC2. Pour la mettre en route, vous devrez...

* Charger la page du tableau de bord EC2
* Cliquer sur Lancer une instance
* Sélectionner une AMI à partir de la page AMI
* Sélectionner un type d'instance à partir de la page Type d'instance
* Configurer les paramètres réseau, IAM, comportement du cycle de vie et données utilisateur sur la page Configurer les détails de l'instance
* Sélectionner un ou plusieurs volumes de stockage sur la page Ajouter un stockage
* Ajouter des tags sur la page Ajouter des tags
* Sélectionner ou configurer un groupe de sécurité sur la page—attendez-le—Configurer le groupe de sécurité
* Et enfin, passer en revue et lancer votre instance sur la page nommée (quoi d'autre?) Passer en revue et lancer

Et n'oubliez pas de cliquer à travers la fenêtre contextuelle où vous confirmerez votre paire de clés, puis de retourner au tableau de bord des instances EC2 pour obtenir les données de votre instance (comme les adresses IP).

Cela vous semble amusant? Cela vous semblera-t-il toujours amusant si vous travaillez avec une connexion Internet lente? Et que se passe-t-il si vous devez effectuer des variations de ce processus une demi-douzaine de fois par semaine?

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-15.png)
_Le clavier : tout ce dont vous avez vraiment besoin pour gérer vos services AWS_

Vous voulez voir comment vous lanceriez cette configuration en utilisant l'AWS CLI à partir d'un shell Bash (que vous pouvez exécuter sous Linux, macOS, et maintenant même Windows 10)? Remarquez comment j'ai utilisé des barres obliques inverses pour indiquer à Bash que la commande n'est pas encore complète. Appuyer sur Entrée lance le tout.

```
aws ec2 run-instances --image-id ami-04681a1dbd79675a5 \
 --count 1 \
 --instance-type r5d.large \
 --key-name MyKeyPair \
 --security-group-ids sg-007e43f80a1758f29 \
 --subnet-id subnet-970ec9f0 \
 --user-data file://my_script.sh \
 --tag-specifications \
 ResourceType=instance,Tags=[{Key=backend,Value=inventory1}]
```

Cette commande précise ne fonctionnera pas pour vous si vous la collez simplement dans votre terminal et l'exécutez. Les identifiants de groupe de sécurité et de sous-réseau sont spécifiques à mon compte, et vous n'avez probablement pas de paire de clés appelée MyKeyPair ou un fichier de script appelé my_script.sh. Mais cela vous montre que, une fois que vous avez fait quelques recherches préliminaires pour obtenir toutes les bonnes valeurs et confirmé que cela fonctionne, vous pourrez enregistrer la commande dans un fichier de script que vous pourrez modifier et exécuter chaque fois que nécessaire. Cela peut réduire un processus de cinq minutes à quelques secondes.

Le meilleur endroit pour obtenir des instructions d'installation de la CLI à jour pour votre système d'exploitation est [cette page de documentation AWS](https://docs.aws.amazon.com/cli/latest/userguide/installing.html). Votre meilleur choix sera généralement l'approche du gestionnaire de paquets Python utilisant PIP.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-16.png)
_La page d'installation de l'AWS CLI_

Configurer votre CLI pour accéder et administrer en toute sécurité les ressources de votre compte AWS est assez simple. Bien que vous deviez d'abord générer (et copier/enregistrer) une clé d'accès pour votre utilisateur AWS à partir du lien Mes informations d'identification de sécurité dans le menu déroulant du compte dans la console. Une fois cela fait, tapez simplement « aws configure » à l'invite de commande et entrez l'ID de la clé d'accès et la clé d'accès secrète que vous avez obtenus de Mes informations d'identification de sécurité. Vous pouvez éventuellement choisir les valeurs par défaut de la région et du format de sortie.

```
worker@workstation:~$ aws configure
AWS Access Key ID [****************KB2Q]: 
AWS Secret Access Key [****************W/Cu]: 
Default region name [us-east-1]: 
Default output format [text]: 
worker@workstation:~$
```

## Modèles de syntaxe de l'AWS CLI

Vous êtes maintenant prêt à commencer. Commençons par décomposer la syntaxe de la commande en ses parties constituantes et illustrons comment tout cela fonctionne à l'aide d'exemples pratiques. Après le préfixe de commande aws, une commande CLI est composée d'**options** (qui, comme le nom l'indique, sont facultatives), de **commandes**, de **sous-commandes** et de **paramètres**.

```
aws [options] <command> <subcommand> [parameters]
```

Cet exemple renverra toutes les images AMI EC2 officiellement maintenues par Amazon qui exécutent le système d'exploitation Linux CentOS.

```
aws --output table ec2 describe-images \
 --filters "Name=description,Values=*CentOS*" \
 "Name=owner-alias,Values=amazon"
```

Il utilise l'**option** de sortie, lui donnant la valeur « table » pour afficher la sortie de texte dans des tableaux. La **commande** de premier niveau ici est ec2. La plupart—sinon toutes—les commandes de premier niveau invoqueront des services AWS spécifiques. s3, iam et dynamodb sont d'autres exemples.

La **sous-commande** est _describe-images_, qui renverra les données liées à toutes les images Amazon Machine Images actuellement disponibles pour vos instances EC2. Cela renverrait une énorme quantité de données, car il existe des centaines d'AMI et chacune d'entre elles est représentée par beaucoup de métadonnées. Vous voudrez donc réduire un peu la recherche. Pour cela, j'ai fourni deux valeurs au paramètre—filtres : la description de l'image doit contenir le mot _CentOS_—en mettant en majuscule le c, o et s puisque cela sera sensible à la casse, et la valeur owner-alias doit être égale à _amazon_.

Vous exécuterez souvent des sous-commandes basées sur _describe_ pour obtenir des identifiants de ressources importants que vous pourrez ensuite utiliser dans vos commandes d'action réelles. Cet identifiant d'image CentOS serait typiquement utilisé dans le cadre d'une commande ec2 _run-instances_ pour lancer réellement une instance.

Outre describe et run, d'autres sous-commandes courantes commenceront par des verbes comme create, delete, enable, disable, modify, request, stop et terminate.

Les **options** incluent _region_, _output_ et _profile_—que vous avez déjà vues—plus _dry-run_, qui ne fera rien, mais affichera plutôt la sortie que votre commande générerait _si_ elle était réellement exécutée. Cela peut être très utile lorsque vous n'êtes pas sûr d'avoir la syntaxe tout à fait correcte. Essayons d'exécuter cette commande ec2 run-instances ci-dessus, mais cette fois en ajoutant _dry-run_.

## Exemple S3

Il est temps de faire un peu de magie S3. J'ai une entreprise qui a besoin d'un site web simple sans accès à une base de données ou à des clochettes et sifflets javascript. Juste un peu de HTML5 ordinaire. Je vais donc créer, configurer soigneusement et remplir mon bucket afin qu'il fonctionne comme un site web statique—en d'autres termes, afin que le trafic entrant soit automatiquement dirigé vers le fichier index.html que j'ai créé.

Bien que cela ne jouera aucun rôle dans cette démonstration, je vais éventuellement vouloir configurer un nom de domaine .com dans Route 53 d'Amazon qui pointe vers le site, donc je vais devoir créer un bucket S3 avec exactement ce nom—.com et tout. Je crée un bucket en utilisant _mb_ et un nom de bucket globalement unique.

```
aws s3 mb s3://mysite548.com
```

Le bucket devra être publiquement lisible, donc j'utiliserai _s3api put-bucket-acl_, avec les paramètres _bucket_ et _acl_. Ce dernier prendra la valeur _public-read_.

```
aws s3api put-bucket-acl --bucket mysite548.com --acl public-read
```

Ensuite, j'utiliserai s3 sync pour déplacer tout le contenu de mon répertoire local actuel vers mon bucket. J'ai créé trois fichiers : _index.html_ est la page web par défaut et _error.html_ sera la page chargée lorsqu'une ressource inexistante est demandée. Il y a aussi une petite image pour aider à embellir la démonstration. Le paramètre _acl public-read_ donnera aux fichiers eux-mêmes les mêmes permissions que le bucket.

```
aws s3 sync . s3://mysite548.com --acl public-read
```

Enfin, je définirai le but de ces fichiers html pour S3 en utilisant « s3 website ». Les paramètres _index-document_ et _error-document_ pointent simplement vers les fichiers pertinents. Vous n'avez pas besoin d'utiliser ces noms de fichiers spécifiques, d'ailleurs, c'est juste moi. Je confirmerai cette opération en utilisant s3api get-bucket-website.

```
aws s3 website s3://mysite548.com/ --index-document index.html --error-document error.html
aws s3api get-bucket-website --bucket mysite548.com
```

## Qu'est-ce qui suit ?

La syntaxe de commande de l'AWS CLI est assez intuitive. Néanmoins, vous aurez souvent besoin d'aide pour la faire exactement correctement. Comme je le montre dans [le cours Pluralsight](https://pluralsight.pxf.io/c/1191769/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fautomating-aws-operations-aws-cli), vous pouvez obtenir d'excellents conseils à partir du système _help_ en ligne de commande, ou à partir de la [documentation en ligne AWS](https://docs.aws.amazon.com/cli/latest/reference/index.html#cli-aws). Mon livre [Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27) contient également des conseils utiles et des exemples.

_Cet article est un extrait adapté de mon nouveau [Cours Pluralsight, Automatiser les opérations AWS avec l'AWS CLI](https://pluralsight.pxf.io/c/1191769/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fautomating-aws-operations-aws-cli)._