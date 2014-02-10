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

# NOTE: need to replace ampersands first, since if we replace the other
# symbols first, there may be strings like '&gt;' where replacing the
# ampersands will yield '&amp;gt;', which is an incorrect result.
def escape_html(s):
	for ( i, o ) in ( ( '&', '&amp;'  ),
	                  ( '>', '&gt;'   ),
	                  ( '<', '&lt;'   ),
	                  ( '"', '&quot;' ) ):
		s = s.replace( i, o )
	return s

print escape_html( '<html> This is a simple form & I "like" it too!' )

