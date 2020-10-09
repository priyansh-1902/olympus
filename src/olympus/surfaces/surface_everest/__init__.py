#!/usr/bin/env python

from olympus.utils.misc import check_module
from olympus.surfaces import get_surfaces_list

surface = 'Everest'
module  = 'scipy'
link    = 'https://docs.scipy.org/doc/scipy/reference/'

message = '''Surface {surface} requires {module} which could not be found. Please install
{module} and check out {link} for further instructions or use another
available planner: {planners_list}'''
check_module(module, message, planner=surface, planners_list=', '.join(get_surfaces_list()), link=link)

from .wrapper_everest import Everest