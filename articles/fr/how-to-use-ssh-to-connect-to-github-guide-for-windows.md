---
title: 'Comment utiliser SSH pour se connecter en toute sécurité à GitHub : un guide
  simple pour Windows'
subtitle: ''
author: Oghenekparobo Stephen
co_authors: []
series: null
date: '2024-09-27T14:33:54.735Z'
originalURL: https://freecodecamp.org/news/how-to-use-ssh-to-connect-to-github-guide-for-windows
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727226065318/c1522ad1-df49-4bc9-aa31-567d4012585a.avif
tags:
- name: ssh
  slug: ssh
- name: networking
  slug: networking
- name: Beginner Developers
  slug: beginners
- name: Programming Blogs
  slug: programming-blogs
- name: programming
  slug: programming-ciovqvfcb008mb253jrczo9ye
- name: coding
  slug: coding
- name: learning
  slug: learning
seo_title: 'Comment utiliser SSH pour se connecter en toute sécurité à GitHub : un
  guide simple pour Windows'
seo_desc: 'In this article, we will explore the Secure Shell (SSH) protocol, a vital
  tool for securing network communications.

  SSH is widely used for accessing remote servers and managing code repositories securely,
  particularly in environments like GitHub. You...'
---

Dans cet article, nous allons explorer le protocole Secure Shell (SSH), un outil essentiel pour sécuriser les communications réseau.

SSH est largement utilisé pour accéder à des serveurs distants et gérer des dépôts de code en toute sécurité, particulièrement dans des environnements comme GitHub. Vous découvrirez les concepts fondamentaux de SSH, son fonctionnement et les étapes pratiques pour le configurer sous Windows. Nous couvrirons tout, de la génération des clés SSH au test de votre connexion et au clonage de dépôts.

D'ici la fin de ce guide, vous aurez une solide compréhension de SSH et serez équipé pour améliorer votre flux de travail grâce à des connexions sécurisées.

### Ce que nous allons couvrir :

1. [Qu'est-ce que SSH ?](#heading-quest-ce-que-ssh)
    
2. [Comment fonctionne le protocole Secure Shell ?](#heading-comment-fonctionne-le-protocole-secure-shell)
    

* [TCP/IP](#heading-tcpip)
    
* [Le processus de connexion SSH](#heading-le-processus-de-connexion-ssh)
    

3. [Comment utiliser SSH sous Windows](#heading-comment-utiliser-ssh-sous-windows)
    

* [Windows PowerShell ou l'invite de commande](#heading-windows-powershell-ou-linvite-de-commande)
    
* [Windows Subsystem for Linux (WSL)](#heading-windows-subsystem-for-linux-wsl)
    
* [Clients SSH tiers (par exemple, PuTTY)](#heading-clients-ssh-tiers-par-exemple-putty)
    

4. [Comment utiliser SSH sous Windows pour se connecter à GitHub](#heading-comment-utiliser-ssh-sous-windows-pour-se-connecter-a-github)
    

* [Installer via les fonctionnalités facultatives de Windows](#heading-installer-via-les-fonctionnalites-facultatives-de-windows)
    
* [Télécharger et installer depuis GitHub](#heading-telecharger-et-installer-depuis-github)
    
* [Comment générer des clés SSH](#heading-comment-generer-des-cles-ssh)
    
* [Comment ajouter la clé publique à GitHub](#heading-comment-ajouter-la-cle-publique-a-github)
    
* [Tester la connexion SSH](#heading-tester-la-connexion-ssh)
    
* [Cloner un dépôt à l'aide de SSH](#heading-cloner-un-depot-a-laide-de-ssh)
    

5. [Conclusion](#heading-conclusion)
    

### Prérequis

Avant de commencer ce tutoriel, assurez-vous de disposer des éléments suivants :

* **Compréhension de base de la ligne de commande** : Vous devez être familier avec l'utilisation de l'interface de ligne de commande (CLI) sous Windows, y compris la manière d'ouvrir PowerShell ou l'invite de commande.
    
* **Système d'exploitation Windows** : Ce tutoriel est spécifiquement conçu pour les utilisateurs exécutant Windows 10 ou des versions ultérieures.
    
* **Client OpenSSH installé** : Assurez-vous que le client OpenSSH est installé sur votre système. Vous pouvez le vérifier en tapant `ssh` dans votre interface de ligne de commande.
    
* **Compte GitHub** : Vous aurez besoin d'un compte GitHub pour tester les connexions SSH et gérer les dépôts.
    
* **Éditeur de texte** : Vous aurez également besoin d'un éditeur de code (comme Visual Studio Code, Notepad++ ou similaire) pour modifier les fichiers de configuration si nécessaire.
    

# Qu'est-ce que SSH ?

**SSH** signifie Secure Shell (protocole). Le protocole Secure Shell est un protocole réseau cryptographique permettant d'exploiter des services réseau de manière sécurisée sur un réseau non sécurisé.

En termes plus simples, **SSH** est un moyen d'utiliser des services en toute sécurité sur un réseau, comme accéder à un ordinateur distant, même lorsque le réseau lui-même n'est pas totalement sûr. Il protège vos données et vos communications en brouillant (chiffrant) tout, afin que personne ne puisse les espionner ou les falsifier, même s'ils les interceptent.

C'est particulièrement utile lors de la connexion à des services comme GitHub, où vous souhaitez gérer du code en toute sécurité sur un serveur distant.

### Comment fonctionne le protocole Secure Shell ?

SSH repose sur l'ensemble de règles [TCP/IP](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/) que les ordinateurs utilisent pour communiquer sur Internet.

### TCP/IP

**TCP** signifie **Transmission Control Protocol**. C'est l'un des protocoles de base de la **suite TCP/IP**, utilisé pour envoyer des données sur Internet. **IP** signifie **Internet Protocol**. Il fait également partie de l'ensemble de règles TCP/IP, et son rôle est de guider les paquets de données vers la bonne destination sur Internet.

Vous pouvez en savoir plus sur le protocole TCP/IP [ici](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) si vous souhaitez approfondir le sujet.

### Le processus de connexion SSH

Le **protocole Secure Shell** fonctionne en établissant une connexion sécurisée entre un client (votre machine locale) et un serveur distant.

Tout d'abord, le client initie la connexion en spécifiant l'adresse du serveur (IP ou domaine) et les identifiants de connexion. Pendant la phase d'authentification, le serveur vérifie l'identité du client, généralement à l'aide d'un mot de passe ou, plus sûrement, de clés SSH. Il s'agit d'une paire composée d'une clé privée stockée sur le client et d'une clé publique sur le serveur.

Une fois authentifié, SSH chiffre toutes les données transférées entre le client et le serveur, garantissant la confidentialité et l'intégrité. Ce canal sécurisé permet au client d'exécuter des commandes, de transférer des fichiers et de gérer le serveur à distance comme s'il était physiquement présent, tout en protégeant les données contre toute interception ou falsification potentielle.

L'**IP** est responsable de l'adressage et du routage de la demande de connexion initiale du client vers le serveur. Elle garantit que la demande, qui inclut l'adresse du serveur, est envoyée à la bonne destination.

Une fois que la demande de connexion SSH atteint le serveur, le **TCP** établit un canal de communication fiable. Il gère la transmission des données entre le client et le serveur, en s'assurant que tous les paquets sont livrés avec précision et dans le bon ordre.

Pendant la session SSH, le **TCP** s'assure que les [paquets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) de données sont correctement transmis et réassemblés, tandis que l'**IP** gère l'adressage. SSH utilise ensuite ce canal sécurisé et fiable pour authentifier le client, chiffrer toutes les données transférées et maintenir une connexion sécurisée. Cela permet la gestion à distance et le transfert de fichiers avec confidentialité et intégrité.

## Comment utiliser SSH sous Windows

Windows propose plusieurs façons d'utiliser SSH :

### **Windows PowerShell ou l'invite de commande**

Windows est livré avec un client OpenSSH intégré. Vous pouvez y accéder en ouvrant PowerShell ou l'invite de commande et en tapant `ssh`. Cette méthode est simple et ne nécessite aucun logiciel supplémentaire.

### **Windows Subsystem for Linux (WSL)**

Vous pouvez activer le Windows Subsystem for Linux pour exécuter une distribution Linux directement sur votre PC Windows. De nombreuses distributions Linux sont livrées avec OpenSSH pré-installé, vous permettant d'utiliser les commandes `ssh` depuis le terminal Linux. Cette méthode est idéale si vous préférez un environnement de type Linux.

### **Clients SSH tiers (par exemple, PuTTY)**

Si vous préférez une application autonome, des outils comme PuTTY offrent une interface graphique pour gérer les connexions SSH. PuTTY est largement utilisé pour se connecter à des serveurs et prend en charge des options avancées comme l'enregistrement de profils de connexion.

Windows 10 et les versions ultérieures sont livrés avec un client OpenSSH natif, qui vous permet de vous connecter en toute sécurité à des systèmes distants via une connexion SSH (Secure Shell).

## Comment utiliser SSH sous Windows pour se connecter à GitHub

Si vous utilisez Windows 10 ou une version ultérieure, vous pouvez profiter des fonctionnalités SSH intégrées.

Pour commencer, ouvrez votre terminal Windows ou PowerShell, de préférence en tant qu'administrateur. Dans l'interface de ligne de commande, vous pouvez vérifier si SSH est installé en tapant la commande `ssh`. Cela confirmera si le client SSH est disponible sur votre système.

![résultat de la commande cli ssh, dans ce cas un résultat positif indiquant que ssh est installé sur le système](https://cdn.hashnode.com/res/hashnode/image/upload/v1727215416889/9985624e-ffe6-4aff-9e58-2fe3e6b36f26.png align="center")

Si vous obtenez l'image ci-dessus, cela signifie que SSH est disponible sur votre système local.

La première chose dont vous aurez besoin pour configurer une connexion SSH est une paire de clés SSH – une clé publique et une clé privée. Celles-ci se trouvent généralement dans le répertoire `.ssh` de votre dossier personnel si elles ont déjà été générées.

Sous Windows, votre répertoire personnel est généralement `C:\Users\proprietaire\.ssh`. C'est là que vous trouverez vos fichiers de clés SSH s'ils ont déjà été générés.

You pouvez facilement installer OpenSSH sur votre système Windows. Il existe plusieurs façons de procéder :

### Installer via les fonctionnalités facultatives de Windows

1. Ouvrez le menu Démarrer de Windows et tapez "fonctionnalités facultatives" dans la barre de recherche.
    
2. Cliquez sur "Ajouter ou supprimer des fonctionnalités facultatives de Windows" pour ouvrir la fenêtre des fonctionnalités facultatives.
    
3. Dans la fenêtre des fonctionnalités facultatives, faites défiler vers le bas et trouvez l'option "Client OpenSSH".
    
4. Cochez la case correspondante et cliquez sur le bouton "Installer" en bas pour installer le client OpenSSH.
    

### Télécharger et installer depuis GitHub

1. Visitez le dépôt GitHub pour la version Win32-OpenSSH (32 bits) ou Win64-OpenSSH (64 bits), selon votre version de Windows :
    
    * 32 bits : [https://github.com/PowerShell/Win32-OpenShell/releases](https://github.com/PowerShell/Win32-OpenShell/releases)
        
    * 64 bits : [https://github.com/PowerShell/Win64-OpenShell/releases](https://github.com/PowerShell/Win64-OpenShell/releases)
        
2. Téléchargez le dernier fichier d'installation .msi correspondant à l'architecture de votre Windows.
    
3. Exécutez l'installeur .msi pour installer le client OpenSSH sur votre système.
    

Après avoir installé OpenSSH, vous pouvez maintenant générer des clés SSH en ouvrant le terminal Windows ou PowerShell et en exécutant la commande `ssh-keygen`. Cela vous guidera tout au long du processus de création d'une nouvelle paire de clés publique-privée que vous pourrez utiliser pour authentifier vos connexions SSH, par exemple vers votre compte GitHub.

La clé publique peut ensuite être ajoutée aux paramètres de votre compte GitHub, vous permettant de vous connecter à vos dépôts en utilisant le protocole SSH au lieu de HTTPS. N'oubliez pas de garder votre clé privée en sécurité, car elle donne accès à votre compte GitHub.

En installant OpenSSH, vous avez mis en place la base nécessaire pour travailler avec les clés SSH et établir des connexions sécurisées vers des systèmes distants et des services comme GitHub.

Vous pouvez maintenant vérifier si le serveur OpenSSH est en cours d'exécution en accédant à l'utilitaire Services de Windows. Pour ce faire, appuyez sur la touche Windows + R pour ouvrir la boîte de dialogue Exécuter, puis saisissez "services.msc" et appuyez sur Entrée. Cela ouvrira le gestionnaire de services.

![une invite windows, générée en cliquant sur "windows + r"](https://cdn.hashnode.com/res/hashnode/image/upload/v1727217366905/348ece20-432c-443e-951c-5c61ae4c7b94.png align="center")

Le gestionnaire de services :

![Le gestionnaire de services généré après avoir cliqué sur "windows + r"](https://cdn.hashnode.com/res/hashnode/image/upload/v1727217489636/dffca024-3cb2-4b2b-8a03-fb4a2b5cc629.png align="center")

Faites défiler et cherchez le serveur OpenSSH SSH :

![cette image indique que le serveur openSSH est en cours d'exécution dans le système, automatiquement dès que le système est sous tension](https://cdn.hashnode.com/res/hashnode/image/upload/v1727217823859/accbf838-e6cb-491a-ad1a-affa0dd59230.png align="center")

Si le service Serveur OpenSSH est en cours d'exécution dans la fenêtre Services, cela signifie que le composant serveur OpenSSH est correctement configuré sur votre système Windows. C'est une première étape importante pour activer les connexions SSH sécurisées.

Pour vous assurer que le serveur OpenSSH démarre automatiquement à chaque fois que votre PC est allumé, vous pouvez configurer davantage le type de démarrage du service. Dans la fenêtre Services, faites un clic droit sur le service "OpenSSH Server" et sélectionnez "Propriétés".

Dans les propriétés du service, cherchez le menu déroulant "Type de démarrage" et sélectionnez "Automatique". Cela garantira que le service Serveur OpenSSH démarre automatiquement dès que votre ordinateur est sous tension, au lieu de vous obliger à le démarrer manuellement à chaque fois.

En configurant le service Serveur OpenSSH pour qu'il démarre automatiquement, vous pouvez être certain que le serveur sera prêt à accepter les connexions SSH entrantes à tout moment, sans avoir besoin de vous rappeler de le démarrer manuellement. Cela simplifie le processus d'utilisation de l'authentification basée sur SSH et de l'accès à distance sur votre machine Windows.

N'oubliez pas que le fait d'avoir le service Serveur OpenSSH en cours d'exécution et configuré pour démarrer automatiquement n'est que la première étape. Vous devrez encore générer des clés SSH et configurer votre compte GitHub (ou d'autres services) pour utiliser la clé publique pour l'authentification. Mais cette configuration initiale du serveur OpenSSH pose les bases d'une utilisation fluide de SSH à l'avenir.

![ouverture de l'openSSH sur le gestionnaire de services](https://cdn.hashnode.com/res/hashnode/image/upload/v1727218121688/a902b304-8103-49a5-8852-7094b4f70d5a.png align="center")

Maintenant que vous avez confirmé que le serveur OpenSSH fonctionne sur votre système Windows, l'étape suivante consiste à s'assurer qu'il peut communiquer à travers le Pare-feu Windows. Le moyen le plus simple d'y parvenir est d'utiliser une commande PowerShell.

Ouvrez PowerShell en tant qu'administrateur et exécutez la commande suivante :

```plaintext
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH SSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22 -Program "C:\Program Files\OpenSSH\sshd.exe"
```

Cette commande PowerShell créera une nouvelle règle de pare-feu qui autorise le trafic TCP entrant sur le port 22 (le port SSH par défaut) pour l'exécutable du serveur OpenSSH situé à "C:\\Program Files\\OpenSSH\\sshd.exe".

Voici le détail des différents paramètres utilisés dans la commande :

* `-Name sshd` : Assigne le nom "sshd" à la nouvelle règle de pare-feu.
    
* `-DisplayName 'OpenSSH SSH Server'` : Fournit un nom d'affichage descriptif pour la règle.
    
* `-Enabled True` : Garantit que la règle est active et activée.
    
* `-Direction Inbound` : Spécifie que la règle s'applique au trafic réseau entrant.
    
* `-Protocol TCP` : Configure la règle pour autoriser les connexions de protocole TCP.
    
* `-Action Allow` : Indique au pare-feu d'autoriser le trafic spécifié.
    
* `-LocalPort 22` : Définit le port local sur 22, qui est le port SSH par défaut.
    
* `-Program "C:\Program Files\OpenSSH\sshd.exe"` : Identifie le programme spécifique (l'exécutable du serveur OpenSSH) auquel la règle doit s'appliquer.
    

En exécutant cette commande PowerShell, vous créez une règle de pare-feu dédiée qui permet au serveur OpenSSH de communiquer à travers le Pare-feu Windows, vous permettant d'établir des connexions SSH sécurisées vers votre système.

N'oubliez pas qu'il est toujours judicieux de revoir périodiquement vos paramètres de pare-feu, surtout si vous modifiez votre configuration réseau ou si vous souhaitez affiner davantage l'accès au serveur OpenSSH.

Si l'opération réussit, vous devriez obtenir ceci :

![règle de pare-feu dédiée qui permet au serveur OpenSSH de communiquer à travers le Pare-feu Windows](https://cdn.hashnode.com/res/hashnode/image/upload/v1727219301264/fb58d5ce-f8cf-49d2-9b56-6f1571c08652.png align="center")

#### Résumé de la réponse CLI ci-dessus :

* **Nom de la règle** : sshd
    
* **Nom d'affichage** : OpenSSH SSH Server
    
* **Direction** : Entrant (Inbound)
    
* **Action** : Autoriser (Allow)
    
* **Activé** : True
    
* **Profil** : Tout (Any)
    

La règle est conçue pour autoriser le trafic entrant, permettant aux clients externes de se connecter au serveur. Le statut "Activé" confirme que la règle est actuellement active, tandis que le "Profil" défini sur "Tout" indique qu'elle s'applique à tous les types de réseaux, y compris publics, privés et de domaine.

#### Politiques de sécurité :

* **Politique de traversée de bord (Edge Traversal Policy)** : Bloquer
    
* **Mappage de source lâche (Loose Source Mapping)** : False
    
* **Mappage local uniquement (Local Only Mapping)** : False
    

La "EdgeTraversalPolicy" est configurée sur "Bloquer", empêchant le trafic de traverser la limite du réseau, interdisant spécifiquement les connexions des réseaux publics vers les réseaux privés. Cela aide à renforcer la sécurité en atténuant les vulnérabilités potentielles.

Les paramètres pour "LooseSourceMapping" et "LocalOnlyMapping" sont tous deux définis sur false, garantissant que seules les connexions directes sont autorisées sans mappage supplémentaire.

#### Statut et application :

* **Statut principal** : OK
    
* **Statut** : La règle a été analysée avec succès depuis le magasin.
    
* **Statut d'application** : Non applicable
    
* **Source du magasin de politiques** : Magasin persistant (PersistentStore)
    
* **Type de source du magasin de politiques** : Local
    

Le champ "Statut" confirme que la règle a été analysée avec succès depuis le magasin de politiques, indiquant qu'il n'y a aucun problème de configuration. Le "Statut d'application" marqué comme "Non applicable" suggère qu'il n'y a pas de restrictions qui empêcheraient l'application de la règle.

N'oubliez pas que pour configurer une connexion SSH, nous avons besoin d'une paire de clés SSH – une clé publique et une clé privée. Voyons comment faire cela maintenant.

### Comment générer des clés SSH

* Ouvrez votre terminal Windows ou PowerShell.
    
* Exécutez la commande `ssh-keygen` pour générer une nouvelle paire de clés SSH.
    
* Suivez les invites pour spécifier l'emplacement d'enregistrement et la phrase secrète (facultative) pour vos clés.
    

![commande cli pour générer des clés ssh et sa réponse](https://cdn.hashnode.com/res/hashnode/image/upload/v1727220068539/7ee02096-da9e-4a26-8da8-106ec2dcefee.png align="center")

Vous obtiendrez ce que vous voyez dans l'image ci-dessus si vous réussissez.

La clé publique sera enregistrée sous le nom `id_`[`rsa.pub`](http://rsa.pub) dans le répertoire `.ssh` de votre dossier utilisateur personnel (par exemple, `C:\Users\vous\.ssh\id_`[`rsa.pub`](http://rsa.pub)).

![affichage de la clé privée et publique sur notre système local dans notre répertoire-personnel/.ssh](https://cdn.hashnode.com/res/hashnode/image/upload/v1727220167279/b04fed4a-17d1-49e6-ad34-d5cb41692d13.png align="center")

### Comment ajouter la clé publique à GitHub

* Connectez-vous à votre compte GitHub et accédez aux paramètres de votre compte.
    
* Naviguez vers la section "SSH and GPG keys".
    
* Cliquez sur le bouton "New SSH key". Donnez à votre clé un titre descriptif, puis copiez le contenu du fichier `id_`[`rsa.pub`](http://rsa.pub) (votre clé publique) dans le champ "Key".
    
* Cliquez sur "Add SSH key" pour enregistrer la nouvelle clé.
    

### Tester la connexion SSH

Dans votre terminal Windows ou PowerShell, exécutez la commande suivante pour tester votre connexion SSH vers GitHub :

```plaintext
ssh -T git@github.com
```

Si vous y êtes invité, saisissez votre phrase secrète si vous en avez défini une lors du processus de génération de clé. Si vous n'avez pas défini de phrase secrète, tapez simplement "yes" lorsqu'on vous demande une réponse au handshake.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727220975104/6ed54e15-00a9-4cad-b95e-3424be855596.png align="center")

Si la connexion est réussie, vous devriez voir un message tel que "Hi username! You've successfully authenticated, but GitHub does not provide shell access."

Vous pouvez résoudre cela en suivant le processus décrit [ici](https://gist.github.com/bsara/5c4d90db3016814a3d2fe38d314f9c23).

### Clonage d'un dépôt à l'aide de SSH

Accédez à l'un de vos dépôts GitHub et copiez l'URL de clonage SSH, qui commence généralement par [`git@github.com`](mailto:git@github.com) :

![lien ssh pour cloner un dépôt github](https://cdn.hashnode.com/res/hashnode/image/upload/v1727222441040/926444a1-bdf8-4f33-980c-0c2c87691a6b.png align="center")

Dans votre terminal local, exécutez la commande `git clone` [`git@github.com`](mailto:git@github.com)`:nom_utilisateur/depot.git` pour cloner le dépôt en utilisant le protocole SSH.

## Conclusion

Vous avez maintenant SSH qui fonctionne entre votre ordinateur Windows et votre compte GitHub. Cela signifie que vous pouvez travailler sur vos projets GitHub plus facilement et plus sûrement.

### Pourquoi SSH est génial :

1. C'est extrêmement sécurisé. SSH brouille vos données pour que les autres ne puissent pas les espionner.
    
2. C'est pratique. Plus besoin de taper des mots de passe tout le temps !
    
3. C'est flexible. Vous pouvez l'utiliser pour bien d'autres choses que GitHub.
    
4. Vous pouvez avoir différentes "clés" pour différents projets.
    
5. Cela fonctionne bien avec les outils de codage automatique.
    

Mais ce n'est pas parfait :

1. Garder une trace de nombreuses clés SSH peut être un casse-tête.
    
2. Si quelqu'un obtient votre clé privée, il pourrait accéder à vos données.
    
3. La configuration initiale peut être délicate.
    
4. Vous devez penser à changer vos clés vous-même pour plus de sécurité.
    
5. Certains réseaux peuvent bloquer SSH, ce qui peut être ennuyeux.
    

N'oubliez pas de garder votre clé SSH privée en sécurité. C'est comme un mot de passe spécial pour votre compte GitHub, alors protégez-la bien.

Même avec ces petits inconvénients, SSH reste fantastique pour la plupart des développeurs. Vous êtes maintenant prêt à travailler sur vos projets GitHub plus facilement et en toute sécurité. Amusez-vous bien avec votre configuration de codage améliorée et continuez à apprendre de nouvelles façons de sécuriser votre travail.