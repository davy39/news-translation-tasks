---
title: 2 meilleures façons de faire fonctionner Particle Mesh avec Blynk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-29T13:01:00.000Z'
originalURL: https://freecodecamp.org/news/2-best-ways-to-get-particle-mesh-working-with-blynk
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Copy-of-Mesh-to-Blynk.png
tags:
- name: particle
  slug: particle
seo_title: 2 meilleures façons de faire fonctionner Particle Mesh avec Blynk
seo_desc: 'By Jared Wolff

  This post is originally from my blog on www.jaredwolff.com.

  Writing an app takes time. It takes even more time to write one that works with
  hardware.

  Luckily there''s a solution to this problem.

  Enter Blynk.

  It''s an app that connects to...'
---

Par Jared Wolff

**Cet article provient à l'origine de mon blog sur [www.jaredwolff.com](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/).**

Écrire une application prend du temps. Cela prend encore plus de temps pour en écrire une qui fonctionne avec du matériel.

Heureusement, il existe une solution à ce problème.

Voici [Blynk](http://blynk.io).

C'est une application qui se connecte à votre matériel. Elle dispose d'une interface glisser-déposer avec des widgets préconstruits. Cela signifie que vous pouvez construire une application en quelques secondes. Ensuite, téléchargez les lectures des capteurs de votre appareil en quelques minutes.

Blynk fonctionne avec Argon, Boron ou Xenon connecté à l'ethernet. Malheureusement, il ne fonctionne pas sur un réseau Particle Mesh. Dans cet article, vous apprendrez quelques solutions pour faire fonctionner vos projets basés sur le mesh.

## Du Particle Cloud à Blynk

Commençons par le cas d'utilisation le plus simple : obtenir des données de n'importe quel appareil Particle vers Blynk.

Les données de qualité de l'air de [Particle Squared](http://jaredwolff.com/homemade-indoor-air-quality-sensor/) sont parfaites pour cet exemple. Je vais donc les utiliser.

Commençons par créer un nouveau projet Blynk

![Créer un projet dans Blynk](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/IMG_2233-2a80b63a-b88b-4e58-a50b-5fc02923ae23.png)

Récupérez le **Auth Token**, nous en aurons besoin dans un instant. Vous pouvez **appuyer sur le Auth Token** pour le copier dans votre presse-papiers.

Ensuite, ajoutons un **SuperChart** pour cet exemple.

![Ajouter un SuperChart](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/IMG_2231-308d94bf-63f4-40a6-98e3-e49ced05c90a.png)

Configurez le SuperChart pour utiliser une broche virtuelle. Nous n'avons pas accès aux broches matérielles réelles de l'appareil. **V0** est un bon choix.

![Sélectionner la broche virtuelle 0](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/IMG_2232-e53a0997-453e-47ee-b2d1-27a30dc12dfc.png)

Pour mettre à jour les valeurs dans Blynk, nous devons nous connecter d'une manière ou d'une autre. La meilleure façon est d'utiliser une **Intégration** dans la **Console Particle.**

Dans la Console Particle, cliquez sur l'icône en dessous de l'icône du terminal. Ensuite, cliquez sur **Nouvelle Intégration.**

![Créer une nouvelle intégration dans la Console Particle](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Screen_Shot_2019-07-27_at_10-33b85b6e-d685-4c1a-b639-423df7b2dd85.43.37_AM.png)

Regardez l'exemple ci-dessous pour voir comment j'ai tout rempli.

![Entrez toutes les informations dans l'écran de Nouvelle Intégration](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Screen_Shot_2019-07-24_at_3-a5433944-8a2a-4b0d-81b6-faa4c038bd65.27.06_PM.png)

Particle Squared utilise le **Nom de l'Événement** comme ****`blob`. Pour d'autres projets, cela peut être différent. **Rappel :** votre nom d'événement est le même que celui de `Particle.publish(eventName, data)`.

L'**URL** est définie pour utiliser l'adresse `blink-cloud.com`. Selon leur API, un exemple d'URL ressemble à ceci :

![Appel API de l'écriture de la broche du cloud Blink](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Screen_Shot_2019-07-24_at_4-730022d3-f758-43b3-b4cc-bb3012d22d9e.44.06_PM.png)

Je vais également l'inclure ici pour qu'il soit plus facile à copier

```
http://blynk-cloud.com/auth_token/update/pin?value=value

```

Remplacez `auth_token` par le **Auth Token** que nous avons obtenu précédemment.

Remplacez `pin` par la broche virtuelle que nous voulons modifier. Dans ce cas, **V0**

Remplacez la `value` par la valeur que vous souhaitez utiliser.

Nous allons référencer l'une des valeurs dans le `blob` de Particle Squared. Il est organisé comme ceci :

```
{
  "temperature": 28.60,
  "humidity": 45.00,
  "sgp30_tvoc": 18,
  "sgp30_c02": 400,
  "bme680_temp": 27.36,
  "bme680_pres": 1012.43,
  "bme680_hum": 43.80,
  "bme680_iaq": 43.90,
  "bme680_temp_calc": 27.30,
  "bme680_hum_calc": 43.97
}

```

Particle utilise des [modèles mustache](http://mustache.github.io/mustache.5.html). Comme vous pouvez le voir dans la capture d'écran ci-dessus, vous pouvez définir `value` sur `{{{temperature}}}`.

**Note :** Si vous travaillez sur votre propre projet, il est important de publier avec JSON. En référence, la commande `Particle.publish` ressemble à ceci :

```
// Publier des données
Particle.publish("blob", String::format("{\"temperature\":%.2f,\"humidity\":%.2f}",si7021_data.temperature, si7021_data.humidity) , PRIVATE, WITH_ACK);

```

Cliquez sur le **grand bouton bleu Enregistrer** en bas de l'écran. Ensuite, nous pouvons passer à l'étape suivante !

### Test

Depuis la création de notre Intégration Webhook Particle, elle publie des données vers Blynk. Allons voir si cela fonctionne.

Tout d'abord, retournons à l'application Blynk. **Appuyez sur le bouton Lecture en haut à droite** dans l'écran Blynk.

![Regarder les données arriver dans l'application Blynk](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/IMG_2234-43cebeaa-2dd4-401c-84e5-b365953f4a66.png)

Si votre intégration fonctionne depuis un moment, vous devriez voir le graphique se remplir avec des données ! Dans le cas où vous ne voyez rien, vérifions les logs.

**Retournez à votre intégration** et **faites défiler vers le bas**. Nous voulons voir s'il y a des erreurs.

Vous ne savez pas à quoi cela ressemble ? Voici un exemple d'intégration avec des erreurs :

![Erreurs d'intégration de la console Particle](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Screen_Shot_2019-07-24_at_4-47e820b4-1636-406e-8ba1-ff22cf899478.55.36_PM.png)

Vous pouvez faire défiler plus bas pour enquêter sur la raison de l'erreur.

![Enquêtez davantage sur l'échec de l'intégration Particle](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Screen_Shot_2019-07-24_at_4-2e5843f3-1960-41a7-90b0-d80432d6ef2d.56.36_PM.png)

Tout en bas, on voit la réponse du serveur. Selon le service, ils vous donneront des informations sur la raison pour laquelle votre appel API a échoué. Dans mon cas, il manquait des valeurs pour deux champs.

### Particle vers Blynk fonctionne !

Vous avez maintenant une méthode de base pour publier sur une broche virtuelle dans Blynk. Il y a cependant des inconvénients. Plus important encore, vous devrez créer une intégration pour chaque broche virtuelle de signal. Si vous avez huit lectures, cela signifie huit intégrations.

Dommage.

Dans la section suivante, vous apprendrez une autre façon de configurer Blynk. C'est parti !

## Mesh Local Utilisant la Bibliothèque Blynk

![Particle Mesh vers Blynk](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Mesh_to_Blynk-0a66867b-a193-4b97-801a-b780c9a481e2.png)

Contrairement à la première méthode, nous allons nous concentrer uniquement sur la modification du firmware.

Nous utiliserons un Argon, Boron ou Xenon connecté à Ethernet et un Xenon régulier. Pour le reste de ce tutoriel, nous appellerons ces appareils un "routeur de bord".

Le Xenon exécutera le code Particle Squared. Au lieu d'utiliser `Particle.publish`, nous utiliserons `Mesh.publish`. Cela nous permet de publier uniquement sur le réseau mesh local.

Pendant ce temps, le routeur de bord écoute le message. Il collecte les valeurs puis utilise l'API Blynk pour les publier dans l'application.

Voici les étapes :

### Configurer notre Routeur de Bord

Ouvrez le menu en appuyant sur **Cmd+Shift+P**. Tapez **Installer la Bibliothèque.**

![Installer la bibliothèque dans Visual Studio Code](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Screen_Shot_2019-07-28_at_4-f8149823-96fc-460f-b47e-2bcf56b670c2.50.29_PM.png)

Ensuite, entrez **blynk.** La bibliothèque devrait se télécharger si ce n'est pas déjà fait.

Une fois installée, vous pouvez inclure la bibliothèque en haut de votre fichier `.ino` comme suit :

```
#include <blynk.h>

```

Dans notre fonction `setup()`, initialisons la bibliothèque Blynk :

```
// Mettre l'initialisation comme pinMode et les fonctions begin ici.
Blynk.begin(auth);

```

Dans notre fonction `setup()`, abonnez-vous à l'événement `temperature`. Le Xenon connecté générera cet événement.

```
// S'abonner aux événements de température
Mesh.subscribe("temperature",tempHandler);

```

Définissez `tempHandler` comme ceci pour l'instant :

```
// Gestionnaire d'événements de température pour le mesh
void tempHandler(const char *event, const char *data){
}

```

Dans la fonction `loop()`, assurez-vous d'avoir `Blynk.run();`

```
// loop() s'exécute encore et encore, aussi rapidement qu'il peut s'exécuter.
void loop() {
  // Le cœur de votre code vivra probablement ici.
  Blynk.run();
}

```

Enfin, pour `tempHandler`, nous pouvons ajouter une impression de débogage pour surveiller les événements. J'ai utilisé quelque chose comme ceci :

```
Serial.printlnf("event=%s data=%s", event, data ? data : "NULL");

```

Particle utilise cela dans certains de leurs exemples. C'est parfait pour nos besoins également !

**Note :** assurez-vous d'avoir appelé `Serial.begin()` dans votre fonction `Setup()` !

Maintenant, nous avons `tempHandler` pour recevoir les données du Xenon. Le routeur de bord peut maintenant prendre ces données et les télécharger vers Blynk. Utilisons la fonction `Blynk.virtualWrite` pour cela :

```
// Écrire les données
Blynk.virtualWrite(V0, data);

```

Cela écrira la valeur de température d'un Xenon vers la broche `V0`. Si vous avez utilisé autre chose que V0, assurez-vous de changer cette valeur ici. (C'est la même configuration que l'exemple précédent _Particle Cloud vers Blynk_)

![DataStream V0](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/IMG_2232-e53a0997-453e-47ee-b2d1-27a30dc12dfc.png)

Le code final pour le routeur de bord devrait ressembler à ceci. Compilez et flashez-le sur votre appareil lorsque vous êtes prêt !

```
/*
 * Projet blynk-argon-forwarder
 * Description : Argon Blynk forwarder pour Particle Mesh. Transfère les données des appareils connectés au mesh vers Blynk.
 * Auteur : Jared Wolff
 * Date : 7/25/2019
 */

#include <blynk.h>

char auth[] = "<ENTREZ VOTRE CLÉ D'AUTHENTIFICATION>";

// Gestionnaire d'événements de température pour le mesh
void tempHandler(const char *event, const char *data){
  Serial.printlnf("event=%s data=%s", event, data ? data : "NULL");

  // Écrire les données
  Blynk.virtualWrite(V0, data);
}

// setup() s'exécute une fois, lorsque l'appareil est allumé pour la première fois.
void setup() {

  // Serial pour le débogage
  Serial.begin();

  // Mettre l'initialisation comme pinMode et les fonctions begin ici.
  Blynk.begin(auth);

  // S'abonner aux événements de température
  Mesh.subscribe("temperature",tempHandler);

}

// loop() s'exécute encore et encore, aussi rapidement qu'il peut s'exécuter.
void loop() {
  // Le cœur de votre code vivra probablement ici.
  Blynk.run();

}

```

N'oubliez pas de définir `auth` en utilisant le `AUTH TOKEN` dans l'application Blynk !

### Configurer un Xenon

![Xenon!](https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/Copy_of_Compose-a34be8da-a352-4a76-af8c-8c83e65efe50.png)

Créez un nouveau projet. Cette fois, il sera pour le Xenon capturant les "données de température".

Ajoutons une variable appelée `time_millis` en haut du fichier. Le type est `system_tick_t`. Nous l'utiliserons pour créer un minuteur de délai simple pour les lectures de température.

```
// Variable globale pour suivre le temps (utilisée pour les lectures du capteur de température)
system_tick_t time_millis;

```

Pour l'intervalle, utilisons une définition de préprocesseur

```
#define INTERVAL_MS 2000

```

Maintenant, associons-les dans la fonction `loop()`. Nous utiliserons une instruction `if` pour comparer notre temps système actuel avec celui du dernier événement plus le décalage. Si vous avez besoin d'un minuteur simple, c'est l'une des meilleures façons de le faire !

```
// Vérifier si notre intervalle > 2000ms
  if( millis() - time_millis > INTERVAL_MS ) {
  }

```

Une fois à l'intérieur, assurez-vous de réinitialiser `timer_millis` :

```
		// Définir le temps sur le 'temps actuel' en millisecondes
    time_millis = millis();

```

Ensuite, nous générerons la valeur de température en utilisant la fonction `random()`. Nous utiliserons la variante à deux paramètres. Ainsi, nous pouvons définir la valeur minimale et la valeur maximale :

```
    // Créer un nombre aléatoire
    int rand = random(20,30);

```

Enfin, nous publierons la valeur avec `Mesh.publish` :

```
    // Publier notre valeur "temperature"
    Mesh.publish("temperature",String::format("%d",rand));

```

Lorsque cet exemple s'exécute, la température est diffusée sur le réseau mesh. Ensuite, le routeur de bord la reçoit et la transfère à Blynk !

Vous pouvez flasher ce firmware quand vous êtes prêt. Voici le code complet pour le Xenon afin que vous puissiez comparer :

```
/*
 * Projet blynk-xenon-rgb
 * Description : Recevoir le niveau RGB du routeur de bord connecté. Envoie des valeurs de température simulées via le mesh au cloud Blynk.
 * Auteur : Jared Wolff
 * Date : 7/25/2019
 */

// Fréquence de mise à jour de la température
#define INTERVAL_MS 2000

// Variable globale pour suivre le temps (utilisée pour les lectures du capteur de température)
system_tick_t time_millis;
// setup() s'exécute une fois, lorsque l'appareil est allumé pour la première fois.
void setup() {

  // Définir le temps sur 0
  time_millis = 0;

}

// loop() s'exécute encore et encore, aussi rapidement qu'il peut s'exécuter.
void loop() {

  // Vérifier si notre intervalle > 2000ms
  if( millis() - time_millis > INTERVAL_MS ) {
    // Définir le temps sur le 'temps actuel' en millisecondes
    time_millis = millis();

    // Créer un nombre aléatoire
    int rand = random(20,30);

    // Publier notre valeur "temperature"
    Mesh.publish("temperature",String::format("%d",rand));

  }

}

```

### Testons-le !

Maintenant que nous avons programmé les deux appareils, faisons-les communiquer entre eux.

J'ai déjà configuré l'Argon avec un réseau mesh appelé **8f-9.** Je vais expliquer comment connecter le Xenon avec le CLI. Vous pouvez également utiliser l'application Particle.

Tout d'abord, connectons le Xenon à l'USB et mettons-le en mode écoute. Après la connexion, maintenez le **bouton Mode** enfoncé jusqu'à ce qu'il clignote en **bleu.**

<video width="100%" height="500px" controls=""><source src="https://www.jaredwolff.com/two-best-ways-to-get-particle-mesh-working-with-blynk/images/720p.mov" type="video/mp4"></video>

Ensuite, utilisez le CLI pour configurer le réseau mesh. Tout d'abord, obtenons l'ID de l'appareil :

```
Jareds-MacBook-Pro:nrfjprog.sh jaredwolff$ particle identify
? Quel appareil vouliez-vous dire ?
  /dev/tty.usbmodem146401 - Argon
  /dev/tty.usbmodem146101 - Xenon

```

Si vous avez plusieurs appareils connectés, assurez-vous de sélectionner le bon ! Si vous y êtes invité, sélectionnez un appareil. Votre sortie devrait ressembler à ceci :

```
Votre identifiant de périphérique est e00fce682d9285fbf4412345
Votre version de firmware système est 1.3.0-rc.1

```

Nous aurons besoin de l'**id** pour l'étape suivante. Maintenant, exécutons la commande `particle mesh`.

```
particle mesh add <xenon id> <id de votre argon, boron, etc>

```

Voici un exemple ci-dessous :

```
particle mesh add e00fce682d9285fbf4412345 hamster_turkey
? Entrez le mot de passe du réseau [masqué]
  Ajout de l'appareil au réseau...

```

À la fin, vous verrez :

```
Terminé ! L'appareil devrait maintenant se connecter au cloud.

```

Ce processus n'est pas parfait. Pendant l'étape `Ajout de l'appareil au réseau...`, j'ai dû supprimer le Xenon en utilisant `particle mesh remove`. Ensuite, j'ai relancé la commande `particle mesh add` après avoir réinitialisé l'Argon.

Maintenant, voici la finale.

Connectez les deux appareils à la série en utilisant `particle serial monitor --follow`

Si vous avez les deux appareils connectés, `particle serial monitor` vous demandera de sélectionner :

```
Jareds-MacBook-Pro:blynk-xenon-rgb jaredwolff$ particle serial monitor --follow
Sondage pour un périphérique série disponible...
? Quel appareil vouliez-vous dire ? /dev/tty.usbmodem146101 - Xenon
Ouverture du moniteur série pour le port com : "/dev/tty.usbmodem146101"
Moniteur série ouvert avec succès :

```

**Rappel :** Vous devez exécuter `particle serial monitor` pour chaque appareil auquel vous souhaitez vous connecter.

Si tout fonctionne, vous verrez probablement une sortie du routeur de bord !

```
Moniteur série ouvert avec succès :
event=temperature data=21
event=temperature data=28
event=temperature data=21
event=temperature data=27
event=temperature data=28
event=temperature data=26
event=temperature data=23
event=temperature data=26
event=temperature data=21

```

En regardant l'application, le **Super Chart** devrait réagir à ces nouvelles données.

Comparez la dernière valeur dans la ligne de commande à la dernière sur le graphique ? Correspondent-elles ? Si oui, vous êtes arrivé à la fin de cet exemple !

## Conclusion

Dans ce tutoriel, vous avez appris comment transférer les données du Particle Cloud vers Blynk. Vous avez également appris comment faire de même en utilisant un Particle Argon, Boron ou Xenon connecté à l'ethernet. Awe yea. 💡

Maintenant que vous avez les outils pour Blink-ifier vos projets alimentés par Particle Mesh, il est temps de se mettre au travail !

**Vous aimez cet article ?**

Cet article est un extrait de mon prochain _Guide Ultime de Particle Mesh_. Je partagerai plus de contenu exclusif avec ma liste de diffusion à mesure qu'il se rapproche du lancement. [Vous pouvez vous inscrire ici pour les mises à jour.](https://jaredwolff.com/the-ultimate-guide-to-particle-mesh/)

**Vous avez encore des questions ?**

Laissez un commentaire ou [envoyez-moi un message.](https://www.jaredwolff.com/about)