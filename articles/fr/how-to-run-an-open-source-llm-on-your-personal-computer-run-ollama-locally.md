---
title: Comment exécuter un LLM open-source sur votre ordinateur personnel – Exécuter
  Ollama localement
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-10T21:19:06.401Z'
originalURL: https://freecodecamp.org/news/how-to-run-an-open-source-llm-on-your-personal-computer-run-ollama-locally
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762809417189/37e154b9-9bf0-4210-921a-4722cd448b09.png
tags:
- name: 'LLM''s '
  slug: llms
- name: llm
  slug: llm
- name: open source
  slug: open-source
- name: ollama
  slug: ollama
seo_title: Comment exécuter un LLM open-source sur votre ordinateur personnel – Exécuter
  Ollama localement
seo_desc: 'Running a large language model (LLM) on your computer is now easier than
  ever. You no longer need a cloud subscription or a massive server. With just your
  PC, you can run models like Llama, Mistral, or Phi, privately and offline.

  This guide will show...'
---

Exécuter un grand modèle de langage (LLM) sur votre ordinateur est désormais plus facile que jamais. Vous n'avez plus besoin d'un abonnement cloud ou d'un serveur massif. Avec seulement votre PC, vous pouvez exécuter des modèles comme Llama, Mistral ou Phi, de manière privée et hors ligne.

Ce guide vous montrera comment configurer un LLM open-source localement, expliquera les outils impliqués et vous guidera à travers les méthodes d'installation via l'UI et la ligne de commande.

## Ce que nous allons aborder

* [Comprendre les LLM open-source](#heading-comprendre-les-llm-open-source)
    
* [Choisir une plateforme pour exécuter des LLM localement](#heading-choisir-une-plateforme-pour-executer-des-llm-localement)
    
* [Comment installer Ollama](#heading-comment-installer-ollama)
    
* [Comment installer et exécuter des LLM via la ligne de commande](#heading-comment-installer-et-executer-des-llm-via-la-ligne-de-commande)
    
* [Comment gérer les modèles et les ressources](#heading-comment-gerer-les-modeles-et-les-ressources)
    
* [Comment utiliser Ollama avec d'autres applications](#heading-comment-utiliser-ollama-avec-d-autres-applications)
    
* [Dépannage et problèmes courants](#heading-depannage-et-problemes-courants)
    
* [Pourquoi l'exécution locale des LLM est importante](#heading-pourquoi-lexecution-locale-des-llm-est-importante)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre les LLM open-source

Un grand modèle de langage open-source est un type d'IA capable de comprendre et de générer du texte, tout comme ChatGPT, mais il peut fonctionner sans dépendre de serveurs externes.

Vous pouvez télécharger les fichiers du modèle, les exécuter sur votre machine et même les [fine-tune](https://www.turingtalks.ai/p/how-ai-agents-remember-things-the-role-of-vector-stores-in-llm-memory) pour vos cas d'utilisation spécifiques.

Des projets comme Llama 3, Mistral, Gemma et Phi ont permis d'exécuter des modèles qui s'adaptent bien au matériel grand public. Vous pouvez choisir entre des modèles plus petits qui fonctionnent sur CPU ou des plus grands qui bénéficient des GPU.

L'exécution de ces modèles localement vous offre confidentialité, contrôle et flexibilité. Cela aide également les développeurs à intégrer des fonctionnalités d'IA dans leurs applications sans dépendre d'API cloud.

## Choisir une plateforme pour exécuter des LLM localement

Pour exécuter un modèle open-source, vous avez besoin d'une plateforme capable de le charger, de gérer ses paramètres et de fournir une interface pour interagir avec lui.

Trois choix populaires pour une configuration locale sont :

1. [**Ollama**](https://ollama.com/) — un système convivial qui exécute des modèles comme OpenAI GPT OSS, Google Gemma avec une seule commande. Il dispose d'une version UI pour Windows et d'une version CLI.
    
2. [**LM Studio**](https://lmstudio.ai/) — une application de bureau graphique pour ceux qui préfèrent une interface point-and-click.
    
3. [Gpt4All](https://www.nomic.ai/gpt4all) — une autre application de bureau GUI populaire.
    

Nous utiliserons Ollama comme exemple dans ce guide car il est largement supporté et s'intègre facilement avec d'autres outils.

## Comment installer Ollama

Ollama fournit un installeur en un clic qui configure tout ce dont vous avez besoin pour exécuter des modèles locaux. Visitez [le site officiel d'Ollama](https://ollama.com/) et téléchargez l'installeur Windows.

![Page d'accueil d'Ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1762438947066/9b6c84c1-e8ae-4765-9b55-a444bdf68283.png align="center")

Une fois téléchargé, double-cliquez sur le fichier pour lancer l'installation. L'assistant de configuration vous guidera tout au long du processus, qui ne prend que quelques minutes.

Lorsque l'installation est terminée, Ollama s'exécutera en arrière-plan en tant que service local. Vous pouvez y accéder soit par son interface de bureau graphique, soit en utilisant la ligne de commande.

Après avoir installé Ollama, vous pouvez ouvrir l'application depuis le Menu Démarrer. L'UI facilite l'interaction avec les modèles locaux pour les débutants.

![Interface Ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439008725/a1ebb4fc-c638-41f0-817a-cd6772c8577e.png align="center")

Sur l'interface d'Ollama, vous verrez une simple zone de texte où vous pouvez taper des prompts et recevoir des réponses. Il y a également un panneau qui liste les modèles disponibles.

![Modèles Ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439045357/760b04b6-f826-422d-8ba9-6a255917ae29.png align="center")

Pour télécharger et utiliser un modèle, il suffit de le sélectionner dans la liste. Ollama récupérera automatiquement les poids du modèle et les chargera en mémoire.

La première fois que vous posez une question, il téléchargera le modèle s'il n'existe pas. Vous pouvez également choisir le modèle sur la [page de recherche de modèles](https://ollama.com/search).

J'utiliserai le modèle [gemma 270m](https://ollama.com/library/gemma3) qui est le plus petit modèle disponible dans Ollama.

![Ollama téléchargeant un modèle](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439068617/c88f191b-f2f7-4c7a-b1dc-b1eea7745a35.png align="center")

Vous pouvez voir le modèle en cours de téléchargement lors de sa première utilisation. Selon la taille du modèle et les performances de votre système, cela peut prendre quelques minutes.

Une fois chargé, vous pouvez commencer à discuter ou à exécuter des tâches directement dans l'UI. Elle est conçue pour ressembler à une fenêtre de chat normale, mais tout s'exécute localement sur votre PC.

Vous n'avez pas besoin de connexion Internet une fois que le modèle a été téléchargé.

## Comment installer et exécuter des LLM via la ligne de commande

Si vous préférez plus de contrôle, vous pouvez utiliser l'interface de ligne de commande (CLI) d'Ollama. C'est utile pour les développeurs ou ceux qui souhaitent intégrer des modèles locaux dans des scripts et des workflows.

Pour ouvrir la ligne de commande, recherchez « Invite de commandes » ou « PowerShell » dans Windows et lancez-le. Vous pouvez maintenant interagir avec Ollama en utilisant des commandes simples.

Pour vérifier si l'installation a fonctionné, tapez :

```python-repl
ollama --version
```

Si vous voyez un numéro de version, Ollama est prêt. Ensuite, pour exécuter votre premier modèle, utilisez la commande pull :

```python-repl
ollama pull gemma3:270m
```

Cela téléchargera le modèle Gemma sur votre machine.

![Ollama pull model](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439104192/14ed4a53-330f-41c6-82dd-f2a22ecb9d05.png align="center")

Lorsque le processus est terminé, lancez-le avec :

```python-repl
ollama run gemma3:270m
```

Ollama lancera le modèle et ouvrira une invite interactive où vous pourrez taper des messages.

![Shell interactif Ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439115178/9d17c753-52af-4834-93f4-155bad39bd8d.png align="center")

Tout se passe localement, et vos données ne quittent jamais votre ordinateur.

Vous pouvez arrêter le modèle à tout moment en tapant `/bye`.

## Comment gérer les modèles et les ressources

Chaque modèle que vous téléchargez occupe de l'espace disque et de la mémoire. Les modèles plus petits comme Phi-3 Mini ou Gemma 2B sont plus légers et adaptés à la plupart des ordinateurs portables grand public. Les plus grands comme Mistral 7B ou Llama 3 8B nécessitent des GPU plus puissants ou des CPU haut de gamme.

Vous pouvez lister tous les modèles installés en utilisant :

```python-repl
ollama list
```

![Modèles installés Ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439131985/31bc6125-aec9-47bb-90a8-7017d422e527.png align="center")

Et en supprimer un lorsque vous n'en avez plus besoin :

```python-repl
ollama rm nom_du_modèle
```

Si votre PC a une RAM limitée, essayez d'abord d'exécuter des modèles plus petits. Vous pouvez expérimenter avec différents modèles pour trouver le bon équilibre entre vitesse et précision.

## Comment utiliser Ollama avec d'autres applications

Une fois Ollama installé, vous pouvez l'utiliser au-delà de l'interface de chat. Les développeurs peuvent s'y connecter via des API et des ports locaux.

Ollama exécute un serveur local sur `http://localhost:11434`. Cela signifie que vous pouvez envoyer des requêtes depuis vos propres scripts ou applications.

![API Ollama](https://cdn.hashnode.com/res/hashnode/image/upload/v1762439148881/b506c227-8b83-45f4-a2c3-662081ec9faf.png align="center")

Par exemple, un simple script Python peut appeler le modèle local comme ceci :

```python
import requests, json

# Définir l'endpoint de l'API locale Ollama
url = "http://localhost:11434/api/generate"

# Envoyer un prompt au modèle Gemma 3
payload = {
    "model": "gemma3:270m",
    "prompt": "Write a short story about space exploration."
}

# stream=True indique à requests de lire la réponse comme un flux de données en direct
response = requests.post(url, json=payload, stream=True)

# Ollama envoie un objet JSON par ligne au fur et à mesure qu'il génère du texte
for line in response.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        # Chaque bloc possède une clé "response" contenant une partie du texte
        if "response" in data:
            print(data["response"], end="", flush=True)
```

Cette configuration transforme votre ordinateur en un moteur d'IA local. Vous pouvez l'intégrer à des chatbots, des assistants de codage ou des outils d'automatisation sans utiliser d'API externes.

## Dépannage et problèmes courants

Si vous rencontrez des problèmes pour exécuter un modèle, vérifiez d'abord les ressources de votre système. Les modèles ont besoin de suffisamment de RAM et d'espace disque pour se charger correctement. Fermer d'autres applications peut aider à libérer de la mémoire.

Parfois, un logiciel antivirus peut bloquer les ports réseau locaux. Si Ollama ne parvient pas à démarrer, ajoutez-le à la liste des programmes autorisés.

Si vous utilisez le CLI et voyez des erreurs concernant les pilotes GPU, assurez-vous que vos pilotes graphiques sont à jour. Ollama prend en charge l'exécution sur CPU et GPU, mais des pilotes à jour améliorent les performances.

## Pourquoi l'exécution locale des LLM est importante

L'exécution locale des LLM change votre façon de travailler avec l'IA. Vous n'êtes plus lié aux coûts d'API ou aux limites de débit. C'est idéal pour les développeurs qui veulent prototyper rapidement, les chercheurs explorant le fine-tuning ou les passionnés qui accordent de l'importance à la confidentialité.

Les modèles locaux sont également parfaits pour les environnements hors ligne. Vous pouvez expérimenter la conception de prompts, générer du contenu ou tester des applications assistées par l'IA sans connexion Internet.

À mesure que le matériel s'améliore et que les communautés open-source grandissent, l'IA locale continuera de devenir plus puissante et accessible.

## Conclusion

Configurer et exécuter un LLM open-source sur Windows est désormais simple. Avec des outils comme Ollama et LM Studio, vous pouvez télécharger un modèle, l'exécuter localement et commencer à générer du texte en quelques minutes.

L'UI le rend convivial pour les débutants, tandis que la ligne de commande offre un contrôle total pour les développeurs. Que vous construisiez une application, testiez des idées ou exploriez l'IA pour un usage personnel, l'exécution de modèles localement met tout entre vos mains, le rendant rapide, privé et flexible.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*