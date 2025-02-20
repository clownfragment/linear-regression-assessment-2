"""Unit Tests for Student Submission"""
import unittest
import pandas as pd
import numpy as np
# import student_solution
import solutions # this will be the student solution


class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solutions.df.shape, (506, 14))
        self.assertEqual(len(solutions.df.index), 506)
        self.assertEqual(len(solutions.df.columns), 14)
        self.assertTrue(isinstance(solutions.df.shape, tuple))
        self.assertTrue(isinstance(solutions.df, pd.core.frame.DataFrame))

    def test_part2(self):
        self.assertEqual(solutions.rm_rad, -0.21)
        self.assertEqual(solutions.ptratio_mdev, -0.51)
        self.assertEqual(solutions.chas_nox, 0.091)
        
    def test_part3(self):
        self.assertEqual(len(solutions.corr_features), 3)
        self.assertEqual(solutions.corr_features[0], 'RM')
        self.assertEqual(solutions.corr_features[1], 'LSTAT')
        self.assertEqual(solutions.corr_features[2], 'MDEV')
        
    def test_part4(self):
        self.assertEqual(solutions.y.shape, (506,))
        self.assertEqual(len(solutions.y.index), 506)
        self.assertTrue(isinstance(solutions.y, pd.core.series.Series))
        self.assertEqual(solutions.y.name, 'MDEV')
        self.assertEqual(solutions.X_mult.shape, (506, 2))
        self.assertEqual(len(solutions.X_mult.index), 506)
        self.assertEqual(len(solutions.X_mult.columns), 2)
        self.assertTrue('RM' in list(solutions.X_mult.columns))
        self.assertTrue('LSTAT' in list(solutions.X_mult.columns))

    def test_part5(self):
        self.assertEqual(solutions.b_0_mult, -1.358272811874489)
        self.assertEqual(solutions.coefs_mult[0], 5.094787984336544)
        self.assertEqual(solutions.coefs_mult[1], -0.6423583342441294)
        self.assertTrue(isinstance(solutions.b_0_mult, np.float64))
        self.assertTrue(isinstance(solutions.coefs_mult[0], np.float64))
        self.assertTrue(isinstance(solutions.coefs_mult[1], np.float64))
        
    def test_part6(self):
        self.assertEqual(solutions.b_0_single, 62.344627474832635)
        self.assertEqual(solutions.coefs_single[0], -2.157175296060964)
        self.assertTrue(isinstance(solutions.b_0_single, np.float64))
        self.assertTrue(isinstance(solutions.coefs_single[0], np.float64))
        
    def test_part7(self):
        self.assertEqual(len(solutions.y_hat_mult), 506)
        self.assertTrue(isinstance(solutions.y_hat_mult, np.ndarray))
        self.assertEqual(len(solutions.y_hat_single), 506)
        self.assertTrue(isinstance(solutions.y_hat_single, np.ndarray))
        self.assertEqual(solutions.r2_mult, 0.6385616062603403)
        self.assertEqual(solutions.r2_single, 0.2578473180092231)
        self.assertEqual(solutions.mse_mult, 30.51246877729947)
        self.assertEqual(solutions.mse_single, 62.65220001376926)
        self.assertEqual(solutions.ssr_mult, 15439.309201313532)
        self.assertEqual(solutions.ssr_single, 31702.013206967247)
        self.assertEqual(solutions.best_scores, (0.6385616062603403, 30.51246877729947, 15439.309201313532))
        self.assertTrue(isinstance(solutions.best_scores, tuple))
        
    def test_part8(self):
        self.assertTrue(solutions.significant_ptratio_rm)
        
    def test_part9(self):
        self.assertFalse(solutions.significant_lstat_rad_nox)

    def test_part10(self):
        self.assertTrue(solutions.significant_nox_rad)
        

if __name__ == "__main__":
    unittest.main()
