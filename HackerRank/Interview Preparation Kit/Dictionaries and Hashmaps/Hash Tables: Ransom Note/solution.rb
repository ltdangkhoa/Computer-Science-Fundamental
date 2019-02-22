#!/bin/ruby

require 'json'
require 'stringio'

def checkMagazine(magazine, note)
  dict_magazine = {}
  for word in magazine do
    if !dict_magazine.has_key?(word)
      dict_magazine[word] = 1
    else
      dict_magazine[word] += 1
    end
  end

  can_replicate = TRUE
  for word in note do
    if dict_magazine[word] && dict_magazine[word] >= 1
        dict_magazine[word] -= 1
    else
        can_replicate = FALSE
        break
    end
  end

  puts can_replicate ? 'Yes' : 'No'

end

INPUT_PATH = 'input/'
Dir.foreach(INPUT_PATH) do |filename|
  next if filename == '.' or filename == '..'
  puts "📂 %s " % [filename]
  f = File.open(INPUT_PATH + filename)

  inputs = f.readlines
  input_line = 0
  mn = inputs[input_line].rstrip.split
  input_line += 1
  m = mn[0].to_i
  n = mn[1].to_i
  magazine = inputs[input_line].rstrip.split(' ').map(&:to_s)
  input_line += 1
  note = inputs[input_line].rstrip.split(' ').map(&:to_s)
  input_line += 1

  start = Time.now.to_f
  checkMagazine magazine, note
  timeit = Time.now.to_f - start
  puts "⏰ %0.12f seconds ⏰" % [timeit]
end
