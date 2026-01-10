---
title: Comment construire un chatbot IA conversationnel avec Stream Chat et React
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2025-06-17T20:29:11.402Z'
originalURL: https://freecodecamp.org/news/build-a-conversational-ai-chatbot-with-stream-chat-and-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750192110424/b23653af-c2de-4631-973f-dcac3c0bdb41.png
tags:
- name: React
  slug: reactjs
- name: AI
  slug: ai
- name: chatbot
  slug: chatbot
seo_title: Comment construire un chatbot IA conversationnel avec Stream Chat et React
seo_desc: Modern chat applications are increasingly incorporating voice input capabilities
  because they offer a more engaging and versatile user experience. This also improves
  accessibility, allowing users with different needs to interact more comfortably
  with...
---

Les applications de chat modernes intègrent de plus en plus des capacités de saisie vocale car elles offrent une expérience utilisateur plus engageante et polyvalente. Cela améliore également l'accessibilité, permettant aux utilisateurs ayant des besoins différents d'interagir plus confortablement avec de telles applications.

Dans ce tutoriel, je vais vous guider à travers le processus de création d'une application IA conversationnelle qui intègre une fonctionnalité de chat en temps réel avec reconnaissance vocale. En tirant parti de Stream Chat pour une messagerie robuste et de l'API Web Speech pour la conversion de la parole en texte, vous construirez une application de chat multifacette qui prend en charge à la fois les interactions vocales et textuelles.

## Table des matières

* [Prérequis](#heading-prérequis)
    
* [Aperçu](#heading-aperçu)
    
* [Technologies principales](#heading-technologies-principales)
    
* [Guide d'implémentation du backend](#heading-guide-dimplémentation-du-backend)
    
    * [Installation du projet](#heading-installation-du-projet)
        
* [Guide d'implémentation du frontend](#heading-guide-dimplémentation-du-frontend)
    
    * [Installation du projet](#heading-installation-du-projet-1)
        
    * [Comprendre le composant App](#heading-comprendre-le-composant-app)
        
    * [Ajout de l'IA au canal](#heading-ajout-de-lia-au-canal)
        
    * [Configuration du ChannelHeader](#heading-configuration-du-channelheader)
        
    * [Ajout d'un indicateur d'état de l'IA](#heading-ajout-dun-indicateur-détat-de-lia)
        
    * [Construction de la fonctionnalité de reconnaissance vocale](#heading-construction-de-la-fonctionnalité-de-reconnaissance-vocale)
        
* [Flux de processus complet](#heading-flux-de-processus-complet)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* Un compte Stream avec une clé API et un secret (Lisez comment les obtenir [ici](https://getstream.io/blog/stream-getting-started-guide/))
    
* Accès à une API LLM (comme OpenAI, Anthropic).
    
* Node.js et npm/yarn installés.
    
* Connaissance de base de React et TypeScript.
    
* Navigateur moderne avec support de l'API WebSpeech (comme Chrome, Edge)
    

## Aperçu

Prenons un rapide aperçu de l'application que nous allons construire dans ce tutoriel. Ainsi, vous aurez une idée de ce qu'elle fait avant de plonger dans les détails.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749925010635/5228ae93-ff56-4b0f-8ea8-c7a160973191.gif align="center")

Si vous êtes maintenant excité, commençons tout de suite !

## Technologies principales

Cette application est alimentée par trois principaux acteurs : Stream Chat, l'API Web Speech et un backend Node.js + Express.

[Stream Chat](https://getstream.io/) est une plateforme qui vous aide à construire et intégrer facilement des expériences de chat et de messagerie riches et en temps réel dans vos applications. Il offre une variété de SDK (Software Development Kits) pour différentes plateformes (comme Android, iOS, React) et des composants d'interface utilisateur pré-construits pour rationaliser le développement. Sa robustesse et ses fonctionnalités de chat engageantes en font un excellent choix pour cette application - nous n'avons pas besoin de construire quoi que ce soit à partir de zéro.

[Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) est une norme de navigateur qui vous permet d'intégrer l'entrée et la sortie vocales dans vos applications, permettant des fonctionnalités comme la reconnaissance vocale (conversion de la parole en texte) et la synthèse vocale (conversion du texte en parole). Nous utiliserons la fonctionnalité de reconnaissance vocale dans ce projet.

Le backend Node.js + Express gère l'instantiation correcte de l'agent et traite les réponses conversationnelles générées par notre API LLM.

## Guide d'implémentation du backend

Commençons par notre backend, la salle des machines - où l'entrée de l'utilisateur est acheminée vers le modèle IA approprié, et une réponse traitée est retournée. Notre backend prend en charge plusieurs modèles IA, spécifiquement OpenAI et Anthropic.

### Installation du projet

1. Créez un dossier, appelez-le 'My-Chat-Application'.
    
2. Clonez ce [dépôt Github](https://github.com/GetStream/ai-assistant-nodejs.git)
    
3. Après le clonage, renommez le dossier en 'backend'
    
4. Ouvrez le fichier `.env.example` et fournissez les clés nécessaires (vous devrez fournir soit la clé OpenAI soit la clé Anthropic - la clé Open Weather est facultative).
    
5. Renommez le fichier `env.example` en `.env`
    
6. Installez les dépendances en exécutant cette commande :
    
    ```javascript
    npm install
    ```
    
7. Exécutez le projet en entrant cette commande :
    
    ```javascript
    npm start
    ```
    
    Votre backend devrait fonctionner sans problème sur `localhost:3000`.
    

## Guide d'implémentation du frontend

Cette section explore deux composants larges et interdépendants : la structure du chat et la reconnaissance vocale.

### Installation du projet

Nous allons créer et configurer notre projet React avec le SDK Stream Chat React. Nous utiliserons Vite avec le modèle TypeScript. Pour cela, naviguez vers votre dossier **My-Chat-Application**, ouvrez votre terminal et entrez cette commande :

```javascript
npm create vite frontend -- --template react-ts
cd chat-example
npm i stream-chat stream-chat-react
```

Avec notre projet frontend configuré, nous pouvons maintenant exécuter l'application :

```javascript
npm run dev
```

### Comprendre le composant App

L'objectif principal ici est d'initialiser un client de chat, de connecter un utilisateur, de créer un canal et de rendre l'interface de chat. Nous allons passer par tous ces processus étape par étape pour vous aider à mieux les comprendre :

#### Définir les constantes

Tout d'abord, nous devons fournir certaines informations d'identification importantes dont nous avons besoin pour la création d'utilisateurs et la configuration du client de chat. Vous pouvez trouver ces informations d'identification sur votre tableau de bord Stream [dashboard](https://dashboard.getstream.io/).

```javascript
const apiKey = "xxxxxxxxxxxxx";
const userId = "111111111";
const userName = "John Doe";
const userToken = "xxxxxxxxxx.xxxxxxxxxxxx.xx_xxxxxxx-xxxxx_xxxxxxxx"; // votre clé secrète stream
```

> Note : Ce sont des informations d'identification factices. Assurez-vous d'utiliser vos propres informations d'identification.

#### Créer un utilisateur

Ensuite, nous devons créer un objet utilisateur. Nous allons le créer en utilisant un ID, un nom et une URL d'avatar générée :

```javascript
const user: User = {
  id: userId,
  name: userName,
  image: `https://getstream.io/random_png/?name=${userName}`,
};
```

#### Configurer un client

Nous devons suivre l'état du canal de chat actif en utilisant le hook `useState` pour garantir une messagerie en temps réel sans faille dans cette application Stream Chat. Un hook personnalisé appelé `useCreateChatClient` initialise le client de chat avec une clé API, un jeton utilisateur et des données utilisateur :

```javascript
  const [channel, setChannel] = useState<StreamChannel>();
  const client = useCreateChatClient({
    apiKey,
    tokenOrProvider: userToken,
    userData: user,
  });
```

#### Initialiser le canal

Maintenant, nous initialisons un canal de messagerie pour permettre la communication en temps réel dans l'application Stream Chat. Lorsque le client de chat est prêt, le hook `useEffect` déclenche la création d'un canal de messagerie nommé `my_channel`, ajoutant l'utilisateur comme membre. Ce canal est ensuite stocké dans l'état du canal, garantissant que l'application est prête pour le rendu dynamique de la conversation.

```javascript
  useEffect(() => {
    if (!client) return;
    const channel = client.channel("messaging", "my_channel", {
      members: [userId],
    });

    setChannel(channel);
  }, [client]);
```

#### Rendre l'interface de chat

Avec toutes les parties intégrales de notre application de chat configurées, nous allons retourner un JSX pour définir la structure et les composants de l'interface de chat :

```javascript
 if (!client) return <div>Configuration du client et de la connexion...</div>;

  return (
    <Chat client={client}>
      <Channel channel={channel}>
        <Window>
          <MessageList />
          <MessageInput />
        </Window>
        <Thread />
      </Channel>
    </Chat>
  );
```

Dans cette structure JSX :

* Si le client n'est pas prêt, il affiche un message "Configuration du client et de la connexion...".
    
* Une fois le client prêt, il rend l'interface de chat en utilisant :
    
    * `<Chat>` : Enveloppe le contexte Stream Chat avec le client initialisé.
        
    * `<Channel>` : Définit le canal actif.
        
    * `<Window>` : Contient les principaux composants de l'interface utilisateur de chat :
        
        * `<MessageList>` : Affiche la liste des messages.
            
        * `<MessageInput>` : Utilise un `CustomMessageInput` personnalisé pour envoyer des messages.
            
    * `<Thread>` : Rend les réponses en fil de discussion.
        

Avec cela, nous avons configuré notre interface de chat et notre canal, et nous avons un client prêt. Voici à quoi ressemble notre interface jusqu'à présent :

![interface de chat stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1749901280964/4b788065-27ae-40b4-9882-c74bacef0fc4.png align="center")

### Ajout de l'IA au canal

Rappelez-vous, cette application de chat est conçue pour interagir avec une IA, donc nous devons pouvoir à la fois ajouter et supprimer l'IA du canal. Sur l'interface utilisateur, nous allons ajouter un bouton dans l'en-tête du canal pour permettre aux utilisateurs d'ajouter et de supprimer l'IA. Mais nous devons encore déterminer si nous l'avons déjà dans le canal pour savoir quelle option afficher.

Pour cela, nous allons créer un hook personnalisé appelé `useWatchers`. Il surveille la présence de l'IA en utilisant un concept appelé `watchers` :

```javascript
import { useCallback, useEffect, useState } from 'react';
import { Channel } from 'stream-chat';

export const useWatchers = ({ channel }: { channel: Channel }) => {
  const [watchers, setWatchers] = useState<string[]>([]);
  const [error, setError] = useState<Error | null>(null);

  const queryWatchers = useCallback(async () => {
    setError(null);

    try {
      const result = await channel.query({ watchers: { limit: 5, offset: 0 } });
      setWatchers(result?.watchers?.map((watcher) => watcher.id).filter((id): id is string => id !== undefined) || [])
      return;
    } catch (err) {
      setError(err as Error);
    }
  }, [channel]);

  useEffect(() => {
    queryWatchers();
  }, [queryWatchers]);

  useEffect(() => {
    const watchingStartListener = channel.on('user.watching.start', (event) => {
      const userId = event?.user?.id;
      if (userId && userId.startsWith('ai-bot')) {
        setWatchers((prevWatchers) => [
          userId,
          ...(prevWatchers || []).filter((watcherId) => watcherId !== userId),
        ]);
      }
    });

    const watchingStopListener = channel.on('user.watching.stop', (event) => {
      const userId = event?.user?.id;
      if (userId && userId.startsWith('ai-bot')) {
        setWatchers((prevWatchers) =>
          (prevWatchers || []).filter((watcherId) => watcherId !== userId)
        );
      }
    });

    return () => {
      watchingStartListener.unsubscribe();
      watchingStopListener.unsubscribe();
    };
  }, [channel]);

  return { watchers, error };
};
```

### Configuration du ChannelHeader

Nous pouvons maintenant construire un nouveau composant d'en-tête de canal en utilisant le hook `useChannelStateContext` pour accéder au canal et initialiser le hook personnalisé `useWatchers`. En utilisant les données des observateurs, nous définissons une variable `aiInChannel` pour afficher le texte pertinent. En fonction de cette variable, nous invoquons soit le point de terminaison `start-ai-agent` soit `stop-ai-agent` sur le backend Node.js.

```javascript
import { useChannelStateContext } from 'stream-chat-react';
import { useWatchers } from './useWatchers';

export default function ChannelHeader() {
  const { channel } = useChannelStateContext();
  const { watchers } = useWatchers({ channel });

  const aiInChannel =
    (watchers ?? []).filter((watcher) => watcher.includes('ai-bot')).length > 0;
  return (
    <div className='my-channel-header'>
      <h2>{(channel?.data as { name?: string })?.name ?? 'Chat IA vocale et textuelle'}</h2>
      <button onClick={addOrRemoveAgent}>
        {aiInChannel ? 'Retirer l\'IA' : 'Ajouter l\'IA'}
      </button>
    </div>
  );

  async function addOrRemoveAgent() {
    if (!channel) return;
    const endpoint = aiInChannel ? 'stop-ai-agent' : 'start-ai-agent';
    await fetch(`http://127.0.0.1:3000/${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ channel_id: channel.id, platform: 'openai' }),
    });
  }
}
```

### Ajout d'un indicateur d'état de l'IA

Les IA prennent un peu de temps pour traiter les informations, donc pendant que l'IA traite, nous ajoutons un indicateur pour refléter son statut. Nous créons un `AIStateIndicator` qui fait cela pour nous :

```javascript
import { AIState } from 'stream-chat';
import { useAIState, useChannelStateContext } from 'stream-chat-react';

export default function MyAIStateIndicator() {
  const { channel } = useChannelStateContext();
  const { aiState } = useAIState(channel);
  const text = textForState(aiState);
  return text && <p className='my-ai-state-indicator'>{text}</p>;

  function textForState(aiState: AIState): string {
    switch (aiState) {
      case 'AI_STATE_ERROR':
        return 'Quelque chose s\'est mal passé...';
      case 'AI_STATE_CHECKING_SOURCES':
        return 'Vérification des ressources externes...';
      case 'AI_STATE_THINKING':
        return "Je réfléchis actuellement...";
      case 'AI_STATE_GENERATING':
        return 'Génération d\'une réponse pour vous...';
      default:
        return '';
    }
  }
}
```

### Construction de la fonctionnalité de reconnaissance vocale

Jusqu'à présent, nous avons une application de chat fonctionnelle qui envoie des messages et reçoit des commentaires d'une IA. Maintenant, nous voulons activer l'interaction vocale, permettant aux utilisateurs de parler à l'IA au lieu de taper manuellement.

Pour y parvenir, nous allons configurer la fonctionnalité de reconnaissance vocale dans un composant `CustomMessageInput`. Passons en revue l'ensemble du processus, étape par étape, pour comprendre comment y parvenir.

#### Configuration initiale des états

Lorsque le composant `CustomMessageInput` est monté pour la première fois, il commence par établir sa structure d'état fondamentale :

```javascript
  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [isRecognitionReady, setIsRecognitionReady] = useState<boolean>(false);
  const recognitionRef = useRef<any>(null);
  const isManualStopRef = useRef<boolean>(false);
  const currentTranscriptRef = useRef<string>("");
```

Cette étape d'initialisation est cruciale car elle établit la capacité du composant à suivre plusieurs états concurrents : si l'enregistrement est actif, si l'API de reconnaissance vocale est prête, et divers mécanismes de persistance pour gérer le cycle de vie de la reconnaissance vocale.

#### Intégration du contexte

Dans Stream Chat, le `MessageInputContext` est établi dans le composant `MessageInput`. Il fournit des données au composant d'interface utilisateur Input et à ses enfants. Puisque nous voulons utiliser les valeurs stockées dans le `MessageInputContext` pour construire notre propre composant d'interface utilisateur d'entrée personnalisé, nous allons appeler le hook personnalisé `useMessageInputContext` :

```javascript
  // Accéder au contexte MessageInput
  const { handleSubmit, textareaRef } = useMessageInputContext();
```

Cette étape garantit que la fonctionnalité d'entrée vocale s'intègre de manière transparente avec l'infrastructure de chat existante, partageant la même référence `textarea` et les mécanismes de soumission que les autres méthodes d'entrée utilisent.

#### Détection et initialisation de l'API Web Speech

L'API Web Speech n'est pas prise en charge par certains navigateurs, c'est pourquoi nous devons vérifier si le navigateur exécutant cette application est compatible. Le premier processus majeur du composant implique la détection et l'initialisation de l'API Web Speech :

```javascript
 const SpeechRecognition = (window as any).SpeechRecognition||(window as any).webkitSpeechRecognition;
```

Une fois l'API détectée, le composant configure le service de reconnaissance vocale avec des paramètres optimaux.

#### Configuration des gestionnaires d'événements

Nous aurons deux gestionnaires d'événements : le gestionnaire de traitement des résultats et le gestionnaire d'événements de cycle de vie.

Le gestionnaire de traitement des résultats traite la sortie de la reconnaissance vocale. Il démontre une approche de traitement en deux phases où les résultats intermédiaires fournissent un retour immédiat tandis que les résultats finaux sont accumulés pour la précision.

```javascript
      recognition.onresult = (event: any) => {
        let finalTranscript = "";
        let interimTranscript = "";

        // Traiter tous les résultats à partir du dernier index traité
        for (let i = event.resultIndex; i < event.results.length; i++) {
          const transcriptSegment = event.results[i][0].transcript;
          if (event.results[i].isFinal) {
            finalTranscript += transcriptSegment + " ";
          } else {
            interimTranscript += transcriptSegment;
          }
        }

        // Mettre à jour la transcription actuelle
        if (finalTranscript) {
          currentTranscriptRef.current += finalTranscript;
        }

        // Combiner la transcription finale stockée avec les résultats intermédiaires actuels
        const combinedTranscript = (currentTranscriptRef.current + interimTranscript).trim();
        
        // Mettre à jour le textarea
        if (combinedTranscript) {
          updateTextareaValue(combinedTranscript);
        }
      };
```

Le gestionnaire d'événements de cycle de vie garantit que le composant répond de manière appropriée à chaque phase des événements de cycle de vie de la reconnaissance vocale (`onstart`, `onend` et `onerror`) :

```javascript
      recognition.onstart = () => {
        console.log("La reconnaissance vocale a commencé");
        setIsRecording(true);
        currentTranscriptRef.current = ""; // Réinitialiser la transcription au démarrage
      };

      recognition.onend = () => {
        console.log("La reconnaissance vocale s'est terminée");
        setIsRecording(false);
        
        // Si ce n'était pas un arrêt manuel et que nous devons encore enregistrer, redémarrer
        if (!isManualStopRef.current && isRecording) {
          try {
            recognition.start();
          } catch (error) {
            console.error("Erreur de redémarrage de la reconnaissance :", error);
          }
        }
        
        isManualStopRef.current = false;
      };

      recognition.onerror = (event: any) => {
        console.error("Erreur de reconnaissance vocale :", event.error);
        setIsRecording(false);
        isManualStopRef.current = false;

        switch (event.error) {
          case "no-speech":
            console.warn("Aucune parole détectée");
            // Ne pas afficher d'alerte pour l'absence de parole, simplement la journaliser
            break;
          case "not-allowed":
            alert(
              "Accès au microphone refusé. Veuillez autoriser les permissions du microphone.",
            );
            break;
          case "network":
            alert("Une erreur réseau s'est produite. Veuillez vérifier votre connexion.");
            break;
          case "aborted":
            console.log("Reconnaissance vocale abandonnée");
            break;
          default:
            console.error("Erreur de reconnaissance vocale :", event.error);
        }
      };

      recognitionRef.current = recognition;
      setIsRecognitionReady(true);
      } else {
      console.warn("L'API Web Speech n'est pas prise en charge dans ce navigateur.");
      setIsRecognitionReady(false);
      }
```

#### Démarrage de l'entrée vocale

Lorsque l'utilisateur clique sur le bouton du microphone, le composant initie un processus en plusieurs étapes qui implique la demande de permissions pour le microphone et la gestion claire des erreurs si les utilisateurs refusent l'accès.

```javascript
 const toggleRecording = async (): Promise<void> => {
    if (!recognitionRef.current) {
      alert("La reconnaissance vocale n'est pas disponible");
      return;
    }

    if (isRecording) {
      // Arrêter l'enregistrement
      isManualStopRef.current = true;
      recognitionRef.current.stop();
    } else {
      try {
        // Demander la permission du microphone
        await navigator.mediaDevices.getUserMedia({ audio: true });

        // Effacer le texte actuel et réinitialiser la transcription avant de commencer
        currentTranscriptRef.current = "";
        updateTextareaValue("");

        // Démarrer la reconnaissance
        recognitionRef.current.start();
      } catch (error) {
        console.error("Erreur d'accès au microphone :", error);
        alert(
          "Impossible d'accéder au microphone. Veuillez vérifier les permissions et réessayer.",
        );
      }
    }
  };
```

#### Réinitialisation de l'état et démarrage de la reconnaissance

Avant de commencer la reconnaissance vocale, le composant réinitialise son état interne. Cette réinitialisation garantit que chaque nouvelle session d'entrée vocale commence avec une ardoise propre, empêchant les interférences des sessions précédentes.

```javascript
currentTranscriptRef.current = "";
updateTextareaValue("");
recognitionRef.current.start();
```

#### Traitement de la parole en temps réel

Deux choses se produisent simultanément pendant ce processus :

1. **Traitement continu des résultats :** Alors que l'utilisateur parle, le composant traite en continu les données vocales entrantes via un pipeline sophistiqué :
    
    * Chaque segment de parole est classé comme intermédiaire (temporaire) ou final (confirmé).
        
    * Les résultats finaux sont accumulés dans la référence de transcription persistante.
        
    * Les résultats intermédiaires sont combinés avec les résultats finaux accumulés pour un affichage immédiat.
        
2. **Mises à jour dynamiques du Textarea :** Le composant met à jour le `textarea` en temps réel en utilisant une approche de manipulation DOM personnalisée :
    
    ```javascript
    const updateTextareaValue = (value: string) => {
      const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
        window.HTMLTextAreaElement.prototype,
        'value'
      )?.set;
      
      if (nativeInputValueSetter) {
        nativeInputValueSetter.call(textareaRef.current, value);
        const inputEvent = new Event('input', { bubbles: true });
        textareaRef.current.dispatchEvent(inputEvent);
      }
    };
    ```
    
    Cette étape implique de contourner le comportement conventionnel des composants contrôlés de React pour fournir un retour immédiat, tout en maintenant la compatibilité avec le système d'événements de React.
    

#### Retour d'information de l'interface utilisateur

Pour rendre les interactions vocales plus fluides pour les utilisateurs, nous allons ajouter quelques fonctionnalités de retour visuel. Celles-ci incluent :

1. **Basculer entre les icônes de micro et d'arrêt**
    
    Nous affichons une icône de microphone lorsque le système est inactif et une icône d'arrêt lorsque l'enregistrement est actif. Cela fournit une indication claire de l'état de l'enregistrement.
    
    ```javascript
    <button
      className={`voice-input-button ${isRecording ? 'recording' : 'idle'}`}
      title={isRecording ? "Arrêter l'enregistrement" : "Démarrer l'entrée vocale"}
    >
      {isRecording ? (
        <Square size={20} className="voice-icon recording-icon" />
      ) : (
        <Mic size={20} className="voice-icon idle-icon" />
      )}
    </button>
    ```
    
2. **Bannière de notification d'enregistrement**
    
    Une bannière de notification apparaît en haut de l'écran pour indiquer que l'enregistrement vocal est en cours. Cette notification garantit que les utilisateurs sont conscients lorsque le microphone est actif, répondant aux préoccupations de confidentialité et d'utilisabilité.
    
    ```javascript
    {isRecording && (
      <div className="recording-notification show">
        <span className="recording-icon">🎤</span>
        Enregistrement... Cliquez sur arrêter lorsque vous avez terminé
      </div>
    )}
    ```
    

#### Intégration et soumission des messages

Le texte transcrit s'intègre de manière transparente avec le système de chat existant via la référence `textarea` partagée et le gestionnaire de soumission fourni par le contexte :

```javascript
<SendButton sendMessage={handleSubmit} />
```

Cette intégration signifie que les messages générés par la voix suivent le même chemin de soumission que les messages tapés, maintenant la cohérence avec le comportement du système de chat. Après la soumission du message, le composant garantit un nettoyage approprié de son état interne, se préparant pour la prochaine session d'entrée vocale.

#### Passage du composant CustomMessageInput

Ayant construit notre composant d'entrée de messagerie personnalisé, nous allons maintenant le passer à la prop `Input` du composant `MessageInput` dans notre `App.tsx` :

```javascript
<MessageInput Input={CustomMessageInput} />
```

## **Flux de processus complet**

Voici comment fonctionne l'application :

1. Après le montage du composant, vous ajoutez l'IA au chat en cliquant sur le bouton **Ajouter l'IA**.
    
2. Cliquez sur l'**icône du micro** pour commencer l'enregistrement.
    
3. Votre navigateur demandera la permission d'utiliser le microphone.
    
4. Si vous **refusez** la permission, l'enregistrement ne commencera pas.
    
5. Si vous **autorisez** la permission, l'enregistrement et la transcription commencent simultanément.
    
6. Cliquez sur l'**icône d'arrêt (carré)** pour terminer l'enregistrement.
    
7. Cliquez sur le **bouton d'envoi** pour soumettre votre message.
    
8. L'IA traite votre entrée et génère une réponse.
    
## Conclusion

Dans ce tutoriel, vous avez appris à construire un puissant chatbot conversationnel en utilisant Stream Chat et React. L'application prend en charge à la fois les entrées textuelles et vocales.

Si vous souhaitez créer vos propres expériences de chat engageantes, vous pouvez explorer les fonctionnalités Stream [Chat](https://getstream.io/chat/) et [Video](https://getstream.io/video/) pour faire passer vos projets au niveau supérieur.

Obtenez le code source complet de ce projet [ici](https://github.com/TimothyOlanrewaju/My-Chat-Application). Si vous avez aimé lire cet article, connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750) ou suivez-moi sur [X](https://x.com/SmoothTee_DC) pour plus de publications et d'articles liés à la programmation.

À la prochaine !