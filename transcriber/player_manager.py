'''
LTranscribe 

Copyright (C) 2022  zBennyAnd

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
class Player_manager:
    def __init__(self):
        self.audio_loaded = False
        self.pause_on_typing = True  # Enable/disable pause on typing

    def audio_loaded_getter(self):
        return self.audio_loaded

    def audio_loaded_setter(self, value):
        self.audio_loaded = value

    def pause_on_typing_getter(self):
        return self.pause_on_typing

    def pause_on_typing_setter(self, value):
        self.pause_on_typing = value
