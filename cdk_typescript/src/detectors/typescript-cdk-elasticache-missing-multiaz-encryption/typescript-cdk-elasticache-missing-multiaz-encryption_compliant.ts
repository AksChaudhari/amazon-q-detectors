// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=typescript-cdk-elasticache-missing-multiAz-encryption@v1.0 defects=0}
import {
    CfnReplicationGroup
} from 'aws-cdk-lib/aws-elasticache';
import * as cdk from 'aws-cdk-lib';
import { Stack } from "aws-cdk-lib";

export class CdkStarterStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // Complaint: Enables Multi-AZ deployment for high availability and failover support.
    new CfnReplicationGroup(Stack, 'rRedisGroup', {
      cacheNodeType: 'cache.t3.micro',
      engine: 'redis',
      replicationGroupDescription: 'lorem ipsum dolor sit amet',
      cacheSubnetGroupName: 'lorem',
      multiAzEnabled: true
    });
  }
}
// {/fact}