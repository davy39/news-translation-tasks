---
title: Comment améliorer Nmap avec Python
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-02-08T19:28:43.000Z'
originalURL: https://freecodecamp.org/news/enhance-nmap-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/home_nmap.png
tags:
- name: computer networking
  slug: computer-networking
- name: cybersecurity
  slug: cybersecurity
- name: nmap
  slug: nmap
- name: Python
  slug: python
seo_title: Comment améliorer Nmap avec Python
seo_desc: 'Very few pieces of Open Source software generate so much hype as Nmap.
  It is one of those tools that packs in so many useful features that it can help
  you make your systems more secure by just running it with a few flags.

  Nmap ("Network Mapper") is a...'
---

Très peu de logiciels Open Source génèrent [autant de buzz](https://nmap.org/movies/) que [Nmap](https://nmap.org/). C'est l'un de ces outils qui regorge de fonctionnalités utiles qu'il peut aider à rendre vos systèmes plus sécurisés simplement en l'exécutant avec quelques flags.

Nmap ("Network Mapper") est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité.

De nombreux administrateurs système et réseau le trouvent également utile pour des tâches telles que l'inventaire réseau, la gestion des plannings de mise à jour des services et la surveillance du temps de fonctionnement des hôtes ou des services.

Vous pouvez également l'utiliser pour contourner les protections faibles, trouver des services cachés ou mal configurés, ou simplement pour mieux comprendre comment fonctionnent les réseaux.

## Table des matières :

* [Ce que vous apprendrez dans cet article](#heading-ce-que-vous-apprendrez-dans-cet-article)
    
* [Nmap 101 : Identifier tous les services publics de notre réseau](#heading-nmap-101-identifier-tous-les-services-publics-de-notre-reseau)
    
* [Comment écrire un scanner réseau 'bouton facile' qui utilise Nmap](#heading-comment-ecrire-un-scanner-reseau-bouton-facile-qui-utilise-nmap)
    
* [Comment faire d'un scanner de réseau domestique un service Web](#heading-comment-faire-dun-scanner-de-reseau-domestique-un-service-web)
    
* [Qu'avons-nous appris ?](#heading-quavons-nous-appris)
    

## Ce que vous apprendrez dans cet article

Nous aborderons les points suivants pour illustrer comment vous pouvez améliorer Nmap avec Python :

* Écrire un petit script qui peut scanner tous les hôtes du réseau local, en veillant à ce qu'il s'exécute avec les privilèges appropriés.
    
* Améliorer Nmap en corrélant les services avec les avis de sécurité.
    
* Convertir nos scripts en un service web. Ajoutera une sécurité de base (autorisation et chiffrement).
    

### Ce que vous devez savoir et faire avant de commencer

Ne vous inquiétez pas trop, car je vais vous guider à travers les étapes. Ce sera une expérience amusante, et vous aurez tout le code source pour suivre :

* Être familier avec les concepts de réseau de base comme [Classless inter-domain routing (CIDR)](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
    
* Être capable d'écrire un programme dans un langage de script comme [Python](https://www.python.org/).
    
* Le code peut être installé en utilisant un environnement virtuel. Si vous n'êtes pas familier avec un environnement virtuel, vous pouvez lire ce qui suit : [Packaging applications to install on other machines with Python](https://www.redhat.com/sysadmin/packaging-applications-python).
    

### Quels outils aurez-vous besoin pour ce tutoriel ?

Je ne couvrirai pas l'installation de ces outils, mais il existe de nombreuses documentations pour vous aider à démarrer.

* Installez tout le code de ce tutoriel en suivant les instructions expliquées dans le fichier [README document](http://README.md) principal sur mon site [official repository site](https://github.com/josevnz/home_nmap). Vous devrez [installer](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) [Git](https://git-scm.com/docs/gittutorial) pour cloner le code.
    
* Une distribution Linux. Fedora, Ubuntu, Kali, utilisez celle avec laquelle vous êtes le plus à l'aise (j'ai utilisé [Fedora](https://docs.fedoraproject.org/en-US/fedora/rawhide/install-guide/) 35.)
    
* [Interpréteur Python](https://developer.fedoraproject.org/tech/languages/python/python-installation.html). Une bonne distribution Linux viendra avec Python préinstallé ou au moins facilitera son installation. J'ai utilisé Python 3.9 ici.
    

Dernières *deux choses* :

* J'ai sauté **certaines** imports dans les extraits de code car ils n'améliorent pas les démonstrations de code. Pour obtenir le code le plus précis, veuillez cloner le dépôt Git public pour ce tutoriel et ouvrir le code source.
    
* *Exécutez ces exemples uniquement contre votre réseau local*. Vous pouvez être curieux, vous amuser et apprendre de nouvelles choses sur les outils existants sans affecter les autres.
    

Le piratage, c'est apprendre !

# Nmap 101 : Identifier tous les services publics de notre réseau

### Mot de prudence : Le dicton 'mieux vaut demander pardon que permission' ne s'applique pas ici

Nous ne nous soucions pas d'être 'furtifs' ou de déclencher un [Intrusion Detection System (IDS)](https://en.wikipedia.org/wiki/Intrusion_detection_system) en raison de notre activité de scan de ports. Un IDS recherche généralement des schémas réseau anormaux et si une machine ouvre et ferme des ports en succession rapide sur de nombreux hôtes, cela serait considéré comme une attaque par scan de ports. Encore une fois, ce ne sera pas le cas dans notre réseau domestique car, eh bien, nous savons que c'est nous qui exécutons un tel scan.

Pour la même raison, vous ne devez pas lancer un scan de ports sur un réseau que vous ne possédez pas, car Nmap n'est pas 100 % furtif (vous pouvez toujours jouer avec la randomisation de la fréquence, le type de poignée de main TCP, le nombre de ports ouverts, utiliser un proxy, etc., et pourtant vous manquerez probablement quelque chose).

Alors, mieux vaut se comporter, d'accord ? :-)

### Que devons-nous faire pour exécuter Nmap et l'identification des empreintes OS ?

L'objectif ici est de voir quels services sont en cours d'exécution dans notre réseau en utilisant une interface de ligne de commande (CLI) script.

Nmap nécessite des privilèges élevés pour effectuer l'identification des empreintes OS et les scans utilisant des sockets bruts. Vous devrez exécuter les commandes en tant que root ou [su "do" (SUDO)](https://www.sudo.ws/) pour élever vos permissions. Une règle SUDO pour faire cela est similaire à ceci (fichier /etc/sudoers) :

```shell
## Même chose sans mot de passe
%wheel	ALL=(ALL)	NOPASSWD: ALL
```

Cela signifie que toute personne dans le groupe unix 'wheel' peut exécuter des commandes en tant que root :

```shell
(2600) [josevnz@dmaf5 2600]$ grep wheel /etc/group
wheel:x:10:josevnz,services

# Pour confirmer que nous pouvons exécuter des commandes en tant que root
(2600) [josevnz@dmaf5 2600]$ sudo -l
Matching Defaults entries for josevnz on dmaf5:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin, env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
    env_keep+="MAIL QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES", env_keep+="LC_MONETARY
    LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE", env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/var/lib/snapd/snap/bin

User josevnz may run the following commands on dmaf5:
    (ALL) NOPASSWD: ALL
```

Ensuite, nous allons faire un scan rapide de notre réseau local (dans cet exemple, c'est 192.168.1.0/24). J'ai utilisé le flag -v (verbose) pour obtenir un retour de progression pendant le scan de tous les ports tout en faisant également l'identification des empreintes OS (-O).

J'ai sauvegardé l'exécution de Nmap dans un fichier XML (-oX), que Nmap peut utiliser pour reprendre l'exécution si elle est interrompue (--resume) :

```shell
# Au cas où le scan est interrompu : nmap --resume $HOME/home_scan.xml
[josevnz@dmaf5 docs]$ sudo nmap -v -n -p- -sT -sV -O --osscan-limit --max-os-tries 1 -oX $HOME/home_scan.xml 192.168.1.0/24
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-30 16:35 EST
NSE: Loaded 45 scripts for scanning.
Initiating ARP Ping Scan at 16:35
Scanning 254 hosts [1 port/host]
...
# Après un certain temps et plusieurs tasses de café vénézuélien...
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=265 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 192.168.1.20
Host is up (0.0097s latency).
Not shown: 65530 closed ports
PORT      STATE    SERVICE      VERSION
36184/tcp filtered unknown
37309/tcp filtered unknown
49323/tcp open     unknown
49376/tcp filtered unknown
62078/tcp open     iphone-sync?
MAC Address: 9E:90:75:3A:D7:XX (Unknown)
...
```

Le fichier résultant au [format XML](https://nmap.org/book/output-formats-xml-output.html) est très verbeux :

```xml
<host starttime="1640901327" endtime="1640902555"><status state="up" reason="arp-response" reason_ttl="0"/>
<address addr="192.168.1.1" addrtype="ipv4"/>
<address addr="38:5B:5E:1D:52:99" addrtype="mac"/>
<hostnames>
</hostnames>
<ports><extraports state="closed" count="65523">
<extrareasons reason="conn-refused" count="65523"/>
</extraports>
<port protocol="tcp" portid="139"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="netbios-ssn" product="Samba smbd" version="3.X - 4.X" extrainfo="workgroup: ZZZ" method="probed" conf="10"><cpe>cpe:/a:samba:samba</cpe></service></port>
    ...
```

Il est temps de faire un peu de codage. L'analyse de données dans de nombreux formats est l'une des forces de Python. Les données sont extraites et normalisées pour tous les ports qui ne sont pas 'fermés' en utilisant [lxml](https://github.com/lxml/lxml) :

```python
class OutputParser:
    """
    Analyser la sortie XML brute de Nmap
    """

    @staticmethod
    def parse_nmap_xml(xml: str) -> (str, Any):
        """
        Analyser le XML et retourner les détails des ports scannés
        @param xml:
        @return: tuple des arguments de nmap, détails des ports
        """
        parsed_data = []
        root = ElementTree.fromstring(xml)
        nmap_args = root.attrib['args']
        for host in root.findall('host'):
            for address in host.findall('address'):
                curr_address = address.attrib['addr']
                data = {
                    'address': curr_address,
                    'ports': []
                }
                states = host.findall('ports/port/state')
                ports = host.findall('ports/port')
                for i in range(len(ports)):
                    if states[i].attrib['state'] == 'closed':
                        continue  # Ignorer les ports fermés
                    port_id = ports[i].attrib['portid']
                    protocol = ports[i].attrib['protocol']
                    services = ports[i].findall('service')
                    cpe_list = []
                    service_name = ""
                    service_product = ""
                    service_version = ""
                    for service in services:
                        for key in ['name', 'product', 'version']:
                            if key in service.attrib:
                                if key == 'name':
                                    service_name = service.attrib['name']
                                elif key == 'product':
                                    service_product = service.attrib['product']
                                elif key == 'version':
                                    service_version = service.attrib['version']
                        cpes = service.findall('cpe')
                        for cpe in cpes:
                            cpe_list.append(cpe.text)
                        data['ports'].append({
                            'port_id': port_id,
                            'protocol': protocol,
                            'service_name': service_name,
                            'service_product': service_product,
                            'service_version': service_version,
                            'cpes': cpe_list
                        })
                        parsed_data.append(data)
        return nmap_args, parsed_data
```

Une fois les données collectées, nous pouvons créer un beau tableau dans le terminal avec l'aide de [Rich](https://github.com/Textualize/rich).

Le tableau a les colonnes suivantes :

* Adresse Internet Protocol (IP)
    
* Protocole : Dans ce script, il sera toujours Transfer Control Protocol (TCP)
    
* ID de port : Le numéro de port où le service s'exécute
    
* Service : Un service réseau comme Secure Shell (SSH)
    
* Common Platform Enumeration ([CPE](https://nvd.nist.gov/products/cpe)) : C'est un schéma de nommage structuré pour les systèmes de technologie de l'information, les logiciels et les packages.
    
* Avis : Toute vulnérabilité liée au CPE identifié par Nmap. Il faudra les corrélater nous-mêmes.
    

```python
def create_scan_table(*, cli: str) -> Table:
    """
    Créer un tableau pour l'interface CLI
    :param cli: Arguments complets de Nmap utilisés lors de l'exécution
    :return: Tableau squelette, sans données
    """
    nmap_table = Table(title=f"Informations d'exécution de NMAP : {cli}")
    nmap_table.add_column("IP", justify="right", style="cyan", no_wrap=True)
    nmap_table.add_column("Protocole", justify="right", style="cyan", no_wrap=True)
    nmap_table.add_column("ID de port", justify="right", style="magenta", no_wrap=True)
    nmap_table.add_column("Service", justify="right", style="green")
    nmap_table.add_column("CPE", justify="right", style="blue")
    nmap_table.add_column("Avis", justify="right", style="blue")
    return nmap_table
...
def fill_simple_table(*, exec_data: str, parsed_xml: Dict[Any, Any]) -> Table:
    """
    Méthode de commodité pour créer un tableau d'interface utilisateur simple avec la sortie XML de Nmap
    :param exec_data: Arguments et options utilisés pour exécuter Nmap
    :param parsed_xml: Données Nmap sous forme de dictionnaire
    :return: Tableau rempli
    """
    nmap_table = create_scan_table(cli=exec_data)
    for row_data in parsed_xml:
        address = row_data['address']
        ports = row_data['ports']
        for port_data in ports:
            nmap_table.add_row(
                address,
                port_data['protocol'],
                port_data['port_id'],
                f"{port_data['service_name']} {port_data['service_product']} {port_data['service_version']}",
                "\n".join(port_data['cpes']),
                ""
            )
    return nmap_table
```

Le script résultant utilise le code ci-dessus pour donner à l'utilisateur une vue d'ensemble complète du scan du réseau local :

```python
#!/usr/bin/env python
import sys
from rich.console import Console
from home_nmap.query import OutputParser
from home_nmap.ui import fill_simple_table

if __name__ == "__main__":
    console = Console()
    for nmap_xml in sys.argv[1:]:
        with open(nmap_xml, 'r') as xml:
            xml_data = xml.read()
            rundata, parsed = OutputParser.parse_nmap_xml(xml_data)
            nmap_table = fill_simple_table(exec_data=rundata, parsed_xml=parsed)
            console.print(nmap_table)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/nmap_scan_rpt_noadvisories.png align="left")

*Scan du réseau local. La colonne Avis est vide*

Si vous remarquez, la colonne 'Avis' est laissée complètement vide. Nous utiliserons le [moteur de recherche du site de cybersécurité NIST](https://www.nist.gov/cybersecurity) pour remplir les avis manquants, en contournant les CPE qui ont des *informations de version* pour éviter les faux positifs.

Nous utilisons [requests](https://github.com/psf/requests) pour nous aider avec la communication HTTP :

```python
from dataclasses import dataclass
import requests
IGNORED_CPES = {"cpe:/o:linux:linux_kernel"}
from cpe import CPE
from lxml import html

@dataclass
class NIDS:
    summary: str
    link: str
    score: str

class NDISHtml:

    def __init__(self):
        """
        Certains CPE retournent trop de faux positifs,
        donc ils sont ignorés dès le départ
        """
        self.raw_html = None
        self.parsed_results = []
        self.url = "https://nvd.nist.gov/vuln/search/results"
        self.ignored_cpes = IGNORED_CPES

    def get(self, cpe: str) -> str:
        """
        Exécuter une recherche CPE sur le site NDIS. Si le CPE n'a pas de version, sauter la recherche
        car elle retournera trop de faux positifs
        @param cpe: Identifiant CPE provenant de Nmap, comme cpe:/a:openbsd:openssh:8.0
        @return:
        """
        params = {
            'form_type': 'Basic',
            'results_type': 'overview',
            'search_type': 'all',
            'isCpeNameSearch': 'false',
            'query': cpe
        }
        if cpe in self.ignored_cpes:
            return ""
        valid_cpe = CPE(cpe)
        if not valid_cpe.get_version()[0]:
            return ""
        response = requests.get(
            url=self.url,
            params=params
        )
        response.raise_for_status()
        return response.text

    def parse(self, html_data: str) -> list[NIDS]:
        """
        Analyser la recherche web NDIS. Non conscient qu'ils offrent une API REST qui ne nécessite pas d'analyse.
        Il est supposé que cette méthode n'est jamais appelée directement par les utilisateurs finaux, donc aucune vérification supplémentaire n'est effectuée sur le
        contenu du fichier HTML.
        @param html_data: HTML brut utilisé pour le scrapping
        @return: Liste de NDIS, si disponible
        """
        self.parsed_results = []
        if html_data:
            ndis_html = html.fromstring(html_data)
            # Correspondance 1:1 entre 3 éléments, utiliser un tableau parallèle
            summary = ndis_html.xpath("//*[contains(@data-testid, 'vuln-summary')]")
            cve = ndis_html.xpath("//*[contains(@data-testid, 'vuln-detail-link')]")
            score = ndis_html.xpath("//*[contains(@data-testid, 'vuln-cvss2-link')]")
            for i in range(len(summary)):
                ndis = NIDS(
                    summary=summary[i].text,
                    link="https://nvd.nist.gov/vuln/detail/" + cve[i].text,
                    score=score[i].text
                )
                self.parsed_results.append(ndis)
        return self.parsed_results
```

Ensuite, nous corrélons les CPE de Nmap dans les résultats avec chacun des avis, le cas échéant :

```python
from typing import Any
from dataclasses import dataclass
@dataclass
class NIDS:
    summary: str
    link: str
    score: str
class NDISHtml:
    def correlate_nmap_with_nids(self, parsed_xml: Any) -> dict[str, list[NIDS]]:
        correlated_cpe = {}
        for row_data in parsed_xml:
            ports = row_data['ports']
            for port_data in ports:
                for cpe in port_data['cpes']:
                    raw_ndis = self.get(cpe)
                    cpes = self.parse(raw_ndis)
                    correlated_cpe[cpe] = cpes
        return correlated_cpe
```

Le nouveau tableau parle de lui-même :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/nmap_scan_rpt.png align="left")

*Résultats du scan Nmap dans un beau tableau*

Plus complet, et nous pouvons voir maintenant que quelques-uns de nos services locaux peuvent avoir une vulnérabilité !

Pouvons-nous faire mieux ? Par exemple, il serait bien de pouvoir exécuter Nmap directement depuis Python au lieu d'analyser les résultats d'une exécution, alors codons cela.

# Comment écrire un scanner réseau 'bouton facile' qui utilise Nmap

## Comment encapsuler Nmap avec Python (subprocess.run)

Nmap n'offre pas d'API formelle pour interagir avec des programmes externes. Pour cette raison, nous allons l'exécuter depuis Python et sauvegarder les résultats dans un fichier XML. Nous pouvons ensuite utiliser les données comme nous le souhaitons (voir l'appel 'subprocess.run' dans la méthode 'scan' de notre classe NmapRunner) :

```python
class NMapRunner:

    def __init__(self):
        """
        Créer un exécuteur Nmap
        """
        self.nmap_report_file = None
        found_sudo = shutil.which('sudo', mode=os.F_OK | os.X_OK)
        if not found_sudo:
            raise ValueError(f"SUDO est manquant")
        self.sudo = found_sudo
        found_nmap = shutil.which('nmap', mode=os.F_OK | os.X_OK)
        if not found_nmap:
            raise ValueError(f"NMAP est manquant")
        self.nmap = found_nmap

    def scan(
            self,
            *,
            hosts: str,
            sudo: bool = True
    ):
        command = []
        if sudo:
            command.append(self.sudo)
        command.append(self.nmap)
        command.extend(__NMAP__FLAGS__)
        command.append(hosts)
        completed = subprocess.run(
            command,
            capture_output=True,
            shell=False,
            check=True
        )
        completed.check_returncode()
        args, data = OutputParser.parse_nmap_xml(completed.stdout.decode('utf-8'))
        return args, data, completed.stderr
```

*Note de sécurité* : L'argument nommé 'shell=False' nous indique que nous ne voulons pas créer un nouveau shell lors de l'exécution de notre processus. Cela fournira une protection contre les attaques par [injection de shell](https://en.wikipedia.org/wiki/Code_injection#Shell_injection).

## Comment accélérer Nmap (rappeler tous ces flags en un seul endroit)

Votre réseau local a moins de latence que l'Internet. Il sera également plus facile de scanner les ports ouverts et d'identifier les empreintes OS car il n'y a pas de pare-feu entre vous et les hôtes.

De plus, nous ne nous soucions pas de déclencher une détection IDS, donc vous pouvez utiliser ce qui suit pour réduire le temps nécessaire pour compléter le scan des ports (Variable **NMAP\_\_FLAGS** dans le package système) :

```python
import shlex
# Convertir les args pour une utilisation correcte sur la CLI
NMAP_HOME_NETWORK_DEFAULT_FLAGS = {
    '-n': 'Ne jamais faire de résolution DNS',
    '-sS': 'Scan TCP SYN, recommandé',
    '-p-': 'Tous les ports',
    '-sV': 'Sonder les ports ouverts pour déterminer les informations de service/version',
    '-O': 'Sonde OS. Nécessite sudo/ root',
    '-T4': 'Modèle de temporisation agressif',
    '-PE': 'Activer ce comportement de requête echo. Bon pour les réseaux internes',
    '--version-intensity 5': 'Définir l\'intensité du scan de version. Par défaut est 7',
    '--disable-arp-ping': 'Pas de ping ARP ou ND',
    '--max-hostgroup 20': 'Taille du groupe d\'hôtes (lot d\'hôtes scannés simultanément)',
    '--min-parallelism 10': 'Nombre de sondes qui peuvent être en attente pour un groupe d\'hôtes',
    '--osscan-limit': 'Limiter la détection OS aux cibles prometteuses',
    '--max-os-tries 1': 'Nombre maximum de tentatives de détection OS contre une cible',
    '-oX -': 'Envoyer la sortie XML vers STDOUT, éviter de créer un fichier temporaire'
}
__NMAP__FLAGS__ = shlex.split(" ".join(NMAP_HOME_NETWORK_DEFAULT_FLAGS.keys()))
```

La documentation de Nmap suggère également que vous pouvez diviser la liste totale des hôtes sur plusieurs instances de Nmap (elle ne peut pas être supérieure au nombre de CPU dans le serveur exécutant l'outil) pour augmenter le parallélisme. Mais cela n'est pas gratuit. Vous devrez vous soucier des problèmes comme les conditions de course et la synchronisation dans les threads concurrents exécutant Nmap.

Pour l'instant, nous allons garder cela simple et laisser Nmap s'occuper de toute optimisation en fournissant les flags montrés ci-dessus.

## Comment déterminer les réseaux locaux sur la machine où Nmap s'exécute ?

Notre script Python peut également vérifier les interfaces qui sont actives, sauter les interfaces virtuelles, et sauter l'interface de boucle spéciale. Heureusement, le noyau publie toutes les informations dont nous avons besoin dans le fichier /proc/net/dev :

```shell
(2600) [josevnz@dmaf5 2600]$ cat /proc/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo: 18303833  303389    0    0    0     0          0         0 18303833  303389    0    0    0     0       0          0
enp2s0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
  eno1: 1931173135 3908073    0    1    0     0          0    407486 274206691 3289566    0    0    0     0       0          0
```

Nous pouvons l'analyser comme ceci (classe HostIface, méthode **refresh\_interfaces**) :

```python
class HostIface:    
    ...
    
    def __refresh_interfaces__(self, *, skip_loopback: bool = True, only_alive: bool = True) -> Set[str]:
        """
        Alive signifie une interface qui a montré une activité d'octet depuis que le serveur est en ligne
        Saute l'interface de boucle par défaut
        :param only_alive: Sauter les interfaces avec une activité d'octet nulle
        :param skip_loopback
        :return: Ensemble avec les noms d'interface
        """
        with open('/proc/net/dev', 'r') as dev:
            for line in dev:
                tokens = line.split()
                if tokens[0].find(":") != -1:
                    name = tokens[0].split(':')[0]
                    if re.search('virbr\\d+|docker', name):
                        continue  # Sauter les interfaces virtuelles
                    if only_alive and int(tokens[1].strip()) == 0:
                        continue
                    if skip_loopback and name == 'lo':
                        continue
                    self.interfaces.add(name)
        return self.interfaces
```

La classe HostIface obtient l'adresse IP et les masques de réseau de chaque interface locale en utilisant la [programmation de sockets](https://docs.python.org/3/howto/sockets.html). Ensuite, elle mappe chaque liste de réseaux pour ces combinaisons d'adresses IP + masques de réseau :

```python
SIOCGIFADDR = 0x8915
SIOCGIFNETMASK = 0x891B

class HostIface:
    @staticmethod
    def get_iface_details(iface: str):
        """
        Obtenir l'IP de l'interface réseau en utilisant le nom de l'interface réseau
        :return: Adresse IP et masque de réseau
        :param iface: Nom de l'interface (comme eth0, enp2s0, etc.)
        """
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            iface_pack = struct.pack('256s', bytes(iface, 'ascii'))
            packed_ip = fcntl.ioctl(s.fileno(), SIOCGIFADDR, iface_pack)[20:24]
            packed_netmask = fcntl.ioctl(s.fileno(), SIOCGIFNETMASK, iface_pack)[20:24]
        return socket.inet_ntoa(packed_ip), socket.inet_ntoa(packed_netmask)
    
    def get_local_networks(self, *, refresh: bool = False) -> List[ipaddress.IPv4Network]:
        """
        Obtenir la liste des réseaux locaux, en utilisant toutes les adresses IP locales
        :param refresh: Si vrai, relire /proc pour obtenir la liste des interfaces
        :return: Liste des adresses IPv4Network
        """
        local_networks: List[ipaddress.IPv4Network] = []
        for iface in self.get_alive_interfaces(refresh=refresh):
            ip, netmask = self.get_iface_details(iface)
            network: ipaddress.IPv4Network = ipaddress.ip_network(f"{ip}/{netmask}", strict=False)
            if network not in local_networks:
                local_networks.append(network)
        return local_networks
```

Notez que cela n'est pas portable sur d'autres systèmes d'exploitation comme BSD et surtout Windows.

## Comment assembler le nouveau frontend CLI de Nmap

Maintenant, créer une nouvelle CLI pour Nmap est simple. En plus, le nouveau frontend permet également de sauvegarder vos résultats de scan sous forme de fichier json (argument optionnel --report) :

```python
#!/usr/bin/env python
"""
# home_scan.py - Un script simple de découverte d'hôtes
Ce script peut scanner votre réseau domestique pour afficher les informations de tous les appareils connectés.

## Références :
* [Référence Nmap](https://nmap.org/book/man.html)

# Auteur
Jose Vicente Nunez Zuleta (kodegeek.com@protonmail.com)
"""
import json
import logging
import re
import sys

from rich.layout import Layout
from rich.live import Live
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.traceback import install
from rich.progress import TimeElapsedColumn, Progress, TextColumn
from typing import List
import argparse

from home_nmap.nmap import Scanner
from home_nmap.system import HostIface
from home_nmap.ui import create_scan_table, update_scan_table


def get_targets(target_list: List[str], cli_args: argparse.Namespace) -> str:
    if cli_args.target:
        for target in target_list:
            """
            Cela ne devrait pas arriver car le script a un alias pour -oX
            """
            if re.search("-oX", target):
                raise ValueError(f"Impossible de rediriger la sortie vers un fichier en passant -oX. Exécutez ce script avec --help")
        return ','.join(target_list)
    return ','.join(HostIface().get_prefixed_local_networks())


if __name__ == '__main__':

    install()
    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

    console = Console()
    arg_parser = argparse.ArgumentParser(
        description="Identifier mes appareils réseau locaux, avec les ports ouverts",
        prog=__file__
    )
    arg_parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help="Activer le mode débogage"
    )
    arg_parser.add_argument(
        '--results',
        '-xO',
        action='store',
        help=f"Si défini, sauvegarder les résultats du scan dans ce fichier."
    )
    arg_parser.add_argument(
        'target',
        action='store',
        nargs='*',
        help=(f"Une ou plusieurs cibles, au format Nmap (scanme.homenmap.org, microsoft.com/24, 192.168.0.1; "
              f"10.0.0-255.1-254). Si non fourni, scanner les réseaux locaux")
    )
    args = arg_parser.parse_args()

    current_app_progress = Progress(
        TimeElapsedColumn(),
        TextColumn("{task.description}"),
    )
    scanning_task = current_app_progress.add_task("[yellow]Attente[/yellow] des résultats du scan... :hourglass:")

    try:
        scanner = Scanner()
        scan_targets = get_targets(args.target, args)
        if args.results:
            table_title = f"Cibles : {scan_targets}, fichier des résultats={args.results}"
        else:
            table_title = f"Cibles : {scan_targets}"
        results_table = create_scan_table(cli=f"Cibles : {table_title}")
        layout = Layout()
        layout.split(
            Layout(name="Statut du scan", size=1),
            Layout(name="Résultats du scan"),
        )
        with Live(
                layout,
                console=console,
                screen=False,
                redirect_stderr=False,
        ) as live:
            layout['Scan results'].update(Text(
                text=f"Pas encore de résultats ({scan_targets})", style="green", justify="center")),
            layout['Scan status'].update(current_app_progress)
            nmap_args, data, stderr = scanner.scan(hosts=scan_targets)
            update_scan_table(scan_result=data,
                              results_table=results_table,
                              main_layout=layout,
                              progress=current_app_progress,
                              task_id=scanning_task
                              )
        if args.results:
            report_data = {
                'args': nmap_args,
                'scan': data
            }
            with open(args.results, 'w') as report_file:
                json.dump(report_data, report_file, indent=True)

    except ValueError:
        logging.exception("Il y a eu une erreur")
        sys.exit(100)
    except KeyboardInterrupt:
        console.log("Scan interrompu, sortie...")
        pass
    sys.exit(0)
```

Le code est devenu un peu plus verbeux en raison de l'analyse des arguments et de la gestion des mises à jour de l'interface utilisateur, mais pas trop.

Voyons un exemple contre 127.0.0.1 :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/home_scan.png align="left")

*Résultats d'une exécution en direct de Nmap, enrichis avec des avis CVE*

Si vous êtes curieux de savoir à quoi ressemble le rapport JSON résultant lorsque vous passez le flag --report :

```json
{
 "args": "/usr/bin/nmap -n -sS -p- -sV -O -T4 -PE --version-intensity 5 --disable-arp-ping --max-hostgroup 20 --min-parallelism 10 --osscan-limit --max-os-tries 1 -oX - 127.0.0.1",
 "scan": [
  {
   "addresses": [
    {   
     "ip": "127.0.0.1"
    }   
   ],  
   "ports": [
    {   
     "protocol": "tcp",
     "port_id": "22",
     "service_name": "ssh",
     "service_product": "OpenSSH",
     "service_version": "8.4",
     "cpe": "cpe:/o:linux:linux_kernel:2.6.32"
    },  
    {   
     "protocol": "tcp",
     "port_id": "631",
     "service_name": "ipp",
     "service_product": "CUPS",
     "service_version": "2.3",
     "cpe": "cpe:/o:linux:linux_kernel:2.6.32"
    },  
...]
}
```

## Et une interface graphique ?

Nmap dispose d'une interface graphique très complète appelée [Zenmap](https://nmap.org/zenmap/), mais le but était de vous montrer que vous pouvez également écrire une belle interface utilisateur texte en Python pour afficher les résultats.

Vous pouvez atteindre le même objectif en utilisant d'autres frameworks populaires comme [Tkinter](https://docs.python.org/3/library/tkinter.html), qui dispose d'une [documentation](https://tkdocs.com/tutorial/) incroyablement détaillée. Pour cette raison, nous n'approfondirons pas davantage ce sujet.

Au lieu de cela, laissez-moi vous montrer comment vous pouvez construire une API REST auto-documentée pour Nmap.

# Comment faire d'un scanner de réseau domestique un service Web

Parfois, vous ne pouvez pas installer Nmap car vous manquez des privilèges élevés pour le faire ou le serveur a des contraintes d'installation (comme l'espace ou la mémoire).

Ou il pourrait s'agir que vous souhaitez exécuter le scanner de ports sur une machine capable de se connecter à un réseau non directement accessible depuis le serveur sur lequel vous êtes actuellement connecté (et en contournant la ségrégation réseau imposée par le pare-feu). Dans ce cas, le service web agira comme un proxy pour exécuter notre commande Nmap.

Cela s'appelle également le "**pivoting**", et c'est une technique courante utilisée pour contourner les pare-feux et les serveurs proxy.

Faisons un petit détour pour parler davantage du pivoting avec Nmap.

### Peut-on exécuter Nmap à travers un proxy ?

Oui, vous pouvez utiliser [proxychains](https://github.com/haad/proxychains) pour exécuter Nmap à travers un hôte avec une meilleure connectivité ou pour contourner les restrictions de pare-feu :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pivot.png align="left")

*Utilisation du pivoting avec Nmap et Proxy-chains*

Supposons, pour l'argument, que l'hôte 'External Linux' n'a pas de connectivité directe avec le réseau 192.168.1.0/24 mais que 'Multi homed Linux' en a, et qu'il peut exécuter un proxy SOCKS-5.

Pour accéder au réseau interne, nous exécutons [SSH](https://en.wikipedia.org/wiki/Secure_Shell) en transférant le port 9050 (en tant que proxy SOCKS-5) sous l'utilisateur 'josevnz' :

```shell
josevnz@multihomed:~$ ssh  -N -D 9050 josevnz@192.168.1.11
The authenticity of host '192.168.1.11 (192.168.1.11)' can't be established.
ECDSA key fingerprint is SHA256:VIZCaCMb5rN2oL/xuv6CPrG1II+huW44x4TWhyKv8QM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.1.11' (ECDSA) to the list of known hosts.
```

Ensuite, nous installons proxychains sur 'External Linux' s'il n'est pas déjà présent :

```shell
# Vous installez d'abord proxychains avec 
# RedHat : 'sudo dnf -y install proxychains'
# Debian : 'sudo apt-get install proxychains4'
```

Et créez un fichier proxychains.conf pointant vers votre serveur proxy SSH SOCKS-5 :

```shell
cat<<CFG>$HOME/proxychains.conf
strict_chain
proxy_dns
remote_dns_subnet 224
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks5 192.168.1.11 9050
CFG
```

Enfin, exécutez Nmap, en utilisant un scan TCP :

```shell
[josevnz@external docs]$ proxychains -q -f $HOME/proxychains.conf sudo Nmap -sT 192.168.1.0/24
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-30 16:06 EST
```

Alternativement, dites simplement à Nmap lui-même d'utiliser notre nouveau proxy SOCKS-5 (la documentation [dit que cela est encore en développement](https://nmap.org/book/man-bypass-firewalls-ids.html)) :

```shell
[josevnz@external docs]$ sudo nmap -v -sT --proxies socks4://192.168.1.11:9050 192.168.1.0/24
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-31 09:03 EST
```

Maintenant, revenons au code de notre [service web](https://en.wikipedia.org/wiki/Web_service).

## Comment exécuter Nmap en tant que service web

Dans tous les cas, exécuter Nmap en tant que service n'est pas quelque chose de nouveau ([Nmap-cgi](http://nmap-cgi.tuxfamily.org/)). Nous allons créer le nôtre en utilisant [FastAPI](https://fastapi.tiangolo.com/).

J'ai assemblé un service web qui montre la version actuelle et également les interfaces réseau disponibles (home\_nmap/main.py) :

```python
"""
# Service web pour home_nmap
# Auteur
Jose Vicente Nunez Zuleta (kodegeek.com@protonmail.com)
"""
from home_nmap import __version__
from fastapi import FastAPI

from home_nmap.system import HostIface

app = FastAPI()


@app.get("/version")
async def version():
    return {"version": __version__}


@app.get("/local_networks")
async def local_networks():
    hi = HostIface()
    return hi.get_local_networks()
```

Dans FastApi, nous définissons les points de terminaison du service web avec des annotations, il s'occupe de la sérialisation de notre réponse vers le client.

Voici comment vous pouvez démarrer le service en utilisant le serveur web [uvicorn](https://www.uvicorn.org/) avec le flag '--reload' pour détecter les changements dans notre code automatiquement :

```shell
(home_nmap) [josevnz@dmaf5 home_nmap]$ uvicorn home_nmap.main:app --reload
INFO:     Will watch for changes in these directories: ['/home/josevnz/Documents/home_nmap']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [122202] using watchgod
INFO:     Started server process [122204]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Obtenir la version de l'API home\_nmap en utilisant [curl](https://curl.se/), impression JSON joli avec [jq](https://stedolan.github.io/jq/) :

```shell
(home_nmap) [josevnz@dmaf5 rich]$ curl --fail --silent http://127.0.0.1:8000/version| jq '.'
{
  "version": "0.0.1"
}
```

Maintenant, obtenir la liste des réseaux locaux en appelant le point de terminaison '/local\_networks' :

```shell
(home_nmap) [josevnz@dmaf5 rich]$ curl --fail --silent http://127.0.0.1:8000/local_networks| jq '.'
[
  "192.168.1.0/24"
]
```

Une chose agréable avec FastApi est que vous obtenez une documentation automatique pour vos points de terminaison REST ([http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)) :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/home_nmap_rest_documentation.png align="left")

*API REST auto-documentée de Nmap*

Pas mal pour quelques lignes de code, si vous me demandez.

## Comment implémenter le service de scanner

Dans le fichier 'main.py', nous implémentons le point de terminaison pour scanner le réseau local et pour corrélier le CPE avec d'éventuels avis :

```python
from typing import Optional
from home_nmap.system import NMapRunner
from home_nmap.query import NDISHtml, target_validator
from fastapi import FastAPI, HTTPException
app: FastAPI = FastAPI()

@app.get("/scan")
def scan(
        target: Optional[str] = None,
        full_advisories=True
):
    """
    Scanner une cible pour obtenir des informations sur les services.
    Note, FastAPI a un validateur de requête, mais j'ai décidé d'utiliser le mien car je recherche des cibles incorrectes :
    Query(None, min_length=MIN_LEN_TARGET, max_length=MAX_LEN_TARGET)
    @param target: Remplacer le réseau local par des cibles personnalisées, au format Nmap.
    @param full_advisories: Si faux, sauter les informations de résumé des avis
    @return: JSON contenant les résultats du scan
    """
    try:
        scanner = NMapRunner()
        args, scan_results, stderr = scanner.scan(hosts=target_validator(target))
        enriched_results = {
            'args': args,
            'hosts': []
        }
        if not scan_results:
            raise HTTPException(status_code=404, detail=f"Aucun résultat obtenu à partir du scan de la cible={target}")
        cpe_details = NDISHtml().correlate_nmap_with_nids(scan_results)
        for host_data in scan_results:
            enriched_host_data = {
                'address': host_data['address'],
                'ports': []
            }
            ports = host_data['ports']
            for port_data in ports:
                advisories = []
                # Déplier les avis, le cas échéant...
                for cpe in port_data['cpes']:
                    if cpe in cpe_details:  # Le service peut ne pas avoir d'avis
                        for nids in cpe_details[cpe]:
                            if full_advisories:
                                advisories.append({
                                    'link': nids.link,
                                    'summary': nids.summary,
                                    'score': nids.score
                                })
                            else:
                                advisories.append({
                                    'link': nids.link,
                                    'summary': '',  # Pour la cohérence
                                    'score': nids.score
                                })
                enriched_host_data['ports'].append(
                    {
                        'cpes': port_data['cpes'],
                        'advisories': advisories,
                        'protocol': port_data['protocol'],
                        'port_id': port_data['port_id'],
                        'service': [
                            f"{port_data['service_name']},",
                            f"{port_data['service_product']},",
                            f"{port_data['service_version']}"
                        ]
                    }
                )
            enriched_results['hosts'].append(enriched_host_data)
        return enriched_results
    except (TypeError, ValueError) as exp:
        raise HTTPException(status_code=500, detail=str(exp))
```

La fonction 'target\_validator' effectue quelques vérifications sur la cible pour s'assurer que seules des cibles de scan valides sont passées (c'est la même fonction que nous avons écrite pour le programme CLI) :

```python
import re
MIN_LEN_TARGET = 9
MAX_LEN_TARGET = 50
from typing import Optional
import shlex
def target_validator(target: Optional[str]) -> str:
    """
    Validateur simple pour les expressions de cible Nmap
    @param target: (scanme.homenmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254). None ou vide sont valides
    @return:
    """
    if target:
        regexp_list = [
            '-[a-z-A-Z][A-Z]*',
            '-[a-zA-Z]\\d*',
            '--[a-z-]+'
        ]
        if len(target) < MIN_LEN_TARGET:
            raise ValueError(f"Longueur fournie pour la cible trop petite < {MIN_LEN_TARGET}")
        if len(target) > MAX_LEN_TARGET:
            raise ValueError(f"Longueur fournie pour la cible trop grande < {MAX_LEN_TARGET}")
        for arg in shlex.split(target):
            for regexp in regexp_list:
                if re.search(regexp, arg):
                    raise ValueError(f"Vous ne pouvez pas remplacer les arguments de Nmap : {arg}")
    return target
```

Il est temps de tout rassembler.

### À quoi ressemble une exécution de scan (JSON très verbeux) ?

Voici à quoi ressemble le résultat du scan de 2 machines dans mon réseau local (le service web s'exécute sur dmaf5.home sur le port 8000) :

```shell
[josevnz@dmaf5 ~]$ curl http://dmaf5.home:8000/scan?target=192.168.1.10,23
{"args":"/usr/bin/nmap -n -sS -p- -sV -O -T4 -PE --version-intensity 5 --disable-arp-ping --max-hostgroup 20 --min-parallelism 10 --osscan-limit --max-os-tries 1 -oX - 192.168.1.10,23","hosts":[{"address":"192.168.1.10","ports":[{"cpes":["cpe:/a:openbsd:openssh:8.2p1"],"advisories":[{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-41617","summary":"sshd dans OpenSSH 6.2 à 8.x avant 8.8, lorsqu\'il est utilisé avec certaines configurations non par défaut, permet une élévation de privilèges car les groupes supplémentaires ne sont pas initialisés comme prévu. Les programmes d\'assistance pour AuthorizedKeysCommand et AuthorizedPrincipalsCommand peuvent s\'exécuter avec les privilèges associés aux appartenances de groupe du processus sshd, si la configuration spécifie l\'exécution de la commande en tant qu\'utilisateur différent.","score":"4.4 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2016-20012","summary":"OpenSSH jusqu\'à 8.7 permet aux attaquants distants, qui ont un soupçon qu\'une certaine combinaison de nom d\'utilisateur et de clé publique est connue d\'un serveur SSH, de tester si ce soupçon est correct. Cela se produit car un défi est envoyé uniquement lorsque cette combinaison pourrait être valide pour une session de connexion.","score":"4.3 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-28041","summary":"ssh-agent dans OpenSSH avant 8.5 a un double free qui peut être pertinent dans quelques scénarios moins courants, tels que l\'accès non contraint au socket de l\'agent sur un système d\'exploitation hérité, ou le transfert d\'un agent vers un hôte contrôlé par l\'attaquant.","score":"4.6 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2020-15778","summary":"** DISPUTÉ ** scp dans OpenSSH jusqu\'à 8.3p1 permet l\'injection de commande dans la fonction toremote de scp.c, comme démontré par des caractères backtick dans l\'argument de destination. NOTE : le fournisseur aurait apparemment déclaré qu\'ils omettent intentionnellement la validation des \"transfers d\'arguments anormaux\" car cela pourrait \"avoir une grande chance de rompre les workflows existants.\"","score":"6.8 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2020-14145","summary":"Le côté client dans OpenSSH 5.7 à 8.4 a une Discrepancy Observable conduisant à une fuite d\'informations dans la négociation d\'algorithme. Cela permet aux attaquants de type man-in-the-middle de cibler les tentatives de connexion initiales (où aucune clé d\'hôte pour le serveur n\'a été mise en cache par le client). NOTE : certains rapports indiquent que 8.5 et 8.6 sont également affectés.","score":"4.3 MEDIUM"}],"protocol":"tcp","port_id":"22","service":[["ssh"],["OpenSSH"],["8.2p1 Ubuntu 4ubuntu0.3"]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"2377","service":[["swarm"],[""],[""]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"7946","service":[["unknown"],[""],[""]]},{"cpes":["cpe:/a:influxdata:influxdb:2.1.1"],"advisories":[],"protocol":"tcp","port_id":"8086","service":[["http"],["InfluxDB http admin"],["2.1.1"]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"9100","service":[["jetdirect"],[""],[""]]},{"cpes":["cpe:/a:protocol_labs:go-ipfs"],"advisories":[],"protocol":"tcp","port_id":"9323","service":[["http"],["Golang net/http server"],[""]]}]},{"address":"DC:A6:32:F9:47:48","ports":[{"cpes":["cpe:/a:openbsd:openssh:8.2p1"],"advisories":[{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-41617","summary":"sshd dans OpenSSH 6.2 à 8.x avant 8.8, lorsqu\'il est utilisé avec certaines configurations non par défaut, permet une élévation de privilèges car les groupes supplémentaires ne sont pas initialisés comme prévu. Les programmes d\'assistance pour AuthorizedKeysCommand et AuthorizedPrincipalsCommand peuvent s\'exécuter avec les privilèges associés aux appartenances de groupe du processus sshd, si la configuration spécifie l\'exécution de la commande en tant qu\'utilisateur différent.","score":"4.4 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2016-20012","summary":"OpenSSH jusqu\'à 8.7 permet aux attaquants distants, qui ont un soupçon qu\'une certaine combinaison de nom d\'utilisateur et de clé publique est connue d\'un serveur SSH, de tester si ce soupçon est correct. Cela se produit car un défi est envoyé uniquement lorsque cette combinaison pourrait être valide pour une session de connexion.","score":"4.3 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-28041","summary":"ssh-agent dans OpenSSH avant 8.5 a un double free qui peut être pertinent dans quelques scénarios moins courants, tels que l\'accès non contraint au socket de l\'agent sur un système d\'exploitation hérité, ou le transfert d\'un agent vers un hôte contrôlé par l\'attaquant.","score":"4.6 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2020-15778","summary":"** DISPUTÉ ** scp dans OpenSSH jusqu\'à 8.3p1 permet l\'injection de commande dans la fonction toremote de scp.c, comme démontré par des caractères backtick dans l\'argument de destination. NOTE : le fournisseur aurait apparemment déclaré qu\'ils omettent intentionnellement la validation des \"transfers d\'arguments anormaux\" car cela pourrait \"avoir une grande chance de rompre les workflows existants.\"","score":"6.8 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2020-14145","summary":"Le côté client dans OpenSSH 5.7 à 8.4 a une Discrepancy Observable conduisant à une fuite d\'informations dans la négociation d\'algorithme. Cela permet aux attaquants de type man-in-the-middle de cibler les tentatives de connexion initiales (où aucune clé d\'hôte pour le serveur n\'a été mise en cache par le client). NOTE : certains rapports indiquent que 8.5 et 8.6 sont également affectés.","score":"4.3 MEDIUM"}],"protocol":"tcp","port_id":"22","service":[["ssh"],["OpenSSH"],["8.2p1 Ubuntu 4ubuntu0.3"]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"2377","service":[["swarm"],[""],[""]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"7946","service":[["unknown"],[""],[""]]},{"cpes":["cpe:/a:influxdata:influxdb:2.1.1"],"advisories":[],"protocol":"tcp","port_id":"8086","service":[["http"],["InfluxDB http admin"],["2.1.1"]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"9100","service":[["jetdirect"],[""],[""]]},{"cpes":["cpe:/a:protocol_labs:go-ipfs"],"advisories":[],"protocol":"tcp","port_id":"9323","service":[["http"],["Golang net/http server"],[""]]}]},{"address":"192.168.1.23","ports":[{"cpes":["cpe:/a:openbsd:openssh:8.4"],"advisories":[{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-41617","summary":"sshd dans OpenSSH 6.2 à 8.x avant 8.8, lorsqu\'il est utilisé avec certaines configurations non par défaut, permet une élévation de privilèges car les groupes supplémentaires ne sont pas initialisés comme prévu. Les programmes d\'assistance pour AuthorizedKeysCommand et AuthorizedPrincipalsCommand peuvent s\'exécuter avec les privilèges associés aux appartenances de groupe du processus sshd, si la configuration spécifie l\'exécution de la commande en tant qu\'utilisateur différent.","score":"4.4 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2016-20012","summary":"OpenSSH jusqu\'à 8.7 permet aux attaquants distants, qui ont un soupçon qu\'une certaine combinaison de nom d\'utilisateur et de clé publique est connue d\'un serveur SSH, de tester si ce soupçon est correct. Cela se produit car un défi est envoyé uniquement lorsque cette combinaison pourrait être valide pour une session de connexion.","score":"4.3 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-28041","summary":"ssh-agent dans OpenSSH avant 8.5 a un double free qui peut être pertinent dans quelques scénarios moins courants, tels que l\'accès non contraint au socket de l\'agent sur un système d\'exploitation hérité, ou le transfert d\'un agent vers un hôte contrôlé par l\'attaquant.","score":"4.6 MEDIUM"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2020-14145","summary":"Le côté client dans OpenSSH 5.7 à 8.4 a une Discrepancy Observable conduisant à une fuite d\'informations dans la négociation d\'algorithme. Cela permet aux attaquants de type man-in-the-middle de cibler les tentatives de connexion initiales (où aucune clé d\'hôte pour le serveur n\'a été mise en cache par le client). NOTE : certains rapports indiquent que 8.5 et 8.6 sont également affectés.","score":"4.3 MEDIUM"}],"protocol":"tcp","port_id":"22","service":[["ssh"],["OpenSSH"],["8.4"]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"5355","service":[["llmnr"],[""],[""]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"8443","service":[["https-alt"],[""],[""]]},{"cpes":[],"advisories":[],"protocol":"tcp","port_id":"9100","service":[["jetdirect"],[""],[""]]}]}]}[josevnz@dmaf5 ~]$
```

## Ce service web est-il sécurisé ?

Nous avons exposé notre scanner Nmap *sans autorisation*, ce qui signifie que toute personne connaissant l'emplacement du service peut l'utiliser. Cela peut ne pas être un gros problème sur le réseau local, mais il serait bon de contrôler qui utilise nos précieuses ressources.

### Comment ajouter une authentification et une autorisation

Actuellement, n'importe qui peut appeler notre service. Il est bon de contrôler qui peut exécuter Nmap contre notre réseau domestique.

Il existe [plusieurs façons](https://fastapi.tiangolo.com/tutorial/security/) de s'assurer que notre service web ne peut être utilisé que par des clients autorisés. Une façon de le faire est de demander à un client de fournir une clé également connue du serveur. C'est l'approche que nous allons suivre ici.

NOTE : Comme vous l'avez peut-être deviné, si quelqu'un découvre la clé, votre service est compromis. Pour le rendre plus sécurisé, vous devez :

* Stocker la clé dans un endroit sûr, chiffrée
    
* Avoir une date d'expiration, pour purger les anciennes
    
* Et le transit de ces clés doit se faire sur un canal chiffré, comme HTTPS (nous en parlerons bientôt)
    

Nous allons tirer parti de [fastapi\_simple\_security](https://github.com/mrtolkien/fastapi_simple_security) pour implémenter l'accès sécurisé à l'API de notre application web. Il ne nécessite que quelques nouvelles importations et que nous déclarions une dépendance sur nos points de terminaison REST API :

```python
from fastapi import FastAPI, Depends
from fastapi_simple_security import api_key_router, api_key_security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import typing
from home_nmap.system import HostIface
...
app: typing.Union[FastAPI] = FastAPI()
app.include_router(api_key_router, prefix="/auth", tags=["_auth"])

# Ensuite, ajoutez une 'dependencies' à chacun des points de terminaison que nous voulons sécuriser
@app.get("/local_networks", dependencies=[Depends(api_key_security)])
def local_networks():
    """
    Obtenir les réseaux locaux disponibles où home_nmap s'exécute
    @return: Liste avec les réseaux locaux au format CIDR
    """
    response = JSONResponse(jsonable_encoder(HostIface().get_local_networks()))
    return response
...
```

Si nous ne définissons pas de clé API secrète, le framework nous en fournira une au démarrage (mais vous pouvez la remplacer plus tard via la page de documentation) :

```shell
(home_nmap) [josevnz@dmaf5 home_nmap]$ uuidgen 
23eb5572-1e63-4404-a64b-bcc18b62d4eb
(home_nmap) [josevnz@dmaf5 home_nmap]$ export FASTAPI_SIMPLE_SECURITY_SECRET="23eb5572-1e63-4404-a64b-bcc18b62d4eb"; uvicorn home_nmap.main:app --host 0.0.0.0 --port 8000 --reloadINFO:     Will watch for changes in these directories: ['/home/josevnz/Documents/home_nmap']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [134702] using watchgod
INFO:     Started server process [134704]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Maintenant, toutes les API qui sont protégées par les clés ont une décoration différente dans la documentation (un cadenas à côté de chaque point de terminaison) :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/documentation_shows_secured_endpoints.png align="left")

*La documentation montre maintenant les points de terminaison sécurisés*

Que se passe-t-il si nous essayons d'obtenir la liste des réseaux locaux, sans notre clé ?

```shell
josevnz@dmaf5 ~]$ curl 'http://127.0.0.1:8000/local_networks' --header 'accept: application/json'
{"detail":"Une clé API doit être passée en tant que requête ou en-tête"}
```

Pour terminer la configuration, vous devez entrer votre 'clé secrète' (`23eb5572-1e63-4404-a64b-bcc18b62d4eb`) dans la page d'authentification des docs. Ensuite, allez à */auth/new pour obtenir la clé API*, qui est celle que vos clients utiliseront (en-tête, cookie ou partie des requêtes GET). Dans mon cas, j'ai obtenu ceci :

```shell
curl 'http://127.0.0.1:8000/auth/new?never_expires=false' \
  --header 'accept: application/json' \
  --header 'secret-key: 23eb5572-1e63-4404-a64b-bcc18b62d4eb'
"e4c03730-02a1-4cb9-8e00-36a63930c064"
```

Maintenant, essayons à nouveau mais en passant notre clé API secrète :

```shell
[josevnz@dmaf5 home_nmap]$ curl 'http://127.0.0.1:8000/local_networks'  --header 'accept: application/json' --header 'api-key: e4c03730-02a1-4cb9-8e00-36a63930c064'
["192.168.1.0/24"][josevnz@dmaf5 home_nmap]$
```

Nous n'avons pas encore terminé. Supposons que quelqu'un ait réussi à exécuter un renifleur sur votre réseau et capture tout votre trafic HTTP :

```shell
[josevnz@dmaf5 home_nmap]$ tshark -i eno1 -Px -Y http
Capturing on 'eno1'
   72 5.107984320 192.168.1.11  192.168.1.25 HTTP 219 GET /local_networks HTTP/1.1 

0000  1c 83 41 28 44 21 dc a6 32 f9 47 48 08 00 45 00   ..A(D!..2.GH..E.
0010  00 cd 7b ca 40 00 40 06 3a ec c0 a8 01 0b c0 a8   ..{.@.@.:.......
0020  01 19 b1 a6 1f 40 ce 1b 2a 22 ab b5 24 3c 80 18   .....@..*"..$<..
0030  01 f6 d0 3d 00 00 01 01 08 0a f3 07 ee 27 9d 96   ...=.........'..
0040  87 76 47 45 54 20 2f 6c 6f 63 61 6c 5f 6e 65 74   .vGET /local_net
0050  77 6f 72 6b 73 20 48 54 54 50 2f 31 2e 31 0d 0a   works HTTP/1.1..
0060  48 6f 73 74 3a 20 64 6d 61 66 35 2e 68 6f 6d 65   Host: dmaf5.home
0070  3a 38 30 30 30 0d 0a 55 73 65 72 2d 41 67 65 6e   :8000..User-Agen
0080  74 3a 20 63 75 72 6c 2f 37 2e 36 38 2e 30 0d 0a   t: curl/7.68.0..
0090  61 63 63 65 70 74 3a 20 61 70 70 6c 69 63 61 74   accept: applicat
00a0  69 6f 6e 2f 6a 73 6f 6e 0d 0a 61 70 69 2d 6b 65   ion/json..api-ke
00b0  79 3a 20 65 34 63 30 33 37 33 30 2d 30 32 61 31   y: e4c03730-02a1
00c0  2d 34 63 62 39 2d 38 65 30 30 2d 33 36 61 36 33   -4cb9-8e00-36a63
00d0  39 33 30 63 30 36 34 0d 0a 0d 0a                  930c064....
```

Vous pouvez clairement voir notre clé API qui n'est plus si secrète. Il est temps d'ajouter la prochaine couche de protection.

### Nous avons besoin de chiffrement

Le protocole HTTP n'est pas chiffré. Cela signifie que quelqu'un utilisant un renifleur (comme tcpdump ou wireshark) peut capturer le trafic. Par exemple, si nous demandons la version de home\_nmap en utilisant curl :

```shell
curl http://dmaf5.home:8000/version
```

Il est possible pour quelqu'un d'autre exécutant [tshark](https://tshark.dev/setup/install/) de voir tout le trafic (regardez le content-type : charge utile Application/Json) :

```shell
root@dmaf5 ~]# tshark -i eno1 -Px -Y http
Running as user "root" and group "root". This could be dangerous.
Capturing on 'eno1'
  127 4.342379691 192.168.1.11  192.168.1.23 HTTP 152 GET /version HTTP/1.1 

0000  1c 83 41 28 44 21 dc a6 32 f9 47 48 08 00 45 00   ..A(D!..2.GH..E.
0010  00 8a c3 8a 40 00 40 06 f3 70 c0 a8 01 0b c0 a8   ....@.@..p......
0020  01 17 c7 68 1f 40 dc af 3c 37 c1 12 e6 69 80 18   ...h.@..<7...i..
0030  01 f6 ff a7 00 00 01 01 08 0a 08 94 d3 55 a8 7c   .............U.|
0040  ec df 47 45 54 20 2f 76 65 72 73 69 6f 6e 20 48   ..GET /version H
0050  54 54 50 2f 31 2e 31 0d 0a 48 6f 73 74 3a 20 64   TTP/1.1..Host: d
0060  6d 61 66 35 2e 68 6f 6d 65 3a 38 30 30 30 0d 0a   maf5.home:8000..
0070  55 73 65 72 2d 41 67 65 6e 74 3a 20 63 75 72 6c   User-Agent: curl
0080  2f 37 2e 36 38 2e 30 0d 0a 41 63 63 65 70 74 3a   /7.68.0..Accept:
0090  20 2a 2f 2a 0d 0a 0d 0a                            */*....

  129 4.344312849 192.168.1.23  192.168.1.11 HTTP/JSON 210 HTTP/1.1 200 OK , JavaScript Object Notation (application/json)

0000  dc a6 32 f9 47 48 1c 83 41 28 44 21 08 00 45 00   ..2.GH..A(D!..E.
0010  00 c4 36 78 40 00 40 06 80 49 c0 a8 01 17 c0 a8   ..6x@.@..I......
0020  01 0b 1f 40 c7 68 c1 12 e6 69 dc af 3c 8d 80 18   ...@.h...i..<...
0030  01 fd 84 29 00 00 01 01 08 0a a8 7c ec e1 08 94   ...).......|....
0040  d3 55 48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f   .UHTTP/1.1 200 O
0050  4b 0d 0a 64 61 74 65 3a 20 4d 6f 6e 2c 20 31 37   K..date: Mon, 17
0060  20 4a 61 6e 20 32 30 32 32 20 32 30 3a 31 36 3a    Jan 2022 20:16:
0070  32 39 20 47 4d 54 0d 0a 73 65 72 76 65 72 3a 20   29 GMT..server: 
0080  75 76 69 63 6f 72 6e 0d 0a 63 6f 6e 74 65 6e 74   uvicorn..content
0090  2d 6c 65 6e 67 74 68 3a 20 31 39 0d 0a 63 6f 6e   -length: 19..con
00a0  74 65 6e 74 2d 74 79 70 65 3a 20 61 70 70 6c 69   tent-type: appli
00b0  63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a 0d 0a 7b   cation/json....{
00c0  22 76 65 72 73 69 6f 6e 22 3a 22 30 2e 30 2e 31   "version":"0.0.1
00d0  22 7d                                             "}
```

Nous pouvons protéger notre trafic en le chiffrant en utilisant [Hypertext Transfer Protocol Secure (HTTPS)](https://en.wikipedia.org/wiki/HTTPS).

#### Comment créer les certificats Secure Socket Layer (SSL)

Laissez-moi vous montrer rapidement [comment vous pouvez installer un certificat de serveur auto-signé](https://github.com/rob-blackbourn/ssl-certs) sur Fedora en utilisant [Cloudflare cfssl](https://github.com/cloudflare/cfssl). D'abord, installons les outils :

```shell
# Sur Fedora, faites simplement 
sudo dnf install -y golang-github-cloudflare-cfssl
# Ou go get github.com/cloudflare/cfssl/cmd/...
```

L'étape suivante consiste à créer une autorité de certification (CA). Nous l'utiliserons pour signer d'autres certificats. Pour cela, créons une définition au format JSON :

```json
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
```

Créez le certificat :

```shell
cfssl gencert -initca ca.json | cfssljson -bare ca
```

Ensuite, nous devons créer un fichier de profil (cfssl.json), qui spécifiera certaines caractéristiques des certificats, comme l'expiration dans 2 ans :

```json
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
```

Maintenant, nous créons un certificat intermédiaire (intermediate-ca.json) qui expirera dans 5 ans :

```json
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
```

Voici la commande pour le faire :

```shell
cfssl gencert -initca intermediate-ca.json | cfssljson -bare intermediate_ca
cfssl sign -ca ca.pem -ca-key ca-key.pem -config cfssl.json -profile intermediate_ca intermediate_ca.csr | cfssljson -bare intermediate_ca
```

### L'étape suivante est de créer les certificats d'hôte

Vous devrez mettre votre nom d'hôte entièrement qualifié (`hostname -f`) dans le fichier host-1.json. De plus, certains logiciels s'attendent à l'adresse IP (`ip address|grep inet`) – nous ferons les deux :

```json
{
  "CN": "dmaf5.home",
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
    "dmaf5.home",
    "localhost",
    "dmaf5",
    "192.168.1.23",
    "192.168.1.26"
  ]
}
```

Vous pouvez créer trois types de certificats :

* client
    
* serveur
    
* pair
    

Nous n'utiliserons que le certificat serveur, mais nous créerons les trois :

```shell
cfssl gencert -ca intermediate_ca.pem -ca-key intermediate_ca-key.pem -config cfssl.json -profile=peer host-1.json| cfssljson -bare host-1-peer  # Pair
cfssl gencert -ca intermediate_ca.pem -ca-key intermediate_ca-key.pem -config cfssl.json -profile=server host-1.json | cfssljson -bare host-1-server  # Serveur
cfssl gencert -ca intermediate_ca.pem -ca-key intermediate_ca-key.pem -config cfssl.json -profile=client host-1.json | cfssljson -bare host-1-client  # Client
```

Nous sommes très proches maintenant. Installez le certificat intermédiaire dans l'emplacement approprié afin que les clients sur dmaf5 ne se plaignent pas du certificat auto-signé :

```shell
# Le chemin ci-dessous est pour Fedora, veuillez consulter la documentation de votre OS pour trouver le bon chemin pour vous
sudo /bin/cp --preserve --verbose tutorial/intermediate_ca.pem /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust
```

Redémarrez uvicorn pour écouter maintenant uniquement sur un port sécurisé, en utilisant la clé d'hôte et les certificats que nous venons de créer :

```shell
(home_nmap) [josevnz@dmaf5 home_nmap]$ uvicorn home_nmap.main:app --host 0.0.0.0 --port 8443 --reload --ssl-keyfile=$PWD/tutorial/host-1-server-key.pem --ssl-certfile=$PWD/tutorial/host-1-server.pem
INFO:     Will watch for changes in these directories: ['/home/josevnz/Documents/home_nmap']
INFO:     Uvicorn running on https://0.0.0.0:8443 (Press CTRL+C to quit)
INFO:     Started reloader process [166275] using watchgod
INFO:     Started server process [166277]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     192.168.1.23:47704 - "GET /version HTTP/1.1" 200 OK
```

Puis testez avec curl (sans le flag --insecure, pas de plaintes de curl) :

```shell
[josevnz@dmaf5 ~]$ curl --fail https://dmaf5.home:8443/version
{"version":"0.0.1"}[josevnz@dmaf5 ~]$
```

Essayez à nouveau de capturer la version de notre service en utilisant tshark :

```shell
# 'tshark -i eno1 -Px -Y http' ne fonctionne plus car la charge utile est chiffrée. Alors au moins voyons comment se passe le SSL hello
tshark -i eno1 -Y ssl -Px
  343 59.344539258 192.168.1.11  192.168.1.23 TLSv1 583 Client Hello

0000  1c 83 41 28 44 21 dc a6 32 f9 47 48 08 00 45 00   ..A(D!..2.GH..E.
0010  02 39 8b 6b 40 00 40 06 29 e1 c0 a8 01 0b c0 a8   .9.k@.@.).......
0020  01 17 93 14 20 fb 10 10 d7 6f 7d ff f7 c1 80 18   .... ....o}.....
0030  01 f6 0b fe 00 00 01 01 08 0a 08 a5 00 20 a8 8d   ............. ..
0040  27 47 16 03 01 02 00 01 00 01 fc 03 03 39 03 ac   'G...........9..
0050  19 7c bd 38 dc e2 cf 72 8b 7e 00 e2 2d fc 68 7a   .|.8...r.~..-.hz
0060  cc af 9c d6 d5 1d ed 94 79 b2 0f c8 cf 20 a3 f8   ........y.... ..
0070  2a 8e 20 c0 d2 c1 57 ee 36 48 2e 8f 46 e7 da 76   *. ...W.6H..F..v
0080  69 67 d1 9d 5a 70 24 0e 7d ea ec 8b e2 a0 00 3e   ig..Zp$.}......>
0090  13 02 13 03 13 01 c0 2c c0 30 00 9f cc a9 cc a8   .......,.0......
00a0  cc aa c0 2b c0 2f 00 9e c0 24 c0 28 00 6b c0 23   ...+./...$.(.k.#
00b0  c0 27 00 67 c0 0a c0 14 00 39 c0 09 c0 13 00 33   .'.g.....9.....3
00c0  00 9d 00 9c 00 3d 00 3c 00 35 00 2f 00 ff 01 00   .....=.<.5./....
00d0  01 75 00 00 00 0f 00 0d 00 00 0a 64 6d 61 66 35   .u.........dmaf5
00e0  2e 68 6f 6d 65 00 0b 00 04 03 00 01 02 00 0a 00   .home...........
00f0  0c 00 0a 00 1d 00 17 00 1e 00 19 00 18 33 74 00   .............3t.
0100  00 00 10 00 0e 00 0c 02 68 32 08 68 74 74 70 2f   ........h2.http/
0110  31 2e 31 00 16 00 00 00 17 00 00 00 31 00 00 00   1.1.........1...
0120  0d 00 2a 00 28 04 03 05 03 06 03 08 07 08 08 08   ..*.(...........
0130  09 08 0a 08 0b 08 04 08 05 08 06 04 01 05 01 06   ................
0140  01 03 03 03 01 03 02 04 02 05 02 06 02 00 2b 00   ..............+.
```

Notez qu'il est possible de capturer le trafic et de le déchiffrer plus tard si vous avez accès à la clé privée. C'est pourquoi il est si important que vous gardiez ce fichier sécurisé.

Qu'en est-il de notre requête autorisée utilisant la clé API + chiffrement ?

```shell
josevnz@raspberrypi:~$ curl 'https://dmaf5.home:8443/local_networks' --header 'accept: application/json' --header 'api-key: e4c03730-02a1-4cb9-8e00-36a63930c064'
["192.168.1.0/24"]
```

La configuration de notre application est maintenant complète.

# Qu'avons-nous appris ?

Dans cet article, nous avons couvert de nombreux sujets et sommes passés d'un analyseur XML très simple à un service web auto-documenté. Pas mal pour une seule session !

Vous devriez maintenant connaître les sujets suivants :

* Comment analyser un fichier de résultats XML de Nmap et l'enrichir avec des avis de sécurité du NIST
    
* Comment améliorer Nmap en le mélangeant avec d'autres scripts pour automatiser son exécution
    
* Comment appliquer les options de Nmap pour rendre notre scan de réseau local plus rapide
    
* Comprendre ce qu'est le pivoting et comment vous pouvez l'utiliser pour contourner les protections de pare-feu avec l'aide de SSH et tcpproxy
    
* Comment écrire une API REST au-dessus de notre script CLI original et le sécuriser avec SSL et une authentification de base
    
* Comment ajouter une autorisation à un service web en utilisant une clé API
    
* Comment utiliser tshark pour démontrer comment le trafic HTTP peut être capturé et montrer la charge utile des données
    
* Comment ajouter un chiffrement à un service web en créant des certificats auto-signés
    

### Et que pourriez-vous apprendre d'autre ? Voici quelques suggestions finales :

* Consultez la documentation officielle de Nmap [documentation](https://nmap.org/docs.html).
    
* L'[identification des empreintes du système d'exploitation](https://nmap.org/book/osdetect.html) est fascinante. Déterminer exactement ce qui se cache derrière un port est un art et une cible mouvante.
    
* Intégration avec d'autres excellents outils de [test d'intrusion](https://en.wikipedia.org/wiki/Penetration_test) comme [Metasploit](https://github.com/rapid7/metasploit-framework), que vous avez deviné, [peut également être scripté en Ruby](https://www.offensive-security.com/metasploit-unleashed/custom-scripting/) !
    
* De plus, en bonus, vous avez mon code qui peut être installé en utilisant [pip](https://pip.pypa.io/en/stable/) et peut exécuter quelques tests unitaires avec [unittest](https://docs.python.org/3/library/unittest.html). Je suis ouvert aux pull requests et suggestions.
    

N'hésitez pas à me contacter avec vos commentaires et [rapports de bugs](https://github.com/josevnz/home_nmap/issues). J'espère que vous prendrez autant de plaisir à l'utiliser que j'en ai eu à l'écrire.