# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-neptune-cluster-multi-az@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk.aws_rds import DatabaseInstance

class CdkStarter(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id) 

        # Compliant: Enables `multiAz`, ensuring high availability and fault tolerance for the database.
        DatabaseInstance(Stack, 'rDatabaseCluster', 
            multi_az=True
        )
# {/fact}
