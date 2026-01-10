---
title: 'Comment créer un slackbot basique : un guide pour débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-06T20:29:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-basic-slackbot-a-beginners-guide-6b40507db5c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h89l_KJR8w2NrzQXtPCAmw.jpeg
tags:
- name: automation
  slug: automation
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: slack
  slug: slack
- name: 'tech '
  slug: tech
seo_title: 'Comment créer un slackbot basique : un guide pour débutants'
seo_desc: 'By Vishwa Shah

  Update: code and tutorial updated on June 28 to reflect Slack API changes.

  Slackbots: Why use them?

  Before we get into the tutorial part of this post, let’s take a look at why this
  can be a worthy project and tool.

  Slack is an increasi...'
---

Par Vishwa Shah

**Mise à jour : le code et le tutoriel ont été mis à jour le 28 juin pour refléter les changements de l'API Slack**.

# Slackbots : Pourquoi les utiliser ?

Avant de passer à la partie tutoriel de cet article, examinons pourquoi ce peut être un projet et un outil dignes d'intérêt.

[Slack](http://slack.com/) est un outil de communication de plus en plus populaire pour les équipes. Il s'est développé pour inclure des plugins pour d'autres outils de gestion de projet largement utilisés, comme JIRA, Google Drive, et autres. Tout utilisateur de Slack sait — plus vous pouvez faire de choses depuis la conversation, mieux c'est.

Les utilisations courantes d'un slackbot vont d'un simple notificateur pour quand une tâche est terminée (comme une construction de test, ou quand votre déjeuner est prêt) à des bots interactifs basés sur des boutons qui exécutent des commandes à la volonté de l'utilisateur. Vous pouvez créer des mécanismes de sondage, des bots conversationnels, et plus encore.

# Installation d'un environnement de programmation Python

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_p65lij8MGz7AUNRl9D3sNw.gif)

Si vous êtes un utilisateur Windows et que vous n'avez pas utilisé Python auparavant, vous devrez l'[installer](https://docs.python.org/3/using/windows.html). Utilisateurs Linux/Mac : Unix vient avec Python !

Une fois installé, lancez votre terminal et tapez `python` ou `python3` (si vous avez plusieurs installations) pour vous assurer qu'il fonctionne et est présent.

Vérifiez également que vous avez un bon éditeur de texte pour le code : [sublime](https://www.sublimetext.com/3) et [atom](https://flight-manual.atom.io/getting-started/sections/installing-atom/) sont d'excellents choix.

Optionnel : Il peut également être utile de travailler dans un environnement virtuel — c'est une bonne pratique lorsque vous avez beaucoup de dépendances.

```
pip install virtualenv
virtualenv tutorial
source tutorial/bin/activate
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_QHX3UYi6NFRe_xteZ9qiYQ.gif)

Vous devriez également fork le [dépôt GitHub du tutoriel](https://github.com/vishwa35/slackbot-tutorial) et le cloner sur votre machine locale, car nous utiliserons ce code comme framework pour ce tutoriel.

Pour ce faire, allez sur le [dépôt](https://github.com/vishwa35/slackbot-tutorial) et cliquez sur `Fork` en haut à droite. Le dépôt forké devrait être **<votreutilisateur>/slackbot-tutorial**. Cliquez sur le bouton vert `Clone or download` à droite sous la barre de statistiques, et copiez l'URL. Retournez au terminal pour cloner le dépôt :

```
cd Desktop/
git clone https://github.com/votreutilisateur/slackbot-tutorial.git
cd slackbot-tutorial/
sublime . (ou ouvrez votre éditeur de texte et ouvrez ce répertoire)
```

# Applications Slack

Il existe deux façons de créer votre slackbot : des bots autonomes ou des applications Slack. Les applications permettent une gamme de fonctionnalités plus large à l'avenir et constituent la méthode recommandée par Slack pour créer un utilisateur bot.

Allez sur [https://api.slack.com/apps](https://api.slack.com/apps) et cliquez sur `Create New App` en haut à droite. Donnez-lui un nom et choisissez un espace de travail où vous pouvez créer un canal pour tester votre bot. Vous pouvez toujours reconfigurer votre bot pour un autre espace de travail plus tard, ou même le publier dans le répertoire des applications Slack.

Je recommande de créer un canal #test dans un espace de travail que vous créez uniquement à des fins de développement, ou dans un espace qui a relativement peu d'utilisateurs qui ne vous dérangeraient pas de tester quelque chose.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_aHE2Te70SwllhMxUE5Tgpg.png)

La première chose que vous voudrez faire est d'obtenir le jeton du bot. Lorsque vous arrivez à la page ci-dessus, cliquez sur Bots. Ajoutez quelques portées ; celles-ci déterminent quelles permissions l'utilisateur bot de votre application aura. Pour commencer, [**chat:write**](https://api.slack.com/scopes/chat:write) et [**im:write**](https://api.slack.com/scopes/im:write) sont probablement suffisants.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_881iK1n-kUuZVXagvfS5qg.png)

Maintenant, pour obtenir vos jetons, vous voudrez aller à `OAuth & Permissions` dans la barre latérale de gauche.

Ici, vous pourrez `Install the App to the Workspace` et générer les jetons nécessaires. En règle générale, les **jetons de bot** commencent par `xoxb-.`

Vous voudrez également le **secret de signature**, qui se trouve sous Basic Information > App Credentials.

## Agir en tant que votre Bot

Maintenant, vous avez les informations d'identification nécessaires pour faire des appels API et agir en tant que votre bot. Pour tester cela, lancez un terminal et exécutez ceci (avec le jeton et le nom du canal corrects) :

```
curl -X POST \
     -H 'Authorization: Bearer xoxb-votre-jeton' \
     -H 'Content-type: application/json;charset=utf-8' \
    --data '{"channel":"#test","text":"Bonjour, Slack !"}' \
https://slack.com/api/chat.postMessage
```

Si vous allez dans ce canal dans votre espace de travail Slack, vous devriez maintenant voir un message de votre bot ! Vous venez de faire une requête HTTP POST — vous avez demandé à un serveur de poster un message quelque part.

# Programmer le Bot

Nous voulons faire ce qui précède de manière programmatique. Il existe plusieurs façons de configurer un slackbot. Je couvrirai les points suivants :

* Déclenché périodiquement (selon un calendrier) pour dire quelque chose
* Commandes /slash

La seconde méthode nécessite un serveur en cours d'exécution, tandis que la première n'en a pas besoin.

## Messages planifiés

Supposons que vous souhaitiez envoyer périodiquement un message quelque part — peut-être tous les lundis matins. Allez à l'éditeur de texte où vous avez ouvert `slackbot-tutorial`.

Vous devriez voir un fichier `scheduled.py`. Jetez un coup d'œil : `sendMessage` est une fonction qui envoie l'appel API à Slack et publie un message. En bas, vous verrez la méthode principale : ce qui s'exécute lorsque vous lancez le script. Ici, vous verrez quelques points à noter :

* `SLACK_BOT_TOKEN` est extrait de `os.environ['SLACK_BOT_TOKEN']` — comment ? Exécutez `export SLACK_BOT_TOKEN="xoxb-votre-jeton"` dans votre terminal pour définir cette variable.
* Un planificateur est utilisé ici, et il y a une boucle infinie qui vérifie les événements sur le planificateur. Par défaut ici, j'ai planifié la fonction `sendMessage` pour qu'elle soit appelée toutes les minutes.

Pour tester cela, retournez au terminal où vous êtes dans le répertoire `slackbot-tutorial` et exécutez

```
export SLACK_BOT_TOKEN="xoxb-votre-jeton"
python scheduled.py
```

Vous devriez voir les messages de journalisation s'imprimer. Assurez-vous d'avoir changé `**channel=#test**` dans le code par le nom de votre canal de test (si différent) et d'avoir ajouté votre bot (dans le canal Slack, tapez `/invite @nomdubot`. Laissez-le fonctionner pendant quelques minutes et regardez les messages apparaître sur Slack !

Ceci est, bien sûr, une implémentation super basique d'un envoyeur de messages planifiés — vous pouvez en fait faire cela simplement avec le slackbot `/remind #test "Bonjour, Slack !" tous les lundis à 9h`.

Le **vrai pouvoir** ici est que vous pouvez substituer n'importe quelle fonction à `sendMessage`, en exploitant le pouvoir de l'interface avec des services externes via des API, en faisant des maths, etc., puis en construisant un message à poster.

## Commandes Slash

Cela nécessite un peu plus de configuration — retournez à vos [paramètres d'application](http://api.slack.com/apps) > Slash Commands. Créez une nouvelle commande slash : par exemple, `/test`. Pour l'URL de requête, vous devrez soit déployer ce serveur web (j'utilise Heroku), soit exécuter une instance locale `ngrok` pour le tester. Ce dernier l'exécutera localement et est le meilleur pour les tests. Vous pouvez faire `brew install ngrok` ou l'obtenir depuis [ici](https://ngrok.com/download).

Dans le dépôt de code de démarrage, cherchez `slashCommand.py` pour commencer à comprendre cette méthode. Pour démarrer le serveur, exécutez `python server.py`. L'URL de requête à mettre dans Slack sera donnée par votre instance `ngrok` et le `@app.route` dans votre code — ce serait quelque chose comme [http://a1234b5cde6f.ngrok.io](http://a8787d2fea3b.ngrok.io/)/**slack/test** (la partie en gras provient de la route définie dans le code). Vous devriez pouvoir tester les commandes slash dans votre espace de travail Slack. À partir du code du tutoriel, essayez `/test`.

# Aller de l'avant

Maintenant, vous avez un slackbot très basique qui fonctionne soit sur commande, soit s'exécute de temps en temps. Soyez créatif dans la façon dont vous l'utilisez ! Réfléchissez à ce que vous pouvez relier à ce squelette pour le rendre plus utile.

## Autres façons dont votre bot pourrait répondre

1. Les actions/réponses pourraient être déclenchées par des mentions ou certaines phrases. Cela nécessite l'exécution d'un serveur et l'écoute des messages quelque part.
2. Votre bot pourrait être conversationnel et pourrait contribuer à des fils de discussion. Consultez certains NLP pour commencer à avoir une conversation intelligible ! Word2Vec + TensorFlow ou Keras pourraient être un bon point de départ. DialogFlow est également excellent.
3. Reliez-le à d'autres API. Peut-être voulez-vous pouvoir interagir avec une feuille Google et effectuer quelques calculs. Vous pourriez vouloir envoyer un message à d'autres utilisateurs en fonction de certaines actions. Intégrez des [boutons](https://api.slack.com/docs/message-buttons). Peut-être voulez-vous déclencher des messages en fonction de quelque chose d'autre.