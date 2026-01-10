---
title: Alias Email – Comment Configurer une Adresse Email Professionnelle Gratuitement
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-10-12T22:26:51.000Z'
originalURL: https://freecodecamp.org/news/email-alias-set-up-a-professional-email-for-free
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Email-Alias-with-Gmail.png
tags:
- name: email
  slug: email
- name: gmail
  slug: gmail
seo_title: Alias Email – Comment Configurer une Adresse Email Professionnelle Gratuitement
seo_desc: "I needed to log in to AWS. But my main email address was rejected. Apparently\
  \ I'd done this in the past and the account had been irreversibly deleted. \nNo\
  \ reset option – just a message saying the account was permanently deleted:\n\n\
  There are about a mi..."
---

Je devais me connecter à AWS. Mais mon adresse email principale a été rejetée. Apparemment, j'avais déjà fait cela par le passé et le compte avait été supprimé de manière irréversible. 

Aucune option de réinitialisation – juste un message indiquant que le compte était définitivement supprimé :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-2.17.29-PM.png)

Il existe environ un million de façons d'obtenir une nouvelle adresse email, mais je voulais configurer l'un des domaines que je possède avec une adresse email. 

Et je me suis dit qu'il y aurait probablement un moyen de la rediriger vers mon Gmail. 

J'avais raison ! 

Dans ce guide rapide, je vais vous montrer :

* Comment créer un alias email
* Rediriger les emails de l'alias vers un compte Gmail
* Envoyer des emails en tant qu'alias email

## Comment Créer un Alias Email

J'utilise les produits Google : [Google Domains](https://domains.google.com/registrar/) et [Gmail](https://gmail.com/). Toutes ces étapes devraient s'appliquer généralement à d'autres services de domaine et d'email.

Tout d'abord, connectez-vous à votre fournisseur de domaine et sélectionnez le menu **Email**. Vous pourrez sélectionner "**Ajouter un alias email**" dans les options du menu. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-2.37.40-PM.png)

## Comment Rediriger les Emails vers une Autre Adresse

Remarque : si vous ajoutez le symbole astérisque (*), cela créera un alias générique qui redirigera tout email vers l'adresse spécifiée. Nous allons ajouter un alias spécifique dans ce tutoriel.

Ajoutez l'email de votre choix et entrez l'adresse vers laquelle vous souhaitez qu'il soit redirigé. Je vais rediriger **hi@sieis.com** vers mon adresse Gmail principale.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-2.41.16-PM.png)

Si vous utilisez les serveurs de noms Google, alors Google Domains configurera automatiquement les bons enregistrements de courrier (MX).

Sinon, vous devrez configurer ces enregistrements MX. Le processus est exactement le même que la configuration des serveurs de noms si vous l'avez déjà fait pour héberger votre site web ailleurs que là où vous avez acheté le domaine.

| Nom/Hôte/Alias | Type | Temps de vie (TTL) | Priorité | Valeur/Réponse/Destination      |
|-----------------|------|--------------------|----------|-------------------------------|
| Vide ou @       | MX   | 1H                 | 5        | gmr-smtp-in.l.google.com      |
| Vide ou @       | MX   | 1H                 | 10       | alt1.gmr-smtp-in.l.google.com |
| Vide ou @       | MX   | 1H                 | 20       | alt2.gmr-smtp-in.l.google.com |
| Vide ou @       | MX   | 1H                 | 30       | alt3.gmr-smtp-in.l.google.com |
| Vide ou @       | MX   | 1H                 | 40       | alt4.gmr-smtp-in.l.google.com |

Bonus : J'ai fait cela pour un site hébergé sur Netlify, et c'est très simple. Depuis le tableau de bord Netlify, sélectionnez **Options**, **Aller au panneau DNS**, puis entrez les enregistrements MX :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.42.25-PM.png)

👍

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.42.53-PM-2.png)

Google enverra un email de vérification unique ici, mais si vous avez déjà fait cette vérification, il se peut qu'il n'en envoie pas un autre.

Envoyez-vous un email depuis une adresse différente et vérifiez-le !

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.02.53-PM-1.png)
_Email envoyé à l'alias et redirigé vers le Gmail principal_

Remarque : l'envoi depuis votre adresse Gmail principale n'apparaît pas comme un message non lu comme cela serait normalement le cas lorsque vous vous envoyez un email. Envoyez-le depuis une adresse différente à ce stade. Après le reste des étapes, il se comportera normalement lorsque nous aurons terminé la partie "envoyer un email en tant qu'alias".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.04.35-PM.png)

## Comment Envoyer des Emails en tant qu'Alias

Si vous répondez depuis votre Gmail principal actuellement, le destinataire verra cette adresse lorsque vous répondrez au lieu de l'alias. Cela peut ne pas être un gros problème selon le cas d'utilisation, mais nous pouvons certainement le configurer pour que les emails envoyés semblent provenir du domaine personnalisé également.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.08.37-PM.png)

Vous devrez aller dans votre [**Compte Google Sécurité**](https://myaccount.google.com/security) et cliquer sur **Mots de passe d'application**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.12.46-PM.png)

Sélectionnez **Mail** dans le menu déroulant de l'application et **Autre** dans le menu déroulant de l'appareil.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.14.18-PM.png)

Entrez le nom de votre domaine et cliquez sur **Générer**. Il vous donnera un mot de passe de 16 chiffres. Enregistrez-le pour l'utiliser dans Gmail...

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.15.34-PM.png)

Dans Gmail, allez dans les paramètres -> **Comptes et Importation** et cliquez sur **Ajouter une autre adresse email**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.17.49-PM.png)

Cela fera apparaître une nouvelle petite fenêtre où vous devrez entrer les détails de l'alias. Entrez le **nom** que vous souhaitez que les destinataires voient et l'**adresse** de l'alias. Assurez-vous que la case "**Traiter comme un alias**" est cochée.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.21.46-PM.png)

À l'écran suivant, vous devrez changer le **serveur SMTP** en smtp.gmail.com, le **nom d'utilisateur** en votre nom d'utilisateur Gmail, puis coller le **mot de passe de 16 chiffres** que vous avez généré depuis la sécurité Google dans les étapes précédentes.

Le **port** doit être 587, et le bouton radial **TLS** doit être coché.

Cliquez sur **Ajouter un compte**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.23.33-PM.png)

Cela déclenchera l'envoi d'un code de vérification à l'alias email... qui devrait à son tour aller au compte Gmail. Entrez-le, et vous serez prêt à partir !

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.27.09-PM-1.png)

De retour dans notre fil de discussion email dans Gmail, vous aurez l'option de menu déroulant lors de la rédaction de nouveaux messages pour sélectionner le compte depuis lequel vous souhaitez l'envoyer.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.29.10-PM.png)

Maintenant, nous pouvons voir dans notre fil de discussion complet que notre email est redirigé vers et envoyé depuis notre compte Gmail en utilisant l'alias email et le nom d'affichage que nous avons sélectionnés.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-12-at-3.35.15-PM.png)

## Merci d'avoir lu !

Cela a été éclairant pour moi, et j'espère que cela sera utile pour vous aussi.

Venez dire bonjour sur Twitter : [https://twitter.com/EamonnCottrell](https://twitter.com/EamonnCottrell)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/goodtogo.gif)