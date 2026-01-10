---
title: 'Python multithread : se faufiler à travers un goulot d''étranglement d''I/O
  ?'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-03-01T00:16:00.000Z'
originalURL: https://freecodecamp.org/news/multithreaded-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover.png
tags:
- name: Computers
  slug: computers
- name: multithreading
  slug: multithreading
- name: Python
  slug: python
seo_title: 'Python multithread : se faufiler à travers un goulot d''étranglement d''I/O
  ?'
seo_desc: 'How taking advantage of parallelism in Python can make your software orders
  of magnitude faster.

  I recently developed a project that I called Hydra: a multithreaded link checker
  written in Python. Unlike many Python site crawlers I found while resear...'
---

### Comment tirer parti du parallélisme en Python peut rendre votre logiciel des ordres de grandeur plus rapide.

J'ai récemment développé un projet que j'ai appelé [Hydra](https://github.com/victoriadrake/hydra-link-checker) : un vérificateur de liens multithread écrit en Python. Contrairement à de nombreux crawlers Python que j'ai trouvés lors de mes recherches, Hydra utilise uniquement des bibliothèques standard, sans dépendances externes comme BeautifulSoup. Il est destiné à être exécuté dans le cadre d'un processus CI/CD, donc une partie de son succès dépendait de sa rapidité.

Les threads multiples en Python sont un sujet un peu épineux (et je ne m'en excuse pas) dans le sens où l'interpréteur Python n'autorise pas réellement l'exécution simultanée de plusieurs threads.

Le [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock), ou GIL, de Python empêche plusieurs threads d'exécuter des bytecodes Python en même temps. Chaque thread qui souhaite s'exécuter doit d'abord attendre que le GIL soit libéré par le thread en cours d'exécution. Le GIL est à peu près comme le microphone dans un panel de conférence à petit budget, sauf que personne ne peut crier.

Cela a l'avantage d'éviter les [conditions de course](https://en.wikipedia.org/wiki/Race_condition). Cependant, cela manque des avantages de performance offerts par l'exécution de plusieurs tâches en parallèle. (Si vous souhaitez une piqûre de rappel sur la concurrency, le parallélisme et le multithreading, voir [Concurrency, parallelism, and the many threads of Santa Claus](https://victoria.dev/blog/concurrency-parallelism-and-the-many-threads-of-santa-claus/).)

Bien que je préfère Go pour ses primitives de première classe qui supportent la concurrency (voir [Goroutines](https://tour.golang.org/concurrency/1)), les destinataires de ce projet étaient plus à l'aise avec Python. J'ai pris cela comme une opportunité de tester et d'explorer !

L'exécution simultanée de plusieurs tâches en Python n'est pas impossible ; cela demande simplement un peu plus de travail. Pour Hydra, l'avantage principal est de surmonter le goulot d'étranglement d'entrée/sortie (I/O).

Pour obtenir des pages web à vérifier, Hydra doit aller sur Internet et les récupérer. Comparé aux tâches effectuées par le CPU seul, aller sur le réseau est relativement plus lent. À quel point ?

Voici des temps approximatifs pour des tâches effectuées sur un PC typique :

|         | Tâche                                | Temps                            |
| ------- | ----------------------------------- | ------------------------------- |
| CPU     | exécuter une instruction typique     | 1/1,000,000,000 sec = 1 nanosec |
| CPU     | récupérer depuis la mémoire cache L1 | 0.5 nanosec                     |
| CPU     | prédiction de branche erronée        | 5 nanosec                       |
| CPU     | récupérer depuis la mémoire cache L2 | 7 nanosec                       |
| RAM     | verrouillage/déverrouillage de Mutex | 25 nanosec                      |
| RAM     | récupérer depuis la mémoire principale | 100 nanosec                     |
| Réseau  | envoyer 2K octets sur un réseau 1Gbps | 20,000 nanosec                  |
| RAM     | lire 1MB séquentiellement depuis la mémoire | 250,000 nanosec                 |
| Disque  | récupérer depuis un nouvel emplacement de disque (recherche) | 8,000,000 nanosec   (8ms)       |
| Disque  | lire 1MB séquentiellement depuis le disque | 20,000,000 nanosec  (20ms)      |
| Réseau  | envoyer un paquet des États-Unis vers l'Europe et retour | 150,000,000 nanosec (150ms)     |

Peter Norvig a publié ces chiffres il y a quelques années dans [Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html#answers). Comme les ordinateurs et leurs composants changent d'année en année, les chiffres exacts présentés ci-dessus ne sont pas le point principal. Ce que ces chiffres aident à illustrer, c'est la différence, en ordres de grandeur, entre les opérations.

Comparez la différence entre la récupération depuis la mémoire principale et l'envoi d'un simple paquet sur Internet. Bien que ces deux opérations se produisent en moins de temps qu'il n'en faut pour cligner des yeux (littéralement) d'un point de vue humain, vous pouvez voir que l'envoi d'un simple paquet sur Internet est plus d'un million de fois plus lent que la récupération depuis la RAM. C'est une différence qui, dans un programme à thread unique, peut rapidement s'accumuler pour former des goulots d'étranglement problématiques.

Dans Hydra, la tâche d'analyse des données de réponse et d'assemblage des résultats dans un rapport est relativement rapide, car tout se passe sur le CPU. La partie la plus lente de l'exécution du programme, de plus de six ordres de grandeur, est la latence du réseau. Non seulement Hydra doit récupérer des paquets, mais des pages web entières !

Une façon d'améliorer les performances de Hydra est de trouver un moyen pour que les tâches de récupération de pages s'exécutent sans bloquer le thread principal.

Python offre quelques options pour effectuer des tâches en parallèle : plusieurs processus ou plusieurs threads. Ces méthodes vous permettent de contourner le GIL et d'accélérer l'exécution de différentes manières.

## Plusieurs processus

Pour exécuter des tâches parallèles en utilisant plusieurs processus, vous pouvez utiliser [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) de Python. Une sous-classe concrète de [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor) du module [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html), `ProcessPoolExecutor` utilise un pool de processus créés avec le module [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) pour éviter le GIL.

Cette option utilise des sous-processus workers qui, par défaut, correspondent au nombre de processeurs sur la machine. Le module `multiprocessing` vous permet de paralléliser au maximum l'exécution de fonctions à travers les processus, ce qui peut vraiment accélérer les tâches liées au calcul (ou [CPU-bound](https://en.wikipedia.org/wiki/CPU-bound)).

Puisque le principal goulot d'étranglement pour Hydra est l'I/O et non le traitement à effectuer par le CPU, je suis mieux servi en utilisant plusieurs threads.

## Plusieurs threads

De manière appropriée nommé, [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) de Python utilise un pool de threads pour exécuter des tâches asynchrones. Également une sous-classe de [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor), il utilise un nombre défini de threads workers maximum (au moins cinq par défaut, selon la formule `min(32, os.cpu_count() + 4)`) et réutilise les threads inactifs avant d'en démarrer de nouveaux, ce qui le rend assez efficace.

Voici un extrait de Hydra avec des commentaires montrant comment Hydra utilise `ThreadPoolExecutor` pour atteindre le bonheur multithread parallèle :

```py
# Créer la classe Checker
class Checker:
    # File d'attente des liens à vérifier
    TO_PROCESS = Queue()
    # Nombre maximum de workers à exécuter
    THREADS = 100
    # Secondes maximum à attendre pour une réponse HTTP
    TIMEOUT = 60

    def __init__(self, url):
        ...
        # Créer le pool de threads
        self.pool = futures.ThreadPoolExecutor(max_workers=self.THREADS)


def run(self):
    # Exécuter jusqu'à ce que la file TO_PROCESS soit vide
    while True:
        try:
            target_url = self.TO_PROCESS.get(block=True, timeout=2)
            # Si nous n'avons pas déjà vérifié ce lien
            if target_url["url"] not in self.visited:
                # Le marquer comme visité
                self.visited.add(target_url["url"])
                # Soumettre le lien au pool
                job = self.pool.submit(self.load_url, target_url, self.TIMEOUT)
                job.add_done_callback(self.handle_future)
        except Empty:
            return
        except Exception as e:
            print(e)

```

Vous pouvez consulter le code complet dans le [dépôt GitHub de Hydra](https://github.com/victoriadrake/hydra-link-checker).

## D'un seul thread à multithread

Si vous souhaitez voir l'effet complet, j'ai comparé les temps d'exécution pour la vérification de mon site web entre un prototype de programme à thread unique et Hydra multithread.

```text
time python3 slow-link-check.py https://victoria.dev

real    17m34.084s
user    11m40.761s
sys     0m5.436s


time python3 hydra.py https://victoria.dev

real    0m15.729s
user    0m11.071s
sys     0m2.526s

```

Le programme à thread unique, qui bloque sur l'I/O, a mis environ dix-sept minutes. Lorsque j'ai exécuté la version multithread pour la première fois, elle s'est terminée en 1m13.358s - après un peu de profilage et de réglage, elle a pris un peu moins de seize secondes.

Encore une fois, les temps exacts ne signifient pas grand-chose ; ils varieront en fonction de facteurs tels que la taille du site à crawler, votre vitesse de réseau et l'équilibre de votre programme entre le surcoût de la gestion des threads et les avantages du parallélisme.

La chose la plus importante, et le résultat que je prendrai n'importe quel jour, est un programme qui s'exécute des ordres de grandeur plus rapidement.