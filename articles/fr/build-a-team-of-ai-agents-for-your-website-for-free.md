---
title: Comment créer une équipe d'agents IA pour votre site web gratuitement en utilisant
  Agno et Groq
subtitle: ''
author: Andrew Baisden
co_authors: []
series: null
date: '2025-03-31T22:46:11.824Z'
originalURL: https://freecodecamp.org/news/build-a-team-of-ai-agents-for-your-website-for-free
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742397437476/0ffa13b0-c668-40d7-864f-596f523f6101.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: react js
  slug: react-js
- name: programming
  slug: programming-ciovqvfcb008mb253jrczo9ye
- name: Python
  slug: python
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Comment créer une équipe d'agents IA pour votre site web gratuitement en
  utilisant Agno et Groq
seo_desc: AI is quickly changing the way we work, and more and more companies are
  using it to help them get and retain clients. Teams are also using AI to create
  innovative and responsive websites capable of engaging visitors while also providing
  helpful infor...
---

L'IA change rapidement notre façon de travailler, et de plus en plus d'entreprises l'utilisent pour les aider à acquérir et à fidéliser des clients. Les équipes utilisent également l'IA pour créer des sites web innovants et réactifs capables d'engager les visiteurs tout en fournissant des informations utiles.

Les agents IA sont des outils puissants pour les services client. Les faire alimenter vos plateformes et sites web peut sembler une proposition coûteuse nécessitant une expertise technique élevée. Mais avec l'émergence de nouvelles plateformes modernes comme Agno et Groq, il est désormais plus facile d'intégrer un système d'agents IA dans votre site web tout en restant dans votre budget.

Dans cet article, vous allez suivre le processus de développement de votre propre écosystème d'agents IA (gratuitement). Cela vous permettra d'avoir un site web capable de gérer les demandes des clients, de créer du contenu, d'analyser le comportement d'un utilisateur et de fournir des expériences personnalisées pour chaque utilisateur. C'est une configuration fantastique car vous pouvez automatiser une partie de votre entreprise, accélérant la génération de leads et libérant votre temps pour travailler sur des tâches plus prioritaires.

Cet article s'adresse aux développeurs familiarisés avec JavaScript, React et Python. Même si vous n'avez pas une compréhension complète des trois, tant que vous êtes débutant ou junior avec quelques connaissances, vous devriez être capable de comprendre au moins une partie du code. Par exemple, JavaScript et Python sont assez similaires en termes de syntaxe, donc si vous avez de l'expérience avec l'un d'eux, alors simplement parcourir le code vous donnera une idée de comment tout fonctionne.

Pour ce tutoriel, nous allons construire un site web de portfolio. Mais vous pouvez utiliser les idées et concepts que vous apprenez ici pour tout type de site web, que vous soyez un entrepreneur solo ou partie d'une grande entreprise. Avec ces outils et frameworks, il est possible de transformer votre présence web sans dépasser votre budget.

## Table des matières

* [Prérequis](#prerequisites)
    
* [Qu'est-ce que les agents IA ?](#questce-que-les-agents-ia)
    
* [Qu'est-ce qu'Agno et Groq Cloud ?](#questce-quagno-et-groq-cloud)
    
* [Ce que vous allez construire](#ce-que-vous-allez-construire)
    
* [Construction de notre backend Python](#construction-de-notre-backend-python)
    
    * [Création d'un compte sur Groq Cloud](#creation-dun-compte-sur-groq-cloud)
        
    * [Configuration de notre projet Python](#configuration-de-notre-projet-python)
        
    * [Travail sur le codebase Python](#travail-sur-le-codebase-python)
        
    * [Exécution de notre backend Python](#execution-de-notre-backend-python)
        
* [Construction de notre frontend React](#construction-de-notre-frontend-react)
    
* [Conclusion](#conclusion)
    
* [Restez à jour avec la tech, la programmation, la productivité et l'IA](#restes-a-jour-avec-la-tech-la-programmation-la-productivite-et-lia)
    

## Prérequis

* Connaissance préalable de JavaScript, React et Python
    
* [Python](https://www.python.org/) installé et configuré localement sur votre ordinateur
    
* Un compte sur [Groq Cloud](https://groq.com/)
    
* Un éditeur de code/IDE installé comme [Cursor](https://www.cursor.com/en), [Windsurf](https://codeium.com/windsurf), ou [VS Code](https://code.visualstudio.com/)
    

## Qu'est-ce que les agents IA ?

Les agents IA sont des systèmes ou programmes informatiques conçus pour utiliser l'intelligence artificielle afin d'interagir avec leur environnement et d'atteindre certains objectifs. Ils sont capables de percevoir leur environnement - par le biais de capteurs, d'entrées utilisateur ou de données - et d'agir pour atteindre des objectifs, généralement avec un certain degré d'autonomie. Cela signifie qu'ils prendront des décisions par eux-mêmes, parfois avec peu ou pas d'intervention humaine, selon leur conception.

## Qu'est-ce qu'Agno et Groq Cloud ?

Agno est une bibliothèque légère qui vous permet de construire des agents multimodaux. C'est un moteur d'inférence IA conçu pour optimiser les LLMs pour la vitesse et les performances. Cela signifie qu'il peut fournir une inférence de modèle IA ultra-rapide avec une latence réduite et une meilleure utilisation des ressources. Il a le potentiel de remplacer les plateformes d'inférence actuelles comme NVIDIA TensorRT ou Hugging Face's Text Generation Inference (TGI).

Groq Cloud est une plateforme d'inférence IA basée sur le cloud basée sur les puces Groq LPU (Language Processing Unit), qui sont optimisées pour des charges de travail IA à ultra-faible latence. Groq est excellent pour les taux de génération de tokens à haute vitesse, ce qui le rend parfait pour les applications IA en temps réel comme les chatbots, l'aide à la programmation IA et d'autres charges de travail sensibles à la latence. La plateforme Groq Cloud offre un accès gratuit à ses grands modèles de langage (LLMs) via un niveau gratuit, mais il y a certaines limites d'utilisation.

Si vous allez sur le [Groq Cloud Playground](https://console.groq.com/playground), vous pouvez trouver des modèles LLM de différentes entreprises comme :

* Qwen
    
* DeepSeek R1
    
* Google Gemma 2
    
* Hugging Face
    
* Meta llama
    
* Mistral AI
    
* OpenAI
    

C'est génial car Groq Cloud nous donne la flexibilité de choisir parmi l'un de ces modèles LLM IA pour notre application d'agents IA. Agno agit essentiellement comme la couche d'orchestration pour plusieurs agents IA. Dans notre cas, ce serait WelcomeAgent, ProjectAgent, CareerAgent, BusinessAdvisor et ResearchAgent.

La plateforme est capable de gérer leurs conversations, la délégation de tâches et la mémoire. Lorsque l'un de nos agents IA doit raisonner ou générer une sortie, Agno utilise ensuite Groq Cloud, qui peut exécuter de grands modèles de langage (LLMs), et il le fait avec une ultra-faible latence. L'avantage est qu'il garantit des réponses rapides et efficaces. Groq Cloud lui-même n'est pas un LLM - plutôt, c'est un moteur d'inférence haute performance qui héberge et sert des LLMs de nombreux fournisseurs différents.

Pour ce projet, nous utiliserons le modèle LLaMA 3 de Meta car il offre un bon équilibre entre performance et précision et est ouvertement accessible. Cela signifie qu'il est bien adapté aux agents IA de notre site web de portfolio.

Il est intéressant de noter que nous aurions pu utiliser le modèle LLaMA de [llama.com](http://llama.com). Cependant, nous allons plutôt l'utiliser via Groq Cloud, car ainsi, nous obtenons une meilleure optimisation, plus de capacités et des réponses de meilleure qualité pour chaque agent IA. Cela est dû au fait que Groq Cloud nous donne la flexibilité de tester et de choisir entre différents modèles IA si nous le souhaitons, et cela signifie que nous pouvons obtenir le meilleur pour nos besoins.

## Ce que vous allez construire

Aujourd'hui, vous allez construire un site web de portfolio qui intègre des agents IA avec lesquels n'importe qui peut interagir. Ces agents IA sont comme des représentants du service client car n'importe qui peut leur poser des questions sur vos compétences et votre portfolio, et ils fourniront des informations à la personne.

C'est génial car cela signifie que les clients potentiels peuvent en apprendre davantage sur vous 24h/24 et 7j/7 sans avoir à vous parler lorsque vous n'êtes pas disponible. Vous pourriez même utiliser ce portfolio comme modèle pour construire votre site web de portfolio ou comme inspiration pour en créer un.

Au total, il y aura cinq agents IA sur votre site web de portfolio :

* WelcomeAgent : un spécialiste pour aider les utilisateurs à naviguer sur le site web, que l'utilisateur soit un employeur, un client ou un fellow programmer
    
* ProjectAgent : un spécialiste des projets qui peut fournir des informations sur les projets, la technologie et les défis
    
* CareerAgent : un spécialiste de carrière qui peut fournir des informations sur les compétences, l'expérience et le parcours professionnel
    
* BusinessAdvisor : un spécialiste client qui peut fournir des informations sur les services, les tarifs et les détails des projets
    
* ResearchAgent : un spécialiste de la recherche qui peut fournir des informations sur la technologie, les tendances et les actualités du secteur
    

L'avantage majeur d'intégrer des agents IA dans un site web de portfolio est qu'ils peuvent créer une expérience personnalisée en offrant une expérience interactive sur mesure et non facilement réplicable sur d'autres sites web plus génériques.

Cela peut distinguer votre site web car, contrairement à un site web statique pour mettre en valeur votre talent, un agent IA est capable de guider les visiteurs, de répondre aux questions sur vos projets et de recommander des travaux pertinents en fonction d'un intérêt.

Une autre fonctionnalité intéressante est la capacité de simuler une conversation, ce qui peut rendre le portfolio plus dynamique, engageant et immersif tout en démontrant votre maîtrise des outils modernes.

Tout cela combiné vous offre une manière pratique et accessible d'explorer les agents IA. Cela peut être un exemple concret et un projet personnel qui ne nécessite pas la mise en œuvre d'une application commerciale à grande échelle pour voir à quel point ce type de concept peut être précieux.

Le site web comportera les six pages suivantes :

* Accueil – la page web principale
    
* Projets – mettant en avant certains projets et compétences techniques
    
* Carrière – montrant les compétences, l'expérience, l'éducation et les certifications
    
* Services – services clients et processus d'engagement
    
* Recherche – un moyen de rechercher sur le web concernant l'industrie technologique
    
* Contact – une page avec un formulaire pour contacter l'utilisateur
    

Vous pouvez voir à quoi ressemblera votre application frontend React ci-dessous :

Tout d'abord, vous avez votre page d'accueil de portfolio :

![Page d'accueil du portfolio IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977313487/4ac8fd65-4d3a-4da1-80b8-4b4ff5136e7e.png align="center")

Ensuite, votre page Projets :

![Page Projets du portfolio IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977426609/1c05544d-5255-40c2-85da-d072c8ecd6fc.png align="center")

Maintenant, vous avez votre page Carrière :

![Page Carrière du portfolio IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977482985/ce61c17e-d948-49b5-83fa-7a77556796b5.png align="center")

Ensuite, vous avez la page Services :

![Page Services du portfolio IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977517562/45614042-68b1-466a-9c43-b5f6aa5fde26.png align="center")

Ensuite, vous pouvez voir votre page Recherche et Insights :

![Page Recherche & Insights du portfolio IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977558018/c2c083be-bd9a-4fac-9713-ff6c895d0cb0.png align="center")

Enfin, vous avez votre page Contact :

![Page Contactez-moi IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977630020/3c73726a-7de2-46af-a474-ce03fa3ace7b.png align="center")

Maintenant, commençons à construire votre application, en commençant par le backend Python.

## Construction de notre backend Python

Pour ce tutoriel, j'utiliserai macOS, et les commandes devraient également fonctionner sur Linux. Si vous êtes un utilisateur Windows, la plupart des commandes devraient fonctionner (bien qu'il y ait quelques différences comme l'activation d'un environnement Python). Vous pouvez trouver les commandes correctes en recherchant si nécessaire - et vous saurez si votre terminal vous donne des erreurs lorsque vous essayez d'exécuter une commande.

### Création d'un compte sur Groq Cloud

Comme mentionné précédemment, nous utiliserons le LLaMA 3 de Meta via Groq Cloud, ce qui est idéal. Donc, tout d'abord, nous devons créer un compte sur [Groq Cloud](https://console.groq.com/login), comme montré ici.

![Création d'un compte sur Groq Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977123301/80f8a1a6-de52-4a3d-870a-25c1067c13eb.png align="center")

Une fois que vous avez créé un compte sur Groq Cloud, allez sur la page des clés API et créez une clé API comme montré dans cet exemple. J'ai donné à la mienne le nom `team-ai-agents` :

![Création d'une clé API Groq Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977205655/7c7dcc3e-685b-4383-b80a-4d8088be7d2d.png align="center")

Vous devriez avoir une clé API qui ressemble à cet exemple, alors assurez-vous de la sauvegarder quelque part en sécurité - nous en aurons besoin plus tard.

```shell
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
```

### Configuration de notre projet Python

D'accord, maintenant, configurons rapidement notre projet. Naviguez vers un emplacement sur votre ordinateur, comme le bureau, et créez un dossier appelé `ai-agent-app`. `cd` dans le dossier du projet et préparez-vous - nous allons commencer à construire notre backend en utilisant Python.

Je recommande d'installer `agno` et `groq` localement dans un environnement virtuel Python. Tout d'abord, utilisez cette commande de terminal pour configurer un environnement virtuel Python à l'intérieur de votre dossier `ai-agent-app` :

```shell
python3 -m venv venv
source venv/bin/activate
cd venv
```

Note : selon votre environnement Python local, vous devrez peut-être utiliser la commande `python` ou `python3` pour exécuter les commandes Python. Dans mon environnement et mes exemples, j'utilise `python3`, alors ajustez la commande à vos besoins.

Il en va de même lorsque vous utilisez `pip` ou `pip3` lors de l'installation de packages Python. Vous pouvez vérifier quelle version de Python et de pip vous avez installée avec les commandes `python --version`, `python3 --version`, `pip --version` et `pip3 --version` dans votre fenêtre de terminal.

La commande ci-dessus devrait créer un dossier `venv` à l'intérieur de votre dossier `ai-agent-app`. Ce sera votre backend REST avec toutes vos endpoints API que votre frontend React utilisera plus tard dans ce tutoriel. Votre environnement virtuel Python a également été activé.

Pour activer et désactiver votre environnement Python, vous pouvez utiliser ces commandes :

```shell
# Activer sur macOS/Linux
source venv/bin/activate

# Activer sur Windows
venv\Scripts\activate

# Désactiver fonctionne sur toutes les plateformes
conda deactivate
```

À ce stade, il est bon d'ouvrir le projet dans votre éditeur de code. Maintenant, vous devrez installer `agno` et `groq` en utilisant `pip` ainsi que quelques autres packages : `flask`, `requests`, et `python-dotenv`. Vous avez besoin de ces packages pour configurer votre environnement serveur, alors installez-les tous avec cette commande :

```shell
pip install agno
pip install groq
pip install flask
pip install flask_cors
pip install requests
pip install python-dotenv
```

Avec ces packages Python installés, vous êtes maintenant prêt à configurer votre API pour ce projet. Nous allons utiliser le framework d'application web Python Flask, ainsi que le package CORS afin que nous puissions accéder au serveur n'importe où. En même temps, nous allons également utiliser le module requests, qui nous permet d'envoyer des requêtes HTTP en utilisant Python.

Notez que vous aurez également besoin d'un fichier `.env` pour vos clés API, alors assurez-vous d'avoir installé le package `python-dotenv` dans votre environnement Python, bien que dans certains cas, il soit installé automatiquement.

### Travail sur le codebase Python

D'accord, il est temps de commencer à travailler sur le codebase. Mais d'abord, générons tous les fichiers pour votre projet. Vous pouvez le faire simplement en exécutant le script que j'ai créé pour le projet. Exécutez cette commande dans le dossier `venv` :

```shell
mkdir agents
touch .env main.py
cd agents
touch __init__.py base_agent.py career_agent.py client_agent.py project_agent.py research_agent.py welcome_agent.py
```

Avec ce script, vous devriez maintenant avoir :

* Créé un fichier `.env` pour vos clés API
    
* Créé un dossier agents avec tous les fichiers pour créer vos différents agents IA
    
* Créé un fichier `main.py`, qui sera le fichier principal du projet pour toute votre application backend
    

D'accord, vos fichiers sont prêts. Il ne reste plus qu'à ajouter le codebase, et le backend est complet. Commençons par le fichier `.env`, car il ne nécessite qu'une ligne de code et c'est pour votre clé API. Voir mon exemple et mettez-le à jour avec votre propre clé API :

```shell
GROQ_API_KEY="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"
```

Votre application dispose maintenant d'une clé API, qui vous donne accès à Groq Cloud. Maintenant, commençons à ajouter le code pour tous les différents agents IA. Le premier fichier sur lequel nous allons travailler sera le `__init__.py` qui contient les imports pour tous les fichiers d'agents IA.

Ajoutez ce code au fichier :

```python
from agents.welcome_agent import WelcomeAgent
from agents.project_agent import ProjectAgent
from agents.career_agent import CareerAgent
from agents.client_agent import ClientAgent
from agents.research_agent import ResearchAgent

# Exporter tous les agents
__all__ = ['WelcomeAgent', 'ProjectAgent', 'CareerAgent', 'ClientAgent', 'ResearchAgent']
```

Comme vous pouvez le voir, toutes les classes pour les agents IA seront importées et exportées depuis ici afin que vous puissiez les utiliser dans votre fichier `main.py` plus tard.

D'accord, bien. Maintenant, nous avons 6 fichiers d'agents IA à travailler, en commençant par le fichier `base_agent.py`.

Assurez-vous d'ajouter ce code au fichier :

```python
from agno.agent import Agent
from agno.models.groq import Groq
import os


class BaseAgent:
    def __init__(self, name, description, avatar="default_avatar.png"):

        self.name = name
        self.description = description
        self.avatar = avatar
        self.model = Groq(id="llama-3.3-70b-versatile")
        self.agent = Agent(model=self.model, markdown=True)

    def get_response(self, query, stream=False):

        return self.agent.get_response(query, stream=stream)

    def print_response(self, query, stream=True):

        return self.agent.print_response(query, stream=stream)
```

Cette classe utilise le framework `agno` pour créer des agents IA alimentés par le modèle LLama 3.3 70B de Groq, qui est gratuit à utiliser avec certaines restrictions d'utilisation pour les appels API. Cela devrait être bien pour votre projet. Elle fournit la structure de base que d'autres agents spécialisés dans l'application peuvent hériter et étendre avec des fonctionnalités spécifiques au domaine.

Le modèle que nous avons choisi est disponible sur la plateforme Groq Cloud, et nous pouvons le changer si nous le souhaitons. Chaque modèle a des avantages et des inconvénients, et une date de coupure pour savoir à quel point il est à jour, donc vous pouvez vous attendre à obtenir des résultats différents. Gardez simplement à l'esprit que l'utilisation d'un LLM à jour comme OpenAI fournira de meilleurs résultats, mais vous devrez peut-être payer pour cela.

Le fichier suivant sur lequel nous allons travailler sera le fichier `career_agent.py`.

Et voici le code requis pour celui-ci :

```python
from agents.base_agent import BaseAgent


class CareerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CareerGuide",
            description="Je suis le spécialiste de carrière. Je peux fournir des informations sur les compétences, l'expérience et l'adéquation aux emplois.",
            avatar="career_avatar.png"
        )

        self.skills = {
            "languages": ["Python", "JavaScript", "TypeScript", "Java", "SQL"],
            "frameworks": ["React", "Vue.js", "Node.js", "Django", "Flask", "Spring Boot"],
            "tools": ["Git", "Docker", "AWS", "Azure", "CI/CD", "Kubernetes"],
            "soft_skills": ["Leadership d'équipe", "Gestion de projet", "Méthodologies Agile", "Rédaction technique", "Communication client"]
        }

        self.experience = [
            {
                "title": "Développeur Full Stack Senior",
                "company": "Tech Innovations Inc.",
                "period": "2020-Présent",
                "responsibilities": [
                    "Dirigé le développement d'une plateforme SaaS basée sur le cloud",
                    "Géré une équipe de 5 développeurs",
                    "Implémenté un pipeline CI/CD réduisant le temps de déploiement de 40%",
                    "Architecturé une infrastructure de microservices"
                ]
            },
            {
                "title": "Développeur Full Stack",
                "company": "WebSolutions Co.",
                "period": "2017-2020",
                "responsibilities": [
                    "Développé des applications web réactives utilisant React et Node.js",
                    "Implémenté des API RESTful et des schémas de base de données",
                    "Collaboré avec des designers UX/UI pour implémenter des interfaces conviviales",
                    "Participé à des revues de code et mentoré des développeurs juniors"
                ]
            },
            {
                "title": "Développeur Junior",
                "company": "StartUp Labs",
                "period": "2015-2017",
                "responsibilities": [
                    "Construire et maintenir des sites web clients",
                    "Développé des plugins WordPress personnalisés",
                    "Implémenté des designs réactifs et une compatibilité multi-navigateurs",
                    "Assisté dans la conception et l'optimisation de bases de données"
                ]
            }
        ]

    def get_skills_summary(self):

        prompt = f"""
        Générer un résumé professionnel des compétences suivantes pour un site web de portfolio :

        Langages de programmation : {', '.join(self.skills['languages'])}
        Frameworks & Bibliothèques : {', '.join(self.skills['frameworks'])}
        Outils & Plateformes : {', '.join(self.skills['tools'])}
        Compétences douces : {', '.join(self.skills['soft_skills'])}

        Formater la réponse en markdown avec des sections et des points forts appropriés.
        """
        return self.get_response(prompt)

    def get_experience_summary(self):

        experience_text = "# Expérience professionnelle\n\n"
        for job in self.experience:
            experience_text += f"## {job['title']} chez {job['company']}\n"
            experience_text += f"**{job['period']}**\n\n"
            experience_text += "**Responsabilités :**\n"
            for resp in job['responsibilities']:
                experience_text += f"- {resp}\n"
            experience_text += "\n"

        prompt = f"""
        Sur la base de l'expérience professionnelle suivante, générer un résumé de carrière professionnel pour un site web de portfolio :

        {experience_text}

        Mettre en avant la progression de carrière, les réalisations clés et la croissance. Formater la réponse en markdown.
        """
        return self.get_response(prompt)

    def assess_job_fit(self, job_description):

        skills_flat = []
        for skill_category in self.skills.values():
            skills_flat.extend(skill_category)

        experience_flat = []
        for job in self.experience:
            experience_flat.extend(job['responsibilities'])

        prompt = f"""
        Évaluer l'adéquation pour la description de poste suivante en fonction des compétences et de l'expérience fournies :

        Description du poste :
        {job_description}

        Compétences :
        {', '.join(skills_flat)}

        Expérience :
        {' '.join(experience_flat)}

        Fournir une analyse des forces, des lacunes potentielles et de l'adéquation globale pour le rôle. Formater la réponse en markdown.
        """
        return self.get_response(prompt)
```

Cet agent est conçu pour aider les utilisateurs avec des tâches liées à la carrière telles que :

* Créer des résumés professionnels des compétences techniques et douces
    
* Générer des récits de carrière basés sur l'expérience de travail
    
* Évaluer l'adéquation à un emploi en comparant les compétences et l'expérience avec les descriptions de poste
    

L'agent utilise les capacités LLM de l'agent de base (en utilisant le modèle LLama 3.3 70B de Groq) pour générer des réponses en langage naturel qui sont formatées en markdown, les rendant adaptées pour l'inclusion dans des sites web de portfolio, des CV ou des candidatures. Ce fichier contient des données de carrière d'exemple, et dans une implémentation réelle, celles-ci proviendraient d'une base de données.

D'accord, il est temps de passer au prochain agent IA - cette fois, c'est le fichier `client_agent.py`, qui reçoit ce code :

```python
from agents.base_agent import BaseAgent


class ClientAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="BusinessAdvisor",
            description="Je suis le spécialiste client. Je peux fournir des informations sur les services, les tarifs et les détails des projets.",
            avatar="client_avatar.png"
        )

        self.services = {
            "web_development": {
                "name": "Développement Web",
                "description": "Développement d'applications web personnalisées utilisant des frameworks modernes et les meilleures pratiques.",
                "pricing_model": "Basé sur le projet ou à l'heure",
                "price_range": "5 000 $ - 50 000 $ selon la complexité",
                "timeline": "4-12 semaines selon l'ampleur",
                "technologies": ["React", "Vue.js", "Node.js", "Django", "Flask"]
            },
            "mobile_development": {
                "name": "Développement d'applications mobiles",
                "description": "Développement d'applications mobiles natives et multiplateformes pour iOS et Android.",
                "pricing_model": "Basé sur le projet",
                "price_range": "8 000 $ - 60 000 $ selon la complexité",
                "timeline": "6-16 semaines selon l'ampleur",
                "technologies": ["React Native", "Flutter", "Swift", "Kotlin"]
            },
            "consulting": {
                "name": "Conseil technique",
                "description": "Conseils d'expert sur l'architecture, la pile technologique et les pratiques de développement.",
                "pricing_model": "À l'heure",
                "price_range": "150 $ - 250 $ par heure",
                "timeline": "En cours ou selon les besoins",
                "technologies": ["Divers selon les besoins du client"]
            }
        }

        self.process = [
            "Consultation initiale pour comprendre les exigences",
            "Préparation de la proposition et du devis",
            "Signature du contrat et lancement du projet",
            "Phase de conception et de prototypage",
            "Sprints de développement avec retour régulier du client",
            "Tests et assurance qualité",
            "Déploiement et lancement",
            "Support et maintenance post-lancement"
        ]

    def get_services_overview(self):

        services_text = "# Services proposés\n\n"
        for service_id, service in self.services.items():
            services_text += f"## {service['name']}\n"
            services_text += f"{service['description']}\n\n"
            services_text += f"**Modèle de tarification** : {service['pricing_model']}\n"
            services_text += f"**Fourchette de prix** : {service['price_range']}\n"
            services_text += f"**Calendrier** : {service['timeline']}\n"
            services_text += f"**Technologies** : {', '.join(service['technologies'])}\n\n"

        prompt = f"""
        Générer un aperçu professionnel des services suivants pour le site web de portfolio d'un programmeur :

        {services_text}

        Formater la réponse en markdown avec des sections et des points forts appropriés.
        """
        return self.get_response(prompt)

    def get_service_details(self, service_id):

        if service_id in self.services:
            service = self.services[service_id]
            prompt = f"""
            Générer une description détaillée pour le service suivant :

            Nom du service : {service['name']}
            Description : {service['description']}
            Modèle de tarification : {service['pricing_model']}
            Fourchette de prix : {service['price_range']}
            Calendrier : {service['timeline']}
            Technologies : {', '.join(service['technologies'])}

            Inclure des informations sur la proposition de valeur, les livrables typiques et les avantages pour le client. Formater la réponse en markdown.
            """
            return self.get_response(prompt)
        else:
            return "Service non trouvé. Veuillez vérifier l'ID du service et réessayer."

    def explain_process(self):

        process_text = "# Processus d'engagement client\n\n"
        for i, step in enumerate(self.process, 1):
            process_text += f"## Étape {i} : {step}\n\n"

        prompt = f"""
        Sur la base du processus d'engagement client suivant, générer une explication détaillée pour les clients potentiels :

        {process_text}

        Pour chaque étape, fournir une brève explication de ce qui se passe, de ce à quoi le client peut s'attendre et des livrables. Formater la réponse en markdown.
        """
        return self.get_response(prompt)

    def generate_proposal(self, project_description):

        prompt = f"""
        Générer une proposition de projet professionnelle basée sur les exigences suivantes du client :

        Description du projet :
        {project_description}

        Inclure les sections suivantes :
        1. Compréhension du projet
        2. Approche proposée
        3. Calendrier estimé
        4. Fourchette de budget estimée
        5. Prochaines étapes

        Baser votre proposition sur les services et processus décrits dans le portfolio. Formater la réponse en markdown.
        """
        return self.get_response(prompt)
```

Cet agent est conçu pour aider les utilisateurs avec des tâches liées aux clients et aux affaires telles que :

* Fournir des aperçus des services disponibles pour les supports marketing
    
* Générer des descriptions de services détaillées pour des offres spécifiques
    
* Expliquer le processus d'engagement client aux clients potentiels
    
* Créer des propositions de projet personnalisées basées sur les exigences des clients
    

L'agent utilise également les capacités LLM de l'agent de base (en utilisant le modèle LLama 3.3 70B de Groq) pour générer du contenu professionnel et orienté business formaté en markdown. Comme avant, ce fichier contient également des données de service d'exemple.

Maintenant, nous pouvons commencer à travailler sur le fichier `project_agent.py` et ajouter ce code à son codebase :

```python
from agents.base_agent import BaseAgent


class ProjectAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="TechExpert",
            description="Je suis le spécialiste des projets. Je peux fournir des informations détaillées sur tout projet de ce portfolio.",
            avatar="project_avatar.png"
        )

        self.projects = {
            "project1": {
                "name": "Plateforme E-commerce",
                "tech_stack": ["React", "Node.js", "MongoDB", "Express"],
                "description": "Une plateforme e-commerce full-stack avec authentification utilisateur, catalogue de produits, panier d'achat et traitement des paiements.",
                "highlights": ["Design réactif", "API RESTful", "Intégration Stripe", "Authentification JWT"],
                "github_link": "https://github.com/username/ecommerce-platform",
                "demo_link": "https://ecommerce-demo.example.com"
            },
            "project2": {
                "name": "Application de gestion des tâches",
                "tech_stack": ["Vue.js", "Firebase", "Tailwind CSS"],
                "description": "Une application de gestion des tâches en temps réel avec des fonctionnalités collaboratives, des notifications et un suivi des progrès.",
                "highlights": ["Mises à jour en temps réel", "Collaboration utilisateur", "Interface glisser-déposer", "Application Web Progressive"],
                "github_link": "https://github.com/username/task-manager",
                "demo_link": "https://taskmanager-demo.example.com"
            },
            "project3": {
                "name": "Tableau de bord de visualisation de données",
                "tech_stack": ["Python", "Django", "D3.js", "PostgreSQL"],
                "description": "Un tableau de bord interactif pour visualiser des ensembles de données complexes avec des fonctionnalités de filtrage, de tri et d'exportation.",
                "highlights": ["Graphiques interactifs", "Filtrage des données", "Exportation CSV/PDF", "Design réactif"],
                "github_link": "https://github.com/username/data-dashboard",
                "demo_link": "https://dataviz-demo.example.com"
            }
        }

    def get_project_list(self):

        project_list = "# Projets disponibles\n\n"
        for project_id, project in self.projects.items():
            project_list += f"## {project['name']}\n"
            project_list += f"**Pile technologique** : {', '.join(project['tech_stack'])}\n"
            project_list += f"{project['description']}\n\n"

        return project_list

    def get_project_details(self, project_id):

        if project_id in self.projects:
            project = self.projects[project_id]
            prompt = f"""
            Générer une description détaillée pour le projet suivant :

            Nom du projet : {project['name']}
            Pile technologique : {', '.join(project['tech_stack'])}
            Description : {project['description']}
            Points forts : {', '.join(project['highlights'])}
            GitHub : {project['github_link']}
            Démo : {project['demo_link']}

            Inclure des détails techniques sur les défis d'implémentation et les solutions. Formater la réponse en markdown.
            """
            return self.get_response(prompt)
        else:
            return "Projet non trouvé. Veuillez vérifier l'ID du projet et réessayer."

    def answer_technical_question(self, project_id, question):

        if project_id in self.projects:
            project = self.projects[project_id]
            prompt = f"""
            Répondre à la question technique suivante sur ce projet :

            Nom du projet : {project['name']}
            Pile technologique : {', '.join(project['tech_stack'])}
            Description : {project['description']}
            Points forts : {', '.join(project['highlights'])}

            Question : {question}

            Fournir une réponse technique détaillée avec des exemples de code si pertinent.
            """
            return self.get_response(prompt)
        else:
            return "Projet non trouvé. Veuillez vérifier l'ID du projet et réessayer."
```

Cet agent est conçu pour aider les utilisateurs avec des tâches liées aux projets telles que :

* Fournir un aperçu de tous les projets dans un portfolio
    
* Générer des descriptions détaillées de projets spécifiques
    
* Répondre à des questions techniques sur les détails d'implémentation
    

L'agent, comme dans les exemples précédents, utilise les capacités LLM de l'agent de base (en utilisant le modèle LLama 3.3 70B de Groq) pour générer du contenu technique et orienté projet formaté en markdown. Cela est bon pour la documentation technique, ou lors de la réponse à des demandes concernant les implémentations de projets. Nous utilisons des données fictives ici plutôt qu'une base de données.

Avec ce fichier complété, il nous en reste deux. Le suivant est le fichier `research_agent.py`, alors ajoutez ce code :

```python
from agents.base_agent import BaseAgent
import requests
import os
import json


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ResearchAssistant",
            description="Je suis le spécialiste de la recherche. Je peux rechercher sur le web des informations sur les technologies, les tendances et les actualités du secteur.",
            avatar="research_avatar.png"
        )
        self.api_key = os.getenv("GROQ_API_KEY")

    def search_web(self, query):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "Vous êtes un assistant de recherche utile."},
                {"role": "user", "content": f"Rechercher sur le web pour : {query}"}
            ],
            "tools": [
                {
                    "type": "web_search"
                }
            ]
        }

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"Erreur lors de la recherche sur le web : {response.status_code} - {response.text}"
        except Exception as e:
            return f"Erreur lors de la recherche sur le web : {str(e)}"

    def research_technology(self, technology):

        query = f"derniers développements et meilleures pratiques pour {technology} dans le développement logiciel"
        search_results = self.search_web(query)

        prompt = f"""
        Sur la base des résultats de recherche suivants concernant {technology}, fournir un résumé concis de :
        1. Ce que c'est
        2. État actuel et popularité
        3. Fonctionnalités et avantages clés
        4. Cas d'utilisation courants
        5. Tendances futures

        Résultats de recherche :
        {search_results}

        Formater la réponse en markdown avec des sections appropriées.
        """
        return self.get_response(prompt)

    def compare_technologies(self, tech1, tech2):

        query = f"comparaison entre {tech1} et {tech2} pour le développement logiciel"
        search_results = self.search_web(query)

        prompt = f"""
        Sur la base des résultats de recherche suivants comparant {tech1} et {tech2}, fournir une comparaison détaillée incluant :
        6. Différences principales
        7. Considérations de performance
        8. Courbe d'apprentissage
        9. Support communautaire
        10. Recommandations de cas d'utilisation

        Résultats de recherche :
        {search_results}

        Formater la réponse en markdown avec un tableau de comparaison et un texte explicatif.
        """
        return self.get_response(prompt)

    def get_industry_trends(self):

        query = "dernières tendances dans l'industrie du développement logiciel"
        search_results = self.search_web(query)

        prompt = f"""
        Sur la base des résultats de recherche suivants concernant les tendances du développement logiciel, fournir un résumé de :
        11. Technologies émergentes
        12. Changements dans l'industrie
        13. Compétences recherchées
        14. Prédictions futures

        Résultats de recherche :
        {search_results}

        Formater la réponse en markdown avec des sections et des points forts appropriés.
        """
        return self.get_response(prompt)
```

Cet agent est conçu pour aider les utilisateurs avec des tâches de recherche telles que :

* Rechercher des technologies spécifiques pour comprendre leurs fonctionnalités, avantages et cas d'utilisation
    
* Comparer différentes technologies pour prendre des décisions éclairées
    
* Rester à jour sur les tendances de l'industrie et les technologies émergentes
    

Ce qui rend cet agent unique par rapport aux autres agents est qu'il récupère activement des informations en temps réel sur le web en utilisant la capacité de recherche web de l'API Groq Toolhouse au lieu de s'appuyer uniquement sur des données prédéfinies ou sur les données d'entraînement du LLM. Cela lui permet de fournir des informations plus actuelles et complètes sur des sujets technologiques en rapide évolution.

D'accord, nous avons un dernier agent IA à créer et c'est le fichier `welcome_agent.py`. Ajoutez ce code au fichier :

```python
from agents.base_agent import BaseAgent


class WelcomeAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Greeter",
            description="Je suis l'agent d'accueil de ce portfolio. Je peux vous aider à vous orienter vers la bonne section en fonction de vos intérêts.",
            avatar="welcome_avatar.png"
        )

    def greet(self, visitor_type=None):

        if visitor_type == "employer":
            return self.get_response(
                "Générer un message d'accueil amical et professionnel pour un employeur potentiel visitant le site web de portfolio d'un programmeur. "
                "Mentionner qu'ils peuvent explorer la section Projets pour voir les compétences techniques et la section Carrière pour l'expérience professionnelle."
            )
        elif visitor_type == "client":
            return self.get_response(
                "Générer un message d'accueil amical et orienté business pour un client potentiel visitant le site web de portfolio d'un programmeur. "
                "Mentionner qu'ils peuvent consulter la section Projets pour des exemples de travaux passés et la section Client pour les détails des services."
            )
        elif visitor_type == "fellow_programmer":
            return self.get_response(
                "Générer un message d'accueil amical et décontracté pour un fellow programmer visitant un site web de portfolio. "
                "Mentionner qu'ils peuvent explorer la section Projets pour les détails techniques et les exemples de code."
            )
        else:
            return self.get_response(
                "Générer un message d'accueil amical et général pour un visiteur du site web de portfolio d'un programmeur. "
                "Demander s'ils sont un employeur, un client ou un fellow programmer pour fournir des informations plus adaptées."
            )

    def suggest_section(self, interest):

        prompt = f"Sur la base d'un visiteur exprimant un intérêt pour '{interest}', suggérer quelle section du portfolio d'un programmeur ils devraient visiter. Les options incluent : Projets, Carrière, Travail client, À propos de moi, Contact. Expliquer pourquoi en 1-2 phrases."
        return self.get_response(prompt)
```

Cet agent est conçu pour servir de premier point de contact pour les visiteurs d'un site web de portfolio, fournissant :

* Des salutations personnalisées en fonction du type de visiteur
    
* Des conseils vers des sections pertinentes en fonction d'intérêts spécifiques
    
* Une introduction amicale et conversationnelle au portfolio
    

Le `WelcomeAgent` est plus simple que certains des autres agents que nous avons vus car il se concentre sur la création d'une bonne première impression et aide les visiteurs à naviguer vers le contenu le plus pertinent pour leurs besoins. Il utilise les capacités LLM de l'agent de base pour générer des réponses naturelles et contextuellement appropriées.

D'accord, bien - votre API backend est presque prête. Il ne vous reste plus qu'un dernier fichier à travailler : le fichier `main.py` qui complète votre codebase. Ce fichier est assez grand, donc je vais le diviser en trois parties. Vous devrez copier et coller chaque section dans le fichier. Si vous ne l'avez pas encore fait, il est utile d'installer l'extension [Python](https://open-vsx.org/extension/ms-python/python) pour VS Code car elle offre le débogage, le linting et le formatage pour les fichiers Python.

D'accord, voici la première partie du codebase pour notre fichier `main.py` :

```python
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import json
import requests
from flask_cors import CORS


load_dotenv()


app = Flask(__name__)
CORS(app)


class BaseAgent:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.api_key = os.getenv("GROQ_API_KEY")

    def get_response(self, prompt):

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": f"Vous êtes {self.name}, {self.description}. Répondez de manière utile, concise et professionnelle."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Erreur : {response.status_code} - {response.text}"
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"


class WelcomeAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "WelcomeAgent",
            "un spécialiste de l'accueil qui salue les visiteurs et les aide à naviguer sur le site web du portfolio"
        )

    def greet(self, visitor_type=None):
        if visitor_type == "employer":
            return self.get_response("Générer un message de bienvenue chaleureux pour un employeur visitant le site web de portfolio d'un programmeur. Suggérer de consulter les sections Projets et Carrière.")
        elif visitor_type == "client":
            return self.get_response("Générer un message de bienvenue chaleureux pour un client potentiel visitant le site web de portfolio d'un programmeur. Suggérer de consulter la section Services.")
        elif visitor_type == "fellow_programmer":
            return self.get_response("Générer un message de bienvenue chaleureux pour un fellow programmer visitant le site web de portfolio d'un programmeur. Suggérer de consulter les sections Projets et Recherche.")
        else:
            return self.get_response("Générer un message de bienvenue général pour un visiteur du site web de portfolio d'un programmeur. Demander s'ils sont un employeur, un client ou un fellow programmer.")

    def suggest_section(self, interest):
        return self.get_response(f"Un visiteur de mon site web de portfolio a exprimé un intérêt pour {interest}. Suggérer quelle(s) section(s) du site web ils devraient visiter en fonction de cet intérêt.")


class ProjectAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "ProjectAgent",
            "un spécialiste des projets qui fournit des informations détaillées sur les projets du programmeur"
        )

    def get_project_list(self):
        return self.get_response("Générer une liste de 3-5 projets de développement logiciel impressionnants qui pourraient figurer dans le portfolio d'un programmeur. Inclure une brève description pour chacun.")

    def get_project_details(self, project_id):
        project_prompts = {
            "project1": "Décrivez en détail un projet de plateforme e-commerce pour le portfolio d'un programmeur. Inclure les technologies utilisées, les défis surmontés et les fonctionnalités clés.",
            "project2": "Décrivez en détail un projet d'application de gestion des tâches pour le portfolio d'un programmeur. Inclure les technologies utilisées, les défis surmontés et les fonctionnalités clés.",
            "project3": "Décrivez en détail un projet de tableau de bord de visualisation de données pour le portfolio d'un programmeur. Inclure les technologies utilisées, les défis surmontés et les fonctionnalités clés."
        }

        prompt = project_prompts.get(
            project_id, f"Décrivez un projet appelé {project_id} en détail.")
        return self.get_response(prompt)

    def answer_technical_question(self, project_id, question):
        return self.get_response(f"Répondez à cette question technique sur un projet : '{question}'. Le projet est {project_id}.")
```

Cette partie du code contient vos imports, la configuration et quelques salutations pour l'agent IA.

Maintenant, pour la deuxième partie, ajoutez ce code au fichier sous le premier code que vous avez ajouté :

```python

class CareerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "CareerAgent",
            "un spécialiste de carrière qui fournit des informations sur les compétences et l'expérience du programmeur"
        )

    def get_skills_summary(self):
        return self.get_response("Générer un résumé complet des compétences techniques et professionnelles pour le portfolio d'un développeur full-stack.")

    def get_experience_summary(self):
        return self.get_response("Générer un résumé de l'expérience de travail pour un développeur full-stack avec plus de 5 ans d'expérience.")

    def assess_job_fit(self, job_description):
        return self.get_response(f"Évaluer dans quelle mesure un développeur full-stack avec plus de 5 ans d'expérience conviendrait à cette description de poste : '{job_description}'. Mettre en avant les compétences et l'expérience correspondantes.")


class ClientAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "ClientAgent",
            "un spécialiste client qui fournit des informations sur les services, les tarifs et le processus d'engagement client"
        )

    def get_services_overview(self):
        return self.get_response("Générer un aperçu des services qu'un développeur full-stack freelance pourrait offrir à ses clients.")

    def get_service_details(self, service_type):
        service_prompts = {
            "web_development": "Décrivez les services de développement web offerts par un développeur full-stack freelance, y compris les technologies, la fourchette de prix et le calendrier typique.",
            "mobile_development": "Décrivez les services de développement d'applications mobiles offerts par un développeur full-stack freelance, y compris les technologies, la fourchette de prix et le calendrier typique.",
            "consulting": "Décrivez les services de conseil technique offerts par un développeur full-stack freelance, y compris les domaines d'expertise, la fourchette de tarifs horaires et le modèle d'engagement."
        }

        prompt = service_prompts.get(
            service_type, f"Décrivez les services {service_type} en détail.")
        return self.get_response(prompt)

    def explain_process(self):
        return self.get_response("Expliquez le processus d'engagement client pour un développeur full-stack freelance, de la consultation initiale à la livraison du projet.")

    def generate_proposal(self, project_description):
        return self.get_response(f"Générer une proposition de projet pour cette demande client : '{project_description}'. Inclure le calendrier estimé, la fourchette de coûts et l'approche.")


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "ResearchAgent",
            "un spécialiste de la recherche qui fournit des informations sur les technologies, les tendances et les actualités de l'industrie"
        )

    def search_web(self, query):
        return self.get_response(f"Fournir des informations sur '{query}' comme si vous veniez de rechercher sur le web les dernières informations. Inclure les points clés et les insights.")

    def compare_technologies(self, tech1, tech2):
        return self.get_response(f"Comparer {tech1} vs {tech2} en termes de fonctionnalités, de performance, de cas d'utilisation, de support communautaire et de perspectives futures.")

    def get_industry_trends(self):
        return self.get_response("Décrivez les tendances actuelles en matière de développement logiciel et de technologie qu'il est important pour les développeurs de connaître.")


welcome_agent = WelcomeAgent()
project_agent = ProjectAgent()
career_agent = CareerAgent()
client_agent = ClientAgent()
research_agent = ResearchAgent()


@app.route('/static/images/default_avatar.png')
@app.route('/static/images/default_project.jpg')
def block_default_images():

    response = app.make_response(
        b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
    response.headers['Content-Type'] = 'image/gif'

    response.headers['Cache-Control'] = 'public, max-age=31536000'
    response.headers['Expires'] = 'Thu, 31 Dec 2037 23:59:59 GMT'
    return response


@app.route('/api/welcome', methods=['POST'])
def welcome_agent_endpoint():
    data = request.json
    message = data.get('message', '')

    visitor_type = None
    if 'employer' in message.lower():
        visitor_type = 'employer'
    elif 'client' in message.lower():
        visitor_type = 'client'
    elif 'programmer' in message.lower() or 'developer' in message.lower():
        visitor_type = 'fellow_programmer'

    if 'interest' in message.lower() or 'looking for' in message.lower():

        interest = message.replace('interest', '').replace(
            'looking for', '').strip()
        response = welcome_agent.suggest_section(interest)
    else:
        response = welcome_agent.greet(visitor_type)

    return jsonify({'response': response})
```

Dans cette partie de votre codebase, vous avez plus de réponses d'IA et une route d'API de bienvenue.

Enfin, complétez le code en ajoutant cette dernière partie à la fin :

```python

@app.route('/api/project', methods=['POST'])
def project_agent_endpoint():
    data = request.json
    message = data.get('message', '')

    project_id = None
    if 'e-commerce' in message.lower() or 'ecommerce' in message.lower():
        project_id = 'project1'
    elif 'task' in message.lower() or 'management' in message.lower():
        project_id = 'project2'
    elif 'data' in message.lower() or 'visualization' in message.lower() or 'dashboard' in message.lower():
        project_id = 'project3'

    if project_id and ('tell me more' in message.lower() or 'details' in message.lower()):
        response = project_agent.get_project_details(project_id)
    elif 'list' in message.lower() or 'all projects' in message.lower():
        response = project_agent.get_project_list()
    elif project_id:

        response = project_agent.answer_technical_question(project_id, message)
    else:

        response = project_agent.get_response(
            f"L'utilisateur a demandé : '{message}'. Répondez comme si vous étiez un spécialiste des projets pour un site web de portfolio. "
            "S'ils demandent un projet spécifique, suggérez-leur de mentionner l'un des projets : "
            "Plateforme E-commerce, Application de gestion des tâches ou Tableau de bord de visualisation de données."
        )

    return jsonify({'response': response})


@app.route('/api/career', methods=['POST'])
def career_agent_endpoint():
    data = request.json
    message = data.get('message', '')

    if 'skills' in message.lower():
        response = career_agent.get_skills_summary()
    elif 'experience' in message.lower() or 'work history' in message.lower():
        response = career_agent.get_experience_summary()
    elif 'job' in message.lower() or 'position' in message.lower() or 'role' in message.lower():

        response = career_agent.assess_job_fit(message)
    else:

        response = career_agent.get_response(
            f"L'utilisateur a demandé : '{message}'. Répondez comme si vous étiez un spécialiste de carrière pour un site web de portfolio. "
            "Suggérez-leur de demander des compétences, de l'expérience ou une évaluation de l'adéquation à un emploi."
        )

    return jsonify({'response': response})


@app.route('/api/client', methods=['POST'])
def client_agent_endpoint():
    data = request.json
    message = data.get('message', '')

    if 'services' in message.lower() or 'offerings' in message.lower():
        response = client_agent.get_services_overview()
    elif 'web' in message.lower() and 'development' in message.lower():
        response = client_agent.get_service_details('web_development')
    elif 'mobile' in message.lower() and 'development' in message.lower():
        response = client_agent.get_service_details('mobile_development')
    elif 'consulting' in message.lower() or 'technical consulting' in message.lower():
        response = client_agent.get_service_details('consulting')
    elif 'process' in message.lower() or 'how does it work' in message.lower():
        response = client_agent.explain_process()
    elif 'proposal' in message.lower() or 'quote' in message.lower() or 'estimate' in message.lower():

        response = client_agent.generate_proposal(message)
    else:

        response = client_agent.get_response(
            f"L'utilisateur a demandé : '{message}'. Répondez comme si vous étiez un spécialiste client pour un site web de portfolio. "
            "Suggérez-leur de demander des services, le processus d'engagement client ou de demander une proposition."
        )

    return jsonify({'response': response})


@app.route('/api/research', methods=['POST'])
def research_agent_endpoint():
    data = request.json
    message = data.get('message', '')

    if 'compare' in message.lower() and ('vs' in message.lower() or 'versus' in message.lower()):

        tech_parts = message.lower().replace('compare', '').replace(
            'vs', ' ').replace('versus', ' ').split()
        tech1 = tech_parts[0] if len(tech_parts) > 0 else ''
        tech2 = tech_parts[-1] if len(tech_parts) > 1 else ''
        response = research_agent.compare_technologies(tech1, tech2)
    elif 'trends' in message.lower() or 'industry' in message.lower():
        response = research_agent.get_industry_trends()
    else:
        response = research_agent.search_web(message)

    return jsonify({'response': response})


if __name__ == '__main__':

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True   # Assurez-vous que les templates se rechargent

    @app.after_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    app.run(host='0.0.0.0', port=5001, debug=True,
            use_reloader=False, threaded=True)
```

D'accord, si votre fichier contient des erreurs, elles sont probablement causées par l'indentation Python. Espérons que le formatage ne les rendra pas trop difficiles à corriger.

Le fichier est maintenant complet, et vous avez créé le reste de vos routes API IA.

### Exécution de notre backend Python

Il ne reste plus qu'à exécuter votre serveur Flask et à faire fonctionner le backend. Vous pouvez le faire avec ce script d'exécution à l'intérieur du dossier `venv` :

```shell
python3 main.py
```

Votre backend devrait maintenant fonctionner sur [http://127.0.0.1:5001/](http://127.0.0.1:5001/). Si vous allez sur la page, vous verrez une erreur comme celle-ci :

```markdown
Non trouvé

L'URL demandée n'a pas été trouvée sur le serveur. Si vous avez saisi l'URL manuellement, veuillez vérifier l'orthographe et réessayer.
```

C'est attendu, car si vous avez vérifié le codebase, vous réaliserez qu'il n'y a pas de routes GET, seulement des routes POST. Pour les voir fonctionner, vous devez utiliser un client HTTP comme Postman. Une autre option est de créer quelques commandes `curl` qui envoient une requête POST, que vous pouvez exécuter depuis votre terminal. Utilisons `curl` car il y a moins de configuration. Vous devrez copier et coller les commandes.

Chaque requête POST utilisera exactement un appel API sur Groq Cloud pour votre clé API que vous pouvez consulter ici [https://console.groq.com/keys](https://console.groq.com/keys). N'oubliez pas qu'il est gratuit à utiliser mais qu'il y a des limites d'utilisation que vous pouvez lire dans leur documentation sur [Rate Limits](https://console.groq.com/docs/rate-limits).

J'ai fourni quelques exemples de commandes curl ci-dessous - il suffit de les copier et de les coller dans votre terminal et d'appuyer sur entrée, et vous devriez voir le message de réponse :

**1. Test de l'endpoint Welcome Agent**

```shell
curl -X POST http://localhost:5001/api/welcome \
  -H "Content-Type: application/json" \
  -d '{"message": "I am an employer looking for a skilled developer"}'
```

**2. Test de l'endpoint Project Agent**

```shell
curl -X POST http://localhost:5001/api/project \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me more about the e-commerce project"}'
```

**3. Test de l'endpoint Career Agent**

```shell
curl -X POST http://localhost:5001/api/career \
  -H "Content-Type: application/json" \
  -d '{"message": "What skills do you have?"}'
```

**4. Test de l'endpoint Client Agent**

```shell
curl -X POST http://localhost:5001/api/client \
  -H "Content-Type: application/json" \
  -d '{"message": "What services do you offer?"}'
```

**5. Test de l'endpoint Research Agent**

```shell
curl -X POST http://localhost:5001/api/research \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the current trends in web development?"}'
```

## Construction de notre frontend React

Nous avons atteint le point médian, et il ne reste plus qu'à construire votre frontend. Nous allons construire le frontend en utilisant [Vite](https://vite.dev/), et le site web comportera six pages. Assurez-vous que vous êtes maintenant dans le dossier racine du projet `ai-agent-app`. Vous pouvez laisser le serveur Python en cours d'exécution car votre frontend va se connecter aux routes API que vous avez créées.

Maintenant, exécutez les commandes ci-dessous pour configurer votre projet React en utilisant Vite, Tailwind CSS, react-router et Axios, dont nous avons besoin pour le routage des pages et les requêtes fetch :

```shell
npm create vite@latest frontend -- --template react
cd frontend
npm install -D tailwindcss@3 postcss autoprefixer react-router axios
npx tailwindcss init -p
npm install
```

Super, maintenant avec ces packages installés et nos dépendances configurées, nous sommes presque prêts à commencer à travailler sur le codebase. Mais avant cela, nous devons exécuter un autre script, qui va créer tous les fichiers et dossiers pour notre projet. C'est beaucoup plus rapide que de les faire tous manuellement.

Exécutez cette commande à l'intérieur du dossier frontend :

```shell
mkdir -p src/components src/pages
touch src/style.css src/components/{Chat,Footer,Layout,Navbar}.jsx
touch src/pages/{Career,Contact,Home,Projects,Research,Services}.jsx
```

Notre frontend React devrait maintenant avoir une structure de projet comme l'exemple montré ci-dessous :

![Structure du projet frontend de l'application AI Agent](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977692485/9940901d-bd7a-49dd-a18b-ab3edf5e3714.png align="center")

Nous sommes maintenant prêts à commencer à écrire du code.

Tout d'abord, le fichier `tailwind.config.js`. C'est le seul fichier de configuration sur lequel vous devrez travailler, car les autres ont déjà la configuration dont nous avons besoin. Remplacez tout le code dans le fichier par le code ci-dessous :

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

Tout ce que fait ce code est d'ajouter les chemins vers tous vos fichiers de template.

D'accord, ensuite, vous allez travailler sur vos styles et Tailwind CSS. Il y a trois fichiers CSS à travailler : `App.css`, `index.css`, et `style.css`.

Tout d'abord, le fichier `App.css`. Remplacez tout le code par ce code ici :

```css
#root {
  max-width: 100%;
  margin: 0;
  padding: 0;
  text-align: left;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}
```

Nous avons ici quelques styles de mise en page de base pour `root` et `main`.

Ensuite, le fichier `index.css`. Voici le code dont vous aurez besoin, alors remplacez tout dans le fichier par celui-ci :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family: system-ui, Avenir, Helvetica, Arial, sans-serif;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

@layer components {
  .chat-container {
    @apply w-full h-96 flex flex-col;
  }

  .chat-messages {
    @apply flex-1 overflow-y-auto p-4;
  }

  .message {
    @apply flex mb-4;
  }

  .user-message {
    @apply justify-end;
  }

  .agent-message {
    @apply justify-start;
  }

  .message-avatar {
    @apply flex-shrink-0 mr-2;
  }

  .avatar-placeholder {
    @apply w-10 h-10 rounded-full bg-blue-500 text-white flex items-center justify-center font-bold;
  }

  .message-content {
    @apply p-3 rounded-lg max-w-xs sm:max-w-sm md:max-w-md;
  }

  .user-message .message-content {
    @apply bg-blue-500 text-white;
  }

  .agent-message .message-content {
    @apply bg-gray-200 text-gray-800;
  }

  .chat-input-container {
    @apply p-4 border-t border-gray-200;
  }

  .chat-input-group {
    @apply flex;
  }

  .chat-input {
    @apply flex-1 border border-gray-300 rounded-l-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500;
  }

  .chat-send-button {
    @apply bg-blue-500 text-white px-4 py-2 rounded-r-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500;
  }

  .loading-dots:after {
    @apply content-['...'] animate-pulse;
  }

  .project-image-placeholder {
    @apply h-48 bg-gray-300 flex items-center justify-center text-gray-600 font-semibold;
  }

  .agent-avatar-placeholder {
    @apply w-16 h-16 rounded-full bg-blue-500 text-white flex items-center justify-center font-bold mx-auto;
  }
}
```

Tous ces styles concernent votre configuration Tailwind CSS dans tout votre projet.

Il ne reste plus qu'un fichier pour le CSS et c'est le fichier `style.css`. C'est un gros fichier, donc je vais le diviser en deux parties - il suffit de les copier et de les coller dans le fichier.

Voici la première partie :

```css
/* Styles principaux */
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  color: #333;
  background-color: #f8f9fa;
}

/* Styles de mise en page */
#root {
  max-width: 100%;
  margin: 0;
  padding: 0;
  text-align: left;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 600;
}

footer {
  margin-top: auto;
}

/* Styles de la barre de navigation */
.navbar {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-brand {
  font-weight: 700;
}

.navbar .container {
  max-width: 1320px;
}

/* Styles des cartes */
.card {
  border: none;
  border-radius: 0.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  margin-bottom: 1rem;
  padding: 2em;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

/* Styles des agents */
.agent-avatar-placeholder {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: #6c757d;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: bold;
  margin: 0 auto;
  border: 3px solid #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.avatar-placeholder {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #6c757d;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: bold;
}

/* Styles du conteneur de chat */
.chat-container {
  display: flex;
  flex-direction: column;
  height: 400px;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  overflow: hidden;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  background-color: #f8f9fa;
}
```

Et voici la deuxième partie :

```css
.chat-input-container {
  padding: 0.5rem;
  background-color: #fff;
  border-top: 1px solid #dee2e6;
}

.chat-input-group {
  display: flex;
}

.chat-input {
  flex: 1;
  margin-right: 0.5rem;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  padding: 0.5rem;
}

.chat-send-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 0.25rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.chat-send-button:hover {
  background-color: #0069d9;
}

/* Styles des messages */
.message {
  margin-bottom: 1rem;
  max-width: 80%;
}

.user-message {
  margin-left: auto;
  text-align: right;
}

.agent-message {
  display: flex;
  align-items: flex-start;
}

.message-avatar {
  margin-right: 0.5rem;
}

.message-content {
  background-color: #fff;
  padding: 0.75rem;
  border-radius: 0.5rem;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.user-message .message-content {
  background-color: #007bff;
  color: #fff;
}

.agent-message .message-content {
  background-color: #fff;
}

/* Animation de chargement */
.loading-dots:after {
  content: '.';
  animation: dots 1.5s steps(5, end) infinite;
}

@keyframes dots {
  0%,
  20% {
    content: '.';
  }
  40% {
    content: '..';
  }
  60% {
    content: '...';
  }
  80%,
  100% {
    content: '';
  }
}
```

Ce code contient les styles principaux pour la mise en page du contenu du site web. Cela prend en charge le style. Il ne nous reste plus que les composants et les pages, puis vous pourrez exécuter votre application. Avant de commencer à travailler sur ces dossiers, faisons rapidement les fichiers `App.jsx` et `main.jsx` dans le dossier `src`.

Ajoutez donc ce code au fichier `App.jsx` :

```javascript
import { BrowserRouter as Router, Routes, Route } from 'react-router';
import Layout from './components/Layout';
import Home from './pages/Home';
import Projects from './pages/Projects';
import Career from './pages/Career';
import Services from './pages/Services';
import Research from './pages/Research';
import Contact from './pages/Contact';
import './App.css';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/career" element={<Career />} />
          <Route path="/services" element={<Services />} />
          <Route path="/research" element={<Research />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```

Dans ce fichier, vous avez toutes vos routes. C'est ainsi que vous naviguerez entre les pages en utilisant `BrowserRouter`.

Enfin, remplacez et mettez à jour tout le code à l'intérieur de `main.jsx` avec ceci :

```javascript
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import './style.css';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

La seule mise à jour que nous avons faite ici est l'ajout d'un import pour `import './style.css'` afin que vous puissiez maintenant accéder aux styles de ce fichier dans toute votre application.

Il est temps de travailler sur vos fichiers de composants, en commençant par le fichier `Chat.jsx`. Je l'ai divisé en deux parties car c'est un gros fichier, alors assurez-vous de tout ajouter ensemble.

Comme avant, voici la première partie :

```javascript
import { useState, useEffect, useRef, useCallback } from "react";
import axios from "axios";

function Chat({ agentType, initialMessage, agentInitials, directQuestion }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const [processedQuestions, setProcessedQuestions] = useState([]);

  const API_BASE_URL = "http://127.0.0.1:5001";

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleSendMessage = useCallback(
    async (questionOverride = null) => {
      const messageToSend = questionOverride || input;

      if (!messageToSend.trim()) return;

      const userMessage = {
        content: messageToSend,
        isUser: true,
      };

      setMessages((prev) => [...prev, userMessage]);

      if (!questionOverride) {
        setInput("");
      }

      setIsLoading(true);

      try {
        const response = await axios.post(
          `${API_BASE_URL}/api/${agentType}`,
          {
            message: messageToSend,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
            },
          }
        );

        if (response.data && response.data.response) {
          setMessages((prev) => [
            ...prev,
            {
              content: response.data.response,
              isUser: false,
            },
          ]);
        }
      } catch (error) {
        console.error("Erreur lors de l'envoi du message :", error);
        setMessages((prev) => [
          ...prev,
          {
            content:
              "Désolé, une erreur s'est produite lors de la connexion à l'agent IA. Veuillez vous assurer que le serveur Flask est en cours d'exécution à l'adresse http://127.0.0.1:5001/",
            isUser: false,
          },
        ]);
      } finally {
        setIsLoading(false);
      }
    },
    [input, agentType, API_BASE_URL]
  );

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  };

  const cleanQuestion = (question) => {
    return question.replace(/\s*\[\d+\]\s*$/, "");
  };

  useEffect(() => {
    if (initialMessage) {
      setMessages([
        {
          content: initialMessage,
          isUser: false,
        },
      ]);
    }
  }, [initialMessage]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);
```

La première partie de ce code contient vos imports, l'URL de base pour se connecter au backend et les fonctions.

Maintenant, ajoutons la deuxième partie du codebase :

```javascript
  useEffect(() => {
    if (
      directQuestion &&
      directQuestion.trim() !== "" &&
      !processedQuestions.includes(directQuestion)
    ) {
      const cleanedQuestion = cleanQuestion(directQuestion);
      setInput(cleanedQuestion);
      handleSendMessage(cleanedQuestion);
      setProcessedQuestions((prev) => [...prev, directQuestion]);
    }
  }, [directQuestion, processedQuestions, handleSendMessage]);

  const renderContent = (content) => {
    let formattedContent = content;

    formattedContent = formattedContent.replace(
      /#{6}\s+(.*?)(?=\n|$)/g,
      "<h6>$1</h6>"
    );
    formattedContent = formattedContent.replace(
      /#{5}\s+(.*?)(?=\n|$)/g,
      "<h5>$1</h5>"
    );
    formattedContent = formattedContent.replace(
      /#{4}\s+(.*?)(?=\n|$)/g,
      "<h4>$1</h4>"
    );
    formattedContent = formattedContent.replace(
      /#{3}\s+(.*?)(?=\n|$)/g,
      "<h3>$1</h3>"
    );
    formattedContent = formattedContent.replace(
      /#{2}\s+(.*?)(?=\n|$)/g,
      "<h2>$1</h2>"
    );
    formattedContent = formattedContent.replace(
      /#{1}\s+(.*?)(?=\n|$)/g,
      "<h1>$1</h1>"
    );

    formattedContent = formattedContent.replace(
      /\*\*(.*?)\*\*/g,
      "<strong>$1</strong>"
    );

    formattedContent = formattedContent.replace(/\*(.*?)\*/g, "<em>$1</em>");

    formattedContent = formattedContent.replace(/`(.*?)`/g, "<code>$1</code>");

    formattedContent = formattedContent.replace(
      /\[(.*?)\]\((.*?)\)/g,
      '<a href="$2" target="_blank">$1</a>'
    );

    formattedContent = formattedContent.replace(
      /^\s*\*\s+(.*?)(?=\n|$)/gm,
      "<li>$1</li>"
    );
    formattedContent = formattedContent.replace(
      /<li>(.*?)<\/li>(?:\s*<li>.*?<\/li>)*/g,
      "<ul>$&</ul>"
    );

    formattedContent = formattedContent.replace(
      /^\s*\d+\.\s+(.*?)(?=\n|$)/gm,
      "<li>$1</li>"
    );
    formattedContent = formattedContent.replace(
      /<li>(.*?)<\/li>(?:\s*<li>.*?<\/li>)*/g,
      "<ol>$&</ol>"
    );

    return { __html: formattedContent };
  };

  return (
    <div className="chat-container">
      <div className="chat-messages" id={`${agentType}-messages`}>
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${
              message.isUser ? "user-message" : "agent-message"
            }`}
          >
            {!message.isUser && (
              <div className="message-avatar">
                <div className="avatar-placeholder">
                  {agentInitials || "AI"}
                </div>
              </div>
            )}
            <div className="message-content">
              <div dangerouslySetInnerHTML={renderContent(message.content)} />
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="message agent-message">
            <div className="message-avatar">
              <div className="avatar-placeholder">{agentInitials || "AI"}</div>
            </div>
            <div className="message-content">
              <p className="loading-dots">Réflexion</p>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <div className="chat-input-container">
        <div className="chat-input-group">
          <input
            type="text"
            id={`${agentType}-input`}
            className="chat-input"
            placeholder="Tapez votre message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
          />
          <button
            id={`${agentType}-send`}
            className="chat-send-button"
            onClick={() => handleSendMessage()}
          >
            <i className="fa-solid fa-paper-plane mr-2"></i>Envoyer
          </button>
        </div>
      </div>
    </div>
  );
}

export default Chat;
```

La deuxième partie du code contient principalement le JSX pour les composants.

Bien, ensuite, faisons le fichier `Footer.jsx` en ajoutant ce code au fichier :

```javascript
function Footer() {
  return (
    <footer className="bg-dark text-white py-4">
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <h5>Portfolio</h5>
            <p>Présentation de mon travail avec l'aide d'agents IA</p>
          </div>
          <div className="col-md-6 text-md-end">
            <h5>Connectez-vous</h5>
            <div className="social-links">
              <a href="#" className="text-white me-2"></a>
              <a href="#" className="text-white me-2"></a>
              <a href="#" className="text-white me-2"></a>
            </div>
          </div>
        </div>
        <div className="row mt-3">
          <div className="col-12 text-center">
            <p className="mb-0">
              &copy; {new Date().getFullYear()} Portfolio. Tous droits réservés.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
```

Le code est assez explicite - il contient quelques détails de contact qui apparaîtront en bas de votre page dans la section du pied de page.

Maintenant, nous pouvons travailler sur le `Layout.jsx`. Je l'ai également divisé en deux parties.

Ajoutez la première partie du codebase ici :

```javascript
import { Link, useLocation } from "react-router";
import { useState } from "react";

function Layout({ children }) {
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <div className="flex flex-col min-h-screen">
      <nav className="bg-gray-800 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <Link className="text-xl font-bold" to="/">
                Portfolio
              </Link>
            </div>
            <div className="hidden md:block">
              <div className="ml-10 flex items-center space-x-4">
                <Link
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    location.pathname === "/"
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white"
                  }`}
                  to="/"
                >
                  Accueil
                </Link>
                <Link
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    location.pathname === "/projects"
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white"
                  }`}
                  to="/projects"
                >
                  Projets
                </Link>
                <Link
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    location.pathname === "/career"
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white"
                  }`}
                  to="/career"
                >
                  Carrière
                </Link>
                <Link
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    location.pathname === "/services"
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white"
                  }`}
                  to="/services"
                >
                  Services
                </Link>
                <Link
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    location.pathname === "/research"
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white"
                  }`}
                  to="/research"
                >
                  Recherche
                </Link>
                <Link
                  className={`px-3 py-2 rounded-md text-sm font-medium ${
                    location.pathname === "/contact"
                      ? "bg-gray-900 text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white"
                  }`}
                  to="/contact"
                >
                  Contact
                </Link>
              </div>
            </div>
            <div className="md:hidden flex items-center">
              <button
                onClick={() => setIsMenuOpen(!isMenuOpen)}
                className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
              >
                <span className="sr-only">Ouvrir le menu principal</span>
                {isMenuOpen ? (
                  <svg
                    className="block h-6 w-6"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                ) : (
                  <svg
                    className="block h-6 w-6"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M4 6h16M4 12h16M4 18h16"
                    />
                  </svg>
                )}
              </button>
            </div>
          </div>
        </div>
```

Cette partie du code contient de nombreux composants, comme prévu pour la mise en page.

Voici la deuxième partie du code à ajouter au fichier :

```javascript
        {/* Menu mobile, afficher/masquer en fonction de l'état du menu */}
        {isMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
              <Link
                className={`block px-3 py-2 rounded-md text-base font-medium ${
                  location.pathname === "/"
                    ? "bg-gray-900 text-white"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
                to="/"
                onClick={() => setIsMenuOpen(false)}
              >
                Accueil
              </Link>
              <Link
                className={`block px-3 py-2 rounded-md text-base font-medium ${
                  location.pathname === "/projects"
                    ? "bg-gray-900 text-white"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
                to="/projects"
                onClick={() => setIsMenuOpen(false)}
              >
                Projets
              </Link>
              <Link
                className={`block px-3 py-2 rounded-md text-base font-medium ${
                  location.pathname === "/career"
                    ? "bg-gray-900 text-white"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
                to="/career"
                onClick={() => setIsMenuOpen(false)}
              >
                Carrière
              </Link>
              <Link
                className={`block px-3 py-2 rounded-md text-base font-medium ${
                  location.pathname === "/services"
                    ? "bg-gray-900 text-white"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
                to="/services"
                onClick={() => setIsMenuOpen(false)}
              >
                Services
              </Link>
              <Link
                className={`block px-3 py-2 rounded-md text-base font-medium ${
                  location.pathname === "/research"
                    ? "bg-gray-900 text-white"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
                to="/research"
                onClick={() => setIsMenuOpen(false)}
              >
                Recherche
              </Link>
              <Link
                className={`block px-3 py-2 rounded-md text-base font-medium ${
                  location.pathname === "/contact"
                    ? "bg-gray-900 text-white"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
                to="/contact"
                onClick={() => setIsMenuOpen(false)}
              >
                Contact
              </Link>
            </div>
          </div>
        )}
      </nav>

      <main className="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>

      <footer className="bg-gray-800 text-white py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="md:flex md:justify-between">
            <div className="mb-8 md:mb-0">
              <h5 className="text-lg font-semibold mb-2">Portfolio</h5>
              <p className="text-gray-300">
                Présentation de mon travail avec l'aide d'agents IA
              </p>
            </div>
          </div>
          <div className="mt-8 border-t border-gray-700 pt-8 text-center">
            <p className="text-gray-300">
              &copy; 2025 Portfolio. Tous droits réservés.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Layout;
```

Ce code contient plus de composants, ce qui complète le composant Layout.

Nous avons presque terminé. Maintenant, pour le dernier composant, `Navbar.jsx`, avant de passer aux pages.

Voici le code dont vous avez besoin pour le fichier :

```javascript
import { Link, useLocation } from 'react-router';

function Navbar() {
  const location = useLocation();

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <Link className="navbar-brand" to="/">
          Portfolio
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <Link
                className={`nav-link ${
                  location.pathname === '/' ? 'active' : ''
                }`}
                to="/"
              >
                Accueil
              </Link>
            </li>
            <li className="nav-item">
              <Link
                className={`nav-link ${
                  location.pathname === '/projects' ? 'active' : ''
                }`}
                to="/projects"
              >
                Projets
              </Link>
            </li>
            <li className="nav-item">
              <Link
                className={`nav-link ${
                  location.pathname === '/career' ? 'active' : ''
                }`}
                to="/career"
              >
                Carrière
              </Link>
            </li>
            <li className="nav-item">
              <Link
                className={`nav-link ${
                  location.pathname === '/services' ? 'active' : ''
                }`}
                to="/services"
              >
                Services
              </Link>
            </li>
            <li className="nav-item">
              <Link
                className={`nav-link ${
                  location.pathname === '/research' ? 'active' : ''
                }`}
                to="/research"
              >
                Recherche
              </Link>
            </li>
            <li className="nav-item">
              <Link
                className={`nav-link ${
                  location.pathname === '/contact' ? 'active' : ''
                }`}
                to="/contact"
              >
                Contact
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
```

Le composant navbar contient vos liens de navigation, ce qui vous permet de naviguer entre les pages en utilisant `react-router`.

D'accord, le codebase des composants est prêt ! Il ne reste plus que les six routes de pages dans notre dossier pages.

Le premier fichier sur lequel nous allons travailler sera le fichier `Career.jsx`. Je vais diviser le codebase pour la lisibilité comme avant, alors copiez les différentes sections en commençant par la première partie ici :

```javascript
import { useState } from "react";
import Chat from "../components/Chat";

function Career() {
  const initialMessage =
    "Bonjour ! Je suis CareerAgent, le spécialiste de carrière. Je peux fournir des informations sur les compétences, l'expérience et le parcours professionnel. Que souhaitez-vous savoir ?";

  const [currentQuestion, setCurrentQuestion] = useState("");

  const askCareerQuestion = (question) => {
    setCurrentQuestion(`${question} [${Date.now()}]`);

    setTimeout(() => {
      setCurrentQuestion("");
    }, 500);
  };

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-8 mb-12">
        <div className="md:w-1/3">
          <h1 className="text-3xl font-bold mb-4">Carrière</h1>
          <p className="text-lg mb-4">
            Ici, vous pouvez trouver des informations sur mon parcours professionnel,
            mes compétences et mon expérience. N'hésitez pas à demander à CareerAgent pour plus
            de détails.
          </p>
        </div>
        <div className="md:w-2/3">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Discuter avec CareerAgent
              </h5>
              <p className="text-gray-600 mb-4">
                Notre spécialiste de carrière peut fournir des informations sur les compétences,
                l'expérience et le parcours professionnel.
              </p>
              <Chat
                agentType="career"
                initialMessage={initialMessage}
                agentInitials="CA"
                directQuestion={currentQuestion}
              />
            </div>
          </div>
        </div>
      </div>

      <div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Compétences</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-4">
                Développement Frontend
              </h5>
              <ul className="divide-y divide-gray-200">
                <li className="py-3 flex justify-between items-center">
                  React
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Expert
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Vue.js
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Angular
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Intermédiaire
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  TypeScript
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  CSS/SASS
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Expert
                  </span>
                </li>
              </ul>
              <button
                className="mt-4 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askCareerQuestion(
                    "Parlez-moi plus de vos compétences en développement frontend"
                  )
                }
              >
                Demander sur les compétences Frontend
              </button>
```

Comme avant, nous avons des imports, des états et quelques composants. Maintenant, pour la deuxième partie, qui est ici :

```javascript
 </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-4">
                Développement Backend
              </h5>
              <ul className="divide-y divide-gray-200">
                <li className="py-3 flex justify-between items-center">
                  Node.js
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Expert
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Python
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Django
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Intermédiaire
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Flask
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  SQL/NoSQL
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
              </ul>
              <button
                className="mt-4 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askCareerQuestion(
                    "Parlez-moi plus de vos compétences en développement backend"
                  )
                }
              >
                Demander sur les compétences Backend
              </button>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-4">Autres compétences</h5>
              <ul className="divide-y divide-gray-200">
                <li className="py-3 flex justify-between items-center">
                  DevOps
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Intermédiaire
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Conception UI/UX
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Gestion de projet
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Avancé
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Méthodologies Agile
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Expert
                  </span>
                </li>
                <li className="py-3 flex justify-between items-center">
                  Rédaction technique
                  <span className="px-2.5 py-0.5 bg-blue-500 text-white text-xs font-medium rounded-full">
                    Intermédiaire
                  </span>
                </li>
              </ul>
              <button
                className="mt-4 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askCareerQuestion("Quelles autres compétences avez-vous ?")
                }
              >
                Demander sur les autres compétences
              </button>
            </div>
          </div>
        </div>
      </div>
```

Il y a beaucoup plus de code de composant ici pour la page de carrière. Enfin, ajoutons la dernière partie du code pour cette page :

```javascript
<div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Expérience</h2>
        </div>
        <div className="space-y-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <div className="flex justify-between items-start mb-2">
                <h5 className="text-xl font-semibold">
                  Développeur Full-Stack Senior
                </h5>
                <span className="text-gray-500 text-sm">2020 - Présent</span>
              </div>
              <h6 className="text-gray-600 mb-3">Tech Innovations Inc.</h6>
              <p className="text-gray-700 mb-4">
                Développeur principal pour plusieurs applications web et mobiles,
                gestion d'une équipe de 5 développeurs. Implémentation de pipelines CI/CD et
                amélioration de l'efficacité du flux de travail de développement de 30%.
              </p>
              <button
                className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askCareerQuestion(
                    "Parlez-moi plus de votre expérience chez Tech Innovations Inc."
                  )
                }
              >
                Plus de détails
              </button>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <div className="flex justify-between items-start mb-2">
                <h5 className="text-xl font-semibold">Développeur Full-Stack</h5>
                <span className="text-gray-500 text-sm">2017 - 2020</span>
              </div>
              <h6 className="text-gray-600 mb-3">WebSolutions Co.</h6>
              <p className="text-gray-700 mb-4">
                Développé et maintenu plusieurs sites web et applications web clients. Spécialisé dans le développement frontend React et
                les services backend Node.js.
              </p>
              <button
                className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askCareerQuestion(
                    "Parlez-moi plus de votre expérience chez WebSolutions Co."
                  )
                }
              >
                Plus de détails
              </button>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <div className="flex justify-between items-start mb-2">
                <h5 className="text-xl font-semibold">Développeur Web Junior</h5>
                <span className="text-gray-500 text-sm">2015 - 2017</span>
              </div>
              <h6 className="text-gray-600 mb-3">Digital Creations Ltd.</h6>
              <p className="text-gray-700 mb-4">
                Travaillé sur le développement frontend pour des sites web e-commerce. Acquis
                de l'expérience avec JavaScript, CSS et les principes de conception réactive
                principes.
              </p>
              <button
                className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askCareerQuestion(
                    "Parlez-moi plus de votre expérience chez Digital Creations Ltd."
                  )
                }
              >
                Plus de détails
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-4">Éducation</h5>
            <div className="mb-6">
              <div className="flex justify-between items-start mb-1">
                <h6 className="font-medium">
                  Master of Science en Informatique
                </h6>
                <span className="text-gray-500 text-sm">2013 - 2015</span>
              </div>
              <p className="text-gray-600">Université de Technologie</p>
            </div>
            <div>
              <div className="flex justify-between items-start mb-1">
                <h6 className="font-medium">
                  Bachelor of Science en Génie Logiciel
                </h6>
                <span className="text-gray-500 text-sm">2009 - 2013</span>
              </div>
              <p className="text-gray-600">Université d'État</p>
            </div>
            <button
              className="mt-4 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              onClick={() =>
                askCareerQuestion(
                  "Parlez-moi plus de votre parcours éducatif"
                )
              }
            >
              Demander sur l'éducation
            </button>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-4">Certifications</h5>
            <ul className="divide-y divide-gray-200">
              <li className="py-3 flex justify-between items-center">
                AWS Certified Solutions Architect
                <span className="text-gray-500 text-sm">2022</span>
              </li>
              <li className="py-3 flex justify-between items-center">
                Google Cloud Professional Developer
                <span className="text-gray-500 text-sm">2021</span>
              </li>
              <li className="py-3 flex justify-between items-center">
                Microsoft Certified: Azure Developer Associate
                <span className="text-gray-500 text-sm">2020</span>
              </li>
              <li className="py-3 flex justify-between items-center">
                Certified Scrum Master
                <span className="text-gray-500 text-sm">2019</span>
              </li>
            </ul>
            <button
              className="mt-4 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              onClick={() =>
                askCareerQuestion("Parlez-moi plus de vos certifications")
              }
            >
              Demander sur les certifications
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Career;
```

Et cela complète notre page `Career.jsx` : nous avons des formulaires et plus de composants dans cette partie du code.

Ensuite, notre page `Contact.jsx`. Comme avant, je vais diviser le codebase pour la lisibilité, alors ajoutez la première partie de ce code :

```javascript
import { useState } from "react";

function Contact() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });
  const [formResponse, setFormResponse] = useState(null);

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [id]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    setFormResponse({
      type: "success",
      message:
        "Merci pour votre message ! Je vous répondrai dès que possible.",
    });

    setFormData({
      name: "",
      email: "",
      subject: "",
      message: "",
    });

    document
      .getElementById("form-response")
      .scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-8 mb-12">
        <div className="md:w-2/3">
          <h1 className="text-3xl font-bold mb-4">Contactez-moi</h1>
          <p className="text-lg mb-4">
            Vous avez une question ou souhaitez discuter d'un projet potentiel ? N'hésitez pas à
            me contacter en utilisant le formulaire ci-dessous ou via l'un de mes canaux de médias sociaux.
          </p>
        </div>
        <div className="md:w-1/3">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-4">Liens rapides</h5>
              <div className="flex flex-col gap-2">
                <a
                  href="/projects"
                  className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 text-center transition-colors"
                >
                  Voir les projets
                </a>
                <a
                  href="/services"
                  className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 text-center transition-colors"
                >
                  Services et tarifs
                </a>
                <a
                  href="/research"
                  className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 text-center transition-colors"
                >
                  Recherche et ressources
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-4">Formulaire de contact</h5>
            <form id="contact-form" onSubmit={handleSubmit}>
              <div className="mb-4">
                <label
                  htmlFor="name"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Nom
                </label>
                <input
                  type="text"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  id="name"
                  placeholder="Votre Nom"
                  required
                  value={formData.name}
                  onChange={handleChange}
                />
              </div>
```

Nous avons nos imports, fonctions et une partie des composants ici. Enfin, ajoutez la deuxième partie pour compléter cette page :

```javascript
<div className="mb-4">
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Email
                </label>
                <input
                  type="email"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  id="email"
                  placeholder="votre.email@example.com"
                  required
                  value={formData.email}
                  onChange={handleChange}
                />
              </div>
              <div className="mb-4">
                <label
                  htmlFor="subject"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Sujet
                </label>
                <input
                  type="text"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  id="subject"
                  placeholder="Sujet"
                  required
                  value={formData.subject}
                  onChange={handleChange}
                />
              </div>
              <div className="mb-4">
                <label
                  htmlFor="message"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Message
                </label>
                <textarea
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  id="message"
                  rows="5"
                  placeholder="Votre message..."
                  required
                  value={formData.message}
                  onChange={handleChange}
                ></textarea>
              </div>
              <button
                type="submit"
                className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors"
              >
                Envoyer le message
              </button>
            </form>
            <div
              id="form-response"
              className="mt-4"
              style={{ display: formResponse ? "block" : "none" }}
            >
              {formResponse && (
                <div
                  className={`p-4 ${
                    formResponse.type === "success"
                      ? "bg-green-100 text-green-700"
                      : "bg-red-100 text-red-700"
                  } rounded-md`}
                >
                  <i className="bi bi-check-circle-fill mr-2"></i>
                  {formResponse.message}
                </div>
              )}
            </div>
          </div>
        </div>
        <div className="space-y-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-4">
                Informations de contact
              </h5>
              <ul className="space-y-3">
                <li className="flex items-center">
                  <i className="bi bi-envelope mr-2"></i>
                  <a
                    href="mailto:contact@example.com"
                    className="text-blue-500 hover:underline"
                  >
                    contact@example.com
                  </a>
                </li>
                <li className="flex items-center">
                  <i className="bi bi-geo-alt mr-2"></i>
                  Royaume-Uni
                </li>
              </ul>
              <h5 className="text-xl font-semibold mt-6 mb-3">
                Connectez-vous sur les réseaux sociaux
              </h5>
              <div className="flex flex-wrap gap-2">
                <a
                  href="#"
                  className="px-3 py-1.5 border border-gray-800 text-gray-800 rounded-md hover:bg-gray-100 flex items-center transition-colors"
                >
                  <i className="bi bi-github mr-1"></i> GitHub
                </a>
                <a
                  href="#"
                  className="px-3 py-1.5 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 flex items-center transition-colors"
                >
                  <i className="bi bi-linkedin mr-1"></i> LinkedIn
                </a>
                <a
                  href="#"
                  className="px-3 py-1.5 border border-gray-800 text-gray-800 rounded-md hover:bg-gray-100 flex items-center transition-colors"
                >
                  <i className="bi bi-twitter mr-1"></i> X
                </a>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-3">Disponibilité</h5>
              <p className="text-gray-700 mb-3">
                Je suis actuellement disponible pour du travail freelance et du conseil. Mon
                temps de réponse typique est dans les 24 heures.
              </p>
              <p className="text-gray-700">
                Pour les demandes urgentes, veuillez appeler le numéro de téléphone indiqué ci-dessus.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Contact;
```

Avec cela, cette page est maintenant terminée, et nous avons le reste des composants et le formulaire.

D'accord, il ne reste plus que quatre pages : commençons par la page d'accueil. Le code n'est pas si grand, donc nous pouvons tout faire en une seule fois.

Voici le code à ajouter au fichier de la page `Home.jsx` :

```javascript
import { Link } from 'react-router';
import Chat from '../components/Chat';

function Home() {
  const initialMessage =
    "Bonjour ! Je suis WelcomeAgent, le spécialiste de l'accueil. Je peux vous aider à naviguer sur ce site web de portfolio. Êtes-vous un employeur, un client ou un fellow programmer ?";

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-8 mb-12">
        <div className="md:w-1/3">
          <h1 className="text-3xl font-bold mb-4">Bienvenue sur mon Portfolio</h1>
          <p className="text-lg mb-4">
            Ce portfolio présente mon travail et mes compétences avec l'aide
            d'agents IA spécialisés. Chaque agent est conçu pour vous aider avec
            différents aspects de mon portfolio.
          </p>
          <p className="text-gray-700">
            N'hésitez pas à interagir avec le WelcomeAgent pour obtenir des recommandations personnalisées
            sur les sections du portfolio à explorer en fonction de vos intérêts.
          </p>
        </div>
        <div className="md:w-2/3">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Discuter avec WelcomeAgent
              </h5>
              <p className="text-gray-600 mb-4">
                Notre spécialiste de l'accueil peut vous aider à naviguer sur ce site web de portfolio.
              </p>
              <Chat
                agentType="welcome"
                initialMessage={initialMessage}
                agentInitials="WA"
              />
            </div>
          </div>
        </div>
      </div>

      <div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Rencontrez les Agents</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6 flex flex-col items-center">
              <div className="agent-avatar-placeholder mb-4">PA</div>
              <h5 className="text-xl font-semibold mb-2">ProjectAgent</h5>
              <p className="text-gray-600 mb-4 text-center">
                Fournit des informations détaillées sur mes projets, les technologies
                utilisées et les défis surmontés.
              </p>
              <Link
                to="/projects"
                className="mt-auto py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              >
                Voir les Projets
              </Link>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6 flex flex-col items-center">
              <div className="agent-avatar-placeholder mb-4">CA</div>
              <h5 className="text-xl font-semibold mb-2">CareerAgent</h5>
              <p className="text-gray-600 mb-4 text-center">
                Partage des informations sur mes compétences, mon expérience et mon parcours
                professionnel.
              </p>
              <Link
                to="/career"
                className="mt-auto py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              >
                Voir la Carrière
              </Link>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6 flex flex-col items-center">
              <div className="agent-avatar-placeholder mb-4">BA</div>
              <h5 className="text-xl font-semibold mb-2">BusinessAdvisor</h5>
              <p className="text-gray-600 mb-4 text-center">
                Fournit des informations sur les services, les tarifs et le processus d'engagement client.
              </p>
              <Link
                to="/services"
                className="mt-auto py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              >
                Voir les Services
              </Link>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-2">Projets en vedette</h5>
            <p className="text-gray-600 mb-4">
              Consultez quelques-uns de mes travaux récents :
            </p>
            <ul className="divide-y divide-gray-200">
              <li className="py-3 px-2">Plateforme E-commerce</li>
              <li className="py-3 px-2">Application de gestion des tâches</li>
              <li className="py-3 px-2">Tableau de bord de visualisation de données</li>
            </ul>
            <div className="mt-4">
              <Link
                to="/projects"
                className="inline-block py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              >
                Voir tous les projets
              </Link>
            </div>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-2">Recherche et Insights</h5>
            <p className="text-gray-600 mb-4">
              Explorez mes recherches sur les technologies émergentes et les tendances de l'industrie :
            </p>
            <ul className="divide-y divide-gray-200">
              <li className="py-3 px-2">L'IA dans le développement web</li>
              <li className="py-3 px-2">Frameworks Frontend modernes</li>
              <li className="py-3 px-2">Modèles d'architecture Cloud</li>
            </ul>
            <div className="mt-4">
              <Link
                to="/research"
                className="inline-block py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              >
                Voir la Recherche
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
```

Cela contient le code pour notre page d'accueil et WelcomeAgent.

D'accord, maintenant travaillons sur la page `Projects.jsx`. Pour la lisibilité, il est plus facile de diviser le code en deux. Donc voici la première partie :

```javascript
import { useState } from "react";
import Chat from "../components/Chat";

function Projects() {
  const initialMessage =
    "Bonjour ! Je suis ProjectAgent, le spécialiste des projets. Je peux fournir des informations détaillées sur les projets, les technologies utilisées et les défis surmontés. Que souhaitez-vous savoir ?";

  const [currentQuestion, setCurrentQuestion] = useState("");

  const askProjectQuestion = (question) => {
    setCurrentQuestion(`${question} [${Date.now()}]`);

    setTimeout(() => {
      setCurrentQuestion("");
    }, 500);
  };

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-8 mb-12">
        <div className="md:w-1/3">
          <h1 className="text-3xl font-bold mb-4">Projets</h1>
          <p className="text-lg mb-4">
            Ici, vous pouvez explorer mon portfolio de projets. N'hésitez pas à
            demander à ProjectAgent plus de détails sur n'importe quel projet.
          </p>
        </div>
        <div className="md:w-2/3">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Discuter avec ProjectAgent
              </h5>
              <p className="text-gray-600 mb-4">
                Notre spécialiste des projets peut fournir des informations détaillées sur
                les projets, les technologies et les défis.
              </p>
              <Chat
                agentType="project"
                initialMessage={initialMessage}
                agentInitials="PA"
                directQuestion={currentQuestion}
              />
            </div>
          </div>
        </div>
      </div>

      <div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Projets en vedette</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="project-image-placeholder">Plateforme E-commerce</div>
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Plateforme E-commerce
              </h5>
              <p className="text-gray-600 mb-4">
                Une plateforme e-commerce complète avec gestion des produits,
                panier d'achat et traitement des paiements.
              </p>
              <div className="flex justify-between items-center">
                <div className="flex space-x-2">
                  <button
                    type="button"
                    className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                    onClick={() =>
                      askProjectQuestion(
                        "Parlez-moi plus du projet de Plateforme E-commerce"
                      )
                    }
                  >
                    Voir les détails
                  </button>
                  <button
                    type="button"
                    className="py-1.5 px-3 text-sm border border-gray-500 text-gray-500 rounded-md hover:bg-gray-50 transition-colors"
                    onClick={() =>
                      askProjectQuestion(
                        "Quelles technologies ont été utilisées dans le projet de Plateforme E-commerce ?"
                      )
                    }
                  >
                    Technologies
                  </button>
                </div>
                <span className="text-sm text-gray-500">2023</span>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="project-image-placeholder">Application de gestion des tâches</div>
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Application de gestion des tâches
              </h5>
              <p className="text-gray-600 mb-4">
                Une application de gestion des tâches collaborative avec des mises à jour en temps réel
                et des fonctionnalités de collaboration d'équipe.
              </p>
              <div className="flex justify-between items-center">
                <div className="flex space-x-2">
                  <button
                    type="button"
                    className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                    onClick={() =>
                      askProjectQuestion(
                        "Parlez-moi plus du projet d'Application de gestion des tâches"
                      )
                    }
                  >
                    Voir les détails
                  </button>
```

Comme mentionné précédemment, nous avons nos imports, fonctions et quelques composants. Complétez la page avec la deuxième partie du code ici :

```javascript
 <button
                    type="button"
                    className="py-1.5 px-3 text-sm border border-gray-500 text-gray-500 rounded-md hover:bg-gray-50 transition-colors"
                    onClick={() =>
                      askProjectQuestion(
                        "Quelles technologies ont été utilisées dans le projet d'Application de gestion des tâches ?"
                      )
                    }
                  >
                    Technologies
                  </button>
                </div>
                <span className="text-sm text-gray-500">2022</span>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="project-image-placeholder">Visualisation de données</div>
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Tableau de bord de visualisation de données
              </h5>
              <p className="text-gray-600 mb-4">
                Un tableau de bord interactif pour visualiser des ensembles de données complexes avec
                des graphiques personnalisables et des filtres.
              </p>
              <div className="flex justify-between items-center">
                <div className="flex space-x-2">
                  <button
                    type="button"
                    className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                    onClick={() =>
                      askProjectQuestion(
                        "Parlez-moi plus du projet de Tableau de bord de visualisation de données"
                      )
                    }
                  >
                    Voir les détails
                  </button>
                  <button
                    type="button"
                    className="py-1.5 px-3 text-sm border border-gray-500 text-gray-500 rounded-md hover:bg-gray-50 transition-colors"
                    onClick={() =>
                      askProjectQuestion(
                        "Quelles technologies ont été utilisées dans le projet de Tableau de bord de visualisation de données ?"
                      )
                    }
                  >
                    Technologies
                  </button>
                </div>
                <span className="text-sm text-gray-500">2021</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-2">
              Présentation des compétences techniques
            </h5>
            <p className="text-gray-600 mb-4">
              Ces projets démontrent une maîtrise des technologies suivantes :
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <h6 className="font-semibold mb-2">Frontend</h6>
                <ul className="list-disc pl-5 space-y-1">
                  <li>React</li>
                  <li>Vue.js</li>
                  <li>Angular</li>
                  <li>TypeScript</li>
                  <li>CSS/SASS</li>
                </ul>
              </div>
              <div>
                <h6 className="font-semibold mb-2">Backend</h6>
                <ul className="list-disc pl-5 space-y-1">
                  <li>Node.js</li>
                  <li>Python</li>
                  <li>Django</li>
                  <li>Flask</li>
                  <li>MongoDB</li>
                </ul>
              </div>
            </div>
            <button
              className="mt-4 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              onClick={() =>
                askProjectQuestion(
                  "Quelles autres technologies maîtrisez-vous ?"
                )
              }
            >
              Demander sur les autres compétences
            </button>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-2">Demande de projet</h5>
            <p className="text-gray-600 mb-4">
              Intéressé par un type de projet ou une technologie spécifique ? Demandez
              à ProjectAgent plus d'informations.
            </p>
            <div className="flex flex-col space-y-3">
              <button
                className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askProjectQuestion(
                    "Avez-vous des projets impliquant le machine learning ou l'IA ?"
                  )
                }
              >
                Demander sur les projets IA
              </button>
              <button
                className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askProjectQuestion("Quels sont vos projets les plus difficiles ?")
                }
              >
                Demander sur les projets difficiles
              </button>
              <button
                className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askProjectQuestion(
                    "Pouvez-vous me montrer des exemples de votre travail UI/UX ?"
                  )
                }
              >
                Demander sur le travail UI/UX
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Projects;
```

Avec les composants restants ajoutés, cette page est maintenant complète.

Il est temps de faire la page `Research.jsx`, en commençant par la première moitié du codebase :

```javascript
import { useState } from "react";
import Chat from "../components/Chat";

function Research() {
  const initialMessage =
    "Bonjour ! Je suis ResearchAgent, le spécialiste de la recherche. Je peux fournir des informations sur les technologies, les tendances et les actualités de l'industrie. Que souhaitez-vous savoir ?";
  const [searchQuery, setSearchQuery] = useState("");
  const [tech1, setTech1] = useState("");
  const [tech2, setTech2] = useState("");

  const [currentQuestion, setCurrentQuestion] = useState("");

  const askResearchQuestion = (question) => {
    setCurrentQuestion(`${question} [${Date.now()}]`);

    setTimeout(() => {
      setCurrentQuestion("");
    }, 500);
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      askResearchQuestion(`Rechercher des informations sur : ${searchQuery}`);
      setSearchQuery("");
    }
  };

  const handleCompare = (e) => {
    e.preventDefault();
    if (tech1.trim() && tech2.trim()) {
      askResearchQuestion(`Comparer ${tech1} vs ${tech2}`);
      setTech1("");
      setTech2("");
    }
  };

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-8 mb-12">
        <div className="md:w-1/3">
          <h1 className="text-3xl font-bold mb-4">Recherche & Insights</h1>
          <p className="text-lg mb-4">
            Ici, vous pouvez explorer des recherches sur les technologies, les tendances et les actualités
            de l'industrie. N'hésitez pas à demander à ResearchAgent plus d'informations.
          </p>
        </div>
        <div className="md:w-2/3">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Discuter avec ResearchAgent
              </h5>
              <p className="text-gray-600 mb-4">
                Notre spécialiste de la recherche peut fournir des informations sur
                les technologies, les tendances et les actualités de l'industrie.
              </p>
              <Chat
                agentType="research"
                initialMessage={initialMessage}
                agentInitials="RA"
                directQuestion={currentQuestion}
              />
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-3">
              Rechercher des informations
            </h5>
            <p className="text-gray-600 mb-4">
              Entrez un sujet pour rechercher les dernières informations et insights.
            </p>
            <form onSubmit={handleSearch}>
              <div className="flex mb-4">
                <input
                  type="text"
                  className="flex-grow px-3 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="ex. WebAssembly, Edge Computing, etc."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
                <button
                  className="px-4 py-2 bg-blue-500 text-white rounded-r-md hover:bg-blue-600 transition-colors"
                  type="submit"
                >
                  Rechercher
                </button>
              </div>
            </form>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-3">Comparer les technologies</h5>
            <p className="text-gray-600 mb-4">
              Comparez deux technologies pour comprendre leurs avantages, inconvénients et cas
              d'utilisation.
            </p>
            <form onSubmit={handleCompare}>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                <div>
                  <input
                    type="text"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Première technologie"
                    value={tech1}
                    onChange={(e) => setTech1(e.target.value)}
                  />
                </div>
```

Nous avons nos imports, état, fonctions et quelques composants pour le ResearchAgent, donc c'est assez simple. Maintenant, nous pouvons compléter la page en la terminant avec le reste du code :

```javascript
<div>
                  <input
                    type="text"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Deuxième technologie"
                    value={tech2}
                    onChange={(e) => setTech2(e.target.value)}
                  />
                </div>
              </div>
              <button
                className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors"
                type="submit"
              >
                Comparer
              </button>
            </form>
          </div>
        </div>
      </div>

      <div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Tendances technologiques actuelles</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6 flex flex-col h-full">
              <h5 className="text-xl font-semibold mb-3">
                L'IA dans le développement web
              </h5>
              <p className="text-gray-600 mb-4 flex-grow">
                Explorer comment l'intelligence artificielle transforme les pratiques et les outils
                de développement web.
              </p>
              <button
                className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors self-start"
                onClick={() =>
                  askResearchQuestion("Parlez-moi de l'IA dans le développement web")
                }
              >
                En savoir plus
              </button>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6 flex flex-col h-full">
              <h5 className="text-xl font-semibold mb-3">
                Frameworks Frontend modernes
              </h5>
              <p className="text-gray-600 mb-4 flex-grow">
                Analyse des frameworks frontend actuels, leurs forces et
                leurs cas d'utilisation idéaux.
              </p>
              <button
                className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors self-start"
                onClick={() =>
                  askResearchQuestion("Comparer les frameworks frontend modernes")
                }
              >
                En savoir plus
              </button>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6 flex flex-col h-full">
              <h5 className="text-xl font-semibold mb-3">
                Modèles d'architecture Cloud
              </h5>
              <p className="text-gray-600 mb-4 flex-grow">
                Bonnes pratiques et modèles pour concevoir des applications basées sur le cloud
                scalables.
              </p>
              <button
                className="py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors self-start"
                onClick={() =>
                  askResearchQuestion("Expliquer les modèles d'architecture Cloud")
                }
              >
                En savoir plus
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="mb-6">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-3">Tendances de l'industrie</h5>
            <p className="text-gray-600 mb-4">
              Restez à jour sur les dernières tendances en matière de développement logiciel et
              de technologie.
            </p>
            <button
              className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
              onClick={() =>
                askResearchQuestion(
                  "Quelles sont les tendances actuelles en matière de développement logiciel et de technologie ?"
                )
              }
            >
              Obtenir les tendances de l'industrie
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Research;
```

La deuxième moitié du code contient les composants restants, ce qui complète la page.

Maintenant, pour la dernière page qui est pour `Services.jsx`. Le codebase est assez grand, donc nous allons le décomposer.

Et voici la première partie du codebase à ajouter :

```javascript
import { useState } from "react";
import axios from "axios";
import Chat from "../components/Chat";

function Services() {
  const initialMessage =
    "Bonjour ! Je suis BusinessAdvisor, le spécialiste client. Je peux fournir des informations sur les services, les tarifs et les détails des projets. Que souhaitez-vous savoir ?";
  const [projectDescription, setProjectDescription] = useState("");

  const [currentQuestion, setCurrentQuestion] = useState("");

  const askClientQuestion = (question) => {
    setCurrentQuestion(`${question} [${Date.now()}]`);

    setTimeout(() => {
      setCurrentQuestion("");
    }, 500);
  };

  const generateProposal = async () => {
    if (!projectDescription.trim()) return;

    try {
      const response = await axios.post("/api/client/proposal", {
        project_description: projectDescription,
      });

      if (response.data && response.data.proposal) {
        askClientQuestion(
          `Pouvez-vous fournir une proposition pour ce projet : ${projectDescription}`
        );
      }
    } catch (error) {
      console.error("Erreur lors de la génération de la proposition :", error);
    }
  };

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-8 mb-12">
        <div className="md:w-1/3">
          <h1 className="text-3xl font-bold mb-4">Services</h1>
          <p className="text-lg mb-4">
            Ici, vous pouvez trouver des informations sur les services que je propose. N'hésitez
            pas à demander à BusinessAdvisor plus de détails sur les tarifs, les délais,
            et les spécificités des projets.
          </p>
        </div>
        <div className="md:w-2/3">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Discuter avec BusinessAdvisor
              </h5>
              <p className="text-gray-600 mb-4">
                Notre spécialiste client peut fournir des informations sur les services,
                les tarifs et les détails des projets.
              </p>
              <Chat
                agentType="client"
                initialMessage={initialMessage}
                agentInitials="BA"
                directQuestion={currentQuestion}
              />
            </div>
          </div>
        </div>
      </div>

      <div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Services proposés</h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">Développement Web</h5>
              <p className="text-gray-600 mb-4">
                Développement d'applications web personnalisées utilisant des frameworks modernes et
                les meilleures pratiques.
              </p>
              <h6 className="font-semibold mb-2">Technologies</h6>
              <ul className="list-disc pl-5 space-y-1 mb-4">
                <li>React</li>
                <li>Vue.js</li>
                <li>Node.js</li>
                <li>Django</li>
                <li>Flask</li>
              </ul>
              <h6 className="font-semibold mb-2">Détails</h6>
              <ul className="space-y-2 mb-4">
                <li>
                  <strong>Modèle de tarification :</strong> Basé sur le projet ou à l'heure
                </li>
                <li>
                  <strong>Fourchette de prix :</strong> 5 000 $ - 50 000 $ selon la
                  complexité
                </li>
                <li>
                  <strong>Calendrier :</strong> 4-12 semaines selon l'ampleur
                </li>
              </ul>
              <button
                className="mt-2 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askClientQuestion(
                    "Parlez-moi plus de vos services de développement web"
                  )
                }
              >
                Demander sur le développement web
              </button>
            </div>
          </div>
```

Nous avons plus d'instructions d'importation, d'état et de composants pour notre agent IA BusinessAdvisor. Passons à la partie suivante de ce codebase ici :

```javascript
 <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Développement d'applications mobiles
              </h5>
              <p className="text-gray-600 mb-4">
                Développement d'applications mobiles natives et multiplateformes pour iOS
                et Android.
              </p>
              <h6 className="font-semibold mb-2">Technologies</h6>
              <ul className="list-disc pl-5 space-y-1 mb-4">
                <li>React Native</li>
                <li>Flutter</li>
                <li>Swift</li>
                <li>Kotlin</li>
              </ul>
              <h6 className="font-semibold mb-2">Détails</h6>
              <ul className="space-y-2 mb-4">
                <li>
                  <strong>Modèle de tarification :</strong> Basé sur le projet
                </li>
                <li>
                  <strong>Fourchette de prix :</strong> 8 000 $ - 60 000 $ selon la
                  complexité
                </li>
                <li>
                  <strong>Calendrier :</strong> 6-16 semaines selon l'ampleur
                </li>
              </ul>
              <button
                className="mt-2 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askClientQuestion(
                    "Parlez-moi plus de vos services de développement d'applications mobiles"
                  )
                }
              >
                Demander sur le développement mobile
              </button>
            </div>
          </div>
          <div className="bg-white rounded-lg shadow-md overflow-hidden h-full">
            <div className="p-6">
              <h5 className="text-xl font-semibold mb-2">
                Conseil technique
              </h5>
              <p className="text-gray-600 mb-4">
                Conseils d'expert sur l'architecture, la pile technologique et les pratiques de développement.
              </p>
              <h6 className="font-semibold mb-2">Domaines d'expertise</h6>
              <ul className="list-disc pl-5 space-y-1 mb-4">
                <li>Architecture système</li>
                <li>Conception de base de données</li>
                <li>Optimisation des performances</li>
                <li>Meilleures pratiques de sécurité</li>
                <li>Implémentation DevOps</li>
              </ul>
              <h6 className="font-semibold mb-2">Détails</h6>
              <ul className="space-y-2 mb-4">
                <li>
                  <strong>Modèle de tarification :</strong> À l'heure
                </li>
                <li>
                  <strong>Fourchette de prix :</strong> 150 $ - 250 $ par heure
                </li>
                <li>
                  <strong>Calendrier :</strong> En cours ou selon les besoins
                </li>
              </ul>
              <button
                className="mt-2 py-1.5 px-3 text-sm border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                onClick={() =>
                  askClientQuestion(
                    "Parlez-moi plus de vos services de conseil technique"
                  )
                }
              >
                Demander sur le conseil
              </button>
            </div>
          </div>
        </div>
      </div>
```

Nous pouvons nous attendre à voir beaucoup de code de composant ici pour la page, alors terminons-la avec la partie finale maintenant :

```javascript
 <div className="mb-12">
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">Processus d'engagement client</h2>
        </div>
        <div className="w-full">
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6">
              <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div className="mb-6 md:mb-0">
                  <div className="flex flex-col items-center">
                    <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center text-xl font-bold mb-4">
                      1
                    </div>
                    <h5 className="text-lg font-semibold mt-2 mb-1">
                      Consultation initiale
                    </h5>
                    <p className="text-gray-600 text-center">
                      Comprendre vos exigences et objectifs du projet
                    </p>
                  </div>
                </div>
                <div className="mb-6 md:mb-0">
                  <div className="flex flex-col items-center">
                    <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center text-xl font-bold mb-4">
                      2
                    </div>
                    <h5 className="text-lg font-semibold mt-2 mb-1">
                      Proposition
                    </h5>
                    <p className="text-gray-600 text-center">
                      Préparation détaillée du devis et du plan de projet
                    </p>
                  </div>
                </div>
                <div className="mb-6 md:mb-0">
                  <div className="flex flex-col items-center">
                    <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center text-xl font-bold mb-4">
                      3
                    </div>
                    <h5 className="text-lg font-semibold mt-2 mb-1">
                      Développement
                    </h5>
                    <p className="text-gray-600 text-center">
                      Sprints réguliers avec retour du client
                    </p>
                  </div>
                </div>
                <div className="mb-6 md:mb-0">
                  <div className="flex flex-col items-center">
                    <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center text-xl font-bold mb-4">
                      4
                    </div>
                    <h5 className="text-lg font-semibold mt-2 mb-1">
                      Livraison
                    </h5>
                    <p className="text-gray-600 text-center">
                      Tests, déploiement et support continu
                    </p>
                  </div>
                </div>
              </div>
              <div className="flex justify-center mt-8">
                <button
                  className="py-2 px-4 border border-blue-500 text-blue-500 rounded-md hover:bg-blue-50 transition-colors"
                  onClick={() =>
                    askClientQuestion(
                      "Expliquez votre processus d'engagement client en détail"
                    )
                  }
                >
                  En savoir plus sur le processus
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="w-full">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="p-6">
            <h5 className="text-xl font-semibold mb-2">Demander une proposition</h5>
            <p className="text-gray-600 mb-4">
              Intéressé à travailler ensemble ? Décrivez votre projet ci-dessous et
              BusinessAdvisor générera une proposition personnalisée pour vous.
            </p>
            <div className="mb-4">
              <label
                htmlFor="project-description"
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Décrivez votre projet :
              </label>
              <textarea
                id="project-description"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                rows="5"
                placeholder="Entrez la description du projet..."
                value={projectDescription}
                onChange={(e) => setProjectDescription(e.target.value)}
              ></textarea>
            </div>
            <button
              className="py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors"
              onClick={generateProposal}
            >
              Générer une proposition
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Services;
```

Notre page de services est complète, et l'application aussi !

Assurez-vous que le serveur backend Python est en cours d'exécution, puis démarrez votre frontend React avec le script d'exécution habituel de Vite ici à l'intérieur du dossier `frontend` :

```shell
npm run dev
```

Vous devriez voir le site web en cours d'exécution sur [http://localhost:5173/](http://localhost:5173/) avec des agents IA fonctionnels sur toutes les pages (à l'exception de la page de contact, qui n'en a pas). N'oubliez pas que chaque fois que vous utilisez l'un des agents IA pour poser une question, cela utilisera 1 appel API sur Groq Cloud, alors consultez les [Limites de taux](https://console.groq.com/docs/rate-limits) pour les différents LLMs.

## Conclusion

Construire une équipe d'agents IA pour votre site web en utilisant des plateformes comme Agno et Groq est un moyen puissant de montrer comment les flux de travail automatisés innovants peuvent améliorer l'expérience utilisateur sans dépenser beaucoup d'argent.

La combinaison d'Agno et de Groq offre une voie gratuite pour explorer les agents IA, ce qui peut être très bénéfique. Avec l'orchestration d'agents sans code d'Agno et l'inférence ultra-rapide de Groq, vous pouvez déployer des fonctionnalités alimentées par l'IA qui engagent les visiteurs et facilitent les interactions.

Ainsi, qu'il s'agisse d'un chatbot, d'un générateur de contenu ou d'un assistant intelligent, ces outils rendent plus facile que jamais l'intégration de l'IA dans votre marque. Avec les avancées que la technologie IA réalise, être capable d'essayer ces solutions gratuites vous maintiendra certainement en avance et fera briller votre site web alors que vous continuez à moderniser votre marque.

### Restez à jour avec la tech, la programmation, la productivité et l'IA

Si vous avez apprécié ces articles, connectez-vous et suivez-moi sur les [réseaux sociaux](https://limey.io/andrewbaisden), où je partage du contenu lié à tous ces sujets 📡

![Bannière des réseaux sociaux d'Andrew Baisden, développeur logiciel et rédacteur technique](https://cdn.hashnode.com/res/hashnode/image/upload/v1741977770238/3766c236-f276-4939-996e-61ab1306cc26.png align="center")