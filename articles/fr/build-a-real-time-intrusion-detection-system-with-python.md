---
title: Comment construire un système de détection d'intrusion en temps réel avec Python
  et des bibliothèques open-source
subtitle: ''
author: Chaitanya Rahalkar
co_authors: []
series: null
date: '2025-01-21T14:28:32.163Z'
originalURL: https://freecodecamp.org/news/build-a-real-time-intrusion-detection-system-with-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737469496956/6cb12a90-de25-46da-aafc-bbd5048d0411.png
tags:
- name: Python
  slug: python
- name: Open Source
  slug: opensource
- name: learning
  slug: learning
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: Comment construire un système de détection d'intrusion en temps réel avec
  Python et des bibliothèques open-source
seo_desc: An Intrusion Detection System (IDS) is like a security camera for your network.
  Just as security cameras help identify suspicious activities in the physical world,
  an IDS will monitor your network to help detect any potential cyber attacks and
  securi...
---

Un système de détection d'intrusion (IDS) est comme une caméra de sécurité pour votre réseau. Tout comme les caméras de sécurité aident à identifier les activités suspectes dans le monde physique, un IDS surveillera votre réseau pour aider à détecter les potentielles cyberattaques et les violations de sécurité.

À la fin de ce tutoriel, vous saurez comment fonctionne un IDS et serez capable de construire votre propre système de surveillance de réseau en temps réel en utilisant Python.

## Table des matières

* [Comprendre les types d'IDS](#heading-comprendre-les-types-dids)
    
* [Comment installer votre environnement de développement](#heading-comment-installer-votre-environnement-de-developpement)
    
* [Construction des composants principaux de l'IDS](#heading-construction-des-composants-principaux-de-lids)
    
    * [Construction du moteur de capture de paquets](#heading-construction-du-moteur-de-capture-de-paquets)
        
    * [Construction du module d'analyse du trafic](#heading-construction-du-module-danalyse-du-trafic)
        
    * [Construction du moteur de détection](#heading-construction-du-moteur-de-detection)
        
    * [Construction du système d'alerte](#heading-construction-du-systeme-dalerte)
        
    * [Mettre le tout ensemble](#heading-mettre-le-tout-ensemble)
        
* [Idées pour étendre l'IDS](#heading-idees-pour-etendre-lids)
    
* [Considérations de sécurité](#heading-considerations-de-securite)
    
* [Test de l'IDS sur des données simulées](#heading-test-de-lids-sur-des-donnees-simulees)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre les types d'IDS

Avant de nous lancer dans la partie codage, comprenons les types d'IDS :

1. **IDS basé sur le réseau (NIDS)** : Ce système surveille le trafic réseau pour détecter les activités suspectes.
    
2. **IDS basé sur l'hôte (HIDS)** : Ce système surveille les journaux système et les changements de fichiers sur des hôtes individuels et n'est pas directement déployé dans le réseau.
    
3. **IDS basé sur les signatures** : Ce système est soit dans le réseau, soit sur l'hôte, et identifie les motifs d'attaque basés sur des motifs connus.
    
4. **IDS basé sur les anomalies** : Ce système identifie les comportements inhabituels en utilisant des heuristiques et des algorithmes de prédiction qui sont entraînés sur des motifs d'attaque précédemment observés.
    

Pour ce tutoriel, vous allez construire un système hybride qui combine les systèmes de détection basés sur les signatures et les anomalies pour surveiller le trafic réseau.

## Comment installer votre environnement de développement

Commençons par configurer notre environnement Python (j'utilise Python 3) et installer les prérequis suivants :

```bash
pip install scapy
pip install python-nmap
pip install numpy
pip install sklearn
```

## Construction des composants principaux de l'IDS

Notre IDS sera composé de quatre composants principaux :

1. Un système de capture de paquets
    
2. Un module d'analyse du trafic
    
3. Un moteur de détection
    
4. Un système d'alerte
    

### Construction du moteur de capture de paquets

Commençons par le moteur de capture de paquets. Nous utiliserons Scapy pour cela. Scapy est une bibliothèque de réseau qui permet d'effectuer des opérations réseau et liées au réseau en utilisant Python.

Tout d'abord, nous définirons notre classe `PacketCapture` qui servira de base à notre IDS.

```python
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import threading
import queue

class PacketCapture:
    def __init__(self):
        self.packet_queue = queue.Queue()
        self.stop_capture = threading.Event()
        
    def packet_callback(self, packet):
        if IP in packet and TCP in packet:
            self.packet_queue.put(packet)
    
    def start_capture(self, interface="eth0"):
        def capture_thread():
            sniff(iface=interface,
                  prn=self.packet_callback,
                  store=0,
                  stop_filter=lambda _: self.stop_capture.is_set())
        
        self.capture_thread = threading.Thread(target=capture_thread)
        self.capture_thread.start()
    
    def stop(self):
        self.stop_capture.set()
        self.capture_thread.join()
```

Prenons rapidement le temps de parcourir le code et de comprendre ce que font ces fonctions. Pour cela, vous utiliserez le threading et les files d'attente pour traiter et capturer efficacement les paquets réseau.

La méthode `init` initialise la classe en créant une `queue.Queue` pour stocker les paquets capturés et un événement de threading pour contrôler quand la capture de paquets doit s'arrêter. La méthode `packet_callback` agit comme un gestionnaire pour chaque paquet capturé et vérifie si le paquet contient à la fois des couches IP et TCP. Si c'est le cas, elle l'ajoute à la file d'attente pour un traitement ultérieur.

La méthode `start_capture` commence à capturer des paquets sur une interface spécifiée (par défaut `eth0` pour capturer des paquets à partir de l'interface Ethernet). Exécutez `ifconfig` pour comprendre les interfaces disponibles et sélectionnez l'interface appropriée dans la liste.

La fonction crée un thread séparé pour exécuter la fonction sniff de Scapy, qui surveille en continu l'interface pour les paquets. Le paramètre `stop_filter` garantit que la capture s'arrête lorsque l'événement `stop_capture` est déclenché.

La méthode `stop` arrête la capture en définissant l'événement `stop_capture` et attend que le thread termine son exécution, garantissant que le processus se termine proprement. Cette conception permet une capture de paquets en temps réel sans bloquer le thread principal.

### Construction du module d'analyse du trafic

Maintenant, écrivons le module d'analyse du trafic. Ce module traitera les paquets capturés et extraira les caractéristiques pertinentes.

```python
class TrafficAnalyzer:
    def __init__(self):
        self.connections = defaultdict(list)
        self.flow_stats = defaultdict(lambda: {
            'packet_count': 0,
            'byte_count': 0,
            'start_time': None,
            'last_time': None
        })
    
    def analyze_packet(self, packet):
        if IP in packet and TCP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport
            
            flow_key = (ip_src, ip_dst, port_src, port_dst)
            
            # Mettre à jour les statistiques de flux
            stats = self.flow_stats[flow_key]
            stats['packet_count'] += 1
            stats['byte_count'] += len(packet)
            current_time = packet.time
            
            if not stats['start_time']:
                stats['start_time'] = current_time
            stats['last_time'] = current_time
            
            return self.extract_features(packet, stats)
    
    def extract_features(self, packet, stats):
        return {
            'packet_size': len(packet),
            'flow_duration': stats['last_time'] - stats['start_time'],
            'packet_rate': stats['packet_count'] / (stats['last_time'] - stats['start_time']),
            'byte_rate': stats['byte_count'] / (stats['last_time'] - stats['start_time']),
            'tcp_flags': packet[TCP].flags,
            'window_size': packet[TCP].window
        }
```

Dans cette section de code, nous définissons la classe `TrafficAnalyzer` pour analyser le trafic réseau. Ici, nous suivons les flux de connexion et calculons les statistiques des paquets en temps réel. Nous utilisons la structure de données `defaultdict` en Python pour gérer les connexions et les statistiques de flux en organisant les données par flux uniques.

La méthode `__init__` initialise deux attributs : `connections`, qui stocke des listes de paquets liés pour chaque flux, et `flow_stats`, qui stocke les statistiques agrégées pour chaque flux, telles que le nombre de paquets, le nombre d'octets, l'heure de début et l'heure du paquet le plus récent.

La méthode `analyze_packet` traite chaque paquet. Si le paquet contient des couches IP et TCP, elle extrait les adresses IP source et destination ainsi que les ports, formant une `flow_key` unique pour identifier le flux. Elle met à jour les statistiques du flux en incrémentant le nombre de paquets, en ajoutant la taille du paquet au nombre d'octets, et en définissant ou en mettant à jour l'heure de début et la dernière heure du flux. Finalement, elle appelle `extract_features` pour calculer et retourner des métriques supplémentaires.

La méthode `extract_features` calcule les caractéristiques détaillées du flux et du paquet actuel. Celles-ci incluent la taille du paquet, la durée du flux, le taux de paquets, le taux d'octets, les flags TCP et la taille de la fenêtre TCP. Ces métriques sont très utiles pour identifier les motifs, les anomalies ou les menaces potentielles dans le trafic réseau.

### Construction du moteur de détection

Maintenant, nous allons définir notre moteur de détection qui implémentera à la fois les mécanismes de détection basés sur les signatures et les anomalies :

```python
from sklearn.ensemble import IsolationForest
import numpy as np

class DetectionEngine:
    def __init__(self):
        self.anomaly_detector = IsolationForest(
            contamination=0.1,
            random_state=42
        )
        self.signature_rules = self.load_signature_rules()
        self.training_data = []
    
    def load_signature_rules(self):
        return {
            'syn_flood': {
                'condition': lambda features: (
                    features['tcp_flags'] == 2 and  # SYN flag
                    features['packet_rate'] > 100
                )
            },
            'port_scan': {
                'condition': lambda features: (
                    features['packet_size'] < 100 and
                    features['packet_rate'] > 50
                )
            }
        }
    
    def train_anomaly_detector(self, normal_traffic_data):
        self.anomaly_detector.fit(normal_traffic_data)
    
    def detect_threats(self, features):
        threats = []
        
        # Détection basée sur les signatures
        for rule_name, rule in self.signature_rules.items():
            if rule['condition'](features):
                threats.append({
                    'type': 'signature',
                    'rule': rule_name,
                    'confidence': 1.0
                })
        
        # Détection basée sur les anomalies
        feature_vector = np.array([[
            features['packet_size'],
            features['packet_rate'],
            features['byte_rate']
        ]])
        
        anomaly_score = self.anomaly_detector.score_samples(feature_vector)[0]
        if anomaly_score < -0.5:  # Seuil pour la détection d'anomalies
            threats.append({
                'type': 'anomaly',
                'score': anomaly_score,
                'confidence': min(1.0, abs(anomaly_score))
            })
        
        return threats
```

Ce code définit un système hybride qui combine les méthodes de détection basées sur les signatures et les anomalies. Nous utilisons le modèle Isolation Forest pour détecter les anomalies et utilisons également des règles prédéfinies pour identifier des motifs d'attaque spécifiques. Si vous souhaitez en savoir plus sur le fonctionnement du modèle Isolation Forest, consultez [cet](https://medium.com/@corymaklin/isolation-forest-799fceacdda4) article.

Dans cet extrait de code, la méthode `train_anomaly_detector` entraîne le modèle Isolation Forest en utilisant un ensemble de données de caractéristiques de trafic normal. Cela permet au modèle de différencier les motifs de trafic typiques des anomalies.

La méthode `detect_threats` évalue les caractéristiques du trafic réseau pour détecter les menaces potentielles en utilisant deux approches :

1. **Détection basée sur les signatures** : Elle parcourt chaque règle prédéfinie, appliquant la condition de la règle aux caractéristiques du trafic. Si une règle correspond, une menace basée sur la signature est enregistrée avec une confiance élevée.
    
2. **Détection basée sur les anomalies** : Elle traite le vecteur de caractéristiques (taille du paquet, taux de paquets et taux d'octets) à travers le modèle Isolation Forest pour calculer un score d'anomalie. Si le score indique un comportement inhabituel, le moteur de détection le déclenche comme une anomalie et produit un score de confiance proportionnel à la gravité de l'anomalie.
    

Enfin, nous retournons la liste agrégée des menaces identifiées avec leurs annotations respectives (signature ou anomalie), la règle ou le score qui a déclenché l'anomalie, et un score de confiance qui suggère la probabilité que le motif identifié soit une menace.

### Construction du système d'alerte

Maintenant, construisons le dernier composant de notre IDS, qui est le système d'alerte. Il traitera et journalisera les menaces détectées de manière structurée. Vous aurez également la possibilité d'étendre le système pour inclure des mécanismes de notification supplémentaires comme Slack, des tickets Jira, etc.

```python
import logging
import json
from datetime import datetime

class AlertSystem:
    def __init__(self, log_file="ids_alerts.log"):
        self.logger = logging.getLogger("IDS_Alerts")
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def generate_alert(self, threat, packet_info):
        alert = {
            'timestamp': datetime.now().isoformat(),
            'threat_type': threat['type'],
            'source_ip': packet_info.get('source_ip'),
            'destination_ip': packet_info.get('destination_ip'),
            'confidence': threat.get('confidence', 0.0),
            'details': threat
        }
        
        self.logger.warning(json.dumps(alert))
        
        if threat['confidence'] > 0.8:
            self.logger.critical(
                f"High confidence threat detected: {json.dumps(alert)}"
            )
            # Implémenter des méthodes de notification supplémentaires ici
            # (par exemple, email, Slack, intégration SIEM)
```

La méthode `init` configure un logger nommé `IDS_Alerts` avec un niveau de journalisation `INFO` pour capturer les informations d'alerte. Il écrit les logs dans un fichier spécifié, `ids_alerts.log` par défaut. Un `FileHandler` dirige les logs vers le fichier, tandis que le `Formatter` garantit que les logs suivent un format cohérent.

La méthode `generate_alert` est responsable de la création d'entrées d'alerte structurées. Chaque alerte inclut des informations clés telles que l'horodatage de la détection, le type de menace, les adresses IP source et destination impliquées, le niveau de confiance de la détection et des détails spécifiques à la menace. Ces alertes sont journalisées en tant que messages de niveau `WARNING` au format JSON.

Si le niveau de confiance d'une menace détectée est élevé (supérieur à 0,8), l'alerte est escaladée et journalisée en tant que message de niveau `CRITICAL`. Notez que cette méthode est conçue pour être extensible, permettant des mécanismes de notification supplémentaires, tels que l'envoi d'alertes par email ou l'intégration avec des systèmes tiers comme Slack ou des solutions SIEM.

### Mettre le tout ensemble

Maintenant, intégrons tous les composants dans notre solution IDS entièrement fonctionnelle :

```python
class IntrusionDetectionSystem:
    def __init__(self, interface="eth0"):
        self.packet_capture = PacketCapture()
        self.traffic_analyzer = TrafficAnalyzer()
        self.detection_engine = DetectionEngine()
        self.alert_system = AlertSystem()
        
        self.interface = interface
    
    def start(self):
        print(f"Démarrage de l'IDS sur l'interface {self.interface}")
        self.packet_capture.start_capture(self.interface)
        
        while True:
            try:
                packet = self.packet_capture.packet_queue.get(timeout=1)
                features = self.traffic_analyzer.analyze_packet(packet)
                
                if features:
                    threats = self.detection_engine.detect_threats(features)
                    
                    for threat in threats:
                        packet_info = {
                            'source_ip': packet[IP].src,
                            'destination_ip': packet[IP].dst,
                            'source_port': packet[TCP].sport,
                            'destination_port': packet[TCP].dport
                        }
                        self.alert_system.generate_alert(threat, packet_info)
            
            except queue.Empty:
                continue
            except KeyboardInterrupt:
                print("Arrêt de l'IDS...")
                self.packet_capture.stop()
                break

if __name__ == "__main__":
    ids = IntrusionDetectionSystem()
    ids.start()
```

Dans ce code, la classe `IntrusionDetectionSystem` configure ses composants principaux : `PacketCapture` pour capturer les paquets à partir d'une interface réseau, `TrafficAnalyzer` pour extraire et analyser les caractéristiques des paquets, `DetectionEngine` pour identifier les menaces en utilisant des méthodes basées sur les signatures et les anomalies, et `AlertSystem` pour journaliser et escalader les menaces détectées. Le paramètre d'interface spécifie l'interface réseau à surveiller, par défaut `eth0` (l'interface Ethernet généralement nommée sur la plupart des systèmes).

La fonction `start` initie l'IDS. Elle commence par démarrer la capture de paquets sur l'interface spécifiée et entre dans une boucle pour traiter en continu les paquets entrants. Pour chaque paquet capturé, le système extrait ses caractéristiques en utilisant le `TrafficAnalyzer` et les analyse pour détecter les menaces potentielles en utilisant le `DetectionEngine`. Si des menaces sont détectées, le système génère des alertes détaillées via le `AlertSystem`.

Le système fonctionne en boucle jusqu'à ce qu'il soit interrompu par l'une des deux exceptions clés : `queue.Empty`, qui se produit si aucun paquet n'est disponible pour le traitement, et `KeyboardInterrupt`, qui arrête l'IDS proprement en stoppant la capture de paquets et en quittant la boucle.

## Idées pour étendre l'IDS

Pour améliorer ou étendre l'IDS, vous pouvez envisager de concevoir ou d'implémenter les fonctionnalités/améliorations suivantes :

1. **Améliorations de l'apprentissage automatique** : Vous pouvez améliorer les capacités de l'IDS en incorporant des modèles de deep learning comme les Auto-Encodeurs pour la détection d'anomalies et en utilisant des RNN pour l'analyse de motifs séquentiels. Cela améliorera la capacité du système à identifier les menaces complexes et évolutives en tirant parti de l'ingénierie des caractéristiques avancées.
    
2. **Optimisations de performance** : Vous pouvez optimiser l'IDS en utilisant PyPy pour une exécution plus rapide, l'échantillonnage de paquets pour gérer les réseaux à fort trafic, et le traitement parallèle pour mettre à l'échelle le système efficacement.
    
3. **Capacités d'intégration** : Vous pouvez étendre l'IDS en considérant le support d'une API REST pour la surveillance à distance, permettant une interaction transparente avec des systèmes externes.
    

## Considérations de sécurité

Lors du déploiement de l'IDS, notez que le système est une preuve de concept et n'est pas destiné à des cas d'utilisation en production. Gardez également à l'esprit les points suivants :

* Exécutez le système avec les permissions appropriées (root/admin requis pour la capture de paquets)
    
* Sécurisez les journaux d'alertes et implémentez une rotation de logs appropriée
    
* Mettez régulièrement à jour les règles de signature et réentraînez les modèles de détection d'anomalies
    
* Surveillez l'utilisation des ressources système, en particulier dans les environnements à fort trafic
    
* Implémentez des contrôles d'accès appropriés pour la configuration de l'IDS et les alertes
    

## Test de l'IDS sur des données simulées

Pour valider la fonctionnalité de votre IDS, vous pouvez le tester en utilisant des données simulées qui simuleront le trafic réseau du monde réel. Cela vous permettra d'observer comment le système traite les paquets, analyse le trafic et génère des alertes sans nécessiter un environnement réseau en direct.

Utilisez la fonction suivante pour tester l'IDS :

```python
from scapy.all import IP, TCP

def test_ids():
    # Créer des paquets de test pour simuler divers scénarios
    test_packets = [
        # Trafic normal
        IP(src="192.168.1.1", dst="192.168.1.2") / TCP(sport=1234, dport=80, flags="A"),
        IP(src="192.168.1.3", dst="192.168.1.4") / TCP(sport=1235, dport=443, flags="P"),
        
        # Simulation d'une attaque SYN flood
        IP(src="10.0.0.1", dst="192.168.1.2") / TCP(sport=5678, dport=80, flags="S"),
        IP(src="10.0.0.2", dst="192.168.1.2") / TCP(sport=5679, dport=80, flags="S"),
        IP(src="10.0.0.3", dst="192.168.1.2") / TCP(sport=5680, dport=80, flags="S"),
        
        # Simulation d'un scan de ports
        IP(src="192.168.1.100", dst="192.168.1.2") / TCP(sport=4321, dport=22, flags="S"),
        IP(src="192.168.1.100", dst="192.168.1.2") / TCP(sport=4321, dport=23, flags="S"),
        IP(src="192.168.1.100", dst="192.168.1.2") / TCP(sport=4321, dport=25, flags="S"),
    ]
    
    ids = IntrusionDetectionSystem()
    
    # Simuler le traitement des paquets et la détection des menaces
    print("Démarrage du test de l'IDS...")
    for i, packet in enumerate(test_packets, 1):
        print(f"\nTraitement du paquet {i}: {packet.summary()}")
        
        # Analyser le paquet
        features = ids.traffic_analyzer.analyze_packet(packet)
        
        if features:
            # Détecter les menaces basées sur les caractéristiques
            threats = ids.detection_engine.detect_threats(features)
            
            if threats:
                print(f"Menaces détectées: {threats}")
            else:
                print("Aucune menace détectée.")
        else:
            print("Le paquet ne contient pas de couches IP/TCP ou est ignoré.")
    
    print("\nTest de l'IDS terminé.")

if __name__ == "__main__":
    test_ids()
```

Cela testera le système contre une variété d'attaques comme les inondations SYN et les scans de ports.

## Conclusion

Maintenant, vous savez comment construire un système de détection d'intrusion de base avec Python et quelques bibliothèques open-source ! Cet IDS démontre certains concepts de base de la sécurité réseau et de la détection de menaces en temps réel.

Gardez à l'esprit que ce tutoriel est à des fins éducatives uniquement. Il existe des systèmes professionnels conçus pour les entreprises comme Snort et Suricata qui peuvent gérer des menaces avancées et des déploiements à grande échelle.

J'espère que vous avez acquis des connaissances sur les fondamentaux de la sécurité réseau et appris comment Python peut être utilisé pour construire des solutions de sécurité pratiques.