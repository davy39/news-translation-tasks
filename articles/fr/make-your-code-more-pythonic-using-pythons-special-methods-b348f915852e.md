---
title: Rendez votre code plus « pythonique » en utilisant les méthodes spéciales de
  Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-22T20:15:03.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-more-pythonic-using-pythons-special-methods-b348f915852e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_vcMHRjT4BItOuz8LNA6FA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Rendez votre code plus « pythonique » en utilisant les méthodes spéciales
  de Python
seo_desc: 'By Marco Massenzio

  In his excellent Fluent Python book, Luciano Ramalho talks about Python’s “data
  model.” He gives some excellent examples of how the language achieves internal consistency
  through the judicious use of a well-defined API. In particul...'
---

Par Marco Massenzio

Dans son excellent livre [Fluent Python](http://amzn.to/29QsgTn), Luciano Ramalho parle du « modèle de données » de Python. Il donne quelques excellents exemples de la manière dont le langage atteint une cohérence interne grâce à l'utilisation judicieuse d'une API bien définie. En particulier, il discute de la manière dont les « [méthodes spéciales](https://docs.python.org/3/reference/datamodel.html#special-method-names) » de Python permettent la construction de solutions élégantes, qui sont concises et très lisibles.

Et bien que vous puissiez trouver d'innombrables exemples en ligne sur la manière d'implémenter les méthodes spéciales _itératives_ (___iter__()_ et autres), ici je voulais présenter un exemple de l'utilisation de deux des méthodes spéciales moins connues : ___del__()_ et ___call__()_.

Pour ceux qui sont familiers avec le C++, celles-ci implémentent deux motifs très familiers : le _destructeur_ et l'_objet fonction_ (aka, _operator()_).

### Implémenter une clé auto-destructrice

![Image](https://cdn-media-1.freecodecamp.org/images/lPGK0cKKFRjq4A--onWrbnrNLis8-6JaYNty)
_Crédit : [ke dickinson](https://www.flickr.com/photos/ke-dickinson/7159943526/in/photolist-bUGzLb-JXhz-8MMTUA-o8fGSq-9tdgxB-" rel="noopener" target="_blank" title=")_

Supposons que nous voulons concevoir une _clé de chiffrement_ qui sera à son tour chiffrée avec une _clé principale_ — et dont la valeur en « texte clair » ne sera utilisée que « en vol » pour chiffrer et déchiffrer nos données — mais qui sinon ne sera stockée que sous forme chiffrée.

Il y a de nombreuses raisons pour lesquelles vous pourriez vouloir faire cela, mais la plus courante est lorsque les données à chiffrer sont très volumineuses et prennent beaucoup de temps à chiffrer. Si la _clé principale_ est compromise, nous pourrions la révoquer puis rechiffrer les clés de chiffrement avec une nouvelle clé principale — tout cela sans subir la pénalité de temps associée au déchiffrement et au rechiffrement de plusieurs téraoctets de données.

En fait, le rechiffrement des clés de chiffrement peut être si peu coûteux en termes de calcul que cela pourrait être fait régulièrement, en faisant tourner la _clé principale_ à des intervalles fréquents (peut-être hebdomadaires) pour réduire la surface d'attaque.

Si nous utilisons les outils en ligne de commande [OpenSSL](http://openssl.org) pour effectuer toutes les tâches de chiffrement et de déchiffrement, nous devons temporairement stocker la clé de chiffrement en « texte clair » dans un fichier, que nous détruirons de manière sécurisée en utilisant l'outil Linux shred.

Notez que nous utilisons le terme « texte clair » ici pour signifier que le contenu est déchiffré, et non pour signifier un format de texte brut. La clé est toujours des données binaires, mais si elle est interceptée par un attaquant, elle **ne** serait **pas** protégée par le chiffrement.

Cependant, simplement implémenter l'appel à l'utilitaire de déchiquetage comme dernière étape de notre algorithme de chiffrement ne suffirait pas à garantir que cela soit exécuté sous **tous** les chemins d'exécution possibles du code. Il peut y avoir des erreurs, des exceptions levées, une terminaison gracieuse (Control-c), ou une interruption brutale SIGKILL du programme.

Se prémunir contre toutes les possibilités n'est pas seulement fastidieux, mais aussi sujet aux erreurs. Au lieu de cela, nous pouvons laisser l'interpréteur Python faire le travail difficile pour nous, et garantir que certaines actions sont **toujours** entreprises lorsque l'objet est collecté par le ramasse-miettes.

Notez que la technique montrée ici ne fonctionnera pas pour le cas SIGKILL (aka kill -9), pour lequel vous devriez employer une technique plus avancée (gestionnaires de signaux).

L'idée est de créer une classe qui implémente la méthode spéciale ___del__()_, qui est garantie d'être **toujours** invoquée lorsqu'il n'y a plus de références à l'objet et qu'il est en cours de collecte par le ramasse-miettes. Le moment exact où cela se produit dépend de l'implémentation, mais dans les interpréteurs Python courants, cela semble être presque instantané.

Voici ce qui se passe sur un ordinateur portable MacOS, exécutant El Capitan et Python 2.7 :

```
$ pythonPython 2.7.10 (default, Oct 23 2015, 19:19:21)[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin>>> class Foo():...     def __del__(self):...         print("I'm gone, goodbye!")...>>> foo = Foo()>>> bar = foo>>> foo = None>>> bar = 99I'm gone, goodbye!>>> another = Foo()>>> ^DI'm gone, goodbye!$
```

Comme vous pouvez le voir, la méthode « destructeur » sera invoquée soit lorsqu'il n'y a plus de références à celle-ci (_foo_), soit lorsque l'interpréteur quitte (_bar_).

Le fragment de code suivant montre comment nous avons fini par implémenter notre clé « auto-chiffrante ». Je l'ai appelée _SelfDestructKey_ parce que la vraie caractéristique est qu'elle _détruit_ la version en texte clair de la clé de chiffrement à la sortie.

```
class SelfDestructKey(object):    """Une clé auto-destructrice : elle déchiquetera son contenu lorsqu'elle sera supprimée.        Cette clé se chiffrera également avec la clé donnée avant de s'écrire dans un fichier.    """     def __init__(self, encrypted_key, keypair):        """Crée une clé de chiffrement, en utilisant la paire de clés donnée pour la chiffrer/déchiffrer.         La version en texte clair de cette clé est conservée dans un fichier temporaire qui sera détruit de manière sécurisée        lorsque cet objet sera collecté par le ramasse-miettes.         :param encrypted_key la version chiffrée de cette clé est conservée dans ce fichier : si elle            n'existe pas, elle sera créée lorsque cette clé sera sauvegardée        :param keypair un tuple contenant la paire de clés (privée, publique) qui sera utilisée pour            déchiffrer et chiffrer (respectivement) cette clé.        :type keypair collections.namedtuple (Keypair)        """        self._plaintext = mkstemp()[1]        self.encrypted = encrypted_key        self.key_pair = keypair        if not os.path.exists(encrypted_key):            openssl('rand', '32', '-out', self._plaintext)        else:            with open(self._plaintext, 'w') as self_decrypted:                openssl('rsautl', '-decrypt', '-inkey', keypair.private, _in=encrypted_key,                        _out=self_decrypted)     def __str__(self):        return self._plaintext     def __del__(self):        try:            if not os.path.exists(self.encrypted):                self._save()            shred(self._plaintext)        except ErrorReturnCode as rcode:            raise RuntimeError(                "Soit nous n'avons pas pu sauvegarder le chiffré, soit nous n'avons pas pu déchiqueter la phrase secrète en texte clair "                "dans le fichier {plain} vers le fichier {enc}.  Vous devrez supprimer de manière sécurisée la version en texte clair "                "en utilisant quelque chose comme `shred -uz {plain}".format(                    plain=self._plaintext, enc=self.encrypted))     def _save(self):        """ Chiffre le contenu de la clé et l'écrit sur le disque.         :param dest: le chemin complet du fichier qui contiendra le contenu chiffré de cette clé.        :param key: le nom du fichier qui contient une clé de chiffrement (la partie PUBLIQUE d'une paire de clés).        :return: None        """        if not os.path.exists(self.key_pair.public):            raise RuntimeError("Fichier de clé de chiffrement '%s' introuvable" % self.key_pair.public)        with open(self._plaintext, 'rb') as selfkey:            openssl('rsautl', '-encrypt', '-pubin', '-inkey', self.key_pair.public,                    _in=selfkey, _out=self.encrypted)
```

De plus, notez comment j'ai implémenté la méthode ___str__()_, afin que je puisse obtenir le nom du fichier contenant la clé en texte clair en invoquant simplement :

```
passphrase = SelfDestructKey(secret_file, keypair=keys) encryptor = FileEncryptor(    secret_keyfile=str(passphrase),    plain_file=plaintext,    dest_dir=enc_cfg.out)
```

Notez qu'il s'agit d'une version simplifiée du code. Le code complet est disponible dans le dépôt Github [filecrypt](https://github.com/massenz/filecrypt), et il a été plus complètement expliqué dans cet [article de blog](https://codetrips.com/2016/07/13/filecrypt-openssl-file-encryption).

Nous aurions tout aussi facilement pu implémenter la méthode ___str__()_ pour retourner le contenu réel de la clé de chiffrement.

Quoi qu'il en soit, si vous regardez le code qui utilise la clé de chiffrement, à aucun moment nous n'avons besoin d'invoquer la méthode __save()_ ou d'invoquer directement l'utilitaire shred. Tout cela sera pris en charge par l'interpréteur lorsque la phrase secrète sort de la portée, ou que le script se termine (normalement ou anormalement).

### Implémenter le motif Command avec un objet appelable

![Image](https://cdn-media-1.freecodecamp.org/images/HeGyL0Ptmx1urLNbVe6DGXC8gtDcxDvhx6MQ)
_Crédit : [Defence-Imagery via Pixabay](https://pixabay.com/en/users/Defence-Imagery-11/" rel="noopener" target="_blank" title=")_

Python a le concept appelé _callable_, qui est essentiellement « quelque chose qui peut être invoqué comme si c'était une fonction. » Cela suit l'approche du _Duck Typing_ : « si cela ressemble à un canard, et cancane comme un canard, alors c'est un canard. » Eh bien, dans le cas de _callable_, « si cela ressemble à une fonction, et peut être appelé comme une fonction, alors c'est une fonction. »

Pour qu'un objet de classe se comporte comme un _callable_, tout ce que nous devons faire est de définir une méthode ___call__()_ puis de l'implémenter comme toute autre méthode de classe « ordinaire ».

Supposons que nous voulons implémenter un script « exécuteur de commandes » qui (similaire à, par exemple, git) peut prendre un ensemble de sous-commandes et les exécuter. Une approche pourrait être d'utiliser le [motif Command](http://amzn.to/29QSxB5) dans notre classe CommandRunner :

```
class CommandRunner(object):    """Implémente le motif Command, avec l'aide de la       méthode spéciale __call__()."""     def __init__(self, config):        """Initialise le Runner avec la configuration            à partir de l'analyse de la ligne de commande.            :param config les arguments de la ligne de commande, tels que analysés                 par ``argparse``           :type config Namespace        """        self._config = config     def __call__(self):        method = self._config.cmd        if hasattr(self, method):            callable_meth = self.__getattribute__(method)            if callable_meth:                callable_meth()        else:            raise RuntimeError('Commande inattendue "{}"; non trouvée'.format(method))     def run(self):        # Faire quelque chose avec les fichiers        pass     def build(self):        # Appeler une méthode externe qui prend une liste de fichiers        build(self._config.files)     def diff(self):        """Calculera la différence entre les deux fichiers passés"""        if self._config.files and len(self._config.files) == 2:            file_a, file_b = tuple(self._config.files)            diff_files(file_a, file_b)        else:            raise RuntimeError("Pas assez d'arguments pour diff : "                               "2 attendus, {} trouvés".format(                len(self._config.files) if self._config.files                                         else 'aucun'))     def diff_all(self):        # Cela prendra un nombre variable de fichiers et         # calculera la différence entre tous        pass
```

Voici l'argument d'initialisation de la configuration est un objet Namespace tel que retourné par la bibliothèque [argparse](https://docs.python.org/3/library/argparse.html) :

```
def parse_command():    """ Analyse les arguments de la ligne de commande et retourne un objet config
```

```
    :return: les options configurées    :rtype: Namespace ou None    """    parser = argparse.ArgumentParser()     # Supprimé l'argument `help` pour une meilleure lisibilité ;    # incluez toujours cela pour aider votre utilisateur, lorsqu'il invoque votre     # script avec le drapeau `--help`.    parser.add_argument('--host', default='localhost')    parser.add_argument('-p', '--port', type=int, default=8080,)    parser.add_argument('--workdir', default=default_wkdir)     parser.add_argument('cmd', default='run', choices=[        'run', 'build', 'diff', 'diff_all'])    parser.add_argument('files', nargs=argparse.REMAINDER")    return parser.parse_args()
```

Pour invoquer ce script, nous utiliserions quelque chose comme :

```
$ ./main.py run my_file.py
```

ou :

```
$ ./main.py diff file_1.md another_file.md
```

Il est intéressant de noter comment nous nous protégeons également contre les erreurs en utilisant une autre méthode spéciale (___getattribute__()_) et la méthode _hasattr()_ qui fait partie du modèle de données de Python mentionné ci-dessus :

```
if hasattr(self, method):    callable_meth = self.__getattribute__(method)
```

Notez que nous aurions pu utiliser la méthode spéciale ___getattr__()_ pour définir le comportement de la classe lors de la tentative d'accès à des attributs inexistants, mais dans ce cas, il était probablement plus facile de le faire au point d'appel.

Étant donné que nous disons à _argparse_ de limiter la valeur possible aux _choices_ lors de l'analyse de l'argument _cmd_, nous sommes assurés que nous n'obtiendrons jamais une commande « inconnue ». Cependant, la classe _CommandRunner_ n'a pas besoin de le savoir, et elle peut être utilisée dans d'autres instances où nous n'avons pas une telle garantie. Sans compter que nous ne sommes qu'à une faute de frappe d'un bug très déroutant, si nous n'avons pas fait notre travail dans ___call__()_.

Pour faire fonctionner tout cela, nous n'avons besoin d'implémenter qu'un simple extrait de ___main___ :

```
if __name__ == '__main__':     cfg = parse_command()     try: runner = CommandRunner(cfg)         runner() # Ressemble à une fonction, utilisons-la comme telle.     except Exception as ex:         logging.error("Impossible d'exécuter la commande `{}`: {}".format(            cfg.cmd, ex))         exit(1)
```

Notez comment nous invoquons le runner comme s'il s'agissait d'une méthode. Cela exécutera à son tour la méthode ___call__()_ et lancera la commande souhaitée.

Nous espérons vraiment que tout le monde s'accordera à dire que c'est un code bien plus agréable à regarder que des monstruosités telles que :

```
# NE FAITES PAS CELÀ CHEZ VOUS# Veuillez éviter les châteaux de if, ils sont simplement moches.si cfg.cmd == "build":    # faire quelque chose pour buildsinon si cfg.cmd == "run":    # faire quelque chose pour runsinon si cfg.cmd == "diff":    # faire quelque chose pour diffsinon si cfg.cmd == "diff_all":    # faire quelque chose pour diff_allsinon:    print("Commande inconnue", cfg.cmd)
```

Apprendre les « méthodes spéciales » de Python rendra votre code plus facile à lire et à réutiliser dans différentes situations. Cela rendra également votre code plus « pythonique » et immédiatement reconnaissable par d'autres pythonistes, rendant ainsi votre intention plus claire à comprendre et à raisonner.

_Publié à l'origine sur [codetrips.com](https://codetrips.com/2016/07/22/python-magic-methods/) le 22 juillet 2016._