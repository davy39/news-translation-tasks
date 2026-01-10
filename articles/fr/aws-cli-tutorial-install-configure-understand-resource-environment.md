---
title: Tutoriel AWS CLI – Comment installer, configurer et utiliser AWS CLI pour comprendre
  votre environnement de ressources
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-05-11T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-cli-tutorial-install-configure-understand-resource-environment
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/keyboard.png
tags:
- name: AWS
  slug: aws
- name: aws cli
  slug: aws-cli
- name: Cloud Computing
  slug: cloud-computing
- name: cloudformation
  slug: cloudformation
seo_title: Tutoriel AWS CLI – Comment installer, configurer et utiliser AWS CLI pour
  comprendre votre environnement de ressources
seo_desc: 'How to get exactly the account and environment information you need to
  manage your AWS account using just the AWS CLI

  Installing the AWS CLI is actually quite simple. The best way to get it done is
  to head over to the AWS installation guide and follo...'
---

_Comment obtenir exactement les informations de compte et d'environnement dont vous avez besoin pour gérer votre compte AWS en utilisant uniquement l'AWS CLI_

L'installation de l'AWS CLI est en réalité assez simple. La meilleure façon de le faire est de se rendre sur le [guide d'installation d'AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) et de suivre les instructions pour votre système d'exploitation.

Actuellement, ils nous poussent vers la version 2 de la CLI et je n'ai vu aucune raison de ne pas suivre. Je travaille avec Linux, donc c'est là que je me dirigerais ensuite.

Pour le faire, je vais coller la commande curl de la page Amazon dans mon shell Linux qui téléchargera le package et l'écrira dans un fichier zip local, que je décompresserai ensuite. Cela créera un nouveau répertoire appelé aws qui contiendra un script d'installation, que je peux exécuter en utilisant sudo pour obtenir les privilèges admin. Je vais exécuter aws --version pour confirmer que tout a fonctionné comme prévu.

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
ls aws
sudo ./aws/install
aws --version

```

L'étape suivante nécessitera un rapide passage par la console de gestion. Vous voyez, pour authentifier la CLI à votre compte, vous aurez besoin d'une clé d'accès valide. Maintenant, la CLI dispose d'une commande "create-access-key" qui générera une nouvelle clé, mais cela n'est possible qu'une fois que je me suis authentifié. Je suis sûr que vous comprenez le problème avec cela.

Vous accédez à la page des informations d'identification de sécurité à partir du menu déroulant du compte en haut de n'importe quelle page de la console. Avec vos informations d'identification en main, vous pouvez exécuter "aws configure". Vous serez invité à entrer votre ID de clé d'accès et la clé secrète elle-même. Si vous le souhaitez, vous pouvez ensuite choisir une région AWS par défaut et un format de sortie. Le format ne posera pas de problème, donc je vais le laisser par défaut.

```
aws configure

```

C'est tout. Juste pour confirmer que tout a fonctionné, je vais lister tous les buckets S3 de mon compte. Avec cela, nous serons tous prêts à nous mettre au travail dans le prochain clip.

```
aws s3 ls

```

Vous savez peut-être déjà que le service CloudFormation d'Amazon existe pour vous permettre de gérer l'infrastructure de votre application en l'organisant en piles de ressources de votre compte AWS.

Les modèles CloudFormation qui définissent ces piles peuvent être partagés, modifiés et lancés n'importe où, vous offrant des environnements d'application cloud prévisibles et fiables où et quand vous en avez besoin.

Vous savez peut-être aussi que vous pouvez gérer vos piles CloudFormation à la fois via la console de gestion AWS et, comme je le discute dans mon [nouveau cours Pluralsight, Créer et gérer des piles avec AWS CloudFormation en utilisant l'interface de ligne de commande](https://pluralsight.pxf.io/EMPE2), en utilisant l'AWS CLI.

Si vous choisissez d'utiliser l'AWS CLI – ce que je recommande vivement – vous aurez besoin d'un moyen de recueillir des informations clés sur d'autres ressources de compte. Mais comment vous êtes censé obtenir ces informations via la CLI peut, au premier abord, ne pas sembler si évident.

Pour vous montrer ce que je veux dire, expérimentons avec une pile plus complexe en utilisant un modèle qui provient des exemples de documentation AWS.

L'ensemble de modèles [Application Frameworks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-appframeworks-us-east-1.html) inclut un modèle pour des serveurs Linux auto-scalés qui seront pré-provisionnés avec le serveur web Apache et le langage de script PHP, et une connexion à une instance de base de données RDS Multi-AZ exécutant le moteur de base de données MySQL.

Vous pouvez cliquer sur View depuis cette page de documentation AWS et jeter un coup d'œil au modèle lui-même. Vous y verrez des sections Paramètres définissant le VPC et les sous-réseaux dans lesquels votre instance sera lancée et le nom de la base de données MySQL, l'utilisateur et le mot de passe.

Il est crucial que tous les bons services connaissent ces détails car, sinon, ils ne pourront pas communiquer entre eux. Nous devrons trouver un moyen d'ajouter ces valeurs. Pour commencer, vous pouvez simplement cliquer pour voir le modèle ([que vous pouvez voir ici](https://s3.amazonaws.com/cloudformation-templates-us-east-1/LAMP_Multi_AZ.template)), et copier le contenu, le coller dans un nouveau fichier JSON sur votre machine locale.

Vous utilisez la CLI pour lancer une pile CloudFormation en utilisant la commande create-stack. La commande, cependant, prend quelques arguments pour passer des informations importantes. Cet exemple minimal vous montre comment pointer CloudFormation vers votre fichier de modèle JSON, un nom à attribuer à votre pile, et une clé SSH valide pour que je puisse me connecter à l'instance qu'elle crée.

```
aws cloudformation create-stack \
  --template-body file://lamp-as.json \
  --stack-name lamp \
  --parameters \
  ParameterKey=KeyName,ParameterValue=mykey

```

Le problème est que, si vous deviez exécuter cette commande contre le modèle dans votre document JSON, elle échouerait. C'est parce que, comme vous vous en souviendrez sans doute en regardant le modèle, il y a quelques paramètres supplémentaires qui doivent être satisfaits. Plus précisément, nous aurons besoin de références à un VPC et à deux sous-réseaux - et parce que cela est un déploiement multi-zone de disponibilité, ils devront être dans différentes zones.

Comment cela va-t-il fonctionner ? C'est l'AWS CLI à la rescousse. Besoin d'un ID de VPC ? En gardant à l'esprit que les VPC sont des objets EC2, vous pouvez exécuter aws ec2 describe-vpcs et toutes les données dont vous aurez besoin - y compris l'ID de VPC - apparaîtront magiquement. Et les sous-réseaux ? Eh bien, plus de la même chose, évidemment. Il suffit de copier les ID de sous-réseau pour deux des sous-réseaux qui apparaîtront et vous êtes en affaires.

```
aws ec2 describe-vpcs
aws ec2 describe-subnets

```

Maintenant, rassemblons toutes ces informations dans notre nouvelle version de la commande create-stack. Vous devrez être prudent avec cela car il y a quelques pièges désagréables dans la syntaxe.

```
aws cloudformation create-stack \
  --template-body file://lamp-as.json \
  --stack-name lamp-as \
  --parameters \
  ParameterKey=KeyName,ParameterValue=mykey \
  ParameterKey=VpcId,ParameterValue=vpc-1ffbc964 \
  ParameterKey=Subnets,ParameterValue=\'subnet-0e170b31,subnet-52d6117c\' \
  ParameterKey=DBUser,ParameterValue=myadmin \
  ParameterKey=DBPassword,ParameterValue=mypass23

```

Le premier nouveau paramètre est VPC-ID. Mais assurez-vous d'avoir la bonne casse : utiliser un D majuscule dans Id fera échouer tout le processus. Je ne sais pas pourquoi ils rendent les choses si difficiles à vivre, mais c'est ce que nous avons.

Le suivant est encore plus délicat. Puisque nous avons besoin de deux sous-réseaux, nous devrons les entrer sur une seule ligne séparés par une virgule - mais sans espace. Cependant, nous devrons également enfermer la chaîne dans des apostrophes. Mais la CLI ne peut pas lire les apostrophes comme ça, donc nous devrons les échapper en utilisant des barres obliques inverses. Vous avez compris ?

Je vais également ajouter ces deux paramètres de base de données : DBUser et mon ultra-secret, super cryptique DBPassword. Est-ce que cela fonctionnera ? Vous pariez. Mais ne dites à personne combien de fois j'ai dû essayer cela sans que vous regardiez avant de réussir. Souvenez-vous : l'échec est votre ami.

Lorsque notre pile est bien lancée (ce qui peut prendre jusqu'à une demi-heure), l'exécution de describe-stacks nous donnera notre URL de site web.

```
aws cloudformation describe-stacks

```

Mais ce n'est pas toute l'histoire. Je vais utiliser une autre commande aws ec2 - describe-instances cette fois - pour obtenir des informations sur les instances EC2 qui ont été lancées dans le cadre de cette pile. Celle-ci filtrera les résultats, restreignant la sortie aux seules instances qui sont actuellement en cours d'exécution.

```
aws ec2 describe-instances \
  --filters Name=instance-state-name,Values=running \
  --query 'Reservations[*].Instances[*].{Instance:InstanceId,PublicIPAddress:PublicIpAddress}'

```

Il se trouve que je n'ai pas d'autres instances en cours d'exécution dans cette région, donc seules les instances CloudFormation apparaîtront. Maintenant, j'utilise --query pour filtrer davantage la sortie afin de ne me donner que les ID d'instance et les adresses IP publiques de ces instances. Il y en a, comme vous vous en doutez, exactement deux en cours d'exécution.

Juste un avant-goût - et la plupart d'entre eux sont spécifiquement liés à CloudFormation - mais je pense que vous comprenez l'idée de la collecte d'informations en utilisant l'AWS CLI.

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com)._