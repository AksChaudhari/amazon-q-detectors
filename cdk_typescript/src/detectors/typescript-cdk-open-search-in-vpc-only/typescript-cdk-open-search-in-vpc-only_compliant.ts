// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=typescript-cdk-open-search-in-vpc-only@v1.0 defects=0}
import { CfnDomain as LegacyCfnDomain } from 'aws-cdk-lib/aws-elasticsearch';
import * as cdk from 'aws-cdk-lib';
import { Stack } from "aws-cdk-lib/core";

export class CdkStarterStack extends cdk.Stack {
    constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Compliant: The LegacyCfnDomain instantiation sets `subnetIds`.
        new LegacyCfnDomain(Stack, 'Domain', {
            vpcOptions: {
                subnetIds: ['mycoolsubnet'],
            },
        });
    }
}// {/fact}
