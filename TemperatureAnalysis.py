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
    
    def largest_temp_range(self, output_file_path="largest_temp_range_station.txt"):
        """Find and save the station with the largest temperature range."""
        
                
    def temperature_stability(self, output_file_path="temperature_stability_stations.txt"):
        """Find and save the most stable and most variable stations."""



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