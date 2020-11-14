def add_time(start, duration, day=None):
	'''Function that add the duration time to the start time and return the result.'''

	start_time, start_period = start.split()
	start_h, start_m = start_time.split(':')
	duration_h, duration_m = duration.split(':')
	initial_period = start_period

	periods_passed = 0
	days_passed = 0

	new_h = int(start_h) + int(duration_h)
	new_m = int(start_m) + int(duration_m)

	if new_m > 59:
		new_m -= 60
		new_h += 1

	h_period = new_h


	while new_h > 12:
		new_h -= 12

	while h_period > 11:
		h_period -= 12
		start_period = 'PM' if start_period == 'AM' else 'AM'
		periods_passed += 1

	if periods_passed % 2 != 0:
		if initial_period == 'PM':
			periods_passed += 1
		else:
			periods_passed -= 1

	days_passed = periods_passed / 2

	days_of_week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
	
	result = f"{new_h}:{str(new_m).zfill(2)} {start_period}"

	if day:
		start_day_index = days_of_week.index(day.title())
		new_day_index = int((start_day_index + days_passed) % 7)
		result += f', {days_of_week[new_day_index]}'

	if days_passed == 1:
		result += ' (next day)'
			
	if days_passed > 1:
		result += f' ({int(days_passed)} days later)'

	return result