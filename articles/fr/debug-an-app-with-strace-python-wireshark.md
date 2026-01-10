---
title: Comment déboguer des applications avec Strace, Python et Wireshark
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-04-26T00:23:26.000Z'
originalURL: https://freecodecamp.org/news/debug-an-app-with-strace-python-wireshark
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-egor-kamelev-3819742.jpg
tags:
- name: debugging
  slug: debugging
- name: Problem Solving
  slug: problem-solving
- name: Python
  slug: python
seo_title: Comment déboguer des applications avec Strace, Python et Wireshark
seo_desc: 'In this article I will show you a few techniques you can use to troubleshoot
  a program when is not behaving.

  This list is not universal and, depending on what you are looking for, it may not
  be enough to solve your problem. But it should be a good st...'
---

Dans cet article, je vais vous montrer quelques techniques que vous pouvez utiliser pour dépanner un programme lorsqu'il ne se comporte pas correctement.

Cette liste n'est pas universelle et, selon ce que vous recherchez, elle peut ne pas suffire à résoudre votre problème. Mais cela devrait être un bon début.

Avant de commencer, vous devriez être familier avec quelques notions :

* Comment exécuter des commandes sur Linux

* Protocoles comme DNS, HTTP et TLS

* Un langage de script comme Python

Ne vous inquiétez pas trop. Je vais vous donner suffisamment d'informations pour que vous puissiez suivre le tutoriel.

Et qu'allez-vous apprendre ?

* Utilisation de base de strace, nslookup et RPM

* Comment utiliser certaines fonctionnalités intéressantes du débogueur Python

* Comment analyser le trafic avec Wireshark

## **Le problème : Échec du téléchargement d'un fichier vers asciinema**

J'ai donc enregistré un asciicast, en utilisant le projet Open Source [asciinema](https://asciinema.org/docs/usage), pour mon petit projet Open Source [SuricataLog](https://pypi.org/project/SuricataLog). Ensuite, j'ai décidé de le partager avec le monde.

Mais contrairement aux autres enregistrements, celui-ci a refusé d'être téléchargé :

```python
[josevnz@dmaf5 SuricataLog]$ asciinema upload demo-ascii.cast 
asciinema: upload failed: <urlopen error [Errno 32] Broken pipe>
asciinema: retry later by running: asciinema upload demo-ascii.cast
```

Asciinema ne nous donne pas beaucoup d'informations sur l'erreur. Par exemple :

* Quel serveur et quel port l'outil essaie-t-il d'utiliser pour télécharger le fichier ?

* Quelle partie de la poignée de main du protocole échoue ?

* Est-ce que le problème vient de la destination ou est-ce un problème de mon côté ?

Nous allons utiliser quelques outils pour voir ce qui se passe ici.

## **Comment exécuter le programme avec strace**

Qu'est-ce que [strace](https://strace.io/) ?

> strace est un utilitaire de diagnostic, de débogage et d'instruction pour l'espace utilisateur sous Linux. Il est utilisé pour surveiller et manipuler les interactions entre les processus et le noyau Linux, qui incluent les appels système, les livraisons de signaux et les changements d'état des processus.
> 
> Les administrateurs système, les diagnosticiens et les dépanneurs le trouveront inestimable pour résoudre les problèmes avec les programmes pour lesquels le code source n'est pas facilement disponible, car ils n'ont pas besoin d'être recompilés pour être tracés.

strace est super utile lorsque vous n'avez pas le code source d'une application et que vous devez comprendre ce qui ne va pas lorsque vous appelez un programme. Il est temps de le voir en action :

```python
josevnz@dmaf5 SuricataLog]$ strace asciinema upload demo-ascii.cast
xecve("/usr/bin/asciinema", ["asciinema", "upload", "demo-ascii.cast"], 0x7ffdcddb1160 /* 55 vars */) = 0
brk(NULL)                               = 0x55e912d58000
arch_prctl(0x3001 /* ARCH_??? */, 0x7fff2f136480) = -1 EINVAL (Invalid argument)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=92299, ...}) = 0
mmap(NULL, 92299, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f69dd26a000
close(3)                                = 0
# 
# Commented out LOTS output
# ...
close(4)                                = 0
socket(AF_INET, SOCK_DGRAM|SOCK_CLOEXEC, IPPROTO_IP) = 4
connect(4, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("109.107.38.233")}, 16) = 0
getsockname(4, {sa_family=AF_INET, sin_port=htons(33771), sin_addr=inet_addr("192.168.1.22")}, [28 => 16]) = 0
connect(4, {sa_family=AF_UNSPEC, sa_data="\0\0\0\0\0\0\0\0\0\0\0\0\0\0"}, 16) = 0
connect(4, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("109.107.37.0")}, 16) = 0
getsockname(4, {sa_family=AF_INET, sin_port=htons(35023), sin_addr=inet_addr("192.168.1.22")}, [28 => 16]) = 0
close(4)                                = 0
socket(AF_INET, SOCK_STREAM|SOCK_CLOEXEC, IPPROTO_TCP) = 4
connect(4, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("109.107.38.233")}, 16) = 0
setsockopt(4, SOL_TCP, TCP_NODELAY, [1], 4) = 0
getsockopt(4, SOL_SOCKET, SO_TYPE, [1], [4]) = 0
getsockname(4, {sa_family=AF_INET, sin_port=htons(55682), sin_addr=inet_addr("192.168.1.22")}, [128 => 16]) = 0
ioctl(4, FIONBIO, [0])                  = 0
getpeername(4, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("109.107.38.233")}, [16]) = 0
getpid()                                = 45070
getpid()                                = 45070
getpid()                                = 45070
getpid()                                = 45070
getpid()                                = 45070
getpid()                                = 45070
write(4, "\26\3\1\2\0\1\0\1\374\3\3\327\2*\v\316GT*\262\207\235\264\317\254\37$|,V\205\362"..., 517) = 517
read(4, "\26\3\3\0z", 5)                = 5
read(4, "\2\0\0v\3\3E\217G?\335.;\212\237pn\16\257$\2\324J\324y\17\306\263\325i\264p"..., 122) = 122
read(4, "\24\3\3\0\1", 5)               = 5
read(4, "\1", 1)                        = 1
read(4, "\27\3\3\0\27", 5)              = 5
read(4, "0{}\22t9\264\265\340j\362\30\342\360\234\205\1\370\33\246\1z'", 23) = 23
read(4, "\27\3\3\17\335", 5)            = 5
read(4, "\17\5\310\261\355\271\227oUaI\366\361]\3\275q)\5{\367z\20\233\345\352k?\371\272\23\237"..., 4061) = 4061
stat("/etc/pki/tls/certs/8d33f237.0", 0x7ffd20be3620) = -1 ENOENT (No such file or directory)
read(4, "\27\3\3\1\31", 5)              = 5
read(4, "t\27\337\366G6\226Qs\273\327\314,\205\221\222Xu\233\21%\0s\340\270\224\330\t\2774\222h"..., 281) = 281
read(4, "\27\3\3\0005", 5)              = 5
read(4, "\204{\314\232\311\0P-*$\245\315\271\236c\210N\315\5\371\364\23\235\16\0350N0K\246\336\374"..., 53) = 53
write(4, "\24\3\3\0\1\1\27\3\3\0005\361\311\347\t\254m#\273\204\350\16\343\34P\320sS\211\30\232<"..., 64) = 64
ioctl(4, FIONBIO, [0])                  = 0
write(4, "\27\3\3\1\251\271\2673-\30\313\253\363\320H0\224\370Q\353(#?,\216\3\341\315|J\353\303"..., 430) = 430
write(4, "\27\3\3@\21\20\221\240\331\2737\10\244pv\312B\n\rn\272\33\336T\216\f\303\374k\177c\25"..., 16406) = 16406
write(4, "\27\3\3@\21\214\30\262\240s\216\240\354e\31\304Q\337Oy\21y\373\241g\311\224)\26\320\10{"..., 16406) = 16406
write(4, "\27\3\3@\21\36\323\240\376\276\224\35\f\10!@\36D\347\33ay\2617Hpv\4d\267y7"..., 16406) = 16406
write(4, "\27\3\3@\21\366x\264\242O2\7?\7\334\221W\24\2\f)\"@\20\375~\354\243W\32\0c"..., 16406) = 16406
write(4, "\27\3\3@\21\354\32W\36\265g\304\314\376\205\315\20\22\10c\333\342\264\330\366SS\4\217\356:V"..., 16406) = 16406
write(4, "\27\3\3@\21\1\274\35\335\271n\235e\202\202\207\221~\313\0y\210\344\312\32r\347\306x]\241C"..., 16406) = 16406
write(4, "\27\3\3@\21I\315\202\274\342\274\26\335qx\22-\226\322\320\203\231\274wLB\250\252\2\352\367\""..., 16406) = 8716
write(4, "\377\4m\341\317\376SUr\rQ\221\207\22#\262\314B7\33_v\310\271\fl\v\242\fK\v?"..., 7690) = -1 EPIPE (Broken pipe)
--- SIGPIPE {si_signo=SIGPIPE, si_code=SI_USER, si_pid=45070, si_uid=1000} ---
close(4)                                = 0
close(3)                                = 0
write(2, "\33[0;31masciinema: upload failed:"..., 76asciinema: upload failed: <urlopen error [Errno 32] Broken pipe>
) = 76
write(2, "\33[0;31masciinema: retry later by"..., 79asciinema: retry later by running: asciinema upload demo-ascii.cast
) = 79
munmap(0x7fa1aa089000, 12447744)        = 0
rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fa1bad0fa70}, {sa_handler=0x7fa1baf551d0, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fa1bad0fa70}, 8) = 0
munmap(0x7fa1ac649000, 593920)          = 0
exit_group(1)                           = ?
+++ exited with 1 +++
```

Regardez cet appel de socket (`man 2 getpeername`) :

```shell
getpeername(4, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("109.107.38.233")}, [16]) = 0
```

Et en dessous, comme vous pouvez le voir, nous écrivons effectivement des données sur le site web et la connexion se rompt :

```shell
write(4, "\27\3\3@\21\366x\264\242O2\7?\7\334\221W\24\2\f)\"@\20\375~\354\243W\32\0c"..., 16406) = 16406
write(4, "\27\3\3@\21\354\32W\36\265g\304\314\376\205\315\20\22\10c\333\342\264\330\366SS\4\217\356:V"..., 16406) = 16406
write(4, "\27\3\3@\21\1\274\35\335\271n\235e\202\202\207\221~\313\0y\210\344\312\32r\347\306x]\241C"..., 16406) = 16406
write(4, "\27\3\3@\21I\315\202\274\342\274\26\335qx\22-\226\322\320\203\231\274wLB\250\252\2\352\367\""..., 16406) = 8716
write(4, "\377\4m\341\317\376SUr\rQ\221\207\22#\262\314B7\33_v\310\271\fl\v\242\fK\v?"..., 7690) = -1 EPIPE (Broken pipe)
--- SIGPIPE {si_signo=SIGPIPE, si_code=SI_USER, si_pid=45070, si_uid=1000} ---
```

Alors, qui est '109.107.38.233' ? :

```python
[josevnz@dmaf5 SuricataLog]$ nslookup 109.107.38.233
233.38.107.109.in-addr.arpa	name = cip-109-107-38-233.gb1.brightbox.com.
```

Vous pouvez voir sur la page [about](https://asciinema.org/about) que brightbox.com fournit l'hébergement pour asciinema.

Alors, quel est le problème ? Ce n'est pas que le site est hors ligne ou inaccessible. Pouvez-vous creuser plus loin ?

## **Si seulement j'avais le code source – plongée en profondeur avec le débogueur Python**

```python
[josevnz@dmaf5 SuricataLog]$ file /usr/bin/asciinema
/usr/bin/asciinema: Python script, ASCII text executable
```

Oh, oui, nous l'avons ! Toujours curieux, vous ouvrez le script asciinema :

```python
#!/usr/bin/python3
# EASY-INSTALL-ENTRY-SCRIPT: 'asciinema==2.0.2','console_scripts','asciinema'
import re
import sys 

# for compatibility with easy_install; see #2198
__requires__ = 'asciinema==2.0.2'

try:
    from importlib.metadata import distribution
except ImportError:
    try:
        from importlib_metadata import distribution
    except ImportError:
        from pkg_resources import load_entry_point


def importlib_load_entry_point(spec, group, name):
    dist_name, _, _ = spec.partition('==')
    matches = ( 
        entry_point
        for entry_point in distribution(dist_name).entry_points
        if entry_point.group == group and entry_point.name == name
    )   
    return next(matches).load()


globals().setdefault('load_entry_point', importlib_load_entry_point)


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(load_entry_point('asciinema==2.0.2', 'console_scripts', 'asciinema')())
```

Le script principal a été généré avec [easy install](https://setuptools.pypa.io/en/latest/deprecated/easy_install.html), ce qui signifie que `asciinema.py` est juste un wrapper autour du code intéressant. Pour découvrir où se trouve le code intéressant, exécutons le script à travers le débogueur Python [pdb debugger](https://www.redhat.com/sysadmin/python-debugger-pdb) :

```python
[josevnz@dmaf5 SuricataLog]$ python3 -m pdb /usr/bin/asciinema upload demo-ascii.cast 
> /usr/bin/asciinema(3)<module>()
-> import re
(Pdb) n
> /usr/bin/asciinema(4)<module>()
-> import sys
(Pdb) c
asciinema: upload failed: <urlopen error [Errno 32] Broken pipe>
asciinema: retry later by running: asciinema upload demo-ascii.cast
The program exited via sys.exit(). Exit status: 1
```

Ce n'est pas exactement ce dont nous avons besoin. Le programme s'exécute, rencontre l'exception, puis redémarre depuis le début.

Trichons un peu. Asciinema a-t-il été installé avec un RPM (j'utilise Fedora Linux) ?

```python
[josevnz@dmaf5 SuricataLog]$ rpm -qif /usr/bin/asciinema
Name        : asciinema
Version     : 2.0.2
Release     : 6.fc33
```

Et nous essayons de télécharger un fichier, quelque chose qui ressemble à un uploader ?

```python
josevnz@dmaf5 SuricataLog]$ rpm -qil asciinema|grep -i uploa
/usr/lib/python3.9/site-packages/asciinema/commands/__pycache__/upload.cpython-39.opt-1.pyc
/usr/lib/python3.9/site-packages/asciinema/commands/__pycache__/upload.cpython-39.pyc
/usr/lib/python3.9/site-packages/asciinema/commands/upload.py
```

Ah, ça devient intéressant ! Ouvrons 'upload.py' :

```python
from asciinema.commands.command import Command
from asciinema.api import APIError


class UploadCommand(Command):

    def __init__(self, api, filename):
        Command.__init__(self)
        self.api = api 
        self.filename = filename

    def execute(self):
        try:
            result, warn = self.api.upload_asciicast(self.filename)

            if warn:
                self.print_warning(warn)

            self.print(result.get('message') or result['url'])

        except OSError as e:
            self.print_error("upload failed: %s" % str(e))
            return 1

        except APIError as e:
            self.print_error("upload failed: %s" % str(e))
            self.print_error("retry later by running: asciinema upload %s" % self.filename)
            return 1

        return 0
```

Placons quelques points d'arrêt à l'intérieur de UploadCommand (lignes 14, 26 dans ma copie du code) :

```python
[josevnz@dmaf5 SuricataLog]$ python3 -m pdb /usr/bin/asciinema upload demo-ascii.cast 
> /usr/bin/asciinema(3)<module>()
-> import re
(Pdb) b /usr/lib/python3.9/site-packages/asciinema/commands/upload.py:14
Breakpoint 1 at /usr/lib/python3.9/site-packages/asciinema/commands/upload.py:14
(Pdb) c
> /usr/lib/python3.9/site-packages/asciinema/commands/upload.py(14)execute()
-> result, warn = self.api.upload_asciicast(self.filename)
(Pdb) c
> /usr/lib/python3.9/site-packages/asciinema/commands/upload.py(26)execute()
-> self.print_error("upload failed: %s" % str(e))
(Pdb) n
asciinema: upload failed: <urlopen error [Errno 32] Broken pipe>
> /usr/lib/python3.9/site-packages/asciinema/commands/upload.py(27)execute()
-> self.print_error("retry later by running: asciinema upload %s" % self.filename)
(Pdb) ll
 12  	    def execute(self):
 13  	        try:
 14 B	            result, warn = self.api.upload_asciicast(self.filename)
 15  	
 16  	            if warn:
 17  	                self.print_warning(warn)
 18  	
 19  	            self.print(result.get('message') or result['url'])
 20  	
 21  	        except OSError as e:
 22  	            self.print_error("upload failed: %s" % str(e))
 23  	            return 1
 24  	
 25  	        except APIError as e:
 26 B	            self.print_error("upload failed: %s" % str(e))
 27  ->	            self.print_error("retry later by running: asciinema upload %s" % self.filename)
 28  	            return 1
 29  	
 30  	        return 0
```

Nous avons obtenu une APIError. Y a-t-il quelque chose d'intéressant avec ce type d'exception ?

```shell
(Pdb) source APIError
11  	class APIError(Exception):
12  	    pass
(Pdb) e.args
('<urlopen error [Errno 32] Broken pipe>',)
```

Donc rien de spécial, dérivé directement de `Exception`. De plus, les arguments de l'exception sont simplement le message d'erreur.

Bien sûr, l'étape suivante est de voir si cette erreur provient d'une bibliothèque connue (recherchez sur Internet [l'erreur](https://duckduckgo.com/?q=%3Curlopen+error+%5BErrno+32%5D+Broken+pipe%3E&ia=web)).

J'ai trouvé ce problème sur [GitHub](https://github.com/asciinema/asciinema/issues/335). En lisant [plus loin](https://github.com/asciinema/asciinema/issues/91), vous pouvez voir que l'auteur généreux d'Asciicast paie le stockage de sa propre poche afin que nous puissions tous profiter du stockage en ligne gratuitement :

> La taille maximale a été fixée à 2 Mo, ce qui semble être trop bas. Je l'ai augmentée à 5 Mo. Ce n'est pas beaucoup, mais je paie pour le stockage (S3) de ma propre poche, donc je ne peux pas offrir des Go de stockage pour chaque utilisateur. Faites-moi savoir si cela fonctionne pour vous. Je suis d'accord pour l'augmenter encore plus, mais maintenant je veux trouver un bon compromis entre les besoins des utilisateurs et les coûts d'hébergement.

Alors, confirmons que c'est bien la cause :

```python
[josevnz@dmaf5 SuricataLog]$ ls -lh demo-ascii.cast 
-rw-rw-r-- 1 josevnz josevnz 12M Apr 21 15:44 demo-ascii.cast
```

Jusqu'à présent, la grande taille du fichier semble être le coupable.

Je suis toujours en train d'exécuter le débogueur, et j'aimerais voir quels modules asciinema ont été chargés. Pour cela, basculez en mode '*interact*' et obtenez cette liste avec une [compréhension de liste](https://peps.python.org/pep-0202/) et une [expression régulière](https://docs.python.org/3/howto/regex.html) :

```python
(Pdb) interact
*interactive*
>>> import re
>>> import sys
>>> import pprint
>>> pprint.pprint([name for name in sys.modules.keys() if re.search('asciinema', name)], indent=True)
['asciinema.asciicast.events',
 'asciinema.asciicast.v1',
 'asciinema.asciicast.v2',
 'asciinema.asciicast',
 'asciinema.term',
 'asciinema.pty',
 'asciinema',
 'asciinema.config',
 'asciinema.commands',
 'asciinema.commands.command',
 'asciinema.commands.auth',
 'asciinema.asciicast.raw',
 'asciinema.http_adapter',
 'asciinema.urllib_http_adapter',
 'asciinema.api',
 'asciinema.commands.record',
 'asciinema.player',
 'asciinema.commands.play',
 'asciinema.commands.cat',
 'asciinema.commands.upload',
 'asciinema.__main__']
>>>
```

Les éléments suivants semblent pouvoir contenir des indices :

* asciinema.urllib_http_adapter

* asciinema.commands.upload

* asciinema.http_adapter

Quittez le débogueur (ou allez dans un autre terminal) et recherchez l'urllib_http_adapter :

```python
[josevnz@dmaf5 SuricataLog]$ find /usr/lib/python3.9/site-packages/asciinema/ -name 'urllib_http_adapter*'
/usr/lib/python3.9/site-packages/asciinema/__pycache__/urllib_http_adapter.cpython-39.opt-1.pyc
/usr/lib/python3.9/site-packages/asciinema/__pycache__/urllib_http_adapter.cpython-39.pyc
/usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py
```

Si vous ouvrez le fichier, vous verrez que la méthode 'post' est celle que nous voulons déboguer :

```python
class URLLibHttpAdapter:

    def post(self, url, fields={}, files={}, headers={}, username=None, password=None):
        content_type, body = MultipartFormdataEncoder().encode(fields, files)

        headers = headers.copy()
        headers["Content-Type"] = content_type

        if password:
            auth = "%s:%s" % (username, password)
            encoded_auth = base64.encodebytes(auth.encode('utf-8'))[:-1]
            headers["Authorization"] = b"Basic " + encoded_auth

        request = Request(url, data=body, headers=headers, method="POST")

        try:
            response = urlopen(request)
            status = response.status
            headers = self._parse_headers(response)
            body = response.read().decode('utf-8')
        except HTTPError as e:
            status = e.code
            headers = {}
            body = e.read().decode('utf-8')
        except (http.client.RemoteDisconnected, URLError) as e:
            raise HTTPConnectionError(str(e))

        return (status, headers, body)
```

Un point d'arrêt à la ligne 65 nous amènera là où nous devons être :

```python
[josevnz@dmaf5 SuricataLog]$ python3 -m pdb /usr/bin/asciinema upload demo-ascii.cast 
> /usr/bin/asciinema(3)<module>()
-> import re
(Pdb) b /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py:65
Breakpoint 1 at /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py:65
(Pdb) c
> /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py(65)post()
-> headers = headers.copy()
(Pdb) ll
 62  	    def post(self, url, fields={}, files={}, headers={}, username=None, password=None):
 63  	        content_type, body = MultipartFormdataEncoder().encode(fields, files)
 64  	
 65 B->	        headers = headers.copy()
 66  	        headers["Content-Type"] = content_type
 67  	
 68  	        if password:
 69  	            auth = "%s:%s" % (username, password)
 70  	            encoded_auth = base64.encodebytes(auth.encode('utf-8'))[:-1]
 71  	            headers["Authorization"] = b"Basic " + encoded_auth
 72  	
 73  	        request = Request(url, data=body, headers=headers, method="POST")
 74  	
 75  	        try:
 76  	            response = urlopen(request)
 77  	            status = response.status
 78  	            headers = self._parse_headers(response)
 79  	            body = response.read().decode('utf-8')
 80  	        except HTTPError as e:
 81  	            status = e.code
 82  	            headers = {}
 83  	            body = e.read().decode('utf-8')
 84  	        except (http.client.RemoteDisconnected, URLError) as e:
 85  	            raise HTTPConnectionError(str(e))
 86  	
 87  	        return (status, headers, body)
(Pdb) args
self = <asciinema.urllib_http_adapter.URLLibHttpAdapter object at 0x7f59ed3e4640>
url = 'https://asciinema.org/api/asciicasts'
fields = {}
files = {'asciicast': ('ascii.cast', <_io.BufferedReader name='demo-ascii.cast'>)}
headers = {'User-Agent': 'asciinema/2.0.2 CPython/3.9.9 Linux/5.14.18-100.fc33.x86_64-x86_64-with-glibc2.32', 'Accept': 'application/json'}
username = 'XXXX'
password = 'XXXX0f1-1d73-43fc-XX36-c9d7ZZZAAAA'
```

Très intéressant — nous pourrions définitivement utiliser les champs suivants pour exercer la fonctionnalité de téléchargement sans Python (obtenus en utilisant `args` à partir du débogueur) :

* url = '[https://asciinema.org/api/asciicasts](https://asciinema.org/api/asciicasts)'

* headers = {'User-Agent': 'asciinema/2.0.2 CPython/3.9.9 Linux/5.14.18-100.fc33.x86_64-x86_64-with-glibc2.32', 'Accept': 'application/json'}

* username = 'XXXX'

* password = 'XXXX0f1-1d73-43fc-XX36-c9d7ZZZAAAA'

Quelle exception allons-nous obtenir ? Nous définissons 2 points d'arrêt supplémentaires et laissons le débogueur s'exécuter jusqu'à ce qu'il les atteigne :

```python
(Pdb) b 81
Breakpoint 2 at /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py:81
(Pdb) b 85
Breakpoint 3 at /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py:85
(Pdb) c
> /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py(85)post()
-> raise HTTPConnectionError(str(e))
(Pdb) e
URLError(BrokenPipeError(32, 'Broken pipe'))
```

Le type de l'erreur est [BrokenPipeError](https://docs.python.org/3/library/exceptions.html#BrokenPipeError) :

> Une sous-classe de ConnectionError, levée lors de la tentative d'écriture sur un pipe alors que l'autre extrémité a été fermée, ou lors de la tentative d'écriture sur une socket qui a été fermée pour l'écriture. Correspond à errno EPIPE et ESHUTDOWN.

Une dernière chose — lisons-nous le fichier entier en mémoire avant de l'envoyer au site web ?

```python
[josevnz@dmaf5 SuricataLog]$ python3 -m pdb /usr/bin/asciinema upload demo-ascii.cast 
> /usr/bin/asciinema(3)<module>()
-> import re
(Pdb) b /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py:49
Breakpoint 1 at /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py:49
(Pdb) c
> /usr/lib/python3.9/site-packages/asciinema/urllib_http_adapter.py(49)iter()
-> yield (data, len(data))
(Pdb) len(data)
12444283
```

12 Mo, pas énorme pour la mémoire des ordinateurs d'aujourd'hui, mais pas petit non plus.

Vous vous souvenez des paramètres que nous avons réussi à capturer précédemment avec l'aide du débogueur (URL, utilisateur, etc.) ? Nous en savons maintenant assez pour utiliser un outil différent ([curl](https://curl.se/)) pour essayer de télécharger le fichier :

```python
[josevnz@dmaf5 SuricataLog]$ curl --fail --http1.1 --verbose --user $USER:$(cat ~/.config/asciinema/install-id) https://asciinema.org/api/asciicasts --form asciicast=@demo-ascii.cast
*   Trying 109.107.37.0:443...
* Connected to asciinema.org (109.107.37.0) port 443 (#0)
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/pki/tls/certs/ca-bundle.crt
  CApath: none
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: CN=*.asciinema.org
*  start date: Mar  9 06:02:26 2022 GMT
*  expire date: Jun  7 06:02:25 2022 GMT
*  subjectAltName: host "asciinema.org" matched cert's "asciinema.org"
*  issuer: C=US; O=Let's Encrypt; CN=R3
*  SSL certificate verify ok.
* Server auth using Basic with user 'XXXX'
> POST /api/asciicasts HTTP/1.1
> Host: asciinema.org
> Authorization: Basic XXXXX=
> User-Agent: curl/7.71.1
> Accept: */*
> Content-Length: 12444495
> Content-Type: multipart/form-data; boundary=------------------------0d76dac3e1f8aed4
> Expect: 100-continue
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* Mark bundle as not supporting multiuse
< HTTP/1.1 100 Continue
* Mark bundle as not supporting multiuse
* The requested URL returned error: 413 Request Entity Too Large
* Closing connection 0
* TLSv1.3 (OUT), TLS alert, close notify (256):
curl: (22) The requested URL returned error: 413 Request Entity Too Large
```

L'erreur `413 Request Entity Too Large` [signifie](https://developer.mozilla.org/en-US/docs/web/http/status/413) :

> Le code de statut de réponse HTTP 413 Payload Too Large indique que l'entité de la requête est plus grande que les limites définies par le serveur ; le serveur peut fermer la connexion ou retourner un champ d'en-tête Retry-After.

Donc curl est beaucoup mieux que Python pour nous dire la vérité sur pourquoi notre fichier a été rejeté.

Combien de données avons-nous réussi à transmettre avant que notre connexion ne soit coupée ? Voyons si nous pouvons le découvrir en utilisant un renifleur de paquets.

## **Comment utiliser Wireshark et le SSLKEYLOGFILE pour inspecter le trafic HTTP**

Vous pouvez capturer le trafic entre votre machine et le site web asciinema en utilisant un renifleur de réseau comme [Wireshark](https://wireshark.org/) ou le bien connu [tcpdump](https://www.tcpdump.org/).

Le trafic sera chiffré car nous utilisons HTTPS, mais en utilisant une fonctionnalité supportée par de nombreux programmes connue sous le nom de '[TLS master encryption secrets](https://www.paolotagliaferri.com/overview-of-transport-layer-security-protocol-tls-1-3/)' vous pouvez déchiffrer la session. Pour cela, activons la [fonctionnalité](https://everything.curl.dev/usingcurl/tls/sslkeylogfile) sur le client :

```python
export SSLKEYLOGFILE=$HOME/keylogfile.txt
```

Si c'est supporté, le fichier $SSLKEYLOGFILE sera rempli avec les clés :

```python
[josevnz@dmaf5 SuricataLog]$ export SSLKEYLOGFILE=$HOME/keylogfile.txt
[josevnz@dmaf5 SuricataLog]$ /usr/bin/asciinema upload demo-ascii.cast 
asciinema: upload failed: <urlopen error [Errno 32] Broken pipe>
asciinema: retry later by running: asciinema upload demo-ascii.cast
[josevnz@dmaf5 SuricataLog]$ ls -l $SSLKEYLOGFILE
-rw-rw-r-- 1 josevnz josevnz 832 Apr 21 21:02 /home/josevnz/keylogfile.txt

[josevnz@dmaf5 SuricataLog]$ cat /home/josevnz/keylogfile.txt

# TLS secrets log file, generated by OpenSSL / Python
SERVER_HANDSHAKE_TRAFFIC_SECRET 2987e32066d608a3de0cdd896f62801290045c2616abfaef5fac1c6986131847 4dd1a1bc1261a84886b28ee72798d89ba77d7de7051b3dcdafd548a621ed1124
EXPORTER_SECRET 2987e32066d608a3de0cdd896f62801290045c2616abfaef5fac1c6986131847 1ec8d94b7ec373a984abed25fa0dfaa6346fe67feea0516d7e2e46a666a12614
SERVER_TRAFFIC_SECRET_0 2987e32066d608a3de0cdd896f62801290045c2616abfaef5fac1c6986131847 e1d8fa6dba5eea00d4e52af0ce7e7007da0ade4c9dd9da3d9a060b55880531f1
CLIENT_HANDSHAKE_TRAFFIC_SECRET 2987e32066d608a3de0cdd896f62801290045c2616abfaef5fac1c6986131847 903bf381f927d783e72846201e87203ff130d9cf21f84cf0b923834d69c3fe76
CLIENT_TRAFFIC_SECRET_0 2987e32066d608a3de0cdd896f62801290045c2616abfaef5fac1c6986131847 495b5acf783869d74a7521e3b9c3f7bfc6dbc25e24ba95f684e96f6b2a435206
SERVER_HANDSHAKE_TRAFFIC_SECRET 82cab66e906c3cd3c58b3aeeecd66b2a12e521704d3e19e2f008550705e78e00 5a0d699640bd460530bd38148cf979e585b9a43c1bd545974561df18841fa5f4
EXPORTER_SECRET 82cab66e906c3cd3c58b3aeeecd66b2a12e521704d3e19e2f008550705e78e00 32b69cb41b8db36371e7d207a45e20d401bb05e0cd8bf492e3ace009e2845d12
SERVER_TRAFFIC_SECRET_0 82cab66e906c3cd3c58b3aeeecd66b2a12e521704d3e19e2f008550705e78e00 1f42b4392b2cc14789c4eaec4dae275c6a040ae3b11fc6bba58c90c7b80caa96
CLIENT_HANDSHAKE_TRAFFIC_SECRET 82cab66e906c3cd3c58b3aeeecd66b2a12e521704d3e19e2f008550705e78e00 bd93073bda56e559743a1f1ffc48c062089addcfc007c7defe08c28ac0ee6287
CLIENT_TRAFFIC_SECRET_0 82cab66e906c3cd3c58b3aeeecd66b2a12e521704d3e19e2f008550705e78e00 32b615c0dd25cb7b430a0cff44871e3263bd67af973e4b2f7fb19aab4df468d8
SERVER_HANDSHAKE_TRAFFIC_SECRET 68dcc859bc4edb51354a9f583e036d0b2787a337ee894e253925e273a5cd3889 a52a20827ce04dfc4ee557608ed5a0bfb6794ace0c4a1b69a1d56e5f16d8570b
EXPORTER_SECRET 68dcc859bc4edb51354a9f583e036d0b2787a337ee894e253925e273a5cd3889 8179afb8e7c7a77e35143c40a6bb62ccea2e644e48cc95b91b05f525bc59ada7
SERVER_TRAFFIC_SECRET_0 68dcc859bc4edb51354a9f583e036d0b2787a337ee894e253925e273a5cd3889 3d4abf6a9ea06395648a45428ca78c24962d8cc11440fe1d72f035ae35e61010
CLIENT_HANDSHAKE_TRAFFIC_SECRET 68dcc859bc4edb51354a9f583e036d0b2787a337ee894e253925e273a5cd3889 1d812a6c3c012a8fa4a6017ee573b47a5b361d15b861938ebca9194ecbc2a250
CLIENT_TRAFFIC_SECRET_0 68dcc859bc4edb51354a9f583e036d0b2787a337ee894e253925e273a5cd3889 6348a88dc9b6a350d72a7154140b824db80ba4f48c9e1fabcee76da8d248b041
```

Bien. L'étape suivante est de capturer le trafic. Nous allons utiliser [tcpdump](https://www.tcpdump.org/) avec une [expression simple](https://www.tcpdump.org/papers/ethereal-tcpdump.pdf) pour filtrer le trafic capturé :

```python
[josevnz@dmaf5 temp]$ sudo tcpdump -i eno1 -v -v -v 'host asciinema.org' -w ~/temp/asciinema.org.pcap
dropped privs to tcpdump
tcpdump: listening on eno1, link-type EN10MB (Ethernet), snapshot length 262144 bytes
```

Et dans une autre fenêtre, exécutez le client asciinema (nous le ferons deux fois pour avoir plus de données) :

```python
[josevnz@dmaf5 SuricataLog]$ /usr/bin/asciinema upload demo-ascii.cast 
asciinema: upload failed: <urlopen error [Errno 32] Broken pipe>
asciinema: retry later by running: asciinema upload demo-ascii.cast
[josevnz@dmaf5 SuricataLog]$ 
[josevnz@dmaf5 SuricataLog]$ /usr/bin/asciinema upload demo-ascii.cast 
asciinema: upload failed: <urlopen error [Errno 104] Connection reset by peer>
asciinema: retry later by running: asciinema upload demo-ascii.cast
```

Maintenant, arrêtez la capture tcpdump dans l'autre fenêtre :

```python
tcpdump: listening on eno1, link-type EN10MB (Ethernet), snapshot length 262144 bytes
^C113 packets captured
118 packets received by filter
0 packets dropped by kernel
```

Rejouons le fichier pcap pour voir ce qui a été enregistré :

```python
[josevnz@dmaf5 temp]$ tcpdump -r ~/temp/asciinema.org.pcap
reading from file /home/josevnz/temp/asciinema.org.pcap, link-type EN10MB (Ethernet), snapshot length 262144
07:17:18.244941 IP dmaf5.home.59896 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [S], seq 1651239781, win 64240, options [mss 1460,sackOK,TS val 3293505858 ecr 0,nop,wscale 7], length 0
07:17:18.337023 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59896: Flags [S.], seq 2395275599, ack 1651239782, win 65160, options [mss 1460,sackOK,TS val 3934370169 ecr 3293505858,nop,wscale 7], length 0
07:17:18.337070 IP dmaf5.home.59896 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [.], ack 1, win 502, options [nop,nop,TS val 3293505950 ecr 3934370169], length 0
07:17:18.337643 IP dmaf5.home.59896 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [P.], seq 1:518, ack 1, win 502, options [nop,nop,TS val 3293505951 ecr 3934370169], length 517
07:17:18.429273 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59896: Flags [.], ack 518, win 506, options [nop,nop,TS val 3934370263 ecr 3293505951], length 0
07:17:18.433850 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59896: Flags [.], seq 1:1449, ack 518, win 506, options [nop,nop,TS val 3934370267 ecr 3293505951], length 1448
07:17:18.433863 IP dmaf5.home.59896 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [.], ack 1449, win 501, options [nop,nop,TS val 3293506047 ecr 3934370267], length 0
07:17:18.433966 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59896: Flags [P.], seq 1449:2897, ack 518, win 506, options [nop,nop,TS val 3934370267 ecr 3293505951], length 1448
07:17:18.433981 IP dmaf5.home.59896 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [.], ack 2897, win 496, options [nop,nop,TS val 3293506047 ecr 3934370267], length 0
07:17:18.434089 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59896: Flags [.], seq 2897:4345, ack 518, win 506, options [nop,nop,TS val 3934370267 ecr 3293505951], length 1448
...
07:17:30.612523 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59898: Flags [.], ack 11148, win 501, options [nop,nop,TS val 3934382447 ecr 3293518134], length 0
07:17:30.612524 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59898: Flags [.], ack 12596, win 501, options [nop,nop,TS val 3934382447 ecr 3293518134], length 0
07:17:30.612558 IP dmaf5.home.59898 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [.], seq 35764:37212, ack 4724, win 499, options [nop,nop,TS val 3293518226 ecr 3934382447], length 1448
07:17:30.612563 IP dmaf5.home.59898 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [P.], seq 37212:38660, ack 4724, win 499, options [nop,nop,TS val 3293518226 ecr 3934382447], length 1448
07:17:30.612637 IP dmaf5.home.59898 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [.], seq 38660:40108, ack 4724, win 499, options [nop,nop,TS val 3293518226 ecr 3934382447], length 1448
07:17:30.612643 IP dmaf5.home.59898 > cip-109-107-37-0.gb1.brightbox.com.https: Flags [P.], seq 40108:41556, ack 4724, win 499, options [nop,nop,TS val 3293518226 ecr 3934382447], length 1448
07:17:30.613064 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59898: Flags [P.], seq 4724:5080, ack 12596, win 501, options [nop,nop,TS val 3934382448 ecr 3293518134], length 356
07:17:30.613106 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59898: Flags [P.], seq 5080:5104, ack 12596, win 501, options [nop,nop,TS val 3934382448 ecr 3293518134], length 24
07:17:30.614231 IP cip-109-107-37-0.gb1.brightbox.com.https > dmaf5.home.59898: Flags [R.], seq 5104, ack 12596, win 501, options [nop,nop,TS val 3934382448 ecr 3293518134], length 0
```

Il est temps de lancer Wireshark. J'aime utiliser une interface graphique pour cela car les capacités de filtrage sont agréables, et vous pouvez explorer le contenu du fichier PCAP beaucoup plus facilement.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/wireshark-open-pcap-file.png align="left")

Le contenu de la capture de trafic :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/wireshark-traffic-dump.png align="left")

Donc, nous suivons la première fois où nous avons obtenu un message TLS hello, cliquez avec le bouton droit sur les préférences du protocole —> Transport Layer Security puis "pre-Master-Secret log filename" :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/wireshark-tls-pre-master-key.png align="left")

Maintenant, la partie amusante. Si vous cliquez avec le bouton droit sur le premier message hello et dites "follow TLS stream", une nouvelle fenêtre s'ouvrira avec toute la conversation jusqu'au moment où nous avons obtenu notre réinitialisation de connexion, sans chiffrement !

![Image](https://www.freecodecamp.org/news/content/images/2022/04/wireshark-follow-tls.png align="left")

Nous n'avons donc réussi à envoyer que 33 Ko avant d'être coupés par le serveur asciinema. Quelle impolitesse ! 😊

Parce que la charge utile des données n'est pas si grande, je vais vous la montrer ensuite, assurez-vous de prêter attention aux éléments suivants :

1. J'ai changé le contenu de Authorization: Basic car je ne veux pas divulguer mon utilisateur/mot de passe encodé en base64.

2. Content-Length: 12444474. C'est ainsi qu'asciinema sait quelle est la taille du fichier que nous voulons télécharger, donc le serveur le rejette.

3. Asciinema utilise Nginx.

4. Vous pouvez voir le message de fermeture à la fin (entité trop grande).

```python
POST /api/asciicasts HTTP/1.1
Accept-Encoding: identity
Content-Length: 12444474
Host: asciinema.org
User-Agent: asciinema/2.0.2 CPython/3.9.9 Linux/5.14.18-100.fc33.x86_64-x86_64-with-glibc2.32
Accept: application/json
Content-Type: multipart/form-data; boundary=d5c6b2543ee94511943126c6a3c5d33a
Authorization: Basic XXXXX=
Connection: close

--d5c6b2543ee94511943126c6a3c5d33a
Content-Disposition: form-data; name="asciicast"; filename="ascii.cast"
Content-Type: application/octet-stream

{"version": 2, "width": 203, "height": 32, "timestamp": 1650568938, "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}
[0.191182, "o", "\u001b]777;notify;Command completed;eve_log.py --format table --timestamp '2022-02-23T18:22:24.405139+0000' test/eve.json\u001b\\\u001b]777;precmd\u001b\\\u001b]0;josevnz@dmaf5:~/SuricataLog-Logging-features-branch\u001b\\"]
[0.19215, "o", "\u001b]7;file://dmaf5/home/josevnz/SuricataLog-Logging-features-branch\u001b\\"]
[0.192399, "o", "[josevnz@dmaf5 SuricataLog-Logging-features-branch]$ "]
[1.000538, "o", "Let me show you how you can filter your Suricata alerts, displaying the results in different formats"]
[4.506902, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C"]
[4.921813, "o", "\u001b[1@#"]
[5.170393, "o", "\u001b[1@ "]
[5.538486, "o", "\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C"]
[6.914337, "o", "\r\n"]
[6.918708, "o", "\u001b]777;notify;Command completed;# Let me show you how you can filter your Suricata alerts, displaying the results in different formats\u001b\\\u001b]777;precmd\u001b\\\u001b]0;josevnz@dmaf5:~/SuricataLog-Logging-features-branch\u001b\\"]
[6.920219, "o", "\u001b]7;file://dmaf5/home/josevnz/SuricataLog-Logging-features-branch\u001b\\"]
[6.920352, "o", "[josevnz@dmaf5 SuricataLog-Logging-features-branch]$ "]
[8.202111, "o", "1"]
[8.658197, "o", ")"]
[8.962176, "o", " "]
[10.153862, "o", "A"]
[10.409632, "o", " "]
[10.61679, "o", "n"]
[10.777002, "o", "i"]
[10.881112, "o", "c"]
[10.952884, "o", "e"]
[11.088641, "o", " "]
[11.201045, "o", "t"]
[11.466022, "o", "a"]
[11.553785, "o", "b"]
[11.818412, "o", "l"]
[11.961808, "o", "e"]
[13.51443, "o", "\r\n"]
[13.514675, "o", "bash: syntax error near unexpected token `)'\r\n"]
[13.518913, "o", "\u001b]777;notify;Command completed;1) A nice table\u001b\\\u001b]777;precmd\u001b\\\u001b]0;josevnz@dmaf5:~/SuricataLog-Logging-features-branch\u001b\\"]
[13.520551, "o", "\u001b]7;file://dmaf5/home/josevnz/SuricataLog-Logging-features-branch\u001b\\"]
[13.52072, "o", "[josevnz@dmaf5 SuricataLog-Logging-features-branch]$ "]
[22.176716, "o", "eve_log.py --format table --timestamp '2022-02-23T18:22:24.405139+0000' test/eve.jso"]
[24.202009, "o", "n"]
[26.097822, "o", "\r\n"]
[26.098024, "o", "\u001b]777;preexec\u001b\\"]
[26.312676, "o", "\u001b[?1049h\u001b[H\u001b[?1000h\u001b[?1003h\u001b[?1015h\u001b[?1006h\u001b[?25l\u001b[?1003h\r\n"]
[26.314059, "o", "\u001bP=1s\u001b\\\u001b[H\u001b[H                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                               "]
[26.314299, "o", "            \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                              "]
[26.314387, "o", "             \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                             "]
[26.314455, "o", "              \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                            "]
[26.314502, "o", "               \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                           "]
[26.31456, "o", "                \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                          "]
[26.314616, "o", "                 \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \u001bP=2s\u001b\\"]
[26.31467, "o", "\u001bP=1s\u001b\\\u001b[H\u001b[H                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                               "]
[26.314714, "o", "            \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                              "]
[26.314781, "o", "             \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                             "]
[26.314843, "o", "              \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                            "]
[26.314902, "o", "               \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                           "]
[26.314957, "o", "                \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                          "]
[26.315012, "o", "                 \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \u001bP=2s\u001b\\"]
[26.316033, "o", "\u001b[?25l"]
[26.318086, "o", "\r\u001b[2KParsing test/eve.json \u001b[38;5;237m........................................................................................................................\u001b[0m \u001b[35m  0%\u001b[0m \u001b[36m-:--:--\u001b[0m"]
[26.378123, "o", "\r\u001b[2KParsing test/eve.json \u001b[38;2;114;156;31m........................................................................................................................\u001b[0m \u001b[35m100%\u001b[0m \u001b[36m0:00:00\u001b[0m\r\n\u001b[?25h"]
[26.390312, "o", "\u001bP=1s\u001b\\\u001b[H\u001b[H                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                               "]
[26.39044, "o", "            \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                              "]
[26.390499, "o", "             \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                             "]
[26.390559, "o", "              \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                            "]
[26.390615, "o", "               \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                           "]
[26.39064, "o", "                \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                          "]
[26.390719, "o", "                 \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \u001bP=2s\u001b\\"]
[26.390868, "o", "\u001bP=1s\u001b\\\u001b[H\u001b[H                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                               "]
[26.390893, "o", "            \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                              "]
[26.390944, "o", "             \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                             "]
[26.391027, "o", "              \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                            "]
[26.391091, "o", "               \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                           "]
[26.391116, "o", "                \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                          "]
[26.391172, "o", "                 \r\n                                                                                                                                                                                                           \r\n                                                                                                                                                                                                           \u001bP=2s\u001b\\"]
[26.431391, "o", "\u001bP=1s\u001b\\\u001b[H\u001b[3m                                                                                      Suricata alerts for 2022-02-23 18:22:24.405139, logs=test/eve.json                                                   \u001b[0m\r\n.................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................\r\n...\u001b[1;35m \u001b[0m\u001b[1;35mTimestamp                      \u001b[0m\u001b[1;35m \u001b[0m...\u001b[1;35m \u001b[0m\u001b[1;35mSeverity\u001b[0m\u001b[1;35m \u001b[0m...\u001b[1;35m \u001b[0m\u001b[1;35mSignature                                           \u001b"]
[26.431543, "o", "[0m\u001b[1;35m \u001b[0m...\u001b[1;35m \u001b[0m\u001b[1;35mProtocol\u001b[0m\u001b[1;35m \u00HTTP/1.1 413 Request Entity Too Large
Content-Length: 176
Content-Type: text/html
Date: Fri, 22 Apr 2022 11:17:19 GMT
Server: nginx
Connection: close

<html>
<head><title>413 Request Entity Too Large</title></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

# **Quelle est la prochaine étape pour vous ?**

Ainsi, la prochaine fois que vous avez un problème avec un programme installé sur votre système, vous saurez quoi vérifier.

Nous avons couvert 3 façons d'enquêter sur un problème avec une application qui télécharge un fichier vers un site web distant en utilisant HTTPS :

1. Utilisation de *strace*

2. Si le programme est un script Python, alors il y a de bonnes chances que vous puissiez lire le code vous-même et exécuter le script à travers *le débogueur*, étape par étape, pour comprendre le problème. C'est probablement la méthode la plus chronophage, mais c'est aussi la plus gratifiante car vous apprenez comment d'autres bons développeurs pensent !

3. Et enfin, nous avons capturé le trafic chiffré entre nous et le site distant et analysé le téléchargement. En activant certaines fonctionnalités spéciales, nous avons pu déchiffrer et rejouer le trafic, confirmant nos découvertes des deux interactions précédentes.

Cette liste de techniques n'est pas exhaustive, mais pour certains cas comme celui-ci, ils vous donneront un bon départ.

Comme d'habitude, veuillez partager vos commentaires ! Engageons une conversation pour que tout le monde apprenne un peu.