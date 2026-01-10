---
title: 'Concurrence vs Parallélisme : Quelle est la différence et pourquoi s''y intéresser
  ?'
subtitle: ''
author: Wisdom Usa
co_authors: []
series: null
date: '2025-10-17T15:08:36.162Z'
originalURL: https://freecodecamp.org/news/concurrency-vs-parallelism-whats-the-difference-and-why-should-you-care
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760622633358/ad43bbd8-116c-42eb-95b7-0ef70156983a.png
tags:
- name: Computer Science
  slug: computer-science
- name: software development
  slug: software-development
- name: concurrency
  slug: concurrency
- name: Parallel Programming
  slug: parallel-programming
seo_title: 'Concurrence vs Parallélisme : Quelle est la différence et pourquoi s''y
  intéresser ?'
seo_desc: 'In software engineering, certain concepts appear deceptively simple at
  first glance but fundamentally shape the way we design and architect systems. Concurrency
  and parallelism are two such concepts that warrant careful examination.

  These terms are f...'
---

En génie logiciel, certains concepts paraissent trompeusement simples au premier abord, mais façonnent fondamentalement la manière dont nous concevons et architecturons les systèmes. La concurrence et le parallélisme sont deux de ces concepts qui méritent un examen attentif.

Ces termes sont fréquemment utilisés de manière interchangeable, même parmi les développeurs expérimentés. Mais bien qu'ils puissent sembler similaires et se chevaucher occasionnellement en pratique, ils répondent à des problèmes distincts et servent des objectifs architecturaux différents. Comprendre cette distinction n'est pas seulement un exercice académique. Cela impacte directement la façon dont vous construisez des systèmes évolutifs et efficaces.

Que vous développiez un serveur web à fort trafic, que vous entraîniez des modèles de machine learning complexes ou que vous optimisiez les performances d'une application, une solide compréhension de ces concepts peut faire la différence entre une solution qui fonctionne simplement et une solution qui monte en charge élégamment dans des conditions réelles.

Cet article propose une analyse complète des deux concepts à travers des analogies visuelles, des exemples pratiques et des implémentations techniques. À la fin, vous serez équipé pour appliquer ces principes en toute confiance dans vos projets logiciels.

### Voici ce que nous allons couvrir :

1. [Comprendre les concepts fondamentaux](#heading-comprendre-les-concepts-fondamentaux)
    
    * [L'analogie de la cuisine](#heading-lanalogie-de-la-cuisine)
        
2. [À quoi ressemble la concurrence en pratique](#heading-a-quoi-ressemble-la-concurrence-en-pratique)
    
    * [Exemple Python : Implémenter la concurrence avec asyncio](#heading-exemple-python-implementer-la-concurrence-avec-asyncio)
        
3. [À quoi ressemble le parallélisme en pratique](#heading-a-quoi-ressemble-le-parallelisme-en-pratique)
    
    * [Exemple Python : Implémenter le parallélisme avec multiprocessing](#heading-exemple-python-implementer-le-parallelisme-avec-multiprocessing)
        
4. [Concurrence vs Parallélisme : Une comparaison détaillée](#heading-concurrence-vs-parallelisme-une-comparaison-detaillee)
    
    * [Quand utiliser l'un ou l'autre](#heading-quand-utiliser-lun-ou-lautre)
        
5. [Applications réelles et cas d'utilisation](#heading-applications-reelles-et-cas-dutilisation)
    
    * [La concurrence dans les systèmes de production](#heading-la-concurrence-dans-les-systemes-de-production)
        
    * [Le parallélisme dans les systèmes de production](#heading-le-parallelisme-dans-les-systemes-de-production)
        
    * [Approches hybrides](#heading-approches-hybrides)
        
6. [Choisir la bonne approche pour votre problème](#heading-choisir-la-bonne-approche-pour-votre-probleme)
    
    * [Piège courant à éviter](#heading-piege-courant-a-eviter)
        
7. [Pourquoi cette distinction est importante en pratique](#heading-pourquoi-cette-distinction-est-importante-en-pratique)
    
8. [Idées reçues courantes et clarifications](#heading-idees-recues-courantes-et-clarifications)
    
9. [Stratégies d'implémentation pratiques](#heading-strategies-dimplementation-pratiques)
    
    * [Lors de l'implémentation de la concurrence](#heading-lors-de-limplementation-de-la-concurrence)
        
    * [Lors de l'implémentation du parallélisme](#heading-lors-de-limplementation-du-parallelisme)
        
10. [Outils et technologies par langage](#heading-outils-et-technologies-par-langage)
    
11. [Ressources d'apprentissage supplémentaires](#heading-ressources-dapprentissage-supplementaires)
    
12. [Conclusion](#heading-conclusion)
    

## Comprendre les concepts fondamentaux

Avant de plonger dans les implémentations, établissons des définitions claires :

**La concurrence** fait référence à la capacité d'un système à gérer plusieurs tâches sur des périodes de temps qui se chevauchent. Cela ne signifie pas nécessairement que ces tâches s'exécutent au même instant précis. La concurrence consiste plutôt à structurer un programme pour gérer plusieurs opérations en entrelaçant leur exécution, souvent sur un seul cœur de processeur.

**Le parallélisme**, par opposition, implique l'exécution simultanée de plusieurs tâches. Cela nécessite généralement plusieurs cœurs de processeur ou processeurs travaillant en tandem, chacun gérant une partie distincte de la charge de travail en même temps.

### L'analogie de la cuisine

Considérez le processus de cuisine comme un modèle mental utile :

Une cuisine concurrente emploie un seul chef qui passe rapidement d'une préparation à l'autre. Le chef peut couper des légumes pour un plat, puis remuer une sauce pour un autre, puis revenir au premier plat pour continuer la préparation. Du point de vue d'un observateur, il semble que plusieurs plats sont préparés « en même temps », mais en réalité, le chef effectue une action à la fois en succession rapide.

Une cuisine parallèle dispose de plusieurs chefs, chacun travaillant sur des plats différents simultanément. Un chef prépare l'entrée pendant qu'un autre s'occupe du plat principal, et un troisième gère le dessert. Un véritable travail simultané a lieu entre plusieurs travailleurs.

Même cuisine, stratégies différentes, résultats différents.

## À quoi ressemble la concurrence en pratique

[![Comparaison visuelle entre concurrence et parallélisme dans l'exécution des tâches. À gauche, un seul CPU alterne entre la Tâche 1 et la Tâche 2 (ou Thread 1 et Thread 2), illustrant la concurrence sans véritable parallélisme. À droite, deux CPU exécutent la Tâche 1 et la Tâche 2 simultanément, illustrant à la fois la concurrence et le parallélisme.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760010754774/e4563560-b9b2-42e0-8c69-5c052db2656c.png align="center")](https://mechdampiitb.github.io/cs751_shyamsundar/)

La concurrence concerne fondamentalement l'ordonnancement des tâches, la coordination et la gestion des ressources. Elle permet à un programme de gérer plusieurs opérations en entrelaçant stratégiquement leur exécution, que ce soit sur un seul cœur ou sur plusieurs threads.

Un exemple pratique : lorsque vous regardez une vidéo sur YouTube pendant que votre appareil télécharge un fichier en arrière-plan et que votre application de messagerie vérifie les nouveaux messages, votre CPU effectue des changements de contexte rapides entre ces tâches. Chaque tâche reçoit une tranche de temps de traitement, créant l'illusion d'une exécution simultanée même sur un processeur monocœur.

### Exemple Python : Implémenter la concurrence avec asyncio

Pour examiner la concurrence plus en détail, nous allons créer une application simple qui récupère des données sur diverses API de manière asynchrone. C'est un exemple de la façon dont la bibliothèque Python, asyncio, nous permet de lancer plusieurs opérations réseau sans blocage afin d'utiliser efficacement le temps d'attente.

Dans cette implémentation, nous simulerons des appels API vers un service météo, un service d'actualités et une base de données de profils utilisateurs. Notez que les trois requêtes commencent presque en même temps, mais le programme n'attend pas que l'une d'elles soit terminée avant de commencer la suivante.

```python
import asyncio

async def fetch_data_from_api(api_name, delay):
    print(f"Démarrage de la requête vers {api_name}...")
    await asyncio.sleep(delay)  # Simule l'attente d'E/S réseau
    print(f"Réponse reçue de {api_name}")
    return f"Données de {api_name}"

async def fetch_user_profile(user_id):
    print(f"Récupération du profil pour l'utilisateur {user_id}...")
    await asyncio.sleep(1.5)
    print(f"Profil chargé pour l'utilisateur {user_id}")
    return {"user_id": user_id, "name": "John Doe"}

async def main():
    # Toutes les tâches démarrent et sont gérées de manière concurrente
    results = await asyncio.gather(
        fetch_data_from_api("Weather API", 2),
        fetch_data_from_api("News API", 1),
        fetch_user_profile(12345)
    )
    print("\nToutes les opérations sont terminées !")
    print("Résultats :", results)

asyncio.run(main())
```

**Ce qui se passe pendant l'exécution :**

1. Les trois fonctions asynchrones sont initiées approximativement en même temps.
    
2. La boucle d'événements (event loop) gère leur exécution, basculant entre les tâches lorsque l'une d'elles est en attente (pendant les instructions `await`).
    
3. Pendant qu'une tâche attend une E/S simulée, la boucle d'événements permet aux autres tâches de progresser.
    
4. La tâche avec le délai le plus court se termine en premier, même si toutes ont été démarrées ensemble.
    
5. Aucune tâche ne bloque les autres, ce qui permet une utilisation efficace du thread unique.
    

**Aperçu clé :** La concurrence optimise la réactivité et l'utilisation des ressources. Elle ne rend pas intrinsèquement les tâches individuelles plus rapides. Au lieu de cela, elle permet à plusieurs tâches de progresser pendant la même période, en particulier lorsque ces tâches impliquent d'attendre des ressources externes.

## À quoi ressemble le parallélisme en pratique

[![Diagramme illustrant la chronologie d'exécution d'une région parallèle utilisant OpenMP. Il montre comment les threads sont divisés (fork) et rejoints (join), avec des horodatages au fork (t_f) et au join (t_j), la création de threads individuels (t_{i,s}) et leur achèvement (t_{i,c}), ainsi que la mémoire allouée par CPU/thread.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760010925777/c85a1976-96da-4f74-abba-62d1d0489d60.png align="center")](https://www.researchgate.net/figure/Parallelism-mechanism-in-OpenMP-with-multiple-CPU-threads_fig3_311454812)

Le parallélisme se concentre sur l'exécution simultanée réelle. Cette approche exploite plusieurs cœurs de processeur ou processeurs pour diviser le travail et exécuter des portions de manière concurrente en temps réel.

Le parallélisme brille lors du traitement d'opérations gourmandes en CPU telles que les calculs mathématiques, le traitement d'images, le rendu vidéo ou l'entraînement de modèles de deep learning.

### Exemple Python : Implémenter le parallélisme avec multiprocessing

Pour mieux comprendre l'exécution parallèle, nous allons créer un programme qui effectue des calculs intensifs sur un ensemble de cœurs de CPU. L'exemple donné s'appuie sur Python et le module multiprocessing pour créer différents processus qui sont exécutés sur différents cœurs de processeur.

Pour travailler avec un exemple suffisamment complexe, nous allons calculer la somme des carrés de millions de nombres. Contrairement à l'échantillon de code concurrent, où nous attendions de recevoir des E/S, nous effectuons ici un travail réellement intensif pour le CPU. Vous remarquerez la réduction du temps nécessaire pour exécuter le travail lorsqu'il est partagé par plusieurs cœurs.

```python
from multiprocessing import Process, current_process
import time

def compute_heavy_task(task_name, iterations):
    """Simule une opération gourmande en CPU"""
    process_name = current_process().name
    print(f"{task_name} démarré sur {process_name}")
    
    # Simule un travail lié au CPU
    result = 0
    for i in range(iterations):
        result += i ** 2
    
    time.sleep(1)  # Travail simulé supplémentaire
    print(f"{task_name} terminé sur {process_name}. Résultat : {result}")
    return result

if __name__ == "__main__":
    start_time = time.time()
    
    # Crée des processus séparés pour chaque tâche
    p1 = Process(target=compute_heavy_task, args=("Tâche 1", 10000000))
    p2 = Process(target=compute_heavy_task, args=("Tâche 2", 10000000))
    p3 = Process(target=compute_heavy_task, args=("Tâche 3", 10000000))
    
    # Démarre tous les processus (ils s'exécutent sur des cœurs de CPU séparés)
    p1.start()
    p2.start()
    p3.start()
    
    # Attend que tous les processus se terminent
    p1.join()
    p2.join()
    p3.join()
    
    end_time = time.time()
    print(f"\nToutes les tâches terminées en {end_time - start_time:.2f} secondes")
```

**Ce qui se passe pendant l'exécution :**

1. Trois processus distincts sont lancés, chacun alloué aux cœurs de CPU disponibles.
    
2. Chaque processus s'exécute indépendamment avec son propre espace mémoire et son propre interpréteur Python.
    
3. Les trois calculs intensifs s'exécutent véritablement simultanément sur plusieurs cœurs.
    
4. Le temps d'exécution total est déterminé par la tâche la plus longue, et non par la somme cumulative de toutes les tâches.
    
5. Sur un système multicœur, cela se termine environ trois fois plus vite qu'une exécution séquentielle.
    

**Aperçu clé :** Le parallélisme permet un gain de vitesse réel en répartissant la charge de travail informatique sur plusieurs processeurs. Cela réduit directement le temps d'exécution total pour les opérations liées au CPU.

## Concurrency vs Parallélisme : Une comparaison détaillée

| Aspect | Concurrence | Parallélisme |
| --- | --- | --- |
| **Définition de base** | Gérer et coordonner plusieurs tâches sur des périodes de temps qui se chevauchent | Exécuter plusieurs tâches simultanément sur plusieurs processeurs |
| **Objectif principal** | Améliorer la structure, la réactivité et l'efficacité des ressources | Augmenter le débit de calcul brut et la vitesse |
| **Utilisation du CPU** | Peut fonctionner sur un seul ou plusieurs cœurs via l'entrelacement | Nécessite plusieurs cœurs ou processeurs pour un véritable parallélisme |
| **Modèle d'exécution** | Commutation et ordonnancement des tâches | Exécution simultanée sur le matériel |
| **Cas d'utilisation optimal** | Opérations liées aux E/S (requêtes réseau, opérations sur fichiers, requêtes de base de données) | Opérations liées au CPU (calculs mathématiques, traitement de données, rendu) |
| **Techniques d'implémentation courantes** | Modèles Async/await, threads, coroutines, boucles d'événements | Multiprocessing, calcul sur GPU et frameworks de calcul distribué |
| **Caractéristique de performance** | Réduit le temps d'inactivité et améliore le débit sans nécessairement accélérer les tâches individuelles | Réduit directement le temps d'exécution en divisant le travail |
| **Applications typiques** | Serveurs web, API REST, applications GUI, systèmes de chat et notifications en temps réel | Encodage vidéo, simulations scientifiques, entraînement de machine learning, analyse de big data |
| **Surcharge de ressources** | Faible (mémoire partagée, changement de contexte léger) | Élevée (espaces mémoire séparés, coûts de communication inter-processus) |

### Quand utiliser l'un ou l'autre :

Utilisez la **concurrence** lorsque vous souhaitez gérer plus de tâches efficacement au cours de la même période, en particulier lorsque ces tâches passent du temps à attendre des ressources externes.

Utilisez le **parallélisme** lorsque vous souhaitez terminer les tâches plus rapidement en exploitant plusieurs processeurs pour diviser la charge de travail informatique.

## Applications réelles et cas d'utilisation

### La concurrence dans les systèmes de production

#### 1\. Serveurs Web et API

Les frameworks web modernes comme Node.js, Django avec des vues asynchrones et FastAPI gèrent des milliers de connexions clients simultanées. Chaque requête peut impliquer des requêtes de base de données, des appels d'API externes ou des opérations sur fichiers. La concurrence permet au serveur de gérer de nouvelles requêtes tout en attendant que les opérations d'E/S des requêtes précédentes se terminent.

#### 2\. Communication en temps réel

Les applications de chat, les outils d'édition collaborative et les plateformes de streaming en direct gèrent plusieurs connexions simultanées. Les messages doivent être reçus, traités et diffusés à plusieurs clients de manière concurrente sans bloquer aucune connexion individuelle.

#### 3\. Applications mobiles

Les applications mobiles effectuent la synchronisation en arrière-plan, la gestion des notifications push et la mise en cache des données tout en maintenant une interface utilisateur réactive. Le thread UI reste libre pendant que les opérations en arrière-plan se déroulent de manière concurrente.

#### 4\. Orchestration de microservices

Les maillages de services (service meshes) coordonnent plusieurs appels d'API vers différents microservices, agrégeant les résultats efficacement sans attendre que chaque appel se termine séquentiellement.

### Le parallélisme dans les systèmes de production

#### 1\. Machine Learning et IA

L'entraînement des réseaux de neurones implique des calculs matriciels massifs qui peuvent être répartis sur plusieurs cœurs de GPU ou même plusieurs machines. Des Frameworks comme TensorFlow et PyTorch parallélisent automatiquement les opérations sur le matériel disponible.

#### 2\. Traitement de Big Data

Les frameworks de calcul distribué tels qu'Apache Spark, Hadoop et Dask divisent les grands ensembles de données entre les nœuds d'un cluster. Chaque nœud traite sa portion de données en parallèle, permettant l'analyse d'ensembles de données à l'échelle du pétaoctet.

#### 3\. Traitement multimédia

Le transcodage vidéo, le traitement par lots d'images et le rendu audio exploitent plusieurs cœurs de CPU ou GPU. Chaque image ou segment peut être traité indépendamment en parallèle.

#### 4\. Calcul scientifique

Les simulations de physique numérique, le séquençage du génome et la modélisation climatique nécessitent d'énormes ressources informatiques. Le parallélisme sur des clusters de superordinateurs permet à ces calculs de se terminer dans des délais raisonnables.

#### 5\. Modélisation financière

L'analyse des risques et l'optimisation de portefeuille impliquent l'exécution de milliers de scénarios. Le traitement parallèle permet à ces calculs de s'exécuter simultanément, fournissant des résultats assez rapidement pour une prise de décision en temps réel.

### Approches hybrides

En pratique, les systèmes sophistiqués combinent fréquemment les deux paradigmes. Considérez une application web moderne :

1. Le serveur web gère les requêtes des clients de manière concurrente (gestion de plusieurs utilisateurs simultanément).
    
2. Chaque requête peut déclencher des tâches de traitement de données parallèles (telles que le redimensionnement d'image sur plusieurs cœurs).
    
3. Le pool de connexions à la base de données gère l'exécution concurrente des requêtes.
    
4. Les travailleurs de tâches en arrière-plan traitent les tâches en parallèle (comme l'envoi d'e-mails ou la génération de rapports).
    

Cette approche par couches exploite les forces de la concurrence et du parallélisme pour créer des systèmes à la fois réactifs et efficaces sur le plan informatique.

## Choisir la bonne approche pour votre problème

Comprendre quel paradigme appliquer nécessite d'analyser la nature de votre charge de travail :

| Si votre tâche est... | Choisissez... | Raisonnement |
| --- | --- | --- |
| **Liée aux E/S** (attente du réseau, du disque ou de la base de données) | **Concurrence** | Maximise l'efficacité en permettant à d'autres travaux de progresser pendant les temps d'attente. Le goulot d'étranglement n'est pas le calcul CPU mais la disponibilité des ressources externes. |
| **Liée au CPU** (calcul mathématique lourd, traitement de données, rendu) | **Parallélisme** | Répartit la charge de calcul sur plusieurs processeurs, réduisant directement le temps d'exécution. Le goulot d'étranglement est la capacité du CPU. |
| **Charge de travail mixte** (E/S et calcul intensif) | **Concurrence + Parallélisme** | La gestion concurrente des opérations d'E/S combinée au traitement parallèle des segments gourmands en CPU offre des performances optimales. |
| **Nombreuses petites tâches indépendantes** | **Concurrence** (si E/S) ou **Parallélisme** (si CPU) | Choisissez selon que les tâches attendent ou calculent. |
| **Peu de grands calculs divisibles** | **Parallélisme** | Divisez chaque calcul sur les cœurs pour un gain de vitesse maximal. |

### Piège courant à éviter

Une erreur fréquente consiste à tenter d'utiliser le threading pour des tâches liées au CPU dans des langages dotés d'un Global Interpreter Lock (comme le CPython de Python) et à s'attendre à des gains de vitesse parallèles. Dans de tels cas, les threads offrent de la concurrence mais pas de véritable parallélisme.

Le GIL garantit qu'un seul thread exécute le bytecode Python à la fois, ce qui entraîne une surcharge de changement de contexte sans véritable exécution parallèle. Pour le travail lié au CPU en Python, le multiprocessing ou les extensions C sont nécessaires pour un véritable parallélisme.

## Pourquoi cette distinction est importante en pratique

Saisir la différence entre concurrence et parallélisme va au-delà de l'écriture d'un code plus rapide. Cela influence fondamentalement la façon dont vous architecturez les systèmes et prenez des décisions technologiques :

Tout d'abord, choisir le modèle d'exécution approprié pour chaque composant de votre système conduit à un code plus propre et plus facile à maintenir. Vous évitez de sur-concevoir des solutions ou d'appliquer le mauvais outil à un problème.

Comprendre ces concepts évite également les modèles de gaspillage tels que le lancement de processus inutiles pour un travail lié aux E/S ou l'utilisation d'approches monothread pour des calculs parallélisables. Cela se traduit directement par une réduction des coûts d'infrastructure.

Les systèmes conçus avec des modèles de concurrence appropriés montent également en charge horizontalement plus efficacement. Ceux qui exploitent correctement le parallélisme utilisent pleinement les ressources matérielles à mesure que vous montez en charge verticalement.

De plus, vous obtiendrez des optimisations de performance clés en choisissant la bonne approche. Lorsque le profilage révèle des goulots d'étranglement, savoir s'il faut optimiser pour la concurrence ou le parallélisme guide vos efforts de refactorisation dans la bonne direction.

Au-delà de cela, dans les environnements cloud où vous payez pour les ressources de calcul, l'utilisation efficace de la concurrence et du parallélisme affecte directement les coûts opérationnels. Un système concurremment efficace pourrait gérer 10 fois la charge sur le même matériel par rapport à une alternative synchrone mal conçue.

Et ces concepts sont fondamentaux pour l'ingénierie backend, les systèmes distribués, le DevOps, l'ingénierie du machine learning et la programmation système. Ils apparaissent fréquemment dans les entretiens techniques et sont essentiels pour les rôles d'ingénieur senior.

## Idées reçues courantes et clarifications

### « L'utilisation de threads me donne automatiquement du parallélisme. »

En réalité, les threads permettent la concurrence mais ne garantissent pas l'exécution parallèle. Dans les systèmes dotés d'un Global Interpreter Lock (comme CPython) ou sur des machines monocœur, les threads s'exécutent de manière concurrente mais pas en parallèle. Le véritable parallélisme nécessite plusieurs cœurs de CPU et des mécanismes qui évitent les contraintes de verrouillage.

### « Le parallélisme est toujours plus rapide que l'exécution séquentielle. »

En fait, le parallélisme introduit une surcharge, notamment la création de processus, la communication inter-processus et les coûts de synchronisation des données. Pour les petites tâches ou les opérations liées aux E/S, cette surcharge peut l'emporter sur les avantages. Le parallélisme montre des gains lorsque le travail de calcul justifie la surcharge.

### « La concurrence et le parallélisme s'excluent mutuellement. »

Comme vous l'avez appris, les systèmes modernes de haute performance combinent couramment les deux. Un serveur web peut gérer les requêtes de manière concurrente, chaque requête déclenchant un traitement parallèle. Comprendre comment superposer ces approches est la clé pour construire des systèmes sophistiqués.

### « Plus de threads ou de processus signifient toujours de meilleures performances. »

Au-delà d'un certain point, l'ajout de threads ou de processus supplémentaires entraîne des rendements décroissants et même une dégradation des performances en raison de l'augmentation des changements de contexte et de la contention des ressources. Le nombre optimal dépend des caractéristiques de la charge de travail et du matériel disponible.

### « Async/await rend mon code plus rapide. »

Async/await améliore l'efficacité des opérations liées aux E/S en réduisant le temps d'inactivité, mais il n'accélère pas les calculs liés au CPU. Il modifie la façon dont l'attente est gérée, et non la rapidité avec laquelle les opérations individuelles s'exécutent.

## Stratégies d'implémentation pratiques

### Comment implémenter la concurrence

Pour introduire la concurrence dans vos programmes, vous devrez d'abord identifier où le temps est perdu. Les opérations bloquantes qui sont maintenues en attente de ressources externes sont les meilleures candidates pour être placées sous exécution concurrente.

Supposons que vous construisiez un scraper web pour récupérer un tas de données sur divers sites. Chaque requête HTTP attend très probablement que le serveur renvoie une réponse. D'autres requêtes pourraient être en cours dans votre programme au lieu d'attendre pendant cette période d'attente. Ces points d'attente sont identifiables en profilant votre application et en recherchant les opérations avec des appels réseau, des E/S de fichiers ou des requêtes de base de données.

Après avoir découvert ces points d'attente, la prochaine grande étape sera de sélectionner la primitive de concurrence. En Python, les opérations liées aux E/S fonctionnent très bien en utilisant les modèles d'async/await avec le support du Framework asyncio. Cela s'accompagne également d'un coût minimal.

Prenons une situation où vous devez récupérer des données utilisateur dans une API REST et interroger une base de données en même temps. Avec asyncio, vous pouvez écrire du code qui initie les deux tâches presque simultanément, puis laisser la boucle d'événements alterner entre elles pendant les périodes d'attente.

Voici un exemple pratique :

```python
import asyncio
import aiohttp

async def fetch_user_api(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.example.com/users/{user_id}') as response:
            return await response.json()

async def query_database(user_id):
    # Simulation d'une requête de base de données
    await asyncio.sleep(0.5)
    return {'preferences': 'theme:dark', 'notifications': True}

async def get_complete_user_data(user_id):
    api_data, db_data = await asyncio.gather(
        fetch_user_api(user_id),
        query_database(user_id)
    )
    return {**api_data, **db_data}
```

Cela donne un aperçu approfondi du fonctionnement de la concurrence en pratique.

### Lors de l'implémentation du parallélisme

Avant d'engager le parallélisme dans votre système, vous devrez profiler le système et vous assurer que ce qui cause votre goulot d'étranglement est un calcul lié au CPU. De nombreux développeurs pensent que leur code nécessite du parallélisme alors qu'il devrait en fait employer la concurrence.

Vous pouvez utiliser des outils de profilage tels que cProfile de Python ou des line profilers pour déterminer où le temps est utilisé ou gaspillé dans votre programme. Lorsque le temps passé dans les boucles de calcul est important par rapport à l'attente en E/S, le parallélisme peut être bénéfique.

Pour prendre un exemple, lors du traitement d'images, le temps d'exécution dans les algorithmes de manipulation de pixels consomme 90 % du temps d'exécution. C'est un bon signe que le parallélisme serait utile.

Décider comment partitionner le travail entre plusieurs processeurs est parfois une question complexe que vous devez examiner attentivement (en termes de division des tâches en points indépendants). Ces morceaux devraient pouvoir être traités individuellement sans avoir besoin de communiquer entre eux de manière régulière.

Imaginez que vous deviez examiner les fichiers journaux (logs) de plusieurs serveurs. Le traitement de chaque fichier peut se faire sur un cœur différent, et les résultats seront ajoutés à l'étape finale.

Voici comment vous pourriez structurer cela :

```python
from multiprocessing import Pool
import re

def analyze_log_file(filepath):
    error_count = 0
    with open(filepath, 'r') as f:
        for line in f:
            if re.search(r'ERROR|CRITICAL', line):
                error_count += 1
    return filepath, error_count

if __name__ == '__main__':
    log_files = ['server1.log', 'server2.log', 'server3.log', 'server4.log']
    
    with Pool(processes=4) as pool:
        results = pool.map(analyze_log_file, log_files)
    
    for filepath, count in results:
        print(f'{filepath}: {count} erreurs trouvées')
```

Dans cet exemple, chaque fichier journal est entièrement traité sur un cœur sans avoir besoin de communiquer avec d'autres processus jusqu'à l'agrégation finale des résultats.

## Outils et technologies par langage

Divers langages de programmation offrent différentes méthodes pour atteindre la concurrence et le parallélisme avec leurs propres avantages et inconvénients. Et lorsque vous comprenez les outils disponibles dans votre langage de choix, vous serez en mesure de faire un choix architectural judicieux.

### Python

Python dispose d'un environnement concurrent et parallèle. Pour la programmation concurrente, la bibliothèque asyncio offre une syntaxe plus moderne d'async/await qui est idéale pour les tâches liées aux E/S telles que le scraping web ou la communication API.

Le module threading permet l'exécution en mémoire partagée, mais est limité sur les tâches liées au CPU par le Global Interpreter Lock. Le module concurrent.futures est une interface de haut niveau pour l'exécution de tâches concurrentes, ce qui peut être utile lorsque vous souhaitez paralléliser des opérations d'E/S sans avoir à écrire le code de bas niveau des opérations asynchrones.

Parfois, vous aurez besoin d'un véritable parallélisme parce que votre travail nécessite beaucoup de temps CPU. Le multiprocessing lance des processus Python individuels, qui n'utilisent pas du tout le GIL.

Dans le cas de la science des données et des processus de machine learning, le parallélisme distribué est proposé dans des bibliothèques telles que joblib, ray et dask et peut s'exécuter de votre ordinateur portable jusqu'à un cluster d'ordinateurs.

### JavaScript et Node.js

L'architecture de la boucle d'événements a fait de la concurrence le fondement de JavaScript et Node.js. La programmation asynchrone est désormais intuitive avec la syntaxe native et les Promises utilisées comme modèle standard de gestion des opérations d'E/S (comme les requêtes HTTP ou l'accès au système de fichiers).

JavaScript est monothread, et Node.js est conçu pour exécuter des programmes monothread qui font bon usage des tâches concurrentes liées aux E/S, telles que les serveurs web, qui prennent en charge des milliers de connexions parallèles.

Dans les cas de parallélisme réel (par exemple, le traitement d'images ou les tâches cryptographiques), les worker threads vous permettent d'exécuter du JavaScript sur plusieurs cœurs. Le module child_process peut lancer des instances individuelles de Node.js, et le module cluster vous permet de lancer un pool de workers pour accepter les connexions entrantes et tirer le meilleur parti de tous les cœurs de CPU dans un serveur web.

### Java

Java dispose d'un support de concurrence et de parallélisme mature et éprouvé. CompletableFuture offre une interface fluide pour les opérations asynchrones, il est donc plus facile de séquencer des tâches asynchrones dépendantes sans tomber dans l'enfer des callbacks.

Le modèle ExecutorService fournit également une gestion détaillée des pools de threads et de l'ordonnancement des tâches, ce qui est nécessaire au développement de programmes serveurs haute performance. Les pools de threads Java pour le parallélisme sont efficaces pour gérer les threads de travail afin d'exécuter des tâches liées au CPU, tandis que ForkJoinPool utilise des algorithmes de vol de travail (work-stealing) utiles pour les problèmes de type « diviser pour régner ».

Java 8 propose des flux parallèles (parallel streams), qui vous permettent de traiter des collections en parallèle avec un minimum de réécriture de code – mais vous devez porter une attention particulière au moment où ils amélioreront ou non réellement les performances.

### Go

Go a introduit la concurrence comme un concept de premier ordre : les goroutines et les canaux (channels). Les goroutines sont des threads légers contrôlés par le runtime Go, ce qui signifie que vous pouvez exécuter des milliers, voire des millions d'opérations de manière concurrente avec une surcharge minimale.

La philosophie de communication dans les Channels offre un moyen sécurisé de communication entre les goroutines, et elle inclut l'expression « ne communiquez pas en partageant la mémoire ; partagez la mémoire en communiquant ». Une telle conception rend la programmation concurrente plus conviviale et sans erreur.

En matière de parallélisme, Go alloue automatiquement les goroutines à plusieurs cœurs de CPU selon la variable d'environnement GOMAXPROCS, et l'exécution parallèle est réalisée automatiquement. Cela rend Go particulièrement efficace dans la construction de systèmes parallèles tels que les serveurs web, les outils réseau et les systèmes distribués.

### Rust

Rust fournit une programmation concurrente et parallèle avec une sécurité mémoire sans dégradation des performances. Le système de propriété (ownership) du langage élimine toutes les formes de courses aux données (data races) au moment de la compilation, ce qui signifie que toute la catégorie de bugs de concurrence trouvés dans d'autres langages n'existe pas.

Dans le cas des opérations asynchrones, vous pouvez appliquer la syntaxe de Rust aux opérations de type asynchrone avec des bibliothèques de runtime telles que tokio ou async-std et obtenir des performances similaires au C++ sans sacrifier la sécurité.

La bibliothèque Rayon rend le parallélisme des données extrêmement facile. Parfois, vous pouvez paralléliser un calcul en remplaçant `.iter()` par `.par_iter()`. Les pools de threads et les canaux de Rust vous donnent un contrôle de bas niveau là où c'est nécessaire, et le système de types maintient les threads en sécurité, s'assurant que les problèmes ne surviennent pas dans votre code.

## Conclusion

La concurrence et le parallélisme représentent les piliers fondamentaux de l'architecture informatique moderne. Ce ne sont pas des mots à la mode interchangeables, mais plutôt des paradigmes distincts qui répondent à des défis différents :

La concurrence se concentre sur la structure du programme et la coordination efficace des tâches. Elle permet aux systèmes de gérer plusieurs opérations sur des périodes de temps qui se chevauchent, maximisant l'utilisation des ressources et la réactivité.

Le parallélisme se concentre sur le débit de calcul et la vitesse d'exécution. Il divise le travail sur plusieurs processeurs pour terminer les tâches plus rapidement grâce à l'exécution simultanée.

Les systèmes les plus puissants combinent stratégiquement les deux approches, en appliquant chacune là où elle offre le plus grand avantage.

La prochaine fois que vous ferez face à un défi de performance, posez-vous ces questions critiques :

1. Mon goulot d'étranglement est-il causé par l'attente (lié aux E/S) ou par le calcul (lié au CPU) ?
    
2. Est-ce que j'essaie de gérer plus de tâches simultanément ou de terminer les tâches plus rapidement ?
    
3. Ai-je besoin d'une meilleure utilisation des ressources ou d'un débit de calcul brut ?
    

Vos réponses vous guideront vers la bonne solution. Comprendre quand appliquer la concurrence, quand exploiter le parallélisme et quand les combiner est ce qui sépare les solutions adéquates des solutions exceptionnelles. Ces connaissances vous permettent de construire des systèmes qui sont non seulement rapides mais aussi efficaces, évolutifs et économiquement viables.

Maîtrisez ces concepts et vous vous retrouverez équipé pour relever des défis d'ingénierie de plus en plus complexes avec confiance et précision.

### Ressources d'apprentissage supplémentaires

* ["Go Concurrency Patterns" par Rob Pike (Google Tech Talk)](https://www.youtube.com/watch?v=f6kdp27TYZs)
    
* ["Concurrency is not Parallelism" par Rob Pike](https://www.youtube.com/watch?v=oV9rvDllKEg&utm_source=chatgpt.com)
    
* [Documentation officielle de Python AsyncIO](https://docs.python.org/3/library/asyncio.html)
    
* [Real Python: Concurrency and Parallelism in Python](https://realpython.com/python-concurrency/)
    
* [Java Concurrency in Practice par Brian Goetz](https://jcip.net/?utm_source=chatgpt.com)
    
* [Documentation Apache Spark pour le parallélisme Big Data](https://spark.apache.org/docs/latest/)