# Author: Nic Wolfe <nic@wolfeden.ca>
# URL: http://code.google.com/p/sickbeard/
#
# This file is part of SickGear.
#
# SickGear is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickGear is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickGear.  If not, see <http://www.gnu.org/licenses/>.

import os

from sickbeard import logger
import sickbeard

# This module tries to deal with the apparently random behavior of python when dealing with unicode <-> utf-8
# encodings. It tries to just use unicode, but if that fails then it tries forcing it to utf-8. Any functions
# which return something should always return unicode.


def fixStupidEncodings(x, silent=False):
    if type(x) == str:
        try:
            return x.decode(sickbeard.SYS_ENCODING)
        except UnicodeDecodeError:
            logger.log(u"Unable to decode value: " + repr(x), logger.ERROR)
            return None
    elif type(x) == unicode:
        return x
    else:
        logger.log(
            u"Unknown value passed in, ignoring it: " + str(type(x)) + " (" + repr(x) + ":" + repr(type(x)) + ")",
            logger.DEBUG if silent else logger.ERROR)
        return None


def fixListEncodings(x):
    if type(x) != list and type(x) != tuple:
        return x
    else:
        return filter(lambda x: x != None, map(fixStupidEncodings, x))


def callPeopleStupid(x):
    try:
        return x.encode(sickbeard.SYS_ENCODING)
    except UnicodeEncodeError:
        logger.log(
            u"YOUR COMPUTER SUCKS! Your data is being corrupted by a bad locale/encoding setting. Report this error on the forums or IRC please: " + repr(
                x) + ", " + sickbeard.SYS_ENCODING, logger.ERROR)
        return x.encode(sickbeard.SYS_ENCODING, 'ignore')


def fixParaLists(x):
    if type(x) == list:
        return [callPeopleStupid(a) if type(a) in (str, unicode) else a for a in x]
    else:
        return x


def win_encode_unicode(x):
    if isinstance(x, str):
        try:
            return x.decode('UTF-8')
        except UnicodeDecodeError:
            return x
    return x


def ek(func, *args, **kwargs):
    if os.name == 'nt':
        # convert all str parameter values to unicode
        args = tuple([x if not isinstance(x, str) else win_encode_unicode(x) for x in args])
        kwargs = {k: x if not isinstance(x, str) else win_encode_unicode(x) for k, x in
                  kwargs.iteritems()}
        result = func(*args, **kwargs)
    else:
        result = func(*[callPeopleStupid(x) if type(x) in (str, unicode) else fixParaLists(x) for x in args], **kwargs)

    if type(result) in (list, tuple):
        return fixListEncodings(result)
    elif type(result) == str:
        return fixStupidEncodings(result)
    else:
        return result
