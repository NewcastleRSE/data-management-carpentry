import file_generator as fgen


def main(trial = True):
    """
    Function to generate files. 

    trail (default: True) - if local trail run is wanted. 
    """

    if trial is True:
        path1 = "./test/"
        path2 = "./test/big_file.txt"
        path3 = "./test/"
        path4 = "./test/penguins.csv"
    else:
        path1="../data/penguin_project_data/New Folder/"
        path2="../data/penguin_project_data/New Folder/big_file.txt"
        path3="../data/penguin_project_data/processing_data/"
        path4="../data/penguin_project_data/penguins/palmer_penguins.csv"

    fgen.make_IMG_files_for_bulk_rename(path1, nfiles=20, message="This is an example")
    fgen.make_big_file(path2, 200, 300)
    fgen.make_various_files(path=path3, n_date_files=10)
    fgen.penguin_data_changer(None, path4, n_samples=25)
    fgen.generate_misc_data()

    
main()