import numpy as np
import pandas as pd
from datetime import datetime
from palmerpenguins import load_penguins
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def make_IMG_files_for_bulk_rename(path, nfiles=20, message="This is an example"):
    """
    Script for generating IMG_001.png files for the bulk renaming exercise
    Takes the word 'penguin' and makes a word cloud.  

    input:

        path - path to folder the files will be written in
        nfiles - number of files to write
        message - content of file
    """

    files =     ['data-formats.md',
                'deleting-data.md',
                'documentation.md',
                'file-names.md',
                'file-structures.md',
                'introduction.md',
                'storing-data.md',
                'tabular-data.md',
                'transferring-data.md']

    loadall = []
    for file in files:
        with open(f"../episodes/{file}",'r') as f:
            data = f.read()   
            loadall.append(data)    
    
    set1 = np.arange(len(files))
    set2 = []
    for i in range(9):
        for j in range(i,9):
            if i!=j:
                set2.append([i,j])
    set2 = np.array(set2)
    idx = np.arange(set2.shape[0])

    np.random.seed(10)
    res = np.random.choice(idx, size=20, replace=False)
    sub_set2 = set2[res]


    # set 1
    for i in range(8):
        print(i)
        wc = WordCloud(background_color="white", repeat=True,width=2048, height=2048)

        wc.generate(loadall[i]) 
        plt.figure(figsize=(4,4))  
        plt.axis('off')
        plt.imshow(wc, interpolation="bilinear")  
    
        fname = f'IMG_{i:03d}'
        plt.savefig(f"{path}/{fname}.png")

    # set 2
    for i in range(12):
        print(i)
        wc = WordCloud(background_color="white", repeat=True,width=2048, height=2048)

        data = loadall[sub_set2[i,0]]+loadall[sub_set2[i,1]]
        wc.generate(data)
        plt.figure(figsize=(4,4))  
        plt.axis('off')
        plt.imshow(wc, interpolation="bilinear")  
    
        fname = f'IMG_{8+i:03d}'
        plt.savefig(f"{path}/{fname}.png")

    # Set 3
    iref = [1,2,8,9,10,80,81,93]
    for i in range(8):
        print(i)
        wc = WordCloud(background_color="white", repeat=True,width=2048, height=2048)

        data = loadall[sub_set2[12+i,0]]+loadall[sub_set2[12+i,1]]
        wc.generate(data)
        plt.figure(figsize=(4,4))  
        plt.axis('off')
        plt.imshow(wc, interpolation="bilinear")  
    
        fname = f'image_{iref[i]}'
        plt.savefig(f"{path}/{fname}.png")
    




def apply_change(x, column, orig, change, rate):
    """
    Function to apply changes to dataframe values. 

    x -- the row of the dataframe
    column -- the name of the column to change
    orig -- original value to change
    change == value to change orig to 
    rate -- the approximate fraction of rows to change
    """
    if x[column] == orig:
        if np.random.random()< rate:
            x[column] = change
    return x

def penguin_data_changer(path_to_file, outfile, n_samples=100):

    """
    Takes the Palmer Penguin dataset (https://allisonhorst.github.io/palmerpenguins/)
    and makes it worse it.
    
    Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) 
    penguin data. R package version 0.1.0. https://allisonhorst.github.io/palmerpenguins/. 
    doi: 10.5281/zenodo.3960218.

    License: CC0 
        https://allisonhorst.github.io/palmerpenguins/LICENSE.html


    Inputs: 
        path_to_file -- path to the file containing data. If None uses palmer penguins package

        outfile -- path of output csv

        n_samples -- number of entries in example dataset  


    """

    np.random.seed(seed=24)


    if path_to_file is None:
        pen = load_penguins()

    # spoil categories
    cat_species = {'Adelie':["Adelie","A","Ade","Adelei"], 'Gentoo':["Gentoo","G","Gen","Gen too"], 'Chinstrap':["Chinstrap","C","Chin'"]}
    r_species = {'Adelie':[.7,.2,.05,.05], 'Gentoo':[.6,.3,.05,.05], 'Chinstrap':[.6,.2,.2]}
    cat_island = {'Torgersen':["Torgersen","T","Tor","Torgersan"], 'Biscoe':["Biscoe","B"], 'Dream':["Dream","D"]}
    r_island = {'Torgersen':[.5,.4,.09,.01], 'Biscoe':[0.5,0.5], 'Dream':[0.8,0.2]}
    cat_year = {2007:[2007],2008:[2008], 2009:[2009,9]}
    r_year = {2007:[1.],2008:[1.], 2009:[.8,.2]}
    cat_sex = {"female":['female','f'], "male":["male","m"]}
    r_sex = {"female":[.8,.1], "male":[.7,.2]}

    
    pen_updated = pen
    for key in cat_species.keys():
        for i  in range(len(cat_species[key])):
            pen_updated = pen_updated.apply(apply_change, args = ('species',key,cat_species[key][i],r_species[key][i]), axis=1)

    for key in cat_island.keys():
        for i  in range(len(cat_island[key])):
            pen_updated = pen_updated.apply(apply_change, args = ('island',key,cat_island[key][i],r_island[key][i]), axis=1)
   
    for key in cat_year.keys():
        for i  in range(len(cat_year[key])):
            pen_updated = pen_updated.apply(apply_change, args = ('year',key,cat_year[key][i],r_year[key][i]), axis=1)

    for key in cat_sex.keys():
        for i  in range(len(cat_sex[key])):
            pen_updated = pen_updated.apply(apply_change, args = ('sex',key,cat_sex[key][i],r_sex[key][i]), axis=1)
    
    # Units in a column
    pen_updated['bill_depth_mm'] = pen_updated['bill_depth_mm'].astype(str) + " mm"

 
    # Get subsample
    pen_updated = pen_updated.sample(n_samples, random_state=42)

    # Sort by species, island year and sex
    pen_updated=pen_updated.sort_values(['species','island','year','sex'])

    # Update headers
    header = {"id":"", 
              "species":"specsies", 
              "island":"island", 
              "bill_length_mm":"bill_len", 
              "bill_depth_mm":"depth_of_bill", 
              "flipper_length_mm":"fliplength",
              "body_mass_g":"g", 
              "sex":"sex", 
              "year":"YEAR"
            }
    pen_updated = pen_updated.rename(columns=header)

    pen_updated.to_csv(outfile)

def make_big_file(outfile, xsize, ysize):
    """
    Makes a larger file, filled with random numbers
    """
    img = np.random.random((xsize, ysize))
    np.savetxt(outfile,img)

def make_various_files(path="./data/legacy_dataset/processing_data/", n_date_files=10):


    # make file with overly long name
    f_overlong = f"{path}/10-Nov-26_penguin_withtheirnames_and_weatherreport.txt"
    with open(f_overlong,'w') as f:
        f.write("This is data!")

    #Selection of files with inconsistent dates
    time1Jan2026 = datetime.strptime("2026-01-01","%Y-%m-%d")
    ts = time1Jan2026.timestamp()
    for i in range(n_date_files):
        xr = np.random.random() 
        if xr > 0.7:
            date = datetime.fromtimestamp(ts-i/2*1e7).strftime("%Y-%m-%d")
        elif xr > 0.4:
            date = datetime.fromtimestamp(ts-i/2*1e7).strftime("%d-%m-%Y")   
        else:
            date = datetime.fromtimestamp(ts-i/2*1e7).strftime("%Y-%B-%d")
        fname = f"{path}/{date}_penguin_data.csv"
        with open(fname,'w') as f:
            f.write("# Penguin data")
            f.write("ID,Name,Age,Location,Favourite_fish,tracker_id,walk_speed_kph,swimspeed_kph\n")
            f.write("<pretend there is data here>")

def temp_image_gen():

    """
    Generates wordcloud containing text from data-formats.md lesson
    """
    wc = WordCloud(background_color="white", repeat=True,width=2048, height=2048)

    with open("../episodes/data-formats.md",'r') as f:
        data = f.read()

    wc.generate(data)

    plt.axis('off')
    plt.figure(figsize=(20,20))
    plt.savefig("test.png")



make_IMG_files_for_bulk_rename("../data/legacy_dataset/New Folder", nfiles=20, message="This is an example")

