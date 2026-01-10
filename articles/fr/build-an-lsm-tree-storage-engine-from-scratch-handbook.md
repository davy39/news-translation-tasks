---
title: Comment construire un moteur de stockage LSM-Tree à partir de zéro – Le guide
  complet
author: Ramesh Sinha
date: '2025-12-18T20:25:02.609Z'
originalURL: https://freecodecamp.org/news/build-an-lsm-tree-storage-engine-from-scratch-handbook
description: 'Les bases de données sont l''une des parties les plus importantes d''un
  système logiciel. Elles nous permettent de stocker d''énormes quantités de données
  de manière organisée et de les récupérer efficacement quand nous en avons besoin.

  À l''époque, lorsque le volume de données était relativement faible, les ingénieurs...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766089431510/433ff03f-8aca-4a87-82d3-0b6d6c1f371c.png
tags:
- name: Databases
  slug: databases
- name: lsmtree
  slug: lsmtree
- name: storage solutions
  slug: storage-solutions
- name: Go Language
  slug: go
- name: heap
  slug: heap
- name: handbook
  slug: handbook
seo_desc: 'Databases are one of the most important parts of a software system. They
  allow us to store huge amounts of data in an organized way and retrieve it efficiently
  when we need it.

  In the early days, when the volume of data was relatively small, engineer...'
---


Les bases de données sont l'un des composants les plus essentiels d'un système logiciel. Elles nous permettent de stocker d'énormes quantités de données de manière organisée et de les récupérer efficacement lorsque nous en avons besoin.

À l'époque, lorsque le volume de données était relativement faible, les ingénieurs privilégiaient la récupération rapide des données et stockaient celles-ci dans des [structures B-tree](https://en.wikipedia.org/wiki/B-tree) qui rendaient la recherche efficace.

Mais au fil du temps, nous avons commencé à construire des systèmes devant ingérer des quantités massives de données telles que des logs, des métriques, des likes, des chats et des tweets. Il est alors devenu nécessaire de concevoir un système de stockage qui accélérerait l'écriture.

L'un de ces systèmes de stockage est l'LSM-tree (Log-Structured Merge tree).

Dans ce tutoriel, plutôt que de plonger immédiatement dans les concepts théoriques d'un système de stockage LSM-Tree, j'adopterai une approche pratique axée sur les problèmes. Je pense que l'apprentissage par la résolution de problèmes est bien plus efficace et stimulant que la simple mémorisation de concepts.

En abordant ces idées de manière progressive, mon objectif est de vous guider étape par étape à travers des défis et des solutions d'ingénierie réels, vous offrant une place de choix pour observer les subtilités de la construction d'un moteur de stockage robuste à partir de zéro.

Nous commencerons par identifier les défis concrets qui surviennent lors de la conception d'une base de données – comme la gestion de charges de travail intensives en écriture, la garantie de la durabilité des données ou la gestion d'un stockage efficace. Ces défis prépareront le terrain pour chaque fonctionnalité et composant des LSM-Trees.

Grâce à cette méthode, nous explorerons les fondements des systèmes de stockage LSM-Tree et approfondirons leurs composants clés : MemTable, SSTable, Write-Ahead Log (WAL) et fichier Manifest.

Nous examinerons également les chemins d'écriture et de lecture, explorerons les mécanismes de durabilité et de récupération après crash, et conclurons par l'un des processus les plus critiques : la compaction.

À la fin de ce guide, vous comprendrez non seulement ce que sont ces composants, mais aussi pourquoi ils sont conçus ainsi et comment ils résolvent les défis uniques de la construction de bases de données modernes et performantes.

### **Ce que nous allons couvrir :**

1. [Prérequis](#heading-prerequis)
    
2. [Qu'est-ce qu'un LSM-Tree ?](#heading-qu-est-ce-qu-un-lsm-tree)
    
3. [Préface : Configuration pour construire une base de données LSM-Tree](#heading-preface-configuration-pour-construire-une-base-de-donnees-lsm-tree)
    
    * [Ensemble initial de fonctionnalités : Poser les bases du système de base de données](#heading-ensemble-initial-de-fonctionnalites-poser-les-bases-du-systeme-de-base-de-donnees)
        
    * [MemTable : Stockage de données en mémoire](#heading-memtable-stockage-de-donnees-en-memoire)
        
    * [SSTable : Persistance des données pour la durabilité](#heading-sstable-persistance-des-donnees-pour-la-durabilite)
        
    * [Le WAL (Write Ahead Log) : La récupération après crash simplifiée](#heading-le-wal-write-ahead-log-la-recuperation-apres-crash-simplifiee)
        
    * [Fichier Manifest : Suivi de l'état de la base de données](#heading-fichier-manifest-suivi-de-l-etat-de-la-base-de-donnees)
        
    * [Mise à jour et suppression : Gérer la mutabilité dans un système immuable](#heading-mise-a-jour-et-suppression-gerer-la-mutabilite-dans-un-systeme-immuable)
        
    * [Compaction : Nettoyage des données obsolètes et supprimées](#heading-compaction-nettoyage-des-donnees-obsoletes-et-supprimees)
        
4. [Conclusion](#heading-conclusion)
    
    * [Code complet](#heading-code-complet)
        

## **Prérequis**

Bien que ce tutoriel soit conçu pour être complet et accessible, il sera utile que vous possédiez des connaissances de base dans les domaines suivants :

* **Programmation en Golang** : La familiarité avec la syntaxe Go, la gestion des erreurs et les bibliothèques standards (par exemple `os`, `encoding/gob`, `container/heap`) facilitera le travail sur les exemples d'implémentation.
    
* **Structures de données et algorithmes de base** : Des concepts tels que les maps, les heaps (tas), certains algorithmes de tri et l'arrêt précoce sont exploités tout au long du tutoriel.
    
* **Compréhension du stockage persistant** : La connaissance des différences entre le stockage en mémoire et sur disque, ainsi que des opérations de lecture/écriture séquentielles par rapport aux opérations aléatoires, sera utile pour saisir les compromis liés aux performances.
    
* **Connaissances générales sur les bases de données** : Si vous êtes familier avec les bases de données clé-valeur ou les opérations CRUD (Create, Read, Update, Delete), vous aurez une longueur d'avance.
    
* **Concurrence** : Compréhension de base des threads et de la concurrence.
    

Bien que l'expérience dans ces domaines approfondisse votre compréhension des concepts et réduise la courbe d'apprentissage, je fournirai suffisamment de détails et d'explications pratiques à chaque étape pour vous assurer d'acquérir les connaissances nécessaires pour suivre et construire votre propre moteur de stockage basé sur un LSM-tree.

## Qu'est-ce qu'un LSM-Tree ?

Un arbre de fusion structuré en journaux (ou LSM-tree) est une structure de données qui rend les écritures en base de données extrêmement rapides en enregistrant d'abord les nouvelles données en mémoire, puis en les triant et en les fusionnant périodiquement dans des fichiers plus volumineux sur le disque.

Le terme « log » (journal) dans son nom fait référence au fait qu'il sauvegarde les données dans un format structuré en journaux (plutôt que de simplement les stocker). Nous reviendrons sur ce que sont ces journaux dans un instant.

Les LSM-trees continuent d'ajouter de nouvelles données aux données existantes, au lieu de chercher quelque chose qui existe déjà pour le mettre à jour. En d'autres termes, vous n'avez pas à dépenser de cycles CPU pour réfléchir à l'endroit où stocker les données – il suffit de les ajouter à la fin.

Un LSM-tree contient également le mot « tree » (arbre) dans son nom, mais stocke-t-il réellement les données dans un arbre ? Pas vraiment. L'« arbre » ici est principalement un concept abstrait. Il fait référence à l'organisation hiérarchique des niveaux (L0, L1, L2, etc.), et non à une structure de données arborescente avec des nœuds et des pointeurs. Encore une fois, nous reviendrons sur ces niveaux un peu plus tard, mais pour l'instant, disons simplement qu'il est logique de l'appeler un arbre étant donné qu'il stocke les données de manière hiérarchisée.

Notez simplement qu'il n'y a pas de structure d'arbre tangible en jeu (comme des arbres binaires ou des graphes) – ce n'est pas un stockage basé sur des nœuds.

Enfin, il y a la partie « merge » (fusion) du nom. Pour l'instant, qu'il suffise de dire que vous verrez bientôt comment ce moteur de stockage fusionne les données pour économiser de l'espace en évitant les doublons.

Personnellement, je pense que « Log-Structured Merge **System** » serait plus clair que « tree », mais « LSM tree » est le terme établi dans l'industrie, c'est donc celui que nous utiliserons.

## Préface : Configuration pour construire une base de données LSM-Tree

Maintenant que nous avons posé le contexte, mettons cette théorie en pratique et commençons à construire notre propre moteur de stockage de base de données basé sur un LSM-tree à partir de zéro.

Pour suivre ce tutoriel :

* Assurez-vous que Golang est installé sur votre système. Sinon, vous pouvez le télécharger et l'installer depuis le [site officiel de Go](https://go.dev/).
    
* Configurez votre environnement de développement et créez un nouveau module Go pour ce projet en exécutant : `go mod init lsm-db`
    
* Gardez un éditeur de code ou un IDE prêt pour tester les exemples.
    

### Ensemble initial de fonctionnalités : Poser les bases du système de base de données

Lorsque je conçois ou construis un système, j'aime imaginer que le système existe déjà, et je suppose que je peux simplement commencer à appeler des fonctions qui supportent les fonctionnalités du système. Je suivrai ce modèle ici et supposerai que les fonctions suivantes du LSM-tree existent et que nous pouvons les invoquer depuis [main.go](http://main.go).

```go
db, err := NewDB[string, string](3, 3) // il y a une fonctionnalité pour créer une nouvelle instance avec certains paramètres que nous verrons plus tard
db.Put("a", "apple") // une fonctionnalité pour ajouter une paire clé-valeur
db.Delete("a") // une fonctionnalité pour supprimer une clé
val, _ := db.Get("a") // une fonctionnalité pour obtenir une valeur à partir d'une clé
```

Au fur et à mesure de notre progression, j'introduirai des fonctionnalités essentielles telles que le stockage en mémoire, le vidage (flushing) des données sur le disque et la gestion des clés dupliquées. Nous explorerons également des composants plus avancés, notamment un Write-Ahead Log (WAL) pour garantir la tolérance aux pannes, un fichier Manifest pour maintenir l'état de la base de données lors des redémarrages de l'application, et un processus de compaction pour nettoyer les données redondantes ou obsolètes en fusionnant les anciennes SSTables.

À la fin de ce tutoriel, vous aurez une compréhension claire de la manière dont tous ces composants collaborent pour former un système de stockage robuste et efficace basé sur un LSM-tree.

### MemTable : Stockage de données en mémoire

Nous construisons un système de stockage de base de données, vous aurez donc naturellement besoin d'un moyen de stocker des données. Cela signifie qu'il vous faut un support de stockage. Ce support de stockage dans un LSM-tree est appelé une MemTable. Le « Mem » fait référence à son stockage en mémoire (in-memory). L'avantage du stockage en mémoire est qu'il est des ordres de grandeur plus rapide que le stockage sur disque.

Pour plus de simplicité, au cœur de la MemTable, vous pouvez utiliser une map (ou un dictionnaire selon le langage de programmation) comme structure de données sous-jacente pour stocker les paires clé-valeur. La map permet des recherches, des insertions et des suppressions rapides, ce qui la rend idéale pour le stockage en mémoire où la performance est cruciale. Ainsi, la structure de la MemTable ressemblera à ceci :

```go
type MemTable[K comparable, V any] struct {
    data map[K]V // c'est la map de stockage primaire. Elle est générique pour que vous
                  // puissiez stocker n'importe quel type de données
}
```

Le code ci-dessus définit une structure `MemTable`, où `data` est une map qui agit comme stockage principal pour nos paires clé-valeur. Puisque le champ `data` est une map, vous pourrez rapidement ajouter, récupérer ou supprimer des valeurs associées à une clé donnée.

Vous avez dû remarquer quelque chose de nouveau dans le code : l'utilisation de `<K comparable, V any>`. Cette syntaxe correspond aux **types génériques** de Go, qui nous permettent d'écrire du code flexible capable de gérer différents types de données.

Les génériques sont un moyen d'écrire du code indépendant de tout type de données spécifique. Ils vous permettent d'écrire des fonctions et des structures de données pouvant fonctionner avec un string, un int, un float ou tout type personnalisé que vous définissez, sans sacrifier la sécurité des types.

Dans le code ci-dessus, K et V sont des paramètres de type. Ils signifient : « Cette MemTable peut fonctionner avec n'importe quel type de clé K qui est comparable, et n'importe quel type de valeur V. »

Maintenant que vous avez la MemTable, réfléchissez aux fonctions qu'elle devrait fournir à ses clients. Eh bien, les clients doivent pouvoir sauvegarder et récupérer des valeurs associées à une clé, donc les fonctions suivantes s'intégreraient naturellement :

```go
func (m *MemTable[K, V]) Put(key K, value V) {
    m.data[key] = value
}

func (m *MemTable[K, V]) Get(key K) (V, bool) {
    value, ok := m.data[key]
    var zero V
    if !ok {
        return zero, false
    }
    return value, true
}
```

Le code ci-dessus contient les fonctions `Put` et `Get` – décomposons-les :

* **Put** : Cette fonction permet au client d'insérer une paire clé-valeur dans la MemTable. Si la clé existe déjà dans la map, sa valeur sera mise à jour avec la nouvelle valeur fournie en argument. C'est effectivement l'opération d'écriture (`write`) de notre magasin clé-valeur.
    
* **Get** : Cette fonction est responsable de la récupération d'une valeur associée à une clé donnée dans la MemTable. Elle retourne deux valeurs : la valeur elle-même (de type `V`) et un booléen (`true` ou `false`). Le booléen indique si la clé a été trouvée dans la map. Si la clé n'existe pas, la fonction retourne une « valeur zéro » (plus de détails ci-dessous) ainsi que `false`.
    

Avez-vous remarqué `var zero V` ?

C'est assez intéressant. Imaginez une situation où nous ne récupérons pas de valeur de la map – disons que la clé n'est pas là, ou qu'un autre problème survient. Que doit retourner la fonction `Get` dans ce cas ? Peut-elle retourner un int (0), ou une chaîne "Not found", ou un objet aléatoire (foo) ? Vous ne connaissez pas encore le type (Génériques), vous ne pouvez donc pas lui dire quoi retourner.

Dans ce cas, le compilateur vient à la rescousse. Go possède ce concept de valeur zéro (zero value) : tout doit avoir une valeur par défaut. Un int a 0, un string a "", un bool a false, et un pointeur, une slice ou une map ont nil. En disant `var zero V`, vous dites au compilateur : « Je ne connais pas encore le type, détermine-le lors de la compilation et utilise-le ici comme type de retour. » Élégant !

J'ai oublié une chose cependant : comment un client invoquerait-il ces fonctions ? Exact, nous avons besoin d'un moyen de construire le type MemTable.

Pour construire et initialiser une MemTable, nous pouvons utiliser une **factory function** : un modèle de programmation courant pour créer et retourner de nouveaux objets ou instances sans exposer directement les détails de l'implémentation sous-jacente.

```go
func NewMemTable[K comparable, V any]() *MemTable[K, V] {
    return &MemTable[K, V]{
        data: make(map[K]V),
    }
}
```

Remarquez comment nous avons initialisé le champ data en utilisant la fonction intégrée `make`. Voici pourquoi nous faisons cela :

Go possède une fonction intégrée appelée `make`, utilisée pour allouer et initialiser des slices, des maps et des channels. Cette allocation garantit qu'ils sont prêts à l'emploi sans risque de paniques à l'exécution (runtime panics).

Vous pourriez vous demander, pourquoi ne pas utiliser la fonction `new` pour allouer la map ? Après tout, les développeurs venant d'autres horizons (comme le C++ ou Java) pourraient s'attendre à utiliser `new` pour tous les types d'allocation mémoire. Mais Go **différencie la gestion de la mémoire pour les types composites par rapport aux types basiques/numériques**, et c'est là que `make` intervient.

Cette distinction est importante car la fonction `new` ne fait qu'**allouer de la mémoire** pour un objet et retourne un *pointeur* vers cette mémoire. L'objet lui-même n'est pas initialisé, ce qui signifie que bien que la mémoire soit allouée, la map n'est pas prête à l'emploi. Si nous essayons d'effectuer des opérations (comme ajouter une paire clé-valeur) sur une `map` allouée uniquement avec `new`, cela provoquera une panique à l'exécution car la map n'a pas été correctement initialisée.

Par exemple :

```go
m := new(map[string]int) // Alloue un pointeur vers une map non initialisée
(*m)["a"] = 1            // Cela va paniquer car la map n'est pas initialisée
```

D'un autre côté, `make` à la fois alloue et **initialise la map**, garantissant qu'elle est immédiatement fonctionnelle. C'est pourquoi la manière correcte de créer une map est :

```go
m1 := make(map[string]int) // Initialise correctement la map
m1["a"] = 1                // Cela fonctionne comme prévu
```

Maintenant que vous avez la MemTable qui peut stocker des données en mémoire, connectons-la et utilisons-la.

Mais avant cela, vous souvenez-vous qu'au début j'ai utilisé des invocations de fonctions comme `db.Put` et `db.Get` ? Eh bien, qu'est-ce que `db` ? Puisque nous construisons un système de stockage de base de données, il est plus logique de nommer l'interface `db` au lieu de MemTable, n'est-ce pas ? Et pour être honnête, il semble que la MemTable va faire partie du système de base de données, et non être le système entier, n'est-ce pas ?

Même s'il n'est pas intuitif pour le moment de définir quelque chose comme un type DB, faisons-le. Croyez-moi, cela deviendra plus clair au fur et à mesure. Ce type `db` enveloppera l'ajout et la récupération de données de la MemTable.

```go
type DB[K comparable, V any] struct {
    memtable *MemTable[K, V]
}

// factory function pour le type DB
func NewDB[K comparable, V any]() (*DB[K, V], error) {
    memtable := NewMemTable[K, V]()
    return &DB[K, V]{
        memtable: memtable,
    }, nil
}
```

Définissons simplement les fonctions Put et Get qui invoqueront les fonctions correspondantes dans la MemTable :

```go
func (db *DB[K, V]) Put(key K, value V) error {
    db.memtable.Put(key, value)
    return nil
}

func (db *DB[K, V]) Get(key K) (V, error) {
    if val, ok := db.memtable.Get(key); ok {
        return val, nil
    }
    var zero V
    return zero, errors.New("key not found")
}
```

Intégrons tout ce que nous avons construit jusqu'à présent et exécutons-le. Pour l'exécuter, ajoutez le code ci-dessous dans main.go et lancez-le avec `go run main.go`.

```go
db, err := NewDB[string, string]()
if err != nil {
    log.Fatalf("Failed to create DB: %v", err)
}
db.Put("a", "apple")
val, _ := db.Get("a")
log.Printf("Get('a') = %s (should be 'apple')", val)
```

Regardez ça, vous avez construit une base de données en mémoire où vos clients peuvent stocker et récupérer des données. Elle utilise des génériques, vous pouvez donc stocker n'importe quel type de valeurs (int, string, objets).

Supposons maintenant que vous livriez cette solution et qu'elle crash. Vos clients perdront toutes leurs données. Pourquoi cela pourrait-il crasher ? D'une part, la mémoire est limitée et à un moment donné, vous allez en manquer. Il y a donc deux problèmes majeurs avec le stockage uniquement en mémoire :

1. Ce n'est pas durable.
    
2. L'utilisation illimitée de la mémoire va faire crasher le système.
    

Comment résoudre ces problèmes ?

Voici une idée : et si nous vidions (flush) les données de la MemTable sur le disque à intervalles réguliers ? De cette façon, nous pouvons garantir que la MemTable ne dépasse pas certaines limites. De plus, si la base de données crash, nous ne perdrons pas toutes les données. Nous perdrons toujours les données qui n'ont pas encore été vidées, mais c'est bien mieux que de tout perdre.

### SSTable : Persistance des données pour la durabilité

Une SSTable est une « Sorted String Table ». J'aurais aimé qu'ils l'appellent une table de « Stockage Secondaire », mais historiquement les clés et les valeurs étaient des chaînes de caractères – d'où le nom « Sorted String Table ». Une SSTable est un fichier persistant, ordonné et immuable qui stocke des paires clé-valeur. C'est un fichier stocké sur disque, il est donc clair qu'il est persistant (durable).

Discutons de quelques caractéristiques clés de la SSTable :

* **Elle est ordonnée** : Il y a un avantage à stocker les clés dans un ordre trié, car cela rend la recherche de clés plus rapide et efficace. Sans cela, vous devriez parcourir tout le fichier pour trouver une clé. Plus tard, je signalerai du code qui tire parti du stockage trié.
    
* **Elle est immuable** : Une fois qu'un fichier SSTable est écrit, il ne peut plus être modifié. Pour mettre à jour ou supprimer une clé, vous devez écrire un nouvel enregistrement dans une SSTable plus récente. Cela simplifie la conception et rend les lectures et écritures très prévisibles.
    

Mais attendez, comment cela simplifie-t-il la conception ?

L'une des choses les plus complexes en génie logiciel est de gérer la concurrence. Disons que vous écrivez dans un fichier et qu'un autre thread le met à jour en même temps. Comment savoir si vous avez les bonnes données ?

Avec une conception immuable, vous n'avez pas du tout à vous en soucier. Vous êtes sûr à 100 % que les données que vous lisez n'ont été altérées par personne d'autre. Je considère cela comme une simplification massive : vous n'avez pas à gérer les verrous (locks), la famine (starvation), l'obsolescence, etc.

#### Comment cela rend-il le chemin d'écriture prévisible ?

Je répondrai partiellement ici et j'y reviendrai quand nous aurons complété davantage l'implémentation. Vous verrez que chaque écriture dans notre code suit exactement les mêmes étapes. Il n'y a pas une seule condition différente ou cas particulier.

Dans une base de données traditionnelle (utilisant un B-Tree), une écriture typique implique :

1. Trouver les données sur le disque.
    
2. Lire le bloc de données du disque vers la mémoire.
    
3. Modifier les données en mémoire.
    
4. Réécrire le bloc entier sur le disque.
    

Plus il y a d'étapes, plus les performances peuvent devenir imprévisibles, car l'écriture peut être rapide si les données sont déjà dans le cache mémoire ou lente si plusieurs recherches sur disque (disk seeks) sont nécessaires.

Certes, notre code est une version simplifiée à l'extrême, mais l'extension de ce concept reste vraie dans les implémentations LSM réelles.

#### Comment cela rend-il le chemin de lecture prévisible ?

La lecture est prévisible car n'importe quel nombre de threads peut lire le même fichier SSTable en même temps sans aucun problème, avec la certitude que les données n'ont pas été mises à jour.

En revanche, lors de la lecture d'une structure de données mutable, vous devez craindre qu'un autre thread soit en train de modifier les données que vous essayez de lire.

Pour éviter cela, les bases de données basées sur les B-Tree utilisent des mécanismes de verrouillage complexes, ce qui ajoute de la surcharge et de l'imprévisibilité.

Je dois toutefois apporter une nuance : la lecture dans un stockage LSM-tree n'est pas toujours prévisible. Elle peut être plus rapide si les données sont lues depuis la mémoire et elle peut être très lente si plusieurs SSTables doivent être consultées pour trouver la clé.

Cela dit, vous n'avez pas à vous soucier d'autres goulots d'étranglement de performance dus aux verrous. Autrement dit, dans un stockage B-Tree, votre requête de lecture peut être plus lente parce qu'une autre requête d'écriture détient un verrou. Dans des cas d'utilisation simples à faible concurrence, vous obtiendrez généralement d'excellentes performances de lecture avec une structure B-Tree, mais cet avantage s'estompe à mesure que la concurrence augmente.

L'LSM-tree a été conçu pour des cas d'utilisation hautement concurrents et intensifs en écriture, et parfois, des lectures plus lentes sont un compromis acceptable.

Ce qu'il faut retenir pour mieux concevoir vos systèmes, c'est que les B-trees sont préférables pour les charges de travail intensives en lecture. Les lectures sont généralement plus rapides et plus cohérentes, mais les performances peuvent présenter des valeurs aberrantes (outliers) imprévisibles sous une forte concurrence d'écriture en raison du verrouillage.

Un LSM-tree est préférable pour les charges de travail intensives en écriture. Les écritures sont beaucoup plus rapides. Les lectures sont généralement plus lentes et plus variables, mais leur profil de performance est plus prévisible sous une forte concurrence d'écriture car il n'y a pas de verrouillage lecture-écriture.

Implémentons une SSTable pour voir comment elle fonctionne.

**Le chemin d'écriture :**

```go
func writeSSTable[K comparable, V any](memtable *MemTable[K, V], path string) (*SSTable[K, V], error) {
    file, err := os.Create(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()
    
    pairs := make([]Pair[K, V], 0, len(memtable.data))
    for k, v := range memtable.data {
        pairs = append(pairs, Pair[K, V]{Key: k, Value: v})
    }
    
    sort.Slice(pairs, func(i, j int) bool {
        return any(pairs[i].Key).(string) < any(pairs[j].Key).(string)
    })
    
    encoder := gob.NewEncoder(file)
    for _, pair := range pairs {
        if err := encoder.Encode(pair); err != nil {
            return nil, err
        }
    }
    
    return &SSTable[K, V]{path: path}, nil
}
```

Les points suivants sont importants à noter dans le code ci-dessus :

1. `sort.Slice` : Vous vous souvenez que j'ai parlé d'ordre plus tôt ? Nous stockons les données dans la SSTable de manière triée, et nous verrons comment nous en tirons parti dans le chemin de lecture.
    
2. J'ai utilisé le package d'encodage `gob`. Un encodeur vous simplifie la vie car il diffuse les données vers et depuis les structures de données Go vers des flux binaires pouvant être stockés sur disque. Il gère toute la complexité de la représentation des types, des noms de champs et des valeurs dans un format binaire standardisé, afin que vous n'ayez pas à le faire.
    

**Le chemin de lecture :**

```go
func (s *SSTable[K, V]) Get(key K) (V, error) {
    file, err := os.Open(s.path)
    if err != nil {
        var zero V
        return zero, err
    }
    defer file.Close()
    
    decoder := gob.NewDecoder(file)
    
    for {
        var pair Pair[K, V]
        if err := decoder.Decode(&pair); err != nil {
            if err == io.EOF {
                break
            }
            var zero V
            return zero, err
        }
        
        // pour une comparaison simple, nous supposons que la clé est juste un string
        keyInDB := any(pair.Key).(string)
        if keyInDB == any(key).(string) {
            if any(pair.Value).(string) == TOMBSTONE {
                var zero V
                return zero, ErrNotFound
            }
            return pair.Value, nil
        }
        
        if keyInDB > any(key).(string) {
            var zero V
            return zero, ErrNotFound
        }
    }
    
    var zero V
    return zero, ErrNotFound
}
```

Sur le chemin de lecture, regardez `keyInDB > any(key).(string)`. C'est l'un des exemples de la façon dont nous avons profité du stockage des données dans un ordre de clés trié. Dès que nous trouvons une clé dans la SSTable **qui est supérieure à la clé** que nous recherchons, nous arrêtons de chercher car il est évident que toutes les autres clés seront supérieures à celle-ci, donc nous ne trouverons plus notre clé.

Maintenant que vous avez implémenté la SSTable, il vous suffit de décider quand vider les données de la MemTable vers la SSTable. Vous pouvez simplement définir une taille maximale pour la MemTable et la vider sur le disque lors du chemin d'écriture lorsque la taille maximale est atteinte.

Je saute certaines variables, le code répétitif (boilerplate) et je simplifie les choses par souci de brièveté. Je posterai un lien GitHub avec l'implémentation complète plus tard.

```go
type DB[K comparable, V any] struct {
    memtable        *MemTable[K, V]
    maxMemtableSize int
    memtableSize    int
    sstables        []*SSTable[K, V]
    sstableCounter  int
}

func NewDB[K comparable, V any](maxMemtableSize int) (*DB[K, V], error) {
    sstables := make([]*SSTable[K, V], 0)
    memtable := NewMemTable[K, V]()
    
    return &DB[K, V]{
        memtable:        memtable,
        maxMemtableSize: maxMemtableSize,
        sstables:        sstables,
    }, nil
}

func (db *DB[K, V]) Put(key K, value V) error {
    db.memtable.Put(key, value)
    db.memtableSize++
    
    if db.memtableSize >= db.maxMemtableSize {
        if err := db.flushMemtable(); err != nil {
            return err
        }
    }
    
    return nil
}

func (db *DB[K, V]) flushMemtable() error {
    sstablePath := fmt.Sprintf("data-%d.sstable", db.sstableCounter)
    sstable, err := writeSSTable(db.memtable, sstablePath)
    if err != nil {
        return err
    }
    
    db.sstables = append(db.sstables, sstable)
    db.sstableCounter++
    db.memtable = NewMemTable[K, V]()
    db.memtableSize = 0
    
    return nil
}
```

Vous remarquerez que chaque fois que nous vidons sur le disque, nous écrivons dans une nouvelle SSTable au lieu d'utiliser une seule SSTable pour toute la base de données. C'est l'aspect d'immuabilité dont nous avons discuté plus tôt.

```go
func (db *DB[K, V]) Get(key K) (V, error) {
    if val, ok := db.memtable.Get(key); ok {
        return val, nil
    }
    
    for i := len(db.sstables) - 1; i >= 0; i-- {
        sstable := db.sstables[i]
        val, err := sstable.Get(key)
        if err != nil {
            if err == ErrNotFound {
                continue
            }
            var zero V
            return zero, err
        }
        return val, nil
    }
    
    var zero V
    return zero, ErrNotFound
}
```

Un aspect important à noter sur le chemin de lecture est que nous lisons d'abord la SSTable la plus récente. C'est parce que la SSTable la plus récente contient la valeur la plus à jour pour la clé.

Ainsi, supposons que vous ayez une clé "a" avec la valeur "apple", et qu'en cours de route vous mettiez à jour cette valeur pour "a" en "apricot". Vous l'auriez vidée dans une nouvelle SSTable (pour l'immuabilité), et donc si vous deviez lire une SSTable plus ancienne en premier, vous obtiendriez l'ancienne valeur. En lisant d'abord la SSTable la plus récente, nous obtenons la valeur correcte et nous n'avons pas à nous soucier de mettre à jour les anciennes SSTables.

### Le WAL (Write Ahead Log) : La récupération après crash simplifiée

Maintenant que nous avons une SSTable, nos données sont durables et nous sommes à l'abri de la perte de données en cas de crash. Sommes-nous vraiment en sécurité, cependant ? Imaginez un scénario où un crash survient avant que nous ne vidions les données dans la SSTable. Nous savons que la MemTable a un seuil maximal, et jusque-là, les données vivent en mémoire. Nous sommes donc toujours susceptibles de perdre des données si un crash survient avant le flush.

C'est là que le WAL (Write Ahead Log) entre en jeu. C'est l'aspect le plus important de l'LSM-tree.

Nous suivrons une règle simple : « Avant d'écrire une donnée dans la MemTable en mémoire, nous l'écrivons d'abord dans un fichier journal (log) sur le disque. »

Si un crash survient et que la base de données redémarre, la première chose qu'elle fait est de chercher un WAL, de le lire s'il en trouve un, et de rejouer toutes les données dans la MemTable. Ce processus reconstruit la MemTable exactement dans l'état où elle se trouvait juste avant le crash.

Il est naturel de penser que si toutes vos écritures sont d'abord écrites sur le disque, cela impactera les performances. Vous n'avez pas tort, mais il y a des nuances.

Les écritures dans le WAL sont différentes car elles sont en mode ajout uniquement (append-only) et séquentielles, ce qui signifie que des recherches aléatoires sur disque ne sont pas nécessaires. Sur un disque dur mécanique traditionnel (HDD), c'est rapide car la tête de lecture/écriture du disque n'a pas à se déplacer vers un nouvel emplacement. Sur un disque SSD moderne, les écritures séquentielles sont également beaucoup plus rapides que les écritures aléatoires.

Le léger impact sur les performances que nous acceptons est un compromis nécessaire pour la durabilité.

Maintenant que nous savons ce que fait le WAL, implémentons-le. Les deux fonctions clés du WAL sont d'écrire dans un fichier sur disque et de rejouer la MemTable au démarrage.

Notez que dans la factory function ci-dessous (`NewWAL`), le fichier a été ouvert en mode ajout (append).

```go
func NewWAL[K comparable, V any](path string) (*WAL[K, V], error) {
    file, err := os.OpenFile(path, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        return nil, err
    }
    return &WAL[K, V]{
        file:    file,
        encoder: gob.NewEncoder(file),
    }, nil
}

func (wal *WAL[K, V]) Write(key K, value V) error {
    entry := WALEntry[K, V]{Key: key, Value: value}
    return wal.encoder.Encode(&entry)
}

func ReplayWAL[K comparable, V any](path string) (*MemTable[K, V], error) {
    memtable := NewMemTable[K, V]()
    file, err := os.Open(path)
    if err != nil {
        if os.IsNotExist(err) {
            // Si le fichier n'existe pas, c'est correct. Retourner une memtable vide.
            return memtable, nil
        }
        return nil, err
    }
    defer file.Close()
    
    decoder := gob.NewDecoder(file)
    for {
        var entry WALEntry[K, V]
        if err := decoder.Decode(&entry); err != nil {
            if err == io.EOF {
                break // Nous avons atteint la fin du fichier.
            }
            return nil, err
        }
        memtable.Put(entry.Key, entry.Value)
    }
    
    return memtable, nil
}
```

Quelques notes sur le code ci-dessus :

* **NewWAL** : Cette fonction crée une instance du WAL pour notre base de données. Elle prend le chemin du fichier où les données du WAL doivent être stockées et ouvre le fichier en utilisant la fonction `os.OpenFile` de Go. De plus, un `gob.Encoder` est initialisé pour simplifier l'encodage des structures de données Go en format binaire pour un stockage efficace dans le fichier WAL.
    
* **Write** : La fonction Write ajoute une nouvelle paire clé-valeur au fichier WAL. Chaque opération d'écriture dans la MemTable appelle d'abord cette fonction pour s'assurer que la mise à jour est enregistrée de manière durable.
    
* **ReplayWAL** : C'est la fonction la plus importante. En cas de crash, cette fonction vient à notre secours en reconstruisant la MemTable à partir du fichier WAL. Elle rejoue les entrées stockées dans le fichier WAL et les écrit dans la MemTable. Voici comment elle fonctionne :
    
    1. La fonction commence par créer une nouvelle instance de MemTable vide qui sera peuplée avec les paires clé-valeur.
        
    2. Elle tente ensuite d'ouvrir le fichier WAL. Si le fichier n'existe pas (par exemple, s'il s'agit du premier démarrage), la fonction suppose qu'il n'y a rien à récupérer et retourne simplement la MemTable vide.
        
    3. Un `gob.Decoder` est utilisé pour lire le fichier WAL, ce qui aide à désérialiser les données `WALEntry` encodées en binaire pour les transformer à nouveau en paires clé-valeur.
        
    4. Pour chaque `WALEntry` décodée avec succès, la paire clé-valeur est rajoutée dans la MemTable en utilisant la fonction `Put`.
        

Grâce à cela, la base de données peut récupérer entièrement son état en rejouant toutes les opérations enregistrées dans le WAL.

En ce qui concerne l'intégration, chaque fois que vous créez une nouvelle DB, vous devriez penser à rejouer à partir d'un WAL existant et à ouvrir le WAL en mode ajout. De plus, Put devrait d'abord écrire dans le WAL.

```go
func NewDB[K comparable, V any](maxMemtableSize int) (*DB[K, V], error) {
    walPath := "db.wal"
    memtable, err := ReplayWAL[K, V](walPath) // c'est le replay
    if err != nil {
        return nil, err
    }
    // ouvrir le WAL en mode ajout
    wal, err := NewWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    return &DB[K, V]{
        memtable:        memtable,
        maxMemtableSize: maxMemtableSize,
        memtableSize:    len(memtable.data),
        wal:             wal,
        walPath:         walPath,
        sstables:        make([]*SSTable[K, V], 0),
    }, nil
}

func (db *DB[K, V]) Put(key K, value V) error {
// d'abord écrire dans le WAL
    if err := db.wal.Write(key, value); err != nil {
        return err
    }
    
    db.memtable.Put(key, value)
    db.memtableSize++
    
    if db.memtableSize >= db.maxMemtableSize {
        if err := db.flushMemtable(); err != nil {
            return err
        }
    }
    
    return nil
}
```

### Fichier Manifest : Suivi de l'état de la base de données

À ce stade, la base de données est assez robuste et durable, mais une question importante subsiste : lors des redémarrages, comment notre base de données connaît-elle les SSTables ? Connaître toutes les SSTables est crucial pour récupérer les données.

Supposons que notre base de données crash après avoir écrit plusieurs SSTables. Sans connaître ces SSTables, la base de données créera une nouvelle slice de SSTables et toutes nos anciennes données seront perdues – les requêtes ne liront pas ces fichiers.

Pour résoudre ce problème, nous introduisons un inventaire des SSTables appelé MANIFEST. Chaque fois que nous créons avec succès une nouvelle SSTable dans `flushMemtable`, nous ajoutons son chemin au MANIFEST et sauvegardons le MANIFEST sur le disque.

La toute première chose que fait `NewDB` au démarrage est de lire le MANIFEST. Cela lui donne la liste de tous les chemins de fichiers, et elle utilise cette liste pour reconstruire parfaitement sa slice de SSTables.

En résumé, le MANIFEST détermine l'état de la DB.

Le Manifest contient une slice de `SSTablePaths`. La fonction Read lira le fichier MANIFEST pour restaurer la connaissance des SSTables. La fonction Write écrira un nouveau fichier manifest.

```go
type Manifest struct {
    SSTablePaths []string
}

func ReadManifest(path string) (*Manifest, error) {
    file, err := os.Open(path)
    if err != nil {
        if os.IsNotExist(err) {
            // Si le manifest n'existe pas, retourner un manifest vide
            return &Manifest{SSTablePaths: []string{}}, nil
        }
        return nil, err
    }
    defer file.Close()
    
    var manifest Manifest
    decoder := gob.NewDecoder(file)
    err = decoder.Decode(&manifest)
    if err != nil {
        return nil, err
    }
    
    return &manifest, nil
}

func WriteManifest(path string, manifest *Manifest) error {
    tmpPath := path + ".tmp"
    file, err := os.Create(tmpPath)
    if err != nil {
        return err
    }
    
    encoder := gob.NewEncoder(file)
    if err := encoder.Encode(manifest); err != nil {
        file.Close()
        os.Remove(tmpPath)
        return err
    }
    
    if err := file.Close(); err != nil {
        return err
    }
    // Renommage atomique
    return os.Rename(tmpPath, path)
}
```

Vous remarquerez que nous ne modifions pas directement le fichier MANIFEST existant. Au lieu de cela, nous créons un fichier temporaire, y écrivons toutes les données, le fermons, puis le « renommons atomiquement » pour remplacer l'ancien MANIFEST.

L'opération `os.Rename()` est atomique sur la plupart des systèmes de fichiers, ce qui signifie qu'elle réussit complètement ou échoue complètement – il n'y a pas d'état intermédiaire. C'est crucial car si le système crash pendant la mise à jour du MANIFEST, nous devons nous assurer de ne pas nous retrouver avec un fichier corrompu. Nous en reparlerons ci-dessous lors de la discussion sur la compaction.

Avec cette approche, nous avons soit l'ancien MANIFEST valide, soit le nouveau MANIFEST valide, jamais un fichier corrompu partiellement écrit.

Du point de vue de l'intégration, `NewDB` lira le manifest et définira sa slice de SSTables en fonction de celui-ci. La méthode flush, étant donné qu'elle écrit dans une SSTable, écrira également les informations de la SSTable dans le manifest pour tenir la DB à jour sur les nouvelles SSTables.

```go
type DB[K comparable, V any] struct {
    memtable        *MemTable[K, V]
    maxMemtableSize int
    memtableSize    int
    sstables        []*SSTable[K, V]
    sstableCounter  int
    wal             *WAL[K, V]
    walPath         string
    manifest        *Manifest
    manifestPath    string
}

func NewDB[K comparable, V any](maxMemtableSize int) (*DB[K, V], error) {
    walPath := "db.wal"
    memtable, err := ReplayWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    wal, err := NewWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    manifestPath := "MANIFEST"
    manifest, err := ReadManifest(manifestPath)
    if err != nil {
        return nil, err
    }
    
    sstables := make([]*SSTable[K, V], len(manifest.SSTablePaths))
    for i, path := range manifest.SSTablePaths {
        sstables[i] = &SSTable[K, V]{path: path}
    }
    
    return &DB[K, V]{
        memtable:        memtable,
        maxMemtableSize: maxMemtableSize,
        memtableSize:    len(memtable.data),
        wal:             wal,
        walPath:         walPath,
        manifest:        manifest,
        manifestPath:    manifestPath,
        sstables:        sstables,
    }, nil
}

func (db *DB[K, V]) flushMemtable() error {
    sstablePath := fmt.Sprintf("data-%d.sstable", db.sstableCounter)
    sstable, err := writeSSTable(db.memtable, sstablePath)
    if err != nil {
        return err
    }
    
    db.sstables = append(db.sstables, sstable)
    db.sstableCounter++
    
    db.manifest.SSTablePaths = append(db.manifest.SSTablePaths, sstablePath)
    if err := WriteManifest(db.manifestPath, db.manifest); err != nil {
        return err
    }
    
    db.memtable = NewMemTable[K, V]()
    db.memtableSize = 0
    
    return nil
}
```

À ce stade, notre DB possède presque tout. Elle peut écrire en mémoire (MemTable), persister sur disque (SSTable) et récupérer après des crashs (WAL et manifest). Vous devriez inclure les fonctionnalités de mise à jour et de suppression pour être complet – voyons cela ensuite.

### Mise à jour et suppression : Gérer la mutabilité dans un système immuable

À présent, vous devriez savoir que dans un système de stockage LSM, les données ne sont jamais mises à jour – au contraire, de nouvelles données sont écrites. Par exemple, si vous avez une paire de données ("a": "apple") et qu'au fil du temps celle-ci doit devenir ("a": "apricot"), une nouvelle paire sera écrite dans une SSTable différente sans aucune modification de la paire existante. Et oui, cela entraîne des doublons.

De plus, fait intéressant, les données ne sont même pas supprimées lors des opérations d'écriture. La raison en est que, dans un sens traditionnel, si vous devez supprimer ("a":"apple"), vous devrez trouver où elle se trouve sur le disque et la retirer. Cela ralentit les écritures. Au lieu de cela, un mécanisme ingénieux est utilisé : au lieu de supprimer directement la donnée, vous pouvez marquer la clé comme supprimée en écrivant une valeur spéciale appelée `TOMBSTONE`.

Ainsi, dans le cas de la suppression de (a : apple), vous ne retireriez pas la clé d'une SSTable. Au lieu de cela, vous écririez une nouvelle paire clé-valeur telle que ("a": "TOMBSTONE"). Voici ce que cela permet d'accomplir :

* Le `"TOMBSTONE"` sert de marqueur au sein de la SSTable, indiquant au système que la clé `"a"` a été logiquement supprimée, même si elle existe toujours physiquement dans les SSTables plus anciennes.
    
* Lors des futures lectures, toute valeur associée à `"TOMBSTONE"` sera traitée comme supprimée, garantissant que l'entrée n'apparaisse plus dans les résultats de requête.
    
* Ce mécanisme évite le besoin de suppressions immédiates ou de mises à jour coûteuses sur place, rendant les opérations d'écriture plus rapides et plus simples.
    

Mais cela soulève également les questions suivantes :

1. Comment lire avec précision lorsqu'il y a des doublons ? C'est-à-dire, comment les utilisateurs obtiennent-ils ("a": "apricot") au lieu de ("a": "apple") parce que la première est la plus récente et la plus exacte ?
    
2. Comment gérer les suppressions pour s'assurer que les clés supprimées ne sont pas retournées (et qu'à la place, un message d'erreur approprié est renvoyé) ?
    
3. Ces données obsolètes et supprimées sont des déchets. Comment s'en débarrasser pour économiser de l'espace de stockage ?
    

Tant que les données sont dans la MemTable (map en mémoire), les doublons sont faciles à gérer : les nouvelles valeurs remplaceront simplement les anciennes.

Mais cela devient délicat lorsque les données se trouvent dans plusieurs SSTables. Il existe une solution très simple à ce problème : il suffit de lire la SSTable la plus récente avant les plus anciennes. De cette façon, vous lireez toujours la dernière valeur pour une clé donnée et sortirez prématurément.

Le code suivant dans le chemin de lecture garantit la lecture des SSTables les plus récentes avant de passer aux plus anciennes (notez que la boucle commence à `len(db.sstables) - 1`) :

```go
func (db *DB[K, V]) Get(key K) (V, error) {
    // Vérifier d'abord la memtable
    if val, ok := db.memtable.Get(key); ok {
        if any(val).(string) == TOMBSTONE {
            var zero V
            return zero, ErrNotFound
        }
        return val, nil
    }
    
    // Ensuite, vérifier les sstables de la plus récente à la plus ancienne
    for i := len(db.sstables) - 1; i >= 0; i-- {
        sstable := db.sstables[i]
        val, err := sstable.Get(key)
        if err != nil {
            if err == ErrNotFound {
                continue
            }
            var zero V
            return zero, err
        }
        return val, nil
    }
    
    var zero V
    return zero, ErrNotFound
}
```

Et pour la suppression, vous pourriez simplement ajouter une nouvelle valeur "TOMBSTONE" :

```go
func (db *DB[K, V]) Delete(key K) error {
    return db.Put(key, any(TOMBSTONE).(V))
}
```

Note : Cette implémentation suppose que V est de type string. Dans un système de production, vous auriez besoin d'un moyen plus robuste pour gérer les tombstones qui fonctionne avec n'importe quel type de valeur.

La gestion des clés supprimées devient simple maintenant. Vous pouvez vérifier la valeur (dans la MemTable et la SSTable) et retourner une erreur si la valeur est "TOMBSTONE" :

```go
// db.go
func (db *DB[K, V]) Get(key K) (V, error) {
    if val, ok := db.memtable.Get(key); ok {
        if any(val).(string) == TOMBSTONE { // TOMBSTONE trouvé, retourner zero
            var zero V
            return zero, ErrNotFound
        }
        return val, nil
    }
    // ... reste de la fonction
}
```

```go
// sstable.go
func (s *SSTable[K, V]) Get(key K) (V, error) {
    // ... code précédent
    
    keyInDB := any(pair.Key).(string)
    if keyInDB == any(key).(string) {
        if any(pair.Value).(string) == TOMBSTONE {
            var zero V
            return zero, ErrNotFound
        }
        return pair.Value, nil
    }
    
    // ... reste de la fonction
}
```

### Compaction : Nettoyage des données obsolètes et supprimées

Nous avons géré tous les scénarios jusqu'à présent, sauf un. Ce n'est pas une préoccupation pour servir le trafic de lecture/écriture, mais c'est quelque chose d'important pour la santé du système de stockage.

Au fil du temps, le système a accumulé beaucoup de déchets (données obsolètes, supprimées) et a besoin d'un mécanisme de ramasse-miettes (garbage collection). La compaction est un processus de maintenance en arrière-plan qui nettoie et réorganise les données dans un système de stockage LSM.

À mesure que le système grandit, plusieurs SSTables ont été créées. Cela conduit les lectures à nécessiter plusieurs opérations sur les fichiers pour obtenir des valeurs. En compactant (ou fusionnant) plusieurs SSTables en une seule, vous évitez la surcharge des opérations disque. En cours de route, vous devriez également supprimer définitivement les données qui ont été marquées par un TOMBSTONE.

Note : La compaction est le seul moment où les données sont définitivement supprimées d'un système de stockage LSM.

Pour saisir le concept de compaction, nous allons implémenter ce qu'on appelle une `Full Compaction` où vous fusionnerez toutes les SSTables existantes en une seule SSTable plus grande. Dans les implémentations de bases de données réelles, la stratégie est plus complexe, impliquant une compaction à plusieurs niveaux (multi-level compaction).

#### Algorithme de compaction

Nous allons implémenter une `K-way merge` (fusion à K voies) pour effectuer la compaction. C'est un algorithme général qui prend K listes triées et les fusionne en une seule liste triée combinée. Dans ce cas, les K listes triées sont les SSTables, et vous allez toutes les fusionner en une seule SSTable.

Nos SSTables sont déjà triées, donc l'idée de les fusionner implique :

1. Prendre les plus petites (premières) clés de chaque SSTable.
    
2. Trouver la plus petite parmi ces clés.
    
3. Stocker la plus petite clé trouvée dans le nouveau fichier SSTable.
    
4. Récupérer la clé suivante de la SSTable à laquelle appartenait la plus petite clé.
    
5. Répéter ce processus pour toutes les SSTables.
    

Voici un exemple simple avec des nombres :

```bash
Supposons que nous ayons 3 listes triées :
Liste A : [4, 8, 12]
Liste B : [3, 9]
Liste C : [7, 10, 11]

Lors de la première itération, nous prendrons (4, 3, 7) car ce sont les plus petites clés de chaque liste. 
Nous trouvons la plus petite parmi elles, qui est 3, et stockons 3 dans la liste de résultats.

Lors de la deuxième itération, nous prendrons (4, 9, 7). Notez que 3 a déjà été pris en compte. 
Nous choisissons 4 et le stockons dans la liste de résultats.

En répétant cela jusqu'à ce que toutes les listes soient vides, nous obtenons :
Liste de résultats : [3, 4, 7, 8, 9, 10, 11, 12]
```

La partie centrale de cet algorithme consiste à trouver la plus petite clé parmi les plus petites clés des SSTables individuelles. Heureusement, nous avons une structure de données appelée `Min-Heap` (tas binaire minimal) qui fait cela pour nous. Ainsi, vous allez prendre la plus petite clé de chaque SSTable et les mettre toutes sur un Min-Heap pour qu'il retourne la plus petite d'entre elles. Nous allons exploiter le package `container/heap` de Go pour obtenir la structure de données Min-Heap et l'algorithme correspondant pour trouver la valeur minimale et la placer au sommet du tas.

Le Min-Heap nécessite que vous fournissiez une fonction pour déterminer quelle est la plus petite clé entre deux clés, car il utilise cette logique pour déterminer le minimum global. La fonction suivante est implémentée à cet effet :

```go
func (h MinHeap[K, V]) Less(i, j int) bool {
    // encore une fois, pour une comparaison simple, supposons une clé string
    keyI := any(h[i].Pair.Key).(string)
    keyJ := any(h[j].Pair.Key).(string)
    if keyI != keyJ {
        return keyI < keyJ
    }
    // ceci est nécessaire pour le cas où vous avez des clés dupliquées,
    // vous voudrez choisir celle qui se trouve dans la sstable la plus récente car c'est la dernière
    return h[i].SSTableIndex > h[j].SSTableIndex
}
```

Un aspect important de la fonction `Less` présentée ci-dessus est la façon dont elle gère les égalités. Si nous avons deux paires avec la même clé, laquelle est la plus petite ? Supposons deux paires comme `(a: apple)` et `(a: apricot)`, où (a: apple) est l'ancienne valeur (écrite dans une SSTable plus ancienne), quelle paire la fonction Less doit-elle retourner comme étant la plus petite ?

La réponse est celle qui se trouve dans la SSTable la plus récente (voir `h[i].SSTableIndex > h[j].SSTableIndex`). Cela garantit que la SSTable avec l'index le plus élevé (c'est-à-dire la plus récente) devient la valeur « moindre », de sorte que (a: apricot) l'emporte. Il est important de toujours obtenir la valeur la plus récente d'une clé donnée.

Le code pour la compaction ressemble à ce qui suit. Notez que nous écartons les valeurs supprimées (TOMBSTONE) et les anciennes valeurs.

```go
// placez ceci dans un nouveau fichier compaction.go
func MergeSSTables[K comparable, V any](sstables []*SSTable[K, V], newPath string) (*SSTable[K, V], error) {
    newFile, err := os.Create(newPath) // créer un nouveau fichier sstable
    if err != nil {
        return nil, err
    }
    defer newFile.Close() // éviter les fuites de mémoire en s'assurant que le fichier est fermé
    
    newEncoder := gob.NewEncoder(newFile) // initialiser l'encodeur pour le nouveau fichier SSTable
    
    
    files := make([]*os.File, len(sstables)) // ouvrir toutes les sstables
    decoders := make([]*gob.Decoder, len(sstables)) // initialiser un décodeur par fichier sstable
    for i, sstable := range sstables {
        files[i], err = os.Open(sstable.path)
        if err != nil {
            return nil, err
        }
        defer files[i].Close() // éviter les fuites de mémoire en s'assurant que le fichier est fermé
        decoders[i] = gob.NewDecoder(files[i])
    }
    
    // lire la première paire de chaque sstable et la stocker dans un tableau de paires
    pairs := make([]Pair[K, V], len(decoders))
    emptySSTables := make([]bool, len(decoders)) // suivre les sstables vides
    for i, decoder := range decoders {
        if err := decoder.Decode(&pairs[i]); err != nil {
            if err == io.EOF {
                emptySSTables[i] = true
                continue
            }
            return nil, err
        }
    }
    
    // pousser ces paires sur le tas
    h := &MinHeap[K, V]{}
    for i, pair := range pairs {
        if !emptySSTables[i] {
            heap.Push(h, &HeapItem[K, V]{Pair: pair, SSTableIndex: i})
        }
    }
    
    // initialiser l'algorithme de calcul du min-heap du package container/heap
    heap.Init(h)
    
    var lastKey K
    firstKey := true
    
    // extraire l'élément min du tas et le stocker dans la nouvelle sstable
    for h.Len() > 0 {
        item := heap.Pop(h).(*HeapItem[K, V])
        
        // Si cette clé est un doublon de la dernière vue, l'ignorer
        if !firstKey && item.Pair.Key == lastKey {
            // Nous ne nous soucions que de la version de la SSTable la plus récente,
            // que nous avons déjà traitée
        } else {
            if any(item.Pair.Value).(string) != TOMBSTONE {
                // écarter les éléments supprimés
                if err := newEncoder.Encode(item.Pair); err != nil {
                    return nil, err
                }
            }
        }
        
        lastKey = item.Pair.Key
        firstKey = false
        
        // Pousser l'élément suivant de la même SSTable dans le tas
        var nextPair Pair[K, V]
        if err := decoders[item.SSTableIndex].Decode(&nextPair); err == nil {
            heap.Push(h, &HeapItem[K, V]{Pair: nextPair, SSTableIndex: item.SSTableIndex})
        } else if err != io.EOF {
            return nil, err
        }
    }
    
    return &SSTable[K, V]{path: newPath}, nil
}
```

Toute la magie de la compaction a été regroupée dans une seule fonction, `MergeSSTables`. La fonction suit les étapes logiques suivantes (vous pouvez consulter les commentaires en ligne dans le code pour suivre) :

1. Nous créons un nouveau fichier SSTable de destination et initialisons le `gob.Encoder` correspondant.
    
2. Nous ouvrons tous les fichiers SSTable existants et stockons leurs références dans le tableau `files`. De plus, nous initialisons un `gob.Decoder` par fichier SSTable existant. Pour éviter les fuites de mémoire, une instruction `defer` garantit que chaque fichier sera fermé une fois que la fonction aura terminé son travail.
    
3. Chaque `decoder` lit la première paire clé-valeur de sa SSTable correspondante et la stocke dans le tableau `pairs`.
    
4. Les SSTables qui sont déjà épuisées (par exemple, vides ou ayant atteint la fin du fichier) sont marquées comme telles dans la slice `emptySSTables`, et nous évitons de les pousser sur le tas.
    
5. Nous poussons chaque paire du tableau pairs vers le `Min-Heap`, puis initialisons l'algorithme de calcul du `Min-Heap`. Cet algorithme est présent dans le package `container/heap` de Go.
    
6. Chaque fois que la plus petite paire clé-valeur est extraite du min-heap, elle est comparée à la clé précédemment traitée (`lastKey`). Les clés dupliquées (celles dont les valeurs sont déjà écrites) sont ignorées.
    
7. Les valeurs marquées d'un `"TOMBSTONE"` (entrées logiquement supprimées) sont ignorées et ne sont pas écrites dans la nouvelle SSTable, nettoyant ainsi efficacement les données supprimées.
    
8. Pour continuer la fusion, la paire clé-valeur suivante de la même SSTable (celle que nous venons de traiter) est lue et poussée sur le tas, à moins que la fin de la SSTable (`io.EOF`) n'ait été atteinte.
    

Pour intégrer cela à la DB, vous pourriez utiliser un seuil de compaction et déclencher la compaction lors du flush lorsque ce seuil est atteint :

```go
type DB[K comparable, V any] struct {
    memtable            *MemTable[K, V]
    maxMemtableSize     int
    memtableSize        int
    sstables            []*SSTable[K, V]
    sstableCounter      int
    wal                 *WAL[K, V]
    walPath             string
    manifest            *Manifest
    manifestPath        string
    compactionThreshold int
}

func NewDB[K comparable, V any](maxMemtableSize int, compactionThreshold int) (*DB[K, V], error) {
    walPath := "db.wal"
    memtable, err := ReplayWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    wal, err := NewWAL[K, V](walPath)
    if err != nil {
        return nil, err
    }
    
    manifestPath := "MANIFEST"
    manifest, err := ReadManifest(manifestPath)
    if err != nil {
        return nil, err
    }
    
    sstables := make([]*SSTable[K, V], len(manifest.SSTablePaths))
    for i, path := range manifest.SSTablePaths {
        sstables[i] = &SSTable[K, V]{path: path}
    }
    
    return &DB[K, V]{
        wal:                 wal,
        walPath:             walPath,
        memtable:            memtable,
        memtableSize:        len(memtable.data),
        maxMemtableSize:     maxMemtableSize,
        manifestPath:        manifestPath,
        manifest:            manifest,
        sstables:            sstables,
        compactionThreshold: compactionThreshold,
    }, nil
}

// une nouvelle fonction compact
func (db *DB[K, V]) Compact() error {
    compactedSSTablePath := fmt.Sprintf("data-compacted-%d.sstable", db.sstableCounter)
    compactedSSTable, err := MergeSSTables(db.sstables, compactedSSTablePath)
    if err != nil {
        return err
    }
    // écrire la nouvelle SSTable dans le fichier MANIFEST
    db.manifest.SSTablePaths = []string{compactedSSTablePath}
    if err := WriteManifest(db.manifestPath, db.manifest); err != nil {
        return err
    }
    // note : supprimer seulement après avoir écrit le manifest
    for _, sstable := range db.sstables {
        if err := os.Remove(sstable.path); err != nil {
            log.Printf("Failed to remove old sstable %s: %v", sstable.path, err)
        }
    }
    
    db.sstables = []*SSTable[K, V]{compactedSSTable}
    db.sstableCounter++
    
    return nil
}

func (db *DB[K, V]) flushMemtable() error {
    sstablePath := fmt.Sprintf("data-%d.sstable", db.sstableCounter)
    sstable, err := writeSSTable(db.memtable, sstablePath)
    if err != nil {
        return err
    }
    
    db.sstables = append(db.sstables, sstable)
    db.sstableCounter++
    
    db.manifest.SSTablePaths = append(db.manifest.SSTablePaths, sstablePath)
    if err := WriteManifest(db.manifestPath, db.manifest); err != nil {
        return err
    }
    
    db.memtable = NewMemTable[K, V]()
    db.memtableSize = 0
    
    // déclencher la compaction
    if len(db.sstables) >= db.compactionThreshold {
        if err := db.Compact(); err != nil {
            log.Printf("Compaction failed: %v", err)
            return err
        }
    }
    
    return nil
}
```

Remarquez la fonction `Compact()` dans le code de la DB intégrée ? C'est là que nous invoquons la fonction `MergeSSTables` précédemment définie pour déclencher le processus de compaction. Après avoir invoqué `MergeSSTables`, nous écrivons une nouvelle SSTable dans le fichier MANIFEST, puis nous supprimons les anciennes SSTables.

Précédemment, dans la section [Fichier Manifest : Suivi de l'état de la base de données](#heading-fichier-manifest-suivi-de-l-etat-de-la-base-de-donnees), j'ai parlé du renommage atomique `os.Rename(tmpPath, path)`. Voyons pourquoi le renommage atomique du MANIFEST est crucial pour la compaction.

Pendant la compaction, nous effectuons un changement majeur dans l'état de la base de données : le remplacement de plusieurs SSTables par une seule SSTable compactée. La mise à jour du MANIFEST est critique ici car c'est la source de vérité indiquant quelles SSTables existent.

Réfléchissons à ce qui pourrait mal se passer sans renommage atomique :

1. Vous commencez à écrire le nouveau MANIFEST (qui pointe vers la SSTable compactée).
    
2. Le système crash en milieu d'écriture.
    
3. Le MANIFEST est corrompu et illisible.
    
4. Au redémarrage, la base de données n'a aucune idée des SSTables qui existent.
    
5. Toutes les données sont effectivement perdues.
    

Avec le renommage atomique :

1. Nous écrivons le nouveau MANIFEST dans MANIFEST.tmp.
    
2. Nous le fermons complètement et le synchronisons sur le disque.
    
3. Nous renommons atomiquement MANIFEST.tmp en MANIFEST en utilisant `os.Rename(tmpPath, path)`.
    
4. Si un crash survient avant l'étape 3 : l'ancien MANIFEST est intact, nous réessayons la compaction.
    
5. Si un crash survient pendant l'étape 3 : l'opération atomique est soit terminée, soit elle ne l'est pas – pas de corruption.
    
6. Si un crash survient après l'étape 3 : le nouveau MANIFEST est en place, tout va bien.
    

C'est aussi pourquoi nous ne supprimons les anciennes SSTables qu'après avoir mis à jour le MANIFEST avec succès. Si nous les supprimions avant de mettre à jour le MANIFEST et que nous crashions ensuite, le MANIFEST pointerait toujours vers des fichiers qui n'existent plus.

#### Vue d'ensemble :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1765740593067/c18083ad-bf8a-4cae-92d3-d690a61dac52.png align="center")

## Conclusion

Félicitations ! Vous avez construit un moteur de stockage LSM-tree fonctionnel à partir de zéro. En suivant l'approche axée sur les problèmes – en découvrant les problèmes et en implémentant des solutions au fur et à mesure qu'ils se présentaient – vous avez expérimenté la façon dont les ingénieurs conçoivent des systèmes de stockage robustes. J'espère que cela est plus efficace que de simplement mémoriser des concepts.

**Points clés à retenir**

* **Les écritures en mode ajout uniquement (append-only)** rendent les LSM-trees rapides pour les charges de travail intensives en écriture.
    
* **L'immuabilité** élimine les problèmes complexes de concurrence.
    
* **Le compromis** est que l'LSM-tree favorise les écritures par rapport aux lectures (à l'inverse des B-trees).
    
* **La durabilité** nécessite plusieurs mécanismes travaillant ensemble (WAL, MANIFEST, opérations atomiques).
    
* **La maintenance en arrière-plan** (compaction) est essentielle pour la santé et le coût à long terme.
    

Note importante : Il s'agit d'une implémentation pédagogique. Cela signifie que j'ai intentionnellement simplifié le code, il n'est donc **pas prêt pour la production**. Les limitations majeures incluent :

* Pas de contrôle de concurrence (absence de mutex/verrous).
    
* Pas de filtres de Bloom pour des recherches efficaces.
    
* Stratégie de compaction simplifiée.
    
* Problèmes de sécurité des types avec les tombstones génériques.
    
* Absence de récupération d'erreurs robuste.
    

### Code complet :

Comme je l'ai mentionné précédemment, j'ai omis le code répétitif (boilerplate) et les fonctions utilitaires par souci de brièveté. L'implémentation complète et exécutable est disponible [sur ce dépôt GitHub](https://github.com/justramesh2000/lsm-db).

Pour en savoir plus sur les implémentations LSM de production, étudiez RocksDB, LevelDB, ou lisez l'article original sur l'LSM-tree par O'Neil et al. : [https://www.cs.umb.edu/~poneil/lsmtree.pdf](https://www.cs.umb.edu/~poneil/lsmtree.pdf)