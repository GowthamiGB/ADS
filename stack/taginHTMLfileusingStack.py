# match tags in html file using stack 
def match_tags(HTML):
    stack=[]

    for ch in HTML:
        if ch=='<':
            stack.append('<')
        elif ch=='>':
            if not stack or stack.pop()!='<' :
                return False
    return len(stack)==0


# Test the function with an HTML string
HTML_string = "<html><head><title>Example</title></head><body><h1>Hello, World!</h1></body></html>"
result=match_tags(HTML_string)
if result:
    print("All HTML tags are matched.")
else:
    print("HTML tags are not matched.")