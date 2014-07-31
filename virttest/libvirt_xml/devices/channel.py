"""
Classes to support XML for channel devices

http://libvirt.org/formatdomain.html#elementCharSerial
"""

from virttest.libvirt_xml import base
from virttest.libvirt_xml import accessors
from virttest.libvirt_xml.devices.character import CharacterBase


class Channel(CharacterBase):

    __slots__ = ('source', 'target',)

    def __init__(self, type_name='unix', virsh_instance=base.virsh):
        accessors.XMLElementDict('source', self, parent_xpath='/',
                                 tag_name='source')
        accessors.XMLElementDict('target', self, parent_xpath='/',
                                 tag_name='target')
        super(
            Channel, self).__init__(device_tag='channel', type_name=type_name,
                                    virsh_instance=virsh_instance)
