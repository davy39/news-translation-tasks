---
title: Comment construire un traducteur multimodal Makaton-Anglais pour une éducation
  accessible
subtitle: ''
author: OMOTAYO OMOYEMI
co_authors: []
series: null
date: '2025-09-18T01:20:45.526Z'
originalURL: https://freecodecamp.org/news/build-a-multimodal-translator-for-accessible-education
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758158024064/bf3d7dac-0231-450a-9b40-6abf43085e49.png
tags:
- name: Accessibility
  slug: accessibility
- name: Python
  slug: python
- name: AI
  slug: ai
seo_title: Comment construire un traducteur multimodal Makaton-Anglais pour une éducation
  accessible
seo_desc: 'Discover how AI is transforming accessibility in education, from Makaton
  gesture translation to adaptive speech assistants like AURA. Explore multimodal
  AI '
---

Un élève de troisième entre en classe plein d'idées, mais au moment de contribuer, les outils qui l'entourent ne l'écoutent pas. Sa parole est difficile à reconnaître pour les systèmes vocaux standards, taper au clavier lui semble lent et épuisant, et la leçon avance sans que sa voix ne soit entendue. Le défi n'est pas un manque de capacité, mais un manque d'accès.

À travers le monde, des millions d'apprenants font face à des barrières de communication. Certains vivent avec une apraxie de la parole ou une dysarthrie, d'autres avec une mobilité réduite, des différences auditives ou des besoins neurodivers. Lorsque parler, écrire ou pointer devient peu fiable ou fatiguant, la participation se limite, le feedback est perdu et la confiance s'érode lentement. Ce n'est pas une exception rare, mais une réalité quotidienne dans les salles de classe.

Ces barrières se manifestent de manières très concrètes. Les élèves sont ignorés ou mal compris lorsqu'ils ne peuvent pas répondre rapidement. Leur capacité est sous-évaluée car leurs moyens d'expression sont restreints. Les enseignants luttent pour maintenir le rythme des cours tout en procédant à des aménagements individuels. Les pairs interagissent moins souvent, réduisant les opportunités d'appartenance sociale.

Les technologies d'assistance ont aidé au fil des ans, avec des outils comme la synthèse vocale, les tableaux de symboles et les entrées gestuelles simples. Pourtant, la plupart de ces outils sont conçus pour un mode d'interaction unique. Ils supposent que l'apprenant va soit parler, soit taper, soit toucher. La communication réelle, cependant, est fluide. Les apprenants combinent naturellement gestes, parole partielle, symboles et contexte pour partager un sens, surtout lorsque la fatigue, l'anxiété ou les défis moteurs entrent en jeu.

C'est là que l'IA moderne change la donne. Nous commençons à dépasser les outils à solution unique pour passer à des systèmes multimodaux capables de comprendre la parole, même lorsqu'elle est désordonnée, d'interpréter les gestes et les symboles visuels, de combiner les signaux pour déduire l'intention et de s'adapter en temps réel à mesure que les capacités de l'apprenant se développent ou changent.

L'IA remodèle l'accessibilité dans l'éducation en passant d'outils isolés à des systèmes multimodaux et adaptatifs. Ces systèmes combinent le geste, la parole et un feedback intelligent pour rejoindre les apprenants là où ils en sont, tout en soutenant leur croissance au fil du temps.

Dans cet article, nous explorerons à quoi ressemble ce changement dans la pratique, comment il peut débloquer la participation, et comment le feedback adaptatif personnalise le soutien. Nous construirons également une démo multimodale pratique qui transforme ces idées en un outil prêt pour la classe.

## Prérequis

* **Un système d'exploitation :** Windows, macOS ou Linux
    
* **Python installé (3.9 ou plus récent)** – Avec `pip` pour l'installation des packages.
    
* **Éditeur :** Visual Studio Code ou n'importe quel environnement de développement intégré (IDE)
    
* **Bases :** Être à l'aise avec l'exécution de commandes dans un terminal
    
* **Matériel optionnel :** Microphone (entrée vocale), Webcam (onglet image unique), haut-parleurs (lecture TTS)
    
* **Internet :** Requis pour SpeechRecognition par défaut (Google Web Speech API) et gTTS
    
* **Aucun jeu de données/modèle requis :** Un classificateur de gestes "stub" (bouchon) est fourni pour que la démo s'exécute de bout en bout
    

## Table des matières

* [Prérequis](#heading-pre-requis)
    
* [Ce que nous avons accompli jusqu'à présent](#heading-ce-que-nous-avons-accompli-jusqua-present)
    
* [Étude de cas 1 : Traduire le Makaton en Anglais](#heading-etude-de-cas-1-traduire-le-makaton-en-anglais)
    
* [Étude de cas 2 : Prototype AURA (Assistant vocal adaptatif)](#heading-etude-de-cas-2-prototype-aura-assistant-vocal-adaptatif)
    
* [Vue d'ensemble : Outils d'accessibilité multimodaux](#heading-vue-densemble-outils-daccessibilite-multimodaux)
    
* [Comment construire un traducteur multimodal Makaton-Anglais (Geste + Parole)](#heading-comment-construire-un-traducteur-multimodal-makaton-anglais-geste-parole)
    
* [Aperçu du projet](#heading-apercu-du-projet)
    
* [Défis et considérations éthiques](#heading-defis-et-considerations-ethiques)
    
* [Vers quoi nous nous dirigeons ensuite](#heading-vers-quoi-nous-nous-dirigeons-ensuite)
    
* [Conclusion : Construire un avenir inclusif avec l'IA](#heading-conclusion-construire-un-avenir-inclusif-avec-lia)
    

## Ce que nous avons accompli jusqu'à présent

Ces dernières années ont montré comment l'IA peut rendre les classes plus inclusives lorsque nous nous concentrons sur l'accessibilité. Les développeurs, les éducateurs et les chercheurs expérimentent déjà des outils qui comblent les lacunes de communication.

Dans [mon premier tutoriel freeCodeCamp](https://www.freecodecamp.org/news/create-a-real-time-gesture-to-text-translator/), j'ai construit un traducteur geste-vers-texte en utilisant MediaPipe. Ce projet a démontré comment la vision par ordinateur peut suivre les mouvements de la main et les convertir en texte en temps réel. Pour les apprenants qui comptent sur les gestes, ce type de système peut constituer une passerelle vers la participation.

Voici un exemple simplifié de la façon dont MediaPipe détecte les points de repère (landmarks) de la main :

```python
import mediapipe as mp
import cv2

# Initialiser MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Commencer la capture vidéo depuis la webcam
cap = cv2.VideoCapture(0)

# Capturer une image de la vidéo
ret, frame = cap.read()

# Traiter l'image pour détecter les points de repère de la main
results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# Afficher les points de repère détectés
print("Hand landmarks:", results.multi_hand_landmarks)
```

Ce petit bout de code montre comment MediaPipe traite une image vidéo et extrait les points de repère de la main. À partir de là, vous pouvez classifier les gestes et les mapper à du texte.

👉 Vous pouvez explorer le projet complet sur [GitHub](https://github.com/tayo4christ/Gesture_Article) ou lire le tutoriel complet sur [freeCodeCamp](https://www.freecodecamp.org/news/create-a-real-time-gesture-to-text-translator/).

Dans un autre [article de freeCodeCamp](https://www.freecodecamp.org/news/build-ai-accessibility-tools-with-python/), j'ai démontré comment construire des outils d'accessibilité IA avec Python, tels que la reconnaissance vocale et la synthèse vocale. Ces projets ont fourni aux lecteurs une base pour construire leurs propres outils inclusifs, et vous pouvez trouver le code source complet dans le [repository](https://github.com/tayo4christ/inclusive-ai-toolkit).

Au-delà de ces projets individuels, le domaine plus large a également réalisé des progrès significatifs. Les avancées dans la reconnaissance de la langue des signes ont amélioré la précision de la capture des formes de mains et des mouvements complexes. Les systèmes de synthèse vocale sont devenus plus naturels et adaptatifs, donnant aux utilisateurs des voix plus proches de la parole humaine. Les applications d'accessibilité mobiles et de bureau ont apporté ces capacités dans les salles de classe quotidiennes.

Ces accomplissements sont encourageants, mais ils restent limités. La plupart des outils d'aujourd'hui sont encore conçus pour un mode unique de communication. Un système peut fonctionner pour les gestes, ou pour la parole, ou pour le texte, mais pas tous ensemble.

L'étape suivante est claire : nous avons besoin d'outils d'IA multimodaux et adaptatifs capables de mélanger gestes, parole et feedback dans des systèmes unifiés. C'est là que se trouvent les opportunités les plus passionnantes en matière d'accessibilité, et c'est ce vers quoi nous allons nous tourner maintenant.

![Systèmes isolés vs multimodaux](https://github.com/tayo4christ/ai-accessibility-articles-assets/blob/main/single-vs-multimodal.png?raw=true align="left")

*Figure 1 : Comparaison des systèmes à modalité unique isolés avec les systèmes d'IA multimodaux unifiés.*

## Étude de cas 1 : Traduire le Makaton en Anglais

L'un de mes premiers projets dans ce domaine portait sur la traduction du Makaton vers l'Anglais.

Le Makaton est un programme linguistique qui utilise des signes et des symboles pour aider les personnes ayant des difficultés de parole et de langage. Il est largement utilisé dans les classes où les apprenants ne s'appuient pas entièrement sur la parole. Le défi est que, pendant qu'un apprenant communique en Makaton, ses enseignants et ses pairs travaillent souvent en anglais, ce qui crée un fossé de communication.

### Le Workflow de l'IA

Le système suivait un pipeline clair :

*Entrée Caméra → Détection de Points de Repère de Main → Classification de Geste → Sortie de Traduction Anglaise*

![Workflow Makaton](https://github.com/tayo4christ/ai-accessibility-articles-assets/blob/main/makaton-workflow.png?raw=true align="left")

*Figure 2 : Workflow IA pour la traduction des gestes Makaton en anglais.*

* **Entrée Caméra** : capture le signe Makaton de l'apprenant.
    
* **Détection de Points de Repère de Main** : une bibliothèque de vision telle que MediaPipe ou OpenCV identifie la position des doigts et des mains.
    
* **Classification de Geste** : un modèle de Machine Learning entraîné classifie quel signe Makaton a été fait.
    
* **Sortie de Traduction Anglaise** : le système mappe ce geste à son mot ou sa phrase en anglais et l'affiche.
    

### Exemple en Python

Voici une version simplifiée de ce à quoi ce workflow pourrait ressembler en code :

```python
# Étape 1 : Capturer l'entrée
frame = camera.read()

# Étape 2 : Détecter les points de repère de la main
landmarks = mediapipe.process(frame)

# Étape 3 : Classifier le geste
gesture = gesture_model.predict(landmarks)

# Étape 4 : Traduire en anglais
translation_map = {
    "hello_sign": "Hello",
    "thank_you_sign": "Thank you"
}
text = translation_map.get(gesture, "Unknown sign")

print("Makaton sign:", gesture, " -> English:", text)
```

C'est un exemple simplifié, mais il montre l'idée centrale : mapper les gestes au sens, puis faire le pont entre ce sens et l'anglais.

### Pourquoi c'est important

Imaginez un élève signant *merci* en Makaton et le système affichant instantanément les mots à l'écran. Les enseignants peuvent vérifier la compréhension, les pairs peuvent répondre naturellement, et la contribution de l'apprenant devient visible pour tous.

Le point clé à retenir est que l'IA peut faire le lien entre les langues basées sur des symboles et des gestes et la communication parlée et écrite conventionnelle. Au lieu de forcer les apprenants à s'adapter à des systèmes rigides, nous pouvons concevoir des systèmes qui s'adaptent à la façon dont ils communiquent déjà.

## Étude de cas 2 : Prototype AURA (Assistant vocal adaptatif)

Un autre projet sur lequel j'ai travaillé s'appelle [**AURA**](https://aura-apraxia-aac-a8qejouwasaqequrhetbfw.streamlit.app/), l'*Apraxia of Speech Adaptive Understanding and Relearning Assistant*. L'idée était de concevoir un système qui non seulement reconnaît la parole, mais soutient également les apprenants souffrant de troubles de la parole en détectant les erreurs, en adaptant le feedback et en proposant des alternatives multimodales.

### Le Défi

La plupart des systèmes de reconnaissance vocale commerciaux échouent lorsque la parole d'une personne ne suit pas les modèles typiques. C'est particulièrement vrai pour les personnes souffrant d'apraxie de la parole, où les difficultés de planification motrice rendent la prononciation incohérente. Le résultat est une reconnaissance erronée fréquente, de la frustration et l'exclusion des outils qui reposent sur l'entrée vocale.

### Le Workflow de l'IA

Le prototype AURA utilisait une architecture en couches :

*Entrée vocale → Wav2Vec2 (affiné pour la parole désordonnée) → Détection d'erreurs CNN + BiLSTM → Feedback par Apprentissage par Renforcement → Sortie multimodale (Parole + Geste)*

![Workflow AURA](https://github.com/tayo4christ/ai-accessibility-articles-assets/blob/main/aura-workflow.png?raw=true align="left")

*Figure 3 : Workflow du prototype AURA, combinant parole, détection d'erreurs, feedback adaptatif et sorties multimodales.*

* **Reconnaissance vocale Wav2Vec2** : affinée (fine-tuned) sur la parole désordonnée pour améliorer la précision de la transcription.
    
* **Modèle CNN + BiLSTM** : classifie les erreurs d'articulation ou phonologiques en temps réel.
    
* **Moteur d'Apprentissage par Renforcement** : adapte les boucles de rétroaction pour que les suggestions de thérapie s'améliorent à mesure que l'apprenant progresse.
    
* **Entrée multimodale Geste-vers-Parole** : lorsque la parole est trop difficile, les gestes MediaPipe peuvent être utilisés pour déclencher des sorties vocales.
    
* **Interface Streamlit** : intègre le tout dans une application accessible unique pour les tests.
    

Voici une vue simplifiée de la structure d'un module de détection d'erreurs :

```python
# Exemple : Classification d'erreurs utilisant CNN + BiLSTM
import torch
import torch.nn as nn

# Définir le modèle ErrorClassifier
class ErrorClassifier(nn.Module):
    def __init__(self):
        super(ErrorClassifier, self).__init__()
        self.cnn = nn.Conv1d(in_channels=40, out_channels=64, kernel_size=3)
        self.lstm = nn.LSTM(64, 128, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(256, 3)  # Classes de sortie : ex. correct, substitution, omission

    def forward(self, x):
        x = self.cnn(x)
        x, _ = self.lstm(x)
        return self.fc(x[:, -1, :])

# Instancier le modèle
model = ErrorClassifier()
```

Cet extrait montre le cœur du pipeline de détection d'erreurs : la combinaison de couches CNN pour l'extraction de caractéristiques avec des BiLSTM pour la modélisation de séquences. Le modèle peut signaler les erreurs d'articulation, qui guident ensuite la boucle de rétroaction.

### Pourquoi c'est important

Avec AURA, l'objectif n'était pas seulement de reconnaître ce que quelqu'un disait, mais de l'aider à communiquer plus efficacement. Le prototype s'adaptait en temps réel en offrant un feedback correctif, en suggérant des gestes ou en changeant de mode lorsque la parole devenait difficile.

L'idée à retenir est que l'IA peut évoluer d'un simple outil de reconnaissance passif vers un partenaire actif dans l'apprentissage et la communication.

## Vue d'ensemble : Outils d'accessibilité multimodaux

Les deux projets que nous avons explorés, la traduction du Makaton vers l'anglais et la construction du prototype AURA, mettent en lumière une transformation beaucoup plus vaste en cours. La technologie de l'accessibilité s'éloigne des applications isolées à but unique pour s'orienter vers des plateformes multimodales qui regroupent la parole, les gestes, le texte et l'IA adaptative en un seul système fluide.

### Pourquoi ce changement est important

Les avantages de ce changement sont profonds :

* **Une plus grande inclusivité dans les classes** : les apprenants qui s'appuient sur différents modes de communication peuvent participer sur un pied d'égalité.
    
* **Soutien en temps réel** : les systèmes qui détectent les erreurs ou s'adaptent aux gestes donnent aux apprenants un feedback immédiat plutôt que des corrections différées.
    
* **Moins de frustration** : les options multimodales signifient que si un canal échoue (par exemple, la parole), d'autres comme le geste ou le texte peuvent prendre le relais en douceur.
    
* **Confiance et indépendance** : les apprenants s'expriment plus pleinement, sans dépendre lourdement du personnel de soutien ou des interprètes.
    

### Au-delà de la salle de classe

L'impact de l'accessibilité multimodale s'étend à de nombreux secteurs :

* Dans la **santé**, les patients ayant des difficultés de communication peuvent utiliser des assistants IA multimodaux pour exprimer clairement leurs besoins, réduisant ainsi les erreurs de diagnostic et le stress.
    
* Sur le **lieu de travail**, les employés souffrant de troubles de la parole ou moteurs peuvent collaborer efficacement grâce à des outils d'IA adaptatifs.
    
* Dans les **paramètres communautaires**, les individus peuvent participer plus librement aux conversations, aux services et aux plateformes numériques, renforçant ainsi l'inclusion sociale.
    

### Visualiser le changement

![Applications multimodales](https://github.com/tayo4christ/ai-accessibility-articles-assets/blob/main/multimodal-applications.png?raw=true align="left")

## Comment construire un traducteur multimodal Makaton-Anglais (Geste + Parole)

Cette démo combine les deux cas d'utilisation : un outil de classe Makaton vers Anglais et le chemin de parole assistée de type AURA. Il donne la priorité au geste lorsqu'un signe est détecté, se rabat sur la parole s'il ne l'est pas, et produit une sortie anglaise unifiée (avec synthèse vocale optionnelle). Nous nous concentrerons sur la couche de traduction, la fusion multimodale et une interface UI Streamlit simple.

### Structure du projet

```python
makaton_multimodal_demo/
├── .streamlit/
│   └── config.toml 
├── assets/
│   └── README.txt 
├── tests/
│   └── test_fuse.py 
└── streamlit_app.py 
```

La structure fournie ci-dessus présente l'organisation d'un répertoire de projet pour une démo de traducteur Makaton vers Anglais multimodal utilisant Streamlit. Voici une brève explication de chaque composant :

* `makaton_multimodal_demo/` : C'est le répertoire racine du projet.
    
* `.streamlit/` : Ce répertoire contient les fichiers de configuration pour Streamlit, qui est un Framework utilisé pour construire des applications web en Python. Le fichier `config.toml` est optionnel et peut être utilisé pour personnaliser les paramètres de l'application Streamlit.
    
* `assets/` : Ce répertoire est destiné à stocker les modèles ou d'autres fichiers nécessaires au projet. Le `README.txt` sert d'espace réservé pour indiquer où ces fichiers doivent être placés.
    
* `tests/` : Ce répertoire est destiné aux scripts de test. Le fichier `test_`[`fuse.py`](http://fuse.py) contient probablement des tests pour la fonction de fusion, qui fait partie du processus de traduction multimodale.
    
* `streamlit_`[`app.py`](http://app.py) : C'est le fichier principal de l'application où l'application Streamlit est implémentée. Il contient le code qui exécute l'application, gérant l'interface utilisateur et la logique de traduction des gestes Makaton et de la parole en anglais.
    

### Installation et exécution

```bash
# (optionnel) créer et activer un virtualenv
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

L'extrait de code ci-dessus fournit les instructions pour créer et activer un environnement virtuel Python.

1. `python -m venv .venv` : Cette commande crée un nouvel environnement virtuel dans un répertoire nommé `.venv`.
    
2. `.\.venv\Scripts\activate` (Windows) : Cette commande active l'environnement virtuel sur Windows.
    
3. `source .venv/bin/activate` (macOS/Linux) : Cette commande active l'environnement virtuel sur macOS ou Linux.
    

### Installer les dépendances

```python
pip install streamlit opencv-python mediapipe SpeechRecognition gTTS pydub numpy
```

La commande ci-dessus est utilisée pour installer plusieurs packages Python à la fois :

* **streamlit** : Un Framework pour construire des applications web interactives en Python.
    
* **opencv-python** : Fournit OpenCV, une bibliothèque pour les tâches de vision par ordinateur.
    
* **mediapipe** : Une bibliothèque développée par Google pour les solutions de Machine Learning pour les médias en direct, incluant la détection des mains et des visages.
    
* **SpeechRecognition** : Une bibliothèque pour effectuer de la reconnaissance vocale.
    
* **gTTS** : Google Text-to-Speech, pour interfacer avec l'API de synthèse vocale de Google Translate.
    
* **pydub** : Une bibliothèque pour le traitement audio.
    
* **numpy** : Un package fondamental pour le calcul scientifique en Python.
    

### Créer `streamlit_app.py`

```python
# streamlit_app.py
from io import BytesIO
from typing import Optional
import streamlit as st

# Dépendances optionnelles
try:
    import cv2
    import mediapipe as mp
    MP_OK = True
except Exception:
    MP_OK = False

try:
    import speech_recognition as sr
    SR_OK = True
except Exception:
    SR_OK = False

try:
    from gtts import gTTS
    GTTS_OK = True
except Exception:
    GTTS_OK = False

# --- 1) Dictionnaire Makaton minimal (à étendre au besoin)
MAKATON_DICT = {
    "hello_sign": "Bonjour",
    "thank_you_sign": "Merci",
    "help_sign": "Aide",
    "toilet_sign": "Toilettes",
    "stop_sign": "Arrêter",
}

# --- 2) Classificateur de gestes (bouchon pour la démo)
def classify_gesture(landmarks) -> Optional[str]:
    """
    Retourne un label canonique comme 'hello_sign' ou None si inconnu.
    Remplacez ce bouchon par votre modèle entraîné + seuil de confiance.
    """
    return "hello_sign" if landmarks else None

# --- 3) Reconnaissance vocale (chemin de secours)
def transcribe_speech(seconds: int = 3) -> Optional[str]:
    if not SR_OK:
        return None
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("Écoute en cours...")
            audio = r.listen(source, phrase_time_limit=seconds)
        return r.recognize_google(audio, language="fr-FR") # Ajusté pour le français
    except Exception as e:
        st.warning(f"Erreur de reconnaissance vocale : {e}")
        return None

# --- 4) Logique de fusion (geste d'abord, parole en secours)
def fuse(gesture_label: Optional[str], speech_text: Optional[str]) -> str:
    if gesture_label and gesture_label in MAKATON_DICT:
        return MAKATON_DICT[gesture_label]
    if speech_text:
        return speech_text
    return "Aucune entrée détectée"

# --- 5) Optionnel : extraire les points de repère de la main via MediaPipe
def extract_hand_landmarks_from_image(image_bytes: bytes):
    if not MP_OK:
        return None
    try:
        import numpy as np
        np_arr = np.frombuffer(image_bytes, dtype=np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            return None

        mp_hands = mp.solutions.hands
        with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = hands.process(img_rgb)

        if not result.multi_hand_landmarks:
            return None

        hand_landmarks = result.multi_hand_landmarks[0]
        return [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
    except Exception:
        return None

# --- 6) Interface UI Streamlit
st.set_page_config(page_title="Makaton → Français (Démo Multimodale)")
st.title("Makaton → Français (Démo Multimodale)")
st.caption("Combine un traducteur Makaton de classe avec un chemin vocal assisté (style AURA).")

with st.expander("Ce que cette démo montre"):
    st.write(
        "- **Couche de traduction :** petit dictionnaire Makaton extensible.\n"
        "- **Fusion multimodale :** geste prioritaire, parole en secours.\n"
        "- **UI :** une seule page, sortie claire, synthèse vocale optionnelle."
    )

tabs = st.tabs(["Signe Simulé", "Webcam Image Unique (Optionnel)", "À propos"])

# Onglet 1 : Simulé (aucun modèle CV requis)
with tabs[0]:
    st.subheader("Geste Simulé + Parole")
    col1, col2 = st.columns(2)

    with col1:
        simulate = st.selectbox(
            "Choisissez un signe",
            ["", "hello_sign", "thank_you_sign", "help_sign", "toilet_sign", "stop_sign"],
            index=0
        )
        gesture_label = simulate or None

    with col2:
        speech_text = st.session_state.get("speech_text")
        st.write("Parole actuelle :", speech_text or "Aucune")
        if st.button("Transcrire 3s"):
            if SR_OK:
                speech_text = transcribe_speech(3)
                st.session_state["speech_text"] = speech_text
            else:
                st.warning("SpeechRecognition non installé.")

    output = fuse(gesture_label, st.session_state.get("speech_text"))
    st.markdown(f"### Résultat : **{output}**")

    if output and output != "Aucune entrée détectée":
        if st.button("Lire le résultat"):
            if GTTS_OK:
                mp3 = BytesIO()
                try:
                    gTTS(output, lang="fr").write_to_fp(mp3)
                    st.audio(mp3.getvalue(), format="audio/mp3")
                except Exception as e:
                    st.warning(f"Échec TTS : {e}")
            else:
                st.warning("gTTS non installé.")

# Onglet 2 : Capture webcam image unique
with tabs[1]:
    st.subheader("Détection de main image unique (Webcam)")
    if not MP_OK:
        st.warning("Installez MediaPipe + OpenCV pour activer cet onglet.")
    else:
        img = st.camera_input("Capturer une image")
        captured_label = None
        if img is not None:
            landmarks = extract_hand_landmarks_from_image(img.getvalue())
            if landmarks:
                captured_label = classify_gesture(landmarks)
                st.success("Main détectée.")
            else:
                st.info("Aucun point de repère trouvé. Essayez un meilleur éclairage.")

        if st.button("Transcrire 3s (onglet webcam)"):
            st.session_state["speech_text2"] = transcribe_speech(3) if SR_OK else None

        speech_text2 = st.session_state.get("speech_text2")
        st.write("Parole actuelle :", speech_text2 or "Aucune")

        output2 = fuse(captured_label, speech_text2)
        st.markdown(f"### Résultat : **{output2}**")

        if output2 and output2 != "Aucune entrée détectée":
            if st.button("Lire le résultat (onglet webcam)"):
                if GTTS_OK:
                    mp3 = BytesIO()
                    try:
                        gTTS(output2, lang="fr").write_to_fp(mp3)
                        st.audio(mp3.getvalue(), format="audio/mp3")
                    except Exception as e:
                        st.warning(f"Échec TTS : {e}")
                else:
                    st.warning("gTTS non installé.")
```

Ce code crée une application Streamlit qui combine la reconnaissance de gestes et la reconnaissance vocale pour traduire les signes Makaton. Voici comment cela fonctionne :

1. **Dépendances et Configuration** : Le code tente d'importer les dépendances optionnelles pour la détection de gestes, la reconnaissance vocale et la synthèse vocale.
    
2. **Dictionnaire Makaton** : Un dictionnaire minimal qui mappe les signes Makaton à des mots. 
    
3. **Classificateur de Gestes** : Une fonction de substitution (`classify_gesture`) est utilisée pour la démo.
    
4. **Reconnaissance Vocale** : La fonction `transcribe_speech` utilise la bibliothèque SpeechRecognition comme solution de secours.
    
5. **Logique de Fusion** : La fonction `fuse` donne la priorité au geste sur la parole.
    
6. **Extraction de Points de Repère** : Utilise MediaPipe pour extraire les coordonnées de la main d'une image.
    
7. **Interface UI Streamlit** : Propose des onglets pour simuler les signes ou utiliser une webcam.

### Exécution

```bash
streamlit run .\streamlit_app.py
```

La commande ci-dessus lance l'application Streamlit, ouvrant le script dans un navigateur web pour interagir avec l'interface.

![Interface de l'application](https://github.com/tayo4christ/ai-accessibility-articles-assets/blob/8117234b9dc032aa0f4ff32abad92e7ad3344b81/ui-home-simulated-tab.jpg?raw=1 align="left")

*Figure — Interface de l'application : l'onglet Signe Simulé avant toute entrée.*

![Signe simulé hello_sign](https://github.com/tayo4christ/ai-accessibility-articles-assets/blob/8117234b9dc032aa0f4ff32abad92e7ad3344b81/ui-simulated-hello-output.jpg?raw=1 align="left")

*Figure — La sélection de* `hello_sign` *produit "Résultat : Bonjour".*

## Aperçu du projet

Vous avez développé un traducteur multimodal qui intègre à la fois la reconnaissance de gestes (signes Makaton) et la reconnaissance vocale pour produire une sortie unifiée. Le système est conçu pour donner la priorité à l'entrée gestuelle, en utilisant la parole comme solution de secours.

**Interface Utilisateur**

L'application est construite avec Streamlit, comprenant deux onglets principaux :

* **Onglet Signe Simulé** : Permet aux utilisateurs de simuler des gestes sans nécessiter de capacités de vision par ordinateur (CV).
    
* **Onglet Webcam Image Unique** : Utilise optionnellement une webcam pour traiter une image pour la détection de gestes.
    

**Intégration des cas d'utilisation**

* **Traduction Makaton-Français** : Dans un cadre scolaire, les signes Makaton détectés sont traduits en phrases courtes, facilitant la communication.
    
* **Chemin assisté de style AURA** : Si aucun geste n'est détecté, le système s'appuie sur l'entrée vocale pour générer une sortie.
    

**Limites de conception**

* Le classificateur de gestes est actuellement un bouchon (placeholder) et devrait être remplacé par un modèle entraîné avec un seuil de confiance.
    
* Le dictionnaire Makaton est minimal et peut être étendu avec plus de phrases et de modèles.
    
* Le composant de reconnaissance vocale utilise un outil de base. Pour plus de robustesse, envisagez des modèles avancés comme Wav2Vec2.
    

**Extensions suggérées**

* Implémenter un seuil de confiance pour afficher les deux entrées (geste et parole) en cas d'incertitude.
    
* Étendre le dictionnaire pour supporter des modèles à emplacements (ex: "Je veux [objet]").
    
* Introduire un interrupteur pour choisir la priorité entre parole et geste.
    
* Activer la journalisation des sorties pour les enseignants avec export en CSV.
    

**Conseils de dépannage**

* En cas d'erreurs de microphone, vérifiez l'installation de `pyaudio`.
    
* Si la webcam n'est pas détectée, vérifiez les permissions du navigateur.
    

Lien vers le code complet : [Multimodal_Makaton](https://github.com/tayo4christ/makaton-multimodal-demo/tree/main/makaton_multimodal_demo)

## Défis et considérations éthiques

Bien que la promesse des outils d'accessibilité multimodaux soit passionnante, les construire de manière responsable nécessite de confronter plusieurs défis techniques et éthiques.

### Rareté des données

L'entraînement des systèmes d'IA nécessite de grands jeux de données diversifiés. Mais pour la parole désordonnée ou les systèmes comme le Makaton, les données sont limitées. Sans assez d'exemples, les modèles risquent d'être imprécis ou biaisés. La collecte de données doit se faire de manière éthique, avec consentement.

### Équité et Inclusion

Les systèmes d'IA fonctionnent souvent mieux pour certains groupes que pour d'autres. Un modèle entraîné sur des locuteurs fluides peut échouer pour ceux ayant des accents forts ou des difficultés de parole. L'équité signifie concevoir des modèles qui fonctionnent pour toutes les capacités, accents et cultures.

### Confidentialité et Sécurité

Les données vocales et vidéo sont sensibles, surtout dans les écoles. La protection de ces données est une exigence. Les systèmes doivent anonymiser ou crypter les enregistrements et les stocker de manière sécurisée.

### Accessibilité des outils eux-mêmes

Ironiquement, de nombreux "outils d'accessibilité" restent inaccessibles car trop chers ou complexes. Pour que l'IA réduise réellement les barrières, les solutions doivent être abordables, légères et faciles à installer dans de vraies classes.

## Vers quoi nous nous dirigeons ensuite

L'avenir des outils d'accessibilité IA est spéculatif mais prometteur. Ce que nous avons maintenant sont des prototypes ; ce qui nous attend sont des outils qui pourraient remodeler la société.

### Traduction Makaton Multilingue

Une direction prometteuse est la capacité de traduire le Makaton vers plusieurs langues. Un apprenant au Royaume-Uni pourrait signer en Makaton et voir sa contribution apparaître en français, en espagnol ou en yoruba, ouvrant les classes internationales.

### Tuteurs IA avec adaptation dynamique

Imaginez un assistant de classe capable de changer de mode en temps réel : si l'apprenant fatigue des gestes, l'IA propose des options basées sur des symboles, s'adaptant continuellement aux forces de chaque élève.

### Dispositifs multimodaux portables (Wearables)

Des lunettes pourraient capturer les gestes et superposer du texte, tandis que des oreillettes pourraient traduire une parole désordonnée en un audio clair pour les pairs. L'accessibilité deviendrait portable et omniprésente.

### Un impact plus large

Ces innovations s'alignent sur les Objectifs de Développement Durable (ODD) des Nations Unies, notamment l'**Éducation de Qualité (Objectif 4)** et la **Réduction des Inégalités (Objectif 10)**.

## Conclusion : Construire un avenir inclusif avec l'IA

Les outils d'accessibilité IA ne sont plus de simples options. Ils deviennent des moteurs essentiels de l'inclusion dans l'éducation, la santé et le travail.

Le passage des systèmes de reconnaissance de gestes précoces aux prototypes multimodaux comme la traduction Makaton et AURA montre ce qui est possible lorsque la technologie est conçue autour de l'humain. Ces innovations brisent les barrières de communication et ouvrent de nouvelles opportunités pour les apprenants souvent laissés en marge.

Mais cet avenir n'est pas automatique. Il dépend de nos choix en tant que développeurs, éducateurs et décideurs. La vision est claire : un monde où chaque apprenant, quelle que soit sa capacité, peut s'exprimer pleinement et participer avec confiance.

**L'avenir de l'éducation est inclusif et, avec un design réfléchi, l'IA peut nous aider à y parvenir.**