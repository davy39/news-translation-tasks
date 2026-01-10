---
title: Comment mesurer la température et l'envoyer à AWS IoT en utilisant un Raspberry
  Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T15:51:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-measure-temperature-and-send-it-to-aws-iot-using-a-raspberry-pi-d6f7b196ec35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*luZBAP5jAeQXIoKDlm2Lqg.jpeg
tags:
- name: AWS
  slug: aws
- name: Internet of Things
  slug: internet-of-things
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Comment mesurer la température et l'envoyer à AWS IoT en utilisant un Raspberry
  Pi
seo_desc: 'By Leo Kyrpychenko

  What if you want to self-correct the temperature in your office? Or what if you
  are curious to understand your office environment using IoT sensors?

  If this sounds interesting to you, please read on.

  To begin with, we need to set u...'
---

Par Leo Kyrpychenko

Et si vous vouliez auto-corriger la température dans votre bureau ? Ou si vous étiez curieux de comprendre votre environnement de bureau en utilisant des capteurs IoT ?

Si cela vous intéresse, veuillez continuer à lire.

Pour commencer, nous devons configurer un capteur de lecture de température. Nous le connectons à un Arduino qui se connecte à un Raspberry Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*luZBAP5jAeQXIoKDlm2Lqg.jpeg)

L'étape suivante consiste à configurer le SDK AWS IoT sur votre Raspberry Pi.

#### Installation de la Chose

1. Créez une chose dans AWS IoT :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HMoK-8MpdziO3p1KgUu1WQ.png)

2. Créez une seule chose pour commencer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zkpo9cALdjh6y_91NkYlgQ.png)

3. Créez une chose d'un type particulier. Nous utilisons Raspberry Pi ici (les types sont créés par vous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*wpws9o3IaQd1QrhZerkgxw.png)

4. Créez un certificat pour votre Chose afin qu'elle communique avec AWS :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kvhutJBA_nZMl4tCRYlPhw.png)

5. Téléchargez les certificats, une autorité de certification racine (CA), activez la Chose et attachez la politique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IlIegdjeWhnlsCPsk2CR9A.png)

6. Le code de la politique est ici. Il peut sembler un peu permissif, mais c'est acceptable pour l'application de démonstration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mY-mP_JRKku7qBxk-PkTVg.png)

#### Configuration de votre Raspberry Pi

Avant de commencer la configuration, veuillez copier tous les certificats et tous les fichiers de l'autorité de certification racine sur le Raspberry Pi (scp peut vous aider). Vous devez également installer Node.js si ce n'est pas déjà fait.

Vous devrez également installer le SDK AWS IoT pour les appareils.

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nodejs

openssl x509 -in ./CA-roots/VeriSign-Class\ 3-Public-Primary-Certification-Authority-G5.pem -inform PEM -out root-CA.crt
chmod 775 root-CA.crt

npm install aws-iot-device-sdk
```

Voici le code qui lit les données du port série et envoie les relevés de température en utilisant le SDK AWS IoT pour les appareils. Le code est basé sur les exemples d'Amazon.

```js
'use strict';

console.log('Exécution...');

const SerialPort = require('serialport');
const Readline = require('@serialport/parser-readline')

const portName = '/dev/ttyACM0';
const port = new SerialPort(portName, (err) => {
	if (err) {
		return console.log('Erreur : ', err.message);
	}
});

const deviceModule = require('aws-iot-device-sdk').device;

const parser = port.pipe(new Readline({ delimiter: '\r\n' }));
const rePattern = new RegExp(/C: (.+)F:(.+)/);

parser.on('data', (data) => {
	const arrMatches = data.match(rePattern);

	if(arrMatches && arrMatches.length >= 1) {
		const readingInC = arrMatches[1].trim();
		console.log(readingInC);

		sendDataToTheNube(readingInC);
	}
});

const defaults = {
	protocol: 'mqtts',
	privateKey: './iot/f5b0580f5c-private.pem.key',
	clientCert: './iot/f5b0580f5c-certificate.pem.crt',
	caCert: './iot/root-CA.crt',
	testMode: 1,
	/* millisecondes */
	baseReconnectTimeMs: 4000,
	/* secondes */
	keepAlive: 300,
	/* millisecondes */
	delay: 4000,
	thingName: 'cuttlefish-hub-01',
	clientId: 'nouser' + (Math.floor((Math.random() * 100000) + 1)),
	Debug: false,
	Host: 'a7773lj8lvoid9a.iot.ap-southeast-2.amazonaws.com',
	region: 'ap-southeast-2'
};

function sendDataToTheNube(readingInC) {
	const device = deviceModule({
	      keyPath: defaults.privateKey,
	      certPath: defaults.clientCert,
	      caPath: defaults.caCert,
	      clientId: defaults.clientId,
	      region: defaults.region,
	      baseReconnectTimeMs: defaults.baseReconnectTimeMs,
	      keepalive: defaults.keepAlive,
	      protocol: defaults.Protocol,
	      port: defaults.Port,
	      host: defaults.Host,
	      debug: defaults.Debug
	});

	device.publish(`temperature/${defaults.thingName}`, JSON.stringify({
		temperature: readingInC
	}));
}
```

Alors, que pouvez-vous faire avec ces données ?

Vous pouvez écrire une fonction Lambda qui met les données en file d'attente pour le traitement. Cela peut ressembler à ceci :

```js
require("source-map-support").install();

import { Callback, Handler } from "aws-lambda";
import { baseHandler } from "../shared/lambda";
import logger from "../shared/logger";
import {Models} from "../shared/models";
import {QueueWriter} from "./queue-writer";

const handler: Handler = baseHandler((event: any, callback: Callback) => {
    logger.json("Event:", event);

    const writer = new QueueWriter();

    const { temperature, sensorId } = event;

    const reading: Models.Readings.TemperatureReading = {
        temperature,
        sensorId,
    };

    writer.enqueue(reading)
        .then(() => callback())
        .catch(callback);
});

export { handler };
```

Et votre fichier serverless.com peut ressembler à ceci :

```yaml
functions:
    sensorReadings:
        name: ${self:provider.stage}-${self:service}-sensor-readings
        handler: sensor-readings/index.handler
        description: Déclenché par AWS IoT
        timeout: 180
        environment:
            READING_QUEUE_NAME: ${self:provider.stage}_${self:custom.productName}_reading
            READING_DL_QUEUE_NAME: ${self:provider.stage}_${self:custom.productName}_reading_dl
        tags:
            service: ${self:service}
        events:
             - iot:
                sql: "SELECT * FROM '#'"
```

J'espère que cet article vous a fait gagner du temps pour configurer votre appareil. Merci d'avoir lu !