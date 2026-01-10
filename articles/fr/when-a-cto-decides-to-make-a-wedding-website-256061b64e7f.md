---
title: Quand un CTO décide de créer un site web de mariage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-29T15:17:33.000Z'
originalURL: https://freecodecamp.org/news/when-a-cto-decides-to-make-a-wedding-website-256061b64e7f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vVOogQpEJW26iPDp.png
tags:
- name: open source
  slug: open-source
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: weddings
  slug: weddings
seo_title: Quand un CTO décide de créer un site web de mariage
seo_desc: 'By Cory Zue

  An open-source, responsive, Django-powered wedding website and invitation + guest
  management system with 250+ commits, unit tests, and more.

  When my wife and I got married in the summer of 2016 I decided I wanted to make
  our own wedding w...'
---

Par Cory Zue

#### Un site web de mariage et un système de gestion des invités open-source, responsive, alimenté par Django avec 250+ commits, des tests unitaires, et plus.

Quand ma femme et moi nous sommes mariés à l'été 2016, j'ai décidé de créer notre [propre site web de mariage](http://www.coryandro.com/) à partir de zéro.

Pourquoi ne pas simplement utiliser quelque chose comme Wedding Wire ou Squarespace, me direz-vous ?

Principalement parce que je pensais que ce serait un petit projet amusant. En tant que développeur web expérimenté (à l'époque j'étais CTO de [Dimagi](http://www.dimagi.com/)), j'aime construire des choses et cela semblait être une bonne opportunité de passer quelques jours à assembler un peu de HTML et de CSS et à lui donner une touche vraiment personnelle.

Bien sûr, plus vite que vous ne pouvez dire « dérive de portée », une chose en a mené à une autre et bientôt j'avais construit une application plutôt significative qui comprenait :

* Un site web de mariage traditionnel, responsive, sur une seule page
* Une application complète de gestion des invités
* Un framework d'email pour envoyer les save-the-dates
* Un framework d'email pour les invitations et un système intégré de RSVP
* Un tableau de bord en direct pour les invités

18 mois et 250 commits plus tard, j'ai pensé qu'il serait amusant d'écrire un peu sur le projet et de le partager avec le monde.

**Si vous voulez juste voir le code, vous pouvez [le récupérer sur github](https://github.com/czue/django-wedding-website/).**

![Image](https://cdn-media-1.freecodecamp.org/images/0*gm_auZRogIqkl7VF.png)
_Chronologie des commits pour le projet_

![Image](https://cdn-media-1.freecodecamp.org/images/0*8Uwc_TQj2j4bVLEV.png)
_Mon temps total passé sur la planification du mariage (y compris le site web)_

### Le Site Web Statique de Mariage

Au début, le plan était simplement de créer un site web de mariage standard, banal. Vous savez, le genre de truc standard « voici notre histoire de fiançailles » et « voici les informations sur l'événement ».

À l'époque, j'avais beaucoup d'expérience dans la création de sites Django et pas beaucoup d'expérience avec d'autres frameworks, alors j'ai décidé de simplement faire le site en Django même si je n'étais pas sûr d'avoir besoin d'un backend. Si je ne faisais _que_ le site web statique de mariage, un meilleur choix aurait probablement été un [générateur de site statique](https://www.staticgen.com/), mais au fond de moi, je pense que je savais que je voulais faire plus avec le projet.

Pour le site, je savais que je voulais qu'il soit visuellement attrayant — au moins autant qu'un développeur backend handicapé par le design comme moi pouvait le faire — et qu'il soit adapté aux mobiles. Je savais aussi que je voulais une application sur une seule page parce que c'était à la mode. J'ai finalement décidé d'utiliser [Twitter Bootstrap](http://getbootstrap.com/) et j'ai modifié un [thème gratuit](https://blackrockdigital.github.io/startbootstrap-creative/) pour qu'il me plaise.

C'était tout du HTML/CSS/JS/Bootstrap3 assez standard, donc je ne vous ennuyerai pas avec les détails. Si vous voulez voir le produit fini, vous pouvez le faire sur notre [site en direct](http://www.coryandro.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*sgNmW39JMaa57_BK.png)
_Un des éléments de l'interface de navigation du site._

### Comment la Dérive de Fonctionnalités Commence

Quand nous avons commencé à réfléchir à nos save-the-dates, la première décision que nous avons prise a été de les envoyer électroniquement. Cela semblait plus efficace, plus rentable, plus écologique, et bien, bien plus facile que d'essayer d'obtenir les adresses de tous nos amis et de notre famille et d'envoyer des choses à la main. (Surtout depuis notre nouvelle maison en Afrique du Sud !)

**Comme beaucoup de décisions possiblement mauvaises, celle-ci a commencé avec cinq mots très simples : « ne serait-ce pas cool si… ? »**

Dans notre cas, la phrase était « ne serait-ce pas cool si, au lieu d'utiliser quelque chose comme evite ou paperless post, nous envoyions nous-mêmes les save-the-dates ? Ensuite, nous pourrions faire quelque chose de beaucoup plus personnalisé et amusant, comme envoyer différentes versions à différentes personnes. »

_Hmm, me suis-je dit. Cela semble assez simple. Nous devons simplement créer quelques modèles d'email, puis tout ce dont nous avons besoin est une liste de tous nos invités et de leurs adresses email, puis nous pourrions — soit aléatoirement, soit explicitement — les assigner à un modèle et l'envoyer._

_Cela ressemble à un modèle super simple avec un nom, un email et quelques autres propriétés de suivi. Je parie que je peux le faire en une heure._

### Entrée en Scène du Modèle Invité

Si nous allions envoyer des emails à nos invités, nous devions les suivre. Heureusement, puisque j'avais choisi d'utiliser Django, cela était aussi simple que de créer un modèle de base de données.

Voici ma première tentative du modèle `Guest`.

```python
class Guest(models.Model):
    name = models.TextField()
    email = models.TextField()
    save_the_date_sent = models.BooleanField(default=False)
    save_the_date_opened = models.BooleanField(default=False)
    invited = models.BooleanField(default=False)
    attending = models.NullBooleanField(default=None)
```

Nom, email, deux champs pour suivre si nous avions envoyé le save-the-date et s'ils l'avaient ouvert (une fonctionnalité qui a été construite plus tard). Également un champ pour suivre s'ils étaient officiellement invités — au début, nous avions certaines personnes qui étaient incertaines (désolé, les tantes folles !) — et s'ils assistaient. Contrairement aux autres, attending utilisait un `NullBooleanField` au lieu d'un `BooleanField` afin que nous puissions représenter l'absence d'information avec `None`.

Facile comme bonjour.

### Dérive Supplémentaire : C'est l'Heure de la Fête

Le modèle `Guest` était un bon début, mais bientôt nous avions un problème : que faire des personnes dont nous n'avions pas les emails ? Ou des personnes qui n'avaient même pas d'email, comme les enfants de mes frères ? Nous avions besoin d'un moyen de représenter ces personnes, mais nous ne pouvions pas suivre leurs réponses individuellement. Ainsi est venu le modèle `Party` — pour aider à représenter une collection de `Guests`.

J'ai déplacé la plupart des métadonnées du modèle `Guest` vers le modèle `Party` et j'ai simplement laissé `name`, `email`, et `is_attending` sur les `Guests`. J'ai également décidé de séparer le prénom et le nom de famille à ce stade — je pense surtout pour correspondre au format que nous avions dans notre feuille de calcul des invités. Nous avons également décidé d'ajouter un « type » au champ party pour représenter si nos invités étaient « formels » ou « amusants » — puisque nous voulions envoyer différents save-the-dates à chaque groupe.

Voici les versions mises à jour des modèles `Guest` et `Party` :

```python
# ceux-ci détermineront la formalité par défaut de la correspondance
ALLOWED_TYPES = [
    ('formal', 'formal'),
    ('fun', 'fun')
]

class Party(models.Model):
    """
    Une fête se compose d'un ou plusieurs invités.
    """
    name = models.TextField()
    type = models.CharField(max_length=10, choices=ALLOWED_TYPES)
    save_the_date_sent = models.DateTimeField(null=True, default=None)
    save_the_date_opened = models.DateTimeField(null=True, default=None)
    is_invited = models.BooleanField(default=False)
    is_attending = models.NullBooleanField(default=None)

class Guest(models.Model):
    """
    Un invité unique
    """
    party = models.ForeignKey(Party)
    first_name = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    email = models.TextField()
    is_attending = models.NullBooleanField(default=None)
```

### Importateur d'Invités

Nous avions précédemment suivi notre liste d'invités dans une feuille Google, et il n'était pas question que nous réentrions tous ces invités à la main. _Nous avions besoin d'un importateur._

J'ai fini par créer un [processeur CSV assez basique et simple](https://github.com/czue/django-wedding-website/commit/8928de5dc266da86aad5d36d01a916103e8278c6), bien qu'une chose importante à son sujet était qu'il était [idempotent](https://en.wikipedia.org/wiki/Idempotence) — ce qui signifie qu'il pouvait être exécuté en toute sécurité plusieurs fois de suite. Nous modifiions toujours notre liste d'invités dans Google Sheets et avions besoin de pouvoir l'importer continuellement par-dessus la base de données existante. Puisque cela semblait important pour que cette partie soit sans erreur, j'ai également décidé d'ajouter quelques tests unitaires en utilisant [un ensemble d'invités d'exemple de Game of Thrones](https://github.com/czue/django-wedding-website/blob/8928de5dc266da86aad5d36d01a916103e8278c6/guests/tests/data/guests-test.csv).

```python
class GuestImporterTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(GuestImporterTest, cls).setUpClass()
        cls.path = os.path.join(os.path.dirname(__file__), 'data', 'guests-test.csv')

    def test_import(self):
        import_guests(self.path)
        self.assertEqual(2, Party.objects.count())
        self.assertEqual(4, Guest.objects.count())
        the_starks = Guest.objects.filter(party__name='The Starks')
        self.assertEqual(3, the_starks.count())

    def test_import_idempotent(self):
        for i in range(3):
            import_guests(self.path)
            self.assertEqual(2, Party.objects.count())
            self.assertEqual(4, Guest.objects.count())
            the_starks = Guest.objects.filter(party__name='The Starks')
            self.assertEqual(3, the_starks.count())
```

### Enfin Prêt à Commencer sur les Save the Dates

Après avoir mis les modèles dans un état où ils pouvaient supporter tout ce que nous voulions faire, il était enfin temps de commencer à travailler sur nos save-the-dates.

La première étape consistait à trouver un modèle d'email qui fonctionnerait sur tous les clients — un problème qui est notoirement douloureux. Ma femme (également une ancienne développeuse web) en a trouvé un sur [litmus.com](https://litmus.com/resources/free-responsive-email-templates) et l'a personnalisé selon nos besoins.

Puisque nous voulions envoyer différents modèles à différents invités, nous avons dû extraire les parties du modèle que nous voulions personnaliser. Finalement, nous avons terminé avec un seul modèle avec quelques parties personnalisables : une image d'en-tête, une image principale, une couleur de fond et une couleur de texte. C'est beaucoup de code de compatibilité désordonné, donc je ne le collerai pas ici, mais tous les modèles sont [sur github ici](https://github.com/czue/django-wedding-website/tree/master/guests/templates/guests/email_templates).

Nous avons réfléchis ensemble à quelques idées de modèles différentes et avons finalement abouti à six — deux « standard » avec de belles photos de nous, trois qui étaient plus drôles/amusantes et une qui était une blague interne qui ne serait pertinente que pour les personnes qui travaillaient pour notre entreprise.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3R6guLXK9VUHoLhX.png)
_Un de nos modèles finaux de save-the-date. Celui-ci était pour mes amis américains (nous nous sommes mariés au Canada)._

Une fois cette infrastructure en place, nous avons simplement ajouté tous nos save-the-dates à une liste contenant les différentes propriétés configurables, et écrit un peu de code pour insérer ces valeurs dans un modèle partagé :

```python
SAVE_THE_DATE_CONTEXT_MAP = {
    'lions-head': {
        'title': "Lion's Head",
        'header_filename': 'hearts.png',
        'main_image': 'lions-head.jpg',
        'main_color': '#fff3e8',
        'font_color': '#666666',
    },
    'canada': {
        'title': 'Canada!',
        'header_filename': 'maple-leaf.png',
        'main_image': 'canada-cartoon-resized.jpg',
        'main_color': '#ea2e2e',
        'font_color': '#e5ddd9',
    },
    # autres modèles omis pour plus de concision
}
```

Ensuite, nous avons écrit une fonction simple pour choisir un modèle semi-aléatoirement en fonction de nos critères définis (que vous pouvez voir dans les commentaires) :

```python
def get_template_id_from_party(party):
    if party.type == 'formal':
        # tous les invités formels reçoivent des invitations formelles
        return random.choice(['lions-head', 'ski-trip'])
    elif party.type == 'dimagi':
        # tous les dimagis non formels reçoivent des invitations dimagi
        return 'dimagi'
    elif party.type == 'fun':
        all_options = SAVE_THE_DATE_CONTEXT_MAP.keys()
        all_options.remove('dimagi')
        if party.category == 'ro':
            # ne pas envoyer l'invitation canada à la foule de ro
            all_options.remove('canada')
        # sinon choisir aléatoirement parmi toutes les options pour tout le monde
        return random.choice(all_options)
    else:
        return None
```



En tant qu'étape finale avant l'envoi, nous avons également décidé de faire de la page d'accueil de notre site un save-the-date sélectionné aléatoirement (puisque tout le monde ne recevrait qu'un seul modèle et nous voulions que les gens voient les autres). Nous avons finalement [déplacé cette page ici](http://www.coryandro.com/save-the-date/) (si vous actualisez, vous en obtiendrez un nouveau).

```python
def save_the_date_random(request):
    template_id = random.choice(SAVE_THE_DATE_CONTEXT_MAP.keys())
    context = get_save_the_date_context(template_id)
    context['email_mode'] = False
    return render(request, SAVE_THE_DATE_TEMPLATE, context=context)
```

Vous pouvez voir l'ensemble final des save-the-dates ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WJKtyQB4IH99KTUt.png)
_L'ensemble complet des save-the-dates._

Enfin, nous avons écrit une commande de gestion pour gérer l'envoi réel qui appelait une fonction qui ressemble à ceci :

```python
def send_all_save_the_dates(test_only=False, mark_as_sent=False):
    to_send_to = Party.in_default_order().filter(is_invited=True, save_the_date_sent=None)
    for party in to_send_to:
        send_save_the_date_to_party(party, test_only=test_only)
        if mark_as_sent:
            party.save_the_date_sent = datetime.now()
            party.save()
```

Après beaucoup de tests, nous étions confiants que tout était prêt et il était temps d'appuyer sur le gros bouton effrayant « envoyer » (ou dans ce cas, exécuter `./manage.py send_save_the_dates --send --mark-sent`).

Presque immédiatement, nous avons commencé à recevoir des réponses amusantes de nos amis parlant des save-the-dates et c'était amusant de les voir se confondre en décrivant les différents modèles.

Dans l'ensemble, grâce à des tests et une préparation approfondis, ce fut un grand succès !

Bien que je devrais noter que, probablement sans surprise, tout cela a pris beaucoup plus de temps que prévu. _Et nous n'en étions qu'au début !_

### Invitations

Après quelques mois de temps de repos bien apprécié, la date limite des trois mois avant laquelle vous êtes censé envoyer les invitations a commencé à approcher. Nous nous sentions globalement bien par rapport à l'expérience des save-the-dates, nous avons donc décidé une fois de plus de faire les invitations et les RSVPs nous-mêmes. Cela a ajouté beaucoup de portée supplémentaire. En particulier, nous avons décidé que nous voulions :

* Pouvoir suivre les ouvertures d'invitations
* Permettre aux gens de RSVP sur notre site web
* Ne pas obliger les gens à se connecter ou à entrer leurs emails
* Remplir automatiquement les noms des invités à partir du lien d'invitation
* Permettre aux gens de sélectionner des repas et de spécifier la présence pour chaque invité

### Mise à Jour des Modèles

Toutes ces fonctionnalités supplémentaires signifiaient une autre mise à jour significative des modèles. Voici les modèles `Party` et `Guest` finaux après que les invitations aient été faites :

```python
class Party(models.Model):
    """
    Une fête se compose d'un ou plusieurs invités.
    """
    name = models.TextField()
    type = models.CharField(max_length=10, choices=ALLOWED_TYPES)
    category = models.CharField(max_length=20, null=True, blank=True)
    save_the_date_sent = models.DateTimeField(null=True, blank=True, default=None)
    save_the_date_opened = models.DateTimeField(null=True, blank=True, default=None)
    invitation_id = models.CharField(max_length=32, db_index=True, default=_random_uuid, unique=True)
    invitation_sent = models.DateTimeField(null=True, blank=True, default=None)
    invitation_opened = models.DateTimeField(null=True, blank=True, default=None)
    is_invited = models.BooleanField(default=False)
    rehearsal_dinner = models.BooleanField(default=False)
    is_attending = models.NullBooleanField(default=None)
    comments = models.TextField(null=True, blank=True)

class Guest(models.Model):
    """
    Un invité unique
    """
    party = models.ForeignKey(Party)
    first_name = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    is_attending = models.NullBooleanField(default=None)
    meal = models.CharField(max_length=20, choices=MEALS, null=True, blank=True)
    is_child = models.BooleanField(default=False)
```

Le changement le plus important a été l'ajout de l'`invitation_id` au modèle `Party`. Il s'agissait d'un GUID de 32 caractères que nous avons utilisé dans nos URL d'invitation pour empêcher les gens de pouvoir deviner les liens d'invitation des autres (ce qui aurait été facile si nous avions utilisé des entiers standard). L'`invitation_id` a également résolu le problème de permettre aux invités de RSVP sans nécessiter de connexions ; chaque fête aurait simplement un identifiant d'invitation unique que seuls ils connaîtront et qui pourrait être utilisé pour RSVP.

En plus de l'`invitation_id`, les Parties ont également obtenu quelques métadonnées sur le moment où les invitations ont été envoyées et ouvertes et un champ de commentaires pour que nos invités puissent y mettre des vœux.

Pendant ce temps, les `Guests` ont obtenu deux champs supplémentaires liés aux RSVPs — un pour la sélection des repas, et un autre pour représenter s'ils étaient des enfants ou non. Nous avons dû ajouter ce dernier champ car nous ne voulions pas offrir de sélection de repas aux enfants, et cela nous a également aidé à mieux planifier nos comptes finaux et nos coûts.

### Email d'Invitation et Suivi des Ouvertures

Nous allions initialement implémenter un [pixel de suivi](https://skillcrush.com/2012/07/19/tracking-pixel/) dans les emails d'invitation pour voir s'ils étaient ouverts ou non, mais nous avons finalement opté pour une approche plus simple. Nous avons décidé de faire de notre email d'invitation réel un « teaser » qui vous menait à la « vraie » invitation — qui était votre lien personnalisé et votre page RSVP. Ensuite, puisque nos invitations étaient déjà des liens individualisés par fête, nous avons simplement décidé de traiter l'ouverture de ce lien comme l'ouverture de l'invitation.

Une fois cela décidé, il était assez facile d'ajouter un peu de code pour mettre à jour le champ de suivi lorsque la page était ouverte pour la première fois.

```python
def invitation(request, invite_id):
    party = guess_party_by_invite_id_or_404(invite_id)
    if party.invitation_opened is None:
        # mise à jour si c'est la première fois que l'invitation est ouverte
        party.invitation_opened = datetime.utcnow()
        party.save()
```

Pour l'email lui-même, nous avons fini par utiliser essentiellement le même modèle que les save-the-dates, sauf que cette fois l'email devait être intelligent pour injecter le bon lien dans le mail en fonction de la personne à qui il était envoyé — un processus simple avec le rendu de modèle de Django.

![Image](https://cdn-media-1.freecodecamp.org/images/0*S7pE-cB4_5HohvFp.png)
_Notre email d'invitation. Nous avons trouvé [une image en ligne qui nous ressemblait un peu](https://www.iconfinder.com/icons/372878/boyfriend_girlfriend_heart_marriage_sweetheart_valentines_wedding_icon" rel="noopener" target="_blank" title=") pour 1 $._

### La Page d'Invitation et de RSVP

La page d'invitation/RSVP ([exemple ici](http://coryandro.com/invite/b2ad24ec5dbb4694a36ef4ab616264e0/)) était assez simple (je suis plus un développeur backend, donc j'ai dû garder les choses assez simples côté UI).

En gros, elle se compose d'une courte vidéo intégrée que nous avons faite, de quelques détails sur l'événement et d'un formulaire RSVP. Le bit le plus délicat était la validation et la logique des repas, qui était la suivante :

* Vous devez RSVP pour tous les invités de votre fête
* Vous n'êtes autorisé à sélectionner un repas que si vous RSVP « oui »
* Les enfants n'ont pas de repas

J'ai utilisé l'excellent [Validator for Bootstrap 3 library](https://github.com/1000hz/bootstrap-validator) pour l'UI et la plupart de la logique javascript, et j'ai simplement dû ajouter un peu de JavaScript manuel pour connecter le workflow d'assistance/repas :

```javascript
$(function () {
    // activer/désactiver les choix de repas en fonction de la présence
    $("input.attending-radio").change(function (e) {
        var target = $(e.target);
        if (target.closest('.form-group').data('is-child') === "True") {
            // ne pas tenter de mettre à jour les repas pour les enfants, qui n'en ont pas.
            return;
        }
        var value = target.attr('value');
        var mealButtonContainer = target.closest('.form-group').next('.form-group');
        var mealButtons = mealButtonContainer.find('[type=radio]');
        if (value === 'yes') {
            mealButtonContainer.removeClass('text-muted');
            mealButtons.each(function (index, button) {
                button.disabled = false;
                button.required = true;
            });
        } else if (value === "no") {
            mealButtonContainer.addClass('text-muted');
            mealButtons.each(function (index, button) {
                button.checked = false;
                button.disabled = true;
                button.required = false;
            });
        }
        // recharger la validation
        $(document.forms[0]).validator('destroy');
        $(document.forms[0]).validator();
    });
});
```

Voici à quoi ressemblait cette partie :

![Image](https://cdn-media-1.freecodecamp.org/images/0*uLCWK_dtJYp-9nVt.png)
_Belle UI et activation/désactivation automatique du bouton de soumission grâce à [Validator for Bootstrap 3](https://github.com/1000hz/bootstrap-validator" rel="noopener" target="_blank" title=")._

Enfin, après avoir soumis votre formulaire — qui, bien sûr, met à jour votre présence et vos préférences de repas en conséquence — nous vous avons mené à une page de confirmation personnalisée avec un merci et quelques autres informations.

![Image](https://cdn-media-1.freecodecamp.org/images/0*evj64A-okaQX9mIb.png)
_Ce que vous voyez après avoir RSVP_

### Envoi des Invitations

Une fois de plus, tout s'est incroyablement bien passé grâce à des tests approfondis et à plusieurs répétitions à blanc avant d'envoyer les vraies invitations. Il n'y a eu **aucun bug** rencontré par nos invités pendant le processus de RSVP, un fait dont je suis assez fier.

En revanche, à ce stade, j'avais passé bien plus de 40 heures de temps les soirs et les week-ends à construire le site.

### La Pièce Finale : un Tableau de Bord en Direct pour les Invités

Une fois que nous avons commencé à envoyer les invitations et que les RSVPs ont commencé à arriver, la dernière chose que nous voulions était un tableau de bord pour suivre les progrès de tout cela. Cela s'est avéré assez simple — juste quelques chiffres agrégés et des listes de personnes qui n'avaient pas répondu ou qui n'avaient pas vu l'invitation afin que nous puissions les relancer directement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6K42ZZZEZYLnjcXL.png)
_La vue du tableau de bord des invités._

Nous avons en fait beaucoup utilisé le tableau de bord ! C'était un excellent endroit pour voir nos chiffres de présence prévus, les comptes de repas et les listes de personnes que nous devions relancer pour obtenir des RSVPs. Voici un lien vers le [code de la vue du tableau de bord](https://github.com/czue/django-wedding-website/blob/master/guests/views.py#L31-L61).

> « J'ai trouvé cela super, super utile de connaître le nombre maximum possible de participants puisque nous devons fournir ces chiffres au lieu et qu'il y a des implications de coûts significatives. »

> _— Ma femme, Rowena_

### Conclusion

Si vous êtes arrivé jusqu'ici, vous avez probablement appris quelques choses sur Django, le type de travail qui entre dans la construction de quelque chose comme cela, et comment la portée s'immisce rapidement même dans les choses les plus simples.

Si vous êtes intéressé à utiliser le projet pour votre propre mariage, n'hésitez pas à nous contacter ! Tout est [sur Github](https://github.com/czue/django-wedding-website) et je suis heureux de travailler avec les gens pour le rendre plus convivial pour l'open-source.

Merci d'avoir lu !

— Cory

### À Propos de Moi

Je suis l'ancien CTO de Dimagi, où j'ai dirigé l'équipe qui fait [CommCare HQ](https://www.commcarehq.org/) — l'une des plus grandes bases de code Django dont j'ai connaissance — pendant 6 ans. Je développe des applications Django depuis 2007.

Je travaille actuellement sur un [modèle Django SaaS](https://www.saaspegasus.com/), ainsi que sur d'autres projets secondaires, y compris une application pour [créer des cartes de place imprimables en ligne](https://www.placecard.me/) et [une extension Chrome pour personnaliser votre écran de nouvel onglet avec vos propres photos](http://bit.ly/photostab).

_J'ai initialement publié cela sur mon blog à [www.placecard.me](https://www.placecard.me/django-wedding-website/).