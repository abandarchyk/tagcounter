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


#filter func
def get_site(host):
    sites = config['sites']
    site = [site for site in sites.values() if site['host'] == host][0]
    print(site)
    return site



# todo parse_props

# todo create site class to use methods
