def number_count(input_list):
  in_s = sorted(input_list)
  output_dict = {}
  for i in in_s:
    output_dict.update({i: input_list.count(i)})
  return output_dict

input_list =  [1, 5, 1, 2, 2, 3, 4, 4]
output_dict = number_count(input_list)
print(output_dict)