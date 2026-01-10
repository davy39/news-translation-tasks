---
title: Comment utiliser Node, un Raspberry Pi et un écran LCD pour surveiller la météo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T18:34:14.000Z'
originalURL: https://freecodecamp.org/news/monitor-the-weather-with-node-and-raspberry-pi
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vinicius-amnx-amano-ALpEkP29Eys-unsplash.jpg
tags:
- name: hardware
  slug: hardware
- name: projects
  slug: projects
- name: Raspberry Pi
  slug: raspberry-pi
- name: smart home
  slug: smart-home
seo_title: Comment utiliser Node, un Raspberry Pi et un écran LCD pour surveiller
  la météo
seo_desc: "By Stan Georgian\nOver the last few years, smart home devices have gone\
  \ from less than 300,000 back in 2015 up to almost 1.2 billion in 2020. And they’re\
  \ expected to grow to 1.5 billion by 2021. \nSo it's likely you have at least some\
  \ smart devices in ..."
---

Par Stan Georgian

Au cours des dernières années, les appareils domestiques intelligents sont passés de moins de 300 000 en 2015 à près de 1,2 milliard en 2020. Et ils devraient atteindre [1,5 milliard d'ici 2021](https://www.omdia.com/resources/product-content/how-the-smart-home-will-develop-by-2021). 

Il est donc probable que vous ayez au moins quelques appareils intelligents chez vous, étant donné que la moyenne atteindra 8,7 appareils intelligents par foyer d'ici 2021.

En tant que développeurs, nous avons un certain avantage dans ce domaine, puisque nous pouvons construire nos propres appareils domestiques intelligents.

Ce ne sont pas seulement les appareils qui ont connu un développement rapide. Les cartes de développement utilisées pour eux ont commencé à devenir de plus en plus commerciales et accessibles. 

Dans cet article, nous verrons comment utiliser un Raspberry Pi, un écran LCD et quelques lignes de code pour surveiller la météo à l'extérieur ou pour un lieu spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/ezgif-6-8af115ff0d25.gif)

Étant donné que ce projet est à faire soi-même (DIY), il y a quelques prérequis dont nous avons besoin pour cet appareil.

## Prérequis

* Raspberry Pi 3 (ou supérieur)
* Écran LCD
* Fils de connexion
* Potentiomètre (Optionnel)
* Plaque d'essai (Optionnel)

# Comment le construire

Dès que nous avons tout ce dont nous avons besoin, nous pouvons commencer. Prenons cela étape par étape.

## Étape I - Configuration de base

La première étape consiste en la configuration de base et une vérification de tous les composants.

Pour cette démonstration, nous utiliserons l'API météo ClimaCell comme fournisseur de données météo, car ils disposent d'un grand nombre d'indicateurs, y compris des indicateurs de qualité de l'air, que nous pouvons utiliser.

Pour utiliser leur API, nous devons ouvrir un compte sur leur plateforme et obtenir une clé API, que nous utiliserons pour signer nos requêtes.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/bQHbP2FU.png)
_Limite de l'API ClimaCell_

Le compte est gratuit à ouvrir et il vient avec une limite de 100 heures d'appels API, ce qui est plus que suffisant pour notre projet.

Dès que nous avons cette clé API, nous pouvons passer à la configuration matérielle et connecter l'écran LCD à notre Raspberry Pi. Vous devriez éteindre le Raspberry Pi pendant que vous faites la connexion des fils.

La disposition des broches pour le Raspberry Pi 3 peut être vue dans l'image suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/emiVLiHU.png)
_Broches du Raspberry Pi 3_

La connexion des fils entre le LCD et la carte de développement est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/WWjB6lbg.png)
_Connexion entre le Raspberry PI et le LCD_

Cette connexion matérielle fera que l'écran LCD sera à pleine luminosité et à plein contraste. Le niveau de luminosité n'est pas un problème, mais le contraste l'est car nous ne pourrons pas voir les caractères à l'écran. 

C'est pourquoi nous devons introduire au moins un potentiomètre avec lequel régler le niveau de contraste.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/DFu8N63z.png)
_Schéma_

À ce stade, nous pouvons allumer notre Raspberry Pi et nous devrions voir l'écran LCD s'allumer. Avec l'aide de la résistance variable, nous devrions être capables de contrôler le contraste.

## Étape II - Configuration du projet

En tant que langage de programmation, nous utiliserons [NodeJS](https://nodejs.org/en/) pour écrire le code. Si vous n'avez pas encore NodeJS installé sur votre Raspberry, vous pouvez suivre ces [instructions simples](https://www.instructables.com/id/Install-Nodejs-and-Npm-on-Raspberry-Pi/).

Dans un nouveau dossier, exécutez la commande `npm init -y` pour configurer un nouveau package npm, suivie de la commande `npm install lcd node-fetch` pour installer ces 2 dépendances nécessaires.  


* `lcd` sera utilisé pour communiquer avec l'écran LCD
* `node-fetch` sera utilisé pour faire des requêtes [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) à l'API ClimaCell.

Nous avons dit que nous avions besoin d'une clé API pour communiquer avec le fournisseur de données météo. Vous pouvez placer votre clé API secrète directement dans le code principal, ou vous pouvez créer un fichier `config.json` dans lequel vous pouvez placer cette clé et toute autre configuration liée au code que vous pourriez avoir.

`config.json`

```javascript
{  "cc_key": "<votre_clé_API_ClimaCell>"}
```

Enfin, créons le fichier principal de notre projet et incluons toutes ces choses dont nous avons parlé.

```javascript
// * Dépendances
const Lcd = require("lcd");
const fs = require("fs");
const fetch = require("node-fetch");

// * Variables globales
const { cc_key } = JSON.parse(fs.readFileSync("./config.json"));

```

## Étape III - L'écran LCD

Écrire sur l'écran est un jeu d'enfant en utilisant le module lcd. Cette bibliothèque agit comme une couche d'abstraction sur la manière dont nous communiquons avec l'appareil. De cette façon, nous n'avons pas besoin de micro-gérer chaque commande individuellement.

Le code complet pour notre écran LCD est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/MidH14Tk.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=const%2520lcd%2520%253D%2520new%2520Lcd(%257B%2520rs%253A%252026%252C%2520e%253A%252019%252C%2520data%253A%2520%255B13%252C%25206%252C%25205%252C%252011%255D%252C%2520cols%253A%252016%252C%2520rows%253A%25202%2520%257D)%253B%250A%250A%250Afunction%2520writeToLcd(col%252C%2520row%252C%2520data)%2520%257B%250A%2520%2520return%2520new%2520Promise((resolve%252C%2520reject)%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520lcd.setCursor(col%252C%2520row)%253B%250A%2520%2520%2520%2520lcd.print(data%252C%2520(err)%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520%2520%2520if%2520(err)%2520%257B%250A%2520%2520%2520%2520%2520%2520%2520%2520reject()%253B%250A%2520%2520%2520%2520%2520%2520%257D%250A%2520%2520%2520%2520%2520%2520resolve()%253B%250A%2520%2520%2520%2520%257D)%253B%250A%2520%2520%257D)%253B%250A%257D)_

La première étape consistait à créer un nouvel objet `lcd` et à passer en argument les broches que nous avons utilisées.

Les clés `cols` et `rows` représentent le nombre de colonnes et de lignes de notre affichage LCD. 16x2 est celui que j'ai utilisé dans cet exemple. Si votre LCD n'a que 8 colonnes et 1 ligne, remplacez 16 et 2 par vos valeurs.

Pour écrire quelque chose sur l'affichage, nous devons utiliser ces deux méthodes successivement :

* lcd.setCursor() - sélectionner la position à partir de laquelle commencer à écrire
* lcd.print()

En même temps, nous avons enveloppé ces deux fonctions dans une promesse pour utiliser les mots-clés `async/await`.

À ce stade, vous pouvez utiliser cette fonction et imprimer quelque chose sur votre affichage. `writeToLcd(0,0,'Hello World')` devrait imprimer le message `Hello World` sur la première ligne en commençant par la première colonne.

## Étape IV - Les données météo

L'étape suivante consiste à obtenir les données météo et à les imprimer sur l'affichage.

ClimaCell fournit beaucoup d'informations sur les données météo, mais aussi sur la qualité de l'air, le pollen, les incendies et autres. Les données sont vastes, mais gardez à l'esprit que votre écran LCD n'a que 16 colonnes et 2 lignes, soit seulement 32 caractères.

Si vous souhaitez afficher plus de types de données et que cette limite est trop petite pour vous, vous pouvez utiliser un effet de défilement.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/81w9nkUg.gif)

Pour cette démonstration, nous allons garder cela simple et nous allons imprimer sur l'écran LCD les données suivantes :

* date actuelle (heure, minutes, secondes)
* température
* intensité des précipitations

![Image](https://www.freecodecamp.org/news/content/images/2020/06/zj8FQisB.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=async%2520function%2520getWeatherData(apiKey%252C%2520lat%252C%2520lon)%2520%257B%250A%2520%2520const%2520url%2520%253D%2520%2560https%253A%252F%252Fapi.climacell.co%252Fv3%252Fweather%252Frealtime%253Flat%253D%2524%257Blat%257D%2526lon%253D%2524%257Blon%257D%2526unit_system%253Dsi%2526fields%253Dtemp%2526fields%253Dprecipitation%2526apikey%253D%2524%257BapiKey%257D%2560%253B%250A%250A%2520%2520const%2520res%2520%253D%2520await%2520fetch(url)%253B%250A%2520%2520const%2520data%2520%253D%2520await%2520res.json()%253B%250A%2520%2520return%2520data%253B%250A%257D%250A%250Aasync%2520function%2520printWeatherData()%2520%257B%250A%2520%2520const%2520%257B%2520temp%252C%2520precipitation%2520%257D%2520%253D%2520await%2520getWeatherData(cc_key%252C%252045.658%252C%252025.6012)%253B%250A%250A%2520%2520%252F%252F%2520*%2520première%2520ligne%250A%2520%2520await%2520writeToLcd(0%252C%25200%252C%2520Math.round(temp.value)%2520%252B%2520temp.units)%253B%250A%250A%2520%2520%252F%252F%2520*%2520deuxième%2520ligne%250A%2520%2520const%2520precipitationMessage%2520%253D%250A%2520%2520%2520%2520%2522Précip.%253A%2520%2522%2520%252B%2520precipitation.value%2520%252B%2520precipitation.units%253B%250A%2520%2520await%2520writeToLcd(0%252C%25201%252C%2520precipitationMessage)%253B%250A%257D)_

Pour obtenir des données de ClimaCell pour un lieu spécifique, vous devez envoyer ses coordonnées géographiques, latitude et longitude.

Pour trouver les coordonnées de votre ville, vous pouvez utiliser un outil gratuit comme [latlong.net](https://www.latlong.net/place/new-york-city-ny-usa-1848.html), puis vous pouvez les enregistrer dans le fichier `config.json` avec votre clé API, ou vous pouvez les écrire directement dans le code.

À ce stade, le format des données retourné par l'appel API est le suivant :

```javascript
{
  lat: 45.658,
  lon: 25.6012,
  temp: { value: 17.56, units: 'C' },
  precipitation: { value: 0.3478, units: 'mm/hr' },
  observation_time: { value: '2020-06-22T16:30:22.941Z' }
}
```

Nous pouvons déconstruire cet objet et obtenir les valeurs de température et de précipitations, puis les imprimer sur la première et la deuxième ligne.

## Étape V - Finalisation

Tout ce que nous devons faire maintenant est d'écrire la logique de notre script et de mettre à jour l'écran LCD lorsque de nouvelles données arrivent.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/oeM4lSfQ.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=async%2520function%2520main()%2520%257B%250A%2520%2520await%2520printWeatherData()%253B%250A%250A%2520%2520setInterval(()%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520printWeatherData()%253B%250A%2520%2520%257D%252C%25205%2520*%252060%2520*%25201000)%253B%250A%250A%2520%2520setInterval(async%2520()%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520await%2520writeToLcd(8%252C%25200%252C%2520new%2520Date().toISOString().substring(11%252C%252019))%253B%250A%2520%2520%257D%252C%25201000)%253B%250A%257D%250A%250Alcd.on(%2522ready%2522%252C%2520main)%253B%250A%250A%252F%252F%2520*%2520Si%2520ctrl%252Bc%2520est%2520appuyé%252C%2520libérer%2520les%2520ressources%2520et%2520quitter.%250Aprocess.on(%2522SIGINT%2522%252C%2520(_)%2520%253D%253E%2520%257B%250A%2520%2520lcd.close()%253B%250A%2520%2520process.exit()%253B%250A%257D)%253B)_

Les données météo sont mises à jour toutes les 5 minutes. Mais comme nous avons une limite de 100 appels API/heure imposée par ClimaCell, nous pouvons aller encore plus loin et mettre à jour les données météo chaque minute.

Pour la date actuelle, nous avons deux options : 

* nous pouvons utiliser la propriété `observation_time` et afficher la date à laquelle les données ont été reçues, ou 
* nous pouvons faire une horloge réelle et afficher l'heure actuelle.

J'ai choisi la deuxième option, mais faites comme vous le souhaitez.

Pour imprimer l'heure dans le coin supérieur droit, nous devons d'abord calculer la colonne de départ pour que le texte s'ajuste parfaitement. Pour cela, nous pouvons utiliser la formule suivante : `nombre total de colonnes` moins `longueur du texte à afficher`

La date a 8 caractères et comme il y a 16 colonnes, nous devons commencer à partir de la colonne numéro 8.

La configuration de l'écran LCD est asynchrone, donc nous devons utiliser la méthode `lcd.on()` fournie par la bibliothèque associée, pour savoir quand le LCD a été initialisé et est prêt à être utilisé.

Une autre bonne pratique dans les systèmes embarqués est de fermer et de libérer les ressources que vous utilisez. C'est pourquoi nous utilisons l'événement `SIGNINT` pour fermer l'écran LCD lorsque le programme est arrêté. D'autres événements comme celui-ci incluent :  


* `SIGUSR1` et `SIGUSR2` - pour attraper les "kill pid" comme le redémarrage de nodemon
* `uncaughtException` - pour attraper les exceptions non capturées

## Étape VI - Exécuter en continu

Le script est complet et à ce stade, nous pouvons exécuter notre programme. Nous avons juste une dernière chose à faire avant de pouvoir terminer. 

À ce stade, vous êtes probablement connecté à votre Raspberry Pi en utilisant SSH ou directement avec un câble HDMI et un moniteur. Peu importe, lorsque vous fermez votre terminal, le programme s'arrêtera. 

En même temps, si vous éteignez votre appareil et que vous le rallumez après un certain temps ou immédiatement, le script ne démarrera pas et vous devrez le faire manuellement.

Pour résoudre ce problème, nous pouvons utiliser un gestionnaire de processus comme [pm2](https://www.npmjs.com/package/pm2).

Voici les étapes :  


1. `sudo npm install pm2 -g` - installer pm2
2. `sudo pm2 startup` - créer un script de démarrage pour le gestionnaire pm2
3. `pm2 start index.js` - démarrer une application
4. `pm2 save` - sauvegarder votre liste de processus après le redémarrage du serveur

Maintenant, vous pouvez redémarrer votre carte et le script démarrera automatiquement lorsque l'appareil sera prêt.

# Conclusion

À partir de ce point, vous pouvez personnaliser votre nouvel appareil comme vous le souhaitez. Si vous trouvez ces données météo importantes pour vous (ou toute autre donnée de ClimaCell, comme la pollution de l'air, le pollen, l'indice de feu ou le risque routier), vous pouvez créer un boîtier personnalisé pour y mettre le Raspberry Pi et l'écran LCD. Ensuite, après avoir ajouté une batterie, vous pouvez placer l'appareil dans votre maison.

Le [Raspberry Pi](https://www.raspberrypi.org/) est comme un ordinateur personnel, donc vous pouvez faire beaucoup plus avec lui que ce que vous feriez normalement sur un microcontrôleur comme [Arduino](https://www.arduino.cc/). Grâce à cela, il est facile de le combiner avec d'autres appareils que vous avez dans votre maison.