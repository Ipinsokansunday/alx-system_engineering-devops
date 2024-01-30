#!/usr/bin/env ruby
# Check if the argument matches the regular expression for 10 capital letters
puts ARGV[0].scan(/[A-Z]*/).join
