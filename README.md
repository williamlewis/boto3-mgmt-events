# boto3-mgmt-events

[In Progress]

Personal scripts to automate management of AWS resources using Python

</br>

When learning AWS, you must frequently create, modify, and delete resources for demo and test purposes.

Using Boto3 scripting, these repetitive actions can be automated for expediency and can help ensure that demo resources have been removed to avoid incurring unexpected costs.

</br>

[Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

<!---
Boto3 as defined in the official [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html):

> You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
--->

</br>

<table>
    <thead>
        <tr>
            <th>Description</th>
            <th>Classes</th>
            <th>Methods / Collections</th>
            <th>Link ↗</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan=4, style="text-align: left"><h2>S3</h2></td>
        </tr>
        <tr>
            <td>Create a new S3 bucket</td>
            <td><code>S3. ServiceResource</code></td>
            <td><code>.create_bucket()</code></td>
            <td><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/s3_create_bucket.py">s3 create bucket.py</a></td>
        </tr>
        <tr>
            <td rowspan="3">Delete a specific S3 bucket including all objects and object versions within</td>
            <td><code>S3. ServiceResource</code></td>
            <td><code>--</code></td>
            <td rowspan="3"><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/s3_delete_bucket_and_objects.py">s3 delete bucket and objects.py</a></td>
        </tr>
        <tr>
            <td><code>S3. Bucket</code></td>
            <td><code>.objects.all()</code> <code>.delete()</code></td>
        </tr>
        <tr>
            <td><code>S3. Object</code></td>
            <td><code>.object_versions_delete()</code> <code>.delete()</code></td>
        </tr>
        <!-- <tr>
            <td colspan=4></td>
        </tr>
        <tr>
            <td colspan=4, style="text-align: left"><h2>DynamoDB</h2></td>
        </tr>
        <tr>
            <td width="50%">[description]</td>
            <td><code>[classes]</code></td>
            <td><code>[methods]</code></td>
            <td><a href="">link</a></td>
        </tr>
        <tr>
            <td colspan=4></td>
        </tr> -->
        <tr>
            <td colspan=4, style="text-align: left"><h2>EC2</h2></td>
        </tr>
        <tr>
            <td>Launch a specified number of new instances from defined AMI & instance type</td>
            <td><code>EC2. Client</code></td>
            <td><code>.run_instances()</code></td>
            <td><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/ec2_launch_new_instances.py">ec2 launch new instances.py</a></td>
        </tr>
        <tr>
            <td>List out InstanceId attribute for all current instances</td>
            <td><code>EC2. ServiceResource</code></td>
            <td><code>.instances.all()</code></td>
            <td><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/ec2_get_all_instance_ids.py">ec2 get all instance ids.py</a></td>
        </tr>
        <tr>
            <td rowspan="2">Deregister (delete) a custom machine image from a specific region</td>
            <td><code>EC2. ServiceResource</code></td>
            <td><code>--</code></td>
            <td rowspan="2"><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/ec2_deregister_ami.py">ec2 deregister ami.py</a></td>
        </tr>
        <tr>
            <td><code>EC2. Image</code></td>
            <td><code>.deregister()</code></td>
        </tr>
        <!-- <tr>
            <td colspan=4></td>
        </tr>
        <tr>
            <td colspan=4, style="text-align: left"><h2>SNS</h2></td>
        </tr>
        <tr>
            <td width="50%">[description]</td>
            <td><code>[classes]</code></td>
            <td><code>[methods]</code></td>
            <td><a href="">link</a></td>
        </tr>
        <tr>
            <td colspan=4></td>
        </tr> -->
        <tr>
            <td colspan=4, style="text-align: left"><h2>Lambda</h2></td>
        </tr>
        <tr>
            <td>Delete a specific Lambda function</td>
            <td><code>Lambda. Client</code></td>
            <td><code>.delete_function()</code></td>
            <td><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/lambda_delete_function.py">lambda delete function.py</a></td>
        </tr>
        <!-- <tr>
            <td colspan=4></td>
        </tr> -->
        <tr>
            <td colspan=4, style="text-align: left"><h2>CloudWatch Logs</h2></td>
        </tr>
        <tr>
            <td>Find and delete log groups from CloudWatchLogs</td>
            <td><code>CloudWatchLogs. Client</code></td>
            <td><code>.describe_log_groups()</code> <code>.delete_log_group()</code></td>
            <td><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/cloudwatchlogs_delete_log_groups.py">cloudwatchlogs delete log groups.py</a></td>
        </tr>
        <tr>
            <td colspan=4, style="text-align: left"><h2>CloudWatch</h2></td>
        </tr>
        <tr>
            <td rowspan=2>Delete CloudWatch metric alarms</td>
            <td><code>CloudWatch. ServiceResource</code></td>
            <td><code>.alarms.all()</code></td>
            <td rowspan=2><a href="https://github.com/williamlewis/boto3-mgmt-events/blob/main/01%20-%20Terminal%20Scripts/cloudwatch_delete_alarms.py">cloudwatch delete alarms.py</a></td>
        </tr>
        <tr>
            <td><code>CloudWatch. Alarm</code></td>
            <td><code>.delete()</code></td>
        </tr>
    </tbody>
</table>

</br>


