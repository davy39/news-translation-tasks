---
title: Comment connecter le nRF9160 Feather à une instance Mosquitto auto-hébergée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-05T16:29:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-the-nrf9160-feather-to-mosquitto
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Copy-of-Bluetooth-with-nRF9160-Feather.png
tags:
- name: embedded systems
  slug: embedded-systems
- name: iot
  slug: iot
- name: mqtt
  slug: mqtt
seo_title: Comment connecter le nRF9160 Feather à une instance Mosquitto auto-hébergée
seo_desc: 'By Jared Wolff

  One thing that’s always tripped me up as an IoT developer is figuring out the best
  way to transmit data. There are many different kinds of radios and mediums. On top
  of that, there are different protocols to boot.

  As of this writing, t...'
---

Par Jared Wolff

Une chose qui m'a toujours posé problème en tant que développeur IoT est de trouver la meilleure façon de transmettre des données. Il existe de nombreux types de radios et de médias différents. En plus de cela, il existe différents protocoles.

À l'heure où j'écris ces lignes, il existe un protocole qui a régné en maître dans le monde de l'IoT :

MQTT.

Contrairement à un serveur HTTP, un appareil peut se connecter, publier et s'abonner à des sujets. Ces sujets sont ensuite envoyés à un courtier et distribués à d'autres appareils abonnés. Il se trouve également que MQTT sur le nRF9160 de Nordic est bien supporté.

Dans cet article, je vais vous montrer comment connecter le nRF9160 Feather à une instance auto-hébergée de [Mosquitto](https://github.com/eclipse/mosquitto). Vous apprendrez à générer vos propres certificats et à tester vos connexions.

Prêt à jouer ? Commençons.

## Où héberger ?

Si vous souhaitez héberger Mosquitto, vous aurez besoin d'un serveur. Puisque Mosquitto est écrit en C, il est léger et peut aller presque partout. De plus, il consomme peu de ressources, vous pouvez donc l'installer sur un VPS économique sans trop de soucis. C'est là qu'intervient un fournisseur de VPS comme Digital Ocean ou Vultr.

Pour configurer un nouveau serveur, voici quelques étapes :

* Connectez-vous à Digital Ocean. Si vous n'avez pas Digital Ocean et que vous souhaitez soutenir, cliquez [ici](https://m.do.co/c/9574d3846a29) pour créer un compte.
* Créez une nouvelle Droplet

![Créer une nouvelle droplet](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/Screen_Shot_2020-08-02_at_5.21.21_PM.png)

* Choisissez FreeBSD 12.1 avec UFS.

![Créer une Droplet FreeBSD 12.1 avec UFS](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/Screen_Shot_2020-08-02_at_5.21.29_PM.png)

* Choisissez l'instance à 5 $. Cela suffit généralement.

![Sélectionner le niveau de Droplet](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/Screen_Shot_2020-08-02_at_5.21.42_PM.png)

* Assurez-vous d'importer votre clé publique. Sinon, vous ne pourrez pas utiliser immédiatement la connexion sans mot de passe.

![Choisir la méthode d'authentification](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/Screen_Shot_2020-08-02_at_5.21.50_PM.png)

* Appuyez sur le bouton vert **Créer Droplet**, et mettons-nous en route.

![Bouton Créer Droplet](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/Screen_Shot_2020-08-02_at_5.21.54_PM.png)

### Étape supplémentaire importante

Pour que les certificats fonctionnent avec Mosquitto, vous devrez configurer un domaine pour pointer vers l'adresse IP de votre VPS. Un enregistrement CNAME ou A fonctionne. Si vous ne savez pas comment faire, [voici un bon guide](https://misago.gitbook.io/docs/setup/domain). Notez le (sous)domaine que vous avez utilisé. Nous en aurons besoin dans un instant...

## Installer Mosquitto

J'exécute mes serveurs dans une prison FreeBSD en utilisant [Bastille](https://bastillebsd.org/). Dans ce tutoriel, nous allons sauter la partie prison et nous concentrer sur le fonctionnement du nRF9160 Feather.

* Vous devriez être prêt avec une instance Digital Ocean (ou similaire) utilisant FreeBSD. Si vous ne l'avez pas encore fait, revenez à la section **Où héberger ?**.
* Ensuite, pour installer `mosquitto` sur votre droplet, exécutez `pkg install mosquitto`. Si vous utilisez autre chose que FreeBSD, cette commande peut différer. `apt-get install mosquitto` fonctionne sur les systèmes basés sur Debian. Si vous voulez les dépôts les plus à jour, assurez-vous d'exécuter `sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa` au préalable. Voici à quoi ressemble la sortie complète sur FreeBSD :

```bash
$ pkg install mosquitto
The package management tool is not yet installed on your system.
Do you want to fetch and install it now? [y/N]: y
Bootstrapping pkg from pkg+http://pkg.FreeBSD.org/FreeBSD:12:amd64/quarterly, please wait...
Verifying signature with trusted certificate pkg.freebsd.org.2013102301... done
[mosquitto] Installing pkg-1.14.6...
[mosquitto] Extracting pkg-1.14.6: 100%
Updating FreeBSD repository catalogue...
[mosquitto] Fetching meta.conf: 100%    163 B   0.2kB/s    00:01
[mosquitto] Fetching packagesite.txz: 100%    6 MiB   6.6MB/s    00:01
Processing entries: 100%
FreeBSD repository update completed. 31943 packages processed.
All repositories are up to date.
Updating database digests format: 100%
The following 4 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        c-ares: 1.16.1
        ca_root_nss: 3.55
        e2fsprogs-libuuid: 1.45.6
        mosquitto: 1.6.7

Number of packages to be installed: 4

The process will require 2 MiB more space.
682 KiB to be downloaded.

Proceed with this action? [y/N]: y
[mosquitto] [1/4] Fetching mosquitto-1.6.7.txz: 100%  226 KiB 231.1kB/s    00:01
[mosquitto] [2/4] Fetching ca_root_nss-3.55.txz: 100%  285 KiB 291.5kB/s    00:01
[mosquitto] [3/4] Fetching e2fsprogs-libuuid-1.45.6.txz: 100%   34 KiB  34.7kB/s    00:01
[mosquitto] [4/4] Fetching c-ares-1.16.1.txz: 100%  138 KiB 140.9kB/s    00:01
Checking integrity... done (0 conflicting)
[mosquitto] [1/4] Installing ca_root_nss-3.55...
[mosquitto] [1/4] Extracting ca_root_nss-3.55: 100%
[mosquitto] [2/4] Installing e2fsprogs-libuuid-1.45.6...
[mosquitto] [2/4] Extracting e2fsprogs-libuuid-1.45.6: 100%
[mosquitto] [3/4] Installing c-ares-1.16.1...
[mosquitto] [3/4] Extracting c-ares-1.16.1: 100%
[mosquitto] [4/4] Installing mosquitto-1.6.7...
===> Creating users
Using existing user 'nobody'.
[mosquitto] [4/4] Extracting mosquitto-1.6.7: 100%
=====
Message from ca_root_nss-3.55:

--
FreeBSD does not, and can not warrant that the certification authorities
whose certificates are included in this package have in any way been
audited for trustworthiness or RFC 3647 compliance.

Assessment and verification of trust is the complete responsibility of the
system administrator.

This package installs symlinks to support root certificates discovery by
default for software that uses OpenSSL.

This enables SSL Certificate Verification by client software without manual
intervention.

If you prefer to do this manually, replace the following symlinks with
either an empty file or your site-local certificate bundle.

  * /etc/ssl/cert.pem
  * /usr/local/etc/ssl/cert.pem
  * /usr/local/openssl/cert.pem
=====
Message from mosquitto-1.6.7:

--
The mosquitto MQTT Python driver is now provided by net/py-paho-mqtt

```

Toute la configuration des packages installés se trouve dans `/usr/local/etc/mosquitto/`. Nous devrons éditer `mosquitto.conf` dans ce dossier pour utiliser des certificats. Voici à quoi il ressemble :

```bash
# Configuration du démon
pid_file /var/run/mosquitto.pid
user nobody

# Port à utiliser pour l'écouteur par défaut.
port 8885

# Au moins l'un de cafile ou capath doit être défini.
cafile /root/pki/ca.crt

# Chemin vers le certificat serveur encodé PEM.
certfile /root/pki/issued/mosquitto.crt

# Chemin vers le fichier de clé encodé PEM.
keyfile /root/pki/private/mosquitto.key

# Chemin vers le fichier CRL
#crlfile /root/pki/crl.pem

# Chaque client a son propre certificat
require_certificate true
use_identity_as_username true

# port d'écoute [adresse IP/nom d'hôte]
listener 1883
protocol mqtt

# port d'écoute [adresse IP/nom d'hôte]
# listener 8080
# protocol websockets

# =================================================================
# Journalisation
# =================================================================
log_dest syslog

# Types de messages à journaliser.
log_type all
#log_type warning
# websockets_log_level 127

# -----------------------------------------------------------------
# Authentification par défaut et contrôle d'accès aux sujets
# -----------------------------------------------------------------
# password_file /usr/local/etc/mosquitto/pwfile

```

Avant de pouvoir démarrer le serveur, nous devrons provisionner quelques certificats RSA. Nous y viendrons dans l'étape suivante.

## Provisionner les certificats

Vous pouvez utiliser **easy-rsa** pour générer un serveur CA et des certificats clients. (Ces instructions proviennent de [ce guide](https://github.com/OpenVPN/easy-rsa/blob/master/README.quickstart.md).) Pour la production, vous devez générer vos clés et certificats sur une machine hors ligne. Ainsi, vos clés privées sont en sécurité si votre serveur devient une cible.

Tout d'abord, installez `easy-rsa` :

```bash
$ pkg install easy-rsa
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
All repositories are up to date.
The following 1 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        easy-rsa: 3.0.7

Number of packages to be installed: 1

44 KiB to be downloaded.

Proceed with this action? [y/N]: y
[mosquitto] [1/1] Fetching easy-rsa-3.0.7.txz: 100%   44 KiB  44.8kB/s    00:01
Checking integrity... done (0 conflicting)
[mosquitto] [1/1] Installing easy-rsa-3.0.7...
[mosquitto] [1/1] Extracting easy-rsa-3.0.7: 100%

```

Ensuite, commençons le processus de création de certificats :

```fallback
$ easyrsa init-pki

Note: using Easy-RSA configuration from: /usr/local/share/easy-rsa/vars

init-pki complete; you may now create a CA or requests.
Your newly created PKI dir is: /root/pki
$
$ easyrsa build-ca

Note: using Easy-RSA configuration from: /usr/local/share/easy-rsa/vars
Using SSL: openssl OpenSSL 1.1.1d-freebsd  10 Sep 2019

Enter New CA Key Passphrase:
Re-Enter New CA Key Passphrase:
Generating RSA private key, 2048 bit long modulus (2 primes)
......................+++++
..................................................................................+++++
e is 65537 (0x010001)
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [Easy-RSA CA]:testserver.jaredwolff.com

CA creation complete and you may now import and sign cert requests.
Your new CA certificate file for publishing is at:
/root/pki/ca.crt

```

**Note :** Vous serez invité à entrer un mot de passe à l'étape `build-ca`. Assurez-vous de garder ce mot de passe à portée de main.

Pour générer un certificat serveur, utilisez :

```fallback
$ easyrsa gen-req mosquitto nopass

Note: using Easy-RSA configuration from: /usr/local/share/easy-rsa/vars
Using SSL: openssl OpenSSL 1.1.1d-freebsd  10 Sep 2019
Generating a RSA private key
...............+++++
........................................+++++
writing new private key to '/root/pki/easy-rsa-82720.X2NVQ0/tmp.akOxhO'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [mosquitto]:testserver.jaredwolff.com

Keypair and certificate request completed. Your files are:
req: /root/pki/reqs/mosquitto.req
key: /root/pki/private/mosquitto.key
$
$ easyrsa sign-req server mosquitto

Note: using Easy-RSA configuration from: /usr/local/share/easy-rsa/vars
Using SSL: openssl OpenSSL 1.1.1d-freebsd  10 Sep 2019

You are about to sign the following certificate.
Please check over the details shown below for accuracy. Note that this request
has not been cryptographically verified. Please be sure it came from a trusted
source or that you have verified the request checksum with the sender.

Request subject, to be signed as a server certificate for 825 days:

subject=
    commonName                = testserver.jaredwolff.com

Type the word 'yes' to continue, or any other input to abort.
  Confirm request details: yes
Using configuration from /root/pki/easy-rsa-82744.hyuGzt/tmp.lZHLEH
Enter pass phrase for /root/pki/private/ca.key:
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
commonName            :ASN.1 12:'testserver.jaredwolff.com'
Certificate is to be certified until Nov  3 01:12:53 2022 GMT (825 days)

Write out database with 1 new entries
Data Base Updated

Certificate created at: /root/pki/issued/mosquitto.crt

```

Vous serez invité à entrer à la fois le Common Name (c'est-à-dire le nom de votre serveur) et le mot de passe du certificat CA dans l'étape ci-dessus. **Important** : le **Common Name** doit correspondre au nom de domaine de votre serveur ! (Vous vous souvenez, nous l'avons noté plus tôt ?)

Pour générer le certificat nRF9160, utilisez :

```fallback
$ easyrsa gen-req nrf9160 nopass batch
$ easyrsa sign-req client nrf9160 batch

```

Suivez la même procédure que précédemment. La seule différence est que nous générons un certificat **client** au lieu d'un certificat **serveur**.

Une fois terminé, nous aurons besoin de certains fichiers. Voici une liste complète :

**Pour votre serveur Mosquitto**

* `/root/pki/ca.crt`
* `/root/pki/private/mosquitto.key`
* `/root/pki/issued/mosquitto.crt`

**Pour votre nRF9160 Feather**

* `/root/pki/ca.crt`
* `/root/pki/private/nrf9160.key`
* `/root/pki/issued/nrf9160.crt`

Si vous utilisez la configuration ci-dessus, elle pointe déjà vers vos certificats serveur. Tout ce que nous avons à faire maintenant est de démarrer `mosquitto` !

```bash
$ service mosquitto start
Cannot 'start' mosquitto. Set mosquitto_enable to YES in /etc/rc.conf or use 'onestart' instead of 'start'.

```

Si vous obtenez une erreur concernant `mosquitto_enable`, exécutez simplement :

```bash
$ sysrc mosquitto_enable=YES
$ service mosquitto start
Starting mosquitto.

```

Cela permet à `mosquitto` de démarrer lorsque votre système démarre.

Maintenant, vérifiez si `mosquitto` est en cours d'exécution en utilisant `ps aux` :

```bash

$ ps aux
USER     PID %CPU %MEM   VSZ  RSS TT  STAT STARTED    TIME COMMAND
root   82401  0.0  0.2 11472 2424  -  SsJ  01:02   0:00.00 /usr/sbin/syslogd -ss
root   82457  0.0  0.2 11408 2284  -  IsJ  01:02   0:00.00 /usr/sbin/cron -J 60 -s
nobody 82900  0.0  0.6 16352 6212  -  SsJ  01:17   0:00.02 /usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf -d
root   82488  0.0  0.3 12096 2848  0  IJ   01:02   0:00.01 login [pam] (login)
root   82489  0.0  0.3 13092 3504  0  SJ   01:02   0:00.03 -csh (csh)
root   82902  0.0  0.3 11704 2540  0  R+J  01:17   0:00.00 ps aux

```

Maintenant que nous avons un serveur chargé et en cours d'exécution, faisons fonctionner le firmware.

## Bits de firmware

Travailler avec des certificats sur le nRF9160 Feather est un processus en deux étapes. La première étape consiste à charger les certificats à l'aide du firmware `at_client`. La seconde est de charger la bibliothèque `mqtt_simple` avec un support TLS ajouté. Commençons par les certificats.

### Programmez d'abord `at_client`

Changez de répertoire pour `ncs/nrf/samples/nrf9160/at_client/` et commencez une nouvelle compilation :

```c
$ west build -b circuitdojo_feather_nrf9160ns -p

```

Puis flashez sur votre carte en utilisant :

```c
$ west flash --erase
$ nrfjprog -r

```

Nous aurons besoin de cet exemple sur votre carte pour l'étape suivante.

### Ajouter des certificats à l'appareil

Pour installer nos nouveaux certificats, nous aurons besoin de nRF Connect Desktop installé. Vous pouvez le télécharger [en allant ici](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Connect-for-desktop/Download#infotabs).

Vous aurez également besoin d'une version personnalisée de **LTE Link Monitor**. Vous pouvez obtenir la version modifiée sur [docs.jaredwolff.com](http://localhost:3000/files/pc-nrfconnect-linkmonitor-1.1.1.tgz).

Tout d'abord, installez l'application nRF Connect Desktop. Ensuite, copiez le fichier .tgz de LTE Link Monitor dans `%USERPROFILE%\.nrfconnect-apps\local` (sur Windows) ou `$HOME/.nrfconnect-apps/local` (sur Linux/macOS). Voici un exemple de l'endroit où il se trouve sur Windows :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-11.png)

Fermez et rouvrez nRF Connect Desktop (s'il est ouvert).

Ensuite, cliquez sur _Ouvrir_ à côté de la version 1.1.1 de LTE Link Monitor. Il y aura également écrit **local** en dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-12.png)

Ensuite, lançons-le !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-13.png)

Une fois que vous avez ouvert le port, appuyez sur le bouton de réinitialisation. Assurez-vous de désactiver les **Demandes automatiques**.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-14.png)

Ensuite, dans la boîte de commande, envoyez **AT+CFUN=4**. Cela éteindra votre modem pour qu'il soit prêt à télécharger des certificats. Vous pouvez exécuter **AT+CFUN?** pour confirmer que votre modem est dans ce mode.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-15.png)

Ouvrez le gestionnaire de certificats.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-16.png)

Assurez-vous de définir la balise de sécurité. Dans ce cas, j'utilise 1234. Il s'agit d'un identifiant important dont vous aurez besoin plus tard. Faites-en ce que vous voulez, mais je vous déconseille d'utiliser 16842753. Il s'agit de la balise par défaut pour NRF Cloud. Vous ne voulez pas effacer vos certificats nRF Cloud !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-17.png)

Copiez et collez le contenu de vos fichiers `ca.crt`, `nrf9160.crt` et `nrf9160.key` dans les cases (dans cet ordre). Vous pouvez facilement obtenir les certificats en utilisant `cat` sur Unix/Linux :

```bash
$ cat cat.crt
-----BEGIN CERTIFICATE-----
MIIDdTCCAl2gAwIBAgIUDLkBxLLQO9wosNDtA7E9qvqHOxMwDQYJKoZIhvcNAQEL
BQAwJDEiMCAGA1UEAwwZdGVzdHNlcnZlci5qYXJlZHdvbGZmLmNvbTAeFw0yMDA3
MzEwMTExNDJaFw0zMDA3MjkwMTExNDJaMCQxIjAgBgNVBAMMGXRlc3RzZXJ2ZXIu
amFyZWR3b2xmZi5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC3
de1v8k+FXzY/Im7Z2YKS7wwbBRft5CUxqP1sdYJgMvheS9LhFufk81URZ0lHD9pK
aNPxU1UEmnLvVDTGLJ+YAmMH08xn17FS1R1UVPYzi2ouwqRM2pR9EStsSlP9Zj44
1MsdizABnnlkZndUVLL/gjc4cNsNncMLBSEbsz6b5WzhtAGg3rOpdAxSSblZVSFw
bquCgg5hb2NUzy+JxGtUIsE5d6CxTDdSs4Z3FK/RRYjmCG6qsaya4N5W35yf8h5O
StfKRecl3kq2kCnWa6P+lErG4wuxIBtMkgz2zV+zd1tz4aHXxSdoZTqLz7dTVbFA
zEVnKD+ZReBG+4fwUL6rAgMBAAGjgZ4wgZswHQYDVR0OBBYEFIvdGnjrxRPzvXQi
7XJ70LzpZSOjMF8GA1UdIwRYMFaAFIvdGnjrxRPzvXQi7XJ70LzpZSOjoSikJjAk
MSIwIAYDVQQDDBl0ZXN0c2VydmVyLmphcmVkd29sZmYuY29tghQMuQHEstA73Ciw
0O0DsT2q+oc7EzAMBgNVHRMEBTADAQH/MAsGA1UdDwQEAwIBBjANBgkqhkiG9w0B
AQsFAAOCAQEAIzz1nSSDkPueNPlADRYMDOMFNkxoKA+gRXwDVa7y39As7IZp7Fqr
KAH79U1XtGyDlt6FPKTvDJ7jtd4y8auIGVQO7z3AG9pVU1imIWZHoIqgBUCEhsjp
uMxD23kRCX5kd9dsmF9WOGGxb4kkMv83Rh2rCONQmvnozuI3fJv2ZFX/ORoADGLP
OPSJPl11x+2rxPxiLi+T8RyzDh3DwqnPVsSnbRWV7hosaN0ip/cbnSTaIul9mbCY
ID6qm9leqlY/gha9aZfg+tv1Lm6PT6o8Pzek2VeDoIS5YERBMOwV84hQrZjV3vIE
jT6y663HGsl7KvqVaWdV3fM6Cr7f0QdR5A==
-----END CERTIFICATE-----

```

Vous aurez besoin de tout, de `-----BEGIN CERTIFICATE-----` à `-----END CERTIFICATE-----`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-18.png)

Vérifiez la zone **Journal** pour plus de détails. Si tout s'est bien passé, il devrait indiquer que vos certificats ont été mis à jour.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-19.png)

### Utilisation de l'exemple mqtt_simple

Nous utiliserons l'exemple `mqtt_simple` dans le dépôt nRF Connect SDK. Le chemin complet est : `ncs/nrf/samples/nrf9160/mqtt_simple`. Nous devrons apporter quelques modifications pour ajouter une compatibilité TLS complète. Tous les fichiers se trouvent dans le répertoire `mqtt_simple`.

Tout d'abord, nous devrons mettre à jour le fichier `proj.conf`. Voici les différences mises en évidence :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-20.png)

La section `# Set the PDP Context` est particulièrement importante si vous utilisez une carte SIM Hologram (incluse avec le nRF9160 Feather). Si vous utilisez une SIM qui n'en a pas besoin, vous n'avez pas besoin de cette section.

Adaptez votre `CONFIG_MQTT_BROKER_HOSTNAME` à votre nom d'hôte (configuré au début de ce guide).

Vous devrez également ajouter ces lignes dans `KConfig` :

```c
config SEC_TAG
	int "Security tag to use for the connection"
	default 1234

config PEER_VERIFY
	int "Peer verify parameter for mqtt_client"
	default 1
	help
			Set to 0 for VERIFY_NONE, 1 for VERIFY_OPTIONAL, and 2 for VERIFY_REQUIRED.

```

Enfin, dans main, ajoutez ce bloc en haut de votre fichier :

```c
#if defined(CONFIG_MQTT_LIB_TLS)
static sec_tag_t sec_tag_list[] = { CONFIG_SEC_TAG };
#endif /* defined(CONFIG_MQTT_LIB_TLS) */

```

Puis ajoutez ce bloc à `client_init` sous `#if defined(CONFIG_MQTT_LIB_TLS)`

```c
  struct mqtt_sec_config *tls_config = &client->transport.tls.config;

	client->transport.type = MQTT_TRANSPORT_SECURE;

	tls_config->peer_verify = CONFIG_PEER_VERIFY;
	tls_config->cipher_count = 0;
	tls_config->cipher_list = NULL;
	tls_config->sec_tag_count = ARRAY_SIZE(sec_tag_list);
	tls_config->sec_tag_list = sec_tag_list;
	tls_config->hostname = CONFIG_MQTT_BROKER_HOSTNAME;

```

Les modifications devraient ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-21.png)

Puis compilez avec :

```c
$ west build -b circuitdojo_feather_nrf9160ns -p

```

Enfin, flashez-le en utilisant `west flash` :

```c
$ west flash --erase
$ nrfjprog -r

```

Ouvrez votre terminal série et vérifiez que votre nRF9160 Feather se connecte. Vous pouvez également utiliser LTE Link Monitor pour voir votre progression (exemple ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-22.png)

Beaucoup des informations ci-dessus proviennent de l'article de [Nordic](https://devzone.nordicsemi.com/nordic/cellular-iot-guides/b/software-and-protocols/posts/enabling-and-testing-tls-in-mqtt_5f00_simple) sur le sujet.

## Envoyer un message

Nous y sommes presque ! Vous avez configuré votre nRF9160 Feather pour qu'il se connecte à Mosquitto en utilisant des certificats auto-générés. La dernière partie consiste à connecter un autre appareil pour voir si le nRF9160 Feather répond à un message.

J'ai créé un nouvel ensemble de certificats à cette fin. Je les ai appelés `test`.

```bash
$ easyrsa gen-req test nopass batch
$ easyrsa sign-req client test batch

```

Je les ai copiés sur mon bureau en utilisant CyberDuck (un excellent petit client SFTP visuel) :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-23.png)

Vous pouvez également utiliser quelque chose comme `scp` si vous êtes confiant dans vos capacités de transfert de fichiers en ligne de commande. Ensuite, ouvrez un terminal et exécutez :

```bash
mosquitto_sub --cafile ca.crt --cert test.crt --key test.key -q 1 -d -h testserver.jaredwolff.com -p 8885 -t "/my/publish/topic" &
mosquitto_pub --cafile ca.crt --cert test.crt --key test.key -q 1 -d -h testserver.jaredwolff.com -p 8885 -t "/my/subscribe/topic" -m "hello there"

```

Vous devriez voir une sortie comme celle-ci :

```bash
$ mosquitto_sub --cafile ca.crt --cert test.crt --key test.key -q 1 -d -h testserver.jaredwolff.com -p 8885 -t "/my/publish/topic" &
$ mosquitto_pub --cafile ca.crt --cert test.crt --key test.key -q 1 -d -h testserver.jaredwolff.com -p 8885 -t "/my/subscribe/topic" -m "hello there"
Client mosq-CczskQKzMKdtTo4O4s sending CONNECT
Client mosq-CczskQKzMKdtTo4O4s received CONNACK (0)
Client mosq-CczskQKzMKdtTo4O4s sending PUBLISH (d0, q1, r0, m1, '/my/subscribe/topic', ... (11 bytes))
Client mosq-CczskQKzMKdtTo4O4s received PUBACK (Mid: 1, RC:0)
Client mosq-CczskQKzMKdtTo4O4s sending DISCONNECT
MacBook-Pro:Downloads jaredwolff$ Client mosq-qK8tMlJk0Qri4Z7jUo sending PINGREQ
Client mosq-qK8tMlJk0Qri4Z7jUo received PINGRESP
MacBook-Pro:Downloads jaredwolff$ Client mosq-qK8tMlJk0Qri4Z7jUo received PUBLISH (d0, q0, r0, m0, '/my/publish/topic', ... (11 bytes))
hello there

```

Hourra ! Vous avez une connexion active et fonctionnelle à votre propre serveur Mosquitto.

## Conclusion

Nous avons atteint la fin ! À ce stade de l'article, vous devriez avoir un serveur Mosquitto en cours d'exécution et un nRF9160 connecté. Maintenant, vous pouvez utiliser vos nouvelles compétences pour ajouter plus d'appareils à vos déploiements et plus encore.

Si vous n'avez pas encore eu l'occasion de jouer avec le nRF9160, vous devriez consulter le nRF9160 Feather. Il dispose du nRF9160 LTE-M, NB IoT + GPS Combo de Nordic Semiconductor, ainsi qu'une alimentation flexible, une mémoire flash externe et une mise hors tension à faible consommation.

Oh, et did I mention it's 100% open source? Learn more by checking out the campaign on [GroupGets and Hackster Launch](https://www.jaredwolff.com/store/nrf91-feather/). 🚀

![nRF9160 Feather Top Side](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/IMG_8749.jpg)

![nRF9160 Feather Bottom Side](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/images/IMG_8750.jpg)

Crédit photo aux gens formidables de [GroupGets](https://www.groupgets.com/) !

**Vous pouvez lire cet article et beaucoup d'autres bonnes choses sur [jaredwolff.com](https://www.jaredwolff.com/how-to-connect-nrf9160-feather-to-mosquitto/).**