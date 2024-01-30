#!/usr/bin/env ruby
# Check if the argument matches the regular expression
match_result = ARGV[0].scan(/School/).join
puts match_result.empty? ? "$" : match_result
