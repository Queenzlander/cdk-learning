import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2


class CdkVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html

        vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.10.0.0/16",
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[
                           ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Web",
                               cidr_mask=24),
                           ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                               name="App",
                               cidr_mask=24),
                           ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                               name="DB",
                               cidr_mask=24)
                           ]
                        )
