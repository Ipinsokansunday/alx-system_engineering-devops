#!/usr/bin/env ruby
# Function to extract sender, receiver, and flags from a text message
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
