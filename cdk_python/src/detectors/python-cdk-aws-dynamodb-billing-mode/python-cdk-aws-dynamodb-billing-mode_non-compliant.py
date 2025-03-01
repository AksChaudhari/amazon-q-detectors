# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-aws-dynamodb-billing-mode@v1.0 defects=1}
import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk.aws_dynamodb import Table, AttributeType,Attribute

class CdkStarterStack(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id)

        # Noncompliant: `billing_mode` is not set to `PAY_PER_REQUEST`.
        Table(Stack, "GlobalTable", partition_key=Attribute(name="pk", type=AttributeType.STRING))
        # {/fact}
