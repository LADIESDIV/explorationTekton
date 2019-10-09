import yaml
import logging

logger = logging.getLogger(__name__)

NUMBER_OF_TESTS = 10

# load log config file
with open("/workspace/git-repo/appli/log_spec.yaml", "r") as log_spec_file:
    logging.config.dictConfig(yaml.load(log_spec_file))
