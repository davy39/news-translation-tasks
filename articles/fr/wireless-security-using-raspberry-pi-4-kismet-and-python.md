---
title: Comment sécuriser votre infrastructure sans fil domestique avec Kismet et Python
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-03-02T16:22:20.000Z'
originalURL: https://freecodecamp.org/news/wireless-security-using-raspberry-pi-4-kismet-and-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/wireless_security_with_kismet_and_python.png
tags:
- name: information security
  slug: information-security
- name: Python
  slug: python
- name: Raspberry Pi
  slug: raspberry-pi
- name: Security
  slug: security
seo_title: Comment sécuriser votre infrastructure sans fil domestique avec Kismet
  et Python
seo_desc: 'Everything is connected to wireless these days. In my case I found that
  I have LOTS of devices after running a simple nmap command on my home network:

  [josevnz@dmaf5 ~]$ sudo nmap -v -n -p- -sT -sV -O --osscan-limit --max-os-tries
  1 -oX $HOME/home_sc...'
---

Tout est connecté sans fil de nos jours. Dans mon cas, j'ai découvert que j'avais BEAUCOUP d'appareils après avoir exécuté une simple [commande nmap sur mon réseau domestique](https://www.freecodecamp.org/news/enhance-nmap-with-python/#nmap-101-identify-all-the-public-services-in-our-network) :

```shell
[josevnz@dmaf5 ~]$ sudo nmap -v -n -p- -sT -sV -O --osscan-limit --max-os-tries 1 -oX $HOME/home_scan.xml 192.168.1.0/24
```

Alors j'ai commencé à me demander :

* Mon réseau sans fil est-il sécurisé ?
  
* Combien de temps faudrait-il à un attaquant pour s'infiltrer ?
  

J'ai un *Raspberry 4* avec Ubuntu (focal) installé et j'ai décidé d'utiliser le bien connu [Kismet](https://www.kismetwireless.net/) pour le découvrir.

Dans cet article, vous apprendrez :

* Comment obtenir une vue d'ensemble des réseaux à proximité avec Kismet
  
* Comment personnaliser Kismet en utilisant Python et l'API REST
  

![Image](https://www.freecodecamp.org/news/content/images/2022/03/raspberrypi-wireless-setup-1.png align="left")

*Si vous êtes curieux, voici mon Raspberry PI 4 domestique, petit moniteur et tout*

# Table des matières

* [Le dicton 'Mieux vaut prévenir que guérir' ne s'applique pas ici](#heading-le-dicton-mieux-vaut-prevenir-que-guerir-ne-sapplique-pas-ici)
  
* [Découverte de votre matériel](#heading-decouverte-de-votre-materiel)
  
* [kismet](#kismet)
  
* [REST-API](#restapi)
  
* [Qu'avons-nous appris ?](#heading-quavons-nous-appris)
  

# Le dicton 'Mieux vaut prévenir que guérir' ne s'applique pas ici

Et par là, je veux dire que *vous ne devriez pas essayer d'écouter ou d'infiltrer un réseau sans fil qui ne vous appartient pas*. Il est relativement facile de détecter si un nouveau client inconnu a rejoint votre réseau sans fil, et c'est aussi illégal.

Alors faites ce qu'il faut – utilisez ce tutoriel pour apprendre et non pour pirater le réseau de quelqu'un d'autre, d'accord ?

# Découverte de votre matériel

Je vais sauter un peu en avant pour vous montrer un petit problème avec l'interface sans fil intégrée du Raspberry 4.

**La carte sans fil intégrée du Raspberry PI 4 ne fonctionnera pas directement** car le firmware ne supporte pas le mode moniteur.

Il existe des travaux pour [supporter cela](https://github.com/seemoo-lab/bcm-rpi3). Au lieu de cela, j'ai pris la solution de facilité et j'ai commandé un dongle Wi-Fi externe chez [CanaKit](https://www.canakit.com/raspberry-pi-wifi.html).

La carte sans fil CanaKit a fonctionné directement, et nous la verrons bientôt. Mais d'abord, installons et jouons avec Kismet.

## Assurez-vous que l'interface fonctionne en mode moniteur

Par défaut, l'interface réseau aura le mode moniteur désactivé :

```shell
root@raspberrypi:~# iwconfig wlan1
wlan1     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=0 dBm   
          Retry short  long limit:2   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
```

Je sais que je vais toujours configurer mon adaptateur sans fil Ralink Technology, Corp. RT5370 en mode moniteur, mais je dois être prudent car Ubuntu peut échanger wlan0 et wlan1 (l'adaptateur Broadcom que je veux ignorer est un périphérique PCI).

L'adaptateur Ralink est un adaptateur USB, donc nous pouvons découvrir où il se trouve :

```shell
josevnz@raspberrypi:/etc/netplan$ /bin/lsusb|grep Ralink
Bus 001 Device 004: ID 148f:5370 Ralink Technology, Corp. RT5370 Wireless Adapter
```

Maintenant, nous devons découvrir quel périphérique a été mappé à l'adaptateur Ralink. Avec un peu d'aide de la communauté Ubuntu, j'ai découvert que l'adaptateur Ralink utilise le pilote rt2800usb [5370 Ralink Technology](https://help.ubuntu.com/community/WifiDocs/Device/Ralink_RT5370)

La réponse que je cherche est ici :

```shell
josevnz@raspberrypi:~$ ls /sys/bus/usb/drivers/rt2800usb/*:1.0/net/
wlan1
```

Ainsi, le code qui effectue la détection de la carte sans fil ressemble à ceci :

```shell
root@raspberrypi:~#/bin/cat<<RC_LOCAL>/etc/rc.local
#!/bin/bash
usb_driver=rt2800usb
wlan=$(/bin/ls /sys/bus/usb/drivers/$usb_driver/*/net/)
if [ $? -eq 0 ]; then
        set -ex
        /usr/sbin/ifconfig "$wlan" down
        /usr/sbin/iwconfig "$wlan" mode monitor
        /usr/sbin/ifconfig "$wlan" up
        set +ex
fi
RC_LOCAL
root@raspberrypi:~# chmod u+x /etc/rc.local && shutdown -r now "Enabling monitor mode"
```

Assurez-vous que la carte est en mode moniteur :

```shell
root@raspberrypi:~# iwconfig wlan1
iw        iwconfig  iwevent   iwgetid   iwlist    iwpriv    iwspy     
root@raspberrypi:~# iwconfig wlan1
wlan1     IEEE 802.11  Mode:Monitor  Frequency:2.412 GHz  Tx-Power=20 dBm   
          Retry short  long limit:2   RTS thr:off   Fragment thr:off
          Power Management:off
```

Bien, continuons avec la configuration de l'outil

# Qu'est-ce que Kismet ?

[Kismet](https://www.kismetwireless.net/) est :

> un détecteur de réseau et d'appareils sans fil, un renifleur, un outil de wardriving, et un framework de détection d'intrusion sans fil (WIDS).

## Installation et configuration de Kismet

La version qui vient avec Ubuntu RaspberryPI par défaut est de 2016, *beaucoup trop ancienne*.

Au lieu de cela, obtenez un binaire mis à jour comme [expliqué ici](https://www.kismetwireless.net/docs/readme/packages/) (j'ai Ubuntu focal, vérifiez avec `lsb_release --all`).

```shell
wget -O - https://www.kismetwireless.net/repos/kismet-release.gpg.key | sudo apt-key add -
echo 'deb https://www.kismetwireless.net/repos/apt/release/focal focal main' | sudo tee /etc/apt/sources.list.d/kismet.list
sudo apt update
sudo apt install kismet
```

### Ne pas exécuter en tant que root, utilisez un [binaire SUID](https://fr.wikipedia.org/wiki/Setuid) et un accès de groupe unix

Kismet nécessite des privilèges élevés pour s'exécuter. Et traite des données potentiellement hostiles. Donc, l'exécuter avec des permissions minimisées est l'approche la plus sûre.

La bonne façon de le configurer est d'utiliser un groupe Unix et un binaire set user id (*SUID*). Mon utilisateur est 'josevnz' donc j'ai fait ceci :

```python
sudo apt-get install kismet
sudo usermod --append --groups kismet josevnz
```

### Chiffrez votre accès à Kismet avec un certificat auto-signé

Je vais activer SSL pour mon installation Kismet [en utilisant un certificat auto-signé](https://github.com/josevnz/home_nmap/tree/main/tutorial). J'utiliserai pour cela les outils Cloudflare CFSSL :

```python
sudo apt-get update -y
sudo apt-get install -y golang-cfssl
```

L'étape suivante est de créer les certificats auto-signés. Il y a beaucoup d'étapes de boilerplate ici, donc je vais vous montrer comment vous pouvez sauter à travers elles (mais lisez les pages de manuel pour voir ce que chaque commande fait) :

#### Certificat initial

```shell
sudo /bin/mkdir --parents /etc/pki/raspberrypi
sudo /bin/cat<<CA>/etc/pki/raspberrypi/ca.json
{
   "CN": "Nunez Barrios family Root CA",
   "key": {
     "algo": "rsa",
     "size": 2048
   },
   "names": [
   {
     "C": "US",
     "L": "CT",
     "O": "Nunez Barrios",
     "OU": "Nunez Barrios Root CA",
     "ST": "United States"
   }
  ]
}
CA
cfssl gencert -initca ca.json | cfssljson -bare ca
```

#### Configuration du profil SSL

```shell
root@raspberrypi:/etc/pki/raspberrypi# /bin/cat<<PROFILE>/etc/pki/raspberrypi/cfssl.json
{
   "signing": {
     "default": {
       "expiry": "17532h"
     },
     "profiles": {
       "intermediate_ca": {
         "usages": [
             "signing",
             "digital signature",
             "key encipherment",
             "cert sign",
             "crl sign",
             "server auth",
             "client auth"
         ],
         "expiry": "17532h",
         "ca_constraint": {
             "is_ca": true,
             "max_path_len": 0, 
             "max_path_len_zero": true
         }
       },
       "peer": {
         "usages": [
             "signing",
             "digital signature",
             "key encipherment", 
             "client auth",
             "server auth"
         ],
         "expiry": "17532h"
       },
       "server": {
         "usages": [
           "signing",
           "digital signing",
           "key encipherment",
           "server auth"
         ],
         "expiry": "17532h"
       },
       "client": {
         "usages": [
           "signing",
           "digital signature",
           "key encipherment", 
           "client auth"
         ],
         "expiry": "17532h"
       }
     }
   }
}
PROFILE
```

#### Certificat intermédiaire

```shell
root@raspberrypi:/etc/pki/raspberrypi# /bin/cat<<INTERMEDIATE>/etc/pki/raspberrypi/intermediate-ca.json
{
  "CN": "Barrios Nunez Intermediate CA",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C":  "US",
      "L":  "CT",
      "O":  "Barrios Nunez",
      "OU": "Barrios Nunez Intermediate CA",
      "ST": "USA"
    }
  ],
  "ca": {
    "expiry": "43830h"
  }
}
INTERMEDIATE
cfssl gencert -initca intermediate-ca.json | cfssljson -bare intermediate_ca
cfssl sign -ca ca.pem -ca-key ca-key.pem -config cfssl.json -profile intermediate_ca intermediate_ca.csr | cfssljson -bare intermediate_ca
```

#### Configuration pour le certificat SSL sur la machine Raspberry PI 4

Ici, nous mettons le nom et l'adresse IP de la machine qui exécutera notre application web Kismet :

```shell
/bin/cat<<RASPBERRYPI>/etc/pki/raspberrypi/raspberrypi.home.json
{
  "CN": "raspberrypi.home",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
  {
    "C": "US",
    "L": "CT",
    "O": "Barrios Nunez",
    "OU": "Barrios Nunez Hosts",
    "ST": "USA"
  }
  ],
  "hosts": [
    "raspberrypi.home",
    "localhost",
    "raspberrypi",
    "192.168.1.11"
  ]               
}
RASPBERRYPI
cd /etc/pki/raspberrypi
cfssl gencert -ca intermediate_ca.pem -ca-key intermediate_ca-key.pem -config cfssl.json -profile=peer raspberrypi.home.json| cfssljson -bare raspberry-peer
cfssl gencert -ca intermediate_ca.pem -ca-key intermediate_ca-key.pem -config cfssl.json -profile=server raspberrypi.home.json| cfssljson -bare raspberry-server
cfssl gencert -ca intermediate_ca.pem -ca-key intermediate_ca-key.pem -config cfssl.json -profile=client raspberrypi.home.json| cfssljson -bare raspberry-client
```

L'ajout de la prise en charge SSL est alors aussi simple que d'ajouter les substitutions suivantes :

```shell
/bin/cat<<SSL>>/etc/kismet/kismet_site.conf
httpd_ssl=true
httpd_ssl_cert=/etc/pki/raspberrypi/raspberry-server.csr
httpd_ssl_key=/etc/pki/raspberrypi/raspberry-server-key.pem
SSL
```

### Mettre tout ensemble, avec un fichier de substitutions 'site' de Kismet

Kismet a une fonctionnalité vraiment sympa : il peut utiliser un fichier qui remplace certains paramètres par défaut, sans avoir besoin d'éditer plusieurs fichiers. Dans ce cas, mon installation remplacera les paramètres SSL, l'interface Wi-Fi et l'emplacement du journal. Il est donc temps de mettre à jour notre fichier /etc/rc.local :

```shell
#!/bin/bash
# Kismet setup
usb_driver=rt2800usb
wlan=$(ls /sys/bus/usb/drivers/$usb_driver/*/net/)
if [ $? -eq 0 ]; then
    set -ex
    /usr/sbin/ifconfig "$wlan" down
    /usr/sbin/iwconfig "$wlan" mode monitor
    /usr/sbin/ifconfig "$wlan" up
    set +ex
    /bin/cat<<KISMETOVERR>/etc/kismet/kismet_site.conf
server_name=Nunez Barrios Kismet server
logprefix=/data/kismet
source=$wlan
httpd_ssl=true
httpd_ssl_cert=/etc/pki/raspberrypi/raspberry-server.csr
httpd_ssl_key=/etc/pki/raspberrypi/raspberry-server-key.pem
KISMETOVERR
fi
```

Enfin, il est temps de démarrer Kismet (dans mon cas en tant qu'utilisateur non-root josevnz) :

```python
# Si vous savez quelle interface est celle en mode surveillance, alors 
josevnz@raspberrypi:~$ kismet
```

Maintenant, connectons-nous pour la première fois à l'interface web (dans mon cas [http://raspberripi.home:2501](http://raspberripi.home:2501))

![Image](https://www.freecodecamp.org/news/content/images/2022/03/kismet-set-login.png align="left")

*Vous obtiendrez une invite la première fois que vous essayez de vous connecter à votre installation Kismet*

Ici, vous configurez votre utilisateur et mot de passe administrateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/kismet-main-screen.png align="left")

*Exemple des réseaux sans fil détectés*

Après un certain temps, Kismet remplira le tableau de bord principal avec la liste des réseaux sans fil et des appareils qu'il peut détecter. Vous serez surpris non seulement par le nombre d'appareils voisins qui existent, mais aussi par le nombre d'appareils que vous avez dans votre propre maison.

Dans mon exemple, les appareils sans fil autour de moi semblent assez normaux, sauf un qui n'a pas de nom :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/suspect-device-details-kismet.png align="left")

*Un appareil aux caractéristiques suspectes*

L'interface web fournit toutes sortes d'informations utiles, mais existe-t-il un moyen facile de filtrer toutes les adresses mac sur mes réseaux ?

Kismet dispose d'une API REST, il est donc temps de voir ce que nous pouvons automatiser à partir de là.

# REST-API en Python

La [documentation pour les développeurs](https://www.kismetwireless.net/docs/devel_group.html) contient des exemples sur la façon d'étendre Kismet, en particulier celui lié à l'[API REST officielle de Kismet en Python](https://github.com/kismetwireless/python-kismet-rest).

Mais il semble manquer une fonctionnalité pour utiliser des clés API, au lieu de l'utilisateur/mot de passe. Et l'interaction avec les points de terminaison ne semble pas compliquée, donc j'écrirai mon propre wrapper (moins riche en fonctionnalités).

Vous pouvez télécharger et installer le code pour une petite application que j'ai écrite ([kismet\_home](https://github.com/josevnz/kismet_home) pour illustrer comment travailler avec Kismet (contient également une copie de ce tutoriel) comme ceci :

```shell
python3 -m venv ~/virtualenv/kismet_home
. ~/virtualenv/kismet_home/bin/activate
python -m pip install --upgrade pip
git clone git@github.com:josevnz/kismet_home.git
python setup.py bdist_wheel
pip install kismet_home-0.0.1-py3-none-any.whl
```

Ensuite, exécutez les tests unitaires/les tests d'intégration et même le scanner de vulnérabilités tiers :

```shell
. ~/virtualenv/kismet_home/bin/activate
# Unit/ integration tests
python -m unittest test/unit_test_config.py
python -m unittest /home/josevnz/kismet_home/test/test_integration_kismet.py
# Third party vulnerability scanner
pip-audit  --requirement requirements.txt
```

Vous trouverez plus de détails dans les fichiers [README.md](https://github.com/josevnz/kismet_home/blob/main/README.md) et [DEVELOPER.md](https://github.com/josevnz/kismet_home/blob/main/DEVELOPER.md).

Passons maintenant au code.

### Comment interagir avec Kismet en utilisant Python

Tout d'abord, j'écrirai un client HTTP générique que je peux utiliser pour interroger ou envoyer des commandes à Kismet, c'est la classe *KismetWorker* :

```python
import json
from datetime import datetime
from typing import Any, Dict, Set, List, Union
import requests


class KismetBase:

    def __init__(self, *, api_key: str, url: str):
        """
        Constructeur paramétrique
        :param api_key: La clé API générée par Kismet
        :param url: URL où le serveur Kismet s'exécute
        """
        self.api_key = api_key
        if url[-1] != '/':
            self.url = f"{url}/"
        else:
            self.url = url
        self.cookies = {'KISMET': self.api_key}

    def __str__(self):
        return f"url={self.url}, api_key=XXX"

class KismetWorker(KismetBase):

    def check_session(self) -> None:
        """
        Confirmer si la session est valide pour une clé API donnée
        :return: None, lève une exception si la session est invalide
        """
        endpoint = f"{self.url}session/check_session"
        r = requests.get(endpoint, cookies=self.cookies)
        r.raise_for_status()

    def check_system_status(self) -> Dict[str, Any]:
        """
        Statut global du serveur Kismet
        :return: Dictionnaire imbriqué décrivant différents aspects du système Kismet
        """
        endpoint = f"{self.url}system/status.json"
        r = requests.get(endpoint, cookies=self.cookies)
        r.raise_for_status()
        return json.loads(r.text)

    def get_all_alerts(self) -> Any:
        """
        Vous pouvez obtenir une description de la configuration du système d'alertes comme montré ici : /alerts/definitions.prettyjson
        Cette méthode retourne les N dernières alertes enregistrées par le système. La gravité et la signification de l'alerte sont expliquées
        ici : https://www.kismetwireless.net/docs/devel/webui_rest/alerts/
        :return:
        """
        endpoint = f"{self.url}alerts/all_alerts.json"
        r = requests.get(endpoint, cookies=self.cookies)
        r.raise_for_status()
        return json.loads(r.text)

    def get_alert_by_hash(self, identifier: str) -> Dict[str, Any]:
        """
        Obtenir les détails d'une seule alerte par son identifiant (hash)
        :return:
        """
        parsed = int(identifier)
        if parsed < 0:
            raise ValueError(f"ID invalide fourni : {identifier}")
        endpoint = f"{self.url}alerts/by-id/{identifier}/alert.json"
        r = requests.get(endpoint, cookies=self.cookies)
        r.raise_for_status()
        return json.loads(r.text)

    def get_alert_definitions(self) -> Dict[Union[str, int], Any]:
        """
        Obtenir les types d'alertes définis
        :return:
        """
        endpoint = f"{self.url}alerts/definitions.json"
        r = requests.get(endpoint, cookies=self.cookies)
        r.raise_for_status()
        return json.loads(r.text)
```

La manière dont l'API Kismet fonctionne est que vous faites de la clé API une partie de la requête, ou vous la définissez dans le cookie KISMET. J'ai choisi de remplir le cookie.

KismetWorker implémente les méthodes suivantes :

* **check\_session** : Vérifie si votre clé API est valide. Si ce n'est pas le cas, elle lèvera une exception.
  
* **check\_system\_status** : Valide si l'administrateur (vous probablement) a défini un administrateur pour le serveur Kismet. Si ce n'est pas le cas, alors toutes les requêtes API échoueront.
  
* **get\_all\_alerts** : Obtient toutes les alertes disponibles (le cas échéant) de votre serveur Kismet.
  
* **get\_alert\_by\_hash** : Si vous connaissez l'identifiant (hash) d'une alerte, vous pouvez récupérer les détails de cet événement uniquement.
  
* **get\_alert\_definitions** : Obtient toutes les définitions d'alertes. Kismet supporte une large gamme d'alertes et un utilisateur sera définitivement intéressé de découvrir quels types d'alertes ils sont.
  

Vous pouvez voir [tout le code d'intégration](https://github.com/josevnz/kismet_home/blob/main/test/test_integration_kismet.py) ici pour voir comment les méthodes fonctionnent en action.

J'ai également écrit une classe qui nécessite des privilèges d'administrateur. Je l'utilise pour définir un type d'alerte personnalisé et pour envoyer des alertes en utilisant ce type à Kismet, dans le cadre des tests d'intégration. Pour l'instant, je n'ai pas beaucoup d'utilité à envoyer des alertes personnalisées à Kismet dans la vie réelle, mais cela pourrait changer à l'avenir, donc voici le code :

```python
class KismetAdmin(KismetBase):

    def define_alert(
            self,
            *,
            name: str,
            description: str,
            throttle: str = '10/min',
            burst: str = "1/sec",
            severity: int = 5,
            aclass: str = 'SYSTEM'

    ):
        """
        Définir un nouveau type d'alerte pour Kismet
        :param aclass: Classe d'alerte
        :param severity: Gravité de l'alerte
        :param throttle: Limite optionnelle
        :param name: Nom de la nouvelle alerte
        :param description: Que signifie ceci
        :param burst: Rafale optionnelle
        :return:
        """
        endpoint = f"{self.url}alerts/definitions/define_alert.cmd"
        command = {
            'name': name,
            'description': description,
            'throttle': throttle,
            'burst': burst,
            'severity': severity,
            'class': aclass
        }
        r = requests.post(endpoint, json=command, cookies=self.cookies)
        r.raise_for_status()

    def raise_alert(
            self,
            *,
            name: str,
            message: str
    ) -> None:
        """
        Envoyer une alerte à Kismet
        :param name: Un nom ou un identifiant bien défini pour l'alerte. DOIT exister
        :param message: Message à envoyer
        :return: None. Lèvera une erreur si l'alerte n'a pas pu être envoyée
        """
        endpoint = f"{self.url}alerts/raise_alerts.cmd"
        command = {
            'name': name,
            'text': message
        }
        r = requests.post(endpoint, json=command, cookies=self.cookies)
        r.raise_for_status()
```

Obtenir les données n'est qu'une partie de l'histoire. Nous devons les normaliser, afin qu'elles puissent être utilisées par les scripts finaux.

### Comment normaliser les données brutes de Kismet

Kismet contient beaucoup de détails sur les alertes, mais nous n'avons pas besoin de montrer à l'utilisateur ces détails (pensez à la belle vue que vous obtenez avec l'application web). Au lieu de cela, nous effectuons quelques transformations en utilisant la classe suivante avec des méthodes statiques :

* **parse\_alert\_definitions** : Retourne un rapport simplifié de toutes les définitions d'alertes
  
* **process\_alerts** : Change les alertes numériques pour des types plus descriptifs et retourne également des dictionnaires pour les types et la gravité de ces alertes.
  
* **pretty\_timestamp** : Convertit le timestamp numérique en quelque chose que nous pouvons utiliser pour les comparaisons et l'affichage
  

Le code pour la classe d'assistance *KismetResultsParser* :

```python
class KismetResultsParser:
    SEVERITY = {
        0: {
            'name': 'INFO',
            'description': 'Alertes informatives, telles que les erreurs de source de données, les changements d'état de Kismet, etc.'
        },
        5: {
            'name': 'LOW',
            'description': 'Événements à faible risque tels que les empreintes de sondage'
        },
        10: {
            'name': 'MEDIUM',
            'description': 'Événements à risque moyen tels que les tentatives de déni de service'
        },
        15: {
            'name': 'HIGH',
            'description': 'Événements à haut risque tels que les appareils surveillés avec empreintes, les attaques par déni de service, '
                           'et similaires '
        },
        20: {
            'name': 'CRITICAL',
            'description': 'Erreurs critiques telles que les exploits connus avec empreintes'
        }
    }

    TYPES = {
        'DENIAL': 'Possible tentative de déni de service',
        'EXPLOIT': 'Tentative d'exploitation connue avec empreinte contre une vulnérabilité',
        'OTHER': 'Catégorie générale pour les alertes qui ne correspondent à aucune catégorie existante',
        'PROBE': 'Sonde par des outils connus',
        'SPOOF': 'Tentative de contrefaçon d'un appareil existant',
        'SYSTEM': 'Événements système, tels que les changements de journal, les erreurs de source de données, etc.'
    }

    @staticmethod
    def parse_alert_definitions(
            *,
            alert_definitions: List[Dict[str, str]],
            keys_of_interest: Set[str] = None
    ) -> List[Dict[str, str]]:
        """
        Supprime les clés indésirables du dump complet des définitions d'alertes, pour faciliter la lecture à l'écran
        :param alert_definitions: Définitions d'alertes Kismet originales
        :param keys_of_interest: Clés Kismet d'intérêt
        :return: Liste de dictionnaires avec des clés réduites, description, gravité et en-tête pour une lecture facile
        """
        if keys_of_interest is None:
            keys_of_interest = {
                'kismet.alert.definition.class',
                'kismet.alert.definition.description',
                'kismet.alert.definition.severity',
                'kismet.alert.definition.header'
            }
        parsed_alerts: List[Dict[str, str]] = []
        for definition in alert_definitions:
            new_definition = {}
            for def_key in definition:
                if def_key in keys_of_interest:
                    new_key = def_key.split('.')[-1]
                    new_definition[new_key] = definition[def_key]
            parsed_alerts.append(new_definition)
        return parsed_alerts

    @staticmethod
    def process_alerts(
            *,
            alerts: List[Dict[str, Union[str, int]]],

    ) -> Any:
        """
        Supprime les champs indésirables des détails des alertes, retourne également des données supplémentaires pour la gravité et les types d'alertes
        :param alerts:
        :return:
        """
        processed_alerts = []
        found_types = {}
        found_severities = {}
        for alert in alerts:
            severity = alert['kismet.alert.severity']
            severity_name = KismetResultsParser.SEVERITY[severity]['name']
            severity_desc = KismetResultsParser.SEVERITY[severity]['description']
            found_severities[severity_name] = severity_desc
            text = alert['kismet.alert.text']
            aclass = alert['kismet.alert.class']
            found_types[aclass] = KismetResultsParser.TYPES[aclass]
            processed_alert = {
                'text': text,
                'class': aclass,
                'severity': severity_name,
                'hash': alert['kismet.alert.hash'],
                'dest_mac': alert['kismet.alert.dest_mac'],
                'source_mac': alert['kismet.alert.source_mac'],
                'timestamp': alert['kismet.alert.timestamp']
            }
            processed_alerts.append(processed_alert)
        return processed_alerts, found_severities, found_types

    @staticmethod
    def pretty_timestamp(timestamp: float) -> datetime:
        """
        Convertit un timestamp Kismet (TIMESTAMP.UTIMESTAMP) en une chaîne de timestamp lisible
        :param timestamp:
        :return:
        """
        return datetime.fromtimestamp(timestamp)
```

Si vous exécutez les tests d'intégration avec le rôle d'administrateur activé, vous verrez qu'une ou plusieurs (selon le nombre de fois où vous avez exécuté le test) alertes ont été ajoutées à l'interface utilisateur Web :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/kismet_generated_alerts.png align="left")

*Ces alertes ont été générées en utilisant le client Python et l'API REST*

Pour rappel, vous pouvez voir comment cela est utilisé en regardant le code [ici](https://github.com/josevnz/kismet_home/blob/main/test/test_integration_kismet.py). Voici un exemple d'exécution de tous les tests d'intégration contre mon installation (celui-ci sans publier d'alertes, donc certains tests sont ignorés) :

```shell
(kismet_home) [josevnz@dmaf5 kismet_home]$ python -m unittest /home/josevnz/kismet_home/test/test_integration_kismet.py 
[09:13:05] DEBUG    Starting new HTTP connection (1): raspberrypi.home:2501                                                                                                                                                        connectionpool.py:228
           DEBUG    http://raspberrypi.home:2501 "GET /session/check_session HTTP/1.1" 200 None                                                                                                                                    connectionpool.py:456
.           DEBUG    Starting new HTTP connection (1): raspberrypi.home:2501                                                                                                                                                        connectionpool.py:228
           DEBUG    http://raspberrypi.home:2501 "GET /system/status.json HTTP/1.1" 200 None                                                                                                                                       connectionpool.py:456
.           DEBUG    Starting new HTTP connection (1): raspberrypi.home:2501                                                                                                                                                        connectionpool.py:228
           DEBUG    http://raspberrypi.home:2501 "GET /alerts/definitions.json HTTP/1.1" 200 None                                                                                                                                  connectionpool.py:456
.[09:13:05] 'ADMIN_SESSION_API' environment variable not defined. Skipping this test                                                                                                                                       test_integration_kismet.py:105
....
----------------------------------------------------------------------
Ran 7 tests in 0.053s

OK
```

### Où stockons-nous notre clé API et autres détails de configuration ?

Les détails comme ceux-ci ne seront pas codés en dur dans les scripts, mais résideront plutôt dans un fichier de configuration externe :

```shell
(kismet_home) [josevnz@dmaf5 kismet_home]$ cat ~/.config/kodegeek/kismet_home/config.ini 
[server]
url = http://raspberrypi.home:2501
api_key = E41CAD466552810392D538FF8D43E2C5
```

Les classes suivantes gèrent tous les détails d'accès (en utilisant une classe Reader et une classe Writer pour chaque type d'opération) :

```python
"""
Gestion simple de la configuration pour les paramètres de kismet_home
"""
import os.path
from configparser import ConfigParser
from pathlib import Path
from typing import Dict

from kismet_home import CONSOLE

DEFAULT_INI = os.path.expanduser('~/.config/kodegeek/kismet_home/config.ini')
VALID_KEYS = {'api_key', 'url'}


class Reader:

    def __init__(self, config_file: str = DEFAULT_INI):
        """
        Constructeur
        :param config_file: Remplacement optionnel du fichier de configuration ini
        """
        self.config = ConfigParser()
        if not self.config.read(config_file):
            raise ValueError(f"Impossible de lire {config_file}")

    def get_api_key(self):
        """
        Récupère la clé API utilisée pour se connecter à Kismet
        :return:
        """
        return self.config.get('server', 'api_key')

    def get_url(self):
        """
        Récupère l'URL du serveur Kismet
        :return:
        """
        return self.config.get('server', 'url')


class Writer:

    def __init__(
            self,
            *,
            server_keys: Dict[str, str]
    ):
        if not server_keys:
            raise ValueError("La configuration est incomplète, abandon !")
        self.config = ConfigParser()
        self.config.add_section('server')
        valid_keys_cnt = 0
        for key in server_keys:
            value = server_keys[key]
            if key not in VALID_KEYS:
                CONSOLE.log(f"Ignorer la clé invalide : {key} = {value}")
                continue
            self.config.set('server', key, value)
            CONSOLE.log(f"Ajouté : server : {key} = {value}")
        for valid_key in VALID_KEYS:
            if not self.config.get('server', valid_key):
                raise ValueError(f"Clé requise manquante : {valid_key}")

    def save(
            self,
            *,
            config_file: str = DEFAULT_INI
    ):
        basedir = Path(config_file).parent
        basedir.mkdir(exist_ok=True, parents=True)
        with open(config_file, 'w') as config:
            self.config.write(config, space_around_delimiters=True)
        CONSOLE.log(f"Fichier de configuration {config_file} écrit")
```

La première fois que vous configurez votre installation kismet\_home, vous pouvez créer les fichiers de configuration comme ceci :

```shell
[josevnz@dmaf5 kismet_home]$ python3 -m venv ~/virtualenv/kismet_home
[josevnz@dmaf5 kismet_home]$ . ~/virtualenv/kismet_home/bin/activate
(kismet_home) [josevnz@dmaf5 kismet_home]$ python -m pip install --upgrade pip
(kismet_home) [josevnz@dmaf5 kismet_home]$ git clone git@github.com:josevnz/kismet_home.git
(kismet_home) [josevnz@dmaf5 kismet_home]$ python setup.py bdist_wheel
(kismet_home) [josevnz@dmaf5 kismet_home]$ pip install kismet_home-0.0.1-py3-none-any.whl

(kismet_home) [josevnz@dmaf5 kismet_home]$ kismet_home_config.py 
Veuillez entrer l'URL de votre serveur Kismet : http://raspberrypi.home:2501/
Veuillez entrer votre clé API : E41CAD466552810392D538FF8D43E2C5
[13:02:35] Ajouté : server : url = http://raspberrypi.home:2501/                                                                                 config.py:44
           Ajouté : server : api_key = E41CAD466552810392D538FF8D43E2C5                                                                          config.py:44
           Fichier de configuration /home/josevnz/.config/kodegeek/kismet_home/config.ini écrit
```

Veuillez noter l'utilisation de l'environnement virtuel ici. Cela nous permettra de garder les bibliothèques de l'application auto-contenues.

## Mettre tout ensemble : Comment écrire notre CLI pour kismet\_home

Le script *kismet\_home\_alerts.py* prendra en charge deux modes :

* Afficher les définitions d'alertes
  
* Afficher toutes les alertes
  

De plus, il permettra de filtrer les alertes en fonction du niveau (INFO, MEDIUM, HIGH, ...).

Afficher toutes les définitions, filtrées par CRITICAL :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/alert_definitions_filtered_by_level.png align="left")

*Vous pouvez voir ici les définitions d'alertes filtrées par niveau*

Ou afficher toutes les alertes reçues jusqu'à présent, avec des adresses MAC anonymes (parfait pour les captures d'écran comme celle-ci) :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/kismet_home_alerts.png align="left")

*Alertes pour mon réseau local, avec des adresses MAC anonymes et filtrées*

Comment pouvez-vous générer ces tableaux avec facilité ? Il existe une classe dédiée pour l'interface utilisateur en texte (TUI) :

```python
from typing import List, Dict, Any

from rich.layout import Layout
from rich.table import Table

from kismet_home.kismet import KismetResultsParser


def create_alert_definition_table(
        *,
        alert_definitions: List[Dict[str, Any]],
        level_filter: str = 0
) -> Table:
    """
    Crée un tableau montrant les définitions d'alertes
    :param alert_definitions: Définitions d'alertes de Kismet
    :param level_filter: L'utilisateur peut remplacer le niveau des alertes affichées. Par défaut, c'est 0 (INFO)
    :return: Un tableau avec les définitions d'alertes
    """
    definition_table = Table(title="Définitions d'alertes")
    definition_table.add_column("Gravité", justify="right", style="cyan", no_wrap=True)
    definition_table.add_column("Description", style="magenta")
    definition_table.add_column("En-tête", justify="right", style="yellow")
    definition_table.add_column("Classe", justify="right", style="green")
    filter_level = KismetResultsParser.get_level_for_security(level_filter)
    filtered_definitions = 0
    for definition in alert_definitions:
        int_severity: int = definition['severity']
        if int_severity < filter_level:
            continue
        severity = KismetResultsParser.SEVERITY[int_severity]['name']
        if 0 <= int_severity < 5:
            severity = f"[bold blue]{severity}[/ bold blue]"
        if 5 <= int_severity < 10:
            severity = f"[bold yellow]{severity}[/ bold yellow]"
        if 10 <= int_severity < 15:
            severity = f"[bold orange]{severity}[/ bold orange]"
        else:
            severity = f"[bold red]{severity}[/ bold red]"
        filtered_definitions += 1
        definition_table.add_row(
            severity,
            definition['description'],
            definition['header'],
            definition['class']
        )
    definition_table.caption = f"Total des définitions : {filtered_definitions}"
    return definition_table


def create_alert_layout(
        *,
        alerts: List[Dict[str, Any]],
        level_filter: str = 0,
        anonymize: bool = False,
        severities: Dict[str, str]
):
    """
    :param severities:
    :param alerts:
    :param level_filter:
    :param anonymize:
    :return:
    """
    alerts_table = Table(title="Définitions d'alertes")
    alerts_table.add_column("Timestamp", no_wrap=True)
    alerts_table.add_column("Gravité", justify="right", style="cyan", no_wrap=True)
    alerts_table.add_column("Texte", style="magenta")
    alerts_table.add_column("MAC Source", justify="right", style="yellow", no_wrap=True)
    alerts_table.add_column("MAC Destination", justify="right", style="yellow", no_wrap=True)
    alerts_table.add_column("Classe", justify="right", style="green", no_wrap=True)
    filter_level = KismetResultsParser.get_level_for_security(level_filter)

    filtered_definitions = 0
    for alert in alerts:
        int_severity: int = KismetResultsParser.get_level_for_security(alert['severity'])
        if int_severity < filter_level:
            continue
        severity = KismetResultsParser.SEVERITY[int_severity]['name']
        if 0 <= int_severity < 5:
            severity = f"[bold blue]{severity}[/ bold blue]"
        if 5 <= int_severity < 10:
            severity = f"[bold yellow]{severity}[/ bold yellow]"
        if 10 <= int_severity < 15:
            severity = f"[bold orange]{severity}[/ bold orange]"
        else:
            severity = f"[bold red]{severity}[/ bold red]"
        filtered_definitions += 1
        if anonymize:
            s_mac = KismetResultsParser.anonymize_mac(alert['source_mac'])
            d_mac = KismetResultsParser.anonymize_mac(alert['dest_mac'])
        else:
            s_mac = alert['source_mac']
            d_mac = alert['dest_mac']
        alerts_table.add_row(
            str(KismetResultsParser.pretty_timestamp(alert['timestamp'])),
            severity,
            alert['text'],
            s_mac,
            d_mac,
            alert['class']
        )
    alerts_table.caption = f"Total des alertes : {filtered_definitions}"

    severities_table = Table(title="Légende de gravité")
    severities_table.add_column("Gravité")
    severities_table.add_column("Explication")
    for severity in severities:
        explanation = f"[green]{severities[severity]}[/green]"
        severities_table.add_row(f"[yellow]{severity}[/yellow]", explanation)

    layout = Layout()
    layout.split(
        Layout(ratio=2, name="alerts"),
        Layout(name="severities"),
    )
    layout["alerts"].update(alerts_table)
    layout["severities"].update(severities_table)
    return layout, filtered_definitions
```

Et maintenant, avec tous les ingrédients prêts, nous pouvons voir à quoi ressemble le script final :

```python
#!/usr/bin/env python
"""
# kismet_home_alerts.py
# Auteur
Jose Vicente Nunez Zuleta (kodegeek.com@protonmail.com)
"""
import logging
import sys

from requests import HTTPError
import argparse

from kismet_home import CONSOLE
from kismet_home.config import Reader
from kismet_home.kismet import KismetWorker, KismetResultsParser
from kismet_home.tui import create_alert_definition_table, create_alert_layout

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(
        description="Afficher les alertes générées par votre installation locale de Kismet",
        prog=__file__
    )
    arg_parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help="Activer le mode débogage"
    )
    arg_parser.add_argument(
        '--anonymize',
        action='store_true',
        default=False,
        help="Anonymiser les adresses MAC"
    )
    arg_parser.add_argument(
        '--level',
        action='store',
        default='INFO',
        help="Activer le mode débogage"
    )
    arg_parser.add_argument(
        'mode',
        action='store',
        choices=['alert_type', 'alerts'],
        help="Mode de fonctionnement"
    )

    try:
        args = arg_parser.parse_args()
        conf_reader = Reader()
        kw = KismetWorker(
            api_key=conf_reader.get_api_key(),
            url=conf_reader.get_url()
        )
        if args.mode == 'alert_type':
            alert_definitions = KismetResultsParser.parse_alert_definitions(
                alert_definitions=kw.get_alert_definitions()
            )
            table = create_alert_definition_table(alert_definitions=alert_definitions, level_filter=args.level)
            if table.columns:
                CONSOLE.print(table)
            else:
                CONSOLE.print(f"[b]Impossible d'obtenir les définitions d'alertes ![/b]")
        elif args.mode == 'alerts':
            alerts, severities, types = KismetResultsParser.process_alerts(
                alerts=kw.get_all_alerts()
            )
            layout, found = create_alert_layout(
                alerts=alerts,
                level_filter=args.level,
                anonymize=args.anonymize,
                severities=severities
            )
            if found:
                CONSOLE.print(layout)
            else:
                CONSOLE.print(f"[b]Aucune alerte à afficher pour le niveau={args.level}[/b]")
    except (ValueError, HTTPError):
        logging.exception("Une erreur s'est produite")
        sys.exit(100)
    except KeyboardInterrupt:
        CONSOLE.log("Scan interrompu, sortie...")
    sys.exit(0)
```

Quelques points à noter :

* Ce n'est pas une application à long terme. Au lieu de cela, c'est un instantané de toutes les alertes. Si vous vouliez, par exemple, transférer ces alertes par e-mail ou vers un framework comme [grafana](https://grafana.com/), vous seriez mieux avec [Websockets](https://pypi.org/project/websockets/) et l'une des méthodes qui ne récupère que les derniers changements.
  
* La disposition est rudimentaire, et il y a beaucoup de place pour l'amélioration. Mais notre petit tui affiche des informations pertinentes sans trop de distractions
  
* Et c'était amusant à coder !
  

# Qu'avons-nous appris ?

* Comment installer Kismet et le sécuriser avec un certificat SSL auto-signé
  
* Comment écrire un simple script Bash pour configurer l'interface sans fil correcte en mode moniteur, après le redémarrage du RaspBerryPI
  
* Comment ajouter une clé API avec un accès en lecture seule pour l'utiliser à la place du schéma utilisateur/mot de passe hérité pour l'authentification et l'autorisation
  
* Comment écrire des classes en Python qui peuvent communiquer avec Kismet en utilisant son API REST
  
* Comment ajouter des tests unitaires et d'intégration au code pour s'assurer que tout fonctionne et que les nouveaux changements de code ne cassent pas la fonctionnalité existante
  

Veuillez laisser vos commentaires sur le [dépôt git](https://github.com/josevnz/kismet_home) et signaler tout bug. Mais surtout, obtenez Kismet, obtenez le code de ce tutoriel, et commencez à sécuriser votre infrastructure sans fil domestique en un rien de temps.