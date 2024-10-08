"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.ausbildungssuche.model.response_embedded_termine_inner_adresse import (
    ResponseEmbeddedTermineInnerAdresse,
)
from deutschland.ausbildungssuche.model.response_embedded_termine_inner_angebot import (
    ResponseEmbeddedTermineInnerAngebot,
)
from deutschland.ausbildungssuche.model.response_embedded_termine_inner_dauer import (
    ResponseEmbeddedTermineInnerDauer,
)
from deutschland.ausbildungssuche.model.response_embedded_termine_inner_unterrichtsform import (
    ResponseEmbeddedTermineInnerUnterrichtsform,
)

from deutschland import ausbildungssuche

globals()["ResponseEmbeddedTermineInnerAdresse"] = ResponseEmbeddedTermineInnerAdresse
globals()["ResponseEmbeddedTermineInnerAngebot"] = ResponseEmbeddedTermineInnerAngebot
globals()["ResponseEmbeddedTermineInnerDauer"] = ResponseEmbeddedTermineInnerDauer
globals()[
    "ResponseEmbeddedTermineInnerUnterrichtsform"
] = ResponseEmbeddedTermineInnerUnterrichtsform
from deutschland.ausbildungssuche.model.response_embedded_termine_inner import (
    ResponseEmbeddedTermineInner,
)


class TestResponseEmbeddedTermineInner(unittest.TestCase):
    """ResponseEmbeddedTermineInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseEmbeddedTermineInner(self):
        """Test ResponseEmbeddedTermineInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseEmbeddedTermineInner()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
