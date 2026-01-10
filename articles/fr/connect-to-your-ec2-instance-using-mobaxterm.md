---
title: Comment se connecter à votre instance EC2 en utilisant MobaXterm avec SSH et
  un fichier de paire de clés (.pem)
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-10-22T10:54:33.284Z'
originalURL: https://freecodecamp.org/news/connect-to-your-ec2-instance-using-mobaxterm
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729574902773/f80eb07d-524a-4fa2-a8d8-29c6438d37aa.png
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
seo_title: Comment se connecter à votre instance EC2 en utilisant MobaXterm avec SSH
  et un fichier de paire de clés (.pem)
seo_desc: In this article, I’ll walk you through the steps of connecting to your EC2
  instance using MobaXterm with a .pem keypair file. Whether you're a beginner dipping
  your toes into the cloud or an experienced user looking for a quicker method, I’ve
  got you...
---

Dans cet article, je vais vous guider à travers les étapes de connexion à votre instance EC2 en utilisant MobaXterm avec un fichier de paire de clés `.pem`. Que vous soyez un débutant qui s'initie au cloud ou un utilisateur expérimenté à la recherche d'une méthode plus rapide, je vous couvre. Alors, plongeons-nous dans le sujet !

## **Table des matières**

* [Pourquoi MobaXterm ?](#heading-pourquoi-mobaxterm)
    
* [Étape 1 : Installer MobaXterm](#heading-etape-1-installer-mobaxterm)
    
* [Étape 2 : Obtenir l'IP publique de votre instance EC2 et la paire de clés](#heading-etape-2-obtenir-lip-publique-de-votre-instance-ec2-et-la-paire-de-cles)
    
* [Étape 3 : Ouvrir MobaXterm et démarrer une nouvelle session SSH](#heading-etape-3-ouvrir-mobaxterm-et-demarrer-une-nouvelle-session-ssh)
    
* [Étape 4 : Entrer les détails de la session SSH](#heading-etape-4-entrer-les-details-de-la-session-ssh)
    
* [Étape 5 : Attacher votre paire de clés .pem](#heading-etape-5-attacher-votre-paire-de-cles-pem)
    
* [Étape 6 : Se connecter à votre instance EC2](#heading-etape-6-se-connecter-a-votre-instance-ec2)
    
* [Étape 7 : Résoudre les problèmes courants](#heading-etape-7-resoudre-les-problemes-courants)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi MobaXterm ?

Vous vous demandez peut-être pourquoi nous utilisons MobaXterm plutôt que d'autres outils SSH. Eh bien, pour commencer, il est très convivial pour les débutants, et il combine plusieurs outils puissants en un seul. Vous pouvez l'utiliser pour transférer des fichiers, exécuter des scripts, ou même ouvrir plusieurs sessions simultanément.

De plus, c'est comme le couteau suisse des connexions à distance. Que vous travailliez avec AWS, Google Cloud, ou même un Raspberry Pi à la maison, MobaXterm peut tout faire.

## Étape 1 : Installer MobaXterm

Si vous n'êtes pas déjà familier avec MobaXterm, il est principalement utilisé pour tout ce qui concerne l'accès à distance. Vous pouvez le télécharger [ici](https://mobaxterm.mobatek.net/download-home-edition.html) gratuitement. L'installation est très simple : téléchargez, cliquez et installez.

Une fois que vous l'avez configuré, lancez MobaXterm et préparez-vous pour la partie amusante.

## Étape 2 : Obtenir l'IP publique de votre instance EC2 et la paire de clés

Avant de continuer, il y a deux informations clés dont vous aurez besoin :

**Adresse IP publique** : Il s'agit de l'adresse unique qu'AWS attribue à votre instance EC2. Pour la trouver, allez dans le **Tableau de bord EC2** dans AWS, sélectionnez votre instance en cours d'exécution et récupérez l'**Adresse IPv4 publique** (elle ressemble à `13.123.45.67`).

**Votre fichier .pem** : Il s'agit du fichier de clé privée que vous avez téléchargé lors de la création de votre instance EC2. Si vous ne l'avez pas enregistré, vous devrez peut-être créer une nouvelle paire de clés car AWS ne vous permet de le télécharger qu'une seule fois. (Pas de pression, mais cette fois, ne le perdez pas !)

## Étape 3 : Ouvrir MobaXterm et démarrer une nouvelle session SSH

Il est temps de faire un peu de magie avec MobaXterm ! Ouvrez l'application, et vous verrez une interface intuitive. Ne vous laissez pas intimider par tous les boutons, concentrez-vous simplement sur le coin supérieur gauche où il est écrit **Session**.

![Interface utilisateur de MobaXterm](https://cdn.hashnode.com/res/hashnode/image/upload/v1729567478544/cf69a56b-9d1e-4de3-b6d8-224634b55ae3.png align="center")

Voici ce qu'il faut faire ensuite :

* Cliquez sur **Session** (vous vous sentirez puissant rien qu'en appuyant sur ce bouton).
    
* Dans la nouvelle fenêtre, sélectionnez **SSH** comme type de session.
    

![Onglet de configuration de la session MobaXterm](https://cdn.hashnode.com/res/hashnode/image/upload/v1729567593446/ee8f369d-24be-419d-971f-30e3e4355dd6.png align="center")

## Étape 4 : Entrer les détails de la session SSH

Il est temps de remplir les détails qui permettront à MobaXterm de se connecter à votre instance EC2. Voici ce que vous devez savoir :

* **Hôte distant** : Entrez l'**Adresse IP publique** de votre instance EC2 ici. Souvenez-vous, vous l'avez récupérée depuis le Tableau de bord EC2 plus tôt.
    
* **Nom d'utilisateur** : Si vous utilisez Amazon Linux, votre nom d'utilisateur par défaut est `ec2-user`. Si vous êtes sur Ubuntu, c'est `ubuntu`.
    
## Étape 5 : Attacher votre paire de clés .pem

MobaXterm rend très facile l'utilisation de votre fichier de clé `.pem` pour l'authentification (pas besoin de le convertir en `.ppk`, comme vous devriez le faire avec d'autres outils).

Voici comment attacher votre fichier `.pem` :

* Allez dans l'onglet **Paramètres SSH avancés**.
    
* Cochez l'option **Utiliser une clé privée**.
    
* Cliquez sur **Parcourir** et trouvez votre fichier `.pem` sur votre ordinateur.
    
* Sélectionnez le fichier et cliquez sur **OK**.
    

C'est comme donner à MobaXterm la clé secrète pour déverrouiller votre instance EC2.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1729567798203/535c226e-fbd2-43fc-b1af-a48ce171b974.png align="center")

## Étape 6 : Se connecter à votre instance EC2

Maintenant que vous avez rempli tous les détails, cliquez sur **OK** pour démarrer votre session. Si tout a été configuré correctement, vous devriez voir un terminal apparaître, et MobaXterm fera sa magie pour vous connecter à votre instance EC2.

🎉 Et voilà, vous êtes connecté ! Vous devriez voir une fenêtre de terminal connectée à votre instance, et maintenant vous pouvez commencer à taper des commandes comme un pro.

## Étape 7 : Résoudre les problèmes courants

Nous savons tous que la technologie ne se comporte pas toujours comme prévu. Voici quelques problèmes courants que vous pourriez rencontrer – et comment les résoudre :

* **Délai de connexion dépassé** : Cela peut être dû aux paramètres du groupe de sécurité de votre instance. Assurez-vous que votre groupe de sécurité EC2 autorise le trafic entrant sur le **port 22** (le port SSH) depuis votre adresse IP.
    
* **Échec de l'authentification** : Assurez-vous d'utiliser le bon nom d'utilisateur (`ec2-user` pour Amazon Linux, `ubuntu` pour Ubuntu).
    
## Conclusion

Et voilà ! Se connecter à votre instance EC2 en utilisant MobaXterm avec votre paire de clés `.pem` est aussi simple que de suivre ces étapes. Ce n'est pas de la science-fiction, mais ça y ressemble un peu, n'est-ce pas ? Maintenant que vous avez votre instance EC2 en marche, le ciel est la limite.

Alors, allez-y, prenez ce que vous avez appris ici, explorez, expérimentez, et surtout, amusez-vous avec ça ! Jusqu'à la prochaine fois, bon calcul dans le cloud ! ☁️

Vous pouvez me suivre sur

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)