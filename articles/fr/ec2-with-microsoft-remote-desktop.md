---
title: Comment se connecter à Amazon EC2 en utilisant Microsoft Remote Desktop sur
  macOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-09T01:22:54.000Z'
originalURL: https://freecodecamp.org/news/ec2-with-microsoft-remote-desktop
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/rdp.png
tags:
- name: configuration
  slug: configuration
- name: ec2
  slug: ec2
- name: macOS
  slug: macos
- name: rdp
  slug: rdp
seo_title: Comment se connecter à Amazon EC2 en utilisant Microsoft Remote Desktop
  sur macOS
seo_desc: 'By Clark Jason Ngo

  I created this guide because of an experience I had while teaching. My students
  needed to use an application that was only available on Windows OS but the students
  only had macOS.

  We will be touching on the technologies shown below...'
---

Par Clark Jason Ngo

J'ai créé ce guide suite à une expérience vécue pendant que j'enseignais. Mes étudiants devaient utiliser une application uniquement disponible sur Windows OS, mais ils n'avaient que macOS.

Nous allons aborder les technologies présentées ci-dessous :  


![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-56.png)

* Amazon EC2 : lancer un Windows Server 2019
* Microsoft Remote Desktop : application macOS pour se connecter à distance (RDP) à EC2

## Amazon EC2

### Lancement d'une instance EC2 Windows Server

1. Connectez-vous à votre [AWS Management Console](https://aws.amazon.com/console/).
2. Choisissez **Services**, puis **EC2**.
3. Dans la barre latérale, cliquez sur **Instances**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-57.png)
_Barre latérale EC2_

4. Cliquez sur **Lancer une instance**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-58.png)
_Bouton Lancer une instance_

5. Faites défiler vers le bas et choisissez **Microsoft Windows Server 2019 Base**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-59.png)
_Page de choix de l'AMI_

6. En bas de la page Choix du type d'instance, cliquez sur **Revoir et lancer**. Cela vous amènera à la page de révision.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-60.png)
_Lancement avec une configuration minimale_

7. Dans la page de révision, cliquez sur **Lancer**. Vous serez invité à sélectionner une paire de clés existante ou une nouvelle paire de clés. 

Si vous choisissez **Créer une nouvelle paire de clés**, vous devez donner un nom à la nouvelle paire de clés, puis télécharger la paire de clés. Ensuite, vous pourrez procéder à la sélection de **Lancer l'instance**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-61.png)
_Paire de clés pour accéder à l'instance_

Si vous choisissez **Choisir une paire de clés existante**, vous devez sélectionner une paire de clés et cocher la case pour reconnaître l'utilisation de la paire de clés.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-62.png)
_Dernière étape pour lancer l'instance_

8. Cliquez sur l'ID d'instance généré.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-63.png)
_Accès à l'instance EC2_

9. Trouvez et sauvegardez les informations suivantes :

* DNS public (Adresse IP)
* Nom d'utilisateur
* Mot de passe

Pour obtenir l'adresse IP, faites défiler vers la droite de votre instance EC2 :  

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-70.png)
_Adresse IP de l'instance EC2_

Vous pouvez également trouver cela dans l'onglet Description ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-67.png)
_Adresse IP de l'instance EC2_

10. Pour obtenir le nom d'utilisateur et le mot de passe, choisissez l'instance EC2 (cocher la case), cliquez sur **Actions**, puis **Obtenir le mot de passe Windows**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-68.png)
_Obtention du nom d'utilisateur et du mot de passe_

Vous pouvez rencontrer _Mot de passe non disponible_ et vous devrez attendre quelques minutes.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-71.png)
_Provisionnement du mot de passe généré automatiquement_

11. Localisez la paire de clés existante ou la nouvelle paire de clés que vous avez téléchargée sur votre machine locale. Cliquez sur **Choisir un fichier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-72.png)
_Récupération de la paire de clés_

12. Après avoir téléchargé la paire de clés, cliquez sur **Décrypter le mot de passe**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-73.png)

13. Copiez les informations suivantes et sauvegardez-les dans un fichier ou dans le presse-papiers. Cliquez sur **Fermer** lorsque vous avez terminé.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-74.png)
_Informati
ons pour la connexion à distance_

## Microsoft Remote Desktop 

### Installation de l'application et connexion à l'instance EC2

1. Ouvrez votre App Store, puis recherchez **Microsoft Remote Desktop**. Cliquez sur Installer (il montre UPDATE ici car je l'ai déjà installé).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-64.png)
_Microsoft Remote Desktop dans l'App Store_

2. Après l'installation, ouvrez Microsoft Remote Desktop.

3. En haut, cliquez sur l'icône **+** et choisissez **Bureau**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-65.png)
_Création d'une nouvelle connexion de bureau_

4. Dans le nom de l'ordinateur, copiez l'adresse IP de l'instance EC2, puis cliquez sur **Ajouter**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-66.png)
_Ajout de l'adresse IP_

5. Copiez l'administrateur et le mot de passe de plus tôt et collez-les ici. Appuyez sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-75.png)
_Connexion avec le nom d'utilisateur et le mot de passe_

Vous êtes maintenant connecté à votre instance EC2 Windows Server.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-76.png)
_Instance EC2 Windows Server_

Remarque : Pour éviter d'être facturé après avoir utilisé le niveau gratuit pour EC2, cliquez soit sur **Arrêter** pour réduire les coûts, soit sur **Terminer** pour supprimer l'instance et ne pas être facturé. 

Vous avez accès à cela en sélectionnant l'instance et en choisissant **Actions > État de l'instance > Arrêter/Terminer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-77.png)

## Voici un tutoriel vidéo :

%[https://youtu.be/QQIivlr_CKk]

Connectez-vous avec moi sur LinkedIn [ici](https://www.linkedin.com/in/clarkngo/).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-243.png)