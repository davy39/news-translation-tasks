---
title: 'Certification AWS Security Specialty : Comment se préparer à l''examen'
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2024-10-15T15:44:32.079Z'
originalURL: https://freecodecamp.org/news/aws-security-specialty-certification-study-tips
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729003266992/5be45b39-6a46-42a0-89f8-82dde56f0207.jpeg
tags:
- name: AWS
  slug: aws
- name: Certification
  slug: certification
- name: Security
  slug: security
seo_title: 'Certification AWS Security Specialty : Comment se préparer à l''examen'
seo_desc: Welcome to my latest tutorial! After a three-year hiatus from certifications,
  I'm thrilled to announce that I've successfully obtained the AWS Certified Security
  Specialty certification. As someone who strongly believes in the power of community
  lear...
---

Bienvenue dans mon dernier tutoriel ! Après une pause de trois ans dans les certifications, je suis ravi de vous annoncer que j'ai obtenu avec succès la certification AWS Certified Security Specialty. En tant que personne qui croit fermement au pouvoir de l'apprentissage communautaire, je suis enthousiaste à l'idée de partager mon parcours et mes réflexions avec vous.

Dans ce guide, je vais vous faire part de mon expérience de préparation et de réussite à l'examen AWS Certified Security Specialty. Plutôt qu'un guide d'étude complet, je vais vous présenter cela comme une collection de notes d'étude et d'observations personnelles. Mon objectif est de vous fournir des conseils et des stratégies pratiques qui m'ont aidé à réussir.

Pour ceux qui recherchent une approche plus structurée, je recommande vivement le guide d'étude officiel de la certification AWS et les excellentes ressources fournies par TutorialsDojo. Ces ressources ont été inestimables dans ma préparation et pourraient être de grandes ressources pour votre propre parcours.

Alors, que vous envisagiez cette certification ou que vous soyez simplement curieux de la sécurité AWS, j'espère que vous trouverez de la valeur dans les expériences et les réflexions que je m'apprête à partager.

## Devriez-vous vous certifier ?

Il existe des opinions mitigées dans l'industrie technologique sur l'importance des certifications. Certaines personnes soutiennent que les certificats que vous possédez n'ont pas d'importance – tout est une question de connaissances pratiques.

Mais tout le monde n'a pas la chance de travailler sur des projets concrets. Et les questions de certification sont basées sur des scénarios réels. Donc, si vous n'avez pas eu l'occasion de travailler beaucoup avec la sécurité AWS en pratique, vous pouvez apprendre de cet examen et appliquer vos apprentissages sur des projets réels.

D'un autre côté, si vous travaillez déjà avec AWS, passer l'examen est une excellente occasion de tester vos connaissances et d'en apprendre davantage sur son fonctionnement interne.

Par exemple, vous avez peut-être travaillé avec AWS depuis un certain temps, mais vous n'avez pas touché à la sécurité AWS, ou vous n'avez pas suivi les meilleures pratiques. La certification couvre tous les aspects de la sécurité AWS, vous apprendrez donc comment vous pouvez réduire vos coûts et suivre les meilleures pratiques.

## Structure de l'examen

* **Durée de l'examen** : 170 minutes

* **Format de l'examen** : 65 questions. Choix multiples, réponses multiples

* **Score de réussite** : L'examen utilise un système de notation mis à l'échelle de 100 à 1 000. Pour réussir, vous devez obtenir un score minimum de 750.

* **Coût** : 300 USD. Taxes supplémentaires possibles de 30 USD.

* **Méthode de livraison** : Centre de test Pearson VUE ou examen en ligne surveillé

Il m'a fallu environ 110 minutes pour terminer les questions, et j'en ai marqué 25 pour révision. J'ai ensuite passé 60 minutes supplémentaires à réviser ces 25 questions.

Dans mon cas, la connexion Internet a été coupée et mon examen a gelé. Ne paniquez pas ! Relancez simplement le logiciel VUE, vous êtes autorisé à reprendre l'examen. Aucune collation ou pause toilette n'est autorisée, mais vous pouvez avoir de l'eau.

## Mon approche d'étude

J'ai utilisé une méthode structurée pour me préparer à l'examen AWS Certified Security Specialty :

* J'ai suivi un cours complet sur la sécurité AWS sur Udemy

* J'ai pratiqué avec plusieurs séries de questions d'examen :

    * J'ai analysé attentivement les réponses incorrectes

    * J'ai consulté la documentation AWS et les vidéos YouTube AWS pour une compréhension plus approfondie

* J'ai utilisé des ressources de pratique supplémentaires :

    * Examens pratiques de TutorialsDojo

    * Tests simulés de WhizLabs

Cette approche m'a aidé à acquérir à la fois des connaissances théoriques et des compétences pratiques de résolution de problèmes essentielles pour l'examen.

## Sujets et concepts clés

### Rapport d'identifiants AWS IAM

Il est crucial de comprendre comment examiner le rapport d'identifiants AWS IAM. Voici quelques points clés :

1. Application de l'authentification multifacteur (MFA) : Identifiez les utilisateurs qui n'ont pas activé la MFA et imposez son utilisation.

2. Surveillance du compte racine : Surveillez l'utilisation du compte racine pour vous assurer qu'il n'est pas utilisé pour les opérations quotidiennes.

3. Suivez les dates de création des utilisateurs et de leur dernière activité pour gérer efficacement les cycles de vie des utilisateurs.

4. Surveillance de l'utilisation des clés d'accès : Identifiez les clés d'accès inutilisées qui pourraient poser un risque de sécurité.

5. Trouvez les utilisateurs avec des mots de passe ou des clés d'accès anciens qui pourraient être compromis.

6. Comprenez le format du rapport : [Documentation AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html#id_credentials_understanding_the_report_format)

### Verrouillage des objets AWS S3

Le verrouillage des objets AWS S3 est une fonctionnalité qui aide à empêcher la suppression ou l'écrasement des objets pendant une durée fixe ou indéfiniment. Il est particulièrement utile pour les scénarios nécessitant l'immuabilité des données, tels que la conformité réglementaire ou la protection contre la suppression accidentelle ou malveillante.

* Mode de conformité : Empêche toute personne, y compris l'utilisateur racine, de remplacer ou de supprimer une version d'objet.

* Mode de gouvernance : Permet aux utilisateurs disposant d'autorisations spéciales de remplacer ou de supprimer des versions d'objets protégées.

### Intégration d'Active Directory sur site avec IAM

Il est important de connaître les étapes impliquées dans l'intégration d'Active Directory sur site avec IAM pour l'authentification unique. Pour plus de détails, consultez cet [article du blog AWS](https://aws.amazon.com/blogs/security/how-to-connect-your-on-premises-active-directory-to-aws-using-ad-connector/).

### Politiques de contrôle de service AWS (SCP)

Étudiez les exemples de SCP AWS. Les politiques de contrôle de service (SCP) sont des politiques au niveau de l'organisation qui gèrent les autorisations dans votre organisation AWS. Elles fournissent un contrôle centralisé sur les autorisations maximales disponibles pour les utilisateurs et rôles IAM dans les comptes de votre organisation.

Pour des exemples de SCP, consultez la [documentation AWS](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html).

### Servir du contenu privé via CloudFront

Apprenez à servir du contenu privé via CloudFront. Le [guide du développeur AWS CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) fournit des informations détaillées sur ce sujet.

* L'utilisation d'URL signées est bénéfique lorsque vous souhaitez restreindre l'accès à des fichiers individuels, par exemple, un téléchargement d'installation pour votre application.

* L'utilisation de cookies signés est bénéfique lorsque vous souhaitez fournir un accès à plusieurs fichiers restreints, et que vous ne souhaitez pas modifier vos URL actuelles.

### Comprendre les ports éphémères

Comprenez pourquoi il est important de définir la plage des ports éphémères dans les règles sortantes. Les ports éphémères sont des ports temporaires utilisés dans les communications réseau et Internet, gérés par le système d'exploitation de la machine.

Consultez cet [article Medium](https://remy-nts.medium.com/aws-nacl-why-the-need-to-set-ephemeral-ports-range-for-outbound-rules-50ee93986555) sur les NACL et les ports éphémères.

### Sécuriser l'accès aux sites web via CloudFront

Pour vous assurer que les utilisateurs ne peuvent accéder à votre site web que via l'URL CloudFront tout en restreignant complètement l'accès via l'URL de l'Application Load Balancer (ALB), vous devez savoir comment faire ce qui suit :

1. Configurer le groupe de sécurité ALB : Restreignez l'accès à votre ALB en permettant uniquement le trafic provenant des plages d'IP de CloudFront.

2. Implémenter des en-têtes personnalisés : Définissez un en-tête personnalisé dans CloudFront et configurez votre ALB pour n'accepter que les requêtes avec cet en-tête.

### AWS KMS et chiffrement par enveloppe

AWS KMS peut directement chiffrer des données jusqu'à 4 Ko. Pour les fichiers de plus de 4 Ko, vous devez utiliser le chiffrement par enveloppe. Voici les étapes :

* Générez une clé de données en utilisant AWS KMS

* Utilisez la clé de données pour chiffrer vos grandes données

* Chiffrez la clé de données avec KMS

* Stockez la clé de données chiffrée avec vos données chiffrées

![AWS KMS et chiffrement par enveloppe](https://cdn.hashnode.com/res/hashnode/image/upload/v1728487271329/bdd34ea3-5e47-474a-a083-6e031e508949.png align="left")

### Conditions de politique KMS

Apprenez comment fonctionnent les conditions dans la politique AWS KMS. Consultez le [guide du développeur AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-key-origin) pour des informations détaillées.

### Conditions de politique IAM

* Familiarisez-vous avec les conditions importantes des politiques IAM. Le [guide de l'utilisateur AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String) offre des informations détaillées.

* Je vous suggère vivement de regarder ces deux vidéos pour comprendre les conditions des politiques IAM avec des exemples :

    * [Vidéo 1](https://www.youtube.com/watch?v=qsF6Kauh2J4)

    * [Vidéo 2](https://www.youtube.com/watch?v=4PJienr4gZI)

### Fonction Lambda assumant un rôle IAM dans un autre compte AWS

Comprenez comment configurer une fonction Lambda pour assumer un rôle IAM dans un autre compte AWS. Consultez cet [article du centre de connaissances AWS](https://repost.aws/knowledge-center/lambda-function-assume-iam-role) pour plus de détails.

### Rotation des clés KMS

Comprenez quels types de clés peuvent être tournés automatiquement et lesquels nécessitent une rotation manuelle.

* Les clés KMS de chiffrement symétrique peuvent être tournées automatiquement.

* Les clés KMS asymétriques, les clés KMS HMAC et les magasins de clés personnalisés nécessitent une rotation manuelle.

* Les clés KMS avec du matériel de clé importé nécessitent également une rotation manuelle.

Pour plus d'informations, consultez le [guide du développeur AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

### Analyse des images Amazon ECR

Vous pouvez analyser les images Amazon Elastic Container Registry (ECR) pour détecter les vulnérabilités. Il existe deux types d'analyse disponibles dans ECR :

* **Analyse avancée**—Amazon ECR s'intègre à Amazon Inspector pour fournir une analyse automatisée et continue de vos dépôts. L'analyse avancée offre ce qui suit :

    * Vulnérabilités des paquets du système d'exploitation et des langages de programmation.

    * Deux fréquences d'analyse : analyse à la poussée et analyse continue.

* **Analyse de base**—Amazon ECR propose deux versions d'analyse de base qui utilisent la base de données des vulnérabilités et expositions courantes (CVEs) :

    * La version actuelle GA, qui utilise le projet open-source Clair

    * Une version améliorée qui utilise la technologie native AWS

L'analyse de base offre :

* Des analyses du système d'exploitation

* Deux fréquences d'analyse : manuelle et analyse à la poussée

### Implémentation du trafic chiffré de bout en bout

Sachez quand vous avez un cas d'utilisation qui nécessite la mise en œuvre d'un trafic chiffré de bout en bout. Les étapes sont listées ci-dessous :

1. Configurez votre distribution CloudFront pour exiger HTTPS pour toutes les requêtes des utilisateurs.

    * Utilisez un certificat SSL/TLS personnalisé (d'AWS Certificate Manager ou importé) pour CloudFront.

    * Utilisez un certificat SSL/TLS tiers sur votre Application Load Balancer (ALB) ou vos instances EC2.

    * Assurez-vous d'utiliser le même certificat sur vos instances EC2 que sur votre ALB pour la cohérence.

### Stockage sécurisé des identifiants RDS

Apprenez à stocker de manière sécurisée les identifiants RDS. AWS Secrets Manager est le service recommandé pour stocker et gérer des informations sensibles comme les identifiants de base de données. Il n'est pas judicieux de coder en dur les identifiants de base de données dans votre code ou de les stocker dans Lambda en tant que variables d'environnement.

### CloudTrail : Événements de données vs Événements de gestion

Comprenez les différences entre les événements de données et les événements de gestion dans CloudTrail.

* **Événements de gestion**

    * Fournissent des informations sur les opérations de gestion effectuées sur les ressources dans votre compte AWS.

    * Exemples incluent :

        * Opérations IAM AttachRolePolicy

        * Opérations Amazon EC2 CreateSubnet

        * Opérations AWS CloudTrail CreateTrail

* **Événements de données**

    * Fournissent des informations sur les opérations de ressources effectuées sur ou au sein d'une ressource.

    * Exemples incluent :

        * Activité de l'API au niveau des objets Amazon S3

        * Activité d'exécution des fonctions AWS Lambda

        * Activité de l'API au niveau des objets Amazon DynamoDB sur les tables

    * Les événements de données ne sont pas journalisés par défaut.

### GuardDuty : Règles de suppression, listes d'IP de confiance et listes de menaces

Attendez-vous à des questions sur les règles de suppression et sur la manière d'ajouter des IP connues aux listes d'IP de confiance et aux listes de menaces lors des tests de pénétration.

* [Documentation sur les règles de suppression de GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/findings_suppression-rule.html)

* [Documentation sur les listes de téléchargement de GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html)

Comprenez quels journaux sont analysés par AWS GuardDuty. Ceux-ci incluent les journaux d'événements de gestion AWS CloudTrail, les journaux de flux VPC, les journaux DNS, les journaux d'audit EKS, les événements de données S3 et l'activité d'exécution des charges de travail EKS, EC2 et ECS.

### E-mail d'abus AWS

Sachez comment répondre à un e-mail d'abus AWS.

* Examinez attentivement l'avis d'abus pour comprendre quel contenu ou quelle activité a été signalée. Le rapport inclut généralement des journaux ou d'autres preuves impliquant l'activité abusive.

* Enquêtez sur le problème signalé au sein de vos ressources AWS.

* Vérifiez et comprenez la cause de l'abus signalé.

* Prenez des mesures immédiates pour arrêter ou prévenir l'activité abusive. Cela peut impliquer :

    * La suppression ou la modification de contenu offensant

    * La sécurisation des ressources compromis

    * La mise à jour des paramètres de sécurité

    * La révocation de l'accès non autorisé

### Inspector

Vous devez savoir quels services AWS sont analysés par AWS Inspector.

* Amazon Inspector peut évaluer :

    * Les instances EC2

    * Les images de conteneurs dans Amazon ECR

    * Les fonctions Lambda pour les vulnérabilités et les problèmes de sécurité

Les services AWS suivants s'intègrent avec Amazon Inspector :

* AWS Security Hub pour une vue centralisée des résultats de sécurité

* Amazon EventBridge pour des réponses automatisées aux résultats

* AWS Systems Manager pour la gestion des correctifs basée sur les résultats d'Inspector

* Amazon Elastic Container Registry (ECR) pour l'analyse des images de conteneurs

### AWS Config

Apprenez ces règles importantes d'AWS Config :

* **encrypted-volumes** : Vérifie si les volumes EBS attachés sont chiffrés.

* **s3-bucket-public-read-prohibited** : Garantit que vos compartiments S3 ne permettent pas l'accès en lecture publique.

* **iam-user-no-policies-check** : Vérifie que les utilisateurs IAM n'ont pas de politiques directement attachées (la meilleure pratique est d'utiliser des politiques de groupe).

* **root-account-mfa-enabled** : Vérifie si le compte racine a l'authentification multifacteur (MFA) activée.

* **ec2-instances-in-vpc** : Garantit que toutes les instances EC2 sont lancées dans un VPC.

* **cloudtrail-enabled** : Vérifie que CloudTrail est activé dans votre compte.

* **rds-instance-public-access-check** : Vérifie si les instances RDS ne sont pas accessibles publiquement.

* **iam-password-policy** : Garantit que la politique de mot de passe du compte répond à des exigences de complexité spécifiées.

* **restricted-ssh** : Vérifie si les groupes de sécurité permettent un trafic SSH entrant sans restriction.

* **cloudwatch-alarm-action-check** : Vérifie si les alarmes CloudWatch ont au moins une action d'alarme, une action INSUFFICIENT\_DATA ou une action OK activée.

Pour plus de détails, consultez la [documentation sur les règles gérées par AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).

### Trusted Advisor

Soyez conscient des vérifications effectuées par AWS Trusted Advisor :

* **Groupes de sécurité - Ports spécifiques non restreints** : Identifie les groupes de sécurité qui permettent un accès non restreint à des ports spécifiques, exposant potentiellement vos ressources à des risques de sécurité.

* **Utilisation d'IAM** : Garantit que vous suivez les meilleures pratiques de sécurité en utilisant des utilisateurs, groupes et rôles IAM pour contrôler l'accès à vos ressources AWS, plutôt que d'utiliser les identifiants de votre compte racine.

* **MFA sur le compte racine** : Vérifie si l'authentification multifacteur (MFA) est activée sur l'utilisateur racine de votre compte AWS, améliorant ainsi considérablement la sécurité.

* **Instantanés EBS publics** : Identifie les instantanés EBS qui sont accessibles publiquement, ce qui pourrait entraîner une exposition non intentionnelle des données.

* **Instantanés RDS publics** : Similaire à la vérification EBS, identifie les instantanés RDS qui sont accessibles publiquement.

* **Autorisations des compartiments S3** : Vérifie les compartiments S3 avec des autorisations d'accès ouvertes ou ceux qui permettent l'accès à tout utilisateur AWS authentifié.

* **Journalisation CloudTrail** : Vérifie si CloudTrail est activé pour toutes les régions, crucial pour maintenir une trace d'audit des actions effectuées sur votre compte AWS.

* **Politique de mot de passe IAM** : Vérifie si votre politique de mot de passe IAM est conforme aux meilleures pratiques de sécurité, telles que les exigences de longueur et de complexité minimales.

* **Clés d'accès exposées** : Identifie si l'une de vos clés d'accès AWS a été exposée publiquement sur des dépôts de code ou d'autres sites publics.

* **Groupes de sécurité - Accès non restreint** : Vérifie les groupes de sécurité qui permettent un accès non restreint (0.0.0.0/0) à des ports spécifiques.

### Chiffrement S3

Apprenez les différents cas d'utilisation pour les options de chiffrement S3.

* **Chiffrement côté serveur (SSE)**

    * Il s'agit de la méthode de chiffrement par défaut pour tous les nouveaux compartiments et objets.

    * Amazon S3 gère la gestion des clés et le chiffrement/déchiffrement automatiquement.

    * Utilise l'algorithme de chiffrement AES-256.

    * Chaque objet est chiffré avec une clé unique, et la clé elle-même est chiffrée avec une clé principale régulièrement tournée.

* **SSE-KMS (Chiffrement côté serveur avec des clés gérées par AWS KMS)**

    * Utilise AWS Key Management Service (KMS) pour gérer les clés de chiffrement.

    * Fournit un contrôle supplémentaire et une trace d'audit pour vos clés.

    * Vous permet d'utiliser des clés gérées par le client (CMK) ou des clés gérées par AWS.

    * Vous permet de définir des politiques de rotation des clés et de contrôler l'utilisation des clés via des politiques IAM.

* **SSE-C (Chiffrement côté serveur avec des clés fournies par le client)**

    * Vous gérez vos propres clés de chiffrement.

    * S3 effectue le chiffrement/déchiffrement, mais vous fournissez la clé avec chaque requête.

    * Les clés ne sont pas gérées par AWS ; vous devez fournir la clé correcte pour accéder à l'objet.

* **Chiffrement côté client**

    * Les données sont chiffrées avant d'être envoyées à S3.

    * Vous pouvez utiliser le client de chiffrement Amazon S3 ou implémenter votre propre chiffrement côté client.

    * Fournit un chiffrement de bout en bout, car les données sont chiffrées avant de quitter votre application.

Pour plus d'informations, regardez cette [vidéo](https://www.youtube.com/watch?v=2uaeFDlVPlY).

### CloudFormation et secrets

L'utilisation de secrets dans AWS CloudFormation est un excellent moyen de gérer des informations sensibles de manière sécurisée. CloudFormation prend en charge les références dynamiques aux secrets stockés dans AWS Secrets Manager.

Dans l'exemple ci-dessous, MySecret:`{{resolve:secretsmanager:SecretName:SecretKey:VersionStage:VersionId}}` récupère le champ 'password' du secret 'MySecretName' dans Secrets Manager.

```json
MySecret:
  Type: AWS::SecretsManager::Secret
  Properties:
    Name: MySecretName
    Description: "Ceci est mon secret"
    SecretString: '{"username":"myuser","password":"mypassword"}'
```

### VPC FlowLog

Comprenez les cas d'utilisation de l'utilisation des journaux de flux VPC.

* Identifiez les schémas de trafic inhabituels ou les connexions refusées inattendues.

* Détectez les menaces de sécurité potentielles en identifiant les adresses IP suspectes ou les activités de port inhabituelles.

* Vous pouvez configurer des alertes automatisées à l'aide des alarmes CloudWatch pour des schémas de trafic spécifiques.

```json
2 123456789010 eni-1234567890abcdef0 10.0.1.5 10.0.0.220 39812 80 6 20 4249 1418530010 1418530070 ACCEPT O
```

Décortiquons cette entrée de journal :

1. Numéro de version (2)

2. ID de compte AWS (123456789010)

3. ID de l'interface réseau (eni-1234567890abcdef0)

4. Adresse IP source (10.0.1.5)

5. Adresse IP de destination (10.0.0.220)

6. Port source (39812)

7. Port de destination (80)

8. Protocole (6 = TCP)

9. Paquets transférés (20)

10. Octets transférés (4249)

11. Heure de début (1418530010)

12. Heure de fin (1418530070)

13. Action (ACCEPT)

14. Statut du journal (0)

### Politiques de verrouillage de coffre S3 Glacier et options de récupération d'archivage

Les politiques de verrouillage de coffre S3 Glacier sont une fonctionnalité puissante pour imposer des contrôles de conformité sur vos coffres Amazon S3 Glacier. Ces politiques vous permettent de créer et de verrouiller des règles qui contrôlent l'accès à vos archives, garantissant que vos politiques de conservation et de suppression des données sont strictement appliquées.

Lors de l'initiation d'un travail pour récupérer une archive, vous pouvez spécifier l'une des options de récupération suivantes, en fonction de vos exigences de temps d'accès et de coût.

* **Expedited** : Les récupérations expedited vous permettent d'accéder rapidement à vos données stockées dans la classe de stockage S3 Glacier Flexible Retrieval ou le niveau d'accès aux archives S3 Intelligent-Tiering lorsque des demandes urgentes occasionnelles de restauration d'archives sont nécessaires. Pour toutes les archives sauf les plus grandes (plus de 250 Mo), les données accessibles à l'aide des récupérations expedited sont généralement disponibles en 1 à 5 minutes. La capacité provisionnée garantit que la capacité de récupération pour les récupérations expedited est disponible lorsque vous en avez besoin.

* **Standard** : Les récupérations standard vous permettent d'accéder à n'importe laquelle de vos archives en quelques heures. Les récupérations standard sont généralement terminées en 3 à 5 heures. Standard est l'option par défaut pour les demandes de récupération qui ne spécifient pas l'option de récupération.

* **Bulk** : Les récupérations bulk sont l'option de récupération S3 Glacier la moins coûteuse, que vous pouvez utiliser pour récupérer de grandes quantités, même des pétaoctets, de données de manière économique en un jour. Les récupérations bulk sont généralement terminées en 5 à 12 heures.

### Copie des instantanés chiffrés RDS

* Vous ne pouvez pas partager des instantanés qui sont chiffrés avec la clé gérée par AWS par défaut. Vous ne pouvez partager que des instantanés qui sont chiffrés avec une clé gérée par le client.

* Vous ne pouvez partager que des instantanés non chiffrés publiquement.

* Lorsque vous partagez un instantané chiffré, vous devez également partager la clé gérée par le client utilisée pour chiffrer l'instantané.

* Puisque vous ne pouvez pas partager un instantané qui est chiffré avec la clé gérée par AWS par défaut, vous pouvez d'abord copier l'instantané. Lorsque vous copiez un instantané, vous pouvez chiffrer la copie ou vous pouvez spécifier une clé KMS différente de l'originale, et l'instantané copié résultant utilise la nouvelle clé KMS.

* De plus, vous ne pouvez pas activer le chiffrement des instantanés sur les RDS existants.

### Protections WAF

Comprenez à quel niveau AWS WAF fonctionne. AWS WAF (Web Application Firewall) fonctionne principalement au niveau de la couche application (couche 7) du [modèle OSI (Open Systems Interconnection)](https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/).

### AWS Config Aggregator

Vous pouvez vous attendre à des questions sur AWS Config Aggregator. Cette fonctionnalité vous permet de rassembler des données de configuration et de conformité provenant de plusieurs comptes et régions dans un seul compte, vous offrant une vue complète de vos ressources AWS.

Pour plus d'informations, consultez la [documentation AWS Config Aggregator](https://docs.aws.amazon.com/config/latest/developerguide/aggregated-create.html).

### AWS Macie

Apprenez à catégoriser vos données à l'aide d'Amazon Macie.

* Macie peut analyser automatiquement vos compartiments S3 pour identifier les données sensibles telles que les informations personnelles identifiables (PII), les données financières ou la propriété intellectuelle.

* Macie aide à évaluer et à surveiller la posture de sécurité de vos compartiments S3, en identifiant les mauvaises configurations ou les politiques d'accès trop permissives.

* Classifie automatiquement les données en fonction de leur sensibilité, aidant les organisations à gérer et à protéger les données selon leur importance.

### AWS CloudFront OAI

Apprenez à restreindre l'accès des utilisateurs au contenu directement depuis S3.

Pour limiter l'accès des utilisateurs au contenu directement depuis S3 lors de l'utilisation d'Amazon CloudFront, vous pouvez utiliser l'identité d'accès à l'origine (OAI). Une OAI est un utilisateur CloudFront spécial qui vous permet de restreindre l'accès au contenu de votre compartiment S3. Lorsque vous créez une OAI, CloudFront la connecte à votre distribution, et vous pouvez configurer votre compartiment S3 pour n'autoriser l'accès que depuis cette OAI.

### AWS CloudHSM

Utilisez AWS CloudHSM au lieu de KMS lorsque vous souhaitez un contrôle total sur le matériel de gestion des clés et les clés.

AWS CloudHSM vous permet de gérer et d'utiliser vos clés sur du matériel approuvé FIPS. Il utilise des instances HSM à locataire unique, appartenant au client, qui fonctionnent dans votre propre Virtual Private Cloud (VPC). Si vous avez besoin d'un contrôle total sur le module de sécurité matériel (HSM) qui stocke et gère vos clés cryptographiques, CloudHSM est le meilleur choix.

### Types de clés AWS KMS

Apprenez les types de clés KMS disponibles :

1. **Clés symétriques**

    * Clés gérées par AWS

    * Clés gérées par le client

2. **Clés asymétriques** : Elles se composent d'une paire de clés publique et privée.

3. **Clés HMAC** : Utilisées pour générer et vérifier l'authentification de message basée sur le hachage.

4. **Clés multi-régions** : Un ensemble de clés interopérables qui peuvent être répliquées dans plusieurs régions AWS. Elles sont utiles pour chiffrer des données dans plusieurs régions ou pour des scénarios de reprise après sinistre.

5. **Clés avec matériel de clé importé** : Permet d'importer votre propre matériel de clé dans KMS.

6. **Clés dans des magasins de clés personnalisés** : Permet de créer et de gérer des clés KMS dans un cluster AWS CloudHSM.

### Quelques notes sur AWS CloudTrail

1. Activez CloudTrail dans toutes les régions : Pour garantir une journalisation complète, activez CloudTrail dans chaque région AWS. Cela vous donne un enregistrement complet des activités dans toute votre infrastructure AWS.

2. Utilisez un compartiment S3 dédié : Stockez les journaux CloudTrail dans un compartiment S3 spécifique avec des contrôles d'accès stricts. Cela aide à prévenir l'accès non autorisé et garantit l'intégrité de vos journaux d'audit.

3. Activez la validation de l'intégrité des fichiers journaux : Cette fonctionnalité utilise des algorithmes standard de l'industrie pour garantir que vos fichiers journaux n'ont pas été altérés après leur livraison à S3.

4. Chiffrez les fichiers journaux : Utilisez le chiffrement côté serveur avec des clés gérées par AWS KMS (SSE-KMS) pour sécuriser vos fichiers journaux CloudTrail pendant leur stockage. Cela fournit une couche supplémentaire de sécurité pour vos données d'audit.

5. Pour le compartiment S3 qui stocke les journaux CloudTrail, activez la suppression avec authentification multifacteur (MFA). Cela aide à prévenir la suppression non autorisée des fichiers journaux.

6. Utilisez les règles AWS Config pour vous assurer que CloudTrail est toujours activé et configuré correctement dans tous vos comptes.

7. Passez régulièrement en revue et analysez vos journaux CloudTrail. Envisagez d'utiliser des services AWS comme Amazon Athena ou des outils SIEM tiers pour l'analyse des journaux.

8. Si vous utilisez AWS Organizations, envisagez de configurer des traces à l'échelle de l'organisation pour centraliser la journalisation pour tous les comptes de votre organisation.

### Réplication S3

Apprenez à répliquer des objets S3 chiffrés entre les régions.

* La versioning doit être activée sur les compartiments source et de destination.

* Créez un rôle de réplication : Créez un rôle IAM qui permet à S3 d'assumer le rôle et d'effectuer des tâches de réplication.

* Attachez une politique au rôle de réplication : Cette politique doit accorder des autorisations pour lire depuis le compartiment source et écrire dans le compartiment de destination.

* Vous pouvez configurer la réplication en utilisant la console de gestion AWS, l'AWS CLI.

* Autorisations des clés KMS : Si vous utilisez AWS KMS pour le chiffrement, vous devez accorder au rôle de réplication l'autorisation d'utiliser la clé KMS dans les régions source et de destination.

### AWS Service Catalog

Apprenez les cas d'utilisation d'AWS Service Catalog.

Vous pouvez utiliser AWS Service Catalog pour standardiser vos applications et les distribuer à vos équipes. Par exemple, si vous souhaitez définir des restrictions sur le chiffrement et les AMI, vous pouvez créer une pile d'application complète et la partager avec votre équipe.

### MFA pour les utilisateurs Active Directory

Vous pouvez activer l'authentification multifacteur (MFA) pour votre répertoire AWS Managed Microsoft AD afin d'augmenter la sécurité lorsque vos utilisateurs spécifient leurs identifiants AD pour accéder aux applications Amazon Enterprise prises en charge.

Lorsque vous activez la MFA, vos utilisateurs entrent leur nom d'utilisateur et leur mot de passe (premier facteur) comme d'habitude, et ils doivent également entrer un code d'authentification (le deuxième facteur) qu'ils obtiennent de votre solution MFA virtuelle ou matérielle.

### AWS IAM Access Analyzer

* Analyse de l'accès inter-comptes : Aide à identifier les ressources qui sont partagées avec des comptes AWS externes, garantissant que seul l'accès inter-comptes prévu existe.

## Conclusion

Obtenir la certification AWS Certified Security Specialty a été une excellente expérience qui m'a permis d'en apprendre davantage sur la sécurité AWS. En étudiant et en appliquant ce que j'ai appris, j'ai acquis des connaissances utiles sur la sécurisation des environnements AWS.

Cette certification a prouvé mes compétences et m'a donné les outils pour appliquer les meilleures pratiques dans des situations réelles. Que vous soyez nouveau dans la sécurité AWS ou que vous souhaitiez améliorer vos compétences, obtenir cette certification peut être une partie importante de votre croissance professionnelle.

J'espère que mes expériences vous encourageront et vous aideront dans votre parcours de certification. Gardez à l'esprit que l'apprentissage continu et l'implication dans la communauté sont importants pour rester à jour dans le monde en constante évolution de la sécurité du cloud.