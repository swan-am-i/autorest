# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CustomDomain(Model):
    """
    The custom domain assigned to this storage account. This can be set via
    Update.

    :param name: Gets or sets the custom domain name. Name is the CNAME
     source.
    :type name: str
    :param use_sub_domain: Indicates whether indirect CName validation is
     enabled. Default value is false. This should only be set on updates
    :type use_sub_domain: bool
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'use_sub_domain': {'key': 'useSubDomain', 'type': 'bool'},
    }

    def __init__(self, name=None, use_sub_domain=None):
        self.name = name
        self.use_sub_domain = use_sub_domain
