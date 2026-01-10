---
title: Comment utiliser Ansible pour gérer vos ressources AWS
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-10-28T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/ansible-manage-aws
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/jean_victor_balin_icon_monitoring-1.png
tags:
- name: ansible
  slug: ansible
- name: AWS
  slug: aws
- name: Orchestration
  slug: orchestration
seo_title: Comment utiliser Ansible pour gérer vos ressources AWS
seo_desc: "Wouldn't you love to be able to simply wave a wand and layers of resources\
  \ in your AWS account would suddenly - and magically - spring to perfectly configured\
  \ life, ready to meet your complex infrastructure needs? \nIf you already have experience\
  \ with..."
---

N'aimeriez-vous pas pouvoir simplement agiter une baguette magique et voir les couches de ressources de votre compte AWS soudainement - et magiquement - prendre vie, parfaitement configurées, prêtes à répondre à vos besoins complexes en infrastructure ?

Si vous avez déjà de l'expérience avec AWS, vous savez à quel point il peut être fastidieux de travailler page après page dans la console de gestion Amazon pour provisionner manuellement les services. Et même l'AWS CLI - qui représente un énorme progrès - peut ajouter sa propre complexité et ses propres efforts au mélange.

Cela ne signifie pas qu'AWS lui-même ne traite pas le problème avec sa propre classe d'outils d'orchestration puissants, incluant CloudFormation et leur service Elastic Kubernetes (un sujet que j'aborde en détail dans [mon cours "Using Docker on AWS" chez Pluralsight](https://pluralsight.pxf.io/nZgKx)). Mais aucune de ces options ne se rapproche autant de votre infrastructure existante - ou n'utilise une méthode d'opération aussi familière - qu'Ansible.

Si vous utilisez déjà Ansible pour vos opérations sur site, le connecter à votre compte AWS peut parfois être le moyen le plus rapide et le moins douloureux de migrer vos opérations vers le cloud.

### Comprendre l'avantage Ansible/AWS

Mon livre "[Manage AWS Resources Using Ansible](https://www.amazon.com/gp/product/B07YK42ZH1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07YK42ZH1&linkCode=as2&tag=projemun-20&linkId=d90b5a553223444f00992afa4c8f8d16)" - dont cet article est extrait - est conçu pour vous introduire rapidement à l'application de l'approche _déclarative_ d'Ansible pour travailler avec les ressources AWS. Pouvoir "déclarer" les résultats de configuration précis que vous souhaitez et les produire en faisant lire un playbook par Ansible est la baguette magique d'Ansible. Lorsqu'il est correctement planifié, il est incroyable de voir à quel point il peut être simple d'exécuter des déploiements AWS complexes et en couches.

Avant de lancer un simple playbook "Hello World" Ansible, assurons-nous d'abord que vous avez un environnement de travail correctement configuré à travers lequel Ansible peut communiquer avec tous ses nouveaux amis dans votre compte AWS.

### Préparer un environnement local

Comme vous le savez probablement déjà, Ansible est un outil d'orchestration qui vous permet d'écrire des fichiers _playbook_ en texte brut qui _déclarent_ le profil logiciel et l'état idéal que vous souhaitez appliquer à un serveur cible. Ces serveurs - connus sous le nom d'hôtes - peuvent être provisionnés pour presque n'importe quelle charge de travail numérique que vous pouvez imaginer, en utilisant presque n'importe quelle combinaison de logiciels d'application, et fonctionnant sur presque n'importe quelle plateforme.

Dans le bon vieux temps, lorsqu'un playbook était exécuté contre un serveur physique, Ansible utilisait une connexion SSH existante pour se connecter de manière sécurisée à l'hôte distant et commencer à construire votre application. Mais cela ne fonctionnera pas pour les charges de travail AWS. Vous voyez, parce que les instances EC2 et autres infrastructures que vous souhaitez lancer n'existent pas encore, il ne peut y avoir de connexions SSH "existantes". Au lieu de cela, Ansible utilisera Boto 3 - le kit de développement logiciel (ou SDK) utilisé par AWS qui permet au code Python de communiquer avec l'API AWS.

### Utiliser l'AWS CLI pour connecter Ansible

Vous n'avez pas besoin de savoir comment tout cela fonctionne, mais cela doit être là pour que cela _puisse_ fonctionner. Pour cette raison, vous allez installer l'interface de ligne de commande (CLI) AWS. Nous n'utiliserons pas le CLI lui-même pour quoi que ce soit d'important, mais son installation nous donnera toutes les dépendances dont nous aurons besoin. Vous pouvez découvrir comment faire fonctionner cela sur la dernière version de n'importe quel système d'exploitation que vous utilisez à partir de la [page de documentation AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

Travailler avec le gestionnaire de paquets Python, PIP, est un moyen populaire de tout faire. Voici comment vous installeriez PIP lui-même puis l'AWS CLI sur une machine Ubuntu :

```
sudo apt update
sudo apt install python3-pip
pip3 install awscli
```

Je devrais noter que, au moment où j'écris ces lignes, Python 2 est encore vivant... mais seulement juste. Il peut donc parfois y avoir des versions séparées de Python 2 et Python 3 installées sur votre système. Comme Python 2 sera bientôt complètement obsolète, vous n'aurez probablement pas à vous soucier de spécifier python3 ou pip3 avec vos commandes : cela devrait être automatique.

Une fois le CLI installé, exécutez `aws configure` et entrez votre ID de clé d'accès AWS et votre clé d'accès secrète.

```
aws configure
cat .aws/credentials
```

Vous pouvez obtenir des clés à partir de la page Vos informations d'identification de sécurité dans la console de gestion AWS. Voici à quoi ces clés ressembleront (ne vous donnez pas de mauvaises idées, celles-ci ne sont pas valides) :

```
AccessKeyId: AKIALNZTQW6H3EFBRLHQ
SecretAccessKey: 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
```

Rappelez-vous simplement qu'une paire de clés émise à l'utilisateur root de votre compte AWS fournit un accès complet à l'ensemble de votre compte AWS. Toute personne en possession de ces identifiants pourrait rapidement accumuler des frais de services à six, voire sept chiffres, alors soyez _très_ prudent quant à la manière dont vous les utilisez et les stockez. Idéalement, vous seriez mieux protégé en limitant votre exposition au risque en créant un utilisateur administrateur dans le service AWS Identify and Access Management (IAM) avec des pouvoirs limités et en utilisant une clé émise à cet utilisateur.

Dans tous les cas, pourquoi fais-je cela ? La valeur de remplir mon fichier d'identifiants AWS est qu'Ansible est suffisamment intelligent pour le rechercher et, si aucune autre clé d'authentification n'est disponible dans l'environnement système, il utilisera celles-ci. Vous verrez bientôt à quel point cela sera pratique. Cependant, vous devez être conscient d'autres moyens de gérer l'authentification pour les playbooks Ansible, comme l'utilisation de _ansible-vault_ ou en créant puis en invoquant un fichier aws_keys.yml. Mais une chose que vous ne devriez définitivement PAS faire est de coder en dur les clés dans vos fichiers de playbook - surtout si vous prévoyez de les pousser vers un dépôt en ligne comme GitHub. Je vais rapidement tester le CLI pour m'assurer que nous pouvons nous connecter correctement à AWS. Cette commande simple listera tous les buckets S3 que je peux avoir dans ce compte.

```
aws s3 ls
```

Nous sommes maintenant prêts à installer ansible. Je vais utiliser pip3 pour cela. Je pourrais utiliser le dépôt apt régulier d'Ubuntu tout aussi facilement, mais il installera probablement une version légèrement plus ancienne. Selon votre connexion réseau, cela prendra une minute ou deux, mais je vais sauter la plupart de cela.

```
$ pip3 install ansible

```

Je vais confirmer qu'il est correctement installé en exécutant ansible --version. Cela nous montre la version qui a été construite, que les modules Ansible configurés seront, par défaut, enregistrés dans l'un de ces deux emplacements dans le système de fichiers, que d'autres modules seraient disponibles ici et - surtout - que l'exécutable Ansible est situé dans le répertoire /local/bin/ sous le répertoire personnel de mon utilisateur. Mon utilisateur ici, d'ailleurs, s'appelle ubuntu. Vous pouvez également voir que nous utilisons une version récente et à jour de Python 3.

```
$ ansible --version
ansible 2.8.5
  config file = None
  configured module search path = 
    ['/home/ubuntu/.ansible/plugins/modules', 
    '/usr/share/ansible/plugins/modules']
  ansible python module location = 
    /home/ubuntu/.local/lib/python3.6/site-packages/ansible
  executable location = /home/ubuntu/.local/bin/ansible
  python version = 3.6.8 (default, Aug 20 2019, 17:12:48) [GCC 8.3.0]

```

Une étape de plus. Comme je l'ai mentionné précédemment, Ansible se connectera à AWS en utilisant le SDK boto. Nous devons donc installer les packages boto et boto 3. Je vais utiliser PIP pour celui-ci également.

```
$ pip3 install boto boto3

```

Une fois que celui-ci aura été intégré, nous serons prêts à accomplir des tâches réelles. Cela commencera dans la section suivante.

## Tester Ansible avec un Playbook Simple

Ce sera une démonstration de preuve de concept très simple. Je vais créer quelques fichiers, vous expliquer la syntaxe, puis le lancer. Tout d'abord, j'utiliserai n'importe quel éditeur de texte pour créer un fichier _hosts_. Normalement, le fichier hosts indique à Ansible où trouver les serveurs distants que vous souhaitez provisionner. Mais puisque, dans le cas d'AWS, les ressources qui seront nos hôtes n'existent pas encore, nous allons simplement pointer Ansible vers localhost et boto gérera les connexions en arrière-plan. Voici à quoi ressemblera le contenu de ce fichier :

```
[local]
localhost

```

Ensuite, je vais créer un fichier playbook que j'appellerai test-ansible.yml. L'extension yml indique, bien sûr, que ce fichier doit être formaté en utilisant la syntaxe du langage de balisage YAML. Comme vous pouvez le voir à partir du texte du fichier que j'ai collé juste en dessous, cela commencera par trois tirets marquant le début du fichier et ensuite un tiret en retrait introduisant un ensemble de définitions. La valeur de "hosts" pourrait être un ou plusieurs ordinateurs distants mais, comme je l'ai dit, nous laisserons cela au système local pour le déterminer. Il en va de même pour notre connexion.

La section suivante inclut les _tâches_ que nous voulons qu'Ansible exécute. Celle-ci utilisera le module aws_s3 pour _créer_ un nouveau bucket sur le service de stockage simple S3 d'Amazon dans la région us-east-1. Je dois lui donner ce nom peu attrayant car les buckets S3 nécessitent des noms uniques à l'échelle mondiale - si un nom que vous choisissez entre en conflit avec l'un des innombrables millions de noms déjà existants, l'opération échouera.

```yaml
---
  - name: Test s3
    hosts: local
    connection: local

    tasks:
      - name: Create new bucket
        aws_s3:
          bucket: testme817275b
          mode: create
          region: us-east-1

```

J'exécute le playbook en appelant la commande ansible-playbook en utilisant -i pour spécifier le fichier hosts, puis en pointant vers le fichier test.yml. Ansible devrait nous donner un retour dans un instant ou deux. Si nous réussissons, vous verrez "0" comme valeur de "failed" et au moins "1" comme valeur de "ok".

```
$ ansible-playbook -i hosts test-ansible.yml
PLAY [Test s3] ******************************************************

TASK [Create new bucket] ********************************************

changed: [localhost]

PLAY RECAP **********************************************************
localhost: ok=1    changed=1    unreachable=0    failed=0   skipped=0
    rescued=0    ignored=0 

```

Si je vérifie une fois de plus ma liste de buckets, je devrais - et je vois - le nouveau :

```
$ aws s3 ls
2018-12-30 15:19:24 elasticbeanstalk-us-east-1-297972716276
2018-10-12 04:09:37 mysite548.com
2019-09-24 15:53:26 testme817275b

```

C'est une très brève introduction à la configuration d'un environnement Ansible. Nous avons vu comment l'utilisation d'Ansible avec les ressources provisionnées automatiquement d'Amazon fonctionnera différemment de ce qu'elle serait avec des hôtes Ansible traditionnels. Vous aurez besoin d'un ensemble différent d'outils d'authentification et de contrôle d'inventaire. Nous avons parcouru le processus de configuration d'un environnement Ansible et de sa connexion à AWS, puis l'exécution d'un playbook simple. Court et doux.

Cet article est extrait de mon livre "[Manage AWS Resources Using Ansible](https://www.amazon.com/gp/product/B07YK42ZH1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07YK42ZH1&linkCode=as2&tag=projemun-20&linkId=d90b5a553223444f00992afa4c8f8d16)". Il y a plus de bonnes choses technologiques - sous forme de livres, de cours et d'articles - disponibles sur mon [site web, bootstrap-it.com](https://bootstrap-it.com).