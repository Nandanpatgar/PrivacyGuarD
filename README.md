# PrivacyGuarD

**A Context-Aware Sensitive Information Detection and Redaction System**

PrivacyGuarD  is a Python-based application designed to identify sensitive information in text, analyse the context in which the information may be shared, classify privacy risks, and redact sensitive data before sharing.

The project aims to help users recognise potential privacy risks and make safer decisions when sharing text with external platforms or services.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Workflow](#system-workflow)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Testing and Evaluation](#testing-and-evaluation)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Security Considerations](#security-considerations)
- [License](#license)

## Overview

Sharing text through online platforms can unintentionally expose personal, organisational, or technical information. Such information may include email addresses, phone numbers, employee identifiers, account identifiers, IP addresses, and personal names.

PrivacyGuard AI addresses this problem through a multi-stage privacy analysis pipeline. It combines pattern-based detection, named entity recognition, contextual analysis, risk classification, and automated redaction.

The application provides a user interface where users can submit text, inspect detected information, review privacy risks, and download sanitised text and analysis reports.

## Key Features

### 1. Sensitive Information Detection

Identifies potentially sensitive information using regular expressions and spaCy-based Named Entity Recognition.

Supported categories include:

- Email addresses
- Phone numbers
- Employee IDs
- Account IDs
- PAN-like identifiers
- IPv4 addresses
- Personal names detected through named entity recognition

Detection performance depends on the input format, detection rules, and language model.

### 2. Context Analysis

Analyses the sharing context to help determine whether the detected information may create a privacy risk.

### 3. Privacy Risk Classification

Classifies the identified privacy risk based on the application's implemented rules and analysis results.

### 4. Automated Data Redaction

Replaces detected sensitive information with placeholders to generate a sanitised version of the original text.

### 5. Privacy-Preserving Results

Displays masked sensitive values in the results interface to reduce unnecessary exposure of the original information.

### 6. Report Generation

Generates downloadable reports containing the analysis results and detected privacy risks.

### 7. Testing and Evaluation

Includes test scripts and evaluation utilities for checking detection behaviour and measuring performance on the available test data.

## System Workflow

The application follows this general workflow:

```text
                User Input
                    |
                    v
       Sensitive Information Detection
                    |
                    v
             Context Analysis
                    |
                    v
          Privacy Risk Classification
                    |
                    v
          Sensitive Data Redaction
                    |
                    v
             Results Dashboard
                    |
          +---------+---------+
          |                   |
          v                   v
    Sanitised Text       Analysis Report
       Download             Download
```

### Workflow Explanation

1. **User Input:** The user enters text containing information that needs to be analysed.
2. **Detection:** The detection module identifies potentially sensitive information using regular expressions and named entity recognition.
3. **Context Analysis:** The context analyser evaluates the sharing context according to the implemented rules.
4. **Risk Classification:** The risk classifier determines the privacy risk based on the available analysis results.
5. **Redaction:** The redaction module replaces detected sensitive values with placeholders.
6. **Results:** The application displays the analysis results and provides options to download sanitised text and reports.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Regular Expressions | Pattern-based sensitive information detection |
| spaCy | Named Entity Recognition |
| HTML and CSS | Web presentation and styling, where implemented |
| scikit-learn | Evaluation or machine learning utilities, where used |
| Git | Version control |
| GitHub | Source code hosting |

## Project Structure

```text
PrivacyGuardAI/
│
├── main.py
├── detector.py
├── context_analyzer.py
├── risk_classifier.py
├── redactor.py
├── report_generator.py
├── privacy_utils.py
│
├── evaluate_detector.py
├── evaluate_metrics.py
│
├── test_context.py
├── test_detector.py
├── test_ip_validation.py
├── test_privacy.py
├── test_redactor.py
├── test_report_generation.py
├── test_risk_classifier.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

**Note:** The structure above represents the intended organisation of the project. Keep only the files and folders that actually exist in your repository. The `static/` directory is optional if your current implementation does not use it.

## Installation and Setup

Follow these steps to run PrivacyGuard AI locally.

### Prerequisites

Install the following software:

- Python
- Git
- Visual Studio Code (recommended)

### 1. Clone the Repository

Replace `<your-github-username>` with your GitHub username.

```bash
git clone https://github.com/<your-github-username>/PrivacyGuardAI.git
```

Navigate to the project directory:

```bash
cd PrivacyGuardAI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install Dependencies

Ensure that `requirements.txt` contains the dependencies required by your project.

Install them using:

```bash
python -m pip install -r requirements.txt
```

### 5. Download the spaCy Language Model

If it is not already installed, run:

```bash
python -m spacy download en_core_web_sm
```

### 6. Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

The application will start locally. Open the URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Launch the PrivacyGuard AI application.
2. Enter or paste the text you want to analyse.
3. Select the appropriate sharing destination if the interface provides that option.
4. Run the privacy scan.
5. Review the detected sensitive information.
6. Examine the context analysis and privacy risk classification.
7. Review the sanitised text generated by the application.
8. Download the sanitised text or analysis report if required.

**Important:** Review the sanitised output before sharing it. Automated detection may miss sensitive information or incorrectly identify ordinary text as sensitive.

## Testing and Evaluation

The project includes test and evaluation scripts for checking the implemented modules.

Run the following commands from the project root after activating the virtual environment.

### Test Sensitive Information Detection

```bash
python test_detector.py
```

### Test Context Analysis

```bash
python test_context.py
```

### Test IP Address Validation

```bash
python test_ip_validation.py
```

### Test Redaction

```bash
python test_redactor.py
```

### Test Privacy Utilities

```bash
python test_privacy.py
```

### Test Risk Classification

```bash
python test_risk_classifier.py
```

### Test Report Generation

```bash
python test_report_generation.py
```

### Evaluate Detection

```bash
python evaluate_detector.py
```

### Evaluate Performance Metrics

```bash
python evaluate_metrics.py
```

The results depend on the test cases and evaluation dataset. Performance measured on a small test dataset should not be interpreted as guaranteed accuracy in real-world applications.

## Limitations

- Regular-expression detection depends on the patterns defined in the application.
- Named Entity Recognition may fail to identify some personal names, particularly ambiguous names or names appearing in unusual formats.
- The system may produce false positives by identifying ordinary text as sensitive information.
- The system may produce false negatives by failing to detect some sensitive information.
- Context analysis and risk classification depend on the rules implemented in the current version.
- Detection results may vary depending on the language, structure, and quality of the input text.
- The application should not be considered a complete privacy compliance or data-loss prevention solution.

## Future Enhancements

Potential improvements include:

- Expanding the range of supported sensitive information categories.
- Improving detection accuracy using additional models and datasets.
- Introducing more advanced context-aware risk assessment.
- Supporting multiple languages.
- Adding custom detection rules for different organisations.
- Improving evaluation using larger and more diverse datasets.
- Developing a more flexible frontend using separate HTML, CSS, and JavaScript files.
- Adding authentication and access control if required.
- Supporting additional report formats.
- Exploring integration with document processing and enterprise privacy workflows.

## Security Considerations

PrivacyGuard AI is a prototype intended to demonstrate sensitive information detection and redaction.

Before using it with confidential or personal information, consider the following:

- Avoid entering real confidential information during development and testing.
- Do not publish private datasets, credentials, API keys, or personal information to GitHub.
- Review the redacted output before sharing it externally.
- Remember that redaction is only as reliable as the detection process.
- Apply appropriate access controls and secure data handling practices before deploying the application in a production environment.

## License

This project is available for educational and research purposes.

A formal open-source licence has not been specified. Add a `LICENSE` file if you intend to distribute the project under a particular licence.

---

**PrivacyGuard AI — Detect sensitive information, assess privacy risks, and support safer text sharing.**
