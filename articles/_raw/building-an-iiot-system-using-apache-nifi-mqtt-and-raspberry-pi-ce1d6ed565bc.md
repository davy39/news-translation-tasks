---
title: How to build an IIoT system using Apache NiFi, MiNiFi, C2 Server, MQTT and
  Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-27T19:29:34.000Z'
originalURL: https://freecodecamp.org/news/building-an-iiot-system-using-apache-nifi-mqtt-and-raspberry-pi-ce1d6ed565bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3VQlvDAxQimCkjdcSzhteg.png
tags:
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Abdelkrim Hadjidj

  How long do you think it takes to build an advanced Industrial IoT prototype that
  can:


  Collect data from sensors to a gateway at every factory

  Move sensors data from one or several factories to the Cloud or the Data Center

  Autom...'
---

By Abdelkrim Hadjidj

How long do you think it takes to build an advanced Industrial IoT prototype that can:

* Collect data from sensors to a gateway at every factory
* Move sensors data from one or several factories to the Cloud or the Data Center
* Automatically Warm-Deploy new configurations to all the edge devices
* Support large scale data volume and end-to-end security

With the right tool, you can build such system in less than one hour! In this blog post, I’ll show you how to implement an advanced IIoT prototype using Raspberry Pi hardware and open source softwares (MQTT broker, Apache NiFi, MiNiFi and MiNiFi C2 Server). I’ll focus on the architecture, the connectivity, the data collection and the automatic re-configuration.

This article is meant to be the beginning of a series of articles on IoT. Edge processing and data analysis will be the subject of following articles, so stay tuned :)

### Industrial IoT architecture

There are plenty of IoT reference architectures. Often, in industrial settings, you don’t have direct access to sensors and control systems. A gateway is used to bridge the OT and the IT world. For this reason, IIoT architecture often includes edge devices, gateways, regional hubs and finally storage/processing systems.

The following picture shows the global architecture of our system and the software tools that we will use at each level.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3VQlvDAxQimCkjdcSzhteg.png)
_IIoT architecture_

**At the edge level**, sensors collect information on the digital world and send them to a gateway through a variety of wired and wireless protocols (Serial, RS-485, MODBUS, CAN bus, OPC UA, BLE, WiFi, and so on). In our example, we will use various sensors (light, temperature, cameras, accelerometers, and so on) that send data to the gateway via WiFi.

**The gateway** is a Raspberry Pi running a Mosquitto Broker and a MiNiFi agent. [Mosquitto](https://mosquitto.org/) is an Open Source, lightweight messaging broker that we use to expose sensor data through the MQTT protocol. MQTT has a minimal footprint which makes it suitable for IoT applications and ressource constrained hardware, such as phones or microcontrollers.

Apache MiNiFi — a subproject of Apache NiFi — is a light-weight agent that implements the core features of Apache NiFi, focusing on data collection at the edge.

MiNiFi design goals are: small size and low resource consumption, central management of agents, and edge intelligence. MiNiFi can be easily integrated with NiFi through Site-to-Site protocol (S2S) to build an end-to-end flow management solution which is scalable, secure, and provides full chain of custody of information (provenance).

In our system, MiNiFi will subscribe to all the topics of the Mosquitto broker, and forward every new message to NiFi at the Regional level. We can also use it to connect to SCADA system or any other OT data provider.

**At the regional level,** we have two components:

[Apache NiFi](https://nifi.apache.org/) is a powerful data flow platform with more than 200 out-of-the-box connectors. Thanks to its UI, designing data flows becomes quick and easy.

NiFi doesn’t trade power for simplicity. Indeed, it’s a highly scalable distributed system with guaranteed delivery, backpressure, and load distribution. These features make NiFi a great tool for IoT applications where the network quality can be challenging.

In our system, NiFi plays the central role of collecting data from every factory and routing it to several systems and applications (HDFS, HBase, Kafka, S3, and so on).

[MiNiFi C2 Server (MiNiFi Commande & Control)](https://cwiki.apache.org/confluence/display/MINIFI/C2+Design+Proposal) is another subproject of Apache NiFi currently under development. Its role is to provide a central point of configuration to hundreds or thousands of MiNiFi agents in the wild. The C2 server manages versioned classes of applications (MiNiFi flow configurations) and exposes them through a Rest API. MiNiFi agents can connect to this API at a defined frequency to update their configuration.

Once data land at the company servers, on **the Cloud or at the Data Center**, there’s a large set of applications that can be implemented. Real-time monitoring, process analysis and optimization, or predictive maintenance are a few examples. Data processing and use case implementation will be discussed in a future article.

### System implementation

Let’s start building our prototype.

#### Preparing the Raspberry Pi: MQTT and MiNiFi

To install Mosquitto MQTT broker and MiNiFi agent, run the following commands on your Raspberry Pi.

To have a small size, MiNiFi is packaged with a minimal set of default processors. It’s possible to add any NiFi processor by deploying the NAR (NiFi Archive) in the lib directory. In the last command of the below block, I add the MQTT processor’s NAR.

```
sudo apt-get update#install and run Mosquitto broker on default port 1883sudo apt-get install mosquittomosquitto#install and prepare MiNiFi agentwget http://apache.crihan.fr/dist/nifi/minifi/0.4.0/minifi-0.4.0-bin.tar.gztar -xvf minifi-0.4.0-bin.tar.gzcd minifi-0.4.0#add mqtt processorwget https://github.com/ahadjidj-hw/NiFi/raw/master/nifi-mqtt-nar-1.5.0.nar -P ./lib/
```

By default, configuring a MiNiFi agent requires editing the file ./conf/config.yml to include the list of used processors and their configurations. The configuration can be written manually, or designed using the NiFi UI and exporting the flow as a template. The template is an XML file that we need to convert to a YML file with the [MiNiFi toolkit](https://nifi.apache.org/minifi/minifi-toolkit.html). Here’s an example of a [configuration file](https://github.com/apache/nifi-minifi/blob/master/minifi-bootstrap/src/test/resources/config.yml) that tails a file and sends each line to a remote NiFi via S2S.

For our project, we won’t use these manual steps. With many MiNiFi agents running on geographically distributed factories, it is not possible to manually stop, edit the config.yml, and then restart every agent every time their configuration needs to change.

MiNiFi uses a _“Change Ingestor”_ by which the agent is notified of a potential new configuration. Change ingestors are pluggable modules, and currently three ingestors are supported OOTB:

* FileChangeIngestor
* RestChangeIngestor
* PullHttpChangeIngestor

We will use a PullHttpChangeIngestor to query a C2 server every period of time and download any new configuration available. To configure this ingestor, edit the file ./conf/bootstrap.conf, uncomment the corresponding lines, and set the ingestor properties as follows:

```
nifi.minifi.notifier.ingestors=org.apache.nifi.minifi.bootstrap.configuration.ingestors.PullHttpChangeIngestor
```

```
# Hostname on which to pull configurations from
```

```
nifi.minifi.notifier.ingestors.pull.http.hostname=c2-server
```

```
# Port on which to pull configurations from
```

```
nifi.minifi.notifier.ingestors.pull.http.port=10080
```

```
# Path to pull configurations from
```

```
nifi.minifi.notifier.ingestors.pull.http.path=/c2/config
```

```
# Query string to pull configurations with
```

```
nifi.minifi.notifier.ingestors.pull.http.query=class=iot-minifi-raspberry-agent
```

```
# Period on which to pull configurations from, defaults to 5 minutes if commented out
```

```
nifi.minifi.notifier.ingestors.pull.http.period.ms=60000
```

With this configuration, each MiNiFi agent will query the C2 Server REST API at [http://c2-server:10080/c2/config](http://nifi-dev:10080/c2/config) every 1 minute and ask for the latest configuration for the “iot-minifi-raspberry-agent” class.

Note: the 1 minute frequency is only for demo purposes. You won’t be updating your agents so frequently.

Don’t start your agent now, and let’s move to the regional level and configure MiNiFi C2 server and NiFi.

#### Installing and configuring the MiNiFi C2 Server

Install MiNiFi C2 server on a public server that’s reachable from the MiNiFi agents. You can use hierarchical C2 deployment for network constrained applications as described a few lines below. Run the following command to install the C2 server:

```
wget http://apache.crihan.fr/dist/nifi/minifi/0.4.0/minifi-c2-0.4.0-bin.tar.gztar -xvf minifi-c2-0.4.0-bin.tar.gzcd minifi-c2-0.4.0
```

The C2 server exposes MiNiFi applications through a REST API organized by classes. C2 supports pluggable “Configuration Providers” and currently supports:

* The **CacheConfigurationProvider,** which looks at the directory on the filesystem or on S3
* The **DelegatingConfigurationProvider,** which delegates to another C2 server to allow for hierarchical C2 structures
* The **NiFiRestConfigurationProvider,** which pulls templates from a NiFi instance over its REST API

Configure the C2 Server to use NiFi as a configuration provider. Edit the file ./conf/minifi-c2-context.xml and provide the NiFi server address [http://nifi-dev:8080](http://nifi-dev:8080)

#### Installing and configuring the NiFi Server

Install NiFi on a server reachable from the C2 server and run it.

```
wget http://apache.crihan.fr/dist/nifi/1.6.0/nifi-1.6.0-bin.tar.gztar -xvf nifi-1.6.0-bin.tar.gzcd nifi-1.6.0./bin/nifi.sh start
```

Let’s connect to the NiFi UI at [http://nifi-dev:8080/nifi/](http://nifi-dev:8080/nifi/) and create the flow that will run in the MiNiFi agents. But before this, add an input port to the root canvas and name it “from Raspberry MiNiFi”. This is where NiFi will receive flow files from MiNiFi.

Add a consumeMQTT processor to subscribe to the Mosquitto broker and subscribe to all topics under _iot/sensors_. Note that the tcp://raspberrypi:1883 here is equivalent to tcp://localhost:1883, since this flow will be running on the Raspberry Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_2o7XYaLQis3B_K7UeMlNA.png)

Use an UpdateAttribute processor to add a _“version”_ attribute that we will use to show the re-configuration feature. You can add any attribute you want: timestamp, agent name, location, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AlovfoMCxTmo8fwIY_T9Jg.png)

And finally, add a Remote Process Group (RPG) to send the consumed events to NiFi. Connect these three processors.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pipjKZaixzgo6mx61D4ioA.png)

Your flow now looks like the below screenshot. The left flow will be running in NiFi to receive data from MiNiFi. The right flow here is only for design and will effectively run on each Raspberry Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8qMAq8mrVgwbY3MM4G6WZg.png)

Save the right flow as a template under the name “iot-minifi-raspberry-agent.v1”. The naming convention here is very important. We must use the same name as the class name used in the MiNiFi bootstrap configuration.

### Deploy and start the application

Before starting the MiNiFi agents on the Raspberry Pi, let’s see if the C2 server is well configured. Open the following URL in your web browser : [http://c2-server:10080/c2/config?class=iot-minifi-raspberry-agent&version=1](http://c2-server:10080/c2/config?class=iot-minifi-raspberry-agent&version=1) . The C2 Server replies with a file containing the configuration of the template we built, in YML format . That’s great.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dswF9vj5b8f8arb5dOAqAg.png)
_Results of C2 Rest API call_

If you look to the C2 logs, you can see that the server received a query with the parameters {class=[iot-minifi-raspberry-agent], version=[1]}

![Image](https://cdn-media-1.freecodecamp.org/images/1*bGTZK8FAhk1lZyksark5Zw.png)
_C2 server logs after the Rest API call_

Now that communication between the different components of the architecture (MQTT, MiNiFi, NiFi and C2) is working, start the MiNiFi agent on the Raspberry Pi with the command:

```
./bin/minifi.sh start
```

After a few seconds, you see the following C2 server logs. The host 192.168.1.50 (this is the Raspberry Pi’s IP address) asked the C2 server to give it the latest version of the class “iot-minifi-raspberry-agent”. Compared to our previous call with the web browser, you’ll notice that the MiNiFi agent didn’t specify a version. If you open now the MiNiFi agent configuration at ./conf/config.yml you will find the same conf file that we retrieved from the C2 Rest API.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Q4mCfsw_eUUVhJflVvs4g.png)
_C2 Server logs_

Also, the MQTT shows that the MiNiFi agent connected to the broker and subscribed to the topics iot/sensors/#

![Image](https://cdn-media-1.freecodecamp.org/images/1*nKnkdcvyDHg9V3mkX5j57Q.png)
_MQTT Logs after MiNiFi agent start_

Perfect! The IIoT system is running like a charm. Now let’s start our sensors to generate data and publish it in MQTT. MiNiFi will then start consuming data and sending it to NiFi as shown in the following screenshot where we have received 196 messages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_3ePgulNqJI5y7bf8PuV8g.png)

Now let’s inspect one of these messages with the provenance feature of NiFi. This data comes from the light sensor _“iot/sensors/LightIntensity/z”_ and the application version is 1.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3H9LUSHv-0_0o65xE3PrA.png)

### Automagic Warm Redeploy

Now that our IIoT is running and data is flowing from every factory to our data center, let’s deploy a new application. For our test, we will make a minor modification to our MiNiFi agent configuration. Go to the NiFi web UI and edit the updateAttribute processor. Set the “version” attribute to 2 instead of 1 and save the flow in a new template “iot-minifi-raspberry-agent.v2”. That’s all! The new application will be automagically deployed.

You can see the C2 server logs below showing that a new version V2 was detected. The C2 server does not have this version in its cache and start a download and conversion process.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m3jNaye1W-hWBIdvKsxK8w.png)
_C2 Server reaction to a new template_

Then, the MiNiFi agents detect the new configuration, backup the previous configuration, deploy the new one, and restart.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CpLj2Fvhyw7J3KPjPsSU-A.png)

Now let’s look to the data coming from the agents. As you can see in the provenance UI below, this data comes from a Gyroscope and has an application version 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*143i4FJ_vk6jkZQywxzxig.png)

### Conclusions

Apache NiFi and its eco-system (MiNiFi and C2 server) are powerful tools for end-to-end IoT data management. It can be used to easily and quickly build advanced IoT applications with flexible architectures and advanced features (automatic warm deploy, data provenance, backpressure, and so on).

In future articles, I’ll show you how to use this data, secure the platform, and implement advanced edge processing scenarios. In the meantime, you can read [this article](https://medium.com/@abdelkrim.hadjidj/best-practices-for-using-apache-nifi-in-real-world-projects-3-takeaways-1fe6912101db) on how Renault, a multinational automobile manufacturer, uses Apache NiFi in IIoT projects and what are the best practices that they adopted.

Thanks for reading. As always, feedback and suggestions are welcome.

If you found this article useful then give it some claps and follow me for more Big Data and IoT articles!

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZEb8WxL62ot7Wv5nRuinbQ.gif)
_Claps and subscription_

