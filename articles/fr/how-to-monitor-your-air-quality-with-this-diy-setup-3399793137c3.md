---
title: Comment surveiller la qualité de l'air avec ce montage DIY
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T16:02:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-monitor-your-air-quality-with-this-diy-setup-3399793137c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d43dkbPP_oxPGy6o0WWvnw.jpeg
tags:
- name: Electronics
  slug: electronics
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Raspberry Pi
  slug: raspberry-pi
seo_title: Comment surveiller la qualité de l'air avec ce montage DIY
seo_desc: 'By Bert Carremans

  With a Raspberry Pi, low-cost gas sensors, and a remote-controlled switch, you can
  control the air quality in your house.

  The air we breathe indoors is not always healthier than the air outside.

  According to a study of the E.U. Join...'
---

Par Bert Carremans

#### Avec un Raspberry Pi, des capteurs de gaz peu coûteux et un interrupteur télécommandé, vous pouvez contrôler la qualité de l'air dans votre maison.

L'air que nous respirons à l'intérieur n'est pas toujours plus sain que l'air extérieur.

Selon une étude du [Centre commun de recherche de l'U.E.](http://europa.eu/rapid/press-release_IP-03-1278_en.htm), on peut trouver une large gamme de polluants atmosphériques à l'intérieur. Certains d'entre eux sont toxiques, ou peuvent provoquer des mutations génétiques ou des cancers. Les facteurs qui influencent la qualité de l'air intérieur sont :

* l'air ambiant, ou l'air extérieur
* l'étanchéité à l'air et la ventilation du bâtiment
* les sources intérieures comme la fumée de tabac, les gaz de chauffage, les produits de consommation, etc.

Savez-vous combien de temps vous passez à l'intérieur ? Selon l'Agence de protection de l'environnement, les Américains passent [87 % de leur temps à l'intérieur](https://www.nature.com/articles/7500165). En Europe, ce pourcentage moyen est de 90 %, selon le JRC. Et plus nous passons de temps à l'intérieur, plus nous inhalons de polluants.

Il serait donc intéressant de suivre la qualité de l'air intérieur. Dans cet article, je vais expliquer comment j'ai fait cela avec un [Raspberry Pi](https://www.raspberrypi.org/), un [GrovePi](https://www.dexterindustries.com/grovepi/) et quelques capteurs. Nous allons télécharger les données des capteurs vers une base de données [Firebase](https://firebase.google.com/) et visualiser les tendances avec [Dash](https://dash.plot.ly/).

Lorsque les niveaux de polluants atteignent un niveau malsain, nous pouvons envoyer une notification d'alerte pour nous avertir.

De plus, il serait formidable si nous pouvions démarrer automatiquement la ventilation pour purifier l'air. Cela peut être fait avec un [interrupteur télécommandé d'Energenie](https://www.raspberrypi.org/blog/controlling-electrical-sockets-with-energenie-pi-mote/).

#### Raspberry Pi et GrovePi

![Image](https://cdn-media-1.freecodecamp.org/images/A50dJjzt1x9eSTy0qoMm8trrsQ0M3GiAGM1t)
_Raspberry Pi modèle 2B_

Dans ce projet, j'utiliserai un Raspberry Pi modèle 2B. Le Raspberry Pi est un petit ordinateur à faible coût. Il permet aux programmeurs et aux makers de construire tout ce qu'ils peuvent imaginer.

![Image](https://cdn-media-1.freecodecamp.org/images/M4xPtxNXeO6K2NCIA6WXpHLMQvGdG77xAd10)
_GrovePi (carte bleue) attaché à un Raspberry Pi_

Le GrovePi est une carte électronique que nous attachons au Raspberry Pi. Il facilite la connexion d'une large gamme de capteurs. Ainsi, vous n'avez pas besoin de vous soucier d'une plaque d'essai, de résistances, de soudure ou de fils de cavalier. Vous pouvez brancher un connecteur et commencer à travailler avec.

#### Flux de données

Dans l'illustration ci-dessous, vous voyez comment les données des capteurs circuleront des capteurs aux graphiques sur une page web. Nous utiliserons Python pour tout cela.

![Image](https://cdn-media-1.freecodecamp.org/images/fNyezC61-WH5nzRtVLodEZriNHkihVwLQz9c)
_Flux de données d'un GrovePi et d'un Raspberry Pi vers Firebase vers une page web hébergée sur PythonAnywhere._

La première étape consiste à récupérer les données des capteurs Grove. Ensuite, nous traitons les données sur le Raspberry Pi et les envoyons à une base de données Firebase. Ces données sont également utilisées pour allumer ou éteindre une unité de ventilation via un interrupteur télécommandé.

Nous pouvons obtenir les données stockées avec un script s'exécutant sur PythonAnywhere.com. Avec le package Dash, nous pouvons construire un tableau de bord pour suivre la qualité de l'air intérieur.

#### Capteurs de gaz

Nous utiliserons un ensemble de trois capteurs de gaz différents pour ce projet. J'utilise des capteurs de gaz Grove et les connecte au GrovePi.

Il n'est pas nécessaire d'utiliser les trois capteurs dans votre propre projet. Vous pouvez choisir les capteurs qui répondent à vos besoins. Vous pouvez le faire dans le fichier `config.py` en conservant les capteurs dont vous avez besoin dans le dictionnaire Python `MQ_SENSORS`.

![Image](https://cdn-media-1.freecodecamp.org/images/ZYw4C3gJXMR1SOZ5cdz81uJkdfQejUdxiy3y)
_Capteurs de gaz Grove_

Chaque capteur détecte un ensemble spécifique de gaz. Il y a un certain chevauchement entre les capteurs en ce qui concerne les gaz qu'ils détectent. Cependant, la plage dans laquelle les capteurs détectent un gaz peut différer. Vous pouvez trouver les plages sur le [site web de Seeedstudio](http://wiki.seeedstudio.com/How_to_Chose_A_Gas_Sensor/).

![Image](https://cdn-media-1.freecodecamp.org/images/aXpnoZufynmqRnxESFGV9LiKPJGQ0fm2OAmV)
_Gaz détectés par type de capteur_

#### Capteur de température et d'humidité

La température et l'humidité influencent les lectures des capteurs de gaz. Il est donc intéressant de mesurer également la température et l'humidité. Nous utilisons le capteur Grove BME680 pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/8PZoW1BkZtV2xNa3nHXAxT5-xfV1p2ltalSv)
_Grove BME680 pour mesurer la température et l'humidité_

### Travailler avec les données des capteurs

En bref, un capteur de gaz émettra une tension plus élevée lorsque la concentration d'un gaz est plus élevée. Cela est dû au fait que la résistance intégrée varie sa résistance (Rs) en fonction de la concentration du gaz.

La valeur du capteur ne reflète qu'une approximation d'une tendance dans la concentration de gaz. Cela signifie que vous pouvez l'utiliser pour montrer si la concentration de gaz augmente ou diminue. Elle ne donne pas la concentration exacte de gaz. Si vous souhaitez mesurer la concentration réelle, vous auriez besoin d'un capteur plus coûteux.

À des fins d'apprentissage, nous utiliserons la valeur du capteur pour approximer la concentration de gaz. Vous devez garder cela à l'esprit. **Vous ne devez pas utiliser ces scripts dans des situations réelles pour prévenir l'intoxication par ces gaz !**

Sur les fiches techniques listées ci-dessous, vous trouvez un graphique avec la relation entre la concentration de gaz et les valeurs de résistance du capteur. La concentration de gaz est exprimée en parties par million (ppm). Les valeurs de résistance comme le rapport Rs/R0.

* [Fiche technique MQ2](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/res/MQ-2.pdf)
* [Fiche technique MQ5](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ5/master/res/MQ-5.pdf)
* [Fiche technique MQ9](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/res/MQ-9.pdf)

Les courbes ci-dessous correspondent aux conditions standard de :

* une température de 20°C
* une humidité de 65%
* une concentration d'oxygène de 21%
* une résistance de charge de 5 kilo-ohms. La résistance de charge est la résistance totale d'un circuit électronique.

![Image](https://cdn-media-1.freecodecamp.org/images/ISA1CBYm5WM3hWuxAU5wsSXEhZ87aQv54Kr8)
_Courbes affichant la relation entre les concentrations de gaz et les valeurs de résistance du capteur. Les axes x et y sont sur une échelle logarithmique._

Nous pouvons supposer que la résistance de charge et la concentration d'oxygène sont stables dans le temps. Pourtant, la température et l'humidité à l'intérieur peuvent varier. Ces deux facteurs ont une influence sur les lectures du capteur, comme vous pouvez le voir dans le graphique ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/QgM73v0r-BeZXMFVFb9PW9rttlbEKOlbPnCh)
_Influence de différentes températures et humidités (RH) sur les valeurs de résistance du capteur dans le capteur MQ2 pour une concentration d'hydrogène (H2) de 1 000 ppm._

Pour obtenir des lectures précises, vous devriez avoir un graphique ou une table de consultation pour diverses combinaisons température-humidité. Malheureusement, ces graphiques ne sont pas fournis par le fabricant.

Une autre approche consiste à corriger les lectures du capteur pour l'influence de la température et de l'humidité.

Nous pouvons le faire avec des réseaux de neurones artificiels, comme proposé dans [l'article de Nenova & Dimchev](https://www.uni-obuda.hu/journal/Nenova_Dimchev_41.pdf). Cette approche nécessite des mesures de référence des concentrations de gaz. Cela dépasse le cadre de cet article.

#### Définition de la valeur R0

Tout d'abord, nous devons calculer la valeur R0. R0 représente la valeur de résistance du capteur pour 1 000 ppm d'hydrogène (H2) dans l'air pur. Le rapport pour l'air pur (ligne noire avec des croix bleues) est constant. Il reste à 9,8 indépendamment de la concentration d'air pur. Ainsi, nous pouvons calculer R0 en lisant la valeur du capteur (Rs) dans l'air pur et en la divisant par 9,8.

La valeur que nous obtenons du capteur est une valeur comprise entre 0 et 1,023 et n'a pas d'unité de mesure. Donc, pour obtenir la tension de sortie, nous divisons la valeur du capteur par 1,023. Nous multiplions cette valeur par la tension du circuit, qui est généralement de 5V.

À partir de la tension du capteur, nous pouvons dériver la résistance du capteur en appliquant la [loi d'Ohm](https://fr.wikipedia.org/wiki/Loi_d%27Ohm). La résistance du capteur est égale à

![Image](https://cdn-media-1.freecodecamp.org/images/HipHVSJozj6CkZ3TKlEHQlAJTdb5D-dsmsLZ)
_Vc est la tension du circuit et Vs est la tension du capteur_

Voyons comment nous faisons cela avec Python. Le code complet et plus de documentation peuvent être trouvés sur [Github](https://github.com/bertcarremans/air_quality_monitoring) dans le script `get_R0_values.py`.

```python
import config as cfg
import grovepi
import time
```

Tout d'abord, nous importons quelques packages. Le package `config` est un script Python que j'ai créé pour stocker tous les paramètres de configuration.

Tout au long du code, vous remarquerez que je fais parfois référence à `cfg.PARAMETER_NAME`. Nous définissons la valeur `PARAMETER_NAME` dans ce fichier `config.py`. Il contient également certains mots de passe et jetons API.

Pour des raisons de sécurité, je ne sauvegarderai pas ce fichier sur [Github](https://github.com/bertcarremans/air_quality_monitoring). Au lieu de cela, je fournirai un modèle propre `config_template.py` que vous pouvez utiliser pour votre propre projet.

Ensuite, nous importons le package `grovepi`. Vous pouvez l'installer à partir de la [page Github de Dexter Industries](https://github.com/DexterInd/GrovePi/tree/master/Software/Python) sur votre Raspberry Pi. Il nous permet de travailler avec le GrovePi et les capteurs connectés.

Enfin, nous utilisons le package `time` pour mettre en pause le programme pendant les lectures des capteurs.

```
mq_values = {}

for sensor, data in cfg.MQ_SENSORS.items():
    grovepi.pinMode(data['pin'],"INPUT")
    mq_values[sensor] = 0
```

Nous allons stocker les valeurs des capteurs pour les différents capteurs dans le dictionnaire `mq_values`. Mais d'abord, nous initialisons les valeurs à zéro dans une boucle sur les capteurs définis dans `MQ_SENSORS`.

Avec la méthode `pinMode`, vous pouvez définir la broche comme `INPUT` ou `OUTPUT`. Dans notre cas, nous l'utiliserons comme `INPUT`.

La `pin` nous indique à quelle broche du GrovePi le capteur est connecté. Nous utilisons les broches analogiques (ou ports) qui sont étiquetées A0, A1 et A2 sur le GrovePi. Assurez-vous de connecter le bon capteur au port décrit dans le fichier `config.py`.

```
for i in range(cfg.NB_R0_READ):
    for sensor, value in mq_values.items():
        mq_values[sensor] += grovepi.analogRead(cfg.MQ_SENSORS[sensor]['pin'])
    time.sleep(cfg.R0_INTERVAL)
```

Nous lisons ensuite la valeur du capteur dans une boucle pour `cfg.NB_R0_READ` fois et la cumulons dans `mq_value[sensor]`. Nous lisons la valeur du capteur avec la méthode `analogRead` du package `grovepi`.

Comme décrit dans la [documentation](https://www.dexterindustries.com/GrovePi/programming/python-library-documentation/), cela retournera une valeur entre 0 et 1,023. En fait, il convertit une valeur de capteur analogique en une valeur numérique.

Après une lecture pour tous les capteurs, nous mettons en pause le programme à `cfg.R0_INTERVAL` secondes. Pour obtenir la valeur moyenne, nous divisons la valeur cumulée par `cfg.NB_RO_READ`.

```
for sensor, value in mq_values.items():
    mq_values[sensor] = mq_values[sensor]/cfg.NB_R0_READ
    mq_values[sensor] = mq_values[sensor]/cfg.AR_MAX * cfg.VC
    mq_values[sensor] = (cfg.VC - mq_values[sensor])/mq_values[sensor]
    mq_values[sensor] = mq_values[sensor]/cfg.MQ_SENSORS[sensor]['r0_rs_air']
```

Nous calculons la tension du capteur en divisant la valeur moyenne du capteur par `cfg.AR_MAX`. Ensuite, nous la multiplions par la tension du circuit `cfg.VC`.

À partir de cette tension, nous pouvons appliquer la loi d'Ohm et calculer la valeur de résistance du capteur. En divisant cela par le rapport pour l'air pur `cfg.MQ_SENSORS[sensor]['r0_rs_air']`, nous obtenons R0.

Il est préférable de faire fonctionner le capteur pendant au moins 24 heures avant de mesurer la valeur R0. Cela donnera des lectures de capteur plus stables.

#### Interpolation linéaire de la concentration de gaz

Maintenant que nous connaissons la valeur R0, nous pouvons calculer le rapport Rs/R0 avec la valeur du capteur. Avec ce rapport, nous pouvons dériver la concentration de gaz avec [l'interpolation linéaire](https://fr.wikipedia.org/wiki/Interpolation_linéaire).

Pour cela, nous supposons que nous travaillons dans les conditions standard décrites pour le premier graphique. Dans ce cas, les courbes sont presque linéaires.

Pour l'interpolation linéaire, nous avons besoin de deux points connus de chaque courbe pour calculer sa pente. Supposons que nous avons deux points avec les coordonnées (x1, y1) et (x2, y2). Les valeurs y représentent les valeurs Rs/R0 et les valeurs x les concentrations de gaz. Pour une courbe linéaire, la pente est alors calculée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/JadXCd-aISp-O16p2TcXsGD8kMaCGptYIwIs)

Lorsque nous connaissons la pente, nous pouvons trouver la concentration de gaz (x) pour toute valeur Rs/R0 donnée (y). La formule pour cela est :

![Image](https://cdn-media-1.freecodecamp.org/images/nSsOuEVNkeRnpvWPOPNKm0z-iuK8Z4QTyNpK)

Les extraits de code ci-dessous proviennent du script `get_sensor_values.py` que vous pouvez trouver sur [Github](https://github.com/bertcarremans/air_quality_monitoring).

Nous mettons la formule dans une fonction `get_ppm`. `curve['y']` et `curve['x']` sont les points connus sur la courbe pour un gaz. `curve['slope']` est ce que nous avons calculé avec la formule précédente.

Vous pouvez trouver ces valeurs dans le fichier `config_template.py`. J'ai dérivé ces valeurs avec [Webplotdigitizer](https://automeris.io/WebPlotDigitizer/) à partir des graphiques sur les fiches techniques. Par conséquent, ces valeurs ne sont pas complètement précises. Utilisez-les avec prudence.

Notez l'utilisation de `np.log10` et `np.power`. La raison en est que les axes du graphique sont sur une échelle logarithmique.

```
def get_ppm(Rs_R0_ratio, curve):
    x_val = (np.log10(Rs_R0_ratio) - curve['y'])/curve['slope'] + curve['x']
    ppm_val = np.power(x_val, 10)
    return ppm_val
```

Nous calculons le `Rs_R0_ratio` de la même manière que lors du calcul de la valeur R0. Je ne vais donc pas le répéter. Pour calculer ce rapport, nous parcourons tous les gaz et capteurs et stockons cela dans `ppm_values[mq_sensor][gas]`.

```python
for gas, curve in cfg.CURVES[mq_sensor].items():
                ppm_values[mq_sensor][gas] = get_ppm(mq_values[mq_sensor], curve)
```

#### Température, humidité et pression

Outre les capteurs de gaz, nous lisons la température, l'humidité et la pression avec le capteur BME680. Le capteur BME680 est connecté au GrovePi via un port I2C. Pour utiliser le capteur, nous importons le package qui peut être installé à partir du [dépôt Pimoroni](https://github.com/pimoroni/bme680-python) sur Github.

```
import bme680
```

Les méthodes `set_..._oversample` spécifient combien d'échantillons nous prenons pour calculer la valeur moyenne. Nous l'avons également fait pour les gaz. Avec `get_sensor_data`, nous lisons les valeurs des capteurs.

```python
bme680_sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
bme680_sensor.set_humidity_oversample(bme680.OS_2X)
bme680_sensor.set_pressure_oversample(bme680.OS_4X)
bme680_sensor.set_temperature_oversample(bme680.OS_8X)
bme680_sensor.get_sensor_data()
```

```
bme680_sensor.get_sensor_data()
```

### Stockage et récupération des données des capteurs dans Cloud Firestore

Certains capteurs fournissent de nouvelles lectures très rapidement. D'autres capteurs (moins chers) prendront plus de temps. Pour ce projet, nous lirons les données chaque minute. Cela est défini dans le fichier de configuration avec `FIREBASE_INTERVAL = 60`.

Dans le plan Spark gratuit de Firebase, le [quota de Cloud Firestore](https://firebase.google.com/docs/firestore/quotas) permet 20K écritures par jour. Avec un intervalle d'une minute, nous serons bien en dessous de ce quota. La limite pour la lecture de documents dans le Firestore est de 50K par jour.

Vous devrez créer un projet Firebase et [créer un Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart). Après cela, assurez-vous de [générer les identifiants](https://firebase.google.com/docs/admin/setup) pour authentifier votre application. Enregistrez le fichier d'identifiants dans un endroit sécurisé.

Pour travailler avec Firebase via Python, nous devons importer le package `firebase_admin`. Ce package doit être installé sur votre Raspberry Pi au préalable, si nécessaire.

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
```

Après cela, nous pouvons initialiser l'application Firebase avec les identifiants. Je stocke l'emplacement du fichier d'identifiants dans `cfg.FIREBASE_CREDS_JSON`. Lorsque l'application est initialisée, nous créons un objet Firestore `db`.

```python
firebase_path = Path.cwd() / cfg.FIREBASE_CREDS_JSON
cred = credentials.Certificate(str(firebase_path))
firebase_admin.initialize_app(cred)
```

Après avoir traité les valeurs de gaz, il est temps de les stocker dans le Cloud Firestore. Nous allons créer un dictionnaire `firebase_values` pour rassembler toutes les données. Avec une compréhension de dictionnaire, nous ajoutons les valeurs pour tous les gaz pour tous les capteurs MQ. Les valeurs BME680 et le timestamp sont également ajoutés.

Avec la méthode `add` de l'objet Firestore `db`, il est facile de stocker les données dans le Firestore.

Le nom de la collection dans le Firestore est `cfg.FIREBASE_DB_NAME`. En savoir plus sur le [modèle de données de Firestore](https://firebase.google.com/docs/firestore/data-model) sur le site web de Firebase.

```python
firebase_values = {mq_sensor + '_' + gas + '_ppm': ppm
                            for mq_sensor, gases in ppm_values.items()
                            for gas, ppm in gases.items()
                          }
firebase_values['temperature'] = bme680_sensor.data.temperature
firebase_values['pressure'] = bme680_sensor.data.pressure
firebase_values['humidity'] = bme680_sensor.data.humidity
firebase_values['date'] = datetime.now()
db.collection(cfg.FIREBASE_DB_NAME).add(firebase_values)
```

Après avoir stocké les données, nous attendons une minute pour recommencer avec la ligne de code suivante.

```
time.sleep(cfg.FIREBASE_INTERVAL)
```

### Améliorer la qualité de l'air

Si la qualité de l'air à l'intérieur n'est pas bonne, nous devons prendre des mesures pour l'améliorer. Avant de pouvoir le faire, nous devons être informés des concentrations critiques de gaz.

Une possibilité est d'envoyer une notification d'alerte par e-mail, que nous aborderons ci-dessous.

Parfois, la source de la pollution de l'air intérieur provient de l'air extérieur. Par exemple, lorsque vos voisins ont des poêles à bois ou lorsque vous vivez près d'une usine.

Dans ce cas, vous pourriez installer votre station de mesure à l'extérieur et éteindre l'unité de ventilation dans votre maison si la qualité de l'air extérieur est mauvaise. Avec un interrupteur télécommandé, cela peut être fait facilement.

Tout le code pour cette section se trouve dans `improve_air_quality.py` sur Github.

#### Envoyer des notifications lorsque la qualité de l'air atteint un niveau critique

Nous ne voulons pas envoyer un e-mail chaque fois que le capteur émet des valeurs critiques (ici, chaque minute).

Disons que nous voulons vérifier chaque heure s'il y avait des valeurs critiques dans la dernière heure. Pour cela, nous devons suivre un `reference_time`. Nous l'initialisons lorsque le programme de lecture des valeurs des capteurs commence. L'intervalle auquel nous vérifions à nouveau les concentrations critiques de gaz est défini dans `cfg.ALERT_INTERVAL`.

```
reference_time = datetime.now()
```

Lorsque qu'une heure s'est écoulée depuis `reference_time`, nous pouvons commencer à vérifier s'il y avait des valeurs critiques de polluants atmosphériques. Nous mettons à jour `reference_time` avec l'heure actuelle.

Avec le package `pytz`, nous pouvons prendre en compte notre fuseau horaire. Dans mon cas, c'est `Europe/Brussels`. Nous calculons `one_hour_ago` en soustrayant 60 minutes de l'heure actuelle.

```
if datetime.now() > reference_time + timedelta(minutes=cfg.ALERT_INTERVAL):
    reference_time = datetime.now()
    brussels_tz = pytz.timezone('Europe/Brussels')
    prev_check_time = brussels_tz.localize(datetime.now()) - timedelta(minutes=cfg.ALERT_INTERVAL)
```

Avec `prev_check_time`, nous extrayons les lectures des capteurs de Firebase de la dernière heure. Nous faisons cela en appliquant une clause `where` aux données que nous `get` de Cloud Firestore.

Dans ce script, nous n'utiliserons qu'un seul capteur de gaz et un ensemble limité de gaz. Le capteur est sélectionné dans `cfg.ALERT_SENSOR`. Les gaz sont sélectionnés dans `cfg.ALERT_GASES`. Les données par gaz sont ajoutées à `ppm_vals` ainsi que les `timestamps`.

```
timestamps = []
ppm_vals = {}
for gas in cfg.ALERT_GASES:
    ppm_vals[gas] = []
            
docs = db.collection(cfg.FIREBASE_DB_NAME).order_by(u'date').where(u'date', '>=', one_hour_ago).get()
            
for doc in docs:
    data = doc.to_dict()
    for gas in cfg.ALERT_GASES:
        ppm_vals[gas].append(data[cfg.ALERT_SENSOR + gas + '_ppm'])

    timestamps.append(data['date'].strftime('%H:%M:%S'))
```

Nous recherchons des valeurs critiques avec la fonction `find_crit_val`. Nous ne vérifierons que si la valeur a dépassé une limite supérieure `ubound`. Ces limites supérieures doivent être spécifiées dans le fichier de configuration.

Les données sont dans l'ordre chronologique ascendant. Ainsi, nous pouvons utiliser la méthode `next` pour trouver le premier timestamp pour lequel `v > ubound`. Nous retournons un tuple contenant le timestamp de la valeur critique et la valeur critique elle-même.

S'il n'y a pas de valeur critique, nous retournons le tuple `(None, None)`.

```
def find_crit_val(timestamps, val_list, ubound):
    try:
        (crit_time, crit_value) = next(((i,v) for i, v in zip(timestamps, val_list) if v > ubound))          
    except:
        (crit_time, crit_value) = (None,None)
    return (crit_time, crit_value)
```

Les tuples critiques sont stockés dans un dictionnaire `crit_dict`. En tant que clé, nous utilisons le nom du gaz. Nous vérifions ensuite les combinaisons gaz-capteur avec un timestamp critique et une valeur critique. Dans ce cas, nous ajoutons un message d'alerte à `critical_msg`.

```
crit_dict = {}
for gas in cfg.ALERT_GASES:
    (crit_time, crit_value) = find_crit_val(timestamps, ppm_vals[gas], cfg.UPPERBOUNDS[gas])
    crit_dict[gas] = (crit_time, crit_value)
critical_msg = ''
    for k, v in crit_dict.items():
        if v[0] is not None and v[1] is not None:
            critical_msg += '\nCritical value for ' + k + ' of ' + str(v[1]) + cfg.UNITS[k] + ' at ' + str(v[0])
```

Si `critical_msg` n'est pas vide, nous envoyons un e-mail. L'envoi d'un e-mail se fait avec le package `smtplib`. Comment envoyer un e-mail avec Python est expliqué sur [AutomateThe BoringStuff.com](https://automatetheboringstuff.com/chapter16/).

Vous devez générer un [mot de passe spécifique à l'application](https://support.google.com/mail/?p=InvalidSecondFactor) pour votre e-mail si vous utilisez l'authentification à deux facteurs de Google.

```
if critical_msg != '':
    try:
        msg = MIMEText(critical_msg, _charset='utf-8')
        msg['Subject'] = Header('Air Quality Alert', 'utf-8')
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(cfg.EMAIL, cfg.EMAIL_PW)
        smtpObj.sendmail(cfg.EMAIL, cfg.EMAIL, msg.as_string())
        smtpObj.quit()  
    except smtplib.SMTPException:
        print('Something went wrong while sending the email')
```

#### Contrôler automatiquement votre unité de ventilation

Avec un interrupteur télécommandé, nous pouvons allumer ou éteindre n'importe quel appareil qui y est connecté. Ainsi, également une unité de ventilation. [Energenie](https://energenie.com/) crée l'add-on PiMote spécifiquement pour le Raspberry Pi. Pour contrôler l'interrupteur Energenie, vous devez installer le package `energenie` et l'importer.

Notez que vous ne pouvez pas attacher le PiMote sur le GrovePi. Vous aurez donc besoin d'un second Raspberry Pi.

Lorsque vous démarrez le script, la première chose que nous faisons est de définir une variable booléenne `ventilation_on`. Nous la définissons à `False` car c'est la première fois que nous exécutons le script.

```
import energenie
ventilation_on = False
```

Si `critical_msg` n'est pas vide, il y avait une concentration critique de gaz dans le dernier intervalle d'alerte. Dans ce cas, nous allumons la ventilation avec la méthode `switch_on` du package energenie.

S'il n'y avait pas de concentration critique de gaz et que la ventilation était allumée dans le dernier intervalle d'alerte, nous pouvons l'éteindre.

Vous devrez peut-être définir un autre intervalle avant d'éteindre votre ventilation. Cela dépend du débit de votre unité de ventilation, des gaz mesurés et du fait que la source de pollution ait été désactivée.

```
if critical_msg != '':
    if not ventilation_on:
        energenie.switch_on(1)
        ventilation_on = True
else:
    if ventilation_on:
        energenie.switch_off(1)
        ventilation_on = False
```

### Visualisation de la qualité de l'air avec Dash

Une notification avec des concentrations critiques de gaz peut aider à prendre des mesures immédiates. Mais il est également intéressant de suivre les concentrations de gaz au fil du temps. En visualisant les valeurs des capteurs dans un tableau de bord, nous pouvons observer la tendance des concentrations de gaz. Cela peut être fait avec Dash. Sur le site web de Dash, vous pouvez trouver un [excellent tutoriel](https://dash.plot.ly/) pour commencer.

Dans ce projet, nous allons construire un tableau de bord et l'héberger sur [PythonAnyWhere.com](https://www.pythonanywhere.com/). Pour utiliser Dash sur PythonAnywhere, vous devez créer un [environnement virtuel](https://help.pythonanywhere.com/pages/Virtualenvs/). Vous pouvez suivre les étapes de [cette démonstration](https://github.com/conradho/dashingdemo) sur la façon de configurer une application Dash sur PythonAnyWhere.

Ci-dessous, je vais montrer comment j'ai construit le tableau de bord pour notre station de qualité de l'air. Le script complet peut être trouvé dans plot_sensor_values.py sur [Github](https://github.com/bertcarremans/air_quality_monitoring).

Tout d'abord, vous devez importer le package `dash`.

```
import dash
import dash_core_components as dcc
import dash_html_components as html
```

Dans la démonstration sur le site web de Dash, ils utilisent un lien vers une feuille de style en cascade (CSS) pour fournir un design de page agréable. Si vous souhaitez [utiliser un CSS local](https://dash.plot.ly/external-resources) sur votre ordinateur portable ou serveur web, vous pouvez ajouter un dossier d'actifs. Dans ce dossier, vous pouvez ajouter votre CSS et Dash le récupérera à partir de là.

Ensuite, vous devrez obtenir les données de Firebase. Cela peut être fait de manière similaire à ce que nous avons fait pour envoyer les notifications d'alerte. Nous ne passerons donc pas par cela à nouveau.

Avec les données collectées de Firebase, nous pouvons remplir les graphiques de notre tableau de bord. Nous créons d'abord un objet Dash `app` et lui donnons un `title`.

```
app = dash.Dash(__name__)
app.title = 'Tableau de bord de la qualité de l'air intérieur'
```

Ensuite, nous créons la `layout` du tableau de bord. Un composant d'en-tête `H1`, un `container` div et un div contenant les `graphs`.

```
app.layout = html.Div([
    html.H1(style={'textAlign':'center'}, children='Tableau de bord de la qualité de l'air intérieur'),
    html.Div(id='container'),
    html.Div(graphs)
])
```

`graphs` est une liste qui contient les informations par graphique. Ci-dessous, vous pouvez voir comment le graphique pour la température est configuré. Vous pouvez ajouter le `dcc.Graph` pour l'humidité et la pression également en les ajoutant à `graphs`.

```
graphs = [
    dcc.Graph(
        id='temperature',
        figure={
            'data':[{
                'x':timestamps,
                'y':temperatures,
                'type':'line',
                'name': 'Température',
                'line': {'width':2, 'color': '#542788'}
                }],
            'layout':{
                'title': 'Température',
                'yaxis': {'title': 'Celsius'},
                'xaxis': {'title': 'Timestamp', 'tickvals':timestamps}
            }
        }
    )
]
```

Les graphiques pour les capteurs MQ peuvent être ajoutés dans une boucle for.

```
for mq_sensor in cfg.MQ_SENSORS.keys():
    for gas in cfg.CURVES[mq_sensor].keys():
        sensor_gas_key = mq_sensor + '_' + gas + '_ppm'
        title = gas + ' concentration sur '+ mq_sensor + ' capteur'
        data = ppm_values[mq_sensor][gas]
        data.reverse()

        graphs.append(dcc.Graph(
            id=sensor_gas_key,
            figure={
                'data': [{
                    'x': timestamps,
                    'y': data,
                    'type':'line',
                    'name': title,
                    'line': {'width':2}
                }],
                'layout': {
                    'title': title,
                    'yaxis': {'title': 'ppm'},
                    'xaxis': {'title': 'Timestamp', 'tickvals':timestamps}
                }
            }
        ))
```

En résultat, vous aurez un tableau de bord avec des graphiques comme celui ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/XhmuZyEJBLsJ1eUuTWb80qkmI99ptztNyiF7)
_Graphique avec les données du capteur MQ2 pour le méthane (ch4)_

### Conclusion

Avec quelques capteurs de gaz peu coûteux et un Raspberry Pi (et GrovePi), il est facile de construire une station de mesure de la qualité de l'air. Vous pouvez ensuite agir sur les données en envoyant des notifications d'alerte lorsque la qualité de l'air est mauvaise ou en allumant la ventilation. Avec Dash, vous pouvez créer de belles visualisations pour surveiller la qualité de l'air au fil du temps.

Ci-dessous, j'ai noté quelques idées pour aller plus loin avec ce projet.

* créer une application mobile pour les visualisations et la réception des notifications
* ajouter des LEDs, un buzzer et un écran OLED au Raspberry Pi pour obtenir un retour instantané sur la qualité de l'air
* installer des stations de mesure chez vos amis et votre famille et [les visualiser sur une carte interactive](https://towardsdatascience.com/visualizing-air-pollution-with-folium-maps-4ce1a1880677).
* une fois que vous avez assez de données, [construire un modèle de série temporelle](https://towardsdatascience.com/forecasting-air-pollution-with-recurrent-neural-networks-ffb095763a5c) pour prédire la qualité de l'air intérieur

Espérons que cette histoire vous motive à commencer à construire votre propre station de mesure. Si vous avez des questions ou des suggestions, faites-le moi savoir.