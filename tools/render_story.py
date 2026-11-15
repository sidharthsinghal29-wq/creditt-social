# Build 1080x1920 (9:16) story versions from the 4:5 feed images
import sys
from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/'
def story(src, dst, bg, top_text, top_col, bottom_text, bottom_col):
    W,H=1080,1920
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
    post=Image.open(src).convert('RGB').resize((1000,1250),Image.LANCZOS)
    y=(H-1250)//2
    im.paste(post,(40,y))
    tf=ImageFont.truetype(F+'Inter-Bold.otf',40)
    d.text(((W-d.textlength(top_text,font=tf))/2,(y-tf.size)//2),top_text,font=tf,fill=top_col)
    bf=ImageFont.truetype(F+'Inter-Bold.otf',44)
    yb=y+1250+((H-y-1250)-bf.size)//2
    d.text(((W-d.textlength(bottom_text,font=bf))/2,yb),bottom_text,font=bf,fill=bottom_col)
    im.save(dst,quality=92)
s=sys.argv[1]; p='posts/'+s
story(p+'.jpg',p+'-story.jpg','#413080',"Buyer's market update",'#FFD15D','Free chat: creditt.com.au','white')
story(p+'-aussie-linkedin.jpg',p+'-aussie-story.jpg','#413080','Home loan tip','#FFD11F','Call Sidharth: 0402 993 545','white')
