"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.ausbildungssuche.model.response_aggregations_anbieter227923 import (
    ResponseAggregationsANBIETER227923,
)

from deutschland import ausbildungssuche


class TestResponseAggregationsANBIETER227923(unittest.TestCase):
    """ResponseAggregationsANBIETER227923 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseAggregationsANBIETER227923(self):
        """Test ResponseAggregationsANBIETER227923"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseAggregationsANBIETER227923()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
