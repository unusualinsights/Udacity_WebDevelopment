# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
	if month:
		cap_month = month.capitalize()
		if cap_month in months:
			return cap_month

print valid_month( 'january' )
print valid_month( 'January' )
print valid_month( 'foo' )
print valid_month( '' )

# valid_month('january') => 'January'    
# valid_month('January') => 'January'
# valid_month('foo') => None
# valid_month('') => None


