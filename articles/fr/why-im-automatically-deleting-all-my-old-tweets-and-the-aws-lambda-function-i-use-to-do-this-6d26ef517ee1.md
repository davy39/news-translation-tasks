---
title: Pourquoi je supprime automatiquement tous mes anciens tweets, et la fonction
  AWS Lambda que j'utilise pour le faire
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2018-05-20T19:31:21.000Z'
originalURL: https://freecodecamp.org/news/why-im-automatically-deleting-all-my-old-tweets-and-the-aws-lambda-function-i-use-to-do-this-6d26ef517ee1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g1pmPaZgQ3vJAQe_Nh6Ejw.jpeg
tags:
- name: AWS
  slug: aws
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
seo_title: Pourquoi je supprime automatiquement tous mes anciens tweets, et la fonction
  AWS Lambda que j'utilise pour le faire
seo_desc: 'From now on, my tweets are ephemeral. Here’s why I’m deleting all my old
  tweets, and the AWS Lambda function I’m using to do all this for free.

  Stuff and opinions

  I’ve only been a one-bag nomad for a little over a year and a half. Before that,
  I live...'
---

Désormais, mes tweets sont éphémères. Voici pourquoi je supprime tous mes anciens tweets, et la fonction AWS Lambda que j'utilise pour le faire gratuitement.

### Objets et opinions

Je ne suis une nomade avec un seul sac que depuis un peu plus d'un an et demi. Avant cela, je vivais comme la plupart des gens dans un appartement ou une maison. Je possédais des meubles, plus de vêtements que nécessaire, et assez de "choses" pour remplir au moins quelques cartons de déménagement. Si je devais vivre ailleurs, que ce soit pour l'école, la famille ou le travail, je faisais mes valises et emportais tout avec moi. Au fil des années, j'ai accumulé de plus en plus de choses.

Adopter ce que beaucoup appellent un mode de vie minimaliste a rapidement changé beaucoup de mes opinions de longue date. Donner toutes mes affaires (une idée que je trouvais autrefois intéressante en principe mais un peu ridicule en pratique) est devenu normal. Pour moi, maintenant, il est normal de ne pas posséder des choses que je n'utilise pas régulièrement. Je ne garde pas d'étagères remplies de vieux livres, de vaisselle, de vêtements ou de jouets d'enfance, car ces objets ne sont plus pertinents pour moi. Je garde simplement de bons souvenirs, à la place.

Imaginez, un instant, que je vive toujours dans une maison. Imaginez que dans cette maison, sur le frigo, il y a un dessin que j'ai fait quand j'avais six ans. Dans le coin inférieur droit de ce dessin, griffonné au crayon vert, on peut lire "le brocoli est nul — Victoria, 6 ans".

Si vous étiez dans ma maison et que vous voyiez ce dessin sur le frigo, penseriez-vous que l'affirmation "le brocoli est nul" représente une opinion exacte et actuelle sur le brocoli ? Bien sûr que non. J'avais six ans quand j'ai écrit cela. J'ai eu tout le temps de changer d'avis.

### Les réseaux sociaux ne sont pas sociaux

J'ai une amie que je connais depuis que nous étions toutes les deux à la maternelle. Nous avons traversé l'école primaire ensemble, puis nous nous sommes parlé et vues à des occasions irrégulières au fil des années. Nous sommes maintenant toutes les deux adultes. Parfois, quand nous discutons, nous nous rappelons un souvenir amusant de notre jeunesse. La nature de la mémoire étant ce qu'elle est, je n'ai aucune illusion que ce que nous nous rappelons est raconté avec beaucoup de précision. Nos impressions des choses qui se sont passées — les erreurs que nous avons commises et les moments de victoire — sont colorées par les expériences que nous avons eues depuis, et tout ce que nous avons appris. Un moment gênant à l'anniversaire d'un camarade de classe devient un exemple d'un enfant apprenant à socialiser, au lieu du moment de honte mondial qu'il a probablement ressenti à l'époque.

C'est ainsi que fonctionne la mémoire. En un sens, elle est mise à jour, et c'est très bien ainsi. Les personnes vivant dans de petites communautés se souviennent des choses que leur voisin a faites il y a de nombreuses années, mais les rappellent dans le contexte de qui est leur voisin maintenant, et de ce que leur relation actuelle est. Cette recoloration de l'histoire est une partie importante de la manière dont les gens guérissent, prennent de bonnes décisions et socialisent.

Les réseaux sociaux ne font pas cela. Votre tweet parfaitement préservé de cinq jours ou cinq ans peut être rappelé avec une précision absolue. Pour la plupart des gens, ce n'est pas particulièrement inquiétant. Nous avons tendance à tweeter des choses assez banales — des choses qui nous viennent à l'esprit quand nous nous ennuyons et voulons que quelqu'un nous remarque. Individuellement, généralement, nos anciens tweets sont assez insignifiants. En aggregate, cependant, ils brossent un tableau assez complet des pensées aléatoires et involontairement révélatrices d'une personne. C'est le problème.

L'hypothèse faite sur les choses écrites sur les réseaux sociaux et sur Twitter en particulier est une hypothèse très différente de celle que vous pourriez faire sur les griffonnages de quelqu'un sur un bloc-notes de la semaine dernière. Je ne cherche pas à spéculer pourquoi — j'ai simplement vu assez de cas où quelqu'un se fait publiquement critiquer pour quelque chose qu'il a posté il y a des années pour savoir que cela arrive. C'est étrange. Si vous ne supposeriez pas qu'un griffonnage sur un bloc-notes de la semaine dernière ou un dessin au crayon de décennies en arrière reflète l'essence de qui quelqu'un est maintenant, pourquoi supposeriez-vous qu'un ancien tweet le fait ?

Vous n'êtes pas la même personne que vous étiez le mois dernier — vous avez vu des choses, lu des choses, compris et appris des choses qui, d'une certaine manière, vous ont changé. Bien qu'une personne puisse avoir le même sens de soi et d'identité tout au long de sa vie, même cela grandit et change au fil des années. Nous changeons nos opinions, nos désirs, nos habitudes. Nous ne sommes pas des êtres stagnants, et nous ne devrions pas nous laisser représenter comme tels, même involontairement.

### Tweets éphémères

Si vous regardez ma page de profil Twitter aujourd'hui, vous y verrez moins de tweets que vous n'avez de doigts (je l'espère). J'utilise [ephemeral](https://github.com/victoriadrake/ephemeral/) — un utilitaire léger que j'ai écrit pour une utilisation sur [AWS Lambda](https://aws.amazon.com/lambda/) — pour supprimer tous mes tweets de plus de quelques jours. Je fais cela pour la même raison que je ne garde pas les choses que je n'utilise plus — ces choses ne sont plus pertinentes pour moi. Elles ne me représentent pas non plus.

Le code qui compose ephemeral est écrit en Go. AWS Lambda crée un environnement pour chaque fonction Lambda, donc ephemeral utilise des variables d'environnement pour vos clés privées de l'API Twitter et l'âge maximum des tweets que vous souhaitez conserver, représenté en heures, comme `72h`.

```js
var (
	consumerKey       = getenv("TWITTER_CONSUMER_KEY")
	consumerSecret    = getenv("TWITTER_CONSUMER_SECRET")
	accessToken       = getenv("TWITTER_ACCESS_TOKEN")
	accessTokenSecret = getenv("TWITTER_ACCESS_TOKEN_SECRET")
	maxTweetAge       = getenv("MAX_TWEET_AGE")
	logger            = log.New()
)
func getenv(name string) string {
	v := os.Getenv(name)
	if v == "" {
		panic("missing required environment variable " + name)
	}
	return v
}
```

Le programme utilise la bibliothèque [anaconda](https://github.com/ChimeraCoder/anaconda). Il récupère votre timeline jusqu'à la limite de l'API Twitter de 200 tweets par requête, puis compare la date de création de chaque tweet à votre variable `MAX_TWEET_AGE` pour décider s'il est assez ancien pour être supprimé. Après avoir supprimé tous les tweets expirés, la fonction Lambda se termine.

```
func deleteFromTimeline(api *anaconda.TwitterApi, ageLimit time.Duration) {
	timeline, err := getTimeline(api)
if err != nil {
		log.Error("Could not get timeline")
	}
	for _, t := range timeline {
		createdTime, err := t.CreatedAtTime()
		if err != nil {
			log.Error("Couldn't parse time ", err)
		} else {
			if time.Since(createdTime) > ageLimit {
				_, err := api.DeleteTweet(t.Id, true)
				log.Info("DELETED: Age - ", time.Since(createdTime).Round(1*time.Minute), " - ", t.Text)
				if err != nil {
					log.Error("Failed to delete! ", err)
				}
			}
		}
	}
	log.Info("No more tweets to delete.")
}
```

Lisez le code complet [ici](https://github.com/victoriadrake/ephemeral/blob/master/main.go).

Pour un cas d'utilisation comme celui-ci, AWS Lambda a un niveau gratuit qui ne coûte rien. Si vous êtes développeur à quelque niveau que ce soit, c'est un outil extrêmement utile à maîtriser. Pour un guide complet avec des captures d'écran sur la façon de configurer une fonction Lambda qui tweete pour vous, vous pouvez lire [cet article](https://victoria.dev/verbose/running-a-free-twitter-bot-on-aws-lambda/). La configuration pour ephemeral est la même, elle a simplement une fonction opposée. :)

J'ai forké ephemeral à partir de [Harold](https://github.com/adamdrake/harold) d'Adam Drake, un outil Twitter qui a de nombreuses fonctions utiles au-delà de garder votre timeline épurée. Si vous avez plus de 200 tweets à supprimer lors du premier passage, veuillez utiliser Harold pour cela d'abord. Vous pouvez exécuter Harold avec le flag `deletetimeline` depuis votre terminal.

Vous voudrez peut-être d'abord [télécharger tous vos tweets avant de les supprimer](https://twitter.com/settings/your_twitter_data) pour leur valeur sentimentale.

### Pourquoi utiliser Twitter du tout ?

En anticipation de la question, laissez-moi dire que oui, j'utilise Twitter autrement que comme un simple récipient que mes fonctions Lambda remplissent et vident. Il a ses avantages, principalement liés à ce que je perçois être son but initial : être un moyen de communication quasi instantané pour des morceaux d'information courts et digestes atteignant un large public.

Je l'utilise comme un moyen de suivre ce qui se passe maintenant. Je l'utilise pour commenter, plaisanter et compatir avec les tweets des personnes que je suis maintenant. En gardant ma timeline limitée aux quelques jours les plus récents, j'ai l'impression d'utiliser Twitter plus comme il était censé être utilisé : une façon de rejoindre la conversation et de voir ce qui se passe dans le monde maintenant — au lieu d'être simplement un autre endroit pour accumuler plus de "choses".

Merci d'avoir lu ! Si vous souhaitez en savoir plus sur la façon dont j'améliore ma vie avec la technologie, vous pouvez me suivre ici ainsi que consulter mon blog où j'explique le codage avec plus de gribouillis mal dessinés de nourriture : [Victoria.dev](https://victoria.dev)

J'espère que vous passerez une excellente journée ! :)