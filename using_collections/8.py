text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# line 3 slices so the string is 'for the fjords!' and then says on index 8 is the last occurance of 'f'
# line 4 is also looking for the last usage of 'f' but its still using the entire string. Line 3 basically created another string so its length decreased