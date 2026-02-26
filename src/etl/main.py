import pandas as pd
from transform import transform_data
from datetime import datetime
import os
import logging
import yaml


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    # Load configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    input_path = config["input_path"]
    output_base_path = config["output_base_path"]

    # EXTRACT
    logging.info("Extracting Data...")
    df = pd.read_csv(input_path)

    logging.info("Original Data:")
    logging.info(f"\n{df}")

    # TRANSFORM
    df_transformed = transform_data(df)

    logging.info("Transformed Data:")
    logging.info(f"\n{df_transformed}")

    # LOAD
    today = datetime.today().strftime("%Y-%m-%d")
    output_path = f"{output_base_path}/date={today}"

    os.makedirs(output_path, exist_ok=True)

    file_path = f"{output_path}/data.parquet"
    df_transformed.to_parquet(file_path, index=False)

    logging.info(f"Data successfully written to {file_path}")


if __name__ == "__main__":
    main()