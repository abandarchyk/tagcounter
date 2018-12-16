import yaml

# YAML
with open('conf/config.yaml', 'r') as config_file:
    config = yaml.load(config_file)


#filter func
def get_site(host):
    sites = config['sites']
    site = [site for site in sites.values() if site['host'] == host][0]
    print(site)
    return site

# todo parse_props

# todo create site class to use methods
