"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.ausbildungssuche.model.response_embedded_termine_inner_adresse_ort_strasse_koordinaten import (
    ResponseEmbeddedTermineInnerAdresseOrtStrasseKoordinaten,
)
from deutschland.ausbildungssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter_adresse_ort_strasse_land import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresseOrtStrasseLand,
)

from deutschland import ausbildungssuche

globals()[
    "ResponseEmbeddedTermineInnerAdresseOrtStrasseKoordinaten"
] = ResponseEmbeddedTermineInnerAdresseOrtStrasseKoordinaten
globals()[
    "ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresseOrtStrasseLand"
] = ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresseOrtStrasseLand
from deutschland.ausbildungssuche.model.response_embedded_termine_inner_adresse_ort_strasse import (
    ResponseEmbeddedTermineInnerAdresseOrtStrasse,
)


class TestResponseEmbeddedTermineInnerAdresseOrtStrasse(unittest.TestCase):
    """ResponseEmbeddedTermineInnerAdresseOrtStrasse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseEmbeddedTermineInnerAdresseOrtStrasse(self):
        """Test ResponseEmbeddedTermineInnerAdresseOrtStrasse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseEmbeddedTermineInnerAdresseOrtStrasse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
