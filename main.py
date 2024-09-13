import pandas as pd
from io import StringIO
import boto3

def upload_dict_to_s3_csv(order_data, bucket_name, s3_key):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(order_data)
    
    # Create a buffer to hold the CSV data
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    
    # Initialize the S3 client
    s3 = boto3.client('s3')
    
    # Upload the CSV data to S3
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=csv_buffer.getvalue())
    
    print("CSV file uploaded successfully!")

# Example usage
order_data = [
    {'OrderID': '001', 'Customer': 'John Doe', 'Product': 'Widget A', 'Quantity': 10, 'Price': 19.99},
    {'OrderID': '002', 'Customer': 'Jane Smith', 'Product': 'Widget B', 'Quantity': 5, 'Price': 29.99},
    {'OrderID': '003', 'Customer': 'Emily Johnson', 'Product': 'Widget C', 'Quantity': 7, 'Price': 39.99}
]

bucket_name = 'test-s3-650251706104'
s3_key = 'results/order_data.csv'

# Call the function
upload_dict_to_s3_csv(order_data, bucket_name, s3_key)
