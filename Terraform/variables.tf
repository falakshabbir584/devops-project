variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "service_account_key_file" {
  description = "Path to the GCP service account JSON key file"
  type        = string
}
