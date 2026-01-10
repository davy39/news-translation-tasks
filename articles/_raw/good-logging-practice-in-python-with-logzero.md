---
title: How to Practice Logging in Python with Logzero
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-13T21:26:52.000Z'
originalURL: https://freecodecamp.org/news/good-logging-practice-in-python-with-logzero
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/logezero-image.png
tags:
- name: logging
  slug: logging
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Davis David

  Logzero is a Python package created by Chris Hager that simplifies logging with
  Python 2 and 3. Logzero makes it easier as a print statement to show information
  and debugging details.

  If you are wondering what logging is, I recommend t...'
---

By Davis David

Logzero is a Python package created by [Chris Hager](https://twitter.com/metachris) that simplifies logging with Python 2 and 3. Logzero makes it easier as a print statement to show information and debugging details.

If you are wondering **what logging is**, I recommend that you read the previous article I wrote about [“How to Run Machine Learning Experiments with Python Logging Module”](https://medium.com/analytics-vidhya/how-to-run-machine-learning-experiments-with-python-logging-module-9030fbee120e), especially the first 3 sections. 

In that article, you will learn:

* What is Logging?
* Why logging is important.
* Applications of logging in different technology industries.

Logzero has different features that make it easier to use in Python projects. Some of these features are:

* Easy logging to console and/or file.
* Provides a fully configured standard Python logger object.
* Pretty formatting, including level-specific **colors** in the console.
* works with all kinds of character encodings and special characters.
* Compatible with Python 2 and 3.
* No further Python dependencies.

## Installation

To install logzero with pip run the following:

```python
pip install -U logzero
```

You can also install logzero from the public [Github repo](https://github.com/metachris/logzero):

```
git clone https://github.com/metachris/logzero.git
cd logzero
python setup.py install
```

## Basic Example

We will start with a basic example. In the python file, we will import the logger from logzero and try 4 different logging level examples.

```python
#import logger from logzero
from logzero import logger

logger.debug("hello")
logger.info("info")
logger.warning("warning")
logger.error("error")
```

The output is colored so it's easy to read.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/dfdfdf.PNG)
_logzero output_

As you can see each level has its own color. This means you can identify the level easily by checking the color.

## Write logs to a file

Most of the time Python users tend to write logs in the file. When the system is running you can save logs in the file and review them for error checks and maintenance purposes. You can also set a file to save all the log entries in legzero.

We will import the logger and logfile from logezero. The logfile method will help us configure the log file to save our log entries.

Now your log entries will be logged into the file named my_logfile.log.

```python
#import logger and logfile
from logzero import logger, logfile

#set logfile path
logfile('my_logfile.log')

# Log messages
logger.info("This log message saved in the log file")
```

The output in the my_logfile.log contains the logging level label (for info level labeled as “I”), date, time, python filename, line number and the message itself.

```
[I 200409 23:49:59 demo:8] This log message saved in the log file
```

## Rotating a log file

You don't need to have a single log file saving all the log entries. This results in a massive log file that is intensive for the system to open and close.

You can use the **maxBytes** and **backupCount** parameters to allow the file to roll over at a predetermined size. When the size is about to be exceeded, the file is closed and a new file is silently opened for output. Rollover occurs whenever the current log file is nearly maxBytes in length. If either maxBytes or backupCount is zero, rollover never occurs.

In the example below, we have set the maxBytes to be **1000000 bytes (1 MB).** This means that when the size exceeds 1MB the file is closed and a new file is opened to save log entries. The number of backups to keep is set to 3.

```python
# Set a rotating logfile
logzero.logfile("my_logfile.log", maxBytes=1000000, backupCount=3)
```

## Set a Minimum Logging Level

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_5vfxSz_sdZuPR0CnnBlDLg.png)
_[Photo by Son Nguyen Kim](https://www.toptal.com/resume/son-nguyen-kim?__hstc=753710.17be834d28ba29055621f0833fc6733b.1582400164835.1582400164835.1582400164835.1&amp;__hssc=753710.1.1582400164836&amp;__hsfp=3618320745" rel="noopener nofollow noopener)_

The logging level means to set the importance level of a given log message. You can also set a different **log level** for the file handler by using the loglevel argument in the logfile method.

In the example below, we set loglevel to be `warning`. This means all log entries below the **warning level** will not be saved into a log file.

```python
#import logzero package
from logzero import logger, logfile
import logging

# You can also set a different loglevel for the file handler
logfile("my_logfile.log", loglevel=logging.WARNING)

# Log messages
logger.info("This log message saved in the log file")
logger.warning("This log message saved in the log file")
```

## Set a custom formatter

How you want the log record to be formated is up to you. There are different ways you can format your log record. You can include the date, time and logging level in your format so that you know when the log was sent and at what level. 

The example below shows how you can configure the format of the log records.

```python
#import logzero package
import logzero
from logzero import logger, logfile
import logging

#set file path
logfile("my_logfile.log")

# Set a custom formatter
my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');
logzero.formatter(my_formatter)

# Log messages
logger.info("This log message saved in the log file")
logger.warning("This log message saved in the log file")
```

In the example above we have configured the log format by including _filename, date, time, logging level name,_ and _message._

This is the output in the my_logfile.log:

```
demo.py - 2020–04–10 00:51:44,706 - INFO: This log message saved in the log file
demo.py - 2020–04–10 00:51:44,707 - WARNING: This log message saved in the log file
```

## Custom Logger Instances

Instead of using the default logger, you can also setup specific logger instances with **logzero.setup_logger(..)**. You can configure and returns a fully configured logger instance with different parameters such as _name, logfile name, formatter, maxBytes, backupCount,_ and _logging level._

This is a working example of how to setup logging with a custom logger instance:

```python
import logzero package
from logzero import logger, logfile, setup_logger
import logging

# Set a custom formatter
my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');


#create custom logger instance
custom_logger = setup_logger(
 name="My Custom Logger",
 logfile="my_logfile.log",
 formatter=my_formatter,
 maxBytes=1000000,
 backupCount=3,level=logging.INFO)

# Log messages
custom_logger.info("This log message saved in the log file")
custom_logger.warning("This log message saved in the log file")
```

In the example above we have set a custom logger instance called **custom_logger** with different configured parameter values.

## Wrap up

In this article, you've learned the basics, along with some examples, of how to use the Logezero Python package. You can learn more about the features available in the [documentation](https://logzero.readthedocs.io/en/latest/#). Now you can start implementing the logzero package in your next [python project](https://realpython.com/intermediate-python-project-ideas/).

If you learned something new or enjoyed reading this article, please share it so that others can see it. Until then, see you in the next post! I can also be reached on Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid)

