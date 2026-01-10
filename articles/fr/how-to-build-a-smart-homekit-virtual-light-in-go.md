---
title: Comment créer une lampe virtuelle HomeKit intelligente en Go
author: Rez Moss
date: '2025-12-19T00:41:41.417Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-smart-homekit-virtual-light-in-go
description: 'Récemment, j''ai voulu comprendre comment les appareils de maison intelligente
  fonctionnent réellement. Quand vous scannez un code QR et qu''une lampe apparaît
  dans votre application Maison, que se passe-t-il vraiment ? Quand vous appuyez sur
  "on", quels octets circulent sur votre réseau ?


  La meilleure façon que je connaisse pour comprendre...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766104866742/8d8c0158-95d0-493b-a311-cd99189654e1.png
tags:
- name: HAP
  slug: hap
- name: Go Language
  slug: go
- name: homekit
  slug: homekit
- name: Apple
  slug: apple
- name: Matter
  slug: matter
- name: protocols
  slug: protocols
seo_desc: 'Recently, I wanted to understand how smart home devices actually work.
  When you scan a QR code and a light appears in your Home app, what''s really happening?
  When you tap "on", what bytes travel across your network?


  The best way I know to understand...'
---


Récemment, j'ai voulu comprendre comment les appareils de maison intelligente fonctionnent réellement. Quand vous scannez un code QR et qu'une lampe apparaît dans votre application Maison, que se passe-t-il vraiment ? Quand vous appuyez sur "on", quels octets circulent sur votre réseau ?

![Virtual HomeKit Light QR code](https://cdn.hashnode.com/res/hashnode/image/upload/v1765414117210/e65d5768-792d-4aae-8669-db0ac7a9c60d.png align="center")

La meilleure façon que je connaisse pour comprendre quelque chose est de le construire, j'ai donc créé une lampe virtuelle HomeKit en Go. Dans ce tutoriel, je vais vous expliquer ma démarche. Nous allons lever le voile sur les protocoles de maison intelligente pour que vous compreniez leur fonctionnement en profondeur. C'est parti.

### Ce que nous allons aborder :

1. [Ce qu'est réellement HomeKit](#heading-ce-qu-est-reellement-homekit)
    
2. [Le paysage des protocoles de maison intelligente](#heading-le-paysage-des-protocoles-de-maison-intelligente)
    
3. [Comment fonctionne la découverte HomeKit](#heading-comment-fonctionne-la-decouverte-homekit)
    
4. [Le processus de jumelage : que se passe-t-il quand vous scannez le code QR](#heading-le-processus-de-jumelage-que-se-passe-t-il-quand-vous-scannez-le-code-qr)
    
5. [L'URI de configuration : que contient ce code QR ?](#heading-l-uri-de-configuration-que-contient-ce-code-qr)
    
6. [Ce qu'il se passe quand vous allumez ou éteignez la lampe](#heading-ce-qu-il-se-passe-quand-vous-allumez-ou-eteignez-la-lampe)
    
7. [Le modèle de base de données des accessoires](#heading-le-modele-de-base-de-donnees-des-accessoires)
    
8. [Persistance des données de jumelage](#heading-persistance-des-donnees-de-jumelage)
    
9. [Notifications d'événements](#heading-notifications-d-evenements)
    
10. [L'implémentation complète](#heading-l-implementation-complete)
    
11. [Ce que j'ai appris](#heading-ce-que-j-ai-appris)
    

## Ce dont vous aurez besoin

Avant de commencer la construction, assurons-nous que vous avez la bonne configuration. Ce projet nécessite deux choses :

1. **Go 1.21 ou ultérieur** : Nous utilisons certaines fonctionnalités modernes de Go, et la bibliothèque `brutella/hap` fonctionne mieux avec les versions récentes. Vous pouvez vérifier votre version avec `go version`. Si vous devez mettre à jour, récupérez la dernière version sur go.dev.
    
2. **Un environnement Apple HomeKit** : Cela signifie un iPhone ou un iPad sous iOS 15+ avec l'application Maison. Vous devrez également être sur le même réseau WiFi que la machine exécutant votre lampe virtuelle. HomeKit est entièrement local, votre téléphone doit donc pouvoir joindre votre machine de développement directement.
    

Une chose qui m'a posé problème au début : si vous exécutez cela sur un serveur Linux ou dans un conteneur, assurez-vous que le trafic mDNS n'est pas bloqué. Votre pare-feu doit autoriser le port UDP 5353 (pour la découverte mDNS) et le port sur lequel votre accessoire s'exécute (nous utiliserons le 51826). Sur un Mac, cela fonctionne généralement sans configuration supplémentaire.

## Ce qu'est réellement HomeKit

HomeKit est le framework de maison intelligente d'Apple. Il est composé de trois éléments :

1. **un protocole (HAP)** qui définit comment les appareils communiquent entre eux,
    
2. **un modèle de sécurité** qui chiffre et authentifie tout,
    
3. **et un écosystème** (l'application Maison, Siri, les automatisations).
    

Ici, nous nous concentrerons sur la couche protocole. Nous construisons quelque chose qui parle suffisamment bien le HAP pour que l'écosystème d'Apple l'accepte comme un véritable accessoire.

## Le paysage des protocoles de maison intelligente

Avant de commencer, comprenons à quoi nous avons affaire. Deux protocoles sont en jeu ici :

1. **HomeKit Accessory Protocol (HAP) :** Le protocole original de maison intelligente d'Apple datant de 2014. Il fonctionne sur votre réseau WiFi local, utilise mDNS pour la découverte et chiffre tout avec Curve25519 et ChaCha20-Poly1305. Chaque appareil HomeKit que vous avez utilisé parle le HAP.
    
2. **Matter** : Le nouveau standard de l'industrie (2022) soutenu par Apple, Google, Amazon et d'autres. Matter est en fait construit sur bon nombre des mêmes primitives cryptographiques que le HAP. Quand Apple a ajouté le support de Matter, ils ont essentiellement rendu HomeKit bilingue, car il peut parler les deux protocoles.
    

Voici ce qui est intéressant : les appareils Matter qui se connectent à Apple Home finissent toujours par être contrôlés via l'infrastructure de HomeKit. Matter est la couche de jumelage et de découverte, mais une fois qu'un appareil est dans votre Maison, l'écosystème d'Apple prend le relais.

Pour ce projet, j'utilise directement le protocole HAP via la bibliothèque `brutella/hap`. Cela nous permet de voir exactement ce qui se passe sans la couche d'abstraction supplémentaire de Matter.

## Comment fonctionne la découverte HomeKit

Quand vous lancez un accessoire HomeKit sur votre réseau, il ne se contente pas d'attendre. Il s'annonce activement en utilisant le **mDNS** (multicast DNS), également appelé Bonjour sur les plateformes Apple.

L'accessoire diffuse un enregistrement de service qui ressemble à ceci :

```plaintext
_hap._tcp.local.
  name: Virtual Light._hap._tcp.local.
  port: 51826
  txt: 
    c#=1          // numéro de config (les changements déclenchent une redécouverte)
    ff=0          // feature flags
    id=XX:XX:XX   // ID de l'appareil (comme une adresse MAC)
    md=Virtual Light  // nom du modèle
    pv=1.1        // version du protocole
    s#=1          // numéro d'état
    sf=1          // status flag (1=non jumelé, 0=jumelé)
    ci=5          // catégorie (5=ampoule)
    sh=XXXXXX     // hash de configuration
```

Votre iPhone écoute constamment les diffusions `_hap._tcp.local.`. S'il en voit une avec `sf=1` (non jumelé), elle apparaît dans "Ajouter un accessoire" comme étant disponible.

Voyons cela en code. Voici la configuration minimale du serveur :

```go
package main

import (
    "context"
    "fmt"
    "log"
    
    "github.com/brutella/hap"
    "github.com/brutella/hap/accessory"
)

func main() {
    light := accessory.NewLightbulb(accessory.Info{
        Name:         "Virtual Light",
        Manufacturer: "My Smart Home",
    })

    server, err := hap.NewServer(hap.NewFsStore("./data"), light.A)
    if err != nil {
        log.Fatal(err)
    }

    server.Pin = "00102003"
    server.Addr = ":51826"

    server.ListenAndServe(context.Background())
}
```

Quand `ListenAndServe` s'exécute, il :

1. Génère un ID d'appareil unique s'il n'en existe pas déjà.
    
2. Commence à écouter sur le port 51826.
    
3. Enregistre l'enregistrement de service mDNS.
    
4. Attend les connexions.
    

À ce stade, votre iPhone peut le découvrir. Mais que se passe-t-il quand vous essayez de le jumeler ?

## Le processus de jumelage : que se passe-t-il quand vous scannez le code QR

C'est là que ça devient intéressant. HomeKit utilise le protocole **SRP (Secure Remote Password)** pour le jumelage. C'est le même protocole utilisé dans des systèmes comme l'authentification de 1Password.

Quand vous scannez le code QR ou entrez le code PIN, voici la séquence réelle :

### Étape 1 : Pair Setup M1 (iOS → Accessoire)

```plaintext
iOS envoie : { method: "pair-setup", state: 1 }
```

Votre téléphone initialise le jumelage, disant à l'accessoire "Je veux me jumeler avec toi."

### Étape 2 : Pair Setup M2 (Accessoire → iOS)

```plaintext
L'accessoire envoie : { 
  state: 2,
  salt: <16 octets aléatoires>,
  public_key: <clé publique SRP B>
}
```

L'accessoire génère un sel SRP et une clé publique. Le code PIN que vous avez saisi n'est pas envoyé sur le réseau – à la place, il est utilisé pour dériver localement un vérificateur.

### Étape 3 : Pair Setup M3 (iOS → Accessoire)

```plaintext
iOS envoie : {
  state: 3,
  public_key: <clé publique SRP A>,
  proof: <preuve SRP M1>
}
```

Votre iPhone utilise le PIN pour calculer ses propres valeurs SRP et envoie une preuve qu'il connaît le PIN.

### Étape 4 : Pair Setup M4 (Accessoire → iOS)

```plaintext
L'accessoire envoie : {
  state: 4,
  proof: <preuve SRP M2>
}
```

L'accessoire vérifie la preuve. Si le PIN est incorrect, le jumelage échoue ici. S'il est correct, il renvoie sa propre preuve.

### Étapes 5-6 : Échange de clés

Désormais, les deux parties disposent d'un secret partagé dérivé du SRP. Elles l'utilisent pour établir un canal chiffré et échanger des clés publiques Ed25519 à long terme. Ces clés sont stockées de manière permanente. C'est pourquoi vos lampes fonctionnent toujours après le redémarrage de votre routeur.

Toute cette danse prend environ 2 secondes. Après cela, le `sf` dans l'enregistrement mDNS passe de `1` à `0` et l'accessoire disparaît de "Ajouter un accessoire".

## L'URI de configuration : que contient ce code QR ?

Le code QR contient une URI qui encode tout le nécessaire pour le jumelage :

```plaintext
X-HM://0ABCDEFGH1234
        ^^^^^^^^^^^^
        |       |
        |       +-- ID de configuration (4 chars)
        +---------- Charge utile encodée (9 chars, base-36)
```

La charge utile regroupe trois éléments dans 45 bits :

1. **Catégorie :** le type d'accessoire (5 = ampoule, 6 = prise, 10 = thermostat, etc.).
    
2. **Flags :** comment l'accessoire peut se jumeler (2 = supporte le jumelage IP/WiFi, 4 = supporte le jumelage BLE, 6 = supporte les deux).
    
3. **Code PIN** sous forme d'entier.
    

Cela permet à votre iPhone de savoir quelle icône afficher et quel PIN utiliser, le tout en scannant un seul code QR.

```go
func generateSetupURI(pin, setupID string, category int) string {
    // Le PIN "00102003" devient l'entier 102003
    var pinInt uint64
    for _, c := range pin {
        if c >= '0' && c <= '9' {
            pinInt = pinInt*10 + uint64(c-'0')
        }
    }

    // Disposition des bits :
    // [39:32] = catégorie (5 = ampoule)
    // [31:28] = flags (2 = jumelage IP supporté)
    // [26:0]  = code PIN
    payload := (uint64(category) << 32) | (2 << 28) | (pinInt & 0x7FFFFFF)

    // Encodage en base-36 (0-9, A-Z)
    const chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded := ""
    for payload > 0 {
        encoded = string(chars[payload%36]) + encoded
        payload /= 36
    }

    for len(encoded) < 9 {
        encoded = "0" + encoded
    }

    return "X-HM://" + encoded + setupID
}
```

Quand l'appareil photo de votre iPhone voit `X-HM://`, il sait qu'il s'agit d'un code HomeKit. Il décode la charge utile pour extraire la catégorie (afin d'afficher la bonne icône) et le PIN (pour que vous n'ayez pas à le taper). L'ID de configuration aide à l'identification lorsque plusieurs accessoires non jumelés sont sur le réseau.

## Ce qu'il se passe quand vous allumez ou éteignez la lampe

Passons maintenant à la partie qui m'intriguait le plus. Quand vous appuyez sur le bouton de la lampe dans l'application Maison, qu'est-ce qui circule réellement sur votre réseau ?

### Étape 1 : Session chiffrée

Votre iPhone n'envoie pas de commandes en clair. Chaque session jumelée utilise les clés à long terme échangées lors du jumelage pour établir une clé de session. Toute la communication est chiffrée avec ChaCha20Poly1305.

### Étape 2 : Requête HAP

À l'intérieur du canal chiffré, HomeKit utilise un protocole simple de type HTTP. Une commande "allumer" ressemble à ceci :

```plaintext
PUT /characteristics HTTP/1.1
Host: Virtual Light._hap._tcp.local
Content-Type: application/hap+json

{
  "characteristics": [{
    "aid": 1,        // ID de l'accessoire
    "iid": 10,       // ID de l'instance (la caractéristique "On")
    "value": true    // nouvel état
  }]
}
```

### Étape 3 : Réponse de l'accessoire

L'accessoire traite la requête et répond ainsi :

```plaintext
HTTP/1.1 204 No Content
```

Si quelque chose s'est mal passé, il renverra un objet de statut avec un code d'erreur.

Dans notre code Go, nous nous branchons là-dessus avec un callback :

```go
light.Lightbulb.On.OnValueRemoteUpdate(func(on bool) {
    if on {
        fmt.Println("💡 Light ON")
    } else {
        fmt.Println("💡 Light OFF")
    }
})
```

Ce callback se déclenche quand la `value` dans cette requête PUT change. La bibliothèque `brutella/hap` gère tout le déchiffrement, l'analyse syntaxique et la génération de la réponse.

## Le modèle de base de données des accessoires

HomeKit organise tout selon une hiérarchie :

```plaintext
Accessoire (aid=1)
└── Services
    ├── AccessoryInformation (iid=1)
    │   ├── Name (iid=2)
    │   ├── Manufacturer (iid=3)
    │   ├── Model (iid=4)
    │   └── SerialNumber (iid=5)
    │
    └── Lightbulb (iid=9)
        ├── On (iid=10)           ← boolean
        ├── Brightness (iid=11)   ← int 0-100
        └── Hue (iid=12)          ← float 0-360
```

Chaque caractéristique possède un `iid` (instance ID). Quand vous changez la luminosité à 75 %, la requête PUT cible `aid=1, iid=11, value=75`.

Ce modèle est la raison pour laquelle les accessoires HomeKit sont interopérables. Chaque ampoule, quel que soit le fabricant, possède la même structure de caractéristiques.

## Persistance des données de jumelage

Quand votre accessoire se jumelle avec un contrôleur (iPhone), il stocke :

* La clé publique Ed25519 du contrôleur.
    
* Un ID de contrôleur (UUID de 36 caractères).
    
* Le niveau de permission (administrateur ou utilisateur standard).
    

L'accessoire possède également ses propres paires de clés qui doivent persister après les redémarrages. Si vous les perdez, tous les contrôleurs jumelés deviennent orphelins – c'est-à-dire qu'ils pensent être jumelés, mais l'accessoire ne les reconnaît plus.

Comme mentionné précédemment, nous devons sauvegarder les informations de jumelage pour que si l'application ou l'appareil redémarre, il puisse communiquer à nouveau avec HomeKit. Vous pourriez utiliser une base de données, mais pour un seul accessoire, un fichier JSON suffit. Si le processus plante en milieu de session, vous ne perdrez pas les données de jumelage.

J'ai écrit un stockage JSON simple pour tout garder dans un seul fichier :

```go
type JSONStore struct {
    path string
    data map[string][]byte
    mu   sync.RWMutex
}

func (s *JSONStore) Set(key string, value []byte) error {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.data[key] = value
    return s.save()
}

func (s *JSONStore) Get(key string) ([]byte, error) {
    s.mu.RLock()
    defer s.mu.RUnlock()
    if v, ok := s.data[key]; ok {
        return v, nil
    }
    return nil, fmt.Errorf("key not found: %s", key)
}
```

La bibliothèque HAP stocke plusieurs clés :

* `uuid` – l'identifiant unique de l'accessoire.
    
* `public` / `private` – la paire de clés Ed25519.
    
* `*-pairings` – les clés des contrôleurs jumelés.
    

Si vous supprimez ce fichier JSON, l'accessoire (notre lampe virtuelle) oublie tous ses contrôleurs jumelés. Votre iPhone pense toujours être jumelé, mais l'accessoire ne le reconnaît plus – vous verrez "Sans réponse" dans l'application Maison. La solution consiste à supprimer l'accessoire de l'application Maison et à le jumeler à nouveau à l'aide du code QR.

## Notifications d'événements

Une chose à laquelle je ne m'attendais pas est que HomeKit supporte les notifications push provenant des accessoires. Quand l'état de notre lampe change (peut-être via un interrupteur physique), nous pouvons notifier tous les contrôleurs connectés :

```go
light.Lightbulb.On.SetValue(true)  // Ceci déclenche les notifications
```

Sous le capot, l'accessoire maintient des connexions persistantes avec les contrôleurs. Lorsqu'une caractéristique change, il envoie un message EVENT :

```plaintext
EVENT/1.0 200 OK
Content-Type: application/hap+json

{
  "characteristics": [{
    "aid": 1,
    "iid": 10,
    "value": true
  }]
}
```

C'est ainsi que votre application Maison se met à jour en temps réel quand quelqu'un d'autre allume une lampe.

## L'implémentation complète

Voici l'ensemble du code réuni :

```go
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "os"
    "os/signal"
    "sync"
    "syscall"

    "github.com/brutella/hap"
    "github.com/brutella/hap/accessory"
    "github.com/skip2/go-qrcode"
)

const (
    pinCode  = "00102003"
    setupID  = "VLTX"
    category = 5
    dbFile   = "data.json"
)

type JSONStore struct {
    path string
    data map[string][]byte
    mu   sync.RWMutex
}

func NewJSONStore(path string) *JSONStore {
    s := &JSONStore{
        path: path,
        data: make(map[string][]byte),
    }
    s.load()
    return s
}

func (s *JSONStore) load() {
    file, err := os.ReadFile(s.path)
    if err != nil {
        return
    }
    json.Unmarshal(file, &s.data)
}

func (s *JSONStore) save() error {
    file, err := json.MarshalIndent(s.data, "", "  ")
    if err != nil {
        return err
    }
    return os.WriteFile(s.path, file, 0644)
}

func (s *JSONStore) Set(key string, value []byte) error {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.data[key] = value
    return s.save()
}

func (s *JSONStore) Get(key string) ([]byte, error) {
    s.mu.RLock()
    defer s.mu.RUnlock()
    if v, ok := s.data[key]; ok {
        return v, nil
    }
    return nil, fmt.Errorf("key not found: %s", key)
}

func (s *JSONStore) Delete(key string) error {
    s.mu.Lock()
    defer s.mu.Unlock()
    delete(s.data, key)
    return s.save()
}

func (s *JSONStore) KeysWithSuffix(suffix string) ([]string, error) {
    s.mu.RLock()
    defer s.mu.RUnlock()
    var keys []string
    for k := range s.data {
        if len(k) >= len(suffix) && k[len(k)-len(suffix):] == suffix {
            keys = append(keys, k)
        }
    }
    return keys, nil
}

func generateSetupURI(pin, setupID string, category int) string {
    var pinInt uint64
    for _, c := range pin {
        if c >= '0' && c <= '9' {
            pinInt = pinInt*10 + uint64(c-'0')
        }
    }

    payload := (uint64(category) << 32) | (2 << 28) | (pinInt & 0x7FFFFFF)

    const chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded := ""
    for payload > 0 {
        encoded = string(chars[payload%36]) + encoded
        payload /= 36
    }

    for len(encoded) < 9 {
        encoded = "0" + encoded
    }

    return "X-HM://" + encoded + setupID
}

func main() {
    light := accessory.NewLightbulb(accessory.Info{
        Name:         "Virtual Light",
        Manufacturer: "My Smart Home",
    })

    light.Lightbulb.On.OnValueRemoteUpdate(func(on bool) {
        if on {
            fmt.Println("💡 Light ON")
        } else {
            fmt.Println("💡 Light OFF")
        }
    })

    store := NewJSONStore(dbFile)

    server, err := hap.NewServer(store, light.A)
    if err != nil {
        log.Fatal(err)
    }

    server.Pin = pinCode
    server.SetupId = setupID
    server.Addr = ":51826"

    fmt.Println("==============================================")
    fmt.Println("       Virtual HomeKit Light")
    fmt.Println("==============================================")
    fmt.Println("PIN: 001-02-003")
    fmt.Println()

    setupURI := generateSetupURI(pinCode, setupID, category)
    if qr, err := qrcode.New(setupURI, qrcode.Medium); err == nil {
        fmt.Println(qr.ToSmallString(false))
    }

    fmt.Println("Manual: Home app → + → More Options → Virtual Light")
    fmt.Printf("Data stored in: %s\n", dbFile)
    fmt.Println("==============================================")

    ctx, cancel := context.WithCancel(context.Background())
    go func() {
        c := make(chan os.Signal, 1)
        signal.Notify(c, os.Interrupt, syscall.SIGTERM)
        <-c
        cancel()
    }()

    fmt.Println("Running... (Ctrl+C to stop)")
    server.ListenAndServe(ctx)
}
```

Lancez-le, jumelez-le, et observez le terminal pendant que vous basculez l'interrupteur depuis votre téléphone. Chaque "💡 Light ON" est l'aboutissement d'une requête chiffrée qui a voyagé de votre téléphone, via votre routeur, jusqu'à ce processus Go.

## Ce que j'ai appris

Construire ce projet a clarifié plusieurs points qui étaient vagues pour moi :

1. **HomeKit est entièrement local.** Aucun serveur cloud n'est impliqué dans le contrôle des appareils – vos commandes vont directement du téléphone à l'appareil via votre réseau local (LAN). C'est pourquoi les appareils HomeKit fonctionnent même quand votre connexion internet est coupée.
    
2. **Le modèle de sécurité est solide.** L'utilisation de SRP pour le jumelage signifie que le PIN ne traverse jamais le réseau. Ed25519 + ChaCha20 pour les sessions signifie que même quelqu'un interceptant votre WiFi ne verra que des blobs chiffrés.
    
3. **Matter ne remplace pas le HAP.** Du moins pas dans l'écosystème Apple. Matter gère la découverte et le jumelage entre écosystèmes, mais Apple Home utilise toujours les concepts HAP en interne.
    
4. **Le protocole est de type HTTP.** Une fois le chiffrement passé, ce ne sont que des requêtes PUT/GET avec des corps JSON – étonnamment accessible.
    

### Merci de m'avoir lu !

Le [code est disponible ici](https://github.com/rezmoss/virtual-light) si vous voulez expérimenter par vous-même. Vous pourriez essayer d'ajouter le contrôle de la luminosité, ou créer un interrupteur au lieu d'une lampe. La meilleure façon de comprendre un protocole est de le parler ;)