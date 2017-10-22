
# Albert - Adgorithms Optimization Developer Exercise

#### 1.Find the best performing ad of the given time period


```python
import csv
import numpy as np

# load a csv
NUMBER_OF_LINES  = "Number of lines"
with open(r'C:\Users\hilatash\Downloads\albert\albert_dev_test.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = []
        i = 0
        lines = 0
        #parse number of lines from data
        for row in readCSV:
            if NUMBER_OF_LINES in row[0]:
                lines = int(row[0].split("-")[1])
                #next line is #
                readCSV.next()
                break

        #parse data into list
        for row in readCSV:
            if i < lines + 1:
                data.append(row)
            i = i + 1

        #convert list to dict with the relevants headlines
        ads_list = []
        dict_of_ads = {}
        headlines = data[0]
        #remove headlines from the data
        data.remove(data[0])
        ad_number = 1
        for line in data:
            ad_dict = {}
            ad_dict[headlines[0]] = line[0]
            ad_dict[headlines[1]] = line[1]
            ad_dict[headlines[2]] = line[2]
            ad_dict[headlines[3]] = line[3]
            ad_dict[headlines[4]] = line[4]
            ad_dict[headlines[5]] = line[5]
            ad_dict[headlines[6]] = line[6]
            ad_dict[headlines[7]] = line[7]
            ads_list.append(ad_dict)
            dict_of_ads[ad_number] = ad_dict
            ad_number += 1


        #Find the best performing ad of the given time period.
        best_ad_performance = -1
        best_ad_in_period = None
        for ad in ads_list:
            try:
                clicks = ad['clicks']
                impressions = ad['impressions']
                ad['CTR'] = float(clicks) /float(impressions)
            except Exception:
                ad['CTR'] = 0
            if ad['CTR'] > best_ad_performance:
                best_ad_performance = ad['CTR']
                best_ad_in_period = ad
        
        print "The best performing ad of the given time period - "
        print best_ad_in_period['headLine']
        print best_ad_in_period['bodyText'] 
        


```

    The best performing ad of the given time period - 
    Sporting Goods - The place for you!
    forget everything you know about sports
    

####   2. Find the best performing ad of each day within the time period.


```python
import csv
import numpy as np

# load a csv
NUMBER_OF_LINES  = "Number of lines"
with open(r'C:\Users\hilatash\Downloads\albert\albert_dev_test.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = []
        i = 0
        lines = 0
        #parse number of lines from data
        for row in readCSV:
            if NUMBER_OF_LINES in row[0]:
                lines = int(row[0].split("-")[1])
                #next line is #
                readCSV.next()
                break

        #parse data into list
        for row in readCSV:
            if i < lines + 1:
                data.append(row)
            i = i + 1

        #convert list to dict with the relevants headlines
        ads_list = []
        dict_of_ads = {}
        headlines = data[0]
        #remove headlines from the data
        data.remove(data[0])
        ad_number = 1
        for line in data:
            ad_dict = {}
            ad_dict[headlines[0]] = line[0]
            ad_dict[headlines[1]] = line[1]
            ad_dict[headlines[2]] = line[2]
            ad_dict[headlines[3]] = line[3]
            ad_dict[headlines[4]] = line[4]
            ad_dict[headlines[5]] = line[5]
            ad_dict[headlines[6]] = line[6]
            ad_dict[headlines[7]] = line[7]
            ads_list.append(ad_dict)
            dict_of_ads[ad_number] = ad_dict
            ad_number += 1


        #Find the best performing ad of the given time period.
        #sdd CTR key calculate ...#todo
        best_ad_performance = -1
        best_ad_in_period = None
        for ad in ads_list:
            try:
                clicks = ad['clicks']
                impressions = ad['impressions']
                ad['CTR'] = float(clicks) /float(impressions)
            except Exception:
                ad['CTR'] = 0
            if ad['CTR'] > best_ad_performance:
                best_ad_performance = ad['CTR']
                best_ad_in_period = ad

        #Find the best performing ad of each day within the time period.
        #create dict of days , for each day will be list of ads of this day
        #for example: ads_per_day['10.10.2016'] = {ad1,ad2,ad3}

        day = {}
        ads_per_day_dict = {}
        #create dict of empty lists
        for ad in ads_list:
            ads_per_day_dict[ad['date']] = []
        #add ads to list of ads per day
        for ad in ads_list:
            ads_per_day_dict[ad['date']].append(ad)

        best_ad_per_day = {}
        for date in ads_per_day_dict:
            best_ad_performance = -1
            for ad in ads_per_day_dict[date]:
                if ad['CTR'] > best_ad_performance:
                    best_ad_performance = ad['CTR']
                    best_ad = ad
            best_ad_per_day[date] = best_ad


        import pandas as pd
        print "Find the best performing ad of each day within the time period - "
        df = pd.DataFrame(columns=['best_ad_per_day'])
        for date in  best_ad_per_day:
            ad =  best_ad_per_day[date]['headLine'] +","+ best_ad_per_day[date]['bodyText']
            df.loc[date] = ad

        print df
```

    Find the best performing ad of each day within the time period - 
                                                  best_ad_per_day
    2016-10-19      Goods buy sports,don't do sports, its not fun
    2016-10-18             Buy sporting goods,balls, balls balls!
    2016-10-30      Goods buy sports,don't do sports, its not fun
    2016-10-15  Sporting Goods - The place for you!,Now socks ...
    2016-10-14  Buy sporting goods,forget everything you know ...
    2016-10-17  Sporting The Goods,forget everything you know ...
    2016-10-16  Goods buy sports,forget everything you know ab...
    2016-10-11             Buy sporting goods,balls, balls balls!
    2016-10-10  Buy sporting goods,forget everything you know ...
    2016-10-13  Sporting The Goods,forget everything you know ...
    2016-10-12             Sporting The Goods,balls, balls balls!
    2016-10-08             Sporting The Goods,balls, balls balls!
    2016-10-27             Buy sporting goods,balls, balls balls!
    2016-10-28  Sporting Goods - The place for you!,Now socks ...
    2016-10-07      Goods buy sports,don't do sports, its not fun
    2016-10-20  Sporting Goods - The place for you!,forget eve...
    2016-10-21  Sporting Goods - The place for you!,forget eve...
    2016-10-22              Buy sporting goods,Now socks on sale!
    2016-10-23             Buy sporting goods,balls, balls balls!
    2016-10-24             Buy sporting goods,balls, balls balls!
    2016-10-25  Buy sporting goods,forget everything you know ...
    2016-10-26  Sporting Goods - The place for you!,forget eve...
    2016-10-09  Buy sporting goods,forget everything you know ...
    2016-10-06             Buy sporting goods,balls, balls balls!
    2016-10-29              Sporting The Goods,Now socks on sale!
    2016-10-04    Buy sporting goods,don't do sports, its not fun
    2016-10-05  Sporting The Goods,forget everything you know ...
    2016-10-02                Goods buy sports,Now socks on sale!
    2016-10-03     Buy sporting goods,golf balls are the new rage
    2016-10-01              Buy sporting goods,Now socks on sale!
    

#### 3.Provide the ids and statistics of the best performing ad group and campaign for the given time



```python
import csv
import numpy as np

# load a csv
NUMBER_OF_LINES  = "Number of lines"
with open(r'C:\Users\hilatash\Downloads\albert\albert_dev_test.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = []
        i = 0
        lines = 0
        #parse number of lines from data
        for row in readCSV:
            if NUMBER_OF_LINES in row[0]:
                lines = int(row[0].split("-")[1])
                #next line is #
                readCSV.next()
                break

        #parse data into list
        for row in readCSV:
            if i < lines + 1:
                data.append(row)
            i = i + 1

        #convert list to dict with the relevants headlines
        ads_list = []
        dict_of_ads = {}
        headlines = data[0]
        #remove headlines from the data
        data.remove(data[0])
        ad_number = 1
        for line in data:
            ad_dict = {}
            ad_dict[headlines[0]] = line[0]
            ad_dict[headlines[1]] = line[1]
            ad_dict[headlines[2]] = line[2]
            ad_dict[headlines[3]] = line[3]
            ad_dict[headlines[4]] = line[4]
            ad_dict[headlines[5]] = line[5]
            ad_dict[headlines[6]] = line[6]
            ad_dict[headlines[7]] = line[7]
            ads_list.append(ad_dict)
            ad_number += 1    
        
        #Find the best performing ad of the given time period.
        best_ad_performance = -1
        best_ad_in_period = None
        for ad in ads_list:
            try:
                clicks = ad['clicks']
                impressions = ad['impressions']
                ad['CTR'] = float(clicks) /float(impressions)
            except Exception:
                ad['CTR'] = 0
            if ad['CTR'] > best_ad_performance:
                best_ad_performance = ad['CTR']
                best_ad_in_period = ad
        
        #Provide the ids and statistics of the best performing ad group and campaign for the given time
        from collections import defaultdict
        #create dict of camps that each include dict of groups that include list of ads
        #for example d['camp1']->['group1'],['group2']
        #d['camp1']->['group1']->{ad1,ad2,ad3}
        outerdict = defaultdict(lambda: defaultdict(list))
        for ad in ads_list:
            outerdict[ad['campaign']][ad['adGroupId']].append(ad)
        #check the best score
        best_group_scroe = 0
        best_score = 0
        best_result_group = None
        best_result_camp = None
        for camp in outerdict:
            for group in outerdict[camp]:
                group_sum = 0
                #calculate the score of all ads in group a and campaign b
                for ad in  outerdict[camp][group]:
                    group_sum +=ad['CTR']
                if group_sum > best_group_scroe:
                    best_group_scroe = group_sum
                    best_result_group = group
            if best_group_scroe > best_score:
                best_score = best_group_scroe
                best_result_camp = camp
        print "best result camp: " + best_result_camp
        print "best group id: " + best_result_group

        df = pd.DataFrame(columns=['date','impressions','clicks','cost'])
        i = 0
        for ad in outerdict[best_result_camp][best_result_group]:
            df.loc[i] = [ad['date'],ad['impressions'],ad['clicks'],ad['cost']]
            i +=1
        print df



```

    best result camp: #Albert_**[8327983]**_Current_campaign
    best group id: 1899689
               date impressions clicks                cost
    0    2016-10-22        6577   6419              42.095
    1    2016-10-30        3081    542               12.71
    2    2016-10-26        8148   1562  17.810000000000002
    3    2016-10-05         810    415              12.075
    4    2016-10-06         231     60                10.3
    5    2016-10-01         410    132               10.66
    6    2016-10-19        6232   1615              18.075
    7    2016-10-20        6608   2569              22.845
    8    2016-10-23         253     68               10.34
    9    2016-10-24        5803   1252  16.259999999999998
    10   2016-10-29        3922    339              11.695
    11   2016-10-01         618    547              12.735
    12   2016-10-16        5140   2823  24.115000000000002
    13   2016-10-03        1447    974  14.870000000000001
    14   2016-10-28       12265  11006               65.03
    15   2016-10-29        2291    836               14.18
    16   2016-10-11          79     66               10.33
    17   2016-10-15        2152   1428               17.14
    18   2016-10-05         702    690               13.45
    19   2016-10-14        9279   7964               49.82
    20   2016-10-17        5401   3188  25.939999999999998
    21   2016-10-04        1191   1032               15.16
    22   2016-10-30        3956   3742               28.71
    23   2016-10-07         934    886               14.43
    24   2016-10-29        6257   3188  25.939999999999998
    25   2016-10-14        7359   6562               42.81
    26   2016-10-11        1250    157              10.785
    27   2016-10-03         450    361              11.805
    28   2016-10-05        1283   1256               16.28
    29   2016-10-04        1129   1097              15.485
    ..          ...         ...    ...                 ...
    210  2016-10-22         620    576  12.879999999999999
    211  2016-10-24        5277   4733              33.665
    212  2016-10-16        2494   1364               16.82
    213  2016-10-20        2977    560                12.8
    214  2016-10-28        2254   1290               16.45
    215  2016-10-01         716    662               13.31
    216  2016-10-08        2277   1961              19.805
    217  2016-10-02         864    493              12.465
    218  2016-10-19        3886     --                  --
    219  2016-10-24        6004    964               14.82
    220  2016-10-25        1891   1076  15.379999999999999
    221  2016-10-14        2310   2216               21.08
    222  2016-10-22        4885   1503              17.515
    223  2016-10-25         243     --                  --
    224  2016-10-08        2793   1067              15.335
    225  2016-10-13        4075     31              10.155
    226  2016-10-22        4357   2313  21.564999999999998
    227  2016-10-28        4098   3233              26.165
    228  2016-10-30         782    737              13.685
    229  2016-10-12        2224    561              12.805
    230  2016-10-27        5829   5153              35.765
    231  2016-10-22        6534   2437  22.185000000000002
    232  2016-10-03        1418    867              14.335
    233  2016-10-30        8168   7889              49.445
    234  2016-10-03         822     --                  --
    235  2016-10-27        6161   4088               30.44
    236  2016-10-06         489    263              11.315
    237  2016-10-15        1002    539              12.695
    238  2016-10-12        2523   1356               16.78
    239  2016-10-11        1246    632               13.16
    
    [240 rows x 4 columns]
    

#### 4.For each ad group, state if it is in the lower quartile of its campaign in terms of impressions


```python
        #For each ad group, state if it is in the lower quartile of its campaign in terms of impressions
        groups = {}
        impressions_for_group = {}
        ad_group_id_result = {}
        for camp in outerdict:
            camp_impressions = 0
            for group in outerdict[camp]:
                group_impressions = 0
                #calculate the num of group impressions
                for ad in  outerdict[camp][group]:
                    group_impressions += int(ad['impressions'])
                    camp_impressions += int(ad['impressions'])
                impressions_for_group[group] = group_impressions

            for group in impressions_for_group:
                if impressions_for_group[group] < (camp_impressions / 4):
                    groups[group] = "lower"
                else:
                    groups[group] = "higer"
        
        
        #print the results
        print str(groups)

```

    {'5807362': 'lower', '8293668': 'lower', '1866565': 'higer', '8569794': 'higer', '4313194': 'higer', '4971442': 'lower', '6014739': 'lower', '3903713': 'higer', '4855135': 'lower', '3615100': 'higer', '4485830': 'lower', '5868614': 'higer', '7971631': 'higer', '2383411': 'lower', '9451923': 'higer', '7722033': 'higer', '8541554': 'lower', '2010461': 'lower', '3792257': 'lower', '4015172': 'higer', '4944523': 'higer', '9575470': 'lower', '4006933': 'higer', '7311131': 'lower', '9168766': 'lower', '4939747': 'higer', '6345811': 'higer', '6959614': 'lower', '7672563': 'higer', '2463253': 'lower', '6300436': 'higer', '9491413': 'higer', '3576949': 'higer', '4442461': 'higer', '2866165': 'higer', '4763817': 'higer', '4764110': 'higer', '3577787': 'lower', '5941016': 'lower', '8841866': 'higer', '3163353': 'lower', '7459969': 'higer', '1177231': 'lower', '2585424': 'higer', '9605519': 'higer', '3549150': 'lower', '2410919': 'higer', '2832875': 'higer', '7796774': 'higer', '9292440': 'lower', '5677471': 'higer', '8741505': 'lower', '8257023': 'lower', '6488442': 'higer', '8778230': 'higer', '3095322': 'higer', '5175939': 'higer', '2449071': 'higer', '1899689': 'higer', '8385118': 'lower', '3179271': 'higer', '5284053': 'higer', '4698902': 'higer', '4429509': 'lower', '7582227': 'higer', '6327620': 'lower', '8163940': 'higer', '8302218': 'lower', '8430359': 'higer', '3902573': 'higer', '3416165': 'higer', '5813436': 'lower', '4956049': 'lower', '7379622': 'higer', '3939385': 'higer', '4975245': 'lower', '4287974': 'lower', '3789344': 'higer', '2794197': 'higer', '3048169': 'higer', '4638799': 'higer', '5188263': 'higer', '4408005': 'higer', '3486363': 'higer', '9198695': 'higer', '1174996': 'lower', '7924778': 'higer', '8031715': 'higer', '1489318': 'lower', '5944683': 'lower', '8837791': 'higer', '5824565': 'higer', '9551915': 'higer', '5474141': 'lower', '3264884': 'higer', '8014850': 'higer', '4688329': 'higer', '4047866': 'higer', '6680145': 'lower', '1874413': 'higer', '2805337': 'higer', '1622823': 'higer', '9830440': 'higer', '4245589': 'higer', '2288812': 'higer', '5200888': 'higer', '2885804': 'higer', '1200893': 'higer', '5049780': 'lower', '3419063': 'higer', '4842318': 'higer', '5152640': 'lower', '5386927': 'higer', '1154125': 'lower', '8848686': 'lower', '8124925': 'higer', '6117972': 'higer', '8469876': 'lower', '9816779': 'higer', '4137722': 'higer', '8951273': 'lower', '5123061': 'lower', '6228142': 'higer', '6633057': 'lower', '3943837': 'lower', '5194661': 'higer', '1069535': 'higer', '9736636': 'lower', '9506390': 'lower', '7452900': 'higer', '5475294': 'lower', '2631343': 'lower', '6792441': 'lower', '1536304': 'higer', '3736390': 'higer', '9879071': 'lower', '3714450': 'lower', '9228053': 'lower', '5424344': 'lower', '3979814': 'higer', '8660897': 'lower', '3429400': 'higer', '9954073': 'higer', '3422129': 'lower', '9463970': 'higer', '6175985': 'lower', '7025720': 'higer', '5165908': 'higer', '4031885': 'lower', '2802729': 'higer', '8025166': 'lower', '4921971': 'higer', '7612319': 'lower', '1372466': 'higer', '5200260': 'higer', '1363173': 'lower', '2565352': 'lower', '6741507': 'higer', '9467087': 'lower', '7554473': 'lower', '4156678': 'lower', '1934499': 'higer', '4542110': 'lower', '1125634': 'lower', '1791538': 'lower', '4390227': 'lower', '9989555': 'lower', '6262873': 'higer', '5942799': 'lower', '9187421': 'higer', '5075451': 'higer', '9577834': 'lower', '3020291': 'higer', '5594366': 'lower', '8191415': 'lower', '1432606': 'higer', '5401841': 'lower', '3957866': 'lower', '2235236': 'higer', '2127071': 'lower', '8007878': 'higer', '5453287': 'lower', '2652087': 'lower', '4435726': 'lower', '4858877': 'higer', '9829701': 'lower', '8434792': 'higer', '6022513': 'lower', '6102965': 'lower', '8899367': 'higer', '7062934': 'lower', '5866085': 'higer', '7091824': 'lower', '2485831': 'lower', '7160069': 'higer', '2039299': 'lower', '8723647': 'lower', '1119945': 'lower', '9650298': 'higer', '2319724': 'lower', '7487205': 'higer', '3301863': 'higer', '4242437': 'higer', '2456166': 'higer', '9612043': 'higer', '9116416': 'higer', '7768270': 'higer', '7012252': 'lower', '5081707': 'higer', '8488646': 'lower', '8653523': 'higer', '4181364': 'higer', '7109304': 'higer', '3433304': 'higer', '8345364': 'lower', '7328398': 'higer', '4386257': 'lower', '7537766': 'higer', '4724646': 'lower', '8890195': 'lower', '4713214': 'higer', '5789874': 'higer', '1974993': 'higer', '6274736': 'lower', '6837235': 'higer', '3177419': 'higer', '5913822': 'lower', '3737325': 'lower', '3692407': 'lower', '1114350': 'higer', '3394234': 'higer', '1980772': 'lower', '9461148': 'lower', '8374019': 'lower', '3213323': 'higer', '8493281': 'lower', '3089264': 'higer', '5005861': 'higer', '8179300': 'lower', '4986077': 'lower', '5129507': 'lower', '1527239': 'lower', '2966028': 'higer', '4535846': 'lower', '4300783': 'lower', '2340139': 'lower', '9307897': 'lower', '1451398': 'lower', '7062368': 'higer', '2154589': 'lower', '6579772': 'lower', '1613520': 'lower', '8286734': 'higer', '9674289': 'lower', '8954266': 'higer', '9317823': 'lower', '3662151': 'lower', '8245782': 'higer', '1276217': 'higer', '9273730': 'higer', '8046998': 'higer', '9440344': 'higer', '7811335': 'higer', '5670784': 'lower', '7832932': 'lower', '9719546': 'lower', '1444921': 'higer', '2003113': 'higer', '9332987': 'higer', '6088312': 'lower', '6146419': 'higer', '8393514': 'higer', '1846944': 'lower', '7866794': 'higer', '5902875': 'higer', '9945123': 'higer', '5933581': 'higer', '1833167': 'higer', '1930357': 'higer', '5975079': 'higer', '9730242': 'higer', '1294384': 'higer', '8811363': 'higer', '9521780': 'higer', '9518604': 'lower', '3116275': 'lower', '1221066': 'higer', '1530388': 'higer', '3498900': 'higer', '8026482': 'higer', '3814914': 'lower', '9599676': 'higer', '8471725': 'lower', '8369278': 'higer', '7737941': 'higer', '8628618': 'lower', '4580071': 'higer', '7198390': 'lower', '2497550': 'higer', '1051479': 'higer', '4800207': 'lower', '3208340': 'higer', '9820563': 'higer', '5947450': 'lower', '4940610': 'higer', '9715008': 'lower', '2726335': 'higer', '9454366': 'higer', '2972117': 'higer', '1473984': 'lower', '8920191': 'higer', '5639223': 'higer', '3804489': 'lower', '5089982': 'higer', '6369462': 'higer', '7127383': 'higer', '7775816': 'lower', '6415458': 'higer', '6788815': 'higer', '4362846': 'higer', '4085120': 'lower', '7638799': 'lower', '3452660': 'lower', '9855139': 'higer', '8240096': 'higer', '6197149': 'lower', '6027135': 'lower', '4967500': 'higer', '3709177': 'higer', '5151780': 'higer', '9864183': 'higer', '6937897': 'lower', '7322776': 'higer', '8476363': 'lower', '9409750': 'lower', '1654669': 'lower', '7678273': 'higer', '5051924': 'lower', '9783082': 'lower', '2045520': 'lower', '3970959': 'lower', '3637365': 'lower', '4250434': 'higer', '3745262': 'lower', '9732274': 'higer', '2734711': 'higer', '7438484': 'higer', '7297024': 'higer', '5577103': 'higer', '5077594': 'higer', '5043242': 'higer', '3513344': 'lower', '8798834': 'lower', '2236553': 'higer', '5978861': 'higer', '8964601': 'higer', '5111050': 'lower', '3779317': 'lower', '3679925': 'lower', '2889236': 'lower', '7692546': 'higer', '1146974': 'higer', '3011710': 'higer', '1428234': 'higer', '2114510': 'higer', '3292821': 'lower', '1413521': 'lower', '6208456': 'higer', '5048086': 'lower', '1226462': 'lower', '4297163': 'higer', '5954685': 'higer', '4090832': 'higer', '7775695': 'lower', '4460555': 'higer', '2355699': 'higer', '4142892': 'lower', '1159774': 'lower', '3436333': 'lower', '5960024': 'lower', '1774209': 'higer', '7033738': 'higer', '2148679': 'higer', '3233227': 'lower', '6665807': 'lower', '4030177': 'lower', '5456200': 'lower', '5560641': 'lower', '3054649': 'higer', '3643296': 'lower', '4246427': 'higer', '7731367': 'higer', '4285753': 'lower', '4123372': 'higer', '1043138': 'higer', '2014703': 'lower', '9225532': 'lower', '4048508': 'lower', '1434770': 'higer', '7689957': 'lower', '8149013': 'higer', '3671741': 'lower', '4927068': 'lower', '5760458': 'lower', '8926691': 'lower', '4289840': 'lower', '8566493': 'lower', '4713417': 'higer', '5327832': 'higer', '9442954': 'lower', '6293783': 'higer', '2942783': 'lower', '7645694': 'lower', '3555115': 'lower', '2845171': 'higer', '7499424': 'lower', '9712245': 'higer', '4888444': 'lower', '3752877': 'higer', '7393287': 'lower', '2183268': 'higer', '6864353': 'lower', '4381338': 'higer', '1943239': 'lower', '3905191': 'lower', '9335959': 'higer', '5054658': 'lower', '7719701': 'higer', '8352632': 'lower', '4758398': 'higer', '9361782': 'higer', '8691736': 'higer', '7928023': 'higer', '3778595': 'lower', '6259763': 'higer', '1135791': 'lower', '4894125': 'lower', '6343998': 'lower', '5038559': 'higer', '7579342': 'lower', '8666333': 'lower', '5613437': 'lower', '2254104': 'lower', '6991060': 'lower', '6977738': 'higer', '9358628': 'lower', '5372581': 'higer', '8844321': 'higer', '6162419': 'lower', '6033675': 'lower', '1658261': 'lower', '1305669': 'higer', '9330990': 'higer', '3559042': 'lower', '5168537': 'lower', '4709772': 'lower', '5188951': 'lower', '8633185': 'higer', '1640929': 'higer', '3987251': 'lower', '3142294': 'higer', '8918071': 'lower', '6466722': 'higer', '7105438': 'higer', '5352858': 'lower', '8336085': 'higer', '4287549': 'higer', '6272339': 'lower', '2817498': 'lower', '5593428': 'higer', '5889724': 'lower', '1913778': 'higer', '9049931': 'lower', '3913362': 'lower', '9184941': 'lower', '8294544': 'lower', '7637821': 'higer', '9156733': 'higer', '9341013': 'higer', '2834727': 'higer', '3448866': 'higer', '5906956': 'lower', '3873101': 'higer', '8982889': 'higer', '7968968': 'higer', '1818703': 'higer', '6254022': 'lower', '5816860': 'higer', '8260076': 'higer', '8778462': 'higer', '1211991': 'lower', '4869296': 'lower', '8691268': 'lower', '6371596': 'higer', '7303458': 'higer', '7136842': 'lower', '3217616': 'higer', '6991877': 'higer', '8198550': 'higer', '7385173': 'higer'}
    

#### 5.Organize the ad groups by the following logic


```python
#Organize the ad groups by the following logic
contain_the_best_ad = {}
contain_both_components = {}
contain_only_one_comp = {}
contain_no_component = {}

groups = {}

for ad in ads_list:
    groups[ad['adGroupId']] = []
for ad in ads_list:
    groups[ad['adGroupId']].append(ad)

for group in groups:
    flag_headLine_comp = 0
    flag_bodyText_comp = 0
    flag_best = 0
    #calculate the num of group impressions
    for ad in  groups[group]:
        if ad['headLine'] == best_ad_in_period['headLine'] and ad['bodyText'] == best_ad_in_period['bodyText']:
            contain_the_best_ad[group] =group
            flag_best = 1
            break
        if  ad['headLine'] == best_ad_in_period['headLine']:
            flag_headLine_comp = 1
        if  ad['bodyText'] == best_ad_in_period['bodyText']:
            flag_bodyText_comp = 1
        if flag_headLine_comp == 1 and flag_bodyText_comp ==1:
            contain_both_components[group] = group
            break

    if (flag_headLine_comp and not flag_bodyText_comp) or (not flag_headLine_comp and flag_bodyText_comp):
            contain_only_one_comp[group] = group
    if (flag_headLine_comp == 0) and (flag_bodyText_comp == 0) and (flag_best == 0):
        contain_no_component[group] = group
        
print "All the ad groups that contain the best performing ad :"
print str(contain_the_best_ad)


print "All the ad groups that contain both components - not from the same ad :"
print str(contain_both_components)


print "All the ad groups that contain only one component of the best performing ad :"
print str(contain_only_one_comp)


print "All the ad groups that contain no component of the best performing ad :"
print str(contain_no_component)

```

    All the ad groups that contain the best performing ad :
    {'4142892': '4142892', '8286734': '8286734', '9273730': '9273730', '5123061': '5123061', '7033738': '7033738', '6665807': '6665807', '5868614': '5868614', '8245782': '8245782', '8541554': '8541554', '4246427': '4246427', '7924778': '7924778', '4285753': '4285753', '4123372': '4123372', '9575470': '9575470', '9463970': '9463970', '6345811': '6345811', '5760458': '5760458', '2802729': '2802729', '6300436': '6300436', '9491413': '9491413', '5200260': '5200260', '9358628': '9358628', '3576949': '3576949', '6959614': '6959614', '3814914': '3814914', '9467087': '9467087', '4156678': '4156678', '3163353': '3163353', '3752877': '3752877', '3792257': '3792257', '4381338': '4381338', '2832875': '2832875', '6262873': '6262873', '3208340': '3208340', '5175939': '5175939', '2726335': '2726335', '5284053': '5284053', '4429509': '4429509', '2631343': '2631343', '7452900': '7452900', '8294544': '8294544', '3736390': '3736390', '6175985': '6175985', '7379622': '7379622', '3939385': '3939385', '6991060': '6991060', '6788815': '6788815', '5372581': '5372581', '4085120': '4085120', '8240096': '8240096', '9518604': '9518604', '7062934': '7062934', '4709772': '4709772', '2485831': '2485831', '5151780': '5151780', '9864183': '9864183', '8633185': '8633185', '8723647': '8723647', '3448866': '3448866', '2010461': '2010461', '6741507': '6741507', '5593428': '5593428', '2045520': '2045520', '7731367': '7731367', '4763817': '4763817', '5824565': '5824565', '9551915': '9551915', '5474141': '5474141', '4688329': '4688329', '7637821': '7637821', '2805337': '2805337', '1974993': '1974993', '6274736': '6274736', '6837235': '6837235', '7968968': '7968968', '2889236': '2889236', '4245589': '4245589', '8149013': '8149013', '7499424': '7499424', '3292821': '3292821', '3419063': '3419063', '7303458': '7303458', '7109304': '7109304', '2966028': '2966028', '4090832': '4090832', '7385173': '7385173', '8691268': '8691268', '1613520': '1613520'}
    All the ad groups that contain both components - not from the same ad :
    {'1866565': '1866565', '8569794': '8569794', '8951273': '8951273', '9674289': '9674289', '6228142': '6228142', '1774209': '1774209', '4971442': '4971442', '7866794': '7866794', '3943837': '3943837', '2148679': '2148679', '4869296': '4869296', '3233227': '3233227', '3662151': '3662151', '6488442': '6488442', '4030177': '4030177', '6792441': '6792441', '1536304': '1536304', '3643296': '3643296', '9440344': '9440344', '5670784': '5670784', '4015172': '4015172', '9228053': '9228053', '2003113': '2003113', '7775816': '7775816', '9954073': '9954073', '7311131': '7311131', '9168766': '9168766', '1846944': '1846944', '5902875': '5902875', '3671741': '3671741', '1276217': '1276217', '4927068': '4927068', '4031885': '4031885', '8926691': '8926691', '1930357': '1930357', '4289840': '4289840', '7672563': '7672563', '7612319': '7612319', '1372466': '1372466', '3559042': '3559042', '4442461': '4442461', '2866165': '2866165', '1221066': '1221066', '2942783': '2942783', '8026482': '8026482', '4764110': '4764110', '3555115': '3555115', '3577787': '3577787', '9599676': '9599676', '5941016': '5941016', '7737941': '7737941', '7459969': '7459969', '1177231': '1177231', '8046998': '8046998', '9605519': '9605519', '2410919': '2410919', '1791538': '1791538', '4390227': '4390227', '2497550': '2497550', '4580071': '4580071', '8257023': '8257023', '7438484': '7438484', '1051479': '1051479', '7719701': '7719701', '8778230': '8778230', '8982889': '8982889', '9577834': '9577834', '6327620': '6327620', '8691736': '8691736', '7928023': '7928023', '9715008': '9715008', '1432606': '1432606', '9454366': '9454366', '6259763': '6259763', '1294384': '1294384', '2235236': '2235236', '6343998': '6343998', '5038559': '5038559', '5089982': '5089982', '5453287': '5453287', '3416165': '3416165', '7579342': '7579342', '4858877': '4858877', '3422129': '3422129', '7136842': '7136842', '4287974': '4287974', '3789344': '3789344', '2383411': '2383411', '7638799': '7638799', '8844321': '8844321', '9855139': '9855139', '1305669': '1305669', '4638799': '4638799', '5188951': '5188951', '5188263': '5188263', '5866085': '5866085', '5168537': '5168537', '3709177': '3709177', '9330990': '9330990', '3486363': '3486363', '3987251': '3987251', '8476363': '8476363', '9409750': '9409750', '1654669': '1654669', '1114350': '1114350', '8031715': '8031715', '3301863': '3301863', '4242437': '4242437', '8336085': '8336085', '6272339': '6272339', '2817498': '2817498', '5081707': '5081707', '5944683': '5944683', '4181364': '4181364', '1530388': '1530388', '1913778': '1913778', '9732274': '9732274', '7328398': '7328398', '8014850': '8014850', '5077594': '5077594', '5043242': '5043242', '7537766': '7537766', '6680145': '6680145', '2114510': '2114510', '9156733': '9156733', '1874413': '1874413', '2236553': '2236553', '9341013': '9341013', '5111050': '5111050', '8964601': '8964601', '9830440': '9830440', '3779317': '3779317', '3679925': '3679925', '3177419': '3177419', '5913822': '5913822', '7692546': '7692546', '3011710': '3011710', '8260076': '8260076', '3394234': '3394234', '9461148': '9461148', '8471725': '8471725', '8920191': '8920191', '3213323': '3213323', '1200893': '1200893', '8163940': '8163940', '5049780': '5049780', '4842318': '4842318', '5005861': '5005861', '8179300': '8179300', '4986077': '4986077', '9712245': '9712245', '5129507': '5129507', '5152640': '5152640', '3217616': '3217616', '1527239': '1527239', '1226462': '1226462', '4297163': '4297163', '8848686': '8848686', '6146419': '6146419', '8198550': '8198550', '6117972': '6117972', '3902573': '3902573', '8469876': '8469876', '2355699': '2355699'}
    All the ad groups that contain only one component of the best performing ad :
    {'4142892': '4142892', '4855135': '4855135', '3615100': '3615100', '4313194': '4313194', '3903713': '3903713', '9317823': '9317823', '5194661': '5194661', '1069535': '1069535', '4137722': '4137722', '8741505': '8741505', '5475294': '5475294', '4287549': '4287549', '8245782': '8245782', '5560641': '5560641', '7971631': '7971631', '3054649': '3054649', '5075451': '5075451', '3736390': '3736390', '9879071': '9879071', '4246427': '4246427', '8007878': '8007878', '3714450': '3714450', '4944523': '4944523', '9719546': '9719546', '1444921': '1444921', '1640929': '1640929', '9332987': '9332987', '5424344': '5424344', '3979814': '3979814', '8660897': '8660897', '3429400': '3429400', '1043138': '1043138', '8393514': '8393514', '9463970': '9463970', '4939747': '4939747', '6345811': '6345811', '1434770': '1434770', '1211991': '1211991', '8374019': '8374019', '2014703': '2014703', '5165908': '5165908', '9829701': '9829701', '6088312': '6088312', '5760458': '5760458', '2802729': '2802729', '8025166': '8025166', '4921971': '4921971', '2463253': '2463253', '5975079': '5975079', '6300436': '6300436', '9730242': '9730242', '9945123': '9945123', '8811363': '8811363', '4713417': '4713417', '9521780': '9521780', '9358628': '9358628', '3576949': '3576949', '1363173': '1363173', '2565352': '2565352', '3116275': '3116275', '6293783': '6293783', '7105438': '7105438', '4250434': '4250434', '3498900': '3498900', '9467087': '9467087', '7554473': '7554473', '5372581': '5372581', '2845171': '2845171', '8666333': '8666333', '8345364': '8345364', '8369278': '8369278', '1934499': '1934499', '7198390': '7198390', '4888444': '4888444', '4542110': '4542110', '7393287': '7393287', '2585424': '2585424', '9506390': '9506390', '7796774': '7796774', '6162419': '6162419', '9989555': '9989555', '5677471': '5677471', '6665807': '6665807', '5942799': '5942799', '8493281': '8493281', '1159774': '1159774', '3095322': '3095322', '4758398': '4758398', '9820563': '9820563', '1899689': '1899689', '4940610': '4940610', '7127383': '7127383', '8385118': '8385118', '3179271': '3179271', '5594366': '5594366', '8191415': '8191415', '2726335': '2726335', '5284053': '5284053', '2972117': '2972117', '4429509': '4429509', '1135791': '1135791', '5639223': '5639223', '7499424': '7499424', '8430359': '8430359', '4460555': '4460555', '6027135': '6027135', '2652087': '2652087', '4435726': '4435726', '4956049': '4956049', '8841866': '8841866', '5613437': '5613437', '9225532': '9225532', '6415458': '6415458', '3939385': '3939385', '6977738': '6977738', '6788815': '6788815', '8434792': '8434792', '9361782': '9361782', '2794197': '2794197', '3452660': '3452660', '6022513': '6022513', '6033675': '6033675', '8240096': '8240096', '9518604': '9518604', '6197149': '6197149', '3448866': '3448866', '3048169': '3048169', '8899367': '8899367', '4408005': '4408005', '4967500': '4967500', '4709772': '4709772', '2485831': '2485831', '5151780': '5151780', '7160069': '7160069', '6937897': '6937897', '2039299': '2039299', '8633185': '8633185', '9442954': '9442954', '3913362': '3913362', '9650298': '9650298', '7678273': '7678273', '1174996': '1174996', '3142294': '3142294', '7731367': '7731367', '8918071': '8918071', '6466722': '6466722', '7487205': '7487205', '5352858': '5352858', '2456166': '2456166', '9612043': '9612043', '9116416': '9116416', '7768270': '7768270', '5051924': '5051924', '9783082': '9783082', '7832932': '7832932', '7811335': '7811335', '8653523': '8653523', '8837791': '8837791', '3433304': '3433304', '9551915': '9551915', '3745262': '3745262', '2734711': '2734711', '3264884': '3264884', '5577103': '5577103', '4386257': '4386257', '3513344': '3513344', '4688329': '4688329', '4047866': '4047866', '4724646': '4724646', '8890195': '8890195', '5327832': '5327832', '8798834': '8798834', '2805337': '2805337', '7025720': '7025720', '4713214': '4713214', '5789874': '5789874', '6274736': '6274736', '3873101': '3873101', '7968968': '7968968', '5816860': '5816860', '4245589': '4245589', '4048508': '4048508', '5054658': '5054658', '1428234': '1428234', '5200888': '5200888', '2885804': '2885804', '8149013': '8149013', '4156678': '4156678', '3089264': '3089264', '3292821': '3292821', '3419063': '3419063', '6208456': '6208456', '5048086': '5048086', '6579772': '6579772', '1154125': '1154125', '5933581': '5933581', '5954685': '5954685', '8124925': '8124925', '6991877': '6991877', '4300783': '4300783', '3804489': '3804489', '7385173': '7385173', '1451398': '1451398', '7062368': '7062368', '9816779': '9816779'}
    All the ad groups that contain no component of the best performing ad :
    {'5807362': '5807362', '8293668': '8293668', '4975245': '4975245', '4362846': '4362846', '3020291': '3020291', '1943239': '1943239', '9451923': '9451923', '5813436': '5813436', '1119945': '1119945', '2254104': '2254104', '1622823': '1622823', '6014739': '6014739', '2834727': '2834727', '5978861': '5978861', '7645694': '7645694', '9736636': '9736636', '8954266': '8954266', '9049931': '9049931', '6102965': '6102965', '5906956': '5906956', '1658261': '1658261', '4485830': '4485830', '6254022': '6254022', '3737325': '3737325', '8302218': '8302218', '5456200': '5456200', '8566493': '8566493', '1146974': '1146974', '9307897': '9307897', '3692407': '3692407', '1125634': '1125634', '7091824': '7091824', '3436333': '3436333', '2288812': '2288812', '7722033': '7722033', '6864353': '6864353', '3549150': '3549150', '5960024': '5960024', '1980772': '1980772', '8488646': '8488646', '2154589': '2154589', '9198695': '9198695', '7322776': '7322776', '3905191': '3905191', '9335959': '9335959', '7689957': '7689957', '9292440': '9292440', '2183268': '2183268', '4006933': '4006933', '3778595': '3778595', '1413521': '1413521', '2319724': '2319724', '6371596': '6371596', '4800207': '4800207', '9187421': '9187421', '8352632': '8352632', '1818703': '1818703', '4894125': '4894125', '2449071': '2449071', '8778462': '8778462', '5947450': '5947450', '5386927': '5386927', '8628618': '8628618', '1489318': '1489318', '7012252': '7012252', '6633057': '6633057', '6369462': '6369462', '4535846': '4535846', '4698902': '4698902', '3637365': '3637365', '1473984': '1473984', '5889724': '5889724', '2340139': '2340139', '7582227': '7582227', '3957866': '3957866', '1833167': '1833167', '2127071': '2127071', '7297024': '7297024', '9184941': '9184941', '3970959': '3970959', '5401841': '5401841', '7775695': '7775695'}
    

#### Given that the budget is spread equally on all the campaigns and ad groups, and
#### based on your findings, how would you optimize the performance of the campaigns?
#### (Exploration) Explore the data and try to come up with a new and interesting insight, write a short
I want to check if there is connection between the length of the ad (headLine and bodyText) to the performance to the ad.

```python
%matplotlib inline
import collections

ctr_to_len = {}
sum_of_len = 0
for ad in ads_list:
    ctr_to_len[ad['CTR']]  = len(ad['headLine']) + len(ad['bodyText'])
    sum_of_len += len(ad['headLine'])+ len(ad['bodyText'])
# print len_to_succeed
ave_len = sum_of_len / len(ctr_to_len)

print "average len of ad(headLine + bodyText): " + str(ave_len)
od = collections.OrderedDict(sorted(ctr_to_len.items(), reverse=True))
i = 0
print "TOP 5"
for ctr in od:
    if i < 5:
        print str(ctr) + "," + str(od[ctr])
    else:
        break
    i+=1
    
horizontalData = []
verticalData = []
import pandas as pd
df = pd.DataFrame(columns=['performance'])
i = 0
for ctr in ctr_to_len:
    if i < 5:
        horizontalData.append(ctr)
        verticalData.append(od[ctr])
    else:
        break
    i += 1


    
plt.plot(verticalData, horizontalData)
plt.ylabel('Len-CTR Graph')
plt.show()

```

    average len of ad(headLine + bodyText): 60
    TOP 5
    1.0,46
    0.999891880203,34
    0.999852354939,53
    0.999832831829,45
    0.999811391928,57
    


![png](output_13_1.png)

My conclusion is that in order to increase the performance you can shorter the length of the ad to average length and get better results
#### Explore the data and try to come up with a new and interesting insight, write a short
#### description on what you looked for and how
Does money matter?
I want to check if there is connection between the cost of the ad to performance?

```python
%matplotlib inline

new_dict = {}
ctr_arr = []
sum_of_len = 0
for ad in ads_list:
    new_dict[ad['cost']] = ad['CTR']

import collections
import matplotlib.pyplot as plt
od = collections.OrderedDict(sorted(new_dict.items(), reverse=True))
verticalData = []
horizontalData = []
i = 0
for ctr in od:
    if i < 5000:
        horizontalData.append(od[ctr])
        verticalData.append(ctr)
    else:
        break
    i += 1

plt.plot(verticalData, horizontalData, 'ro')
plt.ylabel('Cost-Score Graph')
plt.show()


```


![png](output_17_0.png)

The answer to the question is not unequivocal...on the one hand there are with low cost that have high performance but on the other hand we can see that most of all the ads with the high cost have high performance. so if I have 1 chance I would pay more to get best result