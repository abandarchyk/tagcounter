import yaml

# YAML
with open('conf/config.yaml', 'r') as config_file:
    config = yaml.load(config_file)


def get_url(user_input: str):
    print('Checking if site=' + user_input + ' already exists in the config')
    site = dict(config['sites']).get(user_input, None)
    result = site['url'] if site is not None else None
    print('Found: ' + str(result))
    return result


def get_sites_urls():
    sites = config['sites']
    urls = [site['url'] for site in sites.values()]
    return urls