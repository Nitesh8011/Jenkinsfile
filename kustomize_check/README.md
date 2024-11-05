# Kustomize Check

This repository is set up to perform a Kustomize validation check as part of a Jenkins pipeline.

## Files

- **Jenkinsfile**: Contains the Jenkins pipeline configuration for running the Kustomize check.
- **kustomize.sh**: The script that performs the Kustomize validation. This script checks if the Kubernetes YAML files are properly customized and formatted.

## Getting Started

To set up and run the Kustomize check:

1. **Add `kustomize.sh` to Your Repository**: Ensure that `kustomize.sh` is present in your repository, as it contains the logic for the Kustomize validation.
  
2. **Run with Jenkins**: The pipeline is configured in `Jenkinsfile`. Once your Jenkins environment is set up, it will automatically execute the `kustomize.sh` script as part of the build process.

## Usage

The `kustomize.sh` script will validate all YAML files customized through Kustomize in your repository. If there are any issues, it will report them in the Jenkins build log.

### Running Locally

To run the `kustomize.sh` script locally, simply execute:

```bash
./kustomize.sh
