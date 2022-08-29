# Image-Web-Scrapper-Python
This repo contains the code to create an image web scrapper written in Python using AWS Serverless Architecture and CDK.

Python code scrapes a particular weblink, finds the images and writes them to S3. This project uses the serverless architect on AWS cloud. Specific services/tools used in this project are S3, Lambda, Lambda Layer, IAM, AWS CDK, and Python.

Quick Summary of used AWS services:

#### AWS Lambda
A serverless, event-driven compute service from AWS that lets you process data at scale

#### AWS CDK
AWS CDK is an infrastrcutre as a code service which is less verbose than other similar services like CloudFormation etc. It lets you create infrastructure using a programming language. For this project, I've used Python. For more information, visit this link: https://docs.aws.amazon.com/cdk/v2/guide/home.html

#### Lambda Layers
An easy way to package your libraries abd other dependencies that you ca use with your lambda code. Using layer reduces the size of your overall deployment package, thus making it possible to edit the code inline within lambda. It is also a faster way of deploying and testing the code.

