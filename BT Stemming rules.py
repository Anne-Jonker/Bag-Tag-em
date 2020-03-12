import pandas as pd


klinker = set(['a', 'e', 'o'])
special_klinker = set(['i', 'u'])
 



def REST_Stemmer(REST_data):
    REST_data['Final stem rest'] = REST_data['Word']
    REST_data = REST_data.drop(['BT tag', 'BT stem'], axis=1)

    return(REST_Stemmer)
    
def BVNW_stemmer(BVNW_data):
    
    BVNW_data['BT stem'] = BVNW_data['Word']
    
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('er'), 'BT stem'] = BVNW_data['BT stem'].str[:-2]    
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('ste'), 'BT stem'] = BVNW_data['BT stem'].str[:-3]
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('ende'), 'BT stem'] = BVNW_data['BT stem'].str[:-4]
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('en'), 'BT stem'] = BVNW_data['BT stem'].str[:-2]
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('e'), 'BT stem'] = BVNW_data['BT stem'].str[:-1]
    
    
    # 'False' f and s
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('v'), 'BT stem'] = BVNW_data['BT stem'].str.replace('v','f',-1)
    BVNW_data.loc[BVNW_data['BT stem'].str.endswith('z'), 'BT stem'] = BVNW_data['BT stem'].str.replace('z','s',-1)

#    # Doubling of  a,e,o,u
    BVNW_data.loc[BVNW_data['BT stem'].str[-2].str.match('a') & (~BVNW_data['BT stem'].str[-3].isin(klinker)) & (~BVNW_data['BT stem'].str.endswith('r')), 'BT stem'] = BVNW_data['BT stem'].str.replace('a','aa',-1)
    BVNW_data.loc[BVNW_data['BT stem'].str[-2].str.match('e') & (~BVNW_data['BT stem'].str[-3].isin(klinker)) & (~BVNW_data['BT stem'].str.endswith('r')), 'BT stem'] = BVNW_data['BT stem'].str.replace('e','ee',-1)
    BVNW_data.loc[BVNW_data['BT stem'].str[-2].str.match('o') & (~BVNW_data['BT stem'].str[-3].isin(klinker)) & (~BVNW_data['BT stem'].str.endswith('r')), 'BT stem'] = BVNW_data['BT stem'].str.replace('o','oo',-1)
    BVNW_data.loc[BVNW_data['BT stem'].str[-2].str.match('u') & (~BVNW_data['BT stem'].str[-3].isin(klinker)) & (~BVNW_data['BT stem'].str[-3].isin(special_klinker)), 'BT stem'] = BVNW_data['BT stem'].str.replace('u','uu',-1)

#    # double letter at the end
    BVNW_data.loc[BVNW_data['BT stem'].str[-1] == BVNW_data['BT stem'].str[-2], 'BT stem'] = BVNW_data['BT stem'].str[:-1]


    BVNW_data['Final stem BVNW'] = BVNW_data['BT stem']
        
    BVNW_data = BVNW_data.drop(['BT tag','BT stem'], axis=1)

    return(BVNW_data)
    

def ZNW_Stemmer(ZNW_data):
    
        # Preparing the data

        ZNW_data['BT stem'] = ZNW_data['Word']
        ZNW_data['BT tag getal v2'] = 'ev'
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('en'), 'BT tag getal v2'] = ZNW_data['BT tag getal v2'].replace('ev', 'mv')
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('jes'), 'BT tag getal v2'] = ZNW_data['BT tag getal v2'].replace('ev', 'mv')
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('s'), 'BT tag getal v2'] = ZNW_data['BT tag getal v2'].replace('ev', 'mv')

        
        # For now assume that a ZNW in ev is already final stem 
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('en') & (ZNW_data['BT tag getal v2'].str.match('mv')), 'BT stem'] = ZNW_data['BT stem'].str[:-2]
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('jes') & (ZNW_data['BT tag getal v2'].str.match('mv')), 'BT stem'] = ZNW_data['BT stem'].str[:-3]
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('jes') & (ZNW_data['BT tag getal v2'].str.match('mv')), 'BT stem'] = ZNW_data['BT stem'].str[:-1]

        
        #'False' f and s
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('v') & (ZNW_data['BT tag getal v2'].str.match('mv')), 'BT stem'] = ZNW_data['BT stem'].str.replace('v','f',-1)
        ZNW_data.loc[ZNW_data['BT stem'].str.endswith('z') & (ZNW_data['BT tag getal v2'].str.match('mv')), 'BT stem'] = ZNW_data['BT stem'].str.replace('z','s',-1)
        
        # double letter at the end
        ZNW_data.loc[ZNW_data['BT stem'].str[-1] == ZNW_data['BT stem'].str[-2], 'BT stem'] = ZNW_data['BT stem'].str[:-1]


        ZNW_data['Final stem ZNW'] = ZNW_data['BT stem']
        
        ZNW_data = ZNW_data.drop(['BT tag','BT stem', 'BT tag getal v2'], axis=1)
        
        return(ZNW_data)


def WW_Stemmer(WW_data):
    
    # Preparing the data
    WW_data['FirstChars'] = [x[:3] for x in WW_data['Word']]
    WW_data['Samenstelling'] = pd.np.where(WW_data.FirstChars.str.match("aan"), "aan",
                   pd.np.where(WW_data.FirstChars.str.match("af"), "af",
                   pd.np.where(WW_data.FirstChars.str.match("bij"), "bij",
                   pd.np.where(WW_data.FirstChars.str.match("in"), "in", 
                   pd.np.where(WW_data.FirstChars.str.match("op"), "op",
                   pd.np.where(WW_data.FirstChars.str.match("uit"), "uit",""))))))    
    WW_data['Process'] = [e.replace(k, '',1) for e, k in zip(WW_data.Word.astype('str'), WW_data.Samenstelling.astype('str'))]
    WW_data = WW_data.drop(['FirstChars'], axis=1)
    irregular = pd.read_excel('Exception list location')
    WW_data = pd.merge(WW_data, irregular, on='Process', how= 'left')
    WW_data['BT Irregular'] = 1
    WW_data['Irregular Stem'] = WW_data['Irregular Stem'].fillna(' ')
    WW_data.loc[WW_data['Irregular Stem'].str.contains(' '), 'BT Irregular'] = WW_data['BT Irregular'].replace(1, 0)
    WW_data['BT stem'] = WW_data['Process']
    WW_data['BT tag getal v2'] = 'ev'
    
    
    # To ensure BVNW is seen as mv
    WW_data.loc[WW_data['BT stem'].str.endswith('en'), 'BT tag getal v2'] = WW_data['BT tag getal v2'].replace('ev', 'mv')


# VTT/ VVT
    WW_data.loc[WW_data['BT tag'].str.match('vtt') & (WW_data['BT stem'].str.startswith('ge')), 'BT stem'] = WW_data['BT stem'].str[2:]
    WW_data.loc[WW_data['BT tag'].str.match('vtt') & (WW_data['BT stem'].str.endswith('d')), 'BT stem'] = WW_data['BT stem'].str[:1]



# GENERAL (OTT)
    
    # Remove -en but ensure lentgh is at least 3 chars long
    WW_data.loc[WW_data['BT stem'].str.endswith('en') & (WW_data['BT stem'].str.len() > 3), 'BT stem'] = WW_data['BT stem'].str[:-2]
    # Converts ovt ev to ott ev
    WW_data.loc[WW_data['BT tag'].str.match('ovt') & (WW_data['BT stem'].str.endswith('e')) & (WW_data['BT stem'].str.len() > 3), 'BT stem'] = WW_data['BT stem'].str[:-1]
    # Remove t after dt
    WW_data.loc[WW_data['BT stem'].str.endswith('t') & (WW_data['BT stem'].str[-2] == 'd'), 'BT stem'] = WW_data['BT stem'].str[:-1]
    # If not irregular remove t at the end
    WW_data.loc[WW_data['BT stem'].str.endswith('t') & (WW_data['BT Irregular'] == 0)  & (~WW_data['BT stem'].str[-2].isin(klinker)), 'BT stem'] = WW_data['BT stem'].str[:-1]
    # 'False' s and f
    WW_data.loc[WW_data['BT stem'].str.endswith('v'), 'BT stem'] = WW_data['BT stem'].str.replace('v','f',-1)
    WW_data.loc[WW_data['BT stem'].str.endswith('z'), 'BT stem'] = WW_data['BT stem'].str.replace('z','s',-1)
    
    
    #        Doubling of vowels
    WW_data.loc[WW_data['BT stem'].str[-2].isin(klinker) & (~WW_data['BT stem'].str[-3].isin(klinker)) & (WW_data['BT tag getal v2'].str.match('mv')) & (WW_data['BT stem'].str[-2].str.match('a')), 'BT stem'] = WW_data['BT stem'].str.replace('a','aa',-1)
    WW_data.loc[WW_data['BT stem'].str[-2].isin(klinker) & (~WW_data['BT stem'].str[-3].isin(klinker)) & (WW_data['BT tag getal v2'].str.match('mv')) & (WW_data['BT stem'].str[-2].str.match('e')), 'BT stem'] = WW_data['BT stem'].str.replace('e','ee',-1)
    WW_data.loc[WW_data['BT stem'].str[-2].isin(klinker) & (~WW_data['BT stem'].str[-3].isin(klinker)) & (WW_data['BT tag getal v2'].str.match('mv')) & (WW_data['BT stem'].str[-2].str.match('o')), 'BT stem'] = WW_data['BT stem'].str.replace('o','oo',-1)

  
#    This is for correcting the double letters (Becarefull for slee)
    WW_data.loc[WW_data['BT stem'].str[-1] == WW_data['BT stem'].str[-2], 'BT stem'] = WW_data['BT stem'].str[:-1]
   
#    This is for handling irregular verbs
    WW_data.loc[WW_data['BT Irregular'] == 1, 'BT stem'] = WW_data['Irregular Stem']

#    This is for finalising the stem
    WW_data['Final stem WW'] = WW_data['Samenstelling'].fillna('') + WW_data['BT stem']
    
    WW_data = WW_data.drop(['BT tag', 'BT stem', 'Samenstelling', 'Process', 'Irregular Stem', 'BT Irregular', 'BT tag getal v2'], axis=1)

    return(WW_data)
    
	
def Finalise(WW_data, BVNW_data, ZNW_data, REST_data):
    data = pd.DataFrame()
    WW = WW_data
    BVNW = BVNW_data
    ZNW = ZNW_data
    REST = REST_data
    
    data = WW
    data = pd.merge(data, ZNW, on='Word', how='left')
    data = pd.merge(data, BVNW, on='Word', how='left')
    data = pd.merge(data, REST, on='Word', how='left')

    
    data['BT'] = data['Final stem WW'].fillna('') + data['Final stem ZNW'].fillna('') + data['Final stem rest'].fillna('') + data['Final stem BVNW'].fillna('')
    data = data.drop(['Final stem WW', 'Final stem ZNW', 'Final stem BVNW', 'Final stem rest'], axis=1)

    data.to_excel('OUTPUT location')

if __name__== "__main__":
    data = pd.read_excel('INPUT file after tagging')
    data['BT stem'] = data['Word']
    WW_data = data.loc[data['BT tag'].str.match(pat = '(ott)|(ovt)|(vtt)')]
    WW_data = WW_Stemmer(WW_data)
    BVNW_data = data.loc[data['BT tag'].str.match('BVNW')]
    BVNW_data = BVNW_stemmer(BVNW_data)
    ZNW_data = data.loc[data['BT tag'].str.match('ZNW')]
    ZNW_data = ZNW_Stemmer(ZNW_data)
    REST_data = data.loc[~data['BT tag'].str.match(pat = '(ott)|(ovt)|(vtt)|(BVNW)|(ZNW)')]
    REST_data = REST_Stemmer(REST_data)
    Finalise(WW_data, BVNW_data, ZNW_data, REST_data)    
    
    
