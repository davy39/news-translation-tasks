---
title: Comment créer un coach de sport IA en temps réel avec Vision Agents
author: Ekemini Samuel
date: '2025-12-19T17:29:13.678Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-ai-gym-coach-with-vision-agents
description: La vision par ordinateur transforme la façon dont les gens s'entraînent,
  des séances à domicile aux miroirs de sport intelligents. Imaginez entrer dans votre
  salle de sport personnelle, allumer votre caméra et disposer d'un coach IA qui observe
  vos mouvements, compte vos répétitions et corrige votre posture en temps réel...
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766158143362/b5d2947c-cc24-4948-a7fd-7ef2b3a79d5f.png
tags:
- name: AI
  slug: ai
- name: agentic AI
  slug: agentic-ai
- name: Python
  slug: python
seo_desc: 'Computer vision is transforming how people train, from at-home workouts
  to smart gym mirrors.

  Imagine walking into your home gym, turning on your camera, and having an AI coach
  that sees your movements, counts your reps, and corrects your form in rea...'
---


La vision par ordinateur transforme la façon dont les gens s'entraînent, des séances à domicile aux miroirs de sport intelligents.

Imaginez entrer dans votre salle de sport personnelle, allumer votre caméra et disposer d'un coach IA qui observe vos mouvements, compte vos répétitions et corrige votre posture en temps réel.

C'est exactement ce que nous allons construire dans ce tutoriel : un compagnon de sport et coach de fitness en temps réel.

Nous intégrerons l'inférence vidéo à faible latence de [Vision Agents](https://visionagents.ai/) pour détecter les schémas de mouvement, compter les répétitions et donner un retour vocal instantané comme « Redressez votre dos ! » ou « Gardez une posture gainée ! », tout comme le ferait un entraîneur humain.

Voici une [vidéo de démonstration](https://youtu.be/etqq68p-RGE) du compagnon de sport IA lors d'une séance d'entraînement :

%[https://youtu.be/etqq68p-RGE] 

## Ce que nous allons aborder :

1. [Prérequis](#heading-prerequis)
    
2. [Configuration du projet](#heading-configuration-du-projet)
    
3. [Comment lancer l'application](#heading-comment-lancer-l-application)
    
4. [Prochaines étapes](#heading-prochaines-etapes)
    

## **Prérequis**

* Python 3.13 ou supérieur
    
* Des clés API pour :
    
    * [Gemini](https://ai.google.dev/) (pour le LLM multimodal en temps réel)
        
    * [Stream](https://getstream.io/video/) (pour l'infrastructure vidéo/audio)
        
    * Alternativement : [OpenAI](https://openai.com) (si vous utilisez [OpenAI Realtime](https://platform.openai.com/docs/guides/realtime) à la place)
        
* Un éditeur de code comme VS Code ou Windsurf
    

## **Configuration du projet**

Créez un nouveau répertoire sur votre ordinateur appelé `gym_buddy`. Vous pouvez également le faire directement dans votre terminal avec cette commande :

```bash
mkdir gym_buddy
```

Ouvrez ensuite le répertoire dans votre IDE (pour ce guide, j'utilise [Windsurf IDE](https://windsurf.com/)).

Si vous n'avez pas uv (un installateur et résolveur de paquets Python rapide) installé sur votre ordinateur, installez-le avec cette commande :

```bash
pip install uv
```

Note : Après avoir installé uv, vous pouvez également exécuter `uv -init` pour configurer le projet avec des fichiers d'exemple et un fichier `.toml` contenant les métadonnées.

Ensuite, nous allons créer le fichier `pyproject.toml`. Il s'agit d'un fichier de configuration pour les projets Python qui spécifie les exigences du système de construction et d'autres métadonnées du projet. C'est un fichier standard utilisé par les outils modernes de packaging Python.

Saisissez le code ci-dessous :

```bash
[project]
name = "gym-buddy"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "python-dotenv>=1.0",
    "vision-agents",
    "vision-agents-plugins-openai",
    "vision-agents-plugins-getstream",
    "vision-agents-plugins-ultralytics",
    "vision-agents-plugins-gemini",
]

[tool.uv.sources]
"vision-agents" = {path = "../../agents-core", editable=true}
"vision-agents-plugins-deepgram" = {path = "../../plugins/deepgram", editable=true}
"vision-agents-plugins-ultralytics" = {path = "../../plugins/ultralytics", editable=true}
"vision-agents-plugins-openai" = {path = "../../plugins/openai", editable=true}
"vision-agents-plugins-getstream" = {path = "../../plugins/getstream", editable=true}
"vision-agents-plugins-gemini" = {path = "../../plugins/gemini", editable=true}
```

Vous pouvez également créer un fichier `requirements.in` avec uniquement les dépendances directes, comme ceci :

```bash
python-dotenv>=1.0
vision-agents
vision-agents-plugins-openai
vision-agents-plugins-getstream
vision-agents-plugins-ultralytics
vision-agents-plugins-gemini
```

Installez ensuite les dépendances à l'aide de uv et de l'une de ces commandes :

```bash
uv sync
```

Cela générera le fichier `uv.lock` du gestionnaire de paquets uv qui gère les dépendances et les builds du projet.

Si vous utilisez Windows, vous pourriez rencontrer une erreur d'installation des dépendances, particulièrement avec NumPy. Cela est probablement dû à l'absence d'outils de compilation sur votre système.

#### Pourquoi NumPy est requis

NumPy est une bibliothèque Python pour le calcul numérique. Dans ce projet, elle est utilisée par les composants de vision par ordinateur et d'IA (tels que la détection basée sur YOLO et Vision Agents) pour manipuler les données d'image, les boîtes de délimitation (bounding boxes), les coordonnées et autres sorties numériques produites lors de l'analyse vidéo en temps réel.

De nombreuses bibliothèques utilisées ici en dépendent pour les opérations rapides sur les tableaux et les calculs mathématiques. C'est pourquoi NumPy est installé lors de la configuration et pourquoi les problèmes liés à son installation peuvent affecter l'ensemble du pipeline.

Pour résoudre ce problème, installez les [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) (requis pour compiler les paquets Python avec des extensions C). Lors de l'installation, assurez-vous de sélectionner « Développement Desktop en C++ ». Cela installe tous les outils de compilation nécessaires.

Visual Studio s'affiche comme ceci une fois l'installation terminée. Vous devrez peut-être redémarrer votre ordinateur pour que les mises à jour prennent effet.

![L'installateur Visual Studio](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863109016/81d76ab4-9cd8-48f6-8cd9-83654ab27071.png align="center")

Exécutez maintenant cette commande dans votre terminal :

```bash
python -m pip install -e .
```

La commande ci-dessus installe toutes les dépendances nécessaires au projet.

### Comment obtenir vos clés API

Pour ce projet, nous devons obtenir des clés API de Stream et Gemini/OpenAI.

Pour obtenir votre clé API Stream, [inscrivez-vous](https://getstream.io/) avec votre méthode préférée.

![Page d'inscription de Stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863152347/b46c8cc0-0f2f-448f-b7c5-f723fee94fb5.png align="center")

Ensuite, accédez à votre [tableau de bord](https://dashboard.getstream.io/organization/1270689/apps) et cliquez sur « Create App » pour créer une nouvelle application pour le compagnon de sport IA.

![Tableau de bord Stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863177461/8c8c51d5-46fe-44fe-8a2c-2336d3492da4.png align="center")

Saisissez le nom de l'application, choisissez l'environnement (Development/Production), sélectionnez une région et cliquez sur **« Create App »**.

![Créer l'application sur Stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863207947/529df7e3-bbdd-4d84-8023-3cb80241040b.png align="center")

Après avoir créé l'application, cliquez sur l'onglet d'aperçu du tableau de bord dans la barre latérale gauche, puis accédez à l'onglet Video et cliquez sur **« API Keys »**. Copiez votre clé API et votre secret, et conservez-les en lieu sûr.

Pour obtenir votre clé API [Gemini](https://gemini.google.com/), visitez le [site Google AI Studio](https://aistudio.google.com/welcome?utm_source=PMAX&utm_medium=display&utm_campaign=FY25-global-DR-pmax-1710442&utm_content=pmax&gclsrc=aw.ds&gad_source=1&gad_campaignid=22301327511&gclid=CjwKCAiA55rJBhByEiwAFkY1QOJAyRZcUSQvxW3RlHpE-GvzAoERF7Pt_mRq7p9dFYp2cu8CCNidEBoC65MQAvD_BwE), puis cliquez sur « Get started ».

![Configuration de votre compte Google AI studio](https://cdn.hashnode.com/res/hashnode/image/upload/v1765864009410/9d588512-c2ea-42bc-8e72-d2c213587cf0.png align="center")

Ensuite, allez sur votre tableau de bord et cliquez sur **« Create API key »**.

![Créer votre clé API](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863451321/99f73092-5e05-47c4-a3de-6350dfec50f0.png align="center")

Saisissez un nom pour la clé, puis créez un nouveau projet pour la clé API.

![Nommer votre clé API](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863470658/40c7e61c-6be3-40a6-8e61-236e334241d9.png align="center")

Une fois la nouvelle clé API créée, copiez-la et conservez-la en lieu sûr.

### Création du compagnon de sport IA

Maintenant que vous avez les clés API nécessaires, créez un fichier `.env` dans le répertoire racine du projet et ajoutez toutes les clés API comme ceci :

```bash
GEMINI_API_KEY=votre_cle_gemini
STREAM_API_KEY=votre_cle_stream
STREAM_API_SECRET=votre_secret_stream
```

Si vous utilisez [OpenAI](https://openai.com/) au lieu de Gemini, ajoutez également :

```bash
OPENAI_API_KEY=votre_cle_openai
```

Voici la structure du projet et de la base de code pour l'application de compagnon de sport que nous construisons :

![La base de code et le dossier du projet pour le compagnon de sport IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1766598231388/c0ca918c-de0d-4bbe-b55b-21ae3082c002.webp align="center")

Dans le répertoire racine, créez un fichier `__init__.py` vide. Ce fichier permet à Python de traiter le répertoire comme un paquet. Vous pouvez ajouter un commentaire dans le fichier pour vous en souvenir, comme ceci :

```bash
# Ce fichier permet à Python de traiter le répertoire comme un paquet.
```

Ensuite, créez un fichier `gym_buddy.py`. C'est le fichier principal de l'application, contenant la configuration de l'agent et la logique de connexion à l'appel pour le Gym Companion. Saisissez le code ci-dessous dans le fichier :

```python
import logging
from dotenv import load_dotenv
from vision_agents.core import User, Agent, cli
from vision_agents.core.agents import AgentLauncher
from vision_agents.plugins import getstream, ultralytics, gemini
logger = logging.getLogger(__name__)
load_dotenv()
async def create_agent(**kwargs) -> Agent:
    agent = Agent(
        edge=getstream.Edge(),  # use stream for edge video transport
        agent_user=User(name="AI gym companion"),
        instructions="Read @gym_buddy.md",  # read the gym buddy markdown instructions
        llm=gemini.Realtime(fps=3),  # Share video with gemini
        # llm=openai.Realtime(fps=3), use this to switch to openai
        processors=[
            ultralytics.YOLOPoseProcessor(model_path="yolo11n-pose.pt")
        ],  # realtime pose detection with yolo
    )
    return agent
async def join_call(agent: Agent, call_type: str, call_id: str, **kwargs) -> None:
    call = await agent.create_call(call_type, call_id)
    # join the call and open a demo env
    with await agent.join(call):
        await agent.llm.simple_response(
            text="Say hi. After the user does their exercise, offer helpful feedback."
        )
        await agent.finish()  # run till the call ends
if __name__ == "__main__":
    cli(AgentLauncher(create_agent=create_agent, join_call=join_call))
```

Ensuite, créez un fichier `gym_buddy.md`. Il s'agit d'un fichier d'instructions pour le guide de coaching de l'agent, qu'il suivra lors de l'analyse des entraînements et de la fourniture de retours en temps réel. Saisissez le code markdown ci-dessous :

```markdown
You are a voice fitness coach. You will watch the user's workout and offer feedback.
The video clarifies the body position using Yolo's pose analysis, so you'll see their exact movement.
Speak with a high-energy, motivating tone. Be strict about form but encouraging. Do not give feedback if you are not sure or do not see an exercise.
# Gym Workout Coaching Guide
## 1. Introduction
A fitness coach's primary responsibility is to ensure safety and efficacy in every movement. While everybody is different, the fundamental mechanics of human movement—stability, alignment, and range of motion—remain constant. By monitoring key checkpoints like spinal alignment, joint tracking, and tempo, coaches can guide athletes toward stronger, injury-free workouts. The following guidelines break down the core compound movements into phases, with clear teaching points and coaching cues.
## 2. The Squat: Setup and Stance
The squat is the king of lower-body exercises, but it starts before the descent. The athlete should stand with feet shoulder-width apart or slightly wider, toes pointed slightly outward (5-30 degrees). The spine must be neutral, chest proud, and core braced. Coaches should watch for collapsing arches in the feet or a rounded upper back. A solid setup creates the tension needed for a powerful lift.
## 3. The Squat: Descent (Eccentric Phase)
The movement begins by breaking at the hips and knees simultaneously. The hips should travel back and down, as if sitting in a chair, while the knees track in line with the toes. Coaches must ensure the heels stay glued to the floor. Common errors include "knee valgus" (knees caving in) or the torso collapsing forward. The descent should be controlled and deliberate.
## 4. The Squat: Depth and Reversal
"Depth" is achieved when the hip crease drops below the top of the knee (parallel). While not everyone has the mobility for this, it is the standard for a full range of motion. At the bottom, the athlete should maintain tension—no bouncing or relaxing. The reversal (concentric phase) is driven by driving the feet into the floor and extending the hips and knees, exhaling forcefully.
## 5. The Push-up: The Plank Foundation
A perfect push-up is essentially a moving plank. The setup requires hands placed slightly wider than shoulder-width, directly under the shoulders. The body must form a straight line from head to heels. Coaches should watch for sagging hips (lumbar extension) or piking hips (flexion). Glutes and quads should be squeezed tight to lock the body into a rigid lever.
## 6. The Push-up: Mechanics
As the athlete lowers themselves, the elbows should track back at roughly a 45-degree angle to the torso, forming an arrow shape, not a "T". The chest should descend until it nearly touches the floor. The neck must remain neutral—no reaching with the chin. The push back up should be explosive, fully extending the arms without locking the elbows violently.
## 7. The Lunge: Step and Stability
The lunge challenges balance and unilateral strength. Whether forward or reverse, the step should be long enough to allow both knees to bend to approximately 90 degrees at the bottom. The feet should remain hip-width apart throughout the movement, like moving on train tracks, not a tightrope. Coaches should look for wobbling or the front heel lifting off the ground.
## 8. The Lunge: Alignment
In the bottom position, the front knee should be directly over the ankle, not shooting far past the toes (though some forward travel is acceptable). The torso should remain upright or have a very slight forward lean; collapsing over the front thigh is a fault. The back knee should hover just an inch off the ground. Drive through the front heel to return to the start.
## 9. Tempo and Control
Time under tension builds muscle and control. Coaches should encourage a specific tempo, such as 2-0-1 (2 seconds down, 0 pause, 1 second up). Rushing through reps often masks muscle imbalances and relies on momentum rather than strength. If an athlete speeds up, cue them to "slow down and own the movement."
## 10. Breathing Mechanics
Proper breathing stabilises the core. The general rule is to inhale during the eccentric phase (lowering) and exhale during the concentric phase (lifting/pushing). For heavy lifts, the Valsalva manoeuvre (bracing the core with a held breath) may be appropriate, but for general fitness, rhythmic breathing ensures oxygen delivery and blood pressure management.
## 11. Common Faults and Fixes
- **Squat - Butt Wink**: Posterior pelvic tilt at the bottom. Fix: Limit depth or improve hamstring/ankle mobility.
- **Push-up - Winging Scapula**: Shoulder blades popping up. Fix: Push the floor away at the top (protraction) and engage serratus anterior.
- **Lunge - Valgus Knee**: Front knee collapsing in. Fix: Cue "push the knee out" and engage the glute medius.
- **General - Ego Lifting**: Sacrificing form for reps or weight. Fix: Regress the exercise or slow the tempo
```

### Comment fonctionne l'agent IA

Nous avons maintenant configuré le fichier d'instructions pour l'agent IA. Voyons comment le code interagit avec la création de l'agent et le fichier d'instructions Markdown ci-dessus. Dans `gym_buddy.py`, l'agent est créé et initialisé avec des composants spécifiques comme ceci :

```python
def create_agent() -> Agent:
    # Initialize video transport
    video_transport = StreamVideoTransport()
    
    # Set up AI components
    gemini = GeminiRealtime()
    pose_processor = YOLOPoseProcessor(model_path="yolo11n-pose.pt")
    
    # Create agent with instructions
    return Agent(
        name="AI Gym Buddy",
        instructions="gym_buddy.md",  # Loads coaching instructions
        video_transport=video_transport,
        llm=gemini,
        processors=[pose_processor]
    )
```

Le fichier `gym_buddy.md` contient des instructions structurées qui guident le comportement de l'agent compagnon de sport.

```markdown
## Coaching Style
- Be encouraging and positive
- Provide clear, actionable feedback
- Focus on one correction at a time

## Squat Form
- Keep chest up and back straight
- Knees should track over toes
- Lower until thighs are parallel to ground
- Push through heels to stand

## Safety Guidelines
- Stop user if a dangerous form is detected
- Suggest modifications for beginners
- Remind to keep core engaged
```

Ces instructions sont chargées avec le paramètre `instructions="gym_buddy.md"` dans le fichier `gym_buddy.py`. L'agent analyse ensuite ce fichier pour comprendre comment évaluer votre posture pendant la séance d'entraînement et fournir des retours.

```python
# Processing video frames
async def process_frame(self, frame):
    # Analyze pose using YOLO
    poses = await self.pose_processor.process(frame)
    
    # Generate feedback based on instructions
    feedback = await self.llm.generate_feedback(
        poses=poses,
        instructions=self.instructions
    )
    return feedback
```

Lorsqu'il donne un retour, l'agent compare les poses détectées avec la posture idéale décrite dans le markdown. Ensuite, il génère un retour en langage naturel en utilisant le ton et le style spécifiés. Les consignes de sécurité dans `gym_buddy.md` sont vérifiées en priorité, puis les corrections de posture spécifiques sont mentionnées par l'agent.

Pour ajouter un nouvel exercice, vous pouvez mettre à jour le fichier `gym_buddy.md` avec une nouvelle section comme celle-ci :

```markdown
## Push-up Form
- Keep body in a straight line
- Lower until chest nearly touches floor
- Push through palms to return up
- Keep core engaged
```

L'agent intégrera automatiquement ces instructions lors de sa prochaine exécution. Cela facilite la mise à jour et l'extension des capacités de l'agent en éditant simplement le fichier markdown.

Vous pouvez consulter le code complet du AI Gym Companion dans le [dépôt GitHub](https://github.com/Tabintel/gym_buddy).

## Comment lancer l'application

Tout d'abord, créez un environnement virtuel en Python avec cette commande :

```bash
python -m venv venv
```

Cela crée le répertoire `.venv`.

Activez ensuite l'environnement virtuel Python comme ceci :

```bash
.\venv\Scripts\activate
```

Lancez maintenant l'agent IA avec cette commande :

```bash
uv run gym_buddy.py
```

Vous pouvez également démarrer l'application avec cette commande :

```bash
python gym_buddy.py
```

Le chargement commence ainsi :

![Le compagnon de sport IA est en cours de chargement](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863544434/7fa5fa8e-4286-40d1-9f34-86e7e7e6182b.png align="center")

L'agent IA va :

1. Créer un appel vidéo
    
2. Ouvrir une interface de démonstration dans votre navigateur
    
3. Rejoindre l'appel et commencer l'observation
    
4. Vous demander de faire un exercice de squat
    
5. Analyser vos mouvements et positions, puis fournir un retour
    

![Gemini AI est connecté et le navigateur pour le compagnon de sport est ouvert](https://cdn.hashnode.com/res/hashnode/image/upload/v1766598491312/9cd86035-c182-428e-b059-15842caec0b5.png align="center")

La sortie du terminal ci-dessus montre également que Gemini AI est connecté.

L'agent se charge ensuite dans votre navigateur comme ceci :

![Le compagnon de sport IA est lancé](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863577856/e32b1b35-7356-4c23-8b8b-a8513dd9aabb.png align="center")

Une fenêtre modale s'affiche également pour présenter les Vision Agents. Vous pouvez ignorer l'introduction ou cliquer sur **Next** pour continuer.

Le Vision Agent utilise un edge global pour garantir une latence d'appel optimale. C'est essentiel pour que le compagnon de sport IA puisse fournir des retours en temps réel sur les exercices effectués par les utilisateurs.

![Le compagnon de sport détecte les visuels et les mouvements](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863612816/4bd395ca-ed40-46d7-ab3b-0ceed23f1d0c.png align="center")

Le compagnon de sport IA peut également envoyer des messages de chat sur les exercices via la boîte de dialogue affichée sur le côté droit de l'interface. Ceci est possible grâce au SDK/API de chat.

![Le compagnon de sport IA donne un retour](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863702571/7586bddc-a830-4bf4-8af3-146dccf0f337.png align="center")

Lorsque vous effectuez un squat, le Vision Agent (propulsé par Gemini) analyse les images vidéo en temps réel. Il détecte la fin du mouvement et déclenche l'outil `send_rep_count`. Cela met instantanément à jour le compteur d'exercices sur votre écran et fournit une réponse textuelle et vocale encourageante !

Voici une [vidéo de démonstration](https://youtu.be/etqq68p-RGE) du compagnon de sport IA lors d'une séance d'entraînement :

%[https://youtu.be/etqq68p-RGE] 

Vous pouvez également copier le lien et le partager, ou scanner le code QR ci-dessous pour tester le Gym Companion sur votre téléphone mobile.

![Copiez le code QR pour tester sur votre téléphone mobile](https://cdn.hashnode.com/res/hashnode/image/upload/v1765863762688/a6c7b56e-9b0b-4819-ae9f-61a32ce71280.png align="center")

Si vous souhaitez le tester sur votre téléphone, installez l'application [Stream Video calls](https://apps.apple.com/us/app/stream-video-calls/id1644313060) pour les appareils iOS pour une meilleure expérience mobile.

## **Prochaines étapes**

Dans ce tutoriel, vous avez appris à construire un compagnon de sport IA à l'aide de Vision Agents.

Le Real-Time Gym Companion illustre comment l'IA de vision permet une interactivité de type humain en fusionnant :

* La perception vidéo (voir)
    
* La compréhension par LLM (penser)
    
* Le retour vocal (parler)
    

Cette technologie à faible latence vous permet de créer des applications de fitness en temps réel qui donnent des retours instantanés, tout comme le ferait un entraîneur personnel.

Vous pouvez découvrir d'autres cas d'utilisation de projets avec Vision Agents dans le [dépôt GitHub](https://github.com/GetStream/Vision-Agents/tree/main/examples).