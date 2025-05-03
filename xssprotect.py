import cgi
import html

def sanitize_input(user_input):
    # Sanitize the user input by escaping any HTML characters
    sanitized_input = html.escape(user_input)
    return sanitized_input

# Example usage
user_input = "<script>alert('Hacked');</script>"
safe_input = sanitize_input(user_input)
print(safe_input)  # Output: &lt;script&gt;alert('Hacked');&lt;/script&gt;
