# n8n-comment-checker

The repository demonstrates the use of a n8n workflow for checking if a comment is valid or is insulting etc. with OpenAI Classifier Node.

The n8n workflow checks the comment of the fronted via webhook and saves it in a PostgreSQL database.
Insulting comments are also saved into this google sheet:
https://docs.google.com/spreadsheets/d/1Xf5KHPmKEgvMJW8-NI6aXEcr60HJwRt1Qa5Ft4-NsCk/edit?gid=0#gid=0

Comment-Checker: https://hendrikst.space/n8n-comment-checker


![Alt text](assets/workflow.png?raw=true "Workflow")
