---
title: Comment installer Coolify dans AWS EC2 et avoir le pouvoir de tout faire dans
  le cloud
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2025-06-30T13:50:37.058Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-coolify-in-aws-ec2
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751291416644/05d052cc-dc58-49b4-ac16-3064001fd816.png
tags:
- name: AWS
  slug: aws
- name: hosting
  slug: hosting
- name: Open Source
  slug: opensource
seo_title: Comment installer Coolify dans AWS EC2 et avoir le pouvoir de tout faire
  dans le cloud
seo_desc: Coolify is an open-source, self-hostable platform that serves as an alternative
  to services like Heroku, Netlify, and Vercel. It lets developers deploy and manage
  applications, databases, and services on their own infrastructure, providing greater
  co...
---

Coolify est une plateforme open-source et auto-hébergeable qui sert d'alternative à des services comme Heroku, Netlify et Vercel. Elle permet aux développeurs de déployer et de gérer des applications, des bases de données et des services sur leur propre infrastructure, offrant ainsi un meilleur contrôle et une plus grande flexibilité.

Si vous souhaitez utiliser Coolify, vous avez deux options. Vous pouvez acheter leur plan cloud, ce qui vous coûte de l'argent. D'autre part, vous pouvez l'auto-héberger gratuitement et avoir une utilisation illimitée sans aucune restriction.

Dans cet article, je vais vous montrer comment auto-héberger Coolify directement dans une instance AWS EC2 et utiliser ses fonctionnalités. Je vais également vous montrer comment déployer n'importe quel site web directement dessus.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1747932644011/206603be-4687-4e0d-ab96-6c1271006cf5.png align="center")

Cet article inclut une vidéo pas à pas que j'ai réalisée pour vous. Vous pouvez regarder la vidéo sur ma [chaîne YouTube](https://www.youtube.com/@FahimAmin).

%[https://www.youtube.com/watch?v=LADT0Y_IcNU]

## Table des matières

* [Exigences pour l'auto-hébergement de Coolify](#heading-exigences-pour-lauto-hebergement-de-coolify)

* [Configurer une instance AWS EC2 pour Coolify](#heading-configurer-une-instance-aws-ec2-pour-coolify)

* [Groupe de sécurité d'AWS EC2](#heading-groupe-de-securite-daws-ec2)

* [Installer Coolify dans AWS EC2](#heading-installer-coolify-dans-aws-ec2)

* [Accéder à Coolify de n'importe où en utilisant l'IP publique](#heading-acceder-a-coolify-de-nimporte-ou-en-utilisant-lip-publique)

* [Comment déployer un site web via Coolify](#heading-comment-deployer-un-site-web-via-coolify)

* [Conclusion](#heading-conclusion)

## Exigences pour l'auto-hébergement de Coolify

Puisque nous allons auto-héberger Coolify dans le cloud pour cet article, vous devez vous assurer que vous avez au moins la spécification minimale du serveur. Selon Coolify, actuellement, les exigences minimales sont les suivantes :

### Exigences du serveur

* Un VPS (Virtual Private Server)

* Un serveur dédié

* Une machine virtuelle (VM)

* Un Raspberry Pi (voir notre [**Guide de configuration du système d'exploitation Raspberry Pi**](https://coolify.io/docs/knowledge-base/how-to/raspberry-pi-os#prerequisites))

* Ou tout autre serveur avec accès SSH

### Système d'exploitation pris en charge

* Basé sur Debian (par exemple, Debian, Ubuntu)

* Basé sur Redhat (par exemple, CentOS, Fedora, Redhat, AlmaLinux, Rocky, Asahi)

* Basé sur SUSE (par exemple, SLES, SUSE, openSUSE)

* Arch Linux

* Alpine Linux

* Raspberry Pi OS 64-bit (Raspbian)

### **Architectures prises en charge**

Coolify fonctionne sur des systèmes 64 bits :

* AMD64

* ARM64

### **Exigences matérielles minimales**

* **CPU** : 2 cœurs

* **Mémoire (RAM)** : 2 Go

* **Stockage** : 30 Go d'espace libre

Coolify peut fonctionner correctement sur des serveurs avec des spécifications inférieures à celles mentionnées ci-dessus, mais ils recommandent des exigences minimales légèrement supérieures. Cela garantit que les utilisateurs disposent de ressources suffisantes pour déployer plusieurs applications sans problèmes de performance.

Je vous recommande de consulter les [documents officiels](https://coolify.io/docs/get-started/installation), car il pourrait y avoir une mise à jour concernant les spécifications, et vous ne voulez pas manquer cette partie !

Je vais utiliser **AWS EC2** comme serveur pour ce guide.

## Configurer une instance AWS EC2 pour Coolify

Créez une nouvelle instance EC2 dans AWS.

![Créer EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003070325/e9f40038-12d7-4918-828a-3114d43f8185.png align="center")

Donnez-lui un nom approprié. Je vais utiliser `coolify-yt` pour cet article.

![Nom EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003129368/d9726de2-f5e9-4d87-abbd-15660438c510.png align="center")

Pour l'Amazon Machine Image (AMI), j'utiliserai la dernière version LTS d'Ubuntu (Ubuntu Server 24.04 LTS).

![Type AMI](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003224058/cf23f6b2-c099-40b8-bec1-a39fb0384907.png align="center")

L'architecture sera 64 bits (x86).

![Architecture AMI](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003299729/06970567-5523-4976-9156-d621ccf19899.png align="center")

Pour le type d'instance, je ne peux pas utiliser le niveau gratuit car cela ne répondrait pas aux spécifications minimales. Je vais donc utiliser le `t2.medium`.

![Type d'instance](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003366450/465a7aad-c049-486a-baf4-6fb9a8ee1537.png align="center")

Je vais créer une nouvelle paire de clés. Je vais utiliser RSA, et le format de fichier sera `.pem`.

![Paire de clés](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003554621/6ea1ccba-aeb9-496f-a207-37bf9d554e17.png align="center")

Lorsque vous cliquez sur `Create key pair`, il téléchargera un fichier `.pem`. Assurez-vous de le conserver en sécurité.

Pour le stockage, je prends un stockage par blocs de 50 Go. Mais vous pouvez suivre la spécification minimale de stockage de Coolify (30 Go) pour l'instant si vous le souhaitez.

![Configuration du stockage](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003637365/4238a847-271e-4f4b-a96f-5a84ec9bdf74.png align="center")

Si je veux utiliser mon Coolify de n'importe où, je dois cocher les trois cases dans les paramètres réseau.

* Autoriser le trafic SSH depuis (n'importe où)

* Autoriser le trafic HTTPS depuis Internet

* Autoriser le trafic HTTP depuis Internet

![Paramètres réseau](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003752198/d67af805-bef4-4273-b592-dd1703e56cfd.png align="center")

Maintenant, cliquez simplement sur "Lancer l'instance". Cela créera notre nouveau serveur EC2. Cela peut prendre quelques secondes à une demi-minute. Soyez patient et attendez qu'il termine sa tâche.

![Lancer l'instance](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003903936/277c79c0-f393-4d0f-a78e-5614915f9359.png align="center")

## Groupe de sécurité d'AWS EC2

Allez dans l'onglet des instances et trouvez le nom de votre nouvelle instance EC2. Ensuite, trouvez le nom de son groupe de sécurité.

![instances](https://cdn.hashnode.com/res/hashnode/image/upload/v1751003959839/d85e30ba-c75d-4c70-afb1-d21765e03045.png align="center")

J'ai le nom du groupe de sécurité pour mon nouvel EC2 comme "launch-wizard-7".

![Groupe de sécurité](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004072271/0a1294e6-ae5c-4f61-ab55-6fc3cb1db6be.png align="center")

Maintenant, allez dans l'onglet des groupes de sécurité et trouvez quel groupe de sécurité est associé à votre nouvel EC2.

![groupe de sécurité](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004120094/3a328a4b-3da6-4012-928e-0cc8a9414b29.png align="center")

Comme le nom du groupe de sécurité de mon EC2 était "launch-wizard-7", je vais cliquer sur cet identifiant de groupe de sécurité.

![Identifiant du groupe de sécurité](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004179202/9919cb9f-a77d-47bd-a47d-52ac51f8a9f2.png align="center")

Cela vous mènera à sa page de configuration. Maintenant, cliquez sur "Modifier les règles entrantes".

![Règles entrantes](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004258702/da5ea5a7-ecdf-4358-8e0b-f428bf61bf85.png align="center")

Ajoutez une nouvelle règle. Le type sera "TCP personnalisé". Le port sera "8000". La source sera "Anywhere-IPv4".

![Modifier les règles entrantes](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004306106/249b91f7-c0fe-4797-80a0-6d059d55f922.png align="center")

Maintenant, enregistrez les règles.

![enregistrer les modifications](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004359517/fbaf4dc7-c608-424b-a890-e8c106971097.png align="center")

Maintenant, allez sur la page EC2 et assurez-vous que le nouvel EC2 est en cours d'exécution.

![Statut EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004404168/0321f546-a40e-4ba6-8815-414547e93346.png align="center")

Si vous souhaitez vous connecter au serveur EC2 depuis votre machine locale, vous devez utiliser la clé `.pem`. Pour cela, vous devez aller dans l'onglet "Client SSH" dans les paramètres de connexion.

![Client SSH](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004603377/99a0a7ac-0d99-433d-bae8-e357cdedd2f2.png align="center")

Pour l'instant, je ne vais pas me donner autant de mal, donc je vais utiliser le navigateur pour me connecter à mon serveur en utilisant le bouton "Connect".

![Connecter EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004526291/a56fe27c-2b7f-400d-94f7-b26dc66ad4a4.png align="center")

Assurez-vous de noter l'adresse IPv4 publique de l'EC2. Maintenant, cliquez sur "Connect".

![Connecter](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004626331/f5b8e5a5-5cef-4137-bbf7-807695b79e67.png align="center")

Cela ouvrira un nouvel onglet avec la connexion EC2 dans votre navigateur.

![Connecter EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004654940/951377a0-7c3d-4e88-bc38-bc73b53da337.png align="center")

Il sera prêt à l'emploi en quelques secondes.

![EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004678704/b1313149-61ed-42d9-9a80-03c7a6f84c32.png align="center")

## Installer Coolify dans AWS EC2

Il existe de nombreuses façons d'installer Coolify directement sur notre EC2. Mais je suis généralement le script d'installation recommandé de [Coolify](https://coolify.io/docs/get-started/installation).

`curl -fsSL` [`https://cdn.coollabs.io/coolify/install.sh`](https://cdn.coollabs.io/coolify/install.sh) `| sudo bash`

Utilisez `sudo zsh` au lieu de `sudo bash` si vous exécutez la commande depuis un terminal "ZSH".

![Script Coolify](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004776360/3f7ca4e5-e819-4c06-bf91-1b4b04edae9a.png align="center")

Il commencera à installer Coolify sur votre serveur. Suivez leurs invites dans le terminal EC2.

![installer coolify dans EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004847716/1994a54b-29ae-44a3-94dd-953c2bc9ffc5.png align="center")

Selon la spécification de votre EC2, cela peut prendre plusieurs minutes. Soyez patient et laissez-le faire son travail jusqu'à ce qu'il atteigne l'écran "Félicitations !".

![fin de l'installation](https://cdn.hashnode.com/res/hashnode/image/upload/v1751004975296/c99da698-0e14-41b3-a32e-761d44edca29.png align="center")

## Accéder à Coolify de n'importe où en utilisant l'IP publique

Après l'installation, ouvrez un nouvel onglet et utilisez cette IP publique avec un port de fin `:8000`. Cela vous mènera à la page d'inscription de Coolify pour la première fois.

![S'inscrire](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005087901/473c8834-e8dd-497e-bb29-ed56e50f9d07.png align="center")

Inscrivez votre compte. Le premier devient l'administrateur par défaut. Mais vous pouvez changer le rôle à tout moment si vous le souhaitez.

Vous pouvez suivre leurs instructions pendant l'intégration. Mais pour l'instant, je vais simplement les ignorer.

![Ignorer l'intégration](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005149629/fb3bcf68-d897-44f4-b210-4896ac630651.png align="center")

Votre Coolify est maintenant complètement prêt à l'emploi !

## Comment déployer un site web via Coolify

Maintenant, je veux vous montrer comment vous pouvez facilement déployer un site web statique directement depuis votre dépôt GitHub dans Coolify.

Allez dans "Projet" et cliquez sur "+Ajouter".

![Ajouter un nouveau projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005414046/2b21ea04-e90c-4f88-b853-81f10142f6b1.png align="center")

Donnez-lui un nom et une description appropriée.

![Nom et description du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005442344/dab216e0-10c9-4a05-8528-bfd662dc3094.png align="center")

Je vais utiliser [l'un de mes dépôts publics](https://github.com/FahimFBA/RainyRoof_Restaurant_Website) depuis GitHub pour cet essai.

![Dépôt GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005496252/a4c01732-3f38-4fa3-b3ba-d40ca3a4feba.png align="center")

Vous pouvez également déployer depuis des dépôts privés. Pour ce faire, sélectionnez "Dépôt privé avec l'application GitHub" ou "Avec une clé de déploiement".

Maintenant, cliquez sur Production.

![Projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005567995/6908baa5-8305-4f3e-a30f-f4adceda5e06.png align="center")

Maintenant, nous devons ajouter une ressource à partir de laquelle il tirera les données.

![Ajouter une nouvelle ressource](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005595787/123b4efe-a664-435a-9b26-88a14b636473.png align="center")

Comme ce dépôt est déjà public, je vais sélectionner "Dépôt public" comme source de mon projet.

![Dépôt public](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005668775/f050c0d5-4c49-499a-895d-b3329c143440.png align="center")

Maintenant, fournissez l'URL du dépôt public dans le champ URL du dépôt. Ensuite, cliquez sur "Vérifier le dépôt".

![URL du dépôt public](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005713819/4923f951-4776-4442-9ced-6774b5ee05c7.png align="center")

Il vous montrera la configuration de base du projet. Vérifiez que tout est correct.

![Configuration du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005789227/ca3fa656-a00c-4ba4-ab07-b892755b0335.png align="center")

Si tout est correct, cliquez sur "Continuer".

Comme il s'agit simplement d'un site web statique, je vais changer le build pack en "Static" et cliquer sur "Continuer".

![Mettre à jour la spécification du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005858468/9b1c5a9c-db49-4648-a53f-c5cfec1d4f6c.png align="center")

Maintenant, déployez l'application en cliquant sur le bouton "Déployer".

![Déployer l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005901660/737fc56a-390b-407a-b41b-fe7f7ce0d986.png align="center")

Vous pouvez activer/désactiver le journal de débogage également.

![Journal de débogage](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005931517/659f4812-2762-4e18-b543-2678a1b3e09b.png align="center")

Une fois le déploiement terminé avec succès, vous pouvez trouver l'URL autogénérée du site web dans l'onglet Liens.

![Lien](https://cdn.hashnode.com/res/hashnode/image/upload/v1751005979512/99b6f561-2d4a-4d24-b6a6-ea025857e909.png align="center")

Le site apparaîtra parfaitement !

![Site en direct](https://cdn.hashnode.com/res/hashnode/image/upload/v1751006003870/eab0135a-0c3d-4e17-bbe8-1a0df996d58e.png align="center")

Vous pouvez également auto-générer un nouveau domaine ou ajouter votre propre domaine/sous-domaine à partir des paramètres du projet à tout moment.

![Changer de domaine](https://cdn.hashnode.com/res/hashnode/image/upload/v1751006064485/3a7c6a99-f2c8-43f8-82a9-b4ef3bbbcfcb.png align="center")

Les paramètres du projet contiendront toutes les autres configurations/variables d'environnement nécessaires, et ainsi de suite. Chaque fois que vous modifiez des informations/paramètres/configuration dans la section de configuration, vous devez simplement redéployer l'application pour refléter les changements.

Vous pouvez ajouter de nouveaux membres à l'équipe, changer le domaine Coolify en autre chose (votre domaine/sous-domaine) et en faire un serveur générique, accessible au public.

![Équipe](https://cdn.hashnode.com/res/hashnode/image/upload/v1751006188731/0d8471f4-7a74-4413-8cc2-81a42da410e9.png align="center")

Donc, voici la procédure générale pour installer Coolify dans une instance AWS EC2 sans aucun tracas.

## Conclusion

Merci d'avoir lu ce court tutoriel. J'espère qu'il vous a aidé à installer Coolify sur votre serveur préféré et à augmenter votre productivité.

Pour obtenir plus de contenu comme celui-ci, vous pouvez me suivre sur [GitHub](https://github.com/FahimFBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [YouTube](https://youtube.com/@FahimAmin). Mon [site web](https://www.fahimbinamin.com/) est toujours disponible également.