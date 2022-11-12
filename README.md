# boto3-mgmt-events

[In Progress]

Personal scripts to automate management of AWS resources using Python

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
        <!-- <tr>
            <td colspan=4, style="text-align: left">S3</td>
        </tr>
        <tr>
            <td width="50%">[description]</td>
            <td><code>[classes]</code></td>
            <td><code>[methods]</code></td>
            <td><a href="">link</a></td>
        </tr>
        <tr>
            <td colspan=4></td>
        </tr>
        <tr>
            <td colspan=4, style="text-align: left">DynamoDB</td>
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
            <td colspan=4, style="text-align: left">EC2</td>
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
            <td colspan=4></td>
        </tr>
        <!-- <tr>
            <td colspan=4, style="text-align: left">SNS</td>
        </tr>
        <tr>
            <td width="50%">[description]</td>
            <td><code>[classes]</code></td>
            <td><code>[methods]</code></td>
            <td><a href="">link</a></td>
        </tr>
        <tr>
            <td colspan=4></td>
        </tr>
        <tr>
            <td colspan=4, style="text-align: left">Lambda</td>
        </tr>
        <tr>
            <td width="50%">[description]</td>
            <td><code>[classes]</code></td>
            <td><code>[methods]</code></td>
            <td><a href="">link</a></td>
        </tr>
        <tr>
            <td colspan=4></td>
        </tr>
        <tr>
            <td colspan=4, style="text-align: left">CloudWatch Logs</td>
        </tr>
        <tr>
            <td width="50%">[description]</td>
            <td><code>[classes]</code></td>
            <td><code>[methods]</code></td>
            <td><a href="">link</a></td>
        </tr> -->
        <tr>
            <td colspan=4, style="text-align: left">CloudWatch</td>
        </tr>
        <tr>
            <td rowspan=2 width="50%">Delete CloudWatch metric alarms</td>
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

Refer to [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
