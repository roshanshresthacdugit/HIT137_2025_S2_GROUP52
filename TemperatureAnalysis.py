"""
Question 2: Temperature Analysis 
====================================================================
This program loads temperature data from CSV files, reshapes it into
a long format, and calculates:
- Seasonal averages
- Station with largest temperature range
- Most stable and most variable stations
"""

import glob
import os
import pandas as pd

class TemperatureAnalysis:
    """
    A class to analyze temperature data by seasons and stations.
    """

    MONTH_TO_SEASON = {
        "January": "Summer", "February": "Summer",
        "March": "Autumn", "April": "Autumn", "May": "Autumn",
        "June": "Winter", "July": "Winter", "August": "Winter",
        "September": "Spring", "October": "Spring", "November": "Spring",
        "December": "Summer"
    }

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.reshaped_df = None
        self.reshape()
    
    def reshape(self):
        """Reshape the DataFrame into long format and map months to seasons."""
        structured = self.df.melt(
            id_vars=["STATION_NAME", "STN_ID", "LAT", "LON", "Year"],
            value_vars=list(self.MONTH_TO_SEASON.keys()),
            var_name="Month",
            value_name="Temperature"
        )
        structured["Season"] = structured["Month"].map(self.MONTH_TO_SEASON)
        self.reshaped_df = structured.dropna(subset=["Temperature"])
    
    def seasonal_average(self, output_file_path="average_temp.txt"):
        """Calculate and save seasonal average temperatures."""
        seasonal_avg = self.reshaped_df.groupby("Season")["Temperature"].mean()
       
        with open(output_file_path,"w") as data:
            for season in ["Summer","Autumn","Winter","Spring"]:
                avg = seasonal_avg.get(season,float('nan'))
                if pd.notna(avg):
                    data.write(f"{season}: {avg:.1f}°C\n")
    
    def largest_temp_range(self, output_file_path="largest_temp_range_station.txt"):
        """Find and save the station with the largest temperature range."""
        stats = self.reshaped_df.groupby("STATION_NAME")["Temperature"].agg(['min', 'max'])
        stats['range'] = stats["max"] - stats["min"]
        max_range = stats["range"].max()
        top_stations = stats[stats["range"] == max_range]
        with open(output_file_path, "w") as f:
            for station, row in top_stations.iterrows():
                f.write(
                    f"Station {station}: Range {row['range']:.1f}°C "
                    f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
                )
       
                
    def temperature_stability(self, output_file_path="temperature_stability_stations.txt"):
        """Find and save the most stable and most variable stations."""
        stds = self.reshaped_df.groupby("STATION_NAME")["Temperature"].std()
        min_std = stds.min()
        max_std = stds.max()
        stable_stations = stds[stds == min_std]
        variable_stations = stds[stds == max_std]

        with open(output_file_path, "w") as data:
            for station, value in stable_stations.items():
                data.write(f"Most stable: Station {station}: StdDev {value:.1f}°C\n")
            for station, value in variable_stations.items():
                data.write(f"Most Variable: Station {station}: StdDev {value:.1f}°C\n")



def load_all_data() -> pd.DataFrame:
    """
    Load and combine all temperature CSV files from the ./temperatures/ directory.
    
    Returns:
        pd.DataFrame: Combined DataFrame with Year column included.
    """
    csv_files = glob.glob("./temperatures/*.csv")
    combined_df = []

    for file in csv_files:
        df = pd.read_csv(file)
        year = os.path.splitext(os.path.basename(file))[0].split('_')[-1]
        df["Year"] = int(year)
        combined_df.append(df)

    return pd.concat(combined_df, ignore_index=True)


def main():
    """Main function to run the temperature analysis."""
    try:
        df = load_all_data()
    except FileNotFoundError:
        print("Error: No CSV files found in ./temperatures/")
        return

    analysis = TemperatureAnalysis(df)
    analysis.largest_temp_range()
    analysis.temperature_stability()
    analysis.seasonal_average()
    print("Analysis completed. Results saved to text files.")

if __name__ == "__main__":
    main()
