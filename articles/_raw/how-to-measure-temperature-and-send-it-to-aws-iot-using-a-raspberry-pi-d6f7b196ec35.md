---
title: How to measure temperature and send it to AWS IoT using a Raspberry Pi
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
seo_title: null
seo_desc: 'By Leo Kyrpychenko

  What if you want to self-correct the temperature in your office? Or what if you
  are curious to understand your office environment using IoT sensors?

  If this sounds interesting to you, please read on.

  To begin with, we need to set u...'
---

By Leo Kyrpychenko

What if you want to self-correct the temperature in your office? Or what if you are curious to understand your office environment using IoT sensors?

If this sounds interesting to you, please read on.

To begin with, we need to set up a temperature reading sensor. We connect it to an Arduino which connects to a RaspberryPi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*luZBAP5jAeQXIoKDlm2Lqg.jpeg)

The next step is to set up AWS IoT SDK on your Raspberry Pi.

#### Setup the Thing

1. Create a thing in AWS IoT:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HMoK-8MpdziO3p1KgUu1WQ.png)

2. Create a single thing to begin with:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zkpo9cALdjh6y_91NkYlgQ.png)

3. Create a thing of a particular type. We are using RaspberryPi here (the types are made up by you).

![Image](https://cdn-media-1.freecodecamp.org/images/1*wpws9o3IaQd1QrhZerkgxw.png)

4.Create a certificate for your Thing to communicate with AWS:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kvhutJBA_nZMl4tCRYlPhw.png)

5. Download the certificates, a root certificate authority (CA), activate the Thing, and attach the policy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IlIegdjeWhnlsCPsk2CR9A.png)

6. The policy code is here. It may seem a bit permissive, but it is OK for the demo App.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mY-mP_JRKku7qBxk-PkTVg.png)

#### Setup your RaspberryPi

Before you start the setup, please copy all certificates and all root CA files over to the RaspberryPI (scp might help you). You also need to install Node.js if you don’t have it already.

You will also need to install the AWS IoT device SDK.

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nodejs

openssl x509 -in ./CA-roots/VeriSign-Class\ 3-Public-Primary-Certification-Authority-G5.pem -inform PEM -out root-CA.crt
chmod 775 root-CA.crt

npm install aws-iot-device-sdk
```

Here is the code that reads the data from the serial port and sends temperature readings using the AWS IoT device SDK. The code is based on the examples from Amazon.

```js
'use strict';

console.log('Running...');

const SerialPort = require('serialport');
const Readline = require('@serialport/parser-readline')

const portName = '/dev/ttyACM0';
const port = new SerialPort(portName, (err) => {
	if (err) {
		return console.log('Error: ', err.message);
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
	/* milliseconds */
	baseReconnectTimeMs: 4000,
	/* seconds */
	keepAlive: 300,
	/* milliseconds */
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

So now what can you do with that data?

You can write a Lambda that enqueues the data for processing. It may look like this:

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

And your serverless.com file may look like this:

```yaml
functions:
    sensorReadings:
        name: ${self:provider.stage}-${self:service}-sensor-readings
        handler: sensor-readings/index.handler
        description: Gets triggered by AWS IoT
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

I hope this post has saved you some time setting up your device. Thanks for reading!

