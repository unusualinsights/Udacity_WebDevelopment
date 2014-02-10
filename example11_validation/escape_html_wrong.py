# User Instructions
# 
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
    return s % { '>': '&gt;', '<': '&lt;', '"': '&quot;', '&': '&amp;' }

print escape_html( '<html> This is a simple form & I "like" it too!' )

