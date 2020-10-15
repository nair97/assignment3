#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:39:58 2020

@author: meerarakesh09
"""


import math
# import required modules here

#Computes average of a list, and returns that value.
def compute_mean(value_list):
    return sum(value_list)/len(value_list)

#Computes cumulative sum of a list, and returns that value.
def compute_sum(value_list):
    return sum(value_list)

#Computes the distance between two sets of coordinate points (x1,y1)
#and (x2,y2), and that value.
def distance_between_points(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#Computes the distance between each subsequent set of coordinates 
def compute_distance_traveled(X, Y):
    t_dist = [0]
    for i in range(len(X)-1):
        x1 = (X[i])
        y1 = (Y[i])
        x2 = (X[i+1])
        y2 = (Y[i+1])

        t_dist = t_dist + [distance_between_points(x1,y1,x2,y2)]
    return t_dist

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


def read_data_file(fileName):
    #to read txt file
    fileName = open(fileName, "r")
    lines = fileName.readlines()
    fileName.close()
#to format table data
    Data = [0]*len(lines)
    for lidx in range(1,len(lines)-1):
        Data[lidx] = lines[lidx].strip().split(",")
        Data[lidx][4:6] = map(float,Data[lidx][4:6])
        Data[lidx][6:8] = map(str,Data[lidx][6:8])
        Data[lidx][8] = float(Data[lidx][8])

#data structure framework
    header = lines[0].strip().split(',') # to get the header strings from fileName
    for i in range(len(header)):
        header[i] = header[i].strip()
      
#to build empty data dictionary
    Datadict = dict.fromkeys(header, [])

#to build column in dictionary
    Nlines = len(lines) #to get number of lines
    for lidx in range(1,Nlines-1): # process all data lines in the file
       tmpvar = Data[lidx] # get all data from current line
       for col in range(len(tmpvar)): # loop through all data values on current line
           Datadict[header[col]] = Datadict[header[col]] + [tmpvar[col] ] # create key and store first data item as a list

# to format the animal status
    Datadict["Status"] = lines[-1].strip() #add ew key and store status message
    return Datadict

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
    outline = []
    outline = outline + ['Racoon Name: George#6']
    outline = outline + ["Average location: X " + str(avg_x) + " Y " + str(avg_y)]
    outline = outline + ["Distance traveled : " + str(t_dist)]
    outline = outline + ["Average energy level: " + str(avg_energy)]
    outline = outline + ["Raccoon end state: " + dataDict["Status"]]
    outline = outline + [""]

    #Create headers which are tab seperated
    headers = "Date, X, Y, Asleep, Flag, Behavior Mode, Distance Traveled".replace(',' , ' \t ')
    outline = outline + [headers]

    #Number of data lines
    Nlines = len(dataDict['X'])

    for lidx in range(Nlines):
        #Creating a tab seperated output line
        tmpline = dataDict['Day'][lidx] + '\t'+ str(dataDict['X'][lidx]) + '\t'+ str(dataDict['Y'][lidx]) + '\t'+ dataDict['Asleep'][lidx] + '\t' + dataDict['Behavior Mode'][lidx] + '\t' + str(dataDict['Distance Traveled'][lidx])
        outline = outline + [tmpline]

        file = open(outName,"w")
        file.write('\n \t'.join(outline))
        file.close()

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # set input and output file names
    inFile = '2008Male00006.txt' 
    outFile = "Georges_life.txt"

    # read input file
    dataDict = read_data_file(inFile)
    print ("The X list: \n \t ", dataDict['X'],'\n \t')
    print ("The Y list: \n \t", dataDict['Y'],'\n \t')

    #Compute average of a list
    avg_x = compute_mean(dataDict['X'])
    avg_y = compute_mean(dataDict['Y'])
    avg_energy = compute_mean(dataDict['Energy Level'])
    print ("The average of X list: ", avg_x)
    print ("The average of Y list: ", avg_y)
    print ("Energy Level:", avg_energy, '\n')


    #Computes cumulative sum of a list
    print ("The sum list of X: ", compute_sum(dataDict['X']))
    print ("The sum list of Y: ", compute_sum(dataDict['Y']),'\n')

    dist = compute_distance_traveled(dataDict['X'],dataDict['Y'])
    dataDict['Distance Traveled'] = dist
    t_dist = compute_sum(dist)

    # write output data to a file
    write_output_file( outFile, dataDict, avg_energy, avg_x, avg_y, t_dist)


#outName is a string defining the name of the output file
        #dataDict is the data dictionary first created by read_data_file
        #avg_energy is a single value of the average energy used
        #avg_x is a single value of the average x-position
        #avg_y is a single value of the average y-poisition
        #t_dist is a single value of the total distance traveled'''

