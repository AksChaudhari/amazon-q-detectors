# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=terraform-restrict-neptume-public-access@v1.0 defects=1}
resource "aws_neptune_cluster_instance" "neptune_instance" {
  count              = 2
  cluster_identifier = aws_neptune_cluster.encrypted_neptune_cluster.cluster_identifier
  engine             = "neptune"
  instance_class     = "db.r4.large"
  apply_immediately  = true
  # Noncompliant: Neptune Cluster instance is publicly available.
  publicly_accessible = true
}
# {/fact}