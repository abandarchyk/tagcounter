import yaml
from tagcounter import tclogger

logger = tclogger.get_logger(__name__)


# YAML
with open('tagcounter/conf/config.yaml', 'r') as config_file:
    config = yaml.load(config_file)


def get_url(user_input: str):
    logger.debug('Checking if site=' + user_input + ' already exists in the config')
    site = dict(config['sites']).get(user_input, None)
    result = site['url'] if site is not None else None
    logger.debug('Found: ' + str(result))
    return result


def get_sites_urls():
    sites = config['sites']
    urls = [site['url'] for site in sites.values()]
    return urls
