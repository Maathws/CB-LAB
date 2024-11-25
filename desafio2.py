import boto3
import json
import os
from dotenv import load_dotenv

# apiResponse: Dados pós filtrados em função para separar conjunto de dados
# apiResponse = {
#         "amount": 100.5,
#         ...
#     }

# apiName: endpoint especifico
# apiName = "/res/getGuestChecks"


def uploadJsonS3(apiResponse, apiName, busDt):
    load_dotenv()

    fileName = f"response.json"
    fileKey = f"asa-norte-df/{apiName}/{busDt}/{fileName}"

    bucketName = "coco-bambu"

    s3 = boto3.client(
        service_name='s3',
        region_name= os.getenv("AWS_S3_REGION_NAME"),
        aws_access_key_id= os.getenv("AWS_S3_ACESS_KEY_ID"),
        aws_secret_access_key= os.getenv("AWS_S3_SECRET_KEY")
        )

    s3.put_object(
        Bucket=bucketName,
        Key=fileKey,
        Body=json.dumps(apiResponse),
        ContentType="application/json"
    )

    print(f"Dados armazenados em: s3://{bucketName}/{fileKey}")
