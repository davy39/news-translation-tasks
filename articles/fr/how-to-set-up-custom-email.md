---
title: Comment configurer une adresse e-mail personnalisée avec Cloudflare et Mailgun
subtitle: ''
author: San B
co_authors: []
series: null
date: '2024-04-15T13:49:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-custom-email
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/boolfalse-gmail-manage-custom-email.png
tags:
- name: cloudflare
  slug: cloudflare
- name: email
  slug: email
seo_title: Comment configurer une adresse e-mail personnalisée avec Cloudflare et
  Mailgun
seo_desc: 'As a software engineer, you may consider having a professional email account
  along with your own website, like "info@example.com". But this may cost a certain
  amount that you''ll not be willing to pay.

  But do you know you can do it for free? There is ...'
---

En tant qu'ingénieur logiciel, vous pouvez envisager d'avoir un compte e-mail professionnel avec votre propre site web, comme "_info@example.com_" . Mais cela peut coûter un certain montant que vous ne serez pas prêt à payer.

Mais saviez-vous que vous pouvez le faire gratuitement ? Il existe en effet un moyen de le faire, et en plus du fait que l'avoir un compte e-mail professionnel est gratuit, cela vous aidera à être plus efficace, fiable et sécurisé dans votre travail quotidien.

Dans cet article, vous apprendrez comment créer et configurer votre propre adresse e-mail en utilisant Cloudflare et Mailgun pour gérer les e-mails dans Gmail. Cela signifie que vous pouvez envoyer et recevoir des e-mails directement dans votre boîte de réception Gmail.

Je l'ai déjà fait pour un usage personnel et j'ai pris des captures d'écran de tout le processus que vous verrez dans cet article. Je vais donc partager toutes les étapes nécessaires que vous devez suivre pour configurer votre propre e-mail.

Découvrons ce dont vous avez besoin avant de commencer, ce que vous allez faire et comment cela fonctionnera.

## Ce dont vous avez besoin avant de commencer

Je suppose que vous avez déjà un domaine, appelons-le "_votredomaine.com_" . Plus précisément, vous devez avoir la possibilité de connecter votre domaine avec Cloudflare et de configurer les enregistrements DNS là-bas. Un exemple classique est d'avoir un domaine sur un registre de domaines (comme GoDaddy, Namecheap), et d'ajouter votre domaine à Cloudflare en définissant les enregistrements DNS fournis par Cloudflare sur votre compte de registre de domaines.

L'ajout d'un domaine à Cloudflare implique la mise à jour des serveurs de noms DNS de votre domaine pour pointer vers les serveurs de noms de Cloudflare. Une fois le domaine ajouté, Cloudflare agit comme un intermédiaire pour le trafic web, fournissant des fonctionnalités de sécurité comme la protection DDoS, le pare-feu et le chiffrement SSL, ainsi que des améliorations de performance grâce à la mise en cache et à l'optimisation du contenu.

Si vous ne l'avez pas encore fait, voici la vidéo officielle [vidéo sur YouTube](https://www.youtube.com/watch?v=7hY3gp_-9EU) sur la façon de connecter votre domaine à Cloudflare.

De plus, Cloudflare gère les enregistrements DNS de votre domaine, vous permettant de contrôler comment le trafic est routé et assurant une livraison fiable des services comme l'e-mail. 
Notre travail dans cet article se concentrera exactement sur cela : comment configurer votre domaine sur Cloudflare Email.

[Cloudflare Email](https://blog.cloudflare.com/email-routing-leaves-beta/) est l'un des services de Cloudflare depuis 2021, qui peut être utilisé gratuitement (du moins pour l'instant).

La deuxième hypothèse est que vous avez un compte Gmail et que vous avez accès à ses paramètres de messagerie. Simplement, si vous avez juste un e-mail régulier "_votreemail@gmail.com_" , qui n'est pas sous le contrôle d'un administrateur, alors vous n'avez rien à craindre. Nous explorerons et travaillerons sur les paramètres de messagerie plus tard.

## Ce que vous allez faire

En termes simples, vous allez créer un e-mail personnalisé comme "_quelquechose@votredomaine.com_" , que vous pourrez utiliser pour envoyer et recevoir des e-mails en utilisant la plateforme de Gmail. Vous recevrez et lirez donc les e-mails envoyés à "_quelquechose@votredomaine.com_" dans Gmail, ainsi que l'envoi d'e-mails à partir de cet e-mail personnalisé en utilisant Gmail.

Vous utiliserez Cloudflare Email pour le routage des e-mails et le serveur SMTP de Mailgun pour l'envoi des e-mails.

## Comment cela fonctionnera

Lorsque vous composez un e-mail depuis Gmail avec l'expéditeur défini comme "_quelquechose@votredomaine.com_" , Gmail utilise le serveur SMTP de Mailgun via les identifiants fournis, transmettant l'e-mail. Mailgun traite ensuite le message et le transfère au serveur de messagerie du destinataire, impliquant probablement des recherches DNS pour trouver le serveur du destinataire.

Les e-mails envoyés à "_quelquechose@votredomaine.com_" sont reçus par les serveurs de messagerie de Cloudflare, configurés via les enregistrements MX dans les paramètres DNS du domaine. Cloudflare stocke les e-mails reçus dans le compte associé, accessible via Gmail, qui se connecte périodiquement aux serveurs de Cloudflare (en utilisant les protocoles IMAP ou POP3) pour récupérer les nouveaux messages, permettant un accès transparent aux e-mails entrants.

## Routage des e-mails sur Cloudflare

> Le routage des e-mails de Cloudflare est conçu pour simplifier la manière dont vous créez et gérez les adresses e-mail, sans avoir besoin de surveiller des boîtes aux lettres supplémentaires. Avec le routage des e-mails, vous pouvez créer autant d'adresses e-mail personnalisées que vous le souhaitez pour les utiliser dans des situations où vous ne souhaitez pas partager votre adresse e-mail principale, comme lorsque vous vous abonnez à un nouveau service ou à une newsletter. Les e-mails sont ensuite acheminés vers votre boîte de réception e-mail préférée, sans que vous ayez jamais à exposer votre adresse e-mail principale. ([Documentation Cloudflare](https://developers.cloudflare.com/email-routing/))

Connectez-vous à votre compte Cloudflare et accédez au tableau de bord. 
Choisissez et cliquez sur le site web souhaité. Pour moi, c'est "_boolfalse.com_" , car je veux créer un e-mail personnalisé comme "_email@boolfalse.com_" .

![Image](https://www.freecodecamp.org/news/content/images/2024/04/01-dashboard.png)
_Cloudflare : Sites web_

Accédez à **Routage des e-mails** pour le site sélectionné.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/02-email-routing.png)
_Cloudflare : Routage des e-mails_

Si vous n'avez pas configuré le routage des e-mails, vous pouvez voir quelque chose de similaire à la capture d'écran ci-dessus. Cliquez sur "Commencer". Vous pourrez peut-être créer votre propre adresse pour recevoir des e-mails et prendre des mesures.

Nous allons sauter cette étape sans créer notre propre adresse car nous allons le faire manuellement.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/03-skip-custom-address.png)
_Cloudflare : E-mail personnalisé_

Par défaut, le routage des e-mails est désactivé, vous devez donc l'activer. Cliquez sur le lien pour accéder à la page **Routage des e-mails** .

![Image](https://www.freecodecamp.org/news/content/images/2024/04/04-enable-email-routing.png)
_Cloudflare : Routage des e-mails_

Soumettez-le en cliquant sur "Activer le routage des e-mails".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/05-email-dns-records-enable-email-routing.png)
_Cloudflare : Activer le routage des e-mails_

Vous devez avoir trois enregistrements MX et un enregistrement TXT :

* Type : _**MX**_ ; Nom : _**@**_ ; Serveur de messagerie : _**route1.mx.cloudflare.net**_ ; TTL : **_Auto_** ; Priorité : _**69**_
* Type : _**MX**_ ; Nom : _**@**_ ; Serveur de messagerie : _**route2.mx.cloudflare.net**_ ; TTL : **_Auto_** ; Priorité : **_99_**
* Type : _**MX**_ ; Nom : **_@_** ; Serveur de messagerie : _**route3.mx.cloudflare.net**_ ; TTL : **_Auto_** ; Priorité : **_40_**
* Type : _**TXT**_ ; Nom : _**@**_ ; TTL : **_Auto_** ; Contenu : **_v=spf1 include:_spf.mx.cloudflare.net ~all_**

Vous pouvez les voir en bas de la page **Routage des e-mails** .

![Image](https://www.freecodecamp.org/news/content/images/2024/04/06-required-dns-records.png)
_Cloudflare : Enregistrements DNS pour le routage des e-mails_

Donc, comme déjà dit, dans le menu de gauche, allez dans "DNS" -> "Enregistrements" et ajoutez les enregistrements suivants.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/06-dns-records-added-2.png)
_Cloudflare : Enregistrements DNS ajoutés_

Après avoir créé ces enregistrements, retournez à la page **Routage des e-mails** .

Ici, vous devez uniquement avoir les enregistrements que vous venez de créer. Donc, si vous avez d'autres enregistrements, supprimez-les simplement.

Par exemple, j'avais déjà une entrée inutile que je devrais supprimer.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/07-unnecessary-dns-records.png)
_Cloudflare : enregistrements existants pour le routage des e-mails_

Soumettez pour supprimer les enregistrements DNS existants inutiles.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/08-delete-existing-dns-records.png)
_Cloudflare : suppression des enregistrements inutiles_

Après avoir supprimé les enregistrements DNS inutiles, vous ne verrez que ceux dont vous avez besoin.

Vous pourrez maintenant activer le routage des e-mails en cliquant sur le bouton "Ajouter des enregistrements et activer".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/09-enabling-email-routing.png)
_Cloudflare : Activer le routage des e-mails_

Après l'avoir activé, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/10-email-routing-enabled.png)
_Cloudflare : Enregistrements DNS des e-mails configurés_

## Comment créer un e-mail personnalisé sur Cloudflare

Maintenant, allez dans l'onglet **Routes** et créez un e-mail en cliquant sur le bouton "Créer une adresse".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/11-email-routing-routes-tab.png)
_Cloudflare : Routage des e-mails (activé)_

Dans cet exemple, nous allons créer l'adresse e-mail "_email@boolfalse.com_" en ajoutant "_email_" comme adresse personnalisée, et une adresse e-mail de destination, où je pourrai recevoir des e-mails.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/12-creating-email-address.png)
_Cloudflare : Routage des e-mails_

Vous devriez voir une notification à ce sujet.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/13-email-address-created.png)
_Cloudflare : création d'un e-mail personnalisé_

Vous devriez également recevoir un e-mail pour confirmer cette action.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/14-getting-confirmation-email.png)
_Vérification de l'adresse e-mail de destination_

Continuez et vérifiez l'adresse e-mail.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/15-verify-email-address.png)
_Vérifier l'adresse e-mail_

Une fois que vous avez vérifié l'adresse e-mail, vous pouvez obtenir cette page :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/16-email-address-verified.png)
_Cloudflare : l'adresse e-mail personnalisée est vérifiée_

Vous recevrez probablement un e-mail confirmant que vous avez vérifié votre domaine avec Mailgun :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/36-mailgun-domain-verified-2.png)
_Notification de vérification de l'adresse e-mail personnalisée_

## Comment recevoir des e-mails dans l'e-mail personnalisé

Maintenant, votre adresse e-mail est activée et vous pouvez le voir ici :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/17-email-address-activated.png)
_Cloudflare : l'adresse e-mail personnalisée est active_

À ce stade, vous pouvez envoyer des e-mails à l'e-mail personnalisé que vous venez de configurer. Dans ce cas, il s'agit de "_email@boolfalse.com_" .

Ci-dessous se trouve un e-mail de test envoyé depuis une autre adresse e-mail.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/18-test-email-sending-1.png)
_Test de réception d'e-mails_

Vous recevrez un e-mail de test à l'adresse e-mail personnalisée.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/19-test-email-received.png)
_L'e-mail de test a été reçu_

## Mailgun : Ajout d'un nouveau domaine

Vous pouvez maintenant recevoir des e-mails avec succès, mais vous ne pouvez pas encore envoyer d'e-mails depuis cet e-mail personnalisé.

Il est donc temps de passer au fournisseur de services de messagerie. Dans notre cas, il s'agira de [Mailgun](https://www.mailgun.com/). 
Pour ce faire, vous devez simplement vous inscrire et attacher la carte à votre compte Mailgun. Après avoir activé votre compte avec la carte attachée, vous pouvez configurer un domaine pour votre e-mail.

Vous n'avez pas à vous soucier de la carte, car Mailgun ne facture pas pour des quantités limitées. Je pense que le montant qu'il donne est tout à fait adapté pour un forfait gratuit. 
Vous pouvez trouver les forfaits de prix en détail [ici](https://www.mailgun.com/pricing/).

Accédez à la page **Envoi** -> **Domaines** et cliquez sur le bouton "Ajouter un nouveau domaine".

Dans notre cas, il s'agira de "_mg.boolfalse.com_" , car Mailgun recommande cela pour pouvoir envoyer des e-mails depuis votre domaine racine, c'est-à-dire : "_email@boolfalse.com_" .

Vous devriez voir cette recommandation à droite dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/24-mailgun-adding-domain.png)
_Mailgun : créer un nouveau domaine_

Vous pouvez également sélectionner la région du domaine et la longueur de la clé DCIM, mais vous pouvez tout laisser par défaut. 
Je vais laisser la longueur de la clé DCIM à 1024 et "US" comme région de domaine.

Après avoir créé le domaine, vous pouvez voir des conseils sur la façon de vérifier votre domaine.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/23-add-new-domain-2.png)
_Mailgun : ajout d'un nouveau domaine_

Mailgun vous fournira deux enregistrements TXT, deux enregistrements MX et un enregistrement CNAME à ajouter à votre fournisseur.

* Type : _**TXT**_ ; Nom : _**mailto._domainkey.mg.boolfalse.com**_ ; TTL : **_Auto_** ; Contenu : **_<SECRET>_**
* Type : _**TXT**_ ; Nom : _**mg.boolfalse.com**_ ; TTL : **_Auto_** ; Contenu : **_v=spf1 include:mailgun.org ~all_**
* Type : _**MX**_ ; Nom : _**mg.boolfalse.com**_ ; Serveur de messagerie : _**mxa.mailgun.org**_ ; TTL : **_Auto_** ; Priorité : _**10**_
* Type : _**MX**_ ; Nom **_mg.boolfalse.com_** ; Serveur de messagerie : _**mxb.mailgun.org**_ ; TTL : **_Auto_** ; Priorité : **_10_**
* Type : **_CNAME_** ; Nom : **_email_** ; Cible : **_mailgun.org_** ; TTL : **_Auto_** ; État du proxy : **_On_**

Dans notre cas, nous allons les ajouter à Cloudflare.

Ci-dessous se trouve le premier enregistrement TXT :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/27-mailgun-dns-record-1-new.png)
_Mailgun : premier enregistrement TXT pour un nouveau domaine_

Ci-dessous se trouve le deuxième enregistrement TXT :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/29-mailgun-dns-record-2-new.png)
_Mailgun : deuxième enregistrement TXT pour un nouveau domaine_

Ci-dessous se trouve le premier enregistrement MX :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/30-mailgun-dns-record-3.png)
_Mailgun : premier enregistrement MX pour un nouveau domaine_

Ci-dessous se trouve le deuxième enregistrement MX :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/31-mailgun-dns-record-4.png)
_Mailgun : deuxième enregistrement MX pour un nouveau domaine_

Après avoir ajouté deux enregistrements TXT et deux enregistrements MX, vous pouvez les vérifier en cliquant sur le bouton "Vérifier les enregistrements DNS".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/32-mailgun-checking-dns-records.png)
_Mailgun : vérification des enregistrements TXT et MX pour un nouveau domaine_

Enfin, ajoutez l'enregistrement CNAME.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/33-mailgun-dns-record-5-2.png)
_Mailgun : ajout d'un enregistrement CNAME pour un nouveau domaine_

Vous pouvez voir une icône d'avertissement à gauche de l'enregistrement CNAME. Vous n'avez pas à vous en soucier. Voici ce que dit la [documentation officielle](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages) à ce sujet :

> Si vous avez récemment [ajouté votre domaine](https://developers.cloudflare.com/fundamentals/setup/manage-domains/add-site/) à Cloudflare - ce qui signifie que votre zone est dans un [état en attente](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) - vous pouvez souvent ignorer cet avertissement. 
> Une fois que la plupart des domaines deviennent **Actifs**, Cloudflare émettra automatiquement un certificat SSL universel, qui fournira une couverture SSL/TLS et supprimera le message d'avertissement.

Après avoir ajouté un enregistrement CNAME, vous pouvez le vérifier à nouveau en cliquant sur le deuxième bouton "Vérifier les enregistrements DNS".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/34-mailgun-checking-dns-records.png)
_Mailgun : vérification de l'enregistrement CNAME pour un nouveau domaine_

Si vous avez ajouté les 5 enregistrements sur Cloudflare avec succès, après avoir cliqué sur le bouton de vérification, Mailgun vous redirigera automatiquement vers la page **Aperçu** .

![Image](https://www.freecodecamp.org/news/content/images/2024/04/36-mailgun-verified-1.png)
_Mailgun : 2 TXT, 2 MX et 1 enregistrement CNAME ajoutés pour un nouveau domaine_

Cela signifie que vous êtes prêt à ajouter une clé API d'envoi sur Mailgun.

## Mailgun : Clé API d'envoi et utilisateur SMTP

Accédez à la page **Envoi** -> **Paramètres du domaine** . Choisissez l'onglet **Clés API d'envoi** en haut. Vous ne verrez probablement aucune clé API là-bas. Vous devez simplement créer une nouvelle clé API d'envoi. 

Cliquez sur "Ajouter une clé d'envoi" dans le coin supérieur droit, et dans la fenêtre contextuelle, remplissez le nom de la clé que vous êtes sur le point de créer.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/37-mailgun-create-sending-api-key-1.png)
_Mailgun : création d'une clé API d'envoi_

Après avoir appuyé sur "Créer une clé d'envoi", vous obtiendrez la clé API secrète que vous devez copier et sauvegarder quelque part en sécurité. Après avoir sauvegardé la clé, vous pouvez simplement fermer la fenêtre contextuelle.

Vous devriez voir la clé créée listée :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/38-mailgun-sending-api-key-created.png)
_Mailgun : Clé API d'envoi créée_

Vous devez également créer un nouvel utilisateur SMTP dans le tableau de bord de Mailgun. 
Accédez à la page **Envoi** -> **Paramètres du domaine** . Choisissez l'onglet **Identifiants SMTP** en haut et cliquez sur le bouton "Ajouter un nouvel utilisateur SMTP" dans le coin supérieur gauche. Cela ouvrira une fenêtre contextuelle. 

Saisissez les identifiants de l'utilisateur. Dans notre cas, je vais créer un utilisateur avec le nom "email". Cela sera comme un login pour votre e-mail sur Gmail.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/41-mailgun-create-smtp-user.png)
_Mailgun : création d'un utilisateur SMTP_

Une fois que vous avez créé un utilisateur SMTP dans Mailgun, vous le verrez listé et un mot de passe pour cet utilisateur sera généré automatiquement. Pour obtenir ce mot de passe, copiez-le en cliquant sur le bouton "Copier" dans la notification contextuelle dans le coin inférieur droit.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/42-mailgun-smtp-user-created.png)
_Mailgun : Utilisateur SMTP créé_

Conservez cela dans un endroit sûr pour une utilisation future. Vous aurez besoin de ce login et de ce mot de passe pour vous authentifier sur Gmail.

Vous êtes maintenant prêt à configurer les paramètres de messagerie avec votre fournisseur de messagerie. Dans notre cas, nous allons le faire dans Gmail.

Ouvrez votre compte Gmail dans votre navigateur de bureau et accédez aux paramètres en cliquant sur l'icône des paramètres dans le coin supérieur droit et cliquez sur le bouton "Voir tous les paramètres".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/39-gmail-settings-page.png)
_Mailgun : nouveau domaine est vérifié_

## Authentification Gmail avec le serveur SMTP de Mailgun

Dans la page des paramètres de Gmail, choisissez l'onglet **Comptes et Importation** et cliquez sur "Ajouter une autre adresse e-mail" dans la section "Envoyer des e-mails en tant que" :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/40-gmail-add-another-email-2.png)
_Gmail : Paramètres_

Cela ouvrira une fenêtre contextuelle pour l'authentification. Utilisez le login et le mot de passe que vous venez d'obtenir en créant un utilisateur SMTP sur Mailgun. Assurez-vous de remplir correctement les identifiants.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/43-gmail-add-smtp-user.png)
_Gmail : authentifier un nouvel utilisateur en utilisant un serveur SMTP créé sur Mailgun_

Soumettez le formulaire en cliquant sur le bouton "Ajouter un compte". Il vous demandera probablement de sauvegarder le nom d'utilisateur/mot de passe dans votre navigateur. C'est à vous de décider.

Et la dernière chose importante ici : il vous demandera de vérifier l'ajout d'un compte.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/44-gmail-verify-account.png)
_Gmail : confirmation d'authentification pour un nouvel utilisateur_

Pour la vérification, l'e-mail de confirmation sera envoyé à votre e-mail principal.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/45-gmail-confirmation-code.png)
_Gmail : e-mail de vérification d'authentification_

Vous pouvez soit utiliser le code de confirmation pour le vérifier en utilisant la fenêtre contextuelle, soit simplement suivre le lien fourni dans l'e-mail de confirmation.

Dans ce cas, nous allons cliquer sur un lien qui ouvrira la page où vous serez invité à confirmer. Cliquez sur "Confirmer" et fermez simplement la fenêtre contextuelle précédemment ouverte sans vous inquiéter.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/47-gmail-adding-user-confirmed.png)
_Gmail : vérification de l'authentification_

Vous êtes maintenant prêt à envoyer et recevoir des e-mails depuis l'e-mail personnalisé que vous venez de créer.

Pour envoyer un e-mail depuis l'e-mail personnalisé, vous devez simplement choisir cet e-mail comme e-mail de l'expéditeur :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/49-gmail-send-emails-from-custom-email.png)
_Gmail : envoi d'e-mails_

**C'est tout !**

Une chose supplémentaire qui peut vous être utile est que vous pouvez définir l'adresse e-mail personnalisée que vous venez de créer comme adresse par défaut pour l'envoi d'e-mails depuis Gmail.

Vous pouvez définir cela dans la page des paramètres dans la section "Envoyer des e-mails en tant que" :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/48-gmail-another-email-default.png)
_Gmail : Paramètres (expéditeur par défaut)_

J'espère que ce guide sera une bonne ressource pour configurer votre e-mail personnalisé.

## **Conclusion**

Dans cet article, vous avez appris comment configurer votre propre e-mail pour gérer les e-mails dans Gmail en utilisant Cloudflare Email et Mailgun.

En conclusion, il est intéressant de noter que le choix des outils n'est pas obligatoire, d'autres outils peuvent être utilisés à la place, mais l'idée de base et la logique seront similaires.

Vous pouvez consulter mon site web à l'adresse : [**boolfalse.com**](https://boolfalse.com/)

N'hésitez pas à partager cet article. 😇