import pytest

from common.yaml_util import YamlUtil


class TestSendRequest:

    @pytest.mark.parametrize("caseinfo",YamlUtil().read_extract_yaml("/data/get_token"))
    def test_get_token(self,caseinfo):
        pass
