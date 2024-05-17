#!/bin/bash

# Check if the configuration already exists
if ! grep -q "holberton" /etc/security/limits.d/90-holberton.conf; then
    # Add the limits for the holberton user
    echo -e "holberton soft nofile 4096
holberton hard nofile 4096" > /etc/security/limits.d/90-holberton.conf
    echo "User limits set successfully."
else
    echo "User limits already set."
fi
