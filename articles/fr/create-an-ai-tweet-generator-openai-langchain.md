---
title: Comment créer un générateur de tweets IA avec LangChain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-22T20:20:04.000Z'
originalURL: https://freecodecamp.org/news/create-an-ai-tweet-generator-openai-langchain
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/cover.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Comment créer un générateur de tweets IA avec LangChain
seo_desc: 'By Shane Duggan

  I''ve got a fun tutorial for you today. If you''ve read my previous article on building
  custom-knowledge chatbots using LangChain, then you must be bursting with ideas
  of great projects you can create.

  Well, I want to encourage your cre...'
---

Par Shane Duggan

J'ai un tutoriel amusant pour vous aujourd'hui. Si vous avez lu mon article précédent sur la création de [chatbots personnalisés utilisant LangChain](https://www.freecodecamp.org/news/langchain-how-to-create-custom-knowledge-chatbots/), alors vous devez être rempli d'idées de projets que vous pouvez créer.

Eh bien, je veux encourager votre créativité et donner un exemple concret de ce que vous pouvez construire en utilisant LangChain ainsi qu'un grand modèle de langage (LLM). Et bien que cela puisse sembler intimidant, c'est en fait assez simple à implémenter.

Aujourd'hui, nous allons créer un générateur de tweets IA en utilisant LangChain et les LLM d'OpenAI. C'est un projet simple qui prend un sujet de tweet et génère un tweet à ce sujet.

Mais qu'y a-t-il de si spécial à cela ? Eh bien, la partie amusante est que nous allons utiliser LangChain pour pouvoir **référencer des informations à jour** via Wikipedia. Cela nous permet de surmonter la limitation des données d'entraînement de ChatGPT, car il n'a été entraîné que sur des données jusqu'en 2021.

Voici ce que nous allons créer :

![Image](https://lh4.googleusercontent.com/B-AqnuHPFtkT010tllL0VZlbZRK-wasEjUwl8a5yzDRCuG3VYRt8hz1QPC3tz1F_vnDSXwHM8gJNIbM9jFcGbnz1uu4OSQB-hTVSuDYULlfVRWlQfewvFpS4-XF8pkMn37Gu5Au4liSxujehfV7uCWg)

Jetez un coup d'œil aux informations référencées par notre tweet ci-dessous. Il utilise les informations de Wikipedia concernant l'investissement de Microsoft dans OpenAI **en 2023**. Ainsi, vous n'aurez plus à vous soucier du fait que les données référencées par votre IA soient obsolètes.

![Image](https://lh6.googleusercontent.com/r5CxHduLOViifkCaI2R84nl-n26rGVHnJCOa3Rgpt_WqXlyL9O7Hnar52p0yGLhKNhe3F5F3X6CNM98-0oJBeBXQ8IvQvNgTZirblgs5lSU4j8G9X_X1ROgoPd06vIGhLd_mdmWyEZzAtrC5ESSXvZA)

Si cela vous semble intéressant, alors plongeons-nous dans le vif du sujet.

## Comment configurer le projet

Bien que ce projet nécessite plusieurs composants, tout se trouve en fait dans un seul fichier app.py qui rassemble simplement plusieurs API.

Structurellement, nous allons simplement créer le fichier app.py et un fichier apikey.py pour stocker nos clés API (principalement pour [OpenAI](https://openai.com/blog/openai-api)).

En plus de cela, installons nos services. Voici la liste des bibliothèques que nous allons utiliser pour ce projet :

* **Streamlit** – Utilisé pour construire l'application
* **LangChain** – Utilisé pour construire le flux de travail LLM.
* **OpenAI** – Pour utiliser OpenAI GPT
* **Wikipedia** – Utilisé pour connecter GPT à WIKIPEDIA
* **ChromaDB** – Stockage vectoriel
* **Tiktoken** – Tokenizer backend pour OpenAI

Pour installer ces bibliothèques, exécutez la commande suivante dans votre terminal :

```
pip install streamlit langchain openai wikipedia chromadb tiktoken
```

Si votre système contient déjà certains de ces services, vous pouvez les installer un par un. De plus, nous allons mapper la variable de clé API pour cet environnement. Importons ces éléments dans notre fichier app.py et nous devrions être prêts à commencer.

```python
import os 
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey
```

## Comment implémenter l'interface utilisateur

Maintenant, l'application que nous créons est assez simple. J'ai donc décidé de garder les choses aussi minimalistes que possible avec l'interface utilisateur, avec un seul titre et un champ de saisie de texte. Pour ce générateur de tweets, cela remplit son objectif.

```python
# Création du titre et du champ de saisie
st.title('\ud83e\udd9c\ud83d\udd17 Générateur de Tweets')
prompt = st.text_input('Sujet du tweet : ')
```

Plus tard, nous ajouterons des fonctionnalités pour afficher l'historique de nos sujets, l'historique des tweets, et surtout, les données Wikipedia que nous avons référencées. Pour l'instant, voici l'interface utilisateur avec laquelle nous allons travailler :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-21-at-4.38.00-PM.png)

## Comment inclure les modèles de prompts

Nous entrons maintenant dans le territoire de LangChain. À ce stade, si vous n'êtes pas familier avec LangChain et que vous n'avez pas lu mon [article précédent](https://www.freecodecamp.org/news/langchain-how-to-create-custom-knowledge-chatbots/) sur LangChain, je vous recommande vivement de le faire pour mieux comprendre les étapes à venir.

La première chose que nous allons faire est d'introduire nos PromptTemplates. Pour rappel, les PromptTemplates agissent comme des enveloppes pour vos prompts afin de pouvoir les enchaîner avec plusieurs opérations, ce qui est la base de LangChain.

De plus, nous inclurons un wrapper pour l'API Wikipedia afin de pouvoir inclure les données dans l'exécution de la chaîne.

```python
# Modèle pour le titre
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='écris-moi un tweet sur {topic}'
)

# Modèle pour le tweet
tweet_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='écris-moi un tweet sur ce titre TITRE : {title} tout en utilisant cette recherche wikipedia : {wikipedia_research} '
)

# Wrapper pour les données Wikipedia
wiki = WikipediaAPIWrapper()
```

Dans cet exemple, j'ai également créé un prompt de titre, juste pour nous donner un titre général de notre sujet de tweet. Pour le prompt réel, si vous avez utilisé ChatGPT, c'est essentiellement le même concept – c'est juste que maintenant nous introduisons des variables (sujets de tweets).

Cela nous permet d'éviter de taper "écris-moi un tweet sur..." pour chaque entrée. Au lieu de cela, nous devons simplement insérer le sujet. Cela étant dit, passons à l'introduction du LLM OpenAI.

## Introduction aux LLM d'OpenAI

Il existe plusieurs façons de faire cela, et vous pouvez choisir le modèle que vous jugez approprié. Dans mon article précédent, j'ai utilisé le modèle de chat GPT-3.5-turbo avec le code suivant :

```python
chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)
messages = [
    SystemMessage(content="Vous êtes un expert en science des données"),
    HumanMessage(content="Écrivez un script Python qui entraîne un réseau de neurones sur des données simulées")
]
```

Mais vous pouvez décider quel module vous souhaitez utiliser avec votre clé API et suivre la [documentation de LangChain](https://python.langchain.com/docs/modules/model_io/models/llms/integrations/openai) pour le configurer.

Aujourd'hui, nous allons utiliser le modèle "text-davinci-003", qui est essentiellement le même modèle GPT-3 que dans les premiers jours de ChatGPT.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-22-at-12.17.17-PM.png)
_Les différents modèles d'OpenAI (Trouvés sur leur [site web](https://platform.openai.com/docs/models/overview))_

N'hésitez pas à expérimenter avec les modèles pour voir quels tweets donnent les meilleurs résultats. Vous pourriez même essayer le GPT-4, significativement plus puissant (et coûteux), mais avec un cas de complétion de prompt aussi simple qu'un générateur de tweets, cela pourrait ne pas être nécessaire.

```python
llm = OpenAI(model_name="text-davinci-003", temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
```

J'ai également décidé de spécifier la température à 0,9 pour permettre au modèle de générer des tweets plus créatifs. La température agit comme une mesure de la randomisation et de la créativité des réponses du modèle, allant de 0 pour des réponses directes, à 1 pour des réponses aléatoires. Si vous souhaitez que vos tweets soient plus factuels et déterministes, réduisez simplement cette valeur.

La température sera la seule variable dont nous aurons besoin pour faire fonctionner cela. Si vous souhaitez en savoir plus sur les autres champs, prenez le temps de lire la documentation et de comprendre ce qu'ils sont.

Par exemple, nous pouvons spécifier des limites de tokens pour nous assurer de ne pas obtenir une réponse trop longue, mais avec nos modèles de prompts de tweets actuels, cela ne devrait pas poser de problème.

## Comment garder une trace de l'historique de génération de tweets

Cette partie est optionnelle mais offre une fonctionnalité supplémentaire à l'application. Si vous souhaitez garder une trace de l'historique de l'activité de l'application avec des informations telles que les titres précédents ou les tweets, incluez simplement l'étape suivante :

```python
# Mémoire 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')
```

Dans le code ci-dessus, nous avons créé deux variables de mémoire différentes, `title_memory` et `script_memory`. La `title_memory` conserve l'historique des sujets de tweets et la `script_memory` conserve l'historique des tweets.

[ConversationBufferMemory](https://python.langchain.com/docs/modules/memory/how_to/buffer) est une fonctionnalité de LangChain qui vous permet de garder une trace des entrées et des sorties données jusqu'à présent (dans ce cas, ce sont simplement les sujets et les tweets que nous avons précédemment générés).

## Comment enchaîner les composants

Maintenant que nous avons tous les composants de notre application triés (l'interface utilisateur, les modèles de prompts et notre wrapper Wikipedia), nous pouvons tout rassembler pour l'exécuter. Et c'est là que réside la valeur de LangChain.

Une bonne analogie pour cela serait les fonctions composites dans un programme standard. Sauf que, dans notre cas, nos fonctions sont les PromptTemplates, les LLM et les données Wikipedia. En utilisant nos wrappers de précédemment, nous décidons simplement de l'ordre d'exécution (comme une chaîne) pour obtenir notre sortie souhaitée.

Dans ce cas, cela consisterait à obtenir le titre à partir de notre sujet, suivi de la création du tweet en utilisant des recherches pertinentes sur Wikipedia sur le sujet, puis en affichant ceux-ci à l'aide de Streamlit.

```python
if prompt: 
    title = title_chain.run(prompt)  # Exécution du prompt de titre
    wiki_research = wiki.run(prompt)  # Effectuer une recherche sur Wikipedia
    script = script_chain.run(title=title, wikipedia_research=wiki_research) # Création du tweet

    st.write(title)  # Afficher le sujet/titre du tweet
    st.write(script)  # Afficher le tweet généré

    with st.expander('Historique des titres'): 
        st.info(title_memory.buffer)   # Stocker le sujet du tweet dans l'historique

    with st.expander('Historique des tweets'): 
        st.info(script_memory.buffer)  # Stocker le tweet dans l'historique

    with st.expander('Recherche Wikipedia'): 
        st.info(wiki_research)  # Stocker la recherche Wikipedia sur le sujet dans l'historique
```

Lorsque nous exécutons ces chaînes, nous prenons essentiellement le sujet de l'interface utilisateur et l'insérons dans les PromptTemplates qui sont enchaînés avec le LLM. Le PromptTemplate de tweet prend également des données de Wikipedia pour alimenter le LLM.

Enfin, il est temps de vérifier notre application. Exécutez-la avec la commande suivante :

```
streamlit run app.py
```

## Code final et où aller à partir de là

Le résultat est de pouvoir surmonter les limitations d'informations obsolètes de ChatGPT et de créer des tweets pertinents. Si vous avez trouvé difficile de suivre, voici ce que nous avons jusqu'à présent :

```python
# Importation des packages, fichiers et services nécessaires
import os 
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

# Framework de l'interface utilisateur de l'application
st.title('\ud83e\udd9c\ud83d\udd17 Générateur de Tweets')
prompt = st.text_input('Sujet du tweet : ') 

# Modèles de prompts
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='écris-moi un tweet sur {topic}'
)

tweet_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='écris-moi un tweet sur ce titre TITRE : {title} tout en utilisant cette recherche wikipedia : {wikipedia_research} '
)

# Données Wikipedia
wiki = WikipediaAPIWrapper()

# Mémoire 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
tweet_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(model_name="text-davinci-003", temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
tweet_chain = LLMChain(llm=llm, prompt=tweet_template, verbose=True, output_key='script', memory=tweet_memory)

# Enchaînement des composants et affichage des sorties
if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    tweet = tweet_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title) 
    st.write(tweet) 

    with st.expander('Historique des titres'): 
        st.info(title_memory.buffer)

    with st.expander('Historique des tweets'): 
        st.info(tweet_memory.buffer)

    with st.expander('Recherche Wikipedia'): 
        st.info(wiki_research)
```

Bien sûr, un générateur de tweets est un exemple simple de ce que vous pouvez faire avec LangChain et les LLM. Vous pouvez appliquer ce même processus pour créer un générateur de scripts YouTube ou un assistant de calendrier de contenu pour les réseaux sociaux, par exemple. Les possibilités sont infinies.

## Conclusion

J'espère que vous avez apprécié ce tutoriel amusant ! LangChain est devenu extrêmement populaire ces derniers temps et pour de bonnes raisons – il est incroyablement polyvalent. Je vous recommande vivement de le découvrir.

Si vous avez aimé cet article et que vous souhaitez en savoir plus sur les nouveaux outils passionnants que les créateurs d'IA développent, vous pouvez rester à jour avec ma [**Newsletter Byte-Sized AI**](https://bytesizedai.beehiiv.com/subscribe). Il y a des tonnes d'histoires passionnantes sur ce que les gens construisent dans le domaine de l'IA, et j'adorerais que vous rejoigniez notre communauté.

Je poste également régulièrement sur [Linkedin](https://www.linkedin.com/in/shanepduggan/) et je serais ravi de vous connecter ! Sinon, bon développement et j'ai hâte de voir les projets que vous allez créer.