---
title: Qu'est-ce que la correspondance sémantique ? Comment trouver des mots dans
  un document en utilisant le NLP
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2025-01-09T19:27:37.607Z'
originalURL: https://freecodecamp.org/news/what-is-semantic-matching-find-words-in-a-document-using-nlp
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/Dh7gzpVpdWQ/upload/4e1e504663acda31b980e6fba0c2d661.jpeg
tags:
- name: nlp
  slug: nlp
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Qu'est-ce que la correspondance sémantique ? Comment trouver des mots dans
  un document en utilisant le NLP
seo_desc: 'Have you ever found yourself searching a document for a specific word or
  phrase just to discover that the term you''re looking for isn''t there? It can be
  frustrating, right?

  Sometimes, even though you might not see the exact term you’re looking for, t...'
---

Vous est-il déjà arrivé de rechercher un mot ou une phrase spécifique dans un document pour découvrir que le terme que vous cherchez n'y figure pas ? Cela peut être frustrant, n'est-ce pas ?

Parfois, même si vous ne voyez pas le terme exact que vous cherchez, le document peut contenir des mots ou des phrases similaires qui ont le même sens ou contexte mais qui n'ont pas exactement la même forme (comme des différences d'orthographe).

Les approches traditionnelles de recherche NLP se sont appuyées sur l'utilisation de formes exactes pour rechercher des mots ou des phrases dans un document particulier. Mais cela échoue à trouver des mots basés sur la signification sémantique ou contextuelle.

Pour résoudre ce problème, la correspondance sémantique entre en jeu. C'est une méthode avancée de recherche qui tire parti des méthodes de recherche traditionnelles tout en se concentrant davantage sur la localisation ou la correspondance de mots ou de phrases en fonction de leur sens ou de leur contexte (plutôt que uniquement sur leur forme exacte).

Dans cet article, vous apprendrez à effectuer une correspondance sémantique en utilisant le NLP. Sans plus attendre, commençons.

## Exigences

Pour vous assurer de pouvoir reproduire l'expérience de ce tutoriel, vous aurez besoin de quelques éléments.

Tout d'abord, vous devrez avoir Python 3.x (de préférence Python 3.10) installé sur votre PC. Vous aurez également besoin de certaines bibliothèques, que vous pouvez installer en utilisant le gestionnaire de paquets Pip.

Vous devriez également avoir des connaissances de base en NLP, telles que les techniques de prétraitement de texte et de représentation de texte. Vous pouvez en apprendre davantage [ici](https://www.freecodecamp.org/news/natural-language-processing-techniques-for-beginners/).

Vous pouvez également [forker le dépôt](https://github.com/ibrahim-ogunbiyi/Semantic_Matching) qui contient tout le code de cet article afin de pouvoir suivre.

Pour installer tout cela en utilisant Pip, tapez la commande suivante :

```bash
// pour installer avec pip
pip install pypdf2 keybert sentence-transformers
```

## Définition du problème

Supposons que vous êtes un scientifique des données qui fait partie d'une équipe de développement de programmes scolaires et que vous souhaitez savoir si un concept particulier (mot ou phrase), disons **birth control**, est enseigné dans un programme scolaire qui se trouve dans un document PDF.

Une façon de faire cela est d'ouvrir le PDF en utilisant un outil PDF et ensuite d'utiliser la méthode ctrl + f (rechercher) pour vérifier si la phrase "birth control" est dans le PDF.

![Le PDF avec lequel nous travaillons ici](https://cdn.hashnode.com/res/hashnode/image/upload/v1736408224052/2e6dacef-ef92-4113-a574-ec355e99e6f6.png align="center")

Vous pourriez également le faire de manière programmatique, comme montré ci-dessous :

```python
# importation de la bibliothèque
import PyPDF2

# utilisation de PDFreader de PyPDF2 pour lire le contenu du PDF.
pdf_reader = PyPDF2.PdfReader("Relationships_Education_RSE_and_Health_Education.pdf")

# joindre tout le contenu des pages du PDF ensemble et mettre les lettres en minuscules
pdf_document = " ".join([page.extract_text().lower() for page in pdf_reader.pages])

# vérifier si la chaîne 'birth control' est dans le document [Retourne False]
"birth control" in pdf_document
```

Voici le résultat du code ci-dessus :

```python
False
```

Comme montré ci-dessus, vous pouvez voir que la méthode programmatique de recherche et l'outil PDF indiquent que la phrase "birth control" n'existe pas dans le document PDF.

Cela peut être vrai, mais comme il s'agit d'une méthode traditionnelle de recherche NLP (qui correspond mot à mot sous forme exacte), ne nous y fions pas entièrement. Comme je l'ai expliqué précédemment, certains mots peuvent être sous différentes formes ou avoir une orthographe différente, mais ils peuvent signifier la même chose contextuellement ou sémantiquement.

Alors, comment résoudre ce problème ? C'est là que la correspondance sémantique entre en jeu.

## Qu'est-ce que la correspondance sémantique ?

La correspondance sémantique est une technique utilisée pour déterminer si deux éléments ont le même sens. Un élément peut être un mot, une phrase, une sentence, un document, ou même un corpus. Elle fait référence à la correspondance d'éléments basée sur le sens ou le contexte et pas seulement sur la correspondance basée sur la forme exacte.

Pour effectuer une correspondance sémantique en NLP, il y a certaines choses que vous devez savoir et faire. Passons-les en revue maintenant :

### Qu'est-ce que l'intégration de mots ?

L'intégration de mots est une technique avancée de représentation de texte utilisée pour représenter les mots dans une représentation vectorielle de dimension inférieure. Cette représentation vectorielle capture les informations sémantiques et syntaxiques inter-mots. Cela signifie que les mots qui ont des significations similaires – même s'ils peuvent être orthographiés différemment – auront des représentations vectorielles presque similaires.

#### Que signifie la représentation vectorielle de dimension inférieure ?

En NLP, les méthodes traditionnelles de représentation de texte de manière compréhensible pour les machines (c'est-à-dire, les représentations vectorielles numériques) sont le sac de mots, la fréquence des termes et la fréquence inverse des documents (TF-IDF), et le codage one-hot. Mais ces techniques génèrent généralement des dimensions élevées (généralement la taille du vocabulaire) pour une représentation particulière de mot et sont clairsemées (ce qui signifie qu'il y aura beaucoup de zéros).

Ainsi, par exemple, si un mot doit être représenté comme un vecteur numérique et que le document ou le corpus auquel appartient le mot contient 10 000 vocabulaires, la taille de la dimension de ce mot serait de 10 000 (ce qui le rend élevé).

Les inconvénients de ces techniques sont les dimensions élevées, la clairsemée et leur incapacité à capturer les informations sémantiques. Ainsi, les avancées en NLP ont conduit au développement de techniques d'intégration de mots qui créent simplement des représentations vectorielles de mots de dimension inférieure (également connues sous le nom de plus denses) et peuvent capturer les informations sémantiques inter-mots.

L'intégration de mots est le Saint-Graal en NLP et en technologie du langage, servant de fondation pour les modèles avancés de représentation du langage tels que GPT (Generative Pre-trained Transformer).

Il existe également l'intégration de phrases qui représente les phrases dans une représentation vectorielle de dimension inférieure.

### Comment mesurer si deux vecteurs sont similaires ?

C'est là que la similarité cosinus entre en jeu. La similarité cosinus est une technique mathématique que nous utilisons pour savoir à quel point deux vecteurs sont similaires l'un à l'autre.

En NLP, elle produit généralement une valeur comprise entre 0 et 1. Une valeur proche de 1 signifie que les deux vecteurs sont très similaires.

Par exemple, pour comprendre comment fonctionne la similarité cosinus, créons une représentation vectorielle d'intégration de mots pour trois mots : Homme, Femme et Chat. Ensuite, nous utiliserons la similarité cosinus pour déterminer quels vecteurs sont similaires.

Selon nos propres instincts, nous savons que Homme devrait être plus proche de Femme que de Chat. Alors, utilisons le NLP pour nous aider à valider cela.

Grâce aux avancées en NLP, il existe de nombreux modèles que nous pouvons utiliser pour créer des intégrations de mots, que vous pouvez trouver sur le dépôt Hugging Face. Dans cet article, nous allons utiliser le modèle `all-mpnet-base-v2` de la bibliothèque `SentenceTransformer`. Selon `SentenceTransformer`, il offre les meilleures performances en termes d'intégration de phrases, et vous pouvez également l'utiliser pour créer des intégrations de mots.

Le code ci-dessous nous permet de valider notre affirmation en utilisant le NLP. Donc, tout d'abord, nous initialisons le `SentenceTransformer` avec `all-mpnet-base-v2` et ensuite nous utilisons la méthode encode pour obtenir l'intégration de chaque mot. Enfin, nous utiliserons la classe `cos_sim`, également de `SentenceTransformer`, pour déterminer quels vecteurs sont similaires.

```python
# importation de la bibliothèque
from sentence_transformers import SentenceTransformer # transformateur de phrases
from sentence_transformers.util import cos_sim # similarité cosinus

# initialisation du transformateur de phrases avec le modèle 'all-mpnet-base-v2'
model = SentenceTransformer("all-mpnet-base-v2")
```

```python
# obtenir le vecteur d'intégration des mots homme, femme et chat.
homme_vector = model.encode("homme")
femme_vector = model.encode("femme")
chat_vector = model.encode("chat")

# obtenir la similarité entre homme et femme
similarity = cos_sim(homme_vector, femme_vector)

# obtenir la similarité entre homme et chat
chat_similarity = cos_sim(homme_vector, chat_vector)

print("La similarité entre le vecteur Homme et le vecteur Femme :", similarity, "\n")

print("La similarité entre le vecteur Homme et le vecteur Chat :", chat_similarity)
```

// Résultat

```plaintext
La similarité entre le vecteur Homme et le vecteur Femme : tensor([[0.3501]]) 

La similarité entre le vecteur Homme et le vecteur Chat : tensor([[0.2553]])
```

Comme vous pouvez le voir, le score de similarité entre homme et femme (0,35) est plus élevé que celui entre homme et chat (0,26). Cela montre la beauté de l'intégration de mots et de la similarité cosinus ensemble.

Maintenant, revenons à notre sujet.

## Comment effectuer une correspondance sémantique sur un document PDF

Maintenant, nous allons utiliser la correspondance sémantique pour rechercher un mot ou une phrase dans le document qui correspond à la phrase **birth control**.

### Comment obtenir des mots du PDF en utilisant KeyBERT

L'intégration de mots génère des intégrations pour des mots individuels. Notre document PDF contient un **grand volume de composants textuels**, y compris des chiffres, des caractères spéciaux, des symboles, des mots vides et les mots réels que nous voulons faire correspondre. Donc, pour gagner du temps sur le prétraitement, nous allons utiliser `KeyBERT`. Il s'agit d'une bibliothèque qui nous permet d'obtenir des mots-clés significatifs (mots ou phrases) à partir d'un document particulier de manière minimale.

Gardez à l'esprit que par défaut, `KeyBERT` extrait des mots-clés uniques – mais nous pouvons également lui dire d'extraire des phrases de deux mots ou plus. Nous allons l'utiliser ici pour extraire des mots uniques et des phrases de deux mots. Voici l'implémentation de l'utilisation de `KeyBERT` pour extraire des mots-clés de notre document :

```python
from keybert import KeyBERT
# initialisation du modèle
keybert_model =  KeyBERT()

# extraction de tous les mots-clés (mot unique et phrase de 2 mots) du PDF
all_keywords = keybert_model.extract_keywords(docs=pdf_document, top_n=-1, keyphrase_ngram_range=(1, 2))
# impression de la longueur des mots-clés extraits
print(len(all_keywords))
# affichage des 5 premiers mots-clés
print(all_keywords[:5])
```

Le code ci-dessus importe `KeyBERT` de la bibliothèque `keybert`. Il initialise ensuite `KeyBERT`, et extrait tous les mots-clés (c'est-à-dire, les mots uniques et les phrases de deux mots) du document. Ensuite, la ligne suivante imprime le nombre de mots-clés extraits. Enfin, le code imprime les cinq premiers mots-clés parmi tous les mots-clés extraits du PDF.

Voici le résultat du code ci-dessus :

```python
8669
[('education guidance', 0.5954),
 ('schools guidance', 0.5542),
 ('education policies', 0.5405),
 ('sex education', 0.5228),
 ('education safeguarding', 0.5001)]
```

Comme vous pouvez le voir ci-dessus, KeyBERT a extrait 8 669 mots-clés du PDF. De plus, le modèle `KeyBERT` retourne généralement les mots-clés extraits avec un score pour chaque mot. Nous n'avons pas besoin du score, donc nous allons extraire uniquement chaque mot-clé du tuple dans lequel il est enfermé.

```python
# suppression du score de chaque mot-clé

all_keywords = [keyword[0] for keyword in all_keywords]
all_keywords[:5]
```

Voici le résultat du code ci-dessus :

```python
['education guidance',
 'schools guidance',
 'education policies',
 'sex education',
 'education safeguarding']
```

### Intégration de la phrase "Birth Control" et des mots-clés extraits du PDF

Maintenant que nous avons extrait ces mots-clés du document, l'étape suivante consiste à obtenir l'intégration de notre phrase et des mots-clés du document.

Le code ci-dessous nous permet de faire cela :

```python
# initialisation du transformateur de phrases avec le modèle 'all-mpnet-base-v2'
model = SentenceTransformer("all-mpnet-base-v2")

# obtenir l'intégration de la phrase 'birth control'
birth_control_embedding = model.encode("birth control")

# obtenir l'intégration de tous les mots-clés dans le document
keywords_embedding =  model.encode(all_keywords)
```

### Similarité cosinus de la phrase "Birth Control" et des mots-clés dans le PDF

Après avoir obtenu l'intégration de la phrase et des mots-clés, l'étape suivante consiste à obtenir le score de similarité de la phrase et des mots-clés. Cela nous aidera à savoir quel mot-clé dans le document est très similaire à la phrase.

Le code ci-dessous nous permet d'obtenir la similarité cosinus de la phrase et des vecteurs d'intégration des mots-clés.

```python
# calculer la similarité cosinus du mot 'birth control' et de chaque mot dans le document
cosine_similarity_result = cos_sim(birth_control_embedding, keywords_embedding)
# imprimer la forme (égale au nombre de mots-clés)
print(cosine_similarity_result.shape)
# montrer les 5 premières similarités
print(cosine_similarity_result[:5])
```

Voici le résultat du code ci-dessus :

```python
torch.Size([1, 2034])
tensor([[0.2166, 0.1977, 0.0998,  ..., 0.1634, 0.1082, 0.2194]])
```

Maintenant que nous avons le score de similarité de la phrase et des mots-clés, la taille totale du tenseur résultant sera le nombre de mots-clés, comme montré ci-dessus. Ensuite, nous pouvons utiliser la méthode `argmax()` pour obtenir l'index de l'élément du tenseur avec le score le plus élevé. Cet index nous aidera à filtrer le mot-clé particulier dans la variable de liste `all_keywords`. Le code ci-dessous réalise cela :

```python
# retourner le numéro d'index du score de similarité élevé
index = cosine_similarity_result.argmax()
print(index)
```

Voici le résultat du code ci-dessus. Il nous indique que le mot-clé avec la plus grande similarité avec la phrase **Birth Control** se trouve à l'index 1490.

```python
tensor(1490)
```

Maintenant, regardons le mot-clé à l'index 1490 dans la variable `all_keywords`.

```python
# imprimer le mot-clé à l'index 1490
print(all_keywords[index])
```

Voici le résultat du code ci-dessus :

```python
contraceptive
```

Après l'avoir examiné, nous avons trouvé que "contraceptive" était le mot avec la plus grande similarité, ce qui est logique car "birth control" et "contraceptive" signifient la même chose. Cela démontre l'élégance de la correspondance sémantique pour trouver des mots similaires.

### Explorons également les 5 meilleurs mots-clés dans le PDF qui correspondent à la phrase "Birth Control"

Explorons les 5 meilleurs mots-clés avec le score de similarité le plus élevé par rapport à "birth control" pour voir à quoi ressemblerait le résultat.

Pour ce faire, nous pouvons utiliser la méthode `topk()` pour obtenir les 5 meilleurs indices. Ensuite, nous pouvons parcourir ces indices pour obtenir les mots-clés réels :

```python
# extraire les 5 meilleurs indices
top_5_indices = cosine_similarity_result.topk(5)[1].tolist()[0]

print(top_5_indices)
```

Voici le résultat du code ci-dessus :

```python
[1490, 1972, 871, 1199, 1944]
```

```python
# obtenir les 5 meilleurs mots-clés
top_5_keywords = [all_keywords[index] for index in top_5_indices]
print(top_5_keywords)
```

Voici le résultat du code ci-dessus :

```python
['contraceptive', 'contraception', 'contraceptive choices', 'range contraceptive', 'cover contraception']
```

Là, nous pouvons voir que les cinq meilleurs résultats concernent la contraception et les contraceptifs. Cela démontre que la correspondance sémantique est un moyen efficace de trouver des éléments liés dans un document.

## Conclusion

Dans cet article, vous avez appris ce qu'est la correspondance sémantique et ses avantages par rapport aux méthodes de recherche NLP traditionnelles. Vous avez également rencontré des concepts tels que les intégrations de mots et la similarité cosinus et appris comment ils nous aident à effectuer une correspondance sémantique. Ensuite, nous avons implémenté la correspondance sémantique en trouvant une phrase dans un document.

Merci d'avoir lu cet article, et je vous retrouverai dans le prochain.

### Références

1. [https://sbert.net/](https://sbert.net/)

2. [https://maartengr.github.io/KeyBERT/guides/quickstart.html](https://maartengr.github.io/KeyBERT/guides/quickstart.html)

3. [https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard)