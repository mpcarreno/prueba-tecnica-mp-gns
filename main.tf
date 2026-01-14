
resource "aws_s3_bucket" "my_bucket" {
  bucket        = "prueba-tecnica-gns-mp-bucket"
  force_destroy = true

  tags = {
    Name        = "prueba-tecnica-gns-mp-bucket"
    Environment = var.environment
  }
}

resource "aws_s3_bucket_versioning" "my_bucket_versioning" {
  bucket = aws_s3_bucket.my_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}
