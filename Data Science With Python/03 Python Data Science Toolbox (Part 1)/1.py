# bringing it all together
# Define count_entries()
import pandas as pd

tweets_df = pd.DataFrame( {'lang':['en','et','und'],'source':[
    '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>',
    '<a href="http://www.facebook.com/twitter" rel="nofollow">Facebook</a>',
    '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>']})
    
    # '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
    # '<a href="http://www.twitter.com" rel="nofollow">Twitter for BlackBerry</a>',
    # '<a href="http://www.google.com/" rel="nofollow">Google</a>',
    # '<a href="http://twitter.com/#!/download/ipad" rel="nofollow">Twitter for iPad</a>',
    # '<a href="http://linkis.com" rel="nofollow">Linkis.com</a>',
    # '<a href="http://rutracker.org/forum/viewforum.php?f=93" rel="nofollow">newzlasz</a>',
    # '<a href="http://ifttt.com" rel="nofollow">IFTTT</a>',
    # '<a href="http://www.myplume.com/" rel="nofollow">Plume\xa0for\xa0Android</a>']})

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)