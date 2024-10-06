s = input('')
print('До замены =', s.count('%'))
s = s.replace(':', '%')
print('После замены = ', s.count('%'))
