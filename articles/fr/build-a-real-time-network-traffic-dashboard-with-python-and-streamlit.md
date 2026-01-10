---
title: Comment créer un tableau de bord de trafic réseau en temps réel avec Python
  et Streamlit
subtitle: ''
author: Chaitanya Rahalkar
co_authors: []
series: null
date: '2025-01-03T23:08:28.724Z'
originalURL: https://freecodecamp.org/news/build-a-real-time-network-traffic-dashboard-with-python-and-streamlit
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1735280432228/33730b4a-6424-48b0-a7bf-ef029663fb90.png
tags:
- name: Python
  slug: python
- name: networking
  slug: networking
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: Comment créer un tableau de bord de trafic réseau en temps réel avec Python
  et Streamlit
seo_desc: Have you ever wanted to visualize your network traffic in real-time? In
  this tutorial, you will be learning how to build an interactive network traffic
  analysis dashboard with Python and Streamlit. Streamlit is an open-source Python
  framework you can...
---

Avez-vous déjà voulu visualiser votre trafic réseau en temps réel ? Dans ce tutoriel, vous apprendrez à créer un tableau de bord interactif d'analyse du trafic réseau avec Python et `Streamlit`. `Streamlit` est un framework Python open-source que vous pouvez utiliser pour développer des applications web pour l'analyse de données et le traitement de données.

À la fin de ce tutoriel, vous saurez comment capturer des paquets réseau bruts à partir de la carte réseau (NIC) de votre ordinateur, traiter les données et créer de belles visualisations qui se mettront à jour en temps réel.

## Table des matières

* [Pourquoi l'analyse du trafic réseau est-elle importante ?](#heading-pourquoi-lanalyse-du-trafic-reseau-est-elle-importante)
    
* [Prérequis](#heading-prerequis)
    
* [Comment installer votre projet](#heading-comment-installer-votre-projet)
    
* [Comment construire les fonctionnalités principales](#heading-comment-construire-les-fonctionnalites-principales)
    
* [Comment créer les visualisations Streamlit](#heading-comment-creer-les-visualisations-streamlit)
    
* [Comment capturer les paquets réseau](#heading-comment-capturer-les-paquets-reseau)
    
* [Mettre tout ensemble](#heading-mettre-tout-ensemble)
    
* [Améliorations futures](#heading-ameliorations-futures)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi l'analyse du trafic réseau est-elle importante ?

L'analyse du trafic réseau est une exigence critique dans les entreprises où les réseaux forment l'épine dorsale de presque toutes les applications et services. Au cœur de cela, nous avons l'analyse des paquets réseau qui implique la surveillance du réseau, la capture de tout le trafic (entrant et sortant), et l'interprétation de ces paquets lorsqu'ils circulent à travers un réseau. Vous pouvez utiliser cette technique pour identifier les motifs de sécurité, détecter les anomalies et assurer la sécurité et l'efficacité du réseau.

Ce projet de preuve de concept sur lequel nous travaillerons dans ce tutoriel est particulièrement utile car il vous aide à visualiser et à analyser l'activité du réseau en temps réel. Et cela vous permettra de comprendre comment le dépannage des problèmes, les optimisations de performance et l'analyse de sécurité sont effectués dans les systèmes d'entreprise.

## Prérequis

* Python 3.8 ou une version plus récente installée sur votre système.
    
* Une compréhension de base des [concepts de mise en réseau informatique](https://www.freecodecamp.org/news/computer-networking-how-applications-talk-over-the-internet/).
    
* Familiarité avec le [langage de programmation Python](https://www.freecodecamp.org/news/ultimate-beginners-python-course/) et ses bibliothèques largement utilisées.
    
* Connaissance de base des techniques et bibliothèques de [visualisation de données](https://www.freecodecamp.org/news/learn-data-visualization-in-this-free-17-hour-course/).
    

## Comment installer votre projet

Pour commencer, créez la structure du projet et installez les outils nécessaires avec Pip avec les commandes suivantes :

```bash
mkdir network-dashboard
cd network-dashboard
pip install streamlit pandas scapy plotly
```

Nous utiliserons `Streamlit` pour les visualisations du tableau de bord, `Pandas` pour le traitement des données, `Scapy` pour la capture et le traitement des paquets réseau, et enfin `Plotly` pour tracer des graphiques avec nos données collectées.

## Comment construire les fonctionnalités principales

Nous mettrons tout le code dans un seul fichier nommé `dashboard.py`. Commençons d'abord par importer tous les éléments que nous utiliserons :

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scapy.all import *
from collections import defaultdict
import time
from datetime import datetime
import threading
import warnings
import logging
from typing import Dict, List, Optional
import socket
```

Configurons maintenant le logging en mettant en place une configuration de logging de base. Cela sera utilisé pour suivre les événements et exécuter notre application en mode debug. Nous avons actuellement défini le niveau de logging à `INFO`, ce qui signifie que les événements de niveau `INFO` ou supérieur seront affichés. Si vous n'êtes pas familier avec le logging en Python, je vous recommande de consulter [cette](https://docs.python.org/3/library/logging.html) documentation qui entre dans les détails.

```python
# Configurer le logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

Ensuite, nous allons construire notre processeur de paquets. Nous implémenterons la fonctionnalité de traitement de nos paquets capturés dans cette classe.

```python
class PacketProcessor:
    """Traiter et analyser les paquets réseau"""
    
    def __init__(self):
        self.protocol_map = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP'
        }
        self.packet_data = []
        self.start_time = datetime.now()
        self.packet_count = 0
        self.lock = threading.Lock()
        
    def get_protocol_name(self, protocol_num: int) -> str:
        """Convertir le numéro de protocole en nom"""
        return self.protocol_map.get(protocol_num, f'AUTRE({protocol_num})')
    
    def process_packet(self, packet) -> None:
        """Traiter un seul paquet et extraire les informations pertinentes"""
        try:
            if IP in packet:
                with self.lock:
                    packet_info = {
                        'timestamp': datetime.now(),
                        'source': packet[IP].src,
                        'destination': packet[IP].dst,
                        'protocol': self.get_protocol_name(packet[IP].proto),
                        'size': len(packet),
                        'time_relative': (datetime.now() - self.start_time).total_seconds()
                    }
                    
                    # Ajouter des informations spécifiques à TCP
                    if TCP in packet:
                        packet_info.update({
                            'src_port': packet[TCP].sport,
                            'dst_port': packet[TCP].dport,
                            'tcp_flags': packet[TCP].flags
                        })
                    
                    # Ajouter des informations spécifiques à UDP
                    elif UDP in packet:
                        packet_info.update({
                            'src_port': packet[UDP].sport,
                            'dst_port': packet[UDP].dport
                        })
                    
                    self.packet_data.append(packet_info)
                    self.packet_count += 1
                    
                    # Conserver uniquement les 10000 derniers paquets pour éviter les problèmes de mémoire
                    if len(self.packet_data) > 10000:
                        self.packet_data.pop(0)
                        
        except Exception as e:
            logger.error(f"Erreur lors du traitement du paquet : {str(e)}")
    
    def get_dataframe(self) -> pd.DataFrame:
        """Convertir les données de paquets en DataFrame pandas"""
        with self.lock:
            return pd.DataFrame(self.packet_data)
```

Cette classe construira notre fonctionnalité principale et dispose de plusieurs fonctions utilitaires qui seront utilisées pour traiter les paquets.

Les paquets réseau sont catégorisés en deux au niveau transport (TCP et UDP) et le protocole ICMP au niveau réseau. Si vous n'êtes pas familier avec les concepts de TCP/IP, je vous recommande de consulter [cet](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/) article sur freeCodeCamp News.

Notre constructeur suivra tous les paquets vus qui sont catégorisés dans ces types de protocoles TCP/IP que nous avons définis. Nous noterons également l'heure de capture des paquets, les données capturées et le nombre de paquets capturés.

Nous utiliserons également un verrou de thread pour nous assurer qu'un seul paquet est traité à la fois. Cela peut être étendu pour permettre au projet d'avoir un traitement de paquets en parallèle.

La fonction utilitaire `get_protocol_name` nous aide à obtenir le type correct du protocole en fonction de leurs numéros de protocole. Pour donner un peu de contexte, l'Internet Assigned Numbers Authority (IANA) attribue des numéros standardisés pour identifier différents protocoles dans un paquet réseau. Lorsque nous voyons ces numéros dans le paquet réseau analysé, nous saurons quel type de protocole est utilisé dans le paquet actuellement intercepté. Pour le cadre de ce projet, nous mapperons uniquement TCP, UDP et ICMP (Ping). Si nous rencontrons un autre type de paquet, nous le catégoriserons comme `AUTRE(<protocol_num>)`.

La fonction `process_packet` gère notre fonctionnalité principale qui traitera ces paquets individuels. Si le paquet contient une couche IP, il notera les adresses IP source et de destination, le type de protocole, la taille du paquet et le temps écoulé depuis le début de la capture des paquets.

Pour les paquets avec des protocoles de couche transport spécifiques (comme TCP et UDP), nous capturerons les ports source et de destination ainsi que les flags TCP pour les paquets TCP. Ces détails extraits seront stockés en mémoire dans la liste `packet_data`. Nous suivrons également le `packet_count` au fur et à mesure que ces paquets sont traités.

La fonction `get_dataframe` nous aide à convertir la liste `packet_data` en un `DataFrame` `Pandas` qui sera ensuite utilisé pour notre visualisation.

## Comment créer les visualisations Streamlit

Il est maintenant temps pour nous de construire notre tableau de bord Streamlit interactif. Nous définirons une fonction appelée `create_visualization` dans le script `dashboard.py` (en dehors de notre classe de traitement de paquets).

```python
def create_visualizations(df: pd.DataFrame):
    """Créer toutes les visualisations du tableau de bord"""
    if len(df) > 0:
        # Répartition des protocoles
        protocol_counts = df['protocol'].value_counts()
        fig_protocol = px.pie(
            values=protocol_counts.values,
            names=protocol_counts.index,
            title="Répartition des protocoles"
        )
        st.plotly_chart(fig_protocol, use_container_width=True)
        
        # Chronologie des paquets
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df_grouped = df.groupby(df['timestamp'].dt.floor('S')).size()
        fig_timeline = px.line(
            x=df_grouped.index,
            y=df_grouped.values,
            title="Paquets par seconde"
        )
        st.plotly_chart(fig_timeline, use_container_width=True)
        
        # Top des adresses IP source
        top_sources = df['source'].value_counts().head(10)
        fig_sources = px.bar(
            x=top_sources.index,
            y=top_sources.values,
            title="Top des adresses IP source"
        )
        st.plotly_chart(fig_sources, use_container_width=True)
```

Cette fonction prendra le data frame en entrée et nous aidera à tracer trois graphiques :

1. Graphique de répartition des protocoles : Ce graphique affichera la proportion des différents protocoles (par exemple, TCP, UDP, ICMP) dans le trafic de paquets capturés.
    
2. Graphique de chronologie des paquets : Ce graphique montrera le nombre de paquets traités par seconde sur une période de temps.
    
3. Graphique des principales adresses IP source : Ce graphique mettra en évidence les 10 principales adresses IP qui ont envoyé le plus de paquets dans le trafic capturé.
    

Le graphique de répartition des protocoles est simplement un graphique en secteurs des comptes de protocoles pour les trois différents types (ainsi que AUTRE). Nous utilisons les outils Python `Streamlit` et `Plotly` pour tracer ces graphiques. Puisque nous avons également noté l'horodatage depuis le début de la capture des paquets, nous utiliserons ces données pour tracer la tendance des paquets capturés au fil du temps.

Pour le deuxième graphique, nous effectuerons une opération `groupby` sur les données et obtiendrons le nombre de paquets capturés chaque seconde (`S` signifie secondes), puis nous tracerons enfin le graphique.

Enfin, pour le troisième graphique, nous compterons les IP source distinctes observées et tracerons un graphique des comptes d'IP pour montrer les 10 principales IP.

## Comment capturer les paquets réseau

Maintenant, construisons la fonctionnalité pour nous permettre de capturer les données des paquets réseau.

```python
def start_packet_capture():
    """Démarrer la capture de paquets dans un thread séparé"""
    processor = PacketProcessor()
    
    def capture_packets():
        sniff(prn=processor.process_packet, store=False)
    
    capture_thread = threading.Thread(target=capture_packets, daemon=True)
    capture_thread.start()
    
    return processor
```

Il s'agit d'une fonction simple qui instancie la classe `PacketProcessor` puis utilise la fonction `sniff` dans le module `scapy` pour commencer à capturer les paquets.

Nous utilisons le threading ici pour nous permettre de capturer les paquets indépendamment du flux principal du programme. Cela garantit que l'opération de capture des paquets ne bloque pas les autres opérations comme la mise à jour du tableau de bord en temps réel. Nous retournons également l'instance `PacketProcessor` créée afin qu'elle puisse être utilisée dans notre programme principal.

## Mettre tout ensemble

Maintenant, assemblons toutes ces pièces avec notre fonction `main` qui agira comme la fonction pilote de notre programme.

```python
def main():
    """Fonction principale pour exécuter le tableau de bord"""
    st.set_page_config(page_title="Analyse du trafic réseau", layout="wide")
    st.title("Analyse du trafic réseau en temps réel")
    
    # Initialiser le processeur de paquets dans l'état de session
    if 'processor' not in st.session_state:
        st.session_state.processor = start_packet_capture()
        st.session_state.start_time = time.time()
    
    # Créer la disposition du tableau de bord
    col1, col2 = st.columns(2)
    
    # Obtenir les données actuelles
    df = st.session_state.processor.get_dataframe()
    
    # Afficher les métriques
    with col1:
        st.metric("Total des paquets", len(df))
    with col2:
        duration = time.time() - st.session_state.start_time
        st.metric("Durée de la capture", f"{duration:.2f}s")
    
    # Afficher les visualisations
    create_visualizations(df)
    
    # Afficher les paquets récents
    st.subheader("Paquets récents")
    if len(df) > 0:
        st.dataframe(
            df.tail(10)[['timestamp', 'source', 'destination', 'protocol', 'size']],
            use_container_width=True
        )
    
    # Ajouter un bouton de rafraîchissement
    if st.button('Rafraîchir les données'):
        st.rerun()
    
    # Rafraîchissement automatique
    time.sleep(2)
    st.rerun()
```

Cette fonction instanciera également le tableau de bord `Streamlit` et intégrera tous nos composants ensemble. Nous définissons d'abord le titre de la page de notre tableau de bord `Streamlit`, puis nous initialisons notre `PacketProcessor`. Nous utilisons l'état de session dans `Streamlit` pour nous assurer qu'une seule instance de capture de paquets est créée et que son état est conservé.

Maintenant, nous obtiendrons dynamiquement le data frame à partir de l'état de session chaque fois que les données sont traitées et commencerons à afficher les métriques et les visualisations. Nous afficherons également les paquets récemment capturés ainsi que des informations comme l'horodatage, les IP source et de destination, le protocole et la taille du paquet. Nous ajouterons également la possibilité pour l'utilisateur de rafraîchir manuellement les données à partir du tableau de bord tout en les rafraîchissant automatiquement toutes les deux secondes.

Exécutons enfin le programme avec la commande suivante :

```bash
sudo streamlit run dashboard.py
```

Notez que vous devrez exécuter le programme avec `sudo` car les capacités de capture de paquets nécessitent des privilèges administratifs. Si vous êtes sous Windows, ouvrez votre terminal en tant qu'administrateur, puis exécutez le programme sans le préfixe `sudo`.

Laissez un moment au programme pour commencer à capturer les paquets. Si tout se passe bien, vous devriez voir quelque chose comme ceci :

![Un tableau de bord d'analyse du trafic réseau montre un graphique en secteurs avec la répartition des protocoles : TCP (48,7%), UDP (47,5%) et ICMP (3,8%). En dessous se trouve un graphique en ligne affichant les paquets par seconde au fil du temps avec plusieurs pics notables. Le nombre total de paquets est de 6743, et la durée de capture est de 118,63 secondes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735279281523/34802db4-7982-4c0f-a591-c2d5ca1e1f08.png align="center")

![Un tableau de bord à thème sombre montrant un graphique à barres des principales adresses IP source et un tableau des paquets récents avec des détails comme l'horodatage, la source, la destination, le protocole et la taille.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735279285726/246a5af6-2d15-49fa-9132-8103be79ce3a.png align="center")

Ce sont toutes les visualisations que nous venons d'implémenter dans notre programme de tableau de bord `Streamlit`.

## Améliorations futures

Avec cela, voici quelques idées d'améliorations futures que vous pouvez utiliser pour étendre les fonctionnalités du tableau de bord :

1. Ajouter des capacités de machine learning pour la détection d'anomalies
    
2. Implémenter un mappage géographique des IP
    
3. Créer des alertes personnalisées basées sur des motifs d'analyse de trafic
    
4. Ajouter des options d'analyse de charge utile de paquets
    

## Conclusion

Félicitations ! Vous avez maintenant réussi à créer un tableau de bord d'analyse du trafic réseau en temps réel avec Python et `Streamlit`. Ce programme fournira des informations précieuses sur le comportement du réseau et peut être étendu pour divers cas d'utilisation, de la surveillance de la sécurité à l'optimisation du réseau.

Avec cela, j'espère que vous avez appris quelques bases sur l'analyse du trafic réseau ainsi qu'un peu de programmation Python. Merci d'avoir lu !