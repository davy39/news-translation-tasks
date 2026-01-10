---
title: The voice memo’s BFF — how to make Speech2Text easy with Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:07:43.000Z'
originalURL: https://freecodecamp.org/news/the-voice-memos-bff-speech-to-text-powered-by-machine-learning-1dbc7a6c65f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9NU-RPt9yreyuqqOLQKQYA.jpeg
tags:
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Machine Learning
  slug: machine-learning
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Rafael Belchior

  Do you think recording voice memos is inconvenient because you have to transcribe
  them? Do you waste your precious voice memos because you never write them down?
  Do you feel like you are not unlocking the full potential of what you...'
---

By Rafael Belchior

Do you think recording voice memos is inconvenient because you have to transcribe them? Do you waste your precious voice memos because you never write them down? Do you feel like you are not unlocking the full potential of what you record?

Yeah, that sucks. ?

![Image](https://cdn-media-1.freecodecamp.org/images/Ldug-95Ai5jva-tYYx4uQTcqzRj7bAFHqdsa)
_Write, write, write._

I’m a Computer Science masters student. As I think that all work and no play makes me a dull boy, I’ve decided to invest some time in doing something different. Where? In the [student’s group to which I belong](http://www.gce-neiist.org), [by interviewing a professor.](http://www.gce-neiist.org/articles)

I’ve talked to professor Rui Henriques, a teacher assistant @ Técnico Lisboa and researcher @ INESC-ID. He is an expert in Data Mining and Bioinformatics. The 20 minutes interview turned into almost a full hour conversation.

Rui is not only a brilliant academic but also a very honest, cheerful and easy going person, which made it very easy. I learned a lot while talking to him, and I’m sure you also can. The interview will be online soon enough. ?

Anyway, I had a problem and a need. I wanted to save time by not having to transcribe the whole interview. The idea was to invest only twenty to sixty minutes in order to skyrocket performance when it comes to transcribing. This is not limited to interviews, of course. You can transcribe audio notes taken from several sources like classes, writing notes, thoughts, your shopping list, or your most philosophical pieces.

### So, how do we do that?

I’m also lecturing on [_It Infrastructure Management and Administration_](https://fenix.tecnico.ulisboa.pt/disciplinas/AGISIT/2018-2019/1-semestre) _@ [Técnico Lisboa](https://tecnico.ulisboa.pt/en/)._ In classes, we have used Google Cloud Engine. I remembered a service called [Google Speech-To-Text](https://cloud.google.com/speech-to-text/´), which we could use in this case. And no, [Google](https://www.freecodecamp.org/news/the-voice-memos-bff-speech-to-text-powered-by-machine-learning-1dbc7a6c65f1/undefined) is not paying me to write this ?

So, how to turn an interview of 55 minutes into easily editable text? How to reduce our efforts and focus on what matters? ?

? By the way, to make the most out of this method, please cut noise and try to record with a loud, clear voice. ?

### Step 1: Installing the required software

I use Vagrant to manage virtual machines. The advantage is that to use the environment you need to instantiate the Speech-To-Text service. [In this article, I show step by step how to configure these tools](https://hackernoon.com/devops101-vagrant-6737c8c29904) (read it up to the section “The Experiment”). If you prefer to do this on your local machine, go directly to the third step.

### Step 2: Start the virtual machine

Now, open your console and run:

```
$ vagrant up --provision && vagrant ssh
```

The virtual machine is booting, installing all the required dependencies. This may take a while.

Wait a bit. Done. Nice. Kudos to you ?

### Step 3: Getting the support files

[Fork this repository containing the support files](https://github.com/RafaelAPB/gce-speech2text) and then clone it to your computer. Put it in the folder that is being synced with your guest machine.

### Step 4: Creating an account at Google Cloud Engine

You can [require a free grant ($300)](https://cloud.google.com/free/) for this experiment ? After creating the account, go to G[oogle Console.](https://goo.gl/jo2qQL) Create a project. You can name it “easy-interview” if you are confident enough. You should see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/bjkBeRT3UGJIqilASbqpnwHS5amzLE4D5thc)

After that, go to “APIs & Services”, in order to activate the API we need to get the job done.

![Image](https://cdn-media-1.freecodecamp.org/images/6zhTG1GyeUS59a7hg5lCPUgytLIB6wr0Dky3)

Click on “Create Credentials”. Choose “Cloud Speech API”. On “Are you planning to use this API with App Engine or Compute Engine?” say “No”. On step 2, “Create a service account” name the service “transcribing”. The role is Project => Owner. Key type: JSON.

By now, you should have downloaded a file called “file.txt”. It contains the credentials you need to use the service. Rename the file to “terraform-credentials.json”. Copy it to the folder containing the support files. As that folder is synced with your virtual machine, you will have access to those files from the guest machine. Now, run:

```
$ gcloud auth login
```

Follow the instructions. Authenticate yourself following the link that is shown. Now, analyze the request.json file:

```
{  "config": {      "encoding":"FLAC",      "sampleRateHertz": 16000,      "languageCode": "en-US",      "enableWordTimeOffsets": false  },  "audio": {      "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"  }}
```

Make sure to tune the parameters to fit your case. Beware that there are limitations on the encoding that you can use. If your file is in a different format than _flac_ or _wav_, you will need to convert it. You can convert audio files with [Audacity](https://www.audacityteam.org/), a free, open-source audio software. After converting the audio, you have to upload it to Google Storage. For that, [you have to create a bucket](https://console.cloud.google.com/storage/).

![Image](https://cdn-media-1.freecodecamp.org/images/3TefQe9BJtLH7UJrI87F2cgaAIA2f3mSBabD)

The settings may be:

![Image](https://cdn-media-1.freecodecamp.org/images/s3XAjTQlz1H3VEQLaWnM9Xw1fFBwQb3kgq5H)

After that, upload your file to the bucket. On the Bucket menu, you should be able to access the URI associated with your file. The format is _gs://BUCKET/FILE.EXTENSION_. Take that URI and replace it on the file _my-request.json_.

Your file should look something like this:

```
{  "config": {      "encoding":"FLAC",      "sampleRateHertz": 16000,      "languageCode": "pt-PT",      "enableWordTimeOffsets": false  },  "audio": {      "uri":"gs://easy-interview/interview.flac"  }}
```

Before we use the API, we need to load the credentials. Run the script load-credentials.sh to load them:

```
$ source load-credentials.sh
```

This has set the GOOGLE_APPLICATION_CREDENTIAL environment variable. Next, to test if the connection is successful, run:

```
$ curl -s -H "Content-Type: application/json" \    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \    https://speech.googleapis.com/v1/speech:recognize \    -d @test-request.json
```

You should be able to see a response with some transcribed text. Note that we ran _test-request.json,_ which is just for testing purposes. Now, to make the call with your data, run:

```
$ curl -s -H "Content-Type: application/json" \    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \    https://speech.googleapis.com/v1/speech:longrunningrecognize \    -d @my-request.json >> name.out
```

If you run _more name.out,_ you will see that the response contains a field called name. That name corresponds to the operation name that was created to meet the request. Now you have to wait a bit until the operation completes. Run (replace NAME with your operation’s name):

```
$ curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \     -H "Content-Type: application/json; charset=utf-8" \     "https://speech.googleapis.com/v1/operations/NAME" >> result.out
```

While the operation doesn’t finish, your _result.out_ will have a content similar to this:

{  
 “name”: “8254262642733152416”,  
 “metadata”: {  
 “[@type](http://twitter.com/type)”: “type.googleapis.com/google.cloud.speech.v1.LongRunningRecognizeMetadata”,  
 “progressPercent”: 33,  
 “startTime”: “2018–12–08T01:15:08.969852Z”,  
 “lastUpdateTime”: “2018–12–08T01:19:25.105683Z”  
 }  
}

For a 60mb file, encoded with _flac_ , it took about 12 minutes. You will have a file called _results.out_ with your precious content. It will be in your host machine as well. I’ve written a very simple Python script that parses _results.out._ The script redirects the output to a file named _results-parsed.out_. To execute it, run:

```
$ python parse.py
```

If you don’t like the results, tune the parameters and try again.

Enjoy your content! You are done ? To finish this experiment, exit the machine:

```
$ gcemgmt: exit
```

Now, stop the virtual machine:

```
$ vagrant halt
```

**Don’t forget to delete the files that you uploaded to Google Cloud.**

Well done!?

Well, this took me several hours to write, but at least I didn’t have to transcribe the whole interview. ?

### Bottomline

Firstly, I would ❤️to hear your opinion! Do you record lots of voice memos? Do you find this procedure useful? Do you have a different one?

If you **liked this article**, please click the ? button on the left. D**o you have a friend or family member that would benefit from this solution? Share this article!**

_Keep Rocking_ ?

Entrepreneurship [?](https://emojipedia.org/fire/)

[**Top 8 lessons I’ve learned in European Innovation Academy 2017**](https://blog.startuppulse.net/top-8-lessons-ive-learned-in-european-innovation-academy-2017-50eeb82d74b4)  
[_Imagine you are seeing the opportunity to improve yourself at every level. Would you take it?_blog.startuppulse.net](https://blog.startuppulse.net/top-8-lessons-ive-learned-in-european-innovation-academy-2017-50eeb82d74b4)

**DevOps101** ☄️

[**DevOps101 — Improve Your Workflow! First Steps on Vagrant**](https://hackernoon.com/devops101-vagrant-6737c8c29904)  
[_And make clients and developers happier._hackernoon.com](https://hackernoon.com/devops101-vagrant-6737c8c29904)[**DevOps101 — Infrastructure as Code With Vagrant**](https://hackernoon.com/devops101-itinfrastructure-54337d6a148b)  
[_And deploying a simple IT infrastructure (Two LAMP web servers and a client machine)._hackernoon.com](https://hackernoon.com/devops101-itinfrastructure-54337d6a148b)

Blockchain For Students ⛓️

[**Blockchain For Students 101 -The Basics (Part 1)**](https://hackernoon.com/blockchain-for-students-101-the-basics-part-1-f39b8201a7d5)  
[_Are you ready to dig deep into this life-changing technology?_hackernoon.com](https://hackernoon.com/blockchain-for-students-101-the-basics-part-1-f39b8201a7d5)

