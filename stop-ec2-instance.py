import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='ap-south-1') # Replace your Region name

    # Specify the instance ID of the EC2 instance you want to stop
    instance_id = 'import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='ap-south-1') # Replace your Region name

    # Specify the instance ID of the EC2 instance you want to start
    instance_id = 'i-01ad0101f699d7893' # Replace your Own Instance ID

    # Start the EC2 instance
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(f"Starting EC2 instance {instance_id}...")
        print(f"Response: {response}")
        return {
            'statusCode': 200,
            'body': f"EC2 instance {instance_id} is being started."
        }
    except Exception as e:
        print(f"Error starting EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting EC2 instance: {str(e)}"
        }' # Replace your Own Instance ID

    # Stop the EC2 instance
    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(f"Stopping EC2 instance {instance_id}...")
        print(f"Response: {response}")
        return {
            'statusCode': 200,
            'body': f"EC2 instance {instance_id} is being stopped."
        }
    except Exception as e:
        print(f"Error stopping EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Error stopping EC2 instance: {str(e)}"
        }
