import re

def match_tags(html):
    stack = []  # Create an empty stack to keep track of opening tags

    # Use regular expression to find all tags
    tags = re.findall(r'<[^>]+>', html)

    for tag in tags:
        if tag.startswith('</'):
            # Closing tag
            if not stack:
                return False  # No corresponding opening tag
            last_opening_tag = stack.pop()
            if last_opening_tag != tag[2:-1]:
                return False  # Mismatched opening and closing tags
        elif tag.endswith('/>'):
            # Self-closing tag
            pass
        else:
            # Opening tag
            stack.append(tag[1:-1])

    # If the stack is empty at the end, all tags have been matched
    return len(stack) == 0

# Test the function with an HTML string
html_string = "<html><head><title>Example</title></head><body><h1 class='header'>Hello, World!</h1></body></html>"
result = match_tags(html_string)

if result:
    print("All HTML tags are matched.")
else:
    print("HTML tags are not matched.")
