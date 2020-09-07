"""Tests for class Masw."""

import matplotlib.pyplot as plt

import unittest
import swprocess
from testtools import TestCase, unittest, get_full_path


class Test_Masw(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.full_path = get_full_path(__file__)
        cls.vuws_path = cls.full_path + "../examples/sample_data/vuws/"
        cls.wghs_path = cls.full_path + "../examples/sample_data/wghs/"

    @unittest.skip
    def test_single(self):
        fname = self.vuws_path+"10.dat"
        settings = self.full_path+"settings/settings_new.json"
        fk = swprocess.Masw.run(fnames=fname, settings=settings)
        fk.plot_spectra()

        # # array = swprocess.Array1D.from_files(fnames=self.vuws_path+"22.dat")
        # # phase_shift = swprocess.WavefieldTransform1D(array=array,
        # #                                              settings=self.full_path+"settings/settings_phase-shift.json")
        # # phase_shift.plot_spectra(stype="fv")

        # # array = swprocess.Array1D.from_files(fnames=self.vuws_path+"22.dat")
        # # slant_stack = swprocess.WavefieldTransform1D(array=array,
        # #                                              settings=self.full_path+"settings/settings_slant-stack.json")
        # # slant_stack.plot_spectra(stype="fv")

        # # array = swprocess.Array1D.from_files(fnames=self.vuws_path+"22.dat")
        # # fdbf = swprocess.WavefieldTransform1D(array=array,
        # #                                       settings=self.full_path+"settings/settings_fdbf.json")
        # # fdbf.plot_spectra(stype="fv")
        
        plt.show()

    def test_frequency_domain(self):
        fnames = [self.vuws_path+str(x)+".dat" for x in range(11,15)]
        settings = self.full_path+"settings/settings_new.json"
        fk = swprocess.Masw.run(fnames=fnames, settings=settings)
        fk.plot_spectra()
        plt.show()


if __name__ == "__main__":
    unittest.main()