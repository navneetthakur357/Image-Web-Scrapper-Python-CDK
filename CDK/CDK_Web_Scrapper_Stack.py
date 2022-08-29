# import aws modules
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam as _iam,
    aws_s3 as _s3,   
)
class CdkWebScrapperStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create a bucket
        bucket = _s3.Bucket(self, "enverusdemoscapper20220826"
            ,bucket_name="enverusdemoscapper20220826",
        ),
            
        lambda_role = _iam.Role(scope=self, id='web_scrapper_everus_lambda_role_20220826',
                    assumed_by= _iam.ServicePrincipal('lambda.amazonaws.com'),
                    role_name = 'web_scrapper_everus_lambda_role_20220826',
                    managed_policies=[
                        _iam.ManagedPolicy.from_aws_managed_policy_name(
                        'service-role/AWSLambdaBasicExecutionRole'),
                        _iam.ManagedPolicy.from_aws_managed_policy_name(
                            "AmazonS3FullAccess"
                        )
                    ])

        lambdaLayer = _lambda.LayerVersion(self, 'lambda-layer-20220826',
                  code = _lambda.AssetCode('python'),
                  compatible_runtimes = [_lambda.Runtime.PYTHON_3_8],      
        )  

        #define lambda resource
        my_lambda = _lambda.Function(
            self, 'Enverus_Web_Scrapper',
            runtime = _lambda.Runtime.PYTHON_3_8,
            code = _lambda.Code.from_asset('Lambda_Web_Scrapper'),
            handler = 'Webscrapper_Lambda.lambda_handler',
            timeout= Duration.seconds(900),
            layers=[lambdaLayer],
            role=lambda_role
        )





        
   
