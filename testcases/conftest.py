import pytest

from common.yaml_util import YamlUtil

@pytest.fixture(scope="session",autouse=True)
def clear_yaml(path="/data/extract"):
    YamlUtil().clear_extract_yaml(path)
