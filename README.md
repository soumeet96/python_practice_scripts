# DevOps Scripts with Python and Boto3

Welcome to the **Python for DevOps Scripts** repository! This project is a collection of Python scripts aimed at automating common DevOps tasks, particularly in AWS environments. It leverages the power of `boto3`, AWS's SDK for Python, to interact seamlessly with AWS services.

## Features

- Automate AWS infrastructure tasks (e.g., EC2, S3, Lambda, RDS, etc.).
- Perform common DevOps operations like deployments, backups, monitoring, and more.
- Reusable and modular Python scripts for various AWS and DevOps use cases.

## Getting Started

### Prerequisites

1. **Python 3.7+**
   Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Install `boto3`**
   Install `boto3` using pip:
   ```bash
   pip install boto3
   ```

3. **AWS CLI (optional)**
   Although not mandatory, the AWS CLI can help set up credentials and test configurations. Install it from [AWS CLI Documentation](https://aws.amazon.com/cli/).

4. **AWS Credentials**
   Configure your AWS credentials (access key and secret key) using:
   ```bash
   aws configure
   ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/soumeet96/python_practice_scripts
   ```

2. Navigate to the project directory:
   ```bash
   cd scripts
   ```

## Usage

Each script in this repository is designed for a specific task. Navigate to the desired script, read the script's inline comments or accompanying documentation, and execute it as needed. Example:

```bash
python scripts/manage_s3_buckets.py --action create --bucket-name my-test-bucket
```

### Example Scripts

- **EC2 Management**: Start, stop, or terminate EC2 instances.
- **S3 Operations**: Create, list, and delete S3 buckets.
- **Lambda Deployment**: Automate Lambda function creation and updates.
- **RDS Snapshots**: Automate database snapshots and restorations.

## Folder Structure

```plaintext
.
├── scripts
│   ├── 01_manage_ec2_instances.py      # EC2-related operations
│   ├── s3_operations.py       # S3 bucket management
│   ├── lambda_deploy.py       # Lambda automation
│   └── ...                    # More scripts
├── utils
│   ├── common.py              # Reusable utility functions
│   └── config.py              # Configuration handling
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Contributing

Contributions are welcome! If you have a useful script or improvement, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature-name'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [AWS Documentation](https://docs.aws.amazon.com/)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

Happy automating! 🎉