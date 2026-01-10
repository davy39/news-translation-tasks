---
title: Comment héberger un site web sur AWS EC2 en utilisant un modèle CSS
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-11-08T18:35:50.763Z'
originalURL: https://freecodecamp.org/news/host-a-website-on-aws-ec2-using-a-css-template
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731103973241/e1277a4c-3456-4f11-b809-24caf56ae13a.png
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
- name: CSS
  slug: css
seo_title: Comment héberger un site web sur AWS EC2 en utilisant un modèle CSS
seo_desc: 'Are you ready to take your web hosting skills to the next level by using
  a CSS template? Hosting a professional looking website doesn’t have to be complicated,
  and with AWS EC2, you can have your website live in no time!

  In this guide, I’ll show you ...'
---

Êtes-vous prêt à passer vos compétences en hébergement web au niveau supérieur en utilisant un modèle CSS ? Héberger un site web professionnel n'a pas besoin d'être compliqué, et avec AWS EC2, vous pouvez avoir votre site web en ligne en un rien de temps !

Dans ce guide, je vais vous montrer comment héberger un site web en utilisant un modèle préconçu de [**CSS templates**](https://www.free-css.com/free-css-templates) directement sur votre instance EC2.

Avant de plonger dans ce guide, assurez-vous d'avoir suivi mon [**précédent blog**](https://www.freecodecamp.org/news/how-to-launch-an-ec2-instance-and-a-web-server-using-httpd/) sur la façon de lancer et de se connecter à une instance EC2. Si vous n'avez pas encore configuré une instance EC2, rendez-vous d'abord sur ce post pour mettre votre instance en route. Une fois que c'est fait, vous êtes prêt à continuer !

### Étape 1 : Télécharger le modèle "Built Better"

Pour ce tutoriel, nous utiliserons le modèle Built Better, qui est gratuit et facile à configurer.

Rendez-vous sur [ce lien](https://www.free-css.com/free-css-templates/page284/built-better) et téléchargez le modèle.

Faites un clic droit sur le bouton de téléchargement et sélectionnez "Copier le lien propre". Nous utiliserons ce lien pour télécharger le modèle directement dans votre instance EC2.

### Étape 2 : Télécharger le modèle directement sur votre instance EC2

Maintenant que vous avez le lien vers le modèle, téléchargeons-le directement sur votre instance EC2 en utilisant `wget`.

Connectez-vous à votre instance EC2 via SSH ou MobaXterm (comme couvert dans mon [**précédent blog**](https://www.freecodecamp.org/news/connect-to-your-ec2-instance-using-mobaxterm/)) et naviguez jusqu'au répertoire `/var/www/html` où vos fichiers de site web seront stockés :

```bash
cd /var/www/html
```

Utilisez la commande `wget` suivie du lien copié pour télécharger le modèle "Built Better" directement dans votre instance EC2 :

```bash
sudo wget https://www.free-css.com/assets/files/free-css-templates/download/page284/built-better.zip
```

**Note :** Après le téléchargement, il est bon de vérifier le nom du fichier pour s'assurer qu'il correspond au fichier utilisé dans les commandes suivantes. Vous pouvez le faire en exécutant la commande `ls` :

```bash
ls
```

### Étape 3 : Décompresser les fichiers du modèle

Maintenant que le modèle a été téléchargé, il est temps de l'extraire. Installez l'utilitaire `unzip` s'il n'est pas déjà installé :

```bash
sudo dnf install unzip -y
```

Puis décompressez le modèle :

```bash
sudo unzip built-better.zip -d /var/www/html/
```

Après avoir décompressé, assurez-vous de vérifier le nom du dossier où les fichiers ont été extraits. Vous pouvez le faire en listant le contenu du répertoire `/var/www/html` :

```bash
ls /var/www/html/
```

Dans ce cas, le contenu décompressé se trouve dans un dossier nommé `html`. Ce dossier contient tous les fichiers du modèle. Si le nom du dossier est différent dans votre cas, ajustez les étapes suivantes en conséquence.

Tout d'abord, déplacez les fichiers du dossier `html` vers le répertoire racine `/var/www/html/` :

```bash
sudo mv /var/www/html/html/* /var/www/html/
```

Ensuite, supprimez le dossier inutile :

```bash
sudo rm -r /var/www/html/html
```

Enfin, supprimez le fichier ZIP :

```bash
sudo rm built-better.zip
```

### Étape 4 : Configurer le serveur web pour héberger votre modèle

Si ce n'est pas déjà fait, assurez-vous que votre serveur web Apache HTTPD est installé et en cours d'exécution. Vous pouvez suivre ces étapes pour vous assurer que votre serveur est prêt :

Installez Apache (si ce n'est pas déjà fait) :

```bash
sudo yum install httpd -y
```

Démarrez le service Apache :

```bash
sudo systemctl start httpd
```

Activez Apache pour qu'il démarre au démarrage :

```bash
sudo systemctl enable httpd
```

Votre serveur web devrait maintenant être opérationnel et prêt à servir votre modèle.

### Étape 5 : Tester votre site web

Maintenant, la partie excitante : voir votre site en ligne ! Ouvrez un navigateur et accédez à l'adresse IP publique de votre instance EC2. Vous devriez maintenant voir le modèle Built Better en ligne et prêt à l'emploi.

Voici comment vérifier :

* Trouvez l'adresse IP publique de votre instance EC2 à partir du tableau de bord AWS EC2.

* Entrez l'IP dans votre navigateur, comme ceci : [`http://votre-ip-publique-ec2`](http://your-ec2-public-ip)

* Votre site web devrait maintenant être en ligne avec le modèle Built Better ! 🎉

### Conclusion

Félicitations ! Vous avez réussi à héberger un site web professionnel en utilisant le modèle CSS Built Better sur votre instance EC2.

En seulement quelques étapes, vous êtes passé du lancement d'une instance EC2 à l'hébergement d'un site web entièrement stylisé, le tout en utilisant l'infrastructure cloud puissante d'AWS.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)

* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)