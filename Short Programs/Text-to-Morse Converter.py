morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.'}
text = "SOS"
print(' '.join([morse_code.get(c.upper(), ' ') for c in text]))
# Output: ... --- ...