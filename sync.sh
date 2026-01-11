#!/bin/bash

rsync -avz server n8n \
-e "ssh -i ~/.ssh/t490/key" \
root@37.27.38.223:/root/n8n-comment-checker
