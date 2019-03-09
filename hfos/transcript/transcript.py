#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""
Schema: Transcript
==================

Contains
--------

transcript: Structure to store transcriptions of meetings,

"""

from isomer.schemata.defaultform import *
from isomer.schemata.base import base_object

TranscriptSchema = base_object('transcript')

TranscriptSchema['properties'].update({
    'locked': {
        'type': 'boolean', 'title': 'Locked Transcript',
        'description': 'Determines whether the Transcript should '
                       'be locked against changes.'
    },
    'description': {
        'type': 'string', 'format': 'html',
        'title': 'Transcript description',
        'description': 'Transcript description'
    },
    'content': {
        'type': 'string', 'format': 'html', 'title': 'Transcript content',
        'description': 'Content'
    },
})

TranscriptForm = [
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'name',
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'locked'
                ]
            },
        ]
    },
    'description',
    'content',
    editbuttons
]

Transcript = {'schema': TranscriptSchema, 'form': TranscriptForm}
