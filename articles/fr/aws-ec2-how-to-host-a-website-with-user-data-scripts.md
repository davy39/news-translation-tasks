---
title: 'AWS EC2 : Comment héberger rapidement votre site web avec des scripts de données
  utilisateur'
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-11-26T19:31:16.789Z'
originalURL: https://freecodecamp.org/news/aws-ec2-how-to-host-a-website-with-user-data-scripts
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732639814571/62719c49-cd15-4f2c-9586-22a5a300bc4a.png
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
- name: hosting
  slug: hosting
seo_title: 'AWS EC2 : Comment héberger rapidement votre site web avec des scripts
  de données utilisateur'
seo_desc: If you want to practice and improve your web hosting skills, this tutorial
  is for you. With AWS EC2 and a little magic called user data scripts, you’ll be
  running a stunning website with a CSS template in no time. And the best part? You
  don’t need to...
---

Si vous souhaitez pratiquer et améliorer vos compétences en hébergement web, ce tutoriel est fait pour vous. Avec AWS EC2 et un peu de magie appelée scripts de données utilisateur, vous aurez un site web époustouflant avec un modèle CSS en un rien de temps. Et le meilleur dans tout ça ? Vous n'avez pas besoin d'installer manuellement tout – le script de données utilisateur fait tout le travail difficile pour vous.

Avant de commencer avec ce guide, assurez-vous d'avoir lu mon [tutoriel précédent](https://www.freecodecamp.org/news/host-a-website-on-aws-ec2-using-a-css-template) sur AWS EC2. Il couvre les essentiels de la création et de la configuration d'une instance EC2. Vous apprendrez à naviguer dans la Console de Gestion AWS, à sélectionner le bon type d'instance, à configurer les groupes de sécurité, et plus encore.

Ces connaissances fondamentales vous assureront d'être pleinement préparé à lancer votre site web sans effort avec l'aide des scripts de données utilisateur.

Alors, prenez un café, et plongeons dans ce guide simple et amusant. À la fin, vous serez capable de lancer votre propre site web sans transpirer.

## Table des Matières

* [Ce que nous allons couvrir](#heading-ce-que-nous-allons-couvrir)
    
* [Étape 1 : Lancer votre instance EC2](#heading-etape-1-lancer-votre-instance-ec2)
    
* [Étape 2 : Attendez… Le script a déjà tout fait ?](#heading-etape-2-attendez-le-script-a-deja-tout-fait)
    
* [Étape 3 : Accéder à votre site web](#heading-etape-3-acceder-a-votre-site-web)
    
* [Conclusion](#heading-conclusion)
    
* [Vous en voulez plus ?](#heading-vous-en-voulez-plus)
    

## Ce que nous allons couvrir :

Aujourd'hui, nous allons :

* Lancer une instance EC2 (Ne vous inquiétez pas, c'est plus facile que ça en a l'air).
    
* Utiliser un script de données utilisateur pour automatiser la configuration d'un serveur web.
    
* Télécharger un modèle CSS et l'héberger sur votre instance.
    

Vous vous demandez peut-être : pourquoi un script de données utilisateur ? Imaginez-le comme une liste de tâches pour votre instance EC2. Lorsque l'instance démarre, elle parcourt cette liste et configure tout automatiquement. C'est comme avoir un assistant personnel qui gère toutes les tâches de configuration fastidieuses. Ça a l'air bien, non ?

### Étape 1 : Lancer votre instance EC2

D'abord, rendez-vous sur votre Console de Gestion AWS. C'est là que toute la magie opère.

Connectez-vous à AWS et rendez-vous sur la Console AWS. Si vous n'avez pas encore de compte, ne vous inquiétez pas, vous pouvez simplement vous inscrire – c'est gratuit pour une utilisation basique.

Voici les étapes que vous allez suivre pour lancer l'instance :

* Dans la console, tapez **EC2** dans la barre de recherche et cliquez sur le service EC2.
    
* Cliquez sur le gros bouton **Lancer l'instance**. 
    
* Donnez à votre instance un nom sympa comme "ServeurWeb".
    
* **Choisissez votre AMI** : Sélectionnez l'AMI Amazon Linux 2 (éligible pour le niveau gratuit). Il est léger, rapide et parfait pour notre cas d'utilisation.
    
* **Type d'instance** : Optez pour le t2.micro (il est gratuit pour la plupart des cas d'utilisation, et nous aimons les choses gratuites, n'est-ce pas ?).
    
* **Script de données utilisateur** : Maintenant, c'est là que les choses deviennent intéressantes. Faites défiler jusqu'à Détails avancés, et dans le champ Données utilisateur, collez le script suivant. Ce script gérera tout, de l'installation d'Apache au téléchargement et à la décompression d'un modèle CSS élégant.
    
* ![script de données utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1732640127024/ec187a49-61ac-4a98-82c1-c149bcf8ef91.png align="center")
    
    ```bash
    #!/bin/bash
    
    # Mettre à jour l'instance et installer les paquets nécessaires
    yum update -y
    yum install -y httpd wget unzip
    
    # Démarrer Apache et l'activer pour qu'il démarre au boot
    systemctl start httpd
    systemctl enable httpd
    
    # Naviguer vers le répertoire racine web
    cd /var/www/html
    
    # Télécharger un modèle CSS directement
    wget https://www.free-css.com/assets/files/free-css-templates/download/page284/built-better.zip
    
    # Décompresser le modèle et déplacer les fichiers vers la racine web
    unzip built-better.zip -d /var/www/html/
    mv /var/www/html/html/* /var/www/html/
    
    # Nettoyer les fichiers inutiles
    rm -r /var/www/html/html
    rm built-better.zip
    
    # Redémarrer Apache pour appliquer les changements
    systemctl restart httpd
    ```
    
    * **Configurer votre groupe de sécurité** : Vous voulez que le monde puisse voir votre site, n'est-ce pas ? Alors, assurez-vous d'autoriser **HTTP** (port 80). Cela permettra à votre site web d'être accessible à quiconque avec le lien.
        
    
    * **Lancer votre instance** : Après avoir tout vérifié, cliquez sur **Lancer**. AWS vous demandera de choisir une paire de clés (dont vous aurez besoin si vous souhaitez vous connecter en SSH à votre instance plus tard). Si vous n'en avez pas, créez une nouvelle paire de clés.
        
    
    Boom ! Votre instance EC2 est en cours de lancement. Prenez une collation, elle sera prête dans quelques minutes.
    

### Étape 2 : Attendez… Le script a déjà tout fait ?

Oui, c'est exact ! Grâce au script de données utilisateur, tout le travail difficile est fait pour vous.

Voici ce qui vient de se passer en coulisses :

* Le serveur web Apache a été installé et démarré.
    
* Un modèle CSS appelé "Built Better" a été téléchargé directement sur le serveur.
    
* Le modèle a été décompressé et placé dans le répertoire web.
    

Tout cela s'est passé pendant que vous sirotiez votre café.

### Étape 3 : Accéder à votre site web

La partie excitante est enfin arrivée ! Voyons votre site web en action.

* Trouvez l'IP publique de votre instance :
    
    * Rendez-vous sur votre tableau de bord EC2, et vous verrez votre instance en cours d'exécution.
        
        Copiez l'adresse IPv4 publique.
        
* Ouvrez votre navigateur :
    
    * Dans la barre d'adresse, tapez : `http://votre-ip-publique` (remplacez `votre-ip-publique` par celle que vous venez de copier).
        
    * Appuyez sur Entrée, et… **Voilà !** Votre site web est en ligne, avec un look professionnel grâce au modèle CSS "Built Better".
        

## Conclusion

Prenons un moment pour apprécier ce que vous avez accompli :

* Lancé une instance EC2 ✓
    
* Automatisé la configuration en utilisant un script de données utilisateur ✓
    
* Hébergé un site web élégant en utilisant un modèle CSS ✓
    

Vous venez de tremper vos orteils dans le monde d'AWS et de l'hébergement cloud. Ce n'est pas aussi intimidant que ça en a l'air, n'est-ce pas ? Si vous avez aimé cela, continuez à explorer AWS – les possibilités sont infinies. À la prochaine, bon codage et bon hébergement !

### Vous en voulez plus ?

Suivez-moi sur Twitter ou connectez-vous sur LinkedIn pour plus de conseils et astuces cloud géniaux. Je partage toujours du contenu utile et j'adorerais entendre parler de votre parcours cloud !

Vous pouvez me suivre sur

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)