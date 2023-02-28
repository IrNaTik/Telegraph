import pathlib
import yaml
import aiohttp_debugtoolbar


BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'config.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
        
    return config
    
config = get_config(config_path)

# develop mode
def setup_static(app):
    app.router.add_static('/static/',
                          path= BASE_DIR / 'static' ,
                          name='static')
    
