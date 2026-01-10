---
title: Comment compresser vos prompts et réduire les coûts des LLM
subtitle: Microsoft vient de résoudre le problème des coûts cachés de l'IA avec LLMLingua,
  rendant les grands modèles de langage plus rapides, moins chers et plus intelligents.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-18T19:10:56.935Z'
originalURL: https://freecodecamp.org/news/how-to-compress-your-prompts-and-reduce-llm-costs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763493041384/75c787b8-6e41-4733-bf8d-815170196b5b.png
tags:
- name: llm
  slug: llm
- name: AI
  slug: ai
seo_title: Comment compresser vos prompts et réduire les coûts des LLM
seo_desc: 'Every developer working with large language models eventually faces the
  same challenge: prompts keep getting longer, models keep getting slower, and API
  bills keep getting higher.

  Whether you’re building a retrieval-augmented generation (RAG) system ...'
---


Chaque développeur travaillant avec de grands modèles de langage finit par être confronté au même défi : les prompts deviennent de plus en plus longs, les modèles de plus en plus lents et les factures d'API de plus en plus élevées.

Que vous construisiez un système de [génération augmentée par récupération](https://www.freecodecamp.org/news/mastering-rag-from-scratch/) (RAG) ou un chatbot qui se souvient des conversations passées, chaque token supplémentaire ajoute du coût et de la latence.

Microsoft a discrètement introduit une solution que peu de personnes en dehors des cercles de recherche ont remarquée, avec un projet appelé [LLMLingua](https://github.com/microsoft/LLMLingua). Il compresse les prompts avant de les envoyer à un modèle, ne conservant que les informations les plus importantes. Le résultat : des réponses plus rapides, des factures moins élevées et une voie plus facile pour mettre à l'échelle les LLM.

Dans ce tutoriel, nous verrons comment utiliser LLMLingua pour optimiser vos prompts et les rendre plus efficaces tout en économisant des coûts.

## Ce que nous allons aborder :

* [Le problème caché à la vue de tous](#heading-le-probleme-cache-a-la-vue-de-tous)
    
* [Ce que LLMLingua fait différemment](#heading-ce-que-llmlingua-fait-differemment)
    
* [Travailler avec LLMLingua](#heading-travailler-avec-llmlingua)
    
* [Gestion des contextes longs avec LongLLMLingua](#heading-gestion-des-contextes-longs-avec-longllmlingua)
    
* [LLMLingua-2 : Plus rapide et plus intelligent](#heading-llmlingua-2-plus-rapide-et-plus-intelligent)
    
* [Compression de prompt structurée](#heading-compression-de-prompt-structuree)
    
* [SecurityLingua : La compression comme défense](#heading-securitylingua-la-compression-comme-defense)
    
* [Intégration avec l'écosystème](#heading-integration-avec-lecosysteme)
    
* [Pourquoi LLMLingua est important](#heading-pourquoi-llm-lingua-est-important)
    
* [Conclusion](#heading-conclusion)
    

## Le problème caché à la vue de tous

Lorsqu'un LLM traite un prompt, chaque token compte pour votre coût et la limite d'attention du modèle.

Pour les [applications gourmandes en contexte](https://www.turingtalks.ai/p/how-ai-agents-remember-things-the-role-of-vector-stores-in-llm-memory), il est courant d'atteindre la fenêtre de tokens maximale bien avant d'arriver à la partie utile de vos données.

Ajouter plus de contexte peut aider le modèle à mieux raisonner, mais cela ralentit également l'inférence. Les prompts longs prennent non seulement plus de temps pour générer des réponses, mais entament également votre budget lorsque vous utilisez des API comme GPT-4 ou Claude.

LLMLingua cible directement ce problème en compressant les prompts intelligemment sans réentraîner ni modifier le modèle sous-jacent.

## Ce que LLMLingua fait différemment

LLMLingua utilise un modèle de langage plus petit et compact, comme GPT-2 Small ou LLaMA-7B. Ce modèle plus petit aide à identifier et à supprimer les tokens non essentiels dans un prompt donné.

Au lieu d'envoyer des milliers de tokens à votre modèle principal, vous envoyez une version compacte qui conserve le sens.

Cette approche permet d'atteindre une compression allant jusqu'à 20x avec une perte de précision négligeable. En termes simples, LLMLingua permet à votre LLM de lire le même contenu avec moins de mots.

## Travailler avec LLMLingua

Commencer est simple. La bibliothèque est disponible sur PyPI et fonctionne immédiatement.

```python
pip install llmlingua
```

Une fois installée, vous pouvez l'importer dans Python pour commencer à compresser des prompts.

Voici comment vous pouvez compresser un long prompt textuel en utilisant LLMLingua :

```python
from llmlingua import PromptCompressor

# Initialize the compressor
llm_lingua = PromptCompressor()

# Compress the prompt
prompt = "Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box..."

compressed_prompt = llm_lingua.compress_prompt(prompt, instruction="", question="", target_token=200)

print(compressed_prompt)
```

Lorsque vous exécutez cela, vous obtiendrez un dictionnaire comme celui-ci :

```python
{
  'compressed_prompt': 'Question: Sam bought a dozen boxes each with 30 highlighter pens...',
  'origin_tokens': 2365,
  'compressed_tokens': 211,
  'ratio': '11.2x',
  'saving': 'Saving $0.1 in GPT-4.'
}
```

Vous pouvez également charger différents modèles en fonction de vos ressources.

```python
# Use a more powerful compression model
llm_lingua = PromptCompressor("microsoft/phi-2")

# Or use a quantized model for GPUs with limited memory
# Requires: pip install optimum auto-gptq
llm_lingua = PromptCompressor("TheBloke/Llama-2-7b-Chat-GPTQ", model_config={"revision": "main"})
```

Cette configuration simple peut permettre d'économiser des centaines de dollars en production si vous traitez de longs documents ou des historiques de chat.

## Gestion des contextes longs avec LongLLMLingua

[LongLLMLingua](https://llmlingua.com/longllmlingua.html) étend ce concept à des entrées massives comme des PDF, des transcriptions ou des récupérations multi-documents. Il réordonne et filtre le contexte dynamiquement pour s'assurer que le modèle ne voit que les sections les plus pertinentes.

Voici comment vous pourriez l'utiliser :

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor()

compressed_prompt = llm_lingua.compress_prompt(
    prompt_list,
    question="What are the main regulatory changes in the last quarter?",
    rate=0.55,
    condition_in_question="after_condition",
    reorder_context="sort",
    dynamic_context_compression_ratio=0.3,
    condition_compare=True,
    context_budget="+100",
    rank_method="longllmlingua",
)
```

Cela fonctionne particulièrement bien dans les systèmes RAG où les documents varient en longueur et en pertinence. En combinant la récupération avec la compression, vous pouvez faire tenir plus de contexte dans votre LLM sans atteindre les limites de tokens.

## LLMLingua-2 : Plus rapide et plus intelligent

L'équipe de Microsoft ne s'est pas arrêtée là. Ils ont introduit [LLMLingua-2](https://llmlingua.com/llmlingua2.html), qui est plus rapide et plus polyvalent.

Il utilise la distillation de données de GPT-4 et un encodeur de niveau BERT pour améliorer la fidélité de la compression.

Cette version gère mieux les données hors domaine et s'exécute 3 à 6 fois plus vite que l'original.

```python
from llmlingua import PromptCompressor

# Initialize LLMLingua-2
llm_lingua = PromptCompressor(
    model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
    use_llmlingua2=True,
)

compressed_prompt = llm_lingua.compress_prompt(prompt, rate=0.33, force_tokens=['\n', '?'])

# Or use a smaller multilingual model
llm_lingua = PromptCompressor(
    model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank",
    use_llmlingua2=True,
)
```

Pour les scénarios multilingues et d'entreprise, LLMLingua-2 offre le bon équilibre entre coût, précision et rapidité.

## Compression de prompt structurée

Parfois, vous voulez contrôler quelles sections d'un prompt doivent être compressées.

LLMLingua prend en charge la compression structurée à l'aide de balises spéciales. Vous pouvez marquer des segments de texte à compresser à différents taux ou à ignorer entièrement.

```python
structured_prompt = """<llmlingua, compress=False>Speaker 4:</llmlingua>
<llmlingua, rate=0.4> Thank you. And can we do the functions for content? Items I believe are 11, three, 14, 16 and 28, I believe.</llmlingua>
<llmlingua, compress=False>Speaker 0:</llmlingua>
<llmlingua, rate=0.4> Item 11 is a communication from Council on Price recommendation...</llmlingua>"""

compressed_prompt = llm_lingua.structured_compress_prompt(
    structured_prompt,
    instruction="",
    question="Summarize the meeting notes",
    rate=0.5,
)
print(compressed_prompt['compressed_prompt'])
```

Cette fonctionnalité est particulièrement utile pour la synthèse de réunions ou les systèmes de prise de notes où les balises de locuteur ou les en-têtes de section doivent rester intacts.

## SecurityLingua : La compression comme défense

Un ajout plus récent, SecurityLingua, utilise une compression axée sur la sécurité pour détecter les tentatives de jailbreak malveillantes.

Il révèle l'intention nuisible cachée dans des prompts complexes et défend contre les attaques avec un coût en tokens 100x inférieur par rapport aux garde-fous traditionnels.

```python
from llmlingua import PromptCompressor

securitylingua = PromptCompressor(
    model_name="SecurityLingua/securitylingua-xlm-s2s",
    use_slingua=True
)
intention = securitylingua.compress_prompt(malicious_prompt)
```

Ce modèle propose une approche unique : au lieu de filtrer après la génération, il empêche les instructions malveillantes d'atteindre le modèle en premier lieu.

## Intégration avec l'écosystème

L'une des raisons pour lesquelles LLMLingua se démarque est la façon dont il s'intègre parfaitement dans l'écosystème de l'IA moderne.

Au lieu d'être un prototype de recherche autonome, il est déjà intégré dans des frameworks populaires comme [LangChain](https://www.turingtalks.ai/p/langchain-vs-langgraph), LlamaIndex et Microsoft Prompt Flow.

Cela signifie que vous pouvez le brancher directement dans vos pipelines RAG ou de traitement de documents existants sans réécrire de code ou changer vos modèles.

Par exemple, dans LangChain, LLMLingua agit comme une couche intermédiaire intelligente qui compresse le contexte récupéré avant qu'il n'atteigne le LLM.

Imaginez que vous utilisez un retriever pour extraire des documents d'une base de connaissances. Au lieu d'envoyer ces longs textes directement à votre modèle, LLMLingua filtre les tokens inutiles afin que votre prompt reste concis et efficace.

Voici comment vous pouvez l'intégrer :

```python
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors import LLMLinguaCompressor
from langchain_openai import ChatOpenAI

# Initialize your base model
llm = ChatOpenAI(temperature=0)

# Create an LLMLingua-based compressor
compressor = LLMLinguaCompressor(model_name="openai-community/gpt2", device_map="cpu")

# Wrap your existing retriever with LLMLingua compression
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever  # your existing document retriever
)
# Use it like a normal retriever, but now with smart compression
compressed_docs = compression_retriever.invoke(
    "What did the president say about Ketanji Jackson Brown"
)
pretty_print_docs(compressed_docs)
```

Dans cette configuration, le retriever rassemble d'abord les documents pertinents, et LLMLingua les compresse avant de les transmettre au LLM. Le modèle reçoit un prompt condensé mais riche en informations, ce qui maintient l'utilisation des tokens à un niveau bas tout en préservant la précision.

Cette intégration fonctionne immédiatement avec n'importe quel modèle pris en charge sur LangChain. Elle peut être personnalisée pour utiliser votre taux de compression préféré ou une variante du modèle (comme LLMLingua-2).

Le résultat est un pipeline plus efficace : votre LLM lit moins mais comprend plus.

## Pourquoi LLMLingua est important

LLMLingua ne fera peut-être pas les gros titres comme GPT-5 ou Gemini, mais son impact est fondamental. Il s'attaque à la partie la plus coûteuse des workflows de LLM : la gestion du contexte.

En supprimant les tokens redondants et en préservant l'intention, il transforme la manière dont les développeurs construisent des applications d'IA évolutives.

Que vous résumiez des données réglementaires, traitiez de longs documents juridiques ou alimentiez des chatbots multilingues, LLMLingua vous donne un nouveau levier d'optimisation.

Ce qu'il faut retenir est simple : l'avenir de l'efficacité de l'IA ne viendra pas seulement de modèles plus grands, mais de modèles plus intelligents et de prompts plus intelligents.

## Conclusion

LLMLingua de Microsoft est plus qu'un projet de recherche. C'est une révolution discrète dans la manière dont nous fournissons des informations aux LLM. Il permet aux développeurs de repousser les limites de contexte, de réduire les coûts et d'accélérer l'inférence, le tout sans réentraîner un seul modèle.

En apprenant à compresser les prompts intelligemment, LLMLingua vous aide à parler aux machines plus efficacement. Et dans le monde des grands modèles de langage, en dire plus avec moins est exactement le genre de progrès qui compte le plus.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*