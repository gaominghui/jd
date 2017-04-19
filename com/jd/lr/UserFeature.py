#!/usr/bin/pyhon
#-*-coding:utf-8 -*-



class UserFeature(object):
    def __init__(self, userFilePath,outPath):
        self.userFilePath = userFilePath
        self.outPath = outPath
    def get_user_feature_dict(self):
        age_map = {}
        sex_map = {}
        lv_cd_map = {}
        reg_tm_map = {}
        for line in open(self.userFilePath,'r').readlines():
            splits = line.strip().split(",")
            age = splits[1].strip()
            sex = splits[2].strip()
            lv_cd = splits[3].strip()
            reg_tm = splits[4].strip()
            if age in age_map.keys():
                age_map[age] = age_map[age]+1
            else :
                age_map[age] = 1

            if sex in sex_map.keys():
                sex_map[sex] = sex_map[sex]+1
            else :
                sex_map[sex] = 1

            if lv_cd in lv_cd_map.keys():
                lv_cd_map[lv_cd] = lv_cd_map[lv_cd]+1
            else :
                lv_cd_map[lv_cd] = 1

            if reg_tm[0:7] in reg_tm_map.keys():
                reg_tm_map[reg_tm[0:7]] = reg_tm_map[reg_tm[0:7]]+1
            else :
                reg_tm_map[reg_tm[0:7]] = 1
        del age_map['age']
        del sex_map['sex']
        del lv_cd_map['user_lv_cd']
        del reg_tm_map['user_re']
        return (age_map,sex_map,lv_cd_map,reg_tm_map)

    def onehotcode(self):
        age_map, sex_map, lv_cd_map, reg_tm_map = self.get_user_feature_dict()
        age_code_map = {"NULL":"10000000","-1":"01000000","15岁以下":"00100000",
                        "16-25岁":"00010000","26-35岁":"00001000",
                        "36-45岁":"00000100","46-55岁":"00000010","56岁以上":"00000001"}
        sex_code_map = {"NULL":"1000","0":"0100","1":"0010","2":"0001"}
        lv_cd_code_map = {"1":"10000","2":"01000","3":"00100","4":"00010","5":"00001"}
        reg_tm_code_map = {}
        temp_keys = sorted(reg_tm_map.keys())
        for i in range(len(temp_keys)):
            reg_tm_code_map[temp_keys[i]] = "0"*(i)+"1" + "0"*(len(reg_tm_map)-(i+1))
        return (age_code_map,sex_code_map,lv_cd_code_map,reg_tm_code_map)

    def getUserOneHotCode(self,outflag=True):
        if outflag:
            out_handler = open(self.outPath,'w')
        age_code_map, sex_code_map, lv_cd_code_map, reg_tm_code_map =self.onehotcode()
        user_onehot_feature={}
        for line in open(self.userFilePath).readlines():
            splits = line.strip().split(",")
            user = splits[0].strip()
            if cmp(user,"user_id") ==0 :
                continue
            age = splits[1].strip()
            sex = splits[2].strip()
            lv_cd = splits[3].strip()
            reg_tm = splits[4].strip()
            temp = age_code_map[age]+sex_code_map[sex]+\
                lv_cd_code_map[lv_cd]+reg_tm_code_map[reg_tm[0:7]]
            user_onehot_feature[user]=temp
            if outflag:
                out_handler.write(user+"\t"+temp+"\n")
                out_handler.flush()
        return user_onehot_feature













if __name__ == "__main__":
    user = UserFeature("/Users/gaominghui/Desktop/match/utf8_Data_User.csv","/Users/gaominghui/mowork/pywork/jd/user_onehot_feature.txt")
    user_onehot_feature = user.getUserOneHotCode()
    print "done"










