---
title: Comment construire un cluster EKS à travers les AWS Local Zones en utilisant
  l'AWS CDK
subtitle: ''
author: Gursimar Singh
co_authors: []
series: null
date: '2024-05-28T14:34:30.000Z'
originalURL: https://freecodecamp.org/news/build-an-eks-cluster-using-aws-local-zones-with-aws-cdk
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/pexels-pixabay-357742.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
seo_title: Comment construire un cluster EKS à travers les AWS Local Zones en utilisant
  l'AWS CDK
seo_desc: "AWS Local Zones are a new type of infrastructure that enables you to build\
  \ and run applications closer to end-users, providing low latency and improved performance.\
  \ \nThey are designed to provide the same high availability and reliability as an\
  \ AWS Re..."
---

Les AWS Local Zones sont un nouveau type d'infrastructure qui permet de construire et d'exécuter des applications plus près des utilisateurs finaux, offrant une faible latence et des performances améliorées. 

Elles sont conçues pour fournir la même haute disponibilité et fiabilité qu'une région AWS, mais avec l'avantage supplémentaire de connexions à faible latence pour les applications qui en ont besoin.

L'utilisation des Local Zones peut être particulièrement utile si vous avez des utilisateurs finaux situés dans des zones géographiques spécifiques et que vous souhaitez leur fournir un accès à faible latence à leurs applications. Cela peut être particulièrement important pour les applications qui nécessitent un traitement de données en temps réel ou qui ont des exigences de performance strictes.

Les Local Zones peuvent également minimiser les dépenses réseau, ce qui est un avantage supplémentaire. En exécutant des applications dans une Local Zone plus proche des utilisateurs finaux, vous pouvez limiter la quantité de données qui doivent être transférées sur de longues distances, ce qui réduit les coûts réseau.

Dans ce tutoriel, nous verrons comment construire un cluster EKS hybride de périphérie qui s'étend à travers les régions AWS et les AWS Local Zones en utilisant à la fois la console de gestion AWS et l'AWS Cloud Development Kit (CDK).

Avant de commencer, il est important de noter que les AWS Local Zones sont des emplacements physiquement séparés qui sont connectés à la région AWS principale par des liaisons haut débit. Elles vous permettent d'exécuter certains services plus près de vos clients et de réduire la latence.

Pour construire votre cluster EKS à travers les Local Zones, vous devrez :

1. Créer un cluster EKS dans la région principale
2. Créer un VPC et des ressources associées dans les Local Zones
3. Connecter les VPC des Local Zones au VPC de la région principale
4. Lancer des nœuds de travail dans les VPC des Local Zones

Nous allons passer en revue ces étapes dans ce guide.

![Image](https://lh3.googleusercontent.com/-kdtf6vkPfxVY3aLcGpqQI5wczBZXfcScdCz2z1bhNSuawjGEJyLEznPfB5mqnupfuVsPCNybRHJViCjLTxKmF5F2zq82LdHvRmnItjDFTrPDtTRhAzAgr7ToL8bhuymqSkCpVei2VcPyFdjz7YQC_w)
_Diagramme d'architecture_

### Prérequis

Avant de commencer, vous devez avoir les éléments suivants :

1. Un compte AWS avec les permissions pour créer des ressources dans AWS Wavelength et AWS Local Zones.
2. AWS CDK installé sur votre machine locale. Si vous ne l'avez pas installé, vous pouvez suivre les instructions dans la documentation AWS CDK pour l'installer.
3. AWS CLI installé sur votre machine locale. Si vous ne l'avez pas installé, vous pouvez suivre les instructions dans la documentation AWS CLI pour l'installer.

Enfin, commençons.

## Étape 1 : Créer une AWS Local Zone

La première étape consiste à opter pour les AWS Local Zones dans la région de votre choix. Vous pouvez suivre les instructions dans la [documentation des AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html) pour opter pour ces zones.

## Étape 2 : Créer un projet CDK

Pour commencer, nous devons créer un nouveau projet CDK en utilisant la commande suivante :

```
cdk init --language=javascript
```

Cela créera un nouveau répertoire avec les fichiers et répertoires requis pour un projet CDK.

Ensuite, installez les dépendances requises en utilisant la commande suivante :

```
npm install
```

Maintenant, créons un nouveau fichier appelé local-zone-eks.js dans le répertoire lib et ajoutons le code suivant :

```
const cdk = require('aws-cdk-lib');
const ec2 = require('aws-cdk-lib/aws-ec2');
import * as autoscaling from '@aws-cdk/aws-autoscaling';
import * as ecs from '@aws-cdk/aws-eks';

require('dotenv').config();
const config = {
  env: {
	account: process.env.AWS_ACCOUNT_NUMBER,
	region: process.env.AWS_REGION,
  },
};


class VPCStack extends cdk.Stack {
  constructor(scope, id, props) {
	super(scope, id, props);

	// Créer un VPC 
	const vpc = new ec2.Vpc(this, 'VPC', {
  	cidr: '10.0.0.0/16',
  	maxAzs: 2,
  	subnetConfiguration: [
    	{
      	cidrMask: 24,
      	name: 'Public',
      	subnetType: ec2.SubnetType.PRIVATE,
    	},
    	{
      	cidrMask: 24,
      	name: 'Private',
      	subnetType: ec2.SubnetType.PRIVATE,
    	},
  	],
	});
  }
}

module.exports = { VPCStack };

```

Ce code crée un nouveau VPC avec un bloc CIDR de 10.0.0.0/16, qui s'étend sur deux sous-réseaux privés. 

Ensuite, exportons la variable d'environnement pour notre AWS Local Zone, que nous utiliserons pour créer le seul sous-réseau public dans notre VPC. Dans cet exemple, nous avons sélectionné la Local Zone de Las Vegas et avons configuré le sous-réseau en conséquence.

```
const localZone: string = 'us-west-2-las-1a'

 // Créer un sous-réseau public de Local Zone
	const LocalZoneSubnet = new ec2.PublicSubnet(this, 'localzone-public-subnet', {
  	availabilityZone: localZone,
  	cidrBlock: '10.0.3.0/26',
  	vpcId: vpc.vpcId,
  	mapPublicIpOnLaunch: true,
	});

	// Ajouter le sous-réseau de Local Zone au VPC
	vpc.publicSubnets.push(LocalZoneSubnet);

```

## Étape 3 : Créer un cluster Amazon EKS

Maintenant que nous avons un VPC, nous pouvons créer un cluster Amazon Elastic Container Service pour Kubernetes (Amazon EKS).

Ajoutez le code suivant au fichier local-zone-eks.js :

```
const eks = require('aws-cdk-lib/aws-eks');

class EKSStack extends cdk.Stack {
  constructor(scope, id, props) {
	super(scope, id, props);
	// Créer le cluster EKS
	const cluster = new eks.Cluster(this, 'EKSCluster', {
  	vpc: vpc,
  	defaultCapacity: 0,
  	version: '1.21',
  	clusterName: 'local-zone-eks-demo-cluster',
	});
  }
}
module.exports = { EKSStack };

```

  
Ce code crée un nouveau cluster EKS en utilisant le VPC que nous avons créé précédemment. Il spécifie également la version de Kubernetes à utiliser et le nom du cluster.

## Étape 4 : Créer des nœuds de travail

Ensuite, nous devons créer des nœuds de travail pour exécuter nos applications sur le cluster EKS.

Ajoutez le code suivant au fichier local-zone-eks.js :

```
// Définir l'image optimisée pour EKS pour le modèle de lancement
	const image = new ecs.EksOptimizedAmi();

	// Créer un modèle de lancement pour le groupe de mise à l'échelle automatique à référencer
	const lzLaunchTemplate = new ec2.CfnLaunchTemplate(
  	this,
  	'eks-launch-template',
  	{
    	launchTemplateName: 'lz-launch-template',
    	launchTemplateData: {
      	networkInterfaces: [
        	{
          	deviceIndex: 0,
          	associatePublicIpAddress: true,
          	deleteOnTermination: true,
          	subnetId: LocalZoneSubnet.subnetId!,
        	},
      	],
      	imageId: image.getImage(this).imageId,
      	instanceType: 't3.medium',
      	userData: cdk.Fn.base64(
        	`#!/bin/bash -xe
	      set -o xtrace
	      /etc/eks/bootstrap.sh 'local-zone-eks-demo-cluster'}
        	)
    	},
  	}
	);

 // Créer un groupe de mise à l'échelle automatique
	const lz_asg = new autoscaling.AutoScalingGroup(this, 'LocalZoneWorkerNodes', {
  	instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
  	machineImage: new ecs.EksOptimizedAmi(),
  	updateType: autoscaling.UpdateType.REPLACING_UPDATE,
  	desiredCapacity: 1,
  	vpc: vpc,
	launchTemplate: lzLaunchTemplate
	});

```

Ce code crée un nouveau groupe de mise à l'échelle automatique pour gérer les nœuds de travail, et ajoute les nœuds de travail au cluster EKS en utilisant le script de bootstrap d'instance.

## Étape 5 : Déployer l'application CDK

Maintenant que nous avons tout le code requis, nous pouvons le déployer en utilisant la commande suivante :

```
cdk deploy
```

Avec votre cluster EKS opérationnel, vous pouvez commencer à déployer vos applications. Vous pouvez utiliser des manifestes Kubernetes ou des charts Helm pour déployer vos applications sur le cluster.

## Conclusion

Les AWS Local Zones fournissent un mécanisme robuste pour fournir des applications haute performance aux utilisateurs finaux, indépendamment de leur localisation. Elles offrent également aux utilisateurs finaux une meilleure expérience et des performances élevées.

Je suis toujours ouvert aux suggestions et discussions sur [LinkedIn](https://www.linkedin.com/in/gursimarsm). Envoyez-moi des messages directs.

Si vous avez apprécié mes écrits et souhaitez me motiver, envisagez de laisser des étoiles sur [GitHub](https://github.com/gursimarsm) et de m'endosser pour des compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/gursimarsm).

Jusqu'à la prochaine, restez en sécurité et continuez à apprendre.