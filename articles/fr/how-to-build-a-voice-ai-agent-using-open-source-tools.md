---
title: Comment créer un agent IA vocal à l'aide d'outils open-source
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2025-10-21T19:01:36.836Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-voice-ai-agent-using-open-source-tools
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761073279608/a73ce2cd-c95e-4f8b-b529-8774ce39a43f.png
tags:
- name: AI
  slug: ai
- name: education
  slug: education
- name: stem
  slug: stem
- name: Voice
  slug: voice
- name: agentic AI
  slug: agentic-ai
- name: Open Source
  slug: opensource
- name: Rust
  slug: rust
seo_title: Comment créer un agent IA vocal à l'aide d'outils open-source
seo_desc: 'Voice is the next frontier of conversational AI. It is the most natural
  modality for people to chat and interact with another intelligent being.

  In the past year, frontier AI labs such as OpenAI, xAI, Anthropic, Meta, and Google
  have all released rea...'
---

La voix est la prochaine frontière de l'IA conversationnelle. C'est la modalité la plus naturelle pour que les gens discutent et interagissent avec un autre être intelligent.

Au cours de l'année écoulée, les laboratoires d'IA de pointe tels qu'OpenAI, xAI, Anthropic, Meta et Google ont tous publié des services vocaux en temps réel. Pourtant, les applications vocales ont également les exigences les plus élevées en matière de latence, de confidentialité et de personnalisation. Il est difficile d'avoir une solution d'IA vocale universelle.

Dans cet article, nous explorerons comment utiliser les technologies open-source pour créer des [agents IA vocaux](https://echokit.dev/) qui utilisent votre base de connaissances personnalisée, votre style de voix, vos actions, vos modèles d'IA affinés, et qui s'exécutent sur votre propre ordinateur.

## Ce que nous allons aborder :

* [Prérequis](#heading-prerequis)
    
* [À quoi cela ressemble](#heading-a-quoi-cela-ressemble)
    
* [Deux approches de l'IA vocale](#heading-deux-approches-de-lia-vocale)
    
* [L'orchestrateur d'IA vocale](#heading-lorchestrateur-dia-vocale)
    
    * [Configurer un ASR](#heading-configurer-un-asr)
        
    * [Exécuter et configurer un VAD](#heading-executer-et-configurer-un-vad)
        
    * [Configurer un LLM](#heading-configurer-un-llm)
        
    * [Configurer un TTS](#heading-configurer-un-tts)
        
    * [Configurer le MCP et les actions](#heading-configurer-le-mcp-et-les-actions)
        
* [IA locale avec LlamaEdge](#heading-ia-locale-avec-llamaedge)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Vous devrez posséder et connaître quelques éléments pour suivre ce tutoriel le plus efficacement possible :

* Accès à un système de type Linux. Mac ou Windows WSL suffisent également.
    
* Être à l'aise avec les outils en ligne de commande (CLI).
    
* Être capable d'exécuter des applications serveurs sur le système Linux.
    
* Avoir/obtenir des clés API gratuites de [Groq](https://console.groq.com/keys) et [ElevenLabs](https://elevenlabs.io/app/sign-in?redirect=%2Fapp%2Fdevelopers%2Fapi-keys).
    
* Facultatif : être capable de compiler et de construire du code source Rust.
    
* Facultatif : avoir/obtenir un [appareil EchoKit](https://echokit.dev/echokit_diy.html) ou assembler le vôtre.
    

## À quoi cela ressemble

Le composant logiciel clé que nous allons couvrir est le projet [echokit\_server](https://github.com/second-state/echokit_server). Il s'agit d'un orchestrateur d'agents open-source pour les applications d'IA vocale. Cela signifie qu'il coordonne des services tels que les LLM, ASR, TTS, VAD, MCP, la recherche, les bases de données de connaissances/vectorielles, et d'autres pour générer des réponses vocales intelligentes à partir des invites de l'utilisateur.

Le serveur EchoKit fournit une interface WebSocket qui permet aux clients compatibles d'envoyer et de recevoir des données vocales. Le projet [echokit\_box](https://github.com/second-state/echokit_box) fournit un firmware basé sur ESP32 qui peut agir comme un client pour collecter l'audio de l'utilisateur et lire la voix générée par TTS depuis le serveur EchoKit. Vous pouvez voir quelques démos ici. Vous pouvez assembler votre propre appareil EchoKit ou [en acheter un](https://echokit.dev/echokit_diy.html).

%[https://youtu.be/XroT7a0DLkw] 

%[https://youtu.be/Zy-rLT4EgZQ] 

Bien sûr, vous pouvez également utiliser un client purement logiciel conforme à l'interface WebSocket de [echokit\_server](https://github.com/second-state/echokit_server). Le projet publie une [page web JavaScript](https://echokit.dev/chat/) que vous pouvez exécuter localement pour vous connecter à votre propre serveur EchoKit comme référence.

%[https://youtu.be/Eyd9ToflccY] 

Dans le reste de l'article, je discuterai de la manière dont il est implémenté et de la manière de déployer le système pour vos propres applications d'IA vocale.

## Deux approches de l'IA vocale

Lorsqu'OpenAI a publié ses services de « voix en temps réel » en octobre 2024, le consensus était que l'IA vocale nécessitait des modèles d'IA « de bout en bout ». Les LLM traditionnels prennent du texte en entrée puis répondent en texte. Les modèles vocaux de bout en bout prennent des données audio vocales en entrée et répondent également en données audio vocales. Les modèles de bout en bout pourraient réduire la latence puisque le traitement, la compréhension et la génération de la voix sont effectués en une seule étape.

Mais un modèle de bout en bout est très difficile à personnaliser. Par exemple, il est impossible d'ajouter votre propre invite (prompt) et vos connaissances au contexte pour chaque requête LLM, ou d'agir sur le raisonnement du LLM ou les réponses d'appel d'outils, ou de cloner votre propre voix pour la réponse.

La deuxième approche consiste à utiliser un service d'« orchestration d'agents » pour lier plusieurs modèles d'IA, en utilisant la sortie d'un modèle comme entrée pour le modèle suivant. Cela nous permet de personnaliser ou de sélectionner chaque modèle et de manipuler ou de compléter l'entrée du modèle à chaque étape.

* Le modèle VAD est utilisé pour détecter les tours de parole dans le discours de l'utilisateur. Il détermine quand l'utilisateur a fini de parler et attend maintenant une réponse.
    
* Le modèle ASR/STT transforme la parole de l'utilisateur en texte.
    
* Le modèle LLM génère une réponse textuelle, y compris les appels d'outils MCP.
    
* Le modèle TTS transforme le texte de réponse en voix.
    

Le problème avec l'orchestration multi-modèles et multi-étapes est qu'elle peut être lente. De nombreuses optimisations sont nécessaires pour que cette approche fonctionne bien. Par exemple, une technique utile consiste à utiliser l'entrée et la sortie en streaming partout où cela est possible. De cette façon, chaque modèle n'a pas à attendre la réponse complète du modèle en amont.

Le [serveur EchoKit](https://github.com/second-state/echokit_server) est un orchestrateur de modèles d'IA hautement efficace, où tout est en streaming. Il est entièrement écrit en Rust pour la stabilité, la sécurité et la rapidité.

## L'orchestrateur d'IA vocale

Le projet de serveur EchoKit est un orchestrateur de services d'IA open-source axé sur les cas d'utilisation vocale en temps réel. Il démarre un serveur WebSocket qui écoute l'entrée audio en streaming et renvoie des réponses audio en streaming.

Vous pouvez construire le projet [echokit\_server](https://github.com/second-state/echokit_server) vous-même en utilisant la chaîne d'outils Rust. Ou, vous pouvez simplement télécharger le binaire pré-construit pour votre ordinateur.

```bash
# pour les processeurs x86 / AMD64
curl -LO https://github.com/second-state/echokit_server/releases/download/v0.1.0/echokit_server-v0.1.0-x86_64-unknown-linux-gnu.tar.gz
unzip echokit_server-v0.1.0-x86_64-unknown-linux-gnu.tar.gz

# pour les processeurs arm64
curl -LO https://github.com/second-state/echokit_server/releases/download/v0.1.0/echokit_server-v0.1.0-aarch64-unknown-linux-gnu.tar.gz
unzip echokit_server-v0.1.0-aarch64-unknown-linux-gnu.tar.gz
```

Ensuite, exécutez-le comme suit :

```bash
nohup ./echokit_server &
```

Il lit le fichier `config.toml` du répertoire courant. En haut du fichier, vous pouvez configurer le port sur lequel le serveur WebSocket écoute. Vous pouvez également spécifier un fichier WAV qui est téléchargé sur l'[appareil client EchoKit](https://echokit.dev/echokit_diy.html) connecté en tant que message de bienvenue.

```ini
addr = "0.0.0.0:8000"
hello_wav = "hello.wav"
```

### Configurer un ASR

Lorsque le serveur EchoKit reçoit les données vocales de l'utilisateur, il envoie d'abord les données à un service ASR pour les convertir en texte.

Il existe aujourd'hui de nombreux modèles ASR convaincants. Le serveur EchoKit peut fonctionner avec n'importe quel fournisseur d'API compatible OpenAI, tel qu'OpenAI lui-même, x.ai, OpenRouter et Groq.

Dans notre exemple, nous utilisons le service Whisper ASR de Groq. Whisper est un modèle ASR de pointe publié par OpenAI. Groq fournit des puces matérielles spécialisées pour l'exécuter très rapidement. Vous devrez d'abord obtenir [une clé API gratuite de Groq](https://console.groq.com/keys). Ensuite, configurez le service ASR comme suit. Notez le « prompt » pour le modèle Whisper. C'est une invite éprouvée pour réduire les hallucinations du modèle Whisper.

```ini
[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
api_key = "gsk_XYZ"
model = "whisper-large-v3"
lang = "en"
prompt = "Hello\n你好\n(noise)\n(bgm)\n(silence)\n"
```

### Exécuter et configurer un VAD

Afin de mener une conversation vocale, les participants doivent détecter les intentions de l'autre et ne parler que lorsqu'un tour se présente. Le VAD (Voice Activity Detection) est un modèle d'IA spécialisé utilisé pour détecter les activités et, en particulier, quand l'interlocuteur a fini et attend une réponse.

Dans EchoKit, nous avons une détection VAD à la fois sur l'appareil et sur le serveur.

* VAD côté appareil : Il détecte le langage humain. L'appareil ignore le bruit de fond, la musique, les sons de clavier et les aboiements de chien. Il n'envoie que la voix humaine au serveur.
    
* VAD côté serveur : Il traite le flux audio par morceaux de 100 ms (0,1 s). Une fois qu'il détecte que l'interlocuteur a fini, il envoie tout le texte transcrit au LLM et commence à attendre le flux de réponse du LLM.
    

Le VAD côté serveur est facultatif, car le VAD côté appareil peut également générer des signaux de « tour de conversation ». Mais en raison des ressources informatiques limitées sur l'appareil, l'ajout du VAD côté serveur peut considérablement améliorer les performances globales du VAD.

Nous portons le projet populaire [Silero VAD](https://github.com/snakers4/silero-vad) de Python vers Rust, et créons le projet [silero\_vad\_server](https://github.com/second-state/silero_vad_server). Construisez le projet [comme indiqué](https://github.com/second-state/silero_vad_server?tab=readme-ov-file#build-the-api-server). Vous pouvez démarrer le serveur VAD sur le port 9094 de votre serveur EchoKit comme suit :

```bash
VAD_LISTEN=0.0.0.0:9094 nohup target/release/silero_vad_server &
```

Vous vous demandez peut-être : pourquoi porter vers Rust ? Alors que de nombreux projets d'IA sont écrits en Python pour la facilité de développement, les applications Rust sont souvent beaucoup plus légères, rapides et sûres lors du déploiement. Nous allons donc exploiter des outils d'IA comme [RustCoder](https://github.com/cardea-mcp/RustCoder) pour porter autant de code Python que possible vers Rust. La pile logicielle EchoKit est largement écrite en Rust.

Le serveur VAD est un service WebSocket qui écoute sur le port 9094. Comme nous l'avons vu, le serveur EchoKit diffusera l'audio vers ce WebSocket et arrêtera l'ASR lorsqu'un tour de conversation est détecté. Par conséquent, nous ajouterons le service VAD à la section de configuration ASR du serveur EchoKit dans `config.toml`.

```ini
[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
api_key = "gsk_XYZ"
model = "whisper-large-v3"
lang = "en"
prompt = "Hello\n你好\n(noise)\n(bgm)\n(silence)\n"
vad_realtime_url = "ws://localhost:9094/v1/audio/realtime_vad"
```

### Configurer un LLM

Une fois que le service ASR a transcrit la voix de l'utilisateur en texte, l'étape suivante du pipeline est le LLM (Large Language Model). C'est le service d'IA qui « réfléchit » réellement et génère une réponse en texte.

Encore une fois, le serveur EchoKit peut fonctionner avec n'importe quel fournisseur d'API compatible OpenAI pour les LLM, tel qu'OpenAI lui-même, x.ai, OpenRouter et Groq. Comme le service vocal est très sensible à la vitesse, nous choisirons à nouveau Groq. Groq prend en charge un certain nombre de LLM open-source. Nous choisirons le modèle `gpt-oss-20b` publié par OpenAI.

```ini
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "gsk_XYZ"
model = "openai/gpt-oss-20b"
history = 20 
```

Le champ « history » indique combien de messages doivent être conservés dans le contexte. Une autre caractéristique cruciale d'une application LLM est l'« invite système » (system prompt), où vous indiquez au LLM comment il doit se « comporter ». Vous pouvez également spécifier l'invite système dans la configuration du serveur EchoKit.

```ini
[[llm.sys_prompts]]
role = "system"
content = """
Vous êtes un comédien. Engagez une conversation légère et humoristique avec l'utilisateur. Racontez des blagues quand c'est approprié.
 
"""
```

Comme Groq est très rapide, il peut traiter de très grandes invites système en moins d'une seconde. Vous pouvez ajouter beaucoup plus de contexte et d'instructions à l'invite système. Par exemple, vous pouvez donner à l'application des « connaissances » sur un domaine spécifique en mettant des livres entiers dans l'invite système.

### Configurer un TTS

Enfin, une fois que le LLM génère une réponse textuelle, le serveur EchoKit appellera un service TTS (text to speech) pour convertir le texte en voix et le diffuser en streaming vers l'appareil client.

Bien que Groq dispose d'un service TTS, il n'est pas particulièrement convaincant. ElevenLabs est un fournisseur de TTS de premier plan qui propose des centaines de personnages vocaux. Il peut exprimer des émotions et prend en charge le clonage vocal facile. Dans la configuration ci-dessous, vous mettrez votre [clé API ElevenLabs](https://elevenlabs.io/app/sign-in?redirect=%2Fapp%2Fdevelopers%2Fapi-keys) et sélectionnerez une voix.

```ini
[tts]
platform = "Elevenlabs"
token = "sk_xyz"
voice = "VOICE-ID-ABCD"
```

Les modèles TTS et les services API d'ElevenLabs sont tous excellents, mais ils ne sont pas open-source. Un TTS open-source très convaincant, connu sous le nom de GPT-SoVITS, est également disponible.

Vous pouvez porter GPT-SoVITS de Python vers Rust et créer un projet de serveur API open-source appelé [gsv\_tts](https://github.com/second-state/gsv_tts). Il permet un clonage facile de n'importe quelle voix. Vous pouvez exécuter un serveur API [gsv\_tts](https://github.com/second-state/gsv_tts) en suivant ses instructions. Ensuite, vous pouvez configurer le serveur EchoKit pour lui envoyer du texte en streaming et recevoir de l'audio en streaming de sa part.

```ini
[tts]
platform = "StreamGSV"
url = "http://gsv_tts.server:port/v1/audio/stream_speech"
speaker = "michael"
```

### Configurer le MCP et les actions

Bien sûr, un « agent IA » ne se résume pas à discuter. Il s'agit d'effectuer des actions sur des tâches spécifiques. Par exemple, le cas d'utilisation de [« préparation au test de citoyenneté américaine »](https://www.youtube.com/watch?v=Zy-rLT4EgZQ), que j'ai partagé en exemple vidéo au début de cet article, nécessite que l'agent récupère des questions d'examen dans une base de données, puis génère des réponses qui guident l'utilisateur vers la réponse officielle. Ceci est accompli à l'aide d'outils et d'actions LLM.

* Le LLM détecte que l'utilisateur demande une nouvelle question.
    
* Au lieu de répondre en langage naturel, il répond avec une structure JSON qui ordonne à l'agent de « récupérer une nouvelle question et sa réponse ».
    
* Le serveur EchoKit intercepte cette réponse JSON et récupère la question et la réponse dans une base de données.
    
* Le serveur EchoKit renvoie la question et la réponse au LLM.
    
* Le LLM formule une réponse en langage naturel basée sur la question et la réponse.
    
* Le serveur EchoKit génère une réponse vocale à l'aide de son service TTS.
    

Comme vous pouvez le voir, le serveur EchoKit doit effectuer quelques étapes supplémentaires en coulisses avant de répondre vocalement. Le serveur EchoKit exploite le protocole MCP pour cela. La fonction de recherche de questions et de réponses est fournie par un serveur MCP open-source appelé [ExamPrepAgent](https://github.com/cardea-mcp/ExamPrepAgent).

Le protocole MCP standardise les outils et les fonctions que les LLM peuvent appeler. Il existe de nombreux serveurs MCP disponibles pour toutes sortes de tâches différentes. ExamPrepAgent n'est que l'un d'entre eux.

Nous exécutons ce serveur MCP sur le port 8003. Avec le serveur MCP opérationnel, il vous suffit d'ajouter la configuration suivante au fichier `config.toml` du serveur EchoKit.

```ini
[[llm.mcp_server]]
server = "http://localhost:8003/mcp"
type = "http_streamable" 
```

Avec l'intégration MCP, l'agent IA EchoKit peut désormais effectuer des actions. Il peut appeler des API pour envoyer des messages, effectuer des paiements ou même allumer ou éteindre des appareils électroniques.

## IA locale avec LlamaEdge

Vous avez maintenant vu l'appareil EchoKit open-source fonctionner avec le serveur EchoKit open-source pour comprendre et répondre aux utilisateurs par la voix. Mais les modèles d'IA que nous utilisons, bien qu'également open-source, s'exécutent sur des fournisseurs de cloud commerciaux. Pouvons-nous exécuter des modèles d'IA à l'aide de technologies open-source à la maison ?

[LlamaEdge](https://github.com/LlamaEdge/LlamaEdge) est un serveur API open-source et multiplateforme pour les modèles d'IA. Il [prend en charge de nombreux modèles LLM, ASR et TTS grand public](https://llamaedge.com/docs/ai-models/) sur Linux, Mac, Windows et de nombreuses architectures CPU/GPU. Il est parfait pour exécuter des modèles d'IA sur des ordinateurs personnels ou de bureau. Il fournit également des points de terminaison API compatibles OpenAI, ce qui les rend très faciles à intégrer dans le serveur EchoKit.

Pour installer LlamaEdge et ses dépendances, exécutez la commande shell suivante. Elle détectera votre matériel et installera le logiciel approprié capable de tirer pleinement parti de vos GPU (le cas échéant).

```bash
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install_v2.sh | bash -s
```

Ensuite, téléchargez un modèle LLM open-source. J'utilise le modèle Gemma de Google comme exemple.

```bash
curl -LO https://huggingface.co/second-state/gemma-3-4b-it-GGUF/resolve/main/gemma-3-4b-it-Q5_K_M.gguf
```

Téléchargez le serveur API LlamaEdge multiplateforme.

```bash
curl -LO https://github.com/second-state/LlamaEdge/releases/latest/download/llama-api-server.wasm
```

Démarrez un serveur API LlamaEdge avec le modèle LLM Google Gemma. Par défaut, il écoute sur le port localhost 8080.

```bash
wasmedge --dir .:. --nn-preload default:GGML:AUTO:gemma-3-4b-it-Q5_K_M.gguf llama-api-server.wasm -p gemma-3
```

Testez l'API compatible OpenAI sur ce serveur.

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"system", "content": "Vous êtes un assistant utile. Essayez d'être aussi bref que possible."}, {"role":"user", "content": "Où se trouve la capitale du Texas ?"}]}'
```

Maintenant, vous pouvez ajouter ce service LLM local à la configuration de votre serveur EchoKit.

```ini
[llm]
llm_chat_url = "http://localhost:8080/v1/chat/completions"
api_key = "NONE"
model = "default"
history = 20 
```

Le projet LlamaEdge prend en charge plus que les LLM. Il exécute également le [modèle Whisper ASR](https://github.com/LlamaEdge/whisper-api-server) et le [modèle Piper TTS](https://github.com/LlamaEdge/tts-api-server) en tant que serveurs API compatibles OpenAI.

## Conclusion

La pile logicielle des agents IA vocaux est complexe et profonde. EchoKit est une plateforme open-source qui lie et coordonne tous ces composants. Elle offre un bon point d'observation pour nous permettre d'en apprendre davantage sur l'ensemble de la pile.

J'ai hâte de voir ce que vous allez construire !