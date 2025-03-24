def get_headcount_index(pl,data,target_col,weight_col):
    #pl is the poverty line
    #data is a dataframe containing survey data
    #target_col is the column within the data that will be used. It can be expenditure, income, or something else
    #weight_col is the column that has the weight of each row (i.e. the number of actual households that a row represents)
    total_sample = data[weight_col].sum() # the number of actual people each hh row represents
    #print(total_sample)
    the_poor = data[data[target_col] < pl]  # a dataframe that only includes poor people, ie those below the poverty line
    #print("the poor are ", the_poor)
    the_weighted_poor = the_poor[weight_col].sum()  # the actual amount of poor people based on the number of people each household represents
    #print(the_weighted_poor)
    poverty_index = the_weighted_poor / total_sample
    return poverty_index

