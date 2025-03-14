def get_headcount_index(pl,data):
    #pl is the poverty line
    #data is a dataframe containing survey data
    total_sample = data.shape[0] # number of rows
    the_poor = data[data['total_expenditure'] < pl].shape[0]
    #print("the poor are ", the_poor)
    poverty_index = the_poor / total_sample
    return poverty_index