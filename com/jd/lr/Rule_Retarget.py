#!/user/bin/python
#-*-coding:utf-8-*-


class Retarget(object):
    def __init__(self,filePaths,outPath):
        self.filePaths = filePaths
        self.outPath = outPath
    def getRetarget(self):
        user_retarget={}
        for filepath in self.filePaths:
            for line in open(filepath,'r').readlines():
                splits = line.strip().split(',')
                user = splits[0].strip()
                sku = splits[1].strip()
                type = splits[4].strip()
                if not(cmp(type,"4")==0 or cmp(type,"1")==0 or cmp(type,"2")==0 or cmp(type,"5")==0):
                    continue
                if str(int(float(user))) in user_retarget.keys():
                    user_dict = user_retarget[str(int(float(user)))]
                    if sku in user_dict.keys():
                        user_dict[sku] = user_dict[sku]+1
                    else:
                        user_dict[sku]=1
                    user_retarget[str(int(float(user)))] = user_dict
                else:
                    user_dict={}
                    user_dict[sku]=1
                    user_retarget[str(int(float(user)))]=user_dict
        return user_retarget

    def getRetargetResult(self):
        user_retarget = self.getRetarget()
        out_handler = open(self.outPath,'w')
        out_handler.write("user_id,sku_id\n")
        out_handler.flush()
        for (k,v)in user_retarget.items():
            sort_user_dict = sorted(v.iteritems(),key =lambda t:t[1],reverse=True)
            out_handler.write(k+','+sort_user_dict[0][0]+'\n')
            out_handler.flush()
        out_handler.close()



if __name__ =="__main__":
    #retarget = Retarget(["/Users/gaominghui/Desktop/match/Data_Action_201602.csv",
    #                     "/Users/gaominghui/Desktop/match/Data_Action_201603.csv",
    #                     "/Users/gaominghui/Desktop/match/Data_Action_201603_extra.csv",
    #                     "/Users/gaominghui/Desktop/match/Data_Action_201604.csv",],'/Users/gaominghui/Desktop/match/Rule_Retarget.csv')
    retarget = Retarget(["/Users/gaominghui/Desktop/match/Data_Action_201604.csv"],"/Users/gaominghui/Desktop/match/Rule_Retarget_2.csv")
    retarget.getRetargetResult()
    print 'done'