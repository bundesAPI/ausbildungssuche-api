"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.ausbildungssuche.model.response_aggregations_beginntermin309 import (
    ResponseAggregationsBEGINNTERMIN309,
)

from deutschland import ausbildungssuche


class TestResponseAggregationsBEGINNTERMIN309(unittest.TestCase):
    """ResponseAggregationsBEGINNTERMIN309 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseAggregationsBEGINNTERMIN309(self):
        """Test ResponseAggregationsBEGINNTERMIN309"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseAggregationsBEGINNTERMIN309()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
