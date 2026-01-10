---
title: 'Aide-mémoire sur le Prompt Engineering pour GPT-5 : Apprenez ces modèles pour
  une génération de code robuste'
subtitle: ''
author: Tarun Singh
co_authors: []
series: null
date: '2025-09-12T10:30:29.597Z'
originalURL: https://freecodecamp.org/news/prompt-engineering-cheat-sheet-for-gpt-5
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757672756195/67ddcb24-b8dd-4bf6-a83b-103940f4ae85.png
tags:
- name: Prompt Engineering
  slug: prompt-engineering
- name: openai
  slug: openai
- name: llm
  slug: llm
seo_title: 'Aide-mémoire sur le Prompt Engineering pour GPT-5 : Apprenez ces modèles
  pour une génération de code robuste'
seo_desc: When large language models like ChatGPT first became widely available, a
  lot of us developers felt like we’d been handed a new superpower. We could use LLMs
  to help us develop new coding projects, build websites, and much more – just using
  a few prom...
---

Lorsque les grands modèles de langage (LLM) comme ChatGPT sont devenus largement accessibles, beaucoup d'entre nous, développeurs, avons eu l'impression de recevoir un nouveau super-pouvoir. Nous pouvions utiliser les LLM pour nous aider à développer de nouveaux projets de codage, créer des sites web, et bien plus encore – simplement en utilisant quelques prompts.

Les LLM étaient comme un binôme de programmation infatigable et extrêmement instruit capable de faire apparaître du code à partir de rien. Nous tapions une requête rapide et brouillonne, et il en sortait quelque chose qui... fonctionnait à peu près. C'était incroyable, mais aussi un peu frustrant. Le code pouvait être buggé, inefficace ou passer complètement à côté du contexte subtil de notre projet.

Mais avec [**GPT-5**](https://platform.openai.com/docs/models/gpt-5), la donne a passablement changé. Ce modèle ne se contente pas de recracher du code – il raisonne, s'adapte et comprend le contexte comme jamais auparavant. Pourtant, il y a un hic : vous devez parler sa langue pour obtenir le meilleur résultat. Mais comment ? C'est là que le **prompt engineering** entre en jeu.

Dans cet article, je partagerai 10 modèles (patterns) éprouvés qui vous aideront à transformer GPT-5 d'un outil utile en un partenaire de codage solide comme un roc, auquel vous pourrez faire confiance pour la précision et la rapidité. Commençons !

## Table des matières

1. [Qu'est-ce que GPT-5 ? Pourquoi devriez-vous l'utiliser en tant que développeur ?](#heading-qu-est-ce-que-gpt-5-pourquoi-devriez-vous-l-utiliser-en-tant-que-developpeur)
    
2. [Pourquoi le Prompt Engineering ?](#heading-pourquoi-le-prompt-engineering)
    
3. [Comment utiliser GPT-5 gratuitement ?](#heading-comment-utiliser-gpt-5-gratuitement)
    
4. [Modèles que chaque développeur devrait connaître](#heading-modeles-que-chaque-developpeur-devrait-connaitre)
    
    * [Modèle Persona](#heading-modele-persona)
        
    * [Modèle Few-Shot](#heading-modele-few-shot)
        
    * [Modèle Chain-of-Thought](#heading-modele-chain-of-thought)
        
    * [Modèle Délimiteur](#heading-modele-delimiteur)
        
    * [Modèle de Sortie Structurée](#heading-modele-de-sortie-structuree)
        
    * [Modèle d'Interaction Inversée](#heading-modele-d-interaction-inversee)
        
    * [Modèle de Contrainte Négative](#heading-modele-de-contrainte-negative)
        
    * [Modèle d'Utilisation d'Outils](#heading-modele-d-utilisation-d-outils)
        
    * [Modèle de Verbosité](#heading-modele-de-verbosite)
        
    * [Modèle Le-Code-comme-Contexte](#heading-modele-le-code-comme-contexte)
        
5. [Pièges courants à éviter](#heading-pieges-courants-a-eviter)
    
6. [Dernières réflexions](#heading-dernieres-reflexions)
    

## Qu'est-ce que GPT-5 ? Pourquoi devriez-vous l'utiliser en tant que développeur ?

OpenAI a récemment lancé l'un de ses meilleurs modèles, GPT-5. Il est capable d'exécuter des tâches de codage et des tâches agentiques dans divers domaines. Considérez-le comme un stagiaire full-stack super-intelligent à qui l'on a confié une clé maîtresse de la connaissance d'Internet. Il n'est pas seulement meilleur pour écrire du code, il peut comprendre *pourquoi* vous avez besoin du code, comment il doit s'intégrer dans un système plus large et comment le déboguer.

Il excelle dans :

* **Le raisonnement à long contexte :** Il peut gérer une base de code entière ou une longue documentation d'API, ce qui change la donne pour le refactoring ou la correction de bugs sur plusieurs fichiers.
    
* **Le suivi d'instructions :** Il est beaucoup moins susceptible de s'embrouiller face à une longue liste de contraintes ou un ensemble détaillé d'étapes.
    
* **L'utilisation d'outils et les tâches agentiques :** Il peut décider intelligemment d'appeler une API externe, d'exécuter une commande shell ou de fouiller dans un dépôt pour accomplir une tâche.
    

## Pourquoi le Prompt Engineering ?

Considérez les LLM comme des développeurs juniors : super intelligents, mais littéraux. La façon dont vous formulez votre requête modifie radicalement le résultat. Le prompt engineering est l'art et la science de concevoir des instructions efficaces pour qu'un LLM atteigne un objectif spécifique. C'est la méthode que vous utilisez pour communiquer votre intention, fournir le contexte nécessaire et structurer votre demande de manière à ce que le modèle puisse la comprendre et y répondre le plus précisément possible. Lorsque vous le maîtrisez, vous pouvez :

* Faire en sorte que GPT-5 génère du code fonctionnel et testable.
    
* Éviter les réponses vagues ou non pertinentes.
    
* Économiser des tokens (et de l'argent).
    
* Réduire le temps passé à éditer ou déboguer les sorties.
    

## Comment utiliser GPT-5 gratuitement

Bien que l'API de GPT-5 soit un service **payant**, de nombreux développeurs peuvent accéder à sa puissance gratuitement ou à faible coût. Actuellement, par exemple, la version publique par défaut de ChatGPT utilise souvent la version de GPT-5 avec certains plafonds d'utilisation. De nombreux outils comme **Cursor, GitHub Copilot, Microsoft Copilot** intègrent GPT-5 ou des variantes plus légères.

Consultez la capture d'écran ci-dessous de l'IDE Cursor avec l'intégration de divers modèles, dont `gpt-5-fast`, `gpt-5-low`, et ainsi de suite. Si vous expérimentez, c'est le moyen le plus simple d'explorer GPT-5 sans payer pour des appels d'API directs.

![Capture d'écran des paramètres de l'IDE Cursor, montrant diverses options de modèles GPT-5](https://cdn.hashnode.com/res/hashnode/image/upload/v1757253133347/525d9160-fce7-4310-a85e-7e7dcd9d929d.png align="center")

Pour cet article, nous utiliserons une structure d'appel d'API standard, mais ces mêmes principes s'appliquent que vous utilisiez une interface web ou un outil intégré. Plongeons dans les modèles.

## Modèles que chaque développeur devrait connaître

### Modèle Persona

Vous savez comment, lors d'un entretien avec un candidat, vous pourriez lui demander d'agir comme s'il était un « Responsable technique ou Manager » ou un « Ingénieur Frontend » ? Ce modèle repose sur la même idée. En attribuant un rôle au modèle, vous lui donnez un ensemble immédiat de présupposés et un filtre de connaissances.

Pour créer un persona efficace, soyez spécifique. Par exemple, au lieu de dire « Tu es un développeur », essayez « Tu es un développeur JavaScript senior spécialisé dans les API backend et la scalabilité ». Cela fournit un contexte sur son niveau de compétence, son domaine et son langage de programmation préféré, guidant le LLM vers une réponse plus personnalisée et de niveau expert.

**Exemple :**

```python
# Exemple Python
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="""Tu es un développeur JavaScript senior.
    Refactorise ce code pour la lisibilité :
    numbers = [8, 9, 10, 11, 12]; total=0
    for i in numbers: total+=i
    print(total)"""
)

print(response.output_text)
```

Ce code garantit que les réponses correspondent au ton et à l'expertise que vous attendez, comme spécifié dans le prompt.

### Modèle Few-Shot

Parfois, la meilleure façon d'obtenir un style ou un format de code spécifique est de fournir un exemple. C'est ce qu'on appelle le prompt « few-shot ». Au lieu de simplement décrire ce que vous voulez, vous montrez au modèle quelques exemples terminés.

**Exemple :**

```python
from openai import OpenAI

client = OpenAI()

prompt = """
Convertis les fonctions en syntaxe fléchée :

Exemple :
function sum(x, y) { return x + y; }
=> const sum = (x, y) => x + y;

Puis convertis :
function greet(name) { return "Hey, " + name; }
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print(response.output_text)
```

Cet exemple de code fournit un modèle concret et incontestable que le modèle doit suivre, ce qui est beaucoup plus efficace qu'une description verbeuse.

### Modèle Chain-of-Thought

Face à un problème complexe, les humains ne sautent pas directement à une solution ; ils réfléchissent par étapes. Le modèle Chain-of-Thought (Chaîne de pensée) demande au LLM de faire de même. En disant au modèle de « réfléchir étape par étape », vous ne demandez pas seulement une réponse finale, mais vous l'instruisez d'effectuer un raisonnement interne et de décomposer le problème en parties logiques plus petites. Ce processus est ce qui vous donne de la marge pour déboguer.

Si le résultat final est incorrect, vous pouvez examiner son processus de réflexion pour identifier où la logique a échoué. C'est particulièrement efficace avec les capacités de raisonnement améliorées de GPT-5. Le raisonnement du LLM peut ressembler à un monologue interne intermédiaire que vous ne voyez pas toujours, mais lui demander d'afficher son processus de réflexion peut le rendre explicite.

**Exemple :**

```python
prompt = """
Débogue ce qui suit étape par étape :
La boucle de ma fonction Python saute le dernier élément de la liste. Vérifie pourquoi ?
"""
```

En encourageant le raisonnement, vous réduisez les erreurs dans le code.

### Modèle Délimiteur

Lorsque vous donnez des instructions au LLM, il est important de lui donner un moyen clair de différencier vos instructions des données que vous voulez qu'il traite. Pour ce faire, vous pouvez utiliser des délimiteurs comme `###`, `"""`, ou `<>` autour de votre texte d'entrée pour créer une limite nette. C'est une bonne pratique générale pour tous les LLM, car ils peuvent tous avoir du mal avec cette distinction sans signal clair.

**Exemple :**

```python
prompt = """
Explique ce code en anglais simple et facile :

###
for i in range(10):
    print(i**3)
###
"""
```

Cela aide à empêcher le modèle de mal interpréter vos données comme faisant partie des instructions, en particulier lorsque les données contiennent des chaînes ressemblant à des instructions.

### Modèle de Sortie Structurée

Si vous avez besoin que la réponse du modèle soit facilement analysable par un programme, vous devez spécifier le format clairement. C'est particulièrement important lorsque vous voulez utiliser la sortie comme entrée pour une autre partie de votre logiciel, comme la génération de fichiers de configuration JSON, de XML pour des services web, ou même de fichiers markdown (MD) pour la documentation. En disant au modèle de respecter une structure rigide, vous garantissez que la sortie est cohérente et fiable.

**Exemple :**

```python
import json
from openai import OpenAI

client = OpenAI()

def generate_product_list(product_info):
    prompt = f"""
    Génère un objet JSON pour les informations produit suivantes.
    Le JSON doit avoir une clé 'products', qui est un tableau d'objets.
    Chaque objet doit avoir des clés pour 'name', 'category', 'price', et 'in_stock' (un booléen).

    Informations Produit :
    {product_info}

    Fournis uniquement la sortie JSON, et rien d'autre.
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    # Tentative d'analyse de la réponse en tant que JSON
    try:
        json_output = json.loads(response.output_text)
        return json_output
    except json.JSONDecodeError as e:
        print(f"Erreur lors de l'analyse du JSON : {e}")
        return None

# Essayons
product_data = """
Laptop Pro, Electronics, 1500, True
Ergo Mouse, Accessories, 50, True
Wireless Keyboard, Accessories, 90, False
"""

product_list = generate_product_list(product_data)
if product_list:
    print(json.dumps(product_list, indent=2))
```

Dans cet exemple, le `prompt` est l'instruction que vous donnez au LLM. C'est une chaîne de texte qui définit une tâche claire et spécifie le format de sortie (un objet JSON avec des clés spécifiques). La `response` du modèle est le texte brut qu'il génère, qui devrait être l'objet JSON demandé. Le code Python tente ensuite d'analyser cette réponse textuelle brute en un objet JSON structuré à l'aide de `json.loads()`.

### Modèle d'Interaction Inversée

Parfois, la meilleure façon d'obtenir l'aide de GPT-5 est de lui demander de vous poser des questions avant qu'il n'écrive le moindre code.

**Exemple :**

```python
prompt = """
Je veux un script python pour scraper des sites de voyage afin d'obtenir des données de voyage.
Pose-moi 5 questions de clarification avant d'écrire le code.
"""
```

Ce type de prompt aide à éviter les suppositions et fournira un code plus précis.

### Modèle de Contrainte Négative

S'il est important de dire au modèle ce qu'il **doit faire**, il est aussi parfois tout aussi important de lui dire ce qu'il **ne doit pas faire** ou ce qu'il ne doit pas inclure dans sa réponse. Cela aide le modèle à éviter certains mots, tons ou sujets.

**Exemple :**

```python
from openai import OpenAI

client = OpenAI()

def my_func(technical_report):
    prompt = f"""
    Résume le rapport technique suivant pour un public non technique.
    N'utilise aucun jargon spécialisé, acronyme ou terme complexe.
    Utilise un langage simple et quotidien.

    Rapport Technique :
    \"{technical_report}\"
    """
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text

# Essayons
report = (
    "Le protocole d'intrication quantique (QEP) a montré des améliorations significatives "
    "de la cohérence des qubits en utilisant une nouvelle cascade d'émission multi-photons. "
    "Les données indiquent une réduction de 12 % des taux de décohérence, validant "
    "l'hypothèse selon laquelle une rétroaction optique non linéaire pourrait atténuer le bruit environnemental."
)

summary = my_func(report)
print(summary)
```

Ce modèle est un excellent moyen d'affiner la sortie et de l'éloigner des pièges courants, d'un langage trop technique, etc., garantissant ainsi qu'elle répond à vos exigences spécifiques.

### Modèle d'Utilisation d'Outils

GPT-5 est un moteur de raisonnement incroyable, mais sa véritable puissance se révèle lorsqu'il peut interagir avec des outils externes, comme une recherche web, un interpréteur de code ou un système de récupération de fichiers. Ce modèle consiste à fournir au modèle une description claire des outils qu'il peut ou doit utiliser.

**Exemple :**

```python
prompt = """
Tu as accès à un outil 'code_interpreter'.
Son but est d'exécuter du code JavaScript dans un bac à sable (sandbox) sécurisé.
L'outil prend un seul argument : le code JavaScript sous forme de chaîne.

Ta tâche est d'utiliser cet outil pour calculer l'aire d'un rectangle
avec une longueur et une largeur de 15.
Une fois le résultat obtenu, réponds uniquement avec le chiffre de la réponse finale.
"""
```

C'est ce qui libère le potentiel de GPT-5 pour un véritable comportement agentique. Il peut résoudre un problème de manière autonome en décidant quels outils utiliser et dans quel ordre, allant au-delà de la simple génération de texte.

### Modèle de Verbosité

Selon vos besoins, vous pourriez vouloir une sortie plus ou moins concise de la part du LLM. Avec l'API GPT-5, vous pouvez ajuster le niveau de détail et la longueur de la sortie à l'aide du nouveau paramètre `text.verbosity`. Sélectionnez simplement le niveau de `text.verbosity` parmi `low`, `medium`, ou `high`.

**Exemple :**

```python
from openai import OpenAI

client = OpenAI()

# Verbosité basse pour une fonction concise
def get_concise_code(description):
    prompt = f"Écris une fonction Python pour {description}."
    response = client.responses.create(
        model="gpt-5",
        input=prompt,
        metadata={"verbosity": "low"} 
    )
    return response.output_text

user_input = "un algorithme de quicksort"

concise_code = get_concise_code(user_input)

print("Code Concis-\n", concise_code)
```

Cela vous fait gagner du temps en empêchant le modèle de « trop expliquer » quand vous avez juste besoin d'un extrait rapide, et cela vous donne plus de contexte quand vous apprenez quelque chose de nouveau ou travaillez sur un morceau de code complexe.

### Modèle Le-Code-comme-Contexte

L'immense fenêtre de contexte de GPT-5 change la donne pour travailler avec un fichier complet ou même un petit projet. Au lieu de lui donner seulement un extrait, vous pouvez lui fournir un script entier et lui demander de l'analyser, de le refactoriser ou de l'optimiser.

**Exemple :**

```python
async def my_optimize_codebase(code_file: str) -> str:
    prompt = f"""
    Tu es un expert en optimisation de performance. Analyse le fichier de code JavaScript
    suivant pour détecter d'éventuels goulots d'étranglement, du code redondant ou des fuites de mémoire.
    Fournis un rapport détaillé puis une version refactorisée du code.

    Code à analyser :
    \"\"\"
    {code_file}
    \"\"\"
    """
    # Pour cette démonstration, nous retournerons simplement le prompt
    return prompt


# Entrée utilisateur : "votre code ici"
my_code = """
// Un grand fichier JavaScript non optimisé
const fetchData = async () => {
  const data = await fetch('https://api.example.com/data');
  const jsonData = await data.json();
  const filteredData = jsonData.filter(item => item.isActive);
  const mappedData = filteredData.map(item => {
    return {
      id: item.id,
      name: item.name.toUpperCase(),
      status: 'active'
    };
  });
  
  // C'est une boucle qui pourrait être plus efficace
  const res= [];
  for (let i = 0; i < mappedData.length; i++) {
    for (let j = 0; j < 10000; j++) {
      res.append(mappedData[i])
    }
  }
  return res;
};
"""

import asyncio

async def main():
    prompt = await my_optimize_codebase(my_code)
    print(prompt)

asyncio.run(main())
```

Ce prompt permet à GPT-5 de voir l'image globale. Il peut comprendre la portée des variables, les dépendances des fonctions et la logique d'ensemble d'un fichier d'une manière impossible avec un seul extrait isolé.

## Pièges courants à éviter

* **Être vague ou ambigu :** Un prompt tel que « Écris du code » entraînera une réponse manquant de précision et générique. Assurez-vous de clarifier le langage de programmation, la fonction spécifique, le format de sortie et toute limitation requise.
    
* **Surcharger un seul prompt :** Un exemple tel que « Écris un script Python, résume-le en trois points, puis traduis-le en français » comporte plusieurs tâches sans rapport et générera souvent des rapports désorganisés ou incomplets. Concentrez-vous sur les demandes complexes et décomposez-les en une série de prompts.
    
* **Ne pas itérer :** Généralement, votre premier prompt est rarement le plus précis ou le plus pertinent par rapport au sujet de discussion. Une approche générale consiste à se concentrer sur les prompts générés et à revenir sur les points soulevés dans la réponse. Prenez en compte l'élaboration, l'incorporation de plus de faits et l'affinage, ayez donc une conversation d'avant en arrière pour obtenir le résultat souhaité.
    

## Dernières réflexions

Avec GPT-5, le prompt engineering est bien plus complexe que de trouver une phrase « magique ». Vous devez orienter votre réflexion vers le génie logiciel et l'articuler pour l'IA. Vous ne donnez pas simplement des instructions à l'IA – vous définissez les paramètres dans lesquels elle doit travailler pour arriver à une solution efficace.

Vous pouvez mettre en œuvre ces 10 modèles, ainsi que les nouvelles fonctionnalités d'effort de raisonnement et de contrôle de la verbosité, pour faire de GPT-5 un assistant de codage fiable : génération de code boilerplate, débogage, refactoring de code ou échafaudage d'applications (scaffolding). Commencez à améliorer votre technique de prompt engineering avec des modèles inférieurs comme GPT-4o, Gemini et d'autres. Une fois prêt, passez à GPT-5 pour alimenter des flux de travail de développement réels.

Si vous avez trouvé cet article utile et souhaitez discuter du développement de l'IA, des LLM ou du développement logiciel, n'hésitez pas à me contacter sur [X/Twitter](https://x.com/itsTarun24), [LinkedIn](https://www.linkedin.com/in/tarunsingh24), ou à consulter mon portfolio sur mon [Blog](http://tarunportfolio.vercel.app/blog). Je partage régulièrement des réflexions sur l'IA, le développement, la rédaction technique, etc., et j'aimerais beaucoup voir ce que vous construisez avec ces bases.