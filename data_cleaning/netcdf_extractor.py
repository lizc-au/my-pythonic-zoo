"""
netcdf_extractor.py

NetCDF Geographic Data Extractor.

Slices multidimensional NetCDF (.nc) climate/environmental datasets
by target latitude/longitude coordinates and exports to CSV.
"""

from typing import Any


def extract_coordinate_subset(
    dataset: Any,
    lat: float,
    lon: float,
    output_csv: str = "subset_output.csv",
) -> None:
    """Extracts data for the nearest lat/lon point and saves to CSV.

    Args:
        dataset: Opened xarray Dataset instance.
        lat: Latitude target value.
        lon: Longitude target value.
        output_csv: Target file path for the output CSV.
    """
    # Isolate nearest geographic coordinate slice
    subset = dataset.sel(lat=lat, lon=lon, method="nearest")

    # Flatten slice into pandas DataFrame and write to disk
    df = subset.to_dataframe().reset_index()
    df.to_csv(output_csv, index=False)
    print(f"Successfully extracted subset to {output_csv}")


if __name__ == "__main__":
    print("NetCDF Extractor module initialized.")
