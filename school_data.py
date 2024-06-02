# school_data.py
# JEFF WHEELER
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


years_2d = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
years_3d = np.array([np.reshape(year, (20, 3)) for year in years_2d])



# Class to capture each high school's name, school code and where the school's data is kept in given_data.py
class HighSchool:

    # Constructor
    def __init__(self, name, code, row):
        self.__name = name
        self.__code = code
        self.__row = row

    # Getter for the name of the HighSchool object
    def get_name(self):
        return self.__name
    
    # Getter for the code of the HighSchool object
    def get_code(self):
        return self.__code
    
    # Getter for the data row of the HighSchool object
    def get_row(self):
        return self.__row

# Initialize school objects for each high school
centennial = HighSchool("Centennial High School", "1224", 0)
robert_thirk = HighSchool("Robert Thirsk School", "1679", 1)
louise_dean = HighSchool("Louise Dean School", "9626", 2)
queen_elizabeth = HighSchool("Queen Elizabeth High School", "9806", 3)
forest_lawn = HighSchool("Forest Lawn High School", "9813", 4)
crescent_heights = HighSchool("Crescent Heights High School", "9815", 5)
western_canada = HighSchool("Western Canada High School", "9816", 6)
central_memorial = HighSchool("Central Memorial High School", "9823", 7)
james_fowler = HighSchool("James Fowler High School", "9825", 8)
ernest_manning = HighSchool("Ernest Manning High School", "9826", 9)
william_aberhart = HighSchool("William Aberhart High School", "9829", 10)
national_sport = HighSchool("National Sport School", "9830", 11)
henry_wisewood = HighSchool("Henry Wise Wood High School", "9836", 12)
bowness = HighSchool("Bowness High School", "9847", 13)
lord_beaverbrook = HighSchool("Lord Beaverbrook High School", "9850", 14)
jack_james = HighSchool("Jack James High School", "9856", 15)
winston_churchill = HighSchool("Sir Winston Churchill High School", "9857", 16)
ep_scarlett = HighSchool("Dr. E. P. Scarlett High School", "9858", 17)
john_g_diefenbaker = HighSchool("John G Diefenbaker High School", "9860", 18)
lester_b_pearson = HighSchool("Lester B. Pearson High School", "9865", 19)

# list containing all the high school
high_school_list = [centennial, robert_thirk, louise_dean, queen_elizabeth, forest_lawn, crescent_heights, western_canada, central_memorial, 
                    james_fowler, ernest_manning, william_aberhart, national_sport, henry_wisewood, bowness, lord_beaverbrook, jack_james, 
                    winston_churchill, ep_scarlett, john_g_diefenbaker, lester_b_pearson]

# dictionary containing each high school name as the key and school code as the value
high_school_dict = {school.get_name():school.get_code() for school in high_school_list}

def main():
    print("\nENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements
    print("\nShape of full data array: ", years_3d.shape)
    print("Dimensions of full data array: ", years_3d.ndim)
    
    # Prompt for user input
    user_input = ""
    while (True):    
        user_input = input("Please enter the high school name or school code: ")
        try:
            if ((user_input in high_school_dict.keys()) | (user_input in high_school_dict.values())):
                pass
            else:
                raise ValueError
        except ValueError:
            print("You must enter a valid school name or code.")
            continue
        if user_input in high_school_dict.keys():
            school = user_input
            code = high_school_dict.get(user_input)
            break
        elif user_input in high_school_dict.values():
            for i in high_school_dict: # find key from value input in dictionary
                if (high_school_dict[i] == user_input):
                    school = i
            code = user_input
            break      
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print("School name: " + school + ", School code: " + code)

    for i in high_school_list: # convert school from string to object within list
        if (school == i.get_name()):
            school = i
            break

    print("Mean enrollment for Grade 10: ", int(np.nanmean(years_3d[:10, school.get_row(), 0])))
    print("Mean enrollment for Grade 11: ", int(np.nanmean(years_3d[:10, school.get_row(), 1])))
    print("Mean enrollment for Grade 12: ", int(np.nanmean(years_3d[:10, school.get_row(), 2])))
    print("Highest enrollment for a single grade: ", int(np.nanmax(years_3d[:10, school.get_row(), :3])))
    print("Lowest enrollment for a single grade: ", int(np.nanmin(years_3d[:10, school.get_row(), :3])))
    for i in range(10):
        print("Total enrollment for " + str((i + 2013)) + ": " + str(int(np.nansum(years_3d[i, school.get_row(), :3]))))
    print("Total ten year enrollment: ", int(np.nansum(years_3d[:10, school.get_row(), :3])))
    print("Mean total enrollment over 10 years: ", (int(np.nansum(years_3d[:10, school.get_row(), :3])) // 10))
    years_3d_sub = years_3d[:10, school.get_row(), :3] # subarray to get median over 500
    enroll_over_500 = (years_3d_sub > 500)
    if np.any(enroll_over_500):
        print("For all enrollments over 500, the median was: ", int(np.median(years_3d_sub[enroll_over_500])))
    else:
        print("No enrollments over 500.")


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    print("Mean enrollment in 2013: ", int(np.nanmean(years_3d[0, :20, :3])))
    print("Mean enrollment in 2022: ", int(np.nanmean(years_3d[9, :20, :3])))
    print("Total graduating class of 2022: ", int(np.nansum(years_3d[9, :20, 2])))
    print("Highest enrollment for a single grade: ",int(np.nanmax(years_3d[:10, :20, :3])))
    print("Lowest enrollment for a single grade: ",int(np.nanmin(years_3d[:10, :20, :3])))




if __name__ == '__main__':
    main()

