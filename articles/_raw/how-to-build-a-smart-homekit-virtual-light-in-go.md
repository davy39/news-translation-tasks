---
title: How to Build a Smart HomeKit Virtual Light in Go
subtitle: ''
author: Rez Moss
co_authors: []
series: null
date: '2025-12-19T00:41:41.417Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-smart-homekit-virtual-light-in-go
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
seo_title: null
seo_desc: 'Recently, I wanted to understand how smart home devices actually work.
  When you scan a QR code and a light appears in your Home app, what''s really happening?
  When you tap "on", what bytes travel across your network?


  The best way I know to understand...'
---

Recently, I wanted to understand how smart home devices actually work. When you scan a QR code and a light appears in your Home app, what's really happening? When you tap "on", what bytes travel across your network?

![Virtual HomeKit Light QR code](https://cdn.hashnode.com/res/hashnode/image/upload/v1765414117210/e65d5768-792d-4aae-8669-db0ac7a9c60d.png align="center")

The best way I know to understand something is to build it, so I created a virtual HomeKit light in Go. And in this tutorial, I’ll walk you through how I went about it. We’ll pull back the curtain on smart home protocols so you understand how they work, in depth. Let’s dive in.

### What we’ll cover:

1. [What HomeKit Actually Is](#heading-what-homekit-actually-is)
    
2. [The Smart Home Protocol Landscape](#heading-the-smart-home-protocol-landscape)
    
3. [How HomeKit Discovery Works](#heading-how-homekit-discovery-works)
    
4. [The Pairing Process: What Happens When You Scan the QR Code](#heading-the-pairing-process-what-happens-when-you-scan-the-qr-code)
    
5. [The Setup URI: What's in That QR Code?](#heading-the-setup-uri-whats-in-that-qr-code)
    
6. [What Happens When You Toggle the Light](#heading-what-happens-when-you-toggle-the-light)
    
7. [The Accessory Database Model](#heading-the-accessory-database-model)
    
8. [Persisting Pairing Data](#heading-persisting-pairing-data)
    
9. [Event Notifications](#heading-event-notifications)
    
10. [The Complete Implementation](#heading-the-complete-implementation)
    
11. [What I Learned](#heading-what-i-learned)
    

## What You'll Need

Before we start building, let's make sure you have the right setup. This project requires two things:

1. **Go 1.21 or later**: We're using some modern Go features, and the brutella/HAP library works best with recent versions. You can check your version with `go version`. If you need to upgrade, grab the latest from go.dev
    
2. **An Apple HomeKit environment**: This means an iPhone or iPad running iOS 15+ with the Home app. You'll also want to be on the same WiFi network as the machine running your virtual light. HomeKit is entirely local, so your phone needs to be able to reach your development machine directly.
    

One thing that tripped me up initially is that if you’re running this on a Linux server or inside a container, make sure mDNS traffic isn’t being blocked. Your firewall needs to allow UDP port 5353 (for mDNS discovery) and whatever port your accessory runs on (we'll use 51826). On a Mac this usually just works.

## What HomeKit Actually Is

HomeKit is Apple's smart home framework. It's comprised of three things:

1. **a protocol (HAP)** that defines how devices talk to each other,
    
2. **a security model** that encrypts and authenticates everything,
    
3. **and an ecosystem** (the Home app, Siri, automations)
    

Here, we’ll be focused on the protocol layer. We're building something that speaks HAP well enough that Apple's ecosystem accepts it as a real accessory.

## The Smart Home Protocol Landscape

Before getting started, let's understand what we're dealing with. There are two protocols at play here:

1. **HomeKit Accessory Protocol (HAP):** Apple's original smart home protocol from 2014. It runs over your local WiFi network, uses mDNS for discovery, and encrypts everything with Curve25519 and ChaCha20-Poly1305. Every HomeKit device you've ever used speaks HAP.
    
2. **Matter**: The new industry standard (2022) backed by Apple, Google, Amazon, and others. Matter is actually built on many of the same cryptographic primitives as HAP. When Apple added Matter support, they essentially made HomeKit bilingual, as it can speak both protocols.
    

Here's what's interesting: Matter devices that connect to Apple Home still end up being controlled through HomeKit's infrastructure. Matter is the pairing and discovery layer, but once a device is in your Home, Apple's ecosystem takes over.

For this project, I'm using the HAP protocol directly via the `brutella/hap` library. This lets us see exactly what's happening without Matter's additional abstraction layer.

## How HomeKit Discovery Works

When you run a HomeKit accessory on your network, it doesn't just sit there waiting. It actively announces itself using **mDNS** (multicast DNS), also called Bonjour on Apple platforms.

The accessory broadcasts a service record that looks like this:

```plaintext
_hap._tcp.local.
  name: Virtual Light._hap._tcp.local.
  port: 51826
  txt: 
    c#=1          // config number (changes trigger rediscovery)
    ff=0          // feature flags
    id=XX:XX:XX   // device ID (like a MAC address)
    md=Virtual Light  // model name
    pv=1.1        // protocol version
    s#=1          // state number
    sf=1          // status flag (1=not paired, 0=paired)
    ci=5          // category (5=lightbulb)
    sh=XXXXXX     // setup hash
```

Your iPhone is constantly listening for `_hap._tcp.local.` broadcasts. When it sees one with `sf=1` (unpaired), it shows up in "Add Accessory" as available.

Let's see this in code. Here's the minimal server setup:

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

When `ListenAndServe` runs, it:

1. Generates a unique device ID if one doesn't exist
    
2. Starts listening on port 51826
    
3. Registers the mDNS service record
    
4. Waits for connections
    

At this point, your iPhone can discover it. But what happens when you try to pair it?

## The Pairing Process: What Happens When You Scan the QR Code

This is where it gets interesting. HomeKit uses the **SRP (Secure Remote Password)** protocol for pairing. It’s the same protocol used in things like 1Passwords authentication.

When you scan the QR code or enter the PIN, here's the actual sequence:

### Step 1: Pair Setup M1 (iOS → Accessory)

```plaintext
iOS sends: { method: "pair-setup", state: 1 }
```

Your phone initiates pairing, telling the accessory "I want to pair with you."

### Step 2: Pair Setup M2 (Accessory → iOS)

```plaintext
Accessory sends: { 
  state: 2,
  salt: <16 random bytes>,
  public_key: <SRP public key B>
}
```

The accessory generates an SRP salt and public key. The PIN code you entered isn't sent over the network – instead, it's used to derive a verifier locally.

### Step 3: Pair Setup M3 (iOS → Accessory)

```plaintext
iOS sends: {
  state: 3,
  public_key: <SRP public key A>,
  proof: <SRP proof M1>
}
```

Your iPhone uses the PIN to compute its own SRP values and sends a proof that it knows the PIN.

### Step 4: Pair Setup M4 (Accessory → iOS)

```plaintext
Accessory sends: {
  state: 4,
  proof: <SRP proof M2>
}
```

The accessory verifies the proof. If the PIN was wrong, pairing fails here. If correct, it sends its own proof back.

### Step 5-6: Key Exchange

Now both sides have a shared secret derived from SRP. They use this to establish an encrypted channel and exchange long term Ed25519 public keys. These keys are stored permanently. This is why your lights still work after rebooting your router.

The whole dance takes about 2 seconds. After this, `sf` in the mDNS record changes from `1` to `0` and the accessory disappears from "Add Accessory".

## The Setup URI: What's in That QR Code?

The QR code contains a URI that encodes everything needed for pairing:

```plaintext
X-HM://0ABCDEFGH1234
        ^^^^^^^^^^^^
        |       |
        |       +-- Setup ID (4 chars)
        +---------- Encoded payload (9 chars, base-36)
```

The payload packs three things into 45 bits:

1. **Category:** what type of accessory this is (5 = lightbulb, 6 = outlet, 10 = thermostat, and so on)
    
2. **Flags:** how the accessory can pair (2 = supports IP ,wifi pairing , 4 = supports BLE pairing , 6 = supports both)
    
3. **PIN code** as integer
    

This lets your iPhone know what icon to show and the PIN to use, all from scanning a single QR code.

```go
func generateSetupURI(pin, setupID string, category int) string {
    // PIN "00102003" becomes integer 102003
    var pinInt uint64
    for _, c := range pin {
        if c >= '0' && c <= '9' {
            pinInt = pinInt*10 + uint64(c-'0')
        }
    }

    // Bit layout:
    // [39:32] = category (5 = lightbulb)
    // [31:28] = flags (2 = IP pairing supported)
    // [26:0]  = PIN code
    payload := (uint64(category) << 32) | (2 << 28) | (pinInt & 0x7FFFFFF)

    // Encode as base-36 (0-9, A-Z)
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

When your iPhone camera sees `X-HM://`, it knows this is a HomeKit code. It decodes the payload to extract the category (so it can show the right icon) and the PIN (so you don't have to type it). The setup ID helps with identification when multiple unpaired accessories are on the network.

## What Happens When You Toggle the Light

Now for the part I was most curious about. When you tap the light button in the Home app, what actually travels across your network?

### Step 1: Encrypted Session

Your iPhone doesn't just send commands in plaintext. Every paired session uses the longterm keys exchanged during pairing to establish a session key. All communication is encrypted with ChaCha20Poly1305.

### Step 2: HAP Request

Inside the encrypted channel, HomeKit uses a simple HTTP like protocol. A "turn on" command looks like this:

```plaintext
PUT /characteristics HTTP/1.1
Host: Virtual Light._hap._tcp.local
Content-Type: application/hap+json

{
  "characteristics": [{
    "aid": 1,        // accessory ID
    "iid": 10,       // instance ID (the "On" characteristic)
    "value": true    // new state
  }]
}
```

### Step 3: Accessory Response

The accessory processes the request and responds like this:

```plaintext
HTTP/1.1 204 No Content
```

If something went wrong, it'll return a status object with an error code.

In our Go code, we hook into this with a callback:

```go
light.Lightbulb.On.OnValueRemoteUpdate(func(on bool) {
    if on {
        fmt.Println("💡 Light ON")
    } else {
        fmt.Println("💡 Light OFF")
    }
})
```

This callback fires when the `value` in that PUT request changes. The `brutella/hap` library handles all the decryption, parsing, and response generation.

## The Accessory Database Model

HomeKit organizes everything into a hierarchy:

```plaintext
Accessory (aid=1)
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

Each characteristic has an `iid` (instance ID). When you change brightness to 75%, the PUT request targets `aid=1, iid=11, value=75`.

This model is why HomeKit accessories are interoperable. Every lightbulb, regardless of manufacturer, has the same characteristic structure.

## Persisting Pairing Data

When your accessory pairs with a controller (iPhone), it stores:

* The controller's Ed25519 public key
    
* A controller ID (36chars UUID)
    
* Permission level (admin or regular user)
    

The accessory also has its own keypairs that must persist across restarts. If you lose this, all paired controllers become orphaned – that is, they think they’re paired, but the accessory doesn't recognize them.

As mentioned earlier, we need to save pairing info so that if the app/device restarts, it can communicate with Homekit again. You could use a database, but for a single accessory, a JSON file works fine. If the process crashes mid-session, you won’t lose pairing data.

I wrote a simple JSON store to keep everything in one file:

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

The HAP library stores several keys:

* `uuid` – accessory's unique identifier
    
* `public` / `private` – Ed25519 keypair
    
* `*-pairings` – paired controller keys
    

If you delete this JSON file, the accessory (our virtual-light) forgets all its paired controllers. Your iPhone still thinks it's paired, but the accessory doesn't recognize it anymore – you'll see "No Response" in the Home app. The fix removes the accessory from the Home app and pairs it fresh using the QR code again.

## Event Notifications

One thing I didn't expect is that HomeKit supports push notifications from accessories. When our light state changes (maybe from a physical switch), we can notify all connected controllers:

```go
light.Lightbulb.On.SetValue(true)  // This triggers notifications
```

Under the hood, the accessory maintains persistent connections with controllers. When a characteristic changes, it sends an EVENT message:

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

This is how your Home app updates in realtime when someone else turns on a light.

## The Complete Implementation

Here's everything together:

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

Run it, pair it, and watch the terminal as you toggle from your phone. Each "💡 Light ON" is the end of an encrypted request that traveled from your phone, through your router, to this Go process.

## What I Learned

Building this cleared up several things I'd been fuzzy on:

1. **HomeKit is entirely local.** There are no cloud servers involved in controlling devices – your commands go directly from phone to device over your LAN. This is why HomeKit devices work when your internet is down.
    
2. **The security model is solid.** SRP for pairing means the PIN never crosses the network. Ed25519 + ChaCha20 for sessions means that even someone sniffing your WiFi sees only encrypted blobs.
    
3. **Matter doesn't replace HAP.** At least not in Apple's ecosystem. Matter handles discovery and pairing across ecosystems, but Apple Home still uses HAP concepts internally.
    
4. **The protocol is HTTPish.** Once you get past the encryption, it’s just PUT/GET requests with JSON bodies – surprisingly approachable.
    

### Thanks for reading!

The [code is here](https://github.com/rezmoss/virtual-light) if you want to experiment yourself. You could try adding brightness control, or create a switch instead of a light. The best way to understand a protocol is to speak it ;)
