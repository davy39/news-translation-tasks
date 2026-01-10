---
title: Comment déployer un agent IA avec Amazon Bedrock AgentCore
subtitle: ''
author: Emdadul Islam
co_authors: []
series: null
date: '2025-10-15T01:01:41.361Z'
originalURL: https://freecodecamp.org/news/deploy-an-ai-agent-with-amazon-bedrock
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760489893067/3f33049f-d17e-4d94-8deb-fa43c65ec753.png
tags:
- name: AI
  slug: ai
- name: ai agents
  slug: ai-agents
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Comment déployer un agent IA avec Amazon Bedrock AgentCore
seo_desc: Amazon Bedrock AgentCore is a managed service that makes it easier to build,
  deploy, and operate AI agents securely at scale on AWS. It works seamlessly with
  frameworks like Strands Agents, LangGraph, CrewAI, and LlamaIndex, while taking
  care of the ...
---

Amazon Bedrock AgentCore est un service géré qui facilite la construction, le déploiement et l'exploitation d'agents IA de manière sécurisée et à l'échelle sur AWS. Il fonctionne parfaitement avec des frameworks tels que Strands Agents, LangGraph, CrewAI et LlamaIndex, tout en prenant en charge les tâches complexes telles que la gestion du runtime, la configuration des rôles IAM et l'observabilité.

Dans ce guide, vous allez configurer votre environnement, créer et tester un agent IA simple localement, le déployer avec le kit de démarrage AgentCore et l'invoquer via l'AWS SDK.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Étape 1 : Configurer l'AWS CLI](#heading-etape-1-configurer-l-aws-cli)
    
* [Étape 2 : Installer et créer votre agent](#heading-etape-2-installer-et-creer-votre-agent)
    
    * [Créer un fichier requirements.txt](#heading-creer-un-fichier-requirementstxt)
        
    * [Analyse du code](#heading-analyse-du-code)
        
* [Étape 3 : Tester l'agent localement](#heading-etape-3-tester-l-agent-localement)
    
* [Étape 4 : Déployer sur le Runtime AgentCore](#heading-etape-4-deployer-sur-le-runtime-agentcore)
    
* [Étape 5 : Invoquer l'agent avec l'AWS SDK](#heading-etape-5-invoquer-l-agent-avec-l-aws-sdk)
    
* [Étape 6 : Nettoyage](#heading-etape-6-nettoyage)
    
* [Problèmes courants](#heading-problemes-courants)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir :

* Un compte AWS avec des identifiants configurés.
    
* L'AWS CLI installée et fonctionnelle.
    
* Python 3.10 ou version ultérieure installé.
    
* Boto3 installé.
    
* L'accès aux modèles activé dans la console Amazon Bedrock (par exemple, Anthropic Claude Sonnet 4.0).
    

## Étape 1 : Configurer l'AWS CLI

Tout d'abord, installez l'AWS CLI si vous ne l'avez pas déjà. Sur Linux ou macOS : [Guide de configuration de l'AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Ensuite, [configurez](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) un profil avec AWS SSO :

```bash
aws configure sso --profile my-profile
```

Vous serez invité à saisir des détails tels que :

* **SSO start URL** – l'URL du portail IAM Identity Center de votre organisation AWS.
    
* **SSO region** – la région AWS où IAM Identity Center est configuré.
    
* **Account ID** – le compte AWS auquel vous souhaitez accéder.
    
* **Role name** – le rôle IAM que vous souhaitez assumer dans ce compte.
    
* **Default region** – la région qui sera utilisée lors des requêtes.
    
* **Default output format** – par exemple, `json`, `yaml` ou `table`.
    

Cela crée un nouveau profil nommé `my-profile` dans votre configuration AWS CLI, vous permettant d'utiliser cette identité pour interagir avec les services AWS.

Ensuite, vous devez vérifier votre identité. Une fois votre profil configuré, confirmez que la CLI s'authentifie correctement auprès d'AWS en exécutant :

```bash
aws sts get-caller-identity --profile my-profile
```

Cette commande renvoie des détails sur votre identité, notamment :

* **Account** – l'ID du compte AWS avec lequel vous êtes authentifié.
    
* **UserId** – l'identifiant unique de votre rôle ou utilisateur IAM.
    
* **Arn** – l'Amazon Resource Name (ARN) complet de votre identité.
    

Si la commande réussit et affiche les informations de votre compte, cela signifie que votre profil est correctement configuré et prêt à être utilisé avec les SDK AWS, l'AWS CLI ou des services comme Bedrock AgentCore.

## Étape 2 : Installer et créer votre agent

Tout d'abord, vous devez configurer un environnement virtuel Python. Cela évite les conflits de dépendances avec d'autres projets sur votre machine.

Créons et activons un environnement virtuel :

Sur **macOS/Linux :**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sur **Windows (PowerShell ou CMD) :**

```python
python -m venv .venv
.venv\\Scripts\\activate
```

* `python -m venv .venv` → crée un environnement virtuel nommé `.venv` dans votre dossier de projet.
    
* `.venv\\Scripts\\activate` → active l'environnement.
    

Une fois activé, votre invite de commande affichera (.venv) au début. Pour désactiver :

```bash
deactivate
```

### Créer un fichier `requirements.txt` 

Listez les dépendances dont votre projet a besoin en créant un fichier nommé `requirements.txt` à la racine du projet :

```bash
bedrock-agentcore
strands-agents
```

Cela facilite l'installation de tout en une seule fois avec :

```python
pip install -r requirements.txt
```

Créez un fichier appelé `my_agent.py` et ajoutez le code suivant :

```python
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
# Créer un agent avec les paramètres par défaut
agent = Agent()

@app.entrypoint
def invoke(payload):
    """Votre fonction d'agent IA"""
    user_message = payload.get("prompt", "Bonjour ! Comment puis-je vous aider aujourd'hui ?")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
```

### Analyse du code

* `BedrockAgentCoreApp` – le wrapper de runtime central qui gère la configuration, l'exécution et l'intégration avec les services AWS.
    
* `Agent` – un objet agent de base de la bibliothèque Strands qui peut traiter et répondre aux prompts.
    
* `BedrockAgentCoreApp()` crée l'application conteneur qui gère le cycle de vie de votre agent.
    
* `Agent()` initialise un agent Strands simple avec les paramètres par défaut. Dans un cas réel, vous pouvez personnaliser cela avec des outils spécifiques, de la mémoire ou une logique de raisonnement.
    
* Le décorateur `@app.entrypoint` marque cette fonction comme le point d'entrée appelable pour votre agent. Chaque fois qu'une requête est envoyée à l'agent (via l'AWS SDK, la CLI ou un test local), cette fonction est invoquée.
    
* L'agent recherche un `"prompt"` dans le payload entrant.
    
* Si aucun prompt n'est fourni, il utilise par défaut `"Bonjour ! Comment puis-je vous aider aujourd'hui ?"`.
    
* L'objet `Agent` traite ensuite cette entrée et génère une réponse.
    

## Étape 3 : Tester l'agent localement

Exécutez l'agent :

```bash
python3 -u my_agent.py
```

Ouvrez un autre terminal et envoyez une requête :

```bash
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Bonjour !"}'
```

Si cela réussit, vous verrez :

```plaintext
{"result": "Bonjour ! Je suis là pour vous aider..."}
```

Vous pouvez arrêter l'agent avec Ctrl+C.

## Étape 4 : Déployer sur le Runtime AgentCore

Vous êtes maintenant prêt à déployer votre agent sur AWS.

Configurez l'agent :

```plaintext
agentcore configure -e my_agent.py
```

Cela crée un fichier de configuration appelé `bedrock_agentcore.yaml`.

Vous pouvez lancer le déploiement avec cette commande :

```plaintext
agentcore launch
```

La sortie inclura :

* L'Amazon Resource Name (ARN) de votre agent.
    
* L'emplacement des logs dans Amazon CloudWatch.
    

Testez votre agent déployé :

```bash
agentcore invoke '{"prompt": "raconte-moi une blague"}'
```

Si vous recevez une blague en retour, votre agent fonctionne correctement.

## Étape 5 : Invoquer l'agent avec l'AWS SDK

Vous pouvez appeler votre agent par programmation en utilisant Boto3. Créez un fichier appelé `invoke_agent.py` :

```python
import json
import boto3

agent_arn = "VOTRE_AGENT_ARN"
prompt = "Raconte-moi une blague"

agent_core_client = boto3.client("bedrock-agentcore")

payload = json.dumps({"prompt": prompt}).encode()

response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    payload=payload
)

content = []
for chunk in response.get("response", []):
    content.append(chunk.decode("utf-8"))
print(json.loads("".join(content)))
```

Exécutez le script :

```plaintext
python invoke_agent.py
```

Vous devriez voir la réponse de l'agent IA.

## Étape 6 : Nettoyage

**Si vous ne souhaitez plus exécuter l'agent, supprimez le runtime :**

```plaintext
aws bedrock-agentcore delete-agent-runtime --agent-runtime-arn <votre_arn>
```

### Problèmes courants

* **Permission refusée** : Vérifiez vos identifiants AWS et vos politiques IAM.
    
* **Avertissement Docker** : Ignorez ceci à moins d'utiliser `--local` ou `--local-build`.
    
* **Accès au modèle refusé** : Activez l'accès au modèle (tel que Claude Sonnet 4.0) dans la console Bedrock.
    
* **Erreurs de build** : Vérifiez les logs de build CloudWatch et les politiques IAM.
    

### Conclusion

Amazon Bedrock AgentCore facilite la création et le déploiement d'agents IA sans avoir à gérer des configurations de conteneurs complexes ou l'infrastructure. Vous pouvez tester localement, lancer sur le cloud avec une seule commande et tout surveiller via CloudWatch.

Ce workflow est idéal pour les développeurs qui souhaitent passer rapidement du prototype à la production tout en restant dans l'écosystème AWS.

Ressources :

[https://strandsagents.com/latest/](https://strandsagents.com/latest/)

[https://aws.amazon.com/bedrock/agentcore/](https://aws.amazon.com/bedrock/agentcore/)