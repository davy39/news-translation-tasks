---
title: 'Comment créer votre propre assistant vocal privé : un guide étape par étape
  utilisant des outils open-source'
subtitle: ''
author: Surya Teja Appini
co_authors: []
series: null
date: '2025-11-05T22:12:12.500Z'
originalURL: https://freecodecamp.org/news/private-voice-assistant-using-open-source-tools
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762380694991/10687751-7aec-4d78-8af8-1f76edc28afd.png
tags:
- name: Voice
  slug: voice
- name: voice assistants
  slug: voice-assistants
- name: 'RAG '
  slug: rag
- name: 'Personalization '
  slug: personalization
- name: tool calling
  slug: tool-calling
- name: agentic AI
  slug: agentic-ai
- name: on-device ai
  slug: on-device-ai
- name: Open Source
  slug: opensource
seo_title: 'Comment créer votre propre assistant vocal privé : un guide étape par
  étape utilisant des outils open-source'
seo_desc: Most commercial voice assistants send your voice data to cloud servers before
  responding. By using open‑source tools, you can run everything directly on your
  phone for better privacy, faster responses, and full control over how the assistant
  behaves....
---

La plupart des assistants vocaux commerciaux envoient vos données vocales vers des serveurs cloud avant de répondre. En utilisant des outils open-source, vous pouvez tout exécuter directement sur votre téléphone pour une meilleure confidentialité, des réponses plus rapides et un contrôle total sur le comportement de l'assistant.

Dans ce tutoriel, je vous guiderai pas à pas à travers le processus. Vous n'avez pas besoin d'expérience préalable avec les modèles de machine learning, car nous construirons le système progressivement et testerons chaque partie au fur et à mesure. À la fin, vous disposerez d'un assistant vocal mobile entièrement local propulsé par :

* Whisper pour la reconnaissance vocale automatique (ASR)
    
* Machine Learning Compiler (MLC) LLM pour le raisonnement sur l'appareil
    
* System Text-to-Speech (TTS) utilisant le TTS intégré d'Android
    

Votre assistant sera capable de :

* Comprendre vos commandes vocales hors ligne
    
* Vous répondre avec une parole synthétisée
    
* Effectuer des actions d'appel d'outils (comme contrôler des appareils intelligents)
    
* Stocker des souvenirs personnels et des préférences
    
* Utiliser la génération augmentée par récupération (RAG) pour répondre à des questions à partir de vos propres notes
    
* Exécuter des flux de travail agentiques multi-étapes tels que la génération d'un briefing matinal et l'envoi optionnel du résumé à un contact
    

Ce tutoriel se concentre sur Android en utilisant Termux (l'environnement de terminal pour Android) pour un flux de travail entièrement local.

## Table des matières

* [Aperçu du système](#heading-apercu-du-systeme)
    
* [Prérequis](#heading-prerequis)
    
* [Étape 1 : Tester le microphone et la lecture audio sur Android](#heading-etape-1-tester-le-microphone-et-la-lecture-audio-sur-android)
    
* [Étape 2 : Installer et exécuter Whisper pour l'ASR](#heading-etape-2-installer-et-executer-whisper-pour-l-asr)
    
* [Étape 3 : Installer un LLM local avec MLC](#heading-etape-3-installer-un-llm-local-avec-mlc)
    
* [Étape 4 : Synthèse vocale locale (TTS)](#heading-etape-4-synthese-vocale-locale-tts)
    
* [Étape 5 : La boucle vocale principale](#heading-etape-5-la-boucle-vocale-principale)
    
* [Étape 6 : Appel d'outils (Passer à l'action)](#heading-etape-6-appel-d-outils-passer-a-l-action)
    
* [Étape 7 : Mémoire et personnalisation](#heading-etape-7-memoire-et-personnalisation)
    
* [Étape 8 : Génération augmentée par récupération (RAG)](#heading-etape-8-generation-augmentee-par-recuperation-rag)
    
* [Étape 9 : Flux de travail agentique multi-étapes](#heading-etape-9-flux-de-travail-agentique-multi-etapes)
    
* [Conclusion et prochaines étapes](#heading-conclusion-et-prochaines-etapes)
    

## **Aperçu du système**

Ce diagramme montre comment votre voix circule dans l'assistant : parole en entrée → transcription → raisonnement → action → réponse parlée.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1762319872832/7b52b715-79c0-4c92-b431-b84c49ba7299.png align="center")

Ce pipeline décrit le flux principal :

* Vous parlez dans le microphone.
    
* Whisper convertit l'audio en texte.
    
* Le LLM local interprète votre demande.
    
* L'assistant peut appeler des outils (par exemple, envoyer des notifications ou créer des événements).
    
* La réponse est prononcée à haute voix en utilisant le système de synthèse vocale de l'appareil.
    

### Concepts clés utilisés dans ce tutoriel

* **Reconnaissance vocale automatique (ASR) :** Convertit votre parole en texte. Nous utilisons Whisper ou Faster‑Whisper.
    
* **Modèle de langage local (LLM) :** Un modèle de raisonnement fonctionnant sur votre téléphone via le moteur MLC.
    
* **Synthèse vocale (TTS) :** Convertit le texte en parole. Nous utilisons le TTS système intégré d'Android.
    
* **Appel d'outils (Tool Calling) :** Permet à l'assistant d'effectuer des actions (par exemple, envoyer une notification ou créer un événement).
    
* **Mémoire :** Stocke des faits personnalisés que l'assistant apprend au cours de la conversation.
    
* **Génération augmentée par récupération (RAG) :** Permet à l'assistant de consulter vos documents ou notes.
    
* **Flux de travail agentique :** Une chaîne multi-étapes où l'assistant utilise plusieurs capacités ensemble.
    

## Prérequis

Ce avec quoi vous devriez déjà être familier :

* Utilisation basique de la ligne de commande (exécuter des commandes, naviguer dans les répertoires)
    
* Python très basique (appeler une fonction, éditer un script `.py`)
    

Vous n'avez **pas** besoin d'avoir :

* D'expérience en machine learning
    
* Une compréhension approfondie des réseaux de neurones
    
* Une expérience préalable avec les modèles de parole ou audio
    

Voici les outils et technologies dont vous aurez besoin pour suivre :

* Un téléphone Android avec Snapdragon 8+ Gen 1 ou plus récent recommandé (les appareils plus anciens fonctionneront toujours, mais les réponses peuvent être plus lentes)
    
* Termux
    
* Python 3.9+ à l'intérieur de Termux
    
* Suffisamment de stockage libre (au moins 4 à 6 Go) pour stocker le modèle et les fichiers audio
    

**Pourquoi ces exigences sont importantes :**

Les modèles Whisper et Llama s'exécutent sur l'appareil, le téléphone doit donc gérer le calcul en temps réel. MLC optimise les modèles pour le GPU / NPU de votre appareil, ainsi les processeurs plus récents fonctionneront plus rapidement et chaufferont moins. De plus, le TTS système et les API Termux permettent à l'assistant de parler et d'interagir localement avec le téléphone.

Si votre téléphone est plus ancien ou de milieu de gamme, remplacez le modèle à l'Étape 3 par `Phi-3.5-Mini` qui est plus petit et plus rapide.

Nous commencerons par configurer votre environnement Android avec Termux, Python, l'accès aux médias et les permissions de stockage afin que les étapes ultérieures puissent enregistrer de l'audio, exécuter des modèles et parler.

**Exécutez ceci maintenant :**

```python
# In Termux
pkg update && pkg upgrade -y
pkg install -y python git ffmpeg termux-api
termux-setup-storage  # grant storage permission
```

## Étape 1 : Tester le microphone et la lecture audio sur Android

**Ce que fait cette étape :** Vérifie que le microphone et les haut-parleurs de votre appareil fonctionnent correctement via Termux avant de les connecter à l'assistant vocal.

Les assistants sur l'appareil ont besoin d'un accès fiable au microphone et aux haut-parleurs. Sur Android, Termux fournit des utilitaires pour enregistrer de l'audio et lire des médias. Cela évite les dépendances audio complexes et fonctionne sur davantage d'appareils.

Ces commandes vous permettent de tester rapidement votre microphone et votre lecture audio sans écrire de code. C'est utile pour vérifier que les permissions de votre appareil et les chemins audio fonctionnent avant d'introduire Whisper ou le TTS.

* `termux-microphone-record` enregistre depuis le microphone de l'appareil vers un fichier `.wav` 
    
* `termux-media-player` lit les fichiers audio
    
* `termux-tts-speak` prononce du texte en utilisant la voix TTS du système (solution de repli rapide)
    

**Exécutez ceci maintenant :**

```python
# Start a 4 second recording
termux-microphone-record -f in.wav -l 4 && termux-microphone-record -q

# Play back the captured audio
termux-media-player play in.wav

# Speak text via system TTS (fallback if you do not install a Python TTS)
termux-tts-speak "Hello, this is your on-device assistant running locally."
```

## Étape 2 : Installer et exécuter Whisper pour l'ASR

**Ce que fait cette étape :** Convertit la parole enregistrée en texte afin que le modèle de langage puisse comprendre ce que vous avez dit.

Whisper écoute votre enregistrement audio et le convertit en texte. Les versions plus petites comme `tiny` ou `base` s'exécutent plus rapidement sur la plupart des téléphones et sont suffisantes pour les commandes quotidiennes.

Installer Whisper :

```python
pip install openai-whisper
```

Si vous rencontrez des problèmes d'installation, vous pouvez utiliser Faster‑Whisper à la place :

```python
pip install faster-whisper
```

Voici un petit script Python qui prend le fichier audio enregistré et le transforme en texte. Il essaie d'abord Whisper, et si celui-ci n'est pas disponible, il basculera automatiquement vers Faster‑Whisper.

```python
# Convert recorded speech to text (asr_transcribe.py)
import sys

# Try Whisper, fallback to Faster-Whisper if needed
try:
    import whisper
    use_faster = False
except Exception:
    use_faster = True

if use_faster:
    from faster_whisper import WhisperModel
    model = WhisperModel("tiny.en")
    segments, info = model.transcribe(sys.argv[1])
    text = " ".join(s.text for s in segments)
    print(text.strip())
else:
    model = whisper.load_model("tiny.en")
    result = model.transcribe(sys.argv[1], fp16=False)
    print(result["text"].strip())
```

**Exécutez ceci maintenant :**

```python
# Record 4 seconds and transcribe
termux-microphone-record -f in.wav -l 4 && termux-microphone-record -q
python asr_transcribe.py in.wav
```

## Étape 3 : Installer un LLM local avec MLC

**Ce que fait cette étape :** Installe et teste le modèle de raisonnement sur l'appareil qui générera des réponses à la parole transcrite.

MLC compile les modèles transformer pour les GPU mobiles et les unités de traitement neuronal (NPU), permettant l'inférence sur l'appareil. Vous exécuterez un modèle optimisé pour les instructions avec des poids de 4 bits ou 8 bits pour plus de rapidité.

Installez l'interface de ligne de commande comme ceci :

```python
# Clone and install Python bindings (for scripting) and CLI
git clone https://github.com/mlc-ai/mlc-llm.git
cd mlc-llm
pip install -r requirements.txt
pip install -e python
```

Nous utiliserons **Llama 3 8B Instruct q4** car il offre un raisonnement solide tout en fonctionnant sur de nombreux appareils Android récents. Si votre téléphone a moins de mémoire ou si vous voulez des réponses plus rapides, vous pouvez opter pour **Phi-3.5 Mini** (environ 3,8B) sans changer de code.

Téléchargez un modèle optimisé pour mobile :

```python
mlc_llm download Llama-3-8B-Instruct-q4f16_1
```

Nous utiliserons un court script Python pour envoyer du texte au modèle et afficher la réponse. Cela nous permet de vérifier que le modèle est correctement installé avant de le connecter à l'audio.

```python
# Local LLM text generation (local_llm.py)
from mlc_llm import MLCEngine
import sys

engine = MLCEngine(model="Llama-3-8B-Instruct-q4f16_1")
prompt = sys.argv[1] if len(sys.argv) > 1 else "Hello"
resp = engine.chat([{"role": "user", "content": prompt}])
# The engine may return different structures across versions
reply_text = resp.get("message", resp) if isinstance(resp, dict) else str(resp)
print(reply_text)
```

**Exécutez ceci maintenant :**

```python
python local_llm.py "Summarize this in one sentence: building a local voice assistant on Android"
```

## Étape 4 : Synthèse vocale locale (TTS)

**Ce que fait cette étape :** Transforme les réponses textuelles du modèle en audio parlé afin que l'assistant puisse répondre.

Cette étape convertit le texte renvoyé par le modèle en audio parlé. Elle utilise la voix de synthèse vocale intégrée d'Android et ne nécessite aucun package Python supplémentaire.

```python
termux-tts-speak "Hello, I am running entirely on your device."
```

C'est la méthode de sortie vocale que nous utiliserons tout au long du tutoriel.

## Étape 5 : La boucle vocale principale

**Ce que fait cette étape :** Connecte la reconnaissance vocale, le raisonnement du modèle de langage et la synthèse vocale dans une seule boucle de conversation interactive.

Cette boucle lie l'enregistrement, la transcription, la génération de réponse et la lecture.

```python
# Core voice loop tying ASR + LLM + TTS (voice_loop.py)
import subprocess, os

def run(cmd): return subprocess.check_output(cmd).decode().strip()

print("Listening...")
subprocess.run(["termux-microphone-record", "-f", "in.wav", "-l", "4"]) ; subprocess.run(["termux-microphone-record", "-q"])
text = run(["python", "asr_transcribe.py", "in.wav"])
reply = run(["python", "local_llm.py", text])
try:
    subprocess.run(["python", "speak_xtts.py", reply]); subprocess.run(["termux-media-player", "play", "out.wav"])
except:
    subprocess.run(["termux-tts-speak", reply])
```

Exécution :

```python
python voice_loop.py
```

## Étape 6 : Appel d'outils (Passer à l'action)

**Ce que fait cette étape :** Permet à l'assistant d'effectuer des actions – pas seulement de répondre – en appelant de réelles fonctions sur votre appareil.

L'appel d'outils permet à l'assistant d'effectuer des actions, pas seulement de répondre. Lorsque le modèle reconnaît une demande d'action, il émet une petite instruction JSON, et votre code exécute la fonction correspondante. Vous montrez au modèle quels outils existent et comment les appeler. Le programme intercepte les appels et exécute le code correspondant.

**Exemple de cas d'utilisation :**

Vous dites : *"Planifie une réunion demain à 15h avec John."*

L'assistant :

1. Transcrit ce que vous avez dit.
    
2. Détecte qu'il ne s'agit pas d'une question, mais d'une demande d'action.
    
3. Appelle la fonction `add_event()` avec les bons paramètres.
    
4. Confirme : *"D'accord, j'ai planifié cela."*
    

Voici la structure du fonctionnement des appels d'outils :

* Définir des fonctions Python telles que `add_event`, `control_light`
    
* Fournir un schéma (schema) que le modèle doit produire lorsqu'il souhaite appeler un outil
    
* Détecter ce schéma dans la sortie du LLM et exécuter la fonction
    

```python
# Tool calling functions (tools.py)
import json

def add_event(title: str, date: str) -> dict:
    # Replace with actual calendar integration
    return {"status": "ok", "title": title, "date": date}

TOOLS = {
    "add_event": add_event,
}

def run_tool(call_json: str) -> str:
    """call_json: '{"tool":"add_event","args":{"title":"Dentist","date":"2025-11-10 10:00"}}'"""
    data = json.loads(call_json)
    name = data["tool"]
    args = data.get("args", {})
    if name in TOOLS:
        result = TOOLS[name](**args)
        return json.dumps({"tool_result": result})
    return json.dumps({"error": "unknown tool"})
```

Inciter le modèle à utiliser des outils :

```python
# LLM wrapper enabling tool use (llm_with_tools.py)
from mlc_llm import MLCEngine
import json, sys

SYSTEM = (
    "You can call tools by emitting a single JSON object with keys 'tool' and 'args'. "
    "Available tools: add_event(title:str, date:str). "
    "If no tool is needed, answer directly."
)

engine = MLCEngine(model="Llama-3-8B-Instruct-q4f16_1")
user = sys.argv[1]
resp = engine.chat([
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": user},
])
print(resp.get("message", resp) if isinstance(resp, dict) else str(resp))
```

Et ensuite, assembler le tout :

```python
# Run LLM with tool call detection (run_with_tools.py)
import subprocess, json
from tools import run_tool

user = "Add a dentist appointment next Thursday at 10"
raw = subprocess.check_output(["python", "llm_with_tools.py", user]).decode().strip()

# If the model returned a JSON tool call, run it
try:
    data = json.loads(raw)
    if isinstance(data, dict) and "tool" in data:
        print("Tool call:", data)
        print(run_tool(raw))
    else:
        print("Assistant:", raw)
except Exception:
    print("Assistant:", raw)
```

**Exécutez ceci maintenant :**

```python
python run_with_tools.py
```

## Étape 7 : Mémoire et personnalisation

**Ce que fait cette étape :** Permet à l'assistant de se souvenir des informations personnelles que vous partagez afin que les conversations semblent continues et adaptatives.

Un assistant utile doit donner l'impression d'apprendre à vos côtés. La mémoire permet au système de garder trace des petits détails que vous mentionnez naturellement en conversation.

Sans mémoire, chaque conversation repart de zéro. Avec la mémoire, votre assistant peut se souvenir de faits personnels (par exemple, anniversaires, musique préférée), de vos routines, des réglages de l'appareil ou des notes que vous mentionnez. Cela débloque des interactions plus naturelles et permet une personnalisation au fil du temps.

Vous pouvez commencer par un simple stockage clé-valeur et l'étendre avec le temps. Votre programme lit la mémoire avant l'inférence et y réinscrit de nouveaux faits après.

```python
# Simple key-value memory store (memory.py)
import json
from pathlib import Path

MEM_PATH = Path("memory.json")

def mem_load():
    return json.loads(MEM_PATH.read_text()) if MEM_PATH.exists() else {}

def mem_save(mem):
    MEM_PATH.write_text(json.dumps(mem, indent=2))

def remember(key: str, value: str):
    mem = mem_load()
    mem[key] = value
    mem_save(mem)
```

Utiliser la mémoire dans la boucle :

```python
# Voice loop with memory loading and updating (voice_loop_with_memory.py)
import subprocess, json
from memory import mem_load, remember

# 1) Record and transcribe
subprocess.run(["termux-microphone-record", "-f", "in.wav", "-l", "4"]) 
subprocess.run(["termux-microphone-record", "-q"]) 
user_text = subprocess.check_output(["python", "asr_transcribe.py", "in.wav"]).decode().strip()

# 2) Load memory and add as system context
mem = mem_load()
SYSTEM = "Known facts: " + json.dumps(mem)

# 3) Ask the model
from mlc_llm import MLCEngine
engine = MLCEngine(model="Llama-3-8B-Instruct-q4f16_1")
resp = engine.chat([
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": user_text},
])
reply = resp.get("message", resp) if isinstance(resp, dict) else str(resp)
print("Assistant:", reply)

# 4) Very simple pattern: if the user said "remember X is Y", store it
if user_text.lower().startswith("remember ") and " is " in user_text:
    k, v = user_text[9:].split(" is ", 1)
    remember(k.strip(), v.strip())
```

**Exécutez ceci maintenant :**

```python
python voice_loop_with_memory.py
```

## Étape 8 : Génération augmentée par récupération (RAG)

**Ce que fait cette étape :** Permet à l'assistant de rechercher dans vos notes ou documents hors ligne au moment de répondre, améliorant ainsi la précision pour les tâches personnelles.

Pour utiliser le RAG, nous installons d'abord une base de données vectorielle légère, puis nous y ajoutons des documents, et enfin nous l'interrogeons lors de la réponse aux questions.

Un modèle de langage ne peut pas connaître magiquement les détails de votre vie, de votre travail ou de vos fichiers à moins que vous ne lui donniez un moyen de faire des recherches.

La [Génération augmentée par récupération (RAG)](https://www.freecodecamp.org/news/learn-rag-fundamentals-and-advanced-techniques/) comble cette lacune. Le RAG permet à l'assistant de rechercher dans vos propres données stockées au moment de la requête. Cela signifie que l'assistant peut répondre à des questions sur vos projets, les détails de votre maison, vos plans de voyage, vos études ou tout document personnel que vous stockez complètement hors ligne.

Le RAG permet à l'assistant de se référer à vos notes réelles lors de la réponse, au lieu de se fier uniquement à l'entraînement interne du modèle.

Installer le stockage vectoriel :

```python
pip install chromadb
```

Ajouter et rechercher vos notes :

```python
# Local vector DB indexing and querying (rag.py)
from chromadb import Client

client = Client()
notes = client.create_collection("notes")

# Add your documents (repeat as needed)
notes.add(documents=["Contractor quote was 42000 United States Dollars for the extension."], ids=["q1"]) 

# Query the local vector database
results = notes.query(query_texts=["extension quote"], n_results=1)
context = results["documents"][0][0]
print(context)
```

Utiliser le contexte récupéré dans les réponses :

```python
# LLM answering using retrieved context (llm_with_rag.py)
from mlc_llm import MLCEngine
from chromadb import Client

engine = MLCEngine(model="Llama-3-8B-Instruct-q4f16_1")
client = Client()
notes = client.get_or_create_collection("notes")

question = "What was the quoted amount for the home extension?"
res = notes.query(query_texts=[question], n_results=2)
ctx = "\n".join([d[0] for d in res["documents"]])

SYSTEM = "Use the provided context to answer accurately. If missing, say you do not know.\nContext:\n" + ctx
ans = engine.chat([
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": question},
])
print(ans.get("message", ans) if isinstance(ans, dict) else str(ans))
```

**Exécutez ceci maintenant :**

```python
python rag.py
python llm_with_rag.py
```

## Étape 9 : Flux de travail agentique multi-étapes

**Ce que fait cette étape :** Combine l'écoute, le raisonnement, la mémoire et l'utilisation d'outils dans une routine multi-étapes qui s'exécute automatiquement.

Maintenant que l'assistant peut écouter, répondre, mémoriser des faits et appeler des outils, nous pouvons combiner ces capacités dans une petite routine qui effectue plusieurs étapes automatiquement.

**Exemple pratique : "Briefing matinal" sur votre téléphone**

Objectif : lorsque vous dites *"Donne-moi mon briefing matinal et envoie-le par SMS à mon partenaire"*, l'assistant va :

1. Lire l'agenda du jour à partir d'un fichier local,
    
2. le résumer,
    
3. le prononcer à haute voix, et
    
4. envoyer le résumé par SMS via Termux.
    

![Flux de travail de briefing matinal multi-étapes avec récupération, résumé, sortie vocale et action SMS.](https://cdn.hashnode.com/res/hashnode/image/upload/v1762319593253/99e670d4-4934-47ce-a164-f0f7880ea80f.png align="center")

*Schéma : Flux de travail de briefing matinal multi-étapes avec récupération, résumé, sortie vocale et action SMS.*

### Préparez votre fichier d'agenda

Ce fichier stocke vos événements de la journée. Vous pouvez l'éditer manuellement, le générer ou le synchroniser plus tard si vous le souhaitez.

Créez `agenda.json` dans le même dossier :

```python
{
  "2025-11-03": [
    {"time": "09:30", "title": "Standup meeting"},
    {"time": "13:00", "title": "Lunch with Priya"},
    {"time": "16:30", "title": "Gym"}
  ]
}
```

Outils intégrés au téléphone pour ce flux de travail :

```python
# Phone-integrated agent tools (tools_phone.py)
import json, subprocess, datetime
from pathlib import Path

AGENDA_PATH = Path("agenda.json")

def load_today_agenda():
    today = datetime.date.today().isoformat()
    if not AGENDA_PATH.exists():
        return []
    data = json.loads(AGENDA_PATH.read_text())
    return data.get(today, [])

def send_sms(number: str, text: str) -> dict:
    # Requires Termux:API and SMS permission
    subprocess.run(["termux-sms-send", "-n", number, text])
    return {"status": "sent", "to": number}

def notify(title: str, content: str) -> dict:
    subprocess.run(["termux-notification", "--title", title, "--content", content])
    return {"status": "notified"}
```

Créer la routine de l'agent :

```python
# Multi-step morning briefing agent (agent_morning.py)
import json, subprocess, os
from mlc_llm import MLCEngine
from tools_phone import load_today_agenda, send_sms, notify

PARTNER_PHONE = os.environ.get("PARTNER_PHONE", "+15551234567")

TOOLS = {
    "send_sms": send_sms,
    "notify": notify,
}

SYSTEM = (
  "You assist on a phone. You may emit a single-line JSON when an action is needed "
  "with keys 'tool' and 'args'. Available tools: send_sms(number:str, text:str), "
  "notify(title:str, content:str). Keep messages concise. If no tool is needed, answer in plain text."
)

engine = MLCEngine(model="Llama-3-8B-Instruct-q4f16_1")

agenda = load_today_agenda()
agenda = load_today_agenda()
agenda_text = "\n".join(f"{e['time']} - {e['title']}" for e in agenda) or "No events for today."

user_request = "Give me my morning briefing and text it to my partner." "Give me my morning briefing and text it to my partner."

# 1) Ask LLM for a 2-3 sentence summary to speak
summary = engine.chat([
  {"role": "system", "content": "Summarize this agenda in 2-3 sentences for a morning briefing:"},
  {"role": "user", "content": agenda_text},
])
summary_text = summary.get("message", summary) if isinstance(summary, dict) else str(summary)
print("Briefing:\n", summary_text)

# 2) Speak locally (prefer XTTS, fallback to system TTS)
try:
    subprocess.run(["python", "speak_xtts.py", summary_text], check=True)
    subprocess.run(["termux-media-player", "play", "out.wav"]) 
except Exception:
    subprocess.run(["termux-tts-speak", summary_text])

# 3) Ask LLM whether to send SMS and with what text, using tool schema
resp = engine.chat([
  {"role": "system", "content": SYSTEM},
  {"role": "user", "content": f"User said: '{user_request}'. Partner phone is {PARTNER_PHONE}. Summary: {summary_text}"},
])
msg = resp.get("message", resp) if isinstance(resp, dict) else str(resp)

# 4) If the model requested a tool, execute it
try:
    data = json.loads(msg)
    if isinstance(data, dict) and data.get("tool") in TOOLS:
        # Auto-fill phone number if missing
        if data["tool"] == "send_sms" and "number" not in data.get("args", {}):
            data.setdefault("args", {})["number"] = PARTNER_PHONE
        result = TOOLS[data["tool"]](**data.get("args", {}))
        print("Tool result:", result)
    else:
        print("Assistant:", msg)
except Exception:
    print("Assistant:", msg)
```

**Exécutez ceci maintenant :**

```python
export PARTNER_PHONE=+15551234567
python agent_morning.py
```

Cet exemple est réaliste sur Android car il utilise les utilitaires Termux que vous avez déjà installés : le TTS local pour la sortie vocale, `termux-sms-send` pour la messagerie, et `termux-notification` pour une confirmation rapide sur l'appareil. Vous pourrez l'étendre plus tard avec un outil Home Assistant si vous avez un serveur local (par exemple, pour allumer les lumières ou régler des scènes de thermostat).

## Conclusion et prochaines étapes

Construire un assistant vocal entièrement local est un processus incrémental. Chaque étape ajoutée – reconnaissance vocale, génération de texte, mémoire, récupération et exécution d'outils – a débloqué de nouvelles capacités et a rapproché le système du comportement d'un véritable assistant.

Vous avez construit un assistant vocal entièrement local sur votre téléphone avec :

* Une reconnaissance vocale automatique sur l'appareil avec Whisper (avec repli sur Faster-Whisper)
    
* Un raisonnement sur l'appareil avec le modèle de langage MLC
    
* Une synthèse vocale locale utilisant le TTS système intégré
    
* L'appel d'outils pour des actions réelles
    
* La mémoire et la personnalisation
    
* La génération augmentée par récupération pour les connaissances basées sur des documents
    
* Une boucle d'agent simple pour le travail multi-étapes
    

À partir de là, vous pouvez ajouter :

* La détection de mot de réveil (par exemple, Porcupine ou des modèles open wake word)
    
* Des intégrations spécifiques à l'appareil (par exemple, Home Assistant, éclairage intelligent)
    
* De meilleurs schémas de mémoire et des adaptateurs pour calendriers ou contacts
    

Vos données ne quittent jamais votre appareil, et vous contrôlez chaque partie de la pile. C'est un assistant privé et personnalisable que vous pouvez étendre comme bon vous semble.