#!/bin/bash

# wait for dynamodb to be ready
while ! curl -s http://localhost:4566/ > /dev/null; do
    sleep 1
done

# create fastrunner-table if it doesn't exist
aws --endpoint-url=http://localhost:4566 dynamodb describe-table --table-name fastrunner-table 2>/dev/null || \
    aws --endpoint-url=http://localhost:4566 dynamodb create-table --table-name fastrunner-table \
        --attribute-definitions AttributeName=id,AttributeType=S \
        --key-schema AttributeName=id,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

# add sample data to hogeTable
aws --endpoint-url=http://localhost:4566 dynamodb put-item --table-name fastrunner-table \
    --item '{"id": {"S": "1"}, "name": {"S": "Alice"}, "age": {"N": "25"}}'
aws --endpoint-url=http://localhost:4566 dynamodb put-item --table-name fastrunner-table \
    --item '{"id": {"S": "2"}, "name": {"S": "Bob"}, "age": {"N": "30"}}'