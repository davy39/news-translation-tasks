---
title: Qu'est-ce que SendGrid ? Tutoriel sur les newsletters par e-mail SMTP
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-05-14T20:31:30.000Z'
originalURL: https://freecodecamp.org/news/what-is-sendgrid-smpt-email-newsletter-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/pexels-rakicevic-nenad-1262304.jpg
tags:
- name: communication
  slug: communication
- name: email
  slug: email
- name: newsletters
  slug: newsletters
seo_title: Qu'est-ce que SendGrid ? Tutoriel sur les newsletters par e-mail SMTP
seo_desc: 'You may have heard of the term SMTP before, and wondered what it is. SMTP
  is a common method for handling email messages.

  Today I am going to explain what SMTP is, and how to use an SMTP provider such as
  SendGrid to send emails from your address.

  Wha...'
---

Vous avez peut-être déjà entendu le terme SMTP et vous vous êtes demandé ce que c'était. Le SMTP est une méthode courante de gestion des messages électroniques.

Aujourd'hui, je vais expliquer ce qu'est le SMTP et comment utiliser un fournisseur SMTP tel que [SendGrid](https://sendgrid.com) pour envoyer des e-mails depuis votre adresse.

## Qu'est-ce que le SMTP ?

Le SMTP, ou Simple Mail Transfer Protocol, est la méthode par laquelle les serveurs Internet envoient des messages électroniques. Lorsque vous envoyez un e-mail via votre compte Gmail, par exemple, votre client de messagerie utilise le SMTP pour envoyer ce message au serveur. Le serveur utilise ensuite également le SMTP pour l'envoyer au serveur de réception.

Sans trop entrer dans les détails techniques, la façon la plus simple de le voir est que le SMTP est un serveur de messagerie.

## Qu'est-ce que SendGrid ?

SendGrid est un fournisseur de services SMTP – en fait, c'est le fournisseur que freeCodeCamp utilise pour envoyer la newsletter hebdomadaire de Quincy.

Comme de nombreux fournisseurs SMTP, SendGrid propose l'utilisation de ses serveurs de messagerie pour envoyer vos e-mails. C'est une excellente option pour envoyer de gros volumes d'e-mails, là où le faire manuellement prendrait beaucoup de temps et d'efforts.

### Comment créer un compte SendGrid

La première étape pour utiliser les services de SendGrid est de créer votre compte. Rendez-vous sur le [site web de SendGrid](https://sendgrid.com) pour vous inscrire. Ils proposent plusieurs modèles de tarification, mais le niveau gratuit sera suffisant, au moins pour ce tutoriel.

Cependant, à mesure que votre liste de diffusion s'agrandit, vous pourriez avoir besoin de fonctionnalités supplémentaires provenant d'un niveau d'abonnement supérieur.

Une fois connecté, vous devriez voir une vue par défaut du tableau de bord :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-4.png)
_Image illustrant la vue par défaut du tableau de bord SendGrid._

### Comment configurer votre domaine ou votre e-mail avec SendGrid

Depuis cette vue du tableau de bord, sélectionnez "Settings", puis choisissez "Sender Authentication" dans le menu déroulant. Les paramètres de Sender Authentication sont l'endroit où vous indiquez à SendGrid quels comptes de messagerie sont autorisés à envoyer des e-mails.

Il y a deux approches ici : si vous avez un domaine personnalisé pour vos e-mails, vous pouvez configurer la Domain Authentication. Si vous utilisez une adresse e-mail personnelle, comme une adresse Gmail, vous devrez alors configurer la Single Sender Authentication.

Choisissez l'option qui vous convient le mieux et suivez les instructions de SendGrid pour la configurer. Votre résultat final devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-5.png)
_Image illustrant les paramètres de Sender Authentication._

### Comment envoyer des e-mails via l'API de SendGrid

Le processus réel d'envoi des e-mails se fait via [l'API de SendGrid](https://sendgrid.com/docs/api-reference/). Mais avant de pouvoir utiliser l'API, vous devrez configurer une clé API.

Depuis la vue de votre tableau de bord, sélectionnez "Settings", puis sélectionnez "API Keys". Choisissez "Create API Key" et sélectionnez les autorisations que vous souhaitez que la clé possède (j'ai donné à la mienne toutes les autorisations, juste pour éviter les problèmes).

Une fois que vous avez la clé, enregistrez-la en lieu sûr car vous ne pourrez plus y accéder.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-6.png)
_Image illustrant la page des paramètres des API Keys._

Maintenant que vous avez la clé API, vous devrez configurer le code pour utiliser le point de terminaison `/mail/send`. Vous pouvez écrire le code manuellement ou utiliser l'une des bibliothèques d'aide telles que le [paquet Node.js](https://github.com/sendgrid/sendgrid-nodejs) de SendGrid.

Lors de l'utilisation du paquet Node.js, vous définissez les valeurs de votre e-mail comme suit :

* `to` : L'adresse à laquelle envoyer l'e-mail.
* `from` : L'adresse depuis laquelle envoyer l'e-mail. Cela doit correspondre à vos paramètres dans la Sender Authentication.
* `subject` : L'objet de votre e-mail.
* `text` : Le contenu de votre e-mail, si vous envoyez un e-mail au format texte brut.
* `html` : Le contenu de votre e-mail, si vous envoyez un e-mail au format HTML.

Les propriétés d'un appel API brut sont différentes, tout comme les propriétés des autres bibliothèques d'aide. Assurez-vous de vous référer à la documentation pour votre approche spécifique.

### Comment utiliser les modèles dynamiques dans SendGrid

Comme option alternative, au lieu d'envoyer le contenu de l'e-mail dans votre appel API, vous pouvez utiliser un Dynamic Template (modèle dynamique) pour générer le contenu.

Un Dynamic Template vous permet de définir le contenu des e-mails à envoyer et offre la fonctionnalité Handlebars pour remplacer des champs de données spécifiques.

Pour créer un Dynamic Template, depuis votre tableau de bord, sélectionnez "Email API" puis "Dynamic Templates". Cliquez ensuite sur "Create a Dynamic Template" – vous devriez voir votre modèle apparaître ci-dessous.

Cliquez dessus, puis sélectionnez "Add Version" pour ouvrir la sélection de modèles. Choisissez le modèle vierge, puis sélectionnez le type d'éditeur que vous souhaitez utiliser (j'utilise l'éditeur de code).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-7.png)
_Image illustrant l'éditeur._

Vous pouvez écrire le contenu de votre e-mail et utiliser des espaces réservés tels que `{{name}}` pour les données dynamiques. Ces espaces réservés recevraient des valeurs via vos appels API lorsque vous envoyez les e-mails.

Si vous voulez voir comment cela s'afficherait, vous pouvez utiliser l'onglet "Test Data" pour ajouter des données d'exemple pour les espaces réservés.

### Comment obtenir les blocages/rebonds/spams via l'API de SendGrid

Il est important de suivre les e-mails non distribuables. SendGrid propose des outils pour vous aider à suivre cela, et ces données sont disponibles via trois vues de tableau de bord différentes (ou points de terminaison d'API, si vous souhaitez analyser les données par programmation).

* Les e-mails `Blocked` (bloqués) sont des e-mails qui ont été rejetés par les politiques du fournisseur de messagerie de réception, comme les e-mails universitaires qui n'acceptent pas le trafic externe, ou les e-mails qui n'ont pas pu être résolus (le serveur de messagerie n'a pas été trouvé).
* Les e-mails `Bounced` (rebondis) sont des e-mails qui ont été reçus par le serveur mais renvoyés. Cela se produit dans les cas où le serveur de messagerie existe, mais pas l'utilisateur spécifique, ou si la boîte de réception est pleine.
* Les e-mails `Spam` sont sans doute les plus importants à surveiller, car ils sont générés lorsqu'un utilisateur reçoit votre e-mail et signale à son fournisseur que votre e-mail est un spam. Ceux-ci impactent directement votre réputation en tant qu'expéditeur, il est donc impératif de ne pas envoyer d'e-mail à quelqu'un qui a marqué vos e-mails précédents comme spam.

### Autres préoccupations

En parlant de votre réputation d'expéditeur, SendGrid propose une métrique de haut niveau appelée "Sender Reputation". Cette métrique est une agrégation de votre activité sur leur plateforme et aide à donner une idée générale de la manière dont les fournisseurs de messagerie sont susceptibles de traiter vos e-mails.

Une réputation plus faible entraînera le marquage automatique de vos e-mails comme spam, ou même le blocage de vos adresses IP.

Si vous êtes sur le niveau gratuit de SendGrid, vous utiliserez des adresses IP partagées. Cela signifie que d'autres clients enverront également des e-mails via cette même IP, et leurs actions peuvent avoir un impact négatif sur votre réputation.

Si vous avez l'intention d'envoyer de gros volumes d'e-mails, je vous recommande d'acheter des adresses IP dédiées pour garantir la protection de votre réputation.

## Conclusion

J'espère que cet article vous a aidé à vous familiariser avec SendGrid et les services qu'ils proposent. Vous devriez maintenant être prêt à commencer à envoyer vos propres e-mails.

Si vous prévoyez de lancer une newsletter par e-mail, j'ai écrit un article sur la [création de newsletters par e-mail efficaces](https://www.freecodecamp.org/news/how-to-create-an-email-newsletter-design-layout-send/) qui pourrait vous aider.