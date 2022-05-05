# Plotting scatter metrix for big datamatrix with Python plotly

During working with project for MUT in Warsaw I was working with Big DataSet (1,7 Gb, 58 data columns). 
Before starting the process for training the XGBoost algorythm it was necessary to cut off some data and to  
do this I was planning to plot scatter matrix. Due to the fact that this Data is so big I create the function 
to cut it into pieces and the present it to the user.

## The Data Matrix

![Presentation of Data Matrix](/home/jakub/PycharmProjects/plotly_big_scatter _matrix/matrix.png)

I know that the code is not perfect and maybe one ay I will wrap it into one `def`