---
title: Récepteurs de diffusion pour débutants
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-07-09T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/broadcast-receivers-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca18d740569d1a4ca4f47.jpg
tags:
- name: broadcast-receivers
  slug: broadcast-receivers
- name: Android
  slug: android
- name: coding
  slug: coding
- name: 'tech '
  slug: tech
seo_title: Récepteurs de diffusion pour débutants
seo_desc: Let’s say you have an application that depends on a steady internet connection.
  You want your application to get notified when the internet connection changes.
  How do you do that? A possible solution would be a service which always checks the
  interne...
---

Disons que vous avez une application qui dépend d'une connexion Internet stable. Vous voulez que votre application soit notifiée lorsque la connexion Internet change. Comment faire cela ? Une solution possible serait un service qui vérifie toujours la connexion Internet. Cette implémentation est mauvaise pour diverses raisons, donc nous ne la considérerons même pas. La solution à ce problème est un récepteur de diffusion et il écoutera les changements que vous lui demandez. Un récepteur de diffusion sera toujours notifié d'une diffusion, indépendamment de l'état de votre application. Peu importe si votre application est en cours d'exécution, en arrière-plan ou non en cours d'exécution du tout.

#### Contexte

Les récepteurs de diffusion sont des composants de votre application Android qui écoutent les messages de diffusion (ou événements) provenant de différentes sources :

* D'autres applications
  
* Du système lui-même
  
* De votre application
  
Cela signifie qu'ils sont invoqués lorsqu'une certaine action s'est produite et qu'ils ont été programmés pour l'écouter (c'est-à-dire une diffusion).

Une diffusion est simplement un message enveloppé dans un objet Intent. Une diffusion peut être implicite ou explicite.

* Une ***diffusion implicite*** est une diffusion qui ne cible pas spécifiquement votre application, donc elle n'est pas exclusive à votre application. Pour vous enregistrer à une diffusion implicite, vous devez utiliser un [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) et le déclarer dans votre manifest. Vous devez faire tout cela parce que le système d'exploitation Android parcourt tous les filtres d'intention déclarés dans votre manifest et voit s'il y a une correspondance. En raison de ce comportement, les diffusions implicites n'ont pas d'attribut de cible. Un exemple de diffusion implicite serait une action de réception d'un message SMS.
  
* Une ***diffusion explicite*** est une diffusion qui est spécifiquement ciblée pour votre application sur un composant connu à l'avance. Cela se produit en raison de l'attribut de cible qui contient le nom du package de l'application ou un nom de classe de composant.
  

Il existe deux façons de déclarer un récepteur :

1. En déclarant un récepteur dans votre fichier AndroidManifest.xml avec la balise (également appelé statique)
  

```xml
<receiver android:name=".VotreClasseDeRecepteurDeDiffusion" android:exported="true">
    <intent-filter>
        <!-- Les actions que vous souhaitez écouter, ci-dessous un exemple -->
        <action android:name="android.intent.action.BOOT_COMPLETED"/>
    </intent-filter>
</receiver>
```

Vous remarquerez que le récepteur de diffusion déclaré ci-dessus a une propriété ***exported="true"***. Cet attribut indique au récepteur qu'il peut recevoir des diffusions en dehors du champ d'application de l'application.

2. Ou dynamiquement en enregistrant une instance avec registerReceiver (ce qui est connu comme un enregistrement de contexte)
  

```java
public abstract Intent registerReceiver (BroadcastReceiver receiver, 
                IntentFilter filter);
```

---

#### Implémentation

Pour créer votre propre récepteur de diffusion, vous devez d'abord étendre la classe parente BroadcastReceiver et remplacer la méthode obligatoire, onReceive :

```java
public void onReceive(Context context, Intent intent) {
    // Implémentez votre logique ici
}
```

En mettant tout cela ensemble, cela donne :

```java
public class MyBroadcastReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        StringBuilder sb = new StringBuilder();
        sb.append("Action : " + intent.getAction() + "\n");
        sb.append("URI : " + intent.toUri(Intent.URI_INTENT_SCHEME).toString() + "\n");
        String log = sb.toString();
        Toast.makeText(context, log, Toast.LENGTH_LONG).show();

    }
}
```

> *⚠️ La méthode onReceive s'exécute sur le thread principal, et pour cette raison, son exécution doit être brève.*

Si un long processus est exécuté, le système peut tuer le processus après le retour de la méthode. Pour contourner cela, envisagez d'utiliser [goAsync](https://developer.android.com/reference/android/content/BroadcastReceiver.html#goAsync%28%29) ou de planifier un travail. Vous pouvez lire plus sur la planification d'un travail à la fin de cet article.

---

#### Exemple d'enregistrement dynamique

Pour enregistrer un récepteur avec un contexte, vous devez d'abord instancier une instance de votre récepteur de diffusion :

```java
BroadcastReceiver myBroadcastReceiver = new MyBroadcastReceiver();
```

Ensuite, vous pouvez l'enregistrer en fonction du contexte spécifique que vous souhaitez :

```java
IntentFilter filter = new IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION);
filter.addAction(Intent.ACTION_AIRPLANE_MODE_CHANGED);
this.registerReceiver(myBroadcastReceiver, filter);
```

N'oubliez pas de désenregistrer votre récepteur de diffusion lorsque vous n'en avez plus besoin :

```java
@Override
protected void onStop() {
  super.onStop();
  unregisterReceiver(myBroadcastReceiver);
}
```

#### Diffusion d'un événement

L'objectif de la diffusion de messages depuis votre application est de permettre à votre application de répondre aux événements qui se produisent à l'intérieur. Imaginez un scénario où, dans une partie du code, l'utilisateur effectue une certaine action et, en raison de celle-ci, vous souhaitez exécuter une autre logique que vous avez à un autre endroit.

Il existe trois façons d'envoyer des diffusions :

1. La méthode [***sendOrderedBroadcast***](https://developer.android.com/reference/android/content/Context.html#sendOrderedBroadcast%28android.content.Intent,%20java.lang.String%29) s'assure d'envoyer des diffusions à un seul récepteur à la fois. Chaque diffusion peut, à son tour, transmettre des données à celle qui suit, ou arrêter la propagation de la diffusion aux récepteurs suivants.
  
2. La méthode [***sendBroadcast***](https://developer.android.com/reference/android/content/Context.html#sendBroadcast%28android.content.Intent%29) est similaire à la méthode mentionnée ci-dessus, avec une différence. Tous les récepteurs de diffusion reçoivent le message et ne dépendent pas les uns des autres.
  
3. La méthode ***LocalBroadcastManager.sendBroadcast*** n'envoie des diffusions qu'aux récepteurs définis à l'intérieur de votre application et ne dépasse pas le champ d'application de votre application. Exemple d'envoi d'une diffusion personnalisée.
  

[https://giphy.com/gifs/23gUJhHyWkXEwl7UYV/html5](https://giphy.com/gifs/23gUJhHyWkXEwl7UYV/html5)

---

![Image](https://cdn-media-1.freecodecamp.org/images/0*ywQVksVZ0m-Np16m align="left")

*Photo par* [*Unsplash*](https://unsplash.com/@johngibbons?utm_source=medium&utm_medium=referral)

#### Pièges et points à surveiller

* Ne envoyez pas de données sensibles via une diffusion implicite, car toute application écoutant cette diffusion les recevra. Vous pouvez éviter cela en spécifiant un package ou en attachant une permission à la diffusion.
  
* Ne démarrez pas d'activités à partir d'une diffusion reçue, car l'expérience utilisateur est médiocre. Choisissez plutôt d'afficher une notification.
  

Les points suivants concernent les changements dans les récepteurs de diffusion pertinents pour chaque version d'Android (à partir de la version 7.0). Pour chaque version, certaines limitations ont été mises en place et le comportement a également changé. Gardez ces limitations à l'esprit lorsque vous envisagez d'utiliser un récepteur de diffusion.

* ***7.0 et versions ultérieures (niveau d'API 24)*** - Deux diffusions système ont été désactivées, [Action_New_Picture](https://developer.android.com/reference/android/hardware/Camera.html#ACTION_NEW_PICTURE) et [Action_New_Video](https://developer.android.com/reference/android/hardware/Camera.html#ACTION_NEW_VIDEO) (mais elles ont été rétablies dans Android O pour les récepteurs enregistrés).
  
* ***8.0 et versions ultérieures (niveau d'API 26)*** - La plupart des diffusions implicites doivent être enregistrées dynamiquement et non statiquement (dans votre manifest). Vous pouvez trouver les diffusions qui ont été autorisées dans ce [lien](https://developer.android.com/guide/components/broadcast-exceptions).
  
* ***9.0 et versions ultérieures (niveau d'API 28)*** - Moins d'informations reçues sur la diffusion système Wi-Fi et [Network_State_Changed_Action](https://developer.android.com/reference/android/net/wifi/WifiManager.html#NETWORK_STATE_CHANGED_ACTION).
  

Les changements dans Android O sont ceux dont vous devez être le plus conscient. La raison de ces changements était qu'ils entraînaient des problèmes de performance, une dépletion de la batterie et nuisaient à l'expérience utilisateur. Cela s'est produit parce que de nombreuses applications (même celles qui n'étaient pas en cours d'exécution) écoutaient un changement système global et, lorsque ce changement se produisait, le chaos s'ensuivait. Imaginez que chaque application enregistrée pour l'action se réveille pour vérifier si elle devait faire quelque chose à cause de la diffusion. Prenez en compte quelque chose comme l'état du Wi-Fi, qui change fréquemment, et vous commencerez à comprendre pourquoi ces changements ont eu lieu.

---

#### Alternatives aux récepteurs de diffusion

Pour faciliter la navigation parmi toutes ces restrictions, voici une liste d'autres composants que vous pouvez utiliser en l'absence d'un récepteur de diffusion. Chacun a une responsabilité et un cas d'utilisation différents, alors essayez de déterminer lequel répond à vos besoins.

* ***LocalBroadcastManager*** - Comme je l'ai mentionné ci-dessus, cela est valable uniquement pour les diffusions au sein de votre application.
  
* ***Planification d'un travail*** - Un travail peut être exécuté en fonction d'un signal ou d'un déclencheur reçu, donc vous pouvez constater que la diffusion que vous écoutiez peut être remplacée par un travail. De plus, le [JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler.html) garantira que votre travail sera terminé, mais il prendra en compte divers facteurs système (temps et conditions) pour déterminer quand il doit s'exécuter. Lors de la création d'un travail, vous remplacerez une méthode appelée ***onStartJob***. Cette méthode s'exécute sur le thread principal, alors assurez-vous qu'elle termine son travail en un temps limité. Si vous devez effectuer une logique complexe, envisagez de démarrer une tâche en arrière-plan. De plus, la valeur de retour de cette méthode est un booléen, où true indique que certaines actions sont encore en cours d'exécution, et false signifie que le travail est terminé.
  

---

Si vous souhaitez découvrir par vous-même la joie et l'émerveillement des récepteurs de diffusion, vous pouvez suivre ces liens vers des dépôts que j'ai configurés :

1. [Diffusion personnalisée](https://github.com/TomerPacific/MediumArticles/tree/master/BroadcastReceivers/CustomBroadcast) (avec déclaration dans le manifest)
  
2. [Enregistrement de diffusion](https://github.com/TomerPacific/MediumArticles/tree/master/BroadcastReceivers/RegisteringBroadcast) (sans déclaration dans le manifest)
  
3. [LocalBroadcastManager](https://github.com/TomerPacific/MediumArticles/tree/master/BroadcastReceivers/LocalBroadcastManager)
  

Diffusion terminée.