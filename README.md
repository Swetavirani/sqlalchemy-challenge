## sqlalchemy-challenge

# Climate Analysis and Exploration

Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database, using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Precipitation Analysis

- Finding the most recent date in the dataset.
- Using that date, to get the previous 12 months of precipitation data by querying the previous 12 months of data.
- Loading the query results into a Pandas DataFrame using "date" and "prcp" values, and setting the index to the "date" column.
- Sort the DataFrame values by "date".
- Plotting the results by using the DataFrame plot method:
![image](https://user-images.githubusercontent.com/102982635/224783880-9c0c5363-44ab-468e-b671-8cd9ca855514.png)


- Use Pandas to print the summary statistics for the precipitation data.

Station Analysis

- Calculating the total number of stations in the dataset.
- Finding the most-active stations (that is, the stations that have the most rows) by listing the stations and observation counts in descending order and finding the station id that has the greatest number of observations.
- Calculating the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Plot a histogram by the previous 12 months of temperature observation (TOBS) data , filter by the station that has the greatest number of observations.
![image](https://user-images.githubusercontent.com/102982635/224784022-996e19a5-314e-422b-974c-eb55c601c944.png)


Climate App

/

Start at the homepage.

List all the available routes.

/api/v1.0/precipitation

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations

Return a JSON list of stations from the dataset.
/api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

