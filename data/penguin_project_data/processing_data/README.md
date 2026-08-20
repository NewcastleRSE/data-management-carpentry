This dataset is a (dummified) real world example of some input data for a processing script. It contains several issues, such as:

- `input_data_1.csv` and `input_data_2.csv` are essentially the same type of data that differ only on a categorical parameter;
- `input_data_3.xlsx` is in different (and proprietary) format; it is also one entry long
- `input_data_1.csv` and `input_data_2.csv` contain inconsistant use of columns (names and filenames), inconsistent use of paths (absolute, relative) and inconsistent input file extension for the same type of input (.dat vs .txt);
- `input_data_2.csv` also includes inconsistent number of parameters (i.e., csv is malformed) and inconsistent use of separators (, vs ;)