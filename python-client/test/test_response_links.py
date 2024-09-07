"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.ausbildungssuche.model.response_links_first import ResponseLinksFirst
from deutschland.ausbildungssuche.model.response_links_last import ResponseLinksLast
from deutschland.ausbildungssuche.model.response_links_next import ResponseLinksNext
from deutschland.ausbildungssuche.model.response_links_self import ResponseLinksSelf

from deutschland import ausbildungssuche

globals()["ResponseLinksFirst"] = ResponseLinksFirst
globals()["ResponseLinksLast"] = ResponseLinksLast
globals()["ResponseLinksNext"] = ResponseLinksNext
globals()["ResponseLinksSelf"] = ResponseLinksSelf
from deutschland.ausbildungssuche.model.response_links import ResponseLinks


class TestResponseLinks(unittest.TestCase):
    """ResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseLinks(self):
        """Test ResponseLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
