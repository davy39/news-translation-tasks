---
title: Comment utiliser les Transformers pour la reconnaissance de gestes en temps
  réel
subtitle: ''
author: OMOTAYO OMOYEMI
co_authors: []
series: null
date: '2025-10-06T13:39:30.945Z'
originalURL: https://freecodecamp.org/news/using-transformers-for-real-time-gesture-recognition
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759757931295/5f19fd4e-93c0-4bd7-a75c-a7858e061ecd.png
tags:
- name: Computer Vision
  slug: computer-vision
- name: transformers
  slug: transformers
- name: pytorch
  slug: pytorch
- name: ONNX
  slug: onnx
- name: gradio
  slug: gradio
- name: Machine Learning
  slug: machine-learning
- name: Deep Learning
  slug: deep-learning
- name: Gesture Recognition
  slug: gesture-recognition
- name: Accessibility
  slug: accessibility
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser les Transformers pour la reconnaissance de gestes en temps
  réel
seo_desc: Gesture and sign recognition is a growing field in computer vision, powering
  accessibility tools and natural user interfaces. Most beginner projects rely on
  hand landmarks or small CNNs, but these often miss the bigger picture because gestures
  are no...
---

La reconnaissance de gestes et de signes est un domaine en pleine croissance dans la vision par ordinateur, alimentant les outils d'accessibilité et les interfaces utilisateur naturelles. La plupart des projets pour débutants s'appuient sur des points de repère de la main (landmarks) ou de petits CNN, mais ceux-ci passent souvent à côté de la vision d'ensemble car les gestes ne sont pas des images statiques. Ils se déroulent plutôt dans le temps. Pour construire des systèmes plus robustes et en temps réel, nous avons besoin de modèles capables de capturer à la fois les détails spatiaux et le contexte temporel.

C'est là que les Transformers interviennent. Conçus à l'origine pour le langage, ils sont devenus l'état de l'art dans les tâches de vision grâce à des modèles comme le Vision Transformer (ViT) et des variantes axées sur la vidéo telles que TimeSformer.

Dans ce tutoriel, nous utiliserons une architecture Transformer pour créer un outil de reconnaissance de gestes léger et en temps réel, optimisé pour de petits jeux de données et déployable sur la webcam d'un ordinateur portable standard.

## Table des matières

* [Pourquoi des Transformers pour les gestes ?](#heading-pourquoi-des-transformers-pour-les-gestes)
    
* [Ce que vous allez apprendre](#heading-ce-que-vous-allez-apprendre)
    
* [Pré-requis](#heading-pre-requis)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Générer un jeu de données de gestes](#heading-generer-un-jeu-de-donnees-de-gestes)
    
* [Option 1 : Générer un jeu de données synthétique](#heading-option-1-generer-un-jeu-de-donnees-synthetique)
    
* [Script d'entraînement :](#heading-script-dentrainement-trainpy) [train.py](http://train.py)
    
* [Exporter le modèle vers ONNX](#heading-exporter-le-modele-vers-onnx)
    
* [Évaluer la précision et la latence](#heading-evaluer-la-precision-et-la-latence)
    
* [Option 2 : Utiliser de petits échantillons de jeux de données de gestes publics](#heading-option-2-utiliser-de-petits-echantillons-de-jeux-de-donnees-de-gestes-publics)
    
* [Notes sur l'accessibilité et limites éthiques](#heading-notes-sur-laccessibilite-et-limites-ethiques)
    
* [Prochaines étapes](#heading-prochaines-etapes)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi des Transformers pour les gestes ?

Les Transformers sont puissants car ils utilisent l'auto-attention pour modéliser les relations au sein d'une séquence. Pour les gestes, cela signifie que le modèle ne voit pas seulement des images isolées, mais apprend également comment les mouvements évoluent dans le temps. Un signe de la main, par exemple, ne se distingue d'une main levée que lorsqu'il est visualisé comme une séquence.

Les Vision Transformers traitent les images comme des patchs, tandis que les Transformers vidéo étendent cela à plusieurs images avec une attention temporelle. Même une approche simple, comme l'application de ViT à chaque image et le regroupement (pooling) temporel, peut surpasser les méthodes traditionnelles basées sur les CNN pour les petits jeux de données.

Combinés aux modèles pré-entraînés de Hugging Face et à ONNX Runtime pour l'optimisation, les Transformers permettent de s'entraîner sur un jeu de données modeste tout en obtenant une reconnaissance fluide en temps réel.

## Ce que vous allez apprendre

Dans ce tutoriel, vous allez construire un système de reconnaissance de gestes à l'aide de Transformers. À la fin, vous saurez comment :

* Créer (ou enregistrer) un minuscule jeu de données de gestes
    
* Entraîner un Vision Transformer (ViT) avec pooling temporel
    
* Exporter le modèle vers ONNX pour une inférence plus rapide
    
* Construire une application Gradio en temps réel qui classifie les gestes de votre webcam
    
* Évaluer la précision et la latence de votre modèle avec des scripts simples
    
* Comprendre le potentiel d'accessibilité et les limites éthiques de la reconnaissance de gestes
    

## Pré-requis

Pour suivre ce tutoriel, vous devriez avoir :

* Des connaissances de base en Python (fonctions, scripts, environnements virtuels)
    
* Une familiarité avec PyTorch (tenseurs, jeux de données, boucles d'entraînement) – utile mais pas obligatoire
    
* Python 3.8+ installé sur votre système
    
* Une webcam (pour la démo en direct dans Gradio)
    
* Optionnel : accès à un GPU (l'entraînement sur CPU fonctionne, mais est plus lent)
    

## Configuration du projet

Créez un nouveau dossier de projet et installez les bibliothèques requises.

```bash
# Create a new project directory and navigate into it
mkdir transformer-gesture && cd transformer-gesture

# Set up a Python virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

L'extrait de code fourni est un ensemble de commandes pour configurer un nouveau projet Python avec un environnement virtuel. Voici le détail de chaque partie :

1. `mkdir transformer-gesture && cd transformer-gesture` : Cette commande crée un nouveau répertoire nommé "transformer-gesture" puis y pénètre.
    
2. `python -m venv .venv` : Cette commande crée un nouvel environnement virtuel dans le répertoire courant. L'environnement virtuel est stocké dans un dossier nommé ".venv".
    
3. Activation de l'environnement virtuel :
    
    * Pour Windows PowerShell, vous pouvez utiliser `.venv\Scripts\Activate.ps1` pour activer l'environnement virtuel.
        
    * Pour macOS/Linux, utilisez `source .venv/bin/activate` pour activer l'environnement virtuel.
        

L'activation d'un environnement virtuel garantit que l'interpréteur Python et tous les packages que vous installez sont isolés pour ce projet spécifique, évitant ainsi les conflits avec d'autres projets ou les packages système.

Créez un fichier `requirements.txt` :

```plaintext
torch>=2.0
torchvision
torchaudio
timm
huggingface_hub

onnx
onnxruntime

gradio

numpy
opencv-python
pillow

matplotlib
seaborn
scikit-learn
```

La liste fournie est un ensemble de dépendances de packages typiquement trouvées dans un fichier `requirements.txt` pour un projet Python. Voici une brève explication de chaque package :

1. **torch>=2.0** : PyTorch est un Framework de deep learning open-source populaire qui offre une plateforme flexible et efficace pour construire et entraîner des réseaux de neurones.
    
2. **torchvision** : Cette bibliothèque fait partie de l'écosystème PyTorch et fournit des outils pour les tâches de vision par ordinateur.
    
3. **torchaudio** : Également partie de l'écosystème PyTorch, Torchaudio fournit des outils de traitement audio.
    
4. **timm** : La bibliothèque PyTorch Image Models (timm) propose une collection de modèles pré-entraînés et d'utilitaires pour la vision par ordinateur.
    
5. **huggingface_hub** : Cette bibliothèque permet d'accéder facilement aux modèles et jeux de données hébergés sur le Hugging Face Hub.
    
6. **onnx** : Le format Open Neural Network Exchange (ONNX) est utilisé pour représenter les modèles de machine learning, permettant l'interopérabilité entre différents Frameworks.
    
7. **onnxruntime** : Il s'agit d'un moteur d'exécution haute performance pour exécuter des modèles ONNX.
    
8. **gradio** : Gradio est une bibliothèque pour créer des interfaces utilisateur pour les modèles de machine learning.
    
9. **numpy** : Un package fondamental pour le calcul numérique en Python.
    
10. **opencv-python** : OpenCV est une bibliothèque pour la vision par ordinateur et le traitement d'images.
    
11. **pillow** : Un fork de la Python Imaging Library (PIL), Pillow fournit des outils pour manipuler des images.
    
12. **matplotlib** : Une bibliothèque de traçage pour Python.
    
13. **seaborn** : Basé sur Matplotlib, Seaborn fournit une interface de haut niveau pour dessiner des graphiques statistiques attrayants.
    
14. **scikit-learn** : Une bibliothèque de machine learning en Python qui fournit des outils simples et efficaces pour l'analyse et la modélisation des données.
    

Installez les dépendances :

```bash
pip install -r requirements.txt
```

La commande `pip install -r requirements.txt` est utilisée pour installer tous les packages Python listés dans un fichier nommé `requirements.txt`. C'est une pratique courante dans les projets Python pour gérer et partager facilement les dépendances.

## Générer un jeu de données de gestes

Pour entraîner notre outil de reconnaissance de gestes basé sur Transformer, nous avons besoin de données. Au lieu de télécharger un énorme jeu de données, nous allons commencer par un minuscule jeu de données synthétique que vous pouvez générer en quelques secondes. Cela rend le tutoriel léger et garantit que tout le monde peut suivre sans avoir à gérer des téléchargements de plusieurs gigaoctets.

## Option 1 : Générer un jeu de données synthétique

Nous utiliserons un petit script Python qui crée de courts clips `.mp4` d'une boîte colorée en mouvement (ou immobile). Chaque classe représente un geste :

* **swipe_left** – la boîte se déplace de droite à gauche
    
* **swipe_right** – la boîte se déplace de gauche à droite
    
* **stop** – la boîte reste immobile au centre
    

Enregistrez ce script sous le nom `generate_synthetic_gestures.py` à la racine de votre projet :

```python
import os, cv2, numpy as np, random, argparse

def ensure_dir(p): os.makedirs(p, exist_ok=True)

def make_clip(mode, out_path, seconds=1.5, fps=16, size=224, box_size=60, seed=0, codec="mp4v"):
    rng = random.Random(seed)
    frames = int(seconds * fps)
    H = W = size

    # background + box color
    bg_val = rng.randint(160, 220)
    bg = np.full((H, W, 3), bg_val, dtype=np.uint8)
    color = (rng.randint(20, 80), rng.randint(20, 80), rng.randint(20, 80))

    # path of motion
    y = rng.randint(40, H - 40 - box_size)
    if mode == "swipe_left":
        x_start, x_end = W - 20 - box_size, 20
    elif mode == "swipe_right":
        x_start, x_end = 20, W - 20 - box_size
    elif mode == "stop":
        x_start = x_end = (W - box_size) // 2
    else:
        raise ValueError(f"Unknown mode: {mode}")

    fourcc = cv2.VideoWriter_fourcc(*codec)
    vw = cv2.VideoWriter(out_path, fourcc, fps, (W, H))
    if not vw.isOpened():
        raise RuntimeError(
            f"Could not open VideoWriter with codec '{codec}'. "
            "Try --codec XVID and use .avi extension, e.g. out.avi"
        )

    for t in range(frames):
        alpha = t / max(1, frames - 1)
        x = int((1 - alpha) * x_start + alpha * x_end)
        # small jitter to avoid being too synthetic
        jitter_x, jitter_y = rng.randint(-2, 2), rng.randint(-2, 2)
        frame = bg.copy()
        cv2.rectangle(frame, (x + jitter_x, y + jitter_y),
                      (x + jitter_x + box_size, y + jitter_y + box_size),
                      color, thickness=-1)
        # overlay text
        cv2.putText(frame, mode, (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, mode, (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
        vw.write(frame)

    vw.release()

def write_labels(labels, out_dir):
    with open(os.path.join(out_dir, "labels.txt"), "w", encoding="utf-8") as f:
        for c in labels:
            f.write(c + "\n")

def main():
    ap = argparse.ArgumentParser(description="Generate a tiny synthetic gesture dataset.")
    ap.add_argument("--out", default="data", help="Output directory (default: data)")
    ap.add_argument("--classes", nargs="+",
                    default=["swipe_left", "swipe_right", "stop"],
                    help="Class names (default: swipe_left swipe_right stop)")
    ap.add_argument("--clips", type=int, default=16, help="Clips per class (default: 16)")
    ap.add_argument("--seconds", type=float, default=1.5, help="Seconds per clip (default: 1.5)")
    ap.add_argument("--fps", type=int, default=16, help="Frames per second (default: 16)")
    ap.add_argument("--size", type=int, default=224, help="Frame size WxH (default: 224)")
    ap.add_argument("--box", type=int, default=60, help="Box size (default: 60)")
    ap.add_argument("--codec", default="mp4v", help="Codec fourcc (mp4v or XVID)")
    ap.add_argument("--ext", default=".mp4", help="File extension (.mp4 or .avi)")
    args = ap.parse_args()

    ensure_dir(args.out)
    write_labels(args.classes, ".")  # writes labels.txt to project root

    print(f"Generating synthetic dataset -> {args.out}")
    for cls in args.classes:
        cls_dir = os.path.join(args.out, cls)
        ensure_dir(cls_dir)
        mode = "stop" if cls == "stop" else ("swipe_left" if "left" in cls else ("swipe_right" if "right" in cls else "stop"))
        for i in range(args.clips):
            filename = os.path.join(cls_dir, f"{cls}_{i+1:03d}{args.ext}")
            make_clip(
                mode=mode,
                out_path=filename,
                seconds=args.seconds,
                fps=args.fps,
                size=args.size,
                box_size=args.box,
                seed=i + 1,
                codec=args.codec
            )
        print(f"  {cls}: {args.clips} clips")

    print("Done. You can now run: python train.py, python export_onnx.py, python app.py")

if __name__ == "__main__":
    main()
```

Le script génère un jeu de données de gestes synthétiques en créant des clips vidéo d'une boîte colorée mobile ou stationnaire, simulant des gestes comme "balayer vers la gauche", "balayer vers la droite" et "stop".

Maintenant, exécutez-le dans votre environnement virtuel :

```bash
python generate_synthetic_gestures.py --out data --clips 16 --seconds 1.5
```

La commande ci-dessus génère un jeu de données synthétique avec 16 clips par geste, chacun durant 1,5 seconde, et enregistre le résultat dans un répertoire nommé "data".

Cela crée une structure comme celle-ci :

```plaintext
data/
  swipe_left/*.mp4
  swipe_right/*.mp4
  stop/*.mp4
labels.txt
```

Chaque dossier contient de courts clips d'une boîte en mouvement (ou immobile) qui simulent des gestes. C'est parfait pour tester le pipeline.

### Script d'entraînement : `train.py`

Maintenant que nous avons notre jeu de données, affinons (fine-tune) un Vision Transformer avec pooling temporel. Ce modèle applique ViT image par image, calcule la moyenne des embeddings dans le temps et entraîne une tête de classification sur vos gestes.

Voici le script d'entraînement complet :

```python
# train.py
import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import DataLoader
import timm
from dataset import GestureClips, read_labels

class ViTTemporal(nn.Module):
    """Frame-wise ViT encoder -> mean pool over time -> linear head."""
    def __init__(self, num_classes, vit_name="vit_tiny_patch16_224"):
        super().__init__()
        self.vit = timm.create_model(vit_name, pretrained=True, num_classes=0, global_pool="avg")
        feat_dim = self.vit.num_features
        self.head = nn.Linear(feat_dim, num_classes)

    def forward(self, x):  # x: (B,T,C,H,W)
        B, T, C, H, W = x.shape
        x = x.view(B * T, C, H, W)
        feats = self.vit(x)                  # (B*T, D)
        feats = feats.view(B, T, -1).mean(dim=1)  # (B, D)
        return self.head(feats)

def train():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    labels, _ = read_labels("labels.txt")
    n_classes = len(labels)

    train_ds = GestureClips(train=True)
    val_ds   = GestureClips(train=False)
    print(f"Train clips: {len(train_ds)} | Val clips: {len(val_ds)}")

    # Windows/CPU friendly
    train_dl = DataLoader(train_ds, batch_size=2, shuffle=True,  num_workers=0, pin_memory=False)
    val_dl   = DataLoader(val_ds,   batch_size=2, shuffle=False, num_workers=0, pin_memory=False)

    model = ViTTemporal(num_classes=n_classes).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.05)

    best_acc = 0.0
    epochs = 5
    for epoch in range(1, epochs + 1):
        # ---- Train ----
        model.train()
        total, correct, loss_sum = 0, 0, 0.0
        for x, y in train_dl:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()

            loss_sum += loss.item() * x.size(0)
            correct += (logits.argmax(1) == y).sum().item()
            total += x.size(0)

        train_acc = correct / total if total else 0.0
        train_loss = loss_sum / total if total else 0.0

        # ---- Validate ----
        model.eval()
        vtotal, vcorrect = 0, 0
        with torch.no_grad():
            for x, y in val_dl:
                x, y = x.to(device), y.to(device)
                vcorrect += (model(x).argmax(1) == y).sum().item()
                vtotal += x.size(0)
        val_acc = vcorrect / vtotal if vtotal else 0.0

        print(f"Epoch {epoch:02d} | train_loss {train_loss:.4f} "
              f"| train_acc {train_acc:.3f} | val_acc {val_acc:.3f}")

        if val_acc > best_acc:
            best_acc = val_acc
            torch.save(model.state_dict(), "vit_temporal_best.pt")

    print("Best val acc:", best_acc)

if __name__ == "__main__":
    train()
```

L'exécution de la commande `python train.py` lance le processus d'entraînement. Voici ce qui se passe :

1. **Chargement du jeu de données depuis data/** : Le script accède au jeu de données de gestes.
2. **Affinage d'un Vision Transformer pré-entraîné** : Le script prend un modèle ViT pré-entraîné et l'adapte à vos gestes spécifiques.
3. **Sauvegarde du meilleur point de contrôle sous vit_temporal_best.pt** : La version la plus performante du modèle est sauvegardée.

#### À quoi ressemble l'entraînement

Vous devriez voir des journaux (logs) similaires à ceux-ci :

```plaintext
Train clips: 38 | Val clips: 10
Epoch 01 | train_loss 1.4508 | train_acc 0.395 | val_acc 0.200
Epoch 02 | train_loss 1.2466 | train_acc 0.263 | val_acc 0.200
Epoch 03 | train_loss 1.1361 | train_acc 0.368 | val_acc 0.200
Best val acc: 0.200
```

Ne vous inquiétez pas si votre précision est faible au début, c'est normal avec le jeu de données synthétique. L'essentiel est de prouver que le pipeline Transformer fonctionne. Vous pourrez améliorer les résultats plus tard en :

* Ajoutant plus de clips par classe
* Augmentant le nombre d'époques d'entraînement
* Passant à de vrais gestes enregistrés

![Training logs](https://github.com/tayo4christ/transformer-gesture/blob/07c7071bdb17bc08585baeb60d787eadc3936ef5/images/training-logs.png?raw=true align="left")

Figure 1. Exemple de journaux d'entraînement de `train.py`.

### Exporter le modèle vers ONNX

Pour rendre notre modèle plus facile à exécuter en temps réel (et plus léger sur le CPU), nous allons l'exporter au format ONNX.

**Note :** ONNX (Open Neural Network Exchange) est un format open-source conçu pour faciliter l'échange de modèles de deep learning entre différents Frameworks. Il permet d'entraîner un modèle dans un Framework (comme PyTorch) et de le déployer dans un autre.

Créez un fichier nommé `export_onnx.py` :

```python
import torch
from train import ViTTemporal
from dataset import read_labels

labels, _ = read_labels("labels.txt")
n_classes = len(labels)

# Load trained model
model = ViTTemporal(num_classes=n_classes)
model.load_state_dict(torch.load("vit_temporal_best.pt", map_location="cpu"))
model.eval()

# Dummy input: batch=1, 16 frames, 3x224x224
dummy = torch.randn(1, 16, 3, 224, 224)

# Export
torch.onnx.export(
    model, dummy, "vit_temporal.onnx",
    input_names=["video"], output_names=["logits"],
    dynamic_axes={"video": {0: "batch"}},
    opset_version=13
)

print("Exported vit_temporal.onnx")
```

Exécutez-le avec `python export_onnx.py`.

Cela génère un fichier `vit_temporal.onnx`. ONNX nous permet d'utiliser onnxruntime, qui est beaucoup plus rapide pour l'inférence.

Créez un fichier nommé `app.py` :

```python
import os, tempfile, cv2, torch, onnxruntime, numpy as np
import gradio as gr
from dataset import read_labels

T = 16
SIZE = 224
MODEL_PATH = "vit_temporal.onnx"

labels, _ = read_labels("labels.txt")

# --- ONNX session + auto-detect names ---
ort_session = onnxruntime.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])
# detect first input and first output names to avoid mismatches
INPUT_NAME = ort_session.get_inputs()[0].name   # e.g. "input" or "video"
OUTPUT_NAME = ort_session.get_outputs()[0].name # e.g. "logits" or something else

def preprocess_clip(frames_rgb):
    if len(frames_rgb) == 0:
        frames_rgb = [np.zeros((SIZE, SIZE, 3), dtype=np.uint8)]
    if len(frames_rgb) < T:
        frames_rgb = frames_rgb + [frames_rgb[-1]] * (T - len(frames_rgb))
    frames_rgb = frames_rgb[:T]
    clip = [cv2.resize(f, (SIZE, SIZE), interpolation=cv2.INTER_AREA) for f in frames_rgb]
    clip = np.stack(clip, axis=0)                                    # (T,H,W,3)
    clip = np.transpose(clip, (0, 3, 1, 2)).astype(np.float32) / 255 # (T,3,H,W)
    clip = (clip - 0.5) / 0.5
    clip = np.expand_dims(clip, 0)                                   # (1,T,3,H,W)
    return clip

def _extract_path_from_gradio_video(inp):
    if isinstance(inp, str) and os.path.exists(inp):
        return inp
    if isinstance(inp, dict):
        for key in ("video", "name", "path", "filepath"):
            v = inp.get(key)
            if isinstance(v, str) and os.path.exists(v):
                return v
        for key in ("data", "video"):
            v = inp.get(key)
            if isinstance(v, (bytes, bytearray)):
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
                tmp.write(v); tmp.flush(); tmp.close()
                return tmp.name
    if isinstance(inp, (list, tuple)) and inp and isinstance(inp[0], str) and os.path.exists(inp[0]):
        return inp[0]
    return None

def _read_uniform_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 1
    idxs = np.linspace(0, total - 1, max(T, 1)).astype(int)
    want = set(int(i) for i in idxs.tolist())
    j = 0
    while True:
        ok, bgr = cap.read()
        if not ok: break
        if j in want:
            rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
            frames.append(rgb)
        j += 1
    cap.release()
    return frames

def predict_from_video(gradio_video):
    video_path = _extract_path_from_gradio_video(gradio_video)
    if not video_path or not os.path.exists(video_path):
        return {}
    frames = _read_uniform_frames(video_path)

    # If OpenCV choked on the codec (common with recorded webm), re-encode once:
    if len(frames) == 0:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4"); tmp_name = tmp.name; tmp.close()
        cap = cv2.VideoCapture(video_path)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 640
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 480
        out = cv2.VideoWriter(tmp_name, fourcc, 20.0, (w, h))
        while True:
            ok, frame = cap.read()
            if not ok: break
            out.write(frame)
        cap.release(); out.release()
        frames = _read_uniform_frames(tmp_name)

    clip = preprocess_clip(frames)
    # >>> use the detected ONNX input/output names <<<
    logits = ort_session.run([OUTPUT_NAME], {INPUT_NAME: clip})[0]  # (1, C)
    probs = torch.softmax(torch.from_numpy(logits), dim=1)[0].numpy().tolist()
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

def predict_from_image(image):
    if image is None:
        return {}
    clip = preprocess_clip([image] * T)
    logits = ort_session.run([OUTPUT_NAME], {INPUT_NAME: clip})[0]
    probs = torch.softmax(torch.from_numpy(logits), dim=1)[0].numpy().tolist()
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

with gr.Blocks() as demo:
    gr.Markdown("# Gesture Classifier (ONNX)\nRecord or upload a short video, then click **Classify Video**.")
    with gr.Tab("Video (record or upload)"):
        vid_in = gr.Video(label="Record from webcam or upload a short clip")
        vid_out = gr.Label(num_top_classes=3, label="Prediction")
        gr.Button("Classify Video").click(fn=predict_from_video, inputs=vid_in, outputs=vid_out)
    with gr.Tab("Single Image (fallback)"):
        img_in = gr.Image(label="Upload an image frame", type="numpy")
        img_out = gr.Label(num_top_classes=3, label="Prediction")
        gr.Button("Classify Image").click(fn=predict_from_image, inputs=img_in, outputs=img_out)

if __name__ == "__main__":
    demo.launch()
```

L'exécution de la commande `python app.py` lance une application Gradio dans votre navigateur. Voici ce qui se passe :

1. **Flux webcam en direct** : L'application accède à votre webcam.
2. **Mise à jour continue des prédictions** : Le modèle traite les images en continu.
3. **Affichage des 3 meilleures classes** : L'application affiche les gestes prédits avec leurs probabilités.

Dans l'onglet **Video**, vous pouvez enregistrer un clip de 2 à 4 secondes, puis cliquer sur **Classify Video**. Le modèle affichera les probabilités prédites.

Voici un exemple où j'ai levé la main pour un geste **stop**, et le modèle prédit "stop" comme classe principale :

![Gradio demo output](https://github.com/tayo4christ/transformer-gesture/blob/07c7071bdb17bc08585baeb60d787eadc3936ef5/images/realtime-demo.png?raw=true align="left")

Figure 2. L'application Gradio s'exécutant localement.

### Évaluer la précision et la latence

Maintenant que le modèle fonctionne, vérifions ses performances sous deux angles :

* **Précision (Accuracy)** : le modèle prédit-il la bonne classe ?
* **Latence** : à quelle vitesse répond-il, notamment sur CPU vs GPU ?

#### 1. Vérification rapide de la précision

Enregistrez ceci sous le nom `eval.py` :

```python
import torch
from dataset import GestureClips, read_labels
from train import ViTTemporal

labels, _ = read_labels("labels.txt")
n_classes = len(labels)

# Load validation data
val_ds = GestureClips(train=False)
val_dl = torch.utils.data.DataLoader(val_ds, batch_size=2, shuffle=False)

# Load trained model
model = ViTTemporal(num_classes=n_classes)
model.load_state_dict(torch.load("vit_temporal_best.pt", map_location="cpu"))
model.eval()

correct, total = 0, 0
all_preds, all_labels = [], []

with torch.no_grad():
    for x, y in val_dl:
        logits = model(x)
        preds = logits.argmax(dim=1)
        correct += (preds == y).sum().item()
        total += y.size(0)
        all_preds.extend(preds.tolist())
        all_labels.extend(y.tolist())

print(f"Validation accuracy: {correct/total:.2%}")
```

#### 2. Matrice de confusion

Visualisons quels gestes sont confondus. Ajoutez ce fragment au bas de `eval.py` :

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(all_labels, all_preds)

plt.figure(figsize=(6,6))
sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels, cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
```

En exécutant `python eval.py`, une carte de chaleur (heatmap) apparaîtra.

![Confusion matrix](https://github.com/tayo4christ/transformer-gesture/blob/07c7071bdb17bc08585baeb60d787eadc3936ef5/images/confusion-matrix.png?raw=true align="left")

Figure 3. Matrice de confusion sur le jeu de validation.

#### 3. Benchmark de latence

Enfin, voyons la vitesse d'inférence. Enregistrez ceci sous `benchmark.py` :

```python
import time, numpy as np, onnxruntime
from dataset import read_labels

labels, _ = read_labels("labels.txt")

ort = onnxruntime.InferenceSession("vit_temporal.onnx", providers=["CPUExecutionProvider"])
INPUT_NAME = ort.get_inputs()[0].name
OUTPUT_NAME = ort.get_outputs()[0].name

dummy = np.random.randn(1, 16, 3, 224, 224).astype(np.float32)

# Warmup
for _ in range(3):
    ort.run([OUTPUT_NAME], {INPUT_NAME: dummy})

# Benchmark
t0 = time.time()
for _ in range(50):
    ort.run([OUTPUT_NAME], {INPUT_NAME: dummy})
t1 = time.time()

print(f"Average latency: {(t1 - t0)/50:.3f} seconds per clip")
```

Exécutez : `python benchmark.py`

Sur CPU, vous pourriez voir environ 0,05–0,15s par clip ; sur GPU, c'est beaucoup plus rapide.

## Option 2 : Utiliser de petits échantillons de jeux de données de gestes publics

Si vous préférez entraîner votre modèle sur de *vrais* clips de gestes, vous pouvez récupérer quelques vidéos de jeux de données ouverts comme **20BN Jester Dataset** ou **WLASL**.

### Configuration de votre dossier de données

Placez les clips dans le dossier `data/` sous des sous-dossiers nommés selon chaque classe de geste :

```plaintext
data/
├── swipe_left/
│   ├── clip1.mp4
│   └── clip2.mp4
├── swipe_right/
│   ├── clip1.mp4
│   └── clip2.mp4
└── stop/
    ├── clip1.mp4
    └── clip2.mp4
```

Et mettez à jour `labels.txt` pour correspondre aux noms des dossiers.

## Notes sur l'accessibilité et limites éthiques

Il est important de considérer le **contexte humain** :

* **L'accessibilité d'abord** : Ces outils peuvent aider les personnes ayant des difficultés motrices ou de la parole, mais ils doivent être co-conçus avec les utilisateurs finaux.
* **Sensibilité des données** : Le déploiement d'un tel système nécessite une réflexion approfondie sur le consentement et la représentation.
* **Tolérance aux erreurs** : Même de petites erreurs de classification peuvent avoir de lourdes conséquences. Prévoyez toujours des options de secours.
* **Biais et inclusivité** : Les modèles entraînés sur des jeux de données restreints peuvent échouer selon la couleur de peau, l'éclairage ou les variations culturelles des gestes.

## Prochaines étapes

* **Meilleurs modèles** : Essayez des Transformers axés sur la vidéo comme [TimeSformer](https://arxiv.org/abs/2102.05095).
* **Vocabulaires plus larges** : Ajoutez plus de classes de gestes.
* **Fusion de poses** : Combinez la vidéo avec des points clés de pose humaine via [MediaPipe](https://mediapipe.readthedocs.io/en/latest/solutions/hands.html).
* **Lissage en temps réel** : Implémentez une logique anti-rebond pour stabiliser les prédictions.
* **Quantification** : Convertissez votre modèle ONNX en version quantifiée INT8 pour un déploiement sur Raspberry Pi.

## Conclusion

Dans ce tutoriel, vous avez appris à créer un système de reconnaissance de gestes à l'aide de modèles Transformer. En préparant un petit jeu de données, en entraînant un Vision Transformer avec pooling temporel et en exportant le modèle vers ONNX, vous avez démontré une application pratique de ces technologies de pointe.

Ce projet illustre comment exploiter des méthodes avancées de ML pour améliorer l'accessibilité et la communication, ouvrant la voie à des environnements d'apprentissage plus inclusifs.

Voici le dépôt GitHub pour le code source complet : [transformer-gesture](https://github.com/tayo4christ/transformer-gesture).