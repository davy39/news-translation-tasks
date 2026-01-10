---
title: Comment créer des outils d'accessibilité IA de reconnaissance vocale et de
  synthèse vocale avec Python
subtitle: ''
author: OMOTAYO OMOYEMI
co_authors: []
series: null
date: '2025-09-01T19:50:40.943Z'
originalURL: https://freecodecamp.org/news/build-ai-accessibility-tools-with-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756755907758/3568b7ab-f659-45c9-8c1a-e877d1a0a166.png
tags:
- name: Accessibility
  slug: accessibility
- name: Python
  slug: python
- name: AI
  slug: ai
seo_title: Comment créer des outils d'accessibilité IA de reconnaissance vocale et
  de synthèse vocale avec Python
seo_desc: Learn how to use AI to make classrooms more inclusive. Build simple Python
  tools for speech-to-text and text-to-speech that support diverse learners.
---

Les salles de classe d'aujourd'hui sont plus diversifiées que jamais. Parmi les élèves se trouvent des apprenants neurodivergents ayant des besoins d'apprentissage différents. Bien que ces apprenants apportent des forces uniques, les méthodes d'enseignement traditionnelles ne répondent pas toujours à leurs besoins.

C'est là que les outils d'accessibilité pilotés par l'IA peuvent faire la différence. Du sous-titrage en temps réel au support de lecture adaptatif, l'intelligence artificielle transforme les salles de classe en espaces plus inclusifs.

Dans cet article, vous allez :

* Comprendre ce que signifie l'éducation inclusive en pratique.
    
* Voir comment l'IA peut soutenir les apprenants neurodivergents.
    
* Essayer deux démos Python pratiques :
    
    * **Reconnaissance vocale (Speech-to-Text)** en utilisant Whisper en local (gratuit, sans clé API).
        
    * **Synthèse vocale (Text-to-Speech)** en utilisant Hugging Face SpeechT5.
        
* Obtenir une structure de projet prête à l'emploi, les prérequis et des conseils de dépannage pour les utilisateurs Windows et macOS/Linux.
    

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Remarque sur les fichiers manquants](#heading-remarque-sur-les-fichiers-manquants)
    
* [Ce que l'éducation inclusive signifie réellement](#heading-ce-que-leducation-inclusive-signifie-reellement)
    
* [Boîte à outils : Cinq outils d'accessibilité IA que les enseignants peuvent essayer dès aujourd'hui](#heading-boite-a-outils-cinq-outils-daccessibilite-ia-pour-les-enseignants)
    
* [Remarques par plateforme (Windows vs macOS/Linux)](#heading-remarques-par-plateforme-windows-vs-macoslinux)
    
* [Guide pratique : Créer une boîte à outils d'accessibilité simple (Python)](#heading-guide-pratique-creer-une-boite-a-outils-daccessibilite-python)
    
* [Antisèche de configuration rapide](#heading-antiseche-de-configuration-rapide)
    
* [Du code à l'impact en classe](#heading-du-code-a-limpact-en-classe)
    
* [Défi pour les développeurs : Coder pour l'inclusion](#heading-defi-pour-les-developpeurs-coder-pour-linclusion)
    
* [Défis et considérations](#heading-defis-et-considerations)
    
* [Perspectives d'avenir](#heading-perspectives-davenir)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :

* **Python 3.8** ou version ultérieure installé (pour les utilisateurs Windows, si vous ne l'avez pas, vous pouvez télécharger la dernière version sur : [python.org](http://python.org). Les utilisateurs macOS l'ont généralement déjà via `python3`).
    
* **Environnement virtuel** configuré (`venv`) — recommandé pour garder votre système propre.
    
* **Installation de** [**FFmpeg**](https://www.gyan.dev/ffmpeg/builds/#) (requis pour que Whisper puisse lire les fichiers audio).
    
* **PowerShell** (Windows) ou **Terminal** (macOS/Linux).
    
* **Connaissances de base** sur l'exécution de scripts Python.
    

**Conseil** : Si vous débutez avec les environnements Python, ne vous inquiétez pas car les commandes de configuration seront incluses dans chaque étape ci-dessous.

## Remarque sur les fichiers manquants

Certains fichiers ne sont pas inclus dans le [répôt GitHub](https://github.com/tayo4christ/inclusive-ai-toolkit). C'est intentionnel, ils sont soit générés automatiquement, soit doivent être créés/installés localement :

* `.venv/` → Votre dossier d'environnement virtuel. Chaque lecteur doit créer le sien localement avec :
    
    ```python
    python -m venv .venv
    ```
    
    1. **Installation de FFmpeg** :
        
        * **Windows** : FFmpeg n'est pas inclus dans les fichiers du projet car il est volumineux (environ 90 Mo). Les utilisateurs doivent télécharger le build FFmpeg séparément.
            
        * **macOS** : Les utilisateurs peuvent installer FFmpeg via le gestionnaire de paquets Homebrew avec la commande `brew install ffmpeg`.
            
        * **Linux** : Les utilisateurs peuvent installer FFmpeg via le gestionnaire de paquets avec la commande `sudo apt install ffmpeg`.
            
    2. **Fichier de sortie** :
        
        * `output.wav` est un fichier généré lorsque vous exécutez le script de synthèse vocale. Ce fichier n'est pas inclus dans le dépôt GitHub, il est créé localement sur votre machine lors de l'exécution du script.
            

Pour garder le dépôt propre, ces éléments sont exclus via `.gitignore` :

```python
# Ignorer les environnements virtuels
.venv/
env/
venv/

# Ignorer les fichiers binaires
ffmpeg.exe
*.dll
*.lib

# Ignorer l'audio généré (mais garder l'entrée d'exemple)
*.wav
*.mp3
!lesson_recording.mp3
```

Le dépôt inclut tous les fichiers essentiels nécessaires pour suivre :

* `requirements.txt` (voir ci-dessous)
    
* `transcribe.py` et `tts.py` (couverts étape par étape dans la section pratique).
    

`requirements.txt`

```python
openai-whisper
transformers
torch
soundfile
sentencepiece
numpy
```

De cette façon, vous aurez tout ce dont vous avez besoin pour reproduire le projet.

## Ce que l'éducation inclusive signifie réellement

L'éducation inclusive va au-delà du simple placement d'élèves aux besoins divers dans une même classe. Il s'agit de concevoir des environnements d'apprentissage où chaque élève peut s'épanouir.

Les barrières courantes incluent :

* Difficultés de lecture (par exemple, la dyslexie).
    
* Défis de communication (troubles de la parole ou de l'audition).
    
* Surcharge sensorielle ou troubles de l'attention (autisme, TDAH).
    
* Difficultés de prise de notes et de compréhension.
    

L'IA peut aider à réduire ces barrières grâce au sous-titrage, à la lecture à voix haute, au rythme adaptatif et aux outils de communication alternative.

## Boîte à outils : Cinq outils d'accessibilité IA que les enseignants peuvent essayer dès aujourd'hui

1. [**Lecteur Immersif Microsoft**](https://support.microsoft.com/en-gb/office/use-immersive-reader-in-word-a857949f-c91e-4c97-977c-a4efcaf9b3c1) – Synthèse vocale, guides de lecture et traduction.
    
2. [**Google Live Transcribe**](https://cloud.google.com/speech-to-text) – Sous-titres en temps réel pour le support auditif.
    
3. [**Otter.ai**](http://Otter.ai) – Prise de notes automatique et résumé.
    
4. [**Grammarly**](https://www.grammarly.com/) **/** [**Quillbot**](https://quillbot.com/login?returnUrl=%2F&triggerOneTap=true) – Assistance à l'écriture pour la lisibilité et la clarté.
    
5. [**Seeing AI (Microsoft)**](https://blogs.microsoft.com/accessibility/seeing-ai/) – Décrit le texte et les scènes pour les apprenants malvoyants.
    

### Exemples concrets

Un élève dyslexique peut utiliser le Lecteur Immersif pour écouter un manuel tout en suivant visuellement. Un autre élève malentendant peut utiliser Live Transcribe pour suivre les discussions en classe. Ce sont de petits changements technologiques qui créent de grandes victoires en matière d'inclusion.

## Remarques par plateforme (Windows vs macOS/Linux)

La plupart du code fonctionne de la même manière sur tous les systèmes, mais les commandes de configuration diffèrent légèrement :

**Création d'un environnement virtuel**

Pour créer et activer un environnement virtuel dans PowerShell en utilisant Python 3.8 ou supérieur, vous pouvez suivre ces étapes :

1. **Créer un environnement virtuel** :
    
    ```powershell
    py -3.12 -m venv .venv
    ```
    
2. **Activer l'environnement virtuel** :
    
    ```powershell
    .\.venv\Scripts\Activate
    ```
    

Une fois activée, votre invite PowerShell devrait changer pour indiquer que vous travaillez maintenant dans l'environnement virtuel. Cette configuration aide à gérer les dépendances et à isoler votre projet.

Pour les utilisateurs macOS, pour créer et activer un environnement virtuel dans un shell bash en utilisant Python 3, vous pouvez suivre ces étapes :

1. **Créer un environnement virtuel** :
    
    ```bash
    python3 -m venv .venv
    ```
    
2. **Activer l'environnement virtuel** :
    
    ```bash
    source .venv/bin/activate
    ```
    

**Pour installer FFmpeg sur Windows, suivez ces étapes :**

1. **Télécharger le Build FFmpeg** : Visitez le [site officiel](https://www.gyan.dev/ffmpeg/builds/#) de FFmpeg pour télécharger le dernier build pour Windows.
    
2. **Décompresser le fichier** : Une fois téléchargé, décompressez le fichier pour extraire son contenu. Vous trouverez plusieurs fichiers, dont `ffmpeg.exe`.
    
3. **Copier** `ffmpeg.exe` : Vous avez deux options :
    
    * **Dossier du projet** : Copiez `ffmpeg.exe` directement dans le dossier de votre projet.
        
    * **Ajouter au PATH** : Ajoutez le répertoire contenant `ffmpeg.exe` à la variable d'environnement PATH de votre système.
        

Le dossier complet du projet est disponible au [téléchargement sur GitHub](https://github.com/tayo4christ/inclusive-ai-toolkit).

Pour les utilisateurs macOS :

Utilisez Homebrew :

1. **Ouvrir le Terminal**.
    
2. **Installer Homebrew** (si non installé) : `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
3. **Installer FFmpeg** :
    
    ```bash
    brew install ffmpeg
    ```
    

Pour les utilisateurs Linux (Debian/Ubuntu) :

1. **Ouvrir le Terminal**.
    
2. **Mettre à jour la liste des paquets** : `sudo apt update`
    
3. **Installer FFmpeg** :
    
    ```bash
    sudo apt install ffmpeg
    ```

**Exécuter les scripts Python**

* Windows : `python script.py` ou `py script.py`
    
* macOS/Linux : `python3 script.py`

## Guide pratique : Créer une boîte à outils d'accessibilité simple (Python)

Vous allez créer deux petites démos :

* **Reconnaissance vocale** avec Whisper (local, gratuit).
    
* **Synthèse vocale** avec Hugging Face SpeechT5.
    

### 1) Reconnaissance vocale avec Whisper (Local et gratuit)

**Ce que vous allez construire :**  
Un script Python qui prend un court enregistrement MP3 et affiche la transcription dans votre terminal.

**Pourquoi Whisper ?**  
C'est un modèle de reconnaissance vocale open-source robuste. La version locale est parfaite pour les débutants car elle évite les clés API et fonctionne hors ligne.

**Comment installer Whisper (PowerShell) :**

```powershell
# Activez votre environnement virtuel
# Exemple : .\venv\Scripts\Activate

# Installez le paquet openai-whisper
pip install openai-whisper

# Vérifiez si FFmpeg est disponible
ffmpeg -version
```

**Remarque :** Les utilisateurs macOS peuvent utiliser le même code dans leur terminal.

### Créer `transcribe.py` :

```python
import whisper

# Charger le modèle Whisper
model = whisper.load_model("base")  # Utilisez "tiny" ou "small" pour plus de rapidité

# Transcrire le fichier audio
result = model.transcribe("lesson_recording.mp3", fp16=False)

# Afficher la transcription
print("Transcription :", result["text"])
```

**Fonctionnement du code :**

* `whisper.load_model("base")` — télécharge/charge le modèle une fois, puis utilise le cache.
    
* `model.transcribe(...)` — gère le décodage audio, la détection de la langue et l'inférence.
    
* `fp16=False` — évite les calculs GPU en demi-précision pour fonctionner sur CPU.
    

Lancez-le :

```bash
python transcribe.py
```

### 2) Synthèse vocale avec SpeechT5

**Ce que vous allez construire :**  
Un script Python qui convertit une courte phrase en un fichier audio WAV nommé `output.wav`.

**Pourquoi SpeechT5 ?**  
C'est un modèle ouvert largement utilisé qui fonctionne sur votre CPU. Aucune clé API n'est requise.

**Installer les paquets requis (PowerShell Windows) :**

```powershell
# Activer votre environnement virtuel
# Installer les paquets requis
pip install transformers torch soundfile sentencepiece
```

Créer `tts.py`

```python
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import soundfile as sf
import torch
import numpy as np

# Charger les modèles
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Embedding du locuteur (graine aléatoire fixe pour une voix synthétique constante)
g = torch.Generator().manual_seed(42)
speaker_embeddings = torch.randn((1, 512), generator=g)

# Texte à synthétiser
text = "Bienvenue dans l'éducation inclusive avec l'IA."
inputs = processor(text=text, return_tensors="pt")

# Générer la parole
with torch.no_grad():
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

# Sauvegarder en WAV
sf.write("output.wav", speech.numpy(), samplerate=16000)
print("✅ Audio sauvegardé sous le nom output.wav")
```

Lancez-le :

```bash
python tts.py
```

**Note :** macOS/Linux utilisent `python3 tts.py`.

### 3) Optionnel : Whisper via l'API OpenAI

**Ce que cela fait :**  
Au lieu d'exécuter Whisper localement, vous appelez l'API OpenAI (`whisper-1`). Votre fichier est transcrit sur les serveurs d'OpenAI.

**Pourquoi utiliser l'API ?**

* Pas besoin d'installer de gros modèles localement.
    
* Plus rapide si votre ordinateur est lent.
    

**Configuration de la clé API (PowerShell) :**

```powershell
$env:OPENAI_API_KEY="votre_cle_api_ici"
```

**Créer** `transcribe_api.py`

```python
from openai import OpenAI

# Initialiser le client OpenAI
client = OpenAI()

# Ouvrir le fichier audio et créer une transcription
with open("lesson_recording.mp3", "rb") as f:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=f
    )

print("Transcription :", transcript.text)
```

**Local Whisper vs API Whisper — Lequel utiliser ?**

| Caractéristique | Whisper Local (sur votre machine) | API Whisper OpenAI (cloud) |
| --- | --- | --- |
| **Configuration** | Nécessite paquets Python + FFmpeg | Client `openai` + clé API |
| **Matériel** | Utilise votre CPU/GPU | Serveurs OpenAI |
| **Coût** | ✅ Gratuit | 💳 Payant à la minute |
| **Internet requis** | ❌ Non (une fois installé) | ✅ Oui |
| **Confidentialité** | L'audio reste sur votre machine | L'audio est envoyé à OpenAI |

## **Antisèche de configuration rapide**

| Tâche | Windows (PowerShell) | macOS / Linux (Terminal) |
| --- | --- | --- |
| **Créer venv** | `py -3.12 -m venv .venv` | `python3 -m venv .venv` |
| **Activer venv** | `.\.venv\Scripts\Activate` | `source .venv/bin/activate` |
| **Installer Whisper** | `pip install openai-whisper` | `pip install openai-whisper` |
| **Installer FFmpeg** | [Télécharger](https://www.gyan.dev/ffmpeg/builds/) -> extraire -> PATH | `brew install ffmpeg` / `sudo apt install ffmpeg` |
| **Lancer STT** | `python transcribe.py` | `python3 transcribe.py` |
| **Lancer TTS** | `python tts.py` | `python3 tts.py` |

## Du code à l'impact en classe

Vous avez maintenant un prototype fonctionnel capable de :

* Convertir des leçons orales en texte.
    
* Lire du texte à voix haute pour les élèves qui préfèrent l'entrée auditive.

## Défi pour les développeurs : Coder pour l'inclusion

Essayez de combiner les deux scripts pour créer une **application compagnon de classe** qui :

* **Sous-titre** ce que l'enseignant dit en temps réel.
    
* **Lit à voix haute** les passages de manuels sur demande.

## Défis et considérations

* **Confidentialité** : Les données des élèves doivent être protégées.
    
* **Coût** : Les solutions doivent rester abordables pour les écoles.
    
* **Formation** : Les enseignants ont besoin de soutien pour utiliser ces outils en toute confiance.

## Perspectives d'avenir

L'avenir de l'éducation inclusive passera par l'IA multimodale combinant parole, gestes, symboles et reconnaissance des émotions, créant une communication fluide pour tous les apprenants.

## Conclusion

L'IA n'est pas là pour remplacer les enseignants, mais pour les aider à atteindre chaque élève. En adoptant l'accessibilité pilotée par l'IA, les salles de classe deviennent des espaces où les apprenants neurodivergents ne sont plus laissés pour compte, mais propulsés vers la réussite.

**Code source complet sur GitHub :** [Inclusive AI Toolkit](https://github.com/tayo4christ/inclusive-ai-toolkit)