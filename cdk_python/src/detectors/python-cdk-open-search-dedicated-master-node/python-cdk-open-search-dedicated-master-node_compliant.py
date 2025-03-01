# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-open-search-dedicated-master-node@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk.aws_opensearchservice import CapacityConfig
from aws_cdk.aws_elasticsearch import (
  Domain as LegacyDomain,
  ElasticsearchVersion
)
from aws_cdk.aws_elasticsearch import LoggingOptions

class CdkStarter(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id)

        # Compliant: Specifies`master_nodes` capacity, ensuring sufficient resources for the Elasticsearch cluster.
        LegacyDomain(self, 'Domain', 
            version= ElasticsearchVersion.V7_10,
            capacity= CapacityConfig( master_nodes= 42 ),
            logging= LoggingOptions(
                app_log_enabled=True,
                slow_index_log_enabled=True,
                slow_search_log_enabled=True,
                audit_log_enabled=True
            )
        )
# {/fact}
