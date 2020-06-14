#!/bin/sh

# Setting Up Remote Development
ssh-keygen -t rsa -b 4096 -C "me@example.com" -f /home/cloud_user/.ssh/id_rsa-remote-ssh
ssh-copy-id -i ~/.ssh/id_rsa-remote-ssh.pub cloud_user@SERVER_ID.mylabserver.com
cat >> ~/.ssh/config << EOF
Host python-server
    User cloud_user
    HostName SERVER_ID.mylabserver.com
    IdentityFile ~/.ssh/id_rsa-remote-ssh
EOF
cat >> ~/.ssh/config << EOF
Host *
    AddKeysToAgent yes
    UseKeychain yes
    IdentitiesOnly yes
EOF
ssh-add -K ~/.ssh/id_rsa-remote-ssh
