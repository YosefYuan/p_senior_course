text = ' Today,   is, Sunday '
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]

print(text_list)
