#!/bin/bash

REPOSITORY_NAME="fastrunner-image"
TAG="latest"
REGION="ap-northeast-1"

# default ユーザーを取得
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# ECR にログイン
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# コンテナイメージをビルド
docker build -t $REPOSITORY_NAME:$TAG .

# コンテナイメージを ECR にプッシュ
docker tag $REPOSITORY_NAME:$TAG $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME:$TAG
docker push $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME:$TAG
