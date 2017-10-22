import csv
import numpy as np
import collections

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

        print "The best performing ad of the given time period - "
        print best_ad_in_period

        #Find the best performing ad of each day within the time period.
        #create dict of days , for each day will be list of ads of this day
        #for example: ads_per_day['10.10.2016'] = {ad1,ad2,ad3}

        day = {}
        ads_per_day_dict = {}
        #create dict of empty lists
        ads_per_day_dict = dict((ad['date'], []) for ad in ads_list)
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
        print "Provide the ids and statistics of the best performing ad group and campaign for the given time"
        print best_result_camp
        print best_result_group

        df = pd.DataFrame(columns=['campaign','adGroupId','date','headLine','bodyText','impressions','clicks','cost'])
        i = 0
        for ad in outerdict[best_result_camp][best_result_group]:
            df.loc[i,'campaign'] = ad['campaign']
            df.loc[i,'adGroupId'] = ad['adGroupId']
            df.loc[i,'date'] = ad['date']
            df.loc[i,'headLine'] = ad['headLine']
            df.loc[i,'bodyText'] = ad['bodyText']
            df.loc[i,'impressions'] = ad['impressions']
            df.loc[i,'clicks'] = ad['clicks']
            df.loc[i,'cost'] = ad['cost']
            i +=1
        print df

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
        for group in groups:
            print group + "-> " + groups[group]


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
        for group in contain_the_best_ad:
            print group


        print "All the ad groups that contain both components - not from the same ad :"
        for group in contain_both_components:
            print group


        print "All the ad groups that contain only one component of the best performing ad :"
        for group in contain_only_one_comp:
            print group


        print "All the ad groups that contain no component of the best performing ad :"
        for group in contain_no_component:
            print group


        ctr_to_len = {}
        sum_of_len = 0
        for ad in ads_list:
            ctr_to_len[ad['CTR']]  = len(ad['headLine']) + len(ad['bodyText'])
            sum_of_len += len(ad['headLine'])+ len(ad['bodyText'])
        # print len_to_succeed
        ave_len = sum_of_len / len(ctr_to_len)

        import pandas as pd
        df = pd.DataFrame(columns=['performance'])
        i = 0
        for ctr in ctr_to_len:
            df.loc[ctr_to_len[ctr]] = ctr
            i +=1
        print df

        print "average len of ad(headLine + bodyText): " + str(ave_len)
        od = collections.OrderedDict(sorted(ctr_to_len.items(), reverse=True))
        i = 0
        for ctr in od:
            if i < 5:
                print str(ctr) + "," + str(od[ctr])
            else:
                break
            i+=1

        df.plot()


        new_dict = {}
        ctr_arr = []
        sum_of_len = 0
        for ad in ads_list:
            new_dict[ad['cost']] = ad['CTR']

        import collections
        import matplotlib.pyplot as plt
        od = collections.OrderedDict(sorted(new_dict.items(), reverse=True))
        print od
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
        plt.ylabel('SuperFunny Graph')
        plt.show()
