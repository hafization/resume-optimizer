# Resume Optimizer

An AI-powered resume optimization tool that uses Claude API to tailor resumes for specific job descriptions.

## Features
- Reads your resume and job description
- Uses Claude AI to optimize resume content
- Highlights relevant skills and experience
- Generates professional, ATS-friendly output

## How It Works
1. Add your resume to `resume.txt`
2. Add job description to `job_description.txt`
3. Run `python main.py`
4. Check `optimized_resume.txt` for the optimized version

## Installation

```bash
pip install anthropic
```

## Setup

Set your Claude API key:

```bash
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

```bash
python main.py
```

## Requirements
- Python 3.7+
- Claude API key (get from https://console.anthropic.com/)

## Author
Hafization - AI Automation Services