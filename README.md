To create the s3 bucket:

- dependencias: - terraform

- execute:
  - terraform init
  - terraform plan
  - terraform apply -var-file "yourcredentialsfile"

To run the app.py

    - install boto3
    - install aws cli
    - configure yourprofile
    - create the txt.file
    - execute: python app.py
