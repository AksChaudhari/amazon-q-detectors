// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=typescript-cdk-neptune-cluster-automatic-minor-version-upgrade@v1.0 defects=1}
import { Stack } from 'aws-cdk-lib';
import * as cdk from 'aws-cdk-lib';
import { CfnDBInstance } from 'aws-cdk-lib/aws-neptune';

export class CdkStarterStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);      
    // Noncompliant: Does not enable automatic minor version upgrades, risking outdated database versions.
    new CfnDBInstance(Stack, 'rDatabaseInstance', {
      dbInstanceClass: 'db.r4.2xlarge'
    });
  }
}
// {/fact}
