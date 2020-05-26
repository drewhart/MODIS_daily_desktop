import os

# get files and date
home_dir = '/home/drew/'
txt_file = os.path.join(home_dir, 'MODIS_daily_img/today.txt')
img_file = os.path.join(home_dir, 'Pictures/MODIS_daily.jpg')
print(txt_file)
with open(txt_file, 'r') as f:
    date = f.readlines()[0].strip()

# archive image and text
archive_dir = os.path.join(home_dir, 'MODIS_daily_img/archive', date)
os.mkdir(archive_dir)
txt_cp_cmd = 'cp %s %s' % (txt_file, os.path.join(archive_dir,
                                                  'description.txt'))
img_cp_cmd = 'cp %s %s' % (img_file, os.path.join(archive_dir, 'img.jpg'))
os.system(txt_cp_cmd)
os.system(img_cp_cmd)


