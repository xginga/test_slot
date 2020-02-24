from PIL import Image
import glob

marioes=glob.glob("./images/datasets/0mario/*")



for i in marioes:
	img = Image.open(i)
	r_img = img.rotate(270, expand=True)
	r_img = r_img.resize((150,150))
	
	r_img.save(i)