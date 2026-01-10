---
title: Comment tester les Webhooks lors du développement local
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-30T20:23:41.000Z'
originalURL: https://freecodecamp.org/news/testing-webhooks-while-using-vagrant-for-development-98b5f3bedb1d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0HNQmPw5yXva6powvVwn5Q.jpeg
tags:
- name: development
  slug: development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: vagrant
  slug: vagrant
- name: webhooks
  slug: webhooks
seo_title: Comment tester les Webhooks lors du développement local
seo_desc: 'By Stefan Doorn

  Webhooks can be used by an external system for notifying your system about a certain
  event or update. Probably the most well known type is the one where a Payment Service
  Provider (PSP) informs your system about status updates of paym...'
---

Par Stefan Doorn

Les [Webhooks](https://sendgrid.com/blog/whats-webhook/) peuvent être utilisés par un système externe pour notifier votre système à propos d'un certain événement ou d'une mise à jour. Probablement le type le plus connu est celui où un fournisseur de services de paiement (PSP) informe votre système des mises à jour de statut des paiements.

Souvent, ils se présentent sous la forme où vous écoutez sur une URL prédéfinie. Par exemple, [http://example.com/webhooks/payment-update](http://example.com/webhooks/payment-update)). Pendant ce temps, l'autre système envoie une requête POST avec une certaine charge utile à cette URL (par exemple, un identifiant de paiement). Dès que la requête arrive, vous récupérez l'identifiant de paiement, demandez au PSP le dernier statut via leur API, et mettez à jour votre base de données ensuite.

D'autres exemples peuvent être trouvés dans cette excellente explication sur les Webhooks. [https://sendgrid.com/blog/whats-webhook/](https://sendgrid.com/blog/whats-webhook/).

Tester ces webhooks se fait assez facilement tant que le système est accessible publiquement sur Internet. Cela peut être votre environnement de production ou un environnement de staging accessible publiquement. Cela devient plus difficile lorsque vous développez localement sur votre ordinateur portable ou à l'intérieur d'une machine virtuelle (VM, par exemple, une boîte Vagrant). Dans ces cas, les URL locales ne sont pas accessibles publiquement par la partie envoyant le webhook. De plus, surveiller les requêtes envoyées est difficile, ce qui peut rendre le développement et le débogage ardus.

Ce que cet exemple va résoudre :

* Tester les webhooks à partir d'un environnement de développement local, qui n'est pas accessible sur Internet. Il ne peut pas être accessible par le service envoyant les données au webhook depuis leurs serveurs.
* Surveiller les requêtes et les données envoyées, mais aussi la réponse générée par votre application. Cela permettra un débogage plus facile, et donc un cycle de développement plus court.

Prérequis :

* _Optionnel_ : si vous développez en utilisant une machine virtuelle (VM), assurez-vous qu'elle est en cours d'exécution et que les étapes suivantes sont effectuées dans la VM.
* Pour ce tutoriel, nous supposons que vous avez un vhost défini à `webhook.example.vagrant`. J'ai utilisé une VM Vagrant pour ce tutoriel, mais vous êtes libre de choisir le nom de votre vhost.
* Installez `ngrok` en suivant les [instructions d'installation](https://ngrok.com/download). À l'intérieur d'une VM, je trouve la version Node utile également : [https://www.npmjs.com/package/ngrok](https://www.npmjs.com/package/ngrok), mais vous êtes libre d'utiliser d'autres méthodes.

Je suppose que vous n'avez pas SSL en cours d'exécution dans votre environnement, mais si vous en avez, n'hésitez pas à remplacer le port 80 par le port 433 et `_http://_` par `_https://_` dans les exemples ci-dessous.

#### **Rendre le webhook testable**

Supposons le code d'exemple suivant. J'utiliserai PHP, mais lisez-le comme du pseudo-code car j'ai laissé de côté certaines parties cruciales (par exemple, les clés API, la validation des entrées, etc.)

Le premier fichier : _payment.php_. Ce fichier crée un objet de paiement et l'enregistre ensuite avec le PSP. Il récupère ensuite l'URL que le client doit visiter pour payer et redirige l'utilisateur vers le client.

Notez que le `webhook.example.vagrant` dans cet exemple est le vhost local que nous avons défini pour notre configuration de développement. Il n'est pas accessible depuis l'extérieur.

```php
<?php
/*
 * Ce fichier crée un paiement et indique au PSP quelle URL de webhook utiliser pour les mises à jour
 * Après avoir créé le paiement, nous obtenons une URL pour envoyer le client afin de payer chez le PSP
 */
$payment = [
    'order_id' => 123,
    'amount' => 25.00,
    'description' => 'Test payment',
    'redirect_url' => 'http://webhook.example.vagrant/redirect.php',
    'webhook_url' => 'http://webhook.example.vagrant/webhook.php',
];

$payment = $paymentProvider->createPayment($payment);
header("Location: " . $payment->getPaymentUrl());
```

Deuxième fichier : _webhook.php_. Ce fichier attend d'être appelé par le PSP pour être notifié des mises à jour.

```php
<?php
/*
 * Ce fichier est appelé par le PSP et dans le $_POST, ils soumettent un 'id'
 * Nous pouvons utiliser cet ID pour obtenir le dernier statut du PSP et mettre à jour nos systèmes internes ensuite
 */
 
$paymentId = $_POST['id'];
$paymentInfo = $paymentProvider->getPayment($paymentId);
$status = $paymentInfo->getStatus();

// Effectuer des actions ici pour mettre à jour votre système
if ($status === 'paid') {
    ..
}
elif ($status === 'cancelled') {
    ..
}
```

Notre URL de webhook n'est pas accessible sur Internet (rappel : `webhook.example.vagrant`). Ainsi, le fichier _webhook.php_ ne sera jamais appelé par le PSP. Votre système ne saura jamais le statut du paiement. Cela conduit finalement à des commandes jamais expédiées aux clients.

Heureusement, _ngrok_ peut résoudre ce problème. [_ngrok_](https://ngrok.com) se décrit comme :

> ngrok expose les serveurs locaux derrière les NAT et les pare-feu à l'internet public via des tunnels sécurisés.

Commençons un tunnel de base pour notre projet. Sur votre environnement (soit sur votre système ou sur la VM), exécutez la commande suivante :

`ngrok http -host-header=rewrite webhook.example.vagrant:80`

Lisez plus d'options de configuration dans leur documentation : [https://ngrok.com/docs](https://ngrok.com/docs).

Un écran comme celui-ci apparaîtra :

![Image](https://cdn-media-1.freecodecamp.org/images/PuC-rg6uYtgl0ltFQUooZbU5VJju2qIESJ1F)
_Sortie ngrok_

Qu'avons-nous démarré ? Basiquement, nous avons instructé `ngrok` à démarrer un tunnel vers `[http://webhook.example.vagrant](http://webhook.example.vagrnat/)` sur le port 80. Cette même URL peut maintenant être atteinte via `[http://39741ffc.ngrok.io](http://39741ffc.ngrok.io/)` ou `[https://39741ffc.ngrok.io](http://39741ffc.ngrok.io/)`[,](http://39741ffc.ngrok.io%2C/) Elles sont accessibles publiquement sur Internet par quiconque connaît cette URL.

**Notez** que vous obtenez à la fois HTTP et HTTPS disponibles dès la sortie de la boîte. La documentation donne des exemples de la façon de restreindre cela à HTTPS uniquement : [https://ngrok.com/docs#bind-tls](https://ngrok.com/docs#bind-tls).

Alors, comment faire fonctionner notre webhook maintenant ? Mettez à jour _payment.php_ avec le code suivant :

```php
<?php
/*
 * Ce fichier crée un paiement et indique au PSP quelle URL de webhook utiliser pour les mises à jour
 * Après avoir créé le paiement, nous obtenons une URL pour envoyer le client afin de payer chez le PSP
 */
$payment = [
    'order_id' => 123,
    'amount' => 25.00,
    'description' => 'Test payment',
    'redirect_url' => 'http://webhook.example.vagrant/redirect.php',
    'webhook_url' => 'https://39741ffc.ngrok.io/webhook.php',
];

$payment = $paymentProvider->createPayment($payment);
header("Location: " . $payment->getPaymentUrl());
```

Maintenant, nous avons dit au PSP d'appeler l'URL du tunnel via HTTPS. _ngrok_ s'assurera que votre URL interne est appelée avec une charge utile non modifiée, dès que le PSP appelle le webhook via le tunnel.

#### **Comment surveiller les appels au webhook ?**

La capture d'écran que vous avez vue ci-dessus donne un aperçu des appels effectués à l'hôte du tunnel. Ces données sont plutôt limitées. Heureusement, `ngrok` offre un tableau de bord très pratique, qui vous permet d'inspecter tous les appels :

![Image](https://cdn-media-1.freecodecamp.org/images/5qMSpanO5DID6fouWKns6mZcsj-cgVYXntV-)

Je n'entrerai pas dans les détails car c'est auto-explicatif une fois que vous l'avez en cours d'exécution. Je vais donc expliquer comment y accéder sur la boîte Vagrant car cela ne fonctionne pas directement.

Le tableau de bord vous permettra de voir tous les appels, leurs codes de statut, les en-têtes et les données envoyées. Vous verrez également la réponse générée par votre application.

Une autre fonctionnalité intéressante du tableau de bord est qu'il vous permet de rejouer un certain appel. Supposons que votre code de webhook ait rencontré une erreur fatale, il serait fastidieux de démarrer un nouveau paiement et d'attendre que le webhook soit appelé. Rejouer l'appel précédent rend votre processus de développement beaucoup plus rapide.

Le tableau de bord est accessible par défaut à [http://localhost:4040.](http://localhost:4040.)

#### **Tableau de bord dans une VM**

Pour que cela fonctionne à l'intérieur d'une VM, vous devez effectuer quelques étapes supplémentaires :

Tout d'abord, assurez-vous que la VM peut être accessible sur le port 4040. Ensuite, créez un fichier à l'intérieur de la VM contenant cette configuration :

`web_addr: **0.0.0.0:4040**`

Maintenant, arrêtez le processus `ngrok` qui est toujours en cours d'exécution et démarrez-le avec cette commande légèrement ajustée :

`ngrok http -config=/path/to/config/ngrok.conf -host-header=rewrite webhook.example.vagrant:80`

Vous obtiendrez un écran similaire à la capture d'écran précédente, bien que les identifiants aient changé. L'URL précédente ne fonctionne plus, mais vous avez obtenu une nouvelle URL. De plus, l'URL de l'interface Web a été modifiée :

![Image](https://cdn-media-1.freecodecamp.org/images/IR7nrGbuh0192n0CGzY2Az0qX-RA6kIwoMZs)

Maintenant, dirigez votre navigateur vers `[http://webhook.example.vagrant:4040](http://webhook.example.vagrant:4040)` pour accéder au tableau de bord. De plus, faites un appel à `[https://e65642b5.ngrok.io/webhook.php](https://e65642b5.ngrok.io/webhook.php.)`[.](https://e65642b5.ngrok.io/webhook.php.) Cela résultera probablement en une erreur dans votre navigateur, mais le tableau de bord devrait montrer la requête effectuée.

#### **Remarques finales**

Les exemples ci-dessus sont du pseudo-code. La raison est que chaque système externe utilise les webhooks de manière différente. J'ai essayé de donner un exemple basé sur une implémentation fictive de PSP, car probablement de nombreux développeurs doivent traiter les paiements à un moment donné.

Veuillez être conscient que votre URL de webhook peut également être utilisée par d'autres avec de mauvaises intentions. Assurez-vous de valider toute entrée envoyée.

De préférence, ajoutez également un jeton à l'URL qui est unique pour chaque paiement. Ce jeton ne doit être connu que par votre système et le système envoyant le webhook.

Bonne chance pour tester et déboguer vos webhooks !

**Note :** Je n'ai pas testé ce tutoriel sur Docker. Cependant, ce conteneur Docker semble être un bon point de départ et inclut des instructions claires. [https://github.com/wernight/docker-ngrok](https://github.com/wernight/docker-ngrok).

Stefan Doorn

[https://github.com/stefandoorn](https://github.com/stefandoorn)  
[https://twitter.com/stefan_doorn](https://twitter.com/stefan_doorn)  
[https://www.linkedin.com/in/stefandoorn](https://www.linkedin.com/in/stefandoorn)