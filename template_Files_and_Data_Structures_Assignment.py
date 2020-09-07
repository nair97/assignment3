#!/usr/bin/env python
"""
Update with your header information
"""

# import required modules here

# define required descriptive caluclations here

def compute_mean(value_list):
    ''' Computes average of a list, and returns that value. '''

def compute_sum(value_list):
    ''' Computes cumulative sum of a list, and returns that value. '''

def distance_between_points(x1,y1,x2,y2):
    ''' Computes the distance between two sets of coordinate points (x1,y1) 
    and (x2,y2), and that value.  '''

def compute_distance_traveled(X, Y):
    ''' Computes the distance between each subsequent set of coordinates from 
    two lists, X and Y coordinates of the raccoon.  Function returns list of 
    distances added to dictionary, with initial distance = 0. List should be 
    the same length as the input X and Y lists.'''
        

# define function to read in the contents of the given data file, convert
# columns to appropriate numerical values (as needed), and create a data
# structure for processing using a dictionary.  The dictionary should be
# returned to the main code for later use.
#
# - dictionary keys should not include white space.
# - dictionary items should be named for column headers, and include data for 
#   that column converted to the appropriate numerical format, if appropriate.
# - end status of the raccoon should be stored in the data dictionary under 
#   the keyword 'Status'

def read_data_file( fileName ):


# include a function to output the reformatted data file.
# Output file should have a header that includes:
# Raccoon name: <name of the raccoon> 
# Average location: X <average X position>, Y <average Y position>
# Distance traveled: <total distance traveled>
# Average energy level: <average energy level>
# Raccoon end state: <string indicating final raccoon status>
#
# The header should be followed by a blank line, then the following headers
# prviding a starting point for a tab delimited table of data values:
# - Date, X, Y, Asleep Flag, Behavior Mode, Distance Traveled
# - subsequent lines should be the relevent values for each header category
#   separated by tabs.

def write_output_file( outName, dataDict, avg_energy, avg_x, avg_y, t_dist ):
    ''' outName is a string defining the name of the output file
        dataDict is the data dictionary first created by read_data_file
        avg_energy is a single value of the average energy used
        avg_x is a single value of the average x-position
        avg_y is a single value of the average y-poisition
        t_dist is a single value of the total distance traveled'''


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # set input and output file names
    inFile = '2008Male00006.txt'
    outFile = "Georges_life.txt"

    # read input file
    dataDict = read_data_file(inFile)

    # complete summary calculations

    # write output data to a file
    #write_output_file( outFile, dataDict, avg_energy, avg_x, avg_y, t_dist )
