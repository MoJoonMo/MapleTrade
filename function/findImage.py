from . import gui as gf

def findImage(img_gray, img_rgb, kind):
    
    standard = []
    standard_mid = [0,0,'0']
    standard_end = [0,0,'0']

    if kind == "starforce":
        star_cnt = 0
        starforce_list = ['star']
        for sf in starforce_list:
            w, h, loc = gf.matchTemplate(img_gray,sf, 0.9) 
            for pt in zip(*loc[::-1]):
                break_yn = 'N'
                for xloc in range(w):
                    for yloc in range(h):
                        (b, g, r) = img_rgb[pt[1]+xloc, pt[0]+yloc]
                        #print(pt[1]+xloc,pt[0]+yloc,b,g,r)
                        if b <=2 and g>= 220 and g<=222 and r>= 254:
                            star_cnt = star_cnt + 1
                            break_yn = "Y"
                            break
                    if break_yn == "Y":
                        break
        return star_cnt
    elif kind == "standard":
        edge_list = ['center','center_archer','center_chief','center_chief','center_knight','center_magician','center_pirate','center_xenon','upg','potenability','addipotenoption','potenoption','potenoption2','potenoption3','potenoption4']
        for eg in edge_list: 
            w, h, loc = gf.matchTemplate(img_gray,'edge/' + eg, 0.9) 
            for pt in zip(*loc[::-1]):
                if eg == "upg" or eg == "potenability" or eg == "potenoption" or eg == "potenoption2" or eg == "potenoption3" or eg == "potenoption4" :
                    standard_mid = [pt[1],pt[0],eg]
                elif eg == "addipotenoption":
                    standard_end = [pt[1],pt[0],eg]
                else:
                    standard = [pt[1],pt[0],eg] # y,x,name
        return standard, standard_mid, standard_end