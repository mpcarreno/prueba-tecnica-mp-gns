# Prueba Técnica - S3 Upload/Download Tool

## Prerequisites

- Python 3.x
- Terraform
- AWS CLI
- AWS credentials configured

## Setup

### 1. Configure AWS Credentials

```bash
aws configure
# or use the credentials file at ~/.aws/credentials
```

### 2. Install Python Dependencies

```bash
pip install boto3
```

## Terraform - Create S3 Bucket

### Initialize Terraform

```bash
terraform init
```

### Plan the deployment

```bash
terraform plan -var-file="vars.tfvars"
```

### Apply the configuration

```bash
terraform apply -var-file="vars.tfvars"
```

## Run the Python Application

### Basic Usage

```bash
# Download a file from S3
python app.py download

# Upload a file to S3
python app.py upload
```

### Advanced Usage with Custom Parameters

```bash
# Download with custom file name and bucket
python app.py download --file myfile.txt --bucket my-bucket-name

# Upload with custom file name and bucket
python app.py upload --file myfile.txt --bucket my-bucket-name
```

### Arguments

- `action` (required): Either `upload` or `download`
- `--file`: File name to process (default: file.txt)
- `--bucket`: S3 bucket name (default: prueba-tecnica-gns-mp-bucket)

## Example Workflow

```bash
# 1. Create the S3 bucket with Terraform
terraform apply -var-file="vars.tfvars"

# 2. Create a text file to upload
echo "Hello World" > file.txt

# 3. Upload the file to S3
python app.py upload --file file.txt

# 4. Download the file from S3
python app.py download --file file.txt
```

## Notes

- Ensure your AWS credentials are properly configured before running the application
- The default bucket name is `prueba-tecnica-gns-mp-bucket`
- The default file name is `file.txt`
