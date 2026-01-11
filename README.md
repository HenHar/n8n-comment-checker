# n8n-comment-checker

This repository demonstrates an automated **n8n workflow** designed to classify user comments using the **OpenAI Classifier Node**. It effectively filters comments to determine if they are valid, insulting, or inappropriate.

The n8n workflow checks the comment of the fronted via a webhook and saves it in a PostgreSQL database.
The OpenAI classifier node is used for checking the comment.
Insulting comments are also saved into this google sheet:
<a href="https://docs.google.com/spreadsheets/d/1Xf5KHPmKEgvMJW8-NI6aXEcr60HJwRt1Qa5Ft4-NsCk/edit?gid=0#gid=0" target="_blank">Google Sheet</a>

## Test It

You can see the system in action here:  
👉 [Comment-Checker Demo](https://hendrikst.space/n8n-comment-checker)

## Workflow Preview

![Alt text](assets/workflow.png?raw=true "Workflow")
