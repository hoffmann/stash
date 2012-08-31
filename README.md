stash
=====

[Python Logging Handler][python-logging] that emits [logstash][]/[kibana][] compatible records to [elasticsearch].



[logstash]: http://logstash.net/
[kibana]: http://rashidkpc.github.com/Kibana/
[elasticsearch]: http://www.elasticsearch.org/
[python-logging]: http://docs.python.org/library/logging.handlers.html



The logstash convention is to use a new index named 'logstash-YYYY-MM-DD' for every day.
A logstash/kibana compatible record format looks like:

    {
        "@fields": {
            "_function": "<module>", 
            "_pid": 10175, 
            "_process_name": "MainProcess", 
            "_thread_name": "MainThread", 
            "facility": "test_logger", 
            "file": "<ipython-input-8-25a8c050cea1>", 
            "full_message": "", 
            "host": "mir", 
            "level": 7, 
            "line": 1, 
            "short_message": "Hello Graylog2.", 
            "timestamp": 1346365351.338272, 
            "version": "1.0"
        }, 
        "@message": "", 
        "@source": "gelf://mir/<ipython-input-8-25a8c050cea1>", 
        "@source_host": "gelf://mir/<ipython-input-8-25a8c050cea1>", 
        "@source_path": "/", 
        "@tags": [], 
        "@timestamp": "2012-08-30T22:22:31.339000Z", 
        "@type": "gelf-test"
    }

## Usage

    import logging
    import stash
    sh = stash.StashHandler('127.0.0.1:9200')
    logger = logging.getLogger()
    logger.addHandler(sh)
    logger.warning('Test Message')



This logging hander should only be used in development when you don't want to set up and configure a
logstash server. In production mode you should consider the python gelf handler [grapy][].

[graypy]: http://pypi.python.org/pypi/graypy

## Requirements

* [pyes][]
* running [elasticsearch][] server

[pyes]: https://github.com/aparo/pyes

