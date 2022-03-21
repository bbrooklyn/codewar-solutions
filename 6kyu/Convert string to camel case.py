def to_camel_case(text):
    if text:
        sl = text.split('_') if text.count('_') > text.count('-') else text.split('-')
        s = sl[0]
        for a in sl[1:]:
            s=s+a.capitalize()
        return s
    else:
        return text
