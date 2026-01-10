---
title: Comment envoyer des notifications à votre application Web en utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T21:54:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-notifications-to-your-web-app-using-python-ba490b893292
coverImage: https://cdn-media-1.freecodecamp.org/images/1*htDJgQOlkHDn7eF9WITh8Q.jpeg
tags:
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment envoyer des notifications à votre application Web en utilisant
  Python
seo_desc: 'By Lucas Hild

  Native apps have become hugely popular recently, mostly because of features such
  as working offline, transitions, easy distributability and of course push notifications.
  But unfortunately, you need a good knowledge of languages like Jav...'
---

Par Lucas Hild

Les applications natives sont devenues extrêmement populaires récemment, principalement en raison de fonctionnalités telles que le travail hors ligne, les transitions, la facilité de distribution et bien sûr les notifications push. Mais malheureusement, vous avez besoin d'une bonne connaissance de langages comme Java ou Swift pour créer une application native valable.

### Applications Web Progressives

Les Applications Web Progressives (PWA) sont des applications JavaScript qui s'exécutent dans le navigateur. Elles font l'effort d'apporter certaines des fonctionnalités des applications natives sur le web. Les PWA sont faciles à développer si vous avez une connaissance fondamentale de HTML, CSS, et en particulier JavaScript. De plus, si votre service est déjà accessible pour les appareils de bureau sur un site web, il est plus facile d'ajouter les fonctionnalités d'une Application Web, plutôt que de développer une application mobile native.

### Notifications

Les notifications informent les utilisateurs des nouveaux messages, leur indiquent un nouvel article de blog, et ainsi de suite.

De nombreuses applications natives envoient des notifications push à l'utilisateur. Mais cela est également possible en utilisant les PWA et l'API Notifications.

![Image](https://cdn-media-1.freecodecamp.org/images/H0tzewZI3D7d-DcwdysrJx3CpPTE2IcvEUeE)
_Photo par [Unsplash](https://unsplash.com/@jamie452?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jamie Street</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### OneSignal

Dans ce tutoriel, nous allons utiliser [OneSignal](https://onesignal.com) pour envoyer des notifications à notre application web. OneSignal est un outil puissant qui fournit une interface simple pour les notifications push. Ils fournissent également une API Rest, que nous allons utiliser pour envoyer des notifications.

### Configuration de OneSignal

Pour envoyer des notifications push, vous devez d'abord configurer OneSignal. Pour cela, vous avez besoin d'un compte sur OneSignal. Rendez-vous sur [leur site web](https://onesignal.com) et appuyez sur « Se connecter » dans le coin supérieur droit.

Ensuite, vous devrez créer une application. Donnez-lui un nom et choisissez « Configurer la plateforme ». Ici, vous sélectionnez « Tous les navigateurs ». Après cela, vous choisissez « code personnalisé » comme intégration. Ensuite, vous devez fournir quelques informations sur votre site web.

Dans la zone des paramètres de votre application, il y a un onglet appelé « Clés & ID ». Copiez les deux clés pour plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/CZolsxSB91fV86I3nzpJL2qHSLEOfSyR0eWz)

**Important : Ne partagez pas votre clé REST API. Gardez-la privée !**

C'est tout pour la configuration de OneSignal. C'était facile !

### Configuration de notre site web

Dans la partie suivante, nous allons ajouter la fonctionnalité de notification à notre site web. Le site web devra attendre les notifications envoyées par OneSignal et les afficher à l'utilisateur.

Pour informer le navigateur que vous créez une Application Web Progressive, nous allons ajouter un fichier appelé **manifest.json** à la racine de notre projet.

```
{  "name": "Mon Application",  "short_name": "Application",  "start_url": ".",  "display": "standalone",  "background_color" : "#fff" ,  "description": "Nous vous envoyons des notifications",  "gcm_sender_id": "482941778795",  "gcm_sender_id_comment": "Ne changez pas l'ID de l'expéditeur GCM"}
```

Les six premières paires clé-valeur décrivent l'apparence de l'application. Le **gcm_sender_id** est important pour envoyer des notifications. Si vous voulez en savoir plus sur **manifest.json**, vous pouvez consulter la [Documentation Mozilla](https://developer.mozilla.org/de/docs/Web/Manifest).

Votre navigateur ne recherche pas automatiquement le manifest. Vous devez mettre le chemin d'accès dans chaque document HTML dans la balise _&lt;head>_.

```
<head>    ...    <link rel="manifest" href="manifest.json">    ...</head>
```

De plus, nous avons besoin de quelque code JavaScript pour connecter notre site web à OneSignal.

Vous pouvez mettre le code pour cela dans une balise script dans la partie _&lt;head>_. N'oubliez pas de remplacer **my-app-id** par votre propre identifiant d'application OneSignal.

```
<head>    <script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async=""></script>        <script>        var OneSignal = window.OneSignal || [];        OneSignal.push(function () {            OneSignal.init({                appId: "my-app-id",                autoRegister: false,                notifyButton: {                    enable: true,                },            });        });    <script></head>
```

![Image](https://cdn-media-1.freecodecamp.org/images/rXjHpdqOUr9ahuanYkm9FlHip7ftX12pFV-n)
_Invitez l'utilisateur à s'abonner à vos notifications_

Lorsque vous voulez inviter l'utilisateur à s'abonner à vos notifications, vous exécutez ce morceau de code.

```
OneSignal.push(function () {    OneSignal.showHttpPrompt();});
```

De plus, vous avez besoin d'un service worker, qui écoute en arrière-plan les notifications. Par conséquent, vous avez besoin de deux fichiers dans le répertoire racine de votre projet.

**OneSignalSDKUpdaterWorker.js**

```
importScripts('https://cdn.onesignal.com/sdks/OneSignalSDKWorker.js');
```

**OneSignalSDKWorker.js**

```
importScripts('https://cdn.onesignal.com/sdks/OneSignalSDKWorker.js');
```

### Accéder à l'API en utilisant Python

OneSignal dispose d'une API Rest facile à utiliser. Les points de terminaison sont documentés dans la [Documentation du Développeur OneSignal](https://documentation.onesignal.com/docs).

![Image](https://cdn-media-1.freecodecamp.org/images/JonbuaZJXt9N2C-HIZzS-JR6gp1trvGEZ741)
_Photo par [Unsplash](https://unsplash.com/@maxcodes?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Max Nelson</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Pour y accéder, nous devons envoyer des requêtes HTTP. Par conséquent, nous allons utiliser une bibliothèque appelée [**requests**](http://docs.python-requests.org/en/master/). Pour l'installer, vous pouvez utiliser pip, le gestionnaire de paquets de Python.

```
pip install requests
```

Voici le point de terminaison de l'API dont nous avons besoin pour envoyer une notification : [https://onesignal.com/api/v1/notifications](https://onesignal.com/api/v1/notifications).

Le protocole HTTP dispose de plusieurs méthodes. Dans ce cas, nous voulons faire une requête POST. Pour ce faire, nous devons importer requests et exécuter une fonction.

```
import requests
```

```
requests.post("https://onesignal.com/api/v1/notifications")
```

OneSignal veut vérifier que seul vous pouvez envoyer des notifications à votre site web. Vous devez donc ajouter un en-tête HTTP avec votre clé REST API de OneSignal.

```
requests.post(    "https://onesignal.com/api/v1/notifications",    headers={"Authorization": "Basic my-rest-api-key"})
```

N'oubliez pas de remplacer **my-rest-api-key** par votre clé REST API.

De plus, vous avez besoin de quelques informations de base sur votre notification.

```
data = {    "app_id": "my-app-id",    "included_segments": ["All"],    "contents": {"en": "Hello"}}
```

```
requests.post(    "https://onesignal.com/api/v1/notifications",    headers={"Authorization": "Basic my-rest-api-key"},    json=data)
```

Remplacez **my-app-id** par votre propre identifiant d'application. Ensuite, vous choisissez qui recevra vos notifications. Les valeurs d'exemple sont `"All", "Active Users", "Inactive Users"`. Mais vous pouvez également créer vos propres segments. Et pour le dernier, vous ajoutez un peu de contenu du message en anglais. Si vous avez besoin d'une autre langue, vous pouvez l'ajouter ici aussi.

**C'est tout ! Si vous êtes abonné aux notifications, vous devriez recevoir une notification push.**

![Image](https://cdn-media-1.freecodecamp.org/images/Z6q3cFDErQJTIstdDh8lc93gBpRgtvLxJmTs)

### Envoyer des notifications en utilisant un API Wrapper

Parce que mon code est devenu un peu désordonné avec de nombreuses notifications différentes, j'ai [créé un API wrapper pour OneSignal](https://github.com/Lanseuo/onesignal-notifications).

#### API Wrapper

Mais qu'est-ce qu'un API wrapper ? Un API wrapper facilite l'accès à une API. Vous pouvez dire que c'est une API pour une API. Vous appelez l'API wrapper au lieu de l'API directement.

Vous pouvez installer le wrapper appelé **OneSignal-Notifications** depuis pip.

```
pip install onesignal-notifications
```

Maintenant vous pouvez l'importer et configurer votre client.

```
from onesignal import OneSignal, SegmentNotificationclient = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

Pour envoyer une notification, vous devez initialiser la classe **SegmentNotification** et utiliser la méthode **send**.

```
notification_to_all_users = SegmentNotification(    {        "en": "Hello from OneSignal-Notifications"    },    included_segments=SegmentNotification.ALL)client.send(notification_to_all_users)
```

Peut-être que cela vous semble un peu inutile, car cela prend encore plus de lignes de code. Mais si vous avez plusieurs notifications, cela rend le processus beaucoup plus facile et votre code plus beau.

Par exemple, si vous voulez envoyer une notification basée sur certaines conditions, l'API wrapper a une classe personnalisée pour cela.

```
from onesignal import OneSignal, FilterNotification, Filterclient = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

```
filter_notification = FilterNotification(    {        "en": "Hello from OneSignal-Notifications"    },    filters=[        Filter.Tag("my_key", "<", "5"),        "AND",        Filter.AppVersion(">", "5"),        "OR",        Filter.LastSession(">", "1"),    ])
```

Il y a de nombreux paramètres personnalisés que vous pouvez fournir pour adapter votre notification. Par exemple, vous pouvez ajouter des boutons à la notification. La liste de tous les paramètres peut être trouvée [ici](https://lanseuo.github.io/onesignal-notifications/guide/send-notification.html#common-parameters).

```
from onesignal import OneSignal, FilterNotification, Filterclient = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

```
filter_notification = SegmentNotification(    {        "en": "Hello from OneSignal-Notifications"    },    web_buttons=[        {          "id": "like-button",          "text": "Like",          "icon": "http://i.imgur.com/N8SN8ZS.png",          "url": "https://github.com/Lanseuo/onesignal-notifications"}    ],    included_segments=SegmentNotification.ALL)
```

Si vous voulez en savoir plus sur **OneSignal-Notifications**, vous pouvez consulter le [Dépôt GitHub](https://github.com/Lanseuo/onesignal-notifications) ou la [documentation](https://lanseuo.github.io/onesignal-notifications).