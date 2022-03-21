def to_camel_case(text):
    sl = text.replace('-','_').split('_')
    if text:
        s = sl[0]
        for a in sl[1:]:
            s=s+a.capitalize()
        return s
    else:
        return text
