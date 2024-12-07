import requests
import pandas as pd

try:
    # Fetching data from properties API
    properties_api = requests.get('http://127.0.0.1:8000/api/properties')
    properties_api.raise_for_status()
    properties_api_data = properties_api.json()
    
    # Ensure the dataset has enough rows, potentially with pagination logic
    properties = [
        {**prop['fields'], 'id': prop['pk']} for prop in properties_api_data['properties']
    ]
    vdf = pd.DataFrame(properties)

    # Fetching data from tenants API
    tenants_api = requests.get('http://127.0.0.1:8000/api/tenants')
    tenants_api.raise_for_status()
    tenants_api_data = tenants_api.json()
    
    tenants = [
        {**tenant['fields'], 'id': tenant['pk']} for tenant in tenants_api_data['properties']
    ]
    odf = pd.DataFrame(tenants)
    
    # Merging the two datasets
    inner_merged_df = pd.merge(vdf, odf, on='id', how='inner')
    print(f"Shape of merged data: {inner_merged_df.shape}")
    
    # Task 2: Describe the dataset
    print("Dataset description:")
    print(inner_merged_df.describe())  # Statistical summary
    print(inner_merged_df.info())  # Data types, non-null counts

    # Task 3: Find and replace null values
    # Replace nulls with a placeholder or drop rows/columns as needed
    inner_merged_df.fillna('Missing', inplace=True)  # Replace nulls with 'Missing'
    # Alternatively, you can drop rows with missing values
    # inner_merged_df.dropna(inplace=True)

    # Task 4: Basic preprocessing (Handling duplicates, ensuring correct data types)
    inner_merged_df.drop_duplicates(inplace=True)  # Drop duplicates if any
    # Optionally, convert columns to appropriate data types
    # inner_merged_df['column_name'] = inner_merged_df['column_name'].astype('int')

    # Task 5: Create new features
    # For example, if 'rental_price' and 'area' are columns, you can create a price_per_area feature
    inner_merged_df['price_per_area'] = inner_merged_df['rental_price'] / inner_merged_df['area']

    # Show the first few rows of the processed data
    print(inner_merged_df.head())
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except KeyError as e:
    print(f"Key error: {e} - Check the response structure.")
