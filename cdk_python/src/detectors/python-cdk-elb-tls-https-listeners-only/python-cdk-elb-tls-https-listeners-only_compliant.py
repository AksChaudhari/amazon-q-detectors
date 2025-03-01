# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-elb-tls-https-listeners-only@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk import Stack, Vpc
from aws_cdk.aws_elasticloadbalancing import LoadBalancer,LoadBalancingProtocol
from aws_cdk import aws_elasticloadbalancing as elb

class CdkStarterself(cdk.self):
  def __init__(self, scope: cdk.App, id: str):
    super(scope, id)
    # Compliant: The LoadBalancingProtocol is set to ssl for the both the protocol.
    LoadBalancer(self, 'rELB1', 
        vpc= Vpc(self, 'rVPC'),
    ).add_listener(
        internal_protocol= LoadBalancingProtocol.ssl,
        external_port= 42,
        external_protocol= LoadBalancingProtocol.ssl,
    )
    # {/fact}
