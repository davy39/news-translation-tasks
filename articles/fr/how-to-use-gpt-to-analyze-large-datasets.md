---
title: Comment utiliser GPT pour analyser de grands ensembles de données
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2024-08-28T17:57:59.886Z'
originalURL: https://freecodecamp.org/news/how-to-use-gpt-to-analyze-large-datasets
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724798393633/8ad22b7c-646c-4c02-894d-6a6b08447049.jpeg
tags:
- name: '#ai-tools'
  slug: ai-tools
- name: generative ai
  slug: generative-ai
- name: analytics
  slug: analytics
seo_title: Comment utiliser GPT pour analyser de grands ensembles de données
seo_desc: Absorbing and then summarizing very large quantities of content in just
  a few seconds truly is a big deal. As an example, a while back I received a link
  to the recording of an important 90 minute business video conference that I'd missed
  a few hours ...
---

Absorber puis résumer de très grandes quantités de contenu en quelques secondes seulement est une véritable révolution. Par exemple, il y a quelque temps, j'ai reçu un lien vers l'enregistrement d'une importante visioconférence d'affaires de 90 minutes que j'avais manquée quelques heures auparavant.

La raison pour laquelle j'avais manqué la version en direct était que je n'avais pas le temps (je me dépêchais, si vous voulez tout savoir, de terminer mon [livre Manning, The Complete Obsolete Guide to Generative AI](https://amzn.to/3yLFT3b) – dont cet article est extrait).

Eh bien, une demi-douzaine d'heures plus tard, je n'avais toujours pas le temps pour la vidéo. Et, inexplicablement, le livre n'était toujours pas fini.

Voici comment j'ai résolu le conflit à la manière GPT :

* J'ai utilisé OpenAI Whisper pour générer une transcription basée sur l'audio de l'enregistrement
    
* J'ai exporté la transcription vers un fichier PDF
    
* J'ai téléchargé le PDF sur ChatPDF
    
* J'ai envoyé des prompts à ChatPDF pour obtenir des résumés liés aux sujets spécifiques qui m'intéressaient
    

Temps total pour « télécharger » les moments clés de l'appel de 90 minutes : 10 minutes. C'est 10 minutes pour convertir un ensemble de données composé d'environ 15 000 mots parlés en un format lisible par machine, puis pour le digérer, l'analyser et le résumer.

### Comment utiliser GPT pour l'analyse commerciale

Mais tout cela est déjà de l'histoire ancienne. Le niveau supérieur (le *next-level*) résoudra le problème de l'analyse commerciale (Business Analytics).

Bon. Alors, quel *est* le « problème de l'analyse commerciale » ? C'est le travail acharné consistant à construire un code sophistiqué qui analyse de grands ensembles de données pour les rendre systématiquement lisibles par machine (également connu sous le nom de « data wrangling »). Il applique ensuite des algorithmes complexes pour en extraire des informations utiles. La figure ci-dessous décrit globalement le processus.

![Un diagramme illustrant le processus de data wrangling](https://www.freecodecamp.org/news/content/images/2023/12/gai-8-1.png align="left")

Une grande partie du code répondant à cette description est incroyablement compliquée, sans parler de son ingéniosité. Inciter des ingénieurs de données brillants à écrire ce code astucieux peut, bien sûr, coûter des fortunes aux organisations. Le « problème » est donc le coût.

Ainsi, résoudre ce problème pourrait impliquer de mobiliser quelques centaines de dollars de frais d'API de modèles de langage étendus (LLM). Voici comment je prévois d'illustrer cela.

J'aurai besoin d'une feuille de calcul bien remplie pour travailler, n'est-ce pas ? Le meilleur endroit que je connaisse pour trouver de bonnes données est le [site Web Kaggle](https://www.kaggle.com/).

Kaggle est une plateforme en ligne permettant d'héberger des ensembles de données (et des compétitions de science des données). C'est devenu une ressource importante pour les scientifiques des données, les praticiens de l'apprentissage automatique et les chercheurs, leur permettant de présenter leurs compétences, d'apprendre des [autres](https://www.kaggle.com/) et de collaborer sur des projets. La plateforme offre une large gamme d'ensembles de données publics et privés, ainsi que des outils et des fonctionnalités pour soutenir l'exploration et la modélisation des données.

### Comment préparer un ensemble de données

L'ensemble de données [« Investing Program Type Prediction »](https://www.kaggle.com/datasets/snassimr/data-for-investing-type-prediction) associé à ce code devrait parfaitement convenir. D'après ce que je peux dire, il s'agissait de données agrégées par une banque quelque part dans le monde, représentant le comportement de ses clients.

Tout a été anonymisé, bien sûr, il n'y a donc aucun moyen pour nous de savoir de quelle banque il s'agit, qui étaient les clients, ni même où tout cela se passait dans le monde. En fait, je ne suis même pas sûr à 100 % de ce que chaque colonne de données représente.

Ce qui *est* clair, c'est que l'âge et le quartier de chaque client sont présents. Bien que les emplacements aient été anonymisés sous les noms `C1`, `C2`, `C3` et ainsi de suite, certaines des colonnes restantes contiennent clairement des informations financières.

Sur la base de ces hypothèses, mon objectif ultime est de rechercher des relations statistiquement valides entre les colonnes. Par exemple, existe-t-il des caractéristiques démographiques spécifiques (revenu, quartier, âge) qui prédisent une plus grande probabilité qu'un client achète des produits bancaires supplémentaires ? Pour cet exemple spécifique, je vais voir si je peux identifier les régions géographiques au sein des données dont le patrimoine net moyen des ménages est le plus élevé.

Pour des utilisations normales, des données aussi vaguement décrites seraient sans valeur. Mais puisque nous cherchons simplement à démontrer le processus, cela fera parfaitement l'affaire. Je vais *inventer* des en-têtes de colonnes qui correspondent plus ou moins à la forme de leurs données. Voici comment je les ai nommées :

* ID Client
    
* Âge du client
    
* Emplacement géographique
    
* Visites en agence par an
    
* Total des actifs du ménage
    
* Dette totale du ménage
    
* Total des investissements auprès de la banque
    

Les noms des colonnes doivent être très descriptifs car ce seront les seuls indices que je donnerai à GPT pour l'aider à comprendre les données. J'ai dû ajouter mes propres identifiants clients à cette première colonne (ils n'existaient pas à l'origine).

Le moyen le plus rapide que j'ai trouvé pour le faire a été d'insérer la formule `=(RAND())` dans la cellule de données supérieure de cette colonne (avec le fichier chargé dans un logiciel de tableur comme Excel, Google Sheets ou LibreOffice Calc), puis d'appliquer la formule au reste des lignes de données. Une fois cela fait, les 1 000 lignes de données auront des identifiants uniques, bien que ce soient des identifiants entre 0 et 1 avec de nombreuses décimales.

### Comment appliquer LlamaIndex au problème

Une fois mes données préparées, j'utiliserai [LlamaIndex](https://www.llamaindex.ai/) pour commencer à analyser les chiffres. Comme précédemment, le code que je vais exécuter va :

* Importer les fonctionnalités nécessaires
    
* Ajouter ma clé API OpenAI
    
* Lire le fichier de données qui se trouve dans le répertoire appelé `data`
    
* Construire les nœuds à partir desquels nous peuplerons notre index
    

```python
import os
import openai
from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTVectorStoreIndex

os.environ['OPENAI_API_KEY'] = "sk-XXXX"

documents = SimpleDirectoryReader('data').load_data()
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(documents)
index = GPTVectorStoreIndex.from_documents(documents)
```

Enfin, j'enverrai mon prompt :

```python
response = index.query(
    "Based on the data, which 5 geographic regions had the highest average household net wealth? Show me nothing more than the region codes"
)
print(response)
```

Le voici à nouveau dans un format plus lisible :

> *D'après les données, quelles sont les 5 régions géographiques qui affichent le patrimoine net des ménages le plus élevé ?*

J'ai posé cette question principalement pour confirmer que GPT comprenait les données. Il est toujours bon de tester votre modèle juste pour voir si les réponses que vous obtenez semblent refléter raisonnablement ce que vous savez déjà sur les données.

Pour répondre correctement, GPT devrait comprendre ce que signifie chacun des en-têtes de colonnes et les relations *entre* les colonnes. En d'autres termes, il devrait savoir comment calculer la valeur nette pour chaque ligne (ID de compte) à partir des valeurs des colonnes `Total des actifs du ménage`, `Dette totale du ménage` et `Total des investissements auprès de la banque`. Il devrait ensuite agréger tous les chiffres de valeur nette qu'il a générés par `Emplacement géographique`, calculer les moyennes pour chaque emplacement et, enfin, comparer toutes les moyennes et les classer.

Le résultat ? Je *pense* que GPT a réussi. Après une minute ou deux de réflexion profonde et intense (et environ 0,25 $ de frais d'API), on m'a montré cinq codes d'emplacement (G0, G90, G96, G97, G84, au cas où vous seriez curieux). Cela m'indique que GPT comprend la colonne d'emplacement de la même manière que moi et qu'il tente au moins de déduire des relations entre l'emplacement et les caractéristiques démographiques.

Qu'est-ce que je voulais dire par « je pense » ? Eh bien, je n'ai jamais vérifié pour confirmer que les chiffres avaient du sens. D'une part, il ne s'agit pas de vraies données de toute façon et, pour autant que je sache, j'ai peut-être mal deviné le contenu de chaque colonne.

Mais aussi parce que *chaque* analyse de données doit être vérifiée par rapport au monde réel. En ce sens, l'analyse générée par GPT n'est pas différente. En d'autres termes, chaque fois que vous travaillez avec des données censées représenter le monde réel, vous devriez toujours trouver un moyen de calibrer vos données à l'aide de valeurs connues pour confirmer que tout cela n'est pas une pure fiction.

J'ai ensuite posé une deuxième question qui reflète une requête réelle qui intéresserait n'importe quelle banque :

> *Sur la base de leur âge, de leur situation géographique, du nombre de visites annuelles en agence bancaire et du total des investissements actuels, quels sont les dix clients les plus susceptibles d'investir dans une nouvelle offre de produits ? Montrez-moi uniquement la valeur des colonnes* `ID Client` *pour ces dix clients.*

Une fois de plus, GPT a recraché une réponse qui, au moins, *semblait* avoir du sens. Cette question était également conçue pour tester GPT sur sa capacité à corréler plusieurs métriques et à les soumettre à une évaluation complexe (« ...les plus susceptibles d'investir dans une nouvelle offre de produits »).

Je considère cela comme une autre expérience réussie.

## Conclusion

GPT – et d'autres LLM – sont capables d'analyser, d'interpréter et de tirer des enseignements de manière indépendante à partir de grands ensembles de données.

Il y aura bien sûr des limites à cette magie. GPT et ses cousins peuvent encore halluciner, surtout lorsque vos prompts lui laissent trop de place pour être « créatif » ou, parfois, lorsque vous vous êtes trop enfoncé dans un seul fil de discussion. Et il existe également des limites strictes quant à la quantité de données qu'OpenAI vous permet de télécharger.

Mais, dans l'ensemble, vous pouvez accomplir plus et plus rapidement que ce que vous pouvez probablement imaginer en ce moment.

Bien que tout cela simplifie grandement le processus d'analyse de données, le succès dépend toujours de la compréhension du contexte réel de vos données et de la formulation de prompts spécifiques et astucieux. Ce sera votre travail.

*Cet article est extrait de* [*mon livre Manning, The Complete Obsolete Guide to Generative AI.*](https://amzn.to/3yLFT3b) *De nombreuses autres pépites technologiques sont disponibles sur* [*mon site Web*](https://bootstrap-it.com)*.*