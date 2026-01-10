---
title: Comment fonctionne Kerberos ? Le protocole d'authentification expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-19T14:34:59.000Z'
originalURL: https://freecodecamp.org/news/how-does-kerberos-work-authentication-protocol
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/cerberus.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: cybersecurity
  slug: cybersecurity
seo_title: Comment fonctionne Kerberos ? Le protocole d'authentification expliqué
seo_desc: "By Aaron Katz\nIn this article, we will learn what Kerberos is, how it\
  \ works, and the various pros and cons of using this authentication protocol.  \n\
  What is Kerberos?\nHave you ever wondered what happens when you type in your username\
  \ and password at w..."
---

Par Aaron Katz

Dans cet article, nous allons apprendre ce qu'est Kerberos, comment il fonctionne, et les divers avantages et inconvénients de l'utilisation de ce protocole d'authentification.  

## Qu'est-ce que Kerberos ?

Vous êtes-vous déjà demandé ce qui se passe lorsque vous tapez votre nom d'utilisateur et votre mot de passe au travail, et que vous avez magiquement accès aux serveurs de fichiers, aux serveurs de messagerie et à d'autres ressources ? Il y a de fortes chances que vous utilisiez Kerberos ! 

Kerberos a été conçu pour protéger vos identifiants des pirates en gardant les mots de passe hors des réseaux non sécurisés, même lors de la vérification des identités des utilisateurs.

Kerberos, dans sa forme la plus simple, est un protocole d'authentification pour les applications client/serveur. Il est conçu pour fournir une authentification sécurisée sur un réseau non sécurisé. 

Le protocole a été initialement développé par le MIT dans les années 1980 et a été nommé d'après le chien mythique à trois têtes qui gardait les enfers, Cerbère. Il a ensuite été perfectionné par Microsoft pour être inclus dans Windows 2000 afin de remplacer [NTLM](https://docs.microsoft.com/en-us/windows/win32/secauthn/microsoft-ntlm) – et le protocole reste [Open Source](https://www.kerberos.org/about/FAQ.html).

Si vous devez résumer rapidement Kerberos vs NTLM lors d'un entretien, la description la plus concise est la suivante :

> "Alors que NTLM utilise une poignée de main en trois étapes entre le client et le serveur, où les identifiants sont envoyés entre les systèmes, Kerberos évite d'envoyer des identifiants sur le réseau."

## Authentification avec Kerberos

L'authentification via Kerberos nécessite l'utilisation d'un **Centre de Distribution de Clés (KDC)**. Il s'agit généralement d'un service exécuté sur tous les contrôleurs de domaine (DC) dans le cadre des services de domaine Active Directory (AD DS). Il contient les composants suivants :

1. **Service d'authentification (AS)** : Authentifie les utilisateurs lorsqu'ils tentent initialement d'accéder à un service
2. **Service de délivrance de tickets (TGS)** : Connecte un utilisateur avec le serveur de service (par exemple, un serveur de fichiers) en fonction des informations stockées dans la base de données
3. **Base de données Kerberos** : Où les identifiants et les mots de passe sont stockés, souvent un serveur LDAP ou la base de données Security Account Manager (SAM) dans un environnement Active Directory.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-193.png)
_Flux de travail d'authentification Kerberos_

### Processus d'authentification Kerberos expliqué

Lorsque un utilisateur demande l'accès à un service via le service d'authentification, il entre son nom d'utilisateur et son mot de passe localement, et envoie les informations suivantes :

1. Identifiant de sécurité (SID)
2. Nom du service demandé (par exemple, example.cool.hat)
3. Adresse IP de l'utilisateur
4. Durée de vie souhaitée du ticket de délivrance de tickets (TGT). La valeur par défaut est de 10 heures et peut être modifiée via la stratégie de groupe

Le service d'authentification délivre un ticket de délivrance de tickets (TGT) si l'utilisateur existe dans la base de données. Le premier message envoyé à l'utilisateur contient :

1. Identifiant de sécurité (SID)
2. ID du TGS
3. Horodatage
4. Adresse IP de l'utilisateur
5. Durée de vie du TGT
6. TGT
7. Clé de session

Après ce message, un autre message sera envoyé contenant :

1. ID du TGS
2. Horodatage
3. Clé de session

L'utilisateur envoie le TGT au TGS avec l'ID Kerberos des services demandés. Un autre message est envoyé contenant l'"Authentificateur", qui est composé de l'ID de l'utilisateur et de l'horodatage, chiffré avec la clé de session de l'utilisateur.

Le TGS répondra à l'utilisateur avec deux messages s'il trouve les informations de l'utilisateur dans la base de données Kerberos. Le premier message contiendra les informations suivantes, chiffrées avec la clé de service secrète du serveur :

1. Ticket de service
2. ID de l'utilisateur
3. Adresse IP de l'utilisateur
4. Période de validité
5. Clé de session de service

Un deuxième message, chiffré avec la clé de session de l'utilisateur (par exemple une boîte verrouillée dans une boîte verrouillée, où l'utilisateur ne peut déverrouiller que la première boîte), contiendra la clé de session de service.

L'utilisateur envoie le ticket de service au service demandé avec la demande de service en deux messages. Le premier message sera le premier message de l'étape précédente (chiffré avec la clé de service secrète du serveur). Le deuxième message contiendra un nouvel Authentificateur avec un horodatage mis à jour, chiffré avec la clé de session de l'utilisateur.

Le serveur de service déchiffre le ticket à l'aide de sa propre clé secrète pour récupérer la clé de session de l'utilisateur, qui est utilisée pour déchiffrer l'authentificateur. Si l'ID de l'utilisateur des messages précédents correspond, il enverra un message chiffré avec la clé de session de l'utilisateur à l'utilisateur avec l'horodatage trouvé dans le nouvel authentificateur pour confirmer l'identité du service.

### Chiffrement Kerberos

Lors de la création d'un nouveau compte sur un contrôleur de domaine Active Directory, vous obtenez un nom d'utilisateur et un mot de passe. 

Le client Kerberos ajoute ensuite une chaîne connue sous le nom de sel - une chaîne unique utilisée pour améliorer l'aléatoire d'un identifiant - ainsi que le numéro de version de Kerberos. Dans la plupart des configurations, le sel est le nom d'utilisateur de l'utilisateur. Il exécute ensuite ces deux valeurs via une fonction string2Key qui retournera le secret partagé.

Sur une station de travail, l'utilisateur demandera l'accès à un service (tel que la connexion à la machine) en fournissant son nom d'utilisateur et son mot de passe. Le client Kerberos local effectuera les mêmes étapes que le DC pour arriver à un secret partagé. Si ce secret correspond au secret stocké sur le DC, l'utilisateur peut se connecter.

## Avantages de Kerberos

Kerberos offre plusieurs avantages par rapport aux technologies d'authentification précédentes, telles que :

* Les mots de passe en clair ne sont jamais envoyés au KDC
* Transparence et audit simples de tous les événements
* La vérification auprès du KDC ne se fait qu'une seule fois pour la durée de vie du ticket
* L'authentification unique est l'un des plus grands avantages directs de Kerberos, permettant à un utilisateur d'entrer ses identifiants une fois, et de continuer à renouveler son ticket sans intervention
* Prise en charge de l'authentification multifactorielle (MFA)
* Les deux extrémités de la chaîne de communication doivent être authentifiées

## Vulnérabilités de sécurité de Kerberos 

Maintenant que nous savons comment fonctionne Kerberos, il est important de comprendre les vulnérabilités potentielles inhérentes à sa mise en œuvre, en particulier dans l'extension propriétaire de Microsoft à Kerberos. 

Vous pouvez détecter la majorité de ces attaques en utilisant des outils natifs pour surveiller les journaux, mais il est important de savoir quoi rechercher. Cette section fournira un aperçu de haut niveau des diverses attaques que vous trouverez contre les systèmes Kerberos.

### Attaque par Golden Ticket

Un Golden Ticket est un centre de distribution de clés Kerberos falsifié. Vous pouvez créer des tickets Kerberos utilisables pour des comptes qui n'existent pas dans l'Active Directory. 

Pour obtenir un Golden Ticket, un attaquant a besoin d'un accès administrateur de domaine/local sur la forêt ou le domaine Active Directory – et une fois le ticket créé, il est valable pour 10 ans par défaut !

Si vous pensez que quelqu'un a créé un Golden Ticket non autorisé, vous devrez réinitialiser le compte de service Kerberos, krbtgt. Bien que cela ne soit pas difficile, il y a plusieurs étapes critiques dans le processus. 

Parce qu'Active Directory stocke les anciens et les mots de passe actuels pour tous les comptes, vous devez réinitialiser le compte krbtgt deux fois. Mais la deuxième réinitialisation doit avoir lieu **uniquement après avoir attendu la durée de vie maximale du ticket utilisateur** après la première réinitialisation du mot de passe. Microsoft fournit un script pratique pour aider à cela [ici](https://gallery.technet.microsoft.com/Reset-the-krbtgt-account-581a9e51).

### Attaque par Silver Ticket

Un Silver Ticket est similaire à un Golden Ticket, mais n'a pas les privilèges administratifs étendus du Golden Ticket. 

Un attaquant obtiendrait généralement l'accès à un seul service sur une application, et un attaquant doit avoir compromis des identifiants d'utilisateur légitimes à partir du SAM d'un ordinateur ou d'un compte de service local. 

Ce qui rend ces attaques très difficiles à détecter, c'est que la falsification d'un Silver Ticket (par exemple en utilisant le hachage du mot de passe du compte de service) ne nécessite aucune communication avec un DC.

### Attaque par malware de clé squelette de porte dérobée

Dans une attaque par malware de clé squelette de porte dérobée, l'attaquant a généralement compromis le contrôleur de domaine et exécuté une attaque par Golden Ticket réussie. 

Le malware injecte dans LSASS un mot de passe maître qui fonctionnerait contre n'importe quel compte dans le domaine. Lorsque le compte s'authentifie, le malware vérifie le hachage du mot de passe maître injecté, et s'il correspond, authentifie l'utilisateur, indépendamment du vrai mot de passe de l'utilisateur. Les utilisateurs légitimes pourront toujours se connecter avec leurs identifiants normaux.

### Attaque par transmission de hachage

Il s'agit d'une technique où un attaquant obtient le hachage du mot de passe NTLM d'un utilisateur, et transmet ensuite le hachage pour des fins d'authentification NTLM. 

Cela fonctionne parce que les systèmes ne valident pas réellement le mot de passe d'un utilisateur, mais plutôt le hachage du mot de passe. Cette attaque ne fonctionne que contre les connexions interactives utilisant l'authentification NTLM.

### Attaque par transmission de ticket

Dans cette attaque, l'acteur de la menace crée une fausse clé de session en falsifiant un faux TGT. L'attaquant présentera cela au service comme un identifiant valide. 

Pour exécuter cette attaque, l'attaquant doit obtenir l'accès à la clé de session. Pour effectuer cette attaque, un attaquant obtiendrait des tickets Kerberos de la mémoire du processus LSASS, puis injecterait le TGT volé dans sa propre session, ce qui lui permettrait d'adopter l'identité et les privilèges du TGT volé.

### Attaque par dépassement de hachage

Une combinaison de transmission de hachage et de transmission de ticket, un attaquant utilise un hachage compromis pour obtenir un ticket Kerberos qu'il peut utiliser pour accéder à une ressource. 

Souvent utile si vous avez besoin d'une authentification Kerberos si NTLM est désactivé pour atteindre votre cible mais que vous n'avez qu'un hachage compromis.

### Kerberoasting

Lorsque un compte de domaine est configuré pour exécuter un service (par exemple, Internet Information Systems, MSSQL, etc.), un Service Principal Name est utilisé pour associer le service à un compte de connexion. 

Si un utilisateur souhaite accéder à la ressource, il reçoit un ticket Kerberos signé avec le hachage du mot de passe NTLM du compte exécutant le service. Les pirates peuvent ensuite craquer ce hachage hors ligne et l'utiliser pour obtenir un accès. 

_Tout utilisateur sur le domaine avec un TGT valide peut demander un TGS pour tout service avec un SPN_ - aucun identifiant ou accès fantaisiste nécessaire ! Notez qu'il _n'y a pas de correctif ou de patch_ au-delà de s'assurer que le mot de passe des comptes de service est suffisamment complexe.

Pour détecter cette attaque, votre _seule_ option native est de surveiller l'ID d'événement 4769, et de rechercher un type de chiffrement de ticket de 0x17 - réponse krb_tgt_reply de l'utilisateur à l'utilisateur. Vous pouvez trouver plus d'informations sur la détection des attaques Kerberoast [ici](https://www.trustedsec.com/blog/art_of_kerberoast/).

### Attaque par relecture

Une attaque par relecture se produit si un attaquant vole le paquet envoyé de l'utilisateur au service, qu'il peut ensuite utiliser pour accéder au service sans connaître les identifiants de l'utilisateur. 

Cela est généralement à faible risque et est atténué par le système vérifiant l'horodatage du paquet - tout horodatage antérieur ou identique à un paquet précédent est rejeté, ainsi que tout horodatage non synchronisé avec l'heure du serveur de plus de 5 minutes.

## Comment se défendre contre les attaques sur Kerberos

Maintenant que nous sommes bien conscients des attaques que nous venons de discuter, plongeons dans quelques techniques pour nous défendre contre les attaques sur notre infrastructure Kerberos.

### Journalisation et surveillance

Les attaquants utilisent souvent un compte ou un nom de domaine faux ou vide lors de l'émission d'un Golden Ticket, car ceux-ci n'ont pas besoin d'être réels lors de l'émission d'un ticket valide. 

Vous pouvez rechercher dans les journaux du DC l'ID d'événement **4769** - demande de ticket de service, pour les utilisateurs ou domaines qui n'existent pas. Pour les attaques par Silver Ticket, vous voudrez rechercher l'ID d'événement **4769** pour toute demande de ticket de service utilisant le chiffrement RC4, le type étant défini sur 0x17.

### Appliquez les correctifs !

Assurez-vous que vos systèmes sont à jour. Non seulement cela aidera à empêcher de nombreux outils d'exploitation de fonctionner, mais spécifiquement, le correctif [CVE-2014-6324](https://www.varonis.com/blog/microsoft-fixes-kerberos-silver-ticket-vulnerability/) résoudra une vulnérabilité permettant à un Silver Ticket de devenir un administrateur de domaine.

### Définissez les comptes admin et de service sur "Sensible et ne peut pas être délégué"

Ce paramètre empêchera les attaquants de déléguer leurs comptes piratés à d'autres services ou ordinateurs, limitant leur capacité à se déplacer latéralement dans votre environnement.

### Ne pas ajouter de comptes d'ordinateur aux groupes d'administrateurs

Un compte d'ordinateur qui est membre de groupes d'administrateurs, tels que "AD Backups", peut être exploité pour obtenir des Silver Tickets et permettre aux attaquants de maintenir la persistance dans Active Directory en ajoutant de nouveaux droits au compte.

### Exécuter le service de sous-système d'autorité de sécurité locale (LSASS) en mode protégé

LSASS est responsable de la fourniture du service d'authentification unique pour les utilisateurs, et héberge de nombreux plugins tels que l'authentification NTLM et Kerberos. 

Les identifiants sont présentés à chacun de ces plugins, produisant un hachage unidirectionnel et des tickets dans l'espace mémoire de LSASS, qui reste pour la durée de la session de l'utilisateur.

Lorsqu'il est exécuté en tant que [processus protégé](https://itm4n.github.io/lsass-runasppl/), LSASS ne peut être accessible que par des binaires signés numériquement (dont la plupart des outils d'attaque ne le sont pas, bien qu'il existe quelques méthodes de contournement disponibles).

Cela peut être défini en ouvrant l'Éditeur du Registre en tant qu'administrateur, et en ajoutant un DWORD avec le nom **RunAsPPL** avec une valeur de **1** à _HKLM\SYSTEM\CurrentControlSet\Control\LSA_ et en redémarrant le système.

**IMPORTANT :** Si vous utilisez un _module d'authentification tiers_, il doit répondre aux exigences énumérées ici : [Configuring Additional LSA Protection | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection#protected-process-requirements-for-plug-ins-or-drivers). 

Si vous utilisez _Secure Boot/UEFI_, vous ne pouvez pas désactiver le paramètre en modifiant la clé de registre, et vous devez suivre les instructions spécifiques décrites par Microsoft ici : [Configuring Additional LSA Protection | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection#to-disable-lsa-protection).

### Imposer l'authentification par certificat d'attribut privilégié (PAC) pour TGS

Le certificat d'attribut privilégié contient des informations sur les privilèges d'un utilisateur. Un PAC falsifié peut instruire le TGS d'accorder des privilèges supplémentaires à un utilisateur auxquels il n'a pas droit - et parce que dans la mise en œuvre de Microsoft, le compte krbtgt est désactivé et non utilisé, la clé ne change pas. 

Lorsqu'elle est activée, la validation PAC garantit que le PAC d'une authentification utilisateur à un système est vérifié auprès d'Active Directory pour sa validité. Vous pouvez activer cela en ouvrant l'Éditeur du Registre (**regedit.exe**) en tant qu'administrateur, et en définissant la clé _HKLM\System\CurrentControlSet\Control\LSAKerberosParameters_ à **1**.

### Principe du moindre privilège

Assurez-vous que les comptes utilisateurs dans tout l'environnement n'ont accès qu'aux services, groupes et ressources dont ils ont besoin pour remplir leur fonction. Cela réduit la surface d'attaque et peut aider à prévenir une compromission supplémentaire en cas de compromission d'un compte.

### Utiliser des mots de passe forts et uniques pour les comptes administratifs, locaux et de service

Les comptes administratifs devraient idéalement avoir des mots de passe de plus de 14 caractères. Cependant, les comptes SPN devraient idéalement avoir des mots de passe plus longs pour améliorer la sécurité - idéalement 25 caractères ou plus.  

Les SPN basés sur l'hôte ont des mots de passe sécurisés de 128 caractères changés tous les 30 jours, mais par défaut, les SPN de compte utilisateur n'expirent souvent jamais et ont des mots de passe réutilisés et faibles, car cela simplifie l'administration.

### Activer Windows Defender Credential Guard (sauf sur les contrôleurs de domaine)

Windows Defender Credential Guard empêche les attaques telles que Pass the hash ou Pass the ticket en protégeant les hachages NTLM, les TGT et autres identifiants. Il le fait en tirant parti de la sécurité basée sur la virtualisation et du processus "LSA isolé" pour stocker et protéger les secrets. 

Seules les applications et processus privilégiés et de confiance pourront accéder à ces informations. Vous pouvez trouver plus d'informations ici : [Windows 10 Device Guard and Credential Guard Demystified - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/iis-support-blog/windows-10-device-guard-and-credential-guard-demystified/ba-p/376419).

### Désactiver le chiffrement RC4

RC4-HMAC est une suite de chiffrement connue comme non sécurisée et vous devriez la désactiver si possible.

* Activer la prise en charge AES dans les relations de confiance de domaine où des relations de confiance existent
* Imposer AES256 pour le compte Azure AD SSO si applicable
* Faire tourner la clé de déchiffrement Kerberos
* Désactiver RC4-HMAC via la stratégie de groupe

**IMPORTANT :** Il existe de nombreux "pièges" lors de la désactivation de RC4 en raison de la manière dont Windows s'authentifie et des nombreux endroits où ce paramètre devra être modifié. Assurez-vous de rechercher et de planifier _minutieusement_ avant d'appliquer. 

Voici quelques documents utiles pour vous aider :

* [Tough Questions Answered: Can I disable RC4 Etype for Kerberos on Windows 10 ?](https://techcommunity.microsoft.com/t5/itops-talk-blog/tough-questions-answered-can-i-disable-rc4-etype-for-kerberos-on/ba-p/382718)
* [Lessons in Disabling RC4 in Active Directory](https://syfuhs.net/lessons-in-disabling-rc4-in-active-directory)

## Conclusion

Vous voyez, ce n'était pas si mal - Kerberos peut être amusant ! Kerberos est souvent l'un des composants les moins considérés, mais les plus critiques de tout réseau d'entreprise. Et il est impératif que les défenseurs comprennent comment ce protocole fonctionne, et les diverses attaques et défenses disponibles. Maintenant, allez de l'avant et conquérez !

## Lectures complémentaires

* [Kerberos, Active Directorys Secret Decoder Ring  Active Directory Security](https://adsecurity.org/?p=227)
* [The Kerberos Protocol Explained | Identity & Access Management](https://iam.uconn.edu/the-kerberos-protocol-explained/)
* [Kerberos Authentication 101: Understanding the Essentials of the Kerberos Security Protocol -- Redmondmag.com](https://redmondmag.com/articles/2012/02/01/understanding-the-essentials-of-the-kerberos-protocol.aspx#:~:text=The%20SALT%20string%20is%20the,secret%20key%20on%20the%20client.&text=The%20user%20and%20the%20Authentication,communicate%20using%20the%20shared%20secret.)