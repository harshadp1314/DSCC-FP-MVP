from boto3.s3.transfer import S3Transfer
import boto3
import json

def store_data_in_s3(data):
    # Load credentials from configuration file
    with open("DSCC-FP-MVP-Configuration.json") as config_file:
        config = json.load(config_file)
    client = boto3.client('s3', aws_access_key_id=config["aws_access_key_id"],aws_secret_access_key=config["aws_secret_access_key"])
    
    transfer = S3Transfer(client)
    transfer.upload_file('C:/Users/vvsiv/Repos/DSCC-FP-MVP/apple_stock.csv', 'dsccfpmvpstorage', 'Data'+"/"+'apple_stock.csv')











# import boto3
# import json

# def store_data_in_dynamodb(data):
#     # Load credentials from configuration file
#     with open("DSCC-FP-MVP-Configuration.json") as config_file:
#         config = json.load(config_file)
    
#     # Connect to DynamoDB
#     dynamodb = boto3.resource(
#         "dynamodb",
#         aws_access_key_id=config["aws_access_key_id"],
#         aws_secret_access_key=config["aws_secret_access_key"]
#         # region_name=config["region_name"]
#     )
    
#     # Get the table reference
#     table = dynamodb.Table("dscc-fp-mvp-samsung-stock")
    
#     # Store the data in DynamoDB
#     table.put_item(Item=data)
