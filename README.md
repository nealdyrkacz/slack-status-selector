# slack-status-selector
Raspberry Pi Slack Status Selector Project

************************************************************
*Preliminary Steps*

1. Create a Slack App in your workspace
2. Add User permissions:
   - users.profile:read
   - users.profile:write
   - users:write
3. Install App to workspace and acquire needed auth tokens
4. Acquire user id from Slack
5. Add User Id / Token references in `sendStatus.py`

*************************************************************

Code runs on Raspberry Pi 2 Model B / Jessie / python 3.4.2

*Run code*
`python3 status.py` 


