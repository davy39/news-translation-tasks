---
title: Comment configurer AWS Simple Email Service
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2023-03-27T15:44:03.000Z'
originalURL: https://freecodecamp.org/news/set-up-aws-simple-email-service
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Blog-Banner
seo_title: Comment configurer AWS Simple Email Service
---

Template--3-.png
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: e-mail
  slug: email
seo_title: null
seo_desc: "Si vous recherchez un moyen fiable et rentable d'envoyer des e-mails,\
  \ AWS Simple Email Service (SES) est une excellente option. C'est une plateforme de messagerie basée sur le cloud\
  \ qui vous aide à envoyer et recevoir des e-mails rapidement et facilement. \nAvec SES, vous n'avez\
  \ pas à vous soucier ..."
---

Si vous recherchez un moyen fiable et rentable d'envoyer des e-mails, AWS Simple Email Service (SES) est une excellente option. C'est une plateforme de messagerie basée sur le cloud qui vous aide à envoyer et recevoir des e-mails rapidement et facilement.

Avec SES, vous n'avez pas à vous soucier de la gestion de votre propre serveur de messagerie, et vous pouvez bénéficier de l'évolutivité et de la fiabilité de l'infrastructure cloud d'Amazon.

La configuration de SES comporte quelques étapes, telles que la vérification de votre domaine, la vérification de votre adresse e-mail et la configuration des enregistrements MX. Ce court guide vous accompagnera à travers chaque étape pour opérationnaliser votre SES en un rien de temps.

**Prérequis :** Ce tutoriel sera une démonstration pratique. Pour suivre, assurez-vous d'avoir un [compte AWS](https://aws.amazon.com/free/) actif.

## Comment configurer AWS SES

### Étape 1 – Vérifier les identités

Tout d'abord, connectez-vous à votre compte Console de gestion AWS et recherchez Simple Email Service. Sélectionnez **Amazon Simple Email Service.**

![Image](https://i.imgur.com/8ZjaAKn.png)
_Recherche d'AWS SES_

Cela vous mènera à une console SES.

Pour commencer à envoyer des e-mails, vous devrez créer une identité. Cela implique de vérifier l'adresse e-mail que vous utiliseriez pour envoyer des e-mails. Si vous ne vérifiez pas l'adresse e-mail, vous ne pouvez pas utiliser l'e-mail pour effectuer une quelconque action sur SES.

Notez que vous pouvez ajouter un domaine en tant qu'identité, mais nous utiliserons une adresse e-mail pour ce guide. Cliquez sur **Create identity** pour vérifier une adresse e-mail.

![Image](https://i.imgur.com/8xrgwvL.png)
_Création d'une identité_

Ensuite, sélectionnez l'option **Email address** et saisissez l'adresse e-mail que vous souhaitez utiliser.

Dans Amazon SES, vous pouvez utiliser un domaine, un sous-domaine ou une adresse e-mail comme identité *vérifiée*. Vous pouvez utiliser ce qui vous convient le mieux.

![Image](https://i.imgur.com/apfMPNY.png)
_Vérification d'une identité_

Nous utilisons des tags pour gérer les identités sur Amazon SES. Nous allons passer cette étape ici, mais si vous le souhaitez, vous pouvez définir un tag. Une fois terminé, cliquez sur **Create identity** pour créer une identité pour votre compte SES.

![Image](https://i.imgur.com/8e6swKE.png)
_Création d'une identité pour Amazon SES_

Maintenant, un e-mail sera envoyé à l'adresse e-mail que vous avez utilisée pour créer l'identité. Cliquez sur le lien dans l'e-mail pour vérifier votre adresse.

![Image](https://paper-attachments.dropboxusercontent.com/s_8C16BB81FDF5129198CC129A07A220ADD326C1D4AD8E16A42ED5864426B31F5B_1670344969240_6DeFvpt.png)
_Vérification de votre adresse e-mail_

Une fois cela fait, vous verrez votre adresse e-mail dans la liste des identités vérifiées de votre compte SES.

![Image](https://i.imgur.com/22Q4jrr.png)
_Liste des identités vérifiées_

## Comment créer des identifiants SMTP

Le protocole SMTP (Simple Mail Transfer Protocol) envoie et reçoit des messages via un serveur de messagerie. Dans cette section, vous apprendrez comment créer des identifiants qui vous donnent accès au serveur de messagerie SES pour envoyer et recevoir du courrier.

Tout d'abord, connectez-vous à votre [tableau de bord Amazon SES](https://us-east-1.console.aws.amazon.com/ses/home?region=us-east-1#/account). Cliquez sur **SMTP settings.**

![Image](https://i.imgur.com/1LsYmUe.png)
_Tableau de bord Amazon SES_

Cliquez ensuite sur **Create SMTP credentials** pour créer les détails de connexion à votre compte SMTP sous Amazon SES.

![Image](https://i.imgur.com/M4e6D2p.png)
_Création d'identifiants SMTP_

Vous pouvez choisir de définir un nom d'utilisateur IAM ou d'utiliser celui par défaut. Une fois que c'est fait, cliquez sur **Create**.

![Image](https://i.imgur.com/pI1OI2R.png)
_Création d'un utilisateur IAM pour le SMTP_

Une fois que vous avez créé un utilisateur IAM, vos détails SMTP s'afficheront à côté de votre nom d'utilisateur IAM.

Une notification vous indiquant que votre utilisateur a été créé s'affichera en haut. Assurez-vous de télécharger les identifiants car il s'agit d'un détail d'affichage unique. Vous pouvez les télécharger en cliquant sur **Download Credentials**.

![Image](https://i.imgur.com/uc8Pxta.png)
_Identifiants SMTP créés_

Excellent ! Vous avez accès aux identifiants SMTP d'AWS Simple Email Service. Vous pouvez utiliser ces identifiants pour connecter votre backend au serveur Amazon SES afin d'envoyer des e-mails.

# Conclusion

Amazon Simple Email Service (SES) est un outil puissant et fiable pour envoyer rapidement des e-mails de marketing, de notification et transactionnels. La configuration d'Amazon SES est simple et vous pouvez le faire en quelques étapes faciles.

Après vous être inscrit à un compte AWS et avoir accédé à la console Amazon SES, vous pouvez vérifier et définir une adresse e-mail par défaut et commencer à envoyer des e-mails via le service.

Avec Amazon SES, vous bénéficiez des avantages de l'envoi d'e-mails dans le cloud, notamment une meilleure délivrabilité, une plus grande évolutivité et une sécurité renforcée."