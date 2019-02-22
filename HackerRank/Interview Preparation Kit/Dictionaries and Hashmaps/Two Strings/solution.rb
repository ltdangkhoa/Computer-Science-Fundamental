#!/bin/ruby

require 'json'
require 'stringio'

require 'set'

def twoStrings(s1, s2)
  my_set_1 = Set.new(s1.split(''))
  my_set_2 = Set.new(s2.split(''))
  my_sub_set = my_set_2 - my_set_1
  return my_sub_set != my_set_2 ? 'YES' : 'NO'
end

INPUT_PATH = 'input/'
Dir.foreach(INPUT_PATH) do |filename|
  next if filename == '.' or filename == '..'
  puts "📂 %s " % [filename]
  f = File.open(INPUT_PATH + filename)

  inputs = f.readlines
  input_line = 0
  q = inputs[input_line].to_i
  input_line += 1

  start = Time.now.to_f

  q.times do |q_itr|
    s1 = inputs[input_line].to_s.rstrip
    input_line += 1
    s2 = inputs[input_line].to_s.rstrip
    input_line += 1
    result = twoStrings s1, s2
  end

  timeit = Time.now.to_f - start
  puts "⏰ %0.12f seconds ⏰" % [timeit]
end
