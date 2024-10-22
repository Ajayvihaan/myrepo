from ruamel.yaml import YAML

# Create a YAML instance
yaml = YAML()

# Load the YAML file
with open('config.yml', 'r') as file:
    config = yaml.load(file)

# Accessing the data
print("Database Host:", config['database']['host'])
print("Database Port:", config['database']['port'])
print("Logging Level:", config['logging']['level'])

