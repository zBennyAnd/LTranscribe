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
class Timer:
    def __init__(self, time_start):
        self.time_start = time_start

    def time_getter(self):
        return self.time_start

    def time_adder(self, time):
        self.time_start += time
