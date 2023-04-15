import boto3
from app.setting import settings


class DynamoDBTable:
    def __init__(self, table_name, region_name="ap-northeast-1"):
        self.table_name = table_name
        self.region_name = region_name
        self.dynamodb = boto3.resource("dynamodb", region_name=self.region_name)
        self.dynamodb = boto3.resource(
            "dynamodb",
            endpoint_url=settings.LOCAL_STACK_ENDPOINT
            if settings.LOCAL_STACK_ENDPOINT
            else None,
        )
        self.table = self.dynamodb.Table(self.table_name)

    def put_item(self, item):
        response = self.table.put_item(Item=item)
        return response

    def get_item(self, key):
        response = self.table.get_item(Key=key)
        item = response.get("Item")
        return item

    def delete_item(self, key):
        response = self.table.delete_item(Key=key)
        return response

    def update_item(self, key, update_expression, expression_attribute_values):
        response = self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )
        return response

    def query(self, key_condition_expression, expression_attribute_values):
        response = self.table.query(
            KeyConditionExpression=key_condition_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )
        items = response.get("Items")
        return items

    def scan(self, filter_expression=None, expression_attribute_values=None):
        if filter_expression is None:
            response = self.table.scan()
        else:
            response = self.table.scan(
                FilterExpression=filter_expression,
                ExpressionAttributeValues=expression_attribute_values,
            )
        items = response.get("Items")
        return items
