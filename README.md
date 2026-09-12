# California Housing Boxplot

This code loads the California Housing dataset then produces and saves charts that analyze housing features like age, median income and median home values.

## Data

The California Housing dataset contains 20,640 rows and 9 columns which are detailed below.

| Column | Description |
|---|---|
| `MedInc` | Median income in the block group (tens of thousands of USD) |
| `HouseAge` | Median house age in the block group (years) |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | Block group population |
| `AveOccup` | Average number of household members |
| `Latitude` | Block group latitude |
| `Longitude` | Block group longitude |
| `MedHouseVal` | Median house value (hundreds of thousands of USD) — target variable |

No download is required; scikit-learn fetches the data automatically on first run and caches it locally.

## How to Run
Two commands and you're done!

**Step 1** — Install requirements by running the below:  
python -m pip install -r requirements.txt

This project depends on three Python packages listed in `requirements.txt`:
**pandas** for data handling 
**matplotlib** for plotting charts
**scikit-learn** for sourcing the California Housing dataset. This dataset is built in so no need to download anything seperately.


**Step 2** — Run script using the below:  
python src/boxplot.py

This generates out charts for analysis!

## Expected Output

Running the script produces a histogram of house ages and two boxplots comparing median income and median home values. These charts are automatically saved to repository.

