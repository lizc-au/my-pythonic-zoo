"""
test_netcdf_extractor.py

Unit and integration tests for netcdf_extractor module.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd

from data_cleaning.netcdf_extractor import extract_coordinate_subset


def test_extract_coordinate_subset_calls_xarray_and_exports_csv(
    tmp_path: Path,
) -> None:
    """Verify xarray selection and DataFrame export to CSV."""
    mock_dataset = MagicMock()
    mock_subset = MagicMock()
    mock_dataset.sel.return_value = mock_subset

    mock_df = MagicMock(spec=pd.DataFrame)
    mock_subset.to_dataframe.return_value = mock_df
    mock_df.reset_index.return_value = mock_df

    output_csv = str(tmp_path / "test_output.csv")

    extract_coordinate_subset(
        dataset=mock_dataset, lat=48.8566, lon=2.3522, output_csv=output_csv
    )

    mock_dataset.sel.assert_called_once_with(lat=48.8566, lon=2.3522, method="nearest")
    mock_subset.to_dataframe.assert_called_once()
    mock_df.reset_index.assert_called_once()
    mock_df.to_csv.assert_called_once_with(output_csv, index=False)


@patch("xarray.open_dataset")
def test_open_and_extract_integration(
    mock_open_dataset: MagicMock, tmp_path: Path
) -> None:
    """Test full file opening and subsetting pipeline using tmp_path."""
    mock_ds = MagicMock()
    mock_open_dataset.return_value = mock_ds
    mock_subset = MagicMock()
    mock_ds.sel.return_value = mock_subset

    # Create dummy DataFrame payload
    mock_df = pd.DataFrame({"time": ["2026-01-01"], "pm2p5": [12.5]})
    mock_subset.to_dataframe.return_value = mock_df

    output_csv = str(tmp_path / "integration_output.csv")

    extract_coordinate_subset(
        dataset=mock_ds, lat=52.52, lon=13.40, output_csv=output_csv
    )

    # Confirm file generation on disk
    assert (tmp_path / "integration_output.csv").exists()
