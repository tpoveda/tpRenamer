#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains core implementation for Renamer Tool
"""

from __future__ import print_function, division, absolute_import

import os
import sys

from tpDcc.core import dcc, tool

from tpDcc.tools.renamer.core import consts, client, toolset


class RenamerTool(tool.DccTool, object):

    ID = consts.TOOL_ID
    CLIENT_CLASS = client.RenamerClient
    TOOLSET_CLASS = toolset.RenamerToolset

    def __init__(self, *args, **kwargs):
        super(RenamerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Renamer',
            'id': consts.TOOL_ID,
            'supported_dccs': {
                dcc.Dccs.Maya: ['2017', '2018', '2019', '2020, 2021'],
                dcc.Dccs.Max: ['2017.0', '2018.0', '2019.0', '2020.0', '2021.0'],
                # dcc.Dccs.MotionBuilder: ['2017', '2018', '2019', '2020, 2021'],
                # dcc.Dccs.Unreal: ['4.25.4-14469661+++UE4+Release-4.25'],
                # dcc.Dccs.Houdini: ['2017', '2018', '2019', '2020, 2021']
            },
            'logo': 'rename',
            'icon': 'rename',
            'tooltip': 'Renamer Tool to easily rename DCC objects in a visual way',
            'tags': ['tpDcc', 'dcc', 'tool', 'renamer'],
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Renamer', 'load_on_startup': False, 'color': '', 'background_color': ''}
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


if __name__ == '__main__':

    import tpDcc.loader
    from tpDcc.managers import tools

    tool_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    if tool_path not in sys.path:
        sys.path.append(tool_path)

    tpDcc.loader.init()
    tools.ToolsManager().launch_tool_by_id(consts.TOOL_ID, connect_client=False)
