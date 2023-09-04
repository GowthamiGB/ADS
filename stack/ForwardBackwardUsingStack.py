class Browser:
    def __init__(self):
        self.backward_stack=[]
        self.forward_stack=[]
        self.current_url=None

    def visit(self,url):
        if self.current_url:
            self.backward_stack.append(self.current_url)
            self.forward_stack=[]  # Clear the forward stack when visiting a new page
        self.current_url=url

    def go_back(self):
        if self.backward_stack:
            self.forward_stack.append(self.current_url)
            self.current_url=self.backward_stack.pop()

    def go_forward(self):
        if self.forward_stack:
            self.backward_stack.append(self.current_url)
            self.current_url=self.forward_stack.pop()

    def current_page(self):
        return self.current_url

# Create a browser instance
my_browser=Browser()

# visit webpages

my_browser.visit("https://www.google.com")
my_browser.visit("https://www.openai.com")
my_browser.visit("https://www.example.com")

# Print the current page
print("Current Page:", my_browser.current_page())

# Go back one page
my_browser.go_back()
print("Current Page (after going back):", my_browser.current_page())

# Go forward one page
my_browser.go_forward()
print("Current Page (after going forward):", my_browser.current_page())

