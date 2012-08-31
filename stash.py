import logging
from pyes import ES
import datetime

class StashHandler(logging.Handler):
    def __init__(self, constr, whitelist=None, blacklist=None):
        logging.Handler.__init__(self)
        self.conn = ES(constr)
        if blacklist is None:
            blacklist = set()
        self.whitelist = whitelist
        self.blacklist = blacklist
        self.record_type = 'record'

    @property
    def index_name(self):
        return 'logstash-'+datetime.date.today().strftime('%Y.%m.%d')

    def emit(self, record):
        if self.whitelist is None:
            d = { k: record.__dict__[k] for k in record.__dict__ if k not in self.blacklist }
        else:
            d = { k: record.__dict__[k] for k in record.__dict__ if k in self.whitelist and k not in self.blacklist }
        entry = {
            "@fields": d,
            "@message": record.msg, 
            "@source": "gelf://localhost", 
            "@source_host": "gelf://localhost", 
            "@source_path": "/", 
            "@tags": [], 
            "@timestamp": datetime.datetime.utcnow().isoformat(), 
            "@type": self.record_type}
        self.conn.index(entry, self.index_name, self.record_type)


