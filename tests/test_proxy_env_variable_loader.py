import os
import unittest

from slack_sdk.proxy_env_variable_loader import load_http_proxy_from_env
from tests.helpers import remove_os_env_temporarily, restore_os_env


class TestProxyEnvVariableLoader(unittest.TestCase):
    def setUp(self):
        self.old_env = remove_os_env_temporarily()

    def tearDown(self):
        restore_os_env(self.old_env)

    def test_load_lower_case(self):
        os.environ["https_proxy"] = "http://localhost:9999"
        url = load_http_proxy_from_env()
        self.assertEqual(url, "http://localhost:9999")

    def test_load_upper_case(self):
        os.environ["HTTPS_PROXY"] = "http://localhost:9999"
        url = load_http_proxy_from_env()
        self.assertEqual(url, "http://localhost:9999")
