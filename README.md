# Data Analytics Application

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Setup and Installation](#setup-and-installation)
  - [Docker Setup](#docker-setup)
  - [Running the Application](#running-the-application)
  - [Testing](#testing)
- [Kubernetes Deployment](#kubernetes-deployment)
  - [Using Minikube](#using-minikube)
- [Configuration Management with Ansible](#configuration-management-with-ansible)

## Overview

This project is a data analytics application designed to run in a Docker container and deployable to a Kubernetes cluster using Minikube. The application reads data from a file, performs analysis, and displays the results through a Flask web interface.

## Directory Structure

```plaintext
.
├── data                  # Directory for input data files
├── src                   # Application source code
│   ├── app.py            # Flask application
│   ├── analysis.py       # Analysis functions
│   └── utils.py          # Utility functions
├── tests                 # Test cases
│   └── test_analysis.py  # Test for analysis module
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── k8s                   # Kubernetes manifests
    ├── deployment.yaml   # Deployment configuration
    └── service.yaml      # Service configuration
