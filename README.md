# Plotting scatter matrix for big datamatrix with Python plotly

During working with project for MUT in Warsaw I was working with Big DataSet (1,7 Gb, 58 data columns). 
Before starting the process for training the XGBoost algorythm it was necessary to cut off some data and to  
do this I was planning to plot scatter matrix. Due to the fact that this Data is so big I create the function 
to cut it into pieces and the present it to the user.

## The Data Matrix

![Presentation of Data Matrix](https://github.com/jkowalski995/Scatter_matrix_plotly/blob/main/matrix.png)

## This is how data looks if standard scatter_matrix function will be used.
As presented on the picture data is not readable.
![Scatter_matrix effect](https://github.com/jkowalski995/Scatter_matrix_plotly/blob/main/scatter_matrix.png)

## After using the function from this repository.
Data plot is sliced into parts which consist 6 columns (first column from next figure is doubled with figure from earlier file).
Every figure has names of columns on the top of file.
Function genearate in the same time \*.png and \*.html file. It takes some time so to make it faster just comment the lines with \*.png files generation.
![Fisrt slice of matrix](https://github.com/jkowalski995/Scatter_matrix_plotly/blob/main/fig1.png)


I know that the code is not perfect and maybe one day I will wrap it into one `def`
