"""
netcdf_extractor.py

NetCDF Geographic Data Extractor.

Slices multidimensional NetCDF (.nc) climate/environmental datasets
by target latitude/longitude coordinates and exports to CSV.
"""

from typing import Any

import numpy as np
import pandas as pd
import xarray as xr


def create_sample_netcdf_dataset() -> xr.Dataset:
    """Generates a synthetic NetCDF dataset for local testing."""
    times = pd.date_range("2026-01-01", periods=5, freq="D")
    lats = np.linspace(-35.0, -10.0, 5)  # Sample Australian latitudes
    lons = np.linspace(110.0, 155.0, 5)  # Sample Australian longitudes

    # Create dummy temperature data (5x5x5 array)
    temp_data = 15.0 + 10.0 * np.random.randn(len(times), len(lats), len(lons))

    return xr.Dataset(
        data_vars={"temperature": (["time", "lat", "lon"], temp_data)},
        coords={"time": times, "lat": lats, "lon": lons},
        attrs={"description": "Mock climate dataset for unit testing"},
    )


def extract_point_data(
    ds: xr.Dataset, target_lat: float, target_lon: float
) -> pd.DataFrame:
    """Extracts time-series data for the nearest latitude/longitude coordinate."""
    subset = ds.sel(lat=target_lat, lon=target_lon, method="nearest")
    return subset.to_dataframe().reset_index()


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
    print("\n--- NetCDF Extractor Demonstration ---")

    # 1. Generate sample dataset
    ds = create_sample_netcdf_dataset()
    print("\nDataset Overview:")
    print(ds)

    # 2. Extract spatial point (Perth area coordinates)
    target_lat, target_lon = -31.9522, 115.8614
    df_extracted = extract_point_data(ds, target_lat=target_lat, target_lon=target_lon)

    print(f"\nExtracted Data for Nearest Point (Lat: {target_lat}, Lon: {target_lon}):")
    print(df_extracted[["time", "lat", "lon", "temperature"]])
