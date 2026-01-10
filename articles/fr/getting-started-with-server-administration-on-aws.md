---
title: Comment lancer un serveur distant sur AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-14T04:37:56.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-server-administration-on-aws
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cloudiness-clouds-cloudy-daylight-417045.jpg
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
seo_title: Comment lancer un serveur distant sur AWS
seo_desc: 'By Jillian Rowe

  AWS is so cool because it is made up of discreet building blocks that you can use
  to build some fairly complex infrastructure. This is awesome once you get a handle
  on things. But when you are just starting out you need to know things...'
---

Par Jillian Rowe

AWS est si cool parce qu'il est composé de blocs de construction discrets que vous pouvez utiliser pour construire une infrastructure assez complexe. C'est génial une fois que vous maîtrisez les choses. Mais lorsque vous commencez, vous devez savoir des choses comme "comment obtenir l'adresse IP de mon serveur" et "attendez, quelle clé SSH". 

Passons en revue quelques concepts clés, puis lançons notre propre serveur dans le cloud !

## Ce que vous devez savoir pour administrer des serveurs distants sur AWS

Il y a de nombreuses raisons pour lesquelles vous pourriez vouloir commencer sur AWS. Peut-être que votre entreprise déplace son infrastructure vers le cloud. Peut-être que vous voulez commencer à freelancer et ne pas investir dans des coûts de serveur initiaux. Ou peut-être que vous voulez simplement apprendre un nouvel ensemble de compétences. 

Pour lancer un serveur distant sur AWS, vous devez connaître quelques termes et concepts fondamentaux d'AWS. Je vais passer en revue quelques termes directement applicables au lancement d'un serveur distant, mais ces mêmes concepts sont utilisés pour des services d'infrastructure plus complexes tels qu'ElasticBeanstalk, Docker Swarm et Kubernetes. 

### Elastic Compute Cloud (EC2)

Les instances [AWS EC2](https://aws.amazon.com/ec2/) sont là où réside la puissance de calcul. Ce sont vos serveurs distants. Savoir comment gérer les instances EC2 est incroyablement important car elles apparaissent presque partout. 

### Groupes de sécurité

Les [groupes de sécurité](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) sont ce qui permet l'accès à vos divers services AWS, dans ce cas, une instance EC2. Ceux-ci définissent quels ports sont ouverts pour le trafic entrant et sortant. 

### Paires de clés

Les [paires de clés](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) sont vos clés SSH. Assurez-vous de les suivre et de les garder dans un endroit sûr ! De plus, si vous utilisez beaucoup AWS, vous commencerez une collection de paires de clés, alors assurez-vous de leur donner des noms descriptifs et pas seulement `ssh`. ;-)

### Virtual Private Cloud (VPC)

Un [VPC](https://aws.amazon.com/vpc/) est une ressource isolée où vit votre infrastructure de calcul. Pour continuer avec ma philosophie selon laquelle tout est des Legos, le VPC est la boîte de Legos tandis que l'EC2, les groupes de sécurité et les paires de clés sont les Legos eux-mêmes. 

Les VPC s'occupent de tout votre réseau. Lorsque vous vous inscrivez à un compte AWS, vous obtiendrez un VPC par défaut et c'est ce que nous utiliserons aujourd'hui. 

## Comment lancer une instance EC2

Il existe de nombreuses, nombreuses façons de lancer une instance EC2. Celle que vous choisirez dépendra de vos besoins. Aujourd'hui, nous allons passer en revue l'utilisation de la console web AWS et de la bibliothèque Python `boto3`.

En aparté, comme AWS a tant de services, vous devez aller dans chaque service individuellement pour le gérer. Si vous êtes perdu, recherchez simplement votre service dans le menu 'Services'.

## Lancer une instance EC2 en utilisant l'assistant 

Tout d'abord, vous devrez vous connecter à votre [Console AWS](https://console.aws.amazon.com/).

### Accéder au tableau de bord EC2

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-Services-Menu---Search-EC2.png)
*Accédez à la page des services EC2 en la recherchant dans 'Services'*



1. Cliquez sur Services pour faire apparaître la boîte de recherche.
2. Tapez le nom du service que vous voulez - dans ce cas, EC2.
3. Cliquez sur le nom de votre service dans le menu pour accéder au tableau de bord de ce service. 

### Sélectionnez 'Lancer l'instance'

Une fois sur le tableau de bord EC2, vous voudrez cliquer sur le bouton 'Lancer l'instance' au milieu de l'écran. Cela démarrera l'assistant de lancement AWS EC2, qui nous guidera tout au long du processus de démarrage d'une instance EC2.

Si vous souhaitez passer à la partie 2 où nous démarrerons un serveur EC2 de manière programmatique avec Python, c'est une excellente occasion de noter l'ID de votre VPC par défaut !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS_EC2_-_Select_Instance_Type-1.png)

### Aperçu de l'assistant EC2

Une fois que vous avez sélectionné 'Lancer l'instance', vous serez dirigé vers un assistant. Le menu de l'assistant comporte 7 étapes, et vous pouvez passer de l'une à l'autre comme vous le souhaitez pour configurer votre instance exactement comme vous le voulez.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-EC2-Wizard-Menu.png)

### Assistant EC2 - Sélectionnez votre type d'AMI

C'est là que la magie opère !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS_EC2_-_Select_Instance_Type.png)

C'est ici que vous choisirez votre type d'AMI, qui est principalement le système d'exploitation que vous souhaitez. Il existe de nombreuses AMIs préconfigurées pour de nombreux cas d'utilisation courants, y compris les applications ML, les serveurs web et les bases de données. Consultez le [AWS Marketplace](https://aws.amazon.com/marketplace) pour voir toutes les AMIs cool disponibles !

J'aime l'image Amazon Linux 2, mais vous pouvez rechercher n'importe quel type d'image, y compris Ubuntu, Centos, ou n'importe quelle image [Bitnami](https://bitnami.com/partners/aws). 

Petite note rapide ici. J'adore les images Bitnami. Elles sont toutes géniales, et si vous cherchez à déployer une quelconque application web telle que Ghost, Wordpress, Nginx, ou même des applications plus complexes comme Redash ou Airflow, je les recommande vraiment. 

### Assistant EC2 - Choisissez votre type d'instance

Je choisis celui qui est gratuit car je prévois de le supprimer, mais si vous utilisez réellement cette instance EC2 pour quelque chose d'important, vous voudrez ajouter plus de puissance. Si vous avez besoin de quelque chose impliquant internet, comme le transfert de données, assurez-vous de prêter attention aux capacités internet et de choisir quelque chose dans la gamme modérée. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-EC2-Choose-Instance-Type-Size.png)

Faites défiler vers le bas et choisissez soit 'Lancer' pour lancer avec les paramètres par défaut, soit 'Configurer votre instance' pour ajouter des configurations supplémentaires telles que la modification de la taille du système de fichiers racine, le choix d'un VPC, ou l'ajout de données utilisateur.

### Assistant EC2 - Ajouter des tags

Lorsque vous commencez, cela n'a pas trop d'importance, mais à mesure que vous avancez avec AWS, vousoudrez vous assurer que toutes vos instances ont, au moins, des tags `Name`. Cela vous permettra de rechercher plus facilement vos instances et de faire des choses sympas comme créer des groupes de ressources pour regrouper vos services AWS. 

Dans le menu de l'assistant, sélectionnez 'Ajouter des tags'. Ne vous inquiétez pas, vous pouvez passer d'une étape à l'autre dans l'assistant aussi souvent que vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-EC2-Wizard---Tag.png)

### Assistant EC2 - Configurer le groupe de sécurité

Avant de terminer, nous allons configurer le groupe de sécurité, qui définit les règles d'accès. AWS créera un groupe de sécurité pour vous, ou vous pouvez en choisir un existant. Par défaut, le port 22 est ouvert pour SSH, mais si vous l'utilisez pour des applications web ou de base de données, vous devrez ouvrir ces ports également. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-EC2-Wizard-Seccurity-Group.png)

### Assistant EC2 - LANCEMENT

Maintenant que nous avons dit à AWS ce que nous voulons, lançons notre instance ! Cliquez sur Examiner et Lancer. Vous obtiendrez une fenêtre contextuelle vous demandant quelle clé SSH vous voulez. Vous pouvez également créer une nouvelle paire de clés SSH ici. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/EC2-Wizard---KeyPair.png)

### Assistant EC2 - Page de confirmation

Une fois que vous avez lancé, vous serez dirigé vers une page de confirmation avec votre ID d'instance EC2. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-EC2-Launch-Confirmation.png)

### Tableau de bord EC2 - Obtenez votre adresse IP

Nous y voilà ! Maintenant, il ne reste plus qu'à attendre que notre instance soit prête et à nous connecter en SSH.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/AWS-EC2-Dashboard---Get-IP-Address.png)

D'accord ! Maintenant, nous devons simplement nous connecter en SSH à notre instance. Les détails pour cela seront légèrement différents selon le type d'instance que vous avez choisi.

Cela suppose que vous avez téléchargé votre paire de clés nommée `my-remote-server.pem` et que vous l'avez déplacée vers `~/.ssh`

```bash
chmod 400 ~/.ssh/my-remote-server.pem

# Amazon linux 2 ami
ssh -i ~/.ssh/my-remote-server.pem ec2-user@PUBLIC_DNS

# Ubuntu ou Bitnami
ssh -i ~/.ssh/my-remote-server.pem ubuntu@PUBLIC_DNS
```

C'est tout ! Maintenant vous avez un serveur distant dans le cloud !

## Lancer une instance EC2 avec la bibliothèque Python Boto3

Avertissement complet ici. Cela va bien au-delà de ce que je ferais normalement avec la bibliothèque boto3. Pour tout ce qui dépasse le lancement d'une instance EC2, je recommande d'utiliser la console ou un outil d'infrastructure en tant que code tel que [Cloudformation](https://aws.amazon.com/cloudformation/) ou [Terraform](https://www.freecodecamp.org/news/p/91bf3938-5e24-4f7a-99b0-090255995d6c/terraform.io). Mais lorsque vous commencez, il est vraiment important de comprendre les bases.

J'ai aussi un besoin obsessionnel d'écrire des rapports pour absolument tout. N'hésitez pas à supprimer si vous n'êtes pas aussi paranoïaque. ;-)

```
import boto3
import time
import json
from pprint import pprint
from select import select
import logging
from logging import Logger
from paramiko import SSHClient
import paramiko
from typing import Any
import os

logger = logging.getLogger('launch_ec2')
logger.setLevel(logging.DEBUG)

PROJECT = "my-remote-server"
KEY_PAIR = "my-remote-server"
SECURITY_GROUP="sg-some-number"
# Amazon Linux 2 AMI
AMI_ID="ami-062f7200baf2fa504"
INSTANCE_TYPE="t3a.medium"

report_data = {
    'name': PROJECT,
    'computer_name': KEY_PAIR,
}

def initialize_dir():
	"""
    Initialiser un répertoire pour écrire notre paire de clés et les rapports
    """
    if not os.path.exists(KEY_PAIR):
        os.mkdir(KEY_PAIR)


def create_key_pair():
    ec2_client = boto3.client('ec2')
    key_pair_response = ec2_client.create_key_pair(KeyName=KEY_PAIR)
    report_data['ssh_key'] = {}
    report_data['ssh_key']['id'] = key_pair_response['KeyPairId']
    report_data['ssh_key']['name'] = key_pair_response['KeyName']
    report_data['ssh_key']['key'] = key_pair_response['KeyMaterial']
    report_data['ssh_key']['key_file'] = os.path.abspath(os.path.join(KEY_PAIR, 'keypair.pem'))
    logger.info('Clé SSH créée avec succès')


def write_key_file():
    """
    Écrire le fichier de clé SSH .pem
    :return:
    """
    f = open(os.path.join(KEY_PAIR, 'keypair.pem'), 'w+')
    f.write(report_data['ssh_key']['key'])
    f.close()
    os.chmod(os.path.join(KEY_PAIR, 'keypair.pem'), 0o400)
    logger.info(
        'Fichier de clé SSH écrit dans {keypair}'.format(
            keypair=
            os.path.abspath(os.path.join(KEY_PAIR, 'keypair.pem'))
        )
    )


def create_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        SecurityGroupIds=[SECURITY_GROUP],
        ImageId=AMI_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_PAIR,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': PROJECT
                    },
                ]
            },
        ],
    )
    report_data['ec2'] = {}
    report_data['ec2']['id'] = instance[0].id
    report_data['ec2']['PublicIP'] = None


def get_public_ip():
    print('Attente de l\'initialisation de l\'instance avec une adresse IP publique...')
    print('Cela peut prendre un certain temps...')
    time.sleep(10)
    ec2 = boto3.resource('ec2')
    running_instances = ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        },
        {
            'Name': 'instance-id',
            'Values': [report_data['ec2']['id']]
        }
    ])
    for instance in running_instances:
        # Ajouter les informations de l'instance à un dictionnaire
        report_data['ec2'] = {
            'instance_id': report_data['ec2']['id'],
            'Type': instance.instance_type,
            'State': instance.state['Name'],
            'PrivateIP': instance.private_ip_address,
            'PublicIP': instance.public_ip_address,
            'LaunchTime': str(instance.launch_time)
        }


def write_report():
	"""
    Écrire un fichier JSON avec tous les ID et autres informations nécessaires
    """
    logger.info('Écriture du rapport dans {}'.format(
        os.path.abspath(os.path.join(KEY_PAIR, 'report.json'))
    ))
    f = open(os.path.abspath(os.path.join(KEY_PAIR, 'report.json'))
             , 'w+')
    json.dump(report_data, f, ensure_ascii=False, indent=4)
    f.close()


def print_helper_commands():
    """
    Afficher quelques commandes d'aide pour ssh et rsync à l'écran
    """
    rsync_command = "rsync -av --progress -e 'ssh -i {key_file}' HOST_DIR ec2-user@{public_id}:/home/ec2-user/efs".format(
        key_file=report_data['ssh_key']['key_file'],
        public_id=report_data['ec2']['PublicIP']
    )
    ssh_command = "ssh -i {key_file} ec2-user@{public_ip}".format(
        key_file=report_data['ssh_key']['key_file'],
        public_ip=report_data['ec2']['PublicIP']
    )
    report_data['ssh_command'] = ssh_command
    report_data['rsync_command'] = rsync_command
    print('Quelques commandes utiles !')
    print('###################################')
    print('# Se connecter à l\'instance avec : ')
    print(ssh_command)
    print('###################################')

    print('###################################')
    print('# Synchroniser les données avec l\'instance avec : ')
    print(rsync_command)
    print('###################################')


def print_end_message():
    print('##################################')
    print('Terminé !')
    print('Voir {dir}/report.json pour les détails'.format(dir=KEY_PAIR))


initialize_dir()
create_key_pair()
write_key_file()
create_instance()
while report_data['ec2']['PublicIP'] is None:
    get_public_ip()
print_helper_commands()
write_report()
print_end_message()

```

## Conclusion

C'est tout ce que vous devez savoir pour commencer à lancer des serveurs distants dans le cloud ! Quels types de projets souhaitez-vous déployer dans le cloud ?