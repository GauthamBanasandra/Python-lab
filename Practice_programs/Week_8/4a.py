__author__ = 'gauth_000'
string='''this is a multiline string.
it spans over multiple lines.'''
words=(word for word in sorted(string.split(), key=len, reverse=True)[:2])
print(list(words))