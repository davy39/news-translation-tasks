---
title: Arrêtez les retours d'e-mails [Marketing] ! Comment configurer SPF, DMARC &
  DKIM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-22T17:10:52.000Z'
originalURL: https://freecodecamp.org/news/bananas-stop-email-bouncebacks-spf-dmarc-dkim
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/stop-email-bouncebacks-post-image.jpg
tags:
- name: Backend Development
  slug: backend-development
- name: '#content marketing'
  slug: content-marketing
- name: cybersecurity
  slug: cybersecurity
- name: 'Digital Marketing '
  slug: digital-marketing
- name: email
  slug: email
- name: email marketing
  slug: email-marketing
- name: newsletters
  slug: newsletters
- name: servers
  slug: servers
- name: smtp
  slug: smtp
seo_title: Arrêtez les retours d'e-mails [Marketing] ! Comment configurer SPF, DMARC
  & DKIM
seo_desc: 'By Andreas Lopez

  Setup Requirements:


  Your Domain Name System (DNS) Editor (i.e. GoDaddy Admin that has the email addresses
  registered)

  3rd Party e-mail Admin Accounts (e-mail Blast Service [Mailchimp, ConstantContact,
  etc.], Additional Mail Server y...'
---

Par Andreas Lopez

**Conditions préalables à l'installation :**

* Votre éditeur de système de noms de domaine (DNS) (c'est-à-dire l'administrateur GoDaddy où les adresses e-mail sont enregistrées)
* Comptes administrateur de messagerie tiers (service de messagerie de masse [Mailchimp, ConstantContact, etc.], serveur de messagerie supplémentaire que vous pourriez utiliser, etc.)

Vous lisez peut-être ceci parce que vous souhaitez obtenir de l'aide pour résoudre une erreur que vous venez de recevoir. Cette erreur pourrait indiquer quelque chose concernant vos enregistrements DMARC et que l'e-mail n'a pas été authentifié. Et très probablement, vous avez tenté d'envoyer un e-mail à quelqu'un avec une adresse @gmail.com ou @yahoo.com ou un autre fournisseur de messagerie gratuit et important qui a des directives par défaut plus strictes qu'un serveur de messagerie que vous configureriez via votre propre entreprise.

J'ai également été confronté à cette situation et j'ai mis un certain temps à comprendre non seulement ce dont vous avez besoin, mais aussi comment le faire correctement.

### Nos statistiques avant et après la configuration de SPF, DMARC & DKIM :

Comme vous pourrez le constater dans les images suivantes, ces implémentations nous montrent que :
* Le taux de rebond était de 70 % avant l'implémentation, soit 21 441 e-mails qui n'ont jamais atteint la boîte de réception des abonnés.
* Après l'implémentation, le taux de rebond n'était que de 5,6 %, soit seulement 1 855 retours.
* Les retours ne sont pas tous dus à des problèmes de sécurité, certains e-mails sont supprimés ou l'abonné a fait une faute de frappe (mail.com au lieu de gmail.com est un cas typique).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/ConstantContact-Before-After.jpg)
_Statistiques de rebond de Constant Contact, avant et après la configuration de SPF, DMARC & DKIM._

### Assez parlé de l'importance de l'implémentation, passons à l'action !

Pour être conforme à 100 % en termes d'authentification des e-mails, vous devez configurer trois éléments :

* **SPF (Sender Policy Framework)** : un cadre utilisé pour prévenir la contrefaçon d'e-mails, également connue sous le nom de spoofing. Le spoofing est lorsque quelqu'un prétend envoyer un e-mail depuis votre adresse e-mail.
* **DKIM (DomainKeys Identified Mail)** : Cela permettra à un serveur d'envoyer des e-mails en votre nom tout en étant authentifié pour s'assurer que c'est bien vous. Par exemple, si vous utilisez MailChimp ou ConstantContact pour des envois de newsletters et dites que cela provient de john@doecompany.com, les e-mails seront toujours envoyés depuis le serveur de MailChimp ou ConstantContact. Cependant, vous avez vérifié avec votre service d'envoi de newsletters que c'est bien vous et non quelqu'un qui prétend être vous. **C'est le plus important à configurer correctement pour les entreprises, sinon il y aura un taux de rebond élevé !**
* **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** : Un autre mécanisme anti-spoofing qui fonctionnera en conjonction avec SPF. Avoir l'un ou l'autre est inefficace, vous aurez besoin des deux pour être correctement protégé.

Éditeur DNS / Éditeur de zone DNS, exemples de captures d'écran GoDaddy (connectez-vous et accédez d'abord à votre tableau de bord d'administration) :

![Image](https://cdn-media-1.freecodecamp.org/images/0*RyXa5A0poh-LVZgw.png)
_Capture d'écran du tableau de bord de gestion des domaines GoDaddy avec une flèche pointant sur l'option Gérer. (1)_

![Image](https://cdn-media-1.freecodecamp.org/images/0*lPnjNy8Qd3T6d7lq.png)
_Capture d'écran du tableau de bord des domaines GoDaddy avec la flèche pointant sur l'option Gérer les zones. (1)_

Sélectionnez le domaine auquel vous devez ajouter les entrées DNS dans l'écran après avoir cliqué sur Gérer les zones.

![Image](https://cdn-media-1.freecodecamp.org/images/0*CK4w3j4dsw2ZE060.png)
_Capture d'écran du tableau de bord de l'éditeur de zone DNS GoDaddy avec une flèche pointant sur l'option Ajouter. (1)_

En bas de vos enregistrements, sur le côté droit, vous verrez un bouton Ajouter qui vous mènera au menu de dialogue suivant dans lequel vous entrerez les entrées SPF, DMARC & DKIM chacune individuellement :

![Image](https://cdn-media-1.freecodecamp.org/images/0*lZzVRpdjY3z0dq53.png)
_Capture d'écran du tableau de bord d'administration de l'entrée DNS GoDaddy avec le bouton pointant sur le bouton Enregistrer et TXT comme type, _dmarc comme Hôte et la valeur requise sous Valeur TXT mise en évidence. (1)_

Pour d'autres guides pour les éditeurs de zone, consultez simplement la base de connaissances/le centre de support de votre fournisseur de domaine.

### Configuration de SPF :

Le SPF est le plus facile à configurer. Vous aurez besoin de deux choses :

1. Votre éditeur DNS (c'est-à-dire le portail d'administration GoDaddy)
2. L'adresse IP de votre serveur de messagerie

Après avoir accédé à votre éditeur DNS (également appelé Éditeur de zone DNS dans CPanel), vous souhaitez créer une nouvelle entrée TXT. Dans cette entrée TXT, vous devriez avoir 3 champs possibles : Hôte, Valeur TXT / Valeur & TTL (Time-To-Live). Ce que vous entrerez dans ces champs est le suivant (certains détails peuvent varier, **cela est basé sur une installation GoDaddy**) :
Hôte : @
Valeur TXT : v=spf1 +a +mx +ip4:<ip de votre serveur de messagerie>~all
TTL : 1 heure

![Image](https://cdn-media-1.freecodecamp.org/images/1*5dQV9o1PaFDrABCi3ISHVg.png)
_Exemple d'entrée TXT DNS GoDaddy pour les paramètres SPF tels que décrits ci-dessus._

**Explication / Signification de ces paramètres :**

@ est la désignation au sein de GoDaddy qui fait référence au domaine dans lequel vous travaillez. Donc, si vous travaillez dans doecompany.com, vous pourriez remplacer @ par doecompany.com et le résultat serait le même. Cependant, il est préférable d'utiliser le symbole @ dans le cas de GoDaddy.

<ip de votre serveur de messagerie> est l'IP d'où vos e-mails sont envoyés. Cela n'est pas nécessairement la même IP que celle sur laquelle le site web est hébergé.

**+a :** Inclut l'enregistrement A

**+mx :** Inclut l'enregistrement du serveur de messagerie

**+ip4 :** Désigne depuis quel serveur IPv4

**~all :** Les enregistrements en dehors de ceux précédemment déclarés échoueront.

**TTL = 1 heure** (ou 3600 secondes) : Time-To-Live, ou la fréquence à laquelle cela devrait expirer. Si vous deviez changer de serveurs de messagerie, vous seriez content qu'il n'y ait qu'un maximum de 1 heure de non-authentification.

### Configuration de DKIM :

C'est le plus fastidieux des trois à configurer et le plus critique. Vous authentifierez le tiers pour envoyer au nom de votre adresse e-mail, par exemple john@doecompany.com.

J'ai actuellement 2 DKIM configurés :

1. Pour mon serveur de messagerie réel qui réside sur un serveur différent de mon site web réel (ce qui est plus courant dans les environnements d'entreprise).
2. Pour mon fournisseur de service d'envoi de newsletters par e-mail (ConstantContact dans ce cas, mais cela pourrait facilement être Mailchimp ou quelqu'un d'autre dans votre cas).

Pour les deux scénarios, votre travail est le même. Vous devrez contacter le support e-mail de votre serveur de messagerie ou de votre service tiers d'envoi d'e-mails et leur demander d'installer le DKIM de leur côté, pour votre compte.

Cela est complètement hors de votre contrôle et prend généralement 1 à 2 jours pour accomplir cette tâche. En gros, ce qui se passe, c'est qu'ils enregistreront et installeront un RSA d'au moins 1024 bits (2048 est mieux) sur leur serveur.

Après qu'ils l'aient configuré, ils vous enverront une clé publique que vous utiliserez dans l'étape suivante pour configurer votre enregistrement DKIM.

Tout comme pour les enregistrements SPF & DMARC, vous accéderez à votre éditeur DNS (également appelé Éditeur de zone DNS dans CPanel), et créerez une nouvelle entrée TXT. Dans cette entrée TXT, vous devriez avoir 3 champs possibles : Hôte, Valeur TXT / Valeur & TTL (Time-To-Live). Ce que vous entrerez dans ces champs est le suivant (certains détails peuvent varier, cela est basé sur une installation GoDaddy avec les e-mails hébergés sur inmotionhosting.com et ConstantContact comme service de newsletter). N'oubliez pas de faire 1 entrée séparée par enregistrement DKIM :
Hôte : <fournis par votre tiers>._domainkey
Valeur TXT : v=DKIM1; k=rsa; p=<clé publique>
TTL : 1 heure

Assurez-vous de ne pas laisser d'espaces après les symboles =.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nj_ycXzk_LsASRBfcw7b3A.png)
_Exemple d'entrée TXT DNS GoDaddy pour les paramètres DKIM tels que décrits ci-dessus._

**Explication / Signification de ces paramètres :**

L'hôte peut être un nom ou un nombre et est vraiment unique pour le tiers. Lorsqu'un e-mail est envoyé en votre nom, cet e-mail aura ce nom ou ce nombre inclus dans l'en-tête. C'est l'enregistrement qu'il recherchera sous votre domaine.

En termes simples et dans notre exemple, le serveur du destinataire irait aux enregistrements DNS de doecompany et vérifierait si ce que le tiers prétend être vrai s'y trouve. Seulement si la clé publique est correctement validée avec la clé sur leur serveur, les e-mails seront envoyés.

**v=DKIM1 :** Spécifie simplement la version de DKIM utilisée pour clarifier ce qu'il faut rechercher.

**k=rsa :** RSA est le plus typique à utiliser comme clé (k). Votre tiers pourrait opter pour utiliser autre chose. Mais RSA avec un chiffrement de 2048 bits est l'option la plus sécurisée que vous pouvez avoir pour le moment. 1024 bits est également bon.

**p=<clé publique> :** Au lieu de <clé publique>, vous recevriez une chaîne de 1024 bits ou 2048 bits de texte et de nombres apparemment aléatoires ou d'autres valeurs adaptées au chiffrement que le tiers a décidé d'utiliser.

**TTL = 1 heure** (ou 3600 secondes) : Time-To-Live, ou la fréquence à laquelle cela devrait expirer. Si vous deviez changer de serveurs de messagerie, vous seriez content qu'il n'y ait qu'un maximum de 1 heure de non-authentification.

### Configuration de DMARC :

**Rappel :** Pour que le DMARC fasse son travail, vous DEVEZ configurer SPF ET DKIM avant. Parce que DMARC vérifie les paramètres SPF & DKIM et si l'expéditeur correspond à ces paramètres et n'est pas un usurpateur. Si SPF & DKIM ne sont pas configurés, DMARC ne fonctionnera pas et entraînera le rejet des e-mails.

Tout comme pour les enregistrements SPF, vous accéderez à votre éditeur DNS (également appelé Éditeur de zone DNS dans CPanel), et créerez une nouvelle entrée TXT. Dans cette entrée TXT, vous devriez avoir 3 champs possibles : Hôte, Valeur TXT / Valeur & TTL (Time-To-Live). Ce que vous entrerez dans ces champs est le suivant (certains détails peuvent varier, cela est basé sur une installation GoDaddy avec les e-mails hébergés sur inmotionhosting.com) :
Hôte : _dmarc
Valeur TXT : v=DMARC1;p=reject;sp=none;adkim=r;aspf=r;pct=100;fo=0;rf=afrf;ri=86400
TTL : 1 heure

![Image](https://cdn-media-1.freecodecamp.org/images/1*TvOQkx-VHgLLx7o831YsAg.png)
_Exemple d'entrée TXT DNS GoDaddy pour les paramètres DMARC tels que décrits ci-dessus._

**Explication / Signification de ces paramètres :**

L'hôte est déclaré comme _dmarc car au sein de GoDaddy, il ajoutera automatiquement .johndoe.com comme sous-domaine. Cela signifie que lorsqu'un e-mail est envoyé, le DMARC sera toujours vérifié sous ce sélecteur contre votre domaine. Si cela n'est pas configuré correctement comme _dmarc, les serveurs de messagerie ne pourront pas trouver votre entrée DMARC et échoueront automatiquement votre e-mail car ils croiront qu'il n'y a pas d'entrée pour commencer.

**v=DMARC1 :** Déclare la version du DMARC pour clarifier ce qui est utilisé et rendre l'authentification plus légitime.

**p=reject :** Les e-mails seront rejetés par le serveur de messagerie du destinataire s'ils ne correspondent pas aux enregistrements DMARC.

**sp=none :** Ne pas vérifier si les sous-domaines et le domaine principal ont des paramètres alignés ; cela est facultatif.

**adkim=r :** Être strict (s) ou indulgent (r) avec les paramètres d'identifiant DKIM ; indulgent est la valeur par défaut.

**aspf=r :** Être strict (s) ou indulgent (r) avec les paramètres d'identifiant SPF ; indulgent est la valeur par défaut.

**pct=100 :** 100 pour cent des e-mails seront affectés par le DMARC. Valeurs entières entre 1 et 100 uniquement. Un ensemble plus petit n'aurait de sens que pour les tests ; devrait être 100 pour des raisons de sécurité.

**fo=0 :** Un rapport d'erreur DMARC est créé si SPF & DKIM échouent à être authentifiés. 0 est la valeur par défaut. Les autres sont 1, d et s. 1 si l'un des deux échoue, pour générer un enregistrement. d si la signature a échoué l'évaluation. s si l'évaluation SPF a échoué.

**rf=afrf :** Le formatage pour les rapports d'échec de message. afrf est la seule valeur prise en charge au moment de la rédaction de ce document.

**ri=86400 :** Nombre de secondes écoulées entre l'envoi du rapport à l'expéditeur. 86400 est la valeur par défaut, soit 24 heures ou 1 jour. De nombreux grands fournisseurs de boîtes aux lettres tels que Gmail, Yahoo, etc., enverront plus d'un rapport par jour.

**TTL = 1 heure** (ou 3600 secondes) : Time-To-Live, ou la fréquence à laquelle cela devrait expirer. Si vous deviez changer de serveurs de messagerie, vous seriez content qu'il n'y ait qu'un maximum de 1 heure de non-authentification.

Et c'est ainsi que vous authentifiez correctement vos e-mails. J'espère que cela a enlevé une partie du mystère et de la complication pour vous. Vous serez sur la bonne voie pour ne plus recevoir ces retours gênants de votre mailer-daemon !

---

**Auteur :**

Andreas Lopez

[https://www.linkedin.com/in/andreaslopez/](https://www.linkedin.com/in/andreaslopez/)

**Éditeurs :**

Stevan Pupavac

[https://www.linkedin.com/in/stevan-pupavac/](https://www.linkedin.com/in/stevan-pupavac/)

Frederick Alcantara

[https://www.linkedin.com/in/frederick-alcantara/](https://www.linkedin.com/in/frederick-alcantara/)

**Sources :**

1. Captures d'écran GoDaddy par DMARCanalyzer.com : [https://www.dmarcanalyzer.com/dmarc/dmarc-record-setup-guides/dmarc-setup-guide-godaddy/](https://www.dmarcanalyzer.com/dmarc/dmarc-record-setup-guides/dmarc-setup-guide-godaddy/)