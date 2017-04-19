#!/usr/bin/pyhon
#-*-coding:utf-8 -*-



class ItemFeature(object):
    def __init__(self, itemFilePath,outPath):
        self.itemFilePath = itemFilePath
        self.outPath = outPath
    def get_item_feature_dict(self):
        feature1_map = {}
        feature2_map = {}
        feature3_map = {}
        cate_map = {}
        brand_map = {}
        for line in open(self.itemFilePath,'r').readlines():
            splits = line.strip().split(",")
            feature1 = splits[1].strip()
            feature2 = splits[2].strip()
            feature3 = splits[3].strip()
            cate = splits[4].strip()
            brand = splits[5].strip()
            if feature1 in feature1_map.keys():
                feature1_map[feature1] = feature1_map[feature1]+1
            else :
                feature1_map[feature1] = 1

            if feature2 in feature2_map.keys():
                feature2_map[feature2] = feature2_map[feature2]+1
            else :
                feature2_map[feature2] = 1

            if feature3 in feature3_map.keys():
                feature3_map[feature3] = feature3_map[feature3]+1
            else :
                feature3_map[feature3] = 1
            if cate in cate_map.keys():
                cate_map[cate] = cate_map[cate]+1
            else :
                cate_map[cate] = 1
            if brand in brand_map.keys():
                brand_map[brand] = brand_map[brand]+1
            else :
                brand_map[brand] = 1
        del feature1_map['a1']
        del feature2_map['a2']
        del feature3_map['a3']
        del cate_map['cate']
        del brand_map['brand']
        return (feature1_map,feature2_map,feature3_map,cate_map,brand_map)

    def onehotcode(self):
        feature1_map, feature2_map, feature3_map, cate_map,brand_map = self.get_item_feature_dict()
        feature1_code_map = {"-1":"1000","1":"0100","2":"0010","3":"0001"}
        feature2_code_map = {"-1":"100","1":"010","2":"001"}
        feature3_code_map = {"-1":"100","1":"010","2":"001"}
        cate_code_map ={"8":"1"}
        brand_code_map = {}
        temp_keys = sorted(brand_map.keys())
        for i in range(len(temp_keys)):
            brand_code_map[temp_keys[i]] = "0"*(i)+"1" + "0"*(len(brand_map)-(i+1))
        return (feature1_code_map,feature2_code_map,feature3_code_map,cate_code_map,brand_code_map)

    def getitemOneHotCode(self,outflag=True):
        if outflag:
            out_handler = open(self.outPath,'w')
        feature1_code_map, feature2_code_map, feature3_code_map, cate_code_map, brand_code_map =self.onehotcode()
        item_onehot_feature={}
        for line in open(self.itemFilePath).readlines():
            splits = line.strip().split(",")
            item = splits[0].strip()
            if cmp(item,"sku_id") ==0 :
                continue
            feature1 = splits[1].strip()
            feature2 = splits[2].strip()
            feature3 = splits[3].strip()
            cate = splits[4].strip()
            brand = splits[5].strip()
            temp = feature1_code_map[feature1]+feature2_code_map[feature2]+ \
                   feature3_code_map[feature3]+cate_code_map[cate]+brand_code_map[brand]
            item_onehot_feature[item]=temp
            if outflag:
                out_handler.write(item+"\t"+temp+"\n")
                out_handler.flush()
        return item_onehot_feature


if __name__ == "__main__":
    item = ItemFeature("/Users/gaominghui/Desktop/match/utf8_Data_Product.csv","/Users/gaominghui/mowork/pywork/jd/item_onehot_feature.txt")
    item.getitemOneHotCode()
    print 'done'













