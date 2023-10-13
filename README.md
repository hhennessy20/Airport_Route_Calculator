# 480AirportProject

The project is a Python based AI utilizing A* to plot different routes that can be taken between airports on a map diagram.

## Setup
1. Install Anaconda (https://www.anaconda.com/download) and miniconda (https://docs.conda.io/projects/miniconda/en/latest/)
2. Set up a virtual environment in Pycharm using Anaconda. The Python version for this environment must be 2.7
   <ul>
     <li>This can be done using the following bash command:<pre>conda create --name your_project python=2.7</pre></li>
   </ul>
3. Open the project in an IDE such as PyCharm, and choose the newly created Conda environment as the Python Interpreter.
4. Click Install Dependencies, which should automatically install pandas, matplotlib, etc. If not, these may need to manually be selected in the Anaconda Navigator.
5. Run the frontend_wx.py file in Pycharm. 
6. The GUI should then open and allow the user to enter or select the desired start and end airports.
7. Rather than running frontend_wx.py, you can also run a test by running the main function in porthop.py, which uses the two airports BTV and LNZ (these can be changed in the main function).

## Sources & References
- https://lgoeller.github.io/2018/02/13/visualizing-flight-data-with-basemap.html
- https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter2/generic_search.py
- https://openflights.org/data.html
- https://www.kaggle.com/datasets/elmoallistair/airlines-airport-and-routes/
- https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements
- https://anaconda.org/anaconda/basemap
- https://openflights.org/data.html
