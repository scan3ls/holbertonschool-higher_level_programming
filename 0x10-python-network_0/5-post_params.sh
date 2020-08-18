#!/bin/bash
# sends custom header content
curl -s -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" $1
