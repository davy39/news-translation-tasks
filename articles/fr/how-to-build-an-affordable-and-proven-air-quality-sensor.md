---
title: Comment construire un capteur de qualité de l'air abordable pour votre maison
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-03T20:10:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-affordable-and-proven-air-quality-sensor
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Copy-of-Particle-Sensor-3.png
tags:
- name: Electronics
  slug: electronics
- name: Google Docs
  slug: google-docs
- name: iot
  slug: iot
seo_title: Comment construire un capteur de qualité de l'air abordable pour votre
  maison
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  I got my hands on some of the mesh based Particle boards not too long ago. I’ve
  been itching to try them out but haven’t quite figured out the project.

  One thing has been bothering me tho...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor)**

J'ai mis la main sur certaines des cartes Particle basées sur le maillage il n'y a pas si longtemps. J'avais envie de les essayer mais je n'avais pas encore trouvé le projet idéal.

Une chose me tracassait cependant : la qualité de l'air. Je passe beaucoup de temps dans mon bureau à bricoler, souder, coder et écrire. J'éternue occasionnellement, alors je me suis toujours demandé, à quel point c'est mauvais ? La maison est également sujette à l'exposition à la moisissure pendant les mois chauds, ce qui m'inquiétait.

Alors pourquoi ne pas bricoler quelque chose ?

## Ce dont vous avez besoin
![Toutes les pièces nécessaires](https://www.freecodecamp.org/news/content/images/2020/08/ingredients.jpg)

Le capteur le plus important est le [Honeywell HPM series](https://www.honeywellscportal.com/honeywell-sensing-hpm-series-particle-sensors-datasheet-32322550-e-en.pdf) PM2.5/PM10. Celui-ci vous indique combien de microgrammes de matière flottent dans un volume cubique d'espace. c'est-à-dire qu'il compte les petites particules qui volent dans votre air.

En second lieu, il y a le [AMS CCS811](https://ams.com/documents/20143/36005/CCS811_DS000459_7-00.pdf). Ce capteur vous indique la quantité totale de composés organiques volatils dans l'air ainsi que des choses comme le C02. C'est un autre point de données intéressant à observer. J'avais précédemment placé ce capteur dans notre sous-sol pour être surpris et voir d'énormes pics de VOC et de niveaux de C02 provenant de notre fournaise (à combustion d'huile) qui s'allumait le matin. Il est temps de mieux ventiler !

Enfin, le capteur de température et d'humidité [Silicon Labs Si7021](https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf). Ces deux données environnementales sont utiles. Plus important encore, elles sont utilisées par l'algorithme du CCS811 pour calculer le TVOC et le C02. Compte tenu du coût du CCS811, je suis surpris qu'il n'ait pas ces mesures intégrées, mais peut-être dans leur prochaine révision...

## Câblage de l'ensemble
Il est temps de tout câbler ensemble. Au minimum, vous aurez besoin de :

1. Fil de connexion pour plaque d'essai sans soudure
2. Une plaque d'essai sans soudure
3. Une [carte de développement CCS811](https://www.adafruit.com/product/3566) d'Adafruit ([plus de détails ici](https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor?view=all))
4. Une [carte de développement Si7021 d'Adafruit](https://www.adafruit.com/product/3251) ([plus de détails ici](https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor?view=all))
5. [Une carte Particle de votre choix.](https://www.particle.io/mesh/)
6. Un [capteur de particules HPMA115](https://www.jaredwolff.com/store/dust-sensor/)
7. Câble Molex préassemblé pour le HPMA115 (Molex P/N 0151340803 ou similaire)
8. Quelques connecteurs à pas de 0,1"

J'ai inclus un exemple Fritzing avec ce projet. Il y a aussi une image de connexion ci-dessous :

![Diagramme de connexion Fritzing](https://www.freecodecamp.org/news/content/images/2020/08/particle-squared-hookup-diagram.jpg)
**Note :** le diagramme Fritzing original était incorrect. Les deux Vin du CCS811 et du Si7021 doivent être connectés au 3.3V sur la Particle

Un Adafruit Feather est utilisé pour représenter le Particle Argon. Particle n'a pas encore de modèles Fritzing.

Comme vous pouvez le voir, tout est connecté sauf le capteur PM2.5. Le brochage est inclus ci-dessous.

![Brochage du capteur de particules](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-23_at_12.31.03_PM.png)

Les broches les plus importantes sont les 5V, GND, RX et TX. Les autres peuvent rester déconnectées si vous le souhaitez. Voici les connexions appelées :

    5V     -> USB
    GND    -> GND
    RX     -> TX (sur l'Argon)
    TX     -> RX (sur l'Argon).

Voici une photo de tout assemblé sur une plaque d'essai sans soudure.

![Tout assemblé sur la plaque d'essai](https://www.freecodecamp.org/news/content/images/2020/08/DSC01397.jpg)

Une autre note importante est que j'ai modifié le câble pour le HPMA afin qu'il ait des broches mâles à l'extrémité. Cela a facilité l'insertion dans la plaque d'essai sans soudure. Voici un zoom :

![Broche soudée](https://www.freecodecamp.org/news/content/images/2020/08/DSC01370.jpg)

Lorsque vous achetez le câble pour le capteur PM2.5, il est livré avec 8 fils pré-installés. Pour simplifier les choses, vous pouvez retirer 4 des fils qui ne sont pas utilisés. La meilleure façon de faire est de prendre un outil à pointe fine (cure-dent, aiguille à coudre, etc.) et de le glisser sous les clips que j'ai indiqués en rouge ci-dessous :

![Clips maintenant les fils en place](https://www.freecodecamp.org/news/content/images/2020/08/DSC01371.jpg)

Ensuite, une fois que vous avez votre outil pointu en dessous, tirez sur le fil et il devrait glisser.

Maintenant vous avez moins de fils et moins de maux de tête. Vous pouvez utiliser cette technique pour modifier n'importe quel connecteur de type Molex.

## Plomberie du firmware
Pour ce projet, j'ai décidé de garder mon code cohérent avec l'API de type Wiring/Arduino. Cela signifie du C++ orienté objet. Cela fait un moment que je n'ai pas codé en C++, alors lorsque vous regardez la base de code et que vous vous demandez « pourquoi diable a-t-il fait ça !? » Désolé, pas désolé. ?

La meilleure façon de commencer est d'utiliser Visual Code avec les plugins Particle pour ce projet. [Cliquez ici pour commencer si vous n'êtes pas déjà configuré.](https://www.particle.io/workbench/)

### Si7021

Le Si7021 est super simple. Il n'a que 4 broches actives sur les 6 de la puce.

![Brochage du Si7021](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-23_at_1.18.21_PM.png)
(Copié directement de la documentation du Si7021)

La meilleure façon de lire le capteur de température/humidité est d'émettre une commande de lecture bloquante. Dans un monde embarqué, ce n'est pas idéal. Malheureusement, il n'y a aucun moyen de savoir quand les lectures sont prêtes car il n'y a pas de broche d'interruption.

Comme décrit dans la fiche technique, vous écrivez d'abord la commande puis vous tentez de lire directement depuis l'appareil. Le code ressemble à ceci :

```
    // Si7021 Température
    Wire.beginTransmission(SI7021_ADDRESS);
    Wire.write(SI7021_TEMP_HOLD_CMD); // envoie un octet
    Wire.endTransmission();           // arrête la transaction
    Wire.requestFrom(SI7021_ADDRESS, 2);

    // Obtenez la température brute de l'appareil
    uint16_t temp_code = (Wire.read() & 0x00ff) << 8 | (Wire.read() & 0x00ff);
```

Câblez l'adresse de l'appareil, écrivez la commande puis lisez ensuite le nombre d'octets nécessaires (deux dans ce cas). Le Si7021 étirera alors l'horloge jusqu'à ce que la lecture soit terminée.

Je n'ai pas bidouillé avec d'autres paramètres. Selon votre environnement, vous devrez peut-être ajuster la quantité de courant à alimenter le chauffage. Votre kilométrage peut varier, alors préparez-vous en conséquence !

Enfin, ces lectures sont lues sur un minuteur récurrent. J'utilisais à l'origine l'appel `millis()` et je calculais la différence entre le temps de départ et le temps actuel, mais cela finit par planter (en 50 jours environ). Au lieu de cela, j'ai décidé d'utiliser un minuteur système (similaire, sinon identique, à l'APP_TIMER dans le SDK NRF)

```
Timer timer(MEASUREMENT_DELAY_MS, timer_handler);
```

Ainsi, vous obtenez votre interruption toujours à `MEASUREMENT_DELAY_MS` quoi qu'il arrive ! (Dans mon cas, `MEASUREMENT_DELAY_MS` = 60000 ms == 60s)

### Le CCS811

Le CCS811 vous donne un peu plus de liberté pour jouer, mais il vient avec sa propre *spécialité*.

![Brochage du CCS811](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-23_at_2.34.14_PM.png)

Dans la plupart des cas, la broche ADDR est mise à bas. Cette broche modifie un bit de l'adresse. Cela est utile si vous avez deux appareils identiques ou deux appareils avec la même adresse sur le même bus I2C.

Le CCS811 dispose également de quelques broches d'entrée et de sortie pratiques. La plus importante est la broche d'interruption. Chaque fois qu'une lecture est terminée, cette broche de drain ouvert sera mise à bas. Elle ne sera réinitialisée que lorsque vous lirez le registre de statut. Cela est idéal pour les lectures asynchrones, de sorte que vous ne bloquiez pas votre MCU.

Un point important est que le CCS811 nécessite que vous émettiez une commande « start ». Cela force le MCU interne à commencer à exécuter l'algorithme de détection TVOC/CO2. Si vous tentez de lire les registres de données avant que l'application ne soit démarrée, vous obtiendrez des données erronées. (La commande est 0x90)

Dans le firmware, le CSS811 est traité dans la même boucle que le Si7021. Le code récupère les données disponibles à partir des lectures asynchrones du CSS811. Pas de code bloquant !

### Le HPMA115

Le capteur de particules est un peu plus délicat. Lorsqu'il est allumé, l'appareil commence à envoyer des données de particules à intervalles réguliers. c'est-à-dire qu'il est en mode d'envoi automatique à chaque fois qu'il s'allume.

J'ai essayé précédemment de configurer l'appareil, mais parfois je n'obtenais pas de réponse. C'était toujours aléatoire. Cela me rendait fou.

Alors, afin d'éteindre l'appareil lorsque vous ne l'utilisez pas, je vous recommande vivement d'utiliser un interrupteur de charge. Non seulement cela économisera de l'énergie, mais selon Honeywell, cela augmentera également la durée de vie du ventilateur.

Le flux des lectures :

* Allumez-le toutes les minutes
* Attendez que les données soient envoyées
* Lisez la lecture de manière asynchrone via UART
* Éteignez-le
* Regroupez ces données dans le blob JSON à envoyer au serveur

Ainsi, il n'est pas nécessaire de bidouiller les registres. Toutes les raisons pour lesquelles I2C et même SPI sont de meilleurs bus de données que UART. Je veux juste que cela fonctionne !

![Tenue du HPMA115S0](https://www.freecodecamp.org/news/content/images/2020/08/DSC01372.jpg)

J'ai choisi ce capteur il y a un moment pour sa nature fermée. À mon avis, il est plus facile à intégrer. Mon cerveau d'ingénieur en électricité ne veut pas traiter des choses complexes. Donnez-moi une boîte et c'est parti.

## Faire fonctionner le tout
Pendant la phase de développement de ce projet, je voyageais à l'étranger. Le wifi médiocre ne suffisait pas et il fallait une éternité pour itérer sur le code. L'Argon avait également du mal à se connecter à l'AP de mon iPhone, alors j'ai abandonné cette idée tôt.

Alors, afin de développer le code qui ne nécessitait pas internet, j'ai mis l'appareil en mode manuel. Que fait le mode manuel ? Il permet au code de commencer l'exécution sans être connecté au cloud Particle. Ainsi, vous pouvez prendre des lectures toute la journée sans avoir à être connecté au Wifi. Vous pouvez mettre l'appareil en mode manuel en plaçant cette définition dans votre fichier `.ino` :

```
SYSTEM_MODE(MANUAL);
```

Dans les applications alimentées par batterie, c'est idéal. Le Wifi est coûteux en termes de puissance et vous n'avez pas besoin de l'exécuter si vous n'en avez pas besoin !

Dans une expérience précédente, j'ai découvert qu'il fallait environ 10 à 15 secondes pour passer de rien à l'envoi de données au cloud Particle. C'est un **long moment** dans le monde embarqué. C'est l'une des principales raisons pour lesquelles je pense que Particle a sorti son système de maillage. Cela permet aux nœuds terminaux en veille (ou aux nœuds qui prennent des données et les envoient périodiquement à un point central) de fonctionner beaucoup plus longtemps que leurs cousins basés sur le Wifi.

N'oubliez pas que vous devrez exécuter la fonction `Particle.connect()` afin de vous connecter au wifi en mode manuel. Ou si vous êtes prêt à vous reconnecter, retirez `SYSTEM_MODE(MANUAL);` de votre fichier `.ino`.

### Changer les identifiants Wifi

Pendant mon expérience pour faire fonctionner mon wifi, j'ai découvert quelques outils Particle pratiques pour changer les identifiants wifi, etc. En maintenant le bouton mode pendant le fonctionnement, l'appareil finit par clignoter en bleu. Une fois qu'il clignote en bleu, vous pouvez émettre un `particle serial wifi` qui vous guidera tout au long du processus de changement des identifiants.

Le processus ci-dessus est bien plus rapide que l'utilisation de l'application iPhone/Android. Je pensais que l'application était cool au début, mais elle prend tellement de temps pour scanner et connecter vos appareils.

[Plus d'informations sur cette procédure ici.](https://docs.particle.io/tutorials/device-os/led/argon/#network-reset-fast-blinking-blue-)

### Récupération lorsque les choses tournent mal

J'ai dû récupérer mon Argon pendant mon processus de développement. J'ai fait quelques recherches et j'ai découvert que la reprogrammation du système d'exploitation, de l'application et du chargeur de démarrage semblait faire l'affaire.

Obtenez les fichiers ici : [Version 0.9.0 (Gen 3) · particle-iot/device-os · GitHub](https://github.com/particle-iot/device-os/releases/tag/v0.9.0) (À la date de rédaction, la dernière version est 0.9.0)

Ensuite, programmez ces fichiers en [mode DFU](https://docs.particle.io/tutorials/device-os/led/photon/#dfu-mode-device-firmware-upgrade-) en maintenant le bouton `mode` après avoir appuyé une fois sur le bouton `reset`.

```
particle flash --usb system-part1-0.9.0-argon.bin
particle flash --usb tinker-0.9.0-argon.bin
```

Programmez celui-ci en [mode écoute](https://docs.particle.io/tutorials/device-os/led/photon/#listening-mode) :

```
particle flash --serial bootloader-0.9.0-argon.bin
```

*Note : le suffixe `-argon` peut être différent selon ce que vous programmez. Les autres options sont `-boron` et `-xenon`.

## Surveillance en ligne de commande
Enfin, l'une des commandes les plus utiles est celle-ci :

`particle serial monitor --follow`

Cela vous permet d'utiliser l'interface `Serial` USB pour recevoir des messages de débogage de l'appareil. Cela est similaire à la connexion d'un appareil FTDI à un Arduino.

Par exemple, je peux déboguer une partie du code, donc je veux voir certaines données. Dans la fonction `Setup()`, je m'assurerai d'exécuter `Serial.begin()`, puis plus tard, je ferai un `Serial.printf("data: %d",data.tvoc);` afin qu'il soit envoyé via l'interface Serial USB.

Serial UART pour le débogage, c'est une belle chose.

## Publication
Une chose que j'ai découverte pendant le processus de développement était les limites de publication de la plateforme Particle. Pour un seul appareil, vous ne pouvez pas `Particle.Publish` plus de 4 morceaux de données en une seconde. Même si je prenais des données toutes les minutes, j'envoyais 6 morceaux de données individuelles au serveur en même temps. Après des tests, je me suis rapidement demandé pourquoi mes lectures de C02 et TVOC avaient disparu.

J'avais trouvé le coupable.

Alors, pour faire fonctionner les choses, j'ai dû les formater en un blob JSON. Voyez comment je l'ai fait exactement ci-dessous :

```
String out = String::format("{\"temperature\":%.2f,\"humidity\":%.2f,\"pm25\":%d,\"pm10\":%d,\"tvoc\":%d,\"c02\":%d}",si7021_data.temperature,si7021_data.humidity,hpma115_data.pm25,hpma115_data.pm10,ccs811_data.tvoc,ccs811_data.c02);
Particle.publish("blob", out , PRIVATE, WITH_ACK);
```

J'ai créé une structure JSON puis utilisé `String::format` pour insérer chaque morceau où ils devaient être. Si vous exécutez votre appareil via LTE, cela vous fera envoyer plus de données que nécessaire. Il existe de meilleures options comme [Protocol Buffers](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/) ou l'utilisation de [MessagePack](https://msgpack.org). Si vous traitez des données complexes, je recommande le premier en raison de sa nature programmatique. De plus, vous pouvez l'utiliser avec presque n'importe quel langage de programmation. Donc du web à l'embarqué ? Aucun problème.

Après chaque minute, j'envoie les données uniquement lorsque les trois capteurs ont été lus. J'utilise trois valeurs booléennes séparées pour déterminer l'état des lectures des capteurs. Une fois qu'elles ont toutes été définies sur `true`, j'invoque l'appel `Particle.Publish`.

Ensuite, après la publication, je réinitialise toutes les variables comme suit :

```
ccs811_data_ready = false;
si7021_data_ready = false;
hpma115_data_ready = false;
```

Ensuite, tout recommence. Vous pouvez également créer une structure de statut qui contient chacun de ces drapeaux à l'intérieur. Compte tenu du fait que je n'ai que trois points de données, je n'ai pas fait l'effort supplémentaire.

## Utilisation d'Adafruit IO

Une façon de publier est d'utiliser la plateforme IO d'Adafruit. Voici comment commencer.

1. Créez un compte ici : https://io.adafruit.com
2. Ensuite, créez des flux pour chaque type de données. Nous en aurons besoin de 6 au total.
![Créer un flux dans Adafruit IO](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-19_at_6.47.38_PM.png)

3. Pour chaque flux, ajoutez un Webhook.
![Ajouter un webhook pour les données](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-19_at_6.45.27_PM.png)
4. Prenez chaque adresse de webhook et créez un nouveau Webhook dans la console Particle
5. Changez le `Format de la requête` en JSON
6. Ensuite, sous `Paramètres avancés`, cliquez sur `Personnalisé` pour les **DONNÉES JSON**
7. Remplacez ce qui s'y trouve en utilisant [les modèles mustache](https://docs.particle.io/reference/device-cloud/webhooks/#variable-substitution). Adafruit IO recherche une clé JSON appelée `value`. Donc définissez-la comme ceci :
   ```
   {
    "value":"{{{c02}}}"
   }
   ```

   Vous pouvez remplacer `c02` par n'importe quelle clé de votre blob JSON. Pour rappel, le blob JSON actuel ressemble à ceci :

   ```
   {
    "temperature":21.2,
    "humidity":30,
    "pm10":2,
    "pm25":1,
    "tvoc":650,
    "c02":1001
   }
   ```
8. Répétez cela autant que nécessaire jusqu'à ce que tous les flux aient un Webhook correspondant configuré.
9. Enfin, vous pouvez créer un tableau de bord pour les voir tous au même endroit. C'est simple, suivez simplement les invites à l'écran. :)

![Liste des flux](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-19_at_7.04.16_PM.png)
![Graphiques des flux](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-03-19_at_7.16.17_PM.png)

Vous pouvez consulter mon [tableau de bord en direct ici](https://io.adafruit.com/jaredwolff/dashboards/air-quality-sensor). C'est ingénieux et juste une autre façon d'afficher vos données.

**Note de bas de page :** Mes premières impressions sur Adafruit IO sont bonnes. C'était facile à configurer et à commencer à utiliser. Le principal inconvénient est qu'il est fastidieux, surtout si vous avez plus d'une poignée de points de données. Mais peut-être qu'ils régleront cela à l'avenir !

**Mise à jour :** Si vous avez plusieurs morceaux de données. Vous pouvez pointer votre intégration Particle vers un seul point de terminaison. Assurez-vous simplement que les données sont dans le même groupe ! Voici un exemple de plusieurs valeurs envoyées au même groupe :

```
{
  "feeds": [
    {
      "key": "tvoc",
      "value": "{{{tvoc}}}"
    },
    {
      "key": "c02",
      "value": "{{{c02}}}"
    },
    {
      "key": "temperature",
      "value": "{{{temperature}}}"
    },
    {
      "key": "humidity",
      "value": "{{{humidity}}}"
    },
    {
      "key": "pm2-dot-5",
      "value": "{{{pm25}}}"
    },
    {
      "key": "pm10",
      "value": "{{{pm10}}}"
    }
  ]
}
```

Où votre URL devrait ressembler à ceci :

```
https://io.adafruit.com/api/v2/<USERNAME>/groups/<GROUPNAME>/data
```

Cela devrait garder votre page d'intégration Particle un peu plus saine !

## Comprendre les lectures
Les lectures peuvent être déroutantes. Voici la ventilation de leur fonctionnement :

1. L'humidité est affichée en pourcentage relatif. Il s'agit de l'humidité relative que nous connaissons et aimons. N'oubliez pas qu'elle peut différer de celle de l'extérieur. Cela dépend du fait que votre maison soit climatisée ou si vous utilisez un chauffage, etc.
2. La température est en degrés Celsius (peut être modifiée dans le firmware si vous le souhaitez)
3. Le TVOC est en ppb (parties par milliard). Les COV peuvent se présenter sous la forme de produits chimiques nocifs que vous avez autour de la maison. Pour plus d'informations sur les COV, consultez ce [lien de l'EPA](https://www.epa.gov/indoor-air-quality-iaq/volatile-organic-compounds-impact-indoor-air-quality).
4. Le C02 est en ppm (parties par million). Nous respirons de l'oxygène et exhalons du dioxyde de carbone. Vous pouvez constater que vos niveaux de VOC et de C02 augmentent lorsque vous êtes dans la pièce. Le C02 est également corrélé aux VOC. [Plus d'informations dans la fiche technique.](https://ams.com/documents/20143/36005/CCS811_DS000459_7-00.pdf)
5. PM10. Est en µg/m3 (microgrammes par mètre cube). Le capteur de particules utilise un laser dispersé qui traverse la chambre à air vers un capteur de l'autre côté. Plus les rayons sont bloqués, plus il y a de particules dans l'air. Le capteur de particules effectue ensuite des calculs pour déterminer la quantité de particules dans un certain volume et ainsi votre µg/m3.
6. PM2.5 est le même que ci-dessus mais il suit des particules beaucoup plus petites. (Inférieures ou égales à 2,5 µm de taille !) [Plus d'informations sur le site de l'EPA ici.](https://www.epa.gov/pm-pollution/particulate-matter-pm-basics)

## Vous ne vous souciez pas de quelque chose que vous ne pouvez pas contrôler ?

[Consultez mon tutoriel sur la création de votre propre tableau de bord IoT à l'apparence incroyable.](https://www.jaredwolff.com/how-to-make-an-amazing-looking-iot-dashboard-in-no-time/)

## Vous l'avez fait !
Félicitations. Vous êtes arrivé jusqu'ici. Vous méritez une journée au spa. Ou peut-être une glace au chocolat. Ou si vous vous sentez vraiment aventureux, les deux, en même temps ?? ?

Après avoir construit l'un de ceux-ci, vous pourriez avoir l'impression que votre temps vaut la peine d'être investi ailleurs. Peut-être voulez-vous construire un backend web cool avec des graphiques et des algorithmes plus sophistiqués. Peut-être même utiliser un peu d'apprentissage automatique (pourquoi pas !)

Si vous voulez quelque chose de déjà assemblé et disponible, vous devriez consulter le Particle^2 (prononcé Particle Squared). Il a tout ce dont vous avez besoin ici, y compris la possibilité d'allumer et d'éteindre le capteur de particules HPM. Vous pouvez même le faire fonctionner sur batteries ! Alors placez ce truc n'importe où. [Consultez-le ici.](https://www.jaredwolff.com/store/particle-squared/)

Voici la vidéo complète sur le Particle Squared.

%[https://www.youtube.com/watch?v=IR2W0GmRKk8&t=]

## Code et Source
Ce projet entier est publié sous la licence Creative Commons Share-Alike. [Obtenez le code source et les fichiers matériels ici.](https://www.jaredwolff.com/files/air-quality/#main)

## Préparez-vous pour le Guide Ultime
Cet article est un extrait de mon prochain Guide Ultime sur Particle Mesh. Les premiers abonnés bénéficient d'une réduction lorsqu'il devient disponible ! [Cliquez ici pour vous inscrire.](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/)