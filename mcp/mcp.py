"""
 Copyright (c) 2020 4masaka

 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from thrift.protocol.TCompactProtocol import TCompactProtocolAccelerated


class TMoreCompactProtocol(TCompactProtocolAccelerated):
    def __init__(self, trans, string_length_limit=None, container_length_limit=None):
        super().__init__(trans, string_length_limit, container_length_limit)
        pass