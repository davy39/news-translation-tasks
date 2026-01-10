---
title: Les grands modèles de langage et la cybersécurité – Ce que vous devez savoir
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2023-04-25T01:03:55.000Z'
originalURL: https://freecodecamp.org/news/large-language-models-and-cybersecurity
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/image-228-2.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: cybersecurity
  slug: cybersecurity
seo_title: Les grands modèles de langage et la cybersécurité – Ce que vous devez savoir
seo_desc: 'ChatGPT has had well over a billion visits since its release. Now, what
  happens when you combine the greatest language learning model of the decade with
  malicious hacking...what could go wrong? 💀

  In this article, we''ll explore what artificial intell...'
---

ChatGPT a enregistré bien plus d'un milliard de visites depuis sa sortie. Maintenant, que se passe-t-il lorsque vous combinez le plus grand modèle d'apprentissage linguistique de la décennie avec le piratage malveillant... que pourrait-il mal se passer ? 🚀

Dans cet article, nous explorerons ce qu'est l'intelligence artificielle, son état actuel, comment les grands modèles de langage comme ChatGPT fonctionnent, le rôle de l'IA dans la cybersécurité, et plus encore.

Avertissement : Cet article peut devenir obsolète assez rapidement, car la recherche en IA est en constante évolution et est l'un des domaines les plus rapides en développement actuellement. Mais vous y trouverez toujours des leçons clés. 

De plus, n'essayez pas d'entreprendre des activités illégales avec ces connaissances – ceci est à des fins éducatives uniquement afin que vous puissiez apprendre à vous protéger, vous et vos projets. Merci.

## Ce que nous allons couvrir :

1. Qu'est-ce que l'IA ?
2. Le pirate informatique IA
3. Qu'est-ce qu'un grand modèle de langage ?
4. Caractéristiques des LLMs
5. Inconvénients des LLMs
6. Avantages des LLMs en cybersécurité
7. Dangers des LLMs en cybersécurité

## Qu'est-ce que l'IA ?

![IA § Crédit : Tara Winstead](https://www.freecodecamp.org/news/content/images/2023/04/image-229.png)
_IA § Crédit : Tara Winstead_

L'intelligence artificielle fait référence à la capacité des ordinateurs à effectuer des tâches qui nécessitent généralement un intellect de niveau humain. L'IA est utile dans de nombreux contextes, de l'automatisation à la résolution de problèmes et simplement essayer de comprendre comment les humains pensent. 

Mais il est important de noter que l'IA ne se préoccupe pour l'instant que de l'intelligence humaine – elle pourrait éventuellement aller au-delà.

Beaucoup de gens associent le mot « Intelligence » uniquement à l'« Intelligence Humaine ». Le fait qu'un poulet ne puisse pas résoudre une équation mathématique ne signifie pas qu'il ne s'enfuira pas lorsque vous le poursuivrez. Il est « intelligent » suffisamment pour savoir qu'il ne veut pas que vous l'attrapiez 🐔🍗. 

L'intelligence couvre un spectre beaucoup plus large et s'étend pratiquement à tout être vivant capable de prendre des décisions ou d'effectuer des actions de manière autonome, même les plantes.

Il existe deux grandes divisions de l'IA :

### Intelligence Artificielle Étroite (ANI) 

Celle-ci se concentre sur un petit ensemble de tâches similaires ou une petite tâche programmée pour une seule chose. L'ANI n'est pas performante dans des environnements dynamiques et complexes et est utilisée uniquement dans des domaines spécifiques. Les exemples incluent les voitures autonomes, ainsi que les systèmes de reconnaissance faciale et vocale.

### Intelligence Artificielle Générale (AGI)

Celle-ci se concentre sur un large éventail de tâches et d'activités humaines. L'AGI est actuellement théorique et est proposée pour s'adapter et effectuer la plupart des tâches dans de nombreux environnements dynamiques et complexes. Les exemples incluent J.A.R.V.I.S de Marvel's _Iron Man_ et Ava de _Ex-Machina_.

L'intelligence artificielle est centrée sur les ordinateurs et leur capacité à imiter les actions et les processus de pensée humains. 

La programmation et les expériences ont permis aux humains de produire des systèmes ANI. Ceux-ci peuvent faire des choses comme classer des éléments, trier de grandes quantités de données, rechercher des tendances dans des graphiques, déboguer du code, et représenter et exprimer des connaissances. Mais les ordinateurs ne pensent pas comme les humains, ils imitent simplement les humains.

Cela est évident dans les assistants vocaux tels que l'Assistant de Google, Siri d'Apple, Alexa d'Amazon et Cortana de Microsoft. Ce sont des programmes ANI basiques qui ajoutent « la touche humaine ». En fait, les gens sont connus pour être polis avec ces systèmes simplement parce qu'ils combinent des capacités informatisées avec une sensation humaine. 

Ces assistants se sont améliorés au fil des ans mais ne parviennent pas à atteindre des niveaux élevés de sophistication par rapport à leurs homologues AGI.

## Le pirate informatique IA

![IA dans le monde réel § Crédit : Wallpaperflare.com](https://www.freecodecamp.org/news/content/images/2023/04/image-230.png)
_IA dans le monde réel § Crédit : [Wallpaperflare.com](wallpaperflare.com)_

L'intelligence artificielle est très efficace pour trouver des vulnérabilités, et avec l'aide des humains, elle peut les exploiter encore mieux. 

En informatique, les débogueurs utilisent des logiciels d'IA pour rechercher des bugs dans le code source, l'autocomplétion, l'autocorrection et les logiciels de reconnaissance d'écriture. 

Mais cela peut être poussé un peu plus loin. L'IA peut également trouver des vulnérabilités dans les systèmes financiers, juridiques et même politiques. L'IA est utilisée pour rechercher des lacunes dans les contrats, des ensembles de données sur les personnes et améliorer les lacunes littéraires. 

Cela pose deux problèmes :

Premièrement, l'IA peut être **créée pour pirater** un système. Maintenant, cela peut être bon ou mauvais selon la manière dont les gens l'utilisent. 

Un cybercriminel peut créer un chatbot avancé pour obtenir des informations auprès d'un large éventail de personnes sur diverses plateformes et peut-être même dans différentes langues. D'autre part, les entreprises peuvent également utiliser l'IA pour rechercher les vulnérabilités qu'elles ont et les corriger afin qu'un attaquant ne puisse pas les exploiter.

Deuxièmement, il est possible que l'IA **pirate involontairement** le système. Les ordinateurs ont une logique très différente de celle des humains. Cela signifie que presque tout le temps, ils acceptent les données, les traitent et produisent une sortie de manière complètement différente par rapport aux humains. 

Prenons l'exemple du jeu d'échecs classique : Les échecs sont un jeu de stratégie abstrait qui se joue sur un plateau de 64 cases disposées en une grille de 8x8. Au début, chaque joueur contrôle seize pièces. Le but est de faire échec et mat au roi de l'adversaire avec la condition que le roi est en échec et qu'il n'y a pas d'échappatoire.

Un humain et un moteur d'échecs classique regardent ce jeu de deux manières très différentes. Un humain peut jouer le jeu de la valeur (mesurer la victoire par la valeur et le nombre de pièces sur le plateau), tandis qu'un ordinateur examine un nombre fini de possibilités qui peuvent survenir avec chaque coup de l'adversaire via un algorithme de recherche.

En ayant cette capacité limitée à voir dans le futur, l'ordinateur a l'avantage presque à chaque fois pour gagner la partie. C'est un exemple très préliminaire et assez basique par rapport aux autres systèmes qui peuvent être « piratés » par l'intelligence artificielle.

En tant qu'humains, nous sommes programmés par des connaissances implicites et explicites. Les ordinateurs, en revanche, sont programmés par un ensemble d'instructions et de logique qui ne changent jamais sauf si on leur dit de le faire. Par conséquent, les ordinateurs et les humains auront des approches, des solutions et des piratages différents pour le même problème. 

Mais les systèmes sont construits autour des humains et non des ordinateurs. Donc, lorsque les choses se compliquent, les ordinateurs peuvent faire beaucoup plus de recherche de vulnérabilités et d'exploitation sur de nombreux systèmes, à la fois virtuels et physiques.

## Qu'est-ce qu'un grand modèle de langage ?

![IA dans le monde réel § Crédit : Wallpaperflare.com](https://www.freecodecamp.org/news/content/images/2023/04/image-231.png)
_IA dans le monde réel § Crédit : [Wallpaperflare.com](wallpaperflare.com)_

Un grand modèle de langage (LLM) est un modèle d'apprentissage profond qui consiste en un réseau de neurones avec des milliards de paramètres, formé sur des quantités distinctement grandes de données non étiquetées en utilisant l'apprentissage auto-supervisé. C'est un peu compliqué, alors décomposons cela.

Au cœur de toutes les IA se trouvent des algorithmes. Les algorithmes sont des procédures ou des étapes pour effectuer une tâche spécifique. Plus l'algorithme est complexe, plus les tâches peuvent être effectuées et plus il peut être appliqué largement. L'objectif des développeurs d'IA est de trouver les algorithmes les plus complexes qui peuvent résoudre et effectuer un large éventail de tâches.

Examinons la procédure pour créer un modèle de reconnaissance de fruits de base en utilisant une analogie simple :

1. Il y a deux personnes : un enseignant et un créateur de bots
2. Le créateur de bots crée des bots aléatoires, et l'enseignant les enseigne et les teste sur l'identification de certains fruits
3. Le bot avec le score de test le plus élevé est ensuite renvoyé au créateur comme base pour créer de nouveaux bots améliorés
4. Ces nouveaux bots améliorés sont renvoyés à l'enseignant pour l'enseignement et les tests, et celui avec le score de test le plus élevé est renvoyé au créateur de bots pour créer de nouveaux bots meilleurs.

C'est une simplification excessive du processus, mais néanmoins, cela transmet le concept. Le Modèle/Algorithme/Bot est continuellement formé, testé et modifié jusqu'à ce qu'il soit jugé satisfaisant. Plus de données et une complexité plus élevée signifient plus de temps de formation requis et plus de modifications possibles.

En prenant un indice de l'analogie, vous observeriez également que le développeur du modèle peut ajuster quelques choses sur le modèle mais ne sait peut-être pas comment ces ajustements pourraient affecter les résultats. Un exemple courant de cela sont les réseaux de neurones, qui ont des couches cachées dont les couches les plus profondes et les fonctionnements même le créateur ne comprend peut-être pas pleinement.

L'apprentissage auto-supervisé signifie que plutôt que l'enseignant et le créateur de bots soient deux personnes séparées, c'est une personne hautement qualifiée qui peut à la fois créer des bots et les enseigner. Cela rend le processus beaucoup plus rapide et pratiquement autonome. 

Le résultat est un bot ou un ensemble de bots qui sont à la fois sophistiqués et complexes suffisamment pour reconnaître des fruits dans des environnements dynamiques et différents.

Dans le cas des LLMs, les données ici sont des textes humains, et éventuellement dans diverses langues. La raison pour laquelle les données sont grandes est que les LLMs absorbent d'énormes quantités de données textuelles dans le but de trouver des connexions et des motifs entre les mots pour en déduire le contexte, la signification, les réponses probables et les actions à ces textes.

Les résultats sont des modèles qui semblent comprendre le langage et effectuer des tâches basées sur les prompts qui leur sont donnés. 

**ChatGPT** a été la plus grande réalisation dans ce domaine car il a atteint 100 millions d'utilisateurs actifs en 2 mois à partir du jour de sa sortie. Mais il existe de nombreux autres modèles, et ils incluent :

1. GPT-4 par OpenAI 🔥
2. LLaMA par Meta 🧠
3. AlexaTM par Amazon 🎯
4. Minerva par Google ❌➕

Examinons ce que ces modèles ont à offrir.

## Caractéristiques des LLMs

![Logique et Créativité § Crédit : Wallpaperflare.com](https://www.freecodecamp.org/news/content/images/2023/04/image-232.png)
_Logique et Créativité § Crédit : [Wallpaperflare.com](http://Wallpaperflare.com)_

### Traduction

Les LLMs qui sont formés sur un ensemble de langues plutôt que sur une seule peuvent être utilisés pour la traduction d'une langue à une autre. Il est même théorisé que des LLMs suffisamment grands peuvent trouver des motifs et des connexions dans d'autres langues pour en déduire la signification de langues inconnues et perdues, malgré le fait de ne pas savoir ce que chaque mot individuel peut signifier.

### Automatisation des tâches routinières

L'automatisation des tâches a toujours été un objectif majeur du développement de l'IA. Les modèles de langage ont toujours été capables d'effectuer une analyse syntaxique, de trouver des motifs dans le texte et de répondre de manière appropriée. 

Les grands modèles de langage, en revanche, ont un avantage avec l'analyse sémantique, permettant au modèle de comprendre le sens sous-jacent et le contexte, lui donnant un niveau de précision plus élevé. 

Cela peut être appliqué à un certain nombre de tâches de base comme la synthèse de texte, la reformulation de texte et la génération de texte.

### Capacités émergentes

Les capacités émergentes sont des capacités inattendues mais impressionnantes que les LLMs possèdent en raison de la grande quantité de données sur lesquelles ils sont formés. 

Ces comportements sont généralement découverts lorsque le modèle est utilisé plutôt que lorsqu'il est programmé. Les exemples incluent l'arithmétique multi-étapes, la réussite d'examens de niveau universitaire et l'incitation à la chaîne de pensée.

## Inconvénients des LLMs

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-233.png)
_Une ville numérique § Crédit : [Wallpaperflare.com](http://Wallpaperflare.com)_

### Hallucination

Un résultat infâme de Sydney de Microsoft a été des cas où l'IA a donné des réponses qui étaient soit bizarres, fausses, ou semblaient douées de conscience. Ces cas sont appelés Hallucination, où le modèle donne des réponses ou fait des affirmations qui ne sont pas basées sur ses données de formation.

### Biais

Parfois, les données pourraient être la source du problème. Si un modèle est formé sur des données qui sont discriminatoires envers une personne, un groupe, une race ou une classe, les résultats tendraient également à être discriminatoires. 

Parfois, lorsque le modèle est utilisé, le biais pourrait changer pour s'adapter à ce que les utilisateurs tendent à entrer. Tay de Microsoft en 2016 était un excellent exemple de la manière dont le biais pourrait mal tourner.

### Tokens de glitch

Aussi connus sous le nom d'exemples adverses, les tokens de glitch sont des entrées données à un modèle pour le faire intentionnellement mal fonctionner et être inexact lorsqu'il fournit des réponses.

## Avantages des LLMs en cybersécurité

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-234.png)
_Un cerveau numérique § Crédit : [Wallpaperflare.com](http://Wallpaperflare.com)_

### Débogage et codage

Il existe déjà des débogueurs qui font un assez bon travail. Mais avec les LLMs, vous pouvez littéralement écrire du code et déboguer à un rythme beaucoup plus rapide. Assurez-vous simplement que le LLM est fourni par une entreprise qui n'a pas le potentiel d'utiliser vos données – comme Samsung l'a découvert lorsque leur code propriétaire a été divulgué par accident.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-235.png)
_ChatGPT corrigeant un morceau de code § Crédit : Mercury_

### Analyse des motifs de menace

Les LLMs ont la capacité de trouver des motifs et cela pourrait être utilisé pour analyser les comportements et les tactiques des menaces persistantes avancées afin de mieux attribuer les incidents et les atténuer si de tels motifs sont reconnus en temps réel.

### Automatisation des réponses

Les LLMs ont un grand potentiel dans le Centre des opérations de sécurité et l'automatisation des réponses. Des scripts, des outils et même des rapports peuvent être écrits en utilisant ces modèles, réduisant le temps total dont les professionnels ont besoin pour faire leur travail.

## Dangers des LLMs en cybersécurité

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-236.png)
_IA dangereuse § Crédit : [Wallpaperflare.com](http://Wallpaperflare.com)_

### Ingénierie sociale

Peut-être le danger le plus courant des LLMs en tant qu'outils est leur capacité à générer du nouveau texte. Le phishing est devenu beaucoup plus facile pour les non-natifs comme une conséquence involontaire des LLMs. OpenAI a mis en place des filtres pour minimiser cela, mais ils sont encore assez faciles à contourner. 

Une méthode courante consiste à dire à ChatGPT que vous faites un devoir et qu'il doit vous écrire une lettre à la personne. Dans l'exemple ci-dessous, j'ai dit à ChatGPT que nous jouions à un jeu, j'ai donné le prompt suivant et j'ai obtenu la réponse suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-237.png)
_ChatGPT écrivant un potentiel email de phishing § Crédit : Mercury_

Tout ce dont j'ai besoin maintenant est quelques ajustements à la lettre et je pourrais être ma propre victime d'une escroquerie perpétrée par moi-même 😱.

### Rédaction de contenu malveillant

Tout comme les LLMs peuvent écrire du code pour le bien, ils peuvent écrire du code pour le mal. Dans ses premiers stades, ChatGPT pouvait accidentellement écrire du code malveillant et les gens contournent facilement les filtres pour limiter cela. Les filtres se sont grandement améliorés, mais il reste encore beaucoup de travail à faire. 

Cela a pris un peu de réflexion et quelques prompts, mais la capture d'écran ci-dessous montre comment réinitialiser un mot de passe de compte Windows, comme donné par ChatGPT :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-238.png)
_ChatGPT donnant des étapes pour réinitialiser un mot de passe de compte utilisateur sur Windows § Crédit : Mercury_

Je voulais jouer un peu plus avec, alors j'ai essayé de lui demander d'écrire un script Powershell pour enregistrer toutes les activités dans un navigateur pendant 3 minutes. La réponse originale était celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-239.png)
_ChatGPT refusant d'écrire un script potentiellement malveillant § Crédit : Mercury_

J'ai donc décidé de donner une raison « valable » pour obtenir le script écrit 😶 :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-240.png)
_ChatGPT trompé pour écrire un script potentiellement malveillant § Crédit : Mercury_

Comme vous pouvez l'observer, l'IA m'a dit de l'utiliser de manière éthique. Cependant, je pourrais choisir de ne pas le faire. Ce n'est pas la faute du modèle, car il n'est qu'un outil et pourrait être utilisé à de nombreuses fins.

### Piratage de récompense

L'entraînement des LLMs peut être coûteux en raison de la quantité énorme de données requises et des paramètres. Mais à mesure que le temps et la technologie progressent, le coût deviendra moins cher et il y a une forte chance que quiconque puisse entraîner un LLM pour le piratage de récompense malveillant. 

Aussi connu sous le nom de jeu de spécification, une IA peut se voir donner un objectif et l'atteindre, mais pas de la manière prévue. Ce n'est pas une mauvaise chose en soi, mais cela a un potentiel dangereux. 

Par exemple, un modèle à qui l'on dit de gagner un jeu en obtenant le score le plus élevé pourrait simplement réécrire le score du jeu plutôt que de jouer au jeu. Avec quelques ajustements, les LLMs ont la possibilité de trouver de telles failles dans les systèmes du monde réel, mais plutôt que de les corriger, pourraient finir par les exploiter.

## Conclusion

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-241.png)
_Pixels colorés § Crédit : [Pexels.com](http://Pexels.com)_

Récapitulons ce que vous avez appris :

1. Qu'est-ce que l'IA et comment elle peut être utilisée pour pirater
2. Qu'est-ce que les grands modèles de langage
3. Comment les grands modèles de langage peuvent être utilisés à la fois pour le bien et le mal

L'IA a de nombreuses capacités, pouvant même devenir consciente à l'avenir. Pour l'instant, c'est un outil qui continuera à façonner nos vies en bien ou en mal. Que cet avenir soit radieux ou sombre dépend de la manière dont vous et moi nourrissons cette jeune technologie.

Bonne exploration 🤓.

### Ressources

1. [Un peu plus sur les LLMs](https://research.aimultiple.com/large-language-models/)
2. [Les mauvais côtés des LLMs](https://research.aimultiple.com/large-language-models/)
3. [ChatGPT](https://chat.openai.com)

### Remerciements

Merci à [Anuoluwapo Victor](https://twitter.com/Anuoluwap__o?t=4Cv6VR2c2_wK5HLXwbvXCQ&s=09), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), et ma famille pour l'inspiration, le soutien et les connaissances utilisées pour rassembler cet article. Ce fut un plaisir.

Un merci spécial au [Dr. Ernest Onuiri](https://www.linkedin.com/in/ernest-onuiri-114421a0) pour ses cours sur l'intelligence artificielle et l'encouragement à chercher des connaissances au-delà des salles de classe. Ce fut un honneur d'être votre étudiant.

Crédit de l'image de couverture : Andrew Neel