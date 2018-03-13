f= open("US_births_1994-2003_CDC_NCHS.csv", 'r')
text= f.read()
split_text=text.split("\n")
split_text[0:10]

def calc_counts(list_list,col):
    if col==1:
        births_per_month=dict()
        for each in list_list:
            month=each[1]
            births=each[4]
            if month in births_per_month:
                    births_per_month[month]+=births
            else:
                births_per_month[month]=births
        return births_per_month 
    elif col==3:
        births_per_day=dict()
        for each in list_list:
            day=each[3]
            births=each[4]
            if day in births_per_day:
                births_per_day[day]+=births
            else:
                births_per_day[day]=births
        return births_per_day
    elif col==2:
        births_per_date=dict()
        for each in list_list:
            date=each[3]
            births=each[4]
            if date in births_per_date:
                births_per_date[date]+=births
            else:
                births_per_date[date]=births
        return births_per_date
    elif col==0:
        births_per_year=dict()
        for each in list_list:
            year=each[3]
            births=each[4]
            if year in births_per_year:
                births_per_year[year]+=births
            else:
                births_per_year[year]=births
        return births_per_year
cdc_year_births=calc_counts(cdc_list,0)
cdc_month_births=calc_counts(cdc_list,1)
cdc_dom_births=calc_counts(cdc_list,2)
cdc_dow_births=calc_counts(cdc_list,3)