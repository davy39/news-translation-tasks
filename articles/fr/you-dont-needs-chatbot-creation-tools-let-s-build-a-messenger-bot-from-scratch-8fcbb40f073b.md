---
title: Vous n'avez pas besoin d'outils de création de chatbot — Construisons un bot
  Messenger à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T08:08:41.000Z'
originalURL: https://freecodecamp.org/news/you-dont-needs-chatbot-creation-tools-let-s-build-a-messenger-bot-from-scratch-8fcbb40f073b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eEi9foMd0qRFROy-B8UO6Q.jpeg
tags:
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Vous n'avez pas besoin d'outils de création de chatbot — Construisons un
  bot Messenger à partir de zéro
seo_desc: 'By Daoud Clarke

  There are many many chatbot creation tools out there. To paraphrase Dr. Seuss, some
  are good and some are sad and some are very, very bad. I know, I’ve reviewed a bunch
  of them.

  But what if you want to write one yourself, from scratch...'
---

Par Daoud Clarke

Il existe de nombreux outils de création de chatbots. Pour paraphraser le Dr Seuss, certains sont bons et d'autres sont tristes et certains sont très, très mauvais. Je sais, j'en ai [passé en revue](https://chatbottech.io/) un certain nombre.

Mais que faire si vous voulez en écrire un vous-même, à partir de zéro, sans utiliser d'outils sophistiqués ? Est-ce même possible ? Et pouvez-vous créer quelque chose d'utile ? La réponse est oui, car je l'ai fait, et je vais vous montrer comment.

Tout le code est disponible [ici](https://github.com/daoudclarke/chatbot-from-scratch) sur Github. Nous allons créer un bot pour Facebook Messenger, et nous utiliserons Google App Engine pour héberger notre bot, qui sera écrit en Python.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NVfzXyBPKYGaNqHk2f208w.jpeg)
_Il se trouve que je connais une ou deux choses sur les chatbots. Photo par [Unsplash](https://unsplash.com/photos/KesWZ9GyJ5k?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Scott Webb</a> sur <a href="https://unsplash.com/search/photos/dr-seuss?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Mais attendez, pourquoi vouloir faire cela ? Utiliser une interface graphique pour créer votre bot est beaucoup plus facile. Eh bien, voici quelques raisons :

* C'est gratuit. Le niveau [gratuit](https://cloud.google.com/free/docs/always-free-usage-limits#gae_name) d'App Engine est si généreux qu'il est peu probable que vous le dépassiez à moins d'avoir des milliers d'utilisateurs de bot — auquel cas, vous serez ravi.
* Pour apprendre. Voyez ce qu'il faut vraiment pour construire un chatbot.
* Allez au-delà de ce que les outils de création de chatbots peuvent faire. Vous vous sentez ambitieux ? Créez quelque chose de totalement original, ou créez votre [propre](http://daoudclarke.github.io/chatbots/2018/02/06/manifesto-for-a-new-chatbot-platform) plateforme de chatbot.

### Choix d'un canal de chatbot

Vous pouvez créer un bot pour de nombreux canaux différents. Certains des plus populaires sont Facebook Messenger, Kik, Slack, Twitter et Telegram. Si vous devez supporter plusieurs plateformes, vous serez mieux loti en utilisant un framework de bot. De cette façon, vous n'aurez pas à écrire le code pour vous intégrer à toutes les plateformes que vous souhaitez supporter.

Dans cet article, nous allons créer un chatbot pour Facebook Messenger. Pourquoi ? Eh bien, tout d'abord, c'est la plateforme la plus populaire pour les chatbots. Presque tous les outils pour construire des chatbots ciblent Messenger, et beaucoup d'entre eux ne supportent _que_ Messenger. Et pour de bonnes raisons : il avait 1,2 milliard d'utilisateurs actifs mensuels en 2017. C'est beaucoup d'utilisateurs potentiels de chatbots.

Il y a une autre raison pour laquelle nous voulons cibler Messenger : les réponses rapides. Ce sont des boutons que votre chatbot peut offrir aux utilisateurs comme raccourci pour qu'ils n'aient pas à taper. Non seulement ils rendent votre bot beaucoup plus engageant (qui aime taper sur un téléphone mobile ?), mais ils rendent aussi votre travail de développeur de chatbot beaucoup plus facile.

Si vous offrez des boutons aux utilisateurs, ils appuieront sur ces boutons. Cela signifie que vous n'avez pas à vous soucier de l'analyse des requêtes arbitraires des utilisateurs qui veulent savoir s'il va pleuvoir demain ou où ils peuvent obtenir une pizza. Guider les utilisateurs est bon pour eux et pour nous.

### Que doit faire un bot ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*e0z56Y8J_p8KcfaFYS6rvA.jpeg)
_Aucun ne passera. Eh bien, surtout aucun. Photo par [Unsplash](https://unsplash.com/photos/wdtF-f4qBdU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jeremy Dorrough</a> sur <a href="https://unsplash.com/search/photos/visa?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Votre bot a besoin d'un but. Il ne peut pas tout faire. Mon ami [Naré Vardanyan](https://www.linkedin.com/in/narevardanyan/) et moi avons conçu un bot pour aider les gens à naviguer dans les eaux turbides des demandes de visa pour le Royaume-Uni. Nous utiliserons une version simplifiée de ce bot comme exemple dans cet article.

### Magie de parcours d'arbre

![Image](https://cdn-media-1.freecodecamp.org/images/1*xkhS6RGZ1D7OhYdsC64IQA.jpeg)
_Pas ce genre d'arbre. Photo par [Unsplash](https://unsplash.com/photos/zThTy8rPPsY?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Adarsh Kummur</a> sur <a href="https://unsplash.com/search/photos/tree?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Nous utiliserons une méthode de conception de bot basée sur des [**arbres**](https://en.wikipedia.org/wiki/Tree_(data_structure)). Chaque nœud de l'arbre représente un état de conversation possible. Chaque enfant d'un nœud correspond à un message utilisateur possible que nous comprenons comme étant pertinent à partir de cet état particulier.

```yaml
say: "Quel est le but de votre visite ? (options : voyage, étude, affaires/travail, traitement médical, rejoindre la famille/se marier, visiter un enfant à l'école, visite diplomatique/gouvernementale)"
answers:
  travel:
    say: Vous avez besoin d'un visa de visiteur standard
  study:
    say: Combien de temps allez-vous rester au Royaume-Uni ? jusqu'à 6 mois ; plus de 6 mois
    answers:
      up to 6 months:
        say: Vous pouvez demander un visa d'études à court terme
      more than 6 months:
        say: Vous avez besoin d'un visa d'études (Tier 4)
  business/work:
    say: Combien de temps allez-vous rester au Royaume-Uni ? jusqu'à 6 mois ; plus de 6 mois
    answers:
      up to 6 months:
        say: Vous avez besoin d'un visa de visiteur standard
      more than 6 months:
        say: Êtes-vous 1. entrepreneur 2. investisseur 3. leader dans les arts ou les sciences 4. aucun des ci-dessus
        answers:
          '1':
            say: Vous pouvez demander un Tier 1 Entrepreneur
          '2':
            say: Vous pouvez demander un Tier 1 Investisseur
          '3':
            say: Vous pouvez demander un Tier 1 (Talent Exceptionnel)
          '4':
            say: On vous propose 1. un emploi qualifié 2. un rôle dans la succursale britannique de votre employeur 3. un emploi dans une communauté religieuse 4. un emploi en tant que sportif ou entraîneur d'élite
            answers:
              '1':
                say: Vous pouvez demander un visa Tier 2 (Général)
              '2':
                say: Vous pouvez demander un Tier 2 (Transfert intra-entreprise)
              '3':
                say: Tier 2 (Ministre de la Religion)
              '4':
                say: Tier 2 (Sportif)
  medical treatment:
    say: Vous avez besoin d'un visa de visiteur standard
  join family/get married:
    say: Vous avez besoin d'un visa de famille d'une personne installée si votre famille/partenaire est installée au Royaume-Uni ou d'un visa de 'personne à charge' de leur catégorie de visa s'ils travaillent ou étudient
  visiting a child:
    say: Vous avez besoin d'un visa de parent si vous visitez pendant plus de 6 mois et d'un visa de visiteur standard si votre visite est de moins de 6 mois
  diplomatic or government visit:
    say: Vous pouvez demander un visa d'exemption (exempté du contrôle de l'immigration)
```

Il s'agit d'une version simplifiée de notre bot de conseils de visa, sous forme d'arbre. Il est au format YAML (Yet Another Markup Language), ce qui le rend facile à lire. Le nœud racine spécifie le premier message que le bot envoie à l'utilisateur, dans ce cas, demandant à l'utilisateur « Quel est le but de votre visite ? » Les nœuds enfants (spécifiés sous « answers ») contiennent les réponses possibles que nous accepterons, à savoir « voyage », « étude », « affaires/travail », et ainsi de suite.

### Pour commencer

Pour créer notre bot, nous devons configurer un certain nombre de choses dans Facebook. Les instructions officielles sont [ici](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup), mais en résumé, vous aurez besoin de :

* Une page Facebook — chaque bot a besoin d'une page Facebook différente.
* Un compte développeur pour vous permettre de créer des applications.
* Une application Facebook pour obtenir un jeton d'accès secret qui sera nécessaire plus tard.

Les bots Facebook fonctionnent avec des **webhooks**, qui sont simplement des URL que Facebook Messenger utilise pour interagir avec votre bot.

Pour créer notre webhook, nous utiliserons [Google App Engine](https://cloud.google.com/appengine/). L'avantage de cela est qu'il est gratuit pour les faibles volumes et s'adapte automatiquement à mesure que vous obtenez plus de trafic. Pour cet article, j'ai utilisé Python, mais il y a beaucoup d'autres langages que vous pouvez utiliser. Vous devrez [télécharger le SDK Python](https://cloud.google.com/appengine/docs/standard/python/download) et [créer un projet Google Cloud](https://console.cloud.google.com/project) si vous n'en avez pas déjà un.

### Création de notre webhook

![Image](https://cdn-media-1.freecodecamp.org/images/1*wvmnYETqWUowkuP5Y2jQPA.jpeg)
_Accroché ? Photo par [Unsplash](https://unsplash.com/photos/TRggaD8mHJ4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Fabien Bazanegue</a> sur <a href="https://unsplash.com/search/photos/hook?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

La première chose que notre webhook doit faire est de permettre à Facebook de vérifier que nous sommes vraiment le webhook correct. Nous le faisons en gérant une requête GET qui contient un « verify token ». Il s'agit d'une chaîne secrète aléatoire que nous avons partagée avec Facebook. Cette partie de notre code est basée sur l'excellent dépôt Facebook Messenger Bot [repository](https://github.com/hartleybrody/fb-messenger-bot).

```py
class MainPage(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        super(MainPage, self).__init__(request, response)
        logging.info("Initialisation avec un nouveau bot.")
        self.bot = TreeBot(send_message, UserEventsDao(), TREE)

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        mode = self.request.get("hub.mode")
        if mode == "subscribe":
            challenge = self.request.get("hub.challenge")
            verify_token = self.request.get("hub.verify_token")
            if verify_token == VERIFY_TOKEN:
                self.response.write(challenge)
        else:
            self.response.write("Ok")
```

Ici, nous initialisons d'abord une classe pour gérer les requêtes dans le [framework webapp2](https://webapp2.readthedocs.io/en/latest/). Nous enregistrons d'abord un message pour dire que le bot est en cours d'initialisation, puis nous construisons la classe `TreeBot` qui gérera toute la logique du bot, discutée ci-dessous.

Ensuite, nous vérifions les requêtes « subscribe » de Facebook et vérifions que le jeton de vérification envoyé dans la requête est le même que celui secret que nous avons partagé avec Facebook.

### Gestion des messages des utilisateurs

Ensuite, nous devons interpréter les messages des utilisateurs, qui sont envoyés par Facebook à notre webhook en utilisant des requêtes POST.

```py
    def post(self):
        data = json.loads(self.request.body)
        logging.info("Données reçues : %r", data)

        if data["object"] == "page":

            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    sender_id = messaging_event["sender"]["id"]

                    if messaging_event.get("message"):
                        message = messaging_event['message']
                        if message.get('is_echo'):
                            logging.info("Ignorer l'événement d'écho : " + message.get('text', ''))
                            continue
                        message_text = messaging_event['message'].get('text', '')
                        logging.info("Un message reçu : %s", message_text)
                        self.bot.handle(sender_id, message_text)

                    if messaging_event.get("postback"):
                        payload = messaging_event['postback']['payload']
                        self.bot.handle(sender_id, payload)
                        logging.info("Post-back")
```

Ici, nous analysons d'abord les données JSON de Facebook et les enregistrons pour aider au débogage. Nous itérons ensuite sur les événements de messagerie dans les données. Tout d'abord, nous extrayons l'ID de l'expéditeur, dont nous aurons besoin pour envoyer des réponses à l'utilisateur. Il existe deux types d'événements : les messages (que l'utilisateur a tapés) et les événements « postback », qui sont envoyés lorsqu'un utilisateur clique sur un bouton de réponse rapide.

Pour le premier de ceux-ci, nous devons ignorer les événements « echo ». Nous extrayons ensuite le texte du message et l'envoyons à notre logique de bot pour le traiter. Nous faisons de même avec les événements de postback, en extrayant la charge utile, qui dans notre cas est simplement le texte du bouton.

### Envoi de messages aux utilisateurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*JYGEBAIYB9j-gkfy7iijQg.jpeg)
_Les messages des utilisateurs n'arrivent pas dans des bouteilles. Photo par [Unsplash](https://unsplash.com/photos/ssoJQfH7Acw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Scott Van Hoy</a> sur <a href="https://unsplash.com/search/photos/message-in-a-bottle?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Lorsque nous avons construit notre classe `TreeBot`, nous avons passé une fonction `send_message` qui permet à la logique du bot d'envoyer des messages de retour à l'utilisateur. La voici :

```py
def send_message(recipient_id, message_text, possible_answers):
    logging.info("Envoi d'un message à %r : %s", recipient_id, message_text)
    headers = {
        "Content-Type": "application/json"
    }
    message = get_postback_buttons_message(message_text, possible_answers)
    if message is None:
        message = {"text": message_text}

    raw_data = {
        "recipient": {
            "id": recipient_id
        },
        "message": message
    }
    data = json.dumps(raw_data)
    r = urlfetch.fetch("https://graph.facebook.com/v2.6/me/messages?access_token=%s" % ACCESS_TOKEN,
                       method=urlfetch.POST, headers=headers, payload=data)
    if r.status_code != 200:
        logging.error("Erreur d'envoi du message : %r", r.status_code)


def get_postback_buttons_message(message_text, possible_answers):
    if possible_answers is not None and len(possible_answers) <= 3:
        buttons = []
        for answer in possible_answers:
            if len(answer) > 20:
                return None
            buttons.append({
                "type": "postback",
                "title": answer,
                "payload": answer,
            })
        return {
            "attachment": {
                "type":"template",
                "payload": {
                    "template_type": "button",
                    "text": message_text,
                    "buttons": buttons,
                }
            }
        }
    return None
```

L'ID du destinataire sera l'ID de l'expéditeur que nous avons extrait précédemment. Avec cela, nous avons le texte du message et quelques boutons de réponse rapide pour que l'utilisateur puisse appuyer. Nous vérifions d'abord que les en-têtes de la requête spécifient notre contenu comme JSON, puis nous construisons la partie des boutons de postback du message. Nous spécifions l'ID du destinataire et le texte du message et convertissons en JSON. Nous faisons notre requête à l'API Graph de Facebook, en passant le jeton d'accès secret que Facebook nous a donné lorsque nous avons créé notre application.

### Exécution du serveur de bot

Le dernier morceau de code dans ce fichier construit simplement la classe principale et l'exécute :

```py
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
```

### Cerveau du bot

![Image](https://cdn-media-1.freecodecamp.org/images/1*HFJOSbIDPjI3SW8Jx4a4Zg.jpeg)
_Pas un cerveau, mais y ressemble. Photo par [Unsplash](https://unsplash.com/photos/ZEpxoNzKfcc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Vlad Tchompalov</a> sur <a href="https://unsplash.com/search/photos/brain?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Nous en arrivons à la partie intéressante : comment le bot sait-il quoi dire ? Le cerveau du bot se trouve dans le fichier `bot.py`.

```py
class TreeBot(object):
    def __init__(self, send_callback, users_dao, tree):
        self.send_callback = send_callback
        self.users_dao = users_dao
        self.tree = tree

    def handle(self, user, message):
        self.users_dao.add_user_event(user, 'received', message)
        history = self.users_dao.get_user_events(user)
        tree = self.tree
        logging.debug("Éléments d'historique : %d", len(history))
        restarting = False
        nothing_sent = True
        response = DEFAULT
        possible_answers = DEFAULT_POSSIBLE_ANSWERS
        for direction, content in history:
            response = DEFAULT
            possible_answers = DEFAULT_POSSIBLE_ANSWERS
            if direction == 'received':
                key = get_content_match(content, tree)
                if nothing_sent:
                    response = tree['say']
                    possible_answers = tree['answers'].keys()
                elif key is not None:
                    tree = tree[key]
                    if 'say' in tree:
                        response = tree['say']
                        possible_answers = None
                        if 'answers' in tree:
                            possible_answers = tree['answers'].keys()
                    restarting = False
                elif restarting:
                    if content == 'yes':
                        tree = self.tree
                        response = tree['say']
                        possible_answers = tree['answers'].keys()
                        restarting = False
            elif direction == 'sent':
                nothing_sent = False
                if 'answers' in tree and direction == 'sent' and content == tree.get('say'):
                    tree = tree['answers']
                elif direction == 'sent' and content == DEFAULT:
                    restarting = True
            else:
                raise ValueError("Direction inattendue : " + direction)

        logging.debug("Réponse : %s", response)

        self.send_callback(user, response, possible_answers)
        self.users_dao.add_user_event(user, 'sent', response)
```

La classe est initialisée avec trois paramètres :

* une fonction de rappel (qui a été définie ci-dessus) pour envoyer des messages aux utilisateurs
* un objet d'accès aux données pour stocker des informations sur les utilisateurs
* l'arbre qui contient la logique de ce qui doit être dit et quand. Celui-ci est analysé à partir du YAML que nous avons montré ci-dessus.

Tout d'abord, nous enregistrons que nous avons reçu le message de l'utilisateur, puis nous récupérons toutes les actions passées de l'utilisateur à partir de l'objet d'accès aux données. Nous rejouons ensuite les actions de l'utilisateur pour déterminer où ils se trouvent actuellement dans l'arbre.

Nous initialisons la réponse à un message par défaut qui sera retourné lorsque l'utilisateur dit quelque chose que nous ne comprenons pas. Dans notre cas, il s'agit de « Je suis désolé, je n'ai pas compris, devons-nous recommencer ? » Il y a aussi quelques réponses possibles par défaut, qui sont « oui » et « non ». Nous gardons également une trace de si nous pensons que nous redémarrons la conversation à partir de zéro.

Nous commençons ensuite à itérer sur l'historique de l'utilisateur. Pour chaque message, nous vérifions s'il a été envoyé par nous, ou si nous l'avons reçu de l'utilisateur. S'il a été reçu, nous vérifions s'il correspond aux options actuelles dans l'arbre. Cela utilise la fonction suivante :

```py
def get_content_match(content, tree):
    matches = []
    for key in sorted(tree):
        if content.lower() in key.lower():
            matches.append(key)
    if len(matches) == 1:
        return matches[0]
```

Cela vérifie le contenu du message de l'utilisateur pour voir s'il apparaît comme une sous-chaîne de l'une des options actuelles dans l'arbre. S'il y a exactement une seule correspondance, nous retournons cette correspondance, sinon la réponse de l'utilisateur est ambiguë ou il n'y a pas de correspondance du tout.

Ensuite, nous vérifions si nous avons envoyé quoi que ce soit à l'utilisateur. Si ce n'est pas le cas, nous définissons notre réponse comme étant la première réponse dans l'arbre, et nous définissons les réponses possibles comme étant le premier ensemble de l'arbre.

Ensuite, nous vérifions si nous avons trouvé une correspondance pour le message de l'utilisateur. Si c'est le cas, nous mettons à jour l'arbre pour qu'il soit la branche enfant appropriée, et nous extrayons la bonne réponse et les réponses possibles de l'arbre.

Nous vérifions ensuite si nous avons suggéré de redémarrer et si l'utilisateur a confirmé qu'il souhaite redémarrer la conversation. Dans ce cas, nous réinitialisons l'arbre à son état initial et utilisons la première réponse comme nous l'avons fait précédemment.

Pour chaque message de l'historique qui a été envoyé par le bot, nous mettons à jour l'arbre en conséquence. Ou si nous avons envoyé le message par défaut, nous enregistrons que nous pouvons redémarrer la conversation.

Enfin, après avoir parcouru tout l'historique, nous enregistrons notre réponse, envoyons le message à l'utilisateur et enregistrons le message que nous avons envoyé dans notre objet d'accès aux données.

### La dernière pièce du puzzle

![Image](https://cdn-media-1.freecodecamp.org/images/1*a5N4vokpfnlmUnnJMou9zw.jpeg)
_Écrire un chatbot est plus facile que de faire ce puzzle. Photo par [Unsplash](https://unsplash.com/photos/3y1zF4hIPCg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Hans-Peter Gauster</a> sur <a href="https://unsplash.com/search/photos/puzzle?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Le seul morceau de code restant à discuter est l'objet d'accès aux données qui stocke toutes les interactions des utilisateurs. Nous avons pris la décision de conception de stocker toutes les actions des utilisateurs et de les rejouer comme nous l'avons fait ci-dessus car cela nous a permis de changer facilement la logique du bot et de pouvoir encore déduire un état approprié pour le bot et l'utilisateur. Si nous avions choisi de labelliser chaque nœud de l'arbre et de stocker ce label, alors tout changement dans l'arbre aurait rendu les anciennes conversations invalides.

Ainsi, notre objet d'accès aux données doit être capable de faire deux choses : stocker un nouvel événement utilisateur et récupérer tous les événements pour un utilisateur particulier.

```py
class UserEvent(ndb.Model):
    user = ndb.StringProperty()
    direction = ndb.StringProperty()
    message = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class UserEventsDao(object):
    def add_user_event(self, user, direction, message):
        event = UserEvent()
        event.user = user
        event.direction = direction
        event.message = message
        logging.info("Ajout d'un événement : %r", event)
        event.put()

    def get_user_events(self, user):
        events = UserEvent.query(UserEvent.user == user)
        sorted_events = sorted(events, key=lambda x: x.date)
        return [(event.direction, event.message) for event in sorted_events]
```

Notre objet d'accès aux données utilise [Google Datastore](https://cloud.google.com/datastore/docs/concepts/overview), qui est très facile à utiliser depuis App Engine et dispose d'un niveau d'utilisation gratuit généreux. L'API Python rend l'utilisation de Datastore très facile. Tout d'abord, nous créons une classe de modèle, `UserEvent`, qui spécifie les champs et leurs types. Dans notre cas, l'ID de l'utilisateur, la direction du message et le message lui-même sont des chaînes, et enfin la date de l'événement a un type date-heure.

Pour créer et stocker un nouvel événement utilisateur, nous construisons simplement cette classe, définissons les propriétés, puis appelons `put()` sur l'objet.

Pour récupérer les événements d'un utilisateur, nous appelons la fonction `query()` sur la classe, en passant l'ID de l'utilisateur. Nous trions ensuite les événements par date et retournons une liste de paires direction-message.

### Déploiement

C'est toutes les parties de notre bot ! Maintenant, déployons-le et connectons-le à Messenger.

Pour déployer votre application sur App Engine, utilisez la commande `gcloud` qui est venue avec le SDK App Engine :

```
gcloud app deploy --project [YOUR_PROJECT_ID]
```

Une fois déployé, l'URL de votre webhook est

```
http://[YOUR_PROJECT_ID].appspot.com/
```

Mettez à jour votre application Facebook avec cette URL de webhook (suivez les instructions [ici](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup)) et vous devriez être prêt à partir !

### Le monde est votre huître de chatbot

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-NZf2K93B_GCI71CR5jjA.jpeg)
_Les huîtres sont savoureuses mais les chatbots sont amusants. Photo par [Unsplash](https://unsplash.com/photos/p4-LAfM9yAg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Charlotte Coneybeer</a> sur <a href="https://unsplash.com/search/photos/oyster?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Vous pouvez créer de nombreux types de chatbots en utilisant ces techniques. J'ai déjà eu du plaisir à créer un bot de style [_Choose Your Own Adventure_](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure), mais je suis sûr que vous serez capable de trouver des choses beaucoup plus inventives. Oh, et si vous voulez essayer le bot de visa, vous pouvez l'essayer [ici](https://www.facebook.com/harveyaibot/) (bien que cette version soit un peu plus sophistiquée).

Et, si vous n'avez pas envie de tout ce travail acharné, vous pourriez toujours essayer l'un des nombreux outils de création de chatbot [tools](https://chatbottech.io/).