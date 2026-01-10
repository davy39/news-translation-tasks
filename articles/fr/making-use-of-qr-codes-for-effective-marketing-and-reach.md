---
title: Comment utiliser les QR Codes pour un marketing et une sensibilisation efficaces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-27T21:53:05.000Z'
originalURL: https://freecodecamp.org/news/making-use-of-qr-codes-for-effective-marketing-and-reach
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screenshot_1.jpg
tags:
- name: industry 4.0
  slug: industry-4-0
- name: business strategy
  slug: business-strategy
- name: '#content marketing'
  slug: content-marketing
- name: Digital Transformation
  slug: digital-transformation
- name: qr code
  slug: qr-code
seo_title: Comment utiliser les QR Codes pour un marketing et une sensibilisation
  efficaces
seo_desc: 'By Black Raven

  Efficient means doing things right. Effective is about doing the right things.

  I am an advocate for efficiency and effectiveness. There must be a more efficient
  way to share contact details other than manually typing details into my mo...'
---

Par Black Raven

**Efficace** signifie faire les choses correctement. **Efficace** consiste à faire les bonnes choses.

Je suis un défenseur de l'efficacité et de l'efficience. Il doit y avoir un moyen plus efficace de partager les coordonnées autre que de saisir manuellement les détails dans mon téléphone mobile lorsque je rencontre un nouveau contact professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-187.png align="left")

*Cartes de visite avec QR Code*

# Ajouter un nouveau contact sur votre téléphone mobile en scannant un QR Code

Lorsque Google a lancé l'application **Google Contacts** en 2017, les utilisateurs pouvaient partager des informations de contact avec des QR codes. Pour ajouter un nouveau contact, il suffit de scanner le QR code d'une personne pour enregistrer ses coordonnées sur votre téléphone.

Je pense personnellement qu'une méthode aussi efficace pour enregistrer les coordonnées devrait être implémentée sur les cartes de visite et les brochures marketing.

La tendance ne semble pas avoir décollé, peut-être parce que les gens ne savaient pas comment créer les QR Codes en premier lieu.

## Créer une liste de QR Codes de contacts personnalisés

J'ai utilisé un modèle **Google Sheets** pour générer les QR codes de contact.

Ouvrez le modèle ([lien du modèle ici](https://docs.google.com/spreadsheets/d/1jJdBgqQvYuQM-Bo0An2W7CUS5c4EQKjyRkHYZln3Wr0/edit?usp=sharing)) dans un autre onglet. Ensuite, cliquez sur « Fichier -> Créer une copie » pour l'enregistrer dans votre propre « Mon Drive » (compte Google Drive).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_grwBMqbnT87naQki630AtA.png align="left")

*Modèle Google Sheets pour générer les QR codes de contact*

*Notez que ce modèle Google Sheets semble ne fonctionner que sur les ordinateurs de bureau, pas sur les téléphones mobiles.*

Vous pouvez utiliser ce modèle en mettant à jour le **Prénom**, le **Nom**, le numéro de **Téléphone mobile** et l'**Adresse e-mail**. Le QR Code de contact sera généré dans la colonne suivante en fonction de ces 4 champs.

```excel
=image("https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=BEGIN:VCARD%0AN:" & A3 & "%20" & B3 & "%0ATEL;CELL:" & C3 & "%0AEMAIL:" & D3 & "%0AEND:VCARD")
```

Ensuite, une autre personne peut scanner le QR code généré pour ajouter les coordonnées à son téléphone.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_fZzgOk0-Mc-zTzc3lCuGzA.jpeg align="left")

*Les nouvelles versions d'iOS et d'Android sont équipées d'un scanner de QR Code en mode caméra*

Après le scan, il suffit de cliquer sur « Enregistrer » pour ajouter les informations aux Contacts.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_tkEkTu94w7CBhVhMat1aCA.jpeg align="left")

*Scanner le QR code et enregistrer le contact*

Ce modèle de liste de QR Codes de contacts sera utile lorsque vous rencontrez de nouvelles personnes dans une équipe ou lors d'un salon et que vous souhaitez recueillir les coordonnées de tout le monde.

## Pour créer un QR Code de contact personnalisé unique

Allez sur [QR Code Generator](https://www.qr-code-generator.com/), et sélectionnez 'vCard' où vous pouvez personnaliser divers champs. N'oubliez pas de le tester, car certains champs n'autorisent pas les caractères spéciaux comme "," ou "@".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_q5Yxh3Yrq_XSweBRBOLKtg.png align="left")

[*https://www.qr-code-generator.com/*](https://www.qr-code-generator.com/)

Vous pouvez également ajouter ce QR code à vos cartes de visite et brochures marketing. Les clients et les professionnels peuvent ainsi facilement scanner et enregistrer vos coordonnées sur leurs téléphones mobiles.

# Aller sur un site web en scannant un QR Code

Les nouvelles versions d'iPhone et de téléphones Android sont équipées de la fonction de scan de QR code dans l'application caméra. Il suffit d'allumer la caméra et de survoler le QR Code pour le scanner. Ensuite, vous pouvez cliquer sur la fenêtre contextuelle pour accéder à l'URL du site web intégré.

Par exemple, essayez de scanner ce QR code :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_8Rk_gKSDJVfafeWiullsWw.jpeg align="left")

*URL web intégrée* [*https://www.qrcode-monkey.com*](https://www.qrcode-monkey.com)

## Pour créer vos propres QR Codes personnalisés

Je vais généralement sur [QR Code Monkey](https://www.qrcode-monkey.com/) pour créer des QR codes personnalisés. Il est convivial et **gratuit à utiliser**, et il y a plus d'options si vous souhaitez :

* ajouter une image de logo au milieu (ce peut être votre **logo d'entreprise** !)

* définir une couleur (pour suivre votre **identité corporative**)

* utiliser d'autres designs personnalisés

Ainsi, vous pouvez maintenant facilement créer des supports marketing avec un QR code du site web de votre entreprise.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_-_nSVy6PxwJ9XKzU1PZ9iA.png align="left")

*Supports marketing avec QR codes*

---

## QR Codes pour les cartes de visite et les brochures marketing

J'espère que les conseils ci-dessus sont utiles pour faire les choses de manière plus efficace et efficiente. Bonne chance pour vos efforts de marketing et de sensibilisation !

Merci d'avoir lu !