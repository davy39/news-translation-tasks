---
title: 'Systèmes en temps réel pour les développeurs web : de la théorie à une application
  live Go + React'
subtitle: ''
author: Emmanuel Etukudo
co_authors: []
series: null
date: '2026-01-07T17:24:03.332Z'
originalURL: https://freecodecamp.org/news/real-time-systems-for-web-developers-from-theory-to-a-live-go-react-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767748231282/074fcd8b-8808-4a3d-8c9c-17d5a7b388e6.png
tags:
- name: React
  slug: reactjs
- name: Go Language
  slug: go
- name: websockets
  slug: websockets
- name: realtime apps
  slug: realtime-apps
seo_title: 'Systèmes en temps réel pour les développeurs web : de la théorie à une
  application live Go + React'
seo_desc: 'Many developers think that “real-time” is about Websockets, Live data,
  or instant refreshes on web application dashboards.

  And although these concepts are closely related to what real-time means, the systems
  engineering definition is a bit different....'
---

De nombreux développeurs pensent que le "temps réel" concerne les Websockets, les données en direct ou les rafraîchissements instantanés des tableaux de bord des applications web.

Et bien que ces concepts soient étroitement liés à ce que signifie le temps réel, la définition de l'ingénierie des systèmes est un peu différente. Un système en temps réel n'est pas défini par sa rapidité, mais par sa prévisibilité. 

Dans ce tutoriel, vous apprendrez ce que sont les systèmes en temps réel, pourquoi la plupart des applications web ne sont pas en temps réel, et comment construire un **système en temps réel souple** avec des outils que vous connaissez probablement déjà : Go, React et TypeScript.

À la fin de ce tutoriel, nous construirons une application live qui :

* traite les événements sensibles au temps
  
* fait respecter les délais
  
* abandonne le travail lorsqu'il est trop tard
  
* et visualise la latence et les délais manqués en temps réel
  

 Cet article vous aidera à façonner votre esprit la prochaine fois que vous construirez un système en temps réel.

## Table des matières


* [Prérequis](#heading-prerequis)
    
* [Ce qu'un système en temps réel signifie vraiment](#heading-ce-quun-systeme-en-temps-reel-signifie-vraiment)
    
    * [Types de systèmes en temps réel](#heading-types-de-systemes-en-temps-reel)
        
    * [Pourquoi la plupart des applications web ne sont pas en temps réel](#heading-pourquoi-la-plupart-des-applications-web-ne-sont-pas-en-temps-reel)
        
* [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
    
* [Architecture du système](#heading-architecture-du-systeme)
    
    * [Le temps fait partie de votre modèle de données](#heading-le-temps-fait-partie-de-votre-modele-de-donnees)
        
* [Pourquoi Go est un bon choix pour notre cas d'utilisation](#heading-pourquoi-go-est-un-bon-choix-pour-notre-cas-dutilisation)
    
    * [Génération d'événements avec Go](#heading-generation-devenements-avec-go)
        
    * [Traitement conscient des délais](#heading-traitement-conscient-des-delais)
        
    * [Application de la contre-pression](#heading-application-de-la-contre-pression)
        
    * [Diffusion d'événements vers le navigateur](#heading-diffusion-devenements-vers-le-navigateur)
        
    * [Consommation d'un événement WebSocket (React + TypeScript)](#heading-consommation-dun-evenement-websocket-react-typescript)
        
    * [Rendre React compatible avec le temps réel](#heading-rendre-react-compatible-avec-le-temps-reel)
        
    * [Création du composant StatsBar](#heading-creation-du-composant-statsbar)
        
    * [Création du tableau des événements](#heading-creation-du-tableau-des-evenements)
        
    * [Mettre le tout ensemble](#heading-mettre-le-tout-ensemble)
        
* [Réflexions finales](#heading-reflexions-finales)
  

## Prérequis

Ce tutoriel suppose que vous avez des connaissances de base en `Go`, `React` et `WebSockets`, en particulier le travail avec les goroutines et la consommation d'événements `WebSockets` dans `React`. Si ce n'est pas le cas, je vous recommande vivement de revoir les tutoriels d'introduction avant de continuer afin de tirer le meilleur parti de ce guide. 
 
Les références utiles incluent :

* **Concurrency et Goroutines en Go** : Le blog officiel de Go couvre les modèles de concurrency, y compris les goroutines et les canaux, qui sont [fondamentaux pour écrire du code Go concurrent](https://go.dev/blog/concurrency-patterns).
  
* **WebSockets avec Go** : Un tutoriel complet sur WebSocket utilisant le package populaire gorilla/websocket qui montre comment configurer un serveur WebSocket en Go et gérer les connexions et les messages. [Voici un tutoriel Go WebSocket (avec gorilla/websocket)](https://tutorialedge.net/golang/go-websocket-tutorial).
  
* **WebSockets dans React** : Un guide complet sur les WebSockets dans React, expliquant comment ouvrir et gérer une connexion WebSocket et traiter les messages entrants dans les composants. [Voici un guide complet sur les WebSockets avec React](https://ably.com/blog/websockets-react-tutorial).
  

Les technologies avec lesquelles nous travaillerons incluent :

* `Go`, pour construire notre système backend et faire respecter les garanties en temps réel
  
* `React`, pour construire une interface utilisateur frontend réactive qui affiche les événements diffusés
  
* `Websocket`, pour la livraison à faible latence des données du backend au client
  

## Ce qu'un système en temps réel signifie vraiment

Dans une application web traditionnelle, la justesse est mesurée par le fait que le système a produit le bon résultat. Dans un système en temps réel, la justesse est mesurée par le fait que le système a produit le bon résultat **avant la date limite**. Si le résultat du test est « Non », alors le système a échoué – même si le résultat est correct.

### Types de systèmes en temps réel 

Il existe quelques types différents de systèmes en temps réel dont vous devriez être conscient, chacun avec des niveaux de rigueur variables :

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Système en temps réel</strong></p></td><td colspan="1" rowspan="1"><p><strong>Niche applicable</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Temps réel strict : </strong>Manquer une date limite est catastrophique ici.</p></td><td colspan="1" rowspan="1"><p>Contrôle de vol et stimulateurs cardiaques</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Temps réel souple :</strong> Manquer une date limite dégrade la qualité mais ne fait pas planter le système.</p></td><td colspan="1" rowspan="1"><p>Diffusion vidéo et tableaux de bord de trading</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Temps réel ferme</strong> : Les résultats tardifs sont inutiles et doivent être jetés.</p></td><td colspan="1" rowspan="1"><p>Applications web/mobiles de vente aux enchères de voitures</p></td></tr></tbody></table>

La majorité des systèmes en temps réel basés sur le web entrent dans la catégorie des systèmes en temps réel souple, et c'est exactement ce que nous allons construire ici.

### Pourquoi la plupart des applications web ne sont pas en temps réel

Il existe de nombreuses raisons pour lesquelles un système peut ne pas être en temps réel, et généralement, même ceux commercialisés comme des applications en temps réel manquent de cette garantie.

Voici pourquoi :

1. Les Websockets garantissent la livraison, pas la ponctualité
  
2. Les files de messages sont optimisées pour la durabilité et le débit
  
3. La mise en mémoire tampon infinie masque les délais
  
4. Les interfaces utilisateur (UI) rendent quand elles peuvent, pas quand elles devraient 
  

En d'autres termes, les données arriveront éventuellement, mais rien n'impose quand elles doivent être traitées. C'est exactement l'écart que nous allons combler dans ce tutoriel.

## Ce que nous allons construire 

Dans ce tutoriel, nous allons construire un moniteur d'événements en direct conscient des délais. Vous pouvez le considérer comme un système en temps réel simplifié pour les données de capteurs, les événements de trading, les alertes ou la télémétrie en direct.

Notre application aura ces fonctionnalités et contraintes :

* Les événements sont générés à un taux fixe
  
* Chaque événement a un délai
  
* Le backend traite les événements uniquement s'ils peuvent être complétés à temps
  
* Les événements tardifs sont marqués ou abandonnés
  
* Le frontend visualise :
  
  * la latence de traitement
    
    * les délais manqués
    
    * et la santé du système
    

Cela nous donnera les métriques nécessaires pour mesurer le comportement en temps réel du système au lieu de deviner.

## Architecture du système 

L'architecture du système de haut niveau ressemble à ceci :

```plaintext

+-------------+     +------------------+     +----------------+
| Event       | --> | Deadline-Aware   | --> | WebSocket      |
| Generator   |     | Go Processor     |     | Server         |
+-------------+     +------------------+     +----------------+
                                                     |
                                                     v
                                           +----------------+
                                           | React Dashboard|
                                           +----------------+
```

Décomposons les responsabilités :

**Backend :**

* Génère des événements sensibles au temps
  
* Fait respecter les délais
  
* Applique la contre-pression
  
* Diffuse le résultat au client (frontend)
  

**Front End :**

* Consomme des événements en temps réel
  
* Affiche les métriques en direct
  
* Reste réactif sous charge
  

#### Le temps fait partie de votre modèle de données

Dans un système en temps réel, le temps est explicite, pas implicite. Cela signifie que chaque événement traité inclut :

* quand il a été créé
  
* combien de temps il est autorisé à vivre, et
  
* quand il a été traité
  

Conceptuellement, un modèle de données typique pour un événement ressemble à ceci :

```typescript
{
  id: string
  createdAt: number
  deadlineMs: number
  processedAt?: number
  status: "on-time" | "late" | "dropped"
}
```

C'est le changement de mentalité que nous espérons établir : dans un système en temps réel, le temps est un composant essentiel pour votre système qui garantit la précision.

## Pourquoi Go est un bon choix pour notre cas d'utilisation

Go n'est pas un langage en temps réel strict, mais il est excellent pour les charges de travail en temps réel souple. Cela est dû à ses :

* Goroutines peu coûteuses
  
* Concurrency structurée avec des canaux
  
* Propagation des délais via `context.Context`
  
* Comportement d'exécution simple
  

Plus important encore, Go facilite l'**échec rapide**, ce qui est essentiel pour les systèmes en temps réel.

### Génération d'événements avec Go

Nous commencerons le développement de notre système backend en définissant d'abord la structure Event et en créant une fonction de générateur d'événements à taux fixe :

```go
type Event struct {
   ID        string
   CreatedAt time.Time
   DeadlineMs    time.Duration
}
```

Ici, nous avons créé une structure `Event` avec les propriétés suivantes :

* `ID` un identifiant unique qui aide à la gestion de chaque événement traité par le système
  
* `CreatedAt` pour suivre l'heure à laquelle l'événement a été créé
  
* `Deadline` pour aider à évaluer si l'événement a respecté le délai assigné ou s'il a échoué
  

Ensuite, nous créerons la fonction de générateur d'événements `startGenerator` :

```go
func startGenerator(out chan<- Event) {
   ticker := time.NewTicker(50 * time.Millisecond)
   defer ticker.Stop()

   for range ticker.C {
       event := Event{
           ID:        uuid.New().String(),
           CreatedAt: time.Now(),
           DeadlineMs: 100,
       }

       select {
       case out <- event:
       default:
           // Drop event when load peaks on the goroutine
       }
   }
}
```

Ici, la fonction de générateur d'événements accepte un canal `Go` comme paramètre et utilise un canal `time.Ticker` qui se déclenche toutes les **50 millisecondes**. À chaque tick, elle crée un nouvel `Event` avec un `ID` unique, un timestamp de création et un **délai de 100 millisecondes** (`DeadlineMs: 100`).

Le générateur tente ensuite d'envoyer l'événement dans le canal de sortie en utilisant un envoi non bloquant. Si le canal est prêt, l'événement est livré immédiatement. Si le canal n'est pas prêt (par exemple, parce que les consommateurs en aval sont lents ou surchargés), le cas `default` est exécuté et l'événement est abandonné.

Pourquoi devons-nous abandonner l'événement ici ? Eh bien, parce que masquer la surcharge supprime les garanties en temps réel. En bref, **abandonner les événements est une stratégie délibérée de contre-pression** : elle empêche la surcharge de se propager à travers le système et protège les limites de latence, ce qui est souvent plus important que l'exhaustivité dans les systèmes de diffusion en temps réel.

### Traitement conscient des délais

Ensuite, nous créerons la fonction `processEvent` pour gérer le traitement de l'événement. En Go, vous pouvez faire respecter les délais en utilisant `context.WithTimeout` comme ceci :

```go
func processEvent(event Event) string {
   ctx, cancel := context.WithTimeout(
       context.Background(),
       event.Deadline,
   )

   defer cancel()
   workDone := make(chan struct{})

   go func() {
       time.Sleep(50 * time.Millisecond)
       close(workDone)

   }()

   select {
   case <-workDone:
       return "on-time"
   case <-ctx.Done():
       return "late"
   }
}
```

Ici, nous avons intentionnellement veillé à ce que le travail se termine avant le délai ou échoue immédiatement.

Dans la fonction `processEvent`, chaque événement est traité sous un délai strict imposé par un contexte avec un délai d'attente. La durée du délai d'attente est dérivée directement du délai de l'événement, ce qui signifie que l'événement n'est considéré comme valide que dans la fenêtre de temps spécifiée.

Le travail réel est exécuté dans une goroutine séparée, qui simule le traitement en dormant pendant **50 millisecondes**, puis signale l'achèvement en fermant le canal `workDone`. Nous avons intentionnellement structuré cela de sorte que le travail soit soit terminé dans le délai, soit traité comme un échec immédiatement.

### **Application de la contre-pression** 

Dans les systèmes en temps réel, les files d'attente ne résolvent pas la surcharge – elles la reportent simplement. Lorsque les événements entrants arrivent plus rapidement qu'ils ne peuvent être traités, une file d'attente continue de croître, augmentant le temps que chaque événement passe en attente.

Les tampons peuvent également masquer les échecs. En absorbant la charge excédentaire, ils créent l'illusion que le système est sain, même si les retards de traitement dépassent les limites acceptables. Cette dégradation cachée est dangereuse car le système continue de fonctionner dans un état compromis, produisant des résultats techniquement corrects mais opérationnellement inutiles en raison de leur retard.

À mesure que les files d'attente et les tampons croissent, la latence augmente silencieusement. Il n'y a souvent aucune erreur explicite ou signal indiquant que les délais ne sont pas respectés – le système devient simplement plus lent avec le temps. Dans les systèmes en temps réel, cette croissance silencieuse de la latence est particulièrement néfaste car elle viole l'hypothèse selon laquelle les résultats sont livrés dans une fenêtre de temps connue et bornée.

Pour ces raisons, je recommande fortement d'utiliser des canaux bornés. Lorsque le système est submergé, les canaux bornés appliquent une contre-pression en refusant le travail supplémentaire. Au lieu de bloquer indéfiniment ou de faire croître des files d'attente illimitées, le système abandonne les événements lorsqu'il ne peut pas suivre.

Ce comportement rend les échecs visibles. Les événements abandonnés sont un signal explicite que le système fonctionne au-delà de sa capacité. Plutôt que de se dégrader de manière imprévisible, le système se dégrade de manière contrôlée et observable. Dans ce contexte, l'abandon d'événements est une fonctionnalité, et non un bug, car il préserve les garanties de latence pour les événements qui sont traités et permet aux opérateurs de détecter, de raisonner et de répondre immédiatement aux conditions de surcharge.

### Diffusion d'événements vers le navigateur

Ensuite, nous construirons le système de diffusion WebSocket pour pousser les événements traités vers le frontend en utilisant le package WebSocket [Gorilla](http://github.com/gorilla/websocket) `Go` (mais vous pouvez utiliser n'importe quel package de votre choix).

```go
package main

import (
    "encoding/json"
    "net/http"
    "github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
    CheckOrigin: func(r *http.Request) bool {
        return true
    },
}

func wsHandler(out <-chan Event) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        conn, _ := upgrader.Upgrade(w, r, nil)
        defer conn.Close()
        for event := range out {
            data, _ := json.Marshal(event)
            conn.WriteMessage(websocket.TextMessage, data)
        }
    }
}
```

Ici, nous mettons simplement à niveau une requête `HTTP` entrante vers une connexion `WebSocket` et lisons en continu les événements de notre canal `Event` créé précédemment, en sérialisant chaque événement en `JSON` et en le diffusant au client connecté. Il agit purement comme une couche de transport, poussant les événements déjà traités vers les clients avec une faible latence.

Il est important de noter que les `WebSockets` ne rendent pas un système en temps réel. Les `WebSockets` fournissent simplement une livraison à faible latence du backend au client. Les garanties en temps réel sont établies plus tôt dans le pipeline backend grâce à des choix de conception délibérés : génération d'événements à taux fixe, délais explicites par événement, files d'attente bornées, envois non bloquants, traitement conscient des délais utilisant des contextes, et comportement de défaillance rapide lorsque les délais sont dépassés.

Au moment où un événement est envoyé via un `WebSocket`, il a déjà soit respecté ses contraintes en temps réel, soit été abandonné. La couche `WebSocket` transporte simplement le résultat – elle n'applique ni ne crée de comportement en temps réel.

### Consommation d'un événement WebSocket (React + TypeScript)

Jusqu'à présent, nous avons construit le backend de notre générateur d'événements en temps réel et de notre système de diffusion. Dans les prochaines sections, nous construirons le frontend du système en utilisant `React` et `TypeScript`.

Nous commencerons par initialiser un client `WebSocket` pour consommer les événements entrants du backend en utilisant l'interface WebSocket traditionnelle du navigateur.

```typescript
const socket = new WebSocket("ws://localhost:8080/ws");
socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    buffer.push(data);
};
```

Ici, nous initialisons simplement un nouveau `WebSocket`, en transmettant l'URL WebSocket du backend. Vous devez référencer la même URL. Au lieu de rendre chaque message immédiatement, il est recommandé de toujours regrouper les mises à jour.

### Rendre React compatible avec le temps réel

Ensuite, créons un hook `React` `useRealTimeEvents` pour gérer la diffusion et le traitement des événements diffusés par le backend. Le rendu à chaque message provoque des tempêtes de rendu, des retards d'interface utilisateur et des tableaux de bord trompeurs. Au lieu de cela, nous rendons sur les frames d'animation.

```typescript
import { useEffect, useRef, useState } from 'react';
import type { RealTimeEvent } from 'types/types';

function useRealTimeEvents() {
  const [events, setEvents] = useState<RealTimeEvent[]>([]);
  const buffer = useRef<RealTimeEvent[]>([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080/ws');
    ws.onmessage = (msg) => {
      buffer.current.push(JSON.parse(msg.data));
    };

    let raf: number;

    const flush = () => {
      if (buffer.current.length > 0) {
        const pendingEvents = buffer.current.slice(0);

        setEvents((prev) => {
          const next = [...prev, ...pendingEvents];
          return next.slice(-50);
        });
      }
      raf = requestAnimationFrame(flush);
    };

    raf = requestAnimationFrame(flush);

    return () => {
      ws.close();
      cancelAnimationFrame(raf);
    };
  }, []);
  return events;
}

export default useRealTimeEvents;
```

L'interface utilisateur fait partie du système en temps réel. Il est important de noter que le système diffuse des messages au frontend en millisecondes. Ce comportement dépasse déjà le seuil de taux de rafraîchissement du navigateur web.

Dans certaines situations, vous pourriez même penser que l'utilisation de `setTime` devrait être utile ici. Et c'est une bonne alternative – mais il existe une meilleure solution : utiliser `requestAnimationFrame()`.

La fonction `requestAnimationFrame()` prend une fonction de rappel `flush` qui est régulée par la frame d'animation, garantissant que nous ne dépassons pas le seuil de taux de rafraîchissement avant la prochaine repaint. Vous pouvez en apprendre plus sur `requestAnimationFrame()` [ici](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/requestAnimationFrame).

### Création du composant StatsBar

Ensuite, créons un petit composant `statusBar` pour afficher les événements arrivés dans les délais et ceux arrivés en retard.

Créez un nouveau composant `StatsBar` et ajoutez le code ci-dessous :

```typescript
import { type FC } from 'react';
import type { RealTimeEvent } from 'types/types';

const StatsBar: FC<{ events: RealTimeEvent[] }> = ({ events }) => {
  const late = events.filter((e) => e.status === 'late').length;
  return (
    <div className="flex flex-row gap-2 bg-gray-500 w-full py-2.5 px-2">
      <strong>Événements : {events.length} | </strong>
      <strong>En retard : {late}</strong>
    </div>
  );
};

export default StatsBar;
```

Ici, nous créons un composant de statistiques minimal pour afficher le nombre total d'événements et ceux arrivés en retard en parcourant la liste des événements entrants dont les statuts sont "en retard".

### Création du tableau des événements

Ensuite, nous créerons un composant `EventTable` pour afficher les événements.

```typescript
import { type FC } from 'react';
import type { RealTimeEvent } from 'types/types';

export const EventsTable: FC<{ events: RealTimeEvent[] }> = ({ events }) => {
  const formatDate = (date: string) => new Date(date).toLocaleString();
  return (
    <div className="w-full">
      <div className="relative overflow-x-auto bg-neutral-primary-soft shadow-xs rounded-base border border-default">
        <table className="w-full text-sm text-left rtl:text-right text-body">
          <thead className="text-sm text-body bg-neutral-secondary-soft border-b rounded-base border-default">
            <tr>
              <th scope="col" className="px-6 py-3 font-medium">
                ID
              </th>
              <th scope="col" className="px-6 py-3 font-medium">
                Statut
              </th>
              <th scope="col" className="px-6 py-3 font-medium">
                Créé le
              </th>
              <th scope="col" className="px-6 py-3 font-medium">
                Traité le
              </th>
              <th scope="col" className="px-6 py-3 font-medium">
                Délai
              </th>
            </tr>
          </thead>
          <tbody>
            {events.map((e, i) => (
              <tr
                key={e.id + i}
                className="bg-neutral-primary border-b border-default"
              >
                <td className="px-6 py-4">{e.id.slice(0, 6)}</td>
                <td className="px-6 py-4">{e.status}</td>
                <td className="px-6 py-4">{formatDate(e.createdAt)}</td>
                <td className="px-6 py-4">{formatDate(e.processedAt)}</td>
                <td className="px-6 py-4">{e.deadlineMs}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
```

Ici, nous parcourons tous les événements entrants et affichons l'`id`, le `statut` et le `délai` de l'événement. Ces métriques nous aideront à obtenir des informations sur les performances de notre système de diffusion d'événements en temps réel.

### Mettre le tout ensemble

À ce stade, nous avons implémenté une application en temps réel complète, de bout en bout, qui connecte un backend `Go` conscient des délais à un frontend `React` léger. Sur le backend, les événements sont générés à un taux fixe, traités sous des délais explicites, et abandonnés lorsque le système est sous charge pour préserver les garanties en temps réel. Seuls les événements qui respectent ces garanties sont transférés aux clients connectés via une diffusion `WebSocket`.

Sur le frontend, nous avons construit le hook `useRealtimeEvents` pour établir une connexion `WebSocket` persistante et diffuser en continu les événements du backend à mesure qu'ils arrivent. Le composant `StatsBar` fournit une visibilité immédiate sur le comportement du système en résumant les caractéristiques clés du flux d'événements, tandis que le composant `EventTable` rend les événements individuels dans l'ordre où ils sont reçus. Ensemble, ces composants reflètent clairement le comportement du système dans des conditions normales en temps réel.

Avec les composants frontend et backend en place, l'application fonctionne désormais comme un moniteur en temps réel. Le backend applique les délais et la correction, et le frontend reflète simplement le résultat de ces décisions en temps réel. Il n'y a pas de logique de tamponnage ou de relecture côté client – ce qui est affiché sur l'`UI` est exactement ce que le système a pu traiter dans le délai spécifié.

Enfin, remplacez votre composant `Welcome` par le code ci-dessous pour afficher les composants `StatusBar` et `EventsTable`.

```typescript
import { useRealtimeEvents } from "./hooks/useRealtimeEvents";
import { StatsBar } from "./components/StatsBar";
import { EventTable } from "./components/EventTable";

export default function App() {
  const events = useRealtimeEvents();

  return (
    <div>
      <h1>Moniteur d'événements en temps réel</h1>
      <StatsBar events={events} />
      <EventTable events={events} />
    </div>
  );
}
```

Le frontend React est échafaudé en utilisant [create-react-app](https://react.dev/learn/creating-a-react-app), mais la même approche peut être utilisée pour d'autres frameworks, tels que `Next.js` ou `Vite`. Le code source complet, y compris le frontend et le backend, est disponible dans le dépôt [ici](https://github.com/emmanueletukudo/realtime-go-react). Vous pouvez me contacter sur la plateforme [X](https://x.com/eetukudo_) si vous avez besoin de mon assistance.

## Réflexions finales

Si vous avez suivi ce tutoriel jusqu'à ce point, félicitations ! Vous avez appris la partie la plus critique de la construction de systèmes en temps réel résilients et conscients des délais.

N'oubliez pas, les systèmes en temps réel ne concernent pas la vitesse, mais la **prévisibilité**. Vous n'avez pas besoin d'un système d'exploitation en temps réel (RTOS), d'un doctorat ou de matériel spécialisé pour commencer à apprendre la conception en temps réel.