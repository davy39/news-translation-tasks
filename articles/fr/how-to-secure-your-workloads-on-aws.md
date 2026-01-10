---
title: Comment sécuriser vos charges de travail sur AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-10T17:21:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-workloads-on-aws
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Secure-Your-Workloads-on-AWS.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Services
  slug: cloud-services
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Comment sécuriser vos charges de travail sur AWS
seo_desc: "By Riya Sander\nBusinesses are trying to save money these days, so many\
  \ are moving to the cloud. And a study suggests that the global public cloud services\
  \ market will have grown 6.3% in 2020. \nCloud services revenue will go up to US$257.9\
  \ billion fro..."
---

Par Riya Sander

Les entreprises cherchent à économiser de l'argent ces jours-ci, donc beaucoup migrent vers le cloud. Une étude suggère que le [marché mondial des services cloud publics](https://www.gartner.com/en/newsroom/press-releases/2020-07-23-gartner-forecasts-worldwide-public-cloud-revenue-to-grow-6point3-percent-in-2020#:~:text=The%20worldwide%20public%20cloud%20services,increasing%2095.4%25%20to%20%241.2%20billion.) aura augmenté de 6,3 % en 2020.

Les revenus des services cloud atteindront 257,9 milliards de dollars américains, contre 242,7 milliards de dollars en 2019. Mais à mesure que les technologies deviennent plus avancées, les pirates deviennent meilleurs pour utiliser ces technologies afin d'accéder à vos données critiques. Les [attaques basées sur le cloud](https://www.fintechnews.org/the-2020-cybersecurity-stats-you-need-to-know/) ont augmenté de 630 % entre janvier et avril 2020.

Avec davantage de données stockées dans le cloud, les entreprises doivent disposer de politiques de sécurité robustes. Elles doivent également inclure les meilleures pratiques pour traiter les données stockées dans des services cloud comme AWS.

Avec environ 83 % des [charges de travail des entreprises migrant vers le cloud](https://www.varonis.com/blog/cybersecurity-statistics/) d'ici la fin de 2020, une grande quantité de données critiques doit être protégée.

Dans cet article, nous discuterons de certaines meilleures pratiques que les entreprises devraient mettre en œuvre pour protéger les données qu'elles ont migrées vers le cloud.

## Consultez la documentation AWS

La [documentation AWS](https://docs.aws.amazon.com/) détaille les responsabilités du client ainsi que celles d'AWS. Le [modèle de responsabilité partagée](https://aws.amazon.com/compliance/shared-responsibility-model) stipule qu'AWS est responsable de la protection de l'infrastructure qui exécute les services proposés sur le cloud AWS.

Les responsabilités du client incluent la configuration et la gestion de la sécurité des services qu'ils choisissent d'utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/shared-responsibility-model.png)
_[Source](https://aws.amazon.com/compliance/shared-responsibility-model)_

## Utilisez Identity and Access Management

La documentation AWS stipule catégoriquement que le client doit utiliser les outils Identity and Access Management (IAM) pour protéger ses données. L'[outil AWS IAM](https://aws.amazon.com/iam/) vous permet de gérer les utilisateurs qui auront accès au cloud.

IAM permet aux utilisateurs de contrôler l'accès à certaines ressources. L'outil permet également aux clients de créer et de gérer des utilisateurs et des groupes AWS.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/aws-vpc-module.png)
_[Source](https://aws.amazon.com/blogs/aws/category/iam)_

Des autorisations spécifiques sont fournies pour permettre ou refuser l'accès à diverses ressources AWS. Si vous souhaitez attribuer des autorisations à une seule ressource, vous pouvez créer des politiques comme suit :

* **Actions** : quelles actions de service sont autorisées.
* **Ressources** : pour quelles ressources vous autoriserez ces actions.
* **Effet** : si vous refusez ou autorisez l'accès.
* **Conditions** : les exigences pour lesquelles les actions prendront effet.

Votre webmaster peut créer un ou plusieurs utilisateurs IAM dans le compte AWS. Vous pouvez créer les utilisateurs dans la Console de gestion AWS, et vous pouvez ajouter jusqu'à dix utilisateurs à la fois.

## Utilisez l'authentification multifactorielle

Bien que le stockage de vos données sur AWS soit assez sécurisé, vous devez encore prendre des précautions contre l'accès non autorisé à ces données.

Comme suggéré par AWS, vous pouvez utiliser l'[authentification multifactorielle (MFA)](https://aws.amazon.com/iam/features/mfa/) pour une couche supplémentaire de sécurité. Utiliser uniquement votre identifiant utilisateur et votre mot de passe peut ne pas être suffisamment sûr, car les pirates ont développé de nombreuses méthodes pour contourner votre mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/sign-in-aws-with-mfa.png)
_[Source](https://aws.amazon.com/blogs/security/use-yubikey-security-key-sign-into-aws-management-console)_

Vous pouvez également contrôler l'accès aux API d'AWS en utilisant la MFA. Vous pouvez activer et gérer un appareil MFA virtuel pour un utilisateur IAM dans le compte AWS.

Il suffit de se connecter à la Console de gestion AWS et d'ajouter la MFA après avoir choisi l'utilisateur.

## Ayez un appareil de sécurité robuste en place

Les bases de données relationnelles d'Amazon doivent être chiffrées, sauf si elles sont déjà chiffrées au niveau du stockage. Les clés IAM doivent être changées tous les trois mois.

Vous devez également étiqueter vos instances EC2 de manière logique, car cela peut fournir plus d'informations sur l'emplacement de l'instance et son utilisation. Cela vous aide également à maintenir la cohérence dans votre environnement.

L'étiquetage peut également vous aider à gérer vos ressources Amazon plus efficacement. Votre webmaster peut localiser, classer et identifier les ressources pour leurs divers besoins.

Le filtrage peut vous aider à trouver et à valider les normes d'étiquetage entreprises dans votre organisation. Vous pouvez utiliser des outils automatisés pour aider dans le processus d'étiquetage. Il existe une API Resource Groups Tagging pour vous aider à filtrer, gérer et rechercher des étiquettes.

## **Formez vos employés**

Tout en prenant des mesures pour améliorer la sécurité de vos systèmes sur le cloud AWS, vous devez également organiser des sessions de formation périodiques pour vos employés.

Des études montrent que les pirates ciblent souvent les employés pour accéder aux réseaux protégés. Un petit relâchement dans les défenses peut entraîner une potentielle violation de données qui peut endommager votre organisation.

Vos employés doivent être conscients des protocoles de sécurité que vous utilisez pour protéger vos données sur AWS. Si tout le monde dans votre organisation n'est pas conscient de ces protocoles, vous pourriez avoir des problèmes à les faire respecter.

Lorsque vous introduisez de nouveaux processus, vous devriez organiser une courte session de formation pour vos employés. Vous pouvez également créer des vidéos d'auto-apprentissage et avoir un quiz à la fin.

## Utilisez le chiffrement de bout en bout

Le chiffrement de bout en bout aide à protéger vos données contre l'accès non autorisé - vous devez simplement installer un certificat SSL sur AWS.

La Console de gestion AWS peut utiliser le certificat SSL entre les points de terminaison du service de la console et le navigateur du client. Le certificat SSL permettra une interaction chiffrée entre un navigateur et le serveur web. Le navigateur client peut authentifier l'identité du point de terminaison du service de contrôle.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/LDAP-security-in-AWS-Directory-Service.png)
_[Source](https://aws.amazon.com/blogs/security/how-to-improve-ldap-security-in-aws-directory-service-with-client-side-ldaps)_

L'utilisation du protocole HTTPS peut aider à protéger vos données sensibles. Mais vous devez également prendre en compte les exigences supplémentaires en ressources lorsque vos serveurs gèrent des centaines de sessions SSL/TLS.

Pour installer le certificat, vous devez convertir le certificat et les intermédiaires au format PEM. Ensuite, vous devez le télécharger sur votre compte AWS et configurer un écouteur HTTPS. Examinons ce processus un peu plus en détail.

### Comment installer SSL sur votre serveur AWS

Une fois la CSR générée et soumise à l'autorité de certification, l'autorité de certification vérifie les détails et émet un certificat SSL.

Le fichier de clé privée et le fichier de certificat sont tous deux au format .CRT. Une fois que vous avez ces deux fichiers, vous devez les télécharger sur le serveur.

* Tout d'abord, connectez-vous à AWS et connectez-vous à AWS EC2.
* Ensuite, parcourez le menu de navigation >> cliquez sur « **Sécurité du réseau** » >> choisissez « **Équilibreurs de charge** ».
* Parcourez le panneau principal et sélectionnez l'icône des Équilibreurs de charge lors du téléchargement du certificat.
* Maintenant, cliquez sur l'onglet « **Écouteurs** » et cliquez sur « **Modifier** » et « **Ajouter** ».
* Choisissez HTTPS dans la colonne du certificat SSL et cliquez sur « **changer** » dans la même colonne.
* Cliquez sur le bouton radio « **Téléverser un nouveau certificat SSL vers AWS Identity and Access Management (IAM)** ». Vous pouvez également renommer le certificat ici.
* Dans le champ de la clé privée, collez tout le contenu de la clé privée dans la boîte fournie « ----BEGIN RSA PRIVATE KEY---- » et « ----END RSA PRIVATE KEY---- ».
* Dans le certificat de clé publique, collez les détails du certificat dans le champ respectif « ----BEGIN CERTIFICATE---- » et « ----END CERTIFICATE---- ».
* Enfin, collez la chaîne de certificats ou CA Bundle.crt dans la colonne respective « ----BEGIN CERTIFICATE---- » et « ----END CERTIFICATE---- ».
* Cliquez sur **Enregistrer** pour terminer le processus d'installation. IAM vérifiera et confirmera l'installation après le téléchargement du certificat.
* Redémarrez votre instance **AWS EC2** pour voir les changements.

## Ayez une politique de récupération appropriée en place

Vous devez avoir une politique de sauvegarde et de récupération robuste en place. Même si votre sécurité est de premier ordre, la sauvegarde et la récupération après sinistre sont essentielles.

AWS Backup peut vous aider à trouver les bons outils pour une solution de sauvegarde et de récupération évolutive. Leur processus de sauvegarde centralisé vous permet d'automatiser et de centraliser facilement votre sauvegarde.

Votre webmaster peut facilement surveiller ce processus de sauvegarde pour un certain nombre de ressources AWS. De plus, vous pouvez créer des politiques de sauvegarde dans la console AWS Backup en seulement quelques clics.

Pour démarrer votre sauvegarde AWS, vous devez vous connecter à votre compte AWS et lancer la console AWS Backup.

Ensuite, créez un plan de sauvegarde et allouez les ressources. Les ressources seront sauvegardées en fonction de votre politique.

Une fois les ressources sauvegardées, l'utilisateur peut les surveiller, les restaurer ou les modifier si nécessaire.

Voici quelques étapes que vous devriez suivre pour créer un Plan de Récupération après Sinistre (DRP) :

* Créez un ensemble d'instructions définissant les règles et réglementations relatives au DRP. Cela s'appelle la Déclaration de Contingence de Gestion de la Récupération après Sinistre.
* Effectuez une analyse d'impact sur l'entreprise pour avoir une idée des applications et composants IT critiques ainsi que de l'impact des risques associés à l'entreprise.
* Prenez des mesures de contrôle préventives, détectives et correctives qui détectent et minimisent votre ratio de risque. De plus, maintenez les logiciels de sécurité à jour, installez des alarmes incendie, organisez des sessions de formation pour les employés et installez des logiciels de surveillance de réseau et de serveur.
* Identifiez les départements d'application et d'entreprise qui seront marginalement impactés en cas de défaillance (faible assurance de défaillance).
* Effectuez des tests pour vérifier si des changements sont survenus après chaque processus de test. La direction et les employés doivent être formés au processus de récupération après sinistre.

## **Utilisez CloudTrail**

[CloudTrail](https://aws.amazon.com/cloudtrail) aide à l'audit opérationnel et des risques ainsi qu'à la conformité et à la gouvernance de votre compte AWS.

Ses services permettent à votre webmaster de surveiller en continu l'activité sur votre compte AWS. Il préserve également un historique de toutes les activités sur tous vos services AWS.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/AWS-CloudTrail.png)
_[Source](https://aws.amazon.com/cloudtrail)_

CloudTrail vous aidera à suivre les changements de ressources, analyser vos protocoles de sécurité et détecter les activités inhabituelles sur votre compte. Vous devez identifier les données qui sont critiques pour vos activités.

Vous pouvez analyser les journaux de CloudTrail car ils collectent des données critiques sur l'utilisation de vos comptes AWS. CloudTrail doit être activé dans toutes les géographies pour vous fournir ces informations.

### Comment configurer AWS CloudTrail

Lorsque vous créez une piste dans votre compte AWS, cela vous permet d'utiliser d'autres services AWS. Avec cela, vous pouvez vérifier les données d'événement stockées dans les journaux de CloudTrail. CloudTrail est inclus par défaut lorsque vous créez un compte AWS.

#### Configurer Cloud Trail pour toutes les régions

Nommez votre CloudTrail et choisissez « Oui » pour « Appliquer la piste à toutes les régions ». Vous devez l'appliquer à toutes les régions même si vous ne gérez qu'un seul pays. Vous pouvez vérifier l'activité des autres régions en comparaison avec la vôtre.

#### Sélectionner le journal des événements

Vous pouvez journaliser des événements dissemblables comme les événements de gestion, de données et d'informations. Vous devez choisir les types d'événements en fonction des besoins de votre organisation.

#### Activer la validation des fichiers journaux

Vous devez configurer les journaux sur vos compartiments S3, qui sont par défaut chiffrés avec le chiffrement SSE-S3. Sous l'option d'emplacement de stockage, vous pouvez cliquer sur « Oui » pour « Activer la validation des fichiers journaux ».

#### Configurer les alarmes CloudWatch

Une fois que vous avez créé une piste dans votre compte AWS, vous pouvez configurer la sécurité CloudWatch en cliquant sur le bouton « configurer ».

Après cela, activez IAM en cliquant sur « Créer des alarmes CloudWatch pour l'activité des API liées à la sécurité et au réseau en utilisant le modèle CloudFormation ».

Lorsque vous faites cela, vous recevrez une notification concernant tout appel de sécurité API.

Maintenant, CloudTrail devrait être entièrement configuré.

## Utilisez AWS Trusted Advisor

[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor) vous aide à surveiller tous les aspects de vos services cloud.

Il surveille l'environnement cloud et les applications qui y fonctionnent. Il vous permet également de scanner vos réseaux internes et de les comparer avec les normes d'AWS.

Vous pouvez accéder à AWS Trusted Advisor depuis la Console de gestion AWS. Tous les comptes ont accès à certaines des vérifications.

Les entreprises doivent souscrire aux niveaux Business ou Enterprise du support AWS pour avoir accès à toutes les vérifications.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/AWS-Trusted-Advisor.png)
_[Source](https://aws.amazon.com/premiumsupport/technology/trusted-advisor)_

Vous pouvez obtenir les vérifications suivantes via AWS sans frais supplémentaires :

* **Vérification de l'utilisation d'IAM** : vérifie si le client respecte les meilleures pratiques de sécurité et si des utilisateurs, groupes et rôles ont été créés pour contrôler l'accès aux ressources AWS.
* **Vérification des limites de service** : Votre position pour les limites de service essentielles pour les différents produits est vérifiée.
* **Vérification de la MFA sur le compte racine** : vérifie si vous utilisez la MFA.
* **Groupes de sécurité** (Vérification des ports spécifiques non restreints) : Cette vérification est essentielle et informe le webmaster si l'accès à vos instances EC2 est trop permissif. Elle aide à prévenir les attaques par déni de service ou les piratages.

## Conclusion

Alors que de plus en plus d'entreprises migrent leurs données vers le cloud, elles doivent prendre plus de précautions pour gérer ces données de manière sûre et efficace.

Cette migration vers le cloud a entraîné davantage de violations de données, et les certificats SSL sont devenus essentiels pour des services AWS sécurisés.

J'espère que vous avez appris quelques meilleures pratiques pour vous aider à gérer vos services AWS dans cet article.