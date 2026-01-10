---
title: Comment exécuter des LLMs open source sur votre propre ordinateur en utilisant
  Ollama
subtitle: ''
author: Krishna Sarathi Ghosh
co_authors: []
series: null
date: '2024-12-20T20:51:38.891Z'
originalURL: https://freecodecamp.org/news/how-to-run-open-source-llms-on-your-own-computer-using-ollama
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734681473969/20c1a1cd-898a-4f48-a26f-d2d3d2917efc.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: AI
  slug: ai
- name: ollama
  slug: ollama
- name: ai agents
  slug: ai-agents
seo_title: Comment exécuter des LLMs open source sur votre propre ordinateur en utilisant
  Ollama
seo_desc: Host open-source LLMs privately with Ollama for data privacy and customization.
  Steps for secure, local AI deployment
---

Les outils d'IA sont devenus monnaie courante de nos jours, et vous pouvez les utiliser quotidiennement. L'une des principales façons de sécuriser vos données confidentielles, à la fois personnelles et professionnelles, est d'exécuter votre propre IA sur votre propre infrastructure.

Ce guide expliquera comment héberger un LLM open source sur votre ordinateur. Cela aide à garantir que vous ne compromettez pas vos données avec des entreprises tierces via des solutions d'IA basées sur le cloud.

## Prérequis

* **Un peu de connaissances en IA**. Je couvrirai les principaux concepts liés à ce que nous allons faire dans l'article, mais quelques connaissances de base sur les LLMs vous aideront à mieux comprendre cela. Pas de soucis si vous ne savez rien cependant, vous devriez toujours trouver cela intéressant.

* **Un ordinateur décent** : Un système avec au moins 16 Go de RAM, un CPU multi-cœur et de préférence un GPU pour des performances optimales. (Si vous avez des spécifications inférieures, cela peut être assez lent)

* **Connexion Internet** : Requise pour télécharger et installer les modèles.

* **Temps et patience**

## Qu'est-ce qu'un LLM ?

Les LLMs, ou Large Language Models, sont des systèmes d'IA avancés qui sont formés pour comprendre et générer un langage naturel lisible par l'homme. Ils utilisent des algorithmes pour traiter et comprendre le langage naturel et sont formés sur de grandes quantités d'informations pour comprendre les motifs et les relations dans les données.

Des entreprises comme OpenAI, Anthropic et Meta ont créé des LLMs que vous pouvez utiliser pour effectuer des tâches telles que la génération de contenu, l'analyse de code, la planification de voyages, et ainsi de suite.

## IA basée sur le cloud vs. IA auto-hébergée

Avant de décider d'héberger un modèle d'IA localement, il est important de comprendre comment cette approche diffère des solutions basées sur le cloud. Les deux options ont leurs forces et sont adaptées à différents cas d'utilisation.

### **Solutions d'IA basées sur le cloud**

Ces services sont hébergés et maintenus par des fournisseurs comme OpenAI, Google ou AWS. Les exemples incluent les modèles GPT d'OpenAI, Google Bard et AWS SageMaker. Vous accédez à ces modèles via Internet en utilisant des APIs ou leurs endpoints.

**Caractéristiques clés** :

* **Facile à utiliser** : La configuration est minimale, vous intégrez simplement avec une API ou accédez via les pages web.

* **Scalabilité** : Gère mieux les grandes charges de travail et les requêtes simultanées car elles sont gérées par des entreprises.

* **Modèles de pointe** : Souvent les derniers et les plus puissants modèles sont disponibles dans le cloud.

* **Dépendance aux données** : Vos données sont envoyées dans le cloud pour traitement, ce qui peut soulever des préoccupations en matière de confidentialité.

* **Coûts continus** : Bien que certains modèles soient gratuits, d'autres sont généralement facturés par requête ou utilisation sur certains modèles comme les plus puissants ou les plus récents, ce qui en fait une dépense opérationnelle.

### **IA auto-hébergée**

Avec cette approche, vous exécutez le modèle sur votre propre matériel. Des LLMs open-source comme Llama 2, GPT-J ou Mistral peuvent être téléchargés et hébergés à l'aide d'outils comme Ollama.

**Caractéristiques clés** :

* **Confidentialité des données** : Vos données restent sur votre infrastructure, vous donnant un contrôle total sur elles.

* **Plus économique à long terme** : Nécessite un investissement initial dans le matériel, mais évite les frais récurrents d'API.

* **Personnalisation** : Vous pouvez ajuster et adapter les modèles à des besoins spécifiques.

* **Exigences techniques** : Nécessite un matériel puissant, un effort de configuration et des connaissances techniques.

* **Scalabilité limitée** : Convient mieux pour un usage personnel ou à petite échelle.

### **Laquelle devriez-vous choisir ?**

Si vous avez besoin d'un accès rapide et scalable à des modèles avancés et que cela ne vous dérange pas de partager des données avec un tiers, les solutions d'IA basées sur le cloud sont probablement la meilleure option. En revanche, si la sécurité des données, la personnalisation ou les économies de coûts sont des priorités absolues, l'hébergement d'un LLM localement pourrait être la voie à suivre.

## Comment pouvez-vous exécuter des LLMs localement sur votre machine ?

Il existe diverses solutions qui vous permettent d'exécuter certains LLMs open source sur votre propre infrastructure.

Bien que la plupart des solutions auto-hébergées se concentrent sur les **LLMs open-source**—comme Llama 2, GPT-J ou Mistral—il existe des cas où des modèles propriétaires ou sous licence peuvent également être exécutés localement, selon leurs conditions d'utilisation.

* **Modèles open-source** : Ceux-ci sont librement disponibles et peuvent être téléchargés, modifiés et hébergés sans restrictions de licence. Les exemples incluent Llama 2 (Meta), GPT-J et Mistral.

* **Modèles propriétaires avec options locales** : Certaines entreprises peuvent offrir des versions téléchargeables de leurs modèles pour une utilisation hors ligne, mais cela nécessite souvent une licence spécifique ou du matériel. Par exemple, le framework NeMo de NVIDIA fournit des outils pour héberger leurs modèles sur votre infrastructure, et certaines petites entreprises peuvent offrir des versions téléchargeables de leurs LLMs propriétaires pour les clients entreprises.

Rappelez-vous simplement que si vous exécutez votre propre LLM, vous aurez besoin d'un ordinateur puissant (avec un bon GPU et CPU). Si votre ordinateur n'est pas très puissant, vous pouvez essayer d'exécuter des modèles plus petits et plus légers, bien que cela puisse encore être lent.

**Voici un exemple de configuration système appropriée que j'utilise pour ce guide** :

* CPU : Intel Core i7 13700HX

* RAM : 16 Go DDR5

* STOCKAGE : 512 Go SSD

* GPU : Nvidia RTX 3050 (6 Go)

Dans ce guide, vous utiliserez Ollama pour télécharger et exécuter des modèles d'IA sur votre PC.

### Qu'est-ce qu'Ollama ?

[Ollama](http://ollama.com) est un outil conçu pour simplifier le processus d'exécution de grands modèles de langage open-source (LLMs) directement sur votre ordinateur. Il agit comme un gestionnaire de modèles local et un environnement d'exécution, gérant tout, du téléchargement des fichiers de modèle à la configuration d'un environnement local où vous pouvez interagir avec eux.

**Voici ce qu'Ollama vous aide à faire** :

* **Gérer vos modèles** : Ollama fournit un moyen simple de parcourir, télécharger et gérer différents modèles open-source. Vous pouvez voir une liste des modèles pris en charge sur leur site officiel.

* **Déployer facilement** : Avec seulement quelques commandes, vous pouvez configurer un environnement entièrement fonctionnel pour exécuter et interagir avec les LLMs.

* **Héberger localement** : Les modèles s'exécutent entièrement sur votre infrastructure, garantissant que vos données restent privées et sécurisées.

* **Intégrer différents modèles** : Il inclut le support pour intégrer des modèles dans vos propres projets en utilisant des langages de programmation comme Python ou JavaScript.

En utilisant Ollama, vous n'avez pas besoin de plonger profondément dans les complexités de la configuration des frameworks de machine learning ou de la gestion des dépendances. Il simplifie le processus, surtout pour ceux qui veulent expérimenter avec les LLMs sans avoir besoin d'un background technique approfondi.

Vous pouvez installer Ollama très facilement via le bouton **Télécharger** sur leur [site web](http://ollama.com).

![site officiel d'ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1734604517326/06605e51-4425-4dbe-b8d9-403270eec95b.png align="center")

### Comment utiliser Ollama pour installer/exécuter votre modèle

Après avoir installé Ollama, suivez ces étapes pour installer et utiliser votre modèle :

1. Ouvrez votre navigateur et allez sur [localhost:11434](http://localhost:11434) pour vous assurer qu'Ollama est en cours d'exécution.

2. Maintenant, ouvrez l'invite de commande et écrivez `ollama run <model_name>`. Ajoutez ici le nom du modèle souhaité qui est pris en charge par Ollama, par exemple Llama2 (par Meta) ou Mistral.

   ![image d'une fenêtre d'invite de commande où le modèle llama2 est en cours d'installation](https://cdn.hashnode.com/res/hashnode/image/upload/v1734604496300/beef69ca-f6e0-44b8-a3a7-ed488e78e776.png align="center")

3. Attendez que le processus d'installation se termine.

4. Dans l'invite qui dit `>>> Send a message (/? for help)`, écrivez un message à l'IA et appuyez sur Entrée.

Vous avez installé votre modèle avec succès et vous pouvez maintenant discuter avec lui !

## Construire un chatbot avec votre modèle nouvellement installé

Avec des modèles open source fonctionnant sur votre propre infrastructure, vous avez beaucoup de liberté pour modifier et utiliser le modèle comme vous le souhaitez. Vous pouvez même l'utiliser pour construire des chatbots locaux ou des applications pour un usage personnel en utilisant le module `ollama` en Python, JavaScript et d'autres langages.

Maintenant, voyons comment vous pouvez construire un chatbot avec lui en Python en seulement quelques minutes.

### Étape 1 : Installer Python

Si vous n'avez pas déjà Python installé, téléchargez-le et installez-le depuis le [site officiel de Python](https://www.python.org/). Pour une meilleure compatibilité, évitez d'utiliser la version la plus récente de Python, car certains modules peuvent ne pas encore la supporter pleinement. Au lieu de cela, sélectionnez la dernière version stable (généralement celle avant la dernière sortie) pour assurer le bon fonctionnement de tous les modules requis.

Lors de la configuration de Python, assurez-vous de donner à l'installeur les privilèges administrateur et cochez la case **Ajouter à PATH**.

### Étape 2 : Installer Ollama

Maintenant, vous devez ouvrir une nouvelle fenêtre de terminal dans le répertoire où le fichier est enregistré. Vous pouvez ouvrir le répertoire dans l'Explorateur de fichiers et **cliquer avec le bouton droit**, puis cliquer sur **Ouvrir dans le Terminal** (**Ouvrir avec l'invite de commande** ou **PowerShell** si vous utilisez Windows 10 ou une version précédente).

Tapez `pip install ollama` et appuyez sur Entrée. Cela installera le module `ollama` pour Python, afin que vous puissiez accéder à vos modèles et aux fonctions fournies par l'outil depuis Python. Attendez que le processus se termine.

### Étape 3 : Ajouter le code Python

Allez-y et créez un fichier Python avec l'extension `.py` quelque part dans votre système de fichiers, où vous pouvez y accéder facilement. Ouvrez le fichier avec votre éditeur de code préféré, et si vous n'en avez aucun installé, vous pouvez utiliser la version en ligne de [VS Code](https://vscode.dev/) depuis votre navigateur.

Maintenant, ajoutez ce code dans votre fichier Python :

```python
from ollama import chat

def stream_response(user_input):
    """Diffuse la réponse du modèle de chat et l'affiche dans le CLI."""
    try:
        print("\nAI: ", end="", flush=True)
        stream = chat(model='llama2', messages=[{'role': 'user', 'content': user_input}], stream=True)
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
        print() 
    except Exception as e:
        print(f"\nErreur: {str(e)}")

def main():
    print("Bienvenue dans votre chatbot IA CLI ! Tapez 'exit' pour quitter.\n")
    while True:
        user_input = input("Vous: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Au revoir !")
            break
        stream_response(user_input)

if __name__ == "__main__":
    main()
```

Si vous ne comprenez pas le code Python, voici ce qu'il fait essentiellement :

* Tout d'abord, le module chat est importé de la bibliothèque `ollama`, qui contient du code pré-écrit pour s'intégrer avec l'application Ollama sur votre ordinateur.

* Ensuite, une fonction `stream_response` est déclarée, qui transmet votre prompt au modèle spécifié et diffuse (fournit la réponse morceau par morceau au fur et à mesure qu'elle est générée) la réponse en direct.

* Ensuite, dans la fonction principale, un texte de bienvenue est imprimé dans le terminal. Il obtient l'entrée de l'utilisateur qui est passée à la fonction `stream_response`, le tout enveloppé dans une boucle `while True` ou infinie. Cela nous permet de poser des questions à l'IA sans que le processus d'exécution ne se rompe. Nous spécifions également que si l'entrée de l'utilisateur contient soit **exit** soit **quit**, le code cessera de s'exécuter.

### Étape 4 : Écrire des prompts

Maintenant, retournez à la fenêtre du terminal et tapez `python filename.py`, en remplaçant `filename` par le nom de fichier réel que vous avez défini, et appuyez sur Entrée.

Vous devriez voir une invite disant `Vous:`, comme nous l'avons mentionné dans le code. Écrivez votre prompt et appuyez sur Entrée. Vous devriez voir la réponse de l'IA être diffusée. Pour arrêter l'exécution, entrez le prompt `exit`, ou fermez la fenêtre du Terminal.

Vous pouvez même installer le module pour JavaScript ou tout autre langage pris en charge et intégrer l'IA dans votre code. N'hésitez pas à consulter la [Documentation officielle d'Ollama](https://github.com/ollama/ollama/blob/main/docs/README.md) et comprendre ce que vous pouvez coder avec les modèles d'IA.

## Comment personnaliser vos modèles avec le fine-tuning

### Qu'est-ce que le Fine-Tuning ?

Le fine-tuning est le processus de prise d'un modèle de langage pré-entraîné et de l'entraîner davantage sur un ensemble de données spécifique et personnalisé pour un objectif spécifique. Bien que les LLMs soient entraînés sur des ensembles de données massifs, ils peuvent ne pas toujours parfaitement correspondre à vos besoins. Le fine-tuning vous permet de rendre le modèle mieux adapté à votre cas d'utilisation particulier.

### Comment Fine-Tuner un Modèle

Le fine-tuning nécessite :

* **Un modèle pré-entraîné** : Je suggère de commencer avec un LLM open-source puissant comme LLaMA, Mistral ou Falcon.

* **Un ensemble de données de qualité** : Un **ensemble de données** est une collection de données utilisée pour l'entraînement, les tests ou l'évaluation de modèles de machine learning, y compris les LLMs. La qualité et la pertinence de l'ensemble de données influencent directement la performance du modèle sur une tâche donnée. Utilisez un ensemble de données pertinent pour votre domaine ou votre tâche. Par exemple, si vous voulez que l'IA écrive des articles de blog, entraînez-la sur du contenu de blog de haute qualité.

* **Des ressources suffisantes** : Le fine-tuning implique de ré-entraîner le modèle, ce qui nécessite des ressources computationnelles significatives (de préférence une machine avec un GPU puissant).

Pour fine-tuner votre modèle, il existe plusieurs outils que vous pouvez utiliser. [Unsloth](https://unsloth.ai/) est une option rapide pour fine-tuner un modèle avec n'importe quel ensemble de données.

## Quels sont les avantages des LLMs auto-hébergés ?

Comme je l'ai brièvement discuté ci-dessus, il existe diverses raisons d'auto-héberger un LLM. Pour résumer, voici quelques-uns des principaux avantages :

* Amélioration de la confidentialité et de la sécurité des données, car vos données ne quittent pas votre ordinateur, et vous avez un contrôle complet sur elles.

* Économies de coûts, car vous n'avez pas besoin de payer régulièrement pour des abonnements API. Au lieu de cela, c'est un investissement unique pour obtenir une infrastructure suffisamment puissante pour vous aider à long terme.

* Grande personnalisation, car vous pouvez adapter les modèles à vos besoins spécifiques grâce au fine-tuning ou à l'entraînement sur vos propres ensembles de données.

* Latence réduite

## Quand ne devriez-vous PAS utiliser une IA auto-hébergée ?

Mais cela pourrait ne pas être la bonne solution pour vous pour plusieurs raisons. Tout d'abord, vous ne disposez peut-être pas des ressources système nécessaires pour pouvoir exécuter les modèles, et peut-être que vous ne voulez pas ou ne pouvez pas mettre à niveau.

Deuxièmement, vous ne disposez peut-être pas des connaissances techniques ou du temps pour configurer votre propre modèle et le fine-tuner. Ce n'est pas terriblement difficile, mais cela nécessite quelques connaissances de base et des compétences particulières. Cela peut également être un problème si vous ne savez pas comment résoudre les erreurs qui peuvent survenir.

Vous pouvez également avoir besoin que vos modèles soient disponibles 24h/24 et 7j/7, et vous ne disposez peut-être pas de l'infrastructure pour le gérer.

Aucun de ces problèmes n'est insurmontable, mais ils peuvent influencer votre décision quant à savoir si vous utilisez une solution basée sur le cloud ou hébergez votre propre modèle.

## Conclusion

Héberger vos propres LLMs peut être un changement de jeu si vous valorisez la confidentialité des données, l'efficacité des coûts et la personnalisation.

Des outils comme Ollama rendent plus facile que jamais d'apporter des modèles d'IA puissants directement à votre infrastructure personnelle. Bien que l'auto-hébergement ne soit pas sans ses défis, il vous donne le contrôle sur vos données et la flexibilité d'adapter les modèles à vos besoins.

Assurez-vous simplement d'évaluer vos capacités techniques, vos ressources matérielles et les exigences de votre projet avant de décider de suivre cette voie. Si vous avez besoin de fiabilité, de scalabilité et d'un accès rapide aux fonctionnalités de pointe, les LLMs basés sur le cloud pourraient encore être la meilleure solution.

Si vous avez aimé cet article, n'oubliez pas de montrer votre soutien et de me suivre sur [X](https://x.com/Codeskae) et [LinkedIn](https://www.linkedin.com/in/imkrishnasarathi/) pour rester connecté. De plus, je crée du contenu tech court mais informatif sur [YouTube](https://youtube.com/@krishcodes), alors n'oubliez pas de consulter mon contenu.

Merci d'avoir lu cet article !