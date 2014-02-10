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
    if( month == '' ):
        return None
    monthList = list( month.lower() );
    monthList[0] = monthList[0].upper();
    Month = ''.join( monthList )
    for m in months:
        if Month == m:
            return m
    return None

print valid_month( 'january' )
print valid_month( 'January' )
print valid_month( 'foo' )
print valid_month( '' )

# valid_month('january') => 'January'    
# valid_month('January') => 'January'
# valid_month('foo') => None
# valid_month('') => None


