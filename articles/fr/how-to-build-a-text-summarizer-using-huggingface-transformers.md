---
title: Comment construire un résumé de texte en utilisant Hugging Face Transformers
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-02-28T10:13:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-text-summarizer-using-huggingface-transformers
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/summary-1.jpeg
tags:
- name: nlp
  slug: nlp
seo_title: Comment construire un résumé de texte en utilisant Hugging Face Transformers
seo_desc: 'In today’s fast-paced world, we’re bombarded with information. It’s like
  trying to drink water from a fire hose.

  That''s where a text summarizer comes in. Imagine it as a filter that separates
  the essential bits from the overwhelming flood of words.

  I...'
---

Dans le monde trépidant d'aujourd'hui, nous sommes bombardés d'informations. C'est comme essayer de boire de l'eau à partir d'un tuyau d'incendie.

C'est là qu'intervient un résumé de texte. Imaginez-le comme un filtre qui sépare les éléments essentiels de l'inondation écrasante de mots.

Dans cet article, je vais vous expliquer ce qu'est un résumé, ses cas d'utilisation, ce que sont les Transformers de Hugging Face, et comment vous pouvez construire votre propre résumé de texte en utilisant les Transformers de Hugging Face. Plongeons-nous dans le sujet.

## Qu'est-ce qu'un résumé ?

Un résumé fait exactement ce que son nom suggère. Il prend un grand bloc de texte et le condense en une version plus courte.

Cette version plus courte ne conserve que les points clés. Pensez-y comme à la différence entre lire un roman entier et jeter un coup d'œil à sa couverture arrière. Le but est de gagner du temps tout en obtenant l'essence du contenu.

## Cas d'utilisation d'un résumé

Les résumés ne sont pas seulement des astuces technologiques sympas. Ils répondent à des besoins réels.

Les journalistes les utilisent pour trier rapidement les rapports et les études. Les étudiants les utilisent pour résumer les lectures longues. Les entreprises les utilisent pour condenser les analyses de marché ou les rapports longs.

En essence, toute personne qui doit traiter de grandes quantités de texte rapidement peut bénéficier d'un résumé.

## Qu'est-ce que Hugging Face Transformers ?

[Hugging Face](https://huggingface.co/) est une entreprise qui a créé une plateforme de pointe pour le traitement du langage naturel (NLP).

Leur bibliothèque Transformers est comme un trésor pour les tâches de NLP. Elle inclut des modèles pré-entraînés qui peuvent tout faire, de la traduction et de l'analyse des sentiments, à oui, la synthèse.

Ces modèles ont appris à partir de vastes quantités de texte et peuvent comprendre et générer du langage de manière surprenamment humaine.

## Comment construire un résumé avec Hugging Face Transformers

Maintenant, retroussons nos manches et commençons à construire. Nous allons utiliser le pipeline Huggingface pour implémenter notre modèle de synthèse en utilisant [le modèle Bart de Facebook](https://huggingface.co/facebook/bart-large).

Le modèle BART est pré-entraîné en langue anglaise. C'est un modèle séquence-à-séquence et il est idéal pour la génération de texte (comme la synthèse et la traduction). Il fonctionne également bien pour les tâches de compréhension (par exemple, la classification de texte et la réponse aux questions).

[Hugging Face Pipelines](https://huggingface.co/docs/transformers/en/main_classes/pipelines) offre une approche plus simple pour implémenter diverses tâches. Au lieu de préparer un ensemble de données, de l'entraîner avec le modèle et de l'utiliser ensuite, le pipeline simplifie le code car il masque le besoin de tokenisation manuelle et de personnalisation du modèle.

### Comment configurer votre environnement

Tout d'abord, vous devez configurer votre environnement de codage. Je préfère utiliser un notebook Google Collab au lieu de l'installer sur votre machine locale. [Voici le notebook pour ce tutoriel.](https://colab.research.google.com/drive/1Urxh0anruXP6HTbmi5B5TM0UuK3pQHzI?usp=sharing)

Commençons par installer la bibliothèque de transformateurs. Utilisez un ! avant la commande si vous l'exécutez dans un notebook collab :

```
pip install transformers
```

Maintenant, initialisons un pipeline de résumé de texte en utilisant la bibliothèque `transformers` de Hugging Face :

```
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```

Décomposons ce que fait chaque partie :

* `pipeline` : Il s'agit d'une fonction fournie par la bibliothèque `transformers` de Hugging Face pour faciliter l'application de différents types de tâches de traitement du langage naturel (NLP), telles que la classification de texte, la traduction, la synthèse, etc. La fonction retourne un objet pipeline prêt à l'emploi pour la tâche spécifiée.
* `"summarization"` : Il s'agit du premier argument de la fonction `pipeline` et spécifie le type de tâche que vous souhaitez que le pipeline effectue. Dans ce cas, `"summarization"` signifie que le pipeline sera configuré pour résumer le texte.
* `model="facebook/bart-large-cnn"` : Cet argument spécifie le modèle pré-entraîné à utiliser pour la tâche de synthèse. Ici, `"facebook/bart-large-cnn"` fait référence à un modèle spécifique qui a été entraîné sur un grand ensemble de données pour effectuer la synthèse de texte. Ce modèle est fourni par Facebook et est basé sur l'architecture BART (Bidirectional and Auto-Regressive Transformers), qui est efficace pour les tâches nécessitant la compréhension et la génération du langage naturel. La partie `large-cnn` indique que cette variante particulière du modèle est optimisée pour les tâches de synthèse similaires à celles abordées par les résumés de style CNN traditionnels.

Lorsque cette ligne de code est exécutée, elle crée un objet `summarizer`. Cet objet peut ensuite être utilisé pour effectuer la synthèse de texte en lui passant des données textuelles. Le modèle générera une version plus courte du texte d'entrée, capturant les informations les plus importantes ou pertinentes, selon son entraînement sur la tâche de synthèse.

Nous sommes maintenant prêts à utiliser le modèle pour résumer notre texte (oui, vraiment !). Utilisons un [rapport annuel de la FDA](https://www.fda.gov/drugs/generic-drugs/office-generic-drugs-2023-annual-report) et utilisons-le comme entrée pour obtenir notre résumé.

```
text = """In 2023 generic drugs continued to play a critical role in the U.S. health care system allowing patients greater access to needed medicines. Generic drugs are generally lower cost than their brand-name equivalent and the approval of generic drugs often means multiple manufacturers for generic medicines, which can help stabilize the supply chain and reduce drug shortage risks.

The mission of the Office of Generic Drugs is to ensure high-quality, safe, and effective generic medicines are available to the American public. Our 2023 Annual Report provides highlights of activities and accomplishments including generic drug approvals, first generic approvals, science and research innovations for generic medicines – including complex generics, and international collaboration, as well as how we are doing on agreements made under the third iteration of the Generic Drug User Fee Amendments."""
```

Maintenant, utilisons ce texte comme entrée et appelons notre résumé :

```
summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
```

Cette ligne de code utilise l'objet `summarizer` créé à partir d'un `pipeline` de Hugging Face pour générer un résumé du texte d'entrée. Voici une décomposition de l'appel de fonction et de ses paramètres :

* `summarizer` : Il s'agit de l'objet initialisé précédemment avec la fonction `pipeline`.
* `text` : Il s'agit du texte d'entrée que vous souhaitez résumer.
* `max_length=150` : Ce paramètre spécifie la longueur maximale du résumé en termes de nombre de tokens (mots et signes de ponctuation).
* `min_length=40` : De même, ce paramètre définit la longueur minimale du résumé.

Enfin, nous allons imprimer notre résumé :

```
print(summary[0]['summary_text'])
```

Et voici la réponse :

```
In 2023 generic drugs continued to play a critical role in the U.S. health care system allowing patients greater access to needed medicines. Generic drugs are generally lower cost than their brand-name equivalent and the approval of generic drugs often means multiple manufacturers for generic medicines.
```

En bref, ce code :

* charge un pipeline de synthèse pré-configuré pour utiliser le modèle `facebook/bart-large-cnn`.
* alimente le texte au résumé.
* produit un résumé avec des longueurs minimale et maximale spécifiées.

## Conclusion

Construire un résumé de texte avec Hugging Face Transformers ne consiste pas seulement à jouer avec une technologie cool. Il s'agit de tirer parti de la puissance de l'IA pour faciliter un peu notre vie. Que vous soyez étudiant, professionnel ou simplement quelqu'un de curieux à propos du NLP, la capacité à condenser rapidement l'information est inestimable.

Avec Hugging Face Transformers, vous vous tenez sur les épaules de géants, en utilisant certains des modèles de NLP les plus avancés disponibles aujourd'hui. Alors, essayez-le. Qui sait ? Cela pourrait bien changer la façon dont vous traitez le texte pour toujours.

Merci d'avoir lu cet article. Trouvez plus de tutoriels sur l'IA sur [TuringTalks.ai](https://www.turingtalks.ai/).