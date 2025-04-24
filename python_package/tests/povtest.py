import unittest
import pandas as pd

from povertyInequalityMeasures import poverty

def crazycat( df, times ):
    """
    This just creates an array which is `times` stacked copies of `df`
    """
    dof = copy.deepcopy(df)
    for i in range(0,times-1):
        dof = pd.concat([dof, df], axis=0)
    return dof

class TestPovertyMeasures(unittest.TestCase):
    def test_headline_poverty(self):
        """
        Test the headline poverty function
        """
        # tests from Julia version
                c1 = pd.DataFrame({'inc':[10, 15, 20, 25, 40, 20, 30, 35, 45, 90 ],'weight':np.ones(10)})
        c2 = crazycat( c1, 2) # 2x obs should be same
        c3 = copy.deepcopy( c1 )
        c3.loc[:,'weight'] = 10_000.0 # uniform weight should make no difference
        # very unbalanced copy of dataset 1 with 64 weight1 copies of 1:6 and 4 weight 64 7:10
        c64 = crazycat( c1.iloc[0:7], 64 )
        cx = copy.deepcopy(c1.iloc[7:])
        cx.weight = 64
        c64 = pd.concat( [c64, cx], axis=0 )
        gini1 = inequality.get_gini( data=c1, target_col='inc', weight_col='weight' )
        gini2 = inequality.get_gini( data=c2, target_col='inc', weight_col='weight' )
        gini3 = inequality.get_gini( data=c3, target_col='inc', weight_col='weight' )
        gini64 = inequality.get_gini( data=c64, target_col='inc', weight_col='weight' )
        # weighting and multiplying should make no difference
        print( "gini1");print( gini1 )
        print( "gini2");print( gini2 )
        print( "gini3");print( gini3 )
        print( "gini64");print( gini64 )
        self.assertAlmostEqual( gini1,  0.3272727 )
        self.assertAlmostEqual( gini1,  gini2 )
        self.assertAlmostEqual( gini1,  gini3 )
        self.assertAlmostEqual( gini1,  gini64 )
        data = pd.DataFrame({'total_expenditure': [ 110,120,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_headcount_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.5)

    def test_poverty_gap(self):
        """
        Test the poverty gap index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_poverty_gap_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.08)
    
    def test_poverty_severity(self):
      """
      Test the poverty severity index function
      """
      data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
      poverty_line= 125
      result = poverty.get_poverty_severity_index(poverty_line, data, "total_expenditure","weight")
      self.assertEqual(result, 0.0136)

    def test_poverty_severity_generic_1(self):
        """
        Test the generic poverty severity index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_poverty_severity_index_generic(poverty_line, data, "total_expenditure","weight",0)
        self.assertEqual(result, 0.5)

    def test_poverty_severity_generic_2(self):
        """
        Test the generic poverty severity index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_poverty_severity_index_generic(poverty_line, data, "total_expenditure","weight",1)
        self.assertEqual(result, 0.08)

    def test_poverty_severity_generic_3(self):
        """
        Test the generic poverty severity index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_poverty_severity_index_generic(poverty_line, data, "total_expenditure","weight",2)
        self.assertEqual(result, 0.0136)

    def test_sen_index(self):
        """
        Test the sen index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_sen_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.143)

    def test_watts_index(self):
        """
        Test the watts index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_watts_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.08774)

    # TODO def test_time_to_exit(self):

if __name__ == '__main__':
    unittest.main()
