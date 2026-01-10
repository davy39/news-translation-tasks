---
title: Qu'est-ce que l'Infrastructure as Code ? (Tutoriel)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-11-16T15:02:13.000Z'
originalURL: https://freecodecamp.org/news/what-is-infrastructure-as-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/iac.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: youtube
  slug: youtube
seo_title: Qu'est-ce que l'Infrastructure as Code ? (Tutoriel)
seo_desc: 'What is Infrastructure as Code?

  In this article you will learn all about Infrastructure as Code. I will start with
  an overview of the general concepts, and then I will show you how to implement Infrastructure
  as Code with three different labs. The la...'
---

Qu'est-ce que l'Infrastructure as Code ?

Dans cet article, vous apprendrez tout sur l'Infrastructure as Code. Je commencerai par un aperçu des concepts généraux, puis je vous montrerai comment implémenter l'Infrastructure as Code avec trois laboratoires différents. Les laboratoires utilisent Python et AWS, mais les concepts s'appliqueront à d'autres langages de programmation et fournisseurs de cloud.

Il existe également une version vidéo de cet article. Vous pouvez regarder la [vidéo sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/EtEb40LE5zQ) (1 heure de visionnage).

%[https://youtu.be/EtEb40LE5zQ]

Commençons par parler de ce qu'est l'infrastructure as code. Pour faire simple, il s'agit de configurer votre infrastructure en tant que code.

Par infrastructure, j'entends toutes les différentes choses nécessaires pour déployer votre logiciel dans un environnement cloud. Cela peut signifier des choses comme des machines virtuelles, des conteneurs ou des fonctions serverless. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-92.png)

L'infrastructure signifie également toutes les autres pièces d'infrastructure que vous devez configurer pour réussir. Cela peut être la sécurité comme IAM et KMS, ou le réseau, ou certaines des capacités de surveillance et de journalisation.

Vous pouvez également utiliser du code pour configurer et mettre en place des magasins de données. Ce sont les choses dont votre application a besoin pour stocker et gérer des données.

La dernière pièce du paysage de l'infrastructure est les applications elles-mêmes et l'obtention des applications que nous construisons dans l'infrastructure.

Toutes ces différentes pièces d'infrastructure peuvent être configurées à l'aide de code. 

Il devient de plus en plus important d'automatiser l'infrastructure car les applications peuvent être déployées en production jusqu'à cent fois par jour. Vous ne voulez pas avoir à le faire manuellement.

De plus, il est utile d'automatiser l'infrastructure pour qu'elle soit provisionnée ou désapprovisionnée en réponse à la charge.

L'infrastructure as code consiste à trouver un moyen de décrire à l'aide de code ce que les pièces de notre infrastructure doivent faire.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-93.png)

Au fil des ans, il y a eu une transition dans la manière dont les gens utilisent l'infrastructure cloud au sein de leurs organisations.

Dans la première vague, c'était relativement simple. Les infrastructures étaient assez statiques. Il s'agissait souvent d'une seule machine virtuelle à laquelle on accédait simplement via SSH.

C'est devenu un peu plus complexe dans la deuxième vague. Il y avait plus de conteneurs et les gens ont commencé à utiliser des outils de provisionnement pour spécifier les comportements des applications. Les gens utilisaient Docker et DataDog.

L'infrastructure cloud moderne a ajouté beaucoup plus de complexité. Elle utilise des conteneurs, du serverless et plus de services gérés dans le cadre des applications. Il y a maintenant beaucoup plus de pièces différentes impliquées dans la manière dont les gens construisent l'infrastructure.

L'infrastructure as code devient une partie plus importante de la manière dont les gens construisent et livrent des applications car l'infrastructure as code est ce qui décrit le lien entre toutes les différentes arêtes de ces diagrammes.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-94.png)
_Infrastructure Moderne_

Le diagramme de l'infrastructure moderne peut sembler plus compliqué que les précédents, mais il peut en réalité être plus facile à maintenir. Un avantage clé est que les carrés gris foncé dans le diagramme sont la seule partie qui est le code que vous possédez. Et cette partie est plus petite que les méthodes précédentes de faire les choses. Ainsi, une grande partie de la charge opérationnelle a été réduite par rapport à la manière dont cela était fait auparavant.

Avec l'infrastructure as code, vous confiez une partie de la charge opérationnelle à AWS, Azure, Kubernetes ou un autre système. Maintenant, l'accent est mis sur le lien entre les différents services qui sont gérés par un fournisseur de cloud.

Le code d'infrastructure prend un rôle de plus en plus important dans la manière dont vous gérez tout dans le cloud moderne.

Voici donc les trois principales méthodes qui peuvent être utilisées pour gérer toutes les ressources :

* **manuel** : pointer et cliquer pour créer/modifier des ressources dans la console. 
* **automatisation ad-hoc** : commandes CLI ou scripts pour créer/modifier des ressources. 
* **infrastructure as code** :   
 **provisionnement** : créer/modifier des ressources de manière déclarative.   
 **configuration** : changer l'état d'une ressource existante après le provisionnement.

L'infrastructure as code nous donne la capacité d'écrire ce que nous voulons que l'état souhaité de notre infrastructure soit. Je vais vous montrer exactement comment faire ces choses plus tard.

## Écrire de l'Infrastructure as Code

Une approche de l'infrastructure as code est d'utiliser JSON. Voici un exemple :

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "EC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "InstanceType": "t2.micro",
        "SecurityGroups": [
          {
            "Ref": "InstanceSecurityGroup"
          }
        ],
        "ImageId": "ami-0080e4c5bc078760e"
      }
    },
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Enable HTTP over port 80",
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": "80",
            "ToPort": "80",
            "CidrIp": "0.0.0.0/0"
          }
        ]
      }
    }
  }
}
```

Ce qui précède est un moyen de dire à AWS quelles ressources vous souhaitez avoir.

Une autre méthode consiste à utiliser un langage spécifique de domaine (DSL). Il s'agit d'une méthode personnalisée spécifique à l'outil ou au fournisseur de cloud que vous utilisez. Voici un exemple :

```
provider aws {
    region = "eu-central-1"
}
resource "aws_security_group"
"web_sg" {
    description = "Enable HTTP over port 80"
    ingress {
        protocol = "tcp"
        from_port = 80
        to_port = 80
        cidr_blocks = ["0.0.0.0/0"]
    }
}
resource "aws_instance"
"web" {
    ami = "ami-0080e4c5bc078760e"
    instance_type = "t2.micro"
    security_groups = ["$(aws_security_group.web_sg.id)"]
}
```

Une autre façon de définir l'infrastructure à l'aide de code est d'utiliser un langage de programmation bien connu. Par exemple, Pulumi peut être utilisé pour écrire de l'infrastructure as code en utilisant TypeScript, JavaScript, Python, Go et .NET.

Voici un exemple utilisant TypeScript (et plus tard nous utiliserons Python).

```typescript
import * as aws from "@pulumi/aws";
let group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP over port 80",
    ingress: [{
        protocol: "tcp",
        fromPort: 80,
        toPort: 80,
        cidrBlocks: ["0.0.0.0/0"]
    }, ],
});
for (let az in aws.getAvailabilityZones().names) {
    let server = new aws.ec2.Instance(`web-${az}`, {
        instanceType: "t2.micro",
        securityGroups: [group.id],
        ami: "ami-0080e4c5bc078760e",
        availabilityZone: az,
    });
}
```

L'utilisation de code donne la capacité de faire des choses qui ne sont pas possibles dans certaines des autres méthodes. Dans l'exemple ci-dessus, il y a une boucle `for` qui crée une instance pour chaque zone de disponibilité. Le code donne la capacité d'utiliser des boucles, des conditionnelles, des classes, des packages, et plus encore. L'utilisation de langages de programmation populaires permet également l'utilisation d'IDE communs, de linters et de frameworks de test.

## Laboratoires

Il existe quelques services différents qui vous permettent d'utiliser des langages populaires pour créer de l'infrastructure as code. Dans cet article, nous utiliserons Pulumi.

Cet article (et le cours vidéo) a été rendu possible grâce à une subvention de Pulumi.

Pulumi est un outil open source d'infrastructure as code pour créer, déployer et gérer l'infrastructure cloud. Pulumi fonctionne avec l'infrastructure traditionnelle comme les VM, les réseaux et les bases de données, en plus des architectures modernes, y compris les conteneurs, les clusters Kubernetes et les fonctions serverless. Pulumi supporte des dizaines de fournisseurs de services cloud publics, privés et hybrides.

Nous utiliserons Python et déployerons sur AWS, bien que cela puisse être fait avec d'autres langages de programmation et fournisseurs de cloud.

# Laboratoire 1 : Provisionnement d'infrastructure avec un bucket S3

Nous commencerons par un exemple simple. Cela montrera une expérience complète de travail avec Pulumi en utilisant des ressources très simples.

Dans ce premier exemple, nous ferons ce qui suit :

* Créer un nouveau projet
* Configurer AWS
* Provisionner l'infrastructure
* Mettre à jour l'infrastructure
* Rendre votre pile configurable
* Créer une deuxième pile
* Détruire votre infrastructure

Nous utiliserons un bucket S3, puis nous travaillerons à travers le cycle de vie avec un ensemble simple de ressources. Ensuite, dans les exemples futurs, vous apprendrez comment implémenter des choses plus complexes.

Avec Pulumi, l'infrastructure est organisée en projets. Chaque projet est un programme unique qui, lorsqu'il est exécuté, déclare l'infrastructure souhaitée pour que Pulumi la gère.

Avant de commencer le premier laboratoire, assurez-vous que Pulumi est installé. La manière de l'installer est différente selon votre système d'exploitation. 

Si vous avez MacsOS et [Homebrew](https://brew.sh/), vous pouvez utiliser la commande `brew install pulumi`.

Si vous avez Windows et [Chocolatey](https://chocolatey.org/), vous pouvez utiliser la commande `choco install pulumi`.

[Cette page vous donnera des moyens supplémentaires d'installer Pulumi](https://www.pulumi.com/docs/get-started/install/).

### AWS

Pour cet exemple, nous utilisons AWS. Vous devrez vous assurer d'avoir un compte AWS et d'avoir le CLI configuré et authentifié. ([Il existe également une méthode](https://www.pulumi.com/docs/intro/cloud-providers/aws/setup/) qui n'utilise pas le CLI.)

Vous pouvez vous inscrire pour un compte AWS gratuit ici : [https://aws.amazon.com/free/](https://aws.amazon.com/free/)

Apprenez comment installer le CLI AWS pour votre système d'exploitation ici : [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

Pour MacOS, vous pouvez utiliser ces commandes :

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

Pour Windows, il y a quelques étapes supplémentaires et vous devriez simplement [suivre les instructions ici](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html).

Ensuite, vous devez obtenir un ID de clé d'accès et une clé d'accès secrète d'AWS. [Suivez les instructions d'Amazon pour obtenir ceux-ci](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds).

Maintenant, exécutez ce qui suit dans la ligne de commande :

`aws configure`

Entrez votre ID de clé d'accès et votre clé d'accès secrète lorsque vous y êtes invité. Vous pouvez garder le "Nom de la région par défaut" et le "Format de sortie par défaut" comme None.

### Étape 1 : Créer un répertoire

Chaque projet Pulumi vit dans son propre répertoire. Créez-en un maintenant et changez-le :

`mkdir iac-lab1 cd iac-lab1`

### Étape 2 : Initialiser votre projet

Un projet Pulumi est simplement un répertoire avec quelques fichiers dedans. Il est possible pour vous de créer un nouveau projet à la main. La commande `pulumi new`, cependant, automatise le processus :

`pulumi new python -y`

Si c'est la première fois que vous utilisez Pulumi, vous serez dirigé pour entrer un code d'accès ou vous connecter. Pour obtenir un code d'accès, allez sur [https://app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens)

Cette commande a créé tous les fichiers dont nous avons besoin, initialisé une nouvelle pile nommée `dev` (une instance de notre projet). Nous devons maintenant installer nos dépendances dans le cadre de notre `virtualenv`.

### Étape 3 : Configurer l'environnement virtuel

Nous devons maintenant créer un environnement virtuel et installer les packages Python requis. Le module Python utilisé pour créer et gérer les environnements virtuels s'appelle [`venv`](https://docs.python.org/3/library/venv.html#module-venv). Exécutez les commandes suivantes :

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Étape 4 : Inspecter votre nouveau projet

Notre projet est composé de plusieurs fichiers :

* **`__main__.py`** : le fichier principal d'entrée de votre programme
* **`requirements.txt`** : les informations de dépendance pip de votre projet
* **`Pulumi.yaml`** : les métadonnées de votre projet, contenant son nom et son langage

Si vous regardez dans le fichier `__main__.py`, vous remarquerez une seule ligne de code :

`import pulumi`

### Configurer AWS

Maintenant que vous avez un projet de base, configurons le support AWS pour celui-ci.

### Étape 5 : Installer le package AWS

Exécutez la commande suivante pour installer le package AWS :

`pip3 install pulumi-aws`

### Étape 6 : Importer le package AWS

Maintenant que le package AWS est installé, ajoutez la ligne suivante à `__main__.py` pour l'importer :

`import pulumi_aws as aws`

### Étape 7 : Configurer une région AWS

Configurez la région AWS dans laquelle vous souhaitez déployer en exécutant la commande suivante sur la ligne de commande.

`pulumi config set aws:region us-east-1`

Vous pouvez choisir une région AWS différente si vous le souhaitez. ([Voir ce tableau](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) pour une liste des régions disponibles.)

### Étape facultative : Configurer un profil AWS

Si vous utilisez un profil AWS alternatif, vous pouvez indiquer à Pulumi lequel utiliser de deux manières :

* En utilisant une variable d'environnement : `export AWS_PROFILE=<nom du profil>`
* En utilisant la configuration : `pulumi config set aws:profile <nom du profil>`

### Provisionnement de l'infrastructure

Maintenant que vous avez un projet configuré pour utiliser AWS, vous allez créer une infrastructure de base. Nous commencerons par un simple bucket S3.

### Étape 8 : Déclarer un nouveau bucket

Ajoutez ce qui suit à votre fichier `__main__.py` :

`bucket = aws.s3.Bucket("my-bucket")`

Ainsi, le fichier complet devrait ressembler à ceci :

```
import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("my-bucket")
```

### Étape 9 : Prévisualiser vos modifications

Maintenant, prévisualisez vos modifications :

```
pulumi up

```

Cette commande évalue votre programme, détermine les mises à jour des ressources à effectuer et vous montre un aperçu de ces modifications :

```
Previewing update (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/dev/previews/827f9488-cc23-441f-946a-9852090ab0e3

     Type                 Name          Plan
 +   pulumi:pulumi:Stack  iac-lab1-dev  create
 +    aws:s3:Bucket     my-bucket     create

Resources:
    + 2 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Il s'agit d'une vue sommaire. Sélectionnez `details` pour afficher l'ensemble complet des propriétés :

```
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:dev::iac-lab1::pulumi:pulumi:Stack::iac-lab1-dev]
    + aws:s3/bucket:Bucket: (create)
        [urn=urn:pulumi:dev::iac-lab1::aws:s3/bucket:Bucket::my-bucket]
        [provider=urn:pulumi:dev::iac-lab1::pulumi:providers:aws::default_4_22_1::04da6b54-80e4-46f7-96ec-b56ff0331ba9]
        acl         : "private"
        bucket      : "my-bucket-185b4e1"
        forceDestroy: false

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

La ressource de pile est une ressource synthétique à laquelle toutes les ressources créées par votre programme sont parentées.

### Étape 10 : Déployer vos modifications

Maintenant que nous avons vu l'ensemble complet des modifications, déployons-les. Sélectionnez `yes` :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/dev/updates/1

     Type                 Name          Status
 +   pulumi:pulumi:Stack  iac-lab1-dev  created
 +    aws:s3:Bucket     my-bucket     created

Resources:
    + 2 created

Duration: 5s
```

Notre bucket S3 a maintenant été créé dans notre compte AWS. Si vous consultez vos buckets sur le site Web d'AWS, vous verrez le nouveau bucket. Si vous allez à l'URL indiquée dans la sortie, vous serez redirigé vers la [Console Pulumi](https://www.pulumi.com/docs/intro/console/), qui enregistre votre historique de déploiement.

### Étape 11 : Exporter le nom de votre nouveau bucket

Pour inspecter votre nouveau bucket, vous aurez besoin de son nom physique AWS. Pulumi enregistre un nom logique, `my-bucket`, cependant le nom AWS résultant sera différent.

Les programmes peuvent exporter des variables qui seront affichées dans le CLI et enregistrées pour chaque déploiement. Exportez le nom de votre bucket en ajoutant cette ligne à la fin de `__main__.py` :

`pulumi.export('bucket_name', bucket.bucket)`

Maintenant, déployez les modifications avec :

`pulumi up`

Vous remarquerez maintenant une nouvelle section `Outputs` dans la sortie affichant le nom du bucket :

```
Outputs:
  + bucket_name: "my-bucket-25cb812"
```

Vous pouvez sélectionner "Yes" pour effectuer la mise à jour.

### Étape 12 : Inspecter votre nouveau bucket

Vous pouvez voir toutes les sorties en exécutant `pulumi stack output`.

Le résultat devrait ressembler à ceci :

```
Current stack outputs (1):
    OUTPUT       VALUE
    bucket_name  my-bucket-25cb812
```

Ensuite, vous pouvez exécuter la commande `aws` CLI pour lister les objets dans ce nouveau bucket (en obtenant le nom du bucket en utilisant la commande ci-dessus) :

```
aws s3 ls $(pulumi stack output bucket_name)

```

Il n'y aura actuellement aucun résultat de cette commande puisque le bucket est encore vide.

### Mettre à jour votre infrastructure

Nous venons de voir comment créer une nouvelle infrastructure à partir de zéro. Ensuite, apportons quelques mises à jour :

1. Ajoutez un objet à votre bucket.
2. Servez du contenu à partir de votre bucket en tant que site web.
3. Créez de l'infrastructure de manière programmatique.

Cela démontre comment les outils d'infrastructure as code déclaratifs peuvent être utilisés non seulement pour le provisionnement initial, mais aussi pour les modifications ultérieures des ressources existantes.

### Étape 13 : Ajoutez un objet à votre bucket

Créez un répertoire `site/` et ajoutez un nouveau fichier `index.html` avec le contenu suivant :

```html
<html>
    <body>
        <h1>Bonjour à tous !</h1>
    </body>
</html>
```

Maintenant, mettez à jour votre fichier `__main__.py` pour qu'il ressemble à ceci :

```python
import pulumi
import pulumi_aws as aws
import os

bucket = aws.s3.Bucket("my-bucket")

filepath = os.path.join("site", "index.html")
obj = aws.s3.BucketObject("index.html",
    bucket=bucket.bucket,
    source=pulumi.FileAsset(filepath)
)

pulumi.export('bucket_name', bucket.bucket)
```

Déployez les modifications :

`pulumi up`

Cela vous donnera un aperçu et la sélection de `yes` appliquera les modifications :

```
Previewing update (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/dev/previews/35a07205-2889-403c-b01d-0342eb01ed85

     Type                    Name          Plan
     pulumi:pulumi:Stack     iac-lab1-dev
 +    aws:s3:BucketObject  index.html    create

Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Une seule ressource est ajoutée et les 2 ressources existantes sont laissées inchangées. C'est un attribut clé de l'infrastructure as code — de tels outils déterminent l'ensemble minimal de changements nécessaires pour mettre à jour votre infrastructure d'un changement à l'autre.

Maintenant, listez à nouveau le contenu de votre bucket :

`aws s3 ls $(pulumi stack output bucket_name)`

Vous remarquerez que le fichier `index.html` a été ajouté :

```
2019-10-22 16:50:54        68 index.html

```

### Étape 14 : Servir du contenu à partir de votre bucket en tant que site web

Pour servir du contenu à partir de votre bucket en tant que site web, vous devrez mettre à jour quelques propriétés.

Tout d'abord, votre bucket a besoin d'une propriété de site web qui définit le document d'index par défaut sur `index.html`. Cela peut être réalisé en mettant à jour le fichier `__main__.py` avec ce qui suit :

```
bucket = aws.s3.Bucket("my-bucket",
    website={
        "index_document": "index.html"
})
```

Ensuite, votre objet `index.html` aura besoin de deux modifications : une ACL (Access Control List) de `public-read` afin qu'il puisse être accessible anonymement sur Internet, et un type de contenu afin qu'il soit servi en tant que HTML. Vous devrez également exporter l'URL de point de terminaison du bucket résultant afin que nous puissions y accéder facilement.

En combinant tout, le fichier devrait maintenant ressembler à ceci :

```python
import pulumi
import pulumi_aws as aws
import os
import mimetypes

bucket = aws.s3.Bucket("my-bucket",
    website={
        "index_document": "index.html"
})

filepath = os.path.join("site", "index.html")
mime_type, _ = mimetypes.guess_type(filepath)
obj = aws.s3.BucketObject("index.html",
        bucket=bucket.bucket,
        source=pulumi.FileAsset(filepath),
        acl="public-read",
        content_type=mime_type
)

pulumi.export('bucket_name', bucket.bucket)
pulumi.export('bucket_endpoint', pulumi.Output.concat("http://", bucket.website_endpoint))
```

Maintenant, déployez les modifications :

`pulumi up`

L'aperçu devrait ressembler à ceci :

```
Previewing update (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/dev/previews/50730def-0493-4667-83b8-fcedc4408f3a

     Type                    Name          Plan       Info
     pulumi:pulumi:Stack     iac-lab1-dev
 ~    aws:s3:Bucket        my-bucket     update     [diff: +website]
 ~    aws:s3:BucketObject  index.html    update     [diff: ~acl,contentType]

Outputs:
  + bucket_endpoint: output<string>

Resources:
    ~ 2 to update
    1 unchanged

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

La sélection de `details` pendant l'aperçu contient beaucoup plus d'informations cette fois :

```
  pulumi:pulumi:Stack: (same)
    [urn=urn:pulumi:dev::iac-lab1::pulumi:pulumi:Stack::iac-lab1-dev]
    ~ aws:s3/bucket:Bucket: (update)
        [id=my-bucket-25cb812]
        [urn=urn:pulumi:dev::iac-lab1::aws:s3/bucket:Bucket::my-bucket]
        [provider=urn:pulumi:dev::iac-lab1::pulumi:providers:aws::default_4_22_1::032fffef-7448-4be3-97d2-3198f149eb39]
      + website: {
          + indexDocument: "index.html"
        }
    --outputs:--
  + bucket_endpoint: output<string>
    ~ aws:s3/bucketObject:BucketObject: (update)
        [id=index.html]
        [urn=urn:pulumi:dev::iac-lab1::aws:s3/bucketObject:BucketObject::index.html]
        [provider=urn:pulumi:dev::iac-lab1::pulumi:providers:aws::default_4_22_1::032fffef-7448-4be3-97d2-3198f149eb39]
      ~ acl        : "private" => "public-read"
      ~ contentType: "binary/octet-stream" => "text/html"

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Maintenant, il suffit de sélectionner `yes` pour déployer toutes les mises à jour. Le résultat affichera l'URL qui peut être utilisée pour accéder à votre fichier `index.html`.

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/dev/updates/4

     Type                    Name          Status      Info
     pulumi:pulumi:Stack     iac-lab1-dev
 ~    aws:s3:Bucket        my-bucket     updated     [diff: +website]
 ~    aws:s3:BucketObject  index.html    updated     [diff: ~acl,contentType]

Outputs:
  + bucket_endpoint: "http://my-bucket-25cb812.s3-website-us-east-1.amazonaws.com"
    bucket_name    : "my-bucket-25cb812"

Resources:
    ~ 2 updated
    1 unchanged

Duration: 6s
```

### Étape 15 : Accéder à votre site web

Outre le fait d'aller à l'URL dans un navigateur web (à partir des résultats affichés ci-dessus), vous pouvez également accéder au site web avec cette commande dans le terminal :

`curl $(pulumi stack output bucket_endpoint)`

Cela récupérera et imprimera notre fichier `index.html` :

```
<html>
    <body>
        <h1>Bonjour Pulumi</h1>
    </body>
</html>
```

### Rendre votre pile configurable

Pour l'instant, le contenu du bucket est codé en dur. Ensuite, vous rendrez l'emplacement du contenu configurable et ajouterez la prise en charge du peuplement du bucket avec le contenu d'un répertoire entier.

### Étape 16 : Ajouter une variable de configuration

Au lieu de coder en dur le répertoire `"site"`, nous utiliserons la configuration pour faciliter le changement de l'emplacement sans éditer le programme.

Ajoutez ceci à votre fichier `__main__.py` juste en dessous des imports :

```
config = pulumi.Config()
site_dir = config.require("siteDir")
```

### Étape 17 : Peupler le bucket en fonction de la configuration

Et remplacez le paramètre codé en dur `"site"` par cette variable importée `siteDir` :

```
filepath = os.path.join(site_dir, "index.html")
mime_type, _ = mimetypes.guess_type(filepath)

obj = aws.s3.BucketObject("index.html",
    bucket=bucket.bucket,
    source=pulumi.FileAsset(filepath),
    acl="public-read",
    content_type=mime_type
)
```

Maintenant, voyons comment cela peut être utile. En utilisant le terminal, renommez le répertoire `site` en `www` :

`mv site www`

### Étape 18 : Déployer les modifications

Maintenant, déployez vos modifications. Pour ce faire, configurez d'abord votre pile. Si vous ne le faites pas, vous obtiendrez une erreur :

`pulumi up`

Cela entraîne une erreur comme suit :

```
    error: Missing required configuration variable 'iac-lab1:siteDir'
        please set a value using the command `pulumi config set iac-lab1:siteDir <value>`
    error: an unhandled error occurred: Program exited with non-zero exit code: 1
```

Configurez la variable `iac-workshop:siteDir` de manière similaire à la configuration de la variable `aws:region` :

`pulumi config set iac-lab1:siteDir www`

Ensuite, exécutez :

`pulumi up`

Cela détecte que le chemin a changé et effectuera une simple mise à jour.

### Étape 19 : Ajouter plus de fichiers

Au lieu de coder en dur l'ensemble des fichiers, vous allez maintenant modifier le programme pour lire l'intégralité du contenu du répertoire `www`.

Ajoutez un nouveau fichier nommé `about.html` au répertoire `www` et ajoutez un peu de HTML. Voici une option :

```
<html>
    <p>Je ne suis pas un chat.</p>
</html>

```

Maintenant, remplacez le code d'allocation d'objet par le code ci-dessous. Vous remarquerez qu'il y a maintenant une boucle for pour parcourir chaque fichier dans le répertoire du site :

```
for file in os.listdir(site_dir):
    filepath = os.path.join(site_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = aws.s3.BucketObject(file,
          bucket=bucket.bucket,
          source=pulumi.FileAsset(filepath),
          acl="public-read",
          content_type=mime_type
    )
```

Déployez :

`pulumi up`

Vous verrez un seul nouvel objet créé pour le fichier `about.html` :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/dev/updates/5

     Type                    Name          Status
     pulumi:pulumi:Stack     iac-lab1-dev
 +    aws:s3:BucketObject  about.html    created
```

Vous pouvez maintenant aller à l'URL précédente et ajouter "/about.html" à la fin.

Vous pouvez également obtenir le fichier dans le terminal avec la commande :

`curl $(pulumi stack output bucket_endpoint)/about.html`

### Créer une deuxième pile

Il est facile de créer plusieurs instances du même projet. Dans Pulumi, chaque instance est appelée une pile. Cela est utile si vous avez plusieurs environnements de développement ou de test, de staging versus production, et de mise à l'échelle d'une infrastructure donnée à travers de nombreuses régions.

### Étape 20 : Créer et configurer une nouvelle pile

Créez une nouvelle pile nommée 'prod' :

`pulumi stack init prod`

Ensuite, configurez ses deux variables requises :

```
pulumi config set aws:region eu-west-1
pulumi config set iac-lab1:siteDir wwwprod
```

Vous pouvez voir la liste des piles pour votre projet actuel avec la commande :

`pulumi stack ls`

Il imprimera toutes les piles pour ce projet qui sont disponibles pour vous :

```
NAME   LAST UPDATE     RESOURCE COUNT  URL
dev    12 minutes ago  5               https://app.pulumi.com/beaucarnes/iac-lab1/dev
prod*  n/a             n/a             https://app.pulumi.com/beaucarnes/iac-lab1/prod
```

### Étape 21 : Peupler le nouveau répertoire de site

Nous aurions pu utiliser le répertoire `www` existant pour le `siteDir`. Mais pour cet exemple, vous utiliserez un répertoire `wwwprod` différent pour démontrer comment il peut être configuré.

Donc, créez ce nouveau répertoire :

`mkdir wwwprod`

Ajoutez un nouveau fichier `index.html`. Il peut contenir n'importe quel HTML, mais voici une suggestion :

```
<html>
    <body>
        <h1>Bonjour l'univers.</h1>
        <p>(en production)</p>
    </body>
</html>
```

### Étape 22 : Déployer la nouvelle pile

Maintenant, déployez toutes les modifications :

`pulumi up`

Cela créera un ensemble entièrement nouveau de ressources à partir de zéro, sans lien avec les ressources de la pile `dev` existante.

```
Updating (prod)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/prod/updates/1

     Type                    Name           Status
 +   pulumi:pulumi:Stack     iac-lab1-prod  created
 +    aws:s3:Bucket        my-bucket      created
 +    aws:s3:BucketObject  index.html     created

Outputs:
    bucket_endpoint: "http://my-bucket-0d2f29a.s3-website-eu-west-1.amazonaws.com"
    bucket_name    : "my-bucket-0d2f29a"

Resources:
    + 3 created

Duration: 14s
```

Vous remarquerez une nouvelle URL dans la sortie. Vous pouvez accéder à cette URL dans un navigateur pour voir le nouveau site web.

Vous pouvez également l'obtenir en utilisant cette commande dans le terminal :

`curl $(pulumi stack output bucket_endpoint)`

### Détruire votre infrastructure

La dernière chose que nous couvrirons dans ce premier laboratoire est de détruire toutes les ressources des deux piles créées.

### Étape 23 : Détruire les ressources

Tout d'abord, détruisez les ressources dans votre pile actuelle :

`pulumi destroy`

Cela vous montrera un aperçu, comme le fait la commande `pulumi up` :

```
     Type                    Name           Plan
 -   pulumi:pulumi:Stack     iac-lab1-prod  delete
 -    aws:s3:BucketObject  index.html     delete
 -    aws:s3:Bucket        my-bucket      delete

Outputs:
  - bucket_endpoint: "http://my-bucket-0d2f29a.s3-website-eu-west-1.amazonaws.com"
  - bucket_name    : "my-bucket-0d2f29a"

Resources:
    - 3 to delete

Do you want to perform this destroy?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Pour continuer, sélectionnez `yes`.

```
Destroying (prod)

View Live: https://app.pulumi.com/beaucarnes/iac-lab1/prod/updates/2

     Type                    Name           Status
 -   pulumi:pulumi:Stack     iac-lab1-prod  deleted
 -    aws:s3:BucketObject  index.html     deleted
 -    aws:s3:Bucket        my-bucket      deleted

Outputs:
  - bucket_endpoint: "http://my-bucket-0d2f29a.s3-website-eu-west-1.amazonaws.com"
  - bucket_name    : "my-bucket-0d2f29a"

Resources:
    - 3 deleted

Duration: 3s

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained.
If you want to remove the stack completely, run 'pulumi stack rm prod'.
```

### Étape 24 : Supprimer la pile

Les ressources AWS de cette pile ont été détruites. Vous avez peut-être remarqué le message imprimé à la fin indiquant que l'historique et la configuration associés à la pile sont toujours maintenus. Cela signifie que tout l'historique passé est toujours disponible et que vous pouvez effectuer des mises à jour ultérieures sur cette pile.

Maintenant, supprimez complètement la pile et tout l'historique :

`pulumi stack rm`

Cela est irréversible et demande donc de confirmer que c'est votre intention :

```
This will permanently remove the 'prod' stack!
Please confirm that this is what you'd like to do by typing ("prod"):

```

Tapez le nom de la pile et appuyez sur Entrée. La pile a maintenant disparu.

### Étape 24 : Sélectionner une autre pile, répéter

Après avoir détruit `prod`, vous avez toujours la pile `dev`. Pour la détruire également, sélectionnez-la d'abord :

```
pulumi stack select dev

```

Maintenant, revenez en arrière et répétez les deux étapes précédentes pour la détruire.

### Étape 25 : Vérifier que les piles ont disparu

Vérifiez que toutes les piles de ce projet ont maintenant disparu :

`pulumi stack ls`

## Conclusion du Laboratoire 1

Félicitations ! Vous avez terminé le premier laboratoire. Les prochains laboratoires sont un peu plus courts et démontrent quelques tâches plus avancées.

# Laboratoire 2 : Provisionnement de machines virtuelles EC2

Amazon Elastic Compute Cloud (Amazon EC2) est un service web qui fournit une capacité de calcul sécurisée et redimensionnable dans le cloud. Il est conçu pour faciliter le cloud computing à l'échelle du web pour les développeurs. L'interface de service web simple d'Amazon EC2 vous permet d'obtenir et de configurer une capacité avec un minimum de friction.

Dans ce deuxième laboratoire, vous allez d'abord créer une seule machine virtuelle (VM) EC2. Ensuite, vous allez l'étendre à une VM par zone de disponibilité dans votre région, puis ajouter un équilibreur de charge pour répartir la charge sur toute la flotte.

### Étape 1 : Créer un répertoire

Nous aurions pu utiliser le même projet et répertoire que précédemment. Mais nous allons en créer un nouveau pour avoir plus de pratique.

Créez un nouveau répertoire qui n'est pas à l'intérieur du répertoire utilisé dans le dernier laboratoire.

```
cd ..
mkdir iac-lab2
cd iac-lab2
```

### Étape 2 : Initialiser votre projet

Rappelez-vous, un projet Pulumi est simplement un répertoire avec quelques fichiers dedans. Il est possible pour vous de créer un nouveau projet à la main. La commande `pulumi new`, cependant, automatise le processus :

```bash
pulumi new aws-python -y
```

Cette commande a créé tous les fichiers dont nous avons besoin, initialisé une nouvelle pile nommée `dev` (une instance de notre projet), et installé les dépendances de packages nécessaires depuis PyPi. La partie "aws" de la commande a fait en sorte que notre fichier `__main__.py` commence avec un code d'exemple pour créer un bucket AWS.

### Étape 3 : Configurer une région AWS

Configurez la région AWS dans laquelle vous souhaitez déployer :

```bash
pulumi config set aws:region us-west-2
```

### Étape 4 : Déclarer l'instance EC2

Supprimez tout code existant ici du démarrage de votre projet. Ensuite, importez le package AWS dans un fichier `__main__.py` vide :

```python
from pulumi import export
import pulumi_aws as aws
```

Maintenant, interrogez dynamiquement l'image de la machine Amazon Linux. Faire cela dans le code évite d'avoir à coder en dur l'image de la machine (a.k.a., son AMI - Une image Amazon Machine Image fournit les informations requises pour lancer une instance) :

```python
ami = aws.ec2.get_ami(
    most_recent="true",
    owners=["137112412989"],
    filters=[{"name":"name","values":["amzn-ami-hvm-*-x86_64-ebs"]}])
```

Nous devons également récupérer le Virtual Private Cloud par défaut, un service qui vous permet de lancer des ressources AWS dans un réseau virtuel logiquement isolé que vous définissez, qui est disponible dans notre compte AWS :

```python
vpc = aws.ec2.get_vpc(default=True)
```

Ensuite, créez un groupe de sécurité AWS. Cela permet le `ping` via ICMP et le trafic HTTP sur le port 80 :

```python
group = aws.ec2.SecurityGroup(
    "web-secgrp",
    description='Enable HTTP access',
    vpc_id=vpc.id,
    ingress=[
        { 'protocol': 'icmp', 'from_port': 8, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
])
```

Créez le serveur. Remarquez qu'il a un script de démarrage qui lance un simple serveur web Python :

```python
server = aws.ec2.Instance(
    'web-server',
    instance_type="t2.micro",
    vpc_security_group_ids=[group.id],
    ami=ami.id,
    user_data="""
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
    """,
    tags={
        "Name": "web-server",
    },
)
```

Pour la plupart des applications réelles, vous voudriez créer une image dédiée pour votre application, plutôt que d'intégrer le script dans votre code comme ceci.

Enfin, exportez l'adresse IP et le nom d'hôte résultants des instances EC2 :

```python
pulumi.export('ip', server.public_ip)
pulumi.export('hostname', server.public_dns)
```

Après cette modification, votre fichier `__main__.py` devrait ressembler à ceci :

```python
import pulumi
import pulumi_aws as aws


ami = aws.ec2.get_ami(
    most_recent="true",
    owners=["137112412989"],
    filters=[{"name": "name", "values": ["amzn-ami-hvm-*-x86_64-ebs"]}],
)

vpc = aws.ec2.get_vpc(default=True)

group = aws.ec2.SecurityGroup(
    "web-secgrp",
    description="Enable HTTP Access",
    ingress=[
        {
            "protocol": "icmp",
            "from_port": 8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
)

server = aws.ec2.Instance(
    "web=server",
    instance_type="t2.micro",
    vpc_security_group_ids=[group.name],
    ami=ami.id,
    user_data="""
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
    """,
    tags={
        "Name": "web-server",
    },
)

pulumi.export("ip", server.public_ip)
pulumi.export("hostname", server.public_dns)
```

### Étape 5 : Provisionner l'instance EC2 et y accéder

Pour provisionner la VM, exécutez :

```bash
pulumi up
```

Après confirmation, vous verrez une sortie similaire à ce qui suit :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab2/dev/updates/3

     Type                 Name          Status
     pulumi:pulumi:Stack  iac-lab2-dev
 ~    aws:ec2:Instance  web=server    updated

Outputs:
    hostname: "ec2-52-13-25-152.us-west-2.compute.amazonaws.com"
    ip      : "52.13.25.152"

Resources:
    ~ 1 updated
    2 unchanged

Duration: 8s
```

Si vous obtenez une erreur, essayez d'exécuter à nouveau `pulumi up` et confirmez. La première fois que je l'ai exécuté, il y avait une condition de course qui nécessitait de réexécuter la commande.

Vous pouvez maintenant essayer d'accéder à l'URL de la sortie dans un navigateur web. 

Alternativement, vous pouvez utiliser cette commande :

```bash
curl $(pulumi stack output hostname)
```

Dans les deux cas, vous devriez voir une réponse du serveur web Python :

```
Hello, World!
```

### Étape 6 : Ajouter plus d'instances EC2

Maintenant, vous allez créer plusieurs instances EC2, chacune exécutant le même serveur web Python, dans toutes les zones de disponibilité AWS de votre région. Remplacez la partie de votre code qui crée le serveur web et exporte l'adresse IP et le nom d'hôte résultants par ce qui suit :

```python
...
ips = []
hostnames = []
for az in aws.get_availability_zones().names:
    server = aws.ec2.Instance(f'web-server-{az}',
      instance_type="t2.micro",
      vpc_security_group_ids=[group.id],
      ami=ami.id,
      availability_zone=az,
      user_data="""#!/bin/bash
echo \"Hello, World -- from {}!\" > index.html
nohup python -m SimpleHTTPServer 80 &
""".format(az),
      tags={
          "Name": "web-server",
      },
    )
    ips.append(server.public_ip)
    hostnames.append(server.public_dns)

pulumi.export("ips", ips)
pulumi.export("hostnames", hostnames)
```

Après cette modification, votre fichier `__main__.py` devrait ressembler à ceci :

```python
"""Un programme AWS Python Pulumi"""

import pulumi
import pulumi_aws as aws


ami = aws.ec2.get_ami(
    most_recent="true",
    owners=["137112412989"],
    filters=[{"name": "name", "values": ["amzn-ami-hvm-*-x86_64-ebs"]}],
)

vpc = aws.ec2.get_vpc(default=True)

group = aws.ec2.SecurityGroup(
    "web-secgrp",
    description="Enable HTTP Access",
    vpc_id=vpc.id,
    ingress=[
        {
            "protocol": "icmp",
            "from_port": 8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
)


ips = []
hostnames = []

for az in aws.get_availability_zones().names:
    server = aws.ec2.Instance(
        f"web-server-{az}",
        instance_type="t2.micro",
        vpc_security_group_ids=[group.id],
        ami=ami.id,
        user_data="""#!/bin/bash
echo \"Hello, World -- from {}!\" > index.html
nohup python -m SimpleHTTPServer 80 &
""".format(
            az
        ),
        tags={
            "Name": "web-server",
        },
    )
    ips.append(server.public_ip)
    hostnames.append(server.public_dns)

pulumi.export("ips", ips)
pulumi.export("hostnames", hostnames)
```

Maintenant, exécutez une commande pour mettre à jour votre pile avec les nouvelles définitions de ressources :

```bash
pulumi up
```

Vous verrez une sortie similaire à ce qui suit :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab2/dev/updates/4

     Type                 Name                   Status
     pulumi:pulumi:Stack  iac-lab2-dev
 +    aws:ec2:Instance  web-server-us-west-2a  created
 +    aws:ec2:Instance  web-server-us-west-2b  created
 +    aws:ec2:Instance  web-server-us-west-2c  created
 +    aws:ec2:Instance  web-server-us-west-2d  created
 -    aws:ec2:Instance  web=server             deleted

Outputs:
  - hostname : "ec2-52-13-25-152.us-west-2.compute.amazonaws.com"
  + hostnames: [
  +     [0]: "ec2-34-222-148-4.us-west-2.compute.amazonaws.com"
  +     [1]: "ec2-54-69-196-240.us-west-2.compute.amazonaws.com"
  +     [2]: "ec2-54-186-64-129.us-west-2.compute.amazonaws.com"
  +     [3]: "ec2-52-25-211-116.us-west-2.compute.amazonaws.com"
    ]
  - ip       : "52.13.25.152"
  + ips      : [
  +     [0]: "34.222.148.4"
  +     [1]: "54.69.196.240"
  +     [2]: "54.186.64.129"
  +     [3]: "52.25.211.116"
    ]

Resources:
    + 4 created
    - 1 deleted
    5 changes. 2 unchanged

Duration: 1m55s
```

Remarquez que votre serveur d'origine a été supprimé et que de nouveaux serveurs ont été créés à sa place, car son nom a changé.

Pour tester les modifications, utilisez curl sur l'une des adresses IP ou des noms d'hôte résultants (ou accédez aux URL dans un navigateur web) :

```bash
for i in {0..2}; do curl $(pulumi stack output hostnames | jq -r ".[${i}]"); done
```

Le nombre de serveurs dépend du nombre de zones de disponibilité dans votre région. Vous devrez peut-être ajuster le `{0..2}`.

La commande `pulumi stack output` émet des données JSON sérialisées — d'où l'utilisation de l'outil `jq` pour extraire un index spécifique. Si vous n'avez pas `jq`, ne vous inquiétez pas ; copiez et collez simplement le nom d'hôte ou l'adresse IP à partir de la sortie de la console et utilisez `curl` dessus.

Notez que le numéro du serveur web est inclus dans sa réponse :

```
Hello, World -- from us-west-2a!
Hello, World -- from us-west-2b!
Hello, World -- from us-west-2c!
```

### Ajouter un équilibreur de charge

Avoir besoin de boucler sur les serveurs web n'est pas très réaliste. Vous allez maintenant créer un équilibreur de charge sur eux pour répartir la charge de manière uniforme.

### Étape 7 : Mettre à jour notre groupe de sécurité

Nous devons ajouter une règle de sortie à notre groupe de sécurité. Chaque fois que vous ajoutez un écouteur à votre équilibreur de charge ou mettez à jour le port de vérification de santé pour un groupe cible utilisé par l'équilibreur de charge pour router les requêtes, vous devez vérifier que les groupes de sécurité associés à l'équilibreur de charge permettent le trafic sur le nouveau port dans les deux directions.

```python
...
group = aws.ec2.SecurityGroup(
    "web-secgrp",
    ingress=[
        { 'protocol': 'icmp', 'from_port': 8, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
    ],
    egress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
    ]
)
...
```

Cela est requis pour s'assurer que les règles d'entrée du groupe de sécurité ne sont pas en conflit avec celles de l'équilibreur de charge.

### Étape 8 : Définir l'ALB

Maintenant, juste après la création du groupe de sécurité, et avant le bloc de création EC2, ajoutez les étapes de création de l'équilibreur de charge :

```python
...
vpc = aws.ec2.get_vpc(default=True)
vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=vpc.id)

lb = aws.lb.LoadBalancer(
    "loadbalancer",
    internal=False,
    security_groups=[group.id],
    subnets=vpc_subnets.ids,
    load_balancer_type="application",
)

target_group = aws.lb.TargetGroup(
    "target-group", port=80, protocol="HTTP", target_type="ip", vpc_id=vpc.id
)

listener = aws.lb.Listener(
    "listener",
    load_balancer_arn=lb.arn,
    port=80,
    default_actions=[{"type": "forward", "target_group_arn": target_group.arn}],
)
...
```

Ici, nous avons défini l'ALB, son TargetGroup et quelques Listeners, mais nous n'avons pas encore ajouté les instances EC2 à l'ALB.

### Étape 9 : Ajouter les instances à l'ALB

Remplacez le bloc de création EC2 par ce qui suit :

```python
...
ips = []
hostnames = []
for az in aws.get_availability_zones().names:
    server = aws.ec2.Instance(f'web-server-{az}',
      instance_type="t2.micro",
      security_groups=[group.name],
      ami=ami.id,
      user_data="""#!/bin/bash
echo \"Hello, World -- from {}!\" > index.html
nohup python -m SimpleHTTPServer 80 &
""".format(az),
      availability_zone=az,
      tags={
          "Name": "web-server",
      },
    )
    ips.append(server.public_ip)
    hostnames.append(server.public_dns)

    attachment = aws.lb.TargetGroupAttachment(f'web-server-{az}',
        target_group_arn=target_group.arn,
        target_id=server.private_ip,
        port=80,
    )

export('ips', ips)
export('hostnames', hostnames)
export("url", lb.dns_name)
```

Après cette modification, votre fichier __main__.py devrait ressembler à ceci :

```python
"""Un programme AWS Python Pulumi"""

import pulumi
import pulumi_aws as aws


ami = aws.ec2.get_ami(
    most_recent="true",
    owners=["137112412989"],
    filters=[{"name": "name", "values": ["amzn-ami-hvm-*-x86_64-ebs"]}],
)

vpc = aws.ec2.get_vpc(default=True)
vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=vpc.id)

group = aws.ec2.SecurityGroup(
    "web-secgrp",
    description="Enable HTTP Access",
    vpc_id=vpc.id,
    ingress=[
        {
            "protocol": "icmp",
            "from_port": 8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
)

lb = aws.lb.LoadBalancer(
    "loadbalancer",
    internal=False,
    security_groups=[group.id],
    subnets=vpc_subnets.ids,
    load_balancer_type="application",
)

target_group = aws.lb.TargetGroup(
    "target-group", port=80, protocol="HTTP", target_type="ip", vpc_id=vpc.id
)

listener = aws.lb.Listener(
    "listener",
    load_balancer_arn=lb.arn,
    port=80,
    default_actions=[{"type": "forward", "target_group_arn": target_group.arn}],
)


ips = []
hostnames = []

for az in aws.get_availability_zones().names:
    server = aws.ec2.Instance(
        f"web-server-{az}",
        instance_type="t2.micro",
        vpc_security_group_ids=[group.id],
        ami=ami.id,
        user_data="""#!/bin/bash
echo \"Hello, World -- from {}!\" > index.html
nohup python -m SimpleHTTPServer 80 &
""".format(
            az
        ),
        tags={
            "Name": "web-server",
        },
    )
    ips.append(server.public_ip)
    hostnames.append(server.public_dns)

    attachment = aws.lb.TargetGroupAttachment(
        f"web-server-{az}",
        target_group_arn=target_group.arn,
        target_id=server.private_ip,
        port=80,
    )


pulumi.export("ips", ips)
pulumi.export("hostnames", hostnames)
pulumi.export("url", lb.dns_name)
```

C'est toute l'infrastructure dont nous avons besoin pour notre serveur web avec équilibrage de charge. Appliquons-la.

### Étape 10 : Déployer vos modifications

Déployez ces mises à jour :

```bash
pulumi up
```

Cela devrait entraîner une mise à jour assez importante et, si tout se passe bien, l'URL de point de terminaison résultante de l'équilibreur de charge :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab2/dev/updates/5

     Type                             Name                   Status      Info
     pulumi:pulumi:Stack              iac-lab2-dev
 +    aws:lb:TargetGroup            target-group           created
 ~    aws:ec2:SecurityGroup         web-secgrp             updated     [diff: ~egress]
 +    aws:lb:LoadBalancer           loadbalancer           created
 +    aws:lb:TargetGroupAttachment  web-server-us-west-2a  created
 +    aws:lb:TargetGroupAttachment  web-server-us-west-2b  created
 +    aws:lb:TargetGroupAttachment  web-server-us-west-2c  created
 +    aws:lb:TargetGroupAttachment  web-server-us-west-2d  created
 +    aws:lb:Listener               listener               created

Outputs:
    hostnames: [
        [0]: "ec2-34-222-148-4.us-west-2.compute.amazonaws.com"
        [1]: "ec2-54-69-196-240.us-west-2.compute.amazonaws.com"
        [2]: "ec2-54-186-64-129.us-west-2.compute.amazonaws.com"
        [3]: "ec2-52-25-211-116.us-west-2.compute.amazonaws.com"
    ]
    ips      : [
        [0]: "34.222.148.4"
        [1]: "54.69.196.240"
        [2]: "54.186.64.129"
        [3]: "52.25.211.116"
    ]
  + url      : "loadbalancer-c9a1e24-965935136.us-west-2.elb.amazonaws.com"

Resources:
    + 7 created
    ~ 1 updated
    8 changes. 5 unchanged

Duration: 3m28s
```

### Étape 11 : Vérifier

Maintenant, nous pouvons faire un curl sur l'équilibreur de charge :

```bash
for i in {0..10}; do curl $(pulumi stack output url); done
```

Observez que le texte résultant change en fonction de l'endroit où la requête est routée :

```
Hello, World -- from us-west-2a!
Hello, World -- from us-west-2a!
Hello, World -- from us-west-2d!
Hello, World -- from us-west-2b!
Hello, World -- from us-west-2b!
Hello, World -- from us-west-2c!
Hello, World -- from us-west-2b!
Hello, World -- from us-west-2a!
Hello, World -- from us-west-2c!
Hello, World -- from us-west-2d!
Hello, World -- from us-west-2a!
```

### Étape 12 : Tout détruire

Enfin, détruisez les ressources et la pile elle-même :

```
pulumi destroy
pulumi stack rm
```

## Laboratoire 3 : Déploiement d'images Docker sur ECS & Fargate

Dans ce laboratoire, vous utiliserez Pulumi pour déployer une image Docker sur ECS avec Fargate.

Commençons depuis le début pour avoir plus de pratique.

### Étape 1 : Créer un répertoire

Créez un nouveau répertoire et changez-le :

```bash
cd ..
mkdir iac-lab3
cd iac-lab3
```

Pulumi utilisera le nom du répertoire comme nom de votre projet par défaut. Pour créer un projet indépendant, il suffit de nommer le répertoire différemment.

### Étape 2 : Initialiser votre projet

Un projet Pulumi est simplement un répertoire avec quelques fichiers dedans. Il est possible pour vous de créer un nouveau projet à la main. La commande `pulumi new`, cependant, automatise le processus :

```bash
pulumi new aws-python -y
```

Cette commande a créé tous les fichiers dont nous avons besoin, initialisé une nouvelle pile nommée `dev` (une instance de notre projet), et installé les dépendances de packages nécessaires depuis PyPi.

### Étape 3 : Inspecter votre nouveau projet

Notre projet est composé de plusieurs fichiers (ce sont les mêmes que précédemment, donc c'est une révision) :

* **`__main__.py`** : le fichier principal d'entrée de votre programme
* **`requirements.txt`** : les informations de dépendance Python de votre projet
* **`Pulumi.yaml`** : les métadonnées de votre projet, contenant son nom et son langage
* **`venv`** : un [virtualenv](https://pypi.org/project/virtualenv/) pour votre projet

Exécutez `cat __main__.py` pour voir le contenu du programme vide de votre projet :

```python
"""Un programme AWS Python Pulumi"""

import pulumi
from pulumi_aws import s3

# Créer une ressource AWS (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Exporter le nom du bucket
pulumi.export('bucket_name', bucket.id)
```

N'hésitez pas à explorer les autres fichiers, bien que nous ne les éditerons pas manuellement.

### Étape 4 : Configurer une région AWS

Configurez la région AWS dans laquelle vous souhaitez déployer :

```bash
pulumi config set aws:region us-west-2
```

### Étape 5 : Créer un cluster ECS

Supprimez tout le code de démarrage du projet.

Importez les packages AWS et Pulumi dans un fichier `__main__.py` vide :

```python
import pulumi
import pulumi_aws as aws
```

Et maintenant, créez un nouveau cluster ECS. Vous utiliserez les valeurs par défaut, donc cela est très concis :

Après cette modification, votre fichier `__main__.py` devrait ressembler à ceci :

```python
import pulumi
import pulumi_aws as aws

cluster = aws.ecs.Cluster("cluster")
```

### Étape 6 : Créer un service de conteneur avec équilibrage de charge

Ensuite, allouez l'équilibreur de charge d'application (ALB) et écoutez le trafic HTTP sur le port 80. Pour ce faire, nous devons trouver le VPC par défaut et les groupes de sous-réseaux pour celui-ci :

```python
...
vpc = aws.ec2.get_vpc(default=True)
vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=vpc.id)

group = aws.ec2.SecurityGroup(
    "web-secgrp",
    vpc_id=vpc.id,
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'icmp', 'from_port': 8, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    egress=[
        { 'protocol': "-1", 'from_port': 0, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0'] }
    ])

alb = aws.lb.LoadBalancer(
    "app-lb",
    internal="false",
    security_groups=[group.id],
    subnets=vpc_subnets.ids,
    load_balancer_type="application",
)

atg = aws.lb.TargetGroup(
    "app-tg",
    port=80,
    deregistration_delay=0,
    protocol="HTTP",
    target_type="ip",
    vpc_id=vpc.id,
)

wl = aws.lb.Listener(
    "web",
    load_balancer_arn=alb.arn,
    port=80,
    default_actions=[{"type": "forward", "target_group_arn": atg.arn}],
)
```

Après cette modification, votre fichier `__main__.py` devrait ressembler à ceci :

```python
import pulumi
import pulumi_aws as aws

cluster = aws.ecs.Cluster("cluster")

vpc = aws.ec2.get_vpc(default=True)
vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=vpc.id)

group = aws.ec2.SecurityGroup(
    "web-secgrp",
    vpc_id=vpc.id,
    description="Enable HTTP access",
    ingress=[
        {
            "protocol": "icmp",
            "from_port": 8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "protocol": "-1",
            "from_port": 0,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
)

alb = aws.lb.LoadBalancer(
    "app-lb",
    internal="false",
    security_groups=[group.id],
    subnets=vpc_subnets.ids,
    load_balancer_type="application",
)

atg = aws.lb.TargetGroup(
    "app-tg",
    port=80,
    deregistration_delay=0,
    protocol="HTTP",
    target_type="ip",
    vpc_id=vpc.id,
)

wl = aws.lb.Listener(
    "web",
    load_balancer_arn=alb.arn,
    port=80,
    default_actions=[{"type": "forward", "target_group_arn": atg.arn}],
)
```

Exécutez votre programme avec `pulumi up` :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab3/dev/updates/1

     Type                      Name          Status
 +   pulumi:pulumi:Stack       iac-lab3-dev  created
 +    aws:ecs:Cluster        cluster       created
 +    aws:ec2:SecurityGroup  web-secgrp    created
 +    aws:lb:TargetGroup     app-tg        created
 +    aws:lb:LoadBalancer    app-lb        created
 +    aws:lb:Listener        web           created

Resources:
    + 6 created

Duration: 3m36s
```

Nous avons développé notre infrastructure et ajouté un LoadBalancer auquel nous pouvons ajouter de l'infrastructure. Dans les prochaines étapes, nous exécuterons un conteneur.

### Étape 7 : Créer un service ECS Fargate

Pour créer un service Fargate, nous devons ajouter un rôle IAM, une définition de tâche et un service. Le cluster ECS exécutera l'image `"nginx"` depuis le Docker Hub.

Tout d'abord, nous devons ajouter un nouvel import en haut de notre fichier

```python
import json
```

Maintenant, définissons notre rôle IAM et attachons une politique. Vous devriez définir ceci à la fin de votre fichier `__main__.py` :

```python
...
role = aws.iam.Role("task-exec-role",
    assume_role_policy=json.dumps({
        "Version": "2008-10-17",
        "Statement": [{
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }]
    }))

rpa = aws.iam.RolePolicyAttachment("task-exec-policy",
    role=role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
)
...
```

Ensuite, nous pouvons définir une définition de tâche pour notre service ECS :

```python
task_definition = aws.ecs.TaskDefinition("app-task",
    family="fargate-task-definition",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    execution_role_arn=role.arn,
    container_definitions=json.dumps([{
        "name": "my-app",
        "image": "nginx",
        "portMappings": [{
            "containerPort": 80,
            "hostPort": 80,
            "protocol": "tcp"
        }]
    }])
)

service = aws.ecs.Service("app-svc",
    cluster=cluster.arn,
    desired_count=1,
    launch_type="FARGATE",
    task_definition=task_definition.arn,
    network_configuration={
        "assign_public_ip": "true",
        "subnets": vpc_subnets.ids,
        "security_groups": [group.id]
    },
    load_balancers=[{
        "target_group_arn": atg.arn,
        "container_name": "my-app",
        "container_port": 80
    }],
    opts=pulumi.ResourceOptions(depends_on=[wl])
)

pulumi.export("url", alb.dns_name)
```

Après ces modifications, votre fichier `__main__.py` devrait ressembler à ceci

```python
import pulumi
import pulumi_aws as aws
import json

cluster = aws.ecs.Cluster("cluster")

vpc = aws.ec2.get_vpc(default=True)
vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=vpc.id)

group = aws.ec2.SecurityGroup(
    "web-secgrp",
    vpc_id=vpc.id,
    description="Enable HTTP access",
    ingress=[
        {
            "protocol": "icmp",
            "from_port": 8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "protocol": "-1",
            "from_port": 0,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
)

alb = aws.lb.LoadBalancer(
    "app-lb",
    internal="false",
    security_groups=[group.id],
    subnets=vpc_subnets.ids,
    load_balancer_type="application",
)

atg = aws.lb.TargetGroup(
    "app-tg",
    port=80,
    deregistration_delay=0,
    protocol="HTTP",
    target_type="ip",
    vpc_id=vpc.id,
)

wl = aws.lb.Listener(
    "web",
    load_balancer_arn=alb.arn,
    port=80,
    default_actions=[{"type": "forward", "target_group_arn": atg.arn}],
)

role = aws.iam.Role("task-exec-role",
    assume_role_policy=json.dumps({
        "Version": "2008-10-17",
        "Statement": [{
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }]
    }))

rpa = aws.iam.RolePolicyAttachment("task-exec-policy",
    role=role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
)

task_definition = aws.ecs.TaskDefinition("app-task",
    family="fargate-task-definition",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    execution_role_arn=role.arn,
    container_definitions=json.dumps([{
        "name": "my-app",
        "image": "nginx",
        "portMappings": [{
            "containerPort": 80,
            "hostPort": 80,
            "protocol": "tcp"
        }]
    }])
)

service = aws.ecs.Service("app-svc",
    cluster=cluster.arn,
    desired_count=1,
    launch_type="FARGATE",
    task_definition=task_definition.arn,
    network_configuration={
        "assign_public_ip": "true",
        "subnets": vpc_subnets.ids,
        "security_groups": [group.id]
    },
    load_balancers=[{
        "target_group_arn": atg.arn,
        "container_name": "my-app",
        "container_port": 80
    }],
    opts=pulumi.ResourceOptions(depends_on=[wl])
)

pulumi.export("url", alb.dns_name)
```

### Étape 8 : Provisionner le cluster et le service

Déployez le programme pour mettre en place votre cluster et service initiaux :

```bash
pulumi up
```

Cela affichera le statut et l'URL de l'équilibreur de charge résultant :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab3/dev/updates/2

     Type                             Name              Status      Info
     pulumi:pulumi:Stack              iac-lab3-dev
 +    aws:iam:Role                  task-exec-role    created
 ~    aws:lb:TargetGroup            app-tg            updated     [diff: ~deregistrationDelay]
 +    aws:iam:RolePolicyAttachment  task-exec-policy  created
 +    aws:ecs:TaskDefinition        app-task          created
 +    aws:ecs:Service               app-svc           created

Outputs:
  + url: "app-lb-e92ae89-2123599743.us-west-2.elb.amazonaws.com"

Resources:
    + 4 created
    ~ 1 updated
    5 changes. 5 unchanged

Duration: 10s
```

Vous pouvez accéder à l'URL de la sortie ci-dessus dans un navigateur web. De plus, vous pouvez maintenant utiliser curl sur le point de terminaison résultant :

```bash
curl $(pulumi stack output url)
```

Et vous verrez la page d'accueil par défaut de Nginx :

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

### Étape 9 : Mettre à jour le service

Maintenant, mettez également à jour le nombre de conteneurs souhaités de `1` à `3` :

```
...
    desiredCount: 3,
...
```

Ensuite, mettez à jour la pile :

```bash
pulumi up
```

La sortie devrait ressembler à ceci :

```
Updating (dev)

View Live: https://app.pulumi.com/beaucarnes/iac-lab3/dev/updates/3

     Type                 Name          Status      Info
     pulumi:pulumi:Stack  iac-lab3-dev
 ~    aws:ecs:Service   app-svc       updated     [diff: ~desiredCount]

Outputs:
    url: "app-lb-e92ae89-2123599743.us-west-2.elb.amazonaws.com"

Resources:
    ~ 1 updated
    9 unchanged

Duration: 6s
```

### Étape 10 : Tout détruire

Enfin, détruisez les ressources et la pile elle-même :

```
pulumi destroy
pulumi stack rm
```