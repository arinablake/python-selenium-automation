def well(x):
  count_good = 0
  for i in x:
      if i == 'good':
          count_good += 1
  if count_good > 2:
      return 'I smell a series!'
  elif count_good >= 1:
      return 'Publish!'
  else:
      return 'Fail!'

print(well(['good', 'good', 'good', 'bad', 'bad']))



# def well(x):
#     if x.count("good") == 0:
#         return "Fail!"
#     elif x.count("good") <= 2:
#         return "Publish!"
#     else:
#         return "I smell a series!"