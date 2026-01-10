---
title: Comment créer un système SIEM Python utilisant l'IA et les LLMs pour l'analyse
  des logs et la détection d'anomalies
subtitle: ''
author: Chaitanya Rahalkar
co_authors: []
series: null
date: '2025-03-07T17:28:11.555Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-python-siem-system-using-ai-and-llms
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741368457380/900d7d5b-cffc-4175-b5a5-4d7361ea383d.png
tags:
- name: Python
  slug: python
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: AI
  slug: ai
- name: llm
  slug: llm
seo_title: Comment créer un système SIEM Python utilisant l'IA et les LLMs pour l'analyse
  des logs et la détection d'anomalies
seo_desc: 'In this tutorial, we’ll build a simplified, AI-flavored SIEM log analysis
  system using Python. Our focus will be on log analysis and anomaly detection.

  We’ll walk through ingesting logs, detecting anomalies with a lightweight machine
  learning model, ...'
---

Dans ce tutoriel, nous allons construire un système simplifié d'analyse de logs SIEM avec une touche d'IA en utilisant Python. Notre focus sera sur l'analyse des logs et la détection d'anomalies.

Nous allons parcourir l'ingestion des logs, la détection d'anomalies avec un modèle léger de machine learning, et même aborder comment le système pourrait répondre automatiquement.

Cette preuve de concept pratique illustrera comment l'IA peut améliorer la surveillance de la sécurité de manière pratique et accessible.

## Table des matières

* [Qu'est-ce que les systèmes SIEM ?](#heading-quest-ce-que-les-systemes-siem)
    
* [Prérequis](#heading-prerequis)
    
* [Installation du projet](#heading-installation-du-projet)
    
* [Comment implémenter l'analyse des logs](#heading-comment-implementer-lanalyse-des-logs)
    
* [Comment construire le modèle de détection d'anomalies](#heading-comment-construire-le-modele-de-detection-danomalies)
    
* [Test et visualisation des résultats](#heading-test-et-visualisation-des-resultats)
    
* [Possibilités de réponse automatisée](#heading-possibilites-de-reponse-automatisee)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que les systèmes SIEM ?

Les systèmes de gestion des informations et des événements de sécurité (SIEM) sont le système nerveux central des opérations de sécurité modernes. Un SIEM agrège et corrèle les logs et événements de sécurité à travers un environnement IT pour fournir des insights en temps réel sur les incidents potentiels. Cela aide les organisations à détecter les menaces plus rapidement et à répondre plus tôt.

Ces systèmes rassemblent d'énormes volumes de données de logs — des alertes de pare-feu aux logs d'applications — et les analysent pour détecter des signes de problèmes. La détection d'anomalies dans ce contexte est cruciale, et des motifs inhabituels dans les logs peuvent révéler des incidents qui pourraient échapper aux règles statiques. Par exemple, une augmentation soudaine des requêtes réseau pourrait indiquer une attaque DDoS, tandis que plusieurs tentatives de connexion échouées pourraient pointer vers des tentatives d'accès non autorisées.

L'IA fait passer les capacités des SIEM à un niveau supérieur. En exploitant des modèles d'IA avancés (comme les grands modèles de langage), un SIEM alimenté par l'IA peut analyser et interpréter intelligemment les logs, apprendre ce à quoi ressemble un comportement "normal", et signaler les éléments "bizarres" qui méritent attention.

En essence, l'IA peut agir comme un co-pilote intelligent pour les analystes, repérant des anomalies subtiles et même résumant les résultats en langage clair. Les avancées récentes dans les grands modèles de langage permettent aux SIEM de raisonner sur d'innombrables points de données de manière similaire à un analyste humain — mais avec une vitesse et une échelle bien supérieures. Le résultat est un assistant de sécurité numérique puissant qui aide à filtrer le bruit et à se concentrer sur les vraies menaces.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* Python 3.x installé sur votre système. Les exemples de code devraient fonctionner dans n'importe quelle version récente de Python.
    
* Une familiarité basique avec la programmation Python (boucles, fonctions, utilisation de bibliothèques) et une compréhension des logs (par exemple, à quoi ressemble une entrée de log) seront utiles.
    
* Bibliothèques Python : Nous utiliserons quelques bibliothèques courantes qui sont légères et ne nécessitent pas de matériel spécial :
    
    * [pandas](https://pandas.pydata.org/) pour la manipulation basique des données (si vos logs sont au format CSV ou similaire).
        
    * [numpy](https://numpy.org/) pour les opérations numériques.
        
    * [scikit-learn](https://scikit-learn.org/) pour le modèle de détection d'anomalies (spécifiquement, nous utiliserons l'algorithme IsolationForest).
        
* Un ensemble de données de logs à analyser. Vous pouvez utiliser n'importe quel fichier de logs (logs système, logs d'applications, etc.) en texte brut ou au format CSV. Pour la démonstration, nous simulerons un petit jeu de données de logs afin que vous puissiez suivre même sans fichier de logs prêt à l'emploi.
    

**Note :** Si vous n'avez pas les bibliothèques ci-dessus, installez-les via pip :

```bash
pip install pandas numpy scikit-learn
```

## Installation du projet

Mettons en place une structure de projet simple. Créez un nouveau répertoire pour ce projet de détection d'anomalies SIEM et naviguez dedans. À l'intérieur, vous pouvez avoir un script Python (par exemple, `siem_anomaly_demo.py`) ou un notebook Jupyter pour exécuter le code étape par étape.

Assurez-vous que votre répertoire de travail contient ou peut accéder à vos données de logs. Si vous utilisez un fichier de logs, il pourrait être judicieux de placer une copie dans ce dossier de projet. Pour notre preuve de concept, puisque nous allons générer des données de logs synthétiques, nous n'aurons pas besoin d'un fichier externe — mais dans un scénario réel, ce serait le cas.

**Étapes d'installation du projet :**

1. **Initialiser l'environnement** — Si vous préférez, créez un environnement virtuel pour ce projet (optionnel mais bonne pratique) :
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows utilisez "venv\Scripts\activate"
    ```
    
    Ensuite, installez les packages requis dans cet environnement virtuel.
    
2. **Préparer une source de données** — Identifiez la source de logs que vous souhaitez analyser. Cela pourrait être un chemin vers un fichier de logs ou une base de données. Assurez-vous de connaître le format des logs (par exemple, sont-ils séparés par des virgules, des lignes JSON, ou du texte brut ?). Pour l'illustration, nous allons fabriquer quelques entrées de logs.
    
3. **Configurer votre script ou notebook** — Ouvrez votre fichier Python ou notebook. Nous commencerons par importer les bibliothèques nécessaires et configurer les paramètres (comme les graines aléatoires pour la reproductibilité).
    

À la fin de cette installation, vous devriez avoir un environnement Python prêt à exécuter notre code d'analyse de logs SIEM, et soit un jeu de données de logs réel, soit l'intention de simuler des données avec moi.

## Implémentation de l'analyse des logs

Dans un système SIEM complet, l'analyse des logs implique la collecte de logs à partir de diverses sources et leur analyse dans un format uniforme pour un traitement ultérieur. Les logs contiennent souvent des champs comme l'horodatage, le niveau de gravité, la source, le message d'événement, l'ID utilisateur, l'adresse IP, etc. La première tâche consiste à ingérer et pré-traiter ces logs.

### **1. Ingestion des logs**

Si vos logs sont dans un fichier texte, vous pouvez les lire en Python. Par exemple, si chaque entrée de log est une ligne dans le fichier, vous pourriez faire :

```python
with open("my_logs.txt") as f:
    raw_logs = f.readlines()
```

Si les logs sont structurés (par exemple, au format CSV avec des colonnes), Pandas peut grandement simplifier la lecture :

```python
import pandas as pd
df = pd.read_csv("my_logs.csv")
print(df.head())
```

Cela vous donnera un DataFrame `df` avec vos entrées de logs organisées en colonnes. Mais de nombreux logs sont semi-structurés (par exemple, des composants séparés par des espaces ou des caractères spéciaux). Dans de tels cas, vous devrez peut-être diviser chaque ligne par un délimiteur ou utiliser des expressions régulières pour extraire les champs. Par exemple, imaginez une ligne de log :

```python
2025-03-06 08:00:00, INFO, User login success, user: admin
```

Cela contient un horodatage, un niveau de log, un message et un utilisateur. Nous pouvons analyser de telles lignes avec les méthodes de chaîne de Python :

```python
logs = [
    "2025-03-06 08:00:00, INFO, User login success, user: admin",
    "2025-03-06 08:01:23, INFO, User login success, user: alice",
    "2025-03-06 08:02:45, ERROR, Failed login attempt, user: alice",
    # ... (plus de lignes de log)
]
parsed_logs = []
for line in logs:
    parts = [p.strip() for p in line.split(",")]
    timestamp = parts[0]
    level = parts[1]
    message = parts[2]
    user = parts[3].split(":")[1].strip() if "user:" in parts[3] else None
    parsed_logs.append({"timestamp": timestamp, "level": level, "message": message, "user": user})

# Convertir en DataFrame pour une analyse plus facile
df_logs = pd.DataFrame(parsed_logs)
print(df_logs.head())
```

L'exécution de ce qui précède sur notre liste d'exemple pourrait produire quelque chose comme :

```python
            timestamp  level                 message   user
0  2025-03-06 08:00:00   INFO    User login success   admin
1  2025-03-06 08:01:23   INFO    User login success   alice
2  2025-03-06 08:02:45  ERROR  Failed login attempt   alice
...
```

Nous avons maintenant structuré les logs dans un tableau. Dans un scénario réel, vous continueriez à analyser tous les champs pertinents de vos logs (par exemple, les adresses IP, les codes d'erreur, etc.) en fonction de ce que vous souhaitez analyser.

### **2. Prétraitement et extraction de caractéristiques**

Avec les logs dans un format structuré, l'étape suivante consiste à dériver des caractéristiques pour la détection d'anomalies. Les messages de logs bruts (chaînes de caractères) sont difficiles à apprendre directement pour un algorithme. Nous extrayons souvent des caractéristiques numériques ou des catégories qui peuvent être quantifiées. Voici quelques exemples de caractéristiques :

* **Comptages d'événements :** nombre d'événements par minute/heure, nombre d'échecs de connexion pour chaque utilisateur, etc.
    
* **Durée ou taille :** si les logs incluent des durées ou des tailles de données (par exemple, taille de transfert de fichier, temps d'exécution de requête), ces valeurs numériques peuvent être utilisées directement.
    
* **Encodage catégoriel :** les niveaux de logs (INFO, ERROR, DEBUG) pourraient être mappés à des nombres, ou des types d'événements spécifiques pourraient être encodés en one-hot.
    

Pour cette preuve de concept, concentrons-nous sur une caractéristique numérique simple : le nombre de tentatives de connexion par minute pour un utilisateur donné. Nous allons simuler cela comme nos données de caractéristiques.

Dans un système réel, vous calculeriez cela en regroupant les entrées de logs analysées par fenêtre de temps et utilisateur. L'objectif est d'obtenir un tableau de nombres où chaque nombre représente "combien de tentatives de connexion ont eu lieu dans une minute donnée". La plupart du temps, ce nombre sera faible (comportement normal), mais si une minute particulière a vu un nombre inhabituellement élevé de tentatives, c'est une anomalie (possiblement une attaque par force brute).

Pour simuler, nous allons générer une liste de 50 valeurs représentant un comportement normal, puis ajouter quelques valeurs qui sont anormalement élevées :

```python
import numpy as np

# Simuler 50 minutes de comptages normaux de tentatives de connexion (environ 5 par minute en moyenne)
np.random.seed(42)  # pour un exemple reproductible
normal_counts = np.random.poisson(lam=5, size=50)

# Simuler une anomalie : un pic dans les tentatives de connexion (par exemple, un attaquant essaie 30+ fois en une minute)
anomalous_counts = np.array([30, 40, 50])

# Combiner les données
login_attempts = np.concatenate([normal_counts, anomalous_counts])
print("Tentatives de connexion par minute :", login_attempts)
```

Lorsque vous exécutez ce qui précède, `login_attempts` pourrait ressembler à :

```python
Tentatives de connexion par minute : [ 5  4  4  5  5  3  5  ...  4 30 40 50]
```

La plupart des valeurs sont à un chiffre, mais à la fin nous avons trois minutes avec 30, 40 et 50 tentatives — des valeurs aberrantes claires. Ce sont nos données préparées pour la détection d'anomalies. Dans une analyse de logs réelle, ce type de données pourrait provenir du comptage d'événements dans vos logs au fil du temps ou de l'extraction d'une métrique à partir du contenu des logs.

Maintenant que nos données sont prêtes, nous pouvons passer à la construction du modèle de détection d'anomalies.

## Comment construire le modèle de détection d'anomalies

Pour détecter les anomalies dans nos données dérivées des logs, nous utiliserons une approche de machine learning. Plus précisément, nous utiliserons une Isolation Forest — un algorithme populaire pour la détection d'anomalies non supervisée.

L'Isolation Forest fonctionne en partitionnant aléatoirement les données et en isolant les points. Les anomalies sont ces points qui sont isolés (séparés des autres) rapidement, c'est-à-dire en moins de divisions aléatoires. Cela en fait un excellent outil pour identifier les valeurs aberrantes dans un ensemble de données sans avoir besoin d'étiquettes (nous n'avons pas besoin de savoir à l'avance quelles entrées de log sont "mauvaises").

Pourquoi Isolation Forest ?

* Il est efficace et fonctionne bien même si nous avons beaucoup de données.
    
* Il ne suppose aucune distribution de données spécifique (contrairement à certaines méthodes statistiques).
    
* Il nous donne un moyen simple de noter les anomalies.
    

Entraînons une Isolation Forest sur nos données `login_attempts` :

```python
from sklearn.ensemble import IsolationForest

# Préparer les données dans la forme attendue par le modèle (échantillons, caractéristiques)
X = login_attempts.reshape(-1, 1)  # chaque échantillon est un [compte] à une dimension

# Initialiser le modèle Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
# contamination=0.05 signifie que nous nous attendons à ce que environ 5 % des données soient des anomalies

# Entraîner le modèle sur les données
model.fit(X)
```

Quelques notes sur le code :

* Nous avons remodelé `login_attempts` en un tableau 2D `X` avec une colonne de caractéristiques car scikit-learn nécessite un tableau 2D pour l'entraînement (`fit`).
    
* Nous avons défini `contamination=0.05` pour donner au modèle une indication que environ 5 % des données pourraient être des anomalies. Dans nos données synthétiques, nous avons ajouté 3 anomalies sur 53 points, ce qui représente ~5,7 %, donc 5 % est une estimation raisonnable. (Si vous ne spécifiez pas la contamination, l'algorithme choisira une valeur par défaut basée sur une hypothèse ou utilisera une valeur par défaut de 0,1 dans certaines versions.)
    
* `random_state=42` assure simplement la reproductibilité.
    

À ce stade, le modèle Isolation Forest a été entraîné sur nos données. En interne, il a construit un ensemble d'arbres aléatoires qui partitionnent les données. Les points qui sont difficiles à isoler (c'est-à-dire dans le groupe dense de points normaux) se retrouvent profondément dans ces arbres, tandis que les points qui sont faciles à isoler (les valeurs aberrantes) se retrouvent avec des chemins plus courts.

Ensuite, nous utiliserons ce modèle pour identifier quels points de données sont considérés comme anormaux.

## Test et visualisation des résultats

Voici la partie excitante : utiliser notre modèle entraîné pour détecter les anomalies dans les données de logs. Nous allons faire en sorte que le modèle prédise les étiquettes pour chaque point de données, puis filtrer ceux qui sont signalés comme des valeurs aberrantes.

```python
# Utiliser le modèle pour prédire les anomalies
labels = model.predict(X)
# Le modèle produit +1 pour les points normaux et -1 pour les anomalies

# Extraire les indices et les valeurs des anomalies
anomaly_indices = np.where(labels == -1)[0]
anomaly_values = login_attempts[anomaly_indices]

print("Indices des anomalies :", anomaly_indices)
print("Valeurs des anomalies (tentatives de connexion) :", anomaly_values)
```

Dans notre cas, nous nous attendons à ce que les anomalies soient les grands nombres que nous avons insérés (30, 40, 50). La sortie pourrait ressembler à :

```python
Indices des anomalies : [50 51 52]
Valeurs des anomalies (tentatives de connexion) : [30 40 50]
```

Même sans savoir quoi que ce soit sur les "tentatives de connexion" spécifiquement, l'Isolation Forest a reconnu ces valeurs comme étant en dehors de la ligne par rapport au reste des données.

C'est la puissance de la détection d'anomalies dans un contexte de sécurité : nous ne savons pas toujours à quoi ressemblera une nouvelle attaque, mais si elle provoque quelque chose qui s'éloigne des schémas normaux (comme un utilisateur faisant soudainement 10 fois plus de tentatives de connexion que d'habitude), le détecteur d'anomalies braque un projecteur dessus.

### **Visualisation des résultats**

Dans une analyse réelle, il est souvent utile de visualiser les données et les anomalies. Par exemple, nous pourrions tracer les valeurs de `login_attempts` au fil du temps (minute par minute) et mettre en évidence les anomalies dans une couleur différente.

Dans ce cas simple, un graphique en ligne montrerait une ligne principalement plate autour de 3-8 connexions/min avec trois pics énormes à la fin. Ces pics sont nos anomalies. Vous pourriez obtenir cela avec Matplotlib si vous exécutez cela dans un notebook :

```python
import matplotlib.pyplot as plt

plt.plot(login_attempts, label="Tentatives de connexion par minute")
plt.scatter(anomaly_indices, anomaly_values, color='red', label="Anomalies")
plt.xlabel("Temps (index de minute)")
plt.ylabel("Tentatives de connexion")
plt.legend()
plt.show()
```

Pour une sortie basée sur du texte comme nous l'avons ici, les résultats imprimés confirment déjà que les valeurs élevées ont été capturées. Dans des cas plus complexes, les modèles de détection d'anomalies fournissent également un score d'anomalie pour chaque point (par exemple, à quelle distance il se trouve de la plage normale). Par exemple, l'IsolationForest de scikit-learn possède une méthode `decision_function` qui donne un score (où les scores plus bas signifient plus anormal).

Pour simplifier, nous n'approfondirons pas les scores ici, mais il est bon de savoir que vous pouvez les récupérer pour classer les anomalies par gravité.

Avec la détection d'anomalies fonctionnelle, que pouvons-nous faire lorsque nous trouvons une anomalie ? Cela nous amène à réfléchir aux réponses automatisées.

## Possibilités de réponse automatisée

Détecter une anomalie n'est que la moitié de la bataille — l'étape suivante est d'y répondre. Dans les systèmes SIEM d'entreprise, la réponse automatisée (souvent associée au SOAR — Security Orchestration, Automation, and Response) peut réduire considérablement le temps de réaction aux incidents.

Que pourrait faire un SIEM alimenté par l'IA lorsqu'il signale quelque chose d'inhabituel ? Voici quelques possibilités :

* **Alerte :** L'action la plus simple est d'envoyer une alerte au personnel de sécurité. Cela pourrait être un email, un message Slack, ou la création d'un ticket dans un système de gestion des incidents. L'alerte contiendrait les détails de l'anomalie (par exemple, "L'utilisateur *alice* a eu 50 tentatives de connexion échouées en 1 minute, ce qui est anormal"). L'IA générative peut aider ici en générant un résumé clair en langage naturel de l'incident pour l'analyste.
    
* **Atténuation automatisée :** Les systèmes plus avancés pourraient prendre des mesures directes. Par exemple, si une adresse IP montre un comportement malveillant dans les logs, le système pourrait automatiquement bloquer cette IP sur le pare-feu. Dans notre exemple de pic de connexion, le système pourrait temporairement verrouiller le compte utilisateur ou demander une authentification supplémentaire, sous l'hypothèse qu'il pourrait s'agir d'une attaque par bot. Les SIEM basés sur l'IA aujourd'hui peuvent effectivement déclencher des actions de réponse prédéfinies ou même orchestrer des flux de travail complexes lorsque certaines menaces sont détectées (voir [AI SIEM: How SIEM with AI/ML is Revolutionizing the SOC | Exabeam](https://www.exabeam.com/explainers/siem/ai-siem-how-siem-with-ai-ml-is-revolutionizing-the-soc/#:~:text=automatically%20trigger%20alerts%2C%20implement%20predefined,even%20orchestrate%20complex%20response%20workflows) pour plus d'informations).
    
* **Support à l'investigation :** L'IA générative pourrait également être utilisée pour recueillir automatiquement du contexte. Par exemple, lors de la détection de l'anomalie, le système pourrait extraire les logs associés (événements environnants, autres actions du même utilisateur ou de la même IP) et fournir un rapport agrégé. Cela évite à l'analyste de devoir interroger manuellement plusieurs sources de données.
    

Il est important de mettre en œuvre des réponses automatisées avec soin — vous ne voulez pas que le système surréagisse aux faux positifs. Une stratégie courante est une réponse échelonnée : les anomalies de faible confiance pourraient simplement enregistrer un avertissement ou envoyer une alerte de faible priorité, tandis que les anomalies de haute confiance (ou des combinaisons d'anomalies) déclenchent des mesures de défense actives.

En pratique, un SIEM alimenté par l'IA s'intégrerait à votre infrastructure (via des API, des scripts, etc.) pour exécuter ces actions. Pour notre PoC Python, vous pourriez simuler une réponse automatisée en, par exemple, imprimant un message ou en appelant une fonction factice lorsqu'une anomalie est détectée. Par exemple :

```python
if len(anomaly_indices) > 0:
    print(f"Alerte ! Détecté {len(anomaly_indices)} événements anormaux. Initialisation des procédures de réponse...")
    # Ici, vous pourriez ajouter du code pour désactiver un utilisateur ou notifier un administrateur, etc.
```

Bien que notre démonstration soit simple, il est facile d'imaginer l'évolutivité de cela. Le SIEM pourrait, par exemple, alimenter les anomalies dans un modèle génératif plus large qui évalue la situation et décide de la meilleure marche à suivre (comme un assistant Ops de chatbot qui connaît vos runbooks). Les possibilités d'automatisation s'élargissent à mesure que l'IA devient plus sophistiquée.

## Conclusion

Dans ce tutoriel, nous avons construit un composant SIEM basique alimenté par l'IA qui ingère des données de logs, les analyse pour détecter des anomalies en utilisant un modèle de machine learning, et identifie des événements inhabituels qui pourraient représenter des menaces de sécurité.

Nous avons commencé par analyser et préparer les données de logs, puis utilisé un modèle Isolation Forest pour détecter les valeurs aberrantes dans un flux de comptages de tentatives de connexion. Le modèle a réussi à signaler les comportements hors norme sans aucune connaissance préalable de ce à quoi ressemble une "attaque" — il s'est purement basé sur les écarts par rapport aux schémas normaux appris.

Nous avons également discuté de la manière dont un tel système pourrait répondre aux anomalies détectées, de l'alerte des humains à la prise de mesures automatiques.

Les systèmes SIEM modernes augmentés par l'IA/ML évoluent dans cette direction : non seulement ils détectent les problèmes, mais ils aident également à les trier et à y répondre. L'IA générative améliore encore cela en apprenant des analystes et en fournissant des résumés et des décisions intelligents, devenant effectivement un assistant infatigable dans le Centre des Opérations de Sécurité.

Pour les prochaines étapes et améliorations :

* Vous pouvez essayer cette approche sur des données de logs réelles. Par exemple, prenez un fichier de logs système et extrayez une caractéristique comme "nombre de logs d'erreur par heure" ou "octets transférés par session" et exécutez la détection d'anomalies sur cela.
    
* Expérimentez avec d'autres algorithmes comme One-Class SVM ou Local Outlier Factor pour la détection d'anomalies afin de voir comment ils se comparent.
    
* Incorporez un modèle de langage simple pour analyser les lignes de logs ou pour expliquer les anomalies. Par exemple, un LLM pourrait lire une entrée de log anormale et suggérer ce qui pourrait ne pas aller ("Cette erreur signifie généralement que la base de données est inaccessible").
    
* Étendez les caractéristiques : dans un vrai SIEM, vous utiliseriez de nombreux signaux à la fois (comptages d'échecs de connexion, géolocalisation IP inhabituelle, noms de processus rares dans les logs, etc.). Plus de caractéristiques et de données peuvent améliorer le contexte pour la détection.