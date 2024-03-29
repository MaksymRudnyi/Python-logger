import logging
from cmreslogging.handlers import CMRESHandler
handler = CMRESHandler(hosts=[{'host': 'localhost', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="my_python_index")
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

log = logging.getLogger("PythonTest")
log.setLevel(logging.INFO)
log.addHandler(handler)
