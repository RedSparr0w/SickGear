import unittest

import sys
import os.path
sys.path.insert(1, os.path.abspath('..'))

from sickbeard import common
from sickbeard.common import Quality, wantedQualities
from sickbeard.name_parser.parser import NameParser


class QualityTests(unittest.TestCase):

    def check_quality_names(self, quality, cases):
        for fn in cases:
            second = common.Quality.nameQuality(fn)
            self.assertEqual(quality, second, 'fail %s != %s for case: %s' % (quality, second, fn))

    def check_proper_level(self, cases, is_anime=False):
        np = NameParser(False, indexer_lookup=False, try_scene_exceptions=False, testing=True)
        for case, level in cases:
            p = np.parse(case)
            second = common.Quality.get_proper_level(p.extra_info_no_name(), p.version, is_anime)
            self.assertEqual(level, second, 'fail %s != %s for case: %s' % (level, second, case))

    def check_wantedquality_list(self, cases):
        for show_quality, result in cases:
            sq = common.Quality.combineQualities(*show_quality)
            wd = common.wantedQualities()
            res = wd.get_wantedlist(sq, False, common.Quality.NONE, common.UNAIRED, manual=True)
            for w, v in wd.iteritems():
                if w == sq:
                    for u, o in sorted(v.iteritems()):
                        self.assertEqual(o, result.get(u))

    def check_wantedquality_get_wantedlist(self, cases):
        for show_quality, result in cases:
            sq = common.Quality.combineQualities(*show_quality)
            wd = common.wantedQualities()
            for case, wlist in result:
                ka = {'qualities': sq}
                ka.update(case)
                res = wd.get_wantedlist(**ka)
                self.assertEqual(res, wlist)

    # TODO: repack / proper ? air-by-date ? season rip? multi-ep?

    def test_SDTV(self):

        self.assertEqual(common.Quality.compositeStatus(common.DOWNLOADED, common.Quality.SDTV),
                         common.Quality.statusFromName('Test.Show.S01E02-GROUP.mkv'))

        self.check_quality_names(common.Quality.SDTV, [
            'Test.Show.S01E02.PDTV.XViD-GROUP',
            'Test.Show.S01E02.PDTV.x264-GROUP',
            'Test.Show.S01E02.HDTV.XViD-GROUP',
            'Test.Show.S01E02.HDTV.x264-GROUP',
            'Test.Show.S01E02.DSR.XViD-GROUP',
            'Test.Show.S01E02.DSR.x264-GROUP',
            'Test.Show.S01E02.TVRip.XViD-GROUP',
            'Test.Show.S01E02.TVRip.x264-GROUP',
            'Test.Show.S01E02.WEBRip.XViD-GROUP',
            'Test.Show.S01E02.WEBRip.x264-GROUP',
            'Test.Show.S01E02.Web-Rip.x264.GROUP',
            'Test.Show.S01E02.WEB-DL.x264-GROUP',
            'Test.Show.S01E02.WEB-DL.AAC2.0.H.264-GROUP',
            'Test.Show.S01E02 WEB-DL H 264-GROUP',
            'Test.Show.S01E02_WEB-DL_H_264-GROUP',
            'Test.Show.S01E02.WEB-DL.AAC2.0.H264-GROUP',
            'Test.Show.S01E02.HDTV.AAC.2.0.x264-GROUP',
            'Test.Show.S01E02.HDTV.DD5.1.XViD-GROUP',
            'Test.Show.S01E02.HDTV.DD7.1.h.264-GROUP',
            'Test.Show.S01E02.WEB-DL.DD5.1.h.264-GROUP',
            'Test.Show.S01E02.WEB.h264-GROUP',
            'Test.Show.S01E02.WEB.x264-GROUP',
            'Test.Show.S01E02.WEB.h265-GROUP',
            'Test.Show.S01E02.WEB.x265-GROUP',
            'Test.Show.S01E02.WEBRip.h264-GROUP',
            'Test.Show.S01E02.WEBRip.x264-GROUP'])

    def test_SDDVD(self):
        self.check_quality_names(common.Quality.SDDVD, [
            'Test.Show.S01E02.DVDRiP.XViD-GROUP',
            'Test.Show.S01E02.DVDRiP.DiVX-GROUP',
            'Test.Show.S01E02.DVDRiP.x264-GROUP',
            'Test.Show.S01E02.DVDRip.WS.XViD-GROUP',
            'Test.Show.S01E02.DVDRip.WS.DiVX-GROUP',
            'Test.Show.S01E02.DVDRip.WS.x264-GROUP',
            'Test.Show-S01E02-Test.Dvd Rip',
            'Test.Show.S01E02.BDRIP.XViD-GROUP',
            'Test.Show.S01E02.BDRIP.DiVX-GROUP',
            'Test.Show.S01E02.BDRIP.x264-GROUP',
            'Test.Show.S01E02.BDRIP.WS.XViD-GROUP',
            'Test.Show.S01E02.BDRIP.WS.DiVX-GROUP',
            'Test.Show.S01E02.BDRIP.WS.x264-GROUP'])

    def test_HDTV(self):
        self.check_quality_names(common.Quality.HDTV, [
            'Test.Show.S01E02.720p.HDTV.x264-GROUP',
            'Test.Show.S01E02.HR.WS.PDTV.x264-GROUP',
            'Test.Show.S01E02.720p.AHDTV.x264-GROUP'])

    def test_RAWHDTV(self):
        self.check_quality_names(common.Quality.RAWHDTV, [
            'Test.Show.S01E02.720p.HDTV.DD5.1.MPEG2-GROUP',
            'Test.Show.S01E02.1080i.HDTV.DD2.0.MPEG2-GROUP',
            'Test.Show.S01E02.1080i.HDTV.H.264.DD2.0-GROUP',
            'Test Show - S01E02 - 1080i HDTV MPA1.0 H.264 - GROUP',
            'Test.Show.S01E02.1080i.HDTV.DD.5.1.h264-GROUP'])

    def test_FULLHDTV(self):
        self.check_quality_names(common.Quality.FULLHDTV, [
            'Test.Show.S01E02.1080p.HDTV.x264-GROUP',
            'Test.Show.S01E02.1080p.AHDTV.x264-GROUP'])

    def test_HDWEBDL(self):
        self.check_quality_names(common.Quality.HDWEBDL, [
            'Test.Show.S01E02.720p.WEB-DL-GROUP',
            'Test.Show.S01E02.720p.WEBRip-GROUP',
            'Test.Show.S01E02.WEBRip.720p.H.264.AAC.2.0-GROUP',
            'Test.Show.S01E02.720p.WEB-DL.AAC2.0.H.264-GROUP',
            'Test Show S01E02 720p WEB-DL AAC2 0 H 264-GROUP',
            'Test_Show.S01E02_720p_WEB-DL_AAC2.0_H264-GROUP',
            'Test.Show.S01E02.720p.WEB-DL.AAC2.0.H264-GROUP',
            'Test.Show.S01E02.720p.iTunes.Rip.H264.AAC-GROUP',
            'Test.Show.s01e02.WEBDL.720p.GROUP',
            'Test Show s01e02 WEBDL 720p GROUP',
            'Test Show S01E02 720p WEB-DL AVC-GROUP',
            'Test.Show.S01E02.WEB-RIP.720p.GROUP',
            'Test.Show.S01E02.720p.WEB.h264-GROUP',
            'Test.Show.S01E02.720p.WEB.x264-GROUP',
            'Test.Show.S01E02.720p.WEB.h265-GROUP',
            'Test.Show.S01E02.720p.WEB.x265-GROUP',
            'Test.Show.S01E02.720p.WEBRip.h264-GROUP',
            'Test.Show.S01E02.720p.WEBRip.x264-GROUP'])

    def test_FULLHDWEBDL(self):
        self.check_quality_names(common.Quality.FULLHDWEBDL, [
            'Test.Show.S01E02.1080p.WEB-DL-GROUP',
            'Test.Show.S01E02.1080p.WEBRip-GROUP',
            'Test.Show.S01E02.WEBRip.1080p.H.264.AAC.2.0-GROUP',
            'Test.Show.S01E02.WEBRip.1080p.H264.AAC.2.0-GROUP',
            'Test.Show.S01E02.1080p.iTunes.H.264.AAC-GROUP',
            'Test Show S01E02 1080p iTunes H 264 AAC-GROUP',
            'Test_Show_S01E02_1080p_iTunes_H_264_AAC-GROUP',
            'Test.Show.s01e02.WEBDL.1080p.GROUP',
            'Test Show s01e02 WEBDL 1080p GROUP',
            'Test Show S01E02 1080p WEB-DL AVC-GROUP',
            'Test.Show.S01E02.WEB-RIP.1080p.GROUP',
            'Test.Show.S01E02.1080p.WEB.h264-GROUP',
            'Test.Show.S01E02.1080p.WEB.x264-GROUP',
            'Test.Show.S01E02.1080p.WEB.h265-GROUP',
            'Test.Show.S01E02.1080p.WEB.x265-GROUP',
            'Test.Show.S01E02.1080p.WEBRip.h264-GROUP',
            'Test.Show.S01E02.1080p.WEBRip.x264-GROUP'])

    def test_HDBLURAY(self):
        self.check_quality_names(common.Quality.HDBLURAY, [
            'Test.Show.S01E02.720p.BluRay.x264-GROUP',
            'Test.Show.S01E02.720p.HDDVD.x264-GROUP',
            'Test.Show.S01E02.720p.Blu-ray.x264-GROUP'])

    def test_FULLHDBLURAY(self):
        self.check_quality_names(common.Quality.FULLHDBLURAY, [
            'Test.Show.S01E02.1080p.BluRay.x264-GROUP',
            'Test.Show.S01E02.1080p.HDDVD.x264-GROUP',
            'Test.Show.S01E02.1080p.Blu-ray.x264-GROUP',
            'Test Show S02 1080p Remux AVC FLAC 5.1'])

    def test_UHD4KWEB(self):
        self.check_quality_names(common.Quality.UHD4KWEB, [
            'Test.Show.S01E02.2160p.WEBRip.h264-GROUP',
            'Test.Show.S01E02.2160p.WEBRip.x264-GROUP',
            'Test.Show.S01E02.2160p.WEBRip.x265-GROUP'])

    def test_UNKNOWN(self):
        self.check_quality_names(common.Quality.UNKNOWN, ['Test.Show.S01E02-SiCKGEAR'])

    def test_reverse_parsing(self):
        self.check_quality_names(common.Quality.SDTV, ['Test Show - S01E02 - SD TV - GROUP'])
        self.check_quality_names(common.Quality.SDDVD, ['Test Show - S01E02 - SD DVD - GROUP'])
        self.check_quality_names(common.Quality.HDTV, ['Test Show - S01E02 - HD TV - GROUP'])
        self.check_quality_names(common.Quality.RAWHDTV, ['Test Show - S01E02 - RawHD TV - GROUP'])
        self.check_quality_names(common.Quality.FULLHDTV, ['Test Show - S01E02 - 1080p HD TV - GROUP'])
        self.check_quality_names(common.Quality.HDWEBDL, ['Test Show - S01E02 - 720p WEB-DL - GROUP'])
        self.check_quality_names(common.Quality.FULLHDWEBDL, ['Test Show - S01E02 - 1080p WEB-DL - GROUP'])
        self.check_quality_names(common.Quality.HDBLURAY, ['Test Show - S01E02 - 720p BluRay - GROUP'])
        self.check_quality_names(common.Quality.FULLHDBLURAY, ['Test Show - S01E02 - 1080p BluRay - GROUP'])
        self.check_quality_names(common.Quality.UNKNOWN, ['Test Show - S01E02 - Unknown - SiCKGEAR'])

    def test_get_proper_level(self):
        # release_name, expected level
        self.check_proper_level([
            ('Test.Show.S01E13.PROPER.REPACK.720p.HDTV.x264-GROUP', 2),
            ('Test.Show.S01E13.720p.WEBRip.AAC2.0.x264-GROUP', 0),
            ('Test.Show.S01E13.PROPER.720p.HDTV.x264-GROUP', 1),
            ('Test.Show.S03E09-E10.REAL.PROPER.720p.HDTV.x264-GROUP', 2),
            ('Test.Show.S01E07.REAL.PROPER.1080p.WEB.x264-GROUP', 2),
            ('Test.Show.S13E20.REAL.REPACK.720p.HDTV.x264-GROUP', 2),
            ('Test.Show.S02E04.REAL.HDTV.x264-GROUP', 1),
            ('Test.Show.S01E10.Episode.Name.HDTV.x264-GROUP', 0),
            ('Test.Show.S12E10.1080p.WEB.x264-GROUP', 0),
            ('Test.Show.S03E01.Real.720p.WEB-DL.DD5.1.H.264-GROUP', 1),
            ('Test.Show.S04E06.REAL.PROPER.RERIP.720p.WEBRip.X264-GROUP', 2),
            ('Test.Show.S01E09.REPACK.REAL.PROPER.HDTV.XviD-GROUP.[SOMETHING].GROUP', 3),
            ('Test.Show.S01E13.REPACK.REAL.PROPER.720p.HDTV.x264-GROUP', 3),
            ('Test.Show.S01E06.The.Episode.Name.PROPER.480p.BluRay.x264-GROUP', 1),
            ('Test.Show.S01E19.PROPER.1080p.BluRay.x264-GROUP', 1),
            ('Test.Show.S01E03.REAL.PROPER.720p.BluRay.x264-GROUP', 2),
            ('Test.Show.S03E09.Episode.Name.720p.HDTV.x264-GROUP', 0),
            ('Test.Show.S02E07.PROPER.HDTV.x264-GROUP', 1),
            ('Test.Show.S02E12.REAL.REPACK.DSR.XviD-GROUP', 2),
            ('Test.Show Part2.REAL.AC3.WS DVDRip XviD-GROUP', 1),
            ('Test.Show.S01E02.Some.episode.title.REAL.READ.NFO.DVDRip.XviD-GROUP', 1)
        ])

    def test_wantedQualities_List(self):
        self.check_wantedquality_list([([(Quality.SDTV, Quality.HDTV), (Quality.HDWEBDL, Quality.FULLHDBLURAY)],
                                        {Quality.NONE: {wantedQualities.wantedlist: [Quality.SDTV, Quality.HDTV], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.SDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.SDDVD: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.RAWHDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDWEBDL: {wantedQualities.wantedlist: [Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: True},
                                         Quality.FULLHDWEBDL: {wantedQualities.wantedlist: [Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDBLURAY: {wantedQualities.wantedlist: [Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDBLURAY: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: True},
                                         Quality.UHD4KWEB: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.UNKNOWN: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False}
                                         }),
                                       ([(Quality.SDTV, Quality.HDTV), ()],
                                        {Quality.NONE: {wantedQualities.wantedlist: [Quality.SDTV, Quality.HDTV], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.SDTV: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.SDDVD: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDTV: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.RAWHDTV: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDTV: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDWEBDL: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDWEBDL: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDBLURAY: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDBLURAY: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.UHD4KWEB: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.UNKNOWN: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False}
                                         }),
                                       ([(Quality.SDTV, Quality.HDTV, Quality.HDWEBDL, Quality.HDBLURAY, Quality.FULLHDBLURAY), (Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY)],
                                        {Quality.NONE: {wantedQualities.wantedlist: [Quality.SDTV, Quality.HDTV, Quality.HDWEBDL, Quality.HDBLURAY, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.SDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.SDDVD: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.RAWHDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDTV: {wantedQualities.wantedlist: [Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.HDWEBDL: {wantedQualities.wantedlist: [Quality.FULLHDWEBDL, Quality.FULLHDBLURAY], wantedQualities.bothlists: True, wantedQualities.upgradelist: True},
                                         Quality.FULLHDWEBDL: {wantedQualities.wantedlist: [Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: True},
                                         Quality.HDBLURAY: {wantedQualities.wantedlist: [Quality.FULLHDBLURAY], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.FULLHDBLURAY: {wantedQualities.wantedlist: [], wantedQualities.bothlists: True, wantedQualities.upgradelist: True},
                                         Quality.UHD4KWEB: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False},
                                         Quality.UNKNOWN: {wantedQualities.wantedlist: [], wantedQualities.bothlists: False, wantedQualities.upgradelist: False}
                                         })
                                       ])

    def test_wantedQualities_get_wantedlist(self):
        self.check_wantedquality_get_wantedlist([([(Quality.SDDVD, Quality.RAWHDTV), (Quality.HDWEBDL, Quality.HDBLURAY)],
                                                  [({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),

                                                   # unaired:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),

                                                   # manual:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                   
                                                   # upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   
                                                   # unaired, manual:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                   
                                                   # unaired, upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   
                                                   # unaired, manual, upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                   
                                                   # upgrade once, manual:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # FULLHDTV (between init and upgrade qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDWEBDL, Quality.HDBLURAY]),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                   ]),
                                                   # init quality only show
                                                   ([(Quality.SDDVD, Quality.RAWHDTV), ()],
                                                  [({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),

                                                   # unaired:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),

                                                   # manual:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                   
                                                   # upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   
                                                   # unaired, manual:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                   
                                                   # unaired, upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   
                                                   # unaired, manual, upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                   
                                                   # upgrade once, manual:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # HDTV (between init qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # RAWHDTV (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDTV (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # HDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDWEBDL (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # HDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDBLURAY (above init quality + unwanted)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                   ]),
                                                   # init, upgrade quality show (overlapping)
                                                   ([(Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL), (Quality.RAWHDTV, Quality.HDBLURAY)],
                                                  [({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),

                                                   # unaired:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),

                                                   # manual:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDWEBDL (upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                   
                                                   # upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': False}, []),
                                                   
                                                   # unaired, manual:
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': False, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': False, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                   
                                                   # unaired, upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': False}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': False}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': False}, []),
                                                   
                                                   # unaired, manual, upgrade once:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': True, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': True, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': True, 'manual': True}, []),
                                                   
                                                   # upgrade once, manual:
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.UNAIRED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.SKIPPED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.IGNORED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.WANTED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                   ({'upgradeonce': True, 'quality': Quality.NONE, 'status': common.FAILED, 'unaired': False, 'manual': True}, [Quality.SDDVD, Quality.RAWHDTV, Quality.HDWEBDL]),
                                                        # SDTV (below init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # SDDVD (init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.SDDVD, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # HDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.RAWHDTV, Quality.HDBLURAY]),
                                                        # RAWHDTV (init + upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.RAWHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDTV (between init qualities + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDTV, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDWEBDL (max init quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.HDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # FULLHDWEBDL (unwanted quality between upgrade qualities)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDWEBDL, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, [Quality.HDBLURAY]),
                                                        # HDBLURAY (max upgrade quality)
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.HDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                        # FULLHDBLURAY (higher then max upgrade quality + unwanted quality)
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_PROPER, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.SNATCHED_BEST, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.DOWNLOADED, 'unaired': False, 'manual': True}, []),
                                                   ({'upgradeonce': True, 'quality': Quality.FULLHDBLURAY, 'status': common.ARCHIVED, 'unaired': False, 'manual': True}, []),
                                                   ]),
                                                ])

    def test_get_proper_level_anime(self):
        # release_name, expected level
        self.check_proper_level([
            ('Boruto - Naruto Next Generations - 59 [480p]', 0),
            ('[SGKK] Bleach - 312v2 (1280x720 h264 AAC) [F501C9BE]', 1),
            ('[SGKK] Bleach 312v1 [720p/MKV]', 0),
            ('[Cthuko] Shirobako - 05v2 [720p H264 AAC][80C9B09B]', 1),
            ('Naruto Shippuden - 314v3', 2)
        ], is_anime=True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(QualityTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
