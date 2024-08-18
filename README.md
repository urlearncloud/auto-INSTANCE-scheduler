## Serverless EC2 Instance Scheduler for Company Working Hours 


### steps :-

create instance

policy for one lambda function ( start-lambdafunction )

--->  service = ec2    ---->  Actions allowed = select  " DescribeInstances , StartInstances "

--->  Resources  = all

--->  Policy name = start-ec2-policy

policy for one lambda function ( stop-lambdafunction )

--->  service = ec2    ---->  Actions allowed = select  " DescribeInstances , StopInstances "

--->  Resources  = all

--->  Policy name = stop-ec2-policy
