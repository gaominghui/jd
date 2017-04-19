#!/usr/bin/pyhon
#-*-coding:utf-8 -*-



class ItemComment(object):
    def __init__(self, itemCommentPath,outPath):
        self.itemCommentPath = itemCommentPath
        self.outPath = outPath
    def get_item_comment_dict(self):
        date_map = {}
        comment_num_map = {}
        has_bad_comment_map = {}
        bad_comment_rate_map = {}


        for line in open(self.itemCommentPath,'r').readlines():
            splits = line.strip().split(",")
            date = splits[0].strip()
            if(cmp(date,"dt")==0):
                continue
            comment_num = splits[2].strip()
            has_bad_comment = splits[3].strip()
            bad_comment_rate = float(splits[4].strip())
            bad_comment_flag = -1
            if bad_comment_rate<=0.02:
                bad_comment_flag= 1
            elif bad_comment_rate>0.02 and bad_comment_rate<=0.05:
                bad_comment_flag =2
            elif bad_comment_rate>0.05 and bad_comment_rate<=0.1:
                bad_comment_flag =3
            elif bad_comment_rate>0.1 and bad_comment_rate<=0.2:
                bad_comment_flag = 4
            elif bad_comment_rate>0.2 and bad_comment_rate<=0.3:
                bad_comment_flag = 5
            elif bad_comment_rate>0.3 and bad_comment_rate<=0.4:
                bad_comment_flag = 6
            elif bad_comment_rate>0.4:
                bad_comment_flag = 7

            if date in date_map.keys():
                date_map[date] = date_map[date]+1
            else :
                date_map[date] = 1
            if comment_num in comment_num_map.keys():
                comment_num_map[comment_num] = comment_num_map[comment_num]+1
            else :
                comment_num_map[comment_num] = 1
            if has_bad_comment in has_bad_comment_map.keys():
                has_bad_comment_map[has_bad_comment] = has_bad_comment_map[has_bad_comment]+1
            else :
                has_bad_comment_map[has_bad_comment] = 1

            if bad_comment_flag in bad_comment_rate_map.keys():
                bad_comment_rate_map[bad_comment_flag] = bad_comment_rate_map[bad_comment_flag]+1
            else :
                bad_comment_rate_map[bad_comment_flag] = 1


        return (date_map,comment_num_map,has_bad_comment_map,bad_comment_rate_map)

    def onehotcode(self):
        comment_num_code_map = {"0":"10000","1":"01000","2":"00100","3":"00010","4":"00001"}
        has_bad_comment_code_map = {"0":"10","1":"01"}
        bad_comment_rate_code_map ={"1":"1000000","2":"0100000","3":"0010000","4":"0001000","5":"0000100","6":"00000010","7":"0000001"}
        return (comment_num_code_map,has_bad_comment_code_map,bad_comment_rate_code_map)


    def getitemOneHotCode(self,outflag=True):
        out_handler = open(self.outPath,'w')
        comment_num_code_map, has_bad_comment_code_map, bad_comment_rate_code_map  =self.onehotcode()

        item_onehot_comment_feature={}
        for line in open(self.itemCommentPath).readlines():
            splits = line.strip().split(",")
            item = splits[1].strip()
            if cmp(item,"sku_id") ==0 :
                continue
            date = splits[0].strip()
            if not (cmp(date,"2016-04-15")==0):
                continue
            comment_num = splits[2].strip()
            has_bad_comment = splits[3].strip()
            bad_comment_rate = float(splits[4].strip())
            bad_comment_flag = -1
            if bad_comment_rate<=0.02:
                bad_comment_flag= 1
            elif bad_comment_rate>0.02 and bad_comment_rate<=0.05:
                bad_comment_flag =2
            elif bad_comment_rate>0.05 and bad_comment_rate<=0.1:
                bad_comment_flag =3
            elif bad_comment_rate>0.1 and bad_comment_rate<=0.2:
                bad_comment_flag = 4
            elif bad_comment_rate>0.2 and bad_comment_rate<=0.3:
                bad_comment_flag = 5
            elif bad_comment_rate>0.3 and bad_comment_rate<=0.4:
                bad_comment_flag = 6
            elif bad_comment_rate>0.4:
                bad_comment_flag = 7
            temp = comment_num_code_map[comment_num]+has_bad_comment_code_map[has_bad_comment]+ \
                   bad_comment_rate_code_map[str(bad_comment_flag)]
            item_onehot_comment_feature[item]=temp
        if outflag:
            for (k,v) in item_onehot_comment_feature.items():
                out_handler.write(k+"\t"+v)
                out_handler.flush()
        out_handler.close()
        return item_onehot_comment_feature


if __name__ == "__main__":
    print "begin"
    item = ItemComment("/Users/gaominghui/Desktop/match/utf8_Data_Comment.csv","/Users/gaominghui/mowork/pywork/jd/item_onehot_comment.txt")
    item.getitemOneHotCode()
    print 'done'














