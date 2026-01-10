---
title: 'Comment construire un honeypot en Python : Un guide pratique de la déception
  de sécurité'
subtitle: ''
author: Chaitanya Rahalkar
co_authors: []
series: null
date: '2024-12-19T16:58:45.448Z'
originalURL: https://freecodecamp.org/news/build-a-honeypot-with-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734581440876/9b4a1d00-6185-4666-94cc-97131eed03fa.png
tags:
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: 'Comment construire un honeypot en Python : Un guide pratique de la déception
  de sécurité'
seo_desc: 'In cybersecurity, a honeypot is a decoy system that’s designed to attract
  and then detect potential attackers attempting to compromise the system. Just like
  a pot of honey sitting out in the open would attract flies.

  Think of these honeypots as secur...'
---

En cybersécurité, un honeypot est un système leurre conçu pour attirer et détecter les attaquants potentiels tentant de compromettre le système. Tout comme un pot de miel laissé à découvert attirerait les mouches.

Considérez ces honeypots comme des caméras de sécurité pour votre système. Tout comme une caméra de sécurité nous aide à comprendre qui tente de s'introduire dans un bâtiment et comment ils procèdent, ces honeypots vous aideront à comprendre qui tente d'attaquer votre système et quelles techniques ils utilisent.

À la fin de ce tutoriel, vous serez capable d'écrire un honeypot de démonstration en Python et de comprendre comment les honeypots fonctionnent.

## Table des matières

* [Comprendre les types de honeypots](#heading-comprendre-les-types-de-honeypots)
    
* [Comment configurer votre environnement de développement](#heading-comment-configurer-votre-environnement-de-developpement)
    
* [Comment construire le cœur du honeypot](#heading-comment-construire-le-cœur-du-honeypot)
    
    * [Implémenter les écouteurs réseau](#heading-implementer-les-ecouteurs-reseau)
        
    * [Exécuter le honeypot](#heading-executer-le-honeypot)
        
    * [Écrire le simulateur d'attaques du honeypot](#heading-ecrire-le-simulateur-dattaques-du-honeypot)
        
* [Comment analyser les données du honeypot](#heading-comment-analyser-les-donnees-du-honeypot)
    
* [Considérations de sécurité](#heading-considerations-de-securite)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre les types de honeypots

Avant de commencer à concevoir notre propre honeypot, comprenons rapidement leurs différents types :

1. Honeypots de production : Ces types de honeypots sont placés dans un environnement de production réel et sont utilisés pour détecter des attaques de sécurité réelles. Ils sont généralement simples dans leur conception, faciles à maintenir et à déployer, et offrent une interaction limitée pour réduire les risques.
    
2. Honeypots de recherche : Il s'agit de systèmes plus complexes mis en place par des chercheurs en sécurité pour étudier les schémas d'attaque, effectuer des analyses empiriques sur ces schémas, collecter des échantillons de logiciels malveillants et comprendre de nouvelles techniques d'attaque non découvertes auparavant. Ils émulent souvent des systèmes d'exploitation ou des réseaux entiers plutôt que de se comporter comme une application dans l'environnement de production.
    

Pour ce tutoriel, nous allons construire un honeypot à interaction moyenne qui journalise les tentatives de connexion et le comportement de base de l'attaquant.

## Comment configurer votre environnement de développement

Commençons par configurer votre environnement de développement en Python. Exécutez les commandes suivantes :

```python
import socket
import sys
import datetime
import json
import threading
from pathlib import Path

# Configurer le répertoire de journalisation
LOG_DIR = Path("honeypot_logs")
LOG_DIR.mkdir(exist_ok=True)
```

Nous allons utiliser les bibliothèques intégrées, donc nous n'aurons pas besoin d'installer de dépendances externes. Nous allons stocker nos journaux dans le répertoire `honeypot_logs`.

## Comment construire le cœur du honeypot

Notre honeypot de base sera composé de trois composants :

1. Un écouteur réseau qui accepte les connexions
    
2. Un système de journalisation pour enregistrer les activités
    
3. Un service d'émulation de base pour interagir avec les attaquants
    

Commençons par initialiser la classe principale Honeypot :

```python
class Honeypot:
    def __init__(self, bind_ip="0.0.0.0", ports=None):
        self.bind_ip = bind_ip
        self.ports = ports or [21, 22, 80, 443]  # Ports par défaut à surveiller
        self.active_connections = {}
        self.log_file = LOG_DIR / f"honeypot_{datetime.datetime.now().strftime('%Y%m%d')}.json"
        
    def log_activity(self, port, remote_ip, data):
        """Journaliser l'activité suspecte avec un horodatage et des détails"""
        activity = {
            "timestamp": datetime.datetime.now().isoformat(),
            "remote_ip": remote_ip,
            "port": port,
            "data": data.decode('utf-8', errors='ignore')
        }
        
        with open(self.log_file, 'a') as f:
            json.dump(activity, f)
            f.write('\n')
            
    def handle_connection(self, client_socket, remote_ip, port):
        """Gérer les connexions individuelles et émuler les services"""
        service_banners = {
            21: "220 FTP server ready\r\n",
            22: "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n",
            80: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n",
            443: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n"
        }
        
        try:
            # Envoyer la bannière appropriée pour le service
            if port in service_banners:
                client_socket.send(service_banners[port].encode())
            
            # Recevoir les données de l'attaquant
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                    
                self.log_activity(port, remote_ip, data)
                
                # Envoyer une fausse réponse
                client_socket.send(b"Command not recognized.\r\n")
                
        except Exception as e:
            print(f"Erreur lors de la gestion de la connexion : {e}")
        finally:
            client_socket.close()
```

Cette classe contient beaucoup d'informations importantes, alors passons en revue chaque fonction une par une.

La fonction `__init__` enregistre l'IP et les numéros de port sur lesquels nous allons héberger le honeypot, ainsi que le chemin / nom de fichier du fichier de journal. Nous allons également maintenir un enregistrement du nombre total de connexions actives que nous avons avec le honeypot.

La fonction `log_activity` va recevoir les informations sur l'IP, les données et le port auquel l'IP a tenté une connexion. Ensuite, nous allons ajouter ces informations à notre fichier de journal au format JSON.

La fonction `handle_connection` va imiter ces services qui seront exécutés sur les différents ports que nous avons. Nous aurons le honeypot en cours d'exécution sur les ports 21, 22, 80 et 443. Ces services sont pour FTP, SSH, HTTP et le protocole HTTPS, respectivement. Ainsi, tout attaquant tentant d'interagir avec le honeypot devrait s'attendre à ces services sur ces ports.

Pour imiter le comportement de ces services, nous allons utiliser les bannières de service qu'ils utilisent en réalité. Cette fonction va d'abord envoyer la bannière appropriée lorsque l'attaquant se connecte, puis recevoir les données et les journaliser. Le honeypot enverra également une fausse réponse "Command not recognized" à l'attaquant.

### Implémenter les écouteurs réseau

Maintenant, implémentons les écouteurs réseau qui vont gérer les connexions entrantes. Pour cela, nous allons utiliser une simple programmation de socket. Si vous n'êtes pas familier avec le fonctionnement de la programmation de socket, [consultez cet article](https://www.freecodecamp.org/news/socket-programming-in-python) qui explique certains concepts liés à celle-ci.

```python
def start_listener(self, port):
    """Démarrer un écouteur sur le port spécifié"""
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.bind_ip, port))
        server.listen(5)
        
        print(f"[*] Écoute sur {self.bind_ip}:{port}")
        
        while True:
            client, addr = server.accept()
            print(f"[*] Connexion acceptée de {addr[0]}:{addr[1]}")
            
            # Gérer la connexion dans un thread séparé
            client_handler = threading.Thread(
                target=self.handle_connection,
                args=(client, addr[0], port)
            )
            client_handler.start()
            
    except Exception as e:
        print(f"Erreur lors du démarrage de l'écouteur sur le port {port}: {e}")
```

La fonction `start_listener` va démarrer le serveur et écouter sur le port fourni. Le `bind_ip` pour nous sera `0.0.0.0` ce qui indique que le serveur écoutera sur toutes les interfaces réseau.

Maintenant, nous allons gérer chaque nouvelle connexion dans un thread séparé, car il pourrait y avoir des cas où plusieurs attaquants tentent d'interagir avec le honeypot ou un script ou outil d'attaque analyse le honeypot. Si vous n'êtes pas familier avec le fonctionnement du threading, vous pouvez [consulter cet article](https://www.freecodecamp.org/news/concurrency-in-python/) qui explique le threading et la concurrency en Python.

Assurez-vous également de mettre cette fonction dans la classe principale `Honeypot`.

### Exécuter le honeypot

Maintenant, créons la fonction `main` qui démarrera notre honeypot.

```python
def main():
    honeypot = Honeypot()
    
    # Démarrer les écouteurs pour chaque port dans des threads séparés
    for port in honeypot.ports:
        listener_thread = threading.Thread(
            target=honeypot.start_listener,
            args=(port,)
        )
        listener_thread.daemon = True
        listener_thread.start()
    
    try:
        # Garder le thread principal en vie
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Arrêt du honeypot...")
        sys.exit(0)

if __name__ == "__main__":
    main()
```

Cette fonction instancie la classe `Honeypot` et démarre les écouteurs pour chacun de nos ports définis (21, 22, 80, 443) en tant que thread séparé. Maintenant, nous allons garder notre thread principal qui exécute notre programme réel en vie en le mettant dans une boucle infinie. Mettez tout cela ensemble dans un script et exécutez-le.

### Écrire le simulateur d'attaques du honeypot

Maintenant, essayons de simuler quelques scénarios d'attaque et cibler notre honeypot afin que nous puissions collecter des données dans notre fichier de journal JSON.

Ce simulateur nous aidera à démontrer quelques aspects importants concernant les honeypots :

1. Schémas d'attaque réalistes : Le simulateur simulera des schémas d'attaque courants comme le balayage de ports, les tentatives de force brute et les exploits spécifiques aux services.
    
2. Intensité variable : Le simulateur ajustera l'intensité de la simulation pour tester comment votre honeypot gère différentes charges.
    
3. Plusieurs types d'attaques : Il démontrera différents types d'attaques que des attaquants réels pourraient tenter, vous aidant à comprendre comment votre honeypot répond à chacun.
    
4. Connexions concurrentes : Le simulateur utilisera le threading pour tester comment votre honeypot gère plusieurs connexions simultanées.
    

```python
# honeypot_simulator.py

import socket
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import argparse

class HoneypotSimulator:
    """
    Une classe pour simuler différents types de connexions et d'attaques contre notre honeypot.
    Cela aide à tester les capacités de journalisation et de réponse du honeypot.
    """
    
    def __init__(self, target_ip="127.0.0.1", intensity="medium"):
        # Configuration pour le simulateur
        self.target_ip = target_ip
        self.intensity = intensity
        
        # Ports courants que les attaquants sondent souvent
        self.target_ports = [21, 22, 23, 25, 80, 443, 3306, 5432]
        
        # Dictionnaire des commandes courantes utilisées par les attaquants pour différents services
        self.attack_patterns = {
            21: [  # Commandes FTP
                "USER admin\r\n",
                "PASS admin123\r\n",
                "LIST\r\n",
                "STOR malware.exe\r\n"
            ],
            22: [  # Tentatives SSH
                "SSH-2.0-OpenSSH_7.9\r\n",
                "admin:password123\n",
                "root:toor\n"
            ],
            80: [  # Requêtes HTTP
                "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n",
                "POST /admin HTTP/1.1\r\nHost: localhost\r\nContent-Length: 0\r\n\r\n",
                "GET /wp-admin HTTP/1.1\r\nHost: localhost\r\n\r\n"
            ]
        }
        
        # Paramètres d'intensité affectant la fréquence et le volume des attaques simulées
        self.intensity_settings = {
            "low": {"max_threads": 2, "delay_range": (1, 3)},
            "medium": {"max_threads": 5, "delay_range": (0.5, 1.5)},
            "high": {"max_threads": 10, "delay_range": (0.1, 0.5)}
        }

    def simulate_connection(self, port):
        """
        Simule une tentative de connexion à un port spécifique avec des schémas d'attaque réalistes
        """
        try:
            # Créer une nouvelle connexion socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            
            print(f"[*] Tentative de connexion à {self.target_ip}:{port}")
            sock.connect((self.target_ip, port))
            
            # Obtenir la bannière si elle existe
            banner = sock.recv(1024)
            print(f"[+] Bannière reçue du port {port}: {banner.decode('utf-8', 'ignore').strip()}")
            
            # Envoyer des schémas d'attaque basés sur le port
            if port in self.attack_patterns:
                for command in self.attack_patterns[port]:
                    print(f"[*] Envoi de la commande au port {port}: {command.strip()}")
                    sock.send(command.encode())
                    
                    # Attendre la réponse
                    try:
                        response = sock.recv(1024)
                        print(f"[+] Réponse reçue: {response.decode('utf-8', 'ignore').strip()}")
                    except socket.timeout:
                        print(f"[-] Aucune réponse reçue du port {port}")
                    
                    # Ajouter un délai réaliste entre les commandes
                    time.sleep(random.uniform(*self.intensity_settings[self.intensity]["delay_range"]))
            
            sock.close()
            
        except ConnectionRefusedError:
            print(f"[-] Connexion refusée sur le port {port}")
        except socket.timeout:
            print(f"[-] Délai de connexion dépassé sur le port {port}")
        except Exception as e:
            print(f"[-] Erreur de connexion au port {port}: {e}")

    def simulate_port_scan(self):
        """
        Simule un balayage de ports de base sur les ports courants
        """
        print(f"\n[*] Début de la simulation de balayage de ports contre {self.target_ip}")
        for port in self.target_ports:
            self.simulate_connection(port)
            time.sleep(random.uniform(0.1, 0.3))

    def simulate_brute_force(self, port):
        """
        Simule une attaque par force brute contre un service spécifique
        """
        common_usernames = ["admin", "root", "user", "test"]
        common_passwords = ["password123", "admin123", "123456", "root"]
        
        print(f"\n[*] Début de la simulation de force brute contre le port {port}")
        
        for username in common_usernames:
            for password in common_passwords:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((self.target_ip, port))
                    
                    if port == 21:  # FTP
                        sock.send(f"USER {username}\r\n".encode())
                        sock.recv(1024)
                        sock.send(f"PASS {password}\r\n".encode())
                    elif port == 22:  # SSH
                        sock.send(f"{username}:{password}\n".encode())
                    
                    sock.close()
                    time.sleep(random.uniform(0.1, 0.3))
                    
                except Exception as e:
                    print(f"[-] Erreur dans la tentative de force brute: {e}")

    def run_continuous_simulation(self, duration=300):
        """
        Exécute une simulation continue pendant une durée spécifiée
        """
        print(f"\n[*] Début de la simulation continue pour {duration} secondes")
        print(f"[*] Niveau d'intensité: {self.intensity}")
        
        end_time = time.time() + duration
        
        with ThreadPoolExecutor(
            max_workers=self.intensity_settings[self.intensity]["max_threads"]
        ) as executor:
            while time.time() < end_time:
                # Mélange de différents schémas d'attaque
                simulation_choices = [
                    lambda: self.simulate_port_scan(),
                    lambda: self.simulate_brute_force(21),
                    lambda: self.simulate_brute_force(22),
                    lambda: self.simulate_connection(80)
                ]
                
                # Choisir et exécuter aléatoirement un schéma d'attaque
                executor.submit(random.choice(simulation_choices))
                time.sleep(random.uniform(*self.intensity_settings[self.intensity]["delay_range"]))

def main():
    """
    Fonction principale pour exécuter le simulateur de honeypot avec des arguments en ligne de commande
    """
    parser = argparse.ArgumentParser(description="Simulateur d'attaques de honeypot")
    parser.add_argument("--target", default="127.0.0.1", help="Adresse IP cible")
    parser.add_argument(
        "--intensity",
        choices=["low", "medium", "high"],
        default="medium",
        help="Niveau d'intensité de la simulation"
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=300,
        help="Durée de la simulation en secondes"
    )
    
    args = parser.parse_args()
    
    simulator = HoneypotSimulator(args.target, args.intensity)
    
    try:
        simulator.run_continuous_simulation(args.duration)
    except KeyboardInterrupt:
        print("\n[*] Simulation interrompue par l'utilisateur")
    except Exception as e:
        print(f"[-] Erreur de simulation: {e}")
    finally:
        print("\n[*] Simulation terminée")

if __name__ == "__main__":
    main()
```

Nous avons beaucoup de choses dans ce script de simulation, alors décomposons-le une par une. J'ai également ajouté des commentaires pour chaque fonction et opération pour rendre cela un peu plus lisible dans le code.

Nous avons d'abord notre classe utilitaire appelée `HoneypotSimulator`. Dans cette classe, nous avons la fonction `__init__` qui configure la configuration de base de notre simulateur. Elle prend deux paramètres : une adresse IP cible (par défaut [localhost](http://localhost)) et un niveau d'intensité (par défaut "medium").

Nous définissons également trois composants importants : les ports cibles à sonder (services courants comme FTP, SSH, HTTP), les schémas d'attaque spécifiques à chaque service (comme les tentatives de connexion et les commandes), et les paramètres d'intensité qui contrôlent à quel point notre simulation sera agressive à travers les comptes de threads et les délais de synchronisation.

La fonction `simulate_connection` gère les tentatives de connexion individuelles à un port spécifique. Elle crée une connexion socket, essaie d'obtenir des bannières de service (comme les informations de version SSH), puis envoie des commandes d'attaque appropriées en fonction du type de service. Nous avons ajouté une gestion des erreurs pour les problèmes réseau courants et également ajouté des délais réalistes entre les commandes pour imiter l'interaction humaine.

Notre fonction `simulate_port_scan` agit comme un outil de reconnaissance, qui vérifiera systématiquement chaque port dans notre liste de cibles. C'est similaire à la façon dont des outils comme `nmap` fonctionnent - en passant par les ports un par un pour voir quels services sont disponibles. Pour chaque port, elle appelle la fonction `simulate_connection` et ajoute de petits délais aléatoires pour rendre le schéma de balayage plus naturel.

La fonction `simulate_brute_force` maintient des listes de noms d'utilisateur et de mots de passe courants, en essayant différentes combinaisons contre des services comme FTP et SSH. Pour chaque tentative, elle crée une nouvelle connexion, envoie les informations d'identification de connexion au format correct pour ce service, puis ferme la connexion. Cela nous aide à tester à quel point le honeypot détecte et journalise les attaques par bourrage d'identifiants.

La fonction `run_continuous_simulation` s'exécute pendant une durée spécifiée, en choisissant aléatoirement entre différents types d'attaques comme le balayage de ports, la force brute ou des attaques spécifiques aux services. Elle utilise le `ThreadPoolExecutor` de Python pour exécuter plusieurs attaques simultanément en fonction du niveau d'intensité spécifié.

Enfin, nous avons la fonction `main` qui fournit l'interface de ligne de commande pour le simulateur. Elle utilise `argparse` pour gérer les arguments de ligne de commande, permettant aux utilisateurs de spécifier l'IP cible, le niveau d'intensité et la durée de la simulation. Elle crée une instance de la classe `HoneypotSimulator` et gère l'exécution globale, y compris la gestion appropriée des interruptions utilisateur et des erreurs.

Après avoir placé le code du simulateur dans un script séparé, exécutez-le avec la commande suivante :

```python
# Exécuter avec les paramètres par défaut (intensité moyenne, localhost, 5 minutes)
python honeypot_simulator.py

# Exécuter avec des paramètres personnalisés
python honeypot_simulator.py --target 192.168.1.100 --intensity high --duration 600
```

Puisque nous exécutons le honeypot ainsi que le simulateur sur la même machine localement, la cible sera `localhost`. Mais cela peut être autre chose dans un scénario réel ou si vous exécutez le honeypot dans une VM ou une machine différente - assurez-vous donc de confirmer l'IP avant d'exécuter le simulateur.

## Comment analyser les données du honeypot

Écrivons rapidement une fonction d'assistance qui nous permettra d'analyser toutes les données collectées par le honeypot. Puisque nous les avons stockées dans un fichier de journal JSON, nous pouvons les analyser commodément en utilisant le package JSON intégré.

```python
import datetime
import json

def analyze_logs(log_file):
    """Analyse avancée des journaux de honeypot avec des schémas temporels et comportementaux"""
    ip_analysis = {}
    port_analysis = {}
    hourly_attacks = {}
    data_patterns = {}
    
    # Suivre les schémas de session
    ip_sessions = {}
    attack_timeline = []
    
    with open(log_file, 'r') as f:
        for line in f:
            try:
                activity = json.loads(line)
                timestamp = datetime.datetime.fromisoformat(activity['timestamp'])
                ip = activity['remote_ip']
                port = activity['port']
                data = activity['data']
                
                # Initialiser le suivi IP si nouveau
                if ip not in ip_analysis:
                    ip_analysis[ip] = {
                        'total_attempts': 0,
                        'first_seen': timestamp,
                        'last_seen': timestamp,
                        'targeted_ports': set(),
                        'unique_payloads': set(),
                        'session_count': 0
                    }
                
                # Mettre à jour les statistiques IP
                ip_analysis[ip]['total_attempts'] += 1
                ip_analysis[ip]['last_seen'] = timestamp
                ip_analysis[ip]['targeted_ports'].add(port)
                ip_analysis[ip]['unique_payloads'].add(data.strip())
                
                # Suivre les schémas horaires
                hour = timestamp.hour
                hourly_attacks[hour] = hourly_attacks.get(hour, 0) + 1
                
                # Analyser les schémas de ciblage de port
                if port not in port_analysis:
                    port_analysis[port] = {
                        'total_attempts': 0,
                        'unique_ips': set(),
                        'unique_payloads': set()
                    }
                port_analysis[port]['total_attempts'] += 1
                port_analysis[port]['unique_ips'].add(ip)
                port_analysis[port]['unique_payloads'].add(data.strip())
                
                # Suivre les schémas de payload
                if data.strip():
                    data_patterns[data.strip()] = data_patterns.get(data.strip(), 0) + 1
                
                # Suivre la chronologie des attaques
                attack_timeline.append({
                    'timestamp': timestamp,
                    'ip': ip,
                    'port': port
                })
                
            except (json.JSONDecodeError, KeyError) as e:
                continue
    
    # Génération du rapport d'analyse
    print("\n=== Rapport d'analyse du honeypot ===")
    
    # 1. Analyse basée sur l'IP
    print("\nTop 10 des IP les plus actives:")
    sorted_ips = sorted(ip_analysis.items(), 
                       key=lambda x: x[1]['total_attempts'], 
                       reverse=True)[:10]
    for ip, stats in sorted_ips:
        duration = stats['last_seen'] - stats['first_seen']
        print(f"\nIP: {ip}")
        print(f"Total des tentatives: {stats['total_attempts']}")
        print(f"Durée active: {duration}")
        print(f"Ports uniques ciblés: {len(stats['targeted_ports'])}")
        print(f"Payloads uniques: {len(stats['unique_payloads'])}")
    
    # 2. Analyse des ports
    print("\nAnalyse du ciblage des ports:")
    sorted_ports = sorted(port_analysis.items(),
                         key=lambda x: x[1]['total_attempts'],
                         reverse=True)
    for port, stats in sorted_ports:
        print(f"\nPort {port}:")
        print(f"Total des tentatives: {stats['total_attempts']}")
        print(f"Attaquants uniques: {len(stats['unique_ips'])}")
        print(f"Payloads uniques: {len(stats['unique_payloads'])}")
    
    # 3. Analyse temporelle
    print("\nDistribution des attaques par heure:")
    for hour in sorted(hourly_attacks.keys()):
        print(f"Heure {hour:02d}: {hourly_attacks[hour]} tentatives")
    
    # 4. Analyse de la sophistication des attaques
    print("\nAnalyse de la sophistication des attaquants:")
    for ip, stats in sorted_ips:
        sophistication_score = (
            len(stats['targeted_ports']) * 0.4 +  # Diversité des ports
            len(stats['unique_payloads']) * 0.6   # Diversité des payloads
        )
        print(f"IP {ip}: Score de sophistication {sophistication_score:.2f}")
    
    # 5. Schémas de payload courants
    print("\nTop 10 des payloads les plus courants:")
    sorted_payloads = sorted(data_patterns.items(),
                            key=lambda x: x[1],
                            reverse=True)[:10]
    for payload, count in sorted_payloads:
        if len(payload) > 50:  # Tronquer les payloads longs
            payload = payload[:50] + "..."
        print(f"Compte {count}: {payload}")
```

Vous pouvez placer cela dans un fichier de script séparé et appeler la fonction sur les journaux JSON. Cette fonction nous fournira des informations complètes à partir du fichier JSON basé sur les données collectées.

Notre analyse commence par regrouper les données en plusieurs catégories comme les statistiques basées sur l'IP, les schémas de ciblage de port, les distributions d'attaques horaires et les caractéristiques des payloads. Pour chaque IP, nous suivons le nombre total de tentatives, les premiers et derniers horodatages, les ports ciblés et les payloads uniques. Cela nous aidera à construire des profils uniques pour les attaquants.

Nous examinons également les schémas d'attaque basés sur les ports ici qui surveillent les ports les plus fréquemment ciblés, et par combien d'attaquants uniques. Nous effectuons également une analyse de la sophistication des attaques qui nous aide à identifier les attaquants ciblés, en tenant compte de facteurs comme les ports ciblés et les payloads uniques utilisés. Cette analyse est utilisée pour séparer les activités de balayage simples et les attaques sophistiquées.

L'analyse temporelle nous aide à identifier les schémas dans les tentatives d'attaque horaires, révélant des schémas dans le timing des attaques et des campagnes de ciblage automatisées potentielles. Enfin, nous publions les payloads couramment vus pour identifier les chaînes ou commandes d'attaque couramment vues.

## Considérations de sécurité

Lors du déploiement de ce honeypot, assurez-vous de prendre en compte les mesures de sécurité suivantes :

1. Exécutez votre honeypot dans un environnement isolé. Typiquement à l'intérieur d'une VM, ou sur votre machine locale qui est derrière un NAT et un pare-feu.
    
2. Exécutez le honeypot avec des privilèges système minimaux (généralement pas en tant que root) pour réduire le risque en cas de compromission.
    
3. Soyez prudent avec les données collectées si vous prévoyez de les déployer un jour comme un honeypot de production ou de recherche, car elles peuvent contenir des logiciels malveillants ou des informations sensibles.
    
4. Implémentez des mécanismes de surveillance robustes pour détecter les tentatives de sortie de l'environnement du honeypot.
    

## Conclusion

Avec cela, nous avons construit notre honeypot, écrit un simulateur pour simuler des attaques pour notre honeypot et analysé les données de nos journaux de honeypot pour faire quelques inférences simples. C'est une excellente façon de comprendre à la fois les concepts de sécurité offensive et défensive. Vous pouvez envisager de construire sur cela pour créer des systèmes de détection plus complexes et penser à ajouter des fonctionnalités comme :

1. Émulation de service dynamique basée sur le comportement d'attaque
    
2. Intégration avec des systèmes de renseignement sur les menaces qui effectueront une meilleure analyse d'inférence de ces journaux de honeypot collectés
    
3. Collecter des journaux encore plus complets au-delà de l'IP, du port et des données réseau grâce à des mécanismes de journalisation avancés
    
4. Ajouter des capacités d'apprentissage automatique pour détecter les schémas d'attaque
    

N'oubliez pas que même si les honeypots sont des outils de sécurité puissants, ils doivent faire partie d'une stratégie de sécurité défensive complète, et non la seule ligne de défense.

J'espère que vous avez appris comment fonctionnent les honeypots, quel est leur but ainsi qu'un peu de programmation Python également !