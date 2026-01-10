---
title: Comment configurer les notifications push dans votre bot Telegram
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T22:36:36.000Z'
originalURL: https://freecodecamp.org/news/telegram-push-notifications-58477e71b2c2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mN13Q59wDCwvUWCF
tags:
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: telegram
  slug: telegram
seo_title: Comment configurer les notifications push dans votre bot Telegram
seo_desc: 'By Nikita Kholin

  Telegram is a great platform with lots of great users (I’m a Telegram user myself).
  And what would be the best way for Telegram users to receive notifications? We can’t
  know for sure. Maybe they like email or something else. But we c...'
---

Par Nikita Kholin

Telegram est une excellente plateforme avec de nombreux utilisateurs (je suis moi-même un utilisateur de Telegram). Et quelle serait la meilleure façon pour les utilisateurs de Telegram de recevoir des notifications ? Nous ne pouvons pas en être sûrs. Peut-être qu'ils préfèrent les emails ou autre chose. Mais nous pouvons supposer que l'envoi de notifications via Telegram serait assez pratique.

Si vous souhaitez envoyer des notifications Telegram depuis votre application, vous êtes au bon endroit. J'ai ajouté cette fonctionnalité à [mon application](https://musicnotifier.com/) et je l'adore.

Une petite note rapide. Dans cet article, je fournis des exemples de code en Python. Mais les idées ne sont pas spécifiques à Python et peuvent être traduites dans un autre langage sans aucun problème.

Alors sans plus attendre, plongeons dans la manière dont nous pouvons le faire.

### Créer un bot Telegram

Tout d'abord, vous devez créer un bot Telegram. Pour cela, vous devez utiliser un autre bot Telegram, [BotFather](https://telegram.me/botfather). Il suffit de lui parler (appuyez sur démarrer).

![Image](https://cdn-media-1.freecodecamp.org/images/K0IHhahp6VR-IJDs8ohcZRxBBlUMaRWuUt4g)

Maintenant, vous voyez ce qu'il peut faire. Mais ce qui nous intéresse, c'est de créer un nouveau bot, c'est donc ce que nous allons choisir (`/newbot`).

![Image](https://cdn-media-1.freecodecamp.org/images/4TCF43Y1rArQcRQb-5F6XblOvTEMXUwWazrd)

Vous allez rapidement découvrir que le nom du bot doit se terminer par « bot ». Et comme vous êtes comme moi et que vous arrivez trop tard dans le jeu, la plupart des noms de bots sont déjà pris.

![Image](https://cdn-media-1.freecodecamp.org/images/yRoEugA8JJ1ccppRU8g3kcy40mGsJqCalzRG)

Mais finalement, vous allez trouver un nom pour votre bot et obtenir un jeton d'accès dont nous aurons besoin.

Maintenant que vous avez un bot, les utilisateurs de Telegram peuvent le trouver et l'utiliser. Mais il y a un problème — vous ne pouvez pas associer les utilisateurs qui viennent de Telegram aux utilisateurs de votre application. Laissez-moi vous montrer pourquoi.

Une fois qu'un utilisateur appuie sur le bouton « Start » de votre bot, vous recevrez une « mise à jour ». Vous pouvez vérifier toutes les mises à jour du bot même dans votre navigateur en visitant l'URL suivante `https://api.telegram.org/bot{bot_token}/getUpdates` (n'oubliez pas d'utiliser votre jeton d'accès dans l'URL). Voici ce que j'ai obtenu :

![Image](https://cdn-media-1.freecodecamp.org/images/AydGLffhxTaXFcqwj3untIxDVGf-AyGE26pc)

Vous ne pouvez rien lire ? Ne vous inquiétez pas. Vous pouvez corriger cela en installant une extension de mise en forme JSON dans votre navigateur. J'utilise [JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/mhimpmpmffogbmmkmajibklelopddmjf) pour Chrome. C'est beaucoup mieux.

![Image](https://cdn-media-1.freecodecamp.org/images/iG2V6vR4rqS8Lmw-Cxg5FisuCHU9XAFEquzc)

Comme vous pouvez le voir, nous n'obtenons pas beaucoup d'informations sur la personne. À partir de ces informations, nous pouvons obtenir leur nom complet. Mais ce serait de la chance si l'utilisateur fournissait son nom complet dans votre application, et cela ne garantit pas son unicité. Nous ne pouvons donc pas utiliser cela pour trouver un utilisateur dans vos applications.

Une autre information que nous obtenons est le nom d'utilisateur. Cela est plus utile car il est unique entre tous les utilisateurs de Telegram. Mais il est peu probable que vous ayez cela de disponible dans vos applications. Nous devrions donc demander à un utilisateur d'entrer son nom d'utilisateur quelque part dans l'application. C'est juste trop de travail et je ne suis pas sûr que quelqu'un le fasse.

Une autre option pour associer un utilisateur serait de lui demander de fournir l'email qu'il a utilisé dans votre application au bot. Mais cela présente trop de défauts : l'utilisateur peut faire une faute de frappe en entrant l'email, l'utilisateur peut entrer l'email d'un autre utilisateur et exploiter le système. C'est juste trop mauvais.

Pouvons-nous faire mieux ?

### Associer un utilisateur

Bien sûr que nous pouvons. Pour associer l'utilisateur, nous allons utiliser une technique appelée [deep linking](https://core.telegram.org/bots#deep-linking).

Tout d'abord, vous devez créer un jeton unique aléatoire pour chaque utilisateur. J'ai utilisé le code suivant pour générer le jeton en utilisant Python :

```
from secrets import token_urlsafetoken = token_urlsafe(8)token# => 'uEDbtJFHxKc'
```

Ensuite, vous devez sauvegarder ce jeton pour pouvoir trouver un utilisateur avec celui-ci plus tard. Vous pouvez le sauvegarder dans votre base de données ou utiliser un autre endroit comme un cache par exemple. J'ai un modèle `Notification` donc j'ai ajouté un champ à la table du modèle.

```
class Notification(models.Model):    user = models.ForeignKey(User, on_delete=models.CASCADE)	# ...    connect_token = models.CharField(max_length=64, null=True)
```

Nous avons donc généré le jeton `uEDbtJFHxKc` et l'avons sauvegardé. Maintenant, nous devons utiliser ce jeton dans une URL vers le bot Telegram que l'utilisateur doit cliquer pour que tout fonctionne :

```
telegram_url = 'https://www.telegram.me'bot_name = 'music_notification_bot'token = 'uEDbtJFHxKc'url = f'{telegram_url}/{bot_name}?start={token}'
```

Maintenant que nous avons notre URL, `'https://telegram.me/music_notification_bot?start=uEDbtJFHxKc'`, il est temps de la montrer à l'utilisateur. Il suffit de l'afficher à n'importe quel endroit de votre application et d'attendre que l'utilisateur clique dessus.

Une fois que l'utilisateur a mordu à l'hameçon et cliqué sur « Start », vous devriez recevoir une autre mise à jour :

```
{    "ok": true,    "result": [        // ...        // mises à jour précédentes       	// ...		{			"update_id": 599162365,			"message": {                "message_id": 174,                "from": { ... },                "chat": { ... },                "date": 1549788357,                "text": "/start uEDbtJFHxKc",                "entities": [ ... ]        	}        }    ]}
```

Nous pouvons enfin identifier notre utilisateur. Le champ `text` contient maintenant notre jeton utilisateur. Allons-y et extrayons-le de ce champ :

```
bot_token = 'your_bot_token'updates_url = f'https://api.telegram.org/bot{bot_token}/getUpdates'import requestsresponse = requests.get(updates_url).json()text = response['result'][0]['message']['text']text# => '/start uEDbtJFHxKc'splitted_text = text.split(' ')# => ['/start', 'uEDbtJFHxKc']token = splitted_text[-1]# => 'uEDbtJFHxKc'
```

Ce jeton peut être utilisé pour trouver l'utilisateur. Votre implémentation dépend de la manière dont vous avez sauvegardé le jeton au départ. Mais voici comment je le fais :

```
notification = Notification.objects.get(channel='telegram', connect_token=token)user = notification.user
```

L'utilisateur a donc appuyé sur le bouton « Start ». Mais il voit que rien ne s'est passé. Accueillons-le au moins.

![Image](https://cdn-media-1.freecodecamp.org/images/t3LnDt2icX4drb1ZwOr4t0gd8rHaoNhuOxoR)

Pour accueillir l'utilisateur, nous devons découvrir que l'utilisateur a commencé une conversation avec notre bot. Il y a deux options pour cela : le polling et les webhooks.

Vous savez déjà ce qu'est le polling. Vous l'avez déjà fait. Ou du moins, vous m'avez vu le faire. Une fois que nous avons consulté la page `https://api.telegram.org/bot{bot_token}/getUpdates`, nous avons fait un polling. Le polling consiste à vérifier constamment les mises à jour, toutes les 2 secondes par exemple. De cette manière, nous pouvons toujours savoir quand quelqu'un a interagi avec le bot.

Les webhooks prennent une direction un peu différente. Au lieu de vérifier toutes les 2 secondes les mises à jour, nous attendons simplement qu'une mise à jour se produise. Et lorsqu'elle se produit, Telegram enverra une requête avec les données de mise à jour à une URL que nous spécifions. De cette manière, nous pouvons donner du repos à la fois à nos serveurs et à ceux de Telegram et simplement attendre que la mise à jour arrive.

Le polling peut être meilleur si vous avez un trafic élevé, mais malheureusement, c'est plutôt une exception, donc j'ai décidé d'opter pour le webhook.

### Webhooks

![Image](https://cdn-media-1.freecodecamp.org/images/nn4BJScN-LpTraRBdaaZ6--uBVl7Ikrlfj6E)

La configuration d'un webhook dans Telegram est très facile. Vous devez simplement envoyer une requête à `https://api.telegram.org/bot{bot_token}/setWebhook?url={your_server_url}`. Ouvrir ce lien dans votre navigateur fonctionne également. `your_server_url` est l'URL à laquelle Telegram enverra les mises à jour. Voici ce que vous devriez obtenir en réponse :

```
{    "ok": true,    "result": true,    "description": "Webhook was set"}
```

Si vous ne vous faites pas confiance, vous pouvez visiter `https://api.telegram.org/bot{bot_token}/getWebhookInfo` juste pour vérifier que tout est OK. Vous devriez voir quelque chose comme ceci :

```
{    "ok": true,    "result": {        "url": "https://example.com/your_server_endpoint",        "has_custom_certificate": false,        "pending_update_count": 0,        "max_connections": 40    }}
```

Maintenant, si quelque chose ne va pas (par exemple, vous avez défini une URL incorrecte), vous pouvez toujours supprimer le webhook en visitant `[https://api.telegram.org/bot{bot_token}/deleteWebhook](https://api.telegram.org/bot{bot_token}/deleteWebhook)` puis en définissant à nouveau le webhook.

### Développement local

Avant de continuer, je voudrais dire quelques mots sur le développement local. Les webhooks ne sont pas très adaptés à cela. Les webhooks sont envoyés à une URL et il est peu probable que vous connaissiez l'URL de votre ordinateur. De plus, un webhook Telegram nécessite que l'URL soit sécurisée (HTTPS).

Mais il existe une solution à ce problème : [ngrok](https://ngrok.com/). ngrok est un outil qui expose votre environnement local au monde. [Téléchargez ngrok](https://ngrok.com/download), installez-le et lancez-le avec le port sur lequel votre serveur est en cours d'exécution. Mon serveur est en cours d'exécution sur le port `8000`, donc je devrais exécuter dans une console

```
/path/to/ngrok http 8000
```

Ensuite, ngrok devrait vous donner une URL que vous pouvez utiliser pour configurer un webhook.

### Accueillir un utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/g5chjEivn8kFMGCWNKvl1x5FmYxWRaXlfPgX)

Maintenant que vous êtes prêt à développer, accueillons notre utilisateur — il l'attend.

Une fois que l'utilisateur clique sur « Start », votre Telegram enverra une mise à jour à l'URL de votre serveur. Les parties intéressantes de la mise à jour devraient ressembler à ceci :

```
{    "message": {        "chat": {            "id": 457        },		"text": "/start uEDbtJFHxKc",    }}
```

C'est le moment idéal pour associer l'utilisateur en utilisant le texte du message. Il y a aussi une information intéressante, l'ID de chat. L'ID de chat est ce dont nous avons besoin pour envoyer un message à cet utilisateur. Telegram a un point de terminaison API pour envoyer un message qui ressemble à ceci `https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}`. Je ne suis pas sûr de devoir expliquer comment l'utiliser, mais voici à quoi ressemble mon code qui traite le webhook :

```
import jsonimport requestsdef callback(request):    body = json.loads(request.body)    text = body['message']['text']    token = text.split(' ')[-1]    associate_user_by_token(token)    bot_key = os.environ.get('TELEGRAM_API_KEY')    chat_id = body['message']['chat']['id']	text = "Bienvenue !"	send_message_url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={text}'	requests.post(send_message_url)
```

Si nous envoyons un message de bienvenue après que l'utilisateur a cliqué sur le célèbre bouton « Start », l'utilisateur n'aura aucun doute sur le fait que tout fonctionne ou non.

### Envoyer des notifications push

![Image](https://cdn-media-1.freecodecamp.org/images/xfdeU5lYWIBYfeZ9wjFxW6x1zxjVNLnMvB2P)

Enfin, nous arrivons au point pour lequel nous faisons tout cela — les notifications push. Vous pouvez vouloir notifier l'utilisateur sur certaines informations qui se sont produites dans votre application. Par exemple, quelqu'un a aimé la publication de l'utilisateur ou autre chose. J'utilise Telegram pour notifier les [nouvelles sorties musicales](https://musicnotifier.com/) des artistes préférés de l'utilisateur.

Vous savez déjà comment envoyer des notifications. Vous devez simplement envoyer un message en utilisant `[https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}](https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}.)`[.](https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}.)

Bien sûr, si vous prévoyez d'envoyer des notifications non seulement lorsque l'utilisateur interagit avec le bot, vous devez sauvegarder `chat_id` dans votre base de données.

Vous pouvez également vouloir inclure des liens ou d'autres formats dans votre message. Dans ce cas, vous devrez ajouter un autre paramètre à l'URL d'envoi de message, `parse_mode`. Il y a 2 options de parsing : Markdown ou HTML. J'utilise Markdown car je le trouve plus simple à utiliser. Si vous n'êtes pas familier avec Markdown, vous pouvez utiliser HTML, mais je vous recommande de lire [à quel point Markdown est facile](https://www.markdownguide.org/basic-syntax).

Voici à quoi ressemble l'URL d'envoi de message avec le paramètre `parse_mode` `[https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}&parse_mode=markdown](https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}&parse_mode=markdown.)`[.](https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}&parse_mode=markdown.)

J'ajoute des liens aux nouvelles sorties dans le texte des notifications comme ceci `{release.date}: {release.artist.name} - [{release.title}]({release.url})`. Vous pouvez lire plus sur la façon de formater vos messages [ici](https://core.telegram.org/bots/api#formatting-options).

De plus, il y a [plus de paramètres disponibles](https://core.telegram.org/bots/api#sendmessage) pour l'URL d'envoi de message comme `disable_notification`. Il y a toujours un endroit à explorer.

### Conclusion

Maintenant, vous devriez savoir comment

* créer un bot dans Telegram en utilisant BotFather
* vérifier les mises à jour (et quelle est la meilleure façon — webhooks ou polling)
* associer un utilisateur en utilisant le deep linking
* envoyer un message de bienvenue et continuer à envoyer des notifications
* formater les messages que vous envoyez

Espérons que cet article vous a été utile. Il s'agit de la cinquième partie d'une série d'articles sur [MuN](http://musicnotifier.com/). Restez à l'écoute pour la partie 6. Vous pouvez trouver [le code de ce projet](https://github.com/hmlON/mun), ainsi que mes autres projets, sur ma [page GitHub](https://github.com/hmlON). Laissez vos commentaires ci-dessous et suivez-moi si vous avez aimé cet article.

_Publié à l'origine sur [https://kholinlabs.com/telegram-push-notifications](https://kholinlabs.com/telegram-push-notifications) le 12 février 2019._