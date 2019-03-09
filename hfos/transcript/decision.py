#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer Application Framework
# ============================
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
from schemata.base import base_object

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""
Schema: Decision
================

Contains
--------

Decision: Stores decisions of a gremium


"""

from isomer.schemata.defaultform import *

# TODO: Convert to base_object

DecisionSchema = base_object('decision', roles_write='owner', roles_read='crew')
DecisionSchema['properties'].update({
    'votes_for': {'type': 'integer'},
    'votes_against': {'type': 'integer'},
    'votes_undecided': {'type': 'integer'}
})

DecisionForm = [
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'name'
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'votes_for', 'votes_undecided', 'votes_against'
                ]
            },
        ]
    },
    editbuttons
]

Decision = {'schema': DecisionSchema, 'form': DecisionForm}
