"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert über die clientId der Ausbildungssuchesuche, die einem GET-request an         https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:  **clientId:** infosysbub-absuche  Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.ausbildungssuche.model.response_aggregations_beginntermin102 import (
    ResponseAggregationsBEGINNTERMIN102,
)

from deutschland import ausbildungssuche


class TestResponseAggregationsBEGINNTERMIN102(unittest.TestCase):
    """ResponseAggregationsBEGINNTERMIN102 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseAggregationsBEGINNTERMIN102(self):
        """Test ResponseAggregationsBEGINNTERMIN102"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseAggregationsBEGINNTERMIN102()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
