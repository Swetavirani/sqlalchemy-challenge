## sqlalchemy-challenge

# Climate Analysis and Exploration

Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database, using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Precipitation Analysis

- Finding the most recent date in the dataset.
- Using that date, to get the previous 12 months of precipitation data by querying the previous 12 months of data.
- Loading the query results into a Pandas DataFrame using "date" and "prcp" values, and setting the index to the "date" column.
- Sort the DataFrame values by "date".
- Plotting the results by using the DataFrame plot method:


- Use Pandas to print the summary statistics for the precipitation data.

Station Analysis

- Calculating the total number of stations in the dataset.
- Finding the most-active stations (that is, the stations that have the most rows) by listing the stations and observation counts in descending order and finding the station id that has the greatest number of observations.
- Calculating the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Plot a histogram by the previous 12 months of temperature observation (TOBS) data , filter by the station that has the greatest number of observations.


