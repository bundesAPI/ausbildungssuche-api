"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 1c852184-1944-4a9e-a093-5cc078981294  **ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.ausbildungssuche.api_client import ApiClient
from deutschland.ausbildungssuche.api_client import Endpoint as _Endpoint
from deutschland.ausbildungssuche.model.response import Response
from deutschland.ausbildungssuche.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ausbildungssuche_endpoint = _Endpoint(
            settings={
                "response_type": (Response,),
                "auth": ["clientCredAuth"],
                "endpoint_path": "/pc/v1/ausbildungsangebot",
                "operation_id": "ausbildungssuche",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "sty",
                    "ids",
                    "orte",
                    "page",
                    "uk",
                    "re",
                    "bart",
                    "ityp",
                    "bt",
                    "ban",
                    "bg",
                ],
                "required": [],
                "nullable": [],
                "enum": [
                    "sty",
                    "uk",
                    "re",
                    "bart",
                    "ityp",
                    "bt",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("sty",): {"0": 0, "1": 1, "2": 2, "3": 3},
                    ("uk",): {
                        "BUNDESWEIT": "Bundesweit",
                        "25": "25",
                        "50": "50",
                        "100": "100",
                        "150": "150",
                        "200": "200",
                    },
                    ("re",): {
                        "BAW": "BAW",
                        "BAY": "BAY",
                        "BER": "BER",
                        "BRA": "BRA",
                        "BRE": "BRE",
                        "HAM": "HAM",
                        "HES": "HES",
                        "MBV": "MBV",
                        "NDS": "NDS",
                        "NRW": "NRW",
                        "RPF": "RPF",
                        "SAA": "SAA",
                        "SAC": "SAC",
                        "SAN": "SAN",
                        "SLH": "SLH",
                        "TH%C3%9C": "TH%C3%9C",
                        "-": "-",
                    },
                    ("bart",): {
                        "0": 0,
                        "100": 100,
                        "101": 101,
                        "102": 102,
                        "103": 103,
                        "104": 104,
                        "105": 105,
                        "106": 106,
                        "107108": 107108,
                        "109": 109,
                    },
                    ("ityp",): {"0": 0, "1": 1},
                    ("bt",): {
                        "2": 2,
                        "101": 101,
                        "102": 102,
                        "103": 103,
                        "104": 104,
                        "105": 105,
                        "106": 106,
                        "107": 107,
                        "108": 108,
                        "109": 109,
                        "110": 110,
                        "111": 111,
                        "112": 112,
                    },
                },
                "openapi_types": {
                    "sty": (int,),
                    "ids": (int,),
                    "orte": (int,),
                    "page": (int,),
                    "uk": (str,),
                    "re": (str,),
                    "bart": (int,),
                    "ityp": (int,),
                    "bt": (int,),
                    "ban": (int,),
                    "bg": (bool,),
                },
                "attribute_map": {
                    "sty": "sty",
                    "ids": "ids",
                    "orte": "orte",
                    "page": "page",
                    "uk": "uk",
                    "re": "re",
                    "bart": "bart",
                    "ityp": "ityp",
                    "bt": "bt",
                    "ban": "ban",
                    "bg": "bg",
                },
                "location_map": {
                    "sty": "query",
                    "ids": "query",
                    "orte": "query",
                    "page": "query",
                    "uk": "query",
                    "re": "query",
                    "bart": "query",
                    "ityp": "query",
                    "bt": "query",
                    "ban": "query",
                    "bg": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def ausbildungssuche(self, **kwargs):
        """Ausbildungssuche  # noqa: E501

        Die Ausbildungssuche ermöglicht verfügbare Angebote mit dem Ziel einer Berufsausbildung, Schulabschluss, Ausbildungsvorbereitung oder -begleitung mit verschiedenen GET-Parametern zu filtern.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ausbildungssuche(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sty (int): sty - 0=Berufsausbildung; 1=Schulabschluss; 2=Vorbereitung auf Aus- und Weiterbildung oder berufliche Tätigkeit; 3=Begleitende Hilfen.. [optional]
            ids (int): Berufs-ID einer Berufsbezeichnung. Mehrere Komma-getrennte Angaben möglich.. [optional]
            orte (int): ID eines Ortes. Mehrere Komma-getrennte Angaben möglich.. [optional]
            page (int): Ergebnissseite. [optional]
            uk (str): Umkreis - Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km.. [optional]
            re (str): Region/Bundesland - BAW=Bade-Württemberg, BAY=Bayern, BER=Berlin, BRA=Brandenburg, BRE=Bremen, HAM=Hamburg, HES=Hessen, MBV=Mecklenburg-Vorpommern, NDS=Niedersachsen, NRW=Nordrhein-Westfalen, RPF=Rheinland-Pfalz, SAA=Saarland, SAC=Sachsen, SAN=Sachsen-Anhalt, SLH=Schleswig-Holstein, THÜ=Thüringen, -=überregional. Mehrere Komma-getrennte Angaben möglich (z.B. re=THÜ,BAW).. [optional]
            bart (int): Ausbildungstyp - 0=Keine Zuordnung möglich, 100=Allgemeinbildung, 101=Teilqualifizierung, 102=Berufsausbildung, 103=Gesetzlich/gesetzesähnlich geregelte Fortbildung/Qualifizierung, 104=Fortbildung/Qualifizierung, 105=Abschluss nachholen, 106=Rehabilitation,  107108=Studienangebot - grundständig, 109=Umschulung. [optional]
            ityp (int): Integrationstyp - 0=Ausbildung Reha, 1=weiterbildung Reha. Mehrere Komma-getrennte Angaben möglich.. [optional]
            bt (int): Beginntermin - 2=frühere Termine, 101=Januar des Folgejahres, 102=Februar des Folgejahres, 103=März des Folgejahres, 104=April des Folgejahres, 105=Mai des Folgejahres, 106=Juni des Folgejahres, 107=Juli des Folgejahres, 108=August des Folgejahres, 109=September des Folgejahres, 110=Oktober des Folgejahres, 111=November des Folgejahres, 112=Dezember des Folgejahres. Mehrere Komma-getrennte Angaben möglich.. [optional]
            ban (int): Bildungsanbieter-ID. Mehrere Komma-getrennte Angaben möglich.. [optional]
            bg (bool): Bildungsgutschein - true=nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen, false=nicht nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.ausbildungssuche_endpoint.call_with_http_info(**kwargs)
