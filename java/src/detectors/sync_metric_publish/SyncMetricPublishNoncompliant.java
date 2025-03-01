// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=java-sync-metric-publish@v1.0 defects=1}
import com.amazonaws.regions.Regions;
import com.amazonaws.services.cloudwatch.AmazonCloudWatch;
import com.amazonaws.services.cloudwatch.AmazonCloudWatchClientBuilder;
import com.amazonaws.services.cloudwatch.model.MetricDatum;
import com.amazonaws.services.cloudwatch.model.PutMetricDataRequest;
import com.amazonaws.services.cloudwatch.model.StandardUnit;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.ScheduledEvent;
public class SyncMetricPublishNoncompliant  implements RequestHandler<ScheduledEvent, Void> {

    AmazonCloudWatch cloudwatch;

    public SyncMetricPublishNoncompliant() {
        cloudwatch = AmazonCloudWatchClientBuilder.standard().withRegion(Regions.US_WEST_2.toString()).build();
    }

    // Noncompliant: Synchronous CloudWatch metric publishing within Lambda function, potentially increasing execution time and costs.
    @Override
    public Void nonCompliant(ScheduledEvent scheduledEvent, Context context) {
        final long startTime = System.currentTimeMillis();
        doSomething(scheduledEvent, context);
        final long endTime = System.currentTimeMillis();
        final long timeElapsed = endTime - startTime;
        PutMetricDataRequest putMetricDataRequest = new PutMetricDataRequest();
        MetricDatum metricDatum = new MetricDatum().withMetricName("TIME_ELAPSED")
                .withUnit(StandardUnit.Milliseconds).withValue((double) timeElapsed);
        putMetricDataRequest.withNamespace("EXAMPLE_NAMESPACE").withMetricData(metricDatum);
        cloudwatch.putMetricData(putMetricDataRequest);
        return null;
    }

    private void doSomething(ScheduledEvent scheduledEvent, Context context) {

    }
}
// {/fact}
