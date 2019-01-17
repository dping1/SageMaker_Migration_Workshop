# SageMaker Migration Workshop

SageMaker Migration Workshop is designed to enable data scientists/ML engineers with no or little SageMaker experience to build, train, and deploy customer's own machine learning models using SageMaker. The primary outcome of the workshop will be:

   - Hands-on experience with SageMaker and AWS ML ecosystem for customer's own ML use cases
   - An AWS sandbox environment for on-going ML experiments and testing
   - A set of working data science notebooks and training scripts for customer ML projects
   - A process and mechanism for training and deploy customer's own machine learning models for online prediction and/or batch prediction
 

## Pre-requisite
 - Model training scripts (Python preferred)
 - Training dataset
 - Non-production AWS account with limits increased for notebook instance, training instance, and hosting instance
     - SageMaker Notebook: ml.t2.medium
     - SageMaker Training: ml.m4.xlarge
     - SageMkaer Hosting: ml.m4.xlarge
 - A S3 Working bucket for storing data and output
 - AWS User accounts with the following IAM permission
     - Managed policy: AmazonSageMakerFullAccess
     - Custom policy for access to a S3 working bucket
     - Custom policy for a subset of IAM permission
 
Sample policy for S3 bucket access
```ruby
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:ListAllMyBuckets"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["<arn for the s3 bucket>"]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": ["<arn for the S3 bucket>/*"]
    }
  ]
}
```

Sample policy for SageMaker role management
    
```ruby
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": ["iam:CreateRole", "iam:CreatePolicy", "iam:AttachRolePolicy"],
    "Resource": "*"
  }
}

```

## Instruction

Follow the steps below to get started:

1. Follow the instruction below to create a SageMaker notebook

    - Open the Amazon SageMaker console at https://console.aws.amazon.com/sagemaker/.

    - Choose Notebook instances, then choose Create notebook instance.

    - On the Create notebook instance page, provide the following information:

         - For Notebook instance name, type a name for the noteboook instance.

         - For Instance type, choose ml.t2.medium.

         - For IAM role, create an IAM role.  Choose Create a new role. 
             - on the pop up screen, select **Specific S3 Bucket** and enter the bucket name for the lab
         - Change **volume size in GB** if need more than 5GB for data storage for the notebook instance
         - Leave other as defaults
         - Click on **Create Notebook Instance**
    - After the status changes to **InService**, click on **Open JupyterLab** to launch the Jupyter Notebook
    
             
2. Once you are inside the JupyterLab environment, follow the instruction below to download the content

    - Click the **Terminal** icon in the Launcher pane.
    - Type the command below inside the terminal to get into the CD SageMaker directory
     
    > `cd SageMaker`
    
    - Type the command below to download the content
    
    > `git clone https://github.com/dping1/SageMaker_Migration_Workshop.git`
    
3. You should see a new folder called **SageMaker-Migration-Workshop** is created inside the left pane. Double click on the folder to list its content. There are folders named **step-x**. And inside each folder, there is a notebook that starts with **step-x-instruction.ipynb**. Start with **step-1** and follow the instruction in **step-1-instruction.ipynb** to continue with the workshop. 