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


Module: TranscriptManager
=========================


"""

from isomer.component import ConfigurableComponent
from isomer.logger import warn  # , isomerlog, error, critical


# from isomer.database import objectmodels
# from datetime import datetime
# from isomer.events.system import updatesubscriptions, send


class TranscriptManager(ConfigurableComponent):
    """
    The Transcript component monitors transcript changes. It does not do much.
    """
    channel = 'isomer-web'

    configprops = {
    }

    def __init__(self, *args):
        """
        Initialize the Transcript component.

        :param args:
        """

        super(TranscriptManager, self).__init__("TRANSCRIPT", *args)

        self.log("Started")

    def objectcreation(self, event):
        if event.schema == 'transcript':
            self.log("Transcriptconfig was modified: ", event)
