---
title: Comment configurer le déploiement automatisé dans AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-24T23:58:20.000Z'
originalURL: https://freecodecamp.org/news/automated-deployment-in-aws-5aadc2e708a9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*a0I_eNlhdrTw_p-b
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment configurer le déploiement automatisé dans AWS
seo_desc: 'By Harry Sauers

  Provisioning and Configuring Servers

  Introduction

  In this tutorial, you’ll learn how to use Amazon’s AWS SDK to deploy your Python
  application to a real-world server.

  Before we begin, you should have a working knowledge of Python, Git...'
---

Par Harry Sauers

### Approvisionnement et configuration des serveurs

#### Introduction

Dans ce tutoriel, vous apprendrez à utiliser le SDK AWS d'Amazon pour déployer votre application Python sur un serveur réel.

Avant de commencer, vous devez avoir une connaissance pratique de Python, Git et de l'infrastructure cloud en général. Je recommande [Codecademy](https://www.codecademy.com/) si vous souhaitez apprendre ces fondamentaux.

Certaines des commandes Terminal/Bash que j'utilise sont pour un système Ubuntu. Si elles ne fonctionnent pas, vérifiez les équivalents pour votre système.

![Image](https://cdn-media-1.freecodecamp.org/images/yO2RvLxE1FNJDJnIA2BWRcl7cpWPHMaCXz6I)

### Pour commencer

* Lancez votre [IDE Python](https://www.programiz.com/python-programming/ide) préféré et créez un nouveau projet.
* Créez votre fichier principal de projet et nommez-le comme vous le souhaitez — j'ai choisi « app.py » pour simplifier.
* Ajoutez _print("Hello Python!")_ au fichier et exécutez-le pour vous assurer que votre environnement est correctement configuré.
* Ensuite, nous devons installer le SDK d'Amazon. Bien qu'AWS fournisse une API HTTP standard, le kit de développement logiciel est beaucoup plus robuste. Le SDK gère les opérations fastidieuses et de bas niveau pour vous.
* Ouvrez un terminal et tapez `_sudo pip3 install boto3_` et entrez votre mot de passe sudo, si nécessaire.
* Ajoutez `_import boto3_` en haut de votre fichier Python.
* Cela nous permet d'utiliser le SDK d'Amazon dans notre application Python.

### Identifiants AWS

Avant de pouvoir utiliser quoi que ce soit sur AWS, nous avons besoin d'identifiants pour notre compte AWS. Si vous n'en avez pas, vous pouvez vous inscrire ici.

* Allez dans votre [panneau Identity and Access Management](https://console.aws.amazon.com/iam/home?#/users) et cliquez sur « Ajouter un utilisateur » sous l'onglet « Utilisateurs ».
* Entrez un nom d'utilisateur et cochez la case à côté de « accès programmatique ».
* Cliquez sur « Suivant : Autorisations » et créez un nouveau groupe, si nécessaire.
* Pour les besoins de ce tutoriel, je vais créer un nouveau groupe avec la politique « AdministratorAccess ». Cela nous donne la permission de gérer tout dans notre console AWS de manière programmatique.
* Cliquez sur « Suivant : Balises » et ajoutez toute information pertinente. Cela est facultatif.
* Cliquez sur « Examiner », puis sur « Créer un utilisateur ».
* Téléchargez vos identifiants de sécurité (le fichier CSV) et copiez-le dans le répertoire racine de votre projet. Si vous utilisez le contrôle de source, soyez prudent.

### Lecture des identifiants

* Créez un nouveau fichier « creds.py » avec le code suivant :

```
import csv
```

```
class Creds:
```

```
# identifiants
```

```
username = ""
```

```
access_key_id = ""
```

```
secret_key = ""
```

```
def __init__(self, creds_file):
```

```
with open(creds_file) as file:
```

```
reader = csv.reader(file, delimiter=",")
```

```
header = next(reader)
```

```
creds_line = next(reader)
```

```
self.username = creds_line[0]
```

```
self.access_key_id = creds_line[2]
```

```
self.secret_key = creds_line[3]
```

* Ajoutez `_from creds import Creds_` en haut de votre fichier Python principal.
* Initialisez votre objet Creds dans celui-ci : `_creds = Creds("credentials.csv")_`

Super ! Maintenant, nous pouvons utiliser ceux-ci pour accéder à Amazon Web Services.

![Image](https://cdn-media-1.freecodecamp.org/images/GWhZsqkFPHtB6U1KYh6oFrz9f0dHaqCd5Lpn)

### Approvisionnement d'un serveur EC2

Ajoutez le code suivant après votre variable `_creds` :

```
REGION = "us-east-2"
```

```
client = boto3.client(
```

```
'ec2',
```

```
aws_access_key_id=creds.access_key_id,
```

```
aws_secret_access_key=creds.secret_key,
```

```
region_name=REGION
```

```
)
```

Maintenant, approvisionnons une nouvelle instance d'Ubuntu Server 18.04. Cela est également éligible pour le niveau gratuit d'Amazon !

En haut de votre fichier, ajoutez _from botocore.exceptions import ClientError_ pour que votre programme sache comment gérer les erreurs.

Rendez-vous sur votre tableau de bord AWS et allez dans EC2->Network & Security-> Key pairs et cliquez sur « Create key pair ».

Entrez un nom et cliquez sur « Create ». J'ai utilisé « robot » pour le mien. Bien que vous devriez éviter de coder en dur des chaînes comme celle-ci, nous allons passer outre pour l'instant afin de le faire fonctionner.

Pour exécuter des commandes sur le serveur et l'ouvrir au Web, nous devons créer un groupe de sécurité et un rôle IAM sur AWS. Allez sur votre tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/EWYx2GTGhMeEkIAQ3SW6YrPxNLsVqtjycK-z)

### Création d'un groupe de sécurité :

* Accédez à Network & Security -> Security Groups.
* Créez un groupe de sécurité et ouvrez les ports 22, 80, 443 et 5000. Cela permettra un accès général à celui-ci depuis le Web. Autorisez toutes les IP à y accéder.
* Copiez l'ID du groupe de sécurité que vous venez de créer et collez-le dans une variable globale appelée _SECURITY_GROUP_.

![Image](https://cdn-media-1.freecodecamp.org/images/Kg3HGuiibb-AQL9U8fo2eehou0dqFGbZcKYF)

### Création d'un rôle IAM :

* Allez sur votre tableau de bord AWS et accédez au service IAM.
* Cliquez sur l'onglet « Rôles ».
* Cliquez sur « Créer un rôle » et sélectionnez « EC2 ». Pour les besoins de ce tutoriel, vous voudrez sélectionner « Administrator Access », mais dans un cadre réel, cela peut ne pas être approprié.
* Cliquez sur les étapes restantes pour créer un rôle.
* Copiez le nom du rôle IAM et collez-le dans une variable globale appelée _IAM_PROFILE_.
* Ajoutez ce code pour approvisionner un serveur Ubuntu minimal depuis Amazon :

```
def provision_server():
```

```
# ID du serveur Ubuntu 18.04 depuis le panneau AWS
```

```
image_id = "ami-0f65671a86f061fcd"
```

```
# Deuxième plus petite instance, éligible pour le niveau gratuit.
```

```
instance_type = "t2.micro"
```

```
# Faites de ceci un argument de ligne de commande à l'avenir.
```

```
keypair_name = "robot"
```

```
response = {}
```

```
try:
```

```
response = ec2.run_instances(ImageId=image_id,
```

```
InstanceType=instance_type,
```

```
KeyName=keypair_name,
```

```
SecurityGroupIds=[SECURITY_GROUP],
```

```
IamInstanceProfile={'Name': IAM_PROFILE},
```

```
MinCount=1,
```

```
MaxCount=1)
```

```
print(response['Instances'][0])
```

```
print("Approvisionnement de l'instance...")
```

```
# attendre que le serveur soit approvisionné avant de retourner quoi que ce soit
```

```
time.sleep(60)
```

```
return str(response['Instances'][0]['InstanceId'])
```

```
except ClientError as e:
```

```
print(e)
```

Félicitations ! Vous êtes prêt à approvisionner votre premier serveur EC2 sur Amazon. Apprenez à configurer ses paramètres réseau et de sécurité et à déployer une véritable application web dessus dans la Partie 2 lorsque vous serez prêt à passer à l'étape suivante.

### Déploiement de votre application

Vous l'avez fait ! Apprenons à gérer les instances EC2 et à déployer une application depuis Github sur l'une d'entre elles.

Le SDK d'Amazon prend en charge l'exécution de commandes sur l'instance. Cela est très utile. Il nous permet de gérer l'instance sans avoir à nous soucier de la configuration d'un shell sécurisé et autres.

* Tout d'abord, nous devons obtenir une liste des instances dans votre cloud privé :

```
def get_instance_ids():
```

```
instance_id_list = []
```

```
instances = ec2.describe_instances()
```

```
instances = instances['Reservations'][0]['Instances']
```

```
for instance in instances:
```

```
instance_id_list.append(instance['InstanceId'])
```

```
return instance_id_list
```

* Ajoutez ce code pour pouvoir exécuter des commandes sur le terminal de votre serveur :

```
def send_command_aws(commands=["echo hello"], instance="i-06cca6072e593a0ac"):
```

```
ssm_client = boto3.client('ssm',
```

```
aws_access_key_id=creds.access_key_id,
```

```
aws_secret_access_key=creds.secret_key,
```

```
region_name=REGION)
```

```
response = ssm_client.send_command(
```

```
InstanceIds=[instance],
```

```
DocumentName="AWS-RunShellScript",
```

```
Parameters={'commands': commands}, )
```

```
command_id = response['Command']['CommandId']
```

```
time.sleep(5)
```

```
output = ssm_client.get_command_invocation(
```

```
CommandId=command_id,
```

```
InstanceId=instance,
```

```
)
```

```
print(output)
```

* Enfin, nous devons générer des commandes pour installer les dépendances et déployer une application web Flask depuis Github sur le serveur en direct :

```
def generate_git_commands(git_url=GIT_URL, start_command="sudo python3 hellopython/app.py", pip3_packages=[], additional_commands=[]):
```

```
commands = []
```

```
if ".git" in git_url:
```

```
git_url = git_url[:-4]
```

```
repo_name = git_url[git_url.rfind('/'):]
```

```
# installer les dépendances
```

```
commands.append("sudo apt-get update")
```

```
commands.append("sudo apt-get install -y git")
```

```
commands.append("sudo apt-get install -y python3")
```

```
commands.append("sudo apt-get install -y python3-pip")
```

```
commands.append("sudo rm -R hellopython")
```

```
commands.append("pip3 — version")
```

```
commands.append("sudo git clone " + git_url)
```

```
# commands.append("cd " + repo_name)
```

```
# installer les dépendances python
```

```
for dependency in pip3_packages:
```

```
commands.append("sudo pip3 install " + dependency)
```

```
# exécuter des commandes personnalisées supplémentaires
```

```
for command in additional_commands:
```

```
commands.append(command)
```

```
# démarrer l'exécution du programme
```

```
commands.append(start_command)
```

```
return commands
```

* Ajoutez ces constantes en haut de votre programme :

```
GIT_URL = "https://github.com/hsauers5/hellopython"
REGION = "us-east-2"
SECURITY_GROUP = "sg-0c7a3bfa35c85f8ce"
IAM_PROFILE = "Python-Tutorial"
```

* Maintenant, ajoutez cette ligne en bas de votre programme :

```
send_command_aws(commands=generate_git_commands(GIT_URL, pip3_packages=["flask"]), instance=provision_server())
```

* Exécutez votre code ! `_python3 app.py_`
* Rendez-vous sur votre panneau EC2 et copiez le DNS public de la machine. Ajoutez « :5000 » et accédez-y dans votre navigateur.

Félicitations ! Vous venez de terminer votre premier déploiement automatisé en utilisant le SDK Boto3 d'Amazon.

Vous pouvez consulter ou télécharger le dépôt complet ici : [https://github.com/hsauers5/AWS-Deployment](https://github.com/hsauers5/AWS-Deployment)