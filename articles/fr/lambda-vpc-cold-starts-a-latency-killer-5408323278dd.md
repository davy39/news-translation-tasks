---
title: Comment gérer les démarrages à froid de Lambda VPC et traiter cette latence
  meurtrière
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T22:27:53.000Z'
originalURL: https://freecodecamp.org/news/lambda-vpc-cold-starts-a-latency-killer-5408323278dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*16yC8qApBwQirGLItTPtjA.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: Comment gérer les démarrages à froid de Lambda VPC et traiter cette latence
  meurtrière
seo_desc: 'By Nathan Malishev

  All serverless computing suffers from the dreaded “cold start”, and AWS Lambda is
  no different. I’ve explored cold starts before in a previous article. But what is
  not common knowledge is how using Lambda in conjunction with a Virt...'
---

Par Nathan Malishev

Tous les calculs serverless souffrent du redouté « démarrage à froid », et [AWS Lambda](http://aws.amazon.com/lambda/) ne fait pas exception. J'ai exploré les [démarrages à froid](https://medium.com/@nathan.malishev/lambda-cold-starts-language-comparison-\ufe0f-a4f4b5f16a62) dans un article précédent. Mais ce qui est moins connu, c'est comment l'utilisation de Lambda en conjonction avec un Virtual Private Cloud affecte la latence. Selon [divers](https://www.reddit.com/r/aws/comments/6lfubn/aws_lambda_vpc_redis_slow/) [rapports](https://forums.aws.amazon.com/thread.jspa?threadID=231069) [sur le web](https://www.reddit.com/r/aws/comments/7gpd53/lambda_rds_incredibly_slow/), les démarrages à froid au sein des VPC pourraient ajouter **jusqu'à 10 secondes de latence !** ⏳

### **Contexte**

**AWS Lambda et le calcul serverless** changent le paradigme du calcul en exécutant le code à la demande. Et oui, cela signifie que vous ne payez que lorsque votre code est en cours d'exécution ! 💰

Le **démarrage à froid** serverless est la première fois que votre code est exécuté par votre fournisseur de cloud, et nécessite qu'il soit téléchargé, conteneurisé, démarré et prêt à être exécuté. Cela peut ajouter un surcoût significatif — **jusqu'à 1,5 s de latence** !

Mais bonne nouvelle : ces démarrages à froid sont censés être des valeurs aberrantes, n'affectant que 5 % des exécutions. Donc, bien qu'ils ne se produisent pas tout le temps, ils sont importants à prendre en compte lors de la conception de votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HsUccdkDffywiUjM7AYdFw.png)
_[Démarrage à froid régulier](https://youtu.be/oQFORsso2go?t=8m5s" rel="noopener" target="_blank" title=") (capture d'écran de la vidéo)_

**Virtual Private Cloud (VPC)** est un réseau privé dans lequel vous contrôlez strictement le trafic réseau entrant et sortant. Ils sont largement utilisés et, traditionnellement, vous exécuteriez vos bases de données et serveurs en toute sécurité derrière votre VPC, en n'exposant qu'un équilibreur de charge. Si vous avez des exigences de sécurité strictes ou des services déjà derrière un VPC auxquels vous devez accéder, vous devrez peut-être déployer vos fonctions Lambda dans un VPC.

La complexité ajoutée d'avoir une fonction Lambda vivre à l'intérieur d'un VPC introduit de nouvelles latences. Ces latences sont dues à la création d'une interface réseau élastique et à l'attente que Lambda s'assigne cette IP. Faites également attention, chaque fonction Lambda nécessite une adresse IP et vous ne voulez pas en manquer !

![Image](https://cdn-media-1.freecodecamp.org/images/1*FCpFITtI7oxassyWOQdrKw.png)
_[Démarrage à froid dans un VPC](https://youtu.be/oQFORsso2go?t=41m49s" rel="noopener" target="_blank" title=") (capture d'écran de la vidéo)_

C'est un surcoût réseau supplémentaire que vous ne pouvez pas éviter, sauf en évitant le VPC dès le départ. Alors, à quel point c'est grave ?

### Installation

Pour tester l'effet du VPC et des démarrages à froid, j'ai créé deux piles [CloudFormation](https://aws.amazon.com/cloudformation/) presque identiques.

**CloudFormation est l'infrastructure en tant que code**, qui est nativement prise en charge par AWS. Vous avez peut-être entendu parler de produits similaires comme Terraform ou Ansible, qui sont d'excellentes alternatives. Le grand avantage de CloudFormation est l'intégration étroite avec AWS et ses [fonctions intrinsèques](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html).

**[AWS Sam](https://github.com/awslabs/serverless-application-model)** est une extension géniale de CloudFormation, qui réduit considérablement la complexité du déploiement d'une fonction Lambda. Il lie plusieurs ressources cloud-formation ensemble, afin que vous n'ayez pas à les gérer séparément pour déployer une fonction Lambda. Il facilite également le processus de déploiement, en compressant et en déployant votre code vers S3 de manière transparente. Il propose également des **[déploiements canari intégrés](https://docs.aws.amazon.com/lambda/latest/dg/automating-updates-to-serverless-apps.html)** ! Mais il existe d'excellentes alternatives comme [serverless](https://serverless.com/), si être agnostique du cloud est votre truc.

Cet article ne parle pas de CloudFormation et Sam, mais si vous souhaitez en voir un, laissez un commentaire :)

![Image](https://cdn-media-1.freecodecamp.org/images/0*teE_0mjhNDaQCTRz.png)
_[AWS Sam](https://github.com/awslabs/serverless-application-model" rel="noopener" target="_blank" title=") est génial !_

Mes deux piles sont toutes deux des piles CloudFormation avec l'extension AWS Sam. Elles comportent toutes deux une fonction simple de lecture et d'écriture, écrite en [Golang](https://golang.org/). Ces fonctions lisent et écrivent dans une seule instance [AWS Aurora RDS](https://aws.amazon.com/rds/aurora/). La différence est qu'une pile est dans un sous-réseau privé et nécessite le surcoût supplémentaire du démarrage à froid.

Les instances VPC et RDS sont gérées uniquement par CloudFormation, tandis que l'API Gateway et les fonctions Lambda sont gérées par l'extension Sam.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LwyfJUjmHsFbdMgGpLj57g.png)
_Le diagramme tente de donner une représentation visuelle des deux piles et de la manière dont leur déploiement est géré._

Ci-dessous se trouve un extrait de la pile #1 :

L'autre pile et le reste du code peuvent être trouvés dans mon dépôt GitHub [ici](https://github.com/nathanmalishev/go-lambda-vpc-experiment).

### Résultats

J'ai exécuté ces piles, avec une règle automatisée [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Scheduled-Rule.html) pour déclencher les fonctions Lambda toutes les heures. J'ai également déployé les piles avec différents degrés de RAM : 128 Mo, 1536 Mo et 3008 Mo. Dans le graphique ci-dessous, toutes les valeurs au-dessus de la marque de 5 secondes proviennent de la pile #2 (à l'intérieur d'un VPC), et toutes les valeurs en dessous proviennent de la pile #1 (en dehors d'un VPC).

![Image](https://cdn-media-1.freecodecamp.org/images/1*16yC8qApBwQirGLItTPtjA.png)
_Fonctions de lecture et d'écriture Lambda des piles #1 et #2. [Jouez avec le graphique ici](https://plot.ly/~nathanmalishev/1/" rel="noopener" target="_blank" title=")_

Il est intéressant de noter que, sur tous les points de données, l'ajout d'un **VPC a augmenté les temps de démarrage à froid en moyenne de 8,83 s**. L'augmentation de la RAM semblait réduire les temps de démarrage à froid ajoutés par le VPC.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GwWZRFPuYZ8qx0cBRFiH2A.png)
_Temps moyen de démarrage à froid sur les piles et configurations de RAM_

Il semble que l'internet avait raison, et que le déploiement de vos fonctions Lambda dans un VPC ajoute d'énormes surcoûts. Un délai de 8 secondes seul est une horrible expérience utilisateur. Si votre application est correctement découplée, rencontrer plusieurs démarrages à froid affecterait négativement l'expérience d'un utilisateur.

### Quand utiliser un VPC ?

Vous devriez vraiment mettre vos fonctions Lambda dans un VPC uniquement lorsque vous avez absolument besoin d'accéder à des ressources qui ne peuvent pas être exposées au monde extérieur. Sinon, vous allez payer pour cela en temps de démarrage **et cela compte**. Comme [Yan Cui](https://www.freecodecamp.org/news/lambda-vpc-cold-starts-a-latency-killer-5408323278dd/undefined) l'a souligné dans son article [« Vous pensez mal aux démarrages à froid »](https://medium.com/p/im-afraid-you-re-thinking-about-aws-lambda-cold-starts-all-wrong-7d907f278a4f?source=user_popover), les démarrages à froid peuvent se produire à tout moment, et surtout pendant les pics d'utilisation du service.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4RwbY1CiZC2jzsD7jBtIlQ.png)
_Arbre de décision pour Lambda et VPC de leur [Livre blanc Serverless](https://d1.awsstatic.com/whitepapers/architecture/AWS-Serverless-Applications-Lens.pdf" rel="noopener" target="_blank" title=")_

### Pièges ⚠️

Si vous devez utiliser un VPC, gardez à l'esprit que chaque fois qu'une fonction Lambda est exécutée, elle utilise une proportion de votre capacité ENI à partir du sous-réseau. Selon la [documentation AWS](https://docs.aws.amazon.com/lambda/latest/dg/vpc.html), ils indiquent que vous devez avoir une capacité ENI suffisante pour supporter vos exigences de mise à l'échelle Lambda. Si vous manquez de capacité ENI, cela entraînera l'échec de vos fonctions Lambda !

Pour calculer vos exécutions Lambda concurrentes maximales dans un sous-réseau donné, nous devons utiliser la formule suivante.

`Capacité ENI = Exécutions concurrentes de pointe projetées * (Mémoire en Go / 3 Go)`

`Capacité ENI` = Nombre d'adresses IP de votre sous-réseau

`Mémoire en Go` = RAM dédiée à votre fonction Lambda

Par exemple, le sous-réseau 10.0.70.0/24 dispose de 251 sous-réseaux disponibles. Si nous avons une fonction Lambda assignée avec 1,5 Go de RAM :

251 = Exécutions concurrentes de pointe projetées * (1,5/3)

Exécutions concurrentes de pointe (Lambda) projetées = 502

Comme vos exécutions Lambda concurrentes dépendent directement des adresses IP disponibles dans les sous-réseaux, il est préférable d'utiliser un sous-réseau qui vous donne plus de 1000 adresses IP.

Si vous n'êtes pas sûr, vous pouvez faire le calcul et vous assurer que votre allocation de RAM pour toutes vos fonctions Lambda dans un sous-réseau donné est appropriée pour vos IP disponibles.

**Merci d'avoir lu !** Si vous avez aimé, n'oubliez pas de cliquer sur le bouton d'applaudissements.

### Références

Les premières diapositives affichant les variantes de démarrage à froid proviennent de la conférence AWS Reinvent 2017 intitulée « Devenir une ceinture noire [Serverless](https://serverless.com) ».

#### Liens utiles

[Le modèle d'application serverless AWS](https://github.com/awslabs/serverless-application-model) sur GitHub.

[Mon expérience Lambda VPC](https://github.com/nathanmalishev/go-lambda-vpc-experiment) sur GitHub.