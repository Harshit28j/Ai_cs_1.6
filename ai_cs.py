import pyautogui as pyg
import keyboard as k
import time as t 
cord=(0,310,800,50)  #cordinated of region
fire_shots=0
while True:
	ss=pyg.screenshot('test.png',region=cord)
	r,g,b=ss.getpixel((403,28))   	#to  get color at specific pixels
	print(r,g,b)
	if (r <40) or (g <40) or (b<40):
		print('YEs')
		pyg.click(403,320)		#click/shot in the middle of the region
		if fire_shots==5:
			pyg.moveTo(410,y)	#change position if fired 5 times 
			fire_shots=0
		t.sleep(1)
		fire_shots+=1         #fire shots count
	else:
		print('No')
		pyg.moveTo(430,320)		#change position if find nothing
		t.sleep(1)
	if k.is_pressed('q'):		#press q to exit
		break