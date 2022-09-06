from PIL import Image
import numpy as np

def get_img(name):
    path = 'img_library/'+name+'.png'
    fanwei = 50
    img = Image.open(path)
    #img.show()
    img_array = np.array(img)#把图像转成数组格式img = np.asarray(image)
    shape = img_array.shape
    height = shape[0]
    width = shape[1]
    dst = np.zeros((height,width,3))

    # [[[[max,min],[max,min],[max,min]],[x,y],[x,y]],[[[max,min],[max,min],[max,min]],[x,y],[x,y]]]
    # [[[max,min],[max,min],[max,min]],[x,y],[x,y]]
    # 将所有颜色分类
    point_list = []
    for h in range(0,height):
        for w in range (0,width):
            same = False
            (r,g,b) = img_array[h,w]
            if len(point_list)==0:
                point_list.append([[[r+fanwei,r-fanwei],[g+fanwei,g-fanwei],[b+fanwei,b-fanwei]],[h,w]])
                continue
            for i in range(0,len(point_list)):
                if point_list[i][0][0][0] >= r >= point_list[i][0][0][1] and point_list[i][0][1][0] >= g >= point_list[i][0][1][1] and point_list[i][0][2][0] >= b >= point_list[i][0][2][1]:
                    point_list[i].append([h,w])
                    same = True
                    break
            if not same:
                point_list.append([[[r+fanwei,r-fanwei],[g+fanwei,g-fanwei],[b+fanwei,b-fanwei]],[h,w]])
    # 按每个分类数量排序
    point_list.sort(key = lambda i:len(i),reverse=True)
    # 取前三位颜色
    t_num = 3
    for i in range(1,t_num+1):
        text = point_list[i]
        for te in range(1,len(text)):
            h = text[te][0]
            w = text[te][1]
            dst[h,w] = (255,255,255)
    # 去除零星碎点
    for h in range(0,height):
        for w in range (0,width):
            (r,g,b) = dst[h,w]
            if (r,g,b) != (255,255,255):
                continue
            count = 0
            t_h = h
            t_w = w
            hh = ''
            ww = ''
            # 图片边界判断
            if t_h==0:
                hh='+'
            if t_h==height-1:
                hh='-'
            if t_w==0:
                ww='+'
            if t_w==width-1:
                ww='-'
            if hh == '-':
                count+=1
            else:
                (r,g,b) = dst[t_h+1,t_w]
                if (r,g,b)!=(255,255,255):
                    count+=1
            if hh == '+':
                count+=1
            else:
                (r,g,b) = dst[t_h-1,t_w]
                if (r,g,b)!=(255,255,255):
                    count+=1
            if ww == '-':
                count+=1
            else:
                (r,g,b) = dst[t_h,t_w+1]
                if (r,g,b)!=(255,255,255):
                    count+=1
            if ww == '+':
                count+=1
            else:
                (r,g,b) = dst[t_h,t_w-1]
                if (r,g,b)!=(255,255,255):
                    count+=1
            # 上下左右有三个空白，就算干扰物，删除
            if count > 2:
                dst[h,w] = (0,0,0)
    img2 = Image.fromarray(np.uint8(dst))
    img2.save("image_store/"+name+".png","png")
if __name__ == "__main__":
    get_img('21_img_1662456656')