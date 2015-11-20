# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Serializer, Deserializer
from msrest.service_client import async_request
from msrest.exceptions import (
    DeserializationError,
    HttpOperationError)
import uuid

from ..models import *


class parameter_groupingOperations(object):

    def __init__(self, client, config, serializer, derserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = derserializer

        self.config = config

    def _serialize_data(self, name, value, datatype, **kwargs):

        try:
            value = self._serialize.serialize_data(value, datatype, **kwargs)

        except ValueError:
            raise ValueError("{} must not be None.".format(name))

        except DeserializationError:
            raise TypeError("{} must be type {}.".format(name, datatype))

        else:
            return value

    @async_request
    def post_required(self, parameter_grouping_post_required_parameters, custom_headers={}, raw=False, callback=None):
        """

        Post a bunch of required parameters grouped

        :param parameter_grouping_post_required_parameters: Additional
        parameters for the operation
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type parameter_grouping_post_required_parameters: object
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        body = None
        if parameter_grouping_post_required_parameters is not None:
            body = parameter_grouping_post_required_parameters.body
        custom_header = None
        if parameter_grouping_post_required_parameters is not None:
            custom_header = parameter_grouping_post_required_parameters.custom_header
        query = None
        if parameter_grouping_post_required_parameters is not None:
            query = parameter_grouping_post_required_parameters.query
        path = None
        if parameter_grouping_post_required_parameters is not None:
            path = parameter_grouping_post_required_parameters.path

        # Construct URL
        url = '/parameterGrouping/postRequired/{path}'
        path_format_arguments = {
            'path': self._serialize_data("path", path, 'str')
        }
        url = url.format(**path_format_arguments)

        # Construct parameters
        query = {}
        if query is not None:
            query['query'] = self._serialize_data("query", query, 'int')

        # Construct headers
        headers = {}
        if self.config.accept_language is not None:
            headers['accept-language'] = self._serialize_data("self.config.accept_language", self.config.accept_language, 'str')
        if custom_header is not None:
            headers['customHeader'] = self._serialize_data("custom_header", custom_header, 'str')
        headers.update(custom_headers)
        headers['x-ms-client-request-id'] = str(uuid.uuid1())
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(body, 'int')

        # Construct and send request
        request = self._client.post(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def post_optional(self, parameter_grouping_post_optional_parameters, custom_headers={}, raw=False, callback=None):
        """

        Post a bunch of optional parameters grouped

        :param parameter_grouping_post_optional_parameters: Additional
        parameters for the operation
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type parameter_grouping_post_optional_parameters: object or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        custom_header = None
        if parameter_grouping_post_optional_parameters is not None:
            custom_header = parameter_grouping_post_optional_parameters.custom_header
        query = None
        if parameter_grouping_post_optional_parameters is not None:
            query = parameter_grouping_post_optional_parameters.query

        # Construct URL
        url = '/parameterGrouping/postOptional'

        # Construct parameters
        query = {}
        if query is not None:
            query['query'] = self._serialize_data("query", query, 'int')

        # Construct headers
        headers = {}
        if self.config.accept_language is not None:
            headers['accept-language'] = self._serialize_data("self.config.accept_language", self.config.accept_language, 'str')
        if custom_header is not None:
            headers['customHeader'] = self._serialize_data("custom_header", custom_header, 'str')
        headers.update(custom_headers)
        headers['x-ms-client-request-id'] = str(uuid.uuid1())
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.post(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def post_multiple_parameter_groups(self, first_parameter_group, parameter_grouping_post_multiple_parameter_groups_second_parameter_group, custom_headers={}, raw=False, callback=None):
        """

        Post parameters from multiple different parameter groups

        :param first_parameter_group: Additional parameters for the operation
        :param
        parameter_grouping_post_multiple_parameter_groups_second_parameter_group:
        Additional parameters for the operation
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type first_parameter_group: object or none
        :type
        parameter_grouping_post_multiple_parameter_groups_second_parameter_group:
        object or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        header_one = None
        if first_parameter_group is not None:
            header_one = first_parameter_group.header_one
        query_one = None
        if first_parameter_group is not None:
            query_one = first_parameter_group.query_one
        header_two = None
        if parameter_grouping_post_multiple_parameter_groups_second_parameter_group is not None:
            header_two = parameter_grouping_post_multiple_parameter_groups_second_parameter_group.header_two
        query_two = None
        if parameter_grouping_post_multiple_parameter_groups_second_parameter_group is not None:
            query_two = parameter_grouping_post_multiple_parameter_groups_second_parameter_group.query_two

        # Construct URL
        url = '/parameterGrouping/postMultipleParameterGroups'

        # Construct parameters
        query = {}
        if query_one is not None:
            query['query-one'] = self._serialize_data("query_one", query_one, 'int')
        if query_two is not None:
            query['query-two'] = self._serialize_data("query_two", query_two, 'int')

        # Construct headers
        headers = {}
        if self.config.accept_language is not None:
            headers['accept-language'] = self._serialize_data("self.config.accept_language", self.config.accept_language, 'str')
        if header_one is not None:
            headers['header-one'] = self._serialize_data("header_one", header_one, 'str')
        if header_two is not None:
            headers['header-two'] = self._serialize_data("header_two", header_two, 'str')
        headers.update(custom_headers)
        headers['x-ms-client-request-id'] = str(uuid.uuid1())
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.post(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def post_shared_parameter_group_object(self, first_parameter_group, custom_headers={}, raw=False, callback=None):
        """

        Post parameters with a shared parameter group object

        :param first_parameter_group: Additional parameters for the operation
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type first_parameter_group: object or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        header_one = None
        if first_parameter_group is not None:
            header_one = first_parameter_group.header_one
        query_one = None
        if first_parameter_group is not None:
            query_one = first_parameter_group.query_one

        # Construct URL
        url = '/parameterGrouping/sharedParameterGroupObject'

        # Construct parameters
        query = {}
        if query_one is not None:
            query['query-one'] = self._serialize_data("query_one", query_one, 'int')

        # Construct headers
        headers = {}
        if self.config.accept_language is not None:
            headers['accept-language'] = self._serialize_data("self.config.accept_language", self.config.accept_language, 'str')
        if header_one is not None:
            headers['header-one'] = self._serialize_data("header_one", header_one, 'str')
        headers.update(custom_headers)
        headers['x-ms-client-request-id'] = str(uuid.uuid1())
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.post(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response
