# -*- coding: utf-8 -*-
'''
    The Unofficial KissAnime Plugin - a plugin for Kodi
    Copyright (C) 2016  dat1guy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


# DEBUG
import time
t_start = time.time()


from resources.lib.common.helpers import helper
from resources.lib.common import controller
from resources.lib.common import args


helper.location("Default entry point")

if args.action == None:
    controller.Controller().main_menu()
elif args.action == 'genericList':
    controller.Controller().show_list()
elif args.action == 'mediaContainerList':
    controller.Controller().show_media_container_list()
elif args.action == 'mediaList':
    controller.Controller().show_media_list()
elif args.action == 'quality':
    controller.Controller().show_quality()
elif args.action == 'autoplay':
    controller.Controller().auto_play()
elif args.action == 'play':
    controller.Controller().play_video()
elif args.action == 'search':
    controller.Controller().search()
elif args.action == 'findmetadata':
    controller.Controller().find_metadata()
elif args.action == 'lastvisited':
    controller.Controller().show_last_visited()
elif args.action == 'bookmarkList':
    controller.Controller().show_bookmark_list()
elif args.action == 'addBookmark':
    controller.Controller().add_bookmark()
elif args.action == 'removeBookmark':
    controller.Controller().remove_bookmark()
else:
    helper.log_error("WHAT HAVE YOU DONE?")
    helper.show_error_dialog(['Something went wrong.  Please restart the addon.'])

helper.location("Default exit point")

t_end = time.time()
helper.log_notice('TIMER - TOTAL TIME: %f' % (t_end - t_start))