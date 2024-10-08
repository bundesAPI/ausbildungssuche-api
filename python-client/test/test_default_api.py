"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import unittest

from deutschland.ausbildungssuche.api.default_api import DefaultApi  # noqa: E501

from deutschland import ausbildungssuche


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ausbildungsdetails(self):
        """Test case for ausbildungsdetails

        Ausbildungsdetails  # noqa: E501
        """
        pass

    def test_ausbildungssuche(self):
        """Test case for ausbildungssuche

        Ausbildungssuche  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
