---
title: Comment déployer une application NodeJS avec AWS CloudFormation
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-04-18T18:03:26.000Z'
originalURL: https://freecodecamp.org/news/deploy-nodejs-app-with-cloudformation
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/CloudFormation.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: node
  slug: node
seo_title: Comment déployer une application NodeJS avec AWS CloudFormation
seo_desc: 'Imagine you have built a great product and its user base is growing rapidly.
  You want to scale your product to be available to people around the world. To do
  this, you''ll need good cloud infrastructure.

  But managing your cloud infrastructure manually...'
---

Imaginez que vous avez construit un excellent produit et que sa base d'utilisateurs croît rapidement. Vous souhaitez mettre à l'échelle votre produit pour qu'il soit disponible pour les personnes du monde entier. Pour ce faire, vous aurez besoin d'une bonne infrastructure cloud.

Mais gérer manuellement votre infrastructure cloud peut être épuisant. Vous pourriez commencer à vous demander : "Comment font les entreprises pour y parvenir ?"

Eh bien, elles automatisent la gestion de leur infrastructure cloud via du code. Et c'est ce qu'offre AWS CloudFormation – un moyen de gérer votre infrastructure cloud en tant que code.

Dans ce tutoriel, nous explorerons les bases d'AWS CloudFormation et comment il peut vous aider à automatiser la gestion de votre infrastructure cloud. Plongeons dans le monde de l'infrastructure en tant que code.

## Qu'est-ce que CloudFormation ?

AWS CloudFormation est un service qui vous aide à automatiser la création et la gestion de vos ressources cloud.

Imaginez que vous construisez une maison et que vous souhaitez vous assurer que tout est à sa place – les murs, le toit, les portes et les fenêtres. Avant de construire, vous créeriez un plan pour votre maison et spécifieriez exactement ce que vous voulez et où vous le voulez.

De même, CloudFormation vous permet de créer un plan pour votre infrastructure cloud. Vous pouvez spécifier quelles ressources vous souhaitez créer (par exemple, des serveurs EC2, des bases de données, du stockage, etc.) et comment elles doivent être configurées. CloudFormation se charge de créer et de gérer ces ressources automatiquement pour vous.

CloudFormation peut être utile dans de nombreux cas. J'en listerai quelques-uns ici :

1. Gérer les changements d'infrastructure dans plusieurs environnements (Développement, Staging, Production)
2. Re-créer la même infrastructure dans une région/compte différent
3. Re-créer une ressource qui a été supprimée accidentellement avec la configuration exacte en quelques secondes (pas manuellement, car vous avez toutes les configurations dans votre code)

Le meilleur aspect est que CloudFormation rend la mise à jour de votre infrastructure super simple et automatique. Si vous souhaitez ajouter une nouvelle ressource, changer une configuration ou supprimer une ressource, vous pouvez mettre à jour votre plan, et CloudFormation gérera les changements pour vous.

## Comment fonctionne CloudFormation

Vous vous demandez peut-être comment fonctionne CloudFormation. C'est simple : nous allons télécharger nos modèles CloudFormation dans Amazon S3 (en coulisses) qui seront récupérés par CloudFormation.

Un point important à noter est que nous ne pouvons pas modifier le modèle une fois téléchargé. Nous devons re-télécharger le modèle mis à jour vers AWS que CloudFormation compare avec l'infrastructure existante et apporte les modifications nécessaires.

Une fonctionnalité géniale est que vous pouvez supprimer toutes les ressources créées par CloudFormation en un clic en supprimant la pile. La pile CloudFormation n'est rien d'autre qu'une collection de ressources AWS que vous pouvez gérer en tant qu'unité unique.

Vous définissez une pile en créant un modèle CloudFormation qui décrit les ressources que vous souhaitez créer, et exécutez le modèle pour créer la pile.

## Comment déployer des modèles CloudFormation

Nous pouvons déployer le modèle CloudFormation de deux manières. L'une est d'utiliser CloudFormation Designer et l'autre est d'écrire le code dans un fichier YAML/JSON.

Si vous n'êtes pas familier avec YAML/JSON, vous pouvez opter pour CloudFormation Designer. C'est ce que je recommanderais pour ceux qui ne savent pas coder. Il vous permet de créer et de modifier des modèles graphiquement, ce qui facilite la visualisation de votre infrastructure et simplifie le processus de création de modèles. Mais dans ce tutoriel, nous allons écrire du code YAML pour déployer notre application.

## Comment créer un modèle CloudFormation pour déployer une application NodeJS

Vous pouvez créer un modèle CloudFormation en utilisant soit un fichier YAML soit JSON – mais nous allons utiliser un fichier YAML dans ce tutoriel.

Dans ce modèle, nous allons créer une instance EC2, configurer un groupe de sécurité pour EC2, et ajouter un script pour déployer une simple application NodeJS.

### Modèle CloudFormation pour créer une instance EC2

Il existe plus de 224 types de ressources, mais nous devons créer une ressource EC2. Les **ressources** représentent les différents composants AWS qui seront créés et configurés. Nous définirons les identifiants de type de **ressource** dans le format suivant :

```
AWS::aws-product-name::data-type-name
```

Le format de ressource pour l'instance EC2 est `AWS::EC2::Instance`. Pour en savoir plus sur les ressources AWS et la syntaxe, consultez la [documentation officielle AWS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) et jouez avec. Regardez la [documentation EC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) pour comprendre la déclaration de l'instance EC2. Les syntaxes JSON et YAML sont disponibles, mais nous allons nous en tenir à YAML pour ce tutoriel.

Il existe de nombreuses propriétés disponibles pour personnaliser la création de nos instances EC2. Pour simplifier les choses, nous allons configurer AvailabilityZone, ImageId et InstanceType, qui sont des propriétés de base nécessaires pour créer une instance EC2.

```
Resources:
  SampleNodejsDeploy:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-a4c7edb2
      InstanceType: t2.micro
```

Ici, `SampleNodejsDeploy` fait référence au nom de la ressource que nous allons créer. Vous pouvez nommer votre ressource comme vous le souhaitez.

Voyons le processus pour déployer l'application NodeJS.

### Comment déployer une application NodeJS en utilisant un modèle CloudFormation

Nous allons déployer l'application NodeJS en utilisant la propriété `UserData` dans la ressource EC2.

Si vous ne connaissez pas les données utilisateur EC2, c'est une fonctionnalité d'AWS EC2 qui nous permet de passer des informations lors du lancement de l'instance EC2. Vous pouvez l'utiliser pour effectuer des actions personnalisées, telles que l'installation de logiciels et l'exécution de scripts.

Écrivons le script bash pour déployer l'application NodeJS et attachons-le aux données utilisateur.

Voici le script simple pour déployer l'application NodeJS :

```
#!/bin/bash 
set -e
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt install nodejs
node -v
npm -v
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn
yarn --version
sudo -i -u ubuntu bash << EOF
set -e
cd /home/ubuntu
sudo npm install -g pm2
git clone https://github.com/5minslearn/node_with_docker.git
cd node_with_docker
yarn install 
pm2 start yarn --time --interpreter bash --name sample_node -- start -p 8000
EOF
```

Le script ci-dessus installe NodeJS, Yarn et PM2. Il clone un projet NodeJS depuis [Git](https://github.com/5minslearn/node_with_docker.git), installe les dépendances et démarre l'application avec PM2.

Notre prochaine étape est d'attacher ce script au modèle CloudFormation.

### Comment attacher UserData au modèle CloudFormation

```
Resources:
  SampleNodejsDeploy:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-014d05e6b24240371
      UserData: 
        Fn::Base64:
          |
          #!/bin/bash 
          set -e
          curl -sL https://deb.nodesource.com/setup_16.x | bash -
          sudo apt install nodejs
          node -v
          npm -v
          curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
          echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
          sudo apt update && sudo apt install yarn
          yarn --version
          sudo -i -u ubuntu bash << EOF
          set -e
          cd /home/ubuntu
          sudo npm install -g pm2
          git clone https://github.com/5minslearn/node_with_docker.git
          cd node_with_docker
          yarn install 
          pm2 start yarn --time --interpreter bash --name sample_node -- start -p 8000
          EOF
```

Vous remarquerez que la propriété `UserData` est ajoutée au bloc EC2. `Fn::Base64` est une fonction dans AWS CloudFormation qui permet aux utilisateurs d'encoder une chaîne au format base64. Cette fonction peut être utilisée pour passer des informations sensibles, telles que des identifiants, aux ressources AWS de manière sécurisée. Puisque les données utilisateur EC2 ne sont pas chiffrées, il est toujours préférable de les encoder.

Juste en dessous de cette ligne, vous pouvez voir une petite barre verticale (`|`). Elle est utilisée pour la prise en charge des chaînes multi-lignes car notre script fait plus d'une ligne.

D'accord. Maintenant, nous avons un script pour déployer l'application NodeJS. Mais nous devons nous souvenir d'un élément super important. Par défaut, les applications NodeJS s'exécutent sur le port 8000. Nous devons exposer le port 8000 depuis EC2. Maintenant, nous devons créer une configuration de groupe de sécurité pour notre instance EC2.

### Comment créer un groupe de sécurité en utilisant un modèle CloudFormation

Ce processus est similaire à la création d'une instance EC2, sauf que nous allons remplacer le type de `Instance` par `SecurityGroup`.

```
SampleNodejsDeploySG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: pour les nœuds de l'application qui permettent ssh, http, 8000
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '8000'
        ToPort: '8000'
        CidrIp: 0.0.0.0/0
```

Le code ci-dessus devrait être assez explicite – nous avons défini un groupe de sécurité, permettant les ports 22 (port SSH), 80 (port HTTP) et 8000 (NodeJS). Nous avons nommé la ressource `SampleNodejsDeploySG`.

### Comment attacher le groupe de sécurité à EC2

Vous vous demandez peut-être : "Nous avons créé un modèle pour créer un groupe de sécurité, mais comment cela sera-t-il lié à l'instance EC2 ?"

La solution est simple. CloudFormation fournit une fonction intrinsèque appelée `!Ref` qui nous permet de référencer une ressource ou un paramètre dans un modèle CloudFormation.

```
Resources:
  SampleNodejsDeploy:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-014d05e6b24240371
      SecurityGroups:
        - !Ref SampleNodejsDeploySG
      UserData: 
        Fn::Base64:
          |
          #!/bin/bash 
          set -e
          curl -sL https://deb.nodesource.com/setup_16.x | bash -
          sudo apt install nodejs
          node -v
          npm -v
          curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
          echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
          sudo apt update && sudo apt install yarn
          yarn --version
          sudo -i -u ubuntu bash << EOF
          set -e
          cd /home/ubuntu
          sudo npm install -g pm2
          git clone https://github.com/5minslearn/node_with_docker.git
          cd node_with_docker
          yarn install 
          pm2 start yarn --time --interpreter bash --name sample_node -- start -p 8000
          EOF
            
  SampleNodejsDeploySG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: pour les nœuds de l'application qui permettent ssh, http 
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '8000'
        ToPort: '8000'
        CidrIp: 0.0.0.0/0
```

Vous pouvez voir que la propriété `SecurityGroups` est ajoutée à l'instance EC2 et que la configuration du groupe de sécurité créé est liée à l'instance EC2 en utilisant le paramètre `!Ref`.

Maintenant, nous avons le modèle CloudFormation. Mais nous n'avons pas encore terminé. Il nous manque encore une chose. Pouvez-vous la deviner ? Nous avons créé une instance EC2 et nous avons autorisé un port SSH... mais pour nous connecter en utilisant SSH, nous devons attacher une paire clé-valeur, n'est-ce pas ? Faisons cela.

Nous pouvons attacher le nom de la paire clé-valeur directement au modèle. Par exemple, supposons que votre nom de paire clé-valeur est `5minslearn`, vous pouvez attacher la propriété `KeyName` directement au bloc de ressource EC2 comme montré ci-dessous ou nous pouvons la passer via des paramètres.

```
Resources:
  SampleNodejsDeploy:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-014d05e6b24240371
      KeyName: 5minslearn
      SecurityGroups:
        - !Ref SampleNodejsDeploySG
```

### Comment utiliser des paramètres dans le modèle CloudFormation

Nous pouvons utiliser des paramètres pour obtenir le nom de la paire clé-valeur de l'utilisateur lors de la création de la pile. Basiquement, les paramètres nous permettent de passer des valeurs d'entrée dans les modèles CloudFormation à l'exécution. Voyons comment faire cela.

```
Parameters:
  SSHKey:
    Type: AWS::EC2::KeyPair::KeyName
    Description: nom de la paire de clés pour se connecter en ssh à l'instance
Resources:
  SampleNodejsDeploy:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-014d05e6b24240371
      KeyName: !Ref SSHKey
      SecurityGroups:
        - !Ref SampleNodejsDeploySG
      UserData: 
        Fn::Base64:
          |
          #!/bin/bash 
          set -e
          curl -sL https://deb.nodesource.com/setup_16.x | bash -
          sudo apt install nodejs
          node -v
          npm -v
          curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
          echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
          sudo apt update && sudo apt install yarn
          yarn --version
          sudo -i -u ubuntu bash << EOF
          set -e
          cd /home/ubuntu
          sudo npm install -g pm2
          git clone https://github.com/5minslearn/node_with_docker.git
          cd node_with_docker
          yarn install 
          pm2 start yarn --time --interpreter bash --name sample_node -- start -p 8000
          EOF
            
  SampleNodejsDeploySG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: pour les nœuds de l'application qui permettent ssh, http 
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: '8000'
        ToPort: '8000'
        CidrIp: 0.0.0.0/0

```

Dans le modèle ci-dessus, nous avons ajouté un paramètre pour obtenir le nom de la paire de clés et l'avons référencé à la propriété `KeyName`.

Super ! Nous avons créé avec succès un modèle CloudFormation pour créer une instance EC2 et un groupe de sécurité. En plus de cela, nous avons également ajouté un script pour déployer l'application NodeJS. Maintenant, il est temps de créer une pile CloudFormation.

## Comment créer une pile CloudFormation

La première étape consiste à se connecter à la console AWS et à rechercher CloudFormation dans la barre de recherche (voir la capture d'écran ci-dessous). Cliquez sur les piles dans la barre latérale gauche pour commencer avec CloudFormation.

![Image](https://lh6.googleusercontent.com/tIzQQwxjsDLgPxI65f8l9jcAtw90UVVCRakld4M9h8ZUJrMvMhPVxPuSHm_Pdr-UZO1YPeAFTSP_6CU9fNx7a99Hjp04LnhkmmzG9ZdhEvi-o9mqil-vr6yKFYkdDv21AK1s13rKAVQue6l09MOFEpU)
_CloudFormation Getting Started_

Cliquez sur le bouton créer une pile pour créer la pile CloudFormation.

![Image](https://lh4.googleusercontent.com/64WKWRSq7334K9DEXzOmuE_u-sDWUcSO3ZqpAhhJqFOnLC0Alp7NbP38PWjB0fj_qZw5sookagPnANLkJfjVASZrCwF4OODljGNdLdMKeaSrQfGg7BiyHmopUWBEQcIh1JuRWHZlvYgnFqxzyfTACpo)
_Create CloudFormation Stack_

Comme nous avons notre modèle prêt, sélectionnez "Le modèle est prêt" et choisissez "Télécharger un fichier de modèle" dans la section Source du modèle, et téléchargez le fichier de modèle.

![Image](https://lh5.googleusercontent.com/KsaSLPVYV3UbphozR2kSzWR9ICXWnW1O6w2H5ooT_AmfxWknCCkfZ3km3fT2nscCsekhxgz6zrcphBY5l8olGTzPX5ZcmxoAwGFXPg92B4W9N1BVbUwUGdLq43gfD1FGIdj9O60vpO25wI9-3DJvBok)
_Deploying CloudFormation Template_

Une fois que vous avez téléchargé le fichier, le bouton "Voir dans le concepteur" sera activé. Cliquez dessus pour voir la conception de votre modèle.

## Comment valider le modèle CloudFormation

![Image](https://lh3.googleusercontent.com/Ddg61T-pDsR33QjMFGyVk7sIhDDs7qQ9nVQd6P1vOn5RY7DtlquWnEWFrzmDHH_4Ny78jzuAlmOg49ONtKw0XcxcDDjJtAqAEALC3RNsSuhwuFgkgQz_UzldzSHwPfwoGhEAnwALs8jlcq9_FyKUglU)
_Validate CloudFormation Template_

Pour valider notre modèle, cliquez sur l'icône "Cocher" en haut à gauche dans le concepteur. Il validera et nous montrera les erreurs le cas échéant. Une fois la validation terminée, cliquez sur l'icône "Nuage" à gauche de l'icône "Cocher". Cela vous mènera à la page de création de pile.

Dans la page des détails de la pile, entrez le nom de la pile et sélectionnez votre paire clé-valeur. Si vous n'avez pas de paire clé-valeur, créez-en une et sélectionnez-la.

![Image](https://lh4.googleusercontent.com/o9myUy3ijGaRzsqsISNq0eoMB6_JyvmJyF2JiwkKxbCoDPFKPTOHSiC5I5ioZP1CXQAyraUYLT72u17sKtZfIaRyHWnJLojFqumkaeEXeFXhMwBL1-rnmvZOSpemDDZ-axzGtxmfYAm0RQi1Pf7VUu8)
_Specify CloudFormation stack details_

Laissez la section Configurer les options de pile telle quelle et cliquez sur continuer puisque nous n'avons pas besoin de permissions IAM ou d'options avancées.

Enfin, passez en revue la page et soumettez le modèle. Le modèle commencera à créer les ressources.

![Image](https://lh4.googleusercontent.com/wsD_CWoQk3P90rku7vPiC0uozKlj6fwYdmoZfP3SggCDOwLs5g1hshhK3crKMoDkvvTILf8206AktFBDQ1IeVDAPQ5ksPmYDAhu7v2h7R9Rg7mb9qSETOYQHhEoXNvOFyTD8sgf_AbHGO7MaGTNIjIE)
_CloudFormation stack creating resources_

Une fois cela fait, cliquez sur l'onglet ressources. Vous pourrez voir les ressources que nous avons créées (ressources EC2 et groupe de sécurité).

![Image](https://www.freecodecamp.org/news/content/images/2023/04/1.png)
_Resources created by CloudFormation Template_

Cliquez sur l'instance EC2, et vous verrez que notre instance est en cours d'exécution. Copiez l'adresse IPv4 publique.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/2.png)
_EC2 instance up and running_

Ouvrez votre navigateur et accédez à `http://<ip_address>:8000` (dans mon cas, c'est `http://54.176.19.18:8000/`). Vous devriez voir une page similaire à celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-from-2023-04-14-02-35-22.png)
_NodeJS app running_

Cela indique que notre application NodeJS est déployée avec succès !

**Note :** Les données utilisateur EC2 prendront un certain temps pour installer les dépendances. Donc, la première fois, la page mettra longtemps à se charger. Soyez patient jusqu'à ce que le site soit chargé.

## Comment supprimer la pile CloudFormation

Si vous n'avez plus besoin de la pile, vous pouvez la supprimer depuis la console CloudFormation.

Sélectionnez la pile que vous souhaitez supprimer, cliquez sur "Supprimer la pile" et confirmez l'action. Cette action supprimera toutes les ressources créées à l'aide de cette pile. Dans notre cas, elle supprimera à la fois EC2 et le groupe de sécurité. Vous n'avez pas besoin de supprimer l'instance EC2 et le groupe de sécurité individuellement.

![Image](https://lh5.googleusercontent.com/qIonqqdC9U22tCeGsJXtcLG6U5LaiCnbNATAzNBKA8bKXttf9GLhHRMa28F9oMYE_W1OjeoPCdrDnlUk569rwnPlMFgcVKjLOc-oKYQxHYKA_SkrzI4UBjgTlf5gCrGukTTDuXR61pa8I5OWDMSd5Gg)
_Deleting CloudFormation stack_

## Conclusion

Dans cet article, nous avons appris ce qu'est CloudFormation, comment il fonctionne et comment créer et supprimer une pile de modèles.

J'espère que vous avez apprécié la lecture de cet article ! Si vous êtes bloqué à un moment donné, n'hésitez pas à me poser vos questions à mon [email](mailto:arun@gogosoon.com). Je serai ravi de vous aider.

Si vous souhaitez en savoir plus sur AWS, abonnez-vous à ma [newsletter](https://5minslearn.gogosoon.com/?ref=fcc_cloud_formation) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_cloud_formation)) et suivez-moi sur les réseaux sociaux.