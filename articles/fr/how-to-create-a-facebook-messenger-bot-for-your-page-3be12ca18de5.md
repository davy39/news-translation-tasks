---
title: Comment créer un bot Facebook Messenger pour votre page
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T17:12:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-facebook-messenger-bot-for-your-page-3be12ca18de5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q5N9wNLQUAl3tnqHbmHWwQ.png
tags:
- name: AI
  slug: ai
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un bot Facebook Messenger pour votre page
seo_desc: 'By Paul Pinard

  When it comes to sharing your chatbot, Facebook Messenger is a must. We created
  a very easy step-by-step integration process for our platform users. Let’s dive
  in!

  In fact, we realized many companies immediately put their bots on Faceb...'
---

Par Paul Pinard

Quand il s'agit de partager votre chatbot, Facebook Messenger est un must. Nous avons créé un processus d'intégration étape par étape très simple pour les utilisateurs de notre plateforme. Plongeons-nous dedans !

En fait, nous avons réalisé que de nombreuses entreprises mettent immédiatement leurs bots sur Facebook une fois en production, car c'est clairement le moyen le plus convivial et le plus simple pour un client de contacter une entreprise.

Un chatbot Facebook présente de nombreux avantages :

* Disponibilité 24/7
* 100% de réponses
* Réponses instantanées (pensez à votre _taux de réponse_ !)
* Les tâches fastidieuses sont automatisées

Sur la plateforme SAP Conversational AI, nous avons créé un processus d'intégration étape par étape pour nos utilisateurs, afin que cela ne prenne que quelques minutes pour révéler votre chatbot à vos abonnés Facebook. Plongeons-nous dedans !

### Étape 1 : Préparez votre chatbot

Tout d'abord, vous aurez besoin d'un chatbot (cela semble légitime, n'est-ce pas ?!). Notez que une fois votre chatbot en ligne sur Facebook, vous pourrez le modifier, et toute modification que vous y apporterez apparaîtra dans votre chat Messenger.

Pour les besoins de ce tutoriel, nous n'aborderons pas la création d'un chatbot. Au lieu de cela, je vous invite chaleureusement à [créer votre compte](https://cai.tools.sap/signup) (c'est complètement gratuit !) et à [lire notre tutoriel](https://medium.freecodecamp.org/how-to-build-your-first-chatbot-with-the-sap-conversational-ai-9a1a2bd44e3c).

Une fois que votre « chatbot qui raconte des blagues » (ou ce que vous avez construit) est prêt, revenez ici !

### Étape 2 : Préparez votre page Facebook

Votre chatbot ne sera disponible pour l'intégration que sur une **page Facebook** (et non sur votre profil personnel). Cela signifie que vous devez créer une page Facebook ou avoir en tête celle que vous utiliserez. Supposons que votre entreprise, votre activité ou votre groupe dispose déjà d'une page. (Si ce n'est pas le cas, cliquez sur [ce lien](https://www.facebook.com/bookmarks/pages) et créez-en une.)

Comme je l'ai dit dans l'introduction, avoir un chatbot sur une page Facebook automatisera les messages privés une fois qu'il est connecté à votre page. Ainsi, si vous décidez de supprimer le chatbot, vous reviendrez immédiatement aux conversations traditionnelles de personne à personne (ce qui signifie que rien ne se passera lorsque les utilisateurs entreront un message jusqu'à ce que vous y répondiez manuellement).

### Étape 3 : Créez une application Facebook Messenger

Créer une application aidera à établir la **connexion entre SAP Conversational AI et votre page Facebook**. Sans cette application, vous ne pourrez pas publier votre chatbot sur votre page Facebook.

Cliquez sur ce lien, choisissez _Mes applications_ dans le menu supérieur, puis _Ajouter une nouvelle application_.

![Image](https://cdn-media-1.freecodecamp.org/images/PeVCMeylF1uf-IiqZrC2XUDMF1LWji-Id-BA)

Une fois votre application créée, vous devrez ajouter un « produit » Messenger.

Il existe de nombreuses tâches pour lesquelles une application Facebook peut être dédiée, mais nous voulons spécifiquement une application de messagerie privée. Allez dans le tableau de bord de votre application et cliquez sur _Configurer_ dans la boîte _Messenger_.

![Image](https://cdn-media-1.freecodecamp.org/images/alQcAGzqHcXP0aGvcCNyzBN1JFMgdNCkafai)

Dans le menu de gauche, vous verrez alors _Messenger_ sous _PRODUITS_.

### Étape 4 : Obtenez votre jeton de page et le secret de l'application

Maintenant que nous avons créé une application Messenger, nous devons la lier à votre page Facebook (par défaut, une application Facebook est une entité indépendante). Avec cette connexion, vous recevrez un jeton, qui est essentiellement un code unique qui dit « OK, voici le code de l'application Messenger de la page X ».

Dans le menu de gauche, cliquez sur _Paramètres_ juste en dessous du produit _Messenger_.

![Image](https://cdn-media-1.freecodecamp.org/images/YAYFtBF9SLnId6tm51ImbksdfubG0hlbX0xK)

Choisissez la page sur laquelle vous souhaitez que votre chatbot apparaisse.

Pour des raisons de sécurité, vous devrez probablement autoriser l'application à interagir avec votre page Facebook. Cliquez sur le bouton bleu _Modifier les autorisations_, sélectionnez votre page et cochez les différentes cases.

Une fois les autorisations accordées, un jeton sera généré.

![Image](https://cdn-media-1.freecodecamp.org/images/LOSgIcffDSDDT2S7aEKA1POo6-X0DRc4MuqL)

Retournez à l'onglet _Connecter_ dans votre chatbot SAP Conversational AI, choisissez _Messenger_ et collez votre jeton dans le champ _Jeton de page_ à l'étape 4.

**Hourra, nous sommes à mi-chemin !** Obtenons maintenant notre « secret d'application », qui est comme un mot de passe pour votre application.

Dans le menu de gauche, allez dans _Paramètres_ > _Basique_.

![Image](https://cdn-media-1.freecodecamp.org/images/ihFc65y1uMs6SXh5ArP9CNJDc55XrT82opCN)

Pour des raisons de confidentialité, le secret de l'application est masqué. Cliquez sur _Afficher_ et copiez-le dans le champ _Secret de l'application_ de l'onglet _Connecter_ de votre chatbot (similaire à ce que vous venez de faire avec le jeton de page).

Cliquez sur _Mettre à jour le canal_ sous le formulaire SAP Conversational AI.

### Étape 5 : Connectez SAP Conversational AI à votre application

Il est temps de connecter notre plateforme à Messenger !

Sur la page _Produits_ > _Messenger_ > _Paramètres_, allez dans la section _Webhooks_ et cliquez sur _S'abonner aux événements_.

![Image](https://cdn-media-1.freecodecamp.org/images/BNzlSqmuJyI4uUsnB4xDeURV5AWJF958r9JR)

Dans la fenêtre contextuelle, entrez les valeurs pour _URL de rappel_ et _Jeton de vérification_ que vous trouverez à l'étape 4 de l'onglet _Connecter_ de votre chatbot.

![Image](https://cdn-media-1.freecodecamp.org/images/ApENnguDSN3hUUxXMn3EfjToXZwRnDowRPdT)

Cochez également les cases affichées ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/BNecL0jhzxHxfxJJ9k7fKSYnYR0duMCpgjcs)

Une fois votre page rechargée, sélectionnez votre page dans la liste afin qu'elle puisse accéder à votre webhook.

### Étape 6 : Testez et publiez le chatbot Messenger

Maintenant, **vous pouvez tester votre bot en tant qu'administrateur** (vous pouvez également accorder certains rôles de test en utilisant _Rôles_ > _Utilisateurs de test_ dans le menu de gauche). Votre bot ne sera pas accessible au public tant que vous ne changerez pas le statut, **prenez donc votre temps pour le tester et vous assurer que tout est parfait avant de le publier !**

![Image](https://cdn-media-1.freecodecamp.org/images/wadmMwha2ugHb63V7qmaoW75BK-8F4O8Ou4H)

Une fois que vous êtes satisfait de votre bot, si vous changez le bouton bascule sur _ON_ (dans le coin supérieur droit), vous serez redirigé vers les paramètres et invité à fournir quelques informations supplémentaires avant que votre bot ne soit publié. (Astuce : Vous pouvez également accéder aux paramètres sous _Paramètres_ > _Basique_ dans le menu de gauche.)

![Image](https://cdn-media-1.freecodecamp.org/images/2Kb-lvORz10FyneB-VlZM-wXL155lwmc1t5W)

Toute dernière étape : Facebook voudra vérifier et tester votre chatbot Messenger. Voici ce qu'ils disent à propos de cette étape dans leur documentation :

> _« Lorsque vous êtes prêt à publier votre bot pour le public, vous devez le soumettre à notre équipe pour examen et approbation. Ce processus de révision nous permet de nous assurer que votre bot Messenger respecte nos politiques et fonctionne comme prévu avant qu'il ne soit mis à la disposition de tous sur Messenger. » — Documentation Facebook_

Dans le menu de gauche, allez dans _Produits_ > _Messenger_ > _Paramètres_ et cliquez sur _Ajouter à la soumission_ dans le bloc _messagerie de la page_.

![Image](https://cdn-media-1.freecodecamp.org/images/0XcELdwF90OFhNryXq4PyKU-YHZmaZ5p2kz0)

Il ne faudra pas longtemps à l'équipe de révision de Facebook pour examiner votre bot et vous donner le feu vert pour le publier !

**Et voilà, c'est tout !**

J'espère que vous avez apprécié ce tutoriel. Et n'oubliez pas que vous êtes les bienvenus pour nous contacter si vous avez besoin d'aide, via la section des commentaires ci-dessous ou via [Stack Overflow](https://stackoverflow.com/questions/tagged/sap-conversational-ai).

Bonne construction de bot ?